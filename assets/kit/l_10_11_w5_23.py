# -*- coding: utf-8 -*-
"""10-11-sinf · 5-hafta · 23-dars — API Xavfsizligi va Rate Limiting: Token Bucket, DDoS va HMAC."""

import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from build import (Lesson, slide, title_slide, box, code, el, i18n,
                   sheet_header, mission, table, sheet_box, rubric, writelines, sign_box)

D = "classes/10-11-sinf/5-hafta/23-dars-api-xavfsizligi-va-rate-limiting"

TITLES = {
    "uz": "23-dars: API Xavfsizligi va Rate Limiting — Token Bucket, DDoS va HMAC",
    "ru": "Урок 23: Безопасность API и Rate Limiting — Token Bucket, DDoS и HMAC",
    "en": "Lesson 23: Enterprise API Security & Rate Limiting — Token Bucket, DDoS & HMAC",
}
SHEET_TITLES = {k: v + (" — Ish Varaqasi" if k == "uz" else
                        " — Рабочий Лист" if k == "ru" else " — Worksheet")
                for k, v in TITLES.items()}

S = []

# 1. Title Slide
S.append(title_slide(
    ph=("Kirish", "Введение", "Intro"), time="0–3",
    eyebrow=("CyberSecurity · 23-dars · 10–11-sinf (Enterprise API Defense)",
             "CyberSecurity · Урок 23 · 10–11 класс (Enterprise API Defense)",
             "CyberSecurity · Lesson 23 · Grades 10–11 (Enterprise API Defense)"),
    h1=("API Xavfsizligi va Rate Limiting: Token Bucket, DDoS va HMAC",
        "Безопасность API и Rate Limiting: Token Bucket, DDoS и HMAC",
        "Enterprise API Security & Rate Limiting: Token Bucket, DDoS & HMAC"),
    lede=("Zamonaviy veb va mobil ilovalar to'liq <b>REST, GraphQL va gRPC API</b>lar orqali ishlaydi. "
          "Har bir tugma, avtorizatsiya va to'lov tranzaksiyasi ortida server API endpointi yotadi. "
          "Agar API to'g'ri himoyalanmasa, bitta buzg'unchi script soniyasiga 100,000 ta so'rov bilan serverni yiqitishi (DDoS), "
          "foydalanuvchilarning barcha ma'lumotlarini qirib olishi (Scraping) yoki so'rovlarni soxtalashtirishi mumkin. "
          "Bugungi darsda <b>OWASP API Top 10</b> tahdidlari, <b>Token Bucket / Leaky Bucket</b> algoritmlari, "
          "Redis orqali taqsimlangan Rate Limiting va bank darajasidagi <b>HMAC-SHA256</b> so'rov imzolashni amalda o'rganamiz.",
          "Современная разработка строится на микросервисных <b>REST, GraphQL и gRPC API</b>. "
          "За каждой кнопкой мобильного банкинга или веб-сервиса стоит эндпоинт. "
          "Без эшелонированной защиты вредоносный скрипт может положить сервер миллионами запросов (DDoS), "
          "выкачать приватные профили (Scraping) или подделать платёжный запрос (Replay Attack). "
          "Сегодня мы изучим <b>OWASP API Top 10</b>, математику алгоритмов <b>Token Bucket</b>, "
          "распределённый Rate Limiting в Redis и криптографическую подпись запросов <b>HMAC-SHA256</b>.",
          "Modern web and cloud-native backends rely entirely on <b>REST, GraphQL, and gRPC APIs</b>. "
          "Every frontend interaction routes directly into mission-critical API endpoints. "
          "Without multi-tiered defense, an adversary can exhaust compute resources via Layer 7 DDoS, "
          "harvest entire customer databases via automated scraping, or execute catastrophic Replay Attacks. "
          "Today we explore <b>OWASP API Security Top 10</b>, <b>Token Bucket & Leaky Bucket</b> rate limiting algorithms, "
          "distributed atomic Redis throttling, and enterprise-grade <b>HMAC-SHA256</b> cryptographic request signing."),
    meta=[("<b>Fan:</b> Kiberxavfsizlik · API Infratuzilma Himoyasi",
           "<b>Предмет:</b> Кибербезопасность · Защита API Инфраструктуры",
           "<b>Subject:</b> CyberSecurity · Enterprise API Defense"),
          ("<b>Kohorta:</b> 10-11-sinf Kiber-Muhandis",
           "<b>Когорта:</b> 10-11 класс Инженер Безопасности",
           "<b>Cohort:</b> Grade 10-11 Security Engineer"),
          ("<b>Hafta:</b> 5 (3-soat)", "<b>Неделя:</b> 5 (3-й час)", "<b>Week:</b> 5 (Hour 3)")],
))

# 2. OWASP API Security Top 10
S.append(slide(
    ph=("Standartlar", "Стандарты", "Standards"), time="3–7",
    eyebrow=("OWASP API Top 10 (2023 Standarti)", "OWASP API Top 10 (Стандарт 2023)", "OWASP API Top 10 (2023 Standard)"),
    title=("Nega Standart Veb Himoyasi API Uchun Yetarli Emas?",
           "Почему Стандартного Фаервола Недостаточно для API?",
           "Why Traditional Web Defense Fails at API Protection"),
    body=table(
        headers=[("Zaiflik (OWASP)", "Уязвимость (OWASP)", "OWASP API Vulnerability"),
                 ("Hujum Mexanizmi", "Механизм Атаки", "Attack Vector"),
                 ("Real Oqibati", "Реальные Последствия", "Impact"),
                 ("Muhandislik Himoyasi", "Инженерная Защита", "Engineering Mitigation")],
        rows=[
            [("<b>API1: BOLA / IDOR</b><br>(Broken Object Level Auth)", "<b>API1: BOLA / IDOR</b>", "<b>API1: BOLA / IDOR</b>"),
             ("Foydalanuvchi <code>/api/orders/401</code> o'rniga <code>/api/orders/402</code> deb boshqa odam hisobini so'raydi.",
              "Подмена ID в запросе для чтения чужих объектов без проверки владения.",
              "Manipulating resource IDs to access arbitrary tenant records."),
             ("Begona mijozlarning barcha shaxsiy va moliyaviy ma'lumotlari sizib chiqadi.",
              "Полная утечка конфиденциальных данных чужих клиентов.",
              "Catastrophic horizontal authorization privilege escalation."),
             ("Har bir so'rovda obyekt egasi sessiya tokeni egasi bilan solishtiriladi.",
              "Валидация владельца записи: <code>order.user_id === req.user.id</code>.",
              "Strict object-level authorization middleware on each database query.")],
            [("<b>API4: Unrestricted Resource</b><br>(Resurs chegarasi yo'qligi)", "<b>API4: Unrestricted Consumption</b>", "<b>API4: Unrestricted Consumption</b>"),
             ("Cheklovsiz so'rovlar yuborish, millionlab sahifalarni paginatsiyasiz tortish.",
              "Массовые параллельные запросы без лимитов пагинации и частоты.",
              "High-frequency queries and unbounded pagination payloads."),
             ("Server protsessori 100% ga to'lib, xotira tugaydi va xizmat to'xtaydi (DoS).",
              "Отказ в обслуживании, истощение CPU/RAM, огромные счета за облако.",
              "CPU starvation, memory exhaustion, and server availability crash."),
             ("<b>Rate Limiting (Token Bucket)</b> va qat'iy <code>limit=50</code> paginatsiyasi.",
              "Движок <b>Rate Limiting</b> и жесткие лимиты на размер выборки.",
              "Enforcing distributed rate limiting and hard limits on query pagination.")],
            [("<b>API3: BOPLA / Mass Assign</b><br>(Property Level Auth)", "<b>API3: BOPLA / Mass Assignment</b>", "<b>API3: BOPLA / Mass Assignment</b>"),
             ("JSON tanasida qo'shimcha parametrlar: <code>{\"role\": \"admin\", \"balance\": 999999}</code> yuborish.",
              "Внедрение недопустимых полей в тело JSON (например, <code>isAdmin: true</code>).",
              "Injecting internal attributes into deserialized JSON payloads."),
             ("Oddiy foydalanuvchi o'zini bir soniyada tizim adminiga aylantiradi.",
              "Несанкционированное повышение привилегий до суперпользователя.",
              "Privilege escalation to administrator or arbitrary balance alteration."),
             ("DTO (Data Transfer Object) oq ro'yxati (Whitelist validation: Zod, Joi).",
              "Строгая валидация входящих DTO по белым спискам разрешённых полей.",
              "Strict schema whitelisting (DTO validation discarding unexpected fields).")]
        ]
    )
))

# 3. DDoS: Layer 3/4 vs Layer 7 Attacks
S.append(slide(
    ph=("Tahdid Tahlili", "Анализ Угроз", "Threat Vectors"), time="7–11",
    eyebrow=("Infratuzilma darajalari", "Сетевые уровни OSI", "OSI Layer Attacks"),
    title=("L3/L4 vs L7 DDoS: Nega HTTP Flood Xavfliroq?",
           "L3/L4 против L7 DDoS: Почему HTTP-Флуд Опаснее?",
           "L3/L4 vs L7 DDoS: Why Application Layer Attacks are Deadlier"),
    body='<div class="cols">\n'
         + box("navy", ("Tarmoq Qatlami (Layer 3 / 4 DDoS)", "Сетевой Уровень (L3/L4 DDoS)", "Network Layer (L3/L4 DDoS)"),
               items=[
                   ("<b>Hujum turi:</b> SYN Flood, UDP Amplification, ICMP smurf hujumlari.",
                    "<b>Типы атак:</b> SYN Flood, UDP Amplification, переполнение полосы.",
                    "<b>Attack Types:</b> SYN Floods, UDP reflection/amplification, line saturation."),
                   ("<b>Maqsad:</b> Serverning tarmoq kanalini (masalan 10 Gbps) yoki marshrutizator xotirasini tiqiltirish.",
                    "<b>Цель:</b> Забить канал провайдера (Bandwidth) мусорным трафиком.",
                    "<b>Objective:</b> Saturate physical network bandwidth and firewall connection tables."),
                   ("<b>Himoya usuli:</b> Anycast DNS, BGP Blackholing, Cloudflare Magic Transit tarmoq filtrlari.",
                    "<b>Защита:</b> Фильтрация на уровне магистральных операторов, Anycast, scrubbing centers.",
                    "<b>Mitigation:</b> Anycast routing, automated BGP Flowspec scrubbing, Cloudflare Magic Transit.")
               ])
         + box("red", ("Ilova Qatlami (Layer 7 API DDoS)", "Уровень Приложений (L7 API DDoS)", "Application Layer (L7 API DDoS)"),
               items=[
                   ("<b>Hujum turi:</b> HTTP GET/POST Flood, Slowloris, Murakkab DB Qidiruvlari, ReDoS.",
                    "<b>Типы атак:</b> HTTP Flood, тяжелые поисковые запросы к БД, ReDoS.",
                    "<b>Attack Types:</b> HTTP GET/POST Floods, heavy SQL full-text queries, ReDoS regex bombs."),
                   ("<b>Xavfli jihati:</b> Har bir so'rov <b>qonuniy va to'g'ri</b> ko'rinadi (TLS o'rnatilgan, HTTP 200). L3/L4 filtrlar buni o'tkazib yuboradi!",
                    "<b>Коварство:</b> Запросы легитимны с точки зрения TCP/TLS. Сетевой фаервол не видит аномалий.",
                    "<b>Stealth factor:</b> Every packet is valid TCP/TLS with normal headers. Network firewalls pass them blindly!"),
                   ("<b>Oqibati:</b> 10,000 ta og'ir SQL qidiruv so'rovi butun ma'lumotlar bazasini 10 soniyada to'xtatadi.",
                    "<b>Результат:</b> Всего 10 000 сложных запросов кладут Postgres/MySQL на лопатки.",
                    "<b>Result:</b> A mere 10,000 requests paralyze database connection pools and crash microservices.")
               ])
         + '</div>'
))

# 4. Mathematical Rate Limiting Algorithms
S.append(slide(
    ph=("Algoritmlar", "Алгоритмы", "Algorithms"), time="11–15",
    eyebrow=("Matematik modellar", "Математические модели", "Mathematical Models"),
    title=("Rate Limiting Algoritmlari: Qaysi Biri Qachon Qo'llanadi?",
           "Алгоритмы Ограничения Запросов: Архитектурный Выбор",
           "Rate Limiting Algorithms: Architectural Trade-offs"),
    body=table(
        headers=[("Algoritm", "Алгоритм", "Algorithm"),
                 ("Ishlash Mexanizmi", "Принцип Работы", "Mechanism"),
                 ("Kamchiligi (Tuzog'i)", "Недостаток / Уязвимость", "Downside / Edge Case"),
                 ("Eng Yaxshi Foydalanish", "Лучшее Применение", "Optimal Use Case")],
        rows=[
            [("<b>Fixed Window Counter</b>", "<b>Fixed Window Counter</b>", "<b>Fixed Window Counter</b>"),
             ("Har daqiqada hisoblagich 0 dan boshlanadi. Masalan: 10:00 da 100 ta so'rov ruxsat etiladi.",
              "Счётчик сбрасывается в фиксированное время (например, в начале каждой минуты).",
              "Resets request count at fixed interval boundaries (e.g. at 00 seconds)."),
             ("<b>Chegara effekti (Burst):</b> 10:00:59 da 100 ta va 10:01:01 da yana 100 ta — 2 soniyada 200 ta so'rov o'tadi!",
              "Всплеск на границе окна: в 2 секунды может пройти удвоенный лимит (2x burst).",
              "Boundary spike: 2x allowed volume can hit the server across window frontiers."),
             ("Oddiy, resurs kam talab qiladigan ichki keshlar.",
              "Простые внутренние сервисы с минимальными накладными расходами.",
              "Low-overhead internal utilities and non-critical cron jobs.")],
            [("<b>Sliding Window Log</b>", "<b>Sliding Window Log</b>", "<b>Sliding Window Log</b>"),
             ("Har bir so'rovning vaqti (timestamp) xotirada (Redis ZSET) saqlanadi va oxirgi 60 soniya hisoblanadi.",
              "Хранение точных таймстемпов каждого запроса в сортированном множестве Redis.",
              "Maintains timestamps of every request in sorted sets, discarding older entries."),
             ("Xotira sarfi yuqori: har bir so'rov uchun alohida yozuv (RAM O(N)).",
              "Высокое потребление памяти при миллионах запросов.",
              "High RAM footprint proportional to incoming request volume (O(N))."),
             ("Yuqori aniqlik talab qilinadigan moliyaviy tranzaksiyalar.",
              "Высокоточные финансовые API с жестким контролем.",
              "High-stakes financial transaction endpoints.")],
            [("<b>Token Bucket (Sanoat standarti)</b>", "<b>Token Bucket (Промышленный)</b>", "<b>Token Bucket (Industry Standard)</b>"),
             ("Chelakka doimiy tezlikda (r) tokenlar tushadi. Har bir so'rov 1 ta tokenni oladi. Token tugasa — 429 xato.",
              "В ведро с фиксированной емкостью непрерывно капают токены. Запрос забирает токен.",
              "Bucket has fixed capacity B and refills at rate R. Requests consume tokens or get HTTP 429."),
             ("Qisqa muddatli tezlik portlashiga (Burst) ruxsat beradi, ammo uzoq muddatli o'rtacha tezlikni ushlaydi.",
              "Позволяет кратковременные легитимные всплески, сглаживая общий трафик.",
              "Allows controlled burst spikes while guaranteeing strict long-term rate limits."),
             ("AWS, Cloudflare, Stripe va Stripe API shlyuzlarining asosi.",
              "Публичные API платформ: Stripe, AWS, GitHub, Cloudflare.",
              "Enterprise API gateways: AWS API Gateway, Stripe, GitHub, Cloudflare.")]
        ]
    )
))

# 5. Distributed Rate Limiting & Redis Lua
S.append(slide(
    ph=("Taqsimlangan Tizimlar", "Распределенные Системы", "Distributed Architecture"), time="15–18",
    eyebrow=("Klaster infratuzilmasi", "Кластерная инфраструктура", "Cluster Infrastructure"),
    title=("Nega Lokal Xotira Kifoya Qilmaydi? Redis & Atomar Lua",
           "Почему Локальной Памяти Мало? Redis и Атомарные Lua Скрипты",
           "Why Local Memory Fails: Distributed Redis & Atomic Lua Scripts"),
    body='<div class="cols">\n'
         + box("red", ("Lokal Xotira Tuzog'i (Memory Leak & Desync)", "Ловушка Локальной Памяти (In-Memory Fail)", "The In-Memory Cluster Flaw"),
               items=[
                   ("Kompaniyada <b>4 ta Node.js server nusxasi</b> (Kubernetes Pods) ishlaydi.",
                    "Микросервис масштабирован на 4 инстанса за балансировщиком Load Balancer.",
                    "Microservice runs across 4 horizontal Kubernetes pods behind a Load Balancer."),
                   ("Agar rate limiter xotirada (RAM) saqlansa, har bir pod o'zining hisoblagichiga ega bo'ladi.",
                    "Если лимитер хранит счётчик в памяти процесса, у каждого пода свой счётчик.",
                    "If rate limiting is process-local, each node maintains its own isolated counter."),
                   ("Hujumchi 100 ta o'rniga <b>400 ta so'rov</b> yuborishga muvaffaq bo'ladi (Round-Robin taqsimoti tufayli)!",
                    "Атакующий может отправить 400 запросов вместо 100, распределяя их по подам!",
                    "An attacker easily bypasses thresholds by cycling requests across pods (4x amplification).")
               ])
         + box("green", ("Redis + Lua: Poyga Xatosi (Race Condition) Himoyasi", "Redis + Lua: Защита от Race Condition", "Redis + Lua: Atomic Concurrency Defense"),
               items=[
                   ("Barcha serverlar yagona <b>Redis In-Memory Data Store</b> ga ulanadi.",
                    "Все поды обращаются к единому централизованному Redis кластеру.",
                    "All microservice pods query a single central Redis in-memory cluster."),
                   ("<b>Poyga xatosi (Race Condition):</b> Ikki server bir vaqtda <code>GET</code> qilsa va keyin <code>DECR</code> qilsa, hisob adashadi.",
                    "Если выполнять GET и DECR раздельно, параллельные потоки нарушат баланс токенов.",
                    "Separating GET and DECR creates time-of-check to time-of-use (TOCTOU) race flaws."),
                   ("<b>Yechim — Lua Skripti:</b> Redis bir ipli (single-threaded) bo'lgani uchun, unga yuborilgan Lua skripti <b>100% atomar (bo'linmas)</b> bajariladi!",
                    "<b>Решение — Lua:</b> Скрипт исполняется атомарно внутри движка Redis без блокировок.",
                    "<b>Solution — Lua Script:</b> Redis executes embedded Lua scripts atomically without thread lock overhead.")
               ])
         + '</div>'
))

# 6. Cryptographic Integrity: HMAC-SHA256 API Request Signing
S.append(slide(
    ph=("Kriptografik Himoya", "Криптозащита", "Cryptographic Defense"), time="18–22",
    eyebrow=("Bank darajasidagi yaxlitlik", "Банковский уровень защиты", "Bank-Grade Integrity"),
    title=("HMAC-SHA256: So'rovlarni Imzolash va Replay Hujumlariga Barham Berish",
           "HMAC-SHA256: Подпись Запросов и Защита от Replay-Атак",
           "HMAC-SHA256: Request Signing & Total Replay Attack Mitigation"),
    body='<div class="cols">\n'
         + box("blue", ("Oddiy API Kalitlarining Kamchiligi", "Уязвимость Обычных API Keys", "The API Key Interception Flaw"),
               items=[
                   ("Ko'p dasturchilar shunchaki <code>Authorization: Bearer my-secret-api-key</code> yuborishadi.",
                    "Стандартный подход: передача статичного токена в заголовке Authorization.",
                    "Standard practice: sending static API tokens via HTTP headers."),
                   ("Agar server proksisi, log tizimi yoki xodimlardan biri kalitni ko'rib qolsa — kalit butunlay o'g'irlanadi.",
                    "При компрометации логов или MITM-прокси ключ перехватывается навсегда.",
                    "Logs, proxies, or internal leaks permanently compromise the credentials."),
                   ("Hujumchi so'rov parametrlarini o'zgartirib, pul o'tkazmasini o'z hamyoniga yo'naltirishi mumkin.",
                    "Злоумышленник может модифицировать тело запроса и отправить его повторно.",
                    "Adversaries can tamper with payload parameters (e.g. destination account).")
               ])
         + box("purple", ("HMAC-SHA256 va Replay Himoyasi Mexanizmi", "Механика HMAC-SHA256 и Replay Defense", "HMAC Signing & Replay Prevention Architecture"),
               items=[
                   ("1. <b>Kanonik Matn:</b> <code>Method + Path + Timestamp + Nonce + Body</code> birlashtiriladi.",
                    "1. <b>Каноническая строка:</b> Метод + URL + Таймстемп + Nonce + Хэш тела JSON.",
                    "1. <b>Canonical String:</b> Concatenates Method, Path, Timestamp, Nonce, and Payload hash."),
                   ("2. <b>HMAC Imzo:</b> Server va mijoz o'rtasidagi maxfiy kalit bilan <code>HMAC-SHA256</code> hisoblanadi.",
                    "2. <b>HMAC Подпись:</b> Вычисление криптографической подписи секретным симметричным ключом.",
                    "2. <b>HMAC Signature:</b> Generated via <code>crypto.createHmac('sha256', secret)</code>."),
                   ("3. <b>X-Timestamp:</b> Agar so'rov vaqti 5 daqiqadan eski bo'lsa — rad etiladi (Time Skew Expired).",
                    "3. <b>Временное окно:</b> Запрос старше 300 секунд немедленно отбрасывается.",
                    "3. <b>Window Validation:</b> Reject requests older than 300 seconds (clock skew protection)."),
                   ("4. <b>X-Nonce (Number Once):</b> Ishlatilgan har bir Nonce Redis keshda 5 daqiqa saqlanadi. Bir xil so'rovni ikkinchi marta yuborib bo'lmaydi (Replay Attack barbod bo'ladi)!",
                    "4. <b>X-Nonce:</b> Одноразовый ID запроса сохраняется в Redis. Повторный запрос отклоняется!",
                    "4. <b>X-Nonce Cache:</b> One-time tokens stored in Redis for window duration, completely nullifying replay attacks!")
               ])
         + '</div>'
))

# 7. Code Dissection: Node.js HMAC & Token Bucket
S.append(slide(
    ph=("Kod Tahlili", "Анализ Кода", "Code Dissection"), time="22–26",
    eyebrow=("Dasturiy realizatsiya", "Программная реализация", "Middleware Implementation"),
    title=("Node.js da HMAC Tekshirish va Token Bucket Middleware",
           "Реализация HMAC и Token Bucket на Node.js",
           "Production Node.js HMAC Verification & Token Bucket Middleware"),
    body=code("""const crypto = require('crypto');

// 1. HMAC-SHA256 Request Signature Verification Middleware
function verifyHmacSignature(secretKey, nonceCache) {
  return (req, res, next) => {
    const signature = req.headers['x-signature'];
    const timestamp = parseInt(req.headers['x-timestamp'], 10);
    const nonce = req.headers['x-nonce'];

    if (!signature || !timestamp || !nonce) {
      return res.status(401).json({ error: 'Missing security headers' });
    }

    // Replay attack prevention: 5-minute validity window
    const now = Math.floor(Date.now() / 1000);
    if (Math.abs(now - timestamp) > 300) {
      return res.status(401).json({ error: 'Request timestamp expired (Time Skew)' });
    }

    // Check if nonce was already consumed
    if (nonceCache.has(nonce)) {
      return res.status(401).json({ error: 'Replay attack detected: Nonce already used' });
    }
    nonceCache.add(nonce); // Store nonce in memory/Redis with TTL

    // Build canonical string and recalculate HMAC
    const payload = JSON.stringify(req.body || {});
    const canonical = `${req.method}|${req.path}|${timestamp}|${nonce}|${payload}`;
    const expectedSig = crypto.createHmac('sha256', secretKey).update(canonical).digest('hex');

    // Constant-time comparison to prevent timing attacks
    if (!crypto.timingSafeEqual(Buffer.from(signature), Buffer.from(expectedSig))) {
      return res.status(403).json({ error: 'Invalid HMAC signature: Payload tampered!' });
    }
    next();
  };
}""")
))

# 8. Real World Case Studies: T-Mobile Breach & Cloudflare Record
S.append(slide(
    ph=("Keyslar", "Кейсы", "Case Studies"), time="26–30",
    eyebrow=("Haqiqiy hodisalar", "Реальн\u044bе инциденты", "Real-World Cyber Incidents"),
    title=("T-Mobile 2023 Falokati va Cloudflare 71M RPS Rekordi",
           "Утечка T-Mobile 2023 и Рекорд Cloudflare 71M RPS",
           "The T-Mobile 2023 API Catastrophe vs Cloudflare 71M RPS Defense"),
    body='<div class="cols">\n'
         + box("red", ("T-Mobile 2023: 37 Million Mijoz Ma'lumotlari Sizishi", "T-Mobile: Утечка 37 Миллионов Аккаунтов", "T-Mobile: The 37M Record API Disaster"),
               items=[
                   ("<b>Zaiflik:</b> Kompaniyaning ochiq API endpointida Rate Limiting va BOLA/avtorizatsiya to'g'ri o'rnatilmagan edi.",
                    "<b>Причина:</b> Незащищенный API без rate limiting и должной авторизации.",
                    "<b>Root Cause:</b> An unauthenticated, rate-unlimited API endpoint exposed internal records."),
                   ("<b>Hujum:</b> Hacker oddiy skript orqali 37 million mijozning ismi, tug'ilgan sanasi, manzili va telefon raqamlarini tortib oldi.",
                    "<b>Ход атаки:</b> Злоумышленник скриптом без помех выкачал персональные данные 37 млн абонентов.",
                    "<b>Execution:</b> Automated scraper quietly harvested 37 million subscriber records over weeks."),
                   ("<b>Oqibat:</b> Kompaniyaga <b>$350 million jarima</b> va jiddiy obro' yo'qotilishi.",
                    "<b>Ущерб:</b> $350 млн судебных штрафов и компенсаций пользователям.",
                    "<b>Aftermath:</b> $350M settlement penalty and irreversible brand damage.")
               ])
         + box("green", ("Cloudflare & HTTP/2 Rapid Reset (CVE-2023-44487)", "Cloudflare: Защита от 71 Млн Запросов в Секунду", "Cloudflare: Mitigating 71M RPS Rapid Reset"),
               items=[
                   ("<b>Tarixdagi eng yirik L7 hujum:</b> Soniyasiga <b>71 million so'rov (RPS)</b> yuborildi.",
                    "<b>Масштаб:</b> Крупнейшая в истории L7 DDoS-атака мощностью более 71 млн RPS.",
                    "<b>Magnitude:</b> Record-shattering Layer 7 DDoS assault peaking at 71M requests/second."),
                   ("<b>Hujum hiylasi:</b> HTTP/2 protokolidagi <code>RST_STREAM</code> kadrini suiiste'mol qilib, ulanishni yopmasdan yangi so'rovlar oqimi yuborilgan.",
                    "<b>Механизм:</b> Злоупотребление отменой потоков RST_STREAM в HTTP/2 без разрыва TCP.",
                    "<b>Exploit Vector:</b> Abusing HTTP/2 stream multiplex cancellation before server frames responded."),
                   ("<b>Natija:</b> Taqsimlangan Token Bucket va Anycast arxitekturasi tufayli Cloudflare mijozlari buni sezmadi ham!",
                    "<b>Итог:</b> Алгоритмы динамической фильтрации Cloudflare отразили атаку без простоя сервисов.",
                    "<b>Result:</b> Autonomous token bucket mitigation and stream thresholds absorbed the surge with zero downtime.")
               ])
         + '</div>'
))

# 9. Enterprise Defense: WAF, API Gateway & JA4 Fingerprinting
S.append(slide(
    ph=("Arxitektura", "Архитектура", "Architecture"), time="30–33",
    eyebrow=("Korporativ himoya", "Корпоративная эшелонированная защита", "Enterprise Perimeter Defense"),
    title=("API Gateway, WAF va TLS Fingerprinting (JA4)",
           "Шлюзы API, WAF и Отпечатки TLS (JA4)",
           "Modern API Gateways, WAF & Cryptographic TLS Fingerprinting"),
    body='<div class="cols">\n'
         + box("navy", ("API Gateway & WAF Vazifalari", "Роль API Gateway и WAF", "API Gateway & WAF Roles"),
               items=[
                   ("<b>Markazlashgan tekshiruv:</b> Har bir mikroservis alohida kod yozmaydi. API Gateway (Kong, Envoy) kirishdayoq Token Bucket tekshiruvini bajaradi.",
                    "<b>Единая точка входа:</b> Gateway (Kong, Envoy) берёт на себя rate limiting и проверку JWT до микросервисов.",
                    "<b>Centralized Ingress:</b> Edge gateways (Kong, Envoy, Traefik) enforce token rate limits before services."),
                   ("<b>Sxema validatsiyasi:</b> Kelayotgan JSON OpenAPI spetsifikatsiyasiga mos kelmasa, so'rov darhol to'xtatiladi.",
                    "<b>Валидация схемы:</b> Проверка структуры JSON по контракту OpenAPI прямо на границе сети.",
                    "<b>OpenAPI Contract Validation:</b> Drops malformed or poisoned payloads before reaching backend nodes.")
               ])
         + box("purple", ("JA4 / TLS Barmoq Izi (Anti-Bot Texnologiyasi)", "TLS Fingerprinting (Технология JA4)", "JA4 Fingerprinting & Bot Mitigation"),
               items=[
                   ("Hacker o'z skriptida <code>User-Agent: Mozilla/5.0</code> deb brauzerni soxtalashtirishi mumkin.",
                    "Атакующий легко подделывает заголовки User-Agent под настоящий браузер Chrome.",
                    "Adversaries easily spoof HTTP headers like User-Agent to mimic Chrome browsers."),
                   ("Ammo Python <code>requests</code> yoki Golang mijozining <b>TLS Handshake parametrlari (Cipher Suites, Extensions)</b> haqiqiy Chrome brauzeridan mutlaqo farq qiladi!",
                    "Однако набор шифров TLS и расширений у Python скрипта кардинально отличается от браузера.",
                    "However, TLS Client Hello extension suites distinctly unmask Python, Go, or curl clients."),
                   ("<b>JA4 algoritmi:</b> TLS ulanishidan hosil bo'lgan xesh orqali buzg'unchi botlar IP manzilini o'zgartirsa ham 100% aniqlanadi va bloklanadi!",
                    "<b>Отпечаток JA4:</b> Хэширование параметров TLS позволяет мгновенно блокировать скриптовых ботов.",
                    "<b>JA4 Hashing:</b> Fingerprints client TLS stack attributes, neutralizing bot proxies instantly.")
               ])
         + '</div>'
))

# 10. Hands-on Lab
S.append(slide(
    ph=("Amaliyot", "Практика", "Hands-on Lab"), time="33–42",
    eyebrow=("Interaktiv Studio", "Интерактивная Студия", "Interactive Studio"),
    title=("Amaliy Ish: API Defender Studio — Token Bucket va HMAC Laboratoriyasi",
           "Практика: Студия API Defender — Token Bucket и HMAC",
           "Hands-on Lab: API Defender Studio — Token Bucket & HMAC"),
    body='<div class="box blue">\n'
         + el("h3", "Laboratoriya Missiyasi: API Defender Studio (12 Daqiqa)", "Миссия Лаборатории: Студия API Defender (12 Минут)", "Lab Mission: API Defender Studio (12 Minutes)")
         + el("p", "Brauzerda <code>studio/index.html</code> ni oching. Terminal yoki server o'rnatish shart emas! Jonli Token Bucket chelagi, DDoS hujumlari va WebCrypto HMAC-SHA256 imzolashni sinovdan o'tkazing.",
              "Откройте <code>studio/index.html</code> в браузере. Установка серверов не требуется! Исследуйте ведро Token Bucket, DDoS-атаки и криптографическую подпись HMAC-SHA256.",
              "Open <code>studio/index.html</code> in your browser. No server setup required! Test live Token Bucket physics, DDoS floods, and WebCrypto HMAC-SHA256 signing.")
         + '</div>\n'
         + table(
             headers=[("Kvest", "Квест", "Quest"),
                      ("Amal va Vazifa", "Действие в Студии", "Studio Action"),
                      ("Kutilayotgan Natija (Tekshirish)", "Ожидаемый Результат", "Expected Verification")],
             rows=[
                 [("<b>1-Kvest: Token Bo'shatish</b><br>(2 Ball)", "<b>Квест 1: Исчерпание Токенов</b>", "<b>Quest 1: Token Exhaustion</b>"),
                  ("<code>1x So'rov</code> tugmasini ketma-ket 10 marta bosing (Capacity: 10, Refill: 2/s).",
                   "Нажмите <code>1x Запрос</code> 10 раз подряд до полного опустошения ведра.",
                   "Click <code>1x Request</code> 10 times consecutively until bucket empties."),
                  ("Chelakdagi tokenlar 0 ga tushadi va birinchi <b>HTTP 429 Too Many Requests</b> bloklanadi.",
                   "Токены заканчиваются и фиксируется первая ошибка <b>HTTP 429 Too Many Requests</b>.",
                   "Tokens drop to 0 and first <b>HTTP 429 Too Many Requests</b> is recorded.")],
                 [("<b>2-Kvest: 50 RPS DDoS Hujumi</b><br>(3 Ball)", "<b>Квест 2: DDoS 50 RPS</b>", "<b>Quest 2: 50 RPS DDoS Attack</b>"),
                  ("<code>50 RPS Portlash (DDoS)</code> tugmasini bosing va 20 tadan ko'p so'rov bloklanishini kuzating.",
                   "Запустите <code>DDoS Всплеск (50 RPS)</code> и заблокируйте более 20 вредоносных запросов.",
                   "Trigger <code>50 RPS Burst (DDoS)</code> and observe over 20 malicious requests dropped."),
                  ("Chelak to'lib-toshib ketadi, qonuniy limitdan oshgan barcha so'rovlar HTTP 429 bilan qaytariladi.",
                   "Лимитер успешно сглаживает трафик, отсекая весь флуд со статусом 429.",
                   "Bucket overflows; excess queries safely discarded with HTTP 429.")],
                 [("<b>3-Kvest: Soxtalashtirish (Tamper)</b><br>(3 Ball)", "<b>Квест 3: Подмена (Tamper)</b>", "<b>Quest 3: Payload Tampering</b>"),
                  ("HMAC tabida <code>Soxtalashtirish (Tamper Attack)</code> tugmasini bosing (summa $100 -> $999,999 ga aylanadi).",
                   "В табе HMAC нажмите <code>Подменить данные (Tamper Attack)</code> ($100 -> $999,999).",
                   "In HMAC tab, click <code>Tamper Payload</code> (altering amount from $100 to $999,999)."),
                  ("Kanonik xesh buziladi: Server <b>HTTP 403 / 401 Signature Mismatch!</b> deb so'rovni bekor qiladi.",
                   "Канонический хэш нарушен: Сервер отклоняет запрос с ошибкой <b>403 Signature Mismatch</b>.",
                   "Hash integrity broken: Server rejects request with <b>HTTP 403 Signature Mismatch!</b>")],
                 [("<b>4-Kvest: Replay Attack</b><br>(2 Ball)", "<b>Квест 4: Replay-атака</b>", "<b>Quest 4: Replay Attack</b>"),
                  ("Qonuniy yuborilgan so'rovdan so'ng <code>Replay Attack Sinovi</code> tugmasini bosing.",
                   "После валидного запроса нажмите <code>Тест Replay-атаки</code> с тем же Nonce.",
                   "Click <code>Simulate Replay Attack</code> using identical Nonce."),
                  ("Server Nonce keshini ko'rib, <b>HTTP 401 Replay Attack Detected: Nonce already consumed</b> beradi.",
                   "Сервер определяет дубликат Nonce и блокирует повторную транзакцию с <b>HTTP 401</b>.",
                   "Server flags duplicate Nonce and rejects duplicate transaction with <b>HTTP 401</b>.")]
             ]
         )
))

# 11. Security Matrix
S.append(slide(
    ph=("Taqqoslash", "Сравнение", "Comparison"), time="42–44",
    eyebrow=("Muhandislik xulosasi", "Инженерное резюме", "Security Matrix"),
    title=("API Xavfsizlik Choralarining Taqqoslama Matritsasi",
           "Матрица Сравнения Технологий Защиты API",
           "Comprehensive API Security Control Matrix"),
    body=table(
        headers=[("Himoya Qatlami", "Уровень Защиты", "Defense Layer"),
                 ("To'xtatadigan Tahdidi", "Предотвращаемые Угрозы", "Mitigated Threats"),
                 ("Bajarilish Nuqtasi", "Где Исполняется", "Execution Point"),
                 ("Kechikish (Latency)", "Задержка (Latency)", "Latency Overhead")],
        rows=[
            [("<b>mTLS / TLS 1.3</b>", "<b>mTLS / TLS 1.3</b>", "<b>mTLS / TLS 1.3</b>"),
             ("Paketlarni tutish (Sniffing), MitM, ruxsatsiz mijoz ulanishi.",
              "Перехват трафика, MitM-атаки, несанкционированные клиенты.",
              "Packet eavesdropping, MitM tampering, unauthorized endpoints."),
             ("Transport darajasi (Reverse Proxy / Envoy).",
              "Транспортный уровень (Ingress / Envoy).",
              "Transport Layer (Edge Ingress / Envoy mesh)."),
             ("&lt; 1 ms (Handshake paytida 1 marta).",
              "&lt; 1 мс (только при установке соединения).",
              "&lt; 1 ms (Handshake one-time cost).")],
            [("<b>Distributed Rate Limiter</b>", "<b>Distributed Rate Limiter</b>", "<b>Distributed Rate Limiter</b>"),
             ("L7 DDoS, Brute-Force parol sindirish, Data Scraping.",
              "L7 DDoS, перебор паролей, скрапинг базы данных.",
              "Layer 7 DDoS, brute-force attacks, high-speed data harvesting."),
             ("API Gateway + Redis Lua Engine.",
              "Шлюз API + Redis кластер через Lua.",
              "Edge Gateway + Centralized Redis via Lua."),
             ("~1–2 ms (In-memory Redis query).",
              "~1–2 мс (быстрый запрос в оперативную память).",
              "~1–2 ms (Optimized in-memory network round-trip).")],
            [("<b>HMAC-SHA256 Signing</b>", "<b>HMAC-SHA256 Signing</b>", "<b>HMAC-SHA256 Signing</b>"),
             ("So'rov parametrlarini o'zgartirish (Tampering), Replay Attack.",
              "Подмена параметров запроса, атаки повторного воспроизведения.",
              "Payload parameter tampering, intercepted replay exploitation."),
             ("Ilova darajasi (Node.js / Go Middleware).",
              "Уровень приложения (Middleware шлюза).",
              "Application Middleware layer."),
             ("&lt; 0.1 ms (Lokal kriptografik hisoblash).",
              "&lt; 0.1 мс (локальное вычисление хэша).",
              "&lt; 0.1 ms (Local cryptographic CPU execution).")]
        ]
    )
))

# 12. Summary & Homework
S.append(slide(
    ph=("Xulosa", "Итоги", "Summary"), time="44–45",
    eyebrow=("Mustaqil muhandislik ishi", "Домашнее задание", "Engineering Project"),
    title=("Xulosa va Uy Vazifasi: Bank API Himoya Spetsifikatsiyasi",
           "Итоги и Задание: Архитектура Защиты Банковского API",
           "Summary & Homework: Enterprise Financial API Security Blueprint"),
    body='<div class="cols">\n'
         + box("blue", ("Dars Xulosasi", "Главные Выводы", "Key Takeaways"),
               items=[
                   ("Oddiy autentifikatsiya (API key) yetarli emas: har bir API endpointi <b>Rate Limiting</b> va <b>BOLA</b> tekshiruviga ega bo'lishi shart.",
                    "Статичных токенов недостаточно: критичны жесткие лимиты частоты и верификация прав владения.",
                    "Static tokens provide zero protection against resource exhaustion and horizontal BOLA privilege leaks."),
                   ("<b>Token Bucket</b> algoritmi resurslarni himoyalagan holda qonuniy foydalanuvchilarning tezkor so'rovlariga moslashadi.",
                    "Алгоритм Token Bucket балансирует защиту от DDoS с комфортом легитимных клиентов.",
                    "Token Bucket algorithm elegantly balances DDoS defense with natural client request bursts."),
                   ("Kritik tranzaksiyalar doimo <b>HMAC imzo, Nonce va Timestamp</b> bilan replay hujumlaridan himoyalanishi shart.",
                    "Финансовые эндпоинты требуют криптографической подписи HMAC, Nonce и проверки времени.",
                    "Financial transaction payloads mandate HMAC signing, ephemeral nonces, and timestamp skew validation.")
               ])
         + box("purple", ("Uy Vazifasi: Bank Transfer API Arxitekturasi (10 Ball)", "Домашнее Задание: Защита API Переводов (10 Баллов)", "Homework: Bank Transfer API Blueprint (10 Pts)"),
               items=[
                   ("Bankning <code>/api/v1/transfers</code> endpointi uchun himoya tizimi arxitekturasini loyihalashtiring.",
                    "Спроектируйте архитектуру комплексной защиты эндпоинта денежных переводов <code>/api/v1/transfers</code>.",
                    "Design comprehensive defense architecture for financial endpoint <code>/api/v1/transfers</code>."),
                   ("<b>Talablar:</b> 1) Idempotency Key orqali dublikatlarni to'xtatish. 2) Token Bucket (5 req/min). 3) HMAC-SHA256 imzosi tekshiruvi. 4) BOLA tekshiruvi.",
                    "<b>Требования:</b> 1) Idempotency Key. 2) Token Bucket (5 req/min). 3) HMAC верификация. 4) Проверка BOLA.",
                    "<b>Requirements:</b> 1) Idempotency key logic. 2) Token Bucket (5 req/min). 3) HMAC verification. 4) BOLA ownership validation."),
                   ("Kod va tushuntirish xatini Markdown formatida taqdim eting.",
                    "Предоставьте код middleware и архитектурную записку в формате Markdown.",
                    "Submit middleware code and architectural specification in Markdown format.")
               ])
         + '</div>'
))

# Teacher Notes
N_UZ = [
    ["Kirish", "O'quvchilarga kundalik hayotdagi Instagram, Payme yoki Click orqasida har soniya millionlab API so'rovlari o'tishini tushuntiring.", "Slaydni oching."],
    ["OWASP API Top 10", "Veb zaifliklar (XSS, SQLi) dan farqli o'laroq, API zaifliklari asosan biznes-mantiq (BOLA, Rate Limit) bilan bog'liqligini ta'kidlang.", "Jadvalni ko'rsating."],
    ["L3/L4 vs L7", "O'quvchilarga oddiy DDOS (kanalni tiqiltirish) va ilova darajasidagi DDOS (og'ir SQL so'rov orqali DBni yiqitish) farqini misollar bilan ochib bering.", "Taqqoslang."],
    ["Algoritmlar", "Doskada Token Bucket chelagi va suv tomchilarini chizib ko'rsating. Qanday qilib qisqa portlash (burst) o'tishi va cheklov ishlashi tushuntirilsin.", "Formulani tushuntiring."],
    ["Redis & Lua", "Nega bitta serverdagi o'zgaruvchi klasterda ishlamasligini va Lua skripti Redisda atomar (navbatsiz) bajarilishini tushuntiring.", "Klaster sxemasini chizing."],
    ["HMAC", "Payme yoki Stripe webhooklarida qanday qilib imzo tekshirilishi, Nonce nima uchun kerakligini va Replay hujumlarini ko'rsating.", "Sxemani tushuntiring."],
    ["Kod tahlili", "crypto.timingSafeEqual funksiyasi nega oddiy === o'rniga ishlatilishini (timing attack himoyasi) tushuntiring.", "Kodni tahlil qiling."],
    ["Keyslar", "T-Mobile hodisasida oddiy limit yo'qligi kompaniyaga $350 millionga tushganini eslating.", "Keysni muhokama qiling."],
    ["Infratuzilma", "JA4 TLS barmoq izi orqali hacker Python skriptini Chrome deb alday olmasligi sababini tushuntiring.", "JA4 ni tushuntiring."],
    ["Amaliyot", "O'quvchilar bilan birgalikda 10 ta so'rov yuborib, 429 xatosini va Replay attack rad etilishini terminalda kuzating.", "12 daqiqa taymerni yoqing."],
    ["Matritsa", "Xavfsizlik qatlamlari (mTLS, Rate Limiting, HMAC) bir-birini to'ldirishini, bittasi ikkinchisini almashtira olmasligini ta'kidlang.", "Matritsani ko'rib chiqing."],
    ["Xulosa", "Uy vazifasidagi 10 ballik mezonni e'lon qiling va savollarga javob bering.", "Varaqalarni yig'ing."]
]

N_RU = [
    ["Введение", "Объясните, что за каждым мобильным приложением (Click, Payme, Instagram) стоят миллионы API запросов каждую секунду.", "Откройте титульный слайд."],
    ["OWASP API", "Подчеркните, что в отличие от классического веба, уязвимости API кроются в бизнес-логике (BOLA, отсутствие лимитов).", "Разберите таблицу OWASP."],
    ["L3/L4 vs L7", "Покажите разницу между флудом каналов связи и тяжелыми SQL-запросами L7, которые валят базу данных при 100 запросах в секунду.", "Сравните уровни L3/L7."],
    ["Алгоритмы", "Нарисуйте модель ведра Token Bucket на доске. Объясните механику пополнения токенов и сглаживание трафика.", "Поясните Token Bucket."],
    ["Redis & Lua", "Разберите проблему рассинхронизации памяти в кластерах и атомарность скриптов Lua внутри Redis.", "Объясните атомарность Lua."],
    ["HMAC", "Объясните, почему критичные платёжные шлюзы подписывают запросы через HMAC и как Nonce предотвращает повторные списания средств.", "Разберите HMAC подпись."],
    ["Анализ кода", "Обратите внимание на crypto.timingSafeEqual для защиты от тайминг-атак при сравнении хэшей.", "Построчно разберите middleware."],
    ["Кейсы", "Напомните, что халатность T-Mobile стоила $350 млн из-за банального отсутствия лимитов на эндпоинте.", "Обсудите последствия утечки."],
    ["Инфраструктура", "Объясните концепцию отпечатков TLS JA4, разоблачающих скриптовых ботов независимо от поддельного User-Agent.", "Поясните JA4 TLS фингерпринт."],
    ["Практикум", "Контролируйте выполнение 3 задач в терминале, убедитесь в фиксации ошибки 429 и блокировке дубликата Nonce.", "Запустите таймер 12 минут."],
    ["Матрица", "Резюмируйте эшелонированный подход: mTLS для транспорта, Rate Limit для ресурсов, HMAC для целостности.", "Обобщите матрицу мер."],
    ["Итоги", "Огласите критерии домашнего задания на 10 баллов и ответьте на вопросы.", "Соберите рабочие листы."]
]

N_EN = [
    ["Intro", "Contextualize that modern digital experiences (Payme, Stripe, banking apps) communicate exclusively via continuous API transactions.", "Open title slide."],
    ["OWASP API", "Highlight that unlike legacy web exploits (XSS, SQLi), modern API vulnerabilities exploit authorization flaws and missing quotas.", "Review OWASP matrix."],
    ["L3/L4 vs L7", "Differentiate between raw volumetric bandwidth floods and stealthy Layer 7 resource-exhaustion queries hitting unindexed database tables.", "Contrast L3/L4 with L7."],
    ["Algorithms", "Illustrate the Token Bucket model on whiteboard, demonstrating token regeneration and burst tolerance versus leaky bucket pacing.", "Explain bucket math."],
    ["Redis & Lua", "Unpack why in-memory rate limiting fails across Kubernetes pods and how embedded Lua guarantees concurrency atomicity.", "Diagram Redis clustering."],
    ["HMAC", "Explain symmetric request signing architectures used by Stripe and AWS SigV4, emphasizing nonce caches against replay attacks.", "Break down HMAC pipeline."],
    ["Code Dissection", "Point out why crypto.timingSafeEqual is strictly mandatory over string equality to mitigate side-channel timing attacks.", "Walk through JS middleware."],
    ["Case Studies", "Discuss the $350M T-Mobile breach as an empirical consequence of rate-unlimited scraping of customer entities.", "Discuss incident findings."],
    ["Infrastructure", "Demystify JA4 TLS client fingerprinting and explain how TLS cipher suites expose automated headless scripts.", "Explain JA4 signatures."],
    ["Lab", "Guide students through executing 10 burst requests, witnessing HTTP 429 backoff and intercepting simulated replay exploits.", "Start 12-min lab timer."],
    ["Matrix", "Synthesize defense-in-depth: mTLS on wire, distributed rate limiting on ingress, and HMAC signature validation on application logic.", "Synthesize architecture."],
    ["Summary", "Announce the 10-point banking API security blueprint assignment and open the floor for technical questions.", "Collect worksheets."]
]

NOTES = {"uz": N_UZ, "ru": N_RU, "en": N_EN}

# --- Worksheet (Varaqa) ---
V = []
V.append(sheet_header(
    h1=("Kiberxavfsizlik: API Xavfsizligi va Rate Limiting",
        "Кибербезопасность: Безопасность API и Rate Limiting",
        "CyberSecurity: Enterprise API Security & Rate Limiting"),
    sub=("Amaliy Laboratoriya Varaqasi · 10–11-sinf · 5-hafta · 23-dars",
         "Практический Рабочий Лист · 10–11 класс · Неделя 5 · Урок 23",
         "Hands-On Lab Worksheet · Grades 10–11 · Week 5 · Lesson 23")
))

V.append(mission(
    h=("Laboratoriya Vazifasi: API Defender Studio Kvestlari",
       "Миссия Лабораторной: Квесты в Студии API Defender",
       "Lab Mission: API Defender Studio Defense Quests"),
    p=("Interaktiv <code>API Defender Studio</code> (studio/index.html) muhitida Token Bucket chelagi bilan DDoS hujumlarini qaytarish, "
       "WebCrypto API orqali HMAC-SHA256 so'rov imzolash, Tamper (soxtalashtirish) va Replay Attack hujumlarini fosh qilish.",
       "В интерактивной среде <code>API Defender Studio</code> (studio/index.html) отразить DDoS-флуд с помощью алгоритма Token Bucket, "
       "подписать запросы HMAC-SHA256 через WebCrypto API и нейтрализовать атаки фальсификации (Tamper) и повтора (Replay).",
       "In the interactive <code>API Defender Studio</code> (studio/index.html), mitigate DDoS floods via Token Bucket rate limiting, "
       "cryptographically sign requests with WebCrypto HMAC-SHA256, and intercept payload tampering and replay attacks."))
)

V.append(table(
    headers=[
        ("Amaliy Kvest (Studio)", "Практический Квест (Студия)", "Studio Defense Quest"),
        ("Harakat / Hujum Turi", "Действие / Тип Атаки", "Action / Attack Scenario"),
        ("Kutilgan Natija (Status)", "Ожидаемый Результат", "Expected Verification"),
        ("Ball va Holat", "Баллы и Статус", "Score & Status")
    ],
    rows=[
        [("1. Tokenlarni Bo'shatish", "1. Исчерпание Токенов", "1. Token Exhaustion"),
         ("`1x So'rov` tugmasini ketma-ket 10 marta bosing", "Нажатие `1x Запрос` 10 раз подряд", "10 consecutive `1x Request` clicks"),
         ("Tokenlar 0 ga tushadi, HTTP 429 Too Many Requests olinadi", "Токены на нуле, статус 429 Too Many Requests", "Tokens reach 0, HTTP 429 Too Many Requests logged"),
         ("2 ball / [  ]", "2 балла / [  ]", "2 pts / [  ]")],
        [("2. 50 RPS DDoS Hujumi", "2. DDoS-атака 50 RPS", "2. 50 RPS DDoS Burst"),
         ("`50 RPS Portlash (DDoS)` oqimini yoqish", "Запуск всплеска `50 RPS Burst`", "Execute `50 RPS Burst (DDoS)` attack"),
         ("Chelak toshadi: 20+ ta ortiqcha so'rov 429 bilan to'xtatiladi", "Лимитер сглаживает всплеск, отсекая 20+ запросов со статусом 429", "Bucket throttles surge: 20+ excessive queries dropped with 429"),
         ("3 ball / [  ]", "3 балла / [  ]", "3 pts / [  ]")],
        [("3. Soxtalashtirish (Tamper)", "3. Подмена (Tamper Attack)", "3. Payload Tampering"),
         ("`Soxtalashtirish` tugmasi ($100 -> $999,999)", "Подмена суммы ($100 -> $999,999)", "Tamper payload amount ($100 -> $999,999)"),
         ("HMAC imzosi buziladi: HTTP 403 / 401 Signature Mismatch!", "Хэш нарушен: ошибка 403/401 Signature Mismatch!", "HMAC hash fails: HTTP 403/401 Signature Mismatch!"),
         ("3 ball / [  ]", "3 балла / [  ]", "3 pts / [  ]")],
        [("4. Replay Attack Sinovi", "4. Защита от Replay-атаки", "4. Replay Attack Defense"),
         ("Eski so'rovni bir xil Nonce bilan qayta yuborish", "Повторная отправка с тем же Nonce", "Resend payload with duplicated Nonce"),
         ("Server Nonce keshini ko'rib, HTTP 401 Replay Detected beradi", "Сервер видит дубликат Nonce: отказ 401 Replay Detected", "Server flags cached Nonce: HTTP 401 Replay Detected"),
         ("2 ball / [  ]", "2 балла / [  ]", "2 pts / [  ]")]
    ]
))

V.append(sheet_box(
    h=("Xavfsizlik Tahlili va Nazariy Savollar", "Анализ Безопасности и Вопросы", "Architectural Analysis & Written Queries"),
    body_html=writelines(3, label=("1. Nega taqsimlangan mikroservislarda (Kubernetes klasterida) rate limiting lokal xotirada (RAM) emas, Redis orqali yuritilishi shart?",
                                   "1. Почему в распределенных микросервисах (Kubernetes) rate limiting обязан вестись через Redis, а не локальную память?",
                                   "1. Why must rate limiting in distributed Kubernetes clusters be coordinated via Redis rather than process-local RAM?"))
             + "<br>"
             + writelines(3, label=("2. API so'rovlarida HMAC-SHA256 imzosi, X-Timestamp va X-Nonce birgalikda qanday qilib Replay Attack va Tampering hujumlarini to'xtatadi?",
                                   "2. Как связка HMAC-SHA256, X-Timestamp и X-Nonce полностью нейтрализует атаки Tampering и Replay?",
                                   "2. How does the triad of HMAC-SHA256, X-Timestamp, and X-Nonce definitively prevent payload tampering and replay attacks?"))
))

V.append(sheet_box(
    h=("Baholash Mezoni (10 Ball)", "Критерии Оценки (10 Баллов)", "Grading Rubric (10 Points)"),
    body_html=rubric([
        (("Token Bucket algoritmi va Redis taqsimlangan arxitekturasi to'g'ri tushuntirilgan", "Алгоритм Token Bucket и архитектура Redis разобраны верно", "Token Bucket mathematics & distributed Redis analyzed"), "3 ball"),
        (("HMAC-SHA256 imzosi, X-Nonce va Replay Attack himoyasi to'liq asoslangan", "Подпись HMAC-SHA256, Nonce и защита от Replay-атак аргументированы", "HMAC-SHA256, Nonce cache & replay defense justified"), "3 ball"),
        (("OWASP API Top 10 (BOLA, DDoS, Mass Assignment) va T-Mobile keysi tahlil qilingan", "Разобраны OWASP API Top 10 и инцидент T-Mobile 2023", "OWASP API Top 10 & T-Mobile breach case evaluated"), "2 ball"),
        (("Laboratoriya bosqichlari to'liq bajarilgan va yozma savollarga asosli javob berilgan", "Практические шаги выполнены, даны ответы на аналитические вопросы", "Lab experiments validated and written queries rigorously answered"), "2 ball"),
    ], "10 ball")
))

V.append("</div>\n" + sign_box("Musulmonov Mamarajab"))

VARAQA_BODY = "\n".join(V)

lesson = Lesson(
    outdir=D,
    titles=TITLES,
    sheet_titles=SHEET_TITLES,
    key="vc-notes-10-23",
    slides=S,
    notes=NOTES,
    varaqa_body=VARAQA_BODY
)

if __name__ == "__main__":
    out = lesson.build()
    print("Created:", out)
