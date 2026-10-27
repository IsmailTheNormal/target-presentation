#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
9-Sinf: 25 Savolli Veb Xavfsizlik, OWASP va Tizim Ma'murligi Testi
Uzbek va Russian variantlari (5 ta variant: A, B, C, D, E)
"""

META_9_UZ = {
    "school_name": "TARGET INTERNATIONAL SCHOOL — YUNUSOBOD",
    "exam_title": "9-SINF: VEB XAVFSIZLIK, OWASP VA TIZIM MUHANDISLIGI",
    "track_title": "CyberSecurity & Junior Vibecoder Track",
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

KEYS_META_9_UZ = {
    "heading": "JAVOBLAR KALITI VA BAHOLASH MEZONI",
    "subheading": "O'qituvchi uchun rasmiy tekshirish kaliti (9-sinf, 25 ta savol)",
    "table_headers": ["№", "Kalit", "Mavzu / Kompetensiya", "Izoh va Tushuntirish"],
    "scale_heading": "Rasmiy 25 Ballik Baholash Shkalasi:",
    "rubric_tiers": [
        {"grade": "A'lo (5)", "range": "22 – 25 ball", "desc": "Veb xavfsizlik, OWASP va Linux tizim himoyasi bo'yicha mustahkam muhandislik bilimi"},
        {"grade": "Yaxshi (4)", "range": "18 – 21 ball", "desc": "SQLi, XSS, autentifikatsiya va tarmoq xavfsizligi yaxshi o'zlashtirilgan"},
        {"grade": "Qoniqarli (3)", "range": "13 – 17 ball", "desc": "Server xavfsizligi va tokenlar mexanizmini qayta takrorlash zarur"},
        {"grade": "Qoniqarsiz (2)", "range": "0 – 12 ball", "desc": "Veb xavfsizlik asoslari qaytadan o'rganilishi lozim"}
    ]
}

META_9_RU = {
    "school_name": "TARGET INTERNATIONAL SCHOOL — ЮНУСАБАД",
    "exam_title": "9 КЛАСС: ВЕБ-БЕЗОПАСНОСТЬ, OWASP И СИСТЕМНАЯ ИНЖЕНЕРИЯ",
    "track_title": "CyberSecurity & Junior Vibecoder Track",
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

KEYS_META_9_RU = {
    "heading": "КЛЮЧИ ОТВЕТОВ И КРИТЕРИИ ОЦЕНИВАНИЯ",
    "subheading": "Официальный ключ для учителя (9 класс, 25 вопросов)",
    "table_headers": ["№", "Ключ", "Тема / Компетенция", "Пояснение и Обоснование"],
    "scale_heading": "Официальная 25-балльная шкала оценивания:",
    "rubric_tiers": [
        {"grade": "Отлично (5)", "range": "22 – 25 баллов", "desc": "Глубокие инженерные знания веб-безопасности, OWASP и администрирования Linux"},
        {"grade": "Хорошо (4)", "range": "18 – 21 балл", "desc": "Хорошее понимание уязвимостей SQLi, XSS, аутентификации и сетей"},
        {"grade": "Удовлетворительно (3)", "range": "13 – 17 баллов", "desc": "Требуется повторение серверной защиты, токенов и заголовков"},
        {"grade": "Неудовлетворительно (2)", "range": "0 – 12 баллов", "desc": "Необходимо повторное изучение основ веб-безопасности"}
    ]
}

QUESTIONS_9_UZ = [
    {
        "text": "OWASP (Open Worldwide Application Security Project) tashkilotining asosiy vazifasi nima?",
        "a": "Dasturchilarga pullik litsenziyalar va dasturlar sotish.",
        "b": "Dasturiy ta'minot xavfsizligini oshirish bo'yicha bepul metodologiyalar, eng xavfli zaifliklar (OWASP Top 10) ro'yxati va himoya standartlarini ishlab chiqish.",
        "c": "Kompyuter o'yinlari uchun grafik drayverlar yaratish.",
        "d": "Internet provayderlariga optik tolali kabellar tortish.",
        "e": "Foydalanuvchilarning shaxsiy ma'lumotlarini qonuniy ravishda sotish.",
        "correct": "B",
        "topic": "OWASP Standarti",
        "expl": "OWASP — veb va dasturiy ta'minot xavfsizligi bo'yicha xalqaro ochiq konsortsium bo'lib, OWASP Top 10 standartini yaratadi."
    },
    {
        "text": "Foydalanuvchi kirish maydoniga `admin' OR '1'='1` kiritganda parolsiz tizimga kirib ketishi qaysi kiber-hujum turiga misol bo'ladi?",
        "a": "Cross-Site Scripting (XSS)",
        "b": "DDoS hujumi",
        "c": "SQL Injection (SQLi)",
        "d": "DNS Spoofing",
        "e": "Phishing",
        "correct": "C",
        "topic": "SQL Injection",
        "expl": "Foydalanuvchi ma'lumoti SQL so'rovi sintaksisini o'zgartirib, mantiqiy doimiy rost (`1=1`) shartni hosil qilishi SQL Injection deyiladi."
    },
    {
        "text": "Backend dasturchisi SQL Injection zaifligini 100% bartaraf etish uchun qanday usuldan foydalanishi shart?",
        "a": "Faqat kiruvchi parollarni tekshirish.",
        "b": "Parametrlangan so'rovlar (Prepared Statements / Parameterized Queries) orqali kiritilgan ma'lumotni kod sifatida emas, sof ma'lumot sifatida uzatish.",
        "c": "Barcha matnlarni katta harflarga o'tkazish.",
        "d": "Ma'lumotlar bazasini har 1 soatda o'chirib qayta yoqish.",
        "e": "SQL o'rniga faqat matnli fayllardan foydalanish.",
        "correct": "B",
        "topic": "Prepared Statements",
        "expl": "Parametrlangan so'rovlar ma'lumotlar bazasi drayveriga SQL sintaksisi va foydalanuvchi parametrlarini alohida uzatadi, inyeksiya imkonini yo'qotadi."
    },
    {
        "text": "XSS (Cross-Site Scripting) hujumining mohiyati nimadan iborat?",
        "a": "Server protsessorini haddan tashqari yuklash.",
        "b": "Foydalanuvchining brauzerida ruxsatsiz yovuz JavaScript kodlarini majburiy ishga tushirish.",
        "c": "Tarmoq routerini jismonan o'chirib qo'yish.",
        "d": "Kompyuter ekranining yorqinligini kamaytirish.",
        "e": "Foydalanuvchiga reklama SMS xabarlarini yuborish.",
        "correct": "B",
        "topic": "XSS Mexanizmi",
        "expl": "XSS orqali tajovuzkor veb-sahifaga skript joylab, jabrlanuvchi brauzerida cookie va sessiyalarni o'g'irlaydi."
    },
    {
        "text": "Stored (Doimiy) XSS hujumi Reflected (Qaytuvchi) XSS dan nimasi bilan farq qiladi?",
        "a": "Stored XSS faqat mobil telefonlarda ishlaydi.",
        "b": "Stored XSS da yovuz skript server ma'lumotlar bazasiga yozib saqlanadi va sahifani ochgan barcha foydalanuvchilar brauzerida avtomatik ishga tushadi.",
        "c": "Stored XSS faqat CSS stillarini o'zgartiradi.",
        "d": "Stored XSS uchun internet aloqasi talab etilmaydi.",
        "e": "Stored XSS hech qanday zarar yetkazmaydi.",
        "correct": "B",
        "topic": "Stored vs Reflected XSS",
        "expl": "Stored XSS server bazasida (masalan, izohlarda) saqlanib, sahifani ochgan har bir kishiga zarba beradi."
    },
    {
        "text": "Frontend JavaScript dasturlashda XSS ning oldini olish uchun qaysi metoddan qochish va o'rniga nimani ishlatish tavsiya etiladi?",
        "a": "`console.log()` dan qochib `alert()` ishlatish.",
        "b": "Xavfli `element.innerHTML` dan qochib, xavfsiz `element.textContent` yoki DOMPurify tozalash kutubxonasidan foydalanish.",
        "c": "Barcha o'zgaruvchilarni `var` bilan e'lon qilish.",
        "d": "HTML tugmalaridan foydalanmaslik.",
        "e": "Faqat `prompt()` oynalarini ishlatish.",
        "correct": "B",
        "topic": "DOM XSS va Sanitization",
        "expl": "`innerHTML` matn ichidagi `<script>` yoki `<img>` teglarini HTML sifatida render qiladi; `textContent` esa ularni xavfsiz oddiy matn sifatida chiqaradi."
    },
    {
        "text": "Cookie fayllarida `HttpOnly` bayrog'i (flag) yoqilganda qanday xavfsizlik kafolati ta'minlanadi?",
        "a": "Cookie faqat kunduzgi soatlarda ishlaydi.",
        "b": "Cookie fayliga mijoz tomondagi JavaScript (masalan, `document.cookie`) orqali murojaat qilish butunlay bloklanadi, bu esa XSS orqali sessiya o'g'irlanishining oldini oladi.",
        "c": "Cookie parolini foydalanuvchining o'zi o'zgartira oladi.",
        "d": "Cookie faqat Google Chrome brauzerida saqlanadi.",
        "e": "Cookie faylining hajmi 10 barobarga qisqaradi.",
        "correct": "B",
        "topic": "HttpOnly Cookie",
        "expl": "HttpOnly yovuz JavaScript kodiga `document.cookie` orqali autentifikatsiya sessiyasini o'qishga yo'l qo'ymaydi."
    },
    {
        "text": "Cookie-dagi `SameSite=Strict` atributi veb-ilovaga qanday himoya beradi?",
        "a": "Brauzerni to'liq qotirib qo'yadi.",
        "b": "Cookie faqat o'sha saytning o'zidan yuborilgan so'rovlarda uzatiladi, begona saytlardan keluvchi havolalarda cookielar yuborilmaydi (CSRF himoyasi).",
        "c": "Saytga faqat bitta kompyuterdan kirishga ruxsat beradi.",
        "d": "Cookie har 5 soniyada o'zini o'zi o'chiradi.",
        "e": "Sayt dizaynini qora mavzuga o'tkazadi.",
        "correct": "B",
        "topic": "SameSite Cookie Atributi",
        "expl": "SameSite=Strict uchinchi tomon saytlaridan kelayotgan har qanday so'rovda cookie yuborilishini bloklab, CSRF hujumlarini to'xtatadi."
    },
    {
        "text": "CSRF (Cross-Site Request Forgery) hujumi nima?",
        "a": "Foydalanuvchi kompyuteridagi fayllarni shifrlash.",
        "b": "Tajovuzkor jabrlanuvchining avtorizatsiyadan o'tgan brauzer sessiyasidan foydalanib, uning nomidan yashirincha moliyaviy yoki ma'muriy so'rovlar yuborishi.",
        "c": "Server apparaturasini elektrdan uzish.",
        "d": "Saytning logotipini soxtalashtirish.",
        "e": "Klaviaturadan terilgan belgilarni ovoz chiqarib o'qish.",
        "correct": "B",
        "topic": "CSRF Hujumi",
        "expl": "CSRF da jabrlanuvchi zararlangan havolani ochganda, uning brauzeridagi faol cookie bilan begona sayt orqali serverga uning nomidan amallar bajariladi."
    },
    {
        "text": "CSRF hujumlariga qarshi backend qanday asosiy mexanizm bilan himoyalanadi?",
        "a": "Foydalanuvchilarga har safar yangi kompyuter sotib olishni talab qilish.",
        "b": "Har bir shakl (form) va so'rovga server tomonidan yaratilgan yashirin, bir martalik va taxmin qilib bo'lmaydigan Anti-CSRF Token qo'shish.",
        "c": "Faqat GET so'rovlaridan foydalanish.",
        "d": "Barcha rasmlarni saytdan o'chirib tashlash.",
        "e": "Foydalanuvchi parolini URL manzilida ochiq ko'rsatish.",
        "correct": "B",
        "topic": "Anti-CSRF Token",
        "expl": "Anti-CSRF tokenini begona sayt o'qiy olmaydi (Same-Origin Policy), shuning uchun uning soxta so'rovlari server tomonidan rad etiladi."
    },
    {
        "text": "Nima sababdan ma'lumotlar bazasida foydalanuvchi parollarini MD5 yoki SHA-1 orqali saqlash zamonaviy xavfsizlikda qat'iyan taqiqlanadi?",
        "a": "Chunki MD5 algoritmi parollarni juda sekin hisoblaydi.",
        "b": "Chunki MD5 va SHA-1 juda tez hisoblanadi va oldindan hisoblangan tayyor jadvallar (Rainbow Tables) hamda zamonaviy GPUlar orqali soniyada milliardlab variant bilan osongina ochiladi.",
        "c": "Chunki MD5 bazada juda ko'p joy egallaydi.",
        "d": "Chunki MD5 faqat ruscha harflarni shifrlay oladi.",
        "e": "Chunki MD5 faqat 4 xonali sonlarni qo'llab-quvvatlaydi.",
        "correct": "B",
        "topic": "Kriptografik Xeshlar Zaifligi",
        "expl": "MD5/SHA-1 GPU-brute-force va Rainbow tables oldida himoyasiz. Ular tezkor hisoblangani uchun parollar xavfsizligiga yaroqsiz."
    },
    {
        "text": "Parollarni xavfsiz saqlashda `bcrypt` yoki `Argon2` algoritmlarida 'Tuz' (Salt) ning vazifasi nima?",
        "a": "Serverni ortiqcha issiqlikdan sovutish.",
        "b": "Har bir paroldan oldin unikal tasodifiy belgilar qo'shib, bir xil parolga ega ikki foydalanuvchining xeshlarini butunlay farqli qilish va Rainbow Table hujumlarini yo'qqa chiqarish.",
        "c": "Parol uzunligini qisqartirish.",
        "d": "Parolni faqat ma'lumotlar bazasi adminiga ochiq ko'rsatish.",
        "e": "Foydalanuvchini har 5 daqiqada parolini o'zgartirishga majburlash.",
        "correct": "B",
        "topic": "Salt va bcrypt",
        "expl": "Salt (tuz) har bir foydalanuvchi uchun alohida tasodifiy baytlar bo'lib, tayyor jadvallar (Rainbow Tables) yordamida parollarni ommaviy ochishni mutlaqo imkonsiz qiladi."
    },
    {
        "text": "Kiberxavfsizlikda 'Autentifikatsiya' va 'Avtorizatsiya' tushunchalari orasidagi farq nima?",
        "a": "Autentifikatsiya — o'yin o'ynash; Avtorizatsiya — kompyuterni o'chirish.",
        "b": "Autentifikatsiya — shaxsning kimligini tasdiqlash (login/parol); Avtorizatsiya — tasdiqlangan shaxsning qaysi resurslarga huquqi borligini tekshirish (admin, o'quvchi).",
        "c": "Hech qanday farqi yo'q, ikkalasi ham bir xil tushuncha.",
        "d": "Autentifikatsiya faqat Wi-Fi da, Avtorizatsiya esa faqat Bluetooth da ishlaydi.",
        "e": "Avtorizatsiya — parolni yaratish; Autentifikatsiya — uni bloklash.",
        "correct": "B",
        "topic": "AuthN vs AuthZ",
        "expl": "Authentication (AuthN) = 'Siz kimsiz?' (kimlikni isbotlash); Authorization (AuthZ) = 'Sizga nimalarga ruxsat berilgan?' (vakolatlar doirasi)."
    },
    {
        "text": "JWT (JSON Web Token) tuzilishi nuqtalar (.) bilan ajratilgan qaysi 3 qismdan tashkil topgan?",
        "a": "HTML, CSS, JavaScript.",
        "b": "Header (Sarlavha), Payload (Foydali yuk/ma'lumotlar) va Signature (Raqamli imzo).",
        "c": "Login, Parol, Email.",
        "d": "IP-manzil, MAC-manzil, DNS-server.",
        "e": "Protsessor, Tezkor xotira, Qattiq disk.",
        "correct": "B",
        "topic": "JWT Tuzilishi",
        "expl": "JWT uchta Base64Url qismdan iborat: Header (algoritm turi), Payload (foydalanuvchi da'volari/claims), Signature (server maxfiy kaliti bilan imzo)."
    },
    {
        "text": "Veb-saytda HTTPS (TLS/SSL) protokoli nima uchun shart qilib qo'yilgan?",
        "a": "Saytdagi video va rasmlar hajmini kattalashtirish uchun.",
        "b": "Brauzer va server o'rtasidagi ma'lumotlar oqimini shifrlab, oraliqdagi tajovuzkorlar (MITM) parollar yoki xabarlarni o'qiy olmasligini ta'minlash uchun.",
        "c": "Internet tezligini 10 barobarga pasaytirish uchun.",
        "d": "Faqat Windows operatsion tizimida saytlarni ochish uchun.",
        "e": "Saytga faqat pullik a'zolik orqali kirishni joriy etish uchun.",
        "correct": "B",
        "topic": "HTTPS va TLS Shifrlash",
        "expl": "HTTPS transport qatlamida assimetrik va simmetrik kriptografiya orqali trafik yaxlitligi va maxfiyligini kafolatlaydi."
    },
    {
        "text": "Linux serverni xavfsiz sozlashda `/etc/ssh/sshd_config` faylida `PermitRootLogin no` qoidasi nima uchun o'rnatiladi?",
        "a": "Barcha foydalanuvchilarning hisoblarini serverdan o'chirish uchun.",
        "b": "Tajovuzkorlarning to'g'ridan-to'g'ri 'root' (superfoydalanuvchi) nomi bilan serverga SSH orqali kirishini taqiqlash va hujum yuzasini qisqartirish uchun.",
        "c": "Server internetini to'xtatish uchun.",
        "d": "Faqat root foydalanuvchiga parol kiritish huquqini berish uchun.",
        "e": "Serverdagi barcha veb-saytlarni bloklash uchun.",
        "correct": "B",
        "topic": "Linux Server Hardening",
        "expl": "Root foydalanuvchiga to'g'ridan-to'g'ri SSH login taqiqlanadi; avval oddiy foydalanuvchi sifatida kirib, keyin `sudo` orqali vakolat oshiriladi."
    },
    {
        "text": "SSH orqali serverga kirishda ochiq va yopiq kalitlar (Public/Private Key) juftligi qanday ishlaydi?",
        "a": "Ikkala kalit ham serverga yuklanadi va ommaga tarqatiladi.",
        "b": "Ochiq kalit (Public key) serverdagi `authorized_keys` ga joylanadi, maxfiy yopiq kalit (Private key) esa faqat foydalanuvchining shaxsiy kompyuterida qoladi va hech qachon tarmoqqa uzatilmaydi.",
        "c": "Kalitlar har kuni internet orqali barchaga bepul yuboriladi.",
        "d": "Yopiq kalit yordamida faqat musiqa tinglash mumkin.",
        "e": "Ochiq kalit har doim fleshkaga ko'chirilib yo'q qilinadi.",
        "correct": "B",
        "topic": "SSH Kalitlari Arxitekturasi",
        "expl": "Asimmetrik kriptografiya: server public key bilan qiyin topishmoq (challenge) shifrlaydi, uni faqat mijozdagi private key yechib isbotlay oladi."
    },
    {
        "text": "Linux-da maxfiy server konfiguratsiya fayliga `chmod 777` buyrug'ini berish nima sababdan jiddiy xavfsizlik xatosi hisoblanadi?",
        "a": "Fayl operatsion tizimdan butunlay o'chib ketadi.",
        "b": "Tizimdagi har qanday foydalanuvchi yoki kompromiss qilingan jarayonga ushbu maxfiy faylni o'qish, o'zgartirish va ishga tushirish (rwx) huquqini to'liq ochib beradi.",
        "c": "Fayl nomi avtomatik o'zgaradi.",
        "d": "Server xotirasi to'lib qoladi.",
        "e": "Fayl faqat konsolda ko'rinmay qoladi.",
        "correct": "B",
        "topic": "Linux File Permissions",
        "expl": "777 huquqi (rwxrwxrwx) Owner, Group va Others uchun to'liq ruxsat beradi, bu esa eng xavfli ma'muriy xatolardan biridir."
    },
    {
        "text": "Linux tizimlarida UFW (Uncomplicated Firewall) vositasi qanday vazifani bajaradi?",
        "a": "Antivirus kabi qattiq diskdagi fayllarni skanerlash.",
        "b": "Serverning kiruvchi va chiquvchi tarmoq portlarini boshqarish, faqat ruxsat berilgan portlarni (masalan, 22, 80, 443) ochib, qolgan barcha begona ulanishlarni bloklash.",
        "c": "Foydalanuvchilarning monitor ranglarini sozlash.",
        "d": "Dasturlash tillarini avtomatik yangilash.",
        "e": "Klaviaturadagi bosilgan tugmalar sonini hisoblash.",
        "correct": "B",
        "topic": "UFW Firewall",
        "expl": "UFW — iptables uchun sodda interfeys bo'lib, foydalanilmayotgan xavfli portlarni (masalan, ochiq ma'lumotlar bazasi portlari) tashqi olamdan berkitadi."
    },
    {
        "text": "Serverda `Fail2ban` dasturiy vositasi qanday ishlaydi?",
        "a": "Server xotirasini optimallashtirib, o'yinlarni tezlashtiradi.",
        "b": "Tizim loglarini (masalan, auth.log) doimiy kuzatib, ketma-ket bir necha bor noto'g'ri parol tergan tajovuzkorning IP-manzilini avtomatik ravishda vaqtinchalik yoki butunlay bloklaydi.",
        "c": "O'chirilgan fayllarni savatdan qaytaradi.",
        "d": "Foydalanuvchilarga bepul SSL sertifikat tarqatadi.",
        "e": "Sayt dizaynini yangi versiyaga yangilaydi.",
        "correct": "B",
        "topic": "Fail2ban Himoyasi",
        "expl": "Fail2ban log fayllardagi xatolarni tahlil qilib, brute-force qilayotgan IP-manzillarni firewall (iptables/ufw) orqali blokirovka qiladi."
    },
    {
        "text": "Xavfsizlik bo'yicha mutaxassislar (va xakerlar) `Nmap` dasturidan nima maqsadda foydalanishadi?",
        "a": "Kino va seriallarni yuqori sifatda tomosha qilish.",
        "b": "Maqsadli tarmoq yoki serverdagi ochiq portlarni, ishlayotgan xizmatlarni (services) va ularning operatsion tizim versiyalarini skanerlab aniqlash.",
        "c": "Qattiq diskdagi keraksiz kesh fayllarni tozalash.",
        "d": "Word hujjatlaridagi grammatik xatolarni tuzatish.",
        "e": "Foydalanuvchining ovozini o'zgartirib gapirish.",
        "correct": "B",
        "topic": "Nmap Port Skaneri",
        "expl": "Nmap (Network Mapper) — tarmoqdagi xostlar, ochiq portlar va zaif servis versiyalarini aniqlash uchun kiber-razvedkaning asosiy vositasidir."
    },
    {
        "text": "`Wireshark` dasturiy vositasining tarmoq xavfsizligidagi asosiy vazifasi nima?",
        "a": "Video montaj qilish va 3D modellash.",
        "b": "Tarmoq interfeysidan o'tayotgan paketlarni ushlab olish (sniffing), ularning protokollari va mazmunini chuqur tahlil qilish.",
        "c": "Elektron pochta qutilariga avtomatik spam yuborish.",
        "d": "Kompyuterni begona fleshkalardan formatlash.",
        "e": "Faqat kompyuter o'yinlari tezligini (FPS) o'lchash.",
        "correct": "B",
        "topic": "Wireshark Paket Tahlili",
        "expl": "Wireshark — tarmoq trafigini paketlar darajasida (Ethernet, IP, TCP, HTTP) tahlil qiluvchi sniffer va diagnostika vositasi."
    },
    {
        "text": "DDoS (Distributed Denial of Service) hujumining oddiy DoS hujumidan tub farqi nimada?",
        "a": "DDoS faqat bitta noutbukdan amalga oshiriladi.",
        "b": "DDoS hujumida dunyo bo'ylab tarqalgan minglab zararlangan qurilmalar (Botnet / Zombi tarmog'i) bir vaqtning o'zida bitta serverga so'rovlar yog'dirib, uni ishdan chiqaradi.",
        "c": "DDoS faqat Wi-Fi yo'q joyda ishlaydi.",
        "d": "DDoS serverdagi parollarni o'g'irlaydi, lekin server faoliyatini to'xtatmaydi.",
        "e": "DDoS faqat SMS xabarlari orqali tarqaladi.",
        "correct": "B",
        "topic": "DoS vs DDoS va Botnet",
        "expl": "DDoS taqsimlangan bo'lib, botnet to'dasi orqali server kanalini (bandwidth) va resurslarini to'ldirib, qonuniy mijozlarga xizmat ko'rsatishni to'xtatadi."
    },
    {
        "text": "Node.js/Express dasturchilari nima uchun o'z loyihalariga `helmet` (Helmet.js) kutubxonasini o'rnatadilar?",
        "a": "Dasturning ishlash tezligini 100 barobarga oshirish uchun.",
        "b": "HTTP javob sarlavhalarini (masalan, X-Powered-By ni yashirish, CSP, X-Frame-Options) avtomatik xavfsiz sozlab, ko'plab standart veb-zaifliklarni to'sish uchun.",
        "c": "Sayt logotipiga ritsar dubulg'asi rasmini chizish uchun.",
        "d": "Faqat Bluetooth ulanishlarini tekshirish uchun.",
        "e": "Ma'lumotlar bazasiga avtomatik ulanish hosil qilish uchun.",
        "correct": "B",
        "topic": "Helmet.js va Xavfsiz Sarlavhalar",
        "expl": "Helmet.js 15 ga yaqin xavfsizlik HTTP sarlavhalarini o'rnatib, clickjacking, MIME-sniffing va boshqa hujumlardan ilovani himoya qiladi."
    },
    {
        "text": "Dasturiy loyihada API kalitlari, ma'lumotlar bazasi parollari va maxfiy tokenlarni xavfsiz saqlashning eng to'g'ri amaliyoti qaysi?",
        "a": "Ularni JavaScript kodining ichiga to'g'ridan-to'g'ri ochiq yozish va GitHub ga yuklash.",
        "b": "Maxfiy parametrlarni `.env` muhit faylida saqlash va ushbu fayl nomini `.gitignore` ro'yxatiga kiritib, ochiq repozitoriyga chiqib ketishining oldini olish.",
        "c": "Parollarni saytning bosh sahifasidagi rasm tagiga izoh qilib yozish.",
        "d": "Barcha API kalitlarini o'chirib tashlab, parolsiz ishlash.",
        "e": "Maxfiy kalitlarni brauzer konsoliga doimiy chop etib borish.",
        "correct": "B",
        "topic": "Environment Variables va .gitignore",
        "expl": "Maxfiy ma'lumotlar hech qachon manba kodida (hardcoded) bo'lmasligi kerak; ular `.env` faylida saqlanadi va `.gitignore` orqali repo himoyalanadi."
    }
]

QUESTIONS_9_RU = [
    {
        "text": "Какова главная миссия международной организации OWASP (Open Worldwide Application Security Project)?",
        "a": "Продавать разработчикам платные коммерческие антивирусы.",
        "b": "Повышать безопасность ПО путем разработки бесплатных методологий, стандартов защиты и отчетов о самых критических уязвимостях (OWASP Top 10).",
        "c": "Создавать графические драйверы для компьютерных игр.",
        "d": "Прокладывать оптоволоконные интернет-кабели между городами.",
        "e": "Легально перепродавать персональные данные пользователей рекламодателям.",
        "correct": "B",
        "topic": "Стандарт OWASP",
        "expl": "OWASP — некоммерческий консорциум, создающий стандарты и всемирный рейтинг топ-уязвимостей веб-приложений."
    },
    {
        "text": "Когда злоумышленник вводит в поле логина `admin' OR '1'='1` и входит в систему без пароля, какую уязвимость он эксплуатирует?",
        "a": "Cross-Site Scripting (XSS)",
        "b": "DDoS-атаку",
        "c": "SQL Injection (SQL-инъекцию)",
        "d": "DNS-спуфинг",
        "e": "Фишинг",
        "correct": "C",
        "topic": "SQL Injection",
        "expl": "Внедрение вредоносного SQL-кода меняет логику запроса к БД на постоянное истинное условие (`1=1`), обходя проверку пароля."
    },
    {
        "text": "Какой метод обязан использовать бэкенд-разработчик для 100% надежного предотвращения SQL-инъекций?",
        "a": "Проверять только сложность паролей на клиенте.",
        "b": "Использовать параметризованные запросы (Prepared Statements), передающие данные отдельно от исполняемого SQL-синтаксиса.",
        "c": "Переводить весь текст запроса в верхний регистр.",
        "d": "Перезагружать базу данных каждые 60 минут.",
        "e": "Отказаться от SQL в пользу обычных текстовых файлов.",
        "correct": "B",
        "topic": "Prepared Statements",
        "expl": "Параметризованные запросы разделяют код и пользовательские данные, делая исполнение инъецированных команд невозможным."
    },
    {
        "text": "В чем заключается фундаментальная суть уязвимости XSS (Cross-Site Scripting)?",
        "a": "В аппаратной перегрузке центрального процессора сервера.",
        "b": "В принудительном внедрении и выполнении вредоносного JavaScript-кода в браузере доверенного пользователя.",
        "c": "В физическом отключении сетевого коммутатора.",
        "d": "В программном снижении яркости монитора.",
        "e": "В массовой отправке рекламных SMS-сообщений.",
        "correct": "B",
        "topic": "Механизм XSS",
        "expl": "XSS позволяет атакующему выполнять скрипты в контексте браузера жертвы для кражи сессий и учетных данных."
    },
    {
        "text": "Чем постоянная (Stored / Хранимая) XSS отличается от отраженной (Reflected) XSS?",
        "a": "Stored XSS способна работать исключительно на смартфонах.",
        "b": "При Stored XSS вредоносный скрипт сохраняется в базе данных сервера и автоматически запускается в браузере каждого посетителя страницы.",
        "c": "Stored XSS изменяет исключительно фоновые цвета CSS.",
        "d": "Для Stored XSS не требуется подключение к интернету.",
        "e": "Stored XSS абсолютно безвредна для пользователей.",
        "correct": "B",
        "topic": "Stored vs Reflected XSS",
        "expl": "Хранимая XSS внедряется в БД (например, в комментарии) и атакует всех пользователей, загрузивших страницу."
    },
    {
        "text": "Какого метода следует избегать во фронтенд-разработке на JavaScript для защиты от DOM-based XSS, и что использовать взамен?",
        "a": "Избегать `console.log()` и заменять его на `alert()`.",
        "b": "Избегать опасного свойства `innerHTML` и использовать безопасный `textContent` либо библиотеку санитизации DOMPurify.",
        "c": "Объявлять абсолютно все переменные через устаревший `var`.",
        "d": "Полностью отказаться от кнопок в HTML-разметке.",
        "e": "Использовать исключительно диалоговые окна `prompt()`.",
        "correct": "B",
        "topic": "DOM XSS и Санитизация",
        "expl": "`innerHTML` парсит строки как исполняемый HTML-код, а `textContent` экранирует символы и вставляет их как безопасный плоский текст."
    },
    {
        "text": "Какую гарантию безопасности обеспечивает установка флага `HttpOnly` для Cookie-файлов сессии?",
        "a": "Файлы Cookie функционируют исключительно в дневное время суток.",
        "b": "Клиентский JavaScript (например, `document.cookie`) полностью лишается доступа к чтению этой Cookie, предотвращая ее кражу через XSS.",
        "c": "Пользователь получает возможность вручную редактировать свой пароль в Cookie.",
        "d": "Cookie сохраняется только в браузере Google Chrome.",
        "e": "Размер Cookie уменьшается ровно в десять раз.",
        "correct": "B",
        "topic": "HttpOnly Cookie",
        "expl": "Флаг HttpOnly защищает токены аутентификации от кражи вредоносными скриптами на стороне клиента."
    },
    {
        "text": "Какую ключевую защиту дает атрибут `SameSite=Strict` в заголовке Set-Cookie?",
        "a": "Полностью замораживает работу браузера при открытии сайта.",
        "b": "Cookie отправляется только при прямых запросах с этого же домена и блокируется при любых переходах со сторонних сайтов (защита от CSRF).",
        "c": "Разрешает доступ к сайту только с одного конкретного компьютера.",
        "d": "Cookie автоматически самоуничтожается каждые 5 секунд.",
        "e": "Переключает тему оформления веб-сайта на темную.",
        "correct": "B",
        "topic": "Атрибут SameSite",
        "expl": "SameSite=Strict предотвращает передачу авторизационных кук при межсайтовых запросах, нейтрализуя атаки CSRF."
    },
    {
        "text": "Что представляет собой атака CSRF (Cross-Site Request Forgery / Межсайтовая подделка запроса)?",
        "a": "Шифрование файлов на жестком диске жертвы с требованием выкупа.",
        "b": "Вынуждение авторизованного браузера жертвы скрытно отправить нежелательный запрос (перевод денег, смена пароля) на целевой уязвимый сервер.",
        "c": "Физическое обесточивание серверного оборудования.",
        "d": "Подделка визуального логотипа веб-сайта.",
        "e": "Чтение вслух символов, набираемых пользователем на клавиатуре.",
        "correct": "B",
        "topic": "Атака CSRF",
        "expl": "CSRF эксплуатирует доверие сервера к браузеру аутентифицированного пользователя, отправляя команды от его имени."
    },
    {
        "text": "Какой общепринятый механизм надежно защищает веб-приложение от атак класса CSRF?",
        "a": "Требование от клиентов покупки нового ноутбука при каждом входе.",
        "b": "Генерация сервером и проверка уникального, непредсказуемого одноразового Anti-CSRF токена для каждой формы и транзакции.",
        "c": "Использование исключительно GET-запросов для любых операций.",
        "d": "Полное удаление всех изображений с веб-страниц.",
        "e": "Отображение пароля пользователя прямо в URL-адресе страницы.",
        "correct": "B",
        "topic": "Anti-CSRF Токен",
        "expl": "Сторонний сайт не может узнать Anti-CSRF токен из-за политики Same-Origin, поэтому его поддельные запросы отклоняются сервером."
    },
    {
        "text": "Почему хранение паролей в базе данных с помощью алгоритмов MD5 или SHA-1 сегодня категорически запрещено?",
        "a": "Потому что алгоритм MD5 работает слишком медленно.",
        "b": "Потому что они вычисляются экстремально быстро, а современные GPU и готовые таблицы (Rainbow Tables) подбирают миллиарды таких хешей в секунду.",
        "c": "Потому что MD5 занимает терабайты дискового пространства.",
        "d": "Потому что алгоритм MD5 поддерживает только кириллицу.",
        "e": "Потому что он способен хешировать только четырехзначные числа.",
        "correct": "B",
        "topic": "Слабость MD5 и SHA-1",
        "expl": "Быстрые хеши непригодны для паролей. Атакующие мгновенно восстанавливают исходные пароли методом брутфорса на GPU."
    },
    {
        "text": "Какова главная роль криптографической 'Соли' (Salt) в алгоритмах хеширования паролей `bcrypt` и `Argon2`?",
        "a": "Охлаждение процессора сервера при интенсивной нагрузке.",
        "b": "Добавление уникальной случайной последовательности к каждому паролю, что делает хеши одинаковых паролей разными и обесценивает Rainbow Tables.",
        "c": "Принудительное сокращение длины пароля до 8 символов.",
        "d": "Предоставление администратору возможности видеть пароль в открытом виде.",
        "e": "Автоматическая смена пароля пользователя каждые 5 минут.",
        "correct": "B",
        "topic": "Salt и bcrypt",
        "expl": "Соль делает каждый хеш уникальным, предотвращая атаки по предварительно вычисленным радужным таблицам."
    },
    {
        "text": "В чем заключается фундаментальное различие между понятиями 'Аутентификация' и 'Авторизация'?",
        "a": "Аутентификация — запуск компьютерной игры; Авторизация — завершение работы ОС.",
        "b": "Аутентификация — подтверждение подлинности личности (кто вы?); Авторизация — проверка прав доступа к ресурсам (что вам разрешено делать?).",
        "c": "Между ними нет никакой разницы, это абсолютные синонимы.",
        "d": "Аутентификация применяется только в Wi-Fi, а Авторизация — в Bluetooth.",
        "e": "Авторизация — создание пароля; Аутентификация — блокировка учетной записи.",
        "correct": "B",
        "topic": "AuthN vs AuthZ",
        "expl": "Аутентификация удостоверяет личность (логин/пароль), а авторизация определяет уровень прав и полномочий (роли User, Admin)."
    },
    {
        "text": "Из каких 3 структурных частей, разделенных точками, состоит стандартный JSON Web Token (JWT)?",
        "a": "HTML, CSS, JavaScript.",
        "b": "Header (Заголовок), Payload (Полезная нагрузка / данные) и Signature (Цифровая подпись).",
        "c": "Логин, Пароль, Email.",
        "d": "IP-адрес, MAC-адрес, DNS-сервер.",
        "e": "Процессор, Оперативная память, Жесткий диск.",
        "correct": "B",
        "topic": "Структура JWT",
        "expl": "JWT состоит из трех частей в формате Base64Url: Заголовок (алгоритм), Полезные данные (claims) и Криптографическая подпись."
    },
    {
        "text": "Зачем каждому современному веб-сайту критически необходимо обязательное использование протокола HTTPS (TLS)?",
        "a": "Чтобы искусственно увеличить объем загружаемых видеороликов.",
        "b": "Чтобы надежно зашифровать трафик между браузером и сервером, предотвращая перехват и модификацию данных злоумышленниками (атаки MITM).",
        "c": "Чтобы замедлить интернет-соединение ровно в 10 раз.",
        "d": "Чтобы сайт открывался исключительно в операционной системе Windows.",
        "e": "Чтобы сделать доступ к сайту платным для всех пользователей.",
        "correct": "B",
        "topic": "Протокол HTTPS и TLS",
        "expl": "HTTPS обеспечивает сквозное шифрование, гарантируя конфиденциальность и целостность передаваемых паролей и данных."
    },
    {
        "text": "Почему при настройке безопасности Linux-сервера в файле `/etc/ssh/sshd_config` задают директиву `PermitRootLogin no`?",
        "a": "Чтобы удалить все учетные записи с сервера.",
        "b": "Чтобы запретить прямое подключение к серверу под суперпользователем 'root' по SSH, уменьшая поверхность атак методом перебора.",
        "c": "Чтобы полностью отключить интернет на сервере.",
        "d": "Чтобы разрешить вход по паролю только пользователю root.",
        "e": "Чтобы заблокировать отображение веб-сайтов на сервере.",
        "correct": "B",
        "topic": "Харденинг Linux-сервера",
        "expl": "Прямой вход под root по SSH запрещается для безопасности; администраторы входят под обычным логином и повышают права через `sudo`."
    },
    {
        "text": "Как работает аутентификация по SSH-ключам (Public/Private Key)?",
        "a": "Оба ключа копируются на сервер и публикуются в открытом доступе.",
        "b": "Открытый ключ (Public) размещается на сервере в `authorized_keys`, а секретный закрытый ключ (Private) хранится только на ПК пользователя и никогда не передается по сети.",
        "c": "Ключи ежедневно рассылаются всем желающим по электронной почте.",
        "d": "Закрытый ключ используется исключительно для воспроизведения аудиофайлов.",
        "e": "Открытый ключ каждый раз копируется на флешку и уничтожается.",
        "correct": "B",
        "topic": "Архитектура SSH-ключей",
        "expl": "Асимметричная криптография: сервер шифрует проверку открытым ключом, а клиент расшифровывает ее своим приватным ключом."
    },
    {
        "text": "Почему установка прав доступа `chmod 777` на конфигурационный файл в Linux является грубейшей ошибкой безопасности?",
        "a": "Файл мгновенно удаляется из файловой системы навсегда.",
        "b": "Любой пользователь и любой скомпрометированный процесс в системе получают полный доступ на чтение, изменение и выполнение этого файла.",
        "c": "Имя файла автоматически заменяется на случайный набор цифр.",
        "d": "Оперативная память сервера мгновенно переполняется.",
        "e": "Файл становится невидимым в окне терминала.",
        "correct": "B",
        "topic": "Права доступа в Linux",
        "expl": "Права 777 (rwxrwxrwx) дают неограниченные полномочия владельцу, группе и всем остальным, создавая критическую дыру в защите."
    },
    {
        "text": "Какую ключевую задачу выполняет системная утилита UFW (Uncomplicated Firewall) в Linux?",
        "a": "Сканирует жесткий диск на наличие вирусов подобно антивирусу.",
        "b": "Управляет сетевым межсетевым экраном, разрешая доступ только к нужным портам (22, 80, 443) и блокируя все несанкционированные подключения извне.",
        "c": "Настраивает цветовую гамму монитора пользователя.",
        "d": "Автоматически обновляет версии установленных компиляторов.",
        "e": "Подсчитывает суммарное число нажатий клавиш на клавиатуре.",
        "correct": "B",
        "topic": "Файрвол UFW",
        "expl": "UFW — удобный интерфейс для управления iptables, закрывающий незащищенные сетевые порты от атак из интернета."
    },
    {
        "text": "По какому принципу утилита `Fail2ban` защищает сервер от атак методом подбора паролей (Brute-Force)?",
        "a": "Оптимизирует ОЗУ для увеличения частоты кадров в играх.",
        "b": "Непрерывно анализирует системные логи (например, auth.log) и при обнаружении серии неудачных попыток входа автоматически блокирует IP-адрес атакующего через файрвол.",
        "c": "Восстанавливает случайно удаленные файлы из корзины.",
        "d": "Бесплатно раздает коммерческие SSL-сертификаты.",
        "e": "Обновляет графическую оболочку сервера до новой версии.",
        "correct": "B",
        "topic": "Защита Fail2ban",
        "expl": "Fail2ban мониторит системные журналы и динамически добавляет правила блокировки в iptables для IP-адресов с подозрительной активностью."
    },
    {
        "text": "С какой основной целью специалисты по информационной безопасности (и этичные хакеры) используют утилиту `Nmap`?",
        "a": "Для просмотра фильмов и сериалов в сверхвысоком разрешении.",
        "b": "Для сканирования целевых сетей и хостов с целью выявления открытых сетевых портов, работающих служб и версий их операционных систем.",
        "c": "Для очистки системного диска от временных файлов кэша.",
        "d": "Для автоматической проверки пунктуации в документах Word.",
        "e": "Для изменения тональности голоса при звонках.",
        "correct": "B",
        "topic": "Сканер портов Nmap",
        "expl": "Nmap — отраслевой стандарт сетевого сканирования, используемый для аудита открытых портов и инвентаризации сервисов."
    },
    {
        "text": "Каково главное предназначение анализатора сетевых протоколов `Wireshark`?",
        "a": "Профессиональный монтаж видео и 3D-анимация.",
        "b": "Перехват сетевых пакетов (sniffing) в реальном времени и их детальный побайтовый анализ на разных уровнях модели OSI.",
        "c": "Массовая генерация спам-рассылок по базам адресов.",
        "d": "Принудительное форматирование чужих USB-накопителей.",
        "e": "Измерение скорости обновления кадров (FPS) в играх.",
        "correct": "B",
        "topic": "Анализ пакетов в Wireshark",
        "expl": "Wireshark позволяет захватывать и подробно исследовать сетевой трафик, выявляя передачу данных в открытом виде (HTTP, Telnet)."
    },
    {
        "text": "В чем заключается принципиальное отличие распределенной DDoS-атаки от обычной DoS-атаки?",
        "a": "DDoS-атака всегда проводится исключительно с одного мобильного телефона.",
        "b": "При DDoS атакующие запросы генерируются одновременно огромным количеством зараженных компьютеров по всему миру (Ботнетом), что делает блокировку по одному IP невозможной.",
        "c": "DDoS функционирует только в помещениях без сети Wi-Fi.",
        "d": "DDoS похищает пароли пользователей, не влияя на доступность сервера.",
        "e": "DDoS распространяется исключительно через короткие SMS-сообщения.",
        "correct": "B",
        "topic": "DoS vs DDoS и Ботнеты",
        "expl": "DDoS распределена (Distributed): армия ботов перегружает сетевой канал или ресурсы сервера, лишая легитимных клиентов доступа."
    },
    {
        "text": "Зачем разработчики приложений на Node.js/Express подключают модуль `helmet` (Helmet.js)?",
        "a": "Чтобы ускорить рендеринг веб-страниц ровно в 100 раз.",
        "b": "Чтобы автоматически настроить безопасные HTTP-заголовки (скрыть заголовок X-Powered-By, включить CSP, X-Frame-Options) и защититься от типовых веб-атак.",
        "c": "Чтобы отобразить изображение рыцарского шлема рядом с логотипом сайта.",
        "d": "Чтобы проверять наличие активных Bluetooth-соединений.",
        "e": "Чтобы автоматически подключаться к удаленной базе данных без логина.",
        "correct": "B",
        "topic": "Helmet.js и Заголовки Безопасности",
        "expl": "Helmet устанавливает критически важные защитные заголовки ответа HTTP, предотвращая атаки кликджекинга и XSS."
    },
    {
        "text": "Какая практика хранения секретных ключей API и паролей базы данных является общепринятым стандартом безопасности?",
        "a": "Вписывать ключи открытым текстом прямо в исходный код JavaScript и коммитить в публичный репозиторий GitHub.",
        "b": "Хранить секреты в файле переменных окружения `.env`, а сам файл `.env` обязательно добавлять в `.gitignore`, чтобы он никогда не попал в репозиторий.",
        "c": "Публиковать пароли в комментариях под фотографиями на главной странице сайта.",
        "d": "Удалить все пароли и перевести проект на работу без авторизации.",
        "e": "Постоянно выводить секретные токены в консоль браузера `console.log()`.",
        "correct": "B",
        "topic": "Переменные окружения и .gitignore",
        "expl": "Секреты должны храниться в переменных окружения (`.env`) и исключаться из контроля версий через `.gitignore`."
    }
]

print("Grade 9 test data loaded (25 questions UZ & RU).")
