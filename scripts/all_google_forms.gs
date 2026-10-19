/**
 * Target International School — Barcha Darslar Google Forms Yaratuvchisi
 */

/**
 * Target International School — Google Form Generator
 * Dars: 9-Sinf: 28-Dars Full-Stack Xavfsiz Servis va CTF — Oraliq Nazorat Kiber-Testi
 * Til / Language: UZ
 */
function createGoogleForm_28_dars_fullstack_xavfsiz_servis_oraliq_nazorat_uz() {
  // 1. Yangi Google Form yaratish va Quiz rejimini yoqish
  var form = FormApp.create("9-Sinf: 28-Dars Full-Stack Xavfsiz Servis va CTF — Oraliq Nazorat Kiber-Testi");
  form.setDescription("Target International School // 9-Sinf // 1-Chorak Oraliq Nazorat Imtihoni\nMavzu: Express MVC, SQLite Relyatsion Sxema, JWT, XSS/CSRF va Docker Sandbox\nO'qituvchi: M. Musulmonov");
  form.setIsQuiz(true);
  form.setRequireLogin(false);
  form.setCollectEmail(true);
  form.setShowLinkToRespondAgain(false);
  form.setProgressBar(true);
  form.setShuffleQuestions(false);

  // 2. O'quvchi ma'lumotlarini to'plash
  form.addTextItem().setTitle("O'quvchining F.I.Sh. (Familiya, Ism)").setRequired(true);
  form.addListItem().setTitle("Sinfingizni tanlang:").setChoiceValues(["9-A", "9-B"]).setRequired(true);

  // Savol 1 (3 ball)
  var q1 = form.addMultipleChoiceItem();
  q1.setTitle("1. Quyidagi Express server kodida qaysi kritik zaiflik mavjud?\n\napp.post('/api/profile', (req, res) => {\n  const query = \"UPDATE users SET bio = '\" + req.body.bio + \"' WHERE id = \" + req.user.id;\n  db.run(query);\n  res.send('<h1>Updated:</h1><div>' + req.body.bio + '</div>');\n});");
  q1.setPoints(3);
  q1.setChoices([
    q1.createChoice("Kritik zaiflik: bir vaqtning o'zida ham SQL Injection (satr qo'shish), ham Stored/Reflected XSS (sanitizatsiyasiz HTML) mavjud!", true),
    q1.createChoice("Kod mutlaqo xavfsiz, chunki GET o'rniga POST metodi qo'llanilgan.", false),
    q1.createChoice("Yagona xato — Content-Type sarlavhasi yozilmaganligida.", false),
    q1.createChoice("Faqat server xotirasida (RAM) resurs yetishmovchiligi yuz beradi.", false)
  ]);
  q1.setFeedbackForCorrect(FormApp.createFeedback().setText("To'g'ri! Satrlarni birlashtirish (' + req.body.bio + ') SQL Injection ochadi, to tozalanmagan matnni res.send() bilan qaytarish esa XSS xurujiga sabab bo'ladi.").build());
  q1.setFeedbackForIncorrect(FormApp.createFeedback().setText("Xato. Bu yerda bir vaqtning o'zida ham SQL Injection, ham XSS xavfi mavjud. Parametrlangan so'rovlar (?) va DOMPurify/res.json ishlatilishi shart.").build());
  q1.setRequired(true);

  // Savol 2 (2 ball)
  var q2 = form.addMultipleChoiceItem();
  q2.setTitle("2. SQLite relyatsion ma'lumotlar bazasida 'orders' jadvalidagi 'user_id' ustuniga nima uchun FOREIGN KEY cheklovi qo'yiladi?");
  q2.setPoints(2);
  q2.setChoices([
    q2.createChoice("Faqat mavjud bo'lgan foydalanuvchilar buyurtma bera olishini kafolatlash (Referential Integrity)", true),
    q2.createChoice("Foydalanuvchi parolini SHA-256 orqali avtomatik shifrlash uchun", false),
    q2.createChoice("Server diskida fayl hajmini 50% gacha tejash uchun", false),
    q2.createChoice("Faqat SELECT so'rovlarini keshlab olish uchun", false)
  ]);
  q2.setFeedbackForCorrect(FormApp.createFeedback().setText("A'lo! FOREIGN KEY jadvallar o'rtasidagi bog'liqlik va referensial yaxlitlikni saqlaydi, mavjud bo'lmagan id ga buyurtma yozilishiga yo'l qo'ymaydi.").build());
  q2.setFeedbackForIncorrect(FormApp.createFeedback().setText("Xato. FOREIGN KEY — ma'lumotlar bazasida referensial yaxlitlik (Referential Integrity) kafolatidir.").build());
  q2.setRequired(true);

  // Savol 3 (2 ball)
  var q3 = form.addMultipleChoiceItem();
  q3.setTitle("3. JWT (JSON Web Token) autentifikatsiyasida tokenni XSS skriptlaridan o'g'irlanishiga yo'l qo'ymaslik uchun eng xavfsiz saqlash usuli qaysi?");
  q3.setPoints(2);
  q3.setChoices([
    q3.createChoice("Brauzer kuki faylida 'HttpOnly; Secure; SameSite=Strict' bayroqlari bilan saqlash", true),
    q3.createChoice("Brauzerning LocalStorage xotirasida ochiq saqlash", false),
    q3.createChoice("Tokinni har bir URL manzilida query parametr (?token=...) sifatida uzatish", false),
    q3.createChoice("HTML tegidagi data-* atributi ichida qoldirish", false)
  ]);
  q3.setFeedbackForCorrect(FormApp.createFeedback().setText("To'g'ri! HttpOnly bayrog'i JavaScript document.cookie buyrug'iga to'siq qo'yadi va XSS kiber-xurujlarida tokenni o'g'irlashni imkonsiz qiladi.").build());
  q3.setFeedbackForIncorrect(FormApp.createFeedback().setText("Xato. LocalStorage ga XSS skripti osongina kira oladi. Eng xavfsiz yo'l — HttpOnly; Secure; SameSite=Strict kuki.").build());
  q3.setRequired(true);

  // Savol 4 (3 ball)
  var q4 = form.addMultipleChoiceItem();
  q4.setTitle("4. Dockerfile da nima sababdan 'USER node' (non-root) direktivasi yozilishi xavfsizlik standarti hisoblanadi?");
  q4.setPoints(3);
  q4.setChoices([
    q4.createChoice("Konteyner ichida RCE (masofaviy kod bajarish) zaifligi yuz berganda xakerga xost operatsion tizimining root huquqlari o'tib ketmasligi uchun", true),
    q4.createChoice("Node.js serverining ishlash tezligini 2 barobar oshirish uchun", false),
    q4.createChoice("Konteyner fayl hajmini MB larda qisqartirish uchun", false),
    q4.createChoice("Faqat Vercel yoki AWS platformalarida deploy qilish imkoniyatini ochish uchun", false)
  ]);
  q4.setFeedbackForCorrect(FormApp.createFeedback().setText("To'g'ri! Minimal imtiyozlar printsipi (Principle of Least Privilege) konteyner sindirilganda xost serverini to'liq egallashdan asraydi.").build());
  q4.setFeedbackForIncorrect(FormApp.createFeedback().setText("Xato. Agar Docker konteyneri root foydalanuvchida ishlasa, xaker serverni to'liq boshqaruvga oladi. USER node non-root huquq beradi.").build());
  q4.setRequired(true);

  Logger.log("=========================================");
  Logger.log("✅ Google Form muvaffaqiyatli yaratildi!");
  Logger.log("📌 Form Nomi: " + form.getTitle());
  Logger.log("✏️ Tahrirlash havolasi (Edit URL): " + form.getEditUrl());
  Logger.log("🌐 O'quvchilarga tarqatish havolasi (Published URL): " + form.getPublishedUrl());
  Logger.log("=========================================");
}

/**
 * Target International School — Google Form Generator
 * Dars: 9-Sinf: 27-Dars Veb Xavfsizlik: XSS, CSRF va Input Sanitization — Kiber-Test
 * Til / Language: UZ
 */
function createGoogleForm_27_dars_veb_xavfsizlik_xss_va_csrf_uz() {
  // 1. Yangi Google Form yaratish va Quiz rejimini yoqish
  var form = FormApp.create("9-Sinf: 27-Dars Veb Xavfsizlik: XSS, CSRF va Input Sanitization — Kiber-Test");
  form.setDescription("Target International School // 9-Sinf // 7-Hafta Kiber-Xavfsizlik Testi\nMavzu: XSS turlari (Stored, Reflected, DOM), Anti-CSRF tokenlar, DOMPurify va Helmet sarlavhalari\nO'qituvchi: M. Musulmonov");
  form.setIsQuiz(true);
  form.setRequireLogin(false);
  form.setCollectEmail(true);
  form.setShowLinkToRespondAgain(false);
  form.setProgressBar(true);
  form.setShuffleQuestions(false);

  // 2. O'quvchi ma'lumotlarini to'plash
  form.addTextItem().setTitle("O'quvchining F.I.Sh. (Familiya, Ism)").setRequired(true);
  form.addListItem().setTitle("Sinfingizni tanlang:").setChoiceValues(["9-A", "9-B"]).setRequired(true);

  // Savol 1 (2 ball)
  var q1 = form.addMultipleChoiceItem();
  q1.setTitle("1. XSS (Cross-Site Scripting) kiber-hujumining qaysi turi ma'lumotlar bazasida saqlanib, sahifani ochgan barcha foydalanuvchilarga doimiy zarar yetkazadi?");
  q1.setPoints(2);
  q1.setChoices([
    q1.createChoice("Stored (Persistent) XSS", true),
    q1.createChoice("Reflected (Aks etuvchi) XSS", false),
    q1.createChoice("DOM-based XSS", false),
    q1.createChoice("Blind SQL Injection", false)
  ]);
  q1.setFeedbackForCorrect(FormApp.createFeedback().setText("To'g'ri! Stored XSS ma'lumotlar bazasiga (masalan sharhlar yoki profil bio ga) yoziladi va saytga kirgan barcha odamlarda ishga tushadi.").build());
  q1.setFeedbackForIncorrect(FormApp.createFeedback().setText("Xato. Bazada saqlanuvchi va hammaga ta'sir qiluvchi XSS turi — bu Stored (Persistent) XSS.").build());
  q1.setRequired(true);

  // Savol 2 (3 ball)
  var q2 = form.addMultipleChoiceItem();
  q2.setTitle("2. Veb-ilovada foydalanuvchining sessiyasini aldov yo'li bilan ishlatuvchi CSRF (Cross-Site Request Forgery) xurujiga qarshi qaysi himoya eng samarali?");
  q2.setPoints(3);
  q2.setChoices([
    q2.createChoice("Kriptografik Anti-CSRF tokenlar va cookie uchun 'SameSite=Strict' rejimi", true),
    q2.createChoice("Faqat HTTPS shifrlash sertifikatini yoqish", false),
    q2.createChoice("Foydalanuvchi parolini har 15 daqiqada yangilatish", false),
    q2.createChoice("Foydalanuvchining IP manzilini tekshirish", false)
  ]);
  q2.setFeedbackForCorrect(FormApp.createFeedback().setText("To'g'ri! Anti-CSRF token taxmin qilib bo'lmaydigan maxfiy kalit bo'lib, SameSite=Strict esa begona saytlardan kuki yuborilishini man etadi.").build());
  q2.setFeedbackForIncorrect(FormApp.createFeedback().setText("Xato. HTTPS protokoli CSRF dan asramaydi, chunki brauzer kukilarni avtomatik qo'shib yuboradi. Anti-CSRF token shart.").build());
  q2.setRequired(true);

  // Savol 3 (3 ball)
  var q3 = form.addMultipleChoiceItem();
  q3.setTitle("3. JavaScript da foydalanuvchi kiritgan matnni xavfsiz render qilishda XSS dan xalos bo'lish uchun qaysi vosita qo'llaniladi?");
  q3.setPoints(3);
  q3.setChoices([
    q3.createChoice("DOMPurify kutubxonasi (DOMPurify.sanitize) yoki element.textContent xususiyati", true),
    q3.createChoice("To'g'ridan-to'g'ri element.innerHTML ga tenglashtirish", false),
    q3.createChoice("eval() funksiyasi orqali matnni tahlil qilish", false),
    q3.createChoice("Faqat regex orqali <script> so'zini qirqib tashlash", false)
  ]);
  q3.setFeedbackForCorrect(FormApp.createFeedback().setText("A'lo! DOMPurify zararli onload, onerror va script xurujlarini tozalaydi, textContent esa matnni HTML emas, oddiy string sifatida xavfsiz chiqaradi.").build());
  q3.setFeedbackForIncorrect(FormApp.createFeedback().setText("Xato. innerHTML eng xavfli XSS manbasidir. DOMPurify yoki textContent ishlatish shart.").build());
  q3.setRequired(true);

  // Savol 4 (2 ball)
  var q4 = form.addMultipleChoiceItem();
  q4.setTitle("4. Express.js backend serverida Content-Security-Policy (CSP), HSTS va X-Frame-Options sarlavhalarini avtomatik ulovchi middleware qaysi?");
  q4.setPoints(2);
  q4.setChoices([
    q4.createChoice("Helmet.js (app.use(helmet()))", true),
    q4.createChoice("Morgan logger", false),
    q4.createChoice("Nodemon", false),
    q4.createChoice("Babel compiler", false)
  ]);
  q4.setFeedbackForCorrect(FormApp.createFeedback().setText("To'g'ri! Helmet.js 15 ta xavfsizlik HTTP sarlavhasini bir qatorda faollashtiradi.").build());
  q4.setFeedbackForIncorrect(FormApp.createFeedback().setText("Xato. Express da sanoat standarti — bu Helmet.js middleware kutubxonasidir.").build());
  q4.setRequired(true);

  Logger.log("=========================================");
  Logger.log("✅ Google Form muvaffaqiyatli yaratildi!");
  Logger.log("📌 Form Nomi: " + form.getTitle());
  Logger.log("✏️ Tahrirlash havolasi (Edit URL): " + form.getEditUrl());
  Logger.log("🌐 O'quvchilarga tarqatish havolasi (Published URL): " + form.getPublishedUrl());
  Logger.log("=========================================");
}

/**
 * Target International School — Google Form Generator
 * Dars: 10–11-Sinf: 32-Dars Korporativ Tarmoq Himoyasi va CTF — Oraliq Nazorat Kiber-Testi
 * Til / Language: UZ
 */
function createGoogleForm_32_dars_korporativ_himoya_va_ctf_uz() {
  // 1. Yangi Google Form yaratish va Quiz rejimini yoqish
  var form = FormApp.create("10–11-Sinf: 32-Dars Korporativ Tarmoq Himoyasi va CTF — Oraliq Nazorat Kiber-Testi");
  form.setDescription("Target International School // 10–11-Sinf // 1-Chorak Oraliq Nazorat Imtihoni\nMavzu: NIST SP 800-61 Hodisalar Tsikli, Blue Team Hardening, Red Team Exploitation, MTTR\nO'qituvchi: M. Musulmonov");
  form.setIsQuiz(true);
  form.setRequireLogin(false);
  form.setCollectEmail(true);
  form.setShowLinkToRespondAgain(false);
  form.setProgressBar(true);
  form.setShuffleQuestions(false);

  // 2. O'quvchi ma'lumotlarini to'plash
  form.addTextItem().setTitle("O'quvchining F.I.Sh. (Familiya, Ism)").setRequired(true);
  form.addListItem().setTitle("Sinfingizni tanlang:").setChoiceValues(["10-A", "10-B", "11-A", "11-B"]).setRequired(true);

  // Savol 1 (2 ball)
  var q1 = form.addMultipleChoiceItem();
  q1.setTitle("1. NIST SP 800-61 standarti bo'yicha kiber-insidentlarni boshqarish tsiklining to'g'ri ketma-ketligi qaysi javobda ko'rsatilgan?");
  q1.setPoints(2);
  q1.setChoices([
    q1.createChoice("1. Tayyorgarlik (Preparation) -> 2. Aniqlash va Tahlil (Detection) -> 3. Izolyatsiya va Yo'q qilish (Containment/Eradication) -> 4. Insidentdan keyingi faoliyat (Post-Incident)", true),
    q1.createChoice("1. Hujum qilish -> 2. Xulosa chiqarish -> 3. Serverni o'chirish -> 4. Parol yangilash", false),
    q1.createChoice("1. Skanerlash -> 2. Brute-Force -> 3. Port ochish -> 4. Hisobot berish", false),
    q1.createChoice("1. Firewall o'rnatish -> 2. Kutish -> 3. Backup olish", false)
  ]);
  q1.setFeedbackForCorrect(FormApp.createFeedback().setText("To'g'ri! NIST SP 800-61 qat'iy 4 fazadan iborat bo'lib, xalqaro SOC va kiber-xavfsizlik markazlarining qonunidir.").build());
  q1.setFeedbackForIncorrect(FormApp.createFeedback().setText("Xato. Standart tartib: Preparation -> Detection -> Containment & Eradication -> Post-Incident Activity.").build());
  q1.setRequired(true);

  // Savol 2 (3 ball)
  var q2 = form.addMultipleChoiceItem();
  q2.setTitle("2. Blue Team muhandisi Linux serverida tarmoq perimetrini 'Default Deny' tamoyili asosida sozlashda qaysi UFW buyruqlarini kiritishi kerak?");
  q2.setPoints(3);
  q2.setChoices([
    q2.createChoice("ufw default deny incoming && ufw allow 2222/tcp && ufw enable", true),
    q2.createChoice("ufw allow all incoming && ufw default allow", false),
    q2.createChoice("ufw disable && iptables -F", false),
    q2.createChoice("ufw reject outgoing && ufw allow 80/tcp", false)
  ]);
  q2.setFeedbackForCorrect(FormApp.createFeedback().setText("To'g'ri! Default deny barcha kiruvchi trafikni yopadi va faqat xavfsizlangan nostandart SSH (2222-port) ulanishiga ruxsat beradi.").build());
  q2.setFeedbackForIncorrect(FormApp.createFeedback().setText("Xato. Xavfsiz tarmoq barcha kiruvchi paketlarni bloklaydi (default deny incoming) va faqat kerakli portlarni ochiq qoldiradi.").build());
  q2.setRequired(true);

  // Savol 3 (3 ball)
  var q3 = form.addMultipleChoiceItem();
  q3.setTitle("3. Kiber-xavfsizlik SOC boshqaruvida MTTR (Mean Time to Remediate) va MTTD (Mean Time to Detect) ko'rsatkichlari qanday ta'riflanadi?");
  q3.setPoints(3);
  q3.setChoices([
    q3.createChoice("MTTD — tahdidni aniqlashgacha bo'lgan o'rtacha vaqt; MTTR — insident aniqlangandan to uni to'liq bartaraf etguncha ketgan o'rtacha vaqt", true),
    q3.createChoice("MTTR — serverning protsessor tezligi; MTTD — tarmoq kabelining o'tkazuvchanligi", false),
    q3.createChoice("MTTD — xakerning tizimda qolgan umumiy yillari; MTTR — bazadagi jadvallar soni", false),
    q3.createChoice("Ushbu parametrlar faqat Windows operatsion tizimiga tegishli", false)
  ]);
  q3.setFeedbackForCorrect(FormApp.createFeedback().setText("A'lo! MTTR qanchalik kichik bo'lsa, korxona xavfsizlik quvvati va insidentlarga qarshi javob berish tezligi shunchalik yuqori hisoblanadi.").build());
  q3.setFeedbackForIncorrect(FormApp.createFeedback().setText("Xato. MTTD — aniqlash vaqti (Detect), MTTR — bartaraf etish vaqti (Remediate).").build());
  q3.setRequired(true);

  // Savol 4 (2 ball)
  var q4 = form.addMultipleChoiceItem();
  q4.setTitle("4. CTF (Capture The Flag) kiber-turnirida xakerlik exploitining yakuniy maqsadi nimadan iborat?");
  q4.setPoints(2);
  q4.setChoices([
    q4.createChoice("Zaiflik orqali tizimga kirib, nishon serveridagi yashirin bayroqcha (Flag: TARGET{...}) ni qo'lga kiritish va ball olish", true),
    q4.createChoice("Serverdagi barcha ma'lumotlarni o'chirib yuborish va tizimni qulatish", false),
    q4.createChoice("Faqat maktab veb-saytining dizaynini o'zgartirish", false),
    q4.createChoice("Antivirus dasturlarini yangilash", false)
  ]);
  q4.setFeedbackForCorrect(FormApp.createFeedback().setText("To'g'ri! Axloqiy kiber-musobaqalarda maqsad buzg'unchilik emas, balki zaiflikni fosh etuvchi bayroqcha (Flag) ni qo'lga kiritishdir.").build());
  q4.setFeedbackForIncorrect(FormApp.createFeedback().setText("Xato. CTF turnirlarida maqsad bayroqchani (Flag) olishdir. Buzg'unchilik noqonuniy va taqiqlangan.").build());
  q4.setRequired(true);

  Logger.log("=========================================");
  Logger.log("✅ Google Form muvaffaqiyatli yaratildi!");
  Logger.log("📌 Form Nomi: " + form.getTitle());
  Logger.log("✏️ Tahrirlash havolasi (Edit URL): " + form.getEditUrl());
  Logger.log("🌐 O'quvchilarga tarqatish havolasi (Published URL): " + form.getPublishedUrl());
  Logger.log("=========================================");
}

/**
 * Target International School — Google Form Generator
 * Dars: 7–8-Sinf: 30-Dars Sport Simulyatori va O'yin Fizikasi — Oraliq Nazorat Testi
 * Til / Language: UZ
 */
function createGoogleForm_30_dars_sport_simulyatori_oraliq_nazorat_uz() {
  // 1. Yangi Google Form yaratish va Quiz rejimini yoqish
  var form = FormApp.create("7–8-Sinf: 30-Dars Sport Simulyatori va O'yin Fizikasi — Oraliq Nazorat Testi");
  form.setDescription("Target International School // 7–8-Sinf // 1-Chorak Oraliq Nazorat Imtihoni\nMavzu: Tarkib Kimyosi Graflari, Match Engine FSM, 2D To'qnashuv Fizikasi va 5% Soliq\nO'qituvchi: M. Musulmonov");
  form.setIsQuiz(true);
  form.setRequireLogin(false);
  form.setCollectEmail(true);
  form.setShowLinkToRespondAgain(false);
  form.setProgressBar(true);
  form.setShuffleQuestions(false);

  // 2. O'quvchi ma'lumotlarini to'plash
  form.addTextItem().setTitle("O'quvchining F.I.Sh. (Familiya, Ism)").setRequired(true);
  form.addListItem().setTitle("Sinfingizni tanlang:").setChoiceValues(["7-A", "7-B", "8-A", "8-B"]).setRequired(true);

  // Savol 1 (2 ball)
  var q1 = form.addMultipleChoiceItem();
  q1.setTitle("1. FUT kartasining umumiy reytingi (OVR) qaysi usulda hisoblab chiqariladi?");
  q1.setPoints(2);
  q1.setChoices([
    q1.createChoice("Futbolchining ampluasiga qarab uning muhim ko'rsatkichlariga yuqori koeffitsient beruvchi vaznli formula (Weighted Average) orqali", true),
    q1.createChoice("Barcha 6 ta ko'rsatkichning (PAC, SHO, PAS, DRI, DEF, PHY) oddiy arifmetik o'rtachasi orqali", false),
    q1.createChoice("Faqat futbolchining bo'yi va yoshiga qarab", false),
    q1.createChoice("Math.random() orqali tasodifiy son berish bilan", false)
  ]);
  q1.setFeedbackForCorrect(FormApp.createFeedback().setText("To'g'ri! Masalan hujumchi uchun PAC va SHO 70% vaznga ega bo'lsa, himoyachi uchun DEF va PHY asosiy rol o'ynaydi.").build());
  q1.setFeedbackForIncorrect(FormApp.createFeedback().setText("Xato. OVR oddiy o'rtacha emas, balki ampluaga mos vaznli o'rtacha (Weighted Average) hisoblanadi.").build());
  q1.setRequired(true);

  // Savol 2 (3 ball)
  var q2 = form.addMultipleChoiceItem();
  q2.setTitle("2. Tarkib kimyosi (Chemistry) algoritmining to'liq 33 ballik sinergiyasiga qaysi shartlar orqali erishiladi?");
  q2.setPoints(3);
  q2.setChoices([
    q2.createChoice("11 ta o'yinchining to'g'ri pozitsiyada turishi hamda bir xil klub, liga va millat bo'yicha bog'lanishlarining to'liq qanoatlantirilishi", true),
    q2.createChoice("Faqat eng qimmat narxdagi oltin kartalarni sotib olish orqali", false),
    q2.createChoice("Barcha o'yinchilarning yoshi teng bo'lishi orqali", false),
    q2.createChoice("Tarkibda faqat hujumchilarni qoldirish orqali", false)
  ]);
  q2.setFeedbackForCorrect(FormApp.createFeedback().setText("A'lo! 11 ta pozitsiyadagi o'yinchilarning har biri 3 tagacha kimyo yulduzchasiga ega bo'lib, jami 33 ball beradi.").build());
  q2.setFeedbackForIncorrect(FormApp.createFeedback().setText("Xato. Kimyo kartaning narxiga bog'liq emas. Klub, liga va millat aloqalari (Graf sinergiyasi) zarur.").build());
  q2.setRequired(true);

  // Savol 3 (3 ball)
  var q3 = form.addMultipleChoiceItem();
  q3.setTitle("3. 2D o'yin fizikasi dvigatelida to'p va darvoza to'sini to'qnashuvini hisoblashda qaysi algoritm qo'llaniladi?");
  q3.setPoints(3);
  q3.setChoices([
    q3.createChoice("AABB (Axis-Aligned Bounding Box) to'rtburchaklar keshishishi formulasi", true),
    q3.createChoice("Nyutonning 1-harakat qonuni", false),
    q3.createChoice("Faqat Pifagor gipotenuzasi formulasi", false),
    q3.createChoice("CSS margin va padding qiymatlarini solishtirish", false)
  ]);
  q3.setFeedbackForCorrect(FormApp.createFeedback().setText("To'g'ri! AABB algoritmi x va y koordinatalari bo'yicha min va max chegaralarni taqqoslab, to'qnashuvni millisekundlarda fosh qiladi.").build());
  q3.setFeedbackForIncorrect(FormApp.createFeedback().setText("Xato. O'yin grafikasi va fizikasida standart to'qnashuv tekshiruvi — bu AABB (Bounding Box) algoritmidir.").build());
  q3.setRequired(true);

  // Savol 4 (2 ball)
  var q4 = form.addMultipleChoiceItem();
  q4.setTitle("4. FUT auksion bozoridagi har bir bitimdan olinadigan 5% savdo solig'i (EA Tax) virtual o'yinda qanday iqtisodiy vazifani bajaradi?");
  q4.setPoints(2);
  q4.setChoices([
    q4.createChoice("Tizimdan ortiqcha tangalarni doimiy yoqish (Coin Sink) orqali inflyatsiyani to'xtatish va bozor narxlarini barqaror saqlash", true),
    q4.createChoice("O'yin yaratuvchilarining real boyishi uchun", false),
    q4.createChoice("Kartalarni avtomatik o'chirib yuborish uchun", false),
    q4.createChoice("O'yin yuklanishini tezlashtirish uchun", false)
  ]);
  q4.setFeedbackForCorrect(FormApp.createFeedback().setText("A'lo! O'yinchilar mukofotlar orqali uzluksiz tanga ishlab chiqaradilar (Minting). 5% soliq (Coin Sink) bo'lmasa, pul qadrsizlanadi va giperinflyatsiya boshlanadi.").build());
  q4.setFeedbackForIncorrect(FormApp.createFeedback().setText("Xato. 5% auksion solig'i — o'yin iqtisodiyotidagi giperinflyatsiyaning oldini oluvchi Coin Sink mexanizmidir.").build());
  q4.setRequired(true);

  Logger.log("=========================================");
  Logger.log("✅ Google Form muvaffaqiyatli yaratildi!");
  Logger.log("📌 Form Nomi: " + form.getTitle());
  Logger.log("✏️ Tahrirlash havolasi (Edit URL): " + form.getEditUrl());
  Logger.log("🌐 O'quvchilarga tarqatish havolasi (Published URL): " + form.getPublishedUrl());
  Logger.log("=========================================");
}

/**
 * Target International School — Google Form Generator
 * Dars: 5–6-Sinf: 22-Dars Kiber-Qalqon Viktorinasi — Oraliq Nazorat Testi
 * Til / Language: UZ
 */
function createGoogleForm_22_dars_kiber_qalqon_oraliq_nazorat_uz() {
  // 1. Yangi Google Form yaratish va Quiz rejimini yoqish
  var form = FormApp.create("5–6-Sinf: 22-Dars Kiber-Qalqon Viktorinasi — Oraliq Nazorat Testi");
  form.setDescription("Target International School // 5–6-Sinf // 1-Chorak Kiber-Qalqon Viktorinasi\nMavzu: Mustahkam Parollar, Fishing Qopqonlari, Troyanlar va Shaxsiy Maxfiylik\nO'qituvchi: M. Musulmonov");
  form.setIsQuiz(true);
  form.setRequireLogin(false);
  form.setCollectEmail(true);
  form.setShowLinkToRespondAgain(false);
  form.setProgressBar(true);
  form.setShuffleQuestions(false);

  // 2. O'quvchi ma'lumotlarini to'plash
  form.addTextItem().setTitle("O'quvchining F.I.Sh. (Familiya, Ism)").setRequired(true);
  form.addListItem().setTitle("Sinfingizni tanlang:").setChoiceValues(["5-A", "5-B", "6-A", "6-B"]).setRequired(true);

  // Savol 1 (2 ball)
  var q1 = form.addMultipleChoiceItem();
  q1.setTitle("1. Kiber-xavfsizlik qoidalariga ko'ra, eng mustahkam va xakerlar buza olmaydigan parol qanday tuziladi?");
  q1.setPoints(2);
  q1.setChoices([
    q1.createChoice("Kamida 14+ ta belgi, katta va kichik harflar, raqamlar hamda maxsus belgilar (#, $, !) aralashmasidan", true),
    q1.createChoice("O'z ismi va tug'ilgan yili (masalan: ali2014)", false),
    q1.createChoice("Klaviaturadagi ketma-ket harflar (12345678 yoki qwerty)", false),
    q1.createChoice("Faqat 4 xonali oddiy PIN-kod", false)
  ]);
  q1.setFeedbackForCorrect(FormApp.createFeedback().setText("Barakalla! 14+ belgili murakkab parolni superkompyuterlar ham yuzlab yillar davomida buza olmaydi.").build());
  q1.setFeedbackForIncorrect(FormApp.createFeedback().setText("Xato. Ism, tug'ilgan yil va 123456 parolini xakerlar 1 soniyada buzib kiradilar. Parol 14+ belgili bo'lishi shart.").build());
  q1.setRequired(true);

  // Savol 2 (3 ball)
  var q2 = form.addMultipleChoiceItem();
  q2.setTitle("2. Internetda 'Shoshiling! Bepul 10,000 Robux yoki Telegram Premium beramiz, parolingizni kiriting' degan havolani ko'rsangiz nima qilishingiz kerak?");
  q2.setPoints(3);
  q2.setChoices([
    q2.createChoice("Sahifani darhol yopish va parolni kiritmaslik — bu xakerlarning fishing (aldov) qopqoni!", true),
    q2.createChoice("Tezda profilingiz parolini kiritib, bepul mukofotni kutish", false),
    q2.createChoice("Havolani barcha sinfdoshlar va guruhlarga tarqatish", false),
    q2.createChoice("Kompyuter ekranini o'chirib qo'yish", false)
  ]);
  q2.setFeedbackForCorrect(FormApp.createFeedback().setText("To'g'ri! 'Tekin pishloq faqat qopqonda bo'ladi'. Hech kim internetda bepul robux yoki pul bermaydi, bu profilni o'g'irlash usulidir.").build());
  q2.setFeedbackForIncorrect(FormApp.createFeedback().setText("Xato. Agar parolni kiritib yuborsangiz, profilingiz xakerlar qo'liga o'tadi. Soxta havolalarni aslo ochmang.").build());
  q2.setRequired(true);

  // Savol 3 (3 ball)
  var q3 = form.addMultipleChoiceItem();
  q3.setTitle("3. Fotosuratni internetga joylashdan oldin nega undagi yashirin GPS (EXIF) metama'lumotlarni tozalash zarur?");
  q3.setPoints(3);
  q3.setChoices([
    q3.createChoice("Notanish odamlar va firibgarlar sizning uyingiz, maktabingiz yoki qayerda ekanligingizni xaritada aniqlay olmasligi uchun", true),
    q3.createChoice("Suratning ranglarini yanada yorqinroq qilish uchun", false),
    q3.createChoice("Faqat smartfon xotirasini tejash uchun", false),
    q3.createChoice("Surat internetda tezroq ochilishi uchun", false)
  ]);
  q3.setFeedbackForCorrect(FormApp.createFeedback().setText("Barakalla! EXIF fotosurat olingan aniq kenglik va uzunlik koordinatalarini saqlaydi. Uni o'chirish orqali shaxsiy xavfsizligingizni ta'minlaysiz.").build());
  q3.setFeedbackForIncorrect(FormApp.createFeedback().setText("Xato. EXIF geolokatsiyasi orqali uyingiz manzilini topib olishlari mumkin. Doim rasmlarni tozalab yuklang.").build());
  q3.setRequired(true);

  // Savol 4 (2 ball)
  var q4 = form.addMultipleChoiceItem();
  q4.setTitle("4. Internetda xavfsiz yashashning 'Katta Ekran Qoidasi' (Billboard Rule) nimani anglatadi?");
  q4.setPoints(2);
  q4.setChoices([
    q4.createChoice("Shaharning eng gavjum ko'chasidagi ulkan ekranga chiqarishdan uyaladigan shaxsiy ma'lumot yoki rasmlarni internetga aslo yuklamaslik", true),
    q4.createChoice("Faqat katta televizor va monitordan foydalanish", false),
    q4.createChoice("Xabarlarni faqat KATTA HARFLARDA yozish", false),
    q4.createChoice("Kinoteatrga borib film tomosha qilish", false)
  ]);
  q4.setFeedbackForCorrect(FormApp.createFeedback().setText("To'g'ri! Internetga tushgan har qanday narsa abadiy qoladi va butun dunyoga ko'rinishi mumkin. Shuning uchun o'zingizni ehtiyot qiling!").build());
  q4.setFeedbackForIncorrect(FormApp.createFeedback().setText("Xato. 'Billboard Rule' — shaxsiy sir va noqulay narsalarni internetga qo'ymaslik qoidasidir.").build());
  q4.setRequired(true);

  Logger.log("=========================================");
  Logger.log("✅ Google Form muvaffaqiyatli yaratildi!");
  Logger.log("📌 Form Nomi: " + form.getTitle());
  Logger.log("✏️ Tahrirlash havolasi (Edit URL): " + form.getEditUrl());
  Logger.log("🌐 O'quvchilarga tarqatish havolasi (Published URL): " + form.getPublishedUrl());
  Logger.log("=========================================");
}