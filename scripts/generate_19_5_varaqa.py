import os

varaqa_content = '''<!DOCTYPE html>
<html lang="uz">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>19.5-dars: Vibecoding E-Commerce Backend & Postman — Ishchi Varaqa</title>
<link rel="icon" type="image/svg+xml" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 96 96'%3E%3Cstyle%3E:root%7B--n:%2300214A;--r:%23FF1100%7D@media(prefers-color-scheme:dark)%7B:root%7B--n:%23FFFFFF;--r:%23FF3B26%7D%7D.nf%7Bfill:var(--n)%7D.ns%7Bstroke:var(--n);fill:none%7D.rf%7Bfill:var(--r)%7D.rs%7Bstroke:var(--r);fill:none%7D%3C/style%3E%3Cpath class='ns' stroke-width='11.5' d='M54.5 7.9A40.5 40.5 0 0 1 88.1 41.5M88.1 54.5A40.5 40.5 0 0 1 54.5 88.1M41.5 88.1A40.5 40.5 0 0 1 7.9 54.5M7.9 41.5A40.5 40.5 0 0 1 41.5 7.9'/%3E%3Ccircle class='rs' cx='48' cy='48' r='17.2' stroke-width='7.2'/%3E%3Crect class='rf' x='45.6' y='3' width='4.8' height='28' rx='.5'/%3E%3Crect class='rf' x='45.6' y='65' width='4.8' height='28' rx='.5'/%3E%3Crect class='rf' x='3' y='45.6' width='28' height='4.8' rx='.5'/%3E%3Crect class='rf' x='65' y='45.6' width='28' height='4.8' rx='.5'/%3E%3Ccircle class='nf' cx='48' cy='48' r='7.2'/%3E%3C/svg%3E">
<link rel="alternate icon" type="image/png" sizes="32x32" href="/assets/favicon-32x32.png">
<link rel="apple-touch-icon" sizes="180x180" href="/assets/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Manrope:wght@500;700;800&family=Source+Sans+3:wght@400;600;700&family=JetBrains+Mono:wght@400;700&display=swap">
<style>
:root{
  --bg:#C9D6E8; --sheet:#FFFFFF; --panel:#EDF2F9; --panel-2:#DEE7F3;
  --grid:rgba(0,33,74,.05);
  --ink:#00214A; --ink-2:#46587A; --ink-3:#8496B0;
  --rule:#C4D2E4; --hair:#DCE5F0;
  --accent:#FF1100; --accent-ink:#C21000; --accent-soft:#FFE7E3;
  --green:#0B6B4F;
  --orange:#FF6C37;
  --write:#AFC0D6;
}
@media (prefers-color-scheme: dark){
  :root:not([data-theme="light"]){
    --bg:#03101F; --sheet:#0A1D3D; --panel:#102550; --panel-2:#183260;
    --grid:rgba(232,238,247,.05);
    --ink:#E9EFF8; --ink-2:#A2B4CE; --ink-3:#70859F;
    --rule:#22406B; --hair:#1A3358;
    --accent:#FF3B26; --accent-ink:#FF7563; --accent-soft:#3B140F;
    --green:#7FD3B2;
    --orange:#FF7C4D;
    --write:#2E4A73;
  }
}
:root[data-theme="dark"]{
  --bg:#03101F; --sheet:#0A1D3D; --panel:#102550; --panel-2:#183260;
  --grid:rgba(232,238,247,.05);
  --ink:#E9EFF8; --ink-2:#A2B4CE; --ink-3:#70859F;
  --rule:#22406B; --hair:#1A3358;
  --accent:#FF3B26; --accent-ink:#FF7563; --accent-soft:#3B140F;
  --green:#7FD3B2;
  --orange:#FF7C4D;
  --write:#2E4A73;
}

*{box-sizing:border-box}
body{
  background:var(--bg); margin:0; padding:20px 16px;
  font-family:"Source Sans 3",sans-serif; color:var(--ink); font-size:9.4pt; line-height:1.42;
}

.noprint{
  max-width:210mm; margin:0 auto 16px; display:flex; gap:12px; align-items:center; justify-content:space-between; flex-wrap:wrap;
  font-family:"JetBrains Mono",monospace; font-size:8.8pt; color:var(--ink-3);
}
.noprint-left{display:flex; gap:10px; align-items:center;}
.noprint-right{display:flex; gap:10px; align-items:center;}
.noprint #printBtn{
  font-family:inherit; font-size:8.8pt; font-weight:700; letter-spacing:.05em;
  padding:7px 16px; background:var(--ink); color:var(--sheet); border:0; cursor:pointer; border-radius:4px;
  transition:.15s;
}
.noprint #printBtn:hover{background:var(--accent);}
.noprint .btn-sub{
  font-family:inherit; font-size:8.8pt; padding:6px 12px; background:var(--sheet);
  border:1px solid var(--rule); color:var(--ink); cursor:pointer; border-radius:4px;
}
.noprint .langs{display:inline-flex; border:1px solid var(--rule); border-radius:4px; overflow:hidden;}
.noprint .langs button{
  font-family:inherit; font-size:8.8pt; font-weight:700; padding:6px 10px;
  background:var(--sheet); border:0; color:var(--ink-3); cursor:pointer;
}
.noprint .langs button.is-on{background:var(--ink); color:var(--sheet);}

.sheet{
  width:210mm; min-height:297mm; max-height:297mm; margin:0 auto 20px; background:var(--sheet);
  box-shadow:0 8px 30px rgba(0,33,74,.18); padding:16mm 18mm 14mm;
  position:relative; display:flex; flex-direction:column; justify-content:space-between;
  overflow:hidden; box-sizing:border-box;
}

.sheet::before{
  content:""; position:absolute; top:0; left:0; right:0; height:4px;
  background:linear-gradient(90deg, #FF1100 0%, #00214A 50%, #0B6B4F 100%);
}

.sheet-head{
  display:grid; grid-template-columns:auto 1fr auto; gap:14px; align-items:center;
  border-bottom:1.5px solid var(--rule); padding-bottom:10px; margin-bottom:12px;
}
.logo-block img{height:30px; width:auto; display:block;}
:root[data-theme="dark"] .logo-block img{filter:brightness(0) invert(1);}
@media (prefers-color-scheme: dark){
  :root:not([data-theme="light"]) .logo-block img{filter:brightness(0) invert(1);}
}

.head-title h1{
  font-family:"Manrope",sans-serif; font-size:13.5pt; font-weight:800; line-height:1.2;
  margin:0; color:var(--ink); letter-spacing:-.01em;
}
.head-title .sub{
  font-size:8.4pt; color:var(--ink-2); margin-top:2px; font-weight:600;
}
.head-badges{
  display:flex; flex-direction:column; align-items:flex-end; gap:3px;
  font-family:"JetBrains Mono",monospace; font-size:7.4pt;
}
.badge{
  padding:2px 7px; border-radius:3px; font-weight:700; text-transform:uppercase; letter-spacing:.05em;
}
.badge-red{background:var(--accent-soft); color:var(--accent-ink); border:1px solid var(--accent);}
.badge-blue{background:var(--panel-2); color:var(--ink); border:1px solid var(--rule);}
.badge-orange{background:#FFF0EA; color:#FF6C37; border:1px solid #FF6C37;}

.pupil-grid{
  display:grid; grid-template-columns:2fr 1fr 1fr; gap:12px;
  background:var(--panel); border:1px solid var(--rule); border-radius:6px;
  padding:7px 12px; margin-bottom:12px; font-size:8.8pt;
}
.pupil-field{display:flex; align-items:center; gap:6px;}
.pupil-field label{font-weight:700; color:var(--ink-2); white-space:nowrap;}
.pupil-field .line{flex:1; border-bottom:1px dotted var(--write); height:14px;}

.sec-title{
  font-family:"Manrope",sans-serif; font-size:9.8pt; font-weight:800;
  text-transform:uppercase; letter-spacing:.05em; color:var(--ink);
  display:flex; align-items:center; gap:6px; margin:0 0 6px;
  border-left:3px solid var(--accent); padding-left:7px;
}

.block{margin-bottom:12px;}

.grid-2{display:grid; grid-template-columns:1fr 1fr; gap:12px;}
.grid-3{display:grid; grid-template-columns:1fr 1fr 1fr; gap:10px;}

.box{
  background:var(--panel); border:1px solid var(--rule); border-radius:6px; padding:9px 11px;
}

.tbl{
  width:100%; border-collapse:collapse; font-size:8.4pt; margin:4px 0 6px;
}
.tbl th, .tbl td{
  border:1px solid var(--rule); padding:5px 8px; text-align:left;
}
.tbl th{
  background:var(--panel-2); font-family:"JetBrains Mono",monospace; font-weight:700;
  color:var(--ink); font-size:7.8pt;
}

.mono-box{
  background:var(--panel-2); border:1px solid var(--rule); border-radius:4px;
  padding:6px 9px; font-family:"JetBrains Mono",monospace; font-size:8.2pt;
  line-height:1.4; color:var(--ink);
}

.write-area{
  border:1px dashed var(--write); border-radius:4px; background:var(--panel);
  min-height:44px; padding:6px 8px; display:flex; flex-direction:column; justify-content:space-around;
}
.write-line{border-bottom:1px solid var(--hair); height:16px;}

.rubric-list{
  list-style:none; padding:0; margin:0; font-size:8.5pt; display:grid; gap:4px;
}
.rubric-list li{
  display:flex; justify-content:space-between; align-items:center;
  padding:4px 8px; background:var(--panel); border:1px solid var(--rule); border-radius:4px;
}

.sign-box{
  border-top:1.5px solid var(--rule); padding-top:8px; margin-top:8px;
  display:flex; justify-content:space-between; align-items:center;
  font-family:"JetBrains Mono",monospace; font-size:7.4pt; color:var(--ink-3);
}

@media print {
  :root,
  :root:not([data-theme="light"]),
  :root[data-theme="dark"],
  :root[data-theme="light"]{
    --bg:#fff; --sheet:#fff; --panel:transparent; --panel-2:transparent;
    --grid:transparent; --ink:#000; --ink-2:#333; --ink-3:#5E5E5E;
    --rule:#8C8C8C; --hair:#C6C6C6;
    --accent:#000; --accent-ink:#000; --accent-soft:transparent;
    --green:#000; --orange:#000; --write:#B4B4B4;
  }
  body{background:#fff; padding:0; margin:0}
  .noprint{display:none !important}
  .sheet{box-shadow:none; width:210mm; min-height:297mm; max-height:297mm; padding:8mm 10mm; border:0; page-break-after:avoid; break-after:avoid;}
  .box{background:none; border-color:#888}
  .tbl th{background:none; color:#000; border-color:#888}
  .tbl td{border-color:#888}
  .mono-box{background:none; border-color:#888}
}
@page{ size:A4; margin:10mm; }
</style>
</head>
<body>

<div class="noprint">
  <div class="noprint-left">
    <button id="printBtn" data-ru="🖨️ ЧАСТЬ / ПЕЧАТЬ" data-en="🖨️ PRINT WORKSHEET">🖨️ CHOP ETISH</button>
    <a href="studio/index.html" class="btn-sub" target="_blank" style="text-decoration:none;" data-ru="⚡ Открыть Студию" data-en="⚡ Launch Studio">⚡ Studiyani Ochish</a>
    <a href="prezentatsiya.html" class="btn-sub" style="text-decoration:none;" data-ru="📺 Презентация" data-en="📺 Presentation">📺 Prezentatsiya</a>
  </div>
  <div class="noprint-right">
    <div class="langs">
      <button data-l="uz" class="is-on">UZ</button>
      <button data-l="ru">RU</button>
      <button data-l="en">EN</button>
    </div>
    <button class="btn-sub" id="themeBtn" title="Mavzuni o'zgartirish">🌓</button>
  </div>
</div>

<!-- =====================================================================
     PAGE 1: ARCHITECTURE, METHODS & VIBECODING PROMPTS
     ===================================================================== -->
<div class="sheet">
  <div>
    <!-- HEADER -->
    <div class="sheet-head">
      <div class="logo-block">
        <img src="../../../assets/target-logo.png" alt="Target School Logo">
      </div>
      <div class="head-title">
        <h1 data-ru="19.5-Урок: Vibecoding E-Commerce Backend & Postman" data-en="Lesson 19.5: Vibecoding E-Commerce Backend & Postman">19.5-dars: Vibecoding E-Commerce Backend & Postman</h1>
        <div class="sub" data-ru="Рабочий лист инженера: Реляционная модель, CRUD-роуты, валидация баланса и автотесты" data-en="Engineering Worksheet: Relational Schema, CRUD Routes, Balance Guards & Postman Tests">Muhandislik amaliyoti: Relyatsion model, CRUD marshrutlar, balans nazorati va Postman testlari</div>
      </div>
      <div class="head-badges">
        <span class="badge badge-red" data-ru="9 Класс" data-en="Grade 9">9-sinf</span>
        <span class="badge badge-orange" data-ru="Неделя 4 · Урок 19.5" data-en="Week 4 · Lesson 19.5">4-hafta · 19.5-dars</span>
        <span class="badge badge-blue" data-ru="40 Мин" data-en="40 Min">40 daqiqa</span>
      </div>
    </div>

    <!-- PUPIL INFO -->
    <div class="pupil-grid">
      <div class="pupil-field">
        <label data-ru="Ученик:" data-en="Student:">O'quvchi:</label>
        <div class="line"></div>
      </div>
      <div class="pupil-field">
        <label data-ru="Класс:" data-en="Class:">Sinf:</label>
        <div class="line"></div>
      </div>
      <div class="pupil-field">
        <label data-ru="Дата:" data-en="Date:">Sana:</label>
        <div class="line"></div>
      </div>
    </div>

    <!-- SECTION 1 -->
    <div class="block">
      <div class="sec-title" data-ru="1. Реляционная Архитектура и CRUD Матрица" data-en="1. Relational Architecture & CRUD Matrix">1. Relyatsion Arxitektura va CRUD Matritsasi</div>
      <table class="tbl">
        <thead>
          <tr>
            <th data-ru="Метод" data-en="Method">Method</th>
            <th data-ru="Маршрут" data-en="Route">Marshrut</th>
            <th data-ru="Назначение в E-Commerce" data-en="E-Commerce Purpose">E-Commerce dagi Vazifasi</th>
            <th data-ru="Статус Успеха" data-en="Success Code">Muvaffaqiyat Kodi</th>
            <th data-ru="Почему PATCH, а не PUT?" data-en="Why PATCH over PUT?">Nega PUT emas, PATCH?</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td data-ru="GET" data-en="GET"><b>GET</b></td>
            <td data-ru="/api/users" data-en="/api/users"><code>/api/users</code></td>
            <td data-ru="Список клиентов с балансами" data-en="List all customers & balances">Barcha mijozlar va ularning hisob balansi</td>
            <td data-ru="200 OK" data-en="200 OK"><code>200 OK</code></td>
            <td data-ru="Safe & Idempotent (только чтение)" data-en="Safe & Idempotent (read-only)">Xavfsiz va Idempotent (o'qish rejimi)</td>
          </tr>
          <tr>
            <td data-ru="POST" data-en="POST"><b>POST</b></td>
            <td data-ru="/api/orders" data-en="/api/orders"><code>/api/orders</code></td>
            <td data-ru="Оформление заказа с проверкой баланса" data-en="Place order with balance deduction">Buyurtma berish va mablag' yechish</td>
            <td data-ru="201 Created" data-en="201 Created"><code>201 Created</code></td>
            <td data-ru="Создаёт новую запись в таблице orders" data-en="Inserts fresh record into orders">Yangi buyurtma qatorini kiritadi</td>
          </tr>
          <tr>
            <td data-ru="PATCH" data-en="PATCH"><b>PATCH</b></td>
            <td data-ru="/api/orders/:id" data-en="/api/orders/:id"><code>/api/orders/:id</code></td>
            <td data-ru="Смена статуса (pending ➔ completed)" data-en="Update lifecycle status (pending ➔ completed)">Buyurtma holatini yangilash (pending ➔ completed)</td>
            <td data-ru="200 OK" data-en="200 OK"><code>200 OK</code></td>
            <td data-ru="Частичное обновление (не стирает сумму и товар!)" data-en="Partial update (preserves amount & product)">Qisman yangilash (narx va nomni o'chirib yubormaydi)</td>
          </tr>
          <tr>
            <td data-ru="DELETE" data-en="DELETE"><b>DELETE</b></td>
            <td data-ru="/api/orders/:id" data-en="/api/orders/:id"><code>/api/orders/:id</code></td>
            <td data-ru="Отмена заказа и возврат средств" data-en="Order cancellation and DB cleanup">Buyurtmani bekor qilish yoki o'chirish</td>
            <td data-ru="200 OK" data-en="200 OK"><code>200 OK</code></td>
            <td data-ru="Удаляет запись по первичному ключу ID" data-en="Deletes record matching primary key ID">Birlamchi kalit (ID) bo'yicha tozalaydi</td>
          </tr>
        </tbody>
      </table>

      <div style="font-size:8.4pt; margin-top:4px;">
        <b data-ru="Инженерный Вопрос:" data-en="Engineering Question:">Muhandislik Savoli:</b>
        <span data-ru="Почему проверку <code>if (user.balance < amount)</code> категорически нельзя делать в браузере (на клиенте)?" data-en="Why must <code>if (user.balance < amount)</code> strictly execute on the server, never in the browser?">Nega <code>if (user.balance < amount)</code> tekshiruvini brauzerda emas, faqat serverda qilish shart?</span>
      </div>
      <div class="write-area" style="min-height:38px; margin-top:4px;">
        <div class="write-line"></div>
        <div class="write-line"></div>
      </div>
    </div>

    <!-- SECTION 2 -->
    <div class="block">
      <div class="sec-title" data-ru="2. Вайбкодинг: Промпт для ИИ и Логика Баланса" data-en="2. Vibecoding: AI Prompt Engineering & Balance Logic">2. Vibecoding: AI Prompti va Balans Nazorati Kodingi</div>
      <div class="grid-2">
        <div class="box">
          <h4 style="margin:0 0 4px; font-size:8.6pt;" data-ru="🤖 Промпт для Cursor / ChatGPT" data-en="🤖 Prompt for Cursor / ChatGPT">🤖 Cursor / ChatGPT Uchun Professional Prompt</h4>
          <div class="mono-box" style="font-size:7.4pt; line-height:1.35;">
            "Rol: Senior Backend Dev. Express + SQLite.<br>
            Sxema: users(id, balance), orders(id, user_id, amount, status).<br>
            Vazifa: POST /api/orders yoz. req.body(user_id, product_name, amount).<br>
            Qoidalar: user_id topilmasa 404, balance &lt; amount bo'lsa 400 Bad Request, yetarli bo'lsa balance -= amount qilib 201 Created qaytar."
          </div>
        </div>

        <div class="box">
          <h4 style="margin:0 0 4px; font-size:8.6pt;" data-ru="💻 Заполните Пропуски в server.js" data-en="💻 Complete Code Gaps in server.js">💻 server.js dagi Bo'sh Joylarni To'ldiring</h4>
          <div class="mono-box" style="font-size:7.4pt; line-height:1.35;">
            const user = users.find(u =&gt; u.id === user_id);<br>
            if (!user) return res.status(<b>___</b>).json({error});<br>
            if (user.balance &lt; amount) {<br>
            &nbsp;&nbsp;return res.status(<b>___</b>).json({error: "Mablag' kam"});<br>
            }<br>
            user.balance <b>___</b> amount; // mablag' yechish<br>
            orders.push({ user_id, amount, status: 'pending' });<br>
            res.status(<b>___</b>).json({ success: true });
          </div>
        </div>
      </div>
    </div>
  </div>

  <div class="sign-box">
    <span data-ru="Target International School · Кафедра IT & Кибербезопасности" data-en="Target International School · IT & CyberSecurity Department">Target International School · IT & Kiberxavfsizlik Kafedrasi</span>
    <span data-ru="Страница 1 из 2" data-en="Page 1 of 2">1-bet / 2</span>
  </div>
</div>

<!-- =====================================================================
     PAGE 2: POSTMAN TESTING & 10-POINT RUBRIC
     ===================================================================== -->
<div class="sheet">
  <div>
    <!-- HEADER MINI -->
    <div class="sheet-head" style="margin-bottom:8px;">
      <div class="logo-block"><img src="../../../assets/target-logo.png" alt="Target Logo"></div>
      <div class="head-title">
        <h1 data-ru="Postman Тестирование и Оценка Лабораторной" data-en="Postman Testing & Lab Assessment">Postman Sinovlari va Laboratoriya Baholashi</h1>
        <div class="sub" data-ru="Часть 2: Автотесты pm.test, Регрессионное тестирование и 10-балльный результат" data-en="Part 2: Automated pm.test Suites, Regression Testing & 10-Point Scorecard">2-qism: pm.test avtotestlari, regressiya nazorati va 10 ballik natija</div>
      </div>
      <div class="head-badges">
        <span class="badge badge-orange">Postman v2.1</span>
      </div>
    </div>

    <!-- SECTION 3 -->
    <div class="block">
      <div class="sec-title" data-ru="3. Postman: Анатомия Запроса и Автотесты (pm.test)" data-en="3. Postman: Request Anatomy & Automated Tests (pm.test)">3. Postman: So'rov Tuzilmasi va Avtotestlar (pm.test)</div>
      
      <div class="grid-3">
        <div class="box">
          <b style="font-size:8.4pt;" data-ru="1. Headers" data-en="1. Headers">1. Headers (Sarlavha)</b>
          <p style="font-size:7.8pt; margin:4px 0 0;" data-ru="Обязательно указать <code>Content-Type: application/json</code>, чтобы Express распарсил тело в <code>req.body</code>." data-en="Must include <code>Content-Type: application/json</code> for Express to populate <code>req.body</code>.">Express <code>req.body</code> ni o'qiy olishi uchun <code>Content-Type: application/json</code> shart.</p>
        </div>
        <div class="box">
          <b style="font-size:8.4pt;" data-ru="2. Raw JSON Body" data-en="2. Raw JSON Body">2. Raw JSON Body</b>
          <p style="font-size:7.8pt; margin:4px 0 0;" data-ru="Тело POST/PATCH: ключи в двойных кавычках <code>{ &quot;amount&quot;: 180000 }</code>. Числа без кавычек!" data-en="POST/PATCH payload: keys in double quotes <code>{ &quot;amount&quot;: 180000 }</code>. Numbers unquoted!">Kalitlar qo'shtirnoqda bo'lishi shart. Raqamlar qo'shtirnoqsiz yoziladi!</p>
        </div>
        <div class="box">
          <b style="font-size:8.4pt;" data-ru="3. Tests Вкладка" data-en="3. Tests Tab">3. Tests Oynasi</b>
          <p style="font-size:7.8pt; margin:4px 0 0;" data-ru="Код JavaScript, выполняемый сразу после ответа сервера для верификации контракта API." data-en="JavaScript code executed instantly after response arrives to verify API contract.">Server javob bergach shartlarni tekshiruvchi avtomatik JavaScript kodi.</p>
        </div>
      </div>

      <div style="margin-top:8px;">
        <h4 style="margin:0 0 4px; font-size:8.6pt;" data-ru="✍️ Напишите Postman Тест-Скрипт" data-en="✍️ Write Postman Test Script">✍️ Postman Test Skriptini Yozing (Status 201 va pending holati uchun)</h4>
        <div class="write-area" style="min-height:50px;">
          <div style="font-family:'JetBrains Mono',monospace; font-size:7.6pt; color:var(--ink-2);">pm.test("Status code is 201", function () { ... });</div>
          <div class="write-line"></div>
          <div class="write-line"></div>
        </div>
      </div>
    </div>

    <!-- SECTION 4 -->
    <div class="block">
      <div class="sec-title" data-ru="4. Практика в Студии и 10-Балльный Результат" data-en="4. Studio Practical Quests & 10-Point Scorecard">4. Studiya Amaliyoti va 10 Ballik Rasmiy Mezon</div>

      <div class="grid-2">
        <div class="box">
          <h4 style="margin:0 0 6px; font-size:8.8pt;" data-ru="📋 Выполнение 4-х Квестов" data-en="📋 4 Practical Quests Check">📋 4 Ta Kvest Bajarilishi</h4>
          <ul class="rubric-list">
            <li>
              <span data-ru="[ ] Квест 1: Регистрация клиента (POST /api/users)" data-en="[ ] Quest 1: User Registration (POST /api/users)">[ ] 1-Kvest: Mijoz ro'yxati (POST /api/users)</span>
              <b>2.5 ball</b>
            </li>
            <li>
              <span data-ru="[ ] Квест 2: Заказ и списание баланса (POST /api/orders)" data-en="[ ] Quest 2: Order & Balance debit (POST /api/orders)">[ ] 2-Kvest: Buyurtma va balans (POST /api/orders)</span>
              <b>2.5 ball</b>
            </li>
            <li>
              <span data-ru="[ ] Квест 3: Обновление статуса (PATCH /api/orders/:id)" data-en="[ ] Quest 3: Status update (PATCH /api/orders/:id)">[ ] 3-Kvest: PATCH holati (completed)</span>
              <b>2.5 ball</b>
            </li>
            <li>
              <span data-ru="[ ] Квест 4: 100% зелёные тесты Postman Runner" data-en="[ ] Quest 4: 100% green Postman Test Runner">[ ] 4-Kvest: 100% yashil Postman testlari</span>
              <b>2.5 ball</b>
            </li>
          </ul>
        </div>

        <div class="box" style="display:flex; flex-direction:column; justify-content:space-between;">
          <h4 style="margin:0 0 6px; font-size:8.8pt;" data-ru="✍️ Итоговая Оценка Преподавателя" data-en="✍️ Teacher Evaluation">✍️ O'qituvchi Bahosi</h4>
          <div style="font-size:8.4pt; color:var(--ink-2); display:grid; gap:6px;">
            <div>
              <b data-ru="Набрано баллов:" data-en="Score:">To'plangan ball:</b> 
              <span style="font-size:13pt; font-weight:800; color:var(--accent-ink); font-family:'JetBrains Mono',monospace;">___ / 10 ball</span>
            </div>
            <div>
              <b data-ru="Подпись учителя:" data-en="Teacher Signature:">O'qituvchi imzosi:</b> ___________________
            </div>
            <div style="font-size:7.4pt; color:var(--ink-3);" data-ru="Target International School · Yunusobod" data-en="Target International School · Yunusobod">
              Target International School · Yunusobod
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>

  <div class="sign-box">
    <span data-ru="Следующий шаг: 20-урок — Full-Stack Deploy и Защита Проекта" data-en="Next step: Lesson 20 — Full-Stack Cloud Deploy & Demo Day">Keyingi qadam: 20-dars — Full-Stack Bulutli Deploy va Demo Day</span>
    <span data-ru="Страница 2 из 2" data-en="Page 2 of 2">2-bet / 2</span>
  </div>
</div>

<script>
var lang = 'uz';
var TITLES = {
  "uz": "19.5-dars: Vibecoding E-Commerce Backend & Postman — Ishchi Varaqa",
  "ru": "Урок 19.5: Vibecoding E-Commerce Backend & Postman — Рабочий Лист",
  "en": "Lesson 19.5: Vibecoding E-Commerce Backend & Postman — Worksheet"
};

function setLanguage(l){
  lang = l;
  document.querySelectorAll('.langs button').forEach(function(b){
    b.classList.toggle('is-on', b.getAttribute('data-l') === l);
  });
  document.querySelectorAll('[data-ru], [data-en]').forEach(function(el){
    if (!el.dataset.uz) el.dataset.uz = el.innerHTML;
    var val = (l === 'uz') ? el.dataset.uz : el.getAttribute('data-' + l);
    el.innerHTML = (val !== null && val !== undefined && val !== '') ? val : el.dataset.uz;
  });
  document.title = TITLES[l] || TITLES.uz;
  try { localStorage.setItem('vc-lang', l); } catch(e){}
}

document.querySelectorAll('.langs button').forEach(function(b){
  b.onclick = function(){ setLanguage(this.getAttribute('data-l')); };
});

function toggleTheme(){
  var html = document.documentElement;
  var curT = html.getAttribute('data-theme');
  var nextT = curT === 'dark' ? 'light' : 'dark';
  html.setAttribute('data-theme', nextT);
  try { localStorage.setItem('vc-theme', nextT); } catch(e){}
}
document.getElementById('themeBtn').onclick = toggleTheme;
document.getElementById('printBtn').onclick = function(){ window.print(); };

// Restore preferences
try {
  var st = localStorage.getItem('vc-theme');
  if (st) document.documentElement.setAttribute('data-theme', st);
  var sl = localStorage.getItem('vc-lang');
  if (sl && ['uz','ru','en'].includes(sl)) setLanguage(sl);
} catch(e){}
</script>
</body>
</html>
'''

target_path = "/home/dpdp/target/classes/9-sinf/4-hafta/19.5-dars-ecommerce-backend-va-postman/varaqa.html"
with open(target_path, "w", encoding="utf-8") as f:
    f.write(varaqa_content)

print(f"Varaqa created successfully at: {target_path} ({len(varaqa_content)} bytes)")
