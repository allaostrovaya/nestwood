# -*- coding: utf-8 -*-
"""Звірка набору вайрфреймів: структура, нейминг, навігація, звʼязність."""
import pathlib, re, collections
W = pathlib.Path('wireframes')
pages = sorted(p for p in W.glob('*.html') if p.name not in ('_nav.html','ia.html','index.html'))
files = {p.name for p in W.glob('*.html')}
issues = collections.defaultdict(list)

for p in pages:
    s = p.read_text(encoding='utf-8')
    n = p.name
    # структура
    if s.count('<main>') != 1: issues[n].append('не один <main>')
    if s.count('<h1>') != 1: issues[n].append('не один <h1>')
    if '<html lang="uk">' not in s: issues[n].append('lang не uk')
    if '<nav class="wf-tree"' not in s: issues[n].append('немає дерева')
    if 'aria-current="page"' not in s: issues[n].append('немає поточного вузла')
    if 'class="wf-shell"' not in s: issues[n].append('немає wf-shell')
    if 'class="device"' not in s: issues[n].append('немає device')
    # зобовʼязання
    if 'Kartverket' not in s: issues[n].append('немає атрибуції')
    if '<summary>Звідки це взято</summary>' not in s: issues[n].append('немає шару «Звідки це взято»')
    # зони
    sec = len(re.findall(r'<section aria-labelledby=', s))
    if sec == 0: issues[n].append('немає жодної зони')
    # рів'ю-хром: рівно один рядок позиції, і жодних коментарів розробників
    if s.count('class="meta"') != 1: issues[n].append('немає рядка позиції')
    if 'class="ann' in s: issues[n].append('лишилась анотація зони')
    if 'details class="review"' in s: issues[n].append('лишилась шапка-details')
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

# ── звʼязність: у кожного екрана має бути вхід із іншого макета ──
TABS = {'catalogue.html','plans.html','guide.html','safety.html','me.html'}
SUF = ('-empty','-error','-loading','-offline','-degraded','-conflict','-seasonal','-nooptions','-intrip','-past')
def in_device(t):
    i = t.find('<div class="device"'); j = t.find('<nav class="tabbar"')
    return t[i:j] if i >= 0 and j > i else ''
inbound = collections.Counter()
for p in pages:
    src = in_device(p.read_text(encoding='utf-8'))
    for t in set(re.findall(r'(?:href|action)="\./([a-z-]+\.html)"', src)):
        if t != p.name: inbound[t] += 1
orphan = [p.name for p in pages
          if inbound[p.name] == 0 and p.name not in TABS
          and not any(p.name[:-5].endswith(x) for x in SUF)]
if orphan:
    print(f'\nекранів без жодного входу з макета: {len(orphan)}')
    for n in orphan: print(f'  {n}')
else:
    print('\nекранів без входу: 0 — кожен досяжний із іншого макета')

# ── ієрархія: «назад» веде до оголошеного батька ──
import importlib.util as _il
_sp = _il.spec_from_file_location('g','wireframes/_generate.py')
_g = _il.module_from_spec(_sp); _sp.loader.exec_module(_g)
bad_back = []
for p in pages:
    t = p.read_text(encoding='utf-8')
    par, pname = _g.parent_of(p.name)
    if p.name in _g.SHEETS:                      # аркуш: «✕ Закрити», не «назад»
        if '<a class="close"' not in t: bad_back.append(f'{p.name}: аркуш без «✕ Закрити»')
        elif '<a class="back"' in t: bad_back.append(f'{p.name}: аркуш і «назад» одночасно')
        continue
    m = re.search(r'<a class="back" href="\./([a-z-]+\.html)"', t)
    if par and not m: bad_back.append(f'{p.name}: немає «назад», батько {par}')
    elif par and m.group(1) != par: bad_back.append(f'{p.name}: «назад» веде на {m.group(1)}, а батько {par}')
    elif not par and m: bad_back.append(f'{p.name}: хаб вкладки, «назад» зайве')
if bad_back:
    print(f'\nієрархія — розбіжностей {len(bad_back)}:')
    for b in bad_back: print('  ' + b)
else:
    print('ієрархія: «назад» усюди веде до оголошеного батька')
