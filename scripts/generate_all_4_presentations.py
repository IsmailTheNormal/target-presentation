#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Full generator for 4 modern minimalist presentations:
1. 9-sinf 26-dars (MVC Backend, SQLite, Foreign Keys)
2. 10-11-sinf 31-dars (Penetration Testing, Ethical Hacking, Scanner)
3. 7-8-sinf 29-dars (GPS Navigation, Graphs, Dijkstra, Haversine)
4. 5-6-sinf 21-dars (Digital Footprint, Privacy, EXIF)
"""

import os
import json
import html

# Load CSS from 28-dars
with open("classes/9-sinf/8-hafta/28-dars-fullstack-xavfsiz-servis-oraliq-nazorat/prezentatsiya.html", "r", encoding="utf-8") as f:
    t28 = f.read()

css_chunk = t28[t28.find("<style>"):t28.find("</style>") + 8]

def get_floating_elements(cohort_tag):
    return f"""
<a href="/index.html" class="floating-brand" title="Bosh sahifa / Home" data-title-ru="Главная страница / Home" data-title-en="Home Page">
  <div class="logo-box">
    <img src="/assets/target-logo.png" alt="Target Logo">
  </div>
  <span class="name">TARGET</span>
  <span class="tag">{cohort_tag}</span>
</a>

<!-- Floating Top-Right Controls Dock -->
<div class="floating-dock">
  <button class="dock-btn lang-btn" data-lang="uz" onclick="setLang('uz')" title="O'zbek tili" data-title-ru="Узбекский язык" data-title-en="Uzbek language">UZ</button>
  <button class="dock-btn lang-btn" data-lang="ru" onclick="setLang('ru')" title="Rus tili" data-title-ru="Русский язык" data-title-en="Russian language">RU</button>
  <button class="dock-btn lang-btn" data-lang="en" onclick="setLang('en')" title="Ingliz tili" data-title-ru="Английский язык" data-title-en="English language">EN</button>
  <button class="dock-btn" onclick="toggleTheme()" title="Mavzuni almashtirish" data-title-ru="Переключить тему" data-title-en="Toggle Theme">🌓</button>
  <button class="dock-btn" onclick="toggleNotes()" title="O'qituvchi izohlari (N)" data-title-ru="Заметки преподавателя (N)" data-title-en="Teacher Notes (N)">📝</button>
  <button class="dock-btn" onclick="toggleHelp()" title="Klavishlar yordami (?)" data-title-ru="Справка клавиш (?)" data-title-en="Keyboard Help (?)">⌨️</button>
</div>

<!-- Floating Slide Counter -->
<div class="floating-counter">
  <span class="curr" id="slide-curr">01</span> / <span id="slide-total">12</span>
</div>

<!-- Floating Phase Badge -->
<div class="floating-phase" id="slide-phase" data-phase="KIRISH|ВВЕДЕНИЕ|INTRO">
  KIRISH
</div>
"""

def get_modals():
    return """
<!-- Teacher Notes Modal -->
<div class="notes-modal" id="notesModal" onclick="if(event.target===this)toggleNotes()">
  <div class="modal-box">
    <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px;">
      <h3 style="margin:0;" data-ru="Заметки преподавателя" data-en="Teacher Notes">O'qituvchi izohlari</h3>
      <span style="font-family:'JetBrains Mono',monospace; font-size:12px; color:var(--ink-2); cursor:pointer;" onclick="toggleNotes()">[ESC]</span>
    </div>
    <div class="notes-body" id="notesContent">...</div>
  </div>
</div>

<!-- Keyboard Help Modal -->
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

def get_js(notes_dict):
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

  // Update phase badge
  var act = slides[currentSlide];
  var phaseData = act.getAttribute("data-phase") || "DARS|УРОК|LESSON";
  var parts = phaseData.split("|");
  var pText = parts[0];
  if (currentLang === "ru" && parts[1]) pText = parts[1];
  if (currentLang === "en" && parts[2]) pText = parts[2];
  document.getElementById("slide-phase").textContent = pText;

  // Update notes triplet
  var notesArr = NOTES[currentLang] || NOTES["uz"] || [];
  var note = notesArr[currentSlide] || ["", "", ""];
  var titleLabel = currentLang === "ru" ? "Слайд" : (currentLang === "en" ? "Slide" : "Slayd");
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

  // Update in-place translations
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
    var langs = ["uz", "ru", "en"];
    var nextIdx = (langs.indexOf(currentLang) + 1) % langs.length;
    setLang(langs[nextIdx]);
  }} else if (e.key === "t" || e.key === "T") {{
    toggleTheme();
  }} else if (e.key === "n" || e.key === "N") {{
    toggleNotes();
  }} else if (e.key === "?" || e.key === "/") {{
    toggleHelp();
  }} else if (e.key === "Escape") {{
    document.getElementById("notesModal").classList.remove("active");
    document.getElementById("helpModal").classList.remove("active");
  }}
}});

document.addEventListener("DOMContentLoaded", function() {{
  var savedTheme = "dark";
  try {{ savedTheme = localStorage.getItem("target_theme") || "dark"; }} catch(e) {{}}
  document.documentElement.setAttribute("data-theme", savedTheme);

  var savedLang = "uz";
  try {{ savedLang = localStorage.getItem("target_lang") || "uz"; }} catch(e) {{}}
  setLang(savedLang);

  updateSlideView();
}});
</script>
"""

# Let's generate Lesson 26 (9-sinf)
def build_lesson_26():
    folder = "classes/9-sinf/6-hafta/26-dars-mvc-backend-va-relyatsion-baza"
    cohort_tag = "9-SINF · WEEK 6"
    title = {
      "uz": "9-Sinf · 26-Dars: MVC Backend Asoslari, Relyatsion SQLite va REST API",
      "ru": "9-Класс · Урок 26: Архитектура MVC, Реляционная SQLite и REST API",
      "en": "Grade 9 · Lesson 26: MVC Backend Architecture, Relational SQLite & REST API"
    }

    slides_html = """
<div class="stage">

  <!-- SLIDE 1: TITUL -->
  <section class="slide active" data-phase="KIRISH|ВВЕДЕНИЕ|INTRO" data-time="3 min">
    <div class="eyebrow" data-ru="9-КЛАСС · 6-Я НЕДЕЛЯ · УРОК 26" data-en="GRADE 9 · WEEK 6 · LESSON 26">
      9-SINF · 6-HAFTA · 26-DARS
    </div>
    <h1 class="hero-title" data-ru="Архитектура MVC и Реляционная SQLite" data-en="MVC Backend Architecture &amp; Relational SQLite">
      MVC Backend Asoslari va Relyatsion SQLite
    </h1>
    <p class="lede" data-ru="Изучение профессионального разделения обязанностей: слои Model, View, Controller, связи Foreign Key и проектирование надежного REST API." data-en="Mastering industry-grade separation of concerns: Model, View, Controller layers, Foreign Key constraints, and robust REST API design.">
      Professional backend muhandisligi: kodni Model, View, Controller qatlamlariga ajratish, SQLite relyatsion jadvallari va mustahkam REST API qurish.
    </p>
    <ul class="big-list">
      <li><span class="num">01</span> <span data-ru="<strong>Архитектурная чистота:</strong> переход от хаотичного монолита server.js к модульной структуре MVC." data-en="<strong>Architectural Hygiene:</strong> transitioning from chaotic server.js spaghetti to modular MVC layers."><strong>Arxitektura intizomi:</strong> tartibsiz server.js monolitidan professional MVC modul qatlamlariga o'tish.</span></li>
      <li><span class="num">02</span> <span data-ru="<strong>Реляционная база данных:</strong> таблицы users, products, orders и связи 1-ко-многим через Foreign Key." data-en="<strong>Relational SQLite:</strong> connecting users, products, and orders via 1-to-Many Foreign Keys."><strong>Relyatsion baza:</strong> users, products va orders jadvallari o'rtasida Foreign Key orqali 1-to-Many aloqa o'rnatish.</span></li>
    </ul>
  </section>

  <!-- SLIDE 2: THE PROBLEM (SPAGHETTI CODE) -->
  <section class="slide" data-phase="MUAMMO|ПРОБЛЕМА|THE PROBLEM" data-time="3 min">
    <div class="eyebrow" data-ru="АНТИ-ПАТТЕРН SPAGHETTI" data-en="SPAGHETTI MONOLITH PROBLEM">
      ARXITEKTURA MUAMMOSI
    </div>
    <h2 class="section-title" data-ru="Почему 10,000 строк в server.js убивают проект?" data-en="Why 10,000 Lines in server.js Break Projects?">
      Nega bitta server.js fayliga barcha kodni yozish loyihani barbod qiladi?
    </h2>
    <p class="statement" data-ru="Представьте ресторан, где один человек одновременно встречает гостей, жарит мясо, моет посуду и ведет бухгалтерию. Он захлебнется за полчаса. В коде то же самое: маршрутизация, валидация и SQL должны быть строго разделены." data-en="Imagine a restaurant where one cook greets patrons, prepares steaks, washes plates, and files tax returns simultaneously. It collapses in 30 minutes. Code requires identical segregation: routing, validation, and SQL must reside in distinct layers.">
      Tasavvur qiling, restoranda oshpazning o'zi eshikda mehmon kutib olsa, o'zi buyurtma olsa, ovqat pishirsa va idish yuvsa nima bo'ladi? Restoran 30 daqiqada to'xtaydi. Backendda ham xuddi shunday: router, controller va SQL qat'iy ajratilishi shart.
    </p>
    <div class="text-cols">
      <div class="col-item">
        <span class="col-num">01</span>
        <h3 class="col-title" data-ru="Хаос в коде" data-en="Spaghetti Logic">Chalkashlik</h3>
        <p class="col-desc" data-ru="Бизнес-логика перемешана с SQL-запросами, изменения ломают соседние модули." data-en="Business rules intermingle with SQL queries; modifying one feature breaks another.">Biznes mantiq SQL so'rovlar bilan aralashib ketadi, bitta o'zgarish boshqa joyni buzadi.</p>
      </div>
      <div class="col-item">
        <span class="col-num">02</span>
        <h3 class="col-title" data-ru="Трудность тестов" data-en="Untestable Code">Testlab bo'lmaydi</h3>
        <p class="col-desc" data-ru="Невозможно протестировать обработку платежа отдельно от HTTP-сервера." data-en="Impossible to test database interactions isolated from the HTTP layer.">HTTP so'rovni ma'lumotlar bazasidan ajratib alohida testlab bo'lmaydi.</p>
      </div>
      <div class="col-item">
        <span class="col-num">03</span>
        <h3 class="col-title" data-ru="Уязвимость" data-en="Vulnerability Risk">Kiber-zaiflik</h3>
        <p class="col-desc" data-ru="Легко пропустить валидацию и получить инъекцию в базу данных." data-en="Validation lapses quickly open avenues for SQL injection flaws.">Validatsiya qolib ketishi sababli bazaga xom parametrlar o'tib ketadi.</p>
      </div>
    </div>
  </section>

  <!-- SLIDE 3: MVC TRIAD -->
  <section class="slide" data-phase="ARXITEKTURA|АРХИТЕКТУРА|ARCHITECTURE" data-time="4 min">
    <div class="eyebrow" data-ru="СТАНДАРТ ИНДУСТРИИ" data-en="INDUSTRY STANDARD">
      MVC UCHLIGI
    </div>
    <h2 class="section-title" data-ru="Model · View · Controller: Четкие обязанности" data-en="Model · View · Controller: Clean Separation">
      Model · View · Controller: Mas'uliyatlarning aniq taqsimoti
    </h2>
    <p class="lede" data-ru="Каждый слой решает строго одну задачу. Никто не вмешивается в чужую зону ответственности:" data-en="Each layer executes precisely one mission without crossing operational boundaries:">
      Har bir qatlam faqat o'z ishiga javob beradi va boshqa qatlamning vazifasiga aralashmaydi:
    </p>
    <div class="text-cols">
      <div class="col-item">
        <span class="col-num">MODEL</span>
        <h3 class="col-title" data-ru="Слой данных" data-en="Data Layer">Baza Qatlami</h3>
        <p class="col-desc" data-ru="Работает с SQLite: SQL-запросы, таблицы, валидация схемы. Не знает про HTTP!" data-en="Interfaces with SQLite: SQL queries, table schemas, data integrity. Completely agnostic of HTTP!">Faqat SQLite bilan ishlaydi: SQL so'rovlar, jadvallar sxemasi. HTTP haqida hech narsa bilmaydi!</p>
      </div>
      <div class="col-item">
        <span class="col-num">CONTROLLER</span>
        <h3 class="col-title" data-ru="Бизнес-логика" data-en="Business Logic">Boshqaruv Markazi</h3>
        <p class="col-desc" data-ru="Принимает req, валидирует данные (quantity > 0), обращается к Model, отдает статус." data-en="Receives req, validates input (quantity > 0), calls Model, returns HTTP status.">HTTP so'rovni qabul qiladi, miqdorni tekshiradi, Modelga topshiradi va status qaytaradi.</p>
      </div>
      <div class="col-item">
        <span class="col-num">VIEW</span>
        <h3 class="col-title" data-ru="Представление" data-en="Presentation">Taqdimot Qatlami</h3>
        <p class="col-desc" data-ru="Клиентский интерфейс: чистый JSON для API или Web Dashboard для пользователя." data-en="Client presentation: structured JSON for API clients or reactive Web Dashboard.">Foydalanuvchiga ko'rinadigan qism: toza JSON formati yoki veb-dashboard.</p>
      </div>
    </div>
  </section>

  <!-- SLIDE 4: RELATIONAL DATABASE & FOREIGN KEYS -->
  <section class="slide" data-phase="BAZA|БАЗА ДАННЫХ|DATABASE" data-time="4 min">
    <div class="eyebrow" data-ru="РЕЛЯЦИОННЫЕ СВЯЗИ" data-en="RELATIONAL ASSOCIATIONS">
      RELYATSION BAZA VA FOREIGN KEY
    </div>
    <h2 class="section-title" data-ru="Как связать заказы, пользователей и товары?" data-en="Linking Orders, Users, and Products">
      Buyurtmalar, foydalanuvchilar va tovarlarni qanday bog'laymiz?
    </h2>
    <p class="lede" data-ru="В реляционной базе данные не дублируются. Таблица orders хранит только ID покупателя и товара, ссылаясь на родительские таблицы через Foreign Key:" data-en="Relational schemas eliminate redundant duplication. The orders table stores only foreign IDs referencing primary tables:">
      Relyatsion bazada ma'lumotlar takrorlanmaydi. `orders` jadvali faqat xaridor va tovarning ID raqamini saqlaydi va Foreign Key orqali ularga bog'lanadi:
    </p>
    <pre class="code-block">CREATE TABLE orders (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  user_id INTEGER NOT NULL,
  product_id INTEGER NOT NULL,
  quantity INTEGER NOT NULL CHECK (quantity &gt; 0),
  total_price INTEGER NOT NULL,
  FOREIGN KEY (user_id) REFERENCES users(id),
  FOREIGN KEY (product_id) REFERENCES products(id)
);</pre>
    <ul class="big-list">
      <li><span class="num">01</span> <span data-ru="<strong>Ссылочная целостность:</strong> база не позволит создать заказ для несуществующего user_id." data-en="<strong>Referential Integrity:</strong> database rejects orders referencing nonexistent user_ids."><strong>Yaxlitlik kafolati:</strong> baza mavjud bo'lmagan user_id uchun buyurtma yaratishga yo'l qo'ymaydi.</span></li>
      <li><span class="num">02</span> <span data-ru="<strong>Каскадность:</strong> при удалении пользователя можно автоматически очистить его заказы." data-en="<strong>Cascading Rules:</strong> deleting a user profile can automatically purge associated order rows."><strong>Kaskad o'chirish:</strong> foydalanuvchi o'chirilganda uning barcha buyurtmalarini avtomatik tozalash mumkin.</span></li>
    </ul>
  </section>

  <!-- SLIDE 5: REST API & HTTP STATUS CODES -->
  <section class="slide" data-phase="REST API|REST API|REST API" data-time="4 min">
    <div class="eyebrow" data-ru="ПРОТОКОЛ ОБЩЕНИЯ" data-en="COMMUNICATION CONTRACT">
      REST API VA HTTP STATUS KODLARI
    </div>
    <h2 class="section-title" data-ru="Говорим на одном языке: 200, 201 и 400" data-en="Speaking the Same Language: 200, 201 &amp; 400">
      To'g'ri HTTP status kodlari bilan javob qaytarish
    </h2>
    <p class="lede" data-ru="Нельзя возвращать 200 OK, если произошла ошибка! Клиент должен точно знать результат операции:" data-en="Never return 200 OK on client errors! API clients rely on standard status codes:">
      Xatolik yuz berganda hech qachon 200 OK qaytarmang! Mijoz operatsiya natijasini status koddan bilishi shart:
    </p>
    <div class="text-cols">
      <div class="col-item">
        <span class="col-num">200 OK</span>
        <h3 class="col-title" data-ru="Чтение данных" data-en="Successful Read">Muvaffaqiyatli</h3>
        <p class="col-desc" data-ru="GET /api/orders — список успешно прочитан из базы и возвращен клиенту." data-en="GET /api/orders — records successfully queried and returned.">GET /api/orders — buyurtmalar ro'yxati bazadan muvaffaqiyatli o'qildi.</p>
      </div>
      <div class="col-item">
        <span class="col-num">201 CREATED</span>
        <h3 class="col-title" data-ru="Запись создана" data-en="Resource Created">Yaratildi</h3>
        <p class="col-desc" data-ru="POST /api/orders — новый заказ успешно валидирован и вставлен в SQLite." data-en="POST /api/orders — new entity validated and inserted into SQLite.">POST /api/orders — yangi buyurtma tekshirildi va bazaga muvaffaqiyatli yozildi.</p>
      </div>
      <div class="col-item">
        <span class="col-num">400 BAD REQ</span>
        <h3 class="col-title" data-ru="Ошибка клиента" data-en="Client Validation">Mijoz Xatosi</h3>
        <p class="col-desc" data-ru="Клиент прислал отрицательное количество (quantity <= 0) или забыл указать user_id." data-en="Client submitted invalid quantity or omitted mandatory foreign IDs.">Mijoz manfiy miqdor (quantity <= 0) yubordi yoki user_id ni unutdi.</p>
      </div>
    </div>
  </section>

  <!-- SLIDE 6: CONTROLLER IMPLEMENTATION -->
  <section class="slide" data-phase="KOD|КОД|CODE" data-time="4 min">
    <div class="eyebrow" data-ru="КОНТРОЛЛЕР EXPRESS" data-en="EXPRESS CONTROLLER">
      CONTROLLER KODI VA VALIDATSIYA
    </div>
    <h2 class="section-title" data-ru="Как выглядит правильный метод orderController.js" data-en="Production Pattern for orderController.js">
      Professional orderController.js qanday yoziladi?
    </h2>
    <pre class="code-block">// controllers/orderController.js
exports.createOrder = (req, res) =&gt; {
  const { user_id, product_id, quantity } = req.body;

  // 1. Kiruvchi ma'lumotlarni tekshirish (Validation)
  if (!user_id || !product_id || !quantity || quantity &lt;= 0) {
    return res.status(400).json({ error: "Foydalanuvchi, tovar yoki miqdor xato!" });
  }

  // 2. Model orqali bazaga murojaat
  OrderModel.create({ user_id, product_id, quantity }, (err, order) =&gt; {
    if (err) return res.status(500).json({ error: "Baza xatosi yuz berdi" });
    // 3. Muvaffaqiyatli javob: 201 Created
    res.status(201).json({ message: "Buyurtma saqlandi", order });
  });
};</pre>
  </section>

  <!-- SLIDE 7: SQL INNER JOIN -->
  <section class="slide" data-phase="SQL JOIN|SQL JOIN|SQL JOIN" data-time="4 min">
    <div class="eyebrow" data-ru="СБОРКА ОТЧЕТОВ" data-en="RELATIONAL COMPILATION">
      SQL INNER JOIN SEHRI
    </div>
    <h2 class="section-title" data-ru="Объединяем 3 таблицы в один красивый JSON" data-en="Joining 3 Tables into a Unified JSON">
      3 ta jadvalni yagona hisobotga birlashtirish
    </h2>
    <p class="lede" data-ru="Клиенту в чеке нужны имена покупателей и названия товаров, а не сухие цифры user_id=4. INNER JOIN связывает таблицы на лету:" data-en="Receipts require customer names and product titles rather than raw IDs. INNER JOIN compiles related rows instantaneously:">
      Xaridorga quruq `user_id: 2` emas, balki ismi va tovar nomi kerak. `INNER JOIN` bog'langan jadvallarni bitta so'rovda birlashtiradi:
    </p>
    <pre class="code-block">SELECT 
  orders.id AS order_id,
  users.name AS customer_name,
  products.title AS product_name,
  orders.quantity,
  orders.total_price
FROM orders
INNER JOIN users ON orders.user_id = users.id
INNER JOIN products ON orders.product_id = products.id
ORDER BY orders.id DESC;</pre>
  </section>

  <!-- SLIDE 8: INTERACTIVE STUDIO -->
  <section class="slide" data-phase="STUDIO|СТУДИЯ|STUDIO" data-time="4 min">
    <div class="eyebrow" data-ru="ИНТЕРАКТИВНАЯ ЛАБОРАТОРИЯ" data-en="INTERACTIVE WORKBENCH">
      MVC &amp; SQLITE STUDIO
    </div>
    <h2 class="section-title" data-ru="Визуальный тренажер: Поток запросов и база" data-en="Visual Simulator: Request Lifecycle &amp; DB">
      Vizual simulyator: So'rov oqimi va jonli SQLite jadvali
    </h2>
    <p class="lede" data-ru="В папке studio/index.html открывается интерактивная среда: вы отправляете REST-запросы и видите анимацию перехода Client ➔ Router ➔ Controller ➔ SQLite." data-en="Launch studio/index.html to explore live visual request flow: Client ➔ Router ➔ Controller ➔ SQLite:">
      `studio/index.html` laboratoriyasida siz yuborgan har bir so'rov Client ➔ Router ➔ Controller ➔ Model ➔ SQLite zanjiri bo'ylab jonli animatsiyada ko'rsatiladi.
    </p>
    <ul class="big-list">
      <li><span class="num">01</span> <span data-ru="<strong>Схема связей:</strong> визуальный инспектор внешних ключей и таблиц." data-en="<strong>Schema Inspector:</strong> interactive visualization of foreign keys and relational schema."><strong>Sxema inspektori:</strong> jadvallar va tashqi kalitlar (Foreign Keys) o'zaro qanday bog'langanini ko'rish.</span></li>
      <li><span class="num">02</span> <span data-ru="<strong>Консоль REST API:</strong> отправка POST, GET, DELETE и отслеживание статус-кодов в реальном времени." data-en="<strong>REST API Console:</strong> dispatching POST, GET, DELETE payloads with real-time status telemetry."><strong>REST API konsoli:</strong> POST, GET, DELETE so'rovlarini yuborish va status kodlarni kuzatish.</span></li>
    </ul>
  </section>

  <!-- SLIDE 9: QUIZ & FIX -->
  <section class="slide" data-phase="TEST|ТЕСТ|QUIZ &amp; FIX" data-time="5 min">
    <div class="eyebrow" data-ru="ИНТЕРАКТИВНЫЙ ТЕСТ" data-en="INTERACTIVE TEST &amp; FIX">
      JONLI KIBER-TEST VA YECHIM (FIX)
    </div>
    <h2 class="section-title" data-ru="Тест: Что произойдет, если передать quantity = -5?" data-en="Quiz: What Happens if Client Sends quantity = -5?">
      Sinov: Agar xaridor quantity = -5 yuborsa nima bo'ladi?
    </h2>
    <p class="lede" data-ru="Посмотрите на фрагмент контроллера и определите, какой ответ получит клиент:" data-en="Inspect this controller logic and determine the client HTTP response:">
      Quyidagi kodni tekshiring va controller mijozga qanday javob qaytarishini ayting:
    </p>
    <pre class="code-block">if (!quantity || quantity &lt;= 0) {
  return res.status(???).json({ error: "Noto'g'ri miqdor" });
}</pre>
    <div class="quiz-box">
      <div class="quiz-option" onclick="checkQuiz(this, false)">
        <span class="num">A</span> <span data-ru="200 OK — сервер автоматически исправит число на положительное." data-en="200 OK — server automatically converts the negative integer.">200 OK — server sonni avtomatik musbatga aylantiradi.</span>
      </div>
      <div class="quiz-option" onclick="checkQuiz(this, true)">
        <span class="num">B</span> <span data-ru="400 Bad Request — валидация отклонит неверные входные данные." data-en="400 Bad Request — input validation promptly rejects the payload.">400 Bad Request — validatsiya noto'g'ri ma'lumotni rad etadi.</span>
      </div>
      <div class="quiz-option" onclick="checkQuiz(this, false)">
        <span class="num">C</span> <span data-ru="500 Internal Server Error — сервер упадет из-за сбоя." data-en="500 Internal Server Error — server crashes due to fatal error.">500 Internal Server Error — server xatodan qulab tushadi.</span>
      </div>
    </div>
    <div class="test-actions">
      <button class="test-btn" onclick="toggleTestFix()" data-ru="Показать исправление (Fix)" data-en="Show Solution (Fix)">Yechimni ko'rish (Fix)</button>
    </div>
    <div class="fix-reveal" id="testFixBox">
      // MUHANDISLIK YECHIMI (FIX):<br>
      // Kiruvchi parametrlar xato bo'lganda HAR DOIM 400 Bad Request qaytariladi:<br>
      return res.status(400).json({ error: "Miqdor musbat butun son bo'lishi shart!" });
    </div>
  </section>

  <!-- SLIDE 10: MISSIONS -->
  <section class="slide" data-phase="AMALIYOT|ПРАКТИКА|MISSIONS" data-time="8 min">
    <div class="eyebrow" data-ru="4 ИНЖЕНЕРНЫХ КВЕСТА" data-en="4 ENGINEERING MISSIONS">
      AMALIYOT: 4 TA MUHANDISLIK KVESTI
    </div>
    <h2 class="section-title" data-ru="Практика в Studio: Запусти свой Backend" data-en="Studio Practice: Run Your Backend">
      Studioda amaliyot: O'z backend tizimingni sinovdan o'tkaz
    </h2>
    <div class="text-cols">
      <div class="col-item">
        <span class="col-num">KVEST 01</span>
        <h3 class="col-title" data-ru="Создание заказа" data-en="Create Order">Buyurtma berish</h3>
        <p class="col-desc" data-ru="Отправьте POST /api/orders с валидными user_id и quantity. Получите статус 201." data-en="Dispatch valid POST /api/orders and receive 201 Created.">POST /api/orders so'rovini yuboring va 201 Created javobini oling.</p>
      </div>
      <div class="col-item">
        <span class="col-num">KVEST 02</span>
        <h3 class="col-title" data-ru="Отчет с JOIN" data-en="JOIN Report">JOIN hisoboti</h3>
        <p class="col-desc" data-ru="Выполните GET /api/orders/details и проверьте имена покупателей в таблице." data-en="Run GET /api/orders/details and inspect customer names in table.">GET /api/orders/details so'rovini yuboring va xaridor nomlarini tekshiring.</p>
      </div>
      <div class="col-item">
        <span class="col-num">KVEST 03</span>
        <h3 class="col-title" data-ru="Отлов 400 ошибки" data-en="Catch 400 Bad Req">400 Xatoni ushlash</h3>
        <p class="col-desc" data-ru="Передайте quantity = 0 и убедитесь, что контроллер возвращает 400 Bad Request." data-en="Submit quantity = 0 and verify controller responds with 400.">quantity = 0 yuboring va controller 400 Bad Request qaytarganini ko'ring.</p>
      </div>
    </div>
  </section>

  <!-- SLIDE 11: RUBRIC -->
  <section class="slide" data-phase="BAHOLASH|ОЦЕНКА|RUBRIC" data-time="3 min">
    <div class="eyebrow" data-ru="10-БАЛЛЬНЫЙ СТАНДАРТ" data-en="10-POINT STANDARD">
      RASMIY BAHOLASH MEZONI
    </div>
    <h2 class="section-title" data-ru="Критерии оценки за урок (10 баллов)" data-en="Lesson Evaluation Rubric (10 Points)">
      10 ballik rasmiy baholash mezoni
    </h2>
    <ul class="big-list">
      <li><span class="num">01</span> <span data-ru="<strong>MVC Архитектура (2.5 балла):</strong> четкое разделение ролей Model, View и Controller." data-en="<strong>MVC Architecture (2.5 pts):</strong> strict separation of concerns across Model, View, Controller."><strong>MVC Arxitekturasi (2.5 ball):</strong> Model, View va Controller rollarini to'g'ri ajrata olish.</span></li>
      <li><span class="num">02</span> <span data-ru="<strong>Реляционная база (2.5 балла):</strong> создание Foreign Key связей в SQLite и понимание целостности." data-en="<strong>Relational Schema (2.5 pts):</strong> defining SQLite Foreign Key constraints and schema integrity."><strong>Relyatsion Baza (2.5 ball):</strong> SQLite bazasida Foreign Key bog'lanishlarini to'g'ri qurish.</span></li>
      <li><span class="num">03</span> <span data-ru="<strong>REST API Валидация (2.5 балла):</strong> корректная обработка статусов 201 Created и 400 Bad Request." data-en="<strong>REST Validation (2.5 pts):</strong> handling status codes 201 Created vs 400 Bad Request reliably."><strong>REST API Validatsiyasi (2.5 ball):</strong> 201 Created va 400 Bad Request statuslarini to'g'ri boshqarish.</span></li>
      <li><span class="num">04</span> <span data-ru="<strong>SQL JOIN и Studio (2.5 балла):</strong> выполнение квестов в Studio и составление отчетов." data-en="<strong>SQL JOIN &amp; Studio (2.5 pts):</strong> completing Studio workbench quests and multi-table queries."><strong>SQL JOIN va Studio (2.5 ball):</strong> Studiodagi kvestlarni to'liq bajarib hisobot olish.</span></li>
    </ul>
  </section>

  <!-- SLIDE 12: SUMMARY -->
  <section class="slide" data-phase="XULOSA|ИТОГИ|SUMMARY" data-time="2 min">
    <div class="eyebrow" data-ru="ИТОГИ И МОСТ" data-en="SUMMARY &amp; NEXT STEP">
      XULOSA VA KEYINGI DARS
    </div>
    <h1 class="hero-title" data-ru="Вы — Junior Backend Архитекторы!" data-en="You are Junior Backend Architects!">
      Siz — Junior Backend Arxitektorsiz!
    </h1>
    <p class="lede" data-ru="Вы научились строить масштабируемый бэкенд. Но открытый API уязвим: в следующий раз мы изучим атаки XSS, CSRF и способы санитизации входящих данных!" data-en="You have engineered scalable backend foundations. Next, we safeguard our APIs against XSS, CSRF, and weaponized payloads!">
      Siz professional backend asoslarini o'rgandingiz. Keyingi 27-darsda biz ushbu API ni xakerlik hujumlari (XSS, CSRF) dan tozalash va himoyalashni o'rganamiz!
    </p>
    <ul class="big-list">
      <li><span class="num">✓</span> <span data-ru="<strong>Домашнее задание:</strong> выполните 4 задачи в vazifa.html и пройдите онлайн-тест." data-en="<strong>Homework:</strong> complete the 4 challenges in vazifa.html and take the online quiz."><strong>Uy vazifasi:</strong> vazifa.html faylidagi 4 ta topshiriqni bajaring va test.html sinovidan o'ting.</span></li>
    </ul>
  </section>

</div>
"""

    notes = {
      "uz": [
        ["1-slayd: Kirish va Reja", "Bugun professional backend qurishni o'rganamiz: barcha kodni qismlarga ajratamiz.", "O'quvchilarga monolitdan MVC ga o'tish zaruratini uqtiring."],
        ["2-slayd: Tizimli Arxitektura", "Restoranda bitta oshpaz hamma ishni qilsa nima bo'ladi? Restoran qulaydi.", "Doskada Spaghetti kodning xavflarini sanab bering."],
        ["3-slayd: MVC Uchligi", "Model faqat baza bilan ishlaydi, Controller mantiqni tekshiradi, View natijani beradi.", "Har bir qatlamning o'z mas'uliyati borligini ta'kidlang."],
        ["4-slayd: Relyatsion Baza", "Foreign Key orqali buyurtmalar xaridorlar bilan 1-to-Many bog'lanadi.", "Baza mavjud bo'lmagan user_id ni qabul qilmasligini ko'rsating."],
        ["5-slayd: REST API Statuslar", "Xato bo'lganda 400 Bad Request, muvaffaqiyatda 201 Created qaytariladi.", "Status kodlarning ahamiyatini tushuntiring."],
        ["6-slayd: Controller Kodi", "Controller kodi kiruvchi quantity musbat ekanligini qat'iy tekshiradi.", "Kod blokidagi if shartini ko'rsating."],
        ["7-slayd: SQL INNER JOIN", "INNER JOIN 3 ta jadvaldan xaridor nomi va tovar nomini birlashtiradi.", "So'rov sintaksisini ko'rsating."],
        ["8-slayd: Studio Laboratoriyasi", "studio/index.html da so'rov oqimi animatsiyasini jonli sinab ko'ring.", "O'quvchilarga studioni ochishni ayting."],
        ["9-slayd: Jonli Kiber-Test", "Interaktiv testni yeching va 'Yechimni ko'rish' tugmasi bilan to'g'ri kodni ko'rsating.", "Sinf bilan birgalikda variantlarni tahlil qiling."],
        ["10-slayd: Amaliy Kvestlar", "Studioda 4 ta kvestni bajarib 100 ballga erishish zarur.", "Sinf bo'ylab aylanib o'quvchilarga yo'l ko'rsating."],
        ["11-slayd: 10 Ballik Mezon", "Baholash shaffof: arxitektura, baza, validatsiya va JOIN topshiriqlari.", "Mezon talablarini o'qib bering."],
        ["12-slayd: Xulosa va Uy Vazifasi", "Bugungi bilimlar 27-darsdagi XSS va CSRF himoyasiga poydevor bo'ladi.", "vazifa.html va test.html ni topshirishni eslating."]
      ],
      "ru": [
        ["Слайд 1: Введение и План", "Сегодня мы учимся строить масштабируемый бэкенд по стандарту MVC.", "Озвучьте тему урока и цели инженерной практики."],
        ["Слайд 2: Проблема Монолита", "Метафора ресторана: один повар не может делать всё одновременно.", "Поясните минусы спагетти-кода в server.js."],
        ["Слайд 3: Триада MVC", "Model отвечает за базу данных, Controller — за бизнес-логику, View — за выдачу.", "Объясните строгое разделение ответственности."],
        ["Слайд 4: Реляционные Связи", "Связи Foreign Key соединяют заказы с пользователями и товарами.", "Покажите обеспечение ссылочной целостности."],
        ["Слайд 5: Статусы REST API", "Никогда не возвращайте 200 при ошибке: используйте 400 Bad Request.", "Сравните коды 200, 201 и 400."],
        ["Слайд 6: Код Контроллера", "Контроллер валидирует тело запроса до обращения к базе.", "Разберите условия валидации на слайде."],
        ["Слайд 7: SQL INNER JOIN", "INNER JOIN объединяет связанные таблицы в плоский человекочитаемый чек.", "Покажите синтаксис объединения."],
        ["Слайд 8: Студия MVC", "В studio/index.html запросы визуализируются живой анимацией.", "Дайте команду открыть интерактивную лабораторию."],
        ["Слайд 9: Интерактивный Тест", "Разберите вопрос о статусе 400 Bad Request и покажите фикс.", "Обсудите правильный ответ с классом."],
        ["Слайд 10: Практика в Студии", "Выполните 4 инженерных квеста и соберите свой API.", "Контролируйте успешность выполнения квестов."],
        ["Слайд 11: 10-Балльный Критерий", "Оценка складывается из 4 понятных компонентов по 2.5 балла.", "Озвучьте требования к выполнению заданий."],
        ["Слайд 12: Итоги и Домашнее Задание", "Бэкенд готов к защите от XSS и CSRF на следующем уроке.", "Напомните о выполнении vazifa.html и онлайн-теста."]
      ],
      "en": [
        ["Slide 1: Intro & Goals", "Today we architect resilient backends using the industry-standard MVC pattern.", "Set an inspiring professional tone for the lesson."],
        ["Slide 2: Monolith Bottlenecks", "Restaurant metaphor: a solo cook doing all chores causes instant gridlock.", "Outline why 10,000 lines in server.js fail."],
        ["Slide 3: The MVC Triad", "Model handles raw SQLite data, Controller manages logic, View formats JSON.", "Emphasize clean boundaries of responsibility."],
        ["Slide 4: Relational SQLite", "Foreign Keys link transactions to users without data duplication.", "Explain referential integrity protections."],
        ["Slide 5: REST Status Codes", "Never reply with 200 on failure: standard status codes matter.", "Compare 200 OK, 201 Created, and 400 Bad Request."],
        ["Slide 6: Controller Validation", "Controllers must assert input bounds before invoking database models.", "Trace the input verification checks."],
        ["Slide 7: SQL INNER JOIN", "INNER JOIN merges three tables into a unified human-readable invoice.", "Explain joining syntax across primary keys."],
        ["Slide 8: Studio Workbench", "Launch studio/index.html to observe request flows in live animation.", "Prompt students to initiate test payloads."],
        ["Slide 9: Interactive Quiz & Fix", "Analyze why invalid payloads trigger 400 Bad Request and inspect the fix.", "Work through choices collaboratively."],
        ["Slide 10: 4 Engineering Quests", "Solve all 4 workbench challenges to master the API lifecycle.", "Facilitate lab work across student desks."],
        ["Slide 11: 10-Point Rubric", "Grading criteria: architecture, schema, validation, and multi-table queries.", "Clarify grading thresholds."],
        ["Slide 12: Summary & Next Step", "A scalable foundation is laid for XSS & CSRF defense next week.", "Direct students to vazifa.html and test.html."]
      ]
    }

    full_html = f"""<!DOCTYPE html>
<html lang="uz" data-theme="dark">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title data-ru="{html.escape(title['ru'])}" data-en="{html.escape(title['en'])}">{html.escape(title['uz'])}</title>
<link rel="icon" type="image/svg+xml" href="/assets/favicon.svg">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Manrope:wght@600;700;800&family=Source+Sans+3:wght@400;600;700&family=JetBrains+Mono:wght@400;600;700&display=swap">
{css_chunk}
</head>
<body>

{get_floating_elements(cohort_tag)}

{slides_html}

{get_modals()}

{get_js(notes)}

</body>
</html>
"""
    dest = os.path.join(folder, "prezentatsiya.html")
    with open(dest, "w", encoding="utf-8") as out:
        out.write(full_html)
    print(f"✓ Built {dest}")

build_lesson_26()

# 2. 10-11-sinf 31-dars: Penetration Testing & Ethical Hacking
def build_lesson_31():
    folder = "classes/10-11-sinf/7-hafta/31-dars-penetration-testing-va-ethical-hacking"
    cohort_tag = "10-11-SINF · WEEK 7"
    title = {
      "uz": "10–11-Sinf · 31-Dars: Penetration Testing & Ethical Hacking: O'z Zaiflik Skaneringni Dasturlash",
      "ru": "10–11-Класс · Урок 31: Тестирование на Проникновение и Этичный Хакинг: Разработка Своего Сканера",
      "en": "Grades 10–11 · Lesson 31: Penetration Testing & Ethical Hacking: Developing a Custom Scanner"
    }

    slides_html = """
<div class="stage">

  <!-- SLIDE 1: TITUL -->
  <section class="slide active" data-phase="KIRISH|ВВЕДЕНИЕ|INTRO" data-time="3 min">
    <div class="eyebrow" data-ru="10–11-КЛАСС · 7-Я НЕДЕЛЯ · УРОК 31" data-en="GRADES 10–11 · WEEK 7 · LESSON 31">
      10–11-SINF · 7-HAFTA · 31-DARS
    </div>
    <h1 class="hero-title" data-ru="Этичный Хакинг и Свой Сканер Уязвимостей" data-en="Ethical Hacking &amp; Custom Scanner Logic">
      Penetration Testing &amp; Ethical Hacking
    </h1>
    <p class="lede" data-ru="Переход от пассивной обороны к активному аудиту безопасности: методология PTES, ликвидация BOLA/IDOR, заголовки защиты и разработка CLI сканера." data-en="Pivoting from passive defense to proactive penetration audits: PTES lifecycle, BOLA/IDOR eradication, browser security headers, and automated CLI scanner construction.">
      Mudofaadan faol xavfsizlik auditiga o'tish: PTES metodologiyasi, OWASP #1 BOLA/IDOR zaifligini bartaraf etish, HTTP Security Headers va shaxsiy CLI skanerini dasturlash.
    </p>
    <ul class="big-list">
      <li><span class="num">01</span> <span data-ru="<strong>White Hat Принципы:</strong> законные границы аудита безопасности (Scope of Work и ст. 278 УК РУз)." data-en="<strong>White Hat Mandates:</strong> legal boundaries of penetration testing (Scope of Work &amp; legal codes)."><strong>White Hat qonuniy doirasi:</strong> yozma ruxsatnoma (Scope of Work) va O'zR JK 278-moddasi talablari.</span></li>
      <li><span class="num">02</span> <span data-ru="<strong>Автоматизация аудита:</strong> собственный легковесный сканер на Node.js для поиска утечек секретов." data-en="<strong>Audit Automation:</strong> developing a dependency-free Node.js CLI scanner to catch leaked secrets."><strong>Audit avtomatlashtirish:</strong> Node.js da RegEx orqali sizib chiqqan AWS va GitHub kalitlarini ovlovchi CLI skaner.</span></li>
    </ul>
  </section>

  <!-- SLIDE 2: WHITE HAT & PTES -->
  <section class="slide" data-phase="METODOLOGIYA|МЕТОДОЛОГИЯ|METHODOLOGY" data-time="3 min">
    <div class="eyebrow" data-ru="МЕТОДОЛОГИЯ PTES" data-en="PTES STANDARD">
      AXLOQIY XAKERLIK VA PTES
    </div>
    <h2 class="section-title" data-ru="Что отличает этичного инженера от киберпреступника?" data-en="What Distinguishes White Hats from Criminals?">
      Axloqiy xaker bilan kiber-jinoyatchi o'rtasidagi farq nima?
    </h2>
    <p class="statement" data-ru="Защитник обязан закрыть 100% дверей, а злоумышленнику достаточно найти одну щель. White Hat хакер действует строго в рамках утвержденного Scope of Work, чтобы найти уязвимость раньше врага и помочь ее закрыть." data-en="Defenders must safeguard 100% of the perimeter; adversaries require only a single opening. White Hat engineers act strictly within written Scope of Work boundaries to patch vulnerabilities before exploitation.">
      Himoyachi barcha eshiklarni qulflashi shart, hujumchiga esa atigi bitta xato yetarli. Axloqiy xaker (White Hat) faqat rasmiy ruxsatnoma (Scope of Work) doirasida zaiflikni dushmandan oldin topib, uni yopish uchun harakat qiladi.
    </p>
    <div class="text-cols">
      <div class="col-item">
        <span class="col-num">01</span>
        <h3 class="col-title" data-ru="Разведка (OSINT)" data-en="Reconnaissance">Razvedka</h3>
        <p class="col-desc" data-ru="Сбор информации о портах, версиях сервисов и доменных записях без шума." data-en="Passive and active intelligence gathering on ports, banners, and DNS.">Ochiq portlar, xizmat versiyalari va DNS yozuvlarini tahlil qilish.</p>
      </div>
      <div class="col-item">
        <span class="col-num">02</span>
        <h3 class="col-title" data-ru="Анализ угроз" data-en="Threat Modeling">Zaiflik tahlili</h3>
        <p class="col-desc" data-ru="Поиск ошибок авторизации BOLA, отсутствия CSP и утечек в бандлах." data-en="Spotting BOLA authorization flaws, missing CSP, and bundle token leaks.">BOLA ruxsat xatolari, yetishmayotgan CSP va sizib chiqqan kalitlarni topish.</p>
      </div>
      <div class="col-item">
        <span class="col-num">03</span>
        <h3 class="col-title" data-ru="Отчет (Report)" data-en="Remediation Report">Hisobot va Patch</h3>
        <p class="col-desc" data-ru="Оценка по CVSS v3.1 и точные рекомендации разработчикам по исправлению." data-en="CVSS v3.1 impact scoring and actionable patch guidelines for developers.">CVSS v3.1 xavf ballini hisoblash va dasturchilarga aniq tuzatish kodini berish.</p>
      </div>
    </div>
  </section>

  <!-- SLIDE 3: BOLA / IDOR EXPLAINED -->
  <section class="slide" data-phase="BOLA/IDOR|BOLA/IDOR|BOLA/IDOR" data-time="4 min">
    <div class="eyebrow" data-ru="OWASP API TOP 10 #1" data-en="OWASP API TOP 10 #1">
      OWASP API #1 XATOSI: BOLA / IDOR
    </div>
    <h2 class="section-title" data-ru="Broken Object Level Authorization: Анатомия взлома" data-en="Broken Object Level Authorization: Flaw Anatomy">
      BOLA / IDOR: Obyekt darajasidagi avtorizatsiyaning buzilishi
    </h2>
    <p class="lede" data-ru="Самая частая и разрушительная уязвимость современных API: сервер проверяет, что вы залогинены (JWT валиден), но забывает проверить, ваш ли это документ!" data-en="The most pervasive vulnerability in modern cloud APIs: server asserts user is authenticated, but forgets to verify object ownership:">
      Zamonaviy bulutli API larning eng xavfli nuqtasi: server foydalanuvchi tizimga kirganini tekshiradi (JWT to'g'ri), lekin bu hujjat aynan unga tegishlimi yoki yo'qligini tekshirishni unutadi!
    </p>
    <pre class="code-block">// ZAIF ENDPOINT (BOLA XAVFI):
app.get('/api/medical-records/:id', authenticateToken, (req, res) =&gt; {
  // Xaker :id ni 1001 dan 1002 ga o'zgartirib, begonaning kasallik varaqasini o'qiydi!
  const record = db.findRecord(req.params.id);
  res.json(record);
});</pre>
  </section>

  <!-- SLIDE 4: BOLA REMEDIATION -->
  <section class="slide" data-phase="TUZATISH|ИСПРАВЛЕНИЕ|REMEDIATION" data-time="4 min">
    <div class="eyebrow" data-ru="КОД ИСПРАВЛЕНИЯ" data-en="CODE REMEDIATION">
      BOLA ZAIFLIGINI KODDA TUZATISH
    </div>
    <h2 class="section-title" data-ru="Проверка владения: doc.owner_id === req.user.id" data-en="Ownership Assertion: doc.owner_id === req.user.id">
      Obyekt egasini qat'iy tekshirish va 403 Forbidden
    </h2>
    <p class="lede" data-ru="Каждый запрос к приватному ресурсу обязан сопоставлять ID владельца в БД с идентификатором из подтвержденного JWT токена:" data-en="Every private resource access must cross-examine database owner_id against authenticated JWT claims:">
      Har bir shaxsiy resurs so'rovida bazadagi `owner_id` bilan JWT tokendan olingan `req.user.id` solishtirilishi shart:
    </p>
    <pre class="code-block">// XAVFSIZ VA TUZATILGAN KOD:
app.get('/api/medical-records/:id', authenticateToken, (req, res) =&gt; {
  const record = db.findRecord(req.params.id);
  if (!record) return res.status(404).json({ error: "Yozuv topilmadi" });

  // EGASINI TEKSHIRISH (BOLA QALQONI):
  if (record.owner_id !== req.user.id) {
    return res.status(403).json({ error: "Kirish taqiqlangan! (403 Forbidden)" });
  }

  res.json({ success: true, record });
});</pre>
  </section>

  <!-- SLIDE 5: SECURITY HEADERS -->
  <section class="slide" data-phase="HEADERS|ЗАГОЛОВКИ|SECURITY HEADERS" data-time="4 min">
    <div class="eyebrow" data-ru="БРАУЗЕРНЫЕ ЗАГОЛОВКИ" data-en="BROWSER HEADERS">
      HTTP SECURITY HEADERS
    </div>
    <h2 class="section-title" data-ru="Защита от кликджекинга и перехвата трафика" data-en="Guarding Against Clickjacking &amp; MitM">
      Clickjacking va trafik o'g'irlanishiga qarshi HTTP sarlavhalari
    </h2>
    <div class="text-cols">
      <div class="col-item">
        <span class="col-num">X-FRAME-OPTIONS</span>
        <h3 class="col-title" data-ru="Кликджекинг" data-en="Clickjacking">Anti-Clickjacking</h3>
        <p class="col-desc" data-ru="DENY запрещает отображение сайта в чужих iframe, нейтрализуя невидимые клики." data-en="DENY blocks rendering in foreign iframes, halting invisible click attacks.">DENY qiymati saytni begona iframe ichida ochishni butkul taqiqlaydi.</p>
      </div>
      <div class="col-item">
        <span class="col-num">CSP</span>
        <h3 class="col-title" data-ru="Белый список скриптов" data-en="Content Security">Content-Security</h3>
        <p class="col-desc" data-ru="Разрешает загрузку скриптов только с доверенных доменов, блокируя инъекции XSS." data-en="Permits script execution strictly from whitelisted origins, repelling XSS.">Faqat ruxsat berilgan serverlardan skript yuklashga ruxsat berib XSS ni to'xtatadi.</p>
      </div>
      <div class="col-item">
        <span class="col-num">HSTS</span>
        <h3 class="col-title" data-ru="Только HTTPS" data-en="Enforce HTTPS">Strict-Transport</h3>
        <p class="col-desc" data-ru="Принуждает браузер использовать строго зашифрованное соединение HTTPS." data-en="Forces browsers to communicate exclusively over encrypted HTTPS channels.">Brauzerni faqat shifrlangan HTTPS orqali bog'lanishga majburlaydi.</p>
      </div>
    </div>
  </section>

  <!-- SLIDE 6: CVSS V3.1 SCORING -->
  <section class="slide" data-phase="CVSS|ОЦЕНКА CVSS|CVSS SCORING" data-time="4 min">
    <div class="eyebrow" data-ru="МЕЖДУНАРОДНАЯ ШКАЛА" data-en="GLOBAL BENCHMARK">
      CVSS V3.1 XAVF SHKALASI
    </div>
    <h2 class="section-title" data-ru="Как рассчитать тяжесть уязвимости (0.0 – 10.0)" data-en="Quantifying Severity via CVSS v3.1 (0.0 – 10.0)">
      Zaiflik xavfini xalqaro CVSS formulasi bilan hisoblash
    </h2>
    <p class="lede" data-ru="CVSS v3.1 — глобальный стандарт оценки уязвимостей. Балл вычисляется из вектора атаки, сложности и ущерба:" data-en="CVSS v3.1 is the global standard for threat quantification. Metrics balance attack vectors, complexity, and impact:">
      CVSS v3.1 tizimi zaiflik xavfini xolisona o'lchaydi: hujum yo'li, murakkabligi va yetkaziladigan zarar hisobga olinadi:
    </p>
    <ul class="big-list">
      <li><span class="num">0.1–3.9</span> <span data-ru="<strong>Low (Низкий):</strong> минимальный локальный риск, требуется физический доступ." data-en="<strong>Low Severity:</strong> minimal threat, requires local access or rare preconditions."><strong>Low (Past):</strong> kichik lokal xavf, jiddiy ma'lumotlar yo'qolmaydi.</span></li>
      <li><span class="num">4.0–6.9</span> <span data-ru="<strong>Medium (Средний):</strong> атака требует аутентификации или взаимодействия с жертвой." data-en="<strong>Medium Severity:</strong> requires authentication or victim interaction."><strong>Medium (O'rtacha):</strong> autentifikatsiya yoki qurbonning harakati talab etiladi.</span></li>
      <li><span class="num">7.0–8.9</span> <span data-ru="<strong>High (Высокий):</strong> удаленное чтение конфиденциальных данных или сбой сервиса." data-en="<strong>High Severity:</strong> remote unauthorized data leak or denial of service."><strong>High (Yuqori):</strong> masofadan maxfiy ma'lumotlarni sizdirish imkoniyati.</span></li>
      <li><span class="num">9.0–10.0</span> <span data-ru="<strong>Critical (Критический):</strong> удаленный захват сервера (RCE) без авторизации." data-en="<strong>Critical Severity:</strong> unauthenticated remote code execution or full compromise."><strong>Critical (Kritik):</strong> parolsiz masofadan serverni to'liq qo'lga olish (RCE).</span></li>
    </ul>
  </section>

  <!-- SLIDE 7: CUSTOM CLI SCANNER -->
  <section class="slide" data-phase="SKANER|СКАНЕР|CLI SCANNER" data-time="4 min">
    <div class="eyebrow" data-ru="РАЗРАБОТКА ИНСТРУМЕНТА" data-en="CUSTOM TOOLING">
      SHAXSIY CLI ZAIFLIK SKANERI
    </div>
    <h2 class="section-title" data-ru="Пишем свой сканер на чистом Node.js (scanner.js)" data-en="Engineering a Native Node.js CLI Scanner">
      Tashqi kutubxonasiz Node.js da skaner dasturlash
    </h2>
    <p class="lede" data-ru="Наш сканер скачивает HTML и JS-бандлы цели, анализирует заголовки и ищет забытые API-ключи через RegEx:" data-en="Our standalone CLI scanner inspects HTTP headers and searches JS bundles for leaked cloud secrets via RegEx:">
      Skanerimiz server sarlavhalarini tekshiradi va JavaScript fayllar ichidan unutib qoldirilgan bulut kalitlarini qidiradi:
    </p>
    <pre class="code-block">// scanner/scanner.js
const SECRET_PATTERNS = [
  { name: 'GitHub Token', regex: /ghp_[a-zA-Z0-9]{{36}}/g, cvss: 9.8 },
  { name: 'AWS Access Key', regex: /AKIA[0-9A-Z]{{16}}/g, cvss: 9.5 },
  { name: 'Private Key Block', regex: /-----BEGIN PRIVATE KEY-----/g, cvss: 10.0 }
];

function auditHeaders(headers) {{
  if (!headers['x-frame-options']) console.log('⚠️ Clickjacking xavfi bor!');
  if (!headers['content-security-policy']) console.log('⚠️ CSP yetishmayapti!');
}}</pre>
  </section>

  <!-- SLIDE 8: PENTEST STUDIO -->
  <section class="slide" data-phase="STUDIO|СТУДИЯ|STUDIO" data-time="4 min">
    <div class="eyebrow" data-ru="ИНТЕРАКТИВНЫЙ АУДИТ" data-en="INTERACTIVE AUDIT">
      TARGET PENTEST STUDIO
    </div>
    <h2 class="section-title" data-ru="Графическая студия: Сканирование в реальном времени" data-en="GUI Workbench: Real-Time Security Telemetry">
      Vizual studio: Jonli ANSI telemetriyasi va CVSS kalkulyatori
    </h2>
    <p class="lede" data-ru="В папке studio/index.html открывается тренировочный полигон: 4 модуля сканирования, живой журнал аудита и CVSS калькулятор." data-en="Launch studio/index.html for live testing: 4 security audit modules, ANSI console logs, and CVSS calculators:">
      `studio/index.html` da xavfsiz laboratoriya muhiti yaratilgan: 4 ta modulni tanlab tizimni skanerlash va natijalarni jonli tahlil qilish mumkin.
    </p>
    <ul class="big-list">
      <li><span class="num">01</span> <span data-ru="<strong>Модули аудита:</strong> проверка BOLA, сканирование заголовков, поиск AWS ключей и SQLi." data-en="<strong>Audit Modules:</strong> BOLA checks, security header sweeps, AWS secret discovery, and SQLi fuzzing."><strong>Audit modullari:</strong> BOLA tekshiruvi, xavfsizlik sarlavhalari, AWS kalitlari va SQLi qidiruvi.</span></li>
      <li><span class="num">02</span> <span data-ru="<strong>CVSS v3.1 Слайдер:</strong> интерактивное изменение метрик и автоматический пересчет тяжести." data-en="<strong>Interactive CVSS:</strong> dynamic metric adjustments recalculating vulnerability score."><strong>Interaktiv CVSS:</strong> slayderlarni o'zgartirib zaiflik darajasini hisoblash.</span></li>
    </ul>
  </section>

  <!-- SLIDE 9: QUIZ & FIX -->
  <section class="slide" data-phase="TEST|ТЕСТ|QUIZ &amp; FIX" data-time="5 min">
    <div class="eyebrow" data-ru="ИНТЕРАКТИВНЫЙ ТЕСТ" data-en="INTERACTIVE TEST &amp; FIX">
      JONLI KIBER-TEST VA YECHIM (FIX)
    </div>
    <h2 class="section-title" data-ru="Тест: Как предотвратить атаку BOLA / IDOR?" data-en="Quiz: How to Prevent BOLA / IDOR Flaws?">
      Sinov: BOLA / IDOR hujumini qanday to'xtatish mumkin?
    </h2>
    <p class="lede" data-ru="Выберите наиболее надежный инженерный способ защиты API:" data-en="Identify the definitive engineering mitigation for BOLA:">
      Quyidagi usullardan qaysi biri BOLA zaifligini butunlay yo'qotadi:
    </p>
    <div class="quiz-box">
      <div class="quiz-option" onclick="checkQuiz(this, false)">
        <span class="num">A</span> <span data-ru="Использовать случайные длинные ID (UUID) вместо чисел." data-en="Rely solely on randomized UUIDs instead of integer IDs.">Raqamlar o'rniga faqat tasodifiy uzun UUID ishlatish kifoya.</span>
      </div>
      <div class="quiz-option" onclick="checkQuiz(this, true)">
        <span class="num">B</span> <span data-ru="Проверять doc.owner_id === req.user.id и отдавать 403 Forbidden при несовпадении." data-en="Assert doc.owner_id === req.user.id and return 403 Forbidden on mismatch.">doc.owner_id === req.user.id ni tekshirish va mos kelmasa 403 qaytarish.</span>
      </div>
      <div class="quiz-option" onclick="checkQuiz(this, false)">
        <span class="num">C</span> <span data-ru="Отключить логирование запросов на сервере." data-en="Disable backend request logging.">Serverda so'rovlar tarixini o'chirib qo'yish.</span>
      </div>
    </div>
    <div class="test-actions">
      <button class="test-btn" onclick="toggleTestFix()" data-ru="Показать исправление (Fix)" data-en="Show Solution (Fix)">Yechimni ko'rish (Fix)</button>
    </div>
    <div class="fix-reveal" id="testFixBox">
      // MUHANDISLIK TUZATMASI (FIX):<br>
      // UUID faqat taxmin qilishni qiyinlashtiradi, lekin huquqni tekshirmaydi!<br>
      // Haqiqiy himoya faqat Obyekt Egasini tekshirishdir:<br>
      if (document.owner_id !== req.user.id) return res.status(403).json({ error: "Access Denied" });
    </div>
  </section>

  <!-- SLIDE 10: PRACTICE PATHS -->
  <section class="slide" data-phase="AMALIYOT|ПРАКТИКА|PRACTICE" data-time="8 min">
    <div class="eyebrow" data-ru="ДВА ПУТИ АУДИТА" data-en="DUAL AUDIT PATHS">
      AMALIYOT: IKKI YO'NALISHLI SINOV
    </div>
    <h2 class="section-title" data-ru="Выбери свой трек: GUI Studio или CLI Scanner" data-en="Choose Your Track: GUI Studio or CLI Scanner">
      Yo'lingizni tanlang: GUI Studio yoki Terminal CLI
    </h2>
    <div class="text-cols">
      <div class="col-item">
        <span class="col-num">PATH A</span>
        <h3 class="col-title" data-ru="Target Pentest Studio" data-en="GUI Pentest Studio">Brauzerda Studio</h3>
        <p class="col-desc" data-ru="Запустите studio/index.html, просканируйте 4 модуля и рассчитайте CVSS балл." data-en="Launch studio/index.html, scan all 4 targets, and calculate CVSS ratings.">studio/index.html ni oching, 4 ta modulni skanerlang va CVSS hisoblang.</p>
      </div>
      <div class="col-item">
        <span class="col-num">PATH B</span>
        <h3 class="col-title" data-ru="Node.js CLI Scanner" data-en="CLI Scanner Engine">Terminalda CLI</h3>
        <p class="col-desc" data-ru="Выполните node scanner/scanner.js --demo и получите JSON-отчет безопасности." data-en="Execute node scanner/scanner.js --demo and export your security-report.json.">Terminalda node scanner/scanner.js --demo ni yurgizing va hisobot oling.</p>
      </div>
    </div>
  </section>

  <!-- SLIDE 11: RUBRIC -->
  <section class="slide" data-phase="BAHOLASH|ОЦЕНКА|RUBRIC" data-time="3 min">
    <div class="eyebrow" data-ru="10-БАЛЛЬНЫЙ СТАНДАРТ" data-en="10-POINT STANDARD">
      RASMIY BAHOLASH MEZONI
    </div>
    <h2 class="section-title" data-ru="Критерии оценки за урок (10 баллов)" data-en="Lesson Evaluation Rubric (10 Points)">
      10 ballik rasmiy baholash mezoni
    </h2>
    <ul class="big-list">
      <li><span class="num">01</span> <span data-ru="<strong>PTES и этика White Hat (2.5 балла):</strong> понимание фаз аудита и законных рамок." data-en="<strong>PTES &amp; White Hat Ethics (2.5 pts):</strong> comprehension of audit lifecycle and legal rules."><strong>PTES va White Hat etikasi (2.5 ball):</strong> audit bosqichlari va qonuniy me'yorlarni tushunish.</span></li>
      <li><span class="num">02</span> <span data-ru="<strong>Ликвидация BOLA/IDOR (2.5 балла):</strong> корректное исправление контроллера через проверку owner_id." data-en="<strong>BOLA Mitigation (2.5 pts):</strong> patching controllers by validating owner_id vs req.user.id."><strong>BOLA zaifligini tuzatish (2.5 ball):</strong> owner_id tekshiruvi bilan kodni xavfsiz qilish.</span></li>
      <li><span class="num">03</span> <span data-ru="<strong>Security Headers и CVSS (2.5 балла):</strong> настройка X-Frame-Options, CSP и расчет баллов угрозы." data-en="<strong>Security Headers &amp; CVSS (2.5 pts):</strong> configuring X-Frame-Options, CSP, and CVSS score math."><strong>Security Headers va CVSS (2.5 ball):</strong> brauzer sarlavhalari va CVSS formulasi tahlili.</span></li>
      <li><span class="num">04</span> <span data-ru="<strong>Сканнер и Studio (2.5 балла):</strong> запуск аудита в Studio или через CLI и получение отчета." data-en="<strong>Scanner Execution (2.5 pts):</strong> completing audit runs in Studio or CLI and generating reports."><strong>Skaner va Studio (2.5 ball):</strong> Studioda yoki terminalda audit o'tkazib natija olish.</span></li>
    </ul>
  </section>

  <!-- SLIDE 12: SUMMARY -->
  <section class="slide" data-phase="XULOSA|ИТОГИ|SUMMARY" data-time="2 min">
    <div class="eyebrow" data-ru="ИТОГИ И МОСТ" data-en="SUMMARY &amp; NEXT STEP">
      XULOSA VA KEYINGI DARS
    </div>
    <h1 class="hero-title" data-ru="Готовы к рубежному CTF турниру!" data-en="Ready for the Midterm CTF Tournament!">
      Oraliq Nazorat CTF Kiber-Turniriga Tayyorsiz!
    </h1>
    <p class="lede" data-ru="Вы научились думать как атакующий, чтобы надежно строить оборону. На следующем 32-уроке нас ждет итоговый рубежный контроль — CTF Kiber-Turniri!" data-en="You now understand attack surfaces to engineer invincible defenses. Lesson 32 brings our Quarter 1 Midterm Exam: Corporate Defense &amp; CTF Tournament!">
      Siz tizimni xavfsiz himoyalash uchun unga hujumchi ko'zi bilan qarashni o'rgandingiz. Keyingi 32-darsda 1-chorak oraliq nazorati — CTF Kiber-Turniri bo'lib o'tadi!
    </p>
    <ul class="big-list">
      <li><span class="num">✓</span> <span data-ru="<strong>Домашнее задание:</strong> выполните 4 задачи в vazifa.html и пройдите онлайн-тест." data-en="<strong>Homework:</strong> complete all 4 challenges in vazifa.html and take the online quiz."><strong>Uy vazifasi:</strong> vazifa.html dagi topshiriqlarni bajaring va test.html sinovidan o'ting.</span></li>
    </ul>
  </section>

</div>
"""

    notes = {
      "uz": [
        ["1-slayd: Kirish va Reja", "Bugun mudofaadan hujumga o'tamiz — shaxsiy zaiflik skanerimizni yaratamiz.", "O'quvchilarda axloqiy xakerlikka qiziqish uyg'oting."],
        ["2-slayd: White Hat va PTES", "White Hat faqat yozma ruxsat bilan ishlaydi. O'zR JK 278-moddasini eslating.", "Doskada PTES 5 bosqichini sanab bering."],
        ["3-slayd: BOLA Zaifligi", "BOLA — zamonaviy API larning 1-raqamli kritik xatosi hisoblanadi.", "Nega UUID yetarli emasligini tushuntiring."],
        ["4-slayd: BOLA ni Tuzatish", "owner_id tekshiruvi orqali foydalanuvchini faqat o'z fayliga cheklaymiz.", "403 Forbidden status kodini ko'rsating."],
        ["5-slayd: Security Headers", "Clickjacking hujumiga qarshi X-Frame-Options: DENY sarlavhasini tushuntiring.", "Helmet kutubxonasi afzalligini ayting."],
        ["6-slayd: CVSS v3.1 Shkalasi", "CVSS reytingi 0.0 dan 10.0 gacha bo'lishini va Critical darajani ko'rsating.", "Formula parametrlarini tahlil qiling."],
        ["7-slayd: Shaxsiy CLI Skaner", "scanner.js kodi qanday qilib regex bilan AWS va GitHub kalitlarini ovlashini ko'rsating.", "RegEx sintaksisini tushuntiring."],
        ["8-slayd: Studio Laboratoriyasi", "studio/index.html ochib real-vaqtli skanerlashni boshlang.", "O'quvchilarga studioni ochishni buyuring."],
        ["9-slayd: Jonli Test va Yechim", "Testni yeching va nima uchun faqat owner_id to'liq himoya qilishini ko'rsating.", "Yechimni ko'rish tugmasini bosing."],
        ["10-slayd: Ikki Yo'nalish", "Path A (Studio) yoki Path B (CLI skaner) bo'yicha amaliyot bajartiring.", "Terminal buyruqlarini tekshirib yordam bering."],
        ["11-slayd: 10 Ballik Mezon", "Baholash shaffof: nazariya, BOLA fix, headers va skanerlash.", "Mezon talablarini o'qib bering."],
        ["12-slayd: Xulosa va Keyingi Dars", "Keyingi 32-darsda 1-chorak oraliq nazorati — CTF kiber-turniri o'tkaziladi.", "vazifa.html va test.html ni topshirishni eslating."]
      ],
      "ru": [
        ["Слайд 1: Введение и План", "Сегодня мы переходим на сторону этичного хакинга и пишем свой сканер уязвимостей.", "Озвучьте цели урока и инженерные задачи."],
        ["Слайд 2: Этика White Hat", "Этичный хакинг действует строго в рамках Scope of Work и закона (ст. 278 УК РУз).", "Перечислите 5 фаз стандарта PTES."],
        ["Слайд 3: Анатомия BOLA", "BOLA — уязвимость №1 в мировом рейтинге OWASP API Top 10.", "Покажите механику подмены id в эндпоинте."],
        ["Слайд 4: Устранение BOLA", "Проверка doc.owner_id === req.user.id и статус 403 Forbidden.", "Разберите патч контроллера на слайде."],
        ["Слайд 5: Заголовки Безопасности", "Заголовок X-Frame-Options: DENY полностью блокирует атаки кликджекинга.", "Объясните CSP и HSTS."],
        ["Слайд 6: Шкала CVSS v3.1", "CVSS ранжирует угрозы от 0.0 до 10.0 баллов (9.0–10.0 — Critical).", "Покажите, как вычисляется тяжесть риска."],
        ["Слайд 7: CLI Сканер на Node.js", "Скрипт scanner.js находит скрытые приватные ключи через RegEx.", "Разберите структуру сигнатур."],
        ["Слайд 8: Студия Pentest", "В studio/index.html доступен интерактивный аудит с ANSI журналом.", "Дайте команду открыть лабораторию."],
        ["Слайд 9: Интерактивный Тест", "Разберите вопрос о BOLA и покажите инженерный фикс.", "Обсудите правильный ответ с классом."],
        ["Слайд 10: Два Пути Практики", "Ученики выбирают трек: визуальный в Studio или через CLI в терминале.", "Контролируйте ход выполнения аудита."],
        ["Слайд 11: 10-Балльный Критерий", "Оценка складывается из 4 компонентов по 2.5 балла.", "Озвучьте требования к выполнению заданий."],
        ["Слайд 12: Итоги и CTF Турнир", "На 32-м уроке нас ждет главный рубежный экзамен — CTF турнир!", "Напомните о выполнении vazifa.html и онлайн-теста."]
      ],
      "en": [
        ["Slide 1: Intro & Goals", "Today we shift into ethical penetration testing and code our own vulnerability scanner.", "Set an inspiring professional tone for the session."],
        ["Slide 2: White Hat Ethics", "White Hat actions mandate strict written Scope of Work adherence.", "Walk through the 5 phases of the PTES lifecycle."],
        ["Slide 3: BOLA / IDOR Flaw", "BOLA ranks #1 across OWASP API Security Top 10 worldwide.", "Explain why UUID obfuscation alone fails."],
        ["Slide 4: BOLA Remediation", "Cross-checking doc.owner_id against req.user.id and returning 403.", "Inspect the patched controller code."],
        ["Slide 5: Security Headers", "X-Frame-Options: DENY completely repels Clickjacking iframe framing.", "Discuss CSP and HSTS enforcement."],
        ["Slide 6: CVSS v3.1 Benchmarking", "CVSS scoring ranges from 0.0 to 10.0 (9.0–10.0 denotes Critical).", "Explain metrics driving vulnerability math."],
        ["Slide 7: Native Node.js Scanner", "scanner.js catches leaked tokens inside bundles using targeted RegEx.", "Review signature definitions."],
        ["Slide 8: Pentest Workbench", "Launch studio/index.html for live testing and telemetry observation.", "Direct students to initialize security sweeps."],
        ["Slide 9: Interactive Quiz & Fix", "Analyze why object ownership assertions eliminate BOLA completely.", "Review choices collaboratively."],
        ["Slide 10: Dual Audit Tracks", "Students choose Path A (GUI Studio) or Path B (Terminal CLI engine).", "Support students during hands-on execution."],
        ["Slide 11: 10-Point Rubric", "Transparent criteria: ethics, BOLA fix, headers, and scanner execution.", "Clarify grading thresholds."],
        ["Slide 12: Summary & Next Step", "Next week: Lesson 32 Midterm Exam — Corporate Defense & CTF Tournament!", "Direct students to vazifa.html and test.html."]
      ]
    }

    full_html = f"""<!DOCTYPE html>
<html lang="uz" data-theme="dark">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title data-ru="{html.escape(title['ru'])}" data-en="{html.escape(title['en'])}">{html.escape(title['uz'])}</title>
<link rel="icon" type="image/svg+xml" href="/assets/favicon.svg">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Manrope:wght@600;700;800&family=Source+Sans+3:wght@400;600;700&family=JetBrains+Mono:wght@400;600;700&display=swap">
{css_chunk}
</head>
<body>

{get_floating_elements(cohort_tag)}

{slides_html}

{get_modals()}

{get_js(notes)}

</body>
</html>
"""
    dest = os.path.join(folder, "prezentatsiya.html")
    with open(dest, "w", encoding="utf-8") as out:
        out.write(full_html)
    print(f"✓ Built {dest}")

build_lesson_31()

# 3. 7-8-sinf 29-dars: GPS Navigatsiya va Eng Qisqa Yo'l Algoritmi
def build_lesson_29():
    folder = "classes/7-8-sinf/7-hafta/29-dars-gps-navigatsiya-va-eng-qisqa-yol"
    cohort_tag = "7-8-SINF · WEEK 7"
    title = {
      "uz": "7–8-Sinf · 29-Dars: GPS Navigatsiya va Eng Qisqa Yo'l Algoritmi: Google Maps Qanday Ishlaydi?",
      "ru": "7–8-Класс · Урок 29: GPS Навигация и Алгоритм Кратчайшего Пути: Как работает Google Maps?",
      "en": "Grades 7–8 · Lesson 29: GPS Navigation & Shortest Path Algorithm: How Google Maps Works?"
    }

    slides_html = """
<div class="stage">

  <!-- SLIDE 1: TITUL -->
  <section class="slide active" data-phase="KIRISH|ВВЕДЕНИЕ|INTRO" data-time="3 min">
    <div class="eyebrow" data-ru="7–8-КЛАСС · 7-Я НЕДЕЛЯ · УРОК 29" data-en="GRADES 7–8 · WEEK 7 · LESSON 29">
      7–8-SINF · 7-HAFTA · 29-DARS
    </div>
    <h1 class="hero-title" data-ru="GPS Навигация и Алгоритмы Кратчайшего Пути" data-en="GPS Navigation &amp; Shortest Path Algorithms">
      GPS Navigatsiya va Eng Qisqa Yo'l Algoritmi
    </h1>
    <p class="lede" data-ru="Как работают Google Maps и Yandex Go: теория графов, алгоритмы Дейкстры и A*, сферическая тригонометрия Гаверсинуса и Geolocation API." data-en="Unraveling Google Maps and Yandex Go navigation: graph theory, Dijkstra and A* pathfinding, spherical Haversine trigonometry, and HTML5 Geolocation API.">
      Google Maps va Yandex Go qanday ishlaydi: graf nazariyasi, Dijkstra va A* algoritmlari, Haversine sferik masofasi va brauzer Geolocation API.
    </p>
    <ul class="big-list">
      <li><span class="num">01</span> <span data-ru="<strong>Карта как граф:</strong> перекрестки — вершины (Vertices), дороги — взвешенные ребра (Edges)." data-en="<strong>Map as a Graph:</strong> intersections as vertices, streets as weighted connecting edges."><strong>Xarita — bu Graf:</strong> chorrahalar tugunlar (Vertices), ko'chalar esa vaznli qirralar (Edges).</span></li>
      <li><span class="num">02</span> <span data-ru="<strong>Мгновенный расчет пути:</strong> математика поиска кратчайшего маршрута без перебора миллиардов дорог." data-en="<strong>Instant Routing:</strong> calculating optimal routes without bruteforcing millions of roads."><strong>Tezkor yo'l hisobi:</strong> millionlab yo'llarni bittalab tekshirmasdan eng optimalini topish.</span></li>
    </ul>
  </section>

  <!-- SLIDE 2: THE PROBLEM -->
  <section class="slide" data-phase="MUAMMO|ПРОБЛЕМА|THE CHALLENGE" data-time="3 min">
    <div class="eyebrow" data-ru="ИНЖЕНЕРНАЯ ЗАДАЧА" data-en="ENGINEERING CHALLENGE">
      NAVIGATSIYA MUAMMOSI
    </div>
    <h2 class="section-title" data-ru="Как найти маршрут за 0.05 секунды среди 10 млн улиц?" data-en="Finding Routes in 0.05s Across 10 Million Roads">
      Qanday qilib 10 million ko'cha ichidan 0.05 soniyada yo'l topiladi?
    </h2>
    <p class="statement" data-ru="Если перебирать все возможные комбинации улиц по очереди, даже суперкомпьютеру потребуются годы. Навигаторы используют взвешенные графы и алгоритм Дейкстры, отсекая тупиковые ветки мгновенно." data-en="Exhaustive brute-force checks across urban roads would take supercomputers years. Modern GPS engines structure roads into weighted graphs and use Dijkstra pathfinding to prune dead ends instantly.">
      Agar barcha ko'chalarni ketma-ket bittalab hisoblab chiqilsa, superkompyuterga ham yillar kerak bo'lar edi. Navigatsiya tizimlari graf nazariyasi va Dijkstra algoritmidan foydalanib, befoyda yo'llarni bir zumda chetga suradi.
    </p>
    <div class="text-cols">
      <div class="col-item">
        <span class="col-num">01</span>
        <h3 class="col-title" data-ru="Перекрестки" data-en="Intersections">Tugunlar (Vertices)</h3>
        <p class="col-desc" data-ru="Точки на карте, где можно изменить направление движения." data-en="Decision points on maps where drivers can switch routes.">Xaritada harakat yo'nalishini o'zgartirish mumkin bo'lgan chorrahalar.</p>
      </div>
      <div class="col-item">
        <span class="col-num">02</span>
        <h3 class="col-title" data-ru="Дороги" data-en="Street Segments">Qirralar (Edges)</h3>
        <p class="col-desc" data-ru="Улицы, связывающие перекрестки. Могут быть односторонними." data-en="Road segments connecting vertices. Can be one-way or bidirectional.">Chorrahalarni bog'lovchi ko'chalar. Ular bir tomonlama bo'lishi mumkin.</p>
      </div>
      <div class="col-item">
        <span class="col-num">03</span>
        <h3 class="col-title" data-ru="Веса ребер" data-en="Edge Weights">Vaznlar (Weights)</h3>
        <p class="col-desc" data-ru="Расстояние в метрах или время с учетом текущих пробок." data-en="Travel distance in meters or latency adjusted by live traffic.">Masofa (metrda) yoki tirbandlikka qarab ketadigan daqiqalar.</p>
      </div>
    </div>
  </section>

  <!-- SLIDE 3: GRAPH IN JAVASCRIPT -->
  <section class="slide" data-phase="GRAF|ГРАФЫ В КОДЕ|GRAPH IN JS" data-time="4 min">
    <div class="eyebrow" data-ru="СТРУКТУРА ДАННЫХ" data-en="DATA STRUCTURE">
      GRAFLARNI JAVASCRIPTDA YOZISH
    </div>
    <h2 class="section-title" data-ru="Список смежности (Adjacency List) на объектах JS" data-en="Adjacency List Representation in JavaScript">
      Adjacency List: Xaritani JavaScript ob'ektida saqlash
    </h2>
    <p class="lede" data-ru="В коде карта представляется как вложенный объект, где ключи — это вершины, а значения — соседние точки с расстояниями:" data-en="Navigation maps are programmed as nested objects where keys represent vertices and values define neighbor distances:">
      Kodda xarita ichma-ich ob'ekt shaklida ifodalanadi: har bir chorraha nomi kalit, unga ulangan qo'shni ko'chalar esa masofasi bilan saqlanadi:
    </p>
    <pre class="code-block">const cityMap = {
  'Maktab':  { 'Metro': 500, 'Park': 800 },
  'Metro':   { 'Maktab': 500, 'Park': 300, 'Stadion': 600 },
  'Park':    { 'Maktab': 800, 'Metro': 300, 'Stadion': 400 },
  'Stadion': { 'Metro': 600, 'Park': 400 }
};</pre>
  </section>

  <!-- SLIDE 4: DIJKSTRA ALGORITHM -->
  <section class="slide" data-phase="DIJKSTRA|ДЕЙКСТРА|DIJKSTRA" data-time="4 min">
    <div class="eyebrow" data-ru="АЛГОРИТМ ДЕЙКСТРЫ" data-en="DIJKSTRA PATHFINDING">
      DIJKSTRA ENG QISQA YO'L ALGORITMI
    </div>
    <h2 class="section-title" data-ru="Как волна находит самый быстрый путь" data-en="Finding the Shortest Route Like a Ripple">
      To'lqin kabi eng qisqa yo'lni qidirish
    </h2>
    <p class="lede" data-ru="Эдсгер Дейкстра придумал этот алгоритм в 1956 году. Он исследует ближайшие непосещенные вершины шаг за шагом:" data-en="Invented by Edsger Dijkstra in 1956, this algorithm expands outward by always visiting the nearest unvisited node:">
      1956 yilda yaratilgan ushbu algoritm boshlang'ich nuqtadan boshlab har doim eng yaqin ko'rilmagan tugunni tanlaydi:
    </p>
    <ul class="big-list">
      <li><span class="num">01</span> <span data-ru="<strong>Инициализация:</strong> расстояние до старта = 0, до всех остальных = бесконечность (Infinity)." data-en="<strong>Initialization:</strong> distance to start = 0, all other nodes set to Infinity."><strong>Boshlang'ich holat:</strong> start nuqtagacha masofa = 0, qolgan barcha nuqtalargacha = cheksizlik (Infinity).</span></li>
      <li><span class="num">02</span> <span data-ru="<strong>Релаксация ребер:</strong> проверяем: если путь через соседа короче текущего, обновляем значение." data-en="<strong>Edge Relaxation:</strong> if path through neighbor is shorter than recorded distance, update it."><strong>Qirralarni yangilash:</strong> agar qo'shni orqali borish qisqaroq bo'lsa, masofani yangilab boradi.</span></li>
      <li><span class="num">03</span> <span data-ru="<strong>Финиш:</strong> когда дошли до цели, восстанавливаем цепочку родителей (Backtracking)." data-en="<strong>Backtracking:</strong> once target is reached, reconstruct the shortest path chain."><strong>Yo'lni tiklash:</strong> manzilga yetgach, orqaga qarab eng optimal marshrut chizib beriladi.</span></li>
    </ul>
  </section>

  <!-- SLIDE 5: HAVERSINE FORMULA -->
  <section class="slide" data-phase="HAVERSINE|ГАВЕРСИНУС|HAVERSINE" data-time="4 min">
    <div class="eyebrow" data-ru="СФЕРИЧЕСКАЯ ГЕОМЕТРИЯ" data-en="SPHERICAL TRIGONOMETRY">
      HAVERSINE MASOFA FORMULASI
    </div>
    <h2 class="section-title" data-ru="Земля — это шар: Почему Пифагор ошибается" data-en="Earth is a Sphere: Why Planar Math Fails">
      Yer sharsimon: Nega oddiy Pifagor formulasi to'g'ri kelmaydi?
    </h2>
    <p class="statement" data-ru="На плоскости расстояние вычисляется как a² + b² = c². Но Земля искривлена! При расстояниях более 5 км погрешность плоской формулы накапливается. Формула Гаверсинуса учитывает радиус Земли (6371 км)." data-en="On flat planes, distance is a² + b² = c². But Earth curves! Over distances exceeding 5km, planar errors multiply. The Haversine formula factors in Earth's spherical radius (6371 km).">
      Tekis qog'ozda masofa Pifagor teoremasi (a² + b² = c²) bilan hisoblanadi. Lekin Yer shar shaklida egrilikka ega! 5 km dan ortiq masofalarda tekislik formulasi adashadi. Haversine formulasi Yer radiusi (6371 km) bo'ylab aniq egrilikni hisoblaydi.
    </p>
    <pre class="code-block">function haversine(lat1, lon1, lat2, lon2) {
  const R = 6371; // Yer radiusi (km)
  const toRad = deg =&gt; deg * Math.PI / 180;
  const dLat = toRad(lat2 - lat1);
  const dLon = toRad(lon2 - lon1);
  const a = Math.sin(dLat/2)**2 + 
            Math.cos(toRad(lat1)) * Math.cos(toRad(lat2)) * Math.sin(dLon/2)**2;
  return R * 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));
}</pre>
  </section>

  <!-- SLIDE 6: GEOLOCATION API -->
  <section class="slide" data-phase="GPS API|GEOLOCATION API|GEOLOCATION API" data-time="4 min">
    <div class="eyebrow" data-ru="БРАУЗЕРНЫЙ СТАНДАРТ" data-en="BROWSER STANDARD">
      W3C GEOLOCATION API
    </div>
    <h2 class="section-title" data-ru="Как браузер узнает, где вы находитесь" data-en="How Browsers Locate Your Device">
      Brauzer qurilma koordinatalarini qanday aniqlaydi?
    </h2>
    <p class="lede" data-ru="JavaScript может запросить у спутников GPS и Wi-Fi вышек точные координаты широты (Latitude) и долготы (Longitude):" data-en="JavaScript interfaces with GPS satellites and Wi-Fi towers to fetch live Latitude and Longitude coordinates:">
      JavaScript orqali foydalanuvchining ruxsati bilan sun'iy yo'ldosh va Wi-Fi nuqtalari orqali joriy koordinatalarni olish mumkin:
    </p>
    <pre class="code-block">navigator.geolocation.getCurrentPosition(
  pos =&gt; {
    const lat = pos.coords.latitude;
    const lon = pos.coords.longitude;
    console.log(`Mening lokatsiyam: ${lat}, ${lon}`);
  },
  err =&gt; console.error("Ruxsat berilmadi:", err.message),
  { enableHighAccuracy: true, timeout: 5000 }
);</pre>
  </section>

  <!-- SLIDE 7: A* SEARCH OPTIMIZATION -->
  <section class="slide" data-phase="A* SEARCH|АЛГОРИТМ A*|A* SEARCH" data-time="4 min">
    <div class="eyebrow" data-ru="ЭВРИСТИЧЕСКИЙ ПОИСК" data-en="HEURISTIC SEARCH">
      A* (A-STAR) ALGORITMI
    </div>
    <h2 class="section-title" data-ru="Дейкстра + Компас: Поиск с направлением" data-en="Dijkstra + Compass: Directed Pathfinding">
      Dijkstra algoritmini kompas (evristika) bilan tezlashtirish
    </h2>
    <p class="lede" data-ru="Дейкстра ищет во все стороны равномерно, как круги на воде. A* добавляет «притяжение» к цели через формулу f(n) = g(n) + h(n):" data-en="Dijkstra expands equally in all directions like ripples. A* introduces directional guidance toward the target using f(n) = g(n) + h(n):">
      Dijkstra algoritmi suvga tushgan tosh kabi barcha tomonga teng tarqaladi. A* algoritmi esa manzil tomonga yo'naltiruvchi kompas qo'shadi:
    </p>
    <div class="text-cols">
      <div class="col-item">
        <span class="col-num">g(n)</span>
        <h3 class="col-title" data-ru="Пройденный путь" data-en="Traversed Cost">Bosib o'tilgan yo'l</h3>
        <p class="col-desc" data-ru="Точное расстояние от старта до текущей точки." data-en="Exact cost accumulated from start to current node.">Startdan hozirgi nuqtagacha aniq bosib o'tilgan masofa.</p>
      </div>
      <div class="col-item">
        <span class="col-num">h(n)</span>
        <h3 class="col-title" data-ru="Эвристика" data-en="Heuristic Estimate">Taxminiy masofa</h3>
        <p class="col-desc" data-ru="Расстояние по прямой (Haversine) от текущей точки до финиша." data-en="As-the-crow-flies distance from current node to destination.">Hozirgi nuqtadan manzilgacha to'g'ri chiziqli taxminiy masofa.</p>
      </div>
      <div class="col-item">
        <span class="col-num">f(n)</span>
        <h3 class="col-title" data-ru="Итоговый приоритет" data-en="Total Priority">Jami ustunlik</h3>
        <p class="col-desc" data-ru="Алгоритм исследует сначала те дороги, которые приближают к цели." data-en="Prioritizes pathways that steer directly toward the finish line.">Faqat manzil tomonga eltuvchi eng istiqbolli yo'llarni ko'radi.</p>
      </div>
    </div>
  </section>

  <!-- SLIDE 8: GPS STUDIO -->
  <section class="slide" data-phase="STUDIO|СТУДИЯ|STUDIO" data-time="4 min">
    <div class="eyebrow" data-ru="ИНТЕРАКТИВНАЯ КАРТА" data-en="INTERACTIVE MAP">
      GPS NAVIGATOR STUDIO
    </div>
    <h2 class="section-title" data-ru="Визуальный навигатор в studio/index.html" data-en="Visual Navigator in studio/index.html">
      Vizual simulyator: Marshrut chizish va tirbandlikni hisoblash
    </h2>
    <p class="lede" data-ru="В папке studio/index.html открывается интерактивная карта: вы кликаете две точки и видите, как алгоритм прокладывает зеленую линию кратчайшего пути." data-en="Launch studio/index.html to explore interactive map pathfinding: click two landmarks and watch the optimal path render in real time:">
      `studio/index.html` laboratoriyasida shahar xaritasi joylashgan: istalgan 2 ta nuqtani tanlab eng qisqa yo'lni qidiruvchi algoritmni jonli kuzating.
    </p>
    <ul class="big-list">
      <li><span class="num">01</span> <span data-ru="<strong>Визуализация графа:</strong> динамическое добавление ребер и изменение веса дороги." data-en="<strong>Graph Visualizer:</strong> dynamically adding vertices and adjusting road weights."><strong>Graf redaktori:</strong> yangi yo'llar qo'shish va ularning masofasini o'zgartirish.</span></li>
      <li><span class="num">02</span> <span data-ru="<strong>Симуляция пробок:</strong> увеличение веса дороги заставляет навигатор объезжать затор." data-en="<strong>Traffic Simulation:</strong> traffic bottlenecks dynamically reroute the navigator."><strong>Tirbandlik simulyatori:</strong> tirband ko'chani aylanib o'tishni avtomatik qayta hisoblash.</span></li>
    </ul>
  </section>

  <!-- SLIDE 9: QUIZ & FIX -->
  <section class="slide" data-phase="TEST|ТЕСТ|QUIZ &amp; FIX" data-time="5 min">
    <div class="eyebrow" data-ru="ИНТЕРАКТИВНЫЙ ТЕСТ" data-en="INTERACTIVE TEST &amp; FIX">
      JONLI KIBER-TEST VA YECHIM (FIX)
    </div>
    <h2 class="section-title" data-ru="Тест: Какой путь из A в D короче?" data-en="Quiz: Which Path from A to D is Optimal?">
      Sinov: Maktabdan (A) Stadionga (D) qaysi yo'l eng qisqa?
    </h2>
    <p class="lede" data-ru="Граф дорог: A-B=500, B-D=600, A-C=800, C-D=400, B-C=300. Выберите оптимальный маршрут:" data-en="Graph specs: A-B=500, B-D=600, A-C=800, C-D=400, B-C=300. Identify the shortest route:">
      Masofalar: A-B=500m, B-D=600m, A-C=800m, C-D=400m, B-C=300m. Eng qisqa yo'l qaysi?
    </p>
    <div class="quiz-box">
      <div class="quiz-option" onclick="checkQuiz(this, true)">
        <span class="num">A</span> <span data-ru="A ➔ B ➔ D = 1100 метров (500 + 600)." data-en="A ➔ B ➔ D = 1100 meters (500 + 600).">A ➔ B ➔ D = 1100 metr (500 + 600).</span>
      </div>
      <div class="quiz-option" onclick="checkQuiz(this, false)">
        <span class="num">B</span> <span data-ru="A ➔ C ➔ D = 1200 метров (800 + 400)." data-en="A ➔ C ➔ D = 1200 meters (800 + 400).">A ➔ C ➔ D = 1200 metr (800 + 400).</span>
      </div>
      <div class="quiz-option" onclick="checkQuiz(this, false)">
        <span class="num">C</span> <span data-ru="A ➔ B ➔ C ➔ D = 1200 метров (500 + 300 + 400)." data-en="A ➔ B ➔ C ➔ D = 1200 meters (500 + 300 + 400).">A ➔ B ➔ C ➔ D = 1200 metr (500 + 300 + 400).</span>
      </div>
    </div>
    <div class="test-actions">
      <button class="test-btn" onclick="toggleTestFix()" data-ru="Показать исправление (Fix)" data-en="Show Solution (Fix)">Yechimni ko'rish (Fix)</button>
    </div>
    <div class="fix-reveal" id="testFixBox">
      // MATEMATIK YECHIM (FIX):<br>
      // 1-yo'l: A ➔ B ➔ D = 500 + 600 = 1100m.<br>
      // 2-yo'l: A ➔ C ➔ D = 800 + 400 = 1200m.<br>
      // 3-yo'l: A ➔ B ➔ C ➔ D = 500 + 300 + 400 = 1200m.<br>
      // Eng qisqa marshrut: A ➔ B ➔ D (1100m).
    </div>
  </section>

  <!-- SLIDE 10: MISSIONS -->
  <section class="slide" data-phase="AMALIYOT|ПРАКТИКА|MISSIONS" data-time="8 min">
    <div class="eyebrow" data-ru="4 НАВИГАЦИОННЫХ ЗАДАНИЯ" data-en="4 NAVIGATION MISSIONS">
      AMALIYOT: 4 TA MUHANDISLIK TOPSHIRIG'I
    </div>
    <h2 class="section-title" data-ru="Практика в Studio: Проложи маршрут" data-en="Studio Practice: Chart Your Course">
      Studioda amaliyot: Shahar bo'ylab eng optimal yo'lni top
    </h2>
    <div class="text-cols">
      <div class="col-item">
        <span class="col-num">KVEST 01</span>
        <h3 class="col-title" data-ru="Построить граф" data-en="Build Graph">Graf qurish</h3>
        <p class="col-desc" data-ru="Добавьте 4 точки на карту и соедините их дорогами с реальными расстояниями." data-en="Place 4 landmarks and connect them with weighted road links.">Xaritada 4 ta joyni belgilang va ularni masofa bilan bog'lang.</p>
      </div>
      <div class="col-item">
        <span class="col-num">KVEST 02</span>
        <h3 class="col-title" data-ru="Запуск Дейкстры" data-en="Run Dijkstra">Dijkstra hisobi</h3>
        <p class="col-desc" data-ru="Выберите старт и финиш, наблюдайте пошаговую релаксацию ребер." data-en="Select start and finish; observe step-by-step edge relaxations.">Start va finishni tanlab algoritmni bosqichma-bosqich yurgizing.</p>
      </div>
      <div class="col-item">
        <span class="col-num">KVEST 03</span>
        <h3 class="col-title" data-ru="Объезд пробки" data-en="Avoid Traffic">Tirbandlikni aylanib o'tish</h3>
        <p class="col-desc" data-ru="Увеличьте вес дороги из-за пробки и найдите альтернативный объезд." data-en="Simulate a road bottleneck and evaluate the alternative detour.">Biror yo'lga probka berib, yangi qisqa yo'lni toping.</p>
      </div>
    </div>
  </section>

  <!-- SLIDE 11: RUBRIC -->
  <section class="slide" data-phase="BAHOLASH|ОЦЕНКА|RUBRIC" data-time="3 min">
    <div class="eyebrow" data-ru="10-БАЛЛЬНЫЙ СТАНДАРТ" data-en="10-POINT STANDARD">
      RASMIY BAHOLASH MEZONI
    </div>
    <h2 class="section-title" data-ru="Критерии оценки за урок (10 баллов)" data-en="Lesson Evaluation Rubric (10 Points)">
      10 ballik rasmiy baholash mezoni
    </h2>
    <ul class="big-list">
      <li><span class="num">01</span> <span data-ru="<strong>Теория графов (2.5 балла):</strong> понимание вершин, ребер и весов дорог." data-en="<strong>Graph Theory (2.5 pts):</strong> comprehension of vertices, edges, and road weights."><strong>Graf nazariyasi (2.5 ball):</strong> tugunlar, qirralar va yo'l vaznlarini tushunish.</span></li>
      <li><span class="num">02</span> <span data-ru="<strong>Алгоритм Дейкстры (2.5 балла):</strong> пошаговый поиск кратчайшего пути без ошибок." data-en="<strong>Dijkstra Logic (2.5 pts):</strong> tracing the shortest path iteratively without mistakes."><strong>Dijkstra algoritmi (2.5 ball):</strong> qadamma-qadam eng qisqa masofani to'g'ri topish.</span></li>
      <li><span class="num">03</span> <span data-ru="<strong>Формула Гаверсинуса (2.5 балла):</strong> расчет расстояния по сферическим координатам." data-en="<strong>Haversine Trigonometry (2.5 pts):</strong> computing distance between spherical GPS coordinates."><strong>Haversine formulasi (2.5 ball):</strong> GPS koordinatalari bo'yicha masofani hisoblash.</span></li>
      <li><span class="num">04</span> <span data-ru="<strong>Geolocation API и Studio (2.5 балла):</strong> получение координат и работа в Studio." data-en="<strong>Geolocation API &amp; Studio (2.5 pts):</strong> browser coordinate retrieval and workbench usage."><strong>Geolocation API va Studio (2.5 ball):</strong> brauzerda GPS olish va studioda marshrut qurish.</span></li>
    </ul>
  </section>

  <!-- SLIDE 12: SUMMARY -->
  <section class="slide" data-phase="XULOSA|ИТОГИ|SUMMARY" data-time="2 min">
    <div class="eyebrow" data-ru="ИТОГИ И МОСТ" data-en="SUMMARY &amp; NEXT STEP">
      XULOSA VA KEYINGI DARS
    </div>
    <h1 class="hero-title" data-ru="Готовы к рубежному контролю!" data-en="Ready for the Midterm Exam!">
      Oraliq Nazorat Imtihoniga Tayyorsiz!
    </h1>
    <p class="lede" data-ru="Вы освоили алгоритмы пространственной навигации. На следующем 30-уроке нас ждет итоговый рубежный контроль — Sport Simulyatori va O'yin Fizikasi!" data-en="You have conquered spatial pathfinding algorithms. Lesson 30 brings our Quarter 1 Midterm Exam: Sports Simulator &amp; Game Physics!">
      Siz eng muhim algoritmlardan biri bo'lgan navigatsiyani o'rgandingiz. Keyingi 30-darsda 1-chorak oraliq nazorati — Sport Simulyatori va O'yin Fizikasi imtihoni bo'lib o'tadi!
    </p>
    <ul class="big-list">
      <li><span class="num">✓</span> <span data-ru="<strong>Домашнее задание:</strong> выполните 4 задачи в vazifa.html и пройдите онлайн-тест." data-en="<strong>Homework:</strong> complete all 4 challenges in vazifa.html and take the online quiz."><strong>Uy vazifasi:</strong> vazifa.html dagi topshiriqlarni bajaring va test.html sinovidan o'ting.</span></li>
    </ul>
  </section>

</div>
"""

    notes = {
      "uz": [
        ["1-slayd: Kirish va Reja", "Bugun Google Maps va Yandex Go qanday ishlashini o'rganamiz: graf nazariyasi va algoritmlar.", "O'quvchilarda qiziqish uyg'oting."],
        ["2-slayd: Navigatsiya Muammosi", "Nega millionlab yo'llarni bittalab tekshirib bo'lmaydi? Graf vaznlari va tugunlarni tushuntiring.", "Doskada 3 ta nuqtani chizing."],
        ["3-slayd: Graf Kodda", "Adjacency List JavaScript ob'ekti yordamida qanday yozilishini ko'rsating.", "Ob'ekt sintaksisini tahlil qiling."],
        ["4-slayd: Dijkstra Algoritmi", "To'lqin tarqalishi kabi har doim eng yaqin ko'rilmagan tugun tanlanadi.", "Infinity qiymati nega kerakligini ayting."],
        ["5-slayd: Haversine Formulasi", "Yer tekis emas, sferik ekanligini va Pifagor formulasidagi xatolikni ko'rsating.", "Radius 6371 km ekanini eslating."],
        ["6-slayd: Geolocation API", "navigator.geolocation brauzerda qanday ishlashini ko'rsating.", "Ruxsat berish dialogini tushuntiring."],
        ["7-slayd: A* Algoritmi", "Dijkstra ga manzil tomon kompas qo'shilsa A* hosil bo'ladi.", "Evristika tushunchasini ayting."],
        ["8-slayd: GPS Studio", "studio/index.html da xaritani ochib yo'l chizishni buyuring.", "O'quvchilarga studioni ochishni ayting."],
        ["9-slayd: Jonli Kiber-Test", "Slayddagi masofalarni hisoblang va A-B-D yo'li 1100 metr ekanligini ko'rsating.", "Yechimni ko'rish tugmasini bosing."],
        ["10-slayd: Amaliy Topshiriqlar", "Studioda 3 ta topshiriqni bajarib yo'l chizishni nazorat qiling.", "Sinf bo'ylab aylanib yordam bering."],
        ["11-slayd: 10 Ballik Mezon", "Baholash shaffof: graf, Dijkstra, Haversine va GPS.", "Mezon talablarini o'qib bering."],
        ["12-slayd: Xulosa va Keyingi Dars", "Keyingi 30-darsda 1-chorak oraliq nazorati — Sport Simulyatori imtihoni bo'ladi.", "vazifa.html va test.html ni eslating."]
      ],
      "ru": [
        ["Слайд 1: Введение и План", "Сегодня мы разберем, как устроены навигаторы: теория графов и алгоритмы поиска пути.", "Озвучьте цели урока."],
        ["Слайд 2: Вызов Навигации", "Почему нельзя перебирать 10 млн дорог подряд? Понятия вершин, ребер и весов.", "Покажите структуру дорожной сети."],
        ["Слайд 3: Графы в JavaScript", "Список смежности на объектах JS — простой и эффективный способ хранения карты.", "Разберите структуру cityMap."],
        ["Слайд 4: Алгоритм Дейкстры", "Пошаговый выбор ближайшей вершины с релаксацией ребер.", "Покажите принцип нахождения кратчайшего пути."],
        ["Слайд 5: Формула Гаверсинуса", "Земля — геоид. Почему плоская геометрия ошибается на больших расстояниях.", "Разберите тригонометрическую формулу."],
        ["Слайд 6: Geolocation API", "Метод navigator.geolocation.getCurrentPosition запрашивает широту и долготу.", "Объясните получение геопозиции."],
        ["Слайд 7: Оптимизация A*", "A* добавляет эвристику направления h(n) к пройденному пути g(n).", "Сравните Дейкстру и A*."],
        ["Слайд 8: Студия GPS", "В studio/index.html интерактивная карта позволяет тестировать алгоритмы.", "Дайте команду открыть лабораторию."],
        ["Слайд 9: Интерактивный Тест", "Рассчитайте расстояния на слайде: A-B-D = 1100 м — самый короткий путь.", "Покажите решение."],
        ["Слайд 10: Практика в Студии", "Выполните квесты: постройте граф и симулируйте пробку.", "Контролируйте ход работы."],
        ["Слайд 11: 10-Балльный Критерий", "Оценка складывается из 4 компонентов по 2.5 балла.", "Озвучьте требования к выполнению заданий."],
        ["Слайд 12: Итоги и Экзамен", "На 30-м уроке нас ждет рубежный зачет — Спортивный симулятор и физика!", "Напомните о выполнении vazifa.html и онлайн-теста."]
      ],
      "en": [
        ["Slide 1: Intro & Goals", "Today we decode GPS navigators: graph theory and shortest path engines.", "Set an inspiring tone for the lesson."],
        ["Slide 2: Navigation Challenge", "Why brute-forcing 10M roads is impossible: vertices, edges, and traffic weights.", "Diagram intersections on board."],
        ["Slide 3: Graph in Code", "Adjacency lists in JavaScript objects represent maps efficiently.", "Inspect the cityMap syntax."],
        ["Slide 4: Dijkstra Pathfinding", "Dijkstra ripples outward, choosing the nearest unvisited node every step.", "Explain edge relaxation."],
        ["Slide 5: Haversine Formula", "Earth is curved: why planar Pythagorean math introduces errors.", "Review spherical trigonometry."],
        ["Slide 6: Geolocation API", "navigator.geolocation.getCurrentPosition retrieves device coordinates.", "Explain browser permission prompts."],
        ["Slide 7: A* Heuristics", "A* steers Dijkstra toward the goal using direction heuristics.", "Compare Dijkstra vs A*."],
        ["Slide 8: GPS Workbench", "Launch studio/index.html to interact with the map simulator.", "Prompt students to chart paths."],
        ["Slide 9: Interactive Quiz & Fix", "Evaluate routes A-B-D (1100m) vs A-C-D (1200m) and show fix.", "Solve together with the class."],
        ["Slide 10: 4 Hands-On Missions", "Build graphs, run algorithms, and route around simulated traffic jams.", "Support students hands-on."],
        ["Slide 11: 10-Point Rubric", "Grading criteria: graphs, Dijkstra, Haversine, and Geolocation API.", "Clarify grading thresholds."],
        ["Slide 12: Summary & Next Step", "Next week: Lesson 30 Midterm Exam — Sports Simulator & Game Physics!", "Direct students to vazifa.html and test.html."]
      ]
    }

    full_html = f"""<!DOCTYPE html>
<html lang="uz" data-theme="dark">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title data-ru="{html.escape(title['ru'])}" data-en="{html.escape(title['en'])}">{html.escape(title['uz'])}</title>
<link rel="icon" type="image/svg+xml" href="/assets/favicon.svg">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Manrope:wght@600;700;800&family=Source+Sans+3:wght@400;600;700&family=JetBrains+Mono:wght@400;600;700&display=swap">
{css_chunk}
</head>
<body>

{get_floating_elements(cohort_tag)}

{slides_html}

{get_modals()}

{get_js(notes)}

</body>
</html>
"""
    dest = os.path.join(folder, "prezentatsiya.html")
    with open(dest, "w", encoding="utf-8") as out:
        out.write(full_html)
    print(f"✓ Built {dest}")

build_lesson_29()

# 4. 5-6-sinf 21-dars: Raqamli Iz va Maxfiylik
def build_lesson_21():
    folder = "classes/5-6-sinf/7-hafta/21-dars-raqamli-iz-va-maxfiylik"
    cohort_tag = "5-6-SINF · WEEK 7"
    title = {
      "uz": "5–6-Sinf · 21-Dars: Raqamli Iz va Shaxsiy Maxfiylik: Internetda Xavfsiz Bo'lish",
      "ru": "5–6-Класс · Урок 21: Цифровой След и Личная Конфиденциальность: Безопасность в Сети",
      "en": "Grades 5–6 · Lesson 21: Digital Footprint & Personal Privacy: Staying Safe Online"
    }

    slides_html = """
<div class="stage">

  <!-- SLIDE 1: TITUL -->
  <section class="slide active" data-phase="KIRISH|ВВЕДЕНИЕ|INTRO" data-time="3 min">
    <div class="eyebrow" data-ru="5–6-КЛАСС · 7-Я НЕДЕЛЯ · УРОК 21" data-en="GRADES 5–6 · WEEK 7 · LESSON 21">
      5–6-SINF · 7-HAFTA · 21-DARS
    </div>
    <h1 class="hero-title" data-ru="Цифровой След и Личная Конфиденциальность" data-en="Digital Footprint &amp; Personal Privacy">
      Raqamli Iz va Shaxsiy Maxfiylik
    </h1>
    <p class="lede" data-ru="Что интернет помнит о нас: правило большого экрана (Billboard Rule), скрытые геометки в фотографиях (EXIF) и защита профиля в соцсетях." data-en="What the internet remembers about us: the Billboard Rule, hidden EXIF GPS location tags in photos, and social profile privacy hardening.">
      Internet biz haqimizda nimani eslab qoladi: Katta Ekran qoidasi (Billboard Rule), fotosuratlardagi yashirin EXIF GPS xavfi va shaxsiy maxfiylikni himoyalash.
    </p>
    <ul class="big-list">
      <li><span class="num">01</span> <span data-ru="<strong>След в сети:</strong> каждый клик, фото и комментарий остаются в интернете навсегда." data-en="<strong>Permanent Footprint:</strong> every tap, post, and photo leaves an indelible digital trace."><strong>O'chmas iz:</strong> internetga yuklangan har bir rasm va xabar butun umrga saqlanib qoladi.</span></li>
      <li><span class="num">02</span> <span data-ru="<strong>Скрытые опасности:</strong> как фото на смартфон может выдать точный домашний адрес злоумышленникам." data-en="<strong>Hidden Vulnerabilities:</strong> how ordinary smartphone snapshots leak exact home coordinates."><strong>Yashirin xavf:</strong> uydan olingan oddiy rasm begonalarga uyingiz manzilini qanday ochib qo'yadi.</span></li>
    </ul>
  </section>

  <!-- SLIDE 2: DIGITAL FOOTPRINT -->
  <section class="slide" data-phase="RAQAMLI IZ|ЦИФРОВОЙ СЛЕД|DIGITAL FOOTPRINT" data-time="3 min">
    <div class="eyebrow" data-ru="ПОНЯТИЕ СЛЕДА" data-en="TRACE DEFINITION">
      RAQAMLI IZ NIMA?
    </div>
    <h2 class="section-title" data-ru="Как следы на свежем снегу, но которые нельзя стереть" data-en="Like Footsteps in Snow That Never Melt">
      Qorda qolgan iz kabi, lekin uni hech qachon o'chirib bo'lmaydi
    </h2>
    <p class="statement" data-ru="Каждый раз, когда вы открываете сайт, ставите лайк или выкладываете фото, вы оставляете цифровой след. Даже если вы удалите пост, кто-то успеет сделать скриншот или сохранить копию в архиве." data-en="Every time you browse, post, or like, you stamp a digital footprint. Even if you hit delete, automated archives and screenshots preserve that data indefinitely.">
      Har gal sayt ochganingizda, layk bosganingizda yoki rasm qo'yganingizda raqamli iz qoldirasiz. Hatto postni o'chirib yuborsangiz ham, kimdir skrinshot olgan yoki robotlar arxivga saqlab qo'ygan bo'ladi.
    </p>
    <div class="text-cols">
      <div class="col-item">
        <span class="col-num">FAOL IZ</span>
        <h3 class="col-title" data-ru="Активный след" data-en="Active Footprint">Faol Raqamli Iz</h3>
        <p class="col-desc" data-ru="То, что вы публикуете сами: фото, сторис, комментарии, посты в каналах." data-en="Content you intentionally upload: photos, stories, comments, channel posts.">O'zingiz ataylab internetga qo'ygan rasmlar, videolar va izohlar.</p>
      </div>
      <div class="col-item">
        <span class="col-num">PASSIV IZ</span>
        <h3 class="col-title" data-ru="Пассивный след" data-en="Passive Footprint">Passiv Raqamli Iz</h3>
        <p class="col-desc" data-ru="То, что сайты собирают скрытно: IP-адрес, тип устройства, история переходов." data-en="Data captured silently: IP address, device specs, browsing cookies.">Saytlar bildirmasdan yig'adigan ma'lumotlar: IP manzil, qurilma modeli.</p>
      </div>
    </div>
  </section>

  <!-- SLIDE 3: BILLBOARD RULE -->
  <section class="slide" data-phase="QOIDA|ПРАВИЛО ЭКРАНА|BILLBOARD RULE" data-time="4 min">
    <div class="eyebrow" data-ru="ЗОЛОТОЕ ПРАВИЛО КИБЕРГИГИЕНЫ" data-en="GOLDEN RULE OF SAFETY">
      KATTA EKRAN QOIDASI (BILLBOARD RULE)
    </div>
    <h2 class="section-title" data-ru="Перед тем как нажать «Опубликовать»: Спроси себя!" data-en="Before Hitting 'Post': Ask Yourself!">
      «Ulashish» tugmasini bosishdan oldin o'zingizga savol bering!
    </h2>
    <p class="statement" data-ru="«Если это фото, сообщение или видео завтра появится на огромном мониторе у входа в мою школу на глазах у всех учителей, родителей и друзей — будет ли мне стыдно?»" data-en="'If this photo, video, or chat message appeared tomorrow on a gigantic billboard at the school gates before all teachers, parents, and friends — would I feel embarrassed?'">
      «Agar ushbu rasm, video yoki xabar ertaga maktabim darvozasidagi ulkan ekranda hamma o'qituvchilarim, ota-onam va do'stlarim ko'z o'ngida ko'rinsa — men uyalmaymanmi?»
    </p>
    <ul class="big-list">
      <li><span class="num">✓</span> <span data-ru="<strong>Если ответ «ДА, мне будет стыдно»:</strong> НЕМЕДЛЕННО УДАЛИТЕ и никогда не отправляйте!" data-en="<strong>If the answer is 'YES, I would feel bad':</strong> DELETE IT IMMEDIATELY and never post!"><strong>Agar javobingiz «HA, uyalaman» bo'lsa:</strong> UNI DARHOL O'CHIRING va hech qachon internetga qo'ymang!</span></li>
      <li><span class="num">✓</span> <span data-ru="<strong>Если ответ «НЕТ, я горжусь этим»:</strong> публиковать безопасно (учеба, победы, спорт)." data-en="<strong>If the answer is 'NO, I am proud of it':</strong> safe to share (awards, sports, learning)."><strong>Agar javobingiz «YO'Q, faxrlanaman» bo'lsa:</strong> bemalol ulashishingiz mumkin (yutuqlar, sport, bilim).</span></li>
    </ul>
  </section>

  <!-- SLIDE 4: EXIF METADATA IN PHOTOS -->
  <section class="slide" data-phase="EXIF|ГЕОМЕТКИ EXIF|EXIF METADATA" data-time="4 min">
    <div class="eyebrow" data-ru="НЕВИДИМЫЙ ШПИОН" data-en="INVISIBLE TRACKER">
      FOTOSURATLAR ICHIDAGI YASHIRIN EXIF
    </div>
    <h2 class="section-title" data-ru="Как фото котика выдает координаты вашей спальни" data-en="How a Pet Photo Leaks Your Home Address">
      Uydagi mushukcha rasmi uyingiz manzilini qanday oshkor qiladi?
    </h2>
    <p class="lede" data-ru="Когда смартфон делает снимок, камера автоматически записывает внутрь файла скрытые технические данные (EXIF):" data-en="Whenever smartphones snap photos, camera sensors inject hidden technical metadata (EXIF) inside the image payload:">
      Smartfoningizda rasmga olganingizda, kamera fayl ichiga ko'zga ko'rinmas maxfiy ma'lumotlarni (EXIF) yozib qo'yadi:
    </p>
    <div class="text-cols">
      <div class="col-item">
        <span class="col-num">GPS</span>
        <h3 class="col-title" data-ru="Точные координаты" data-en="Exact Location">Aniq GPS Lokatsiya</h3>
        <p class="col-desc" data-ru="Широта и долгота дома с точностью до 1 метра! Злоумышленник видит точку на карте." data-en="Latitude and longitude accurate within 1 meter! Strangers can pin your home.">Uyingizning aniq koordinatasi 1 metrgacha aniqlikda xaritada ko'rinadi!</p>
      </div>
      <div class="col-item">
        <span class="col-num">TIME</span>
        <h3 class="col-title" data-ru="Дата и время" data-en="Timestamp">Aniq Vaqt va Sana</h3>
        <p class="col-desc" data-ru="Когда именно сделан снимок: злоумышленник понимает, когда вас нет дома." data-en="Exact minute of capture: strangers learn when you leave home unattended.">Rasm qachon olingani: begona odam qachon uyda yo'qligingizni bilib oladi.</p>
      </div>
      <div class="col-item">
        <span class="col-num">DEVICE</span>
        <h3 class="col-title" data-ru="Модель телефона" data-en="Device Model">Qurilma Modeli</h3>
        <p class="col-desc" data-ru="iPhone 15 Pro, Samsung Galaxy S24 — модель помогает подобрать эксплойт." data-en="Hardware model details helping attackers target device-specific exploits.">Telefoningiz modeli: iPhone yoki Samsung modeli xakerlarga qo'l keladi.</p>
      </div>
    </div>
  </section>

  <!-- SLIDE 5: HOW TO STRIP EXIF -->
  <section class="slide" data-phase="HIMOYA|ОЧИСТКА EXIF|DEFENSE" data-time="4 min">
    <div class="eyebrow" data-ru="ПРАКТИЧЕСКАЯ ЗАЩИТА" data-en="PRACTICAL SHIELD">
      EXIF MA'LUMOTLARINI QANDAY O'CHIRAMIZ?
    </div>
    <h2 class="section-title" data-ru="2 простых шага, чтобы закрыть геолокацию" data-en="2 Simple Steps to Disable Geotagging">
      Geolokatsiyani o'chirishning 2 ta oson usuli
    </h2>
    <div class="text-cols">
      <div class="col-item">
        <span class="col-num">QADAM 01</span>
        <h3 class="col-title" data-ru="В настройках камеры" data-en="Camera Settings">Kamera Sozlamalari</h3>
        <p class="col-desc" data-ru="Зайдите в Настройки ➔ Камера ➔ Геопозиция ➔ выберите «Никогда»." data-en="Open Settings ➔ Camera ➔ Location ➔ select 'Never'.">Sozlamalar ➔ Kamera ➔ Joylashuv ➔ «Hech qachon» rejimini tanlang.</p>
      </div>
      <div class="col-item">
        <span class="col-num">QADAM 02</span>
        <h3 class="col-title" data-ru="При отправке фото" data-en="Sharing Settings">Yuborish Sozlamasi</h3>
        <p class="col-desc" data-ru="В Telegram отправляйте как обычное фото со сжатием — мессенджер сам очистит EXIF." data-en="In Telegram, send as compressed photo — the app strips EXIF tags automatically.">Telegramda rasmni fayl qilib emas, oddiy qisqartirilgan rasm sifatida yuboring.</p>
      </div>
    </div>
  </section>

  <!-- SLIDE 6: PUBLIC WI-FI DANGERS -->
  <section class="slide" data-phase="WI-FI|ОТКРЫТЫЙ WI-FI|PUBLIC WI-FI" data-time="4 min">
    <div class="eyebrow" data-ru="БЕСПЛАТНЫЙ СЫР В МЫШЕЛОВКЕ" data-en="TRAP OF FREE WI-FI">
      OCHIQ VA BEPUL WI-FI XATARLARI
    </div>
    <h2 class="section-title" data-ru="Почему открытый Wi-Fi в кафе опасен?" data-en="Why Unsecured Public Wi-Fi is Dangerous">
      Nega kafe va parkdagi parolsiz Wi-Fi ga ulanish xavfli?
    </h2>
    <p class="lede" data-ru="Открытая сеть не шифрует радиоволны. Любой человек за соседним столиком со специальной программой (Wireshark) может перехватить незащищенный трафик:" data-en="Open networks transmit unencrypted radio packets. Anyone nearby with a packet analyzer can intercept unencrypted sessions:">
      Parolsiz ochiq tarmoq to'lqinlarni shifrlamaydi. Yon stolingizda o'tirgan odam noutbukida barcha jo'natayotgan ma'lumotlaringizni ushlab olishi mumkin:
    </p>
    <ul class="big-list">
      <li><span class="num">01</span> <span data-ru="<strong>Никаких паролей:</strong> никогда не вводите пароли и номера карт в открытых сетях." data-en="<strong>Zero Passwords:</strong> never enter account credentials or bank cards on public Wi-Fi."><strong>Parollarni kiritmang:</strong> ochiq Wi-Fi da shaxsiy akkountlarga kirmang va to'lov qilmang.</span></li>
      <li><span class="num">02</span> <span data-ru="<strong>Всегда включайте VPN:</strong> надежный VPN шифрует весь интернет-трафик в защищенную трубу." data-en="<strong>Always Engage VPN:</strong> trusted VPN creates an encrypted tunnel shielding all packets."><strong>VPN ni yoqing:</strong> ishonchli VPN barcha ma'lumotlaringizni himoyalangan tunnelga oladi.</span></li>
    </ul>
  </section>

  <!-- SLIDE 7: PROFILE PRIVACY & 2FA -->
  <section class="slide" data-phase="2FA|ПРИВАТНОСТЬ И 2FA|PRIVACY &amp; 2FA" data-time="4 min">
    <div class="eyebrow" data-ru="ДВОЙНОЙ ЗАМОК" data-en="DOUBLE LOCK">
      YOPIQ PROFIL VA 2-BOSQICHLI HIMOYА (2FA)
    </div>
    <h2 class="section-title" data-ru="Закрываем профиль и включаем 2FA за 60 секунд" data-en="Private Profile &amp; 2FA in 60 Seconds">
      Profilingizni begonalardan 100% himoya qilish
    </h2>
    <div class="text-cols">
      <div class="col-item">
        <span class="col-num">QALQON 01</span>
        <h3 class="col-title" data-ru="Закрытый аккаунт" data-en="Private Profile">Yopiq Profil (Private)</h3>
        <p class="col-desc" data-ru="Ваши фото увидят только те, кого вы одобрили лично. Чужие люди не увидят ничего." data-en="Restricts your media exclusively to confirmed friends. Strangers see zero posts.">Rasmlaringizni faqat siz tasdiqlagan do'stlar ko'radi. Begonalar hech narsa ko'rmaydi.</p>
      </div>
      <div class="col-item">
        <span class="col-num">QALQON 02</span>
        <h3 class="col-title" data-ru="2FA Двухфакторка" data-en="Two-Factor Auth">2FA (Ikki Bosqich)</h3>
        <p class="col-desc" data-ru="Даже если кто-то узнает пароль, без SMS-кода или ключа войти невозможно." data-en="Even if your password is stolen, login fails without the second device confirmation code.">Hatto parolingizni bilib olishsa ham, telefoningizga keladigan maxfiy kodsiz kira olishmaydi.</p>
      </div>
    </div>
  </section>

  <!-- SLIDE 8: CYBER DETECTIVE STUDIO -->
  <section class="slide" data-phase="STUDIO|СТУДИЯ|STUDIO" data-time="4 min">
    <div class="eyebrow" data-ru="ИНТЕРАКТИВНЫЙ ДЕТЕКТИВ" data-en="CYBER DETECTIVE WORKBENCH">
      CYBER DETECTIVE STUDIO
    </div>
    <h2 class="section-title" data-ru="Интерактивный симулятор в studio/index.html" data-en="Interactive Simulator in studio/index.html">
      Vizual simulyator: Raqamli izingizni tekshiring
    </h2>
    <p class="lede" data-ru="В папке studio/index.html открывается лаборатория детектива: загрузите тестовое фото и посмотрите, какие скрытые данные в нем спрятаны!" data-en="Open studio/index.html to access the detective workbench: analyze sample photos to inspect hidden metadata:">
      `studio/index.html` laboratoriyasida kiber-detektiv studiyasi joylashgan: test rasmlarini tekshirib, ulardagi yashirin GPS koordinatalarini ochib tashlang!
    </p>
    <ul class="big-list">
      <li><span class="num">01</span> <span data-ru="<strong>EXIF Сканер:</strong> обнаружение GPS меток, модели камеры и точной даты съемки." data-en="<strong>EXIF Inspector:</strong> detecting GPS pins, camera specs, and shooting timestamps."><strong>EXIF skaneri:</strong> rasmdagi GPS nuqtani, telefon markasini va vaqtni topish.</span></li>
      <li><span class="num">02</span> <span data-ru="<strong>Очиститель данных:</strong> генерация очищенного безопасного файла в один клик." data-en="<strong>Privacy Cleaner:</strong> generating stripped sanitized image files with one click."><strong>Ma'lumot tozalagich:</strong> bir marta bosish bilan rasmni 100% xavfsiz qilish.</span></li>
    </ul>
  </section>

  <!-- SLIDE 9: QUIZ & FIX -->
  <section class="slide" data-phase="TEST|ТЕСТ|QUIZ &amp; FIX" data-time="5 min">
    <div class="eyebrow" data-ru="ИНТЕРАКТИВНЫЙ ТЕСТ" data-en="INTERACTIVE TEST &amp; FIX">
      JONLI KIBER-TEST VA YECHIM (FIX)
    </div>
    <h2 class="section-title" data-ru="Тест: Какую публикацию безопасно выложить?" data-en="Quiz: Which Post is 100% Safe to Share?">
      Sinov: Quyidagi postlardan qaysi birini internetga qo'yish xavfsiz?
    </h2>
    <div class="quiz-box">
      <div class="quiz-option" onclick="checkQuiz(this, false)">
        <span class="num">A</span> <span data-ru="Фото авиабилета в отпуск с четким штрих-кодом и фамилией." data-en="Photo of family boarding passes showing barcodes and passport info.">Oila bilan sayohatga bilet va pasport rasmi.</span>
      </div>
      <div class="quiz-option" onclick="checkQuiz(this, true)">
        <span class="num">B</span> <span data-ru="Фото диплома за победу в олимпиаде без домашнего адреса." data-en="Photo of academic competition award without home addresses.">Olimpiada musobaqasida olgan faxriy yorlig'imiz va diplomimiz.</span>
      </div>
      <div class="quiz-option" onclick="checkQuiz(this, false)">
        <span class="num">C</span> <span data-ru="Видео с видом из окна спальни с включенной геолокацией." data-en="Video showing bedroom window view with live GPS location tagged.">Uydagi xonamiz derazasidan olingan va joylashuvi ko'ringan video.</span>
      </div>
    </div>
    <div class="test-actions">
      <button class="test-btn" onclick="toggleTestFix()" data-ru="Показать исправление (Fix)" data-en="Show Solution (Fix)">Yechimni ko'rish (Fix)</button>
    </div>
    <div class="fix-reveal" id="testFixBox">
      // TO'G'RI JAVOB VA TUZATMA (FIX):<br>
      // 1. Chiptadagi shtrix-kod orqali firibgarlar barcha pasport ma'lumotlarini bilib oladi!<br>
      // 2. Deraza videosi uyingiz qayerdaligini ko'rsatib qo'yadi.<br>
      // 3. Yutuq va diplomlar esa sizning ijobiy va chiroyli raqamli izingizni yaratadi!
    </div>
  </section>

  <!-- SLIDE 10: MISSIONS -->
  <section class="slide" data-phase="AMALIYOT|ПРАКТИКА|MISSIONS" data-time="8 min">
    <div class="eyebrow" data-ru="3 ДЕТЕКТИВНЫХ ЗАДАНИЯ" data-en="3 DETECTIVE MISSIONS">
      AMALIYOT: 3 TA KIBER-DETEKTIV KVESTI
    </div>
    <h2 class="section-title" data-ru="Практика в Studio: Очисти свои фотографии" data-en="Studio Practice: Sanitize Your Media">
      Studioda amaliyot: Rasmlaringizni maxfiy xavflardan tozalang
    </h2>
    <div class="text-cols">
      <div class="col-item">
        <span class="col-num">KVEST 01</span>
        <h3 class="col-title" data-ru="Аудит фото" data-en="Audit Photo">Rasm tekshiruvi</h3>
        <p class="col-desc" data-ru="Загрузите тестовую фотографию и найдите в ней скрытые GPS координаты." data-en="Inspect sample image files and uncover hidden GPS coordinates.">Test rasmini yuklang va undagi yashirin GPS koordinatalarini toping.</p>
      </div>
      <div class="col-item">
        <span class="col-num">KVEST 02</span>
        <h3 class="col-title" data-ru="Очистка EXIF" data-en="Strip EXIF">EXIF tozalash</h3>
        <p class="col-desc" data-ru="Используйте кнопку очистки и проверьте, что геометка пропала." data-en="Use the strip tool to remove all location tags permanently.">Tozalash tugmasini bosib, GPS belgisi yo'qolganini tasdiqlang.</p>
      </div>
      <div class="col-item">
        <span class="col-num">KVEST 03</span>
        <h3 class="col-title" data-ru="Настройка 2FA" data-en="Enable 2FA">2FA tekshiruvi</h3>
        <p class="col-desc" data-ru="Проверьте безопасность своего аккаунта и включите двухфакторную защиту." data-en="Verify personal account security and enable two-factor protections.">Akkountingiz xavfsizligini tekshirib 2-bosqichli himoyani rejalashtiring.</p>
      </div>
    </div>
  </section>

  <!-- SLIDE 11: RUBRIC -->
  <section class="slide" data-phase="BAHOLASH|ОЦЕНКА|RUBRIC" data-time="3 min">
    <div class="eyebrow" data-ru="10-БАЛЛЬНЫЙ СТАНДАРТ" data-en="10-POINT STANDARD">
      RASMIY BAHOLASH MEZONI
    </div>
    <h2 class="section-title" data-ru="Критерии оценки за урок (10 баллов)" data-en="Lesson Evaluation Rubric (10 Points)">
      10 ballik rasmiy baholash mezoni
    </h2>
    <ul class="big-list">
      <li><span class="num">01</span> <span data-ru="<strong>Правило большого экрана (2.5 балла):</strong> оценка последствий публикаций в интернете." data-en="<strong>Billboard Rule (2.5 pts):</strong> evaluating online consequences before posting media."><strong>Katta Ekran qoidasi (2.5 ball):</strong> post qo'yishdan oldin oqibatlarini to'g'ri baholash.</span></li>
      <li><span class="num">02</span> <span data-ru="<strong>EXIF Метаданные (2.5 балла):</strong> нахождение скрытых геометок и их удаление." data-en="<strong>EXIF Metadata (2.5 pts):</strong> discovering hidden geotags and stripping coordinates."><strong>EXIF Metama'lumotlar (2.5 ball):</strong> yashirin GPS koordinatalarini topish va tozalash.</span></li>
      <li><span class="num">03</span> <span data-ru="<strong>Безопасный Wi-Fi (2.5 балла):</strong> соблюдение правил защиты в открытых сетях." data-en="<strong>Public Wi-Fi Safety (2.5 pts):</strong> applying cyber hygiene practices on public networks."><strong>Xavfsiz Wi-Fi (2.5 ball):</strong> ochiq tarmoqlarda shaxsiy ma'lumotlarni himoyalash.</span></li>
      <li><span class="num">04</span> <span data-ru="<strong>Приватность и 2FA (2.5 балла):</strong> закрытый профиль и настройка двухфакторки." data-en="<strong>Privacy &amp; 2FA (2.5 pts):</strong> private account configurations and 2FA deployment."><strong>Maxfiylik va 2FA (2.5 ball):</strong> profilni yopiq qilish va ikki bosqichli himoyani yoqish.</span></li>
    </ul>
  </section>

  <!-- SLIDE 12: SUMMARY -->
  <section class="slide" data-phase="XULOSA|ИТОГИ|SUMMARY" data-time="2 min">
    <div class="eyebrow" data-ru="ИТОГИ И МОСТ" data-en="SUMMARY &amp; NEXT STEP">
      XULOSA VA KEYINGI DARS
    </div>
    <h1 class="hero-title" data-ru="Вы — Настоящие Кибер-Детективы!" data-en="You are True Cyber Detectives!">
      Siz — Haqiqiy Kiber-Detektivsiz!
    </h1>
    <p class="lede" data-ru="Вы научились защищать свои данные и личную жизнь в интернете. На следующем 22-уроке нас ждет итоговый рубежный контроль — Kiber-Qalqon Viktorinasi!" data-en="You now master safeguarding personal data and privacy online. Lesson 22 brings our Quarter 1 Midterm Exam: Cyber Shield Tournament!">
      Siz internetda shaxsiy ma'lumotlar va oilaviy xavfsizlikni himoyalashni o'rgandingiz. Keyingi 22-darsda 1-chorak oraliq nazorati — Kiber-Qalqon Viktorinasi bo'lib o'tadi!
    </p>
    <ul class="big-list">
      <li><span class="num">✓</span> <span data-ru="<strong>Домашнее задание:</strong> выполните 4 задачи в vazifa.html и пройдите онлайн-тест." data-en="<strong>Homework:</strong> complete all 4 challenges in vazifa.html and take the online quiz."><strong>Uy vazifasi:</strong> vazifa.html dagi topshiriqlarni bajaring va test.html sinovidan o'ting.</span></li>
    </ul>
  </section>

</div>
"""

    notes = {
      "uz": [
        ["1-slayd: Kirish va Reja", "Bugun internetdagi raqamli izimiz va shaxsiy maxfiylikni o'rganamiz.", "O'quvchilarda qiziqish uyg'oting."],
        ["2-slayd: Raqamli Iz Nima?", "Qorda qolgan iz o'chadi, lekin internetdagi iz abadiy saqlanadi.", "Faol va passiv iz farqini ayting."],
        ["3-slayd: Katta Ekran Qoidasi", "Maktab darvozasidagi monitor metaforasi: uyalsang, aslo post qo'yma!", "Sinf bilan muhokama qiling."],
        ["4-slayd: EXIF Metama'lumotlari", "Kamera uydagi aniq koordinatani rasm ichiga yozib qo'yishini ko'rsating.", "GPS, sana va telefon modelini tushuntiring."],
        ["5-slayd: EXIF ni Tozalash", "Kamera sozlamalarida geolokatsiyani o'chirib qo'yish kerakligini ayting.", "2 ta oson qadamni ko'rsating."],
        ["6-slayd: Ochiq Wi-Fi Xavfi", "Kafe va parkdagi bepul Wi-Fi da xakerlar paketlarni ushlab olishi mumkin.", "VPN va parollarni kiritmaslikni uqtiring."],
        ["7-slayd: Yopiq Profil va 2FA", "Profilingizni 'Private' qilish va ikki bosqichli himoyani yoqish sirlari.", "2FA qo'shimcha kalit ekanini ayting."],
        ["8-slayd: Studio Laboratoriyasi", "studio/index.html ni ochib rasmdagi yashirin EXIF ni tekshirib ko'ring.", "Studioni ochishni buyuring."],
        ["9-slayd: Jonli Kiber-Test", "Qaysi post xavfsiz ekanligini toping va diplom post qilish xavfsizligini ayting.", "Yechimni ko'rish tugmasini bosing."],
        ["10-slayd: Detektiv Kvestlar", "Studioda rasmni skanerlash va tozalash amaliyotini o'tkazing.", "Sinf bo'ylab aylanib yordam bering."],
        ["11-slayd: 10 Ballik Mezon", "Baholash shaffof: Katta ekran qoidasi, EXIF, Wi-Fi va 2FA.", "Mezon talablarini o'qib bering."],
        ["12-slayd: Xulosa va Keyingi Dars", "Keyingi 22-darsda 1-chorak oraliq nazorati — Kiber-Qalqon viktorinasi bo'ladi.", "vazifa.html va test.html ni eslating."]
      ],
      "ru": [
        ["Слайд 1: Введение и План", "Сегодня мы изучим цифровой след и защиту личных данных в интернете.", "Озвучьте цели урока."],
        ["Слайд 2: Что Такое Цифровой След", "Следы на снегу тают, но цифровой след в интернете остается навсегда.", "Объясните активный и пассивный след."],
        ["Слайд 3: Правило Большого Экрана", "Если стыдно показать фото на мониторе у школы — не публикуй его!", "Обсудите правило с учениками."],
        ["Слайд 4: Метаданные EXIF", "Камера смартфона незаметно вшивает точные координаты спальни.", "Покажите поля GPS, даты и модели."],
        ["Слайд 5: Удаление EXIF", "Отключите геопозицию в настройках камеры телефона.", "Покажите 2 простых шага защиты."],
        ["Слайд 6: Опасность Открытого Wi-Fi", "Бесплатный Wi-Fi в кафе не шифрует радиоволны — используйте VPN.", "Предостерегите от ввода паролей."],
        ["Слайд 7: Приватность и 2FA", "Закрытый аккаунт и двухфакторка защищают профиль от угона.", "Объясните важность 2FA."],
        ["Слайд 8: Студия Детектива", "В studio/index.html можно загрузить фото и обнаружить геометку.", "Дайте команду открыть студию."],
        ["Слайд 9: Интерактивный Тест", "Разберите, почему диплом публиковать безопасно, а билеты — опасно.", "Покажите фикс."],
        ["Слайд 10: Практика в Студии", "Выполните аудит и очистку фотографий в интерактивном симуляторе.", "Контролируйте ход работы."],
        ["Слайд 11: 10-Балльный Критерий", "Оценка складывается из 4 компонентов по 2.5 балла.", "Озвучьте требования к выполнению заданий."],
        ["Слайд 12: Итоги и Экзамен", "На 22-м уроке нас ждет рубежная викторина «Кибер-Щит»!", "Напомните о выполнении vazifa.html и онлайн-теста."]
      ],
      "en": [
        ["Slide 1: Intro & Goals", "Today we explore our digital footprint and learn to protect privacy online.", "Set an encouraging and focused tone."],
        ["Slide 2: Digital Footprint Defined", "Footsteps in snow melt away, but internet footprints last forever.", "Contrast active vs passive trails."],
        ["Slide 3: The Billboard Rule", "If you'd be embarrassed seeing a post on a giant school monitor — never upload it!", "Engage in class dialogue."],
        ["Slide 4: Hidden EXIF Metadata", "Smartphone cameras quietly embed exact home coordinates into photos.", "Explain GPS, timestamp, and device tags."],
        ["Slide 5: Stripping EXIF Geotags", "Disable camera location permissions in phone settings.", "Outline the 2 simple steps."],
        ["Slide 6: Public Wi-Fi Hazards", "Unsecured open Wi-Fi lacks encryption: always engage a VPN.", "Caution against credential entry."],
        ["Slide 7: Account Hardening & 2FA", "Private profile settings and Two-Factor Authentication safeguard accounts.", "Explain 2FA secondary lock."],
        ["Slide 8: Cyber Detective Lab", "Launch studio/index.html to inspect and sanitize media metadata.", "Direct students to the simulator."],
        ["Slide 9: Interactive Quiz & Fix", "Evaluate why sharing awards is safe while boarding passes pose severe risks.", "Review choices together."],
        ["Slide 10: 3 Detective Quests", "Audit test media, scrub metadata, and configure account hardening.", "Support students hands-on."],
        ["Slide 11: 10-Point Rubric", "Grading criteria: billboard rule, EXIF metadata, Wi-Fi, and 2FA.", "Clarify grading thresholds."],
        ["Slide 12: Summary & Next Step", "Next week: Lesson 22 Midterm Exam — Cyber Shield Tournament!", "Direct students to vazifa.html and test.html."]
      ]
    }

    full_html = f"""<!DOCTYPE html>
<html lang="uz" data-theme="dark">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title data-ru="{html.escape(title['ru'])}" data-en="{html.escape(title['en'])}">{html.escape(title['uz'])}</title>
<link rel="icon" type="image/svg+xml" href="/assets/favicon.svg">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Manrope:wght@600;700;800&family=Source+Sans+3:wght@400;600;700&family=JetBrains+Mono:wght@400;600;700&display=swap">
{css_chunk}
</head>
<body>

{get_floating_elements(cohort_tag)}

{slides_html}

{get_modals()}

{get_js(notes)}

</body>
</html>
"""
    dest = os.path.join(folder, "prezentatsiya.html")
    with open(dest, "w", encoding="utf-8") as out:
        out.write(full_html)
    print(f"✓ Built {dest}")

build_lesson_21()
