import json
from collections import defaultdict
from app.core.paths import LEARNING_DIR

def append_learning(record: dict) -> None:
    path = LEARNING_DIR / "history.jsonl"
    with path.open("a", encoding="utf-8") as f:
        f.write(json.dumps(record, ensure_ascii=False) + "\n")

def get_learning_stats() -> dict:
    path = LEARNING_DIR / "history.jsonl"
    if not path.exists():
        return {"stats": {}}
    stats = defaultdict(lambda: {"count": 0, "avg_target_lufs": 0.0, "common_issues": {}})
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        row = json.loads(line)
        genre = row.get("genre", "unknown")
        stats[genre]["count"] += 1
        stats[genre]["avg_target_lufs"] += float(row.get("target_lufs", -10.5))
        for issue in row.get("issues", []):
            stats[genre]["common_issues"][issue] = stats[genre]["common_issues"].get(issue, 0) + 1
    for genre, item in stats.items():
        if item["count"]:
            item["avg_target_lufs"] = round(item["avg_target_lufs"] / item["count"], 2)
            item["common_issues"] = dict(sorted(item["common_issues"].items(), key=lambda kv: kv[1], reverse=True))
    return {"stats": stats}
