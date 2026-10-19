/**
 * Target International School — Google Forms Generator Script
 * Dars: 9-Sinf: 28-Dars Full-Stack Xavfsiz Servis va CTF — Oraliq Nazorat Kiber-Testi
 * 
 * QO'LLANMA:
 * 1. https://script.new sahifasini oching.
 * 2. Ushbu fayl kodini to'liq nusxalab, script.new tahrirchisiga qo'ying.
 * 3. Tepada funksiyani tanlang (masalan, createGoogleForm_28_dars_fullstack_xavfsiz_servis_oraliq_nazorat_uz) va "Run" (▶️) tugmasini bosing.
 * 4. Google Drive ichingizda test avtomatik yaratiladi va konsolda havola chiqadi!
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
 * Dars: 9-Sinf: 28-Dars Full-Stack Xavfsiz Servis va CTF — Oraliq Nazorat Kiber-Testi
 * Til / Language: RU
 */
function createGoogleForm_28_dars_fullstack_xavfsiz_servis_oraliq_nazorat_ru() {
  // 1. Yangi Google Form yaratish va Quiz rejimini yoqish
  var form = FormApp.create("9-Класс: Урок 28 Полностековый Безопасный Сервис и CTF — Рубежный Тест");
  form.setDescription("Target International School // 9-Класс // Рубежный контроль 1-й четверти\nТема: Express MVC, SQLite, JWT, защита от XSS/CSRF и Docker Sandbox\nУчитель: М. Мусульмонов");
  form.setIsQuiz(true);
  form.setRequireLogin(false);
  form.setCollectEmail(true);
  form.setShowLinkToRespondAgain(false);
  form.setProgressBar(true);
  form.setShuffleQuestions(false);

  // 2. O'quvchi ma'lumotlarini to'plash
  form.addTextItem().setTitle("Ф.И.О. Учащегося").setRequired(true);
  form.addListItem().setTitle("Выберите ваш класс:").setChoiceValues(["9-A", "9-B"]).setRequired(true);

  // Savol 1 (3 ball)
  var q1 = form.addMultipleChoiceItem();
  q1.setTitle("1. Какая критическая уязвимость присутствует в следующем фрагменте кода Express?\n\napp.post('/api/profile', (req, res) => {\n  const query = \"UPDATE users SET bio = '\" + req.body.bio + \"' WHERE id = \" + req.user.id;\n  db.run(query);\n  res.send('<h1>Updated:</h1><div>' + req.body.bio + '</div>');\n});");
  q1.setPoints(3);
  q1.setChoices([
    q1.createChoice("Критическая уязвимость: одновременный SQL Injection (конкатенация) и XSS (вывод без санитизации)!", true),
    q1.createChoice("Код полностью безопасен, так как применен POST вместо GET.", false),
    q1.createChoice("Единственная ошибка — отсутствие заголовка Content-Type.", false),
    q1.createChoice("Произойдет только утечка оперативной памяти (RAM) на сервере.", false)
  ]);
  q1.setFeedbackForCorrect(FormApp.createFeedback().setText("Правильно! Конкатенация строк ведет к SQL Injection, а отправка несанитизированного ввода через res.send() создает XSS.").build());
  q1.setFeedbackForIncorrect(FormApp.createFeedback().setText("Неверно. Здесь присутствуют одновременно SQL Injection и XSS. Необходимо использовать параметризованные запросы (?) и санитизацию.").build());
  q1.setRequired(true);

  // Savol 2 (2 ball)
  var q2 = form.addMultipleChoiceItem();
  q2.setTitle("2. Зачем в реляционной базе SQLite на столбец 'user_id' таблицы 'orders' накладывается ограничение FOREIGN KEY?");
  q2.setPoints(2);
  q2.setChoices([
    q2.createChoice("Гарантировать, что заказы могут создавать только существующие пользователи (Referential Integrity)", true),
    q2.createChoice("Для автоматического шифрования паролей пользователей по SHA-256", false),
    q2.createChoice("Для уменьшения размера файла базы данных на диске на 50%", false),
    q2.createChoice("Исключительно для кэширования запросов SELECT", false)
  ]);
  q2.setFeedbackForCorrect(FormApp.createFeedback().setText("Отлично! Внешний ключ гарантирует ссылочную целостность между таблицами.").build());
  q2.setFeedbackForIncorrect(FormApp.createFeedback().setText("Неверно. Внешний ключ необходим для обеспечения ссылочной целостности данных.").build());
  q2.setRequired(true);

  // Savol 3 (2 ball)
  var q3 = form.addMultipleChoiceItem();
  q3.setTitle("3. Какой способ хранения JWT токена наиболее безопасен против кражи через XSS атаки?");
  q3.setPoints(2);
  q3.setChoices([
    q3.createChoice("Хранить в cookies с флагами 'HttpOnly; Secure; SameSite=Strict'", true),
    q3.createChoice("Хранить в открытом виде в LocalStorage браузера", false),
    q3.createChoice("Передавать токен как GET query параметр (?token=...)", false),
    q3.createChoice("Записывать в data-* атрибуты HTML разметки", false)
  ]);
  q3.setFeedbackForCorrect(FormApp.createFeedback().setText("Верно! Флаг HttpOnly запрещает доступ к куки из клиентского JavaScript (document.cookie).").build());
  q3.setFeedbackForIncorrect(FormApp.createFeedback().setText("Неверно. LocalStorage уязвим к XSS. Стандарт безопасности — HttpOnly куки.").build());
  q3.setRequired(true);

  // Savol 4 (3 ball)
  var q4 = form.addMultipleChoiceItem();
  q4.setTitle("4. Почему директива 'USER node' (non-root) в Dockerfile является обязательным стандартом безопасности?");
  q4.setPoints(3);
  q4.setChoices([
    q4.createChoice("Чтобы при уязвимости RCE злоумышленник не получил права суперпользователя (root) на хост-системе", true),
    q4.createChoice("Для ускорения работы Node.js сервера в 2 раза", false),
    q4.createChoice("Для сжатия размера контейнера", false),
    q4.createChoice("Исключительно для возможности деплоя на Vercel или AWS", false)
  ]);
  q4.setFeedbackForCorrect(FormApp.createFeedback().setText("Верно! Принцип наименьших привилегий предотвращает побег из контейнера с root правами.").build());
  q4.setFeedbackForIncorrect(FormApp.createFeedback().setText("Неверно. Запуск под root создает критический риск захвата хоста. USER node ограничивает привилегии.").build());
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
 * Dars: 9-Sinf: 28-Dars Full-Stack Xavfsiz Servis va CTF — Oraliq Nazorat Kiber-Testi
 * Til / Language: EN
 */
function createGoogleForm_28_dars_fullstack_xavfsiz_servis_oraliq_nazorat_en() {
  // 1. Yangi Google Form yaratish va Quiz rejimini yoqish
  var form = FormApp.create("Grade 9: Lesson 28 Full-Stack Secure Service & CTF — Midterm Security Quiz");
  form.setDescription("Target International School // Grade 9 // Quarter 1 Midterm Exam\nTopic: Express MVC, SQLite Relational Schema, JWT, XSS/CSRF Defense & Docker Sandbox\nInstructor: M. Musulmonov");
  form.setIsQuiz(true);
  form.setRequireLogin(false);
  form.setCollectEmail(true);
  form.setShowLinkToRespondAgain(false);
  form.setProgressBar(true);
  form.setShuffleQuestions(false);

  // 2. O'quvchi ma'lumotlarini to'plash
  form.addTextItem().setTitle("Student Full Name").setRequired(true);
  form.addListItem().setTitle("Select your class:").setChoiceValues(["9-A", "9-B"]).setRequired(true);

  // Savol 1 (3 ball)
  var q1 = form.addMultipleChoiceItem();
  q1.setTitle("1. Which critical vulnerability exists in the following Express server snippet?\n\napp.post('/api/profile', (req, res) => {\n  const query = \"UPDATE users SET bio = '\" + req.body.bio + \"' WHERE id = \" + req.user.id;\n  db.run(query);\n  res.send('<h1>Updated:</h1><div>' + req.body.bio + '</div>');\n});");
  q1.setPoints(3);
  q1.setChoices([
    q1.createChoice("Critical vulnerability: simultaneous SQL Injection (string concatenation) and XSS (unsanitized HTML output)!", true),
    q1.createChoice("The code is completely secure because POST is used instead of GET.", false),
    q1.createChoice("The only flaw is the missing Content-Type header.", false),
    q1.createChoice("Only a memory leak (RAM exhaustion) will occur on the server.", false)
  ]);
  q1.setFeedbackForCorrect(FormApp.createFeedback().setText("Correct! String concatenation causes SQL Injection, and outputting unsanitized input via res.send() enables XSS.").build());
  q1.setFeedbackForIncorrect(FormApp.createFeedback().setText("Incorrect. Both SQL Injection and XSS are present. Parameterized queries (?) and sanitization via DOMPurify/res.json are required.").build());
  q1.setRequired(true);

  // Savol 2 (2 ball)
  var q2 = form.addMultipleChoiceItem();
  q2.setTitle("2. Why is a FOREIGN KEY constraint applied to the 'user_id' column of the 'orders' table in an SQLite relational database?");
  q2.setPoints(2);
  q2.setChoices([
    q2.createChoice("To guarantee that only existing users can place orders (Referential Integrity)", true),
    q2.createChoice("To automatically encrypt user passwords using SHA-256", false),
    q2.createChoice("To reduce database file size on disk by up to 50%", false),
    q2.createChoice("Exclusively to cache SELECT queries", false)
  ]);
  q2.setFeedbackForCorrect(FormApp.createFeedback().setText("Excellent! Foreign keys maintain referential integrity across related tables.").build());
  q2.setFeedbackForIncorrect(FormApp.createFeedback().setText("Incorrect. A foreign key enforces referential integrity across relational data.").build());
  q2.setRequired(true);

  // Savol 3 (2 ball)
  var q3 = form.addMultipleChoiceItem();
  q3.setTitle("3. Which storage mechanism is most secure for JWT tokens to prevent theft via XSS attacks?");
  q3.setPoints(2);
  q3.setChoices([
    q3.createChoice("Storing inside cookies with 'HttpOnly; Secure; SameSite=Strict' flags", true),
    q3.createChoice("Storing as plaintext inside browser LocalStorage", false),
    q3.createChoice("Passing token as a GET query parameter (?token=...)", false),
    q3.createChoice("Writing token into HTML data-* attributes", false)
  ]);
  q3.setFeedbackForCorrect(FormApp.createFeedback().setText("Correct! The HttpOnly flag prevents client-side JavaScript access via document.cookie.").build());
  q3.setFeedbackForIncorrect(FormApp.createFeedback().setText("Incorrect. LocalStorage is vulnerable to XSS. The industry standard is HttpOnly cookies.").build());
  q3.setRequired(true);

  // Savol 4 (3 ball)
  var q4 = form.addMultipleChoiceItem();
  q4.setTitle("4. Why is the 'USER node' (non-root) directive in a Dockerfile an essential security standard?");
  q4.setPoints(3);
  q4.setChoices([
    q4.createChoice("To prevent an attacker from gaining host superuser (root) privileges in the event of an RCE exploit", true),
    q4.createChoice("To increase Node.js server performance by 2x", false),
    q4.createChoice("To compress the container image size", false),
    q4.createChoice("Exclusively to enable deployment on Vercel or AWS", false)
  ]);
  q4.setFeedbackForCorrect(FormApp.createFeedback().setText("Correct! The Principle of Least Privilege prevents container escape attacks with root privileges.").build());
  q4.setFeedbackForIncorrect(FormApp.createFeedback().setText("Incorrect. Running containers as root creates container breakout risks. USER node limits privileges.").build());
  q4.setRequired(true);

  Logger.log("=========================================");
  Logger.log("✅ Google Form muvaffaqiyatli yaratildi!");
  Logger.log("📌 Form Nomi: " + form.getTitle());
  Logger.log("✏️ Tahrirlash havolasi (Edit URL): " + form.getEditUrl());
  Logger.log("🌐 O'quvchilarga tarqatish havolasi (Published URL): " + form.getPublishedUrl());
  Logger.log("=========================================");
}
