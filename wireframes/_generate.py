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

# ── СТРУКТУРА: розділ → екран → стани ─────────────────────────
TREE = [
 ('Карта', [
   ('Каталог','catalogue.html',[('порожній','catalogue-empty.html')]),
   ('Картка маршруту ⭐','route.html',[('порожній','route-empty.html'),('помилка','route-error.html'),('завантаження','route-loading.html')]),
   ('Умови · нотатки','field-notes.html',[('порожній','field-notes-empty.html')]),
   ('Відгуки',None,[]),
   ('Повноекранна карта','map.html',[('помилка','map-error.html'),('завантаження','map-loading.html'),('офлайн','map-offline.html')]),
   ('Зібрати маршрут',None,[]),
 ]),
 ('Плани', [
   ('Список планів','plans.html',[('порожній','plans-empty.html')]),
   ('План по днях ⭐','plan.html',[('порожній','plan-empty.html'),('помилка','plan-error.html'),('завантаження','plan-loading.html'),('конфлікт','plan-conflict.html'),('офлайн','plan-offline.html'),('degraded','plan-degraded.html')]),
   ('День','day.html',[('норма замість прогнозу','day-seasonal.html')]),
   ('Ніч: гарантія й доступ','night.html',[('порожній','night-empty.html'),('помилка','night-error.html'),('degraded','night-degraded.html')]),
   ('Ночівлі — ланцюжок','nights.html',[]),
   ('Спорядження','gear.html',[]),
   ('Транспорт','transport.html',[('порожній','transport-empty.html'),('помилка','transport-error.html'),('завантаження','transport-loading.html')]),
   ('Що змінилось','changes.html',[('завантаження','changes-loading.html'),('помилка','changes-error.html'),('варіантів немає','changes-nooptions.html')]),
   ('Що лишилось закріпити','lock-in.html',[('порожній','lock-in-empty.html'),('помилка','lock-in-error.html'),('офлайн','lock-in-offline.html')]),
   ('Офлайн-пакет',None,[]),
   ('Підсумок для передачі','share.html',[]),
   ('Сьогодні','today.html',[('офлайн','today-offline.html')]),
 ]),
 ('Довідник', [
   ('Довідник','guide.html',[]),
   ('Як працює ця система ночівлі','lodging-system.html',[]),
   ('Правила й fjellvett',None,[]),
 ]),
 ('Безпека', [
   ('Безпека · SOS','safety.html',[]),
   ('Перша допомога','first-aid.html',[]),
 ]),
 ('Профіль', [
   ('Про мене','me.html',[]),
   ('Моє спорядження','my-gear.html',[]),
   ('Членство й ключ','membership.html',[]),
   ('Налаштування',None,[]),
 ]),
]

def node(label, file, current, cls=''):
    c = f' class="{cls}"' if cls else ''
    if not file: return f'<span class="todo{" "+cls if cls else ""}">{label}</span>'
    cur = ' aria-current="page"' if file == current else ''
    return f'<a{c} href="./{file}"{cur}>{label}</a>'

def nav_html(current):
    out = ['<nav class="wf-tree" data-review lang="uk" aria-label="Структура вайрфреймів">',
           '  <h2>NESTWOOD · ВАЙРФРЕЙМИ</h2>',
           '  <ul>']
    for grp, screens in TREE:
        out.append(f'    <li><span class="grp">{grp}</span>\n      <ul>')
        for label, file, states in screens:
            out.append(f'        <li>{node(label, file, current)}')
            if states:
                out.append('          <ul>')
                for slabel, sfile in states:
                    out.append(f'            <li>{node(slabel, sfile, current, "st")}</li>')
                out.append('          </ul>')
            out.append('        </li>')
        out.append('      </ul>\n    </li>\n')
    out.append('  </ul>\n</nav>')
    return '\n'.join(out)


APPNAV = '''  <header class="app">
    <p class="brand">Nestwood</p>
    <nav aria-label="Головна навігація">
      <ul>
        <li><a href="./catalogue.html"{m}>Карта</a></li>
        <li><a href="./plans.html"{p}>Плани</a></li>
        <li><a href="./guide.html"{d}>Довідник</a></li>
        <li><a href="./safety.html"{x}>Безпека</a></li>
        <li><a href="./me.html"{f}>Профіль</a></li>
      </ul>
    </nav>
  </header>
  <p class="ann" data-review lang="uk">ЗОНА · Глобальна навігація — пʼять вкладок. Незмінна в усіх станах: стан екрана ніколи не чіпає оболонку. Дім контекстний: «Плани», коли похід активний або старт за день-два, «Карта» в решті випадків. Сірим — вкладки, чиї екрани ще не намальовані: посилання на них не ставимо, щоб не робити 404-тупик.</p>
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
    """Файл (екран або стан) → назва вкладки. Джерело — TREE."""
    for tab, screens in TREE:
        for _, sf, states in screens:
            if f == sf or f in [s[1] for s in states]: return tab
    return None

def appnav_for(f):
    t = tab_of(f)
    return APPNAV.format(m=' aria-current="page"' if t == 'Карта' else '',
                         p=' aria-current="page"' if t == 'Плани' else '',
                         d=' aria-current="page"' if t == 'Довідник' else '',
                         x=' aria-current="page"' if t == 'Безпека' else '',
                         f=' aria-current="page"' if t == 'Профіль' else '')

def R(state, flow, rule, extra=''):
    """Згорнута шапка сторінки — третій елемент рев'ю-хрому."""
    return f"""  <summary>{state}</summary>
  <div class="review-body">
    <p><b>Місце у flow:</b> {flow}</p>
    <p><b>Правило стану:</b> {rule}</p>
    {extra}
  </div>"""

def zone(zid, head, body, ann):
    return (f'    <section aria-labelledby="{zid}">\n      <h2 id="{zid}">{head}</h2>\n{body}\n    </section>\n'
            f'    <p class="ann" data-review lang="uk">ЗОНА · {ann}</p>\n')

def page(current, title, h1, review, zones, src, appnav=True, base=None):
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
{review}
</details>

<div class="device" data-screen="{screen}" data-state="{state}">

{nav}
  <main>
    <h1>{h1}</h1>

{zones}
  </main>

{FOOT.format(src=src)}
</div>

<p class="ann ann-out" data-review lang="uk">ЗОНА · Футер оболонки. Атрибуція ©Kartverket є <b>в кожному стані</b> — це юридична вимога CC BY 4.0, а не підпис.</p>

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
