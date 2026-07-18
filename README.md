# pandatechie rebuild — v9

## What changed this round
- "The log" cards on the homepage now show real thumbnails, pulled from each post's cover_image (falls back to the old category-text treatment if a post has no cover image).
- Hero subtext and "throughline" copy updated to your final wording.

## Heads up on the thumbnails
Two of the three featured posts' images are hotlinked from third-party sites, not pandatechie.in itself:
- "How to Save Time Like a CEO" → i.kym-cdn.com (KnowYourMeme's CDN)
- "The Real Joy of Influencing" → practicebusiness.co.uk

These aren't sites you control, so there's a real chance one of these images disappears or gets blocked from hotlinking at some point without warning — worth keeping an eye on, or swapping in your own image for these two posts eventually (add/replace the `cover_image:` line in that post's frontmatter with your own hosted image URL, rebuild).

## Update loop (unchanged)
Unzip → copy `site-build/`, `content-source/`, `build.py`, `homepage_body.html`, `about_body.html`, `assets/` over your local folder → confirm `git status` shows real changes → commit → push.
