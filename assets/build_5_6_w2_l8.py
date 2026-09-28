#!/usr/bin/env python3
import os, sys
sys.path.insert(0, '/home/dpdp/target/assets')
from curriculum_generator import build_presentation, build_worksheet

BASE = '/home/dpdp/target/classes/5-6-sinf/2-hafta'
l8_dir = os.path.join(BASE, '08-dars-oyun-dunyosi-va-level-design')
os.makedirs(l8_dir, exist_ok=True)

l8_slides = """
<section class="slide is-on" data-phase="Kirish|Вступление|Opening" data-time="0–3">
  <div class="title-wrap">
    <div class="eyebrow">Vibecoding · <span data-ru="урок 8 · 5-6 классы" data-en="lesson 8 · grades 5-6">8-dars · 5-6 sinflar</span></div>
    <div class="title-meta">
      <span><b lang="uz">Fan:</b><span data-ru=" IT / Vibecoding" data-en=" IT / Vibecoding"> IT / Vibecoding</span><b lang="ru">Предмет:</b><span lang="ru"> IT / Vibecoding</span><b lang="en">Subject:</b><span lang="en"> IT / Vibecoding</span></span>
      <span><b lang="uz">Hafta:</b><span data-ru=" 2" data-en=" 2"> 2</span><b lang="ru">Неделя:</b><span lang="ru"> 2</span><b lang="en">Week:</b><span lang="en"> 2</span></span>
    </div>
    <h1 data-ru="Игровой Мир: Левел-Дизайн, Биомы и Карта" data-en="Game World: Level Design, Biomes & Map Architecture">O'yin Dunyosi: Level Design, Biomlar va Xarita Arxitekturasi</h1>
    <p class="lede" data-ru="Почему в одни карты хочется играть часами, а с других сразу выходят? Проектируем уровни, настраиваем освещение, биомы и баланс испытаний." data-en="Why do gamers explore some maps for hours while abandoning others instantly? Architecting levels, environmental biomes, lighting, and challenge pacing.">Nega ba'zi xaritalarni soatlab o'ynagimiz keladi, boshqalaridan esa darhol chiqib ketamiz? O'yin sathlari, biomlar, yorug'lik va sinovlar muvozanatini loyihalaymiz.</p>
  </div>
</section>

<section class="slide" data-phase="Tushuncha|Что такое Левел-Дизайн|Level Design Core" data-time="3–7">
  <div class="eyebrow"><span data-ru="Основы левел-дизайна" data-en="Level Design Principles">Level Design Qonunlari</span></div>
  <h2 data-ru="Что такое Левел-Дизайн: Управление Вниманием Игрока" data-en="What is Level Design: Directing Player Attention & Flow">Level Design Nima? O'yinchi Diqqatini Yo'naltirish San'ati</h2>
  <p data-ru="Левел-дизайн — это не просто расстановка деревьев и домиков. Это невидимый маршрут, ведущий игрока:" data-en="Level design is not merely scattering trees and obstacles. It is the invisible psychological flow guiding the player:">Level design — shunchaki daraxt yoki qutilarni terish emas. Bu o'yinchini maqsadi sari boshlovchi ko'rinmas psixologik yo'lakdir:</p>
  <div class="cols c2" style="margin-top:15px;">
    <div class="box">
      <h3 style="color:var(--ink-2);" data-ru="Плохая карта (Хаос) ❌" data-en="Chaotic Map ❌">Yomon Xarita (Tartibsizlik) ❌</h3>
      <p data-ru="Игрок появляется в случайном месте и не понимает, куда бежать. Везде тупики, нет ориентиров и света. Через 2 минуты игрок закрывает игру." data-en="Spawn without visual cues or objectives. Surrounded by dead ends and confusing geometry. Abandoned in 2 minutes.">O'yinchi qayerga borishni bilmaydi. Hamma joy berk ko'cha, yo'naltiruvchi mayoqlar yo'q. 2 daqiqada o'yin o'chiriladi.</p>
    </div>
    <div class="box" style="border-left:4px solid var(--green);">
      <h3 style="color:var(--green);" data-ru="Продуманная карта (Поток) ✅" data-en="Flow Map ✅">Aqlli Xarita (Oqim / Flow) ✅</h3>
      <p data-ru="Свет и силуэты зданий сразу подсказывают путь к цели! Препятствия постепенно усложняются, держа интерес на максимуме." data-en="Dynamic lighting and landmark silhouettes instantly communicate objectives. Hazards escalate smoothly to preserve engagement.">Chiroqlar va binolar silueti o'yinchini marraga yetaklaydi. To'siqlar bosqichma-bosqich qiyinlashib, hayajonni ushlab turadi.</p>
    </div>
  </div>
</section>

<section class="slide" data-phase="Biomlar|Биомы и Атмосфера|Biomes & Ambience" data-time="7–11">
  <div class="eyebrow"><span data-ru="Игровые биомы" data-en="Environmental Biomes">Biomlar va Rang Palitrasi</span></div>
  <h2 data-ru="3 Популярных Биома и Их Визуальные Законы" data-en="3 Classic Biomes & Their Visual Color Rules">O'yin Biomlari: 3 Xil Dunyo va Ularning Qonunlari</h2>
  <p data-ru="Биом задает настроение всей игре. Сравните, как цвет и геометрия меняют восприятие:" data-en="A biome establishes emotional tone. Observe how color palettes and geometry alter player perception:">Biom butun o'yin kayfiyatini belgilaydi. Rang va muhit o'yinchi his-tuyg'ularini qanday boshqaradi:</p>
  <div class="cols c3" style="display:grid; grid-template-columns:1fr 1fr 1fr; gap:12px; margin-top:12px;">
    <div class="box" style="border-top:4px solid #00E5FF;">
      <h3 style="color:#00838F;" data-ru="1. Кибер-Мегаполис 🏙️" data-en="1. Cyber Metropolis 🏙️">1. Kiber-Megapolis 🏙️</h3>
      <p data-ru="Тёмный мокрый асфальт, фиолетовый и бирюзовый неон, гигантские голограммы и небоскребы." data-en="Dark wet asphalt, purple & cyan neon rimlights, towering holographic billboards.">Qorong'u ho'l asfalt, binafsha va havorang neon chiroqlari, ulkan gologrammalar.</p>
    </div>
    <div class="box" style="border-top:4px solid #FF5722;">
      <h3 style="color:#D84315;" data-ru="2. Огненная Пустошь 🌋" data-en="2. Volcanic Wasteland 🌋">2. Vulqon Cho'li 🌋</h3>
      <p data-ru="Черный базальт, раскаленная лава, оранжевое свечение, трещины и падающий пепел." data-en="Black basalt crags, flowing magma crevices, amber ambient haze, and falling ash.">Qora bazalt toshlar, qaynoq lava ariqlari, to'q qizil tutun va chaqmoqlar.</p>
    </div>
    <div class="box" style="border-top:4px solid #76FF03;">
      <h3 style="color:#2E7D32;" data-ru="3. Парящие Острова ☁️" data-en="3. Skybound Isles ☁️">3. Suzuvchi Orollar ☁️</h3>
      <p data-ru="Левитирующие скалы, изумрудная трава, водопады в бездну и сияющие кристаллы." data-en="Levitating rocky landmasses, emerald foliage, endless skyboxes, and arcane crystals.">Osmondagi uchuvchi qoyalar, zumrad maysa, tubsizlikka quyiluvchi sharsharalar va kristallar.</p>
    </div>
  </div>
</section>

<section class="slide" data-phase="Mexanizm|Skybox и Освещение|Skybox & Shaders" data-time="11–15">
  <div class="eyebrow"><span data-ru="Атмосфера и свет" data-en="Skybox & Lighting">Atmosfera va Skybox</span></div>
  <h2 data-ru="Секрет Глубины: Skybox и Световые Ориентиры" data-en="The Depth Secret: Skyboxes & Directional Beacons">Katta Dunyo Hissi: Skybox va Yo'naltiruvchi Chiroqlar</h2>
  <p data-ru="В Roblox и Unity небо — это гигантская 360-сфера вокруг игрока (Skybox). Как свет управляет игроком:" data-en="In Roblox and Unity, the atmosphere is enclosed by a 360° spherical panoramic backdrop (Skybox):">O'yinlarda osmon — bu o'yinchi atrofini 360 daraja o'rab turuvchi ulkan fon (Skybox). Chiroq o'yinchini qanday boshqaradi:</p>
  <ul class="rules">
    <li><span class="t" data-ru="<b>1. Принцип мотылька (Lighthouse effect):</b> Игрок подсознательно бежит к самому яркому объекту в поле зрения (фонарь, светящаяся башня)." data-en="<b>1. The Moth Principle:</b> Gamers instinctually gravitate toward the highest luminance in view (beacons, illuminated towers)."><b>1. Parvona effekti (Mayoqli yo'l):</b> O'yinchi ko'z qorachig'i doimo eng yorug' obyektga tomon intiladi (baland minora, neon darvoza).</span></li>
    <li><span class="t" data-ru="<b>2. Безопасные и опасные зоны:</b> Теплый желтый свет означает лагерь и союзников, холодный красный — ловушки и врагов." data-en="<b>2. Safe vs Hazard Coding:</b> Warm amber illumination denotes shelter/allies; sinister crimson indicates turrets/traps."><b>2. Xavfsiz va xavfli hududlar kodi:</b> Iliq sariq nur — do'stlar va xavfsiz baza; sovuq qizil nur — tuzoqlar va dushmanlar.</span></li>
    <li><span class="t" data-ru="<b>3. Чекпоинты (Checkpoints):</b> Игрок должен видеть место сохранения заранее, чтобы не бояться рисковать!" data-en="<b>3. Visible Checkpoints:</b> Respawn pads must remain visually identifiable to encourage player experimentation."><b>3. Jon saqlovchi maydonchalar (Checkpoints):</b> O'yinchi xavfli sakrashdan oldin jon saqlash joyini aniq ko'rib turishi shart.</span></li>
  </ul>
</section>

<section class="slide" data-phase="Ko'rsatma|Сетка уровня|Level Grid Prompt" data-time="15–19">
  <div class="eyebrow"><span data-ru="Проектирование карты" data-en="Grid Blueprint">Top-Down Xarita Formulasi</span></div>
  <h2 data-ru="Промпт для Генерации Схемы Уровня (Top-Down Map)" data-en="Engineering Top-Down Game Level Blueprints">AI Bilan Yuqoridan Ko'rinish (Top-Down) Xaritasi Prompti</h2>
  <div class="box" style="background:var(--panel); border-left:5px solid var(--green); padding:16px;">
    <p style="font-family:monospace; font-size:0.95em; line-height:1.6;" data-ru="<b>[ВИД]</b> Top-down orthographic level map design, 2D game blueprint<br>+ <b>[БИОМ]</b> Кибернетическая фабрика роботов с лазерными коридорами<br>+ <b>[ЗОНЫ]</b> Start Spawn (левый низ) -> Зона головоломок с ящиками -> Финальные врата босса (правый верх)<br>+ <b>[ДЕТАЛИ]</b> Четкие стены, нарисованная стрелками траектория движения, чекпоинты, сетка 8x8" data-en="<b>[VIEW]</b> Top-down orthographic level map design, 2D blueprint layout<br>+ <b>[BIOME]</b> Cybernetic automaton factory with electrified laser corridors<br>+ <b>[ZONING]</b> Start Spawn (bottom left) -> Crate puzzle chambers -> Boss extraction gates (top right)<br>+ <b>[DETAILS]</b> Clean structural walls, arrow-marked traversal routes, checkpoints, 8x8 grid overlay">
      <b>1. KO'RINISh:</b> Top-down ortografik xarita chizmasi, 2D o'yin level sxemasi<br>
      + <b>2. BIOM:</b> Lazerli dahlizlarga ega kiber-robotlar fabrikasi<br>
      + <b>3. HUDUDLAR:</b> Start nuqtasi (chap burchak) -> Qutilar va to'siqlar zonasi -> Boss darvozasi (o'ng yuqori)<br>
      + <b>4. DETALLAR:</b> Qalin devorlar, o'yinchi harakat yo'nalishi ko'rsatilgan chiziqlar, 8x8 katakli setka
    </p>
  </div>
  <p style="margin-top:12px; font-size:0.9em; color:var(--ink-2);" data-ru="Схема сверху позволяет сразу увидеть тупики и баланс ловушек перед постройкой в 3D!" data-en="Top-down blueprints expose bottlenecks and dead ends before committing to 3D construction!">Yuqoridan ko'rinish xaritasi 3D da qurishdan oldin barcha xatolarni qog'ozda ko'rish imkonini beradi!</p>
</section>

<section class="slide" data-phase="Sinov|Баланс сложности|Difficulty Curve" data-time="19–23">
  <div class="eyebrow"><span data-ru="Кривая сложности" data-en="Difficulty Balance">Qiyinlik Balansi</span></div>
  <h2 data-ru="Кривая Сложности: Как не Разозлить Игрока" data-en="The Difficulty Curve: Balancing Challenge vs Rage-Quit">O'yin Balansi: O'yinchini Qachon Jahli Chiqadi?</h2>
  <p data-ru="Игру удаляют, если она слишком легкая (скучно) или непроходимо сложная (гнев). Идеальный ритм:" data-en="Gamers quit if a level is boringly trivial or infuriatingly unfair. The master rhythm:">O'yin juda oson bo'lsa zerikarli bo'ladi, o'tib bo'lmas darajada qiyin bo'lsa o'yinchi jahl bilan o'chiradi:</p>
  <div class="cols c3" style="display:grid; grid-template-columns:1fr 1fr 1fr; gap:12px; margin-top:15px;">
    <div class="box">
      <h3 style="color:var(--ink-2);" data-ru="1. Обучение (0–20%)" data-en="1. Onboarding (0–20%)">1. O'rganish (0–20%)</h3>
      <p data-ru="Безопасный прыжок через 1 блок. Игрок понимает физику и кнопки управления." data-en="Safe hop across 1 block gap. Teaches movement physics with zero death risk.">1 blokdan xavfsiz sakrash. O'yinchi boshqaruv va sakrash kuchini tushunadi.</p>
    </div>
    <div class="box">
      <h3 style="color:var(--accent);" data-ru="2. Испытание (20–70%)" data-en="2. Escalation (20–70%)">2. Qiyinlashuv (20–70%)</h3>
      <p data-ru="Движущиеся платформы, исчезающие блоки и лазеры с таймером." data-en="Moving platforms, disappearing bridges, and rhythmic timed hazards.">Harakatlanuvchi platformalar, yo'qolib qoluvchi plitalar va lazerlar.</p>
    </div>
    <div class="box" style="border-left:4px solid var(--green);">
      <h3 style="color:var(--green);" data-ru="3. Кульминация (100%)" data-en="3. Climax (100%)">3. Kulminatsiya (100%)</h3>
      <p data-ru="Финальная битва или сложный паркур к порталу победы. Максимальная награда!" data-en="Climactic boss showdown or precision parkour gauntlet to victory extraction.">Boss bilan jang yoki g'alaba portaliga qadar tezkor parkur. Katta yutuq!</p>
    </div>
  </div>
</section>

<section class="slide" data-phase="Vazifa|Миссия урока|Level Lab" data-time="23–27">
  <div class="eyebrow"><span data-ru="Практическая миссия" data-en="Level Blueprinting">Amaliy Vazifa</span></div>
  <h2 data-ru="Миссия: Спроектировать 3 Зоны Игрового Уровня" data-en="Mission: Architect 3 Zones of Your Game Level">Bugungi Vazifa: O'z O'yiningiz Uchun 3 Ta Zonani Chizing</h2>
  <p data-ru="Используя рабочий лист и генератор ИИ, спроектируйте уровень из 3 последовательных зон:" data-en="Leveraging your worksheet and AI, map out an actionable level spanning 3 progressive zones:">Varaqadagi katakli setka va AI yordamida o'z o'yiningizning 3 ta zonasini rejalashtiring:</p>
  <ul class="rules">
    <li><span class="t" data-ru="<b>1. Зона Старта (Safe Zone):</b> Место возрождения, инструкция от NPC, начальный сундук." data-en="<b>1. Safe Spawn Zone:</b> Player spawn pad, starting NPC guide, initial supply cache."><b>1. Boshlang'ich hudud (Safe Zone):</b> Jonlanish joyi, yo'l ko'rsatuvchi NPC va boshlang'ich qurol sandig'i.</span></li>
    <li><span class="t" data-ru="<b>2. Зона Препятствий (Hazard Zone):</b> 2 вида ловушек (лазеры / лава) и 1 спрятанный секрет." data-en="<b>2. Hazard Gauntlet:</b> 2 distinct mechanical traps (lasers/lava) plus 1 secret easter egg."><b>2. To'siqlar hududi (Hazard Zone):</b> Kamida 2 xil to'siq (lazerlar / lava) va 1 ta yashirin tanga.</span></li>
    <li><span class="t" data-ru="<b>3. Зона Финиша (Victory Vault):</b> Врата босса, портал выхода и финальный сундук с кристаллами." data-en="<b>3. Extraction / Vault:</b> Boss arena gates, extraction portal, and crystal loot reward."><b>3. Marra hududi (Victory Vault):</b> Boss darvozasi, chiqish portali va afsonaviy xazina.</span></li>
  </ul>
</section>

<section class="slide" data-phase="Amaliyot|Левел-Спринт|Level Design Sprint" data-time="27–31">
  <div class="eyebrow"><span data-ru="Инженерный спринт" data-en="Level Sprint">Jonli Amaliyot · Taymer</span></div>
  <h2 data-ru="Левел-Спринт: 11 Минут на Создание Архитектуры Уровня" data-en="Level Sprint: 11 Minutes to Map Your Realm">Level Ustaxona: 11 Daqiqalik Xarita Loyihasi</h2>
  <div class="timer" id="timer">
    <div class="digits" id="digits">11:00</div>
    <div class="ctrls">
      <button id="tstart">Start / Stop</button>
      <button class="ghost" id="treset">Reset</button>
    </div>
  </div>
  <p style="margin-top:15px; font-size:0.95em;" data-ru="Нарисуйте схему уровня на сетке рабочего листа и сгенерируйте Top-Down концепт через ИИ!" data-en="Sketch your level routing on your worksheet grid and generate an AI top-down concept!">Varaqadagi katakli chizmaga xarita yo'nalishini chizing va AI da xarita konseptini generatsiya qiling!</p>
</section>

<section class="slide" data-phase="Tahlil|Тест проходимости|Playtest Audit" data-time="31–36">
  <div class="eyebrow"><span data-ru="Тестирование карты" data-en="Playtest Audit">Xarita Tahlili</span></div>
  <h2 data-ru="Краш-Тест Карты: Проверка Проходимости Пальцем" data-en="Map Crash Test: The Finger-Playtest Simulation">Xaritani Barmoq Bilan Sinash (Finger-Playtest)</h2>
  <p data-ru="Отдайте лист соседу. Пусть он проведет пальцем от Старта до Финиша:" data-en="Hand your worksheet to your classmate. Have them trace the route with their finger:">Varaqangizni yoningizdagi sherigingizga bering. U barmoq bilan Startdan Marraga qadar yursin:</p>
  <div class="cols c3" style="display:grid; grid-template-columns:1fr 1fr 1fr; gap:12px; margin-top:15px;">
    <div class="box">
      <h3 style="color:var(--accent);" data-ru="1. Нет ли тупиков?" data-en="1. No Dead Ends?">1. Berk Ko'chalar Yo'qmi?</h3>
      <p data-ru="Понятно ли с первого взгляда, в какую дверь нужно идти?" data-en="Is the forward progression path visually obvious at first glance?">Birinchi qarashdayoq qaysi eshikka borish kerakligi tushunarlimi?</p>
    </div>
    <div class="box">
      <h3 style="color:var(--accent);" data-ru="2. Честные ловушки?" data-en="2. Fair Hazards?">2. To'siqlar Adolatlimi?</h3>
      <p data-ru="Видит ли игрок лазер до того, как наступит на него?" data-en="Can the player anticipate the laser before walking directly into it?">O'yinchi to'siqqa urilishdan oldin uni ko'rib, sakrashga ulguradimi?</p>
    </div>
    <div class="box" style="border-left:4px solid var(--green);">
      <h3 style="color:var(--green);" data-ru="3. Достойная награда?" data-en="3. Rewarding Loot?">3. Yutuq Qoniqarlimi?</h3>
      <p data-ru="Хочется ли пройти сложный путь ради финального сундука?" data-en="Does the finish vault feel worth the tension and parkour effort?">Qiyin yo'ldan so'ng beriladigan mukofot o'yinchiga quvonch beradimi?</p>
    </div>
  </div>
</section>

<section class="slide" data-phase="Uy vazifasi|Домашнее задание|Homework" data-time="36–40">
  <div class="eyebrow"><span data-ru="Домашний проект" data-en="Take-Home Project">Uyga Vazifa</span></div>
  <h2 data-ru="Домашнее Задание: Карта Уровня + Skybox + 10 Баллов" data-en="Homework: Complete Level Map + Skybox + 10-Point Rubric">Uyga Vazifa: To'liq Level Xaritasi va Skybox Dizayni</h2>
  <div class="hw" style="display:grid; grid-template-columns:1.4fr 1fr; gap:20px; margin-top:15px;">
    <div class="box" style="border-left:5px solid var(--accent);">
      <h3 style="color:var(--accent);" data-ru="Что нужно сделать:" data-en="Assignment Details:">Bajarilishi shart bo'lgan vazifalar:</h3>
      <ol style="margin-top:8px; padding-left:18px; line-height:1.6;">
        <li data-ru="Дорисовать полную сетку уровня на 8x8 блоков в рабочей тетради." data-en="Finalize the complete 8x8 block level map layout on your worksheet.">Varaqadagi 8x8 katakli xaritani to'liq chizib, to'siqlar va yo'laklarni belgilang.</li>
        <li data-ru="Сгенерировать 1 атмосферный Skybox (360° панорама неба) для выбранного биома через ИИ." data-en="Generate 1 atmospheric skybox panoramic backdrop matching your biome with AI.">AI orqali o'z biomingizga mos 1 ta panoramali Skybox (osmon foni) rasmini yarating.</li>
        <li data-ru="Записать 3 правила прохождения карты (условия победы и поражения)." data-en="Define 3 clear game rules (win conditions and fail states) in your workbook.">O'yin qoidalarini yozing: qanday qilib yutish va qachon yutqazish shartlari.</li>
      </ol>
    </div>
    <div class="box" style="background:var(--panel);">
      <h3 style="color:var(--green);" data-ru="Критерии Оценки (10 баллов):" data-en="Grading Rubric (10 Points):">Baholash Mezoni (10 ball):</h3>
      <ul style="margin-top:8px; padding-left:16px; line-height:1.6; font-size:0.9em;">
        <li data-ru="<b>3 балла:</b> Карта 8x8 размечена логично (Старт, Препятствия, Финиш)." data-en="<b>3 pts:</b> Logical 8x8 layout (Spawn, Hazards, Vault)."><b>3 ball:</b> Xaritada Start, To'siqlar va Marra aniq belgilangan.</li>
        <li data-ru="<b>4 балла:</b> Сгенерирован визуальный Skybox или Top-Down концепт биома." data-en="<b>4 pts:</b> Visual Skybox or top-down biome concept generated."><b>4 ball:</b> Biomga mos chiroyli Skybox yoki xarita konsepti yaratilgan.</li>
        <li data-ru="<b>3 балла:</b> Описаны 3 правила победы и поражения в тетради." data-en="<b>3 pts:</b> 3 win/loss gameplay rules detailed in workbook."><b>3 ball:</b> O'yinning 3 ta yutish va yutqazish qoidalari yozilgan.</li>
      </ul>
    </div>
  </div>
</section>
"""

l8_notes = {
  'uz': [
    "Kirish: O'quvchilardan 'Qaysi o'yin xaritasi eng sevimli?' deb so'rang. Level design shunchaki bezak emas, o'yin mantig'i ekanini ochib bering.",
    "Level Design qonunlari: Tartibsiz xarita va aqlli yo'naltiruvchi xaritaning farqini doskada chizib ko'rsating.",
    "Biomlar: 3 xil biom misolida ranglar palitrasi o'yinchi ruhiyatiga qanday ta'sir qilishini tushuntiring.",
    "Skybox va yorug'lik: Osmon foni (Skybox) va mayoq effekti (eng yorug' joyga borish) mexanizmini tushuntiring.",
    "Top-down prompt: Yuqoridan ko'rinish xaritasi chizmasini AI orqali generatsiya qilish formulasini ko'rsating.",
    "Qiyinlik balansi: O'yinchini zeriktirmaslik va jahlini chiqarmaslik uchun to'siqlar qanday bosqichma-bosqich oshirilishini tushuntiring.",
    "Amaliy topshiriq: Varaqadagi kataklarga 3 ta zonani (Start, To'siqlar, Marra) joylashtirish vazifasini bering.",
    "Jonli sprint: 11 daqiqalik taymerni yoqing. O'quvchilar xaritani chizib, AI da konseptini chiqarishadi.",
    "Xarita tahlili: Barmoq bilan sinov (Finger-playtest) mashqi: sherigining xaritasidan barmoq bilan yurib, adolatli ekanini tekshirishadi.",
    "Uy vazifasi: 8x8 katakli xaritani tugatish, Skybox foni yaratish va 3 ta o'yin qoidasini yozish. 10 ballik mezonni eslating."
  ],
  'ru': [
    "Вступление: Спросите учеников об их любимых игровых картах. Объясните, что левел-дизайн — это архитектура эмоций игрока.",
    "Суть левел-дизайна: Разница между хаотичным нагромождением блоков и продуманным визуальным маршрутом (Flow).",
    "Игровые биомы: Разберите цветовую палитру и настроение 3 биомов (Киберпанк, Пустошь, Парящие острова).",
    "Skybox и свет: Зачем нужен 360° фон неба и как принцип маяка ведет игрока к светящимся башням.",
    "Формула промпта: Промпт для Top-Down чертежа уровня с четкой сеткой и траекториями движения.",
    "Кривая сложности: Обучение (20%) -> Усложнение (50%) -> Кульминация (100%). Как избежать ярости игрока.",
    "Постановка задачи: Спроектировать на листе 3 зоны (Старт, Ловушки, Финишные врата) и запустить генерацию.",
    "Практический спринт: Таймер на 11 минут. Ученики чертят уровень и генерируют атмосферный арт биома.",
    "Тест проходимости: Упражнение 'тест пальцем': сосед проверяет карту на проходимость и отсутствие тупиков.",
    "Домашнее задание: Финализировать сетку 8x8, создать Skybox и прописать 3 правила победы. Напомните критерии 10 баллов."
  ],
  'en': [
    "Opening: Solicit students' favorite video game arenas. Establish that level design is behavioral engineering, not mere decoration.",
    "Level Design Core: Contrast disorienting dead-end layouts against intentional cognitive flow and landmark orientation.",
    "Environmental Biomes: Explore thematic palettes across 3 biomes (Cyberpunk Neon, Magma Crags, Levitation Islands).",
    "Skybox & Lighting: How 360° panoramic skydomes and the lighthouse luminance principle direct player motion.",
    "Top-Down Blueprinting: Engineering visual prompt formulas for orthographic 2D floor plans with traversal arrows.",
    "Difficulty Curve: Safe onboarding (20%) -> Escalating hazards (50%) -> Climactic extraction (100%).",
    "Mission Brief: Design 3 structured zones (Safe Spawn, Hazard Gauntlet, Victory Vault) directly onto the worksheet grid.",
    "Live Level Sprint: Run the 11-minute timer. Students sketch layout geometry and synthesize an AI biome skybox.",
    "Finger Playtest Audit: Peer QA exercise where partners trace the route with a finger to catch dead ends.",
    "Homework: Complete the 8x8 layout grid, engineer an AI skybox render, and write 3 win/loss rules. Review 10-point rubric."
  ]
}

p8_html = build_presentation("08-dars: O'yin Dunyosi va Level Design", l8_slides, l8_notes)
with open(os.path.join(l8_dir, "prezentatsiya.html"), "w", encoding="utf-8") as f:
    f.write(p8_html)

l8_t1 = {"uz": "O'yin Dunyosi va Level Design", "ru": "Игровой Мир и Левел-Дизайн", "en": "Game World & Level Design"}
l8_s1 = {"uz": "O'yinchi diqqatini yo'naltiruvchi sathlar (levels), biomlar va osmon (skybox) arxitekturasini loyihalang.", "ru": "Проектируйте уровни, биомы и атмосферу скайбокса, управляющие вниманием игрока.", "en": "Architect level maps, biomes, and skybox lighting that guide player attention and flow."}
l8_k1 = {"uz": "Level design — bu shunchaki bezak emas, o'yinchini marraga yetaklovchi ko'rinmas psixologik yo'ldir.", "ru": "Левел-дизайн — это не просто декорация, а невидимый психологический маршрут к цели.", "en": "Level design is not decoration; it is an invisible psychological path guiding the player to victory."}

l8_p1 = """
  <section class="sec">
    <div class="h"><span class="no">01</span><h2><span lang="uz">Level Design Asosiy Qoidasi</span><span lang="ru">Главный Закон Левел-Дизайна</span><span lang="en">The Law of Level Flow</span></h2></div>
    <div class="compare">
      <div class="bad">
        <span class="lbl"><span lang="uz">Tartibsiz Xarita (Chaos)</span><span lang="ru">Хаотичная Карта</span><span lang="en">Chaotic Layout</span></span>
        <p class="pr"><span lang="uz">Startda hech qanday belgi yo'q. Hamma yo'l bir xil, berk ko'chalar ko'p. O'yinchi 2 daqiqada zerikadi.</span><span lang="ru">Нет ориентиров на старте. Сплошные тупики. Игрок теряется и выходит через 2 минуты.</span><span lang="en">Zero landmarks at spawn. Abundant dead ends. Gamers abandon the match within 2 minutes.</span></p>
      </div>
      <div class="good">
        <span class="lbl"><span lang="uz">Aqlli Oqim (Flow)</span><span lang="ru">Осознанный Поток</span><span lang="en">Intentional Flow</span></span>
        <p class="pr"><span lang="uz">Yorug' minora va mayoqlar yo'lni ko'rsatadi. To'siqlar asta-sekin qiyinlashadi, qiziqish so'nmaydi!</span><span lang="ru">Свет и маяки ведут вперед. Препятствия нарастают плавно, интерес постоянно растет!</span><span lang="en">Lighting beacons guide motion. Hazards escalate smoothly to sustain engagement.</span></p>
      </div>
    </div>
  </section>

  <section class="sec">
    <div class="h"><span class="no">02</span><h2><span lang="uz">O'yin Biomlari (Biomes)</span><span lang="ru">Игровые Биомы</span><span lang="en">Game World Biomes</span></h2></div>
    <div class="trio">
      <div>
        <b><span lang="uz">Kiber-Shahar 🏙️</span><span lang="ru">Кибер-Город 🏙️</span><span lang="en">Cyber City 🏙️</span></b>
        <span class="d"><span lang="uz">Qorong'u metall, binafsha neon va osmono'par binolar.</span><span lang="ru">Темный металл, фиолетовый неон и небоскребы.</span><span lang="en">Dark metal, violet neon, towering megastructures.</span></span>
      </div>
      <div>
        <b><span lang="uz">Vulqon Qoyalari 🌋</span><span lang="ru">Вулканические Скалы 🌋</span><span lang="en">Volcanic Crags 🌋</span></b>
        <span class="d"><span lang="uz">Qora bazalt, olovli lava va zaharli tutunlar.</span><span lang="ru">Черный базальт, раскаленная лава и пепел.</span><span lang="en">Black basalt, magma channels, dense ember haze.</span></span>
      </div>
      <div>
        <b><span lang="uz">Suzuvchi Orollar ☁️</span><span lang="ru">Парящие Острова ☁️</span><span lang="en">Sky Islands ☁️</span></b>
        <span class="d"><span lang="uz">Moviy osmon, parvoz qiluvchi qoyalar va sharsharalar.</span><span lang="ru">Левитирующие скалы, синее небо и водопады.</span><span lang="en">Levitating crags, pristine skyboxes, waterfalls.</span></span>
      </div>
    </div>
  </section>

  <section class="sec">
    <div class="h"><span class="no">03</span><h2><span lang="uz">Level Design Qiyinlik Balansi</span><span lang="ru">Баланс Сложности</span><span lang="en">Difficulty Balancing</span></h2></div>
    <div class="formula">
      <div class="p"><b>1. O'rganish (20%)</b><span class="d">Xavfsiz sakrash</span></div>
      <div class="plus">-></div>
      <div class="p"><b>2. Sinov (50%)</b><span class="d">Harakatli lazerlar</span></div>
      <div class="plus">-></div>
      <div class="p"><b>3. Boss (30%)</b><span class="d">Tezkor parkur</span></div>
    </div>
  </section>

  <section class="sec">
    <div class="h"><span class="no">04</span><h2><span lang="uz">Skybox va Yorug'lik Qoidalari</span><span lang="ru">Правила Skybox и Света</span><span lang="en">Skybox & Lighting Rules</span></h2></div>
    <div class="checklist">
      <div><b>Parvona Qoidasi:</b> <span lang="uz">O'yinchi ko'zi eng yorug' obyekt tomon intiladi — asosiy darvozani yoritib qo'ying.</span><span lang="ru">Игрок инстинктивно идет на свет — подсвечивайте ключевые врата.</span><span lang="en">Players instinctively track bright beacons — illuminate primary objective portals.</span></div>
      <div><b>Rang Kodi:</b> <span lang="uz">Iliq sariq/yashil = xavfsiz baza; sovuq qizil/binafsha = dushman va tuzoqlar.</span><span lang="ru">Желтый/зеленый = база; красный/фиолетовый = опасность.</span><span lang="en">Warm amber/green = shelter; sinister red/violet = traps and hostile turrets.</span></div>
    </div>
  </section>
"""

l8_t2 = {"uz": "Level Blueprint: 8x8 Xarita Sxemasi", "ru": "Схема Уровня 8x8", "en": "Level Blueprint: 8x8 Grid"}
l8_s2 = {"uz": "O'z o'yiningiz sathini 8x8 katakli xaritaga chizing va to'siqlarni joylashtiring.", "ru": "Нарисуйте сетку уровня 8x8 и расставьте ключевые препятствия.", "en": "Draft your 8x8 level layout grid and position strategic hazards."}

l8_p2 = """
  <section class="sec">
    <div class="h"><span class="no">05</span><h2><span lang="uz">8x8 Katakli Level Xaritasi</span><span lang="ru">Сетка Уровня 8x8</span><span lang="en">8x8 Traversal Grid</span></h2></div>
    <div style="display:grid; grid-template-columns:1.2fr 1fr; gap:12px;">
      <div style="border:2px solid var(--rule); display:grid; grid-template-columns:repeat(8, 1fr); grid-template-rows:repeat(8, 22px); gap:1px; background:var(--rule); padding:1px;">
        <div style="background:var(--panel);"></div><div style="background:var(--panel);"></div><div style="background:var(--panel);"></div><div style="background:var(--panel);"></div><div style="background:var(--panel);"></div><div style="background:var(--panel);"></div><div style="background:var(--panel);"></div><div style="background:#E8F5E9; text-align:center; font-size:7pt; font-weight:bold;">EXIT</div>
        <div style="background:var(--panel);"></div><div style="background:var(--panel);"></div><div style="background:var(--panel);"></div><div style="background:var(--panel);"></div><div style="background:var(--panel);"></div><div style="background:var(--panel);"></div><div style="background:var(--panel);"></div><div style="background:var(--panel);"></div>
        <div style="background:var(--panel);"></div><div style="background:var(--panel);"></div><div style="background:var(--panel);"></div><div style="background:var(--panel);"></div><div style="background:var(--panel);"></div><div style="background:var(--panel);"></div><div style="background:var(--panel);"></div><div style="background:var(--panel);"></div>
        <div style="background:var(--panel);"></div><div style="background:var(--panel);"></div><div style="background:var(--panel);"></div><div style="background:var(--panel);"></div><div style="background:var(--panel);"></div><div style="background:var(--panel);"></div><div style="background:var(--panel);"></div><div style="background:var(--panel);"></div>
        <div style="background:var(--panel);"></div><div style="background:var(--panel);"></div><div style="background:var(--panel);"></div><div style="background:var(--panel);"></div><div style="background:var(--panel);"></div><div style="background:var(--panel);"></div><div style="background:var(--panel);"></div><div style="background:var(--panel);"></div>
        <div style="background:var(--panel);"></div><div style="background:var(--panel);"></div><div style="background:var(--panel);"></div><div style="background:var(--panel);"></div><div style="background:var(--panel);"></div><div style="background:var(--panel);"></div><div style="background:var(--panel);"></div><div style="background:var(--panel);"></div>
        <div style="background:var(--panel);"></div><div style="background:var(--panel);"></div><div style="background:var(--panel);"></div><div style="background:var(--panel);"></div><div style="background:var(--panel);"></div><div style="background:var(--panel);"></div><div style="background:var(--panel);"></div><div style="background:var(--panel);"></div>
        <div style="background:#E3F2FD; text-align:center; font-size:7pt; font-weight:bold;">START</div><div style="background:var(--panel);"></div><div style="background:var(--panel);"></div><div style="background:var(--panel);"></div><div style="background:var(--panel);"></div><div style="background:var(--panel);"></div><div style="background:var(--panel);"></div><div style="background:var(--panel);"></div>
      </div>
      <div style="font-size:8.5pt; display:flex; flex-direction:column; gap:4px;">
        <b>Xarita Belgilari (Shartli):</b>
        <span>[S] = Start Nuqtasi (Spawn)</span>
        <span>[#] = O'tib bo'lmas Devor / Qoya</span>
        <span>[L] = Lazer / Lava To'sig'i</span>
        <span>[*] = Maxfiy Sandiq / Tanga</span>
        <span>[C] = Checkpoint (Saqlash joyi)</span>
        <span>[E] = Exit / Boss Darvozasi</span>
      </div>
    </div>
  </section>

  <section class="sec">
    <div class="h"><span class="no">06</span><h2><span lang="uz">Top-Down Xarita AI Prompti</span><span lang="ru">Промпт Карты в ИИ</span><span lang="en">Top-Down Blueprint Prompt</span></h2></div>
    <div style="border:1px solid var(--rule); background:var(--panel); padding:10px; min-height:40px; font-family:monospace; font-size:8.5pt;">
      "Top-down 2D level map blueprint of ___________________________ with laser corridors, spawn area at bottom-left and exit vault at top-right, clean game schematic"
    </div>
  </section>

  <section class="sec">
    <div class="h"><span class="no">07</span><h2><span lang="uz">O'yin Qoidalari (Win / Fail States)</span><span lang="ru">Правила Игры</span><span lang="en">Gameplay Rules</span></h2></div>
    <div style="display:grid; grid-template-columns:1fr 1fr; gap:10px; font-size:8.5pt;">
      <div style="border:1px dashed var(--write); padding:6px;">
        <b>Qanday Qilib Yutadi (Win)?</b><br>
        1. ____________________________________<br>
        2. ____________________________________
      </div>
      <div style="border:1px dashed var(--write); padding:6px;">
        <b>Qachon Yutqazadi (Fail)?</b><br>
        1. ____________________________________<br>
        2. ____________________________________
      </div>
    </div>
  </section>

  <section class="sec">
    <div class="h"><span class="no">08</span><h2><span lang="uz">Finger-Playtest Audit</span><span lang="ru">Аудит Проходимости</span><span lang="en">Finger-Playtest Audit</span></h2></div>
    <div style="display:flex; flex-direction:column; gap:4px; font-size:8.5pt;">
      <label><input type="checkbox"> Sherigim barmoq bilan Startdan Exitga qadar berk ko'chalarsiz yetib bordi.</label>
      <label><input type="checkbox"> To'siqlar orasida kamida bitta xavfsiz Checkpoint mavjud.</label>
      <label><input type="checkbox"> Xarita biomi va Skybox osmon foni bir-biriga mos keladi.</label>
    </div>
  </section>
"""

l8_hw = """
  <p><b>1. Xaritani Tugatish:</b> 8x8 katakli xaritadagi barcha yo'laklarni, to'siqlarni va maxfiy joylarni to'liq chizib chiqing.</p>
  <p><b>2. Skybox Generatsiyasi:</b> O'z biomingizga mos 1 ta panoramali Skybox (osmon foni) rasmini AI da yarating.</p>
  <p><b>3. O'yin Shartlari:</b> Varaqadagi yutish va yutqazish shartlarini daftaringizga aniq qilib yozing.</p>
"""

l8_crit = """
  <div class="r"><span>8x8 xarita tuzilishi va to'siqlar mantiqli chizilgan</span><b>3</b></div>
  <div class="r"><span>Biomga mos sifatli Skybox foni yaratilgan</span><b>4</b></div>
  <div class="r"><span>Yutish va yutqazish qoidalari to'liq yozilgan</span><b>3</b></div>
"""

l8_nxt = {'uz': "O'yin Ovozlar Sehri: AI SFX va Musiqa", 'ru': "Магия Игрового Звука: AI SFX и Музыка", 'en': "Game Audio Magic: AI SFX & Music"}

ws8_html = build_worksheet('5-6-sinf', 2, 8, l8_t1, l8_s1, l8_k1, l8_p1, l8_t2, l8_s2, l8_p2, l8_hw, l8_crit, l8_nxt)
with open(os.path.join(l8_dir, 'varaqa.html'), 'w', encoding='utf-8') as f:
    f.write(ws8_html)

print("5-6 Week 2 Lesson 8 generated successfully!")
