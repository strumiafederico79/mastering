import os, shutil, subprocess

def ffmpeg_supports(name: str) -> bool:
    try:
        res = subprocess.run(["ffmpeg", "-filters"], capture_output=True, text=True, check=False)
        return name in (res.stdout or "")
    except Exception:
        return False

def scan_plugins() -> dict:
    ladspa_paths = ["/usr/lib/ladspa", "/usr/local/lib/ladspa"]
    lv2_paths = ["/usr/lib/lv2", "/usr/local/lib/lv2"]
    return {
        "ffmpeg": shutil.which("ffmpeg") is not None,
        "ladspa_filter": ffmpeg_supports("ladspa"),
        "lv2_filter": ffmpeg_supports("lv2"),
        "ladspa_path_exists": any(os.path.isdir(p) for p in ladspa_paths),
        "lv2_path_exists": any(os.path.isdir(p) for p in lv2_paths),
        "carla_exists": shutil.which("carla") is not None,
        "reaper_exists": shutil.which("reaper") is not None,
        "reaper_plugin_paths": [p for p in ladspa_paths + lv2_paths if os.path.isdir(p)],
        "backend_selected": "native",
    }
