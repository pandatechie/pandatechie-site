import os, json, re, glob, math, shutil
import markdown as md_lib
from datetime import datetime

SITE_DIR = '/home/claude/site'
CONTENT_ARCHIVE = os.path.join(SITE_DIR, 'content/archive')
OUT = os.path.join(SITE_DIR, 'dist')
POSTS_PER_PAGE = 12

os.makedirs(OUT, exist_ok=True)
os.makedirs(os.path.join(OUT, 'archive'), exist_ok=True)

TAILWIND_CONFIG = open(os.path.join(SITE_DIR, 'assets/tailwind-config.js'), encoding='utf-8').read()
SITE_CSS = open(os.path.join(SITE_DIR, 'assets/site.css'), encoding='utf-8').read()
SITE_JS = open(os.path.join(SITE_DIR, 'assets/site.js'), encoding='utf-8').read()

# Ordered list of categories shown on the archive hub. "placeholder" categories
# have no posts yet but still get a card, marked "Coming soon" — add posts to
# them the normal way (matching `categories` in a post's frontmatter) and they
# stop being placeholders automatically.
CATEGORY_META = [
    ("cryptocurrency", "Cryptocurrency", "Bitcoin, blockchain, and the wider crypto ecosystem — the site's original beat.", False),
    ("technology-trends", "Technology Trends", "Consumer tech, apps, and everyday digital life.", False),
    ("ai", "AI", "Applied AI in the enterprise — practical notes, not hype.", True),
    ("change-management", "Change Management", "How organisations actually adopt new systems and processes.", True),
    ("uncategorized", "Uncategorized", "Early posts and one-offs that don't fit elsewhere.", False),
]

def slugify_category(name):
    s = re.sub(r'[^a-z0-9]+', '-', name.lower()).strip('-')
    return s

def category_of(p):
    cats = p.get('categories') or []
    return cats[0] if cats else 'Uncategorized'

def parse_frontmatter(text):
    parts = text.split('---', 2)
    fm_raw = parts[1]
    body = parts[2]
    fm = {}
    for line in fm_raw.strip().split('\n'):
        if ':' not in line:
            continue
        key, val = line.split(':', 1)
        key = key.strip()
        val = val.strip()
        if val.startswith('[') and val.endswith(']'):
            fm[key] = json.loads(val)
        elif val.startswith('"') and val.endswith('"'):
            fm[key] = val[1:-1]
        elif val in ('true', 'false'):
            fm[key] = (val == 'true')
        else:
            fm[key] = val
    return fm, body.strip()

def load_posts():
    posts = []
    for path in glob.glob(os.path.join(CONTENT_ARCHIVE, '*.md')):
        with open(path, encoding='utf-8') as f:
            text = f.read()
        fm, body = parse_frontmatter(text)
        fm['body_md'] = body
        fm['html'] = md_lib.markdown(body, extensions=['fenced_code', 'tables'])
        excerpt_src = re.sub(r'[#*`>_]', '', body)
        fm['excerpt'] = (excerpt_src.strip()[:160] + '…') if len(excerpt_src) > 160 else excerpt_src.strip()
        posts.append(fm)
    posts.sort(key=lambda p: p.get('date', ''), reverse=True)
    return posts

def page_shell(title, body, description="Raghav — writer and facilitator, cross-industry.", active="home"):
    def nav_link(href, label, key):
        if key == active:
            return f'<a href="{href}" class="font-body-md text-body-md text-secondary font-bold border-b-2 border-secondary pb-1">{label}</a>'
        return f'<a href="{href}" class="font-body-md text-body-md text-on-surface-variant hover:text-secondary transition-colors">{label}</a>'

    return f"""<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="icon" href="/assets/favicon.svg" type="image/svg+xml">
<link href="https://fonts.googleapis.com/css2?family=Hanken+Grotesk:wght@400;600;700;800&amp;family=Inter:wght@400;500;600&amp;family=JetBrains+Mono:wght@500&amp;display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=block" rel="stylesheet">
<script src="https://cdn.tailwindcss.com?plugins=forms,container-queries"></script>
<script id="tailwind-config">try{{ {TAILWIND_CONFIG} }}catch(_e){{}}</script>
<style>{SITE_CSS}</style>
</head>
<body class="bg-surface font-body-md text-on-surface overflow-x-hidden">
<nav class="fixed top-0 w-full z-50 bg-surface/80 backdrop-blur-md border-b border-outline-variant/10 h-20">
<div class="max-w-container-max mx-auto px-margin-mobile md:px-margin-desktop flex justify-between items-center h-full">
<a href="/" class="pandatechie-logo font-headline-md text-headline-md font-bold text-primary select-none">pandatechie <span class="font-label-sm text-label-sm text-on-surface-variant font-normal align-middle">aka Raghav</span></a>
<div class="hidden md:flex items-center gap-8">
{nav_link('/', 'Home', 'home')}
{nav_link('/archive/', 'Log', 'archive')}
{nav_link('/about/', 'About', 'about')}
</div>
<a href="/#contact-footer" class="hidden md:flex items-center gap-2 px-6 py-2 bg-primary text-on-primary font-label-md text-label-md hover:bg-secondary transition-all">Contact Me</a>
</div>
</nav>
{body}
<footer id="contact-footer" class="w-full py-12 bg-surface-container-lowest border-t border-outline-variant/10">
<div class="max-w-container-max mx-auto px-margin-mobile md:px-margin-desktop flex flex-col md:flex-row justify-between items-center gap-base">
<div class="mb-8 md:mb-0 text-center md:text-left">
<div class="font-headline-md text-headline-md font-bold text-primary mb-2">pandatechie</div>
<p class="font-label-sm text-label-sm text-on-surface-variant">© {datetime.now().year}</p>
</div>
<div class="flex flex-wrap justify-center gap-3">
<a href="https://github.com/pandatechie" target="_blank" aria-label="GitHub" title="GitHub" class="w-10 h-10 rounded-full border border-outline-variant/20 flex items-center justify-center hover:border-electric-azure hover:text-electric-azure text-on-surface-variant transition-colors"><svg viewBox="0 0 24 24" width="18" height="18" fill="currentColor"><path d="M12 .5C5.73.5.5 5.73.5 12c0 5.08 3.29 9.39 7.86 10.91.57.1.78-.25.78-.55 0-.27-.01-1.17-.02-2.12-3.2.7-3.88-1.36-3.88-1.36-.53-1.34-1.29-1.7-1.29-1.7-1.05-.72.08-.71.08-.71 1.17.08 1.78 1.2 1.78 1.2 1.03 1.77 2.7 1.26 3.36.96.1-.75.4-1.26.73-1.55-2.55-.29-5.24-1.28-5.24-5.69 0-1.26.45-2.29 1.19-3.1-.12-.29-.52-1.46.11-3.05 0 0 .97-.31 3.18 1.18a11.1 11.1 0 0 1 5.79 0c2.2-1.49 3.17-1.18 3.17-1.18.64 1.59.24 2.76.12 3.05.74.81 1.18 1.84 1.18 3.1 0 4.42-2.69 5.4-5.25 5.68.41.36.78 1.08.78 2.17 0 1.57-.01 2.83-.01 3.22 0 .3.2.66.79.55A10.97 10.97 0 0 0 23.5 12C23.5 5.73 18.27.5 12 .5Z"/></svg></a>
<a href="https://linkedin.com/in/rgvd" target="_blank" aria-label="LinkedIn" title="LinkedIn" class="w-10 h-10 rounded-full border border-outline-variant/20 flex items-center justify-center hover:border-electric-azure hover:text-electric-azure text-on-surface-variant transition-colors"><svg viewBox="0 0 24 24" width="18" height="18" fill="currentColor"><path d="M20.45 20.45h-3.55v-5.57c0-1.33-.02-3.04-1.85-3.04-1.86 0-2.15 1.45-2.15 2.94v5.67H9.35V9h3.41v1.56h.05c.47-.9 1.63-1.85 3.36-1.85 3.6 0 4.27 2.37 4.27 5.45v6.29zM5.34 7.43a2.06 2.06 0 1 1 0-4.12 2.06 2.06 0 0 1 0 4.12zM7.12 20.45H3.56V9h3.56v11.45z"/></svg></a>
<a href="https://instagram.com/pandatechie_" target="_blank" aria-label="Instagram" title="Instagram" class="w-10 h-10 rounded-full border border-outline-variant/20 flex items-center justify-center hover:border-electric-azure hover:text-electric-azure text-on-surface-variant transition-colors"><svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="1.6"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.4" cy="6.6" r="1"/></svg></a>
<a href="https://twitter.com/pandatechie_" target="_blank" aria-label="X (Twitter)" title="X (Twitter)" class="w-10 h-10 rounded-full border border-outline-variant/20 flex items-center justify-center hover:border-electric-azure hover:text-electric-azure text-on-surface-variant transition-colors"><svg viewBox="0 0 24 24" width="18" height="18" fill="currentColor"><path d="M18.3 3H21l-6.6 7.55L22 21h-6.14l-4.8-6.28L5.5 21H2.8l7.03-8.03L2 3h6.28l4.34 5.74L18.3 3Zm-1.08 16.17h1.5L7.86 4.72H6.25l11 14.45Z"/></svg></a>
<a href="https://calendly.com/summon_panda" target="_blank" aria-label="Calendly" title="Calendly" class="w-10 h-10 rounded-full border border-outline-variant/20 flex items-center justify-center hover:border-electric-azure hover:text-electric-azure text-on-surface-variant transition-colors"><span class="material-symbols-outlined text-[18px]">calendar_month</span></a>
<a href="mailto:dudejaraghav@gmail.com" aria-label="Email" title="Email" class="w-10 h-10 rounded-full border border-outline-variant/20 flex items-center justify-center hover:border-electric-azure hover:text-electric-azure text-on-surface-variant transition-colors"><span class="material-symbols-outlined text-[18px]">mail</span></a>
</div>
</div>
</footer>
<script>{SITE_JS}</script>
</body>
</html>"""

def _post_card(p):
    legacy = p.get('archive')
    cat = category_of(p)
    badge_color = "bg-secondary/10 text-secondary" if not legacy else "bg-vibrant-magenta/10 text-vibrant-magenta"
    return f"""
<article class="group ghost-border rounded-lg p-6 card-hover transition-all duration-300 bg-surface-container-lowest flex flex-col">
<span class="font-label-sm text-label-sm {badge_color} px-3 py-1 rounded self-start mb-4">{cat.upper()}</span>
<h3 class="font-headline-md text-[19px] mb-3 leading-snug group-hover:text-electric-azure transition-colors"><a href="/archive/{p['slug']}/">{p['title']}</a></h3>
<p class="font-body-md text-body-md text-on-surface-variant line-clamp-3 mb-4 flex-1">{p.get('excerpt','')}</p>
<div class="flex justify-between items-center mt-auto pt-4 border-t border-outline-variant/10">
<span class="font-label-sm text-label-sm text-outline-variant">{p.get('date','')}</span>
<a href="/archive/{p['slug']}/" class="material-symbols-outlined text-outline-variant group-hover:text-electric-azure transition-colors">open_in_new</a>
</div>
</article>"""

def _pagination(page_num, pages, base_path):
    if pages <= 1:
        return ""
    prev_html = ""
    if page_num > 1:
        href = base_path if page_num == 2 else f'{base_path}page/{page_num-1}/'
        prev_html = f'<a href="{href}" class="w-12 h-12 rounded-full border border-outline-variant flex items-center justify-center hover:bg-surface-gray transition-colors"><span class="material-symbols-outlined">chevron_left</span></a>'
    next_html = ""
    if page_num < pages:
        next_html = f'<a href="{base_path}page/{page_num+1}/" class="w-12 h-12 rounded-full border border-outline-variant flex items-center justify-center hover:bg-surface-gray transition-colors"><span class="material-symbols-outlined">chevron_right</span></a>'
    return f"""
<div class="mt-20 flex justify-center items-center gap-4">
{prev_html}
<span class="font-label-md text-label-md px-4">Page {page_num} of {pages}</span>
{next_html}
</div>"""

def render_archive_hub(posts):
    groups = {}
    for p in posts:
        cat_name = category_of(p)
        slug = slugify_category(cat_name)
        groups.setdefault(slug, {"name": cat_name, "posts": []})["posts"].append(p)

    cards = ""
    for slug, display_name, description, is_placeholder in CATEGORY_META:
        group = groups.get(slug)
        count = len(group["posts"]) if group else 0
        if count == 0:
            cards += f"""
<div class="ghost-border rounded-lg p-8 bg-surface-container-lowest flex flex-col opacity-70">
<span class="font-label-sm text-label-sm bg-outline-variant/20 text-on-surface-variant px-3 py-1 rounded self-start mb-4">COMING SOON</span>
<h3 class="font-headline-md text-[22px] mb-3">{display_name}</h3>
<p class="font-body-md text-body-md text-on-surface-variant flex-1">{description}</p>
</div>"""
        else:
            cards += f"""
<a href="/archive/category/{slug}/" class="group ghost-border rounded-lg p-8 card-hover transition-all duration-300 bg-surface-container-lowest flex flex-col">
<span class="font-label-sm text-label-sm bg-secondary/10 text-secondary px-3 py-1 rounded self-start mb-4">{count} POST{'S' if count != 1 else ''}</span>
<h3 class="font-headline-md text-[22px] mb-3 group-hover:text-electric-azure transition-colors">{display_name}</h3>
<p class="font-body-md text-body-md text-on-surface-variant flex-1">{description}</p>
</a>"""

    body = f"""
<main class="pt-20">
<section class="py-16 reveal-item">
<div class="max-w-container-max mx-auto px-margin-mobile md:px-margin-desktop">
<div class="flex justify-between items-center mb-16">
<div>
<h2 class="font-label-sm text-label-sm text-secondary uppercase tracking-widest mb-4">The full log</h2>
<h1 class="font-headline-lg text-headline-lg">{len(posts)} posts, sorted by topic</h1>
</div>
<a href="/archive/all/" class="hidden sm:flex items-center gap-2 font-label-md text-label-md text-secondary hover:text-vibrant-magenta transition-colors">Browse all chronologically <span class="material-symbols-outlined">arrow_forward</span></a>
</div>
<div class="grid grid-cols-1 md:grid-cols-2 gap-gutter">{cards}
</div>
</div>
</section>
</main>"""
    html = page_shell("The Log | Raghav", body, active="archive")
    out_path = os.path.join(OUT, 'archive', 'index.html')
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(html)

def render_category_listings(posts):
    groups = {}
    for p in posts:
        cat_name = category_of(p)
        slug = slugify_category(cat_name)
        groups.setdefault(slug, {"name": cat_name, "posts": []})["posts"].append(p)

    for slug, group in groups.items():
        cat_posts = group["posts"]
        display_name = group["name"]
        pages = math.ceil(len(cat_posts) / POSTS_PER_PAGE)
        base_path = f'/archive/category/{slug}/'
        for page_num in range(1, pages + 1):
            chunk = cat_posts[(page_num-1)*POSTS_PER_PAGE : page_num*POSTS_PER_PAGE]
            cards = "".join(_post_card(p) for p in chunk)
            body = f"""
<main class="pt-20">
<section class="py-16 reveal-item">
<div class="max-w-container-max mx-auto px-margin-mobile md:px-margin-desktop">
<a href="/archive/" class="font-label-sm text-label-sm text-secondary flex items-center gap-2 mb-8">← All categories</a>
<div class="flex justify-between items-center mb-16">
<div>
<h2 class="font-label-sm text-label-sm text-secondary uppercase tracking-widest mb-4">Category</h2>
<h1 class="font-headline-lg text-headline-lg">{display_name}</h1>
</div>
</div>
<div class="grid grid-cols-1 md:grid-cols-3 gap-gutter">{cards}
</div>
{_pagination(page_num, pages, base_path)}
</div>
</section>
</main>"""
            html = page_shell(f"{display_name} — The Log | Raghav", body, active="archive")
            if page_num == 1:
                out_path = os.path.join(OUT, 'archive', 'category', slug, 'index.html')
            else:
                out_path = os.path.join(OUT, 'archive', 'category', slug, 'page', str(page_num), 'index.html')
            os.makedirs(os.path.dirname(out_path), exist_ok=True)
            with open(out_path, 'w', encoding='utf-8') as f:
                f.write(html)

def render_archive_all(posts):
    pages = math.ceil(len(posts) / POSTS_PER_PAGE)
    base_path = '/archive/all/'
    for page_num in range(1, pages + 1):
        chunk = posts[(page_num-1)*POSTS_PER_PAGE : page_num*POSTS_PER_PAGE]
        cards = "".join(_post_card(p) for p in chunk)
        body = f"""
<main class="pt-20">
<section class="py-16 reveal-item">
<div class="max-w-container-max mx-auto px-margin-mobile md:px-margin-desktop">
<a href="/archive/" class="font-label-sm text-label-sm text-secondary flex items-center gap-2 mb-8">← All categories</a>
<div class="flex justify-between items-center mb-16">
<div>
<h2 class="font-label-sm text-label-sm text-secondary uppercase tracking-widest mb-4">Everything, chronologically</h2>
<h1 class="font-headline-lg text-headline-lg">{len(posts)} posts, 2020 to now</h1>
</div>
</div>
<div class="grid grid-cols-1 md:grid-cols-3 gap-gutter">{cards}
</div>
{_pagination(page_num, pages, base_path)}
</div>
</section>
</main>"""
        html = page_shell(f"All posts — Page {page_num} | Raghav", body, active="archive")
        if page_num == 1:
            out_path = os.path.join(OUT, 'archive', 'all', 'index.html')
        else:
            out_path = os.path.join(OUT, 'archive', 'all', 'page', str(page_num), 'index.html')
        os.makedirs(os.path.dirname(out_path), exist_ok=True)
        with open(out_path, 'w', encoding='utf-8') as f:
            f.write(html)

def render_post(p):
    cats = ' '.join(f'<span class="font-label-sm text-label-sm bg-secondary/10 text-secondary px-3 py-1 rounded">{c.upper()}</span>' for c in p.get('categories', []))
    legacy_banner = ""
    if p.get('archive'):
        legacy_banner = f"""<div class="mt-8 ghost-border rounded-lg p-4 flex items-center gap-3 bg-vibrant-magenta/5">
<span class="w-1.5 h-1.5 rounded-full bg-vibrant-magenta flex-shrink-0"></span>
<p class="font-label-sm text-label-sm text-on-surface-variant">Originally published {p.get('date','')} on the site's earlier chapter as a crypto/Web3 blog. Kept as-is for the record.</p>
</div>"""
    cover = f'<img src="{p["cover_image"]}" alt="" class="w-full rounded-xl ghost-border mt-10" loading="lazy">' if p.get('cover_image') else ''
    body = f"""
<main class="pt-20">
<article class="py-16 reveal-item">
<div class="max-w-container-max mx-auto px-margin-mobile md:px-margin-desktop max-w-3xl">
<a href="/archive/" class="font-label-sm text-label-sm text-secondary flex items-center gap-2">← Back to the log</a>
<div class="flex flex-wrap gap-2 mt-8">{cats}</div>
<h1 class="font-headline-lg text-[32px] md:text-headline-lg mt-6 leading-tight">{p['title']}</h1>
<div class="font-label-sm text-label-sm text-outline-variant mt-4">{p.get('date','')}</div>
{legacy_banner}
{cover}
<div class="prose-post font-body-lg text-body-lg text-on-surface leading-relaxed mt-10">
{p['html']}
</div>
</div>
</article>
</main>
<style>
.prose-post h2{{font-family:'Hanken Grotesk',sans-serif; font-size:26px; font-weight:600; margin-top:40px; margin-bottom:14px; color:#F3F3F1;}}
.prose-post h3{{font-family:'Hanken Grotesk',sans-serif; font-size:20px; font-weight:600; margin-top:28px; margin-bottom:10px; color:#F3F3F1;}}
.prose-post p{{margin-top:14px;}}
.prose-post ul, .prose-post ol{{margin-top:14px; padding-left:22px;}}
.prose-post li{{margin-top:6px;}}
.prose-post img{{margin-top:20px; border-radius:10px; border:1px solid rgba(255,255,255,0.1);}}
.prose-post a{{color:#FF6A3D; text-decoration:underline; text-underline-offset:3px;}}
.prose-post blockquote{{margin-top:18px; padding-left:18px; border-left:3px solid #FF6A3D; color:#9C9CA3; font-style:italic;}}
.prose-post code{{background:rgba(255,106,61,0.12); padding:2px 6px; border-radius:4px; font-family:'JetBrains Mono',monospace; font-size:14px; color:#F3F3F1;}}
</style>"""
    html = page_shell(f"{p['title']} | Raghav", body, description=p.get('excerpt',''), active="archive")
    out_dir = os.path.join(OUT, 'archive', p['slug'])
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(html)

def render_homepage(posts):
    with open(os.path.join(SITE_DIR, 'homepage_body_v2.html'), encoding='utf-8') as f:
        tpl = f.read()

    featured = [p for p in posts if p.get('featured')]
    if featured:
        log_preview = featured[:3]
    else:
        recent_new = [p for p in posts if not p.get('archive')][:1]
        recent_legacy = [p for p in posts if p.get('archive')][:2]
        log_preview = (recent_new + recent_legacy)[:3]

    cards = ""
    for p in log_preview:
        legacy = p.get('archive')
        cat = (p.get('categories') or (['Archive'] if legacy else ['Field / SFE']))[0]
        cover = p.get('cover_image')
        if cover:
            thumb_html = f'<img src="{cover}" alt="" loading="lazy" class="absolute inset-0 w-full h-full object-cover thumb-duotone">'
        else:
            thumb_html = f'<div class="p-8 h-full flex flex-col justify-center"><div class="text-outline text-headline-md font-bold opacity-10">{cat.upper()}</div></div>'
        cards += f"""
<a href="/archive/{p['slug']}/" class="group cursor-pointer block">
<div class="relative aspect-video mb-6 overflow-hidden bg-surface-container rounded-lg border border-outline-variant/10">
{thumb_html}
<div class="absolute inset-0 flex items-center justify-center opacity-0 group-hover:opacity-100 transition-opacity bg-primary/20 backdrop-blur-sm">
<span class="px-6 py-2 bg-white text-primary font-label-md text-label-md">Read</span>
</div>
</div>
<div class="font-label-sm text-label-sm text-secondary mb-2">{p.get('date','').upper()}</div>
<h4 class="font-headline-md text-headline-md mb-2 group-hover:text-secondary transition-colors text-[20px]">{p['title']}</h4>
<p class="font-body-md text-body-md text-on-surface-variant line-clamp-2">{p.get('excerpt','')}</p>
</a>"""

    total_archive = len([p for p in posts if p.get('archive')])
    tpl = tpl.replace('{{LOG_CARDS}}', cards)
    tpl = tpl.replace('{{ARCHIVE_COUNT}}', str(total_archive))

    html = page_shell("Raghav — Writer & Facilitator", tpl, active="home")
    with open(os.path.join(OUT, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(html)

def render_about(posts):
    total_archive = len([p for p in posts if p.get('archive')])
    with open(os.path.join(SITE_DIR, 'about_body.html'), encoding='utf-8') as f:
        tpl = f.read()
    tpl = tpl.replace('{{ARCHIVE_COUNT}}', str(total_archive))
    html = page_shell("About | Raghav", tpl, active="about")
    out_dir = os.path.join(OUT, 'about')
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(html)

def copy_static_assets():
    # Copy image assets (photos etc.) into dist/assets — skip the CSS/JS/config
    # source files, which are inlined into the page shell instead.
    src_dir = os.path.join(SITE_DIR, 'assets')
    dst_dir = os.path.join(OUT, 'assets')
    os.makedirs(dst_dir, exist_ok=True)
    skip = {'site.css', 'site.js', 'tailwind-config.js'}
    for fname in os.listdir(src_dir):
        if fname in skip:
            continue
        shutil.copy2(os.path.join(src_dir, fname), os.path.join(dst_dir, fname))

def render_404():
    body = """
<main class="pt-20">
<section class="min-h-[70vh] flex items-center reveal-item">
<div class="max-w-container-max mx-auto px-margin-mobile md:px-margin-desktop text-center">
<div class="text-[100px] mb-4">🐼</div>
<h1 class="font-headline-lg text-headline-lg mb-4">This page wandered off into the bamboo.</h1>
<p class="font-body-lg text-body-lg text-on-surface-variant max-w-md mx-auto mb-10">404 — nothing here. It might have moved, or it might just be a panda's idea of a joke.</p>
<a href="/" class="magnetic inline-flex items-center gap-2 px-8 py-4 bg-primary text-on-primary font-label-md text-label-md hover:bg-secondary hover:text-white transition-all">Back to solid ground <span class="material-symbols-outlined">arrow_forward</span></a>
</div>
</section>
</main>"""
    html = page_shell("Page not found | Raghav", body, active="")
    with open(os.path.join(OUT, '404.html'), 'w', encoding='utf-8') as f:
        f.write(html)

def main():
    posts = load_posts()
    print(f"Loaded {len(posts)} archive posts")
    render_archive_hub(posts)
    render_category_listings(posts)
    render_archive_all(posts)
    for p in posts:
        render_post(p)
    render_homepage(posts)
    render_about(posts)
    render_404()
    copy_static_assets()
    print("Build complete ->", OUT)

if __name__ == '__main__':
    main()
