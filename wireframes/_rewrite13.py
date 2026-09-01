# -*- coding: utf-8 -*-
"""Назви двох екранів — фінальні, і всі входи до них уніфіковані.

«Останні кроки» — справжня фраза, зрозуміла без пояснень, і вона спонукає:
видно, що лишилось небагато.

«Сказати, куди йду» — наказова форма замість канцеляриту, майже дослівно те,
що радить DNT. Гасла на кшталт «Безпека понад усе» тут не ставимо: воно обіцяє
безпеку, якої екран не дає, і заходить у реєстр, що належить DNT і Røde Kors.

Заразом уніфіковано шість різних написів, що вели на share: навігація тепер
скрізь «Сказати, куди йду», а «Надіслати маршрут і час повернення» лишається
кнопкою самої дії всередині екрана.

    python3 wireframes/_rewrite13.py [--check]
"""
import pathlib, re, json, sys

W = pathlib.Path('wireframes')
SKIP = {'_nav.html', 'ia.html', 'flow.html', 'index.html'}
PAGES = [p.name for p in sorted(W.glob('*.html')) if p.name not in SKIP]

T = [
 ('<h1>Що зробити до виходу</h1>', '<h1>Останні кроки</h1>'),
 ('<h1>Повідомити рідних</h1>', '<h1>Сказати, куди йду</h1>'),
 ('Що зробити до виходу — 4 кроки', 'Останні кроки — лишилось 4'),
 ('>Що зробити до виходу<', '>Останні кроки<'),
 ('Що зробити до виходу</b>', 'Останні кроки</b>'),
 ('список до виходу веде в глухий кут', '«Останні кроки» ведуть у глухий кут'),
 # усі входи на share — одна назва
 ('>Поділитися планом<', '>Сказати, куди йду<'),
 ('>Поділитися<', '>Сказати, куди йду<'),
 ('>Поділитися маршрутом і часом повернення<', '>Сказати, куди йду<'),
 ('>Сказати близьким, де ми<', '>Сказати, куди йду<'),
 ('>Поділитися — маршрут і час повернення<', '>Сказати, куди йду<'),
 ('<b>Поділитися</b>', '<b>Сказати, куди йду</b>'),
 ('<b>Надіслати підсумок</b>', '<b>Сказати, куди йду</b>'),
]

def span(s):
    i, j = s.find('<div class="device"'), s.find('</div><!-- /.wf-main -->')
    return (i, j) if i >= 0 and j > i else (None, None)

check = '--check' in sys.argv
log, miss = [], []
for old, new in sorted(T, key=lambda x: -len(x[0])):
    hit = 0
    for name in PAGES:
        p = W / name; s = p.read_text(encoding='utf-8')
        i, j = span(s)
        if i is None: continue
        b = s[i:j]
        if old not in b: continue
        hit += b.count(old); log.append({'file': name, 'old': old[:55], 'new': new[:55]})
        if not check: p.write_text(s[:i] + b.replace(old, new) + s[j:], encoding='utf-8')
    if not hit:
        plain = re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', '', old)).strip()
        if plain and any(plain in re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', '', (W / n).read_text(encoding='utf-8')))
                         for n in PAGES): miss.append(old[:70])
print(('НЕ ЗБІГЛОСЬ: ' + '; '.join(miss)) if miss else
      'усі правила знайшли ціль' + ('' if log else ' — усе вже застосовано'))
print(f'правок: {len(log)} у {len({x["file"] for x in log})} сторінках')
if not check and log:
    (W / '_rewrite13_log.json').write_text(json.dumps(log, ensure_ascii=False, indent=1), encoding='utf-8')
