/**
 * Target International School — Google Forms Generator Script
 * Dars: 7–8-Sinf: 27-Dars GPS Navigatsiya va Eng Qisqa Yo'l Algoritmi — Kiber-Test
 * 
 * QO'LLANMA:
 * 1. https://script.new sahifasini oching.
 * 2. Ushbu fayl kodini to'liq nusxalab, script.new tahrirchisiga qo'ying.
 * 3. Tepada funksiyani tanlang (masalan, createGoogleForm_27_dars_gps_navigatsiya_va_eng_qisqa_yol_uz) va "Run" (▶️) tugmasini bosing.
 * 4. Google Drive ichingizda test avtomatik yaratiladi va konsolda havola chiqadi!
 */

/**
 * Target International School — Google Form Generator
 * Dars: 7–8-Sinf: 27-Dars GPS Navigatsiya va Eng Qisqa Yo'l Algoritmi — Kiber-Test
 * Til / Language: UZ
 */
function createGoogleForm_27_dars_gps_navigatsiya_va_eng_qisqa_yol_uz() {
  // 1. Yangi Google Form yaratish va Quiz rejimini yoqish
  var form = FormApp.create("7–8-Sinf: 27-Dars GPS Navigatsiya va Eng Qisqa Yo'l Algoritmi — Kiber-Test");
  form.setDescription("Target International School // 7–8-Sinf // 7-Hafta // 27-Dars\nMavzu: Graf Tuzilmasi, Dijkstra va A* Algoritmlari, Haversine formulasi va W3C Geolocation API\nO'qituvchi: M. Musulmonov");
  form.setIsQuiz(true);
  form.setRequireLogin(false);
  form.setCollectEmail(true);
  form.setShowLinkToRespondAgain(false);
  form.setProgressBar(true);
  form.setShuffleQuestions(false);

  // 2. O'quvchi ma'lumotlarini to'plash
  form.addTextItem().setTitle("O'quvchining F.I.Sh. (Familiya, Ism)").setRequired(true);
  form.addListItem().setTitle("Sinfingizni tanlang:").setChoiceValues(["7-A", "7-B", "8-A", "8-B"]).setRequired(true);

  // Savol 1 (3 ball)
  var q1 = form.addMultipleChoiceItem();
  q1.setTitle("1. Google Maps yoki Yandex Go xaritasida shahar ko'chalari va chorrahalari qaysi ma'lumotlar tuzilmasi (Data Structure) yordamida dasturlanadi?");
  q1.setPoints(3);
  q1.setChoices([
    q1.createChoice("Vaznli yo'naltirilgan Graf (Weighted Directed Graph): chorrahalar — tugunlar (Vertices), ko'chalar — qirralar (Edges), masofa/tirbandlik — vaznlar (Weights).", true),
    q1.createChoice("Faqat bitta oddiy 1-o'lchamli massiv (Array).", false),
    q1.createChoice("Oddiy matnli satr (String).", false),
    q1.createChoice("Faqat HTML jadvali (Table).", false)
  ]);
  q1.setFeedbackForCorrect(FormApp.createFeedback().setText("Ofarin! Graf nazariyasi navigatsiya tizimlarining yuragi hisoblanadi.").build());
  q1.setFeedbackForIncorrect(FormApp.createFeedback().setText("Xato. Shahar navigatsiyasi vaznli yo'naltirilgan Graf orqali hisoblanadi.").build());
  q1.setRequired(true);

  // Savol 2 (3 ball)
  var q2 = form.addMultipleChoiceItem();
  q2.setTitle("2. Ikki nuqta orasidagi eng kam vaqt yoki eng qisqa masofani topishda qaysi mashhur kompyuter algoritmidan foydalaniladi?");
  q2.setPoints(3);
  q2.setChoices([
    q2.createChoice("Dijkstra (Deykstra) va A* (A-Star) eng qisqa yo'l algoritmlari.", true),
    q2.createChoice("Bubble Sort (Pufakchali saralash).", false),
    q2.createChoice("Binary Search (ikkilik qidiruv).", false),
    q2.createChoice("Math.random() orqali tasodifiy yo'l tanlash.", false)
  ]);
  q2.setFeedbackForCorrect(FormApp.createFeedback().setText("To'g'ri! Dijkstra algoritmi boshlang'ich nuqtadan barcha tugunlargacha bo'lgan optimal yo'lni aniqlaydi.").build());
  q2.setFeedbackForIncorrect(FormApp.createFeedback().setText("Xato. Eng qisqa yo'lni topish Dijkstra yoki A* algoritmi yordamida hisoblanadi.").build());
  q2.setRequired(true);

  // Savol 3 (2 ball)
  var q3 = form.addMultipleChoiceItem();
  q3.setTitle("3. Yer sferik yuzasida ikki GPS koordinata (kenglik va uzunlik) orasidagi aniq masofani hisoblash formulasi nima deb ataladi?");
  q3.setPoints(2);
  q3.setChoices([
    q3.createChoice("Haversine (Gaversinus) formulasi — yer egriligini hisobga olgan holda to'g'ri chiziqli masofani beradi.", true),
    q3.createChoice("Oddiy Pifagor teoremasi (a² + b² = c²) yer yuzida har doim 100% aniq ishlaydi.", false),
    q3.createChoice("Nyutonning butun olam tortishish qonuni.", false),
    q3.createChoice("Eynshteynning E=mc² formulasi.", false)
  ]);
  q3.setFeedbackForCorrect(FormApp.createFeedback().setText("To'g'ri! Yer shar shaklida bo'lgani sababli GPS masofalari Haversine formulasi bilan hisoblanadi.").build());
  q3.setFeedbackForIncorrect(FormApp.createFeedback().setText("Xato. Yer sferasidagi GPS masofasi Haversine formulasi orqali topiladi.").build());
  q3.setRequired(true);

  // Savol 4 (2 ball)
  var q4 = form.addMultipleChoiceItem();
  q4.setTitle("4. Zamonaviy veb-brauzerda foydalanuvchining joriy GPS kenglik va uzunlik koordinatalarini olish uchun qaysi standart API chaqiriladi?");
  q4.setPoints(2);
  q4.setChoices([
    q4.createChoice("navigator.geolocation.getCurrentPosition()", true),
    q4.createChoice("document.getElementById('gps').click()", false),
    q4.createChoice("window.localStorage.getItem('latitude')", false),
    q4.createChoice("console.log(process.env.GPS_COORDINATES)", false)
  ]);
  q4.setFeedbackForCorrect(FormApp.createFeedback().setText("To'g'ri! W3C standarti bo'yicha Geolocation API navigator.geolocation orqali ishlaydi.").build());
  q4.setFeedbackForIncorrect(FormApp.createFeedback().setText("Xato. Geolokatsiya olish navigator.geolocation.getCurrentPosition() orqali bajariladi.").build());
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
 * Dars: 7–8-Sinf: 27-Dars GPS Navigatsiya va Eng Qisqa Yo'l Algoritmi — Kiber-Test
 * Til / Language: RU
 */
function createGoogleForm_27_dars_gps_navigatsiya_va_eng_qisqa_yol_ru() {
  // 1. Yangi Google Form yaratish va Quiz rejimini yoqish
  var form = FormApp.create("7–8-Класс: Урок 27 GPS Навигация и Алгоритм Кратчайшего Пути — Тест");
  form.setDescription("Target International School // 7–8-Класс // 7-я Неделя // Урок 27\nТема: Структуры графов, алгоритмы Дейкстры и A*, формула Гаверсинуса и W3C Geolocation API\nУчитель: М. Мусульмонов");
  form.setIsQuiz(true);
  form.setRequireLogin(false);
  form.setCollectEmail(true);
  form.setShowLinkToRespondAgain(false);
  form.setProgressBar(true);
  form.setShuffleQuestions(false);

  // 2. O'quvchi ma'lumotlarini to'plash
  form.addTextItem().setTitle("Ф.И.О. Учащегося").setRequired(true);
  form.addListItem().setTitle("Выберите ваш класс:").setChoiceValues(["7-A", "7-B", "8-A", "8-B"]).setRequired(true);

  // Savol 1 (3 ball)
  var q1 = form.addMultipleChoiceItem();
  q1.setTitle("1. С помощью какой структуры данных программируются улицы и перекрестки в Google Maps или Yandex Go?");
  q1.setPoints(3);
  q1.setChoices([
    q1.createChoice("Взвешенный ориентированный Граф: перекрестки — вершины (Vertices), дороги — ребра (Edges), время/пробки — веса (Weights).", true),
    q1.createChoice("Обычный одномерный массив (Array).", false),
    q1.createChoice("Обычная строковая переменная (String).", false),
    q1.createChoice("Обычная HTML-таблица без логических связей.", false)
  ]);
  q1.setFeedbackForCorrect(FormApp.createFeedback().setText("Отлично! Теория графов лежит в основе всех мировых систем навигации.").build());
  q1.setFeedbackForIncorrect(FormApp.createFeedback().setText("Неверно. Карта дорог моделируется в виде взвешенного графа.").build());
  q1.setRequired(true);

  // Savol 2 (3 ball)
  var q2 = form.addMultipleChoiceItem();
  q2.setTitle("2. Какой знаменитый алгоритм используется для поиска быстрейшего или кратчайшего пути между двумя точками графа?");
  q2.setPoints(3);
  q2.setChoices([
    q2.createChoice("Алгоритмы Дейкстры (Dijkstra) и A* (A-Star).", true),
    q2.createChoice("Пузырьковая сортировка (Bubble Sort).", false),
    q2.createChoice("Бинарный поиск в массиве чисел.", false),
    q2.createChoice("Случайный выбор маршрута через Math.random().", false)
  ]);
  q2.setFeedbackForCorrect(FormApp.createFeedback().setText("Верно! Алгоритм Дейкстры математически гарантирует нахождение кратчайшего пути.").build());
  q2.setFeedbackForIncorrect(FormApp.createFeedback().setText("Неверно. Кратчайший путь рассчитывается алгоритмом Дейкстры или A*.").build());
  q2.setRequired(true);

  // Savol 3 (2 ball)
  var q3 = form.addMultipleChoiceItem();
  q3.setTitle("3. Как называется математическая формула для вычисления расстояния между двумя GPS координатами на сфере Земли?");
  q3.setPoints(2);
  q3.setChoices([
    q3.createChoice("Формула Гаверсинуса (Haversine) — учитывает сферическую кривизну Земли.", true),
    q3.createChoice("Обычная теорема Пифагора на плоской плоскости без погрешностей.", false),
    q3.createChoice("Закон всемирного тяготения Ньютона.", false),
    q3.createChoice("Формула теории относительности Эйнштейна.", false)
  ]);
  q3.setFeedbackForCorrect(FormApp.createFeedback().setText("Верно! Из-за сферической формы Земли точное расстояние рассчитывается по формуле Гаверсинуса.").build());
  q3.setFeedbackForIncorrect(FormApp.createFeedback().setText("Неверно. Расстояние между GPS точками рассчитывается по формуле Гаверсинуса.").build());
  q3.setRequired(true);

  // Savol 4 (2 ball)
  var q4 = form.addMultipleChoiceItem();
  q4.setTitle("4. Какой стандартный браузерный API используется для получения текущих GPS координат пользователя?");
  q4.setPoints(2);
  q4.setChoices([
    q4.createChoice("navigator.geolocation.getCurrentPosition()", true),
    q4.createChoice("document.getElementById('gps').click()", false),
    q4.createChoice("window.localStorage.getItem('latitude')", false),
    q4.createChoice("console.log(process.env.GPS_COORDINATES)", false)
  ]);
  q4.setFeedbackForCorrect(FormApp.createFeedback().setText("Верно! Доступ к геолокации в браузере осуществляется через navigator.geolocation.").build());
  q4.setFeedbackForIncorrect(FormApp.createFeedback().setText("Неверно. Стандартный метод геолокации — navigator.geolocation.getCurrentPosition().").build());
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
 * Dars: 7–8-Sinf: 27-Dars GPS Navigatsiya va Eng Qisqa Yo'l Algoritmi — Kiber-Test
 * Til / Language: EN
 */
function createGoogleForm_27_dars_gps_navigatsiya_va_eng_qisqa_yol_en() {
  // 1. Yangi Google Form yaratish va Quiz rejimini yoqish
  var form = FormApp.create("Grades 7–8: Lesson 27 GPS Navigation & Shortest Path Algorithm — Quiz");
  form.setDescription("Target International School // Grades 7–8 // Week 7 // Lesson 27\nTopic: Graph Structures, Dijkstra & A* Algorithms, Haversine Distance & W3C Geolocation API\nInstructor: M. Musulmonov");
  form.setIsQuiz(true);
  form.setRequireLogin(false);
  form.setCollectEmail(true);
  form.setShowLinkToRespondAgain(false);
  form.setProgressBar(true);
  form.setShuffleQuestions(false);

  // 2. O'quvchi ma'lumotlarini to'plash
  form.addTextItem().setTitle("Student Full Name").setRequired(true);
  form.addListItem().setTitle("Select your class:").setChoiceValues(["7-A", "7-B", "8-A", "8-B"]).setRequired(true);

  // Savol 1 (3 ball)
  var q1 = form.addMultipleChoiceItem();
  q1.setTitle("1. Which fundamental Data Structure models street networks and intersections in navigation systems like Google Maps?");
  q1.setPoints(3);
  q1.setChoices([
    q1.createChoice("Weighted Directed Graph: intersections as vertices, streets as edges, travel distance/traffic as weights.", true),
    q1.createChoice("A simple flat 1-dimensional array.", false),
    q1.createChoice("A single continuous string scalar.", false),
    q1.createChoice("An unstructured HTML table tag.", false)
  ]);
  q1.setFeedbackForCorrect(FormApp.createFeedback().setText("Bravo! Graph structures power global navigation engines.").build());
  q1.setFeedbackForIncorrect(FormApp.createFeedback().setText("Incorrect. Road networks are structured as weighted graphs.").build());
  q1.setRequired(true);

  // Savol 2 (3 ball)
  var q2 = form.addMultipleChoiceItem();
  q2.setTitle("2. Which foundational computer algorithm discovers the optimal or shortest path between two graph nodes?");
  q2.setPoints(3);
  q2.setChoices([
    q2.createChoice("Dijkstra's shortest path and A* heuristic search algorithms.", true),
    q2.createChoice("Bubble Sort sorting algorithm.", false),
    q2.createChoice("Binary Search on sorted lists.", false),
    q2.createChoice("Stochastic random path picking via Math.random().", false)
  ]);
  q2.setFeedbackForCorrect(FormApp.createFeedback().setText("Correct! Dijkstra's algorithm mathematically guarantees optimal path traversal.").build());
  q2.setFeedbackForIncorrect(FormApp.createFeedback().setText("Incorrect. Shortest route discovery relies on Dijkstra or A*.").build());
  q2.setRequired(true);

  // Savol 3 (2 ball)
  var q3 = form.addMultipleChoiceItem();
  q3.setTitle("3. What is the mathematical formula determining great-circle distance between two GPS coordinates across Earth's sphere?");
  q3.setPoints(2);
  q3.setChoices([
    q3.createChoice("Haversine formula — accurately incorporates Earth's spherical curvature.", true),
    q3.createChoice("Simple planar Pythagorean theorem without any curvature adjustment.", false),
    q3.createChoice("Newton's universal law of gravitation.", false),
    q3.createChoice("Einstein's mass-energy equivalence equation.", false)
  ]);
  q3.setFeedbackForCorrect(FormApp.createFeedback().setText("Correct! Earth's spherical geometry necessitates the Haversine formula for exact distance.").build());
  q3.setFeedbackForIncorrect(FormApp.createFeedback().setText("Incorrect. GPS spherical distance calculation requires the Haversine formula.").build());
  q3.setRequired(true);

  // Savol 4 (2 ball)
  var q4 = form.addMultipleChoiceItem();
  q4.setTitle("4. Which browser standard API retrieves the user's live GPS geographic coordinates?");
  q4.setPoints(2);
  q4.setChoices([
    q4.createChoice("navigator.geolocation.getCurrentPosition()", true),
    q4.createChoice("document.getElementById('gps').click()", false),
    q4.createChoice("window.localStorage.getItem('latitude')", false),
    q4.createChoice("console.log(process.env.GPS_COORDINATES)", false)
  ]);
  q4.setFeedbackForCorrect(FormApp.createFeedback().setText("Correct! Browser GPS access is implemented via navigator.geolocation.").build());
  q4.setFeedbackForIncorrect(FormApp.createFeedback().setText("Incorrect. Standard geolocation access requires navigator.geolocation.getCurrentPosition().").build());
  q4.setRequired(true);

  Logger.log("=========================================");
  Logger.log("✅ Google Form muvaffaqiyatli yaratildi!");
  Logger.log("📌 Form Nomi: " + form.getTitle());
  Logger.log("✏️ Tahrirlash havolasi (Edit URL): " + form.getEditUrl());
  Logger.log("🌐 O'quvchilarga tarqatish havolasi (Published URL): " + form.getPublishedUrl());
  Logger.log("=========================================");
}
