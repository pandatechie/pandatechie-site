# What's new — animations & panda personality

## Restored
- **Count-up stat numbers** — the homepage's archive-post/cohort/industry
  counts now animate upward when scrolled into view. This existed in the very
  first mockup, got dropped during the Stitch redesign, and is now back site-wide
  via `data-count` / `data-suffix` attributes — reusable anywhere you want a
  number to count up, not just the homepage.

## New
- **Magnetic buttons** — the two primary CTA buttons on the homepage now pull
  gently toward your cursor when you hover near them (`.magnetic` class in
  `site.js` — add that class to any other button to get the same effect).
  Automatically disabled on touch devices.
- **Panda easter egg** — click the "pandatechie" wordmark in the nav 5 times
  fast and bamboo leaves / panda emoji fall down the screen. Purely
  decorative, self-contained, doesn't affect layout or load unless triggered.
- **Custom favicon** — a minimal geometric panda face (`assets/favicon.svg`),
  matches the dark/coral palette, shows in every browser tab.
- **Custom scrollbar** — thin, dark track, coral thumb on hover, matches the
  rest of the theme instead of the browser default.
- **Panda-themed 404 page** (`site-build/404.html`) — "This page wandered off
  into the bamboo," with a way back home.

## One thing you need to do for the 404 page to actually work

Cloudflare Workers needs to be told to serve this file when someone hits a
broken link. Open `wrangler.jsonc` in your repo root and add
`not_found_handling` under `assets`:

```jsonc
{
  "name": "pandatechie-site",
  "compatibility_date": "2026-07-19",
  "assets": {
    "directory": "site-build",
    "not_found_handling": "404-page"
  }
}
```

Without this line, broken links will still work (Cloudflare has a generic
fallback), they just won't show your custom panda page.
