# Реєстр скріншотів

> Папка `research/screens/` · Кореневий індекс репо — [`../../README.md`](../../README.md)

Зібрано через Playwright, mobile viewport 390×844, дата збору 2026-08-03. У колонці «Кадр»: `повна` — скрін усієї сторінки (`fullPage`), `екран` — тільки видима область (для важких сторінок, де повний скрін падав по таймауту).

## Аудит конкурентів ([`../audit.md`](../audit.md))

| Файл | URL | Група | Кадр |
|---|---|---|---|
| `stf--home-search--mobile.png` | https://www.svenskaturistforeningen.se/ | Хард | повна |
| `naturkartan--home-search--mobile.png` | https://naturkartan.se/en | Хард | повна |
| `outdooractive--home-search--mobile.png` | https://www.outdooractive.com/en/ | Хард | повна |
| `hipcamp--home-search--mobile.png` | https://www.hipcamp.com/en-US | Хард | повна |
| `campingse--home-search--mobile.png` | https://www.camping.se/en | Хард | повна |
| `komoot--home-search--mobile.png` | https://www.komoot.com/ | Софт | повна |
| `alltrails--home-search--mobile.png` | https://www.alltrails.com/ | Софт | екран |
| `park4night--home-search--mobile.png` | https://park4night.com/en | Софт | повна |
| `airbnb--home-search--mobile.png` | https://www.airbnb.com/ | Софт | екран |
| `getyourguide--home-search--mobile.png` | https://www.getyourguide.com/ | Софт | екран |
| `roadtrippers--home-search--mobile.png` | https://roadtrippers.com/ | Аспіраційний | повна |
| `wanderlog--home-search--mobile.png` | https://wanderlog.com/ | Аспіраційний | повна |
| `tripit--home-search--mobile.png` | https://www.tripit.com/ | Аспіраційний | повна |
| `bookingcom--home-search--mobile.png` | https://www.booking.com/ | Аспіраційний | екран |
| `googlemaps--map-layers--mobile.png` | https://www.google.com/maps?hl=en | Аспіраційний | екран |

## Бенчмарк ([`../benchmark.md`](../benchmark.md))

| Файл | URL | Роль | Кадр |
|---|---|---|---|
| `expedia--bundle-search--mobile.png` | https://www.expedia.com/Vacation-Packages | Bundle-чекаут | екран |
| `omio--multimodal-search--mobile.png` | https://www.omio.com/ | Мультимодальна агрегація | екран |
| `gadventures--tour-bundle--mobile.png` | https://www.gadventures.com/ | Парасолькова гарантія | екран |
| `reitravel--tour-bundle--mobile.png` | https://www.rei.com/travel | Той самий патерн, довідково | екран |

## Відомі обмеження цих скрінів

**Локаль — виправлено 2026-08-03.** Чотири сайти спершу автоматично редіректнули на українські локалі (`uk.airbnb.com`, `/uk-ua/`, `index.uk.html`, `hl=uk`), бо браузер геолокований поза цільовим ринком. Перезняті з англійською локаллю, яка й є нашою лінзою за `CLAUDE.md` §6 (мова v1 — англійська, аудиторія — міжнародні туристи):

| Файл | URL перезняття | Як домоглися |
|---|---|---|
| `airbnb--home-search--mobile.png` | `airbnb.com/?locale=en` | параметр локалі + закрито cookie-модалку («Only necessary») |
| `getyourguide--home-search--mobile.png` | `getyourguide.com/en-gb/` | очищені куки локалі, бо сайт запамʼятовував попередній вибір; закрито банер («Only essential») |
| `bookingcom--home-search--mobile.png` | `booking.com/index.en-gb.html?lang=en-gb&selected_currency=EUR` | явна локаль + валюта; закрито панель («Decline») |
| `googlemaps--map-layers--mobile.png` | `google.com/maps?hl=en` | `hl=en` + пройдено консент («Reject all»), тому замість cookie-стіни тепер знята сама карта |

**Гео лишається хорватським — зняти не вдалося.** Мову інтерфейсу нав'язати можна, а IP-геолокацію без проксі — ні. Тому регіональні дефолти в цих скрінах не наші: Airbnb рекомендує Любляну/Спліт/Будапешт, Google Maps центрує карту на Загребі. На механізми, які ми цитуємо (структура картки, бейджі довіри, шари над картою), це не впливає, але як вигляд шведського ринку ці скріни читати не можна.

**Доступ обмежений.** У Google Maps персоналізований шар (збережені місця, Trips) за акаунтом Google — не знімався. Публічна карта з категорійними чіпами, погодою, трафіком і кнопкою Layers доступна й знята.

**Глибина — головне обмеження всієї вибірки.** Усі 19 скрінів — вхідні/головні сторінки. Реальні флоу (пошук → лістинг → чекаут) не проходились, тому механізми, заявлені в таблицях аудиту (instant book, структура зручностей, підтвердження бронювання), цими скрінами **не підтверджені** — вони фіксують факт відвідування продукту й вигляд входу, не роботу механізму.
