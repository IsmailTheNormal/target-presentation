#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Target International School — 5–6-Sinf Vibecoding Test Ma'lumotlari
Fan: Vibecoding (Junior Creators, Kiber-O'yinlar va Raqamli Madaniyat)
O'qituvchi: Ismoiljon Usmonov · Yunusobod filiali

Struktura:
- 18 ta tushunarli, aniq va asosiy savollar (Steady)
- 7 ta qiziqarli amaliy bilim savollari (Tricky Real Knowledge)
- Barcha savollar veb-platformadagi darslar (index.html va classes/5-6-sinf/) asosida tuzilgan
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
        {"grade": "A'lo (5)", "range": "22 – 25 ball", "desc": "O'yin yaratish, qahramonlar boshqaruvi va kiber-xavfsizlik bo'yicha a'lo bilim"},
        {"grade": "Yaxshi (4)", "range": "18 – 21 ball", "desc": "Asosiy o'yin mexanikasi va xavfsizlik qoidalarini yaxshi o'zlashtirgan"},
        {"grade": "Qoniqarli (3)", "range": "13 – 17 ball", "desc": "Ayrim o'yin obyektlari va parollar mavzusini takrorlash kerak"},
        {"grade": "Qoniqarsiz (2)", "range": "0 – 12 ball", "desc": "Vibecoding asoslari qayta o'rganilishi lozim"}
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
        {"grade": "Отлично (5)", "range": "22 – 25 баллов", "desc": "Отличные знания создания игр, управления героями и кибербезопасности"},
        {"grade": "Хорошо (4)", "range": "18 – 21 балл", "desc": "Игровая механика и правила безопасности хорошо освоены"},
        {"grade": "Удовл. (3)", "range": "13 – 17 баллов", "desc": "Требуется повторение игровых объектов и правил создания паролей"},
        {"grade": "Неудовл. (2)", "range": "0 – 12 баллов", "desc": "Необходимо повторить основы Vibecoding"}
    ]
}

QUESTIONS_5_6_UZ = [
    # 1. Steady
    {
        "text": "1-darsga ko'ra, Sun'iy intellekt (AI) nima va u bizga qanday yordam beradi?",
        "a": "U inson kabi tirik mavjudot bo'lib, o'zi mustaqil ovqatlanadi.",
        "b": "U kompyuter dasturi bo'lib, o'rgatilgan bilimlar asosida bizga matn, rasm va o'yin kodlarini yozishda yordam beradi.",
        "c": "U kompyuterni buzib qo'yadigan zararli virus.",
        "d": "U faqat telefonning batareyasini quvvatlaydigan qurilma.",
        "e": "U faqat oddiy soat vazifasini bajaradi.",
        "correct": "B",
        "topic": "01-dars: AI nima",
        "expl": "AI — bu inson kiritgan ma'lumotlar asosida savollarga javob beradigan va o'yin yaratishda ko'maklashadigan aqlli dastur."
    },
    # 2. Steady
    {
        "text": "2-darsda o'rganilganidek, AI yordamida o'yin qahramoniga (NPC) xarakter berish uchun nima qilish kerak?",
        "a": "Kompyuter ekranini o'chirib qo'yish kerak.",
        "b": "Promptda uning ismi, kasbi, qanday gapirishi (quvnoq yoki jiddiy) va maqsadini yozib berish kerak.",
        "c": "Faqat bitta nuqta qo'yib yuborish kifoya.",
        "d": "Klaviatura simini uzib qo'yish kerak.",
        "e": "O'yin qahramoniga faqat raqamlarni aytish kerak.",
        "correct": "B",
        "topic": "02-dars: AI Aktyor va NPC",
        "expl": "Promptda qahramonning xarakteri va fe'l-atvori qanchalik aniq yozilsa, AI unga shunchalik qiziqarli xarakter bag'ishlaydi."
    },
    # 3. Steady
    {
        "text": "3-darsdagi 'Game Lore' (O'yin afsonasi) nima uchun kerak?",
        "a": "O'yinni darhol o'chirib tashlash uchun.",
        "b": "O'yin dunyosi qanday paydo bo'lgani, qahramonning siri va sarguzashtli tarixini bilish uchun.",
        "c": "Faqat kompyuter sichqonchasini tezroq qilish uchun.",
        "d": "O'yinda faqat bitta rang ishlatilishi uchun.",
        "e": "O'yinchining internetini o'chirish uchun.",
        "correct": "B",
        "topic": "03-dars: Game Lore",
        "expl": "Game Lore — bu o'yin olamining qiziqarli hikoyasi bo'lib, o'yinchiga nima uchun kurashayotganini tushuntiradi."
    },
    # 4. Steady
    {
        "text": "4-darsda o'yin uchun 'Concept Art' (boshlang'ich rasm) chizdirishda qaysi uslubni tanlash mumkin?",
        "a": "Faqat oq qog'oz uslubi.",
        "b": "Pixel Art, Cyberpunk, 3D multfilm yoki Anime uslublari.",
        "c": "Faqat ko'rinmas shaffof uslub.",
        "d": "Faqat xira qora dog'lar uslubi.",
        "e": "Hech qanday uslubni tanlab bo'lmaydi.",
        "correct": "B",
        "topic": "04-dars: Concept Art va Uslublar",
        "expl": "Concept art chizdirishda Pixel Art yoki 3D multfilm kabi aniq uslub nomlari berilsa, chiroyli rasm chiqadi."
    },
    # 5. Steady
    {
        "text": "5-darsda 'Deepfake' (sun'iy intellekt chizgan soxta surat) larni qaysi belgisidan payqash mumkin?",
        "a": "Surat fayli nomidan.",
        "b": "Qo'ldagi barmoqlar soni g'alati (masalan 6 ta) bo'lib qolishi yoki ko'zlardagi akslar tabiiy bo'lmasligidan.",
        "c": "Suratda osmon ko'k rangda bo'lishidan.",
        "d": "Suratda mashina borligidan.",
        "e": "Surat tiniq ko'ringanidan.",
        "correct": "B",
        "topic": "05-dars: Deepfake belgilari",
        "expl": "AI ko'pincha qo'l barmoqlarini, sirg'alarni yoki ko'z qorachiqlarini chizishda noaniqlik va xatolarga yo'l qo'yadi."
    },
    # 6. Steady
    {
        "text": "6-darsdagi 'Demo Day' da 1 daqiqalik taqdimotda nima haqida gapiriladi?",
        "a": "Ertalab nima ovqat yeyilgani haqida.",
        "b": "O'z o'yiningiz nomi, unda nima qilish kerakligi va eng qiziqarli joyi haqida.",
        "c": "Faqat klaviatura tugmalari soni haqida.",
        "d": "Kompyuter ekranining narxi haqida.",
        "e": "Hech narsa gapirmasdan jim turish kerak.",
        "correct": "B",
        "topic": "06-dars: Game Pitch va Demo Day",
        "expl": "1 daqiqalik pitch taqdimotida o'yinning asosiy g'oyasi va eng qiziqarli mexanikasi sinfdoshlarga tushuntiriladi."
    },
    # 7. Steady
    {
        "text": "7-darsda o'rganilgan 3D modellar nimalardan tashkil topadi?",
        "a": "Faqatgina oddiy suv tomchilaridan.",
        "b": "Mesh (to'r) deb ataluvchi nuqtalar, qirralar va poligonlar to'plamidan.",
        "c": "Faqat qog'oz varaqlaridan.",
        "d": "Faqat audio quloqchinlardan.",
        "e": "Faqat elektr simlaridan.",
        "correct": "B",
        "topic": "07-dars: 3D Modellar va Mesh",
        "expl": "3D obyektlar fazoda nuqtalardan tashkil topgan to'r (mesh) ko'rinishida yasaladi va ustiga rang beriladi."
    },
    # 8. Tricky (Real Knowledge)
    {
        "text": "8-darsda 'Level Design' qilayotganda, platformalar orasiga nega kamida 2-3 ta katak bo'sh joy qoldiriladi?",
        "a": "Faqat o'yin hajmini kichraytirish uchun.",
        "b": "Chunki qahramon bir sakrashda ma'lum masofani bosib o'tadi; agar oraliq juda uzoq bo'lsa sakrab yeta olmaydi, juda yaqin bo'lsa o'yin qiziqsiz bo'lib qoladi.",
        "c": "Kompyuter qotib qolmasligi uchun.",
        "d": "O'yinda ranglar aralashib ketmasligi uchun.",
        "e": "O'yin faqat sichqoncha bilan o'ynalishi uchun.",
        "correct": "B",
        "topic": "08-dars: Level Design masofalari",
        "expl": "O'yin qiziq bo'lishi uchun sakrash masofasi aniq o'lchanadi: yetib bo'lmaydigan darajada uzoq yoki o'ta oson bo'lmasligi kerak."
    },
    # 9. Steady
    {
        "text": "9-darsda o'yinlardagi SFX (Sound Effects) nima?",
        "a": "Faqat kompyuterni o'chirish ovozi.",
        "b": "Qahramon sakraganda, tanga olganda yoki to'siqqa tekkanda chiqadigan qisqa tovush effektlari.",
        "c": "Faqat televizor yangiliklari diktori ovozi.",
        "d": "Kompyuter fanining shovqini.",
        "e": "Telefonning zaryad olayotgan ovozi.",
        "correct": "B",
        "topic": "09-dars: SFX Ovozlar",
        "expl": "SFX — o'yindagi harakatlarga javoban chalinadigan tovushlar (sakrash 'hop', tanga 'jiring')."
    },
    # 10. Tricky (Real Knowledge)
    {
        "text": "10-darsda 'Tarmoqlanuvchi Dialog' da o'yinchi NPC ga 'Yordam beraman' deb javob bersa nima sodir bo'ladi?",
        "a": "O'yin darhol kompyuterdan o'chib ketadi.",
        "b": "NPC o'yinchiga yangi kvest (topshiriq) beradi va o'yin hikoyasi boshqa yo'nalish bo'yicha davom etadi.",
        "c": "Kompyuter monitori qorayib qoladi.",
        "d": "NPC qahramonning barcha ballarini o'chirib yuboradi.",
        "e": "Hech qanday o'zgarish bo'lmaydi.",
        "correct": "B",
        "topic": "10-dars: Tarmoqlanuvchi Dialoglar",
        "expl": "Tarmoqlanuvchi dialoglarda har bir tanlov yangi vazifa, yangi sovg'a yoki boshqa ssenariyni ochib beradi."
    },
    # 11. Steady
    {
        "text": "11-darsda ekranning yuqori burchagidagi HUD panelida nimalar ko'rinib turadi?",
        "a": "Faqat o'qituvchining uy vazifasi.",
        "b": "Qahramonning joni (HP yurakchalari), to'plangan tangalar soni va o'yin vaqti.",
        "c": "Faqat internet saytlarining reklamasi.",
        "d": "Kompyuterning qattiq diski rasmi.",
        "e": "Faqat maktab binosi surati.",
        "correct": "B",
        "topic": "11-dars: HUD va HP Barlari",
        "expl": "HUD (interfeys paneli) o'yinchiga qancha joni va nechta tangasi qolganini doimo ko'rsatib turadi."
    },
    # 12. Steady
    {
        "text": "12-darsdagi 'Game Jam' marafonida bolalar nima bilan shug'ullanishadi?",
        "a": "Bir yil davomida bitta o'yinni o'ynab o'tirishadi.",
        "b": "Berilgan qisqa vaqt ichida o'z g'oyalari bo'yicha ishlaydigan yangi mini-o'yin prototipini yaratishadi.",
        "c": "Kompyuter klaviaturalarini bo'yashadi.",
        "d": "Faqat tayyor internet videolarini tomosha qilishadi.",
        "e": "Boshqa o'quvchilarning sichqonchasini yashirib qo'yishadi.",
        "correct": "B",
        "topic": "12-dars: Game Jam Mini-Prototip",
        "expl": "Game Jam — bu bolalar qisqa vaqt ichida o'zlarining shaxsiy kichik o'yinini yasab ko'radigan qiziqarli musobaqa."
    },
    # 13. Steady
    {
        "text": "13-darsdagi 'Game Loop' (O'yin tsikli) o'yinda qanday vazifani bajaradi?",
        "a": "O'yin boshlanishi bilan uni to'xtatib qo'yadi.",
        "b": "Soniyasiga ko'p marta aylanib, qahramon harakatini tekshiradi va ekrandagi rasmni yangilab turadi.",
        "c": "Faqat kompyuter ekranini o'chiradi.",
        "d": "O'yindagi barcha ballarni nol qiladi.",
        "e": "Faqat o'yin tugaganida ishlaydi.",
        "correct": "B",
        "topic": "13-dars: Game Loop",
        "expl": "Game Loop to'xtovsiz ishlab, o'yinchining tugmalarni bosganini ko'rib, qahramonni ekranda harakatlantiradi."
    },
    # 14. Steady
    {
        "text": "14-darsda qahramon o'tkir tikanga yoki lazerga tegib ketsa nima bo'ladi?",
        "a": "Qahramonning joni (HP) birdan 1000 ga yetadi.",
        "b": "Qahramonning joni (HP) bittaga kamayadi va agar joni 0 bo'lsa 'Game Over' bo'ladi.",
        "c": "O'yin avtomatik ravishda yutiladi.",
        "d": "Kompyuter o'chib qoladi.",
        "e": "O'yin tezligi 100 baravar sekinlashadi.",
        "correct": "B",
        "topic": "14-dars: To'siqlar va HP",
        "expl": "Xavfli to'siqqa tekkanda o'yinchining joni (HP) kamayadi, barcha jonlari tugasa o'yin qaytadan boshlanadi."
    },
    # 15. Steady
    {
        "text": "15-darsda o'yindagi oltin kristallga qahramon yetib borganda nima yuz beradi?",
        "a": "O'yin to'xtab qoladi.",
        "b": "Ochko ko'payadi, quvnoq tovush chiqadi va olingan kristall xaritadan yo'qoladi.",
        "c": "Qahramon o'yin maydonidan tushib ketadi.",
        "d": "Kristall butun ekranni to'sib qo'yadi.",
        "e": "O'yindagi hamma narsa muzlab qoladi.",
        "correct": "B",
        "topic": "15-dars: Kristall to'plash",
        "expl": "Kristall yig'ilganda ballar soni oshadi, tovush yangraydi va kristall yana qayta olinmasligi uchun ekrandan o'chiriladi."
    },
    # 16. Tricky (Real Knowledge)
    {
        "text": "16-darsda Boss jangida 'Lazer Qalqoni' ni qaysi paytda yoqish eng to'g'ri strategiya hisoblanadi?",
        "a": "Boss umuman hujum qilmayotgan paytda.",
        "b": "Boss kuchli lazer nurlarini o'yinchiga qaratib otgan paytda, zarardan saqlanish uchun.",
        "c": "O'yin boshlanmasdan oldin.",
        "d": "Faqat o'yinda yutqazib bo'lgandan keyin.",
        "e": "Qalqonni hech qachon ishlatmaslik kerak.",
        "correct": "B",
        "topic": "16-dars: Boss jangi va Qalqon",
        "expl": "Lazer qalqoni qisqa muddatga ishlaydi, shuning uchun uni aynan Boss qizil lazer hujumini boshlagan paytda yoqish kerak."
    },
    # 17. Tricky (Real Knowledge)
    {
        "text": "4-hafta 15-darsda 'Dushman AI' qahramon uning ko'rish doirasidan TASHQARIDA bo'lganida nima qiladi?",
        "a": "O'yin maydonidan uchib ketadi.",
        "b": "O'zining platformasida tinchgina u yoqdan-bu yoqqa qarab patrul qilib yuradi.",
        "c": "O'yin maydonidagi barcha kristallarni yeb qo'yadi.",
        "d": "To'g'ridan-to'g'ri o'yinchining ustiga sakraydi.",
        "e": "Darhol o'zini o'zi yo'q qiladi.",
        "correct": "B",
        "topic": "15-dars (4-h): Dushman AI patruli",
        "expl": "Dushman faqat o'yinchi uning yaqiniga (ko'rish doirasiga) kelgandagina quva boshlaydi, ungacha o'z joyida patrul qiladi."
    },
    # 18. Tricky (Real Knowledge)
    {
        "text": "4-hafta 16-darsda o'zimiz yaratgan levelni do'stimizga yuborish uchun 'Level Kodi' dan qanday foydalanamiz?",
        "a": "Do'stimizning uyiga borib kompyuterni ochib beramiz.",
        "b": "Redaktorda chiqqan qisqa kodli matnni nusxalab (copy), chatdan do'stimizga yuboramiz va u o'z o'yiniga joylaydi (import).",
        "c": "Faqat telefon bilan ekranni rasmga olamiz.",
        "d": "O'yin kodini butunlay o'chirib tashlaymiz.",
        "e": "Level kodini hech kimga berib bo'lmaydi.",
        "correct": "B",
        "topic": "16-dars (4-h): Level Kodi va Ulashish",
        "expl": "Level kodi xaritadagi barcha bloklar o'rnini matnga aylantiradi, do'stingiz bu kodni kiritib aynan sizning levelingizni o'ynay oladi."
    },
    # 19. Steady
    {
        "text": "5-hafta 17-darsga ko'ra, quyidagi parollardan qaysi biri eng mustahkam va xavfsiz hisoblanadi?",
        "a": "12345678",
        "b": "Target#2026!Kiber",
        "c": "parol123",
        "d": "admin",
        "e": "qwertyui",
        "correct": "B",
        "topic": "17-dars (5-h): Kuchli parollar",
        "expl": "Kuchli parol kamida 10-12 belgidan iborat bo'lib, katta-kichik harflar, raqamlar va maxsus belgilarni (#!) o'z ichiga oladi."
    },
    # 20. Steady
    {
        "text": "5-hafta 18-darsda o'rganilgan 'Fishing' (Phishing) aldovi nima?",
        "a": "Baliq ovi haqidagi qiziqarli o'yin.",
        "b": "Haqiqiy saytga o'xshatib yasalgan soxta havola orqali o'quvchilarning parolini o'g'irlash usuli.",
        "c": "Kompyuterga yangi o'yin yuklash usuli.",
        "d": "Maktab veb-saytini chiroyli qilish usuli.",
        "e": "Internet tezligini oshirish dasturi.",
        "correct": "B",
        "topic": "18-dars (5-h): Fishing havolalar",
        "expl": "Fishing — xakerlar yasagan soxta sahifa bo'lib, u orqali akkaunt logini va parolini aldov yo'li bilan bilib olishadi."
    },
    # 21. Steady
    {
        "text": "5-hafta 19-darsda 'Troyalik Ot' (Trojan) virusi kompyuterga qanday niqob ostida kirib oladi?",
        "a": "Faqat kompyuterni tozalash paytida.",
        "b": "'Tekin Robux', 'O'yin uchun cheat' yoki 'Tekin o'yin' niqobi ostida soxta fayl ko'rinishida.",
        "c": "Faqat maktab kundaligi ochilganda.",
        "d": "Faqat rasm chizadigan dasturda.",
        "e": "Kompyuterga hech qanday virus kirmaydi.",
        "correct": "B",
        "topic": "19-dars (5-h): Troyan viruslari",
        "expl": "Troyan virusi tekin qiziqarli o'yin yoki tekin o'yin boyligi niqobida bo'ladi va o'rnatilgach tizimni buzadi."
    },
    # 22. Steady
    {
        "text": "6-hafta 20-darsda biz yaratgan 'Cyber Shield' kiber-detektor ilovasi nima ish qilar edi?",
        "a": "Faqat kompyuter o'yinlarini o'ynatar edi.",
        "b": "Chatdagi shubhali xabarlarni tekshirib, yolg'on va firibgarlik bor joylarni qizil bilan ko'rsatar edi.",
        "c": "Uy vazifasini o'quvchi o'rniga ishlab berar edi.",
        "d": "Kompyuterdagi suratlarni o'chirib yuborar edi.",
        "e": "Faqat musiqa chalar edi.",
        "correct": "B",
        "topic": "20-dars (6-h): Cyber Shield ilovasi",
        "expl": "Cyber Shield chatda kelgan 'tekin narsalar' va soxta havolalarni tekshirib, xavfdan ogohlantiradi."
    },
    # 23. Tricky (Real Knowledge)
    {
        "text": "7-hafta 21-darsda uyda olingan oddiy suratni internetga joylashda qaysi xavfli yashirin ma'lumot (EXIF) oshkor bo'lishi mumkin?",
        "a": "Faqat surat olingan xonaning havo harorati.",
        "b": "Surat fayli ichidagi aniq GPS koordinatalari (uyning xaritadagi joylashuv manzili).",
        "c": "Faqat kompyuterning modeli.",
        "d": "Foydalanuvchining kelajakdagi rejalari.",
        "e": "Suratlarda hech qachon yashirin ma'lumot bo'lmaydi.",
        "correct": "B",
        "topic": "21-dars (7-h): EXIF va GPS Maxfiyligi",
        "expl": "Telefonlar har bir surat ichiga uning qayerda (GPS) olinganini yozib qo'yadi, shuning uchun uydan olingan rasmlarni ehtiyotkorlik bilan yuklash kerak."
    },
    # 24. Steady
    {
        "text": "8-hafta 22-darsdagi 'Katta Ekran Qoidasi' (Billboard Rule) nima haqida ogohlantiradi?",
        "a": "Katta televizor sotib olish haqida.",
        "b": "Katta ko'cha ekraniga osishga uyaladigan shaxsiy rasm yoki xabarni aslo internetga yuklamaslik haqida.",
        "c": "O'yinlarni faqat kinoteatrda ko'rish haqida.",
        "d": "Telefon ekranini qorong'i qilish haqida.",
        "e": "Kompyuter ekranini pardalar bilan to'sish haqida.",
        "correct": "B",
        "topic": "22-dars (8-h): Katta Ekran Qoidasi",
        "expl": "Internet — butun shahar ko'radigan katta ekran kabi. Begonalar ko'rishini istamagan narsangizni tarmoqqa qo'ymang."
    },
    # 25. Steady
    {
        "text": "Vibecoding darslarida o'rganilgan eng muhim qoida qaysi?",
        "a": "Boshqalarning o'yinini o'g'irlab, o'zimniki deyish.",
        "b": "Sun'iy intellektdan unumli foydalanib o'z o'yinlarimizni yaratish va kiber-xavfsizlik qoidalariga doimo amal qilish.",
        "c": "Kun bo'yi faqat o'yin o'ynash.",
        "d": "Notanish odamlar yuborgan har qanday havolani bosish.",
        "e": "Parollarni hamma do'stlarga tarqatish.",
        "correct": "B",
        "topic": "Xulosa: Yosh Vibecoder qoidasi",
        "expl": "Haqiqiy Vibecoder — AI yordamida yangi foydali loyihalar yaratadigan va o'zini kiber-xavflardan himoya qila oladigan ijodkordir."
    }
]

QUESTIONS_5_6_RU = [
    # 1. Steady
    {
        "text": "Согласно Уроку 1, что такое Искусственный Интеллект (ИИ) и как он нам помогает?",
        "a": "Это живое существо, как человек, которое само кушает.",
        "b": "Это умная компьютерная программа, которая на основе обученных знаний помогает нам писать тексты, рисовать и создавать игры.",
        "c": "Это вредоносный вирус, ломающий компьютер.",
        "d": "Это прибор, который только заряжает аккумулятор телефона.",
        "e": "Это обычные простые часы на стене.",
        "correct": "B",
        "topic": "Урок 01: Что такое ИИ",
        "expl": "ИИ — это умный цифровой помощник, обученный на огромных данных, который помогает писать код и генерировать идеи."
    },
    # 2. Steady
    {
        "text": "Как мы узнали на Уроке 2, что нужно сделать в промпте, чтобы задать характер игровому персонажу (NPC)?",
        "a": "Нужно просто выключить монитор компьютера.",
        "b": "В промпте нужно четко описать его имя, профессию, настроение (веселый или строгий) и его цель.",
        "c": "Достаточно отправить одну точку.",
        "d": "Нужно выдернуть шнур клавиатуры.",
        "e": "Нужно заставить персонажа называть только цифры.",
        "correct": "B",
        "topic": "Урок 02: ИИ Актёр и персонажи NPC",
        "expl": "Чем подробнее в промпте описаны характер и манера речи персонажа, тем интереснее и живее он получается в игре."
    },
    # 3. Steady
    {
        "text": "Для чего на Уроке 3 создается 'Game Lore' (Лор и предыстория игры)?",
        "a": "Чтобы моментально стереть игру с диска.",
        "b": "Чтобы знать историю появления игрового мира, тайну главного героя и смысл его приключений.",
        "c": "Исключительно для ускорения мышки.",
        "d": "Чтобы в игре был только один цвет.",
        "e": "Чтобы отключить интернет игроку.",
        "correct": "B",
        "topic": "Урок 03: Game Lore и история мира",
        "expl": "Game Lore — это сюжетная вселенная игры, которая объясняет игроку, ради чего он проходит уровни."
    },
    # 4. Steady
    {
        "text": "На Уроке 4, какой стиль можно выбрать при генерации концепт-арта (Concept Art) для игры?",
        "a": "Только стиль чистого белого листа.",
        "b": "Стили Pixel Art, Киберпанк, 3D мультфильм или Аниме.",
        "c": "Только полностью невидимый прозрачный стиль.",
        "d": "Стиль размытых черных клякс.",
        "e": "Никакой стиль выбрать невозможно.",
        "correct": "B",
        "topic": "Урок 04: Концепт-арт и стили",
        "expl": "Указание конкретного визуального стиля (например, Pixel Art или 3D мультфильм) позволяет получить яркий и гармоничный арт."
    },
    # 5. Steady
    {
        "text": "По какому признаку на Уроке 5 можно разоблачить 'Дипфейк' (картинку, нарисованную нейросетью)?",
        "a": "По названию файла фотографии.",
        "b": "По странному количеству пальцев на руках (например, 6 пальцев) или неестественным бликам в глазах.",
        "c": "По тому, что небо на картинке голубого цвета.",
        "d": "По тому, что на картинке нарисована машина.",
        "e": "По тому, что картинка очень четкая.",
        "correct": "B",
        "topic": "Урок 05: Признаки дипфейка",
        "expl": "Нейросети часто ошибаются в сложной анатомии: рисуют лишние пальцы, неровные уши и смазанные зрачки."
    },
    # 6. Steady
    {
        "text": "О чем рассказывают ученики во время минутной презентации на 'Demo Day' (Урок 6)?",
        "a": "О том, что они кушали сегодня на завтрак.",
        "b": "О названии своей игры, о том, как в нее играть и какая в ней самая захватывающая фишка.",
        "c": "Только о количестве кнопок на клавиатуре.",
        "d": "О стоимости монитора компьютера.",
        "e": "Нужно просто молчать и ничего не говорить.",
        "correct": "B",
        "topic": "Урок 06: Game Pitch и презентация",
        "expl": "За 1 минуту питча автор рассказывает главную идею игры и показывает одноклассникам ее самый крутой момент."
    },
    # 7. Steady
    {
        "text": "Из чего состоят 3D модели, которые мы изучали на Уроке 7?",
        "a": "Исключительно из капель воды.",
        "b": "Из полигональной сетки (Mesh), состоящей из вершин, граней и маленьких многоугольников.",
        "c": "Только из бумажных страниц тетради.",
        "d": "Исключительно из наушников.",
        "e": "Только из электрических проводов.",
        "correct": "B",
        "topic": "Урок 07: 3D Модели и сетка Mesh",
        "expl": "Каркас любой трехмерной модели состоит из полигональной сетки (Mesh), на которую натягивается текстура."
    },
    # 8. Tricky (Real Knowledge)
    {
        "text": "На Уроке 8 при дизайне уровня (Level Design), почему между платформами оставляют расстояние в 2-3 клетки?",
        "a": "Только чтобы уменьшить размер игры.",
        "b": "Потому что герой прыгает на определенную дистанцию: если сделать слишком далеко — не допрыгнет, а если слишком близко — играть неинтересно.",
        "c": "Чтобы компьютер не зависал.",
        "d": "Чтобы цвета в игре не перемешались.",
        "e": "Чтобы играть можно было только одной мышкой.",
        "correct": "B",
        "topic": "Урок 08: Дизайн уровней и баланс прыжков",
        "expl": "Геймдизайнер выверяет дистанцию прыжка: яма должна быть преодолимой, но требовать от игрока внимания и сноровки."
    },
    # 9. Steady
    {
        "text": "Что такое звуковые эффекты SFX (Sound Effects) в играх (Урок 9)?",
        "a": "Звук выключения компьютера.",
        "b": "Короткие звуки при действиях героя: звук прыжка, звон подобранной монетки или звук удара.",
        "c": "Только голос диктора в вечерних новостях.",
        "d": "Шум вентилятора внутри ноутбука.",
        "e": "Звук подключения зарядного устройства.",
        "correct": "B",
        "topic": "Урок 09: Звуковые эффекты SFX",
        "expl": "SFX — это звуки конкретных действий (прыжок, взятие кристалла, получение урона), делающие игру живой."
    },
    # 10. Tricky (Real Knowledge)
    {
        "text": "На Уроке 10 в ветвящемся диалоге, что произойдет, если игрок ответит NPC: 'Да, я помогу тебе'?",
        "a": "Игра сразу же сотрется с компьютера.",
        "b": "NPC выдаст игроку новое задание (квест), и сюжет пойдет по новой интересной ветке.",
        "c": "Экран монитора полностью погаснет.",
        "d": "NPC отберет у героя все набранные очки.",
        "e": "Вообще ничего не изменится.",
        "correct": "B",
        "topic": "Урок 10: Ветвящиеся диалоги и квесты",
        "expl": "Ветвление сюжета реагирует на выбор игрока: согласие на помощь открывает новый квест и награду."
    },
    # 11. Steady
    {
        "text": "Что обычно отображается на панели HUD в верхнем углу игрового экрана (Урок 11)?",
        "a": "Домашнее задание от учителя.",
        "b": "Жизни героя (сердечки HP), количество собранных кристаллов и время игры.",
        "c": "Реклама сайтов из интернета.",
        "d": "Рисунок жесткого диска компьютера.",
        "e": "Фотография здания школы.",
        "correct": "B",
        "topic": "Урок 11: Панель HUD и сердечки HP",
        "expl": "Интерфейс HUD показывает текущее состояние персонажа: сколько жизней (HP) осталось и сколько монет собрано."
    },
    # 12. Steady
    {
        "text": "Чем занимаются ученики на творческом марафоне 'Game Jam' (Урок 12)?",
        "a": "Играют в одну и ту же игру целый год.",
        "b": "За короткое отведенное время создают свой собственный рабочий прототип новой мини-игры.",
        "c": "Раскрашивают кнопки клавиатуры красками.",
        "d": "Просто смотрят видеоролики в интернете.",
        "e": "Прячут мышки других учеников в классе.",
        "correct": "B",
        "topic": "Урок 12: Марафон Game Jam",
        "expl": "Game Jam — это хакатон, где ребята за короткий срок придумывают и собирают прототип настоящей игры."
    },
    # 13. Steady
    {
        "text": "Какую главную работу выполняет игровой цикл 'Game Loop' (Урок 13)?",
        "a": "Останавливает игру сразу после запуска.",
        "b": "Непрерывно много раз в секунду проверяет нажатия кнопок и перерисовывает кадры на экране.",
        "c": "Только выключает монитор компьютера.",
        "d": "Сбрасывает все очки до нуля.",
        "e": "Работает только тогда, когда игра уже закрыта.",
        "correct": "B",
        "topic": "Урок 13: Игровой цикл Game Loop",
        "expl": "Game Loop непрерывно работает со скоростью 60 кадров в секунду, обеспечивая плавное управление и анимацию."
    },
    # 14. Steady
    {
        "text": "Что происходит на Уроке 14, когда персонаж натыкается на острые шипы или лазер?",
        "a": "Количество жизней героя резко возрастает до 1000.",
        "b": "Персонаж теряет жизнь (HP уменьшается), а если жизни кончились, наступает экран 'Game Over'.",
        "c": "Игра автоматически объявляется выигранной.",
        "d": "Компьютер полностью выключается.",
        "e": "Игра замедляется в 100 раз.",
        "correct": "B",
        "topic": "Урок 14: Препятствия и потеря HP",
        "expl": "При столкновении с опасностью отнимается сердечко HP; потеря всех жизней ведет к перезапуску уровня."
    },
    # 15. Steady
    {
        "text": "Что происходит на Уроке 15, когда герой касается золотого кристалла в игре?",
        "a": "Игра зависает.",
        "b": "Игроку начисляются очки, звучит приятный SFX, а сам кристалл исчезает с экрана.",
        "c": "Персонаж проваливается сквозь землю.",
        "d": "Кристалл закрывает собой весь монитор.",
        "e": "Все объекты в игре замерзают.",
        "correct": "B",
        "topic": "Урок 15: Сбор кристаллов и очков",
        "expl": "Подобранный кристалл увеличивает счет игрока, издает победный звон и убирается с карты."
    },
    # 16. Tricky (Real Knowledge)
    {
        "text": "В битве с Боссом (Урок 16), в какой именно момент выгоднее всего включать 'Лазерный Щит'?",
        "a": "Когда Босс вообще не стреляет и спокойно стоит.",
        "b": "В момент, когда Босс выпускает мощные лазерные лучи в героя, чтобы отразить урон.",
        "c": "До того, как игра вообще началась.",
        "d": "Только после того, как игра уже проиграна.",
        "e": "Щит вообще никогда не нужно включать.",
        "correct": "B",
        "topic": "Урок 16: Тактика щита в битве с Боссом",
        "expl": "Заряд щита кратковременный, поэтому его берегут для защиты от самых мощных лазерных атак босса."
    },
    # 17. Tricky (Real Knowledge)
    {
        "text": "На Уроке 15 (4-я неделя), как ведет себя 'ИИ врага', пока игрок находится ВНЕ зоны его видимости?",
        "a": "Враг улетает за пределы игрового поля.",
        "b": "Он спокойно ходит взад-вперед (патрулирует) по своей платформе.",
        "c": "Он съедает все кристаллы на уровне.",
        "d": "Он сразу прыгает на голову игроку через всю карту.",
        "e": "Он моментально взрывается сам по себе.",
        "correct": "B",
        "topic": "Урок 15 (4-нед): Патрулирование врагов",
        "expl": "Враг переходит в режим погони только тогда, когда игрок зашел в его радиус видимости; до этого он просто патрулирует."
    },
    # 18. Tricky (Real Knowledge)
    {
        "text": "Как переслать другу созданную в редакторе карту с помощью 'Кода Уровня' (Урок 16, 4-я неделя)?",
        "a": "Прийти к другу домой и включить его компьютер.",
        "b": "Скопировать сгенерированный редактором текст кода и отправить в чат, а друг нажмет кнопку 'Импорт'.",
        "c": "Сфотографировать экран телефоном.",
        "d": "Полностью стереть весь код игры.",
        "e": "Созданную карту вообще никому нельзя отправить.",
        "correct": "B",
        "topic": "Урок 16 (4-нед): Код Уровня и кнопка импорта",
        "expl": "Редактор превращает карту в текстовую строчку (Level Code), которую можно отправить в сообщении и загрузить в игру."
    },
    # 19. Steady
    {
        "text": "Какой из следующих паролей является самым надежным и взломостойким (Урок 17, 5-я неделя)?",
        "a": "12345678",
        "b": "Target#2026!Kiber",
        "c": "parol123",
        "d": "admin",
        "e": "qwertyui",
        "correct": "B",
        "topic": "Урок 17 (5-нед): Надежные пароли",
        "expl": "Надежный пароль длинный (10+ знаков) и содержит большие и маленькие буквы, цифры и спецсимволы (!#)."
    },
    # 20. Steady
    {
        "text": "Что такое 'Фишинг' (Phishing), изученный на Уроке 18 (5-я неделя)?",
        "a": "Компьютерная игра про рыбалку на озере.",
        "b": "Поддельная ссылка-ловушка, похожая на настоящий сайт, созданная мошенниками для кражи паролей.",
        "c": "Способ бесплатно скачать новую игру.",
        "d": "Способ украсить сайт школы.",
        "e": "Программа для ускорения интернета.",
        "correct": "B",
        "topic": "Урок 18 (5-нед): Фишинговые ссылки",
        "expl": "Фишинг заманивает на поддельный сайт, чтобы выманить логин и пароль от аккаунта."
    },
    # 21. Steady
    {
        "text": "Под каким видом вирус 'Троянский Конь' чаще всего проникает на компьютеры (Урок 19, 5-я неделя)?",
        "a": "Только во время протирки клавиатуры от пыли.",
        "b": "Под видом 'бесплатных робуксов', 'читов для игры' или 'взломанной бесплатной игры'.",
        "c": "Только при открытии школьного электронного дневника.",
        "d": "Исключительно в программе для рисования.",
        "e": "Вирусов на компьютерах вообще не бывает.",
        "correct": "B",
        "topic": "Урок 19 (5-нед): Троянские программы",
        "expl": "Троян притворяется полезной игрой или подарком, но на самом деле открывает доступ злоумышленникам."
    },
    # 22. Steady
    {
        "text": "Какую задачу выполняло веб-приложение 'Cyber Shield', которое мы собирали на Уроке 20?",
        "a": "Оно только запускало игры.",
        "b": "Оно проверяло подозрительные сообщения чата и подсвечивало красным цветом обман и ловушки.",
        "c": "Оно решало домашнее задание за учеников.",
        "d": "Оно стирало фотографии с компьютера.",
        "e": "Оно только проигрывало музыку.",
        "correct": "B",
        "topic": "Урок 20 (6-нед): Приложение Cyber Shield",
        "expl": "Cyber Shield анализирует текст сообщений и предостерегает от фальшивых предложений и мошенников."
    },
    # 23. Tricky (Real Knowledge)
    {
        "text": "Какую опасную скрытую информацию (EXIF) может выдать обычная фотография, сделанная дома (Урок 21)?",
        "a": "Температуру воздуха в комнате.",
        "b": "Точные GPS-координаты дома, вшитые в файл фотографии телефоном.",
        "c": "Модель монитора компьютера.",
        "d": "Планы пользователя на завтрашний день.",
        "e": "Фотографии вообще никогда не содержат скрытых данных.",
        "correct": "B",
        "topic": "Урок 21 (7-нед): GPS-данные в фотографиях",
        "expl": "Смартфоны записывают в свойства фото точные координаты места съемки, поэтому домашние фото нельзя бездумно слать чужим."
    },
    # 24. Steady
    {
        "text": "О чем предупреждает 'Правило Большого Экрана' (Billboard Rule) из Урока 22 (8-я неделя)?",
        "a": "О том, что нужно купить огромный телевизор.",
        "b": "О том, что нельзя выкладывать в интернет фото или слова, которые постеснялся бы показать на огромном экране посреди города.",
        "c": "О том, что фильмы нужно смотреть только в кинотеатре.",
        "d": "О том, что нужно сделать экран телефона темным.",
        "e": "О том, что монитор нужно закрывать шторами.",
        "correct": "B",
        "topic": "Урок 22 (8-нед): Правило Большого Экрана",
        "expl": "Billboard Rule: Интернет публичен. Если вы не готовы показать фото всему городу на билборде — не выкладывайте его в сеть."
    },
    # 25. Steady
    {
        "text": "Какое главное правило отличает настоящего юного разработчика (Vibecoder)?",
        "a": "Копировать чужие игры и говорить, что сделал сам.",
        "b": "Умно использовать ИИ для создания крутых игр и всегда соблюдать правила цифровой безопасности.",
        "c": "Играть в компьютерные игры целыми днями без перерыва.",
        "d": "Нажимать на любые незнакомые ссылки от чужих людей.",
        "e": "Раздавать свои пароли всем знакомым.",
        "correct": "B",
        "topic": "Итог: Правило юного Vibecoder",
        "expl": "Vibecoder создает классные игры и проекты с помощью технологий, при этом бережет свои данные и уважает других."
    }
]

print("Grade 5-6 Vibecoding test data loaded (18 steady + 7 tricky). Teacher: Ismoiljon Usmonov.")
