#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
7–8-Sinf: 25 Savolli Amaliy Vibecoding, UI Prototip va AI Ish Qurollari Testi
O'qituvchi: Ismoiljon Usmonov · Target International School, Yunusobod
Uzbek va Russian variantlari (5 ta variant: A, B, C, D, E)
"""

META_7_8_UZ = {
    "school_name": "TARGET INTERNATIONAL SCHOOL — YUNUSOBOD",
    "teacher_name": "Ismoiljon Usmonov",
    "exam_title": "7–8-SINF: AMALIY VIBECODING, UI PROTOTIP VA AI WORKFLOW",
    "track_title": "Applied Vibecoding & UI Prototyping Track · O'qituvchi: Ismoiljon Usmonov",
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

KEYS_META_7_8_UZ = {
    "heading": "JAVOBLAR KALITI VA BAHOLASH MEZONI",
    "subheading": "O'qituvchi: Ismoiljon Usmonov · 7–8-sinf Vibecoding rasmiy kaliti (25 ta savol)",
    "table_headers": ["№", "Kalit", "Mavzu / Kompetensiya", "Izoh va Tushuntirish"],
    "scale_heading": "Rasmiy 25 Ballik Baholash Shkalasi:",
    "rubric_tiers": [
        {"grade": "A'lo (5)", "range": "22 – 25 ball", "desc": "Cursor, UI prototiplash, debugging va AI workflow bo'yicha chuqur amaliy bilim"},
        {"grade": "Yaxshi (4)", "range": "18 – 21 ball", "desc": "Prompt tuzilishi va komponentli dasturlash yaxshi o'zlashtirilgan"},
        {"grade": "Qoniqarli (3)", "range": "13 – 17 ball", "desc": "Kontekst boshqaruvi va refaktoringni takrorlash lozim"},
        {"grade": "Qoniqarsiz (2)", "range": "0 – 12 ball", "desc": "Vibecoding amaliyoti qayta o'rganilishi zarur"}
    ]
}

META_7_8_RU = {
    "school_name": "TARGET INTERNATIONAL SCHOOL — ЮНУСАБАД",
    "teacher_name": "Исмоилжон Усмонов",
    "exam_title": "7–8 КЛАСС: ПРИКЛАДНОЙ VIBECODING, UI-ПРОТОТИПИРОВАНИЕ И AI WORKFLOW",
    "track_title": "Applied Vibecoding & UI Prototyping Track · Преподаватель: Исмоилжон Усмонов",
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

KEYS_META_7_8_RU = {
    "heading": "КЛЮЧИ ОТВЕТОВ И КРИТЕРИИ ОЦЕНИВАНИЯ",
    "subheading": "Преподаватель: Исмоилжон Усмонов · Официальный ключ Vibecoding (7–8 класс, 25 вопросов)",
    "table_headers": ["№", "Ключ", "Тема / Компетенция", "Пояснение и Обоснование"],
    "scale_heading": "Официальная 25-балльная шкала оценивания:",
    "rubric_tiers": [
        {"grade": "Отлично (5)", "range": "22 – 25 баллов", "desc": "Глубокое понимание Cursor, прототипирования UI, отладки и AI-воркфлоу"},
        {"grade": "Хорошо (4)", "range": "18 – 21 балл", "desc": "Хорошее владение структурой промптов и компонентным подходом"},
        {"grade": "Удовлетворительно (3)", "range": "13 – 17 баллов", "desc": "Требуется повторение управления контекстом и рефакторинга"},
        {"grade": "Неудовлетворительно (2)", "range": "0 – 12 баллов", "desc": "Необходимо повторное изучение практического Vibecoding"}
    ]
}

QUESTIONS_7_8_UZ = [
    {
        "text": "Vibecoding yondashuvida dasturchining asosiy kuchi nimada namoyon bo'ladi?",
        "a": "Kodni qorong'i xonada faqat ko'z bilan terishda.",
        "b": "Aniq arxitektura qurish, AI ga to'g'ri texnik topshiriq berish, hosil bo'lgan kodni tekshirish (Vibe-checking) va loyihani tezkor prototipdan tayyor mahsulotga yetkazishda.",
        "c": "Barcha sun'iy intellekt vositalarini o'chirib qo'yishda.",
        "d": "Faqat ingliz tili darsligini o'qishda.",
        "e": "Klaviaturadagi harflarni yoddan aytib berishda.",
        "correct": "B",
        "topic": "Vibecoding Falsafasi",
        "expl": "Vibecoder sintaksis mexanikasiga emas, balki g'oya, arxitektura va AI natijasini tekshirib sayqallashga e'tibor qaratadi."
    },
    {
        "text": "Dasturlash uchun eng mukammal prompt anatomiyasi qaysi 5 ta asosiy bo'limdan iborat?",
        "a": "Kirish, Xulosa, Rasm, Qo'shiq, Video.",
        "b": "Rol (Role), Kontekst (Context), Aniq Vazifa (Task), Cheklovlar (Constraints) va Kutilayotgan Natija Formati (Output Format).",
        "c": "Faqat foydalanuvchi ismi va paroli.",
        "d": "Faqat kompyuter modeli va operatsion tizim.",
        "e": "Hech qanday bo'lim kerak emas, 1 ta jumla yetarli.",
        "correct": "B",
        "topic": "Dasturlash Prompti Anatomiyasi",
        "expl": "Ushbu 5 element AI ga loyiha chegaralarini to'liq ko'rsatib, ortiqcha xatolarning 90% ini oldini oladi."
    },
    {
        "text": "Cursor va zamonaviy AI IDE muhitlarida `Cmd+K` (yoki `Ctrl+K`) tugmasi qanday vazifani bajaradi?",
        "a": "Kompyuterni o'chiradi.",
        "b": "Belgilangan kod bo'lagi ustida bevosita AI ga buyruq berish, yangi funksiya qo'shish yoki kodni joyida tahrirlash (inline edit) oynasini ochadi.",
        "c": "Faqat shrift hajmini kattalashtiradi.",
        "d": "Faylni butunlay o'chirib tashlaydi.",
        "e": "Brauzer oynasini yopadi.",
        "correct": "B",
        "topic": "Cursor IDE va Inline Edit (Cmd+K)",
        "expl": "Inline AI tahrirlovchisi kod ichida to'g'ridan-to'g'ri o'zgartirishlar kiritish uchun eng tezkor vositadir."
    },
    {
        "text": "v0.dev va Bolt.new kabi zamonaviy Vibecoding platformalarining asosiy mo'jizasi nimada?",
        "a": "Ular internet talab qilmaydi.",
        "b": "Faqat bitta tabiiy tildagi matnli prompt orqali bir necha soniyada to'liq zamonaviy interfeys (React/Tailwind UI) va ishlovchi veb-prototip generatsiya qilib beradi.",
        "c": "Faqat qora va oq rasmlar chizadi.",
        "d": "Kompyuter klaviaturasini tozalaydi.",
        "e": "Faqat Word fayllarni o'qiydi.",
        "correct": "B",
        "topic": "v0.dev va Bolt.new Platformalari",
        "expl": "Ushbu vositalar 'Prompt-to-UI' inqilobini yaratdi: g'oyadan ishlovchi veb-interfeysgacha bo'lgan vaqt bir daqiqaga qisqardi."
    },
    {
        "text": "Veb-sayt yaratishda 'Komponentli yondashuv' (Component-driven prompting) nima uchun zarur?",
        "a": "AI ga birdaniga butun saytni aytish osonroq bo'lgani uchun.",
        "b": "AI bir vaqtning o'zida hamma narsani mukammal qila olmaydi; avval alohida Navbar, keyin Hero banner, keyin Mahsulot kartalarini navbatma-navbat yaratish xatolarni yo'qotadi.",
        "c": "Sayt hajmini sun'iy ravishda kattalashtirish uchun.",
        "d": "Faqat bitta tugma bilan cheklanish uchun.",
        "e": "Faqat rasmlar yuklash uchun.",
        "correct": "B",
        "topic": "Komponentli Yondashuv",
        "expl": "Katta loyihani kichik mustaqil komponentlarga (bloklarga) bo'lib prompt berish Vibecoding ning oltin qoidasidir."
    },
    {
        "text": "Cursor da `@Files` yoki `@Codebase` teglari nima vazifani bajaradi?",
        "a": "Fayllarni internetga sotish.",
        "b": "AI ga butun loyihaning kerakli fayllarini kontekst sifatida aniq ko'rsatish, natijada AI boshqa fayllardagi o'zgaruvchilar va funksiyalarni to'g'ri tushunadi.",
        "c": "Koddagi barcha so'zlarni bosh harfga aylantirish.",
        "d": "Litsenziya sotib olish.",
        "e": "Klaviaturani bloklash.",
        "correct": "B",
        "topic": "Kontekst Boshqaruvi (@Files)",
        "expl": "@ belgilari orqali kerakli fayllar AI ga uzatiladi, bu esa noto'g'ri o'zgaruvchi va kutubxona nomlarini to'qib chiqarishni to'xtatadi."
    },
    {
        "text": "AI ga zamonaviy dizayn tizimi (Design System) berish uchun promptga nimalar kiritiladi?",
        "a": "Faqat 'Chiroyli ranglar qo'y'.",
        "b": "Ranglar palitrasi (masalan, asosiy Navy `#00214A`, aksent Cyan `#0284C7`), shriftlar oilasi, kartalar uchun 16px radius va Tailwind CSS klasslari.",
        "c": "Faqat o'quvchining sevimli avtomobili nomi.",
        "d": "Faqat kompyuter monitori diagonali.",
        "e": "Hech qanday rang ko'rsatilmasligi kerak.",
        "correct": "B",
        "topic": "AI Dizayn Tizimi va Ranglar",
        "expl": "Aniq hex ranglar va padding o'lchamlari berilganda AI bir xil uslubdagi zamonaviy SaaS darajasidagi dizayn chiqaradi."
    },
    {
        "text": "AI yozgan kodda tugma bosilganda qizil xatolik chiqsa, Vibecoding uslubida qanday prompt beriladi?",
        "a": "'Sen yomon AIsan, ishlamayapti.'",
        "b": "'Mana brauzer konsolidagi to'liq xatolik: `Uncaught TypeError: Cannot read properties of undefined (reading 'addEventListener') at app.js:14`. Mening HTML va JS kodim ilova qilindi. Sababini tushuntir va to'g'rilangan kodni ber.'",
        "c": "'Hammasini o'chirib boshqatdan yoz.'",
        "d": "'Menga yangi kompyuter kerak.'",
        "e": "'Faqat CSS kodini ko'rsat.'",
        "correct": "B",
        "topic": "AI Bilan Console Error Debugging",
        "expl": "Xatolik satri va uning to'liq matnini uzatish AI ga bir zumda DOM elementi qayerda topilmaganini ko'rsatib beradi."
    },
    {
        "text": "Kodni tozalash va takomillashtirishda 'Refaktoring' prompti qanday bo'lishi kerak?",
        "a": "'Kodni o'chir.'",
        "b": "'Ushbu kodning tashqi ishlashini o'zgartirmasdan, DRY prinsipiga muvofiq takrorlanuvchi bloklarni alohida funksiyalarga ajrat, o'zgaruvchilarga tushunarli nomlar ber va kodga izohlar qo'sh.'",
        "c": "'Faqat shrift rangini o'zgartir.'",
        "d": "'Kodni faqat 1 qatorga joyla.'",
        "e": "'Kodni rus tiliga tarjima qil.'",
        "correct": "B",
        "topic": "Kodni Refaktoring Qilish",
        "expl": "Refaktoring kodning tuzilishini sifatli, o'qilishi oson va xatosiz qiladi, uning tashqi natijasiga ta'sir qilmaydi."
    },
    {
        "text": "Veb-ilovada sinov uchun foydalanuvchilar ro'yxati kerak bo'lsa, AI ga qanday 'Mock Data' so'rovi beriladi?",
        "a": "'Menga odamlar kerak.'",
        "b": "'O'zbekistonlik 10 ta o'quvchi uchun JSON formatida soxta ma'lumotlar (id, ism, familiya, yosh, ball, avatar rasmi havolasi) massivini yaratib ber.'",
        "c": "'Do'stlarimning telefonini top.'",
        "d": "'Haqiqiy pasport ma'lumotlarini qidir.'",
        "e": "'Faqat bitta ism yoz.'",
        "correct": "B",
        "topic": "Mock Data (Soxta Ma'lumotlar) Generatsiyasi",
        "expl": "AI soniyalar ichida mukammal JSON massivlarini yaratib beradi, bu esa dasturchiga haqiqiy server bo'lmaganda ham interfeysni sinash imkonini beradi."
    },
    {
        "text": "AI ga saytni barcha qurilmalarga moslashtirish (Responsive Design) buyrug'i qanday beriladi?",
        "a": "'Saytni kichik qil.'",
        "b": "'Sayt mobil telefonlarda (iPhone), planshetlarda va katta monitorlarda birdek qulay ochilishi uchun CSS Media Queries yoki Tailwind `sm:`, `md:`, `lg:` klasslaridan foydalan.'",
        "c": "'Faqat noutbukda ochilsin.'",
        "d": "'Barcha rasmlarni o'chirib tashla.'",
        "e": "'Sahifani qora mavzuga o'tkaz.'",
        "correct": "B",
        "topic": "Responsive Dizayn Promptlari",
        "expl": "Responsive buyruq sayt elementlarining turli ekran eniga qarab moslashuvchan (elastik) joylashishini ta'minlaydi."
    },
    {
        "text": "AI yordamida tashqi API (masalan, Jonli Valyuta Kurslari) ulashda qanday prompt beriladi?",
        "a": "'Menga pul ber.'",
        "b": "'Ochiq valyuta API sidan (masalan, open.er-api.com) so'nggi kurslarni `fetch()` orqali oladigan, yuklanish holatini (Loading spinner) va xatolik yuz bergandagi xabarni ko'rsatuvchi funksiya yozib ber.'",
        "c": "'Bank hisobini och.'",
        "d": "'Kriptovalyuta sotib ol.'",
        "e": "'Faqat valyuta ramzini chiz.'",
        "correct": "B",
        "topic": "AI Bilan API Integratsiyasi",
        "expl": "To'liq promptda so'rov usuli (`fetch`), yuklanish indikatori va xatoliklarni ushlash (`try/catch`) shartlari bo'lishi kerak."
    },
    {
        "text": "Few-Shot kod yozdirishning Zero-Shot dan ustunligi nimada?",
        "a": "Zero-Shot har doim pullik bo'ladi.",
        "b": "AI ga loyihangizdagi mavjud kod uslubidan namuna (Few-Shot) ko'rsatsangiz, u yangi modulni loyihangizning aynan o'sha arxitektura qoidalariga moslab yozib beradi.",
        "c": "Few-Shot kompyuterni tezroq o'chiradi.",
        "d": "Few-Shot faqat HTML da ishlaydi.",
        "e": "Hech qanday farqi yo'q.",
        "correct": "B",
        "topic": "Few-Shot vs Zero-Shot Kodlash",
        "expl": "Misollar berilganda AI loyihaning mavjud konvensiyalari va o'zgaruvchi nomlash qoidalariga 100% moslashadi."
    },
    {
        "text": "AI ga cheklovlar (Constraints) qo'yish nima uchun muhim?",
        "a": "AI ning tezligini ataylab sekinlashtirish uchun.",
        "b": "AI o'zboshimchalik bilan ortiqcha kutubxonalar (masalan, og'ir jQuery yoki React) qo'shib yubormasligi uchun 'Faqat sof Vanilla JavaScript ishlat, tashqi kutubxonalarsiz' deb chegaralash uchun.",
        "c": "Faqat inglizcha kod yozdirish uchun.",
        "d": "Kodni qisqartirishni taqiqlash uchun.",
        "e": "Faqat 10 ta belgi ishlatish uchun.",
        "correct": "B",
        "topic": "Prompt Cheklovlari (Constraints)",
        "expl": "Cheklovlar qo'yilmasa, AI loyihaga keraksiz uchinchi tomon vositalarini tiqishtirib, loyihani og'irlashtirishi mumkin."
    },
    {
        "text": "AI tomonidan 'Hallucinated Package' (to'qib chiqarilgan paket) xatosi nima?",
        "a": "AI yangi kompyuter sotib olishni talab qiladi.",
        "b": "AI kod yozayotganda aslida internetda mavjud bo'lmagan, soxta npm kutubxona nomini (masalan, `npm install super-cool-game-physics-2026`) o'ylab topib, kodga kiritib yuborishi.",
        "c": "Koddagi barcha sonlarning yo'qolib qolishi.",
        "d": "Sayt fonining o'z-o'zidan o'zgarishi.",
        "e": "Internet provayderining almashishi.",
        "correct": "B",
        "topic": "Soxta Paketlar Gallyutsinatsiyasi",
        "expl": "AI kutubxona nomlarini to'qib chiqarishi mumkin. Har qanday tavsiya qilingan paket `npmjs.com` dan tekshirib o'rnatilishi shart."
    },
    {
        "text": "Vibe-checking jarayonida dasturchi nimalarni sinovdan o'tkazadi?",
        "a": "Faqat kod chiroyli ko'rinishini.",
        "b": "Barcha tugmalar bosilishi, chegaraviy holatlar (Edge Cases: bo'sh matn kiritilsa nima bo'ladi), mobil ko'rinish va animatsiyalarning silliqligini real hayotda sinab ko'radi.",
        "c": "Faqat kompyuter ekranining yorqinligini.",
        "d": "Faqat o'yin ballari rekordini.",
        "e": "Hech narsani tekshirmaydi, AI ga 100% ishonadi.",
        "correct": "B",
        "topic": "Vibe-Checking va Edge Cases",
        "expl": "Vibe-checking — bu mahsulotni haqiqiy foydalanuvchi ko'zi bilan sinash va chekka holatlardagi xatolarni aniqlashdir."
    },
    {
        "text": "AI yordamida Git commit xabarlarini professional yozish (Conventional Commits) qanday bo'ladi?",
        "a": "'update', 'tuzatdim', 'tamom'.",
        "b": "'feat: add interactive FUT chemistry calculator with visual synergy links' yoki 'fix: resolve navbar overlap issue on mobile screens'.",
        "c": "Faqat smayliklar qo'yish.",
        "d": "Faqat bitta nuqta qo'yish.",
        "e": "Bugungi ob-havoni yozish.",
        "correct": "B",
        "topic": "Git Conventional Commits",
        "expl": "Professional commitlar qisqa prefiks (`feat:`, `fix:`, `style:`) va aniq bajarilgan ish tavsifi bilan yoziladi."
    },
    {
        "text": "AI ga ovozli assistent (Target Jarvis) yaratish buyrug'i qanday beriladi?",
        "a": "'Menga gapiruvchi robot qil.'",
        "b": "'HTML va JS da brauzerning Web Speech API (`webkitSpeechRecognition` va `speechSynthesis`) dan foydalanuvchi, mikrofondan buyruq eshitib, ovoz chiqarib javob qaytaruvchi interfeys yarat.'",
        "c": "'Menga MP3 musiqa qo'y.'",
        "d": "'Telefon raqamiga qo'ng'iroq qil.'",
        "e": "'Faqat rasm chiz.'",
        "correct": "B",
        "topic": "Web Speech API Prompti",
        "expl": "Brauzerning aniq Web API texnologiyasi ko'rsatilganda AI kutubxonalarsiz sof ovozli interfeys kodi yozib beradi."
    },
    {
        "text": "AI dan Kiber-Reaksiya mini-o'yinini so'rashda qaysi mantiqiy shartlar yoziladi?",
        "a": "'Menga o'yin qil.'",
        "b": "'Ekranda tasodifiy (1-5 soniya oralig'ida) qizil rang yashilga aylansin; o'yinchi bosgan paytdagi millisekundlar farqini (`performance.now()`) o'lchab, reaksiya tezligini chiqarsin.'",
        "c": "'Faqat o'yin logotipini chiz.'",
        "d": "'Faqat hisoblagich qo'y.'",
        "e": "'Klaviaturadagi barcha tugmalarni yoq.'",
        "correct": "B",
        "topic": "Mantiqiy O'yin Prompti",
        "expl": "Tasodifiy taymer, rang almashishi va millisekundlar hisobi aniq ko'rsatilganda o'yin mukammal generatsiya qilinadi."
    },
    {
        "text": "Loyiha uchun professional README.md hujjatini yaratishda AI ga nima topshiriladi?",
        "a": "Faqat dasturchining rasmini qo'yish.",
        "b": "Loyiha tavsifi, imkoniyatlari (Features), o'rnatish va ishga tushirish yo'riqnomasi, texnologiyalar ro'yxati va ekran rasmlari uchun joylarni Markdown formatida tuzish.",
        "c": "Faqat bitta satr matn yozish.",
        "d": "Word faylini o'chirish.",
        "e": "Faqat do'stlarning ismini yozish.",
        "correct": "B",
        "topic": "README.md Hujjatlashtirish",
        "expl": "Yaxshi README hujjati loyihani boshqa dasturchilar va ish beruvchilarga professional tarzda tanishtiradi."
    },
    {
        "text": "Vibecoding-da 'Kodni tushuntirib ber' (Explain Code) promptining o'quvchi uchun eng katta foydasi nima?",
        "a": "Kodni umuman o'qimaslik imkonini beradi.",
        "b": "AI murakkab kodning har bir qatori nima qilayotganini oddiy so'zlar bilan tushuntiradi, bu esa o'quvchining dasturlash bilimini chuqurlashtiradi.",
        "c": "Kompyuter ekranini o'chiradi.",
        "d": "Faqat xatolar sonini oshiradi.",
        "e": "Dasturni pullik qiladi.",
        "correct": "B",
        "topic": "AI Orqali O'rganish (Explain Code)",
        "expl": "Vibecoder shunchaki kod ko'chirmaydi, AI dan kodning ishlash mantiqini so'rab, o'z bilimini oshirib boradi."
    },
    {
        "text": "Freelance platformasida (Upwork/Fiverr) mijozdan kelgan qisqa texnik talabni tahlil qilishda AI dan qanday foydalaniladi?",
        "a": "Mijozning profilini bloklash uchun.",
        "b": "Mijoz xabarini AI ga kiritib, loyiha uchun zarur qismlar ro'yxatini, taxminiy bajarilish vaqtini va mos taklif (Proposal) xatini yozdirish uchun.",
        "c": "Faqat pulni hisoblash uchun.",
        "d": "Mijozga shaxsiy parollarni yuborish uchun.",
        "e": "Xabarni o'chirib yuborish uchun.",
        "correct": "B",
        "topic": "Freelance va Mijoz Bilan Muloqot",
        "expl": "AI mijozning noaniq xabarlarini aniq texnik vazifalarga ajratib, professional javob tayyorlashda yordam beradi."
    },
    {
        "text": "Vercel platformasiga loyihani deploy qilishda qanday texnik ustunlik mavjud?",
        "a": "Sayt faqat 1 soat ishlaydi.",
        "b": "GitHub repozitoriyasiga har safar yangi commit yuborilganda, Vercel avtomatik ravishda yangi versiyani global internetga chiqaradi va bepul SSL (HTTPS) beradi.",
        "c": "Kompyuterni har kuni format qilish kerak bo'ladi.",
        "d": "Faqat bitta foydalanuvchi kira oladi.",
        "e": "Vercel faqat pullik bo'ladi.",
        "correct": "B",
        "topic": "Avtomatik Vercel Deploy",
        "expl": "Vercel Git bilan to'liq integratsiyalashgan bo'lib, avtomatik CI/CD quvuri va tezkor global CDN serverlarini taqdim etadi."
    },
    {
        "text": "7–8-sinf Vibecoder o'zining Demo Day taqdimotida loyihasini qanday qilib eng yuqori darajada ko'rsatadi?",
        "a": "Faqat PowerPoint slaydlarini o'qib berish orqali.",
        "b": "Jonli ishlayotgan mahsulotni katta ekranda ko'rsatish, tomoshabinlarga telefonlari orqali kirish uchun QR kod ochish va AI bilan qanday yaratganini tushuntirish orqali.",
        "c": "Hech narsa gapirmasdan kompyuter yonida turish orqali.",
        "d": "Boshqa o'quvchilarning ishlarini tanqid qilish orqali.",
        "e": "Faqat loyiha narxini baland aytish orqali.",
        "correct": "B",
        "topic": "Demo Day va Mahsulot Taqdimoti",
        "expl": "Jonli interaktiv namoyish, QR kod orqali auditoriya bilan sinash va muhandislik qarorlarini tushuntirish Demo Day ning oltin kalitidir."
    },
    {
        "text": "Vibecoding falsafasida xatoliklar (bugs) yuz berganda to'g'ri fikrlash (mindset) qanday bo'lishi kerak?",
        "a": "Vahimaga tushib hamma narsani tashlab ketish.",
        "b": "Xatolikni o'rganish imkoniyati deb bilish: AI ga aniq belgilarni ko'rsatish, qat'iyat bilan tekshirish va muammoni yechib yangi tajriba orttirish.",
        "c": "Faqat kompyuterni ayblash.",
        "d": "Do'stiga darsni qildirib olish.",
        "e": "Xatoni yashirib qo'yish.",
        "correct": "B",
        "topic": "Vibecoder Mindset (Fikrlash Tarzi)",
        "expl": "Xatolar dasturlashning tabiiy qismidir. Vibecoder xatolikni AI bilan birga yechib, kuchli muhandisga aylanadi."
    }
]

QUESTIONS_7_8_RU = [
    {
        "text": "В чем заключается главная сила разработчика в подходе Vibecoding?",
        "a": "В механическом наборе кода вслепую в темной комнате.",
        "b": "В системном архитектурном мышлении: формулировании точных ТЗ для AI, валидации кода (Vibe-checking) и быстрой сборке прототипа в готовый продукт.",
        "c": "В полном отключении всех ассистентов искусственного интеллекта.",
        "d": "Исключительно в чтении школьных учебников английского языка.",
        "e": "В заучивании названий клавиш клавиатуры наизусть.",
        "correct": "B",
        "topic": "Философия Vibecoding",
        "expl": "Vibecoder фокусируется на архитектуре, логике и проверке результата, делегируя написание шаблонного кода нейросетям."
    },
    {
        "text": "Из каких 5 фундаментальных частей состоит идеальная анатомия промпта для разработки ПО?",
        "a": "Вступление, Заключение, Картинка, Песня, Видео.",
        "b": "Роль (Role), Контекст (Context), Конкретная Задача (Task), Ограничения (Constraints) и Формат Вывода (Output Format).",
        "c": "Исключительно логин и пароль пользователя.",
        "d": "Модель материнской платы и версия Windows.",
        "e": "Никаких разделов не требуется, достаточно одного неполного предложения.",
        "correct": "B",
        "topic": "Анатомия Промпта Разработчика",
        "expl": "Эти 5 блоков полностью очерчивают границы задачи для нейросети, предотвращая до 90% типичных ошибок."
    },
    {
        "text": "Какую функцию выполняет комбинация клавиш `Cmd+K` (или `Ctrl+K`) в среде Cursor и современных AI IDE?",
        "a": "Полностью выключает компьютер.",
        "b": "Открывает окно встроенного AI-редактирования (inline edit) для генерации, модификации или рефакторинга выделенного блока кода на месте.",
        "c": "Увеличивает масштаб системного шрифта.",
        "d": "Безвозвратно удаляет проект с диска.",
        "e": "Закрывает вкладку веб-браузера.",
        "correct": "B",
        "topic": "Cursor IDE и Inline Edit (Cmd+K)",
        "expl": "Встроенный диалог `Cmd+K` позволяет редактировать код прямо внутри файла без переключения в боковой чат."
    },
    {
        "text": "В чем заключается прорыв платформ v0.dev и Bolt.new в современном веб-программировании?",
        "a": "Они не требуют подключения к интернету.",
        "b": "Они генерируют полноценные современные интерфейсы (React/Tailwind UI) и работающие прототипы приложений всего по одному текстовому промпту.",
        "c": "Они рисуют только черно-белые иконки.",
        "d": "Они физически очищают клавиатуру ноутбука.",
        "e": "Они работают исключительно с файлами Microsoft Word.",
        "correct": "B",
        "topic": "Платформы v0.dev и Bolt.new",
        "expl": "Инструменты Prompt-to-UI сократили путь от идеи до интерактивного работающего веб-интерфейса до пары минут."
    },
    {
        "text": "Почему при создании сайтов с нейросетью критически важен компонентный подход (Component-driven prompting)?",
        "a": "Потому что нейросети проще объяснить сразу весь проект целиком.",
        "b": "Нейросеть не способна качественно сгенерировать все экраны разом; пошаговое создание компонентов (Navbar, Hero, Cards, Footer) исключает путаницу в коде.",
        "c": "Чтобы искусственно раздуть объем файлов.",
        "d": "Чтобы сайт состоял строго из одной кнопки.",
        "e": "Только для пакетной загрузки картинок.",
        "correct": "B",
        "topic": "Компонентный Подход",
        "expl": "Декомпозиция сложного интерфейса на изолированные блоки — золотое правило стабильного Vibecoding."
    },
    {
        "text": "Какую задачу выполняют упоминания `@Files` или `@Codebase` в редакторе Cursor?",
        "a": "Продажу исходных кодов на аукционе.",
        "b": "Явную передачу нужных файлов проекта в контекст AI, благодаря чему нейросеть точно видит импорты, типы и существующие функции.",
        "c": "Перевод всех названий переменных в верхний регистр.",
        "d": "Покупку коммерческой лицензии.",
        "e": "Блокировку экрана паролем.",
        "correct": "B",
        "topic": "Управление Контекстом (@Files)",
        "expl": "Тегирование файлов через `@` передает релевантный контекст, исключая выдумывание несуществующих функций и переменных."
    },
    {
        "text": "Что следует включить в промпт для задания строгой дизайн-системы (Design System) будущего интерфейса?",
        "a": "Фразу 'Сделай приятные цвета'.",
        "b": "Палитру HEX-цветов (например, основной Navy `#00214A`, акцент Cyan `#0284C7`), семейство шрифтов, скругления 16px и классы Tailwind CSS.",
        "c": "Название любимой марки автомобиля.",
        "d": "Диагональ экрана монитора в дюймах.",
        "e": "Категорический запрет на использование стилей.",
        "correct": "B",
        "topic": "Дизайн-Система и Цвета",
        "expl": "Четкие параметры палитры и отступов гарантируют создание цельного интерфейса коммерческого уровня (SaaS-стиль)."
    },
    {
        "text": "Как правильно составить промпт для исправления ошибки в консоли браузера при нажатии кнопки?",
        "a": "'Ты плохой искусственный интеллект, ничего не работает.'",
        "b": "'Вот полный текст ошибки: `Uncaught TypeError: Cannot read properties of undefined (reading 'addEventListener') at app.js:14`. Прилагаю код HTML и JS. Объясни причину и исправь.'",
        "c": "'Удали весь проект и начни заново.'",
        "d": "'Мне срочно нужен новый компьютер.'",
        "e": "'Покажи мне только правила CSS.'",
        "correct": "B",
        "topic": "Отладка Консольных Ошибок (Debugging)",
        "expl": "Стек вызова ошибки и номер строки позволяют модели мгновенно понять, какой DOM-элемент не успел инициализироваться."
    },
    {
        "text": "Каким должен быть грамотный инженерный запрос на рефакторинг исходного кода?",
        "a": "'Удали код.'",
        "b": "'Без изменения внешнего поведения программы примени принцип DRY, вынеси повторяющиеся блоки в чистые функции, дай понятные имена переменным и добавь комментарии.'",
        "c": "'Просто измени цвет фона.'",
        "d": "'Запиши весь файл в одну длинную строчку.'",
        "e": "'Переведи названия переменных на латынь.'",
        "correct": "B",
        "topic": "Рефакторинг Исходного Кода",
        "expl": "Рефакторинг делает структуру чистой, читаемой и масштабируемой, не ломая при этом функциональность программы."
    },
    {
        "text": "Как составить промпт для генерации реалистичных тестовых данных (Mock Data) для веб-приложения?",
        "a": "'Мне нужны люди.'",
        "b": "'Сгенерируй массив Mock Data из 10 объектов в формате JSON: id, имя, фамилия, возраст, рейтинг, аватар (unsplash url) для тестирования таблицы.'",
        "c": "'Найди телефоны моих друзей в интернете.'",
        "d": "'Сделай снимок реальных паспортов.'",
        "e": "'Напиши одно случайное слово.'",
        "correct": "B",
        "topic": "Генерация Mock Data (JSON)",
        "expl": "Синтетический JSON позволяет полноценно протестировать рендеринг списков и сортировок еще до создания настоящего бэкенда."
    },
    {
        "text": "Как четко потребовать от нейросети создание адаптивного дизайна (Responsive Design)?",
        "a": "'Сделай сайт меньше.'",
        "b": "'Обеспечь идеальное отображение на смартфонах (iPhone), планшетах и десктопах, используя медиазапросы CSS или адаптивные префиксы Tailwind (`sm:`, `md:`, `lg:`).' ",
        "c": "'Сайт должен открываться строго на ноутбуках.'",
        "d": "'Удали все картинки со страницы.'",
        "e": "'Переведи страницу в черно-белый режим.'",
        "correct": "B",
        "topic": "Адаптивный Дизайн (Responsive)",
        "expl": "Указание контрольных точек (breakpoints) гарантирует перестроение колонок в удобный мобильный стек на экранах телефонов."
    },
    {
        "text": "Какой промпт корректно подключит внешний публичный API (например, курсы валют) к фронтенду?",
        "a": "'Дай мне деньги.'",
        "b": "'Напиши функцию получения данных с открытого API через `fetch()`, добавь индикатор загрузки (Loading spinner) и обработку возможных ошибок через `try/catch`.'",
        "c": "'Взломай банковский счет.'",
        "d": "'Купи криптовалюту на бирже.'",
        "e": "'Нарисуй значок доллара.'",
        "correct": "B",
        "topic": "Интеграция с API",
        "expl": "Профессиональный промпт учитывает не только успешный запрос, но и состояния загрузки (Loading) и сетевые сбои (Error handling)."
    },
    {
        "text": "В чем ключевое преимущество подхода Few-Shot при генерации кода по сравнению с Zero-Shot?",
        "a": "Zero-Shot всегда требует платной подписки.",
        "b": "Показав нейросети образец существующего кода вашего проекта, вы гарантируете, что новый модуль будет написан в точности по вашим стандартам и стилю.",
        "c": "Few-Shot быстрее выключает операционную систему.",
        "d": "Few-Shot работает строго внутри HTML-разметки.",
        "e": "Между ними нет функциональной разницы.",
        "correct": "B",
        "topic": "Few-Shot vs Zero-Shot Кодинг",
        "expl": "Примеры в контексте задают строгий архитектурный шаблон, которому модель следует при генерации новых файлов."
    },
    {
        "text": "Зачем в промптах обязательно прописывают технические ограничения (Constraints)?",
        "a": "Чтобы искусственно замедлить генерацию ответа.",
        "b": "Чтобы нейросеть не добавляла лишние тяжелые библиотеки и фреймворки, четко ограничивая стек (например: 'Только чистый Vanilla JavaScript без сторонних библиотек').",
        "c": "Чтобы код генерировался только на английском языке.",
        "d": "Чтобы запретить форматирование кода.",
        "e": "Чтобы ограничить программу 10 символами.",
        "correct": "B",
        "topic": "Ограничения в Промптах (Constraints)",
        "expl": "Ограничения удерживают AI в рамках выбранного легковесного стека, защищая проект от перегрузки лишними зависимостями."
    },
    {
        "text": "Что представляет собой ошибка галлюцинации пакета ('Hallucinated Package') в коде от нейросети?",
        "a": "Требование купить новый процессор.",
        "b": "Ситуация, когда AI выдумывает название несуществующего npm-пакета (например, `npm i super-game-maker-2026`), которого нет в природе.",
        "c": "Исчезновение всех чисел из исходного кода.",
        "d": "Самопроизвольная смена обоев рабочего стола.",
        "e": "Смена интернет-провайдера.",
        "correct": "B",
        "topic": "Галлюцинации Пакетов (npm)",
        "expl": "Модели могут генерировать правдоподобно звучащие, но несуществующие пакеты. Каждый сторонний модуль нужно проверять на `npmjs.com`."
    },
    {
        "text": "Что именно тестирует разработчик в процессе 'Vibe-checking' созданного веб-приложения?",
        "a": "Только визуальную красоту текста.",
        "b": "Реальную работу всех интерактивных элементов, граничные сценарии (Edge Cases: пустой ввод, спецсимволы), мобильную верстку и плавность анимаций.",
        "c": "Уровень яркости экрана ноутбука.",
        "d": "Рекордное число набранных очков в игре.",
        "e": "Ничего не проверяет, слепо доверяя AI.",
        "correct": "B",
        "topic": "Vibe-Checking и Edge Cases",
        "expl": "Vibe-checking — это всесторонняя ручная и функциональная верификация продукта перед передачей пользователям."
    },
    {
        "text": "Как выглядит профессиональное сообщение коммита Git по стандарту Conventional Commits, сгенерированное AI?",
        "a": "'update', 'починил', 'все готово'.",
        "b": "'feat: add interactive FUT chemistry calculator with visual synergy links' или 'fix: resolve navbar overlap issue on mobile screens'.",
        "c": "Случайный набор смайликов.",
        "d": "Одна точка в поле описания.",
        "e": "Прогноз погоды на сегодня.",
        "correct": "B",
        "topic": "Стандарт Conventional Commits",
        "expl": "Инженерные коммиты используют стандартизированные префиксы (`feat:`, `fix:`, `refactor:`) и емко описывают суть внесенного изменения."
    },
    {
        "text": "Какой промпт создаст полноценного голосового ассистента на веб-технологиях?",
        "a": "'Сделай говорящего робота.'",
        "b": "'Используя встроенный Web Speech API браузера (`webkitSpeechRecognition` и `speechSynthesis`), создай интерфейс голосового помощника, принимающий команды и отвечающий голосом.'",
        "c": "'Включи мне музыку.'",
        "d": "'Позвони на телефон.'",
        "e": "'Нарисуй микрофон.'",
        "correct": "B",
        "topic": "Промпт для Web Speech API",
        "expl": "Указание встроенных API платформы позволяет получить легкое работающее решение без внешних тяжелых библиотек."
    },
    {
        "text": "Какие условия необходимо включить в промпт для генерации мини-игры на скорость реакции?",
        "a": "'Сделай игру.'",
        "b": "'Экран меняет цвет с красного на зеленый через случайный интервал 1–5 секунд; измерь разницу во времени клика в миллисекундах (`performance.now()`) и покажи скорость реакции.'",
        "c": "'Нарисуй только заставку.'",
        "d": "'Поставь счетчик очков.'",
        "e": "'Зажги все лампочки на клавиатуре.'",
        "correct": "B",
        "topic": "Промпт Мини-Игры на Реакцию",
        "expl": "Случайный таймер, смена визуального состояния и точный замер миллисекунд формируют завершенную механику игры."
    },
    {
        "text": "Что поручают сгенерировать искусственному интеллекту для составления документации README.md?",
        "a": "Только фотографию автора проекта.",
        "b": "Структурированный Markdown-файл: описание проекта, ключевые фичи (Features), инструкцию по запуску, стек технологий и ссылки на демо.",
        "c": "Одну строчку приветственного текста.",
        "d": "Удаление текстовых файлов.",
        "e": "Список имен одноклассников.",
        "correct": "B",
        "topic": "Документация README.md",
        "expl": "Качественный README презентует проект сообществу, объясняя ценность продукта и способ его быстрого развертывания."
    },
    {
        "text": "В чем заключается главная польза промпта 'Объясни, как работает этот фрагмент кода' (Explain Code)?",
        "a": "В возможности никогда не читать код программы.",
        "b": "В быстром разборе сложной логики простыми словами, что повышает личную инженерную грамотность ученика и учит новым приемам.",
        "c": "В отключении экрана компьютера.",
        "d": "В увеличении числа багов в файле.",
        "e": "В переводе программы в платный режим.",
        "correct": "B",
        "topic": "Обучение с AI (Explain Code)",
        "expl": "Разбор сгенерированного кода превращает каждую задачу в интерактивный урок, формируя глубокое понимание алгоритмов."
    },
    {
        "text": "Как использовать AI для работы с первыми заказами на фрилансе (Upwork / Kwork)?",
        "a": "Блокировать профили потенциальных клиентов.",
        "b": "Передать бриф клиента в AI, декомпозировать задачу на этапы, оценить сроки и составить вежливый профессиональный отклик (Proposal).",
        "c": "Только подсчитывать прибыль на калькуляторе.",
        "d": "Отправлять клиентам личные пароли от почты.",
        "e": "Сразу удалять входящие сообщения.",
        "correct": "B",
        "topic": "Фриланс и Анализ Брифов с AI",
        "expl": "AI помогает начинающему разработчику грамотно понять требования заказчика и составить сильное коммерческое предложение."
    },
    {
        "text": "В чем ключевое инженерное преимущество публикации проекта на платформе Vercel?",
        "a": "Сайт работает строго 60 минут.",
        "b": "Каждый git push в ветку main автоматически пересобирает проект, разворачивает его на глобальной CDN и выдает бесплатный HTTPS-сертификат.",
        "c": "Требуется ежедневная переустановка операционной системы.",
        "d": "На сайт может зайти только один человек.",
        "e": "Хостинг Vercel доступен только на платной основе.",
        "correct": "B",
        "topic": "Автоматический Деплой на Vercel",
        "expl": "Бесшовный CI/CD пайплайн Vercel связывает Git с продакшн-серверами, обеспечивая мгновенную доставку изменений пользователям."
    },
    {
        "text": "Как ученику 7–8 класса эффективнее всего продемонстрировать свой проект на школьном Demo Day?",
        "a": "Зачитывать длинный текст с экрана проектора.",
        "b": "Показать живой работающий продукт на экране, вывести QR-код для тестирования гостями со своих смартфонов и рассказать о преодоленных технических челленджах.",
        "c": "Молча стоять рядом с выключенным монитором.",
        "d": "Искать ошибки в проектах других участников.",
        "e": "Утверждать, что проект стоит миллион долларов.",
        "correct": "B",
        "topic": "Презентация на Demo Day",
        "expl": "Живое интерактивное демо с вовлечением жюри через QR-код — визитная карточка профессионального Vibecoder-а."
    },
    {
        "text": "Каким должен быть правильный психологический настрой (mindset) при возникновении багов в коде?",
        "a": "Впадать в панику и бросать начатое дело.",
        "b": "Воспринимать ошибку как возможность научиться новому: предоставить факты нейросети, последовательно протестировать фикс и победить проблему.",
        "c": "Обвинять во всем производителя клавиатуры.",
        "d": "Просить других сделать работу за себя.",
        "e": "Пытаться скрыть наличие ошибки от всех.",
        "correct": "B",
        "topic": "Инженерный Mindset Vibecoder-а",
        "expl": "Баги — неотъемлемая часть создания программ. Спокойный системный анализ с помощью AI развивает стойкость и мастерство."
    }
]

print("Grade 7-8 TRUE Vibecoding test data loaded (25 questions UZ & RU). Teacher: Ismoiljon Usmonov.")
