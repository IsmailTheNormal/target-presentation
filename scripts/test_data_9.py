#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
9-Sinf: 25 Savolli Vibecoding Full-Stack, REST API va Agentik Muhandislik Testi
O'qituvchi: Ismoiljon Usmonov · Target International School
Uzbek va Russian variantlari (5 ta variant: A, B, C, D, E)
"""

META_9_UZ = {
    "school_name": "TARGET INTERNATIONAL SCHOOL — YUNUSOBOD",
    "teacher_name": "Ismoiljon Usmonov",
    "exam_title": "9-SINF: VIBECODING FULL-STACK, REST API VA AGENTIK MUHANDISLIK",
    "track_title": "Vibecoding Full-Stack & DevOps Track · O'qituvchi: Ismoiljon Usmonov",
    "academic_year": "2026–2027 O'quv Yili",
    "label_name": "O'quvchi F.I.Sh.",
    "label_class": "Sinfi",
    "label_date": "Sana",
    "label_variant": "Variant",
    "variant_val": "1-Variant (Rasmiy)",
    "label_max_score": "Maksimal ball",
    "unit_points": "ball",
    "label_score": "To'plangan ball",
    "instructions": "Ko'rsatma: Har bir savolga berilgan 5 ta variantdan (A, B, C, D, E) faqat bitta to'g'ri javobni tanlang va belgilang. Har bir to'g'ri javob uchun 1 ball beriladi."
}

KEYS_META_9_UZ = {
    "heading": "JAVOBLAR KALITI VA BAHOLASH MEZONI",
    "subheading": "O'qituvchi: Ismoiljon Usmonov · 9-sinf Vibecoding rasmiy kaliti (25 ta savol)",
    "table_headers": ["№", "Kalit", "Mavzu / Kompetensiya", "Izoh va Tushuntirish"],
    "scale_heading": "Rasmiy 25 Ballik Baholash Shkalasi:",
    "rubric_tiers": [
        {"grade": "A'lo (5)", "range": "22 – 25 ball", "desc": "Full-Stack, Express REST API, SQLite, Docker va Git bo'yicha mustahkam muhandislik bilimi"},
        {"grade": "Yaxshi (4)", "range": "18 – 21 ball", "desc": "Backend, HTTP statuslar va autentifikatsiya yaxshi o'zlashtirilgan"},
        {"grade": "Qoniqarli (3)", "range": "13 – 17 ball", "desc": "SQL so'rovlari va middleware mexanizmini takrorlash lozim"},
        {"grade": "Qoniqarsiz (2)", "range": "0 – 12 ball", "desc": "Full-Stack asoslari qayta o'rganilishi zarur"}
    ]
}

META_9_RU = {
    "school_name": "TARGET INTERNATIONAL SCHOOL — ЮНУСАБАД",
    "teacher_name": "Исмоилжон Усмонов",
    "exam_title": "9 КЛАСС: VIBECODING FULL-STACK, REST API И АГЕНТНАЯ ИНЖЕНЕРИЯ",
    "track_title": "Vibecoding Full-Stack & DevOps Track · Преподаватель: Исмоилжон Усмонов",
    "academic_year": "2026–2027 Учебный Год",
    "label_name": "Ф.И.О. Ученика",
    "label_class": "Класс",
    "label_date": "Дата",
    "label_variant": "Вариант",
    "variant_val": "Вариант 1 (Официальный)",
    "label_max_score": "Макс. балл",
    "unit_points": "баллов",
    "label_score": "Набранный балл",
    "instructions": "Инструкция: Из 5 предложенных вариантов (A, B, C, D, E) выберите и отметьте только один правильный ответ. За каждый правильный ответ начисляется 1 балл."
}

KEYS_META_9_RU = {
    "heading": "КЛЮЧИ ОТВЕТОВ И КРИТЕРИИ ОЦЕНИВАНИЯ",
    "subheading": "Преподаватель: Исмоилжон Усмонов · Официальный ключ Vibecoding (9 класс, 25 вопросов)",
    "table_headers": ["№", "Ключ", "Тема / Компетенция", "Пояснение и Обоснование"],
    "scale_heading": "Официальная 25-балльная шкала оценивания:",
    "rubric_tiers": [
        {"grade": "Отлично (5)", "range": "22 – 25 баллов", "desc": "Глубокие инженерные знания Full-Stack, Express REST API, SQLite, Docker и Git"},
        {"grade": "Хорошо (4)", "range": "18 – 21 балл", "desc": "Хорошее понимание бэкенда, HTTP статусов и аутентификации"},
        {"grade": "Удовлетворительно (3)", "range": "13 – 17 баллов", "desc": "Требуется повторение SQL-запросов и middleware"},
        {"grade": "Неудовлетворительно (2)", "range": "0 – 12 баллов", "desc": "Необходимо повторное изучение основ Full-Stack разработки"}
    ]
}

QUESTIONS_9_UZ = [
    {
        "text": "Full-Stack dasturlash arxitekturasida uch asosiy qatlam (3-Tier) qanday taqsimlanadi?",
        "a": "Monitor, Klaviatura va Sichqoncha.",
        "b": "Frontend (Foydalanuvchi interfeysi), Backend (Server va biznes mantiq) va Database (Ma'lumotlar bazasi).",
        "c": "HTML, CSS va shriftlar.",
        "d": "Faqat Windows, Linux va MacOS.",
        "e": "Faqat audio, video va rasmlar.",
        "correct": "B",
        "topic": "Full-Stack Arxitekturasi",
        "expl": "Full-Stack uch bo'g'indan iborat: mijoz brauzeri (Frontend), hisoblovchi server (Backend) va doimiy xotira (Database)."
    },
    {
        "text": "Vibecoding-da loyihani boshlashdan oldin PRD (Product Requirements Document) yozish nega muhim?",
        "a": "Kutubxonadagi kitoblar ro'yxatini tuzish uchun.",
        "b": "Loyiha maqsadi, funksiyalari, ma'lumotlar tuzilishi va API cheklovlarini AI ga aniq belgilab berish, noto'g'ri kod hosil bo'lishining oldini olish uchun.",
        "c": "Dasturlash tillarini bekor qilish uchun.",
        "d": "Faqat printerda qog'oz chiqarish uchun.",
        "e": "Loyiha narxini 100 barobarga oshirish uchun.",
        "correct": "B",
        "topic": "PRD va Loyiha Arxitekturasi",
        "expl": "PRD dasturchi va AI uchun texnik yo'l xaritasi bo'lib, loyihaning aniq talablar asosida qurilishini ta'minlaydi."
    },
    {
        "text": "Murakkab boshqaruv paneli (Admin Dashboard) yaratishda CSS Grid ning Flexbox dan asosiy afzalligi nimada?",
        "a": "CSS Grid faqat matnlar uchun ishlatiladi.",
        "b": "CSS Grid bir vaqtning o'zida ham qatorlar, ham ustunlar bo'yicha (2 o'lchamli) boshqaruv beradi, Flexbox esa faqat 1 o'lchamli yo'nalishga mo'ljallangan.",
        "c": "CSS Grid internetni tezlashtiradi.",
        "d": "Flexbox eskirgan va taqiqlangan.",
        "e": "Hech qanday farqi yo'q.",
        "correct": "B",
        "topic": "CSS Grid vs Flexbox",
        "expl": "Grid ikki o'lchamli (satrlar va ustunlar matritsasi) maketlar uchun, Flexbox esa bitta o'q bo'ylab joylashtirish uchun qulay."
    },
    {
        "text": "Brauzerda tashqi serverdan ma'lumot olishda qaysi asinxron JavaScript mexanizmi eng qulay hisoblanadi?",
        "a": "Sinxron while tsikli",
        "b": "`async / await` sintaksisi bilan `fetch()` funksiyasi.",
        "c": "Faqat `alert()` oynalari",
        "d": "Kodni 10 marta qayta ishga tushirish",
        "e": "Matnli faylni qo'lda ochish",
        "correct": "B",
        "topic": "Asinxron JavaScript (async/await)",
        "expl": "`async/await` Promiselar bilan ishlashni sinxron kod kabi o'qilishi oson va tushunarli qiladi, brauzerni qotirib qo'ymaydi."
    },
    {
        "text": "REST API arxitekturasida ma'lumotlar bazasiga YANGI foydalanuvchi yoki buyurtma qo'shish uchun qaysi HTTP metodi ishlatiladi?",
        "a": "GET",
        "b": "POST",
        "c": "DELETE",
        "d": "OPTIONS",
        "e": "HEAD",
        "correct": "B",
        "topic": "REST HTTP Metodlari",
        "expl": "GET — o'qish, POST — yangi resurs yaratish, PUT/PATCH — yangilash, DELETE — o'chirish metodlaridir."
    },
    {
        "text": "Mijoz so'ragan sahifa yoki resurs serverda topilmaganida qaysi rasmiy HTTP status kodi qaytadi?",
        "a": "200 OK",
        "b": "404 Not Found",
        "c": "500 Internal Server Error",
        "d": "201 Created",
        "e": "301 Moved Permanently",
        "correct": "B",
        "topic": "HTTP Status Kodlari",
        "expl": "200 — Muvaffaqiyatli, 201 — Yaratildi, 400 — Xato so'rov, 404 — Topilmadi, 500 — Server xatosi."
    },
    {
        "text": "Frontend va Backend o'rtasida ma'lumot almashish uchun eng keng tarqalgan universal format qaysi?",
        "a": "MP3",
        "b": "JSON (JavaScript Object Notation)",
        "c": "EXE",
        "d": "PNG",
        "e": "DOCX",
        "correct": "B",
        "topic": "JSON Ma'lumotlar Formati",
        "expl": "JSON — yengil, o'qilishi oson va barcha dasturlash tillari tomonidan tushuniladigan kalit-qiymat ma'lumot formatidir."
    },
    {
        "text": "Brauzer begona domendagi backend API ga murojaat qilganda 'CORS Error' chiqsa, sabab nima bo'ladi?",
        "a": "Kompyuter ekrani singan bo'ladi.",
        "b": "Server javob sarlavhasida `Access-Control-Allow-Origin` ruxsatnomasi belgilanmagan bo'ladi.",
        "c": "Faqat internet kabeli uzilgan bo'ladi.",
        "d": "Klaviaturadagi til noto'g'ri tanlangan bo'ladi.",
        "e": "HTML teglari katta harflarda yozilgan bo'ladi.",
        "correct": "B",
        "topic": "CORS Xavfsizligi va Sarlavhalar",
        "expl": "CORS (Cross-Origin Resource Sharing) xavfsizlik mexanizmi bo'lib, backend boshqa domenlarga ruxsat berishini talab qiladi."
    },
    {
        "text": "Node.js platformasida Express freymvorki yordamida veb-server yaratish va portni tinglash kodi qaysi?",
        "a": "server.start(html);",
        "b": "const express = require('express'); const app = express(); app.listen(3000);",
        "c": "window.openPort(3000);",
        "d": "css.createServer();",
        "e": "database.connect('port3000');",
        "correct": "B",
        "topic": "Node.js va Express Asoslari",
        "expl": "Express — Node.js uchun eng mashhur minimalistik freymvork bo'lib, `app.listen()` bilan kiruvchi ulanishlarni qabul qiladi."
    },
    {
        "text": "Express ilovasida kiruvchi JSON so'rov tanasini (`req.body`) o'qish uchun qaysi Middleware ulanishi shart?",
        "a": "app.use(express.static('images'));",
        "b": "app.use(express.json());",
        "c": "app.clear();",
        "d": "app.close();",
        "e": "app.exit();",
        "correct": "B",
        "topic": "Express Middleware (express.json)",
        "expl": "`express.json()` oqimdan kelayotgan JSON baytlarini avtomatik JavaScript obyektiga (`req.body`) aylantirib beradi."
    },
    {
        "text": "Relyatsion ma'lumotlar bazasida (SQLite/PostgreSQL) jadvaldagi har bir qatorni takrorlanmas qiluvchi ustun nima deyiladi?",
        "a": "Foreign Key",
        "b": "Primary Key (Birlamchi Kalit / `id PRIMARY KEY AUTOINCREMENT`)",
        "c": "Text Field",
        "d": "Comment Line",
        "e": "Border Radius",
        "correct": "B",
        "topic": "Primary Key Relyatsion Baza",
        "expl": "Primary Key har bir yozuvning unikal identifikatori bo'lib, qatorlarni chalkashmasdan topish uchun xizmat qiladi."
    },
    {
        "text": "SQL tilida 'users' jadvalidan 18 yoshdan katta bo'lgan barcha foydalanuvchilarni tanlab olish so'rovi qaysi?",
        "a": "FIND users AGE > 18;",
        "b": "SELECT * FROM users WHERE age > 18;",
        "c": "GET ALL users IF age 18;",
        "d": "DELETE FROM users WHERE age > 18;",
        "e": "UPDATE users SET age = 18;",
        "correct": "B",
        "topic": "SQL So'rovlari (SELECT WHERE)",
        "expl": "`SELECT * FROM users WHERE age > 18;` SQL ning klassik qidiruv va filtrlash operatoridir."
    },
    {
        "text": "Buyurtmalar (orders) jadvalini foydalanuvchilar (users) jadvali bilan bog'lash uchun nima ishlatiladi?",
        "a": "Tasodifiy sonlar",
        "b": "Tashqi Kalit (Foreign Key / masalan, `orders.user_id = users.id`) va `JOIN` amali.",
        "c": "Faqat foydalanuvchi ismi",
        "d": "CSS stillari",
        "e": "Bunday jadvallarni bog'lab bo'lmaydi",
        "correct": "B",
        "topic": "Foreign Keys va SQL JOIN",
        "expl": "Foreign Key (Tashqi kalit) ikki jadval o'rtasidagi relyingiy bog'liqlikni yaratadi va ma'lumotlar yaxlitligini ta'minlaydi."
    },
    {
        "text": "MVC (Model-View-Controller) arxitekturasida ma'lumotlar bazasi bilan to'g'ridan-to'g'ri ishlovchi qism qaysi?",
        "a": "View (Ko'rinish)",
        "b": "Model (Model)",
        "c": "Controller (Nazoratchi)",
        "d": "Router",
        "e": "CSS Stili",
        "correct": "B",
        "topic": "MVC Arxitekturasi",
        "expl": "Model — ma'lumotlar strukturasi va bazaviy operatsiyalar uchun mas'ul; Controller esa so'rovlarni boshqaradi; View — interfeys."
    },
    {
        "text": "Foydalanuvchi parollarini ma'lumotlar bazasida xavfsiz saqlash uchun qaysi texnologiya standart hisoblanadi?",
        "a": "Ochiq matn (plaintext) sifatida saqlash",
        "b": "`bcrypt` yoki `Argon2` orqali tuzlangan (salted) kriptografik xesh yaratish.",
        "c": "Parolni faqat teskarisiga o'girib yozish",
        "d": "Parolni rasmlar ichiga yashirish",
        "e": "Parolni faqat ekranda saqlash",
        "correct": "B",
        "topic": "Xavfsiz Autentifikatsiya va bcrypt",
        "expl": "`bcrypt` sekin ishlovchi tuzlangan xesh-funksiya bo'lib, ma'lumotlar bazasi sizib chiqqanda ham parollarni ochishga yo'l qo'ymaydi."
    },
    {
        "text": "JWT (JSON Web Token) ning asosiy ustunligi nimada?",
        "a": "U faqat bitta kompyuterda ishlaydi.",
        "b": "Stateless (holatsiz) arxitektura: server barcha sessiyalarni RAM da saqlamasdan, foydalanuvchi huquqlarini raqamli imzo orqali mustaqil tekshiradi.",
        "c": "U saytdagi barcha reklamalarni o'chiradi.",
        "d": "U kompyuter xotirasini bo'shatadi.",
        "e": "JWT faqat CSS da ishlaydi.",
        "correct": "B",
        "topic": "JWT Stateless Autentifikatsiya",
        "expl": "JWT serverga har bir so'rovda foydalanuvchi ma'lumotlarini bazadan qayta qidirmasdan, imzo orqali tekshirish imkonini beradi."
    },
    {
        "text": "Ma'lumotlar bazasi paroli va maxfiy JWT kalitlarini GitHub ga tasodifan chiqib ketishidan qanday himoyalanamiz?",
        "a": "Parollarni kodning eng pastiga yozish orqali.",
        "b": "Ularni `.env` faylida saqlab, `.gitignore` ro'yxatiga `.env` ni kiritish orqali.",
        "c": "Kodni butunlay o'chirib tashlash orqali.",
        "d": "Faqat kompyuterni o'chirish orqali.",
        "e": "Fayl nomini o'zgartirish orqali.",
        "correct": "B",
        "topic": ".env va .gitignore Xavfsizligi",
        "expl": "Maxfiy sozlamalar muhit o'zgaruvchilari (`process.env`) orqali olinadi va hech qachon Git repozitoriyga qo'shilmaydi."
    },
    {
        "text": "AI Bug Hunter rejimida dastur kodidagi qiyin xatolarni tuzatishda qaysi axborot eng muhim hisoblanadi?",
        "a": "Dasturchining kayfiyati.",
        "b": "To'liq Stack Trace (xato yuz bergan fayl nomi, qator raqami va xatolik turi) hamda tegishli kod parchasi.",
        "c": "Kompyuterning narxi.",
        "d": "Faqat saytning bosh sahifasi rasmi.",
        "e": "Faqat terminalning fon rangi.",
        "correct": "B",
        "topic": "AI Debugging va Stack Trace",
        "expl": "Stack trace xatoning kelib chiqish manzilini aniq ko'rsatadi, bu esa AI ga bir zumda to'g'ri patch yozish imkonini beradi."
    },
    {
        "text": "Git versiya nazoratida yangi funksiyani alohida tarmoqda xavfsiz yozish buyrug'i qaysi?",
        "a": "git delete-all",
        "b": "git checkout -b feature/auth",
        "c": "git stop",
        "d": "git clear-branch",
        "e": "git reload",
        "correct": "B",
        "topic": "Git Branching (Tarmoqlanish)",
        "expl": "`git checkout -b <nom>` yangi mustaqil tarmoq (branch) ochadi, asosiy kodni buzmasdan yangi funksiyalar qo'shish imkonini beradi."
    },
    {
        "text": "GitHub da Pull Request (PR) ning asosiy vazifasi nima?",
        "a": "Do'stlarga xabar yuborish.",
        "b": "O'z tarmog'ingizdagi kodni asosiy tarmoqqa (main) qo'shishdan oldin jamoa a'zolari bilan ko'rib chiqish (Code Review) va muhokama qilish.",
        "c": "Litsenziya sotib olish.",
        "d": "GitHub hisobini o'chirish.",
        "e": "Faqat kompyuter ekranini suratga olish.",
        "correct": "B",
        "topic": "Pull Request va Code Review",
        "expl": "Pull Request professional jamoalarda sifat nazorati bo'lib, xatolarni ishlab chiqarishga chiqishidan oldin aniqlaydi."
    },
    {
        "text": "CI/CD (Continuous Integration / Continuous Deployment) da GitHub Actions qanday vazifani bajaradi?",
        "a": "Faqat foydalanuvchilar sonini hisoblaydi.",
        "b": "Har bir yangi commit yoki Pull Requestda avtomatik ravishda testlarni ishga tushirish, kod sifatini tekshirish va serverga deploy qilish.",
        "c": "Kompyuterni elektr energiyasi bilan ta'minlash.",
        "d": "Faqat videolarni yuklab olish.",
        "e": "Word hujjatlarini formatlash.",
        "correct": "B",
        "topic": "CI/CD va GitHub Actions",
        "expl": "GitHub Actions avtomatlashtirish quvuri bo'lib, inson aralashuvisiz dasturni tekshiradi, quradi va serverga joylaydi."
    },
    {
        "text": "Docker va Konteynerlashtirish nima uchun 'Mening kompyuterimda ishlagandi, serverda ishlamayapti' muammosini yo'qotadi?",
        "a": "Chunki Docker faqat bitta kompyuter turini qo'llab-quvvatlaydi.",
        "b": "Chunki u dastur kodi, kutubxonalar va operatsion tizim muhitini yagona standart izolyatsiyalangan konteynerga (Image) o'raydi.",
        "c": "Chunki Docker barcha dasturlarni o'chirib tashlaydi.",
        "d": "Chunki Docker internet tezligini 10 barobarga oshiradi.",
        "e": "Chunki u faqat rasmlarni saqlaydi.",
        "correct": "B",
        "topic": "Docker va Konteynerlar",
        "expl": "Docker dasturiy ta'minotni uning barcha bog'liqliklari bilan birga o'raydi, bu esa dasturning har qanday serverda bir xil ishlashini kafolatlaydi."
    },
    {
        "text": "Postman vositasi dasturchilarga qanday yordam beradi?",
        "a": "Elektron pochta xabarlarini o'qish uchun.",
        "b": "Backend REST API endpointlariga Frontend tayyor bo'lmasdan turib GET, POST so'rovlari yuborish, status va JSON javoblarini tekshirish uchun.",
        "c": "3D grafika chizish uchun.",
        "d": "Faqat fotosuratlarni tahrirlash uchun.",
        "e": "Kompyuter ekranini tozalash uchun.",
        "correct": "B",
        "topic": "Postman va API Testlash",
        "expl": "Postman — backend dasturchilarining asosiy vositasi bo'lib, har bir endpointning to'g'ri ishlashini tekshirish va hujjatlashtirish imkonini beradi."
    },
    {
        "text": "Full-Stack loyihani internetga chiqarishda (Production Deploy) backend qayerga joylanadi?",
        "a": "Oddiy fleshka ichiga.",
        "b": "Doimiy ishlovchi bulutli serverlarga (masalan, Render, Railway, DigitalOcean yoki AWS).",
        "c": "Faqat brauzerning xatcho'plariga.",
        "d": "Faqat o'qituvchining kompyuteriga.",
        "e": "Bunday backendni chiqarib bo'lmaydi.",
        "correct": "B",
        "topic": "Production Deploy",
        "expl": "Bulutli platformalar Node.js serverlarini 24/7 rejimida uzluksiz ishlatadi, avtomatik qayta ishga tushiradi va HTTPS bilan ta'minlaydi."
    },
    {
        "text": "Demo Day kuni o'z Full-Stack loyihangizni himoya qilishda qaysi jihat eng yuqori baholanadi?",
        "a": "Faqat slaydlar sonining ko'pligi.",
        "b": "Haqiqiy foydalanuvchi muammosini hal qiluvchi to'liq ishlaydigan Full-Stack tizim (Frontend + Backend + DB), toza kod arxitekturasi va jonli namoyish.",
        "c": "Faqat murakkab so'zlarni yoddan aytib berish.",
        "d": "Boshqa o'quvchilarning ishlarini tanqid qilish.",
        "e": "Faqat loyiha narxini baland aytish.",
        "correct": "B",
        "topic": "Demo Day va Mahsulot Himoyasi",
        "expl": "Muvaffaqiyatli Demo Day mezonlari: ishlovchi mahsulot, to'liq ma'lumotlar oqimi (Frontend-Backend-DB) va jamoaviy muhandislik salohiyati."
    }
]

QUESTIONS_9_RU = [
    {
        "text": "Как распределяются три ключевых уровня (3-Tier) в архитектуре Full-Stack разработки?",
        "a": "Монитор, Клавиатура и Мышь.",
        "b": "Frontend (Пользовательский интерфейс), Backend (Сервер и бизнес-логика) и Database (База данных).",
        "c": "HTML, CSS и системные шрифты.",
        "d": "Операционные системы Windows, Linux и MacOS.",
        "e": "Исключительно аудио, видео и изображения.",
        "correct": "B",
        "topic": "Архитектура Full-Stack",
        "expl": "Full-Stack состоит из трех уровней: клиентский браузер (Frontend), сервер вычислений (Backend) и хранилище данных (Database)."
    },
    {
        "text": "Почему составление PRD (Product Requirements Document) критически важно перед началом кодинга с AI?",
        "a": "Для составления библиотечного каталога книг.",
        "b": "Для четкой фиксации целей, структуры данных, API эндпоинтов и бизнес-правил, исключая галлюцинации и ошибки генерации кода нейросетью.",
        "c": "Для отмены традиционных языков программирования.",
        "d": "Только для печати отчетов на принтере.",
        "e": "Для искусственного завышения стоимости проекта.",
        "correct": "B",
        "topic": "PRD и Архитектура Проекта",
        "expl": "PRD служит техническим ориентиром для разработчика и нейросети, гарантируя разработку по точным инженерным спецификациям."
    },
    {
        "text": "В чем главное архитектурное преимущество CSS Grid перед Flexbox при создании панелей управления (Dashboard)?",
        "a": "CSS Grid предназначен исключительно для оформления шрифтов.",
        "b": "CSS Grid обеспечивает полноценное двухмерное управление (одновременно строки и столбцы), тогда как Flexbox работает в одном измерении.",
        "c": "CSS Grid физически ускоряет интернет-соединение.",
        "d": "Flexbox официально объявлен устаревшим.",
        "e": "Между ними нет абсолютно никакой разницы.",
        "correct": "B",
        "topic": "CSS Grid vs Flexbox",
        "expl": "Grid управляет сложными двумерными сетками ячеек, а Flexbox идеален для выравнивания элементов вдоль одной оси."
    },
    {
        "text": "Какой синтаксис асинхронного JavaScript является современным стандартом для сетевых запросов к серверу?",
        "a": "Синхронный цикл while",
        "b": "Функция `fetch()` в связке с конструкцией `async / await`.",
        "c": "Множественные диалоговые окна `alert()`",
        "d": "Десятикратный перезапуск программы",
        "e": "Ручное открытие текстового файла блокнотом",
        "correct": "B",
        "topic": "Асинхронный JS (async/await)",
        "expl": "`async/await` делает асинхронный код линейным и понятным, не блокируя пользовательский интерфейс браузера."
    },
    {
        "text": "Какой HTTP-метод архитектуры REST API используется для создания НОВОЙ записи (пользователя, заказа) в базе данных?",
        "a": "GET",
        "b": "POST",
        "c": "DELETE",
        "d": "OPTIONS",
        "e": "HEAD",
        "correct": "B",
        "topic": "Методы REST HTTP",
        "expl": "GET — чтение, POST — создание нового ресурса, PUT/PATCH — модификация, DELETE — удаление."
    },
    {
        "text": "Какой стандартный код состояния HTTP возвращает сервер, если запрашиваемый ресурс или маршрут не существует?",
        "a": "200 OK",
        "b": "404 Not Found",
        "c": "500 Internal Server Error",
        "d": "201 Created",
        "e": "301 Moved Permanently",
        "correct": "B",
        "topic": "Коды Состояния HTTP",
        "expl": "200 — Успешно, 201 — Создано, 400 — Неверный запрос, 404 — Не найдено, 500 — Ошибка на стороне сервера."
    },
    {
        "text": "Какой текстовый формат стал общепринятым мировым стандартом для обмена данными между Frontend и Backend?",
        "a": "MP3",
        "b": "JSON (JavaScript Object Notation)",
        "c": "EXE",
        "d": "PNG",
        "e": "DOCX",
        "correct": "B",
        "topic": "Формат Данных JSON",
        "expl": "JSON — компактный, человекочитаемый формат представления структурированных данных, поддерживаемый всеми языками."
    },
    {
        "text": "Что является причиной возникновения ошибки 'CORS Error' при обращении браузера к внешнему серверному API?",
        "a": "Физическая поломка матрицы монитора.",
        "b": "Отсутствие в заголовках ответа сервера разрешающей директивы `Access-Control-Allow-Origin` для стороннего домена.",
        "c": "Случайный обрыв кабеля локальной сети.",
        "d": "Неверно выбранная раскладка клавиатуры.",
        "e": "Написание тегов HTML заглавными буквами.",
        "correct": "B",
        "topic": "Безопасность CORS и Заголовки",
        "expl": "CORS защищает пользователей от несанкционированных межсайтовых запросов, требуя явного разрешения от целевого бэкенда."
    },
    {
        "text": "Как выглядит канонический код создания и запуска веб-сервера на Node.js с использованием Express?",
        "a": "server.start(html);",
        "b": "const express = require('express'); const app = express(); app.listen(3000);",
        "c": "window.openPort(3000);",
        "d": "css.createServer();",
        "e": "database.connect('port3000');",
        "correct": "B",
        "topic": "Основы Node.js и Express",
        "expl": "Express инициализирует приложение через вызов `express()` и слушает сетевой порт с помощью функции `app.listen()`."
    },
    {
        "text": "Какой модуль промежуточного слоя (Middleware) необходим в Express для парсинга входящего тела запроса в формате JSON (`req.body`)?",
        "a": "app.use(express.static('images'));",
        "b": "app.use(express.json());",
        "c": "app.clear();",
        "d": "app.close();",
        "e": "app.exit();",
        "correct": "B",
        "topic": "Express Middleware (express.json)",
        "expl": "`express.json()` автоматически парсит сырые сетевые потоки JSON и делает их доступными в виде объекта `req.body`."
    },
    {
        "text": "Как в реляционных базах данных (SQLite/PostgreSQL) называется столбец, гарантирующий уникальность каждой строки таблицы?",
        "a": "Foreign Key",
        "b": "Primary Key (Первичный Ключ / `id PRIMARY KEY AUTOINCREMENT`)",
        "c": "Text Field",
        "d": "Comment Line",
        "e": "Border Radius",
        "correct": "B",
        "topic": "Primary Key в Реляционных БД",
        "expl": "Первичный ключ уникально идентифицирует каждую запись в таблице, исключая дубликаты и путаницу данных."
    },
    {
        "text": "Каким SQL-запросом выбираются все пользователи старше 18 лет из таблицы 'users'?",
        "a": "FIND users AGE > 18;",
        "b": "SELECT * FROM users WHERE age > 18;",
        "c": "GET ALL users IF age 18;",
        "d": "DELETE FROM users WHERE age > 18;",
        "e": "UPDATE users SET age = 18;",
        "correct": "B",
        "topic": "SQL-запросы (SELECT WHERE)",
        "expl": "`SELECT * FROM users WHERE age > 18;` — фундаментальная конструкция языка SQL для выборки данных по заданному критерию."
    },
    {
        "text": "Что связывает таблицу заказов (orders) с таблицей пользователей (users) в реляционной схеме?",
        "a": "Случайные математические числа",
        "b": "Внешний Ключ (Foreign Key / например, `orders.user_id = users.id`) и операция объединения `JOIN`.",
        "c": "Только имя учетной записи пользователя",
        "d": "Стили оформления CSS",
        "e": "Таблицы невозможно связывать между собой",
        "correct": "B",
        "topic": "Foreign Keys и SQL JOIN",
        "expl": "Foreign Key создает строгую ссылочную целостность между сущностями, а JOIN объединяет их данные в одном ответе."
    },
    {
        "text": "Какой компонент в классическом паттерне MVC (Model-View-Controller) отвечает за работу с базой данных?",
        "a": "View (Представление)",
        "b": "Model (Модель)",
        "c": "Controller (Контроллер)",
        "d": "Router (Маршрутизатор)",
        "e": "Стили CSS",
        "correct": "B",
        "topic": "Архитектурный Паттерн MVC",
        "expl": "Model инкапсулирует данные и бизнес-правила БД, Controller обрабатывает входящие запросы, а View отображает UI."
    },
    {
        "text": "Какая технология признана мировым стандартом для безопасного хранения паролей пользователей в базе данных?",
        "a": "Хранение в виде открытого текста (plaintext)",
        "b": "Создание соленого криптографического хеша с помощью алгоритмов `bcrypt` или `Argon2`.",
        "c": "Запись пароля задом наперед",
        "d": "Маскировка пароля внутри изображений",
        "e": "Хранение паролей в оперативной памяти браузера",
        "correct": "B",
        "topic": "Безопасная Аутентификация и bcrypt",
        "expl": "Алгоритм `bcrypt` с солью (salt) гарантирует, что даже при утечке базы данных восстановить пароли будет невозможно."
    },
    {
        "text": "В чем заключается фундаментальное архитектурное преимущество токенов JWT (JSON Web Token)?",
        "a": "Они работают исключительно на одном компьютере.",
        "b": "Stateless-архитектура: серверу не требуется хранить сессии в ОЗУ, проверка подлинности и прав выполняется через цифровую подпись токена.",
        "c": "JWT автоматически блокирует всю рекламу в браузере.",
        "d": "JWT очищает жесткий диск от мусора.",
        "e": "Токены JWT исполняются внутри CSS-файлов.",
        "correct": "B",
        "topic": "Stateless-аутентификация JWT",
        "expl": "JWT передает полезную нагрузку и подпись вместе с запросом, освобождая сервер от хранения состояния активных сессий."
    },
    {
        "text": "Как предотвратить случайную утечку паролей базы данных и секретных ключей API в публичный репозиторий GitHub?",
        "a": "Вписывать пароли в самом низу файла программы.",
        "b": "Хранить секреты в файле `.env`, а сам файл `.env` обязательно добавлять в список игнорирования `.gitignore`.",
        "c": "Полностью удалить исходный код проекта.",
        "d": "Просто выключить компьютер.",
        "e": "Изменить расширение файла с .js на .txt.",
        "correct": "B",
        "topic": "Секреты .env и .gitignore",
        "expl": "Секретные параметры читаются из переменных окружения (`process.env`), а `.gitignore` исключает их попадание в Git."
    },
    {
        "text": "Какая информация критически необходима в режиме AI Bug Hunter для быстрого исправления сложных серверных ошибок?",
        "a": "Настроение программиста.",
        "b": "Полный стек вызовов (Stack Trace: имя файла, номер строки, тип ошибки) и проблемный фрагмент исходного кода.",
        "c": "Рыночная стоимость ноутбука.",
        "d": "Скриншот главной страницы сайта.",
        "e": "Цвет терминального окна.",
        "correct": "B",
        "topic": "AI-Debugging и Stack Trace",
        "expl": "Stack Trace указывает точное место и причину сбоя, позволяя нейросети предложить точечный и надежный фикс."
    },
    {
        "text": "Какой командой Git создается и активируется новая изолированная ветка для разработки нового функционала?",
        "a": "git delete-all",
        "b": "git checkout -b feature/auth",
        "c": "git stop",
        "d": "git clear-branch",
        "e": "git reload",
        "correct": "B",
        "topic": "Ветвление в Git (Branching)",
        "expl": "Команда `git checkout -b <name>` изолирует работу над новой функцией, сохраняя основную ветку main в стабильном виде."
    },
    {
        "text": "В чем заключается главное назначение Pull Request (PR) на платформе GitHub?",
        "a": "Для отправки мгновенных сообщений друзьям.",
        "b": "Для проверки кода (Code Review), автоматического тестирования и обсуждения изменений перед слиянием в основную ветку main.",
        "c": "Для покупки платных лицензий.",
        "d": "Для удаления аккаунта GitHub.",
        "e": "Для создания снимков экрана.",
        "correct": "B",
        "topic": "Pull Request и Code Review",
        "expl": "Pull Request обеспечивает коллективный контроль качества: команда анализирует diff и предотвращает попадание багов в продакшн."
    },
    {
        "text": "Какую ключевую роль играет сервис GitHub Actions в автоматизации процессов CI/CD?",
        "a": "Только подсчитывает суммарное число посетителей сайта.",
        "b": "Автоматически запускает сборку, прогон юнит-тестов и деплой на сервер при каждом новом коммите или Pull Request.",
        "c": "Снабжает компьютер электричеством.",
        "d": "Скачивает фильмы из интернета.",
        "e": "Форматирует текстовые документы Word.",
        "correct": "B",
        "topic": "CI/CD и GitHub Actions",
        "expl": "GitHub Actions автоматизирует пайплайн тестирования и деплоя, гарантируя высокую надежность релизов."
    },
    {
        "text": "Почему контейнеризация Docker решает известную проблему 'На моем ПК работало, а на сервере упало'?",
        "a": "Потому что Docker поддерживает строго одну модель компьютера.",
        "b": "Потому что приложение упаковывается вместе со всеми системными библиотеками, зависимостями и окружением в единый неизменяемый образ (Image).",
        "c": "Потому что Docker удаляет все ненужные программы.",
        "d": "Потому что Docker увеличивает скорость сети в 10 раз.",
        "e": "Потому что он сохраняет только картинки.",
        "correct": "B",
        "topic": "Docker и Контейнеризация",
        "expl": "Контейнер Docker создает предсказуемую и изолированную среду исполнения, одинаково работающую на любой ОС."
    },
    {
        "text": "Чем инструмент Postman незаменим для разработчиков серверных приложений?",
        "a": "Для чтения бумажных писем.",
        "b": "Для отправки тестовых HTTP-запросов (GET, POST), валидации статус-кодов и анализа JSON-ответов бэкенда до готовности фронтенда.",
        "c": "Для трехмерного моделирования.",
        "d": "Для пакетной обработки фотографий.",
        "e": "Для очистки реестра Windows.",
        "correct": "B",
        "topic": "Инструмент Postman и Тестирование API",
        "expl": "Postman позволяет отлаживать и документировать эндпоинты REST API независимо от клиентской части."
    },
    {
        "text": "Куда разворачивается серверная часть (Backend) при промышленном развертывании (Production Deploy)?",
        "a": "На обычную USB-флешку.",
        "b": "На круглосуточно работающие облачные платформы (например, Render, Railway, DigitalOcean или AWS).",
        "c": "В закладки браузера.",
        "d": "Только на рабочий ноутбук преподавателя.",
        "e": "Развертывание бэкенда невозможно.",
        "correct": "B",
        "topic": "Промышленный Деплой (Production)",
        "expl": "Облачные PaaS и VPS платформы обеспечивают непрерывную работу бэкенда 24/7, автомасштабирование и HTTPS."
    },
    {
        "text": "Что ценится выше всего экспертами и жюри при защите Full-Stack проекта на Demo Day?",
        "a": "Исключительно количество слайдов в презентации.",
        "b": "Реально работающий продукт (Frontend + Backend + Database), решающий прикладную задачу, чистый код и живая интерактивная демонстрация.",
        "c": "Механическое заучивание сложных терминов.",
        "d": "Критика проектов других участников.",
        "e": "Громкие заявления о будущей прибыли.",
        "correct": "B",
        "topic": "Demo Day и Защита Проекта",
        "expl": "Живой рабочий Full-Stack сервис с реальным обменом данными и понятной ценностью для пользователя — главный критерий победы."
    }
]

print("Grade 9 Vibecoding test data loaded (25 questions UZ & RU). Teacher: Ismoiljon Usmonov.")
