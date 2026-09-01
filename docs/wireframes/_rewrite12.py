# -*- coding: utf-8 -*-
"""Останні сліди «закріпити» та «передати» після перейменування екранів."""
import pathlib, re, json, sys

W = pathlib.Path('wireframes')
SKIP = {'_nav.html', 'ia.html', 'flow.html', 'index.html'}
PAGES = [p.name for p in sorted(W.glob('*.html')) if p.name not in SKIP]

T = [
 ('Це не збій: список закріплення входить в офлайн-пакет походу.',
  'Це не збій: список входить в офлайн-пакет походу.'),
 ('тому стан закріплення мусить пережити закритий застосунок',
  'тому цей список мусить пережити закритий застосунок'),
 ('щоб формула гарантії й список закріплення рахувались правильно',
  'щоб гарантія ночівлі й список кроків рахувались правильно'),
 ('Поки він є, «закріпити» веде в глухий кут — тому позначене як заблоковане.',
  'Поки він є, список до виходу веде в глухий кут — тому позначений як заблокований.'),
 ('<a href="./lock-in.html">Закріпити</a>', '<a href="./lock-in.html">Що зробити до виходу</a>'),
 ("тут з'явиться план одразу після генерації, зі станом закріплення нічого до кінця.",
  "тут зʼявиться план одразу після того, як складеться."),
 ('параметри походу, стан закріплення й збережені маршрути',
  'параметри походу, що вже зроблено, і збережені маршрути'),
 ('<li><b>Закріплено</b> 1 із 5 ночей', '<li><b>Заброньовано</b> 1 із 5 ночей'),
 ('— ще не закріплені</li>', '— ще не заброньовані</li>'),
 ('<p>Що ми можемо — <b>передати</b>:</p>', '<p>Що можна зробити:</p>'),
]

def span(s):
    i, j = s.find('<div class="device"'), s.find('</div><!-- /.wf-main -->')
    return (i, j) if i >= 0 and j > i else (None, None)

check = '--check' in sys.argv
log, miss = [], []
for old, new in T:
    hit = 0
    for name in PAGES:
        p = W / name; s = p.read_text(encoding='utf-8')
        i, j = span(s)
        if i is None: continue
        b = s[i:j]
        if old not in b: continue
        hit += b.count(old); log.append({'file': name, 'old': old[:60]})
        if not check: p.write_text(s[:i] + b.replace(old, new) + s[j:], encoding='utf-8')
    if not hit:
        plain = re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', '', old)).strip()
        if plain and any(plain in re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', '', (W / n).read_text(encoding='utf-8')))
                         for n in PAGES): miss.append(old[:70])
print(('НЕ ЗБІГЛОСЬ: ' + '; '.join(miss)) if miss else
      'усі правила знайшли ціль' + ('' if log else ' — усе вже застосовано'))
print(f'правок: {len(log)}')
if not check and log:
    (W / '_rewrite12_log.json').write_text(json.dumps(log, ensure_ascii=False, indent=1), encoding='utf-8')
