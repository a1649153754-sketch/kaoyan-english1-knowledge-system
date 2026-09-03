# AGENTS.md

## Scope

This file applies to the entire repository. A more specific `AGENTS.md` may override it only inside its own subtree.

## Project purpose

Maintain a versioned, searchable, copyright-safe knowledge system for China’s Graduate Entrance Examination English I. The repository connects language knowledge, task decisions, evidence, revision, and spaced review; it is not a collection of copied passages or generic templates.

## Read before editing

1. `README.md`
2. `ROADMAP.md`
3. `CONTRIBUTING.md`
4. `docs/17-project-maintenance.md`
5. `docs/CODEX_HANDOFF.md`

## Non-negotiable contracts

- Preserve the stable `V / G / C / R / N / T / W / M` node system and the separate `K / Q / B / J / D` resource namespaces.
- Objective-question notes must identify a minimal evidence span and the distractor mechanism; do not store only an answer letter.
- Translation and writing improvements must use first draft → diagnosis → second draft → transfer. Do not add source-unknown “universal templates” that the learner cannot explain.
- Do not copy full exam passages, complete questions, official or third-party solution text, paid-course material, or long copyrighted excerpts. Use original summaries, short evidence notes, and source locators.
- Personal accuracy, timing, error text, and review schedules should move into a local private layer before v1.2 data work. Do not place personal records in public Git, Pages, Releases, or pull requests.
- Generated bundles should be rebuilt from canonical source files rather than hand-edited.

## Required checks

Run from the repository root:

```bash
python scripts/validate_project.py
python scripts/build_bundle.py
zensical build --clean --strict
git diff --check
```

When adding a private-data layer, schema validation, leak detection, migration tests, and deterministic local-report tests become mandatory.

## Editing workflow

1. Inspect current `VERSION`, branch, and `git status --short --branch`.
2. Use a dedicated branch and one milestone per branch.
3. Update canonical docs or data first, then rebuild derived output.
4. Add validation whenever a new ID type, data field, privacy boundary, or generated report is introduced.
5. Review the diff for copied source text, unsupported language claims, broken links, ID drift, and accidental personal data.
6. Update release metadata only when the change is ready to ship.

## Current direction

The next milestone is v1.2: personal exam mapping, reading-error taxonomy, repeated translation/writing error extraction, and a local private data layer. Build the privacy boundary before importing any personal records.

## Definition of done

A change is complete only when the repository validates and builds, evidence and distractor logic are explicit, copyright and privacy boundaries remain intact, and the final report lists modified files, checks run, known limits, and the next recommended action.
