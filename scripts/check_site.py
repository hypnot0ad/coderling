#!/usr/bin/env python3
"""Check local output without downloading anything. Run after Hugo."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote
import sys
ROOT=Path(__file__).resolve().parents[1]
DOCS=ROOT/'docs'
BASE='/coderling/'
class Page(HTMLParser):
    def __init__(self, text):
        super().__init__();self.links=[];self.ids=set();self.feed(text)
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if 'id' in a:self.ids.add(a['id'])
        for key in ('href','src'):
            if key in a:self.links.append(a[key])
pages={p.resolve():Page(p.read_text()) for p in DOCS.rglob('*.html')}
errors=[]
for path,page in pages.items():
    for link in page.links:
        u=urlsplit(link)
        if u.scheme or u.netloc:continue
        raw=unquote(u.path)
        if raw.startswith('/'):
            if not raw.startswith(BASE):
                errors.append(f'{path.relative_to(ROOT)}: path outside project base: {link}');continue
            target=DOCS/raw[len(BASE):]
        else:target=path.parent/raw if raw else path
        if target.is_dir():target=target/'index.html'
        target=target.resolve()
        if not target.is_file():errors.append(f'{path.relative_to(ROOT)}: missing {link}')
        elif u.fragment and target in pages and unquote(u.fragment) not in pages[target].ids:
            errors.append(f'{path.relative_to(ROOT)}: missing anchor {link}')
lessons=DOCS/'workshops/memory-match'
for path in lessons.glob('*/index.html'):
    s=path.read_text()
    for text in ('smart kiddos','l0lIGWz4yKU','Previous','Next','If something goes wrong'):
        if text not in s:errors.append(f'{path}: missing {text}')
if len(list(lessons.glob('*/index.html'))) != 8:errors.append('Expected eight lesson stages')
if not (DOCS/'.nojekyll').is_file():errors.append('Missing docs/.nojekyll')
if errors:print('\n'.join(errors));sys.exit(1)
print(f'PASS: {len(pages)} HTML pages; internal links, assets, anchors, eight lesson stages, credits and navigation.')
