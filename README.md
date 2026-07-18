# pandatechie rebuild — v7

## What changed this round
- New headshot: upscaled 2x with sharpening, cropped to the hero frame.
- Hero headline: "I build systems for enterprises and write about what breaks them."
- "The log" on the homepage now shows 3 hand-picked, non-branded, generic-strategic posts (via the `featured: true` flag): Delta 4 framework / public blockchain adoption, saving time like a CEO, and the real joy of influencing. Swap these anytime — see below.

## How to make changes yourself
(same workflow as before: edit → `python3 build.py` → check locally → git commit/push)

### Change the featured posts
Open the relevant file in `content-source/archive/`, find or add `featured: true` under `archive: true` in the frontmatter. Only the first 3 posts with that flag (in file order) will show — remove the line to un-feature one.

### Swap the photo again
Replace `assets/raghav-hero.jpg` with a new image of the same filename (or update the filename referenced in `homepage_body.html`), then rebuild.

### Everything else
See the v6 README section carried over below — text edits, new posts, etc.
