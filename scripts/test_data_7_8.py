#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Target International School — 7–8-Sinf Vibecoding Test Ma'lumotlari
Fan: Vibecoding (Game Dev, Interaktiv Veb va Biometrik Muhandislik)
O'qituvchi: Ismoiljon Usmonov · Yunusobod filiali

Struktura:
- 18 ta tushunarli, aniq va mustahkam savollar (Steady)
- 7 ta qiziqarli amaliy bilim savollari (Tricky Real Knowledge)
- Barcha savollar veb-platformadagi darslar (index.html va classes/7-8-sinf/) asosida tuzilgan
"""

META_7_8_UZ = {
    "school_name": "TARGET INTERNATIONAL SCHOOL — YUNUSOBOD",
    "exam_title": "7–8-SINF: VIBECODING, O'YIN FIZIKASI VA INTERAKTIV VEB",
    "track_title": "Game Dev & Interactive Web Systems · O'qituvchi: Ismoiljon Usmonov",
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

KEYS_META_7_8_UZ = {
    "heading": "JAVOBLAR KALITI VA BAHOLASH MEZONI",
    "subheading": "O'qituvchi: Ismoiljon Usmonov · 7–8-sinf Vibecoding rasmiy tekshirish kaliti (25 ta savol)",
    "table_headers": ["№", "Kalit", "Mavzu / Dars", "Izoh va Tushuntirish"],
    "scale_heading": "Rasmiy 25 Ballik Baholash Shkalasi:",
    "rubric_tiers": [
        {"grade": "A'lo (5)", "range": "22 – 25 ball", "desc": "Canvas, Game Loop, o'yin fizikasi va Web API bo'yicha chuqur bilim"},
        {"grade": "Yaxshi (4)", "range": "18 – 21 ball", "desc": "DOM hodisalari, CSS Flexbox va o'yin mexanikasi yaxshi o'zlashtirilgan"},
        {"grade": "Qoniqarli (3)", "range": "13 – 17 ball", "desc": "LocalStorage va massiv metodlarini takrorlash lozim"},
        {"grade": "Qoniqarsiz (2)", "range": "0 – 12 ball", "desc": "Vibecoding va JavaScript asoslari qayta o'rganilishi zarur"}
    ]
}

META_7_8_RU = {
    "school_name": "TARGET INTERNATIONAL SCHOOL — ЮНУСАБАД",
    "exam_title": "7–8 КЛАСС: VIBECODING, ИГРОВАЯ ФИЗИКА И ИНТЕРАКТИВНЫЙ ВЕБ",
    "track_title": "Game Dev & Interactive Web Systems · Учитель: Исмоилжон Усмонов",
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

KEYS_META_7_8_RU = {
    "heading": "КЛЮЧИ ОТВЕТОВ И КРИТЕРИИ ОЦЕНИВАНИЯ",
    "subheading": "Учитель: Исмоилжон Усмонов · Официальный ключ 7–8 класс (25 вопросов)",
    "table_headers": ["№", "Ключ", "Тема / Урок", "Пояснение и разбор ответа"],
    "scale_heading": "Официальная 25-балльная шкала оценивания:",
    "rubric_tiers": [
        {"grade": "Отлично (5)", "range": "22 – 25 баллов", "desc": "Отличные знания Canvas, Game Loop, физики игр и Web API"},
        {"grade": "Хорошо (4)", "range": "18 – 21 балл", "desc": "События DOM, CSS Flexbox и игровая механика хорошо освоены"},
        {"grade": "Удовл. (3)", "range": "13 – 17 баллов", "desc": "Требуется повторение LocalStorage и методов массивов"},
        {"grade": "Неудовл. (2)", "range": "0 – 12 баллов", "desc": "Необходимо повторить основы Vibecoding и JavaScript"}
    ]
}

QUESTIONS_7_8_UZ = [
    # 1. Steady
    {
        "text": "1-darsga ko'ra, Katta Til Modellari (LLM) dasturlashda bizga qanday yordam beradi?",
        "a": "Ular kompyuter monitorini yangilab beradi.",
        "b": "Biz yozgan promptdagi talablarni tushunib, HTML, CSS va JavaScript kodlarini tezkor generatsiya qiladi.",
        "c": "Kompyuterdan barcha fayllarni o'chirib yuboradi.",
        "d": "Faqat kompyuter o'yinlarini o'ynab o'tiradi.",
        "e": "Faqat oddiy kalkulyator vazifasini bajaradi.",
        "correct": "B",
        "topic": "01-dars: LLM va Sun'iy Intellekt",
        "expl": "LLM modellari tabiiy tildagi talablarni qabul qilib, mos dasturlash kodini tez va to'g'ri yozib beradi."
    },
    # 2. Steady
    {
        "text": "2-darsdagi 'AI Duel' darsida AI ga qanday prompt berilsa eng yaxshi natija olinadi?",
        "a": "Faqat bitta noaniq so'z yozilsa.",
        "b": "Dastur nima qilishi kerakligi, qaysi tilda yozilishi va qanday tugmalar bo'lishi aniq ko'rsatilsa.",
        "c": "Faqat kulgili stikerlar yuborilsa.",
        "d": "Prompt faqat qora rangda yozilsa.",
        "e": "AI ga hech qanday talab bermasdan o'ziga tashlab qo'yilsa.",
        "correct": "B",
        "topic": "02-dars: Sifatli Prompt Tuzilishi",
        "expl": "Aniq rollar, aniq texnologiya (HTML/CSS/JS) va qoidalar ko'rsatilgan prompt eng sifatli natijani beradi."
    },
    # 3. Steady
    {
        "text": "3-darsda o'rganilgan SVG (Scalable Vector Graphics) formatining asosiy afzalligi nimada?",
        "a": "U faqat qora rangda bo'ladi.",
        "b": "U vektor chiziqlardan iborat bo'lgani uchun, qanchalik kattalashtirilsa ham xiralashmaydi va tiniq turadi.",
        "c": "U kompyuterda 10 gigabayt joy oladi.",
        "d": "Uni brauzerda ochib bo'lmaydi.",
        "e": "U faqat musiqa tinglash uchun xizmat qiladi.",
        "correct": "B",
        "topic": "03-dars: SVG Vektor Grafikasi",
        "expl": "SVG pikselli rasm emas, balki matematik vektor chiziqlar bo'lib, istalgan ekranda o'ta tiniq ko'rinadi."
    },
    # 4. Steady
    {
        "text": "5-darsda veb-sahifaning asosiy mazmunini o'rab turish uchun qaysi semantik HTML tegi ishlatiladi?",
        "a": "<div>",
        "b": "<main>",
        "c": "<span>",
        "d": "<br>",
        "e": "<input>",
        "correct": "B",
        "topic": "05-dars: Semantik HTML (<main> tegi)",
        "expl": "<main> tegi sahifaning bosh (asosiy) mazmuni qayerda joylashganini brauzerga aniq ko'rsatib beradi."
    },
    # 5. Steady
    {
        "text": "7-darsda CSS Flexbox da elementlarni gorizontal o'q bo'ylab markazga qo'yish uchun nima yoziladi?",
        "a": "align-items: center;",
        "b": "justify-content: center;",
        "c": "text-align: middle;",
        "d": "display: hidden;",
        "e": "float: center;",
        "correct": "B",
        "topic": "07-dars: Flexbox va justify-content",
        "expl": "Flexbox tizimida justify-content: center elementlarni gorizontal asosiy o'q markaziga tekislaydi."
    },
    # 6. Steady
    {
        "text": "8-darsda tugma bosilganini (klik qilinganini) JavaScript orqali eshitib turish qanday yoziladi?",
        "a": "button.startClick()",
        "b": "button.addEventListener('click', () => { ... });",
        "c": "window.destroy()",
        "d": "document.write('click')",
        "e": "console.clear()",
        "correct": "B",
        "topic": "08-dars: addEventListener va Kliklar",
        "expl": "addEventListener('click', callback) metodi foydalanuvchi tugmani bosgan paytda funksiyani ishga tushiradi."
    },
    # 7. Tricky (Real Knowledge)
    {
        "text": "9-darsda 'Kiber-Reaksiya' o'yinida nega Date.now() o'rniga performance.now() funksiyasi ishlatildi?",
        "a": "Chunki Date.now() internet talab qiladi.",
        "b": "Chunki performance.now() vaqtni millisekundning o'ndan birigacha o'ta yuqori aniqlikda hisoblab, reaktsiya tezligini haqqoniy ko'rsatadi.",
        "c": "Chunki u kompyuterni tezlashtiradi.",
        "d": "Chunki performance.now() faqat ovoz chiqaradi.",
        "e": "Chunki u ekranni qizil rangga bo'yaydi.",
        "correct": "B",
        "topic": "09-dars: performance.now() aniqligi",
        "expl": "performance.now() mikrosekundlargacha aniqlikdagi suzuvchi nuqtali vaqtni berib, reaktsiya o'yinida aniq farqni o'lchaydi."
    },
    # 8. Steady
    {
        "text": "10-darsda brauzerda dastur kodidagi xatolar va console.log natijalari qayerda ko'rinadi?",
        "a": "Kompyuterning 'Mening kompyuterim' oynasida.",
        "b": "Brauzer DevTools ning 'Console' (Konsol) panelida.",
        "c": "Faqat Word dasturida.",
        "d": "Telefon ekranida.",
        "e": "Hech qayerda ko'rinmaydi.",
        "correct": "B",
        "topic": "10-dars: DevTools Konsoli",
        "expl": "Dasturchilar kodni sinash va qayerda xato ketganini bilish uchun brauzerning Console oynasiga qaraydi."
    },
    # 9. Tricky (Real Knowledge)
    {
        "text": "11-darsda LocalStorage ga obyektni saqlashda JSON.stringify() ishlatilmasa, brauzerda qanday kutilmagan xato yuz beradi?",
        "a": "Kompyuter o'chib qoladi.",
        "b": "Obyekt o'rniga yaroqsiz '[object Object]' degan matn yozilib qoladi va ma'lumotlar yo'qoladi.",
        "c": "Barcha ballar avtomatik 100 ga aylanadi.",
        "d": "Brauzer yopilib ketadi.",
        "e": "O'yin tezlashib ketadi.",
        "correct": "B",
        "topic": "11-dars: LocalStorage va JSON.stringify",
        "expl": "LocalStorage faqat matn saqlaydi, shuning uchun obyektni JSON.stringify() qilmasangiz, u '[object Object]' ga aylanib buziladi."
    },
    # 10. Steady
    {
        "text": "12-darsda o'yinni do'stlarga havola orqali ulashish uchun Vercel xizmatiga yuklaganda qaysi xavfsiz protokol beriladi?",
        "a": "Oddiy shifrlanmagan HTTP.",
        "b": "Yashil qulf belgili xavfsiz HTTPS va SSL sertifikati.",
        "c": "Faqat Bluetooth aloqasi.",
        "d": "Faqat kompyuter ichidagi localhost.",
        "e": "Faqat kabel orqali ulanish.",
        "correct": "B",
        "topic": "12-dars: Vercel Deploy va HTTPS",
        "expl": "Vercel o'yinni butun dunyo ochishi uchun avtomatik ravishda xavfsiz HTTPS havolasini taqdim etadi."
    },
    # 11. Steady
    {
        "text": "13-darsda JavaScript orqali 2D o'yin grafikasi chiziladigan maxsus HTML tegi qaysi?",
        "a": "<table>",
        "b": "<canvas>",
        "c": "<button>",
        "d": "<audio>",
        "e": "<link>",
        "correct": "B",
        "topic": "13-dars: HTML5 Canvas",
        "expl": "<canvas> tegi JavaScript yordamida harakatlanuvchi qahramonlar, to'siqlar va 2D o'yinlarni chizish maydonidir."
    },
    # 12. Steady
    {
        "text": "13-darsda o'yin soniyasiga 60 kadr (60 FPS) silliq harakatlanishi uchun qaysi funksiya chaqiriladi?",
        "a": "setInterval(update, 5000);",
        "b": "requestAnimationFrame(gameLoop);",
        "c": "window.close();",
        "d": "document.clear();",
        "e": "alert('kadr');",
        "correct": "B",
        "topic": "13-dars: requestAnimationFrame va 60 FPS",
        "expl": "requestAnimationFrame ekranning yangilanishiga moslashib, harakatlarni qotmasdan silliq (60 FPS) chizadi."
    },
    # 13. Steady
    {
        "text": "14-darsda o'yinda yangi paydo bo'lgan dushmanni dushmanlar massiviga qo'shish uchun qaysi metod ishlatiladi?",
        "a": "enemies.pop()",
        "b": "enemies.push(newEnemy)",
        "c": "enemies.slice()",
        "d": "enemies.clear()",
        "e": "enemies.reverse()",
        "correct": "B",
        "topic": "14-dars: Massivga qo'shish (push)",
        "expl": "Massivning .push() metodi yangi elementni (yangi dushmanni) massivning oxiriga qo'shadi."
    },
    # 14. Tricky (Real Knowledge)
    {
        "text": "15-darsda platformer o'yinida gravitatsiya va sakrash fizikasi qaysi formulalar bilan hisoblanadi?",
        "a": "player.x = player.x * 2;",
        "b": "player.vy += gravity; player.y += player.vy;",
        "c": "player.y = 0;",
        "d": "player.speed = player.speed + 10;",
        "e": "player.jump = 'yes';",
        "correct": "B",
        "topic": "15-dars: Gravitatsiya formulasi",
        "expl": "Har bir kadrda vertikal tezlikka gravitatsiya qo'shiladi (vy += gravity), keyin qahramon balandligi o'zgaradi (y += vy)."
    },
    # 15. Tricky (Real Knowledge)
    {
        "text": "15-darsda AABB (Axis-Aligned Bounding Box) to'qnashuv algoritmi qahramonning tangaga tekkanini qanday biladi?",
        "a": "Faqat ikkala obyektning rangi qizil bo'lganda.",
        "b": "Qahramon to'rtburchagi va tanga to'rtburchagining to'rtta chegarasi (chap, o'ng, tepa, past) bir vaqtda kesishganda.",
        "c": "Faqat sichqoncha bilan bosilganda.",
        "d": "Qahramon to'xtab qolganda.",
        "e": "O'yin vaqti tugaganda.",
        "correct": "B",
        "topic": "15-dars: AABB To'qnashuv Mantiqi",
        "expl": "AABB to'qnashuvi ikki to'rtburchakning X va Y o'qlari bo'yicha chegaralari bir-birining ustiga tushganini tekshiradi."
    },
    # 16. Steady
    {
        "text": "17-darsda tashqi audio fayllarsiz toza ovoz effektlarini generatsiya qiluvchi brauzer vositasi nima?",
        "a": "Faqat video pleyer.",
        "b": "Web Audio API (AudioContext va OscillatorNode).",
        "c": "Faqat telefon qo'ng'irog'i.",
        "d": "Faqat mikrofon kabeli.",
        "e": "Faqat kompyuter klaviaturasi.",
        "correct": "B",
        "topic": "17-dars: Web Audio API",
        "expl": "Web Audio API dinamiklar orqali to'g'ridan-to'g'ri tovush to'lqinlarini (sinus, kvadrat) sintez qiladi."
    },
    # 17. Tricky (Real Knowledge)
    {
        "text": "18-darsda qahramon o'ng tomonga yugurganda kamerani uning orqasidan ergashtirish Canvas da qanday qilinadi?",
        "a": "Kompyuter ekranini o'ngga surish orqali.",
        "b": "Chizishdan oldin ctx.translate(-cameraX, 0) orqali kanvas koordinatasini teskari yo'nalishga siljitish bilan.",
        "c": "Qahramonni ekranning o'ng burchagida to'xtatib qo'yish bilan.",
        "d": "Canvasni o'chirib qayta ochish bilan.",
        "e": "O'yinni to'xtatib qo'yish bilan.",
        "correct": "B",
        "topic": "18-dars: Kamera Skrollingi (ctx.translate)",
        "expl": "Kamera qahramon bilan birga siljishi uchun barcha obyektlar ctx.translate(-camX, 0) ofseti bilan chiziladi."
    },
    # 18. Steady
    {
        "text": "19-darsda smartfon sensor ekraniga barmoq tekkan paytda qaysi hodisa ishga tushadi?",
        "a": "onhover",
        "b": "touchstart",
        "c": "keypress",
        "d": "mouseleave",
        "e": "onsubmit",
        "correct": "B",
        "topic": "19-dars: Touch Hodisalari",
        "expl": "Mobil qurilmalarda ekranga barmoq tekkanda 'touchstart', siljitganda 'touchmove', olganda 'touchend' sodir bo'ladi."
    },
    # 19. Steady
    {
        "text": "21-darsdagi 'FUT Card Studio' loyihasida o'yinchining OVR qisqartmasi nimani bildiradi?",
        "a": "Futbolchining oyoq kiyimi o'lchami.",
        "b": "Overall Rating — futbolchi kartasining umumiy reyting bali.",
        "c": "Futbolchining telefon raqami.",
        "d": "Kartaning narxi.",
        "e": "O'yin vaqti.",
        "correct": "B",
        "topic": "21-dars: FUT OVR Reytingi",
        "expl": "OVR (Overall Rating) — futbolchining tezligi, zarbasi va uzatmalari asosida hisoblangan umumiy mahorat bali."
    },
    # 20. Tricky (Real Knowledge)
    {
        "text": "22-darsdagi 'FUT Squad Builder' loyihasida bitta klubda o'ynaydigan ikkita futbolchi tarkibga qo'yilsa nima bo'ladi?",
        "a": "Ikkala futbolchi ham qizil kartochka oladi.",
        "b": "Ularning orasida klub aloqasi bog'lanib, jamoaning Kimyo (Chemistry) balli maksimal (+3) darajada oshadi.",
        "c": "O'yin to'xtab qoladi.",
        "d": "Ularning kiyim raqami o'zgaradi.",
        "e": "Futbolchilar jamoadan chiqib ketadi.",
        "correct": "B",
        "topic": "22-dars: FUT Kimyo Graflari",
        "expl": "Bir xil klubdagi futbolchilar eng kuchli aloqa (+3 kimyo) hosil qilib, butun jamoaning sinergiyasini oshiradi."
    },
    # 21. Steady
    {
        "text": "24-darsda FUT Transfer bozorida EA nega har bir sotuvdan 5% soliq (Coin Sink) oladi?",
        "a": "O'yinchilarni xafa qilish uchun.",
        "b": "O'yinda virtual pullar haddan tashqari ko'payib ketmasligi va narxlar oshib ketmasligi (inflyatsiyani to'xtatish) uchun.",
        "c": "Haqiqiy do'kondan kiyim sotib olish uchun.",
        "d": "Kompyuterlarni tozalash uchun.",
        "e": "Barcha o'yinchilarni tekin qilish uchun.",
        "correct": "B",
        "topic": "24-dars: FUT 5% Soliq va Iqtisodiyot",
        "expl": "5% transfer solig'i (Coin Sink) iqtisodiyotdagi ortiqcha tangalarni yo'qotib, narxlarni barqaror ushlab turadi."
    },
    # 22. Steady
    {
        "text": "25-darsdagi 'Target Jarvis' sun'iy intellektida ovozni matnga aylantirish uchun qaysi Web API ishlatildi?",
        "a": "window.alert()",
        "b": "Web Speech API (SpeechRecognition).",
        "c": "navigator.vibrate()",
        "d": "localStorage.clear()",
        "e": "document.body.remove()",
        "correct": "B",
        "topic": "25-dars: Target Jarvis va Ovoz",
        "expl": "SpeechRecognition interfeysi mikrofon orqali aytilgan so'zlarni taniydi va ularni matn shaklida dasturga uzatadi."
    },
    # 23. Steady
    {
        "text": "26-darsda 'Kiber-Ko'z' veb-kamera orqali harakatni qanday payqaydi?",
        "a": "Xonadagi havo haroratini o'lchash orqali.",
        "b": "Kameraning oldingi va keyingi kadrlari orasidagi piksellarning rang o'zgarishini taqqoslash orqali.",
        "c": "Faqat odamning ismini chaqirish orqali.",
        "d": "Ekranni qora qilib qo'yish orqali.",
        "e": "Faqat sichqoncha qimirlaganda.",
        "correct": "B",
        "topic": "26-dars: Veb-kamera Harakat Detektori",
        "expl": "Harakat detektori kadrlar orasidagi piksellar farqini hisoblaydi: agar o'zgargan piksellar ko'p bo'lsa, demak harakat bor."
    },
    # 24. Tricky (Real Knowledge)
    {
        "text": "27-darsda Biometrik Kiber-Skaner Face ID da qog'ozdagi soxta fotosuratni (2D Photo Spoofing) qanday fosh etadi?",
        "a": "Qog'ozning qalinligini o'lchab.",
        "b": "Liveness Engine yordamida: ko'z qisish (EAR formulasi) va boshning burilishini tekshirib, tirik inson ekanini isbotlash orqali.",
        "c": "Foydalanuvchidan telefon raqamini so'rab.",
        "d": "Kamerani o'chirib yoqish orqali.",
        "e": "Faqat ko'zoynak taqqan odamlarni tekshirib.",
        "correct": "B",
        "topic": "27-dars: Face ID va Liveness Anti-Spoofing",
        "expl": "Anti-Spoofing tizimi odamdan ko'zini miltillatishni (EAR) yoki boshini burishni talab qilib, statik fotosuratlarni rad etadi."
    },
    # 25. Steady
    {
        "text": "7–8-sinf Vibecoding dasturchisining eng asosiy ko'nikmasi nima?",
        "a": "Kodni tushunmasdan ko'chirib olish.",
        "b": "G'oyani interaktiv veb-sayt yoki 2D o'yinga aylantirish, AI yordamida kodni tushunib yozish va xatolarni mustaqil to'g'rilash.",
        "c": "Hech qachon o'z loyihasini internetga chiqarmaslik.",
        "d": "Faqat bitta tugmali o'yinlar yasash.",
        "e": "Kiber-xavfsizlik qoidalarini e'tiborsiz qoldirish.",
        "correct": "B",
        "topic": "Xulosa: 7-8-sinf Dasturchi Ko'nikmasi",
        "expl": "7-8 sinf o'quvchisi interaktiv ilovalar yarata oladi, DevTools bilan xatolarni topadi va zamonaviy veb-texnologiyalardan foydalanadi."
    }
]

QUESTIONS_7_8_RU = [
    # 1. Steady
    {
        "text": "Согласно Уроку 1, как Большие Языковые Модели (LLM) помогают нам в веб-разработке?",
        "a": "Они протирают монитор от пыли.",
        "b": "Они понимают задачи из нашего промпта и быстро генерируют рабочий код на HTML, CSS и JavaScript.",
        "c": "Они удаляют все системные файлы с компьютера.",
        "d": "Они просто играют в компьютерные игры вместо нас.",
        "e": "Они работают исключительно как простейший калькулятор.",
        "correct": "B",
        "topic": "Урок 01: Модели LLM и генерация кода",
        "expl": "LLM понимают инструкции на человеческом языке и мгновенно создают рабочий код веб-приложений и игр."
    },
    # 2. Steady
    {
        "text": "Как правильно составить промпт на Уроке 2 ('AI Duel'), чтобы получить самый качественный и точный код?",
        "a": "Написать всего одно размытое слово.",
        "b": "Четко описать, что должна делать программа, какие языки использовать (HTML/CSS/JS) и какие кнопки должны быть.",
        "c": "Отправлять нейросети только смайлики.",
        "d": "Писать промпт только черными буквами.",
        "e": "Не давать никаких инструкций и ждать чуда.",
        "correct": "B",
        "topic": "Урок 02: Структура качественного промпта",
        "expl": "Четкое описание интерфейса, логики и используемого стека гарантирует получение качественного кода с первой попытки."
    },
    # 3. Steady
    {
        "text": "В чем заключается главное преимущество векторной графики SVG (Урок 3)?",
        "a": "Она бывает исключительно черного цвета.",
        "b": "Она состоит из математических линий, поэтому не размывается и остается четкой при любом увеличении экрана.",
        "c": "Она занимает на диске 10 гигабайт.",
        "d": "Ее невозможно открыть в браузере.",
        "e": "Она используется только для прослушивания музыки.",
        "correct": "B",
        "topic": "Урок 03: Векторная графика SVG",
        "expl": "SVG масштабируется без потери качества на любых экранах, так как строится на векторах, а не на пикселях."
    },
    # 4. Steady
    {
        "text": "Какой семантический тег HTML используется на Уроке 5 для выделения основного контента страницы?",
        "a": "<div>",
        "b": "<main>",
        "c": "<span>",
        "d": "<br>",
        "e": "<input>",
        "correct": "B",
        "topic": "Урок 05: Семантический тег <main>",
        "expl": "Тег <main> четко указывает браузеру и поисковикам, где расположена ключевая смысловая часть страницы."
    },
    # 5. Steady
    {
        "text": "Какое свойство CSS Flexbox центрирует элементы вдоль главной горизонтальной оси (Урок 7)?",
        "a": "align-items: center;",
        "b": "justify-content: center;",
        "c": "text-align: middle;",
        "d": "display: hidden;",
        "e": "float: center;",
        "correct": "B",
        "topic": "Урок 07: Flexbox и justify-content",
        "expl": "Свойство justify-content: center выравнивает дочерние элементы точно по центру вдоль главной оси строки."
    },
    # 6. Steady
    {
        "text": "Как в коде JavaScript слушать нажатие (клик) по кнопке (Урок 8)?",
        "a": "button.startClick()",
        "b": "button.addEventListener('click', () => { ... });",
        "c": "window.destroy()",
        "d": "document.write('click')",
        "e": "console.clear()",
        "correct": "B",
        "topic": "Урок 08: События и addEventListener",
        "expl": "Метод addEventListener('click', fn) вешает слушатель события, реагируя на каждый щелчок мыши."
    },
    # 7. Tricky (Real Knowledge)
    {
        "text": "Почему в игре 'Кибер-Реакция' (Урок 9) вместо Date.now() была использована функция performance.now()?",
        "a": "Потому что Date.now() требует подключения к интернету.",
        "b": "Потому что performance.now() измеряет время с долями миллисекунды, гарантируя сверхточный замер реакции человека.",
        "c": "Потому что она ускоряет процессор компьютера.",
        "d": "Потому что performance.now() только издает звуки.",
        "e": "Потому что она красит экран в красный цвет.",
        "correct": "B",
        "topic": "Урок 09: Высокая точность performance.now()",
        "expl": "performance.now() выдает время с микросекундной точностью, позволяя фиксировать даже минимальные доли реакции."
    },
    # 8. Steady
    {
        "text": "Где в браузере разработчик смотрит ошибки JavaScript и выводы функции console.log (Урок 10)?",
        "a": "В папке 'Мой компьютер'.",
        "b": "На вкладке 'Console' (Консоль) в панели DevTools браузера.",
        "c": "Только в программе Microsoft Word.",
        "d": "На экране смартфона.",
        "e": "Они нигде не отображаются.",
        "correct": "B",
        "topic": "Урок 10: Вкладка Console в DevTools",
        "expl": "Консоль браузера (F12 -> Console) — главное рабочее место для поиска багов и проверки работы скриптов."
    },
    # 9. Tricky (Real Knowledge)
    {
        "text": "Что произойдет в LocalStorage, если сохранить объект без вызова JSON.stringify() (Урок 11)?",
        "a": "Компьютер немедленно выключится.",
        "b": "Вместо данных запишется бесполезная строка '[object Object]', и все поля объекта будут потеряны.",
        "c": "Все очки автоматически станут равны 100.",
        "d": "Браузер навсегда закроется.",
        "e": "Игра станет работать в два раза быстрее.",
        "correct": "B",
        "topic": "Урок 11: Ошибка без JSON.stringify",
        "expl": "LocalStorage хранит только строки; попытка сохранить чистый объект приводит к его приведению в строку '[object Object]'."
    },
    # 10. Steady
    {
        "text": "Какой протокол безопасности автоматически выдается при публикации игры на платформе Vercel (Урок 12)?",
        "a": "Устаревший незашифрованный HTTP.",
        "b": "Безопасный протокол HTTPS с зеленым значком замка и сертификатом SSL.",
        "c": "Только беспроводной Bluetooth.",
        "d": "Только локальный localhost.",
        "e": "Только проводной кабель.",
        "correct": "B",
        "topic": "Урок 12: Публикация на Vercel и HTTPS",
        "expl": "Vercel автоматически защищает проект бесплатным SSL-сертификатом, делая ссылку общедоступной и безопасной."
    },
    # 11. Steady
    {
        "text": "Какой HTML-тег предназначен для рисования 2D игр с помощью JavaScript (Урок 13)?",
        "a": "<table>",
        "b": "<canvas>",
        "c": "<button>",
        "d": "<audio>",
        "e": "<link>",
        "correct": "B",
        "topic": "Урок 13: Холст HTML5 Canvas",
        "expl": "Тег <canvas> — это интерактивный холст, на котором скрипт рисует графику, персонажей и физику игры."
    },
    # 12. Steady
    {
        "text": "Какая функция обеспечивает плавную анимацию игры со скоростью 60 кадров в секунду (60 FPS) на Уроке 13?",
        "a": "setInterval(update, 5000);",
        "b": "requestAnimationFrame(gameLoop);",
        "c": "window.close();",
        "d": "document.clear();",
        "e": "alert('кадр');",
        "correct": "B",
        "topic": "Урок 13: Анимация через requestAnimationFrame",
        "expl": "requestAnimationFrame синхронизируется с частотой развертки монитора, обеспечивая идеальную плавность."
    },
    # 13. Steady
    {
        "text": "Какой метод массива в JavaScript добавляет вновь появившегося врага в список врагов (Урок 14)?",
        "a": "enemies.pop()",
        "b": "enemies.push(newEnemy)",
        "c": "enemies.slice()",
        "d": "enemies.clear()",
        "e": "enemies.reverse()",
        "correct": "B",
        "topic": "Урок 14: Метод push в массивах",
        "expl": "Метод .push() добавляет новый элемент в конец массива объектов."
    },
    # 14. Tricky (Real Knowledge)
    {
        "text": "По каким формулам рассчитывается гравитация и падение героя в платформере на Уроке 15?",
        "a": "player.x = player.x * 2;",
        "b": "player.vy += gravity; player.y += player.vy;",
        "c": "player.y = 0;",
        "d": "player.speed = player.speed + 10;",
        "e": "player.jump = 'yes';",
        "correct": "B",
        "topic": "Урок 15: Формула гравитации",
        "expl": "Гравитация непрерывно увеличивает вертикальную скорость (vy += g), а затем координата Y меняется на эту скорость."
    },
    # 15. Tricky (Real Knowledge)
    {
        "text": "Как алгоритм AABB (Axis-Aligned Bounding Box) определяет, что персонаж коснулся монетки (Урок 15)?",
        "a": "Только когда у обоих объектов одинаковый красный цвет.",
        "b": "Когда прямоугольник героя и прямоугольник монетки одновременно пересекаются по всем четырем границам (X и Y).",
        "c": "Только при нажатии кнопкой мыши.",
        "d": "Когда герой полностью остановился.",
        "e": "Только когда истекло игровое время.",
        "correct": "B",
        "topic": "Урок 15: Алгоритм коллизий AABB",
        "expl": "AABB проверяет перекрытие проекций прямоугольников по горизонтали и вертикали без учета угла поворота."
    },
    # 16. Steady
    {
        "text": "Какой веб-инструмент синтезирует звуковые эффекты в браузере без скачивания внешних файлов (Урок 17)?",
        "a": "Обычный видеоплеер.",
        "b": "Web Audio API (AudioContext и генератор OscillatorNode).",
        "c": "Телефонный звонок.",
        "d": "Провод от наушников.",
        "e": "Клавиатура ноутбука.",
        "correct": "B",
        "topic": "Урок 17: Звуковой движок Web Audio API",
        "expl": "Web Audio API позволяет программно генерировать чистые звуковые волны прямо через звуковую карту."
    },
    # 17. Tricky (Real Knowledge)
    {
        "text": "Как в Canvas заставить камеру следовать за бегущим вправо героем (Урок 18)?",
        "a": "Передвинуть экран монитора руками вправо.",
        "b": "Перед каждым кадром вызывать ctx.translate(-cameraX, 0), смещая координаты холста в обратную сторону.",
        "c": "Остановить персонажа в правом углу навсегда.",
        "d": "Закрыть Canvas и открыть заново.",
        "e": "Остановить выполнение игры.",
        "correct": "B",
        "topic": "Урок 18: Смещение камеры ctx.translate",
        "expl": "Камера смещается вызовом ctx.translate(-camX, 0), благодаря чему весь мир плавно прокручивается мимо игрока."
    },
    # 18. Steady
    {
        "text": "Какое событие JavaScript срабатывает в момент касания пальцем сенсорного экрана телефона (Урок 19)?",
        "a": "onhover",
        "b": "touchstart",
        "c": "keypress",
        "d": "mouseleave",
        "e": "onsubmit",
        "correct": "B",
        "topic": "Урок 19: Сенсорные события touchstart",
        "expl": "На смартфонах касание пальца вызывает событие 'touchstart', движение — 'touchmove', отрыв — 'touchend'."
    },
    # 19. Steady
    {
        "text": "Что означает аббревиатура OVR на карточке футболиста в проекте 'FUT Card Studio' (Урок 21)?",
        "a": "Размер футбольной обуви.",
        "b": "Overall Rating — общий итоговый рейтинг мастерства игрока.",
        "c": "Номер телефона спортсмена.",
        "d": "Стоимость карточки в магазине.",
        "e": "Время начала матча.",
        "correct": "B",
        "topic": "Урок 21: Общий рейтинг OVR в FUT",
        "expl": "OVR (Overall Rating) — ключевое число на карточке, показывающее общий класс и мастерство футболиста."
    },
    # 20. Tricky (Real Knowledge)
    {
        "text": "Что произойдет в 'FUT Squad Builder' (Урок 22), если поставить рядом двух игроков из одного клуба?",
        "a": "Оба игрока получат красную карточку.",
        "b": "Между ними образуется клубная связь, дающая максимальный бонус командной химии (+3 Chemistry).",
        "c": "Игра немедленно заблокируется.",
        "d": "У них поменяются номера на форме.",
        "e": "Футболисты уйдут из состава.",
        "correct": "B",
        "topic": "Урок 22: Граф командной химии FUT",
        "expl": "Игроки одного клуба образуют самую крепкую синергию, принося максимум очков командной химии."
    },
    # 21. Steady
    {
        "text": "Почему на трансферном рынке FUT разработчики ввели 5% налог с каждой продажи (Урок 24)?",
        "a": "Чтобы расстроить игроков.",
        "b": "Чтобы сдерживать инфляцию, выводя лишние монеты из игры и удерживая стабильные цены на игроков.",
        "c": "Чтобы купить реальную одежду в магазине.",
        "d": "Чтобы стереть старые компьютеры.",
        "e": "Чтобы сделать всех футболистов бесплатными.",
        "correct": "B",
        "topic": "Урок 24: Налог 5% Coin Sink в FUT",
        "expl": "Механизм 5% налога (Coin Sink) выводит избыточную виртуальную валюту из оборота, предотвращая гиперинфляцию."
    },
    # 22. Steady
    {
        "text": "Какой браузерный Web API распознает человеческую речь в текст в проекте 'Target Jarvis' (Урок 25)?",
        "a": "window.alert()",
        "b": "Web Speech API (интерфейс SpeechRecognition).",
        "c": "navigator.vibrate()",
        "d": "localStorage.clear()",
        "e": "document.body.remove()",
        "correct": "B",
        "topic": "Урок 25: Распознавание голоса в Target Jarvis",
        "expl": "Интерфейс SpeechRecognition слушает микрофон и превращает слова пользователя в строку текста."
    },
    # 23. Steady
    {
        "text": "Как веб-камера в проекте 'Кибер-Глаз' обнаруживает движение в комнате (Урок 26)?",
        "a": "Измеряя температуру воздуха термометром.",
        "b": "Сравнивая изменение цвета пикселей между предыдущим и текущим видеокадрами.",
        "c": "Громко выкрикивая имя человека.",
        "d": "Заливая весь экран черной краской.",
        "e": "Только когда двигается компьютерная мышка.",
        "correct": "B",
        "topic": "Урок 26: Детектор движения через веб-камеру",
        "expl": "Алгоритм сравнивает два соседних кадра: если разница в цветах пикселей превысила порог — зафиксировано движение."
    },
    # 24. Tricky (Real Knowledge)
    {
        "text": "Как биометрический сканер Face ID отличает живого человека от распечатанной фотографии (Урок 27)?",
        "a": "Измеряя толщину листа бумаги штангенциркулем.",
        "b": "С помощью алгоритма Liveness: проверки моргания глаз (формула EAR) и естественных поворотов головы.",
        "c": "Запрашивая номер сотового телефона.",
        "d": "Выключением и включением веб-камеры.",
        "e": "Проверяя только людей в очках.",
        "correct": "B",
        "topic": "Урок 27: Face ID и защита Anti-Spoofing",
        "expl": "Движок Liveness требует живой реакции (моргание по метрике EAR), отвергая неподвижные фото и плоские экраны."
    },
    # 25. Steady
    {
        "text": "В чем заключается главное умение разработчика (Vibecoder) 7–8 классов?",
        "a": "Слепо копировать чужой код без понимания.",
        "b": "Уметь воплотить идею в интерактивную веб-игру, создавать код с помощью ИИ и самостоятельно находить ошибки в DevTools.",
        "c": "Никогда не показывать свои проекты другим.",
        "d": "Создавать игры, где есть только одна кнопка.",
        "e": "Игнорировать цифровую безопасность.",
        "correct": "B",
        "topic": "Итог: Навыки разработчика 7–8 классов",
        "expl": "Vibecoder умеет проектировать интерфейсы, оживлять их физикой и логикой и грамотно работать с AI-инструментами."
    }
]

print("Grade 7-8 Vibecoding test data loaded (18 steady + 7 tricky). Teacher: Ismoiljon Usmonov.")
