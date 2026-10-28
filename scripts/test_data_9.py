#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Target International School — 9-Sinf Vibecoding Test Ma'lumotlari
Fan: Vibecoding (Full-Stack Muhandislik, REST API, DevOps va Kiberxavfsizlik)
O'qituvchi: Ismoiljon Usmonov · Yunusobod filiali

Struktura:
- 25 ta tushunarli, aniq, qulay va bolalarbop savollar (Steady Easy)
- Veb-platformadagi (index.html va classes/9-sinf/) darslar asosida tuzilgan
"""

META_9_UZ = {
    "school_name": "TARGET INTERNATIONAL SCHOOL — YUNUSOBOD",
    "exam_title": "9-SINF: VIBECODING FULL-STACK, REST API VA DEVOPS MUHANDISLIGI",
    "track_title": "Full-Stack Development & DevOps Track · O'qituvchi: Ismoiljon Usmonov",
    "academic_year": "2026–2027 O'quv Yili",
    "label_name": "O'quvchi F.I.Sh.",
    "label_class": "Sinfi",
    "label_date": "Sana",
    "label_variant": "Variant",
    "variant_val": "1-Variant (Rasmiy)",
    "label_max_score": "Maksimal ball",
    "unit_points": "ball",
    "label_score": "To'plangan ball",
    "instructions": "Ko'rsatma: Har bir savolga berilgan 5 ta variantdan (A, B, C, D, E) faqat bitta to'g'ri javobni tanlang va qalam bilan belgilang. Har bir to'g'ri javob uchun 1 ball beriladi."
}

KEYS_META_9_UZ = {
    "heading": "JAVOBLAR KALITI VA BAHOLASH MEZONI",
    "subheading": "O'qituvchi: Ismoiljon Usmonov · 9-sinf Vibecoding rasmiy tekshirish kaliti (25 ta savol)",
    "table_headers": ["№", "Kalit", "Mavzu / Dars", "Izoh va Tushuntirish"],
    "scale_heading": "Rasmiy 25 Ballik Baholash Shkalasi:",
    "rubric_tiers": [
        {"grade": "A'lo (5)", "range": "22 – 25 ball", "desc": "Express REST API, Docker, SQL, JWT va kiberxavfsizlik bo'yicha mukammal bilim"},
        {"grade": "Yaxshi (4)", "range": "18 – 21 ball", "desc": "Full-stack tizimlar, Git va ma'lumotlar bazasi yaxshi o'zlashtirilgan"},
        {"grade": "Qoniqarli (3)", "range": "13 – 17 ball", "desc": "Middleware, server va SQL so'rovlarini takrorlash lozim"},
        {"grade": "Qoniqarsiz (2)", "range": "0 – 12 ball", "desc": "Backend va kiberxavfsizlik asoslari qayta o'rganilishi lozim"}
    ]
}

META_9_RU = {
    "school_name": "TARGET INTERNATIONAL SCHOOL — ЮНУСАБАД",
    "exam_title": "9 КЛАСС: VIBECODING FULL-STACK, REST API И ИНЖЕНЕРИЯ DEVOPS",
    "track_title": "Full-Stack Development & DevOps Track · Учитель: Исмоилжон Усмонов",
    "academic_year": "2026–2027 Учебный Год",
    "label_name": "Ф.И.О. Ученика",
    "label_class": "Класс",
    "label_date": "Дата",
    "label_variant": "Вариант",
    "variant_val": "Вариант 1 (Официальный)",
    "label_max_score": "Макс. балл",
    "unit_points": "баллов",
    "label_score": "Итоговый балл",
    "instructions": "Инструкция: В каждом вопросе выберите только один правильный вариант ответа из пяти (A, B, C, D, E) и отметьте его. За каждый правильный ответ начисляется 1 балл."
}

KEYS_META_9_RU = {
    "heading": "КЛЮЧИ ОТВЕТОВ И КРИТЕРИИ ОЦЕНИВАНИЯ",
    "subheading": "Учитель: Исмоилжон Усмонов · Официальный ключ 9 класс (25 вопросов)",
    "table_headers": ["№", "Ключ", "Тема / Урок", "Пояснение и разбор ответа"],
    "scale_heading": "Официальная 25-балльная шкала оценивания:",
    "rubric_tiers": [
        {"grade": "Отлично (5)", "range": "22 – 25 баллов", "desc": "Отличные знания Express REST API, Docker, SQL, JWT и кибербезопасности"},
        {"grade": "Хорошо (4)", "range": "18 – 21 балл", "desc": "Full-stack системы, Git и базы данных хорошо освоены"},
        {"grade": "Удовл. (3)", "range": "13 – 17 баллов", "desc": "Требуется повторение Middleware, серверов и SQL запросов"},
        {"grade": "Неудовл. (2)", "range": "0 – 12 баллов", "desc": "Необходимо заново изучить основы бэкенда и кибербезопасности"}
    ]
}

QUESTIONS_9_UZ = [
    {
        "text": "1-hafta 2-darsga ko'ra, zamonaviy 'Vibecoding' yondashuvida dasturchining asosiy vazifasi nima?",
        "a": "Kodni umuman yozmasdan faqat kompyuter o'yinlarini o'ynash.",
        "b": "Tizim arxitektori bo'lish: loyiha talablari (PRD) va qoidalarini aniq belgilash, AI yozgan kodni tekshirish va sinash.",
        "c": "Barcha server parollarini internetga ochiq joylash.",
        "d": "Faqat kompyuter klaviaturasini tozalash.",
        "e": "Hech qanday dasturlash tilini o'rganmaslik.",
        "correct": "B",
        "topic": "02-dars: Vibecoding Asoslari",
        "expl": "Vibecoder — loyiha arxitektori. U nima qilinishini belgilaydi, AI esa kodni tez yozadi, dasturchi uni tekshiradi."
    },
    {
        "text": "1-hafta 4-darsda 'Frilans buyurtma' da PRD (Product Requirements Document) hujjati nima uchun tuziladi?",
        "a": "Faqat buyurtmachidan ko'proq pul talab qilish uchun.",
        "b": "Loyiha nimalarni bajarishi kerakligi, qanday sahifalar va qoidalar bo'lishini oldindan kelishib olish uchun.",
        "c": "Dasturchining telefon raqamini yashirish uchun.",
        "d": "Kompyuter ekranini o'lchash uchun.",
        "e": "Loyiha muddatini cheksiz uzaytirish uchun.",
        "correct": "B",
        "topic": "04-dars: PRD Texnik Hujjati",
        "expl": "PRD — loyihaning texnik shartnomasi bo'lib, talablar va qoidalarni oldindan aniq qilib belgilaydi."
    },
    {
        "text": "2-hafta 7-darsda REST API da yangi ma'lumot (masalan yangi foydalanuvchi) yaratish uchun qaysi HTTP metodi ishlatiladi?",
        "a": "GET",
        "b": "POST",
        "c": "DELETE",
        "d": "HEAD",
        "e": "OPTIONS",
        "correct": "B",
        "topic": "07-dars: REST API va POST Metodi",
        "expl": "REST standartiga ko'ra: GET ma'lumot olish, POST esa serverda yangi ma'lumot yaratish uchun xizmat qiladi."
    },
    {
        "text": "2-hafta 7-darsda so'ralgan veb-sahifa yoki API yo'li serverda topilmasa, qaysi mashhur HTTP status kodi qaytadi?",
        "a": "200 OK",
        "b": "404 Not Found",
        "c": "500 Server Error",
        "d": "201 Created",
        "e": "301 Redirect",
        "correct": "B",
        "topic": "07-dars: HTTP Status Kodlari (404)",
        "expl": "404 kodi so'ralgan sahifa yoki manzil serverda topilmaganini (Not Found) bildiradi."
    },
    {
        "text": "2-hafta 8-darsda 'Jonli Valyuta Konverteri' da tashqi API dan kelgan javobni JavaScript obyektiga aylantirish qanday yoziladi?",
        "a": "const data = response.toText();",
        "b": "const data = await response.json();",
        "c": "const data = window.data;",
        "d": "const data = JSON.clear();",
        "e": "const data = alert(response);",
        "correct": "B",
        "topic": "08-dars: fetch() va response.json()",
        "expl": "response.json() metodi serverdan kelgan JSON matnini JavaScript obyektiga o'girib beradi."
    },
    {
        "text": "2-hafta 9-darsda o'rganilgan 'LocalStorage' ning asosiy vazifasi nima?",
        "a": "Butun internetni kompyuterga ko'chirib olish.",
        "b": "Foydalanuvchi ma'lumotlari (masalan qorong'i rejim yoki til sozlamasi) ni brauzer xotirasida saqlab qolish.",
        "c": "Kompyuter tezligini 10 barobar oshirish.",
        "d": "Faqat videolarni yuklab olish.",
        "e": "Kompyuter parolini o'zgartirish.",
        "correct": "B",
        "topic": "09-dars: LocalStorage vazifasi",
        "expl": "LocalStorage brauzerda ma'lumotlarni saqlaydi, shunda sahifa qayta yangilanganda ham sozlamalar yo'qolmaydi."
    },
    {
        "text": "2-hafta 10-darsda maxfiy API kalitlari va baza parollari nega '.env' faylida saqlanadi va '.gitignore' ga yoziladi?",
        "a": "Faqat fayllar sonini ko'paytirish uchun.",
        "b": "Chunki maxfiy kalitlar ochiq GitHub ga tushib qolsa, xakerlar ularni o'g'irlab, serveringizni buzishi mumkin.",
        "c": "Faqat kompyuter ekranini chiroyli qilish uchun.",
        "d": "Brauzer '.env' faylisiz ishlay olmasligi uchun.",
        "e": "Faqat fayl hajmini kichraytirish uchun.",
        "correct": "B",
        "topic": "10-dars: .env Fayli va Maxfiylik",
        "expl": "Maxfiy parollar .env da saqlanadi va .gitignore orqali GitHub ga chiqib ketishidan himoya qilinadi."
    },
    {
        "text": "2-hafta 11-darsda brauzer DevTools ning 'Network' (Tarmoq) oynasida dasturchi nimalarni ko'ra oladi?",
        "a": "Faqat o'yinlardagi ballarni.",
        "b": "Serverga yuborilgan barcha API so'rovlarini, ularning holatini (200, 404) va kelgan ma'lumotlarni.",
        "c": "Xonadagi Wi-Fi parolini.",
        "d": "Kompyuterning qattiq diskidagi fotosuratlarni.",
        "e": "Faqat Word hujjatlarini.",
        "correct": "B",
        "topic": "11-dars: DevTools Network Paneli",
        "expl": "Network oynasi server bilan brauzer o'rtasida qanday so'rovlar almashinayotganini ko'rsatadi."
    },
    {
        "text": "3-hafta 13-darsda yangi loyihada Git versiya nazorati tizimini ishga tushirish uchun qaysi buyruq beriladi?",
        "a": "git start",
        "b": "git init",
        "c": "git delete",
        "d": "git finish",
        "e": "git run",
        "correct": "B",
        "topic": "13-dars: git init buyrug'i",
        "expl": "git init buyrug'i joriy papkada yangi bo'sh Git omborini (.git) yaratadi."
    },
    {
        "text": "3-hafta 13-darsda yangi funksiya yozish uchun yangi tarmoq (branch) ochish buyrug'i qaysi?",
        "a": "git stop branch",
        "b": "git checkout -b yangi-tarmoq",
        "c": "git push --force",
        "d": "git remove all",
        "e": "git close",
        "correct": "B",
        "topic": "13-dars: Git Branch ochish",
        "expl": "git checkout -b yangi tarmoq ochib, asosiy kodga tegmasdan xavfsiz yangilik kiritish imkonini beradi."
    },
    {
        "text": "3-hafta 14-darsda GitHub da 'Pull Request' (PR) nima uchun ochiladi?",
        "a": "Loyiha egasining hisobini o'chirish uchun.",
        "b": "Yozgan kodingizni asosiy tarmoqqa qo'shishdan oldin jamoa a'zolari ko'rib chiqishi (Code Review) uchun.",
        "c": "Faqat loyiha nomini o'zgartirish uchun.",
        "d": "Internetni o'chirish uchun.",
        "e": "Kompyuterni qayta yoqish uchun.",
        "correct": "B",
        "topic": "14-dars: Pull Request va Code Review",
        "expl": "Pull Request jamoaviy ishlashda kod sifatini tekshirish va xatolarni oldini olish uchun xizmat qiladi."
    },
    {
        "text": "3-hafta 15-darsda GitHub Actions (CI/CD) nima ish bajaradi?",
        "a": "Har kuni yangi video yuklaydi.",
        "b": "Har gal kod GitHub ga yuborilganda, avtomatik testlarni ishga tushiradi va loyihani serverga deploy qiladi.",
        "c": "Kompyuter ekranini o'chiradi.",
        "d": "O'quvchilar nomidan xabar yozadi.",
        "e": "Faqat musiqa qo'yib beradi.",
        "correct": "B",
        "topic": "15-dars: GitHub Actions CI/CD",
        "expl": "CI/CD tizimi kod sifatini tekshirish va serverga yangilanishlarni avtomatik yetkazishni ta'minlaydi."
    },
    {
        "text": "4-hafta 17-darsda 'Docker' konteynerlarining asosiy qulayligi nimada?",
        "a": "U faqat o'yin o'ynash uchun ishlatiladi.",
        "b": "'Mening kompyuterimda ishlagandi, lekin serverda ishlamayapti' degan muammoni yo'qotib, dasturni hamma joyda bir xil ishlatadi.",
        "c": "U kompyuter xotirasini butunlay tozalab tashlaydi.",
        "d": "U faqat rasm chizadi.",
        "e": "U internetsiz ishlamaydi.",
        "correct": "B",
        "topic": "17-dars: Docker va Konteynerlar",
        "expl": "Docker dastur va uning sozlamalarini bitta konteynerga o'rab, har qanday serverda bir xil ishlashini ta'minlaydi."
    },
    {
        "text": "4-hafta 18-darsda 'SQLite' ma'lumotlar bazasining afzalligi nimada?",
        "a": "U faqat matnli fayllarni o'chiradi.",
        "b": "Uni ishlatish uchun alohida og'ir server o'rnatish shart emas, barcha ma'lumotlar bitta yengil faylda saqlanadi.",
        "c": "U internet tezligini sekinlashtiradi.",
        "d": "Unda faqat 3 ta qator saqlash mumkin.",
        "e": "U faqat telefonlarda ishlaydi.",
        "correct": "B",
        "topic": "18-dars: SQLite Ma'lumotlar Bazasi",
        "expl": "SQLite fayl ko'rinishidagi yengil baza bo'lib, o'rnatish oson va kichik loyihalar uchun juda qulay."
    },
    {
        "text": "4-hafta 19-darsda Express da 'GET /api/products' so'roviga javob qaytarish qanday yoziladi?",
        "a": "app.post('/api/products')",
        "b": "app.get('/api/products', (req, res) => { res.json(products); });",
        "c": "window.products()",
        "d": "document.write(products)",
        "e": "console.save(products)",
        "correct": "B",
        "topic": "19-dars: Express Routing",
        "expl": "app.get marshruti kelgan GET so'rovini qabul qiladi va res.json() orqali mijozga mahsulotlar ro'yxatini yuboradi."
    },
    {
        "text": "4-hafta 19.5-darsda Express serverida mijoz yuborgan yangi ma'lumotlarni qabul qilish uchun qaysi so'rov turi ishlatiladi?",
        "a": "Faqat faylni o'chirish so'rovi.",
        "b": "POST so'rovi orqali yuborilib, serverda req.body yordamida o'qib olinadi.",
        "c": "Faqat kompyuter ekranini bo'yash so'rovi.",
        "d": "Faqat internetni o'chirish so'rovi.",
        "e": "Faqat klaviaturani qulflash so'rovi.",
        "correct": "B",
        "topic": "19.5-dars: Express POST va req.body",
        "expl": "POST so'rovlarida mijoz yuborgan ma'lumotlar serverda req.body orqali qulay qabul qilinadi."
    },
    {
        "text": "4-hafta 20-darsda Frontend (interfeys) va Backend (server va baza) birgalikda ishlaganda qanday tizim hosil bo'ladi?",
        "a": "Faqat rasmlar albomi.",
        "b": "To'liq stekli (Full-Stack) zamonaviy veb-ilova.",
        "c": "Kompyuterning qattiq diski.",
        "d": "Faqat kalkulyator dasturi.",
        "e": "Faqat matn muharriri.",
        "correct": "B",
        "topic": "20-dars: Full-Stack Tizimi",
        "expl": "Full-stack — bu foydalanuvchi ko'radigan frontend va ma'lumotlarni qayta ishlaydigan backend ning yagona tizimi."
    },
    {
        "text": "3-hafta 13-darsda zamonaviy AI chatlarda (ChatGPT kabi) javob nima uchun so'zma-so'z oqib (Streaming) chiqadi?",
        "a": "Faqat kompyuter ekranini bezash uchun.",
        "b": "Foydalanuvchi uzoq kutib qolmasligi va hosil bo'lgan har bir so'zni darhol o'qiy olishi uchun.",
        "c": "Internet trafikini sarflash uchun.",
        "d": "Chunki AI birdaniga barcha so'zlarni eslay olmaydi.",
        "e": "Brauzer katta matnlarni umuman o'qiy olmagani uchun.",
        "correct": "B",
        "topic": "13-dars: AI Chat Streaming",
        "expl": "Streaming orqali javob darhol ko'rina boshlaydi, bu esa kutish vaqtini yo'qotib, qulaylik yaratadi."
    },
    {
        "text": "5-hafta 21-darsda Linux serveriga masofadan xavfsiz ulanish uchun qaysi standart port ishlatiladi?",
        "a": "Port 80 (HTTP)",
        "b": "Port 22 (SSH)",
        "c": "Port 443 (HTTPS)",
        "d": "Port 3306 (MySQL)",
        "e": "Port 21 (FTP)",
        "correct": "B",
        "topic": "21-dars: Linux va Port 22 (SSH)",
        "expl": "SSH xavfsiz boshqaruv protokoli bo'lib, odatda 22-port orqali ishlaydi."
    },
    {
        "text": "5-hafta 21-darsda serverni kiber-hujumlardan himoya qilish uchun qanday vosita yoqiladi?",
        "a": "Faqat kompyuter dinamiklari.",
        "b": "Xavfsizlik devori (Firewall / UFW) va ruxsatsiz portlarni yopish.",
        "c": "Faqat telefon zaryadkasi.",
        "d": "Faqat ekranni o'chirib qo'yish.",
        "e": "Faqat qorong'i rejim.",
        "correct": "B",
        "topic": "21-dars: Xavfsizlik devori (UFW)",
        "expl": "Firewall (xavfsizlik devori) begona shubhali ulanishlarni to'sib, serverni xavfsiz saqlaydi."
    },
    {
        "text": "5-hafta 23-darsda ma'lumotlar bazasini SQL Injection kiber-hujumidan qanday himoya qilinadi?",
        "a": "Bazada parollarni umuman saqlamaslik orqali.",
        "b": "Foydalanuvchi kiritgan ma'lumotlarni to'g'ri tekshirib, xavfsiz parametrlangan so'rovlar ishlatish orqali.",
        "c": "SQL o'rniga faqat qog'oz daftarga yozish orqali.",
        "d": "Kompyuterni o'chirib qo'yish orqali.",
        "e": "Faqat bitta foydalanuvchiga ruxsat berish orqali.",
        "correct": "B",
        "topic": "23-dars: SQL Injection Himoyasi",
        "expl": "Xavfsiz so'rovlar yozilsa, buzg'unchilar o'zlarining zararli kodlarini ma'lumotlar bazasiga o'tkaza olmaydi."
    },
    {
        "text": "5-hafta 24-darsda foydalanuvchi veb-saytga kirganini eslab qolish va tekshirish uchun qaysi xavfsiz raqamli kalit ishlatiladi?",
        "a": "Faqat foydalanuvchining rasmi.",
        "b": "JWT (JSON Web Token) deb ataluvchi xavfsiz raqamli token.",
        "c": "Faqat oddiy 1234 paroli.",
        "d": "Faqat brauzer tarixi.",
        "e": "Faqat kompyuter modeli.",
        "correct": "B",
        "topic": "24-dars: JWT Raqamli Tokeni",
        "expl": "JWT foydalanuvchi saytga kirgach beriladi va uning kimligini keyingi so'rovlarda xavfsiz tasdiqlaydi."
    },
    {
        "text": "6-hafta 26-darsda MVC arxitekturasida 'Model' qismi nima uchun javob beradi?",
        "a": "Faqat tugmalarni bo'yash uchun.",
        "b": "Ma'lumotlar bazasi bilan ishlash, ma'lumotlarni saqlash va tartibga solish uchun.",
        "c": "Faqat brauzerni ochish uchun.",
        "d": "Internet tezligini o'lchash uchun.",
        "e": "Faqat audio eshitish uchun.",
        "correct": "B",
        "topic": "26-dars: MVC arxitekturasi va Model",
        "expl": "Model — bu ma'lumotlar qatlami (Database): jadvallar va ma'lumotlarni olish/saqlash bilan shug'ullanadi."
    },
    {
        "text": "7-hafta 27-darsda foydalanuvchining shaxsiy seansini brauzerda xavfsiz saqlash uchun nima ishlatiladi?",
        "a": "Faqat oddiy ochiq matn fayllari.",
        "b": "Xavfsiz va begona kodlardan himoyalangan Cookie fayllari.",
        "c": "Faqat kompyuter klaviaturasi.",
        "d": "Faqat rasmlar galereyasi.",
        "e": "Faqat printer qog'ozi.",
        "correct": "B",
        "topic": "27-dars: Xavfsiz Cookie fayllari",
        "expl": "Xavfsiz Cookie fayllari foydalanuvchi seansini begona xakerlik skriptlaridan himoya qilib turadi."
    },
    {
        "text": "9-sinf Vibecoding muhandislik kursining asosiy maqsadi nima?",
        "a": "Faqat tayyor saytlarni ko'chirib olish.",
        "b": "Full-stack tizimlar (Frontend + Backend + Baza) ni loyihalash, AI vositalaridan unumli foydalanish va kiberxavfsizlikni ta'minlash.",
        "c": "Hech qanday ma'lumotlar bazasini ishlatmaslik.",
        "d": "Parollarni xavfsiz saqlashni e'tiborsiz qoldirish.",
        "e": "Faqat bitta HTML fayl bilan cheklanish.",
        "correct": "B",
        "topic": "Xulosa: Full-Stack Muhandislik",
        "expl": "9-sinf o'quvchisi to'liq stekli veb-ilovalarni qura oladi, API lar bilan ishlaydi va tizim xavfsizligini tushunadi."
    }
]

QUESTIONS_9_RU = [
    {
        "text": "В чем состоит главная задача разработчика в парадигме 'Vibecoding' (Урок 2, 1-я неделя)?",
        "a": "Вообще не писать код и целыми днями играть в компьютерные игры.",
        "b": "Быть системным архитектором: формулировать требования (PRD), ставить рамки, тестировать и проверять сгенерированный ИИ код.",
        "c": "Публиковать все пароли от серверов в открытый доступ.",
        "d": "Только протирать клавиатуру компьютера.",
        "e": "Никогда не изучать языки программирования.",
        "correct": "B",
        "topic": "Урок 02: Суть парадигмы Vibecoding",
        "expl": "Vibecoder — это архитектор проекта: он продумывает логику и проверяет код, а нейросеть берет на себя написание синтаксиса."
    },
    {
        "text": "Для чего на фрилансе составляется документ PRD (Product Requirements Document) на Уроке 4?",
        "a": "Исключительно для того, чтобы попросить у клиента больше денег.",
        "b": "Чтобы заранее четко зафиксировать все функции, страницы и правила проекта и избежать недопонимания.",
        "c": "Чтобы скрыть номер телефона разработчика.",
        "d": "Чтобы измерить диагональ экрана монитора.",
        "e": "Чтобы бесконечно затягивать сроки сдачи проекта.",
        "correct": "B",
        "topic": "Урок 04: Технический документ PRD",
        "expl": "PRD — это технический договор проекта, описывающий требования, функции и критерии успешной сдачи."
    },
    {
        "text": "Какой метод протокола HTTP используется в REST API для создания нового ресурса (Урок 7, 2-я неделя)?",
        "a": "GET",
        "b": "POST",
        "c": "DELETE",
        "d": "HEAD",
        "e": "OPTIONS",
        "correct": "B",
        "topic": "Урок 07: Метод POST в REST API",
        "expl": "В стандартах REST: метод GET запрашивает данные, а метод POST отправляет данные для создания новой записи."
    },
    {
        "text": "Какой общеизвестный статус-код HTTP возвращает сервер, если запрашиваемая страница не найдена (Урок 7)?",
        "a": "200 OK",
        "b": "404 Not Found",
        "c": "500 Server Error",
        "d": "201 Created",
        "e": "301 Redirect",
        "correct": "B",
        "topic": "Урок 07: Статус-код 404 Not Found",
        "expl": "Статус 404 сообщает браузеру, что указанный адрес или ресурс не существует на сервере."
    },
    {
        "text": "Как в коде JavaScript преобразовать ответ от сервера в удобный объект данных (Урок 8)?",
        "a": "const data = response.toText();",
        "b": "const data = await response.json();",
        "c": "const data = window.data;",
        "d": "const data = JSON.clear();",
        "e": "const data = alert(response);",
        "correct": "B",
        "topic": "Урок 08: Парсинг ответа через response.json()",
        "expl": "Метод response.json() асинхронно считывает поток JSON от сервера и превращает его в JavaScript-объект."
    },
    {
        "text": "В чем заключается главная задача хранилища 'LocalStorage' в браузере (Урок 9)?",
        "a": "Скопировать весь интернет на жесткий диск.",
        "b": "Сохранять данные пользователя (например, тему оформления или язык) в браузере, чтобы они не пропадали при перезагрузке.",
        "c": "Увеличить скорость процессора в 10 раз.",
        "d": "Скачивать только видеофайлы.",
        "e": "Изменять системный пароль от Windows.",
        "correct": "B",
        "topic": "Урок 09: Назначение LocalStorage",
        "expl": "LocalStorage хранит настройки и состояние прямо в браузере пользователя без необходимости обращаться к базе данных."
    },
    {
        "text": "Почему секретные ключи API изолируют в файле '.env' и обязательно вносят его в '.gitignore' (Урок 10)?",
        "a": "Только чтобы увеличить общее число файлов в проекте.",
        "b": "Потому что при утечке ключей в открытый репозиторий GitHub хакеры украдут их и взломают сервера.",
        "c": "Исключительно для украшения рабочего стола.",
        "d": "Потому что браузер не запускается без файла .env.",
        "e": "Только чтобы уменьшить размер проекта.",
        "correct": "B",
        "topic": "Урок 10: Секреты в .env и .gitignore",
        "expl": "Ключи и пароли хранятся в .env, а запись в .gitignore защищает их от случайной публикации на GitHub."
    },
    {
        "text": "Что разработчик может инспектировать во вкладке 'Network' (Сеть) панели DevTools браузера (Урок 11)?",
        "a": "Только набранные очки в играх.",
        "b": "Все сетевые запросы к API, их статус-коды (200, 404), заголовки и тело возвращенного ответа.",
        "c": "Пароль от домашнего роутера Wi-Fi.",
        "d": "Личные фотографии на жестком диске.",
        "e": "Исключительно файлы Microsoft Word.",
        "correct": "B",
        "topic": "Урок 11: Анализ сети во вкладке Network",
        "expl": "Вкладка Network фиксирует каждый запрос между клиентом и бэкендом, помогая отслеживать ошибки в API."
    },
    {
        "text": "Какая команда инициализирует новый репозиторий системы контроля версий Git в папке (Урок 13)?",
        "a": "git start",
        "b": "git init",
        "c": "git delete",
        "d": "git finish",
        "e": "git run",
        "correct": "B",
        "topic": "Урок 13: Инициализация Git (git init)",
        "expl": "Команда git init создает скрытую папку .git и начинает отслеживать историю изменений файлов проекта."
    },
    {
        "text": "С помощью какой команды Git создается новая ветка (branch) для безопасной разработки новой функции (Урок 13)?",
        "a": "git stop branch",
        "b": "git checkout -b new-feature",
        "c": "git push --force",
        "d": "git remove all",
        "e": "git close",
        "correct": "B",
        "topic": "Урок 13: Создание ветки в Git",
        "expl": "git checkout -b создает новую ветку и сразу переключается на нее, изолируя разработку от стабильной ветки main."
    },
    {
        "text": "Для чего на платформе GitHub открывается запрос 'Pull Request' (PR) на Уроке 14?",
        "a": "Чтобы удалить учетную запись автора проекта.",
        "b": "Чтобы перед слиянием новой ветки с основной базой кода команда могла провести ревью (Code Review) и обсудить правки.",
        "c": "Только для изменения названия проекта.",
        "d": "Чтобы отключить интернет на сервере.",
        "e": "Чтобы перезагрузить компьютер.",
        "correct": "B",
        "topic": "Урок 14: Pull Request и Code Review",
        "expl": "Pull Request позволяет коллегам просмотреть разницу строк кода (diff), протестировать изменения и одобрить слияние."
    },
    {
        "text": "Какую работу выполняет сервис автоматизации GitHub Actions (CI/CD) на Уроке 15?",
        "a": "Каждый день скачивает новые фильмы.",
        "b": "При каждом коммите автоматически запускает тесты проверки кода и выполняет деплой на боевой сервер.",
        "c": "Выключает компьютер пользователя.",
        "d": "Пишет сообщения за учеников в социальных сетях.",
        "e": "Проигрывает музыку в классе.",
        "correct": "B",
        "topic": "Урок 15: Автоматизация через GitHub Actions",
        "expl": "Пайплайны CI/CD автоматически тестируют и собирают проект при каждом пуше, исключая человеческие ошибки."
    },
    {
        "text": "В чем заключается главное преимущество контейнеров 'Docker' (Урок 17)?",
        "a": "Они используются исключительно для компьютерных игр.",
        "b": "Они решают проблему 'у меня на компьютере работало, а на сервере сломалось', гарантируя одинаковую работу везде.",
        "c": "Они полностью стирают память компьютера.",
        "d": "Они предназначены только для рисования картинок.",
        "e": "Они вообще не работают без интернета.",
        "correct": "B",
        "topic": "Урок 17: Преимущества контейнеризации Docker",
        "expl": "Docker упаковывает приложение вместе со всеми зависимостями, гарантируя идентичный запуск на любом компьютере и сервере."
    },
    {
        "text": "В чем состоит ключевая особенность базы данных 'SQLite' (Урок 18)?",
        "a": "Она предназначена только для удаления текстовых файлов.",
        "b": "Для нее не нужно настраивать тяжелый отдельный сервер: вся база хранится в одном компактном файле.",
        "c": "Она искусственно замедляет скорость интернета.",
        "d": "В ней можно хранить максимум 3 строки данных.",
        "e": "Она работает только на кнопочных телефонах.",
        "correct": "B",
        "topic": "Урок 18: Особенности базы данных SQLite",
        "expl": "SQLite — это легковесная бессерверная реляционная база данных, хранящая все таблицы в одном файле на диске."
    },
    {
        "text": "Как в фреймворке Express описать обработчик запроса 'GET /api/products' (Урок 19)?",
        "a": "app.post('/api/products')",
        "b": "app.get('/api/products', (req, res) => { res.json(products); });",
        "c": "window.products()",
        "d": "document.write(products)",
        "e": "console.save(products)",
        "correct": "B",
        "topic": "Урок 19: Маршрутизация GET в Express",
        "expl": "Метод app.get() слушает запросы по указанному пути и отправляет список товаров клиенту в формате JSON."
    },
    {
        "text": "Какой тип запроса используется на Уроке 19.5 в Express для отправки новых данных на сервер?",
        "a": "Запрос на удаление файла.",
        "b": "Запрос POST, а данные на сервере считываются через объект req.body.",
        "c": "Запрос на перекрашивание экрана.",
        "d": "Запрос на выключение интернета.",
        "e": "Запрос на блокировку клавиатуры.",
        "correct": "B",
        "topic": "Урок 19.5: Запросы POST и req.body",
        "expl": "Данные форм и новые записи отправляются через POST и удобно принимаются на сервере в req.body."
    },
    {
        "text": "Что получается, когда Фронтенд (интерфейс) и Бэкенд (сервер и база данных) работают вместе (Урок 20)?",
        "a": "Обычный альбом для рисования.",
        "b": "Полноценное веб-приложение полного цикла (Full-Stack).",
        "c": "Жесткий диск компьютера.",
        "d": "Обычный калькулятор.",
        "e": "Простой текстовый блокнот.",
        "correct": "B",
        "topic": "Урок 20: Системы Full-Stack",
        "expl": "Full-Stack объединяет клиентскую часть (то, что видит пользователь) и серверную логику с базой данных."
    },
    {
        "text": "Почему ответы в чатах ИИ выводятся на экран потоком по словам (Streaming) на Уроке 13?",
        "a": "Только для украшения экрана.",
        "b": "Чтобы пользователь не ждал долго и сразу читал каждое появляющееся слово.",
        "c": "Чтобы специально потратить больше интернет-трафика.",
        "d": "Потому что нейросеть забывает слова через секунду.",
        "e": "Потому что браузер не умеет отображать длинные тексты.",
        "correct": "B",
        "topic": "Урок 13: Потоковый вывод (Streaming)",
        "expl": "Потоковый вывод позволяет читать ответ сразу, не дожидаясь генерации всего текста целиком."
    },
    {
        "text": "Какой сетевой порт используется для безопасного управления Linux-сервером по SSH (Урок 21)?",
        "a": "Порт 80 (HTTP)",
        "b": "Порт 22 (SSH)",
        "c": "Порт 443 (HTTPS)",
        "d": "Порт 3306 (MySQL)",
        "e": "Порт 21 (FTP)",
        "correct": "B",
        "topic": "Урок 21: Порт 22 для SSH",
        "expl": "Протокол SSH (Secure Shell) по умолчанию слушает входящие подключения на 22 порту."
    },
    {
        "text": "Какой инструмент защищает Linux-сервер от нежелательных сетевых подключений (Урок 21)?",
        "a": "Динамики компьютера.",
        "b": "Сетевой экран (Firewall / UFW), закрывающий лишние порты.",
        "c": "Зарядное устройство.",
        "d": "Выключение монитора.",
        "e": "Темная тема экрана.",
        "correct": "B",
        "topic": "Урок 21: Сетевой экран UFW",
        "expl": "Сетевой экран (Firewall) блокирует подозрительный трафик и защищает порты сервера от проникновения."
    },
    {
        "text": "Как защитить базу данных от атак типа SQL Injection на Уроке 23?",
        "a": "Вообще не хранить пароли в базе данных.",
        "b": "Использовать безопасные параметризованные запросы и проверять вводимые пользователем данные.",
        "c": "Записывать данные только в бумажную тетрадь.",
        "d": "Выключить питание сервера.",
        "e": "Разрешить вход только одному пользователю.",
        "correct": "B",
        "topic": "Урок 23: Защита от SQL Injection",
        "expl": "Параметризованные запросы гарантируют, что введенный пользователем текст не превратится в команду базы данных."
    },
    {
        "text": "Какой цифровой токен используется на Уроке 24 для подтверждения того, что пользователь вошел на сайт?",
        "a": "Фотография пользователя.",
        "b": "Безопасный цифровой токен JWT (JSON Web Token).",
        "c": "Простой пароль 1234.",
        "d": "История посещения сайтов.",
        "e": "Модель компьютера.",
        "correct": "B",
        "topic": "Урок 24: Токены безопасности JWT",
        "expl": "Токен JWT выдается после ввода логина и пароля и безопасно подтверждает авторизацию в последующих запросах."
    },
    {
        "text": "За что отвечает компонент 'Model' (Модель) в архитектуре MVC (Урок 26)?",
        "a": "Исключительно за анимацию кнопок в браузере.",
        "b": "За работу с базой данных: структуру таблиц, сохранение и упорядочивание данных.",
        "c": "Только за запуск браузера.",
        "d": "За измерение скорости интернета.",
        "e": "За воспроизведение звуковых файлов.",
        "correct": "B",
        "topic": "Урок 26: Роль Модели в MVC",
        "expl": "Model (Модель) отвечает за хранение, выборку и обновление данных в базе данных."
    },
    {
        "text": "Что используется на Уроке 27 для безопасного хранения сессии пользователя в браузере?",
        "a": "Простые открытые текстовые файлы.",
        "b": "Защищенные Cookie-файлы, недоступные для посторонних скриптов.",
        "c": "Клавиатура компьютера.",
        "d": "Галерея картинок.",
        "e": "Лист бумаги для принтера.",
        "correct": "B",
        "topic": "Урок 27: Безопасные Cookie-файлы",
        "expl": "Защищенные Cookie изолируют сессию пользователя от вредоносных скриптов в браузере."
    },
    {
        "text": "В чем заключается главная цель курса Vibecoding для 9-го класса?",
        "a": "Просто копировать чужие готовые сайты без понимания.",
        "b": "Освоить full-stack разработку (Фронтенд + Бэкенд + База данных), проектировать сервисы с помощью ИИ и защищать их.",
        "c": "Никогда не использовать базы данных в проектах.",
        "d": "Игнорировать правила информационной безопасности.",
        "e": "Ограничиваться только созданием одного статического HTML-файла.",
        "correct": "B",
        "topic": "Итог: Компетенции Full-Stack разработчика 9 класса",
        "expl": "Выпускник 9-го класса умеет проектировать полноценные сервисы, работать с REST API и базами данных."
    }
]

print("Grade 9 Vibecoding test data loaded (Steady Easy). Teacher: Ismoiljon Usmonov.")
