#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Target International School — 5–6-Sinf Vibecoding Test Ma'lumotlari
Fan: Vibecoding (Junior Creators, Kiber-O'yinlar va Raqamli Madaniyat)
O'qituvchi: Ismoiljon Usmonov · Yunusobod filiali

Struktura:
- 25 ta umumiy, bolalarbop, tushunarli va qulay savollar (General Concepts).
- Taqdimot raqamlari yoki yodlashga asoslangan savollar YO'Q.
- O'yin yaratish asoslari, AI vositalari, qahramon harakati, xavflar, ballar, 
  xatolarni tuzatish (debugging), parollar va raqamli xavfsizlik madaniyati.
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
    "instructions": "Ko'rsatma: Har bir savolga berilgan 5 ta variantdan (A, B, C, D, E) faqat bitta to'g'ri javobni tanlang va qalam bilan belgilang. Har bir to'g'ri javob uchun 1 ball beriladi (Jami: 25 ball)."
}

KEYS_META_5_6_UZ = {
    "heading": "JAVOBLAR KALITI VA BAHOLASH MEZONI",
    "subheading": "O'qituvchi: Ismoiljon Usmonov · 5–6-sinf Vibecoding rasmiy tekshirish kaliti (25 ta savol)",
    "table_headers": ["№", "Kalit", "Mavzu / Yo'nalish", "Izoh va Tushuntirish"],
    "scale_heading": "Rasmiy 25 Ballik Baholash Shkalasi:",
    "rubric_tiers": [
        {"grade": "A'lo (5)", "range": "22 – 25 ball", "desc": "O'yin mexanikasi, AI vositalari va raqamli xavfsizlik bo'yicha a'lo bilim"},
        {"grade": "Yaxshi (4)", "range": "18 – 21 ball", "desc": "Asosiy o'yin tushunchalari va xavfsizlik qoidalarini yaxshi o'zlashtirgan"},
        {"grade": "Qoniqarli (3)", "range": "13 – 17 ball", "desc": "O'yin elementlari va parollar mavzusini biroz takrorlash lozim"},
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
    "instructions": "Инструкция: В каждом вопросе выберите только один правильный вариант ответа из пяти (A, B, C, D, E) и отметьте его. За каждый правильный ответ начисляется 1 балл (Всего: 25 баллов)."
}

KEYS_META_5_6_RU = {
    "heading": "КЛЮЧИ ОТВЕТОВ И КРИТЕРИИ ОЦЕНИВАНИЯ",
    "subheading": "Учитель: Исмоилжон Усмонов · Официальный ключ 5–6 класс (25 вопросов)",
    "table_headers": ["№", "Ключ", "Тема / Направление", "Пояснение и разбор ответа"],
    "scale_heading": "Официальная 25-балльная шкала оценивания:",
    "rubric_tiers": [
        {"grade": "Отлично (5)", "range": "22 – 25 баллов", "desc": "Отличные общие знания создания игр, работы с ИИ и кибербезопасности"},
        {"grade": "Хорошо (4)", "range": "18 – 21 балл", "desc": "Игровая логика и правила онлайн-безопасности хорошо освоены"},
        {"grade": "Удовл. (3)", "range": "13 – 17 баллов", "desc": "Требуется повторение игровых элементов и правил безопасности"},
        {"grade": "Неудовл. (2)", "range": "0 – 12 баллов", "desc": "Необходимо повторить основы Vibecoding"}
    ]
}

QUESTIONS_5_6_UZ = [
    # 1
    {
        "text": "Sun'iy intellekt (AI) nima va u insonlarga nima uchun kerak?",
        "a": "Inson kabi o'zi mustaqil ovqatlanadigan tirik robot.",
        "b": "Inson bergan savollarga javob beradigan, matn va rasmlar yaratishda yordam beradigan aqlli kompyuter dasturi.",
        "c": "Faqatgina kompyuter monitorining elektr simi.",
        "d": "Kompyuterni buzadigan xavfli virus.",
        "e": "Oddiy devor soati.",
        "correct": "B",
        "topic": "01: Sun'iy intellekt nima",
        "expl": "AI — inson ko'rsatmasi bilan g'oyalar, rasmlar va matnlar yaratishda yordam beruvchi aqlli dastur."
    },
    # 2
    {
        "text": "Sun'iy intellektga biror narsa chizdirish yoki yozdirish uchun beriladigan buyruq qanday ataladi?",
        "a": "Wi-Fi paroli",
        "b": "Prompt (so'rov yoki ko'rsatma)",
        "c": "Sichqoncha tugmasi",
        "d": "Klaviatura drayveri",
        "e": "Kompyuter qutisi",
        "correct": "B",
        "topic": "02: Prompt tushunchasi",
        "expl": "Prompt — bu AI ga nima qilish kerakligini tushuntiruvchi matnli topshiriq."
    },
    # 3
    {
        "text": "AI yordamida o'yin yoki dastur yaratish (Vibecoding) ning asosiy maqsadi nima?",
        "a": "Faqat tayyor o'yinlarni o'ynab, dars qilmaslik.",
        "b": "O'z g'oyalaringni AI yordamida tezroq va osonroq qiziqarli o'yinga aylantirish.",
        "c": "Kompyuter ekranini bo'yab qo'yish.",
        "d": "Klaviatura tugmalarini yulib olish.",
        "e": "Internetni butunlay o'chirib qo'yish.",
        "correct": "B",
        "topic": "03: Vibecoding maqsadi",
        "expl": "Vibecoding o'quvchiga o'zining qiziqarli o'yin g'oyalarini AI yordamida amalga oshirish imkonini beradi."
    },
    # 4
    {
        "text": "Kompyuter o'yinlarida qahramonni harakatlantirish uchun odatda nimalardan foydalaniladi?",
        "a": "Faqatgina printerdan.",
        "b": "Klaviatura tugmalari (strelkalar yoki W, A, S, D) va sichqonchadan.",
        "c": "Ovoz karnayining ovoz balandligidan.",
        "d": "Faqat kompyuter sovutgich fanidan.",
        "e": "Monitorning elektr vilkasidan.",
        "correct": "B",
        "topic": "04: Qahramonni boshqarish",
        "expl": "O'yin qahramoni foydalanuvchi klaviatura va sichqonchada bergan signallar orqali harakatlanadi."
    },
    # 5
    {
        "text": "O'yinlarda qahramonning 'Jonlari' (HP yoki yurakchalar) nima uchun kerak?",
        "a": "Monitor ekranini yorqinroq qilish uchun.",
        "b": "Qahramon to'siqqa tekkanda kamayib, nechta imkoniyati qolganini ko'rsatish uchun.",
        "c": "Kompyuter batareyasini zaryadlash uchun.",
        "d": "O'yin xaritasi rangini o'zgartirish uchun.",
        "e": "Faqat kompyuterni o'chirib qo'yish uchun.",
        "correct": "B",
        "topic": "05: Qahramon jonlari (HP)",
        "expl": "HP (Health Points) qahramonning qancha kuchi yoki joni qolganini ifodalaydi."
    },
    # 6
    {
        "text": "O'yindagi to'siqlar (masalan: tikanlar, teshiklar, dushmanlar) nima maqsadda qo'yiladi?",
        "a": "O'yinni buzib tashlash uchun.",
        "b": "O'yin qiziqarli va chaqqonlikni talab qiladigan sarguzasht bo'lishi uchun.",
        "c": "Kompyuter xotirasini to'ldirish uchun.",
        "d": "O'yinchining internet tezligini tushirish uchun.",
        "e": "Ekranni qora rangga bo'yash uchun.",
        "correct": "B",
        "topic": "06: O'yin to'siqlari",
        "expl": "To'siqlar o'yinga hayajon va qiyinchilik qo'shib, o'yinni maroqli qiladi."
    },
    # 7
    {
        "text": "Qahramon o'yinda tanga, yulduzcha yoki kristall yig'sa nima sodir bo'ladi?",
        "a": "Kompyuter drayverlari o'chib ketadi.",
        "b": "O'yinchining ochkolari (Score) ko'payadi va yangi rekord o'rnatiladi.",
        "c": "Klaviatura tugmalari ishlamay qoladi.",
        "d": "Monitor ekrani teskari aylanib qoladi.",
        "e": "O'yin fayllari avtomatik o'chiriladi.",
        "correct": "B",
        "topic": "07: Ballar va mukofotlar",
        "expl": "Kristall va tangalar o'yinchiga ko'proq ball to'plash va g'olib bo'lish imkonini beradi."
    },
    # 8
    {
        "text": "O'yinda 'Game Over' yozuvi chiqqanda bu nimani anglatadi?",
        "a": "Kompyuter buzilib, yangisini sotib olish kerakligini.",
        "b": "Qahramonning barcha jonlari tugaganini va o'yinni qaytadan boshlash mumkinligini.",
        "c": "Internet umrbod o'chirilganini.",
        "d": "Klaviatura tozalanishi kerakligini.",
        "e": "O'yinchi darsga kechikkanini.",
        "correct": "B",
        "topic": "08: Game Over holati",
        "expl": "Game Over — sinov tugaganini va yangidan harakat qilib o'ynash mumkinligini bildiradi."
    },
    # 9
    {
        "text": "O'yinlarda tovush effektlari (sakrash ovozi, tanga jiringlashi, musiqa) nima uchun kerak?",
        "a": "O'yinni yanada qiziqarli, quvnoq va jonli qilish uchun.",
        "b": "Qo'shnilarni bezovta qilish uchun.",
        "c": "Kompyuter fanini tezroq aylantirish uchun.",
        "d": "Ekranning rangini o'zgartirish uchun.",
        "e": "Faqat batareyani tezroq tugatish uchun.",
        "correct": "A",
        "topic": "09: O'yin tovushlari",
        "expl": "Tovushlar va musiqa o'yin atmosferasini yaratadi va qahramon harakatlarini jonlantiradi."
    },
    # 10
    {
        "text": "O'yinlarda kompyuter boshqaradigan boshqa qahramonlar (NPC) nima vazifani bajaradi?",
        "a": "Kompyuterni o'chirib qo'yadi.",
        "b": "Bosh qahramonga maslahat beradi, suhbatlashadi yoki yangi topshiriq (kvest) beradi.",
        "c": "Internet simini uzib qo'yadi.",
        "d": "Faqat kompyuter soatini o'zgartiradi.",
        "e": "O'yin fayllarini yashirib qo'yadi.",
        "correct": "B",
        "topic": "10: O'yin qahramonlari (NPC)",
        "expl": "NPC — o'yinda yordam beruvchi yoki qiziqarli topshiriq beruvchi do'stona qahramonlar."
    },
    # 11
    {
        "text": "O'yinlarda qahramonning yugurishi yoki sakrashi qanday qilib harakatlanayotgandek ko'rinadi?",
        "a": "Rasmlar juda tez ketma-ket almashib, ko'zimizga harakatdek ko'rinadi (Animatsiya).",
        "b": "Monitorning o'zi jismonan harakat qiladi.",
        "c": "Klaviatura o'zi qahramonni itarib yuboradi.",
        "d": "Faqat kompyuter kamerasi orqali ko'rinadi.",
        "e": "Bu haqiqiy tirik odamning ekranga kirib olishidir.",
        "correct": "A",
        "topic": "11: O'yin animatsiyasi",
        "expl": "Animatsiya — bir nechta rasmlarning tez almashishi natijasida hosil bo'ladigan silliq harakat."
    },
    # 12
    {
        "text": "O'yin yaratuvchi dasturchi nima ish qiladi?",
        "a": "Faqat monitor ekranidagi changlarni artadi.",
        "b": "Kompyuter tushunadigan qoidalar va kodlar yozib, o'yin qanday ishlashini belgilaydi.",
        "c": "Kompyuter detallarini bolg'a bilan uradi.",
        "d": "Faqat do'konda kompyuter sotadi.",
        "e": "Maktab qo'ng'irog'ini chaladi.",
        "correct": "B",
        "topic": "12: Dasturchi kasbi",
        "expl": "Dasturchi o'yindagi qahramonlar va to'siqlarning qanday ishlashini kod orqali buyuradi."
    },
    # 13
    {
        "text": "O'yinda qahramon birdan devor ichiga kirib ketishi yoki ball qo'shilmay qolishi nima deb ataladi?",
        "a": "Yangi kompyuter modeli",
        "b": "Bug (dasturdagi xatolik)",
        "c": "Antivirus yangilanishi",
        "d": "Internet tezligi",
        "e": "O'yin mukofoti",
        "correct": "B",
        "topic": "13: O'yindagi Bug",
        "expl": "Bug — bu dastur kodida yo'l qo'yilgan xatolik bo'lib, uni topib tuzatish kerak."
    },
    # 14
    {
        "text": "O'yinda xatolik (bug) paydo bo'lsa, qanday yo'l tutish to'g'ri?",
        "a": "Kompyuterni yerga tashlab yuborish.",
        "b": "Qaysi kod xato yozilganini tekshirib, xatoni tuzatish (debugging qilish).",
        "c": "O'yinni o'chirish va boshqa hech qachon kompyuter ishlatmaslik.",
        "d": "Klaviaturani suv bilan yuvish.",
        "e": "Barcha do'stlar bilan urishib qolish.",
        "correct": "B",
        "topic": "14: Debugging jarayoni",
        "expl": "Dasturchilar xatolardan qo'rqmaydi, balki xatoni qidirib topib tuzatadi (debugging qiladi)."
    },
    # 15
    {
        "text": "O'yinlarda '1-bosqich', '2-bosqich' kabi darajalar (Levels) nima uchun tuziladi?",
        "a": "O'yinchi har bir bosqichda yangi to'siqlarni yengib, qiziqib o'ynashi uchun.",
        "b": "Kompyuter elektr energiyasini kamroq iste'mol qilishi uchun.",
        "c": "Faqat monitor rangini o'chirish uchun.",
        "d": "Klaviatura charchab qolmasligi uchun.",
        "e": "Sichqoncha batareyasini tejash uchun.",
        "correct": "A",
        "topic": "15: O'yin darajalari",
        "expl": "Darajalar bosqichma-bosqich murakkablashib, o'yinchiga qiziq bo'lishini ta'minlaydi."
    },
    # 16
    {
        "text": "O'yin yoki maktab akkauntingiz uchun qaysi parol eng xavfsiz va mustahkam hisoblanadi?",
        "a": "123456",
        "b": "meningismim",
        "c": "Kiber#2026!Target",
        "d": "0000",
        "e": "qwerty",
        "correct": "C",
        "topic": "16: Mustahkam parol",
        "expl": "Katta-kichik harflar, raqamlar va belgilar (#, !) aralashgan uzun parol eng mustahkamdir."
    },
    # 17
    {
        "text": "Nima uchun o'z parolingizni begona odamlarga aytmasligingiz kerak?",
        "a": "Kompyuter ekrani qizarib qolishi uchun.",
        "b": "Begonalar sizning o'yindagi yutuqlaringizni va shaxsiy ma'lumotlaringizni o'g'irlamasligi uchun.",
        "c": "Faqat internet tezligini oshirish uchun.",
        "d": "Klaviatura tugmalari bosilmay qolishi uchun.",
        "e": "Monitor o'z-o'zidan o'chib qolishi uchun.",
        "correct": "B",
        "topic": "17: Parol maxfiyligi",
        "expl": "Parol — bu sizning shaxsiy kalitingiz, uni faqat o'zingiz va ota-onangiz bilishi kerak."
    },
    # 18
    {
        "text": "Internetda kimdir: 'Mana bu havolaga kirsang, senga bepul 10 000 Robux beramiz!' deb yozsa, nima qilish kerak?",
        "a": "Darhol havolani ochib, o'z parolingizni yozish.",
        "b": "Bu yolg'on (fishing) qopqoni ekanini bilib, havolani ochmaslik va kattalarga aytish.",
        "c": "Do'stlaringizning hammasiga o'sha havolani tarqatish.",
        "d": "O'z uyingiz manzilini o'sha odamga yuborish.",
        "e": "Barcha parollaringizni unga xat qilib jo'natish.",
        "correct": "B",
        "topic": "18: Fishing qopqoni",
        "expl": "Bepul narsalar va'da qiluvchi soxta havolalar o'g'rilarning aldovi hisoblanadi."
    },
    # 19
    {
        "text": "Qaysi ma'lumotlarni internetdagi notanish odamlarga HECH QACHON aytmaslik kerak?",
        "a": "O'zingiz yoqtirgan sevimli meva nomini.",
        "b": "Uy manzilingiz, telefon raqamingiz, maktabingiz va parollaringizni.",
        "c": "Sevimli multfilmingiz qahramoni nomini.",
        "d": "O'yindagi robotning rangini.",
        "e": "Sevimli futbol jamoangiz nomini.",
        "correct": "B",
        "topic": "19: Shaxsiy ma'lumotlar",
        "expl": "Uy manzili va telefon raqami shaxsiy ma'lumot bo'lib, begonalarga aytilmaydi."
    },
    # 20
    {
        "text": "Internetga rasm yoki xabar joylashdan oldin qanday o'ylash kerak (Katta Ekran qoidasi)?",
        "a": "'Agar bu rasmni butun maktab va ota-onam ulkan ekranda ko'rsa, men xijolat bo'lmaymanmi?' deb o'ylash.",
        "b": "Faqat eng shovqinli xabarlarni yozish kerak deb o'ylash.",
        "c": "Hech narsa deb o'ylamasdan hamma narsani tarqatish.",
        "d": "Faqat kompyuter narxini surishtirish.",
        "e": "Ekranni qo'l bilan tozalash kerak deb o'ylash.",
        "correct": "A",
        "topic": "20: Katta Ekran qoidasi",
        "expl": "Internetga qo'yilgan ma'lumotni hamma ko'rishi mumkin, shuning uchun faqat yaxshi narsalarni ulashish kerak."
    },
    # 21
    {
        "text": "Kompyuter virusi yoki zararli dastur nima?",
        "a": "Kompyuterga choy to'kilib ketishi.",
        "b": "Kompyuterdagi fayllarni o'chiradigan yoki buzadigan xavfli, yashirin dastur.",
        "c": "O'yin qahramonining yangi kiyimi.",
        "d": "Tezkor Wi-Fi signali.",
        "e": "Chiroyli ish stoli fon rasmi.",
        "correct": "B",
        "topic": "21: Kompyuter viruslari",
        "expl": "Viruslar — kompyuter ishini buzuvchi zararli dasturlar bo'lib, antivirus ulardan himoya qiladi."
    },
    # 22
    {
        "text": "O'yinlar yoki dasturlarni qayerdan yuklab olish eng xavfsiz hisoblanadi?",
        "a": "Noma'lum va shubhali reklama saytlaridan.",
        "b": "Rasmiy va ishonchli do'konlardan (masalan, rasmiy saytlar yoki App Store/Google Play).",
        "c": "Telegramdagi notanish odam yuborgan fayldan.",
        "d": "Faqat elektron pochta spam xabarlaridan.",
        "e": "Qidiruvdagi birinchi chiqqan noma'lum havoladan.",
        "correct": "B",
        "topic": "22: Xavfsiz yuklab olish",
        "expl": "Dastur va o'yinlarni faqat rasmiy manbalardan yuklab olish viruslardan himoya qiladi."
    },
    # 23
    {
        "text": "Do'stlar bilan birgalikda o'yin yaratishning eng katta foydasi nimada?",
        "a": "Hech kim ish qilmasdan faqat uxlashi mumkin.",
        "b": "Har kim o'zining yaxshi bilgan ishini (biri rasm chizadi, biri hikoya yozadi, biri kodlaydi) qilib, ajoyib o'yin yarata oladi.",
        "c": "Kompyuter klaviaturasini talashib sindirish mumkin.",
        "d": "O'yinni tezroq o'chirib tashlash oson bo'ladi.",
        "e": "Dars vaqti behuda o'tadi.",
        "correct": "B",
        "topic": "23: Jamoaviy ishlash",
        "expl": "Jamoada ishlash g'oyalarni birlashtirib, yanada qiziqarliroq o'yin yaratishga yordam beradi."
    },
    # 24
    {
        "text": "O'zingiz yaratgan o'yinni boshqalarga tanishtirayotganda nimalar haqida gapirib berish kerak?",
        "a": "O'yin nomi, qahramonning maqsadi va qanday o'ynash (qoidalari) haqida.",
        "b": "Ertalab nima tush ko'rganingiz haqida.",
        "c": "Faqat xonadagi chiroqlar nechta ekanligi haqida.",
        "d": "Monitor qanchalik og'irligi haqida.",
        "e": "Hech narsa demasdan yig'lash kerak.",
        "correct": "A",
        "topic": "24: O'yin taqdimoti",
        "expl": "Taqdimotda o'yinning qiziqarli g'oyasi, qahramoni va o'ynash qoidalari tushuntiriladi."
    },
    # 25
    {
        "text": "Vibecoding darslarida haqiqiy kiber-ijodkor bo'lish uchun nima eng muhimi?",
        "a": "Xato qilishdan qo'rqmaslik, yangi g'oyalarni sinab ko'rish va AI bilan do'stlashish.",
        "b": "Birinchi xatodanoq kompyuterni o'chirib qo'yish.",
        "c": "Faqat boshqalarning o'yinini ko'chirib olish.",
        "d": "Hech narsani o'rganmasdan o'tirish.",
        "e": "Kompyuter simlarini chalkashtirib qo'yish.",
        "correct": "A",
        "topic": "25: Kiber-ijodkorlik",
        "expl": "Xatolardan qo'rqmay yangi narsalarni sinab ko'rish eng zo'r dasturchi va o'yin yaratuvchi bo'lish siri."
    }
]

QUESTIONS_5_6_RU = [
    # 1
    {
        "text": "Что такое искусственный интеллект (ИИ) и зачем он нужен людям?",
        "a": "Живой робот, который сам питается едой как человек.",
        "b": "Умная компьютерная программа, помогающая отвечать на вопросы, создавать тексты и картинки.",
        "c": "Всего лишь провод питания компьютерного монитора.",
        "d": "Опасный компьютерный вирус, ломающий программы.",
        "e": "Обычные настенные часы.",
        "correct": "B",
        "topic": "01: Что такое ИИ",
        "expl": "ИИ — это умная программа, помогающая создавать идеи, тексты и изображения по инструкциям человека."
    },
    # 2
    {
        "text": "Как называется команда или инструкция, которую мы пишем искусственному интеллекту?",
        "a": "Пароль от Wi-Fi",
        "b": "Промпт (запрос или инструкция)",
        "c": "Кнопка мыши",
        "d": "Драйвер клавиатуры",
        "e": "Корпус компьютера",
        "correct": "B",
        "topic": "02: Понятие промпта",
        "expl": "Промпт — это текстовое задание, объясняющее ИИ, что нужно сделать."
    },
    # 3
    {
        "text": "В чем главная цель создания игр и программ с помощью ИИ (Vibecoding)?",
        "a": "Только играть в готовые игры и не учиться.",
        "b": "Быстрее и проще превращать свои творческие идеи в интересные игры с помощью ИИ.",
        "c": "Раскрасить экран компьютера красками.",
        "d": "Оторвать клавиши на клавиатуре.",
        "e": "Навсегда отключить интернет.",
        "correct": "B",
        "topic": "03: Цель Vibecoding",
        "expl": "Vibecoding позволяет ученику воплощать свои игровые идеи с помощью ИИ."
    },
    # 4
    {
        "text": "Что обычно используется для управления движением персонажа в компьютерной игре?",
        "a": "Только принтер для бумаги.",
        "b": "Клавиши на клавиатуре (стрелки или W, A, S, D) и мышь.",
        "c": "Регулятор громкости колонок.",
        "d": "Вентилятор охлаждения компьютера.",
        "e": "Электрическая вилка монитора.",
        "correct": "B",
        "topic": "04: Управление персонажем",
        "expl": "Персонаж игры управляется нажатиями клавиш клавиатуры и движениями мыши."
    },
    # 5
    {
        "text": "Для чего в играх нужны «Жизни» (HP или сердечки) персонажа?",
        "a": "Чтобы сделать экран монитора ярче.",
        "b": "Чтобы показывать, сколько попыток осталось у героя при столкновении с препятствиями.",
        "c": "Для зарядки аккумулятора ноутбука.",
        "d": "Чтобы менять цвет игровой карты.",
        "e": "Только для выключения компьютера.",
        "correct": "B",
        "topic": "05: Жизни героя (HP)",
        "expl": "HP показывает текущий запас здоровья или попыток персонажа."
    },
    # 6
    {
        "text": "Зачем в игру добавляют препятствия (например: шипы, ловушки, врагов)?",
        "a": "Чтобы сломать игру.",
        "b": "Чтобы игра была интересной, увлекательной и требовала ловкости.",
        "c": "Чтобы забить память компьютера.",
        "d": "Чтобы снизить скорость интернета.",
        "e": "Чтобы покрасить экран в черный цвет.",
        "correct": "B",
        "topic": "06: Игровые препятствия",
        "expl": "Препятствия добавляют азарт и сложность, делая игру интересной."
    },
    # 7
    {
        "text": "Что происходит, когда персонаж собирает монеты, звездочки или кристаллы?",
        "a": "Стираются драйверы компьютера.",
        "b": "Увеличиваются очки (Score) игрока и ставится новый рекорд.",
        "c": "Перестают работать клавиши клавиатуры.",
        "d": "Экран монитора переворачивается.",
        "e": "Файлы игры автоматически удаляются.",
        "correct": "B",
        "topic": "07: Очки и награды",
        "expl": "Сбор предметов увеличивает счет игрока и ведет к победе."
    },
    # 8
    {
        "text": "Что означает надпись «Game Over» в игре?",
        "a": "Компьютер сломался и нужно купить новый.",
        "b": "У героя закончились жизни, и можно начать уровень заново.",
        "c": "Интернет отключился навсегда.",
        "d": "Клавиатуру нужно помыть.",
        "e": "Игрок опоздал на урок.",
        "correct": "B",
        "topic": "08: Состояние Game Over",
        "expl": "Game Over означает окончание попытки и возможность сыграть снова."
    },
    # 9
    {
        "text": "Зачем в играх нужны звуковые эффекты (звук прыжка, звон монет, фоновая музыка)?",
        "a": "Чтобы сделать игру более увлекательной, веселой и живой.",
        "b": "Чтобы разбудить соседей.",
        "c": "Чтобы быстрее крутился вентилятор ноутбука.",
        "d": "Чтобы поменять цвет экрана.",
        "e": "Только чтобы быстрее разрядить батарею.",
        "correct": "A",
        "topic": "09: Звуки в игре",
        "expl": "Звуки и музыка создают атмосферу игры и оживляют действия персонажа."
    },
    # 10
    {
        "text": "Какую роль в играх выполняют персонажи, управляемые компьютером (NPC)?",
        "a": "Выключают компьютер.",
        "b": "Подсказывают главному герою, разговаривают с ним или дают новые задания (квесты).",
        "c": "Отключают интернет-кабель.",
        "d": "Только меняют системное время.",
        "e": "Прячут файлы игры.",
        "correct": "B",
        "topic": "10: Персонажи игры (NPC)",
        "expl": "NPC — это персонажи, которые помогают игроку и дают задания в игровом мире."
    },
    # 11
    {
        "text": "Каким образом бег или прыжок персонажа в игре выглядит движущимся?",
        "a": "Картинки очень быстро сменяют друг друга, создавая иллюзию движения (Анимация).",
        "b": "Сам монитор физически двигается.",
        "c": "Клавиатура сама толкает персонажа.",
        "d": "Это видно только через камеру компьютера.",
        "e": "Настоящий живой человек залезает внутрь экрана.",
        "correct": "A",
        "topic": "11: Анимация в играх",
        "expl": "Анимация — это быстрая смена кадров, создающая эффект плавного движения."
    },
    # 12
    {
        "text": "Чем занимается программист при создании игр?",
        "a": "Только протирает пыль с экрана монитора.",
        "b": "Пишет правила и команды на языке компьютера, определяя, как работает игра.",
        "c": "Стучит молотком по деталям компьютера.",
        "d": "Только продает компьютеры в магазине.",
        "e": "Звонит в школьный колокольчик.",
        "correct": "B",
        "topic": "12: Профессия программиста",
        "expl": "Программист с помощью кода задает правила движения персонажей и работы игры."
    },
    # 13
    {
        "text": "Как называется ситуация, когда персонаж застревает в стене или очки не начисляются?",
        "a": "Новая модель компьютера",
        "b": "Баг (ошибка в программном коде)",
        "c": "Обновление антивируса",
        "d": "Скорость интернета",
        "e": "Главная награда в игре",
        "correct": "B",
        "topic": "13: Ошибка (баг)",
        "expl": "Баг — это программная ошибка, которую необходимо найти и исправить."
    },
    # 14
    {
        "text": "Что правильно делать, если в игре возникла ошибка (баг)?",
        "a": "Бросить компьютер на пол.",
        "b": "Проверить строки кода, найти ошибку и исправить её (сделать дебаггинг).",
        "c": "Удалить игру и больше никогда не пользоваться компьютером.",
        "d": "Помыть клавиатуру под краном с водой.",
        "e": "Поссориться со всеми друзьями.",
        "correct": "B",
        "topic": "14: Исправление ошибок",
        "expl": "Программисты не боятся ошибок, а находят и аккуратно исправляют их."
    },
    # 15
    {
        "text": "Зачем в играх делают уровни (1-й уровень, 2-й уровень)?",
        "a": "Чтобы игрок преодолевал новые испытания и игра оставалась увлекательной.",
        "b": "Чтобы компьютер тратил меньше электричества.",
        "c": "Только чтобы погасить цвет монитора.",
        "d": "Чтобы клавиатура не уставала.",
        "e": "Чтобы сберечь батарейку мышки.",
        "correct": "A",
        "topic": "15: Уровни в игре",
        "expl": "Уровни усложняются постепенно, поддерживая интерес игрока."
    },
    # 16
    {
        "text": "Какой пароль является самым безопасным и надежным для вашего игрового аккаунта?",
        "a": "123456",
        "b": "moeimya",
        "c": "Kiber#2026!Target",
        "d": "0000",
        "e": "qwerty",
        "correct": "C",
        "topic": "16: Надежный пароль",
        "expl": "Длинный пароль с буквами разного регистра, цифрами и знаками самый безопасный."
    },
    # 17
    {
        "text": "Почему нельзя сообщать свой пароль посторонним людям?",
        "a": "Чтобы экран компьютера не покраснел.",
        "b": "Чтобы чужие люди не украли ваши игровые достижения и личные данные.",
        "c": "Только чтобы увеличить скорость интернета.",
        "d": "Чтобы клавиши клавиатуры не перестали нажиматься.",
        "e": "Чтобы монитор сам по себе не выключился.",
        "correct": "B",
        "topic": "17: Секретность пароля",
        "expl": "Пароль — это личный ключ, который должны знать только вы и ваши родители."
    },
    # 18
    {
        "text": "Что делать, если в интернете обещают: «Перейди по ссылке и получи бесплатно 10 000 робуксов»?",
        "a": "Срочно открыть ссылку и ввести свой пароль.",
        "b": "Понять, что это ловушка мошенников (фишинг), не нажимать и рассказать взрослым.",
        "c": "Разослать эту ссылку всем своим друзьям.",
        "d": "Отправить этому человеку адрес своего дома.",
        "e": "Написать ему все свои личные пароли.",
        "correct": "B",
        "topic": "18: Фишинг и обман",
        "expl": "Обещания бесплатных игровых денег — частый обман мошенников для кражи аккаунтов."
    },
    # 19
    {
        "text": "Какую информацию НИКОГДА нельзя сообщать незнакомцам в интернете?",
        "a": "Название любимого фрукта.",
        "b": "Домашний адрес, номер телефона, номер школы и свои пароли.",
        "c": "Имя любимого персонажа из мультфильма.",
        "d": "Цвет робота в вашей игре.",
        "e": "Название любимой футбольной команды.",
        "correct": "B",
        "topic": "19: Личные данные",
        "expl": "Личные данные (адрес, телефон, пароли) должны быть строго защищены от незнакомцев."
    },
    # 20
    {
        "text": "О чем нужно подумать перед тем, как выложить фото или сообщение в интернет (Правило билборда)?",
        "a": "«Будет ли мне стыдно, если это фото увидят на огромном экране вся школа и родители?»",
        "b": "Думать только о том, как сделать больше шума.",
        "c": "Не задумываясь выкладывать абсолютно всё.",
        "d": "Думать только о стоимости компьютера.",
        "e": "Думать о том, как протереть монитор рукой.",
        "correct": "A",
        "topic": "20: Правило билборда",
        "expl": "Всё, что попадает в интернет, могут увидеть другие, поэтому публикуйте только то, за что не будет стыдно."
    },
    # 21
    {
        "text": "Что такое компьютерный вирус или вредоносная программа?",
        "a": "Пролитый на клавиатуру чай.",
        "b": "Опасная скрытая программа, которая может удалить или повредить файлы на компьютере.",
        "c": "Новый костюм персонажа в игре.",
        "d": "Быстрый сигнал Wi-Fi.",
        "e": "Красивые обои для рабочего стола.",
        "correct": "B",
        "topic": "21: Компьютерные вирусы",
        "expl": "Вирусы — это вредоносные программы, нарушающие работу компьютера."
    },
    # 22
    {
        "text": "Откуда безопаснее всего скачивать игры и программы?",
        "a": "С неизвестных и подозрительных сайтов с рекламой.",
        "b": "Из официальных и проверенных источников (официальные сайты, App Store, Google Play).",
        "c": "Из файлов, которые прислал незнакомец в Telegram.",
        "d": "Только из спам-писем электронной почты.",
        "e": "По первой попавшейся непонятной ссылке.",
        "correct": "B",
        "topic": "22: Безопасная загрузка",
        "expl": "Скачивание из проверенных официальных магазинов защищает от вирусов."
    },
    # 23
    {
        "text": "В чем главная польза совместной работы над игрой с друзьями?",
        "a": "Никто ничего не делает и можно просто спать.",
        "b": "Каждый делает то, что умеет лучше всего (один рисует, другой пишет сюжет, третий кодит), и получается крутая игра.",
        "c": "Можно подраться из-за клавиатуры и сломать её.",
        "d": "Проще быстрее удалить игру.",
        "e": "Можно просто потерять время.",
        "correct": "B",
        "topic": "23: Командная работа",
        "expl": "Командная работа объединяет разные таланты и позволяет создать отличную игру."
    },
    # 24
    {
        "text": "О чем нужно рассказать, презентуя созданную вами игру друзьям и одноклассникам?",
        "a": "Об названии игры, цели главного героя и правилах управления.",
        "b": "О том, какой сон приснился утром.",
        "c": "О том, сколько лампочек горит в комнате.",
        "d": "О том, сколько весит монитор.",
        "e": "Нужно молчать и плакать.",
        "correct": "A",
        "topic": "24: Презентация игры",
        "expl": "В презентации объясняют сюжет игры, цель героя и правила управления."
    },
    # 25
    {
        "text": "Что самое главное на уроках Vibecoding, чтобы стать настоящим кибер-создателем?",
        "a": "Не бояться ошибок, пробовать новые идеи и творить вместе с ИИ.",
        "b": "Сдаваться и выключать компьютер при первой же ошибке.",
        "c": "Только копировать чужие готовые игры.",
        "d": "Сидеть и ничего нового не изучать.",
        "e": "Запутать провода компьютера в узел.",
        "correct": "A",
        "topic": "25: Кибер-творчество",
        "expl": "Пробовать новое и не бояться ошибок — главный секрет успешного создателя игр."
    }
]

print("Grade 5-6 Vibecoding test data loaded (General Concepts, Zero Lesson Memorization). Teacher: Ismoiljon Usmonov.")
