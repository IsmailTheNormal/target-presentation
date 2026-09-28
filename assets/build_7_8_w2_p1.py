#!/usr/bin/env python3
import os, sys
sys.path.insert(0, '/home/dpdp/target/assets')
from curriculum_generator import build_presentation, build_worksheet

BASE = '/home/dpdp/target/classes/7-8-sinf/2-hafta'

# =========================================================================
# LESSON 7: VEB-USTAXONASI: CSS FLEXBOX VA GRID
# =========================================================================
l7_dir = os.path.join(BASE, '07-dars-veb-ustaxonasi-grid-va-flexbox')
os.makedirs(l7_dir, exist_ok=True)

l7_slides = """
<section class="slide is-on" data-phase="Kirish|Вступление|Opening" data-time="0–3">
  <div class="title-wrap">
    <div class="eyebrow">Vibecoding · <span data-ru="урок 7 · 7-8 классы" data-en="lesson 7 · grades 7-8">7-dars · 7-8 sinflar</span></div>
    <div class="title-meta">
      <span><b lang="uz">Fan:</b><span data-ru=" IT / Vibecoding" data-en=" IT / Vibecoding"> IT / Vibecoding</span><b lang="ru">Предмет:</b><span lang="ru"> IT / Vibecoding</span><b lang="en">Subject:</b><span lang="en"> IT / Vibecoding</span></span>
      <span><b lang="uz">Hafta:</b><span data-ru=" 2" data-en=" 2"> 2</span><b lang="ru">Неделя:</b><span lang="ru"> 2</span><b lang="en">Week:</b><span lang="en"> 2</span></span>
    </div>
    <h1 data-ru="Веб-Мастерская: Верстка на CSS Flexbox и Grid" data-en="Web Workshop: Modern Layouts with CSS Flexbox & Grid">Veb-Ustaxona: CSS Flexbox va Grid Bilan Maket Tuzish</h1>
    <p class="lede" data-ru="Как современные сайты выстраивают карточки игр и меню ровно по струнке? Осваиваем одномерный Flexbox и двумерный CSS Grid для создания игрового портала." data-en="How do modern platforms align game cards and navbars with pixel-perfect precision? Mastering 1D Flexbox and 2D CSS Grid to architect an esports gaming portal.">Qanday qilib zamonaviy saytlar o'yin kartalari va menyularni chiroyli qatorga tizadi? O'yin portali yaratish uchun 1 o'lchamli Flexbox va 2 o'lchamli Grid texnologiyasini o'rganamiz.</p>
  </div>
</section>

<section class="slide" data-phase="Tushuncha|Flexbox против Grid|Flex vs Grid" data-time="3–7">
  <div class="eyebrow"><span data-ru="Анатомия верстки" data-en="Layout Geometry">Maket Anatomiyasi</span></div>
  <h2 data-ru="Битва Титанов: Flexbox против CSS Grid" data-en="Clash of Titans: CSS Flexbox vs CSS Grid">Qachon Qaysi Biri Kerak? Flexbox vs Grid</h2>
  <p data-ru="В современной веб-разработке верстка делится на два мощных инструмента:" data-en="Modern front-end architecture relies on two complementary layout engines:">Zamonaviy veb dasturlashda elementlarni joylashtirish 2 ta qurolga tayanadi:</p>
  <div class="cols c2" style="margin-top:15px;">
    <div class="box">
      <h3 style="color:var(--ink-2);" data-ru="CSS Flexbox (1D — Одно измерение) 📏" data-en="CSS Flexbox (1D - One Dimension) 📏">CSS Flexbox (1 O'lchamli) 📏</h3>
      <p data-ru="Идеален для одного ряда или одной колонки: панель навигации (Navbar), центрирование кнопки или ряд иконок. Элементы гибко сжимаются и растягиваются." data-en="Engineered for single-axis flow (rows OR columns): navbars, button centering, or icon rows. Content dynamically flexes and stretches.">Faqat 1 ta qator YOKI 1 ta ustun uchun mo'ljallangan: menyular paneli (Navbar), tugmani markazlashtirish yoki piktogrammalar qatori.</p>
    </div>
    <div class="box" style="border-left:4px solid var(--accent);">
      <h3 style="color:var(--accent);" data-ru="CSS Grid (2D — Два измерения) 🔲" data-en="CSS Grid (2D - Two Dimensions) 🔲">CSS Grid (2 O'lchamli) 🔲</h3>
      <p data-ru="Управляет и рядами, и колонками одновременно! Идеален для витрины карточек игр (3x3), фотогалерей и сложных экранов дашборда." data-en="Governs rows AND columns simultaneously! Perfect for game card showcases (3x3), esports dashboard grids, and responsive photo galleries.">Bir vaqtning o'zida ham qatorlar, ham ustunlarni boshqaradi! O'yin kartalari vitrinasi (3x3), foto galereyalar va murakkab panellar uchun ideal.</p>
    </div>
  </div>
</section>

<section class="slide" data-phase="Arxitektura|Flexbox Свойства|Flexbox Properties" data-time="7–11">
  <div class="eyebrow"><span data-ru="Команды Flexbox" data-en="Flexbox Engine">Flexbox Buyruqlari</span></div>
  <h2 data-ru="3 Главных Свойства Flexbox для Управления Элементами" data-en="The 3 Core CSS Flexbox Rules for Clean Alignment">Elementlarni Boshqaruvchi 3 Asosiy Flexbox Qoidasi</h2>
  <p data-ru="Достаточно написать <code>display: flex;</code> на родительском блоке, и элементы подчиняются правилам:" data-en="Specifying <code>display: flex;</code> unlocks precision alignment commands across the axis:">Konteynerga <code>display: flex;</code> yozishingiz bilan quyidagi xususiyatlar ishga tushadi:</p>
  <div class="cols c3" style="display:grid; grid-template-columns:1fr 1fr 1fr; gap:12px; margin-top:12px;">
    <div class="box" style="border-top:4px solid var(--green);">
      <h3 style="color:var(--green);" data-ru="1. justify-content ↔️" data-en="1. justify-content ↔️">1. justify-content ↔️</h3>
      <p data-ru="Выравнивание по горизонтали: <code>center</code> (в центр), <code>space-between</code> (разнести по краям меню)." data-en="Horizontal alignment: <code>center</code>, or <code>space-between</code> (push logo left, buttons right).">Gorizontal tekislash: <code>center</code> (o'rtaga) yoki <code>space-between</code> (chetlarga tarqatish).</p>
    </div>
    <div class="box" style="border-top:4px solid var(--accent);">
      <h3 style="color:var(--accent);" data-ru="2. align-items ↕️" data-en="2. align-items ↕️">2. align-items ↕️</h3>
      <p data-ru="Выравнивание по вертикали: <code>center</code> выравнивает текст и иконки строго по одной линии по высоте." data-en="Vertical alignment: <code>center</code> locks icons and text to the exact vertical midline.">Vertikal tekislash: <code>center</code> yozuv va piktogrammalarni balandlik bo'yicha simmetrik qiladi.</p>
    </div>
    <div class="box" style="border-top:4px solid #00E5FF;">
      <h3 style="color:#00838F;" data-ru="3. gap (Отступы) 📐" data-en="3. gap (Spacing) 📐">3. gap (Masofa) 📐</h3>
      <p data-ru="Автоматический отступ между карточками: <code>gap: 16px;</code> избавляет от старых костылей с margin." data-en="Air-gap spacing between cards: <code>gap: 16px;</code> eliminates clunky legacy margin hacks.">Kartalar orasidagi toza masofa: <code>gap: 16px;</code> eski margin xatolarini yo'q qiladi.</p>
    </div>
  </div>
</section>

<section class="slide" data-phase="Mexanizm|Сетка CSS Grid|CSS Grid System" data-time="11–15">
  <div class="eyebrow"><span data-ru="Магия Grid" data-en="Grid System">CSS Grid Sehri</span></div>
  <h2 data-ru="Магия Grid: Создание Адаптивной Витрины за 1 Строку" data-en="CSS Grid Magic: Responsive Game Storefront in 1 Line">CSS Grid: 1 Qator Kod Bilan Avtomatik Vitrina</h2>
  <p data-ru="Забудьте про расчет процентов ширины. Одна строка Grid автоматически адаптирует карточки под экраны:" data-en="Forget manual percentage math. One CSS Grid rule dynamically reflows cards across devices:">Eni foizlarini hisoblashni unuting. Grid bitta qator bilan kartalarni ekranga moslaydi:</p>
  <div class="box" style="background:var(--panel); border-left:5px solid var(--accent); padding:16px;">
    <p style="font-family:monospace; font-size:1.05em; line-height:1.6;" data-ru="display: grid;<br>grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));<br>gap: 20px;" data-en="display: grid;<br>grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));<br>gap: 20px;">
      <b>display: grid;</b><br>
      <b>grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));</b><br>
      <b>gap: 20px;</b>
    </p>
  </div>
  <p style="margin-top:12px; font-size:0.95em;" data-ru="Что это делает: на мониторе будет 3 или 4 карточки в ряд, а на смартфоне они сами выстроятся в 1 столбец без медиа-запросов!" data-en="What this achieves: on monitors it renders 3-4 cards per row, collapsing to 1 column on phones without media queries!">Bu qoida monitorda 3-4 ta kartani yonma-yon qo'yadi, telefonda esa avtomatik 1 qatorga aylantiradi!</p>
</section>

<section class="slide" data-phase="Ko'rsatma|Карточка Игры|Game Card HTML" data-time="15–19">
  <div class="eyebrow"><span data-ru="Код карточки" data-en="Component Code">O'yin Kartasi KODI</span></div>
  <h2 data-ru="Анатомия Карточки Игры с Неоновым Свечением (Hover)" data-en="Anatomy of a Neon Hover Game Card Component">Neon Effektli O'yin Kartasi Arxitekturasi</h2>
  <div class="box" style="background:var(--panel); border-left:5px solid var(--green); padding:16px;">
    <p style="font-family:monospace; font-size:0.9em; line-height:1.6;" data-ru="&lt;div class=&quot;game-card&quot;&gt;<br>&nbsp;&nbsp;&lt;img src=&quot;banner.jpg&quot; alt=&quot;Cover&quot;&gt;<br>&nbsp;&nbsp;&lt;h3&gt;Aero-Runner 2150&lt;/h3&gt;<br>&nbsp;&nbsp;&lt;div class=&quot;tags&quot;&gt;&lt;span&gt;Cyberpunk&lt;/span&gt;&lt;span&gt;Parkour&lt;/span&gt;&lt;/div&gt;<br>&nbsp;&nbsp;&lt;button class=&quot;play-btn&quot;&gt;O'ynash ▶&lt;/button&gt;<br>&lt;/div&gt;" data-en="&lt;div class=&quot;game-card&quot;&gt;<br>&nbsp;&nbsp;&lt;img src=&quot;banner.jpg&quot; alt=&quot;Cover&quot;&gt;<br>&nbsp;&nbsp;&lt;h3&gt;Aero-Runner 2150&lt;/h3&gt;<br>&nbsp;&nbsp;&lt;div class=&quot;tags&quot;&gt;&lt;span&gt;Cyberpunk&lt;/span&gt;&lt;span&gt;Parkour&lt;/span&gt;&lt;/div&gt;<br>&nbsp;&nbsp;&lt;button class=&quot;play-btn&quot;&gt;Play Now ▶&lt;/button&gt;<br>&lt;/div&gt;">
      &lt;div class="game-card"&gt;<br>
      &nbsp;&nbsp;&lt;img src="banner.jpg" alt="Cover"&gt;<br>
      &nbsp;&nbsp;&lt;h3&gt;Aero-Runner 2150&lt;/h3&gt;<br>
      &nbsp;&nbsp;&lt;div class="tags"&gt;&lt;span&gt;Cyberpunk&lt;/span&gt; &lt;span&gt;3D&lt;/span&gt;&lt;/div&gt;<br>
      &nbsp;&nbsp;&lt;button class="play-btn"&gt;O'ynash ▶&lt;/button&gt;<br>
      &lt;/div&gt;
    </p>
  </div>
  <p style="margin-top:12px; font-size:0.9em; color:var(--ink-2);" data-ru="В CSS добавляем :hover { transform: translateY(-5px); box-shadow: 0 0 15px #00E5FF; } для вау-эффекта!" data-en="In CSS, attach :hover { transform: translateY(-5px); box-shadow: 0 0 15px #00E5FF; } for instant polish!">CSS da <code>:hover</code> orqali karta yuqoriga ko'tarilib, neon moviy nur sochadi!</p>
</section>

<section class="slide" data-phase="Sinov|Ошибки верстки|Layout Traps" data-time="19–23">
  <div class="eyebrow"><span data-ru="Ошибки CSS" data-en="CSS Traps">CSS Xatolari</span></div>
  <h2 data-ru="3 Ошибки Новичков, Ломающие Всю Разметку" data-en="3 Common CSS Traps That Break Web Layouts">Boshlovchilar Ko'p Qiladigan 3 Ta CSS Xatosi</h2>
  <p data-ru="Если карточки съезжают или слипаются, проверьте эти 3 правила:" data-en="If cards collapse or text wraps into ugly columns, verify these 3 fixes:">Agar sahifangiz buzilib ketsa, darhol quyidagi 3 qoidani tekshiring:</p>
  <div class="cols c3" style="display:grid; grid-template-columns:1fr 1fr 1fr; gap:12px; margin-top:12px;">
    <div class="box" style="border-top:4px solid var(--accent);">
      <h3 style="color:var(--accent);" data-ru="1. Забыли box-sizing 📦" data-en="1. Missing box-sizing 📦">1. box-sizing: border-box 📦</h3>
      <p data-ru="Без * { box-sizing: border-box; } любой padding раздувает блок, и карточки вываливаются из экрана." data-en="Without universal border-box, padding inflates card widths, pushing rows out of view.">Ushbu qoidasiz padding kartani shishirib yuboradi va ekran sig'may qoladi.</p>
    </div>
    <div class="box" style="border-top:4px solid var(--accent);">
      <h3 style="color:var(--accent);" data-ru="2. Фиксированная ширина 🔒" data-en="2. Hardcoded Pixels 🔒">2. Qotirilgan En (Fixed Width) 🔒</h3>
      <p data-ru="Если задать <code>width: 1200px;</code>, на телефоне появится уродливый горизонтальный скролл. Используйте <code>max-width: 100%;</code>." data-en="Hardcoding 1200px forces horizontal scrollbars on mobile. Use max-width & percentages."><code>width: 1200px;</code> yozsangiz telefonda gorizontal skroll paydo bo'ladi. Moslashuvchan qiling!</p>
    </div>
    <div class="box" style="border-top:4px solid var(--green);">
      <h3 style="color:var(--green);" data-ru="3. Картинки без flex-fix 🖼️" data-en="3. Distorted Images 🖼️">3. Cho'zilgan Rasmlar 🖼️</h3>
      <p data-ru="Картинки в карточках искажаются, если нет <code>object-fit: cover;</code> и <code>width: 100%;</code>." data-en="Images distort unless styled with width: 100% and object-fit: cover.">Rasmlar xunuk cho'zilib ketmasligi uchun <code>object-fit: cover;</code> yozish shart.</p>
    </div>
  </div>
</section>

<section class="slide" data-phase="Vazifa|Миссия урока|Layout Lab" data-time="23–27">
  <div class="eyebrow"><span data-ru="Практическая миссия" data-en="Hands-on Mission">Amaliy Vazifa</span></div>
  <h2 data-ru="Миссия: Сверстать Игровой Портал из 3 Карточек" data-en="Mission: Code a 3-Card Esports Game Showcase">Bugungi Vazifa: 3 Ta O'yin Kartali Veb Portalini Yig'ing</h2>
  <p data-ru="Сегодня каждый кодит стильную главную страницу для своих игр с Flexbox-шапкой и Grid-витриной:" data-en="Today, each student codes a sleek gaming showcase featuring a Flexbox navbar and Grid catalog:">Bugun har bir o'quvchi Flexbox menyu va Grid vitrinaga ega shaxsiy o'yin portalini yaratadi:</p>
  <ul class="rules">
    <li><span class="t" data-ru="<b>1. Flexbox Navbar:</b> Логотип слева, ссылки меню справа (<code>justify-content: space-between</code>)." data-en="<b>1. Flexbox Navbar:</b> Logo on left, navigation links on right via space-between."><b>1. Flexbox Menyu:</b> Chapda logotip, o'ngda tugmalar (<code>justify-content: space-between</code>).</span></li>
    <li><span class="t" data-ru="<b>2. CSS Grid Витрина:</b> Сетка из 3 карточек игр с отступами <code>gap: 20px</code>." data-en="<b>2. CSS Grid Catalog:</b> 3-card storefront layout driven by <code>gap: 20px</code>."><b>2. CSS Grid Vitrina:</b> 3 ta o'yin kartasi to'plami, <code>gap: 20px</code> oraliq masofa bilan.</span></li>
    <li><span class="t" data-ru="<b>3. Неоновый Hover:</b> При наведении мыши карточка плавно поднимается и светится." data-en="<b>3. Neon Hover FX:</b> Smooth elevation and neon glow box-shadow upon cursor hover."><b>3. Neon Hover Effekti:</b> Sichqoncha borganda karta yuqoriga ko'tariladi va neon nuri porlaydi.</span></li>
    <li><span class="t" data-ru="<b>4. Кнопка Play:</b> Яркая кнопка запуска с градиентом или неоновым контуром." data-en="<b>4. Play Button:</b> High-contrast action button styled with gradient or glowing border."><b>4. O'ynash Tugmasi:</b> Yorqin neon hoshiyali yoki gradientli harakat tugmasi.</span></li>
  </ul>
</section>

<section class="slide" data-phase="Amaliyot|Код-Спринт|Coding Sprint" data-time="27–31">
  <div class="eyebrow"><span data-ru="Инженерный спринт" data-en="Code Sprint">Jonli Amaliyot · Taymer</span></div>
  <h2 data-ru="Код-Спринт: 11 Минут на Верстку Игрового Портала" data-en="Code Sprint: 11 Minutes to Build Your Game Showcase">Kod Ustaxona: 11 Daqiqalik Jonli Veb Maket</h2>
  <div class="timer" id="timer">
    <div class="digits" id="digits">11:00</div>
    <div class="ctrls">
      <button id="tstart">Start / Stop</button>
      <button class="ghost" id="treset">Reset</button>
    </div>
  </div>
  <p style="margin-top:15px; font-size:0.95em;" data-ru="Откройте редактор кода или AI-ассистента. Соберите Navbar и Grid-сетку с неоновыми карточками!" data-en="Open your editor or AI coding tool. Assemble the Flexbox navbar and CSS Grid card catalog!">Kodingizni oching. Flexbox menyu va Grid kartalarini yozing, neon effektlarini qo'shing!</p>
</section>

<section class="slide" data-phase="Tahlil|Тест адаптивности|Responsive Audit" data-time="31–36">
  <div class="eyebrow"><span data-ru="Проверка верстки" data-en="Responsive Audit">Maket Tahlili</span></div>
  <h2 data-ru="Краш-Тест Верстки: Сжатие Экрана в DevTools (F12)" data-en="Layout Crash Test: Viewport Resizing via DevTools (F12)">Brauzerda Ekranni Qisib Ko'rish (F12 Testi)</h2>
  <p data-ru="Откройте панель разработчика (F12) и сожмите окно до размера телефона. Проверьте:" data-en="Press F12 to trigger DevTools and toggle mobile responsive view. Audit:">F12 tugmasini bosing va ekranni telefon hajmiga keltirib, quyidagi 3 holatni tekshiring:</p>
  <div class="cols c3" style="display:grid; grid-template-columns:1fr 1fr 1fr; gap:12px; margin-top:15px;">
    <div class="box">
      <h3 style="color:var(--accent);" data-ru="1. Горизонтальный скролл" data-en="1. No Horizontal Scroll">1. Skroll Paydo Bo'lmadimi?</h3>
      <p data-ru="Появилась ли нижняя полоса прокрутки? (Если да — ищите блок с жесткой шириной)." data-en="Does a horizontal scrollbar appear? If yes, hunt down fixed pixel widths.">Pastda keraksiz o'ngga-chapga suriluvchi skroll yo'qmi? Hamma narsa sig'ishi kerak.</p>
    </div>
    <div class="box">
      <h3 style="color:var(--accent);" data-ru="2. Перестроение Grid" data-en="2. Grid Reflow">2. Grid Qatorga Tushdimi?</h3>
      <p data-ru="Встали ли карточки красиво друг под другом на узком экране телефона?" data-en="Did the 3 cards gracefully stack into a clean single vertical column?">3 ta karta telefonda avtomatik ravishda chiroyli 1 qatorga aylandi-mi?</p>
    </div>
    <div class="box" style="border-left:4px solid var(--green);">
      <h3 style="color:var(--green);" data-ru="3. Неон и Клик" data-en="3. Hover Fidelity">3. Hover va Tugma</h3>
      <p data-ru="Работает ли эффект наведения и кнопки запуска игры?" data-en="Do hover animations and action buttons fire smoothly?">Sichqoncha borganda karta yaltirab, tugma bosilishga tayyormi?</p>
    </div>
  </div>
</section>

<section class="slide" data-phase="Uy vazifasi|Домашнее задание|Homework" data-time="36–40">
  <div class="eyebrow"><span data-ru="Домашний проект" data-en="Take-Home Project">Uyga Vazifa</span></div>
  <h2 data-ru="Домашнее Задание: Портал из 3 Игр + 10 Баллов" data-en="Homework: 3-Game Portal Layout & 10-Point Rubric">Uyga Vazifa: 3 Ta O'yinli Veb Portal Maketi</h2>
  <div class="hw" style="display:grid; grid-template-columns:1.4fr 1fr; gap:20px; margin-top:15px;">
    <div class="box" style="border-left:5px solid var(--accent);">
      <h3 style="color:var(--accent);" data-ru="Что нужно сделать:" data-en="Assignment Details:">Bajarilishi shart bo'lgan vazifalar:</h3>
      <ol style="margin-top:8px; padding-left:18px; line-height:1.6;">
        <li data-ru="Сверстать адаптивную веб-страницу игрового портала: Flexbox Navbar + Grid из 3 карточек игр." data-en="Code a fully responsive game portal: Flexbox navbar + CSS Grid 3-card catalog.">Flexbox menyu va 3 ta o'yin kartali CSS Grid vitrinasini to'liq kodlang.</li>
        <li data-ru="Добавить для карточек неоновый :hover эффект при наведении мыши в CSS." data-en="Implement a glowing neon :hover state elevation effect in CSS.">Har bir karta uchun sichqoncha borganda ishlovchi neon :hover effektini qo'shing.</li>
        <li data-ru="Заполнить структуру разметки и свойства CSS в рабочей тетради." data-en="Document the HTML structure and CSS grid properties in your workbook.">Varaqadagi HTML tuzilma va CSS qoidalarini daftaringizga qayd eting.</li>
      </ol>
    </div>
    <div class="box" style="background:var(--panel);">
      <h3 style="color:var(--green);" data-ru="Критерии Оценки (10 баллов):" data-en="Grading Rubric (10 Points):">Baholash Mezoni (10 ball):</h3>
      <ul style="margin-top:8px; padding-left:16px; line-height:1.6; font-size:0.9em;">
        <li data-ru="<b>3 балла:</b> Flexbox Navbar выровнен чисто без поломок." data-en="<b>3 pts:</b> Flexbox navbar aligned without visual bugs."><b>3 ball:</b> Flexbox menyu toza va xatosiz tekislangan.</li>
        <li data-ru="<b>4 балла:</b> CSS Grid автоматически перестраивается на мобильных." data-en="<b>4 pts:</b> CSS Grid responds dynamically on mobile screens."><b>4 ball:</b> CSS Grid vitrinasi telefonda qulay 1 qatorga aylanadi.</li>
        <li data-ru="<b>3 балла:</b> Неоновый :hover эффект и стилизация карточек." data-en="<b>3 pts:</b> Polished neon :hover styling and button states."><b>3 ball:</b> Neon hover va tugma dizayni to'liq sozlangan.</li>
      </ul>
    </div>
  </div>
</section>
"""

l7_notes = {
  'uz': [
    "Kirish: Steam, Epic Games yoki Roblox saytlaridagi o'yinlar vitrinasini ko'rsating. Qanday qilib barcha kartalar bir xil tekis turishini so'rang.",
    "Flexbox va Grid farqi: Flexbox 1 o'lchamli (faqat qator yoki faqat ustun), Grid esa 2 o'lchamli (jadval/matritsa) ekanini doskada chizing.",
    "Flexbox asoslari: display: flex, justify-content (space-between), align-items: center va gap xususiyatlari tushuntirilsin.",
    "Grid kuchi: repeat(auto-fit, minmax(250px, 1fr)) formulasini ko'rsating. Bu 1 qator kod mobil versiyani o'zi hal qiladi.",
    "O'yin kartasi anatomiyasi: Rasm, sarlavha, janr teglari va harakat tugmasi. :hover da ko'tarilish effekti.",
    "CSS xatolari: box-sizing: border-box yozilmasa nima bo'lishini va fixed width sababli gorizontal skroll xatosini ko'rsating.",
    "Amaliy topshiriq: O'quvchilar 3 ta o'yin kartasidan iborat kiberpank portalini kodlashadi.",
    "Jonli sprint: 11 daqiqalik taymer. O'quvchilar HTML/CSS kodini yozib, natijani brauzerda sinashadi.",
    "DevTools testi: F12 bosib ekranni kichraytirish va mobil moslashuvchanlikni tekshirish mashqi.",
    "Uy vazifasi: O'yin portalini tugatish va neon hover effektlarini qo'shish. 10 ballik baholash mezoni."
  ],
  'ru': [
    "Вступление: Покажите витрины Steam и Epic Games. Спросите, как элементы выстраиваются в идеальную сетку.",
    "Flexbox против Grid: Flexbox для одномерных цепочек (меню), Grid для двумерных сеток (каталог карточек).",
    "Свойства Flexbox: justify-content: space-between, align-items: center и отступы gap: 16px.",
    "Магия CSS Grid: Формула repeat(auto-fit, minmax(250px, 1fr)). Адаптивность без media-queries.",
    "Анатомия карточки: Изображение с object-fit: cover, теги жанров и неоновый :hover эффект при наведении.",
    "Ошибки верстки: Раздувание блоков без border-box и появление горизонтальной прокрутки.",
    "Постановка задачи: Сверстать страницу игрового портала из 3 карточек с шапкой Flexbox.",
    "Практический спринт: Таймер на 11 минут. Ученики верстают витрину в редакторе кода.",
    "Тест в DevTools: Нажатие F12, сжатие экрана до смартфона и проверка отсутствия скролла.",
    "Домашнее задание: Финализировать портал и добавить неоновые тени в CSS (10 баллов)."
  ],
  'en': [
    "Opening: Project storefronts like Steam or Roblox. Prompt students on how complex card layouts maintain alignment.",
    "Flexbox vs Grid: Establish 1D linear flow (Flexbox for navbars) versus 2D Cartesian matrices (Grid for card catalogs).",
    "Flexbox Primitives: justify-content space distribution, align-items centering, and modern gap spacing.",
    "The 1-Line Grid Miracle: repeat(auto-fit, minmax(250px, 1fr)) enabling zero-media-query responsiveness.",
    "Card Anatomy: Bounded containers, object-fit imagery, badge chips, and glowing :hover transform elevation.",
    "CSS Anti-Patterns: Neglecting universal border-box and hardcoding fixed pixel viewports.",
    "Mission Brief: Code a dark cyberpunk 3-card game portal using Flexbox header and Grid showcase.",
    "Live Code Sprint: 11-minute timer. Students build and preview live HTML/CSS structures.",
    "DevTools Viewport Audit: Press F12, drag viewport bounds to mobile width, and verify zero horizontal overflow.",
    "Homework: Complete the 3-card game portal with glowing hover states. Review the 10-point rubric."
  ]
}

p7_html = build_presentation("07-dars: Veb-Ustaxona: CSS Flexbox va Grid", l7_slides, l7_notes)
with open(os.path.join(l7_dir, "prezentatsiya.html"), "w", encoding="utf-8") as f:
    f.write(p7_html)

l7_t1 = {"uz": "Veb-Ustaxona: CSS Flexbox va Grid", "ru": "Веб-Мастерская: Flexbox и Grid", "en": "Web Workshop: Flexbox & Grid"}
l7_s1 = {"uz": "O'yin portali vitrinasini yaratish uchun 1D Flexbox va 2D CSS Grid texnologiyalarini o'rganing.", "ru": "Изучите 1D Flexbox и 2D Grid для создания современной витрины игр.", "en": "Master 1D Flexbox and 2D CSS Grid to construct an esports gaming catalog."}
l7_k1 = {"uz": "Flexbox bitta qatorni boshqaradi, CSS Grid esa butun sahifa matritsasini bir zumda tartibga soladi.", "ru": "Flexbox управляет одной линией, а CSS Grid мгновенно строит двумерную матрицу.", "en": "Flexbox controls single-axis flow, while CSS Grid effortlessly orchestrates 2D layout matrices."}

l7_p1 = """
  <section class="sec">
    <div class="h"><span class="no">01</span><h2><span lang="uz">Flexbox va Grid Farqi</span><span lang="ru">Разница Flexbox и Grid</span><span lang="en">Flexbox vs Grid</span></h2></div>
    <div class="compare">
      <div class="bad">
        <span class="lbl"><span lang="uz">CSS Flexbox (1 O'lchamli)</span><span lang="ru">CSS Flexbox (1D)</span><span lang="en">CSS Flexbox (1D)</span></span>
        <p class="pr"><span lang="uz">Faqat 1 ta qator yoki 1 ta ustun: menyu (Navbar), tugmalar qatori, piktogrammalar.</span><span lang="ru">Один ряд или колонка: шапка сайта, ряд иконок, центрирование.</span><span lang="en">Single axis (row OR column): navbars, button rows, linear icon chips.</span></p>
      </div>
      <div class="good">
        <span class="lbl"><span lang="uz">CSS Grid (2 O'lchamli)</span><span lang="ru">CSS Grid (2D)</span><span lang="en">CSS Grid (2D)</span></span>
        <p class="pr"><span lang="uz">Ham qator, ham ustunlarni bir vaqtda boshqaradi: o'yinlar vitrinasi, foto galereyalar.</span><span lang="ru">Управляет и рядами, и колонками: витрина карточек игр, фотогалереи.</span><span lang="en">Simultaneous row and column control: card catalogs, dashboard matrices.</span></p>
      </div>
    </div>
  </section>

  <section class="sec">
    <div class="h"><span class="no">02</span><h2><span lang="uz">Flexbox Asosiy Qoidalari</span><span lang="ru">Свойства Flexbox</span><span lang="en">Flexbox Rules</span></h2></div>
    <div class="trio">
      <div>
        <b><span lang="uz">justify-content ↔️</span><span lang="ru">justify-content ↔️</span><span lang="en">justify-content ↔️</span></b>
        <span class="d"><span lang="uz">Gorizontal tekislash: <code>center</code> yoki <code>space-between</code>.</span><span lang="ru">По горизонтали: по центру или по краям.</span><span lang="en">Horizontal alignment across main axis.</span></span>
      </div>
      <div>
        <b><span lang="uz">align-items ↕️</span><span lang="ru">align-items ↕️</span><span lang="en">align-items ↕️</span></b>
        <span class="d"><span lang="uz">Vertikal tekislash: <code>center</code> balandlik bo'yicha markazlashtiradi.</span><span lang="ru">По вертикали: строго по центру высоты.</span><span lang="en">Vertical centering along cross axis.</span></span>
      </div>
      <div>
        <b><span lang="uz">gap 📐</span><span lang="ru">gap 📐</span><span lang="en">gap 📐</span></b>
        <span class="d"><span lang="uz">Elementlar orasidagi masofa: <code>gap: 16px;</code>.</span><span lang="ru">Чистый отступ между блоками без margin.</span><span lang="en">Clean gutters between elements.</span></span>
      </div>
    </div>
  </section>

  <section class="sec">
    <div class="h"><span class="no">03</span><h2><span lang="uz">Avtomatik Moslashuvchan Grid KODI</span><span lang="ru">Формула CSS Grid</span><span lang="en">Auto-Fit Grid Code</span></h2></div>
    <div class="formula">
      <div class="p"><b>display: grid;</b><span class="d">Grid rejimini yoqish</span></div>
      <div class="plus">+</div>
      <div class="p"><b>grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));</b><span class="d">Avto-moslashuv</span></div>
      <div class="plus">+</div>
      <div class="p"><b>gap: 20px;</b><span class="d">Oradagi masofa</span></div>
    </div>
  </section>

  <section class="sec">
    <div class="h"><span class="no">04</span><h2><span lang="uz">Xavfli Xatolardan Himoya</span><span lang="ru">Защита от Ошибок</span><span lang="en">Layout Defense</span></h2></div>
    <div class="checklist">
      <div><b>* { box-sizing: border-box; }</b> <span lang="uz">Padding blok hajmini shishirib yubormasligi uchun majburiy qoida.</span><span lang="ru">Обязательное свойство, чтобы padding не ломал ширину.</span><span lang="en">Essential CSS reset preventing padding from expanding box widths.</span></div>
      <div><b>max-width: 100%;</b> <span lang="uz">Rasm va konteynerlar telefonda gorizontal skroll chiqarmasligi shart.</span><span lang="ru">Предотвращает появление горизонтальной полосы прокрутки.</span><span lang="en">Prevents unwanted horizontal scrollbar overflow on mobile screens.</span></div>
    </div>
  </section>
"""

l7_t2 = {"uz": "O'yin Portali Veb Arxitekturasi", "ru": "Архитектура Игрового Портала", "en": "Esports Web Showcase Blueprint"}
l7_s2 = {"uz": "O'yin kartalari kodi va sahifa tuzilishini loyihalang.", "ru": "Спроектируйте код игровых карточек и разметку страницы.", "en": "Architect game card component markup and layout styling."}

l7_p2 = """
  <section class="sec">
    <div class="h"><span class="no">05</span><h2><span lang="uz">O'yin Kartasi HTML Strukturasi</span><span lang="ru">HTML Карточки</span><span lang="en">Game Card HTML Blueprint</span></h2></div>
    <div style="border:1px solid var(--rule); background:var(--panel); padding:8px; font-family:monospace; font-size:8pt; line-height:1.4;">
      &lt;div class="game-card"&gt;<br>
      &nbsp;&nbsp;&lt;img src="cover.jpg" alt="Game Banner" class="card-img"&gt;<br>
      &nbsp;&nbsp;&lt;h3&gt;O'yin Nomi: ___________________________&lt;/h3&gt;<br>
      &nbsp;&nbsp;&lt;p&gt;Tavsif: ___________________________________&lt;/p&gt;<br>
      &nbsp;&nbsp;&lt;button class="btn-play"&gt;Play Now ▶&lt;/button&gt;<br>
      &lt;/div&gt;
    </div>
  </section>

  <section class="sec">
    <div class="h"><span class="no">06</span><h2><span lang="uz">Mening Neon :hover CSS Qoidam</span><span lang="ru">CSS Эффект Hover</span><span lang="en">Neon :hover CSS Rule</span></h2></div>
    <div style="border:1px solid var(--rule); background:var(--panel); padding:8px; font-family:monospace; font-size:8pt; line-height:1.4;">
      .game-card:hover {<br>
      &nbsp;&nbsp;transform: translateY(-5px);<br>
      &nbsp;&nbsp;box-shadow: 0 0 15px #00E5FF;<br>
      &nbsp;&nbsp;border-color: #00E5FF;<br>
      }
    </div>
  </section>

  <section class="sec">
    <div class="h"><span class="no">07</span><h2><span lang="uz">3 Ta O'yin Ro'yxati (Vitrina)</span><span lang="ru">Список 3 Игр</span><span lang="en">3-Game Showcase Inventory</span></h2></div>
    <table class="gridtable" style="width:100%; border-collapse:collapse; font-size:8.5pt; text-align:left;">
      <tr style="background:var(--panel-2);">
        <th style="padding:4px; border:1px solid var(--rule);">#</th>
        <th style="padding:4px; border:1px solid var(--rule);">O'yin Nomi</th>
        <th style="padding:4px; border:1px solid var(--rule);">Janr Teglari</th>
        <th style="padding:4px; border:1px solid var(--rule);">Tugma Rangi</th>
      </tr>
      <tr>
        <td style="padding:4px; border:1px solid var(--rule);">1</td>
        <td style="padding:4px; border:1px solid var(--rule);">Aero-Runner 2150</td>
        <td style="padding:4px; border:1px solid var(--rule);">Cyberpunk / 3D Parkour</td>
        <td style="padding:4px; border:1px solid var(--rule);">Neon Moviy (#00E5FF)</td>
      </tr>
      <tr>
        <td style="padding:4px; border:1px solid var(--rule);">2</td>
        <td style="padding:4px; border:1px solid var(--rule);">_______________________</td>
        <td style="padding:4px; border:1px solid var(--rule);">_______________________</td>
        <td style="padding:4px; border:1px solid var(--rule);">_______________________</td>
      </tr>
      <tr>
        <td style="padding:4px; border:1px solid var(--rule);">3</td>
        <td style="padding:4px; border:1px solid var(--rule);">_______________________</td>
        <td style="padding:4px; border:1px solid var(--rule);">_______________________</td>
        <td style="padding:4px; border:1px solid var(--rule);">_______________________</td>
      </tr>
    </table>
  </section>

  <section class="sec">
    <div class="h"><span class="no">08</span><h2><span lang="uz">DevTools (F12) Nazorat Sinovi</span><span lang="ru">Проверка в DevTools</span><span lang="en">DevTools Responsive Audit</span></h2></div>
    <div style="display:flex; flex-direction:column; gap:4px; font-size:8.5pt;">
      <label><input type="checkbox"> Ekranni toraytirganda pastki gorizontal skroll paydo bo'lmadi.</label>
      <label><input type="checkbox"> Kartalar mobil hajmda avtomatik ravishda 1 ustunga tizildi.</label>
      <label><input type="checkbox"> Sichqoncha borganda neon hover animatsiyasi silliq ishladi.</label>
    </div>
  </section>
"""

l7_hw = """
  <p><b>1. Veb Sahifa KODI:</b> Flexbox Navbar va 3 ta o'yin kartali CSS Grid vitrinasini to'liq kodlang.</p>
  <p><b>2. Neon :hover:</b> Kartalarga sichqoncha borganda ko'tarilish va nur sochish effektini bering.</p>
  <p><b>3. Varaqani To'ldirish:</b> HTML va CSS qoidalarini varaqadagi barcha jadvallarga yozib keling.</p>
"""

l7_crit = """
  <div class="r"><span>Flexbox Navbar xatosiz tekislangan</span><b>3</b></div>
  <div class="r"><span>CSS Grid mobil ekranga moslashadi</span><b>4</b></div>
  <div class="r"><span>Neon :hover effekti va kartalar stili tayyor</span><b>3</b></div>
"""

l7_nxt = {'uz': "Interaktivlik Sehri: JS Hodisalar va Tugmalar", 'ru': "Магия Интерактивности: JS События и Кнопки", 'en': "Interactive Magic: JS Events & Buttons"}

ws7_html = build_worksheet('7-8-sinf', 2, 7, l7_t1, l7_s1, l7_k1, l7_p1, l7_t2, l7_s2, l7_p2, l7_hw, l7_crit, l7_nxt)
with open(os.path.join(l7_dir, 'varaqa.html'), 'w', encoding='utf-8') as f:
    f.write(ws7_html)

print("7-8 Week 2 Lesson 7 generated successfully!")
