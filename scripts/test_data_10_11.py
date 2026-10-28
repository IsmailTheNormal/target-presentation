#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Target International School — Grades 10–11 Vibecoding Test Data
Subject: Vibecoding (AI Engineering, Web Development, Prompt Systems & Security)
Instructor: Ismoiljon Usmonov · Yunusobod Campus

Contains:
1. QUESTIONS_10_11_UZ & QUESTIONS_10_11_RU (Bilingual Uzbek + Russian in braces)
2. QUESTIONS_10_11_EN (English Only)
"""

META_10_11_UZ = {
    "school_name": "TARGET INTERNATIONAL SCHOOL — YUNUSOBOD",
    "exam_title": "10–11-SINF: VIBECODING, VEB-ARXITEKTURA VA SUN'IY INTELLEKT",
    "track_title": "Vibecoding & AI Systems Track · O'qituvchi: Ismoiljon Usmonov",
    "academic_year": "2026–2027 O'quv Yili",
    "label_name": "O'quvchi F.I.Sh.",
    "label_class": "Sinfi",
    "label_date": "Sana",
    "label_variant": "Variant",
    "variant_val": "1-Variant (Rasmiy)",
    "label_max_score": "Maksimal ball",
    "unit_points": "ball",
    "label_score": "To'plangan ball",
    "instructions": "Ko'rsatma: Har bir savolga berilgan 5 ta variantdan (A, B, C, D, E) faqat bitta to'g'ri javobni tanlang va qalam bilan belgilang. Har bir to'g'ri javob uchun 1 ball beriladi (Jami: 25 ball)."
}

KEYS_META_10_11_UZ = {
    "heading": "JAVOBLAR KALITI VA BAHOLASH MEZONI",
    "subheading": "O'qituvchi: Ismoiljon Usmonov · 10–11-sinf Vibecoding rasmiy tekshirish kaliti (25 ta savol)",
    "table_headers": ["№", "Kalit", "Mavzu / Yo'nalish", "Izoh va Tushuntirish"],
    "scale_heading": "Rasmiy 25 Ballik Baholash Shkalasi:",
    "rubric_tiers": [
        {"grade": "A'lo (5)", "range": "22 – 25 ball", "desc": "Vibecoding jarayoni, prompt injiniringi va veb-arxitektura bo'yicha a'lo bilim"},
        {"grade": "Yaxshi (4)", "range": "18 – 21 ball", "desc": "Veb-dasturlash, AI modellari va xavfsizlik tushunchalarini yaxshi o'zlashtirgan"},
        {"grade": "Qoniqarli (3)", "range": "13 – 17 ball", "desc": "API, asinxron oqim va prompt texnikalarini takrorlash lozim"},
        {"grade": "Qoniqarsiz (2)", "range": "0 – 12 ball", "desc": "Vibecoding asoslari qayta o'rganilishi lozim"}
    ]
}

META_10_11_RU = {
    "school_name": "TARGET INTERNATIONAL SCHOOL — ЮНУСАБАД",
    "exam_title": "10–11 КЛАСС: VIBECODING, ВЕБ-АРХИТЕКТУРА И ИСКУССТВЕННЫЙ ИНТЕЛЛЕКТ",
    "track_title": "Vibecoding & AI Systems Track · Учитель: Исмоилжон Усмонов",
    "academic_year": "2026–2027 Учебный Год",
    "label_name": "Ф.И.О. Ученика",
    "label_class": "Класс",
    "label_date": "Дата",
    "label_variant": "Вариант",
    "variant_val": "Вариант 1 (Официальный)",
    "label_max_score": "Макс. балл",
    "unit_points": "баллов",
    "label_score": "Итоговый балл",
    "instructions": "Инструкция: В каждом вопросе выберите только один правильный вариант ответа из пяти (A, B, C, D, E) и отметьте его. За каждый правильный ответ начисляется 1 балл (Всего: 25 баллов)."
}

KEYS_META_10_11_RU = {
    "heading": "КЛЮЧИ ОТВЕТОВ И КРИТЕРИИ ОЦЕНИВАНИЯ",
    "subheading": "Учитель: Исмоилжон Усмонов · Официальный ключ 10–11 класс (25 вопросов)",
    "table_headers": ["№", "Ключ", "Тема / Направление", "Пояснение и разбор ответа"],
    "scale_heading": "Официальная 25-балльная шкала оценивания:",
    "rubric_tiers": [
        {"grade": "Отлично (5)", "range": "22 – 25 баллов", "desc": "Отличное владение логикой Vibecoding, промпт-инжинирингом и веб-архитектурой"},
        {"grade": "Хорошо (4)", "range": "18 – 21 балл", "desc": "Хорошее понимание веб-разработки, моделей ИИ и кибербезопасности"},
        {"grade": "Удовл. (3)", "range": "13 – 17 баллов", "desc": "Требуется повторение работы с API, асинхронностью и структурой промптов"},
        {"grade": "Неудовл. (2)", "range": "0 – 12 баллов", "desc": "Необходимо повторить основы Vibecoding"}
    ]
}

META_10_11_EN = {
    "school_name": "TARGET INTERNATIONAL SCHOOL — YUNUSOBOD",
    "exam_title": "GRADES 10–11: VIBECODING, WEB ARCHITECTURE & ARTIFICIAL INTELLIGENCE",
    "track_title": "Vibecoding & AI Systems Track · Instructor: Ismoiljon Usmonov",
    "academic_year": "Academic Year 2026–2027",
    "label_name": "Student Full Name",
    "label_class": "Grade / Section",
    "label_date": "Date",
    "label_variant": "Variant",
    "variant_val": "Variant 1 (Official)",
    "label_max_score": "Maximum Score",
    "unit_points": "pts",
    "label_score": "Final Score",
    "instructions": "Instructions: For each question, choose and mark exactly ONE correct answer from the 5 options (A, B, C, D, E). Each correct answer is awarded 1 point (Total: 25 points)."
}

KEYS_META_10_11_EN = {
    "heading": "OFFICIAL ANSWER KEY & 25-POINT GRADING RUBRIC",
    "subheading": "Instructor: Ismoiljon Usmonov · Grades 10–11 Vibecoding Official Key (25 Questions)",
    "table_headers": ["№", "Key", "Topic / Lesson", "Explanation"],
    "scale_heading": "Official 25-Point Grading Rubric:",
    "rubric_tiers": [
        {"grade": "Excellent (5)", "range": "22 – 25 pts", "desc": "Outstanding grasp of Vibecoding workflow, prompt systems, web architecture, and AI security"},
        {"grade": "Good (4)", "range": "18 – 21 pts", "desc": "Solid understanding of web development, AI prompting, and core developer tools"},
        {"grade": "Satisfactory (3)", "range": "13 – 17 pts", "desc": "Understands basics; needs further practice with APIs, prompt techniques, and async flow"},
        {"grade": "Unsatisfactory (2)", "range": "0 – 12 pts", "desc": "Foundational review of Vibecoding principles and web concepts required"}
    ]
}

QUESTIONS_10_11_UZ = [
    # 1
    {
        "text": "Zamonaviy dasturiy ta'minot muhandisligida 'Vibecoding'ning asosiy falsafasi nima?",
        "a": "Kodni hech qachon test qilmasdan va ishga tushirmasdan 100% AI ga ishonish.",
        "b": "Barcha kodlarni qo'lda ikkilik (0 va 1) mashina tilida yozish.",
        "c": "Inson dasturchi loyiha arxitekturasi va testlarini rejalashtirgan holda, AI yordamchisiga kod yozishni yo'naltirish.",
        "d": "Eski darsliklardan eskirgan kod parchalarini ko'chirib olish.",
        "e": "Veb-sayt qurayotganda butun internetni o'chirib qo'yish.",
        "correct": "C",
        "topic": "01: Vibecoding falsafasi",
        "expl": "Vibecoding dasturchiga inson nazorati, arxitekturasi va testlarini saqlab, kodlashni AI ga yuklash imkonini beradi."
    },
    # 2
    {
        "text": "AI promptining qaysi qismi modelning roli (personajini), xulq-atvor chegaralari va asosiy qoidalarini belgilaydi?",
        "a": "Wi-Fi sozlash skripti",
        "b": "Tizimli prompt (System Prompt yoki tizim ko'rsatmasi)",
        "c": "Kompyuterning BIOS sozlamalari",
        "d": "CSS uslublar jadvali",
        "e": "HDMI ekran drayveri",
        "correct": "B",
        "topic": "02: Tizimli promptlar",
        "expl": "System Prompt AI ga qanday rolda gapirish, nimalarga ruxsat berilgani va qanday chegaralarga amal qilishni o'rgatadi."
    },
    # 3
    {
        "text": "AI modeliga ko'rsatma berishda 'Few-Shot Prompting' nima?",
        "a": "Yangi vazifani bajarishdan oldin AI ga 1 tadan 3 tagacha aniq kirish-chiqish (input-output) namunalarini ko'rsatish.",
        "b": "AI ga jami faqat uchta so'z yozish.",
        "c": "Prompt yuborishdan oldin kompyuterni uch marta o'chirib yoqish.",
        "d": "Serverni to'xtatish uchun birdaniga uchta bir xil so'rov yuborish.",
        "e": "Kodni bir vaqtning o'zida uchta alohida monitorda ishga tushirish.",
        "correct": "A",
        "topic": "03: Few-Shot Prompting",
        "expl": "Few-Shot prompting aniq namunalar orqali modelga kutilayotgan javob formati va mantiqiy qolipni o'rgatadi."
    },
    # 4
    {
        "text": "Sun'iy intellektning 'Gallyutsinatsiyasi' (Hallucination) nimani anglatadi?",
        "a": "Kabel uzilgani sababli monitor ekrani turli ranglarda miltillashi.",
        "b": "AI modeli mavjud bo'lmagan soxta kutubxona, funksiya yoki xato faktlarni ishonch bilan to'qib chiqarishi.",
        "c": "Protsessor harorati noldan pastga tushib ketishi.",
        "d": "Noutbuk batareyasi kutilganidan tezroq tugashi.",
        "e": "Brauzerda bitta o'rniga ikkita oyna ochilishi.",
        "correct": "B",
        "topic": "04: AI Gallyutsinatsiyasi",
        "expl": "Gallyutsinatsiya — bu model bilmagan faktlarini haqiqatdek ishonchli to'qib chiqarish holatidir."
    },
    # 5
    {
        "text": "Til modelida (LLM) 'Temperature' parametrini 0.0 ga tushirish qanday natija beradi?",
        "a": "AI modeli butunlay to'xtab, javob berishdan bosh tortadi.",
        "b": "Model o'ta ijodiy, tasodifiy bo'lib, to'qima ertaklar yozishni boshlaydi.",
        "c": "Javoblar o'ta aniq, diqqatli, takrorlanuvchi (deterministic) va barqaror bo'ladi.",
        "d": "Uy Wi-Fi tezligi sezilarli darajada oshadi.",
        "e": "Model kompyuteringizdagi barcha kodlarni o'chirib tashlaydi.",
        "correct": "C",
        "topic": "05: LLM Harorati (Temperature)",
        "expl": "Past harorat (0 ga yaqin) tasodifiylikni yo'qotadi va dasturiy kod yozishda eng aniq javoblarni ta'minlaydi."
    },
    # 6
    {
        "text": "AI modelining 'Kontekst oynasi' (Context Window) nimani anglatadi?",
        "a": "Kompyuter xonasidagi jismoniy shisha deraza.",
        "b": "Model bitta suhbat davomida eslab qolishi va qayta ishlay olishi mumkin bo'lgan maksimal tokenlar (so'zlar) hajmi.",
        "c": "Operatsion tizimning ish stoli fon rasmi.",
        "d": "Brauzer oynasining piksellardagi o'lchami.",
        "e": "Qattiq diskdagi bo'sh xotira hajmi.",
        "correct": "B",
        "topic": "06: Kontekst oynasi",
        "expl": "Kontekst oynasi — modelning bir vaqtda eslab qola oladigan ma'lumotlar xotirasi chegarasidir."
    },
    # 7
    {
        "text": "Veb-dasturlashda HTML qanday asosiy vazifani bajaradi?",
        "a": "Sahifaning poydevor strukturasi va semantik tarkibini (sarlavhalar, matnlar, tugmalar, shakllar) belgilaydi.",
        "b": "Kompyuterni bevosita ma'lumotlar bazasi serveriga ulaydi.",
        "c": "Sahifani soyalar, gradientlar va chiroyli animatsiyalar bilan bezaydi.",
        "d": "Serverda orqa fondagi kriptografik hisob-kitoblarni bajaradi.",
        "e": "JavaScript kodini ikkilik mashina kodiga kompilyatsiya qiladi.",
        "correct": "A",
        "topic": "07: HTML Strukturasi",
        "expl": "HTML — har qanday veb-sahifaning skeleti va barcha kontent elementlari asosidir."
    },
    # 8
    {
        "text": "Qaysi CSS xossasi bolalar elementlarini gorizontal va vertikal markazlashtirish va tekislash uchun keng qo'llaniladi?",
        "a": "display: flex (justify-content va align-items bilan)",
        "b": "text-decoration: underline",
        "c": "color: transparent",
        "d": "font-weight: bold",
        "e": "cursor: pointer",
        "correct": "A",
        "topic": "08: CSS Flexbox",
        "expl": "Flexbox — elementlarni bir qator yoki ustunda osonlikcha markazga joylashtirish va joy taqsimlash vositasidir."
    },
    # 9
    {
        "text": "JavaScriptda foydalanuvchi tugmani bosganida (click) funksiyani ishga tushirish uchun qaysi metod ishlatiladi?",
        "a": "button.addEventListener('click', handlerFunction)",
        "b": "button.delete('click')",
        "c": "button.sendEmail('click')",
        "d": "button.restartSystem()",
        "e": "button.printDocument()",
        "correct": "A",
        "topic": "09: JS Hodisalari (Events)",
        "expl": "addEventListener hodisa eshituvchisini ulab, tugma bosilganda kerakli kodni ishga tushiradi."
    },
    # 10
    {
        "text": "Dasturchilar console.log() xabarlari va JavaScript xatoliklarini ko'rish uchun 'Konsol'ni qayerdan ochishadi?",
        "a": "Microsoft Paint dasturidan",
        "b": "Brauzerning dasturchilar panelidan (Developer Tools / F12)",
        "c": "Kompyuterning BIOS sozlamalari menyusidan",
        "d": "Noutbukning ovoz sozlamalaridan",
        "e": "Klaviatura tugmalari orqasidagi qog'ozdan",
        "correct": "B",
        "topic": "10: Brauzer Konsoli",
        "expl": "Brauzer DevTools konsoli dasturdagi xatolarni, ogohlantirishlarni va loglarni tekshirish joyidir."
    },
    # 11
    {
        "text": "Brauzerdagi 'localStorage' xotirasining asosiy vazifasi nima?",
        "a": "Fayllarni tashqi USB fleshkaga saqlash.",
        "b": "Sahifa yangilanganda yoki brauzer yopilganda ham o'chib ketmaydigan kalit-qiymat ma'lumotlarini brauzerda saqlash.",
        "c": "Kompyuterning jismoniy operativ xotirasini (RAM) oshirish.",
        "d": "Ochiq Wi-Fi orqali maxfiy parollarni ochiq yuborish.",
        "e": "Chek printeridan qog'oz chop etish.",
        "correct": "B",
        "topic": "11: Brauzer LocalStorage",
        "expl": "LocalStorage foydalanuvchi sozlamalari yoki rekordlarini (High Score) brauzer diskida doimiy saqlaydi."
    },
    # 12
    {
        "text": "API (Application Programming Interface) nima?",
        "a": "Monitorga ulanadigan jismoniy kabel.",
        "b": "Ikki xil mustaqil dasturning bir-biri bilan ma'lumot almashishiga imkon beruvchi dasturiy ko'prik.",
        "c": "Buzilgan fayllarni tekshiruvchi antivirus vositasi.",
        "d": "Yevropada ishlatiladigan klaviatura shakli.",
        "e": "Telefon zaryadlovchi yangi batareya standarti.",
        "correct": "B",
        "topic": "12: API Asoslari",
        "expl": "API ilovalar o'rtasida ma'lumot (masalan ob-havo ma'lumoti) so'rash va qabul qilish qoidalarini belgilaydi."
    },
    # 13
    {
        "text": "Quyidagilardan qaysi biri to'g'ri JSON (JavaScript Object Notation) formatini ifodalaydi?",
        "a": "{ \"username\": \"alex\", \"score\": 95, \"active\": true }",
        "b": "<username>alex</username><score>95</score>",
        "c": "username = alex, score = 95, active = true",
        "d": "SELECT * FROM users WHERE username = 'alex';",
        "e": "PRINT \"alex\" TO 95",
        "correct": "A",
        "topic": "13: JSON Formati",
        "expl": "JSON ma'lumotlarni jingalak qavs ichida kalit va qiymat ko'rinishida saqlaydi, kalitlar qo'shtirnoqda bo'ladi."
    },
    # 14
    {
        "text": "Veb-dasturlashda Frontend va Backend o'rtasidagi asosiy farq nimada?",
        "a": "Frontend foydalanuvchi brauzerida (UI/UX) ishlaydi, Backend esa uzoqdagi serverda (mantiq, baza, autentifikatsiya) ishlaydi.",
        "b": "Frontend faqat ikkilik tilda yoziladi, Backend esa inglizcha so'zlardan iborat.",
        "c": "Frontend sichqoncha kabi qurilma, Backend esa o'yin dasturi.",
        "d": "Frontendga elektr kerak emas, Backend esa batareyadan quvvat oladi.",
        "e": "Frontend rasm ko'rsata olmaydi, Backend esa faqat rasm ko'rsatadi.",
        "correct": "A",
        "topic": "14: Frontend va Backend",
        "expl": "Frontend vizual interfeysni, Backend esa serverdagi xavfsiz mantiq va ma'lumotlar bazasini boshqaradi."
    },
    # 15
    {
        "text": "Nima uchun dasturchilar o'z loyihalarida Git tizimidan foydalanadilar?",
        "a": "Video fayllarni kichik hajmga siqish uchun.",
        "b": "Koddagi o'zgarishlar tarixini saqlash, alohida tarmoqlar (branch) ochish va xatolik bo'lsa orqaga qaytish uchun.",
        "c": "Kompyuterning anakartini yangisiga almashtirish uchun.",
        "d": "Har oyda server to'lovlarini avtomatik to'lash uchun.",
        "e": "Ijtimoiy tarmoqlar uchun tasodifiy parollar o'ylab topish uchun.",
        "correct": "B",
        "topic": "15: Git Versiyalar Nazorati",
        "expl": "Git kod tarixini saqlab boradi va bir nechta dasturchining birga erkin ishlashiga yordam beradi."
    },
    # 16
    {
        "text": "Nima uchun maxfiy API kalitlari brauzer kodida ochiq qoldirilmasdan, alohida '.env' faylida saqlanishi kerak?",
        "a": "Chunki JavaScript 10 ta belgidan uzun matnni o'qiy olmaydi.",
        "b": "Begonalar GitHubdagi ochiq kodingizni ko'rib, maxfiy kalitingiz va hisobingizdagi mablag'ni o'g'irlamasligi uchun.",
        "c": "Chunki .env fayli internet tezligini ikki barobar oshiradi.",
        "d": "Chunki 5 ta belgidan uzun kod brauzerni qotirib qo'yadi.",
        "e": "Chunki brauzerlar kaliti bo'lmagan saytlarga ruxsat bermaydi.",
        "correct": "B",
        "topic": "16: Maxfiy kalitlar (.env)",
        "expl": "Maxfiy API kalitlari ochiq qolsa, kiber-hujumchilar ularni o'g'irlab, hisobingizdan suiiste'mol qilishi mumkin."
    },
    # 17
    {
        "text": "Veb-loyihani internetga 'Deploy qilish' (masalan, Vercel yoki Netlify orqali) nimani anglatadi?",
        "a": "Loyihani o'chirib, operatsion tizimni qayta o'rnatish.",
        "b": "Loyihani bulutli serverga joylab, butun dunyodagi foydalanuvchilar kirishi uchun unga jonli internet havolasini (URL) berish.",
        "c": "Kodni qog'ozga printerdan chop etib chiqish.",
        "d": "Veb-saytni audio podkast fayliga aylantirish.",
        "e": "Kompyuterda oflayn rejimda viruslarni tekshirish.",
        "correct": "B",
        "topic": "17: Veb-Deploy",
        "expl": "Deploy qilish orqali dasturchi o'z loyihasini hammaga ko'rinadigan global internet manziliga joylashtiradi."
    },
    # 18
    {
        "text": "AI yozib bergan kod ishlamay qolsa, Vibecodingda eng samarali va to'g'ri yo'l qaysi?",
        "a": "Darhol loyihani tashlab, boshqa mavzuga o'tib ketish.",
        "b": "Konsoldagi aniq xatolik matnini (Error va Stack trace) nusxalab, AI ga berish va sababini so'rash.",
        "c": "AI chatiga hech qanday kodsiz 20 ta jahl chiqqan smaylik yuborish.",
        "d": "Kompyuterni o'chirib, 24 soat kutish.",
        "e": "Xotirani tozalash uchun operatsion tizimni o'chirib yuborish.",
        "correct": "B",
        "topic": "18: AI bilan Debugging",
        "expl": "Xatolik matnini aniq ko'rsatish AI ga muammoni darhol topish va to'g'ri yechim berish imkonini yaratadi."
    },
    # 19
    {
        "text": "Murakkab vazifalarda AI ga 'Qadam-baqadam fikrla' (Chain-of-Thought) deb yozish nima uchun foydali?",
        "a": "Kompyuter qizib ketmasligi uchun internetni sekinlashtiradi.",
        "b": "Modelga yakuniy kodni yozishdan oldin mantiqni qadamma-qadam tahlil qilishga majbur qilib, xatoliklarni keskin kamaytiradi.",
        "c": "Kodni avtomatik ravishda 10 ta chet tiliga tarjima qilib beradi.",
        "d": "Barcha xatoliklar paydo bo'lishini 100% yo'qotadi.",
        "e": "Internetdagi barcha sayt parollarini chetlab o'tadi.",
        "correct": "B",
        "topic": "19: Chain-of-Thought",
        "expl": "Qadamma-qadam mulohaza yuritish murakkab algoritmlarni yechishda AI aniqligini sezilarli oshiradi."
    },
    # 20
    {
        "text": "JavaScriptda fetch() kabi asinxron so'rovlarning asosiy vazifasi nima?",
        "a": "Server javob berguncha butun kompyuterni qotirib qo'yish.",
        "b": "Foydalanuvchi interfeysini qotirib qo'ymasdan, orqa fonda serverdan ma'lumot olish uchun HTTP so'rov yuborish.",
        "c": "Brauzer oynasini 5 soniyadan keyin avtomatik yopish.",
        "d": "Kompyuter qattiq diskini avtomatik formatlash.",
        "e": "Fleshkani jismoniy jihatdan otib chiqarish.",
        "correct": "B",
        "topic": "20: Asinxron Fetch",
        "expl": "Asinxron fetch sahifani to'xtatib qo'ymaydi, balki foydalanuvchi ishlayotgan paytda orqada ma'lumot olib keladi."
    },
    # 21
    {
        "text": "Brauzerning 'Network' panelida HTTP 404 kodi chiqsa, bu nimani bildiradi?",
        "a": "200 OK — So'rov muvaffaqiyatli bajarildi.",
        "b": "Not Found — So'ralgan veb-sahifa yoki manzil serverda topilmadi.",
        "c": "Unauthorized — Foydalanuvchi login va parol kiritishi shart.",
        "d": "Internal Server Error — Server ichida nosozlik yuz berdi.",
        "e": "Payment Required — Sahifani ko'rish uchun pul to'lash kerak.",
        "correct": "B",
        "topic": "21: HTTP 404 Statusi",
        "expl": "404 Not Found — manzil noto'g'ri kiritilganida yoki fayl o'chirib yuborilganida qaytadigan xatolik kodi."
    },
    # 22
    {
        "text": "AI dasturlariga nisbatan 'Prompt Injection' kiber-hujumi nima?",
        "a": "Kompyuter ekraniga siyoh quyib yuborish.",
        "b": "Sun'iy intellektni o'zining xavfsizlik qoidalarini buzishga va yopiq sirlarni ochishga majburlovchi ayyorona so'rov kiritish.",
        "c": "Sovutish faniga suyuq azot quyish.",
        "d": "Rasmiy saytdan antivirus yangilanishini o'rnatish.",
        "e": "Faqat bitta qo'l bilan klaviaturada yozish.",
        "correct": "B",
        "topic": "22: Prompt Injection hujumi",
        "expl": "Prompt injection orqali xakerlar AI ni aldab, uning ichki tizim ko'rsatmalarini buzishga urinadilar."
    },
    # 23
    {
        "text": "AI bilan murakkab loyihalarni yaratishda (Vibecoding) eng yaxshi amaliyot qaysi?",
        "a": "Bitta ulkan promptda 5000 qatorli to'liq dasturni yozib berishni so'rash.",
        "b": "Dasturni kichik modullarga bo'lib, har bir qismni tekshirib va sinab, qadamma-qadam qurish.",
        "c": "Butun loyiha 100% tugamaguncha kodni hech qachon ishga tushirmaslik.",
        "d": "AI yaratgan kodlarni umuman o'qib ko'rmaslik.",
        "e": "AI nima kerakligini o'zi tushuntirmasdan topib olishini kutish.",
        "correct": "B",
        "topic": "23: Qadamma-qadam Ishlash",
        "expl": "Bosqichma-bosqich (iterativ) yaratish orqali xatolar darhol aniqlanadi va loyiha mustahkam bo'ladi."
    },
    # 24
    {
        "text": "Veb-saytga kirganda HTTPS va SSL/TLS shifrlash bizni nimalardan himoya qiladi?",
        "a": "Ochiq Wi-Fi tarmoqlarida parollar, cookie va shaxsiy ma'lumotlarni xakerlar tutib olishi va o'g'irlashidan.",
        "b": "Noutbuk batareyasi hech qachon tugab qolmasligidan.",
        "c": "Kodda hech qanday xatoliklar (bug) paydo bo'lmasligidan.",
        "d": "Monitor ekranining o'lchami kattalashib ketishidan.",
        "e": "Maktab uy vazifalarini avtomatik bajarib berishdan.",
        "correct": "A",
        "topic": "24: HTTPS Shifrlash",
        "expl": "HTTPS brauzer va server o'rtasidagi barcha ma'lumotlarni shifrlab, tarmoqdagi josuslikdan himoya qiladi."
    },
    # 25
    {
        "text": "Zamonaviy AI tizimlarida RAG (Retrieval-Augmented Generation) texnologiyasi nima uchun kerak?",
        "a": "Veb-sayt foni uchun tasodifiy ranglar tanlash uchun.",
        "b": "AI ga javob berishdan oldin tashqi ishonchli hujjatlar va bazadan aniq faktlarni topib berib, gallyutsinatsiyalarni yo'qotish uchun.",
        "c": "Qattiq diskdan eski fayllarni tozalab tashlash uchun.",
        "d": "Noutbuk dinamiklarining ovoz balandligini oshirish uchun.",
        "e": "10 daqiqa harakatsizlikdan so'ng kompyuterni o'chirib qo'yish uchun.",
        "correct": "B",
        "topic": "25: RAG Texnologiyasi",
        "expl": "RAG modeli javob berishdan oldin haqiqiy hujjatlarni o'qib oladi va soxta ma'lumot to'qib chiqarishining oldini oladi."
    }
]

QUESTIONS_10_11_RU = [
    # 1
    {
        "text": "В чем заключается ключевая философия «Vibecoding» в современной разработке ПО?",
        "a": "На 100% доверять ИИ, никогда не запуская и не тестируя код.",
        "b": "Писать весь код вручную в двоичном машинном коде.",
        "c": "Направлять ИИ-ассистентов на генерацию кода, пока разработчик-человек проектирует архитектуру, логику и тесты.",
        "d": "Копировать устаревшие фрагменты кода из старых бумажных учебников.",
        "e": "Отключать интернет при разработке веб-сайта.",
        "correct": "C",
        "topic": "01: Философия Vibecoding",
        "expl": "Vibecoding позволяет делегировать кодинг ИИ при сохранении человеческого контроля, архитектуры и тестов."
    },
    # 2
    {
        "text": "Какая часть промпта задает роль модели (персону), правила поведения и системные ограничения?",
        "a": "Скрипт настройки Wi-Fi",
        "b": "Системный промпт (System Prompt или системная инструкция)",
        "c": "Настройки BIOS компьютера",
        "d": "Таблица стилей CSS",
        "e": "Драйвер HDMI экрана",
        "correct": "B",
        "topic": "02: Системные промпты",
        "expl": "System Prompt задает роль, формат ответов, ограничения и правила поведения ИИ."
    },
    # 3
    {
        "text": "Что означает «Few-Shot Prompting» при работе с ИИ?",
        "a": "Предоставление ИИ 1–3 четких примеров входных и выходных данных (input-output) перед выполнением новой задачи.",
        "b": "Запрос к ИИ, состоящий ровно из трех слов.",
        "c": "Трехкратная перезагрузка компьютера перед отправкой промпта.",
        "d": "Одновременная отправка трех одинаковых запросов для сбоя сервера.",
        "e": "Запуск кода одновременно на трех отдельных мониторах.",
        "correct": "A",
        "topic": "03: Few-Shot промптинг",
        "expl": "Few-Shot промптинг через примеры показывает модели точный формат и логику ответа."
    },
    # 4
    {
        "text": "Что означает «Галлюцинация» (Hallucination) искусственного интеллекта?",
        "a": "Мерцание экрана разными цветами из-за поврежденного кабеля.",
        "b": "Ситуация, когда ИИ с высокой уверенностью выдумывает несуществующие библиотеки, функции или ложные факты.",
        "c": "Падение температуры процессора ниже нуля градусов.",
        "d": "Быстрая разрядка аккумулятора ноутбука.",
        "e": "Открытие двух вкладок браузера вместо одной.",
        "correct": "B",
        "topic": "04: Галлюцинации ИИ",
        "expl": "Галлюцинация — это генерация правдоподобно звучащего, но вымышленного и ложного кода или фактов."
    },
    # 5
    {
        "text": "Какой эффект дает установка параметра «Temperature» языковой модели (LLM) на значение 0.0?",
        "a": "Модель полностью отключается и перестает отвечать.",
        "b": "Модель становится максимально творческой, случайной и пишет вымышленные истории.",
        "c": "Ответы становятся сфокусированными, детерминированными и предсказуемо повторяемыми для одного промпта.",
        "d": "Скорость домашнего интернета резко увеличивается.",
        "e": "Модель автоматически удаляет весь проект с компьютера.",
        "correct": "C",
        "topic": "05: Температура LLM",
        "expl": "Низкая температура (близкая к 0) устраняет случайность и делает код строгим и воспроизводимым."
    },
    # 6
    {
        "text": "Что означает «Контекстное окно» (Context Window) модели искусственного интеллекта?",
        "a": "Физическое стеклянное окно в компьютерном классе.",
        "b": "Максимальный объем токенов (слов/символов), который модель может удерживать в памяти за одну сессию.",
        "c": "Фоновый рисунок рабочего стола операционной системы.",
        "d": "Размер окна браузера в пикселях.",
        "e": "Объем свободного места на жестком диске.",
        "correct": "B",
        "topic": "06: Контекстное окно",
        "expl": "Контекстное окно — это лимит памяти модели на ввод и генерацию текста в одном диалоге."
    },
    # 7
    {
        "text": "Какую фундаментальную роль выполняет HTML при создании веб-приложений?",
        "a": "Задает базовую структуру и семантическое содержимое страницы (заголовки, текст, кнопки, формы).",
        "b": "Напрямую подключает компьютер к серверу баз данных.",
        "c": "Стилизует страницу тенями, градиентами и анимациями.",
        "d": "Выполняет серверные фоновые задачи и шифрование данных.",
        "e": "Компилирует JavaScript в машинный код.",
        "correct": "A",
        "topic": "07: Структура HTML",
        "expl": "HTML является скелетом и смысловым фундаментом любой веб-страницы."
    },
    # 8
    {
        "text": "Какое свойство CSS чаще всего используется для простого выравнивания элементов по центру и распределения пространства?",
        "a": "display: flex (вместе с justify-content и align-items)",
        "b": "text-decoration: underline",
        "c": "color: transparent",
        "d": "font-weight: bold",
        "e": "cursor: pointer",
        "correct": "A",
        "topic": "08: Сетка Flexbox в CSS",
        "expl": "Flexbox позволяет гибко выравнивать и центрировать дочерние блоки по главной и поперечной осям."
    },
    # 9
    {
        "text": "Какой метод используется в JavaScript для запуска функции при клике пользователя по кнопке?",
        "a": "button.addEventListener('click', handlerFunction)",
        "b": "button.delete('click')",
        "c": "button.sendEmail('click')",
        "d": "button.restartSystem()",
        "e": "button.printDocument()",
        "correct": "A",
        "topic": "09: События в JavaScript",
        "expl": "addEventListener привязывает обработчик событий клика к элементу на веб-странице."
    },
    # 10
    {
        "text": "Где веб-разработчики открывают «Консоль» для просмотра сообщений console.log() и ошибок JavaScript?",
        "a": "В программе Microsoft Paint",
        "b": "В инструментах разработчика браузера (Developer Tools / F12)",
        "c": "В меню настроек BIOS компьютера",
        "d": "В настройках звука ноутбука",
        "e": "Под физическими клавишами клавиатуры",
        "correct": "B",
        "topic": "10: Консоль разработчика",
        "expl": "Консоль DevTools показывает логи, предупреждения и runtime ошибки скриптов."
    },
    # 11
    {
        "text": "В чем основное назначение хранилища «localStorage» в браузере?",
        "a": "Сохранять файлы на внешнюю USB-флешку.",
        "b": "Сохранять данные (ключ-значение) прямо в браузере пользователя так, чтобы они не стирались при обновлении страницы.",
        "c": "Физически увеличивать оперативную память (RAM) компьютера.",
        "d": "Передавать секретные пароли по открытой сети Wi-Fi.",
        "e": "Печатать квитанции на чековом принтере.",
        "correct": "B",
        "topic": "11: Хранилище LocalStorage",
        "expl": "LocalStorage сохраняет строковые пары ключ-значение на диске браузера между перезагрузками."
    },
    # 12
    {
        "text": "Что такое API (Application Programming Interface)?",
        "a": "Физический кабель, подключаемый к монитору.",
        "b": "Программный интерфейс, позволяющий разным приложениям обмениваться данными между собой.",
        "c": "Антивирусная утилита для проверки жесткого диска.",
        "d": "Особый вид раскладки клавиатуры.",
        "e": "Новый стандарт аккумуляторов для зарядки телефонов.",
        "correct": "B",
        "topic": "12: Основы API",
        "expl": "API определяет набор правил, по которым приложения взаимодействуют и запрашивают данные."
    },
    # 13
    {
        "text": "Какая из следующих записей представляет корректный формат JSON (JavaScript Object Notation)?",
        "a": "{ \"username\": \"alex\", \"score\": 95, \"active\": true }",
        "b": "<username>alex</username><score>95</score>",
        "c": "username = alex, score = 95, active = true",
        "d": "SELECT * FROM users WHERE username = 'alex';",
        "e": "PRINT \"alex\" TO 95",
        "correct": "A",
        "topic": "13: Формат данных JSON",
        "expl": "JSON организует структурированные данные в фигурных скобках в формате пар ключ-значение."
    },
    # 14
    {
        "text": "В чем главное отличие между Frontend и Backend в веб-разработке?",
        "a": "Frontend работает в браузере пользователя (UI/UX интерфейс), а Backend — на сервере (логика, база данных, авторизация).",
        "b": "Frontend пишется только на двоичном коде, а Backend — обычными словами.",
        "c": "Frontend — это устройство вроде мышки, а Backend — компьютерная игра.",
        "d": "Frontend не требует электричества, а Backend работает от аккумулятора.",
        "e": "Frontend не умеет показывать картинки, а Backend показывает только изображения.",
        "correct": "A",
        "topic": "14: Frontend и Backend",
        "expl": "Frontend отвечает за визуальную часть и интерфейс, Backend — за обработку данных на сервере."
    },
    # 15
    {
        "text": "Зачем разработчики используют систему контроля версий Git в своих проектах?",
        "a": "Чтобы сжимать видеофайлы в меньший объем.",
        "b": "Чтобы сохранять историю изменений кода, создавать ветки для функций и откатывать ошибки при необходимости.",
        "c": "Чтобы заменить материнскую плату компьютера.",
        "d": "Чтобы автоматически оплачивать хостинг серверов.",
        "e": "Чтобы придумывать пароли для социальных сетей.",
        "correct": "B",
        "topic": "15: Контроль версий Git",
        "expl": "Git отслеживает историю изменений в коде и упрощает командную работу над проектами."
    },
    # 16
    {
        "text": "Почему секретные API-ключи должны храниться в файле `.env`, а не быть открыто записаны в клиентском JavaScript?",
        "a": "Потому что JavaScript не может читать строки длиннее 10 символов.",
        "b": "Чтобы злоумышленники не смогли увидеть секретные ключи в публичном коде на GitHub и украсть доступ и баланс.",
        "c": "Потому что файл .env удваивает скорость загрузки страниц.",
        "d": "Потому что клиентский код зависает при длинных ключах.",
        "e": "Потому что браузеры блокируют сайты без файла .env.",
        "correct": "B",
        "topic": "16: Секреты окружения (.env)",
        "expl": "Хранение ключей в .env файлах защищает конфиденциальные токены доступа от утечек в сеть."
    },
    # 17
    {
        "text": "Что означает «Деплой» (Deployment) веб-приложения (например, на платформу Vercel или Netlify)?",
        "a": "Удаление репозитория и переустановка системы.",
        "b": "Публикация приложения на облачном сервере, чтобы пользователи со всего мира могли открывать его по ссылке (URL).",
        "c": "Распечатка исходного кода на бумаге.",
        "d": "Конвертация веб-сайта в аудиофайл подкаста.",
        "e": "Проверка компьютера на вирусы в офлайн-режиме.",
        "correct": "B",
        "topic": "17: Деплой веб-приложений",
        "expl": "Деплой делает проект общедоступным в интернете по постоянному веб-адресу."
    },
    # 18
    {
        "text": "Какой способ является самым эффективным в Vibecoding, если сгенерированный ИИ код выдает ошибку?",
        "a": "Сразу бросить проект и заняться другой темой. ",
        "b": "Скопировать точный текст ошибки из консоли (Error и Stack trace) и спросить у ИИ причину и способ исправления.",
        "c": "Отправить в чат 20 сердитых смайликов без текста ошибки.",
        "d": "Выключить компьютер и ждать 24 часа.",
        "e": "Удалить системные файлы для очистки памяти.",
        "correct": "B",
        "topic": "18: Отладка ошибок с ИИ",
        "expl": "Предоставление текста ошибки и логов позволяет ИИ точно локализовать баг и предложить исправление."
    },
    # 19
    {
        "text": "Почему для сложных задач полезен метод «Chain-of-Thought» (указание «Думай шаг за шагом»)?",
        "a": "Замедляет интернет, чтобы ноутбук не перегрелся.",
        "b": "Заставляет модель рассуждать последовательно перед выводом ответа, что резко снижает логические ошибки в коде.",
        "c": "Автоматически переводит код на 10 иностранных языков.",
        "d": "Гарантирует вечное отсутствие любых багов в программе.",
        "e": "Позволяет обходить пароли на любых сайтах.",
        "correct": "B",
        "topic": "19: Пошаговое рассуждение",
        "expl": "Пошаговая цепочка рассуждений помогает модели не пропускать логические этапы при решении сложных задач."
    },
    # 20
    {
        "text": "В чем роль асинхронных операций, таких как fetch(), в JavaScript?",
        "a": "Заморозить экран компьютера до ответа сервера.",
        "b": "Отправлять HTTP-запрос на сервер в фоновом режиме, не блокируя работу интерфейса для пользователя.",
        "c": "Автоматически закрывать вкладку браузера через 5 секунд.",
        "d": "Форматировать жесткий диск компьютера.",
        "e": "Физически выбрасывать флешку из разъема.",
        "correct": "B",
        "topic": "20: Асинхронный fetch в JS",
        "expl": "fetch() запрашивает данные с сервера асинхронно, оставляя интерфейс отзывчивым для пользователя."
    },
    # 21
    {
        "text": "Что означает HTTP статус 404 во вкладке «Network» инструментов разработчика?",
        "a": "200 OK — Запрос выполнен полностью успешно.",
        "b": "Not Found — Запрашиваемая страница или файл не найдены на сервере.",
        "c": "Unauthorized — Требуется ввод логина и пароля.",
        "d": "Internal Server Error — Сервер упал с ошибкой.",
        "e": "Payment Required — Для просмотра страницы требуется оплата.",
        "correct": "B",
        "topic": "21: HTTP статус 404",
        "expl": "Код 404 указывает, что сервер доступен, но запрашиваемый ресурс по указанному URL отсутствует."
    },
    # 22
    {
        "text": "Что представляет собой атака «Prompt Injection» на ИИ-приложения?",
        "a": "Заливка экрана компьютера чернилами.",
        "b": "Ввод специально составленного текста, заставляющего ИИ проигнорировать правила безопасности и выдать скрытые данные.",
        "c": "Охлаждение компьютера жидким азотом.",
        "d": "Установка официального обновления антивируса.",
        "e": "Набор текста на клавиатуре одной рукой.",
        "correct": "B",
        "topic": "22: Атака Prompt Injection",
        "expl": "Вредоносный ввод пользователя пытается переопределить системные правила и заставить ИИ выдать секреты."
    },
    # 23
    {
        "text": "Какая практика является лучшей при создании сложных проектов с помощью ИИ (Vibecoding)?",
        "a": "Просить ИИ написать приложение на 5000 строк кода в одном гигантском запросе.",
        "b": "Разрабатывать приложение модульно, шаг за шагом тестируя и проверяя каждый компонент.",
        "c": "Ни разу не запускать код до тех пор, пока проект не завершен полностью.",
        "d": "Вообще не читать код, создаваемый ИИ-ассистентом.",
        "e": "Ждать, пока ИИ сам догадается обо всех функциях без объяснений.",
        "correct": "B",
        "topic": "23: Итеративная разработка",
        "expl": "Пошаговая модульная разработка позволяет контролировать качество кода на каждом этапе."
    },
    # 24
    {
        "text": "От чего защищает протокол HTTPS с шифрованием SSL/TLS при посещении сайтов?",
        "a": "От перехвата паролей, файлов cookie и личных данных злоумышленниками в публичных сетях Wi-Fi.",
        "b": "От полной разрядки аккумулятора ноутбука.",
        "c": "От появления любых багов в коде приложения.",
        "d": "От изменения физического размера экрана.",
        "e": "От необходимости делать домашние задания.",
        "correct": "A",
        "topic": "24: Шифрование HTTPS",
        "expl": "HTTPS шифрует весь сетевой трафик, предотвращая перехват чувствительных данных третьими лицами."
    },
    # 25
    {
        "text": "Для чего в современных ИИ-системах используется технология RAG (Retrieval-Augmented Generation)?",
        "a": "Для подбора случайных цветов фона веб-страницы.",
        "b": "Для поиска точных проверенных фактов в базе документов и передачи их модели перед ответом, чтобы исключить галлюцинации.",
        "c": "Для удаления старых файлов с жесткого диска.",
        "d": "Для увеличения громкости динамиков ноутбука.",
        "e": "Для автоматического выключения компьютера через 10 минут.",
        "correct": "B",
        "topic": "25: Технология RAG",
        "expl": "RAG извлекает актуальные факты из доверенных документов и передает их в контекст ИИ для генерации точных ответов."
    }
]

# Keep QUESTIONS_10_11_EN for pure English version
QUESTIONS_10_11_EN = [
    # 1
    {
        "text": "In modern software engineering, what is the core philosophy of 'Vibecoding'?",
        "a": "Relying 100% on AI without ever testing or running the code.",
        "b": "Writing all code in binary machine language by hand.",
        "c": "Guiding and directing AI assistants to generate code while the human developer plans the architecture, logic, and tests.",
        "d": "Copying outdated code snippets from old printed textbooks.",
        "e": "Disabling all internet access while building a website.",
        "correct": "C",
        "topic": "01: Vibecoding Philosophy",
        "expl": "Vibecoding empowers developers to direct AI models to write code while maintaining human architectural vision and testing."
    },
    # 2
    {
        "text": "Which component of an AI prompt establishes the model's persona, rules, and behavioral boundaries?",
        "a": "The Wi-Fi configuration script",
        "b": "The System Prompt (or system instruction)",
        "c": "The computer's BIOS settings",
        "d": "The CSS style sheet",
        "e": "The HDMI display driver",
        "correct": "B",
        "topic": "02: System Prompts",
        "expl": "The System Prompt defines the AI's role, behavioral guidelines, constraints, and operational context."
    },
    # 3
    {
        "text": "What is 'Few-Shot Prompting' when instructing an AI model?",
        "a": "Providing the AI with 1 to 3 clear examples of expected input-output pairs before asking it to solve a new task.",
        "b": "Asking the AI only three words in total.",
        "c": "Restarting the computer three times before submitting a prompt.",
        "d": "Sending three identical prompts simultaneously to crash the server.",
        "e": "Running code on three separate monitors at the same time.",
        "correct": "A",
        "topic": "03: Few-Shot Prompting",
        "expl": "Few-shot prompting provides concrete input-output examples so the AI can recognize patterns and format responses accurately."
    },
    # 4
    {
        "text": "What is meant by an AI 'Hallucination'?",
        "a": "When the computer monitor displays random colors due to a broken cable.",
        "b": "When an AI model generates factually incorrect or non-existent code libraries with high confidence.",
        "c": "When the computer's CPU temperature drops below zero degrees.",
        "d": "When the battery of a laptop drains faster than expected.",
        "e": "When a web browser opens two tabs instead of one.",
        "correct": "B",
        "topic": "04: AI Hallucinations",
        "expl": "AI hallucination refers to plausible-sounding but factually wrong outputs, such as inventing functions or fake API endpoints."
    },
    # 5
    {
        "text": "When adjusting the 'Temperature' parameter of a Large Language Model (LLM), what is the effect of setting it to 0.0?",
        "a": "The AI model completely shuts down and stops answering.",
        "b": "The model becomes highly creative, unpredictable, and writes fictional stories.",
        "c": "The outputs become focused, deterministic, and repeatable for the same prompt.",
        "d": "The speed of your home Wi-Fi connection increases.",
        "e": "The model automatically deletes your codebase.",
        "correct": "C",
        "topic": "05: LLM Temperature",
        "expl": "Low temperature (near 0) produces deterministic and predictable outputs, ideal for structured code generation."
    },
    # 6
    {
        "text": "What does the 'Context Window' of an AI model refer to?",
        "a": "The physical glass window in a computer laboratory.",
        "b": "The maximum number of tokens (words/characters) the model can read and remember in a single session.",
        "c": "The operating system's desktop background wallpaper.",
        "d": "The dimensions of the browser window in pixels.",
        "e": "The amount of free space remaining on a hard drive.",
        "correct": "B",
        "topic": "06: Context Window",
        "expl": "The context window represents the memory limit of an AI model for input prompts and generated responses."
    },
    # 7
    {
        "text": "In web development, what role does HTML play in creating a web application?",
        "a": "It defines the foundational structure and semantic content (headings, paragraphs, buttons, forms).",
        "b": "It connects the computer directly to a database server.",
        "c": "It styles the page with shadows, gradients, and animations.",
        "d": "It executes server-side background tasks and handles cryptography.",
        "e": "It compiles JavaScript code into binary machine code.",
        "correct": "A",
        "topic": "07: HTML Structure",
        "expl": "HTML provides the structural skeleton and DOM elements of a webpage."
    },
    # 8
    {
        "text": "Which CSS property is commonly used to easily center and distribute child elements horizontally and vertically?",
        "a": "display: flex (with justify-content and align-items)",
        "b": "text-decoration: underline",
        "c": "color: transparent",
        "d": "font-weight: bold",
        "e": "cursor: pointer",
        "correct": "A",
        "topic": "08: CSS Flexbox Layout",
        "expl": "Flexbox provides powerful layout tools to align and space items along main and cross axes."
    },
    # 9
    {
        "text": "In JavaScript, what method is used to execute a function when a user clicks a button?",
        "a": "button.addEventListener('click', handlerFunction)",
        "b": "button.delete('click')",
        "c": "button.sendEmail('click')",
        "d": "button.restartSystem()",
        "e": "button.printDocument()",
        "correct": "A",
        "topic": "09: JavaScript Event Listeners",
        "expl": "addEventListener('click', ...) binds an event listener to handle user interactions on DOM elements."
    },
    # 10
    {
        "text": "Where can developers open the 'Console' to view logged messages and JavaScript runtime errors?",
        "a": "In Microsoft Paint",
        "b": "Inside the Browser Developer Tools (Inspect / F12)",
        "c": "In the computer's BIOS setup menu",
        "d": "Inside the laptop's sound settings",
        "e": "On the physical keyboard labels",
        "correct": "B",
        "topic": "10: Browser DevTools Console",
        "expl": "The browser Developer Tools console displays console.log() statements, warnings, and uncaught runtime errors."
    },
    # 11
    {
        "text": "What is the primary purpose of browser 'localStorage'?",
        "a": "To store permanent files on an external USB flash drive.",
        "b": "To save key-value data directly in the user's browser that persists even after closing or refreshing the tab.",
        "c": "To increase the physical RAM memory of the computer.",
        "d": "To transmit secret passwords across open Wi-Fi networks.",
        "e": "To print receipts from a connected receipt printer.",
        "correct": "B",
        "topic": "11: Browser LocalStorage",
        "expl": "LocalStorage allows web apps to save lightweight key-value pairs (like theme or score) across browser sessions."
    },
    # 12
    {
        "text": "What is an API (Application Programming Interface)?",
        "a": "A physical cable that plugs into a computer monitor.",
        "b": "A software intermediary that allows two different applications to communicate and exchange data.",
        "c": "An antivirus tool that scans files for corrupted sectors.",
        "d": "A type of physical keyboard layout used in Europe.",
        "e": "A battery charging standard for mobile devices.",
        "correct": "B",
        "topic": "12: What is an API",
        "expl": "APIs define protocols and rules that allow distinct software services (like web apps and weather servers) to talk."
    },
    # 13
    {
        "text": "Which of the following represents valid JSON (JavaScript Object Notation)?",
        "a": "{ \"username\": \"alex\", \"score\": 95, \"active\": true }",
        "b": "<username>alex</username><score>95</score>",
        "c": "username = alex, score = 95, active = true",
        "d": "SELECT * FROM users WHERE username = 'alex';",
        "e": "PRINT \"alex\" TO 95",
        "correct": "A",
        "topic": "13: JSON Data Format",
        "expl": "JSON formats data as key-value pairs enclosed in curly braces with double-quoted string keys."
    },
    # 14
    {
        "text": "What is the key distinction between Frontend and Backend in web development?",
        "a": "Frontend runs in the user's browser (UI/UX), while Backend runs on a remote server (logic, database, authentication).",
        "b": "Frontend is written only in binary, while Backend is written in English.",
        "c": "Frontend is hardware like mice, while Backend is software like games.",
        "d": "Frontend requires no electricity, while Backend uses battery power.",
        "e": "Frontend cannot display images, while Backend only displays images.",
        "correct": "A",
        "topic": "14: Frontend vs Backend",
        "expl": "The Frontend handles presentation and client interactions, while the Backend processes business logic and data storage."
    },
    # 15
    {
        "text": "Why do developers use Git version control in their coding projects?",
        "a": "To compress video files into smaller zip archives.",
        "b": "To track changes in source code over time, create branches for features, and revert bugs if needed.",
        "c": "To replace the computer's motherboard with an upgraded model.",
        "d": "To automatically pay monthly server hosting bills.",
        "e": "To generate random passwords for social media accounts.",
        "correct": "B",
        "topic": "15: Git Version Control",
        "expl": "Git tracks code history, manages branching, and facilitates collaborative development."
    },
    # 16
    {
        "text": "Why should private API keys (e.g. OpenAI or Gemini API keys) be kept in an environment file (like '.env') rather than hardcoded in public client-side JavaScript?",
        "a": "Because JavaScript cannot read text longer than 10 characters.",
        "b": "To prevent anyone from inspecting your public code on GitHub and stealing your private API credentials and credits.",
        "c": "Because .env files automatically double the speed of your internet.",
        "d": "Because client-side code will crash if any key is longer than 5 digits.",
        "e": "Because browsers only allow websites that lack API keys.",
        "correct": "B",
        "topic": "16: Environment Secrets (.env)",
        "expl": "Secret API keys must stay server-side or in .env to prevent malicious actors from extracting and abusing them."
    },
    # 17
    {
        "text": "What does 'Deploying' a web application mean?",
        "a": "Deleting the repository and reinstalling the operating system.",
        "b": "Publishing the application onto a web server (like Vercel or Netlify) so users worldwide can access it via a URL.",
        "c": "Printing out the source code on A4 paper sheets.",
        "d": "Converting the web application into an audio podcast file.",
        "e": "Running an offline virus scan on your local computer.",
        "correct": "B",
        "topic": "17: Web Application Deployment",
        "expl": "Deploying transfers built web assets to live cloud servers, making the website accessible via a public domain name."
    },
    # 18
    {
        "text": "When an AI chatbot writes a piece of code that does not work, what is the most effective Vibecoding debugging strategy?",
        "a": "Give up immediately and change your project topic.",
        "b": "Copy the exact console error message and stack trace, and prompt the AI: 'Here is the error I received, what caused it and how do I fix it?'.",
        "c": "Send 20 angry emojis to the AI chatbot without any code.",
        "d": "Turn off your computer and wait 24 hours.",
        "e": "Delete your operating system files to clear memory.",
        "correct": "B",
        "topic": "18: Effective AI Debugging",
        "expl": "Providing full error traces and context enables AI assistants to accurately pinpoint syntax or logical flaws."
    },
    # 19
    {
        "text": "Why is 'Chain-of-Thought' prompting (asking the AI to 'think step by step') helpful for complex programming tasks?",
        "a": "It slows down your internet so the computer doesn't overheat.",
        "b": "It forces the model to break down multi-step logic sequentially before producing the final code, reducing reasoning errors.",
        "c": "It automatically translates code into 10 different foreign languages.",
        "d": "It guarantees that no bugs will ever occur in any computer program.",
        "e": "It bypasses all password security protections on the web.",
        "correct": "B",
        "topic": "19: Chain-of-Thought Prompting",
        "expl": "Step-by-step reasoning enables LLMs to decompose complex logic into intermediate stages, significantly improving accuracy."
    },
    # 20
    {
        "text": "In JavaScript, what is the role of an asynchronous operation like 'fetch()'?",
        "a": "It freezes the entire computer until the server responds.",
        "b": "It sends an HTTP network request to retrieve data from a server in the background without blocking the user interface.",
        "c": "It shuts down the browser tab after 5 seconds.",
        "d": "It formats the computer's hard drive automatically.",
        "e": "It physically ejects the USB flash drive.",
        "correct": "B",
        "topic": "20: Asynchronous Fetch in JavaScript",
        "expl": "fetch() performs non-blocking asynchronous HTTP requests, retrieving remote data while the user interface stays responsive."
    },
    # 21
    {
        "text": "When inspecting web requests in the DevTools 'Network' tab, what does an HTTP status code of 404 signify?",
        "a": "200 OK — The request was completely successful.",
        "b": "Not Found — The server could not locate the requested resource or URL.",
        "c": "Unauthorized — The user needs to enter a username and password.",
        "d": "Internal Server Error — The server crashed.",
        "e": "Payment Required — The user must pay money to see the page.",
        "correct": "B",
        "topic": "21: HTTP Status Code 404",
        "expl": "Status code 404 Not Found indicates that the client was able to communicate with the server, but the requested endpoint doesn't exist."
    },
    # 22
    {
        "text": "What is a 'Prompt Injection' attack against an AI application?",
        "a": "Injecting physical ink into the computer monitor screen.",
        "b": "Crafting malicious user input designed to trick the AI into ignoring its system safety instructions and revealing confidential data.",
        "c": "Upgrading the computer's cooling fan with liquid nitrogen.",
        "d": "Installing an antivirus update from an official website.",
        "e": "Typing on the keyboard using only one hand.",
        "correct": "B",
        "topic": "22: AI Prompt Injection",
        "expl": "Prompt injection exploits the language interface by inserting instructions that override the model's intended constraints."
    },
    # 23
    {
        "text": "What is the best practice for building a complex application with AI (Iterative Vibecoding)?",
        "a": "Prompting the AI to generate a 5,000-line full-stack app in a single prompt.",
        "b": "Building the application modularly step-by-step, verifying and testing each component before moving to the next.",
        "c": "Never running the code until the entire project is 100% finished.",
        "d": "Refusing to read any code generated by the AI assistant.",
        "e": "Asking the AI to guess what features you need without explaining them.",
        "correct": "B",
        "topic": "23: Iterative Vibecoding Workflow",
        "expl": "Modular, iterative development allows developers to test, verify, and refine code in manageable increments."
    },
    # 24
    {
        "text": "What does HTTPS with SSL/TLS encryption protect against when users visit a website?",
        "a": "It prevents attackers on public Wi-Fi from intercepting and reading transmitted passwords, cookies, and sensitive data.",
        "b": "It prevents the laptop battery from ever running out of power.",
        "c": "It stops all software bugs from appearing in your source code.",
        "d": "It permanently increases the resolution of your computer screen.",
        "e": "It automatically finishes your school homework for you.",
        "correct": "A",
        "topic": "24: HTTPS & Traffic Encryption",
        "expl": "HTTPS encrypts data in transit between the client and server, mitigating man-in-the-middle interception attacks."
    },
    # 25
    {
        "text": "In modern AI systems, what is 'Retrieval-Augmented Generation' (RAG) used for?",
        "a": "Generating random colors for website background styling.",
        "b": "Fetching relevant, verified information from an external knowledge base or documents and providing it to the AI before it answers.",
        "c": "Deleting old files from a hard drive to free up space.",
        "d": "Increasing the volume of laptop speakers during video playback.",
        "e": "Automatically turning off the computer after 10 minutes of inactivity.",
        "correct": "B",
        "topic": "25: Retrieval-Augmented Generation (RAG)",
        "expl": "RAG augments LLM prompts with retrieved factual documents, grounding responses in verified truth and reducing hallucinations."
    }
]

print("Grade 10-11 Vibecoding test data loaded (Both Bilingual UZ+RU and English). Instructor: Ismoiljon Usmonov.")
