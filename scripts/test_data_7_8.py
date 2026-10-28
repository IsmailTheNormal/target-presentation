#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Target International School — 7–8-Sinf Vibecoding Test Ma'lumotlari
Fan: Vibecoding (Game Dev, Interaktiv Veb va Biometrik Muhandislik)
O'qituvchi: Ismoiljon Usmonov · Yunusobod filiali

Struktura:
- 25 ta tushunarli, aniq, qulay va bolalarbop savollar (Steady Easy)
- Veb-platformadagi (index.html va classes/7-8-sinf/) darslar asosida tuzilgan
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
        {"grade": "A'lo (5)", "range": "22 – 25 ball", "desc": "Canvas, Game Loop, o'yin fizikasi va Web API bo'yicha mukammal bilim"},
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
    {
        "text": "2-darsdagi 'AI Duel' darsida AI ga qanday prompt berilsa eng yaxshi natija olinadi?",
        "a": "Faqat bitta noaniq so'z yozilsa.",
        "b": "Dastur nima qilishi kerakligi, qaysi tilda yozilishi va qanday tugmalar bo'lishi aniq ko'rsatilsa.",
        "c": "Faqat kulgili stikerlar yuborilsa.",
        "d": "Prompt faqat qora rangda yozilsa.",
        "e": "AI ga hech qanday talab bermasdan o'ziga tashlab qo'yilsa.",
        "correct": "B",
        "topic": "02-dars: Sifatli Prompt Tuzilishi",
        "expl": "Aniq rollar, texnologiya (HTML/CSS/JS) va qoidalar ko'rsatilgan prompt eng sifatli natijani beradi."
    },
    {
        "text": "3-darsda o'rganilgan SVG (Scalable Vector Graphics) formatining asosiy afzalligi nimada?",
        "a": "U faqat qora rangda bo'ladi.",
        "b": "U vektor chiziqlardan iborat bo'lgani uchun, qanchalik kattalashtirilsa ham xiralashmaydi va tiniq turadi.",
        "c": "U kompyuterda 10 gigabayt joy oladi.",
        "d": "Uni brauzerda ochib bo'lmaydi.",
        "e": "U faqat musiqa tinglash uchun xizmat qiladi.",
        "correct": "B",
        "topic": "03-dars: SVG Vektor Grafikasi",
        "expl": "SVG pikselli rasm emas, balki matematik vektor chiziqlar bo'lib, istalgan ekranda tiniq ko'rinadi."
    },
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
    {
        "text": "9-darsdagi 'Kiber-Reaksiya' mini-o'yinida o'yinchining qanday qobiliyati o'lchanadi?",
        "a": "O'yinchining klaviaturani qanchalik qattiq ura olishi.",
        "b": "Ekran yashil rangga kirgan zahoti tugmani qanchalik tez bosishi, ya'ni reaktsiya vaqti.",
        "c": "O'yinchining inglizcha so'zlarni qanchalik tez o'qishi.",
        "d": "Kompyuterning internet tezligi.",
        "e": "Sichqonchaning qanchalik og'irligi.",
        "correct": "B",
        "topic": "09-dars: Kiber-Reaksiya va Reaksiya Vaqti",
        "expl": "Kiber-Reaksiya o'yini ekranda signal berilishi bilan o'yinchining reaksiyasini millisekundlarda o'lchaydi."
    },
    {
        "text": "10-darsda brauzerda dastur kodidagi xatolar va console.log natijalari qayerda ko'rinadi?",
        "a": "Kompyuterning 'Mening kompyuterim' papkasida.",
        "b": "Brauzer DevTools ning 'Console' (Konsol) panelida.",
        "c": "Faqat Word dasturida.",
        "d": "Telefon ekranida.",
        "e": "Hech qayerda ko'rinmaydi.",
        "correct": "B",
        "topic": "10-dars: DevTools Konsoli",
        "expl": "Dasturchilar kodni sinash va xatolarni aniqlash uchun brauzerning Console oynasiga qaraydi."
    },
    {
        "text": "11-darsda LocalStorage ga saqlangan o'yin rekordlari qachon o'chib ketadi?",
        "a": "Brauzer oynasi yopilishi bilan darhol o'chadi.",
        "b": "O'chib ketmaydi: sahifa qayta yangilanganda ham, brauzer yopilib qayta ochilganda ham saqlanib turadi.",
        "c": "Faqat kompyuter zaryadi tugaganda o'chadi.",
        "d": "Har 5 soniyada avtomatik o'chib turadi.",
        "e": "Klaviatura bosilishi bilan o'chadi.",
        "correct": "B",
        "topic": "11-dars: LocalStorage doimiyligi",
        "expl": "LocalStorage ma'lumotlarni uzoq muddat saqlaydi, shuning uchun rekord ballar yo'qolmaydi."
    },
    {
        "text": "12-darsda o'yinni do'stlarga havola orqali ulashish uchun Vercel xizmatiga yuklaganda qaysi xavfsiz protokol beriladi?",
        "a": "Oddiy shifrlanmagan HTTP.",
        "b": "Yashil qulf belgili xavfsiz HTTPS va bepul SSL sertifikati.",
        "c": "Faqat Bluetooth aloqasi.",
        "d": "Faqat kompyuter ichidagi localhost.",
        "e": "Faqat kabel orqali ulanish.",
        "correct": "B",
        "topic": "12-dars: Vercel Deploy va HTTPS",
        "expl": "Vercel o'yinni butun dunyo ochishi uchun avtomatik ravishda xavfsiz HTTPS havolasini taqdim etadi."
    },
    {
        "text": "13-darsda JavaScript orqali 2D o'yin grafikasi chiziladigan maxsus HTML tegi qaysi?",
        "a": "<table>",
        "b": "<canvas>",
        "c": "<button>",
        "d": "<audio>",
        "e": "<link>",
        "correct": "B",
        "topic": "13-dars: HTML5 Canvas",
        "expl": "<canvas> tegi JavaScript yordamida qahramonlar, to'siqlar va 2D o'yinlarni chizish maydonidir."
    },
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
    {
        "text": "15-darsda platformer o'yinida qahramon sakragandan so'ng yerga qaytib tushishini nima ta'minlaydi?",
        "a": "Kompyuter ekranining yorug'ligi.",
        "b": "Gravitatsiya (tortishish kuchi) simulyatsiyasi.",
        "c": "O'yinchi sichqonchasining tezligi.",
        "d": "Klaviatura tugmalari soni.",
        "e": "Faqat o'yin musiqasi.",
        "correct": "B",
        "topic": "15-dars: O'yin Fizikasi va Gravitatsiya",
        "expl": "Gravitatsiya kuchi qahramon sakraganda uni pastga tortib, tabiiy tushish harakatini hosil qiladi."
    },
    {
        "text": "15-darsda qahramon tangaga yoki dushmanga tekkanini o'yin kodi qanday biladi?",
        "a": "Faqat ikkala obyektning rangi bir xil bo'lganda.",
        "b": "To'qnashuv (Collision) tekshiruvi orqali: qahramon va obyekt chegaralari ustma-ust tushganda.",
        "c": "Faqat sichqoncha bilan bosilganda.",
        "d": "Qahramon to'xtab qolganda.",
        "e": "O'yin vaqti tugaganda.",
        "correct": "B",
        "topic": "15-dars: To'qnashuv (Collision)",
        "expl": "To'qnashuv algoritmi qahramon va tanga koordinatalari kesishganini tekshirib, tegishni aniqlaydi."
    },
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
    {
        "text": "18-darsda qahramon katta xarita bo'ylab yugurganida kamera nima qiladi?",
        "a": "Kompyuter ekranini o'chirib qo'yadi.",
        "b": "Qahramon orqasidan ergashib siljiydi (Camera Scrolling) va yangi yo'llarni ko'rsatib boradi.",
        "c": "Qahramonni ekranning chetida to'xtatib qo'yadi.",
        "d": "O'yinni boshidan boshlaydi.",
        "e": "O'yinni butunlay to'xtatadi.",
        "correct": "B",
        "topic": "18-dars: Kamera Skrollingi",
        "expl": "Kamera skrollingi qahramonni markazda ushlab, orqa fon va dunyoni siljitib ko'rsatadi."
    },
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
    {
        "text": "21-darsdagi 'FUT Card Studio' loyihasida o'yinchining OVR qisqartmasi nimani bildiradi?",
        "a": "Futbolchining oyoq kiyimi o'lchami.",
        "b": "Overall Rating — futbolchi kartasining umumiy mahorat reytingi bali.",
        "c": "Futbolchining telefon raqami.",
        "d": "Kartaning narxi.",
        "e": "O'yin vaqti.",
        "correct": "B",
        "topic": "21-dars: FUT OVR Reytingi",
        "expl": "OVR (Overall Rating) — futbolchining tezligi, zarbasi va uzatmalari asosida hisoblangan umumiy mahorat bali."
    },
    {
        "text": "22-darsdagi 'FUT Squad Builder' loyihasida bir xil klubdagi futbolchilar birgalikda o'ynasa nima bo'ladi?",
        "a": "Ikkala futbolchi ham qizil kartochka oladi.",
        "b": "Ularning orasida klub aloqasi bog'lanib, jamoaning Kimyo (Chemistry) bali maksimal darajada oshadi.",
        "c": "O'yin to'xtab qoladi.",
        "d": "Ularning kiyim raqami o'zgaradi.",
        "e": "Futbolchilar jamoadan chiqib ketadi.",
        "correct": "B",
        "topic": "22-dars: FUT Kimyo Graflari",
        "expl": "Bir xil klubdagi futbolchilar eng kuchli aloqa hosil qilib, butun jamoaning o'yin sifatini oshiradi."
    },
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
    {
        "text": "26-darsda 'Kiber-Ko'z' veb-kamera orqali xonadagi harakatni qanday payqaydi?",
        "a": "Xonadagi havo haroratini o'lchash orqali.",
        "b": "Kameraning oldingi va keyingi kadrlari orasidagi piksellarning rang o'zgarishini taqqoslash orqali.",
        "c": "Faqat odamning ismini chaqirish orqali.",
        "d": "Ekranni qora qilib qo'yish orqali.",
        "e": "Faqat sichqoncha qimirlaganda.",
        "correct": "B",
        "topic": "26-dars: Veb-kamera Harakat Detektori",
        "expl": "Harakat detektori kadrlar orasidagi piksellar farqini hisoblaydi: agar o'zgargan piksellar ko'p bo'lsa, demak harakat bor."
    },
    {
        "text": "27-darsda Biometrik Face ID tizimi insonni qaysi belgilari orqali taniydi?",
        "a": "Insonning kiygan kiyimi rangi orqali.",
        "b": "Inson yuzining tuzilishi, ko'zlar, burun va qoshlar orasidagi masofalar (Face Landmarks) orqali.",
        "c": "Foydalanuvchining telefon raqami orqali.",
        "d": "Faqat poyabzal o'lchami orqali.",
        "e": "Faqat insonning bo'yi uzunligi orqali.",
        "correct": "B",
        "topic": "27-dars: Biometrik Face ID",
        "expl": "Face ID yuzdagi o'nlab nuqtalarni (Landmarks) skanerlab, har bir insonning o'ziga xos yuz xaritasini tekshiradi."
    },
    {
        "text": "7–8-sinf Vibecoding dasturchisining eng asosiy ko'nikmasi nima?",
        "a": "Kodni tushunmasdan ko'chirib olish.",
        "b": "G'oyani interaktiv veb-sayt yoki 2D o'yinga aylantirish, AI yordamida kod yozish va xatolarni mustaqil to'g'rilash.",
        "c": "Hech qachon o'z loyihasini internetga chiqarmaslik.",
        "d": "Faqat bitta tugmali o'yinlar yasash.",
        "e": "Kiber-xavfsizlik qoidalarini e'tiborsiz qoldirish.",
        "correct": "B",
        "topic": "Xulosa: 7-8-sinf Dasturchi Ko'nikmasi",
        "expl": "7-8 sinf o'quvchisi interaktiv ilovalar yarata oladi, DevTools bilan xatolarni topadi va zamonaviy veb-texnologiyalardan foydalanadi."
    }
]

QUESTIONS_7_8_RU = [
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
    {
        "text": "Какую способность игрока измеряет мини-игра 'Кибер-Реакция' на Уроке 9?",
        "a": "Силу удара пальцем по клавиатуре.",
        "b": "Скорость реакции: насколько быстро игрок успевает нажать на кнопку после того, как экран стал зеленым.",
        "c": "Скорость чтения текста на английском языке.",
        "d": "Скорость интернет-соединения в комнате.",
        "e": "Вес компьютерной мышки.",
        "correct": "B",
        "topic": "Урок 09: Скорость реакции",
        "expl": "Игра замеряет время между появлением зеленого сигнала и кликом игрока в миллисекундах."
    },
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
    {
        "text": "Когда стираются рекорды игры, сохраненные в LocalStorage (Урок 11)?",
        "a": "Они стираются сразу же при закрытии вкладки браузера.",
        "b": "Они не стираются: сохраняются даже при перезагрузке страницы и закрытии браузера.",
        "c": "Только когда в ноутбуке садится батарейка.",
        "d": "Они автоматически стираются каждые 5 секунд.",
        "e": "Они удаляются при первом нажатии пробела.",
        "correct": "B",
        "topic": "Урок 11: Постоянство LocalStorage",
        "expl": "LocalStorage надежно хранит рекорды на диске браузера, позволяя возвращаться к игре в любое время."
    },
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
    {
        "text": "Что заставляет героя в платформере возвращаться на землю после прыжка (Урок 15)?",
        "a": "Яркость подсветки экрана.",
        "b": "Симуляция гравитации (силы тяжести).",
        "c": "Скорость перемещения мышки.",
        "d": "Количество клавиш на клавиатуре.",
        "e": "Музыкальное сопровождение.",
        "correct": "B",
        "topic": "Урок 15: Физика и гравитация",
        "expl": "Гравитация непрерывно тянет персонажа вниз, делая прыжки естественными и плавными."
    },
    {
        "text": "Как код игры узнает, что герой дотронулся до монетки или врага (Урок 15)?",
        "a": "Только если у них совпал цвет заливки.",
        "b": "С помощью проверки столкновения (Collision): когда границы героя и объекта пересекаются.",
        "c": "Только при нажатии кнопкой мыши.",
        "d": "Когда герой полностью остановился.",
        "e": "Только когда истекло игровое время.",
        "correct": "B",
        "topic": "Урок 15: Проверка коллизий",
        "expl": "Алгоритм коллизий проверяет координаты объектов: при их наложении срабатывает сбор монетки или урон."
    },
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
    {
        "text": "Что делает камера в игре, когда герой бежит вперед по большому уровню (Урок 18)?",
        "a": "Выключает монитор компьютера.",
        "b": "Плавно следует за героем (Camera Scrolling), открывая новые участки игрового мира.",
        "c": "Останавливает героя у края экрана навсегда.",
        "d": "Перезапускает игру с начала.",
        "e": "Полностью закрывает игру.",
        "correct": "B",
        "topic": "Урок 18: Скроллинг камеры",
        "expl": "Скроллинг камеры удерживает персонажа в поле зрения, создавая ощущение движения по огромному миру."
    },
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
    {
        "text": "Что произойдет в 'FUT Squad Builder' (Урок 22), если поставить рядом двух игроков из одного клуба?",
        "a": "Оба игрока получат красную карточку.",
        "b": "Между ними образуется клубная связь, дающая максимальный бонус командной химии (Chemistry).",
        "c": "Игра немедленно заблокируется.",
        "d": "У них поменяются номера на форме.",
        "e": "Футболисты уйдут из состава.",
        "correct": "B",
        "topic": "Урок 22: Граф командной химии FUT",
        "expl": "Игроки одного клуба образуют самую крепкую синергию, принося максимум очков командной химии."
    },
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
    {
        "text": "По каким признакам биометрическая система Face ID распознает человека на Уроке 27?",
        "a": "По цвету футболки человека.",
        "b": "По уникальному строению лица: расстоянию между глазами, носом и губами (Face Landmarks).",
        "c": "По номеру мобильного телефона.",
        "d": "Только по размеру обуви.",
        "e": "Только по росту человека.",
        "correct": "B",
        "topic": "Урок 27: Биометрия Face ID",
        "expl": "Face ID сопоставляет ключевые ориентиры лица (Landmarks), создавая неповторимый биометрический профиль."
    },
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

print("Grade 7-8 Vibecoding test data loaded (Steady Easy). Teacher: Ismoiljon Usmonov.")
