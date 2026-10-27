#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
7–8-Sinf: 25 Savolli Amaliy Kiberxavfsizlik va Biometrika Testi
Uzbek va Russian variantlari (5 ta variant: A, B, C, D, E)
"""

META_7_8_UZ = {
    "school_name": "TARGET INTERNATIONAL SCHOOL — YUNUSOBOD",
    "exam_title": "7–8-SINF: AMALIY KIBERXAVFSIZLIK VA BIOMETRIKA",
    "track_title": "Game Dev & Cyber Security Track",
    "academic_year": "2026–2027 O'quv Yili",
    "label_name": "O'quvchi F.I.Sh.",
    "label_class": "Sinfi",
    "label_date": "Sana",
    "label_variant": "Variant",
    "variant_val": "1-Variant (Umumiy)",
    "label_max_score": "Maksimal ball",
    "unit_points": "ball",
    "label_score": "To'plangan ball",
    "instructions": "Ko'rsatma: Har bir savolga berilgan 5 ta variantdan (A, B, C, D, E) faqat bitta to'g'ri javobni tanlang va qalam bilan belgilang. Har bir to'g'ri javob uchun 1 ball beriladi."
}

KEYS_META_7_8_UZ = {
    "heading": "JAVOBLAR KALITI VA BAHOLASH MEZONI",
    "subheading": "O'qituvchi uchun rasmiy tekshirish kaliti (7–8-sinf, 25 ta savol)",
    "table_headers": ["№", "Kalit", "Mavzu / Kompetensiya", "Izoh va Tushuntirish"],
    "scale_heading": "Rasmiy 25 Ballik Baholash Shkalasi:",
    "rubric_tiers": [
        {"grade": "A'lo (5)", "range": "22 – 25 ball", "desc": "Amaliy kiberxavfsizlik va biometrika bo'yicha mustahkam bilim"},
        {"grade": "Yaxshi (4)", "range": "18 – 21 ball", "desc": "Tarmoq va tizim xavfsizligi yaxshi o'zlashtirilgan"},
        {"grade": "Qoniqarli (3)", "range": "13 – 17 ball", "desc": "Biometrika va himoya mexanizmlari takrorlanishi zarur"},
        {"grade": "Qoniqarsiz (2)", "range": "0 – 12 ball", "desc": "Mavzular qayta o'rganilishi lozim"}
    ]
}

META_7_8_RU = {
    "school_name": "TARGET INTERNATIONAL SCHOOL — ЮНУСАБАД",
    "exam_title": "7–8 КЛАСС: ПРИКЛАДНАЯ КИБЕРБЕЗОПАСНОСТЬ И БИОМЕТРИЯ",
    "track_title": "Game Dev & Cyber Security Track",
    "academic_year": "2026–2027 Учебный Год",
    "label_name": "Ф.И.О. Ученика",
    "label_class": "Класс",
    "label_date": "Дата",
    "label_variant": "Вариант",
    "variant_val": "Вариант 1 (Общий)",
    "label_max_score": "Макс. балл",
    "unit_points": "баллов",
    "label_score": "Итоговый балл",
    "instructions": "Инструкция: В каждом вопросе выберите только один правильный вариант ответа из пяти (A, B, C, D, E) и отметьте его. За каждый правильный ответ начисляется 1 балл."
}

KEYS_META_7_8_RU = {
    "heading": "КЛЮЧИ ОТВЕТОВ И КРИТЕРИИ ОЦЕНИВАНИЯ",
    "subheading": "Официальный ключ проверки для учителя (7–8 класс, 25 вопросов)",
    "table_headers": ["№", "Ключ", "Тема / Компетенция", "Пояснение и разбор ответа"],
    "scale_heading": "Официальная 25-балльная шкала оценивания:",
    "rubric_tiers": [
        {"grade": "Отлично (5)", "range": "22 – 25 баллов", "desc": "Глубокие знания прикладной безопасности и биометрии"},
        {"grade": "Хорошо (4)", "range": "18 – 21 балл", "desc": "Сетевая и системная безопасность хорошо освоены"},
        {"grade": "Удовл. (3)", "range": "13 – 17 баллов", "desc": "Требуется повторение биометрических алгоритмов"},
        {"grade": "Неудовл. (2)", "range": "0 – 12 баллов", "desc": "Необходимо повторить базовые темы курса"}
    ]
}

QUESTIONS_7_8_UZ = [
    {
        "text": "Ikki bosqichli autentifikatsiya (2FA) da ishlatiladigan TOTP (Time-based One-Time Password) kodi qanday ishlaydi?",
        "a": "Kodni bir marta yaratib, butun umr davomida barcha saytlarda ishlatiladi.",
        "b": "Maxfiy kalit va joriy vaqt asosida har 30 soniyada o'zgaruvchi bir martalik 6 xonali raqam ishlab chiqaradi.",
        "c": "Kod faqat internet o'chirilganda kompyuter xotirasida paydo bo'ladi.",
        "d": "U foydalanuvchining tug'ilgan yilini avtomatik chiqarib beradi.",
        "e": "Faqat Bluetooth ulanganda telefondan telefonga o'tadi.",
        "correct": "B",
        "topic": "2FA & TOTP Kodlari",
        "expl": "TOTP algoritmi vaqtga bog'liq bo'lib, har 30 soniyada yangi dinamik kod generatsiya qiladi."
    },
    {
        "text": "Xakerlar parollarni 'Brute-force' (kuch bilan saralash) usulida buzishiga qarshi serverlar qanday asosiy himoyani qo'llaydi?",
        "a": "Foydalanuvchi parolini butunlay bekor qilish.",
        "b": "Bir nechta (masalan 5 ta) noto'g'ri urinishdan keyin kirishni vaqtincha muzlatish (Rate Limiting / Lockout).",
        "c": "Monitor ekranini teskari aylantirish.",
        "d": "Kompyuter tezligini 10 barobarga kamaytirish.",
        "e": "Foydalanuvchiga har safar yangi kompyuter sotib olishni talab qilish.",
        "correct": "B",
        "topic": "Brute-force Himoyasi",
        "expl": "Rate Limiting parolni soniyasiga minglab marta terib ko'rish robotlarini to'xtatadi."
    },
    {
        "text": "Nima uchun ma'lumotlar bazasida parollarni oddiy ochiq matn (Plaintext) ko'rinishida saqlash mutlaqo taqiqlanadi?",
        "a": "Chunki ochiq matn diskda juda ko'p joy egallaydi.",
        "b": "Baza sizib chiqqan taqdirda xakerlar barcha foydalanuvchilarning asl parollarini bir zumda qo'lga kiritadi; shuning uchun parollar bir tomonlama xeshlanadi (Hashing).",
        "c": "Chunki ochiq matnli parollar kompyuterni qizdirib yuboradi.",
        "d": "Bazada faqat fotosuratlar saqlanishi kerak.",
        "e": "Bunday parollarni o'qish uchun maxsus ko'zoynak talab qilinadi.",
        "correct": "B",
        "topic": "Parol Xeshlash",
        "expl": "Xeshlash bir tomonlama matematik funksiya bo'lib, xeshdan asl parolni qaytarib bo'lmaydi."
    },
    {
        "text": "Fishing xatining eng shubhali texnik belgilaridan biri qaysi?",
        "a": "Xatda Target maktabining rasmiy logotipi bo'lishi.",
        "b": "Jo'natuvchi pochtasi va havola domeni rasmiy saytga o'xshatib soxtalashtirilganligi (masalan: payme-security.com o'rniga payme.uz).",
        "c": "Xatning dushanba kuni ertalab yuborilganligi.",
        "d": "Xat matnida tinish belgilarining to'g'ri qo'yilganligi.",
        "e": "Xatning hajmi 1 kilobaytdan kichik bo'lishi.",
        "correct": "B",
        "topic": "Fishing Tahlili",
        "expl": "Domen nomidagi kichik o'zgarishlar (typosquatting) fishingning asosiy indikatoridir."
    },
    {
        "text": "Ransomware (tovlamachi zararli dastur) kompyuterga tushganda nima sodir bo'ladi?",
        "a": "Faqat kompyuterdagi musiqalarni o'chirib yuboradi.",
        "b": "Foydalanuvchining barcha fayllarini kuchli algoritm bilan shifrlab qo'yadi va kalit uchun pul (kriptovalyuta) talab qiladi.",
        "c": "Kompyuterga yangi operatsion tizim o'rnatib beradi.",
        "d": "Klaviatura chiroqlarini o'chirib qo'yadi.",
        "e": "Faqat o'yinlardagi ballarni 0 ga tushiradi.",
        "correct": "B",
        "topic": "Ransomware Hujumlari",
        "expl": "Ransomware fayllarni shifrlaydi. Zaxira nusxa (backup) bo'lmasa, ma'lumotlarni qaytarish juda mushkul."
    },
    {
        "text": "Spyware (josus dasturlar) oilasiga kiruvchi 'Keylogger' dasturi qanday ishlaydi?",
        "a": "Klaviatura tugmalarini jismonan qotirib qo'yadi.",
        "b": "Foydalanuvchi klaviaturada bosgan har bir harf, raqam va parolni yashirincha faylga yozib, xakerga jo'natadi.",
        "c": "Kompyuter ekranidagi ranglarni o'zgartiradi.",
        "d": "Faqat matnli hujjatlarni qalin shriftga o'tkazadi.",
        "e": "Sichqonchaning o'ng tugmasini chapga almashtiradi.",
        "correct": "B",
        "topic": "Keylogger Josuslari",
        "expl": "Keylogger barcha terilgan parollar va xabarlarni yashirin qayd qiladi."
    },
    {
        "text": "IP manzil (masalan: 192.168.1.1) ning internet tarmog'idagi asosiy vazifasi nima?",
        "a": "Kompyuterning qaysi do'kondan sotib olinganini ko'rsatish.",
        "b": "Tarmoqdagi har bir qurilmani yagona raqamli manzil bilan aniqlash va paketlarni to'g'ri manzilga yetkazish.",
        "c": "Faqat kompyuter ekranining yorug'ligini sozlash.",
        "d": "Foydalanuvchining yoshini hisoblab borish.",
        "e": "Elektr toki kuchlanishini o'lchash.",
        "correct": "B",
        "topic": "IP Manzillar",
        "expl": "IP manzil — bu global tarmoqdagi qurilmaning unikal raqamli pochtasi hisoblanadi."
    },
    {
        "text": "DNS (Domain Name System) tizimi internetda qanday vazifani bajaradi?",
        "a": "Faqat kompyuter o'yinlarini yuklab beradi.",
        "b": "Inson tushunadigan domen nomlarini (google.com) kompyuterlar tushunadigan raqamli IP manzilga (142.250.180.14) o'giradi.",
        "c": "Foydalanuvchining parollarini barchaga ko'rsatadi.",
        "d": "Tarmoqdagi viruslarni sanab chiqadi.",
        "e": "Faqat saytlardagi rasmlarni qirqib beradi.",
        "correct": "B",
        "topic": "DNS Arxitekturasi",
        "expl": "DNS — bu internetning 'telefon kitobi' bo'lib, sayt nomlarini IP ga tarjima qiladi."
    },
    {
        "text": "Ommaviy ochiq Wi-Fi da 'Man-in-the-Middle' (O'rtadagi odam) kiber-hujumi qanday amalga oshiriladi?",
        "a": "Xaker foydalanuvchilar o'rtasida jismonan turib oladi.",
        "b": "Xaker kompyuter bilan Wi-Fi router o'rtasidagi tarmoq trafigini to'xtatib, o'tib ketayotgan shifrlanmagan ma'lumotlarni o'g'irlaydi.",
        "c": "Router kompyuterni zaryadlashdan to'xtatadi.",
        "d": "Wi-Fi simining uzilishi natijasida sodir bo'ladi.",
        "e": "Faqat kompyuter batareyasi tugaganda yuz beradi.",
        "correct": "B",
        "topic": "MITM Hujumlari",
        "expl": "MITM hujumida kiber-jinoyatchi kanalni egallab, uzatilayotgan parollar va cookie-fayllarni o'g'irlaydi."
    },
    {
        "text": "VPN (Virtual Private Network) xizmati internet foydalanuvchisini qanday himoya qiladi?",
        "a": "Kompyuterdagi barcha viruslarni 1 soniyada yo'q qiladi.",
        "b": "Qurilma bilan server o'rtasida shifrlangan maxfiy tunnel hosil qilib, real IP manzilni yashiradi.",
        "c": "Internet tezligini 100 barobarga oshiradi.",
        "d": "Telefon batareyasini abadiy qiladi.",
        "e": "Barcha pulli saytlarni tekin ochib beradi.",
        "correct": "B",
        "topic": "VPN Texnologiyasi",
        "expl": "VPN barcha chiquvchi va kiruvchi ma'lumotlar oqimini shifrlaydi."
    },
    {
        "text": "Kiberxavfsizlik nuqtai nazaridan Parol bilan Biometrika (yuz, barmoq izi) o'rtasidagi tub farq nima?",
        "a": "Parollar hech qachon esdan chiqmaydi, yuz esa har kuni o'zgaradi.",
        "b": "Parol o'g'irlansa uni 30 soniyada o'zgartirish mumkin, ammo biometrik izlar sizib chiqsa, inson yuzini yoki barmog'ini almashtirib bo'lmaydi.",
        "c": "Biometrika faqat planshetlarda ishlaydi.",
        "d": "Parollar faqat raqamlardan iborat bo'lishi shart.",
        "e": "Hech qanday farqi yo'q, ikkalasi bir xil narsa.",
        "correct": "B",
        "topic": "Biometrika Mas'uliyati",
        "expl": "Biometrik ma'lumotlar insonning biologik tanasiga tegishli bo'lib, ularni qayta tiklab yoki o'zgartirib bo'lmaydi."
    },
    {
        "text": "Face ID va kompyuter ko'rishi tizimlari yuzni aniqlashda nima uchun 68 ta tayanch nuqta (Landmarks) dan foydalanadi?",
        "a": "Chunki 68 soni omad keltiradi deb hisoblanadi.",
        "b": "Bu nuqtalar inson bosh suyagi geometriyasi (ko'zlar, qoshlar, burun va jag') ni qamrab olib, yuzni raqamli koordinatalar to'riga aylantiradi.",
        "c": "Faqat soch turmagining uzunligini o'lchash uchun.",
        "d": "Yuzdagi qon bosimini aniqlash uchun.",
        "e": "Monitor ekranidagi piksellar sonini sanash uchun.",
        "correct": "B",
        "topic": "68 Landmark Nuqtalari",
        "expl": "68 ta tayanch nuqta yuzning barcha asosiy anatomik qismlarini to'liq ifodalaydi."
    },
    {
        "text": "Biometriyada IPD (Inter-Pupillary Distance) ko'rsatkichi nimani anglatadi?",
        "a": "Quloqlar va burun orasidagi vertikal masofa.",
        "b": "Insonning chap va o'ng ko'z qorachiqlari markazlari orasidagi anatomik o'zgarmas masofa (odatda 60-65 mm).",
        "c": "Kompyuter ekranining diagonali.",
        "d": "Internet provayderining eng yaqin serverigacha bo'lgan masofa.",
        "e": "Ko'z qorachig'ining rangi indeksi.",
        "correct": "B",
        "topic": "IPD Masofasi",
        "expl": "IPD kattalarda deyarli o'zgarmas anatomik o'lchov bo'lib, yuz masshtabini aniqlashda muhimdir."
    },
    {
        "text": "Biometrik skanerlarga qarshi '2D Photo Spoofing' hujumi qanday amalga oshiriladi?",
        "a": "Xaker kompyuter kamerasini qora qalam bilan bo'yab qo'yadi.",
        "b": "Qurbonning yuqori sifatli fotosuratini qog'ozda yoki planshet ekranida kameraga tutib, tizimni aldashga urinadi.",
        "c": "Yuzga qora ko'zoynak taqib olish.",
        "d": "Kompyuterga ikkita kamera ulash.",
        "e": "Faqat qorong'i xonada Face ID ni ochish.",
        "correct": "B",
        "topic": "2D Spoofing",
        "expl": "2D Spoofing — tekis fotosurat yordamida Face ID ni aldashga qaratilgan eng sodda hujum."
    },
    {
        "text": "Liveness Detection (tiriklikni tekshirish) texnologiyasi 2D fotosurat bilan aldashni qanday fosh qiladi?",
        "a": "Kamerani 1 soniyaga o'chirib qo'yadi.",
        "b": "Insonning tabiiy biologik harakatlarini (ko'z miltillashi, bosh burilishi, yorug'likning 3D relyefda qaytishi) tekshiradi; qog'ozdagi rasm buni qila olmaydi.",
        "c": "Foydalanuvchidan pasportini ko'rsatishni talab qiladi.",
        "d": "Foydalanuvchiga ovoz chiqarib qo'shiq aytishni buyuradi.",
        "e": "Telefon korpusini qizdiradi.",
        "correct": "B",
        "topic": "Liveness Detection",
        "expl": "Liveness tirik insonning mikrodinamikasini tekshirib, statik tekis suratlarni darhol rad etadi."
    },
    {
        "text": "Eye Aspect Ratio (EAR) formulasi ko'z yumilganini (Blink) qanday matematik belgilaydi?",
        "a": "Ko'z yumilganda EAR qiymati cheksiz kattalashadi.",
        "b": "Ochiq ko'zda EAR ≈ 0.32 bo'ladi; qovoqlar yumilganda vertikal masofa nolga tushib, EAR ko'rsatkichi 0.18 dan pastga tushadi.",
        "c": "EAR faqat ko'z qorachig'ining rangini o'lchaydi.",
        "d": "EAR har doim 0 ga teng bo'ladi.",
        "e": "Ko'z yumilganda kamera avtomatik o'chadi.",
        "correct": "B",
        "topic": "EAR Formulasi",
        "expl": "EAR vertikal masofaning gorizontal kenglikka nisbati bo'lib, miltillashda 0.18 dan pastga sho'ng'iydi."
    },
    {
        "text": "Apple TrueDepth kamerasi nega hatto qop-qorong'i xonada ham Face ID ni aniq ishlatadi?",
        "a": "Telefon ekrani oq rangda miltillab yonadi.",
        "b": "Dot Projector orqali inson yuziga 30 000 ta ko'rinmas infraqizil nuqta sochiladi va infraqizil kamera 3D relyef xaritasini o'qiydi.",
        "c": "Telefonning orqa chirog'i (fonari) yonadi.",
        "d": "Mikrofon orqali inson nafasi o'lchanadi.",
        "e": "Faqat soat 12:00 da ishlaydi.",
        "correct": "B",
        "topic": "TrueDepth 3D Lazer",
        "expl": "TrueDepth xona yorug'ligiga tayanmaydi; u o'zining infraqizil lazer to'ri bilan 3D chuqurlikni o'qiydi."
    },
    {
        "text": "Veb-brauzerda veb-kamera (getUserMedia API) dan foydalanishda kiberxavfsizlik talabi qaysi?",
        "a": "Kamera faqat kompyuter o'chirilganda ishlaydi.",
        "b": "Sayt HTTPS xavfsiz protokoli orqali ochilgan bo'lishi va foydalanuvchi kameraga ruxsat (Permission) berishi shart.",
        "c": "Sayt faqat bitta rangda bo'lishi kerak.",
        "d": "Brauzerga hech qanday ruxsat kerak emas, istalgan sayt kamerani yashirincha yoqa oladi.",
        "e": "Kamera faqat Telegram orqali ishlaydi.",
        "correct": "B",
        "topic": "Brauzer Ruxsatlari",
        "expl": "Zamonaviy brauzerlar kiber-josuslikdan asrash uchun kamerani faqat HTTPS va foydalanuvchi ruxsati bilan ochadi."
    },
    {
        "text": "Veb-saytlarda Cookie fayliga 'HttpOnly' bayrog'i (flag) qo'yilsa, u nimadan himoya qiladi?",
        "a": "Saytning dizaynini chiroyliroq qiladi.",
        "b": "Brauzerdagi JavaScript (XSS skriptlari) ning sessiya kukilarini o'g'irlashiga yo'l qo'ymaydi.",
        "c": "Foydalanuvchining klaviaturasini tozalaydi.",
        "d": "Saytni barcha telefonlarda tekin ochadi.",
        "e": "Internet simining tezligini cheklaydi.",
        "correct": "B",
        "topic": "HttpOnly Bayrog'i",
        "expl": "HttpOnly kukilari document.cookie orqali o'qilmaydi, bu XSS orqali sessiya o'g'irlanishini bartaraf qiladi."
    },
    {
        "text": "Brauzerdagi 'Inkognito' (Private) rejimining kiberxavfsizlikdagi chegarasi nimada?",
        "a": "U kompyuterni har qanday viruslardan 100% himoya qiladi.",
        "b": "U faqat mahalliy qurilmada tarix va kukilarni saqlamaydi, ammo Internet provayderi va tarmoq adminlaridan faoliyatni yashirmaydi.",
        "c": "U kompyuterning IP manzilini butunlay yo'q qiladi.",
        "d": "U barcha pulli filmlarni tekin ko'rsatadi.",
        "e": "U orqali o'chirilgan fayllarni tiklab bo'lmaydi.",
        "correct": "B",
        "topic": "Inkognito Rejimi",
        "expl": "Inkognito faqat mahalliy brauzer tarixini yozmaydi; tashqi tarmoq provayderi qaysi saytlarga kirganingizni ko'radi."
    },
    {
        "text": "'Nolinchi kun zaifligi' (Zero-Day Vulnerability) nima?",
        "a": "Haftaning birinchi kuni sodir bo'ladigan oddiy xato.",
        "b": "Dasturchilar va ishlab chiqaruvchilar hali xabari bo'lmagan yoki tuzatishga ulgurmagan, xakerlar esa foydalanayotgan yangi xavfli kiber-teshik.",
        "c": "Yangi yil kuni barcha parollar yangilanishi.",
        "d": "Kompyuter kalendarining adashib qolishi.",
        "e": "Antivirusning muddati tugashi.",
        "correct": "B",
        "topic": "Zero-Day Zaifliklar",
        "expl": "Zero-day — hali rasmiy yamog'i (patch) chiqmagan eng xavfli va qimmatbaho zaifliklardir."
    },
    {
        "text": "Kiberxavfsizlikda zaxira nusxa olishning mashhur '3-2-1 qoidasi' nimani anglatadi?",
        "a": "Faylni 3 daqiqada ochish, 2 daqiqada o'qish, 1 daqiqada o'chirish.",
        "b": "Ma'lumotlarning 3 ta nusxasi, 2 xil saqlash vositasida (HDD/SSD), 1 tasi boshqa binoda yoki bulutda (Off-site) saqlanishi kerak.",
        "c": "Parolni 3 ta raqam, 2 ta harf, 1 ta belgidan tuzish.",
        "d": "Kompyuterni 3 kunda 1 marta o'chirib yoqish.",
        "e": "Faqat 3 kishiga parolni aytish mumkinligi.",
        "correct": "B",
        "topic": "3-2-1 Zaxiralash",
        "expl": "3-2-1 qoidasi yong'in, suv toshqini yoki ransomware hujumi bo'lganda ham ma'lumotlarni saqlab qoladi."
    },
    {
        "text": "Ijtimoiy muhandislikdagi 'Baiting' (Qopqon / Xo'rak) hujumi qanday usulni qo'llaydi?",
        "a": "Foydalanuvchiga to'g'ridan-to'g'ri qo'ng'iroq qilib baqirish.",
        "b": "Kompaniya yo'lagida qiziquvchanlikni uyg'otuvchi yozuvli (masalan: 'Oyliklar jadvali') virusli USB fleshkani ataylab tashlab ketish.",
        "c": "Foydalanuvchining monitorini o'g'irlab ketish.",
        "d": "Faqat printerga ko'p qog'oz tiqib qo'yish.",
        "e": "Internet simini kesib tashlash.",
        "correct": "B",
        "topic": "Baiting Xuruji",
        "expl": "Baiting insonning qiziquvchanligiga tayanadi: begona USB kompyuterga tiqilishi bilan zararli kod ishga tushadi."
    },
    {
        "text": "'Eng kam imtiyozlar printsipi' (Principle of Least Privilege) axborot xavfsizligida nimani talab qiladi?",
        "a": "Barcha xodimlarga serverning eng yuqori Admin (Root) huquqlarini berish.",
        "b": "Har bir foydalanuvchi va dasturga faqat o'z vazifasini bajarishi uchun zarur bo'lgan minimal darajadagi huquqlarnigina berish.",
        "c": "Faqat eng qimmat kompyuterlardan foydalanish.",
        "d": "Barcha parollarni bir xil qilish.",
        "e": "Hech kimga kompyuterni yoqishga ruxsat bermaslik.",
        "correct": "B",
        "topic": "Least Privilege",
        "expl": "Least Privilege bitta akkaunt buzilganda xaker butun tizimni nazorat qila olmasligini kafolatlaydi."
    },
    {
        "text": "'Oq xaker' (Ethical Hacker / White Hat) ning asosiy maqsadi nima?",
        "a": "Banklarni o'marish va pullarni o'z hisobiga o'tkazish.",
        "b": "Kompaniya ruxsati bilan tizimni qonuniy ravishda sinab, zaifliklarni jinoyatchilardan oldin topish va ularni tuzatishga yordam berish.",
        "c": "Internetda o'yin serverlarini ataylab buzish.",
        "d": "Foydalanuvchilarning fotosuratlarini internetga sizdirish.",
        "e": "Faqat qora kiyim kiyib kompyuterda o'tirish.",
        "correct": "B",
        "topic": "Etik Xakerlik",
        "expl": "Oq xakerlar tizimlarni himoya qilish va kiber-xavfsizlikni kuchaytirish uchun qonuniy ish olib boradilar."
    }
]

QUESTIONS_7_8_RU = [
    {
        "text": "Как работает алгоритм TOTP (Time-based One-Time Password), используемый в двухфакторной аутентификации (2FA)?",
        "a": "Код создается один раз и используется пожизненно на всех сайтах.",
        "b": "Генерирует уникальный 6-значный одноразовый код на основе секретного ключа и текущего времени, меняющийся каждые 30 секунд.",
        "c": "Код появляется в памяти компьютера только при отключении интернета.",
        "d": "Он автоматически вычисляет год рождения пользователя.",
        "e": "Передается с телефона на телефон только через Bluetooth.",
        "correct": "B",
        "topic": "2FA и TOTP",
        "expl": "Алгоритм TOTP математически синхронизирован со временем и генерирует код с окном жизни в 30 секунд."
    },
    {
        "text": "Какую ключевую защиту используют сервера против атак полного перебора паролей (Brute-Force)?",
        "a": "Полную отмену всех паролей в системе.",
        "b": "Временную блокировку учетной записи или ограничение частоты запросов (Rate Limiting) после нескольких неверных попыток.",
        "c": "Переворачивание изображения на мониторе пользователя.",
        "d": "Замедление работы процессора пользователя в 10 раз.",
        "e": "Требование покупать новый компьютер после каждой ошибки.",
        "correct": "B",
        "topic": "Защита от Brute-force",
        "expl": "Rate Limiting пресекает попытки автоматизированного перебора тысяч комбинаций в секунду."
    },
    {
        "text": "Почему строго запрещено хранить пароли пользователей в базе данных в открытом виде (Plaintext)?",
        "a": "Потому что открытый текст занимает слишком много места на диске.",
        "b": "При утечке базы злоумышленники мгновенно получат пароли всех пользователей; поэтому пароли хранят только в виде одностороннего хэша (Hashing).",
        "c": "Потому что открытый текст перегревает видеокарту.",
        "d": "Потому что в базах данных разрешено хранить только фотографии.",
        "e": "Для чтения таких паролей требуются специальные очки.",
        "correct": "B",
        "topic": "Хэширование Паролей",
        "expl": "Односторонние функции хэширования делают невозможным восстановление исходного пароля из хэша."
    },
    {
        "text": "Какой технический признак в письме чаще всего выдает фишинговую атаку?",
        "a": "Наличие официального логотипа школы Target в подписи.",
        "b": "Поддельный домен отправителя или ссылки, визуально похожий на оригинал (например: payme-security.com вместо payme.uz).",
        "c": "Письмо отправлено утром в понедельник.",
        "d": "Правильная расстановка знаков препинания в тексте.",
        "e": "Размер письма менее одного килобайта.",
        "correct": "B",
        "topic": "Анализ Фишинга",
        "expl": "Использование тайпсквоттинга и поддельных доменов — главный признак фишинговых писем."
    },
    {
        "text": "Что происходит при заражении компьютера вирусом-вымогателем (Ransomware)?",
        "a": "Программа лишь удаляет музыкальные треки с диска.",
        "b": "Она шифрует файлы пользователя надежным криптоалгоритмом и требует выкуп (в криптовалюте) за ключ расшифровки.",
        "c": "Она бесплатно устанавливает новую версию Windows.",
        "d": "Она выключает подсветку клавиатуры.",
        "e": "Она сбрасывает счет в компьютерных играх до нуля.",
        "correct": "B",
        "topic": "Вирусы-Вымогатели",
        "expl": "Ransomware блокирует доступ к важным данным путем шифрования с требованием выкупа."
    },
    {
        "text": "По какому принципу работает вредоносная программа класса Keylogger (клавиатурный шпион)?",
        "a": "Она физически блокирует нажатие кнопок на клавиатуре.",
        "b": "Она скрытно перехватывает каждое нажатие клавиши (пароли, сообщения, номера карт) и пересылает лог злоумышленнику.",
        "c": "Она меняет цветовую гамму монитора.",
        "d": "Она форматирует текст во всех документах жирным шрифтом.",
        "e": "Она меняет местами правую и левую кнопки мыши.",
        "correct": "B",
        "topic": "Клавиатурные Шпионы",
        "expl": "Кейлоггеры работают в фоновом режиме, сохраняя вводимые пользователем конфиденциальные данные."
    },
    {
        "text": "Какова основная функция IP-адреса (например: 192.168.1.1) в компьютерных сетях?",
        "a": "Показывать магазин, в котором был куплен ноутбук.",
        "b": "Однозначно идентифицировать устройство в сети для точной доставки пакетов данных.",
        "c": "Настраивать уровень яркости экрана монитора.",
        "d": "Вести учет возраста владельца компьютера.",
        "e": "Измерять напряжение в электрической розетке.",
        "correct": "B",
        "topic": "Функция IP-адреса",
        "expl": "IP-адрес служит уникальным сетевым адресом узла для маршрутизации сетевых пакетов."
    },
    {
        "text": "Какую задачу в глобальной сети выполняет служба DNS (Domain Name System)?",
        "a": "Скачивает компьютерные игры на максимальной скорости.",
        "b": "Преобразует понятные человеку доменные имена (google.com) в понятные машинам цифровые IP-адреса (142.250.180.14).",
        "c": "Публикует личные пароли пользователей в открытом доступе.",
        "d": "Подсчитывает вирусы на жестком диске.",
        "e": "Обрезает края у картинок на веб-сайтах.",
        "correct": "B",
        "topic": "Служба DNS",
        "expl": "DNS сопоставляет буквенные домены с числовыми IP-адресами серверов."
    },
    {
        "text": "В чем заключается суть атаки Man-in-the-Middle (Человек посередине) в открытых сетях Wi-Fi?",
        "a": "Злоумышленник физически садится между двумя пользователями за столом.",
        "b": "Хакер перехватывает трафик между компьютером жертвы и роутером, считывая незашифрованные пароли и сессии.",
        "c": "Роутер отключает зарядку ноутбука.",
        "d": "Она возникает только при физическом обрыве оптоволоконного кабеля.",
        "e": "Она случается при разрядке аккумулятора телефона.",
        "correct": "B",
        "topic": "Атака MITM",
        "expl": "В атаке MITM хакер внедряется в канал передачи данных и прослушивает весь незашифрованный трафик."
    },
    {
        "text": "Как сервис VPN (Virtual Private Network) обеспечивает защиту пользователя в интернете?",
        "a": "Удаляет все вирусы с жесткого диска за одну секунду.",
        "b": "Создает зашифрованный туннель между устройством и сервером, скрывая реальный IP-адрес и защищая трафик от прослушки.",
        "c": "Увеличивает скорость проводного интернета в 100 раз.",
        "d": "Делает заряд батареи телефона бесконечным.",
        "e": "Открывает доступ ко всем платным сайтам бесплатно.",
        "correct": "B",
        "topic": "Технология VPN",
        "expl": "VPN маскирует IP-адрес пользователя и криптографически шифрует сетевые пакеты."
    },
    {
        "text": "В чем принципиальная разница с точки зрения безопасности между Паролем и Биометрией (лицо, палец)?",
        "a": "Пароли никогда не забываются, а лицо меняется каждый день.",
        "b": "Утекший пароль можно легко сменить за 30 секунд, но если скомпрометирован биометрический слепок, сменить лицо или палец невозможно.",
        "c": "Биометрия поддерживается исключительно на планшетах.",
        "d": "Пароли обязаны состоять только из цифр.",
        "e": "Разницы нет, это абсолютно идентичные механизмы.",
        "correct": "B",
        "topic": "Особенности Биометрии",
        "expl": "Биометрические данные неотделимы от тела человека, поэтому их компрометация необратима."
    },
    {
        "text": "Зачем алгоритмы Face ID и компьютерного зрения измеряют 68 опорных точек (Landmarks) на лице?",
        "a": "Считается, что число 68 приносит удачу в программировании.",
        "b": "Эти точки привязаны к анатомической геометрии черепа (глаза, брови, нос, челюсть), формируя неизменяемый цифровой вектор лица.",
        "c": "Исключительно для измерения длины прически.",
        "d": "Для дистанционного измерения давления крови.",
        "e": "Для подсчета пикселей на экране монитора.",
        "correct": "B",
        "topic": "68 Точек Лица",
        "expl": "Сетка из 68 точек описывает ключевые костные ориентиры лица независимо от мимики."
    },
    {
        "text": "Что в биометрических системах обозначает параметр IPD (Inter-Pupillary Distance)?",
        "a": "Вертикальное расстояние от ушей до кончика носа.",
        "b": "Анатомическое расстояние между центрами зрачков левого и правого глаза (обычно 60–65 мм).",
        "c": "Длину диагонали экрана компьютера.",
        "d": "Расстояние до ближайшего сервера провайдера.",
        "e": "Индекс цветовой насыщенности радужки глаза.",
        "correct": "B",
        "topic": "Расстояние IPD",
        "expl": "IPD — индивидуальная константа взрослого человека, используемая для масштабирования лицевой сетки."
    },
    {
        "text": "Как проводится атака '2D Photo Spoofing' против биометрических камер?",
        "a": "Хакер закрашивает объектив камеры черным маркером.",
        "b": "Злоумышленник подносит к объективу качественную распечатанную фотографию или экран планшета с лицом владельца.",
        "c": "Пользователь надевает черные солнцезащитные очки.",
        "d": "К компьютеру подключают одновременно две веб-камеры.",
        "e": "Попытка разблокировать экран в полной темноте.",
        "correct": "B",
        "topic": "2D Спуфинг",
        "expl": "2D Photo Spoofing использует плоские изображения для обмана простых камер без датчиков глубины."
    },
    {
        "text": "Как алгоритмы Liveness Detection (проверка живости) распознают поддельное фото перед камерой?",
        "a": "Камера выключается на 1 секунду.",
        "b": "Система анализирует биологические микродвижения (моргание, поворот головы, микропульсацию и 3D-рельеф); плоское фото этого лишено.",
        "c": "Система требует приложить паспорт к экрану.",
        "d": "Система заставляет пользователя спеть песню вслух.",
        "e": "Телефон нагревает корпус.",
        "correct": "B",
        "topic": "Liveness Detection",
        "expl": "Liveness проверяет физиологическую динамику живого лица, отсекая статичные распечатки."
    },
    {
        "text": "Как формула Eye Aspect Ratio (EAR) математически определяет факт моргания глазом?",
        "a": "При закрытии глаза значение EAR стремится к бесконечности.",
        "b": "При открытом глазе EAR ≈ 0.32; при смыкании век вертикальное расстояние падает до нуля, и EAR резко снижается ниже 0.18.",
        "c": "EAR измеряет только температуру роговицы глаза.",
        "d": "EAR всегда строго равен нулю.",
        "e": "При моргании веб-камера аппаратно перезагружается.",
        "correct": "B",
        "topic": "Формула EAR",
        "expl": "EAR вычисляет отношение высоты глаза к его ширине, фиксируя резкий спад при моргании."
    },
    {
        "text": "Почему сенсор Apple TrueDepth способен распознавать лицо даже в абсолютной темноте?",
        "a": "Экран смартфона на долю секунды загорается белой вспышкой.",
        "b": "Проектор точек (Dot Projector) проецирует 30 000 невидимых инфракрасных точек, а ИК-камера считывает объемную 3D-карту лица.",
        "c": "Включается задний светодиодный фонарик телефона.",
        "d": "Микрофон анализирует звук дыхания человека.",
        "e": "Он работает только ровно в полдень.",
        "correct": "B",
        "topic": "Сенсор TrueDepth",
        "expl": "TrueDepth использует структурированный инфракрасный свет, работающий независимо от освещения комнаты."
    },
    {
        "text": "Какое главное требование кибербезопасности предъявляют браузеры к захвату камеры (getUserMedia)?",
        "a": "Камера может работать только при выключенном питании ПК.",
        "b": "Сайт обязан работать по защищенному протоколу HTTPS, а пользователь должен явно предоставить разрешение (Permission).",
        "c": "Цветовая гамма сайта должна быть однотонной.",
        "d": "Разрешение не требуется — любой сайт может скрытно вести съемку.",
        "e": "Камера доступна только через приложение Telegram.",
        "correct": "B",
        "topic": "Разрешения Браузера",
        "expl": "Защита от шпионажа запрещает доступ к камере без шифрования HTTPS и согласия пользователя."
    },
    {
        "text": "От какой угрозы защищает флаг безопасности 'HttpOnly', установленный на сессионную куку (Cookie)?",
        "a": "Улучшает визуальный дизайн веб-страницы.",
        "b": "Запрещает скриптам JavaScript (включая XSS) читать содержимое куки через document.cookie, предотвращая кражу сессии.",
        "c": "Очищает клавиатуру компьютера от пыли.",
        "d": "Открывает сайт бесплатно на всех телефонах.",
        "e": "Ограничивает скорость передачи данных.",
        "correct": "B",
        "topic": "Флаг HttpOnly",
        "expl": "HttpOnly изолирует куки от клиентского JavaScript, нивелируя кражу токенов через XSS."
    },
    {
        "text": "В чем заключается реальное ограничение режима 'Инкогнито' (Private Browsing) в браузере?",
        "a": "Он полностью защищает компьютер от любых вирусов и троянов.",
        "b": "Он лишь не сохраняет историю и куки на локальном устройстве, но интернет-провайдер и сетевые администраторы по-прежнему видят посещаемые сайты.",
        "c": "Он полностью уничтожает IP-адрес компьютера в сети.",
        "d": "Он делает платные фильмы бесплатными.",
        "e": "Он запрещает удаление файлов с диска.",
        "correct": "B",
        "topic": "Режим Инкогнито",
        "expl": "Инкогнито очищает локальные следы в браузере, но не шифрует сетевой трафик от провайдера."
    },
    {
        "text": "Что в кибербезопасности называют 'Уязвимостью нулевого дня' (Zero-Day Vulnerability)?",
        "a": "Обычную ошибку, возникающую в первый день недели.",
        "b": "Брешь в безопасности, о которой еще не знают разработчики ПО и для которой нет патча, но которую уже используют злоумышленники.",
        "c": "Ежегодный сброс всех паролей в новогоднюю ночь.",
        "d": "Сбой системного календаря на компьютере.",
        "e": "Окончание срока действия лицензии антивируса.",
        "correct": "B",
        "topic": "Уязвимости Zero-Day",
        "expl": "Zero-Day — это критическая брешь, для которой у разработчиков было 'ноль дней' на исправление."
    },
    {
        "text": "Что предписывает золотое правило резервного копирования '3-2-1'?",
        "a": "Открывать файл за 3 минуты, читать за 2 минуты, удалять за 1 минуту.",
        "b": "Иметь 3 копии данных на 2 разных типах носителей, при этом 1 копия должна храниться в другом месте (в облаке или на удаленном сервере).",
        "c": "Составлять пароль из 3 цифр, 2 букв и 1 спецсимвола.",
        "d": "Перезагружать компьютер раз в 3 дня.",
        "e": "Доверять пароль только 3 людям.",
        "correct": "B",
        "topic": "Правило 3-2-1",
        "expl": "Схема 3-2-1 защищает от потери информации при пожарах, поломках оборудования или атаках вымогателей."
    },
    {
        "text": "Какую тактику социальной инженерии использует атака 'Baiting' (Приманка)?",
        "a": "Прямые телефонные звонки с угрозами.",
        "b": "Подбрасывание зараженной вредоносным кодом флешки с интригующей надписью (например, 'Зарплаты 2026') на видном месте в офисе.",
        "c": "Физическую кражу монитора из кабинета.",
        "d": "Умышленное замятие бумаги в принтере.",
        "e": "Перерезание сетевого кабеля ножницами.",
        "correct": "B",
        "topic": "Атака Baiting",
        "expl": "Baiting использует любопытство сотрудников: подключение найденной флешки запускает вирус."
    },
    {
        "text": "Чего требует 'Принцип наименьших привилегий' (Principle of Least Privilege) в администрировании?",
        "a": "Предоставлять каждому сотруднику права полного администратора (Root) на сервере.",
        "b": "Выдавать пользователям и процессам только минимально необходимые права доступа, достаточные для выполнения их задач.",
        "c": "Использовать только самые дорогие компьютеры в офисе.",
        "d": "Устанавливать одинаковый пароль на все рабочие станции.",
        "e": "Запрещать включать компьютеры без разрешения директора.",
        "correct": "B",
        "topic": "Least Privilege",
        "expl": "Минимизация прав доступа ограничивает ущерб в случае взлома отдельной учетной записи."
    },
    {
        "text": "Какова основная цель 'Белого хакера' (Ethical Hacker / White Hat)?",
        "a": "Взламывать банки и выводить деньги на анонимные счета.",
        "b": "С разрешения владельца легально тестировать системы на прочность, находить уязвимости раньше злоумышленников и помогать их устранять.",
        "c": "Ломать игровые серверы ради развлечения.",
        "d": "Сливать фотографии пользователей в даркнет.",
        "e": "Носить черную одежду и капюшон во время работы за ПК.",
        "correct": "B",
        "topic": "Этичный Хакинг",
        "expl": "Белые хакеры проводят санкционированные тесты на проникновение для укрепления безопасности систем."
    }
]

print("Grade 7-8 test data loaded (25 questions UZ & RU).")
