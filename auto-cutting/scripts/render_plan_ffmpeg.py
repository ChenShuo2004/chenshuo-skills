#!/usr/bin/env python3
"""Render a simple auto-cutting JSON plan with FFmpeg.

The script is intentionally dependency-free except for ffmpeg/ffprobe on PATH.
It trims clips, normalizes their canvas/fps/audio, concatenates them, optionally
mixes BGM and burns SRT subtitles, then writes a JSON verification report.
"""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Any


def fmt_seconds(value: float) -> str:
    return f"{value:.3f}".rstrip("0").rstrip(".")


def resolve_path(value: str, base_dir: Path) -> Path:
    path = Path(value).expanduser()
    if not path.is_absolute():
        path = base_dir / path
    return path.resolve()


def load_plan(plan_path: Path) -> dict[str, Any]:
    with plan_path.open("r", encoding="utf-8-sig") as handle:
        plan = json.load(handle)
    if not isinstance(plan, dict):
        raise ValueError("Plan JSON must be an object.")
    return plan


def ensure_tool(name: str, override: str | None = None) -> str:
    if override:
        candidate = shutil.which(override) or override
    else:
        candidate = shutil.which(name)
    if not candidate:
        raise RuntimeError(f"Required tool not found on PATH: {name}")
    return candidate


def run_command(command: list[str], report: dict[str, Any]) -> None:
    item: dict[str, Any] = {"command": command}
    result = subprocess.run(command, text=True, capture_output=True)
    item["returncode"] = result.returncode
    item["stderrTail"] = result.stderr[-4000:]
    report.setdefault("commands", []).append(item)
    if result.returncode != 0:
        raise RuntimeError("FFmpeg command failed. See report commands stderrTail.")


def ffprobe(ffprobe_bin: str, media_path: Path) -> dict[str, Any]:
    command = [
        ffprobe_bin,
        "-v",
        "error",
        "-print_format",
        "json",
        "-show_streams",
        "-show_format",
        str(media_path),
    ]
    result = subprocess.run(command, text=True, capture_output=True)
    if result.returncode != 0:
        raise RuntimeError(f"ffprobe failed for {media_path}: {result.stderr.strip()}")
    return json.loads(result.stdout)


def media_has_stream(probe: dict[str, Any], stream_type: str) -> bool:
    return any(stream.get("codec_type") == stream_type for stream in probe.get("streams", []))


def positive_int(value: Any, name: str) -> int:
    number = int(value)
    if number <= 0:
        raise ValueError(f"{name} must be positive.")
    return number


def positive_float(value: Any, name: str) -> float:
    number = float(value)
    if number <= 0:
        raise ValueError(f"{name} must be positive.")
    return number


def prepare_plan(plan: dict[str, Any], plan_path: Path) -> dict[str, Any]:
    base_dir = plan_path.parent
    target = dict(plan.get("target") or {})
    target["width"] = positive_int(target.get("width", 1080), "target.width")
    target["height"] = positive_int(target.get("height", 1920), "target.height")
    target["fps"] = positive_int(target.get("fps", 30), "target.fps")
    target["crf"] = int(target.get("crf", 20))
    target["preset"] = str(target.get("preset", "veryfast"))
    target["audioBitrate"] = str(target.get("audioBitrate", "192k"))

    if not plan.get("output"):
        raise ValueError("Plan must include output.")
    output = resolve_path(str(plan["output"]), base_dir)

    clips = plan.get("clips")
    if not isinstance(clips, list) or not clips:
        raise ValueError("Plan must include at least one clip.")

    prepared_clips: list[dict[str, Any]] = []
    for index, clip in enumerate(clips):
        if not isinstance(clip, dict):
            raise ValueError(f"clips[{index}] must be an object.")
        if not clip.get("source"):
            raise ValueError(f"clips[{index}].source is required.")
        source = resolve_path(str(clip["source"]), base_dir)
        if not source.exists():
            raise FileNotFoundError(f"Clip source does not exist: {source}")
        in_sec = float(clip.get("inSec", 0))
        if in_sec < 0:
            raise ValueError(f"clips[{index}].inSec cannot be negative.")
        if "outSec" in clip:
            out_sec = float(clip["outSec"])
            duration = out_sec - in_sec
        elif "durationSec" in clip:
            duration = positive_float(clip["durationSec"], f"clips[{index}].durationSec")
            out_sec = in_sec + duration
        else:
            raise ValueError(f"clips[{index}] must include outSec or durationSec.")
        if duration <= 0:
            raise ValueError(f"clips[{index}] duration must be positive.")
        prepared = dict(clip)
        prepared["_source"] = source
        prepared["_inSec"] = in_sec
        prepared["_outSec"] = out_sec
        prepared["_durationSec"] = duration
        prepared_clips.append(prepared)

    prepared_bgm = None
    if plan.get("bgm"):
        bgm = dict(plan["bgm"])
        if not bgm.get("source"):
            raise ValueError("bgm.source is required when bgm is present.")
        source = resolve_path(str(bgm["source"]), base_dir)
        if not source.exists():
            raise FileNotFoundError(f"BGM source does not exist: {source}")
        volume = float(bgm.get("volume", 0.18))
        if volume < 0:
            raise ValueError("bgm.volume cannot be negative.")
        bgm["_source"] = source
        bgm["_volume"] = volume
        prepared_bgm = bgm

    prepared_subtitles = None
    if plan.get("subtitles"):
        subtitles = dict(plan["subtitles"])
        if not subtitles.get("srt"):
            raise ValueError("subtitles.srt is required when subtitles is present.")
        srt = resolve_path(str(subtitles["srt"]), base_dir)
        if not srt.exists():
            raise FileNotFoundError(f"Subtitle file does not exist: {srt}")
        subtitles["_srt"] = srt
        prepared_subtitles = subtitles

    report_path = resolve_path(str(plan.get("report") or output.with_suffix(".report.json")), base_dir)
    work_dir = None
    if plan.get("workDir"):
        work_dir = resolve_path(str(plan["workDir"]), base_dir)

    return {
        "target": target,
        "clips": prepared_clips,
        "bgm": prepared_bgm,
        "subtitles": prepared_subtitles,
        "output": output,
        "report": report_path,
        "workDir": work_dir,
        "keepWorkDir": bool(plan.get("keepWorkDir", False)),
    }


def canvas_filter(target: dict[str, Any]) -> str:
    width = target["width"]
    height = target["height"]
    fps = target["fps"]
    return (
        f"scale={width}:{height}:force_original_aspect_ratio=decrease,"
        f"pad={width}:{height}:(ow-iw)/2:(oh-ih)/2,"
        f"setsar=1,fps={fps},format=yuv420p"
    )


def render_clip(
    ffmpeg_bin: str,
    ffprobe_bin: str,
    clip: dict[str, Any],
    index: int,
    target: dict[str, Any],
    work_dir: Path,
    report: dict[str, Any],
) -> Path:
    source = clip["_source"]
    duration = clip["_durationSec"]
    probe = ffprobe(ffprobe_bin, source)
    if not media_has_stream(probe, "video"):
        raise RuntimeError(f"Clip has no video stream: {source}")
    has_audio = media_has_stream(probe, "audio")
    output = work_dir / f"clip_{index:03d}.mp4"
    command = [
        ffmpeg_bin,
        "-hide_banner",
        "-y",
        "-ss",
        fmt_seconds(clip["_inSec"]),
        "-t",
        fmt_seconds(duration),
        "-i",
        str(source),
    ]
    if has_audio:
        command.extend(
            [
                "-map",
                "0:v:0",
                "-map",
                "0:a:0",
                "-vf",
                canvas_filter(target),
                "-af",
                "aresample=48000,aformat=channel_layouts=stereo",
            ]
        )
    else:
        command.extend(
            [
                "-f",
                "lavfi",
                "-t",
                fmt_seconds(duration),
                "-i",
                "anullsrc=channel_layout=stereo:sample_rate=48000",
                "-map",
                "0:v:0",
                "-map",
                "1:a:0",
                "-vf",
                canvas_filter(target),
            ]
        )
    command.extend(
        [
            "-c:v",
            "libx264",
            "-preset",
            target["preset"],
            "-crf",
            str(target["crf"]),
            "-c:a",
            "aac",
            "-b:a",
            target["audioBitrate"],
            "-shortest",
            str(output),
        ]
    )
    run_command(command, report)
    return output


def concat_file_path(path: Path) -> str:
    return str(path).replace("\\", "/").replace("'", "'\\''")


def concat_clips(ffmpeg_bin: str, clip_paths: list[Path], work_dir: Path, report: dict[str, Any]) -> Path:
    concat_path = work_dir / "concat.txt"
    concat_path.write_text(
        "\n".join(f"file '{concat_file_path(path)}'" for path in clip_paths) + "\n",
        encoding="utf-8",
    )
    output = work_dir / "joined.mp4"
    command = [
        ffmpeg_bin,
        "-hide_banner",
        "-y",
        "-f",
        "concat",
        "-safe",
        "0",
        "-i",
        str(concat_path),
        "-c",
        "copy",
        str(output),
    ]
    run_command(command, report)
    return output


def ffmpeg_filter_path(path: Path) -> str:
    text = path.as_posix().replace("\\", "/")
    text = text.replace(":", "\\:").replace("'", "\\'").replace(",", "\\,")
    return f"'{text}'"


def render_final(
    ffmpeg_bin: str,
    joined: Path,
    output: Path,
    target: dict[str, Any],
    bgm: dict[str, Any] | None,
    subtitles: dict[str, Any] | None,
    report: dict[str, Any],
) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    if not bgm and not subtitles:
        shutil.copyfile(joined, output)
        report.setdefault("commands", []).append({"action": "copy", "from": str(joined), "to": str(output)})
        return

    command = [ffmpeg_bin, "-hide_banner", "-y", "-i", str(joined)]
    filters: list[str] = []
    if bgm:
        command.extend(["-stream_loop", "-1", "-i", str(bgm["_source"])])
        filters.append(f"[1:a]volume={bgm['_volume']}[bgm]")
        filters.append("[0:a][bgm]amix=inputs=2:duration=first:dropout_transition=2[a]")
    if subtitles:
        filters.append(f"[0:v]subtitles={ffmpeg_filter_path(subtitles['_srt'])}[v]")
    if filters:
        command.extend(["-filter_complex", ";".join(filters)])

    command.extend(["-map", "[v]" if subtitles else "0:v:0"])
    command.extend(["-map", "[a]" if bgm else "0:a:0?"])
    if subtitles:
        command.extend(["-c:v", "libx264", "-preset", target["preset"], "-crf", str(target["crf"])])
    else:
        command.extend(["-c:v", "copy"])
    command.extend(["-c:a", "aac", "-b:a", target["audioBitrate"], "-shortest", str(output)])
    run_command(command, report)


def write_report(path: Path, report: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")


def execute(args: argparse.Namespace) -> int:
    plan_path = Path(args.plan).expanduser().resolve()
    plan = load_plan(plan_path)
    prepared = prepare_plan(plan, plan_path)
    report: dict[str, Any] = {
        "status": "checking" if args.check_only else "running",
        "plan": str(plan_path),
        "output": str(prepared["output"]),
        "clips": [
            {
                "source": str(clip["_source"]),
                "inSec": clip["_inSec"],
                "outSec": clip["_outSec"],
                "durationSec": clip["_durationSec"],
                "role": clip.get("role"),
            }
            for clip in prepared["clips"]
        ],
        "target": prepared["target"],
    }

    ffmpeg_bin = ensure_tool("ffmpeg", args.ffmpeg)
    ffprobe_bin = ensure_tool("ffprobe", args.ffprobe)

    for clip in prepared["clips"]:
        probe = ffprobe(ffprobe_bin, clip["_source"])
        if not media_has_stream(probe, "video"):
            raise RuntimeError(f"Clip has no video stream: {clip['_source']}")

    if args.check_only:
        report["status"] = "ok"
        write_report(prepared["report"], report)
        print(json.dumps(report, ensure_ascii=False, indent=2))
        return 0

    output = prepared["output"]
    output.parent.mkdir(parents=True, exist_ok=True)
    if prepared["workDir"]:
        work_dir = prepared["workDir"]
        work_dir.mkdir(parents=True, exist_ok=True)
        cleanup = False
    else:
        work_dir = Path(tempfile.mkdtemp(prefix="auto_cutting_", dir=str(output.parent)))
        cleanup = not prepared["keepWorkDir"]

    try:
        rendered_clips = [
            render_clip(ffmpeg_bin, ffprobe_bin, clip, index, prepared["target"], work_dir, report)
            for index, clip in enumerate(prepared["clips"], start=1)
        ]
        joined = concat_clips(ffmpeg_bin, rendered_clips, work_dir, report)
        render_final(
            ffmpeg_bin,
            joined,
            output,
            prepared["target"],
            prepared["bgm"],
            prepared["subtitles"],
            report,
        )
        if not output.exists() or output.stat().st_size == 0:
            raise RuntimeError(f"Output was not created or is empty: {output}")
        final_probe = ffprobe(ffprobe_bin, output)
        report["final"] = {
            "path": str(output),
            "bytes": output.stat().st_size,
            "durationSec": float(final_probe.get("format", {}).get("duration", 0) or 0),
        }
        report["status"] = "ok"
        return 0
    except Exception as exc:
        report["status"] = "failed"
        report["error"] = str(exc)
        raise
    finally:
        if cleanup and work_dir.exists():
            shutil.rmtree(work_dir, ignore_errors=True)
        write_report(prepared["report"], report)


def main() -> int:
    parser = argparse.ArgumentParser(description="Render an auto-cutting JSON plan with FFmpeg.")
    parser.add_argument("plan", help="Path to render-plan JSON.")
    parser.add_argument("--check-only", action="store_true", help="Validate the plan and tools without rendering.")
    parser.add_argument("--ffmpeg", help="Optional ffmpeg binary path or command name.")
    parser.add_argument("--ffprobe", help="Optional ffprobe binary path or command name.")
    args = parser.parse_args()
    try:
        return execute(args)
    except Exception as exc:  # noqa: BLE001 - CLI should return a concise actionable error.
        print(f"error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
