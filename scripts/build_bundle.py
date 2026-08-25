#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
DIST = ROOT / "dist"

ORDER = [
  "00-overview.md",
  "01-vocabulary.md",
  "21-context-vocabulary-lab.md",
  "02-grammar-long-sentences.md",
  "03-cloze.md",
  "04-reading.md",
  "05-new-question-types.md",
  "06-translation.md",
  "20-translation-lab.md",
  "07-writing.md",
  "19-writing-lab.md",
  "08-method-library.md",
  "09-maintenance-loop.md",
  "10-checklists.md",
  "11-rule-cards.md",
  "12-decision-trees.md",
  "13-problem-archetypes.md",
  "14-counterexamples.md",
  "15-personal-links.md",
  "16-review-templates.md",
  "17-project-maintenance.md",
  "18-official-scope.md"
]

version = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
parts = [(DOCS / name).read_text(encoding="utf-8").strip() for name in ORDER]
DIST.mkdir(exist_ok=True)
out = DIST / f"考研英语一知识体系_v{version}.md"
out.write_text("\n\n---\n\n".join(parts) + "\n", encoding="utf-8", newline="\n")
print(f"Wrote {out.relative_to(ROOT)} ({out.stat().st_size:,} bytes)")
