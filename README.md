# Toddler Storybook Generator — Jungle Book

Two illustrated picture books for ages 2–3, built with Python (Pillow) and exported as multi-page PDFs.

1. **English (rhyming)** — *Mowgli's Jungle Day*: short bounce-along lines, sound words, goodnight ending.
2. **Roman Urdu (storyline)** — *Mowgli aur Jungle ka Ghar*: a longer moral story (listening to elders, honesty, kindness) written in Roman Urdu.

## Layout

```
english/
  build.py                    # composites page art + text → PDF
  jungle_book_toddler.pdf     # finished book (16 pages)
roman-urdu/
  story.py                    # page text + morals
  build.py                    # composites pages → PDF
  jungle_book_urdu.pdf        # finished book (22 pages)
previews/
  english_cover.jpg
  english_character_sheet.jpg
  urdu_cover.jpg
```

## Requirements

- Python 3.10+
- Pillow (`pip install pillow`)
- A TrueType font with weight axes (the scripts expect Fredoka under `/usr/share/fonts/...`; change the path in `build.py` if needed)

## Rebuild

The checked-in PDFs are ready to open. Full rebuild needs the original illustration assets (hash-named JPGs that `build.py` loads from a directory you pass as `argv[1]`). Those source assets are not included here — only the finished PDFs and cover previews.

```bash
# English (once asset dir is available)
cd english && python3 build.py /path/to/english-assets

# Roman Urdu
cd roman-urdu && python3 build.py /path/to/urdu-assets
```

## Scope note

A third personalised book (family likenesses) was made in the same session and is **not** in this repo.

## Notes

- Personal / educational project, not a commercial Disney adaptation claim — characters are used in a home storybook context.
- Intermediate per-page JPGs were left out to keep the repo small; open the PDFs for the full books.
