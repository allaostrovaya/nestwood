# -*- coding: utf-8 -*-
"""Сторінка головного флоу: макети happy path одним рядком, у порядку проходження.

Джерело макетів — самі сторінки набору: блок .device витягується з файлу, а не
переписується руками. Тому flow.html не протухає, коли екран змінюють.
Джерело коментарів — flows.md (MAIN JOB, 2, 7) і CLAUDE.md.

Запуск із кореня репозиторію:
    python3 wireframes/_flow.py
"""
import pathlib, re, importlib.util

W = pathlib.Path('wireframes')

_s = importlib.util.spec_from_file_location('gnav', 'design-system/docs/gnav.py')
_g = importlib.util.module_from_spec(_s); _s.loader.exec_module(_g)
GNAV = _g.gnav('flow', '../')

# назва екрана й вкладка беруться з TREE, позиція — з рядка .meta самої сторінки.
# Зашивати їх тут означало б завести четверте місце, де живе та сама назва.
_t = importlib.util.spec_from_file_location('gen', 'wireframes/_generate.py')
_gen = importlib.util.module_from_spec(_t); _t.loader.exec_module(_gen)

def _pos(fname):
    m = re.search(r'<p class="meta"[^>]*><b>([^<]+)</b>', (W / fname).read_text(encoding='utf-8'))
    return m.group(1) if m else '?'

def _name(fname, override=None, star=False):
    n = override or _gen.TITLE.get(fname, fname)
    return n + (' \u2b50' if star else '')

# ── КРОКИ ────────────────────────────────────────────────────
# file, позиція (джоб.крок), назва в рейці, jobs, lead, body, рішення, гілки.
# Гілка: (мітка, файл або None, пояснення). None → інертний текст, не бите посилання.
STEPS = [
 dict(
  file='catalogue.html', rail=None,
  jobs='1 · 2 · MAIN',
  lead='Вхід у продукт і без візарда: один компонент пошуку «Куди · Коли · Хто», як в Airbnb чи Booking, над картою на весь екран.',
  body='<p><b>Куди</b> — регіон, пресет або свій маршрут «звідки → куди». Точки старту й фінішу задані заздалегідь '
       '(станції, входи на мережу, хижі), тож маршрут ніколи не сходить з маркованої мережі. Поки план не складено, '
       'на карті видно лінію, кілометри й дні. <b>Коли</b> — точні дати. <b>Хто</b> — кількість людей і скільки з них члени.</p>'
       '<p>Пресети з фото, привʼязані до точок на карті: «Найкраще в країні в місяць» і «Класика Скандинавії».</p>',
  q='Під ці дати щось є?',
  branches=[
   ('так', None, 'пресет або свій маршрут → генерація'),
   ('ні', 'catalogue-empty.html', 'у лютому хижі зачинені — інші дати'),
  ]),
 dict(
  file='new-plan-loading.html', rail='Генерація',
  jobs='MAIN',
  lead='Прохідний екран: скелетон нового плану й прогрес — план проявляється на тому самому місці.',
  body='<p>Структурований вивід <code>claude-opus-5</code> у схему плану; пошук по графу хиж.</p>',
  q='Маршрут складається?',
  branches=[
   ('так', None, 'новий план'),
   ('ні', 'new-plan-conflict.html', 'зберегти не можна, виходи названо: +2 дні · інший фініш · намет'),
   ('критичне джерело', 'new-plan-error.html', 'плану немає, спробувати ще раз'),
  ]),
 dict(
  file='new-plan.html', rail=None, star=True,
  jobs='1 · 2 · 4 · 6 · 9 · 11 · MAIN',
  lead='Новий план, ще не збережений. Заглавне фото — з точки старту; під ним один рядок «дати · хто».',
  body='<p>Коли все сходиться — одна плашка, а не текст. Статуси тільки там, де щось не так.</p>',
  q='Що людина робить?',
  branches=[
   ('змінити ночівлю', 'huts.html', 'хижі поруч, компактні картки'),
   ('нотатки й відгуки', 'notes.html', 'нотатка може змінити план, відгук — ніколи'),
   ('зберегти', 'plan.html', 'план переїжджає в «Плани» — акаунт уже є'),
   ('скасувати', 'catalogue.html', 'план зникає'),
  ]),
 dict(
  file='huts.html', rail='Інша хижа',
  jobs='2',
  lead='Заміна ночівлі до збереження — компактні картки хиж.',
  body='<p>Повна картка — на аркуші хижі.</p>',
  q='Є хижа під фільтри?',
  branches=[
   ('так', 'hut.html', 'аркуш хижі → «ночувати тут»'),
   ('ні', 'huts-empty.html', 'зняти фільтр або намет'),
  ]),
 dict(
  file='plan.html', rail=None, star=True,
  jobs='1 · 3 · 4 · 7 · 9 · MAIN',
  lead='Збережений план: зверху загальні алерти, під ними дні, кожен зі своїми алертами.',
  body='<p>Бронь Sälka — на дні 4, квиток на автобус — на дорозі назад: кожна задача на своїй сутності. '
       'Алерт веде туди, де його виправляють. Офлайн-пакет качається сам по Wi-Fi.</p>',
  q='У якому стані план?',
  branches=[
   ('без мережі', 'plan-offline.html', 'плашка зверху'),
   ('не оновився', 'plan-error.html', 'плашка зверху'),
   ('пройдений', 'plan-past.html', 'з нього рахується темп'),
   ('змінити план', 'new-plan.html', 'з попередженням: позначки броней і квитків скинуться'),
   ('забронювати', 'booking.html', 'поза основним флоу: порядок, дедлайн, передача в STF, номер броні'),
  ]),
 dict(
  file='day.html', rail=None,
  jobs='1 · 2 · 3 · 6',
  lead='День — окрема сторінка: перехід, ночівля, умови, погода. Між днями — стрілки й свайп.',
  body='<p>Розділ без змісту не показується.</p>',
  q='Далеко до дня?',
  branches=[
   ('понад 10 днів', 'day-seasonal.html', 'сезонна норма, не прогноз'),
   ('без мережі', 'day-offline.html', 'з офлайн-пакета'),
  ]),
 dict(
  file='day-intrip.html', rail='Сьогодні',
  jobs='3 · 6',
  lead='У поході вкладка «Плани» відкриває сьогоднішній день. Один екран без скролу, SOS постійно.',
  body='<p>Скільки лишилось, до котрої прийти, брід, погода — і кнопка «Написати нотатку з місця».</p>',
  q='Щось на ділянці не так, як на карті?',
  branches=[
   ('так', 'notes.html', 'написати нотатку з місця'),
  ]),
]

# перехід між кроками: що людина робить
LINKS = [
 'пресет або свій маршрут',
 'серверний виклик <code>claude-opus-5</code>',
 'тап по дню · змінити ночівлю',
 'хижа обрана',
 '«Зберегти план» — план у «Планах»',
 'тап по дню',
 'настав день виходу',
]

# ── витяг макета з готової сторінки ──────────────────────────
DEV = re.compile(r'(<div class="device".*?)\n\n</div><!-- /\.wf-main -->', re.S)

def device(fname, n):
    """Блок .device із файлу набору. Ідентифікатори префіксуються номером кроку,
    бо на одній сторінці стоїть десять макетів і id мусять лишитись унікальними."""
    s = (W / fname).read_text(encoding='utf-8')
    m = DEV.search(s)
    if not m: raise SystemExit(f'{fname}: не знайдено блок .device')
    d = m.group(1)
    p = f's{n}-'
    d = re.sub(r'\bid="([^"]+)"', lambda x: f'id="{p}{x.group(1)}"', d)
    d = re.sub(r'\baria-labelledby="([^"]+)"', lambda x: f'aria-labelledby="{p}{x.group(1)}"', d)
    d = re.sub(r'\bfor="([^"]+)"', lambda x: f'for="{p}{x.group(1)}"', d)
    d = re.sub(r'href="#([^"]+)"', lambda x: f'href="#{p}{x.group(1)}"', d)
    return d

def branch_li(label, target, text):
    lead = f'<a href="./{target}">{label}</a>' if target else f'<b>{label}</b>'
    src = f' <code>{target}</code>' if target else ''
    return f'      <li><span class="b-k">{lead}</span>{src} — {text}</li>'

def step_html(i, st):
    n = i + 1
    nn = f'{n:02d}'
    name = _name(st['file'], st.get('rail'), st.get('star'))
    pos = _pos(st['file'])
    tab = _gen.TAB.get(st['file'], '')
    name_plain = name.replace(' \u2b50', '')
    q = (f'      <h3>Рішення</h3>\n      <p class="q">{st["q"]}</p>\n' if st['q']
         else '      <h3>Виходи</h3>\n')
    br = '\n'.join(branch_li(*b) for b in st['branches'])
    return f'''<section class="step" id="s{n}" aria-labelledby="s{n}-h">
  <div class="step-head">
    <span class="step-n">{nn}</span>
    <h2 id="s{n}-h">{name}</h2>
    <p class="step-src" data-review lang="uk">{pos} · <code>{st['file']}</code> · вкладка {tab} · jobs {st['jobs']}</p>
  </div>
  <div class="step-body">
    <div class="flow-screen">
      <p class="meta" data-review lang="uk"><b>{pos}</b> · {name_plain} · <i>як у наборі</i></p>
      <input class="flow-exp" type="checkbox" id="exp{n}" />
      <label class="flow-exp-l" for="exp{n}"></label>
      <div class="flow-dev">
{device(st['file'], n)}
      </div>
      <p class="flow-open"><a href="./{st['file']}">відкрити сторінку макета →</a></p>
    </div>
    <div class="step-note">
      <p class="lead">{st['lead']}</p>
      {st['body']}
{q}      <ul class="branches">
{br}
      </ul>
    </div>
  </div>
</section>'''

def link_html(i):
    return (f'<p class="hop" aria-hidden="false"><span class="hop-arrow">↓</span>'
            f'<span class="hop-t">{LINKS[i]}</span></p>')

rail = '\n'.join(
  f'      <li><a href="#s{i+1}"><span class="rn">{i+1:02d}</span>'
  f'{_name(st["file"], st.get("rail"), st.get("star"))}</a></li>'
  for i, st in enumerate(STEPS))

NBR = sum(len(s_['branches']) for s_ in STEPS)

body = []
for i, st in enumerate(STEPS):
    body.append(step_html(i, st))
    if i < len(LINKS): body.append(link_html(i))

HTML = f'''<!doctype html>
<html lang="uk">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>Nestwood — головний флоу</title>
<link rel="stylesheet" href="./_wireframe.css?v=20260924h" />
<link rel="stylesheet" href="./_flow.css" />
<link rel="stylesheet" href="./_prylad.css?v=20260925m" />
<link rel="stylesheet" href="../design-system/docs/globalnav.css" />
</head>
<body>
<div class="nw-theme" data-review lang="uk" role="radiogroup" aria-label="Тема макета"><input type="radio" name="nw-theme" id="nw-light" checked><label for="nw-light">Світла</label><input type="radio" name="nw-theme" id="nw-dark"><label for="nw-dark">Темна</label></div><script src="./_theme.js"></script>

{GNAV}

<div class="flow-shell">

<nav class="flow-rail" data-review lang="uk" aria-label="Кроки головного флоу">
  <h2>NESTWOOD · ГОЛОВНИЙ ФЛОУ</h2>
  <ol>
{rail}
  </ol>
  <p class="rail-foot">Три тапи до плану, цінність на нульовому.<br>
  Джерела: <a href="./flows.md">flows.md</a> · <a href="./sitemap.md">sitemap.md</a><br>
  Поруч: <a href="./ia.html">архітектура</a> · <a href="./plan.html">увесь набір</a></p>
</nav>

<main class="flow-main">

<header class="flow-mast">
  <p class="eyebrow">Головний флоу · MAIN JOB</p>
  <h1>Десять екранів підряд — рівно той шлях, на якому людина перестає бути інтеграційним шаром</h1>
  <blockquote class="claim">«Коли я планую багатоденний похід у горах, я хочу бути впевненою, що маршрут,
  ночівля, спорядження й погода <b>узгоджені між собою</b>, щоб не бути самою тим, хто зводить
  чотири розрізнені джерела в одне ціле.»</blockquote>
  <p class="dek">Тут стоять справжні макети з набору — не перемальовані, а витягнуті з тих самих
  файлів, тому сторінка не розходиться з ними. Кожен крок підписаний позицією <code>джоб.крок</code>,
  рішенням із <a href="./flows.md">flows.md</a> і гілками, які з цього рішення виходять. Гілка
  веде на намальований стан; там, де стану ще немає, вона лишається текстом, а не битим посиланням.</p>
  <p class="dek"><b>Чому саме ці кроки.</b> Це happy path головного джоба: від пошуку до
  сьогоднішнього дня в поході. Дві поверхні нас відрізняють — <b>новий план</b> (крок 03), де видно
  ночівлі, квитки й навантаження до збереження, і <b>план</b> (крок 06), де зверху загальні
  алерти, а під ними дні зі своїми. Порядок: пошук → генерація → новий план → збереження → план → день.</p>
  <ul class="mast-facts">
    <li><b>{len(STEPS)}</b> екранів у хребті</li>
    <li><b>3</b> тапи до плану</li>
    <li><b>{NBR}</b> гілок і станів названо</li>
    <li><b>0</b> битих виходів</li>
  </ul>
</header>

{chr(10).join(body)}

<footer class="flow-foot">
  <p>Кінець happy path. Далі — <a href="./offline-pack.html">офлайн-пакет</a> і похід:
  <a href="./today.html">сьогоднішня нога</a> та <a href="./changes.html">що змінилось і що ще
  можна зробити</a>. In-trip шар навмисно поза цим флоу: він тримає jobs 3 і 6 і має власний
  потік у <a href="./flows.md">flows.md</a>.</p>
  <p class="attr">Карти й стежки © Kartverket (CC BY 4.0) · Lantmäteriet (CC0) · Погода met.no ·
  Транспорт Entur / Trafikverket. Наявність ліжок у макетах умовна: живе джерело потребує угоди
  з DNT/STF, і це називається в пітчі, а не в інтерфейсі.</p>
  <p class="gen" data-review lang="uk">Сторінка згенерована <code>wireframes/_flow.py</code> з
  файлів набору. Правити тут руками не треба: зміни йдуть у макет, потім
  <code>python3 wireframes/_flow.py</code>.</p>
</footer>

</main>
</div><!-- /.flow-shell -->

</body>
</html>
'''

(W / 'flow.html').write_text(HTML, encoding='utf-8')
print(f'flow.html: {len(STEPS)} кроків, {sum(len(s["branches"]) for s in STEPS)} гілок')
