# -*- coding: utf-8 -*-
"""Генератор сторінок вайрфреймів Nestwood.
Джерело структури — sitemap.md, джерело станів — _screens.md.
Дерево навігації рендериться з одних даних, тому однакове всюди."""
import pathlib, re
W = pathlib.Path('wireframes')

# ── СТРУКТУРА: розділ → екран → стани ─────────────────────────
TREE = [
 ('G · Куди піти', [
   ('G1 Регіони','regions.html',[('порожній','regions-empty.html')]),
   ('G2 Картка маршруту','route.html',[('порожній','route-empty.html'),('помилка','route-error.html'),('завантаження','route-loading.html')]),
   ('G3 Карта','map.html',[('помилка','map-error.html'),('завантаження','map-loading.html'),('офлайн','map-offline.html')]),
 ]),
 ('0 · Вхід', [('Стартовий екран','start.html',[])]),
 ('A · Візард', [
   ('W1 Маршрут','wizard-route.html',[('порожній','wizard-route-empty.html'),('помилка','wizard-route-error.html'),('завантаження','wizard-route-loading.html')]),
   ('W2 Коли і скільки нас','wizard-when.html',[('порожній','wizard-when-empty.html'),('помилка','wizard-when-error.html')]),
   ('W3 Про мене','wizard-about.html',[('порожній','wizard-about-empty.html'),('помилка','wizard-about-error.html')]),
 ]),
 ('B · План', [
   ('B1 План по днях','plan.html',[('порожній','plan-empty.html'),('помилка','plan-error.html'),('завантаження','plan-loading.html'),('конфлікт','plan-conflict.html'),('офлайн','plan-offline.html'),('degraded','plan-degraded.html')]),
   ('B2 День','day.html',[('норма замість прогнозу','day-seasonal.html')]),
   ('B3 Ніч: гарантія й доступ','night.html',[('порожній','night-empty.html'),('помилка','night-error.html'),('degraded','night-degraded.html')]),
   ('B4 Як працює ця система','lodging-system.html',[]),
   ('B5 Спорядження','gear.html',[]),
   ('B6 Транспорт','transport.html',[('порожній','transport-empty.html'),('помилка','transport-error.html'),('завантаження','transport-loading.html')]),
   ('B7 Нотатки з місця','field-notes.html',[('порожній','field-notes-empty.html')]),
   ('B8 Ночівлі — ланцюжок','nights.html',[]),
 ]),
 ('C · Закріпити', [('C1 Що лишилось закріпити','lock-in.html',[('порожній','lock-in-empty.html'),('помилка','lock-in-error.html'),('офлайн','lock-in-offline.html')]),
                    ('C2 Членство й ключ','membership.html',[])]),
 ('D · У дорозі', [('D1 Сьогодні','today.html',[('офлайн','today-offline.html')]),
                   ('D2 Що змінилось','changes.html',[('завантаження','changes-loading.html'),('помилка','changes-error.html'),('варіантів немає','changes-nooptions.html')])]),
 ('E · Показати іншим', [('E Підсумок для передачі','share.html',[])]),
 ('F · Моє', [('F1 Мої походи','mine.html',[('порожній','mine-empty.html')]),('F2 Моє спорядження','my-gear.html',[]),('F3 Я','me.html',[])]),
]

def node(label, file, current, cls=''):
    c = f' class="{cls}"' if cls else ''
    if not file: return f'<span class="todo{" "+cls if cls else ""}">{label}</span>'
    cur = ' aria-current="page"' if file == current else ''
    return f'<a{c} href="./{file}"{cur}>{label}</a>'

def nav_html(current):
    out = ['<nav class="wf-tree" data-review lang="uk" aria-label="Структура вайрфреймів">',
           '  <h2>NESTWOOD · ВАЙРФРЕЙМИ</h2>',
           '  <p class="legend"><b>чорним</b> — намальовано, посилання<br>сірим — ще ні. Відступ = вкладеність:<br>розділ → екран → стан.</p>',
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

def states_row(base, current):
    """рядок станів конкретного екрана"""
    for grp, screens in TREE:
        for label, file, states in screens:
            if file == base:
                parts = [node('успіх', file, current)] + [node(l, f, current, '') for l, f in states]
                return '<p class="states" data-review lang="uk">Стани екрана: ' + ' · '.join(parts) + '</p>'
    return ''

APPNAV = '''  <header class="app">
    <p class="brand">Nestwood</p>
    <nav aria-label="Головна навігація">
      <ul>
        <li><a href="./plan.html"{p}>План</a></li>
        <li><span class="nav-todo">Ночівлі</span></li>
        <li><span class="nav-todo">Закріпити <span class="count">4</span></span></li>
        <li><span class="nav-todo">Моє</span></li>
      </ul>
    </nav>
  </header>
  <p class="ann" data-review lang="uk">ЗОНА · Глобальна навігація — чотири входи в кластери jobs. Незмінна в усіх станах: стан екрана ніколи не чіпає оболонку. Сірим — екрани, яких ще немає у вайрфреймах (крок 8): посилання на них не ставимо, щоб не робити 404-тупик.</p>
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

def zone(zid, head, body, ann):
    return (f'    <section aria-labelledby="{zid}">\n      <h2 id="{zid}">{head}</h2>\n{body}\n    </section>\n'
            f'    <p class="ann" data-review lang="uk">ЗОНА · {ann}</p>\n')

def page(current, title, h1, review, zones, src, appnav=True, base=None):
    nav = APPNAV.format(p=' aria-current="page"' if current.startswith('plan') else '') if appnav else ''
    return f'''<!doctype html>
<html lang="uk">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>{title}</title>
<link rel="stylesheet" href="./_wireframe.css" />
</head>
<body>

<span id="clean"></span>

<p class="toggle"><a href="#clean">сховати анотації й дерево</a> · <a href="#top">показати</a></p>

<div class="wf-shell">

{nav_html(current)}

<div class="wf-main">

{states_row(base or current, current)}

<details class="review" data-review lang="uk" id="top" open>
{review}
</details>

<div class="device">

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

P = {}   # файл → вміст

def R(state, flow, rule, extra=''):
    return f'''  <summary>{state}</summary>
  <div class="review-body">
    <p><b>Місце у flow:</b> {flow}</p>
    <p><b>Правило стану:</b> {rule}</p>
    {extra}
  </div>'''

# ══ 0 · СТАРТОВИЙ ЕКРАН ═══════════════════════════════════════
P['start.html'] = page('start.html','Wireframe · Стартовий екран','Nestwood',
 R('wireframes/start.html — <b>Стартовий екран</b> · станів немає',
   '<code>START</code> → <code>QSAVED: ні</code> → <code>Стартовий екран</code> → <code>QKNOW</code>.',
   'Єдиний екран без job\'а. Підстава зовнішня — пакування як повний застосунок. <b>Обсяг заморожений:</b> обіцянка, тон, два входи. Встановлення PWA звідси прибрано (рішення №14) — воно на B1, разом з офлайн-пакетом.',
   '<p><b>Тригер на перегляд:</b> якщо цей екран почне рости, ми будуємо маркетинг замість продукту.</p>'),
 zone('promise','Що це','''      <p>Багатоденні походи в Скандинавії, зведені в один план: маршрут, ночівлі, спорядження й погода — узгоджені між собою, а не в чотирьох різних вкладках.</p>
      <p>Дані офіційні: Kartverket, Lantmäteriet, met.no. Де їх бракує — ми це кажемо, а не вгадуємо.</p>''',
   'Обіцянка й тон. ГОЛОВНОЇ ДІЇ немає — це поріг, а не крок. Формулювання свідомо не обіцяє «знайдемо тобі маршрут»: продукт зводить, а не шукає.')
 + zone('enter','Почати','''      <p class="actions">
        <a class="cta" href="./wizard-route.html">Я знаю, куди хочу</a>
        <a href="./regions.html">Ще не знаю — покажіть, куди можна</a>
      </p>''',
   'Два входи — це розвилка <code>QKNOW</code> із flows.md, винесена на поріг. До рішення №21 другого входу не існувало, і продукт працював лише для того, хто вже знає регіон.'),
 'Стежки й рельєф: Lantmäteriet (CC0) для Швеції, Kartverket (CC BY 4.0) для Норвегії.',
 appnav=False)

# ══ G1 · РЕГІОНИ ══════════════════════════════════════════════
def regions(empty=False):
    if empty:
        body = '''      <p>У лютому в цих регіонах багатоденних маршрутів немає: хижі зачинені, стежки під снігом, а зимові переходи ми поки не плануємо.</p>
      <ul class="signals">
        <li><b>Варіант 1</b> Червень — липень: Kungsleden відкривається, хижі працюють, комарі ще не в піку</li>
        <li><b>Варіант 2</b> Кінець серпня — вересень: менше людей, кольори, але коротший день</li>
        <li><b>Варіант 3</b> Подивитись усі регіони без фільтра за місяцем</li>
      </ul>
      <p class="actions">
        <form action="./regions.html" method="get" style="display:inline"><button type="submit">Показати червень</button></form>
        <form action="./regions.html" method="get" style="display:inline"><button type="submit">Показати вересень</button></form>
        <form action="./regions.html" method="get" style="display:inline"><button type="submit">Зняти фільтр місяця</button></form>
      </p>'''
        ann = 'Список регіонів → <b>порожній стан</b>. Не «нічого не знайдено», а відповідь: у цей місяць тут не ходять, і ось коли ходять. Виходи готові — правило рішення №12 діє і тут, не лише на B1.'
    else:
        body = '''      <article>
        <h3>Лапландія · Швеція</h3>
        <p>Kungsleden і все навколо нього. Мережа fjällstugor STF, потяг Malmbanan до самих трейлхедів.</p>
        <ul class="signals">
          <li><b>Коли</b> кінець червня — середина вересня. Поза цим хижі зачинені</li>
          <li><b>Маршрути</b> 6, від 4 до 12 днів</li>
          <li><b>Особливість</b> до частини станцій немає дороги — автобусом не замінити</li>
        </ul>
        <p class="actions"><a href="./route.html">Подивитись маршрути</a></p>
      </article>
      <article>
        <h3>Jotunheimen · Норвегія</h3>
        <p>Хижі DNT, найвищі вершини Скандинавії, класичні переходи від хижі до хижі.</p>
        <ul class="signals">
          <li><b>Коли</b> липень — вересень; узимку частина хиж працює як selvbetjent</li>
          <li><b>Маршрути</b> 5, від 3 до 8 днів</li>
          <li><b>Особливість</b> замкнені хижі — потрібен DNT-ключ, а він лише для членів</li>
        </ul>
        <p class="actions"><a href="./route.html">Подивитись маршрути</a></p>
      </article>
      <article>
        <h3>Hardangervidda · Норвегія</h3>
        <p>Найбільше гірське плато Європи. Довгі відкриті переходи, мало укриттів між хижами.</p>
        <ul class="signals">
          <li><b>Коли</b> липень — вересень</li>
          <li><b>Маршрути</b> 4, від 4 до 7 днів</li>
          <li><b>Особливість</b> погода змінюється швидше, ніж встигаєш дійти до наступної хижі</li>
        </ul>
        <p class="actions"><a href="./route.html">Подивитись маршрути</a></p>
      </article>'''
        ann = 'Список регіонів. ГОЛОВНА ДІЯ: відкрити маршрути регіону. <b>Куровано, не каталог</b>: три регіони, у кожному 4–6 маршрутів, і в кожного названо «коли туди має сенс» та «особливість» — те, чого немає в каталозі конкурентів. Сортування за популярністю немає й не буде (межа рішення №21).'
    return page('regions-empty.html' if empty else 'regions.html',
      f'Wireframe · G1 Регіони · {"порожній" if empty else "успіх"}','Куди можна піти',
      R(f'wireframes/regions{"-empty" if empty else ""}.html — <b>G1 Регіони</b> · стан <b>{"порожній" if empty else "успіх"}</b>',
        '<code>Стартовий екран</code> → <code>QKNOW: ні</code> → <code>G1</code> → <code>G2</code>.',
        'Job — <b>R1</b>: «на що я справді здатна на цьому рельєфі». Екран існує з рішення №21: до нього воронка починалась із питання «регіон і місяць», тобто працювала лише для того, хто вже знає відповідь.',
        '<p><b>Межа:</b> куровано — 10–20 маршрутів на країну, без рейтингів, популярності й «топ-10».</p>'),
      zone('when','Коли ви хочете йти','''      <form action="./regions.html" method="get">
        <label for="month">Місяць</label>
        <p class="actions">
          <button type="button">Червень</button><button type="button">Липень</button>
          <button type="button">Серпень</button><button type="button">Вересень</button>
        </p>
        <p>Місяць питаємо тут, а не пізніше: без нього неможливо сказати, які маршрути взагалі мають сенс — хижі відчиняються й зачиняються за сезоном.</p>
      </form>''',
        'Фільтр за місяцем. ГОЛОВНА ДІЯ: обрати місяць. Це не зручність — це умова, без якої список маршрутів був би неправдою.')
      + zone('list','Регіони', body, ann),
      'Стежки: Turrutebasen (Kartverket) і Lantmäteriet. Сезонні дати хиж — із публічної схеми обʼєктів DNT і STF.',
      appnav=False, base='regions.html')

P['regions.html'] = regions(False)
P['regions-empty.html'] = regions(True)

# ══ G2 · КАРТКА МАРШРУТУ ══════════════════════════════════════
ROUTE_MAP = '''      <figure class="bleed">
        <div class="frame frame--map" data-fit="на всю ширину · тап → на весь екран">
          <span>карта<br>Kungsleden, Abisko → Nikkaluokta<br>101 км · 5 хиж · 2 точки сходу</span>
        </div>
        <figcaption>На що мусить відповісти: як стежка йде відносно хиж, де виходить на перевал і де два броди.</figcaption>
      </figure>
      <figure>
        <div class="frame frame--profile" data-fit="на ширину колонки">
          <span>профіль висоти · 1 940 м · найвища точка 1 150 м</span>
        </div>
        <figcaption>На що мусить відповісти: набір розкиданий по днях чи зібраний в один.</figcaption>
      </figure>
      <p class="actions"><a href="./map.html">Відкрити карту на весь екран</a></p>'''

def route(state='ok'):
    cur = {'ok':'route.html','empty':'route-empty.html','error':'route-error.html','loading':'route-loading.html'}[state]
    zones = zone('map','Маршрут на карті', ROUTE_MAP,
      'Карта й профіль. ГОЛОВНА ДІЯ: відкрити карту на весь екран. Це <b>дані, а не ілюстрація</b>: саме ними людина вирішує «чи це той похід», і саме їх нам бракувало проти всіх пʼятьох конкурентів (дірка A1).')

    if state == 'loading':
        zones += zone('facts','Ключові факти','''      <div class="verdict" aria-busy="true">
        <strong>Збираю дані маршруту.</strong>
        <p>Кожен крок — звернення до названого джерела, а не заглушка.</p>
      </div>
      <ul class="signals">
        <li><b>Готово</b> Геометрія й профіль — Lantmäteriet</li>
        <li><b>Зараз</b> Умови на ділянках — Turrutebasen, броди й сніжники</li>
        <li><b>Далі</b> Хижі вздовж маршруту — тип, ключ, ліжка, сезон</li>
        <li><b>Далі</b> Фото й відгуки спільноти</li>
      </ul>
      <p class="actions">
        <button type="button">Скасувати</button>
      </p>
      <p class="ann" data-review lang="uk">РОЗВИЛКА · далі <a href="./route.html">усі джерела відповіли → картка</a> · <a href="./route-error.html">Turrutebasen мовчить → помилка</a></p>''',
      'Ключові факти → <b>завантаження</b>. Етапи названі разом із джерелами — те саме правило, що на B1 (рішення №16). Скасування обовʼязкове.')
    elif state == 'error':
        zones += zone('facts','Ключові факти','''      <div class="verdict" role="alert">
        <strong>Дані маршруту недоступні.</strong>
        <p>Turrutebasen не відповідає з 09:04. Довжина, набір висоти й офіційна градація беруться саме звідти.</p>
      </div>
      <p><b>Чого ми не робимо:</b> не показуємо торішню копію як сьогоднішню й не рахуємо градацію самі — це заборонено окремо, і не нами: DNT просив не заводити альтернативних шкал складності.</p>
      <p>Що вціліло: геометрія й профіль уже завантажені, тому карта вище робоча.</p>
      <p class="actions">
        <form action="./route.html" method="get" style="display:inline"><button type="submit">Спробувати ще раз</button></form>
        <a href="./regions.html">Обрати інший маршрут</a>
      </p>''',
      'Ключові факти → <b>помилка</b>. Показуємо, <b>що саме зламалось</b>, і що вціліло. Два виходи, обидва названі.')
    else:
        zones += zone('facts','Ключові факти','''      <dl>
        <dt>Довжина</dt><dd>101 км · 1 940 м набору · орієнтовно 6 ходових днів</dd>
        <dt>Офіційна градація</dt><dd>blå / medium майже всюди; одна ділянка röd / krevende через Tjäktjapasset
          <small>Це норвезько-шведська офіційна градація, показана як є. Власної шкали ми не рахуємо.</small></dd>
        <dt>Сезон</dt><dd>кінець червня — середина вересня. Поза ним хижі зачинені, човен через Láddjujávri не ходить</dd>
        <dt>Початок і кінець</dt><dd>Abisko Turiststation (потяг) → Nikkaluokta (автобус 91 до Kiruna)</dd>
      </dl>''',
      'Ключові факти. ГОЛОВНОЇ ДІЇ немає — це підстава для рішення. Градація показана з назвою системи й приміткою, що ми її не перераховуємо: констрейнт DNT видно просто в тексті.')

    if state == 'ok':
        zones += zone('cond','Умови на ділянках','''      <ul class="signals">
        <li><b>Вода</b> уздовж усього маршруту, найдовший сухий відрізок 6 км перед перевалом</li>
        <li><b>Броди</b> два: Abiskojåkka (місток) і струмок перед Sälka — влітку по коліно, після дощів вище</li>
        <li><b>Сніжники</b> на Tjäktjapasset тримаються до середини липня</li>
        <li><b>Поверхня</b> 70 км мостків і стежки, 20 км каміння, 11 км болотистого ґрунту</li>
        <li><b>Звʼязок</b> невідомо — оператори не публікують покриття як шар. Перевірте у свого</li>
      </ul>''',
      'Умови на ділянках (сутність 23). Закриває дірку A6: раніше це існувало лише як розріджені нотатки спільноти. «Звʼязок — невідомо» це <b>постійний стан, а не заглушка</b>: ні Nkom, ні PTS не дають покриття придатним шаром.')
        zones += zone('photos','Фото','''      <div class="strip">
        <div class="frame frame--photo" data-fit="4:3"><span>перевал Tjäktjapasset<br>спільнота · CC BY-SA · серп. 2025</span></div>
        <div class="frame frame--photo" data-fit="4:3"><span>Alesjaure fjällstuga<br>STF · за угодою · 2024</span></div>
        <div class="frame frame--photo" data-fit="4:3"><span>брід перед Sälka<br>свідчення стану · лип. 2026</span></div>
      </div>
      <p>Кожен знімок несе джерело, ліцензію й дату. Знімок стану без дати не показуємо взагалі.</p>''',
      'Фото (сутність 21). Заборону знято рішенням №21 — але <b>підстава заборони була «немає джерела», а не «шкідливо»</b>, тому джерело й ліцензія стоять на кожному знімку. Це перетворює фото з ризику на підтвердження простежуваності.')
        zones += zone('reviews','Що кажуть ті, хто йшов','''      <p><b>4,3</b> · 128 відгуків · <b>За останні 30 днів маршрут пройшли 41 людина</b></p>
      <article>
        <h3>Ліжка в Sälka закінчились о 16:00</h3>
        <p>Ішли 8–13 серпня 2026 · досвід: третій багатоденний похід</p>
        <p>Прийшли о 17:30 — місце під дахом дали, але на матраці в коридорі. Наступного разу бронюватиму.</p>
      </article>
      <article>
        <h3>Найкраще — ділянка після Alesjaure</h3>
        <p>Ішла 2–8 серпня 2026 · досвід: ходжу щороку</p>
        <p>22 км другого дня даються важче, ніж здається на профілі: болотисто, мостки місцями розбиті.</p>
      </article>
      <p class="actions"><button type="button">Написати відгук</button></p>''',
      'Відгуки (сутність 22), рівень <b>спільнота</b>. Чотири межі тримаються тут же: оцінка не входить у вердикт узгодженості, не змінює офіційну градацію, <b>не сортує маршрути</b>, і це <b>думка</b>, а не стан — стан живе окремо, у зоні умов вище.')
    elif state == 'empty':
        zones += zone('cond','Умови на ділянках','''      <ul class="signals">
        <li><b>Вода</b> уздовж усього маршруту, найдовший сухий відрізок 6 км перед перевалом</li>
        <li><b>Поверхня</b> 70 км мостків і стежки, 20 км каміння, 11 км болотистого ґрунту</li>
        <li><b>Звʼязок</b> невідомо — оператори не публікують покриття як шар</li>
      </ul>
      <p>Про броди й сніжники на цьому маршруті свіжих свідчень немає — тому ми про них мовчимо, а не пишемо «немає».</p>''',
      'Умови. Частина з офіційних джерел є завжди; частина тримається на свідченнях — і коли їх немає, ми кажемо саме це.')
        zones += zone('photos','Фото','''      <div class="frame frame--photo" data-fit="4:3"><span>знімків цього маршруту поки немає</span></div>
      <p>Ніхто ще не надсилав фото звідси. Це не поламаний блок — просто маршрут новий у продукті.</p>''',
      'Фото → <b>порожній стан</b>. Рамка лишається, щоб було видно місце й пропорцію.')
        zones += zone('reviews','Що кажуть ті, хто йшов','''      <p><b>Відгуків ще немає.</b> Цей маршрут ніхто з наших користувачів поки не проходив — тож і сказати нема чого.</p>
      <p>Що це <b>не</b> означає: що маршрут поганий або складний. Офіційні дані вище від цього не залежать — довжина, градація, хижі й сезон на місці.</p>
      <p class="actions">
        <a class="cta" href="./wizard-when.html">Спланувати цей маршрут</a>
        <button type="button">Пройду — напишу перший відгук</button>
      </p>''',
      '<b>Найважливіший стан цього екрана.</b> Продукт без користувачів — це стан за замовчуванням, а не крайній випадок, і він мусить виглядати гідно. Головне тут — <b>явно розділити «немає відгуків» і «немає даних»</b>: офіційна частина екрана повна, і це сказано вголос.')

    if state != 'loading':
        zones += zone('go','Далі','''      <p class="actions">
        <a class="cta" href="./wizard-when.html">Спланувати цей маршрут</a>
        <a href="./regions.html">Повернутись до регіонів</a>
      </p>
      <p>Маршрут уже обрано — наступний крок питає лише коли й скільки вас.</p>''',
      'ГОЛОВНА ДІЯ екрана: «спланувати цей маршрут» → одразу W2, бо W1 (вибір маршруту) уже пройдено тут. Це і є той порядок, заради якого зʼявилось рішення №20: спершу обираємо, де похід, потім зводимо чотири джерела.')

    return page(cur, f'Wireframe · G2 Картка маршруту · {state}','Kungsleden · Abisko → Nikkaluokta',
      R(f'wireframes/{cur} — <b>G2 Картка маршруту</b> · стан <b>{state}</b>',
        '<code>G1</code> → <code>G2</code> → «спланувати» → <code>W2</code>.',
        'Jobs — <b>R1</b> (скільки я реально пройду на цьому рельєфі), <b>S2</b> (чи це реально для людини як я), <b>E1</b>. Сутність 20 «Маршрут-кандидат».',
        '<p><b>Це та сама «картка маршруту», яку ми свідомо не робили.</b> Тепер робимо — з фото й відгуками, але з чотирма межами сутності 22 і з джерелом на кожному знімку.</p>'),
      zones, 'Геометрія й профіль: Lantmäteriet (CC0). Градація й умови: Turrutebasen (Kartverket, CC BY 4.0). Фото й відгуки: спільнота, рівень джерела позначений на кожному елементі.',
      appnav=False, base='route.html')

for st in ('ok','empty','error','loading'):
    P[{'ok':'route.html','empty':'route-empty.html','error':'route-error.html','loading':'route-loading.html'}[st]] = route(st)

# ══ G3 · КАРТА ════════════════════════════════════════════════
LAYERS = '''      <ul class="signals">
        <li><b>Шари</b> <label><input type="checkbox" checked> маршрут і дні</label> <label><input type="checkbox" checked> хижі за типом</label></li>
        <li><b></b> <label><input type="checkbox" checked> точки сходу</label> <label><input type="checkbox"> вода й броди</label></li>
        <li><b></b> <label><input type="checkbox"> транспортні вузли</label> <label><input type="checkbox"> офіційна градація</label></li>
      </ul>'''

def mapscreen(state='ok'):
    cur = {'ok':'map.html','error':'map-error.html','loading':'map-loading.html'}[state]
    if state == 'ok':
        z = zone('map','Карта',f'''      <figure class="bleed">
        <div class="frame frame--screen" data-fit="на весь екран">
          <span>карта на весь екран<br>Kungsleden, Abisko → Nikkaluokta<br>масштаб 1:50 000 · ©Kartverket / Lantmäteriet</span>
        </div>
      </figure>
{LAYERS}
      <p class="actions"><a href="./plan.html">Повернутись до плану</a></p>''',
      'Карта на весь екран (G3). ГОЛОВНА ДІЯ: перемикати шари. Це <b>поверхня, а не корінь навігації</b> — вхід із G2, B1, B2 і D1. Шари відповідають нашим сутностям: хижі за типом обслуговування, точки сходу, транспортні вузли, вода й броди.')
    elif state == 'loading':
        z = zone('map','Карта',f'''      <figure class="bleed">
        <div class="frame frame--screen" data-fit="на весь екран">
          <span aria-busy="true">завантажую тайли · 12 із 34 МБ<br>Kungsleden, Abisko → Nikkaluokta</span>
        </div>
      </figure>
      <p>Тайли качаються один раз і лишаються в офлайн-пакеті — у горах карта відкриється без мережі.</p>
      <p class="actions"><button type="button">Скасувати</button></p>
      <p class="ann" data-review lang="uk">РОЗВИЛКА · далі <a href="./wizard-route.html">маршрути знайшлись</a> · <a href="./wizard-route-empty.html">нічого не сходиться</a> · <a href="./wizard-route-error.html">стежки недоступні</a></p>
      <p class="ann" data-review lang="uk">РОЗВИЛКА · далі <a href="./map.html">тайли завантажились → карта</a> · <a href="./map-error.html">сервіс тайлів мовчить → помилка</a></p>
{LAYERS}''',
      'Карта → <b>завантаження</b>. Показуємо мегабайти, бо це те, що людина реально вирішує: качати зараз по Wi-Fi чи в дорозі. Скасування є.')
    else:
        z = zone('map','Карта',f'''      <figure class="bleed">
        <div class="frame frame--screen" data-fit="на весь екран">
          <span role="alert">тайли недоступні<br>останнє завантажене: 12 серпня, 18:40</span>
        </div>
      </figure>
      <p><b>Що це означає:</b> сервіс тайлів не відповідає. Маршрут, хижі й точки сходу відомі — їх ми показуємо списком нижче, поки карти немає.</p>
      <ul class="signals">
        <li><b>Хижі</b> Abiskojaure · Alesjaure · Tjäktja · Sälka · Kebnekaise Fjällstation</li>
        <li><b>Точки сходу</b> Alesjaure (човен) · Vakkotavare (автобус 93)</li>
      </ul>
      <p class="actions">
        <form action="./map.html" method="get" style="display:inline"><button type="submit">Спробувати ще раз</button></form>
        <a href="./plan.html">Повернутись до плану</a>
      </p>''',
      'Карта → <b>помилка</b>. Замість порожнього прямокутника — <b>те саме списком</b>: хижі й точки сходу відомі й без тайлів. Два виходи названі.')
    return page(cur, f'Wireframe · G3 Карта · {state}','Карта маршруту',
      R(f'wireframes/{cur} — <b>G3 Карта</b> · стан <b>{state}</b>',
        'Поверхня, не крок потоку. Вхід із <code>G2</code>, <code>B1</code>, <code>B2</code> і <code>D1</code>.',
        'Jobs — <b>R1</b>, <b>R2</b> (хижі за типом на місцевості), <b>R6</b> (транспортні вузли й дорожній доступ). Закриває дірку A1: наш головний актив — офіційні гео-дані, і в них не було власної поверхні.'),
      z, 'Тайли: Kartverket (CC BY 4.0) для Норвегії, Lantmäteriet (CC0) для Швеції. Хижі — публічна схема обʼєктів.',
      base='map.html')

for st,f in (('ok','map.html'),('error','map-error.html'),('loading','map-loading.html')):
    P[f] = mapscreen(st)

# ══ A · ВІЗАРД ════════════════════════════════════════════════
def wiz_head(step):
    return f'''      <p><progress max="3" value="{step}"></progress> Крок {step} з 3</p>
      <p class="actions"><button type="button">Зберегти й вийти</button></p>'''

def wizard_route(state='ok'):
    cur = {'ok':'wizard-route.html','empty':'wizard-route-empty.html','error':'wizard-route-error.html','loading':'wizard-route-loading.html'}[state]
    z = zone('step','Крок', wiz_head(1),
      'Прогрес і вихід (рішення №15). Глобальної навігації у візарді немає — це воронка. Але «зберегти й вийти» є: відсутність навігації не означає, що людину замкнули.')
    if state == 'ok':
        z += zone('where','Де і коли','''      <form action="./wizard-when.html" method="get">
        <label for="reg">Регіон</label>
        <p class="actions"><button type="button">Лапландія</button><button type="button">Jotunheimen</button><button type="button">Hardangervidda</button></p>
        <label for="mon">Орієнтовний місяць</label>
        <p class="actions"><button type="button">Червень</button><button type="button">Липень</button><button type="button">Серпень</button><button type="button">Вересень</button></p>
      </form>''',
      'Регіон і місяць. ГОЛОВНА ДІЯ: обрати. Місяць тут обовʼязковий: без нього список маршрутів нижче був би неправдою — хижі відчиняються за сезоном.')
        z += zone('cands','Маршрути, що вкладаються','''      <figure class="bleed">
        <div class="frame frame--map" data-fit="на всю ширину"><span>карта регіону<br>3 маршрути, що вкладаються у ваш бриф</span></div>
      </figure>
      <article>
        <h3>Kungsleden · Abisko → Nikkaluokta</h3>
        <ul class="signals">
          <li><b>Розмір</b> 101 км · 6 днів · blå / medium</li>
          <li><b>Ночівлі</b> 5 хиж STF уздовж усього шляху</li>
          <li><b>Дорога</b> потяг до старту, автобус від фінішу</li>
        </ul>
        <p class="actions"><form action="./wizard-when.html" method="get" style="display:inline"><button type="submit">Обрати</button></form> <a href="./route.html">Детальніше</a></p>
      </article>
      <article>
        <h3>Abisko → Kebnekaise, коротка версія</h3>
        <ul class="signals">
          <li><b>Розмір</b> 82 км · 5 днів · blå / medium</li>
          <li><b>Ночівлі</b> 4 хижі STF</li>
          <li><b>Дорога</b> та сама, фініш через Nikkaluokta</li>
        </ul>
        <p class="actions"><form action="./wizard-when.html" method="get" style="display:inline"><button type="submit">Обрати</button></form> <a href="./route.html">Детальніше</a></p>
      </article>
      <p>Порядок — за відповідністю вашому брифу. Не за популярністю: сортування за рейтингом перетворює планувальник на машину популярності.</p>''',
      'Маршрути під бриф. ГОЛОВНА ДІЯ: обрати маршрут. Рядок про сортування стоїть у продукті навмисно — це межа рішення №21, і вона має бути видима, а не лише записана в документі.')
    elif state == 'loading':
        z += zone('cands','Шукаю маршрути','''      <div class="verdict" aria-busy="true">
        <strong>Шукаю маршрути під ваш бриф.</strong>
      </div>
      <ul class="signals">
        <li><b>Готово</b> Стежки регіону — Turrutebasen і Lantmäteriet</li>
        <li><b>Зараз</b> Відкидаю ті, що не вкладаються в серпень: сезон хиж</li>
        <li><b>Далі</b> Перевіряю, чи є дорога до старту й від фінішу</li>
      </ul>
      <p class="actions"><button type="button">Скасувати</button></p>
      <p><b>Далі одне з трьох:</b>
        <a href="./wizard-route.html">маршрути знайшлись</a> ·
        <a href="./wizard-route-empty.html">нічого не вкладається в бриф</a> ·
        <a href="./wizard-route-error.html">стежки недоступні</a></p>''',
      'Перший live-запит продукту, ще до генерації плану. Етапи названі — те саме правило, що на B1.')
    elif state == 'error':
        z += zone('cands','Маршрути','''      <div class="verdict" role="alert">
        <strong>Стежки недоступні — маршрути показати не можемо.</strong>
        <p>Turrutebasen і Lantmäteriet не відповідають з 09:04. Без них немає ні геометрії, ні градації, ні довжини.</p>
      </div>
      <p><b>Чого ми не робимо:</b> не показуємо список маршрутів «з памʼяті». Маршрут, зібраний зі здогадів, виглядав би так само впевнено, як справжній.</p>
      <p class="actions">
        <form action="./wizard-route.html" method="get" style="display:inline"><button type="submit">Спробувати ще раз</button></form>
        <a href="./regions.html">Обрати з кураторських регіонів</a>
      </p>
      <p>Кураторські регіони зібрані заздалегідь і лежать у нас — вони працюють і зараз.</p>''',
      'Помилка критичного джерела. Третій вихід тут особливо цінний: <b>куровані регіони не залежать від живого джерела</b>, тому в цьому стані вони й рятують.')
    else:
        z += zone('cands','Маршрути, що вкладаються','''      <p><b>У серпні в Jotunheimen нічого не сходиться під ваш бриф.</b></p>
      <p>Ви шукали 3–4 дні з ночівлями в хижах DNT. Маршрути такої довжини тут або починаються за 6 годин їзди від найближчої станції, або проходять через хижі, зачинені на ремонт до вересня.</p>
      <ul class="signals">
        <li><b>Варіант 1</b> Той самий регіон, 6 днів — тоді ланцюжок хиж складається</li>
        <li><b>Варіант 2</b> Вересень замість серпня — хижі відкриються</li>
        <li><b>Варіант 3</b> Лапландія: там є 4-денні маршрути з хижами STF</li>
      </ul>
      <p class="actions">
        <form action="./wizard-route.html" method="get" style="display:inline"><button type="submit">Шість днів</button></form><form action="./wizard-route.html" method="get" style="display:inline"><button type="submit">Вересень</button></form><form action="./wizard-route.html" method="get" style="display:inline"><button type="submit">Лапландія</button></form>
      </p>''',
      'Порожній стан. Причина названа конкретно (<b>чому</b> не сходиться, а не «нічого не знайдено»), три виходи з наслідком. Те саме правило рішення №12, що й на B1.')
    return page(cur, f'Wireframe · W1 Маршрут · {state}','Куди йдемо',
      R(f'wireframes/{cur} — <b>W1 Маршрут</b> · стан <b>{state}</b>',
        '<code>Стартовий екран</code> → <code>QKNOW: так</code> → <code>W1</code> → <code>QROUTE</code> → <code>W2</code>.',
        'Jobs — <b>MAIN</b> (без обраного маршруту нема чого узгоджувати) і <b>R1</b>. Перший крок продукту з рішення №20.'),
      z, 'Стежки й градація: Turrutebasen (Kartverket), Lantmäteriet. Сезонні дати хиж — публічна схема обʼєктів.',
      appnav=False, base='wizard-route.html')

for st,f in (('ok','wizard-route.html'),('empty','wizard-route-empty.html'),('error','wizard-route-error.html'),('loading','wizard-route-loading.html')):
    P[f] = wizard_route(st)

# ══ W2 · КОЛИ І СКІЛЬКИ НАС ═══════════════════════════════════
def wizard_when(state='ok'):
    cur = {'ok':'wizard-when.html','empty':'wizard-when-empty.html','error':'wizard-when-error.html'}[state]
    filled = state != 'empty'
    z = zone('step','Крок', wiz_head(2),
      'Прогрес і вихід. Для Kristin «Скласти план» стоїть саме тут: W3 приходить із акаунта цілком, тому її шлях — три тапи.')
    z += zone('when','Коли', f'''      <form action="./plan-loading.html" method="get">
        <label for="d1">Вікно дат</label>
        <p>{'17 – 22 серпня 2026' if filled else 'не заповнено'}</p>
        <p><label><input type="checkbox" {'checked' if filled else ''}> дати не рухаються — куплені квитки</label></p>
        <label for="dur">Тривалість і запас</label>
        <p>{'6 ходових днів · запасний день: так' if filled else 'не заповнено'}</p>
      </form>''',
      'Дати й тривалість. Прапорець «дати не рухаються» — не деталь: саме він вирішує, що продукт рухатиме в тупику, маршрут чи вікно. Запасний день стоїть на прямому носії болю: «Korkat av mig att inte ha en reservdag».')
    z += zone('party','Скільки нас', f'''      <p>{'Двоє · обоє члени STF' if filled else 'не заповнено'}</p>
      <p>Питаємо не з цікавості: бронь — це N ліжок, частина спорядження спільна, квитки й вартість — на людину, а в замкнену хижу потрібен щонайменше один член асоціації.</p>''',
      'Розмір групи (рішення №21, дірка A3). Це <b>арифметика, а не сегмент</b>: без цього поля не рахується ні бронь, ні спорядження, ні вартість — і формула гарантії має випадок «група без жодного члена».')
    if state == 'ok':
        z += zone('flex','Гнучкі дати','''      <p>Ваше вікно позначене як жорстке — тому сітка нижче лише показує, що ви пропускаєте.</p>
      <ul class="signals">
        <li><b>10–15 серп</b> ліжка є всюди · дощ 2 з 6 днів · потяги за розкладом</li>
        <li><b>17–22 серп</b> ліжка є всюди · дощ 2 з 6 днів · потяги за розкладом — <b>ваш тиждень</b></li>
        <li><b>24–29 серп</b> ліжка є всюди · дощ 1 з 6 днів · ремонт колії, автобус замість потяга</li>
        <li><b>31 серп – 5 вер</b> Tjäktja зачиняється 1 вересня · менше людей</li>
      </ul>
      <p class="actions"><button type="button">Зняти жорсткість дат</button></p>''',
      'Сітка гнучких дат (рішення №21, дірка A5). Патерн узятий у Skyscanner свідомо. Усе, що ми зводимо, залежить від тижня — ліжка, погода, транспорт, сезон хиж — і <b>в категорії цього немає ні в кого</b>.')
        z += zone('go','Далі','''      <p class="actions">
        <a class="cta" href="./plan-loading.html">Скласти план</a>
        <a href="./wizard-about.html">Спершу перевірити дані про себе</a>
      </p>
      <p>Форма, спорядження й членство вже є в акаунті — ми беремо їх звідти. Змінити можна на кроці 3.</p>''',
      'ГОЛОВНА ДІЯ: «Скласти план». Для primary генерація живе тут, бо W3 префіляється з акаунта — це і є ті самі 3 тапи проти 4 на холодному старті.')
    elif state == 'empty':
        z += zone('flex','Гнучкі дати','''      <p>Заповніть вікно дат — і ми покажемо, який тиждень найкращий за ліжками, погодою й транспортом.</p>''',
      'Порожній стан сітки: без дат порівнювати нема чого. Зона лишається на місці — стан не має права прибирати зону.')
        z += zone('go','Далі','''      <p class="actions">
        <button type="button" disabled>Скласти план</button>
        <form action="./wizard-when.html" method="get" style="display:inline"><button type="submit">Заповнити з акаунта</button></form>
      </p>
      <p>Спершу дати й склад групи — без них план не складеться. Дати ми не памʼятаємо (це і є новий похід), а склад групи можна підтягнути з минулого разу.</p>''',
      'Порожній стан екрана — це <b>холодний старт</b>, тобто перше знайомство з продуктом. Кнопка неактивна, і поруч сказано, чого бракує.')
    else:
        z += zone('flex','Гнучкі дати','''      <p>Ваше вікно жорстке — сітка показує лише те, що ви пропускаєте.</p>''','Без змін у цьому стані.')
        z += zone('go','Далі','''      <div class="verdict" role="alert">
        <strong>План складається на сервері — потрібна мережа.</strong>
        <p>Зараз її немає. Усе введене збережено: дати, склад, маршрут.</p>
      </div>
      <p>Щойно мережа зʼявиться, план складеться сам, і ви знайдете його в «Моїх походах». Нічого перезаповнювати не доведеться.</p>
      <p class="actions">
        <form action="./plan-loading.html" method="get" style="display:inline"><button type="submit">Спробувати зараз</button></form>
        <button type="button">Зберегти й вийти</button>
      </p>''',
      '<b>Єдине місце продукту, де офлайн не має продуктового результату</b>: генерація серверна, і плану взятись нізвідки. Це межа архітектури, а не недоробка UI. Три частини стану обовʼязкові: причина, гарантія збереження, обіцянка автостарту.')
    return page(cur, f'Wireframe · W2 Коли і скільки нас · {state}','Коли і скільки нас',
      R(f'wireframes/{cur} — <b>W2 Коли і скільки нас</b> · стан <b>{state}</b>',
        '<code>W1</code> → <code>W2</code> → <code>QGEN</code> → <code>LOAD</code>.',
        'Jobs — <b>R1</b> (розмір походу під форму й час), <b>R6</b> (прапорець жорстких дат), <b>R2</b ,<b>R7</b> (розмір групи → ліжка й вартість).'),
      z, 'Наявність ліжок по тижнях — ілюстративна: жива наявність потребує угоди зі STF. Погода: met.no. Транспорт: Trafikverket.',
      appnav=False, base='wizard-when.html')

for st,f in (('ok','wizard-when.html'),('empty','wizard-when-empty.html'),('error','wizard-when-error.html')):
    P[f] = wizard_when(st)

# ══ W3 · ПРО МЕНЕ ═════════════════════════════════════════════
def wizard_about(state='ok'):
    cur = {'ok':'wizard-about.html','empty':'wizard-about-empty.html','error':'wizard-about-error.html'}[state]
    filled = state != 'empty'
    z = zone('step','Крок', wiz_head(3),
      'Прогрес і вихід. Цей екран зібрано за одним принципом: <b>усе, що приходить із акаунта, живе в одному місці</b> — саме тому кроків стало девʼять, а екранів лишилось три.')
    z += zone('fit','Форма й темп', f'''      <label for="anchor">Найдовший денний перехід за минулий рік</label>
      <p>{'24 км, рюкзак 12 кг, три дні поспіль' if filled else 'не заповнено'}</p>
      <label for="self">Як ви оцінюєте себе</label>
      <p>{'досвідчена — ходжу щороку' if filled else 'не заповнено'}</p>
      <p>Питаємо двома способами навмисно. Факт і самооцінка часто розходяться — і якщо розійдуться, ми скажемо про це в поясненні плану, а не переоцінимо маршрут за вас.</p>''',
      'Форма (рішення №19). Якірне <b>фактичне</b> питання плюс самооцінка. Підстава: Røde Kors і DNT задокументували, що люди системно себе переоцінюють — тож будувати вхід у формулу R1 на самій самооцінці означало б узяти за основу той самий механізм, який наші джерела називають причиною аварій.')
    z += zone('gear','Спорядження', f'''      <p>{'Каремат, спальник −5, пальник, дощовик. Немає: гамаші, водонепроникні рукавиці' if filled else 'не заповнено'}</p>
      <p class="actions"><a href="./gear.html">Відкрити інвентар</a></p>''',
      'Наявне спорядження. Носій задокументованого болю тут <b>secondary</b>, не Kristin — тримаємо це видимим, щоб не роздути зону.')
    z += zone('sleep','Де ночую', f'''      <p>{'Хижі STF і DNT · членство STF №4471902 · DNT-ключа немає' if filled else 'не заповнено'}</p>
      <p>Членство — не преференція, а <b>умова доступу</b>: від нього залежить і ціна, і чи відчиниться замкнена хижа.</p>
      <details>
        <summary>Бюджет — необовʼязково</summary>
        <p>Можна не заповнювати. Ми все одно покажемо, скільки коштуватиме похід, — але не робитимемо з бюджету бар'єра перед планом.</p>
      </details>''',
      'Режим ночівлі й членство — <b>змінна №4 формули гарантії</b>. Бюджет згорнутий і пропускається за замовчуванням: під ним немає підтвердженого болю (H3).')
    if state == 'error':
        z += zone('go','Далі','''      <div class="verdict" role="alert">
        <strong>План складається на сервері — потрібна мережа.</strong>
        <p>Зараз її немає. Усе введене збережено.</p>
      </div>
      <p class="actions"><form action="./plan-loading.html" method="get" style="display:inline"><button type="submit">Спробувати зараз</button></form> <button type="button">Зберегти й вийти</button></p>''',
      'Той самий офлайн-блок, що на W2 — але на холодному старті генерація живе саме тут. Один стан, два місця; малюємо один раз, і це записано в конвенціях.')
    else:
        z += zone('go','Далі', f'''      <p class="actions">
        <a class="cta" href="./plan-loading.html">Скласти план</a>
      </p>
      <p>{'Усе на місці.' if filled else 'Можна лишити порожнім — тоді план буде обережнішим: без даних про форму ми беремо нижчу межу, а не середню.'}</p>''',
      'ГОЛОВНА ДІЯ: «Скласти план». Порожній варіант не блокує: <b>без даних беремо нижчу межу, а не середню</b> — це «деградувати чесно» у формі поведінки, а не напису.')
    return page(cur, f'Wireframe · W3 Про мене · {state}','Про мене',
      R(f'wireframes/{cur} — <b>W3 Про мене</b> · стан <b>{state}</b>',
        '<code>W2</code> → <code>QBUDGET</code> → <code>W3</code> → <code>QGEN</code> → <code>LOAD</code>.',
        'Jobs — <b>R1</b>, <b>E2</b> (форма й темп), <b>R4</b> (спорядження), <b>R2</b> (членство як credential).'),
      z, 'Дані про членство зберігаються в акаунті як credential, не як преференція.',
      appnav=False, base='wizard-about.html')

for st,f in (('ok','wizard-about.html'),('empty','wizard-about-empty.html'),('error','wizard-about-error.html')):
    P[f] = wizard_about(st)

# ══ B2 · ДЕНЬ ═════════════════════════════════════════════════
P['day.html'] = page('day.html','Wireframe · B2 День · успіх','День 3 · ср 19 серпня',
  R('wireframes/day.html — <b>B2 День</b> · станів із таблиці немає',
    '<code>B1</code> → <code>B2</code> → <code>B3</code> / <code>B5</code> / шар «чому саме так».',
    'Jobs — <b>R1</b>, <b>R3</b>, <b>R4</b>. У таблиці _screens.md рядок B2 <b>порожній по всіх чотирьох станах</b>, тому сторінок станів немає: власних запитів екран не робить (свіжість перевіряється один раз на вході в B1), а недоступність некритичного джерела виражається як degraded усередині зон.'),
  zone('leg','Перехід','''      <p>Alesjaure → Tjäktja · 13 км · +260 м · близько 4 год 30</p>
      <figure class="bleed">
        <div class="frame frame--map" data-fit="на всю ширину · тап → на весь екран"><span>карта дня<br>Alesjaure → Tjäktja · 13 км</span></div>
        <figcaption>На що мусить відповісти: де стежка виходить із долини й де брід перед хижею.</figcaption>
      </figure>
      <details>
        <summary>Офіційна градація: blå / medium</summary>
        <p>Це норвезько-шведська офіційна градація для цієї ділянки, показана як є. Власної шкали «ваша форма → складність» ми не рахуємо: DNT публічно просив не заводити альтернативних систем.</p>
      </details>
      <p class="actions"><a href="./map.html">Відкрити карту</a></p>''',
    'Перехід дня. ГОЛОВНА ДІЯ: відкрити карту. Градація — <b>шар</b>, а не наша оцінка; правило видно просто в тексті.')
  + zone('cond','Умови на цій ділянці','''      <ul class="signals">
        <li><b>Вода</b> струмки кожні 2–3 км, останній за 1 км до хижі</li>
        <li><b>Брід</b> один, перед Tjäktja — влітку по коліно, після дощів вище</li>
        <li><b>Поверхня</b> 8 км мостків, 5 км каміння</li>
        <li><b>Звʼязок</b> невідомо — оператори не публікують покриття як шар</li>
      </ul>''',
    'Умови на ділянці (сутність 23). Закриває дірку A6. «Звʼязок — невідомо» це <b>постійний стан</b>, не заглушка.')
  + zone('weather','Погода','''      <ul class="signals">
        <li><b>Прогноз</b> +9 °C, дощ 4 мм, вітер 7 м/с · met.no, зчитано 13 серпня 09:12</li>
        <li><b>Що це міняє</b> дощовик і гамаші сьогодні критичні; брід після дощу може бути вищим</li>
      </ul>''',
    'Погода дня. Показуємо <b>не самі числа, а що вони міняють</b> — інакше це просто віджет погоди.')
  + zone('night','Ночівля','''      <p>Tjäktja fjällstuga (STF) · ліжко заброньоване · прийти до 18:00</p>
      <p class="actions"><a href="./night.html">Гарантія й доступ на цю ніч</a></p>''',
    'Ночівля дня. ГОЛОВНА ДІЯ: перейти на B3 — це один із двох рівноправних входів у наш диференціатор (другий — із ланцюжка ночей).')
  + zone('why','Чому саме так','''      <details>
        <summary>Що вплинуло на цей день</summary>
        <p>Довжина 13 км: ваш найдовший перехід торік — 24 км, але третій день поспіль, тому взято нижчу межу.</p>
        <p>Хижа Tjäktja: наступна за нею Sälka за 12 км, і разом це 25 км — забагато на третій день.</p>
        <p>Спорядження: дощ 4 мм і брід.</p>
        <p><b>Що не враховано:</b> жива наявність ліжок — джерела немає, потрібна угода зі STF.</p>
      </details>''',
    'Шар «чому саме так» (named-contributor breakdown, R5). Свідомо <b>шар, а не екран</b>: це наша ставка, а не підтверджена потреба. Останній рядок — «чого не враховано» — обовʼязковий.')
  + zone('back','Повернутись', '''      <p class="actions">
        <a class="cta" href="./plan.html">До плану по днях</a>
        <a href="./night.html">Гарантія на цю ніч</a>
        <a href="./gear.html">Спорядження</a>
      </p>''', 'Вихід із дня. Кожна сторінка мусить мати названий вихід — це правило потоків, і на вайрфреймі воно перевіряється тривіально: посилання або є, або ні.')
  + zone('bail','Якщо доведеться зійти','''      <p>Найближчий вихід: Alesjaure, 13 км назад — човен по озеру до Abisko, ходить до 15 вересня.</p>
      <p>Далі на маршруті виходів немає до Vakkotavare — це ще два дні.</p>''',
    'Точка сходу (сутність 19). Не аварійна кнопка й не SOS: показуємо, <b>куди ще можна зійти й доки цей варіант живий</b>. Виклик допомоги — не наша функція.'),
  'Стежки й градація: Turrutebasen (Kartverket). Погода: met.no Locationforecast. Умови: Turrutebasen і свідчення спільноти, рівень позначено.')

# ══ B3 · НІЧ ══════════════════════════════════════════════════
def night(state='ok'):
    cur = {'ok':'night.html','empty':'night-empty.html','error':'night-error.html'}[state]
    if state == 'ok':
        z = zone('guar','Що вам гарантовано','''      <div class="verdict">
        <strong>Ліжко заброньоване. Прийти до 18:00.</strong>
        <p>Після 18:00 бронь не тримають: місце під дахом лишиться, але вже неспецифіковане — можливо, матрац на підлозі.</p>
      </div>
      <dl>
        <dt>Тип обʼєкта</dt><dd>Selvbetjent (самообслуговування) · fjällstuga STF</dd>
        <dt>Бронь</dt><dd>є, на 2 ліжка
          <small data-mock>Статус броні ілюстративний. Жива наявність ліжок потребує угоди про дані зі STF.</small></dd>
        <dt>Час приходу</dt><dd>до 18:00 — шведське правило, воно змінює <b>зміст</b> гарантії, а не її наявність</dd>
        <dt>Членство</dt><dd>STF, обоє — тариф членський, доступ до замкнених обʼєктів є</dd>
      </dl>
      <p>Спільний принцип обох країн: <b>нікого не виганяють</b>. Бронь купує конкретне ліжко; без броні лишається місце під дахом.</p>''',
      '<b>Головний диференціюючий екран продукту.</b> Це формула з чотирьох змінних — тип × бронь × час приходу × членство — і жоден generic-lodging suggester її не виражає. Позначка ілюстративності стоїть <b>на самому полі</b> броні, а не в хромі.')
        z += zone('todo','Що зробити на місці','''      <ul class="signals">
        <li><b>Ключ</b> не потрібен — Tjäktja не замкнена</li>
        <li><b>Логбук</b> записати імена й номер членства, навіть якщо бронювали онлайн</li>
        <li><b>Оплата</b> самореєстрація на місці, якщо бронь не покриває</li>
        <li><b>Прибирання</b> прибрати за собою перед виходом — це не ввічливість, а умова системи</li>
      </ul>
      <p class="actions"><span class="nav-todo">Як працює ця система ночівлі — екран кроку 8</span></p>''',
      'Дії на місці. Бронь <b>не закриває роботу</b> — логбук обовʼязковий навіть після онлайн-оплати. Це задокументована процедура DNT/STF, а не наша інтерпретація.')
        z += zone('photos','Фото й відгуки','''      <div class="strip">
        <div class="frame frame--photo" data-fit="4:3"><span>Tjäktja fjällstuga<br>STF · за угодою · 2024</span></div>
        <div class="frame frame--photo" data-fit="4:3"><span>кухня, самообслуговування<br>спільнота · CC BY-SA · лип. 2026</span></div>
      </div>
      <p><b>4,1</b> · 34 відгуки · рівень: спільнота</p>
      <article>
        <h3>Води треба нести з собою</h3>
        <p>Була 5 серпня 2026 · досвід: ходжу щороку</p>
        <p>Крамниці немає взагалі. Дрова були, вода зі струмка за 200 м.</p>
      </article>''',
      'Фото й відгуки про обʼєкт (сутності 21 і 22), рівень <b>спільнота</b>, візуально відділені від формули вище. Оцінка не входить у вердикт узгодженості й не змінює нічого в гарантії.')
        z += zone('back','Повернутись', '''      <p class="actions">
        <a class="cta" href="./plan.html">До плану по днях</a>
        <a href="./day.html">До дня 3</a>
      </p>''', 'Вихід. B3 має два входи (з дня і з ланцюжка ночей) — виходи теж два.')
    elif state == 'empty':
        z = zone('guar','Що вам гарантовано','''      <div class="verdict">
        <strong>Обʼєкт на цю ніч не підтверджений.</strong>
        <p>План склався в неповному вигляді: на 19 серпня ми не знайшли обʼєкта, який точно працює. Вигадувати хижу, якої може не бути, ми не будемо.</p>
      </div>
      <p><b>Що це означає на практиці:</b> ніч треба або замінити, або йти з наметом за allemansrätten — але тоді спорядження зміниться.</p>
      <p class="actions">
        <form action="./plan-loading.html" method="get" style="display:inline"><button type="submit">Замінити цю ніч</button></form>
        <form action="./plan-loading.html" method="get" style="display:inline"><button type="submit">Іти з наметом — перерахувати спорядження</button></form>
      </p>''',
      'Порожній стан <b>на диференціаторі</b>. Це легальний результат: MAIN дозволяє згенерувати план у degraded, тому ніч без підтвердженого обʼєкта потрапляє сюди штатно. <b>Відновлення живе тут же</b> (рішення №11) — не «піди на B1 і сформулюй це текстом».')
        z += zone('todo','Що зробити на місці','''      <p>Поки обʼєкт не визначено, сказати нема чого: правила залежать від типу — у selvbetjent потрібен спальник і самореєстрація, у обслуговуваній хижі ні.</p>''',
      'Зона лишається порожньою чесно: правила залежать від типу обʼєкта, а типу ми не знаємо.')
        z += zone('photos','Фото й відгуки','''      <p>Немає обʼєкта — немає ні фото, ні відгуків.</p>''','Порожньо як наслідок, а не як окремий збій.')
    else:
        z = zone('guar','Що вам гарантовано','''      <div class="verdict" role="alert">
        <strong>Довідник правил недоступний — показуємо формулу зі статичних полів.</strong>
        <p>Сервіс правил ночівлі не відповідає з 09:04. Те, що нижче, зібрано з полів, які вже є в плані.</p>
      </div>
      <dl>
        <dt>Тип обʼєкта</dt><dd>Selvbetjent (самообслуговування) · fjällstuga STF</dd>
        <dt>Ключ</dt><dd>не потрібен — обʼєкт не замкнений</dd>
        <dt>Ліжка</dt><dd>18 місць, з них частину тримають для тих, хто прийде без броні</dd>
        <dt>Сезон</dt><dd>відчинено 20 червня — 15 вересня</dd>
      </dl>
      <p><b>Чого зараз не скажемо:</b> точний час приходу для цього обʼєкта й локальні правила прибирання. Вони живуть у довіднику, а він мовчить.</p>
      <p class="actions">
        <form action="./night.html" method="get" style="display:inline"><button type="submit">Спробувати ще раз</button></form>
        <span class="nav-todo">Загальні правила системи STF — екран кроку 8</span>
      </p>''',
      'Помилка → <b>не зупиняє екран</b>: формула добудовується зі статичних полів (тип, ключ, ліжка, сезон), і чесно названо, чого бракує. Це найважливіша поведінка нашого диференціатора у зламаному стані.')
        z += zone('todo','Що зробити на місці','''      <p>Загальне правило системи STF діє й без довідника: логбук з іменем і номером членства обовʼязковий, за собою прибрати, оплату лишити при самореєстрації.</p>''',
      'Показуємо те, що знаємо напевно з рівня системи, а не з конкретного обʼєкта.')
        z += zone('photos','Фото й відгуки','''      <p>Фото й відгуки з кешу, останнє оновлення 12 серпня.</p>''','Кеш працює й тоді, коли живе джерело мовчить.')
    return page(cur, f'Wireframe · B3 Ніч · {state}','Ніч 3 · Tjäktja',
      R(f'wireframes/{cur} — <b>B3 Ніч: гарантія й доступ</b> · стан <b>{state}</b>',
        '<code>B2</code> → <code>B3</code>, і другий рівноправний вхід <code>B8</code> → <code>B3</code>.',
        'Jobs — <b>R2</b> (Top Job #1) і <b>E1</b>. Формула чотирьох змінних — найточніша форма нашого диференціатора.'),
      z, 'Тип, ключ, ліжка й сезон — із публічної схеми обʼєктів. Жива наявність ліжок заблокована: потрібна угода зі STF.',
      base='night.html')

for st,f in (('ok','night.html'),('empty','night-empty.html'),('error','night-error.html')):
    P[f] = night(st)

# ══ B5 · СПОРЯДЖЕННЯ ══════════════════════════════════════════
P['gear.html'] = page('gear.html','Wireframe · B5 Спорядження · успіх','Спорядження',
  R('wireframes/gear.html — <b>B5 Спорядження</b> · станів із таблиці немає',
    '<code>B1</code> → <code>B5</code> і <code>B2</code> → <code>B5</code> — два рівноправні входи.',
    'Job — <b>R4</b>. Рядок B5 у _screens.md порожній по всіх чотирьох станах: чекліст виводиться з погоди й типів ночівлі разом із планом, власних запитів не робить. Незаповнений інвентар змінює <b>зміст</b> («взяти» замість «є в мене»), а не дає порожній стан.',
    '<p>⚠️ <b>Чесно про підставу:</b> R4 має найслабшу доказову базу набору, і єдиний задокументований носій болю — secondary-персона, не Kristin. Тому зона коротка й не в центрі продукту.</p>'),
  zone('list','Що взяти','''      <ul class="signals">
        <li><b>Є в мене</b> <label><input type="checkbox" checked> спальник −5</label> · <label><input type="checkbox" checked> каремат</label> · <label><input type="checkbox" checked> пальник і газ</label></li>
        <li><b>Взяти</b> <label><input type="checkbox"> дощовик</label> · <label><input type="checkbox"> запасні шкарпетки ×3</label></li>
        <li><b>Купити</b> <label><input type="checkbox"> гамаші</label> · <label><input type="checkbox"> водонепроникні рукавиці</label></li>
        <li><b>На двох</b> <label><input type="checkbox" checked> намет (несе одна людина)</label> · <label><input type="checkbox"> аптечка</label></li>
      </ul>
      <p>23 позиції · 19 є · 3 докупити · 1 позичити</p>''',
    'Чекліст. ГОЛОВНА ДІЯ: відмітити зібране. Категорія «На двох» зʼявилась із розміру групи (рішення №21): без неї чекліст брехав би — намет і аптечка не потрібні кожному окремо.')
  + zone('why','Чому саме це','''      <ul class="signals">
        <li><b>Гамаші</b> 12 мм дощу на 3-й і 4-й дні + 11 км болотистого ґрунту</li>
        <li><b>Рукавиці</b> +6 °C і вітер 12 м/с на Tjäktjapasset — це четвертий день</li>
        <li><b>Спальник</b> три ночі в selvbetjent: ковдр там немає, тільки матраци</li>
        <li><b>Чого можна не брати</b> фільтр для води — струмки на всьому маршруті; намет — хижі заброньовані всі пʼять ночей</li>
      </ul>''',
    'Пояснення. Job сформульований у <b>два боки</b>: не тягнути зайве й не забути критичне — тому «чого можна не брати» це не бонус, а половина відповіді.')
  + zone('back','Повернутись', '''      <p class="actions">
        <a class="cta" href="./plan.html">До плану по днях</a>
        <a href="./day.html">До дня 3</a>
      </p>''', 'Вихід зі спорядження — два входи були, два виходи є.')
  + zone('inv','Інвентар','''      <p class="actions"><span class="nav-todo">Оновити інвентар — екран кроку 8</span></p>
      <p>Інвентар живе в акаунті: спорядження довготривале, і переписувати його щоразу — рівно те тертя, яке ми обіцяємо зняти.</p>''',
    'Вхід в інвентар (F2). Підстава акаунта тут не персоналізація, а те, що ці дані мусять пережити закриту вкладку.'),
  'Погода: met.no. Типи обʼєктів ночівлі — публічна схема. Список складається з погоди, типу ночівлі, рельєфу й сезону.')

# ══ B6 · ТРАНСПОРТ ════════════════════════════════════════════
def transport(state='ok'):
    cur = {'ok':'transport.html','empty':'transport-empty.html','error':'transport-error.html','loading':'transport-loading.html'}[state]
    if state == 'ok':
        z = zone('there','Дорога туди','''      <article class="leg">
        <h3>нд 16 серпня</h3>
        <p>Нічний потяг 94 · Stockholm C 18:11 → Abisko Turiststation 10:23</p>
        <ul class="signals">
          <li><b>Статус</b> за розкладом · Trafikverket, перевірено 13 серпня 09:12</li>
          <li><b>Дорога</b> Abisko Turiststation стоїть на E10 — замінний автобус сюди доїде</li>
          <li><b>Квиток</b> 1 190 SEK на людину · ще не куплений</li>
        </ul>
      </article>''',
      'Плече до старту. <b>Дорожній доступ — окреме поле, а не деталь</b>: до частини станцій Malmbanan дороги немає взагалі, і тоді замінний автобус фізично неможливий.')
        z += zone('back','Дорога назад','''      <article class="leg">
        <h3>сб 22 серпня</h3>
        <p>Автобус 91 · Nikkaluokta 16:00 → Kiruna 17:20 · далі нічний потяг 92 о 19:44</p>
        <ul class="signals">
          <li><b>Статус</b> за розкладом</li>
          <li><b>Запас</b> 2 год 24 між автобусом і потягом — один пропущений автобус ще лишає вечірній варіант</li>
          <li><b>Останній автобус</b> о 18:00. Після нього виїхати з Nikkaluokta нічим</li>
        </ul>
      </article>''',
      'Плече від фінішу. «Останній автобус» — не довідка, а <b>дедлайн дня 6</b>: він визначає, коли треба вийти з Kebnekaise.')
        z += zone('alt','Якщо щось піде не так','''      <ul class="signals">
        <li><b>Vakkotavare</b> вихід із маршруту на 4-й день · автобус 93 о 16:40, дорога є</li>
        <li><b>Alesjaure</b> човен по озеру до Abisko, ходить до 15 вересня</li>
        <li><b>Katterat</b> станція без дороги — сюди замінний автобус не приїде ніколи</li>
      </ul>''',
      'Альтернативні точки входу-виходу. Katterat названий явно як приклад того, що ми вміємо, а конкуренти ні: «дійти можна, автобус приїхати не може» — обчислюється з відкритих даних.')
        z += zone('back','Повернутись', '''      <p class="actions"><a class="cta" href="./plan.html">До плану по днях</a></p>''',
      'Вихід. У стані «успіх» він теж потрібен: інакше транспорт стає кінцевою сторінкою.')
    elif state == 'loading':
        z = zone('there','Дорога туди','''      <div class="verdict" aria-busy="true">
        <strong>Перевіряю статус рейсів.</strong>
        <p>Розклад уже відомий — уточнюємо, чи не змінилось щось сьогодні.</p>
      </div>
      <ul class="signals">
        <li><b>Готово</b> Розклад — Trafikverket</li>
        <li><b>Зараз</b> Статус рейсу 94 на 16 серпня</li>
        <li><b>Далі</b> Автобус 91 і зворотний потяг</li>
      </ul>
      <p><b>Далі одне з трьох:</b>
        <a href="./transport.html">рейси за розкладом</a> ·
        <a href="./transport-empty.html">рух скасовано</a> ·
        <a href="./transport-error.html">джерело мовчить і кешу немає</a></p>
      <p class="actions"><a class="cta" href="./plan.html">До плану по днях</a></p>''',
      'Стан рейсу — <b>живе поле</b>, тому перевіряється при відкритті, а не приходить із моменту генерації. Єдиний екран набору з живим запитом у нормальному режимі.')
        z += zone('back','Дорога назад','''      <p>Чекає на перевірку.</p>''','Зона на місці, вміст ще не прийшов.')
        z += zone('alt','Якщо щось піде не так','''      <p>Альтернативні виходи відомі з кешу — вони не залежать від сьогоднішнього статусу.</p>''',
      'Показуємо те, що не залежить від запиту: це і є різниця між «завантаження» і «порожньо».')
    elif state == 'empty':
        z = zone('there','Дорога туди','''      <div class="verdict">
        <strong>У ці дати сюди нічим не дістатись.</strong>
        <p>16 серпня рух на ділянці Kiruna — Abisko скасовано: ремонт колії. Замінних автобусів немає, бо частина станцій не має дороги.</p>
      </div>
      <p>Це не «нічого не знайдено» — це відповідь, яка міняє рішення: маршрут лишається, дістатись до нього в ці дати не можна.</p>
      <ul class="signals">
        <li><b>Варіант 1</b> Виїхати 15 серпня — останній потяг перед ремонтом</li>
        <li><b>Варіант 2</b> Почати з Nikkaluokta й пройти маршрут навпаки — туди йде автобус</li>
        <li><b>Варіант 3</b> Зрушити похід на тиждень: з 24 серпня рух відновлюється</li>
      </ul>
      <p class="actions">
        <form action="./plan-loading.html" method="get" style="display:inline"><button type="submit">Виїхати 15-го</button></form><form action="./plan-loading.html" method="get" style="display:inline"><button type="submit">Пройти навпаки</button></form><form action="./plan-loading.html" method="get" style="display:inline"><button type="submit">Зрушити на тиждень</button></form>
      </p>''',
      'Порожній стан. <b>Найсильніша доказова база всього дослідження</b> стоїть саме тут: троє шведів за тиждень, один покинув регіон через транспорт, і випадок Katterat. Виходи готові — правило рішення №12.')
        z += zone('back','Дорога назад','''      <p>Зворотний шлях із Nikkaluokta працює: автобус 91 ходить щодня.</p>''',
      'Показуємо, що вціліло: зламане плече — одне, а не обидва.')
        z += zone('alt','Якщо щось піде не так','''      <p>При варіанті «навпаки» точки сходу теж міняються місцями — Vakkotavare стане доступним на другий день, а не на четвертий.</p>''',
      'Наслідок вибору названий одразу, а не після перегенерації.')
    else:
        z = zone('there','Дорога туди','''      <div class="verdict" role="alert">
        <strong>Розклад недоступний, і кешу теж немає.</strong>
        <p>Trafikverket не відповідає, а цей маршрут ви відкриваєте вперше — тож і показати з памʼяті нема чого.</p>
      </div>
      <p><b>Чого ми не робимо:</b> не показуємо торішній розклад як сьогоднішній. Потяг, якого немає, гірший за відсутність відповіді.</p>
      <p class="actions">
        <form action="./map.html" method="get" style="display:inline"><button type="submit">Спробувати ще раз</button></form>
        <a href="./plan.html">Повернутись до плану</a>
      </p>''',
      'Помилка — <b>вузька гілка</b>: якщо кеш є, це вже offline, а не помилка. Тому в тексті сказано саме «і кешу теж немає».')
        z += zone('back','Дорога назад','''      <p>Те саме джерело — теж недоступне.</p>''','Без вигадок про те, чого не знаємо.')
        z += zone('alt','Якщо щось піде не так','''      <ul class="signals">
        <li><b>Дорожній доступ</b> відомий і без розкладу: він із NVDB, а це інше джерело, і воно відповідає</li>
        <li><b>Katterat</b> дороги немає — цей факт не залежить від сьогоднішнього розкладу</li>
      </ul>''',
      'Різні джерела ламаються окремо. Дорожній доступ це <b>NVDB</b>, а не розклад — тому в цьому стані він працює.')
    return page(cur, f'Wireframe · B6 Транспорт · {state}','Дорога туди й назад',
      R(f'wireframes/{cur} — <b>B6 Транспорт</b> · стан <b>{state}</b>',
        '<code>B1</code> → <code>B6</code>. Інлайн першим і останнім елементом списку днів — не в меню.',
        'Job — <b>R6</b>, найсильніша свіжа доказова база дослідження. Транспорт не став пунктом глобальної навігації свідомо: <b>сила доказу ≠ частота доступу</b>, вимога інша — його має бути неможливо пропустити.'),
      z, 'Розклад і статус: Trafikverket. Дорожній доступ: NVDB (окреме джерело — ламається окремо).',
      base='transport.html')

for st,f in (('ok','transport.html'),('empty','transport-empty.html'),('error','transport-error.html'),('loading','transport-loading.html')):
    P[f] = transport(st)

# ══ ЗАПИС ═════════════════════════════════════════════════════
for f, html in P.items():
    (W/f).write_text(html, encoding='utf-8')
print(f'створено сторінок: {len(P)}')

# оновлюємо дерево в уже наявних plan*.html
for f in ('plan.html','plan-empty.html','plan-error.html','plan-loading.html'):
    p = W/f; s = p.read_text(encoding='utf-8')
    s = re.sub(r'<nav class="wf-tree".*?</nav>', nav_html(f), s, flags=re.S)
    p.write_text(s, encoding='utf-8')
print('дерево оновлено в 4 наявних сторінках')
