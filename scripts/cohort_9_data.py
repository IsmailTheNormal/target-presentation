#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Cohort 9-sinf planned weeks (Weeks 6–36) for Target International School.
5 hours/week. Junior Vibecoders, Full-Stack, Linux & DevOps.
"""

WEEKS_9_PLANNED = {
    6: {
        "title": {"uz": "Ilg'or Backend Muhandisligi: MVC va Relyatsion Bog'lanishlar", "ru": "Продвинутая Бэкенд Инженерия: MVC и Связи в Базе", "en": "Advanced Backend Engineering: MVC and Relational DB"},
        "type": {"uz": "Backend Lab", "ru": "Бэкенд Лаб", "en": "Backend Lab"},
        "skills": {"uz": "MVC (Model-View-Controller) arxitekturasi, Middleware zanjirlari, SQLite da Foreign Keys (Tashqi kalitlar), 1-to-Many va Many-to-Many bog'lanishlar", "ru": "Архитектура MVC, цепочки Middleware, внешние ключи (Foreign Keys) в SQLite, связи 1-ко-Многим и Многие-ко-Многим", "en": "MVC architecture, middleware pipelines, relational foreign keys in SQLite, One-to-Many and Many-to-Many schemas"},
        "deliverable": {"uz": "Mijozlar, buyurtmalar va mahsulotlarni o'zaro bog'lovchi to'liq relyatsion Express REST API", "ru": "Реляционный Express REST API, связывающий клиентов, заказы и товары", "en": "Relational Express REST API linking users, orders, and products with referential integrity"},
        "tools": "Node.js, Express.js, SQLite, Postman"
    },
    7: {
        "title": {"uz": "Veb-Ilova Kiber-Xavfsizligi: XSS, CSRF va Input Sanitization", "ru": "Кибербезопасность Веб-Приложений: XSS, CSRF и Санитизация", "en": "Web Application CyberSecurity: XSS, CSRF, and Input Sanitization"},
        "type": {"uz": "Xavfsizlik Lab", "ru": "Безопасность Лаб", "en": "Security Lab"},
        "skills": {"uz": "Cross-Site Scripting (XSS) mudofaasi, CSRF tokenlar, Helmet kutubxonasi, SQL Injection ga qarshi tayyorlangan so'rovlar (Prepared Statements)", "ru": "Защита от XSS, CSRF токены, библиотека Helmet, подготовленные запросы (Prepared Statements) против SQLi", "en": "XSS mitigation, CSRF tokens, Helmet middleware headers, parameterized SQL queries, input sanitization"},
        "deliverable": {"uz": "Xakerlik hujumlariga qarshi mustahkamlangan va xavfsizlik testlaridan o'tgan Express serveri", "ru": "Защищенный от атак сервер Express, прошедший проверку безопасности", "en": "Hardened Express backend verified against common OWASP injection vectors"},
        "tools": "Helmet.js, DOMPurify, Express-Validator, Burp Suite"
    },
    8: {
        "title": {"uz": "1-Chorak Oraliq Nazorat: Full-Stack Xavfsiz Servis Imtihoni", "ru": "Промежуточный Контроль 1-й Четверти: Защищенный Full-Stack Сервис", "en": "Quarter 1 Midterm Exam: Hardened Full-Stack Service"},
        "type": {"uz": "Oraliq Imtihon", "ru": "Промежуточный Экзамен", "en": "Midterm Examination"},
        "skills": {"uz": "Frontend interfeysini xavfsiz backend va SQLite bazasi bilan integratsiya qilish, Docker konteynerida ishga tushirish", "ru": "Интеграция фронтенда с бэкендом и SQLite, запуск в Docker контейнере", "en": "Full-stack integration of frontend UI, secure Express backend, SQLite DB, and Docker containerization"},
        "deliverable": {"uz": "Oraliq nazorat topshirig'i bo'yicha to'liq ishga tushirilgan va sinovdan o'tgan Full-Stack ilova (10 ballik mezon)", "ru": "Работающее Full-Stack приложение, проверенное по тестам (10-балльная шкала)", "en": "Working end-to-end full-stack containerized web service meeting all test specs (10-point rubric)"},
        "tools": "Docker, Express, SQLite, Vanilla JS, Jest"
    },
    9: {
        "title": {"uz": "1-Chorak Demo Day: Ishlab Turgan Full-Stack Veb-Servislar Taqdimoti", "ru": "Demo Day 1-й Четверти: Презентация Full-Stack Веб-Сервисов", "en": "Quarter 1 Demo Day: Live Full-Stack Web Services Showcase"},
        "type": {"uz": "Demo Day / Taqdimot", "ru": "Demo Day / Презентация", "en": "Demo Day / Presentation"},
        "skills": {"uz": "Loyiha taqdimoti, Texnik arxitekturani tushuntirish, Jonli serverni ko'rsatish, Savol-javob madaniyati", "ru": "Презентация проекта, защита технической архитектуры, живая демонстрация, культура ответов на вопросы", "en": "Project presentation, architectural walkthrough, live server demonstration, and Q&A defense"},
        "deliverable": {"uz": "Internetda ishlayotgan shaxsiy Full-Stack loyiha portfeli va 1-Chorak Muhandislik Sertifikati", "ru": "Портфолио работающего Full-Stack проекта в сети и сертификат 1-й четверти", "en": "Live cloud-hosted full-stack web project portfolio entry and Quarter 1 Engineering Certificate"},
        "tools": "Vercel / Render, GitHub Repo, Live Demo"
    },
    10: {
        "title": {"uz": "Zamonaviy JavaScript (ES6+): Modullar va Asinxron Chuqurlik", "ru": "Современный JavaScript (ES6+): Модули и Асинхронность", "en": "Modern JavaScript (ES6+): Modules and Async Deep Dive"},
        "type": {"uz": "Frontend Asos", "ru": "Фронтенд База", "en": "Frontend Foundation"},
        "skills": {"uz": "ES Modules (import/export), Destructuring, Spread/Rest operatorlari, Promises, Async/Await va xatolarni boshqarish", "ru": "ES Модули (import/export), деструктуризация, Spread/Rest, промисы, Async/Await и обработка ошибок", "en": "ES Modules (import/export), object destructuring, spread/rest syntax, Promises, and robust Async/Await"},
        "deliverable": {"uz": "Modullarga bo'lingan va toza asinxron oqim bilan yozilgan JavaScript kutubxonasi", "ru": "Модульная библиотека JavaScript с чистым асинхронным кодом", "en": "Modularized ES6+ utility library with comprehensive async data fetching pipeline"},
        "tools": "Node.js, ES6 Modules, Chrome DevTools"
    },
    11: {
        "title": {"uz": "Komponentlar Falsafasi: Qayta Ishlatiluvchi UI Bloklari", "ru": "Философия Компонентов: Переиспользуемые Блоки UI", "en": "Component Philosophy: Reusable UI Building Blocks"},
        "type": {"uz": "UI Arxitektura", "ru": "UI Архитектура", "en": "UI Architecture"},
        "skills": {"uz": "Komponentli fikrlash, Props (parametrlarni uzatish), State (ichki holat), UI qismlarini mustaqil modullarga ajratish", "ru": "Компонентное мышление, Props, State, разделение интерфейса на независимые модули", "en": "Component-driven design, Props data passing, State encapsulation, declarative rendering"},
        "deliverable": {"uz": "Tugmalar, kartochkalar va modal oynalardan iborat shaxsiy UI komponentlar to'plami", "ru": "Библиотека собственных UI компонентов (кнопки, карточки, модальные окна)", "en": "Custom lightweight UI component library (Buttons, Modals, Cards) with state toggling"},
        "tools": "Modern JS Components, Web Components / Alpine.js"
    },
    12: {
        "title": {"uz": "SPA (Single Page Application) Asoslari va Client-Side Routing", "ru": "Основы SPA (Single Page Application) и Клиентский Роутинг", "en": "SPA Foundations and Client-Side Routing"},
        "type": {"uz": "Interaktiv Lab", "ru": "Интерактивная Лаб", "en": "Interactive Lab"},
        "skills": {"uz": "Tarix API (History API), pushState/replaceState, Sahifa yangilanmasdan kontent o'zgarishi, Dinamik URL marshrutlari", "ru": "History API, pushState, смена контента без перезагрузки, динамические URL маршруты", "en": "HTML5 History API, pushState routing, seamless page switching without reload, dynamic URL parameters"},
        "deliverable": {"uz": "Brauzer qayta yuklanmasdan ishlovchi ko'p sahifali SPA ilova prototipi", "ru": "Прототип многостраничного SPA приложения без перезагрузки браузера", "en": "Single Page Application (SPA) prototype with lightning-fast route navigation and URL sync"},
        "tools": "History API, Custom Router, Vanilla JS"
    },
    13: {
        "title": {"uz": "Real-Vaqt Texnologiyalari: WebSockets va Jonli Chat", "ru": "Технологии Реального Времени: WebSockets и Живой Чат", "en": "Real-Time Technologies: WebSockets and Live Chat"},
        "type": {"uz": "Tarmoq Lab", "ru": "Сетевая Лаб", "en": "Networking Lab"},
        "skills": {"uz": "HTTP vs WebSockets, ws protokoli, Ikki tomonlama ochiq ulanish (Full-duplex), Xabarlar almashish va xonalarga bo'linish", "ru": "Сравнение HTTP и WebSockets, протокол ws, дуплексное соединение, обмен сообщениями и комнаты", "en": "HTTP polling vs WebSockets, ws protocol handshake, full-duplex messaging channels, rooms and broadcasts"},
        "deliverable": {"uz": "Bir nechta foydalanuvchi bir vaqtda suhbatlashadigan haqiqiy jonli chat xonasi", "ru": "Живой чат реального времени с поддержкой нескольких одновременных пользователей", "en": "Real-time collaborative chat room with multi-user presence and instant broadcasting"},
        "tools": "Node.js, ws / Socket.io, Chrome Network Tab"
    },
    14: {
        "title": {"uz": "Formalar, Muntazam Ifodalar (Regex) va Real-Vaqt Validatsiyasi", "ru": "Формы, Регулярные Выражения (Regex) и Валидация", "en": "Forms, Regular Expressions (Regex), and Real-Time Validation"},
        "type": {"uz": "Amaliy Lab", "ru": "Практическая Лаб", "en": "Hands-on Lab"},
        "skills": {"uz": "Regex sintaksisi (email, telefon, murakkab parollar), Dinamik xatolik ko'rsatish, Accessible (a11y) formalar", "ru": "Синтаксис Regex (email, телефон, пароли), динамический показ ошибок, доступность (a11y)", "en": "Regular Expressions (Regex patterns for email, phone, secure passwords), real-time DOM feedback, a11y"},
        "deliverable": {"uz": "Barcha xatolarni foydalanuvchi yozayotgan paytda ko'rsatuvchi aqlli ro'yxatdan o'tish formasi", "ru": "Умная форма регистрации с мгновенной валидацией и подсветкой ошибок", "en": "Production registration form with instant regex validation, password strength meter, and error badges"},
        "tools": "Regex101, HTML5 Constraint Validation, Vanilla JS"
    },
    15: {
        "title": {"uz": "NPM Ekotizimi, Tashqi Paketlar va Xavfsizlik Auditi", "ru": "Экосистема NPM, Внешние Пакеты и Аудит Безопасности", "en": "NPM Ecosystem, External Packages, and Supply Chain Security"},
        "type": {"uz": "DevOps Asos", "ru": "DevOps База", "en": "DevOps Foundation"},
        "skills": {"uz": "package.json, semantic versioning (^, ~), npm install/audit, Ta'minot zanjiri hujumlari (Supply Chain Attacks), ESLint", "ru": "package.json, версионирование, npm audit, атаки на цепочку поставок (Supply Chain), линтер ESLint", "en": "package.json management, SemVer dependency locking, npm audit, software supply chain security, ESLint"},
        "deliverable": {"uz": "Toza sozlangan, linting qoidalari qo'yilgan va zaifliklardan xoli Node.js loyihasi", "ru": "Настроенный проект Node.js с линтером и отсутствием уязвимостей в зависимостях", "en": "Hardened Node.js project environment with strict ESLint config and zero vulnerability audit report"},
        "tools": "npm CLI, npm audit, ESLint, Prettier"
    },
    16: {
        "title": {"uz": "Veb-Ilova Tezligi: Kesh, Assetlar va Lighthouse Auditi", "ru": "Скорость Веб-Приложений: Кэш, Ассеты и Аудит Lighthouse", "en": "Web Performance: Caching, Asset Optimization, and Lighthouse"},
        "type": {"uz": "Optimizatsiya Lab", "ru": "Оптимизация Лаб", "en": "Performance Lab"},
        "skills": {"uz": "Core Web Vitals (LCP, FID, CLS), Rasmlarni WebP/AVIF formatiga siqish, Gzip/Brotli siqilishi, Brauzer keshi (Cache-Control)", "ru": "Core Web Vitals, сжатие картинок в WebP, сжатие Gzip/Brotli, управление кэшем браузера", "en": "Core Web Vitals metrics, image optimization (WebP/AVIF), HTTP compression (Brotli), Cache-Control headers"},
        "deliverable": {"uz": "Google Lighthouse tekshiruvida barcha yo'nalishlarda 95+ ball to'plagan tezyurar veb-ilova", "ru": "Сверхбыстрое приложение, набравшее 95+ баллов во всех разделах Google Lighthouse", "en": "High-performance web app optimized to score 95+ on Google Lighthouse across all categories"},
        "tools": "Google Lighthouse, Sharp, Chrome Performance Panel"
    },
    17: {
        "title": {"uz": "2-Chorak Oraliq Nazorat: Interaktiv SPA va Real-Vaqt Ilova Sinovi", "ru": "Промежуточный Контроль 2-й Четверти: SPA и Real-Time Приложение", "en": "Quarter 2 Midterm Exam: Interactive SPA and Real-Time Engine"},
        "type": {"uz": "Oraliq Imtihon", "ru": "Промежуточный Экзамен", "en": "Midterm Examination"},
        "skills": {"uz": "Modulli arxitektura, WebSockets jonli sinxronizatsiya, Client routing va Form validatsiyasini birlashtirish", "ru": "Модульная архитектура, WebSockets синхронизация, роутинг и валидация форм в единой системе", "en": "Consolidation of SPA client routing, WebSockets live syncing, form validation, and state caching"},
        "deliverable": {"uz": "Jonli rejimda ishlovchi to'liq interaktiv dasturiy platforma (10 ballik mezon)", "ru": "Интерактивная программная платформа, работающая в режиме реального времени (10-балльная шкала)", "en": "Fully interactive SPA with live multi-user real-time synchronization (10-point rubric)"},
        "tools": "VS Code, Chrome DevTools, Postman"
    },
    18: {
        "title": {"uz": "2-Chorak Demo Day: Dinamik Full-Stack Interaktiv Veb-Ilovalar Ko'rgazmasi", "ru": "Demo Day 2-й Четверти: Выставка Динамических Full-Stack Приложений", "en": "Quarter 2 Demo Day: Dynamic Full-Stack Interactive Web Showcase"},
        "type": {"uz": "Demo Day / Ko'rgazma", "ru": "Demo Day / Выставка", "en": "Demo Day / Expo"},
        "skills": {"uz": "O'z mahsulotini namoyish etish, Foydalanuvchilarni ro'yxatdan o'tkazish, Jonli sinov, Peer feedback", "ru": "Демонстрация продукта, регистрация пользователей, живой тест, взаимный фидбек", "en": "Live user onboarding demo, stress-testing under audience usage, product critique defense"},
        "deliverable": {"uz": "Sinfdoshlar bilan o'ynaladigan/ishlatiladigan to'liq veb-mahsulot va 2-Chorak Sertifikati", "ru": "Готовый веб-продукт, протестированный одноклассниками, и сертификат 2-й четверти", "en": "Deployed production web product tested live by class peers, plus Quarter 2 Diploma"},
        "tools": "Cloud Host, Presentation Deck, Mobile Live Test"
    },
    19: {
        "title": {"uz": "Bulutli Xizmatlar (Cloud): Supabase, Vercel va Object Storage", "ru": "Облачные Сервисы (Cloud): Supabase, Vercel и Object Storage", "en": "Cloud Services: Supabase, Vercel, and Object Storage"},
        "type": {"uz": "Cloud Asos", "ru": "Cloud База", "en": "Cloud Foundation"},
        "skills": {"uz": "Bulut arxitekturasi, Cloudflare CDN, Supabase Storage da rasmlarni saqlash, Pre-signed URL lar, Muhit o'zgaruvchilari", "ru": "Архитектура облака, Cloudflare CDN, хранение картинок в Supabase Storage, переменные окружения", "en": "Cloud hosting primitives, CDN caching, Supabase S3-compatible Object Storage, secure upload URLs"},
        "deliverable": {"uz": "Foydalanuvchi rasmlarini bulutga yuklab, global CDN orqali uzatuvchi ilova", "ru": "Приложение с загрузкой файлов в облачное хранилище и раздачей через CDN", "en": "Cloud-native media upload service storing images in Supabase Storage and serving via CDN"},
        "tools": "Supabase Storage, Cloudflare, Vercel Environment"
    },
    20: {
        "title": {"uz": "AI API Integratsiyasi: Ilovaga Sun'iy Intellekt Miyasini Ulash", "ru": "Интеграция AI API: Подключение Интеллекта к Приложению", "en": "AI API Integration: Supercharging Apps with AI Models"},
        "type": {"uz": "AI Integratsiya", "ru": "AI Интеграция", "en": "AI Integration"},
        "skills": {"uz": "OpenAI / Claude REST API ga ulanish, Streaming javoblar, Matnni umumlashtirish, AI yordamida avtomatik kontent yaratish", "ru": "Подключение к OpenAI / Claude REST API, стриминг ответов, саммаризация, автогенерация контента", "en": "Consuming OpenAI/Claude REST APIs, token stream handling, text summarization, AI generative features"},
        "deliverable": {"uz": "Foydalanuvchi so'roviga ko'ra avtomatik maqola, rasm yoki kod generatsiya qiluvchi aqlli veb-xizmat", "ru": "Умный веб-сервис, генерирующий контент и ответы с помощью AI", "en": "Intelligent web feature generating contextual summaries and automated suggestions using LLM API"},
        "tools": "OpenAI SDK, Fetch API, ReadableStream"
    },
    21: {
        "title": {"uz": "Telegram Bot Muhandisligi: Webhooklar va Interaktiv Menyular", "ru": "Инженерия Telegram-Ботов: Вебхуки и Меню", "en": "Telegram Bot Engineering: Webhooks and Interactive Keyboards"},
        "type": {"uz": "Bot Muhandisligi", "ru": "Инженерия Ботов", "en": "Bot Engineering"},
        "skills": {"uz": "Telegram Bot API, Inline klaviaturalar, Webhook arxitekturasi, Foydalanuvchi sessiyasini xotirada saqlash, FSM bot holatlari", "ru": "Telegram Bot API, инлайн клавиатуры, вебхуки, хранение состояния сессии (FSM)", "en": "Telegram Bot API, inline keyboards, webhook callback handling, conversation state management (FSM)"},
        "deliverable": {"uz": "Veb-sayt bilan sinxron ishlovchi va xaridorlarga xizmat ko'rsatuvchi interaktiv Telegram bot", "ru": "Интерактивный Telegram-бот, синхронизированный с базой данных сайта", "en": "Interactive business Telegram bot synced in real-time with website DB and order queue"},
        "tools": "Node.js, Telegraf / Grammy, Telegram BotFather"
    },
    22: {
        "title": {"uz": "Asinxron Vazifalar, Cron Jobs va Xabarnomalar Tizimi", "ru": "Асинхронные Задачи, Cron Jobs и Система Уведомлений", "en": "Asynchronous Tasks, Cron Jobs, and Notification Queues"},
        "type": {"uz": "Backend Lab", "ru": "Бэкенд Лаб", "en": "Backend Lab"},
        "skills": {"uz": "Vaqtga bog'langan vazifalar (Cron), node-cron, Email jo'natish (Nodemailer), Telegram bildirishnomalari, Asinxron navbatlar", "ru": "Задачи по расписанию (Cron), отправка email (Nodemailer), уведомления в Telegram, очереди задач", "en": "Scheduled tasks (Cron jobs), node-cron scheduler, automated email alerts via SMTP, asynchronous task queues"},
        "deliverable": {"uz": "Har kuni ma'lum vaqtda avtomatik hisobot jo'natuvchi va eslatma beruvchi xizmat", "ru": "Фоновый сервис, ежедневно отправляющий отчеты и напоминания по расписанию", "en": "Automated background cron service dispatching scheduled analytical reports and reminders"},
        "tools": "node-cron, Nodemailer, Resend API, Telegram"
    },
    23: {
        "title": {"uz": "Mikroxizmatlar Arxitekturasi va API Gateway", "ru": "Микросервисная Архитектура и API Gateway", "en": "Microservices Architecture and API Gateway"},
        "type": {"uz": "Tizimli Dizayn", "ru": "Системный Дизайн", "en": "System Design"},
        "skills": {"uz": "Monolit vs Mikroxizmatlar, Xizmatlararo HTTP aloqa, API Gateway orqali so'rovlarni marshrutlash, Mustaqil deploy", "ru": "Монолит vs Микросервисы, межсервисное взаимодействие, маршрутизация через API Gateway", "en": "Monolithic vs Microservices breakdown, service-to-service communication, API Gateway reverse routing"},
        "deliverable": {"uz": "Autentifikatsiya, mahsulotlar va xabarnomalar uchun alohida mikroxizmatlardan iborat arxitektura", "ru": "Архитектура из отдельных микросервисов для авторизации, товаров и уведомлений", "en": "Multi-service architecture decoupling authentication, data catalog, and notifications via Gateway"},
        "tools": "Docker Compose, Express Gateway, Node.js"
    },
    24: {
        "title": {"uz": "Serverless Funksiyalar va Cloudflare Workers", "ru": "Serverless Функции и Cloudflare Workers", "en": "Serverless Functions and Cloudflare Workers"},
        "type": {"uz": "Cloud Muhandislik", "ru": "Cloud Инженерия", "en": "Cloud Engineering"},
        "skills": {"uz": "Serverless hisoblash, Edge runtime, Cloudflare Workers va Vercel Serverless Functions, Sovuq start (Cold start) tahlili", "ru": "Бессерверные вычисления, Edge runtime, Cloudflare Workers, анализ холодного старта (Cold start)", "en": "Serverless execution models, Edge computing, Cloudflare Workers, zero cold-start micro-endpoints"},
        "deliverable": {"uz": "Butun dunyo bo'ylab 50ms dan kam kechikish bilan javob beruvchi serverless Edge API", "ru": "Serverless Edge API с временем отклика менее 50 мс по всему миру", "en": "Sub-50ms latency Serverless Edge function deployed across global Cloudflare edge nodes"},
        "tools": "Cloudflare Wrangler, Vercel Serverless, JavaScript"
    },
    25: {
        "title": {"uz": "Dasturiy Telemetriya, Logging va Sentry Monitori", "ru": "Телеметрия Приложений, Логирование и Мониторинг Sentry", "en": "Application Telemetry, Logging, and Sentry Monitoring"},
        "type": {"uz": "Monitoring Lab", "ru": "Мониторинг Лаб", "en": "Monitoring Lab"},
        "skills": {"uz": "Log turlari (info, warn, error), Strukturaviy Winston loglari, Sentry orqali koddagi xatolarni real vaqtda ushlash", "ru": "Типы логов, структурированные логи Winston, перехват ошибок в реальном времени через Sentry", "en": "Structured JSON logging with Winston, centralized error telemetry with Sentry, alert triggers"},
        "deliverable": {"uz": "Saytda xatolik yuz berishi bilanoq dasturchining Telegramiga signal beruvchi telemetriya tizimi", "ru": "Система телеметрии, мгновенно присылающая отчет об ошибке в Telegram при сбое", "en": "Telemetry pipeline capturing uncaught server exceptions and alerting engineers in real time"},
        "tools": "Winston, Sentry, Telegram Webhook"
    },
    26: {
        "title": {"uz": "3-Chorak Oraliq Nazorat: Bulutli Mikroxizmatlar va AI Integratsiyasi", "ru": "Промежуточный Контроль 3-й Четверти: Облачные Микросервисы и ИИ", "en": "Quarter 3 Midterm Exam: Cloud Microservices and AI Integration"},
        "type": {"uz": "Oraliq Imtihon", "ru": "Промежуточный Экзамен", "en": "Midterm Examination"},
        "skills": {"uz": "Serverless, Telegram bot va AI API ulanmalarini yagona ekotizimga birlashtirish, Xavfsizlik auditi", "ru": "Объединение Serverless, Telegram-бота и AI API в единую экосистему, аудит безопасности", "en": "Integrated evaluation combining Serverless functions, Telegram bot, and AI APIs into a reliable app"},
        "deliverable": {"uz": "Berilgan topshiriq bo'yicha to'liq ishga tushirilgan bulutli AI tizimi (10 ballik mezon)", "ru": "Работающая облачная система с AI по экзаменационному заданию (10-балльная шкала)", "en": "Operational cloud AI micro-platform evaluated under production failure scenarios (10-point rubric)"},
        "tools": "Cloudflare Workers, Supabase, Telegram, OpenAI"
    },
    27: {
        "title": {"uz": "3-Chorak Demo Day: Sun'iy Intellektli Cloud Ilovalar Ko'rgazmasi", "ru": "Demo Day 3-й Четверти: Выставка Облачных AI-Приложений", "en": "Quarter 3 Demo Day: Cloud AI Applications Showcase"},
        "type": {"uz": "Demo Day / Ko'rgazma", "ru": "Demo Day / Выставка", "en": "Demo Day / Expo"},
        "skills": {"uz": "Loyiha arxitekturasini himoya qilish, Foydalanuvchilar oqimini ko'rsatish, Kiber-xavfsizlik kafolati", "ru": "Защита архитектуры, демонстрация пользовательского потока, гарантии кибербезопасности", "en": "Architecture defense, load capacity walkthrough, cyber-hygiene audit presentation"},
        "deliverable": {"uz": "Haqiqiy foydalanuvchilar ishlatayotgan jonli Bulutli AI xizmati va 3-Chorak Sertifikati", "ru": "Живой облачный AI-сервис с реальными пользователями и сертификат 3-й четверти", "en": "Live cloud AI platform utilized by actual target users and Quarter 3 Mastery Diploma"},
        "tools": "Live Cloud Infrastructure, GitHub Docs, Video Demo"
    },
    28: {
        "title": {"uz": "Agile va Scrum Asoslari: Sprint, Backlog va Vazifalar Taqsimoti", "ru": "Основы Agile и Scrum: Спринты, Бэклог и Задачи", "en": "Agile and Scrum Foundations: Sprints, Backlog, and Kanban"},
        "type": {"uz": "Jamoaviy Boshqaruv", "ru": "Управление Командой", "en": "Team Management"},
        "skills": {"uz": "Agile manifesti, Scrum rollari (Product Owner, Scrum Master, Developer), GitHub Projects Kanban doskasi, User Stories", "ru": "Agile манифест, роли в Scrum, Kanban доска GitHub Projects, User Stories", "en": "Agile manifesto, Scrum roles, GitHub Projects Kanban boards, User Stories, and story point sizing"},
        "deliverable": {"uz": "Loyiha bo'yicha tayyorlangan to'liq Sprint Backlog va vazifalar xaritasi", "ru": "Готовый Sprint Backlog и карта задач проекта на GitHub Projects", "en": "Configured GitHub Projects Kanban board with user stories, acceptance criteria, and milestones"},
        "tools": "GitHub Projects, Notion Agile Board, Markdown"
    },
    29: {
        "title": {"uz": "Loyiha MVP Si: Minimal Foydali Mahsulot Arxitekturasi", "ru": "MVP Проекта: Архитектура Минимального Продукта", "en": "Project MVP: Minimal Viable Product Architecture"},
        "type": {"uz": "MVP Muhandislik", "ru": "MVP Инженерия", "en": "MVP Engineering"},
        "skills": {"uz": "MVP tushunchasi, Ortiqcha funksiyalarni olib tashlash, Asosiy qiymat taklifi (Core Value), Baza sxemasi", "ru": "Концепция MVP, отсечение лишнего, ключевая ценность продукта, схема базы данных", "en": "MVP scoping, prioritizing core value proposition, database schema scaffolding, and route skeleton"},
        "deliverable": {"uz": "Faqat eng muhim muammoni yechuvchi va ishlaydigan birinchi MVP versiyasi", "ru": "Первая рабочая версия MVP, решающая главную задачу продукта", "en": "Operational Minimal Viable Product (MVP) core solving the primary user workflow"},
        "tools": "VS Code, Git Branching, SQLite / Supabase"
    },
    30: {
        "title": {"uz": "Backend va API Shinalari: To'liq CRUD va Avtorizatsiya", "ru": "Бэкенд и Шина API: Полный CRUD и Авторизация", "en": "Backend and API Pipelines: Full CRUD and Authorization"},
        "type": {"uz": "Backend Yadro", "ru": "Ядро Бэкенда", "en": "Backend Core"},
        "skills": {"uz": "Barcha asosiy CRUD marshrutlari, JWT token tekshiruvi, Rolga asoslangan kirish (Admin vs User), Xatolarni markaziy ushlash", "ru": "Все основные CRUD маршруты, проверка JWT, доступ по ролям (RBAC), центральный обработчик ошибок", "en": "Complete REST CRUD implementation, JWT authentication guard, RBAC middleware, unified error handling"},
        "deliverable": {"uz": "Loyihaning to'liq himoyalangan va hujjatlashtirilgan REST API yadrosi", "ru": "Полностью защищенное и задокументированное ядро REST API проекта", "en": "Production-hardened REST API core with automated OpenAPI/Swagger documentation"},
        "tools": "Express.js, JWT, Bcrypt, SQLite / PostgreSQL"
    },
    31: {
        "title": {"uz": "Interaktiv UI, Foydalanuvchi Tajribasi (UX) va Toast Xabarlar", "ru": "Интерактивный UI, Пользовательский Опыт (UX) и Уведомления", "en": "Interactive UI, UX Polish, and Feedback Notifications"},
        "type": {"uz": "Frontend Sifat", "ru": "Качество Фронтенда", "en": "Frontend Polish"},
        "skills": {"uz": "UX tamoyillari, Yuklanish holatlari (Spinners, Skeletons), Qulay xatolik bildirishnomalari (Toast notifications), Modal dialoglar", "ru": "Принципы UX, состояния загрузки, всплывающие уведомления (Toast), модальные диалоги", "en": "UX design principles, responsive spinners, accessible toast notifications, optimistic UI updates"},
        "deliverable": {"uz": "Foydalanuvchi har bir harakatiga chiroyli javob qaytaruvchi mukammal interfeys", "ru": "Отзывчивый интерфейс с красивой обратной связью на каждое действие", "en": "Silky-smooth user interface with comprehensive validation badges and notification toasts"},
        "tools": "Tailwind CSS, SweetAlert2 / Toastify, Lucide Icons"
    },
    32: {
        "title": {"uz": "Integratsiya, Jamoaviy Merge va CI/CD Konveyeri", "ru": "Интеграция, Командный Merge и Конвейер CI/CD", "en": "Integration, Team Merge, and CI/CD Automation"},
        "type": {"uz": "DevOps Konveyer", "ru": "DevOps Конвейер", "en": "DevOps Pipeline"},
        "skills": {"uz": "Git jamoaviy branchlarini birlashtirish, Merge konfliktlarini hal qilish, GitHub Actions avtomatik testlari va deploy", "ru": "Слияние командных веток Git, разрешение конфликтов, автотесты и деплой через GitHub Actions", "en": "Branch merging protocols, conflict resolution in pull requests, automated GitHub Actions CI/CD workflows"},
        "deliverable": {"uz": "Har bir commit avtomatik tekshirilib internetga chiqadigan tayyor konveyer", "ru": "Готовый конвейер, где каждый коммит автоматически тестируется и деплоится", "en": "Automated deployment pipeline running linter and unit tests before pushing to live host"},
        "tools": "Git, GitHub Actions, Vercel / Render"
    },
    33: {
        "title": {"uz": "Kiber-Xavfsizlik Sinovi: Saytni Zaifliklarga Tekshirish", "ru": "Тест Кибербезопасности: Проверка Сайта на Уязвимости", "en": "CyberSecurity Audit: Penetration Testing Web Assets"},
        "type": {"uz": "Xavfsizlik Auditi", "ru": "Аудит Безопасности", "en": "Security Audit"},
        "skills": {"uz": "OWASP Top 10 tekshiruvi, SQL Injection va XSS hujumlarini amalda sinab ko'rish, Parollarni mustahkamlash, CORS tekshiruvi", "ru": "Проверка OWASP Top 10, практический тест на SQLi и XSS, проверка политик паролей и CORS", "en": "OWASP Top 10 security verification, testing injection loopholes, CORS restrictions, header verification"},
        "deliverable": {"uz": "Topilgan barcha bo'shliqlari yopilgan va kiber-xavfsizlik hisoboti tuzilgan ilova", "ru": "Приложение с устраненными уязвимостями и отчет по безопасности", "en": "Remediated codebase with zero known high vulnerabilities and formal security checklist"},
        "tools": "OWASP ZAP, Chrome DevTools, Security Headers"
    },
    34: {
        "title": {"uz": "Foydalanuvchi Sinovi (Beta Testing) va Bug-Bounty Musobaqasi", "ru": "Бета-Тестирование Пользователями и Конкурс Bug-Bounty", "en": "User Beta Testing and Peer Bug-Bounty Challenge"},
        "type": {"uz": "QA Musobaqa", "ru": "QA Соревнование", "en": "QA Challenge"},
        "skills": {"uz": "Sinfdoshlar o'rtasida o'zaro ilovalarni buzib ko'rish (Bug-bounty), Xatolarni qayd etish (Issue tracking), Tezkor tuzatishlar", "ru": "Взаимное тестирование и поиск багов (Bug-bounty), фиксация ошибок в GitHub Issues, быстрые фиксы", "en": "Peer bug-bounty challenge, logging reproducible bugs on GitHub Issues, rapid hotfixing cycles"},
        "deliverable": {"uz": "Sinfdoshlar tomonidan topilgan kamchiliklari bartaraf etilgan barqaror v1.0 relizi", "ru": "Стабильный релиз v1.0 с исправлением всех найденных багов", "en": "Stabilized v1.0 production release with closed issues and verified release changelog"},
        "tools": "GitHub Issues, Bug Tracker, Chrome DevTools"
    },
    35: {
        "title": {"uz": "Loyiha Portfoliosi: GitHub README, Hujjatlar va Demo", "ru": "Портфолио Проекта: README на GitHub, Документация и Демо", "en": "Project Portfolio: GitHub README, Docs, and Live Demo"},
        "type": {"uz": "Portfel Tayyorlash", "ru": "Подготовка Портфолио", "en": "Portfolio Building"},
        "skills": {"uz": "Professional README yozish, Skrinshotlar, Jonli sayt havolasi, O'rnatish yo'riqnomasi, 2 daqiqalik video lavha", "ru": "Оформление профессионального README, скриншоты, живая ссылка, инструкция по установке, 2-минутное видео", "en": "Authoring professional GitHub READMEs, architecture badges, installation guides, video demo walkthrough"},
        "deliverable": {"uz": "Har qanday xalqaro darajadagi IT suhbatida faxr bilan ko'rsatsa bo'ladigan portfolio sahifasi", "ru": "Страница портфолио, которую можно уверенно показать на любом IT-собеседовании", "en": "Polished open-source GitHub showcase repository ready for tech interviews and university applications"},
        "tools": "Markdown, Screen Recorder, GitHub Pages"
    },
    36: {
        "title": {"uz": "Katta Demo Day: Yillik Full-Stack Loyiha Himoyasi va Bitiruv", "ru": "Большой Demo Day: Защита Годового Full-Stack Проекта и Выпуск", "en": "Grand Demo Day: Annual Full-Stack Project Defense and Graduation"},
        "type": {"uz": "Grand Demo Day", "ru": "Grand Demo Day", "en": "Grand Demo Day"},
        "skills": {"uz": "Maktab jamoasi oldida o'z mahsulotini jonli ishlatib ko'rsatish, Texnik savollarga javob berish, Diplom taqdimoti", "ru": "Живая демонстрация работающего продукта перед школой, ответы на технические вопросы, вручение дипломов", "en": "Public demonstration of live production web systems, technical justification, graduation diploma ceremony"},
        "deliverable": {"uz": "Muvaffaqiyatli himoya qilingan to'liq Full-Stack veb-mahsulot va Target IT Oltin Diplomi", "ru": "Успешно защищенный Full-Stack веб-продукт и золотой диплом Target IT", "en": "Successfully defended production full-stack application and Target IT Junior Engineer Honors Diploma"},
        "tools": "Live Production App, Presentation Rig, Certificate"
    }
}
