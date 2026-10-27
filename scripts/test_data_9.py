#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
9-Sinf: 25 Savolli Full-Stack Vibecoding, Tizim Arxitekturasi va Agentik Kodlash Testi
O'qituvchi: Ismoiljon Usmonov · Target International School, Yunusobod
Uzbek va Russian variantlari (5 ta variant: A, B, C, D, E)
"""

META_9_UZ = {
    "school_name": "TARGET INTERNATIONAL SCHOOL — YUNUSOBOD",
    "teacher_name": "Ismoiljon Usmonov",
    "exam_title": "9-SINF: FULL-STACK VIBECODING VA AGENTIK DASTURLASH",
    "track_title": "Full-Stack Vibecoding & DevOps Track · O'qituvchi: Ismoiljon Usmonov",
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
        {"grade": "A'lo (5)", "range": "22 – 25 ball", "desc": "Cursor Composer, Full-Stack PRD, API generatsiyasi, Docker va CI/CD bo'yicha a'lo bilim"},
        {"grade": "Yaxshi (4)", "range": "18 – 21 ball", "desc": "Backend promptlari, SQLite sxemalari va AI debugging yaxshi o'zlashtirilgan"},
        {"grade": "Qoniqarli (3)", "range": "13 – 17 ball", "desc": "Tizimli promptlar (.cursorrules) va Git diff tahlilini takrorlash lozim"},
        {"grade": "Qoniqarsiz (2)", "range": "0 – 12 ball", "desc": "Full-Stack Vibecoding asoslari qayta o'rganilishi zarur"}
    ]
}

META_9_RU = {
    "school_name": "TARGET INTERNATIONAL SCHOOL — ЮНУСАБАД",
    "teacher_name": "Исмоилжон Усмонов",
    "exam_title": "9 КЛАСС: FULL-STACK VIBECODING И АГЕНТНОЕ ПРОГРАММИРОВАНИЕ",
    "track_title": "Full-Stack Vibecoding & DevOps Track · Преподаватель: Исмоилжон Усмонов",
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
        {"grade": "Отлично (5)", "range": "22 – 25 баллов", "desc": "Глубокие знания Cursor Composer, Full-Stack PRD, генерации API, Docker и CI/CD"},
        {"grade": "Хорошо (4)", "range": "18 – 21 балл", "desc": "Хорошее понимание бэкенд-промптинга, схем SQLite и AI-отладки"},
        {"grade": "Удовлетворительно (3)", "range": "13 – 17 баллов", "desc": "Требуется повторение системных инструкций (.cursorrules) и анализа diff"},
        {"grade": "Неудовлетворительно (2)", "range": "0 – 12 баллов", "desc": "Необходимо повторное изучение основ Full-Stack Vibecoding"}
    ]
}

QUESTIONS_9_UZ = [
    {
        "text": "Full-Stack Vibecoding nima va uning an'anaviy dasturchi ishidan asosiy farqi nimada?",
        "a": "Dasturchi faqat tayyor CMS lardan foydalanadi.",
        "b": "Dasturchi tizim arxitektori sifatida harakat qiladi: PRD yozadi, AI agentlarga (Cursor Composer, Claude Code) Frontend, Backend va Baza kodini generatsiya qildiradi va integratsiyani boshqaradi.",
        "c": "Faqat ma'lumotlar bazasini qo'lda to'ldirish bilan shug'ullanadi.",
        "d": "Klaviaturadan butunlay voz kechadi.",
        "e": "Faqat ingliz tilidagi maqolalarni tarjima qiladi.",
        "correct": "B",
        "topic": "Full-Stack Vibecoding Mohiyati",
        "expl": "Vibecoder 3-Tier arxitekturani AI agentlar yordamida loyihalaydi, kod yozish tezligini 5-10 barobarga oshiradi."
    },
    {
        "text": "Cursor Composer rejimining (`Cmd+I` / `Ctrl+I`) oddiy chatdan tub farqi nimada?",
        "a": "U faqat bitta faylni o'qiy oladi.",
        "b": "U bir vaqtning o'zida butun loyihaning o'nlab fayllari bo'ylab (Frontend, Backend, DB sxemasi) avtonom o'zgartirishlar kiritadi va yangi fayllarni yaratadi.",
        "c": "U kompyuterni o'chirib qo'yadi.",
        "d": "U faqat fotosuratlarni tahrirlaydi.",
        "e": "U internet aloqasisiz ishlaydi.",
        "correct": "B",
        "topic": "Cursor Composer va Ko'p Faylli Tahrir",
        "expl": "Composer butun repozitoriy kontekstini tushunib, bir nechta fayllar orasidagi o'zgarishlarni sinxron amalga oshiradi."
    },
    {
        "text": "Loyiha ildizidagi `.cursorrules` (yoki `AGENTS.md`) fayli qanday strategik vazifani bajaradi?",
        "a": "O'yin ballarini saqlash uchun xizmat qiladi.",
        "b": "AI uchun doimiy qoidalar va konstitutsiya vazifasini o'taydi: loyiha arxitekturasi, kodlash uslubi, taqiqlangan kutubxonalar va xavfsizlik talablarini belgilaydi.",
        "c": "Faqat brauzer tarixini tozalaydi.",
        "d": "Kompyuter ekranining rangini boshqaradi.",
        "e": "Word fayllarini avtomatik chop etadi.",
        "correct": "B",
        "topic": "Tizimli Promptlar (.cursorrules)",
        "expl": "`.cursorrules` har bir promptga avtomatik qo'shilib, AI ning loyiha standartlaridan chetga chiqmasligini ta'minlaydi."
    },
    {
        "text": "Full-Stack loyihani boshlashda PRD (Product Requirements Document) yozishda AI dan qanday foydalaniladi?",
        "a": "AI ga 'Menga ijtimoiy tarmoq qil' deb yozib kutish.",
        "b": "Xom g'oyani berib, undan foydalanuvchi rollari, ma'lumotlar modellari (ERD), REST API endpointlari va xavfsizlik cheklovlari bo'yicha batafsil texnik topshiriq tuzishni so'rash.",
        "c": "Faqat rasmlar ro'yxatini tuzish.",
        "d": "Dasturchilarning telefon raqamlarini to'plash.",
        "e": "Faqat narxlar ro'yxatini yozdirish.",
        "correct": "B",
        "topic": "AI Bilan PRD Tuzish",
        "expl": "Strukturaviy PRD dasturchi va AI uchun aniq reja yaratadi, loyiha davomida chalkashliklarni yo'qotadi."
    },
    {
        "text": "AI ga relyatsion ma'lumotlar bazasi (SQLite/PostgreSQL) sxemasini yaratishda qanday prompt beriladi?",
        "a": "'Menga baza qilib ber.'",
        "b": "'E-tijorat tizimi uchun Users, Products va Orders jadvallarining SQL DDL sxemasini yoz. Birlamchi kalitlar (PK), tashqi kalitlar (FK), indekslar va kaskadli o'chirish qoidalarini aniq belgilab ber.'",
        "c": "'Barcha foydalanuvchilar parolini ekranga chiqar.'",
        "d": "'Faqat jadval nomlarini sanab ber.'",
        "e": "'Bazani o'chirib tashla.'",
        "correct": "B",
        "topic": "AI Bilan SQL Sxema Loyihalash",
        "expl": "Jadvallararo bog'liqliklar (1:N, M:N) va cheklovlar ko'rsatilgan prompt mustahkam relyatsion sxema generatsiya qiladi."
    },
    {
        "text": "Express.js da REST API routerlarini AI ga yozdirishda qaysi talab kiritilishi shart?",
        "a": "Faqat bitta URL manzili bo'lishi.",
        "b": "Barcha CRUD operatsiyalari (GET, POST, PUT, DELETE), to'g'ri HTTP status kodlari (200, 201, 400, 404, 500) va kiruvchi ma'lumotlarni validatsiya qilish mantiqi bo'lishi.",
        "c": "Faqat CSS stillari ishlatilishi.",
        "d": "Parollarni ochiq ko'rinishda uzatish.",
        "e": "Hech qanday xatolik qaytarmaslik.",
        "correct": "B",
        "topic": "REST API Endpointlari Prompti",
        "expl": "Mukammal API prompti HTTP metodlari, status kodlari va xatoliklarni ushlaydigan `try/catch` bloklarini o'z ichiga oladi."
    },
    {
        "text": "AI yordamida foydalanuvchi autentifikatsiyasini yaratishda qaysi xavfsizlik cheklovi (Constraint) qat'iy beriladi?",
        "a": "Parollarni oddiy matn sifatida bazaga yozish.",
        "b": "'Parollarni faqat bcrypt (salt round = 10) bilan xeshla, sessiyani esa maxfiy kalit bilan imzolangan JWT token orqali stateless boshqar.'",
        "c": "Har bir foydalanuvchiga bir xil parol berish.",
        "d": "Autentifikatsiyani umuman ishlatmaslik.",
        "e": "Faqat monitor orqali tekshirish.",
        "correct": "B",
        "topic": "Xavfsiz Auth va JWT Promptlari",
        "expl": "AI ga xavfsizlik cheklovi berilmasa, u oson lekin zaif kod yozib qo'yishi mumkin. Aniq bcrypt va JWT talabi berilishi shart."
    },
    {
        "text": "AI yozgan kodda Git Diff (o'zgarishlar farqi) paydo bo'lganda, Vibecoder nima qilishi shart?",
        "a": "O'qimasdan darhol 'Accept All' tugmasini bosish.",
        "b": "Diffni diqqat bilan ko'rib chiqish (qaysi satrlar qo'shildi, nimalar o'chirildi), yashirin xato yoki keraksiz o'chirishlar yo'qligini tekshirib, keyin qabul qilish.",
        "c": "Barcha o'zgarishlarni darhol bekor qilish.",
        "d": "Kompyuterni o'chirib qo'yish.",
        "e": "Faqat birinchi qatorni o'qish.",
        "correct": "B",
        "topic": "Git Diff Auditi va Nazorat",
        "expl": "Vibecoder AI taklif qilgan har bir o'zgarishga mas'uldir; diffni o'qib tasdiqlash xatolarning oldini oladi."
    },
    {
        "text": "AI Bug Hunter rejimida kutilmagan asinxron xato (masalan, `UnhandledPromiseRejection`) chiqsa, qanday prompt beriladi?",
        "a": "'Menga yangi server ber.'",
        "b": "'Mana xato yuz bergan Express controller kodi va to'liq terminal stack trace: [...]. Qaysi asinxron funksiya `await` qilinmagan yoki xatosi ushlanmaganini tahlil qil va fix ber.'",
        "c": "'Barcha ma'lumotlar bazasini o'chir.'",
        "d": "'Saytni qora rangga bo'ya.'",
        "e": "'Faqat HTML faylni ko'rsat.'",
        "correct": "B",
        "topic": "Asinxron Xatolarni AI Bilan Tuzatish",
        "expl": "Stack trace va controller kodi taqdim etilganda AI yetishmayotgan `try/catch` yoki unutib qoldirilgan `await` ni bir zumda topadi."
    },
    {
        "text": "Backend API ni sinash uchun Postman kolleksiyasini yaratishda AI dan qanday foydalaniladi?",
        "a": "AI ga Postman dasturini o'chirishni buyurish.",
        "b": "AI ga Express marshrutlar faylini berib, 'Ushbu API uchun import qilishga tayyor Postman Collection v2.1 JSON faylini tuzib ber' deb so'rash.",
        "c": "Faqat bitta URL yozdirish.",
        "d": "Faqat rasm chizdirish.",
        "e": "Bunday narsani AI qila olmaydi.",
        "correct": "B",
        "topic": "Postman Kolleksiyasini Generatsiya Qilish",
        "expl": "AI API spetsifikatsiyasi bo'yicha tayyor Postman JSON kolleksiyasini generatsiya qilib, qo'lda terish vaqtini tejaydi."
    },
    {
        "text": "Loyiha uchun ko'p bosqichli (Multi-stage) Dockerfile yaratishda AI ga qanday talab qo'yiladi?",
        "a": "'Dockerfile hajmi 10 gigabayt bo'lsin.'",
        "b": "'Node.js ilovasi uchun ishlab chiqarishga mo'ljallangan yengil Alpine asosidagi multi-stage Dockerfile yoz: devDependencies ni yakuniy konteynerga kiritma va root bo'lmagan foydalanuvchi bilan ishlat.'",
        "c": "'Faqat bitta qatordan iborat bo'lsin.'",
        "d": "'Barcha fayllarni o'chirib tashlasin.'",
        "e": "'Faqat Windows da ishlasin.'",
        "correct": "B",
        "topic": "Docker Konteynerlashtirish Prompti",
        "expl": "Multi-stage Dockerfile tasvir hajmini bir necha barobarga qisqartiradi va xavfsizlikni oshiradi."
    },
    {
        "text": "AI yordamida avtomatik testlar (Unit Tests / Jest) yozdirishning eng katta afzalligi nimada?",
        "a": "Kodni umuman ishlatmasdan tekshirish.",
        "b": "AI funksiyaning normal ishlashini hamda chekka holatlarni (noto'g'ri parol, bo'sh parametrlar, cheksiz sonlar) qamrab oluvchi 20 ta testni 10 soniyada yozib beradi.",
        "c": "Kompyuter xotirasini bo'shatadi.",
        "d": "Faqat bir martalik alert oynalarini ochadi.",
        "e": "Testlar dasturni sekinlashtiradi.",
        "correct": "B",
        "topic": "Avtomatik Testlar Generatsiyasi",
        "expl": "Testlarni AI ga yozdirish kodning mustahkamligini kafolatlaydi va kelajakdagi regressiyalarni to'xtatadi."
    },
    {
        "text": "GitHub Actions orqali avtomatik CI/CD pipeline yaratishda AI dan qanday yordam olinadi?",
        "a": "Faqat yangiliklar lentasini o'qish.",
        "b": "AI ga `.github/workflows/deploy.yml` faylini tuzdirib, har bir push da testlarni o'tkazish, Docker tasvirini qurish va serverga avto-deploy qilishni sozlash.",
        "c": "GitHub hisobini o'chirish.",
        "d": "Faqat rasm yuklash.",
        "e": "Klaviaturani tozalash.",
        "correct": "B",
        "topic": "GitHub Actions CI/CD Prompti",
        "expl": "GitHub Actions yaml faylini AI orqali sozlash murakkab deploy jarayonini 1 daqiqada avtomatlashtiradi."
    },
    {
        "text": "AI tomonidan taklif qilingan kodda xavfli SQL Injection zaifligi borligini qanday payqaysiz?",
        "a": "Kod qora rangda yozilgan bo'lsa.",
        "b": "Agar AI parametrlangan so'rov o'rniga foydalanuvchi ma'lumotini to'g'ridan-to'g'ri SQL satriga qo'shgan bo'lsa (`SELECT * FROM users WHERE id = ' + req.body.id`).",
        "c": "Kodda raqamlar ko'p bo'lsa.",
        "d": "Fayl nomi kichik harflarda bo'lsa.",
        "e": "Bunday zaiflikni aniqlab bo'lmaydi.",
        "correct": "B",
        "topic": "AI Kodida Xavfsizlik Auditi",
        "expl": "Vibecoder AI kodini doimo ko'zdan kechiradi: qatorlarni ulash (string concatenation) o'rniga parametrlangan so'rovlarni talab qiladi."
    },
    {
        "text": "Frontend da React/Next.js komponentlarini Backend API bilan bog'lashda AI ga qanday prompt beriladi?",
        "a": "'Menga veb-sahifa och.'",
        "b": "'Express backendimizdagi `/api/products` endpointidan ma'lumot oluvchi, yuklanish holati, xatoliklar paneli va savatga qo'shish funksiyasiga ega React komponentini yoz.'",
        "c": "'Faqat HTML tugmasini chiz.'",
        "d": "'Kompyuterni o'chir.'",
        "e": "'Faqat fon rangini o'zgartir.'",
        "correct": "B",
        "topic": "Full-Stack Integratsiya Prompti",
        "expl": "Frontend komponenti backend ma'lumotlar oqimiga bog'langanda to'liq ishlaydigan interaktiv mahsulot hosil bo'ladi."
    },
    {
        "text": "Loyiha hajmi kattalashganda AI ga kontekst yetmay qolmasligi uchun qanday strategiya qo'llaniladi?",
        "a": "Barcha fayllarni bitta ulkan faylga birlashtirish.",
        "b": "Modulli arxitektura: loyihani aniq qatlamlarga (routes, controllers, models, utils) bo'lish va AI ga faqat ayni damda kerakli fayllarni uzatish.",
        "c": "AI ishlatishni to'xtatish.",
        "d": "Fayllarning yarmini o'chirib tashlash.",
        "e": "Faqat rasmlar bilan ishlash.",
        "correct": "B",
        "topic": "Katta Loyihalarda Kontekst Boshqaruvi",
        "expl": "Modulli tizimda kontekst oynasi to'lib ketmaydi va AI diqqati faqat tahrirlanayotgan modulga qaratiladi."
    },
    {
        "text": "AI ga ma'lumotlar bazasini to'ldirish uchun 'Seed Data' generatsiya qildirish nima beradi?",
        "a": "Baza hajmini buzib qo'yadi.",
        "b": "Dasturchiga 100 ta realistik foydalanuvchi, 50 ta mahsulot va buyurtmalar tarixini avtomatik generatsiya qilib, testlashni osonlashtiradi.",
        "c": "Kompyuter tezligini nolga tushiradi.",
        "d": "Faqat bir dona qator yozadi.",
        "e": "Bunday skriptlarni ishlatib bo'lmaydi.",
        "correct": "B",
        "topic": "Database Seed Skriptlari",
        "expl": "Seed skriptlari ilovani bo'sh emas, to'laqonli real ma'lumotlar bilan sinovdan o'tkazish imkonini beradi."
    },
    {
        "text": "AI Code Review (Kodni Ko'rikdan O'tkazish) so'rovi qanday tuziladi?",
        "a": "'Kodim yaxshimi?'",
        "b": "'Ushbu Pull Request diffini Senior Full-Stack Architect sifatida ko'rib chiq: xavfsizlik zaifliklari, unumdorlik (N+1 query muammolari) va kod tozaligi bo'yicha tavsiyalaringni ber.'",
        "c": "'Kodni o'chirib tashla.'",
        "d": "'Faqat maqtov yoz.'",
        "e": "'Faqat shrift nomini ayt.'",
        "correct": "B",
        "topic": "AI Bilan Code Review",
        "expl": "AI ni qattiqqo'l arxitektor roliga qo'yish koddagi yashirin unumdorlik va xavfsizlik nuqsonlarini topishga yordam beradi."
    },
    {
        "text": "AI yozgan murakkab SQL so'rovini optimallashtirish uchun qanday prompt beriladi?",
        "a": "'SQL ni yo'qot.'",
        "b": "'Ushbu sekin ishlayotgan JOIN so'rovining `EXPLAIN QUERY PLAN` tahlilini hisobga olgan holda, kerakli ustunlarga B-Tree indekslar qo'sh va so'rovni qayta yoz.'",
        "c": "'Barcha qatorlarni o'chir.'",
        "d": "'Faqat bitta jadval qoldir.'",
        "e": "'SQL o'rniga rasm chiz.'",
        "correct": "B",
        "topic": "SQL Optimizatsiya va Indekslar",
        "expl": "Indekslar va so'rovni optimallashtirish ma'lumotlar bazasining millionlab qatorlar ustida ham soniyaning ulushlarida ishlashini ta'minlaydi."
    },
    {
        "text": "Vibecoding jarayonida 'Speculative Execution & Rollback' (Sinov va orqaga qaytish) qanday amalga oshiriladi?",
        "a": "Kompyuterni o'chirib yoqish orqali.",
        "b": "Yangi g'oyani alohida Git tarmog'ida AI ga qildirib ko'rish, agar natija kutilganidek bo'lmasa, `git reset` yoki tarmoqni o'chirish orqali toza holatga qaytish.",
        "c": "Barcha fayllarni bittalab qo'lda o'chirish orqali.",
        "d": "Faqat bir marta kod yozish bilan cheklanish orqali.",
        "e": "Klaviaturani almashtirish orqali.",
        "correct": "B",
        "topic": "Git Bilan Xavfsiz Sinovlar",
        "expl": "Git tarmoqlari (branches) Vibecoderga qo'rqmasdan har qanday dadil g'oyani sinab ko'rish va xato bo'lsa darhol orqaga qaytish erkinligini beradi."
    },
    {
        "text": "Freelance bozorida Full-Stack Vibecoder an'anaviy dasturchiga qaraganda qanday katta ustunlikka ega?",
        "a": "U umuman uxlamaydi.",
        "b": "Buyurtmachi talabini bir necha soatda to'liq ishlaydigan MVP prototipiga aylantira oladi va loyihani 5 barobar tezroq topshiradi.",
        "c": "U faqat tekin ishlaydi.",
        "d": "U kompyutersiz ishlaydi.",
        "e": "Hech qanday ustunligi yo'q.",
        "correct": "B",
        "topic": "Vibecoding va Freelance Tezligi",
        "expl": "AI bilan qurollangan dasturchi buyurtmalarni an'anaviy ishlab chiquvchilardan ancha tez va sifatli amalga oshiradi."
    },
    {
        "text": "Upwork yoki Fiverr platformasida mijoz buyurtmasiga kuchli taklif (Proposal) yozishda AI dan qanday foydalaniladi?",
        "a": "Mijozga standart 'Meni ishga ol' spamini yuborish uchun.",
        "b": "Mijozning muammosini tahlil qilib, unga loyihani qanday texnologiyalar bilan tez va sifatli yechish rejasini (Step-by-step roadmap) taklif qiluvchi shaxsiy xat yozdirish.",
        "c": "Faqat eng past narxni taklif qilish uchun.",
        "d": "Mijozni aldash uchun.",
        "e": "Faqat rasm yuborish uchun.",
        "correct": "B",
        "topic": "AI Bilan Professional Taklif (Proposal)",
        "expl": "Mijoz muammosiga yo'naltirilgan va aniq texnik yechim taklif qiluvchi maktub ishni yutib olish ehtimolini keskin oshiradi."
    },
    {
        "text": "Full-Stack loyihani Render yoki Railway platformasiga Production Deploy qilishda qaysi muhim parametr sozlanadi?",
        "a": "Faqat kompyuter ekranining o'lchami.",
        "b": "Environment Variables (Muhit o'zgaruvchilari: `PORT`, `DATABASE_URL`, `JWT_SECRET`) boshqaruv panelida to'g'ri kiritilishi.",
        "c": "Klaviaturaning modeli.",
        "d": "Faqat bosh sahifa sarlavhasi.",
        "e": "Bunday sozlama mavjud emas.",
        "correct": "B",
        "topic": "Production Atrof-muhit Sozlamalari",
        "expl": "Bulutli platformalarda sirlar va ulanish parametrlari xavfsiz Environment Variables orqali uzatiladi."
    },
    {
        "text": "Loyiha taqdimotida (Demo Day) hakamlar oldida qaysi ko'rsatkich dasturchining haqiqiy muhandislik darajasini isbotlaydi?",
        "a": "Faqat slaydlar sonining ko'pligi.",
        "b": "Jonli ishlayotgan Full-Stack arxitekturasi: mijoz ro'yxatdan o'tishi, ma'lumotlar bazasiga yozilishi, real-vaqtda yangilanishi va toza kod strukturasining mavjudligi.",
        "c": "Faqat qimmat kiyim kiyib chiqish.",
        "d": "Boshqa loyihalarni yomonlash.",
        "e": "Faqat nazariy atamalarni yoddan aytib berish.",
        "correct": "B",
        "topic": "Demo Day va Mahsulot Himoyasi",
        "expl": "Jonli, xatosiz ishlayotgan to'liq Full-Stack mahsulot (Frontend + Backend + DB) eng oliy natijadir."
    },
    {
        "text": "9-sinf o'quvchisi uchun professional Vibecoder darajasiga erishishning asosiy formulasini nima belgilaydi?",
        "a": "AI yozgan hamma narsani tushunmasdan qabul qilish.",
        "b": "Chuqur muhandislik tushunchasi (qanday ishlashini bilish) + AI vositalarini ustalik bilan boshqarish + tizimli testlash va mas'uliyat.",
        "c": "Faqat ijtimoiy tarmoqlardagi trendlarni kuzatish.",
        "d": "Faqat bitta dasturlash tilini bilish.",
        "e": "Dasturlashni butunlay tashlab ketish.",
        "correct": "B",
        "topic": "Professional Vibecoder Formulari",
        "expl": "Eng kuchli vibecoderlar AI ga buyruq berishdan oldin tizim qanday ishlashini tushunadigan muhandislardir."
    }
]

QUESTIONS_9_RU = [
    {
        "text": "В чем заключается фундаментальная суть Full-Stack Vibecoding?",
        "a": "В использовании готовых конструкторов сайтов без знания кода.",
        "b": "Разработчик выступает архитектором системы: составляет PRD, направляет AI-агентов (Cursor Composer, Claude Code) на генерацию Frontend, Backend и БД и руководит интеграцией.",
        "c": "Исключительно в ручном заполнении строк в базе данных.",
        "d": "В полном отказе от монитора и клавиатуры.",
        "e": "Только в переводе технической документации.",
        "correct": "B",
        "topic": "Суть Full-Stack Vibecoding",
        "expl": "Vibecoder проектирует 3-уровневую архитектуру вместе с AI, увеличивая скорость выпуска продукта в 5–10 раз."
    },
    {
        "text": "В чем принципиальное отличие режима Cursor Composer (`Cmd+I` / `Ctrl+I`) от стандартного чата?",
        "a": "Composer умеет работать строго с одним файлом.",
        "b": "Composer автономно правит десятки взаимосвязанных файлов проекта одновременно (Frontend, Backend, схемы БД) и создает новые модули в рамках одной задачи.",
        "c": "Composer выключает питание компьютера.",
        "d": "Composer предназначен только для редактирования растровых картинок.",
        "e": "Composer работает без подключения к сети.",
        "correct": "B",
        "topic": "Cursor Composer и Мультифайловое Редактирование",
        "expl": "Composer удерживает в контексте всю структуру репозитория и выполняет синхронные правки между слоями приложения."
    },
    {
        "text": "Какую стратегическую задачу выполняет файл `.cursorrules` (или `AGENTS.md`) в корне проекта?",
        "a": "Служит таблицей рекордов игры.",
        "b": "Является неизменяемой 'конституцией' для нейросетей: задает стек, стиль кодирования, структуру архитектуры, запрещенные библиотеки и требования безопасности.",
        "c": "Очищает историю веб-браузера.",
        "d": "Управляет частотой обновления монитора.",
        "e": "Печатает отчеты на принтере.",
        "correct": "B",
        "topic": "Системные Инструкции (.cursorrules)",
        "expl": "Файл правил незримо подмешивается к каждому промпту, гарантируя соблюдение стандартов команды."
    },
    {
        "text": "Как использовать искусственный интеллект для составления PRD (Product Requirements Document)?",
        "a": "Написать модели: 'Сделай мне социальную сеть' и ждать чудо.",
        "b": "Передать концепцию и запросить подробное ТЗ: роли пользователей, модели данных (ERD), маршруты REST API, логику валидации и граничные сценарии.",
        "c": "Только для поиска картинок.",
        "d": "Для сбора телефонных номеров.",
        "e": "Исключительно для расчета стоимости хостинга.",
        "correct": "B",
        "topic": "Составление PRD с Помощью AI",
        "expl": "Структурированный PRD исключает двусмысленность и служит четкой дорожной картой для автономных AI-агентов."
    },
    {
        "text": "Какой промпт создаст надежную реляционную схему базы данных (SQLite/PostgreSQL)?",
        "a": "'Сделай мне базу.'",
        "b": "'Спроектируй схему SQL DDL для e-commerce: таблицы Users, Products, Orders. Задай первичные ключи (PK), внешние ключи (FK), индексы и каскадное удаление.'",
        "c": "'Выведи все пароли пользователей на экран.'",
        "d": "'Просто перечисли названия таблиц.'",
        "e": "'Удали базу данных.'",
        "correct": "B",
        "topic": "Проектирование Схемы БД через AI",
        "expl": "Указание внешних ключей и связей (1:N, M:N) позволяет получить готовую надежную архитектуру данных."
    },
    {
        "text": "Какое обязательное требование нужно заложить в промпт для генерации REST API на Express.js?",
        "a": "Использовать строго один URL-адрес для всего.",
        "b": "Реализовать все CRUD-операции, возвращать корректные HTTP статус-коды (200, 201, 400, 404, 500) и валидировать входящие данные в теле запроса.",
        "c": "Использовать только стили CSS.",
        "d": "Передавать пароли открытым текстом.",
        "e": "Никогда не возвращать ошибки клиенту.",
        "correct": "B",
        "topic": "Промпт для Маршрутов REST API",
        "expl": "Надежный API обязан возвращать стандартизированные коды статусов и защищаться от невалидных входных данных."
    },
    {
        "text": "Какое ключевое ограничение безопасности (Constraint) необходимо дать AI при реализации аутентификации?",
        "a": "Сохранять пароли в открытом виде.",
        "b": "'Хешируй пароли исключительно с помощью bcrypt (10 раундов соли), а сессии строй на stateless токенах JWT с проверкой подписи на сервере.'",
        "c": "Установить одинаковый пароль всем клиентам.",
        "d": "Полностью отключить проверку прав.",
        "e": "Проверять логины только визуально.",
        "correct": "B",
        "topic": "Безопасный Auth и JWT в Промптах",
        "expl": "Без явного указания bcrypt и JWT нейросеть может применить устаревшие или небезопасные методы хранения учетных записей."
    },
    {
        "text": "Что обязан сделать грамотный Vibecoder при появлении изменений в окне Git Diff от AI?",
        "a": "Слепо нажать 'Accept All' не читая.",
        "b": "Внимательно просмотреть diff (удаленные и добавленные строки), убедиться в отсутствии скрытых багов и случайного удаления нужных функций, и лишь затем подтвердить.",
        "c": "Мгновенно отклонить все правки.",
        "d": "Выключить ноутбук.",
        "e": "Прочитать только первое слово.",
        "correct": "B",
        "topic": "Аудит Изменений (Git Diff Review)",
        "expl": "Разработчик несет персональную ответственность за код в репозитории; просмотр diff защищает от нежелательных мутаций проекта."
    },
    {
        "text": "Какой промпт быстрее всего локализует асинхронную серверную ошибку (`UnhandledPromiseRejection`)?",
        "a": "'Купи мне новый сервер.'",
        "b": "'Вот код контроллера Express и полный стек ошибки из терминала: [...]. Найди, где пропущен `await` или отсутствует блок `try/catch`, и предоставь исправленный фрагмент.'",
        "c": "'Удали всю базу данных.'",
        "d": "'Перекрась сайт в темную тему.'",
        "e": "'Покажи только разметку HTML.'",
        "correct": "B",
        "topic": "Отладка Асинхронных Ошибок с AI",
        "expl": "Передача терминального стека и кода позволяет нейросети мгновенно обнаружить неперехваченный промис."
    },
    {
        "text": "Как использовать AI для автоматической генерации коллекции тестирования в Postman?",
        "a": "Попросить AI удалить Postman.",
        "b": "Передать файл маршрутов Express и попросить: 'Сгенерируй готовый к импорту JSON-файл Postman Collection v2.1 со всеми эндпоинтами, телами запросов и тестами статусов.'",
        "c": "Написать один тестовый URL.",
        "d": "Нарисовать картинку.",
        "e": "Это невозможно сделать через AI.",
        "correct": "B",
        "topic": "Генерация Коллекций Postman",
        "expl": "AI собирает готовые JSON-коллекции для Postman, экономя часы ручного заполнения запросов и заголовков."
    },
    {
        "text": "Какое инженерное требование нужно поставить AI при создании многоэтапного (Multi-stage) Dockerfile?",
        "a": "'Сделай размер контейнера больше 10 Гб.'",
        "b": "'Напиши оптимизированный многоэтапный Dockerfile на базе Alpine: отдели этап сборки от финального образа, исключи devDependencies и запускай под непривилегированным пользователем.'",
        "c": "'Напиши Dockerfile в одну строку.'",
        "d": "'Удали весь исходный код.'",
        "e": "'Сделай образ только для Windows 95.'",
        "correct": "B",
        "topic": "Оптимизация Dockerfile через AI",
        "expl": "Multi-stage сборка уменьшает вес контейнера в десятки раз и закрывает уязвимости среды сборки."
    },
    {
        "text": "В чем фундаментальная польза генерации автоматических тестов (Jest / Supertest) с помощью нейросетей?",
        "a": "В возможности никогда не запускать программу.",
        "b": "AI за 10 секунд покрывает тестами позитивные и пограничные сценарии (пустые поля, неверные пароли, огромные числа), предотвращая регрессионные баги.",
        "c": "В очистке оперативной памяти.",
        "d": "В открытии всплывающих окон alert().",
        "e": "Тесты замедляют разработку.",
        "correct": "B",
        "topic": "Генерация Юнит-Тестов (Jest)",
        "expl": "Делегирование рутинного написания тестов нейросети обеспечивает высокое покрытие кода тестами без потери времени."
    },
    {
        "text": "Как AI помогает настроить автоматический пайплайн CI/CD в GitHub Actions?",
        "a": "Только читает новости в интернете.",
        "b": "Генерирует рабочий конфигурационный файл `.github/workflows/deploy.yml` для автоматического прогона тестов, сборки Docker-образа и деплоя на сервер при каждом пуше.",
        "c": "Удаляет аккаунт на GitHub.",
        "d": "Загружает фильмы.",
        "e": "Очищает клавиатуру.",
        "correct": "B",
        "topic": "Пайплайн GitHub Actions с AI",
        "expl": "Конфигурация workflow-файлов для CI/CD с помощью AI исключает синтаксические ошибки в разметке YAML."
    },
    {
        "text": "Как по коду от AI заметить критическую уязвимость SQL Injection?",
        "a": "Если код подсвечен черным цветом.",
        "b": "Если AI вместо параметризованного запроса выполнил прямую конкатенацию пользовательского ввода в строку SQL (`SELECT * FROM users WHERE id = ' + req.body.id`).",
        "c": "Если в коде много чисел.",
        "d": "Если имя файла написано строчными буквами.",
        "e": "Такую уязвимость заметить невозможно.",
        "correct": "B",
        "topic": "Аудит Безопасности Сгенерированного Кода",
        "expl": "Vibecoder всегда контролирует безопасность: прямая склейка строк SQL категорически пресекается в пользу параметров `$1`."
    },
    {
        "text": "Какой промпт свяжет React/Next.js фронтенд с серверным API бэкенда?",
        "a": "'Открой сайт.'",
        "b": "'Напиши React-компонент каталога товаров, получающий данные с нашего бэкенда `/api/products`: реализуй состояние загрузки (Loading), обработку ошибок и добавление в корзину.'",
        "c": "'Нарисуй кнопку.'",
        "d": "'Выключи компьютер.'",
        "e": "'Поменяй цвет фона.'",
        "correct": "B",
        "topic": "Full-Stack Интеграция Клиента и Сервера",
        "expl": "Связка фронтенда с реальным бэкендом превращает разрозненные модули в живой интерактивный сервис."
    },
    {
        "text": "Какая архитектурная стратегия предотвращает переполнение контекстного окна AI при росте проекта?",
        "a": "Слияние всех файлов в один гигантский файл.",
        "b": "Модульная архитектура: четкое разделение на routes, controllers, models, utils и передача в контекст строго тех модулей, которые затрагиваются текущей задачей.",
        "c": "Полный отказ от нейросетей.",
        "d": "Удаление половины исходного кода.",
        "e": "Работа только с графикой.",
        "correct": "B",
        "topic": "Управление Контекстом в Больших Проектах",
        "expl": "Модульность изолирует контекст: AI видит ровно столько, сколько нужно для решения локальной задачи, не распыляя внимание."
    },
    {
        "text": "Какую ценность несет генерация скриптов 'Seed Data' для базы данных через AI?",
        "a": "Портит структуру таблиц.",
        "b": "Автоматически заполняет базу сотнями реалистичных пользователей, товаров и связей, позволяя полноценно тестировать функционал под нагрузкой.",
        "c": "Снижает производительность до нуля.",
        "d": "Записывает ровно одну строчку.",
        "e": "Такие скрипты нельзя запускать.",
        "correct": "B",
        "topic": "Генерация Seed Data (Наполнение БД)",
        "expl": "Скрипты сидинга эмулируют реальную базу данных, позволяя тестировать пагинацию, сортировку и поиск."
    },
    {
        "text": "Как сформулировать промпт для проведения профессионального Code Review силами AI?",
        "a": "'Мой код хороший?'",
        "b": "'Изучи этот diff как Senior Full-Stack Architect: проверь код на уязвимости безопасности, проблему N+1 запросов к БД, соответствие DRY и дай рекомендации по оптимизации.'",
        "c": "'Удали мой код.'",
        "d": "'Просто напиши похвалу.'",
        "e": "'Назови шрифт в редакторе.'",
        "correct": "B",
        "topic": "Проведение AI Code Review",
        "expl": "Роль требовательного сеньор-архитектора выявляет неочевидные проблемы производительности и безопасности до деплоя."
    },
    {
        "text": "Какой промпт заставит AI оптимизировать медленный SQL-запрос?",
        "a": "'Удали SQL.'",
        "b": "'Этот запрос с множественными JOIN работает медленно. Проанализируй `EXPLAIN QUERY PLAN`, добавь необходимые B-Tree индексы и перепиши запрос для ускорения.'",
        "c": "'Сотри все строки в таблице.'",
        "d": "'Оставь только одну таблицу.'",
        "e": "'Замени SQL на картинку.'",
        "correct": "B",
        "topic": "Оптимизация SQL и Индексы",
        "expl": "Анализ плана запроса и построение индексов ускоряют выборку данных в миллионы раз на реальных объемах."
    },
    {
        "text": "Как в Vibecoding реализуется подход 'Speculative Execution & Rollback' (эксперимент и откат)?",
        "a": "Перезагрузкой Windows.",
        "b": "Созданием отдельной ветки Git для смелого эксперимента с AI; при неудаче выполняется мгновенный откат через `git reset` или удаление ветки без ущерба проекту.",
        "c": "Ручным удалением каждого файла.",
        "d": "Отказом от экспериментов.",
        "e": "Заменой клавиатуры.",
        "correct": "B",
        "topic": "Безопасные Эксперименты в Git",
        "expl": "Ветки Git дают вибкодеру смелость тестировать любые архитектурные гипотезы с мгновенным возвратом в стабильное состояние."
    },
    {
        "text": "В чем выражается главное преимущество Full-Stack Vibecoder-а на рынке фриланса?",
        "a": "В способности работать без сна.",
        "b": "В способности за пару дней превратить сырую идею клиента в работающий SaaS MVP, сдавая заказы в 5 раз быстрее традиционных разработчиков.",
        "c": "В работе за символическую оплату.",
        "d": "В отсутствии необходимости иметь ПК.",
        "e": "Никаких преимуществ нет.",
        "correct": "B",
        "topic": "Vibecoding на Рынке Фриланса",
        "expl": "Скорость сборки MVP и адаптации под нужды клиента дают вибкодеру решающее коммерческое преимущество."
    },
    {
        "text": "Как составить неотразимый отклик (Proposal) на бирже Upwork с помощью AI?",
        "a": "Отправить шаблонный спам 'Наймите меня'.",
        "b": "Проанализировать проблему клиента и сгенерировать персональный план решения задачи с указанием стека, сроков и демонстрацией понимания болей бизнеса.",
        "c": "Предложить самую низкую цену на бирже.",
        "d": "Попытаться обмануть заказчика.",
        "e": "Отправить пустой отклик.",
        "correct": "B",
        "topic": "Продающий Proposal на Фрилансе",
        "expl": "Индивидуальный технический разбор задачи прямо в отклике выделяет разработчика среди сотен шаблонных заявок."
    },
    {
        "text": "Какой ключевой параметр обязательно настраивается при деплое бэкенда на Render или Railway?",
        "a": "Диагональ экрана монитора.",
        "b": "Переменные окружения (Environment Variables: `PORT`, `DATABASE_URL`, `JWT_SECRET`) в панели управления хостингом.",
        "c": "Модель клавиатуры.",
        "d": "Только заголовок вкладки.",
        "e": "Таких параметров нет.",
        "correct": "B",
        "topic": "Настройка Продакшн Окружения (Env)",
        "expl": "Переменные окружения изолируют секреты и настройки боевой базы данных от открытого исходного кода."
    },
    {
        "text": "Что служит главным доказательством инженерного мастерства на презентации Demo Day?",
        "a": "Огромное количество слайдов в PowerPoint.",
        "b": "Демонстрация живой сквозной архитектуры: регистрация пользователя, транзакция в БД, работающий API и чистый масштабируемый код репозитория.",
        "c": "Громкий голос выступающего.",
        "d": "Критика проектов других ребят.",
        "e": "Заучивание определений наизусть.",
        "correct": "B",
        "topic": "Критерии Защиты на Demo Day",
        "expl": "Работающий Full-Stack прототип в боевом облаке — неопровержимое доказательство инженерной компетенции."
    },
    {
        "text": "Какая формула определяет профессионального Vibecoder-а 9 класса?",
        "a": "Слепое принятие всего, что выдал чат-бот.",
        "b": "Глубокое понимание архитектуры систем + виртуозное управление AI-инструментами + ответственность за качество и безопасность кода.",
        "c": "Просмотр развлекательных видео весь день.",
        "d": "Знание строго одного языка разметки.",
        "e": "Отказ от изучения программирования.",
        "correct": "B",
        "topic": "Формула Профессионального Vibecoder-а",
        "expl": "Истинный вибкодер — это инженер, который понимает, что делает программа, и использует AI как мощный усилитель интеллекта."
    }
]

print("Grade 9 TRUE Vibecoding test data loaded (25 questions UZ & RU). Teacher: Ismoiljon Usmonov.")
