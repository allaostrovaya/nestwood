# -*- coding: utf-8 -*-
"""Звірка набору вайрфреймів: структура, нейминг, навігація, звʼязність."""
import pathlib, re, collections
W = pathlib.Path('wireframes')
pages = sorted(p for p in W.glob('*.html') if p.name not in ('_nav.html','ia.html'))
files = {p.name for p in pages}
issues = collections.defaultdict(list)

for p in pages:
    s = p.read_text(encoding='utf-8')
    n = p.name
    # структура
    if s.count('<main>') != 1: issues[n].append('не один <main>')
    if s.count('<h1>') != 1: issues[n].append('не один <h1>')
    if '<html lang="uk">' not in s: issues[n].append('lang не uk')
    if '<nav class="wf-tree"' not in s: issues[n].append('немає дерева')
    if 'class="states"' not in s: issues[n].append('немає рядка станів')
    if 'aria-current="page"' not in s: issues[n].append('немає поточного вузла')
    if 'class="wf-shell"' not in s: issues[n].append('немає wf-shell')
    if 'class="device"' not in s: issues[n].append('немає device')
    if 'ann-out' not in s: issues[n].append('немає фінальної анотації')
    # зобовʼязання
    if 'Kartverket' not in s: issues[n].append('немає атрибуції')
    if '<summary>Звідки це взято</summary>' not in s: issues[n].append('немає шару «Звідки це взято»')
    # зони й анотації
    sec = len(re.findall(r'<section aria-labelledby=', s))
    ann = len(re.findall(r'<p class="ann"[^>]*>ЗОНА', s))
    if sec == 0: issues[n].append('немає жодної зони')
    if ann < sec: issues[n].append(f'анотацій {ann} на {sec} зон')
    # семантика
    if re.search(r'<a[^>]*>\s*<button', s): issues[n].append('<button> усередині <a>')
    if re.search(r'<script', s): issues[n].append('є <script>')
    if re.search(r'https?://(?!www\.w3)', s): issues[n].append('зовнішнє посилання')
    if 'lorem' in s.lower(): issues[n].append('lorem ipsum')
    # колір
    for m in re.findall(r'(?:color|background)\s*:\s*#([0-9a-fA-F]{3,6})', s):
        h = m if len(m)==6 else ''.join(c*2 for c in m)
        if not (h[0:2]==h[2:4]==h[4:6]): issues[n].append(f'колір #{m}')
    # посилання
    for t in set(re.findall(r'(?:href|action)="\./([^"#]+\.html)"', s)):
        if t not in files: issues[n].append(f'биті: {t}')
    body = re.search(r'<div class="device">.*?</div>\s*<p class="ann ann-out"', s, re.S)
    if body and not re.search(r'(?:href|action)="\./', body.group(0)): issues[n].append('немає виходу з екрана')

print(f'сторінок: {len(pages)}')
print(f'з проблемами: {len(issues)}\n')
for n in sorted(issues):
    print(f'  {n:28} {"; ".join(issues[n])}')
