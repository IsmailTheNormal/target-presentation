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

  // Savol 1 (1 ball)
  var q1 = form.addMultipleChoiceItem();
  q1.setTitle("1. По правилам кибербезопасности, как составляется наиболее стойкий и невзламываемый пароль?");
  q1.setPoints(1);
  q1.setChoices([
    q1.createChoice("Не менее 14+ знаков, включая заглавные и строчные буквы, цифры и спецсимволы (#, $, !) (Формула трех фраз)", true),
    q1.createChoice("Свое имя и год рождения (например: sardor2014)", false),
    q1.createChoice("Последовательность клавиш (12345678 или qwerty)", false),
    q1.createChoice("Простой 4-значный цифровой PIN-код", false)
  ]);
  q1.setFeedbackForCorrect(FormApp.createFeedback().setText("Молодец! Длинный сложный пароль из 14+ символов невозможно взломать даже суперкомпьютеру.").build());
  q1.setFeedbackForIncorrect(FormApp.createFeedback().setText("Неверно. Простые пароли и даты рождения взламываются за секунду словарной атакой. Пароль должен быть 14+ знаков.").build());
  q1.setRequired(true);

  // Savol 2 (1 ball)
  var q2 = form.addMultipleChoiceItem();
  q2.setTitle("2. Что нужно сделать, если вы увидели ссылку «Бесплатные 10,000 Robux или Telegram Premium, введите свой пароль»?");
  q2.setPoints(1);
  q2.setChoices([
    q2.createChoice("Немедленно закрыть страницу и ничего не вводить — это фишинговая ловушка мошенников!", true),
    q2.createChoice("Быстро ввести пароль и ждать обещанный подарок", false),
    q2.createChoice("Переслать ссылку друзьям и одноклассникам во все чаты", false),
    q2.createChoice("Просто выключить монитор компьютера", false)
  ]);
  q2.setFeedbackForCorrect(FormApp.createFeedback().setText("Верно! Бесплатный сыр бывает только в мышеловке. Это фишинг для угона учетных записей.").build());
  q2.setFeedbackForIncorrect(FormApp.createFeedback().setText("Неверно. Ввод данных на таких сайтах ведет к немедленной потере аккаунта. Никогда не открывайте такие ссылки.").build());
  q2.setRequired(true);

  // Savol 3 (1 ball)
  var q3 = form.addMultipleChoiceItem();
  q3.setTitle("3. Вы скачали скин для игры, но файл называется «cool_skin.png.exe». Почему его категорически нельзя открывать?");
  q3.setPoints(1);
  q3.setChoices([
    q3.createChoice("Это вирус-троян: злоумышленники замаскировали опасную программу (.exe) под безобидную картинку (.png)!", true),
    q3.createChoice("Потому что такие файлы открываются только на телевизоре", false),
    q3.createChoice("Потому что размер файла слишком маленький", false),
    q3.createChoice("Потому что расширение .exe делает картинку красивее", false)
  ]);
  q3.setFeedbackForCorrect(FormApp.createFeedback().setText("Превосходно! Двойное расширение (.png.exe) — классическая ловушка троянов. Это не картинка, а исполняемый вредоносный код.").build());
  q3.setFeedbackForIncorrect(FormApp.createFeedback().setText("Неверно. Файлы .exe являются программами. Если картинка заканчивается на .exe — это вирус-троян.").build());
  q3.setRequired(true);

  // Savol 4 (1 ball)
  var q4 = form.addMultipleChoiceItem();
  q4.setTitle("4. Если при скачивании мода сайт требует «Отключите антивирус, это ложная тревога», как правильно поступить?");
  q4.setPoints(1);
  q4.setChoices([
    q4.createChoice("Ни в коем случае не отключать антивирус и проверить файл через онлайн-сканер VirusTotal.com или в песочнице (Sandbox)!", true),
    q4.createChoice("Отключить антивирус на день и спокойно установить мод", false),
    q4.createChoice("Полностью удалить антивирусную программу с компьютера", false),
    q4.createChoice("Перезагрузить компьютер и всё равно запустить файл", false)
  ]);
  q4.setFeedbackForCorrect(FormApp.createFeedback().setText("Отлично! Злоумышленники всегда манипулируют игроками, заставляя отключать защиту ради заражения системы.").build());
  q4.setFeedbackForIncorrect(FormApp.createFeedback().setText("Неверно. Отключение антивируса открывает прямой доступ вирусам. Безопасные программы никогда этого не требуют.").build());
  q4.setRequired(true);

  // Savol 5 (1 ball)
  var q5 = form.addMultipleChoiceItem();
  q5.setTitle("5. Если в Telegram или Roblox незнакомец представился «Админом школы» и просит: «Назовите 5-значный СМС код подтверждения», что вы сделаете?");
  q5.setPoints(1);
  q5.setChoices([
    q5.createChoice("Никому не называть код, заблокировать контакт и сообщить учителю или родителям — это попытка угона аккаунта!", true),
    q5.createChoice("Сразу отправить код, ведь это администратор", false),
    q5.createChoice("Вместе с кодом отправить еще и пароль", false),
    q5.createChoice("Удалить чат и ждать повторного СМС", false)
  ]);
  q5.setFeedbackForCorrect(FormApp.createFeedback().setText("Правильно! СМС-код — это ключ к вашему аккаунту. Настоящая администрация сервисов никогда не просит назвать секретный код.").build());
  q5.setFeedbackForIncorrect(FormApp.createFeedback().setText("Неверно. Передача кода приводит к мгновенной краже сессии и потере контроля над профилем.").build());
  q5.setRequired(true);

  // Savol 6 (1 ball)
  var q6 = form.addMultipleChoiceItem();
  q6.setTitle("6. Почему кибер-мошенники часто пишут: «Срочно! Осталось 5 минут, иначе ваш аккаунт навсегда заблокируют!»?");
  q6.setPoints(1);
  q6.setChoices([
    q6.createChoice("Чтобы напугать жертву, вызвать панику и заставить совершить необдуманное действие без проверки", true),
    q6.createChoice("Потому что серверы интернета отключаются каждые 5 минут", false),
    q6.createChoice("Это обычное техническое требование онлайн-игр", false),
    q6.createChoice("Это дружеское напоминание от разработчиков", false)
  ]);
  q6.setFeedbackForCorrect(FormApp.createFeedback().setText("Верно! Срочность и угроза блокировки — типичные манипуляции социальной инженерии. Всегда сохраняйте спокойствие.").build());
  q6.setFeedbackForIncorrect(FormApp.createFeedback().setText("Неверно. Искусственная спешка лишает жертву возможности трезво оценить опасность ситуации.").build());
  q6.setRequired(true);

  // Savol 7 (1 ball)
  var q7 = form.addMultipleChoiceItem();
  q7.setTitle("7. Почему перед публикацией фото в интернет нужно стирать скрытые GPS (EXIF) метаданные?");
  q7.setPoints(1);
  q7.setChoices([
    q7.createChoice("Чтобы посторонние и злоумышленники не смогли вычислить точный адрес вашего дома или школы по карте", true),
    q7.createChoice("Чтобы сделать цвета фотографии ярче", false),
    q7.createChoice("Исключительно для экономии памяти смартфона", false),
    q7.createChoice("Чтобы фотография быстрее загружалась", false)
  ]);
  q7.setFeedbackForCorrect(FormApp.createFeedback().setText("Верно! Данные EXIF содержат точные координаты съемки. Их удаление защищает приватность и безопасность дома.").build());
  q7.setFeedbackForIncorrect(FormApp.createFeedback().setText("Неверно. GPS метки раскрывают точное местоположение вашего дома.").build());
  q7.setRequired(true);

  // Savol 8 (1 ball)
  var q8 = form.addMultipleChoiceItem();
  q8.setTitle("8. Что означает «Правило Большого Экрана» (Billboard Rule) безопасного поведения в интернете?");
  q8.setPoints(1);
  q8.setChoices([
    q8.createChoice("Никогда не выкладывать в интернет то, что вы постеснялись бы показать на огромном экране в центре города", true),
    q8.createChoice("Работать только за большим экраном", false),
    q8.createChoice("Писать сообщения только ЗАГЛАВНЫМИ БУКВАМИ", false),
    q8.createChoice("Ходить в кинотеатр на фильмы", false)
  ]);
  q8.setFeedbackForCorrect(FormApp.createFeedback().setText("Верно! Цифровой след остается навсегда. То, что попало в сеть, может стать доступно каждому.").build());
  q8.setFeedbackForIncorrect(FormApp.createFeedback().setText("Неверно. Правило учит осмотрительности при публикации личной информации.").build());
  q8.setRequired(true);

  // Savol 9 (1 ball)
  var q9 = form.addMultipleChoiceItem();
  q9.setTitle("9. Какой самый надежный способ защитить пароли и переписку при подключении к открытому публичному Wi-Fi в кафе?");
  q9.setPoints(1);
  q9.setChoices([
    q9.createChoice("Включить проверенный VPN (Virtual Private Network) и не входить в банковские кабинеты", true),
    q9.createChoice("Подключить смартфон к кабелю быстрой зарядки", false),
    q9.createChoice("Снизить яркость экрана до минимума", false),
    q9.createChoice("Просто выключить Bluetooth и спокойно вводить пароли на незащищенных сайтах", false)
  ]);
  q9.setFeedbackForCorrect(FormApp.createFeedback().setText("Правильно! В открытых сетях злоумышленники могут перехватить трафик. VPN шифрует весь канал.").build());
  q9.setFeedbackForIncorrect(FormApp.createFeedback().setText("Неверно. Защиту трафика в публичных сетях обеспечивает VPN-туннелирование.").build());
  q9.setRequired(true);

  // Savol 10 (1 ball)
  var q10 = form.addMultipleChoiceItem();
  q10.setTitle("10. Каков единственный 100% надежный способ спасти файлы при атаке вируса-вымогателя (Ransomware), зашифровавшего все фото и документы?");
  q10.setPoints(1);
  q10.setChoices([
    q10.createChoice("Регулярное создание резервных копий (Backup) важных файлов на отдельной флешке или в безопасном облаке", true),
    q10.createChoice("Немедленно заплатить выкуп, который требуют вымогатели", false),
    q10.createChoice("Отключить от системного блока мышь и клавиатуру", false),
    q10.createChoice("Протереть экран монитора влажной салфеткой", false)
  ]);
  q10.setFeedbackForCorrect(FormApp.createFeedback().setText("Отлично! Резервная копия (Backup) — единственная гарантия против вирусов-вымогателей. Файлы восстанавливаются бесплатно за минуты.").build());
  q10.setFeedbackForIncorrect(FormApp.createFeedback().setText("Неверно. Выплата выкупа не гарантирует расшифровку. Единственное спасение — наличие резервной копии (Backup).").build());
  q10.setRequired(true);

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

  // Savol 1 (1 ball)
  var q1 = form.addMultipleChoiceItem();
  q1.setTitle("1. According to cybersecurity rules, how is the strongest, uncrackable password formulated?");
  q1.setPoints(1);
  q1.setChoices([
    q1.createChoice("At least 14+ characters mixing uppercase, lowercase, numbers, and special symbols (#, $, !) (Three-word passphrase formula)", true),
    q1.createChoice("Personal name and birth year (e.g., sardor2014)", false),
    q1.createChoice("Sequential keyboard characters (12345678 or qwerty)", false),
    q1.createChoice("A simple 4-digit numeric PIN", false)
  ]);
  q1.setFeedbackForCorrect(FormApp.createFeedback().setText("Well done! A 14+ character complex passphrase withstands brute-force attempts for centuries.").build());
  q1.setFeedbackForIncorrect(FormApp.createFeedback().setText("Incorrect. Names and simple sequences are cracked within seconds via dictionary attacks. Passwords must be 14+ characters.").build());
  q1.setRequired(true);

  // Savol 2 (1 ball)
  var q2 = form.addMultipleChoiceItem();
  q2.setTitle("2. What must you do if you encounter a link claiming 'Free 10,000 Robux or Telegram Premium, enter your password'?");
  q2.setPoints(1);
  q2.setChoices([
    q2.createChoice("Immediately close the webpage and never enter credentials — it is a phishing trap!", true),
    q2.createChoice("Quickly input account credentials and await the prize", false),
    q2.createChoice("Forward the link to all classmates and school groups", false),
    q2.createChoice("Turn off the computer monitor", false)
  ]);
  q2.setFeedbackForCorrect(FormApp.createFeedback().setText("Correct! Free handouts are classic lures. This is credential phishing designed to steal accounts.").build());
  q2.setFeedbackForIncorrect(FormApp.createFeedback().setText("Incorrect. Submitting credentials on untrusted domains results in immediate account takeover.").build());
  q2.setRequired(true);

  // Savol 3 (1 ball)
  var q3 = form.addMultipleChoiceItem();
  q3.setTitle("3. You downloaded a game skin, but the file is named 'cool_skin.png.exe'. Why must you never open this file?");
  q3.setPoints(1);
  q3.setChoices([
    q3.createChoice("It is a Trojan virus: attackers camouflaged an executable payload (.exe) under a decoy image extension (.png)!", true),
    q3.createChoice("Because such files only open on smart televisions", false),
    q3.createChoice("Because the file size is too small", false),
    q3.createChoice("Because the .exe extension supposedly enhances image quality", false)
  ]);
  q3.setFeedbackForCorrect(FormApp.createFeedback().setText("Splendid! The double extension (.png.exe) is a signature Trojan disguise. It is an executable program, not an image.").build());
  q3.setFeedbackForIncorrect(FormApp.createFeedback().setText("Incorrect. .exe files are programs. An image ending in .exe is always a dangerous Trojan.").build());
  q3.setRequired(true);

  // Savol 4 (1 ball)
  var q4 = form.addMultipleChoiceItem();
  q4.setTitle("4. If a game mod download site insists 'Disable your antivirus, it is a false alarm', what is the proper action?");
  q4.setPoints(1);
  q4.setChoices([
    q4.createChoice("Never disable your antivirus and immediately analyze the file using VirusTotal.com or an isolated Sandbox!", true),
    q4.createChoice("Temporarily disable the antivirus for a day and install the mod", false),
    q4.createChoice("Completely uninstall the antivirus software from the PC", false),
    q4.createChoice("Reboot the computer and run the file anyway", false)
  ]);
  q4.setFeedbackForCorrect(FormApp.createFeedback().setText("Outstanding! Attackers routinely trick gamers into dropping their defenses so malware can take root.").build());
  q4.setFeedbackForIncorrect(FormApp.createFeedback().setText("Incorrect. Disabling antivirus surrenders your system to malware. Safe programs never demand turning off protection.").build());
  q4.setRequired(true);

  // Savol 5 (1 ball)
  var q5 = form.addMultipleChoiceItem();
  q5.setTitle("5. If a stranger on Telegram or Roblox claims to be a 'School Admin' asking: 'Share your 5-digit SMS verification code', what do you do?");
  q5.setPoints(1);
  q5.setChoices([
    q5.createChoice("Never reveal the code, block the contact immediately, and inform a teacher or parent — this is an account takeover attempt!", true),
    q5.createChoice("Send the SMS code immediately since they claim to be an administrator", false),
    q5.createChoice("Send both the code and the account password", false),
    q5.createChoice("Delete the chat and wait for another SMS", false)
  ]);
  q5.setFeedbackForCorrect(FormApp.createFeedback().setText("Correct! The SMS verification code is your account key. Legitimate administrators never solicit private one-time codes.").build());
  q5.setFeedbackForIncorrect(FormApp.createFeedback().setText("Incorrect. Disclosing verification codes enables attackers to instantly seize your account and lock you out.").build());
  q5.setRequired(true);

  // Savol 6 (1 ball)
  var q6 = form.addMultipleChoiceItem();
  q6.setTitle("6. Why do cyber scammers deliberately write: 'Urgent! Only 5 minutes left or your account will be permanently banned!'?");
  q6.setPoints(1);
  q6.setChoices([
    q6.createChoice("To induce panic and fear, forcing victims into hasty irrational actions without verifying facts", true),
    q6.createChoice("Because internet servers restart every 5 minutes", false),
    q6.createChoice("It is merely a routine gaming software technical requirement", false),
    q6.createChoice("A friendly courtesy reminder from online staff", false)
  ]);
  q6.setFeedbackForCorrect(FormApp.createFeedback().setText("Correct! Manufactured urgency is a hallmark of social engineering. Always pause, reflect, and verify independently.").build());
  q6.setFeedbackForIncorrect(FormApp.createFeedback().setText("Incorrect. Scammers intentionally manufacture time crunches to bypass your critical thinking.").build());
  q6.setRequired(true);

  // Savol 7 (1 ball)
  var q7 = form.addMultipleChoiceItem();
  q7.setTitle("7. Why should hidden GPS location (EXIF) metadata be stripped before publishing photos online?");
  q7.setPoints(1);
  q7.setChoices([
    q7.createChoice("To prevent strangers and adversaries from tracking your exact home or school coordinates on a map", true),
    q7.createChoice("To enhance photo colors and brightness", false),
    q7.createChoice("Solely to free up storage on the smartphone", false),
    q7.createChoice("To speed up image rendering", false)
  ]);
  q7.setFeedbackForCorrect(FormApp.createFeedback().setText("Correct! EXIF tags hold precise GPS coordinates. Removing them preserves physical safety and residence privacy.").build());
  q7.setFeedbackForIncorrect(FormApp.createFeedback().setText("Incorrect. GPS metadata discloses exact physical residential locations.").build());
  q7.setRequired(true);

  // Savol 8 (1 ball)
  var q8 = form.addMultipleChoiceItem();
  q8.setTitle("8. What does the 'Billboard Rule' teach about safe online conduct?");
  q8.setPoints(1);
  q8.setChoices([
    q8.createChoice("Never upload personal photos or data that you would feel uncomfortable displaying on a giant public billboard", true),
    q8.createChoice("Only using large desktop monitors", false),
    q8.createChoice("Writing chat messages strictly in ALL CAPS", false),
    q8.createChoice("Going to movie theaters regularly", false)
  ]);
  q8.setFeedbackForCorrect(FormApp.createFeedback().setText("Correct! The digital footprint lasts indefinitely. Treat all online postings as visible to the whole world.").build());
  q8.setFeedbackForIncorrect(FormApp.createFeedback().setText("Incorrect. The Billboard Rule cautions against uploading any material you wouldn't share publicly.").build());
  q8.setRequired(true);

  // Savol 9 (1 ball)
  var q9 = form.addMultipleChoiceItem();
  q9.setTitle("9. What is the most effective safeguard for protecting passwords and chats on open public Wi-Fi?");
  q9.setPoints(1);
  q9.setChoices([
    q9.createChoice("Engage a trusted VPN (Virtual Private Network) and avoid logging into banking portals", true),
    q9.createChoice("Plugging the smartphone into a wall charger", false),
    q9.createChoice("Dimming screen brightness to the minimum", false),
    q9.createChoice("Disabling Bluetooth while submitting passwords over plain unencrypted web pages", false)
  ]);
  q9.setFeedbackForCorrect(FormApp.createFeedback().setText("Correct! Public Wi-Fi lacks encryption. A VPN secures your traffic through an encrypted tunnel.").build());
  q9.setFeedbackForIncorrect(FormApp.createFeedback().setText("Incorrect. Safeguarding public Wi-Fi communication requires VPN tunneling.").build());
  q9.setRequired(true);

  // Savol 10 (1 ball)
  var q10 = form.addMultipleChoiceItem();
  q10.setTitle("10. What is the only 100% reliable safeguard to recover data when hit by Ransomware that encrypted all photos and documents?");
  q10.setPoints(1);
  q10.setChoices([
    q10.createChoice("Regularly maintaining offline data backups on an isolated external drive or secure cloud storage", true),
    q10.createChoice("Immediately paying the ransom fee demanded by extortionists", false),
    q10.createChoice("Disconnecting keyboard and mouse peripherals", false),
    q10.createChoice("Wiping the monitor screen clean", false)
  ]);
  q10.setFeedbackForCorrect(FormApp.createFeedback().setText("Outstanding! Regular offline backups are the gold standard defense against ransomware extortion. Data is restored effortlessly without paying ransoms.").build());
  q10.setFeedbackForIncorrect(FormApp.createFeedback().setText("Incorrect. Paying ransom demands never guarantees decryption. Reliable offline backups are the only proven solution.").build());
  q10.setRequired(true);

  Logger.log("=========================================");
  Logger.log("✅ Google Form muvaffaqiyatli yaratildi!");
  Logger.log("📌 Form Nomi: " + form.getTitle());
  Logger.log("✏️ Tahrirlash havolasi (Edit URL): " + form.getEditUrl());
  Logger.log("🌐 O'quvchilarga tarqatish havolasi (Published URL): " + form.getPublishedUrl());
  Logger.log("=========================================");
}
