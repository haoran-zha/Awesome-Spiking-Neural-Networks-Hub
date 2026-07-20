# Contributing

Contributions are very welcome — this is a **living** list of Spiking Neural
Network papers, models, hardware, datasets, and tools. Thanks for helping keep
it comprehensive and accurate.

## The one rule: keep both languages in sync

This guide is maintained as **two parallel single-language files**:

- [`README.md`](README.md) — English notes
- [`README.zh-CN.md`](README.zh-CN.md) — Chinese (简体中文) notes

They mirror each other 1:1 — the **same entries, in the same sections, in the
same order**, differing only in the language of the one-line note. Every change
to one file must be mirrored in the other.

## Adding an entry

1. Find the right numbered section (see the Table of Contents).
2. Append the entry using this exact format:

   ```markdown
   - Paper Title (**Venue Year**). \[[paper](url)\]\[[code](url)\]
     > One-line "why it matters" note.
   ```

   - `[code]` is optional — omit the bracket if there is no official code.
   - Add a ★ marker right before the period — `(**Venue Year**) ★.` — only for genuinely seminal / must-read works.
3. Add the **same entry** to the other README with a note in that file's language.
4. Keep entries in rough importance / chronological order within their section.

## Other contributions

- Add a dataset / tool / chip, fix a wrong venue or year, or improve an explanation.
- Fixing links, typos, or formatting is always welcome.

## Submitting

- Open a pull request with a short description of what you added or fixed.
- For large additions (a whole new subsection, many entries), open an issue first
  so we can agree on scope and placement.
- Links are checked automatically on every PR — please make sure new URLs resolve.
