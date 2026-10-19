/**
 * Target International School — Google Forms Generator Script
 * Dars: 5–6-Sinf: 22-Dars Kiber-Qalqon Viktorinasi — Oraliq Nazorat Testi
 * 
 * QO'LLANMA:
 * 1. https://script.new sahifasini oching.
 * 2. Ushbu fayl kodini to'liq nusxalab, script.new tahrirchisiga qo'ying.
 * 3. Tepada funksiyani tanlang (masalan, createGoogleForm_22_dars_kiber_qalqon_oraliq_nazorat_uz) va "Run" (▶️) tugmasini bosing.
 * 4. Google Drive ichingizda test avtomatik yaratiladi va konsolda havola chiqadi!
 */

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

/**
 * Target International School — Google Form Generator
 * Dars: 5–6-Sinf: 22-Dars Kiber-Qalqon Viktorinasi — Oraliq Nazorat Testi
 * Til / Language: RU
 */
function createGoogleForm_22_dars_kiber_qalqon_oraliq_nazorat_ru() {
  // 1. Yangi Google Form yaratish va Quiz rejimini yoqish
  var form = FormApp.create("5–6-Класс: Урок 22 Викторина Кибер-Щит — Рубежный Тест");
  form.setDescription("Target International School // 5–6-Класс // Викторина безопасности 1-й четверти\nТема: Надежные пароли, фишинг, троянские программы и цифровая приватность\nУчитель: М. Мусульмонов");
  form.setIsQuiz(true);
  form.setRequireLogin(false);
  form.setCollectEmail(true);
  form.setShowLinkToRespondAgain(false);
  form.setProgressBar(true);
  form.setShuffleQuestions(false);

  // 2. O'quvchi ma'lumotlarini to'plash
  form.addTextItem().setTitle("Ф.И.О. Учащегося").setRequired(true);
  form.addListItem().setTitle("Выберите ваш класс:").setChoiceValues(["5-A", "5-B", "6-A", "6-B"]).setRequired(true);

  // Savol 1 (2 ball)
  var q1 = form.addMultipleChoiceItem();
  q1.setTitle("1. По правилам кибербезопасности, как составляется наиболее стойкий пароль?");
  q1.setPoints(2);
  q1.setChoices([
    q1.createChoice("Не менее 14+ знаков, включая заглавные и строчные буквы, цифры и символы (#, $, !)", true),
    q1.createChoice("Имя и год рождения (например: ali2014)", false),
    q1.createChoice("Последовательность клавиш (12345678 или qwerty)", false),
    q1.createChoice("Простой 4-значный PIN-код", false)
  ]);
  q1.setFeedbackForCorrect(FormApp.createFeedback().setText("Молодец! Длинный сложный пароль из 14+ символов невозможно взломать брутфорсом.").build());
  q1.setFeedbackForIncorrect(FormApp.createFeedback().setText("Неверно. Простые пароли и даты взламываются мгновенно по словарю.").build());
  q1.setRequired(true);

  // Savol 2 (3 ball)
  var q2 = form.addMultipleChoiceItem();
  q2.setTitle("2. Что нужно сделать, если вы увидели ссылку 'Бесплатные 10,000 Robux или Telegram Premium, введите пароль'?");
  q2.setPoints(3);
  q2.setChoices([
    q2.createChoice("Немедленно закрыть страницу и ничего не вводить — это фишинговая ловушка мошенников!", true),
    q2.createChoice("Быстро ввести пароль и ждать приз", false),
    q2.createChoice("Переслать ссылку друзьям во все группы", false),
    q2.createChoice("Выключить монитор", false)
  ]);
  q2.setFeedbackForCorrect(FormApp.createFeedback().setText("Верно! Бесплатный сыр бывает только в мышеловке. Это фишинг для угона аккаунтов.").build());
  q2.setFeedbackForIncorrect(FormApp.createFeedback().setText("Неверно. Ввод данных на таких сайтах ведет к полной потере доступа к аккаунту.").build());
  q2.setRequired(true);

  // Savol 3 (3 ball)
  var q3 = form.addMultipleChoiceItem();
  q3.setTitle("3. Почему перед публикацией фото в интернет нужно стирать скрытые GPS (EXIF) метаданные?");
  q3.setPoints(3);
  q3.setChoices([
    q3.createChoice("Чтобы посторонние и злоумышленники не смогли вычислить точный адрес вашего дома или школы по карте", true),
    q3.createChoice("Чтобы сделать цвета фотографии ярче", false),
    q3.createChoice("Исключительно для экономии памяти смартфона", false),
    q3.createChoice("Чтобы фотография быстрее загружалась", false)
  ]);
  q3.setFeedbackForCorrect(FormApp.createFeedback().setText("Верно! Данные EXIF содержат точные координаты съемки. Их удаление защищает приватность.").build());
  q3.setFeedbackForIncorrect(FormApp.createFeedback().setText("Неверно. GPS метки раскрывают местоположение вашего дома.").build());
  q3.setRequired(true);

  // Savol 4 (2 ball)
  var q4 = form.addMultipleChoiceItem();
  q4.setTitle("4. Что означает 'Правило Большого Экрана' (Billboard Rule) безопасного поведения в интернете?");
  q4.setPoints(2);
  q4.setChoices([
    q4.createChoice("Никогда не выкладывать в интернет то, что вы постеснялись бы показать на огромном экране в центре города", true),
    q4.createChoice("Работать только за большим экраном", false),
    q4.createChoice("Писать сообщения только ЗАГЛАВНЫМИ БУКВАМИ", false),
    q4.createChoice("Ходить в кинотеатр на фильмы", false)
  ]);
  q4.setFeedbackForCorrect(FormApp.createFeedback().setText("Верно! Цифровой след остается навсегда. То, что попало в сеть, может стать доступно каждому.").build());
  q4.setFeedbackForIncorrect(FormApp.createFeedback().setText("Неверно. Правило учит осмотрительности при публикации личной информации.").build());
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
 * Til / Language: EN
 */
function createGoogleForm_22_dars_kiber_qalqon_oraliq_nazorat_en() {
  // 1. Yangi Google Form yaratish va Quiz rejimini yoqish
  var form = FormApp.create("Grades 5–6: Lesson 22 Cyber Shield Security Quiz — Midterm Exam");
  form.setDescription("Target International School // Grades 5–6 // Quarter 1 Security Quiz\nTopic: Strong Passwords, Phishing Detection, Trojan Defense & Digital Privacy\nInstructor: M. Musulmonov");
  form.setIsQuiz(true);
  form.setRequireLogin(false);
  form.setCollectEmail(true);
  form.setShowLinkToRespondAgain(false);
  form.setProgressBar(true);
  form.setShuffleQuestions(false);

  // 2. O'quvchi ma'lumotlarini to'plash
  form.addTextItem().setTitle("Student Full Name").setRequired(true);
  form.addListItem().setTitle("Select your class:").setChoiceValues(["5-A", "5-B", "6-A", "6-B"]).setRequired(true);

  // Savol 1 (2 ball)
  var q1 = form.addMultipleChoiceItem();
  q1.setTitle("1. According to cybersecurity rules, how is the strongest, uncrackable password formulated?");
  q1.setPoints(2);
  q1.setChoices([
    q1.createChoice("At least 14+ characters mixing uppercase, lowercase, numbers, and special symbols (#, $, !)", true),
    q1.createChoice("Personal name and birth year (e.g., ali2014)", false),
    q1.createChoice("Sequential keyboard characters (12345678 or qwerty)", false),
    q1.createChoice("A simple 4-digit numeric PIN", false)
  ]);
  q1.setFeedbackForCorrect(FormApp.createFeedback().setText("Well done! A 14+ character complex passphrase withstands brute-force attempts for centuries.").build());
  q1.setFeedbackForIncorrect(FormApp.createFeedback().setText("Incorrect. Names and sequential numbers are cracked within seconds via dictionary attacks.").build());
  q1.setRequired(true);

  // Savol 2 (3 ball)
  var q2 = form.addMultipleChoiceItem();
  q2.setTitle("2. What must you do if you encounter a link claiming 'Free 10,000 Robux or Telegram Premium, enter your password'?");
  q2.setPoints(3);
  q2.setChoices([
    q2.createChoice("Immediately close the webpage and never enter credentials — it is a phishing trap!", true),
    q2.createChoice("Quickly input account credentials and await the prize", false),
    q2.createChoice("Forward the link to all school chat groups", false),
    q2.createChoice("Turn off the computer screen", false)
  ]);
  q2.setFeedbackForCorrect(FormApp.createFeedback().setText("Correct! Free handouts are classic lures. This is credential phishing designed to steal accounts.").build());
  q2.setFeedbackForIncorrect(FormApp.createFeedback().setText("Incorrect. Submitting credentials on untrusted domains results in immediate account takeover.").build());
  q2.setRequired(true);

  // Savol 3 (3 ball)
  var q3 = form.addMultipleChoiceItem();
  q3.setTitle("3. Why should hidden GPS location (EXIF) metadata be stripped before publishing photos online?");
  q3.setPoints(3);
  q3.setChoices([
    q3.createChoice("To prevent strangers and adversaries from tracking your exact home or school coordinates on a map", true),
    q3.createChoice("To enhance photo colors and brightness", false),
    q3.createChoice("Solely to free up storage on the smartphone", false),
    q3.createChoice("To speed up image rendering", false)
  ]);
  q3.setFeedbackForCorrect(FormApp.createFeedback().setText("Correct! EXIF tags hold precise GPS coordinates. Removing them preserves physical safety and privacy.").build());
  q3.setFeedbackForIncorrect(FormApp.createFeedback().setText("Incorrect. GPS metadata discloses exact physical residential locations.").build());
  q3.setRequired(true);

  // Savol 4 (2 ball)
  var q4 = form.addMultipleChoiceItem();
  q4.setTitle("4. What does the 'Billboard Rule' teach about safe online conduct?");
  q4.setPoints(2);
  q4.setChoices([
    q4.createChoice("Never upload personal photos or data that you would feel uncomfortable displaying on a giant public billboard", true),
    q4.createChoice("Only using large desktop monitors", false),
    q4.createChoice("Writing chat messages strictly in ALL CAPS", false),
    q4.createChoice("Going to movie theaters regularly", false)
  ]);
  q4.setFeedbackForCorrect(FormApp.createFeedback().setText("Correct! The digital footprint lasts indefinitely. Treat all online postings as visible to the whole world.").build());
  q4.setFeedbackForIncorrect(FormApp.createFeedback().setText("Incorrect. The Billboard Rule cautions against uploading any material you wouldn't share publicly.").build());
  q4.setRequired(true);

  Logger.log("=========================================");
  Logger.log("✅ Google Form muvaffaqiyatli yaratildi!");
  Logger.log("📌 Form Nomi: " + form.getTitle());
  Logger.log("✏️ Tahrirlash havolasi (Edit URL): " + form.getEditUrl());
  Logger.log("🌐 O'quvchilarga tarqatish havolasi (Published URL): " + form.getPublishedUrl());
  Logger.log("=========================================");
}
