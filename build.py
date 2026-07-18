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
<link href="https://fonts.googleapis.com/css2?family=Hanken+Grotesk:wght@400;600;700;800&amp;family=Inter:wght@400;500;600&amp;family=JetBrains+Mono:wght@500&amp;display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=block" rel="stylesheet">
<script src="https://cdn.tailwindcss.com?plugins=forms,container-queries"></script>
<script id="tailwind-config">try{{ {TAILWIND_CONFIG} }}catch(_e){{}}</script>
<style>{SITE_CSS}</style>
</head>
<body class="bg-surface font-body-md text-on-surface overflow-x-hidden">
<nav class="fixed top-0 w-full z-50 bg-surface/80 backdrop-blur-md border-b border-outline-variant/10 h-20">
<div class="max-w-container-max mx-auto px-margin-mobile md:px-margin-desktop flex justify-between items-center h-full">
<a href="/" class="font-headline-md text-headline-md font-bold text-primary">pandatechie <span class="font-label-sm text-label-sm text-on-surface-variant font-normal align-middle">aka Raghav</span></a>
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
<div class="flex flex-wrap justify-center gap-6 font-label-sm text-label-sm">
<a href="https://linkedin.com/in/rgvd" target="_blank" class="text-on-surface-variant hover:text-vibrant-magenta transition-colors">LinkedIn</a>
<a href="https://twitter.com/pandatechie_" target="_blank" class="text-on-surface-variant hover:text-vibrant-magenta transition-colors">Twitter</a>
<a href="https://calendly.com/summon_panda" target="_blank" class="text-on-surface-variant hover:text-vibrant-magenta transition-colors">Calendly</a>
<a href="mailto:dudejaraghav@gmail.com" class="text-on-surface-variant hover:text-vibrant-magenta transition-colors">Email</a>
</div>
</div>
</footer>
<script>{SITE_JS}</script>
</body>
</html>"""

def render_archive_index(posts):
    pages = math.ceil(len(posts) / POSTS_PER_PAGE)
    for page_num in range(1, pages + 1):
        chunk = posts[(page_num-1)*POSTS_PER_PAGE : page_num*POSTS_PER_PAGE]
        cards = ""
        for p in chunk:
            legacy = p.get('archive')
            cat = (p.get('categories') or (['Archive'] if legacy else ['Field / SFE']))[0]
            badge_color = "bg-secondary/10 text-secondary" if not legacy else "bg-vibrant-magenta/10 text-vibrant-magenta"
            cards += f"""
<article class="group ghost-border rounded-lg p-6 card-hover transition-all duration-300 bg-surface-container-lowest flex flex-col">
<span class="font-label-sm text-label-sm {badge_color} px-3 py-1 rounded self-start mb-4">{cat.upper()}</span>
<h3 class="font-headline-md text-[19px] mb-3 leading-snug group-hover:text-electric-azure transition-colors"><a href="/archive/{p['slug']}/">{p['title']}</a></h3>
<p class="font-body-md text-body-md text-on-surface-variant line-clamp-3 mb-4 flex-1">{p.get('excerpt','')}</p>
<div class="flex justify-between items-center mt-auto pt-4 border-t border-outline-variant/10">
<span class="font-label-sm text-label-sm text-outline-variant">{p.get('date','')}</span>
<a href="/archive/{p['slug']}/" class="material-symbols-outlined text-outline-variant group-hover:text-electric-azure transition-colors">open_in_new</a>
</div>
</article>"""

        pagination = ""
        if pages > 1:
            prev_html = ""
            if page_num > 1:
                href = '/archive/' if page_num == 2 else f'/archive/page/{page_num-1}/'
                prev_html = f'<a href="{href}" class="w-12 h-12 rounded-full border border-outline-variant flex items-center justify-center hover:bg-surface-gray transition-colors"><span class="material-symbols-outlined">chevron_left</span></a>'
            next_html = ""
            if page_num < pages:
                next_html = f'<a href="/archive/page/{page_num+1}/" class="w-12 h-12 rounded-full border border-outline-variant flex items-center justify-center hover:bg-surface-gray transition-colors"><span class="material-symbols-outlined">chevron_right</span></a>'
            pagination = f"""
<div class="mt-20 flex justify-center items-center gap-4">
{prev_html}
<span class="font-label-md text-label-md px-4">Page {page_num} of {pages}</span>
{next_html}
</div>"""

        body = f"""
<main class="pt-20">
<section class="py-16 reveal-item">
<div class="max-w-container-max mx-auto px-margin-mobile md:px-margin-desktop">
<div class="flex justify-between items-center mb-16">
<div>
<h2 class="font-label-sm text-label-sm text-secondary uppercase tracking-widest mb-4">The full log</h2>
<h1 class="font-headline-lg text-headline-lg">{len(posts)} posts, 2020 to now</h1>
</div>
</div>
<div class="grid grid-cols-1 md:grid-cols-3 gap-gutter">{cards}
</div>
{pagination}
</div>
</section>
</main>"""
        html = page_shell(f"The Log — Page {page_num} | Raghav", body, active="archive")
        if page_num == 1:
            out_path = os.path.join(OUT, 'archive', 'index.html')
        else:
            out_dir = os.path.join(OUT, 'archive', 'page', str(page_num))
            os.makedirs(out_dir, exist_ok=True)
            out_path = os.path.join(out_dir, 'index.html')
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
.prose-post h2{{font-family:'Hanken Grotesk',sans-serif; font-size:26px; font-weight:600; margin-top:40px; margin-bottom:14px;}}
.prose-post h3{{font-family:'Hanken Grotesk',sans-serif; font-size:20px; font-weight:600; margin-top:28px; margin-bottom:10px;}}
.prose-post p{{margin-top:14px;}}
.prose-post ul, .prose-post ol{{margin-top:14px; padding-left:22px;}}
.prose-post li{{margin-top:6px;}}
.prose-post img{{margin-top:20px; border-radius:10px; border:1px solid rgba(0,0,0,0.1);}}
.prose-post a{{color:#5286E1; text-decoration:underline; text-underline-offset:3px;}}
.prose-post blockquote{{margin-top:18px; padding-left:18px; border-left:3px solid #5286E1; color:#48464a; font-style:italic;}}
.prose-post code{{background:rgba(82,134,225,0.1); padding:2px 6px; border-radius:4px; font-family:'JetBrains Mono',monospace; font-size:14px;}}
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
        cards += f"""
<a href="/archive/{p['slug']}/" class="group cursor-pointer block">
<div class="relative aspect-video mb-6 overflow-hidden bg-surface-container rounded-lg border border-outline-variant/10">
<div class="absolute inset-0 bg-gradient-to-tr from-secondary/10 to-vibrant-magenta/5"></div>
<div class="absolute inset-0 flex items-center justify-center opacity-0 group-hover:opacity-100 transition-opacity bg-primary/20 backdrop-blur-sm">
<span class="px-6 py-2 bg-white text-primary font-label-md text-label-md">Read</span>
</div>
<div class="p-8 h-full flex flex-col justify-center">
<div class="text-outline text-headline-md font-bold opacity-10">{cat.upper()}</div>
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

def main():
    posts = load_posts()
    print(f"Loaded {len(posts)} archive posts")
    render_archive_index(posts)
    for p in posts:
        render_post(p)
    render_homepage(posts)
    render_about(posts)
    copy_static_assets()
    print("Build complete ->", OUT)

if __name__ == '__main__':
    main()
