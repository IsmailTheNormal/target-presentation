/**
 * Target International School — Google Forms Generator Script
 * Dars: 10–11-Sinf: 32-Dars Korporativ Tarmoq Himoyasi va CTF — Oraliq Nazorat Kiber-Testi
 * 
 * QO'LLANMA:
 * 1. https://script.new sahifasini oching.
 * 2. Ushbu fayl kodini to'liq nusxalab, script.new tahrirchisiga qo'ying.
 * 3. Tepada funksiyani tanlang (masalan, createGoogleForm_32_dars_korporativ_himoya_va_ctf_uz) va "Run" (▶️) tugmasini bosing.
 * 4. Google Drive ichingizda test avtomatik yaratiladi va konsolda havola chiqadi!
 */

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
 * Dars: 10–11-Sinf: 32-Dars Korporativ Tarmoq Himoyasi va CTF — Oraliq Nazorat Kiber-Testi
 * Til / Language: RU
 */
function createGoogleForm_32_dars_korporativ_himoya_va_ctf_ru() {
  // 1. Yangi Google Form yaratish va Quiz rejimini yoqish
  var form = FormApp.create("10–11-Класс: Урок 32 Защита Корпоративной Сети и CTF — Рубежный Контроль");
  form.setDescription("Target International School // 10–11-Класс // Рубежный контроль 1-й четверти\nТема: NIST SP 800-61, Blue Team мониторинг, Red Team атаки, расчет MTTR\nУчитель: М. Мусульмонов");
  form.setIsQuiz(true);
  form.setRequireLogin(false);
  form.setCollectEmail(true);
  form.setShowLinkToRespondAgain(false);
  form.setProgressBar(true);
  form.setShuffleQuestions(false);

  // 2. O'quvchi ma'lumotlarini to'plash
  form.addTextItem().setTitle("Ф.И.О. Учащегося").setRequired(true);
  form.addListItem().setTitle("Выберите ваш класс:").setChoiceValues(["10-A", "10-B", "11-A", "11-B"]).setRequired(true);

  // Savol 1 (2 ball)
  var q1 = form.addMultipleChoiceItem();
  q1.setTitle("1. Какова правильная последовательность жизненного цикла инцидента по стандарту NIST SP 800-61?");
  q1.setPoints(2);
  q1.setChoices([
    q1.createChoice("1. Подготовка -> 2. Обнаружение и анализ -> 3. Сдерживание и ликвидация -> 4. Постинцидентный анализ", true),
    q1.createChoice("1. Атака -> 2. Выводы -> 3. Отключение сервера -> 4. Смена паролей", false),
    q1.createChoice("1. Сканирование -> 2. Брутфорс -> 3. Открытие портов -> 4. Отчет", false),
    q1.createChoice("1. Установка фаервола -> 2. Ожидание -> 3. Резервное копирование", false)
  ]);
  q1.setFeedbackForCorrect(FormApp.createFeedback().setText("Верно! NIST SP 800-61 определяет 4 ключевых этапа управления инцидентами.").build());
  q1.setFeedbackForIncorrect(FormApp.createFeedback().setText("Неверно. Правильный цикл: Подготовка -> Обнаружение -> Сдерживание -> Постинцидентный анализ.").build());
  q1.setRequired(true);

  // Savol 2 (3 ball)
  var q2 = form.addMultipleChoiceItem();
  q2.setTitle("2. Какие команды UFW должен применить инженер Blue Team для настройки периметра по принципу 'Default Deny'?");
  q2.setPoints(3);
  q2.setChoices([
    q2.createChoice("ufw default deny incoming && ufw allow 2222/tcp && ufw enable", true),
    q2.createChoice("ufw allow all incoming && ufw default allow", false),
    q2.createChoice("ufw disable && iptables -F", false),
    q2.createChoice("ufw reject outgoing && ufw allow 80/tcp", false)
  ]);
  q2.setFeedbackForCorrect(FormApp.createFeedback().setText("Верно! Default Deny блокирует весь входящий трафик, пропуская лишь назначенный защищенный порт SSH.").build());
  q2.setFeedbackForIncorrect(FormApp.createFeedback().setText("Неверно. Защита периметра требует запрета всего входящего трафика по умолчанию.").build());
  q2.setRequired(true);

  // Savol 3 (3 ball)
  var q3 = form.addMultipleChoiceItem();
  q3.setTitle("3. Как определяются метрики MTTR (Mean Time to Remediate) и MTTD (Mean Time to Detect) в SOC центрах?");
  q3.setPoints(3);
  q3.setChoices([
    q3.createChoice("MTTD — среднее время обнаружения атаки; MTTR — среднее время полной ликвидации последствий", true),
    q3.createChoice("MTTR — тактовая частота процессора; MTTD — пропускная способность сети", false),
    q3.createChoice("MTTD — годы присутствия хакера в сети; MTTR — число таблиц базы данных", false),
    q3.createChoice("Эти метрики относятся только к ОС Windows", false)
  ]);
  q3.setFeedbackForCorrect(FormApp.createFeedback().setText("Отлично! Минимизация MTTR и MTTD — главная цель эффективного SOC центра.").build());
  q3.setFeedbackForIncorrect(FormApp.createFeedback().setText("Неверно. MTTD измеряет время детекции, MTTR — время восстановления.").build());
  q3.setRequired(true);

  // Savol 4 (2 ball)
  var q4 = form.addMultipleChoiceItem();
  q4.setTitle("4. В чем заключается главная цель эксплойта в кибер-турнире CTF (Capture The Flag)?");
  q4.setPoints(2);
  q4.setChoices([
    q4.createChoice("Использовать уязвимость для доступа к закрытой системе и извлечения секретного флага (TARGET{...})", true),
    q4.createChoice("Уничтожить данные и сломать сервер", false),
    q4.createChoice("Просто изменить дизайн школьного сайта", false),
    q4.createChoice("Обновить базы антивируса", false)
  ]);
  q4.setFeedbackForCorrect(FormApp.createFeedback().setText("Верно! В этичном хакинге и CTF цель — валидировать уязвимость через захват флага без деструктивных действий.").build());
  q4.setFeedbackForIncorrect(FormApp.createFeedback().setText("Неверно. Цель CTF — нахождение флага для валидации навыка.").build());
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
 * Til / Language: EN
 */
function createGoogleForm_32_dars_korporativ_himoya_va_ctf_en() {
  // 1. Yangi Google Form yaratish va Quiz rejimini yoqish
  var form = FormApp.create("Grades 10–11: Lesson 32 Enterprise Network Defense & CTF — Midterm Exam");
  form.setDescription("Target International School // Grades 10–11 // Quarter 1 Midterm Exam\nTopic: NIST SP 800-61 Incident Lifecycle, Blue Team Hardening, Red Team Exploitation, MTTR\nInstructor: M. Musulmonov");
  form.setIsQuiz(true);
  form.setRequireLogin(false);
  form.setCollectEmail(true);
  form.setShowLinkToRespondAgain(false);
  form.setProgressBar(true);
  form.setShuffleQuestions(false);

  // 2. O'quvchi ma'lumotlarini to'plash
  form.addTextItem().setTitle("Student Full Name").setRequired(true);
  form.addListItem().setTitle("Select your class:").setChoiceValues(["10-A", "10-B", "11-A", "11-B"]).setRequired(true);

  // Savol 1 (2 ball)
  var q1 = form.addMultipleChoiceItem();
  q1.setTitle("1. What is the correct incident response lifecycle sequence according to NIST SP 800-61?");
  q1.setPoints(2);
  q1.setChoices([
    q1.createChoice("1. Preparation -> 2. Detection & Analysis -> 3. Containment, Eradication & Recovery -> 4. Post-Incident Activity", true),
    q1.createChoice("1. Exploitation -> 2. Conclusion -> 3. Server Shutdown -> 4. Password Reset", false),
    q1.createChoice("1. Scanning -> 2. Brute-Force -> 3. Port Opening -> 4. Reporting", false),
    q1.createChoice("1. Firewall Install -> 2. Idle -> 3. Backup", false)
  ]);
  q1.setFeedbackForCorrect(FormApp.createFeedback().setText("Correct! NIST SP 800-61 establishes the 4 essential phases of enterprise incident handling.").build());
  q1.setFeedbackForIncorrect(FormApp.createFeedback().setText("Incorrect. The standardized sequence is: Preparation -> Detection -> Containment -> Post-Incident.").build());
  q1.setRequired(true);

  // Savol 2 (3 ball)
  var q2 = form.addMultipleChoiceItem();
  q2.setTitle("2. Which UFW commands must a Blue Team engineer execute to enforce a 'Default Deny' perimeter on Linux?");
  q2.setPoints(3);
  q2.setChoices([
    q2.createChoice("ufw default deny incoming && ufw allow 2222/tcp && ufw enable", true),
    q2.createChoice("ufw allow all incoming && ufw default allow", false),
    q2.createChoice("ufw disable && iptables -F", false),
    q2.createChoice("ufw reject outgoing && ufw allow 80/tcp", false)
  ]);
  q2.setFeedbackForCorrect(FormApp.createFeedback().setText("Correct! Default Deny closes all inbound vectors, opening only explicitly designated ports.").build());
  q2.setFeedbackForIncorrect(FormApp.createFeedback().setText("Incorrect. Perimeter defense requires a default-deny ingress policy.").build());
  q2.setRequired(true);

  // Savol 3 (3 ball)
  var q3 = form.addMultipleChoiceItem();
  q3.setTitle("3. How are MTTR (Mean Time to Remediate) and MTTD (Mean Time to Detect) metrics defined in SOC management?");
  q3.setPoints(3);
  q3.setChoices([
    q3.createChoice("MTTD is average time to detect an intrusion; MTTR is average time to fully remediate the incident", true),
    q3.createChoice("MTTR is processor clock rate; MTTD is network bandwidth", false),
    q3.createChoice("MTTD is total dwell time in years; MTTR is number of database tables", false),
    q3.createChoice("These metrics only apply to Windows operating systems", false)
  ]);
  q3.setFeedbackForCorrect(FormApp.createFeedback().setText("Excellent! Minimizing MTTR and MTTD represents the primary objective of modern SOC operations.").build());
  q3.setFeedbackForIncorrect(FormApp.createFeedback().setText("Incorrect. MTTD measures detection latency, while MTTR measures remediation time.").build());
  q3.setRequired(true);

  // Savol 4 (2 ball)
  var q4 = form.addMultipleChoiceItem();
  q4.setTitle("4. What is the ultimate objective of an exploit payload during a CTF (Capture The Flag) tournament?");
  q4.setPoints(2);
  q4.setChoices([
    q4.createChoice("Exploiting the target vulnerability to gain unauthorized access and capture the secret flag (TARGET{...})", true),
    q4.createChoice("Destructively wiping system data and taking down the server", false),
    q4.createChoice("Simply defacing the school website design", false),
    q4.createChoice("Updating antivirus definition files", false)
  ]);
  q4.setFeedbackForCorrect(FormApp.createFeedback().setText("Correct! Ethical hacking and CTF focus on finding vulnerabilities and proving access via flags without destructive actions.").build());
  q4.setFeedbackForIncorrect(FormApp.createFeedback().setText("Incorrect. The goal of CTF is capturing the secret flag token to validate access.").build());
  q4.setRequired(true);

  Logger.log("=========================================");
  Logger.log("✅ Google Form muvaffaqiyatli yaratildi!");
  Logger.log("📌 Form Nomi: " + form.getTitle());
  Logger.log("✏️ Tahrirlash havolasi (Edit URL): " + form.getEditUrl());
  Logger.log("🌐 O'quvchilarga tarqatish havolasi (Published URL): " + form.getPublishedUrl());
  Logger.log("=========================================");
}
