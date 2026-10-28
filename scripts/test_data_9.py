#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Target International School — 9-Sinf Vibecoding Test Ma'lumotlari
Fan: Vibecoding (Full-Stack Muhandislik, REST API, DevOps va Kiberxavfsizlik)
O'qituvchi: Ismoiljon Usmonov · Yunusobod filiali

Struktura:
- 18 ta tushunarli, mustahkam va aniq savollar (Steady)
- 7 ta qiziqarli amaliy bilim savollari (Tricky Real Knowledge)
- Barcha savollar veb-platformadagi darslar (index.html va classes/9-sinf/) asosida tuzilgan
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
        {"grade": "Qoniqarli (3)", "range": "13 – 17 ball", "desc": "Middleware, CORS va SQL so'rovlarini takrorlash lozim"},
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
        {"grade": "Удовл. (3)", "range": "13 – 17 баллов", "desc": "Требуется повторение Middleware, CORS и SQL запросов"},
        {"grade": "Неудовл. (2)", "range": "0 – 12 баллов", "desc": "Необходимо заново изучить основы бэкенда и кибербезопасности"}
    ]
}

QUESTIONS_9_UZ = [
    # 1. Steady
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
    # 2. Steady
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
    # 3. Steady
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
    # 4. Steady
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
    # 5. Steady
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
    # 6. Steady
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
    # 7. Steady
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
    # 8. Steady
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
    # 9. Steady
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
    # 10. Steady
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
    # 11. Steady
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
    # 12. Steady
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
    # 13. Steady
    {
        "text": "4-hafta 17-darsda 'Docker' konteynerlarining asosiy qulayligi nimada?",
        "a": "U faqat o'yin o'ynash uchun ishlatiladi.",
        "b": "'Mening kompyuterimda ishlagandi, lekin serverda ishlamayapti' degan muammoni yo'qotib, dasturni hamma joyda bir xil ishlatadi.",
        "c": "U kompyuter xotirasini butunlay tozalab tashlaydi.",
        "d": "U faqat rasm chizadi.",
        "e": "U internetsiz ishlamaydi.",
        "correct": "B",
        "topic": "17-dars: Docker va Konteynerlar",
        "expl": "Docker dastur va uning barcha sozlamalarini bitta qutiga (konteynerga) o'rab, har qanday serverda bir xil ishlashini ta'minlaydi."
    },
    # 14. Steady
    {
        "text": "4-hafta 18-darsda 'SQLite' ma'lumotlar bazasining afzalligi nimada?",
        "a": "U faqat matnli fayllarni o'chiradi.",
        "b": "Uni ishlatish uchun alohida og'ir server o'rnatish shart emas, barcha ma'lumotlar bitta yengil faylda saqlanadi.",
        "c": "U internet tezligini sekinlashtiradi.",
        "d": "Unda faqat 3 ta qator saqlash mumkin.",
        "e": "U faqat telefonlarda ishlaydi.",
        "correct": "B",
        "topic": "18-dars: SQLite Ma'lumotlar Bazasi",
        "expl": "SQLite fayl ko'rinishidagi yengil reliesion baza bo'lib, o'rnatish oson va kichik-o'rta loyihalar uchun juda qulay."
    },
    # 15. Steady
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
    # 16. Tricky (Real Knowledge)
    {
        "text": "4-hafta 19.5-darsda Express da POST so'rovidan yuborilgan ma'lumotni (req.body) o'qiyotganda qaysi middleware yozilmasa dastur qotadi?",
        "a": "app.use(express.static())",
        "b": "app.use(express.json());",
        "c": "app.use(express.cookie())",
        "d": "app.use(express.delete())",
        "e": "app.use(express.clean())",
        "correct": "B",
        "topic": "19.5-dars: Express Middleware (express.json)",
        "expl": "express.json() ulanmasa, Express mijozdan kelgan JSON ni taniy olmaydi va req.body doimo undefined bo'lib qoladi."
    },
    # 17. Tricky (Real Knowledge)
    {
        "text": "4-hafta 20-darsda Frontend (localhost:5173) Backend (localhost:3000) dan ma'lumot so'raganda nima uchun 'CORS Error' xatosi chiqadi?",
        "a": "Frontend kodi buzilgani uchun.",
        "b": "Xavfsizlik qoidasiga ko'ra boshqa portdagi saytga ruxsat yo'qligi sababli; buni to'g'rilash uchun backend da cors middleware ni ruxsat berish kerak.",
        "c": "Kompyuter ekranida joy yetmagani uchun.",
        "d": "Internet simi uzilgani uchun.",
        "e": "Faqat qorong'i rejim yoqilgani uchun.",
        "correct": "B",
        "topic": "20-dars: CORS Xavfsizlik Siyosati",
        "expl": "Brauzerlar turli portlar (5173 va 3000) orasidagi so'rovlarni CORS siyosati orqali to'sadi; serverda 'cors' sozlanishi shart."
    },
    # 18. Tricky (Real Knowledge)
    {
        "text": "3-hafta 13-darsda ChatGPT kabi sun'iy intellekt javoblari nega bitta katta JSON emas, balki so'zma-so'z oqib (Streaming) chiqadi?",
        "a": "Faqat kompyuter chiroyli ko'rinishi uchun.",
        "b": "Server-Sent Events (SSE) orqali: model butun matnni yozib bo'lishini kutmasdan, hosil bo'lgan har bir so'zni darhol ekranga chiqarish uchun.",
        "c": "Internet trafikini tejash uchun emas, aksincha sarflash uchun.",
        "d": "Chunki AI birdaniga hamma so'zni eslay olmaydi.",
        "e": "Brauzer katta matnlarni umuman o'qiy olmagani uchun.",
        "correct": "B",
        "topic": "13-dars: AI Chat Streaming va SSE",
        "expl": "Streaming foydalanuvchini uzoq kuttirmaydi: har bir so'z tayyor bo'lishi bilan SSE kanali orqali brauzerga oqib keladi."
    },
    # 19. Steady
    {
        "text": "5-hafta 21-darsda Linux serveriga masofadan ulanish uchun qaysi standart port ishlatiladi?",
        "a": "Port 80 (HTTP)",
        "b": "Port 22 (SSH)",
        "c": "Port 443 (HTTPS)",
        "d": "Port 3306 (MySQL)",
        "e": "Port 21 (FTP)",
        "correct": "B",
        "topic": "21-dars: Linux va Port 22 (SSH)",
        "expl": "SSH xavfsiz masofaviy boshqaruv protokoli bo'lib, odatda 22-port orqali ishlaydi."
    },
    # 20. Tricky (Real Knowledge)
    {
        "text": "5-hafta 22-darsda Wireshark da kuzatilgan TCP ulanishini o'rnatish (3-Way Handshake) ning to'g'ri ketma-ketligi qaysi?",
        "a": "PING -> PONG -> OK",
        "b": "SYN -> SYN-ACK -> ACK",
        "c": "HELLO -> BYE -> CLOSE",
        "d": "GET -> POST -> DELETE",
        "e": "START -> RUN -> STOP",
        "correct": "B",
        "topic": "22-dars: TCP 3-Way Handshake",
        "expl": "Ishonchli ulanish: Mijoz SYN yuboradi, server SYN-ACK bilan javob beradi va mijoz ACK bilan tasdiqlaydi."
    },
    # 21. Tricky (Real Knowledge)
    {
        "text": "5-hafta 23-darsda SQL Injection hujumidan himoyalanish uchun nega parametrlangan so'rovlar ('SELECT * FROM users WHERE id = ?') ishlatiladi?",
        "a": "Chunki '?' belgisi so'rovni 10 barobar tezlashtiradi.",
        "b": "Chunki foydalanuvchi kiritgan ma'lumot kod sifatida emas, faqat xavfsiz qiymat sifatida qabul qilinadi va bazani buza olmaydi.",
        "c": "Chunki bu SQL tilining yagona qoidasi.",
        "d": "Faqat parollarni yashirish uchun.",
        "e": "Faqat adminlar uchun mo'ljallangan.",
        "correct": "B",
        "topic": "23-dars: SQL Injection va Parametrlar",
        "expl": "Parametrlangan so'rovlar buzg'unchi yozgan 'OR 1=1' kabi hiylalarni kod emas, oddiy matn deb hisoblab, hujumni bartaraf etadi."
    },
    # 22. Tricky (Real Knowledge)
    {
        "text": "5-hafta 24-darsda agar xaker JWT token ichidagi 'role: user' ni 'role: admin' ga o'zgartirsa, server nega uni darhol rad etadi?",
        "a": "Chunki foydalanuvchi ismi o'chib ketadi.",
        "b": "Chunki tokendagi raqamli imzo (Signature) maxfiy kalit bilan tekshirilganda mos kelmaydi va token soxtalashtirilgani fosh bo'ladi.",
        "c": "Chunki tokenda faqat inglizcha so'zlar bo'lishi shart.",
        "d": "Chunki token fayli juda og'irlashib ketadi.",
        "e": "Server foydalanuvchiga qo'ng'iroq qiladi.",
        "correct": "B",
        "topic": "24-dars: JWT Raqamli Imzosi",
        "expl": "JWT imzosi maxfiy kalit bilan hosil qilinadi: ma'lumotning bitta harfi o'zgarsa ham, imzo buziladi va server tokeni rad etadi."
    },
    # 23. Steady
    {
        "text": "6-hafta 26-darsda MVC arxitekturasida 'Model' qismi nima uchun javob beradi?",
        "a": "Faqat tugmalarni bo'yash uchun.",
        "b": "Ma'lumotlar bazasi bilan ishlash, ma'lumotlarni saqlash va ularning to'g'riligini tekshirish uchun.",
        "c": "Faqat brauzerni ochish uchun.",
        "d": "Internet tezligini o'lchash uchun.",
        "e": "Faqat audio eshitish uchun.",
        "correct": "B",
        "topic": "26-dars: MVC arxitekturasi va Model",
        "expl": "Model — bu ma'lumotlar qatlami (Database): jadvallar tuzilishi va ma'lumotlarni olish/saqlash bilan shug'ullanadi."
    },
    # 24. Tricky (Real Knowledge)
    {
        "text": "7-hafta 27-darsda XSS hujumida foydalanuvchi seansini o'g'irlamasliklari uchun Cookie ga nega 'HttpOnly' belgisi qo'yiladi?",
        "a": "Cookie ni faqat kunduzi ishlaydigan qilish uchun.",
        "b": "Brauzerdagi yovuz JavaScript kodi (document.cookie orqali) ushbu tokenni o'g'irlay olmasligi uchun.",
        "c": "Cookie hajmini 1 megabayt qilish uchun.",
        "d": "Faqat parollarni avtomatik to'ldirish uchun.",
        "e": "Barcha foydalanuvchilarni o'chirib yuborish uchun.",
        "correct": "B",
        "topic": "27-dars: HttpOnly Cookie va XSS Himoyasi",
        "expl": "HttpOnly belgisi qo'yilgan cookie larni JavaScript o'qiy olmaydi, natijada XSS hujumi uyushtirilsa ham token o'g'irlanmaydi."
    },
    # 25. Steady
    {
        "text": "9-sinf Vibecoding muhandislik kursining asosiy maqsadi nima?",
        "a": "Faqat tayyor saytlarni ko'chirib olish.",
        "b": "Full-stack tizimlar (Frontend + Backend + Baza) ni arxitektura darajasida loyihalash, AI vositalaridan unumli foydalanish va kiberxavfsizlikni ta'minlash.",
        "c": "Hech qanday ma'lumotlar bazasini ishlatmaslik.",
        "d": "Parollarni xavfsiz saqlashni e'tiborsiz qoldirish.",
        "e": "Faqat bitta HTML fayl bilan cheklanish.",
        "correct": "B",
        "topic": "Xulosa: Full-Stack Muhandislik",
        "expl": "9-sinf o'quvchisi to'liq stekli veb-ilovalarni qura oladi, API lar bilan ishlaydi va tizim xavfsizligini tushunadi."
    }
]

QUESTIONS_9_RU = [
    # 1. Steady
    {
        "text": "В чем состоит главная задача разработчика в парадигме 'Vibecoding' (Урок 2, 1-я неделя)?",
        "a": "Вообще не писать код и целыми днями играть в компьютерные игры.",
        "b": "Быть системным архитектором: формулировать требования (PRD), ставить рамки, тестировать и проверять сгенерированный ИИ код.",
        "c": "Публиковать все пароли от серверов в открытый доступ.",
        "d": "Только протирать клавиатуру компьютера.",
        "e": "Никогда не изучать языки программирования.",
        "correct": "B",
        "topic": "Урок 02: Суть парадигмы Vibecoding",
        "expl": "Vibecoder — это архитектор проекта: он продумывает логику и проверяет код, а нейросеть берет на себя рутинное написание синтаксиса."
    },
    # 2. Steady
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
    # 3. Steady
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
    # 4. Steady
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
    # 5. Steady
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
    # 6. Steady
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
    # 7. Steady
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
    # 8. Steady
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
    # 9. Steady
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
    # 10. Steady
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
    # 11. Steady
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
    # 12. Steady
    {
        "text": "Какую работу выполняет сервис автоматизации GitHub Actions (CI/CD) на Уроке 15?",
        "a": "Каждый день скачивает новые фильмы.",
        "b": "При каждом коммите автоматически запускает тесты проверки кода и выполняет деплой на боевой сервер.",
        "c": "Выключает компьютер пользователя.",
        "d": "Пишет сообщения за учеников в социальных сетях.",
        "e": "Проигрывает музыку в классе.",
        "correct": "B",
        "topic": "Урок 15: Автоматизация через GitHub Actions",
        "expl": "Пайплайны CI/CD автоматически тестируют и собирают проект при каждом пуше, исключая человеческие ошибки при релизе."
    },
    # 13. Steady
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
    # 14. Steady
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
    # 15. Steady
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
    # 16. Tricky (Real Knowledge)
    {
        "text": "Что произойдет в Express при обработке POST-запроса, если забыть подключить middleware 'app.use(express.json())' (Урок 19.5)?",
        "a": "Компьютер мгновенно перезагрузится.",
        "b": "Объект req.body окажется undefined, и попытка прочитать данные пользователя приведет к падению сервера.",
        "c": "Все данные автоматически сохранятся в базу.",
        "d": "Шрифт в коде станет зеленым.",
        "e": "Сервер начнет работать в 10 раз быстрее.",
        "correct": "B",
        "topic": "Урок 19.5: Важность middleware express.json",
        "expl": "Без express.json() фреймворк не парсит входящее тело запроса, в результате чего req.body остается undefined."
    },
    # 17. Tricky (Real Knowledge)
    {
        "text": "Почему возникает ошибка 'CORS Error', когда фронтенд (localhost:5173) обращается к бэкенду (localhost:3000) на Уроке 20?",
        "a": "Потому что сломался монитор.",
        "b": "Потому что браузер в целях безопасности блокирует междоменные запросы с другого порта; на бэкенде нужно разрешить доступ через модуль cors.",
        "c": "Потому что на компьютере закончилось место.",
        "d": "Потому что отошел интернет-кабель.",
        "e": "Потому что включена темная тема оформления.",
        "correct": "B",
        "topic": "Урок 20: Политика безопасности CORS",
        "expl": "Браузер защищает пользователя от несанкционированных запросов между разными портами; бэкенд должен явно разрешить источник фронтенда."
    },
    # 18. Tricky (Real Knowledge)
    {
        "text": "Почему ответы в чатах ИИ (как в ChatGPT) выводятся потоком по словам (Streaming), а не одним куском текста (Урок 13)?",
        "a": "Только ради красивой анимации на экране.",
        "b": "Через протокол Server-Sent Events (SSE): чтобы отдавать пользователю каждое сгенерированное слово сразу, не заставляя ждать весь ответ.",
        "c": "Чтобы специально потратить больше интернет-трафика.",
        "d": "Потому что нейросеть забывает слова через секунду.",
        "e": "Потому что браузер не умеет отображать длинные тексты.",
        "correct": "B",
        "topic": "Урок 13: Потоковая передача данных (SSE)",
        "expl": "Streaming на базе SSE снижает воспринимаемую задержку (TTFT): слова появляются на экране по мере генерации токенов."
    },
    # 19. Steady
    {
        "text": "Какой стандартный сетевой порт используется для безопасного удаленного управления Linux-сервером по SSH (Урок 21)?",
        "a": "Порт 80 (HTTP)",
        "b": "Порт 22 (SSH)",
        "c": "Порт 443 (HTTPS)",
        "d": "Порт 3306 (MySQL)",
        "e": "Порт 21 (FTP)",
        "correct": "B",
        "topic": "Урок 21: Порт 22 для протокола SSH",
        "expl": "Протокол SSH (Secure Shell) по умолчанию слушает входящие подключения на 22 порту."
    },
    # 20. Tricky (Real Knowledge)
    {
        "text": "В какой строгой последовательности происходит трехстороннее рукопожатие TCP (3-Way Handshake) в Wireshark (Урок 22)?",
        "a": "PING -> PONG -> OK",
        "b": "SYN -> SYN-ACK -> ACK",
        "c": "HELLO -> BYE -> CLOSE",
        "d": "GET -> POST -> DELETE",
        "e": "START -> RUN -> STOP",
        "correct": "B",
        "topic": "Урок 22: Рукопожатие TCP (SYN, SYN-ACK, ACK)",
        "expl": "TCP начинает сессию надежно: клиент шлет синхронизацию (SYN), сервер отвечает подтверждением (SYN-ACK), клиент рапортует (ACK)."
    },
    # 21. Tricky (Real Knowledge)
    {
        "text": "Почему параметризованные запросы ('SELECT * FROM users WHERE id = ?') полностью защищают от атак SQL Injection (Урок 23)?",
        "a": "Потому что знак вопроса ускоряет работу базы данных в 10 раз.",
        "b": "Потому что введенные пользователем данные передаются строго как значения переменных, и база никогда не выполнит их как системные команды.",
        "c": "Потому что это единственное правило языка SQL.",
        "d": "Только для того, чтобы скрыть пароли от администратора.",
        "e": "Это работает только для учетной записи администратора.",
        "correct": "B",
        "topic": "Урок 23: Защита от SQL Injection через Prepared Statements",
        "expl": "Параметризация разделяет код запроса и данные: любые кавычки и вредоносные фрагменты воспринимаются как простой безопасный текст."
    },
    # 22. Tricky (Real Knowledge)
    {
        "text": "Почему сервер отклонит поддельный JWT-токен, если злоумышленник изменит в нем 'role: user' на 'role: admin' (Урок 24)?",
        "a": "Потому что имя пользователя сотрется из памяти.",
        "b": "Потому что цифровая подпись (Signature) не совпадет при проверке секретным ключом сервера, и подделка будет разоблачена.",
        "c": "Потому что в токене разрешены только буквы английского алфавита.",
        "d": "Потому что токен станет слишком тяжелым по размеру.",
        "e": "Сервер позвонит владельцу токена по телефону.",
        "correct": "B",
        "topic": "Урок 24: Проверка подписи токена JWT",
        "expl": "Цифровая подпись создается с помощью секретного ключа: изменение хотя бы одного символа в полезной нагрузке делает подпись недействительной."
    },
    # 23. Steady
    {
        "text": "За что отвечает компонент 'Model' (Модель) в архитектурном паттерне MVC (Урок 26)?",
        "a": "Исключительно за анимацию кнопок в браузере.",
        "b": "За работу с базой данных: структуру таблиц, сохранение, изменение и валидацию данных.",
        "c": "Только за запуск браузера.",
        "d": "За измерение скорости интернета.",
        "e": "За воспроизведение звуковых файлов.",
        "correct": "B",
        "topic": "Урок 26: Роль Модели в паттерне MVC",
        "expl": "Model (Модель) инкапсулирует логику хранения данных и прямое взаимодействие с базой данных SQLite."
    },
    # 24. Tricky (Real Knowledge)
    {
        "text": "Почему сессионные куки помечают флагом 'HttpOnly' для защиты от атак XSS (Урок 27)?",
        "a": "Чтобы куки работали только в дневное время суток.",
        "b": "Чтобы скрипты JavaScript в браузере (через document.cookie) не имели доступа к токену и не могли украсть сессию.",
        "c": "Чтобы размер куки увеличился до 1 мегабайта.",
        "d": "Только для автоматического ввода логина.",
        "e": "Чтобы удалить всех пользователей с сайта.",
        "correct": "B",
        "topic": "Урок 27: Флаг HttpOnly против атак XSS",
        "expl": "Флаг HttpOnly полностью изолирует Cookie от клиентского JavaScript: даже при внедрении вредоносного скрипта токен сессии защищен."
    },
    # 25. Steady
    {
        "text": "В чем заключается главная цель курса Vibecoding для 9-го класса?",
        "a": "Просто копировать чужие готовые сайты без понимания.",
        "b": "Освоить full-stack разработку (Фронтенд + Бэкенд + База данных), грамотно проектировать архитектуру с помощью ИИ и защищать свои системы.",
        "c": "Никогда не использовать базы данных в проектах.",
        "d": "Игнорировать правила информационной безопасности.",
        "e": "Ограничиваться только созданием одного статического HTML-файла.",
        "correct": "B",
        "topic": "Итог: Компетенции Full-Stack разработчика 9 класса",
        "expl": "Выпускник 9-го класса умеет проектировать полноценные клиент-серверные сервисы, работать с REST API и базами данных."
    }
]

print("Grade 9 Vibecoding test data loaded (18 steady + 7 tricky). Teacher: Ismoiljon Usmonov.")
