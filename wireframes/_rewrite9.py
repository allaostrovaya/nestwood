# -*- coding: utf-8 -*-
"""Екрани завантаження: рев'ю-навігація переїжджає з макета в рев'ю-хром.

На loading-сторінках усередині телефона стояли посилання «Якщо джерело не
відповість», «Якщо Turrutebasen мовчить», «Готова картка» — це навігація
рецензента по станах, а не кнопки застосунку: у справжньому продукті на екрані
завантаження таких кнопок немає.

Вони переїжджають у рядок позиції над макетом — там уже живе рев'ю-хром
(`data-review`). `_audit.py` і далі перевіряє, що кожен loading веде у свої
результати, але тепер дивиться на всю сторінку, а не тільки всередину `.device`.

Заразом два абзаци на plan-loading, що пояснювали нашу механіку.

    python3 wireframes/_rewrite9.py [--check]
"""
import pathlib, re, json, sys

W = pathlib.Path('wireframes')

# сторінка → (що прибрати з макета, що дописати в рядок позиції)
MOVE = {
 'plan-loading.html': (
   ' <a href="./plan-error.html">Якщо джерело не відповість</a>',
   ' · далі: <a href="./plan.html">план</a> · <a href="./plan-error.html">помилка</a>'),
 'route-loading.html': (
   '<a href="./route.html">Готова картка</a> <a href="./route-error.html">Якщо Turrutebasen мовчить</a> <a href="./route-empty.html">Якщо свідчень ще немає</a>',
   ' · далі: <a href="./route.html">успіх</a> · <a href="./route-error.html">помилка</a> · <a href="./route-empty.html">порожній</a>'),
 'map-loading.html': (
   '<a href="./map.html">Коли тайли дочитаються</a> <a href="./map-error.html">Якщо джерело не відповість</a> <a href="./map-offline.html">Що буде без мережі</a>',
   ' · далі: <a href="./map.html">карта</a> · <a href="./map-error.html">помилка</a> · <a href="./map-offline.html">офлайн</a>'),
}

# текст, що пояснював нашу механіку
T = [
 ("Вартість зʼявиться, коли будуть ночівлі й квитки: вона складається з них, а не рахується окремо.",
  'Вартість зʼявиться разом із ночівлями й квитками.', 'пояснення нашої моделі'),
 ("Вартість з'явиться, коли будуть ночівлі й квитки: вона складається з них, а не рахується окремо.",
  "Вартість зʼявиться разом із ночівлями й квитками.", 'пояснення нашої моделі'),
 ('Правити можна буде, щойно план складеться. Зараз єдина дія — скасувати генерацію, і запит при цьому не загубиться.',
  'Правити можна буде, щойно план складеться. Зараз можна тільки скасувати — запит при цьому не загубиться.',
  '«генерація» — наше слово'),
]

check = '--check' in sys.argv
log, miss = [], []

for name, (drop, add) in MOVE.items():
    p = W / name; s = p.read_text(encoding='utf-8')
    if drop not in s:
        if add.strip() not in s: miss.append(f'{name}: не знайдено «{drop[:50]}»')
        continue
    s2 = s.replace(drop, '')
    # порожній <p class="actions"></p> прибираємо
    s2 = re.sub(r'\s*<p class="actions">\s*</p>', '', s2)
    s2 = s2.replace('<i>завантаження</i></p>', '<i>завантаження</i>' + add + '</p>', 1)
    if s2 != s:
        log.append({'file': name, 'kind': 'move'})
        if not check: p.write_text(s2, encoding='utf-8')

PAGES = [q.name for q in sorted(W.glob('*.html')) if q.name not in {'_nav.html','ia.html','flow.html','index.html'}]
def span(s):
    i, j = s.find('<div class="device"'), s.find('</div><!-- /.wf-main -->')
    return (i, j) if i >= 0 and j > i else (None, None)
for old, new, why in T:
    hit = 0
    for name in PAGES:
        p = W / name; s = p.read_text(encoding='utf-8')
        i, j = span(s)
        if i is None: continue
        b = s[i:j]
        if old not in b: continue
        hit += 1; log.append({'file': name, 'kind': 'trim', 'why': why})
        if not check: p.write_text(s[:i] + b.replace(old, new) + s[j:], encoding='utf-8')

if miss:
    print('НЕ ЗБІГЛОСЬ:'); [print('  ·', m) for m in miss]
else:
    print('усі правила знайшли ціль' + ('' if log else ' — усе вже застосовано'))
print(f'правок: {len(log)}')
if not check and log:
    (W / '_rewrite9_log.json').write_text(json.dumps(log, ensure_ascii=False, indent=1), encoding='utf-8')
