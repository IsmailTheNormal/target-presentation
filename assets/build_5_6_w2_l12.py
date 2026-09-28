#!/usr/bin/env python3
import os, sys
sys.path.insert(0, '/home/dpdp/target/assets')
from curriculum_generator import build_presentation, build_worksheet

BASE = '/home/dpdp/target/classes/5-6-sinf/2-hafta'
l12_dir = os.path.join(BASE, '12-dars-game-jam-mini-loyiha')
os.makedirs(l12_dir, exist_ok=True)

l12_slides = """
<section class="slide is-on" data-phase="Kirish|Вступление|Opening" data-time="0–3">
  <div class="title-wrap">
    <div class="eyebrow">Vibecoding · <span data-ru="урок 12 · 5-6 классы" data-en="lesson 12 · grades 5-6">12-dars · 5-6 sinflar</span></div>
    <div class="title-meta">
      <span><b lang="uz">Fan:</b><span data-ru=" IT / Vibecoding" data-en=" IT / Vibecoding"> IT / Vibecoding</span><b lang="ru">Предмет:</b><span lang="ru"> IT / Vibecoding</span><b lang="en">Subject:</b><span lang="en"> IT / Vibecoding</span></span>
      <span><b lang="uz">Hafta:</b><span data-ru=" 2" data-en=" 2"> 2</span><b lang="ru">Неделя:</b><span lang="ru"> 2</span><b lang="en">Week:</b><span lang="en"> 2</span></span>
    </div>
    <h1 data-ru="Game Jam: Презентация Прототипа Игры и Питчинг" data-en="Game Jam: Mini-Game Prototype Pitch & Demo Day">Game Jam: O'yin Prototipi Taqdimoti va Demo Day</h1>
    <p class="lede" data-ru="Финал 2-й недели! Объединяем 3D-модели, биом, SFX-звуки, умного NPC и HUD в единый 'Паспорт Игры'. Проводим питчинг за 60 секунд и плейтест." data-en="The Week 2 Grand Finale! Uniting 3D assets, biomes, SFX, smart NPCs, and HUD into a unified Game Passport. 60-second pitches and live peer playtesting.">2-hafta finali! Hafta davomida yaratilgan 3D model, biom, SFX ovozlar, aqlli NPC va HUD ni yagona 'O'yin Pasporti'ga jamlaymiz. 60 soniyalik Pitch va Playtest!</p>
  </div>
</section>

<section class="slide" data-phase="Tushuncha|Что такое Game Jam|Game Jam Concept" data-time="3–7">
  <div class="eyebrow"><span data-ru="Фестиваль геймдева" data-en="Indie Festival">Game Jam Madaniyati</span></div>
  <h2 data-ru="Что такое Game Jam: Рождение Игр в Сжатые Сроки" data-en="What is a Game Jam: Rapid Prototyping Under Pressure">Game Jam Nima? Qisqa Vaqtda O'yin Yaratish San'ati</h2>
  <p data-ru="Game Jam — это хакатон для создателей игр. За короткое время разработчики собирают рабочий прототип:" data-en="A Game Jam is a rapid hackathon where game creators build functional prototypes under strict time constraints:">Game Jam — bu geymdev olamidagi eng hayajonli bayram. Bir necha soat ichida noldan ishlovchi o'yin prototipi yig'iladi:</p>
  <div class="cols c2" style="margin-top:15px;">
    <div class="box">
      <h3 style="color:var(--ink-2);" data-ru="Обычная разработка (Годы) 🐢" data-en="Slow Dev Cycle 🐢">Oddiy Loyiha (Yillar davomida) 🐢</h3>
      <p data-ru="Игры делают 5 лет. Добавляют тысячи деталей, тратят миллионы, а в итоге игра может никому не понравиться. Огромный риск." data-en="Studios spend 5 years building massive games. Feature creep delays launch, only to realize the core gameplay was boring.">O'yin ustida 5 yil ishlanadi. Minglab detallar qo'shiladi, oxirida o'yinchilarga yoqmasligi mumkin. Vaqt yo'qotiladi.</p>
    </div>
    <div class="box" style="border-left:4px solid var(--accent);">
      <h3 style="color:var(--accent);" data-ru="Game Jam Метод (Спринт) ⚡" data-en="Game Jam Sprint ⚡">Game Jam Usuli (Tezkor Prototip) ⚡</h3>
      <p data-ru="За считанные дни собирается ядро игры (Core Loop). Друзья тестируют прототип за 5 минут, находят фановые моменты и дают честный фидбек!" data-en="In a sprint, devs assemble the core game loop. Real players test it immediately, identifying the fun factor and providing raw feedback!">Bir necha kunda o'yin yadrosi yig'iladi. Do'stlar darhol sinab ko'radi, qiziqarli joylarini topadi va xatolarni ko'rsatadi!</p>
    </div>
  </div>
</section>

<section class="slide" data-phase="Arxitektura|5 Элементов Игры|5 Game Elements" data-time="7–11">
  <div class="eyebrow"><span data-ru="Интеграция проекта" data-en="Project Integration">5 Asosiy Komponent</span></div>
  <h2 data-ru="5 Столпов Вашего Игрового Прототипа" data-en="The 5 Pillars of Your Playable Game Prototype">Siz Yaratgan O'yinning 5 Ta Tayanch Ustuni</h2>
  <p data-ru="Всю неделю мы по кирпичикам создавали детали полноценной игры. Сегодня они соединяются вместе:" data-en="Throughout Week 2, we architected individual game subsystems. Today, they interlock into one cohesive title:">Hafta davomida biz o'yinning alohida qismlarini yaratdik. Bugun ular yagona butunlikka birlashadi:</p>
  <div class="grid" style="display:grid; grid-template-columns:1fr 1fr; gap:12px; margin-top:10px;">
    <div class="box">
      <h3 style="color:var(--accent);" data-ru="1. 3D Ассеты (Урок 7) 🧊" data-en="1. 3D Assets (L7) 🧊">1. 3D Artefakt va Qurol (7-dars) 🧊</h3>
      <p data-ru="Главное оружие, транспорт или сундук, смоделированный в .GLB формате." data-en="Core weapon, vehicle, or treasure chest exported in watertight .GLB mesh format.">O'yinning asosiy quroli yoki uchar transporti, .GLB formatdagi 3D to'r.</p>
    </div>
    <div class="box">
      <h3 style="color:var(--accent);" data-ru="2. Биом и Карта (Урок 8) 🗺️" data-en="2. Biome & Map (L8) 🗺️">2. Xarita va Skybox Biomi (8-dars) 🗺️</h3>
      <p data-ru="8x8 сетка уровня, зоны старта, препятствий и атмосферный панорамный фон неба." data-en="8x8 layout grid, safe spawn, hazard gauntlet, and atmospheric skybox backdrop.">8x8 katakli xarita, to'siqlar joylashuvi va osmon foni (Skybox).</p>
    </div>
    <div class="box">
      <h3 style="color:var(--accent);" data-ru="3. Аудио-Пак (Урок 9) 🔊" data-en="3. Audio Kit (L9) 🔊">3. SFX va Fon Musiqasi (9-dars) 🔊</h3>
      <p data-ru="Звуки прыжка, сбора монет, сирена урона и зацикленный саундтрек биома." data-en="Sound effects for jumps, coin pickups, hazard damage, and looping soundtrack.">Sakrash, tanga olish va ziyon tovushlari hamda dinamik fon musiqasi.</p>
    </div>
    <div class="box">
      <h3 style="color:var(--accent);" data-ru="4. Умный NPC и HUD (Уроки 10-11) 🧠" data-en="4. NPC & HUD (L10-11) 🧠">4. Aqlli NPC va HUD (10–11-dars) 🧠</h3>
      <p data-ru="Диалоговое дерево квеста с торговцем + эргономичный 4-угольный интерфейс с HP." data-en="Branching quest dialog tree + ergonomic 4-corner HUD interface with HP gauges.">Kvest beruvchi xarakterli personaj + 4 burchak qoidasidagi toza ekran interfeysi.</p>
    </div>
  </div>
</section>

<section class="slide" data-phase="Mexanizm|Искусство Питчинга|Pitching Rules" data-time="11–15">
  <div class="eyebrow"><span data-ru="Презентация за 60 секунд" data-en="Pitching Protocol">60 Soniyalik Pitch</span></div>
  <h2 data-ru="Искусство Питчинга: Как Продать Игру за 60 Секунд" data-en="The Art of Pitching: Selling Your Game in 60 Seconds">60 Soniyada O'yinni Taqdim Etish San'ati (Pitch)</h2>
  <p data-ru="Инвесторы и издатели не слушают часовые лекции. Успешный питч укладывается в 4 шага:" data-en="Publishers and game studios judge pitches in 60 seconds flat. The winning structure:">O'yin nashriyotlari va do'stlaringiz 60 soniyada o'yinga baho berishadi. Muvaffaqiyat formulasi:</p>
  <ul class="rules">
    <li><span class="t" data-ru="<b>1. Захват внимания (Hook 0–15 сек):</b> 'Представьте мир, где весь город парит в облаках, а энергию дают кристаллы!'" data-en="<b>1. The Hook (0–15s):</b> 'Imagine a floating sky metropolis powered solely by unstable plasma crystals!'"><b>1. Qiziqtirish (Hook 0–15 soniya):</b> "Tasavvur qiling, butun shahar osmonda suzib yuradi va energiya kristallari tugamoqda!"</span></li>
    <li><span class="t" data-ru="<b>2. Главная цель (Goal 15–30 сек):</b> 'Игрок берет лазерный джетпак и должен починить реактор, избегая охранных дронов.'" data-en="<b>2. Objective (15–30s):</b> 'Player equips a prototype jetpack to repair the reactor before security droids fire.'"><b>2. Asosiy maqsad (15–30 soniya):</b> "O'yinchi reaktiv ranetsni kiyib, soqchi-dronlardan qochgan holda reaktorni tuzatishi kerak."</span></li>
    <li><span class="t" data-ru="<b>3. Главная фишка (Core Feature 30–45 сек):</b> 'В игре умный NPC-кузнец Болт, который выдает секретные читы, если не грубить!'" data-en="<b>3. Core Innovation (30–45s):</b> 'Features a living AI blacksmith who rewards diplomacy with secret hyper-thrusters!'"><b>3. O'ziga xos qulaylik (30–45 soniya):</b> "O'yinda haqiqiy aqlli NPC temirchi bor — agar unga qo'pol gapirmasangiz, maxfiy qurol beradi!"</span></li>
    <li><span class="t" data-ru="<b>4. Призыв к игре (Call to Action 45–60 сек):</b> 'Сможете ли вы пройти за 60 секунд? Попробуйте прямо сейчас!'" data-en="<b>4. Call to Play (45–60s):</b> 'Can you reach the vault in 60 seconds? Test the prototype right now!'"><b>4. O'ynashga chorlash (45–60 soniya):</b> "Siz ushbu xaritani 60 soniyada o'ta olasizmi? Hozir o'zingiz sinab ko'ring!"</span></li>
  </ul>
</section>

<section class="slide" data-phase="Ko'rsatma|Паспорт Игры|Game Passport" data-time="15–19">
  <div class="eyebrow"><span data-ru="Документация проекта" data-en="Game Design Document">O'yin Pasporti</span></div>
  <h2 data-ru="Паспорт Игры: Визитная Карточка Разработчика" data-en="The Game Design Passport: Indie Developer ID">O'yin Pasporti: Barcha Qismlarni Birlashtirish</h2>
  <div class="box" style="background:var(--panel); border-left:5px solid var(--green); padding:16px;">
    <p style="font-family:monospace; font-size:0.92em; line-height:1.6;" data-ru="<b>НАЗВАНИЕ ИГРЫ:</b> 'Aero-Runner 2150'<br><b>ЖАНР:</b> Sci-Fi Parkour RPG / Roblox Platformer<br><b>ГЛАВНЫЙ ГЕРОЙ:</b> Кибер-курьер 'Нео' с реактивным ранцем (.GLB 3D-модель)<br><b>БИОМ:</b> Парящие острова с лазерными турелями и Skybox заката<br><b>ЗВУКОВОЙ ПАК:</b> Свист турбины (0.4с), звон кристалла (0.8с) + Synthwave Loop<br><b>УМНЫЙ NPC:</b> Торговец 'Винт' (System Prompt + ветвление на 3 ответа)<br><b>ИНТЕРФЕЙС HUD:</b> Шкала энергии (верх-лево), радар (верх-право), ранец (низ-право)" data-en="<b>GAME TITLE:</b> 'Aero-Runner 2150'<br><b>GENRE:</b> Sci-Fi Parkour RPG / Roblox Platformer<br><b>PROTAGONIST / ASSET:</b> Cyber-courier 'Neo' with jetpack (.GLB 3D mesh)<br><b>BIOME:</b> Floating Isles with laser hazards and sunset skydome<br><b>AUDIO SUITE:</b> Thruster whoosh (0.4s), crystal chime (0.8s) + Synthwave Loop<br><b>SMART NPC:</b> Merchant 'Bolt' (System Prompt + 3-branch dialogue tree)<br><b>HUD UI:</b> Energy gauge (Top-Left), radar compass (Top-Right), thruster icon (Bottom-Right)">
      <b>O'YIN NOMI:</b> 'Aero-Runner 2150'<br>
      <b>JANR:</b> Sci-Fi Parkour RPG / Roblox Platformer<br>
      <b>3D ASSET:</b> Kiber-kuryer reaktiv ranetsi (.GLB 3D model)<br>
      <b>BIOM VA XARITA:</b> Lazerli to'siqlarga ega suzuvchi orollar va shom Skybox foni<br>
      <b>AUDIO:</b> Turbina shovqini (0.4s), kristall jiringlashi (0.8s) + Synthwave Loop<br>
      <b>AQLLI NPC:</b> Kiber-savdogar 'Vint' (System Prompt va 3 xil javobli dialog)<br>
      <b>HUD INTERFEYS:</b> Jon/Quvvat (yuqori-chap), minixarita (yuqori-o'ng), qurol (quyi-o'ng)
    </p>
  </div>
  <p style="margin-top:12px; font-size:0.9em; color:var(--ink-2);" data-ru="Заполнение такого паспорта — финальный шаг любого профессионального Game Jam!" data-en="Completing this design passport marks the definitive milestone of any industry Game Jam!">Bunday pasportni to'ldirish har qanday professional Game Jam yakunidagi asosiy qadamdir!</p>
</section>

<section class="slide" data-phase="Sinov|Плейтест и Фидбек|Playtest Ethics" data-time="19–23">
  <div class="eyebrow"><span data-ru="Культура тестирования" data-en="Playtest Protocol">Playtest Qoidalari</span></div>
  <h2 data-ru="Культура Плейтеста: Как Правильно Тестировать Чужую Игру" data-en="Playtesting Ethics: How to Test and Critique Game Prototypes">Playtest Madaniyati: Birovning O'yinini Qanday Sinash Kerak?</h2>
  <p data-ru="Плейтестинг — это проверка игры живым человеком. Главное правило создателя:" data-en="Playtesting reveals unvarnished player reality. The number one rule for developers:">Playtest — o'yinni boshqa odam sinab ko'rishi jarayoni. Geym-dizaynerning eng katta qoidasi:</p>
  <div class="cols c2" style="margin-top:15px;">
    <div class="box">
      <h3 style="color:var(--ink-2);" data-ru="Ошибка создателя (Подсказки) ❌" data-en="Bad Tester: Hovering & Spoiling ❌">Xato Yondashuv (Doim o'rgatish) ❌</h3>
      <p data-ru="Создатель стоит за спиной и каждую секунду командует: 'Жми сюда! Ты не туда идешь!'. Это убивает тест. Игра должна объяснять всё сама." data-en="Dev stands over the shoulder yelling: 'Press E! You are going the wrong way!'. Completely invalidates testing. The game must explain itself.">O'yin muallifi o'rto'g'i boshida turib: "Bu tugmani bos! U yoqqa borma!" deb o'rgataveradi. Bu xato. O'yin o'zi hamma narsani tushuntirishi shart.</p>
    </div>
    <div class="box" style="border-left:4px solid var(--green);">
      <h3 style="color:var(--green);" data-ru="Профессиональный Плейтест (Наблюдение) ✅" data-en="Pro Playtest: Silent Observation ✅">Haqiqiy Playtest (Jim Kuzatish) ✅</h3>
      <p data-ru="Создатель молчит и молча записывает: где игрок застрял? Где ему стало весело? Честный фидбек делает игру шедевром!" data-en="Dev remains silent with notebook: where did the player get confused? Where did they smile? Honest feedback turns games into hits!">Muallif indamay kuzatadi va qog'ozga yozadi: o'yinchi qayerda adashdi? Qayerda kuldi va quvondi? Shu xulosalar o'yinni zo'r qiladi!</p>
    </div>
  </div>
</section>

<section class="slide" data-phase="Vazifa|Миссия урока|Game Jam Lab" data-time="23–27">
  <div class="eyebrow"><span data-ru="Большой финал" data-en="Grand Finale">Amaliy Vazifa</span></div>
  <h2 data-ru="Миссия: Собрать Паспорт и Провести Демо-Питч" data-en="Mission: Finalize Passport & Deliver 60-Second Pitch">Bugungi Vazifa: O'yin Pasportini Yig'ing va 60s Pitch qiling</h2>
  <p data-ru="Финальный спринт 2-й недели: объединяем материалы в рабочий лист и готовимся к защите:" data-en="Week 2 Grand Finale: consolidate all assets into your worksheet and prepare to pitch:">2-haftaning katta finali: barcha 5 ta komponentni varaqaga yozib, 60 soniyalik nutqqa tayyorlaning:</p>
  <ul class="rules">
    <li><span class="t" data-ru="<b>1. Заполнение Паспорта Игры:</b> Название, жанр, описание 3D-модели, биома, звуков и NPC." data-en="<b>1. Game Passport:</b> Complete Title, genre, 3D asset summary, biome, SFX, and smart NPC."><b>1. O'yin Pasportini to'ldirish:</b> O'yin nomi, janri, 3D model, biom, SFX va NPC xususiyatlari.</span></li>
    <li><span class="t" data-ru="<b>2. Репетиция 60-секундного питча:</b> По формуле: Hook -> Цель -> Фишка -> Призыв." data-en="<b>2. Rehearse 60s Pitch:</b> Follow the formula: Hook -> Core Objective -> Unique Feature -> Call to Play."><b>2. 60 soniyalik Pitch mashqi:</b> Hook (Qiziqtirish) -> Maqsad -> O'ziga xos quvvat -> O'ynashga chorlash.</span></li>
    <li><span class="t" data-ru="<b>3. Взаимный плейтест в парах:</b> Поменяться паспортами и оценить концепцию по 3 критериям." data-en="<b>3. Peer Playtest Audit:</b> Swap worksheets and evaluate game viability across 3 criteria."><b>3. O'zaro Playtest:</b> Sherigi bilan varaqalarni almashib, o'yin g'oyasini sinab ko'rish.</span></li>
    <li><span class="t" data-ru="<b>4. Голосование за лучшую игру недели:</b> Выбор победителя в номинациях!" data-en="<b>4. Classroom Awards Vote:</b> Ballot vote for best week 2 game concepts across nominations!"><b>4. Hafta g'oliblarini aniqlash:</b> Sinfda eng zo'r o'yinlar bo'yicha ovoz berish!</span></li>
  </ul>
</section>

<section class="slide" data-phase="Amaliyot|Game Jam Спринт|Game Jam Sprint" data-time="27–31">
  <div class="eyebrow"><span data-ru="Инженерный спринт" data-en="Game Jam Sprint">Jonli Amaliyot · Taymer</span></div>
  <h2 data-ru="Game Jam Спринт: 11 Минут на Сборку и Питч" data-en="Game Jam Sprint: 11 Minutes to Finalize Pitch">Game Jam Ustaxona: 11 Daqiqalik Final Sprint</h2>
  <div class="timer" id="timer">
    <div class="digits" id="digits">11:00</div>
    <div class="ctrls">
      <button id="tstart">Start / Stop</button>
      <button class="ghost" id="treset">Reset</button>
    </div>
  </div>
  <p style="margin-top:15px; font-size:0.95em;" data-ru="Заполните паспорт игры в тетради, откройте свои файлы (модели, арт, звуки) и отрепетируйте 60-секундную речь!" data-en="Complete your game passport on your worksheet, line up your generated assets, and rehearse your 60-second pitch!">Varaqadagi o'yin pasportini to'ldiring, yaratgan fayllaringizni oching va 60 soniyalik nutqingizni tayyorlang!</p>
</section>

<section class="slide" data-phase="Tahlil|Номинации и Награды|Game Awards" data-time="31–36">
  <div class="eyebrow"><span data-ru="Церемония наград" data-en="Award Ceremony">Sinf Ovoz Berishi</span></div>
  <h2 data-ru="Церемония Наград: 3 Главных Номинации Недели" data-en="Game Jam Awards: The 3 Flagship Week 2 Nominations">Target Game Jam: 3 Ta Asosiy Nominatsiya G'oliblari</h2>
  <p data-ru="По результатам питчинга каждый ученик отдает свой голос в одной из 3 категорий:" data-en="Following the 60-second pitches, each student casts a vote across 3 signature categories:">Pitch taqdimotlaridan so'ng sinfdoshlar quyidagi 3 ta nominatsiya bo'yicha ovoz berishadi:</p>
  <div class="cols c3" style="display:grid; grid-template-columns:1fr 1fr 1fr; gap:12px; margin-top:15px;">
    <div class="box" style="border-top:4px solid #FFD700;">
      <h3 style="color:#B78103;" data-ru="🏆 Лучший 3D-Арт" data-en="🏆 Best 3D Visuals">🏆 Eng Zo'r 3D Dizayn</h3>
      <p data-ru="Самая детализированная и чистая 3D-модель + красивый атмосферный Skybox биома." data-en="Most immaculate watertight 3D mesh + cohesive atmospheric biome skybox.">Eng sifatli va teshiklarsiz 3D model hamda jozibali Skybox osmon foni.</p>
    </div>
    <div class="box" style="border-top:4px solid #00E5FF;">
      <h3 style="color:#00838F;" data-ru="⚡ Самый Живой NPC" data-en="⚡ Smartest AI NPC">⚡ Eng Qiziqarli NPC</h3>
      <p data-ru="Персонаж с уникальным голосом, остроумными репликами и не поддающийся взлому." data-en="Living character voice with dynamic quest branching that resisted jailbreaks.">O'ziga xos ovozga ega, aldovlarga uchmagan va zo'r kvest topshiruvchi qahramon.</p>
    </div>
    <div class="box" style="border-top:4px solid #76FF03;">
      <h3 style="color:#2E7D32;" data-ru="🎮 Лучший Геймплей" data-en="🎮 Ultimate Gameplay">🎮 Eng Zo'r Geympley</h3>
      <p data-ru="Идеальная карта 8x8, сочный саунд-дизайн и удобный чистый HUD-интерфейс." data-en="Balanced 8x8 traversal map, punchy SFX feedback, and ergonomic HUD layout.">Mantiqli 8x8 xarita, shirali audio effektlar va qulay HUD interfeysi.</p>
    </div>
  </div>
</section>

<section class="slide" data-phase="Uy vazifasi|Домашнее задание|Homework" data-time="36–40">
  <div class="eyebrow"><span data-ru="Итоги 2-й недели" data-en="Week 2 Finale">Uyga Vazifa va Xulosa</span></div>
  <h2 data-ru="Итоги 2 Недели: Портфолио Игры + 10 Баллов" data-en="Week 2 Capstone: Unified Game Portfolio & 10-Point Rubric">2-Hafta Yakuni: O'yin Portfoliosi va 10 Ballik Baholash</h2>
  <div class="hw" style="display:grid; grid-template-columns:1.4fr 1fr; gap:20px; margin-top:15px;">
    <div class="box" style="border-left:5px solid var(--accent);">
      <h3 style="color:var(--accent);" data-ru="Что нужно сделать:" data-en="Assignment Details:">Bajarilishi shart bo'lgan vazifalar:</h3>
      <ol style="margin-top:8px; padding-left:18px; line-height:1.6;">
        <li data-ru="Собрать все материалы недели в одну папку на Google Drive / компьютере: 2 3D-модели (.GLB), 1 Skybox, 4 аудио-файла (.wav), 1 HUD-спрайт лист." data-en="Consolidate all Week 2 assets into a single project folder: 2 3D models (.GLB), 1 skybox, 4 audio clips (.wav), 1 HUD sprite sheet.">Hafta davomida yaratilgan barcha fayllarni bitta papkaga jamlang: 2 ta 3D model (.GLB), Skybox foni, 4 ta audio (.wav) va HUD ikonkalari.</li>
        <li data-ru="Полностью заполнить 'Паспорт Проекта' в рабочей тетради." data-en="Finalize the complete 'Game Design Passport' in your workbook.">Varaqadagi 'O'yin Loyihasi Pasporti'ni barcha parametrlari bilan to'ldiring.</li>
        <li data-ru="Написать краткий отзыв (3 плюса и 1 совет) по игре соседа." data-en="Author a peer review audit (3 strengths and 1 design recommendation) for your partner.">Sherigingizning o'yini bo'yicha xolis fikr yozing: 3 ta kuchli tomoni va 1 ta maslahat.</li>
      </ol>
    </div>
    <div class="box" style="background:var(--panel);">
      <h3 style="color:var(--green);" data-ru="Критерии Оценки (10 баллов):" data-en="Grading Rubric (10 Points):">Baholash Mezoni (10 ball):</h3>
      <ul style="margin-top:8px; padding-left:16px; line-height:1.6; font-size:0.9em;">
        <li data-ru="<b>3 балла:</b> Полный Паспорт Игры заполнен без пропусков." data-en="<b>3 pts:</b> Complete Game Passport filled out without gaps."><b>3 ball:</b> O'yin pasportidagi barcha qatorlar to'liq to'ldirilgan.</li>
        <li data-ru="<b>4 балла:</b> Все 5 компонентов недели собраны в папку проекта." data-en="<b>4 pts:</b> All 5 week components consolidated in project folder."><b>4 ball:</b> Barcha 5 ta komponent (3D, biom, audio, NPC, HUD) tayyor.</li>
        <li data-ru="<b>3 балла:</b> Проведен успешный 60-секундный питч и плейтест." data-en="<b>3 pts:</b> Delivered 60-second pitch and completed peer playtest."><b>3 ball:</b> 60 soniyalik Pitch nutqi va sherik tekshiruvi bajarilgan.</li>
      </ul>
    </div>
  </div>
</section>
"""

l12_notes = {
  'uz': [
    "Kirish: 2-haftaning katta finali bilan o'quvchilarni tabriklang! Bugun barcha qismlar yagona 'O'yin Pasporti'ga jamlanishini e'lon qiling.",
    "Game Jam nima: Geymdev festivallari qanday o'tishi va bir necha soatda o'yin yadrosini (Core loop) yig'ish madaniyatini tushuntiring.",
    "5 ta komponent: 3D model (7-dars), Biom/Xarita (8-dars), SFX audio (9-dars), Aqlli NPC (10-dars), HUD dizayn (11-dars) ni doskada umumlashtiring.",
    "Pitch qoidalari: 60 soniyada o'yinni qanday sotish mumkin? Hook -> Maqsad -> O'ziga xos quvvat -> O'ynashga chaqirish formulasini o'rgating.",
    "O'yin pasporti: Varaqadagi pasportni professional Game Design Document (GDD) sifatida to'ldirishni ko'rsating.",
    "Playtest madaniyati: Jim kuzatish qoidasi. O'yin muallifi o'yinchiga xalaqit bermasdan, uning his-tuyg'ularini qog'ozga yozib borishi kerak.",
    "Amaliy vazifa: O'yin pasportini yakunlash va sherigiga 60 soniyalik Pitch taqdimotini so'zlab berish.",
    "Jonli sprint: 11 daqiqalik taymer. O'quvchilar pasportni to'ldirib, juftliklarda navbatma-navbat taqdimot qilishadi.",
    "Ovoz berish va nominatsiyalar: Eng yaxshi 3D dizayn, Eng aqlli NPC va Eng zo'r geympley nominatsiyalarini e'lon qiling va g'oliblarni qutlang.",
    "Uy vazifasi: Papkani yig'ish va 2-hafta yakuniy xulosalarini yozish. 10 ballik yakuniy baholash."
  ],
  'ru': [
    "Вступление: Поздравьте ребят с финалом 2-й недели! Объявите Game Jam Demo Day — сборку всех компонентов в единый проект.",
    "Суть Game Jam: Как проходят игровые хакатоны и почему сборка быстрого прототипа эффективнее 5 лет разработки.",
    "5 компонентов недели: 3D-модели (урок 7), Карты и биом (урок 8), SFX (урок 9), NPC (урок 10), HUD (урок 11).",
    "Искусство питчинга: 60 секунд. Формула: Захват внимания -> Главная цель -> Уникальная фишка -> Призыв к игре.",
    "Паспорт Игры: Разберите структуру мини-диздока (GDD) на примере игры 'Aero-Runner 2150'.",
    "Культура плейтеста: Молчаливое наблюдение. Создатель не спойлерит и не подсказывает, а записывает трудности игрока.",
    "Постановка задачи: Заполнить паспорт игры и провести взаимный 60-секундный питчинг в парах.",
    "Практический спринт: Таймер на 11 минут. Ученики репетируют питч и тестируют концепции друг друга.",
    "Церемония наград: Голосование за лучший 3D-арт, самого живого NPC и лучший геймплей. Поздравьте победителей.",
    "Домашнее задание: Собрать файлы в архив и заполнить паспорт проекта (10 баллов)."
  ],
  'en': [
    "Opening: Congratulate developers on reaching the Week 2 Capstone! Announce the Game Jam Demo Day.",
    "Game Jam Culture: Rapid prototyping sprints versus multi-year development stagnation. Finding the fun factor fast.",
    "The 5 Pillars: 3D Assets (L7), Biome/Skybox (L8), SFX Audio (L9), Smart NPCs (L10), and HUD Interface (L11).",
    "Pitching Protocol: 60-second formula: Hook -> Core Objective -> Signature Innovation -> Call to Action.",
    "Game Design Passport: Structuring the one-page Game Design Document (GDD) using 'Aero-Runner 2150'.",
    "Playtesting Ethics: The discipline of silent observation. Watching without spoiling or directing player input.",
    "Mission Brief: Finalize the Game Passport and deliver reciprocal 60-second pitches in pairs.",
    "Live Lab Sprint: 11-minute timer. Pairs pitch their titles and execute live concept playtests.",
    "Award Ceremony: Tally ballot votes for Best 3D Art, Smartest NPC, and Ultimate Gameplay. Celebrate achievements.",
    "Homework: Package all digital assets into Google Drive / portfolio folder and submit passport. 10-point rubric."
  ]
}

p12_html = build_presentation("12-dars: Game Jam: Mini-O'yin Prototipi Taqdimoti", l12_slides, l12_notes)
with open(os.path.join(l12_dir, "prezentatsiya.html"), "w", encoding="utf-8") as f:
    f.write(p12_html)

l12_t1 = {"uz": "Game Jam: O'yin Prototipi Taqdimoti", "ru": "Game Jam: Презентация Прототипа", "en": "Game Jam: Prototype Pitch"}
l12_s1 = {"uz": "Hafta davomida yaratilgan barcha 5 ta komponentni yagona O'yin Pasportiga jamlang va taqdim eting.", "ru": "Соберите все 5 компонентов недели в единый Паспорт Игры и проведите питч.", "en": "Consolidate all 5 week components into the Game Design Passport and deliver your pitch."}
l12_k1 = {"uz": "Game Jam siri — g'oyani yillarga cho'zmasdan, bir necha kunda ishlovchi prototipga aylantirishdir.", "ru": "Секрет Game Jam — превратить идею в рабочий прототип за считанные дни, а не годы.", "en": "The secret of Game Jam is turning an ambitious vision into a playable prototype in days, not years."}

l12_p1 = """
  <section class="sec">
    <div class="h"><span class="no">01</span><h2><span lang="uz">Game Jam Madaniyati Nima?</span><span lang="ru">Что такое Game Jam?</span><span lang="en">What is a Game Jam?</span></h2></div>
    <div class="compare">
      <div class="bad">
        <span class="lbl"><span lang="uz">Katta Sekin Loyiha</span><span lang="ru">Долгий Проект</span><span lang="en">Slow Dev Cycle</span></span>
        <p class="pr"><span lang="uz">Yillar davomida rejalashtiriladi, lekin hech qachon tugatilmaydi. O'yinchilar fikri o'rganilmaydi.</span><span lang="ru">Делается годами и забрасывается. Создатели не показывают игру реальным игрокам.</span><span lang="en">Planned over years but never launched. Zero feedback from real gamers.</span></p>
      </div>
      <div class="good">
        <span class="lbl"><span lang="uz">Tezkor Prototip (Game Jam)</span><span lang="ru">Быстрый Прототип</span><span lang="en">Rapid Game Jam Sprint</span></span>
        <p class="pr"><span lang="uz">Bir necha kunda o'yin yadrosi yig'iladi! Do'stlar darhol sinab ko'radi va eng zo'r g'oyalar aniqlanadi.</span><span lang="ru">Ядро игры собирается за дни! Друзья сразу тестируют и находят самые веселые механики.</span><span lang="en">Core gameplay loop built in days! Friends playtest immediately to validate fun mechanics.</span></p>
      </div>
    </div>
  </section>

  <section class="sec">
    <div class="h"><span class="no">02</span><h2><span lang="uz">O'yinning 5 Ta Tayanch Ustuni</span><span lang="ru">5 Столпов Игры</span><span lang="en">The 5 Game Pillars</span></h2></div>
    <div class="trio">
      <div>
        <b><span lang="uz">1. 3D Model 🧊</span><span lang="ru">1. 3D-Модель 🧊</span><span lang="en">1. 3D Asset 🧊</span></b>
        <span class="d"><span lang="uz">Qurol yoki transport (.GLB toza to'r).</span><span lang="ru">Оружие или транспорт (.GLB сетка).</span><span lang="en">Primary weapon or vehicle (.GLB).</span></span>
      </div>
      <div>
        <b><span lang="uz">2. Xarita va Biom 🗺️</span><span lang="ru">2. Карта и Биом 🗺️</span><span lang="en">2. Map & Biome 🗺️</span></b>
        <span class="d"><span lang="uz">8x8 katakli xarita va Skybox osmon foni.</span><span lang="ru">Сетка 8x8 и панорама неба Skybox.</span><span lang="en">8x8 grid layout & panoramic skybox.</span></span>
      </div>
      <div>
        <b><span lang="uz">3. Ovoz va Musiqa 🔊</span><span lang="ru">3. Аудио и Музыка 🔊</span><span lang="en">3. Audio & SFX 🔊</span></b>
        <span class="d"><span lang="uz">3 ta SFX harakat tovushi + fon musiqasi.</span><span lang="ru">3 SFX эффекта + саундтрек биома.</span><span lang="en">3 isolated SFX + looping music track.</span></span>
      </div>
    </div>
  </section>

  <section class="sec">
    <div class="h"><span class="no">03</span><h2><span lang="uz">60 Soniyalik Pitch Formulasi</span><span lang="ru">Формула Питча</span><span lang="en">60s Pitch Formula</span></h2></div>
    <div class="formula">
      <div class="p"><b>1. Hook (15s)</b><span class="d">Qiziqtiruvchi sir</span></div>
      <div class="plus">+</div>
      <div class="p"><b>2. Maqsad (15s)</b><span class="d">Reaktorni tuzatish</span></div>
      <div class="plus">+</div>
      <div class="p"><b>3. Quvvat (15s)</b><span class="d">Aqlli NPC va jetpak</span></div>
      <div class="plus">+</div>
      <div class="p"><b>4. Chorlov (15s)</b><span class="d">Hozir o'ynab ko'r!</span></div>
    </div>
  </section>

  <section class="sec">
    <div class="h"><span class="no">04</span><h2><span lang="uz">Playtestning Oltin Qoidasi</span><span lang="ru">Правило Плейтеста</span><span lang="en">Playtesting Law</span></h2></div>
    <div class="checklist">
      <div><b>Jim Kuzatish:</b> <span lang="uz">Do'stingiz o'yiningizni sinaganda gapirmang va o'rgatmang! U qayerda to'xtab qolganini daftarga yozib boring.</span><span lang="ru">Молчите во время теста! Записывайте, где игрок запутался.</span><span lang="en">Remain silent during testing! Log where the player hesitates or struggles.</span></div>
      <div><b>Xolis Baho:</b> <span lang="uz">Haqiqiy geymdev tanqiddan xafa bo'lmaydi, balki xatolarni tuzatib o'yinini yanada zo'r qiladi.</span><span lang="ru">Конструктивная критика делает прототип хитом.</span><span lang="en">Constructive criticism turns rough prototypes into blockbuster games.</span></div>
    </div>
  </section>
"""

l12_t2 = {"uz": "Target O'yin Loyihasi Pasporti", "ru": "Паспорт Игрового Проекта", "en": "Game Design Document (GDD)"}
l12_s2 = {"uz": "Hafta davomida yaratilgan barcha 5 ta elementni rasmiy pasportga muhrlang.", "ru": "Зафиксируйте все 5 элементов недели в официальном паспорте игры.", "en": "Consolidate all 5 weekly assets into the official game design passport."}

l12_p2 = """
  <section class="sec">
    <div class="h"><span class="no">05</span><h2><span lang="uz">O'yin Loyihasi Rasmiy Pasporti</span><span lang="ru">Паспорт Проекта</span><span lang="en">Official Game Passport</span></h2></div>
    <div style="display:grid; grid-template-columns:1fr 1fr; gap:8px; font-size:8.5pt;">
      <div style="border:1px dashed var(--write); padding:6px;">
        <b>O'yin Nomi:</b> ___________________________<br>
        <b>Janr:</b> [ ] Parkour [ ] RPG [ ] Survival<br>
        <b>Platforma:</b> [ ] Roblox [ ] Minecraft [ ] Web
      </div>
      <div style="border:1px dashed var(--write); padding:6px;">
        <b>Biom Muhiti:</b> _________________________<br>
        <b>3D Qurol Nomi:</b> _______________________<br>
        <b>Bosh Qahramon:</b> ______________________
      </div>
    </div>
  </section>

  <section class="sec">
    <div class="h"><span class="no">06</span><h2><span lang="uz">Mening 60 Soniyalik Pitch Matnim</span><span lang="ru">Мой Питч 60с</span><span lang="en">My 60-Second Pitch Script</span></h2></div>
    <div style="border:1px solid var(--rule); background:var(--panel); padding:8px; min-height:45px; font-family:monospace; font-size:8pt;">
      "1. Tasavvur qiling: ____________________________________________________________________<br>
      2. Sizning maqsadingiz: ________________________________________________________________<br>
      3. O'yinimizdagi eng zo'r qulaylik: ____________________________________________________<br>
      4. Sinab ko'rishga tayyormisiz? Hozir o'ynang!"
    </div>
  </section>

  <section class="sec">
    <div class="h"><span class="no">07</span><h2><span lang="uz">5 Komponent Tayyorgarlik Holati</span><span lang="ru">Чеклист 5 Элементов</span><span lang="en">5-Pillar Readiness Audit</span></h2></div>
    <table class="gridtable" style="width:100%; border-collapse:collapse; font-size:8pt; text-align:left;">
      <tr style="background:var(--panel-2);">
        <th style="padding:4px; border:1px solid var(--rule);">Komponent</th>
        <th style="padding:4px; border:1px solid var(--rule);">Holat</th>
        <th style="padding:4px; border:1px solid var(--rule);">Fayl / Izoh</th>
      </tr>
      <tr>
        <td style="padding:4px; border:1px solid var(--rule);">1. 3D Model (.GLB)</td>
        <td style="padding:4px; border:1px solid var(--rule);">[ ] Tayyor</td>
        <td style="padding:4px; border:1px solid var(--rule);">Teshiklarsiz, toza to'r</td>
      </tr>
      <tr>
        <td style="padding:4px; border:1px solid var(--rule);">2. Xarita & Skybox</td>
        <td style="padding:4px; border:1px solid var(--rule);">[ ] Tayyor</td>
        <td style="padding:4px; border:1px solid var(--rule);">8x8 katakli chizma + osmon</td>
      </tr>
      <tr>
        <td style="padding:4px; border:1px solid var(--rule);">3. SFX Audio & Musiqa</td>
        <td style="padding:4px; border:1px solid var(--rule);">[ ] Tayyor</td>
        <td style="padding:4px; border:1px solid var(--rule);">3 SFX + fon kuyi</td>
      </tr>
      <tr>
        <td style="padding:4px; border:1px solid var(--rule);">4. Aqlli NPC</td>
        <td style="padding:4px; border:1px solid var(--rule);">[ ] Tayyor</td>
        <td style="padding:4px; border:1px solid var(--rule);">System Prompt + Kvest daraxti</td>
      </tr>
      <tr>
        <td style="padding:4px; border:1px solid var(--rule);">5. HUD UI Interfeys</td>
        <td style="padding:4px; border:1px solid var(--rule);">[ ] Tayyor</td>
        <td style="padding:4px; border:1px solid var(--rule);">4 burchak qoidasidagi maket</td>
      </tr>
    </table>
  </section>

  <section class="sec">
    <div class="h"><span class="no">08</span><h2><span lang="uz">Playtest Taqrizi (Sherik Fikri)</span><span lang="ru">Отзыв Плейтестера</span><span lang="en">Peer Playtest Feedback</span></h2></div>
    <div style="font-size:8pt; border:1px dashed var(--write); padding:6px;">
      <b>Sherigim o'yinining 2 ta eng zo'r tomoni:</b> 1. ___________________  2. ___________________<br>
      <b>1 ta do'stona maslahatim:</b> ___________________________________________________________
    </div>
  </section>
"""

l12_hw = """
  <p><b>1. Papkani Yig'ish:</b> Barcha 5 ta komponent fayllarini bitta o'yin papkasiga to'liq jamlang.</p>
  <p><b>2. Pasportni Yakunlash:</b> Ushbu varaqadagi barcha jadvallar va parametrlarni to'ldiring.</p>
  <p><b>3. Sherik Fikri:</b> Sherigingiz o'yini bo'yicha 2 ta yutuq va 1 ta maslahat yozib keling.</p>
"""

l12_crit = """
  <div class="r"><span>O'yin pasporti barcha qismlari bilan to'ldirilgan</span><b>3</b></div>
  <div class="r"><span>5 ta komponent (3D, xarita, SFX, NPC, HUD) tayyor</span><b>4</b></div>
  <div class="r"><span>60s Pitch va o'zaro Playtest bajarilgan</span><b>3</b></div>
"""

l12_nxt = {'uz': "3-Hafta: Kiber-Xavfsizlik va Katta Turnir", 'ru': "3-Неделя: Кибербезопасность и Турнир", 'en': "Week 3: Cyber Security & Championship"}

ws12_html = build_worksheet('5-6-sinf', 2, 12, l12_t1, l12_s1, l12_k1, l12_p1, l12_t2, l12_s2, l12_p2, l12_hw, l12_crit, l12_nxt)
with open(os.path.join(l12_dir, 'varaqa.html'), 'w', encoding='utf-8') as f:
    f.write(ws12_html)

print("5-6 Week 2 Lesson 12 generated successfully!")
