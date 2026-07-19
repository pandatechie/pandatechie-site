# pandatechie.in — Site Guide

This is a static site: no database, no admin login, no WordPress-style dashboard.
Everything — every post, every headline, every image — lives as a plain file in
this folder. You edit the files, run one command to rebuild, then push to
GitHub, and Cloudflare puts it live automatically.

This doc covers the four things you'll do most often. Skip to the section you need.

---

## The core loop (applies to everything below)

Every change follows the same four steps:

```bash
cd ~/Desktop/pandatechie        # or wherever your local copy lives
# 1. edit whatever file needs editing
python3 build.py                # 2. regenerate the site into site-build/
# 3. check it locally before shipping
cd site-build && python3 -m http.server 8000
# open http://localhost:8000, click around, Ctrl+C to stop the server
cd ..
git add -A
git commit -m "describe what you changed"
git push                        # 4. Cloudflare redeploys automatically
```

After pushing, hard-refresh the live site (Cmd+Shift+R) to bypass browser cache.
If changes don't show up, run `git status` first — if it says "nothing to
commit," your edits never actually got saved into git, and step 4 silently did
nothing. That's the most common thing that goes wrong.

---

## 1. How to add a new post

1. Go into `content-source/archive/`.
2. Copy any existing `.md` file as a starting template — right-click, duplicate.
3. Rename it to `YYYY-MM-DD-your-post-slug.md` (today's date, and a short
   hyphenated slug based on the title — this becomes the URL).
4. Open it and edit the frontmatter block at the top (between the `---` lines):

   ```
   ---
   title: "Your Post Title"
   date: "2026-07-19"
   slug: "your-post-slug"
   categories: ["Category Name"]
   tags: ["tag1", "tag2"]
   original_url: ""
   cover_image: "https://link-to-an-image.jpg"
   ---
   ```

   - `slug` should match the end of the filename.
   - Leave `original_url` blank for a genuinely new post (it's only there for
     posts migrated from the old WordPress blog).
   - **Don't add `archive: true`** — that flag marks old crypto-era posts;
     leaving it off is what makes a post count as new writing.
   - `cover_image` is optional but recommended — it's what shows as the
     thumbnail if this post ever gets featured on the homepage (see below).

5. Below the second `---`, write the post body in plain Markdown:
   - `## Heading` for section headings
   - `**bold**`, `*italic*`
   - `- item` for bullet lists
   - `[link text](https://...)` for links
   - Just blank lines between paragraphs — no special tags needed.

6. Run the core loop above. The new post will appear at the top of `/archive/`
   automatically (posts are sorted by date, newest first).

### Adding a post to a specific category

The `categories` field in the frontmatter controls this — whatever you put as
the **first** category in that list is the one the post gets filed under on
the archive page.

```
categories: ["AI"]
```

The five categories currently on the site are: `Cryptocurrency`,
`Technology Trends`, `AI`, `Change Management`, and `Uncategorized`. Use the
name exactly as spelled here (case matters) so it lands in the right bucket
instead of accidentally creating a near-duplicate category.

**`AI` and `Change Management` currently show as "Coming soon" cards** on the
archive hub with no post count — the moment you publish a post with
`categories: ["AI"]` (or `"Change Management"`) and rebuild, that category
automatically stops being a placeholder and gets its own live listing page.
Nothing else needs to change — the hub detects this from the post content
itself.

**To add a brand new category** that isn't one of the five above: just use a
new name in `categories`, e.g. `categories: ["Facilitation"]`. It'll get its
own listing page at `/archive/category/facilitation/` automatically — but it
won't show a card on the hub page itself unless you also add it to the
`CATEGORY_META` list near the top of `build_v2.py` (copy the format of an
existing entry: slug, display name, one-line description, and `True`/`False`
for whether it should start as a placeholder).

---

## 2. How to change which posts are featured on the homepage

The homepage's "The log" section shows up to 3 posts. By default it shows the
most recent ones, but you can hand-pick specific posts with a `featured` flag.

1. Open the post's file in `content-source/archive/`.
2. In the frontmatter, add a line: `featured: true`

   ```
   ---
   title: "..."
   date: "..."
   ...
   archive: true
   featured: true
   ---
   ```

3. Repeat for up to 3 posts total. **Only the first 3 files (alphabetically,
   which for these filenames means oldest-dated first) with `featured: true`
   will show** — if you mark more than 3, the extras are ignored, so keep it
   to exactly the ones you want.
4. To un-feature a post, just delete that line.
5. Run the core loop.

If no posts are marked featured, it falls back automatically to the 3 most
recent posts.

---

## 3. How to change images

### The homepage hero photo
1. Put your new image file into the `assets/` folder (any filename, e.g.
   `assets/new-photo.jpg`).
2. Open `homepage_body.html`, find the line with
   `<img src="/assets/raghav-hero.jpg" ...>`, and change the filename to
   match your new file.
3. Run the core loop.

*Tip: keep the photo roughly portrait-oriented (taller than wide) since it
sits in a 4:5 frame — a very wide/landscape photo will get cropped hard on
the sides. If you send me a photo, I'll crop and size it properly; if you're
doing it yourself, aim for something already close to that shape.*

### A post's thumbnail / cover image
1. Open the post's file in `content-source/archive/`.
2. Change the `cover_image: "..."` line to a new image URL (or add the line
   if it's missing).
3. Run the core loop. This image is used both as the thumbnail if the post
   gets featured on the homepage, and at the top of the post's own page.

### Images inside a post's body
Add a line in the Markdown body wherever you want the image to appear:
```
![](https://link-to-image.jpg)
```
Local images work too — drop the file in `assets/`, then reference it as
`![](/assets/filename.jpg)`.

---

## 4. How to change any copy, anywhere

Where a piece of text lives depends on what it is:

| What you want to change | File to edit |
|---|---|
| Homepage headline, hero text, "What I do" cards, "The route so far" text, CTA section | `homepage_body.html` |
| About page text | `about_body.html` |
| Nav bar labels ("Home", "Log", "About"), site name in the header, footer text, social icon links | `build_v2.py` — search for the text you want to change (it's plain HTML inside a Python string, same idea as the other files) |
| A specific post's title or body | The post's `.md` file in `content-source/archive/` |

**For `homepage_body.html` and `about_body.html`:** these are plain HTML
files. Open in any text editor (TextEdit, VS Code, even Notes if you must),
find the sentence you want to change using Cmd+F, edit the words between the
tags, leave the `class="..."` bits alone, save.

**For `build_v2.py`:** this is Python, but the text you'd want to change
(nav labels, footer copy) is just sitting in plain quotes inside HTML
strings — search for the words, change them, don't touch anything outside
the quotes.

Run the core loop after any of these.

---

## Quick reference: file map

```
pandatechie/
├── build_v2.py            ← the build script + nav/footer text (run as `build.py`)
├── homepage_body.html      ← homepage content
├── about_body.html         ← about page content
├── content-source/
│   └── archive/*.md        ← every post, one file each
├── assets/
│   ├── raghav-hero.jpg     ← homepage photo
│   ├── site.css / site.js / tailwind-config.js   ← design system, don't touch unless asked
├── site-build/              ← the generated output — never edit this directly,
│                              it gets overwritten every time you run build.py
│   └── archive/
│       ├── index.html            ← category hub (cards)
│       ├── category/<slug>/      ← one listing per category, auto-generated
│       ├── all/                  ← every post, chronological, no category filter
│       └── <post-slug>/          ← each individual post's page
```

---

## When to come back and ask

This covers routine content changes. Come back if you want to:
- Change the visual design, layout, or colors
- Add a new type of page (not a post)
- Set up a proper CMS with a login/form instead of editing files
- Anything that isn't "change some text" or "change an image"
