#!/usr/bin/env python3
from __future__ import annotations
import re, sys, tomllib
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
  "data/sentences.csv",
  "data/translation.csv"
]
EXPECTED = {"checklist": 280, "rule": 160, "archetype": 56, "boundary": 42, "personal": 13, "decision": 12}

def fail(msg: str):
    print("ERROR:", msg, file=sys.stderr); raise SystemExit(1)

for rel in REQUIRED:
    p = ROOT / rel
    if not p.exists() or p.stat().st_size == 0: fail(f"missing or empty: {rel}")

with (ROOT / "zensical.toml").open("rb") as f: cfg = tomllib.load(f)
project = cfg.get("project", {})
if project.get("site_name") != "考研英语一知识体系": fail("unexpected site_name")

def flatten(v):
    if isinstance(v, str): yield v
    elif isinstance(v, list):
        for x in v: yield from flatten(x)
    elif isinstance(v, dict):
        for x in v.values(): yield from flatten(x)

for rel in flatten(project.get("nav", [])):
    if rel.startswith(("http://", "https://")): continue
    if not (DOCS / rel).exists(): fail(f"missing nav target: {rel}")

text = "\n".join(p.read_text(encoding="utf-8") for p in sorted(DOCS.glob("*.md")))
if "sandbox:/" in text or "/mnt/data/" in text: fail("container-only link leaked")
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
    if len(matches) != EXPECTED[name]: fail(f"{name} count expected {EXPECTED[name]}, got {len(matches)}")
    dup = [k for k,v in Counter(matches).items() if v > 1]
    if dup: fail(f"duplicate {name} ids: {dup[:10]}")

# Validate local Markdown links (anchors are intentionally ignored here).
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
if not re.fullmatch(r"\d+\.\d+\.\d+", version): fail("invalid VERSION")
print("Project validation passed")
for k,v in EXPECTED.items(): print(f"  {k:10s}: {v}")
print(f"  version   : {version}")
