"""Fetch public teaching data and render a reproducible observation chart."""

import csv
import argparse
import hashlib
import json
import os
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from urllib.request import Request, urlopen

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
DEST = ROOT / "materials" / "baseline"
URL = "https://api.github.com/repos/org2AI/ORG2"
FIELDS = ["stargazers_count", "forks_count", "open_issues_count"]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--git-credential-user", help="Use an existing github.com Git credential without displaying or saving it")
    args = parser.parse_args()
    DEST.mkdir(parents=True, exist_ok=True)
    headers = {"Accept": "application/vnd.github+json", "User-Agent": "learn2ai-course-materials"}
    if args.git_credential_user:
        if not args.git_credential_user.replace("-", "").isalnum():
            raise ValueError("Invalid GitHub username")
        credentials = subprocess.run(["git", "credential", "fill"],
            input=f"protocol=https\nhost=github.com\nusername={args.git_credential_user}\n\n",
            text=True, capture_output=True, check=True,
            env={**os.environ, "GCM_INTERACTIVE": "Never", "GIT_TERMINAL_PROMPT": "0"})
        fields = dict(line.split("=", 1) for line in credentials.stdout.splitlines() if "=" in line)
        headers["Authorization"] = "Bearer " + fields["password"]
    request = Request(URL, headers=headers)
    with urlopen(request, timeout=30) as response:
        raw = response.read(1024 * 1024 + 1)
        status = response.status
        content_type = response.headers.get("Content-Type")
    if len(raw) > 1024 * 1024:
        raise ValueError("Response exceeds 1 MiB")
    data = json.loads(raw)
    values = [data[field] for field in FIELDS]
    if any(type(value) is not int or value < 0 for value in values):
        raise ValueError("Expected non-negative integer counters")
    fetched_at = datetime.now(timezone.utc).isoformat()
    (DEST / "response.json").write_bytes(raw)
    provenance = {"url": URL, "fetchedAt": fetched_at, "httpStatus": status, "contentType": content_type,
                  "authenticatedRequest": bool(args.git_credential_user),
                  "sha256": hashlib.sha256(raw).hexdigest(), "purpose": "teacher_material_only"}
    (DEST / "provenance.json").write_text(json.dumps(provenance, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    with (DEST / "counters.csv").open("w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["field", "value"])
        writer.writerows(zip(FIELDS, values))
    fig, ax = plt.subplots(figsize=(10, 5), layout="constrained")
    bars = ax.barh(FIELDS, values, color=["#335c67", "#52796f", "#a67c52"])
    ax.bar_label(bars, padding=5)
    ax.set_xlim(0, max(max(values), 1) * 1.2)
    ax.set_xlabel("Count from one API response")
    ax.set_title("org2AI/ORG2: three observed counters", loc="left", weight="bold")
    ax.spines[["top", "right"]].set_visible(False)
    fig.text(0.01, -0.05, f"Fetched: {fetched_at}\nSource: {URL}\nTeaching baseline only. Counts do not establish quality or causation.", fontsize=9)
    fig.savefig(DEST / "counters.png", dpi=160, bbox_inches="tight")
    plt.close(fig)
    print(json.dumps({"httpStatus": status, "fetchedAt": fetched_at, "fields": dict(zip(FIELDS, values)), "sha256": provenance["sha256"]}))


if __name__ == "__main__":
    main()
