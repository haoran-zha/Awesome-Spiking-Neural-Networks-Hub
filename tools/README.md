# tools/

Utilities for maintaining the repo. Nothing here is required to *read* the
guide — these only regenerate the derived timeline pages.

## `build_timeline.py` — generate the Timeline edition

[`TIMELINE.md`](../TIMELINE.md) and [`TIMELINE.zh-CN.md`](../TIMELINE.zh-CN.md)
are **auto-generated** — do not edit them by hand. They are the chronological
(by-year, newest-first) view of the thematic Hub.

The script combines two sources per language:

| Source | Role |
|---|---|
| [`README.md`](../README.md) / [`README.zh-CN.md`](../README.zh-CN.md) | **Curated picks** — every dated entry, with its "why it matters" note, topic tag, and 🧠 landmark marker, re-sorted by year. |
| [`data/thebrainlab-snapshot.md`](data/thebrainlab-snapshot.md) | **Full-year conference index** (2021–2026), from [TheBrainLab/Awesome-Spiking-Neural-Networks](https://github.com/TheBrainLab/Awesome-Spiking-Neural-Networks), de-duplicated against the picks. |

### Regenerate

```bash
python tools/build_timeline.py     # run from the repo root; writes both TIMELINE files
```

Requires only the Python 3 standard library.

### To add papers

- **A curated, annotated entry** → add it to the right thematic section of
  `README.md` (and its 中文 twin in `README.zh-CN.md`), then re-run the script.
  It will appear under that year's **⭐ Curated picks** with its topic tag.
- **Refreshing the conference index** → re-fetch TheBrainLab's `README.md` into
  `data/thebrainlab-snapshot.md` (keep the provenance header), then re-run.

### Notes

- Dedup matches titles after folding "Spiking Neural Network(s)"/"SNN(s)" and
  dropping acronym parentheticals, plus a long-prefix rule — so the same paper
  written slightly differently in the two sources is not listed twice.
- The `links` CI workflow intentionally checks only the curated files
  (`README*.md`), **not** the generated `TIMELINE*.md`, because the conference
  index carries many unverified upstream links.
