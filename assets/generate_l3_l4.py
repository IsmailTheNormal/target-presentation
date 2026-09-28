#!/usr/bin/env python3
import os
import json
from generate_all_5_6 import make_presentation, make_worksheet, BASE_DIR

# ==========================================
# LESSON 3: GAME LORE & WORLDBUILDING
# ==========================================

l3_slides = """
<section class="slide is-on" data-phase="Kirish|Вступление|Opening" data-time="0–3">
  <div class="title-wrap">
    <div class="eyebrow">Vibecoding · <span data-ru="урок 3 · 5-6 классы" data-en="lesson 3 · grades 5-6">3-dars · 5-6 sinflar</span></div>
    <div class="title-meta">
      <span><b lang="uz">Fan:</b><span data-ru=" IT / Vibecoding" data-en=" IT / Vibecoding"> IT / Vibecoding</span><b lang="ru">Предмет:</b><span lang="ru"> IT / Vibecoding</span><b lang="en">Subject:</b><span lang="en"> IT / Vibecoding</span></span>
      <span><b lang="uz">Hafta:</b><span data-ru=" 1" data-en=" 1"> 1</span><b lang="ru">Неделя:</b><span lang="ru"> 1</span><b lang="en">Week:</b><span lang="en"> 1</span></span>
    </div>
    <h1 data-ru="Гейм-Лор и Создание Игровых Миров" data-en="Game Lore & Worldbuilding Architecture">O'yin Olamini Yaratish va Game Lore</h1>
    <p class="lede" data-ru="Как создаются миры в Roblox, Genshin и Minecraft? Проектируем лор, биомы, фракции и сюжетные квесты с помощью ИИ." data-en="How are worlds in Roblox, Genshin, and Minecraft built? Architecting lore, factions, biomes, and questlines with AI.">Roblox, Genshin va Cyberpunk olamlari qanday to'qiladi? AI yordamida o'yin xaritasi, fraksiyalar, afsonalar va kvestlar arxitekturasini yaratamiz.</p>
  </div>
</section>

<section class="slide" data-phase="Geym-Lor|Что такое Лор|Game Lore" data-time="3–7">
  <div class="eyebrow"><span data-ru="Фундамент игры" data-en="Game Foundations">Geymdev Poydevori</span></div>
  <h2 data-ru="Что такое Лор: История и Законы Игрового Мира" data-en="What is Game Lore: History & Laws of the Virtual World">O'yin Loresi (Lore) — O'yinning Ichki Tarixi va Qonunlari</h2>
  <p data-ru="Лор (Lore) — это душа игры. Без интересной предыстории любая игра быстро надоедает." data-en="Lore is the soul of any game. Without a captivating narrative, players quickly lose interest.">Lore — bu o'yinning ruhi. Agar qiziqarli o'tmish va sirli olam bo'lmasa, o'yin juda tez zerikarli bo'lib qoladi:</p>
  <div class="cols c2" style="margin-top:15px;">
    <div class="box">
      <h3 style="color:var(--ink-2);" data-ru="Обычная игра (без лора)" data-en="Game Without Lore">Oddiy O'yin (Loresiz)</h3>
      <p data-ru="Игрок просто прыгает по блокам и собирает монеты. Нет цели, нет тайны. Через 10 минут игру удаляют." data-en="Just running and jumping on blocks with no mystery or goal. Players abandon it in 10 minutes.">O'yinchi shunchaki bloklar ustida sakraydi va tanga yig'adi. Maqsad va sir yo'q. 10 daqiqadan so'ng o'yin unutiladi.</p>
    </div>
    <div class="box" style="border-left:4px solid var(--green);">
      <h3 style="color:var(--green);" data-ru="Мир с Глубоким Лором" data-en="World with Deep Lore">Katta Olam (Boy Lore Bilan)</h3>
      <p data-ru="Каждая руина, меч и персонаж имеют 500-летнюю историю! Игроки годами исследуют тайны и обсуждают теории." data-en="Every ruin, weapon, and NPC carries a 500-year mystery. Players explore and theorize for years.">Har bir xaroba, qurol va personajning 500 yillik siri bor! O'yinchilar olam sirlarini oylab qiziqib o'rganishadi.</p>
    </div>
  </div>
</section>

<section class="slide" data-phase="Dunyo Qurish|Мироустройство|Worldbuilding" data-time="7–11">
  <div class="eyebrow"><span data-ru="4 Столпа Мира" data-en="4 Pillars of Worldbuilding">Worldbuilding Ustunlari</span></div>
  <h2 data-ru="4 Столпа Построения Игрового Мира с ИИ" data-en="4 Pillars of Game Worldbuilding with AI">AI Bilan Olam Qurishning 4 Asosiy Ustuni</h2>
  <p data-ru="Когда мы просим ИИ создать мир, мы описываем 4 обязательных элемента:" data-en="When instructing an AI worldbuilder, we always define 4 foundational pillars:">AI bilan yangi olam yaratishda quyidagi 4 ta ustunni aniq belgilab berish zarur:</p>
  <div class="grid" style="display:grid; grid-template-columns:1fr 1fr; gap:12px; margin-top:10px;">
    <div class="box">
      <h3 style="color:var(--accent);" data-ru="1. Биомы и Карта 🗺️" data-en="1. Biomes & Map 🗺️">1. Biomlar va Xarita 🗺️</h3>
      <p data-ru="Где происходит действие? Неоновый мегаполис, кислотные пустоши, летающие парящие острова." data-en="Where does it take place? Neon metropolises, toxic wastelands, or skybound floating islands.">Voqealar qayerda sodir bo'ladi? Neon megapolis, kislotali g'orlar, osmondagi suzuvchi orollar.</p>
    </div>
    <div class="box">
      <h3 style="color:var(--accent);" data-ru="2. Фракции и Гильдии ⚔️" data-en="2. Factions & Guilds ⚔️">2. Fraksiyalar va Guruhlar ⚔️</h3>
      <p data-ru="Кто здесь живет? Кибер-самураи, гильдия космических торговцев, мятежные роботы-шахтеры." data-en="Who inhabits this realm? Cyber-samurais, space merchants, or rogue miner automatons.">Bu yerda kimlar yashaydi? Kiber-samuraylar, kosmik savdogarlar, isyonchi konchi-robotlar.</p>
    </div>
    <div class="box">
      <h3 style="color:var(--accent);" data-ru="3. Ресурсы и Валюта 💎" data-en="3. Resources & Economy 💎">3. Resurslar va Valyuta 💎</h3>
      <p data-ru="За что все борются? Кристаллы плазмы, чистая вода, древние квантовые чипы." data-en="What is valuable? Plasma crystals, purified water reserves, or ancient quantum microchips.">Hamma nima uchun kurashadi? Plazma kristallari, toza suv zaxirasi, qadimiy kvant chiplari.</p>
    </div>
    <div class="box">
      <h3 style="color:var(--accent);" data-ru="4. Главный Конфликт ⚡" data-en="4. Core Conflict ⚡">4. Katta Konflikt (Moqaro) ⚡</h3>
      <p data-ru="Что угрожает миру? Энергетический кризис, восстание темного ИИ или падение метеорита." data-en="What threatens survival? An energy blackout, rogue AI overlord, or cosmic catastrophe.">Dunyoni nima xavf ostiga qo'ymoqda? Energiya inqirozi, yovuz AI yoki kosmik falokat.</p>
    </div>
  </div>
</section>

<section class="slide" data-phase="Kvest Arxitekturasi|Архитектура Квестов|Quest Design" data-time="11–15">
  <div class="eyebrow"><span data-ru="Механика Квестов" data-en="Quest Architecture">Kvest Arxitekturasi</span></div>
  <h2 data-ru="Архитектура Квестов: От Завязки до Награды" data-en="Quest Architecture: Hook, Hazard & Loot">RPG Kvestlari: Qiziqarli Missiyalar Qanday Yaratiladi?</h2>
  <p data-ru="Игроки не любят скучные задания 'принеси 10 яблок'. Отличный квест строится по формуле 3 шагов:" data-en="Gamers despise boring 'fetch 10 apples' tasks. A memorable quest requires 3 distinct beats:">O'yinchilar "10 ta olma olib kel" kabi zerikarli topshiriqlarni yoqtirmaydi. Haqiqiy kvest 3 bosqichdan iborat:</p>
  <ul class="rules">
    <li><span class="t" data-ru="<b>1. Завязка (Hook):</b> Неожиданный сигнал тревоги, сломанный робот на обочине или зашифрованная дискета." data-en="<b>1. The Hook:</b> An emergency distress beacon, a broken automaton on the road, or an encrypted data disk."><b>1. Chaqiruv (Trigger / Hook):</b> Favqulodda SOS signali, yo'ldagi yarador kiber-skaut yoki shifrlangan chip.</span></li>
    <li><span class="t" data-ru="<b>2. Препятствие (Hazard):</b> Охраняемый лазерный периметр, взлом пароля или ядовитая песчаная буря." data-en="<b>2. The Hazard:</b> A laser-guarded perimeter, cyber terminal puzzle, or toxic radiation storm."><b>2. To'siq (Sinov / Hazard):</b> Lazerli qo'riqlash tizimi, terminalni buzish yoki xavfli kiber-bo'ron.</span></li>
    <li><span class="t" data-ru="<b>3. Награда (Loot & XP):</b> Легендарный плазменный меч, 500 очков опыта и пропуск в секретный сектор." data-en="<b>3. The Reward (Loot & XP):</b> Legendary plasma blade, 500 XP, and a security pass to the restricted sector."><b>3. Mukofot (Loot / XP):</b> Afsonaviy plazma qilichi, 500 tajriba ochkosi (XP) va yopiq sektorga ruxsatnoma.</span></li>
  </ul>
</section>

<section class="slide" data-phase="Prompting|Промптинг|World Prompt" data-time="15–19">
  <div class="eyebrow"><span data-ru="Лаборатория Лора" data-en="Lore Engineering">Geymdev Prompti</span></div>
  <h2 data-ru="Промпт для Генерации Игрового Мира в Нейросети" data-en="Engineering the Worldbuilding Lore Prompt">AI ga Dunyo Yaratishni Buyurish: Professional Prompt</h2>
  <div class="box" style="background:var(--panel); border-left:5px solid var(--green); padding:16px;">
    <p style="font-family:monospace; font-size:0.9em; line-height:1.5;" data-ru="&quot;ТЫ — Главный Нарративный Дизайнер в научно-фантастической RPG 'Aero-Siti'. ТВОЯ ЗАДАЧА — разработать лор летающего города в 2150 году. ОПИШИ: 1) Почему город парит в облаках (2 научные причины)? 2) Две соперничающие фракции: Небесные Пилоты против Подземных Механиков. 3) Первый сюжетный квест для новичка: поломка антигравитационного реактора. СТИЛЬ: динамичный, краткий, без сказочных клише.&quot;" data-en="&quot;YOU ARE the Lead Narrative Designer for a sci-fi RPG named 'Aero-City'. YOUR MISSION: Architect the lore of a floating sky metropolis in the year 2150. DETAIL: 1) Why does the city hover in the clouds (2 technical reasons)? 2) Two rival factions: Sky Pilots vs Underground Mechanics. 3) The starter quest for new players: anti-gravity engine failure. TONE: gritty, dynamic, zero fairy tale tropes.&quot;">
      "SEN — 'Aero-Siti' ilmiy-fantastik RPG o'yinining Bosh Geym-Dizaynerisan. VAZIFANG — 2150-yildagi osmonda suzib yuruvchi shahar loresini yaratish. TALABLAR: 1) Shahar nega osmonda suzadi? (2 ta ilmiy sabab). 2) Raqobatlashuvchi 2 ta fraksiya: Uchuvchilar va Mexaniklar. 3) Yangi o'yinchi uchun 1-kvest: antigravitatsiya reaktori buzilishi. USLUB: tezkor, zamonaviy va ertaknamo gaplarsiz!"
    </p>
  </div>
  <p style="margin-top:12px; font-size:0.95em;" data-ru="Обратите внимание: мы задаем научную причину, чтобы мир выглядел правдоподобно!" data-en="Notice: We demand scientific justification so the game universe feels believable and grounded!">E'tibor bering: biz sun'iy intellektga ilmiy mantiq talabini qo'ydik, shunda o'yin olami ishonarli chiqadi!</p>
</section>

<section class="slide" data-phase="Tanlovlar|Ветвление Сюжета|Branching Narrative" data-time="19–23">
  <div class="eyebrow"><span data-ru="Интерактивный Сюжет" data-en="Branching Lore">Syujet Tarmoqlanishi</span></div>
  <h2 data-ru="Ветвление Сюжета: Выборы и Их Последствия" data-en="Branching Narrative: Player Agency & Consequences">Chiziqli Emas Syujet: O'yinchi Tanlovi Oqibatlari</h2>
  <p data-ru="Современные игры дают игроку выбор. Одно решение меняет судьбу целой фракции:" data-en="Modern gaming empowers player choices. A single decision alters faction diplomacy and world state:">Eng zo'r o'yinlarda tanlov o'yinchining o'zida bo'ladi. Har bir qaror olam taqdirini o'zgartiradi:</p>
  <div class="cols c2" style="margin-top:15px;">
    <div class="box">
      <h3 style="color:var(--accent);" data-ru="Путь А: Мирный Договор 🤝" data-en="Branch A: Diplomacy 🤝">A-Yo'l: Tinchlik Shartnomasi 🤝</h3>
      <p data-ru="Игрок чинит реактор вместе с Механиками. Город спасен, но Пилоты теряют власть и объявляют бойкот. Открывается торговая база." data-en="Player fixes the reactor alongside Mechanics. Metropolis is saved, but Sky Pilots launch an embargo. Unlocks Black Market.">O'yinchi reaktorni Mexaniklar bilan tuzatadi. Shahar qutqariladi, ammo Uchuvchilar g'azablanadi. Yangi savdo bazasi ochiladi.</p>
    </div>
    <div class="box" style="border-left:4px solid var(--green);">
      <h3 style="color:var(--green);" data-ru="Путь B: Тайный Штурм ⚡" data-en="Branch B: Covert Assault ⚡">B-Yo'l: Yashirin Hujum ⚡</h3>
      <p data-ru="Игрок крадет реакторное ядро для Пилотов. Получает редкий реактивный джетпак, но нижний сектор погружается во тьму." data-en="Player steals the core for Sky Pilots. Earns an experimental jetpack, but plunged the lower sector into a power blackout.">O'yinchi reaktor yadrosini Uchuvchilarga topshiradi. Noyob reaktiv ranets oladi, biroq quyi shahar zulmatga g'arq bo'ladi.</p>
    </div>
  </div>
</section>

<section class="slide" data-phase="Lore Boshqaruvi|Библия Лора|Lore Bible" data-time="23–27">
  <div class="eyebrow"><span data-ru="Контроль Логики" data-en="Lore Consistency">Mantiq Nazorati</span></div>
  <h2 data-ru="Lore Bible: Чтобы ИИ Не Путал Законы Мира" data-en="The Lore Bible: Keeping Game Continuity Intact">Lore Bible: AI Dunyo Qonunlarini Unutmasligi Uchun</h2>
  <p data-ru="Если вы не запишете правила, нейросеть начнет путать имена и придумывать противоречия. Создайте документ 'Lore Bible':" data-en="Without written ground rules, AI models start hallucinating contradictions. Maintain a 'Lore Bible':">Agar qoidalarni bitta hujjatga yozib bormasangiz, AI qahramonlar ismini adashtirib, mantiqsiz gaplar to'qiy boshlaydi:</p>
  <ul class="rules">
    <li><span class="t" data-ru="<b>1. Глоссарий терминов:</b> Точные названия валюты, оружия и городов (чтобы AI не выдумывал новые на ходу)." data-en="<b>1. Lore Glossary:</b> Exact names of cities, factions, and currency so AI never invents mismatched terms."><b>1. Terminlar Lug'ati:</b> Valyuta, qurollar va shaharlarning qat'iy nomlari (AI yangi soxta nomlar to'qimasligi uchun).</span></li>
    <li><span class="t" data-ru="<b>2. Законы физики и магии:</b> Если в вашем киберпанке нет магии, AI категорически запрещено добавлять драконов." data-en="<b>2. Physical Laws:</b> If your universe is hard sci-fi, AI is strictly forbidden from spawning fantasy dragons."><b>2. Fizika va Dunyo Qonunlari:</b> Agar kiberpankda sehr bo'lmasa, AI ga sehrgar va ajdaho qo'shish qat'iyan taqiqlanadi.</span></li>
    <li><span class="t" data-ru="<b>3. Хронология событий:</b> Что произошло 100 лет назад, 10 лет назад и вчера. События должны быть логичными." data-en="<b>3. Timeline:</b> What happened a century ago vs yesterday. History must remain seamless and coherent."><b>3. Tarixiy Xronologiya:</b> 100 yil oldin nima bo'lgan, kecha nima yuz berdi. Voqealar zanjiri uzilmasligi shart.</span></li>
  </ul>
</section>

<section class="slide" data-phase="O'yin Etikasi|Этика и Рейтинг|Game Ethics & ESRB" data-time="27–31">
  <div class="eyebrow"><span data-ru="Этика Геймдева" data-en="Game Ethics">Xavfsiz O'yin Dizayni</span></div>
  <h2 data-ru="Этика и Рейтинг: Создаем Игру без Токсичности" data-en="Game Ethics: Safe Worlds & Anti-Toxicity">O'yin Reytingi: Har Bir Yosh Uchun Do'stona Olam</h2>
  <p data-ru="Roblox и крупные игровые платформы строго блокируют миры с агрессией, травлей и токсичностью:" data-en="Roblox and top gaming engines enforce strict rules against toxicity, bullying, and graphic violence:">Roblox va xalqaro platformalar shafqatsizlik va haqoratli o'yinlarni zudlik bilan bloklaydi:</p>
  <div class="cols c2" style="margin-top:15px;">
    <div class="box">
      <h3 style="color:var(--accent);" data-ru="Запрещено в Геймдеве 🚫" data-en="Prohibited in Gamedev 🚫">Taqiqlanadi 🚫</h3>
      <p data-ru="Токсичные диалоги, дискриминация игроков, пропаганда жестокости и вымогательство реальных денег." data-en="Toxic dialogues, cyber-bullying, gory violence, and predatory real-money scams.">O'yinchilarni haqoratlovchi dialoglar, kiber-zo'ravonlik va firibgarlik yo'llari bilan hisobni o'g'irlash.</p>
    </div>
    <div class="box" style="border-left:4px solid var(--green);">
      <h3 style="color:var(--green);" data-ru="Знак Качества (Fair Play) ✅" data-en="Fair Play Quality Mark ✅">Sifatli O'yin Standarti ✅</h3>
      <p data-ru="Умные головоломки, командное сотрудничество, честные награды за мастерство и захватывающие приключения." data-en="Clever puzzles, cooperative multiplayer, skill-based rewards, and epic storylines.">Mantiqiy boshqotirmalar, do'stona jamoaviy yordam, halol yutuqlar va qiziqarli sarguzashtlar.</p>
    </div>
  </div>
</section>

<section class="slide" data-phase="Amaliyot|Практика в парах|Team Challenge" data-time="31–36">
  <div class="eyebrow"><span data-ru="Командный Спринт" data-en="Team Sprint">Jamoaviy Challenge</span></div>
  <h2 data-ru="Геймдев-Спринт: Свой Игровой Мир за 5 Минут!" data-en="Gamedev Sprint: Architect Your World in 5 Minutes!">Geymdev Sprint: 5 Daqiqada Yangi Olam Loresi!</h2>
  <p data-ru="Объединитесь в пары (Сценарист + Тестировщик) и создайте фундамент своего игрового мира:" data-en="Team up in pairs (Narrative Designer + Playtester) and establish your game's lore backbone:">Juftlikda ishlang (Geym-Dizayner + Tester) va AI yordamida yangi o'yin loyihangiz poydevorini quring:</p>
  <div class="cols c2" style="margin-top:15px;">
    <div class="box">
      <h3 style="color:var(--green);" data-ru="Шаг 1: Генерация (3 мин)" data-en="Step 1: Generation (3 min)">1-Qadam: Generatsiya (3 daq)</h3>
      <p data-ru="Напишите промпт: придумайте название мира, 2 биома и 2 соперничающие фракции. Запустите генерацию в ИИ." data-en="Draft your prompt: invent world name, 2 biomes, and 2 rival factions. Run AI generation.">AI ga prompt yozing: olam nomi, 2 ta biom va 2 ta dushman fraksiya. AI javobini oling.</p>
    </div>
    <div class="box" style="border-left:4px solid var(--accent);">
      <h3 style="color:var(--accent);" data-ru="Шаг 2: Тест на прочность (2 мин)" data-en="Step 2: Stress Test (2 min)">2-Qadam: Mantiq Sinovi (2 daq)</h3>
      <p data-ru="Напарник задает каверзный вопрос по физике мира: 'А почему в этом мире не замерзает лава?' Проверьте связность лора!" data-en="Partner tests logic consistency: 'Why doesn't plasma freeze in this biome?' Ensure zero plot holes!">Sherigingiz kutilmagan savol beradi: "Bu biomda reaktor qanday ishlaydi?" Mantiqda xato yo'qligini tekshiring!</p>
    </div>
  </div>
</section>

<section class="slide" data-phase="Uy vazifasi|Домашка|Homework" data-time="36–40">
  <div class="eyebrow"><span data-ru="Домашнее задание" data-en="Homework">Uyga vazifa</span></div>
  <h2 data-ru="Домашка: Создай 'Game Lore Bible' для Своего Проекта" data-en="Homework: Engineer Your Game's Lore Bible">Uy vazifasi: O'z O'yiningizning "Game Lore Bible" Hujjatini Yaratish</h2>
  <div class="hw">
    <div style="display:grid; gap:16px">
      <p class="lede" data-ru="Создайте мини-документ игрового лора для игры вашей мечты (Roblox, RPG, Survival):" data-en="Build a mini Game Lore document for your dream game (Roblox, RPG, Survival):">Orzuingizdagi o'yin (Roblox, RPG, Survival) uchun mini "Game Lore Bible" hujjatini yarating:</p>
      <ul class="plain">
        <li><span class="t" data-ru="Напишите описание мира: название, 2 биома, ресурсы и главный конфликт" data-en="Write the world overview: Realm name, 2 distinct biomes, key resources, and core conflict">Olam tavsifi: O'yin nomi, 2 ta asosiy biom, resurslar va dunyodagi bosh konflikt.</span></li>
        <li><span class="t" data-ru="Опишите 2 противоборствующие фракции и создайте 1 разветвленный квест" data-en="Define 2 rival factions and engineer 1 branching quest with 2 possible player choices">2 ta o'zaro raqobatchi fraksiya va 2 xil yechimga ega bo'lgan 1 ta kvest zanjiri.</span></li>
        <li><span class="t" data-ru="Протестируйте лор с ИИ: сгенерируйте диалог с NPC и сделайте скриншот" data-en="Test your lore with AI: generate an in-lore dialogue and attach the screenshot">Lorni AI bilan sinang: qahramon bilan dialog generatsiya qilib, natijasini saqlang.</span></li>
      </ul>
    </div>
    
    <div class="grade">
      <div class="tag" data-ru="10-балльная шкала" data-en="10 point rubric">10 ballik mezon</div>
      <div class="g"><span><span data-ru="Структурированный лор мира" data-en="Structured World Lore">Mantiqiy dunyo loresi</span></span><b>4</b></div>
      <div class="g"><span><span data-ru="Разветвленный квест (2 пути)" data-en="Branching Questline">Tarmoqlangan kvest</span></span><b>4</b></div>
      <div class="g"><span><span data-ru="Сдано вовремя" data-en="On-time Submission">Vaqtida topshirilgani</span></span><b>2</b></div>
      <div class="g"><span><b><span data-ru="Итого" data-en="Total">Jami</span></b></span><b>10</b></div>
    </div>
  </div>
</section>
"""

l3_notes = {
  "uz": [
    "Darsni boshlash: O'quvchilardan sevimli o'yinlari (Roblox, Genshin, Minecraft) nima uchun qiziq ekanligini so'rang. Mavzu: Lore va Dunyo qurish.",
    "Tushuntiring: Lore — o'yinning ichki tarixi va qonunlari. Nega oddiy sakrash o'yinlari tez unutiladi-yu, boy lorega ega o'yinlar yillar davomida o'ynaladi?",
    "Worldbuildingning 4 ustuni: Biomlar, Fraksiyalar, Resurslar va Konflikt. Har bir element o'yin mexanikasiga qanday bog'lanishini ko'rsating.",
    "Kvest arxitekturasi: Trigger (boshlanish), Hazard (to'siq) va Loot (mukofot). O'quvchilarga '10 ta olma ter' kabi ibtidoiy kvestlardan qochishni o'rgating.",
    "Professional prompt: AI ga aniq rollar va ilmiy mantiq talabini berish. Prompt matnini doskada birgalikda tahlil qiling.",
    "Chiziqli bo'lmagan syujet: O'yinchi qarorlari dunyo holatini o'zgartirishi (Branching Narrative). A va B yo'llarini misol qilib ko'rsating.",
    "Lore Bible tushunchasi: AI faktlarni adashtirib yubormasligi uchun lug'at va xronologiya yuritish muhimligi.",
    "O'yin etikasi: Roblox va xalqaro o'yin standartlari. Toksiklik va kiber-zo'ravonlikka yo'l qo'ymaslik qoidalari.",
    "Amaliy sprint: O'quvchilar juftlikda ishlaydi (biri dizayner, biri tester). 5 daqiqada yangi olam yaratib, mantiqiy savollar bilan sinaydilar.",
    "Uy vazifasi: O'z o'yinlari uchun mini 'Game Lore Bible' tuzish. 10 ballik baholash mezonini aniq tushuntiring."
  ],
  "ru": [
    "Вводная часть: Спросите учеников, почему их любимые игры (Roblox, Genshin, Minecraft) не надоедают. Тема урока: Гейм-лор и создание миров.",
    "Объясните понятие Лора: внутренняя история и законы вселенной. Почему простые кликеры забываются, а глубокие миры живут годами.",
    "4 столпа создания мира: Биомы, Фракции, Ресурсы и Конфликт. Разберите пример каждого элемента на популярных играх.",
    "Архитектура квестов: Завязка (Hook), Препятствие (Hazard) и Награда (Loot). Учите избегать скучных шаблонных квестов.",
    "Промптинг для лора: Как задавать нейросети ограничения и научную основу, чтобы мир получался реалистичным и кинематографичным.",
    "Нелинейный сюжет: Ветвление истории и последствия выборов игрока. Разберите разницу между Путем А и Путем В.",
    "Концепция Lore Bible: Зачем разработчики ведут документ правил, чтобы ИИ не путал факты и не генерировал галлюцинации.",
    "Этика геймдева: Правила платформ (Roblox, Steam), запрет токсичности, кибербуллинга и честная механика наград.",
    "Практический спринт: Работа в парах (Сценарист + Тестировщик). За 5 минут создать ядро мира и протестировать на логические дыры.",
    "Домашнее задание: Создать свой мини-документ 'Game Lore Bible'. Разъясните критерии 10-балльной оценки."
  ],
  "en": [
    "Introduction: Hook students by discussing why hits like Roblox, Genshin, and Minecraft stay popular for years. Topic: Game Lore & Worldbuilding.",
    "Define Lore: The internal history and natural laws of the game universe. Contrast disposable runners with deep, atmospheric worlds.",
    "The 4 Pillars of Worldbuilding: Biomes, Factions, Resources, and Core Conflict. Demonstrate how each shapes actual gameplay loop.",
    "Quest Architecture: Hook, Hazard, and Loot. Coach students to steer clear of repetitive fetch quests in favor of dramatic dilemmas.",
    "Worldbuilding Prompt Engineering: Instructing AI with clear technical boundaries and scientific coherence to prevent fantasy clichés.",
    "Branching Narrative: Player agency and cascading consequences. Break down how Choice A vs Choice B alters faction reputation.",
    "The Lore Bible concept: Why studio game designers maintain strict continuity documents to keep generative models on track.",
    "Gamedev Ethics: Platform standards (Roblox, Steam), anti-toxicity guidelines, and crafting fair, inclusive challenge systems.",
    "Hands-on Sprint: Pair challenge (Narrative Designer + QA Tester). Rapidly prototype a game world core and stress-test its logic in 5 minutes.",
    "Homework: Engineer a mini 'Game Lore Bible' for their dream game. Clarify the 10-point rubric breakdown."
  ]
}

# ==========================================
# LESSON 4: GAME CONCEPT ART & VISUAL ASSETS
# ==========================================

l4_slides = """
<section class="slide is-on" data-phase="Kirish|Вступление|Opening" data-time="0–3">
  <div class="title-wrap">
    <div class="eyebrow">Vibecoding · <span data-ru="урок 4 · 5-6 классы" data-en="lesson 4 · grades 5-6">4-dars · 5-6 sinflar</span></div>
    <div class="title-meta">
      <span><b lang="uz">Fan:</b><span data-ru=" IT / Vibecoding" data-en=" IT / Vibecoding"> IT / Vibecoding</span><b lang="ru">Предмет:</b><span lang="ru"> IT / Vibecoding</span><b lang="en">Subject:</b><span lang="en"> IT / Vibecoding</span></span>
      <span><b lang="uz">Hafta:</b><span data-ru=" 1" data-en=" 1"> 1</span><b lang="ru">Неделя:</b><span lang="ru"> 1</span><b lang="en">Week:</b><span lang="en"> 1</span></span>
    </div>
    <h1 data-ru="Гейм-Концепт Арт и Визуальный Дизайн" data-en="Game Concept Art & Visual Design">Game Concept Art va Vizual Dizayn</h1>
    <p class="lede" data-ru="Как создаются скины, биомы и локации в играх? Генерируем концепт-арт для Roblox и RPG через графические нейросети." data-en="How are skins, biomes, and game assets designed? Generating production-ready concept art using modern AI image models.">O'yin qahramonlari, qurollar va fantastik biomlar qanday chiziladi? Midjourney, DALL-E va Stable Diffusion orqali professional geym-art yaratish.</p>
  </div>
</section>

<section class="slide" data-phase="Konsept Art|Что такое Концепт-Арт|Concept Art" data-time="3–7">
  <div class="eyebrow"><span data-ru="Визуальный Геймдев" data-en="Visual Game Dev">Vizual Geymdev</span></div>
  <h2 data-ru="Концепт-арт — Визуальный Паспорт Игры" data-en="Concept Art: The Visual Blueprint of a Game">Concept Art — O'yinning Vizual Pasporti</h2>
  <p data-ru="Концепт-арт — это не просто красивая картинка, а точный чертеж для 3D-моделлеров и программистов:" data-en="Concept art is not merely an illustration; it is the production blueprint for 3D modelers and engine coders:">Concept Art — bu shunchaki chiroyli rasm emas, balki 3D modellashtiruvchilar va dasturchilar uchun aniq chizma:</p>
  <div class="cols c2" style="margin-top:15px;">
    <div class="box">
      <h3 style="color:var(--ink-2);" data-ru="Случайная Картинка" data-en="Random Artwork">Tasodifiy Rasm</h3>
      <p data-ru="Красиво, но ракурс непонятен, детали размыты. По ней невозможно создать 3D-персонажа для Roblox." data-en="Looks pretty, but angles are vague and proportions warped. Impossible to convert into a functional 3D mesh.">Chiroyli ko'rinadi, lekin burchagi noaniq va detallari xira. Uni Roblox yoki Unity uchun 3D model qilib bo'lmaydi.</p>
    </div>
    <div class="box" style="border-left:4px solid var(--green);">
      <h3 style="color:var(--green);" data-ru="Производственный Концепт" data-en="Production Concept Art">Geymdev Concept Art</h3>
      <p data-ru="Видны материалы (металл, стекло), цветовая палитра и точные пропорции со всех сторон!" data-en="Clearly displays surface textures (metal, glass), color palettes, and orthographic proportions.">Materiallar (metall, lazer, mato), ranglar kodi va qahramonning aniq proporsiyalari ko'rsatilgan!</p>
    </div>
  </div>
</section>

<section class="slide" data-phase="Uslublar|Стили Игр|Art Styles" data-time="7–11">
  <div class="eyebrow"><span data-ru="Стили Графики" data-en="Visual Styles">Grafika Turlari</span></div>
  <h2 data-ru="Стили Игровой Графики: Pixel, Low-Poly, Anime, Cyberpunk" data-en="Game Art Styles: Pixel Art, Low-Poly & Cyberpunk">O'yin Art Uslublari: Voxel, Low-Poly, Pixel Art, Cyberpunk</h2>
  <p data-ru="Прежде чем писать промпт, выберите визуальный стиль вашей игры:" data-en="Before prompting generative models, lock in your game's visual art direction:">Prompt yozishdan oldin o'yiningiz uchun mos vizual uslubni tanlang:</p>
  <div class="grid" style="display:grid; grid-template-columns:1fr 1fr; gap:12px; margin-top:10px;">
    <div class="box">
      <h3 style="color:var(--accent);" data-ru="Voxel & Low-Poly 🧊" data-en="Voxel & Low-Poly 🧊">Voxel & Low-Poly 🧊</h3>
      <p data-ru="Стиль Minecraft и классического Roblox. Геометрические блоки, чистые формы, яркие цвета." data-en="The aesthetic of Minecraft and classic Roblox. Geometric meshes, clean forms, vibrant hues.">Minecraft va Roblox uslubi. Bloklar, sodda geometrik shakllar, yorqin va toza ranglar.</p>
    </div>
    <div class="box">
      <h3 style="color:var(--accent);" data-ru="Pixel Art 👾" data-en="Pixel Art 👾">Pixel Art 👾</h3>
      <p data-ru="Ретро-стиль 8-бит / 16-бит для динамичных 2D-платформеров и инди-хитов." data-en="Retro 8-bit and 16-bit styling for responsive 2D platformers and indie hits.">Klassik 8-bit va 16-bit retro uslub. Qiziqarli 2D platformerlar va indie o'yinlar uchun ideal.</p>
    </div>
    <div class="box">
      <h3 style="color:var(--accent);" data-ru="Cyberpunk & Sci-Fi 🏙️" data-en="Cyberpunk & Sci-Fi 🏙️">Cyberpunk & Sci-Fi 🏙️</h3>
      <p data-ru="Неоновое свечение, темный металл, голограммы и ночной мегаполис будущего." data-en="Luminescent neon highlights, weathered metal, holograms, and rainy dystopian skylines.">Neon chiroqlar, qoramtir metall, gologrammalar va kelajak megapolisi estetikasi.</p>
    </div>
    <div class="box">
      <h3 style="color:var(--accent);" data-ru="Stylized 3D (Anime) ✨" data-en="Stylized 3D (Anime) ✨">Stylized 3D (Anime) ✨</h3>
      <p data-ru="Стиль Genshin Impact и Fortnite. Мягкое освещение, выразительные персонажи и яркая магия." data-en="The look of Genshin Impact and Fortnite. Cel-shaded lighting, emotive faces, vibrant magic.">Genshin Impact va Fortnite uslubi. Yumshoq yorug'lik, chiroyli qahramonlar va jozibali ranglar.</p>
    </div>
  </div>
</section>

<section class="slide" data-phase="Prompt Formulasi|Формула Промпта|Prompt Formula" data-time="11–15">
  <div class="eyebrow"><span data-ru="Формула Промпта" data-en="Visual Formula">AI Rasm Formulasi</span></div>
  <h2 data-ru="5 Элементов Идеального Промпта для Нейросети" data-en="The 5-Element Visual Prompt Formula">AI Rasm Prompti Formulasi: 5 Ta Asosiy Element</h2>
  <p data-ru="Чтобы получить профессиональный игровой арт, промпт должен содержать 5 ключевых параметров:" data-en="To generate studio-grade game concept art, structure your prompt with 5 key parameters:">AI tasodifiy rasm chizmasligi uchun promptni 5 ta qismdan tashkil topgan formula bo'yicha tuzamiz:</p>
  <ul class="rules">
    <li><span class="t" data-ru="<b>1. Объект (Subject):</b> Кто или что на арте? (Кибер-лиса механик, плазменный меч, парящий остров)." data-en="<b>1. Subject:</b> Who or what is depicted? (Cyber-mechanic fox, plasma blade, floating island)."><b>1. Obyekt (Subject):</b> Kim yoki nima tasvirlanadi? (Kiber-mexanik tulki, plazma qilichi, suzuvchi orol).</span></li>
    <li><span class="t" data-ru="<b>2. Стиль (Art Style):</b> Low-poly 3D render, pixel art, cyberpunk, stylized anime cel-shading." data-en="<b>2. Art Style:</b> Low-poly 3D render, pixel art, cyberpunk aesthetic, stylized anime cel-shading."><b>2. Uslub (Art Style):</b> Low-poly 3D render, retro pixel art, cyberpunk yoki stilizatsiya qilingan anime.</span></li>
    <li><span class="t" data-ru="<b>3. Освещение (Lighting):</b> Неоновый синий свет, закатное солнце, кинематографичные тени." data-en="<b>3. Lighting:</b> Volumetric neon backlighting, warm sunset rim light, high-contrast shadows."><b>3. Yoritish (Lighting):</b> Neon ko'k yorug'lik, quyosh botishi nurlari, kinematografik soyalar.</span></li>
    <li><span class="t" data-ru="<b>4. Ракурс камеры (Camera):</b> Изометрия, фронтальный вид (front view), широкий угол (wide angle)." data-en="<b>4. Camera Angle:</b> Isometric perspective, front model view, wide-angle cinematic shot."><b>4. Kamera Burchagi (Camera):</b> Izometrik ko'rinish, to'g'ridan-to'g'ri (front view) yoki keng burchak.</span></li>
    <li><span class="t" data-ru="<b>5. Качество и Движок (Engine):</b> Unreal Engine 5 render, 8k resolution, clean sharp edges, octane render." data-en="<b>5. Quality & Engine:</b> Unreal Engine 5 render, 8k resolution, crisp clean geometry, octane render."><b>5. Dvigatel va Sifat (Engine):</b> Unreal Engine 5 render, 8k tiniqlik, o'tkir qirralar, octane render.</span></li>
  </ul>
</section>

<section class="slide" data-phase="Character Sheet|Лист Персонажа|Character Sheet" data-time="15–19">
  <div class="eyebrow"><span data-ru="Модельный лист" data-en="Model Sheet">3D Modelga Tayyorgarlik</span></div>
  <h2 data-ru="Character Sheet: Персонаж со Всех Ракурсов" data-en="Character Sheet: Multi-Angle Turnaround">Character Turnaround: Personajni Har Tomondan Ko'rish</h2>
  <p data-ru="В геймдеве один ракурс бесполезен. Разработчики всегда генерируют <b>Character Turnaround Sheet</b>:" data-en="In production, a single snapshot is useless. Game artists always produce a <b>Character Turnaround Sheet</b>:">O'yin ishlab chiqarishda bitta burchak yetarli emas. Geym-dizaynerlar har doim <b>Character Sheet</b> generatsiya qiladi:</p>
  <div class="box" style="background:var(--panel); border-left:5px solid var(--green); padding:16px;">
    <p style="font-family:monospace; font-size:0.9em; line-height:1.5;" data-ru="&quot;Character model sheet turnaround, futuristic cyborg ninja scout, front view, side view, back view, orthographic projection, stylized low-poly 3D game asset for Roblox Studio, clean plain white background, vibrant colors, Unreal Engine 5 render --no shadows, blurry&quot;" data-en="&quot;Character model sheet turnaround, futuristic cyborg ninja scout, front view, side view, back view, orthographic projection, stylized low-poly 3D game asset for Roblox Studio, clean plain white background, vibrant colors, Unreal Engine 5 render --no shadows, blurry&quot;">
      "Character model sheet turnaround, futuristic cyborg ninja scout, front view, side view, back view, orthographic projection, stylized low-poly 3D game asset for Roblox Studio, clean plain white background, vibrant colors, Unreal Engine 5 render --no shadows, blurry"
    </p>
  </div>
  <p style="margin-top:12px; font-size:0.95em;" data-ru="Такой лист позволяет 3D-моделлеру сразу смоделировать персонажа в Blender или Roblox Studio!" data-en="This turnaround enables 3D artists to instantly extrude and rig the mesh in Blender or Roblox Studio!">Bunday chizma orqali 3D ustasi personajni darhol Blender yoki Roblox Studio'da yasay oladi!</p>
</section>

<section class="slide" data-phase="AI Xatolari|Артефакты ИИ|Visual Glitches" data-time="19–23">
  <div class="eyebrow"><span data-ru="Ошибки Генерации" data-en="Quality Control">Sifat Nazorati</span></div>
  <h2 data-ru="Артефакты ИИ: Лишние Пальцы и Размытые Текстуры" data-en="AI Artifacts: Hands, Fingers & Physics Glitches">AI Glitch va Artefaktlar: 6 Barmoqli Qo'llar Muammosi</h2>
  <p data-ru="Нейросети рисуют по пиксельной статистике, а не по анатомии. Из-за этого возникают визуальные баги:" data-en="AI generates through probabilistic pixel diffusion, not skeletal anatomy. This causes visual anomalies:">AI inson anatomiyasini bilmaydi, u faqat piksellar ehtimolini hisoblaydi. Shu sababli xatolar yuzaga keladi:</p>
  <div class="cols c2" style="margin-top:15px;">
    <div class="box">
      <h3 style="color:var(--accent);" data-ru="Типичные Баги ИИ ⚠️" data-en="Typical AI Glitches ⚠️">Odatiy AI Xatolari ⚠️</h3>
      <p data-ru="6-7 пальцев на руке, летающие в воздухе мечи, сросшиеся глаза или размытые несимметричные лица." data-en="6 or 7 fingers on hands, floating detached weapons, fused eyes, or distorted facial asymmetry.">Qo'lda 6-7 ta barmoq, havoda osilib qolgan qilichlar, birlashib ketgan ko'zlar va qiyshiq simmetriya.</p>
    </div>
    <div class="box" style="border-left:4px solid var(--green);">
      <h3 style="color:var(--green);" data-ru="Решение: Negative Prompt 🛡️" data-en="Fix: Negative Prompts 🛡️">Yechim: Negative Prompt 🛡️</h3>
      <p data-ru="Добавляйте в конец промпта запрещенные вещи: <code>--no deformed hands, extra fingers, bad anatomy, blurry, watermark</code>" data-en="Append strict negative constraints: <code>--no deformed hands, extra fingers, bad anatomy, blurry, watermark</code>">Prompt oxiriga nimalar bo'lmasligi kerakligini yozing: <code>--no deformed hands, extra fingers, blurry, glitch</code></p>
    </div>
  </div>
</section>

<section class="slide" data-phase="Asset Dizayn|Игровые Ассеты|Game Assets" data-time="23–27">
  <div class="eyebrow"><span data-ru="Предметы и Иконки" data-en="Items & UI Icons">Inventar va UI</span></div>
  <h2 data-ru="Игровые Ассеты: Мечи, Зелья, Порталы и Иконки UI" data-en="Game Assets: Weapons, Potions, Portals & Inventory Icons">O'yin Assetlari: Qilichlar, Portallar va Inventar Ikonkalari</h2>
  <p data-ru="В игре нужны десятки предметов. Как сгенерировать целую сетку иконок для инвентаря?" data-en="Every game demands dozens of item icons. How do we generate inventory grids and sprite sheets?">O'yinda o'nlab buyumlar kerak bo'ladi. Ularning ikonkalari qanday generatsiya qilinadi?</p>
  <ul class="rules">
    <li><span class="t" data-ru="<b>Спрайт-сетка (Sprite Sheet):</b> Промпт: <i>'Set of 9 sci-fi weapon icons, game UI asset sheet, isometric, flat solid background'</i>." data-en="<b>Sprite Sheet:</b> Prompt: <i>'Set of 9 sci-fi weapon icons, game UI asset sheet, isometric, flat solid background'</i>."><b>Ikonkalar To'plami (Sprite Sheet):</b> Prompt: <i>'Set of 9 sci-fi weapon icons, game UI asset sheet, isometric, flat solid background'</i>.</span></li>
    <li><span class="t" data-ru="<b>Однородный фон (Solid BG):</b> Всегда указывайте <i>'isolated on pure white background'</i>, чтобы легко удалить фон." data-en="<b>Solid Background:</b> Always specify <i>'isolated on pure white background'</i> for easy 1-click background removal."><b>Bir xil Fon (Solid BG):</b> Fonni oson o'chirish uchun har doim <i>'isolated on pure white background'</i> deb yozing.</span></li>
    <li><span class="t" data-ru="<b>Единая палитра:</b> Используйте одинаковый стиль для всех предметов, чтобы игра выглядела гармонично." data-en="<b>Unified Palette:</b> Maintain identical style keywords across all assets to keep the game visually coherent."><b>Yagona Rang Palitrasi:</b> Barcha buyumlar uchun bitta uslub so'zlarini qo'llang, shunda o'yin tartibli ko'rinadi.</span></li>
  </ul>
</section>

<section class="slide" data-phase="Mualliflik|Авторские Права|Ethics & Copyright" data-time="27–31">
  <div class="eyebrow"><span data-ru="Авторское Право" data-en="Art Ethics">Geymdev Etikasi</span></div>
  <h2 data-ru="ИИ и Авторские Права: Как Использовать Арт Честно" data-en="AI Ethics: Copyright & Respecting Human Artists">Rassomlar Mehnati va AI: Mualliflik Huquqi Nimani Aytadi?</h2>
  <p data-ru="ИИ обучался на миллионах картин людей-художников. Как юному разработчику использовать арт этично?" data-en="AI engines were trained on human artists' work. How do ethical indie developers use generative art?">Sun'iy intellekt millionlab tirik rassomlarning rasmlari asosida o'rgangan. Undan qanday to'g'ri foydalanamiz?</p>
  <div class="cols c2" style="margin-top:15px;">
    <div class="box">
      <h3 style="color:var(--accent);" data-ru="Неправильно ❌" data-en="Unethical ❌">Noto'g'ri Yondashuv ❌</h3>
      <p data-ru="Копировать стиль одного живого художника без разрешения и утверждать: 'Это на 100% нарисовал я сам'." data-en="Copying a specific living artist's unique name without consent and pretending 'I hand-painted this myself.'">Tirik rassomning nomini ruxsatsiz ishlatish va 'Buni o'zim qo'lda chizdim' deb yolg'on gapirish.</p>
    </div>
    <div class="box" style="border-left:4px solid var(--green);">
      <h3 style="color:var(--green);" data-ru="Профессионально ✅" data-en="Professional ✅">Professional Yondashuv ✅</h3>
      <p data-ru="Использовать ИИ для прототипов, мудбордов и концепт-идей, честно указывать использование ИИ." data-en="Using AI for rapid prototyping, moodboards, and indie concepts while crediting AI tooling honestly.">AI dan g'oyalar, prototip va ilhom olish uchun foydalanish hamda 'AI yordamida yaratildi' deb ochiq ko'rsatish.</p>
    </div>
  </div>
</section>

<section class="slide" data-phase="Amaliyot|Практика в парах|Concept Lab" data-time="31–36">
  <div class="eyebrow"><span data-ru="Арт-Спринт" data-en="Art Sprint">Kreativ Sprint</span></div>
  <h2 data-ru="Арт-Спринт: Концепт-Арт Персонажа за 5 Минут" data-en="Art Sprint: Generate Character Concept Art in 5 Minutes">Geym-Art Sprint: O'z Qahramoningiz Concept Artini Yarating</h2>
  <p data-ru="Создайте визуальный образ главного героя для вашей игры по формуле 5 параметров:" data-en="Design the visual concept art for your game's main hero using our 5-element formula:">5 qismli formula yordamida o'z o'yiningiz bosh qahramoni uchun vizual konsept yarating:</p>
  <div class="cols c2" style="margin-top:15px;">
    <div class="box">
      <h3 style="color:var(--green);" data-ru="Шаг 1: Конструктор Промпта (2 мин)" data-en="Step 1: Formula Prompt (2 min)">1-Qadam: Formula Tuzish (2 daq)</h3>
      <p data-ru="Соедините: [Персонаж] + [Стиль Low-Poly/Cyberpunk] + [Неоновый свет] + [Изометрия] + [Unreal Engine 5]." data-en="Assemble: [Subject] + [Low-Poly / Cyberpunk Style] + [Neon Rimlight] + [Isometric] + [Unreal 5 Render].">Birlashtiring: [Personaj] + [Low-Poly/Cyberpunk uslubi] + [Neon nuri] + [Front/Izometrik burchak] + [Sifat].</p>
    </div>
    <div class="box" style="border-left:4px solid var(--accent);">
      <h3 style="color:var(--accent);" data-ru="Шаг 2: Очистка от Артефактов (3 мин)" data-en="Step 2: Artifact Check (3 min)">2-Qadam: Artefaktlarni Tozalash (3 daq)</h3>
      <p data-ru="Проверьте пальцы, оружие и симметрию. Добавьте Negative Prompt при необходимости и выберите лучший вариант!" data-en="Inspect fingers, attached gear, and symmetry. Add Negative Prompts if warped and pick the best shot!">Barmoqlar, qurol va yuzni tekshiring. Xatolar bo'lsa, Negative Prompt qo'shib, eng toza variantni tanlang!</p>
    </div>
  </div>
</section>

<section class="slide" data-phase="Uy vazifasi|Домашка|Homework" data-time="36–40">
  <div class="eyebrow"><span data-ru="Домашнее задание" data-en="Homework">Uyga vazifa</span></div>
  <h2 data-ru="Домашка: Создай Визуальный Пак Своего Персонажа" data-en="Homework: Engineer a Game Concept Art Pack">Uy vazifasi: O'yin Qahramoni va Biomining Vizual Paketini Yaratish</h2>
  <div class="hw">
    <div style="display:grid; gap:16px">
      <p class="lede" data-ru="Создайте визуальный концепт-пак для своего игрового проекта (Roblox, RPG):" data-en="Build a visual concept pack for your game project (Roblox, RPG):">O'z o'yin loyihangiz (Roblox, RPG) uchun vizual konsept-paket yarating:</p>
      <ul class="plain">
        <li><span class="t" data-ru="Сгенерируйте концепт главного персонажа по 5-элементной формуле промпта" data-en="Generate your hero concept art using the 5-element prompt formula">5 qismli formula yordamida bosh qahramonning to'liq concept artini yarating.</span></li>
        <li><span class="t" data-ru="Создайте арт одного биома (локации) или 2 игровых предметов (оружие/артефакт)" data-en="Generate 1 game biome landscape or 2 distinct inventory items (weapon/artifact)">1 ta o'yin biomi (manzara) yoki 2 ta inventar buyumi (qurol/artefakt) suratini oling.</span></li>
        <li><span class="t" data-ru="Опишите использованные стили, негативные промпты и сохраните финальные арты" data-en="Document the art style, negative prompts used, and compile the final art showcase">Tanlangan uslub, negative promptlar va natijalarni qisqacha yozib, rasmlarni saqlang.</span></li>
      </ul>
    </div>
    
    <div class="grade">
      <div class="tag" data-ru="10-балльная шкала" data-en="10 point rubric">10 ballik mezon</div>
      <div class="g"><span><span data-ru="Персонаж по 5-элементной формуле" data-en="5-Element Character Art">5 qismli formula bilan personaj</span></span><b>4</b></div>
      <div class="g"><span><span data-ru="Арт биома / предметов" data-en="Biome / Items Asset Art">Biom yoki buyumlar konsepti</span></span><b>4</b></div>
      <div class="g"><span><span data-ru="Сдано вовремя" data-en="On-time Submission">Vaqtida topshirilgani</span></span><b>2</b></div>
      <div class="g"><span><b><span data-ru="Итого" data-en="Total">Jami</span></b></span><b>10</b></div>
    </div>
  </div>
</section>
"""

l4_notes = {
  "uz": [
    "Darsni boshlash: O'quvchilarga mashhur o'yinlar konsept-artlarini ko'rsating. Mavzu: O'yin qahramonlari va olamini vizual tasvirlash.",
    "Concept Art nima: Tasodifiy rasm bilan geymdev konsepti farqi (burchaklar, proporsiyalar va teksturalar).",
    "Vizual uslublar: Voxel/Low-poly (Roblox), Pixel art, Cyberpunk va Stylized 3D (Genshin/Fortnite). Har bir uslubning kayfiyati.",
    "Prompt formulasi: 5 ta element (Obyekt + Uslub + Yoritish + Kamera + Dvigatel/Sifat). Prompt tuzish algoritmini tushuntiring.",
    "Character Turnaround Sheet: Nega 3D modelerga qahramonning old, yon va orqa tomoni bitta kadrda kerakligi.",
    "AI artefaktlari: Qo'llar, barmoqlar va deformatsiyalar nega paydo bo'ladi? Negative promptlar yordamida ularni tuzatish.",
    "O'yin assetlari va UI ikonkalari: Sprite sheetlar va bir xil oq fon (solid background) orqali fonni tozalash qulayligi.",
    "Mualliflik huquqi va etika: Tirik rassomlar uslubini o'g'irlamaslik, AI dan ilhom va prototip vositasi sifatida foydalanish.",
    "Amaliy mashg'ulot: O'quvchilar 5 qismli formuladan foydalanib o'z qahramonlarini generatsiya qiladi va xatolarni filtrlaydi.",
    "Uy vazifasi: Qahramon va biom/buyum vizual paketini tayyorlash. 10 ballik baholash mezonini eslating."
  ],
  "ru": [
    "Вводная часть: Покажите концепт-арты известных игр. Объясните цель: создать визуальный образ для своего игрового проекта.",
    "Что такое Концепт-Арт: Разница между случайной картинкой и чертежом для 3D-моделлеров (пропорции, материалы, свет).",
    "Стили графики: Voxel/Low-poly (Roblox), Pixel Art, Cyberpunk и Стилизованное 3D (Fortnite/Genshin).",
    "Формула промпта из 5 частей: Объект + Стиль + Освещение + Ракурс + Движок/Качество. Разберите формулу на доске.",
    "Character Turnaround Sheet: Зачем моделлерам нужен вид спереди, сбоку и сзади на одном листе (ортогональная проекция).",
    "Артефакты нейросетей: Почему ИИ путает пальцы и генерирует лишние мечи. Как писать Negative Prompt.",
    "Игровые ассеты и UI: Создание спрайт-листов иконок оружия/брони на сплошном белом фоне для легкой обтравки.",
    "Этика и авторское право: Уважение к труду художников, честное указание нейросетей и использование для прототипирования.",
    "Практический арт-спринт: Генерация персонажа по формуле в парах, поиск артефактов и очистка негативными промптами.",
    "Домашнее задание: Создать визуальный пак (персонаж + биом/ассет). Напомните критерии 10-балльной оценки."
  ],
  "en": [
    "Introduction: Display iconic industry concept art. Frame the goal: generating cohesive visual assets for their own game project.",
    "What is Concept Art: Contrast artistic wallpaper with actionable technical production sheets (orthographics, materials, lighting).",
    "Game Art Directions: Voxel/Low-poly (Roblox), Pixel Art, Cyberpunk, and Stylized 3D (Fortnite/Genshin Impact aesthetic).",
    "The 5-Element Prompt Formula: Subject + Art Style + Lighting + Camera Angle + Engine/Quality. Walk through concrete examples.",
    "Character Turnaround Sheets: Why 3D modelers require front, profile, and back views aligned on a single sheet for rigging.",
    "Generative Artifacts: Why diffusion models glitch on fingers and topology. Engineering constraint negative prompts.",
    "Game Assets & Inventory UI: Generating sprite sheets for weapons and items isolated on flat solid backgrounds for clean chroma-keying.",
    "Art Ethics & Copyright: Respecting artists, avoiding direct plagiarism, and leveraging AI ethically for indie prototyping.",
    "Hands-on Art Sprint: Crafting formulas in pairs, generating character turnaround assets, and pruning visual glitches.",
    "Homework: Engineer a character and biome/item asset pack. Review the 10-point grading rubric."
  ]
}

# --- WRITE LESSON 3 ---
p3_html = make_presentation("03-dars: Game Lore va O'yin Olamini Yaratish", l3_slides, l3_notes)
with open(os.path.join(BASE_DIR, "03-dars-ai-ertakchi/prezentatsiya.html"), "w", encoding="utf-8") as f:
    f.write(p3_html)
print("Lesson 3 presentation generated successfully.")

# --- WRITE LESSON 4 ---
p4_html = make_presentation("04-dars: Game Concept Art va Vizual Dizayn", l4_slides, l4_notes)
with open(os.path.join(BASE_DIR, "04-dars-ai-multfilm/prezentatsiya.html"), "w", encoding="utf-8") as f:
    f.write(p4_html)
print("Lesson 4 presentation generated successfully.")

