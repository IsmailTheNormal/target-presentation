#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generator for 9-sinf 10-hafta 29-dars:
Zamonaviy JavaScript (ES6+): Modullar va Asinxron Chuqurlik
"""

import os
import json
import html

FOLDER = "classes/9-sinf/10-hafta/29-dars-es6-modullar-va-asinxron-chuqurlik"
os.makedirs(FOLDER, exist_ok=True)
os.makedirs(os.path.join(FOLDER, "lab"), exist_ok=True)

# Load CSS from 28-dars
with open("classes/9-sinf/8-hafta/28-dars-fullstack-xavfsiz-servis-oraliq-nazorat/prezentatsiya.html", "r", encoding="utf-8") as f:
    t28 = f.read()

css_chunk = t28[t28.find("<style>"):t28.find("</style>") + 8]

SLIDES = [
    # 1. Kirish
    {
        "phase": "KIRISH|ВВЕДЕНИЕ|INTRO",
        "eyebrow": {"uz": "9-SINF · 10-HAFTA · 29-DARS", "ru": "9 КЛАСС · 10-Я НЕДЕЛЯ · УРОК 29", "en": "GRADE 9 · WEEK 10 · LESSON 29"},
        "title": {"uz": "Zamonaviy JavaScript (ES6+): Modullar va Asinxron Chuqurlik", "ru": "Современный JavaScript (ES6+): Модули и Асинхронная Глубина", "en": "Modern JavaScript (ES6+): Modules and Asynchronous Depth"},
        "lede": {"uz": "2-Chorakda AI Agentlar va avtonom tizimlar dasturlashga tayyorlanamiz: modulli arxitektura va Event Loop mexanikasi!", "ru": "Во 2-й четверти готовимся к созданию AI-агентов: модульная архитектура и механика Event Loop!", "en": "Quarter 2 prepares us for AI Agents and autonomous systems: modular architecture & Event Loop mechanics!"},
        "body": """
<div class="cards-grid">
  <div class="card">
    <div class="badge" data-ru="Модули ES6" data-en="ES6 Modules">ES Modules</div>
    <h3 data-ru="Изоляция и Экспорт" data-en="Isolation & Export">Modulli Izolyatsiya</h3>
    <p data-ru="export и import заменяют глобальные переменные. Каждый файл — независимый микро-модуль." data-en="export and import eliminate global variable collisions. Each file is an isolated module.">export va import global o'zgaruvchilar to'qnashuvini yo'qotadi. Har bir fayl — mustaqil modul.</p>
  </div>
  <div class="card">
    <div class="badge" data-ru="Деструктуризация" data-en="Destructuring">ES6+ Shakar</div>
    <h3 data-ru="Синтаксическая мощь" data-en="Syntactic Elegance">Destructuring & Spread</h3>
    <p data-ru="const { id, role } = user и оператор расширения (...props) делают код лаконичным и надежным." data-en="const { id, role } = user and spread (...props) make your code expressive and bulletproof.">Obyektlarni bitta qatorda parchalash va spread (...) orqali xavfsiz klonlash imkoniyati.</p>
  </div>
  <div class="card">
    <div class="badge" data-ru="Результат урока" data-en="Lesson Deliverable">Dars natijasi</div>
    <h3 data-ru="Event Loop Движок" data-en="Event Loop Engine">Asinxron Arxitektura</h3>
    <p data-ru="Понимание Call Stack, Microtask Queue (Promises) и Macrotasks. Код без зависаний UI." data-en="Mastering Call Stack, Microtask Queue (Promises), and Macrotasks. Zero UI freeze.">Call Stack, Promises va Event Loop mexanizmini tushunib, toza async/await oqimini yozish.</p>
  </div>
</div>
""",
        "note": ["2-Chorak muhandislik poydevori", "9-sinflar 1-chorakda Full-Stack servis yaratdilar. Endi ularning vazifasi — kodni korporativ modullarga bo'lish va asinxron Event Loop-ni chuqur tushunish.", "Bu bilim 11-13 haftalarda AI agentlarni dasturlash uchun to'g'ridan-to'g'ri kalit hisoblanadi."]
    },

    # 2. Muammo
    {
        "phase": "MUAMMO|ПРОБЛЕМА|PROBLEM",
        "eyebrow": {"uz": "AQLIY HUJUM · MUAMMO", "ru": "МОЗГОВОЙ ШТУРМ · ПРОБЛЕМА", "en": "BRAINSTORMING · PROBLEM"},
        "title": {"uz": "Spaghetti Monolit Kod Nega Korporativ Loyihalarni O'ldiradi?", "ru": "Почему Код Спагетти-Монолита Убивает Корпоративные Проекты?", "en": "Why Does Spaghetti Monolithic Code Kill Enterprise Projects?"},
        "lede": {"uz": "Barcha funksiyalar bitta katta app.js fayliga (3000 qator) yozilsa, bitta o'zgaruvchi butun tizimni buzadi (Global Namespace Pollution).", "ru": "Когда 3000 строк кода сваливают в один app.js, одна глобальная переменная ломает всё приложение.", "en": "Dumping 3000 lines into a monolithic app.js pollutes global scope and leads to silent cascading failures."},
        "body": """
<div class="compare-grid">
  <div class="compare-card bad">
    <div class="badge-bad" data-ru="Глобальный хаос (До ES6)" data-en="Global Chaos (Pre-ES6)">Global Xaos (ES6 gacha)</div>
    <h4 data-ru="&lt;script src='a.js'&gt;&lt;script src='b.js'&gt;" data-en="&lt;script src='a.js'&gt;&lt;script src='b.js'&gt;">&lt;script src="a.js"&gt;&lt;script src="b.js"&gt;</h4>
    <p data-ru="Все переменные летят в window. Если в a.js есть 'let user' и в b.js есть 'let user' — сайт падает!" data-en="Variables leak into window. If both scripts declare 'let user', script execution crashes instantly!">Barcha o'zgaruvchilar bitta window ga tushadi. Ikkita faylda bir xil nom bo'lsa, butun sayt qulaydi.</p>
  </div>
  <div class="compare-card good">
    <div class="badge-good" data-ru="Модульный стандарт (ES6+)" data-en="Modular Standard (ES6+)">Modulli Standart (ES6+)</div>
    <h4 data-ru="import { fetchUser } from './api.js'" data-en="import { fetchUser } from './api.js'">import { fetchUser } from "./api.js"</h4>
    <p data-ru="Каждый модуль имеет закрытую область видимости (Scope). Наружу отдается только то, что помечено export." data-en="Every module has strict lexical scope. Only explicitly exported variables leave the boundary.">Har bir fayl o'z shaxsiy xotirasiga ega. Tashqariga faqat export qilingan narsalar chiqadi.</p>
  </div>
</div>
""",
        "note": ["Spaghetti kod xavfi", "O'quvchilardan so'rang: 'Agar 5 kishi bitta faylni tahrirlasa nima bo'ladi? Git konflikt va xatoliklar!'", "Modulli arxitektura jamoaviy ishlashning yagona to'g'ri yo'lidir."]
    },

    # 3. Konsept
    {
        "phase": "KONSEPT|КОНЦЕПТ|CONCEPT",
        "eyebrow": {"uz": "ARXITEKTURA · ASOS", "ru": "АРХИТЕКТУРА · ОСНОВА", "en": "ARCHITECTURE · CORE"},
        "title": {"uz": "ES Modules: Named Export vs Default Export", "ru": "ES Модули: Named Export против Default Export", "en": "ES Modules: Named Export vs Default Export"},
        "lede": {"uz": "JavaScript-da ma'lumotlarni eksport qilishning 2 xil professional usuli bor: Nomli va Standart (Default).", "ru": "В JavaScript есть 2 профессиональных способа экспорта данных: Именованный и По Умолчанию.", "en": "JavaScript provides 2 standard ways to export components: Named and Default exports."},
        "body": """
<div class="cards-grid">
  <div class="card">
    <div class="badge" data-ru="Именованный экспорт" data-en="Named Export">Named Export (Nomli)</div>
    <div class="code-snippet">
      <span style="color:#E67E22;">export const</span> API_URL = <span style="color:#00D68F;">"/api/v1"</span>;<br>
      <span style="color:#E67E22;">export function</span> <span style="color:#FFB703;">hash</span>(data) {{ ... }}<br><br>
      <span style="color:var(--ink-3);">// Import:</span><br>
      <span style="color:#E67E22;">import</span> {{ API_URL, hash }} <span style="color:#E67E22;">from</span> <span style="color:#00D68F;">"./utils.js"</span>;
    </div>
    <p data-ru="Имена должны точно совпадать (в фигурных скобках). Идеально для наборов функций." data-en="Names must match inside curly braces. Ideal for utility function suites.">Qavslar ichida aniq nom bilan chaqiriladi. Yordamchi funksiyalar uchun standart.</p>
  </div>
  <div class="card">
    <div class="badge" data-ru="Экспорт по умолчанию" data-en="Default Export">Default Export (Yagona)</div>
    <div class="code-snippet">
      <span style="color:#E67E22;">export default class</span> <span style="color:#FFB703;">Agent</span> {{ ... }}<br><br>
      <span style="color:var(--ink-3);">// Import (xohlagan nom bilan):</span><br>
      <span style="color:#E67E22;">import</span> MyAgent <span style="color:#E67E22;">from</span> <span style="color:#00D68F;">"./Agent.js"</span>;
    </div>
    <p data-ru="Один главный экспорт на файл (без фигурных скобок). Идеально для классов и сервисов." data-en="Single primary export per file (no braces). Ideal for major classes and services.">Faylda faqat bitta bo'ladi (jingalak qavssiz). Bosh xizmat yoki sinf uchun mos.</p>
  </div>
</div>
""",
        "note": ["Named va Default farqi", "Named exportda jingalak qavs {} shart, default exportda esa qavssiz xohlagan nom bilan import qilish mumkinligini ko'rsating.", "type='module' atributi HTML faylda bo'lishi shartligini ta'kidlang."]
    },

    # 4. Sxema
    {
        "phase": "ARXITEKTURA|АРХИТЕКТУРА|ARCHITECTURE",
        "eyebrow": {"uz": "INLINE SVG · MODULLAR GRAFI", "ru": "INLINE SVG · ГРАФ МОДУЛЕЙ", "en": "INLINE SVG · MODULE GRAPH"},
        "title": {"uz": "Zamonaviy Modullar Bog'lanishi Grafi (Dependency Graph)", "ru": "Граф Зависимостей Модулей (Dependency Graph)", "en": "Modern Module Dependency Graph"},
        "lede": {"uz": "Brauzer ilovani ishga tushirishdan oldin barcha import bog'lanishlarini daraxt (AST) qilib yig'adi.", "ru": "Перед запуском браузер собирает дерево всех связей импорта в единый граф.", "en": "Before runtime execution, the engine parses all import statements into a strict dependency graph."},
        "body": """
<div style="background:var(--panel-2); border:1px solid var(--rule); border-radius:12px; padding:18px; margin-bottom:12px; text-align:center;">
  <svg viewBox="0 0 520 200" style="max-width:100%; height:auto;">
    <!-- Entry point: app.js -->
    <rect x="200" y="15" width="120" height="42" fill="var(--accent)" rx="6" />
    <text x="260" y="40" fill="#FFF" font-family="JetBrains Mono" font-size="13" font-weight="700" text-anchor="middle">app.js (Entry)</text>

    <!-- Connectors -->
    <path d="M 230 57 L 90 120" stroke="var(--ink-2)" stroke-width="2" marker-end="url(#arrow)" />
    <path d="M 260 57 L 260 120" stroke="var(--ink-2)" stroke-width="2" marker-end="url(#arrow)" />
    <path d="M 290 57 L 430 120" stroke="var(--ink-2)" stroke-width="2" marker-end="url(#arrow)" />

    <!-- Modules -->
    <rect x="30" y="120" width="120" height="42" fill="var(--panel)" stroke="var(--rule)" stroke-width="1.5" rx="6" />
    <text x="90" y="145" fill="var(--ink)" font-family="JetBrains Mono" font-size="12" font-weight="700" text-anchor="middle">api.js</text>

    <rect x="200" y="120" width="120" height="42" fill="var(--panel)" stroke="var(--rule)" stroke-width="1.5" rx="6" />
    <text x="260" y="145" fill="var(--ink)" font-family="JetBrains Mono" font-size="12" font-weight="700" text-anchor="middle">cart.js</text>

    <rect x="370" y="120" width="120" height="42" fill="var(--panel)" stroke="var(--rule)" stroke-width="1.5" rx="6" />
    <text x="430" y="145" fill="var(--ink)" font-family="JetBrains Mono" font-size="12" font-weight="700" text-anchor="middle">ui.js</text>

    <!-- Sub connector -->
    <path d="M 90 162 L 90 180 L 260 180" stroke="var(--ink-3)" stroke-width="1.5" stroke-dasharray="3" />
    <text x="175" y="192" fill="var(--ink-3)" font-family="JetBrains Mono" font-size="10">config.js</text>
  </svg>
</div>
""",
        "note": ["Graflar bilan tushuntirish", "app.js butun loyihaning kirish nuqtasi (Entry Point) hisoblanadi.", "Boshqa fayllar esa mustaqil mikroxizmatlar kabi alohida yuklanadi."]
    },

    # 5. Mexanizm: Destructuring & Spread
    {
        "phase": "MEXANIZM|МЕХАНИЗМ|MECHANISM",
        "eyebrow": {"uz": "ES6+ SINTAKSIS QUDRATI", "ru": "СИНТАКСИС ES6+", "en": "ES6+ SYNTACTIC POWER"},
        "title": {"uz": "Destructuring va Spread/Rest: Toza va Qisqa Kod", "ru": "Деструктуризация и Spread/Rest: Чистый и Краткий Код", "en": "Destructuring and Spread/Rest: Clean and Expressive"},
        "lede": {"uz": "Obyekt va massivlar bilan ishlashda 10 qatorlik eski kodni 1 qatorlik nafis sintaksisga almashtiramiz.", "ru": "Заменяем 10 строк громоздкого кода на одну изящную строку ES6+.", "en": "Replace 10 verbose lines of legacy code with one elegant line of modern ES6+ syntax."},
        "body": """
<div class="box-grid" style="display:grid; grid-template-columns:1fr 1fr; gap:12px;">
  <div class="card">
    <h4 data-ru="1. Деструктуризация (Destructuring)" data-en="1. Destructuring">1. Destructuring (Parchalash)</h4>
    <div class="code-snippet">
      <span style="color:#E67E22;">const</span> order = {{ id: <span style="color:#00D68F;">101</span>, amount: <span style="color:#00D68F;">450</span>, status: <span style="color:#00D68F;">"paid"</span> }};<br><br>
      <span style="color:var(--ink-3);">// Eski usul: order.id, order.amount...</span><br>
      <span style="color:var(--ink-3);">// Yangi ES6+ usuli:</span><br>
      <span style="color:#E67E22;">const</span> {{ id, amount }} = order;<br>
      console.log(id, amount);
    </div>
  </div>
  <div class="card">
    <h4 data-ru="2. Spread / Rest оператор (...)" data-en="2. Spread / Rest operator (...)">2. Spread / Rest operatori (...)</h4>
    <div class="code-snippet">
      <span style="color:#E67E22;">const</span> defaultSettings = {{ theme: <span style="color:#00D68F;">"dark"</span>, sound: <span style="color:#E67E22;">true</span> }};<br>
      <span style="color:#E67E22;">const</span> userCustom = {{ sound: <span style="color:#E67E22;">false</span> }};<br><br>
      <span style="color:var(--ink-3);">// Obyektlarni xavfsiz birlashtirish:</span><br>
      <span style="color:#E67E22;">const</span> final = {{ ...defaultSettings, ...userCustom }};<br>
      <span style="color:var(--ink-3);">// final -> {{ theme: "dark", sound: false }}</span>
    </div>
  </div>
</div>
""",
        "note": ["Destructuring siri", "O'quvchilarga qanday qilib `...` operatori obyektning barcha xususiyatlarini yoyib chiqishini ko'rsating.", "Bu obyektni to'g'ridan-to'g'ri o'zgartirmasdan (immutability) yangi nusxa olish uchun eng xavfsiz usuldir."]
    },

    # 6. Event Loop
    {
        "phase": "MEXANIZM|МЕХАНИЗМ|MECHANISM",
        "eyebrow": {"uz": "ASINXRON YADRO", "ru": "АСИНХРОННОЕ ЯДРО", "en": "ASYNC ENGINE"},
        "title": {"uz": "Event Loop: JavaScript Qanday Qilib Qotib Qolmaydi?", "ru": "Event Loop: Как JavaScript Не Зависает?", "en": "Event Loop: How JavaScript Avoids Freezing"},
        "lede": {"uz": "JavaScript bitta oqimli (Single-Threaded). Serverdan javob kelguncha kutib o'tirmasdan, keyingi ishlarni bajaradi.", "ru": "JavaScript однопоточен. Он не ждет ответа от сервера, а сразу выполняет следующие задачи.", "en": "JavaScript is single-threaded. It never blocks on I/O, executing subsequent tasks immediately."},
        "body": """
<div class="cards-grid">
  <div class="card">
    <div class="badge" data-ru="1. Стек вызовов" data-en="1. Call Stack">1. Call Stack (Sinxron)</div>
    <h3 data-ru="Мгновенный код" data-en="Immediate Code">Navbatdagi amallar</h3>
    <p data-ru="Обычные математические расчеты и вызовы функций выполняются немедленно по очереди (LIFO)." data-en="Synchronous functions and calculations execute immediately in LIFO order.">Oddiy funksiyalar va hisoblar zudlik bilan bittalab bajariladi va o'chiriladi.</p>
  </div>
  <div class="card">
    <div class="badge" data-ru="2. Очередь микрозадач" data-en="2. Microtask Queue">2. Microtask (Promises)</div>
    <h3 data-ru="Высший приоритет" data-en="Top Priority">VIP Asinxron Oqim</h3>
    <p data-ru="Promise.then() и await имеют наивысший приоритет среди асинхронных операций!" data-en="Promise.then() and await have the highest async execution priority!">Serverdan ma'lumot kelganda, Promises birinchi navbatda navbatdan o'tadi.</p>
  </div>
  <div class="card">
    <div class="badge" data-ru="3. Очередь макрозадач" data-en="3. Macrotask Queue">3. Macrotask (Timers)</div>
    <h3 data-ru="Таймеры и клики" data-en="Timers and Clicks">setTimeout & Hodisalar</h3>
    <p data-ru="setTimeout и события UI ждут, пока полностью освободится Call Stack и Microtasks." data-en="setTimeout and UI events wait until both Call Stack and Microtasks are empty.">Taymerlar va foydalanuvchi tugma bosishlari oxirgi navbatda ijro etiladi.</p>
  </div>
</div>
""",
        "note": ["Event Loop iyerarxiyasi", "O'quvchilarga navbatni tushuntiring: 1) Call Stack (sinxron), 2) Microtask (Promise), 3) Macrotask (setTimeout).", "Bu tartibni bilish kiber-dasturchi uchun juda muhim."]
    },

    # 7. async/await vs Callbacks
    {
        "phase": "TAQQOSLASH|СРАВНЕНИЕ|COMPARISON",
        "eyebrow": {"uz": "EVOLYUTSIYA · REFAKTORING", "ru": "ЭВОЛЮЦИЯ · РЕФАКТОРИНГ", "en": "EVOLUTION · REFACTORING"},
        "title": {"uz": "Callback Do'zaxi (Hell) vs async / await", "ru": "Ад Коллбэков (Callback Hell) vs async / await", "en": "Callback Hell vs async / await"},
        "lede": {"uz": "Ilgari 3 ta API ketma-ket chaqirilsa, kod o'ng tomonga qarab piramida bo'lib ketardi. async/await buni tozaladi.", "ru": "Раньше 3 последовательных вызова API превращались в лесенку. async/await сделал код линейным.", "en": "Sequential API chains used to create pyramid indentation. async/await flattens this completely."},
        "body": """
<div class="compare-grid">
  <div class="compare-card bad">
    <div class="badge-bad" data-ru="Callback Hell (Eski usul)" data-en="Callback Hell (Legacy)">Callback Hell (Eski usul)</div>
    <div class="code-snippet">
      getUser((u) =&gt; {{<br>
      &nbsp;&nbsp;getOrders(u.id, (o) =&gt; {{<br>
      &nbsp;&nbsp;&nbsp;&nbsp;calcTotal(o, (t) =&gt; {{<br>
      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;render(t); <span style="color:#FF1100;">// Xatoni ushlash azob!</span><br>
      &nbsp;&nbsp;&nbsp;&nbsp;}});<br>
      &nbsp;&nbsp;}});<br>
      }});
    </div>
  </div>
  <div class="compare-card good">
    <div class="badge-good" data-ru="async / await (Zamonaviy)" data-en="async / await (Modern)">async / await (Zamonaviy)</div>
    <div class="code-snippet">
      <span style="color:#0066FF;">async function</span> <span style="color:#FFB703;">loadData</span>() {{<br>
      &nbsp;&nbsp;<span style="color:#E67E22;">const</span> user = <span style="color:#0066FF;">await</span> getUser();<br>
      &nbsp;&nbsp;<span style="color:#E67E22;">const</span> orders = <span style="color:#0066FF;">await</span> getOrders(user.id);<br>
      &nbsp;&nbsp;<span style="color:#E67E22;">const</span> total = <span style="color:#0066FF;">await</span> calcTotal(orders);<br>
      &nbsp;&nbsp;render(total);<br>
      }}
    </div>
  </div>
</div>
""",
        "note": ["Sintaktik qulaylik", "async/await kodni xuddi oddiy sinxron koddek qator-ba-qator o'qilishini ta'minlaydi.", "Lekin tagida baribir Promise va Event Loop ishlayotganini unutmang."]
    },

    # 8. Xavfsizlik: try/catch
    {
        "phase": "XAVFSIZLIK|БЕЗОПАСНОСТЬ|SAFETY",
        "eyebrow": {"uz": "XATOLARNI BOSHQARISH", "ru": "ОБРАБОТКА ОШИБОК", "en": "ERROR HANDLING"},
        "title": {"uz": "Asinxron Xatolarni Tutish: try / catch / finally", "ru": "Перехват Асинхронных Ошибок: try / catch / finally", "en": "Catching Async Errors: try / catch / finally"},
        "lede": {"uz": "Tarmoq uzilsa yoki server 500 qaytarsa, sayt o'lib qolmasligi uchun har bir await try/catch blokiga olinishi shart.", "ru": "При падении сети или 500 ошибке сервера сайт не должен ломаться — нужен блок try/catch.", "en": "Network drops or 500 errors must not crash the app — every await call demands try/catch wraps."},
        "body": """
<div class="cards-grid">
  <div class="card">
    <div class="badge-bad" data-ru="Без защиты (Краш)" data-en="Uncaught Error">Himoyasiz So'rov</div>
    <div class="code-snippet">
      <span style="color:#E67E22;">const</span> res = <span style="color:#0066FF;">await</span> fetch(<span style="color:#00D68F;">"/api/pay"</span>);<br>
      <span style="color:#E67E22;">const</span> data = <span style="color:#0066FF;">await</span> res.json();
    </div>
    <p data-ru="Если интернет пропал, выскочит Uncaught TypeError и интерфейс навсегда зависнет!" data-en="If network fails, Uncaught TypeError triggers and freezes the UI indefinitely!">Internet o'chsa, xatolik ushlanmay qoladi va sahna to'xtab qoladi.</p>
  </div>
  <div class="card" style="border-left:4px solid var(--ok);">
    <div class="badge-good" data-ru="Корпоративный стандарт" data-en="Production Standard">Mustahkam Qalqon</div>
    <div class="code-snippet">
      <span style="color:#0066FF;">try</span> {{<br>
      &nbsp;&nbsp;showSpinner(<span style="color:#E67E22;">true</span>);<br>
      &nbsp;&nbsp;<span style="color:#E67E22;">const</span> res = <span style="color:#0066FF;">await</span> fetch(<span style="color:#00D68F;">"/api/pay"</span>);<br>
      &nbsp;&nbsp;<span style="color:#0066FF;">return await</span> res.json();<br>
      }} <span style="color:#0066FF;">catch</span> (err) {{<br>
      &nbsp;&nbsp;showToast(<span style="color:#FF1100;">"To'lovda xatolik yuz berdi"</span>);<br>
      }} <span style="color:#0066FF;">finally</span> {{<br>
      &nbsp;&nbsp;showSpinner(<span style="color:#E67E22;">false</span>);<br>
      }}
    </div>
    <p data-ru="finally гарантированно снимет спиннер загрузки при любом исходе!" data-en="finally always dismisses the loading spinner regardless of errors!">finally har qanday holatda ham yuklanish spinnerrini to'xtatadi.</p>
  </div>
</div>
""",
        "note": ["finally bloki ahamiyati", "finally nima uchun kerak? Server xato bersa ham yuklanish animatsiyasi to'xtashi va foydalanuvchi qayta urinishi uchun.", "Bu korporativ darajadagi dasturlash madaniyatidir."]
    },

    # 9. Viktorina (Quiz & Fix)
    {
        "phase": "TEST|ТЕСТ|QUIZ",
        "eyebrow": {"uz": "KIBER-TEST · EVENT LOOP", "ru": "КИБЕР-ТЕСТ · EVENT LOOP", "en": "CYBER-QUIZ · EVENT LOOP"},
        "title": {"uz": "Viktorina: Konsolga Qaysi Ketma-ketlikda Ma'lumot Chiqadi?", "ru": "Викторина: В Каком Порядке Выведется Лог в Консоль?", "en": "Quiz: What is the Output Order in the Console?"},
        "lede": {"uz": "Quyidagi kodni tahlil qiling: Call Stack, Microtasks va Macrotasks qonuniyatini eslang.", "ru": "Проанализируйте код: вспомните порядок Call Stack, Microtasks и Macrotasks.", "en": "Analyze the execution order: recall Call Stack, Microtasks and Macrotasks."},
        "body": """
<div class="code-snippet" style="margin-bottom:12px;">
console.log("1");<br>
setTimeout(() =&gt; console.log("2"), 0);<br>
Promise.resolve().then(() =&gt; console.log("3"));<br>
console.log("4");
</div>
<div class="quiz-box">
  <div class="quiz-option" onclick="checkQuiz(this, false)">
    <span>A)</span> <span>1 -> 2 -> 3 -> 4</span>
  </div>
  <div class="quiz-option" onclick="checkQuiz(this, true)">
    <span>B)</span> <span>1 -> 4 -> 3 -> 2</span>
  </div>
  <div class="quiz-option" onclick="checkQuiz(this, false)">
    <span>C)</span> <span>1 -> 3 -> 4 -> 2</span>
  </div>
  <div class="quiz-option" onclick="checkQuiz(this, false)">
    <span>D)</span> <span>4 -> 1 -> 3 -> 2</span>
  </div>
</div>
<div style="margin-top:14px; text-align:center;">
  <button class="dock-btn" onclick="toggleTestFix()" style="padding:8px 16px; font-weight:700;" data-ru="Показать решение (Fix)" data-en="Reveal Solution (Fix)">💡 Yechimni Ko'rish (Fix)</button>
</div>
<div id="testFixBox" style="display:none; margin-top:12px; background:var(--panel-2); border:1px solid var(--ok); border-radius:8px; padding:12px;">
  <b style="color:var(--ok);" data-ru="Правильный ответ: B (1 -> 4 -> 3 -> 2)!" data-en="Correct Answer: B (1 -> 4 -> 3 -> 2)!">To'g'ri javob: B (1 -> 4 -> 3 -> 2)!</b>
  <p style="margin:4px 0 0;" data-ru="1 и 4 выполняются синхронно в Call Stack. Затем очищается очередь Microtasks (Promise.then -> 3). И только потом из Macrotask очереди запускается таймер (setTimeout -> 2)!" data-en="1 and 4 execute synchronously on the Call Stack. Then the Microtask Queue flushes (Promise.then -> 3). Lastly, the Macrotask timer fires (setTimeout -> 2)!">1 va 4 Call Stack-da darhol sinxron bajariladi. So'ngra Microtask navbati (Promise.then -> 3) ishlaydi. Eng oxirida esa Macrotask navbatidan setTimeout -> 2 ishga tushadi!</p>
</div>
""",
        "note": ["Event Loop imtihon savoli", "Ushbu savol Google, Amazon va Meta dasturchilik suhbatlarida eng ko'p beriladigan klassik savoldir.", "O'quvchilarga to'g'ri tushuntirib, ularning bilimini mustahkamlang."]
    },

    # 10. Amaliy topshiriq
    {
        "phase": "AMALIYOT|ПРАКТИКА|PRACTICE",
        "eyebrow": {"uz": "FULL-STACK MISSIYA · 15 DAQIQA", "ru": "FULL-STACK МИССИЯ · 15 МИНУТ", "en": "FULL-STACK MISSION · 15 MINUTES"},
        "title": {"uz": "Laboratoriya: 3 Ta Modulli Asinxron Valyuta Xizmati", "ru": "Лаборатория: 3-Модульный Асинхронный Сервис Валют", "en": "Lab: 3-Module Asynchronous Currency Engine"},
        "lede": {"uz": "Kodni 3 ta toza ES6 moduliga ajratamiz: api.js (so'rovlar), format.js (matnlar) va app.js (markaziy oqim).", "ru": "Разделяем код на 3 чистых модуля ES6: api.js (запросы), format.js (форматирование) и app.js.", "en": "Split application into 3 clean ES6 modules: api.js (fetch), format.js (helpers), and app.js."},
        "body": """
<div class="cards-grid">
  <div class="card">
    <div class="badge" data-ru="1. api.js" data-en="1. api.js">1. api.js Moduli</div>
    <h3 data-ru="Named Export" data-en="Named Export">fetchRates() funksiyasi</h3>
    <p data-ru="CBU yoki CoinGecko API dan kurslarni tortuvchi va xatolarni try/catch qiluvchi asinxron funksiya." data-en="Async function fetching rates from API with built-in try/catch resilience.">Jonli API kurslarini asinxron tortuvchi va export qilingan fetchRates funksiyasi.</p>
  </div>
  <div class="card">
    <div class="badge" data-ru="2. format.js" data-en="2. format.js">2. format.js Moduli</div>
    <h3 data-ru="Destructuring" data-en="Destructuring">Formatlash funksiyasi</h3>
    <p data-ru="Destructuring orqali kelgan kurs obyektidan { rate, diff } ni ajratib, chiroyli matn qaytaradi." data-en="Extracts { rate, diff } via destructuring and formats human-readable currency badges.">Obyektdan { rate, diff } ni ajratib olib, chiroyli so'm valyutasiga aylantiradi.</p>
  </div>
  <div class="card">
    <div class="badge" data-ru="3. app.js" data-en="3. app.js">3. app.js Moduli</div>
    <h3 data-ru="Entry Point" data-en="Entry Point">Birlashtiruvchi Bosh Modul</h3>
    <p data-ru="Ikkala modulni import qilib, ekranga jonli asinxron kartochkalarni chiqaradi." data-en="Imports both modules and orchestrates live asynchronous UI rendering.">Boshqa modullarni import qilib, ma'lumotlarni asinxron yuklaydi va ekranga chizadi.</p>
  </div>
</div>
""",
        "note": ["Modulli topshiriq", "HTML faylda &lt;script type='module' src='app.js'&gt;&lt;/script&gt; yozilishi shartligini unutmang.", "VS Code Live Server bilan ochish kerak, oddiy fayl protokolida (file://) CORS xatosi berishi mumkin."]
    },

    # 11. Baholash mezoni
    {
        "phase": "BAHOLASH|ОЦЕНКА|GRADING",
        "eyebrow": {"uz": "10 BALLIK MEZON", "ru": "10-БАЛЛЬНАЯ ШКАЛА", "en": "10-POINT RUBRIC"},
        "title": {"uz": "Bugungi Darsni Baholash Mezonlari", "ru": "Критерии Оценки за Сегодняшний Урок", "en": "Today's Lesson Evaluation Rubric"},
        "lede": {"uz": "Har bir amaliy topshiriq professional kod madaniyati talablari asosida baholanadi.", "ru": "Каждое задание оценивается по стандартам чистого кода и надежности.", "en": "Every engineering task evaluated against professional clean code guidelines."},
        "body": """
<div class="rubric-grid" style="display:grid; grid-template-columns:repeat(4, 1fr); gap:10px;">
  <div class="card" style="text-align:center;">
    <div style="font-family:'JetBrains Mono'; font-size:20px; font-weight:800; color:var(--accent);">3 Ball</div>
    <b data-ru="ES Modules" data-en="ES Modules">Modullar Arxitekturasi</b>
    <p style="font-size:12px; margin-top:4px;" data-ru="export и import применены корректно, нет глобального scope." data-en="export/import applied without global scope leaks.">export va import to'g'ri ajratilgan, global xaos yo'q.</p>
  </div>
  <div class="card" style="text-align:center;">
    <div style="font-family:'JetBrains Mono'; font-size:20px; font-weight:800; color:var(--accent);">3 Ball</div>
    <b data-ru="async / await" data-en="async / await">Asinxron Oqim & Xatolar</b>
    <p style="font-size:12px; margin-top:4px;" data-ru="try / catch / finally защищает от сбоев сети." data-en="try/catch/finally protects from network drops.">async/await va try/catch to'liq sozlangan.</p>
  </div>
  <div class="card" style="text-align:center;">
    <div style="font-family:'JetBrains Mono'; font-size:20px; font-weight:800; color:var(--accent);">2 Ball</div>
    <b data-ru="Destructuring" data-en="Destructuring">Destructuring & Spread</b>
    <p style="font-size:12px; margin-top:4px;" data-ru="const { a, b } и оператор ... использованы чисто." data-en="const { a, b } and ... used expressively.">Obyektlar toza destructuring qilingan.</p>
  </div>
  <div class="card" style="text-align:center;">
    <div style="font-family:'JetBrains Mono'; font-size:20px; font-weight:800; color:var(--accent);">2 Ball</div>
    <b data-ru="Интерактив" data-en="Interactivity">Jonli UI va Spinners</b>
    <p style="font-size:12px; margin-top:4px;" data-ru="Интерфейс не зависает при загрузке данных." data-en="UI remains smooth and responsive during load.">Ma'lumot yuklanayotganda ekran qotmaydi.</p>
  </div>
</div>
""",
        "note": ["Baholash reglamenti", "O'quvchilar kodi toza bo'lishi va modullarga bo'lingan bo'lishi kerak.", "Barcha 4 mezonni bajarganlarga 10 ball qo'yiladi."]
    },

    # 12. Xulosa
    {
        "phase": "XULOSA|ИТОГ|SUMMARY",
        "eyebrow": {"uz": "UY VAZIFASI · AMALIYOT", "ru": "ДОМАШНЕЕ ЗАДАНИЕ · ПРАКТИКА", "en": "HOMEWORK · PRACTICE"},
        "title": {"uz": "Xulosa va Mustaqil Muhandislik Vazifasi", "ru": "Итог и Домашнее Задание", "en": "Summary & Homework Mission"},
        "lede": {"uz": "Bugun siz korporativ JavaScript poydevorini o'zlashtirdingiz! Keyingi darsda qayta ishlatiluvchi UI Komponentlar tizimini quramiz.", "ru": "Вы освоили фундамент корпоративного JS! На следующем уроке строим архитектуру компонентов.", "en": "You mastered corporate JavaScript foundations! Next lesson we construct reusable UI Components."},
        "body": """
<div class="cards-grid">
  <div class="card">
    <div class="badge" data-ru="Итог" data-en="Summary">Dars xulosasi</div>
    <h3 data-ru="ES6+ и Event Loop" data-en="ES6+ & Event Loop">ES6+ va Event Loop</h3>
    <p data-ru="Модули изолируют память, а Event Loop гарантирует плавную работу асинхронных операций." data-en="Modules isolate scope while Event Loop ensures butter-smooth async execution.">Modullar xotirani izolyatsiya qiladi, Event Loop esa asinxron ilovaning silliq ishlashini ta'minlaydi.</p>
  </div>
  <div class="card" style="border-left:4px solid var(--accent);">
    <div class="badge-good" data-ru="Домашнее задание" data-en="Homework Mission">Mustaqil Topshiriq</div>
    <h3 data-ru="Портал 'vazifa.html'" data-en="Portal 'vazifa.html'">'vazifa.html' topshiriqlari</h3>
    <p data-ru="Выполните 4 инженерных задания: рефакторинг спагетти-кода, Event Loop анализ и промисы." data-en="Complete 4 engineering tasks: spaghetti refactor, Event Loop trace, and robust Promises.">Portalda 4 ta kiber-topshiriqni bajaring: monolitni modullarga bo'lish, Event Loop tahlili va try/catch.</p>
  </div>
</div>
""",
        "note": ["Keyingi darsga o'tish", "11-haftada 'Komponentlar Falsafasi' mavzusi bo'ladi: React va zamonaviy freymvorklarning yadrosi tushuntiriladi.", "Darsni yuqori kayfiyatda yakunlang!"]
    }
]

SLIDE_TIMES = [
    '00-03|00-03|00-03', '03-07|03-07|03-07', '07-11|07-11|07-11', '11-15|11-15|11-15',
    '15-18|15-18|15-18', '18-21|18-21|18-21', '21-24|21-24|21-24', '24-27|24-27|24-27',
    '27-31|27-31|27-31', '31-36|31-36|31-36', '36-38|36-38|36-38', '38-40|38-40|38-40'
]

slides_html = ""
notes_dict = {"uz": [], "ru": [], "en": []}

for idx, s in enumerate(SLIDES):
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
    notes_dict["uz"].append([s["note"][0], s["note"][1], s["note"][2]])
    notes_dict["ru"].append([s["note"][0], s["note"][1], s["note"][2]])
    notes_dict["en"].append([s["note"][0], s["note"][1], s["note"][2]])

def get_floating_elements():
    return """
<a href="../../../../index.html" class="floating-brand" title="Bosh sahifa / Home" data-title-ru="Главная страница / Home" data-title-en="Home Page">
  <img src="{LOGO_DATA_URI}" alt="Target Logo" class="logo-img">
  <span class="tag">9A 9B · VIBECODING</span>
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
  slides.forEach(function(s, idx) {{ s.classList.toggle("active", idx === currentSlide); }});
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

function nextSlide() {{ if (currentSlide < totalSlides - 1) {{ currentSlide++; updateSlideView(); }} }}
function prevSlide() {{ if (currentSlide > 0) {{ currentSlide--; updateSlideView(); }} }}

function setLang(lang) {{
  currentLang = lang;
  try {{ localStorage.setItem("target_lang", lang); }} catch(e) {{}}
  document.documentElement.lang = lang;

  document.querySelectorAll(".dock-btn.lang-btn").forEach(function(b) {{
    b.classList.toggle("active", b.getAttribute("data-lang") === lang);
  }});

  document.querySelectorAll("[data-ru], [data-en]").forEach(function(el) {{
    if (!el.getAttribute("data-uz-orig")) el.setAttribute("data-uz-orig", el.innerHTML);
    if (lang === "uz") el.innerHTML = el.getAttribute("data-uz-orig");
    else if (lang === "ru" && el.getAttribute("data-ru")) el.innerHTML = el.getAttribute("data-ru");
    else if (lang === "en" && el.getAttribute("data-en")) el.innerHTML = el.getAttribute("data-en");
  }});

  updateSlideView();
}}

function toggleTheme() {{
  var cur = document.documentElement.getAttribute("data-theme") || "dark";
  var next = cur === "dark" ? "light" : "dark";
  document.documentElement.setAttribute("data-theme", next);
  try {{ localStorage.setItem("target_theme", next); }} catch(e) {{}}
}}

function toggleNotes() {{ document.getElementById("notesModal").classList.toggle("active"); }}
function toggleHelp() {{ document.getElementById("helpModal").classList.toggle("active"); }}

function checkQuiz(el, isCorrect) {{
  var box = el.parentElement;
  box.querySelectorAll(".quiz-option").forEach(function(opt) {{ opt.classList.remove("correct", "wrong"); }});
  if (isCorrect) el.classList.add("correct");
  else el.classList.add("wrong");
}}

function toggleTestFix() {{
  var box = document.getElementById("testFixBox");
  if (box) box.style.display = (box.style.display === "block") ? "none" : "block";
}}

document.addEventListener("keydown", function(e) {{
  if (e.target.tagName === "INPUT" || e.target.tagName === "TEXTAREA") return;
  if (e.key === "ArrowRight" || e.key === " ") {{ e.preventDefault(); nextSlide(); }}
  else if (e.key === "ArrowLeft") {{ e.preventDefault(); prevSlide(); }}
  else if (e.key === "l" || e.key === "L") {{
    var order = ["uz", "ru", "en"];
    setLang(order[(order.indexOf(currentLang) + 1) % 3]);
  }} else if (e.key === "t" || e.key === "T") {{ toggleTheme(); }}
  else if (e.key === "n" || e.key === "N") {{ toggleNotes(); }}
  else if (e.key === "?" || e.key === "/") {{ toggleHelp(); }}
  else if (e.key === "Escape") {{
    document.querySelectorAll(".notes-modal.active").forEach(function(m){{ m.classList.remove("active"); }});
  }}
}});

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
  <title data-ru="Урок 29: Современный JS (ES6+) — Модули и Async" data-en="Lesson 29: Modern JS (ES6+) — Modules and Async">29-dars: Zamonaviy JavaScript (ES6+) — Modullar va Asinxron Chuqurlik</title>
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

print("✅ Prezentatsiya generated for 9-sinf 29-dars")

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
<title data-ru="Урок 29: Современный JavaScript (ES6+) — Рабочий лист" data-en="Lesson 29: Modern JavaScript (ES6+) — Worksheet">29-dars: Zamonaviy JavaScript (ES6+) — Amaliy Ish Varaqasi</title>
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
    <span data-ru="9-Класс · Урок 29" data-en="Grade 9 · Lesson 29">9-sinf · 29-dars</span>
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
        <h1 data-ru="ES6+: Модули и Асинхронность" data-en="ES6+: Modules & Asynchrony">Zamonaviy JavaScript (ES6+): Modullar va Asinxronlik</h1>
        <div class="header-meta" data-ru="2-я четверть · 10-я неделя · 29-й урок · 9-класс" data-en="Quarter 2 · Week 10 · Lesson 29 · Grade 9">2-Chorak · 10-hafta · 29-dars · 9-sinf Full-Stack Track</div>
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
      <p data-ru="Декомпозировать спагетти-код на строгие ES6 модули, освоить деструктуризацию и оператор расширения (...), разобрать фазы Event Loop и построить надежные асинхронные цепочки try/catch." data-en="Deconstruct spaghetti scripts into rigid ES6 modules, master destructuring and spread (...), analyze Event Loop phase queues, and construct hardened async try/catch pipelines.">Spaghetti monolit kodni qat'iy ES6 modullariga ajratish, destructuring va spread operatorini o'zlashtirish, Event Loop navbatlarini tahlil qilish va mustahkam asinxron try/catch konveyerini qurish.</p>
    </div>

    <div class="sec-title">
      <span class="num">01</span>
      <span data-ru="Архитектура ES6+: Сопоставьте концепцию и ее код" data-en="ES6+ Architecture: Match Concept and Code Implementation">ES6+ Arxitekturasi: Tushuncha va kodni juftlang</span>
    </div>
    <div class="box-grid">
      <div class="box">
        <h4 data-ru="Концепции ES6+" data-en="ES6+ Concepts">ES6+ Tushunchalari</h4>
        <p><b>1. Named Export</b> — <span data-ru="Экспорт конкретной функции" data-en="Export specific function">Nomli funksiya eksporti</span></p>
        <p><b>2. Destructuring</b> — <span data-ru="Извлечение ключей объекта" data-en="Object key unpacking">Obyekt kalitlarini ajratish</span></p>
        <p><b>3. Spread (...)</b> — <span data-ru="Слияние объектов без мутации" data-en="Immutable object merge">Obyektlarni nusxalash</span></p>
        <p><b>4. Microtask</b> — <span data-ru="Очередь Promise.then()" data-en="Promise.then() queue">Promise asinxron navbati</span></p>
      </div>
      <div class="box">
        <h4 data-ru="Синтаксическая Запись" data-en="Syntax Notation">Sintaksis Namunasi</h4>
        <p data-ru="[ &nbsp; ] const {{ id, title }} = product;" data-en="[ &nbsp; ] const {{ id, title }} = product;">[ &nbsp; ] const {{ id, title }} = product;</p>
        <p data-ru="[ &nbsp; ] export const fetchUsers = () => { ... };" data-en="[ &nbsp; ] export const fetchUsers = () => { ... };">[ &nbsp; ] export const fetchUsers = () => { ... };</p>
        <p data-ru="[ &nbsp; ] const clone = {{ ...original, active: true }};" data-en="[ &nbsp; ] const clone = {{ ...original, active: true }};">[ &nbsp; ] const clone = {{ ...original, active: true }};</p>
        <p data-ru="[ &nbsp; ] Promise.resolve().then(() => run());" data-en="[ &nbsp; ] Promise.resolve().then(() => run());">[ &nbsp; ] Promise.resolve().then(() => run());</p>
      </div>
    </div>

    <div class="sec-title">
      <span class="num">02</span>
      <span data-ru="Анализ Event Loop: Порядок вывода в консоль" data-en="Event Loop Analysis: Console Execution Order">Event Loop Tahlili: Konsolga chiqish tartibi</span>
    </div>
    <div class="code-snippet">
      console.log("ALPHA");<br>
      setTimeout(() =&gt; console.log("BETA"), 0);<br>
      Promise.resolve().then(() =&gt; console.log("GAMMA"));<br>
      console.log("DELTA");
    </div>
    <p style="font-size:8.4pt; color:var(--ink-2); margin:4px 0;" data-ru="Вопрос: Запишите точный порядок вывода (ALPHA, BETA, GAMMA, DELTA) и объясните, почему BETA выводится последней." data-en="Question: Write the exact output order (ALPHA, BETA, GAMMA, DELTA) and explain why BETA prints last.">Savol: Konsolga chiqish tartibini yozing va nima uchun BETA (setTimeout) oxirida chiqishini tushuntiring.</p>
    <div class="write-line"></div>
    <div class="write-line"></div>
  </div>

  <div class="sheet-footer">
    <span>TARGET INTERNATIONAL SCHOOL · VIBECODING 9</span>
    <span data-ru="Страница 1 из 2" data-en="Page 1 of 2">1-bet / 2</span>
  </div>
</div>

<!-- PAGE 2 -->
<div class="sheet">
  <div>
    <div class="brandrule"></div>
    <header>
      <div>
        <h1 data-ru="Практическая Лаборатория и Рубрика" data-en="Practical Lab & Rubric">Amaliy Muhandislik va Baholash</h1>
        <div class="header-meta" data-ru="Модульное разделение и надежный асинхронный код" data-en="Modular decomposition and hardened async code">Modulli ajratish va mustahkam asinxron kod</div>
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
      <span data-ru="4 Инженерных Задания на Компьютере" data-en="4 Hands-on Engineering Tasks">Kompyuterda 4 ta Muhandislik Topshirig'i</span>
    </div>

    <div class="box" style="margin-bottom:6px;">
      <h4 data-ru="1-Topshiriq: Named vs Default Export (3 Ball)" data-en="Task 1: Named vs Default Export (3 Points)">1-Topshiriq: Named vs Default Export (3 Ball)</h4>
      <p data-ru="utils.js faylidan formatCurrency funksiyasini Named export, Database sinfini esa Default export qilib yozing:" data-en="In utils.js, export formatCurrency as Named export and Database class as Default export:">utils.js faylidan formatCurrency funksiyasini Named export, Database sinfini esa Default export qilib yozing:</p>
      <div class="write-line"></div>
    </div>

    <div class="box" style="margin-bottom:6px;">
      <h4 data-ru="2-Topshiriq: async / await va try/catch/finally (3 Ball)" data-en="Task 2: async / await and try/catch/finally (3 Points)">2-Topshiriq: async / await va try/catch/finally (3 Ball)</h4>
      <p data-ru="fetchUsers() funksiyasini yozing: spinnerni yoqish, fetch chaqiruvi, xatolikda toast ko'rsatish va finally da spinnerni o'chirish:" data-en="Write fetchUsers(): toggle spinner, await fetch, catch toast, and always dismiss spinner in finally:">fetchUsers() funksiyasini yozing: spinnerni yoqish, fetch chaqiruvi, xatolikda toast ko'rsatish va finally da spinnerni o'chirish:</p>
      <div class="write-line"></div>
    </div>

    <div class="box" style="margin-bottom:6px;">
      <h4 data-ru="3-Topshiriq: Obyektlarni Klonlash va Spread (2 Ball)" data-en="Task 3: Object Cloning & Spread (2 Points)">3-Topshiriq: Obyektlarni Klonlash va Spread (2 Ball)</h4>
      <p data-ru="Nega user2 = user1 xavfli va uni o'rniga user2 = {{ ...user1 }} yozilishi shartligini tushuntiring:" data-en="Explain why user2 = user1 mutates state dangerously and why user2 = {{ ...user1 }} is mandatory:">Nega user2 = user1 xavfli va uning o'rniga user2 = {{ ...user1 }} yozilishi shartligini tushuntiring:</p>
      <div class="write-line"></div>
    </div>

    <div class="box" style="margin-bottom:8px;">
      <h4 data-ru="4-Topshiriq: type='module' ning Ahamiyati (2 Ball)" data-en="Task 4: Importance of type='module' (2 Points)">4-Topshiriq: type='module' ning Ahamiyati (2 Ball)</h4>
      <p data-ru="Agar HTML faylda &lt;script src='app.js'&gt; yozilib, type='module' qo'yilmasa, brauzer qanday xatolik beradi?" data-en="If &lt;script src='app.js'&gt; omits type='module', what fatal runtime error is thrown?">Agar HTML faylda &lt;script src='app.js'&gt; yozilib, type='module' qo'yilmasa, brauzer qanday xatolik beradi?</p>
      <div class="write-line"></div>
    </div>

    <div class="sec-title">
      <span class="num">04</span>
      <span data-ru="10-Балльная Шкала Оценки" data-en="10-Point Evaluation Rubric">10 Ballik Rasmiy Baholash Mezoni</span>
    </div>
    <div class="rubric-grid">
      <div class="rubric-card">
        <b>3 Ball</b>
        <span data-ru="Модули: Синтаксис export/import" data-en="Modules: export/import syntax">Modullar: export/import toza</span>
      </div>
      <div class="rubric-card">
        <b>3 Ball</b>
        <span data-ru="Async: try/catch/finally" data-en="Async: try/catch/finally">Asinxron: try/catch qalqoni</span>
      </div>
      <div class="rubric-card">
        <b>2 Ball</b>
        <span data-ru="ES6+: Destructuring & Spread" data-en="ES6+: Destructuring & Spread">ES6+: Destructuring ishlatilgan</span>
      </div>
      <div class="rubric-card">
        <b>2 Ball</b>
        <span data-ru="Теория: Знание Event Loop" data-en="Theory: Event Loop knowledge">Nazariya: Event Loop to'g'ri</span>
      </div>
    </div>
  </div>

  <div class="sheet-footer">
    <span>TARGET INTERNATIONAL SCHOOL · VIBECODING 9</span>
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

print("✅ Varaqa generated for 9-sinf 29-dars")

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
<title data-ru="Современный JS (ES6+) — Домашнее Задание" data-en="Modern JS (ES6+) — Homework">Zamonaviy JavaScript (ES6+): Modullar — Mustaqil Uy Vazifasi</title>
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
    <span class="cohort-badge">9A 9B · UY VAZIFASI</span>
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
    <div class="hero-eyebrow" data-ru="9-КЛАСС · 10-Я НЕДЕЛЯ · УРОК 29" data-en="GRADE 9 · WEEK 10 · LESSON 29">9-SINF · 10-HAFTA · 29-DARS</div>
    <h1 class="hero-title" data-ru="Zamonaviy JavaScript (ES6+) — Mustaqil Amaliy Vazifa" data-en="Modern JavaScript (ES6+) — Homework Assignment">Zamonaviy JavaScript (ES6+): Modullar — Amaliy Vazifa</h1>
    <p class="hero-subtitle" data-ru="ES модули, деструктуризация, глубокий анализ Event Loop и отказоустойчивые асинхронные пайплайны." data-en="ES modules, destructuring, in-depth Event Loop analysis, and fault-tolerant async pipelines.">ES modullar, destructuring, Event Loop chuqur tahlili va xatolarga chidamli asinxron konveyerlar.</p>
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
          <option value="9A">9A</option>
          <option value="9B">9B</option>
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
        <h2 class="task-title" data-ru="1. Рефакторинг Спагетти-Кода в ES Модули" data-en="1. Refactoring Spaghetti Monolith to ES Modules">1. Monolit Kodni Toza ES Modullarga Ajratish</h2>
      </div>
      <div class="task-score">2.5 Ball</div>
    </div>
    <p class="task-desc" data-ru="Разработчик свалил в один файл логику расчета налогов, обращение к базе данных и отправку SMS. Как разделить этот код на 3 модуля (taxCalculator.js, dbService.js, notifyService.js)? Напишите примеры export и import." data-en="A developer combined tax calculations, database queries, and SMS dispatches into one script. How should this be divided into 3 modules (taxCalculator.js, dbService.js, notifyService.js)? Provide export/import examples.">Dasturchi soliq hisobi, ma'lumotlar bazasi so'rovlari va SMS yuborishni bitta faylga aralashtirib yozgan. Ushbu logikani 3 ta alohida modulga qanday ajratish kerak? export va import misollarini yozing.</p>
    <textarea class="task-textarea" id="task1_ans" placeholder="Modullarga ajratish rejasini va kod namunalarini yozing..." data-placeholder-ru="Напишите план разделения и примеры кода..." data-placeholder-en="Write splitting plan and code examples..." oninput="autoSave()"></textarea>
    <div style="margin-top:10px;">
      <button class="nav-btn" onclick="toggleFix('fix1')" data-ru="💡 Показать решение (Fix)" data-en="💡 Reveal Solution (Fix)">💡 Yechimni ko'rish (Fix)</button>
      <div id="fix1" class="fix-box" style="display:none; margin-top:8px; padding:10px; background:var(--panel-2); border-left:3px solid var(--ok); border-radius:4px;">
        <b style="color:var(--ok);" data-ru="Эталонное решение:" data-en="Reference Solution:">Etalon Yechim:</b>
        <p style="margin:4px 0 0;" data-ru="1) taxCalculator.js: export function calcTax(amount) {{ return amount * 0.12; }}<br>2) dbService.js: export default class Database {{ ... }}<br>3) notifyService.js: export async function sendSMS(phone, msg) {{ ... }}<br>В app.js: import Database, {{ calcTax }} ... Чистая изоляция без глобального мусора!" data-en="1) taxCalculator.js: export function calcTax(amount) {{ return amount * 0.12; }}<br>2) dbService.js: export default class Database {{ ... }}<br>3) notifyService.js: export async function sendSMS(phone, msg) {{ ... }}<br>In app.js: import Database, {{ calcTax }} ... Pristine modular separation!">1) taxCalculator.js: export function calcTax(amount) {{ return amount * 0.12; }}<br>2) dbService.js: export default class Database {{ ... }}<br>3) notifyService.js: export async function sendSMS(phone, msg) {{ ... }}<br>app.js da esa: import Database from "./dbService.js"; import {{ calcTax }} from "./taxCalculator.js"; Har bir modul o'z sohasiga javob beradi!</p>
      </div>
    </div>
  </article>

  <!-- TASK 2 -->
  <article class="task-card">
    <div class="task-header">
      <div>
        <span class="task-num">Topshiriq 2</span>
        <h2 class="task-title" data-ru="2. Анализ Очередей Event Loop: Microtasks против Macrotasks" data-en="2. Event Loop Queue Analysis: Microtasks vs Macrotasks">2. Event Loop Navbatlari: Microtasks va Macrotasks</h2>
      </div>
      <div class="task-score">2.5 Ball</div>
    </div>
    <p class="task-desc" data-ru="Почему Promise.resolve().then() выполняется раньше, чем setTimeout(() => {{}}, 0), даже если у таймера задержка 0 миллисекунд? Объясните механизм работы очередей Event Loop." data-en="Why does Promise.resolve().then() execute before setTimeout(() => {{}}, 0) even with zero millisecond delay? Explain the Event Loop queue dispatching mechanism.">Nega hatto kechikish 0 millisekund bo'lsa ham, Promise.resolve().then() har doim setTimeout(() => {{}}, 0) dan oldin bajariladi? Event Loop navbatlari mexanizmini tushuntiring.</p>
    <textarea class="task-textarea" id="task2_ans" placeholder="Event Loop ishlash mexanizmini tushuntiring..." data-placeholder-ru="Объясните работу очередей Event Loop..." data-placeholder-en="Explain Event Loop queues..." oninput="autoSave()"></textarea>
    <div style="margin-top:10px;">
      <button class="nav-btn" onclick="toggleFix('fix2')" data-ru="💡 Показать решение (Fix)" data-en="💡 Reveal Solution (Fix)">💡 Yechimni ko'rish (Fix)</button>
      <div id="fix2" class="fix-box" style="display:none; margin-top:8px; padding:10px; background:var(--panel-2); border-left:3px solid var(--ok); border-radius:4px;">
        <b style="color:var(--ok);" data-ru="Эталонное решение:" data-en="Reference Solution:">Etalon Yechim:</b>
        <p style="margin:4px 0 0;" data-ru="В спецификации HTML/JS промисы помещаются в очередь микрозадач (Microtask Queue). Event Loop после каждого синхронного вызова в Call Stack ОБЯЗАН полностью очистить очередь микрозадач, прежде чем переходить к макрозадачам (setTimeout/DOM events). Поэтому Promise всегда обгоняет таймер!" data-en="HTML/JS standards dictate that Promises reside in the Microtask Queue. After clearing the Call Stack, the Event Loop MUST exhaust all Microtasks before pulling the next Macrotask (setTimeout). Hence, Promises always jump ahead!">Standart bo'yicha Promise.then() Microtask navbatiga tushadi. Event Loop har bir sinxron amaldan keyin Macrotask (setTimeout) ga o'tishdan oldin BARCHA Microtask-larni to'liq bajarib bo'lishi SHART. Shu sababli Promise har doim taymerdan o'zib ketadi!</p>
      </div>
    </div>
  </article>

  <!-- TASK 3 -->
  <article class="task-card">
    <div class="task-header">
      <div>
        <span class="task-num">Topshiriq 3</span>
        <h2 class="task-title" data-ru="3. Защита Асинхронного Кода через try / catch / finally" data-en="3. Hardening Async Pipelines via try / catch / finally">3. Asinxron Kod Qalqoni: try / catch / finally</h2>
      </div>
      <div class="task-score">2.5 Ball</div>
    </div>
    <p class="task-desc" data-ru="Напишите функцию fetchSecureData(url), которая: 1) включает флаг loading=true; 2) запрашивает данные через await fetch(url); 3) при ошибке сети выбрасывает понятный алерт; 4) в блоке finally гарантированно сбрасывает loading=false." data-en="Write fetchSecureData(url) that: 1) sets loading=true; 2) awaits fetch(url); 3) catches network errors gracefully; 4) guarantees loading=false inside finally.">1) loading=true holatini yoquvchi; 2) await fetch(url) bilan ma'lumot oluvchi; 3) xatoni chiroyli ushlovchi; 4) finally da loading=false ni o'chiruvchi xavfsiz funksiya kodini yozing.</p>
    <textarea class="task-textarea" id="task3_ans" placeholder="JavaScript kodini yozing..." data-placeholder-ru="Напишите код на JavaScript..." data-placeholder-en="Write the JavaScript function..." oninput="autoSave()"></textarea>
    <div style="margin-top:10px;">
      <button class="nav-btn" onclick="toggleFix('fix3')" data-ru="💡 Показать решение (Fix)" data-en="💡 Reveal Solution (Fix)">💡 Yechimni ko'rish (Fix)</button>
      <div id="fix3" class="fix-box" style="display:none; margin-top:8px; padding:10px; background:var(--panel-2); border-left:3px solid var(--ok); border-radius:4px;">
        <b style="color:var(--ok);" data-ru="Эталонное решение:" data-en="Reference Solution:">Etalon Yechim:</b>
        <p style="margin:4px 0 0;" data-ru="async function fetchSecureData(url) {{<br>&nbsp;&nbsp;let loading = true;<br>&nbsp;&nbsp;try {{<br>&nbsp;&nbsp;&nbsp;&nbsp;const res = await fetch(url);<br>&nbsp;&nbsp;&nbsp;&nbsp;if (!res.ok) throw new Error('HTTP ' + res.status);<br>&nbsp;&nbsp;&nbsp;&nbsp;return await res.json();<br>&nbsp;&nbsp;}} catch (err) {{<br>&nbsp;&nbsp;&nbsp;&nbsp;console.error('API Error:', err.message);<br>&nbsp;&nbsp;&nbsp;&nbsp;alert('Xatolik: ' + err.message);<br>&nbsp;&nbsp;}} finally {{<br>&nbsp;&nbsp;&nbsp;&nbsp;loading = false;<br>&nbsp;&nbsp;}}<br>}}" data-en="async function fetchSecureData(url) {{<br>&nbsp;&nbsp;let loading = true;<br>&nbsp;&nbsp;try {{<br>&nbsp;&nbsp;&nbsp;&nbsp;const res = await fetch(url);<br>&nbsp;&nbsp;&nbsp;&nbsp;if (!res.ok) throw new Error('HTTP ' + res.status);<br>&nbsp;&nbsp;&nbsp;&nbsp;return await res.json();<br>&nbsp;&nbsp;}} catch (err) {{<br>&nbsp;&nbsp;&nbsp;&nbsp;console.error('API Error:', err.message);<br>&nbsp;&nbsp;&nbsp;&nbsp;alert('Xatolik: ' + err.message);<br>&nbsp;&nbsp;}} finally {{<br>&nbsp;&nbsp;&nbsp;&nbsp;loading = false;<br>&nbsp;&nbsp;}}<br>}}">async function fetchSecureData(url) {{<br>&nbsp;&nbsp;let loading = true;<br>&nbsp;&nbsp;try {{<br>&nbsp;&nbsp;&nbsp;&nbsp;const res = await fetch(url);<br>&nbsp;&nbsp;&nbsp;&nbsp;if (!res.ok) throw new Error('HTTP ' + res.status);<br>&nbsp;&nbsp;&nbsp;&nbsp;return await res.json();<br>&nbsp;&nbsp;}} catch (err) {{<br>&nbsp;&nbsp;&nbsp;&nbsp;console.error('API Error:', err.message);<br>&nbsp;&nbsp;&nbsp;&nbsp;alert('Xatolik: ' + err.message);<br>&nbsp;&nbsp;}} finally {{<br>&nbsp;&nbsp;&nbsp;&nbsp;loading = false;<br>&nbsp;&nbsp;}}<br>}}</p>
      </div>
    </div>
  </article>

  <!-- TASK 4 -->
  <article class="task-card">
    <div class="task-header">
      <div>
        <span class="task-num">Topshiriq 4</span>
        <h2 class="task-title" data-ru="4. Практика Destructuring и Неизменяемость (Immutability)" data-en="4. Destructuring & Immutability via Spread">4. Destructuring va Obyektlarni Xavfsiz Yangilash</h2>
      </div>
      <div class="task-score">2.5 Ball</div>
    </div>
    <p class="task-desc" data-ru="Дан объект пользователя: const user = {{ id: 1, name: 'Ali', role: 'student', score: 85 }}. С помощью деструктуризации извлеките name и score. Затем с помощью spread (...) создайте обновленный объект updatedUser со score: 100, не мутируя старый объект." data-en="Given: const user = {{ id: 1, name: 'Ali', role: 'student', score: 85 }}. Use destructuring to unpack name and score. Then use spread (...) to produce updatedUser with score: 100 without mutating user.">Berilgan: const user = {{ id: 1, name: 'Ali', role: 'student', score: 85 }}. Destructuring orqali name va score ni ajrating. So'ngra spread (...) orqali eski obyektni buzmasdan score: 100 qilingan yangi updatedUser obyektini yarating.</p>
    <textarea class="task-textarea" id="task4_ans" placeholder="Kod namunalarini yozing..." data-placeholder-ru="Напишите строки кода..." data-placeholder-en="Write the code statements..." oninput="autoSave()"></textarea>
    <div style="margin-top:10px;">
      <button class="nav-btn" onclick="toggleFix('fix4')" data-ru="💡 Показать решение (Fix)" data-en="💡 Reveal Solution (Fix)">💡 Yechimni ko'rish (Fix)</button>
      <div id="fix4" class="fix-box" style="display:none; margin-top:8px; padding:10px; background:var(--panel-2); border-left:3px solid var(--ok); border-radius:4px;">
        <b style="color:var(--ok);" data-ru="Эталонное решение:" data-en="Reference Solution:">Etalon Yechim:</b>
        <p style="margin:4px 0 0;" data-ru="1) Деструктуризация: const {{ name, score }} = user;<br>2) Неизменяемое обновление через Spread: const updatedUser = {{ ...user, score: 100 }};<br>Оригинальный объект user остался нетронутым (score: 85)!" data-en="1) Destructuring: const {{ name, score }} = user;<br>2) Immutable update: const updatedUser = {{ ...user, score: 100 }};<br>Original user object remains unmutated (score: 85)!">1) Destructuring: const {{ name, score }} = user;<br>2) Spread orqali xavfsiz yangilash: const updatedUser = {{ ...user, score: 100 }};<br>Eski user obyekti buzilmasdan saqlanib qoladi (score: 85)!</p>
      </div>
    </div>
  </article>

  <!-- RUBRIC -->
  <section class="rubric-section" style="margin-top:20px; background:var(--panel); border:1px solid var(--rule); border-radius:12px; padding:18px;">
    <h3 style="margin:0 0 12px; font-family:'Manrope',sans-serif;" data-ru="Критерии Оценки за Домашнюю Работу (10 Баллов)" data-en="Homework Evaluation Rubric (10 Points)">Uy Vazifasi Baholash Mezonlari (10 Ball)</h3>
    <div style="display:grid; grid-template-columns:repeat(4, 1fr); gap:10px;">
      <div class="card" style="padding:10px; text-align:center; background:var(--panel-2); border-radius:8px;">
        <b style="color:var(--accent);">2.5 Ball</b>
        <p style="font-size:12px; margin:4px 0 0;" data-ru="1-Задание: Декомпозиция на 3 модуля" data-en="Task 1: Decomposition to 3 modules">1-Topshiriq: 3 ta modulga ajratilgan</p>
      </div>
      <div class="card" style="padding:10px; text-align:center; background:var(--panel-2); border-radius:8px;">
        <b style="color:var(--accent);">2.5 Ball</b>
        <p style="font-size:12px; margin:4px 0 0;" data-ru="2-Задание: Объяснение Microtask vs Macrotask" data-en="Task 2: Microtask vs Macrotask analysis">2-Topshiriq: Microtask va Macrotask tahlili</p>
      </div>
      <div class="card" style="padding:10px; text-align:center; background:var(--panel-2); border-radius:8px;">
        <b style="color:var(--accent);">2.5 Ball</b>
        <p style="font-size:12px; margin:4px 0 0;" data-ru="3-Задание: Пайплайн try/catch/finally" data-en="Task 3: try/catch/finally pipeline">3-Topshiriq: try/catch/finally to'liq yozilgan</p>
      </div>
      <div class="card" style="padding:10px; text-align:center; background:var(--panel-2); border-radius:8px;">
        <b style="color:var(--accent);">2.5 Ball</b>
        <p style="font-size:12px; margin:4px 0 0;" data-ru="4-Задание: Destructuring и Spread" data-en="Task 4: Destructuring & Spread logic">4-Topshiriq: Destructuring va Spread to'g'ri</p>
      </div>
    </div>
  </section>
</main>

<script>
function autoSave() {{
  ['task1_ans', 'task2_ans', 'task3_ans', 'task4_ans'].forEach(function(id) {{
    var val = document.getElementById(id).value;
    localStorage.setItem("vc_hw_29_9_" + id, val);
  }});
}}

function saveStudentData() {{
  localStorage.setItem("vc_student_name_9", document.getElementById("studentName").value);
  localStorage.setItem("vc_student_class_9", document.getElementById("studentClass").value);
  localStorage.setItem("vc_student_date_9", document.getElementById("studentDate").value);
}}

function loadStudentData() {{
  if (localStorage.getItem("vc_student_name_9")) document.getElementById("studentName").value = localStorage.getItem("vc_student_name_9");
  if (localStorage.getItem("vc_student_class_9")) document.getElementById("studentClass").value = localStorage.getItem("vc_student_class_9");
  if (localStorage.getItem("vc_student_date_9")) document.getElementById("studentDate").value = localStorage.getItem("vc_student_date_9");
  ['task1_ans', 'task2_ans', 'task3_ans', 'task4_ans'].forEach(function(id) {{
    var saved = localStorage.getItem("vc_hw_29_9_" + id);
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

print("✅ Vazifa generated for 9-sinf 29-dars")

# -------------------------------------------------------------
# 4. TEACHER_READING.md (Teacher's Guide)
# -------------------------------------------------------------
teacher_guide = """# 29-Dars: O'qituvchi Uchun Metodik Qo'llanma va Yechimlar Kaliti
**Target International School // 9-Sinf // 10-Hafta (2-Chorak 1-Darsi: 40 daqiqa)**
**Mavzu:** Zamonaviy JavaScript (ES6+): Modullar va Asinxron Chuqurlik
**Kohorta:** `9A 9B` (Junior Vibecoders, Full-Stack & DevOps Track)

---

## 1. Asosiy Pedagogik Maqsad
Bugungi dars bilan 9-sinf o'quvchilari **2-Chorak: Agentik Dasturlash va Avtonom Tizimlar** bosqichiga kirishadilar:
1. **ES Modullar:** Global namespace to'qnashuvlaridan xoli bo'lgan mustaqil fayllar arxitekturasi (`export` va `import`).
2. **ES6+ Sintaksisi:** Destructuring (`const { id } = obj`) va Spread/Rest (`...`) yordamida ma'lumotlarni o'zgartirmasdan nusxalash (Immutability).
3. **Event Loop Mexanikasi:** Call Stack (sinxron), Microtask Queue (Promises) va Macrotask Queue (`setTimeout`) iyerarxiyasini tushunish.
4. **Xavfsiz Asinxron Oqim:** `try / catch / finally` bilan har qanday tarmoq va API xatolarini ushlash.

---

## 2. 40 Daqiqalik Dars Reglamenti

| Vaqt | Bosqich | O'qituvchi Harakati | O'quvchilar Harakati |
|---|---|---|---|
| **00:00 – 03:00** | Kirish & 2-Chorak Anonsi | 2-Chorakda AI agentlar va avtonom tizimlar yaratilishini e'lon qilish. | Noutbuklarni ochish, dars rejasini ko'rish. |
| **03:00 – 08:00** | Aqliy Hujum (Spaghetti Kod) | Nega 3000 qatorli bitta fayl loyihani halokatga yetaklashini savol-javob qilish. | Fikr bildirish, xatolar sababini tahlil qilish. |
| **08:00 – 18:00** | Nazariya va Arxitektura | 12 slaydli taqdimot, Named/Default export va Event Loop mexanizmini tushuntirish. | Asosiy qoidalarni konspekt qilish. |
| **18:00 – 23:00** | Jonli Kiber-Test (Event Loop) | Slayd 9 dagi kodning konsolga chiqish tartibini birgalikda yechish. | Tartibni aniqlash, to'g'ri variantni tanlash. |
| **23:00 – 36:00** | Amaliy Modulli Laboratoriya | O'quvchilar 3 ta modulli (api.js, format.js, app.js) valyuta dasturini quradilar. | Kod yozish, modullarni ulash, xatolarni sinash. |
| **36:00 – 40:00** | Xulosa & Baholash | 10 ballik mezon asosida toza modulli ishlarga baho qo'yish, `vazifa.html` ni berish. | Ishlarni ko'rsatish, vazifani saqlab olish. |

---

## 3. Viktorina va Topshiriqlar Yechimi (Teacher Fixes)

### Viktorina (Slayd 9):
* **Savol:** Konsolga qaysi tartibda chiqadi? (1, setTimeout 2, Promise 3, 4)
* **To'g'ri javob:** **B) 1 -> 4 -> 3 -> 2**
* **Izoh:** 1 va 4 darhol Call Stack-da bajariladi. Keyin Microtask navbati (Promise 3) tozalanadi. Eng oxirida Macrotask (setTimeout 2) ishga tushadi.

### Uy Vazifasi Yechimlari:
1. **Modullarga ajratish:** taxCalculator.js (`calcTax`), dbService.js (`Database`), notifyService.js (`sendSMS`).
2. **Microtasks vs Macrotasks:** Event Loop spetsifikatsiyasi bo'yicha har bir sinxron amaldan keyin Microtask-lar (Promise) to'liq bajarilishi shart, shundan so'ngгина Macrotask (setTimeout) olinadi.
3. **try/catch/finally:** `finally` bloki qanday xato bo'lishidan qat'i nazar loading spinnerrini o'chiradi.
4. **Spread nusxalash:** `user2 = user1` xotiradagi bitta linkka qaraydi (biri o'zgarsa ikkinchisi ham buziladi). `{ ...user1 }` esa mustaqil yangi klon hosil qiladi.

---

## 4. Baholash Mezoni (10 Ball)
* **3 Ball:** ES Modules (`export` va `import`) to'g'ri ajratilgan va ishlatilgan.
* **3 Ball:** `async/await` va `try/catch/finally` zanjiri to'liq sozlangan.
* **2 Ball:** Destructuring va Spread operatori o'rinli qo'llangan.
* **2 Ball:** Event Loop ketma-ketligi to'g'ri tahlil qilingan va interfeys qotmaydi.
"""

with open(os.path.join(FOLDER, "TEACHER_READING.md"), "w", encoding="utf-8") as f:
    f.write(teacher_guide)

print("✅ TEACHER_READING.md generated for 9-sinf 29-dars")

# -------------------------------------------------------------
# 5. LAB (Interactive ES6 & Event Loop Visualizer)
# -------------------------------------------------------------
lab_html = """<!DOCTYPE html>
<html lang="uz" data-theme="dark">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title data-ru="Event Loop & ES6 Модули — Лаборатория" data-en="Event Loop & ES6 Modules — Lab">ES6+ va Event Loop Vizualizatori — Interaktiv Lab</title>
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
  border-radius: 16px; padding: 20px; box-shadow: 0 10px 30px rgba(0,0,0,0.4); max-width: 900px; width: 100%;
}
.columns { display: grid; grid-template-columns: repeat(3, 1fr); gap: 14px; flex: 1; }
.col-box {
  background: var(--panel-2); border-radius: 10px; padding: 14px; border: 1px solid var(--rule);
  display: flex; flex-direction: column; gap: 8px;
}
.col-title { font-family: 'JetBrains Mono', monospace; font-size: 12px; font-weight: 700; color: #FFB703; }
.queue-box {
  min-height: 140px; background: #031024; border-radius: 6px; padding: 10px;
  font-family: 'JetBrains Mono', monospace; font-size: 11px; display: flex; flex-direction: column; gap: 6px;
}
.queue-item {
  background: #1A365D; border-left: 3px solid var(--ok); padding: 6px 8px; border-radius: 4px;
  color: #FFF; animation: fadeIn 0.3s;
}
.queue-item.micro { border-left-color: #9F7AEA; background: #2A1B4E; }
.queue-item.macro { border-left-color: var(--accent); background: #3B120D; }
@keyframes fadeIn { from { opacity: 0; transform: translateY(-4px); } to { opacity: 1; transform: translateY(0); } }
.controls { width: 260px; display: flex; flex-direction: column; gap: 12px; }
.console-box {
  background: #031024; border-radius: 8px; padding: 12px; font-family: 'JetBrains Mono', monospace;
  font-size: 12px; color: var(--ok); border: 1px solid var(--rule); min-height: 120px;
}
button {
  background: var(--panel-2); border: 1px solid var(--rule); color: var(--ink);
  padding: 10px; border-radius: 6px; font-family: 'Manrope', sans-serif;
  font-size: 12px; font-weight: 700; cursor: pointer; transition: 0.2s;
}
button:hover { background: var(--accent); color: #fff; border-color: var(--accent); }
</style>
</head>
<body>

<div class="header">
  <h1 data-ru="Интерактивный Визуализатор Event Loop" data-en="Interactive Event Loop Visualizer">Event Loop va Asinxron Navbatlar Studiyasi</h1>
  <p data-ru="Наблюдайте, как Call Stack, Microtasks и Macrotasks распределяют код в реальном времени!" data-en="Watch how Call Stack, Microtasks, and Macrotasks schedule execution in real-time!">Call Stack, Microtasks va Macrotasks navbatlarining real vaqtdagi harakatini kuzating!</p>
</div>

<div class="lab-container">
  <div class="columns">
    <div class="col-box">
      <div class="col-title" data-ru="1. СТЕК ВЫЗОВОВ (LIFO)" data-en="1. CALL STACK (LIFO)">1. CALL STACK (SINXRON)</div>
      <div class="queue-box" id="stackBox"></div>
    </div>
    <div class="col-box">
      <div class="col-title" style="color:#9F7AEA;" data-ru="2. ОЧЕРЕДЬ МИКРОЗАДАЧ" data-en="2. MICROTASK QUEUE">2. MICROTASK (PROMISES)</div>
      <div class="queue-box" id="microBox"></div>
    </div>
    <div class="col-box">
      <div class="col-title" style="color:var(--accent);" data-ru="3. ОЧЕРЕДЬ МАКРОЗАДАЧ" data-en="3. MACROTASK QUEUE">3. MACROTASK (TIMERS)</div>
      <div class="queue-box" id="macroBox"></div>
    </div>
  </div>

  <div class="controls">
    <div class="col-title" data-ru="КОНСОЛЬ ВЫВОДА" data-en="OUTPUT CONSOLE">KONSOL CHIQISHI</div>
    <div class="console-box" id="consoleView">> Tayyor...</div>
    <button onclick="runSimulation()" data-ru="▶ Запустить Тест" data-en="▶ Run Simulation">▶ Simulyatsiyani Ishga Tushirish</button>
    <button onclick="resetSim()" data-ru="Сбросить" data-en="Reset">Tozalash</button>
  </div>
</div>

<script>
function log(msg) {
  const c = document.getElementById("consoleView");
  c.innerHTML += "<br>> " + msg;
  c.scrollTop = c.scrollHeight;
}

function resetSim() {
  document.getElementById("stackBox").innerHTML = "";
  document.getElementById("microBox").innerHTML = "";
  document.getElementById("macroBox").innerHTML = "";
  document.getElementById("consoleView").innerHTML = "> Tozalandi...";
}

function runSimulation() {
  resetSim();
  log("Simulyatsiya boshlandi...");

  // Step 1: Call Stack pushes console.log(1)
  setTimeout(() => {
    document.getElementById("stackBox").innerHTML = '<div class="queue-item">console.log("1")</div>';
    log("Call Stack: 1");
  }, 400);

  // Step 2: Push setTimeout to Macrotask
  setTimeout(() => {
    document.getElementById("stackBox").innerHTML = '<div class="queue-item">setTimeout(() => 2, 0)</div>';
    document.getElementById("macroBox").innerHTML = '<div class="queue-item macro">Timer: log("2")</div>';
  }, 900);

  // Step 3: Push Promise to Microtask
  setTimeout(() => {
    document.getElementById("stackBox").innerHTML = '<div class="queue-item">Promise.then(() => 3)</div>';
    document.getElementById("microBox").innerHTML = '<div class="queue-item micro">Promise: log("3")</div>';
  }, 1400);

  // Step 4: console.log(4) on Call Stack
  setTimeout(() => {
    document.getElementById("stackBox").innerHTML = '<div class="queue-item">console.log("4")</div>';
    log("Call Stack: 4");
  }, 1900);

  // Step 5: Stack clears
  setTimeout(() => {
    document.getElementById("stackBox").innerHTML = '<span style="color:#64748B;">[Bo\'sh]</span>';
    log("Call Stack bo'shadi! Microtask navbati ishga tushadi...");
  }, 2400);

  // Step 6: Flush Microtask (3)
  setTimeout(() => {
    document.getElementById("stackBox").innerHTML = '<div class="queue-item micro">log("3")</div>';
    document.getElementById("microBox").innerHTML = "";
    log("Microtask: 3");
  }, 2900);

  // Step 7: Flush Macrotask (2)
  setTimeout(() => {
    document.getElementById("stackBox").innerHTML = '<div class="queue-item macro">log("2")</div>';
    document.getElementById("macroBox").innerHTML = "";
    log("Macrotask: 2");
  }, 3500);

  // Complete
  setTimeout(() => {
    document.getElementById("stackBox").innerHTML = '<span style="color:#00D68F;">[Tugadi: 1 -> 4 -> 3 -> 2]</span>';
    log("✅ Event Loop sikli muvaffaqiyatli yakunlandi!");
  }, 4100);
}
</script>
</body>
</html>
"""

with open(os.path.join(FOLDER, "lab", "index.html"), "w", encoding="utf-8") as f:
    f.write(lab_html)

print("✅ Lab generated for 9-sinf 29-dars")
