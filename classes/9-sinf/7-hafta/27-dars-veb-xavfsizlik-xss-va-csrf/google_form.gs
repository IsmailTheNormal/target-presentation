/**
 * Target International School — Google Forms Generator Script
 * Dars: 9-Sinf: 27-Dars Veb Xavfsizlik: XSS, CSRF va Input Sanitization — Kiber-Test
 * 
 * QO'LLANMA:
 * 1. https://script.new sahifasini oching.
 * 2. Ushbu fayl kodini to'liq nusxalab, script.new tahrirchisiga qo'ying.
 * 3. Tepada funksiyani tanlang (masalan, createGoogleForm_27_dars_veb_xavfsizlik_xss_va_csrf_uz) va "Run" (▶️) tugmasini bosing.
 * 4. Google Drive ichingizda test avtomatik yaratiladi va konsolda havola chiqadi!
 */

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
 * Dars: 9-Sinf: 27-Dars Veb Xavfsizlik: XSS, CSRF va Input Sanitization — Kiber-Test
 * Til / Language: RU
 */
function createGoogleForm_27_dars_veb_xavfsizlik_xss_va_csrf_ru() {
  // 1. Yangi Google Form yaratish va Quiz rejimini yoqish
  var form = FormApp.create("9-Класс: Урок 27 Веб-Безопасность: XSS, CSRF и Санитизация — Кибер-Тест");
  form.setDescription("Target International School // 9-Класс // Тест по кибербезопасности 7-й недели\nТема: Виды XSS, CSRF токены, DOMPurify и заголовки Helmet\nУчитель: М. Мусульмонов");
  form.setIsQuiz(true);
  form.setRequireLogin(false);
  form.setCollectEmail(true);
  form.setShowLinkToRespondAgain(false);
  form.setProgressBar(true);
  form.setShuffleQuestions(false);

  // 2. O'quvchi ma'lumotlarini to'plash
  form.addTextItem().setTitle("Ф.И.О. Учащегося").setRequired(true);
  form.addListItem().setTitle("Выберите ваш класс:").setChoiceValues(["9-A", "9-B"]).setRequired(true);

  // Savol 1 (2 ball)
  var q1 = form.addMultipleChoiceItem();
  q1.setTitle("1. Какой тип XSS сохраняется в базе данных и поражает каждого пользователя при открытии страницы?");
  q1.setPoints(2);
  q1.setChoices([
    q1.createChoice("Stored (Хранимый / Постоянный) XSS", true),
    q1.createChoice("Reflected (Отраженный) XSS", false),
    q1.createChoice("DOM-based XSS", false),
    q1.createChoice("Слепая SQL-инъекция", false)
  ]);
  q1.setFeedbackForCorrect(FormApp.createFeedback().setText("Верно! Stored XSS сохраняется в БД и выполняется в браузере любого посетителя страницы.").build());
  q1.setFeedbackForIncorrect(FormApp.createFeedback().setText("Неверно. Постоянный XSS в базе данных — это Stored XSS.").build());
  q1.setRequired(true);

  // Savol 2 (3 ball)
  var q2 = form.addMultipleChoiceItem();
  q2.setTitle("2. Какая защита наиболее эффективна против атак CSRF (межсайтовая подделка запроса)?");
  q2.setPoints(3);
  q2.setChoices([
    q2.createChoice("Криптографические Anti-CSRF токены и режим 'SameSite=Strict' для куки", true),
    q2.createChoice("Использование исключительно HTTPS протокола", false),
    q2.createChoice("Требование смены пароля каждые 15 минут", false),
    q2.createChoice("Проверка IP адреса пользователя", false)
  ]);
  q2.setFeedbackForCorrect(FormApp.createFeedback().setText("Верно! Anti-CSRF токены и SameSite=Strict блокируют несанкционированную отправку запросов.").build());
  q2.setFeedbackForIncorrect(FormApp.createFeedback().setText("Неверно. HTTPS защищает канал, но браузер все равно прикрепит куки. Нужен CSRF токен.").build());
  q2.setRequired(true);

  // Savol 3 (3 ball)
  var q3 = form.addMultipleChoiceItem();
  q3.setTitle("3. Какой инструмент используется в JavaScript для безопасного рендеринга и очистки пользовательского HTML от XSS?");
  q3.setPoints(3);
  q3.setChoices([
    q3.createChoice("Библиотека DOMPurify (DOMPurify.sanitize) или свойство textContent", true),
    q3.createChoice("Прямая вставка в element.innerHTML", false),
    q3.createChoice("Парсинг через функцию eval()", false),
    q3.createChoice("Простая замена слова <script> через RegEx", false)
  ]);
  q3.setFeedbackForCorrect(FormApp.createFeedback().setText("Отлично! DOMPurify удаляет уязвимые обработчики событий и скрипты, а textContent трактует ввод как чистый текст.").build());
  q3.setFeedbackForIncorrect(FormApp.createFeedback().setText("Неверно. innerHTML открывает прямую уязвимость к XSS. Используйте DOMPurify или textContent.").build());
  q3.setRequired(true);

  // Savol 4 (2 ball)
  var q4 = form.addMultipleChoiceItem();
  q4.setTitle("4. Какой middleware автоматически настраивает заголовки CSP, HSTS и X-Frame-Options в Express.js?");
  q4.setPoints(2);
  q4.setChoices([
    q4.createChoice("Helmet.js (app.use(helmet()))", true),
    q4.createChoice("Morgan logger", false),
    q4.createChoice("Nodemon", false),
    q4.createChoice("Babel compiler", false)
  ]);
  q4.setFeedbackForCorrect(FormApp.createFeedback().setText("Верно! Helmet.js устанавливает важнейшие заголовки HTTP безопасности.").build());
  q4.setFeedbackForIncorrect(FormApp.createFeedback().setText("Неверно. Общепринятый стандарт защиты заголовков Express — Helmet.js.").build());
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
 * Til / Language: EN
 */
function createGoogleForm_27_dars_veb_xavfsizlik_xss_va_csrf_en() {
  // 1. Yangi Google Form yaratish va Quiz rejimini yoqish
  var form = FormApp.create("Grade 9: Lesson 27 Web Security: XSS, CSRF & Input Sanitization — Quiz");
  form.setDescription("Target International School // Grade 9 // Week 7 Web Security Quiz\nTopic: XSS Vectors (Stored, Reflected, DOM), Anti-CSRF Tokens, DOMPurify & Helmet Headers\nInstructor: M. Musulmonov");
  form.setIsQuiz(true);
  form.setRequireLogin(false);
  form.setCollectEmail(true);
  form.setShowLinkToRespondAgain(false);
  form.setProgressBar(true);
  form.setShuffleQuestions(false);

  // 2. O'quvchi ma'lumotlarini to'plash
  form.addTextItem().setTitle("Student Full Name").setRequired(true);
  form.addListItem().setTitle("Select your class:").setChoiceValues(["9-A", "9-B"]).setRequired(true);

  // Savol 1 (2 ball)
  var q1 = form.addMultipleChoiceItem();
  q1.setTitle("1. Which type of XSS is persisted in the database and impacts every user loading the page?");
  q1.setPoints(2);
  q1.setChoices([
    q1.createChoice("Stored (Persistent) XSS", true),
    q1.createChoice("Reflected XSS", false),
    q1.createChoice("DOM-based XSS", false),
    q1.createChoice("Blind SQL Injection", false)
  ]);
  q1.setFeedbackForCorrect(FormApp.createFeedback().setText("Correct! Stored XSS persists in the database and executes for every client requesting that page.").build());
  q1.setFeedbackForIncorrect(FormApp.createFeedback().setText("Incorrect. The persistent database vector is Stored XSS.").build());
  q1.setRequired(true);

  // Savol 2 (3 ball)
  var q2 = form.addMultipleChoiceItem();
  q2.setTitle("2. Which defense mechanism is most effective against CSRF (Cross-Site Request Forgery) attacks?");
  q2.setPoints(3);
  q2.setChoices([
    q2.createChoice("Cryptographic Anti-CSRF tokens and 'SameSite=Strict' cookie configuration", true),
    q2.createChoice("Relying solely on HTTPS transport encryption", false),
    q2.createChoice("Enforcing password resets every 15 minutes", false),
    q2.createChoice("Validating client IP addresses", false)
  ]);
  q2.setFeedbackForCorrect(FormApp.createFeedback().setText("Correct! Anti-CSRF tokens and SameSite=Strict eliminate cross-origin unauthorized requests.").build());
  q2.setFeedbackForIncorrect(FormApp.createFeedback().setText("Incorrect. HTTPS protects data in transit, but browsers still send cookies unless tokens are enforced.").build());
  q2.setRequired(true);

  // Savol 3 (3 ball)
  var q3 = form.addMultipleChoiceItem();
  q3.setTitle("3. Which tool is used in JavaScript to safely sanitize user-supplied HTML against XSS?");
  q3.setPoints(3);
  q3.setChoices([
    q3.createChoice("DOMPurify library (DOMPurify.sanitize) or the element.textContent property", true),
    q3.createChoice("Direct assignment into element.innerHTML", false),
    q3.createChoice("Evaluating strings using the eval() function", false),
    q3.createChoice("Simple RegEx replacement of the word <script>", false)
  ]);
  q3.setFeedbackForCorrect(FormApp.createFeedback().setText("Excellent! DOMPurify strips event-based vectors and scripts, while textContent safely escapes raw text.").build());
  q3.setFeedbackForIncorrect(FormApp.createFeedback().setText("Incorrect. innerHTML is the primary cause of XSS. Always use DOMPurify or textContent.").build());
  q3.setRequired(true);

  // Savol 4 (2 ball)
  var q4 = form.addMultipleChoiceItem();
  q4.setTitle("4. Which middleware automatically configures CSP, HSTS, and X-Frame-Options security headers in Express.js?");
  q4.setPoints(2);
  q4.setChoices([
    q4.createChoice("Helmet.js (app.use(helmet()))", true),
    q4.createChoice("Morgan logger", false),
    q4.createChoice("Nodemon", false),
    q4.createChoice("Babel compiler", false)
  ]);
  q4.setFeedbackForCorrect(FormApp.createFeedback().setText("Correct! Helmet.js secures Express apps by setting various HTTP headers.").build());
  q4.setFeedbackForIncorrect(FormApp.createFeedback().setText("Incorrect. The industry standard middleware for HTTP headers is Helmet.js.").build());
  q4.setRequired(true);

  Logger.log("=========================================");
  Logger.log("✅ Google Form muvaffaqiyatli yaratildi!");
  Logger.log("📌 Form Nomi: " + form.getTitle());
  Logger.log("✏️ Tahrirlash havolasi (Edit URL): " + form.getEditUrl());
  Logger.log("🌐 O'quvchilarga tarqatish havolasi (Published URL): " + form.getPublishedUrl());
  Logger.log("=========================================");
}
