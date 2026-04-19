#!/usr/bin/env bash
set -euo pipefail
sudo apt update
sudo apt install -y ca-certificates curl gnupg lsb-release unzip docker.io docker-compose-v2
sudo systemctl enable --now docker
mkdir -p data/uploads data/outputs data/jobs data/learning references
echo "Instalación base lista."
