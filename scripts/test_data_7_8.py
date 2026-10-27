#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Target International School — 7–8-Sinf Vibecoding Test Ma'lumotlari
Fan: Vibecoding (Game Dev, Interaktiv Veb va Biometrik Muhandislik)
O'qituvchi: Ismoiljon Usmonov · Yunusobod filiali

Veb-saytdagi (index.html va classes/7-8-sinf/) barcha 27 ta dars materiallaridan tuzilgan:
1-hafta: AI nima, AI Duel, SVG grafikasi, Semantik HTML va Veb Kvest
2-hafta: CSS Flexbox/Grid, JavaScript hodisalar, Kiber-reaksiya (performance.now), DevTools debugging, LocalStorage, Vercel deploy
3-hafta: Canvas 2D, requestAnimationFrame (60 FPS), Massivlar va saralash, Gravitatsiya va AABB to'qnashuv, Boss holat mashinasi
4-hafta: Web Audio API tovush sintezi, Kamera skrollingi (ctx.translate), Sensorli ekranlar (Touch hodisalar)
5-hafta: FUT Card Studio (File API & OVR), FUT Squad Builder (Kimyo graflari), FUT Match Engine (FSM duel), FUT Transfer bozori (5% Coin Sink), Target Jarvis (Web Speech API)
6-hafta: Kiber-Ko'z: Veb-kamera piksellar farqi harakat detektori
7-hafta: Biometrik Kiber-Skaner: Face ID 68 Landmark, IPD, EAR ko'z qisishi va 2D Photo Spoofing himoyasi
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
        {"grade": "A'lo (5)", "range": "22 – 25 ball", "desc": "Canvas, Game Loop, AABB fizika, FUT kimyo graflari va Biometrik Web API chuqur bilim"},
        {"grade": "Yaxshi (4)", "range": "18 – 21 ball", "desc": "Frontend, DOM hodisalari va o'yin mexanikasi yaxshi o'zlashtirilgan"},
        {"grade": "Qoniqarli (3)", "range": "13 – 17 ball", "desc": "LocalStorage, FSM va Web Speech tushunchalarini takrorlash lozim"},
        {"grade": "Qoniqarsiz (2)", "range": "0 – 12 ball", "desc": "Vibecoding va JavaScript dasturlash asoslari qayta o'rganilishi zarur"}
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
        {"grade": "Отлично (5)", "range": "22 – 25 баллов", "desc": "Глубокие знания Canvas, Game Loop, физики AABB, графов FUT и биометрии"},
        {"grade": "Хорошо (4)", "range": "18 – 21 балл", "desc": "Фронтенд, события DOM и игровая механика хорошо освоены"},
        {"grade": "Удовл. (3)", "range": "13 – 17 баллов", "desc": "Требуется повторение LocalStorage, конечных автоматов и Web Speech"},
        {"grade": "Неудовл. (2)", "range": "0 – 12 баллов", "desc": "Необходимо заново изучить основы Vibecoding и программирования JS"}
    ]
}

QUESTIONS_7_8_UZ = [
    {
        "text": "1-dars materialiga ko'ra, Katta Til Modellari (LLM) dasturlashda kod yozish jarayonini qanday amalga oshiradi?",
        "a": "Ular inson miyasi kabi o'ylaydi va kompyuterdan mustaqil qarorlar qabul qiladi.",
        "b": "Foydalanuvchi bergan matn (prompt) dagi kontekstni tahlil qilib, navbatdagi eng mantiqiy kod tokenlarini ehtimollik asosida bashorat qiladi.",
        "c": "Faqatgina GitHub omboridan tayyor fayllarni o'zgartirmasdan to'g'ridan-to'g'ri ko'chiradi.",
        "d": "Kompyuterdagi barcha dasturlarni o'chirib, o'rniga yangi operatsion tizim o'rnatadi.",
        "e": "Faqat HTML teglarini taniy oladi, lekin JavaScript kodlarini yoza olmaydi.",
        "correct": "B",
        "topic": "01-dars: LLM va Sun'iy Intellekt Asoslari",
        "expl": "LLM modellari kontekst oynasi (Context Window) dagi so'zlar va ko'rsatmalarni tahlil qilib, ehtimollar taqsimoti asosida kod generatsiya qiladi."
    },
    {
        "text": "2-darsdagi 'AI Duel' darsida eng sifatli va aniq ishlovchi dastur kodini olish uchun prompt qanday tuzilishi o'rgatilgan?",
        "a": "Faqat bir jumlali noaniq buyruq berilishi kerak.",
        "b": "Rol (Role), Vazifa (Task), Texnik talablar (Constraints) va Kutilayotgan natija (Output format) aniq ko'rsatilishi lozim.",
        "c": "Prompt ichida faqat kulgili stikerlar yuborilishi shart.",
        "d": "Prompt faqat lotin alifbosisiz yozilishi kerak.",
        "e": "AI ga hech qanday cheklov qo'ymasdan xohlagancha kod yozishga ruxsat berish kerak.",
        "correct": "B",
        "topic": "02-dars: AI Duel va Cheklovli Prompt Muhandisligi",
        "expl": "Sifatli muhandislik natijasiga erishish uchun promptda rol, stek (HTML/CSS/JS), funksional talablar va cheklovlar qat'iy beriladi."
    },
    {
        "text": "3-darsda o'rganilgan SVG (Scalable Vector Graphics) formatining raster (PNG/JPG) rasmlardan eng katta afzalligi nimada?",
        "a": "SVG faqat qora-oq rangda bo'ladi.",
        "b": "SVG matematik formulalar (chiziqlar, nuqtalar) bilan chizilgani sababli, istalgancha kattalashtirilganda ham sifati mutlaqo buzilmaydi.",
        "c": "SVG fayllar kompyuterda juda katta (kamida 1 GB) joy egallaydi.",
        "d": "SVG rasmlarni brauzerda ochib bo'lmaydi.",
        "e": "SVG faqat video formatlar uchun mo'ljallangan.",
        "correct": "B",
        "topic": "03-dars: SVG Vektor Grafikasi va UI Aktivlari",
        "expl": "SVG piksellarga emas, matematik koordinatalarga asoslanganligi sababli istalgan ekran o'lchamida tiniq va ixcham bo'lib qoladi."
    },
    {
        "text": "5-darsda 'Semantik HTML' teglari (<header>, <nav>, <main>, <section>, <footer>) nima uchun <div> ga nisbatan ustun qo'yiladi?",
        "a": "Chunki ular sahifa hajmini 10 barobarga kamaytiradi.",
        "b": "Sahifa tuzilmasini brauzer, qidiruv tizimlari (SEO) va yordamchi texnologiyalar (screen-readers) uchun ma'noli va tushunarli qiladi.",
        "c": "Faqatgina sahifani rangli qilib bezatish uchun.",
        "d": "Bu teglar qo'yilsa, JavaScript yozish umuman talab qilinmaydi.",
        "e": "Ular faqat mobil telefonlarda ishlaydi.",
        "correct": "B",
        "topic": "05-dars: Semantik HTML va Veb Arxitekturasi",
        "expl": "Semantik teglar sahifaning qaysi qismi navigatsiya (<nav>), qaysi biri asosiy kontent (<main>) ekanini dasturiy darajada ifodalaydi."
    },
    {
        "text": "7-darsdagi CSS Flexbox tizimida elementlarni asosiy o'q bo'ylab markazlashtirish uchun qaysi xususiyat ishlatiladi?",
        "a": "align-items: center;",
        "b": "justify-content: center;",
        "c": "float: center;",
        "d": "display: block;",
        "e": "flex-direction: none;",
        "correct": "B",
        "topic": "07-dars: CSS Flexbox va Joylashuv Boshqaruvi",
        "expl": "Flexbox konteynerida 'justify-content' asosiy o'q (main-axis) bo'yicha, 'align-items' esa ko'ndalang o'q (cross-axis) bo'yicha tekislaydi."
    },
    {
        "text": "8-darsda tugma bosilishini JavaScript orqali kuzatib borish uchun qaysi usul qo'llaniladi?",
        "a": "button.setTimer()",
        "b": "button.addEventListener('click', () => { ... });",
        "c": "window.destroy()",
        "d": "console.break()",
        "e": "document.write('click')",
        "correct": "B",
        "topic": "08-dars: JavaScript Hodisalari (Events)",
        "expl": "addEventListener metodi DOM elementiga hodisa eshituvchisini (event listener) bog'laydi va hodisa sodir bo'lganda funksiyani chaqiradi."
    },
    {
        "text": "9-darsdagi 'Kiber-Reaksiya' o'yinida foydalanuvchining reaktsiya tezligini millisekundlarda o'ta aniq hisoblash uchun nima ishlatilgan?",
        "a": "Oddiy devor soati surati.",
        "b": "performance.now() yuqori aniqlikdagi vaqt funksiyasi.",
        "c": "Math.random() tasodifiy soni.",
        "d": "alert() ogohlantirish oynasi.",
        "e": "CSS animation-duration xossasi.",
        "correct": "B",
        "topic": "09-dars: Kiber-Reaksiya va performance.now()",
        "expl": "performance.now() mikrosekundlargacha aniqlikdagi suzuvchi nuqtali vaqt belgisini (DOMHighResTimeStamp) qaytaradi."
    },
    {
        "text": "10-darsdagi 'AI Debugging' jarayonida brauzer konsolida 'Uncaught TypeError: Cannot read properties of null' xatosi nimani bildiradi?",
        "a": "Kompyuter qattiq diskida joy tugaganini.",
        "b": "Kodingiz mavjud bo'lmagan (DOM da topilmagan yoki qiymati null bo'lgan) elementning xususiyatiga murojaat qilmoqchi bo'lganini.",
        "c": "Internet tezligi juda sekinlashib ketganini.",
        "d": "Foydalanuvchi brauzer oynasini yopib qo'yganini.",
        "e": "Barcha o'zgaruvchilar to'g'ri ishlaganini.",
        "correct": "B",
        "topic": "10-dars: AI Debugging va DevTools Xatolari",
        "expl": "document.querySelector mavjud bo'lmagan selektordan null qaytarganda va uning .addEventListener yoki .style siga murojaat qilinganda TypeError chiqadi."
    },
    {
        "text": "11-darsda o'rganilgan 'LocalStorage' ga JavaScript obyektini (masalan: {score: 95, user: 'Aziz'}) saqlash uchun qanday yoziladi?",
        "a": "localStorage.setItem('record', {score: 95});",
        "b": "localStorage.setItem('record', JSON.stringify({score: 95, user: 'Aziz'}));",
        "c": "localStorage.writeAll({score: 95});",
        "d": "window.storage = {score: 95};",
        "e": "localStorage.clear('record');",
        "correct": "B",
        "topic": "11-dars: LocalStorage va JSON Serializatsiyasi",
        "expl": "LocalStorage faqat matn (string) saqlaydi, shuning uchun obyektlar JSON.stringify() orqali qatorga aylantirilib saqlanadi."
    },
    {
        "text": "12-darsda yaratilgan o'yinni butun dunyo ko'rishi uchun Vercel xizmatiga deploy qilganda qaysi xavfsizlik protokoli avtomatik beriladi?",
        "a": "HTTP 1.0 oddiy shifrlanmagan ulanish.",
        "b": "HTTPS va bepul SSL/TLS shifrlash sertifikati.",
        "c": "Faqat mahalliy localhost ulanishi.",
        "d": "Bluetooth simsiz protokoli.",
        "e": "FTP fayl uzatish protokoli.",
        "correct": "B",
        "topic": "12-dars: Veb Deploy va HTTPS/SSL",
        "expl": "Vercel kabi zamonaviy hostinglar avtomatik ravishda global CDN, bepul SSL sertifikati va xavfsiz HTTPS protokoli bilan ta'minlaydi."
    },
    {
        "text": "13-darsda HTML5 <canvas> elementida 60 FPS silliq o'yin animatsiyasini yaratish uchun qaysi funksiya chaqiriladi?",
        "a": "setInterval(update, 1000);",
        "b": "requestAnimationFrame(gameLoop);",
        "c": "setTimeout(gameLoop, 0);",
        "d": "window.reload();",
        "e": "document.refresh();",
        "correct": "B",
        "topic": "13-dars: Canvas 2D va requestAnimationFrame",
        "expl": "requestAnimationFrame brauzerning ekranni yangilash chastotasi bilan sinxronlashib (odatda 60 Gts), tejamkor va uzluksiz kadr chizishni ta'minlaydi."
    },
    {
        "text": "14-darsda dushmanlar massividan ekrandan chiqib ketgan yoki yo'q qilingan dushmanlarni tozalash uchun qaysi massiv metodi ishlatiladi?",
        "a": "enemies.push()",
        "b": "enemies = enemies.filter(enemy => enemy.isAlive);",
        "c": "enemies.join()",
        "d": "enemies.toString()",
        "e": "enemies.reverse()",
        "correct": "B",
        "topic": "14-dars: Massivlar va Ob'yektlarni Filtrlash",
        "expl": "Array.filter() shartga javob beradigan elementlarni saqlab, o'lgan yoki ekrandan chiqqan obyektlarni massivdan o'chiradi."
    },
    {
        "text": "15-darsda qahramonning platformer o'yinida yuqoriga sakrashi va yerga tushishida gravitatsiya qanday hisoblanadi?",
        "a": "player.x += speed;",
        "b": "player.vy += gravity; player.y += player.vy;",
        "c": "player.y = player.y * 2;",
        "d": "player.vy = 0;",
        "e": "player.jump = true;",
        "correct": "B",
        "topic": "15-dars: O'yin Fizikasi: Gravitatsiya va Sakrash",
        "expl": "Har bir kadrda vertikal tezlikka gravitatsiya qo'shiladi (vy += gravity), so'ngra qahramonning koordinatasi o'zgaradi (y += vy)."
    },
    {
        "text": "15-darsning ikkinchi qismidagi AABB (Axis-Aligned Bounding Box) to'qnashuv algoritmida ikkita to'g'ri to'rtburchak qachon to'qnashadi?",
        "a": "Ularning ranglari bir xil bo'lganda.",
        "b": "Ikkala to'rtburchak X va Y o'qlari bo'yicha bir vaqtda bir-birining ustiga tushganda (kesishganda).",
        "c": "Ularning yuzasi teng bo'lganda.",
        "d": "Qahramon harakatdan to'xtaganda.",
        "e": "Faqat sichqoncha bilan bosilganda.",
        "correct": "B",
        "topic": "15-dars: AABB To'qnashuv Algoritmi",
        "expl": "AABB to'qnashuvi to'rtta shart bajarilganda (chap, o'ng, tepa, past chegaralar kesishganda) to'qnashuvni aniqlaydi."
    },
    {
        "text": "16-darsda 'Boss Jangi' dasturlanganda Boss xatti-harakatlarini boshqarish uchun qaysi arxitektura modeli ishlatilgan?",
        "a": "Tasodifiy tartibsiz if-else lar to'plami.",
        "b": "Chekli Holatlar Mashinasi (FSM - Finite State Machine: PATROL, ATTACK, LASER, ENRAGED).",
        "c": "Faqat kompyuter klaviaturasi sozlamalari.",
        "d": "Faqat CSS transition animatsiyasi.",
        "e": "Faqat audio pleyer.",
        "correct": "B",
        "topic": "16-dars: Boss Jangi va Holat Mashinasi (FSM)",
        "expl": "Boss murakkab fazalarga (Patrul, Otishma, Lazer, Quturish) ega bo'lib, uning holatlari FSM (Finite State Machine) orqali boshqariladi."
    },
    {
        "text": "17-darsda 'Web Audio API' yordamida tashqi faylsiz toza audio tovushlarni sintez qilishda nima ishlatiladi?",
        "a": "Faqat MP3 fayllarni internetdan yuklash.",
        "b": "AudioContext va OscillatorNode (to'lqin chastotasini o'zgartiruvchi generator).",
        "c": "Faqat kompyuter dinamikini o'chirib qo'yish.",
        "d": "HTML <video> tegi.",
        "e": "Telefon mikrofoni.",
        "correct": "B",
        "topic": "17-dars: Web Audio API va Tovush Sintezi",
        "expl": "Web Audio API ning AudioContext va OscillatorNode ob'yektlari sinus, kvadrat yoki arra to'lqinlari orqali real-vaqtda tovush hosil qiladi."
    },
    {
        "text": "18-darsda qahramon katta dunyo bo'ylab yurganda kamerani uni kuzatib borishi (Camera Scrolling) Canvas da qanday qilinadi?",
        "a": "Butun kompyuter ekranini qo'lda siljitish orqali.",
        "b": "Har bir kadr chizilishidan oldin ctx.translate(-cameraX, -cameraY) orqali butun kanvas koordinata tizimini siljitish bilan.",
        "c": "Qahramonni ekranning o'ng burchagida qotirib qo'yish bilan.",
        "d": "Canvas o'lchamini 100 000 pikselga kengaytirish bilan.",
        "e": "O'yinni to'xtatib qo'yish bilan.",
        "correct": "B",
        "topic": "18-dars: Kamera Skrollingi va ctx.translate",
        "expl": "Kamera siljishi ctx.translate(-camX, -camY) bilan barcha obyektlarni kamera ofsetiga mos teskari yo'nalishda chizish orqali erishiladi."
    },
    {
        "text": "19-darsda o'yinni smartfonlarda boshqarish uchun qaysi JavaScript sensorli hodisalari (Touch Events) qo'llaniladi?",
        "a": "onhover, onfocus, onblur",
        "b": "touchstart, touchmove, touchend",
        "c": "keyleft, keyright, keyup",
        "d": "dragstart, dragend, drop",
        "e": "submit, change, input",
        "correct": "B",
        "topic": "19-dars: Mobil Moslashuv va Touch Hodisalari",
        "expl": "Sensorli ekranlarda barmoq tegishi 'touchstart', siljishi 'touchmove' va olinishi 'touchend' hodisalari orqali virtual joystikni boshqaradi."
    },
    {
        "text": "21-darsdagi 'FUT Card Studio' loyihasida o'quvchi kompyuteridagi fotosuratni serverga yubormasdan brauzerda o'qish uchun nima ishlatilgan?",
        "a": "HTML5 File API va FileReader (readAsDataURL metodi).",
        "b": "SQL ma'lumotlar bazasi.",
        "c": "Faqat brauzer cookie fayllari.",
        "d": "Telegram boti.",
        "e": "Kompyuter drayverlari.",
        "correct": "A",
        "topic": "21-dars: File API va FUT Card Studio",
        "expl": "FileReader.readAsDataURL() faylni xotirada Base64 data-URL ga aylantirib, darhol <img> yoki <canvas> ga joylash imkonini beradi."
    },
    {
        "text": "21-darsning ikkinchi qismida o'yinchining OVR (Overall Rating) ko'rsatkichi qanday hisoblanadi?",
        "a": "Faqat futbolchining yoshiga qarab.",
        "b": "Futbolchining 6 ta asosiy ko'rsatkichi (PAC, SHO, PAS, DRI, DEF, PHY) ning pozitsiyaga mos vaznli o'rtacha qiymati sifatida.",
        "c": "Tasodifiy son generatori (Math.random) bilan.",
        "d": "Faqat o'yinchining bo'yi uzunligiga qarab.",
        "e": "Faqat kartaning rangi qizilligiga qarab.",
        "correct": "B",
        "topic": "21-dars: FUT OVR Formulasi va Algoritmi",
        "expl": "FUT OVR formulasi futbolchining ampulasiga (hujumchi, himoyachi) qarab atributlarni har xil og'irlikda hisoblab yakuniy reytingni beradi."
    },
    {
        "text": "22-darsdagi 'FUT Squad Builder' loyihasida 11 ta futbolchi orasidagi Kimyo (Chemistry) qanday algoritm bilan hisoblanadi?",
        "a": "Faqat bir xil rangdagi butsalarga qarab.",
        "b": "Tugunlararo bog'lanish graflari orqali: bir xil klub, bir xil liga va bir xil millatga ega futbolchilar orasidagi sinergiya ballari yig'indisi (maksimal 33 ball).",
        "c": "Faqat futbolchilarning kiyim raqamlarini qo'shish orqali.",
        "d": "Futbolchilarning narxini ko'paytirish orqali.",
        "e": "O'yinchi nechta gol urganiga qarab.",
        "correct": "B",
        "topic": "22-dars: FUT Kimyo Graflari (Chemistry Engine)",
        "expl": "Squad Builder kimyosi munosabatlar grafiga asoslanadi: tarkibdagi har bir o'yinchi jamoadoshlari bilan klub, liga va millat aloqalaridan 0 dan 3 gacha ball oladi."
    },
    {
        "text": "23-darsda 'FUT Match Engine' da o'yin simulyatsiyasi davomida qaysi mexanizm navbatdagi hujum yoki gol sodir bo'lishini hal qiladi?",
        "a": "Faqat o'yin boshidagi qura tashlash.",
        "b": "Chekli Holatlar Mashinasi (FSM) va o'yinchilarning statistik ko'rsatkichlari (SHO vs GK DIV) asosidagi ehtimollik hisob-kitobi.",
        "c": "Faqat kompyuter protsessorining harorati.",
        "d": "Foydalanuvchi klaviaturani qanchalik qattiq bosgani.",
        "e": "Faqat o'yin vaqtining soniyalari.",
        "correct": "B",
        "topic": "23-dars: FUT Match Engine va Taktik Duel",
        "expl": "Match Engine har bir vaziyatni (markazdan boshlash, hujum, zarba, seyv) FSM tsikli va o'yinchilar statistikasi dueli orqali simulyatsiya qiladi."
    },
    {
        "text": "24-darsda 'FUT Transfer Bozori' da nima uchun EA 5% lik savdo solig'i (Coin Sink) mexanizmini kiritgan?",
        "a": "Foydalanuvchilarni o'yindan zeriktirish uchun.",
        "b": "O'yin iqtisodiyotidagi tangalar ko'payib ketishi oqibatida yuzaga keladigan inflyatsiyani jilovlash va narxlarni barqaror ushlash uchun.",
        "c": "O'yin yaratuvchilari haqiqiy pul topishi uchun.",
        "d": "Faqat transferlar ro'yxatini tozalash uchun.",
        "e": "Barcha futbolchilarni bepul qilish uchun.",
        "correct": "B",
        "topic": "24-dars: FUT Transfer Bozori va 5% Coin Sink",
        "expl": "5% transfer solig'i — virtual iqtisodiyotdagi pul miqdorini kamaytiruvchi (Coin Sink) mexanizm bo'lib, o'yindagi giperinflyatsiyani to'xtatadi."
    },
    {
        "text": "25-darsdagi 'Target Jarvis' sun'iy intellektli ovozli yordamchisida gapirilgan so'zlarni matnga aylantirish uchun qaysi Web API ishlatilgan?",
        "a": "document.execCommand()",
        "b": "Web Speech API ning webkitSpeechRecognition interfeysi.",
        "c": "navigator.vibrate()",
        "d": "localStorage.getItem()",
        "e": "window.print()",
        "correct": "B",
        "topic": "25-dars: Target Jarvis va Web Speech API",
        "expl": "SpeechRecognition brauzer mikrofoni oqimini olib, nutqni matnga aylantiradi. Javobni esa SpeechSynthesis ovoz chiqarib o'qib beradi."
    },
    {
        "text": "26–27-darslardagi 'Kiber-Ko'z' va 'Biometrik Kiber-Skaner' tizimlarida 2D Photo Spoofing (ekranga rasm tutib aldash) hujumi qanday fosh qilinadi?",
        "a": "Rasmning orqa fonini qora rangga bo'yash orqali.",
        "b": "Liveness Engine yordamida: ko'z qisish (EAR - Eye Aspect Ratio), boshning 3D burilishi (Yaw/Pitch) va mikropulslarni real-vaqtda tekshirish orqali.",
        "c": "Foydalanuvchidan pasportini ko'rsatishni so'rash orqali.",
        "d": "Kamera oynasini artish orqali.",
        "e": "Faqat barmoq izini olish orqali.",
        "correct": "B",
        "topic": "26-27-dars: Biometrik Face ID va Anti-Spoofing",
        "expl": "Anti-Spoofing algoritmi statik fotosuratlar va telefon ekranlarini fosh qilish uchun insonning tiriklik belgilarini (ko'z miltillashi, harakat) tekshiradi."
    }
]

QUESTIONS_7_8_RU = [
    {
        "text": "Согласно материалам Урока 1, как Большие Языковые Модели (LLM) генерируют программный код?",
        "a": "Они мыслят в точности как человеческий мозг и принимают волевые решения независимо от компьютера.",
        "b": "Они анализируют контекст входного запроса (промпта) и на основе распределения вероятностей предсказывают следующие токены кода.",
        "c": "Они лишь напрямую копируют готовые проекты с GitHub без малейших изменений.",
        "d": "Они удаляют все программы с жесткого диска и ставят новую операционную систему.",
        "e": "Они способны понимать только HTML-теги, но не могут генерировать логику на JavaScript.",
        "correct": "B",
        "topic": "Урок 01: Основы LLM и Искусственного Интеллекта",
        "expl": "Модели LLM работают с контекстным окном (Context Window) и математически предсказывают наиболее вероятное продолжение строки кода."
    },
    {
        "text": "На Уроке 2 'AI Duel': как правильно структурировать инженерный промпт для генерации безошибочного кода?",
        "a": "Задать один короткий размытый вопрос без пояснений.",
        "b": "Четко определить Роль (Role), Задачу (Task), Технические ограничения (Constraints) и Формат вывода (Output format).",
        "c": "Отправлять нейросети исключительно смайлики и стикеры.",
        "d": "Писать промпт только на латинском транслите.",
        "e": "Дать ИИ полную свободу писать код без каких-либо правил и стеков.",
        "correct": "B",
        "topic": "Урок 02: AI Duel и инженерия промптов с ограничениями",
        "expl": "Профессиональный промпт содержит роль, стек технологий, явные ограничения и пограничные условия (edge cases)."
    },
    {
        "text": "На Уроке 3, в чем заключается главное преимущество векторного формата SVG перед растровыми изображениями (PNG/JPG)?",
        "a": "SVG бывает исключительно черно-белым.",
        "b": "SVG описывается математическими формулами (векторами и координатами), поэтому масштабируется без потери четкости при любом разрешении.",
        "c": "SVG файлы всегда занимают на диске гигантский объем (от 1 ГБ).",
        "d": "SVG изображения невозможно открыть ни в одном веб-браузере.",
        "e": "SVG предназначен исключительно для хранения видеозаписей.",
        "correct": "B",
        "topic": "Урок 03: Векторная графика SVG и ассеты интерфейса",
        "expl": "Векторный формат SVG основан на математических координатах, сохраняет идеальную резкость и весит всего несколько килобайт."
    },
    {
        "text": "На Уроке 5, почему семантические теги HTML (<header>, <nav>, <main>, <section>, <footer>) предпочтительнее сплошных <div>?",
        "a": "Они уменьшают размер HTML-файла ровно в 10 раз.",
        "b": "Они придают разметке смысловую структуру для поисковых систем (SEO), браузеров и экранных дикторов (accessibility).",
        "c": "Исключительно для автоматической раскраски страницы в яркие цвета.",
        "d": "При их использовании полностью отпадает необходимость писать JavaScript-код.",
        "e": "Они функционируют исключительно на мобильных устройствах.",
        "correct": "B",
        "topic": "Урок 05: Семантический HTML и веб-архитектура",
        "expl": "Семантические теги четко сообщают браузеру и роботам, где находится меню навигации (<nav>), а где ключевой контент статьи (<main>)."
    },
    {
        "text": "На Уроке 7 в CSS Flexbox, какое свойство центрирует дочерние элементы вдоль главной оси (main axis)?",
        "a": "align-items: center;",
        "b": "justify-content: center;",
        "c": "float: center;",
        "d": "display: block;",
        "e": "flex-direction: none;",
        "correct": "B",
        "topic": "Урок 07: CSS Flexbox и управление позиционированием",
        "expl": "В Flexbox свойство justify-content отвечает за распределение элементов вдоль главной оси, а align-items — вдоль поперечной."
    },
    {
        "text": "На Уроке 8, какой метод JavaScript используется для отслеживания клика пользователя по кнопке?",
        "a": "button.setTimer()",
        "b": "button.addEventListener('click', () => { ... });",
        "c": "window.destroy()",
        "d": "console.break()",
        "e": "document.write('click')",
        "correct": "B",
        "topic": "Урок 08: События JavaScript (DOM Events)",
        "expl": "Метод addEventListener привязывает обработчик событий к элементу DOM и выполняет колбэк-функцию при клике."
    },
    {
        "text": "На Уроке 9 в игре 'Кибер-Реакция', что применялось для высокоточного замера времени реакции в миллисекундах?",
        "a": "Картинка с изображением механических настенных часов.",
        "b": "Функция высокоточного системного времени performance.now().",
        "c": "Генератор случайных чисел Math.random().",
        "d": "Модальное окно alert().",
        "e": "CSS-свойство animation-duration.",
        "correct": "B",
        "topic": "Урок 09: Кибер-Реакция и точность performance.now()",
        "expl": "performance.now() возвращает высокоточное время с долями миллисекунды, гарантируя честный замер скорости реакции игрока."
    },
    {
        "text": "На Уроке 10 при отладке (AI Debugging), о чем говорит ошибка 'Uncaught TypeError: Cannot read properties of null' в консоли?",
        "a": "О том, что на жестком диске компьютера закончилась память.",
        "b": "Код пытается прочитать свойство или вызвать метод у элемента, которого нет в DOM (вернулся null).",
        "c": "О том, что скорость интернета упала до критического минимума.",
        "d": "О том, что пользователь закрыл вкладку браузера.",
        "e": "О том, что все переменные в программе сработали корректно.",
        "correct": "B",
        "topic": "Урок 10: Отладка в DevTools и обработка ошибок",
        "expl": "Если document.querySelector не нашел элемент, он возвращает null; попытка вызвать null.addEventListener порождает TypeError."
    },
    {
        "text": "На Уроке 11, как правильно сохранить JavaScript-объект ({score: 95, user: 'Aziz'}) в постоянное хранилище LocalStorage?",
        "a": "localStorage.setItem('record', {score: 95});",
        "b": "localStorage.setItem('record', JSON.stringify({score: 95, user: 'Aziz'}));",
        "c": "localStorage.writeAll({score: 95});",
        "d": "window.storage = {score: 95};",
        "e": "localStorage.clear('record');",
        "correct": "B",
        "topic": "Урок 11: LocalStorage и сериализация через JSON",
        "expl": "LocalStorage сохраняет исключительно строки, поэтому объекты предварительно сериализуются с помощью JSON.stringify()."
    },
    {
        "text": "На Уроке 12 при публикации игры на платформе Vercel, какой протокол безопасности выдается проекту автоматически?",
        "a": "Устаревший незашифрованный HTTP 1.0.",
        "b": "Защищенный HTTPS с бесплатным доверенным SSL/TLS сертификатом.",
        "c": "Исключительно локальное соединение localhost.",
        "d": "Беспроводной протокол Bluetooth.",
        "e": "Протокол передачи файлов FTP.",
        "correct": "B",
        "topic": "Урок 12: Веб-деплой и сертификаты HTTPS/SSL",
        "expl": "Платформы вроде Vercel автоматически генерируют SSL-сертификаты и направляют весь трафик через шифрованный канал HTTPS."
    },
    {
        "text": "На Уроке 13, какая функция используется в HTML5 Canvas для создания плавного игрового цикла со скоростью 60 FPS?",
        "a": "setInterval(update, 1000);",
        "b": "requestAnimationFrame(gameLoop);",
        "c": "setTimeout(gameLoop, 0);",
        "d": "window.reload();",
        "e": "document.refresh();",
        "correct": "B",
        "topic": "Урок 13: Canvas 2D и цикл requestAnimationFrame",
        "expl": "requestAnimationFrame синхронизирует перерисовку кадров с частотой развертки монитора (60 Гц), обеспечивая идеальную плавность."
    },
    {
        "text": "На Уроке 14, какой метод массива применяется для мгновенного удаления уничтоженных или улетевших врагов из памяти?",
        "a": "enemies.push()",
        "b": "enemies = enemies.filter(enemy => enemy.isAlive);",
        "c": "enemies.join()",
        "d": "enemies.toString()",
        "e": "enemies.reverse()",
        "correct": "B",
        "topic": "Урок 14: Работа с массивами и фильтрация объектов",
        "expl": "Метод Array.filter() оставляет в массиве только живые объекты, очищая память от уничтоженных элементов."
    },
    {
        "text": "На Уроке 15, как в коде платформера рассчитывается гравитация при прыжке и падении персонажа?",
        "a": "player.x += speed;",
        "b": "player.vy += gravity; player.y += player.vy;",
        "c": "player.y = player.y * 2;",
        "d": "player.vy = 0;",
        "e": "player.jump = true;",
        "correct": "B",
        "topic": "Урок 15: Физика игры: Гравитация и параболический прыжок",
        "expl": "На каждом кадре гравитация увеличивает вертикальную скорость (vy += g), а затем координата Y смещается на величину этой скорости."
    },
    {
        "text": "Во второй части Урока 15, при каких условиях алгоритм AABB (Axis-Aligned Bounding Box) фиксирует столкновение двух прямоугольников?",
        "a": "Когда у обоих прямоугольников совпадает цвет заливки.",
        "b": "Когда проекции обоих прямоугольников одновременно пересекаются по обеим осям X и Y.",
        "c": "Когда площади прямоугольников строго равны между собой.",
        "d": "Когда персонаж полностью прекратил движение.",
        "e": "Только при прямом нажатии мышью.",
        "correct": "B",
        "topic": "Урок 15: Алгоритм детекции столкновений AABB",
        "expl": "AABB фиксирует столкновение, если прямоугольники перекрываются по горизонтали и вертикали без учета поворота."
    },
    {
        "text": "На Уроке 16 в 'Битве с Боссом', какая архитектурная модель управляла фазами поведения Босса?",
        "a": "Хаотичный набор вложенных условий if-else.",
        "b": "Конечный Автомат (FSM - Finite State Machine: PATROL, ATTACK, LASER, ENRAGED).",
        "c": "Исключительно системные настройки клавиатуры.",
        "d": "Только анимации CSS transition.",
        "e": "Обычный аудиоплеер.",
        "correct": "B",
        "topic": "Урок 16: Битва с Боссом и Конечный Автомат (FSM)",
        "expl": "Паттерн FSM (Finite State Machine) строго переключает фазы босса в зависимости от оставшегося здоровья (HP)."
    },
    {
        "text": "На Уроке 17, с помощью чего Web Audio API позволяет генерировать чистые звуковые эффекты без загрузки аудиофайлов?",
        "a": "Только скачиванием внешних MP3-файлов из сети.",
        "b": "С помощью AudioContext и генераторов частоты OscillatorNode (синусоидальные, квадратные и пилообразные волны).",
        "c": "Исключительно отключением динамиков компьютера.",
        "d": "Через стандартный HTML-тег <video>.",
        "e": "Используя встроенный диктофон смартфона.",
        "correct": "B",
        "topic": "Урок 17: Web Audio API и синтез звука",
        "expl": "OscillatorNode синтезирует звуковые волны заданной частоты напрямую через аудиокарту без внешних файлов."
    },
    {
        "text": "На Уроке 18, как в Canvas реализуется плавное следование виртуальной камеры за бегущим героем (Camera Scrolling)?",
        "a": "Ручным перетаскиванием монитора по столу.",
        "b": "Вызовом ctx.translate(-cameraX, -cameraY) перед отрисовкой каждого кадра для смещения системы координат.",
        "c": "Жесткой фиксацией персонажа в правом углу экрана.",
        "d": "Увеличением ширины Canvas до 100 000 пикселей.",
        "e": "Полной остановкой обновления игры.",
        "correct": "B",
        "topic": "Урок 18: Скроллинг камеры и трансформация ctx.translate",
        "expl": "ctx.translate(-camX, -camY) смещает всю координатную сетку Canvas, создавая эффект движения огромного мира вокруг игрока."
    },
    {
        "text": "На Уроке 19, какие сенсорные события (Touch Events) используются в коде для адаптации управления под мобильные экраны?",
        "a": "onhover, onfocus, onblur",
        "b": "touchstart, touchmove, touchend",
        "c": "keyleft, keyright, keyup",
        "d": "dragstart, dragend, drop",
        "e": "submit, change, input",
        "correct": "B",
        "topic": "Урок 19: Мобильная адаптация и события Touch",
        "expl": "События touchstart (касание), touchmove (ведение пальцем) и touchend (отрыв) формируют работу мобильного виртуального джойстика."
    },
    {
        "text": "На Уроке 21 в 'FUT Card Studio', как прочитать фото с диска ученика прямо в браузере без отправки на сервер?",
        "a": "С помощью HTML5 File API и объекта FileReader (метод readAsDataURL).",
        "b": "Через серверную базу данных SQL.",
        "c": "Исключительно с помощью куки-файлов (cookies).",
        "d": "Через внешнего Telegram-бота.",
        "e": "Через переустановку драйверов видеокарты.",
        "correct": "A",
        "topic": "Урок 21: HTML5 File API и студия карт FUT",
        "expl": "FileReader.readAsDataURL() считывает локальный файл в строку формата Data URL (Base64) и сразу выводит его на Canvas."
    },
    {
        "text": "Во второй части Урока 21, по какой формуле рассчитывается общий рейтинг (OVR) футбольной карточки?",
        "a": "Исключительно на основе возраста игрока.",
        "b": "Как взвешенное среднее шести ключевых параметров (PAC, SHO, PAS, DRI, DEF, PHY) с учетом позиции футболиста.",
        "c": "Случайным генератором чисел Math.random().",
        "d": "Исключительно по росту спортсмена в сантиметрах.",
        "e": "Только по цвету фона карточки.",
        "correct": "B",
        "topic": "Урок 21: Формула расчета OVR в FUT",
        "expl": "Формула OVR учитывает профиль позиции: для нападающего решают SHO и PAC, а для защитника — DEF и PHY."
    },
    {
        "text": "На Уроке 22 в проекте 'FUT Squad Builder', на основе какого алгоритма рассчитывается командная химия (Chemistry)?",
        "a": "Исключительно по совпадению цвета бутс игроков.",
        "b": "На основе графа связей: сумма синергетических баллов за совпадение клуба, лиги и нации между партнерами (до 33 очков).",
        "c": "Простым суммированием номеров на футболках.",
        "d": "Умножением трансферной стоимости игроков.",
        "e": "По общему количеству забитых за карьеру голов.",
        "correct": "B",
        "topic": "Урок 22: Графы связей и движок командной химии FUT",
        "expl": "Squad Builder анализирует состав как граф связей: совпадения по клубу, чемпионату и национальности дают до 33 баллов химии."
    },
    {
        "text": "На Уроке 23 в 'FUT Match Engine', какой механизм рассчитывает исход игровых дуэлей и забитые голы в симуляторе матча?",
        "a": "Только подбрасывание монетки перед началом тайма.",
        "b": "Конечный автомат (FSM) и вероятностный дуэльный алгоритм на основе атрибутов (например, Удар нападающего против Сейва вратаря).",
        "c": "Исключительно температура нагрева процессора.",
        "d": "Сила нажатия игрока на клавишу пробела.",
        "e": "Количество миллисекунд в текущей минуте.",
        "correct": "B",
        "topic": "Урок 23: FUT Match Engine и тактическая симуляция",
        "expl": "Match Engine прогоняет фазы матча через автомат FSM, где шанс гола вычисляется математической вероятностью столкновения характеристик."
    },
    {
        "text": "На Уроке 24 в 'FUT Transfer Market', для чего разработчики ввели 5% торговый налог (Coin Sink)?",
        "a": "Чтобы отбить у игроков желание торговать.",
        "b": "Для сдерживания гиперинфляции и стабилизации цен путем планомерного вывода виртуальных монет из экономики игры.",
        "c": "Чтобы создатели игры забирали эти деньги себе в реальной жизни.",
        "d": "Исключительно для очистки базы данных от старых записей.",
        "e": "Чтобы сделать всех футболистов абсолютно бесплатными.",
        "correct": "B",
        "topic": "Урок 24: Трансферный рынок FUT и налог 5% Coin Sink",
        "expl": "5% налог с каждой продажи на трансферном рынке работает как экономический 'поглотитель монет' (Coin Sink), сдерживая инфляцию."
    },
    {
        "text": "На Уроке 25 в проекте голосового ассистента 'Target Jarvis', какой Web API распознает человеческую речь в текст?",
        "a": "document.execCommand()",
        "b": "Интерфейс webkitSpeechRecognition из стандарта Web Speech API.",
        "c": "navigator.vibrate()",
        "d": "localStorage.getItem()",
        "e": "window.print()",
        "correct": "B",
        "topic": "Урок 25: Target Jarvis и Web Speech API",
        "expl": "Web Speech API преобразует голос микрофона в текст через SpeechRecognition, а ответ синтезирует через SpeechSynthesis."
    },
    {
        "text": "На Уроках 26–27 в системах 'Кибер-Глаз' и 'Биометрический Сканер', как разоблачается атака 2D Photo Spoofing (поднесение фото к камере)?",
        "a": "Перекрашиванием фона видеопотока в сплошной черный цвет.",
        "b": "Движком проверки живого присутствия (Liveness Engine): отслеживанием моргания (EAR), 3D-поворотов головы (Yaw/Pitch) и микропульсаций.",
        "c": "Требованием показать в камеру бумажный паспорт.",
        "d": "Протиркой объектива веб-камеры влажной салфеткой.",
        "e": "Исключительно сканированием отпечатка пальца.",
        "correct": "B",
        "topic": "Уроки 26–27: Face ID, 68 точек лица и Anti-Spoofing",
        "expl": "Anti-Spoofing отвергает плоские фото с помощью Liveness Engine, требуя динамических биометрических тестов (моргание глаз по формуле EAR)."
    }
]

print("Grade 7-8 TRUE Vibecoding test data loaded (25 questions UZ & RU). Teacher: Ismoiljon Usmonov.")
