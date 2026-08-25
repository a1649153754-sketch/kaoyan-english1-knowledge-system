#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
import tomllib
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"

REQUIRED = [
  "README.md",
  "VERSION",
  "zensical.toml",
  "docs/index.md",
  "docs/00-overview.md",
  "docs/01-vocabulary.md",
  "docs/02-grammar-long-sentences.md",
  "docs/03-cloze.md",
  "docs/04-reading.md",
  "docs/05-new-question-types.md",
  "docs/06-translation.md",
  "docs/07-writing.md",
  "docs/08-method-library.md",
  "docs/09-maintenance-loop.md",
  "docs/10-checklists.md",
  "docs/11-rule-cards.md",
  "docs/12-decision-trees.md",
  "docs/13-problem-archetypes.md",
  "docs/14-counterexamples.md",
  "docs/15-personal-links.md",
  "docs/16-review-templates.md",
  "docs/17-project-maintenance.md",
  "docs/18-official-scope.md",
  "docs/19-writing-lab.md",
  "docs/20-translation-lab.md",
  "docs/21-context-vocabulary-lab.md",
  "data/sentences.csv",
  "data/translation.csv",
]

EXPECTED = {
  "checklist": 280,
  "rule": 160,
  "archetype": 56,
  "boundary": 42,
  "personal": 13,
  "decision": 12,
}


def fail(msg: str) -> None:
    print("ERROR:", msg, file=sys.stderr)
    raise SystemExit(1)


for rel in REQUIRED:
    path = ROOT / rel
    if not path.exists() or path.stat().st_size == 0:
        fail(f"missing or empty: {rel}")

with (ROOT / "zensical.toml").open("rb") as file:
    cfg = tomllib.load(file)

project = cfg.get("project", {})
if project.get("site_name") != "考研英语一知识体系":
    fail("unexpected site_name")


def flatten(value):
    if isinstance(value, str):
        yield value
    elif isinstance(value, list):
        for item in value:
            yield from flatten(item)
    elif isinstance(value, dict):
        for item in value.values():
            yield from flatten(item)


for rel in flatten(project.get("nav", [])):
    if rel.startswith(("http://", "https://")):
        continue
    if not (DOCS / rel).exists():
        fail(f"missing nav target: {rel}")

text = "\n".join(path.read_text(encoding="utf-8") for path in sorted(DOCS.glob("*.md")))
if "sandbox:/" in text or "/mnt/data/" in text:
    fail("container-only link leaked")

patterns = {
    "checklist": r"(?m)^- \[ \] [VCGRNTWM]\d-\d+:",
    "rule": r"(?m)^\| (K-[VCGRNTWM]\d-\d{2}) \|",
    "archetype": r"(?m)^\| (Q-[CRNTW]\d{2}) \|",
    "boundary": r"(?m)^\| (B-[A-Z]\d{2}) \|",
    "personal": r"(?m)^\| (J-\d{2}) \|",
    "decision": r"(?m)^## (D-\d{2}) ",
}

for name, pattern in patterns.items():
    matches = re.findall(pattern, text)
    if len(matches) != EXPECTED[name]:
        fail(f"{name} count expected {EXPECTED[name]}, got {len(matches)}")
    duplicates = [key for key, count in Counter(matches).items() if count > 1]
    if duplicates:
        fail(f"duplicate {name} ids: {duplicates[:10]}")

# Validate local Markdown links; anchors are intentionally ignored.
link_pattern = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
for md in ROOT.rglob("*.md"):
    if ".git" in md.parts:
        continue
    body = md.read_text(encoding="utf-8")
    for target in link_pattern.findall(body):
        target = target.strip().split("#", 1)[0]
        if not target or target.startswith(("http://", "https://", "mailto:")):
            continue
        if not (md.parent / target).resolve().exists():
            fail(f"broken local markdown link in {md.relative_to(ROOT)}: {target}")

version = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
if not re.fullmatch(r"\d+\.\d+\.\d+", version):
    fail("invalid VERSION")

print("Project validation passed")
for key, value in EXPECTED.items():
    print(f"  {key:10s}: {value}")
print("  practice  : 3")
print(f"  version   : {version}")
