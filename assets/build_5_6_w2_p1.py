#!/usr/bin/env python3
import os, sys
sys.path.insert(0, '/home/dpdp/target/assets')
from curriculum_generator import build_presentation, build_worksheet

BASE = '/home/dpdp/target/classes/5-6-sinf/2-hafta'

# =========================================================================
# LESSON 7: 3D MODELLAR VA OBYEKTLAR
# =========================================================================
l7_dir = os.path.join(BASE, '07-dars-3d-modellar-va-obyektlar')
os.makedirs(l7_dir, exist_ok=True)

l7_slides = """
<section class="slide is-on" data-phase="Kirish|Вступление|Opening" data-time="0–3">
  <div class="title-wrap">
    <div class="eyebrow">Vibecoding · <span data-ru="урок 7 · 5-6 классы" data-en="lesson 7 · grades 5-6">7-dars · 5-6 sinflar</span></div>
    <div class="title-meta">
      <span><b lang="uz">Fan:</b><span data-ru=" IT / Vibecoding" data-en=" IT / Vibecoding"> IT / Vibecoding</span><b lang="ru">Предмет:</b><span lang="ru"> IT / Vibecoding</span><b lang="en">Subject:</b><span lang="en"> IT / Vibecoding</span></span>
      <span><b lang="uz">Hafta:</b><span data-ru=" 2" data-en=" 2"> 2</span><b lang="ru">Неделя:</b><span lang="ru"> 2</span><b lang="en">Week:</b><span lang="en"> 2</span></span>
    </div>
    <h1 data-ru="Мир 3D-Моделей: Генерация Игровых Объектов с ИИ" data-en="The World of 3D Models: Generating Game Objects with AI">3D Modellar Dunyosi: AI Bilan O'yin Obyektlarini Yaratish</h1>
    <p class="lede" data-ru="Как плоский арт превращается в объемную фигуру для Roblox и Minecraft? Изучаем 3D-сетки, текстуры, полигоны и нейросети генерации 3D." data-en="How does a 2D concept become a tangible 3D asset for Roblox and Minecraft? Exploring meshes, textures, polygons, and text-to-3D engines.">Qanday qilib 2D chizma Roblox va Minecraft uchun haqiqiy hajmli 3D modelga aylanadi? 3D to'rlar, poligonlar, teksturalar va AI 3D generatorlarini o'rganamiz.</p>
  </div>
</section>

<section class="slide" data-phase="Tushuncha|2D против 3D|2D vs 3D" data-time="3–7">
  <div class="eyebrow"><span data-ru="Пространство игры" data-en="Dimensional Geometry">Geometriya Asoslari</span></div>
  <h2 data-ru="В чем разница: Плоский спрайт против 3D-модели" data-en="The Core Distinction: Flat Sprites vs 3D Meshes">2D va 3D Farqi: Yassi Rasm vs Hajmli Model</h2>
  <p data-ru="Современные игры строятся в трехмерном пространстве. Чем 3D-модель превосходит обычную картинку?" data-en="Modern gaming environments operate in 3-dimensional coordinate space. What makes 3D models superior to flat bitmaps?">Zamonaviy o'yinlar 3 o'lchamli fazoda yashaydi. 3D model oddiy yassi rasmdan nima bilan farq qiladi?</p>
  <div class="cols c2" style="margin-top:15px;">
    <div class="box">
      <h3 style="color:var(--ink-2);" data-ru="2D Спрайт (Пиксели) 🖼️" data-en="2D Sprite (Pixels) 🖼️">2D Rasm / Sprayt (Piksel) 🖼️</h3>
      <p data-ru="Имеет только ширину (X) и высоту (Y). Нельзя повернуть, обойти сзади или осветить сбоку. Чтобы показать поворот, нужно рисовать заново." data-en="Bounded strictly to X (width) and Y (height). Cannot be rotated, orbited, or relit dynamically without redrawing each frame.">Faqat Eni (X) va Bo'yi (Y) bor. Uni aylantirib, orqa tomonidan ko'rib bo'lmaydi. Har bir burchak uchun yangi rasm chizish kerak.</p>
    </div>
    <div class="box" style="border-left:4px solid var(--accent);">
      <h3 style="color:var(--accent);" data-ru="3D Модель (Полигоны) 🧊" data-en="3D Model (Polygons) 🧊">3D Model (To'r / Mesh) 🧊</h3>
      <p data-ru="Имеет X, Y и глубину Z! Игрок может вращать модель на 360°, менять масштаб и физически взаимодействовать в игровом движке." data-en="Operates across X, Y, and Z (depth) axes! Gamers can orbit 360°, cast realistic shadows, and scale within physics engines.">X, Y va Chuqurlik (Z) o'qiga ega! O'yinchi modelni 360° aylantirishi, ustiga chiqishi va o'yin ichida erkin boshqarishi mumkin.</p>
    </div>
  </div>
</section>

<section class="slide" data-phase="Arxitektura|Анатомия 3D|3D Anatomy" data-time="7–11">
  <div class="eyebrow"><span data-ru="Строение объекта" data-en="Asset Anatomy">3D Model Anatomiyasi</span></div>
  <h2 data-ru="Из чего состоит 3D-модель: Точки, Полигоны и Сетка" data-en="Anatomy of a 3D Asset: Vertices, Polygons & Meshes">3D Model Ichida Nima Bor? Nuqtalar, Qirralar va Poligonlar</h2>
  <p data-ru="Любой персонаж в игре — это цифровая скульптура из тысяч плоских треугольников:" data-en="Every character and asset in a game is a digital sculpture composed of thousands of geometric polygons:">Har qanday qahramon yoki qurol kompyuter xotirasida uchburchak shakllardan yig'ilgan to'rdir:</p>
  <div class="grid" style="display:grid; grid-template-columns:1fr 1fr; gap:12px; margin-top:10px;">
    <div class="box">
      <h3 style="color:var(--accent);" data-ru="1. Вершины (Vertices) 📍" data-en="1. Vertices (Points) 📍">1. Cho'qqilar (Vertices / Nuqtalar) 📍</h3>
      <p data-ru="Координаты X, Y, Z в пространстве. Это опорные точки, на которых держится вся форма." data-en="3D coordinates in virtual space. Anchoring points that determine geometric form.">3D fazodagi nuqtalar. Butun shakl ushbu nuqtalar ustiga quriladi.</p>
    </div>
    <div class="box">
      <h3 style="color:var(--accent);" data-ru="2. Полигоны (Faces) 📐" data-en="2. Polygons (Faces) 📐">2. Poligonlar (Yuzalar / Faces) 📐</h3>
      <p data-ru="Плоские треугольники, соединяющие точки. Чем больше полигонов, тем более гладкая модель." data-en="Flat triangular or quad facets connecting vertices. Higher counts produce smoother silhouettes.">Nuqtalarni birlashtiruvchi tekis yuzalar. Poligonlar qancha ko'p bo'lsa, model shuncha silliq bo'ladi.</p>
    </div>
    <div class="box">
      <h3 style="color:var(--accent);" data-ru="3. Текстура (Texture / UV) 🎨" data-en="3. Textures (UV Skin) 🎨">3. Tekstura va Rang (Texture Map) 🎨</h3>
      <p data-ru="Цветная 'кожа', натянутая на модель. Задает металл, дерево, свечение или ткань." data-en="A 2D painted wrapper mapped over the 3D mesh, assigning materials like metal, neon, or wood.">To'r ustiga yopilgan rangli 'teri'. U temir, yog'och, neon nur yoki matoni aks ettiradi.</p>
    </div>
    <div class="box">
      <h3 style="color:var(--accent);" data-ru="4. Формат файла (.GLB / .OBJ) 💾" data-en="4. File Formats (.GLB / .OBJ) 💾">4. O'yin Fayli (.GLB / .OBJ) 💾</h3>
      <p data-ru="Стандартные форматы 3D-файлов, которые понимает Roblox Studio, Unity и веб-браузер." data-en="Standard 3D file formats compatible with Roblox Studio, Unity, Blender, and web engines.">Roblox Studio, Minecraft va barcha 3D o'yin dvijoklari taniydigan umumiy 3D fayl formati.</p>
    </div>
  </div>
</section>

<section class="slide" data-phase="Mexanizm|Text-to-3D|Generative 3D" data-time="11–15">
  <div class="eyebrow"><span data-ru="Нейросети нового поколения" data-en="Next-Gen AI">AI 3D Qanday Ishlaydi?</span></div>
  <h2 data-ru="Как ИИ создает 3D: От Текста к Объемной Сетке" data-en="How AI Generates 3D: From Prompt to Spatial Geometry">AI Qanday Qilib Matndan 3D Model Yasaydi?</h2>
  <p data-ru="Раньше 3D-художник тратил неделю на один меч. Нейросеть (Meshy, Tripo3D) делает это за 60 секунд:" data-en="Previously, 3D artists spent weeks sculpting a single blade. Generative AI (Meshy, Tripo3D) accomplishes this in 60 seconds:">Ilgari 3D rassom bitta qurolni yasashga 1 hafta sarflardi. Zamonaviy AI buni 60 soniyada bajaradi:</p>
  <ul class="rules">
    <li><span class="t" data-ru="<b>1. Текстовый промпт:</b> Описываем форму, материал и назначение объекта (например: кибер-щит из темного титана)." data-en="<b>1. Text Prompt:</b> Describe shape, material, and function (e.g., cyber shield forged from dark titanium)."><b>1. Prompt yozish:</b> Shakl, material va obyekt vazifasini aniq bayon qilamiz (masalan: qora titandan yasalgan kiber-qalqon).</span></li>
    <li><span class="t" data-ru="<b>2. Генерация объема (NeRF / Diffusion):</b> ИИ просчитывает объект со всех 360 градусов и строит облако точек." data-en="<b>2. Volumetric Inference:</b> AI computes 360° projections and constructs a spatial point cloud."><b>2. Fazoviy hisoblash:</b> AI modelni har tomondan 360 gradusda tasavvur qilib, fazoviy nuqtalar bulutini yaratadi.</span></li>
    <li><span class="t" data-ru="<b>3. Запекание сетки (Mesh Baking):</b> Точки соединяются в полигоны и накладывается текстура." data-en="<b>3. Mesh Baking:</b> Points interconnect into polygonal faces and surface textures are baked in."><b>3. To'rni qotirish (Mesh Baking):</b> Nuqtalar poligonlarga aylanadi va ustiga yaltiroq tekstura yopiladi.</span></li>
    <li><span class="t" data-ru="<b>4. Экспорт в .GLB:</b> Готовый файл скачивается и загружается в игру одним кликом!" data-en="<b>4. GLB Export:</b> Production-ready file downloaded and dragged directly into the game engine!"><b>4. .GLB faylni yuklab olish:</b> Tayyor 3D faylni yuklab olib, o'yinga to'g'ridan-to'g'ri joylaymiz!</span></li>
  </ul>
</section>

<section class="slide" data-phase="Ko'rsatma|Формула 3D|Prompt Formula" data-time="15–19">
  <div class="eyebrow"><span data-ru="Инженерный подход" data-en="Engineering Formula">3D Prompt Formulasi</span></div>
  <h2 data-ru="Формула Идеального 3D-Промпта (4 Элемента)" data-en="The 4-Element Formula for Clean 3D Assets">Mukammal 3D Promptning 4 Qismli Formulasi</h2>
  <div class="box" style="background:var(--panel); border-left:5px solid var(--green); padding:16px;">
    <p style="font-family:monospace; font-size:0.95em; line-height:1.6;" data-ru="<b>[ОБЪЕКТ]</b> Кибернетический летающий дрон-разведчик<br>+ <b>[СТИЛЬ]</b> Low-poly 3D game asset, Roblox / Minecraft совместимый<br>+ <b>[МАТЕРИАЛ]</b> Матовый титан, неоновые бирюзовые линзы, медные кабели<br>+ <b>[ФОРМА]</b> Симметричный, цельный меш, без лишнего мусора, isolated" data-en="<b>[SUBJECT]</b> Cybernetic hovering recon drone<br>+ <b>[STYLE]</b> Low-poly 3D game asset, Roblox / Minecraft compatible<br>+ <b>[SURFACE]</b> Matte titanium, neon cyan optics, exposed copper conduit<br>+ <b>[TOPOLOGY]</b> Symmetrical, single closed mesh, zero floating debris, isolated">
      <b>1. OBYEKT:</b> Kiber-razvedkachi uchuvchi dron-robot<br>
      + <b>2. O'YIN USLUBI:</b> Low-poly 3D game asset, Roblox / Minecraft ga mos<br>
      + <b>3. MATERIAL VA RANG:</b> Qora mat titan, neon havorang linzalar, mis simlar<br>
      + <b>4. TO'R SIFATI:</b> Simmetrik, butun to'r (single closed mesh), yotqizilgan tekis zamin, isolated
    </p>
  </div>
  <p style="margin-top:12px; font-size:0.9em; color:var(--ink-2);" data-ru="Совет: Слова 'single mesh' и 'game ready' заставляют ИИ делать монолитную модель без дырок." data-en="Pro-Tip: Specifying 'single mesh' and 'game ready' forces the engine to generate clean watertight geometry.">Tavsiya: 'single mesh' va 'game ready' so'zlari AI ga modelni teshik va bo'shliqlarsiz, mustahkam bitta to'r qilib yasashni buyuradi.</p>
</section>

<section class="slide" data-phase="Sinov|Ошибки геометрии|Geometry Traps" data-time="19–23">
  <div class="eyebrow"><span data-ru="Аудит моделей" data-en="Quality Control">3D Xatolarini Nazorat Qilish</span></div>
  <h2 data-ru="3 Опасные Ловушки 3D-Генерации в Играх" data-en="3 Fatal Flaws in AI-Generated 3D Models">AI Yaratgan 3D Modelda Qanday Xatolar Bo'lishi Mumkin?</h2>
  <p data-ru="Не каждая сгенерированная модель годится для игры. Вот на что смотрим в первую очередь:" data-en="Not every generated asset is engine-ready. Watch out for these three structural traps:">Har qanday generatsiya qilingan modelni o'yinga qo'yib bo'lmaydi. Quyidagi 3 ta xatoga diqqat qiling:</p>
  <div class="cols c3" style="display:grid; grid-template-columns:1fr 1fr 1fr; gap:12px; margin-top:12px;">
    <div class="box" style="border-top:4px solid var(--accent);">
      <h3 style="color:var(--accent);" data-ru="1. Невидимые дыры (Holes) 🕳️" data-en="1. Missing Normals / Holes 🕳️">1. Teshik To'rlar (Holes) 🕳️</h3>
      <p data-ru="Если полигон вывернут, сквозь модель видна пустота. Игрок будет проваливаться сквозь такой объект." data-en="Inverted polygons cause see-through glitches. Characters fall through fractured geometry.">Agar poligon teskari qarasa, model ichi ko'rinib qoladi. Qahramon bu to'siqdan o'tib ketadi.</p>
    </div>
    <div class="box" style="border-top:4px solid var(--accent);">
      <h3 style="color:var(--accent);" data-ru="2. Лишние полигоны (Lag) ⚡" data-en="2. Polygon Overload (Lag) ⚡">2. Haddan Tashqari Ko'p Poligon ⚡</h3>
      <p data-ru="Миллион полигонов на один ящик убьет FPS в игре. Модель для мобилок должна быть легкой (Low-Poly)." data-en="A million triangles on a single crate crashes mobile frame rates. Prioritize optimized Low-Poly.">Bitta qutida millionta poligon bo'lsa, o'yin qotadi (lag). O'yinlar uchun yengil Low-Poly kerak.</p>
    </div>
    <div class="box" style="border-top:4px solid var(--green);">
      <h3 style="color:var(--green);" data-ru="3. Летающие куски (Debris) 🎈" data-en="3. Floating Debris 🎈">3. Havodagi Bo'laklar (Debris) 🎈</h3>
      <p data-ru="Нейросеть иногда оставляет висящие в воздухе пиксели. Их нужно удалять в просмотрщике 3D." data-en="AI sometimes leaves disconnected floating artifacts. Inspect and clean before exporting.">AI ba'zan havoda osilib turgan mayda nuqtalarni qoldiradi. Ularni tozalash lozim.</p>
    </div>
  </div>
</section>

<section class="slide" data-phase="Vazifa|Миссия урока|Lab Brief" data-time="23–27">
  <div class="eyebrow"><span data-ru="Практическая миссия" data-en="Hands-on Mission">Amaliy Vazifa</span></div>
  <h2 data-ru="Миссия: Спроектировать и Сгенерировать 3D-Артефакт" data-en="Mission: Architect & Generate a Production 3D Asset">Bugungi Vazifa: O'z O'yiningiz Uchun 3D Artefakt Yarating</h2>
  <p data-ru="Сегодня каждый создает один ключевой 3D-объект для своей будущей игры (оружие, транспорт или реликвию):" data-en="Today, each developer constructs one flagship 3D asset for their upcoming game world:">Bugun har bir o'quvchi o'z o'yini uchun bitta asosiy 3D modelni yaratadi va pasportini to'ldiradi:</p>
  <ul class="rules">
    <li><span class="t" data-ru="<b>1. Выбор объекта:</b> Легендарный меч, кибернетический джетпак, сундук с кристаллами или космокатер." data-en="<b>1. Asset Choice:</b> Legendary energy blade, cybernetic jetpack, quantum loot chest, or speeder."><b>1. Obyektni tanlash:</b> Afsonaviy energiya qilichi, kiber-jetpak, kvant sandig'i yoki uchar transport.</span></li>
    <li><span class="t" data-ru="<b>2. Промпт по формуле:</b> Написать точный промпт с указанием стиля Low-poly и материалов." data-en="<b>2. Prompt Engineering:</b> Draft a 4-part formula specifying Low-poly geometry and surface shaders."><b>2. Formulali prompt:</b> Low-poly uslubi va materiallar ko'rsatilgan professional prompt yozish.</span></li>
    <li><span class="t" data-ru="<b>3. Генерация и 3D-осмотр:</b> Запустить генератор (Meshy / Tripo3D), покрутить модель со всех сторон." data-en="<b>3. Generation & 360 Inspection:</b> Run generation (Meshy / Tripo3D) and orbit the asset 360°."><b>3. Generatsiya va 360° ko'rish:</b> 3D vositada modelni har tomondan tekshirish, nuqsonlarni aniqlash.</span></li>
    <li><span class="t" data-ru="<b>4. Заполнение паспорта:</b> Записать количество полигонов и свойства в рабочий лист." data-en="<b>4. Asset Passport:</b> Record vertex specifications and physical properties on your worksheet."><b>4. Varaqani to'ldirish:</b> Model hajmi, formati va o'yindagi vazifasini varaqaga yozish.</span></li>
  </ul>
</section>

<section class="slide" data-phase="Amaliyot|3D Спринт|3D Lab Sprint" data-time="27–31">
  <div class="eyebrow"><span data-ru="Лабораторный спринт" data-en="Interactive Lab">Jonli Amaliyot · Taymer</span></div>
  <h2 data-ru="3D-Спринт: 11 Минут на Создание Шедевра" data-en="3D Sprint: 11 Minutes to Sculpt Your Asset">3D Ustaxona: 11 Daqiqalik Jonli Generatsiya</h2>
  <div class="timer" id="timer">
    <div class="digits" id="digits">11:00</div>
    <div class="ctrls">
      <button id="tstart">Start / Stop</button>
      <button class="ghost" id="treset">Reset</button>
    </div>
  </div>
  <p style="margin-top:15px; font-size:0.95em;" data-ru="Откройте сервис генерации 3D. Напишите промпт, сгенерируйте модель и проверьте сетку со всех сторон!" data-en="Open the generative 3D suite. Enter your formula prompt, bake the mesh, and inspect all 360 degrees!">3D generatorni oching. Promptingizni kiriting, modelni generatsiya qiling va uni har tomondan aylantirib ko'ring!</p>
</section>

<section class="slide" data-phase="Tahlil|Демонстрация|Showcase" data-time="31–36">
  <div class="eyebrow"><span data-ru="Презентация моделей" data-en="Asset Showcase">Tahlil va Taqdimot</span></div>
  <h2 data-ru="Парад 3D-Моделей: Презентация и Разбор Ошибок" data-en="3D Asset Parade: Peer Review & Mesh Quality Check">3D Modellar Ko'rigi: Sinov va Fikr-Mulohaza</h2>
  <p data-ru="Покажите свою 3D-модель соседу по парте. Проведите быстрый краш-тест:" data-en="Present your 3D model to your peer. Conduct a rapid QA quality check:">3D modelingizni yoningizdagi sherigingizga ko'rsating va quyidagi 3 savolga javob bering:</p>
  <div class="cols c3" style="display:grid; grid-template-columns:1fr 1fr 1fr; gap:12px; margin-top:15px;">
    <div class="box">
      <h3 style="color:var(--accent);" data-ru="1. Ракурс 360°" data-en="1. 360° Orbit">1. 360° Ko'rinishi</h3>
      <p data-ru="Модель выглядит красиво со спины так же, как и спереди? Нет ли смазанных зон?" data-en="Does the backside look as cohesive as the front? Any collapsed geometry?">Model orqa tomonidan ham oldi kabi chiroylimi? Yuvilib ketgan joylari yo'qmi?</p>
    </div>
    <div class="box">
      <h3 style="color:var(--accent);" data-ru="2. Текстура" data-en="2. Shading & Texture">2. Rang va Yaltiroqlik</h3>
      <p data-ru="Похож ли металл на настоящий металл? Читаются ли мелкие детали?" data-en="Does the metal look believable? Are fine specular details readable?">Metall haqiqiy temirga o'xshaydimi? Mayda detallari aniq ko'rinyaptimi?</p>
    </div>
    <div class="box" style="border-left:4px solid var(--green);">
      <h3 style="color:var(--green);" data-ru="3. Готовность к игре" data-en="3. Game Ready">3. O'yinga Tayyorligi</h3>
      <p data-ru="Сможет ли Roblox или Minecraft принять этот файл без зависаний?" data-en="Can Roblox or Minecraft import this mesh without dropping FPS?">Roblox yoki o'yin dvijogi ushbu faylni qotmasdan ocholadimi?</p>
    </div>
  </div>
</section>

<section class="slide" data-phase="Uy vazifasi|Домашнее задание|Homework" data-time="36–40">
  <div class="eyebrow"><span data-ru="Домашний проект" data-en="Take-Home Project">Uyga Vazifa</span></div>
  <h2 data-ru="Домашнее Задание: Пак из 2 Объектов + 10 Баллов" data-en="Homework: 2-Asset Pack & 10-Point Rubric">Uyga Vazifa: O'yin Uchun 2 Ta 3D Obyekt To'plami</h2>
  <div class="hw" style="display:grid; grid-template-columns:1.4fr 1fr; gap:20px; margin-top:15px;">
    <div class="box" style="border-left:5px solid var(--accent);">
      <h3 style="color:var(--accent);" data-ru="Что нужно сделать:" data-en="Assignment Details:">Bajarilishi shart bo'lgan vazifalar:</h3>
      <ol style="margin-top:8px; padding-left:18px; line-height:1.6;">
        <li data-ru="Создать 2 3D-модели для своего проекта: 1 оружие/инструмент + 1 предмет окружения (сундук, турель или портал)." data-en="Generate 2 3D assets for your project: 1 weapon/tool + 1 environmental prop (chest, turret, or portal).">O'z loyihangiz uchun 2 ta 3D model yarating: 1 ta qurol/asbob + 1 ta atrof-muhit buyumi (sandiq, to'siq yoki portal).</li>
        <li data-ru="Скачать обе модели в формате .GLB или сделать скриншоты со всех 4 сторон." data-en="Download both models in .GLB format or capture orthographic screenshots from 4 angles.">Ikkala modelni .GLB formatda saqlang yoki 4 tomondan olingan skrinshotlarini tayyorlang.</li>
        <li data-ru="Заполнить технический паспорт объекта в рабочей тетради (материал, назначение, полигонаж)." data-en="Complete the technical asset passport in your workbook (material, stats, lore).">Varaqadagi texnik pasportni to'liq to'ldiring (material, o'yindagi kuchi, xususiyatlari).</li>
      </ol>
    </div>
    <div class="box" style="background:var(--panel);">
      <h3 style="color:var(--green);" data-ru="Критерии Оценки (10 баллов):" data-en="Grading Rubric (10 Points):">Baholash Mezoni (10 ball):</h3>
      <ul style="margin-top:8px; padding-left:16px; line-height:1.6; font-size:0.9em;">
        <li data-ru="<b>3 балла:</b> Формула промпта из 4 частей составлена верно." data-en="<b>3 pts:</b> 4-part prompt formula correctly structured."><b>3 ball:</b> 4 qismli prompt formulasi to'g'ri yozilgan.</li>
        <li data-ru="<b>4 балла:</b> Созданы 2 цельные 3D-модели без дыр и артефактов." data-en="<b>4 pts:</b> 2 watertight 3D meshes without floating debris."><b>4 ball:</b> Teshiklarsiz, toza 2 ta 3D model generatsiya qilingan.</li>
        <li data-ru="<b>3 балла:</b> Технический паспорт и характеристики заполнены в тетради." data-en="<b>3 pts:</b> Technical passport fully completed in workbook."><b>3 ball:</b> Varaqadagi texnik parametrlar to'liq to'ldirilgan.</li>
      </ul>
    </div>
  </div>
</section>
"""

l7_notes = {
  'uz': [
    "Kirish: O'quvchilarga Roblox va Minecraftdagi 3D modellarni ko'rsating. 2D rasmdan 3D fazoviy to'rga o'tish maqsadini e'lon qiling.",
    "2D va 3D farqi: X, Y va Z o'qlari haqida tushuntiring. Doskada yassi qog'oz va quti solishtirilsin.",
    "3D anatomiyasi: Nuqtalar (Vertices), Poligonlar (Faces) va Tekstura qatlami haqida gapiring.",
    "AI bilan 3D yaratish: Matndan 3D to'r chiqarish mexanizmi va .GLB formati.",
    "Prompt formulasi: Obyekt + Uslub + Material + To'r sifati.",
    "3D xatoliklari: Teshiklar, ortiqcha poligonlar va havoda qolgan keraksiz nuqsonlar.",
    "Amaliy vazifa: O'z o'yini uchun 1 ta afsonaviy 3D artefakt yaratish topshirig'i.",
    "Jonli sprint: 11 daqiqalik taymer. O'quvchilar modelni generatsiya qilib, 360 daraja aylantirib ko'rishadi.",
    "Tahlil: Juftliklarda bir-birining modelini ko'rib chiqish va fikr bildirish.",
    "Uy vazifasi: 2 ta 3D model va texnik pasportni to'ldirish. 10 ballik mezon."
  ],
  'ru': [
    "Вступление: Покажите любимые 3D-модели из Roblox и Minecraft. Объявите переход к трехмерным объектам.",
    "Разница 2D и 3D: Объясните оси X, Y и глубину Z на простом примере коробки.",
    "Анатомия 3D: Вершины, полигоны и текстура.",
    "Генеративный 3D: Как нейросети строят пространственные модели из текста (.GLB).",
    "Формула промпта: Объект + Стиль + Материал + Сетка.",
    "Ошибки геометрии: Дырки в полигонах, перегрузка полигонами и артефакты.",
    "Постановка задачи: Создание ключевого 3D-артефакта для игры.",
    "Практический спринт: Таймер на 11 минут. Генерация и осмотр модели на 360°.",
    "Анализ и показ: Взаимная проверка в парах по критериям.",
    "Домашнее задание: Сгенерировать пак из 2 моделей и заполнить паспорт (10 баллов)."
  ],
  'en': [
    "Opening: Showcase iconic Roblox and Minecraft 3D assets. Announce spatial 3D game meshes.",
    "2D vs 3D: Coordinate axes X, Y, and Z (depth). Contrast flat sprite vs physical mesh.",
    "Asset Anatomy: Demystify vertices, polygonal faces, and texture mapping.",
    "Generative 3D: Volumetric point clouds into watertight .GLB mesh files.",
    "Prompt Formula: Subject + Art Style + Surface Shaders + Mesh Quality.",
    "Geometry Traps: Inverted normals, excessive polygons, and disconnected debris.",
    "Mission Brief: Design one flagship 3D artifact or vehicle.",
    "Live Lab Sprint: 11-minute timer. Input prompts and inspect 360° turnaround.",
    "Showcase & Debrief: Peer review evaluating backside cohesion and engine readiness.",
    "Homework: Engineer a 2-asset pack (.GLB) and finalize the technical passport."
  ]
}

p7_html = build_presentation("07-dars: 3D Modellar Dunyosi va Obyektlar", l7_slides, l7_notes)
with open(os.path.join(l7_dir, "prezentatsiya.html"), "w", encoding="utf-8") as f:
    f.write(p7_html)

l7_t1 = {"uz": "3D Modellar Dunyosi va Obyektlar", "ru": "Мир 3D-Моделей и Игровые Объекты", "en": "The World of 3D Models & Game Assets"}
l7_s1 = {"uz": "Roblox va Minecraft uchun AI yordamida 3D to'rlar, poligonlar va hajmli modellarni loyihalang.", "ru": "Проектируйте 3D-сетки, полигоны и объемные ассеты для Roblox и Minecraft с помощью ИИ.", "en": "Architect 3D meshes, polygon topology, and volumetric assets for Roblox and Minecraft via AI."}
l7_k1 = {"uz": "3D model — bu shunchaki rasm emas, balki fazoviy poligonlardan yig'ilgan haqiqiy geometrik to'rdir.", "ru": "3D-модель — это не просто картинка, а реальная геометрическая сетка из пространственных полигонов.", "en": "A 3D model is not a mere picture; it is a true geometric mesh sculpted from spatial polygons."}

l7_p1 = """
  <section class="sec">
    <div class="h"><span class="no">01</span><h2><span lang="uz">2D Rasm va 3D Model Farqi</span><span lang="ru">Разница 2D и 3D</span><span lang="en">2D vs 3D Difference</span></h2></div>
    <div class="compare">
      <div class="bad">
        <span class="lbl"><span lang="uz">2D Yassi Sprayt (X, Y)</span><span lang="ru">2D Спрайт (X, Y)</span><span lang="en">2D Flat Sprite (X, Y)</span></span>
        <p class="pr"><span lang="uz">Faqat eni va bo'yi bor. Aylantirib orqasini ko'rib bo'lmaydi. Har bir burilish uchun alohida rasm chizish shart.</span><span lang="ru">Только ширина и высота. Нельзя обойти сзади. Для каждого ракурса нужно рисовать заново.</span><span lang="en">Only width and height. Cannot be orbited. Requires separate drawing for each angle.</span></p>
      </div>
      <div class="good">
        <span class="lbl"><span lang="uz">3D Hajmli To'r (X, Y, Z)</span><span lang="ru">3D Объемная Сетка (X, Y, Z)</span><span lang="en">3D Volumetric Mesh (X, Y, Z)</span></span>
        <p class="pr"><span lang="uz">Haqiqiy chuqurlik (Z) bor! 360° erkin aylanadi, o'yin ichida yorug'lik va fizika qonunlariga to'liq bo'ysunadi.</span><span lang="ru">Имеет глубину (Z)! Свободно вращается на 360°, реагирует на свет и физику в движке.</span><span lang="en">True spatial depth (Z)! Free 360° rotation with dynamic lighting and physics response.</span></p>
      </div>
    </div>
  </section>

  <section class="sec">
    <div class="h"><span class="no">02</span><h2><span lang="uz">3D Model Komponentlari</span><span lang="ru">Компоненты 3D-Модели</span><span lang="en">3D Model Components</span></h2></div>
    <div class="trio">
      <div>
        <b><span lang="uz">Nuqtalar (Vertices) 📍</span><span lang="ru">Вершины 📍</span><span lang="en">Vertices 📍</span></b>
        <span class="d"><span lang="uz">Fazoviy koordinatalar — to'rning tayanch ustunlari.</span><span lang="ru">Координаты X,Y,Z — опорные точки сетки.</span><span lang="en">X,Y,Z coordinate points anchoring the mesh.</span></span>
      </div>
      <div>
        <b><span lang="uz">Poligonlar (Faces) 📐</span><span lang="ru">Полигоны 📐</span><span lang="en">Polygons 📐</span></b>
        <span class="d"><span lang="uz">Nuqtalarni bog'lovchi uchburchak yassi yuzalar.</span><span lang="ru">Плоские треугольники между точками.</span><span lang="en">Flat geometric facets bridging vertices.</span></span>
      </div>
      <div>
        <b><span lang="uz">Tekstura (Texture) 🎨</span><span lang="ru">Текстура 🎨</span><span lang="en">Texture 🎨</span></b>
        <span class="d"><span lang="uz">Rang, metall yaltiroqligi va sirt materiali qatlami.</span><span lang="ru">Цвет, блеск металла и материал поверхности.</span><span lang="en">Color wrapper defining metallic and matte surfaces.</span></span>
      </div>
    </div>
  </section>

  <section class="sec">
    <div class="h"><span class="no">03</span><h2><span lang="uz">3D Prompt Formulasi (4 Qism)</span><span lang="ru">Формула 3D-Промпта</span><span lang="en">3D Prompt Formula</span></h2></div>
    <div class="formula">
      <div class="p"><b>1. Obyekt</b><span class="d">Kiber-qilich</span></div>
      <div class="plus">+</div>
      <div class="p"><b>2. Uslub</b><span class="d">Low-poly 3D</span></div>
      <div class="plus">+</div>
      <div class="p"><b>3. Material</b><span class="d">Neon titan</span></div>
      <div class="plus">+</div>
      <div class="p"><b>4. To'r</b><span class="d">Single mesh .glb</span></div>
    </div>
  </section>

  <section class="sec">
    <div class="h"><span class="no">04</span><h2><span lang="uz">O'yin Dvijoklari Formatlari</span><span lang="ru">Форматы для Движков</span><span lang="en">Engine Asset Formats</span></h2></div>
    <div class="checklist">
      <div><b>.GLB / .GLTF:</b> <span lang="uz">Zamonaviy o'yinlar va veb uchun to'liq to'r + tekstura birlashtirilgan yagona fayl.</span><span lang="ru">Единый файл: сетка + текстуры для игр и веб.</span><span lang="en">Unified container: mesh + textures in single file.</span></div>
      <div><b>.OBJ:</b> <span lang="uz">Klassik 3D to'r formati (teksturalar alohida .MTL faylda saqlanadi).</span><span lang="ru">Классический формат геометрии (текстуры отдельно).</span><span lang="en">Classic geometry format with separate texture map.</span></div>
    </div>
  </section>
"""

l7_t2 = {"uz": "O'yin 3D Artefakt Pasporti", "ru": "Паспорт 3D-Артефакта Игры", "en": "Game 3D Asset Blueprint"}
l7_s2 = {"uz": "O'zingiz yaratgan 3D modelning xususiyatlari va o'yindagi parametrlarini qayd eting.", "ru": "Зафиксируйте свойства и параметры созданной 3D-модели в игре.", "en": "Document properties and gameplay parameters of your generated 3D asset."}

l7_p2 = """
  <section class="sec">
    <div class="h"><span class="no">05</span><h2><span lang="uz">3D Model Texnik Pasporti</span><span lang="ru">Техпаспорт 3D-Модели</span><span lang="en">3D Technical Passport</span></h2></div>
    <div style="display:grid; grid-template-columns:1fr 1fr; gap:10px; font-size:9pt;">
      <div style="border:1px dashed var(--write); padding:8px;">
        <b>Model Nomi:</b> ___________________________<br><br>
        <b>Kategoriya:</b> [ ] Qurol [ ] Transport [ ] Sandiq<br><br>
        <b>Format:</b> [ ] .GLB [ ] .OBJ [ ] .FBX
      </div>
      <div style="border:1px dashed var(--write); padding:8px;">
        <b>Asosiy Material:</b> _______________________<br><br>
        <b>Yoritish Turi:</b> [ ] Neon [ ] Mat [ ] Shaffof<br><br>
        <b>Poligon Turi:</b> [ ] Low-poly [ ] Stylized 3D
      </div>
    </div>
  </section>

  <section class="sec">
    <div class="h"><span class="no">06</span><h2><span lang="uz">Mening 3D Generatsiya Promptim</span><span lang="ru">Мой 3D-Промпт</span><span lang="en">My 3D Prompt Engineering</span></h2></div>
    <div style="border:1px solid var(--rule); background:var(--panel); padding:10px; min-height:45px; font-family:monospace; font-size:8.5pt;">
      "____________________________________________________________________________________<br>
      ____________________________________________________________________________________"
    </div>
  </section>

  <section class="sec">
    <div class="h"><span class="no">07</span><h2><span lang="uz">O'yindagi Mexanika va Xususiyatlar</span><span lang="ru">Игровые Характеристики</span><span lang="en">In-Game Stats & Utility</span></h2></div>
    <table class="gridtable" style="width:100%; border-collapse:collapse; font-size:8.5pt; text-align:left;">
      <tr style="background:var(--panel-2);">
        <th style="padding:5px; border:1px solid var(--rule);">Parametr</th>
        <th style="padding:5px; border:1px solid var(--rule);">Qiymat</th>
        <th style="padding:5px; border:1px solid var(--rule);">O'yindagi Vazifasi</th>
      </tr>
      <tr>
        <td style="padding:5px; border:1px solid var(--rule);">Chidamlilik (Durability)</td>
        <td style="padding:5px; border:1px solid var(--rule);">______ / 100</td>
        <td style="padding:5px; border:1px solid var(--rule);">Necha marta zarbaga dosh beradi?</td>
      </tr>
      <tr>
        <td style="padding:5px; border:1px solid var(--rule);">Og'irlik (Weight)</td>
        <td style="padding:5px; border:1px solid var(--rule);">______ kg</td>
        <td style="padding:5px; border:1px solid var(--rule);">O'yinchi tezligiga ta'siri</td>
      </tr>
      <tr>
        <td style="padding:5px; border:1px solid var(--rule);">Noyoblik (Rarity)</td>
        <td style="padding:5px; border:1px solid var(--rule);">[ ] Common [ ] Rare [ ] Legendary</td>
        <td style="padding:5px; border:1px solid var(--rule);">Topilish ehtimoli va narxi</td>
      </tr>
    </table>
  </section>

  <section class="sec">
    <div class="h"><span class="no">08</span><h2><span lang="uz">3D Sifat Nazorati (QA Test)</span><span lang="ru">Контроль Качества</span><span lang="en">3D Quality Assurance</span></h2></div>
    <div style="display:flex; flex-direction:column; gap:4px; font-size:8.5pt;">
      <label><input type="checkbox"> Model 360° aylantirib ko'rildi, orqa qismida teshiklar yo'q.</label>
      <label><input type="checkbox"> Ortiqcha havoda osilgan nuqsonlar (debris) tozalandi.</label>
      <label><input type="checkbox"> .GLB fayl muvaffaqiyatli saqlandi va Roblox / 3D dasturda ochildi.</label>
    </div>
  </section>
"""

l7_hw = """
  <p><b>1. Qurol va Buyum:</b> O'z o'yiningiz uchun 2 ta 3D model yarating: 1 ta qurol + 1 ta atrof-muhit buyumi.</p>
  <p><b>2. Fayllarni Saqlash:</b> Ikkala modelni .GLB formatda yuklab oling yoki 4 tomondan olingan skrinshotini tayyorlang.</p>
  <p><b>3. Pasportni To'ldirish:</b> Ushbu varaqadagi barcha texnik parametrlar va o'yindagi kuchini to'liq yozib keling.</p>
"""

l7_crit = """
  <div class="r"><span>3D Prompt formulasi to'g'ri yozilgan</span><b>3</b></div>
  <div class="r"><span>2 ta nuqsonsiz, butun 3D model yaratilgan</span><b>4</b></div>
  <div class="r"><span>Texnik pasport va parametrlar to'ldirilgan</span><b>3</b></div>
"""

l7_nxt = {'uz': "O'yin Dunyosi: Level Design va Biomlar", 'ru': "Игровой Мир: Левел-Дизайн и Биомы", 'en': "Game World: Level Design & Biomes"}

ws7_html = build_worksheet('5-6-sinf', 2, 7, l7_t1, l7_s1, l7_k1, l7_p1, l7_t2, l7_s2, l7_p2, l7_hw, l7_crit, l7_nxt)
with open(os.path.join(l7_dir, 'varaqa.html'), 'w', encoding='utf-8') as f:
    f.write(ws7_html)

print("5-6 Week 2 Lesson 7 generated successfully!")
