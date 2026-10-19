#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Target International School — Standalone Interactive Homework Generator
Generates full-fledged vazifa.html apps with:
- Top nav bar & floating controls
- Student info persistence (LocalStorage)
- 4 practical engineering tasks with textareas
- Solution reveal ("Yechimni ko'rish (Fix)")
- 10-point rubric
- 100% trilingual in-place localization (UZ/RU/EN)
"""

import os
import json
import html

HOMEWORKS = [
  {
    "folder": "classes/9-sinf/6-hafta/26-dars-mvc-backend-va-relyatsion-baza",
    "cohort_tag": "9-SINF · UY VAZIFASI",
    "eyebrow": {
      "uz": "9-SINF · 6-HAFTA · 26-DARS",
      "ru": "9-КЛАСС · 6-Я НЕДЕЛЯ · УРОК 26",
      "en": "GRADE 9 · WEEK 6 · LESSON 26"
    },
    "title": {
      "uz": "MVC Backend Asoslari va Relyatsion SQLite — Mustaqil Amaliy Vazifa",
      "ru": "Архитектура MVC и Реляционная SQLite — Практическое Задание",
      "en": "MVC Backend Architecture & Relational SQLite — Homework Assignment"
    },
    "subtitle": {
      "uz": "MVC qatlamlarini ajratish, SQLite Foreign Key bog'lanishlari, REST API validatsiyasi va SQL JOIN bo'yicha mustaqil muhandislik topshiriqlari.",
      "ru": "Разделение слоев MVC, связи Foreign Key в SQLite, валидация REST API и составление отчетов SQL JOIN.",
      "en": "MVC layer separation, SQLite Foreign Key constraints, REST API payload validation, and SQL JOIN reporting."
    },
    "meta_course": "Full-Stack & Backend Engineering",
    "tasks": [
      {
        "num": 1,
        "points": "2.5 Ball",
        "title": {
          "uz": "1-Topshiriq: Spaghetti Monolit Kodni MVC Qatlamlariga Ajratish",
          "ru": "Задание 1: Разделение спагетти-кода на слои MVC",
          "en": "Task 1: Decomposing Spaghetti Monolith into MVC Layers"
        },
        "desc": {
          "uz": "Dasturchi barcha kodni (HTML, SQL so'rovlar, ma'lumotlarni tekshirish va javob yuborishni) bitta katta server.js fayliga aralashtirib yozgan. Ushbu logikani MVC ning 3 ta qatlamiga qanday ajratish kerakligini tushuntiring va har bir faylning (`models/orderModel.js`, `controllers/orderController.js`, `routes/orderRoutes.js`) asosiy vazifasini yozing.",
          "ru": "Разработчик смешал весь код (HTML, SQL-запросы, валидацию и отправку ответа) в одном файле server.js. Объясните, как декомпозировать логику на 3 слоя MVC и опишите назначение каждого файла (routes, controllers, models).",
          "en": "A developer dumped all logic (HTML rendering, raw SQL queries, data validation, response dispatch) into a monolithic server.js. Explain how to split this into 3 clean MVC layers and define the responsibility of each file."
        },
        "ph": {
          "uz": "Fayllar tuzilmasi va har bir qatlamning mas'uliyatini bu yerga yozing...",
          "ru": "Опишите структуру файлов и ответственность каждого слоя здесь...",
          "en": "Detail the file structure and each layer's specific responsibilities here..."
        },
        "fix": {
          "uz": "<b>MUHANDISLIK YECHIMI (MVC Arxitekturasi):</b><br>1. <code>routes/orderRoutes.js</code> — faqat HTTP yo'llarini (URL endpoints: POST /, GET /details) controller metodlariga bog'laydi.<br>2. <code>controllers/orderController.js</code> — kiruvchi parametrlar (user_id, quantity) to'g'riligini tekshiradi, xato bo'lsa 400 qaytaradi, to'g'ri bo'lsa Model metodini chaqirib 201 Created yuboradi.<br>3. <code>models/orderModel.js</code> — faqat SQLite ma'lumotlar bazasi bilan ishlaydi (SQL INSERT, SELECT) va natijani qaytaradi.",
          "ru": "<b>ИНЖЕНЕРНОЕ РЕШЕНИЕ (Архитектура MVC):</b><br>1. <code>routes/orderRoutes.js</code> — маршрутизирует URL на методы контроллера.<br>2. <code>controllers/orderController.js</code> — валидирует req.body, возвращает 400 или вызывает Model и отдает 201.<br>3. <code>models/orderModel.js</code> — чистый SQL (INSERT, SELECT) без работы с HTTP.",
          "en": "<b>ENGINEERING SOLUTION (MVC Separation):</b><br>1. <code>routes/orderRoutes.js</code> — maps endpoints to controller functions.<br>2. <code>controllers/orderController.js</code> — validates payload, returns 400 Bad Request on failure or dispatches 201 Created via model.<br>3. <code>models/orderModel.js</code> — strictly database transactions (SQL INSERT, SELECT)."
        }
      },
      {
        "num": 2,
        "points": "2.5 Ball",
        "title": {
          "uz": "2-Topshiriq: Relyatsion SQLite Sxemasi va Foreign Key Himoyasi",
          "ru": "Задание 2: Реляционная схема SQLite и защита Foreign Key",
          "en": "Task 2: Relational SQLite Schema & Foreign Key Constraints"
        },
        "desc": {
          "uz": "Buyurtmalar jadvali (orders) uchun to'liq SQL CREATE TABLE buyrug'ini yozing. Jadvalda id (Primary Key), user_id (users jadvaliga Foreign Key), product_id (products jadvaliga Foreign Key), quantity (faqat musbat son bo'lishi sharti - CHECK) va total_price ustunlari bo'lsin.",
          "ru": "Напишите SQL-запрос CREATE TABLE для таблицы orders. Поля: id (Primary Key), user_id (Foreign Key к users), product_id (Foreign Key к products), quantity (CHECK quantity > 0) и total_price.",
          "en": "Write the complete SQL CREATE TABLE statement for the orders table. Include: id (Primary Key), user_id (Foreign Key to users), product_id (Foreign Key to products), quantity (CHECK quantity > 0), and total_price."
        },
        "ph": {
          "uz": "CREATE TABLE orders (\n  ...\n);",
          "ru": "CREATE TABLE orders (\n  ...\n);",
          "en": "CREATE TABLE orders (\n  ...\n);"
        },
        "fix": {
          "uz": "<b>SQL SXEMASI:</b><br><pre><code>CREATE TABLE orders (\n  id INTEGER PRIMARY KEY AUTOINCREMENT,\n  user_id INTEGER NOT NULL,\n  product_id INTEGER NOT NULL,\n  quantity INTEGER NOT NULL CHECK(quantity > 0),\n  total_price INTEGER NOT NULL,\n  created_at DATETIME DEFAULT CURRENT_TIMESTAMP,\n  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,\n  FOREIGN KEY (product_id) REFERENCES products(id)\n);</code></pre>",
          "ru": "<b>SQL СХЕМА:</b><br><pre><code>CREATE TABLE orders (\n  id INTEGER PRIMARY KEY AUTOINCREMENT,\n  user_id INTEGER NOT NULL,\n  product_id INTEGER NOT NULL,\n  quantity INTEGER NOT NULL CHECK(quantity > 0),\n  total_price INTEGER NOT NULL,\n  FOREIGN KEY (user_id) REFERENCES users(id),\n  FOREIGN KEY (product_id) REFERENCES products(id)\n);</code></pre>",
          "en": "<b>SQL SCHEMA:</b><br><pre><code>CREATE TABLE orders (\n  id INTEGER PRIMARY KEY AUTOINCREMENT,\n  user_id INTEGER NOT NULL,\n  product_id INTEGER NOT NULL,\n  quantity INTEGER NOT NULL CHECK(quantity > 0),\n  total_price INTEGER NOT NULL,\n  FOREIGN KEY (user_id) REFERENCES users(id),\n  FOREIGN KEY (product_id) REFERENCES products(id)\n);</code></pre>"
        }
      },
      {
        "num": 3,
        "points": "2.5 Ball",
        "title": {
          "uz": "3-Topshiriq: REST API Controller Validatsiyasi va Status Kodlari",
          "ru": "Задание 3: Валидация контроллера REST API и статус-коды",
          "en": "Task 3: REST API Controller Validation & HTTP Status Codes"
        },
        "desc": {
          "uz": "Express controllerida yangi buyurtma qabul qiluvchi `createOrder(req, res)` funksiyasi kodini yozing. Agar `user_id` yoki `quantity` kiritilmagan yoki `quantity <= 0` bo'lsa, `400 Bad Request` qaytarsin. Agar ma'lumotlar to'g'ri bo'lsa, bazaga saqlab `201 Created` va buyurtma ob'ektini JSON qilib qaytarsin.",
          "ru": "Напишите функцию контроллера `createOrder(req, res)` на Express. Если user_id или quantity отсутствуют, либо quantity <= 0, возвращайте статус 400 Bad Request. При успехе — сохраняйте в БД и возвращайте 201 Created с JSON.",
          "en": "Write the Express controller function `createOrder(req, res)`. If user_id or quantity is missing, or quantity <= 0, return 400 Bad Request. On valid input, persist to database and respond with 201 Created."
        },
        "ph": {
          "uz": "exports.createOrder = (req, res) => {\n  ...\n};",
          "ru": "exports.createOrder = (req, res) => {\n  ...\n};",
          "en": "exports.createOrder = (req, res) => {\n  ...\n};"
        },
        "fix": {
          "uz": "<b>EXPRESS CONTROLLER KODI:</b><br><pre><code>exports.createOrder = (req, res) => {\n  const { user_id, product_id, quantity } = req.body;\n  if (!user_id || !product_id || !quantity || quantity <= 0) {\n    return res.status(400).json({ error: 'Foydalanuvchi, tovar yoki miqdor noto\\'g\\'ri!' });\n  }\n  OrderModel.create({ user_id, product_id, quantity }, (err, order) => {\n    if (err) return res.status(500).json({ error: 'Baza xatosi' });\n    res.status(201).json({ message: 'Buyurtma yaratildi', order });\n  });\n};</code></pre>",
          "ru": "<b>КОД КОНТРОЛЛЕРА:</b><br><pre><code>exports.createOrder = (req, res) => {\n  const { user_id, product_id, quantity } = req.body;\n  if (!user_id || !product_id || !quantity || quantity <= 0) {\n    return res.status(400).json({ error: 'Некорректные параметры заказа' });\n  }\n  OrderModel.create({ user_id, product_id, quantity }, (err, order) => {\n    if (err) return res.status(500).json({ error: 'Ошибка БД' });\n    res.status(201).json({ success: true, order });\n  });\n};</code></pre>",
          "en": "<b>CONTROLLER IMPLEMENTATION:</b><br><pre><code>exports.createOrder = (req, res) => {\n  const { user_id, product_id, quantity } = req.body;\n  if (!user_id || !product_id || !quantity || quantity <= 0) {\n    return res.status(400).json({ error: 'Invalid payload attributes' });\n  }\n  OrderModel.create({ user_id, product_id, quantity }, (err, order) => {\n    if (err) return res.status(500).json({ error: 'DB Error' });\n    res.status(201).json({ success: true, order });\n  });\n};</code></pre>"
        }
      },
      {
        "num": 4,
        "points": "2.5 Ball",
        "title": {
          "uz": "4-Topshiriq: Relyatsion Baza Bo'yicha SQL INNER JOIN Hisoboti",
          "ru": "Задание 4: Отчет SQL INNER JOIN по связанным таблицам",
          "en": "Task 4: Relational Multi-Table SQL INNER JOIN Query"
        },
        "desc": {
          "uz": "Menejer uchun hisobot tayyorlash kerak: har bir buyurtmaning id raqami, xaridorning ismi (`users.name`), tovarning sarlavhasi (`products.title`), buyurtma miqdori (`orders.quantity`) va jami summasi (`orders.total_price`). Ushbu 3 ta jadvalni bog'lovchi to'liq SQL INNER JOIN so'rovini yozing.",
          "ru": "Составьте SQL-запрос для бизнес-отчета: вывести id заказа, имя клиента (users.name), название товара (products.title), количество (orders.quantity) и общую сумму (orders.total_price), объединив 3 таблицы через INNER JOIN.",
          "en": "Construct a SQL query for a sales report: display order id, customer name (users.name), product title (products.title), ordered quantity (orders.quantity), and total price (orders.total_price), joining all 3 tables with INNER JOIN."
        },
        "ph": {
          "uz": "SELECT ... FROM orders ...",
          "ru": "SELECT ... FROM orders ...",
          "en": "SELECT ... FROM orders ..."
        },
        "fix": {
          "uz": "<b>SQL INNER JOIN SO'ROVI:</b><br><pre><code>SELECT \n  orders.id AS order_id,\n  users.name AS customer_name,\n  products.title AS product_name,\n  orders.quantity,\n  orders.total_price\nFROM orders\nINNER JOIN users ON orders.user_id = users.id\nINNER JOIN products ON orders.product_id = products.id\nORDER BY orders.id DESC;</code></pre>",
          "ru": "<b>SQL ЗАПРОС INNER JOIN:</b><br><pre><code>SELECT \n  orders.id AS order_id,\n  users.name AS customer_name,\n  products.title AS product_name,\n  orders.quantity,\n  orders.total_price\nFROM orders\nINNER JOIN users ON orders.user_id = users.id\nINNER JOIN products ON orders.product_id = products.id\nORDER BY orders.id DESC;</code></pre>",
          "en": "<b>SQL INNER JOIN STATEMENT:</b><br><pre><code>SELECT \n  orders.id AS order_id,\n  users.name AS customer_name,\n  products.title AS product_name,\n  orders.quantity,\n  orders.total_price\nFROM orders\nINNER JOIN users ON orders.user_id = users.id\nINNER JOIN products ON orders.product_id = products.id\nORDER BY orders.id DESC;</code></pre>"
        }
      }
    ]
  },
  {
    "folder": "classes/10-11-sinf/7-hafta/31-dars-penetration-testing-va-ethical-hacking",
    "cohort_tag": "10-11-SINF · UY VAZIFASI",
    "eyebrow": {
      "uz": "10–11-SINF · 7-HAFTA · 31-DARS",
      "ru": "10–11-КЛАСС · 7-Я НЕДЕЛЯ · УРОК 31",
      "en": "GRADES 10–11 · WEEK 7 · LESSON 31"
    },
    "title": {
      "uz": "Penetration Testing & Ethical Hacking — Mustaqil Amaliy Vazifa",
      "ru": "Тестирование на Проникновение и Этичный Хакинг — Задание",
      "en": "Penetration Testing & Ethical Hacking — Homework Assignment"
    },
    "subtitle": {
      "uz": "PTES metodologiyasi, BOLA/IDOR zaifliklarini bartaraf etish, HTTP Security Headers va shaxsiy zaiflik skanerini dasturlash topshiriqlari.",
      "ru": "Методология PTES, устранение BOLA/IDOR, заголовки безопасности HTTP и разработка собственного сканера безопасности.",
      "en": "PTES lifecycle execution, BOLA/IDOR remediation, HTTP security headers configuration, and automated CLI scanner logic."
    },
    "meta_course": "Advanced CyberSecurity & Pentesting",
    "tasks": [
      {
        "num": 1,
        "points": "2.5 Ball",
        "title": {
          "uz": "1-Topshiriq: PTES Metodologiyasi va Axloqiy Xakerlik Kodeksi",
          "ru": "Задание 1: Методология PTES и этический кодекс White Hat",
          "en": "Task 1: PTES Methodology & White Hat Code of Ethics"
        },
        "desc": {
          "uz": "Penetration Testing Execution Standard (PTES) ning 5 ta asosiy bosqichini ketma-ket yozing. Nega mijozning yozma ruxsatisiz (Scope of Work / RoE) tarmoq skaneri ishlatish qonunbuzarlik hisoblanishini O'zbekiston Jinoyat Kodeksining 278-moddasi doirasida asoslab bering.",
          "ru": "Перечислите 5 основных этапов PTES. Обоснуйте, почему запуск сканера без письменного согласия (Scope of Work) квалифицируется как киберпреступление (ст. 278 УК РУз).",
          "en": "List the 5 primary phases of the Penetration Testing Execution Standard (PTES). Explain why scanning target infrastructure absent explicit written Rules of Engagement violates legal cyber statutes."
        },
        "ph": {
          "uz": "PTES bosqichlari va huquqiy tahlilni bu yerga yozing...",
          "ru": "Опишите этапы PTES и правовой анализ здесь...",
          "en": "Detail PTES stages and the statutory legal analysis here..."
        },
        "fix": {
          "uz": "<b>MUHANDISLIK JAVOBI:</b><br>1. <b>PTES 5 bosqichi:</b> 1) Pre-engagement Interactions (Ruxsatnoma va shartnoma) ➔ 2) Intelligence Gathering (OSINT qidiruv) ➔ 3) Threat Modeling & Vulnerability Analysis (Zaifliklarni tahlil qilish) ➔ 4) Exploitation (Hujumni sinash) ➔ 5) Reporting (Tuzatish tavsiyalari hisoboti).<br>2. <b>Huquqiy asos:</b> O'zR JK 278-moddasi ('Kompyuter axborotidan qonunga xilof ravishda foydalanish') bo'yicha ruxsatsiz axborot tizimiga kirish jinoiy javobgarlikka olib keladi. White Hat faqat yozma shartnoma asosida ishlaydi.",
          "ru": "<b>ИНЖЕНЕРНЫЙ ОТВЕТ:</b><br>1. <b>5 этапов PTES:</b> Pre-engagement, Intelligence Gathering, Threat Modeling / Vulnerability Analysis, Exploitation, Reporting.<br>2. <b>Правовой аспект:</b> Сканирование без RoE нарушает ст. 278 УК РУз. White Hat тестирует строго согласованный периметр.",
          "en": "<b>ENGINEERING SOLUTION:</b><br>1. <b>PTES Phases:</b> Pre-engagement, Intelligence Gathering, Threat Modeling/Vuln Analysis, Exploitation, Reporting.<br>2. <b>Statutory compliance:</b> Unsolicited reconnaissance violates unauthorized access statutes. White Hat strictly adheres to written scope."
        }
      },
      {
        "num": 2,
        "points": "2.5 Ball",
        "title": {
          "uz": "2-Topshiriq: OWASP API #1 BOLA / IDOR Zaifligini Kodda Tuzatish",
          "ru": "Задание 2: Устранение уязвимости OWASP API #1 BOLA / IDOR в коде",
          "en": "Task 2: Mitigating OWASP API #1 BOLA / IDOR in Express Code"
        },
        "desc": {
          "uz": "Quyidagi Express endpointida BOLA zaifligi mavjud (har qanday user boshqaning maxfiy hujjatini `docId` ni o'zgartirib o'qiy oladi). Kodni shunday o'zgartiringki, u faqat so'rov yuborgan `req.user.id` ga tegishli hujjatlarni qaytarsin, aks holda `403 Forbidden` tashlasin:<br><code>app.get('/api/docs/:id', (req, res) => { const doc = db.get(req.params.id); res.json(doc); });</code>",
          "ru": "В эндпоинте присутствует BOLA (любой пользователь может прочесть чужой документ через параметр id). Исправьте код, добавив проверку doc.owner_id === req.user.id и статус 403 Forbidden при нарушении прав.",
          "en": "The endpoint below suffers from BOLA (any authenticated user can read arbitrary documents by swapping :id). Patch the controller so that it asserts doc.owner_id === req.user.id and halts with 403 Forbidden otherwise."
        },
        "ph": {
          "uz": "app.get('/api/docs/:id', authenticateToken, (req, res) => {\n  ...\n});",
          "ru": "app.get('/api/docs/:id', authenticateToken, (req, res) => {\n  ...\n});",
          "en": "app.get('/api/docs/:id', authenticateToken, (req, res) => {\n  ...\n});"
        },
        "fix": {
          "uz": "<b>TUZATILGAN XAVFSIZ KOD (IDOR FIX):</b><br><pre><code>app.get('/api/docs/:id', authenticateToken, (req, res) => {\n  const doc = db.get(req.params.id);\n  if (!doc) {\n    return res.status(404).json({ error: 'Hujjat topilmadi' });\n  }\n  // BOLA/IDOR QALQONI:\n  if (doc.owner_id !== req.user.id) {\n    return res.status(403).json({ error: 'Ruxsat berilmagan! (403 Forbidden)' });\n  }\n  res.json({ success: true, doc });\n});</code></pre>",
          "ru": "<b>ИСПРАВЛЕННЫЙ КОД (ЗАЩИТА BOLA):</b><br><pre><code>app.get('/api/docs/:id', authenticateToken, (req, res) => {\n  const doc = db.get(req.params.id);\n  if (!doc) return res.status(404).json({ error: 'Не найдено' });\n  if (doc.owner_id !== req.user.id) {\n    return res.status(403).json({ error: 'Доступ запрещен (403 Forbidden)' });\n  }\n  res.json(doc);\n});</code></pre>",
          "en": "<b>HARDENED IMPLEMENTATION (BOLA MITIGATION):</b><br><pre><code>app.get('/api/docs/:id', authenticateToken, (req, res) => {\n  const doc = db.get(req.params.id);\n  if (!doc) return res.status(404).json({ error: 'Not found' });\n  if (doc.owner_id !== req.user.id) {\n    return res.status(403).json({ error: 'Access Denied (403 Forbidden)' });\n  }\n  res.json(doc);\n});</code></pre>"
        }
      },
      {
        "num": 3,
        "points": "2.5 Ball",
        "title": {
          "uz": "3-Topshiriq: HTTP Security Headers va Helmet Integratsiyasi",
          "ru": "Задание 3: Заголовки безопасности HTTP и интеграция Helmet",
          "en": "Task 3: HTTP Security Headers & Helmet Middleware Hardening"
        },
        "desc": {
          "uz": "Brauzer darajasidagi hujumlarning oldini olish uchun server qaysi 3 ta muhim HTTP sarlavhasini qaytarishi kerak? Har birining vazifasini yozing (`Content-Security-Policy`, `X-Frame-Options`, `Strict-Transport-Security`) va Node.js Express loyihasiga `helmet` paketini qanday ulashni ko'rsating.",
          "ru": "Опишите назначение 3 ключевых заголовков безопасности (CSP, X-Frame-Options, HSTS). Покажите, как подключить библиотеку helmet в приложении Express одной строкой.",
          "en": "Detail the defensive purpose of 3 core security headers (CSP, X-Frame-Options, HSTS). Demonstrate how to integrate helmet middleware in Express with production hardening."
        },
        "ph": {
          "uz": "Security headers tahlili va helmet integratsiyasi...",
          "ru": "Анализ заголовков и подключение helmet...",
          "en": "Security headers analysis and helmet integration..."
        },
        "fix": {
          "uz": "<b>SECURITY HEADERS TAHLILI VA INTEGRATSIYA:</b><br>1. <code>X-Frame-Options: DENY</code> — saytni iframe ichiga tiqish (Clickjacking) hujumini to'xtatadi.<br>2. <code>Content-Security-Policy (CSP)</code> — faqat ruxsat berilgan manbalardan skript yuklashga ruxsat berib, XSS ni to'xtatadi.<br>3. <code>Strict-Transport-Security (HSTS)</code> — brauzerni faqat shifrlangan HTTPS orqali ulanishga majburlaydi (SSL Strip himoyasi).<br><b>Helmet kodi:</b><br><pre><code>const helmet = require('helmet');\napp.use(helmet());</code></pre>",
          "ru": "<b>АНАЛИЗ И ПОДКЛЮЧЕНИЕ HELMET:</b><br>1. <code>X-Frame-Options: DENY</code> — защита от кликджекинга.<br>2. <code>Content-Security-Policy</code> — блокировка XSS через белый список источников.<br>3. <code>Strict-Transport-Security (HSTS)</code> — принудительный HTTPS.<br><code>const helmet = require('helmet'); app.use(helmet());</code>",
          "en": "<b>SECURITY HEADERS SPECIFICATION:</b><br>1. <code>X-Frame-Options: DENY</code> — blocks Clickjacking framing.<br>2. <code>Content-Security-Policy</code> — mitigates XSS via source whitelisting.<br>3. <code>Strict-Transport-Security</code> — enforces SSL/TLS connectivity.<br><code>const helmet = require('helmet'); app.use(helmet());</code>"
        }
      },
      {
        "num": 4,
        "points": "2.5 Ball",
        "title": {
          "uz": "4-Topshiriq: Shaxsiy CLI Skaneriga RegEx Qoidalarini Qo'shish",
          "ru": "Задание 4: Добавление правил RegEx в собственный CLI сканер",
          "en": "Task 4: Expanding CLI Vulnerability Scanner with Custom RegEx Rules"
        },
        "desc": {
          "uz": "Darsdagi shaxsiy Node.js skanerimiz (`scanner/scanner.js`) JavaScript va HTML fayllarni sizib chiqqan kalitlarga tekshiradi. Ushbu skanerga GitHub Personal Access Token (`ghp_[a-zA-Z0-9]{36}`) va AWS Access Key ID (`AKIA[0-9A-Z]{16}`) larni qidiruvchi RegEx qoidalarini qanday qo'shish kerakligini kod shaklida yozing.",
          "ru": "Наш CLI сканер scanner.js проверяет бандлы на утечки секретов. Напишите фрагмент кода на JS с регулярными выражениями (RegEx) для детекции токенов GitHub (ghp_...) и ключей AWS (AKIA...).",
          "en": "Our CLI scanner scanner.js audits frontend bundles for leaked secrets. Provide the JavaScript rule objects with regular expressions to detect GitHub tokens (ghp_...) and AWS access keys (AKIA...)."
        },
        "ph": {
          "uz": "const SECRET_PATTERNS = [\n  ...\n];",
          "ru": "const SECRET_PATTERNS = [\n  ...\n];",
          "en": "const SECRET_PATTERNS = [\n  ...\n];"
        },
        "fix": {
          "uz": "<b>SCANNER REGEX QOIDALARI:</b><br><pre><code>const SECRET_PATTERNS = [\n  {\n    name: 'GitHub Personal Access Token',\n    regex: /ghp_[a-zA-Z0-9]{36}/g,\n    severity: 'CRITICAL',\n    cvss: 9.8\n  },\n  {\n    name: 'AWS Access Key ID',\n    regex: /(?:A3T[A-Z0-9]|AKIA|AGPA|AIDA|AROA|AIPA|ANPA|ANVA|ASIA)[A-Z0-9]{16}/g,\n    severity: 'CRITICAL',\n    cvss: 9.5\n  }\n];</code></pre>",
          "ru": "<b>ПРАВИЛА REGEX ДЛЯ СКАНЕРА:</b><br><pre><code>const SECRET_PATTERNS = [\n  { name: 'GitHub Token', regex: /ghp_[a-zA-Z0-9]{36}/g, severity: 'CRITICAL', cvss: 9.8 },\n  { name: 'AWS Access Key', regex: /AKIA[0-9A-Z]{16}/g, severity: 'CRITICAL', cvss: 9.5 }\n];</code></pre>",
          "en": "<b>REGEX DETECTION SIGNATURES:</b><br><pre><code>const SECRET_PATTERNS = [\n  { name: 'GitHub Token', regex: /ghp_[a-zA-Z0-9]{36}/g, severity: 'CRITICAL', cvss: 9.8 },\n  { name: 'AWS Access Key', regex: /AKIA[0-9A-Z]{16}/g, severity: 'CRITICAL', cvss: 9.5 }\n];</code></pre>"
        }
      }
    ]
  },
  {
    "folder": "classes/7-8-sinf/7-hafta/29-dars-gps-navigatsiya-va-eng-qisqa-yol",
    "cohort_tag": "7-8-SINF · UY VAZIFASI",
    "eyebrow": {
      "uz": "7–8-SINF · 7-HAFTA · 29-DARS",
      "ru": "7–8-Класс · 7-Я НЕДЕЛЯ · УРОК 29",
      "en": "GRADES 7–8 · WEEK 7 · LESSON 29"
    },
    "title": {
      "uz": "GPS Navigatsiya va Eng Qisqa Yo'l Algoritmi — Mustaqil Amaliy Vazifa",
      "ru": "GPS Навигация и Алгоритм Кратчайшего Пути — Задание",
      "en": "GPS Navigation & Shortest Path Algorithm — Homework Assignment"
    },
    "subtitle": {
      "uz": "Graf nazariyasi, Dijkstra eng qisqa yo'l algoritmi, Haversine formulasi va W3C Geolocation API bo'yicha mustaqil topshiriqlar.",
      "ru": "Теория графов, алгоритм Дейкстры, формула расстояния Гаверсинуса и Geolocation API в браузере.",
      "en": "Graph modeling, Dijkstra shortest path execution, Haversine distance calculations, and HTML5 Geolocation API integration."
    },
    "meta_course": "Game Dev & Algorithmic Thinking",
    "tasks": [
      {
        "num": 1,
        "points": "2.5 Ball",
        "title": {
          "uz": "1-Topshiriq: Shahar Xaritasini Graf Tuzilmasida Modellashtirish",
          "ru": "Задание 1: Моделирование карты дорог в виде графа",
          "en": "Task 1: Modeling Street Infrastructure as a Weighted Graph"
        },
        "desc": {
          "uz": "Toshkent shahridagi 4 ta nuqta: Maktab (A), Metro (B), Park (C) va Stadion (D) o'rtasidagi yo'llarni JavaScript ob'ekti (Adjacency List) shaklida ifodalang. Masofalarni (metrda) vazn sifatida belgilang (masalan: A dan B ga 500m, B dan C ga 300m va h.k.).",
          "ru": "Представьте карту из 4 точек (Школа A, Метро B, Парк C, Стадион D) в виде списка смежности (Adjacency List) на JavaScript со взвешенными ребрами (в метрах).",
          "en": "Model a 4-node local map (School A, Metro B, Park C, Stadium D) as a JavaScript Adjacency List with weighted road distances (in meters)."
        },
        "ph": {
          "uz": "const cityGraph = {\n  'A': { 'B': 500, ... },\n  ...\n};",
          "ru": "const cityGraph = {\n  'A': { 'B': 500, ... },\n  ...\n};",
          "en": "const cityGraph = {\n  'A': { 'B': 500, ... },\n  ...\n};"
        },
        "fix": {
          "uz": "<b>GRAF KODI (Adjacency List):</b><br><pre><code>const cityGraph = {\n  'A': { 'B': 500, 'C': 800 },\n  'B': { 'A': 500, 'C': 300, 'D': 600 },\n  'C': { 'A': 800, 'B': 300, 'D': 400 },\n  'D': { 'B': 600, 'C': 400 }\n};</code></pre>",
          "ru": "<b>ГРАФ В ВИДЕ СПИСКА СМЕЖНОСТИ:</b><br><pre><code>const cityGraph = {\n  'A': { 'B': 500, 'C': 800 },\n  'B': { 'A': 500, 'C': 300, 'D': 600 },\n  'C': { 'A': 800, 'B': 300, 'D': 400 },\n  'D': { 'B': 600, 'C': 400 }\n};</code></pre>",
          "en": "<b>ADJACENCY LIST GRAPH OBJECT:</b><br><pre><code>const cityGraph = {\n  'A': { 'B': 500, 'C': 800 },\n  'B': { 'A': 500, 'C': 300, 'D': 600 },\n  'C': { 'A': 800, 'B': 300, 'D': 400 },\n  'D': { 'B': 600, 'C': 400 }\n};</code></pre>"
        }
      },
      {
        "num": 2,
        "points": "2.5 Ball",
        "title": {
          "uz": "2-Topshiriq: Dijkstra Algoritmi Bo'yicha Eng Qisqa Yo'lni Hisoblash",
          "ru": "Задание 2: Расчет кратчайшего пути по алгоритму Дейкстры",
          "en": "Task 2: Dijkstra Shortest Path Computation"
        },
        "desc": {
          "uz": "Yuqoridagi 1-topshiriq grafigidan foydalanib, Maktabdan (A) Stadionga (D) borishning eng qisqa yo'lini Dijkstra algoritmi qadamma-qadam tahlili asosida toping: Yo'l A ➔ B ➔ D qancha masofa bo'ladi? Yo'l A ➔ B ➔ C ➔ D qancha bo'ladi? Eng optimal marshrut qaysi?",
          "ru": "Используя граф из Задания 1, рассчитайте кратчайший путь от Школы (A) до Стадиона (D) по шагам алгоритма Дейкстры. Сравните варианты A-B-D и A-B-C-D.",
          "en": "Using the graph from Task 1, calculate the shortest route from School (A) to Stadium (D) following Dijkstra steps. Compare routes A-B-D vs A-B-C-D."
        },
        "ph": {
          "uz": "Dijkstra hisobi va optimal yo'lni bu yerga yozing...",
          "ru": "Опишите расчет Дейкстры здесь...",
          "en": "Document Dijkstra iterations and optimal path selection here..."
        },
        "fix": {
          "uz": "<b>DIJKSTRA TAHLILI:</b><br>1. 1-variant: A ➔ B ➔ D = 500m + 600m = <b>1100 metr</b>.<br>2. 2-variant: A ➔ C ➔ D = 800m + 400m = <b>1200 metr</b>.<br>3. 3-variant: A ➔ B ➔ C ➔ D = 500m + 300m + 400m = <b>1200 metr</b>.<br><b>Xulosa:</b> Eng qisqa va tez yo'l: <code>A ➔ B ➔ D</code> (1100 metr).",
          "ru": "<b>РАСЧЕТ ДЕЙКСТРЫ:</b><br>1. Путь A ➔ B ➔ D = 500 + 600 = 1100 м.<br>2. Путь A ➔ C ➔ D = 800 + 400 = 1200 м.<br>Оптимальный маршрут: <b>A ➔ B ➔ D (1100 м)</b>.",
          "en": "<b>DIJKSTRA ITERATION:</b><br>Path A ➔ B ➔ D yields 500 + 600 = 1100m. Path A ➔ C ➔ D yields 800 + 400 = 1200m. Optimal shortest route: <b>A ➔ B ➔ D (1100m)</b>."
        }
      },
      {
        "num": 3,
        "points": "2.5 Ball",
        "title": {
          "uz": "3-Topshiriq: Haversine Sferik Masofa Formulasi",
          "ru": "Задание 3: Формула сферического расстояния Гаверсинуса",
          "en": "Task 3: Haversine Great-Circle Distance Implementation"
        },
        "desc": {
          "uz": "Yer yuzidagi ikki GPS nuqta: (lat1, lon1) va (lat2, lon2) orasidagi masofani hisoblovchi JavaScript funksiyasini yozing. Nega oddiy tekislikdagi Pifagor formulasidan ko'ra Haversine formulasi aniqroq ekanligini tushuntiring.",
          "ru": "Напишите функцию на JS для вычисления расстояния между двумя координатами по формуле Гаверсинуса. Объясните, почему плоская теорема Пифагора не подходит для Земли.",
          "en": "Write a JavaScript function calculating distance between two GPS coordinates using the Haversine formula. Explain why planar Pythagorean math introduces errors on spherical Earth."
        },
        "ph": {
          "uz": "function haversineDistance(lat1, lon1, lat2, lon2) {\n  const R = 6371; // Yer radiusi (km)\n  ...\n}",
          "ru": "function haversineDistance(lat1, lon1, lat2, lon2) {\n  const R = 6371;\n  ...\n}",
          "en": "function haversineDistance(lat1, lon1, lat2, lon2) {\n  const R = 6371;\n  ...\n}"
        },
        "fix": {
          "uz": "<b>HAVERSINE FORMULASI KODI:</b><br><pre><code>function haversine(lat1, lon1, lat2, lon2) {\n  const R = 6371; // km\n  const toRad = deg => deg * Math.PI / 180;\n  const dLat = toRad(lat2 - lat1);\n  const dLon = toRad(lon2 - lon1);\n  const a = Math.sin(dLat/2)**2 + Math.cos(toRad(lat1)) * Math.cos(toRad(lat2)) * Math.sin(dLon/2)**2;\n  return R * 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1-a));\n}</code></pre>Sababi: Yer tekis emas, balki sferik shar shaklida.",
          "ru": "<b>КОД ГАВЕРСИНУСА:</b><br><pre><code>function haversine(lat1, lon1, lat2, lon2) {\n  const R = 6371;\n  const toRad = d => d * Math.PI / 180;\n  const dLat = toRad(lat2 - lat1), dLon = toRad(lon2 - lon1);\n  const a = Math.sin(dLat/2)**2 + Math.cos(toRad(lat1)) * Math.cos(toRad(lat2)) * Math.sin(dLon/2)**2;\n  return R * 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1-a));\n}</code></pre>",
          "en": "<b>HAVERSINE FUNCTION:</b><br><pre><code>function haversine(lat1, lon1, lat2, lon2) {\n  const R = 6371;\n  const toRad = d => d * Math.PI / 180;\n  const dLat = toRad(lat2 - lat1), dLon = toRad(lon2 - lon1);\n  const a = Math.sin(dLat/2)**2 + Math.cos(toRad(lat1)) * Math.cos(toRad(lat2)) * Math.sin(dLon/2)**2;\n  return R * 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1-a));\n}</code></pre>"
        }
      },
      {
        "num": 4,
        "points": "2.5 Ball",
        "title": {
          "uz": "4-Topshiriq: HTML5 Geolocation API Integratsiyasi",
          "ru": "Задание 4: Интеграция браузерного Geolocation API",
          "en": "Task 4: Browser HTML5 Geolocation API Integration"
        },
        "desc": {
          "uz": "Brauzerda tugma bosilganda foydalanuvchining joriy kenglik va uzunlik koordinatalarini ekranga chiqaruvchi va agar foydalanuvchi ruxsat bermasa xatoni ushlovchi to'liq JavaScript kodini yozing.",
          "ru": "Напишите JS-код для кнопки «Где я?», запрашивающий текущие координаты через navigator.geolocation.getCurrentPosition с обработкой ошибок.",
          "en": "Write JavaScript code for a 'Find My Location' action that requests coordinates using navigator.geolocation.getCurrentPosition and handles user denial errors."
        },
        "ph": {
          "uz": "function getMyGPS() {\n  if (navigator.geolocation) {\n    ...\n  }\n}",
          "ru": "function getMyGPS() {\n  if (navigator.geolocation) {\n    ...\n  }\n}",
          "en": "function getMyGPS() {\n  if (navigator.geolocation) {\n    ...\n  }\n}"
        },
        "fix": {
          "uz": "<b>GEOLOCATION KODI:</b><br><pre><code>function getMyGPS() {\n  if (!navigator.geolocation) return alert('GPS qo\\'llab-quvvatlanmaydi');\n  navigator.geolocation.getCurrentPosition(\n    pos => {\n      console.log('Kenglik:', pos.coords.latitude, 'Uzunlik:', pos.coords.longitude);\n    },\n    err => {\n      console.error('Geolokatsiyaga ruxsat berilmadi:', err.message);\n    },\n    { enableHighAccuracy: true, timeout: 5000 }\n  );\n}</code></pre>",
          "ru": "<b>КОД GEOLOCATION:</b><br><pre><code>function getMyGPS() {\n  if (!navigator.geolocation) return alert('GPS не поддерживается');\n  navigator.geolocation.getCurrentPosition(\n    pos => alert(`Широта: ${pos.coords.latitude}, Долгота: ${pos.coords.longitude}`),\n    err => alert(`Ошибка: ${err.message}`)\n  );\n}</code></pre>",
          "en": "<b>GEOLOCATION IMPLEMENTATION:</b><br><pre><code>function getMyGPS() {\n  if (!navigator.geolocation) return alert('Geolocation unsupported');\n  navigator.geolocation.getCurrentPosition(\n    pos => alert(`Lat: ${pos.coords.latitude}, Lon: ${pos.coords.longitude}`),\n    err => alert(`Error: ${err.message}`)\n  );\n}</code></pre>"
        }
      }
    ]
  },
  {
    "folder": "classes/5-6-sinf/7-hafta/21-dars-raqamli-iz-va-maxfiylik",
    "cohort_tag": "5-6-SINF · UY VAZIFASI",
    "eyebrow": {
      "uz": "5–6-SINF · 7-HAFTA · 21-DARS",
      "ru": "5–6-КЛАСС · 7-Я НЕДЕЛЯ · УРОК 21",
      "en": "GRADES 5–6 · WEEK 7 · LESSON 21"
    },
    "title": {
      "uz": "Raqamli Iz va Shaxsiy Maxfiylik — Mustaqil Amaliy Vazifa",
      "ru": "Цифровой След и Личная Конфиденциальность — Задание",
      "en": "Digital Footprint & Personal Privacy — Homework Assignment"
    },
    "subtitle": {
      "uz": "Katta Ekran Qoidasi, fotosuratlardagi yashirin EXIF GPS ma'lumotlarini tozalash va ijtimoiy tarmoq xavfsizligi bo'yicha mustaqil topshiriqlar.",
      "ru": "Правило Большого Экрана, удаление скрытых геотегов EXIF из фото и настройка приватности в социальных сетях.",
      "en": "Billboard Rule considerations, stripping EXIF GPS coordinates from media, and hardening social profile privacy."
    },
    "meta_course": "Cyber Hygiene & Digital Safety",
    "tasks": [
      {
        "num": 1,
        "points": "2.5 Ball",
        "title": {
          "uz": "1-Topshiriq: Katta Ekran Qoidasi (Billboard Rule) Sinovi",
          "ru": "Задание 1: Применение «Правила Большого Экрана»",
          "en": "Task 1: Applying the Billboard Rule to Daily Postings"
        },
        "desc": {
          "uz": "Kiber-xavfsizlikdagi 'Katta Ekran Qoidasi' (Billboard Rule) nima ekanligini o'z so'zlaringiz bilan tushuntiring. Quyidagi 3 ta holatdan qaysi birini internetga qo'yish xavfsiz, qaysilarini qo'yish esa xavfli:<br>a) Uy manzilimiz va maktabga boradigan yo'limiz ko'ringan video.<br>b) Musobaqada olgan diplomimiz va g'oliblik quvonchi.<br>c) Oilaviy samolyot chiptasi (bilet) va pasport rasmi.",
          "ru": "Объясните «Правило Большого Экрана». Оцените 3 ситуации: a) Видео с домашним адресом и маршрутом в школу; b) Фото диплома с олимпиады; c) Фото авиабилетов и паспорта.",
          "en": "Explain the Billboard Rule. Evaluate 3 scenarios: a) Video showing home address and school walking path; b) Photo of an academic award; c) Photo of boarding passes and passport."
        },
        "ph": {
          "uz": "Katta Ekran qoidasi va 3 ta holat tahlili...",
          "ru": "Анализ правила и 3 ситуаций...",
          "en": "Billboard rule summary and scenario evaluation..."
        },
        "fix": {
          "uz": "<b>TO'G'RI JAVOB:</b><br>1. <b>Katta Ekran Qoidasi:</b> 'Agar bu ma'lumot maktab oldidagi ulkan ekranda hamma ko'z o'ngida tursa, o'zimni noqulay his qilmaymanmi?' degan fikr bilan post qo'yish.<br>2. <b>Holatlar tahlili:</b><br>- <b>a) Xavfli!</b> Begonalar uyingizni va yurish vaqtingizni bilib oladi.<br>- <b>b) Xavfsiz!</b> Muvaffaqiyat va ijobiy yutuqlar raqamli izingizni chiroyli qiladi.<br>- <b>c) Juda xavfli!</b> Chiptadagi QR/shtrix-kod orqali firibgarlar barcha shaxsiy ma'lumotlaringizni o'g'irlashi mumkin.",
          "ru": "<b>ПРАВИЛЬНЫЙ ОТВЕТ:</b><br>a) Опасно (выдает геолокацию дома). b) Безопасно (формирует положительный цифровой след). c) Критически опасно (штрих-код билета содержит паспортные данные).",
          "en": "<b>ANALYSIS:</b><br>a) Hazardous (leaks home location and schedule). b) Safe (builds a constructive digital reputation). c) Critical risk (barcodes leak personal reservation data)."
        }
      },
      {
        "num": 2,
        "points": "2.5 Ball",
        "title": {
          "uz": "2-Topshiriq: Fotosuratlardagi Yashirin EXIF GPS Lokatsiyasi",
          "ru": "Задание 2: Скрытые метаданные EXIF и геолокация в фото",
          "en": "Task 2: Detecting and Stripping EXIF GPS Metadata"
        },
        "desc": {
          "uz": "Smartfoningizda xonangizda rasmga tushganingizda, rasm fayli ichiga ko'rinmas qanday yashirin ma'lumotlar yozilib qoladi? Nega bu rasmni internetga qo'yishdan oldin EXIF GPS ma'lumotlarini tozalash zarur?",
          "ru": "Какие скрытые метаданные (EXIF) записываются в снимок, сделанный дома на смартфон? Почему критически важно очищать геолокацию перед публикацией?",
          "en": "What hidden EXIF metadata tags are embedded when capturing photos at home on a smartphone? Why is stripping GPS tags imperative prior to online sharing?"
        },
        "ph": {
          "uz": "EXIF ma'lumotlari va tozalash sabablari...",
          "ru": "Описание данных EXIF и причин их удаления...",
          "en": "EXIF metadata description and scrubbing rationale..."
        },
        "fix": {
          "uz": "<b>EXIF TAHLILI:</b><br>1. Rasm ichiga: <b>Aniq GPS kenglik va uzunlik (uydagi aniq koordinatalar)</b>, rasm olingan sana va vaqt, telefon modeli va kamera sozlamalari yoziladi.<br>2. Xavfi: Kiber-jinoyatchi rasmni yuklab olib, maxsus dasturda uyingiz qayerdaligini 1 metr aniqlikda bilib oladi.<br>3. Himoya: Telefon kamerasi sozlamalarida 'Geotagging / Joylashuv'ni o'chirib qo'yish yoki maxsus dasturda EXIF-ni tozalash kerak.",
          "ru": "<b>АНАЛИЗ EXIF:</b><br>В фото вшиваются точные GPS-координаты дома, дата и модель телефона. Злоумышленник может узнать адрес с точностью до метра. Защита: отключать геолокацию в камере.",
          "en": "<b>EXIF SPECIFICATION:</b><br>Photos embed exact GPS lat/lon coordinates, timestamp, and hardware specs. Strangers can resolve your home location within meters. Mitigation: disable camera location tagging."
        }
      },
      {
        "num": 3,
        "points": "2.5 Ball",
        "title": {
          "uz": "3-Topshiriq: Ochiq Jamoat Wi-Fi Tarmoqlarida Kiber-Gigiyena",
          "ru": "Задание 3: Кибергигиена в открытых общественных сетях Wi-Fi",
          "en": "Task 3: Cyber Hygiene on Open Public Wi-Fi Networks"
        },
        "desc": {
          "uz": "Kafeda yoki savdo markazidagi ochiq (parolsiz) bepul Wi-Fi ga ulanganda kiber-xavfsizlikni ta'minlash uchun qanday 3 ta qat'iy qoidaga amal qilish kerak?",
          "ru": "Назовите 3 правила безопасности при подключении к открытому бесплатному Wi-Fi в кафе или ТЦ.",
          "en": "List 3 mandatory safety practices when connecting to open unsecured Wi-Fi in cafes or malls."
        },
        "ph": {
          "uz": "Ochiq Wi-Fi da 3 ta qoida...",
          "ru": "3 правила в открытом Wi-Fi...",
          "en": "3 rules for open public Wi-Fi..."
        },
        "fix": {
          "uz": "<b>OCHIQ WI-FI DA 3 QOIDA:</b><br>1. <b>VPN yoqish:</b> Internetga uzatilayotgan barcha ma'lumotlarni shifrlab, xakerlar paketlarni ushlashini to'xtatish.<br>2. <b>Parol va bank kartalarini kiritmaslik:</b> Ochiq tarmoqda hech qachon shaxsiy to'lovlarni amalga oshirmaslik.<br>3. <b>HTTPS qulfini tekshirish:</b> Sayt manzilida 'https://' va qulf belgisi bo'lmagan ochiq saytlarga kirmaslik.",
          "ru": "<b>3 ПРАВИЛА В ОТКРЫТОМ WI-FI:</b><br>1. Включать надежный VPN.<br>2. Не совершать банковских операций и не вводить пароли.<br>3. Проверять значок HTTPS (замочек) в браузере.",
          "en": "<b>3 PUBLIC WI-FI RULES:</b><br>1. Always engage an encrypted VPN tunnel.<br>2. Avoid entering banking credentials or payment cards.<br>3. Enforce valid HTTPS padlocks on all destinations."
        }
      },
      {
        "num": 4,
        "points": "2.5 Ball",
        "title": {
          "uz": "4-Topshiriq: Shaxsiy Profilni Himoyalash: Yopiq Profil va 2FA",
          "ru": "Задание 4: Защита профиля: Закрытый аккаунт и 2FA",
          "en": "Task 4: Social Account Hardening: Private Profiles & 2FA"
        },
        "desc": {
          "uz": "Telegram, Instagram yoki boshqa ijtimoiy tarmoqda o'z profilingizni xakerlar va begona firibgarlardan 100% himoya qilish uchun qanday sozlamalarni yoqishingiz kerak? Ikki bosqichli autentifikatsiya (2FA) nima uchun zarurligini tushuntiring.",
          "ru": "Какие настройки необходимо включить в Telegram или Instagram для защиты профиля? Зачем нужна двухфакторная аутентификация (2FA)?",
          "en": "Which configuration settings should be enabled in Telegram/Instagram to safeguard accounts? Why is Two-Factor Authentication (2FA) crucial?"
        },
        "ph": {
          "uz": "Maxfiylik sozlamalari va 2FA tushuntirishi...",
          "ru": "Настройки приватности и 2FA...",
          "en": "Privacy configuration and 2FA rationale..."
        },
        "fix": {
          "uz": "<b>PROFILNI HIMOYALASH REJASI:</b><br>1. <b>Profilni 'Yopiq (Private)' qilish:</b> Faqat siz tanigan va tasdiqlagan do'stlaringiz postlaringizni ko'ra oladi.<br>2. <b>Ikki bosqichli himoya (2FA):</b> Parol o'g'irlangan taqdirda ham, telefoningizga keladigan ikkinchi maxfiy kodsiz hech kim hisobingizga kira olmaydi.<br>3. <b>Begona qo'ng'iroq va xabarlarni cheklash:</b> Faqat kontaktlar ro'yxatidagi odamlarga ruxsat berish.",
          "ru": "<b>ПЛАН ЗАЩИТЫ АККАУНТА:</b><br>1. Сделать аккаунт приватным.<br>2. Включить 2FA (двухфакторную аутентификацию) — вход защищен паролем и кодом подтверждения.<br>3. Ограничить видимость номера телефона и фото только для контактов.",
          "en": "<b>ACCOUNT HARDENING CHECKLIST:</b><br>1. Enforce Private Account visibility.<br>2. Enable Two-Factor Authentication (2FA) so credential leaks alone cannot grant access.<br>3. Restrict phone number visibility and incoming chats strictly to personal contacts."
        }
      }
    ]
  }
]

def generate_vazifa_file(hw):
    folder = hw["folder"]
    cohort_tag = hw["cohort_tag"]
    eyebrow = hw["eyebrow"]
    title = hw["title"]
    subtitle = hw["subtitle"]
    meta_course = hw["meta_course"]
    tasks = hw["tasks"]

    tasks_html = []
    for t in tasks:
        t_num = t["num"]
        t_pts = t["points"]
        t_title = t["title"]
        t_desc = t["desc"]
        t_ph = t["ph"]
        t_fix = t["fix"]

        tasks_html.append(f"""
  <!-- TASK {t_num} -->
  <section class="task-card">
    <div class="task-header">
      <span class="task-badge" data-ru="ЗАДАНИЕ {t_num} · {t_pts}" data-en="TASK {t_num} · {t_pts}">{t_num}-TOPSHIRIQ · {t_pts}</span>
      <span class="task-status" id="status_task{t_num}" data-ru="Не заполнено" data-en="Empty">Kiritilmagan</span>
    </div>
    <h3 class="task-title" data-ru="{html.escape(t_title['ru'])}" data-en="{html.escape(t_title['en'])}">
      {html.escape(t_title['uz'])}
    </h3>
    <p class="task-desc" data-ru="{html.escape(t_desc['ru'])}" data-en="{html.escape(t_desc['en'])}">
      {t_desc['uz']}
    </p>
    <textarea class="input-box" id="task{t_num}_ans" rows="4"
              placeholder="{html.escape(t_ph['uz'])}"
              data-placeholder-ru="{html.escape(t_ph['ru'])}"
              data-placeholder-en="{html.escape(t_ph['en'])}"
              oninput="saveAnswer({t_num})"></textarea>
    <div class="task-actions">
      <button type="button" class="fix-btn" onclick="toggleFix({t_num})" data-ru="Показать решение (Fix)" data-en="Show Solution (Fix)">Yechimni ko'rish (Fix)</button>
    </div>
    <div class="fix-box" id="fix_{t_num}">
      <div class="fix-text" data-ru="{html.escape(t_fix['ru'])}" data-en="{html.escape(t_fix['en'])}">
        {t_fix['uz']}
      </div>
    </div>
  </section>""")

    page_html = f"""<!DOCTYPE html>
<html lang="uz" data-theme="dark">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title data-ru="{html.escape(title['ru'])}" data-en="{html.escape(title['en'])}">{html.escape(title['uz'])}</title>
<link rel="icon" type="image/svg+xml" href="/assets/favicon.svg">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Manrope:wght@600;700;800&family=Source+Sans+3:wght@400;600;700&family=JetBrains+Mono:wght@400;600;700&display=swap">

<style>
:root {{
  --bg: #07152D;
  --sheet: #0B1D3A;
  --panel: #0E2246;
  --panel-2: #142E5C;
  --panel-hover: #19386D;
  --ink: #F0F4FA;
  --ink-2: #A5B6D0;
  --ink-3: #6C819F;
  --rule: #1B355A;
  --rule-light: rgba(255, 255, 255, 0.08);
  --accent: #FF3B26;
  --accent-ink: #FF7563;
  --accent-soft: rgba(255, 59, 38, 0.12);
  --green: #10B981;
  --green-soft: rgba(16, 185, 129, 0.12);
  --red: #EF4444;
  --red-soft: rgba(239, 68, 68, 0.12);
  --glass-bg: rgba(14, 34, 70, 0.88);
  --glass-border: rgba(255, 255, 255, 0.12);
  --radius-sm: 8px;
  --radius-md: 14px;
  --radius-lg: 20px;
  --shadow-sm: 0 4px 12px rgba(0, 0, 0, 0.25);
}}

:root[data-theme="light"] {{
  --bg: #F8FAFD;
  --sheet: #FFFFFF;
  --panel: #FFFFFF;
  --panel-2: #EDF2F9;
  --panel-hover: #E3EAF5;
  --ink: #00214A;
  --ink-2: #384A68;
  --ink-3: #7586A2;
  --rule: #DCE4EF;
  --rule-light: rgba(0, 33, 74, 0.06);
  --accent: #FF1100;
  --accent-ink: #C21000;
  --accent-soft: #FFEAE6;
  --green: #0B6B4F;
  --green-soft: #DDF0E8;
  --red: #C21000;
  --red-soft: #FDE8E6;
  --glass-bg: rgba(255, 255, 255, 0.92);
  --glass-border: rgba(0, 33, 74, 0.12);
  --shadow-sm: 0 2px 8px rgba(0, 33, 74, 0.06);
}}

*, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}

body {{
  font-family: "Source Sans 3", sans-serif;
  background: var(--bg);
  color: var(--ink);
  line-height: 1.5;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  transition: background 0.2s ease, color 0.2s ease;
  padding-bottom: 80px;
}}

/* Floating Header Nav */
.top-nav {{
  position: sticky;
  top: 14px;
  z-index: 100;
  max-width: 960px;
  width: calc(100% - 32px);
  margin: 0 auto 28px;
  background: var(--glass-bg);
  backdrop-filter: blur(14px);
  -webkit-backdrop-filter: blur(14px);
  border: 1px solid var(--glass-border);
  padding: 8px 18px;
  border-radius: 999px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  box-shadow: var(--shadow-sm);
}}

.nav-brand {{
  display: flex;
  align-items: center;
  gap: 10px;
  text-decoration: none;
  color: var(--ink);
}}

.nav-brand .logo-box img {{
  height: 22px;
  width: auto;
  display: block;
}}

.nav-brand .name {{
  font-family: "Manrope", sans-serif;
  font-weight: 800;
  font-size: 14px;
  letter-spacing: 0.04em;
}}

.nav-brand .tag {{
  font-family: "JetBrains Mono", monospace;
  font-size: 11px;
  font-weight: 700;
  color: var(--ink-2);
  letter-spacing: 0.08em;
  text-transform: uppercase;
  padding-left: 8px;
  border-left: 1px solid var(--rule);
}}

.nav-tools {{
  display: flex;
  align-items: center;
  gap: 4px;
}}

.dock-btn {{
  background: transparent;
  border: none;
  color: var(--ink-2);
  font-family: "JetBrains Mono", monospace;
  font-size: 12px;
  font-weight: 700;
  padding: 6px 12px;
  border-radius: 999px;
  cursor: pointer;
  transition: all 0.18s ease;
  text-decoration: none;
  display: inline-flex;
  align-items: center;
  justify-content: center;
}}

.dock-btn:hover {{
  color: var(--ink);
  background: var(--rule-light);
}}

.dock-btn.active {{
  color: var(--ink);
  background: var(--panel-2);
  border: 1px solid var(--rule);
  box-shadow: 0 2px 6px rgba(0,0,0,0.12);
}}

.container {{
  max-width: 960px;
  width: calc(100% - 32px);
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  gap: 24px;
}}

.hero-section {{
  background: var(--sheet);
  border: 1px solid var(--rule);
  border-radius: var(--radius-lg);
  padding: 32px;
  box-shadow: var(--shadow-sm);
  position: relative;
  overflow: hidden;
}}

.hero-section::before {{
  content: "";
  position: absolute;
  top: 0; left: 0; right: 0;
  height: 4px;
  background: linear-gradient(90deg, var(--accent) 0%, #6366F1 100%);
}}

.eyebrow {{
  font-family: "JetBrains Mono", monospace;
  font-size: 12px;
  font-weight: 700;
  color: var(--accent);
  text-transform: uppercase;
  letter-spacing: 0.1em;
  margin-bottom: 8px;
}}

.page-title {{
  font-family: "Manrope", sans-serif;
  font-size: clamp(24px, 3.2vw, 36px);
  font-weight: 800;
  letter-spacing: -0.02em;
  line-height: 1.25;
  color: var(--ink);
  margin-bottom: 12px;
}}

.subtitle {{
  font-size: 15px;
  color: var(--ink-2);
  line-height: 1.6;
}}

.meta-grid {{
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 16px;
  margin-top: 24px;
  padding-top: 20px;
  border-top: 1px solid var(--rule);
}}

.meta-item {{
  display: flex;
  flex-direction: column;
  gap: 4px;
}}

.meta-item b {{
  font-family: "JetBrains Mono", monospace;
  font-size: 11px;
  color: var(--ink-3);
  text-transform: uppercase;
  letter-spacing: 0.06em;
}}

.meta-item span {{
  font-size: 14px;
  font-weight: 600;
  color: var(--ink);
}}

.student-card {{
  background: var(--panel);
  border: 1px solid var(--rule);
  border-radius: var(--radius-md);
  padding: 20px 24px;
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  gap: 16px;
}}

.field-group {{
  display: flex;
  flex-direction: column;
  gap: 6px;
}}

.field-group label {{
  font-family: "JetBrains Mono", monospace;
  font-size: 11px;
  font-weight: 700;
  color: var(--ink-2);
  text-transform: uppercase;
}}

.field-group input, .field-group select {{
  background: var(--bg);
  border: 1px solid var(--rule);
  border-radius: var(--radius-sm);
  color: var(--ink);
  font-family: inherit;
  font-size: 14px;
  padding: 8px 12px;
  outline: none;
  transition: all 0.2s ease;
}}

.field-group input:focus, .field-group select:focus {{
  border-color: #6366F1;
  box-shadow: 0 0 0 3px rgba(99, 102, 241, 0.25);
}}

.task-card {{
  background: var(--panel);
  border: 1px solid var(--rule);
  border-radius: var(--radius-md);
  padding: 28px;
  display: flex;
  flex-direction: column;
  gap: 16px;
  box-shadow: var(--shadow-sm);
}}

.task-header {{
  display: flex;
  align-items: center;
  justify-content: space-between;
}}

.task-badge {{
  font-family: "JetBrains Mono", monospace;
  font-size: 12px;
  font-weight: 700;
  color: var(--accent);
  background: var(--accent-soft);
  padding: 4px 10px;
  border-radius: 999px;
  letter-spacing: 0.06em;
}}

.task-status {{
  font-family: "JetBrains Mono", monospace;
  font-size: 11px;
  font-weight: 700;
  color: var(--ink-3);
}}

.task-status.filled {{
  color: var(--green);
}}

.task-title {{
  font-family: "Manrope", sans-serif;
  font-size: 18px;
  font-weight: 700;
  color: var(--ink);
}}

.task-desc {{
  font-size: 14px;
  color: var(--ink-2);
  line-height: 1.6;
}}

.input-box {{
  width: 100%;
  background: var(--bg);
  border: 1px solid var(--rule);
  border-radius: var(--radius-sm);
  padding: 14px;
  font-family: "JetBrains Mono", monospace;
  font-size: 13px;
  color: var(--ink);
  line-height: 1.5;
  resize: vertical;
  min-height: 100px;
  outline: none;
  transition: all 0.2s ease;
}}

.input-box:focus {{
  border-color: #6366F1;
  box-shadow: 0 0 0 3px rgba(99, 102, 241, 0.25);
}}

.task-actions {{
  display: flex;
  justify-content: flex-end;
}}

.fix-btn {{
  background: var(--panel-2);
  border: 1px solid var(--rule);
  color: var(--ink-2);
  font-family: "JetBrains Mono", monospace;
  font-size: 12px;
  font-weight: 700;
  padding: 6px 14px;
  border-radius: 999px;
  cursor: pointer;
  transition: all 0.15s ease;
}}

.fix-btn:hover {{
  color: var(--ink);
  background: var(--rule-light);
  border-color: var(--ink-3);
}}

.fix-box {{
  display: none;
  background: var(--panel-2);
  border-left: 3px solid var(--green);
  border-radius: 4px;
  padding: 16px;
  font-size: 13px;
  line-height: 1.6;
  color: var(--ink);
}}

.fix-box pre {{
  margin-top: 8px;
  background: var(--bg);
  padding: 12px;
  border-radius: 6px;
  overflow-x: auto;
  font-family: "JetBrains Mono", monospace;
}}

.rubric-card {{
  background: var(--sheet);
  border: 1px solid var(--rule);
  border-radius: var(--radius-md);
  padding: 28px;
}}

.rubric-card h3 {{
  font-family: "Manrope", sans-serif;
  font-size: 18px;
  font-weight: 700;
  margin-bottom: 16px;
}}

.rubric-table {{
  width: 100%;
  border-collapse: collapse;
  font-size: 13px;
}}

.rubric-table th, .rubric-table td {{
  padding: 10px 14px;
  border-bottom: 1px solid var(--rule);
  text-align: left;
}}

.rubric-table th {{
  font-family: "JetBrains Mono", monospace;
  font-size: 11px;
  text-transform: uppercase;
  color: var(--ink-3);
}}

@media print {{
  body {{ background: #fff !important; color: #000 !important; padding: 0 !important; }}
  .top-nav, .task-actions, .field-group input, .field-group select {{ display: none !important; }}
  .container {{ width: 100% !important; max-width: 100% !important; }}
  .fix-box {{ display: block !important; border-left-color: #000 !important; background: #f4f4f4 !important; color: #000 !important; }}
  .input-box {{ border: 1px solid #000 !important; background: #fff !important; color: #000 !important; }}
  .task-card, .hero-section, .rubric-card {{ border: 1px solid #ccc !important; background: #fff !important; color: #000 !important; box-shadow: none !important; }}
}}
</style>
</head>
<body>

<!-- Floating Header Nav -->
<nav class="top-nav">
  <a href="/index.html" class="nav-brand">
    <div class="logo-box"><img src="/assets/target-logo.png" alt="Target Logo"></div>
    <span class="name">TARGET</span>
    <span class="tag">{cohort_tag}</span>
  </a>
  <div class="nav-tools">
    <button type="button" class="dock-btn lang-btn active" data-lang="uz" onclick="setLang('uz')">UZ</button>
    <button type="button" class="dock-btn lang-btn" data-lang="ru" onclick="setLang('ru')">RU</button>
    <button type="button" class="dock-btn lang-btn" data-lang="en" onclick="setLang('en')">EN</button>
    <button type="button" class="dock-btn" onclick="toggleTheme()" title="Mavzu" data-title-ru="Тема" data-title-en="Theme">🌓</button>
    <button type="button" class="dock-btn" onclick="window.print()" title="Chop etish" data-title-ru="Печать" data-title-en="Print">🖨️</button>
    <a href="/index.html" class="dock-btn back-btn" title="Bosh sahifa" data-title-ru="Главная" data-title-en="Home">🏠</a>
  </div>
</nav>

<div class="container">

  <!-- HERO SECTION -->
  <header class="hero-section">
    <div class="eyebrow" data-ru="{html.escape(eyebrow['ru'])}" data-en="{html.escape(eyebrow['en'])}">
      {html.escape(eyebrow['uz'])}
    </div>
    <h1 class="page-title" data-ru="{html.escape(title['ru'])}" data-en="{html.escape(title['en'])}">
      {html.escape(title['uz'])}
    </h1>
    <p class="subtitle" data-ru="{html.escape(subtitle['ru'])}" data-en="{html.escape(subtitle['en'])}">
      {html.escape(subtitle['uz'])}
    </p>

    <div class="meta-grid">
      <div class="meta-item">
        <b data-ru="КУРС / НАПРАВЛЕНИЕ" data-en="COURSE / TRACK">KURS / YO'NALISH</b>
        <span>{meta_course}</span>
      </div>
      <div class="meta-item">
        <b data-ru="СРОК СДАЧИ" data-en="DEADLINE">TOPSHIRISH MUDDATI</b>
        <span data-ru="К следующему уроку" data-en="Before next class">Keyingi darsgacha</span>
      </div>
      <div class="meta-item">
        <b data-ru="МАКСИМАЛЬНЫЙ БАЛЛ" data-en="MAX SCORE">MAKSIMAL BALL</b>
        <span>10 Ball (10.0 / 10.0)</span>
      </div>
    </div>
  </header>

  <!-- STUDENT PROFILE -->
  <div class="student-card">
    <div class="field-group">
      <label for="studentName" data-ru="Ф.И.О. Ученика" data-en="Student Full Name">O'quvchi F.I.Sh.</label>
      <input type="text" id="studentName" placeholder="Ism Familiya" data-placeholder-ru="Имя Фамилия" data-placeholder-en="First Last name" oninput="saveProfile()">
    </div>
    <div class="field-group">
      <label for="studentClass" data-ru="Класс" data-en="Class">Sinf</label>
      <input type="text" id="studentClass" placeholder="9-A" data-placeholder-ru="9-A" data-placeholder-en="9-A" oninput="saveProfile()">
    </div>
    <div class="field-group">
      <label for="submissionDate" data-ru="Дата" data-en="Date">Sana</label>
      <input type="date" id="submissionDate" oninput="saveProfile()">
    </div>
  </div>

  <!-- TASKS LIST -->
  {"".join(tasks_html)}

  <!-- RUBRIC TABLE -->
  <section class="rubric-card">
    <h3 data-ru="Критерии официальной оценки (10 баллов)" data-en="Official Grading Rubric (10 Points)">Rasmiy Baholash Mezoni (10 Ball)</h3>
    <table class="rubric-table">
      <thead>
        <tr>
          <th data-ru="Балл" data-en="Points">Ball</th>
          <th data-ru="Критерий выполнения" data-en="Evaluation Criteria">Bajarish Mezoni</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td data-ru="8.5 – 10.0 Баллов" data-en="8.5 – 10.0 Points"><b>8.5 – 10.0 Ball</b></td>
          <td data-ru="Все 4 задания выполнены на высоком инженерном уровне, синтаксис точен, граничные условия учтены." data-en="All 4 tasks completed with robust engineering accuracy, correct syntax, and boundary conditions.">Barcha 4 ta topshiriq to'liq, chuqur va xatosiz bajarilgan, sintaksis va mantiq to'g'ri.</td>
        </tr>
        <tr>
          <td data-ru="6.0 – 8.0 Баллов" data-en="6.0 – 8.0 Points"><b>6.0 – 8.0 Ball</b></td>
          <td data-ru="3 задания выполнены полностью, концепции понятны, присутствуют мелкие синтаксические неточности." data-en="3 tasks fully satisfied, solid understanding, minor syntax gaps.">3 ta topshiriq to'liq bajarilgan, asosiy arxitektura to'g'ri, kichik kamchiliklar bor.</td>
        </tr>
        <tr>
          <td data-ru="1.0 – 5.5 Баллов" data-en="1.0 – 5.5 Points"><b>1.0 – 5.5 Ball</b></td>
          <td data-ru="Выполнено 1–2 задания, есть пробелы в архитектуре и коде, требуется доработка." data-en="Only 1-2 tasks attempted, notable architectural gaps, requires revision.">Faqat 1–2 ta topshiriq qisman bajarilgan, tushunchalar to'liq ochilmagan.</td>
        </tr>
      </tbody>
    </table>
  </section>

</div>

<script>
var currentLang = 'uz';

function setLang(lang) {{
  currentLang = lang;
  try {{ localStorage.setItem('target_lang', lang); }} catch(e) {{}}
  document.documentElement.lang = lang;
  document.querySelectorAll('.lang-btn').forEach(function(b) {{
    b.classList.toggle('active', b.getAttribute('data-lang') === lang);
  }});

  // Update in-place translations
  document.querySelectorAll('[data-ru], [data-en]').forEach(function(el) {{
    if (!el.getAttribute('data-uz-orig')) {{
      el.setAttribute('data-uz-orig', el.innerHTML);
    }}
    if (lang === 'uz') {{
      el.innerHTML = el.getAttribute('data-uz-orig');
    }} else if (lang === 'ru' && el.getAttribute('data-ru')) {{
      el.innerHTML = el.getAttribute('data-ru');
    }} else if (lang === 'en' && el.getAttribute('data-en')) {{
      el.innerHTML = el.getAttribute('data-en');
    }}
  }});

  // Update placeholders
  document.querySelectorAll('[data-placeholder-ru], [data-placeholder-en]').forEach(function(el) {{
    if (!el.getAttribute('data-ph-uz-orig')) {{
      el.setAttribute('data-ph-uz-orig', el.getAttribute('placeholder') || '');
    }}
    if (lang === 'uz') {{
      el.setAttribute('placeholder', el.getAttribute('data-ph-uz-orig'));
    }} else if (lang === 'ru' && el.getAttribute('data-placeholder-ru')) {{
      el.setAttribute('placeholder', el.getAttribute('data-placeholder-ru'));
    }} else if (lang === 'en' && el.getAttribute('data-placeholder-en')) {{
      el.setAttribute('placeholder', el.getAttribute('data-placeholder-en'));
    }}
  }});
}}

function toggleTheme() {{
  var cur = document.documentElement.getAttribute('data-theme') || 'dark';
  var next = cur === 'dark' ? 'light' : 'dark';
  document.documentElement.setAttribute('data-theme', next);
  try {{ localStorage.setItem('target_theme', next); }} catch(e) {{}}
}}

function toggleFix(num) {{
  var b = document.getElementById('fix_' + num);
  if (!b) return;
  b.style.display = (b.style.display === 'block') ? 'none' : 'block';
}}

var storagePrefix = 'target_vazifa_{os.path.basename(folder)}_';

function saveAnswer(num) {{
  var val = document.getElementById('task' + num + '_ans').value;
  try {{ localStorage.setItem(storagePrefix + 'ans_' + num, val); }} catch(e) {{}}
  updateStatus(num, val);
}}

function updateStatus(num, val) {{
  var s = document.getElementById('status_task' + num);
  if (!s) return;
  if (val && val.trim().length > 10) {{
    s.classList.add('filled');
    s.textContent = (currentLang === 'ru') ? 'Заполнено ✓' : (currentLang === 'en' ? 'Answered ✓' : 'Bajarildi ✓');
  }} else {{
    s.classList.remove('filled');
    s.textContent = (currentLang === 'ru') ? 'Не заполнено' : (currentLang === 'en' ? 'Empty' : 'Kiritilmagan');
  }}
}}

function saveProfile() {{
  var p = {{
    name: document.getElementById('studentName').value,
    sClass: document.getElementById('studentClass').value,
    date: document.getElementById('submissionDate').value
  }};
  try {{ localStorage.setItem(storagePrefix + 'profile', JSON.stringify(p)); }} catch(e) {{}}
}}

function loadSaved() {{
  try {{
    var p = JSON.parse(localStorage.getItem(storagePrefix + 'profile') || '{{}}');
    if (p.name) document.getElementById('studentName').value = p.name;
    if (p.sClass) document.getElementById('studentClass').value = p.sClass;
    if (p.date) document.getElementById('submissionDate').value = p.date;

    for (var i = 1; i <= 4; i++) {{
      var ans = localStorage.getItem(storagePrefix + 'ans_' + i);
      if (ans) {{
        document.getElementById('task' + i + '_ans').value = ans;
        updateStatus(i, ans);
      }}
    }}
  }} catch(e) {{}}
}}

document.addEventListener('DOMContentLoaded', function() {{
  var savedTheme = 'dark';
  try {{ savedTheme = localStorage.getItem('target_theme') || 'dark'; }} catch(e) {{}}
  document.documentElement.setAttribute('data-theme', savedTheme);

  var savedLang = 'uz';
  try {{ savedLang = localStorage.getItem('target_lang') || 'uz'; }} catch(e) {{}}
  setLang(savedLang);

  loadSaved();
}});
</script>
</body>
</html>
"""
    target_path = os.path.join(folder, "vazifa.html")
    with open(target_path, "w", encoding="utf-8") as f:
        f.write(page_html)
    print(f"✓ Generated {target_path}")
    return target_path

def main():
    for hw in HOMEWORKS:
        generate_vazifa_file(hw)
    print("\nAll 4 new vazifa.html homework apps generated successfully!")

if __name__ == "__main__":
    main()
