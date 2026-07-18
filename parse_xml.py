import xml.etree.ElementTree as ET
import re, json, os
from markdownify import markdownify as md

NS = {
    'wp': 'http://wordpress.org/export/1.2/',
    'content': 'http://purl.org/rss/1.0/modules/content/',
    'dc': 'http://purl.org/dc/elements/1.1/',
}

SRC = '/mnt/user-data/uploads/Bitcoin_Blockchain_Banter_Export_Jul_18.xml'
OUT_DIR = '/home/claude/site/content/archive'

def clean_wp_content(raw):
    if not raw:
        return ""
    # strip gutenberg block comments
    raw = re.sub(r'<!--\s*/?wp:.*?-->', '', raw, flags=re.DOTALL)
    return raw.strip()

def slugify_fallback(title):
    s = re.sub(r'[^a-z0-9]+', '-', title.lower()).strip('-')
    return s

def first_image(raw_html):
    m = re.search(r'<img[^>]+src="([^"]+)"', raw_html or '')
    return m.group(1) if m else None

def main():
    tree = ET.parse(SRC)
    root = tree.getroot()
    channel = root.find('channel')
    items = channel.findall('item')

    posts = []
    for item in items:
        ptype = item.find('wp:post_type', NS).text
        if ptype != 'post':
            continue
        status = item.find('wp:status', NS).text
        if status != 'publish':
            continue

        title = (item.find('title').text or '').strip()
        slug = item.find('wp:post_name', NS).text or slugify_fallback(title)
        pub_date = item.find('wp:post_date', NS).text  # 'YYYY-MM-DD HH:MM:SS'
        date_only = pub_date.split(' ')[0] if pub_date else ''
        raw_content = item.find('content:encoded', NS).text or ''
        link = item.find('link').text or ''

        cats = []
        tags = []
        for cat_el in item.findall('category'):
            domain = cat_el.get('domain')
            text = cat_el.text or ''
            if domain == 'post_tag':
                tags.append(text)
            else:
                cats.append(text)
        cats = sorted(set(c for c in cats if c))
        tags = sorted(set(t for t in tags if t))

        cleaned_html = clean_wp_content(raw_content)
        cover = first_image(cleaned_html)
        markdown_body = md(cleaned_html, heading_style="ATX")
        # collapse 3+ blank lines
        markdown_body = re.sub(r'\n{3,}', '\n\n', markdown_body).strip()

        posts.append({
            'title': title,
            'slug': slug,
            'date': date_only,
            'categories': cats,
            'tags': tags,
            'original_url': link,
            'cover_image': cover,
            'body_md': markdown_body,
        })

    print(f"Parsed {len(posts)} published posts")

    os.makedirs(OUT_DIR, exist_ok=True)
    manifest = []
    for p in posts:
        fm_lines = ['---']
        def esc(s):
            return s.replace('"', '\\"')
        fm_lines.append(f'title: "{esc(p["title"])}"')
        fm_lines.append(f'date: "{p["date"]}"')
        fm_lines.append(f'slug: "{p["slug"]}"')
        fm_lines.append(f'categories: {json.dumps(p["categories"])}')
        fm_lines.append(f'tags: {json.dumps(p["tags"])}')
        fm_lines.append(f'original_url: "{p["original_url"]}"')
        if p['cover_image']:
            fm_lines.append(f'cover_image: "{p["cover_image"]}"')
        fm_lines.append('archive: true')
        fm_lines.append('---')
        content = "\n".join(fm_lines) + "\n\n" + p['body_md'] + "\n"

        fname = f"{p['date']}-{p['slug']}.md" if p['date'] else f"{p['slug']}.md"
        fpath = os.path.join(OUT_DIR, fname)
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)

        manifest.append({
            'title': p['title'], 'slug': p['slug'], 'date': p['date'],
            'categories': p['categories'], 'tags': p['tags'],
            'file': fname, 'cover_image': p['cover_image'],
        })

    with open('/home/claude/site/content/archive-manifest.json', 'w', encoding='utf-8') as f:
        json.dump(manifest, f, indent=2)

    print(f"Wrote {len(manifest)} markdown files to {OUT_DIR}")

if __name__ == '__main__':
    main()
