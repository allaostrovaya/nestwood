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
 ('Маршрути', [
   ('Куди можна піти','catalogue.html',[('порожній','catalogue-empty.html')], [
     ('Картка маршруту ⭐','route.html',[('порожній','route-empty.html'),('помилка','route-error.html'),('завантаження','route-loading.html')], [
       ('Карта маршруту','map.html',[('помилка','map-error.html'),('завантаження','map-loading.html'),('офлайн','map-offline.html')], []),
       ('Хижі маршруту','huts.html',[('порожній','huts-empty.html')], [
         ('Хижа','hut.html',[], []),
       ]),
       ('Нотатки з місця','field-notes.html',[('порожній','field-notes-empty.html')], []),
       ('Відгуки','reviews.html',[], []),
     ]),
     ('Зібрати маршрут','assemble.html',[], []),
   ]),
 ]),
 ('Плани', [
   ('Мої походи','plans.html',[('порожній','plans-empty.html')], [
     ('План по днях ⭐','plan.html',[('у дорозі','plan-intrip.html'),('пройдений','plan-past.html'),('порожній','plan-empty.html'),('помилка','plan-error.html'),('завантаження','plan-loading.html'),('конфлікт','plan-conflict.html'),('офлайн','plan-offline.html'),('degraded','plan-degraded.html')], [
       ('День','day.html',[('норма замість прогнозу','day-seasonal.html')], [
         ('Ніч','night.html',[('порожній','night-empty.html'),('помилка','night-error.html'),('degraded','night-degraded.html')], []),
       ]),
       ('Ночівлі — ланцюжок ночей','nights.html',[], []),
       ('Спорядження','gear.html',[], []),
       ('Дорога туди й назад','transport.html',[('порожній','transport-empty.html'),('помилка','transport-error.html'),('завантаження','transport-loading.html')], []),
       ('Що змінилось і що ще можна зробити','changes.html',[('завантаження','changes-loading.html'),('помилка','changes-error.html'),('варіантів немає','changes-nooptions.html')], []),
       ('Що лишилось закріпити','lock-in.html',[('порожній','lock-in-empty.html'),('помилка','lock-in-error.html'),('офлайн','lock-in-offline.html')], []),
       ('Офлайн-пакет','offline-pack.html',[], []),
       ('Підсумок для передачі','share.html',[], []),
       ('Сьогодні','today.html',[('офлайн','today-offline.html')], []),
       ('Зберегти похід','account.html',[], []),
       ('Попереджати про зміни','notify.html',[], []),
     ]),
   ]),
 ]),
 ('Довідник', [
   ('Довідник','guide.html',[], [
     ('Як працює ця система ночівлі','lodging-system.html',[], []),
     ('Правила й fjellvett','rules.html',[], []),
   ]),
 ]),
 ('Безпека', [
   ('Безпека','safety.html',[], [
     ('Перша допомога','first-aid.html',[], []),
   ]),
 ]),
 ('Профіль', [
   ('Я','me.html',[], [
     ('Моє спорядження','my-gear.html',[], []),
     ('Членство й ключ','membership.html',[], []),
     ('Налаштування','settings.html',[], []),
   ]),
 ]),
]

# ── похідні мапи: батько, назва, вкладка ─────────────────────
PARENT, TITLE, TAB, BASE = {}, {}, {}, {}
def _walk(nodes, tab, parent):
    for name, f, states, kids in nodes:
        clean = name.replace(' ⭐','')
        TITLE[f] = clean; TAB[f] = tab; PARENT[f] = parent; BASE[f] = f
        for slabel, sf in states:
            TITLE[sf] = clean; TAB[sf] = tab; PARENT[sf] = parent; BASE[sf] = f
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
  'map.html': 'catalogue.html', 'map-error.html': 'catalogue.html',
  'map-loading.html': 'catalogue.html', 'map-offline.html': 'plan.html',
  'lodging-system.html': 'guide.html',
  'account.html': 'plan.html', 'notify.html': 'plan.html',
  'membership.html': 'lock-in.html', 'my-gear.html': 'gear.html',
  'huts.html': 'route.html', 'huts-empty.html': 'night.html', 'hut.html': 'huts.html',
}

def topbar(current):
    """Шапка макета: ‹ назад до батька · назва екрана.
    Хаб вкладки батька не має — там лише назва.
    Аркуш замість «назад» отримує «✕ Закрити»."""
    p, pname = parent_of(current)
    title = TITLE.get(current, '')
    if current in SHEETS:
        return f'  <header class="topbar"><a class="close" href="./{SHEETS[current]}">✕ Закрити</a><span class="title">{title}</span></header>'
    back = f'<a class="back" href="./{p}">‹ {pname}</a>' if p else ''
    return f'  <header class="topbar">{back}<span class="title">{title}</span></header>'

APPNAV = '''  <nav class="tabbar" aria-label="Головна навігація">
    <ul>
      <li><a href="./catalogue.html"{m}><span class="ico" aria-hidden="true"></span>Карта</a></li>
      <li><a href="./plans.html"{p}><span class="ico" aria-hidden="true"></span>Плани{b}</a></li>
      <li><a href="./guide.html"{d}><span class="ico" aria-hidden="true"></span>Довідник</a></li>
      <li><a href="./safety.html"{x}><span class="ico" aria-hidden="true"></span>Безпека</a></li>
      <li><a href="./me.html"{f}><span class="ico" aria-hidden="true"></span>Профіль</a></li>
    </ul>
  </nav>
'''

FOOT = '''  <footer class="app">
    <p>Карти й стежки © Kartverket (CC BY 4.0) · Lantmäteriet (CC0) · Погода met.no · Транспорт Trafikverket</p>
    <details>
      <summary>Звідки це взято</summary>
      <p>{src}</p>
    </details>
    <p>Остання перевірка: 13 серпня 2026, 09:12</p>
  </footer>
'''

def tab_of(f):
    """Файл (екран або стан) → назва вкладки. Джерело — TAB, зібраний із TREE."""
    return TAB.get(f)

# Бейдж на «Планах» — єдиний лічильник продукту: компенсація за прибрану
# вкладку «Закріпити» (sitemap, рішення про пʼять вкладок). Знімається там,
# де плану немає, інакше бейдж бреше.
NOPLAN = {'plans-empty.html', 'plan-empty.html', 'catalogue-empty.html'}

def appnav_for(f):
    t = tab_of(f)
    b = '' if f in NOPLAN else '<span class="count" aria-label="лишилось закріпити: 4">4</span>'
    return APPNAV.format(b=b, m=' aria-current="page"' if t == 'Маршрути' else '',
                         p=' aria-current="page"' if t == 'Плани' else '',
                         d=' aria-current="page"' if t == 'Довідник' else '',
                         x=' aria-current="page"' if t == 'Безпека' else '',
                         f=' aria-current="page"' if t == 'Профіль' else '')

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
<html lang="uk">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>{title}</title>
<link rel="stylesheet" href="./_wireframe.css" />
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
