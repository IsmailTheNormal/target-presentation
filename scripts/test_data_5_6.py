#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
5–6-Sinf: 25 Savolli Vibecoding Asoslari va O'yin Loyihalari Testi
O'qituvchi: Ismoiljon Usmonov · Target International School
Uzbek va Russian variantlari (5 ta variant: A, B, C, D, E)
"""

META_5_6_UZ = {
    "school_name": "TARGET INTERNATIONAL SCHOOL — YUNUSOBOD",
    "teacher_name": "Ismoiljon Usmonov",
    "exam_title": "5–6-SINF: VIBECODING ASOSLARI VA O'YIN LOYIHALARI",
    "track_title": "Vibecoding & Game Dev Track · O'qituvchi: Ismoiljon Usmonov",
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
        {"grade": "A'lo (5)", "range": "22 – 25 ball", "desc": "Vibecoding, Canvas, o'yin fizikasi va AI promptlar bo'yicha a'lo bilim"},
        {"grade": "Yaxshi (4)", "range": "18 – 21 ball", "desc": "O'yin mexanikasi va vizual bloklar yaxshi o'zlashtirilgan"},
        {"grade": "Qoniqarli (3)", "range": "13 – 17 ball", "desc": "Hodisalar va koordinatalarni takrorlash lozim"},
        {"grade": "Qoniqarsiz (2)", "range": "0 – 12 ball", "desc": "Vibecoding asoslari qayta o'rganilishi zarur"}
    ]
}

META_5_6_RU = {
    "school_name": "TARGET INTERNATIONAL SCHOOL — ЮНУСАБАД",
    "teacher_name": "Исмоилжон Усмонов",
    "exam_title": "5–6 КЛАСС: ОСНОВЫ VIBECODING И СОЗДАНИЕ ИГР",
    "track_title": "Vibecoding & Game Dev Track · Преподаватель: Исмоилжон Усмонов",
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
        {"grade": "Отлично (5)", "range": "22 – 25 баллов", "desc": "Отличное владение Vibecoding, Canvas, игровой физикой и промптами"},
        {"grade": "Хорошо (4)", "range": "18 – 21 балл", "desc": "Хорошее понимание игровой механики и логики блоков"},
        {"grade": "Удовлетворительно (3)", "range": "13 – 17 баллов", "desc": "Требуется повторение событий клавиатуры и координат"},
        {"grade": "Неудовлетворительно (2)", "range": "0 – 12 баллов", "desc": "Необходимо повторное изучение основ Vibecoding"}
    ]
}

QUESTIONS_5_6_UZ = [
    {
        "text": "Vibecoding nima va uning an'anaviy dasturlashdan asosiy farqi nimada?",
        "a": "Faqat kompyuter o'yinlarini o'ynash va yangiliklarni o'qish.",
        "b": "Sun'iy intellekt (AI) bilan muloqot qilib, g'oya va promptlar orqali real kod va tayyor interaktiv loyihalarni tezkor yaratish.",
        "c": "Kompyuterni elektr tarmog'idan uzib qo'yish.",
        "d": "Klaviaturadan foydalanmasdan faqat ovoz yozib olish.",
        "e": "Faqat tayyor rasmlarni printerdan chop etish.",
        "correct": "B",
        "topic": "Vibecoding Mohiyati",
        "expl": "Vibecoding — insonning ijodiy g'oyasi va AI ning kod yozish tezligini birlashtirib, tezkor prototiplar va loyihalar yaratishdir."
    },
    {
        "text": "Sun'iy intellektdan o'yin kodi olishda eng sifatli natija beruvchi prompt (buyruq) qaysi?",
        "a": "'Menga biron narsa yozib ber.'",
        "b": "'HTML Canvas da 2D o'yin yarat: qahramon kvadrat bo'lsin, strelkalar bilan yursin, tikanlarga tegsa joni kamaysin va ochko hisoblansin.'",
        "c": "'O'yin qil.'",
        "d": "'Menga eng chiroyli ranglarni ayt.'",
        "e": "'Kompyuterimni tezlashtirib ber.'",
        "correct": "B",
        "topic": "Aniq Prompt Yozish",
        "expl": "Sifatli promptda aniq rol, texnologiya (Canvas), qahramon xususiyatlari, boshqaruv va o'yin qoidalari batafsil ko'rsatiladi."
    },
    {
        "text": "Veb-sahifada 2D o'yin grafikasini chizish uchun qaysi maxsus HTML tegi ishlatiladi?",
        "a": "<button>",
        "b": "<canvas>",
        "c": "<input>",
        "d": "<audio>",
        "e": "<link>",
        "correct": "B",
        "topic": "HTML5 Canvas Tegi",
        "expl": "<canvas> tegi JavaScript yordamida dinamik grafikalar, qahramonlar va animatsiyalar chiziladigan raqamli doska hisoblanadi."
    },
    {
        "text": "Canvas maydonida koordinatalar boshlang'ich nuqtasi (X: 0, Y: 0) qayerda joylashgan bo'ladi?",
        "a": "Ekran markazida.",
        "b": "Canvasning eng chap yuqori burchagida.",
        "c": "O'ng pastki burchakda.",
        "d": "Faqat kompyuter sichqonchasi turgan joyda.",
        "e": "Klaviaturaning 'Space' tugmasi ostida.",
        "correct": "B",
        "topic": "Canvas Koordinatalar Tizimi",
        "expl": "Kompyuter grafikasida X o'qi chapdan o'ngga qarab o'sadi, Y o'qi esa yuqoridan pastga qarab o'sadi. (0,0) chap yuqori burchakda."
    },
    {
        "text": "JavaScript-da o'yinchining to'plagan ballarini (Score) saqlash uchun qaysi kalit so'z bilan o'zgaruvchi e'lon qilinadi?",
        "a": "function score = 0;",
        "b": "let score = 0;",
        "c": "print score;",
        "d": "css score: 0;",
        "e": "html score;",
        "correct": "B",
        "topic": "O'zgaruvchilar (Variables)",
        "expl": "`let score = 0;` o'yin davomida o'zgarib turadigan qiymatlarni (ball, jon, tezlik) xotirada saqlash uchun xizmat qiladi."
    },
    {
        "text": "Qahramonni klaviatura strelkalari bilan boshqarish uchun brauzerning qaysi hodisasi (event) eshitiladi?",
        "a": "onclose",
        "b": "keydown",
        "c": "onclick",
        "d": "onload",
        "e": "oncopy",
        "correct": "B",
        "topic": "Klaviatura Hodisalari",
        "expl": "`keydown` hodisasi foydalanuvchi klaviaturadagi tugmani bosgan paytda ishga tushadi va qahramon harakatini faollashtiradi."
    },
    {
        "text": "O'yinda silliq animatsiya yaratish va ekranni sekundiga 60 marta yangilash uchun qaysi zamonaviy funksiya chaqiriladi?",
        "a": "setTimeout10()",
        "b": "requestAnimationFrame(gameLoop)",
        "c": "stopGame()",
        "d": "alert()",
        "e": "console.clear()",
        "correct": "B",
        "topic": "O'yin Tsikli (Game Loop)",
        "expl": "`requestAnimationFrame` brauzerning monitor yangilanish tezligiga (odatda 60 FPS) mos ravishda silliq harakatni ta'minlaydi."
    },
    {
        "text": "Qahramon har bir kadrdan oldin o'zining eski izlarini o'chirishi uchun Canvasda qaysi buyruq bajarilishi shart?",
        "a": "ctx.save()",
        "b": "ctx.clearRect(0, 0, canvas.width, canvas.height)",
        "c": "canvas.remove()",
        "d": "window.close()",
        "e": "ctx.stroke()",
        "correct": "B",
        "topic": "Kadrni Tozalash",
        "expl": "Agar `ctx.clearRect` ishlatilmasa, qahramon harakatlanganda uning eski chizilgan rasmlari ekranda qolib ketadi (iz qoldiradi)."
    },
    {
        "text": "O'yinda to'rtburchak qahramon chizish uchun qaysi Canvas metodi ishlatiladi?",
        "a": "ctx.drawCircle()",
        "b": "ctx.fillRect(x, y, width, height)",
        "c": "ctx.fillText()",
        "d": "ctx.beginPath()",
        "e": "ctx.createButton()",
        "correct": "B",
        "topic": "Shakllar Chizish",
        "expl": "`fillRect(x, y, w, h)` metodi berilgan koordinatalarda to'ldirilgan to'rtburchak chizadi."
    },
    {
        "text": "Qahramon tikan yoki lazerga tekkanini (to'qnashuvni) aniqlash dasturlashda nima deb ataladi?",
        "a": "Audio Sintezi",
        "b": "Collision Detection (To'qnashuvni tekshirish)",
        "c": "Screen Recording",
        "d": "Auto-saving",
        "e": "Theme Toggle",
        "correct": "B",
        "topic": "To'qnashuv (Collision)",
        "expl": "Collision Detection — ikki obyektning koordinatalari bir-birining ustiga tushganini matematik hisoblash mexanizmidir."
    },
    {
        "text": "Qahramon to'siqqa tekkanda uning joni (HP) kamayishi qanday shart bilan yoziladi?",
        "a": "if (hp < 0) { hp = 100; }",
        "b": "if (isColliding) { hp = hp - 1; }",
        "c": "while (true) { hp = 100; }",
        "d": "let hp = 'o`yin';",
        "e": "score = hp + 10;",
        "correct": "B",
        "topic": "Shart Operatorlari (if/else)",
        "expl": "`if (isColliding) { hp = hp - 1; }` — agar to'qnashuv yuz bersa, joriy jon miqdoridan 1 ta ayirib tashlaydi."
    },
    {
        "text": "O'yinda jon (HP) 0 ga teng bo'lib qolsa, qanday holat yuz berishi kerak?",
        "a": "Kompyuter o'chishi kerak.",
        "b": "O'yin to'xtab, ekranda 'Game Over' (O'yin Tugadi) yozuvi chiqishi va qayta o'ynash tugmasi paydo bo'lishi kerak.",
        "c": "O'yinchining barcha fayllari o'chirilishi kerak.",
        "d": "Ballar avtomatik 1 000 000 bo'lishi kerak.",
        "e": "Internet o'chishi kerak.",
        "correct": "B",
        "topic": "Game Over Holati",
        "expl": "HP nolga teng bo'lganda o'yin tsikli to'xtatiladi va qayta boshlash imkoniyati bilan yakuniy natija ko'rsatiladi."
    },
    {
        "text": "Qahramon oltin tanga yoki kristall ustidan yurganda ballni 10 taga oshirish kodi qaysi?",
        "a": "score = score * 0;",
        "b": "score += 10;",
        "c": "score = 'o`nta';",
        "d": "hp -= 10;",
        "e": "canvas.width += 10;",
        "correct": "B",
        "topic": "Ballarni Oshirish",
        "expl": "`score += 10` amali joriy ballga 10 qo'shib, o'zgaruvchining yangi qiymatini xotirada yangilaydi."
    },
    {
        "text": "O'yinda sakrash effekti hosil bo'lishi uchun qahramonning qaysi koordinatasi o'zgaradi?",
        "a": "Faqat kengligi (width)",
        "b": "Y koordinatasi (vertikal bo'yicha yuqoriga kamayadi, keyin gravitatsiya bilan pastga ortadi)",
        "c": "Faqat rangi",
        "d": "Canvas balandligi",
        "e": "O'yinchining ismi",
        "correct": "B",
        "topic": "Sakrash Mexanikasi",
        "expl": "Sakrash vertikal harakat bo'lib, Y o'qi bo'yicha yuqoriga ko'tarilish va gravitatsiya kuchi ta'sirida yerga qaytish orqali hosil qilinadi."
    },
    {
        "text": "Gravitatsiya (tortish kuchi) kodi har bir freymda qahramonga qanday ta'sir o'tkazadi?",
        "a": "Qahramonni chapga suradi.",
        "b": "Qahramonning vertikal tezligiga (`vy`) doimiy son (masalan, 0.5) qo'shib, uni pastga qarab tortadi.",
        "c": "Qahramonni g'oyib qiladi.",
        "d": "O'yin tezligini nolga tushiradi.",
        "e": "Tugmalar rangini o'zgartiradi.",
        "correct": "B",
        "topic": "Gravitatsiya Fizikasi",
        "expl": "Gravitatsiya kuchi vertikal tezlikni pastga tomon oshirib boradi, natijada qahramon polga (yerga) realistik tushadi."
    },
    {
        "text": "O'yindagi dushmanning avtomatik ravishda chapga va o'ngga yurishi (patrul qilishi) qanday amalga oshiriladi?",
        "a": "Uni o'yinchi klaviaturadan boshqaradi.",
        "b": "Dushmanning X tezligi (`vx`) bo'lib, u devorga yoki chegara koordinatasiga yetganda tezlik ishorasi teskariga o'zgartiriladi (`vx = -vx`).",
        "c": "Dushman har 1 soniyada o'chirib qayta chiziladi.",
        "d": "Faqat sichqoncha qimirlaganda yuradi.",
        "e": "Dushman har doim bir joyda qotib turadi.",
        "correct": "B",
        "topic": "Dushman Patrul AI",
        "expl": "Tezlik ishorasini teskariga burish (`vx = -vx`) orqali dushman chegara nuqtalarida o'z yo'nalishini avtomatik o'zgartirib turadi."
    },
    {
        "text": "Dushmanning o'yinchini ta'qib qilishi (quvishi) uchun unga qanday oddiy 'Sun'iy Intellekt' (AI) mantiqi beriladi?",
        "a": "Dushman ekrandan chiqib ketishi kerak.",
        "b": "Agar o'yinchining X koordinatasi dushmannikidan katta bo'lsa dushman o'ngga yuradi, kichik bo'lsa chapga yuradi.",
        "c": "Dushman uxlab qoladi.",
        "d": "Dushman o'z rangini sariqqa o'zgartiradi.",
        "e": "O'yin kodini o'chirib tashlaydi.",
        "correct": "B",
        "topic": "Ta'qib AI Mantiqi",
        "expl": "Qahramon koordinatasi bilan dushman koordinatasini solishtirish orqali dushman doimo qahramon tomon yo'naladi."
    },
    {
        "text": "O'yinda Boss jangi (yakuniy dushman) oddiy dushmandan nimasi bilan farq qiladi?",
        "a": "Uning rangi bo'lmaydi.",
        "b": "U ancha katta o'lchamga, ko'p jonga (HP shkalasiga) ega bo'ladi va turli hujum fazalarini (masalan, olov otish) ishlatadi.",
        "c": "Boss faqat ovozsiz ishlaydi.",
        "d": "Boss bilan o'yinni boshlash mumkin emas.",
        "e": "Boss hech qachon ekranda ko'rinmaydi.",
        "correct": "B",
        "topic": "Boss Jangi Mexanikasi",
        "expl": "Boss murakkab o'yin obyekti bo'lib, katta HP sig'imi va bir necha fazali xatti-harakatlarga ega bo'ladi."
    },
    {
        "text": "O'yinchi rekord ball to'plaganida brauzer yopilgandan keyin ham natija o'chib ketmasligi uchun qayerda saqlanadi?",
        "a": "Qog'ozga yozib olinadi.",
        "b": "Brauzerning `localStorage` doimiy xotirasida (`localStorage.setItem('highScore', score)`).",
        "c": "Kompyuter monitorida.",
        "d": "Klaviatura ichida.",
        "e": "Faqat bir martalik `alert()` oynasida.",
        "correct": "B",
        "topic": "LocalStorage da Saqlash",
        "expl": "`localStorage` ma'lumotlarni brauzer xotirasida saqlab qoladi, sahifa qayta yangilanganda ham natija o'chmaydi."
    },
    {
        "text": "'O'z levelingni o'zing qur' (Level Editor) vositasida xarita katakchalari dasturlashda qanday massivda saqlanadi?",
        "a": "Bitta harf ichida.",
        "b": "2 o'lchamli massiv (grid jadvali: 0 - bo'sh joy, 1 - devor, 2 - tanga).",
        "c": "Faqat rasm fayli ichida.",
        "d": "Audio fayl ichida.",
        "e": "Bunday narsani saqlab bo'lmaydi.",
        "correct": "B",
        "topic": "Level Xaritasi va Grid",
        "expl": "2D massiv (matritsa) xarita bloklarini qator va ustunlar bo'yicha qulay raqamlar bilan ifodalash imkonini beradi."
    },
    {
        "text": "O'yinda tugma bosilganda yoki sakraganda tovush chiqarish uchun qaysi texnologiyadan foydalaniladi?",
        "a": "CSS Rang filtri",
        "b": "HTML5 `<audio>` tegi yoki Web Audio API",
        "c": "Faqat matnli shriftlar",
        "d": "Kompyuter mikrofonini yoqish",
        "e": "Printer drayveri",
        "correct": "B",
        "topic": "O'yin Ovoz Efekti",
        "expl": "Veb o'yinlarida tovushlar `<audio>` elementlari yoki brauzerning Web Audio API audio-konteksti orqali chalinadi."
    },
    {
        "text": "O'yin yozayotganda konsolda qizil xatolik (Error) chiqsa, Vibecoding usulida nima qilish kerak?",
        "a": "Kompyuterni derazadan tashlab yuborish kerak.",
        "b": "Xatolik matnini (Stack trace) nusxalab, AI ga berish va 'Nega bu xato chiqdi va qanday to'g'rilayman?' deb so'rash kerak.",
        "c": "Dasturlashni butunlay to'xtatish kerak.",
        "d": "Xatoni e'tiborsiz qoldirish kerak.",
        "e": "Klaviaturaning hamma tugmalarini birdaniga bosish kerak.",
        "correct": "B",
        "topic": "AI Bilan Debugging",
        "expl": "Vibecoding madaniyatida AI ga aniq xatolik matnini uzatish eng tezkor va o'rgatuvchi tuzatish yo'lidir."
    },
    {
        "text": "CSS stillari o'yinda qanday vazifani bajaradi?",
        "a": "O'yin logikasini hisoblaydi.",
        "b": "O'yin maydonini markazga joylash, chiroyli ramkalar, neon ranglar, tugmalar dizayni va zamonaviy ko'rinish berish.",
        "c": "Faqat internet tezligini oshiradi.",
        "d": "Kompyuter viruslarini yo'qotadi.",
        "e": "Faqat ovoz balandligini boshqaradi.",
        "correct": "B",
        "topic": "CSS va O'yin Vizuali",
        "expl": "CSS (Cascading Style Sheets) o'yin interfeysini jozibador, responsiv va zamonaviy ko'rinishga keltirish uchun mas'uldir."
    },
    {
        "text": "O'yinda 'Qayta boshlash' (Restart) tugmasi bosilganda nimalar amalga oshirilishi kerak?",
        "a": "Saytni butunlay o'chirib tashlash.",
        "b": "Qahramon koordinatalari, jon miqdori (HP) va ballarni boshlang'ich holatga qaytarib, o'yin tsiklini yangidan ishga tushirish.",
        "c": "Faqat fon rasmini o'zgartirish.",
        "d": "Kompyuter ekranini qoraytirish.",
        "e": "O'yin nomini o'zgartirish.",
        "correct": "B",
        "topic": "O'yinni Qayta Yuklash",
        "expl": "Restart funksiyasi o'yin holatini (state) tozalab, o'yinchiga darhol yangi urinish beradi."
    },
    {
        "text": "Yaratilgan o'yinni do'stlarga yuborish va telefonda o'ynash uchun qanday yakuniy bosqich (Deploy) bajariladi?",
        "a": "Kodni qog'ozga ko'chirib yozish.",
        "b": "Loyihani Vercel yoki GitHub Pages xizmatiga yuklab, hammaga ochiq havola (URL) va QR kod yaratish.",
        "c": "Kompyuterni do'stining uyiga ko'tarib borish.",
        "d": "Faqat o'z kompyuterida o'ynash.",
        "e": "Faylni butunlay yashirib qo'yish.",
        "correct": "B",
        "topic": "Veb Deploy va Ulashish",
        "expl": "Vercel yoki GitHub Pages orqali bir necha soniyada o'yin global internetga chiqadi va har qanday telefonda QR kod orqali ochiladi."
    }
]

QUESTIONS_5_6_RU = [
    {
        "text": "Что такое Vibecoding и в чем его главное отличие от традиционного программирования?",
        "a": "Просто играть в компьютерные игры и читать новости.",
        "b": "Создавать реальный код и готовые интерактивные веб-проекты в диалоге с искусственным интеллектом (AI) через точные идеи и промпты.",
        "c": "Полное отключение компьютера от электричества.",
        "d": "Запись голоса без использования клавиатуры.",
        "e": "Печать готовых картинок на обычном принтере.",
        "correct": "B",
        "topic": "Суть Vibecoding",
        "expl": "Vibecoding объединяет творческую идею человека со скоростью написания кода нейросетью для быстрого создания проектов."
    },
    {
        "text": "Какой промпт (запрос к AI) даст самый качественный результат для генерации игры?",
        "a": "'Напиши мне что-нибудь.'",
        "b": "'Создай 2D-игру на HTML Canvas: персонаж — синий квадрат, ходит на стрелочки, при касании шипов теряет жизни, собирает монеты и считает очки.'",
        "c": "'Сделай игру.'",
        "d": "'Назови мне самые красивые цвета.'",
        "e": "'Ускорь мой компьютер.'",
        "correct": "B",
        "topic": "Написание Четкого Промпта",
        "expl": "Качественный промпт содержит конкретную роль, технологию (Canvas), параметры персонажа, механику управления и правила игры."
    },
    {
        "text": "Какой специальный HTML-тег используется для рисования 2D-графики и игр в браузере?",
        "a": "<button>",
        "b": "<canvas>",
        "c": "<input>",
        "d": "<audio>",
        "e": "<link>",
        "correct": "B",
        "topic": "Тег HTML5 Canvas",
        "expl": "Тег <canvas> служит цифровым холстом, на котором с помощью JavaScript динамически рисуются персонажи и анимации."
    },
    {
        "text": "Где находится начальная точка координат (X: 0, Y: 0) на холсте Canvas?",
        "a": "Точно в центре экрана.",
        "b": "В самом верхнем левом углу холста Canvas.",
        "c": "В правом нижнем углу.",
        "d": "В месте, где находится курсор мыши.",
        "e": "Под клавишей 'Space' на клавиатуре.",
        "correct": "B",
        "topic": "Система Координат Canvas",
        "expl": "В компьютерной графике ось X идет слева направо, а ось Y — сверху вниз. Точка (0,0) находится в верхнем левом углу."
    },
    {
        "text": "С помощью какого ключевого слова в JavaScript объявляется переменная для хранения счета (Score) игры?",
        "a": "function score = 0;",
        "b": "let score = 0;",
        "c": "print score;",
        "d": "css score: 0;",
        "e": "html score;",
        "correct": "B",
        "topic": "Переменные (Variables)",
        "expl": "`let score = 0;` создает переменную в оперативной памяти для хранения изменяющихся данных (очки, жизни, скорость)."
    },
    {
        "text": "Какое браузерное событие (Event) слушают для управления персонажем с помощью клавиатуры?",
        "a": "onclose",
        "b": "keydown",
        "c": "onclick",
        "d": "onload",
        "e": "oncopy",
        "correct": "B",
        "topic": "События Клавиатуры",
        "expl": "Событие `keydown` срабатывает в момент нажатия любой клавиши на клавиатуре и запускает движение героя."
    },
    {
        "text": "Какая функция используется в современных браузерах для плавной анимации игры со скоростью 60 кадров в секунду (FPS)?",
        "a": "setTimeout10()",
        "b": "requestAnimationFrame(gameLoop)",
        "c": "stopGame()",
        "d": "alert()",
        "e": "console.clear()",
        "correct": "B",
        "topic": "Игровой Цикл (Game Loop)",
        "expl": "`requestAnimationFrame` синхронизирует перерисовку кадров с частотой монитора для максимально плавного движения."
    },
    {
        "text": "Какую команду необходимо вызывать перед рисованием каждого нового кадра, чтобы персонаж не оставлял за собой шлейф (следы)?",
        "a": "ctx.save()",
        "b": "ctx.clearRect(0, 0, canvas.width, canvas.height)",
        "c": "canvas.remove()",
        "d": "window.close()",
        "e": "ctx.stroke()",
        "correct": "B",
        "topic": "Очистка Кадра",
        "expl": "`ctx.clearRect` стирает содержимое холста перед отрисовкой нового кадра, исключая размазывание графики."
    },
    {
        "text": "Какой метод Canvas используется для отрисовки прямоугольного персонажа или блока?",
        "a": "ctx.drawCircle()",
        "b": "ctx.fillRect(x, y, width, height)",
        "c": "ctx.fillText()",
        "d": "ctx.beginPath()",
        "e": "ctx.createButton()",
        "correct": "B",
        "topic": "Рисование Фигур",
        "expl": "Метод `fillRect(x, y, w, h)` рисует закрашенный прямоугольник по заданным координатам и размерам."
    },
    {
        "text": "Как в разработке игр называется механизм определения столкновения персонажа с препятствием или шипом?",
        "a": "Аудио-синтез",
        "b": "Collision Detection (Определение столкновений)",
        "c": "Запись экрана",
        "d": "Автосохранение",
        "e": "Смена темы оформления",
        "correct": "B",
        "topic": "Коллизии (Столкновения)",
        "expl": "Collision Detection — это математический расчет пересечения границ двух объектов на игровом поле."
    },
    {
        "text": "Как правильно записать условие уменьшения жизней (HP) при столкновении с опасностью?",
        "a": "if (hp < 0) { hp = 100; }",
        "b": "if (isColliding) { hp = hp - 1; }",
        "c": "while (true) { hp = 100; }",
        "d": "let hp = 'игра';",
        "e": "score = hp + 10;",
        "correct": "B",
        "topic": "Условные Операторы (if/else)",
        "expl": "Если обнаружено столкновение (`isColliding`), то от текущего значения здоровья отнимается единица."
    },
    {
        "text": "Что должно происходить в игре, когда количество жизней (HP) игрока опускается до нуля?",
        "a": "Компьютер должен немедленно выключиться.",
        "b": "Игровой цикл останавливается, на экране появляется надпись 'Game Over' и кнопка 'Перезапуск' (Restart).",
        "c": "С компьютера должны удалиться все файлы.",
        "d": "Счетчик очков должен автоматически стать равным 1 000 000.",
        "e": "Должен пропасть доступ в интернет.",
        "correct": "B",
        "topic": "Состояние Game Over",
        "expl": "При нулевом HP игра завершается, фиксируется финальный счет и пользователю предлагается повторить попытку."
    },
    {
        "text": "Какой код увеличивает счет игрока на 10 при сборе золотой монеты или кристалла?",
        "a": "score = score * 0;",
        "b": "score += 10;",
        "c": "score = 'десять';",
        "d": "hp -= 10;",
        "e": "canvas.width += 10;",
        "correct": "B",
        "topic": "Увеличение Счета",
        "expl": "Оператор `score += 10` прибавляет 10 к текущему значению переменной счета и сохраняет результат."
    },
    {
        "text": "Какая координата изменяется при прыжке персонажа вверх на двумерном экране?",
        "a": "Только ширина (width)",
        "b": "Координата Y (уменьшается при движении вверх и увеличивается под действием гравитации при падении)",
        "c": "Только цвет персонажа",
        "d": "Высота всего окна браузера",
        "e": "Имя учетной записи игрока",
        "correct": "B",
        "topic": "Механика Прыжка",
        "expl": "Прыжок — это вертикальное перемещение по оси Y: сначала вверх (уменьшение Y), затем падение вниз под силой тяжести."
    },
    {
        "text": "Как сила гравитации (Gravity) воздействует на персонажа в каждом кадре игрового цикла?",
        "a": "Сдвигает персонажа строго влево.",
        "b": "Постоянно прибавляет значение к вертикальной скорости (`vy += 0.5`), плавно притягивая персонажа вниз к земле.",
        "c": "Делает персонажа полностью невидимым.",
        "d": "Снижает скорость процессора до нуля.",
        "e": "Перекрашивает фон в синий цвет.",
        "correct": "B",
        "topic": "Физика Гравитации",
        "expl": "Гравитация непрерывно увеличивает вертикальную скорость падения, создавая реалистичное приземление на платформу."
    },
    {
        "text": "Как реализуется автоматическое патрулирование врага влево и вправо по платформе?",
        "a": "Врагом управляет второй игрок со стрелочек клавиатуры.",
        "b": "У врага есть горизонтальная скорость (`vx`), и при касании границы платформы знак скорости инвертируется (`vx = -vx`).",
        "c": "Враг удаляется и создается заново каждую секунду.",
        "d": "Враг перемещается только при движении курсора мыши.",
        "e": "Враг всегда неподвижно стоит на одном месте.",
        "correct": "B",
        "topic": "Патрулирование Врага (AI)",
        "expl": "Смена знака скорости (`vx = -vx`) заставляет врага разворачиваться при достижении края платформы или препятствия."
    },
    {
        "text": "Какая простая логика искусственного интеллекта заставляет врага преследовать игрока?",
        "a": "Враг должен просто вылететь за пределы экрана.",
        "b": "Если координата X игрока больше координаты врага — враг идет вправо, если меньше — идет влево.",
        "c": "Враг должен заснуть.",
        "d": "Враг перекрашивается в желтый цвет.",
        "e": "Враг стирает код программы.",
        "correct": "B",
        "topic": "Логика Преследования AI",
        "expl": "Сравнение координат игрока и врага позволяет боту постоянно двигаться в направлении цели."
    },
    {
        "text": "Чем битва с Боссом (финальным противником) отличается от схватки с обычным врагом?",
        "a": "У Босса нет цвета и формы.",
        "b": "Босс обладает увеличенными размерами, большой полоской здоровья (HP Bar) и использует разные фазы атак (например, фаерболы).",
        "c": "Босс работает только при выключенном звуке.",
        "d": "С Боссом невозможно начать игру.",
        "e": "Босс никогда не отображается на экране.",
        "correct": "B",
        "topic": "Механика Битвы с Боссом",
        "expl": "Босс представляет собой усиленного противника с большим запасом HP и разнообразными фазами поведения."
    },
    {
        "text": "Где сохраняется рекордный счет (High Score), чтобы он не исчез после закрытия или перезагрузки браузера?",
        "a": "Записывается на листок бумаги.",
        "b": "В постоянном локальном хранилище браузера `localStorage` (`localStorage.setItem('highScore', score)`).",
        "c": "Внутри стекла монитора.",
        "d": "Внутри корпуса клавиатуры.",
        "e": "Только во временном окне `alert()`.",
        "correct": "B",
        "topic": "Хранение в LocalStorage",
        "expl": "`localStorage` позволяет браузеру сохранять текстовые данные на диске между сессиями пользователя."
    },
    {
        "text": "В каком виде в коде игры хранится карта уровней для инструмента 'Создай свой уровень' (Level Editor)?",
        "a": "Внутри одной отдельной буквы.",
        "b": "В виде двумерного массива (сетка/матрица, где 0 — пусто, 1 — стена, 2 — монета).",
        "c": "Только в формате аудиофайла.",
        "d": "Карту уровней невозможно сохранить.",
        "e": "В виде случайного числа.",
        "correct": "B",
        "topic": "Карта Уровня и Сетка (Grid)",
        "expl": "Двумерный массив (матрица) наглядно кодирует клетки игрового поля по строкам и столбцам."
    },
    {
        "text": "Какая технология используется для воспроизведения звуков прыжка и сбора монет в браузерной игре?",
        "a": "Цветовой CSS-фильтр",
        "b": "HTML5-тег `<audio>` или Web Audio API",
        "c": "Только шрифты Google Fonts",
        "d": "Включение микрофона пользователя",
        "e": "Драйвер офисного сканера",
        "correct": "B",
        "topic": "Игровые Звуковые Эффекты",
        "expl": "Звуковые эффекты проигрываются через HTML5 Audio элементы либо синтезируются через Web Audio API."
    },
    {
        "text": "Если при запуске игры в консоли браузера появилась красная ошибка (Error), как поступить в стиле Vibecoding?",
        "a": "Срочно выключить компьютер из розетки.",
        "b": "Скопировать текст ошибки (Stack trace), передать его в AI и спросить: 'В чем причина и как исправить этот баг?'",
        "c": "Навсегда бросить программирование.",
        "d": "Сделать вид, что ошибки не существует.",
        "e": "Нажать все клавиши на клавиатуре одновременно.",
        "correct": "B",
        "topic": "AI-Debugging Ошибок",
        "expl": "В культуре Vibecoding передача точного текста ошибки в AI является самым быстрым и обучающим способом решения проблемы."
    },
    {
        "text": "Какую ключевую роль играют стили CSS при создании веб-игры?",
        "a": "Выполняют математические расчеты физики.",
        "b": "Центрируют холст Canvas, задают неоновые рамки, стилизуют кнопки, табло очков и создают стильный дизайн.",
        "c": "Увеличивают скорость интернет-провайдера.",
        "d": "Удаляют вирусы с жесткого диска.",
        "e": "Регулируют громкость колонок.",
        "correct": "B",
        "topic": "CSS и Визуальный Стиль",
        "expl": "CSS отвечает за внешнее оформление, шрифты, отступы и привлекательный современный интерфейс игры."
    },
    {
        "text": "Что должно происходить при нажатии кнопки 'Начать заново' (Restart)?",
        "a": "Полное удаление сайта из интернета.",
        "b": "Сброс координат героя, жизней и счета к начальным значениям и перезапуск игрового цикла.",
        "c": "Только изменение цвета заднего фона.",
        "d": "Отключение экрана монитора.",
        "e": "Смена языка операционной системы.",
        "correct": "B",
        "topic": "Перезапуск Игры (Restart)",
        "expl": "Функция Restart сбрасывает состояние игры (State) к исходным параметрам и начинает новый раунд."
    },
    {
        "text": "Как опубликовать (задеплоить) готовую игру в интернет, чтобы отправить ссылку друзьям и играть на смартфоне?",
        "a": "Переписать весь код от руки в тетрадь.",
        "b": "Загрузить проект на бесплатный хостинг (Vercel или GitHub Pages) и получить рабочую ссылку (URL) и QR-код.",
        "c": "Принести свой системный блок домой к другу.",
        "d": "Играть только в одиночку со своего ПК.",
        "e": "Спрятать файл на флешке в ящик стола.",
        "correct": "B",
        "topic": "Деплой и Публикация Игры",
        "expl": "Сервисы Vercel и GitHub Pages публикуют веб-проекты за считанные секунды, делая их доступными по всему миру."
    }
]

print("Grade 5-6 Vibecoding test data loaded (25 questions UZ & RU). Teacher: Ismoiljon Usmonov.")
