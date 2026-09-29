from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse
import subprocess

class Page(HTMLParser):
    def __init__(self, path):
        super().__init__(convert_charrefs=True)
        self.path, self.ids, self.refs = path, set(), []
        self.headings = 0
        self.feed(path.read_text())
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if 'id' in a:
            assert a['id'] not in self.ids, f'{self.path}: duplicate id {a["id"]}'
            self.ids.add(a['id'])
        if tag == 'h1': self.headings += 1
        if tag == 'img': assert 'alt' in a, f'{self.path}: missing image alternative'
        for name in ('href', 'src', 'poster'):
            if name in a: self.refs.append(a[name])

pages = [Page(Path('index.html'))]
if Path('en.html').exists(): pages.append(Page(Path('en.html')))
for page in pages:
    assert page.headings == 1
    for ref in page.refs:
        url = urlparse(ref)
        if url.scheme or url.netloc: continue
        if url.path: assert (page.path.parent / url.path).is_file(), f'Broken local link: {ref}'
        elif url.fragment: assert url.fragment in page.ids, f'Broken anchor: {ref}'
    print(f'PASS {page.path}: one h1, unique IDs, image alternatives, {len(page.refs)} valid local references')
for name in ('style.css', 'terms.html', 'privacy.html', 'refund.html'):
    assert Path(name).read_bytes() == subprocess.check_output(['git', 'show', f'HEAD:{name}']), f'Unrelated change: {name}'
print('PASS shared CSS and all three legal pages unchanged')
subprocess.run(['git', 'diff', '--check'], check=True)

for filename, lang, other in [('index.html', 'ja', 'en.html'), ('en.html', 'en', 'index.html')]:
    text = Path(filename).read_text()
    assert f'<html lang="{lang}">' in text
    assert f'href="{other}" lang=' in text, 'Missing language switch'
    assert 'hreflang="ja" href="index.html"' in text
    assert 'hreflang="en" href="en.html"' in text
    assert '<script' not in text and '<form' not in text
    assert '$6' in text and '$50' in text
    assert '14日' not in text and '14-day' not in text
print('PASS language metadata, reciprocal links, prices, and no scripts/forms')
