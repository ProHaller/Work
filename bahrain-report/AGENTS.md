# Repository Guidelines

## Project Structure & Module Organization
- `main.typ` is the entrypoint, pulling layout helpers from `report.typ` and data loaders from `data.typ`; compiled artifacts (`main.pdf`, `report.pdf`, `titlepage.pdf`) are checked in for reference.
- `data/*.csv` stores production, GDP, and population inputs; keep column names stable or adjust selectors in `data.typ` when changing schema.
- `assets/` holds brand art and logos; keep vector sources (`*.svg`) with any derived raster versions.
- `target/` and other generated previews should stay lightweight; commit only outputs that illustrate meaningful changes.

## Build, Test, and Development Commands
- `typst compile main.typ main.pdf` — full report build; fails fast on missing fonts or data files.
- `typst watch main.typ --root .` — live rebuild while editing to catch layout and data issues early.
- `typst compile titlepage.typ titlepage.pdf` — regenerate the title page in isolation.
- `typst compile report.typ report.pdf` — sanity-check the base template without full content.

## Coding Style & Naming Conventions
- Typst code uses two-space indentation and concise blocks for readability.
- Prefer `lower_snake_case` for helpers/variables (`usd_oku_en`, `framify`); reserve upper snake for constants if added.
- Reuse shared helpers in `report.typ`/`data.typ` before introducing new globals; keep figures annotated with clear captions plus `kind`/`supplement` metadata to preserve numbering.
- Keep imports (`@preview/echarm`, `@preview/hydra`, `@preview/blinky`) version-pinned unless intentionally upgrading.

## Testing Guidelines
- Treat a clean `typst compile` as the primary test signal; fix warnings immediately.
- Manually review regenerated `main.pdf` for chart labels, Japanese typography (YuMincho), and pagination; spot-check data ranges after CSV edits.
- When adjusting datasets or chart options, run a short `typst watch` session to confirm rendering and scaling.

## Commit & Pull Request Guidelines
- Commit messages are short and imperative (e.g., `Add GDP series`, `Tweak titlepage spacing`); avoid verbose prefixes beyond a brief scope tag.
- PRs should summarize scope, list affected sections/pages, and attach updated `main.pdf` or key figure screenshots.
- Link issues and cite data sources when altering `data/`; call out font or package dependency changes in the description.

## Security & Configuration Tips
- Do not commit proprietary datasets or credentials; only public-source CSVs belong in `data/`.
- Keep new assets license-compatible and optimized (prefer SVG over large PNGs); avoid embedding unlicensed fonts.
- Note required local fonts in PRs so reviewers can reproduce the build.
