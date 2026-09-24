# microcopy.md — увесь текст інтерфейсу Nestwood

**33 екранів · 1244 рядків тексту · 473 унікальних.** Це перепис того, що зараз написано в макетах, без жодної правки. До кінця роботи над флоу він має стати таблицею, з якою звіряється кожен рядок продукту.

## Як це зібрано

Витягнуто скриптом із `wireframes/*.html` — **тільки те, що всередині `.device`**. Дерево навігації, глобальна навігація по документах і рядок позиції над макетом це рев'ю-хром, а не інтерфейс продукту, тому їх тут немає. `ia.html` і `flow.html` — документи, не екрани, теж поза.

**Тип рядка** визначено за розміткою, а не на око: `h1` → заголовок екрана, `h2` → заголовок зони, `button`/`a.cta` → кнопка, `label`/`dt` → підпис поля, `.verdict` → повідомлення стану, `small[data-mock]` → позначка мок-даних, `.frame > span` → заглушка макета, `span.state` → індикатор.

**Зона** — це заголовок `h2` тієї секції, у якій рядок стоїть. Там, де зони немає (шапка, футер, таббар, `h1` над секціями), стоїть назва області або `—`.

⚠️ **Тут нічого не переписано.** Колонка «Позначки» лише вказує на розбіжність; що з нею робити — окреме рішення, і воно ще не ухвалене.

**Правила, з якими це звіряється**, — [../design-system/voice.md](../design-system/voice.md): пʼять принципів голосу, кожен виведений з рядка в дослідженні. Ця таблиця — інвентар, voice.md — правила; розбіжність `plan` / `trip` не розвʼязується жодним із них і лишається питанням глосарія.

## Словник позначок

| Код | Що означає |
|---|---|
| `С1` | той самий обʼєкт: **«trek», «journey», «itinerary»** проти пари «plan» (документ) / «trip» (подія) |
| `С2` | той самий обʼєкт: **«path», «track»** проти «route» / «trail» |
| `С3` | той самий обʼєкт: **«checklist», «inventory», «packing list»** проти «gear» |
| `С5` | той самий обʼєкт: **«stage», «segment»** проти «day» / «leg» / «section» |
| `Д1`–`Д12` | та сама дія під різними назвами кнопок — розшифровка в розділі 4 |
| `Т1` | піктограма або емодзі в тексті продукту |
| `Ж` | технічний жаргон або витік службової назви екрана чи файлу |
| `З1` | заглушка макета — опис того, що буде намальовано в рамці |
| `З2` | текст-заглушка замість змісту, якого ще немає |
| `Р` | **редакційний текст** — пише автор статей або третя сторона, не продуктовий копірайтер |

Позначка `✎` («переписано за voice.md») була в українській версії й зникла разом із нею: переклад 2026-09-24 замінив увесь текст, тож було/стало з `_rewrite.py` більше ні на що не вказує.

## 1. Глобальний хром — винесено з таблиці

Ці рядки стоять **однаково на всіх 63 екранах**, тому в таблиці нижче їх немає: інакше вони дали б 291 однакових рядків шуму. Те, що вони ідентичні, — це добре, і саме тому вони тут окремо, а не серед іншого.

| Область | Рядок | Тип | Екранів |
|---|---|---|---|
| таббар | Map | кнопка | 33 |
| таббар | Plans | кнопка | 33 |
| таббар | Guide | кнопка | 33 |
| таббар | Safety | кнопка | 33 |
| таббар | Profile | кнопка | 33 |
| таббар | 4 *(бейдж «лишилось закріпити»)* | лічильник | 27 |
| футер | Maps and trails © Kartverket (CC BY 4.0) · Lantmäteriet (CC0) · Weather met.no · Transport Trafikverket | атрибуція | 63 |
| футер | Where this comes from | розкривач | 63 |
| футер | Last checked: 13 August 2026, 09:12 | атрибуція | 51 |

**Одне спостереження вже тут.** Рядок джерел у футері (`Where this comes from` → деталізація) **різний на кожному екрані** — тому він лишився в таблиці. Це правильно: він говорить про те, що на цьому екрані стверджується. А от «Last checked: 13 August 2026, 09:12» стоїть на 51 екрані з 63 — і на екранах, де дані свіжі, і на тих, де вони з кешу.

---

## 2. Таблиця — увесь текст інтерфейсу

953 рядків. Згруповано за вкладками, усередині вкладки — базовий екран і його стани одразу за ним, щоб було видно, де стан говорить про те саме інакше.

### Map · Where to go

#### `catalogue.html` — успіх

| Зона | Рядок | Тип | Позначки |
|---|---|---|---|
| — | Where to go | заголовок екрана |  |
| — | Where to go | заголовок екрана |  |
| Where, when, who | Where, when, who | заголовок зони |  |
| Where, when, who | Lapland, Sweden — or your own route: from → to | підпис |  |
| Where, when, who | Where | пункт списку |  |
| Where, when, who | 17–22 August | підпис |  |
| Where, when, who | When | пункт списку |  |
| Where, when, who | 2 people · 1 STF member | підпис |  |
| Where, when, who | Who | пункт списку |  |
| Where, when, who | huts | кнопка |  |
| Where, when, who | tent | кнопка |  |
| Map | Map | заголовок зони |  |
| Map | на весь екран під пошуком · аркуш зі списком зверху | заглушка макета | `З1` |
| Map | map · Sweden · preset route lines · start/finish points: stations, trailheads, huts · own route drawn: Abisko Turiststation → Nikkaluokta | заглушка макета | `З1` |
| Map | your route · 101 km · 6 days · 5 huts | підпис |  |
| Map | Abisko Turiststation → Nikkaluokta | підпис |  |
| Map | Make a plan | кнопка | `Д3` |
| Map | Clear points | кнопка |  |
| Best in Sweden in August | Best in Sweden in August | заголовок зони |  |
| Best in Sweden in August | photo · Kungsleden · path along Abiskojaure lake | заглушка макета | `З1` |
| Best in Sweden in August | 6 days | індикатор |  |
| Best in Sweden in August | 101 km · 1,940 m · 5 STF huts · blå / medium | підпис |  |
| Best in Sweden in August | photo · Kungsleden · path along Abiskojaure lake Kungsleden · Abisko → Nikkaluokta 6 days | посилання |  |
| Best in Sweden in August | photo · Kebnekaise valley from the trail | заглушка макета | `З1` |
| Best in Sweden in August | 5 days | індикатор |  |
| Best in Sweden in August | 82 km · 1,460 m · 4 STF huts · blå / medium | підпис |  |
| Best in Sweden in August | photo · Kebnekaise valley from the trail Kungsleden · Abisko → Kebnekaise 5 days | посилання |  |
| Best in Sweden in August | photo · Padjelanta plateau, Sami huts | заглушка макета | `З1` |
| Best in Sweden in August | 7 days | індикатор |  |
| Best in Sweden in August | 140 km · 900 m · STF and Sami community huts | підпис |  |
| Best in Sweden in August | photo · Padjelanta plateau, Sami huts Padjelantaleden · Kvikkjokk → Ritsem 7 days | посилання |  |
| Scandinavian classics | Scandinavian classics | заголовок зони |  |
| Scandinavian classics | photo · Besseggen ridge, Jotunheimen | заглушка макета | `З1` |
| Scandinavian classics | 4 days | індикатор |  |
| Scandinavian classics | 58 km · 2,300 m · DNT huts · DNT key required | підпис |  |
| Scandinavian classics | photo · Besseggen ridge, Jotunheimen Jotunheimen · Gjendesheim → Spiterstulen 4 days | посилання |  |
| Scandinavian classics | photo · Hardangervidda plateau at Finse | заглушка макета | `З1` |
| Scandinavian classics | 7 days | індикатор |  |
| Scandinavian classics | 120 km · 1,100 m · DNT huts | підпис |  |
| Scandinavian classics | photo · Hardangervidda plateau at Finse Hardangervidda · Finse → Haukeliseter 7 days | посилання |  |
| футер | Trails and terrain: Lantmäteriet (CC0) for Sweden, Kartverket (CC BY 4.0) for Norway. Weather: met.no Locationforecast. Transport: Trafikverket, Entur. Huts — type, key, beds, season — from the static fields of the public DNT and STF object schema. | атрибуція |  |

#### `catalogue-empty.html` — порожній

| Зона | Рядок | Тип | Позначки |
|---|---|---|---|
| — | Where to go | заголовок екрана |  |
| — | Where to go | заголовок екрана |  |
| Where, when, who | Where, when, who | заголовок зони |  |
| Where, when, who | Lapland, Sweden — or your own route: from → to | підпис |  |
| Where, when, who | Where | пункт списку |  |
| Where, when, who | 17–22 August | підпис |  |
| Where, when, who | When | пункт списку |  |
| Where, when, who | 2 people · 1 STF member | підпис |  |
| Where, when, who | Who | пункт списку |  |
| Where, when, who | huts | кнопка |  |
| Where, when, who | tent | кнопка |  |
| Map | Map | заголовок зони |  |
| Map | на весь екран під пошуком · аркуш зверху | заглушка макета | `З1` |
| Map | map · Sweden · no route lines · huts closed for February | заглушка макета | `З1` |
| Map | The huts are closed in February — there are no routes with hut nights. | текст |  |
| Map | Pick dates in June — September | кнопка |  |
| Best in Sweden in February | Best in Sweden in February | заголовок зони |  |
| Best in Sweden in February | huts open, Kungsleden in season | підпис |  |
| Best in Sweden in February | Late June — July | пункт списку |  |
| Best in Sweden in February | 6 routes | індикатор |  |
| Best in Sweden in February | fewer people, shorter days | підпис |  |
| Best in Sweden in February | August — September | пункт списку |  |
| Best in Sweden in February | 6 routes | індикатор |  |
| Scandinavian classics | Scandinavian classics | заголовок зони |  |
| Scandinavian classics | Jotunheimen · Hardangervidda · Kungsleden | підпис |  |
| Scandinavian classics | Summer classics | пункт списку |  |
| футер | Trails and terrain: Lantmäteriet (CC0) for Sweden, Kartverket (CC BY 4.0) for Norway. Weather: met.no Locationforecast. Transport: Trafikverket, Entur. Huts — type, key, beds, season — from the static fields of the public DNT and STF object schema. | атрибуція |  |

### Map · New plan

#### `new-plan.html` — успіх

| Зона | Рядок | Тип | Позначки |
|---|---|---|---|
| — | ‹ Where to go | кнопка |  |
| — | New plan | заголовок екрана |  |
| — | Kungsleden · Abisko → Nikkaluokta | заголовок екрана |  |
| Overview | Overview | заголовок зони |  |
| Overview | на всю ширину | заглушка макета | `З1` |
| Overview | photo · Kungsleden · path along Abiskojaure lake — from the start point | заглушка макета | `З1` |
| Overview | change | підпис |  |
| Overview | 17–22 August · 2 people · 1 STF member | пункт списку |  |
| Plan status | Plan status | заголовок зони |  |
| Plan status | Everything fits. | текст |  |
| Route | Route | заголовок зони |  |
| Route | на всю ширину · тап → на весь екран | заглушка макета | `З1` |
| Route | map · Abisko → Nikkaluokta · day legs · huts · bail-out points | заглушка макета | `З1` |
| Route | distance | підпис |  |
| Route | 101 km | пункт списку |  |
| Route | ascent | підпис |  |
| Route | 1,940 m | пункт списку |  |
| Route | days | підпис |  |
| Route | 6 | пункт списку |  |
| Route | longest day | підпис |  |
| Route | ~8 h | пункт списку |  |
| Route | blå / medium · röd / krevende on the pass | текст |  |
| What you need | What you need | заголовок зони |  |
| What you need | second person isn’t a member: +1,200 SEK for 5 nights | підпис |  |
| What you need | STF membership | пункт списку |  |
| What you need | 1 of 2 | індикатор |  |
| What you need | seasonal normal · +6…+14 °C, rain every third day | підпис |  |
| What you need | Weather in August | підпис |  |
| What you need | 23 items · 11.4 kg | підпис |  |
| What you need | Gear | пункт списку | `Д6` |
| What you need | 2 missing | індикатор |  |
| What you need | 2,500 SEK nights per person · transport 1,430 SEK | підпис |  |
| What you need | Cost | підпис |  |
| Days | Days | заголовок зони |  |
| Days | night train 94 · Stockholm C → Abisko | підпис |  |
| Days | Getting there · Sun 16 Aug | підпис |  |
| Days | 14 km · ~4 h 30 · Abiskojaure fjällstuga | підпис |  |
| Days | 1 · Abisko → Abiskojaure | пункт списку |  |
| Days | 22 km · ~7 h · Alesjaure fjällstuga | підпис |  |
| Days | 2 · Abiskojaure → Alesjaure | пункт списку |  |
| Days | 13 km · ~4 h 30 · Tjäktja — walk-in only | підпис |  |
| Days | 3 · Alesjaure → Tjäktja | пункт списку |  |
| Days | by 18:00 | індикатор |  |
| Days | 12 km · pass 1,150 m · Sälka fjällstuga | підпис |  |
| Days | 4 · Tjäktja → Sälka | пункт списку |  |
| Days | 26 km · ~8 h · Kebnekaise fjällstation | підпис |  |
| Days | 5 · Sälka → Kebnekaise | пункт списку |  |
| Days | 19 km · ~5 h | підпис |  |
| Days | 6 · Kebnekaise → Nikkaluokta | підпис |  |
| Days | bus 91 Nikkaluokta → Kiruna · train 92 | підпис |  |
| Days | Getting back · Sat 22 Aug | підпис |  |
| Notes and reviews | Notes and reviews | заголовок зони |  |
| Notes and reviews | field note · 6 Aug · ford knee-deep | підпис |  |
| Notes and reviews | Bridge before Tjäktja washed out | пункт списку |  |
| Notes and reviews | day 3 | індикатор |  |
| Notes and reviews | 128 · latest 13 Aug | підпис |  |
| Notes and reviews | Reviews | пункт списку | `Д9` |
| Notes and reviews | 4.3 | індикатор |  |
| Save | Save | заголовок зони |  |
| Save | Save plan | кнопка |  |
| Save | Cancel | кнопка |  |
| футер | Trails and terrain: Lantmäteriet (CC0) for Sweden, Kartverket (CC BY 4.0) for Norway. Weather: met.no Locationforecast. Transport: Trafikverket, Entur. Huts — type, key, beds, season — from the static fields of the public DNT and STF object schema. | атрибуція |  |

#### `new-plan-conflict.html` — конфлікт

| Зона | Рядок | Тип | Позначки |
|---|---|---|---|
| — | ‹ Where to go | кнопка |  |
| — | New plan | заголовок екрана |  |
| — | Kungsleden · Abisko → Nikkaluokta | заголовок екрана |  |
| Overview | Overview | заголовок зони |  |
| Overview | на всю ширину | заглушка макета | `З1` |
| Overview | photo · Kungsleden · path along Abiskojaure lake — from the start point | заглушка макета | `З1` |
| Overview | change | підпис |  |
| Overview | 17–20 August · 2 people · 1 STF member | пункт списку |  |
| Plan status | Plan status | заголовок зони |  |
| Plan status | 4 days don’t fit this route | повідомлення стану |  |
| Plan status | Between Sälka and Nikkaluokta 45 km remain — that’s not a day’s walk. | повідомлення стану |  |
| Plan status | 6 days · longest day ~8 h | підпис |  |
| Plan status | +2 days | пункт списку |  |
| Plan status | 19 km shorter | підпис |  |
| Plan status | Finish at Kebnekaise | пункт списку |  |
| Plan status | between Sälka and Singi | підпис |  |
| Plan status | Tent on night 4 | пункт списку |  |
| Plan status | different stay | індикатор |  |
| Route | Route | заголовок зони |  |
| Route | на всю ширину · тап → на весь екран | заглушка макета | `З1` |
| Route | map · Abisko → Nikkaluokta · day legs · huts · bail-out points | заглушка макета | `З1` |
| Route | distance | підпис |  |
| Route | 101 km | пункт списку |  |
| Route | ascent | підпис |  |
| Route | 1,940 m | пункт списку |  |
| Route | days | підпис |  |
| Route | 6 | пункт списку |  |
| Route | longest day | підпис |  |
| Route | ~8 h | пункт списку |  |
| Route | blå / medium · röd / krevende on the pass | текст |  |
| What you need | What you need | заголовок зони |  |
| What you need | second person isn’t a member: +1,200 SEK for 5 nights | підпис |  |
| What you need | STF membership | пункт списку |  |
| What you need | 1 of 2 | індикатор |  |
| What you need | seasonal normal · +6…+14 °C, rain every third day | підпис |  |
| What you need | Weather in August | підпис |  |
| What you need | 23 items · 11.4 kg | підпис |  |
| What you need | Gear | пункт списку | `Д6` |
| What you need | 2 missing | індикатор |  |
| What you need | 2,500 SEK nights per person · transport 1,430 SEK | підпис |  |
| What you need | Cost | підпис |  |
| Days | Days | заголовок зони |  |
| Days | night train 94 · Stockholm C → Abisko | підпис |  |
| Days | Getting there · Sun 16 Aug | підпис |  |
| Days | 14 km · ~4 h 30 · Abiskojaure fjällstuga | підпис |  |
| Days | 1 · Abisko → Abiskojaure | пункт списку |  |
| Days | 22 km · ~7 h · Alesjaure fjällstuga | підпис |  |
| Days | 2 · Abiskojaure → Alesjaure | пункт списку |  |
| Days | 13 km · ~4 h 30 · Tjäktja — walk-in only | підпис |  |
| Days | 3 · Alesjaure → Tjäktja | пункт списку |  |
| Days | by 18:00 | індикатор |  |
| Days | 12 km · pass 1,150 m · Sälka fjällstuga | підпис |  |
| Days | 4 · Tjäktja → Sälka | пункт списку |  |
| Days | 26 km · ~8 h · Kebnekaise fjällstation | підпис |  |
| Days | 5 · Sälka → Kebnekaise | пункт списку |  |
| Days | 19 km · ~5 h | підпис |  |
| Days | 6 · Kebnekaise → Nikkaluokta | підпис |  |
| Days | bus 91 Nikkaluokta → Kiruna · train 92 | підпис |  |
| Days | Getting back · Sat 22 Aug | підпис |  |
| Notes and reviews | Notes and reviews | заголовок зони |  |
| Notes and reviews | field note · 6 Aug · ford knee-deep | підпис |  |
| Notes and reviews | Bridge before Tjäktja washed out | пункт списку |  |
| Notes and reviews | day 3 | індикатор |  |
| Notes and reviews | 128 · latest 13 Aug | підпис |  |
| Notes and reviews | Reviews | пункт списку | `Д9` |
| Notes and reviews | 4.3 | індикатор |  |
| Save | Save | заголовок зони |  |
| Save | Choose one of the options | кнопка |  |
| Save | Cancel | кнопка |  |
| футер | Trails and terrain: Lantmäteriet (CC0) for Sweden, Kartverket (CC BY 4.0) for Norway. Weather: met.no Locationforecast. Transport: Trafikverket, Entur. Huts — type, key, beds, season — from the static fields of the public DNT and STF object schema. | атрибуція |  |

#### `new-plan-error.html` — помилка

| Зона | Рядок | Тип | Позначки |
|---|---|---|---|
| — | ‹ Where to go | кнопка |  |
| — | New plan | заголовок екрана |  |
| — | Kungsleden · Abisko → Nikkaluokta | заголовок екрана |  |
| Overview | Overview | заголовок зони |  |
| Overview | на всю ширину | заглушка макета | `З1` |
| Overview | photo · Kungsleden · path along Abiskojaure lake — from the start point | заглушка макета | `З1` |
| Overview | change | підпис |  |
| Overview | 17–22 August · 2 people · 1 STF member | пункт списку |  |
| Plan status | Plan status | заголовок зони |  |
| Plan status | Couldn’t build the plan | повідомлення стану |  |
| Plan status | Trail data is unavailable right now. Try again in a minute. | повідомлення стану |  |
| Plan status | Try again | кнопка | `Д11` |
| Route | Route | заголовок зони |  |
| Route | No trail data. | текст |  |
| What you need | What you need | заголовок зони |  |
| What you need | — | текст |  |
| Days | Days | заголовок зони |  |
| Days | — | текст |  |
| Notes and reviews | Notes and reviews | заголовок зони |  |
| Notes and reviews | — | текст |  |
| Save | Save | заголовок зони |  |
| Save | Cancel | кнопка |  |
| футер | Trails and terrain: Lantmäteriet (CC0) for Sweden, Kartverket (CC BY 4.0) for Norway. Weather: met.no Locationforecast. Transport: Trafikverket, Entur. Huts — type, key, beds, season — from the static fields of the public DNT and STF object schema. | атрибуція |  |

#### `new-plan-loading.html` — завантаження

| Зона | Рядок | Тип | Позначки |
|---|---|---|---|
| — | ‹ Where to go | кнопка |  |
| — | New plan | заголовок екрана |  |
| — | Kungsleden · Abisko → Nikkaluokta | заголовок екрана |  |
| Overview | Overview | заголовок зони |  |
| Plan status | Plan status | заголовок зони |  |
| Plan status | trails · nights · load · transport · weather | підпис |  |
| Plan status | Building your plan | підпис |  |
| Plan status | 4 of 6 | індикатор |  |
| Route | Route | заголовок зони |  |
| What you need | What you need | заголовок зони |  |
| Days | Days | заголовок зони |  |
| Notes and reviews | Notes and reviews | заголовок зони |  |
| Save | Save | заголовок зони |  |
| футер | Trails and terrain: Lantmäteriet (CC0) for Sweden, Kartverket (CC BY 4.0) for Norway. Weather: met.no Locationforecast. Transport: Trafikverket, Entur. Huts — type, key, beds, season — from the static fields of the public DNT and STF object schema. | атрибуція |  |

### Map · Another hut

#### `huts.html` — успіх

| Зона | Рядок | Тип | Позначки |
|---|---|---|---|
| — | ✕ Close | кнопка | `Т1` |
| — | Another hut | заголовок екрана | `Д4` |
| — | Night 4 · another hut | заголовок екрана |  |
| Filters | Filters | заголовок зони |  |
| Filters | within 5 km of the trail | кнопка |  |
| Filters | bookable | кнопка |  |
| Filters | no key | кнопка |  |
| Huts nearby | Huts nearby | заголовок зони |  |
| Huts nearby | in your plan now · 12 km · 24 beds · no key | підпис |  |
| Huts nearby | Sälka fjällstuga | пункт списку |  |
| Huts nearby | bookable | індикатор |  |
| Huts nearby | +7 km off the trail · 14 beds · no key | підпис |  |
| Huts nearby | Nallostugan | пункт списку |  |
| Huts nearby | bookable | індикатор |  |
| Huts nearby | 26 km — too long a day after the pass | підпис |  |
| Huts nearby | Singi fjällstuga | пункт списку |  |
| Huts nearby | ~9 h | індикатор |  |
| Huts nearby | stay another night · 24 beds | підпис |  |
| Huts nearby | Tjäktja fjällstuga | пункт списку |  |
| Huts nearby | walk-in only | індикатор |  |
| футер | Trails and terrain: Lantmäteriet (CC0) for Sweden, Kartverket (CC BY 4.0) for Norway. Weather: met.no Locationforecast. Transport: Trafikverket, Entur. Huts — type, key, beds, season — from the static fields of the public DNT and STF object schema. | атрибуція |  |

#### `huts-empty.html` — порожній

| Зона | Рядок | Тип | Позначки |
|---|---|---|---|
| — | ✕ Close | кнопка | `Т1` |
| — | Another hut | заголовок екрана | `Д4` |
| — | Night 4 · another hut | заголовок екрана |  |
| Filters | Filters | заголовок зони |  |
| Filters | within 5 km of the trail | кнопка |  |
| Filters | bookable | кнопка |  |
| Filters | no key | кнопка |  |
| Huts nearby | Huts nearby | заголовок зони |  |
| Huts nearby | No huts match these filters. | текст |  |
| Huts nearby | Tjäktja — walk-in only, by 18:00 | підпис |  |
| Huts nearby | Remove “bookable” | пункт списку |  |
| Huts nearby | between Tjäktja and Sälka · allemansrätten allows it | підпис |  |
| Huts nearby | Tent | підпис |  |
| футер | Trails and terrain: Lantmäteriet (CC0) for Sweden, Kartverket (CC BY 4.0) for Norway. Weather: met.no Locationforecast. Transport: Trafikverket, Entur. Huts — type, key, beds, season — from the static fields of the public DNT and STF object schema. | атрибуція |  |

### Map · Hut

#### `hut.html` — успіх

| Зона | Рядок | Тип | Позначки |
|---|---|---|---|
| — | ✕ Close | кнопка | `Т1` |
| — | Hut | заголовок екрана |  |
| — | Sälka fjällstuga | заголовок екрана |  |
| Hut | Hut | заголовок зони |  |
| Hut | на всю ширину | заглушка макета | `З1` |
| Hut | photo · Sälka fjällstuga under the pass | заглушка макета | `З1` |
| Hut | STF fjällstuga · self-service | підпис |  |
| Hut | Type | підпис |  |
| Hut | bookable · after 18:00 the bed isn’t held; a place indoors still is | підпис |  |
| Hut | Booking | підпис |  |
| Hut | 24 | підпис |  |
| Hut | Beds | підпис |  |
| Hut | not needed | підпис |  |
| Hut | Key | підпис |  |
| Hut | 20 June — 15 September | підпис |  |
| Hut | Season | підпис |  |
| On site | On site | заголовок зони |  |
| On site | gas and cookware · shop with basic food | підпис |  |
| On site | Kitchen | підпис |  |
| On site | from the stream 100 m away | підпис |  |
| On site | Water | підпис |  |
| On site | yes | підпис |  |
| On site | Sauna | підпис |  |
| On site | names and membership numbers | підпис |  |
| On site | Logbook | підпис |  |
| Field notes | Field notes | заголовок зони | `Д8` |
| Field notes | note · 8 Aug | підпис |  |
| Field notes | Beds ran out at 16:00 | пункт списку |  |
| In your plan | In your plan | заголовок зони |  |
| In your plan | Stay here on night 4 | кнопка | `Д4` |
| футер | Trails and terrain: Lantmäteriet (CC0) for Sweden, Kartverket (CC BY 4.0) for Norway. Weather: met.no Locationforecast. Transport: Trafikverket, Entur. Huts — type, key, beds, season — from the static fields of the public DNT and STF object schema. | атрибуція |  |

### Map · Notes and reviews

#### `notes.html` — успіх

| Зона | Рядок | Тип | Позначки |
|---|---|---|---|
| — | ✕ Close | кнопка | `Т1` |
| — | Notes and reviews | заголовок екрана |  |
| — | Alesjaure → Tjäktja | заголовок екрана |  |
| Show | Show | заголовок зони |  |
| Show | Field notes | посилання | `Д8` |
| Show | Reviews | посилання | `Д9` |
| Field notes | Field notes | заголовок зони | `Д8` |
| Field notes | 6 Aug · ford knee-deep, waist-deep after rain | підпис |  |
| Field notes | Bridge before Tjäktja washed out | підпис |  |
| Field notes | in your plan | індикатор |  |
| Field notes | 3 Aug · follow the cairns | підпис |  |
| Field notes | Sparse waymarks after the ford | підпис |  |
| Reviews | Reviews | заголовок зони | `Д9` |
| Reviews | 8–13 Aug · got a mattress on the floor | підпис |  |
| Reviews | Beds at Sälka ran out at 16:00 | підпис |  |
| Reviews | 4 of 5 | індикатор |  |
| Reviews | 2–8 Aug | підпис |  |
| Reviews | Day two is harder than the profile suggests | підпис |  |
| Reviews | 5 of 5 | індикатор |  |
| Write a note | Write a note | заголовок зони |  |
| Write a note | trail | кнопка |  |
| Write a note | water | кнопка |  |
| Write a note | ford | кнопка |  |
| Write a note | snow | кнопка |  |
| Write a note | waymarks | кнопка |  |
| Write a note | tent spot | кнопка |  |
| Write a note | What’s on this section right now | підпис поля |  |
| Write a note | ford above the knee after rain | плейсхолдер поля |  |
| Write a note | Send | кнопка |  |
| футер | Trails and terrain: Lantmäteriet (CC0) for Sweden, Kartverket (CC BY 4.0) for Norway. Weather: met.no Locationforecast. Transport: Trafikverket, Entur. Huts — type, key, beds, season — from the static fields of the public DNT and STF object schema. | атрибуція |  |

#### `notes-empty.html` — порожній

| Зона | Рядок | Тип | Позначки |
|---|---|---|---|
| — | ✕ Close | кнопка | `Т1` |
| — | Notes and reviews | заголовок екрана |  |
| — | Alesjaure → Tjäktja | заголовок екрана |  |
| Show | Show | заголовок зони |  |
| Show | Field notes | посилання | `Д8` |
| Show | Reviews | посилання | `Д9` |
| Field notes | Field notes | заголовок зони | `Д8` |
| Field notes | No notes for this section yet. | текст |  |
| Reviews | Reviews | заголовок зони | `Д9` |
| Reviews | No reviews yet. | текст |  |
| Write a note | Write a note | заголовок зони |  |
| Write a note | trail | кнопка |  |
| Write a note | water | кнопка |  |
| Write a note | ford | кнопка |  |
| Write a note | snow | кнопка |  |
| Write a note | waymarks | кнопка |  |
| Write a note | tent spot | кнопка |  |
| Write a note | What’s on this section right now | підпис поля |  |
| Write a note | ford above the knee after rain | плейсхолдер поля |  |
| Write a note | Send | кнопка |  |
| футер | Trails and terrain: Lantmäteriet (CC0) for Sweden, Kartverket (CC BY 4.0) for Norway. Weather: met.no Locationforecast. Transport: Trafikverket, Entur. Huts — type, key, beds, season — from the static fields of the public DNT and STF object schema. | атрибуція |  |

### Plans · Plan

#### `plan.html` — успіх

| Зона | Рядок | Тип | Позначки |
|---|---|---|---|
| — | ‹ My trips | кнопка |  |
| — | Plan | заголовок екрана |  |
| — | Kungsleden · Abisko → Nikkaluokta | заголовок екрана |  |
| Overview | Overview | заголовок зони |  |
| Overview | на всю ширину | заглушка макета | `З1` |
| Overview | photo · Kungsleden · path along Abiskojaure lake | заглушка макета | `З1` |
| Overview | offline ✓ | підпис | `Т1` |
| Overview | 17–22 August · 2 people · 1 STF member | підпис |  |
| Overview | Share my route | кнопка | `Д1` |
| Overview | Change plan | розкривач |  |
| Overview | Booking and ticket marks in the plan will be reset. They stay in STF and SJ — cancel there if you need to. | текст |  |
| Overview | Change and reset | кнопка |  |
| Needs attention | Needs attention | заголовок зони |  |
| Needs attention | day 2: you won’t reach Alesjaure by 18:00 · decide by 15 Aug | підпис |  |
| Needs attention | Flooding on Abiskojåkka | пункт списку |  |
| Needs attention | day 2 | індикатор |  |
| Route | Route | заголовок зони |  |
| Route | на всю ширину · тап → на весь екран, шари там | заглушка макета | `З1` |
| Route | map · Kungsleden · day legs · huts · bail-out points | заглушка макета | `З1` |
| Route | distance | підпис |  |
| Route | 101 km | пункт списку |  |
| Route | ascent | підпис |  |
| Route | 1,940 m | пункт списку |  |
| Route | days | підпис |  |
| Route | 6 | пункт списку |  |
| Route | longest day | підпис |  |
| Route | ~8 h | пункт списку |  |
| About the trip | About the trip | заголовок зони |  |
| About the trip | both STF members | підпис |  |
| About the trip | Membership and key | пункт списку |  |
| About the trip | 23 items · 11.4 kg | підпис |  |
| About the trip | Gear | пункт списку | `Д6` |
| About the trip | 1 missing | індикатор |  |
| About the trip | met.no forecast · 13 Aug 09:12 | підпис |  |
| About the trip | Weather | підпис |  |
| About the trip | 2,500 SEK nights per person · transport 1,430 SEK | підпис |  |
| About the trip | Cost | підпис |  |
| Days | Days | заголовок зони |  |
| Days | night train 94 · Stockholm C → Abisko | підпис |  |
| Days | Getting there · Sun 16 Aug | підпис |  |
| Days | 14 km · ~4 h 30 | підпис |  |
| Days | 1 · Abisko → Abiskojaure | пункт списку |  |
| Days | 22 km · ~7 h | підпис |  |
| Days | 2 · Abiskojaure → Alesjaure | пункт списку |  |
| Days | flood | індикатор |  |
| Days | 13 km · ~4 h 30 · walk-in only | підпис |  |
| Days | 3 · Alesjaure → Tjäktja | пункт списку |  |
| Days | 12 km · pass 1,150 m · Sälka not booked | підпис |  |
| Days | 4 · Tjäktja → Sälka | пункт списку |  |
| Days | book | індикатор | `Д2` |
| Days | 26 km · ~8 h | підпис |  |
| Days | 5 · Sälka → Kebnekaise | пункт списку |  |
| Days | 19 km · ~5 h | підпис |  |
| Days | 6 · Kebnekaise → Nikkaluokta | пункт списку |  |
| Days | bus 91 → Kiruna · ticket not bought | підпис |  |
| Days | Getting back · Sat 22 Aug | пункт списку |  |
| Days | buy | індикатор |  |
| футер | Trails and terrain: Lantmäteriet (CC0) for Sweden, Kartverket (CC BY 4.0) for Norway. Weather: met.no Locationforecast. Transport: Trafikverket, Entur. Huts — type, key, beds, season — from the static fields of the public DNT and STF object schema. | атрибуція |  |

#### `plan-error.html` — помилка

| Зона | Рядок | Тип | Позначки |
|---|---|---|---|
| — | ‹ My trips | кнопка |  |
| — | Plan | заголовок екрана |  |
| — | Kungsleden · Abisko → Nikkaluokta | заголовок екрана |  |
| Overview | Overview | заголовок зони |  |
| Overview | на всю ширину | заглушка макета | `З1` |
| Overview | photo · Kungsleden · path along Abiskojaure lake | заглушка макета | `З1` |
| Overview | offline ✓ | підпис | `Т1` |
| Overview | 17–22 August · 2 people · 1 STF member | підпис |  |
| Overview | Share my route | кнопка | `Д1` |
| Overview | Change plan | розкривач |  |
| Overview | Booking and ticket marks in the plan will be reset. They stay in STF and SJ — cancel there if you need to. | текст |  |
| Overview | Change and reset | кнопка |  |
| Needs attention | Needs attention | заголовок зони |  |
| Needs attention | Couldn’t update. Data from 13 August, 09:12. | текст |  |
| Needs attention | Try again | кнопка | `Д11` |
| Route | Route | заголовок зони |  |
| Route | на всю ширину · тап → на весь екран, шари там | заглушка макета | `З1` |
| Route | map · Kungsleden · day legs · huts · bail-out points | заглушка макета | `З1` |
| Route | distance | підпис |  |
| Route | 101 km | пункт списку |  |
| Route | ascent | підпис |  |
| Route | 1,940 m | пункт списку |  |
| Route | days | підпис |  |
| Route | 6 | пункт списку |  |
| Route | longest day | підпис |  |
| Route | ~8 h | пункт списку |  |
| About the trip | About the trip | заголовок зони |  |
| About the trip | both STF members | підпис |  |
| About the trip | Membership and key | пункт списку |  |
| About the trip | 23 items · 11.4 kg | підпис |  |
| About the trip | Gear | пункт списку | `Д6` |
| About the trip | 1 missing | індикатор |  |
| About the trip | met.no forecast · 13 Aug 09:12 | підпис |  |
| About the trip | Weather | підпис |  |
| About the trip | 2,500 SEK nights per person · transport 1,430 SEK | підпис |  |
| About the trip | Cost | підпис |  |
| Days | Days | заголовок зони |  |
| Days | night train 94 · Stockholm C → Abisko | підпис |  |
| Days | Getting there · Sun 16 Aug | підпис |  |
| Days | 14 km · ~4 h 30 | підпис |  |
| Days | 1 · Abisko → Abiskojaure | пункт списку |  |
| Days | 22 km · ~7 h | підпис |  |
| Days | 2 · Abiskojaure → Alesjaure | пункт списку |  |
| Days | flood | індикатор |  |
| Days | 13 km · ~4 h 30 · walk-in only | підпис |  |
| Days | 3 · Alesjaure → Tjäktja | пункт списку |  |
| Days | 12 km · pass 1,150 m · Sälka not booked | підпис |  |
| Days | 4 · Tjäktja → Sälka | пункт списку |  |
| Days | book | індикатор | `Д2` |
| Days | 26 km · ~8 h | підпис |  |
| Days | 5 · Sälka → Kebnekaise | пункт списку |  |
| Days | 19 km · ~5 h | підпис |  |
| Days | 6 · Kebnekaise → Nikkaluokta | пункт списку |  |
| Days | bus 91 → Kiruna · ticket not bought | підпис |  |
| Days | Getting back · Sat 22 Aug | пункт списку |  |
| Days | buy | індикатор |  |
| футер | Trails and terrain: Lantmäteriet (CC0) for Sweden, Kartverket (CC BY 4.0) for Norway. Weather: met.no Locationforecast. Transport: Trafikverket, Entur. Huts — type, key, beds, season — from the static fields of the public DNT and STF object schema. | атрибуція |  |

#### `plan-offline.html` — офлайн

| Зона | Рядок | Тип | Позначки |
|---|---|---|---|
| — | ‹ My trips | кнопка |  |
| — | Plan | заголовок екрана |  |
| — | Kungsleden · Abisko → Nikkaluokta | заголовок екрана |  |
| Overview | Overview | заголовок зони |  |
| Overview | на всю ширину | заглушка макета | `З1` |
| Overview | photo · Kungsleden · path along Abiskojaure lake | заглушка макета | `З1` |
| Overview | offline pack from 14 Aug | підпис |  |
| Overview | 17–22 August · 2 people · 1 STF member | підпис |  |
| Overview | Share my route | кнопка | `Д1` |
| Overview | Change plan | розкривач |  |
| Overview | Booking and ticket marks in the plan will be reset. They stay in STF and SJ — cancel there if you need to. | текст |  |
| Overview | Change and reset | кнопка |  |
| Needs attention | Needs attention | заголовок зони |  |
| Needs attention | No connection. Data from the offline pack of 14 August. | текст |  |
| Route | Route | заголовок зони |  |
| Route | на всю ширину · тап → на весь екран, шари там | заглушка макета | `З1` |
| Route | map · Kungsleden · day legs · huts · bail-out points · offline pack | заглушка макета | `З1` |
| Route | distance | підпис |  |
| Route | 101 km | пункт списку |  |
| Route | ascent | підпис |  |
| Route | 1,940 m | пункт списку |  |
| Route | days | підпис |  |
| Route | 6 | пункт списку |  |
| Route | longest day | підпис |  |
| Route | ~8 h | пункт списку |  |
| About the trip | About the trip | заголовок зони |  |
| About the trip | both STF members | підпис |  |
| About the trip | Membership and key | пункт списку |  |
| About the trip | 23 items · 11.4 kg | підпис |  |
| About the trip | Gear | пункт списку | `Д6` |
| About the trip | 1 missing | індикатор |  |
| About the trip | met.no forecast · 13 Aug 09:12 | підпис |  |
| About the trip | Weather | підпис |  |
| About the trip | 2,500 SEK nights per person · transport 1,430 SEK | підпис |  |
| About the trip | Cost | підпис |  |
| Days | Days | заголовок зони |  |
| Days | night train 94 · Stockholm C → Abisko | підпис |  |
| Days | Getting there · Sun 16 Aug | підпис |  |
| Days | 14 km · ~4 h 30 | підпис |  |
| Days | 1 · Abisko → Abiskojaure | пункт списку |  |
| Days | 22 km · ~7 h | підпис |  |
| Days | 2 · Abiskojaure → Alesjaure | пункт списку |  |
| Days | flood | індикатор |  |
| Days | 13 km · ~4 h 30 · walk-in only | підпис |  |
| Days | 3 · Alesjaure → Tjäktja | пункт списку |  |
| Days | 12 km · pass 1,150 m · Sälka not booked | підпис |  |
| Days | 4 · Tjäktja → Sälka | пункт списку |  |
| Days | book | індикатор | `Д2` |
| Days | 26 km · ~8 h | підпис |  |
| Days | 5 · Sälka → Kebnekaise | пункт списку |  |
| Days | 19 km · ~5 h | підпис |  |
| Days | 6 · Kebnekaise → Nikkaluokta | пункт списку |  |
| Days | bus 91 → Kiruna · ticket not bought | підпис |  |
| Days | Getting back · Sat 22 Aug | пункт списку |  |
| Days | buy | індикатор |  |
| футер | Trails and terrain: Lantmäteriet (CC0) for Sweden, Kartverket (CC BY 4.0) for Norway. Weather: met.no Locationforecast. Transport: Trafikverket, Entur. Huts — type, key, beds, season — from the static fields of the public DNT and STF object schema. | атрибуція |  |

#### `plan-past.html` — пройдений

| Зона | Рядок | Тип | Позначки |
|---|---|---|---|
| — | ‹ My trips | кнопка |  |
| — | Plan | заголовок екрана |  |
| — | Kungsleden · Abisko → Nikkaluokta | заголовок екрана |  |
| Overview | Overview | заголовок зони |  |
| Overview | на всю ширину | заглушка макета | `З1` |
| Overview | photo · Kungsleden · path along Abiskojaure lake | заглушка макета | `З1` |
| Overview | offline ✓ | підпис | `Т1` |
| Overview | 17–22 August · 2 people · 1 STF member | підпис |  |
| Overview | Share my route | кнопка | `Д1` |
| Overview | Change plan | розкривач |  |
| Overview | Booking and ticket marks in the plan will be reset. They stay in STF and SJ — cancel there if you need to. | текст |  |
| Overview | Change and reset | кнопка |  |
| Needs attention | Needs attention | заголовок зони |  |
| Needs attention | Walked 17–22 August 2025. | текст |  |
| Needs attention | Plan again from this trip | кнопка | `Д3` |
| Route | Route | заголовок зони |  |
| Route | на всю ширину · тап → на весь екран, шари там | заглушка макета | `З1` |
| Route | map · Kungsleden · day legs · huts · bail-out points | заглушка макета | `З1` |
| Route | distance | підпис |  |
| Route | 101 km | пункт списку |  |
| Route | ascent | підпис |  |
| Route | 1,940 m | пункт списку |  |
| Route | days | підпис |  |
| Route | 6 | пункт списку |  |
| Route | longest day | підпис |  |
| Route | ~8 h | пункт списку |  |
| About the trip | About the trip | заголовок зони |  |
| About the trip | both STF members | підпис |  |
| About the trip | Membership and key | пункт списку |  |
| About the trip | 23 items · 11.4 kg | підпис |  |
| About the trip | Gear | пункт списку | `Д6` |
| About the trip | as it was: two rainy days out of five | підпис |  |
| About the trip | Weather | підпис |  |
| About the trip | 2,500 SEK nights per person · transport 1,430 SEK | підпис |  |
| About the trip | Cost | підпис |  |
| Days | Days | заголовок зони |  |
| Days | night train 94 · Stockholm C → Abisko | підпис |  |
| Days | Getting there · Sun 16 Aug | підпис |  |
| Days | 14 km · ~4 h 30 | підпис |  |
| Days | 1 · Abisko → Abiskojaure | пункт списку |  |
| Days | 22 km · ~7 h | підпис |  |
| Days | 2 · Abiskojaure → Alesjaure | пункт списку |  |
| Days | 13 km · ~4 h 30 · walk-in only | підпис |  |
| Days | 3 · Alesjaure → Tjäktja | пункт списку |  |
| Days | 12 km · pass 1,150 m | підпис |  |
| Days | 4 · Tjäktja → Sälka | пункт списку |  |
| Days | 26 km · ~8 h | підпис |  |
| Days | 5 · Sälka → Kebnekaise | пункт списку |  |
| Days | 19 km · ~5 h | підпис |  |
| Days | 6 · Kebnekaise → Nikkaluokta | пункт списку |  |
| Days | bus 91 → Kiruna | підпис |  |
| Days | Getting back · Sat 22 Aug | підпис |  |
| футер | Trails and terrain: Lantmäteriet (CC0) for Sweden, Kartverket (CC BY 4.0) for Norway. Weather: met.no Locationforecast. Transport: Trafikverket, Entur. Huts — type, key, beds, season — from the static fields of the public DNT and STF object schema. | атрибуція |  |

### Plans · Day

#### `day.html` — успіх

| Зона | Рядок | Тип | Позначки |
|---|---|---|---|
| — | ‹ Plan | кнопка |  |
| — | Day | заголовок екрана |  |
| — | Day 3 · Wed 19 August | заголовок екрана |  |
| Leg | Leg | заголовок зони |  |
| Leg | ‹ Day 2 | кнопка |  |
| Leg | Day 4 › | кнопка |  |
| Leg | на всю ширину · тап → на весь екран | заглушка макета | `З1` |
| Leg | map · day 3 · Alesjaure → Tjäktja · ford before the hut | заглушка макета | `З1` |
| Leg | на всю ширину | заглушка макета | `З1` |
| Leg | profile · +260 m | заглушка макета | `З1` |
| Leg | distance | підпис |  |
| Leg | 13 km | пункт списку |  |
| Leg | ascent | підпис |  |
| Leg | +260 m | пункт списку |  |
| Leg | walking | підпис |  |
| Leg | ~4 h 30 | пункт списку |  |
| Night | Night | заголовок зони |  |
| Night | self-service · 24 beds · no key | підпис |  |
| Night | Tjäktja fjällstuga | пункт списку |  |
| Night | walk-in only | індикатор |  |
| Night | Arrive by 18:00 · logbook: names and membership numbers. | текст |  |
| On this section | On this section | заголовок зони |  |
| On this section | note · 6 Aug · ford knee-deep | підпис |  |
| On this section | Bridge before Tjäktja washed out | пункт списку |  |
| On this section | ford | індикатор |  |
| On this section | streams every 2–3 km | підпис |  |
| On this section | Water | підпис |  |
| On this section | 8 km of boardwalk, 5 km of rock | підпис |  |
| On this section | Surface | підпис |  |
| Weather | Weather | заголовок зони |  |
| Weather | +9 °C · rain 4 mm · wind 7 m/s · met.no | текст |  |
| футер | Trails and terrain: Lantmäteriet (CC0) for Sweden, Kartverket (CC BY 4.0) for Norway. Weather: met.no Locationforecast. Transport: Trafikverket, Entur. Huts — type, key, beds, season — from the static fields of the public DNT and STF object schema. | атрибуція |  |

#### `day-intrip.html` — у дорозі

| Зона | Рядок | Тип | Позначки |
|---|---|---|---|
| — | ‹ Plan | кнопка |  |
| — | Day | заголовок екрана |  |
| — | Today · Alesjaure → Tjäktja | заголовок екрана |  |
| Now | Now | заголовок зони |  |
| Now | SOS · 112 | кнопка |  |
| Now | to go | підпис |  |
| Now | 9 km | пункт списку |  |
| Now | walking | підпис |  |
| Now | ~3 h | пункт списку |  |
| Now | arrive by | підпис |  |
| Now | 18:00 | пункт списку |  |
| Now | на всю ширину · позиція на вимогу | заглушка макета | `З1` |
| Now | map · you are here · 4 km from Alesjaure · ford before the hut | заглушка макета | `З1` |
| Night | Night | заголовок зони |  |
| Night | walk-in only · 24 beds · no key | підпис |  |
| Night | Tjäktja fjällstuga | пункт списку |  |
| Night | by 18:00 | індикатор |  |
| On this section | On this section | заголовок зони |  |
| On this section | higher after rain — cross before 15:00 | підпис |  |
| On this section | Ford before the hut | пункт списку |  |
| On this section | ford | індикатор |  |
| On this section | Write a field note | кнопка | `Д8` |
| Weather | Weather | заголовок зони |  |
| Weather | +9 °C · rain from 15:00 · wind 7 m/s | текст |  |
| футер | Trails and terrain: Lantmäteriet (CC0) for Sweden, Kartverket (CC BY 4.0) for Norway. Weather: met.no Locationforecast. Transport: Trafikverket, Entur. Huts — type, key, beds, season — from the static fields of the public DNT and STF object schema. | атрибуція |  |

#### `day-offline.html` — офлайн

| Зона | Рядок | Тип | Позначки |
|---|---|---|---|
| — | ‹ Plan | кнопка |  |
| — | Day | заголовок екрана |  |
| — | Day 3 · Wed 19 August | заголовок екрана |  |
| Leg | Leg | заголовок зони |  |
| Leg | ‹ Day 2 | кнопка |  |
| Leg | Day 4 › | кнопка |  |
| Leg | на всю ширину · тап → на весь екран | заглушка макета | `З1` |
| Leg | map · day 3 · Alesjaure → Tjäktja · ford before the hut · offline pack | заглушка макета | `З1` |
| Leg | на всю ширину | заглушка макета | `З1` |
| Leg | profile · +260 m | заглушка макета | `З1` |
| Leg | distance | підпис |  |
| Leg | 13 km | пункт списку |  |
| Leg | ascent | підпис |  |
| Leg | +260 m | пункт списку |  |
| Leg | walking | підпис |  |
| Leg | ~4 h 30 | пункт списку |  |
| Night | Night | заголовок зони |  |
| Night | self-service · 24 beds · no key | підпис |  |
| Night | Tjäktja fjällstuga | пункт списку |  |
| Night | walk-in only | індикатор |  |
| Night | Arrive by 18:00 · logbook: names and membership numbers. | текст |  |
| On this section | On this section | заголовок зони |  |
| On this section | note · 6 Aug · ford knee-deep | підпис |  |
| On this section | Bridge before Tjäktja washed out | пункт списку |  |
| On this section | ford | індикатор |  |
| On this section | streams every 2–3 km | підпис |  |
| On this section | Water | підпис |  |
| On this section | 8 km of boardwalk, 5 km of rock | підпис |  |
| On this section | Surface | підпис |  |
| Weather | Weather | заголовок зони |  |
| Weather | Forecast from 14 August, 07:00 — from the offline pack. | текст |  |
| футер | Trails and terrain: Lantmäteriet (CC0) for Sweden, Kartverket (CC BY 4.0) for Norway. Weather: met.no Locationforecast. Transport: Trafikverket, Entur. Huts — type, key, beds, season — from the static fields of the public DNT and STF object schema. | атрибуція |  |

#### `day-seasonal.html` — сезонна норма

| Зона | Рядок | Тип | Позначки |
|---|---|---|---|
| — | ‹ Plan | кнопка |  |
| — | Day | заголовок екрана |  |
| — | Day 3 · Wed 19 August | заголовок екрана |  |
| Leg | Leg | заголовок зони |  |
| Leg | ‹ Day 2 | кнопка |  |
| Leg | Day 4 › | кнопка |  |
| Leg | на всю ширину · тап → на весь екран | заглушка макета | `З1` |
| Leg | map · day 3 · Alesjaure → Tjäktja · ford before the hut | заглушка макета | `З1` |
| Leg | на всю ширину | заглушка макета | `З1` |
| Leg | profile · +260 m | заглушка макета | `З1` |
| Leg | distance | підпис |  |
| Leg | 13 km | пункт списку |  |
| Leg | ascent | підпис |  |
| Leg | +260 m | пункт списку |  |
| Leg | walking | підпис |  |
| Leg | ~4 h 30 | пункт списку |  |
| Night | Night | заголовок зони |  |
| Night | self-service · 24 beds · no key | підпис |  |
| Night | Tjäktja fjällstuga | пункт списку |  |
| Night | walk-in only | індикатор |  |
| Night | Arrive by 18:00 · logbook: names and membership numbers. | текст |  |
| On this section | On this section | заголовок зони |  |
| On this section | note · 6 Aug · ford knee-deep | підпис |  |
| On this section | Bridge before Tjäktja washed out | пункт списку |  |
| On this section | ford | індикатор |  |
| On this section | streams every 2–3 km | підпис |  |
| On this section | Water | підпис |  |
| On this section | 8 km of boardwalk, 5 km of rock | підпис |  |
| On this section | Surface | підпис |  |
| Weather | Weather | заголовок зони |  |
| Weather | August seasonal normal: +6…+14 °C, rain every third day. The forecast appears 10 days before you set off. | текст |  |
| футер | Trails and terrain: Lantmäteriet (CC0) for Sweden, Kartverket (CC BY 4.0) for Norway. Weather: met.no Locationforecast. Transport: Trafikverket, Entur. Huts — type, key, beds, season — from the static fields of the public DNT and STF object schema. | атрибуція |  |

### Plans · Book

#### `booking.html` — успіх

| Зона | Рядок | Тип | Позначки |
|---|---|---|---|
| — | ✕ Close | кнопка | `Т1` |
| — | Book | заголовок екрана | `Д2` |
| — | Night 4 · Sälka fjällstuga | заголовок екрана |  |
| What you’re booking | What you’re booking | заголовок зони |  |
| What you’re booking | 2 beds · member rate · 900 SEK for two | підпис |  |
| What you’re booking | Thu 20 August | підпис |  |
| What you’re booking | Sat 15 August, 12:00 | підпис |  |
| What you’re booking | Deadline | підпис |  |
| What you’re booking | in 2 days | індикатор |  |
| Order | Order | заголовок зони |  |
| Order | booked · STF-2026-118442 | підпис |  |
| Order | 1 · Alesjaure | підпис |  |
| Order | now | підпис |  |
| Order | 2 · Sälka | підпис |  |
| Order | next | індикатор |  |
| Order | after Sälka | підпис |  |
| Order | 3 · Kebnekaise fjällstation | підпис |  |
| Order | STF takes payment for one night before the next. | текст |  |
| Book | Book | заголовок зони | `Д2` |
| Book | Booking and payment happen in STF’s system. Dates and number of beds are filled in. | текст |  |
| Book | Open STF booking ↗ | кнопка | `Д2` |
| After booking | After booking | заголовок зони |  |
| After booking | Booking number | підпис поля |  |
| After booking | STF-2026-… | плейсхолдер поля |  |
| After booking | Confirmation or ticket — photo or PDF | підпис поля |  |
| After booking | Save | кнопка |  |
| футер | Trails and terrain: Lantmäteriet (CC0) for Sweden, Kartverket (CC BY 4.0) for Norway. Weather: met.no Locationforecast. Transport: Trafikverket, Entur. Huts — type, key, beds, season — from the static fields of the public DNT and STF object schema. | атрибуція |  |

### Plans · Gear

#### `gear.html` — успіх

| Зона | Рядок | Тип | Позначки |
|---|---|---|---|
| — | ‹ Plan | кнопка |  |
| — | Gear | заголовок екрана | `Д6` |
| — | Gear | заголовок екрана | `Д6` |
| Pack | Pack | заголовок зони |  |
| Pack | three self-service nights — no blankets | підпис |  |
| Pack | sleeping bag −5 °C | підпис |  |
| Pack | rain on days 3 and 4 | підпис |  |
| Pack | rain jacket | підпис |  |
| Pack | 11 km of boggy ground | підпис |  |
| Pack | gaiters | підпис |  |
| Pack | buy | індикатор |  |
| Pack | wind 12 m/s on the pass | підпис |  |
| Pack | waterproof gloves | підпис |  |
| Pack | buy | індикатор |  |
| Pack | shared | підпис |  |
| Pack | first-aid kit | підпис |  |
| Pack | 19 of 23 packed · 11.4 kg | текст |  |
| My gear | My gear | заголовок зони | `Д6` |
| My gear | Open inventory | кнопка | `С3` `Д6` |
| футер | Trails and terrain: Lantmäteriet (CC0) for Sweden, Kartverket (CC BY 4.0) for Norway. Weather: met.no Locationforecast. Transport: Trafikverket, Entur. Huts — type, key, beds, season — from the static fields of the public DNT and STF object schema. | атрибуція |  |

### Plans · My trips

#### `plans.html` — успіх

| Зона | Рядок | Тип | Позначки |
|---|---|---|---|
| — | My trips | заголовок екрана | `Д5` |
| — | My trips | заголовок екрана | `Д5` |
| Upcoming | Upcoming | заголовок зони |  |
| Upcoming | photo · Kungsleden · path along Abiskojaure lake | заглушка макета | `З1` |
| Upcoming | in 4 days | індикатор |  |
| Upcoming | 17–22 August · 2 people · 1 of 5 nights booked · 2 tasks | підпис |  |
| Upcoming | photo · Kungsleden · path along Abiskojaure lake Kungsleden · Abisko → Nikkaluokta in 4 days | посилання |  |
| Past | Past | заголовок зони |  |
| Past | 12–15 August 2025 · 47 km | підпис |  |
| Past | Jotunheimen · Gjendesheim → Bygdin | пункт списку |  |
| футер | Trails and terrain: Lantmäteriet (CC0) for Sweden, Kartverket (CC BY 4.0) for Norway. Weather: met.no Locationforecast. Transport: Trafikverket, Entur. Huts — type, key, beds, season — from the static fields of the public DNT and STF object schema. | атрибуція |  |

#### `plans-empty.html` — порожній

| Зона | Рядок | Тип | Позначки |
|---|---|---|---|
| — | My trips | заголовок екрана | `Д5` |
| — | My trips | заголовок екрана | `Д5` |
| Upcoming | Upcoming | заголовок зони |  |
| Upcoming | No trips yet. | текст |  |
| Upcoming | Where to go | кнопка |  |
| Past | Past | заголовок зони |  |
| Past | Your walked trips will stay here. | текст |  |
| футер | Trails and terrain: Lantmäteriet (CC0) for Sweden, Kartverket (CC BY 4.0) for Norway. Weather: met.no Locationforecast. Transport: Trafikverket, Entur. Huts — type, key, beds, season — from the static fields of the public DNT and STF object schema. | атрибуція |  |

### Plans · Share my route

#### `share.html` — успіх

| Зона | Рядок | Тип | Позначки |
|---|---|---|---|
| — | ‹ Plan | кнопка |  |
| — | Share my route | заголовок екрана | `Д1` |
| — | Share my route | заголовок екрана | `Д1` |
| Message | Message | заголовок зони |  |
| Message | Kungsleden, Abisko → Nikkaluokta · 17–22 August | підпис |  |
| Message | Route | підпис |  |
| Message | Abiskojaure · Alesjaure · Tjäktja · Sälka · Kebnekaise | підпис |  |
| Message | Nights | підпис |  |
| Message | day 3 · Alesjaure → Tjäktja | підпис |  |
| Message | Now | підпис |  |
| Message | Kiruna 19:44 · home on the morning of 23 August | підпис |  |
| Message | Back | підпис |  |
| Send | Send | заголовок зони |  |
| Send | Send | кнопка |  |
| Send | Copy link | кнопка |  |
| Send | PDF | кнопка |  |
| футер | Trails and terrain: Lantmäteriet (CC0) for Sweden, Kartverket (CC BY 4.0) for Norway. Weather: met.no Locationforecast. Transport: Trafikverket, Entur. Huts — type, key, beds, season — from the static fields of the public DNT and STF object schema. | атрибуція |  |

### Guide · Guide

#### `guide.html` — успіх

| Зона | Рядок | Тип | Позначки |
|---|---|---|---|
| — | Guide | заголовок екрана | `Р` |
| — | Guide | заголовок екрана | `Р` |
| Search | Search | заголовок зони | `Р` |
| Search | Word, hut or rule | підпис поля | `Р` |
| Search | Norway | кнопка | `Р` |
| Search | Sweden | кнопка | `Р` |
| Search | Both | кнопка | `Р` |
| Articles | Articles | заголовок зони | `Р` |
| Articles | fjällstuga and fjällstation, the 18:00 rule, the logbook | підпис | `Р` |
| Articles | STF huts | пункт списку | `Р` |
| Articles | Sweden | індикатор | `Р` |
| Articles | hut types, the DNT key, the logbook | підпис | `Р` |
| Articles | DNT huts | пункт списку | `Р` |
| Articles | Norway | індикатор | `Р` |
| Articles | cleaning up, shoes off, shared sleeping space, the honour system | підпис | `Р` |
| Articles | Unwritten hut rules | пункт списку | `Р` |
| Articles | nine rules for the mountains | підпис | `Р` |
| Articles | Fjellvett | пункт списку | `Р` |
| Articles | allemansrätten · friluftsloven | підпис | `Р` |
| Articles | Where you can pitch a tent | пункт списку | `Р` |
| футер | Articles: DNT, STF, Naturvårdsverket, Miljødirektoratet — each linked to its primary source. | атрибуція | `Р` |

### Guide · Article

#### `lodging-system.html` — успіх

| Зона | Рядок | Тип | Позначки |
|---|---|---|---|
| — | ‹ Guide | кнопка | `Р` |
| — | Article | заголовок екрана | `Р` |
| — | STF huts | заголовок екрана | `Р` |
| The key point | The key point | заголовок зони | `Р` |
| The key point | A booking buys a bed. Without one you still get a place indoors — possibly a mattress on the floor. No one is turned away. | текст | `Р` |
| Arrival time | Arrival time | заголовок зони | `Р` |
| Arrival time | your booked bed is held for you | підпис | `Р` |
| Arrival time | Before 18:00 | підпис | `Р` |
| Arrival time | the bed isn’t held — a place indoors still is | підпис | `Р` |
| Arrival time | After 18:00 | підпис | `Р` |
| On site | On site | заголовок зони | `Р` |
| On site | names and membership numbers — even after paying online | підпис | `Р` |
| On site | Logbook | підпис | `Р` |
| On site | self-registration if the booking doesn’t cover the whole night | підпис | `Р` |
| On site | Payment | підпис | `Р` |
| On site | clean up after yourself before you leave | підпис | `Р` |
| On site | Cleaning | підпис | `Р` |
| On site | off at the door | підпис | `Р` |
| On site | Shoes | підпис | `Р` |
| Source | Source | заголовок зони | `Р` |
| Source | Svenska Turistföreningen, pages about fjällstuga (in Swedish) · translation | текст | `Р` |
| футер | Svenska Turistföreningen — pages about fjällstuga, in Swedish. | атрибуція | `Р` |

### Safety · First aid

#### `first-aid.html` — успіх

| Зона | Рядок | Тип | Позначки |
|---|---|---|---|
| — | ‹ Safety | кнопка | `Р` |
| — | First aid | заголовок екрана | `Р` |
| — | First aid | заголовок екрана | `Р` |
| Cards | Cards | заголовок зони | `Р` |
| Cards | Røde Kors | підпис | `Р` |
| Cards | Hypothermia | підпис | `Р` |
| Cards | Røde Kors | підпис | `Р` |
| Cards | Cold injury | підпис | `Р` |
| Cards | Röda Korset | підпис | `Р` |
| Cards | Sprains and fractures | підпис | `Р` |
| Cards | Röda Korset | підпис | `Р` |
| Cards | Dehydration and heat | підпис | `Р` |
| If it’s serious | If it’s serious | заголовок зони | `Р` |
| If it’s serious | The cards work offline; a call doesn’t. | текст | `Р` |
| If it’s serious | SOS and coordinates | кнопка | `Р` |
| футер | Texts: Røde Kors (Norway), Röda Korset (Sweden) — verbatim, with attribution. | атрибуція | `Р` |

### Safety · Safety

#### `safety.html` — успіх

| Зона | Рядок | Тип | Позначки |
|---|---|---|---|
| — | Safety | заголовок екрана |  |
| — | Safety | заголовок екрана |  |
| If it’s happening now | If it’s happening now | заголовок зони |  |
| If it’s happening now | SOS · 112 | кнопка |  |
| If it’s happening now | 112 — all services · 113 — medical, Norway | підпис |  |
| If it’s happening now | Numbers | підпис |  |
| If it’s happening now | 67°55′14″N 18°37′02″E · 8 m · 3 min ago | підпис |  |
| If it’s happening now | My coordinates | підпис |  |
| If it’s happening now | Alesjaure — 6.2 km back, then the boat | підпис |  |
| If it’s happening now | Nearest bail-out point | пункт списку | `Д10` |
| If it’s happening now | 2 of 5 · NVE Varsom · 06:00 | підпис |  |
| If it’s happening now | Avalanche danger | підпис |  |
| First aid | First aid | заголовок зони |  |
| First aid | Røde Kors · Röda Korset · work offline | підпис |  |
| First aid | First-aid cards | пункт списку |  |
| Who knows where you are | Who knows where you are | заголовок зони |  |
| Who knows where you are | Share my route | кнопка | `Д1` |
| Before you go | Before you go | заголовок зони |  |
| Before you go | nine rules for the mountains | підпис |  |
| Before you go | Fjellvett | пункт списку |  |
| футер | Trails and terrain: Lantmäteriet (CC0) for Sweden, Kartverket (CC BY 4.0) for Norway. Weather: met.no Locationforecast. Transport: Trafikverket, Entur. Huts — type, key, beds, season — from the static fields of the public DNT and STF object schema. | атрибуція |  |

### Profile · Sign in

#### `account.html` — успіх

| Зона | Рядок | Тип | Позначки |
|---|---|---|---|
| — | ✕ Close | кнопка | `Т1` |
| — | Sign in | заголовок екрана |  |
| — | Sign in to save your trip | заголовок екрана |  |
| Why | Why | заголовок зони |  |
| Why | Bookings and tickets stay in a trip for days — with an account, your trip isn’t lost with your phone. | текст |  |
| Sign in | Sign in | заголовок зони |  |
| Sign in | Continue with Apple | кнопка |  |
| Sign in | Continue with Google | кнопка |  |
| Sign in | Email | підпис поля |  |
| Sign in | you@email | плейсхолдер поля |  |
| Sign in | Next, one notification request — so we can warn you two days before you set off. | текст |  |
| Sign in | Continue without signing in | кнопка |  |
| футер | Trails and terrain: Lantmäteriet (CC0) for Sweden, Kartverket (CC BY 4.0) for Norway. Weather: met.no Locationforecast. Transport: Trafikverket, Entur. Huts — type, key, beds, season — from the static fields of the public DNT and STF object schema. | атрибуція |  |

### Profile · Profile

#### `me.html` — успіх

| Зона | Рядок | Тип | Позначки |
|---|---|---|---|
| — | Profile | заголовок екрана |  |
| — | Profile | заголовок екрана |  |
| Fitness | Fitness | заголовок зони |  |
| Fitness | 24 km · pack 12 kg | підпис |  |
| Fitness | Longest day last year | підпис |  |
| Fitness | Import from Strava | кнопка |  |
| Fitness | Import from Garmin | кнопка |  |
| Mine | Mine | заголовок зони |  |
| Mine | STF · valid until February 2027 | підпис |  |
| Mine | Membership and key | пункт списку |  |
| Mine | 19 items | підпис |  |
| Mine | My gear | пункт списку | `Д6` |
| Mine | 1 upcoming · 1 past | підпис |  |
| Mine | My trips | пункт списку | `Д5` |
| футер | Trails and terrain: Lantmäteriet (CC0) for Sweden, Kartverket (CC BY 4.0) for Norway. Weather: met.no Locationforecast. Transport: Trafikverket, Entur. Huts — type, key, beds, season — from the static fields of the public DNT and STF object schema. | атрибуція |  |

### Profile · Membership and key

#### `membership.html` — успіх

| Зона | Рядок | Тип | Позначки |
|---|---|---|---|
| — | ✕ Close | кнопка | `Т1` |
| — | Membership and key | заголовок екрана |  |
| — | Membership and key | заголовок екрана |  |
| Membership | Membership | заголовок зони |  |
| Membership | Kristin · No. 4471902 · until 28 February 2027 | підпис |  |
| Membership | STF | підпис |  |
| Membership | not a member | підпис |  |
| Membership | Second person | підпис |  |
| Membership | none | індикатор |  |
| Membership | Show card | кнопка |  |
| Membership | Renew at STF ↗ | кнопка |  |
| On this trip | On this trip | заголовок зони |  |
| On this trip | 2,500 SEK per person as a member · 3,700 without | підпис |  |
| On this trip | Nights | підпис |  |
| On this trip | not needed — all huts are unlocked | підпис |  |
| On this trip | Key | підпис |  |
| DNT key | DNT key | заголовок зони |  |
| DNT key | none | підпис |  |
| DNT key | Status | підпис |  |
| DNT key | DNT shops and staffed huts · members only · 100 NOK deposit | підпис |  |
| DNT key | Where to get one | підпис |  |
| футер | Trails and terrain: Lantmäteriet (CC0) for Sweden, Kartverket (CC BY 4.0) for Norway. Weather: met.no Locationforecast. Transport: Trafikverket, Entur. Huts — type, key, beds, season — from the static fields of the public DNT and STF object schema. | атрибуція |  |

### Profile · My gear

#### `my-gear.html` — успіх

| Зона | Рядок | Тип | Позначки |
|---|---|---|---|
| — | ✕ Close | кнопка | `Т1` |
| — | My gear | заголовок екрана | `Д6` |
| — | My gear | заголовок екрана | `Д6` |
| What you have | What you have | заголовок зони |  |
| What you have | sleeping bag −5 °C · mat | підпис |  |
| What you have | Sleep | підпис |  |
| What you have | stove and gas · 1.5 l pot | підпис |  |
| What you have | Kitchen | підпис |  |
| What you have | rain jacket · gaiters | підпис |  |
| What you have | Clothing | підпис |  |
| What you have | GPS watch · power bank | підпис |  |
| What you have | Navigation | підпис |  |
| To buy | To buy | заголовок зони |  |
| To buy | needed on Kungsleden | підпис |  |
| To buy | Waterproof gloves | підпис |  |
| To buy | buy | індикатор |  |
| футер | Trails and terrain: Lantmäteriet (CC0) for Sweden, Kartverket (CC BY 4.0) for Norway. Weather: met.no Locationforecast. Transport: Trafikverket, Entur. Huts — type, key, beds, season — from the static fields of the public DNT and STF object schema. | атрибуція |  |

### Profile · Settings

#### `settings.html` — успіх

| Зона | Рядок | Тип | Позначки |
|---|---|---|---|
| — | ‹ Profile | кнопка |  |
| — | Settings | заголовок екрана |  |
| — | Settings | заголовок екрана |  |
| Account | Account | заголовок зони |  |
| Account | signed in with Apple | підпис |  |
| Account | kristin@email | підпис |  |
| Account | Sign out | кнопка | `Д12` |
| Account | Delete account | кнопка |  |
| Trail mode | Trail mode | заголовок зони |  |
| Trail mode | Turn on when the trip starts | підпис |  |
| Notifications | Notifications | заголовок зони |  |
| Notifications | Changes to your plan | підпис |  |
| Notifications | Booking deadlines | підпис |  |
| Notifications | Time to pack | підпис |  |
| Offline | Offline | заголовок зони |  |
| Offline | Kungsleden · 84.8 MB | підпис |  |
| Offline | Download the pack over Wi-Fi | підпис |  |
| Location | Location | заголовок зони |  |
| Location | when you open the map | підпис |  |
| Location | Position | підпис |  |
| Language | Language | заголовок зони |  |
| Language | English | підпис |  |
| Language | Interface | підпис |  |
| футер | Trails and terrain: Lantmäteriet (CC0) for Sweden, Kartverket (CC BY 4.0) for Norway. Weather: met.no Locationforecast. Transport: Trafikverket, Entur. Huts — type, key, beds, season — from the static fields of the public DNT and STF object schema. | атрибуція |  |

---

## 3. Той самий предмет під різними іменами

### Багатоденний обʼєкт  ·  `С1`

| Слово | Згадок | Екранів | Де саме, якщо рідкісне |
|---|---|---|---|
| **plan** | 68 | 33 |  |
| **trip** | 21 | 10 |  |

### Лінія на місцевості  ·  `С2`

| Слово | Згадок | Екранів | Де саме, якщо рідкісне |
|---|---|---|---|
| **route** | 26 | 12 |  |
| **trail** | 75 | 33 |  |
| **path** | 11 | 9 |  |

### Речі  ·  `С3`

| Слово | Згадок | Екранів | Де саме, якщо рідкісне |
|---|---|---|---|
| **gear** | 12 | 9 |  |
| **pack** | 10 | 5 |  |
| **inventory** | 1 | 1 | `gear.html` |

### Ночівля

| Слово | Згадок | Екранів | Де саме, якщо рідкісне |
|---|---|---|---|
| **hut** | 73 | 32 |  |
| **night** | 32 | 21 |  |
| **stay** | 9 | 9 |  |
| **bed** | 46 | 31 |  |

### Денний відрізок  ·  `С5`

| Слово | Згадок | Екранів | Де саме, якщо рідкісне |
|---|---|---|---|
| **day** | 78 | 22 |  |
| **leg** | 9 | 9 |  |
| **section** | 7 | 6 |  |

### Бронювання

| Слово | Згадок | Екранів | Де саме, якщо рідкісне |
|---|---|---|---|
| **book / booking** | 31 | 12 |  |

**Що з цього справді розбіжність, а що ні.**

- **`plan` / `trip` — 68 проти 21.** Після перекладу це свідомий поділ, а не розкол: «trip» — похід як подія в житті людини («My trips», «About the trip», «Plan again from this trip»), «plan» — документ, який ми склали й міняємо («New plan», «Save plan», «Change plan»). Межа: «trip» ніколи не стоїть на дії, що змінює документ.
- **`route` / `trail` — 26 проти 75, і це не розбіжність.** Два обʼєкти: route — те, що ми пропонуємо; trail — те, по чому йдуть, і джерело даних (Turrutebasen). `path` (11) живе лише в описах фото й місць на стежці.
- **`hut` / `night` / `stay` / `bed` — чотири обʼєкти, а не синоніми**: обʼєкт, календарна ніч, факт ночівлі й одиниця гарантії. Англійська тримає межу краще за українську: «Stay here on night 4» вживає два з них в одному рядку, кожне у своєму значенні.
- **`gear` (12) проти `inventory` (1) і `checklist` (0)** — «Open inventory» єдиний рідкісний напис для того, що всюди зветься gear.
- **`book` (31) — єдине дієслово бронювання.** `reserve`, `lock in`, `secure` трапляються 0 разів: розрізнення «забронювати / закріпити» з української версії в англійській не відтворилось, і воно не потрібне — бронює завжди офіційна система, а ми показуємо, що лишилось забронювати.

### Шапка й заголовок кажуть те саме двічі — 13 з 33

У смузі згори й у `h1` під нею стоїть один і той самий рядок, і людина бачить його двічі підряд. На решті 20 екранів `h1` натомість несе **імʼя самого обʼєкта** — `plan.html` каже «Kungsleden · Abisko → Nikkaluokta» під шапкою «Plan», `day.html` — «Day 3 · Wed 19 August» під шапкою «Day». Тобто в наборі співіснують два різні рішення про те, що робить `h1`: на хабах вкладок повтор свідомий (великий заголовок iOS), на екранах обʼєкта — ні.

| Екран | Рядок |
|---|---|
| `catalogue-empty.html` | Where to go |
| `catalogue.html` | Where to go |
| `first-aid.html` | First aid |
| `gear.html` | Gear |
| `guide.html` | Guide |
| `me.html` | Profile |
| `membership.html` | Membership and key |
| `my-gear.html` | My gear |
| `plans-empty.html` | My trips |
| `plans.html` | My trips |
| `safety.html` | Safety |
| `settings.html` | Settings |
| `share.html` | Share my route |

---

## 4. Та сама дія під різними назвами кнопок

### `Д3` · Скласти план — 2 назв

| Напис на кнопці | Де стоїть |
|---|---|
| Make a plan | `catalogue.html` |
| Plan again from this trip | `plan-past.html` |

### `Д8` · Нотатки з місця — 2 назв

| Напис на кнопці | Де стоїть |
|---|---|
| Field notes | `notes-empty.html`, `notes.html` |
| Write a field note | `day-intrip.html` |

**Кластерів, де одна дія має два й більше написи: 2 з 12.** Жоден не є розбіжністю:

- `Д3` — «Make a plan» — з нуля, «Plan again from this trip» — з минулого походу: дві точки входу однієї дії, і це свідомо
- `Д8` — прочитати нотатки й написати свою — сусідні дії над одним обʼєктом, а не синоніми

### Найгостріше: дві назви однієї дії на одному екрані

Розбіжність між екранами людина може й не помітити. Ці — помітить, бо обидві кнопки видно водночас.

Колонка «Вердикт» — **прочитання, а не факт із розмітки**: кластери зібрані вручну, і частина пар потрапила в один кластер помилково. Позначено обидва випадки, щоб таблиця не видавала групування за знахідку.

| Екран | Кластер | Кнопки, що стоять поруч | Вердикт |
|---|---|---|---|

**Жодної такої пари в наборі немає.**

Два написи однієї дії поруч на одному екрані — найгостріший вид розбіжності, бо людина бачить обидва водночас. Українська версія мала їх кілька («Гарантія на цю ніч» поруч із «Гарантія й доступ на цю ніч»); англійська писалась одразу з одним написом на дію.

---

## 5. Тон, кліше, піктограми

**Окличних знаків у наборі: 0.** Бадьорого тону, «Ой, щось пішло не так», «Вітаємо» і подібного немає — перевірено пошуком по словах. Це рідкість, і її варто зберегти.

**Помилки говорять однаково**: на екранах помилки (`new-plan-error`, `plan-error`) дія одна — `Try again`.

### Піктограми — 12 рядків  ·  `Т1`

| Рядок | Тип | Де | Що це |
|---|---|---|---|
| ✕ Close | кнопка | 9 екранів | функційний хрестик закриття — не порушення |
| offline ✓ | підпис | `plan-error.html`, `plan-past.html`, `plan.html` | ✓/✗ як індикатор — контракт вимагає слова, не значка |

**Хрестик закриття питань не викликає — це системний жест.** `offline ✓` на плані — інша річ: `_next.md` каже «індикатор — слово, не значок», і тут слово є («offline»), а галочка лише підсилює його. Лишається під наглядом: у стані `plan-offline` замість неї стоїть дата пакета, тобто значок і слово вже роз’їхались по станах.

---

## 6. Заглушки

### `З1` · Заглушки макета — 52 рядків

Опис того, що буде в рамці замість самої рамки: карта, профіль висоти, фото. Це **нормально для вайрфрейма** і зникне з появою реального вмісту — але це текст, який зараз видно на екрані, тому він у таблиці й позначений.

| Екран | Рядок |
|---|---|
| `catalogue-empty.html` | на весь екран під пошуком · аркуш зверху |
| `catalogue-empty.html` | map · Sweden · no route lines · huts closed for February |
| `catalogue.html` | на весь екран під пошуком · аркуш зі списком зверху |
| `catalogue.html` | map · Sweden · preset route lines · start/finish points: stations, trailheads, huts · own route drawn: Abisko Turiststat |
| `catalogue.html` | photo · Kungsleden · path along Abiskojaure lake |
| `catalogue.html` | photo · Kebnekaise valley from the trail |
| `catalogue.html` | photo · Padjelanta plateau, Sami huts |
| `catalogue.html` | photo · Besseggen ridge, Jotunheimen |
| `catalogue.html` | photo · Hardangervidda plateau at Finse |
| `day-intrip.html` | на всю ширину · позиція на вимогу |
| `day-intrip.html` | map · you are here · 4 km from Alesjaure · ford before the hut |
| `day-offline.html` | на всю ширину · тап → на весь екран |
| `day-offline.html` | map · day 3 · Alesjaure → Tjäktja · ford before the hut · offline pack |
| `day-offline.html` | на всю ширину |
| `day-offline.html` | profile · +260 m |
| `day-seasonal.html` | на всю ширину · тап → на весь екран |
| `day-seasonal.html` | map · day 3 · Alesjaure → Tjäktja · ford before the hut |
| `day-seasonal.html` | на всю ширину |
| `day-seasonal.html` | profile · +260 m |
| `day.html` | на всю ширину · тап → на весь екран |
| `day.html` | map · day 3 · Alesjaure → Tjäktja · ford before the hut |
| `day.html` | на всю ширину |
| `day.html` | profile · +260 m |
| `hut.html` | на всю ширину |
| … | *ще 28 — усі позначені `З1` у таблиці розділу 2* |

### `З2` · Текст замість змісту — 0 рядків

Це вже інше: тут стоїть **опис того, що напишуть**, у місці, де людина чекає сам зміст. Таких рядків 0 на 0 екранах.

| Екран | Зона | Рядок |
|---|---|---|

**`first-aid.html` тримає назви карток, а не їхній текст** («Hypothermia · Røde Kors»). Це свідомо: медичний зміст ми не авторуємо, його ліцензію ще не з'ясовано (`CLAUDE.md`, відкриті питання), тож картка називає джерело замість того, щоб вигадувати зміст.
---

## 7. Рядки, які пише автор статей  ·  `Р`

Це **не продуктовий мікрокопі**, і зводити його до тієї самої таблиці правди не можна: у нього інший автор, інша довжина речення і, головне, **інший правовий статус** — частина його нам не належить і цитується з атрибуцією.

| Екран | Рядків | Слів | Чий це текст |
|---|---|---|---|
| `first-aid.html` | 16 | 48 | **не наш** — Røde Kors / Röda Korset, цитата з атрибуцією; медичний зміст ми не авторуємо |
| `guide.html` | 21 | 72 | наш вступний шар над чужим змістом; статті — DNT (норвезькою), переклад наш |
| `lodging-system.html` | 22 | 109 | шаблон статті довідника; зміст — DNT, STF, Naturvårdsverket, Miljødirektoratet, з джерелом у кожній |

**Редакційний текст за межами цих екранів** після перебудови 2026-09-23 зведено до коротких фактів на самих полях: ночівля на дні й хижі каже «прийти до 18:00 · логбук», а не переказує правила.

---

## 8. Технічний жаргон і службові назви  ·  `Ж` — 0 рядків

| Рядок | Тип | Де | Що саме витекло |
|---|---|---|---|

---

## 9. Що це дає, поки рішень ще нема

Позначено 175 рядків із 953. Жодного не змінено.

Що видно тільки з такої таблиці:

1. **Переклад прибрав більшість розбіжностей, бо писався як один текст.** Українська версія накопичувала синоніми з кожною перебудовою; англійська — один прохід по всіх 33 сторінках, тому кластери `Д*` зараз здебільшого порожні. Словники вище тримають відомі синоніми, щоб дрейф було видно з першого ж рядка.
2. **Стани розходяться з базою частіше, ніж базові екрани між собою.** `_audit.py` стежить, щоб у стану був той самий перелік зон, що й у бази, — але за словами всередині зон стежить лише ця таблиця.
3. **`plan` / `trip` — єдина межа, яку варто записати в глосарій.** Вона свідома (документ проти події), але тримається тільки на звичці; наступний, хто писатиме текст, має знати її явно.

