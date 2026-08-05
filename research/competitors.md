# Конкурентний аудит — деталі (Крок 3)

Повний список 15 конкурентів у трьох групах з поясненнями та джерелами. Синтез (матриця, спільні патерни, PM-рішення) — у [research.md](./research.md); деталі глибокого benchmark'у пʼятьох Хард-конкурентів і 5 UX-патернів — у [benchmark.md](./benchmark.md) та [patterns.md](./patterns.md).

Критерій добору групи — не бренд-впізнаваність, а те, яку саме частину задачі Nestwood ("вхід: фіз. підготовка, бюджет, час, спорядження, уподобання → вихід: маршрут + ночівлі + gear-checklist + погодна адаптація, на відкритих даних Nordic") продукт закриває і для кого.

## 1. Хард — той самий продукт, та сама аудиторія, ринок Скандинавія

| Компанія | Чому в цій групі | Що вивчити для нашої задачі | Джерела |
|---|---|---|---|
| **UT.no (DNT)** | Офіційний сайт/застосунок Норвезької трекінгової асоціації — та сама аудиторія, той самий регіон, той самий use case (маршрут + хижі DNT). Один із наших власних acquisition-таргетів. | Як вони моделюють звʼязок "маршрут ↔ хижа" (opening dates, ключі, bed availability); чому бронювання досі не онлайн для частини хиж. | [UT.no — Wikipedia](https://en.wikipedia.org/wiki/UT.no), [DNT cabin booking](https://www.dnt.no/en/Cabins/About-the-DNT-cabins/DNT-cabin-booking/); скріни [ut-no-home.png](./screens/ut-no-home.png), [ut-no-kart-planner.png](./screens/ut-no-kart-planner.png), [ut-no-dnt-hyttebestilling-landing.png](./screens/ut-no-dnt-hyttebestilling-landing.png), [ut-no-dnt-hyttebestilling-search.png](./screens/ut-no-dnt-hyttebestilling-search.png) |
| **STF (Svenska Turistföreningen)** | Точніший шведський аналог DNT, ніж Naturkartan (розглядали й відхилили — це просто trail/nature discovery без власної хижа-мережі): STF безпосередньо оперує 16 гірськими хижами на Kungsleden з відстанню 10–20 км одна від одної. | Модель "no-booking, guaranteed floor space" — інший підхід до надійності ночівлі, ніж у DNT. | [Swedish Tourist Association — Wikipedia](https://en.wikipedia.org/wiki/Swedish_Tourist_Association), [STF huts explained](https://thehikershandbook.com/stf-huts-all-you-need-to-know/); скріни [stf-home.png](./screens/stf-home.png), [stf-mountain-station-info.png](./screens/stf-mountain-station-info.png), [stf-booking-landing.png](./screens/stf-booking-landing.png) |
| **Komoot** | Величезна органічна аудиторія в Nordic outdoor-спільноті; єдиний з "хард"-групи, хто вже публічно рухається в AI-напрямку (лютий 2026 — komoot-застосунок для ChatGPT з natural-language пошуком маршрутів). Acquisition-таргет. | Чому їхній ChatGPT-шар лише **рекомендує з готової бази** (7М маршрутів), а не **генерує** нову multi-day-послідовність. | [Komoot newsroom — ChatGPT app](https://newsroom.komoot.com/261872-komoot-makes-outdoor-adventures-accessible-with-ai-powered-route-discovery-on-chatgpt/), [Komoot — Plan multi-day routes](https://support.komoot.com/hc/en-us/articles/10269672250266-Plan-multi-day-routes); скріни [komoot-home.png](./screens/komoot-home.png), [komoot-planner.png](./screens/komoot-planner.png) |
| **AllTrails** | Глобальний трейл-застосунок з великою Nordic-базою користувачів; на 2026 рік — AI Smart Routing (тар Peak) + інтеграція з Claude/ChatGPT. Acquisition-таргет. | Точна межа AI-фічсету (один трек, один день); SAR-фахівці публічно критикують AI Smart Routing за "надмірну довіру" користувачів без перевірки. | [T3 — AllTrails × Claude](https://www.t3.com/active/outdoors/alltrails-in-claude-launch-anthropic-0426), [Canada's National Observer — SAR concerns](https://www.nationalobserver.com/2025/06/17/news/alltrails-ai-tool-search-rescue-members), [Globetrender — AllTrails Peak](https://globetrender.com/2025/07/28/alltrails-new-premium-membership-delivers-ai-powered-hikes/); скріни [alltrails-home.png](./screens/alltrails-home.png), [alltrails-norway-trail-list.png](./screens/alltrails-norway-trail-list.png) |
| **Outdooractive** | Європейський (німецький) hut-to-hut планувальник з базою 33 000+ хиж. Має власний AI-асистент (White-Label Website AI Assistant, тестують партнери напр. Heidiland Tourismus) — це AI для travel-контенту дестинації, не для персоналізованого multi-day плану користувача. | Структура "hut finder" (доступ, transitions, weather-at-hut); бізнес-інсайт — білейбл під alpenvereinaktiv.com (DAV/ÖAV/AVS) — живий прецедент ліцензування нац. асоціації. | [Outdooractive huts](https://www.outdooractive.com/en/huts/), [Outdooractive Tourism AI — corporate press](https://corporate.outdooractive.com/presse/outdooractive-tourism-ai-immer-mehr-destinationen-setzen-auf-vollstaendig-integrierten-ki-assistenten/); alpenvereinaktiv як білейбл Outdooractive — package `com.outdooractive.alpenverein` на [Google Play listing](https://play.google.com/store/apps/details/alpenvereinaktiv?id=com.outdooractive.alpenverein); скріни [outdooractive-home.png](./screens/outdooractive-home.png), [outdooractive-huts-finder.png](./screens/outdooractive-huts-finder.png) |

## 2. Софт — інший продукт, та сама базова задача

Не трекінг-специфічні, але вирішують той самий job-to-be-done "з розрізнених джерел зібрати повний multi-day outdoor trip" — для іншої активності, географії або лише одного шматка задачі. Група навмисно глобальна (це ринкове обмеження стосується лише Хард-групи).

| Компанія | Чому в цій групі | Що вивчити для нашої задачі | Джерела |
|---|---|---|---|
| **Gaia GPS** (США) | Backcountry multi-day навігація й трек-планування — та сама фіз. активність, інша географія, акцент на navigation-in-the-field, не генерацію плану заздалегідь. | "Contingency routes" — паттерн для погодної адаптації дня; відсутність gear/hut-логіки підтверджує невирішеність цього шматка. | [Backpacker — Gaia GPS review](https://www.backpacker.com/gear/outdoor-electronics/gps-units/gaia-gps-one-backcountry-navigation-app-to-rule-them-all/), [TrailGroove — Gaia GPS guide](https://www.trailgroove.com/blogs/entry/122-how-to-use-the-gaia-gps-app-and-trip-planning-guide/) |
| **PiNCAMP** (Швейцарія/Німеччина/Нідерланди — TCS/ADAC/ANWB) | Пан-європейський маркетплейс бронювання кемпінгів (5 800+ інспектованих сайтів) — вирішує ночівлю, як DNT-хижі в Nestwood, без маршруту. | Модель довіри через фізичну інспекцію сайтів + real-time availability. | [PiNCAMP for business](https://business.pincamp.com/), [PiNCAMP](https://www.pincamp.com/) |
| **WikiCamps** (Австралія/Нова Зеландія) | Trip planner для кемпінгу з маршрутом, витратами на паливо й прямим бронюванням 4000+ сайтів — та сама структура задачі, для авто, в іншому регіоні світу. | Модель "маршрут + список сайтів + офлайн-режим"; монетизація одноразовою покупкою без підписки. | [WikiCamps Australia](https://www.wikicamps.com.au/site) |
| **Wanderlog** | Загальний AI-трипланер, глобально використовується — той самий "вхід → повний multi-day itinerary" паттерн без outdoor-специфіки. | Чому AI визнано "менш конкретним" за конкурентів — застереження на користь grounding на вузьких даних. | [Voyaige — Best AI Travel Planner 2026](https://voyaige.to/blog/best-ai-travel-planner-2026), [Faroway — AI Travel Planner vs Wanderlog](https://www.faroway.ai/blog/ai-travel-planner-vs-wanderlog) |
| **PackPoint** | Закриває рівно один шматок задачі — gear-checklist під погоду й тип активності, без маршруту й ночівлі. | Логіка генерації списку спорядження з погоди + тривалості + типу активності. | [PackPoint](https://www.packpnt.com/), [PackPoint review](https://thoughtcard.com/packpoint-review/) |

Розглянуто й відхилено (замінені на глобальніші аналоги): **Hipcamp** (США) → замінено на PiNCAMP; **The Dyrt** (США, RV) → замінено на WikiCamps; **iOverlander** (глобальний, community-модерований пошук стоянок для оверлендерів) — розглянуто, але дублює PiNCAMP/WikiCamps функціонально, без нового уроку.

## 3. Аспіраційні — міжнародні еталони

Не прямі конкуренти й не завжди про трекінг — задають продуктову/технічну стелю. Група навмисно міжнародна.

| Компанія | Чому в цій групі | Що вивчити для нашої задачі | Джерела |
|---|---|---|---|
| **onX Backcountry** (США) | Продуктова стеля US backcountry-ринку: route builder зі snap-to-trail, 3D-рельєф, waypoints під кемпспоти, погода в потоці планування. | Як зшивають маршрут+waypoints+погоду в одному екрані без відчуття "трьох інструментів". | [onX Backcountry features](https://www.onxmaps.com/backcountry/app/features), [onX Route Builder announcement](https://www.onxmaps.com/blog/onx-backcountry-unveils-route-builder-tool) |
| **FarOut** (США) | Гайди для thru-hiking/бекпекінгу з waypoint-навігацією "скільки до води/кемпспоту/resupply". | Як подають "день переходу" через відстань до наступної точки — модель для розбивки маршруту Nestwood на дні. | [The Trek — best hiking navigation apps 2026](https://thetrek.co/best-hiking-navigation-apps-of-2026/). **Дані не підтверджені**: покриття міжнародних маршрутів (Te Araroa/Camino de Santiago/GR20) не було окремо перевірено пошуком у цьому дослідженні — це з загальних знань про бренд, не з джерела вище; потребує перевірки перед використанням у пітчі. |
| **DOC Great Walks booking** (Нова Зеландія) | Державна трекінгова агенція (аналог DNT в Океанії) із системою бронювання на "concert-ticket"-паттерні; ~100 000 бронювань/сезон, 35% — іноземці. | Архітектура lobby/queue-системи під пікові дати відкриття бронювань. | [DOC — Ready, set, naturing media release](https://www.doc.govt.nz/news/media-releases/2026-media-releases/ready-set-naturing-doc-great-walk-hut-and-campsite-bookings-open-from-12-may/), [DOC blog — guide to booking](https://blog.doc.govt.nz/2026/05/10/your-guide-to-booking-a-great-walk/) |
| **YAMAP** (Японія) | Домінує в хайкінг-категорії Японії — GPS-трекінг офлайн, соціальний шар, погода й emergency-beacon у потоці планування. | Як emergency/safety-шар вбудований у звичайний flow, не окремий SOS-екран. | [Rexby — Route Planning with YAMAP](https://www.rexby.com/YamaTrips.Japan/t/route-planning-and-real-time-pathfinding-with-yamap), [emgoto — YAMAP guide](https://www.emgoto.com/yamap-guide/) |
| **Google Gemini / Travel Concierge** | Явний паттерн-референс з CLAUDE.md: conversational multi-agent AI з grounding через Maps Platform Places API + Search Grounding + MCP. | Архітектура grounding-агента — калька на grounding Nestwood над Kartverket/Lantmäteriet/UT.no. | [Google — Travel Concierge sample](https://developers.google.com/workspace/add-ons/samples/travel-concierge), [Google Maps Platform — agentic grounding](https://mapsplatform.google.com/resources/blog/powering-the-next-era-of-agentic-experiences-announcing-new-grounding-capabilities/) |

Розглянуто й відхилено: **Strava** (спадщина FATMAP-рельєфу) — фітнес-трекінг з рельєфною візуалізацією як побічною фічею; **Roadtrippers Autopilot** — авто-роадтрип у США, база активності розходиться з Nestwood (мех mechanіка описана й перенесена окремо в [patterns.md](./patterns.md)); **CalTopo** та **REI Co-op/REI Adventures** (обидва США) — якісні, але звужені до одного ринку, витіснені DOC Great Walks і YAMAP для географічного балансу.

## Зведена таблиця — усі 15 конкурентів

"AI-асистент" тут означає conversational/generative AI-шар (не rule-based персоналізацію типу фільтрів чи анкет) — перевірено пошуком по кожному окремо, липень–серпень 2026.

| Компанія | Група | Країна | Що це за застосунок (коротко) | AI-асистент? |
|---|---|---|---|---|
| UT.no (DNT) | Хард | Норвегія | Держ. сайт/апка маршрутів + хиж DNT | Ні |
| STF (Svenska Turistföreningen) | Хард | Швеція | Мережа гірських хиж + трекінг | Ні |
| Komoot | Хард | Німеччина | Route-планувальник (піші/вело/біг) | **Так** — ChatGPT-застосунок (рекомендує з бази, не генерує) |
| AllTrails | Хард | США | Трейл-застосунок для пошуку й навігації | **Так** — AI Smart Routing + Claude/ChatGPT (тар Peak) |
| Outdooractive | Хард | Німеччина | Hut-to-hut multi-day route-планувальник | **Так** — White-label AI для дестинацій (inspiration-контент, не персоналізований план) |
| Gaia GPS | Софт | США | Backcountry-навігація й трек-планування | Ні |
| PiNCAMP | Софт | Швейцарія/Німеччина/Нідерланди | Маркетплейс бронювання кемпінгів (Європа) | Ні |
| WikiCamps | Софт | Австралія/Нова Зеландія | Кемпінг-трипланер з бронюванням | Ні |
| Wanderlog | Софт | США | Загальний трипланер для будь-яких подорожей | **Так** — генеративний AI-шар над мапою (визнано "generic") |
| PackPoint | Софт | США | Gear-checklist під погоду й тип активності | Ні (правило-based логіка, не AI) |
| onX Backcountry | Аспіраційні | США | Premium backcountry route-builder + 3D-рельєф | Ні |
| FarOut | Аспіраційні | США (покриття міжнародне — дані не підтверджені) | Waypoint-гайди для thru-hiking | Ні |
| DOC Great Walks booking | Аспіраційні | Нова Зеландія | Держ. система бронювання хиж/треків | Ні |
| YAMAP | Аспіраційні | Японія | Соціальний хайкінг-застосунок з GPS | Ні |
| Google Gemini / Travel Concierge | Аспіраційні | США | Conversational AI travel-агент з grounding | **Так** — це і є продукт |

**Що це показує без слів**: з 15 продуктів лише 4 мають хоч якийсь AI-шар, і жоден з них не генерує персоналізований multi-day-план (маршрут + ночівля + gear + погода). Це gap, на якому будується Nestwood — синтез у [research.md](./research.md).
