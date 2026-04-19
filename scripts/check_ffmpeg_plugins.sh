#!/usr/bin/env bash
set -euo pipefail
ffmpeg -filters | grep -E 'ladspa|lv2' || true
find /usr/lib -maxdepth 3 \( -path "*ladspa*" -o -path "*lv2*" \) 2>/dev/null | head -100 || true
