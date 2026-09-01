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
TITLE, STATE = ns['TITLE'], ns['STATE']
files = {p.name for p in pathlib.Path('wireframes').glob('*.html')}
n = 0
for p in sorted(pathlib.Path('wireframes').glob('*.html')):
    if p.name in ('_nav.html','ia.html','flow.html','index.html'): continue
    s = p.read_text(encoding='utf-8')
    new = re.sub(r'<nav class="wf-tree".*?</nav>', lambda m: nav_html(p.name), s, flags=re.S)
    hdr = appnav_for(p.name)
    new = re.sub(r'  <header class="topbar">.*?</header>', topbar(p.name), new, flags=re.S)
    new = re.sub(r'  <nav class="tabbar".*?</nav>\n', hdr, new, flags=re.S)
    # <title> і мітка на телефоні теж походять із TREE — інакше вони розходяться
    # з назвою екрана при перейменуванні, і цього ніхто не помічає
    scr, st = TITLE.get(p.name), STATE.get(p.name)
    if scr:
        new = re.sub(r'<title>.*?</title>', f'<title>Wireframe \u00b7 {scr} \u00b7 {st}</title>', new, flags=re.S)
        new = re.sub(r'data-screen="[^"]*" data-state="[^"]*"', f'data-screen="{scr}" data-state="{st}"', new)
    if new != s: p.write_text(new, encoding='utf-8'); n += 1
print(f'дерево перегенеровано у {n} сторінках')
# канонічна копія
pathlib.Path('wireframes/_nav.html').write_text(
  '<!-- КАНОНІЧНА КОПІЯ дерева. Генерується з TREE у _generate.py.\n'
  '     Не редагувати руками: запусти python3 /tmp/refresh_nav.py -->\n' + nav_html(''), encoding='utf-8')
print('_nav.html оновлено')
