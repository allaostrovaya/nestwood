# Інвентар UI — увесь продукт

Складено 2026-09-24 з розмітки всіх 33 сторінок `wireframes/*.html` (лише те, що всередині телефона; дерево, рядок позиції й документна навігація — рев'ю-хром, їх тут немає) і з [sitemap.md](../wireframes/sitemap.md). Покриває **всі 20 екранів** — і п'ять пофарбованих мовою «Прилад», і сірі вайрфрейми.

**Правило відбору.** У таблицю потрапляє компонент, що стоїть на **двох і більше різних екранах**. Сторінки станів (`-empty`, `-error`, `-loading`, `-offline`, `-conflict`, `-seasonal`, `-intrip`, `-past`) — це той самий екран, тож окремими екранами не рахуються й вказані в дужках. Одиничні блоки — у списку «Разове» внизу.

**Колонка «Фото»** — чи потрібне компоненту зображення. «Так» — фото з автором і ліцензією на самому знімку (sitemap, сутність 21: «кожне фото несе джерело й ліцензію на самому знімку»). «Карта» — картографічна підкладка, не фото.

Екрани — назви з `TREE`: Where to go (`catalogue`), New plan (`new-plan`), Another hut (`huts`), Hut (`hut`), Notes and reviews (`notes`), My trips (`plans`), Plan (`plan`), Day (`day`), Book (`booking`), Gear (`gear`), Share my route (`share`), Guide (`guide`), Article (`lodging-system`), Safety (`safety`), First aid (`first-aid`), Profile (`me`), My gear (`my-gear`), Membership and key (`membership`), Settings (`settings`), Sign in (`account`).

---

## Навігація

| Компонент | Де зустрічається | Стани | Фото |
|---|---|---|---|
| **Таб-бар** — 5 вкладок Map · Plans · Guide · Safety · Profile | усі 20 екранів (приховано на New plan і Another hut — модальне й аркуш) | активна вкладка — одна з п'яти (за вкладкою екрана) | ні |
| **Бейдж на вкладці Plans** — лічильник «4» | 19 екранів: усі, крім New plan — Where to go, Another hut, Hut, Notes and reviews, My trips, Plan, Day, Book, Gear, Share my route, Guide, Article, Safety, First aid, Profile, My gear, Membership and key, Settings, Sign in | є / немає — знімається там, де плану ще немає (`catalogue-empty`, `plans-empty`, усі стани New plan) | ні |
| **Шапка з «назад»** — посилання на батьківський екран + назва екрана | 8 екранів: New plan (+ loading, conflict, error), Plan (+ past, error, offline), Day (+ seasonal, intrip, offline), Gear, Share my route, Article, First aid, Settings | підпис «назад» = назва батька (Where to go, My trips, Plan, Guide, Safety, Profile); на фото — скляна кнопка, без фото — посилання | ні (але на Plan / New plan лежить на фото-героєві) |
| **Шапка аркуша з «Close»** — закриває й повертає туди, звідки відкрили | 7 екранів: Another hut (+ empty), Hut, Notes and reviews (+ empty), Book, Membership and key, My gear, Sign in | — | ні |
| **Заголовок екрана** (h1) | усі 20 екранів | назва обʼєкта («Kungsleden · Abisko → Nikkaluokta», «Day 3 · Wed 19 August») або назва екрана | ні |
| **Футер атрибуції** — ©Kartverket · Lantmäteriet · met.no · Trafikverket, розкривач «Where this comes from», «Last checked» | усі 20 екранів | розкривач закритий / відкритий; текст джерел різний на кожному екрані | ні |

## Картки й списки

| Компонент | Де зустрічається | Стани | Фото |
|---|---|---|---|
| **Секція із заголовком** (h2 + вміст) | усі 20 екранів | — | ні |
| **Рядок списку** — назва + підпис, у згрупованому списку | 19 екранів — усі, крім Sign in | посилання з шевроном · статичний (без шеврона) · зі станом праворуч · зі станом «увага» праворуч | ні |
| **Стан у рядку** — слово праворуч («bookable», «walk-in only», «4.3», «6 routes», «4 of 6») | 7 екранів: Where to go (+ empty), New plan (+ loading, conflict), Another hut, Notes and reviews, My trips, Day (+ seasonal, offline), Guide | звичайний (нейтральна пігулка) | ні |
| **Стан «увага» в рядку** — «1 missing», «flood», «book», «by 18:00», «~9 h», «none», «buy», «day 2» | 9 екранів: New plan (+ conflict), Another hut, Notes and reviews, Plan (+ error, offline), Day (+ seasonal, intrip, offline), Book, Gear, Membership and key, My gear | тривога (чорна пігулка з жовтою іконкою) · дія над своєю сутністю («book», «buy» → Book) | ні |
| **Рядок-перемикач** — назва + підпис + checkbox | 2 екрани: Gear (чеклист), Settings (перемикачі) | увімкнено / вимкнено; у Gear ще «увага» «buy» | ні |
| **Рядок брифу** — «17–22 August · 2 people · 1 STF member» + примітка | 2 екрани: New plan, Plan (+ past, error, offline) | посилання «change» (New plan) · статичний зі статусом офлайну (Plan: «available offline» / «offline pack from 14 Aug») | ні (на Plan статус лежить на фото) |
| **Список днів** — дорога туди, дні 1–6, дорога назад | 2 екрани: New plan (+ conflict), Plan (+ past, error, offline) | день-посилання · день зі станом «увага» · задача бронювання («book», «buy» → Book) · транспорт без переходу · пройдений (без станів, `plan-past`) | ні |
| **Картка з фото** — фото + назва + стан + підпис | 2 екрани: Where to go (пресети), My trips (найближчий похід) | зі станом тривалості («6 days» / «in 4 days») | **так** |
| **Фото-герой** — зображення на всю ширину у верху екрана | 3 екрани: New plan (+ conflict, error), Plan (+ past, error, offline), Hut | звичайний · на New plan loading — скелет на його місці | **так** |
| **Рамка карти** — карта маршруту або дня | 3 екрани: New plan (+ conflict), Plan (+ past, error, offline), Day (+ seasonal, intrip, offline) | звичайна · з офлайн-пакета (`plan-offline`, `day-offline`) · «ти тут» (`day-intrip`) | карта |
| **Виміри** — ряд чисел із підписами (km, m, days, h, «to go», «arrive by») | 3 екрани: New plan (+ conflict), Plan (+ past, error, offline), Day (+ seasonal, intrip, offline) | 4 числа (Plan, New plan) · 3 числа (Day) · у поході (`day-intrip`: to go · walking · arrive by) | ні (на Plan / New plan лежить на фото) |
| **Порожній стан** — речення про те, чого немає | 4 екрани: Another hut (`huts-empty`), New plan (`new-plan-error`), Notes and reviews (`notes-empty`), My trips (`plans-empty`) | з виходами рядками (Another hut) · з головною кнопкою (My trips) · без виходу в межах секції (New plan error, Notes) | ні |

## Форми й дії

| Компонент | Де зустрічається | Стани | Фото |
|---|---|---|---|
| **Головна кнопка** — одна на екран | 9 екранів: Where to go («Make a plan»; empty — «Pick dates in June — September»), New plan («Save plan»), Hut («Stay here on night 4»), My trips (empty — «Where to go»), Book («Open STF booking»), Share my route («Send»), Sign in («Continue with Apple»), Day / Safety (SOS) | звичайна · **недоступна** («Choose one of the options», `new-plan-conflict`) · **SOS · 112** (Day intrip, Safety) | ні |
| **Вторинна кнопка / дія** | 14 екранів: Where to go («Clear points»), New plan («Cancel»), Plan («Share my route»), Day intrip («Write a field note»), Safety («Share my route»), First aid («SOS and coordinates»), Gear («Open inventory»), Book («Save»), Notes and reviews («Send»), Share my route («Copy link», «PDF»), Profile («Import from Strava / Garmin»), Membership and key («Show card», «Renew at STF»), Sign in («Continue with Google», «Continue without signing in»), Settings («Sign out») | звичайна; на Plan past — «Plan again from this trip» стає головною | ні |
| **«Try again»** — повтор після помилки | 2 екрани: New plan (`new-plan-error`), Plan (`plan-error`) | — | ні |
| **Небезпечна дія** | 2 екрани: Plan («Change and reset», у розкривачі «Change plan»), Settings («Delete account») | — | ні |
| **Розкривач** (details / summary) | усі 20 екранів (футер «Where this comes from») + Plan («Change plan») | закритий / відкритий | ні |
| **Чипи** — вибір значення | 4 екрани: Where to go (huts · tent), Guide (Norway · Sweden · Both), Another hut (фільтри), Notes and reviews (trail · water · ford · snow · waymarks · tent spot) | вибраний / невибраний; кілька вибраних одночасно (Another hut) | ні |
| **Текстове поле з підписом** | 3 екрани: Book («Booking number»), Notes and reviews («What's on this section right now»), Sign in («Email») | порожнє з плейсхолдером | ні |
| **Форма з кнопкою надсилання** | 6 екранів: New plan («Save plan», «Try again»), Plan («Try again»), Book («Save»), Notes and reviews («Send»), Sign in, Guide (пошук) | — | ні |

---

## Разове — у кіт не тягнемо

Стоїть лише на одному екрані (разом із його станами):

- **Пошук «Where · When · Who»** — три рядки брифу згори каталогу — Where to go.
- **Карта на весь екран** під пошуком, зі своїм маршрутом і картками пресетів поверх — Where to go (+ empty).
- **Тривога «Needs attention»** — рядок тривоги рівня походу — Plan.
- **Межа знання** — абзац «No connection / Couldn't update. Data from…» — Plan (`plan-error`, `plan-offline`).
- **Підсумок пройденого** — «Walked 17–22 August 2025.» — Plan (`plan-past`).
- **Вердикт** — «4 days don't fit this route» / «Couldn't build the plan» з варіантами виходу — New plan (`new-plan-conflict`, `new-plan-error`).
- **«Everything fits.»** — стан плану одним словом — New plan.
- **Скелет генерації** — New plan (`new-plan-loading`).
- **Профіль висоти** — Day (+ seasonal, offline).
- **Сегментований перемикач** «Field notes · Reviews» — Notes and reviews (+ empty).
- **Поле пошуку** «Word, hut or rule» — Guide.
- **Поле файлу** «Confirmation or ticket — photo or PDF» — Book.
- **Порядок ланцюжка бронювань** (1 · 2 · 3 з «next») — Book.
- **Шестерня налаштувань у шапці** — Profile.
- **Секція акаунта** — email, спосіб входу — Settings.

---

**Що помітно з таблиці.** Найширші компоненти — таб-бар, шапки, рядок списку, футер атрибуції й розкривач: вони на всіх 20 екранах, тож з них і починати кіт. Фото потрібне лише двом компонентам — фото-герою (3 екрани) і картці з фото (2 екрани); решта продукту — реєстр без зображень, що збігається з рішенням concept.md «каталог фото-центричний, план — реєстр». Карта потрібна трьом екранам у рамці й одному — на весь екран.
