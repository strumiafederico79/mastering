# AI Mastering V8.5 PRO REAL

Run:
```bash
cp .env.example .env
mkdir -p data/uploads data/outputs data/jobs data/learning references
docker compose down --remove-orphans
docker compose build --no-cache
docker compose up -d
```

Checks:
```bash
docker compose ps
docker compose logs -f api
docker compose logs -f worker
curl http://127.0.0.1:${WEB_PORT:-8080}/api/health
curl http://127.0.0.1:${WEB_PORT:-8080}/api/plugins
curl http://127.0.0.1:${WEB_PORT:-8080}/api/learning
```

Optional free plugins:
```bash
./scripts/install_free_plugins_ubuntu.sh
./scripts/check_ffmpeg_plugins.sh
```
