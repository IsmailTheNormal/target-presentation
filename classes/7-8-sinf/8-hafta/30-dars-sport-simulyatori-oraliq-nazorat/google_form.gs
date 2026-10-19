/**
 * Target International School — Google Forms Generator Script
 * Dars: 7–8-Sinf: 30-Dars Sport Simulyatori va O'yin Fizikasi — Oraliq Nazorat Testi
 * 
 * QO'LLANMA:
 * 1. https://script.new sahifasini oching.
 * 2. Ushbu fayl kodini to'liq nusxalab, script.new tahrirchisiga qo'ying.
 * 3. Tepada funksiyani tanlang (masalan, createGoogleForm_30_dars_sport_simulyatori_oraliq_nazorat_uz) va "Run" (▶️) tugmasini bosing.
 * 4. Google Drive ichingizda test avtomatik yaratiladi va konsolda havola chiqadi!
 */

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
 * Dars: 7–8-Sinf: 30-Dars Sport Simulyatori va O'yin Fizikasi — Oraliq Nazorat Testi
 * Til / Language: RU
 */
function createGoogleForm_30_dars_sport_simulyatori_oraliq_nazorat_ru() {
  // 1. Yangi Google Form yaratish va Quiz rejimini yoqish
  var form = FormApp.create("7–8-Класс: Урок 30 Спортивный Симулятор и Игровая Физика — Рубежный Тест");
  form.setDescription("Target International School // 7–8-Класс // Рубежный контроль 1-й четверти\nТема: Граф химии состава, движок симуляции матча (FSM), 2D физика и налог 5%\nУчитель: М. Мусульмонов");
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
  q1.setTitle("1. Каким образом рассчитывается общий рейтинг (OVR) футбольной карточки в симуляторе?");
  q1.setPoints(2);
  q1.setChoices([
    q1.createChoice("По взвешенной формуле, где ключевые для амплуа параметры имеют максимальный коэффициент", true),
    q1.createChoice("Простым средним арифметическим всех 6 параметров", false),
    q1.createChoice("Исключительно по росту и возрасту футболиста", false),
    q1.createChoice("Случайным числом через Math.random()", false)
  ]);
  q1.setFeedbackForCorrect(FormApp.createFeedback().setText("Верно! Для нападающего важны PAC и SHO, для защитника — DEF и PHY.").build());
  q1.setFeedbackForIncorrect(FormApp.createFeedback().setText("Неверно. OVR — это взвешенное среднее, зависимое от позиции игрока.").build());
  q1.setRequired(true);

  // Savol 2 (3 ball)
  var q2 = form.addMultipleChoiceItem();
  q2.setTitle("2. При каких условиях достигается максимальный показатель в 33 балла химии состава?");
  q2.setPoints(3);
  q2.setChoices([
    q2.createChoice("11 игроков на своих позициях с максимальными связями по клубу, лиге и национальности", true),
    q2.createChoice("Покупкой самых дорогих золотых карточек", false),
    q2.createChoice("Если все игроки одного года рождения", false),
    q2.createChoice("Если в составе оставить только форвардов", false)
  ]);
  q2.setFeedbackForCorrect(FormApp.createFeedback().setText("Отлично! 11 игроков дают максимум 3 звезды химии каждый, суммарно 33 очка.").build());
  q2.setFeedbackForIncorrect(FormApp.createFeedback().setText("Неверно. Химия не зависит от цены, важны связи клуба, лиги и страны.").build());
  q2.setRequired(true);

  // Savol 3 (3 ball)
  var q3 = form.addMultipleChoiceItem();
  q3.setTitle("3. Какой алгоритм используется в 2D физическом движке для определения столкновения мяча со штангой ворот?");
  q3.setPoints(3);
  q3.setChoices([
    q3.createChoice("AABB (Axis-Aligned Bounding Box) — пересечение ограничивающих прямоугольников", true),
    q3.createChoice("Первый закон Ньютона", false),
    q3.createChoice("Исключительно формула теоремы Пифагора", false),
    q3.createChoice("Сравнение CSS отступов", false)
  ]);
  q3.setFeedbackForCorrect(FormApp.createFeedback().setText("Верно! AABB быстро определяет коллизии через сравнение проекций на оси X и Y.").build());
  q3.setFeedbackForIncorrect(FormApp.createFeedback().setText("Неверно. Базовый алгоритм коллизий в 2D играх — AABB.").build());
  q3.setRequired(true);

  // Savol 4 (2 ball)
  var q4 = form.addMultipleChoiceItem();
  q4.setTitle("4. Какую экономическую функцию выполняет 5% налог с продаж (EA Tax) на виртуальном трансферном рынке?");
  q4.setPoints(2);
  q4.setChoices([
    q4.createChoice("Служит механизмом сжигания монет (Coin Sink) для борьбы с инфляцией и стабилизации цен", true),
    q4.createChoice("Для реального обогащения создателей игры", false),
    q4.createChoice("Для удаления случайных карточек", false),
    q4.createChoice("Для ускорения загрузки приложения", false)
  ]);
  q4.setFeedbackForCorrect(FormApp.createFeedback().setText("Отлично! Налог является монетарным регулятором (Coin Sink), сдерживающим денежную массу M2.").build());
  q4.setFeedbackForIncorrect(FormApp.createFeedback().setText("Неверно. 5% налог сжигает монеты для защиты от гиперинфляции.").build());
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
 * Til / Language: EN
 */
function createGoogleForm_30_dars_sport_simulyatori_oraliq_nazorat_en() {
  // 1. Yangi Google Form yaratish va Quiz rejimini yoqish
  var form = FormApp.create("Grades 7–8: Lesson 30 Sports Simulator & Game Physics — Midterm Exam");
  form.setDescription("Target International School // Grades 7–8 // Quarter 1 Midterm Exam\nTopic: Squad Chemistry Graphs, Match Engine FSM, 2D Collision Physics & EA 5% Tax\nInstructor: M. Musulmonov");
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
  q1.setTitle("1. How is the overall rating (OVR) of a player card calculated in the simulator?");
  q1.setPoints(2);
  q1.setChoices([
    q1.createChoice("Using a position-dependent weighted average formula where primary attributes carry higher coefficients", true),
    q1.createChoice("By taking the simple unweighted arithmetic mean of all 6 stats", false),
    q1.createChoice("Solely based on the player's physical height and age", false),
    q1.createChoice("By generating a random integer with Math.random()", false)
  ]);
  q1.setFeedbackForCorrect(FormApp.createFeedback().setText("Correct! Different positions weight stats according to positional relevance.").build());
  q1.setFeedbackForIncorrect(FormApp.createFeedback().setText("Incorrect. OVR is computed as a position-based weighted average.").build());
  q1.setRequired(true);

  // Savol 2 (3 ball)
  var q2 = form.addMultipleChoiceItem();
  q2.setTitle("2. Under which conditions is the maximum 33 chemistry score achieved in squad building?");
  q2.setPoints(3);
  q2.setChoices([
    q2.createChoice("All 11 players in their primary positions satisfying club, league, and national synergy thresholds", true),
    q2.createChoice("By purchasing only the most expensive gold cards on the transfer market", false),
    q2.createChoice("If all players share the identical birth year", false),
    q2.createChoice("If the lineup consists solely of attackers", false)
  ]);
  q2.setFeedbackForCorrect(FormApp.createFeedback().setText("Excellent! Each of the 11 positions can earn up to 3 stars, totaling 33 points.").build());
  q2.setFeedbackForIncorrect(FormApp.createFeedback().setText("Incorrect. Chemistry depends on relational graph synergy (club, league, nation).").build());
  q2.setRequired(true);

  // Savol 3 (3 ball)
  var q3 = form.addMultipleChoiceItem();
  q3.setTitle("3. Which algorithm is utilized in a 2D physics engine to detect ball collisions with the goal post?");
  q3.setPoints(3);
  q3.setChoices([
    q3.createChoice("AABB (Axis-Aligned Bounding Box) rectangular intersection testing", true),
    q3.createChoice("Newton's First Law of Motion", false),
    q3.createChoice("Exclusively the Pythagorean hypotenuse formula", false),
    q3.createChoice("Comparing CSS margin and padding properties", false)
  ]);
  q3.setFeedbackForCorrect(FormApp.createFeedback().setText("Correct! AABB detects overlaps efficiently along the X and Y coordinate axes.").build());
  q3.setFeedbackForIncorrect(FormApp.createFeedback().setText("Incorrect. The fundamental 2D collision algorithm is AABB.").build());
  q3.setRequired(true);

  // Savol 4 (2 ball)
  var q4 = form.addMultipleChoiceItem();
  q4.setTitle("4. What economic purpose does the 5% transaction tax (EA Tax) serve in a virtual transfer market?");
  q4.setPoints(2);
  q4.setChoices([
    q4.createChoice("Acts as a Coin Sink to drain excess currency from circulation, mitigating hyperinflation", true),
    q4.createChoice("To generate real cash revenue for developers", false),
    q4.createChoice("To randomly delete unused player cards", false),
    q4.createChoice("To speed up network application loading", false)
  ]);
  q4.setFeedbackForCorrect(FormApp.createFeedback().setText("Excellent! Taxes act as deflationary Coin Sinks counterbalancing continuous minting rewards.").build());
  q4.setFeedbackForIncorrect(FormApp.createFeedback().setText("Incorrect. The 5% tax is an essential monetary Coin Sink preventing hyperinflation.").build());
  q4.setRequired(true);

  Logger.log("=========================================");
  Logger.log("✅ Google Form muvaffaqiyatli yaratildi!");
  Logger.log("📌 Form Nomi: " + form.getTitle());
  Logger.log("✏️ Tahrirlash havolasi (Edit URL): " + form.getEditUrl());
  Logger.log("🌐 O'quvchilarga tarqatish havolasi (Published URL): " + form.getPublishedUrl());
  Logger.log("=========================================");
}
