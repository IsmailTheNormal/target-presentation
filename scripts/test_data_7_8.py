#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
7–8-Sinf: 25 Savolli Vibecoding Frontend, Canvas va O'yin Simulyatsiyasi Testi
O'qituvchi: Ismoiljon Usmonov · Target International School
Uzbek va Russian variantlari (5 ta variant: A, B, C, D, E)
"""

META_7_8_UZ = {
    "school_name": "TARGET INTERNATIONAL SCHOOL — YUNUSOBOD",
    "teacher_name": "Ismoiljon Usmonov",
    "exam_title": "7–8-SINF: VIBECODING FRONTEND, CANVAS VA O'YIN SIMULYATSIYASI",
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

KEYS_META_7_8_UZ = {
    "heading": "JAVOBLAR KALITI VA BAHOLASH MEZONI",
    "subheading": "O'qituvchi: Ismoiljon Usmonov · 7–8-sinf Vibecoding rasmiy kaliti (25 ta savol)",
    "table_headers": ["№", "Kalit", "Mavzu / Kompetensiya", "Izoh va Tushuntirish"],
    "scale_heading": "Rasmiy 25 Ballik Baholash Shkalasi:",
    "rubric_tiers": [
        {"grade": "A'lo (5)", "range": "22 – 25 ball", "desc": "Canvas, Game Loop, AABB fizikasi, FUT algoritmlari va Web API larni chuqur bilish"},
        {"grade": "Yaxshi (4)", "range": "18 – 21 ball", "desc": "Frontend va o'yin fizikasi yaxshi o'zlashtirilgan"},
        {"grade": "Qoniqarli (3)", "range": "13 – 17 ball", "desc": "DOM hodisalari va LocalStorage ni takrorlash lozim"},
        {"grade": "Qoniqarsiz (2)", "range": "0 – 12 ball", "desc": "Vibecoding dasturlash asoslari qayta o'rganilishi zarur"}
    ]
}

META_7_8_RU = {
    "school_name": "TARGET INTERNATIONAL SCHOOL — ЮНУСАБАД",
    "teacher_name": "Исмоилжон Усмонов",
    "exam_title": "7–8 КЛАСС: VIBECODING ФРОНТЕНД, CANVAS И ИГРОВЫЕ СИМУЛЯЦИИ",
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

KEYS_META_7_8_RU = {
    "heading": "КЛЮЧИ ОТВЕТОВ И КРИТЕРИИ ОЦЕНИВАНИЯ",
    "subheading": "Преподаватель: Исмоилжон Усмонов · Официальный ключ Vibecoding (7–8 класс, 25 вопросов)",
    "table_headers": ["№", "Ключ", "Тема / Компетенция", "Пояснение и Обоснование"],
    "scale_heading": "Официальная 25-балльная шкала оценивания:",
    "rubric_tiers": [
        {"grade": "Отлично (5)", "range": "22 – 25 баллов", "desc": "Глубокое понимание Canvas, Game Loop, физики AABB, FUT и браузерных Web API"},
        {"grade": "Хорошо (4)", "range": "18 – 21 балл", "desc": "Хорошее владение фронтендом и физикой двухмерных игр"},
        {"grade": "Удовлетворительно (3)", "range": "13 – 17 баллов", "desc": "Требуется повторение работы с событиями DOM и LocalStorage"},
        {"grade": "Неудовлетворительно (2)", "range": "0 – 12 баллов", "desc": "Необходимо повторное изучение базовых концепций Vibecoding"}
    ]
}

QUESTIONS_7_8_UZ = [
    {
        "text": "Vibecoding metodologiyasida dasturchining asosiy roli qanday o'zgaradi?",
        "a": "Dasturchi faqat matn teruvchiga aylanadi.",
        "b": "Dasturchi arxitektor va yo'naltiruvchi sifatida fikrlaydi: AI ga talab beradi, kodni tekshiradi, sinaydi va tizim integratsiyasini boshqaradi.",
        "c": "Dasturchi kompyuter ishlatishni to'xtatadi.",
        "d": "Faqat tayyor kutubxonalarni sotib oladi.",
        "e": "Faqat ingliz tilini tarjima qiladi.",
        "correct": "B",
        "topic": "Vibecoding Falsafasi",
        "expl": "Vibecoding da inson muhandislik qarorlarini qabul qiladi, AI esa sintaksis va kod yozish jarayonini tezlashtiradi."
    },
    {
        "text": "JavaScript-da DOM elementini topish va unga bosish hodisasini ulashning eng zamonaviy standarti qaysi?",
        "a": "document.write() va alert()",
        "b": "document.querySelector('#startBtn').addEventListener('click', handler);",
        "c": "window.navigate()",
        "d": "canvas.style()",
        "e": "css.bind('click')",
        "correct": "B",
        "topic": "DOM Hodisalari (Events)",
        "expl": "`querySelector` va `addEventListener` DOM bilan ishlashning eng toza va xavfsiz standartidir."
    },
    {
        "text": "O'yin tsiklida (Game Loop) animatsiyani sekunddagi kadrlar chastotasi (FPS) ga bog'liq qilmaslik uchun nimadan foydalaniladi?",
        "a": "Math.random()",
        "b": "Delta Time (dt) — ikki kadr oralig'idagi vaqt farqi.",
        "c": "Faqat for tsikli.",
        "d": "alert oynasi.",
        "e": "localStorage kaliti.",
        "correct": "B",
        "topic": "Delta Time Mexanikasi",
        "expl": "Delta time harakat tezligini vaqtga bog'laydi, natijada o'yin 60Hz va 144Hz monitorlarda bir xil tezlikda harakatlanadi."
    },
    {
        "text": "2D o'yinlarda AABB (Axis-Aligned Bounding Box) to'qnashuv algoritmi qanday ishlaydi?",
        "a": "O'yinchining mikrofon ovozini o'lchaydi.",
        "b": "Ikki to'rtburchakning X va Y o'qlari bo'yicha proyeksiyalari kesishganini (overlap) 4 ta shart orqali tekshiradi.",
        "c": "Faqat ranglarning bir-biriga mosligini tekshiradi.",
        "d": "Brauzer keshini tozalaydi.",
        "e": "Faqat aylana shakllarni hisoblaydi.",
        "correct": "B",
        "topic": "AABB To'qnashuv Algoritmi",
        "expl": "AABB to'qnashuvni tezkor hisoblaydi: `r1.x < r2.x + r2.w && r1.x + r1.w > r2.x && r1.y < r2.y + r2.h && r1.y + r1.h > r2.y`."
    },
    {
        "text": "O'yin mantig'ini boshqaruvchi Chekli Holatlar Mashinasi (FSM - Finite State Machine) qanday holatlardan tashkil topadi?",
        "a": "Katta, Kichik, O'rtacha.",
        "b": "MENU, PLAYING, PAUSED, GAME_OVER kabi aniq ajratilgan diskret holatlar va ularning o'tish qoidalari.",
        "c": "Faqat Wi-Fi va Bluetooth holatlari.",
        "d": "Ertalab, Kunduzi, Kechasi.",
        "e": "Faqat 'Ha' va 'Yo'q'.",
        "correct": "B",
        "topic": "Finite State Machine (FSM)",
        "expl": "FSM o'yin oqimini tartibga soladi: menyu holatida boshqaruv boshqa, o'yin ketayotganda esa o'yin fizikasi ishlaydi."
    },
    {
        "text": "Murakkab o'yin ma'lumotlarini (inventar, koordinatalar, ball) LocalStorage da saqlash uchun nima qilinadi?",
        "a": "Hech qanday o'zgartirishsiz to'g'ridan-to'g'ri obyekt uzatiladi.",
        "b": "`JSON.stringify(gameState)` yordamida obyekt matnga (string) aylantirilib saqlanadi, o'qishda esa `JSON.parse()` qilinadi.",
        "c": "Faqat birinchi raqami saqlanadi.",
        "d": "CSS fayliga yoziladi.",
        "e": "Bunday ma'lumotlarni saqlab bo'lmaydi.",
        "correct": "B",
        "topic": "JSON Serialization & State",
        "expl": "LocalStorage faqat satr (string) saqlaydi, shuning uchun JavaScript obyektlarini JSON ga aylantirish shart."
    },
    {
        "text": "Portlash, sakrash yoki qahramon harakatidagi uchqunlar qanday tizim (Particles System) orqali hosil qilinadi?",
        "a": "Faqat tayyor GIF rasmlarni yuklash orqali.",
        "b": "Har biri o'z koordinatasi, tezligi, rangi va umr ko'rish vaqtiga (life) ega bo'lgan zarralar massivi orqali.",
        "c": "Kompyuter ekranini titratish orqali.",
        "d": "Matn shriftini kattalashtirish orqali.",
        "e": "Brauzerni qayta yuklash orqali.",
        "correct": "B",
        "topic": "Partikllar Tizimi (Particles)",
        "expl": "Partikllar massivi har kadrda zarralar o'rnini yangilaydi va umri tugagan (life <= 0) zarralarni massivdan o'chirib turadi."
    },
    {
        "text": "Web Audio API da dasturiy ravishda 'Beep' (sakrash yoki g'alaba) tovushini yaratish uchun qaysi tugun (node) ishlatiladi?",
        "a": "VideoNode",
        "b": "OscillatorNode — berilgan chastotada (Hz) ovoz to'lqinlarini generatsiya qiluvchi sintezator.",
        "c": "ImageBitmap",
        "d": "PrinterNode",
        "e": "CssFilterNode",
        "correct": "B",
        "topic": "Web Audio API",
        "expl": "OscillatorNode toza tovush to'lqinlarini (sine, square, triangle) yaratadi, audio faylsiz yengil o'yin tovushlarini ta'minlaydi."
    },
    {
        "text": "Katta dunyoli o'yinda Virtual Kamera (Camera Scrolling) qanday ishlaydi?",
        "a": "Kompyuter veb-kamerasini qo'lda burish kerak bo'ladi.",
        "b": "Canvas kontekstini `ctx.translate(-camera.x, -camera.y)` orqali o'yinchi harakatiga teskari surish orqali.",
        "c": "O'yinchini joyida qotirib, fonni o'chirib tashlash orqali.",
        "d": "Brauzer oynasini kichiklashtirish orqali.",
        "e": "Monitor burchagini burish orqali.",
        "correct": "B",
        "topic": "Virtual Kamera va Scrolling",
        "expl": "`ctx.translate` butun koordinatalar sistemasini kamera ortidan siljitadi, natijada katta xarita bo'ylab harakatlanish mumkin bo'ladi."
    },
    {
        "text": "FUT Card Studio loyihasida futbolchining umumiy reytingi (OVR) qanday hisoblanadi?",
        "a": "Foydalanuvchining sevimli raqami bilan belgilanadi.",
        "b": "Pozitsiyaga bog'liq vaznli formula (PAC, SHO, PAS, DRI, DEF, PHY ko'rsatkichlarining pozitsiyaviy koeffitsientlari yig'indisi) orqali.",
        "c": "Faqat yoshi orqali.",
        "d": "Alifbo tartibi orqali.",
        "e": "Har doim 99 deb olinadi.",
        "correct": "B",
        "topic": "FUT OVR Formulasi",
        "expl": "OVR matematik formula: hujumchida SHO va PAC, himoyachida esa DEF va PHY kattaroq vaznga (koeffitsientga) ega bo'ladi."
    },
    {
        "text": "HTML5 File API orqali foydalanuvchi kompyuteridan rasmni o'yin kartasiga yuklash qaysi metod bilan bajariladi?",
        "a": "window.open()",
        "b": "FileReader.readAsDataURL(file)",
        "c": "localStorage.clear()",
        "d": "document.write()",
        "e": "console.log()",
        "correct": "B",
        "topic": "File API & FileReader",
        "expl": "`readAsDataURL` rasmni Base64 formatidagi satrga o'giradi va uni bevosita `<img>` yoki Canvasga joylash imkonini beradi."
    },
    {
        "text": "FUT Squad Builder loyihasida jamoa kimyosi (Chemistry - 33 ballik tizim) qanday algoritm bilan tekshiriladi?",
        "a": "Faqat bir xil rangdagi futbolchilarni terish orqali.",
        "b": "Graf tugunlari aloqasi: bitta klub, bitta liga va bitta millatga mansub o'yinchilar orasidagi kesishmalar sonini hisoblash orqali.",
        "c": "Faqat futbolchilarning bo'yi orqali.",
        "d": "Jamoa logotipini chizish orqali.",
        "e": "Tasodifiy son chiqarish orqali.",
        "correct": "B",
        "topic": "Graf va Kimyo Algoritmi",
        "expl": "Jamoa kimyosi relatsion munosabat bo'lib, o'yinchilar klubi, ligasi va davlati o'rtasidagi bog'liqliklarni tahlil qiladi."
    },
    {
        "text": "FUT Match Engine simulyatorida 90 daqiqalik o'yin jarayoni qanday modellashtiriladi?",
        "a": "Haqiqiy 90 daqiqa kutish orqali.",
        "b": "Tezlashtirilgan hodisalar generatori: har daqiqada jamoalar kuchi va kimyosi asosida hujum, zarba, qutqarish va gol ehtimolligini hisoblash orqali.",
        "c": "Faqat bitta gol bilan tugash sharti orqali.",
        "d": "Klaviatura strelkalari bilan.",
        "e": "Videoni oddiygina ko'rsatish orqali.",
        "correct": "B",
        "topic": "Match Engine Simulyatori",
        "expl": "Match Engine vaqt tsikli va ehtimollik taqsimoti orqali taktik duellarni virtual simulyatsiya qiladi."
    },
    {
        "text": "FUT Transfer Market bozorida EA Sports nega har bir bitimdan 5% soliq (Coin Sink) olib qoladi?",
        "a": "O'yinchilarni xafa qilish uchun.",
        "b": "O'yin iqtisodiyotida pul massasi haddan tashqari ko'payib, inflyatsiya yuz bermasligi va narxlar muvozanatini saqlash uchun.",
        "c": "Server elektr energiyasini to'lash uchun.",
        "d": "Dasturchilarga choy puli yig'ish uchun.",
        "e": "Bu soliq hech narsaga ta'sir qilmaydi.",
        "correct": "B",
        "topic": "O'yin Iqtisodiyoti (Coin Sink)",
        "expl": "Coin Sink o'yindagi ortiqcha virtual valyutani yo'qotib, transfer bozoridagi inflyatsiyani jilovlaydi."
    },
    {
        "text": "Mobil qurilmalarda o'yinni boshqarish uchun qaysi JavaScript hodisalari (Touch Events) qo'llaniladi?",
        "a": "onhover, onwheel",
        "b": "touchstart, touchmove, touchend",
        "c": "keypress, keyup",
        "d": "oncopy, onpaste",
        "e": "onresize, onscroll",
        "correct": "B",
        "topic": "Mobil Touch Hodisalari",
        "expl": "Sensorli ekranlarda teginish, siljitish va qo'lni ko'tarish `touchstart`, `touchmove`, `touchend` hodisalari bilan olinadi."
    },
    {
        "text": "Retina va yuqori zichlikdagi zamonaviy ekranlarda Canvas xira bo'lib qolmasligi uchun nima qilinadi?",
        "a": "Monitorni tozalash kerak.",
        "b": "Canvas o'lchamini `window.devicePixelRatio` koeffitsientiga ko'paytirib, CSS o'lchamini asl holida qoldirish (`ctx.scale`).",
        "c": "Faqat qora va oq ranglarni ishlatish.",
        "d": "Brauzer masshtabini 50% ga tushirish.",
        "e": "Canvasni sahifadan olib tashlash.",
        "correct": "B",
        "topic": "DevicePixelRatio & Crisp Canvas",
        "expl": "Fizik piksellar mantiqiy CSS piksellaridan 2-3 barobar ko'p bo'lgani sababli, `devicePixelRatio` ga masshtablash o'tkir grafikani beradi."
    },
    {
        "text": "Target Jarvis loyihasida o'quvchining ovozli buyruqlarini matnga aylantirish uchun qaysi Web API ishlatiladi?",
        "a": "Web Bluetooth API",
        "b": "Web Speech API (`webkitSpeechRecognition`)",
        "c": "Geolocation API",
        "d": "Battery Status API",
        "e": "Fullscreen API",
        "correct": "B",
        "topic": "Web Speech API (Ovozni Tanish)",
        "expl": "`SpeechRecognition` mikrofondan kiruvchi nutqni real vaqtda tahlil qilib, dasturga matn (text) sifatida uzatadi."
    },
    {
        "text": "AI ovozli yordamchisi (Jarvis) ning o'quvchiga ovoz chiqarib javob qaytarishi qanday amalga oshiriladi?",
        "a": "Faqat ekranda harflarni miltillatish orqali.",
        "b": "`window.speechSynthesis.speak(new SpeechSynthesisUtterance('Xush kelibsiz!'))` orqali nutq sintezlash.",
        "c": "Telefon raqamiga qo'ng'iroq qilish orqali.",
        "d": "Ovoz yozilgan MP3 faylni qidirib topish orqali.",
        "e": "Dasturchining o'zi mikrofon orqali gapirishi orqali.",
        "correct": "B",
        "topic": "Nutq Sintezi (Speech Synthesis)",
        "expl": "SpeechSynthesis API brauzerning ichki nutq generatoridan foydalanib, istalgan matnni ovoz chiqarib o'qib beradi."
    },
    {
        "text": "Brauzerda veb-kamera oqimini (video stream) qabul qilib olish qaysi standart metod orqali amalga oshiriladi?",
        "a": "window.openCamera()",
        "b": "navigator.mediaDevices.getUserMedia({ video: true })",
        "c": "document.getCameraStream()",
        "d": "canvas.captureScreen()",
        "e": "console.camera()",
        "correct": "B",
        "topic": "MediaDevices & Kamera Oqimi",
        "expl": "`getUserMedia` xavfsiz kontekstda foydalanuvchi ruxsati bilan kamera oqimini `<video>` yoki Canvasga uzatadi."
    },
    {
        "text": "Kiber-Ko'z (Motion Detector) loyihasida ekrandagi harakat qanday matematik usulda aniqlanadi?",
        "a": "Kompyuter haroratini o'lchash orqali.",
        "b": "Joriy video kadrining piksel ma'lumotlari (`getImageData`) bilan avvalgi kadr piksellari orasidagi mutlaq farqni (`Math.abs(p1 - p2)`) hisoblash orqali.",
        "c": "Faqat xona yorug'ligini kamaytirish orqali.",
        "d": "Kamerani silkitish orqali.",
        "e": "Internet tezligini o'lchash orqali.",
        "correct": "B",
        "topic": "Kadrlar Farqi va Harakat Detektori",
        "expl": "Frame Differencing algoritmi ketma-ket ikki kadrning RGB qiymatlarini solishtirib, o'zgargan piksellar klasterini harakat sifatida belgilaydi."
    },
    {
        "text": "Dasturlashda DRY (Don't Repeat Yourself) qoidasi nima uchun muhim?",
        "a": "Kompyuter klaviaturasini tejash uchun.",
        "b": "Bir xil kod bloklarini qayta-qayta yozmasdan, ularni alohida funksiya va modullarga ajratish orqali kodni toza va o'zgartirishni oson qilish.",
        "c": "Har kuni yangi dasturlash tilini o'rganish uchun.",
        "d": "Faqat o'yinlarni tezroq yutish uchun.",
        "e": "Faqat 100 qator kod yozish bilan cheklanish uchun.",
        "correct": "B",
        "topic": "DRY Prinsipi va Refaktoring",
        "expl": "DRY printsipi takrorlanishlarni yo'qotadi: mantiq faqat bir joyda saqlanadi, xatolik yuz berganda bitta joyni tuzatish kifoya."
    },
    {
        "text": "Vibecoding jarayonida AI yozgan kodda mantiqiy xato (masalan, to'p devordan qaytmasdan o'tib ketishi) bo'lsa, qanday prompt beriladi?",
        "a": "'Sen yomon dasturchisan!'",
        "b": "'Mening to'pim x: 0 va x: canvas.width chegaralarini hisobga olmayapti, u devordan o'tib ketyapti. Mana mening kodim [...]. Qaytish chegarasi va `vx = -vx` mantiqini tuzatib ber.'",
        "c": "'Hammasini o'chirib boshqatdan yoz.'",
        "d": "'Menga yangi kompyuter kerak.'",
        "e": "'Faqat HTML ni ko'rsat.'",
        "correct": "B",
        "topic": "AI Refaktoring va Tuzatish",
        "expl": "Xatoning aniq alomatlarini va o'zgaruvchi nomlarini ko'rsatuvchi kontekstli prompt AI dan mukammal yechim olishni ta'minlaydi."
    },
    {
        "text": "Protsedural dunyo generatsiyasida (cheksiz yuguruvchi o'yinida) to'siqlar qanday yaratiladi?",
        "a": "Dasturchi har bir to'siqni qo'lda 1000 marta chizib chiqadi.",
        "b": "Algoritmik qoidalar va `Math.random()` orqali ma'lum masofa oralig'ida dinamik yangi to'siq obyektlari yaratilib, ekrandan chiqib ketganlari o'chiriladi.",
        "c": "O'yin faqat bitta to'siq bilan cheklanadi.",
        "d": "Internetdan har safar yangi rasm yuklab olinadi.",
        "e": "Faqat matnli xabarlar chiqariladi.",
        "correct": "B",
        "topic": "Protsedural Generatsiya",
        "expl": "Protsedural generatsiya cheksiz xilma-xillikni ta'minlaydi: o'yin xotirani to'ldirmasdan har safar yangi tajriba beradi."
    },
    {
        "text": "O'yin loyihasini Git va GitHub ga yuklashda qaysi ketma-ketlik to'g'ri hisoblanadi?",
        "a": "git delete -> git exit",
        "b": "git init -> git add . -> git commit -m 'feat: fut engine' -> git push",
        "c": "Faylni shunchaki fleshkaga ko'chirish",
        "d": "git clear -> git restart",
        "e": "Faqat terminalni yopish",
        "correct": "B",
        "topic": "Git Ish Jarayoni",
        "expl": "Standart Git tsikli: repozitoriyni initsializatsiya qilish, o'zgarishlarni kiritish, commit yaratish va GitHub ga yuklash."
    },
    {
        "text": "Demo Day taqdimotida o'z o'yin loyihasini hakamlar va ota-onalarga ko'rsatishning eng ta'sirli usuli qaysi?",
        "a": "Faqat kodni konsolda ko'rsatish.",
        "b": "Jonli ishlayotgan loyihani ekranda ko'rsatish, o'yin mexanikasi va OVR algoritmini tushuntirish hamda QR kod orqali ularning o'z telefonlarida o'ynatib ko'rish.",
        "c": "Faqat kitobdan o'qib berish.",
        "d": "Hech narsa gapirmasdan jim turish.",
        "e": "Faqat xatolarni aytib shikoyat qilish.",
        "correct": "B",
        "topic": "Demo Day va Loyiha Taqdimoti",
        "expl": "Jonli interaktiv namoyish va auditoriyani o'yinga jalb qilish Demo Day taqdimotining eng oliy standartidir."
    }
]

QUESTIONS_7_8_RU = [
    {
        "text": "Как меняется фундаментальная роль разработчика при переходе на методологию Vibecoding?",
        "a": "Разработчик превращается в обычного наборщика текста.",
        "b": "Разработчик выступает в роли архитектора и постановщика задач: формулирует требования для AI, тестирует, проверяет логику и управляет интеграцией систем.",
        "c": "Разработчик полностью отказывается от использования компьютера.",
        "d": "Только покупает готовые шаблоны в интернет-магазинах.",
        "e": "Занимается исключительно ручным переводом английских слов.",
        "correct": "B",
        "topic": "Философия Vibecoding",
        "expl": "В Vibecoding человек принимает ключевые инженерные решения, а искусственный интеллект многократно ускоряет генерацию кода."
    },
    {
        "text": "Какой синтаксис является современным стандартом для поиска элемента DOM и привязки события клика в JavaScript?",
        "a": "document.write() и alert()",
        "b": "document.querySelector('#startBtn').addEventListener('click', handler);",
        "c": "window.navigate()",
        "d": "canvas.style()",
        "e": "css.bind('click')",
        "correct": "B",
        "topic": "События DOM (Events)",
        "expl": "`querySelector` и `addEventListener` представляют собой чистый, производительный и безопасный стандарт работы с DOM."
    },
    {
        "text": "Что используется в игровом цикле (Game Loop) для независимости скорости анимации от частоты обновления экрана (FPS)?",
        "a": "Math.random()",
        "b": "Delta Time (dt) — разница во времени между отрисовкой двух последовательных кадров.",
        "c": "Обычный бесконечный цикл for.",
        "d": "Модальное окно alert().",
        "e": "Ключ в localStorage.",
        "correct": "B",
        "topic": "Механика Delta Time",
        "expl": "Delta Time связывает скорость перемещения с физическим временем, обеспечивая одинаковый геймплей на мониторах 60Hz и 144Hz."
    },
    {
        "text": "Как работает алгоритм проверки столкновений AABB (Axis-Aligned Bounding Box) в двумерных играх?",
        "a": "Измеряет громкость звука микрофона игрока.",
        "b": "Проверяет факт взаимного пересечения (overlap) проекций двух прямоугольников по осям X и Y через 4 базовых неравенства.",
        "c": "Сравнивает совпадение фоновых цветов объектов.",
        "d": "Очищает кэш браузера пользователя.",
        "e": "Работает исключительно с идеально круглыми телами.",
        "correct": "B",
        "topic": "Алгоритм Коллизий AABB",
        "expl": "AABB вычисляет пересечение габаритов прямоугольников: `r1.x < r2.x + r2.w && r1.x + r1.w > r2.x && r1.y < r2.y + r2.h && r1.y + r1.h > r2.y`."
    },
    {
        "text": "Из каких типовых состояний состоит конечный автомат (Finite State Machine / FSM) в архитектуре игры?",
        "a": "Большой, Средний, Маленький.",
        "b": "Четко разграниченные дискретные состояния MENU, PLAYING, PAUSED, GAME_OVER и правила перехода между ними.",
        "c": "Только состояния подключения Wi-Fi и Bluetooth.",
        "d": "Утро, День, Ночь.",
        "e": "Исключительно логические 'Да' и 'Нет'.",
        "correct": "B",
        "topic": "Конечные Автоматы (FSM)",
        "expl": "FSM структурирует логику: в меню обрабатывается клик по кнопкам, а в состоянии игры работает физический движок."
    },
    {
        "text": "Как правильно сохранить сложное состояние игры (инвентарь, здоровье, координаты) в LocalStorage?",
        "a": "Передать сырой объект напрямую без изменений.",
        "b": "Преобразовать объект в строку через `JSON.stringify(gameState)`, а при чтении восстановить объект через `JSON.parse()`.",
        "c": "Сохранить только первую цифру значения.",
        "d": "Записать данные внутрь файла стилей CSS.",
        "e": "Сохранение сложных объектов в браузере невозможно.",
        "correct": "B",
        "topic": "Сериализация JSON и State",
        "expl": "Хранилище LocalStorage принимает только строки, поэтому сериализация объектов в JSON является обязательной."
    },
    {
        "text": "С помощью какой архитектуры создаются эффекты взрывов, искр и дыма (Particles System)?",
        "a": "Загрузкой тяжелых анимированных GIF-изображений.",
        "b": "Массивом автономных частиц, где каждая частица имеет координаты, скорость, цвет и время жизни (life), уменьшающееся каждый кадр.",
        "c": "Физической тряской монитора пользователя.",
        "d": "Увеличением размера шрифтов текста.",
        "e": "Автоматической перезагрузкой вкладки браузера.",
        "correct": "B",
        "topic": "Системы Частиц (Particles)",
        "expl": "Система частиц обновляет массив координат каждый кадр и удаляет угасшие частицы (`life <= 0`), создавая сочные визуальные эффекты."
    },
    {
        "text": "Какой узел (Node) в Web Audio API используется для программного синтеза звуков (прыжок, победа) без аудиофайлов?",
        "a": "VideoNode",
        "b": "OscillatorNode — генератор звуковых волн заданной частоты (в Герцах, Гц).",
        "c": "ImageBitmapNode",
        "d": "PrinterNode",
        "e": "CssFilterNode",
        "correct": "B",
        "topic": "Синтез в Web Audio API",
        "expl": "OscillatorNode синтезирует звуковые колебания (синусоидальные, квадратные, пилообразные), создавая легкие процедурные звуки."
    },
    {
        "text": "Как реализуется механизм виртуальной камеры (Camera Scrolling) в играх с большим миром?",
        "a": "Поворотом объектива физической веб-камеры руками.",
        "b": "Сдвигом системы координат холста с помощью `ctx.translate(-camera.x, -camera.y)` вслед за перемещением персонажа.",
        "c": "Полной заморозкой персонажа и удалением заднего фона.",
        "d": "Принудительным уменьшением окна браузера.",
        "e": "Поворотом монитора на 90 градусов.",
        "correct": "B",
        "topic": "Виртуальная Камера и Скроллинг",
        "expl": "Метод `ctx.translate` смещает мировую матрицу координат, позволяя персонажу свободно путешествовать по гигантской карте."
    },
    {
        "text": "По какому принципу рассчитывается общий рейтинг игрока (OVR) в проекте FUT Card Studio?",
        "a": "Случайным выбором любимого числа пользователя.",
        "b": "По взвешенной формуле позиции (сумма статов PAC, SHO, PAS, DRI, DEF, PHY с учетом позиционных коэффициентов).",
        "c": "Исключительно на основе возраста футболиста.",
        "d": "В алфавитном порядке фамилий.",
        "e": "Рейтинг всегда фиксирован и равен 99.",
        "correct": "B",
        "topic": "Формула Рейтинга FUT OVR",
        "expl": "Рейтинг OVR базируется на математической модели: у нападающих больший вес имеют SHO и PAC, а у защитников — DEF и PHY."
    },
    {
        "text": "Какой метод HTML5 File API считывает файл изображения с диска для отображения на карточке футболиста?",
        "a": "window.open()",
        "b": "FileReader.readAsDataURL(file)",
        "c": "localStorage.clear()",
        "d": "document.write()",
        "e": "console.log()",
        "correct": "B",
        "topic": "HTML5 File API и FileReader",
        "expl": "Метод `readAsDataURL` преобразует локальный файл в строку формата Base64, готовую для вставки в `<img>` или Canvas."
    },
    {
        "text": "Какой алгоритм проверяет сыгранность состава (Chemistry — шкала до 33 баллов) в FUT Squad Builder?",
        "a": "Простой подбор карточек одинакового цвета.",
        "b": "Анализ связей графа: подсчет пересечений по клубу, лиге и национальности между 11 игроками на поле.",
        "c": "Сравнение роста футболистов в сантиметрах.",
        "d": "Отрисовка векторного логотипа команды.",
        "e": "Генерация случайного числа от 1 до 33.",
        "correct": "B",
        "topic": "Графы и Алгоритм Сыгранности",
        "expl": "Сыгранность — это реляционный анализ графа: общие ребра клуба, лиги и страны начисляют баллы синергии в схеме расстановки."
    },
    {
        "text": "Как устроен движок симуляции матча (FUT Match Engine) для расчета 90 минут игры?",
        "a": "Ожиданием реальных 90 минут перед экраном.",
        "b": "Генератором событий на основе вероятностей: поминутный расчет атак, дриблинга, сейвов и голов с учетом статов команд.",
        "c": "Матч всегда завершается со счетом 1:0 без вариантов.",
        "d": "Управлением через стрелочки клавиатуры.",
        "e": "Простым запуском готового видеофайла.",
        "correct": "B",
        "topic": "Симулятор Match Engine",
        "expl": "Match Engine моделирует мини-дуэли игроков через дискретные временные тики и генератор случайных величин на основе OVR."
    },
    {
        "text": "Зачем в трансферном рынке FUT взимается 5% налог с каждой сделки (механизм Coin Sink)?",
        "a": "Чтобы расстроить активных игроков.",
        "b": "Для вывода избыточной игровой валюты из экономики, предотвращения инфляции и стабилизации цен на карточки.",
        "c": "Для оплаты электричества игровых серверов.",
        "d": "Для сбора чаевых разработчикам игры.",
        "e": "Этот налог не оказывает никакого влияния.",
        "correct": "B",
        "topic": "Игровая Экономика (Coin Sink)",
        "expl": "Coin Sink сдерживает гиперинфляцию: без уничтожения части валюты при сделках цены на топ-карты росли бы бесконечно."
    },
    {
        "text": "Какие события JavaScript (Touch Events) используются для управления игрой на мобильных экранах?",
        "a": "onhover, onwheel",
        "b": "touchstart, touchmove, touchend",
        "c": "keypress, keyup",
        "d": "oncopy, onpaste",
        "e": "onresize, onscroll",
        "correct": "B",
        "topic": "События Сенсорных Экранов (Touch)",
        "expl": "События касания (`touchstart`), движения (`touchmove`) и отрыва пальца (`touchend`) формируют виртуальный экранный джойстик."
    },
    {
        "text": "Что необходимо сделать, чтобы графика Canvas оставалась идеально четкой на дисплеях высокой плотности (Retina)?",
        "a": "Тщательно протереть экран монитора салфеткой.",
        "b": "Умножить физический размер холста на `window.devicePixelRatio`, сохранив стиль CSS прежним (`ctx.scale`).",
        "c": "Использовать исключительно черно-белые цвета.",
        "d": "Уменьшить масштаб браузера до 50%.",
        "e": "Удалить холст Canvas со страницы.",
        "correct": "B",
        "topic": "DevicePixelRatio и Четкий Canvas",
        "expl": "Физическое масштабирование под `devicePixelRatio` предотвращает пикселизацию и размытие линий на четких экранах смартфонов."
    },
    {
        "text": "Какой стандартный Web API используется в проекте Target Jarvis для перевода голосовых команд в текст?",
        "a": "Web Bluetooth API",
        "b": "Web Speech API (`webkitSpeechRecognition`)",
        "c": "Geolocation API",
        "d": "Battery Status API",
        "e": "Fullscreen API",
        "correct": "B",
        "topic": "Web Speech API (Распознавание)",
        "expl": "Интерфейс `SpeechRecognition` распознает аудиопоток с микрофона и в реальном времени генерирует строковый текст."
    },
    {
        "text": "Как голосовой ассистент Jarvis озвучивает ответ пользователю через динамики устройства?",
        "a": "Только миганием цветных рамок на экране.",
        "b": "Синтезом речи через `window.speechSynthesis.speak(new SpeechSynthesisUtterance('Добро пожаловать!'))`.",
        "c": "Звонком на сотовый телефон пользователя.",
        "d": "Поиском готового MP3 файла в интернете.",
        "e": "Голосом разработчика через скрытый микрофон.",
        "correct": "B",
        "topic": "Синтез Речи (SpeechSynthesis)",
        "expl": "Встроенный синтезатор `speechSynthesis` генерирует естественную человеческую речь из переданного текста на нужном языке."
    },
    {
        "text": "Какой метод веб-платформы запрашивает доступ к видеопотоку веб-камеры устройства?",
        "a": "window.openCamera()",
        "b": "navigator.mediaDevices.getUserMedia({ video: true })",
        "c": "document.getCameraStream()",
        "d": "canvas.captureScreen()",
        "e": "console.camera()",
        "correct": "B",
        "topic": "Доступ к Камере (getUserMedia)",
        "expl": "`getUserMedia` открывает диалог разрешений безопасности и подключает живой видеопоток камеры к `<video>` или Canvas."
    },
    {
        "text": "Как математически работает датчик движения (Motion Detector) в проекте Кибер-Глаз?",
        "a": "Измерением температуры процессора.",
        "b": "Вычислением модуля разницы цветовых значений пикселей (`Math.abs(p1 - p2)`) между текущим и предыдущим видеокадрами.",
        "c": "Принудительным выключением света в комнате.",
        "d": "Физическим встряхиванием веб-камеры.",
        "e": "Замером скорости интернет-трафика.",
        "correct": "B",
        "topic": "Разница Кадров (Frame Differencing)",
        "expl": "Алгоритм Frame Difference анализирует массив `getImageData` и фиксирует движение при значительном изменении цветов пикселей."
    },
    {
        "text": "Почему принцип DRY (Don't Repeat Yourself) является фундаментальным в архитектуре кода?",
        "a": "Чтобы сберечь ресурс кнопок клавиатуры.",
        "b": "Чтобы исключить дублирование логики, вынося повторяющиеся операции в функции и модули для удобства поддержки и поиска багов.",
        "c": "Чтобы учить новый язык программирования каждый день.",
        "d": "Исключительно для победы в играх.",
        "e": "Чтобы код никогда не превышал ровно 100 строк.",
        "correct": "B",
        "topic": "Принцип DRY и Рефакторинг",
        "expl": "Принцип DRY снижает вероятность ошибок: изменение алгоритма в одном месте автоматически обновляет всю программу."
    },
    {
        "text": "Какой промпт эффективнее всего решит логический баг в коде игры (например, мяч пролетает сквозь стены)?",
        "a": "'Ты плохой искусственный интеллект!'",
        "b": "'Мой мяч не реагирует на границы x: 0 и x: canvas.width. Вот код [...]. Исправь условие отскока и инвертируй скорость `vx = -vx`.'",
        "c": "'Удали все и начни заново.'",
        "d": "'Мне нужен новый мощный компьютер.'",
        "e": "'Покажи мне только код HTML.'",
        "correct": "B",
        "topic": "AI-Рефакторинг и Отладка",
        "expl": "Промпт с точным указанием условий, переменных и ожидаемого поведения позволяет AI мгновенно локализовать и устранить баг."
    },
    {
        "text": "Как алгоритмически генерируются препятствия в процедурном бесконечном раннере?",
        "a": "Разработчик вручную рисует 10 000 препятствий заранее.",
        "b": "Динамическим созданием объектов через интервалы времени и `Math.random()` с удалением объектов, вышедших за границы экрана.",
        "c": "В игре может существовать строго одно препятствие.",
        "d": "Скачиванием новой картинки из интернета каждую секунду.",
        "e": "Отображением только текстовых сообщений в консоли.",
        "correct": "B",
        "topic": "Процедурная Генерация",
        "expl": "Процедурная генерация создает бесконечный уникальный игровой мир на лету, не перегружая память компьютера."
    },
    {
        "text": "Какова стандартная последовательность команд для сохранения и отправки проекта в репозиторий GitHub?",
        "a": "git delete -> git exit",
        "b": "git init -> git add . -> git commit -m 'feat: fut engine' -> git push",
        "c": "Простое копирование папки на флешку.",
        "d": "git clear -> git restart",
        "e": "Просто закрыть окно терминала.",
        "correct": "B",
        "topic": "Рабочий Процесс Git",
        "expl": "Классический цикл контроля версий: инициализация, индексация изменений, создание коммита и отправка в удаленный репозиторий."
    },
    {
        "text": "Какой формат презентации своего проекта на Demo Day производит максимальное впечатление на жюри?",
        "a": "Показ черно-белого текста программы в блокноте.",
        "b": "Живая интерактивная демонстрация работающей игры, объяснение архитектуры OVR и тестирование гостями на смартфонах через QR-код.",
        "c": "Чтение доклада по распечатанному учебнику.",
        "d": "Молчание перед проектором без демонстрации.",
        "e": "Жалобы на то, что программа не успела заработать.",
        "correct": "B",
        "topic": "Demo Day и Презентация Проекта",
        "expl": "Живой рабочий прототип, который зрители могут запустить прямо со своих телефонов по QR-коду — эталон успешного Demo Day."
    }
]

print("Grade 7-8 Vibecoding test data loaded (25 questions UZ & RU). Teacher: Ismoiljon Usmonov.")
