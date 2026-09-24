# -*- coding: utf-8 -*-
"""Таблиця правди по мікрокопі: увесь текст інтерфейсу з макетів + позначки розбіжностей.

Витягається ТІЛЬКИ те, що всередині .device — дерево навігації, глобальна навігація
по документах і рядок позиції над макетом це рев'ю-хром, а не інтерфейс продукту.

Кластери дій, вердикти по зіткненнях і коментарі в розділах 3–9 — ручні: вони
тримають судження, якого з розмітки не видно. Правити треба їх, а не microcopy.md.

Запуск із кореня репозиторію:
    python3 wireframes/_microcopy.py
"""
import pathlib, re, json, html, collections, importlib.util
from html.parser import HTMLParser

W = pathlib.Path('wireframes')
SKIP = {'_nav.html', 'ia.html', 'flow.html', 'index.html'}
PAGES = sorted(p for p in W.glob('*.html') if p.name not in SKIP)

BLOCK = {'h1','h2','h3','p','li','dt','dd','button','label','summary','figcaption',
         'th','td','strong','small','span','a'}
# ці блоки віднімаються з тексту батька, щоб рядок не дублювався
PULL_OUT = {'small', 'count'}   # 'count' — за класом, не за тегом
VOID = {'br','img','input','hr','meta','link'}

STATES = {'empty':'порожній','error':'помилка','loading':'завантаження','offline':'офлайн',
          'degraded':'degraded','conflict':'конфлікт','seasonal':'сезонна норма',
          'nooptions':'варіантів немає','intrip':'у дорозі','past':'пройдений'}

class Ex(HTMLParser):
    def __init__(self, page):
        super().__init__(convert_charrefs=True)
        self.page = page
        self.rows = []
        self.stack = []          # [(tag, attrs)]
        self.buf = []            # [{'tag','attrs','own','all'}]
        self.in_device = False
        self.zone = '—'
        self.pending_zone_h2 = False
        self.region = None       # шапка / футер / таббар

    def ctx(self, cls=None, tag=None):
        for t, a in reversed(self.stack):
            c = a.get('class', '')
            if cls and cls in c.split(): return True
            if tag and t == tag: return True
        return False

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        cls = a.get('class', '').split()
        if 'device' in cls: self.in_device = True
        if not self.in_device:
            if tag not in VOID: self.stack.append((tag, a))
            return
        if 'topbar' in cls: self.region = 'шапка'
        if tag == 'footer' and 'app' in cls: self.region = 'футер'; self.zone = 'футер'
        if 'tabbar' in cls: self.region = 'таббар'; self.zone = 'таббар'
        if tag == 'section':
            self.zone = '?'; self.pending_zone_h2 = True; self.region = None
        # плейсхолдери полів
        ph = a.get('placeholder')
        if ph: self.emit_raw(ph, 'плейсхолдер поля')
        fit = a.get('data-fit')
        if fit: self.emit_raw(fit, 'заглушка макета')
        if tag in VOID: return
        self.stack.append((tag, a))
        if tag in BLOCK:
            self.buf.append({'tag': tag, 'attrs': a, 'own': [], 'all': []})

    def handle_data(self, d):
        if not self.in_device or not d.strip(): return
        if self.buf:
            self.buf[-1]['own'].append(d); self.buf[-1]['all'].append(d)

    def handle_endtag(self, tag):
        if tag in VOID: return
        if self.in_device and self.buf and self.buf[-1]['tag'] == tag:
            b = self.buf.pop()
            own = ' '.join(b['own']); alltxt = ' '.join(b['all'])
            txt = re.sub(r'\s+', ' ', alltxt).strip()
            if own.strip() and txt:
                self.emit(b, txt)
            pull = tag in PULL_OUT or 'count' in b['attrs'].get('class','').split()
            if self.buf and not pull:
                self.buf[-1]['all'].append(alltxt)
        if self.stack and self.stack[-1][0] == tag:
            _, a = self.stack.pop()
            cls = a.get('class', '').split()
            if 'device' in cls: self.in_device = False
            if 'topbar' in cls or (tag == 'footer' and 'app' in cls) or 'tabbar' in cls:
                self.region = None
        if tag == 'section': self.zone = '—'

    def emit_raw(self, txt, typ):
        self.rows.append({'zone': self.zone, 'text': re.sub(r'\s+', ' ', txt).strip(), 'type': typ})

    def emit(self, b, txt):
        tag, a = b['tag'], b['attrs']
        cls = a.get('class', '').split()
        typ = None
        if self.region == 'шапка':
            typ = 'заголовок екрана' if 'title' in cls else 'кнопка'
        elif self.region == 'таббар':
            typ = 'кнопка'
        elif self.region == 'футер':
            typ = 'розкривач' if tag == 'summary' else 'атрибуція'
        elif tag == 'h1': typ = 'заголовок екрана'
        elif tag == 'h2':
            typ = 'заголовок зони'
            if self.pending_zone_h2: self.zone = txt; self.pending_zone_h2 = False
        elif tag == 'h3': typ = 'заголовок блоку'
        elif tag in ('button',) or 'cta' in cls: typ = 'кнопка'
        elif tag == 'a' and self.ctx(cls='actions'): typ = 'кнопка'
        elif tag == 'a': typ = 'посилання'
        elif tag in ('label', 'dt', 'th'): typ = 'підпис поля'
        elif tag == 'dd': typ = 'значення поля'
        elif tag == 'summary': typ = 'розкривач'
        elif tag == 'figcaption': typ = 'підпис'
        elif tag == 'small' and 'data-mock' in a: typ = 'позначка мок-даних'
        elif tag == 'small': typ = 'підпис'
        elif tag == 'span' and self.ctx(cls='frame'): typ = 'заглушка макета'
        elif tag == 'span' and 'count' in cls: typ = 'лічильник'
        elif tag == 'span' and 'state' in cls: typ = 'індикатор'
        elif tag == 'span' and (self.ctx(cls='actions') or self.ctx(cls='cta')): typ = 'кнопка'
        elif tag == 'span' and self.ctx(tag='a'): typ = 'пункт списку'
        elif tag == 'span' and self.ctx(tag='button'): typ = 'кнопка'
        elif tag == 'span': typ = 'підпис'
        elif tag == 'strong' and self.ctx(cls='verdict'): typ = 'повідомлення стану'
        elif tag == 'p' and self.ctx(cls='verdict'): typ = 'повідомлення стану'
        elif tag == 'p' and self.ctx(cls='note'): typ = 'примітка'
        elif tag == 'li' and self.ctx(cls='signals'): typ = 'сигнал'
        elif tag == 'li': typ = 'пункт списку'
        elif tag == 'p': typ = 'текст'
        elif tag == 'td': typ = 'значення поля'
        else: typ = tag
        if self.zone == '?': self.zone = '—'
        self.rows.append({'zone': self.zone, 'text': txt, 'type': typ})

out = []
for p in PAGES:
    stem = p.name[:-5]
    base, state = stem, ''
    for suf, lbl in STATES.items():
        if stem.endswith('-' + suf): base, state = stem[:-len(suf)-1], lbl
    e = Ex(p.name); e.feed(p.read_text(encoding='utf-8'))
    for r in e.rows:
        r.update(file=p.name, screen=base, state=state)
        out.append(r)

rows = out

# журнал перепису за voice.md — звідки беруться колонки «було» / «стало»
_lg = W / '_rewrite_log.json'
REWRITE = json.loads(_lg.read_text(encoding='utf-8')) if _lg.exists() else []
CHANGED = {(r['file'], r['new']) for r in REWRITE}

# TREE — щоб згрупувати екрани за вкладками так само, як у решті набору
_sp = importlib.util.spec_from_file_location('g', 'wireframes/_generate.py')
g = importlib.util.module_from_spec(_sp); _sp.loader.exec_module(g)

# -*- coding: utf-8 -*-
import json, re, collections, pathlib, importlib.util

# ── що виноситься з таблиці як глобальний хром ───────────────
TABBAR = {'Map', 'Plans', 'Guide', 'Safety', 'Profile', '4'}
ATTR = 'Maps and trails © Kartverket (CC BY 4.0) · Lantmäteriet (CC0) · Weather met.no · Transport Trafikverket'
CHROME_TS = 'Last checked: 13 August 2026, 09:12'
def is_chrome(r):
    if r['zone'] == 'таббар' and r['text'] in TABBAR: return True
    if r['text'] == ATTR or r['text'] == 'Where this comes from' or r['text'] == CHROME_TS: return True
    return False

# ── позначки ─────────────────────────────────────────────────
# Інтерфейс англійський з 2026-09-24, тож словники нижче — англійські написи.
# Кластер Д* — усі написи, якими можна назвати ОДНУ дію. Зараз у наборі кожна дія
# має один напис; кластер тримає відомі синоніми, щоб дрейф було видно одразу.
EDITORIAL = {'guide.html', 'lodging-system.html', 'first-aid.html'}

SHARE = {'Share my route', 'Share route', 'Share plan', 'Share my plan', 'Send my route',
         'Tell someone where you’re going', 'Share trip'}
BOOK = {'Book', 'book', 'Book now', 'Book this night', 'Reserve', 'Lock in', 'Secure',
        'Open STF booking ↗', 'Open DNT booking ↗'}
MAKE = {'Make a plan', 'Make my plan', 'Create plan', 'Generate plan', 'Build a plan',
        'Plan again from this trip', 'Plan this trip'}
SWAP = {'Stay here on night 4', 'Another hut', 'Change hut', 'Swap night', 'Replace night',
        'Use this hut'}
PLANOPEN = {'Open plan', 'View plan', 'Back to plan', 'My trips', 'Open trip'}
GEAR = {'Gear', 'My gear', 'Open inventory', 'Packing list', 'Checklist', 'Open checklist'}
TODAY = {'Today', 'Open today', 'Today’s leg', 'Back to today'}
NOTES = {'Field notes', 'Write a field note', 'All field notes', 'Add a note'}
REV = {'Reviews', 'All reviews', 'Route reviews'}
BAIL = {'Nearest bail-out point', 'Bail-out points', 'Exit points'}
RETRY = {'Try again', 'Retry', 'Reload', 'Refresh'}
SIGNOUT = {'Sign out', 'Log out', 'Log off', 'Sign off'}

ACT = [('Д1', SHARE), ('Д2', BOOK), ('Д3', MAKE), ('Д4', SWAP), ('Д5', PLANOPEN), ('Д6', GEAR),
       ('Д7', TODAY), ('Д8', NOTES), ('Д9', REV), ('Д10', BAIL), ('Д11', RETRY), ('Д12', SIGNOUT)]

RX_S1 = re.compile(r'\btrek\w*|\bjourney\w*|\bitinerar\w*', re.I)  # проти пари «plan» (документ) / «trip» (подія)
RX_S2 = re.compile(r'\bpath\w*|\btrack\w*', re.I)                              # проти «route» / «trail»
RX_S3 = re.compile(r'checklist\w*|inventor\w*|packing list', re.I)             # проти «gear»
RX_S5 = re.compile(r'\bstages?\b|\bsegments?\b', re.I)                        # проти «day» / «leg» / «section»
RX_JARGON = re.compile(r'lock-in|\btiles?\b|\bAPI\b|PMTiles|\bpush\b|\bstep \d+\b|\.html\b', re.I)
RX_EMOJI = re.compile(r'[⚠✅✓✗✘✖✔❌✕\U0001F300-\U0001FAFF]')
RX_PLACEHOLDER = re.compile(r'quote with attribution|Signs ·|Not our text|lorem ipsum|TBD|TODO', re.I)

def flags(r):
    f = []
    t = r['text']
    if r['file'] in EDITORIAL: f.append('Р')
    if r['type'] == 'заглушка макета': f.append('З1')
    if RX_PLACEHOLDER.search(t) and r['zone'] != 'футер' and r['type'] != 'атрибуція':
        f.append('З2')
    if RX_EMOJI.search(t): f.append('Т1')
    if RX_JARGON.search(t): f.append('Ж')
    if r['type'] != 'заглушка макета' and 'photo · ' not in t:   # опис рамки — не текст продукту
        if RX_S1.search(t): f.append('С1')
        if RX_S2.search(t): f.append('С2')
        if RX_S3.search(t): f.append('С3')
        if RX_S5.search(t): f.append('С5')
    for code, s in ACT:
        if t in s: f.append(code)
    return f
for r in rows: r['flags'] = flags(r)

# ── групування: вкладка → базовий екран → стан ───────────────
TABORDER = ['Map', 'Plans', 'Guide', 'Safety', 'Profile']
FLOW = ['catalogue.html','new-plan-loading.html','new-plan.html','huts.html','account.html',
        'plan.html','day.html','day-intrip.html']
byfile = collections.OrderedDict()
for r in rows:
    byfile.setdefault(r['file'], []).append(r)

def esc(s): return s.replace('|', '\\|')

order = []
for tab in TABORDER:
    fs = [f for f in byfile if g.TAB.get(f) == tab]
    bases = []
    for f in fs:
        b = g.BASE.get(f, f)
        if b not in bases: bases.append(b)
    for b in sorted(bases, key=lambda x: (FLOW.index(x) if x in FLOW else 99, x)):
        fam = [f for f in fs if g.BASE.get(f, f) == b]
        order.append((tab, b, sorted(fam, key=lambda x: (x != b, x))))

out = []
A = out.append

tbl = [r for r in rows if not is_chrome(r)]
nchrome = len(rows) - len(tbl)
uniq = len({r['text'] for r in rows})
flagged = [r for r in tbl if r['flags']]

A('# microcopy.md — увесь текст інтерфейсу Nestwood')
A('')
A(f'**{len(byfile)} екранів · {len(rows)} рядків тексту · {uniq} унікальних.** Це перепис того, що '
  f'зараз написано в макетах, без жодної правки. До кінця роботи над флоу він має стати таблицею, '
  f'з якою звіряється кожен рядок продукту.')
A('')
A('## Як це зібрано')
A('')
A('Витягнуто скриптом із `wireframes/*.html` — **тільки те, що всередині `.device`**. Дерево '
  'навігації, глобальна навігація по документах і рядок позиції над макетом це рев\'ю-хром, а не '
  'інтерфейс продукту, тому їх тут немає. `ia.html` і `flow.html` — документи, не екрани, теж поза.')
A('')
A('**Тип рядка** визначено за розміткою, а не на око: `h1` → заголовок екрана, `h2` → заголовок '
  'зони, `button`/`a.cta` → кнопка, `label`/`dt` → підпис поля, `.verdict` → повідомлення стану, '
  '`small[data-mock]` → позначка мок-даних, `.frame > span` → заглушка макета, `span.state` → '
  'індикатор.')
A('')
A('**Зона** — це заголовок `h2` тієї секції, у якій рядок стоїть. Там, де зони немає (шапка, футер, '
  'таббар, `h1` над секціями), стоїть назва області або `—`.')
A('')
A('⚠️ **Тут нічого не переписано.** Колонка «Позначки» лише вказує на розбіжність; що з нею робити — '
  'окреме рішення, і воно ще не ухвалене.')
A('')
A('**Правила, з якими це звіряється**, — [../design-system/voice.md](../design-system/voice.md): '
  'пʼять принципів голосу, кожен виведений з рядка в дослідженні. Ця таблиця — інвентар, voice.md — '
  'правила; розбіжність `plan` / `trip` не розвʼязується жодним із них і лишається питанням '
  'глосарія.')
A('')
A('## Словник позначок')
A('')
A('| Код | Що означає |')
A('|---|---|')
A('| `С1` | той самий обʼєкт: **«trek», «journey», «itinerary»** проти пари «plan» (документ) / «trip» (подія) |')
A('| `С2` | той самий обʼєкт: **«path», «track»** проти «route» / «trail» |')
A('| `С3` | той самий обʼєкт: **«checklist», «inventory», «packing list»** проти «gear» |')
A('| `С5` | той самий обʼєкт: **«stage», «segment»** проти «day» / «leg» / «section» |')
A('| `Д1`–`Д12` | та сама дія під різними назвами кнопок — розшифровка в розділі 4 |')
A('| `Т1` | піктограма або емодзі в тексті продукту |')
A('| `Ж` | технічний жаргон або витік службової назви екрана чи файлу |')
A('| `З1` | заглушка макета — опис того, що буде намальовано в рамці |')
A('| `З2` | текст-заглушка замість змісту, якого ще немає |')
A('| `Р` | **редакційний текст** — пише автор статей або третя сторона, не продуктовий копірайтер |')
A('')
A('Позначка `✎` («переписано за voice.md») була в українській версії й зникла разом із нею: '
  'переклад 2026-09-24 замінив увесь текст, тож було/стало з `_rewrite.py` більше ні на що не вказує.')
A('')

# ── перепис за voice.md ──────────────────────────────────────
if False:  # українська історія переписів — див. легенду
    A('---')
    A('')
    A('## Перепис за voice.md — було / стало')
    A('')
    files = sorted({r['file'] for r in REWRITE})
    A(f'{sum(r["n"] for r in REWRITE)} замін на {len(files)} сторінках, '
      f'{len({r["old"] for r in REWRITE})} правил. Змінено **тільки текст**: розмітка, зони, '
      'порядок секцій і навігація не чіпались, аудит лишився на нулі. Застосовує '
      '`_rewrite.py`, там же лежать самі правила — правити треба їх, а не цей файл.')
    A('')
    A('Обсяг: десять екранів головного флоу та їхні стани `-empty`, `-error`, `-loading`.')
    A('')
    def bucket(w):
        if w.startswith('звертання'): return 'Звертання — «ти» замість «ви»'
        if w.startswith('словник'): return 'Словник — одне поняття, одне слово'
        if w.startswith('Д') or 'одна назва' in w or 'екран так і зветься' in w:
            return 'Кнопки — одна дія, одна назва'
        return 'Заборонене'
    groups = {}
    for r in REWRITE: groups.setdefault(bucket(r['why']), []).append(r)
    for _grp in ['Звертання — «ти» замість «ви»', 'Словник — одне поняття, одне слово',
                 'Кнопки — одна дія, одна назва', 'Заборонене']:
        rs = groups.get(_grp)
        if not rs: continue
        A(f'### {_grp}')
        A('')
        A('| Було | Стало | Де | Чому |')
        A('|---|---|---|---|')
        seen = set()
        for r in sorted(rs, key=lambda x: x['old']):
            if r['old'] in seen: continue
            seen.add(r['old'])
            where = sorted({x['file'] for x in rs if x['old'] == r['old']})
            w = ', '.join(f'`{x[:-5]}`' for x in where)
            o = esc(r['old'].strip('><'))
            n = esc(r['new'].strip('><'))
            A(f'| {o} | **{n}** | {w} | {esc(r["why"])} |')
        A('')

# ── розділ 1: глобальний хром ────────────────────────────────
A('## 1. Глобальний хром — винесено з таблиці')
A('')
A(f'Ці рядки стоять **однаково на всіх 63 екранах**, тому в таблиці нижче їх немає: інакше вони дали '
  f'б {nchrome} однакових рядків шуму. Те, що вони ідентичні, — це добре, і саме тому вони тут '
  f'окремо, а не серед іншого.')
A('')
A('| Область | Рядок | Тип | Екранів |')
A('|---|---|---|---|')
for t in ['Map', 'Plans', 'Guide', 'Safety', 'Profile']:
    n = sum(1 for r in rows if r['zone'] == 'таббар' and r['text'] == t)
    A(f'| таббар | {t} | кнопка | {n} |')
n4 = sum(1 for r in rows if r['zone'] == 'таббар' and r['text'] == '4')
A(f'| таббар | 4 *(бейдж «лишилось закріпити»)* | лічильник | {n4} |')
A(f'| футер | {esc(ATTR)} | атрибуція | 63 |')
A('| футер | Where this comes from | розкривач | 63 |')
A(f'| футер | {CHROME_TS} | атрибуція | 51 |')
A('')
A('**Одне спостереження вже тут.** Рядок джерел у футері (`Where this comes from` → деталізація) '
  '**різний на кожному екрані** — тому він лишився в таблиці. Це правильно: він говорить про те, що '
  'на цьому екрані стверджується. А от «Last checked: 13 August 2026, 09:12» стоїть на 51 '
  'екрані з 63 — і на екранах, де дані свіжі, і на тих, де вони з кешу.')
A('')

# ── розділ 2: таблиця ────────────────────────────────────────
A('---')
A('')
A('## 2. Таблиця — увесь текст інтерфейсу')
A('')
A(f'{len(tbl)} рядків. Згруповано за вкладками, усередині вкладки — базовий екран і його стани '
  'одразу за ним, щоб було видно, де стан говорить про те саме інакше.')
A('')
STATE_NOTE = {'':'успіх'}
for tab, base, fam in order:
    A(f'### {tab} · {g.TITLE.get(base, base)}')
    A('')
    for f in fam:
        rs = [r for r in byfile[f] if not is_chrome(r)]
        if not rs: continue
        st = rs[0]['state'] or 'успіх'
        A(f'#### `{f}` — {st}')
        A('')
        A('| Зона | Рядок | Тип | Позначки |')
        A('|---|---|---|---|')
        for r in rs:
            fl = ' '.join(f'`{x}`' for x in r['flags'])
            A(f"| {esc(r['zone'])} | {esc(r['text'])} | {r['type']} | {fl} |")
        A('')

# ── розділ 3: той самий предмет під різними іменами ──────────
A('---')
A('')
A('## 3. Той самий предмет під різними іменами')
A('')
def wordcount(pat):
    rx = re.compile(pat, re.I)
    n = sum(len(rx.findall(r['text'])) for r in rows)
    fs = sorted({r['file'] for r in rows if rx.search(r['text'])})
    return n, fs

GRP = [
 ('Багатоденний обʼєкт', 'С1', [
   (r'\bplan\w*', 'plan'), (r'\btrip\w*', 'trip'), (r'\btrek\w*', 'trek'),
   (r'\bjourney\w*', 'journey'), (r'\bitinerar\w*', 'itinerary')]),
 ('Лінія на місцевості', 'С2', [
   (r'\broute\w*', 'route'), (r'\btrail\w*', 'trail'), (r'\bpath\w*', 'path'), (r'\btrack\w*', 'track')]),
 ('Речі', 'С3', [
   (r'\bgear\b', 'gear'), (r'\bpack\b|\bpacked\b', 'pack'), (r'checklist\w*', 'checklist'),
   (r'inventor\w*', 'inventory')]),
 ('Ночівля', '—', [
   (r'\bhuts?\b', 'hut'), (r'\bnights?\b', 'night'), (r'\bstay\w*', 'stay'), (r'\bbeds?\b', 'bed'),
   (r'lodging|accommodation', 'lodging')]),
 ('Денний відрізок', 'С5', [
   (r'\bdays?\b', 'day'), (r'\blegs?\b', 'leg'), (r'\bsections?\b', 'section'), (r'\bstages?\b', 'stage'),
   (r'\bsegments?\b', 'segment')]),
 ('Бронювання', '—', [
   (r'\bbook\w*', 'book / booking'), (r'\breserv\w*', 'reserve'), (r'lock in|lock-in', 'lock in'),
   (r'\bsecur\w*', 'secure')]),
]
WC = {}
for title, code, pats in GRP:
    A(f'### {title}' + (f'  ·  `{code}`' if code != '—' else ''))
    A('')
    A('| Слово | Згадок | Екранів | Де саме, якщо рідкісне |')
    A('|---|---|---|---|')
    for pat, name in pats:
        n, fs = wordcount(pat)
        WC[name] = (n, len(fs))
        if not n: continue
        where = ', '.join(f'`{x}`' for x in fs) if len(fs) <= 4 else ''
        A(f'| **{name}** | {n} | {len(fs)} | {where} |')
    A('')

def c(name): return WC.get(name, (0, 0))[0]
A('**Що з цього справді розбіжність, а що ні.**')
A('')
A(f'- **`plan` / `trip` — {c("plan")} проти {c("trip")}.** Після перекладу це свідомий поділ, а не '
  'розкол: «trip» — похід як подія в житті людини («My trips», «About the trip», «Plan again from this '
  'trip»), «plan» — документ, який ми склали й міняємо («New plan», «Save plan», «Change plan»). '
  'Межа: «trip» ніколи не стоїть на дії, що змінює документ.')
A(f'- **`route` / `trail` — {c("route")} проти {c("trail")}, і це не розбіжність.** Два обʼєкти: '
  'route — те, що ми пропонуємо; trail — те, по чому йдуть, і джерело даних (Turrutebasen). '
  f'`path` ({c("path")}) живе лише в описах фото й місць на стежці.')
A(f'- **`hut` / `night` / `stay` / `bed` — чотири обʼєкти, а не синоніми**: обʼєкт, календарна ніч, '
  'факт ночівлі й одиниця гарантії. Англійська тримає межу краще за українську: «Stay here on night 4» '
  'вживає два з них в одному рядку, кожне у своєму значенні.')
A(f'- **`gear` ({c("gear")}) проти `inventory` ({c("inventory")}) і `checklist` ({c("checklist")})** — '
  '«Open inventory» єдиний рідкісний напис для того, що всюди зветься gear.')
A(f'- **`book` ({c("book / booking")}) — єдине дієслово бронювання.** `reserve`, `lock in`, `secure` '
  f'трапляються {c("reserve") + c("lock in") + c("secure")} разів: розрізнення «забронювати / закріпити» '
  'з української версії в англійській не відтворилось, і воно не потрібне — бронює завжди офіційна '
  'система, а ми показуємо, що лишилось забронювати.')
A('')
# заголовок шапки = h1
dup = []
for f, rs in byfile.items():
    hs = [r['text'] for r in rs if r['type'] == 'заголовок екрана']
    if len(hs) == 2 and hs[0] == hs[1]: dup.append((f, hs[0]))
A(f'### Шапка й заголовок кажуть те саме двічі — {len(dup)} з {len(byfile)}')
A('')
A('У смузі згори й у `h1` під нею стоїть один і той самий рядок, і людина бачить його двічі підряд. '
  f'На решті {len(byfile)-len(dup)} екранів `h1` натомість несе **імʼя самого обʼєкта** — `plan.html` '
  'каже «Kungsleden · Abisko → Nikkaluokta» під шапкою «Plan», `day.html` — «Day 3 · Wed 19 August» '
  'під шапкою «Day». Тобто в наборі співіснують два різні рішення про те, що робить `h1`: на хабах '
  'вкладок повтор свідомий (великий заголовок iOS), на екранах обʼєкта — ні.')
A('')
A('| Екран | Рядок |')
A('|---|---|')
for f, t in dup: A(f'| `{f}` | {esc(t)} |')
A('')

# ── розділ 4: та сама дія — різні кнопки ─────────────────────
A('---')
A('')
A('## 4. Та сама дія під різними назвами кнопок')
A('')
btn_files = collections.defaultdict(set)
for r in rows:
    if r['type'] in ('кнопка', 'посилання'): btn_files[r['text']].add(r['file'])
NAMES = {
 'Д1': ('Сказати, куди йду', SHARE),
 'Д2': ('Забронювати', BOOK),
 'Д3': ('Скласти план', MAKE),
 'Д4': ('Замінити ночівлю', SWAP),
 'Д5': ('Відкрити план', PLANOPEN),
 'Д6': ('Відкрити спорядження', GEAR),
 'Д7': ('Відкрити сьогоднішній день', TODAY),
 'Д8': ('Нотатки з місця', NOTES),
 'Д9': ('Відгуки', REV),
 'Д10': ('Точки сходу', BAIL),
 'Д11': ('Спробувати ще раз', RETRY),
 'Д12': ('Вийти з акаунта', SIGNOUT),
}
CODES = list(NAMES)
for code in CODES:
    title, s = NAMES[code]
    present = sorted([t for t in s if t in btn_files], key=lambda x: x.lower())
    if len(present) < 2: continue
    A(f'### `{code}` · {title} — {len(present)} назв')
    A('')
    A('| Напис на кнопці | Де стоїть |')
    A('|---|---|')
    for t in present:
        fs = sorted(btn_files[t])
        where = ', '.join(f'`{x}`' for x in fs[:5]) + (f' + ще {len(fs)-5}' if len(fs) > 5 else '')
        A(f'| {esc(t)} | {where} |')
    A('')

multi = [code for code in CODES if sum(1 for t in NAMES[code][1] if t in btn_files) >= 2]
A(f'**Кластерів, де одна дія має два й більше написи: {len(multi)} з {len(CODES)}.** '
  + ('Жоден не є розбіжністю:' if multi else 'Після перекладу кожна дія названа одним написом.'))
A('')
WHY4 = {
 'Д3': '«Make a plan» — з нуля, «Plan again from this trip» — з минулого походу: дві точки входу однієї дії, і це свідомо',
 'Д8': 'прочитати нотатки й написати свою — сусідні дії над одним обʼєктом, а не синоніми',
 'Д2': '«Book» на дні веде в аркуш, «Open STF booking ↗» в аркуші віддає в STF — два кроки однієї дії',
}
for code in multi:
    A(f'- `{code}` — ' + WHY4.get(code, 'не переглянуто — перевірити, чи це справді одна дія'))
A('')

# ── 4б: зіткнення двох назв на ОДНОМУ екрані ─────────────────
A('### Найгостріше: дві назви однієї дії на одному екрані')
A('')
A('Розбіжність між екранами людина може й не помітити. Ці — помітить, бо обидві кнопки видно '
  'водночас.')
A('')
VERDICT = {
 ('safety.html','Д1'): ('різні дії', 'поруч немає двох написів — кластер про запас'),
 ('booking.html','Д2'): ('кроки однієї дії', 'аркуш броні й передача в STF'),
}
A('Колонка «Вердикт» — **прочитання, а не факт із розмітки**: кластери зібрані вручну, і частина '
  'пар потрапила в один кластер помилково. Позначено обидва випадки, щоб таблиця не видавала '
  'групування за знахідку.')
A('')
A('| Екран | Кластер | Кнопки, що стоять поруч | Вердикт |')
A('|---|---|---|---|')
coll = 0; real = 0
for code in CODES:
    title, sset = NAMES[code]
    for f, rs in byfile.items():
        here = sorted({r['text'] for r in rs
                       if r['type'] in ('кнопка','посилання') and r['text'] in sset})
        if len(here) >= 2:
            v, why = VERDICT.get((f, code), ('?', 'не переглянуто'))
            A(f"| `{f}` | `{code}` {title} | " + ' · '.join(esc(h) for h in here)
              + f' | {v} — {why} |')
            coll += 1
            if v.startswith('**та сама'): real += 1
A('')
if coll:
    A(f'**{coll} пар потрапило у фільтр, із них {real} — справді одна дія двома написами.** Решта — '
      'надто широке групування: воно показує, де межа між двома діями тримається тільки на довшому написі.')
else:
    A('**Жодної такої пари в наборі немає.**')
A('')
A('Два написи однієї дії поруч на одному екрані — найгостріший вид розбіжності, бо людина бачить '
  'обидва водночас. Українська версія мала їх кілька («Гарантія на цю ніч» поруч із «Гарантія й '
  'доступ на цю ніч»); англійська писалась одразу з одним написом на дію.')
A('')
# ── розділ 5: тон, кліше, емодзі ─────────────────────────────
A('---')
A('')
A('## 5. Тон, кліше, піктограми')
A('')
excl = [r for r in rows if '!' in r['text']]
A(f'**Окличних знаків у наборі: {len(excl)}.** Бадьорого тону, «Ой, щось пішло не так», «Вітаємо» і '
  'подібного немає — перевірено пошуком по словах. Це рідкість, і її варто зберегти.')
A('')
errs = sorted({r['text'] for r in rows if r['file'].endswith('-error.html') and r['type'] in ('кнопка','посилання') and r['text'] in RETRY})
A('**Помилки говорять однаково**: на екранах помилки (`new-plan-error`, `plan-error`) дія одна — '
  + ', '.join(f'`{e}`' for e in errs) + '.')
A('')
em = [r for r in rows if RX_EMOJI.search(r['text'])]
byem = collections.defaultdict(list)
for r in em: byem[r['text']].append(r['file'])
A(f'### Піктограми — {len(em)} рядків  ·  `Т1`')
A('')
A('| Рядок | Тип | Де | Що це |')
A('|---|---|---|---|')
for t, fs in sorted(byem.items(), key=lambda x: -len(x[1])):
    typ = next(r['type'] for r in em if r['text'] == t)
    where = f'{len(fs)} екранів' if len(fs) > 3 else ', '.join(f'`{x}`' for x in sorted(set(fs)))
    note = ('функційний хрестик закриття — не порушення' if t.startswith('✕') else
            '⚠️ у продуктовому тексті — стиль документів, не інтерфейсу' if '⚠' in t else
            '✓/✗ як індикатор — контракт вимагає слова, не значка')
    A(f'| {esc(t[:70])} | {typ} | {where} | {note} |')
A('')
A('**Хрестик закриття питань не викликає — це системний жест.** `offline ✓` на плані — інша річ: '
  '`_next.md` каже «індикатор — слово, не значок», і тут слово є («offline»), а галочка лише '
  'підсилює його. Лишається під наглядом: у стані `plan-offline` замість неї стоїть дата пакета, тобто '
  'значок і слово вже роз’їхались по станах.')
A('')
# ── розділ 6: заглушки ───────────────────────────────────────
A('---')
A('')
A('## 6. Заглушки')
A('')
z1 = [r for r in rows if r['type'] == 'заглушка макета']
z2 = [r for r in rows if 'З2' in r['flags']]
A(f'### `З1` · Заглушки макета — {len(z1)} рядків')
A('')
A('Опис того, що буде в рамці замість самої рамки: карта, профіль висоти, фото. Це **нормально для '
  'вайрфрейма** і зникне з появою реального вмісту — але це текст, який зараз видно на екрані, тому '
  'він у таблиці й позначений.')
A('')
A('| Екран | Рядок |')
A('|---|---|')
for r in z1[:24]: A(f"| `{r['file']}` | {esc(r['text'][:120])} |")
A(f'| … | *ще {len(z1)-24} — усі позначені `З1` у таблиці розділу 2* |')
A('')
A(f'### `З2` · Текст замість змісту — {len(z2)} рядків')
A('')
A(f'Це вже інше: тут стоїть **опис того, що напишуть**, у місці, де людина чекає сам зміст. '
  f'Таких рядків {len(z2)} на {len({r["file"] for r in z2})} екранах.')
A('')
A('| Екран | Зона | Рядок |')
A('|---|---|---|')
for r in z2: A(f"| `{r['file']}` | {esc(r['zone'])} | {esc(r['text'][:110])} |")
A('')
A('**`first-aid.html` тримає назви карток, а не їхній текст** («Hypothermia · Røde Kors»). Це '
  'свідомо: медичний зміст ми не авторуємо, його ліцензію ще не з\'ясовано (`CLAUDE.md`, відкриті '
  'питання), тож картка називає джерело замість того, щоб вигадувати зміст.')

# ── розділ 7: редакційний текст ──────────────────────────────
A('---')
A('')
A('## 7. Рядки, які пише автор статей  ·  `Р`')
A('')
A('Це **не продуктовий мікрокопі**, і зводити його до тієї самої таблиці правди не можна: у нього '
  'інший автор, інша довжина речення і, головне, **інший правовий статус** — частина його нам не '
  'належить і цитується з атрибуцією.')
A('')
A('| Екран | Рядків | Слів | Чий це текст |')
A('|---|---|---|---|')
ED_WHO = {
 'guide.html': 'наш вступний шар над чужим змістом; статті — DNT (норвезькою), переклад наш',
 'lodging-system.html': 'шаблон статті довідника; зміст — DNT, STF, Naturvårdsverket, Miljødirektoratet, з джерелом у кожній',
 'first-aid.html': '**не наш** — Røde Kors / Röda Korset, цитата з атрибуцією; медичний зміст ми не авторуємо',
}
for f in sorted(EDITORIAL):
    rs = [r for r in byfile[f] if not is_chrome(r)]
    A(f"| `{f}` | {len(rs)} | {sum(len(r['text'].split()) for r in rs)} | {ED_WHO[f]} |")
A('')
A('**Редакційний текст за межами цих екранів** після перебудови 2026-09-23 зведено до коротких '
  'фактів на самих полях: ночівля на дні й хижі каже «прийти до 18:00 · логбук», а не переказує правила.')
A('')

# ── розділ 8: жаргон ─────────────────────────────────────────
jg = [r for r in rows if RX_JARGON.search(r['text'])]
byj = collections.defaultdict(list)
for r in jg: byj[r['text']].append(r['file'])
A('---')
A('')
A(f'## 8. Технічний жаргон і службові назви  ·  `Ж` — {len(jg)} рядків')
A('')
A('| Рядок | Тип | Де | Що саме витекло |')
A('|---|---|---|---|')
JN = [(r'lock-in', '«lock-in» — внутрішня назва кроку'),
      (r'\btiles?\b', '«tiles» — внутрішня назва фрагментів карти'),
      (r'\bAPI\b', '«API» — мова пітчу, не інтерфейсу'),
      (r'\bstep \d+\b', '«step N» без «з скількох» — нумерація без знаменника'),
      (r'\bpush\b', '«push» — внутрішня назва сповіщення'),
      (r'\.html\b', 'імʼя файлу екрана')]
for t, fs in sorted(byj.items(), key=lambda x: -len(x[1])):
    typ = next(r['type'] for r in jg if r['text'] == t)
    note = next((n for p, n in JN if re.search(p, t, re.I)), '—')
    where = f'{len(fs)} екранів' if len(fs) > 3 else ', '.join(f'`{x}`' for x in sorted(set(fs)))
    A(f'| {esc(t[:95])} | {typ} | {where} | {note} |')
A('')

# ── розділ 9: що далі ────────────────────────────────────────
A('---')
A('')
A('## 9. Що це дає, поки рішень ще нема')
A('')
A(f'Позначено {len(flagged)} рядків із {len(tbl)}. Жодного не змінено.')
A('')
A('Що видно тільки з такої таблиці:')
A('')
A('1. **Переклад прибрав більшість розбіжностей, бо писався як один текст.** Українська версія '
  'накопичувала синоніми з кожною перебудовою; англійська — один прохід по всіх 33 сторінках, тому '
  'кластери `Д*` зараз здебільшого порожні. Словники вище тримають відомі синоніми, щоб дрейф '
  'було видно з першого ж рядка.')
A('2. **Стани розходяться з базою частіше, ніж базові екрани між собою.** `_audit.py` стежить, щоб '
  'у стану був той самий перелік зон, що й у бази, — але за словами всередині зон стежить лише ця таблиця.')
A('3. **`plan` / `trip` — єдина межа, яку варто записати в глосарій.** Вона свідома (документ проти '
  'події), але тримається тільки на звичці; наступний, хто писатиме текст, має знати її явно.')
A('')
pathlib.Path('wireframes/microcopy.md').write_text('\n'.join(out) + '\n', encoding='utf-8')
print('microcopy.md:', len(out), 'рядків ·', len(tbl), 'рядків таблиці ·', len(flagged), 'позначено')
