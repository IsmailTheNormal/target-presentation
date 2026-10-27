#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Target International School — 5–6-Sinf Vibecoding Test Ma'lumotlari
Fan: Vibecoding (Junior Creators, Kiber-O'yinlar va Raqamli Madaniyat)
O'qituvchi: Ismoiljon Usmonov · Yunusobod filiali

Veb-saytdagi (index.html va classes/5-6-sinf/) barcha 24 ta dars materiallaridan tuzilgan:
1-hafta: AI nima, NPC aktyor, Game Lore, Concept art, Deepfake detektiv, Demo Day
2-hafta: 3D modellar, Level design va biomlar, SFX audio, Aqlli NPC dialog, HUD/HP, Game Jam
3-hafta: Game loop boshqaruvi, To'siqlar va HP, Oltin kristallar, Boss jangi va lazer qalqoni
4-hafta: Dushman AI patrul va ta'qib, O'z levelingni qur va level kodi
5-hafta: Parollar jangi, Fishing soxta havolalar, Troyanlar va soxta modlar
6-hafta: Cyber Shield detektor ilovasi va ijtimoiy muhandislik
7-hafta: Raqamli iz (Digital Footprint) va EXIF joylashuv maxfiyligi
8-hafta: Kiber-Qalqon oraliq nazorati: Katta Ekran qoidasi (Billboard Rule) va yakuniy xulosa
"""

META_5_6_UZ = {
    "school_name": "TARGET INTERNATIONAL SCHOOL — YUNUSOBOD",
    "exam_title": "5–6-SINF: VIBECODING, O'YIN YARATISH VA KIBER-MADANIYAT",
    "track_title": "Junior Creators & Cyber Gaming Track · O'qituvchi: Ismoiljon Usmonov",
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

KEYS_META_5_6_UZ = {
    "heading": "JAVOBLAR KALITI VA BAHOLASH MEZONI",
    "subheading": "O'qituvchi: Ismoiljon Usmonov · 5–6-sinf Vibecoding rasmiy tekshirish kaliti (25 ta savol)",
    "table_headers": ["№", "Kalit", "Mavzu / Dars", "Izoh va Tushuntirish"],
    "scale_heading": "Rasmiy 25 Ballik Baholash Shkalasi:",
    "rubric_tiers": [
        {"grade": "A'lo (5)", "range": "22 – 25 ball", "desc": "Game loop, dushman AI, level editor va kiber-qalqon bo'yicha mukammal bilim"},
        {"grade": "Yaxshi (4)", "range": "18 – 21 ball", "desc": "O'yin mexanikasi va raqamli xavfsizlik qoidalari yaxshi o'zlashtirilgan"},
        {"grade": "Qoniqarli (3)", "range": "13 – 17 ball", "desc": "Ayrim o'yin obyektlari va fishing tushunchalari takrorlanishi zarur"},
        {"grade": "Qoniqarsiz (2)", "range": "0 – 12 ball", "desc": "Vibecoding va kiber-o'yin asoslari qayta o'rganilishi lozim"}
    ]
}

META_5_6_RU = {
    "school_name": "TARGET INTERNATIONAL SCHOOL — ЮНУСАБАД",
    "exam_title": "5–6 КЛАСС: VIBECODING, СОЗДАНИЕ ИГР И КИБЕРКУЛЬТУРА",
    "track_title": "Junior Creators & Cyber Gaming Track · Учитель: Исмоилжон Усмонов",
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

KEYS_META_5_6_RU = {
    "heading": "КЛЮЧИ ОТВЕТОВ И КРИТЕРИИ ОЦЕНИВАНИЯ",
    "subheading": "Учитель: Исмоилжон Усмонов · Официальный ключ 5–6 класс (25 вопросов)",
    "table_headers": ["№", "Ключ", "Тема / Урок", "Пояснение и разбор ответа"],
    "scale_heading": "Официальная 25-балльная шкала оценивания:",
    "rubric_tiers": [
        {"grade": "Отлично (5)", "range": "22 – 25 баллов", "desc": "Отличные знания Game Loop, ИИ врагов, редактора уровней и киберщита"},
        {"grade": "Хорошо (4)", "range": "18 – 21 балл", "desc": "Игровая механика и цифровая безопасность хорошо освоены"},
        {"grade": "Удовл. (3)", "range": "13 – 17 баллов", "desc": "Требуется повторение отдельных игровых понятий и фишинга"},
        {"grade": "Неудовл. (2)", "range": "0 – 12 баллов", "desc": "Необходимо повторить основы Vibecoding и создания игр"}
    ]
}

QUESTIONS_5_6_UZ = [
    {
        "text": "1-dars materialiga ko'ra, Sun'iy intellekt (AI) qanday ishlaydi va uni qaysi jihatiga qarab kompyuterdan farqlaymiz?",
        "a": "U inson kabi mustaqil his-tuyg'ularga ega bo'lib, o'zi mustaqil xohish bildiradi.",
        "b": "U o'rgatilgan katta ma'lumotlar va naqshlar (pattern) asosida eng mos javobni hisoblab chiqaradi.",
        "c": "U faqat internetdagi Google qidiruv natijalarini to'g'ridan-to'g'ri ko'chirib beradi.",
        "d": "U kompyuterning qattiq diskidagi fayllarni o'chirish uchun yaratilgan virusdir.",
        "e": "U faqat matematika darsidagi oddiy kalkulyator funksiyasini bajaradi.",
        "correct": "B",
        "topic": "01-dars: AI nima va qanday ishlaydi",
        "expl": "AI inson kabi ongga ega emas, u o'rgatilgan katta ma'lumotlar bazasidagi naqshlar (patternlar) asosida eng ehtimolli natijani hisoblab beradi."
    },
    {
        "text": "2-darsda o'rganilgan 'AI Aktyor' mavzusiga ko'ra, o'yin qahramoniga (NPC) AI orqali jon kiritishda nima qilish kerak?",
        "a": "Promptda NPC ning xarakteri, fe'l-atvori, tarixi va o'yindagi maqsadini aniq belgilab berish kerak.",
        "b": "Faqatgina 'Menga o'yinchi yozib ber' deb bir so'zli prompt yozish kifoya.",
        "c": "Kompyuter ekranini o'chirib, qayta yoqish kerak.",
        "d": "NPC ga faqat inglizcha lug'atdagi so'zlarni yodlatish kerak.",
        "e": "AI aktyorlar o'yinlarda faqat dushman bo'la oladi, do'st bo'la olmaydi.",
        "correct": "A",
        "topic": "02-dars: AI Aktyor va NPC larni yaratish",
        "expl": "AI Aktyorga jon kiritish uchun promptda uning xarakteri (quvnoq, qo'rqoq, jangovar), uning maqsadi va qoidalari aniq belgilanadi."
    },
    {
        "text": "3-darsda 'Game Lore' (O'yin olami ssenariysi) yaratishda AI Ertakchidan qanday unumli foydalaniladi?",
        "a": "O'yin qoidalarini butunlay o'chirib tashlash uchun.",
        "b": "O'yin dunyosi qachon paydo bo'lgani, qanday qadimiy sir borligi va bosh qahramonning vazifasini to'qish uchun.",
        "c": "Faqat kompyuterning klaviaturasini sozlash uchun.",
        "d": "O'yin narxini do'konda qimmatroq sotish uchun.",
        "e": "O'yinchining internet tezligini 2 baravar oshirish uchun.",
        "correct": "B",
        "topic": "03-dars: Game Lore va Ertakchi AI",
        "expl": "Game Lore — bu o'yin olamining ssenariysi, afsonasi va tarixi bo'lib, AI orqali o'yin muhiti qiziqarli va sarguzashtli qilinadi."
    },
    {
        "text": "4-darsda o'yin vizual dizayni (Concept Art) uchun sun'iy intellektga prompt berilganda qaysi parametr muhim sanaladi?",
        "a": "Tasvir uslubi (masalan: Pixel Art, Cyberpunk, 3D Render) va yorug'lik ranglari.",
        "b": "Faqat kompyuter sichqonchasining modeli va narxi.",
        "c": "O'quvchining telefon raqami va uy manzili.",
        "d": "Faqatgina 'chiroyli rasm chiz' deb qisqa yozish.",
        "e": "Tasvir faqat qora-oq rangda bo'lishi majburiy shart.",
        "correct": "A",
        "topic": "04-dars: Game Concept Art va Vizual Promptlar",
        "expl": "Sifatli Concept Art olish uchun uslub (Pixel Art, Low-poly, Cyberpunk), ranglar gammasi va kamera burchagi ko'rsatilishi zarur."
    },
    {
        "text": "5-darsdagi 'Kiber-Detektiv' laboratoriyasida Deepfake (soxta rasm/video) larni fosh etuvchi asosiy belgi nima edi?",
        "a": "Suratning juda tiniq va sifatli ekanligi.",
        "b": "Qo'l barmoqlarining 6 ta bo'lib qolishi, ko'z qorachiqlaridagi g'alati akslar va quloq shaklining buzilishi.",
        "c": "Suratda qahramonning jilmayib turishi.",
        "d": "Surat fayli nomining '.png' bilan tugashi.",
        "e": "Surat hajmining 1 megabaytdan kattaligi.",
        "correct": "B",
        "topic": "05-dars: Deepfake va Kiber-Detektivlik",
        "expl": "AI generatsiya qilgan soxta suratlarda barmoqlar soni (masalan 6 ta barmoq), quloqlar nosimmetrikligi va ko'z aksi buzilishi kabi artefaktlar bo'ladi."
    },
    {
        "text": "6-darsdagi 'Demo Day' taqdimotida 1 daqiqalik 'Game Pitch' nima uchun kerak?",
        "a": "O'yin kodini boshidan oxirigacha o'qib berish uchun.",
        "b": "O'yinning asosiy g'oyasi, mexanikasi va nima uchun qiziq ekanini investorlar va sinfdoshlarga tez tushuntirish uchun.",
        "c": "Sinfda eng ko'p gapirgan o'quvchi bo'lish uchun.",
        "d": "Faqat o'yin musiqasini baland ovozda qo'yib berish uchun.",
        "e": "O'yindagi xatolarni yashirish va ko'rsatmaslik uchun.",
        "correct": "B",
        "topic": "06-dars: Game Pitch va Demo Day",
        "expl": "Game Pitch — bu loyihaning mohiyati, janri, bosh qahramoni va asosiy o'ziga xosligini (hook) 1 daqiqada taqdim etish san'ati."
    },
    {
        "text": "7-darsda o'rganilgan 3D modellarning asosi bo'lgan 'Mesh' (to'r) tushunchasi nimani anglatadi?",
        "a": "Faqat kompyuter ekranidagi fon rangini.",
        "b": "3D obyektning shaklini tashkil etuvchi cho'qqilar (vertices), qirralar va poligonlar to'plamini.",
        "c": "O'yinchining internet tarmog'iga ulanish kabelini.",
        "d": "O'yinda ishlatiladigan audio mikrofonni.",
        "e": "O'yindagi barcha yozuvlarning shriftini.",
        "correct": "B",
        "topic": "07-dars: 3D Modellar va Mesh Strukturasi",
        "expl": "3D model 'mesh' (panjara/to'r) deb ataluvchi yuzlab kichik poligonlar va cho'qqilardan iborat bo'lib, uning ustiga tekstura kiygiziladi."
    },
    {
        "text": "8-darsda 'Level Design' (Bosqich dizayni) yaratishda 2D Grid (panjara) nima uchun xaritaga chiziladi?",
        "a": "O'yin faqat qog'ozda o'ynalishi uchun.",
        "b": "Bloklar, platformalar, to'siqlar va qahramonning joylashuv koordinatalarini aniq hisoblash uchun.",
        "c": "Kompyuter ekranini chizib buzish uchun.",
        "d": "O'yin tezligini pasaytirish uchun.",
        "e": "Faqat o'yindagi matnlar sonini sanash uchun.",
        "correct": "B",
        "topic": "08-dars: Level Design va 2D Grid Arxitekturasi",
        "expl": "Grid (panjara) level dizaynerga qahramon sakray oladigan masofani va to'siqlarning qulay joylashuvini kataklar bo'yicha rejalashtirish imkonini beradi."
    },
    {
        "text": "9-darsda o'rganilgan SFX (Sound Effects) o'yinlarda qaysi vazifani bajaradi?",
        "a": "Faqat o'yin hajmini kompyuter diskida 10 baravar kattalashtirish.",
        "b": "Qahramon harakatlari (sakrash, tanga yig'ish, zarba yeyish) ga mos ovoz chiqarib, o'yinga jonli dinamika bag'ishlash.",
        "c": "O'yinchi monitorini yorqinroq ko'rsatish.",
        "d": "Klaviatura tugmalarini qotirib qo'yish.",
        "e": "Faqat o'yin tugagandagina bir marta chalinish.",
        "correct": "B",
        "topic": "09-dars: O'yin Ovozlar Sehri (SFX) va Musiqa",
        "expl": "SFX (Sound Effects) — har bir kichik amalda (kristall olish, sakrash, tikan urilishi) chalinib, o'yinchiga harakat hissini (feedback) beradi."
    },
    {
        "text": "10-darsdagi 'Aqlli NPC' larda 'Tarmoqlanuvchi Dialog' (Branching Dialogue) deganda nima tushuniladi?",
        "a": "NPC doimo faqat bitta gapni takrorlashi.",
        "b": "O'yinchi tanlagan javob variantiga qarab, suhbatning va o'yin vazifasining butunlay boshqa tomonga o'zgarishi.",
        "c": "O'yin dialoglarining faqat xorijiy tilda ko'rsatilishi.",
        "d": "Kompyuterning qotib qolishi.",
        "e": "NPC ning o'yinchidan qochib ketishi.",
        "correct": "B",
        "topic": "10-dars: Aqlli NPC va Tarmoqlanuvchi Dialoglar",
        "expl": "Tarmoqlanuvchi dialoglarda o'yinchi 'A' yoki 'B' javobni tanlaydi, shunga qarab NPC turli mukofot yoki yangi topshiriq (kvest) beradi."
    },
    {
        "text": "11-darsda o'rganilgan HUD (Heads-Up Display) o'yinda qayerda joylashadi va nimalarni ko'rsatadi?",
        "a": "O'yin kodi ichida yashiringan bo'ladi va o'yinchiga ko'rinmaydi.",
        "b": "Ekran chetida qahramonning joni (HP bar), to'plangan kristallari va o'yin vaqtini ko'rsatib turadi.",
        "c": "Faqatgina o'yin boshlanmasdan oldingi qora ekranda.",
        "d": "Faqat o'yindan chiqqandan so'ng kompyuter ish stolida.",
        "e": "O'yinchining internet provayderi reklamasini ko'rsatadi.",
        "correct": "B",
        "topic": "11-dars: O'yin Interfeysi: HUD va HP Barlari",
        "expl": "HUD (Heads-Up Display) — doimiy ravishda ekranda ko'rinib turuvchi o'yinchi hayotiy ko'rsatkichlari (HP, ball, vaqt) panelidir."
    },
    {
        "text": "12-darsdagi 'Game Jam' musobaqasining asosiy maqsadi nima?",
        "a": "Bir yil davomida bitta o'yin ustida shoshilmasdan ishlash.",
        "b": "Belgilangan cheklangan vaqt (masalan 1 dars yoki 48 soat) ichida berilgan mavzuga mos ishlovchi o'yin prototipini yaratish.",
        "c": "Faqat tayyor internetdagi o'yinlarni o'ynab o'tirish.",
        "d": "Boshqa o'quvchilarning kompyuterini buzish.",
        "e": "Eng chiroyli qog'oz chizgan o'quvchini g'olib qilish.",
        "correct": "B",
        "topic": "12-dars: Game Jam va Tezkor Prototip",
        "expl": "Game Jam — bu dasturchilar va dizaynerlar qisqa muddat ichida noldan ishlaydigan yangi o'yin prototipini yaratadigan ijodiy marafon."
    },
    {
        "text": "13-darsdagi 'Game Loop' (O'yin tsikli) dasturda nima uchun kerak?",
        "a": "O'yinni darhol to'xtatib qo'yish uchun.",
        "b": "Soniyasiga 60 marta o'yinchi harakatini o'qish, fizikani hisoblash va ekranni qayta chizish (render) uchun.",
        "c": "Faqat kompyuter sichqonchasini tozalash uchun.",
        "d": "O'yin fayllarini fleshkaga ko'chirib olish uchun.",
        "e": "O'yindagi tovushlarni butunlay o'chirish uchun.",
        "correct": "B",
        "topic": "13-dars: O'yin Mexanikasi va Game Loop",
        "expl": "Game Loop soniyasiga taxminan 60 marta (60 FPS) aylanadi: kiritilgan buyruqlarni tekshiradi, o'yinchi o'rnini yangilaydi va Canvas ga chizadi."
    },
    {
        "text": "14-darsda qahramon lazer yoki tikanga tekkanda (To'qnashuv / Collision) uning HP (Health Points) ko'rsatkichi nima bo'ladi?",
        "a": "Darhol 1000 ga ko'payadi.",
        "b": "Kamayadi (masalan, HP = HP - 1), agar HP 0 ga yetsa 'Game Over' (O'yin tugadi) holati yuz beradi.",
        "c": "O'yin ekrani o'chib, kompyuter o'chib qoladi.",
        "d": "Qahramon osmonga uchib, qaytib tushmaydi.",
        "e": "O'yin tezligi 10 barobar tezlashadi.",
        "correct": "B",
        "topic": "14-dars: To'siqlar, Lazerlar va HP Kamayishi",
        "expl": "To'qnashuv aniqlanganda o'yinchining HP si kamaytiriladi va qahramon qisqa vaqtga miltillab shikastlanganini bildiradi."
    },
    {
        "text": "15-darsda 'Kiber-Yuguruvchi 3.0' loyihasida oltin kristall to'planganda kodda qanday amal bajariladi?",
        "a": "Kristall soni kamayadi va o'yin to'xtaydi.",
        "b": "Ochko ko'payadi (score += 10), SFX jiringlaydi va olingan kristall massivdan o'chiriladi.",
        "c": "Faqat o'yinchi nomi o'zgaradi.",
        "d": "Kompyuter paroli o'zgaradi.",
        "e": "Kristall butun ekranni egallab oladi.",
        "correct": "B",
        "topic": "15-dars: Kristalllar, Ballar va To'planish Mexanikasi",
        "expl": "Kristall olinganda o'yinchining ochkosi oshadi, tanga ovozi chalinadi va olingan kristall xaritadan olib tashlanadi."
    },
    {
        "text": "16-darsdagi 'Boss Jangi' da o'yinchiga berilgan 'Lazer Qalqoni' mexanikasi qanday ishlaydi?",
        "a": "Qalqon faol bo'lgan soniyalarda dushman va boss lazerlari qahramonga zarar yetkaza olmaydi.",
        "b": "Qalqon o'yinchini dushman tomonga o'tkazib yuboradi.",
        "c": "Qalqon yoqilganda o'yinchi harakatlana olmay qoladi.",
        "d": "Qalqon faqat o'yin yutqazilganda ishlaydi.",
        "e": "Qalqon o'yinchining ballarini nollashtirib tashlaydi.",
        "correct": "A",
        "topic": "16-dars: Boss Jangi va Lazer Qalqoni",
        "expl": "Lazer qalqoni o'yinchiga ma'lum soniya davomida daxlsizlik (invulnerability) beradi va kuchli hujumlarni qaytaradi."
    },
    {
        "text": "4-hafta 15-darsda 'Dushman AI' o'yinchini qanday payqaydi va ta'qib qilishni boshlaydi?",
        "a": "Dushman butun xaritani ko'rmaydi, balki o'yinchi uning 'Ko'rish Radiusi' (Vision Radius) ga kirganida quvishni boshlaydi.",
        "b": "Dushman o'yinchiga qo'ng'iroq qilib xabar beradi.",
        "c": "Dushman har doim faqat bitta nuqtada qotib turadi.",
        "d": "Dushman o'yinchining kompyuter kamerasiga qarab biladi.",
        "e": "Dushman faqat o'yinchi yotganida harakatlanadi.",
        "correct": "A",
        "topic": "15-dars (4-h): Dushman AI va Ko'rish Radiusi",
        "expl": "Dushman AI oddiy paytda o'z hududida patrul qiladi. O'yinchi uning radiusiga (masalan 150 piksel) kirishi bilan 'Ta'qib' rejimiga o'tadi."
    },
    {
        "text": "4-hafta 16-darsdagi 'Level Redaktor' (O'z levelingni qur) vositasida yaratilgan xaritani do'stlarga qanday ulashish mumkin edi?",
        "a": "Butun kompyuterni do'stining uyiga ko'tarib borish orqali.",
        "b": "Xarita kataklarini qisqa 'Level Kodi' (matnli kod/JSON) ko'rinishida nusxalab yuborish orqali.",
        "c": "Ekranni rasmga olib chop etish orqali.",
        "d": "Do'stining akkauntini o'chirish orqali.",
        "e": "Xaritani hech kimga ko'rsatib bo'lmaydi.",
        "correct": "B",
        "topic": "16-dars (4-h): Level Redaktor va Level Kodi",
        "expl": "Level redaktorida yaratilgan bloklar koordinatalari bitta matnli kodga (Level Code) aylanadi va do'stlar uni o'z o'yiniga 'Import' qilishi mumkin."
    },
    {
        "text": "5-hafta 17-darsdagi 'Parollar Jangi' ga ko'ra, xakerlar parolni 'Brute-Force' (to'liq saralash) bilan topa olmasligi uchun parol qanday bo'lishi kerak?",
        "a": "12345678 yoki admin123 kabi hamma biladigan so'zlar.",
        "b": "Kamida 12-14 ta belgi, katta-kichik harflar, raqamlar va maxsus belgilar (#$!%) aralashmasi.",
        "c": "Faqat o'quvchining o'z ismi va tug'ilgan yili.",
        "d": "Faqat 4 ta raqamdan iborat bank kartasi kodi.",
        "e": "Barcha ijtimoiy tarmoqlarda bir xil bitta oddiy parol.",
        "correct": "B",
        "topic": "17-dars (5-h): Parollar Jangi va Brute-Force Himoyasi",
        "expl": "12-14 belgidan iborat murakkab parollarni superkompyuterlar ham yuzlab yillar davomida topa olmaydi."
    },
    {
        "text": "5-hafta 18-darsda o'rganilgan 'Fishing' (Phishing) kiber-hujumining asosiy maqsadi nima?",
        "a": "Kompyuterga dars jadvalini o'rnatish.",
        "b": "Soxta havolalar va soxta login oynalari orqali foydalanuvchining shaxsiy paroli va akkauntini o'g'irlash.",
        "c": "O'yinchiga haqiqiy bepul olmoslar sovg'a qilish.",
        "d": "Kompyuter klaviaturasini tozalash.",
        "e": "Internet provayderining tezligini o'lchash.",
        "correct": "B",
        "topic": "18-dars (5-h): Fishing va Soxta Havolalar",
        "expl": "Fishing — firibgarlar haqiqiy saytga o'xshash soxta sahifa (masalan r0bl0x-free.com) yasab, parollarni o'g'irlash usuli."
    },
    {
        "text": "5-hafta 19-darsdagi 'Troyalik Ot' (Trojan) virusi qanday qilib bolalarning kompyuteriga tushib qoladi?",
        "a": "Faqat kompyuter quvvati tugaganda.",
        "b": "'Tekin o'yin', 'O'yin uchun cheat/mod' yoki 'Tekin valyuta' niqobi ostidagi shubhali fayllarni yuklab olish orqali.",
        "c": "Faqat rasmiy maktab saytiga kirganda.",
        "d": "Kompyuterga yangi qonuniy sichqoncha ulanganda.",
        "e": "Kitob o'qiyotganda.",
        "correct": "B",
        "topic": "19-dars (5-h): Zararli Dasturlar va Troyanlar",
        "expl": "Troyan virusi o'zini qiziqarli o'yin yoki tekin o'yin boyligi deb tanishtirib, orqa fonda josus dasturlarni ishga tushiradi."
    },
    {
        "text": "6-hafta 20-darsda o'quvchilar tomonidan yaratilgan 'Cyber Shield' veb-ilovasi nima ish qilar edi?",
        "a": "O'quvchilar nomidan o'qituvchiga dars javoblarini yuborar edi.",
        "b": "Chatdagi shubhali xabarlarni tahlil qilib, 'tekin robux', soxta admin va fishing belgilarini qizil rang bilan fosh etar edi.",
        "c": "Faqat musiqa chaluvchi oddiy pleyer edi.",
        "d": "Kompyuterdagi barcha fotosuratlarni internetga yuklar edi.",
        "e": "Faqat ob-havo ma'lumotini ko'rsatar edi.",
        "correct": "B",
        "topic": "20-dars (6-h): Cyber Shield Detektor Loyihasi",
        "expl": "Cyber Shield ilovasi shubhali chat matnlarini skanerlab, firibgarlarning tipik tuzoqlarini o'quvchiga darhol ko'rsatib beradi."
    },
    {
        "text": "7-hafta 21-darsdagi 'Raqamli Iz' (Digital Footprint) va fotosuratlardagi EXIF ma'lumotlari nimani oshkor qilib qo'yishi mumkin?",
        "a": "Faqat telefon batareyasi qoldig'ini.",
        "b": "Rasm olingan aniq GPS joylashuv (uy manzili), kamera modeli va olingan sanani.",
        "c": "Faqat kompyuterning operatsion tizimi nomini.",
        "d": "Foydalanuvchining kelajakdagi orzularini.",
        "e": "Hech qanday ma'lumotni oshkor qilmaydi.",
        "correct": "B",
        "topic": "21-dars (7-h): Raqamli Iz va EXIF Maxfiyligi",
        "expl": "Surat fayllari ichida (EXIF) ko'pincha GPS koordinatalari yashiringan bo'ladi, begonalarga yuborishdan oldin bu ma'lumotlarni tozalash shart."
    },
    {
        "text": "8-hafta 22-darsda 'Kiber-Qalqon Oraliq Nazorati' da ta'kidlangan 'Katta Ekran Qoidasi' (Billboard Rule) nimani anglatadi?",
        "a": "Har bir kishi uyiga katta televizor sotib olishi shart.",
        "b": "Agar biror rasm, video yoki yozuvni shahar markazidagi katta reklama ekraniga osishga uyalsangiz, uni internetga ham aslo joylamang!",
        "c": "Kompyuter ekranini doimo pardalar bilan yopib yurish kerak.",
        "d": "Faqat katta ekranli telefonlardan foydalanish qoidasi.",
        "e": "O'yinlarni faqat kinoteatrlarda o'ynash lozim.",
        "correct": "B",
        "topic": "22-dars (8-h): Katta Ekran Qoidasi (Billboard Rule)",
        "expl": "Billboard Rule: Internet ommaviy joy. Minglab begona odamlar ko'rishiga rozi bo'lmagan shaxsiy ma'lumotlarni tarmoqqa yuklash mumkin emas."
    },
    {
        "text": "5–6-sinf Vibecoding kursining 1-chorak yakuniy xulosasiga ko'ra, haqiqiy kiber-dasturchining eng muhim qoidasi nima?",
        "a": "Faqat boshqalarning tayyor o'yinlarini ko'chirib, o'ziniki deb ko'rsatish.",
        "b": "AI vositalaridan aqlli foydalanib o'yinlar yaratish, biroq shaxsiy parollar va kiber-xavfsizlik qoidalariga qat'iy amal qilish.",
        "c": "Hech qachon yangi texnologiyalarni o'rganmaslik.",
        "d": "Kun bo'yi tanaffussiz faqat o'yin o'ynash.",
        "e": "Internetdagi har qanday notanish havolani tekshirmasdan bosish.",
        "correct": "B",
        "topic": "Yakuniy Xulosa: Vibecoding Kiber-Dasturchi Standarti",
        "expl": "Vibecoder — bu sun'iy intellekt orqali ajoyib raqamli dunyolar yaratuvchi, o'zini va yaqinlarini kiber-xavflardan himoya qila oladigan zamonaviy ijodkordir."
    }
]

QUESTIONS_5_6_RU = [
    {
        "text": "Согласно материалам Урока 1, как работает Искусственный Интеллект (ИИ) и чем он отличается от человека?",
        "a": "Он обладает чувствами и собственными желаниями, как человек.",
        "b": "Он вычисляет наиболее вероятный ответ на основе обученных больших данных и закономерностей (паттернов).",
        "c": "Он просто напрямую копирует результаты поисковой выдачи Google.",
        "d": "Это вирус, созданный исключительно для удаления файлов с жесткого диска.",
        "e": "Он выполняет только функции простейшего калькулятора.",
        "correct": "B",
        "topic": "Урок 01: Что такое ИИ и как он работает",
        "expl": "ИИ не обладает сознанием, он находит закономерности в колоссальных массивах данных и вычисляет математически подходящий ответ."
    },
    {
        "text": "На Уроке 2 'ИИ Актёр': что необходимо сделать, чтобы оживить игрового персонажа (NPC) с помощью ИИ?",
        "a": "В промпте четко задать характер NPC, его манеру речи, предысторию и цель в игре.",
        "b": "Написать промпт из одного слова: 'Сделай мне персонажа'.",
        "c": "Выключить и снова включить монитор компьютера.",
        "d": "Заставить NPC выучить все слова из словаря наизусть.",
        "e": "ИИ актёры в играх могут быть только врагами и никогда союзниками.",
        "correct": "A",
        "topic": "Урок 02: ИИ Актёр и создание живых NPC",
        "expl": "Чтобы оживить NPC, в системном промпте подробно прописывают его характер, интонацию, предысторию и игровые цели."
    },
    {
        "text": "На Уроке 3 при создании 'Game Lore' (Лор игры), как эффективно использовать ИИ Сказочника?",
        "a": "Чтобы удалить все игровые механики и код игры.",
        "b": "Чтобы придумать историю создания игрового мира, древние тайны и великую миссию главного героя.",
        "c": "Исключительно для настройки чувствительности клавиатуры.",
        "d": "Чтобы завысить цену игры в цифровом магазине.",
        "e": "Чтобы увеличить скорость интернета в два раза.",
        "correct": "B",
        "topic": "Урок 03: Game Lore и ИИ Сказочник",
        "expl": "Game Lore — это сюжетная вселенная игры, мифология и предыстория, которую ИИ помогает сделать захватывающей."
    },
    {
        "text": "На Уроке 4 при генерации концепт-арта (Concept Art) для игры, какой параметр промпта является ключевым?",
        "a": "Художественный стиль (например: Pixel Art, Cyberpunk, 3D Render) и световая палитра.",
        "b": "Только модель и цена компьютерной мыши.",
        "c": "Номер телефона и домашний адрес ученика.",
        "d": "Короткая фраза 'нарисуй красиво'.",
        "e": "Обязательное требование делать изображение только черно-белым.",
        "correct": "A",
        "topic": "Урок 04: Концепт-арт и визуальные промпты",
        "expl": "Для качественного концепт-арта задаются художественный стиль (Pixel Art, Low-poly), ракурс камеры и цветовое освещение."
    },
    {
        "text": "В лаборатории Урока 5 'Кибер-Детектив', какой главный признак позволял разоблачить дипфейк (Deepfake)?",
        "a": "Слишком высокое разрешение и четкость изображения.",
        "b": "Лишние пальцы (шесть пальцев на руке), неестественные блики в зрачках и деформированные уши.",
        "c": "То, что человек на фото улыбается.",
        "d": "То, что файл фотографии имеет расширение .png.",
        "e": "Размер файла превышает 1 мегабайт.",
        "correct": "B",
        "topic": "Урок 05: Deepfake и Кибер-Детектив",
        "expl": "Генеративные нейросети часто ошибаются в анатомии: добавляют лишние пальцы, размывают зрачки и нарушают симметрию ушей."
    },
    {
        "text": "На Уроке 6 на выставке 'Demo Day', для чего предназначен минутный 'Game Pitch'?",
        "a": "Чтобы вслух прочитать весь исходный код игры от начала до конца.",
        "b": "Чтобы за 1 минуту ярко презентовать ключевую идею игры, механику и привлечь интерес аудитории.",
        "c": "Чтобы просто оказаться самым громким учеником в классе.",
        "d": "Чтобы включить музыку на максимальную громкость.",
        "e": "Чтобы скрыть все ошибки и не показывать игру никому.",
        "correct": "B",
        "topic": "Урок 06: Game Pitch и Demo Day",
        "expl": "Game Pitch — это искусство за 60 секунд объяснить концепцию, жанр и изюминку (hook) проекта потенциальным игрокам."
    },
    {
        "text": "На Уроке 7, что означает понятие 'Mesh' (полигональная сетка) в мире 3D моделей?",
        "a": "Цвет фона на экране монитора.",
        "b": "Геометрическую форму объекта, состоящую из вершин (vertices), ребер и многоугольников (полигонов).",
        "c": "Кабель подключения компьютера к локальной сети.",
        "d": "Микрофон, используемый в игре.",
        "e": "Шрифт текста в главном меню игры.",
        "correct": "B",
        "topic": "Урок 07: 3D Модели и структура Mesh",
        "expl": "Mesh (3D полигональная сетка) формирует каркас трехмерного объекта из вершин и полигонов, на который накладываются текстуры."
    },
    {
        "text": "На Уроке 8 при проектировании уровня (Level Design), для чего на карту накладывается сетка 2D Grid?",
        "a": "Чтобы игра запускалась исключительно на бумаге.",
        "b": "Чтобы точно рассчитать координаты размещения блоков, платформ, препятствий и стартовой точки героя.",
        "c": "Чтобы расцарапать экран монитора.",
        "d": "Чтобы искусственно замедлить скорость игры.",
        "e": "Исключительно для подсчета количества букв в тексте.",
        "correct": "B",
        "topic": "Урок 08: Дизайн уровней и сетка 2D Grid",
        "expl": "2D Grid (сетка) позволяет левел-дизайнеру выстраивать проходимые прыжки и гармонично распределять ловушки по клеткам."
    },
    {
        "text": "На Уроке 9, какую ключевую роль в играх играют звуковые эффекты SFX (Sound Effects)?",
        "a": "Исключительно увеличивают размер файла игры в 10 раз.",
        "b": "Озвучивают каждое действие героя (прыжок, сбор монет, удар) и дают игроку мгновенную живую обратную связь.",
        "c": "Делают изображение на экране ярче.",
        "d": "Блокируют клавиши клавиатуры.",
        "e": "Звучат только один раз в самом конце игры.",
        "correct": "B",
        "topic": "Урок 09: Магия игрового звука (SFX) и музыка",
        "expl": "SFX (звуковые эффекты) моментально реагируют на физические действия в игре, создавая эффект погружения и сопричастности."
    },
    {
        "text": "На Уроке 10, что понимается под 'Ветвящимися диалогами' (Branching Dialogues) у умных NPC?",
        "a": "Ситуация, когда NPC монотонно повторяет одну и ту же фразу.",
        "b": "Система, где в зависимости от выбранного игроком ответа сюжет и награды развиваются по разным веткам.",
        "c": "Показ диалогов исключительно на иностранном языке.",
        "d": "Зависание игры.",
        "e": "Бегство персонажа от игрока.",
        "correct": "B",
        "topic": "Урок 10: Умные NPC и ветвящиеся диалоги",
        "expl": "Ветвящийся диалог строится как дерево решений: выбор ответа игрока определяет отношение NPC и дальнейшие квесты."
    },
    {
        "text": "На Уроке 11, где располагается интерфейс HUD (Heads-Up Display) и что он отображает?",
        "a": "Он спрятан внутри кода и никогда не виден игроку.",
        "b": "По краям экрана он показывает шкалу жизней (HP bar), счет собранных кристаллов и таймер игры.",
        "c": "Только на черном экране перед запуском игры.",
        "d": "Только на рабочем столе после закрытия игры.",
        "e": "Показывает рекламу интернет-провайдера.",
        "correct": "B",
        "topic": "Урок 11: Игровой интерфейс HUD и полосы жизней",
        "expl": "HUD (Heads-Up Display) — панель поверх игрового поля, отображающая ключевые параметры персонажа в реальном времени."
    },
    {
        "text": "На Уроке 12, в чем заключается главная цель хакатона 'Game Jam'?",
        "a": "Работать над одной игрой целый год без спешки.",
        "b": "За ограниченное короткое время (например 1 урок или 48 часов) создать рабочий прототип игры на заданную тему.",
        "c": "Просто играть в готовые игры из интернета.",
        "d": "Сломать чужие компьютеры в классе.",
        "e": "Наградить того, кто лучше всех нарисовал рисунок на бумаге.",
        "correct": "B",
        "topic": "Урок 12: Game Jam и быстрый прототип",
        "expl": "Game Jam — это творческий марафон разработчиков, где за ограниченное время создается рабочий прототип игры."
    },
    {
        "text": "На Уроке 13, для чего в коде игры необходим бесконечный цикл 'Game Loop'?",
        "a": "Чтобы моментально остановить игру при запуске.",
        "b": "Чтобы непрерывно (около 60 раз в секунду) опрашивать кнопки, пересчитывать физику и перерисовывать экран.",
        "c": "Исключительно для очистки мышки от пыли.",
        "d": "Чтобы скопировать файлы игры на флешку.",
        "e": "Чтобы полностью отключить звук в игре.",
        "correct": "B",
        "topic": "Урок 13: Игровая механика и Game Loop",
        "expl": "Game Loop работает со скоростью 60 FPS: считывает управление (input), обновляет состояние мира (update) и рисует кадр (render)."
    },
    {
        "text": "На Уроке 14, что происходит со шкалой HP героя при столкновении (Collision) с лазером или шипами?",
        "a": "Значение сразу возрастает до 1000.",
        "b": "Количество жизней уменьшается (HP = HP - 1), а при достижении 0 наступает экран 'Game Over'.",
        "c": "Монитор выключается и компьютер выключается из розетки.",
        "d": "Герой улетает в космос и не возвращается.",
        "e": "Скорость игры увеличивается в 10 раз.",
        "correct": "B",
        "topic": "Урок 14: Препятствия, шипы и потеря жизней",
        "expl": "При детекции столкновения с ловушкой отнимается жизнь (HP), включается мигание неуязвимости и звук получения урона."
    },
    {
        "text": "На Уроке 15 в проекте 'Кибер-Бегун 3.0', что происходит в коде при сборе золотого кристалла?",
        "a": "Количество кристаллов уменьшается и игра зависает.",
        "b": "Счет очков увеличивается (score += 10), звучит SFX и взятый кристалл удаляется из массива объектов.",
        "c": "Меняется только имя игрока.",
        "d": "Меняется системный пароль от компьютера.",
        "e": "Кристалл закрывает собой весь экран.",
        "correct": "B",
        "topic": "Урок 15: Кристаллы, очки и механика сбора",
        "expl": "При подборе предмета счет игрока растет, звучит аудиоэффект, а сам кристалл убирается с карты, чтобы его нельзя было взять дважды."
    },
    {
        "text": "На Уроке 16 в битве с Боссом, как работает механика 'Лазерного Щита', предоставленная игроку?",
        "a": "В секунды активности щита лазеры босса и снаряды врагов не наносят герою никакого урона.",
        "b": "Щит телепортирует героя в команду босса.",
        "c": "При включении щита игрок теряет способность двигаться.",
        "d": "Щит срабатывает только после полного проигрыша.",
        "e": "Щит сбрасывает все набранные очки до нуля.",
        "correct": "A",
        "topic": "Урок 16: Битва с Боссом и Лазерный Щит",
        "expl": "Лазерный щит дает игроку временную неуязвимость (invulnerability), позволяя пережить плотные залпы босса."
    },
    {
        "text": "На Уроке 15 (4-я неделя), как ИИ врагов обнаруживает присутствие игрока и начинает погоню?",
        "a": "Враг видит не всю карту, а реагирует только тогда, когда игрок заходит в его радиус видимости (Vision Radius).",
        "b": "Враг звонит игроку на сотовый телефон.",
        "c": "Враг всегда неподвижно стоит на одном месте.",
        "d": "Враг подглядывает через веб-камеру ноутбука.",
        "e": "Враг двигается только тогда, когда игрок заснул.",
        "correct": "A",
        "topic": "Урок 15 (4-нед): ИИ Врага и радиус видимости",
        "expl": "В режиме патрулирования враг ходит взад-вперед. Как только расстояние до игрока становится меньше радиуса видимости, включается погоня."
    },
    {
        "text": "На Уроке 16 (4-я неделя) в 'Редакторе Уровней', как созданную карту можно переслать одноклассникам?",
        "a": "Принести весь системный блок домой к другу.",
        "b": "Скопировать компактный текстовый 'Код Уровня' (Level Code / JSON) и отправить его в сообщении.",
        "c": "Сфотографировать экран и распечатать на принтере.",
        "d": "Удалить учетную запись друга.",
        "e": "Созданную карту в редакторе никому передать невозможно.",
        "correct": "B",
        "topic": "Урок 16 (4-нед): Редактор Уровней и код уровня",
        "expl": "Координаты всех блоков сериализуются в одну текстовую строку (Level Code), которую другой игрок может загрузить кнопкой 'Import'."
    },
    {
        "text": "На 5-й неделе (Урок 17 'Битва Паролей'), какой пароль невозможно взломать атакой Brute-Force (полным перебором)?",
        "a": "12345678 или admin123, которые все знают.",
        "b": "Длинный пароль из 12-14 символов с буквами разного регистра, цифрами и спецсимволами (#$!%).",
        "c": "Свое имя и год рождения слитно.",
        "d": "Короткий четырехзначный пин-код.",
        "e": "Один и тот же простой пароль на всех сайтах подряд.",
        "correct": "B",
        "topic": "Урок 17 (5-нед): Битва Паролей и защита от Brute-Force",
        "expl": "Пароли длиной от 12-14 символов со спецсимволами обладают гигантской энтропией, их перебор суперкомпьютером займет столетия."
    },
    {
        "text": "На 5-й неделе (Урок 18), в чем заключается главная опасность фишинговой атаки (Phishing)?",
        "a": "Она устанавливает на компьютер электронное школьное расписание.",
        "b": "Через фальшивые ссылки-двойники и окна входа злоумышленники крадут пароли и учетные записи.",
        "c": "Она бесплатно дарит настоящие игровые робуксы и алмазы.",
        "d": "Она стирает пыль с клавиатуры.",
        "e": "Она измеряет скорость интернет-соединения.",
        "correct": "B",
        "topic": "Урок 18 (5-нед): Фишинг и поддельные ссылки",
        "expl": "Фишинг заманивает пользователя на сайт-ловушку (например r0bl0x-free.com), где введенные логин и пароль сразу уходят мошенникам."
    },
    {
        "text": "На 5-й неделе (Урок 19), как троянские программы ('Троянский Конь') чаще всего попадают на компьютеры школьников?",
        "a": "Только когда в ноутбуке разряжается аккумулятор.",
        "b": "Под видом 'бесплатных читов', 'модов для любимой игры' или 'бесплатной игровой валюты' с сомнительных сайтов.",
        "c": "Только при переходе на официальный сайт школы.",
        "d": "При подключении новой лицензионной мыши.",
        "e": "При чтении книги онлайн.",
        "correct": "B",
        "topic": "Урок 19 (5-нед): Вредоносные программы и трояны",
        "expl": "Троян маскируется под полезный файл (чит, взломанный мод), но после запуска незаметно открывает хакерам доступ к системе."
    },
    {
        "text": "На 6-й неделе (Урок 20), какую задачу решало созданное веб-приложение 'Cyber Shield'?",
        "a": "Оно отправляло домашние задания учителю за учеников.",
        "b": "Оно сканировало подозрительные сообщения чата и подсвечивало красным фразы про 'бесплатные робуксы' и фальшивых админов.",
        "c": "Это был обычный музыкальный проигрыватель.",
        "d": "Оно выгружало все фотографии учеников в открытый интернет.",
        "e": "Оно показывало только прогноз погоды.",
        "correct": "B",
        "topic": "Урок 20 (6-нед): Проект детектор Cyber Shield",
        "expl": "Приложение Cyber Shield анализирует текст на маркеры социальной инженерии и учит школьников моментально распознавать ловушки."
    },
    {
        "text": "На 7-й неделе (Урок 21), какую скрытую информацию о вас могут раскрыть фотографии через метаданные EXIF?",
        "a": "Только уровень оставшегося заряда батареи телефона.",
        "b": "Точные GPS-координаты места съемки (вплоть до номера дома), модель смартфона и дату кадра.",
        "c": "Только название операционной системы компьютера.",
        "d": "Будущие мечты пользователя.",
        "e": "Фотографии не содержат никаких скрытых сведений.",
        "correct": "B",
        "topic": "Урок 21 (7-нед): Цифровой след и приватность EXIF",
        "expl": "Метаданные EXIF в оригинале фотографии содержат точные координаты съемки (геолокацию), поэтому перед публикацией их нужно удалять."
    },
    {
        "text": "На 8-й неделе (Урок 22), что означает фундаментальное 'Правило Большого Экрана' (Billboard Rule)?",
        "a": "Каждый школьник обязан купить себе огромный телевизор.",
        "b": "Если вы постеснялись бы вывесить фото или запись на огромный рекламный экран в центре города — не выкладывайте это в интернет!",
        "c": "Необходимо постоянно закрывать экран шторами.",
        "d": "Правило использовать только телефоны с большой диагональю.",
        "e": "Требование играть в игры только в кинотеатрах.",
        "correct": "B",
        "topic": "Урок 22 (8-нед): Правило Большого Экрана (Billboard Rule)",
        "expl": "Billboard Rule напоминает: интернет публичен. То, что вы не готовы показать всему городу на билборде, нельзя доверять сети."
    },
    {
        "text": "Какое главное правило отличает настоящего юного разработчика (Vibecoder) по итогам 1-й четверти 5–6 классов?",
        "a": "Копировать чужие игры целиком и выдавать их за свои.",
        "b": "Уметь творчески создавать игры с помощью ИИ, строго соблюдая цифровую безопасность и правила приватности.",
        "c": "Никогда не изучать новые технологии и языки кода.",
        "d": "Играть в компьютерные игры сутки напролет без перерыва.",
        "e": "Нажимать на все незнакомые ссылки в интернете без разбора.",
        "correct": "B",
        "topic": "Итоги четверти: Стандарт юного Vibecoder",
        "expl": "Vibecoder 5–6 классов — это создатель цифровых миров с помощью ИИ, который бережет свои данные и уважает цифровую гигиену."
    }
]

print("Grade 5-6 TRUE Vibecoding test data loaded (25 questions UZ & RU). Teacher: Ismoiljon Usmonov.")
