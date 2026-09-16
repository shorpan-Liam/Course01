import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
raw_path = root / "data" / "raw-response.json"
data = json.loads(raw_path.read_text(encoding="utf-8"))
checks = {
    "top_level_object": isinstance(data, dict),
    "full_name": data.get("full_name") == "org2AI/ORG2",
    "public": data.get("private") is False,
    "default_branch_string": isinstance(data.get("default_branch"), str),
    "stargazers_count_int": isinstance(data.get("stargazers_count"), int),
    "forks_count_int": isinstance(data.get("forks_count"), int),
    "open_issues_count_int": isinstance(data.get("open_issues_count"), int),
}
for name, passed in checks.items():
    print(f"{name}: {'PASS' if passed else 'FAIL'}")
print("fields:")
for field in ("full_name", "private", "default_branch", "stargazers_count", "forks_count", "open_issues_count", "language"):
    print(f"  {field}={data.get(field)!r} ({type(data.get(field)).__name__})")
if not all(checks.values()):
    raise SystemExit(1)
