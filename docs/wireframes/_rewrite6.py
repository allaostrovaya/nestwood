# -*- coding: utf-8 -*-
"""Каталог: лічильник цифрою, описи маршрутів — про маршрут.

Рядок під заголовком пояснював порядок сортування; лишається кількість.
Другий рядок кожної картки казав, як маршрут збігається з запитом («сходиться
повністю», «не проходить за фільтром»), а не який він. Тепер він називає те, що
допомагає обрати: характер стежки, чим цей маршрут відрізняється від сусіднього
в списку, і практичну умову — транспорт або сезон човнів.

    python3 wireframes/_rewrite6.py [--check]
"""
import pathlib, re, json, sys

W = pathlib.Path('wireframes')
SKIP = {'_nav.html', 'ia.html', 'flow.html', 'index.html'}
PAGES = [p.name for p in sorted(W.glob('*.html')) if p.name not in SKIP]

EDITS = [
 ('<p>6 маршрутів · спершу ті, де сходяться місяць, тривалість і режим ночівлі.</p>',
  '<p>6 маршрутів</p>', 'лічильник цифрою, без пояснення сортування'),

 ('<small>Сходиться повністю: серпень у сезоні, дах щоночі, потяг до старту й автобус із фінішу</small>',
  '<small>Мостки над болотами, перевал Tjäktjapasset і два броди. Потяг просто до старту, автобус із фінішу</small>',
  'опис маршруту замість збігу з запитом'),

 ('<small>Той самий маршрут без останнього дня — якщо вихід із Kebnekaise вертольотом або пішки в Nikkaluokta</small>',
  '<small>Та сама стежка без останнього дня. З Kebnekaise далі — вертоліт або 19 км пішки до Nikkaluokta</small>',
  'конкретніше, чим відрізняється'),

 ('<small>Рівніший за Kungsleden, але довший; човни на початку й у кінці ходять за розкладом до 20 вересня</small>',
  '<small>Рівніший за Kungsleden, майже без набору висоти. На початку й у кінці — човен, ходить до 20 вересня</small>',
  'характер маршруту + практична умова'),

 ('<small>Не проходить за фільтром «ночівля в хижах»: показуємо, бо решта запиту сходиться, і позначаємо, чим саме відрізняється</small>',
  '<small>Ліс і озера замість гір, за годину від Стокгольма — і жодного перевалу</small>',
  'опис маршруту замість пояснення фільтра'),

 # той самий клас у списку хиж
 ('<small>Поза стежкою: показуємо як запас на випадок, коли Sälka переповнена</small>',
  '<small>Поза стежкою — запас на випадок, коли Sälka переповнена</small>',
  '«показуємо» — наша дія, не факт про хижу'),
 ('<small>У плані стоїть як прохідна — але це запасний дах, якщо день 5 не дотягнете</small>',
  '<small>Прохідна, але це запасний дах, якщо день 5 не дотягнеш</small>',
  'звертання + прибрано «у плані стоїть»'),
]

def span(s):
    i, j = s.find('<div class="device"'), s.find('</div><!-- /.wf-main -->')
    return (i, j) if i >= 0 and j > i else (None, None)

check = '--check' in sys.argv
log, miss = [], []
for old, new, why in EDITS:
    hit = 0
    for name in PAGES:
        p = W / name; s = p.read_text(encoding='utf-8')
        i, j = span(s)
        if i is None: continue
        b = s[i:j]
        if old not in b: continue
        hit += b.count(old)
        log.append({'file': name, 'why': why})
        if not check: p.write_text(s[:i] + b.replace(old, new) + s[j:], encoding='utf-8')
    if not hit and any(old in (W / n).read_text(encoding='utf-8') for n in PAGES):
        miss.append(old[:80])

print(('НЕ ЗБІГЛОСЬ: ' + '; '.join(miss)) if miss
      else 'усі правила знайшли ціль' + ('' if log else ' — усе вже застосовано'))
print(f'правок: {len(log)} у {len({x["file"] for x in log})} сторінках')
if not check and log:
    (W / '_rewrite6_log.json').write_text(json.dumps(log, ensure_ascii=False, indent=1), encoding='utf-8')
