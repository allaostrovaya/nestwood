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
| `googlemaps--consent-access-limited--mobile.png` | https://www.google.com/maps | Аспіраційний | екран |

## Бенчмарк ([`../benchmark.md`](../benchmark.md))

| Файл | URL | Роль | Кадр |
|---|---|---|---|
| `expedia--bundle-search--mobile.png` | https://www.expedia.com/Vacation-Packages | Bundle-чекаут | екран |
| `omio--multimodal-search--mobile.png` | https://www.omio.com/ | Мультимодальна агрегація | екран |
| `gadventures--tour-bundle--mobile.png` | https://www.gadventures.com/ | Парасолькова гарантія | екран |
| `reitravel--tour-bundle--mobile.png` | https://www.rei.com/travel | Той самий патерн, довідково | екран |

## Відомі обмеження цих скрінів

**Доступ обмежений.** `googlemaps--consent-access-limited--mobile.png` — знято лише публічний cookie-консент. Глибший шар Trips/Layers за акаунтом Google, доступу немає.

**Неправильна локаль — потребує перезняття.** Чотири сайти автоматично редіректнули на локалізовані версії, бо браузер геолокований поза цільовим ринком. Скріни показують не той вигляд продукту, який бачить наша аудиторія:

| Файл | Фактичний URL після редіректу | Проблема |
|---|---|---|
| `airbnb--home-search--mobile.png` | `uk.airbnb.com` | українська локаль |
| `getyourguide--home-search--mobile.png` | `getyourguide.com/uk-ua/` | українська локаль |
| `bookingcom--home-search--mobile.png` | `booking.com/index.uk.html` | українська локаль |
| `googlemaps--consent-access-limited--mobile.png` | `consent.google.com/...gl=HR&hl=uk` | хорватське гео + українська локаль |

**Глибина.** Усі скріни — вхідні/головні сторінки. Реальні флоу (пошук → лістинг → чекаут) не проходились, тому механізми, заявлені в таблицях аудиту (instant book, структура зручностей, підтвердження бронювання), цими скрінами **не підтверджені** — вони фіксують лише факт відвідування продукту.
