# -*- coding: utf-8 -*-
"""Перегенерація дерева навігації у ВСІХ сторінках вайрфреймів.
Єдине джерело — TREE у _generate.py. Запускати з кореня репозиторію:
    python3 wireframes/_refresh.py
Після кожної нової сторінки: додай її у TREE і запусти це."""
import importlib.util, pathlib, re
spec = importlib.util.spec_from_file_location('g','wireframes/_generate.py')
g = importlib.util.module_from_spec(spec)
import sys; sys.modules['g']=g
src = open('wireframes/_generate.py',encoding='utf-8').read()
ns = {}
exec(src.split('P = {}')[0], ns)          # тільки дані й рендерери, без запису сторінок
nav_html, TREE, appnav_for, topbar = ns['nav_html'], ns['TREE'], ns['appnav_for'], ns['topbar']
files = {p.name for p in pathlib.Path('wireframes').glob('*.html')}
n = 0
for p in sorted(pathlib.Path('wireframes').glob('*.html')):
    if p.name in ('_nav.html','ia.html','index.html'): continue
    s = p.read_text(encoding='utf-8')
    new = re.sub(r'<nav class="wf-tree".*?</nav>', lambda m: nav_html(p.name), s, flags=re.S)
    hdr = appnav_for(p.name)
    new = re.sub(r'  <header class="topbar">.*?</header>', topbar(p.name), new, flags=re.S)
    new = re.sub(r'  <header class="app">.*?Глобальна навігація[^<]*</p>\n', hdr, new, flags=re.S)
    if new != s: p.write_text(new, encoding='utf-8'); n += 1
print(f'дерево перегенеровано у {n} сторінках')
# канонічна копія
pathlib.Path('wireframes/_nav.html').write_text(
  '<!-- КАНОНІЧНА КОПІЯ дерева. Генерується з TREE у _generate.py.\n'
  '     Не редагувати руками: запусти python3 /tmp/refresh_nav.py -->\n' + nav_html(''), encoding='utf-8')
print('_nav.html оновлено')
