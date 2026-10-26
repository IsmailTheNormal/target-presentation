/**
 * Target International School — Google Forms Generator Script
 * Dars: 7–8-Sinf: 27-Dars Biometrik Kiber-Skaner: Yuz, Biometrika va Anti-Spoofing — Kiber-Test
 * 
 * QO'LLANMA:
 * 1. https://script.new sahifasini oching.
 * 2. Ushbu fayl kodini to'liq nusxalab, script.new tahrirchisiga qo'ying.
 * 3. Tepada funksiyani tanlang (masalan, createGoogleForm_27_dars_biometrik_kiber_skaner_yuz_va_anti_spoofing_uz) va "Run" (▶️) tugmasini bosing.
 * 4. Google Drive ichingizda test avtomatik yaratiladi va konsolda havola chiqadi!
 */

/**
 * Target International School — Google Form Generator
 * Dars: 7–8-Sinf: 27-Dars Biometrik Kiber-Skaner: Yuz, Biometrika va Anti-Spoofing — Kiber-Test
 * Til / Language: UZ
 */
function createGoogleForm_27_dars_biometrik_kiber_skaner_yuz_va_anti_spoofing_uz() {
  // 1. Yangi Google Form yaratish va Quiz rejimini yoqish
  var form = FormApp.create("7–8-Sinf: 27-Dars Biometrik Kiber-Skaner: Yuz, Biometrika va Anti-Spoofing — Kiber-Test");
  form.setDescription("Target International School // 7–8-Sinf // 7-Hafta // 27-Dars\nMavzu: 68 ta Tayanch Nuqta (Landmarks), IPD Masofasi, EAR Formulasi va Liveness Anti-Spoofing Himoyasi\nO'qituvchi: M. Musulmonov");
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
  q1.setTitle("1. Nega zamonaviy Face ID biometrik tizimlari insonning soch turmagi, soqoli yoki makiyajiga qaramay, 68 ta tayanch nuqta (Landmarks) ga tayanadi?");
  q1.setPoints(2);
  q1.setChoices([
    q1.createChoice("68 ta nuqta inson bosh suyagining o'zgarmas anatomiyasiga (ko'z kosalari, burun suyagi, jag') bog'langan bo'lib, soch o'zgarishiga bog'liq emas.", true),
    q1.createChoice("Smartfon kameralari rangli soch yoki lab bo'yog'ini ko'ra olmaydi.", false),
    q1.createChoice("Neyrotarmoqqa aslida 1000 ta nuqta kerak, 68 ta nuqta esa faqat batareyani tejash uchun olingan.", false)
  ]);
  q1.setFeedbackForCorrect(FormApp.createFeedback().setText("To'g'ri! Yuzdagi 68 nuqta bosh suyagi relyefini o'lchaydi. Ko'zlararo masofa (IPD) va suyaklar nisbati inson o'zgarganda ham barqaror qoladi.").build());
  q1.setFeedbackForIncorrect(FormApp.createFeedback().setText("Xato. Yuzning 68 nuqtasi soch yoki makiyajga emas, insonning o'zgarmas suyak tuzilishiga (anatomiyasiga) tayanadi.").build());
  q1.setRequired(true);

  // Savol 2 (3 ball)
  var q2 = form.addMultipleChoiceItem();
  q2.setTitle("2. Xaker hisob egasining 8K formatdagi yuqori sifatli fotosuratini qog'ozga chiqarib kameraga tutdi. Qaysi himoya texnologiyasi bu soxtalikni fosh etishi shart?");
  q2.setPoints(3);
  q2.setChoices([
    q2.createChoice("Kamera obyektivi tiniqligini 16K ga ko'tarish.", false),
    q2.createChoice("Liveness Detection (tirik insonni tekshirish: ko'z qisishi EAR, bosh burilishi Yaw va 3D relyef chuqurligi).", true),
    q2.createChoice("Foydalanuvchi hisobi parolini 32 ta belgiga uzaytirish.", false)
  ]);
  q2.setFeedbackForCorrect(FormApp.createFeedback().setText("To'g'ri! Kamera tiniqligi qog'ozdagi rasmni fosh qilolmaydi. Faqatgina Liveness Detection (ko'z miltillashi, mikropuls va 3D relyef) fotosuratni rad etadi.").build());
  q2.setFeedbackForIncorrect(FormApp.createFeedback().setText("Xato. Rasm qanchalik tiniq bo'lmasin, u tekis va jonsiz. Uni faqat Liveness Detection (tiriklik testi) fosh etadi.").build());
  q2.setRequired(true);

  // Savol 3 (3 ball)
  var q3 = form.addMultipleChoiceItem();
  q3.setTitle("3. Eye Aspect Ratio (EAR) formulasi qanday qilib insonning tabiiy ko'z qisganini (miltillaganini) matematik aniqlaydi?");
  q3.setPoints(3);
  q3.setChoices([
    q3.createChoice("Ochiq ko'zda EAR ≈ 0.32 bo'ladi; qovoqlar yumilganda vertikal masofa nolga yaqinlashib, EAR keskin 0.18 dan pastga tushadi.", true),
    q3.createChoice("EAR ko'z shox pardasining haroratini infraqizil o'lchaydi.", false),
    q3.createChoice("EAR ko'z holatidan qat'i nazar har doim doimiy 1.0 qiymatda turadi.", false)
  ]);
  q3.setFeedbackForCorrect(FormApp.createFeedback().setText("To'g'ri! Ko'z qisilganda EAR indeksi 0.32 dan 0.12 ga tushadi va tizim buni tabiiy biologik ritm (Liveness) deb qayd etadi.").build());
  q3.setFeedbackForIncorrect(FormApp.createFeedback().setText("Xato. EAR — bu ko'z balandligining kengligiga nisbati. Ko'z yumilganda u 0.18 dan pastga tushadi.").build());
  q3.setRequired(true);

  // Savol 4 (2 ball)
  var q4 = form.addMultipleChoiceItem();
  q4.setTitle("4. Apple TrueDepth tizimi qop-qorong'i xonada ham qanday qilib foydalanuvchi yuzini aniqlay oladi?");
  q4.setPoints(2);
  q4.setChoices([
    q4.createChoice("Telefon ekrani bir zumga maksimal yorug'likda oq rangda yonadi.", false),
    q4.createChoice("Mikrofon orqali tovush to'lqinlari bilan yuz shakli aks-sado qilinadi.", false),
    q4.createChoice("Dot Projector ko'zga ko'rinmas 30 000 ta infraqizil nuqta sochadi va infraqizil kamera yuzning 3D xaritasini o'qiydi.", true)
  ]);
  q4.setFeedbackForCorrect(FormApp.createFeedback().setText("To'g'ri! Apple Face ID xona chirog'iga qaramaydi. U o'zining 30 000 ta infraqizil lazer nuqtalari bilan qorong'ida ham mukammal 3D relyef oladi.").build());
  q4.setFeedbackForIncorrect(FormApp.createFeedback().setText("Xato. Face ID ekran chirog'i yoki mikrofonga emas, ko'rinmas 30 000 ta infraqizil nuqtalar to'riga tayanadi.").build());
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
 * Dars: 7–8-Sinf: 27-Dars Biometrik Kiber-Skaner: Yuz, Biometrika va Anti-Spoofing — Kiber-Test
 * Til / Language: RU
 */
function createGoogleForm_27_dars_biometrik_kiber_skaner_yuz_va_anti_spoofing_ru() {
  // 1. Yangi Google Form yaratish va Quiz rejimini yoqish
  var form = FormApp.create("7–8-Класс: Урок 27 Биометрический кибер-сканер лица и Anti-Spoofing — Тест");
  form.setDescription("Target International School // 7–8-Класс // 7-я Неделя // Урок 27\nТема: 68 опорных точек (Landmarks), расстояние IPD, формула моргания EAR и защита от спуфинга Liveness\nУчитель: М. Мусульмонов");
  form.setIsQuiz(true);
  form.setRequireLogin(false);
  form.setCollectEmail(true);
  form.setShowLinkToRespondAgain(false);
  form.setProgressBar(true);
  form.setShuffleQuestions(false);

  // 2. O'quvchi ma'lumotlarini to'plash
  form.addTextItem().setTitle("Ф.И.О. Учащегося").setRequired(true);
  form.addListItem().setTitle("Выберите ваш класс:").setChoiceValues(["7-A", "7-B", "8-A", "8-B"]).setRequired(true);

  // Savol 1 (2 ball)
  var q1 = form.addMultipleChoiceItem();
  q1.setTitle("1. Почему современные биометрические системы Face ID игнорируют прическу, бороду и макияж, фокусируясь на 68 опорных точках (Landmarks)?");
  q1.setPoints(2);
  q1.setChoices([
    q1.createChoice("68 точек привязаны к неизменяемой костной структуре черепа (глазницы, переносица, челюсть), которая индивидуальна и не меняется от стрижки.", true),
    q1.createChoice("Камеры смартфонов не умеют различать цветные волосы и помаду.", false),
    q1.createChoice("Нейросеть требует наличия ровно 1000 точек, а 68 точек используются только для экономии батареи.", false)
  ]);
  q1.setFeedbackForCorrect(FormApp.createFeedback().setText("Верно! 68 точек фиксируют анатомический рельеф черепа. Расстояние IPD и костная геометрия инвариантны к внешним изменениям.").build());
  q1.setFeedbackForIncorrect(FormApp.createFeedback().setText("Неверно. 68 точек опираются на неизменяемую костную структуру черепа человека.").build());
  q1.setRequired(true);

  // Savol 2 (3 ball)
  var q2 = form.addMultipleChoiceItem();
  q2.setTitle("2. Хакер распечатал сверхчеткое фото владельца устройства в разрешении 8K на бумаге и поднес к камере. Какая технология обязана заблокировать атаку?");
  q2.setPoints(3);
  q2.setChoices([
    q2.createChoice("Повышение разрешения объектива камеры до 16K.", false),
    q2.createChoice("Liveness Detection (проверка живого человека: моргание EAR, наклон головы Yaw и 3D-глубина рельефа).", true),
    q2.createChoice("Увеличение пароля учетной записи до 32 символов.", false)
  ]);
  q2.setFeedbackForCorrect(FormApp.createFeedback().setText("Верно! Четкость камеры лишь четче снимет бумагу. Только Liveness Detection отсекает плоские статические фото.").build());
  q2.setFeedbackForIncorrect(FormApp.createFeedback().setText("Неверно. Камера 16K не решает проблему плоскости. Необходим Liveness Detection.").build());
  q2.setRequired(true);

  // Savol 3 (3 ball)
  var q3 = form.addMultipleChoiceItem();
  q3.setTitle("3. Как формула Eye Aspect Ratio (EAR) математически фиксирует факт естественного моргания глазами?");
  q3.setPoints(3);
  q3.setChoices([
    q3.createChoice("При открытом глазе EAR ≈ 0.32; в момент закрытия век вертикальное расстояние падает до нуля, и EAR резко снижается ниже порога 0.18.", true),
    q3.createChoice("EAR измеряет температуру роговицы глаза в инфракрасном диапазоне.", false),
    q3.createChoice("EAR всегда остается постоянным числом 1.0 вне зависимости от положения глаз.", false)
  ]);
  q3.setFeedbackForCorrect(FormApp.createFeedback().setText("Верно! При моргании EAR падает с 0.32 ниже 0.18, подтверждая естественный биологический ритм живого человека.").build());
  q3.setFeedbackForIncorrect(FormApp.createFeedback().setText("Неверно. EAR — это отношение высоты глаза к ширине, падающее при моргании ниже 0.18.").build());
  q3.setRequired(true);

  // Savol 4 (2 ball)
  var q4 = form.addMultipleChoiceItem();
  q4.setTitle("4. Каким образом сенсор Apple TrueDepth распознает лицо владельца в абсолютной темноте?");
  q4.setPoints(2);
  q4.setChoices([
    q4.createChoice("Экран смартфона на мгновение вспыхивает максимальной белой яркостью.", false),
    q4.createChoice("Используется микрофон для эхолокации формы лица звуковыми волнами.", false),
    q4.createChoice("Инфракрасный проектор (Dot Projector) проецирует 30 000 невидимых глазу инфракрасных лучей, а IR-камера считывает 3D-рельеф.", true)
  ]);
  q4.setFeedbackForCorrect(FormApp.createFeedback().setText("Верно! TrueDepth использует собственный невидимый инфракрасный свет и 30 000 точек для построения 3D-рельефа.").build());
  q4.setFeedbackForIncorrect(FormApp.createFeedback().setText("Неверно. Face ID использует сетку из 30 000 инфракрасных точек (Dot Projector).").build());
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
 * Dars: 7–8-Sinf: 27-Dars Biometrik Kiber-Skaner: Yuz, Biometrika va Anti-Spoofing — Kiber-Test
 * Til / Language: EN
 */
function createGoogleForm_27_dars_biometrik_kiber_skaner_yuz_va_anti_spoofing_en() {
  // 1. Yangi Google Form yaratish va Quiz rejimini yoqish
  var form = FormApp.create("Grades 7–8: Lesson 27 Biometric Face Cyber-Scanner & Anti-Spoofing — Quiz");
  form.setDescription("Target International School // Grades 7–8 // Week 7 // Lesson 27\nTopic: 68 Facial Landmarks, IPD Calculation, EAR Blink Formula & Liveness Anti-Spoofing Defense\nInstructor: M. Musulmonov");
  form.setIsQuiz(true);
  form.setRequireLogin(false);
  form.setCollectEmail(true);
  form.setShowLinkToRespondAgain(false);
  form.setProgressBar(true);
  form.setShuffleQuestions(false);

  // 2. O'quvchi ma'lumotlarini to'plash
  form.addTextItem().setTitle("Student Full Name").setRequired(true);
  form.addListItem().setTitle("Select your class:").setChoiceValues(["7-A", "7-B", "8-A", "8-B"]).setRequired(true);

  // Savol 1 (2 ball)
  var q1 = form.addMultipleChoiceItem();
  q1.setTitle("1. Why do modern Face ID biometrics ignore hairstyles, beards, and makeup, focusing strictly on 68 facial landmark points?");
  q1.setPoints(2);
  q1.setChoices([
    q1.createChoice("68 landmarks bind to invariant skull bone geometry (eye sockets, nose bridge, jawline), which remains unique regardless of haircuts.", true),
    q1.createChoice("Smartphone cameras lack the ability to differentiate hair dye and lipsticks.", false),
    q1.createChoice("Neural nets require exactly 1,000 landmarks, using 68 solely to save battery.", false)
  ]);
  q1.setFeedbackForCorrect(FormApp.createFeedback().setText("Correct! 68 landmarks capture skull bone topography. IPD and facial bone ratios remain invariant over cosmetic alterations.").build());
  q1.setFeedbackForIncorrect(FormApp.createFeedback().setText("Incorrect. The 68 landmarks measure permanent skull bone structures, not temporary makeup.").build());
  q1.setRequired(true);

  // Savol 2 (3 ball)
  var q2 = form.addMultipleChoiceItem();
  q2.setTitle("2. An attacker prints an ultra-sharp 8K paper portrait of an owner and presents it to the camera. Which technology must intercept this attack?");
  q2.setPoints(3);
  q2.setChoices([
    q2.createChoice("Increasing camera lens resolution to 16K.", false),
    q2.createChoice("Liveness Detection (verifying a live human: EAR eye blinks, Yaw head turns, and 3D depth meshes).", true),
    q2.createChoice("Lengthening the user account password to 32 characters.", false)
  ]);
  q2.setFeedbackForCorrect(FormApp.createFeedback().setText("Correct! Lens resolution merely sharpens the paper print. Only Liveness Detection algorithms detect flat static spoofing.").build());
  q2.setFeedbackForIncorrect(FormApp.createFeedback().setText("Incorrect. High resolution doesn't fix flatness. Liveness Detection is mandatory.").build());
  q2.setRequired(true);

  // Savol 3 (3 ball)
  var q3 = form.addMultipleChoiceItem();
  q3.setTitle("3. How does the Eye Aspect Ratio (EAR) formula mathematically verify a natural eye blink?");
  q3.setPoints(3);
  q3.setChoices([
    q3.createChoice("With open eyes EAR ≈ 0.32; upon eyelid closure vertical distance drops near zero, causing EAR to plummet below 0.18 threshold.", true),
    q3.createChoice("EAR measures the infrared temperature of the corneal lens.", false),
    q3.createChoice("EAR always remains a constant 1.0 regardless of eye states.", false)
  ]);
  q3.setFeedbackForCorrect(FormApp.createFeedback().setText("Correct! Blinking causes EAR to dip from 0.32 below 0.18, confirming authentic living human physiology.").build());
  q3.setFeedbackForIncorrect(FormApp.createFeedback().setText("Incorrect. EAR is vertical eye height divided by width, dipping sharply below 0.18 during a blink.").build());
  q3.setRequired(true);

  // Savol 4 (2 ball)
  var q4 = form.addMultipleChoiceItem();
  q4.setTitle("4. How does the Apple TrueDepth sensor recognize an owner's face in absolute pitch darkness?");
  q4.setPoints(2);
  q4.setChoices([
    q4.createChoice("The phone screen flashes at maximum white luminance for a second.", false),
    q4.createChoice("Microphones emit ultrasound waves to echolocate facial geometry.", false),
    q4.createChoice("An infrared Dot Projector beams 30,000 invisible IR micro-dots, while an IR camera captures the 3D relief mesh.", true)
  ]);
  q4.setFeedbackForCorrect(FormApp.createFeedback().setText("Correct! TrueDepth relies on its dedicated invisible IR dot projector and IR camera, unaffected by ambient light.").build());
  q4.setFeedbackForIncorrect(FormApp.createFeedback().setText("Incorrect. Face ID operates via 30,000 structured invisible infrared dots.").build());
  q4.setRequired(true);

  Logger.log("=========================================");
  Logger.log("✅ Google Form muvaffaqiyatli yaratildi!");
  Logger.log("📌 Form Nomi: " + form.getTitle());
  Logger.log("✏️ Tahrirlash havolasi (Edit URL): " + form.getEditUrl());
  Logger.log("🌐 O'quvchilarga tarqatish havolasi (Published URL): " + form.getPublishedUrl());
  Logger.log("=========================================");
}
