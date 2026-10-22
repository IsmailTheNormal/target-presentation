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

  // Savol 1 (1 ball)
  var q1 = form.addMultipleChoiceItem();
  q1.setTitle("1. Kiber-xavfsizlik qoidalariga ko'ra, eng mustahkam va xakerlar buza olmaydigan parol qanday tuziladi?");
  q1.setPoints(1);
  q1.setChoices([
    q1.createChoice("Kamida 14+ ta belgi, katta va kichik harflar, raqamlar hamda maxsus belgilar (#, $, !) aralashmasidan (Uch so'z formulasi)", true),
    q1.createChoice("O'z ismi va tug'ilgan yili (masalan: sardor2014)", false),
    q1.createChoice("Klaviaturadagi ketma-ket belgilar (12345678 yoki qwerty)", false),
    q1.createChoice("Faqat 4 xonali oddiy raqamli PIN-kod", false)
  ]);
  q1.setFeedbackForCorrect(FormApp.createFeedback().setText("Barakalla! 14+ belgili murakkab parolni superkompyuterlar ham yuzlab yillar davomida buza olmaydi.").build());
  q1.setFeedbackForIncorrect(FormApp.createFeedback().setText("Xato. Ism, tug'ilgan yil va 123456 kabi oddiy parollarni xakerlar 1 soniyada buzib kiradilar. Parol 14+ belgili bo'lishi shart.").build());
  q1.setRequired(true);

  // Savol 2 (1 ball)
  var q2 = form.addMultipleChoiceItem();
  q2.setTitle("2. Internetda 'Shoshiling! Bepul 10,000 Robux yoki Telegram Premium beramiz, parolingizni kiriting' degan havolani ko'rsangiz nima qilishingiz kerak?");
  q2.setPoints(1);
  q2.setChoices([
    q2.createChoice("Sahifani darhol yopish va parolni aslo kiritmaslik — bu xakerlarning fishing (aldov) qopqoni!", true),
    q2.createChoice("Tezda profilingiz parolini kiritib, bepul mukofotni kutish", false),
    q2.createChoice("Havolani barcha sinfdoshlar va maktab guruhlariga tarqatish", false),
    q2.createChoice("Kompyuter ekranini o'chirib qo'yish", false)
  ]);
  q2.setFeedbackForCorrect(FormApp.createFeedback().setText("To'g'ri! 'Tekin pishloq faqat qopqonda bo'ladi'. Begonalar internetda bepul robux yoki pul bermaydi, bu hisobni o'g'irlash usulidir.").build());
  q2.setFeedbackForIncorrect(FormApp.createFeedback().setText("Xato. Agar parolni kiritib yuborsangiz, profilingiz xakerlar qo'liga o'tadi. Soxta havolalarni aslo ochmang.").build());
  q2.setRequired(true);

  // Savol 3 (1 ball)
  var q3 = form.addMultipleChoiceItem();
  q3.setTitle("3. Internetdan o'yin skini yuklab oldingiz, lekin uning nomi 'cool_skin.png.exe' bo'lib chiqdi. Nega bu faylni aslo ochmaslik kerak?");
  q3.setPoints(1);
  q3.setChoices([
    q3.createChoice("Bu troyan virusi: xakerlar Windows kengaytmalarni yashirishidan foydalanib, zararli dasturni (.exe) rasm (.png) niqobiga o'rashgan!", true),
    q3.createChoice("Chunki bu fayl faqat televizorda ochiladi", false),
    q3.createChoice("Chunki fayl hajmi juda kichik", false),
    q3.createChoice("Chunki .exe kengaytmasi rasmlarni yanada chiroyliroq qiladi", false)
  ]);
  q3.setFeedbackForCorrect(FormApp.createFeedback().setText("Barakalla! Ikki qavatli kengaytma (.png.exe) — xakerlarning klassik troyan hiylasi. Bu rasm emas, kompyuterni buzuvchi zararli dasturdir.").build());
  q3.setFeedbackForIncorrect(FormApp.createFeedback().setText("Xato. .exe kengaytmasi bu dasturdir. Rasm nomi oxirida .exe bo'lsa, bu 100% troyan virusidir.").build());
  q3.setRequired(true);

  // Savol 4 (1 ball)
  var q4 = form.addMultipleChoiceItem();
  q4.setTitle("4. O'yin modini yuklab olayotganingizda saytda 'Antivirusni o'chirib qo'ying, u xato signal bermoqda' deb yozilgan bo'lsa, qanday yo'l tutish kerak?");
  q4.setPoints(1);
  q4.setChoices([
    q4.createChoice("Antivirusni aslo o'chirmaslik va shubhali faylni darhol VirusTotal.com yoki xavfsiz Sandbox laboratoriyasida tekshirish!", true),
    q4.createChoice("Antivirusni 1 kunga o'chirib, modni o'rnatish", false),
    q4.createChoice("Antivirus dasturini kompyuterdan butunlay o'chirib tashlash", false),
    q4.createChoice("Kompyuterni qayta ishga tushirib, faylni baribir ishga tushirish", false)
  ]);
  q4.setFeedbackForCorrect(FormApp.createFeedback().setText("Ofarin! Xakerlar virusni kompyuterga kiritish uchun doim foydalanuvchini aldab, antivirusni o'chirishga majburlashadi.").build());
  q4.setFeedbackForIncorrect(FormApp.createFeedback().setText("Xato. Antivirusni o'chirish — xakerga kompyuter eshigini ochib berish demakdir. Xavfsiz dasturlar antivirusni o'chirishni talab qilmaydi.").build());
  q4.setRequired(true);

  // Savol 5 (1 ball)
  var q5 = form.addMultipleChoiceItem();
  q5.setTitle("5. Telegram yoki Roblox da o'zini 'Maktab Admini' deb tanishtirgan begona kimsa: 'Profilingiz xavf ostida, SMS orqali kelgan 5 xonali tasdiqlash kodini ayting' desa, nima qilasiz?");
  q5.setPoints(1);
  q5.setChoices([
    q5.createChoice("Kodni aslo aytmaslik, yozishmani darhol bloklash va o'qituvchiga yoki ota-onaga xabar berish — bu akkauntni o'g'irlash hujumi!", true),
    q5.createChoice("SMS kodni darhol yozib yuborish, chunki u admin ekan", false),
    q5.createChoice("Kod bilan birga akkaunt parolini ham qo'shib berish", false),
    q5.createChoice("Xabarni o'chirib, yangi SMS kelishini kutish", false)
  ]);
  q5.setFeedbackForCorrect(FormApp.createFeedback().setText("To'g'ri! SMS tasdiqlash kodi — hisobingizning maxfiy kalitidir. Haqiqiy adminlar va xizmatlar hech qachon SMS kodni so'ramaydi.").build());
  q5.setFeedbackForIncorrect(FormApp.createFeedback().setText("Xato. SMS kodni berishingiz bilan xaker hisobingizni tortib oladi va sizni chiqarib yuboradi. Kodni hech kimga aytmang.").build());
  q5.setRequired(true);

  // Savol 6 (1 ball)
  var q6 = form.addMultipleChoiceItem();
  q6.setTitle("6. Firibgarlar nima sababdan 'Shoshiling! Faqat 5 daqiqa qoldi, aks holda profilingiz abadiy bloklanadi!' deb vahima uyg'otishadi?");
  q6.setPoints(1);
  q6.setChoices([
    q6.createChoice("O'quvchi qo'rqib qolsin, vahimaga tushsin va vaziyatni xotirjam tahlil qilmasdan o'z parolini berib yuborsin deb", true),
    q6.createChoice("Chunki internetda serverlar har 5 daqiqada o'chib qoladi", false),
    q6.createChoice("Bu shunchaki o'yinning texnik talabi", false),
    q6.createChoice("Do'stona salomlashish usuli", false)
  ]);
  q6.setFeedbackForCorrect(FormApp.createFeedback().setText("Barakalla! Shoshiltirish (Urgency) — firibgarlarning eng kuchli psixologik quroli. Shubhali xabar kelganda to'xtang va tekshiring!").build());
  q6.setFeedbackForIncorrect(FormApp.createFeedback().setText("Xato. Firibgarlar aynan sizni shoshirib, aql bilan o'ylashga imkon bermaslik uchun shunday qilishadi.").build());
  q6.setRequired(true);

  // Savol 7 (1 ball)
  var q7 = form.addMultipleChoiceItem();
  q7.setTitle("7. Nega smartfonda olingan fotosuratlarni internetga yuklashdan oldin undagi yashirin GPS (EXIF) ma'lumotlarini tozalash zarur?");
  q7.setPoints(1);
  q7.setChoices([
    q7.createChoice("Begonalar va kiber-firibgarlar sizning uyingiz, xonadoningiz yoki maktabingizning aniq koordinatalarini xaritada bilib olmasligi uchun", true),
    q7.createChoice("Suratning ranglarini yanada yorqinroq qilish uchun", false),
    q7.createChoice("Faqat smartfon xotirasini tejash uchun", false),
    q7.createChoice("Surat internetda tezroq ochilishi uchun", false)
  ]);
  q7.setFeedbackForCorrect(FormApp.createFeedback().setText("Barakalla! EXIF fotosurat olingan aniq GPS koordinatalarini saqlaydi. Uni tozalash orqali jismoniy xavfsizligingizni himoya qilasiz.").build());
  q7.setFeedbackForIncorrect(FormApp.createFeedback().setText("Xato. EXIF geolokatsiyasi orqali uyingiz manzilini topib olishlari mumkin. Doim rasmlarni tozalab yuklang.").build());
  q7.setRequired(true);

  // Savol 8 (1 ball)
  var q8 = form.addMultipleChoiceItem();
  q8.setTitle("8. Internetda xavfsiz yashashning 'Katta Ekran Qoidasi' (Billboard Rule) nimani anglatadi?");
  q8.setPoints(1);
  q8.setChoices([
    q8.createChoice("Shaharning eng gavjum ko'chasidagi ulkan ekranga chiqarishdan uyaladigan shaxsiy ma'lumot yoki rasmlarni internetga aslo yuklamaslik", true),
    q8.createChoice("Faqat katta televizor va monitordan foydalanish", false),
    q8.createChoice("Xabarlarni faqat KATTA HARFLARDA yozish", false),
    q8.createChoice("Kinoteatrga borib film tomosha qilish", false)
  ]);
  q8.setFeedbackForCorrect(FormApp.createFeedback().setText("To'g'ri! Internetga tushgan har qanday narsa abadiy qoladi va butun dunyoga ko'rinishi mumkin. Shuning uchun o'zingizni ehtiyot qiling!").build());
  q8.setFeedbackForIncorrect(FormApp.createFeedback().setText("Xato. 'Billboard Rule' — shaxsiy sir va noqulay narsalarni internetga qo'ymaslik qoidasidir.").build());
  q8.setRequired(true);

  // Savol 9 (1 ball)
  var q9 = form.addMultipleChoiceItem();
  q9.setTitle("9. Kafeda yoki bog'dagi ochiq bepul Wi-Fi tarmog'iga ulanganda shaxsiy hisob va parollarni o'g'irlanishdan asrashning eng ishonchli usuli qaysi?");
  q9.setPoints(1);
  q9.setChoices([
    q9.createChoice("Ishonchli VPN (Virtual Private Network) shifrlangan tunnelini yoqish va muhim bank ilovalariga yoki parolli akkauntlarga kirmaslik", true),
    q9.createChoice("Telefonni faqat quvvatlovchi simga ulab qo'yish", false),
    q9.createChoice("Ekran yorqinligini eng past darajaga tushirish", false),
    q9.createChoice("Bluetooth-ni o'chirib, ochiq saytlarda parollarni kiritaverish", false)
  ]);
  q9.setFeedbackForCorrect(FormApp.createFeedback().setText("To'g'ri! Ochiq Wi-Fi da ma'lumotlar shifrlanmagan bo'lishi mumkin. VPN trafikingizni shifrlangan tunnelga oladi.").build());
  q9.setFeedbackForIncorrect(FormApp.createFeedback().setText("Xato. Ochiq Wi-Fi da trafikni himoya qilish uchun VPN ishlatish shart.").build());
  q9.setRequired(true);

  // Savol 10 (1 ball)
  var q10 = form.addMultipleChoiceItem();
  q10.setTitle("10. Barcha fayl va fotosuratlarni shifrlab qulflovchi 'Ransomware' (Tovlamachi virus) xurujiga uchraganda ma'lumotlarni qutqarishning yagona 100% ishonchli yo'li nima?");
  q10.setPoints(1);
  q10.setChoices([
    q10.createChoice("Muhim fayllarning zaxira nusxasini (Backup) muntazam ravishda alohida tashqi fleshka yoki xavfsiz bulutda saqlab borish", true),
    q10.createChoice("Tovlamachi xakerlar talab qilgan pulni darhol to'lash", false),
    q10.createChoice("Sichqoncha va klaviaturani kompyuterdan uzib qo'yish", false),
    q10.createChoice("Kompyuter ekranini sovunli suv bilan artish", false)
  ]);
  q10.setFeedbackForCorrect(FormApp.createFeedback().setText("Barakalla! Zaxira nusxa (Backup) — Ransomware virusiga qarshi yagona haqiqiy qalqondir. Xakerlarga pul to'lamasdan fayllaringizni tiklay olasiz!").build());
  q10.setFeedbackForIncorrect(FormApp.createFeedback().setText("Xato. Xakerlarga pul to'lash kafolat bermaydi. Yagona to'g'ri chora — oldindan fayllarning zaxira nusxasini (Backup) olib yurishdir.").build());
  q10.setRequired(true);

  Logger.log("=========================================");
  Logger.log("✅ Google Form muvaffaqiyatli yaratildi!");
  Logger.log("📌 Form Nomi: " + form.getTitle());
  Logger.log("✏️ Tahrirlash havolasi (Edit URL): " + form.getEditUrl());
  Logger.log("🌐 O'quvchilarga tarqatish havolasi (Published URL): " + form.getPublishedUrl());
  Logger.log("=========================================");
}