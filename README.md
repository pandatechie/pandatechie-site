# pandatechie.in rebuild — v4

## What changed this round
- Reverted the blog/archive section naming back to "The Log" / "Log" (nav, headers, page titles) — you liked the original name.
- Hero, "What I do", and origins section remain repositioned around writing and facilitation, with project names/numbers removed per your earlier feedback.

## Contents
- `site-build/` — the finished static site. Deploy as-is to Cloudflare Pages, GitHub Pages, Netlify, or Vercel.
- `content-source/archive/*.md` — your 303 posts as portable Markdown + frontmatter.
- `build.py` — regenerates `site-build/` from the content + templates below. Run `python3 build.py` after any edit.
- `parse_xml.py` — regenerates `content-source/` from a fresh WordPress export.
- `homepage_body.html`, `about_body.html` — page content templates, plain HTML — edit text directly.
- `assets/tailwind-config.js`, `assets/site.css`, `assets/site.js` — shared design system and behavior.

## How to run and test locally
cd site-build && python3 -m http.server 8000, then open http://localhost:8000

## Still open
- Real headshot — swap into the placeholder frame in `homepage_body.html` and `about_body.html`.
- Post-detail images still hotlink to the old pandatechie.in / i0.wp.com URLs.
- Point pandatechie.in's DNS at your chosen host when ready to cut over.
- No CMS yet — see chat for options (editing Markdown directly vs. adding a git-backed admin UI like Decap CMS).
