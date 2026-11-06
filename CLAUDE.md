# CLAUDE.md

You're helping a scientist learn Claude Code at the AEO26 workshop. Many don't write code: they
describe what they want, you build and run it, and they check the results.

## Rules

- Say in plain English what you're about to do, and define any technical term. End every task with
  three bullets: what changed, where the outputs are, and how you checked them.
- Ask before you delete files or change anything outside this repo (installing packages is fine).
- Read `data/README.md` before you use `data/`: values are scaled, nodata differs between files,
  and glider records are latitude/longitude. `data/` is read-only; put downloads in `downloads/`.
- Don't change `CHECK_VALUES.md`, `SETUP.md`, `WORKBOOK.md`, `examples/` or `presenters/`, and never
  copy the example pictures. If your numbers differ from `CHECK_VALUES.md`, explain why.
- Check your work: run the code, look at every figure, and print values that show units and ranges.
- Figures: colour-blind-safe palettes (diverging, centred on zero, for change); label units and the
  year on every panel; give maps a scale bar and a true-north arrow.
- Commit each step once it works, then push.
