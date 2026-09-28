#!/usr/bin/env python3
import os, sys
sys.path.insert(0, '/home/dpdp/target/assets')
from curriculum_generator import build_presentation, build_worksheet

BASE = '/home/dpdp/target/classes/5-6-sinf/2-hafta'
l11_dir = os.path.join(BASE, '11-dars-oyun-interfeysi-ui-hud')
os.makedirs(l11_dir, exist_ok=True)

l11_slides = """
<section class="slide is-on" data-phase="Kirish|Вступление|Opening" data-time="0–3">
  <div class="title-wrap">
    <div class="eyebrow">Vibecoding · <span data-ru="урок 11 · 5-6 классы" data-en="lesson 11 · grades 5-6">11-dars · 5-6 sinflar</span></div>
    <div class="title-meta">
      <span><b lang="uz">Fan:</b><span data-ru=" IT / Vibecoding" data-en=" IT / Vibecoding"> IT / Vibecoding</span><b lang="ru">Предмет:</b><span lang="ru"> IT / Vibecoding</span><b lang="en">Subject:</b><span lang="en"> IT / Vibecoding</span></span>
      <span><b lang="uz">Hafta:</b><span data-ru=" 2" data-en=" 2"> 2</span><b lang="ru">Неделя:</b><span lang="ru"> 2</span><b lang="en">Week:</b><span lang="en"> 2</span></span>
    </div>
    <h1 data-ru="Игровой Интерфейс: HUD, HP-Бары и UI с ИИ" data-en="Game Interface: HUD, HP Bars & In-Game UI with AI">O'yin Interfeysi: HUD, HP Barlari va O'yin UI Dizayni</h1>
    <p class="lede" data-ru="Как игрок понимает, сколько у него жизней и патронов? Изучаем законы Heads-Up Display (HUD), мини-карты, инвентарь и генерацию иконок с ИИ." data-en="How does a player monitor health, ammo, and inventory in real time? Exploring Heads-Up Display (HUD) architecture, minimaps, and AI UI asset generation.">O'yinchi o'z joni (HP), tangalari va o'qlarini qanday ko'rib turadi? Heads-Up Display (HUD) qonunlari, minixarita va AI bilan UI ikonkalari yaratishni o'rganamiz.</p>
  </div>
</section>

<section class="slide" data-phase="Tushuncha|Что такое HUD|HUD Concept" data-time="3–7">
  <div class="eyebrow"><span data-ru="Основы интерфейса" data-en="Interface Foundations">HUD Tushunchasi</span></div>
  <h2 data-ru="Что такое HUD: Приборная Панель Геймера" data-en="What is HUD: The Gamer's Digital Instrument Dashboard">HUD Nima? Ekrandagi Ko'rinmas Asboblar Paneli</h2>
  <p data-ru="HUD (Heads-Up Display) — это слой информации поверх 3D-мира, который держит игрока в курсе событий:" data-en="HUD (Heads-Up Display) is the informational visual layer floating over the 3D game world:">HUD (Heads-Up Display) — bu 3D olam ustiga joylashtirilgan, o'yinchiga eng muhim ma'lumotlarni ko'rsatuvchi oynadir:</p>
  <div class="cols c2" style="margin-top:15px;">
    <div class="box">
      <h3 style="color:var(--ink-2);" data-ru="Ужасный интерфейс (Хаос) ❌" data-en="Cluttered UI ❌">Tartibsiz UI (Ekran to'la) ❌</h3>
      <p data-ru="Кнопки закрывают центр экрана, полоска HP сливается с фоном, шрифт мелкий. Игрок умирает, потому что не заметил, что жизни кончились." data-en="Huge opaque icons obstructing crosshairs, illegible micro-fonts, low contrast. Player dies without realizing HP was zero.">Katta tugmalar ekranni to'sib qo'yadi, jon chizig'i ko'rinmaydi. O'yinchi joni tugab qolganini sezmay o'lib ketadi.</p>
    </div>
    <div class="box" style="border-left:4px solid var(--green);">
      <h3 style="color:var(--green);" data-ru="Профессиональный HUD (Чистота) ✅" data-en="Clean Pro HUD ✅">Professional HUD (Toza) ✅</h3>
      <p data-ru="Центр экрана свободен для обзора! Жизни, патроны и радар разнесены по углам, яркие контрастные цвета предупреждают об опасности." data-en="Screen center stays uncluttered. Vital stats anchored to peripheral corners with high contrast warning colors.">Ekran markazi toza! Jon, o'qlar va minixarita 4 burchakka taqsimlangan, xavf tug'ilganda qizil yonib ogohlantiradi.</p>
    </div>
  </div>
</section>

<section class="slide" data-phase="Arxitektura|Правило 4 Углов|4 Corners Rule" data-time="7–11">
  <div class="eyebrow"><span data-ru="Геометрия экрана" data-en="Screen Layout">4 Burchak Qoidasi</span></div>
  <h2 data-ru="Золотое Правило 4 Углов Игрового Экрана" data-en="The Golden 4-Corner Rule of In-Game HUD Layout">O'yin Ekranining Oltin 4 Burchak Qoidasi</h2>
  <p data-ru="Взгляд геймера сканирует экран по периметру. Классическое распределение HUD-виджетов:" data-en="Gamers scan screens peripherally during intense action. The standard ergonomic layout:">O'yinchi nigohi qizg'in jang paytida 4 burchakka qaraydi. Asosiy elementlar joylashuvi:</p>
  <div class="grid" style="display:grid; grid-template-columns:1fr 1fr; gap:12px; margin-top:10px;">
    <div class="box">
      <h3 style="color:var(--accent);" data-ru="1. Верхний Левый (Статус) 💖" data-en="1. Top-Left (Status) 💖">1. Yuqori Chap: Hayot va Zaxira 💖</h3>
      <p data-ru="Полоска HP (Здоровье), броня, аватарка персонажа и уровень игрока (XP)." data-en="Player HP bar, energy shield, character portrait, and current level (XP).">HP (Jon) chizig'i, qalqon, o'yinchi avatari va darajasi (Level XP).</p>
    </div>
    <div class="box">
      <h3 style="color:var(--accent);" data-ru="2. Верхний Правый (Навигация) 🗺️" data-en="2. Top-Right (Radar) 🗺️">2. Yuqori O'ng: Minixarita 🗺️</h3>
      <p data-ru="Круглый радар, стрелка на квест, количество кристаллов/монет и таймер." data-en="Circular minimap radar, objective waypoint compass, and coin balance.">Doiraviy minixarita, kvestga olib boruvchi kompas, tangalar hisobi.</p>
    </div>
    <div class="box">
      <h3 style="color:var(--accent);" data-ru="3. Нижний Правый (Бой) ⚔️" data-en="3. Bottom-Right (Weapons) ⚔️">3. Quyi O'ng: Qurol va Harakat ⚔️</h3>
      <p data-ru="Выбранное оружие, количество патронов, кнопки способностей и перезарядка." data-en="Equipped weapon slot, ammo counter, special ability cooldown icons.">Tanlangan qurol, qolgan o'qlar soni, maxsus qobiliyat va sakrash tugmasi.</p>
    </div>
    <div class="box">
      <h3 style="color:var(--accent);" data-ru="4. Нижний Левый (Чат / Спец) 🎒" data-en="4. Bottom-Left (Inventory) 🎒">4. Quyi Chap: Inventar / Xabarlar 🎒</h3>
      <p data-ru="Быстрый инвентарь (Hotbar), чат команды или статус микрофона." data-en="Quick-access item hotbar, squad text comms, or interaction prompt.">Tezkor inventar xaltasi (Hotbar), jamoaviy xabarlar yoki harakat tugmasi.</p>
    </div>
  </div>
</section>

<section class="slide" data-phase="Mexanizm|Контраст и Читаемость|Visual Hierarchy" data-time="11–15">
  <div class="eyebrow"><span data-ru="Визуальный контраст" data-en="Visual Contrast">Kontrast Qonunlari</span></div>
  <h2 data-ru="Читаемость за 0.1 Секунды: Контраст и Подложки" data-en="0.1-Second Readability: High Contrast & Dark Underlays">0.1 Soniyada Tushunish: Vizual Kontrast va Qora Soya</h2>
  <p data-ru="В пылу боя игрок не должен щуриться. Интерфейс обязан читаться на любом фоне:" data-en="In mid-combat, players must register health in 0.1 seconds across any background:">Jang paytida o'yinchi harflarni o'qishga vaqt sarflamasligi kerak. Qoidalar:</p>
  <ul class="rules">
    <li><span class="t" data-ru="<b>1. Черная обводка и полупрозрачная подложка:</b> Белые цифры на снежном уровне исчезнут, если под ними нет темной плашки." data-en="<b>1. Dark Stroke & Backdrop:</b> White numerals vanish against snow biomes unless anchored with dark backing."><b>1. To'q orqa fon va qora soya:</b> Qorli xaritada oq raqamlar yo'qolib ketadi — ularning orqasiga qora yarim shaffof plita qo'yiladi.</span></li>
    <li><span class="t" data-ru="<b>2. Цветовое кодирование состояний:</b> 100% HP — зеленый, 50% — желтый, ниже 20% — мигающий ярко-красный!" data-en="<b>2. Color Threshold Signaling:</b> 100% HP = Green, 50% = Amber, sub-20% = Pulsing urgent Red!"><b>2. Ranglar ogohlantirishi:</b> 100% Jon — yashil, 50% — sariq, 20% dan tushganda — qizil yonib-o'chuvchi signal!</span></li>
    <li><span class="t" data-ru="<b>3. Минимализм и прозрачность:</b> 80% площади экрана должно оставаться прозрачным для игры." data-en="<b>3. 80% Transparency Rule:</b> 80% of screen viewport must remain clear for gameplay navigation."><b>3. 80% Shaffoflik Qoidasi:</b> Ekranning kamida 80 foiz maydoni o'yin olami uchun bo'sh turishi shart.</span></li>
  </ul>
</section>

<section class="slide" data-phase="Ko'rsatma|Спрайты UI|UI Sprite Prompt" data-time="15–19">
  <div class="eyebrow"><span data-ru="Промпты интерфейса" data-en="UI Prompting">UI Generatsiya Formulasi</span></div>
  <h2 data-ru="Промпт для Генерации UI-Спрайт Листа в ИИ" data-en="Generating In-Game UI Sprite Sheets with AI">AI Bilan O'yin UI Ikonkalari To'plamini Yaratish Prompti</h2>
  <div class="box" style="background:var(--panel); border-left:5px solid var(--green); padding:16px;">
    <p style="font-family:monospace; font-size:0.95em; line-height:1.6;" data-ru="<b>[ТЕМА]</b> Game UI HUD asset pack, sprite sheet, 2D game icons<br>+ <b>[НАБОР]</b> HP heart icon, mana crystal icon, coin icon, laser ammo badge, locked gate key<br>+ <b>[СТИЛЬ]</b> Clean vector, flat sci-fi cyberpunk style, glowing neon borders<br>+ <b>[ФОН]</b> Isolated on plain solid white background, high contrast, ready for chroma key" data-en="<b>[THEME]</b> Game UI HUD asset pack, modular sprite sheet, vector game badges<br>+ <b>[ASSETS]</b> Health bar container, energy mana crystal, gold coin, laser ammo badge, golden key<br>+ <b>[STYLE]</b> Clean flat sci-fi vector aesthetic, subtle neon rim glow<br>+ <b>[BACKGROUND]</b> Isolated strictly on solid flat white backdrop, no shadows, game-ready">
      <b>1. MAVZU:</b> O'yin UI HUD ikonkalari to'plami (sprite sheet)<br>
      + <b>2. ELEMENTLAR:</b> Qizil HP yurak, havorang kristall, oltin tanga, o'qlar belgisi, kalit<br>
      + <b>3. USLUB:</b> Toza vektor, yassi kiberpank uslubi, neon yaltiroq qirralar<br>
      + <b>4. FON:</b> Oq tekis fonda (solid white background), orqani oson qirqish uchun tayyor
    </p>
  </div>
  <p style="margin-top:12px; font-size:0.9em; color:var(--ink-2);" data-ru="Белый фон позволяет за секунду удалить фон в графическом редакторе и получить прозрачные PNG!" data-en="Solid white backgrounds enable instantaneous background removal for clean transparent PNGs!">Oq fon orqali rasmni 1 soniyada orqa fonsiz shaffof PNG formatga aylantirish mumkin!</p>
</section>

<section class="slide" data-phase="Sinov|Ошибки UI|UI Traps" data-time="19–23">
  <div class="eyebrow"><span data-ru="Ошибки интерфейса" data-en="UI Design Traps">UI Xatolari</span></div>
  <h2 data-ru="3 Катастрофические Ошибки Игрового UI" data-en="3 Fatal UI Sins That Ruin Video Games">O'yinni Buzadigan 3 Ta Xavfli UI Xatosi</h2>
  <p data-ru="Даже крутая игра раздражает, если интерфейс спроектирован с ошибками:" data-en="Even stellar gameplay falls apart if the interface causes friction:">Eng qiziqarli o'yin ham, agar interfeysi noto'g'ri bo'lsa, o'yinchini charchatadi:</p>
  <div class="cols c3" style="display:grid; grid-template-columns:1fr 1fr 1fr; gap:12px; margin-top:12px;">
    <div class="box" style="border-top:4px solid var(--accent);">
      <h3 style="color:var(--accent);" data-ru="1. Перекрытие центра 🚫" data-en="1. Obstructed Crosshair 🚫">1. Markazni To'sish 🚫</h3>
      <p data-ru="Текст миссии или огромная карта прямо посередине экрана. Игрок не видит летящую в него ракету!" data-en="Oversized quest prompts centered right over character crosshairs. Blinds player to threats.">Kvest matni to'ppa-to'g'ri ekran o'rtasiga chiqib qoladi. O'yinchi dushmanning o'qini ko'rolmay qoladi!</p>
    </div>
    <div class="box" style="border-top:4px solid var(--accent);">
      <h3 style="color:var(--accent);" data-ru="2. Мелкий текст 🔍" data-en="2. Microscopic Fonts 🔍">2. Mitti Shriftlar 🔍</h3>
      <p data-ru="На смартфоне или планшете количество патронов видно только под лупой. Шрифты должны быть крупными!" data-en="Microscopic text unreadable on mobile screens. Numbers must be bold and punchy.">Mobil telefonda o'ynaganda o'qlar soni ko'rinmaydi. Raqamlar qalin va yirik bo'lishi shart!</p>
    </div>
    <div class="box" style="border-top:4px solid var(--green);">
      <h3 style="color:var(--green);" data-ru="3. Слепые цвета 🌈" data-en="3. Zero Contrast 🌈">3. Ko'rinmas Ranglar 🌈</h3>
      <p data-ru="Зеленая полоска здоровья на фоне зеленой травы. Игрок не понимает, что здоровье упало." data-en="Green health bars over lush green jungle terrain. HP must feature high-contrast dark borders.">Yashil maysa fonida yashil jon chizig'i. Qora chegaralarsiz jon holati ko'rinmay qoladi.</p>
    </div>
  </div>
</section>

<section class="slide" data-phase="Vazifa|Миссия урока|HUD Mission" data-time="23–27">
  <div class="eyebrow"><span data-ru="Практическая миссия" data-en="HUD Blueprint Mission">Amaliy Vazifa</span></div>
  <h2 data-ru="Миссия: Спроектировать Полный HUD-Макет Экрана" data-en="Mission: Architect Full In-Game HUD Screen Layout">Bugungi Vazifa: O'z O'yiningiz Uchun HUD Maketini Chizing</h2>
  <p data-ru="Сегодня каждый превращается в UI/UX дизайнера и проектирует интерфейс игры на листе:" data-en="Today, each developer steps into UI/UX game design, structuring the HUD layout blueprint:">Bugun har bir o'quvchi UI/UX dizaynerga aylanadi va o'yin ekrani maketini chizadi:</p>
  <ul class="rules">
    <li><span class="t" data-ru="<b>1. Разметка 4 углов:</b> Разместить шкалу HP, радар, счетчик монет и кнопку атаки." data-en="<b>1. 4-Corner Layout:</b> Position HP bar, radar minimap, coin tally, and weapon controls."><b>1. 4 burchakni belgilash:</b> HP paneli, minixarita, tangalar hisoblagichi va qurol tugmasini joylashtirish.</span></li>
    <li><span class="t" data-ru="<b>2. Генерация спрайтов в ИИ:</b> Создать пак из 3 иконок (сердце, монета, кристалл)." data-en="<b>2. AI Sprite Synthesis:</b> Generate an icon set of 3 badges (Health heart, coin, crystal)."><b>2. AI da spraytlar yaratish:</b> 3 ta asosiy ikonka to'plamini (yurak, tanga, kristall) generatsiya qilish.</span></li>
    <li><span class="t" data-ru="<b>3. Проверка читаемости:</b> Добавить черную обводку к цифрам и плашку контраста." data-en="<b>3. Contrast Enforcement:</b> Add dark underlay plates behind text and numbers."><b>3. Kontrastni ta'minlash:</b> Raqamlar orqasiga qora hoshiya va yarim shaffof plita chizish.</span></li>
    <li><span class="t" data-ru="<b>4. Тест соседа:</b> Сосед за 3 секунды находит количество жизней и монет!" data-en="<b>4. 3-Second Peer Test:</b> Partner must identify health and coin totals within 3 seconds! "><b>4. 3 soniyalik test:</b> Sherigingiz 3 soniya ichida jon va tangalar sonini topishi kerak!</span></li>
  </ul>
</section>

<section class="slide" data-phase="Amaliyot|UI-Спринт|UI Lab Sprint" data-time="27–31">
  <div class="eyebrow"><span data-ru="Инженерный спринт" data-en="UI Sprint">Jonli Amaliyot · Taymer</span></div>
  <h2 data-ru="UI-Спринт: 11 Минут на Создание HUD-Интерфейса" data-en="UI Sprint: 11 Minutes to Architect Game HUD">UI Ustaxona: 11 Daqiqalik Ekranni Loyihalash</h2>
  <div class="timer" id="timer">
    <div class="digits" id="digits">11:00</div>
    <div class="ctrls">
      <button id="tstart">Start / Stop</button>
      <button class="ghost" id="treset">Reset</button>
    </div>
  </div>
  <p style="margin-top:15px; font-size:0.95em;" data-ru="Нарисуйте экран игры в тетради и сгенерируйте иконки интерфейса через ИИ!" data-en="Sketch your game screen layout on your worksheet and generate UI icons with AI!">Varaqadagi monitor chizmasiga HUD elementlarini joylang va AI da chiroyli ikonkalarni yarating!</p>
</section>

<section class="slide" data-phase="Tahlil|Тест 3 секунд|3-Sec Audit" data-time="31–36">
  <div class="eyebrow"><span data-ru="Аудит читаемости" data-en="Readability Audit">Tahlil va Test</span></div>
  <h2 data-ru="Тест '3 Секунды': Аудит Читаемости Интерфейса" data-en="The 3-Second Audit: Peer HUD Usability Check">"3 Soniya" Testi: Interfeys Qulayligini Sinash</h2>
  <p data-ru="Покажите лист соседу ровно на 3 секунды, затем закройте рукой. Спросите:" data-en="Show your screen sketch to your peer for exactly 3 seconds, then cover it. Ask:">Varaqadagi chizmani sherigingizga roppa-rosa 3 soniya ko'rsatib, yopib oling. So'rang:</p>
  <div class="cols c3" style="display:grid; grid-template-columns:1fr 1fr 1fr; gap:12px; margin-top:15px;">
    <div class="box">
      <h3 style="color:var(--accent);" data-ru="1. Сколько HP?" data-en="1. What was the HP?">1. Jon Qancha Qolgan?</h3>
      <p data-ru="Заметил ли он цвет шкалы здоровья и уровень опасности?" data-en="Did they immediately register the HP bar level and danger color?">Jon chizig'ining rangi va to'lalik darajasini darhol ilg'adimi?</p>
    </div>
    <div class="box">
      <h3 style="color:var(--accent);" data-ru="2. Где оружие?" data-en="2. Where is Weapon?">2. Qurol Qayerda?</h3>
      <p data-ru="Понятно ли, какое оружие сейчас в руках персонажа?" data-en="Could they tell which weapon was active in the hotbar?">Hozir qo'lda qaysi qurol borligi va uning o'qlari ko'rindimi?</p>
    </div>
    <div class="box" style="border-left:4px solid var(--green);">
      <h3 style="color:var(--green);" data-ru="3. Центр свободен?" data-en="3. Center Unblocked?">3. Markaz Bo'shmi?</h3>
      <p data-ru="Не заслоняют ли гигантские кнопки поле зрения игрока?" data-en="Does the combat crosshair area stay completely open?">Katta tugmalar qahramonning ko'rish maydonini to'smayaptimi?</p>
    </div>
  </div>
</section>

<section class="slide" data-phase="Uy vazifasi|Домашнее задание|Homework" data-time="36–40">
  <div class="eyebrow"><span data-ru="Домашний проект" data-en="Take-Home Project">Uyga Vazifa</span></div>
  <h2 data-ru="Домашнее Задание: Готовый HUD-Макет + 10 Баллов" data-en="Homework: Final In-Game HUD Layout & 10-Point Rubric">Uyga Vazifa: To'liq O'yin HUD Maketi va Ikonkalar</h2>
  <div class="hw" style="display:grid; grid-template-columns:1.4fr 1fr; gap:20px; margin-top:15px;">
    <div class="box" style="border-left:5px solid var(--accent);">
      <h3 style="color:var(--accent);" data-ru="Что нужно сделать:" data-en="Assignment Details:">Bajarilishi shart bo'lgan vazifalar:</h3>
      <ol style="margin-top:8px; padding-left:18px; line-height:1.6;">
        <li data-ru="Полностью оформить экран HUD в рабочей тетради (разместить все 4 угла: HP, карта, патроны, инвентарь)." data-en="Finalize the complete in-game HUD screen layout in your workbook (all 4 corners mapped).">Varaqadagi monitor chizmasiga barcha 4 burchak elementlarini to'liq chizib chiqing.</li>
        <li data-ru="Сгенерировать 1 UI-спрайт лист с 4 игровыми иконками через ИИ на белом фоне." data-en="Generate 1 UI sprite sheet containing 4 game icons on a solid white backdrop via AI.">AI da oq fonda kamida 4 ta o'yin ikonkasidan iborat UI to'plamini yarating.</li>
        <li data-ru="Описать цветовую логику шкалы здоровья (зеленый -> желтый -> красный)." data-en="Document the dynamic color threshold logic for player health states.">Jon chizig'ining dinamik rang o'zgarish qoidalarini daftaringizga yozing.</li>
      </ol>
    </div>
    <div class="box" style="background:var(--panel);">
      <h3 style="color:var(--green);" data-ru="Критерии Оценки (10 баллов):" data-en="Grading Rubric (10 Points):">Baholash Mezoni (10 ball):</h3>
      <ul style="margin-top:8px; padding-left:16px; line-height:1.6; font-size:0.9em;">
        <li data-ru="<b>3 балла:</b> Правило 4 углов соблюдено, центр экрана не загроможден." data-en="<b>3 pts:</b> 4-corner rule respected with center viewport clear."><b>3 ball:</b> 4 burchak qoidasiga amal qilingan, markaz toza.</li>
        <li data-ru="<b>4 балла:</b> Сгенерирован качественный UI-пак иконок на белом фоне." data-en="<b>4 pts:</b> Crisp game UI icon set generated on solid white."><b>4 ball:</b> Oq fonda toza va chiroyli 4 ta UI ikonkasi yaratilgan.</li>
        <li data-ru="<b>3 балла:</b> Добавлены контрастные подложки и цветовая шкала HP." data-en="<b>3 pts:</b> High contrast underlays and dynamic HP states mapped."><b>3 ball:</b> To'q plitalar va ranglar ogohlantirish mantiqi to'ldirilgan.</li>
      </ul>
    </div>
  </div>
</section>
"""

l11_notes = {
  'uz': [
    "Kirish: O'quvchilarga sevimli o'yinlari interfeysini ko'rsating. Jon, tangalar va o'qlar qayerda turishini so'rang.",
    "HUD nima: Asboblar paneli tushunchasi. Tartibsiz ekranni to'suvchi interfeys va toza professional interfeys farqi.",
    "4 burchak qoidasi: Yuqori chap (Jon/Status), Yuqori o'ng (Karta), Quyi o'ng (Qurol/Harakat), Quyi chap (Xaltacha/Chat).",
    "Kontrast va o'qiluvchanlik: Qorli fonda oq harflar yo'qolmasligi uchun to'q plitalar va 80% shaffoflik qoidasi.",
    "UI sprayt prompti: Oq fonda yassi kiberpank piktogrammalar yaratish formulasi tahlil qilinsin.",
    "UI xatolari: Ekranning markazini to'sib qo'yish, o'qib bo'lmaydigan mitti harflar va fonga qo'shilib ketuvchi ranglar.",
    "Amaliy vazifa: Varaqadagi ekranga HUD elementlarini joylashtirish va AI da ikonkalarni generatsiya qilish.",
    "Jonli sprint: 11 daqiqalik taymer. O'quvchilar maketni chizishadi va AI vositasida UI generatsiya qilishadi.",
    "3 soniya testi: Sherigiga 3 soniya ko'rsatib, jon va tangalar sonini topish mashqi orqali qulaylikni tekshirish.",
    "Uy vazifasi: HUD ekranini tugatish va 4 ta ikonkali UI to'plamini tayyorlash. 10 ballik baholash mezoni."
  ],
  'ru': [
    "Вступление: Покажите скриншоты популярных игр. Спросите, где геймеры видят здоровье и патроны.",
    "Суть HUD: Концепт приборной панели. Разница между захламленным хаосом и чистым эргономичным экраном.",
    "Правило 4 углов: Верх-лево (HP/Статус), Верх-право (Радар), Низ-право (Оружие/Атака), Низ-лево (Инвентарь).",
    "Контраст и читаемость: Зачем нужны черные обводки и почему 80% экрана обязано оставаться прозрачным.",
    "Формула промпта: Генерация спрайт-листа векторных иконок на сплошном белом фоне для легкой обтравки.",
    "Ошибки интерфейса: Перекрытие перекрестья прицела, слепые цвета без контраста и мелкий нечитаемый шрифт.",
    "Постановка задачи: Спроектировать интерфейс на сетке монитора и сгенерировать набор иконок.",
    "Практический спринт: Таймер на 11 минут. Ученики рисуют HUD и генерируют элементы.",
    "Тест '3 секунды': Сосед за 3 секунды должен мгновенно назвать остаток здоровья и патронов.",
    "Домашнее задание: Оформить полный HUD-макет и пак из 4 иконок (10 баллов)."
  ],
  'en': [
    "Opening: Project iconic game screenshots. Prompt students to identify where vitals and resources reside.",
    "HUD Foundations: The dashboard metaphor. Contrast suffocating visual clutter against clean spatial awareness.",
    "The 4 Corners Rule: Top-left (Vitals), Top-right (Nav radar), Bottom-right (Combat triggers), Bottom-left (Pouch/Chat).",
    "Contrast & Legibility: Why white UI elements require dark drop shadows and the 80% viewport transparency standard.",
    "UI Prompt Formula: Synthesizing modular vector sprite sheets against clean flat white backgrounds.",
    "UI Design Traps: Obstructing combat reticles, zero contrast across varying terrain, and unreadable micro-type.",
    "Mission Brief: Design a screen blueprint on the monitor template and synthesize an icon set.",
    "Live Lab Sprint: 11-minute timer. Students draft wireframes and generate vector HUD assets.",
    "The 3-Second Audit: Rapid peer usability check ensuring vitals can be parsed in a glance.",
    "Homework: Finalize the in-game HUD wireframe and generate 4 modular UI icons. Review the 10-point rubric."
  ]
}

p11_html = build_presentation("11-dars: O'yin Interfeysi: HUD va UI Dizayn", l11_slides, l11_notes)
with open(os.path.join(l11_dir, "prezentatsiya.html"), "w", encoding="utf-8") as f:
    f.write(p11_html)

l11_t1 = {"uz": "O'yin Interfeysi: HUD va UI Dizayn", "ru": "Игровой Интерфейс: HUD и UI", "en": "Game Interface: HUD & UI Design"}
l11_s1 = {"uz": "O'yinchi ko'zini charchatmaydigan 4 burchak qoidasidagi HUD interfeysi va AI ikonkalarni loyihalang.", "ru": "Проектируйте эргономичный HUD по правилу 4 углов и иконки интерфейса с ИИ.", "en": "Architect an ergonomic 4-corner HUD layout and generative UI badges with AI."}
l11_k1 = {"uz": "Eng zo'r interfeys — bu ko'zga tashlanmaydigan, lekin 0.1 soniyada barcha ma'lumotni yetkazuvchi HUD dir.", "ru": "Идеальный интерфейс незаметен в бою, но сообщает главное за 0.1 секунды.", "en": "The ultimate UI stays invisible in combat while communicating critical vitals in 0.1 seconds."}

l11_p1 = """
  <section class="sec">
    <div class="h"><span class="no">01</span><h2><span lang="uz">HUD Asosiy Qonuni</span><span lang="ru">Закон Читаемости HUD</span><span lang="en">The Law of Clean HUD</span></h2></div>
    <div class="compare">
      <div class="bad">
        <span class="lbl"><span lang="uz">Tartibsiz Ekran (Chaos)</span><span lang="ru">Захламленный Экран</span><span lang="en">Cluttered Viewport</span></span>
        <p class="pr"><span lang="uz">Ekranning markazi yozuvlar bilan to'la. Jon chizig'i ko'rinmaydi. O'yinchi dushmanni ko'rolmay yutqazadi.</span><span lang="ru">Кнопки закрывают обзор. Шкала жизней сливается с травой. Игрок слеп в бою.</span><span lang="en">Icons block the crosshairs. Low contrast makes HP unreadable against bright biomes.</span></p>
      </div>
      <div class="good">
        <span class="lbl"><span lang="uz">Professional HUD (Toza)</span><span lang="ru">Профессиональный HUD</span><span lang="en">Ergonomic Pro HUD</span></span>
        <p class="pr"><span lang="uz">Ekran markazi toza! Jon va o'qlar 4 burchakda, to'q plitalar bilan himoyalangan. 0.1 soniyada tushuniladi!</span><span lang="ru">Центр свободен. Элементы разнесены по углам с темной обводкой. Читается мгновенно!</span><span lang="en">Center stays clear. Vitals anchored to peripheral corners with dark contrast backing.</span></p>
      </div>
    </div>
  </section>

  <section class="sec">
    <div class="h"><span class="no">02</span><h2><span lang="uz">Ekran 4 Burchagi Taqsimoti</span><span lang="ru">4 Угла Экрана</span><span lang="en">4 Screen Corners</span></h2></div>
    <div class="trio">
      <div>
        <b><span lang="uz">Yuqori Chap: Status 💖</span><span lang="ru">Верх-Лево 💖</span><span lang="en">Top-Left 💖</span></b>
        <span class="d"><span lang="uz">HP hayot chizig'i, daraja (XP), qalqon.</span><span lang="ru">Здоровье (HP), щит, аватарка.</span><span lang="en">Player HP bar, shields, avatar portrait.</span></span>
      </div>
      <div>
        <b><span lang="uz">Yuqori O'ng: Karta 🗺️</span><span lang="ru">Верх-Право 🗺️</span><span lang="en">Top-Right 🗺️</span></b>
        <span class="d"><span lang="uz">Minixarita radari, kvest yo'nalishi, tangalar.</span><span lang="ru">Радар, стрелка квеста, монеты.</span><span lang="en">Radar minimap, objective compass, gold.</span></span>
      </div>
      <div>
        <b><span lang="uz">Quyi O'ng: Qurol ⚔️</span><span lang="ru">Низ-Право ⚔️</span><span lang="en">Bottom-Right ⚔️</span></b>
        <span class="d"><span lang="uz">Qurol ikonkasi, o'qlar soni va sakrash tugmasi.</span><span lang="ru">Оружие, патроны, кнопка удара.</span><span lang="en">Equipped weapon, ammo counter, attack trigger.</span></span>
      </div>
    </div>
  </section>

  <section class="sec">
    <div class="h"><span class="no">03</span><h2><span lang="uz">UI Ikonkalari AI Prompt Formulasi</span><span lang="ru">Формула UI-Промпта</span><span lang="en">UI Prompt Blueprint</span></h2></div>
    <div class="formula">
      <div class="p"><b>1. Mavzu</b><span class="d">Game UI pack</span></div>
      <div class="plus">+</div>
      <div class="p"><b>2. Ikonkalar</b><span class="d">HP, coin, key</span></div>
      <div class="plus">+</div>
      <div class="p"><b>3. Uslub</b><span class="d">Flat neon vector</span></div>
      <div class="plus">+</div>
      <div class="p"><b>4. Fon</b><span class="d">Solid white</span></div>
    </div>
  </section>

  <section class="sec">
    <div class="h"><span class="no">04</span><h2><span lang="uz">Kontrast va Shaffoflik Standarti</span><span lang="ru">Стандарт Контраста</span><span lang="en">Contrast Standard</span></h2></div>
    <div class="checklist">
      <div><b>80% Shaffoflik:</b> <span lang="uz">Ekranning 80% maydoni o'yin olamini ko'rish uchun bo'sh turishi shart.</span><span lang="ru">80% площади экрана свободно для обзора мира.</span><span lang="en">80% of screen viewport must remain clear for gameplay navigation.</span></div>
      <div><b>Dinamik HP Rangi:</b> <span lang="uz">100% Jon = Yashil; 50% = Sariq; 20% dan past = Qizil yonib-o'chuvchi signal!</span><span lang="ru">100% HP = зеленый; 50% = желтый; &lt;20% = мигающий красный.</span><span lang="en">100% HP = Green; 50% = Amber; &lt;20% = Pulsing urgent Red!</span></div>
    </div>
  </section>
"""

l11_t2 = {"uz": "O'yin Monitori HUD Maketi", "ru": "Скетч Монитора Игры", "en": "Game Screen HUD Blueprint"}
l11_s2 = {"uz": "O'yin ekranidagi 4 burchakka HUD vidjetlarini joylashtiring va chizing.", "ru": "Разместите виджеты интерфейса по 4 углам экрана монитора.", "en": "Wireframe HUD widgets across the 4 peripheral screen corners."}

l11_p2 = """
  <section class="sec">
    <div class="h"><span class="no">05</span><h2><span lang="uz">Monitor Ekran Maketi (Wireframe)</span><span lang="ru">Скетч Экрана (Wireframe)</span><span lang="en">Screen Wireframe Template</span></h2></div>
    <div style="border:3px solid var(--ink); border-radius:6px; height:120px; position:relative; background:var(--panel);">
      <!-- Top Left -->
      <div style="position:absolute; top:6px; left:6px; border:1px solid var(--accent); background:#FFEBEE; padding:2px 6px; font-size:7pt; border-radius:3px;">
        <b>[HP Bar]</b> [■■■■□] 85/100
      </div>
      <!-- Top Right -->
      <div style="position:absolute; top:6px; right:6px; border:1px solid var(--ink-2); background:#EDE7F6; padding:2px 6px; font-size:7pt; border-radius:3px;">
        <b>[MAP]</b> 🧭 Quest: 120m | 🪙 450
      </div>
      <!-- Center Crosshair -->
      <div style="position:absolute; top:50%; left:50%; transform:translate(-50%, -50%); font-size:12pt; color:var(--ink-3);">
        +
      </div>
      <!-- Bottom Left -->
      <div style="position:absolute; bottom:6px; left:6px; border:1px solid var(--write); background:var(--sheet); padding:2px 6px; font-size:7pt; border-radius:3px;">
        [Hotbar: 1 2 3 4] 🎒
      </div>
      <!-- Bottom Right -->
      <div style="position:absolute; bottom:6px; right:6px; border:1px solid var(--green); background:#E8F5E9; padding:2px 6px; font-size:7pt; border-radius:3px;">
        ⚔️ <b>Plazma Qilich</b> | ⚡ 100%
      </div>
    </div>
  </section>

  <section class="sec">
    <div class="h"><span class="no">06</span><h2><span lang="uz">Mening UI Ikonkalarim (AI Prompt)</span><span lang="ru">Промпт Иконок</span><span lang="en">UI Icons AI Prompt</span></h2></div>
    <div style="border:1px solid var(--rule); background:var(--panel); padding:8px; min-height:40px; font-family:monospace; font-size:8pt;">
      "Game UI HUD sprite sheet of ___________________________________________________________<br>
      flat vector cyberpunk style, glowing neon edges, isolated on solid plain white background"
    </div>
  </section>

  <section class="sec">
    <div class="h"><span class="no">07</span><h2><span lang="uz">Interfeys Ranglar Matritsasi</span><span lang="ru">Цветовая Матрица</span><span lang="en">Color Hierarchy Matrix</span></h2></div>
    <table class="gridtable" style="width:100%; border-collapse:collapse; font-size:8.5pt; text-align:left;">
      <tr style="background:var(--panel-2);">
        <th style="padding:4px; border:1px solid var(--rule);">Element</th>
        <th style="padding:4px; border:1px solid var(--rule);">Rang Kodi</th>
        <th style="padding:4px; border:1px solid var(--rule);">O'yinchi Holati</th>
      </tr>
      <tr>
        <td style="padding:4px; border:1px solid var(--rule);">Sog'lom (Full HP)</td>
        <td style="padding:4px; border:1px solid var(--rule);">Zumrad Yashil (#00E676)</td>
        <td style="padding:4px; border:1px solid var(--rule);">Xavf yo'q, kuchli</td>
      </tr>
      <tr>
        <td style="padding:4px; border:1px solid var(--rule);">Yaralangan (Low HP)</td>
        <td style="padding:4px; border:1px solid var(--rule);">Miltillovchi Qizil (#FF1744)</td>
        <td style="padding:4px; border:1px solid var(--rule);">Ogohlantirish: qochish kerak!</td>
      </tr>
      <tr>
        <td style="padding:4px; border:1px solid var(--rule);">Maxsus Qobiliyat (Ultimate)</td>
        <td style="padding:4px; border:1px solid var(--rule);">Moviy Neon (#00E5FF)</td>
        <td style="padding:4px; border:1px solid var(--rule);">Hujumga tayyor</td>
      </tr>
    </table>
  </section>

  <section class="sec">
    <div class="h"><span class="no">08</span><h2><span lang="uz">3 Soniya Testi: Nazorat</span><span lang="ru">Тест 3 Секунды</span><span lang="en">3-Second Readability Test</span></h2></div>
    <div style="display:flex; flex-direction:column; gap:4px; font-size:8.5pt;">
      <label><input type="checkbox"> Sherigim 3 soniyada qancha jon borligini to'g'ri aytdi.</label>
      <label><input type="checkbox"> Ekran markazi jang va harakat uchun bo'sh qoldirilgan.</label>
      <label><input type="checkbox"> UI ikonkalari oq fonda toza qilib generatsiya qilindi.</label>
    </div>
  </section>
"""

l11_hw = """
  <p><b>1. Monitor Maketi:</b> Varaqadagi ekran chizmasiga barcha 4 burchak vidjetlarini aniq chizing.</p>
  <p><b>2. UI Sprayt To'plami:</b> Oq fonda kamida 4 ta o'yin ikonkasini AI da generatsiya qiling va saqlang.</p>
  <p><b>3. Ranglar Mantig'i:</b> Jon va energiya holatlari bo'yicha ranglar jadvalini to'liq yozib keling.</p>
"""

l11_crit = """
  <div class="r"><span>4 burchak qoidasi bajarilgan, markaz toza</span><b>3</b></div>
  <div class="r"><span>4 ta toza UI ikonkasi oq fonda yaratilgan</span><b>4</b></div>
  <div class="r"><span>Ranglar ogohlantirishi to'g'ri belgilangan</span><b>3</b></div>
"""

l11_nxt = {'uz': "Game Jam: Mini-O'yin Prototipi Taqdimoti", 'ru': "Game Jam: Презентация Прототипа", 'en': "Game Jam: Mini-Game Prototype Pitch"}

ws11_html = build_worksheet('5-6-sinf', 2, 11, l11_t1, l11_s1, l11_k1, l11_p1, l11_t2, l11_s2, l11_p2, l11_hw, l11_crit, l11_nxt)
with open(os.path.join(l11_dir, 'varaqa.html'), 'w', encoding='utf-8') as f:
    f.write(ws11_html)

print("5-6 Week 2 Lesson 11 generated successfully!")
