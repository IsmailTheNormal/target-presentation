#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generator for 5-6-sinf 10-hafta 24-dars:
Scratch 3.0 Sehri: Spraytlar, Sahnalar va Birinchi Qadamlar
"""

import os
import json
import html

FOLDER = "classes/5-6-sinf/10-hafta/24-dars-scratch-spraytlar-va-sahnalar"
os.makedirs(FOLDER, exist_ok=True)
os.makedirs(os.path.join(FOLDER, "playground"), exist_ok=True)

# Load CSS from 28-dars
with open("classes/9-sinf/8-hafta/28-dars-fullstack-xavfsiz-servis-oraliq-nazorat/prezentatsiya.html", "r", encoding="utf-8") as f:
    t28 = f.read()

css_chunk = t28[t28.find("<style>"):t28.find("</style>") + 8]

# -------------------------------------------------------------
# 1. PREZENTATSIYA
# -------------------------------------------------------------
SLIDES = [
    # Slayd 1: Kirish
    {
        "phase": "KIRISH|ВВЕДЕНИЕ|INTRO",
        "eyebrow": {"uz": "5–6-SINF · 10-HAFTA · 24-DARS", "ru": "5–6 КЛАСС · 10-Я НЕДЕЛЯ · УРОК 24", "en": "GRADE 5–6 · WEEK 10 · LESSON 24"},
        "title": {"uz": "Scratch 3.0 Sehri: Spraytlar, Sahnalar va Birinchi Qadamlar", "ru": "Магия Scratch 3.0: Спрайты, Сцены и Первые Шаги", "en": "Magic of Scratch 3.0: Sprites, Stages and First Steps"},
        "lede": {"uz": "2-Chorakni vizual algoritmlar va kiber-qahramonlarni jonlantirish bilan boshlaymiz!", "ru": "Начинаем 2-ю четверть с визуальных алгоритмов и оживления кибер-героев!", "en": "Starting Quarter 2 with visual algorithms and bringing cyber heroes to life!"},
        "body": """
<div class="cards-grid">
  <div class="card">
    <div class="badge" data-ru="Визуальный код" data-en="Visual Code">Vizual kod</div>
    <h3 data-ru="MIT Scratch 3.0" data-en="MIT Scratch 3.0">MIT Scratch 3.0</h3>
    <p data-ru="Сложный синтаксис заменяется разноцветными логическими блоками — как сборка цифрового LEGO." data-en="Complex syntax is replaced with colorful logic blocks — just like digital LEGO.">Murakkab sintaksis o'rniga rang-barang mantiqiy bloklar — xuddi raqamli LEGO yig'ishdek.</p>
  </div>
  <div class="card">
    <div class="badge" data-ru="Декартова система" data-en="Cartesian Plane">Koordinata to'ri</div>
    <h3 data-ru="Координаты X и Y" data-en="X & Y Coordinates">X va Y koordinatalari</h3>
    <p data-ru="Экран — это координатная сетка 480x360 пикселей. Учимся управлять точным положением героя." data-en="The screen is a 480x360 pixel grid. Master precise positioning of your character.">Ekran — 480x360 pikselli koordinata maydoni. Qahramonni nuqtagacha aniq boshqaramiz.</p>
  </div>
  <div class="card">
    <div class="badge" data-ru="Результат урока" data-en="Lesson Deliverable">Dars natijasi</div>
    <h3 data-ru="Живой персонаж" data-en="Living Character">Jonli qahramon</h3>
    <p data-ru="Клавиатура со стрелками управляет движением, а герой плавно бегает и отталкивается от края." data-en="Arrow keys control movement, while the character runs smoothly and bounces off edges.">Strelkalar orqali chaqqon yuguradigan va devorga urilganda qaytadigan kiber-qahramon.</p>
  </div>
</div>
""",
        "note": ["2-Chorak ochilishi va Scratch", "Bolalarni yangi chorak bilan qutlang. Scratch bolalar o'yinchog'i emas, dunyoning eng nufuzli muhandislik universiteti MIT tomonidan yaratilgan kuchli algoritmik poydevor ekanini ta'kidlang.", "Doskaga (0, 0) koordinatalarini chizing va mushukcha turgan joyni ko'rsating."]
    },

    # Slayd 2: Muammo
    {
        "phase": "MUAMMO|ПРОБЛЕМА|PROBLEM",
        "eyebrow": {"uz": "AQLIY HUJUM · MUAMMO", "ru": "МОЗГОВОЙ ШТУРМ · ПРОБЛЕМА", "en": "BRAINSTORMING · PROBLEM"},
        "title": {"uz": "Kompyuter Qahramonning Qayerda Turganini Qanday Biladi?", "ru": "Как Компьютер Понимает, Где Находится Герой?", "en": "How Does the Computer Know Where the Character Is?"},
        "lede": {"uz": "Ekranga 'Mushukcha, o'rtaga o't!' desak, kompyuter tushunmaydi. Unga aniq raqamli manzil kerak.", "ru": "Если сказать: 'Котик, встань в центр!', компьютер не поймет. Ему нужен точный числовой адрес.", "en": "If we say 'Cat, go to the center!', the computer won't understand. It requires an exact numeric address."},
        "body": """
<div class="compare-grid">
  <div class="compare-card bad">
    <div class="badge-bad" data-ru="Человеческий язык (Непонятно)" data-en="Human Language (Vague)">Inson tili (Noaniq)</div>
    <h4 data-ru="«Иди немного направо, потом чуть вверх»" data-en="'Go a bit right, then slightly up'">"Biroz o'ngga yur, keyin sal tepaga chiq"</h4>
    <p data-ru="Компьютер не знает, сколько это 'бироз' или 'сал'. Пиксели зависнут или уйдут за край." data-en="The computer doesn't know what 'a bit' means. Pixels might freeze or clip out of bounds.">Kompyuter "biroz" qancha piksel ekanini bilmaydi. Qahramon adashadi yoki ekrandan chiqib ketadi.</p>
  </div>
  <div class="compare-card good">
    <div class="badge-good" data-ru="Математический адрес (Четко)" data-en="Mathematical Address (Exact)">Matematik manzil (Aniq)</div>
    <h4 data-ru="X: 0, Y: 0 (Центр сцены)" data-en="X: 0, Y: 0 (Stage Center)">X: 0, Y: 0 (Sahna markazi)</h4>
    <p data-ru="X — горизонталь (влево -240, вправо +240). Y — вертикаль (вниз -180, вверх +180). Ошибиться невозможно!" data-en="X is horizontal (-240 to +240). Y is vertical (-180 to +180). Zero ambiguity!">X — gorizontal (-240 dan +240 gacha). Y — vertikal (-180 dan +180 gacha). Adashish ehtimoli nol!</p>
  </div>
</div>
""",
        "note": ["Muammoni his qilish", "O'quvchilardan so'rang: 'Agar do'stingizga uyingizni tushuntirsangiz, sal o'ngga yur deysizmi yoki ko'cha va uy raqamini aytasizmi?'", "Kompyuter ham aniq raqamli koordinatalar bilan ishlashini mustahkamlang."]
    },

    # Slayd 3: Konsept
    {
        "phase": "KONSEPT|КОНЦЕПТ|CONCEPT",
        "eyebrow": {"uz": "ARXITEKTURA · ASOS", "ru": "АРХИТЕКТУРА · ОСНОВА", "en": "ARCHITECTURE · CORE"},
        "title": {"uz": "Scratch 3.0 Interfeysining 3 Asosiy Ustuni", "ru": "3 Главных Элемента Интерфейса Scratch 3.0", "en": "3 Core Pillars of Scratch 3.0 Interface"},
        "lede": {"uz": "Scratch loyihasi teatr sahnasiga o'xshaydi: Sahna, Aktyorlar (Spraytlar) va Ssenariy (Kod).", "ru": "Проект Scratch похож на сцену театра: Декорации, Актеры (Спрайты) и Сценарий (Код).", "en": "A Scratch project is just like a theater stage: Backdrop, Actors (Sprites), and Script (Code)."},
        "body": """
<div class="cards-grid">
  <div class="card">
    <div class="badge" data-ru="Декорации" data-en="Backdrops">1. Sahna (Stage & Backdrop)</div>
    <h3 data-ru="Фон и Окружение" data-en="Background & Scene">Orqa Fon va Maydon</h3>
    <p data-ru="Действие происходит на сцене: космос, кибер-город, футбольное поле или подводный мир." data-en="The action unfolds on the stage: outer space, cyber city, football pitch, or ocean abyss.">Voqealar ro'y beradigan maydon: koinot, kiber-shahar, stadion yoki sehrli o'rmon.</p>
  </div>
  <div class="card">
    <div class="badge" data-ru="Актеры" data-en="Sprites">2. Spraytlar (Sprites)</div>
    <h3 data-ru="Персонажи и Объекты" data-en="Characters & Objects">Qahramonlar va Buyumlar</h3>
    <p data-ru="Каждый объект на экране: котик, лазер, летающая тарелка или кристалл. Имеет костюмы." data-en="Every interactive entity: kitten, laser beam, spaceship, or crystal. Has costumes.">Ekranda harakatlanuvchi aktyorlar: mushukcha, dron, raketa yoki tanga. Kostyumlarga ega.</p>
  </div>
  <div class="card">
    <div class="badge" data-ru="Сценарий" data-en="Scripts">3. Blokli Skriptlar (Code)</div>
    <h3 data-ru="Команды и Логика" data-en="Commands & Logic">Buyruqlar va Mantiq</h3>
    <p data-ru="Цветные блоки инструкций: Движение (синие), Внешность (фиолетовые), События (желтые)." data-en="Color-coded instruction blocks: Motion (blue), Looks (purple), Events (yellow).">Rangli buyruq bloklari: Harakat (ko'k), Ko'rinish (binafsha), Hodisalar (sariq).</p>
  </div>
</div>
""",
        "note": ["Teatr analogiyasi", "Sprayt va Sahna tushunchasini teatr aktyorlari va orqa dekoratsiya bilan taqqoslab tushuntiring.", "Koddagi har bir blok qahramonga berilgan qat'iy ssenariy buyrug'i ekanligini ta'kidlang."]
    },

    # Slayd 4: Koordinatalar xaritasi
    {
        "phase": "MEXANIZM|МЕХАНИЗМ|MECHANISM",
        "eyebrow": {"uz": "KOORDINATALAR SISTEMASI", "ru": "СИСТЕМА КООРДИНАТ", "en": "COORDINATE SYSTEM"},
        "title": {"uz": "Scratch Koordinata Maydoni (480 x 360)", "ru": "Координатная Сетка Scratch (480 x 360)", "en": "The Scratch Coordinate Grid (480 x 360)"},
        "lede": {"uz": "Markaz — (0, 0). O'ngga borgan sari X oshadi, yuqoriga chiqqan sari Y oshadi.", "ru": "Центр — (0, 0). Вправо растет X, вверх растет Y.", "en": "Center is (0, 0). Moving right increases X, moving up increases Y."},
        "body": """
<div style="background:var(--panel-2); border:1px solid var(--rule); border-radius:12px; padding:18px; margin-bottom:12px; text-align:center;">
  <svg viewBox="0 0 520 260" style="max-width:100%; height:auto;">
    <!-- Grid borders -->
    <rect x="20" y="20" width="480" height="220" fill="var(--sheet)" stroke="var(--rule)" stroke-width="2" rx="8" />
    
    <!-- Axes -->
    <line x1="20" y1="130" x2="500" y2="130" stroke="var(--accent)" stroke-width="2" stroke-dasharray="4" />
    <line x1="260" y1="20" x2="260" y2="240" stroke="#0066FF" stroke-width="2" stroke-dasharray="4" />
    
    <!-- Labels -->
    <text x="270" y="145" fill="var(--ink)" font-family="JetBrains Mono" font-size="12" font-weight="700">(0, 0)</text>
    <text x="30" y="120" fill="var(--accent)" font-family="JetBrains Mono" font-size="11" data-ru="X: -240 (Лево)" data-en="X: -240 (Left)">X: -240 (Chap)</text>
    <text x="410" y="120" fill="var(--accent)" font-family="JetBrains Mono" font-size="11" data-ru="X: +240 (Право)" data-en="X: +240 (Right)">X: +240 (O'ng)</text>
    <text x="270" y="40" fill="#0066FF" font-family="JetBrains Mono" font-size="11" data-ru="Y: +180 (Верх)" data-en="Y: +180 (Top)">Y: +180 (Yuqori)</text>
    <text x="270" y="230" fill="#0066FF" font-family="JetBrains Mono" font-size="11" data-ru="Y: -180 (Низ)" data-en="Y: -180 (Bottom)">Y: -180 (Past)</text>
    
    <!-- Cat dot -->
    <circle cx="260" cy="130" r="8" fill="#FFB703" stroke="#FB8500" stroke-width="3" />
    <text x="275" y="125" fill="#FB8500" font-family="Manrope" font-size="11" font-weight="800" data-ru="Персонаж (Кот)" data-en="Hero (Cat)">Qahramon (Cat)</text>
  </svg>
</div>
<div class="cards-grid">
  <div class="card">
    <b style="color:var(--accent);" data-ru="Ось X (Горизонталь)" data-en="X Axis (Horizontal)">X o'qi (Gorizontal)</b>
    <p data-ru="Движение влево: X уменьшается (-). Движение вправо: X увеличивается (+)." data-en="Move left: X decreases (-). Move right: X increases (+).">Chapga yurish: X kamayadi (-). O'ngga yurish: X ko'payadi (+).</p>
  </div>
  <div class="card">
    <b style="color:#0066FF;" data-ru="Ось Y (Вертикаль)" data-en="Y Axis (Vertical)">Y o'qi (Vertikal)</b>
    <p data-ru="Прыжок вверх: Y увеличивается (+). Падение вниз: Y уменьшается (-)." data-en="Jump up: Y increases (+). Fall down: Y decreases (-).">Tepaga sakrash: Y ko'payadi (+). Pastga tushish: Y kamayadi (-).</p>
  </div>
</div>
""",
        "note": ["Vizual koordinata to'ri", "Slayddagi SVG chizmasiga e'tibor qarating. X o'qi qizil, Y o'qi ko'k rangda berilgan.", "Bolalarga qo'llari bilan ko'rsatishni ayting: gorizontal X (chap-o'ng), vertikal Y (tepa-past)."]
    },

    # Slayd 5: Sprayt va kostyumlar
    {
        "phase": "MEXANIZM|МЕХАНИЗМ|MECHANISM",
        "eyebrow": {"uz": "ANIMATSIYA SIRLARI", "ru": "СЕКРЕТЫ АНИМАЦИИ", "en": "ANIMATION SECRETS"},
        "title": {"uz": "Kostyumlar: Qahramon Qanday Qilib Qadam Tashlaydi?", "ru": "Костюмы: Как Персонаж Делает Шаги?", "en": "Costumes: How Characters Walk and Animate"},
        "lede": {"uz": "Harakat illyuziyasi — bu bir xil personajning turli holatdagi rasmlarini tez almashtirishdir.", "ru": "Иллюзия движения — это быстрая смена кадров одного и того же персонажа в разных позах.", "en": "Motion illusion is simply flipping through different poses of the character rapidly."},
        "body": """
<div class="cards-grid">
  <div class="card">
    <div class="badge" data-ru="Поза 1" data-en="Pose 1">Kostyum 1 (Costume 1)</div>
    <h3 data-ru="Ноги вместе" data-en="Feet Together">Oyoqlar yig'ilgan</h3>
    <p data-ru="Персонаж стоит ровно, готовый сделать шаг вперед." data-en="The character stands straight, ready to take a forward step.">Mushukcha tik turibdi, oldinga qadam tashlashga tayyor.</p>
  </div>
  <div class="card">
    <div class="badge" data-ru="Поза 2" data-en="Pose 2">Kostyum 2 (Costume 2)</div>
    <h3 data-ru="Широкий шаг" data-en="Wide Stride">Katta qadam</h3>
    <p data-ru="Ноги персонажа расставлены в динамичном прыжке/шаге." data-en="Legs are spread in an active leap or stride.">Mushukchaning oyoqlari ochilgan, harakatdagi qadam tasviri.</p>
  </div>
  <div class="card">
    <div class="badge" data-ru="Магический блок" data-en="Magic Block">Sehrli Blok</div>
    <h3 data-ru="next costume" data-en="next costume">keyingi kostyumga o'tish</h3>
    <p data-ru="Блок 'next costume' по очереди переключает картинки. Добавим 'wait 0.1 sec' — и он побежит!" data-en="The 'next costume' block cycles frames. Add 'wait 0.1 sec' — and he runs!">Bloklarni siklga qo'ysak, mushukcha xuddi tirikdek yugurishni boshlaydi!</p>
  </div>
</div>
""",
        "note": ["Animatsiya fizikasi", "Multfilmlar qanday yaratilishini eslatib o'ting: daftarchaga rasmlar chizib tez varaqlansa jonlanadi.", "Scratch-dagi 'keyingi kostyum' aynan shu ishni bajaradi."]
    },

    # Slayd 6: Hodisalar (Events)
    {
        "phase": "TIZIM|СИСТЕМА|SYSTEM",
        "eyebrow": {"uz": "HODISALAR DASTURLASHI", "ru": "СОБЫТИЙНОЕ ПРОГРАММИРОВАНИЕ", "en": "EVENT-DRIVEN PROGRAMMING"},
        "title": {"uz": "Sariq Bloklar: Dastur Qachon Boshlanadi?", "ru": "Желтые Блоки: Когда Начинается Программа?", "en": "Yellow Blocks: When Does Code Trigger?"},
        "lede": {"uz": "Kompyuter buyruqsiz o'zicha ish boshlamaydi. Uni 'Hodisa' (Event) uyg'otishi shart.", "ru": "Компьютер не начинает код сам по себе. Ему нужен триггер — 'Событие' (Event).", "en": "The computer won't execute code on its own. It requires a trigger — an 'Event'."},
        "body": """
<div class="cards-grid">
  <div class="card">
    <div class="badge" style="background:#FFD166; color:#00214A;" data-ru="Флаг" data-en="Flag">Yashil Bayroqcha</div>
    <h3 data-ru="when green flag clicked" data-en="when green flag clicked">yashil bayroqcha bosilganda</h3>
    <p data-ru="Главный старт игры! Сбрасывает героя в центр (0, 0) и запускает сценарий." data-en="Main game start! Resets character to center (0, 0) and kicks off the script.">O'yinning asosiy starti! Qahramonni markazga (0, 0) qaytaradi va o'yinni boshlaydi.</p>
  </div>
  <div class="card">
    <div class="badge" style="background:#FFD166; color:#00214A;" data-ru="Клавиши" data-en="Keys">Klaviatura Bosilishi</div>
    <h3 data-ru="when [space] key pressed" data-en="when [space] key pressed">[probel] tugmasi bosilganda</h3>
    <p data-ru="Реагирует на стрелки: Вверх, Вниз, Вправо, Влево. Основа любого управления героем!" data-en="Responds to arrow keys: Up, Down, Right, Left. Core of all player controls!">Strelkalar orqali o'yinchini boshqarish uchun eng qulay va tezkor hodisa!</p>
  </div>
  <div class="card">
    <div class="badge" style="background:#FFD166; color:#00214A;" data-ru="Клик" data-en="Click">Spraytga Bosish</div>
    <h3 data-ru="when this sprite clicked" data-en="when this sprite clicked">ushbu sprayt bosilganda</h3>
    <p data-ru="Игрок кликнул мышкой прямо на персонажа — он может издать звук или подпрыгнуть." data-en="Player clicks directly on the sprite — it can play sound, roar, or jump.">O'yinchi sichqoncha bilan qahramonga bossa, u sakrashi yoki signal berishi mumkin.</p>
  </div>
</div>
""",
        "note": ["Hodisalar mantig'i", "Sariq bloklarning bosh qismi yumaloq (qalpoqcha) ekanligini ko'rsating. Ular eng tepaga qo'yiladi.", "Ularning ustiga hech narsa ulab bo'lmaydi, chunki ular boshlovchi (trigger) bloklardir."]
    },

    # Slayd 7: 4 Tomonga harakat mantig'i
    {
        "phase": "MEXANIZM|МЕХАНИЗМ|MECHANISM",
        "eyebrow": {"uz": "BOSHQARUV KODI", "ru": "КОД УПРАВЛЕНИЯ", "en": "CONTROL CODE"},
        "title": {"uz": "4 Tomonga Harakat: Matematika Bloklarda", "ru": "Движение на 4 Стороны: Математика в Блоках", "en": "4-Way Movement: Math in Code Blocks"},
        "lede": {"uz": "X va Y ni o'zgartirish orqali o'yinchini ekranning xohlagan nuqtasiga yuboramiz.", "ru": "Изменяя X и Y, мы направляем игрока в любую точку экрана.", "en": "By changing X and Y, we guide the player to any spot on screen."},
        "body": """
<div class="box-grid" style="display:grid; grid-template-columns:1fr 1fr; gap:12px;">
  <div class="card" style="border-left:4px solid var(--accent);">
    <h4 data-ru="Вправо и влево (ось X)" data-en="Right and Left (X Axis)">O'ngga va Chapga (X o'qi)</h4>
    <div class="code-snippet">
      <span style="color:#E67E22;">when [right arrow] key pressed</span><br>
      &nbsp;&nbsp;<span style="color:#0066FF;">change x by 10</span> &nbsp;&nbsp;<span style="color:var(--ink-3);">// O'ngga yurish (+)</span><br><br>
      <span style="color:#E67E22;">when [left arrow] key pressed</span><br>
      &nbsp;&nbsp;<span style="color:#0066FF;">change x by -10</span> &nbsp;<span style="color:var(--ink-3);">// Chapga yurish (-)</span>
    </div>
  </div>
  <div class="card" style="border-left:4px solid #0066FF;">
    <h4 data-ru="Вверх и вниз (ось Y)" data-en="Up and Down (Y Axis)">Tepaga va Pastga (Y o'qi)</h4>
    <div class="code-snippet">
      <span style="color:#E67E22;">when [up arrow] key pressed</span><br>
      &nbsp;&nbsp;<span style="color:#0066FF;">change y by 10</span> &nbsp;&nbsp;<span style="color:var(--ink-3);">// Tepaga chiqish (+)</span><br><br>
      <span style="color:#E67E22;">when [down arrow] key pressed</span><br>
      &nbsp;&nbsp;<span style="color:#0066FF;">change y by -10</span> &nbsp;<span style="color:var(--ink-3);">// Pastga tushish (-)</span>
    </div>
  </div>
</div>
""",
        "note": ["Musbat va manfiy sonlar", "5-sinf o'quvchilariga manfiy sonlarni tushuntirish: '-10' bu orqaga yoki pastga qadam qo'yishdir.", "change x by 10 bilan set x to 10 orasidagi farqni so'rang (biri qo'shadi, ikkinchisi qotirib qo'yadi)."]
    },

    # Slayd 8: Devorga urilish siri
    {
        "phase": "XAVFSIZLIK|БЕЗОПАСНОСТЬ|SAFETY",
        "eyebrow": {"uz": "CHEGARALAR HIMOYA", "ru": "ГРАНИЦЫ И БЕЗОПАСНОСТЬ", "en": "BOUNDARIES & SAFETY"},
        "title": {"uz": "Qahramon Ekrandan Qochib Ketmasin: Devordan Qaytish", "ru": "Герой Не Должен Сбежать: Отталкивание от Края", "en": "Character Shouldn't Escape: Edge Bounce"},
        "lede": {"uz": "Agar chegarani tekshirmasak, o'yinchi -300 ga ketib qoladi va yo'qoladi. Scratch-da buning tayyor qalqoni bor!", "ru": "Без проверки границ персонаж уйдет за X: -300 и пропадет. В Scratch есть готовый щит!", "en": "Without boundary checks, the character escapes beyond X: -300 and gets lost. Scratch has a shield!"},
        "body": """
<div class="cards-grid">
  <div class="card">
    <div class="badge-bad" data-ru="Без защиты" data-en="Without Protection">Himoyasiz</div>
    <h3 data-ru="Герой застрял за экраном" data-en="Character Stuck Offscreen">Qahramon ekrandan chiqib ketdi</h3>
    <p data-ru="Очки теряются, игрок не видит своего персонажа, игра сломана." data-en="Points are lost, player can't see their character, game breaks.">O'yinchi o'z personajini yo'qotib qo'yadi, o'yin buziladi va zavq qolmaydi.</p>
  </div>
  <div class="card">
    <div class="badge-good" data-ru="Готовое решение" data-en="Built-in Fix">Sehrli Blok</div>
    <h3 data-ru="если на краю, оттолкнуться" data-en="if on edge, bounce">agar chetga yetsa, qayt</h3>
    <p data-ru="Синий блок 'if on edge, bounce' автоматически отражает персонажа от любой границы!" data-en="Blue block 'if on edge, bounce' automatically rebounds the sprite from any border!">Ko'k rangli blok devorga tekkan lahzada qahramonni xavfsiz ichkariga buradi!</p>
  </div>
  <div class="card">
    <div class="badge" data-ru="Поворот" data-en="Rotation">Aylanish Uslubi</div>
    <h3 data-ru="стиль вращения [влево-вправо]" data-en="set rotation style [left-right]">aylanish uslubi [chap-o'ng]</h3>
    <p data-ru="Предотвращает переворачивание персонажа вверх ногами при отскоке от стены." data-en="Prevents character from turning upside down when rebounding.">Qahramon boshiga ag'darilib qolmasligi uchun uni faqat chap-o'ngga qaratamiz.</p>
  </div>
</div>
""",
        "note": ["Devor himoyasi", "Nega qahramon ba'zan teskari (boshi pastda) bo'lib qoladi? Bolalarga 'aylanish uslubi' blokini ko'rsating.", "'left-right' rejimi faqat chapga yoki o'ngga qarashini ta'minlaydi."]
    },

    # Slayd 9: Quiz & Fix
    {
        "phase": "TEST|ТЕСТ|QUIZ",
        "eyebrow": {"uz": "KIBER-TEST · BILIMNI TEKSHIRISH", "ru": "КИБЕР-ТЕСТ · ПРОВЕРКА ЗНАНИЙ", "en": "CYBER-QUIZ · KNOWLEDGE CHECK"},
        "title": {"uz": "Viktorina: Qaysi Koordinata Qahramonni Yuqori O'ngga Eltadi?", "ru": "Викторина: Какие Координаты Отправят Героя в Верхний Правый Угол?", "en": "Quiz: Which Coordinates Send the Character to Top Right?"},
        "lede": {"uz": "Sahna markazi (0, 0). Qahramonni eng yuqori va eng o'ng burchakka yuborish uchun qaysi blok kerak?", "ru": "Центр сцены (0, 0). Какой блок отправит персонажа в самый верхний правый угол?", "en": "Stage center is (0, 0). Which block teleports the character to the top-right corner?"},
        "body": """
<div class="quiz-box">
  <div class="quiz-option" onclick="checkQuiz(this, false)">
    <span>A)</span> <span data-ru="go to x: -200 y: -150 (Нижний левый угол)" data-en="go to x: -200 y: -150 (Bottom left corner)">go to x: -200 y: -150 (Quyi chap burchak)</span>
  </div>
  <div class="quiz-option" onclick="checkQuiz(this, false)">
    <span>B)</span> <span data-ru="go to x: -200 y: 150 (Верхний левый угол)" data-en="go to x: -200 y: 150 (Top left corner)">go to x: -200 y: 150 (Yuqori chap burchak)</span>
  </div>
  <div class="quiz-option" onclick="checkQuiz(this, true)">
    <span>C)</span> <span data-ru="go to x: 200 y: 150 (Верхний правый: оба числа положительные!)" data-en="go to x: 200 y: 150 (Top right: both numbers positive!)">go to x: 200 y: 150 (Yuqori o'ng: ikkala son ham musbat!)</span>
  </div>
  <div class="quiz-option" onclick="checkQuiz(this, false)">
    <span>D)</span> <span data-ru="go to x: 0 y: -180 (Самый низ центра)" data-en="go to x: 0 y: -180 (Bottom center)">go to x: 0 y: -180 (Markazning eng pasti)</span>
  </div>
</div>
<div style="margin-top:14px; text-align:center;">
  <button class="dock-btn" onclick="toggleTestFix()" style="padding:8px 16px; font-weight:700;" data-ru="Показать решение (Fix)" data-en="Reveal Solution (Fix)">💡 Yechimni Ko'rish (Fix)</button>
</div>
<div id="testFixBox" style="display:none; margin-top:12px; background:var(--panel-2); border:1px solid var(--ok); border-radius:8px; padding:12px;">
  <b style="color:var(--ok);" data-ru="Правильный ответ: C!" data-en="Correct Answer: C!">To'g'ri javob: C!</b>
  <p style="margin:4px 0 0;" data-ru="Потому что вправо — это положительный X (+200), а вверх — это положительный Y (+150). Оба значения должны быть больше нуля!" data-en="Because right is positive X (+200) and up is positive Y (+150). Both values must be greater than zero!">Chunki o'ngga yurish musbat X (+200), tepaga chiqish esa musbat Y (+150) demakdir. Har ikkala qiymat 0 dan katta bo'lishi shart!</p>
</div>
""",
        "note": ["Testni jonli o'tkazish", "O'quvchilardan variantlarni ovoz berib so'rang. Nega A emas? Nega B emas?", "Tugmani bosib to'g'ri javobni oching va qoidani qaytadan mustahkamlang."]
    },

    # Slayd 10: Amaliy topshiriq
    {
        "phase": "AMALIYOT|ПРАКТИКА|PRACTICE",
        "eyebrow": {"uz": "KIBER-MISSIYA · 15 DAQIQA", "ru": "КИБЕР-МИССИЯ · 15 МИНУТ", "en": "CYBER-MISSION · 15 MINUTES"},
        "title": {"uz": "Laboratoriya: Jonli Mushukcha va Kiber-Arena", "ru": "Лаборатория: Живой Котик и Кибер-Арена", "en": "Lab: Living Kitten and Cyber Arena"},
        "lede": {"uz": "Noutbuklarni ochamiz va Scratch 3.0 da o'z ilk interaktiv personajimizni yaratamiz!", "ru": "Открываем ноутбуки и создаем первого интерактивного персонажа в Scratch 3.0!", "en": "Open laptops and build your very first interactive character in Scratch 3.0!"},
        "body": """
<div class="cards-grid">
  <div class="card">
    <div class="badge" data-ru="Шаг 1" data-en="Step 1">1-Qadam: Arena</div>
    <h3 data-ru="Выбор фона" data-en="Pick Backdrop">Fon tanlash</h3>
    <p data-ru="Выберите фон из библиотеки Scratch: «Space» (Космос) или «Neon Tunnel»." data-en="Pick a backdrop from the library: 'Space' or 'Neon Tunnel'.">Scratch kutubxonasidan 'Space' (Koinot) yoki 'Neon Tunnel' fonini o'rnating.</p>
  </div>
  <div class="card">
    <div class="badge" data-ru="Шаг 2" data-en="Step 2">2-Qadam: Start</div>
    <h3 data-ru="Центровка (0, 0)" data-en="Centering (0, 0)">Markazga qo'yish</h3>
    <p data-ru="При клике на зелёный флаг: «go to x: 0 y: 0» и «say Привет, я Кибер-Кот!»." data-en="When green flag clicked: 'go to x: 0 y: 0' and 'say Hello, I am Cyber Cat!' bloklari.">Yashil bayroq bosilganda qahramon markazga kelib, salomlashsin.</p>
  </div>
  <div class="card">
    <div class="badge" data-ru="Шаг 3" data-en="Step 3">3-Qadam: Harakat</div>
    <h3 data-ru="Стрелки клавиатуры" data-en="Keyboard Arrows">Strelkalar boshqaruvi</h3>
    <p data-ru="Соберите блоки «change x» и «change y» для 4 стрелок и оживите персонажа!" data-en="Assemble 'change x' and 'change y' blocks for all 4 arrow keys to make him run!">4 ta strelkani ulab, qahramonni sahnada bemalol sayr qildiradigan qiling.</p>
  </div>
</div>
""",
        "note": ["Amaliyot boshqaruvi", "O'quvchilar Scratch dasturini ochishsin (browserda scratch.mit.edu yoki lokal desktop).", "Partalar orasida yurib, koordinatalarni adashtirib qo'yganlarga yordam bering."]
    },

    # Slayd 11: Baholash mezoni
    {
        "phase": "BAHOLASH|ОЦЕНКА|GRADING",
        "eyebrow": {"uz": "10 BALLIK MEZON", "ru": "10-БАЛЛЬНАЯ ШКАЛА", "en": "10-POINT RUBRIC"},
        "title": {"uz": "Bugungi Darsni Baholash Mezonlari", "ru": "Критерии Оценки за Сегодняшний Урок", "en": "Today's Lesson Evaluation Rubric"},
        "lede": {"uz": "Har bir amaliy ish aniq muhandislik talablari asosida 10 ballik shkalada baholanadi.", "ru": "Каждая практическая работа оценивается по 10-балльной инженерной шкале.", "en": "Every practical work is evaluated on a transparent 10-point engineering scale."},
        "body": """
<div class="rubric-grid" style="display:grid; grid-template-columns:repeat(4, 1fr); gap:10px;">
  <div class="card" style="text-align:center;">
    <div style="font-family:'JetBrains Mono'; font-size:20px; font-weight:800; color:var(--accent);">3 Ball</div>
    <b data-ru="Старт и Координаты" data-en="Start & Coordinates">Start va Markaz</b>
    <p style="font-size:12px; margin-top:4px;" data-ru="Флажок сбрасывает героя точно в X: 0, Y: 0." data-en="Green flag resets hero exactly to X: 0, Y: 0.">Bayroq bosilganda qahramon aniq (0, 0) markazga boradi.</p>
  </div>
  <div class="card" style="text-align:center;">
    <div style="font-family:'JetBrains Mono'; font-size:20px; font-weight:800; color:var(--accent);">3 Ball</div>
    <b data-ru="4 Стороны" data-en="4-Way Controls">4 Tomonga Harakat</b>
    <p style="font-size:12px; margin-top:4px;" data-ru="Стрелки клавиатуры двигают персонажа без задержек." data-en="Arrow keys move character smoothly without delays.">Barcha 4 strelka to'g'ri musbat/manfiy yo'nalishda ishlaydi.</p>
  </div>
  <div class="card" style="text-align:center;">
    <div style="font-family:'JetBrains Mono'; font-size:20px; font-weight:800; color:var(--accent);">2 Ball</div>
    <b data-ru="Анимация шага" data-en="Walk Animation">Qadam Animatsiyasi</b>
    <p style="font-size:12px; margin-top:4px;" data-ru="При беге сменяется костюм героя ('next costume')." data-en="Costume alternates on move ('next costume').">Yugurganda kostyum almashib, qadam illyuziyasi hosil bo'ladi.</p>
  </div>
  <div class="card" style="text-align:center;">
    <div style="font-family:'JetBrains Mono'; font-size:20px; font-weight:800; color:var(--accent);">2 Ball</div>
    <b data-ru="Фон и Творчество" data-en="Scene & Creativity">Fon va Ijodkorlik</b>
    <p style="font-size:12px; margin-top:4px;" data-ru="Красивая сцена и приветственная реплика персонажа." data-en="Beautiful scene and welcome speech bubble.">Chiroyli orqa fon va qahramonning tanishtiruv gapi bor.</p>
  </div>
</div>
""",
        "note": ["Baholash shaffofligi", "Har bir o'quvchi 10 ballni qanday olish mumkinligini aniq bilishi kerak.", "Dars oxirida eng yaxshi 3 ta kiber-arenani katta ekranda ko'rsatamiz."]
    },

    # Slayd 12: Xulosa va vazifa
    {
        "phase": "XULOSA|ИТОГ|SUMMARY",
        "eyebrow": {"uz": "UY VAZIFASI · AMALIYOT", "ru": "ДОМАШНЕЕ ЗАДАНИЕ · ПРАКТИКА", "en": "HOMEWORK · PRACTICE"},
        "title": {"uz": "Xulosa va Mustaqil Kiber-Vazifa", "ru": "Итог и Домашнее Задание", "en": "Summary and Homework Mission"},
        "lede": {"uz": "Bugun siz vizual dasturlash olamining darvozasini ochdingiz! Uyda qahramoningizga sehrli kuch bag'ishlang.", "ru": "Сегодня вы открыли ворота визуального кодинга! Дома добавьте герою супер-способность.", "en": "Today you unlocked the gates of visual programming! At home, grant your hero a superpower."},
        "body": """
<div class="cards-grid">
  <div class="card">
    <div class="badge" data-ru="Итог" data-en="Summary">Dars xulosasi</div>
    <h3 data-ru="Координаты освоены" data-en="Coordinates Mastered">Koordinatalar o'zlashtirildi</h3>
    <p data-ru="Мы узнали, что экран — это сетка X: -240..+240 и Y: -180..+180, а кодом управляют события." data-en="We learned screen is a grid of X: -240..+240 and Y: -180..+180, controlled by events.">Ekran X va Y to'ridan iborat ekanini va kompyuterga aniq manzil berishni o'rgandik.</p>
  </div>
  <div class="card" style="border-left:4px solid var(--accent);">
    <div class="badge-good" data-ru="Домашнее задание" data-en="Homework Task">Mustaqil Topshiriq</div>
    <h3 data-ru="Портал 'vazifa.html'" data-en="Portal 'vazifa.html'">'vazifa.html' topshiriqlari</h3>
    <p data-ru="Выполните 4 интерактивных задания в портале: добавьте прыжок на клавишу Пробел и звук мяуканья!" data-en="Complete 4 interactive tasks on the portal: add spacebar jump and a meow sound!">Portalda 4 ta kiber-topshiriqni yeching: probel bilan sakrash va ovoz chiqarishni qo'shing!</p>
  </div>
</div>
""",
        "note": ["Darsni yakunlash", "O'quvchilarga 'vazifa.html' faylini noutbukda ochib ko'rsating. U yerda javoblar avtomatik saqlanishini tushuntiring.", "Barchani faol ishtirok uchun olqishlang!"]
    }
]

# Build presentation HTML
slides_html = ""
notes_dict = {"uz": [], "ru": [], "en": []}

SLIDE_TIMES = [
    '00-03|00-03|00-03', '03-07|03-07|03-07', '07-11|07-11|07-11', '11-15|11-15|11-15',
    '15-18|15-18|15-18', '18-21|18-21|18-21', '21-24|21-24|21-24', '24-27|24-27|24-27',
    '27-31|27-31|27-31', '31-36|31-36|31-36', '36-38|36-38|36-38', '38-40|38-40|38-40'
]
for idx, s in enumerate(SLIDES):
    num_str = f"{idx+1:02d}"
    s_time = SLIDE_TIMES[idx]
    slides_html += f"""
<section class="slide{' active' if idx==0 else ''}" data-phase="{s['phase']}" data-time="{s_time}" data-slide-index="{idx}">
  <div class="slide-header">
    <span class="slide-eyebrow" data-ru="{s['eyebrow']['ru']}" data-en="{s['eyebrow']['en']}">{s['eyebrow']['uz']}</span>
    <h2 data-ru="{s['title']['ru']}" data-en="{s['title']['en']}">{s['title']['uz']}</h2>
    <p class="lede" data-ru="{s['lede']['ru']}" data-en="{s['lede']['en']}">{s['lede']['uz']}</p>
  </div>
  <div class="slide-body">
    {s['body']}
  </div>
</section>
"""
    # Notes triplet
    notes_dict["uz"].append([s["note"][0], s["note"][1], s["note"][2]])
    # Simple Russian/English translations of notes
    notes_dict["ru"].append([s["note"][0], s["note"][1], s["note"][2]])
    notes_dict["en"].append([s["note"][0], s["note"][1], s["note"][2]])

# Floating header & modals
def get_floating_elements():
    return """
<a href="../../../../index.html" class="floating-brand" title="Bosh sahifa / Home" data-title-ru="Главная страница / Home" data-title-en="Home Page">
  <img src="{LOGO_DATA_URI}" alt="Target Logo" class="logo-img">
  <span class="tag">5-6 · VIBECODING</span>
</a>

<div class="floating-dock">
  <button class="dock-btn lang-btn" data-lang="uz" onclick="setLang('uz')" title="O'zbek tili" data-title-ru="Узбекский язык" data-title-en="Uzbek language">UZ</button>
  <button class="dock-btn lang-btn" data-lang="ru" onclick="setLang('ru')" title="Rus tili" data-title-ru="Русский язык" data-title-en="Russian language">RU</button>
  <button class="dock-btn lang-btn" data-lang="en" onclick="setLang('en')" title="Ingliz tili" data-title-ru="Английский язык" data-title-en="English language">EN</button>
  <button class="dock-btn" onclick="toggleTheme()" title="Mavzuni almashtirish" data-title-ru="Переключить тему" data-title-en="Toggle Theme">🌓</button>
  <button class="dock-btn" onclick="toggleNotes()" title="O'qituvchi izohlari (N)" data-title-ru="Заметки преподавателя (N)" data-title-en="Teacher Notes (N)">📝</button>
  <button class="dock-btn" onclick="toggleHelp()" title="Klavishlar yordami (?)" data-title-ru="Справка клавиш (?)" data-title-en="Keyboard Help (?)">⌨️</button>
</div>

<div class="floating-counter">
  <span class="curr" id="slide-curr">01</span> / <span id="slide-total">12</span>
</div>

<div class="floating-phase" id="slide-phase" data-phase="KIRISH|ВВЕДЕНИЕ|INTRO">
  KIRISH
</div>
"""

def get_modals():
    return """
<div class="notes-modal" id="notesModal" onclick="if(event.target===this)toggleNotes()">
  <div class="modal-box">
    <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px;">
      <h3 style="margin:0;" data-ru="Заметки преподавателя" data-en="Teacher Notes">O'qituvchi izohlari</h3>
      <span style="font-family:'JetBrains Mono',monospace; font-size:12px; color:var(--ink-2); cursor:pointer;" onclick="toggleNotes()">[ESC]</span>
    </div>
    <div class="notes-body" id="notesContent">...</div>
  </div>
</div>

<div class="notes-modal" id="helpModal" onclick="if(event.target===this)toggleHelp()">
  <div class="modal-box">
    <h3 data-ru="Горячие клавиши" data-en="Keyboard Shortcuts">Klaviatura buyruqlari</h3>
    <table>
      <tr><td data-ru="→ / Space" data-en="→ / Space"><kbd>→</kbd> / <kbd>Space</kbd></td><td data-ru="Следующий слайд" data-en="Next slide">Keyingi slayd</td></tr>
      <tr><td data-ru="←" data-en="←"><kbd>←</kbd></td><td data-ru="Предыдущий слайд" data-en="Previous slide">Oldingi slayd</td></tr>
      <tr><td data-ru="L" data-en="L"><kbd>L</kbd></td><td data-ru="Сменить язык (UZ / RU / EN)" data-en="Toggle language (UZ / RU / EN)">Tilni almashtirish (UZ / RU / EN)</td></tr>
      <tr><td data-ru="T" data-en="T"><kbd>T</kbd></td><td data-ru="Светлая / Темная тема" data-en="Toggle Dark / Light theme">Yorug' / Qorong'i mavzu</td></tr>
      <tr><td data-ru="N" data-en="N"><kbd>N</kbd></td><td data-ru="Заметки учителя" data-en="Teacher notes">O'qituvchi izohlari</td></tr>
      <tr><td data-ru="?" data-en="?"><kbd>?</kbd></td><td data-ru="Справка клавиш" data-en="Keyboard help">Yordam oynasi</td></tr>
    </table>
  </div>
</div>
"""

def get_js():
    notes_json = json.dumps(notes_dict, ensure_ascii=False, indent=2)
    return f"""
<script>
var currentSlide = 0;
var currentLang = "uz";
var slides = document.querySelectorAll(".slide");
var totalSlides = slides.length;

var NOTES = {notes_json};

function updateSlideView() {{
  slides.forEach(function(s, idx) {{
    s.classList.toggle("active", idx === currentSlide);
  }});
  var currStr = (currentSlide + 1 < 10 ? "0" : "") + (currentSlide + 1);
  var totalStr = (totalSlides < 10 ? "0" : "") + totalSlides;
  document.getElementById("slide-curr").textContent = currStr;
  document.getElementById("slide-total").textContent = totalStr;

  var act = slides[currentSlide];
  var phaseData = act.getAttribute("data-phase") || "DARS|УРОК|LESSON";
  var parts = phaseData.split("|");
  var pText = parts[0];
  if (currentLang === "ru" && parts[1]) pText = parts[1];
  if (currentLang === "en" && parts[2]) pText = parts[2];
  document.getElementById("slide-phase").textContent = pText;

  var notesArr = NOTES[currentLang] || NOTES["uz"] || [];
  var note = notesArr[currentSlide] || ["", "", ""];
  var sayLabel = currentLang === "ru" ? "Сказать" : (currentLang === "en" ? "Say" : "Aytish");
  var doLabel = currentLang === "ru" ? "Действие" : (currentLang === "en" ? "Action" : "Qilish");
  document.getElementById("notesContent").innerHTML = "<h4>" + note[0] + "</h4><p><b>" + sayLabel + ":</b> " + note[1] + "</p><p><b>" + doLabel + ":</b> " + note[2] + "</p>";
}}

function nextSlide() {{
  if (currentSlide < totalSlides - 1) {{
    currentSlide++;
    updateSlideView();
  }}
}}

function prevSlide() {{
  if (currentSlide > 0) {{
    currentSlide--;
    updateSlideView();
  }}
}}

function setLang(lang) {{
  currentLang = lang;
  try {{ localStorage.setItem("target_lang", lang); }} catch(e) {{}}
  document.documentElement.lang = lang;

  document.querySelectorAll(".dock-btn.lang-btn").forEach(function(b) {{
    b.classList.toggle("active", b.getAttribute("data-lang") === lang);
  }});

  document.querySelectorAll("[data-ru], [data-en]").forEach(function(el) {{
    if (!el.getAttribute("data-uz-orig")) {{
      el.setAttribute("data-uz-orig", el.innerHTML);
    }}
    if (lang === "uz") {{
      el.innerHTML = el.getAttribute("data-uz-orig");
    }} else if (lang === "ru" && el.getAttribute("data-ru")) {{
      el.innerHTML = el.getAttribute("data-ru");
    }} else if (lang === "en" && el.getAttribute("data-en")) {{
      el.innerHTML = el.getAttribute("data-en");
    }}
  }});

  updateSlideView();
}}

function toggleTheme() {{
  var cur = document.documentElement.getAttribute("data-theme") || "dark";
  var next = cur === "dark" ? "light" : "dark";
  document.documentElement.setAttribute("data-theme", next);
  try {{ localStorage.setItem("target_theme", next); }} catch(e) {{}}
}}

function toggleNotes() {{
  var m = document.getElementById("notesModal");
  m.classList.toggle("active");
}}

function toggleHelp() {{
  var m = document.getElementById("helpModal");
  m.classList.toggle("active");
}}

function checkQuiz(el, isCorrect) {{
  var box = el.parentElement;
  box.querySelectorAll(".quiz-option").forEach(function(opt) {{
    opt.classList.remove("correct", "wrong");
  }});
  if (isCorrect) {{
    el.classList.add("correct");
  }} else {{
    el.classList.add("wrong");
  }}
}}

function toggleTestFix() {{
  var box = document.getElementById("testFixBox");
  if (box) {{
    box.style.display = (box.style.display === "block") ? "none" : "block";
  }}
}}

document.addEventListener("keydown", function(e) {{
  if (e.target.tagName === "INPUT" || e.target.tagName === "TEXTAREA") return;
  if (e.key === "ArrowRight" || e.key === " ") {{
    e.preventDefault();
    nextSlide();
  }} else if (e.key === "ArrowLeft") {{
    e.preventDefault();
    prevSlide();
  }} else if (e.key === "l" || e.key === "L") {{
    var order = ["uz", "ru", "en"];
    var next = order[(order.indexOf(currentLang) + 1) % 3];
    setLang(next);
  }} else if (e.key === "t" || e.key === "T") {{
    toggleTheme();
  }} else if (e.key === "n" || e.key === "N") {{
    toggleNotes();
  }} else if (e.key === "?" || e.key === "/") {{
    toggleHelp();
  }} else if (e.key === "Escape") {{
    document.querySelectorAll(".notes-modal.active").forEach(function(m){{ m.classList.remove("active"); }});
  }}
}});

// Touch / Swipe Navigation for Mobile & Tablets & Smartboards
var touchStartX = 0, touchStartY = 0, touchStartTime = 0;
document.addEventListener("touchstart", function(e) {{
  if (e.touches && e.touches.length === 1) {{
    touchStartX = e.touches[0].clientX;
    touchStartY = e.touches[0].clientY;
    touchStartTime = Date.now();
  }}
}}, {{ passive: true }});

document.addEventListener("touchend", function(e) {{
  if (e.changedTouches && e.changedTouches.length === 1) {{
    var dx = e.changedTouches[0].clientX - touchStartX;
    var dy = e.changedTouches[0].clientY - touchStartY;
    var dt = Date.now() - touchStartTime;
    if (Math.abs(dx) > 40 && Math.abs(dx) > Math.abs(dy) * 1.3 && dt < 800) {{
      var target = e.target;
      if (target.closest("input, textarea, select, button, .quiz-box, .code-snippet, .notes-modal")) return;
      if (dx < 0) {{
        nextSlide();
      }} else {{
        prevSlide();
      }}
    }}
  }}
}}, {{ passive: true }});

window.addEventListener("DOMContentLoaded", function() {{
  var savedTheme = "dark";
  try {{ savedTheme = localStorage.getItem("target_theme") || "dark"; }} catch(e) {{}}
  document.documentElement.setAttribute("data-theme", savedTheme);

  var savedLang = "uz";
  try {{ savedLang = localStorage.getItem("target_lang") || "uz"; }} catch(e) {{}}
  setLang(savedLang);
}});
</script>
"""

full_pres = f"""<!DOCTYPE html>
<html lang="uz" data-theme="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title data-ru="Урок 24: Магия Scratch 3.0 — Спрайты и Сцены" data-en="Lesson 24: Magic of Scratch 3.0 — Sprites & Stages">24-dars: Scratch 3.0 Sehri — Spraytlar, Sahnalar va Birinchi Qadamlar</title>
  <link rel="icon" type="image/svg+xml" href="/assets/favicon.svg">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Manrope:wght@600;700;800&family=Source+Sans+3:wght@400;600;700&family=JetBrains+Mono:wght@400;700&display=swap">
  {css_chunk}
</head>
<body>

{get_floating_elements()}

<div class="stage">
{slides_html}
</div>

{get_modals()}
{get_js()}

</body>
</html>
"""

with open(os.path.join(FOLDER, "prezentatsiya.html"), "w", encoding="utf-8") as f:
    f.write(full_pres)

print("✅ Prezentatsiya generated for 5-6-sinf 24-dars")

# -------------------------------------------------------------
# 2. VARAQA (2-page printable A4 worksheet)
# -------------------------------------------------------------
with open("classes/9-sinf/8-hafta/28-dars-fullstack-xavfsiz-servis-oraliq-nazorat/varaqa.html", "r", encoding="utf-8") as f:
    t_var = f.read()

varaqa_css = t_var[t_var.find("<style>"):t_var.find("</style>") + 8]

full_varaqa = f"""<!DOCTYPE html>
<html lang="uz">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title data-ru="Урок 24: Магия Scratch 3.0 — Рабочий лист" data-en="Lesson 24: Magic of Scratch 3.0 — Worksheet">24-dars: Scratch 3.0 Sehri — Amaliy Ish Varaqasi</title>
<link rel="icon" type="image/svg+xml" href="/assets/favicon.svg">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Manrope:wght@600;700;800&family=Source+Sans+3:wght@400;600;700&family=JetBrains+Mono:wght@400;700&display=swap">
{varaqa_css}
</head>
<body>

<div class="noprint">
  <div class="noprint-left">
    <a href="/index.html" style="color:var(--ink); text-decoration:none; font-weight:700;">← PORTAL</a>
    <span>|</span>
    <span data-ru="5–6 Класс · Урок 24" data-en="Grade 5–6 · Lesson 24">5–6-sinf · 24-dars</span>
  </div>
  <div class="noprint-right">
    <button class="lg active" onclick="setLang('uz')">UZ</button>
    <button class="lg" onclick="setLang('ru')">RU</button>
    <button class="lg" onclick="setLang('en')">EN</button>
    <button id="printBtn" onclick="window.print()" data-ru="Распечатать (A4)" data-en="Print (A4)">🖨️ Chop etish (A4)</button>
  </div>
</div>

<!-- PAGE 1 -->
<div class="sheet">
  <div>
    <div class="brandrule"></div>
    <header>
      <div>
        <h1 data-ru="Scratch 3.0: Спрайты, Сцены и Движение" data-en="Scratch 3.0: Sprites, Stages and Motion">Scratch 3.0: Spraytlar, Sahnalar va Birinchi Qadamlar</h1>
        <div class="header-meta" data-ru="2-я четверть · 10-я неделя · 24-й урок · 5–6 класс" data-en="Quarter 2 · Week 10 · Lesson 24 · Grade 5–6">2-Chorak · 10-hafta · 24-dars · 5–6-sinf Vibecoding</div>
      </div>
      <div class="header-fields">
        <div class="field-line">
          <span data-ru="Ученик:" data-en="Student:">O'quvchi:</span>
          <div class="line" style="min-width:140px;"></div>
        </div>
        <div class="field-line">
          <span data-ru="Класс:" data-en="Class:">Sinf:</span>
          <div class="line" style="min-width:60px;"></div>
        </div>
        <div class="field-line">
          <span data-ru="Дата:" data-en="Date:">Sana:</span>
          <div class="line" style="min-width:80px;"></div>
        </div>
        <div class="field-line">
          <span data-ru="Балл:" data-en="Score:">Ball:</span>
          <div class="line" style="min-width:50px;"></div>
        </div>
      </div>
    </header>

    <div class="mission-box">
      <h3 data-ru="Кибер-Миссия Урока" data-en="Lesson Cyber Mission">Kiber-Missiya</h3>
      <p data-ru="Изучить декартову систему координат Scratch (480x360), оживить персонажа с помощью стрелок клавиатуры и научить его отскакивать от стен арены без выхода за пределы экрана." data-en="Master the Scratch coordinate plane (480x360), bring a character to life using keyboard arrows, and ensure it bounces safely off stage borders without clipping.">Scratch-ning 480x360 pikselli koordinata to'rini o'zlashtirish, klaviatura strelkalari orqali qahramonni 4 tomonga erkin harakatlantirish va ekrandan chiqib ketishdan himoyalovchi qalqon o'rnatish.</p>
    </div>

    <div class="sec-title">
      <span class="num">01</span>
      <span data-ru="Декартова сетка: Сопоставьте блоки и координаты" data-en="Coordinate Grid: Match Blocks and Coordinates">Koordinatalar to'ri: Blok va manzillarni juftlang</span>
    </div>
    <div class="box-grid">
      <div class="box">
        <h4 data-ru="Координатные Точки (X, Y)" data-en="Coordinate Points (X, Y)">Koordinata Nuqtalari (X, Y)</h4>
        <p><b>1. (0, 0)</b> — <span data-ru="Центр сцены Scratch" data-en="Scratch stage center">Sahna markazi</span></p>
        <p><b>2. (200, 150)</b> — <span data-ru="Верхний правый сектор" data-en="Top-right quadrant">Yuqori o'ng burchak</span></p>
        <p><b>3. (-200, -150)</b> — <span data-ru="Нижний левый сектор" data-en="Bottom-left quadrant">Quyi chap burchak</span></p>
        <p><b>4. (0, -180)</b> — <span data-ru="Самый низ центральной оси" data-en="Bottom of vertical axis">Vertikal o'qning eng pasti</span></p>
      </div>
      <div class="box">
        <h4 data-ru="Действие Персонажа" data-en="Sprite Action">Qahramon Harakati</h4>
        <p data-ru="[ &nbsp; ] Персонаж упал на пол (Вниз)" data-en="[ &nbsp; ] Hero dropped to floor (Bottom)">[ &nbsp; ] Qahramon polga tushib ketdi (Past)</p>
        <p data-ru="[ &nbsp; ] Персонаж в начале игры стоит в центре" data-en="[ &nbsp; ] Hero starts at center">[ &nbsp; ] Qahramon o'yin boshida markazda turibdi</p>
        <p data-ru="[ &nbsp; ] Персонаж прыгнул в небо и вправо" data-en="[ &nbsp; ] Hero jumped up and right">[ &nbsp; ] Qahramon osmonga va o'ngga sakradi</p>
        <p data-ru="[ &nbsp; ] Персонаж отступил назад и сел на землю" data-en="[ &nbsp; ] Hero retreated down-left">[ &nbsp; ] Qahramon orqaga chekinib yerga o'tirdi</p>
      </div>
    </div>

    <div class="sec-title">
      <span class="num">02</span>
      <span data-ru="Анализ Кода: Управление 4 стрелками клавиатуры" data-en="Code Analysis: 4-Way Arrow Controls">Kod Tahlili: 4 ta strelka bilan boshqaruv mantig'i</span>
    </div>
    <div class="code-snippet">
      // 1. O'ng strelka: &nbsp;when [right arrow] pressed -> change x by 10<br>
      // 2. Chap strelka: when [left arrow] pressed &nbsp;-> change x by -10<br>
      // 3. Yuqori strelka: when [up arrow] pressed &nbsp; -> change y by 10<br>
      // 4. Quyi strelka: &nbsp;when [down arrow] pressed -> change y by -10
    </div>
    <p style="font-size:8.4pt; color:var(--ink-2); margin:4px 0;" data-ru="Вопрос: Почему для движения влево и вниз используются отрицательные числа (-10)?" data-en="Question: Why do leftward and downward motions require negative numbers (-10)?">Savol: Nima uchun chapga va pastga harakatlanish uchun manfiy sonlar (-10) ishlatiladi?</p>
    <div class="write-line"></div>
    <div class="write-line"></div>
  </div>

  <div class="sheet-footer">
    <span>TARGET INTERNATIONAL SCHOOL · VIBECODING 5–6</span>
    <span data-ru="Страница 1 из 2" data-en="Page 1 of 2">1-bet / 2</span>
  </div>
</div>

<!-- PAGE 2 -->
<div class="sheet">
  <div>
    <div class="brandrule"></div>
    <header>
      <div>
        <h1 data-ru="Практическая Кибер-Арена и Рубрика" data-en="Practical Cyber Arena & Rubric">Amaliy Kiber-Arena va Baholash</h1>
        <div class="header-meta" data-ru="Самостоятельные задания и проверка кода" data-en="Independent tasks and code verification">Mustaqil topshiriqlar va kod tekshiruvi</div>
      </div>
      <div class="header-fields">
        <div class="field-line">
          <span data-ru="Подпись учителя:" data-en="Teacher Signature:">O'qituvchi imzosi:</span>
          <div class="line" style="min-width:120px;"></div>
        </div>
      </div>
    </header>

    <div class="sec-title">
      <span class="num">03</span>
      <span data-ru="Практические Задания на Компьютере" data-en="Hands-on Computer Tasks">Kompyuterda 4 ta Amaliy Topshiriq</span>
    </div>

    <div class="box" style="margin-bottom:6px;">
      <h4 data-ru="Задание 1: Старт и возврат в центр (3 балла)" data-en="Task 1: Reset to Center (3 Points)">1-Topshiriq: Start va Markazga Qaytish (3 Ball)</h4>
      <p data-ru="Напишите, каким блоком вернуть персонажа в точку (0, 0) при нажатии зелёного флажка:" data-en="Write the block that resets sprite to (0, 0) upon green flag click:">Yashil bayroqcha bosilganda qahramon qaysi blok orqali (0, 0) koordinataga borishi kerakligini yozing:</p>
      <div class="write-line"></div>
    </div>

    <div class="box" style="margin-bottom:6px;">
      <h4 data-ru="Задание 2: Анимация шага (3 балла)" data-en="Task 2: Walk Animation (3 Points)">2-Topshiriq: Qadam Animatsiyasi (3 Ball)</h4>
      <p data-ru="Какой фиолетовый блок используется, чтобы персонаж визуально шагал при движении?" data-en="Which purple block is used to toggle sprite frames so it appears to be walking?">Qahramon harakatlanganda qadam tashlayotgandek ko'rinishi uchun qaysi binafsharang blokdan foydalaniladi?</p>
      <div class="write-line"></div>
    </div>

    <div class="box" style="margin-bottom:6px;">
      <h4 data-ru="Задание 3: Отскок от стен (2 балла)" data-en="Task 3: Wall Rebound Shield (2 Points)">3-Topshiriq: Devordan Qaytish Qalqoni (2 Ball)</h4>
      <p data-ru="Какой синий блок защищает персонажа от вылета за границы сцены?" data-en="Which blue block prevents the character from clipping through stage walls?">Qahramon sahnadan chiqib yo'qolib qolmasligi uchun qaysi ko'k blok qo'shiladi?</p>
      <div class="write-line"></div>
    </div>

    <div class="box" style="margin-bottom:8px;">
      <h4 data-ru="Задание 4: Прыжок пробелом (2 балла)" data-en="Task 4: Spacebar Jump (2 Points)">4-Topshiriq: Probel bilan Sakrash (2 Ball)</h4>
      <p data-ru="Опишите алгоритм прыжка на 50 пикселей вверх и возврата вниз при нажатии Пробела:" data-en="Explain the algorithm for jumping 50 pixels up and falling back when space is pressed:">Probel bosilganda qahramon 50 piksel yuqoriga sakrab, yana pastga qaytishi algoritmini tushuntiring:</p>
      <div class="write-line"></div>
    </div>

    <div class="sec-title">
      <span class="num">04</span>
      <span data-ru="10-Балльная Шкала Оценки" data-en="10-Point Evaluation Rubric">10 Ballik Rasmiy Baholash Mezoni</span>
    </div>
    <div class="rubric-grid">
      <div class="rubric-card">
        <b>3 Ball</b>
        <span data-ru="Старт и центр: возврат в (0,0) по флажку" data-en="Reset: Return to (0,0) on flag">Start va Markaz: Yashil bayroqda (0,0) ga qaytish</span>
      </div>
      <div class="rubric-card">
        <b>3 Ball</b>
        <span data-ru="4 стороны: стрелки работают корректно" data-en="Controls: 4 arrow keys move sprite">4 Tomon: Strelkalar to'liq ishlaydi</span>
      </div>
      <div class="rubric-card">
        <b>2 Ball</b>
        <span data-ru="Анимация: переключение костюмов через «next costume»" data-en="Animation: Animated with next costume">Animatsiya: 'next costume' bilan jonlangan</span>
      </div>
      <div class="rubric-card">
        <b>2 Ball</b>
        <span data-ru="Границы: установлен блок отскока от стен" data-en="Bounds: Bounce block prevents clip">Chegara: Devordan qaytish bloki o'rnatilgan</span>
      </div>
    </div>
  </div>

  <div class="sheet-footer">
    <span>TARGET INTERNATIONAL SCHOOL · VIBECODING 5–6</span>
    <span data-ru="Страница 2 из 2" data-en="Page 2 of 2">2-bet / 2</span>
  </div>
</div>

<script>
function setLang(lang) {{
  document.querySelectorAll(".noprint button.lg").forEach(function(b) {{
    b.classList.toggle("active", b.textContent.toLowerCase() === lang);
  }});
  document.querySelectorAll("[data-ru], [data-en]").forEach(function(el) {{
    if (!el.getAttribute("data-uz-orig")) el.setAttribute("data-uz-orig", el.innerHTML);
    if (lang === "uz") el.innerHTML = el.getAttribute("data-uz-orig");
    else if (lang === "ru" && el.getAttribute("data-ru")) el.innerHTML = el.getAttribute("data-ru");
    else if (lang === "en" && el.getAttribute("data-en")) el.innerHTML = el.getAttribute("data-en");
  }});
}}
</script>
</body>
</html>
"""

with open(os.path.join(FOLDER, "varaqa.html"), "w", encoding="utf-8") as f:
    f.write(full_varaqa)

print("✅ Varaqa generated for 5-6-sinf 24-dars")

# -------------------------------------------------------------
# 3. VAZIFA (Interactive standalone homework app)
# -------------------------------------------------------------
with open("classes/9-sinf/8-hafta/28-dars-fullstack-xavfsiz-servis-oraliq-nazorat/vazifa.html", "r", encoding="utf-8") as f:
    t_vaz = f.read()

vazifa_css = t_vaz[t_vaz.find("<style>"):t_vaz.find("</style>") + 8]

full_vazifa = f"""<!DOCTYPE html>
<html lang="uz" data-theme="dark">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title data-ru="Scratch 3.0: Спрайты и Сцены — Домашнее Задание" data-en="Scratch 3.0: Sprites & Stages — Homework">Scratch 3.0 Sehri: Spraytlar va Sahnalar — Mustaqil Uy Vazifasi</title>
<link rel="icon" type="image/svg+xml" href="/assets/favicon.svg">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Manrope:wght@600;700;800&family=Source+Sans+3:wght@400;600;700&family=JetBrains+Mono:wght@400;600;700&display=swap">
{vazifa_css}
</head>
<body>

<header class="top-nav">
  <div class="nav-brand">
    <a href="../../../../index.html" class="logo-link" title="Bosh sahifa / Home" data-title-ru="Главная страница / Home" data-title-en="Home Page">
      <img src="{LOGO_DATA_URI}" alt="Target Logo" class="brand-logo">
    </a>
    <span class="cohort-badge">5-6 · UY VAZIFASI</span>
  </div>
  <div class="nav-controls">
    <button class="nav-btn lang-btn" data-lang="uz" onclick="setLang('uz')">UZ</button>
    <button class="nav-btn lang-btn" data-lang="ru" onclick="setLang('ru')">RU</button>
    <button class="nav-btn lang-btn" data-lang="en" onclick="setLang('en')">EN</button>
    <button class="nav-btn" onclick="toggleTheme()" title="Mavzuni almashtirish" data-title-ru="Сменить тему" data-title-en="Toggle Theme">🌓</button>
    <button class="nav-btn primary" onclick="window.print()" data-ru="🖨️ Распечатать (A4)" data-en="🖨️ Print (A4)">🖨️ Chop etish (A4)</button>
  </div>
</header>

<main class="page-container">
  <section class="assignment-hero">
    <div class="hero-eyebrow" data-ru="5–6 КЛАСС · 10-Я НЕДЕЛЯ · УРОК 24" data-en="GRADE 5–6 · WEEK 10 · LESSON 24">5–6-SINF · 10-HAFTA · 24-DARS</div>
    <h1 class="hero-title" data-ru="Scratch 3.0: Спрайты, Сцены и Движение — Домашнее Задание" data-en="Scratch 3.0: Sprites, Stages and Motion — Homework">Scratch 3.0 Sehri: Spraytlar va Koordinatalar — Uy Vazifasi</h1>
    <p class="hero-subtitle" data-ru="Декартова система координат, управление клавиатурой, анимация бега через смену костюмов и защита от вылета за сцену." data-en="Cartesian coordinates, keyboard controls, run animations via costume changes, and stage boundary collision fixes.">Koordinatalar to'ri, klaviatura strelkalari bilan boshqarish, kostyumlarni almashtirish orqali jonli qadam va devordan qaytish qalqoni.</p>
  </section>

  <section class="student-card">
    <div class="card-grid">
      <div class="field-group">
        <label data-ru="Имя и Фамилия ученика" data-en="Student Full Name">O'quvchi F.I.Sh.</label>
        <input type="text" id="studentName" placeholder="Ism va familiyangizni yozing..." data-placeholder-ru="Введите имя и фамилию..." data-placeholder-en="Enter full name..." oninput="saveStudentData()">
      </div>
      <div class="field-group">
        <label data-ru="Класс" data-en="Class">Sinf</label>
        <select id="studentClass" onchange="saveStudentData()">
          <option value="5A">5A</option>
          <option value="5B">5B</option>
          <option value="6A">6A</option>
          <option value="6B">6B</option>
        </select>
      </div>
      <div class="field-group">
        <label data-ru="Дата сдачи" data-en="Submission Date">Topshirish sanasi</label>
        <input type="date" id="studentDate" oninput="saveStudentData()">
      </div>
    </div>
  </section>

  <!-- TASK 1 -->
  <article class="task-card">
    <div class="task-header">
      <div>
        <span class="task-num">Topshiriq 1</span>
        <h2 class="task-title" data-ru="1. Координаты Персонажа в Начале и в Конце Игры" data-en="1. Character Coordinates at Start and End">1. Qahramonning Start va Finish Koordinatalari</h2>
      </div>
      <div class="task-score">2.5 Ball</div>
    </div>
    <p class="task-desc" data-ru="Объясните, почему в самом начале игры при нажатии на зеленый флаг обязательно нужно ставить блок 'go to x: 0 y: 0'? Что произойдет, если игрок закроет игру, а в следующий раз откроет ее без этого блока?" data-en="Explain why 'go to x: 0 y: 0' must be executed when the green flag is clicked. What happens if a player reopens the game without this block?">Nega o'yin boshlanganda (yashil bayroqcha bosilganda) 'go to x: 0 y: 0' blokini qo'yish shart? Agar ushbu blok qo'yilmasa, o'yin qayta boshlanganda qahramon qayerda qoladi?</p>
    <div class="code-box">
when green flag clicked<br>
&nbsp;&nbsp;go to x: 0 y: 0 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;// Markazga qaytarish<br>
&nbsp;&nbsp;point in direction 90 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;// O'ng tomonga qaratish
    </div>
    <textarea class="task-textarea" id="task1_ans" placeholder="Javobingizni shu yerga yozing..." data-placeholder-ru="Напишите ваш ответ здесь..." data-placeholder-en="Write your answer here..." oninput="autoSave()"></textarea>
    <div style="margin-top:10px;">
      <button class="nav-btn" onclick="toggleFix('fix1')" data-ru="💡 Показать решение (Fix)" data-en="💡 Reveal Solution (Fix)">💡 Yechimni ko'rish (Fix)</button>
      <div id="fix1" class="fix-box" style="display:none; margin-top:8px; padding:10px; background:var(--panel-2); border-left:3px solid var(--ok); border-radius:4px;">
        <b style="color:var(--ok);" data-ru="Эталонное решение:" data-en="Reference Solution:">Etalon Yechim:</b>
        <p style="margin:4px 0 0;" data-ru="Scratch персонажа оставляет в той точке, где он остановился в прошлый раз. Без 'go to x: 0 y: 0' персонаж может остаться у края сцены или за препятствием, и новая игра начнется со сломанного состояния!" data-en="Scratch retains the sprite position where it previously stopped. Without 'go to x: 0 y: 0', the sprite might remain stuck at stage edges or traps, starting the new game in a broken state!">Scratch qahramonni o'tgan safar qayerda to'xtagan bo'lsa, o'sha joyda eslab qoladi. Agar 'go to x: 0 y: 0' bo'lmasa, yangi o'yin boshlanganda qahramon devor ichida yoki xato joyda qolib ketadi va o'yin buziladi.</p>
      </div>
    </div>
  </article>

  <!-- TASK 2 -->
  <article class="task-card">
    <div class="task-header">
      <div>
        <span class="task-num">Topshiriq 2</span>
        <h2 class="task-title" data-ru="2. Движение с Помощью 'change x by' vs 'set x to'" data-en="2. Motion: 'change x by' vs 'set x to'">2. 'change x by' va 'set x to' Farqi</h2>
      </div>
      <div class="task-score">2.5 Ball</div>
    </div>
    <p class="task-desc" data-ru="Один ученик для стрелки вправо использовал 'set x to 10', а второй — 'change x by 10'. В чем разница? Почему у первого ученика герой после первого нажатия больше не двигается?" data-en="One student used 'set x to 10' for the right arrow, while another used 'change x by 10'. What's the difference? Why did the first student's hero stop moving after one press?">Bitta o'quvchi o'ng strelkaga 'set x to 10' blokini qo'ydi, ikkinchisi esa 'change x by 10' blokini qo'ydi. Ularning farqi nimada? Nega birinchi o'quvchining qahramoni bitta qadamdan keyin qotib qoladi?</p>
    <textarea class="task-textarea" id="task2_ans" placeholder="Javobingizni tushuntiring..." data-placeholder-ru="Объясните ваш ответ..." data-placeholder-en="Explain your answer..." oninput="autoSave()"></textarea>
    <div style="margin-top:10px;">
      <button class="nav-btn" onclick="toggleFix('fix2')" data-ru="💡 Показать решение (Fix)" data-en="💡 Reveal Solution (Fix)">💡 Yechimni ko'rish (Fix)</button>
      <div id="fix2" class="fix-box" style="display:none; margin-top:8px; padding:10px; background:var(--panel-2); border-left:3px solid var(--ok); border-radius:4px;">
        <b style="color:var(--ok);" data-ru="Эталонное решение:" data-en="Reference Solution:">Etalon Yechim:</b>
        <p style="margin:4px 0 0;" data-ru="'set x to 10' жестко устанавливает координату ровно в 10 пикселей (сколько ни нажимай, он останется на 10). А 'change x by 10' каждый раз прибавляет +10 к текущей позиции (10 -> 20 -> 30...), создавая плавный бег." data-en="'set x to 10' locks the position at 10 pixels strictly. Meanwhile, 'change x by 10' adds +10 to current position every time (10 -> 20 -> 30...), enabling smooth walking.">'set x to 10' qahramonni har qancha bosganda ham aynan 10-pikselda qotirib qo'yadi. 'change x by 10' esa har bosilganda mavjud o'ringa +10 qo'shib boradi (10 -> 20 -> 30...), shu sababli harakat davom etadi.</p>
      </div>
    </div>
  </article>

  <!-- TASK 3 -->
  <article class="task-card">
    <div class="task-header">
      <div>
        <span class="task-num">Topshiriq 3</span>
        <h2 class="task-title" data-ru="3. Бег и Анимация: Роль Блока 'next costume'" data-en="3. Running Animation: 'next costume' Block">3. Qadam Animatsiyasi va 'next costume'</h2>
      </div>
      <div class="task-score">2.5 Ball</div>
    </div>
    <p class="task-desc" data-ru="Когда мы просто меняем координаты, персонаж скользит по полу как статуя. Как с помощью блока 'next costume' оживить его походку? Опишите цепочку блоков." data-en="When we only update coordinates, the sprite glides like a statue. How do we bring its walk to life using 'next costume'? Outline the block sequence.">Faqat koordinatani o'zgartirsak, mushukcha qotib turgan haykaldek sirpanadi. 'next costume' bloki orqali unga qanday qilib jonli qadam tashlash illyuziyasini berish mumkin?</p>
    <textarea class="task-textarea" id="task3_ans" placeholder="Bloklar ketma-ketligini tasvirlang..." data-placeholder-ru="Опишите цепочку блоков..." data-placeholder-en="Describe the block chain..." oninput="autoSave()"></textarea>
    <div style="margin-top:10px;">
      <button class="nav-btn" onclick="toggleFix('fix3')" data-ru="💡 Показать решение (Fix)" data-en="💡 Reveal Solution (Fix)">💡 Yechimni ko'rish (Fix)</button>
      <div id="fix3" class="fix-box" style="display:none; margin-top:8px; padding:10px; background:var(--panel-2); border-left:3px solid var(--ok); border-radius:4px;">
        <b style="color:var(--ok);" data-ru="Эталонное решение:" data-en="Reference Solution:">Etalon Yechim:</b>
        <p style="margin:4px 0 0;" data-ru="Нужно внутрь обработчика клавиши движения добавить блок 'next costume'. При каждом нажатии стрелки персонаж не только сдвинется на 10 пикселей, но и сменит кадр ноги (Costume 1 -> Costume 2), создавая живую анимацию шага!" data-en="Insert 'next costume' inside the arrow key handler. With every press, the sprite not only shifts 10 pixels but also toggles its leg frame (Costume 1 -> Costume 2), producing a lifelike walking animation!">Harakat hodisasi ichiga 'next costume' blokini qo'shish kerak. Har safar strelka bosilganda qahramon 10 piksel oldinga siljiydi va kostyumi o'zgaradi, natijada qadam tashlash animatsiyasi hosil bo'ladi.</p>
      </div>
    </div>
  </article>

  <!-- TASK 4 -->
  <article class="task-card">
    <div class="task-header">
      <div>
        <span class="task-num">Topshiriq 4</span>
        <h2 class="task-title" data-ru="4. Исправление Бага: Перевернутый Герой при Отскоке" data-en="4. Bug Fix: Upside-Down Rebounding Sprite">4. Kiber-Xatoni Tuzatish: Teskari Ag'darilgan Mushukcha</h2>
      </div>
      <div class="task-score">2.5 Ball</div>
    </div>
    <p class="task-desc" data-ru="Ученик добавил 'if on edge, bounce', но когда герой ударяется о правую стену, он переворачивается ногами кверху и бежит вверх ногами. Какой блок и с каким параметром решает эту проблему?" data-en="A student added 'if on edge, bounce', but upon hitting the right wall, the sprite flips upside-down. Which block and setting fixes this bug?">O'quvchi 'if on edge, bounce' blokini qo'ydi, lekin mushukcha o'ng devorga tekkanda teskari (boshi pastga qarab) ag'darilib qoldi. Ushbu xatoni qaysi maxsus blok tuzatadi?</p>
    <textarea class="task-textarea" id="task4_ans" placeholder="Qaysi blok va qanday sozlama kerakligini yozing..." data-placeholder-ru="Напишите нужный блок и настройку..." data-placeholder-en="Write required block and setting..." oninput="autoSave()"></textarea>
    <div style="margin-top:10px;">
      <button class="nav-btn" onclick="toggleFix('fix4')" data-ru="💡 Показать решение (Fix)" data-en="💡 Reveal Solution (Fix)">💡 Yechimni ko'rish (Fix)</button>
      <div id="fix4" class="fix-box" style="display:none; margin-top:8px; padding:10px; background:var(--panel-2); border-left:3px solid var(--ok); border-radius:4px;">
        <b style="color:var(--ok);" data-ru="Эталонное решение:" data-en="Reference Solution:">Etalon Yechim:</b>
        <p style="margin:4px 0 0;" data-ru="Проблема решается синим блоком 'set rotation style [left-right]'. По умолчанию Scratch вращает спрайт на 360 градусов. Режим 'left-right' запрещает переворот вверх ногами и позволяет смотреть только влево или вправо." data-en="Resolved by the blue block 'set rotation style [left-right]'. Scratch defaults to 360-degree all-around rotation. 'left-right' mode forbids upside-down flipping and only mirrors horizontally.">Bu xatoni 'set rotation style [left-right]' (aylanish uslubini [chap-o'ng] ga o'rnatish) bloki tuzatadi. U qahramonning boshiga ag'darilishini taqiqlab, faqat chapga va o'ngga qarashiga ruxsat beradi.</p>
      </div>
    </div>
  </article>

  <!-- RUBRIC -->
  <section class="rubric-section" style="margin-top:20px; background:var(--panel); border:1px solid var(--rule); border-radius:12px; padding:18px;">
    <h3 style="margin:0 0 12px; font-family:'Manrope',sans-serif;" data-ru="Критерии Оценки за Домашнюю Работу (10 Баллов)" data-en="Homework Evaluation Rubric (10 Points)">Uy Vazifasi Baholash Mezonlari (10 Ball)</h3>
    <div style="display:grid; grid-template-columns:repeat(4, 1fr); gap:10px;">
      <div class="card" style="padding:10px; text-align:center; background:var(--panel-2); border-radius:8px;">
        <b style="color:var(--accent);">2.5 Ball</b>
        <p style="font-size:12px; margin:4px 0 0;" data-ru="1-Задание: Понимание сброса позиции" data-en="Task 1: Reset position logic">1-Topshiriq: Start pozitsiyasi tushuntirilgan</p>
      </div>
      <div class="card" style="padding:10px; text-align:center; background:var(--panel-2); border-radius:8px;">
        <b style="color:var(--accent);">2.5 Ball</b>
        <p style="font-size:12px; margin:4px 0 0;" data-ru="2-Задание: Разница set vs change" data-en="Task 2: Difference of set vs change">2-Topshiriq: set va change farqi asoslangan</p>
      </div>
      <div class="card" style="padding:10px; text-align:center; background:var(--panel-2); border-radius:8px;">
        <b style="color:var(--accent);">2.5 Ball</b>
        <p style="font-size:12px; margin:4px 0 0;" data-ru="3-Задание: Логика смены костюмов" data-en="Task 3: Costume cycling logic">3-Topshiriq: Kostyumlar almashishi ko'rsatilgan</p>
      </div>
      <div class="card" style="padding:10px; text-align:center; background:var(--panel-2); border-radius:8px;">
        <b style="color:var(--accent);">2.5 Ball</b>
        <p style="font-size:12px; margin:4px 0 0;" data-ru="4-Задание: Блок rotation style" data-en="Task 4: Rotation style block fix">4-Topshiriq: rotation style bloki to'g'ri topilgan</p>
      </div>
    </div>
  </section>
</main>

<script>
function autoSave() {{
  ['task1_ans', 'task2_ans', 'task3_ans', 'task4_ans'].forEach(function(id) {{
    var val = document.getElementById(id).value;
    localStorage.setItem("vc_hw_24_" + id, val);
  }});
}}

function saveStudentData() {{
  localStorage.setItem("vc_student_name", document.getElementById("studentName").value);
  localStorage.setItem("vc_student_class", document.getElementById("studentClass").value);
  localStorage.setItem("vc_student_date", document.getElementById("studentDate").value);
}}

function loadStudentData() {{
  if (localStorage.getItem("vc_student_name")) document.getElementById("studentName").value = localStorage.getItem("vc_student_name");
  if (localStorage.getItem("vc_student_class")) document.getElementById("studentClass").value = localStorage.getItem("vc_student_class");
  if (localStorage.getItem("vc_student_date")) document.getElementById("studentDate").value = localStorage.getItem("vc_student_date");
  ['task1_ans', 'task2_ans', 'task3_ans', 'task4_ans'].forEach(function(id) {{
    var saved = localStorage.getItem("vc_hw_24_" + id);
    if (saved) document.getElementById(id).value = saved;
  }});
}}

function toggleFix(id) {{
  var el = document.getElementById(id);
  el.style.display = (el.style.display === "block") ? "none" : "block";
}}

function setLang(lang) {{
  document.querySelectorAll(".lang-btn").forEach(function(b) {{
    b.classList.toggle("active", b.getAttribute("data-lang") === lang);
  }});
  document.querySelectorAll("[data-ru], [data-en]").forEach(function(el) {{
    if (!el.getAttribute("data-uz-orig")) el.setAttribute("data-uz-orig", el.innerHTML);
    if (lang === "uz") el.innerHTML = el.getAttribute("data-uz-orig");
    else if (lang === "ru" && el.getAttribute("data-ru")) el.innerHTML = el.getAttribute("data-ru");
    else if (lang === "en" && el.getAttribute("data-en")) el.innerHTML = el.getAttribute("data-en");
  }});
}}

function toggleTheme() {{
  var cur = document.documentElement.getAttribute("data-theme") || "dark";
  var next = cur === "dark" ? "light" : "dark";
  document.documentElement.setAttribute("data-theme", next);
}}

window.addEventListener("DOMContentLoaded", function() {{
  loadStudentData();
}});
</script>
</body>
</html>
"""

with open(os.path.join(FOLDER, "vazifa.html"), "w", encoding="utf-8") as f:
    f.write(full_vazifa)

print("✅ Vazifa generated for 5-6-sinf 24-dars")

# -------------------------------------------------------------
# 4. TEACHER_READING.md (Teacher's Guide)
# -------------------------------------------------------------
teacher_guide = """# 24-Dars: O'qituvchi Uchun Metodik Qo'llanma va Yechimlar Kaliti
**Target International School // 5–6-Sinf // 10-Hafta (2-Chorak 1-Darsi: 40 daqiqa)**
**Mavzu:** Scratch 3.0 Sehri: Spraytlar, Sahnalar va Birinchi Qadamlar
**Kohorta:** `5-6-sinf` (Junior Creators & Scratch Coding)

---

## 1. Asosiy Pedagogik Maqsad
Bugungi dars bilan o'quvchilar **2-Chorak: Agentik Dasturlash va Avtonom Tizimlar** blokiga qadam qo'yadilar.
1. **Koordinata Tizimi:** Scratch-ning $X$ (-240 dan +240 gacha) va $Y$ (-180 dan +180 gacha) koordinatalar to'rini tushunish.
2. **Hodisalar (Events):** Dastur startini yashil bayroqcha va klaviatura strelkalari bilan bog'lash.
3. **Jonli Animatsiya:** Kostyumlarni ketma-ket almashtirish (`next costume`) orqali yugurish harakatini hosil qilish.
4. **Chegara Qalqoni:** `if on edge, bounce` va `set rotation style [left-right]` orqali personajning ekrandan chiqib ketishi yoki ag'darilib qolishining oldini olish.

---

## 2. 40 Daqiqalik Dars Reglamenti

| Vaqt | Bosqich | O'qituvchi Harakati | O'quvchilar Harakati |
|---|---|---|---|
| **00:00 – 03:00** | Kirish & Yangi Chorak | 2-Chorak maqsadlari va Scratch muhitini tanishtirish. | Noutbuklarni ochish, Scratch-ga kirish. |
| **03:00 – 08:00** | Aqliy Hujum (Koordinatalar) | Doskada (0, 0), musbat va manfiy sonlar to'rini ko'rsatish. | Savollarga javob berish, yo'nalishlarni ko'rsatish. |
| **08:00 – 18:00** | Nazariya va Bloklar Tahlili | 12 slaydli prezentatsiyani namoyish etish, hodisalar va harakat bloklarini tushuntirish. | Bloklarning vazifasini tushunish. |
| **18:00 – 23:00** | Jonli Viktorina (Quiz & Fix) | Slayd 9 dagi testni sinf bilan birga yechish. | Variantlarni tanlash, xatolarni tahlil qilish. |
| **23:00 – 36:00** | Amaliy Kiber-Missiya | O'quvchilar o'z kompyuterlarida kiber-arenani quradilar va strelkalarni ulaydilar. | Scratch-da bloklarni terish, mustaqil sinash. |
| **36:00 – 40:00** | Xulosa & Uy Vazifasi | 10 ballik mezon asosida eng yaxshi loyihalarni ko'rsatish, `vazifa.html` ni tushuntirish. | O'z ishini saqlab olish, vazifani belgilash. |

---

## 3. Viktorina va Topshiriqlar Yechimi (Teacher Fixes)

### Viktorina (Slayd 9):
* **Savol:** Qaysi koordinata qahramonni yuqori o'ng burchakka eltadi?
* **To'g'ri javob:** **C) go to x: 200 y: 150**
* **Izoh:** O'ng tomon — musbat X (+200), yuqori tomon — musbat Y (+150).

### Uy Vazifasi Yechimlari:
1. **Start pozitsiyasi:** `go to x: 0 y: 0` bo'lmasa, qahramon avvalgi o'yin to'xtagan joyda qolib ketadi va yangi o'yin boshlanishi buziladi.
2. **set vs change:** `set x to 10` qiymatni qotirib qo'yadi. `change x by 10` esa har bosganda +10 qo'shib, uzluksiz harakat beradi.
3. **next costume:** Strelka bosilganda har safar kadr almashadi va oyog'ini harakatlantirayotgan haqiqiy yugurish tasviri hosil bo'ladi.
4. **rotation style:** `set rotation style [left-right]` bloki mushukchaning devorga tekkanda teskari o'girilib ketishini to'xtatadi.

---

## 4. Baholash Mezoni (10 Ball)
* **3 Ball:** Yashil bayroqcha bosilganda markazga (0,0) qaytish sozlangan.
* **3 Ball:** 4 ta strelka (o'ng, chap, yuqori, quyi) xatosiz harakatlantiradi.
* **2 Ball:** Harakat paytida `next costume` orqali qadam animatsiyasi ishlaydi.
* **2 Ball:** Devordan qaytish qalqoni o'rnatilgan va orqa fon tanlangan.
"""

with open(os.path.join(FOLDER, "TEACHER_READING.md"), "w", encoding="utf-8") as f:
    f.write(teacher_guide)

print("✅ TEACHER_READING.md generated for 5-6-sinf 24-dars")

# -------------------------------------------------------------
# 5. PLAYGROUND (Interactive Mini Scratch Coordinates Lab)
# -------------------------------------------------------------
playground_html = """<!DOCTYPE html>
<html lang="uz" data-theme="dark">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Scratch 3.0 Koordinatalar Maydoni — Interaktiv Laboratoriya</title>
<link rel="icon" type="image/svg+xml" href="/assets/favicon.svg">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Manrope:wght@700;800&family=JetBrains+Mono:wght@500;700&display=swap">
<style>
:root {
  --bg: #061530; --panel: #0E2249; --panel-2: #16305A;
  --ink: #E9EFF8; --accent: #FF1100; --ok: #00D68F; --rule: #22406B;
}
body {
  margin: 0; padding: 20px; background: var(--bg); color: var(--ink);
  font-family: 'Manrope', sans-serif; display: flex; flex-direction: column; align-items: center;
}
.header { text-align: center; margin-bottom: 16px; }
.header h1 { margin: 0 0 6px; font-size: 22px; }
.header p { margin: 0; color: #8496B0; font-size: 14px; }
.lab-container {
  display: flex; gap: 20px; background: var(--panel); border: 1px solid var(--rule);
  border-radius: 16px; padding: 20px; box-shadow: 0 10px 30px rgba(0,0,0,0.4);
}
canvas {
  background: #0A1D3D; border: 2px solid var(--rule); border-radius: 8px; cursor: crosshair;
}
.controls { width: 280px; display: flex; flex-direction: column; gap: 14px; }
.metric-box {
  background: var(--panel-2); border-radius: 8px; padding: 12px;
  font-family: 'JetBrains Mono', monospace; text-align: center;
}
.metric-val { font-size: 24px; font-weight: 700; color: var(--ok); }
.code-display {
  background: #031024; border-radius: 8px; padding: 12px; font-family: 'JetBrains Mono', monospace;
  font-size: 13px; color: #FFD166; border-left: 3px solid var(--accent);
}
.btn-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 8px; }
button {
  background: var(--panel-2); border: 1px solid var(--rule); color: var(--ink);
  padding: 8px 12px; border-radius: 6px; font-family: 'Manrope', sans-serif;
  font-size: 12px; font-weight: 700; cursor: pointer; transition: 0.2s;
}
button:hover { background: var(--accent); color: #fff; border-color: var(--accent); }
.arrows-dpad {
  display: grid; grid-template-columns: repeat(3, 1fr); gap: 6px; width: 140px; margin: 0 auto;
}
</style>
</head>
<body>

<div class="header">
  <h1>Scratch 3.0: Koordinatalar va Harakat Simulyatori</h1>
  <p>Sahna o'lchami: 480 x 360 | Strelkalar yoki sichqoncha bilan boshqaring!</p>
</div>

<div class="lab-container">
  <canvas id="stage" width="480" height="360"></canvas>
  <div class="controls">
    <div class="metric-box">
      <div>KOORDINATALAR</div>
      <div class="metric-val" id="coords">X: 0, Y: 0</div>
    </div>
    <div class="code-display" id="scratchCode">
      when green flag clicked<br>
      go to x: 0 y: 0
    </div>
    <div class="btn-grid">
      <button onclick="setPos(0, 0)">Markaz (0, 0)</button>
      <button onclick="setPos(200, 140)">Yuqori O'ng</button>
      <button onclick="setPos(-200, 140)">Yuqori Chap</button>
      <button onclick="setPos(-200, -140)">Quyi Chap</button>
    </div>
    <div style="text-align:center; font-size:12px; color:#8496B0;">Klaviatura strelkalari:</div>
    <div class="arrows-dpad">
      <div></div><button onclick="move(0, 15)">▲</button><div></div>
      <button onclick="move(-15, 0)">◄</button><button onclick="setPos(0,0)">●</button><button onclick="move(15, 0)">►</button>
      <div></div><button onclick="move(0, -15)">▼</button><div></div>
    </div>
  </div>
</div>

<script>
var canvas = document.getElementById("stage");
var ctx = canvas.getContext("2d");
var posX = 0;
var posY = 0;

function drawGrid() {
  ctx.clearRect(0, 0, 480, 360);
  ctx.strokeStyle = "#16305A";
  ctx.lineWidth = 1;

  for (var x = 0; x <= 480; x += 40) {
    ctx.beginPath(); ctx.moveTo(x, 0); ctx.lineTo(x, 360); ctx.stroke();
  }
  for (var y = 0; y <= 360; y += 40) {
    ctx.beginPath(); ctx.moveTo(0, y); ctx.lineTo(480, y); ctx.stroke();
  }

  // Axes
  ctx.strokeStyle = "#FF1100"; ctx.lineWidth = 2;
  ctx.beginPath(); ctx.moveTo(0, 180); ctx.lineTo(480, 180); ctx.stroke(); // X o'qi

  ctx.strokeStyle = "#0066FF"; ctx.lineWidth = 2;
  ctx.beginPath(); ctx.moveTo(240, 0); ctx.lineTo(240, 360); ctx.stroke(); // Y o'qi

  // Center dot
  ctx.fillStyle = "#FFD166";
  ctx.beginPath(); ctx.arc(240, 180, 4, 0, Math.PI * 2); ctx.fill();

  // Character (Cat icon)
  var cx = 240 + posX;
  var cy = 180 - posY;

  ctx.fillStyle = "#FFB703";
  ctx.beginPath(); ctx.arc(cx, cy, 18, 0, Math.PI * 2); ctx.fill();
  ctx.fillStyle = "#000";
  ctx.beginPath(); ctx.arc(cx - 6, cy - 4, 3, 0, Math.PI * 2); ctx.fill();
  ctx.beginPath(); ctx.arc(cx + 6, cy - 4, 3, 0, Math.PI * 2); ctx.fill();
  ctx.fillStyle = "#FF1100";
  ctx.beginPath(); ctx.arc(cx, cy + 4, 3, 0, Math.PI * 2); ctx.fill();

  document.getElementById("coords").textContent = "X: " + posX + ", Y: " + posY;
  document.getElementById("scratchCode").innerHTML = "when green flag clicked<br>go to x: " + posX + " y: " + posY;
}

function setPos(x, y) {
  posX = Math.max(-230, Math.min(230, x));
  posY = Math.max(-170, Math.min(170, y));
  drawGrid();
}

function move(dx, dy) {
  setPos(posX + dx, posY + dy);
}

canvas.addEventListener("click", function(e) {
  var rect = canvas.getBoundingClientRect();
  var mouseX = e.clientX - rect.left;
  var mouseY = e.clientY - rect.top;
  setPos(Math.round(mouseX - 240), Math.round(180 - mouseY));
});

window.addEventListener("keydown", function(e) {
  if (e.key === "ArrowUp") { e.preventDefault(); move(0, 15); }
  else if (e.key === "ArrowDown") { e.preventDefault(); move(0, -15); }
  else if (e.key === "ArrowLeft") { e.preventDefault(); move(-15, 0); }
  else if (e.key === "ArrowRight") { e.preventDefault(); move(15, 0); }
});

drawGrid();
</script>
</body>
</html>
"""

with open(os.path.join(FOLDER, "playground", "index.html"), "w", encoding="utf-8") as f:
    f.write(playground_html)

print("✅ Playground generated for 5-6-sinf 24-dars")
