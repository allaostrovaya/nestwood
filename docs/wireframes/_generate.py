# -*- coding: utf-8 -*-
"""Структура набору вайрфреймів: TREE, дерево навігації, шапка застосунку, каркас сторінки.

Це НЕ фабрика сторінок. Вміст екранів живе у самих файлах; тут — те, що мусить
бути однаковим усюди, і те, що читає _refresh.py. Джерело структури — sitemap.md.

Нова сторінка: додай запис у TREE (файлом або None, якщо ще не намальована),
створи файл за каркасом page() і запусти python3 wireframes/_refresh.py."""
import pathlib, re, importlib.util
W = pathlib.Path('wireframes')

# глобальна навігація по документах — спільний рендерер, не копія
_s = importlib.util.spec_from_file_location('gnav', 'design-system/docs/gnav.py')
_g = importlib.util.module_from_spec(_s); _s.loader.exec_module(_g)
GNAV = _g.gnav('wireframes', '../')

# ── СТРУКТУРА ────────────────────────────────────────────────
# вкладка → хаб → заглиблення. Вузол: (назва, файл, [стани], [діти]).
# Назва екрана = те, що написано на ньому (h1), крім екранів одного
# обʼєкта (маршрут, день, ніч, відгуки) — там h1 показує назву обʼєкта.
# Батько виводиться з вкладеності: «‹ назад» веде саме до нього.
TREE = [
 ('Map', [
   ('Where to go','catalogue.html',[('порожній','catalogue-empty.html')], [
     ('New plan ⭐','new-plan.html',[('генерація','new-plan-loading.html'),('неможливий маршрут','new-plan-conflict.html'),('помилка','new-plan-error.html')], [
       ('Another hut','huts.html',[('порожній','huts-empty.html')], [
         ('Hut','hut.html',[], []),
       ]),
       ('Notes and reviews','notes.html',[('порожній','notes-empty.html')], []),
     ]),
   ]),
 ]),
 ('Plans', [
   ('My trips','plans.html',[('порожній','plans-empty.html')], [
     ('Plan ⭐','plan.html',[('пройдений','plan-past.html'),('помилка','plan-error.html'),('офлайн','plan-offline.html')], [
       ('Day','day.html',[('норма замість прогнозу','day-seasonal.html'),('сьогодні','day-intrip.html'),('офлайн','day-offline.html')], [
         ('Book','booking.html',[], []),
       ]),
       ('Gear','gear.html',[], []),
       ('Share my route','share.html',[], []),
     ]),
   ]),
 ]),
 ('Guide', [
   ('Guide','guide.html',[], [
     ('Article','lodging-system.html',[], []),
   ]),
 ]),
 ('Safety', [
   ('Safety','safety.html',[], [
     ('First aid','first-aid.html',[], []),
   ]),
 ]),
 ('Profile', [
   ('Profile','me.html',[], [
     ('My gear','my-gear.html',[], []),
     ('Membership and key','membership.html',[], []),
     ('Settings','settings.html',[], [
       ('Sign in','account.html',[], []),
     ]),
   ]),
 ]),
]


# ── похідні мапи: батько, назва, вкладка ─────────────────────
PARENT, TITLE, TAB, BASE, STATE = {}, {}, {}, {}, {}
def _walk(nodes, tab, parent):
    for name, f, states, kids in nodes:
        clean = name.replace(' ⭐','')
        TITLE[f] = clean; TAB[f] = tab; PARENT[f] = parent; BASE[f] = f; STATE[f] = 'успіх'
        for slabel, sf in states:
            TITLE[sf] = clean; TAB[sf] = tab; PARENT[sf] = parent; BASE[sf] = f; STATE[sf] = slabel
        _walk(kids, tab, f)
for _tab, _nodes in TREE:
    _walk(_nodes, _tab, None)

def parent_of(f):
    """Файл → (файл батька, його назва). Хаб вкладки батька не має."""
    p = PARENT.get(BASE.get(f, f))
    return (p, TITLE[p]) if p else (None, None)

def node(label, file, current, cls=''):
    c = f' class="{cls}"' if cls else ''
    if not file: return f'<span class="todo{" "+cls if cls else ""}">{label}</span>'
    cur = ' aria-current="page"' if file == current else ''
    return f'<a{c} href="./{file}"{cur}>{label}</a>'

def _branch(nodes, current, depth=0):
    """Рекурсія: вкладеність у дереві = ієрархія екранів."""
    out = ['  ' * (depth + 3) + '<ul>']
    for label, file, states, kids in nodes:
        out.append('  ' * (depth + 4) + f'<li>{node(label, file, current)}')
        if states or kids:
            inner = []
            if states:
                inner.append('  ' * (depth + 5) + '<ul class="states">')
                for slabel, sfile in states:
                    inner.append('  ' * (depth + 6) + f'<li>{node(slabel, sfile, current, "st")}</li>')
                inner.append('  ' * (depth + 5) + '</ul>')
            if kids:
                inner.append(_branch(kids, current, depth + 2))
            out.extend(inner)
        out.append('  ' * (depth + 4) + '</li>')
    out.append('  ' * (depth + 3) + '</ul>')
    return '\n'.join(out)

def nav_html(current):
    out = ['<nav class="wf-tree" data-review lang="uk" aria-label="Структура вайрфреймів">',
           '  <h2>NESTWOOD · ВАЙРФРЕЙМИ</h2>',
           '  <ul>']
    for grp, nodes in TREE:
        out.append(f'    <li><span class="grp">{grp}</span>')
        out.append(_branch(nodes, current))
        out.append('    </li>')
    out.append('  </ul>\n</nav>')
    return '\n'.join(out)

# ── аркуші (рівень 4) ────────────────────────────────────────
# Екран, який відкривається з кількох різних контекстів і мусить
# повертати туди, звідки прийшли, а не до «свого» батька. Керування —
# «✕ Закрити», не «‹ назад». У статичному макеті href веде до
# найчастішого відкривача, бо стека в нас немає.
SHEETS = {
  'account.html': 'settings.html',
  'huts.html': 'new-plan.html', 'huts-empty.html': 'new-plan.html', 'hut.html': 'huts.html',
  'notes.html': 'new-plan.html', 'notes-empty.html': 'day.html',
  'booking.html': 'day.html',
  'membership.html': 'plan.html', 'my-gear.html': 'gear.html',
}

# дія праворуч у шапці: шестерня налаштувань у профілі, як у Strava / Komoot / AllTrails
TOPBAR_ACT = {
  'me.html': '<a class="act" href="./settings.html" aria-label="Settings"><svg class="gear" width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#4a4a4a" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="3"/><path d="M19.4 15a1.7 1.7 0 0 0 .3 1.8l.1.1a2 2 0 1 1-2.8 2.8l-.1-.1a1.7 1.7 0 0 0-1.8-.3 1.7 1.7 0 0 0-1 1.5V21a2 2 0 1 1-4 0v-.1a1.7 1.7 0 0 0-1.1-1.5 1.7 1.7 0 0 0-1.8.3l-.1.1a2 2 0 1 1-2.8-2.8l.1-.1a1.7 1.7 0 0 0 .3-1.8 1.7 1.7 0 0 0-1.5-1H3a2 2 0 1 1 0-4h.1a1.7 1.7 0 0 0 1.5-1.1 1.7 1.7 0 0 0-.3-1.8l-.1-.1a2 2 0 1 1 2.8-2.8l.1.1a1.7 1.7 0 0 0 1.8.3H9a1.7 1.7 0 0 0 1-1.5V3a2 2 0 1 1 4 0v.1a1.7 1.7 0 0 0 1 1.5 1.7 1.7 0 0 0 1.8-.3l.1-.1a2 2 0 1 1 2.8 2.8l-.1.1a1.7 1.7 0 0 0-.3 1.8V9a1.7 1.7 0 0 0 1.5 1H21a2 2 0 1 1 0 4h-.1a1.7 1.7 0 0 0-1.5 1z"/></svg></a>',
}

def topbar(current):
    """Шапка макета: ‹ назад до батька · назва екрана.
    Хаб вкладки батька не має — там лише назва.
    Аркуш замість «назад» отримує «✕ Закрити»."""
    p, pname = parent_of(current)
    title = TITLE.get(current, '')
    if current in SHEETS:
        return f'  <header class="topbar"><a class="close" href="./{SHEETS[current]}">✕ Close</a><span class="title">{title}</span></header>'
    back = f'<a class="back" href="./{p}">‹ {pname}</a>' if p else ''
    act = TOPBAR_ACT.get(current, '')
    return f'  <header class="topbar">{back}<span class="title">{title}</span>{act}</header>'

APPNAV = '''  <nav class="tabbar" aria-label="Main navigation">
    <ul>
      <li><a href="./catalogue.html"{m}><span class="ico" aria-hidden="true"></span>Map</a></li>
      <li><a href="./plans.html"{p}><span class="ico" aria-hidden="true"></span>Plans{b}</a></li>
      <li><a href="./guide.html"{d}><span class="ico" aria-hidden="true"></span>Guide</a></li>
      <li><a href="./safety.html"{x}><span class="ico" aria-hidden="true"></span>Safety</a></li>
      <li><a href="./me.html"{f}><span class="ico" aria-hidden="true"></span>Profile</a></li>
    </ul>
  </nav>
'''

FOOT = '''  <footer class="app">
    <p>Maps and trails © Kartverket (CC BY 4.0) · Lantmäteriet (CC0) · Weather met.no · Transport Trafikverket</p>
    <details>
      <summary>Where this comes from</summary>
      <p>{src}</p>
    </details>
    <p>Last checked: 13 August 2026, 09:12</p>
  </footer>
'''

def tab_of(f):
    """Файл (екран або стан) → назва вкладки. Джерело — TAB, зібраний із TREE."""
    return TAB.get(f)

# Бейдж на «Планах» — єдиний лічильник продукту: компенсація за прибрану
# вкладку «Закріпити» (sitemap, рішення про пʼять вкладок). Знімається там,
# де плану немає, інакше бейдж бреше.
NOPLAN = {'plans-empty.html', 'catalogue-empty.html', 'new-plan.html', 'new-plan-loading.html', 'new-plan-conflict.html', 'new-plan-error.html'}

def appnav_for(f):
    t = tab_of(f)
    b = '' if f in NOPLAN else '<span class="count" aria-label="4 steps left">4</span>'
    return APPNAV.format(b=b, m=' aria-current="page"' if t == 'Map' else '',
                         p=' aria-current="page"' if t == 'Plans' else '',
                         d=' aria-current="page"' if t == 'Guide' else '',
                         x=' aria-current="page"' if t == 'Safety' else '',
                         f=' aria-current="page"' if t == 'Profile' else '')

def zone(zid, head, body):
    """Смислова зона екрана. Анотацій тут немає: у макеті — лише семантика
    самого застосунку, а не коментарі розробників."""
    return f'    <section aria-labelledby="{zid}">\n      <h2 id="{zid}">{head}</h2>\n{body}\n    </section>\n'

def meta(pos, title, state='успіх'):
    """Єдиний рев'ю-хром усередині сторінки: позиція <джоб>.<крок>."""
    return f'<p class="meta" data-review lang="uk"><b>{pos}</b> · {title} · <i>{state}</i></p>' 

def page(current, title, h1, metaline, zones, src, appnav=True, base=None):
    nav = appnav_for(current) if appnav else ''
    parts = title.split(' · ')
    screen, state = (parts[1] if len(parts) > 1 else title), (parts[2] if len(parts) > 2 else 'успіх')
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>{title}</title>
<link rel="stylesheet" href="./_wireframe.css?v=20260924" />
<link rel="stylesheet" href="../design-system/docs/globalnav.css" />
</head>
<body>

{GNAV}

<div class="wf-shell">

{nav_html(current)}

<div class="wf-main">

<details class="review" data-review lang="uk" id="top" open>
{metaline}
</details>

<div class="device" data-screen="{screen}" data-state="{state}">
  <div class="screen">
  <header class="topbar"><p class="brand">Nestwood</p></header>
  <main>
    <h1>{h1}</h1>

{zones}
  </main>

{FOOT.format(src=src)}
  </div>
{nav}</div>

</div><!-- /.wf-main -->
</div><!-- /.wf-shell -->

</body>
</html>
'''

# ── каркас для нової сторінки ─────────────────────────────────
# Приклад: python3 -c "import importlib.util,sys; \
#   spec=importlib.util.spec_from_file_location('g','wireframes/_generate.py'); \
#   g=importlib.util.module_from_spec(spec); spec.loader.exec_module(g); \
#   open('wireframes/нова.html','w').write(g.page('нова.html', 'Wireframe · Назва · успіх', 'H1', review, zones, src))"
