import os

presentation_content = '''<!DOCTYPE html>
<html lang="uz">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>19.5-dars: Vibecoding E-Commerce Backend — Users, Orders & Postman API Testing</title>
<link rel="icon" type="image/svg+xml" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 96 96'%3E%3Cstyle%3E:root%7B--n:%2300214A;--r:%23FF1100%7D@media(prefers-color-scheme:dark)%7B:root%7B--n:%23FFFFFF;--r:%23FF3B26%7D%7D.nf%7Bfill:var(--n)%7D.ns%7Bstroke:var(--n);fill:none%7D.rf%7Bfill:var(--r)%7D.rs%7Bstroke:var(--r);fill:none%7D%3C/style%3E%3Cpath class='ns' stroke-width='11.5' d='M54.5 7.9A40.5 40.5 0 0 1 88.1 41.5M88.1 54.5A40.5 40.5 0 0 1 54.5 88.1M41.5 88.1A40.5 40.5 0 0 1 7.9 54.5M7.9 41.5A40.5 40.5 0 0 1 41.5 7.9'/%3E%3Ccircle class='rs' cx='48' cy='48' r='17.2' stroke-width='7.2'/%3E%3Crect class='rf' x='45.6' y='3' width='4.8' height='28' rx='.5'/%3E%3Crect class='rf' x='45.6' y='65' width='4.8' height='28' rx='.5'/%3E%3Crect class='rf' x='3' y='45.6' width='28' height='4.8' rx='.5'/%3E%3Crect class='rf' x='65' y='45.6' width='28' height='4.8' rx='.5'/%3E%3Ccircle class='nf' cx='48' cy='48' r='7.2'/%3E%3C/svg%3E">
<link rel="alternate icon" type="image/png" sizes="32x32" href="/assets/favicon-32x32.png">
<link rel="apple-touch-icon" sizes="180x180" href="/assets/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Manrope:wght@500;700;800&family=Source+Sans+3:wght@400;600;700&family=JetBrains+Mono:wght@400;700&display=swap">
<style>
:root{
  --bg:#F1F5FB; --panel:#E6EDF7; --panel-2:#D5E1F0;
  --grid:rgba(0,33,74,.055);
  --ink:#00214A; --ink-2:#46587A; --ink-3:#8496B0;
  --rule:#CBD7E7;
  --accent:#FF1100; --accent-ink:#C21000; --accent-soft:#FFE7E3;
  --green:#0B6B4F; --green-soft:#DDF0E8;
  --purple:#5B21B6; --purple-soft:#EDE9FE;
  --orange:#FF6C37; --orange-soft:#FFF0EA;
}
@media (prefers-color-scheme: dark){
  :root:not([data-theme="light"]){
    --bg:#061530; --panel:#0E2249; --panel-2:#16305A;
    --grid:rgba(232,238,247,.05);
    --ink:#E9EFF8; --ink-2:#A2B4CE; --ink-3:#70859F;
    --rule:#1E3A63;
    --accent:#FF3B26; --accent-ink:#FF7563; --accent-soft:#3B140F;
    --green:#7FD3B2; --green-soft:#0F2E26;
    --purple:#A78BFA; --purple-soft:#2E1065;
    --orange:#FF7C4D; --orange-soft:#3A1A0F;
  }
}
:root[data-theme="dark"]{
  --bg:#061530; --panel:#0E2249; --panel-2:#16305A;
  --grid:rgba(232,238,247,.05);
  --ink:#E9EFF8; --ink-2:#A2B4CE; --ink-3:#70859F;
  --rule:#1E3A63;
  --accent:#FF3B26; --accent-ink:#FF7563; --accent-soft:#3B140F;
  --green:#7FD3B2; --green-soft:#0F2E26;
  --purple:#A78BFA; --purple-soft:#2E1065;
  --orange:#FF7C4D; --orange-soft:#3A1A0F;
}

*{box-sizing:border-box}
* {scrollbar-width:thin; scrollbar-color:var(--rule) transparent}
::-webkit-scrollbar{width:9px; height:9px}
::-webkit-scrollbar-track{background:transparent}
::-webkit-scrollbar-thumb{background:var(--rule); border-radius:99px}
::-webkit-scrollbar-thumb:hover{background:var(--ink-3)}

html,body{
  margin:0; padding:0; width:100%; height:100%; overflow:hidden;
  background:var(--bg); color:var(--ink);
  font-family:"Source Sans 3",system-ui,-apple-system,sans-serif;
  -webkit-font-smoothing:antialiased;
}
body{display:flex; flex-direction:column; position:relative}

.brandrule{
  position:absolute; top:0; left:0; right:0; height:4px;
  background:linear-gradient(90deg, #FF1100 0%, #00214A 50%, #0B6B4F 100%);
  z-index:100;
}

.stage{
  flex:1; width:100%; height:calc(100% - 56px);
  position:relative; overflow:hidden;
}
.slide{
  position:absolute; inset:0; padding:36px 56px 28px;
  display:none; flex-direction:column; justify-content:flex-start;
  overflow-y:auto; box-sizing:border-box;
  background-image:
    linear-gradient(to right, var(--grid) 1px, transparent 1px),
    linear-gradient(to bottom, var(--grid) 1px, transparent 1px);
  background-size:28px 28px;
}
.slide.active{display:flex}

.eyebrow{
  display:inline-flex; align-items:center; gap:8px;
  font-family:"JetBrains Mono",monospace; font-size:12px; font-weight:700;
  letter-spacing:.08em; text-transform:uppercase; color:var(--accent-ink);
  margin-bottom:8px;
}
.eyebrow::before{
  content:""; display:inline-block; width:8px; height:8px;
  background:var(--accent); border-radius:50%;
}

h1{
  font-family:"Manrope",system-ui,sans-serif; font-size:44px; font-weight:800;
  line-height:1.12; color:var(--ink); margin:0 0 12px; letter-spacing:-.02em;
}
h2{
  font-family:"Manrope",system-ui,sans-serif; font-size:32px; font-weight:800;
  line-height:1.2; color:var(--ink); margin:0 0 14px; letter-spacing:-.015em;
}
h3{
  font-family:"Manrope",system-ui,sans-serif; font-size:18px; font-weight:700;
  line-height:1.3; color:var(--ink); margin:0 0 6px;
}
p{
  font-size:16px; line-height:1.5; color:var(--ink-2); margin:0 0 12px;
}
.lede{
  font-size:18px; line-height:1.5; color:var(--ink); margin-bottom:18px;
  max-width:960px; font-weight:500;
}

.cols{display:grid; gap:16px; width:100%; margin:8px 0 12px}
.c2{grid-template-columns:1fr 1fr}
.c3{grid-template-columns:1fr 1fr 1fr}
.c4{grid-template-columns:1fr 1fr 1fr 1fr}
.c3-2{grid-template-columns:3fr 2fr}
.c2-3{grid-template-columns:2fr 3fr}

.box{
  background:var(--panel); border:1px solid var(--rule);
  border-radius:10px; padding:16px 18px; position:relative;
}
.box.accent{border-left:4px solid var(--accent)}
.box.green{border-left:4px solid var(--green)}
.box.purple{border-left:4px solid var(--purple)}
.box.orange{border-left:4px solid var(--orange)}

ul.plain{list-style:none; padding:0; margin:0}
ul.plain li{
  font-size:14.5px; line-height:1.45; color:var(--ink);
  margin-bottom:8px; padding-left:18px; position:relative;
}
ul.plain li::before{
  content:"▸"; position:absolute; left:0; color:var(--accent-ink);
  font-weight:700; font-family:"JetBrains Mono",monospace;
}

.tbl{
  width:100%; border-collapse:collapse; margin:8px 0; font-size:13.5px;
  background:var(--panel); border-radius:8px; overflow:hidden; border:1px solid var(--rule);
}
.tbl th, .tbl td{
  padding:8px 12px; text-align:left; border-bottom:1px solid var(--rule);
}
.tbl th{
  background:var(--panel-2); font-family:"JetBrains Mono",monospace;
  font-size:12px; font-weight:700; color:var(--ink); letter-spacing:.03em;
}
.tbl tr:last-child td{border-bottom:none}
.tbl code{
  font-family:"JetBrains Mono",monospace; font-size:12.5px;
  background:var(--panel-2); padding:2px 6px; border-radius:4px;
}

pre{
  background:var(--panel-2); border:1px solid var(--rule);
  border-radius:8px; padding:12px 14px; margin:6px 0 10px;
  overflow-x:auto; font-family:"JetBrains Mono",monospace; font-size:12.5px;
  line-height:1.45; color:var(--ink);
}

.pill{
  display:inline-flex; align-items:center; gap:6px;
  padding:3px 9px; border-radius:99px; font-family:"JetBrains Mono",monospace;
  font-size:11.5px; font-weight:700;
}
.pill-accent{background:var(--accent-soft); color:var(--accent-ink)}
.pill-green{background:var(--green-soft); color:var(--green)}
.pill-purple{background:var(--purple-soft); color:var(--purple)}
.pill-orange{background:var(--orange-soft); color:var(--orange)}

.meta-chip{
  display:inline-flex; align-items:center; gap:6px;
  font-family:"JetBrains Mono",monospace; font-size:12px; color:var(--ink-2);
  background:var(--panel-2); padding:4px 10px; border-radius:6px;
  border:1px solid var(--rule); margin-right:8px; margin-bottom:8px;
}

/* BOTTOM BAR */
.bar{
  height:56px; background:var(--panel); border-top:1px solid var(--rule);
  display:flex; align-items:center; justify-content:space-between;
  padding:0 24px; position:relative; z-index:90;
}
.bar-left, .bar-right{display:flex; align-items:center; gap:12px}
.brandmark{display:flex; align-items:center; gap:8px}
.bar-mark img{height:24px; width:auto}
:root[data-theme="dark"] .on-light{display:none}
:root[data-theme="dark"] .on-dark{display:block}
:root:not([data-theme="dark"]) .on-light{display:block}
:root:not([data-theme="dark"]) .on-dark{display:none}
@media (prefers-color-scheme: dark){
  :root:not([data-theme="light"]) .on-light{display:none}
  :root:not([data-theme="light"]) .on-dark{display:block}
}

.phase{
  font-family:"JetBrains Mono",monospace; font-size:12px; font-weight:700;
  text-transform:uppercase; letter-spacing:.05em; color:var(--ink-2);
  padding:4px 10px; background:var(--panel-2); border-radius:6px;
}
.count{
  font-family:"JetBrains Mono",monospace; font-size:12px; color:var(--ink-2);
}
.timer{
  font-family:"JetBrains Mono",monospace; font-size:12px; font-weight:700;
  color:var(--accent-ink); padding:4px 8px; border-radius:4px;
  background:var(--accent-soft); cursor:pointer;
}

.btn-ctrl{
  background:var(--panel-2); border:1px solid var(--rule); color:var(--ink);
  font-family:"JetBrains Mono",monospace; font-size:12px; font-weight:700;
  padding:6px 12px; border-radius:6px; cursor:pointer; transition:.15s;
}
.btn-ctrl:hover{background:var(--ink); color:var(--bg)}
.btn-lang{
  background:var(--panel-2); border:1px solid var(--rule); color:var(--ink-2);
  font-family:"JetBrains Mono",monospace; font-size:11px; font-weight:700;
  padding:4px 8px; border-radius:4px; cursor:pointer;
}
.btn-lang.active{background:var(--ink); color:var(--bg)}

/* SPEAKER NOTES */
.notes-pane{
  position:fixed; bottom:56px; left:0; right:0; height:180px;
  background:var(--panel); border-top:2px solid var(--accent);
  padding:14px 28px; z-index:95; display:none; overflow-y:auto;
  box-shadow:0 -8px 24px rgba(0,0,0,.15);
}
.notes-pane.open{display:block}
.notes-title{
  font-family:"Manrope",system-ui,sans-serif; font-size:13px; font-weight:800;
  text-transform:uppercase; letter-spacing:.06em; color:var(--accent-ink);
  margin-bottom:6px;
}
.notes-text{
  font-size:13.5px; line-height:1.45; color:var(--ink); margin:0;
}
</style>
</head>
<body>
<div class="brandrule"></div>

<div class="stage">

<!-- SLIDE 1: TITUL -->
<section class="slide active" data-phase="Kirish|Введение|Introduction" data-time="0–3">
  <div class="eyebrow"><span data-ru="9 Класс · Неделя 4 · Урок 19.5" data-en="Grade 9 · Week 4 · Lesson 19.5">9-sinf · 4-hafta · 19.5-dars</span></div>
  <div style="margin:12px 0 16px;">
    <span class="meta-chip" data-ru="<b>Трек:</b> Backend & Postman" data-en="<b>Track:</b> Backend & Postman"><b>Yo'nalish:</b> Backend & Postman</span>
    <span class="meta-chip" data-ru="<b>Когорта:</b> 9 класс Junior Vibecoder" data-en="<b>Cohort:</b> Grade 9 Junior Vibecoder"><b>Kohorta:</b> 9-sinf Junior Vibecoder</span>
    <span class="meta-chip" data-ru="<b>Формат:</b> Практикум (40 мин)" data-en="<b>Format:</b> Deep-Dive Lab (40 min)"><b>Format:</b> Amaliyot (40 daqiqa)</span>
  </div>
  <h1 data-ru="Vibecoding E-Commerce Backend: Users, Orders & Postman API" data-en="Vibecoding E-Commerce Backend: Users, Orders & Postman API">Vibecoding E-Commerce Backend: Users, Orders & Postman API</h1>
  <p class="lede" data-ru="В 19-уроке мы заложили основы Express. Сегодня мы строим полноценную E-Commerce систему: связываем таблицы <b>users</b> и <b>orders</b>, внедряем проверку баланса, реализуем все методы <b>CRUD (GET, POST, PATCH, DELETE)</b> и тестируем API через индустриальный стандарт <b>Postman</b>." data-en="In lesson 19 we mastered Express fundamentals. Today we engineer a production-ready E-Commerce backend: wiring relational <b>users</b> and <b>orders</b> tables, enforcing balance guards, implementing full <b>CRUD (GET, POST, PATCH, DELETE)</b>, and verifying the entire pipeline via industry-standard <b>Postman</b>.">19-darsda Express poydevorini o'rgandik. Bugun esa haqiqiy elektron tijorat (E-Commerce) serverini quramiz: <b>users</b> va <b>orders</b> relyatsion jadvallarini ulaymiz, hisob balansi nazoratini kiritamiz, to'liq <b>CRUD (GET, POST, PATCH, DELETE)</b> marshrutlarini yozamiz va butun tizimni jahon standarti <b>Postman</b> orqali sinovdan o'tkazamiz.</p>
  
  <div class="cols c3" style="margin-top:16px;">
    <div class="box green">
      <span class="pill pill-green">Entity 1</span>
      <h3 style="margin-top:6px;" data-ru="Пользователи (Users)" data-en="Users Entity">Foydalanuvchilar (Users)</h3>
      <p style="font-size:13px;" data-ru="Профиль клиента, email, баланс в сумах и история транзакций." data-en="Client profile, email, account balance, and transaction history.">Mijoz profili, email, so'mdagi hisob balansi va xaridlar tarixi.</p>
    </div>
    <div class="box orange">
      <span class="pill pill-orange">Entity 2</span>
      <h3 style="margin-top:6px;" data-ru="Заказы (Orders)" data-en="Orders Entity">Buyurtmalar (Orders)</h3>
      <p style="font-size:13px;" data-ru="Связка user_id, сумма, статус (pending/completed) и валидация средств." data-en="Foreign key user_id, order amount, lifecycle status, and balance guard.">user_id bog'lanishi, buyurtma summasi, statusi va balans nazorati.</p>
    </div>
    <div class="box purple">
      <span class="pill pill-purple">QA & Tests</span>
      <h3 style="margin-top:6px;" data-ru="Postman Среда" data-en="Postman Workspace">Postman Muhiti</h3>
      <p style="font-size:13px;" data-ru="Коллекция запросов, тестирование статус-кодов (pm.test) и авто-раннер." data-en="API collections, status assertions (pm.test), and automated runner.">So'rovlar to'plami, status kodlar testi (pm.test) va avtomatlashtirilgan runner.</p>
    </div>
  </div>
</section>

<!-- SLIDE 2: E-COMMERCE ARXITEKTURASI -->
<section class="slide" data-phase="Arxitektura|Архитектура|Architecture" data-time="3–7">
  <div class="eyebrow"><span data-ru="Реляционная Модель" data-en="Relational Model">Relyatsion Model</span></div>
  <h2 data-ru="E-Commerce Архитектура: Users, Orders и Финансовый Баланс" data-en="E-Commerce Architecture: Users, Orders & Financial Guardrails">E-Commerce Arxitekturasi: Users, Orders va Moliyaviy Balans</h2>
  <div class="cols c2">
    <div class="box accent">
      <h3 data-ru="Таблица USERS (Клиенты)" data-en="USERS Table (Customers)">USERS Jadvali (Mijozlar)</h3>
      <ul class="plain">
        <li><span class="t" data-ru="<b>id:</b> Уникальный ключ (Primary Key)." data-en="<b>id:</b> Unique Primary Key."><b>id:</b> Birlamchi kalit (Primary Key).</span></li>
        <li><span class="t" data-ru="<b>full_name & email:</b> Уникальные данные клиента." data-en="<b>full_name & email:</b> Unique customer identity."><b>full_name & email:</b> Mijozning yagona identifikatori.</span></li>
        <li><span class="t" data-ru="<b>balance:</b> Текущий денежный счёт (например, 500 000 сум)." data-en="<b>balance:</b> Active customer funds (e.g. 500,000 UZS)."><b>balance:</b> Mijoz hisobidagi naqd pul (masalan: 500 000 so'm).</span></li>
      </ul>
      <pre>CREATE TABLE users (
  id INTEGER PRIMARY KEY,
  full_name TEXT NOT NULL,
  email TEXT UNIQUE NOT NULL,
  balance INTEGER DEFAULT 0
);</pre>
    </div>

    <div class="box green">
      <h3 data-ru="Таблица ORDERS (Заказы)" data-en="ORDERS Table (Orders)">ORDERS Jadvali (Buyurtmalar)</h3>
      <ul class="plain">
        <li><span class="t" data-ru="<b>id:</b> Номер чека (Primary Key)." data-en="<b>id:</b> Order receipt ID (Primary Key)."><b>id:</b> Buyurtma cheki (Primary Key).</span></li>
        <li><span class="t" data-ru="<b>user_id:</b> Внешний ключ (Foreign Key) к таблице users." data-en="<b>user_id:</b> Foreign Key linked to users table."><b>user_id:</b> users jadvaliga bog'langan tashqi kalit (FK).</span></li>
        <li><span class="t" data-ru="<b>amount:</b> Сумма заказа. Не может быть больше баланса!" data-en="<b>amount:</b> Order total. Cannot exceed user balance!"><b>amount:</b> Xarid summasi. Balansdan katta bo'lishi mumkin emas!</span></li>
        <li><span class="t" data-ru="<b>status:</b> 'pending', 'completed' или 'cancelled'." data-en="<b>status:</b> 'pending', 'completed', or 'cancelled'."><b>status:</b> 'pending', 'completed' yoki 'cancelled'.</span></li>
      </ul>
      <pre>CREATE TABLE orders (
  id INTEGER PRIMARY KEY,
  user_id INTEGER NOT NULL REFERENCES users(id),
  product_name TEXT NOT NULL,
  amount INTEGER NOT NULL,
  status TEXT DEFAULT 'pending'
);</pre>
    </div>
  </div>
  <div class="box orange" style="margin-top:4px;">
    <span class="pill pill-orange" data-ru="Золотое Правило Backend" data-en="Backend Golden Rule">Backend Oltin Qoidasi</span>
    <p style="margin:4px 0 0; font-size:14px;" data-ru="<b>Никогда не доверяйте клиенту!</b> Браузер может прислать любую сумму. Только сервер проверяет: <code>if (user.balance < amount) return res.status(400)</code>." data-en="<b>Never trust the client!</b> The browser can forge any payload. Only the server enforces: <code>if (user.balance < amount) return res.status(400)</code>."><b>Mijozga (brauzerga) hech qachon ishonmang!</b> Brauzer har qanday soxta so'rov yuborishi mumkin. Faqat server hisobni tekshiradi: <code>if (user.balance < amount) return res.status(400)</code>.</p>
  </div>
</section>

<!-- SLIDE 3: REST CRUD VA HTTP METHODLAR -->
<section class="slide" data-phase="HTTP Standartlari|HTTP Стандарты|HTTP Standards" data-time="7–11">
  <div class="eyebrow"><span data-ru="REST Конвенции" data-en="REST Conventions">REST Standartlari</span></div>
  <h2 data-ru="Анатомия CRUD: Почему PATCH, а не PUT? Статус-коды" data-en="CRUD Mechanics: Why PATCH Over PUT? HTTP Status Codes">CRUD Anatomiyasi: Nega PUT emas, balki PATCH? Status Kodlar</h2>
  
  <table class="tbl">
    <thead>
      <tr>
        <th data-ru="Метод" data-en="Method">Method</th>
        <th data-ru="Маршрут" data-en="Route">Marshrut</th>
        <th data-ru="Действие" data-en="Action">Amal</th>
        <th data-ru="Статус Успеха" data-en="Success Code">Muvaffaqiyat Kodi</th>
        <th data-ru="Особенность (Инженерия)" data-en="Engineering Nuance">Muhandislik Nozikligi</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td data-ru="GET" data-en="GET"><span class="pill pill-green">GET</span></td>
        <td data-ru="/api/users" data-en="/api/users"><code>/api/users</code></td>
        <td data-ru="Получить всех пользователей" data-en="Fetch all users">Barcha foydalanuvchilarni olish</td>
        <td data-ru="200 OK" data-en="200 OK"><code>200 OK</code></td>
        <td data-ru="Safe & Idempotent (сервер не меняет данные)" data-en="Safe & Idempotent (read-only state)">Xavfsiz va Idempotent (bazani o'zgartirmaydi)</td>
      </tr>
      <tr>
        <td data-ru="POST" data-en="POST"><span class="pill pill-blue">POST</span></td>
        <td data-ru="/api/users" data-en="/api/users"><code>/api/users</code></td>
        <td data-ru="Создать нового клиента" data-en="Create new customer">Yangi mijoz ro'yxatdan o'tkazish</td>
        <td data-ru="201 Created" data-en="201 Created"><code>201 Created</code></td>
        <td data-ru="Принимает req.body, возвращает созданный объект с ID" data-en="Consumes req.body, yields created record with ID">req.body qabul qiladi, yangi ID beradi</td>
      </tr>
      <tr>
        <td data-ru="POST" data-en="POST"><span class="pill pill-blue">POST</span></td>
        <td data-ru="/api/orders" data-en="/api/orders"><code>/api/orders</code></td>
        <td data-ru="Оформить заказ и списать баланс" data-en="Place order & debit balance">Buyurtma berish va balansdan yechish</td>
        <td data-ru="201 Created" data-en="201 Created"><code>201 Created</code></td>
        <td data-ru="Проверяет баланс; при нехватке возвращает 400 Bad Request" data-en="Guards balance; yields 400 Bad Request on deficit">Balansni tekshiradi; yetmasa 400 Bad Request</td>
      </tr>
      <tr>
        <td data-ru="PATCH" data-en="PATCH"><span class="pill pill-purple">PATCH</span></td>
        <td data-ru="/api/orders/:id" data-en="/api/orders/:id"><code>/api/orders/:id</code></td>
        <td data-ru="Обновить статус заказа (pending ➔ completed)" data-en="Update order status (pending ➔ completed)">Buyurtma holatini yangilash (pending ➔ completed)</td>
        <td data-ru="200 OK" data-en="200 OK"><code>200 OK</code></td>
        <td data-ru="Частичное обновление! PUT заменил бы весь объект целиком" data-en="Partial update! PUT would overwrite the entire record">Qisman yangilash! PUT butun obyektni o'chirib yozadi</td>
      </tr>
      <tr>
        <td data-ru="DELETE" data-en="DELETE"><span class="pill pill-accent">DELETE</span></td>
        <td data-ru="/api/orders/:id" data-en="/api/orders/:id"><code>/api/orders/:id</code></td>
        <td data-ru="Отменить и удалить заказ" data-en="Cancel & delete order">Buyurtmani bekor qilish yoki o'chirish</td>
        <td data-ru="200 OK" data-en="200 OK"><code>200 OK</code></td>
        <td data-ru="Удаляет запись по ID; при повторе даёт 404 Not Found" data-en="Removes record by ID; subsequent calls yield 404">ID bo'yicha o'chiradi; qayta chaqirilsa 404</td>
      </tr>
    </tbody>
  </table>

  <div class="cols c2" style="margin-top:6px;">
    <div class="box purple">
      <h3 data-ru="💡 PATCH против PUT" data-en="💡 PATCH vs PUT">💡 PATCH vs PUT Farqi</h3>
      <p style="font-size:13px; margin:0;" data-ru="<b>PUT:</b> Перезаписывает документ целиком (если не прислать product_name, оно сотрётся).<br><b>PATCH:</b> Меняет только указанные поля (например, только <code>{ status: 'completed' }</code>). В E-Commerce это стандарт." data-en="<b>PUT:</b> Overwrites the entire resource (missing fields become null).<br><b>PATCH:</b> Modifies only specific fields (e.g. only <code>{ status: 'completed' }</code>). Industry standard for orders."><b>PUT:</b> Obyektni to'liq almashtiradi (agar product_name yuborilmasa, o'chib ketadi).<br><b>PATCH:</b> Faqat ko'rsatilgan maydonni yangilaydi (masalan: <code>{ status: 'completed' }</code>). E-Commerce da bu standart.</p>
    </div>
    <div class="box accent">
      <h3 data-ru="⚠️ Коды Ошибок" data-en="⚠️ Standard Error Responses">⚠️ Asosiy Xato Kodlari</h3>
      <p style="font-size:13px; margin:0;" data-ru="<b>400 Bad Request:</b> Ошибка клиента (нет email, баланс меньше суммы заказа).<br><b>404 Not Found:</b> Ресурс не найден (нет клиента с таким ID).<br><b>500 Internal Server Error:</b> Ошибка сервера (упал код или база данных)." data-en="<b>400 Bad Request:</b> Client validation error (missing email, insufficient balance).<br><b>404 Not Found:</b> Missing resource (no user found with given ID).<br><b>500 Internal Server Error:</b> Server crash or unhandled DB exception."><b>400 Bad Request:</b> Mijoz xatosi (email yo'q, balans yetarli emas).<br><b>404 Not Found:</b> Resurs topilmadi (bunday ID li mijoz yo'q).<br><b>500 Server Error:</b> Server xatosi (kodda xatolik yuz berdi).</p>
    </div>
  </div>
</section>

<!-- SLIDE 4: POSTMAN NIMA -->
<section class="slide" data-phase="Vositalar|Инструменты|Tooling" data-time="11–15">
  <div class="eyebrow"><span data-ru="Индустриальный Стандарт" data-en="Industry Standard">Sanoat Standarti</span></div>
  <h2 data-ru="Что Такое Postman и Почему Браузера Недостаточно?" data-en="What is Postman & Why Is the Browser Not Enough?">Postman Nima va Nega Brauzerning O'zi Yetarli Emas?</h2>
  
  <div class="cols c2">
    <div class="box accent">
      <h3 data-ru="❌ Ограничение Браузера" data-en="❌ Browser Limitations">❌ Brauzer Cheklovlari</h3>
      <ul class="plain">
        <li><span class="t" data-ru="<b>Только GET:</b> Адресная строка браузера может отправлять только GET-запросы." data-en="<b>GET-only:</b> Browser address bar can only initiate GET requests."><b>Faqat GET:</b> Brauzer manzil qatori faqat GET so'rov yubora oladi.</span></li>
        <li><span class="t" data-ru="<b>Нет JSON Body:</b> Нельзя руками ввести тело запроса (payload) для POST или PATCH." data-en="<b>No raw JSON:</b> You cannot easily enter JSON payloads for POST or PATCH."><b>JSON Body yo'q:</b> POST yoki PATCH uchun qo'lda JSON jo'natib bo'lmaydi.</span></li>
        <li><span class="t" data-ru="<b>Нет заголовков:</b> Нельзя гибко настроить <code>Content-Type</code> или токены авторизации." data-en="<b>No headers:</b> Cannot configure <code>Content-Type</code> or auth tokens easily."><b>Headers yo'q:</b> <code>Content-Type</code> yoki auth tokenlarini moslab bo'lmaydi.</span></li>
      </ul>
    </div>

    <div class="box orange">
      <h3 data-ru="✅ Postman: Мощь API Инженера" data-en="✅ Postman: API Engineering Powerhouse">✅ Postman: API Muhandisining Asosiy Quroli</h3>
      <ul class="plain">
        <li><span class="t" data-ru="<b>Любой HTTP метод:</b> GET, POST, PUT, PATCH, DELETE, OPTIONS." data-en="<b>Any HTTP method:</b> Full support for GET, POST, PUT, PATCH, DELETE."><b>Barcha HTTP methodlar:</b> GET, POST, PUT, PATCH, DELETE to'liq qo'llab-quvvatlanadi.</span></li>
        <li><span class="t" data-ru="<b>Raw JSON Body:</b> Подсветка синтаксиса, автоформатирование и валидация тела." data-en="<b>Raw JSON Body:</b> Syntax highlighting, formatting, and JSON validation."><b>Raw JSON Body:</b> Sintaksis tekshiruvi, formatlash va qulay JSON muharriri.</span></li>
        <li><span class="t" data-ru="<b>Коллекции и Переменные:</b> Сохранение маршрутов в виде <code>{{base_url}}/api/orders</code>." data-en="<b>Collections & Variables:</b> Group endpoints and reuse <code>{{base_url}}</code>."><b>Kolleksiyalar:</b> Marshrutlarni bitta faylga yig'ish va <code>{{base_url}}</code> o'zgaruvchilari.</span></li>
        <li><span class="t" data-ru="<b>Автотесты (Test Scripts):</b> Проверка статус-кодов за 1 миллисекунду." data-en="<b>Test Scripts:</b> Automatic status code assertions in 1 millisecond."><b>Avtomatik Testlar:</b> Har bir so'rov natijasini 1 millisekundda tekshirish.</span></li>
      </ul>
    </div>
  </div>

  <div class="box purple" style="margin-top:6px;">
    <h3 data-ru="4 Части Запроса в Postman" data-en="4 Core Parts of a Postman Request">Postmanda So'rovning 4 Asosiy Qismi</h3>
    <div class="cols c4" style="margin:4px 0 0;">
      <div><b>1. Method & URL</b><br><span style="font-size:12px; color:var(--ink-2);">POST http://localhost:3000/api/orders</span></div>
      <div><b>2. Headers</b><br><span style="font-size:12px; color:var(--ink-2);">Content-Type: application/json</span></div>
      <div><b>3. Body (raw)</b><br><span style="font-size:12px; color:var(--ink-2);">{ "user_id": 1, "amount": 180000 }</span></div>
      <div><b>4. Tests (JS)</b><br><span style="font-size:12px; color:var(--ink-2);">pm.response.to.have.status(201)</span></div>
    </div>
  </div>
</section>

<!-- SLIDE 5: VIBECODING PROMPT ENGINEERING -->
<section class="slide" data-phase="Vibecoding|Вайбкодинг|Vibecoding" data-time="15–19">
  <div class="eyebrow"><span data-ru="Искусство Промпта" data-en="Prompt Engineering">Vibecoding Texnikasi</span></div>
  <h2 data-ru="Vibecoding: Как Правильно Формулировать Backend-Промпты" data-en="Vibecoding: Formulating Robust Backend Prompts for AI">Vibecoding: AI ga Aniq Backend Prompt Berish Qoidalari</h2>
  
  <div class="cols c2">
    <div class="box accent">
      <h3 data-ru="❌ Слабый Промпт (Даст Дырявый Код)" data-en="❌ Weak Prompt (Yields Broken Code)">❌ Kuchsiz Prompt (Xato va Zaif Kod Beradi)</h3>
      <p style="font-size:13px; font-style:italic;" data-ru="«Напиши мне бэкенд для интернет-магазина на ноде чтобы заказы работали»" data-en="«Write a backend for an online shop in node so orders work»">"Menga Node da internet magazin backendini yoz, buyurtmalar ishlasin"</p>
      <ul class="plain">
        <li><span class="t" data-ru="AI не знает структуру таблиц (нет user_id, amount)." data-en="AI does not know database schema (missing user_id, amount).">AI jadval ustunlarini bilmaydi (user_id va amount yo'q).</span></li>
        <li><span class="t" data-ru="Нет валидации баланса: клиент может купить товар на 10 млн с нулевым счётом!" data-en="No balance validation: user can order with zero funds!">Balans nazorati yo'q: hisobida 0 so'm bo'lgan odam ham buyurtma beraveradi!</span></li>
        <li><span class="t" data-ru="Нет правильных статус-кодов (вернёт 200 везде, даже при ошибках)." data-en="No HTTP status codes (returns 200 everywhere, masking errors).">Status kodlar yo'q: xato bo'lsa ham 200 OK qaytaraveradi.</span></li>
      </ul>
    </div>

    <div class="box green">
      <h3 data-ru="✅ Профессиональный Vibecoding Промпт" data-en="✅ Professional Vibecoding Prompt">✅ Professional Vibecoding Prompt</h3>
      <pre>Rol: Senior Node.js Backend Muhandisi.
Texnologiya: Express va SQLite (users va orders jadvallari).

Vazifa: POST /api/orders marshrutini yoz.
Kiruvchi parametrlar (req.body):
- user_id (butun son, majburiy)
- product_name (matn, majburiy)
- amount (musbat son, majburiy)

Biznes Mantiq:
1. Agar maydonlar to'liq bo'lmasa: 400 Bad Request.
2. user_id mavjud bo'lmasa: 404 Not Found.
3. user.balance < amount bo'lsa: 400 Bad Request ("Mablag' yetarli emas").
4. Agar yetarli bo'lsa: user.balance -= amount, orders ga status='pending' bilan yoz va 201 Created qaytar.</pre>
    </div>
  </div>
</section>

<!-- SLIDE 6: KOD TAHLILI: USERS -->
<section class="slide" data-phase="Kod Tahlili|Разбор Кода|Code Breakdown" data-time="19–23">
  <div class="eyebrow"><span data-ru="Маршруты Пользователей" data-en="Users Endpoints">Users Marshrutlari</span></div>
  <h2 data-ru="Разбор Кода: GET и POST Маршруты для Users" data-en="Code Breakdown: GET & POST Routes for Users">Kod Tahlili: Users Uchun GET va POST Marshrutlari</h2>
  
  <div class="cols c2">
    <div class="box green">
      <h3 data-ru="1. GET /api/users и /api/users/:id" data-en="1. GET /api/users & /api/users/:id">1. Mijozlarni O'qish (GET)</h3>
      <pre>// Barcha foydalanuvchilar ro'yxati
app.get('/api/users', (req, res) => {
  res.status(200).json({
    success: true,
    count: users.length,
    users: users
  });
});

// Bitta foydalanuvchi va uning buyurtmalari
app.get('/api/users/:id', (req, res) => {
  const id = parseInt(req.params.id, 10);
  const user = users.find(u => u.id === id);
  if (!user) {
    return res.status(404).json({ error: "Topilmadi" });
  }
  // Relyatsion bog'lash:
  const userOrders = orders.filter(o => o.user_id === id);
  res.status(200).json({ user: { ...user, orders: userOrders } });
});</pre>
    </div>

    <div class="box blue">
      <h3 data-ru="2. POST /api/users (Создание Клиента)" data-en="2. POST /api/users (Customer Creation)">2. Yangi Mijoz Yaratish (POST)</h3>
      <pre>app.post('/api/users', (req, res) => {
  const { full_name, email, balance } = req.body;

  // 1. Validatsiya
  if (!full_name || !email) {
    return res.status(400).json({
      error: "full_name va email majburiy!"
    });
  }

  // 2. Email unikalligi tekshiruvi
  const exists = users.find(u => u.email === email);
  if (exists) {
    return res.status(400).json({ error: "Email band!" });
  }

  const newUser = {
    id: nextUserId++,
    full_name: full_name.trim(),
    email: email.trim().toLowerCase(),
    balance: Number(balance) || 0
  };
  users.push(newUser);

  res.status(201).json({ success: true, user: newUser });
});</pre>
    </div>
  </div>
</section>

<!-- SLIDE 7: KOD TAHLILI: ORDERS -->
<section class="slide" data-phase="Tranzaksiyalar|Транзакции|Transactions" data-time="23–27">
  <div class="eyebrow"><span data-ru="Финансовая Логика" data-en="Financial Logic">Tranzaksiya Mantig'i</span></div>
  <h2 data-ru="Разбор Кода: POST, PATCH и DELETE для Orders" data-en="Code Breakdown: POST, PATCH & DELETE for Orders">Kod Tahlili: Orders Uchun POST, PATCH va DELETE</h2>
  
  <div class="cols c2">
    <div class="box orange">
      <h3 data-ru="POST /api/orders (Списание Баланса)" data-en="POST /api/orders (Balance Deduction)">POST /api/orders (Balansdan Yechish)</h3>
      <pre>app.post('/api/orders', (req, res) => {
  const { user_id, product_name, amount } = req.body;
  const user = users.find(u => u.id === parseInt(user_id));

  if (!user) return res.status(404).json({ error: "Mijoz yo'q" });
  if (user.balance < amount) {
    return res.status(400).json({
      error: `Balans yetarli emas! Mavjud: ${user.balance} so'm`
    });
  }

  // Mablag' yechish va buyurtma yaratish
  user.balance -= amount;
  const newOrder = {
    id: nextOrderId++,
    user_id: user.id,
    product_name,
    amount,
    status: "pending"
  };
  orders.push(newOrder);

  res.status(201).json({ success: true, order: newOrder });
});</pre>
    </div>

    <div class="box purple">
      <h3 data-ru="PATCH & DELETE /api/orders/:id" data-en="PATCH & DELETE /api/orders/:id">PATCH va DELETE Marshrutlari</h3>
      <pre>// PATCH: Holatni o'zgartirish (pending -> completed)
app.patch('/api/orders/:id', (req, res) => {
  const order = orders.find(o => o.id === parseInt(req.params.id));
  if (!order) return res.status(404).json({ error: "Topilmadi" });

  const { status } = req.body;
  order.status = status; // completed yoki cancelled

  // Agar cancelled bo'lsa, pulni qaytarish (refund)
  if (status === 'cancelled') {
    const user = users.find(u => u.id === order.user_id);
    if (user) user.balance += order.amount;
  }

  res.status(200).json({ success: true, order });
});

// DELETE: O'chirish
app.delete('/api/orders/:id', (req, res) => {
  const idx = orders.findIndex(o => o.id === parseInt(req.params.id));
  if (idx === -1) return res.status(404).json({ error: "Topilmadi" });
  orders.splice(idx, 1);
  res.status(200).json({ message: "O'chirildi" });
});</pre>
    </div>
  </div>
</section>

<!-- SLIDE 8: POSTMAN TEST ASSERTIONS -->
<section class="slide" data-phase="Avtotestlar|Автотесты|Auto Tests" data-time="27–31">
  <div class="eyebrow"><span data-ru="Автоматизация Тестирования" data-en="Test Automation">Avtomatlashtirilgan Testlar</span></div>
  <h2 data-ru="Postman Test Scripts: Проверка Кода за 1 Миллисекунду" data-en="Postman Test Scripts: Validating Endpoints in 1 Millisecond">Postman Test Skriptlari: Natijalarni Avtomatik Tekshirish</h2>
  
  <div class="cols c2">
    <div class="box orange">
      <h3 data-ru="Что Такое pm.test()?" data-en="What is pm.test()?">pm.test() Nima?</h3>
      <p style="font-size:14px;" data-ru="Каждый раз, когда сервер возвращает ответ, Postman исполняет ваш JavaScript код во вкладке <b>Tests</b>. Если условие верно — тест зелёный (PASS), если нет — красный (FAIL)." data-en="Whenever the server returns a response, Postman runs your JavaScript code from the <b>Tests</b> tab. If conditions match, it renders green (PASS), otherwise red (FAIL).">Har safar serverdan javob kelganda, Postman <b>Tests</b> oynasidagi JavaScript kodini ishga tushiradi. Agar shart bajarilsa yashil (PASS), bajarilmasa qizil (FAIL) bo'ladi.</p>
      
      <pre>// 1. Status kod tekshiruvi
pm.test("Status 201 Created bo'lishi shart", function () {
    pm.response.to.have.status(201);
});

// 2. JSON javob tuzilmasini tekshirish
pm.test("Buyurtma statusi pending ekanligi", function () {
    var data = pm.response.json();
    pm.expect(data.order.status).to.eql("pending");
    pm.expect(data.order.amount).to.be.above(0);
});</pre>
    </div>

    <div class="box green">
      <h3 data-ru="Преимущества Test Runner" data-en="Benefits of Test Runner">Postman Collection Runner</h3>
      <ul class="plain">
        <li><span class="t" data-ru="<b>1 клик — 7 тестов:</b> Запуск всех маршрутов интернет-магазина за секунду." data-en="<b>1 click — 7 tests:</b> Execute every store route in under 2 seconds."><b>1 ta klik — 7 ta test:</b> Internet do'konning barcha so'rovlarini 1 soniyada tekshiradi.</span></li>
        <li><span class="t" data-ru="<b>Регрессионное тестирование:</b> Если вы изменили код в server.js, тесты сразу покажут, сломалось ли что-то." data-en="<b>Regression protection:</b> When editing server.js, tests immediately flag regressions."><b>Regressiya nazorati:</b> server.js da kod o'zgartirsangiz, biror narsa buzilganini bir zumda ko'rsatadi.</span></li>
        <li><span class="t" data-ru="<b>CI/CD Готовность:</b> Эти же тесты запускаются на GitHub Actions через утилиту Newman!" data-en="<b>CI/CD Ready:</b> The exact same tests run inside GitHub Actions via Newman CLI!"><b>CI/CD ga tayyor:</b> Shu testlar GitHub Actions da Newman orqali avtomatik ishlaydi!</span></li>
      </ul>
      <div style="background:var(--panel-2); padding:10px; border-radius:6px; margin-top:10px;">
        <span class="pill pill-green">PASS</span> <code>Status code is 200 (14ms)</code><br>
        <span class="pill pill-green">PASS</span> <code>User balance successfully deducted (18ms)</code><br>
        <span class="pill pill-green">PASS</span> <code>Order status is completed (12ms)</code>
      </div>
    </div>
  </div>
</section>

<!-- SLIDE 9: LABORATORIYA ARENASI -->
<section class="slide" data-phase="Laboratoriya|Лаборатория|Lab Arena" data-time="31–34">
  <div class="eyebrow"><span data-ru="Интерактивная Студия" data-en="Interactive Studio">Laboratoriya Arenasi</span></div>
  <h2 data-ru="Лаборатория: E-Commerce Backend & Postman Studio" data-en="Lab Arena: E-Commerce Backend & Postman Studio">Laboratoriya: E-Commerce Backend & Postman Studio</h2>
  
  <p class="lede" data-ru="В браузере запущена полноценная студия: реальный HTTP-движок Express, реляционная база Users & Orders, визуализатор таблиц в реальном времени и симулятор Postman!" data-en="A full-featured environment runs right in your browser: real Express HTTP engine, relational Users & Orders tables, real-time database viewer, and Postman workspace!">Brauzer ichida to'liq ishchi studiya ishga tushirildi: Express HTTP dvigateli, relyatsion Users & Orders bazasi, jadvallarning jonli monitori va interaktiv Postman muhiti!</p>

  <div class="cols c4">
    <div class="box blue">
      <span class="pill pill-blue">Kvest 1 (2.5 b)</span>
      <h3 style="margin-top:6px;" data-ru="Клиенты" data-en="Users">Mijozlar</h3>
      <p style="font-size:12.5px;" data-ru="GET /api/users va POST /api/users orqali yangi mijoz qo'shing." data-en="Use GET and POST /api/users to register a new customer.">GET va POST /api/users orqali yangi mijoz ro'yxatdan o'tkazing.</p>
    </div>
    <div class="box orange">
      <span class="pill pill-orange">Kvest 2 (2.5 b)</span>
      <h3 style="margin-top:6px;" data-ru="Заказ и Баланс" data-en="Order & Balance">Balans Nazorati</h3>
      <p style="font-size:12.5px;" data-ru="POST /api/orders bering. Mijoz balansidan mablag' yechilganini ko'ring." data-en="Place POST /api/orders. Verify funds deducted from user balance.">POST /api/orders bering. Mijoz hisobidan pul yechilishini tekshiring.</p>
    </div>
    <div class="box purple">
      <span class="pill pill-purple">Kvest 3 (2.5 b)</span>
      <h3 style="margin-top:6px;" data-ru="Статус PATCH" data-en="PATCH Status">PATCH Holati</h3>
      <p style="font-size:12.5px;" data-ru="PATCH /api/orders/2 yuborib statusni 'completed' ga o'tkazing." data-en="Send PATCH /api/orders/2 to change status to 'completed'.">PATCH /api/orders/2 yuborib statusni 'completed' ga o'zgartiring.</p>
    </div>
    <div class="box green">
      <span class="pill pill-green">Kvest 4 (2.5 b)</span>
      <h3 style="margin-top:6px;" data-ru="Тесты Postman" data-en="Postman Tests">Yashil Testlar</h3>
      <p style="font-size:12.5px;" data-ru="'Run All Tests' tugmasini bosing va 100% yashil natija oling." data-en="Click 'Run All Tests' and achieve 100% green test passes.">'Run All Tests' tugmasini bosing va 100% yashil natija oling.</p>
    </div>
  </div>

  <div style="margin-top:16px; text-align:center;">
    <a href="studio/index.html" target="_blank" style="display:inline-block; background:var(--orange); color:#fff; font-family:'Manrope',sans-serif; font-weight:800; font-size:16px; padding:12px 32px; border-radius:8px; text-decoration:none; box-shadow:0 4px 14px rgba(255,108,55,.4);" data-ru="🚀 Открыть E-Commerce & Postman Studio" data-en="🚀 Launch E-Commerce & Postman Studio">🚀 E-Commerce & Postman Studiyani Ochish</a>
  </div>
</section>

<!-- SLIDE 10: 12 DAQIQALIK REGLAMENT -->
<section class="slide" data-phase="Reglament|Регламент|Protocol" data-time="34–36">
  <div class="eyebrow"><span data-ru="Практический Тайминг" data-en="Lab Protocol">12 Daqiqalik Reglament</span></div>
  <h2 data-ru="12 Минут: Пошаговый Маршрут Выполнения Лабораторной" data-en="12 Minutes: Step-by-Step Lab Execution Protocol">12 Daqiqa: Amaliy Ishni Bajarish Bosqichlari</h2>
  
  <div class="cols c2">
    <div class="box green">
      <h3 data-ru="0–3 мин: Знакомство со Студией" data-en="0–3 min: Exploration & Discovery">0–3 daqiqa: Boshlang'ich Holatni Ko'rish</h3>
      <ul class="plain">
        <li><span class="t" data-ru="Откройте студию, переключите вкладки users и orders в правой панели." data-en="Open studio, inspect users and orders tabs on the right panel.">Studiyani oching, o'ng paneldagi users va orders jadvallarini ko'ring.</span></li>
        <li><span class="t" data-ru="Отправьте <code>GET /api/users</code> и получите JSON со списком из 3 клиентов." data-en="Execute <code>GET /api/users</code> to view the 3 seed customers in JSON."><code>GET /api/users</code> ni jo'nating va 3 ta mijoz ro'yxatini ko'ring.</span></li>
      </ul>

      <h3 style="margin-top:14px;" data-ru="3–7 мин: Создание Клиента и Заказ" data-en="3–7 min: User & Order Creation">3–7 daqiqa: Yangi Mijoz va Buyurtma</h3>
      <ul class="plain">
        <li><span class="t" data-ru="Отправьте <code>POST /api/users</code> с балансом 900 000 сум." data-en="Execute <code>POST /api/users</code> with 900,000 UZS balance."><code>POST /api/users</code> orqali 900 000 so'm balansli yangi mijoz qo'shing.</span></li>
        <li><span class="t" data-ru="Отправьте <code>POST /api/orders</code> на 180 000 сум. Убедитесь, что баланс уменьшился!" data-en="Execute <code>POST /api/orders</code> for 180,000 UZS. Verify balance drop!"><code>POST /api/orders</code> ga buyurtma bering va mijoz balansi kamayganini tekshiring!</span></li>
      </ul>
    </div>

    <div class="box orange">
      <h3 data-ru="7–10 мин: Обновление Статуса и Отмена" data-en="7–10 min: Status Lifecycle & Cancel">7–10 daqiqa: PATCH va DELETE Amallari</h3>
      <ul class="plain">
        <li><span class="t" data-ru="Отправьте <code>PATCH /api/orders/2</code> с телом <code>{ status: 'completed' }</code>." data-en="Execute <code>PATCH /api/orders/2</code> with <code>{ status: 'completed' }</code>."><code>PATCH /api/orders/2</code> ga <code>{ status: 'completed' }</code> yuboring.</span></li>
        <li><span class="t" data-ru="Проверьте, что в таблице orders статус стал зелёным (completed)." data-en="Confirm that the order badge in orders table turned green.">Jadvalda buyurtma statusi yashil (completed) bo'lganini tasdiqlang.</span></li>
      </ul>

      <h3 style="margin-top:14px;" data-ru="10–12 мин: Прогон Автотестов" data-en="10–12 min: Test Suite & Export">10–12 daqiqa: Postman Test Runner va Eksport</h3>
      <ul class="plain">
        <li><span class="t" data-ru="Нажмите кнопку <b>«Barcha Testlar»</b> (Run All Tests)." data-en="Click <b>«Run All Tests»</b> in the header.">Tepada <b>«Barcha Testlar»</b> tugmasini bosing.</span></li>
        <li><span class="t" data-ru="Добейтесь 10 / 10 баллов в трекере квестов и скачайте файл коллекции." data-en="Secure 10 / 10 points in the quest tracker and export collection file.">Kvestlar panelida 10 / 10 ball oling va kolleksiyani eksport qiling.</span></li>
      </ul>
    </div>
  </div>
</section>

<!-- SLIDE 11: TOP-3 XATO VA DEBUGGING -->
<section class="slide" data-phase="Debugging|Отладка|Debugging" data-time="36–38">
  <div class="eyebrow"><span data-ru="Ошибки Разработчиков" data-en="Common Pitfalls">Debugging va Xatolar</span></div>
  <h2 data-ru="Топ-3 Ошибок при Разработке API в Postman" data-en="Top 3 API Engineering Traps in Postman">Junior Dasturchilarning Postmanda Top-3 Xatosi</h2>
  
  <div class="cols c3">
    <div class="box accent">
      <span class="pill pill-accent">Xato 1</span>
      <h3 style="margin-top:6px;" data-ru="Забыт Content-Type" data-en="Missing Content-Type">Content-Type Unutilishi</h3>
      <p style="font-size:13px;" data-ru="Если в Postman не выбрать <code>raw ➔ JSON</code>, заголовок <code>Content-Type: application/json</code> не отправится. Сервер не сможет распарсить body, и <code>req.body</code> будет пустым <code>undefined</code>!" data-en="If raw ➔ JSON is omitted in Postman, <code>Content-Type</code> is missing. Express cannot parse body, leaving <code>req.body</code> undefined!">Postman da <code>raw ➔ JSON</code> tanlanmasa, server <code>req.body</code> ni o'qiy olmaydi va u bo'sh (undefined) bo'lib qoladi!</p>
    </div>

    <div class="box orange">
      <span class="pill pill-orange">Xato 2</span>
      <h3 style="margin-top:6px;" data-ru="Путаница с PUT и PATCH" data-en="PUT vs PATCH Confusion">PUT va PATCH ni Adashtirish</h3>
      <p style="font-size:13px;" data-ru="Отправка <code>PUT /api/orders/2</code> с телом <code>{ status: 'completed' }</code> сотрёт имя товара и сумму, если роут ожидает полный объект! Для частичных изменений всегда используйте <b>PATCH</b>." data-en="Sending <code>PUT</code> with only <code>{ status: 'completed' }</code> wipes product_name and amount! Always use <b>PATCH</b> for partial updates.">Faqat statusni o'zgartirish uchun PUT yuborilsa, boshqa hamma maydonlar o'chib ketishi mumkin! Doimo <b>PATCH</b> dan foydalaning.</p>
    </div>

    <div class="box purple">
      <span class="pill pill-purple">Xato 3</span>
      <h3 style="margin-top:6px;" data-ru="Строка Вместо Числа" data-en="String vs Number Types">Matn va Raqam Xatosi</h3>
      <p style="font-size:13px;" data-ru="Передача <code>amount: '180000'</code> вместо числа приводит к ошибке конкатенации строк: <code>500000 - '180000'</code> может дать неожиданный результат в SQL. Всегда используйте <code>parseInt()</code> или <code>Number()</code>." data-en="Passing <code>amount: '180000'</code> as a string breaks arithmetic logic. Always cast inputs via <code>parseInt()</code> or <code>Number()</code>.">Raqam o'rniga matn yuborilsa, pul hisob-kitoblarida jiddiy xato kelib chiqadi. Doimo <code>Number(amount)</code> orqali tekshiring.</p>
    </div>
  </div>
</section>

<!-- SLIDE 12: XULOSA VA BAHOLASH MEZONI -->
<section class="slide" data-phase="Xulosa|Итоги|Wrap-Up" data-time="38–40">
  <div class="eyebrow"><span data-ru="Итоги и Оценка" data-en="Wrap-Up & Grading">Xulosa va Baholash</span></div>
  <h2 data-ru="Итоги Урока, Домашнее Задание и Критерии Оценки" data-en="Lesson Wrap-Up, Homework & 10-Point Grading Rubric">Dars Xulosasi, Uy Vazifasi va 10 Ballik Baholash Mezoni</h2>
  
  <div class="cols c2">
    <div class="box green">
      <h3 data-ru="Что Мы Освоили Сегодня" data-en="Core Competencies Mastered">Bugun O'zlashtirilgan Ko'nikmalar</h3>
      <ul class="plain">
        <li><span class="t" data-ru="E-Commerce реляционную архитектуру (Users ➔ Orders) с внешними ключами." data-en="E-Commerce relational schema (Users ➔ Orders) with foreign keys.">Users va Orders relyatsion jadvallari va tashqi kalitlar mantiqi.</span></li>
        <li><span class="t" data-ru="Финансовую валидацию на стороне сервера (проверка баланса)." data-en="Server-side balance guard against client-side tampering.">Serverda mijoz hisob balansini qat'iy tekshirish va mablag' yechish.</span></li>
        <li><span class="t" data-ru="Полный стек CRUD: GET, POST, PATCH (статус заказа) и DELETE." data-en="Complete CRUD cycle: GET, POST, PATCH (order lifecycle), and DELETE.">To'liq CRUD tsikli: GET, POST, PATCH (holat o'zgartirish) va DELETE.</span></li>
        <li><span class="t" data-ru="Тестирование через Postman с автоматическими скриптами <code>pm.test()</code>." data-en="API verification in Postman backed by automated <code>pm.test()</code> suites.">Postman muhiti va <code>pm.test()</code> avtomatlashtirilgan test skriptlari.</span></li>
      </ul>
      <div style="background:var(--panel-2); padding:10px; border-radius:6px; margin-top:8px;">
        <span class="pill pill-orange" data-ru="Мост к Уроку 20" data-en="Bridge to Lesson 20">20-darsga Ko'prik</span>
        <p style="margin:4px 0 0; font-size:13px;" data-ru="В 20-уроке мы задеплоим этот готовый бэкенд в облако (Railway/Render) и подключим к реальному веб-фронтенду!" data-en="In lesson 20, we deploy this backend to the cloud (Railway/Render) and link it to our interactive frontend!">20-darsda ushbu tayyor backendni bulutga (Railway/Render) deploy qilamiz va to'liq Full-Stack ilovaga aylantiramiz!</p>
      </div>
    </div>

    <div class="box purple">
      <h3 data-ru="10-Балльная Шкала Оценки" data-en="10-Point Assessment Rubric">10 Ballik Baholash Mezoni</h3>
      <table class="tbl" style="margin-top:6px;">
        <thead>
          <tr>
            <th data-ru="Квест" data-en="Quest">Kvest</th>
            <th data-ru="Действие" data-en="Action">Amal</th>
            <th data-ru="Балл" data-en="Points">Ball</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td data-ru="<b>Квест 1</b>" data-en="<b>Quest 1</b>"><b>Kvest 1</b></td>
            <td data-ru="GET /api/users и POST /api/users (Регистрация клиента)" data-en="GET /api/users & POST /api/users (User creation)">Mijozlarni olish va yangi mijoz yaratish (POST)</td>
            <td data-ru="<b>2.5 балла</b>" data-en="<b>2.5 pts</b>"><b>2.5 ball</b></td>
          </tr>
          <tr>
            <td data-ru="<b>Квест 2</b>" data-en="<b>Quest 2</b>"><b>Kvest 2</b></td>
            <td data-ru="POST /api/orders со списанием средств с баланса" data-en="POST /api/orders with balance validation">Buyurtma berish va balans kamayishini tekshirish</td>
            <td data-ru="<b>2.5 балла</b>" data-en="<b>2.5 pts</b>"><b>2.5 ball</b></td>
          </tr>
          <tr>
            <td data-ru="<b>Квест 3</b>" data-en="<b>Quest 3</b>"><b>Kvest 3</b></td>
            <td data-ru="PATCH /api/orders/:id со сменой статуса на 'completed'" data-en="PATCH /api/orders/:id changing status to 'completed'">Buyurtma statusini PATCH orqali 'completed' qilish</td>
            <td data-ru="<b>2.5 балла</b>" data-en="<b>2.5 pts</b>"><b>2.5 ball</b></td>
          </tr>
          <tr>
            <td data-ru="<b>Квест 4</b>" data-en="<b>Quest 4</b>"><b>Kvest 4</b></td>
            <td data-ru="100% зелёный прогон автотестов в Postman (Run All Tests)" data-en="100% green test assertions run in Postman">Postman avtotestlarini 100% yashil o'tkazish</td>
            <td data-ru="<b>2.5 балла</b>" data-en="<b>2.5 pts</b>"><b>2.5 ball</b></td>
          </tr>
        </tbody>
      </table>
      <div style="font-size:12.5px; color:var(--ink-2); margin-top:6px;" data-ru="<b>Домашнее задание:</b> Добавьте в server.js эндпоинт <code>GET /api/users/:id/orders</code>, возвращающий заказы конкретного пользователя, и протестируйте в Postman." data-en="<b>Homework:</b> Add <code>GET /api/users/:id/orders</code> to server.js returning filtered orders for a specific user, and verify it in Postman."><b>Uy vazifasi:</b> server.js ga faqat bitta mijozning buyurtmalarini qaytaruvchi <code>GET /api/users/:id/orders</code> marshrutini qo'shing va Postmanda tekshiring.</div>
    </div>
  </div>
</section>

</div>

<!-- BOTTOM CONTROL BAR -->
<div class="bar">
  <div class="bar-left">
    <div class="brandmark bar-mark">
      <img src="../../../assets/target-logo.png" alt="Target School Logo" class="on-light" style="height:24px; width:auto;">
      <img src="../../../assets/target-logo.png" alt="Target School Logo" class="on-dark" style="height:24px; width:auto; filter:brightness(0) invert(1);">
    </div>
    <span class="phase" id="phaseTag">Kirish</span>
    <span class="count"><span id="count">1 / 12</span></span>
    <span class="timer" id="timer" title="Taymerni to'xtatish / boshlash" data-title-ru="Остановить / запустить таймер" data-title-en="Pause / resume timer">40:00</span>
  </div>

  <div class="bar-right">
    <button class="btn-ctrl" id="prevBtn" title="Oldingi slayd (←)" data-title-ru="Предыдущий слайд (←)" data-title-en="Previous slide (←)">←</button>
    <button class="btn-ctrl" id="nextBtn" title="Keyingi slayd (→)" data-title-ru="Следующий слайд (→)" data-title-en="Next slide (→)">→</button>
    <button class="btn-ctrl" id="notesBtn" title="O'qituvchi izohlari (N)" data-title-ru="Заметки преподавателя (N)" data-title-en="Teacher notes (N)">N</button>
    
    <div style="display:inline-flex; gap:2px; margin-left:6px;">
      <button class="btn-lang active" data-lang="uz">UZ</button>
      <button class="btn-lang" data-lang="ru">RU</button>
      <button class="btn-lang" data-lang="en">EN</button>
    </div>

    <button class="btn-ctrl" id="themeBtn" title="Mavzuni almashtirish (T)" data-title-ru="Переключить тему (T)" data-title-en="Toggle theme (T)">🌓</button>
  </div>
</div>

<!-- SPEAKER NOTES PANE -->
<div class="notes-pane" id="notesPane">
  <div class="notes-title" id="notesTitle">O'qituvchi Izohi</div>
  <p class="notes-text" id="notesText"></p>
</div>

<script>
var slides = document.querySelectorAll('.slide');
var cur = 0;
var total = slides.length;
var timerEl = document.getElementById('timer');
var countEl = document.getElementById('count');
var phaseTag = document.getElementById('phaseTag');
var notesPane = document.getElementById('notesPane');
var notesTitle = document.getElementById('notesTitle');
var notesText = document.getElementById('notesText');
var currentLang = 'uz';

var NOTES = {
  "uz": [
    [
      "Titul slayd",
      "Bugungi dars — 19-dars (Backend asoslari) va 20-dars (Deploy) oralig'idagi amaliy ko'prik. O'quvchilar real elektron tijorat tizimida Users va Orders jadvallarini, moliyaviy balans tekshiruvini va Postman avtotestlarini o'rganadilar.",
      "Proyektorda studio/index.html ni oldindan ochib qo'ying."
    ],
    [
      "E-Commerce Arxitekturasi",
      "Relyatsion bog'lanish va tashqi kalit (Foreign Key) mohiyatini tushuntiring: buyurtma o'z-o'zidan mavjud bo'la olmaydi, u qaysidir mijozga tegishli. Moliyaviy balans nazorati nega faqat serverda bo'lishi shartligini ta'kidlang.",
      "Doskada Users va Orders jadvallarining bog'lanishini chizing."
    ],
    [
      "REST CRUD va PATCH vs PUT",
      "O'quvchilarga PUT va PATCH farqini jonli misol bilan tushuntiring: buyurtmaning faqat statusini completed qilish uchun PUT ishlatsak, mahsulot nomi va summa o'chib ketishi xavfi bor. PATCH esa faqat kerakli maydonni o'zgartiradi.",
      "O'quvchilardan status kodlar ma'nosini so'rang (201 vs 400)."
    ],
    [
      "Postman Vositalari",
      "Nega brauzerning o'zi yetarli emas? Chunki brauzer URL qatori faqat GET so'rov yubora oladi. POST, PATCH, DELETE va JSON Body yuborish uchun professional HTTP mijoz kerak.",
      "Postman butun dunyoda backend muhandislarining standart ish quroli ekanligini ayting."
    ],
    [
      "Vibecoding Prompt Texnikasi",
      "Cursor yoki ChatGPT ga backend kodi yozdirishda sxemani, maydonlarni va status kodlarni aniq bermasak, zaif kod hosil bo'ladi. Prompt muhandisligi qoidalarini ko'rsating.",
      "Keltirilgan professional prompt namunasini tahlil qiling."
    ],
    [
      "Kod Tahlili: Users",
      "GET /api/users va POST /api/users kodini tahlil qiling. req.body dan ma'lumotlarni olish, email unikalligini tekshirish va 201 Created kodi bilan javob qaytarishni tushuntiring.",
      "O'quvchilar e'tiborini status kodlarga qarating."
    ],
    [
      "Kod Tahlili: Orders va Tranzaksiya",
      "POST /api/orders dagi user.balance -= amount mantiqiy tekshiruvini ko'rsating. Agar balans yetarli bo'lmasa, buyurtma rad etiladi (400). PATCH dagi refund (pulni qaytarish) mantiqini tushuntiring.",
      "Bu bank va to'lov tizimlarining eng asosiy poydevori."
    ],
    [
      "Postman Avtotestlari (pm.test)",
      "Har safar qo'lda tekshirmaymiz: pm.test() yordamida status kodlar va ma'lumotlar avtomatik tekshiriladi. Collection Runner bir tugma bilan barcha 7 ta so'rovni tekshirishini ko'rsating.",
      "Testlarning yashil nishonlari muhandislik kafolati ekanini ayting."
    ],
    [
      "Laboratoriya Arenasi",
      "O'quvchilarga studio/index.html ni ochishni ayting. 4 ta amaliy kvest va har biri 2.5 balldan jami 10 ballik mezon borligini e'lon qiling.",
      "Har bir o'quvchi o'z kompyuterida studiyani ishga tushirsin."
    ],
    [
      "12 Daqiqalik Reglament",
      "Vaqt taqsimotini qat'iy nazorat qiling: 0-3 daqiqa GET, 3-7 daqiqa POST, 7-10 daqiqa PATCH/DELETE, 10-12 daqiqa avtotestlar va natijalarni tekshirish.",
      "Taymerni ishga tushiring."
    ],
    [
      "Top-3 API Xatosi va Debugging",
      "Eng ko'p uchraydigan 3 ta xatoni tahlil qiling: Content-Type unutilishi (req.body undefined bo'lib qoladi), PUT/PATCH adashishi va satr/raqam chalkashishi.",
      "Konsolda xato chiqqan o'quvchilarga yordam bering."
    ],
    [
      "Xulosa va 10 Ballik Mezon",
      "Darsni sarhisob qiling. Har bir o'quvchining olgan balini daftarga yoki tizimga qayd eting. 20-darsda ushbu backend bulutga deploy qilinishini aytib qiziqish uyg'oting.",
      "Varaqadagi xulosa qismini to'ldirishni buyuring."
    ]
  ],
  "ru": [
    [
      "Титульный слайд",
      "Практический мост между 19-м и 20-м уроками. Ученики строят живой E-Commerce бэкенд на связке Users & Orders с проверкой баланса и автотестами в Postman.",
      "Откройте studio/index.html на проекторе."
    ],
    [
      "Архитектура E-Commerce",
      "Объясните внешние ключи (Foreign Keys): заказ всегда привязан к клиенту. Разберите финансовую валидацию на стороне сервера.",
      "Нарисуйте связь таблиц на доске."
    ],
    [
      "REST CRUD и PATCH vs PUT",
      "Разберите разницу между PUT и PATCH. Объясните, почему для смены статуса заказа используется именно PATCH.",
      "Спросите учеников о статус-кодах 201 и 400."
    ],
    [
      "Инструменты Postman",
      "Почему браузера недостаточно? Браузер отправляет только GET. Для POST/PATCH/DELETE нужен специализированный клиент.",
      "Подчеркните, что Postman — индустриальный стандарт."
    ],
    [
      "Техника Вайбкодинга",
      "Как формулировать промпты для AI, чтобы получать надежный и валидированный код бэкенда.",
      "Разберите шаблон профессионального промпта."
    ],
    [
      "Разбор Кода: Users",
      "Анализ GET и POST маршрутов для пользователей. Валидация уникальности email и возврат 201 Created.",
      "Обратите внимание на структуру ответа."
    ],
    [
      "Разбор Кода: Orders и Транзакции",
      "Логика списания баланса user.balance -= amount. Защита от отрицательного баланса и возврат средств при отмене.",
      "Это фундаментальная логика платежных систем."
    ],
    [
      "Автотесты в Postman",
      "Автоматизация проверок через pm.test(). Collection Runner как инструмент регрессионного тестирования.",
      "Зеленые тесты — гарантия качества кода."
    ],
    [
      "Лабораторная Арена",
      "Анонс практической работы в studio/index.html. 4 квеста по 2.5 балла (всего 10 баллов).",
      "Ученики открывают студию на своих ПК."
    ],
    [
      "Регламент 12 Минут",
      "Тайминг: 0-3 мин GET, 3-7 мин POST, 7-10 мин PATCH, 10-12 мин автотесты и экспорт.",
      "Запустите таймер на проекторе."
    ],
    [
      "Топ-3 Ошибок и Отладка",
      "Забытый Content-Type, путаница PUT/PATCH, передача строк вместо чисел.",
      "Помогите ученикам с ошибками в консоли."
    ],
    [
      "Итоги и 10 Баллов",
      "Подведение итогов, фиксация оценок по 10-балльной шкале. Анонс деплоя в 20-м уроке.",
      "Заполните рабочие листы."
    ]
  ],
  "en": [
    [
      "Title Slide",
      "Practical bridge between Lesson 19 (Express basics) and Lesson 20 (Cloud Deploy). Students build an E-Commerce backend with Users, Orders, balance checks, and automated Postman test suites.",
      "Pre-open studio/index.html on projector."
    ],
    [
      "E-Commerce Architecture",
      "Explain relational models and Foreign Keys: an order strictly belongs to a user. Emphasize why financial balance checks must live strictly on the server.",
      "Draw the Users-Orders relationship on the board."
    ],
    [
      "REST CRUD & PATCH vs PUT",
      "Explain why PATCH is preferred over PUT for order lifecycle updates to avoid wiping existing attributes.",
      "Quiz students on HTTP 201 vs 400."
    ],
    [
      "Postman Tooling",
      "Why browser alone fails: address bar is strictly GET. Postman enables headers, JSON payloads, and automated test runners.",
      "Explain Postman as the industry standard."
    ],
    [
      "Vibecoding Prompt Technique",
      "Engineering precise prompts for Cursor and AI models to generate resilient, validated backend code.",
      "Analyze the professional prompt structure."
    ],
    [
      "Code Walkthrough: Users",
      "Analyze GET /api/users and POST /api/users. Explain payload validation, unique email enforcement, and 201 status.",
      "Highlight JSON response contracts."
    ],
    [
      "Code Walkthrough: Orders & Transactions",
      "Explain user.balance -= amount guardrails and refund logic on cancelled orders.",
      "Core foundation of fintech systems."
    ],
    [
      "Postman Test Scripts",
      "Automated validations with pm.test(). Running entire test suites via Collection Runner.",
      "Green badges represent engineering confidence."
    ],
    [
      "Lab Arena",
      "Direct students to studio/index.html. Outline 4 quests worth 2.5 points each (10 points total).",
      "Ensure students launch the studio on laptops."
    ],
    [
      "12-Minute Protocol",
      "Strict timing: 0-3m GET, 3-7m POST, 7-10m PATCH/DELETE, 10-12m test execution & export.",
      "Start the countdown timer."
    ],
    [
      "Top 3 API Pitfalls & Debugging",
      "Missing Content-Type header, PUT vs PATCH confusion, and string vs number type mismatches.",
      "Assist students observing console errors."
    ],
    [
      "Wrap-Up & 10-Point Rubric",
      "Wrap-up lesson deliverables, record 10-point grades, and build anticipation for cloud deployment in Lesson 20.",
      "Sign off worksheets."
    ]
  ]
};

function showSlide(n) {
  slides[cur].classList.remove('active');
  cur = (n + total) % total;
  slides[cur].classList.add('active');
  countEl.textContent = (cur + 1) + ' / ' + total;

  var phase = slides[cur].dataset.phase || "Kirish|Введение|Introduction";
  var parts = phase.split('|');
  var pIdx = currentLang === 'ru' ? 1 : currentLang === 'en' ? 2 : 0;
  phaseTag.textContent = parts[pIdx] || parts[0];

  updateNotes();
}

function updateNotes() {
  var langNotes = NOTES[currentLang] || NOTES['uz'];
  var item = langNotes[cur] || ["Izoh", "Ushbu slayd bo'yicha ko'rsatma", ""];
  notesTitle.textContent = item[0];
  notesText.innerHTML = "<b>Ko'rsatma:</b> " + item[1] + (item[2] ? "<br><b>Tavsiya:</b> " + item[2] : "");
}

document.getElementById('prevBtn').onclick = function(){ showSlide(cur - 1); };
document.getElementById('nextBtn').onclick = function(){ showSlide(cur + 1); };

document.getElementById('notesBtn').onclick = function(){
  notesPane.classList.toggle('open');
};

document.addEventListener('keydown', function(e){
  if (e.key === 'ArrowRight' || e.key === ' ') { showSlide(cur + 1); }
  else if (e.key === 'ArrowLeft') { showSlide(cur - 1); }
  else if (e.key.toLowerCase() === 'n') { notesPane.classList.toggle('open'); }
  else if (e.key === 'Escape') { notesPane.classList.remove('open'); }
  else if (e.key.toLowerCase() === 't') { toggleTheme(); }
});

// LANGUAGE TOGGLE
var langBtns = document.querySelectorAll('.btn-lang');
function setLanguage(lang) {
  currentLang = lang;
  langBtns.forEach(function(b){ b.classList.toggle('active', b.dataset.lang === lang); });
  document.querySelectorAll('[data-' + lang + ']').forEach(function(el){
    el.innerHTML = el.getAttribute('data-' + lang);
  });
  showSlide(cur);
  localStorage.setItem('target_lang', lang);
}
langBtns.forEach(function(b){
  b.onclick = function(){ setLanguage(b.dataset.lang); };
});

// THEME TOGGLE
function toggleTheme() {
  var current = document.documentElement.getAttribute('data-theme');
  var next = current === 'dark' ? 'light' : 'dark';
  document.documentElement.setAttribute('data-theme', next);
  localStorage.setItem('target_theme', next);
}
document.getElementById('themeBtn').onclick = toggleTheme;

// TIMER
var timeLeft = 40 * 60;
var timerRunning = true;
var timerInterval = setInterval(function(){
  if (!timerRunning) return;
  if (timeLeft <= 0) { clearInterval(timerInterval); return; }
  timeLeft--;
  var m = Math.floor(timeLeft / 60);
  var s = timeLeft % 60;
  timerEl.textContent = (m < 10 ? '0' : '') + m + ':' + (s < 10 ? '0' : '') + s;
}, 1000);
timerEl.onclick = function(){ timerRunning = !timerRunning; };

// INIT
showSlide(0);
var savedTheme = localStorage.getItem('target_theme');
if (savedTheme) document.documentElement.setAttribute('data-theme', savedTheme);
var savedLang = localStorage.getItem('target_lang');
if (savedLang) setLanguage(savedLang);
</script>
</body>
</html>
'''

target_path = "/home/dpdp/target/classes/9-sinf/4-hafta/19.5-dars-ecommerce-backend-va-postman/prezentatsiya.html"
with open(target_path, "w", encoding="utf-8") as f:
    f.write(presentation_content)

print(f"Prezentatsiya created successfully at: {target_path} ({len(presentation_content)} bytes)")
