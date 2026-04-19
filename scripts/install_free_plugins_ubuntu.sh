#!/usr/bin/env bash
set -euo pipefail
sudo apt update
sudo apt install -y calf-plugins swh-plugins tap-plugins || true
echo "Listo. Validá con ./scripts/check_ffmpeg_plugins.sh"
