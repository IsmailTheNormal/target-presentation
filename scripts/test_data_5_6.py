#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Target International School — 5–6-Sinf Vibecoding Test Ma'lumotlari
Fan: Vibecoding (Junior Creators, Kiber-O'yinlar va Raqamli Madaniyat)
O'qituvchi: Ismoiljon Usmonov · Yunusobod filiali

Struktura:
- 25 ta tushunarli, bolalarbop, qulay va mustahkam savollar (Steady Easy)
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
        {"grade": "Qoniqarli (3)", "range": "13 – 17 ball", "desc": "Ayrim o'yin obyektlari va parollar mavzusini takrorlash lozim"},
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
        {"grade": "Удовл. (3)", "range": "13 – 17 баллов", "desc": "Требуется повторение игровых объектов и правил безопасности"},
        {"grade": "Неудовл. (2)", "range": "0 – 12 баллов", "desc": "Необходимо повторить основы Vibecoding"}
    ]
}

QUESTIONS_5_6_UZ = [
    {
        "text": "1-darsga ko'ra, Sun'iy intellekt (AI) nima va u bizga qanday yordam beradi?",
        "a": "U inson kabi tirik mavjudot bo'lib, o'zi mustaqil ovqatlanadi.",
        "b": "U aqlli kompyuter dasturi bo'lib, bizga matn yozish, rasm chizish va o'yin yaratishda yordam beradi.",
        "c": "U kompyuterni buzadigan zararli virus.",
        "d": "U faqat telefonning batareyasini quvvatlaydigan sim.",
        "e": "U oddiy devor soati.",
        "correct": "B",
        "topic": "01-dars: AI nima",
        "expl": "AI — bu inson bergan topshiriqlar asosida yangi g'oyalar va o'yinlar yaratishda yordam beruvchi aqlli dastur."
    },
    {
        "text": "2-darsda AI yordamida o'yin qahramoniga (NPC) xarakter berish uchun nima qilish kerak?",
        "a": "Kompyuter ekranini o'chirib qo'yish kerak.",
        "b": "Promptda uning ismi, kasbi, qanday gapirishi (quvnoq yoki botir) va maqsadini yozib berish kerak.",
        "c": "Faqat bitta nuqta qo'yib yuborish kifoya.",
        "d": "Klaviatura simini uzib qo'yish kerak.",
        "e": "O'yin qahramoniga faqat raqamlarni aytish kerak.",
        "correct": "B",
        "topic": "02-dars: AI Aktyor va NPC",
        "expl": "Promptda qahramonning xarakteri qanchalik aniq yozilsa, u o'yinda shunchalik qiziqarli gapiradi."
    },
    {
        "text": "3-darsdagi 'Game Lore' (O'yin afsonasi) nima?",
        "a": "O'yinni darhol o'chirib tashlash usuli.",
        "b": "O'yin dunyosining qiziqarli hikoyasi, qahramonning siri va sarguzashtli tarixi.",
        "c": "Faqat kompyuter sichqonchasini tezroq qilish usuli.",
        "d": "O'yinda faqat bitta rang ishlatish qoidasi.",
        "e": "O'yinchining internetini o'chirish usuli.",
        "correct": "B",
        "topic": "03-dars: Game Lore",
        "expl": "Game Lore — bu o'yin olamining ertaknamo qiziqarli tarixi bo'lib, o'yinni maroqli qiladi."
    },
    {
        "text": "4-darsda o'yin uchun boshlang'ich rasm (Concept Art) chizdirishda qaysi uslubni tanlash mumkin?",
        "a": "Faqat bo'sh oq qog'oz uslubi.",
        "b": "Pixel Art, Cyberpunk, 3D multfilm yoki Anime uslublari.",
        "c": "Faqat ko'rinmas shaffof uslub.",
        "d": "Faqat qora dog'lar uslubi.",
        "e": "Hech qanday uslubni tanlab bo'lmaydi.",
        "correct": "B",
        "topic": "04-dars: Concept Art uslublari",
        "expl": "Pixel Art yoki 3D multfilm kabi chiroyli uslublar yordamida o'yinimizga ajoyib rasmlar chizdiramiz."
    },
    {
        "text": "5-darsda 'Deepfake' (sun'iy intellekt chizgan soxta surat) larni qanday payqash mumkin?",
        "a": "Surat fayli nomidan.",
        "b": "Qo'ldagi barmoqlar soni g'alati (masalan 6 ta) bo'lib qolishi yoki ko'zlardagi akslar tabiiy bo'lmasligidan.",
        "c": "Suratda osmon ko'k rangda bo'lishidan.",
        "d": "Suratda mashina borligidan.",
        "e": "Surat tiniq ko'ringanidan.",
        "correct": "B",
        "topic": "05-dars: Deepfake belgilari",
        "expl": "AI ba'zan qo'l barmoqlarini yoki ko'z qorachiqlarini chizishda xato qilib qo'yadi va buni osongina payqash mumkin."
    },
    {
        "text": "6-darsdagi 'Demo Day' taqdimotida bolalar nima haqida gapirib berishadi?",
        "a": "Ertalab nima ovqat yeyilgani haqida.",
        "b": "O'z o'yini qanday atalishi, unda nima qilish kerakligi va qahramonning vazifasi haqida.",
        "c": "Faqat klaviatura tugmalari soni haqida.",
        "d": "Kompyuter ekranining narxi haqida.",
        "e": "Hech narsa gapirmasdan jim turishadi.",
        "correct": "B",
        "topic": "06-dars: Game Pitch taqdimoti",
        "expl": "Demo Day kuni har bir o'quvchi o'zi yaratgan o'yinni sinfdoshlariga faxr bilan ko'rsatib, tanishtiradi."
    },
    {
        "text": "7-darsda o'rganilgan 3D modellar kompyuterda nimalardan yasaladi?",
        "a": "Faqatgina oddiy suv tomchilaridan.",
        "b": "Mesh (to'r) deb ataluvchi nuqtalar va shakllar to'plamidan.",
        "c": "Faqat qog'oz varaqlaridan.",
        "d": "Faqat audio quloqchinlardan.",
        "e": "Faqat elektr simlaridan.",
        "correct": "B",
        "topic": "07-dars: 3D Modellar",
        "expl": "3D o'yin qahramonlari fazoviy nuqtalardan tashkil topgan shakllar to'plami (mesh) orqali chiziladi."
    },
    {
        "text": "8-darsda 'Level Design' (O'yin xaritasi) da qahramon yurishi uchun nimalar joylashtiriladi?",
        "a": "Faqat bo'sh qora ekran.",
        "b": "Sakrash uchun platformalar, yig'iladigan tangalar va qochish kerak bo'lgan to'siqlar.",
        "c": "Kompyuter drayverlari.",
        "d": "Faqat raqamlar ro'yxati.",
        "e": "Faqat maktab qoidalari.",
        "correct": "B",
        "topic": "08-dars: Level Design elementlari",
        "expl": "Level dizayneri o'yinchiga qiziq bo'lishi uchun sakraydigan yerlar (platformalar), tangalar va to'siqlarni chizadi."
    },
    {
        "text": "9-darsda o'yinlardagi SFX (Sound Effects) nima?",
        "a": "Kompyuterni o'chirish ovozi.",
        "b": "Qahramon sakraganda, tanga yig'ganda yoki to'siqqa tekkanda chiqadigan qisqa tovushlar.",
        "c": "Faqat televizor yangiliklari ovozi.",
        "d": "Kompyuter fanining shovqini.",
        "e": "Telefonning zaryad olayotgan ovozi.",
        "correct": "B",
        "topic": "09-dars: SFX tovushlar",
        "expl": "SFX — qahramon harakatlanganda chalinadigan quvnoq o'yin tovushlari (sakrash, tanga jiringlashi)."
    },
    {
        "text": "10-darsda o'yindagi qahramonlar (NPC) bilan suhbatda turli javob tanlansa nima bo'ladi?",
        "a": "O'yin darhol o'chib ketadi.",
        "b": "Qahramon boshqacha javob beradi va o'yinda yangi qiziqarli topshiriq (kvest) ochiladi.",
        "c": "Kompyuter ekrani qorayib qoladi.",
        "d": "Barcha ballar o'chib ketadi.",
        "e": "Hech narsa o'zgarmaydi.",
        "correct": "B",
        "topic": "10-dars: Aqlli NPC dialoglari",
        "expl": "Aqlli NPC larda o'yinchi tanlagan javobiga qarab yangi topshiriq yoki sovg'a beriladi."
    },
    {
        "text": "11-darsda ekranning yuqori qismidagi HUD panelida nimalar ko'rinib turadi?",
        "a": "Faqat ob-havo ma'lumoti.",
        "b": "Qahramonning joni (HP yurakchalari), to'plangan tangalari va o'yin vaqti.",
        "c": "Faqat do'kon reklamasi.",
        "d": "Kompyuterning qattiq diski rasmi.",
        "e": "Faqat maktab binosi surati.",
        "correct": "B",
        "topic": "11-dars: HUD paneli",
        "expl": "HUD paneli o'yinchiga nechta joni (HP) va nechta tangasi borligini doim ko'rsatib turadi."
    },
    {
        "text": "12-darsdagi 'Game Jam' marafonida bolalar nima qilishadi?",
        "a": "Kun bo'yi faqat uxlab yotishadi.",
        "b": "Qisqa vaqt ichida o'z g'oyalari bo'yicha kichik o'yin yasab ko'rishadi.",
        "c": "Kompyuter klaviaturalarini bo'yashadi.",
        "d": "Faqat tayyor internet videolarini tomosha qilishadi.",
        "e": "Boshqa o'quvchilarning sichqonchasini yashirib qo'yishadi.",
        "correct": "B",
        "topic": "12-dars: Game Jam marafoni",
        "expl": "Game Jam — bolalar qisqa vaqt ichida o'zlarining shaxsiy o'yinini yaratib sinab ko'radigan qiziqarli dars."
    },
    {
        "text": "13-darsdagi 'Game Loop' (O'yin tsikli) o'yinda nima vazifani bajaradi?",
        "a": "O'yinni boshlanishi bilanoq yopib qo'yadi.",
        "b": "Har doim qahramon qayerga yurganini tekshirib, ekrandagi o'yinni yangilab turadi.",
        "c": "Faqat kompyuter ekranini o'chiradi.",
        "d": "O'yindagi barcha ballarni nollashtiradi.",
        "e": "Faqat o'yin tugaganida ishlaydi.",
        "correct": "B",
        "topic": "13-dars: Game Loop boshqaruvi",
        "expl": "Game Loop to'xtovsiz ishlab, klaviatura bosilishiga qarab qahramonni ekranda harakatlantiradi."
    },
    {
        "text": "14-darsda qahramon o'tkir tikanga yoki qizil lazerga tegib ketsa nima bo'ladi?",
        "a": "Qahramonning joni birdan 1000 ga yetadi.",
        "b": "Qahramonning bitta joni (HP yurakchasi) kamayadi.",
        "c": "O'yin avtomatik yutiladi.",
        "d": "Kompyuter o'chib qoladi.",
        "e": "O'yin tezligi 100 baravar sekinlashadi.",
        "correct": "B",
        "topic": "14-dars: To'siqlar va HP",
        "expl": "Xavfli to'siqqa tekkanda o'yinchining bitta joni ketadi, agar hamma jonlari tugasa o'yin qayta boshlanadi."
    },
    {
        "text": "15-darsda qahramon yaltirab turgan oltin kristallga yetib borsa nima bo'ladi?",
        "a": "O'yin to'xtab qoladi.",
        "b": "Ochko ko'payadi, chiroyli tovush chiqadi va kristall xaritadan olinadi.",
        "c": "Qahramon o'yin maydonidan tushib ketadi.",
        "d": "Kristall butun ekranni qoplab oladi.",
        "e": "O'yindagi hamma narsa muzlab qoladi.",
        "correct": "B",
        "topic": "15-dars: Kristall yig'ish",
        "expl": "Oltin kristallga tekkanda ballarimiz ko'payadi, tovush yangraydi va kristall yig'ib olinadi."
    },
    {
        "text": "16-darsda Boss jangida 'Lazer Qalqoni' qahramonga qanday yordam beradi?",
        "a": "Bossni darhol yo'qotib yuboradi.",
        "b": "Qalqon yoqilgan paytda dushman hujumlari qahramonga zarar yetkaza olmaydi.",
        "c": "Qahramonni o'yindan chiqarib yuboradi.",
        "d": "Faqat o'yinda yutqazib bo'lgandan keyin ishlaydi.",
        "e": "Barcha to'plangan tangalarni o'chirib yuboradi.",
        "correct": "B",
        "topic": "16-dars: Qalqon himoyasi",
        "expl": "Lazer qalqoni o'yinchini dushmanning xavfli zarbalaridan vaqtinchalik himoya qilib turadi."
    },
    {
        "text": "4-hafta 15-darsda 'Dushman AI' qahramonni ko'rib qolsa nima qiladi?",
        "a": "O'yin maydonidan uchib ketadi.",
        "b": "Qahramonning orqasidan quva boshlaydi.",
        "c": "Barcha kristallarni yeb qo'yadi.",
        "d": "O'yinchiga salom deb yozadi.",
        "e": "Darhol o'zini o'zi yo'q qiladi.",
        "correct": "B",
        "topic": "15-dars (4-h): Dushman AI quvishi",
        "expl": "Dushman o'yinchini ko'rish doirasiga kirishi bilan uni quvishni boshlaydi."
    },
    {
        "text": "4-hafta 16-darsda o'zimiz yaratgan levelni do'stimiz ham o'ynashi uchun nima qilamiz?",
        "a": "Kompyuterni do'stimizning uyiga ko'tarib boramiz.",
        "b": "O'yinda chiqqan Level Kodini nusxalab do'stimizga jo'natamiz, u o'z o'yiniga joylaydi.",
        "c": "Faqat telefon bilan ekranni rasmga olamiz.",
        "d": "O'yin kodini butunlay o'chirib tashlaymiz.",
        "e": "Level kodini hech kimga berib bo'lmaydi.",
        "correct": "B",
        "topic": "16-dars (4-h): Level Kodi bilan ulashish",
        "expl": "Level kodi bu matn bo'lib, uni do'stimizga yuborsak, u o'z kompyuterida biz chizgan xaritani ochib o'ynay oladi."
    },
    {
        "text": "5-hafta 17-darsga ko'ra, quyidagi parollardan qaysi biri eng mustahkam va xavfsiz?",
        "a": "12345678",
        "b": "Target#2026!Kiber",
        "c": "parol123",
        "d": "admin",
        "e": "qwerty",
        "correct": "B",
        "topic": "17-dars (5-h): Xavfsiz parol",
        "expl": "Katta-kichik harflar, raqamlar va maxsus belgilar (#!) aralashgan uzun parol eng xavfsiz hisoblanadi."
    },
    {
        "text": "5-hafta 18-darsda o'rganilgan 'Fishing' (Phishing) aldovi nima?",
        "a": "Baliq ovi haqidagi qiziqarli o'yin.",
        "b": "Haqiqiy saytga o'xshatib yasalgan soxta havola orqali akkaunt va parollarni o'g'irlash usuli.",
        "c": "Kompyuterga yangi o'yin yuklash usuli.",
        "d": "Maktab veb-saytini chiroyli qilish dasturi.",
        "e": "Internet tezligini oshiruvchi sim.",
        "correct": "B",
        "topic": "18-dars (5-h): Fishing havolalar",
        "expl": "Fishing bu firibgarlarning soxta sayti bo'lib, ular parollarni bilib olishga urinadi."
    },
    {
        "text": "5-hafta 19-darsda 'Troyalik Ot' virusi bolalarning kompyuteriga qanday qilib tushib qoladi?",
        "a": "Faqat kompyuterni latta bilan tozalaganda.",
        "b": "'Tekin Robux', 'O'yin uchun cheat' yoki 'Tekin o'yin' niqobi ostidagi soxta fayllarni yuklaganda.",
        "c": "Faqat maktab kundaligi ochilganda.",
        "d": "Faqat rasm chizadigan dastur ochilganda.",
        "e": "Kompyuterga hech qachon virus tushmaydi.",
        "correct": "B",
        "topic": "19-dars (5-h): Troyan viruslari",
        "expl": "Troyan virusi o'zini yoqimli sovg'a yoki tekin o'yin deb ko'rsatib, kompyuterga yashirincha kirib oladi."
    },
    {
        "text": "6-hafta 20-darsda biz yasagan 'Cyber Shield' ilovasi nima ish qilar edi?",
        "a": "Faqat kompyuter o'yinlarini o'ynatar edi.",
        "b": "Chatdagi shubhali xabarlarni tekshirib, yolg'on va aldov bor joylarni qizil bilan ko'rsatar edi.",
        "c": "Uy vazifasini o'quvchi o'rniga ishlab berar edi.",
        "d": "Kompyuterdagi suratlarni o'chirib yuborar edi.",
        "e": "Faqat musiqa chalar edi.",
        "correct": "B",
        "topic": "20-dars (6-h): Cyber Shield ilovasi",
        "expl": "Cyber Shield chatdagi firibgarlik va shubhali havolalarni tekshirib, xavfdan ogohlantiradi."
    },
    {
        "text": "7-hafta 21-darsda nega internetda begona odamlarga uydan olingan suratlarni yubormaslik kerak?",
        "a": "Chunki suratlar xonadagi havoni sovutib qo'yishi mumkin.",
        "b": "Chunki suratlarda uyning qayerda joylashgani (GPS manzili) ko'rinib qolishi mumkin.",
        "c": "Chunki suratlar telefonni og'irlashtiradi.",
        "d": "Chunki telefon ekranining rangi o'chadi.",
        "e": "Suratlarda hech qanday xavf bo'lmaydi.",
        "correct": "B",
        "topic": "21-dars (7-h): Shaxsiy fotosuratlar va maxfiylik",
        "expl": "Suratlarda uyning manzili va shaxsiy ma'lumotlar fosh bo'lmasligi uchun ularni begonalarga yubormaslik kerak."
    },
    {
        "text": "8-hafta 22-darsdagi 'Katta Ekran Qoidasi' (Billboard Rule) nima haqida?",
        "a": "Katta televizor sotib olish haqida.",
        "b": "Katta ko'cha ekraniga osishga uyaladigan shaxsiy rasm yoki gaplarni internetga ham aslo qo'ymaslik haqida.",
        "c": "O'yinlarni faqat kinoteatrda ko'rish haqida.",
        "d": "Telefon ekranini qorong'i qilish haqida.",
        "e": "Kompyuter ekranini pardalar bilan to'sish haqida.",
        "correct": "B",
        "topic": "22-dars (8-h): Katta Ekran Qoidasi",
        "expl": "Internet ommaviy joy. Butun shahar ko'rishini istamaydigan shaxsiy narsalaringizni internetga joylamang."
    },
    {
        "text": "Vibecoding darslarida o'rganilgan eng muhim qoida qaysi?",
        "a": "Boshqalarning o'yinini o'g'irlab, o'zimniki deb aytish.",
        "b": "Sun'iy intellektdan unumli foydalanib o'z o'yinlarimizni yaratish va kiber-xavfsizlik qoidalariga doimo amal qilish.",
        "c": "Kun bo'yi faqat o'yin o'ynash.",
        "d": "Notanish odamlar yuborgan har qanday havolani tekshirmasdan bosish.",
        "e": "Parollarni hamma do'stlarga tarqatish.",
        "correct": "B",
        "topic": "Xulosa: Yosh Vibecoder qoidasi",
        "expl": "Vibecoder — texnologiyalar yordamida yangi foydali o'yinlar yaratadigan va xavfsizlikka doim amal qiladigan ijodkordir."
    }
]

QUESTIONS_5_6_RU = [
    {
        "text": "Согласно Уроку 1, что такое Искусственный Интеллект (ИИ) и как он нам помогает?",
        "a": "Это живое существо, как человек, которое само кушает.",
        "b": "Это умная компьютерная программа, которая помогает нам писать тексты, рисовать и создавать игры.",
        "c": "Это вредоносный вирус, ломающий компьютер.",
        "d": "Это провод, который только заряжает аккумулятор телефона.",
        "e": "Это обычные простые часы на стене.",
        "correct": "B",
        "topic": "Урок 01: Что такое ИИ",
        "expl": "ИИ — это умный цифровой помощник, помогающий создавать новые игры и генерировать идеи."
    },
    {
        "text": "Что нужно сделать на Уроке 2 в промпте, чтобы задать характер игровому персонажу (NPC)?",
        "a": "Нужно просто выключить монитор компьютера.",
        "b": "В промпте нужно четко описать его имя, профессию, настроение (веселый или храбрый) и его цель.",
        "c": "Достаточно отправить одну точку.",
        "d": "Нужно выдернуть шнур клавиатуры.",
        "e": "Нужно заставить персонажа называть только цифры.",
        "correct": "B",
        "topic": "Урок 02: Персонажи NPC с характером",
        "expl": "Чем понятнее описан характер персонажа в промпте, тем живее и интереснее он общается в игре."
    },
    {
        "text": "Что такое 'Game Lore' (Лор и предыстория игры) из Урока 3?",
        "a": "Способ мгновенно стереть игру с диска.",
        "b": "Увлекательная история игрового мира, тайна главного героя и смысл его приключений.",
        "c": "Исключительно способ ускорения мышки.",
        "d": "Правило использовать в игре только один цвет.",
        "e": "Способ отключить интернет игроку.",
        "correct": "B",
        "topic": "Урок 03: Game Lore и история мира",
        "expl": "Game Lore — это сказочная предыстория игры, делающая прохождение интересным и захватывающим."
    },
    {
        "text": "Какой стиль можно выбрать на Уроке 4 при генерации концепт-арта (Concept Art) для игры?",
        "a": "Только стиль чистого белого листа.",
        "b": "Стили Pixel Art, Киберпанк, 3D мультфильм или Аниме.",
        "c": "Только полностью невидимый прозрачный стиль.",
        "d": "Стиль размытых черных клякс.",
        "e": "Никакой стиль выбрать невозможно.",
        "correct": "B",
        "topic": "Урок 04: Стили концепт-арта",
        "expl": "С помощью таких стилей, как Pixel Art или 3D мультфильм, мы создаем красивые изображения для игры."
    },
    {
        "text": "По какому признаку на Уроке 5 можно разоблачить 'Дипфейк' (картинку, нарисованную нейросетью)?",
        "a": "По названию файла фотографии.",
        "b": "По странному количеству пальцев на руках (например, 6 пальцев) или неестественным бликам в глазах.",
        "c": "По тому, что небо на картинке голубого цвета.",
        "d": "По тому, что на картинке нарисована машина.",
        "e": "По тому, что картинка очень четкая.",
        "correct": "B",
        "topic": "Урок 05: Признаки дипфейка",
        "expl": "ИИ иногда ошибается при рисовании пальцев рук или зрачков, и такие неточности легко заметить."
    },
    {
        "text": "О чем рассказывают ребята во время презентации на 'Demo Day' (Урок 6)?",
        "a": "О том, что они кушали сегодня на завтрак.",
        "b": "О названии своей игры, о том, что в ней нужно делать и какая миссия у главного героя.",
        "c": "Только о количестве кнопок на клавиатуре.",
        "d": "О стоимости монитора компьютера.",
        "e": "Они просто молчат и ничего не говорят.",
        "correct": "B",
        "topic": "Урок 06: Презентация Game Pitch",
        "expl": "На Demo Day каждый ученик с гордостью показывает свою созданную игру одноклассникам."
    },
    {
        "text": "Из чего состоят 3D модели в компьютере, которые мы изучали на Уроке 7?",
        "a": "Исключительно из капель воды.",
        "b": "Из полигональной сетки (Mesh) — набора точек, граней и геометрических фигур.",
        "c": "Только из бумажных страниц тетради.",
        "d": "Исключительно из наушников.",
        "e": "Только из электрических проводов.",
        "correct": "B",
        "topic": "Урок 07: 3D Модели и сетка Mesh",
        "expl": "Трехмерные игровые персонажи строятся из точек и граней (сетки Mesh), образующих форму тела."
    },
    {
        "text": "Что размещается на карте уровня (Level Design) на Уроке 8, чтобы игроку было интересно играть?",
        "a": "Только пустой черный экран.",
        "b": "Платформы для прыжков, собираемые золотые монетки и опасные препятствия.",
        "c": "Драйверы компьютера.",
        "d": "Только список цифр.",
        "e": "Только правила школы.",
        "correct": "B",
        "topic": "Урок 08: Элементы дизайна уровня",
        "expl": "Левел-дизайнер размещает дорожки для прыжков, награды и препятствия, чтобы игра была увлекательной."
    },
    {
        "text": "Что такое звуковые эффекты SFX (Sound Effects) в играх (Урок 9)?",
        "a": "Звук выключения компьютера.",
        "b": "Короткие веселые звуки действий: прыжок героя, звон собранной монетки или звук касания ловушки.",
        "c": "Только голос диктора в новостях.",
        "d": "Шум вентилятора внутри ноутбука.",
        "e": "Звук подключения зарядного устройства.",
        "correct": "B",
        "topic": "Урок 09: Звуковые эффекты SFX",
        "expl": "SFX — это звуки событий в игре (прыжки, монетка 'дзынь'), делающие игру динамичной."
    },
    {
        "text": "Что происходит на Уроке 10 в диалоге с NPC, если выбрать другой вариант ответа?",
        "a": "Игра сразу же стирается с компьютера.",
        "b": "Персонаж отвечает по-другому, и открывается новое интересное задание (квест).",
        "c": "Экран монитора полностью темнеет.",
        "d": "Все набранные очки исчезают.",
        "e": "Вообще ничего не меняется.",
        "correct": "B",
        "topic": "Урок 10: Умные диалоги NPC",
        "expl": "Умные персонажи реагируют на ответы игрока и могут выдать новый квест или награду."
    },
    {
        "text": "Что обычно отображается на панели HUD в верхней части экрана (Урок 11)?",
        "a": "Только прогноз погоды.",
        "b": "Жизни героя (сердечки HP), количество собранных монеток и время игры.",
        "c": "Только реклама из магазинов.",
        "d": "Рисунок жесткого диска компьютера.",
        "e": "Фотография здания школы.",
        "correct": "B",
        "topic": "Урок 11: Панель HUD",
        "expl": "Панель HUD всегда показывает игроку, сколько жизней (HP) и кристаллов у него осталось."
    },
    {
        "text": "Чем занимаются ученики на марафоне 'Game Jam' (Урок 12)?",
        "a": "Спят целый день на уроке.",
        "b": "За короткое время создают свою собственную маленькую работающую игру.",
        "c": "Раскрашивают кнопки клавиатуры красками.",
        "d": "Просто смотрят видеоролики в интернете.",
        "e": "Прячут мышки других учеников в классе.",
        "correct": "B",
        "topic": "Урок 12: Марафон Game Jam",
        "expl": "Game Jam — это марафон, на котором ребята за короткий срок пробуют собрать свою игру."
    },
    {
        "text": "Какую работу выполняет игровой цикл 'Game Loop' (Урок 13)?",
        "a": "Закрывает игру сразу после запуска.",
        "b": "Постоянно проверяет, куда движется герой, и плавно обновляет картинку на экране.",
        "c": "Только выключает монитор компьютера.",
        "d": "Сбрасывает все очки до нуля.",
        "e": "Работает только тогда, когда игра уже закрыта.",
        "correct": "B",
        "topic": "Урок 13: Игровой цикл Game Loop",
        "expl": "Game Loop непрерывно опрашивает клавиши управления и двигает героя по экрану."
    },
    {
        "text": "Что происходит на Уроке 14, когда персонаж задевает острые шипы или лазер?",
        "a": "Количество жизней героя резко возрастает до 1000.",
        "b": "Персонаж теряет одну жизнь (одно сердечко HP).",
        "c": "Игра автоматически объявляется выигранной.",
        "d": "Компьютер полностью выключается.",
        "e": "Игра замедляется в 100 раз.",
        "correct": "B",
        "topic": "Урок 14: Препятствия и потеря HP",
        "expl": "При касании шипов отнимается жизнь; если все сердечки закончились, уровень начинается заново."
    },
    {
        "text": "Что происходит на Уроке 15, когда герой добегает до сверкающего золотого кристалла?",
        "a": "Игра зависает.",
        "b": "Начисляются очки, звучит приятный звук, и кристалл забирается с карты.",
        "c": "Персонаж проваливается сквозь землю.",
        "d": "Кристалл закрывает собой весь экран.",
        "e": "Все объекты в игре замерзают.",
        "correct": "B",
        "topic": "Урок 15: Сбор кристаллов",
        "expl": "Сбор кристалла увеличивает наш счет, звучит звуковой эффект, а кристалл исчезает."
    },
    {
        "text": "Как 'Лазерный Щит' помогает герою во время битвы с Боссом (Урок 16)?",
        "a": "Сразу же уничтожает Босса.",
        "b": "Пока щит включен, атаки и выстрелы врагов не наносят герою никакого урона.",
        "c": "Выбрасывает героя из игры.",
        "d": "Срабатывает только после полного проигрыша.",
        "e": "Удаляет все собранные монетки.",
        "correct": "B",
        "topic": "Урок 16: Лазерный щит",
        "expl": "Щит дает герою временную защиту, спасая от опасных лазерных залпов босса."
    },
    {
        "text": "Что делает 'ИИ врага' на Уроке 15 (4-я неделя), когда замечает приближение героя?",
        "a": "Улетает за пределы игрового поля.",
        "b": "Начинает бежать и преследовать героя.",
        "c": "Съедает все кристаллы на уровне.",
        "d": "Пишет игроку приветствие в чат.",
        "e": "Моментально взрывается сам по себе.",
        "correct": "B",
        "topic": "Урок 15 (4-нед): Погоня врагов",
        "expl": "Как только герой заходит в зону видимости врага, тот сразу начинает погоню."
    },
    {
        "text": "Что нужно сделать, чтобы друг тоже смог поиграть на карте, которую мы создали в редакторе (Урок 16)?",
        "a": "Принести системный блок к другу домой.",
        "b": "Скопировать полученный в редакторе Код Уровня и отправить другу в сообщении.",
        "c": "Сфотографировать экран телефоном.",
        "d": "Полностью стереть весь код игры.",
        "e": "Созданную карту вообще никому нельзя передать.",
        "correct": "B",
        "topic": "Урок 16 (4-нед): Передача Кода Уровня",
        "expl": "Код уровня — это текст; если отправить его другу, он сможет загрузить именно нашу карту."
    },
    {
        "text": "Какой из следующих паролей является самым надежным и безопасным (Урок 17, 5-я неделя)?",
        "a": "12345678",
        "b": "Target#2026!Kiber",
        "c": "parol123",
        "d": "admin",
        "e": "qwerty",
        "correct": "B",
        "topic": "Урок 17 (5-нед): Надежный пароль",
        "expl": "Длинный пароль с большими и маленькими буквами, цифрами и спецсимволами (#!) сложнее всего взломать."
    },
    {
        "text": "Что такое 'Фишинг' (Phishing), о котором мы говорили на Уроке 18 (5-я неделя)?",
        "a": "Компьютерная игра про рыбалку.",
        "b": "Поддельная ссылка, похожая на настоящий сайт, созданная мошенниками для кражи паролей.",
        "c": "Способ бесплатно скачать новую игру.",
        "d": "Программа для украшения сайта школы.",
        "e": "Провод для ускорения интернета.",
        "correct": "B",
        "topic": "Урок 18 (5-нед): Фишинговые ссылки",
        "expl": "Фишинг — это ловушка мошенников, маскирующаяся под сайт игры, чтобы выманить пароль."
    },
    {
        "text": "Как вирус 'Троянский Конь' чаще всего попадает на компьютеры (Урок 19, 5-я неделя)?",
        "a": "Только во время протирки клавиатуры салфеткой.",
        "b": "Под видом 'бесплатных робуксов', 'читов для игры' или 'бесплатной игры' с сомнительных сайтов.",
        "c": "Только при открытии школьного электронного дневника.",
        "d": "Исключительно в программе для рисования.",
        "e": "На компьютеры вирусы вообще никогда не попадают.",
        "correct": "B",
        "topic": "Урок 19 (5-нед): Троянские программы",
        "expl": "Троян притворяется заманчивым бесплатным подарком, но на деле вредит компьютеру."
    },
    {
        "text": "Какую полезную задачу выполняло приложение 'Cyber Shield', собранное нами на Уроке 20?",
        "a": "Оно только запускало игры.",
        "b": "Оно проверяло сообщения чата и подсвечивало красным цветом опасные ссылки и обман.",
        "c": "Оно решало домашнее задание за учеников.",
        "d": "Оно стирало фотографии с компьютера.",
        "e": "Оно только проигрывало музыку.",
        "correct": "B",
        "topic": "Урок 20 (6-нед): Приложение Cyber Shield",
        "expl": "Cyber Shield анализирует текст в чатах и вовремя предупреждает об уловках мошенников."
    },
    {
        "text": "Почему на Уроке 21 не рекомендуется пересылать незнакомым людям фотографии, сделанные дома?",
        "a": "Потому что фотографии могут остудить воздух в комнате.",
        "b": "Потому что в свойствах фото могут сохраниться координаты и адрес вашего дома (GPS).",
        "c": "Потому что телефон от этого станет тяжелым.",
        "d": "Потому что экран телефона станет бледным.",
        "e": "В фотографиях нет никакой опасности.",
        "correct": "B",
        "topic": "Урок 21 (7-нед): Приватность домашних фото",
        "expl": "Фотографии могут раскрыть точное местоположение дома, поэтому не стоит отправлять их посторонним."
    },
    {
        "text": "О чем предупреждает 'Правило Большого Экрана' (Billboard Rule) из Урока 22 (8-я неделя)?",
        "a": "О том, что нужно купить огромный телевизор.",
        "b": "О том, что нельзя выкладывать в интернет то, что постеснялся бы показать на огромном экране посреди города.",
        "c": "О том, что фильмы нужно смотреть только в кинотеатре.",
        "d": "О том, что нужно сделать экран телефона темным.",
        "e": "О том, что монитор нужно закрывать шторами.",
        "correct": "B",
        "topic": "Урок 22 (8-нед): Правило Большого Экрана",
        "expl": "Интернет публичен: то, что вы не готовы показать всему городу на билборде, нельзя выкладывать в сеть."
    },
    {
        "text": "Какое самое главное правило отличает настоящего юного разработчика (Vibecoder)?",
        "a": "Копировать чужие игры и говорить, что сделал сам.",
        "b": "Умно использовать ИИ для создания полезных игр и всегда соблюдать правила безопасности в интернете.",
        "c": "Играть в компьютерные игры сутки напролет.",
        "d": "Нажимать на любые незнакомые ссылки от чужих людей.",
        "e": "Раздавать свои пароли всем знакомым.",
        "correct": "B",
        "topic": "Итог: Правило юного Vibecoder",
        "expl": "Vibecoder создает классные проекты с помощью технологий и бережет свою цифровую безопасность."
    }
]

print("Grade 5-6 Vibecoding test data loaded (Steady Easy). Teacher: Ismoiljon Usmonov.")
