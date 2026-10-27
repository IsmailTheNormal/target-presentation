#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
5–6-Sinf: 25 Savolli Haqiqiy Vibecoding va Sun'iy Intellekt Asoslari Testi
O'qituvchi: Ismoiljon Usmonov · Target International School, Yunusobod
Uzbek va Russian variantlari (5 ta variant: A, B, C, D, E)
"""

META_5_6_UZ = {
    "school_name": "TARGET INTERNATIONAL SCHOOL — YUNUSOBOD",
    "teacher_name": "Ismoiljon Usmonov",
    "exam_title": "5–6-SINF: VIBECODING VA SUN'IY INTELLEKT ASOSLARI",
    "track_title": "Vibecoding & AI Creators Track · O'qituvchi: Ismoiljon Usmonov",
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

KEYS_META_5_6_UZ = {
    "heading": "JAVOBLAR KALITI VA BAHOLASH MEZONI",
    "subheading": "O'qituvchi: Ismoiljon Usmonov · 5–6-sinf Vibecoding rasmiy kaliti (25 ta savol)",
    "table_headers": ["№", "Kalit", "Mavzu / Kompetensiya", "Izoh va Tushuntirish"],
    "scale_heading": "Rasmiy 25 Ballik Baholash Shkalasi:",
    "rubric_tiers": [
        {"grade": "A'lo (5)", "range": "22 – 25 ball", "desc": "Prompt muhandisligi, AI bilan kod yozish va dizayn vositalari bo'yicha a'lo bilim"},
        {"grade": "Yaxshi (4)", "range": "18 – 21 ball", "desc": "AI muloqot qoidalari va prompt tuzilishi yaxshi o'zlashtirilgan"},
        {"grade": "Qoniqarli (3)", "range": "13 – 17 ball", "desc": "Kontekst va AI xatolarini tekshirishni takrorlash lozim"},
        {"grade": "Qoniqarsiz (2)", "range": "0 – 12 ball", "desc": "Vibecoding asoslari qayta o'rganilishi zarur"}
    ]
}

META_5_6_RU = {
    "school_name": "TARGET INTERNATIONAL SCHOOL — ЮНУСАБАД",
    "teacher_name": "Исмоилжон Усмонов",
    "exam_title": "5–6 КЛАСС: ОСНОВЫ VIBECODING И ИСКУССТВЕННОГО ИНТЕЛЛЕКТА",
    "track_title": "Vibecoding & AI Creators Track · Преподаватель: Исмоилжон Усмонов",
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

KEYS_META_5_6_RU = {
    "heading": "КЛЮЧИ ОТВЕТОВ И КРИТЕРИИ ОЦЕНИВАНИЯ",
    "subheading": "Преподаватель: Исмоилжон Усмонов · Официальный ключ Vibecoding (5–6 класс, 25 вопросов)",
    "table_headers": ["№", "Ключ", "Тема / Компетенция", "Пояснение и Обоснование"],
    "scale_heading": "Официальная 25-балльная шкала оценивания:",
    "rubric_tiers": [
        {"grade": "Отлично (5)", "range": "22 – 25 баллов", "desc": "Отличное владение промпт-инжинирингом, генерацией кода и AI-инструментами"},
        {"grade": "Хорошо (4)", "range": "18 – 21 балл", "desc": "Хорошее понимание диалога с нейросетями и структуры промпта"},
        {"grade": "Удовлетворительно (3)", "range": "13 – 17 баллов", "desc": "Требуется повторение работы с контекстом и проверки ошибок AI"},
        {"grade": "Неудовлетворительно (2)", "range": "0 – 12 баллов", "desc": "Необходимо повторное изучение основ Vibecoding"}
    ]
}

QUESTIONS_5_6_UZ = [
    {
        "text": "Vibecoding tushunchasining asosiy mohiyati nimada?",
        "a": "Dasturchining o'zi kodning har bir harfini qo'lda terishi.",
        "b": "Sun'iy intellekt (AI) ga aniq g'oya va promptlar berib, kod va loyihalarni tezkor yaratish hamda natijani boshqarish.",
        "c": "Faqat kompyuter o'yinlarini o'ynash.",
        "d": "Kompyuterni elektr tarmog'idan uzib qo'yish.",
        "e": "Klaviaturani umuman ishlatmaslik.",
        "correct": "B",
        "topic": "Vibecoding Tushunchasi",
        "expl": "Vibecoding — insonning ijodiy g'oyasi va AI ning kod yozish tezligini birlashtirib, tayyor dasturlar yaratishdir."
    },
    {
        "text": "Sun'iy intellektga yuboriladigan buyruq yoki savol matni nima deb ataladi?",
        "a": "Virus",
        "b": "Prompt (Prompt / So'rov)",
        "c": "Drayver",
        "d": "Piksel",
        "e": "Kabel",
        "correct": "B",
        "topic": "Prompt Tushunchasi",
        "expl": "Prompt — foydalanuvchi sun'iy intellektga beradigan matnli yo'riqnoma, buyruq yoki savoldir."
    },
    {
        "text": "AI bilan muloqotda eng sifatli javob olish uchun prompt qanday tuzilishi kerak?",
        "a": "Faqat bitta so'z yozish kifoya.",
        "b": "Rol (Sen kimsan), Vazifa (Nima qilish kerak), Kontekst va Natija formati aniq ko'rsatilishi kerak.",
        "c": "Faqat katta harflar bilan yozilishi shart.",
        "d": "Faqat ingliz tilida yozilishi kerak, o'zbekcha yozish taqiqlanadi.",
        "e": "Har doim nuqtalarsiz yozilishi kerak.",
        "correct": "B",
        "topic": "Yaxshi Prompt Tuzilishi",
        "expl": "Kuchli promptda 4 element bo'ladi: Rol, Aniq vazifa, Qo'shimcha shartlar (kontekst) va Kutilgan format."
    },
    {
        "text": "Nega 'Menga sayt qilib ber' prompti yomon, lekin 'Menga bolalar uchun interaktiv matematika viktorinasi HTML/CSS kodini yozib ber' prompti yaxshi?",
        "a": "Chunki ikkinchisi qisqaroq.",
        "b": "Chunki ikkinchi promptda maqsad, mavzu, auditoriya va kerakli texnologiya aniq ko'rsatilgan.",
        "c": "Chunki birinchi promptda xatolar ko'p.",
        "d": "Chunki AI bolalarni yoqtirmaydi.",
        "e": "Ikkalasi ham bir xil natija beradi.",
        "correct": "B",
        "topic": "Aniq vs Noaniq Prompt",
        "expl": "Noaniq promptda AI taxmin qilishga majbur bo'ladi; aniq prompt esa kutilgan natijani birinchi urinishda beradi."
    },
    {
        "text": "AI bilan suhbatda 'Rol berish' (Role Prompting) usuli nima uchun ishlatiladi?",
        "a": "AI ning rangini o'zgartirish uchun.",
        "b": "AI ni ma'lum bir mutaxassis (masalan, 'Sen tajribali frontend dasturchisan') sifatida fikrlashga va professional javob berishga yo'naltirish uchun.",
        "c": "Kompyuter ovozini balandlatish uchun.",
        "d": "Internet tezligini oshirish uchun.",
        "e": "Faqat o'yin qahramonlarini chizish uchun.",
        "correct": "B",
        "topic": "Rol Berish (Role Prompting)",
        "expl": "Rol berilganda AI o'sha sohaning terminologiyasi va eng yaxshi amaliyotlaridan foydalanib javob qaytaradi."
    },
    {
        "text": "Sun'iy intellektning 'Gallyutsinatsiyasi' (Hallucination) nima?",
        "a": "AI ning kompyuterni o'chirib qo'yishi.",
        "b": "AI ning bilmagan narsasini xuddi haqiqatdek ishonch bilan to'qib chiqarishi (noto'g'ri fakt aytishi).",
        "c": "AI ning juda tez ishlashi.",
        "d": "AI ning rasm chiza olmasligi.",
        "e": "AI ning internetga ulanishi.",
        "correct": "B",
        "topic": "AI Gallyutsinatsiyasi",
        "expl": "Gallyutsinatsiya — modelning mavjud bo'lmagan ma'lumot yoki qoidalarni haqiqatdek taqdim etishi, shuning uchun natijani tekshirish shart."
    },
    {
        "text": "Murakkab masalalarni yechishda AI ga 'Qadam-baqadam o'yla' (Think step by step / Chain of Thought) deyilsa nima yuz beradi?",
        "a": "AI javob berishdan bosh tortadi.",
        "b": "AI masalani mantiqiy bo'laklarga bo'lib tahlil qiladi va xatoliklar ehtimoli keskin kamayadi.",
        "c": "Kompyuter xotirasi to'lib qoladi.",
        "d": "Faqat 1 ta so'zdan iborat javob qaytadi.",
        "e": "Matn teskari tartibda chiqadi.",
        "correct": "B",
        "topic": "Chain-of-Thought (Bosqichma-bosqich fikrlash)",
        "expl": "Bosqichma-bosqich fikrlash AI ga oraliq xulosalar chiqarishga imkon beradi va to'g'ri yakuniy javobni kafolatlaydi."
    },
    {
        "text": "AI chatida 'Kontekst' (Context) nima?",
        "a": "Kompyuter sichqonchasining o'ng tugmasi.",
        "b": "Suhbat davomida avval yozilgan xabarlar, berilgan qoidalar va ma'lumotlar tarixi.",
        "c": "Faqat monitordagi piksellar soni.",
        "d": "Fayllarning fayl kengaytmasi.",
        "e": "Internet provayderining nomi.",
        "correct": "B",
        "topic": "Kontekst Tushunchasi",
        "expl": "Kontekst — AI eslab turadigan suhbat tarixi. Yangi savol berilganda AI oldingi javoblarni kontekstdan oladi."
    },
    {
        "text": "AI yordamida interaktiv tugma kodi yaratilganda, uni o'z kompyuteringizda qanday tekshirasiz?",
        "a": "Kodni qog'ozga ruchka bilan yozib qo'yish orqali.",
        "b": "Kodni `.html` kengaytmali faylga saqlab, istalgan brauzerda (Chrome, Edge) ikki marta bosib ochish orqali.",
        "c": "Faqat Word dasturida ochish orqali.",
        "d": "Faylni printerga yuborish orqali.",
        "e": "Kodni ovoz chiqarib o'qish orqali.",
        "correct": "B",
        "topic": "AI Kodini Ishga Tushirish",
        "expl": "HTML/CSS/JS fayllari mustaqil veb-sahifa bo'lib, har qanday brauzerda maxsus dastursiz ham darhol ochiladi."
    },
    {
        "text": "AI yozib bergan veb-sahifada tugma bosilganda ishlamasa, Vibecoding uslubida nima qilish kerak?",
        "a": "Kompyuterni qayta ishga tushirish kerak.",
        "b": "Brauzer konsolidagi (F12) xatolik matnini nusxalab, AI ga 'Bu kod ishlamadi, mana bu xato chiqdi, tuzatib ber' deb yuborish kerak.",
        "c": "Barcha fayllarni o'chirib tashlash kerak.",
        "d": "Dasturlashni butunlay tashlash kerak.",
        "e": "Tugmani qattiqroq bosish kerak.",
        "correct": "B",
        "topic": "AI Bilan Debugging (Tuzatish)",
        "expl": "Vibecoding madaniyatida xatolik matnini AI ga qayta taqdim etish eng tezkor va samarali tuzatish yo'lidir."
    },
    {
        "text": "Few-Shot Prompting (Misollar bilan o'rgatish) nima?",
        "a": "AI ga umuman savol bermaslik.",
        "b": "Prompt ichida AI ga 1–2 ta savol-javob namunalarini ko'rsatib, keyingi javobni ham xuddi shu uslubda talab qilish.",
        "c": "AI ga faqat bitta rasm yuborish.",
        "d": "Kompyuter ekranini rasmga olish.",
        "e": "Faqat inglizcha lug'atdan foydalanish.",
        "correct": "B",
        "topic": "Few-Shot Prompting",
        "expl": "Few-shot usulida namuna ko'rsatilganda AI siz kutgan aniq format va uslubni darhol tushunadi."
    },
    {
        "text": "AI yordamida rasm generatsiya qilishda (Midjourney / Bing Image Creator) sifatli natija olish uchun qaysi parametrlar yoziladi?",
        "a": "Faqat 'Chiroyli rasm qil'.",
        "b": "Obyekt, uning harakati, joylashgan muhiti, yorug'lik turi (masalan, kiberpank, neon, quyosh botishi) va badiiy uslub (3D, rasm, multfilm).",
        "c": "Faqat fayl hajmi (masalan, 5 megabayt).",
        "d": "Kompyuterning IP-manzili.",
        "e": "Faqat o'quvchining telefon raqami.",
        "correct": "B",
        "topic": "Rasm Generatsiyasi Promptlari",
        "expl": "Vizual promptlarda yorug'lik, uslub, atmosfera va detallar qanchalik aniq yozilsa, rasm shunchalik chiroyli chiqadi."
    },
    {
        "text": "Rasm generatsiyasida 'Salbiy prompt' (Negative Prompt) nima uchun kerak?",
        "a": "AI ning kayfiyatini buzish uchun.",
        "b": "Hosil bo'ladigan rasmda ko'rishni istamaydigan narsalarni (masalan, 'loyqa, xira, ortiqcha qo'llar') chiqarib tashlash uchun.",
        "c": "Faqat qora rangli rasmlar chizish uchun.",
        "d": "Rasmni o'chirib yuborish uchun.",
        "e": "Rasmni kichiklashtirish uchun.",
        "correct": "B",
        "topic": "Negative Prompt Tushunchasi",
        "expl": "Negative prompt orqali keraksiz elementlar filtrlanadi, bu esa tasvir sifatini oshiradi."
    },
    {
        "text": "AI dan olingan ma'lumotni maktab loyihasida ishlatishdan oldin nima qilish shart?",
        "a": "Hech narsa qilmasdan to'g'ridan-to'g'ri ko'chirib olish.",
        "b": "Faktlarni tekshirish (Fakt-cheking), tushunib o'qib chiqish va o'z so'zlari bilan boyitish.",
        "c": "Matnni do'stiga pullash.",
        "d": "Matnni o'chirib tashlash.",
        "e": "Faqat matnning rangini o'zgartirish.",
        "correct": "B",
        "topic": "Fakt-cheking va Mas'uliyat",
        "expl": "AI yordamchi vositadir; o'quvchi ma'lumotning to'g'riligini doimo darslik yoki ishonchli manbalardan tekshirishi kerak."
    },
    {
        "text": "AI ga javob formatini aniq belgilash (Output Formatting) qanday bo'ladi?",
        "a": "AI ga 'O'zing bilganingdek qil' deb yozish.",
        "b": "'Javobni 3 ustunli jadval ko'rinishida ber' yoki 'Faqat 5 ta raqamlangan bandda yoz' deb buyruq berish.",
        "c": "AI ga qarab qichqirish.",
        "d": "Klaviaturadan tasodifiy harflarni bosish.",
        "e": "Faqat rasm chizishni so'rash.",
        "correct": "B",
        "topic": "Natija Formatini Belgilash",
        "expl": "Formatni belgilash orqali ortiqcha gaplarsiz darhol jadval, ro'yxat yoki toza kod olish mumkin."
    },
    {
        "text": "Vibecoding jarayonida 'Iteratsiya' (Iteration) nimani anglatadi?",
        "a": "Kompyuterni format qilishni.",
        "b": "Loyihani bittada emas, ketma-ket qadamlar bilan AI ga savol berib, yaxshilab, sayqallab borish jarayonini.",
        "c": "Bir xil qo'shiqni qayta-qayta eshitishni.",
        "d": "Faqat bitta prompt bilan cheklanishni.",
        "e": "Dasturni o'chirishni.",
        "correct": "B",
        "topic": "Iterativ Rivojlanish",
        "expl": "Vibecoding doimiy muloqotdir: avval sodda skelet olinadi, keyin ranglar, keyin funksiyalar qo'shiladi."
    },
    {
        "text": "AI yordamida maktab taqdimoti tayyorlashda qaysi prompt eng samarali hisoblanadi?",
        "a": "'Prezentatsiya qil.'",
        "b": "'5-sinf o'quvchilari uchun 'Koinot va Sayyoralar' mavzusida 5 ta slayddan iborat reja, qisqa matnlar va slayd rasmlari uchun g'oyalar yozib ber.'",
        "c": "'Menga rasm ko'rsat.'",
        "d": "'Sayyora nima?'",
        "e": "'Faqat inglizcha slayd yoz.'",
        "correct": "B",
        "topic": "AI Bilan Prezentatsiya",
        "expl": "Mavzu, slaydlar soni va har bir slayd tarkibi ko'rsatilgan prompt tayyor va tartibli prezentatsiya beradi."
    },
    {
        "text": "AI chatida shaxsiy maxfiylikni (Privacy) saqlash uchun nima qilish taqiqlanadi?",
        "a": "AI dan matematika formulasini so'rash.",
        "b": "O'z uy manzili, telefon raqami, pasport ma'lumotlari yoki oilaviy parollarni AI ga yozish.",
        "c": "AI dan inglizcha so'z tarjimasini so'rash.",
        "d": "AI ga o'yin qoidalarini yozdirish.",
        "e": "AI bilan do'stona muloqot qilish.",
        "correct": "B",
        "topic": "AI da Maxfiylik Xavfsizligi",
        "expl": "Hech qachon shaxsiy maxfiy ma'lumotlarni ochiq AI botlariga kiritmaslik kerak."
    },
    {
        "text": "AI yordamida interaktiv mini-kalkulyator yaratishda qaysi texnologiyalar kodi so'raladi?",
        "a": "Faqat Photoshop fayli.",
        "b": "HTML (tuzilishi), CSS (chiroyli dizayni) va JavaScript (hisoblash mantig'i).",
        "c": "Faqat Word fayli.",
        "d": "Faqat MP3 audio fayli.",
        "e": "Hech qanday texnologiya kerak emas.",
        "correct": "B",
        "topic": "HTML, CSS, JS Triadasi",
        "expl": "Veb-loyihalarda HTML karkas, CSS tashqi ko'rinish, JavaScript esa harakat va hisob-kitobni ta'minlaydi."
    },
    {
        "text": "AI bergan kodni sinashda 'Live Server' vositasi qanday yordam beradi?",
        "a": "Kompyuter ekranini tozalaydi.",
        "b": "Koddagi o'zgarishlarni saqlashingiz bilan brauzerni avtomatik yangilab, natijani darhol ko'rsatadi.",
        "c": "Internet narxini pasaytiradi.",
        "d": "Klaviaturadagi xatolarni tuzatadi.",
        "e": "Faqat audio eshitishga yordam beradi.",
        "correct": "B",
        "topic": "Live Server Vositalari",
        "expl": "Live Server har bir `Ctrl+S` bosilganda natijani brauzerda qayta yuklamasdan jonli ko'rsatadi."
    },
    {
        "text": "AI ga 'Ushbu kodga tushunarli o'zbekcha izohlar (comments) qo'shib ber' deyilsa, dasturda nima paydo bo'ladi?",
        "a": "Dastur ishlamay qoladi.",
        "b": "Kod satrlari yonida nima vazifa bajarayotganini tushuntiruvchi yozuvlar (`// bu yerda ball oshadi`) paydo bo'ladi.",
        "c": "Sayt foniga rasm qo'yiladi.",
        "d": "Faqat katta harflar o'chib ketadi.",
        "e": "Dastur tezligi ikki barobar kamayadi.",
        "correct": "B",
        "topic": "Kodni Izohlash (Comments)",
        "expl": "Izohlar dasturchiga va boshqalarga kodning qanday ishlashini o'rganishda yordam beradi."
    },
    {
        "text": "AI yordamida logo (ramz) yaratishda promptga qanday sifatlar qo'shiladi?",
        "a": "'Iloji boricha ko'p rang va 100 ta detal bo'lsin.'",
        "b": "'Minimalistik, zamonaviy, vektorli, oq fonda, aniq geometrik shakllar va 2 ta uyg'un rang.'",
        "c": "'Faqat qorong'i va tushunarsiz bo'lsin.'",
        "d": "'Faqat matnsiz bo'lsin.'",
        "e": "'Faqat o'lchami 1 piksel bo'lsin.'",
        "correct": "B",
        "topic": "Logo Dizayni Promptlari",
        "expl": "Professional logotiplar sodda, minimalistik va taniqli bo'lishi kerak. Bu talablar promptda aytiladi."
    },
    {
        "text": "Bir nechta AI vositalarini birga ishlatish (Workflow) qanday bo'ladi?",
        "a": "Faqat bitta brauzer yorlig'ini ochish.",
        "b": "ChatGPT dan g'oya va matn olish -> Midjourney da rasm chizdirish -> Claude/Cursor da veb-sahifa kodini yaratish.",
        "c": "Barcha AI vositalarini o'chirib tashlash.",
        "d": "Faqat qog'ozda ishlash.",
        "e": "Faqat kalkulyatordan foydalanish.",
        "correct": "B",
        "topic": "AI Workflow (Ish Jarayoni)",
        "expl": "Eng zo'r vibecoderlar har bir vazifa uchun eng kuchli AI vositasini tanlab, ularni bitta zanjirga birlashtiradi."
    },
    {
        "text": "Yaratilgan interaktiv loyihani butun dunyoga ko'rsatish uchun uni qayerga bepul joylash (Deploy) mumkin?",
        "a": "Kompyuterning 'Savat' (Recycle Bin) papkasiga.",
        "b": "Vercel, Netlify yoki GitHub Pages platformalariga bir necha soniyada yuklab havola olish mumkin.",
        "c": "Faqat fleshkaga ko'chirib uyda saqlash kerak.",
        "d": "Faqat printerdan qog'ozga chiqarish kerak.",
        "e": "Saytni internetga joylash mumkin emas.",
        "correct": "B",
        "topic": "Veb Deploy Qilish",
        "expl": "Vercel va Netlify loyihalarni global internetda ishga tushirish uchun havola (URL) va QR kod beradi."
    },
    {
        "text": "Vibecoding bilan shug'ullanuvchi 5–6-sinf o'quvchisining eng muhim ko'nikmasi nima?",
        "a": "Kodni ko'r-ko'rona ko'chirish.",
        "b": "G'oyani aniq ifodalash, AI ga to'g'ri prompt berish, xatolarni tuzatish va yangi narsalarni yaratishga qiziqish.",
        "c": "Kun bo'yi ijtimoiy tarmoqlarda video ko'rish.",
        "d": "Kompyuter ekranini o'chirib qo'yish.",
        "e": "Faqat ingliz tili lug'atini yodlash.",
        "correct": "B",
        "topic": "Vibecoder Ko'nikmalari",
        "expl": "Vibecoding — bu ijodkorlik, mantiqiy fikrlash va AI vositalaridan to'g'ri foydalanib natija ko'rsatish san'atidir."
    }
]

QUESTIONS_5_6_RU = [
    {
        "text": "В чем заключается главная суть концепции Vibecoding?",
        "a": "В ручном наборе каждой строчки кода строго по памяти.",
        "b": "В быстром создании реальных работающих программ в диалоге с искусственным интеллектом (AI) через точные идеи и промпты.",
        "c": "Исключительно в игре в компьютерные игры.",
        "d": "В полном отключении компьютера от питания.",
        "e": "В полном отказе от клавиатуры.",
        "correct": "B",
        "topic": "Концепция Vibecoding",
        "expl": "Vibecoding объединяет творческий замысел человека со скоростью написания кода нейросетями."
    },
    {
        "text": "Как называется текстовый запрос или инструкция, которую пользователь отправляет нейросети?",
        "a": "Вирус",
        "b": "Промпт (Prompt / Запрос)",
        "c": "Драйвер",
        "d": "Пиксель",
        "e": "Сетевой кабель",
        "correct": "B",
        "topic": "Понятие Промпта",
        "expl": "Промпт — это текст, вопрос или команда, определяющая поведение и результат работы искусственного интеллекта."
    },
    {
        "text": "Из каких ключевых элементов строится действительно качественный и результативный промпт?",
        "a": "Достаточно написать всего одно короткое слово.",
        "b": "Роль (Кем выступает AI), Задача (Что сделать), Контекст (Условия) и Формат итогового ответа.",
        "c": "Текст должен быть написан исключительно заглавными буквами.",
        "d": "Писать можно строго на английском языке, русский язык запрещен.",
        "e": "В тексте нельзя ставить точки и знаки препинания.",
        "correct": "B",
        "topic": "Структура Качественного Промпта",
        "expl": "Эффективный промпт содержит четкую роль эксперта, конкретную цель, ограничения и формат ответа."
    },
    {
        "text": "Почему промпт 'Сделай мне сайт' плохой, а 'Создай интерактивную викторину по математике на HTML/CSS для 5 класса' — хороший?",
        "a": "Потому что второй промпт гораздо короче первого.",
        "b": "Потому что во втором промпте четко определены цель, предмет, целевая аудитория и стек технологий.",
        "c": "Потому что в первом промпте много орфографических ошибок.",
        "d": "Потому что нейросети не умеют работать с сайтами.",
        "e": "Оба промпта выдадут абсолютно одинаковый результат.",
        "correct": "B",
        "topic": "Точные vs Размытые Промпты",
        "expl": "Размытый промпт заставляет AI наугад придумывать детали, а точный промпт дает идеальный результат с первого раза."
    },
    {
        "text": "Зачем в начале промпта задают роль нейросети (Role Prompting, например: 'Ты опытный фронтенд-разработчик')?",
        "a": "Чтобы изменить цвет интерфейса чата.",
        "b": "Чтобы настроить модель на профессиональный стиль мышления, правильную терминологию и лучшие отраслевые практики.",
        "c": "Чтобы увеличить громкость колонок компьютера.",
        "d": "Чтобы повысить скорость домашнего интернета.",
        "e": "Исключительно для генерации картинок.",
        "correct": "B",
        "topic": "Задание Роли (Role Prompting)",
        "expl": "Ролевой контекст активирует нужные профессиональные паттерны в базе знаний нейросети."
    },
    {
        "text": "Что в сфере искусственного интеллекта называют 'Галлюцинацией' (Hallucination)?",
        "a": "Внезапное выключение монитора.",
        "b": "Уверенное сочинение несуществующих фактов, правил или данных, выдаваемых моделью за чистую правду.",
        "c": "Сверхбыструю работу видеокарты.",
        "d": "Неспособность нейросети генерировать смайлики.",
        "e": "Автоматическое обновление драйверов.",
        "correct": "B",
        "topic": "Галлюцинации Нейросетей",
        "expl": "Галлюцинация — это генерация ложной информации, поэтому ответы AI всегда требуют проверки человеком."
    },
    {
        "text": "Что происходит при добавлении в промпт фразы 'Думай шаг за шагом' (Think step by step / Chain of Thought)?",
        "a": "Нейросеть полностью отказывается отвечать.",
        "b": "Модель разбивает решение сложной задачи на последовательные логические шаги, многократно снижая риск ошибки.",
        "c": "Оперативная память компьютера моментально переполняется.",
        "d": "Ответ состоит строго из одного слова.",
        "e": "Текст ответа переворачивается задом наперед.",
        "correct": "B",
        "topic": "Пошаговое Рассуждение (Chain-of-Thought)",
        "expl": "Цепочка рассуждений позволяет AI делать промежуточные выводы и приходить к безошибочному решению."
    },
    {
        "text": "Что представляет собой 'Контекст' (Context) в окне диалога с искусственным интеллектом?",
        "a": "Правая кнопка компьютерной мыши.",
        "b": "История предыдущих сообщений, исходные файлы, правила и инструкции в рамках текущего диалога.",
        "c": "Общее количество точек на экране монитора.",
        "d": "Расширение файла на жестком диске.",
        "e": "Название интернет-браузера.",
        "correct": "B",
        "topic": "Понятие Контекста",
        "expl": "Контекст — это оперативная память диалога, благодаря которой AI помнит тему беседы и предыдущие задачи."
    },
    {
        "text": "Как проверить работоспособность веб-страницы или интерактивной кнопки, код которой написал AI?",
        "a": "Переписать весь код шариковой ручкой в тетрадь.",
        "b": "Сохранить код в файл с расширением `.html` и открыть его двойным кликом в любом браузере (Chrome, Edge).",
        "c": "Открыть файл исключительно в программе Microsoft Word.",
        "d": "Отправить файл на печать на принтер.",
        "e": "Прочитать текст кода вслух в микрофон.",
        "correct": "B",
        "topic": "Запуск Кода от AI",
        "expl": "Файлы HTML открываются стандартным браузером на любом компьютере и смартфоне без дополнительного ПО."
    },
    {
        "text": "Если код от нейросети не работает или выдает ошибку, как поступить в парадигме Vibecoding?",
        "a": "Срочно выдернуть шнур питания из розетки.",
        "b": "Скопировать текст ошибки из консоли браузера (F12) и отправить в AI с запросом: 'Кнопка не нажимается, вот ошибка, исправь код'.",
        "c": "Удалить все файлы с компьютера.",
        "d": "Навсегда бросить программирование.",
        "e": "Нажимать на кнопку мыши с максимальной силой.",
        "correct": "B",
        "topic": "AI-Отладка (Debugging)",
        "expl": "В культуре Vibecoding передача точного текста ошибки в AI является самым быстрым способом получения рабочего фикса."
    },
    {
        "text": "Что такое Few-Shot Prompting (обучение на примерах прямо в запросе)?",
        "a": "Полный отказ от использования текста.",
        "b": "Добавление в текст промпта 1–2 готовых образцов 'вопрос-ответ', чтобы модель сформировала ответ в таком же стиле.",
        "c": "Отправка нейросети только одной картинки.",
        "d": "Снимок экрана монитора.",
        "e": "Использование только англо-русского словаря.",
        "correct": "B",
        "topic": "Few-Shot Prompting",
        "expl": "Примеры прямо в промпте наглядно задают нейросети формат, структуру и тон ответа без долгих объяснений."
    },
    {
        "text": "Какие параметры необходимо описать в промпте для генерации красивой иллюстрации в Midjourney или Bing Creator?",
        "a": "Только короткую фразу 'Сделай красиво'.",
        "b": "Объект, окружение, действие, тип освещения (неон, закат, кинематографичный свет) и стиль (3D-рендер, акварель, пиксель-арт).",
        "c": "Исключительно размер файла в мегабайтах.",
        "d": "IP-адрес домашнего роутера.",
        "e": "Номер мобильного телефона пользователя.",
        "correct": "B",
        "topic": "Промпты для Генерации Изображений",
        "expl": "Чем точнее описаны стиль, свет, ракурс и композиция, тем привлекательнее получается сгенерированное изображение."
    },
    {
        "text": "Для чего в генерации изображений используется 'Отрицательный промпт' (Negative Prompt)?",
        "a": "Чтобы разозлить искусственный интеллект.",
        "b": "Чтобы исключить появление нежелательных деталей на картинке (например: 'размытость, лишние пальцы, водяные знаки').",
        "c": "Чтобы рисовать только черным цветом.",
        "d": "Чтобы удалить файл с диска.",
        "e": "Чтобы уменьшить разрешение картинки.",
        "correct": "B",
        "topic": "Отрицательный Промпт (Negative)",
        "expl": "Отрицательный промпт фильтрует артефакты и нежелательные объекты, повышая чистоту композиции."
    },
    {
        "text": "Что обязан сделать ученик перед использованием сгенерированного AI текста в школьном проекте?",
        "a": "Скопировать текст не читая и сдать учителю.",
        "b": "Проверить факты (фактчекинг), вдумчиво прочитать материал и дополнить его своими словами и мыслями.",
        "c": "Продать текст однокласснику.",
        "d": "Сразу же удалить файл.",
        "e": "Просто поменять цвет шрифта на синий.",
        "correct": "B",
        "topic": "Фактчекинг и Ответственность",
        "expl": "AI — умный ассистент, но ответственность за достоверность информации всегда лежит на человеке."
    },
    {
        "text": "Как в промпте явно задать формат вывода информации (Output Formatting)?",
        "a": "Написать модели: 'Сделай как-нибудь сам'.",
        "b": "Добавить четкую инструкцию: 'Оформи ответ в виде таблицы из 3 колонок' или 'Ответь строго списком из 5 пунктов'.",
        "c": "Громко закричать в микрофон.",
        "d": "Нажать случайные клавиши на клавиатуре.",
        "e": "Попросить нарисовать кружок.",
        "correct": "B",
        "topic": "Фиксация Формата Ответа",
        "expl": "Четкое указание формата отсекает лишние рассуждения и выдает готовую структурированную таблицу или список."
    },
    {
        "text": "Что в культуре Vibecoding означает термин 'Итерация' (Iteration)?",
        "a": "Полное форматирование операционной системы.",
        "b": "Пошаговое улучшение проекта через серию последовательных вопросов к AI: от простого скелета к идеальному интерфейсу.",
        "c": "Многократное прослушивание одной песни.",
        "d": "Ограничение работы строго одним запросом.",
        "e": "Удаление программного кода.",
        "correct": "B",
        "topic": "Итеративная Разработка",
        "expl": "Vibecoding — это непрерывный диалог: сначала генерируется база, затем добавляются стили, логика и анимация."
    },
    {
        "text": "Какой промпт эффективнее всего создаст структуру для школьной презентации?",
        "a": "'Сделай презентацию.'",
        "b": "'Составь план презентации на 5 слайдов для 5 класса на тему 'Планеты Солнечной системы': текст для каждого слайда и идеи для иллюстраций.'",
        "c": "'Покажи картинку космоса.'",
        "d": "'Что такое планета?'",
        "e": "'Напиши текст на латыни.'",
        "correct": "B",
        "topic": "Презентации с Помощью AI",
        "expl": "Указание темы, числа слайдов и аудитории позволяет получить готовую структуру для каждого экрана."
    },
    {
        "text": "Какое ключевое правило приватности (Privacy) нельзя нарушать при общении с публичными нейросетями?",
        "a": "Нельзя спрашивать правила правописания.",
        "b": "Категорически запрещено передавать свой домашний адрес, телефон, пароли или паспортные данные семьи.",
        "c": "Нельзя просить перевести текст на иностранный язык.",
        "d": "Запрещено придумывать сюжеты для сказок.",
        "e": "Нельзя здороваться с чат-ботом.",
        "correct": "B",
        "topic": "Приватность и Безопасность",
        "expl": "Персональные и конфиденциальные данные никогда не должны попадать в публичные чаты с AI."
    },
    {
        "text": "Код каких трех базовых веб-технологий запрашивают у AI для создания интерактивного калькулятора?",
        "a": "Файлов программы Photoshop.",
        "b": "HTML (структура каркаса), CSS (стильный внешний вид) и JavaScript (вычислительная логика).",
        "c": "Документа программы Microsoft Word.",
        "d": "Аудиозаписи формата MP3.",
        "e": "Никакие технологии не требуются.",
        "correct": "B",
        "topic": "Триада HTML, CSS и JS",
        "expl": "HTML формирует элементы страницы, CSS задает цвета и отступы, а JavaScript выполняет расчеты."
    },
    {
        "text": "Какую пользу приносит расширение 'Live Server' при разработке веб-страниц с AI?",
        "a": "Очищает экран ноутбука от пыли.",
        "b": "Мгновенно обновляет страницу в браузере при каждом сохранении файла, сразу показывая результат работы кода.",
        "c": "Снижает ежемесячную плату за интернет.",
        "d": "Исправляет орфографические ошибки в словах.",
        "e": "Включает фоновую музыку.",
        "correct": "B",
        "topic": "Инструмент Live Server",
        "expl": "Live Server экономит время: каждое сохранение кода (`Ctrl+S`) сразу отображается в окне браузера."
    },
    {
        "text": "Что произойдет в исходном коде, если попросить AI: 'Добавь к каждой функции подробные комментарии'?",
        "a": "Программа полностью перестанет работать.",
        "b": "Рядом со строчками кода появятся понятные пояснения на человеческом языке (`// здесь увеличивается счетчик`), объясняющие логику.",
        "c": "На фоне веб-сайта появится видеоклип.",
        "d": "Сотрутся все заглавные буквы.",
        "e": "Скорость программы упадет в два раза.",
        "correct": "B",
        "topic": "Комментарии в Коде",
        "expl": "Комментарии помогают разработчику и другим людям быстро разобраться, как работает каждая часть программы."
    },
    {
        "text": "Какие требования к стилю логотипа следует указать в промпте нейросети-художнику?",
        "a": "'Используй как можно больше мелких деталей и 50 разных цветов.'",
        "b": "'Минималистичный, векторный, современный стиль, на чистом белом фоне, с четкими геометрическими формами и 2 гармоничными цветами.'",
        "c": "'Сделай все размытым и темным.'",
        "d": "'Логотип без форм и цветов.'",
        "e": "'Размер ровно 1 пиксель.'",
        "correct": "B",
        "topic": "Промпты для Логотипов",
        "expl": "Хороший логотип узнаваем и лаконичен. Минимализм и чистый фон — стандарты современного брендинга."
    },
    {
        "text": "В чем заключается создание комплексного рабочего процесса (AI Workflow)?",
        "a": "В открытии всего одной вкладки браузера.",
        "b": "В объединении сильных сторон разных сервисов: идея в ChatGPT -> арт в Midjourney -> генерация веб-кода в Claude/Cursor.",
        "c": "В удалении всех программ с компьютера.",
        "d": "В отказе от использования интернета.",
        "e": "В решении задач только на калькуляторе.",
        "correct": "B",
        "topic": "Комплексный AI Workflow",
        "expl": "Эффективный vibecoder использует лучший инструмент под каждую подзадачу, собирая их в единую цепочку."
    },
    {
        "text": "Куда можно за секунды бесплатно опубликовать (задеплоить) созданный веб-проект, чтобы открыть его на телефоне по QR-коду?",
        "a": "В корзину рабочего стола Windows.",
        "b": "На хостинг-платформы Vercel, Netlify или GitHub Pages, получив готовую публичную ссылку (URL).",
        "c": "Только скопировать на старую дискету.",
        "d": "Распечатать на бумаге формата А4.",
        "e": "Публикация сайтов в интернете невозможна.",
        "correct": "B",
        "topic": "Публикация (Deploy)",
        "expl": "Платформы Vercel и Netlify дают глобальную ссылку и QR-код для демонстрации проекта друзьям и родителям."
    },
    {
        "text": "Какое главное качество отличает успешного юного Vibecoder-а 5–6 класса?",
        "a": "Слепое копирование чужих текстов без понимания.",
        "b": "Умение четко формулировать свои идеи, грамотно задавать промпты AI, исправлять ошибки и стремление создавать полезные проекты.",
        "c": "Бессмысленное листание коротких видеороликов весь день.",
        "d": "Боязнь задавать вопросы компьютеру.",
        "e": "Механическое заучивание терминов наизусть.",
        "correct": "B",
        "topic": "Навыки Vibecoder-а",
        "expl": "Vibecoding развивает продуктовое мышление: от зарождения идеи в голове до ее воплощения в коде вместе с AI."
    }
]

print("Grade 5-6 TRUE Vibecoding test data loaded (25 questions UZ & RU). Teacher: Ismoiljon Usmonov.")
