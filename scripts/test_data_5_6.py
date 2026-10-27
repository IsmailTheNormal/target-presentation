#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
5–6-Sinf: 25 Savolli Kiberxavfsizlik va Kiber-Gigiyena Testi
Uzbek va Russian variantlari (5 ta variant: A, B, C, D, E)
"""

META_5_6_UZ = {
    "school_name": "TARGET INTERNATIONAL SCHOOL — YUNUSOBOD",
    "exam_title": "5–6-SINF: KIBERXAVFSIZLIK VA RAQAMLI GIGIENA",
    "track_title": "Junior Creators & Cyber Security Track",
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

KEYS_META_5_6_UZ = {
    "heading": "JAVOBLAR KALITI VA BAHOLASH MEZONI",
    "subheading": "O'qituvchi uchun rasmiy tekshirish kaliti (5–6-sinf, 25 ta savol)",
    "table_headers": ["№", "Kalit", "Mavzu / Kompetensiya", "Izoh va Tushuntirish"],
    "scale_heading": "Rasmiy 25 Ballik Baholash Shkalasi:",
    "rubric_tiers": [
        {"grade": "A'lo (5)", "range": "22 – 25 ball", "desc": "Mukammal kiber-gigiyena va raqamli madaniyat"},
        {"grade": "Yaxshi (4)", "range": "18 – 21 ball", "desc": "Asosiy qoidalar yaxshi o'zlashtirilgan"},
        {"grade": "Qoniqarli (3)", "range": "13 – 17 ball", "desc": "Ayrim xavfsizlik tushunchalari takrorlanishi zarur"},
        {"grade": "Qoniqarsiz (2)", "range": "0 – 12 ball", "desc": "Kiberxavfsizlik asoslari qayta o'rganilishi lozim"}
    ]
}

META_5_6_RU = {
    "school_name": "TARGET INTERNATIONAL SCHOOL — ЮНУСАБАД",
    "exam_title": "5–6 КЛАСС: КИБЕРБЕЗОПАСНОСТЬ И ЦИФРОВАЯ ГИГИЕНА",
    "track_title": "Junior Creators & Cyber Security Track",
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

KEYS_META_5_6_RU = {
    "heading": "КЛЮЧИ ОТВЕТОВ И КРИТЕРИИ ОЦЕНИВАНИЯ",
    "subheading": "Официальный ключ проверки для учителя (5–6 класс, 25 вопросов)",
    "table_headers": ["№", "Ключ", "Тема / Компетенция", "Пояснение и разбор ответа"],
    "scale_heading": "Официальная 25-балльная шкала оценивания:",
    "rubric_tiers": [
        {"grade": "Отлично (5)", "range": "22 – 25 баллов", "desc": "Безупречная кибергигиена и цифровая грамотность"},
        {"grade": "Хорошо (4)", "range": "18 – 21 балл", "desc": "Ключевые правила надежно усвоены"},
        {"grade": "Удовл. (3)", "range": "13 – 17 баллов", "desc": "Требуется повторение отдельных правил безопасности"},
        {"grade": "Неудовл. (2)", "range": "0 – 12 баллов", "desc": "Необходимо заново пройти курс кибергигиены"}
    ]
}

QUESTIONS_5_6_UZ = [
    {
        "text": "Quyidagilardan qaysi biri eng mustahkam va kiber-xavfsiz parol hisoblanadi?",
        "a": "12345678",
        "b": "azamat2012",
        "c": "Target#2026!Kiber",
        "d": "qwertyuiop",
        "e": "parol12345",
        "correct": "C",
        "topic": "Kuchli Parollar",
        "expl": "Mustahkam parol kamida 8-12 belgidan iborat bo'lib, katta-kichik harflar, raqamlar va maxsus belgilarni (!#$) o'z ichiga olishi shart."
    },
    {
        "text": "Nima uchun shaxsiy parollarni hatto eng yaqin sinfdoshingizga ham aytmaslik kerak?",
        "a": "Chunki ular parolni adashib unutib qo'yishi mumkin.",
        "b": "Parol shaxsiy hisobingiz kaliti bo'lib, birov bilsa siz nomingizdan noo'rin xabarlar yuborishi mumkin.",
        "c": "Chunki maktabda parollarni aytish dars qoidasiga zid.",
        "d": "Parolni boshqalar bilsa telefonning xotirasi to'lib qoladi.",
        "e": "Faqat o'qituvchi ruxsat berganida aytish mumkin.",
        "correct": "B",
        "topic": "Parol Maxfiyligi",
        "expl": "Hisob xavfsizligida parol faqat egasiga tegishli shaxsiy sir hisoblanadi."
    },
    {
        "text": "Internetdagi 'Fishing' (Phishing) kiber-hujumi deganda nima tushuniladi?",
        "a": "Kompyuter ekranida baliq ovlash haqidagi video o'yin.",
        "b": "Foydalanuvchini aldab, soxta saytlar orqali uning paroli yoki bank kartasi ma'lumotlarini o'g'irlash.",
        "c": "Kompyuter tezligini ikki barobar oshiruvchi yangilanish dasturi.",
        "d": "Internet simining suv ostidan o'tkazilishi.",
        "e": "Faqat antivirus dasturlari yuboradigan rasmiy xabar.",
        "correct": "B",
        "topic": "Fishing Hujumlari",
        "expl": "Fishing (qarmakka ilintirish) — bu soxta havolalar va xabarlar yordamida parollarni o'g'irlash usuli."
    },
    {
        "text": "Chatda notanish kimsa sizga: 'Ushbu havola orqali kirsangiz, o'yiningizga 1000 ta bepul Robux tushadi' deb xabar yuborsa, nima qilish kerak?",
        "a": "Darhol havolaga kirib, o'yin login va parolini kiritish kerak.",
        "b": "Xabarni butun sinf guruhiga yuborib tarqatish kerak.",
        "c": "Havolani ochmaslik, bu firibgarlik ekanini bilish va xabarni o'chirib yuborish kerak.",
        "d": "O'sha odamga yana 5000 ta berishini so'rab yozish kerak.",
        "e": "Telefonni zaryadga qo'yib, 1 soatdan keyin kirish kerak.",
        "correct": "C",
        "topic": "O'yin Aldovlari",
        "expl": "Hech kim begonalarga tekin tanga bermaydi. Bu odatda hisobni o'g'irlash uchun tuzoqdir."
    },
    {
        "text": "Brauzerda veb-saytning xavfsiz va shifrlangan ekanligini qaysi belgi bildiradi?",
        "a": "Sayt manzilining qizil rangda yozilishi",
        "b": "Manzil satrida yopiq qulf belgisi va 'https://' protokoli bo'lishi",
        "c": "Sahifada ko'plab miltillovchi yorqin reklamalar bo'lishi",
        "d": "Sayt nomida faqat raqamlar qatnashishi",
        "e": "Saytning juda sekin yuklanishi",
        "correct": "B",
        "topic": "Xavfsiz Protokol",
        "expl": "HTTPS va qulf belgisi brauzer bilan server orasidagi ma'lumotlar shifrlanganini ko'rsatadi."
    },
    {
        "text": "Kompyuter virusi aslida nima?",
        "a": "Kompyuter klaviaturasiga tushgan chang va mikroblar.",
        "b": "Fayllarni buzish, o'chirish yoki o'g'irlash uchun yovuz niyatda yozilgan zararli dastur.",
        "c": "Monitor ekranining charchab qolishi.",
        "d": "Kompyuter o'yinining eng qiyin bosqichi.",
        "e": "Internet provayderining maxsus tezlik o'lchagichi.",
        "correct": "B",
        "topic": "Viruslar Tabiyati",
        "expl": "Virus — bu ruxsatsiz kompyuterga kirib, zarar yetkazuvchi yashirin dastur kodi."
    },
    {
        "text": "Qadimgi afsona nomi bilan ataluvchi 'Troyan oti' (Trojan Horse) qanday zararli dastur?",
        "a": "Faqat otlar haqidagi o'yinlarda uchraydigan qahramon.",
        "b": "Foydali o'yin yoki dastur niqobi ostida kompyuterga kirib, yashirincha ma'lumotlarni o'g'irlovchi dastur.",
        "c": "Kompyuterni viruslardan tozalovchi eng kuchli dastur.",
        "d": "Faqat sichqoncha ishlamay qolganda paydo bo'ladigan xato.",
        "e": "Internet tezligini oshiruvchi bepul ilova.",
        "correct": "B",
        "topic": "Troyan Dasturlari",
        "expl": "Troyan dasturi foydalanuvchini aldaydi: o'zini qiziqarli o'yin deb ko'rsatib, orqa fonda xakerga yo'l ochadi."
    },
    {
        "text": "Elektron pochtangizga notanish kimsadan 'super_sovga.exe' nomli fayl kelsa, nima qilish kerak?",
        "a": "Faylni darhol ochib, sovg'ani qabul qilish kerak.",
        "b": "Faylni ochmasdan o'chirib tashlash va antivirus bilan skaner qilish kerak.",
        "c": "Uni barcha do'stlarga yuborish kerak.",
        "d": "Fayl nomini o'zgartirib keyin ochish kerak.",
        "e": "Kompyuterni o'chirib, 1 kundan keyin ochish kerak.",
        "correct": "B",
        "topic": "Zararli Fayllar",
        "expl": "Notanish .exe (bajariluvchi) fayllar deyarli har doim virus yoki troyan bo'ladi."
    },
    {
        "text": "Insonning 'Raqamli izi' (Digital Footprint) deganda nima tushuniladi?",
        "a": "Smartfon ekranida barmoqdan qolgan haqiqiy yog'li izlar.",
        "b": "Internetda qoldirgan barcha ma'lumotlar: saytlar tarixi, layklar, izohlar va rasmlar.",
        "c": "Kompyuter sichqonchasi tagidagi rezina gilamcha.",
        "d": "Faqat kompyuter o'chirilganda paydo bo'ladigan qora ekran.",
        "e": "Internet kabelining devordagi uzunligi.",
        "correct": "B",
        "topic": "Raqamli Iz",
        "expl": "Raqamli iz — insonning internetdagi barcha faoliyati yig'indisi bo'lib, u yillab saqlanib qolishi mumkin."
    },
    {
        "text": "Ijtimoiy tarmoqlardagi ochiq profilingizga qaysi ma'lumotni joylashtirish eng xavfli hisoblanadi?",
        "a": "Sevimli kitobingiz yoki filmingiz nomi",
        "b": "Uy manzilingiz, telefon raqamingiz va ota-onangiz ish joyi",
        "c": "Chizgan rasmingiz yoki maktab formangizdagi nishon",
        "d": "Futbol komandangiz nomi",
        "e": "Sevimli taomingiz surati",
        "correct": "B",
        "topic": "Shaxsiy Maxfiylik",
        "expl": "Uy manzili va telefon o'g'rilar hamda kiber-jinoyatchilar uchun to'g'ridan-to'g'ri nishon bo'lishi mumkin."
    },
    {
        "text": "Smartfonda olingan fotosuratlarda qanday yashirin ma'lumot (EXIF) saqlanib, joylashuvingizni fosh qilishi mumkin?",
        "a": "Batareya quvvati foizi",
        "b": "Aniq GPS geolokatsiya koordinatalari (uyingizning xaritadagi nuqtasi)",
        "c": "Telefoningizning rangi",
        "d": "Xonadagi musiqa ovozi",
        "e": "Telefon egasining qon bosimi",
        "correct": "B",
        "topic": "EXIF Geolokatsiya",
        "expl": "Fotosuratlarda yashirin GPS koordinatalari saqlanadi. Uni begonalarga yuborish uyingiz manzilini ko'rsatib qo'yishi mumkin."
    },
    {
        "text": "'Katta Ekran Qoidasi' (Billboard Rule) nimani anglatadi?",
        "a": "Kinoteatrda film ko'rayotganda telefonni o'chirib qo'yish kerakligini.",
        "b": "Internetga faqat butun shahar ko'rsa ham uyalmaydigan narsalarni joylashtirish kerakligini.",
        "c": "Katta televizorda faqat dars qilish kerakligini.",
        "d": "Kompyuter ekranini haftada bir marta tozalash lozimligini.",
        "e": "Internetga xohlagan narsani yashirincha qo'yish mumkinligini.",
        "correct": "B",
        "topic": "Katta Ekran Qoidasi",
        "expl": "Internetga joylangan narsa abadiy qolishi mumkin, shuning uchun shaxsiy narsalarni ommaga chiqarmaslik lozim."
    },
    {
        "text": "Kafelar yoki parklardagi ochiq (parolsiz) tekin Wi-Fi tarmoqlarida nima qilish xavfli?",
        "a": "Ob-havo ma'lumotlarini tekshirish",
        "b": "Bank kartasi orqali xarid qilish va shaxsiy parollarni kiritish",
        "c": "Elektron soatni to'g'rilash",
        "d": "Matnli kitob o'qish",
        "e": "Kalkulyatorda hisoblash",
        "correct": "B",
        "topic": "Ochiq Wi-Fi Xavfi",
        "expl": "Ochiq Wi-Fi tarmog'idagi barcha parollarni bitta tarmoqda o'tirgan xaker maxsus dastur bilan ushlab olishi mumkin."
    },
    {
        "text": "Kompyuterdagi Antivirus dasturining asosiy vazifasi nima?",
        "a": "Kompyuterda yangi multfilmlar chizish.",
        "b": "Zararli dasturlarni aniqlash, bloklash va ularni yo'q qilish.",
        "c": "Faqat kompyuter o'yinlarini tezroq o'ynash.",
        "d": "Klaviatura tugmalarini o'rgatish.",
        "e": "Internet kabelining uzilishini ta'mirlash.",
        "correct": "B",
        "topic": "Antivirus Tizimlari",
        "expl": "Antivirus doimiy ravishda xotira va fayllarni tekshirib, xavflarni bartaraf etadi."
    },
    {
        "text": "Noutbuk kamerasining yonidagi kichik yashil yoki oq chiroq to'satdan yonib qolsa, bu nimani bildiradi?",
        "a": "Kompyuterning zaryadi 100% to'lganini.",
        "b": "Kamera hozirda faol ishlayotgani va kimdir video yozayotganini.",
        "c": "Xonadagi chiroq yetarli emasligini.",
        "d": "Monitor ekranining muzlab qolganini.",
        "e": "Internet tarmog'i uzilganini.",
        "correct": "B",
        "topic": "Kamera Xavfsizligi",
        "expl": "Kamera indikatori yonsa, dastur video olyapti degani. Agar siz kamerani yoqmagan bo'lsangiz, troyan ishlayotgan bo'lishi mumkin."
    },
    {
        "text": "Internetda kimdir sizga qo'pol so'zlar yozib kamsitsa (kiber-bulling), eng to'g'ri harakat qaysi?",
        "a": "Unga javoban undan ham battar yomon so'zlar bilan haqorat qilish.",
        "b": "Dalil sifatida skrinshot olib, uni bloklash va ota-onangiz yoki o'qituvchingizga aytish.",
        "c": "Kompyuterni derazadan uloqtirib yuborish.",
        "d": "Hamma parollaringizni unga berib qochish.",
        "e": "Hech kimga aytmasdan o'zingiz yig'lab o'tirish.",
        "correct": "B",
        "topic": "Kiber-Bulling",
        "expl": "Kiber-tajovuzkorga javob qaytarmaslik, skrinshot olib bloklash va kattalardan yordam so'rash to'g'ri yo'ldir."
    },
    {
        "text": "Ijtimoiy muhandislik: Notanish odam 'Men Roblox adminiman, parolingizni tekshirib beraman' desa, nima qilish kerak?",
        "a": "Darhol parolni yozib yuborish kerak.",
        "b": "Haqiqiy adminlar hech qachon foydalanuvchidan parolini so'ramasligini bilib, uni bloklash kerak.",
        "c": "Parol bilan birga telefon raqamni ham yuborish kerak.",
        "d": "Do'stingizning parolini berib ko'rish kerak.",
        "e": "Unga yangi o'yin kashf qilishni taklif qilish kerak.",
        "correct": "B",
        "topic": "Ijtimoiy Muhandislik",
        "expl": "Rasmiy adminlar parolni hech qachon so'ramaydi. Parol so'ragan shaxs 100% firibgardir."
    },
    {
        "text": "Ikki bosqichli autentifikatsiya (2FA) ning foydasi nimada?",
        "a": "Internet tezligini ikki marta tezlashtiradi.",
        "b": "Parol o'g'irlangan taqdirda ham, telefoningizga keladigan ikkinchi kodsiz hisobingizga kirishga yo'l qo'ymaydi.",
        "c": "Kompyuterni har kuni o'zi tozalab turadi.",
        "d": "Ekranning yorug'ligini avtomatik oshiradi.",
        "e": "Barcha o'yinlarni tekin qilib beradi.",
        "correct": "B",
        "topic": "2FA Himoyasi",
        "expl": "2FA (parol + SMS yoki ilova kodi) hisobingizni begona shaxslar ochishidan to'liq asraydi."
    },
    {
        "text": "Ekranda to'satdan 'Siz 10 000 000 so'm yutdingiz! Yutuqni olish uchun kartangizni kiriting' degan oyna chiqsa nima qilasiz?",
        "a": "Xursand bo'lib plastik karta raqamini kiritasiz.",
        "b": "Bu klassik aldov ekanini bilib, oynani yopasiz va hech narsa kiritmaysiz.",
        "c": "Do'stlaringizning ham kartasini qo'shib yozasiz.",
        "d": "Kompaniyaga qo'ng'iroq qilib pulni naqd berishini so'raysiz.",
        "e": "Bankka borib navbatda turasiz.",
        "correct": "B",
        "topic": "Soxta Yutuqlar",
        "expl": "Hech qanday o'yinda qatnashmagan odam yutuq yutmaydi. Bu karta pullarini o'g'irlash usulidir."
    },
    {
        "text": "Maktabdagi umumiy kompyuterdan foydalangandan keyin eng muhim qoida qaysi?",
        "a": "Kompyuter monitorini o'chirib qo'yish.",
        "b": "Barcha ochilgan shaxsiy hisoblardan (Log Out / Chiqish) chiqib, brauzerni yopish.",
        "c": "Klaviatura ustiga daftar qo'yish.",
        "d": "Sichqonchani teskari aylantirib qo'yish.",
        "e": "O'rindiqni stol ostiga surib qo'yish.",
        "correct": "B",
        "topic": "Jamoat Kompyuteri",
        "expl": "Agar hisobingizdan chiqmasangiz, keyingi o'quvchi sizning nomingizdan harakat qilishi mumkin."
    },
    {
        "text": "Sinfda yoki yo'lakda begona USB fleshka topib olsangiz, eng to'g'ri harakat qaysi?",
        "a": "Qiziqib darhol o'z kompyuteringizga tiqib, ichidagi fayllarni ko'rish.",
        "b": "Fleshkaga zararli dastur yozilgan bo'lishi mumkinligi sababli uni kompyuterga tiqmasdan o'qituvchiga topshirish.",
        "c": "Uni barcha partadoshlarga tarqatish.",
        "d": "Ichiga yangi musiqa yozib olish.",
        "e": "Cho'ntakka solib uyga olib ketish.",
        "correct": "B",
        "topic": "USB Xavfsizligi",
        "expl": "Xakerlar maxsus virusli fleshkalarni ataylab tashlab ketishadi (Baiting). Uni kompyuterga tiqish butun tizimni buzishi mumkin."
    },
    {
        "text": "Nima uchun kompyuter va telefon operatsion tizimini muntazam yangilab (Update) turish kerak?",
        "a": "Faqat telefon korpusi yangiroq ko'rinishi uchun.",
        "b": "Kiber-jinoyatchilar topgan xavfli zaifliklarni bartaraf etish va tizim himoyasini kuchaytirish uchun.",
        "c": "Telefonning kamerasi kattalashishi uchun.",
        "d": "Ekranning oynasi sinmasligi uchun.",
        "e": "Internetdagi barcha o'yinlarni o'chirib yuborish uchun.",
        "correct": "B",
        "topic": "Tizim Yangilanishlari",
        "expl": "Yangilanishlar (patches) dasturchilar tomonidan aniqlangan kiber-teshiklarni yopadi."
    },
    {
        "text": "Kompyuterdagi muhim fayllarning 'Zaxira nusxasi' (Backup) nima uchun kerak?",
        "a": "Fayllar ko'proq joy egallashi uchun.",
        "b": "Kompyuter buzilsa yoki virus tushsa, muhim ma'lumotlarni yo'qotmasdan tiklash uchun.",
        "c": "Fayllarni internetga tekinga sotish uchun.",
        "d": "Kompyuterni har kuni format qilish uchun.",
        "e": "Monitor rangini yaxshilash uchun.",
        "correct": "B",
        "topic": "Zaxira Nusxalash",
        "expl": "Backup bo'lsa, har qanday virus yoki buzilishdan keyin barcha dars va fayllarni qaytarish mumkin."
    },
    {
        "text": "Do'stingiz o'yin hisobingizni bir kunga so'rab parolingizni berishingizni iltimos qilsa, nima qilish to'g'ri?",
        "a": "Darhol parolni berish, chunki u do'stingiz.",
        "b": "Hisob xavfsizligi qoidalariga ko'ra parollar hech kimga berilmasligini muloyimlik bilan tushuntirish.",
        "c": "Do'stingizga ota-onangizning bank kartasi rasmini yuborish.",
        "d": "Unga parolni o'rniga telefoningizni sovg'a qilib yuborish.",
        "e": "U bilan butunlay urishib qolish.",
        "correct": "B",
        "topic": "Parol Madaniyati",
        "expl": "Parolni berish hisobingiz o'g'irlanishiga yoki bloklanishiga sabab bo'ladi."
    },
    {
        "text": "Internetda shubhali xabarga duch kelsangiz yoki kiber-firibgarlik sezilsa, birinchi kimga murojaat qilish kerak?",
        "a": "Hech kimga aytmasdan kutib turish.",
        "b": "Ota-onangizga yoki informatika o'qituvchingizga xabar berish.",
        "c": "Internetdagi notanish guruhlarga yozish.",
        "d": "Kompyuterni qayta yoqib, o'yin o'ynashda davom etish.",
        "e": "Firibgarga barcha shaxsiy ma'lumotlarni yuborish.",
        "correct": "B",
        "topic": "Yordam So'rash",
        "expl": "Kattalar va o'qituvchilar kiber-xavfni tezda bartaraf etishga yordam beradi."
    }
]

QUESTIONS_5_6_RU = [
    {
        "text": "Какой из следующих паролей является наиболее надежным и безопасным?",
        "a": "12345678",
        "b": "azamat2012",
        "c": "Target#2026!Kiber",
        "d": "qwertyuiop",
        "e": "parol12345",
        "correct": "C",
        "topic": "Надежные Пароли",
        "expl": "Надежный пароль состоит минимум из 8-12 символов, содержит заглавные и строчные буквы, цифры и спецсимволы (!#$)."
    },
    {
        "text": "Почему нельзя сообщать свои личные пароли даже близкому однокласснику?",
        "a": "Потому что он может случайно забыть пароль.",
        "b": "Пароль — это ключ к аккаунту; узнав его, посторонний может отправлять сообщения от вашего имени.",
        "c": "Потому что в школе запрещено говорить вслух буквы.",
        "d": "Если кто-то узнает пароль, переполнится память телефона.",
        "e": "Пароль можно говорить только с разрешения дежурного.",
        "correct": "B",
        "topic": "Тайна Пароля",
        "expl": "Пароль является строгой личной тайной, обеспечивающей неприкосновенность вашего аккаунта."
    },
    {
        "text": "Что в кибербезопасности называется 'Фишингом' (Phishing)?",
        "a": "Компьютерная игра про рыбалку на озере.",
        "b": "Обман пользователей через поддельные сайты для кражи их паролей или данных банковских карт.",
        "c": "Программа для ускорения работы процессора.",
        "d": "Прокладка интернет-кабеля по дну океана.",
        "e": "Официальное уведомление антивируса об обновлении.",
        "correct": "B",
        "topic": "Фишинг",
        "expl": "Фишинг ('ловля на крючок') — метод кражи учетных данных с помощью поддельных ссылок."
    },
    {
        "text": "Если незнакомец в чате пишет: 'Перейди по ссылке и получи 1000 бесплатных робуксов (Robux)', как поступить?",
        "a": "Срочно перейти и ввести свой логин и пароль от игры.",
        "b": "Переслать ссылку во все школьные группы.",
        "c": "Не открывать ссылку, понять что это обман, удалить сообщение и заблокировать отправителя.",
        "d": "Попросить прислать 5000 робуксов вместо тысячи.",
        "e": "Поставить телефон на зарядку и войти через час.",
        "correct": "C",
        "topic": "Игровые Ловушки",
        "expl": "Бесплатной игровой валюты от незнакомцев не бывает. Это частый трюк для кражи аккаунтов."
    },
    {
        "text": "Какой значок в браузере указывает на безопасное и зашифрованное соединение с сайтом?",
        "a": "Красный цвет названия сайта",
        "b": "Значок закрытого замка в адресной строке и протокол 'https://'",
        "c": "Большое количество мигающих баннеров на странице",
        "d": "Наличие только цифр в названии сайта",
        "e": "Очень медленная загрузка страницы",
        "correct": "B",
        "topic": "Безопасный Протокол",
        "expl": "HTTPS и значок замка подтверждают шифрование данных между браузером и сайтом."
    },
    {
        "text": "Что представляет собой компьютерный вирус?",
        "a": "Пыль и бактерии на поверхности клавиатуры.",
        "b": "Вредоносная программа, созданная для повреждения файлов, кражи данных или слежки.",
        "c": "Усталость экрана после долгой работы.",
        "d": "Сложный финальный уровень в компьютерной игре.",
        "e": "Специальный измеритель скорости интернета от провайдера.",
        "correct": "B",
        "topic": "Природа Вирусов",
        "expl": "Вирус — это вредоносный код, тайно проникающий в систему для нанесения ущерба."
    },
    {
        "text": "Какой тип вредоносных программ называют 'Троянским конем' (Трояном)?",
        "a": "Персонаж из древней исторической стратегии.",
        "b": "Программу, маскирующуюся под полезную игру или утилиту, но тайно открывающую хакеру доступ к компьютеру.",
        "c": "Самый мощный антивирус для очистки диска.",
        "d": "Ошибку, возникающую только при поломке мыши.",
        "e": "Бесплатное приложение для раздачи интернета.",
        "correct": "B",
        "topic": "Троянские Программы",
        "expl": "Троян выдает себя за безвредную программу, но внутри скрывает вредоносный код."
    },
    {
        "text": "Если на почту от неизвестного адресата пришел файл с именем 'podarok.exe', что следует сделать?",
        "a": "Быстро открыть его, чтобы забрать подарок.",
        "b": "Ни в коем случае не открывать, удалить письмо и проверить систему антивирусом.",
        "c": "Переслать файл всем друзьям.",
        "d": "Переименовать файл и запустить его.",
        "e": "Выключить монитор на 24 часа.",
        "correct": "B",
        "topic": "Опасные Файлы",
        "expl": "Файлы с расширением .exe от незнакомцев практически всегда содержат вирусы."
    },
    {
        "text": "Что означает понятие 'Цифровой след' (Digital Footprint)?",
        "a": "Следы от пальцев на сенсорном экране смартфона.",
        "b": "Вся совокупность информации, оставленная вами в интернете: история поиска, посты, лайки и фото.",
        "c": "Резиновый коврик под компьютерной мышью.",
        "d": "Черный экран при выключении компьютера.",
        "e": "Длина интернет-кабеля в вашей комнате.",
        "correct": "B",
        "topic": "Цифровой След",
        "expl": "Цифровой след сохраняется на серверах годами и формирует вашу онлайн-репутацию."
    },
    {
        "text": "Какую информацию наиболее опасно публиковать в открытом профиле соцсетей?",
        "a": "Название любимой книги или мультфильма",
        "b": "Домашний адрес, личный номер телефона и распорядок дня семьи",
        "c": "Рисунок, нарисованный на уроке ИЗО",
        "d": "Название футбольного клуба, за который болеете",
        "e": "Фотографию любимого блюда",
        "correct": "B",
        "topic": "Приватность Данных",
        "expl": "Публикация адреса и телефона ставит под угрозу вашу физическую и цифровую безопасность."
    },
    {
        "text": "Какая скрытая информация (EXIF) в фотографиях со смартфона может выдать ваше местоположение?",
        "a": "Процент заряда аккумулятора телефона",
        "b": "Точные географические GPS-координаты места съемки",
        "c": "Цвет чехла смартфона",
        "d": "Громкость музыки в комнате",
        "e": "Модель наушников",
        "correct": "B",
        "topic": "Геолокация EXIF",
        "expl": "Метаданные EXIF в фото содержат точные координаты, раскрывая адрес вашего дома."
    },
    {
        "text": "В чем суть 'Правила большого экрана' (Billboard Rule)?",
        "a": "В кинотеатре нужно выключать звук телефона.",
        "b": "Публикуйте в сети только то, что вам не стыдно было бы показать на огромном рекламном щите в центре города.",
        "c": "Уроки нужно делать только перед большим телевизором.",
        "d": "Экран ноутбука нужно протирать раз в неделю.",
        "e": "В интернете можно тайно писать любые комментарии.",
        "correct": "B",
        "topic": "Правило Большого Экрана",
        "expl": "Информация из интернета не удаляется бесследно, поэтому публикуйте только безопасный контент."
    },
    {
        "text": "Что опасно делать при подключении к бесплатному открытому Wi-Fi в кафе или парке?",
        "a": "Читать онлайн-статью об истории",
        "b": "Вводить пароли от аккаунтов и совершать платежи банковской картой",
        "c": "Сверять время на электронных часах",
        "d": "Просматривать прогноз погоды",
        "e": "Считать на калькуляторе",
        "correct": "B",
        "topic": "Открытые Сети Wi-Fi",
        "expl": "В незащищенной сети злоумышленник может перехватить незашифрованные пароли и данные карт."
    },
    {
        "text": "Какова главная задача антивирусной программы?",
        "a": "Создавать новые компьютерные игры.",
        "b": "Обнаруживать, блокировать и удалять вредоносные программы.",
        "c": "Увеличивать скорость нажатия клавиш.",
        "d": "Рисовать красивые заставки на рабочий стол.",
        "e": "Чинить сломанный провод питания.",
        "correct": "B",
        "topic": "Антивирусная Защита",
        "expl": "Антивирус сканирует память и файлы, защищая систему от заражения."
    },
    {
        "text": "Если световой индикатор рядом с веб-камерой ноутбука внезапно загорелся сам по себе, это означает:",
        "a": "Ноутбук полностью зарядился до 100%.",
        "b": "Камера в данный момент включена и передает или записывает видео.",
        "c": "В комнате стало слишком темно.",
        "d": "Сломалась клавиша пробела.",
        "e": "Отключился роутер Wi-Fi.",
        "correct": "B",
        "topic": "Индикатор Камеры",
        "expl": "Светодиод камеры аппаратный. Если он горит без вашего ведома — возможно, активен вирус-шпион."
    },
    {
        "text": "Если кто-то в интернете грубит вам и пытается запугать (кибербуллинг), какое действие правильное?",
        "a": "Ответить еще более обидными и грубыми словами.",
        "b": "Сделать скриншот в качестве доказательства, заблокировать обидчика и рассказать родителям или учителю.",
        "c": "Выбросить ноутбук в окно.",
        "d": "Отдать обидчику все свои пароли.",
        "e": "Молча переживать в одиночестве.",
        "correct": "B",
        "topic": "Кибербуллинг",
        "expl": "Не вступайте в перепалку: зафиксируйте факт нарушения скриншотом и обратитесь к взрослым."
    },
    {
        "text": "Незнакомец пишет: 'Я администратор игры, дай свой пароль для проверки честности'. Ваши действия:",
        "a": "Немедленно отправить пароль.",
        "b": "Заблокировать его, помня, что настоящая администрация никогда не просит пароли пользователей.",
        "c": "Отправить пароль вместе с номером телефона.",
        "d": "Отправить пароль своего друга.",
        "e": "Предложить ему сыграть в шахматы.",
        "correct": "B",
        "topic": "Социальная Инженерия",
        "expl": "Администраторы сервисов видят данные в системе и никогда не спрашивают пароль в чате."
    },
    {
        "text": "В чем главное преимущество двухфакторной аутентификации (2FA)?",
        "a": "Она в два раза ускоряет работу интернета.",
        "b": "Даже если хакер узнает ваш пароль, он не сможет войти без второго одноразового кода из SMS или приложения.",
        "c": "Она автоматически удаляет спам с компьютера.",
        "d": "Она делает экран телефона ярче.",
        "e": "Она открывает все платные уровни в играх.",
        "correct": "B",
        "topic": "Двухфакторная Защита",
        "expl": "2FA создает второй барьер защиты: пароль плюс одноразовый временный код."
    },
    {
        "text": "На экране всплыло окно: 'Поздравляем! Вы выиграли 10 000 000 сум! Введите данные карты для получения'. Что делать?",
        "a": "Обрадоваться и ввести номер карты родителей.",
        "b": "Закрыть вкладку, понимая, что это мошенническая уловка для списания денег.",
        "c": "Поделиться новостью со всем классом.",
        "d": "Позвонить в банк и потребовать выдать выигрыш наличными.",
        "e": "Ввести данные карты соседа.",
        "correct": "B",
        "topic": "Всплывающие Ловушки",
        "expl": "Если вы не участвовали в конкурсе, вы не могли выиграть. Это типичный обман для кражи средств."
    },
    {
        "text": "Какое главное правило безопасности при работе за компьютером в школе или библиотеке?",
        "a": "Выключить монитор кнопкой на панели.",
        "b": "Обязательно выйти из всех своих аккаунтов (Выйти / Log Out) и закрыть браузер.",
        "c": "Положить ручку рядом с мышкой.",
        "d": "Перевернуть коврик для мыши.",
        "e": "Задвинуть стул под стол.",
        "correct": "B",
        "topic": "Общественные Компьютеры",
        "expl": "Если не нажать 'Выйти', следующий пользователь сможет читать ваши личные сообщения."
    },
    {
        "text": "Если вы нашли на улице или в классе чужую неизвестную USB-флешку, как поступить правильно?",
        "a": "Сразу вставить ее в свой компьютер, чтобы посмотреть, что там записано.",
        "b": "Не подключать к компьютеру, так как на ней могут быть вирусы, и отдать учителю.",
        "c": "Раздать флешку друзьям по очереди.",
        "d": "Записать на нее свои любимые игры.",
        "e": "Попробовать сломать ее пополам.",
        "correct": "B",
        "topic": "Опасность Флешек",
        "expl": "Хакеры часто подбрасывают зараженные флешки (Baiting), чтобы заразить устройства при первом подключении."
    },
    {
        "text": "Зачем необходимо регулярно обновлять (Update) операционную систему и программы?",
        "a": "Только ради изменения формы иконок.",
        "b": "Чтобы устранить дыры в безопасности (уязвимости), найденные разработчиками, и защититься от новых вирусов.",
        "c": "Чтобы камера смартфона стала больше.",
        "d": "Чтобы экран никогда не разбивался.",
        "e": "Чтобы удалить все игры с телефона.",
        "correct": "B",
        "topic": "Обновления Безопасности",
        "expl": "Патчи безопасности закрывают лазейки, через которые вредоносные программы проникают в систему."
    },
    {
        "text": "Для чего нужно создавать резервные копии (Backup) важных файлов?",
        "a": "Чтобы файлы занимали больше места на диске.",
        "b": "Чтобы при поломке компьютера или атаке вируса можно было восстановить важные документы без потерь.",
        "c": "Чтобы продавать свои файлы в интернете.",
        "d": "Чтобы каждый день форматировать диск.",
        "e": "Для улучшения звука в наушниках.",
        "correct": "B",
        "topic": "Резервное Копирование",
        "expl": "Бэкап гарантирует сохранность ваших домашних заданий и фото даже при выходе устройства из строя."
    },
    {
        "text": "Если друг просит пароль от вашего игрового аккаунта 'на один день покачать персонажа', как ответить?",
        "a": "Сразу дать пароль, ведь это друг.",
        "b": "Вежливо объяснить, что по правилам безопасности передавать пароли кому-либо строго запрещено.",
        "c": "Отправить ему фото банковской карты.",
        "d": "Подарить ему свой телефон.",
        "e": "Перестать с ним разговаривать навсегда.",
        "correct": "B",
        "topic": "Культура Паролей",
        "expl": "Передача паролей третьим лицам часто приводит к потере аккаунта или его блокировке системой."
    },
    {
        "text": "К кому в первую очередь следует обратиться, если вы столкнулись с угрозой или мошенничеством в интернете?",
        "a": "Никому не рассказывать и ждать, что само пройдет.",
        "b": "Сообщить родителям или учителю информатики.",
        "c": "Написать в незнакомые чаты в соцсетях.",
        "d": "Перезагрузить компьютер и продолжить играть.",
        "e": "Отправить мошеннику все свои сбережения.",
        "correct": "B",
        "topic": "Помощь Взрослых",
        "expl": "Взрослые и педагоги помогут быстро и грамотно нейтрализовать киберугрозу."
    }
]

print("Grade 5-6 test data loaded (25 questions UZ & RU).")
