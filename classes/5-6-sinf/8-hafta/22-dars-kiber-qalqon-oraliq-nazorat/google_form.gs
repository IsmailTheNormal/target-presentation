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

  // Savol 11 (1 ball)
  var q11 = form.addMultipleChoiceItem();
  q11.setTitle("11. Hisobingizga 2FA (Ikki bosqichli himoya) ulangan. Agar xaker parolingizni bilib olsa, hisobingizga to'g'ridan-to'g'ri kira oladimi?");
  q11.setPoints(1);
  q11.setChoices([
    q11.createChoice("Yo'q, kira olmaydi! Chunki ikkinchi bosqichdagi SMS yoki Authenticator maxfiy bir martalik kodi faqat sizning telefoningizga keladi", true),
    q11.createChoice("Ha, parolni bilsa bo'ldi, 2FA avtomatik bekor qilinadi", false),
    q11.createChoice("Faqat kunduzi kira olmaydi, kechasi bemalol kiradi", false),
    q11.createChoice("Xaker barcha SMS kodlarni telefon raqamisiz ko'ra oladi", false)
  ]);
  q11.setFeedbackForCorrect(FormApp.createFeedback().setText("To'g'ri! 2FA — bu mustahkam ikkinchi temir qulf. Parol fosh bo'lsa ham, telefondagi kodsiz akkauntga kirib bo'lmaydi. Kodni hech kimga bermang!").build());
  q11.setFeedbackForIncorrect(FormApp.createFeedback().setText("Xato. 2FA bor joyda xaker faqat parol bilan kira olmaydi, chunki telefoningizdagi bir martalik tasdiq kodi talab qilinadi.").build());
  q11.setRequired(true);

  // Savol 12 (1 ball)
  var q12 = form.addMultipleChoiceItem();
  q12.setTitle("12. Maktab hovlisida yoki parta ustida yangi chiroyli USB fleshka topib oldingiz. Kiber-xavfsizlik bo'yicha to'g'ri qaror qaysi?");
  q12.setPoints(1);
  q12.setChoices([
    q12.createChoice("Hech qachon o'z yoki maktab kompyuteriga tiqmaslik va uni o'qituvchiga topshirish (BadUSB yoki virus xavfi)", true),
    q12.createChoice("Darhol noutbukka ulab, ichida qanday zo'r o'yinlar borligini ko'rish", false),
    q12.createChoice("Uni format qilib, o'z musiqalaringizni yozib olish", false),
    q12.createChoice("Barcha sinfdoshlarning kompyuterlariga navbatma-navbat ulab tekshirish", false)
  ]);
  q12.setFeedbackForCorrect(FormApp.createFeedback().setText("To'g'ri! 'Tashlab ketilgan USB' — xakerlarning eng xavfli qopqonlaridan biri. BadUSB kompyuterga ulanganda soniyalar ichida zararli buyruqlarni kiritishi mumkin.").build());
  q12.setFeedbackForIncorrect(FormApp.createFeedback().setText("Xato. Notanish USB ni aslo kompyuterga ulamang! Unda klaviatura kabi zararli dastur yuboruvchi mikrokontroller (BadUSB) bo'lishi mumkin.").build());
  q12.setRequired(true);

  // Savol 13 (1 ball)
  var q13 = form.addMultipleChoiceItem();
  q13.setTitle("13. Smartfonga oddiy 'Chiroqcha' (Fonar) yoki 'Kalkulyator' ilovasi o'rnatilayotganda, u 'Kamera, Mikrofon va Kontaktlar'ga ruxsat so'rasa, nima qilish kerak?");
  q13.setPoints(1);
  q13.setChoices([
    q13.createChoice("Ruxsatni rad etish va ilovani darhol o'chirib tashlash (chunki oddiy kalkulyatorga mikrofon kerak emas, bu josuslik dasturi bo'lishi mumkin)", true),
    q13.createChoice("Hammasiga 'Ruxsat berish' tugmasini bosish, aks holda ilova yaxshi hisoblamaydi", false),
    q13.createChoice("Faqat mikrofonga ruxsat berib, boshqalarini o'chirish", false),
    q13.createChoice("Telefon batareyasini chiqarib olish", false)
  ]);
  q13.setFeedbackForCorrect(FormApp.createFeedback().setText("A'lo! Minimal ruxsatlar qoidasi: Agar oddiy dastur ortiqcha shaxsiy ma'lumotlarni so'rasa, bu maxfiy josuslik dasturidir (Spyware).").build());
  q13.setFeedbackForIncorrect(FormApp.createFeedback().setText("Xato. Kalkulyatorga hech qachon kontaktlar va mikrofon kerak bo'lmaydi. Bunday ruxsat berish shaxsiy ma'lumotlaringizni xakerlarga topshirish demakdir.").build());
  q13.setRequired(true);

  // Savol 14 (1 ball)
  var q14 = form.addMultipleChoiceItem();
  q14.setTitle("14. Sinfdoshingizning Telegram profilidan: 'Salom, zudlik bilan kartamga 50,000 so'm tashlab ber, dori olishim kerak, kartam bloklandi' degan xabar keldi. Birinchi to'g'ri qadam:");
  q14.setPoints(1);
  q14.setChoices([
    q14.createChoice("Pul o'tkazishdan oldin unga telefon qilib yoki ovozli xabar orqali, haqiqatan u yozayotganiga ishonch hosil qilish", true),
    q14.createChoice("Do'stga zudlik bilan yordam berish kerak deb, kartasiga darhol pul o'tkazish", false),
    q14.createChoice("O'z bank kartangiz rasmini va SMS kodini yuborish", false),
    q14.createChoice("Xabarni barcha tanishlarga forward qilib tarqatish", false)
  ]);
  q14.setFeedbackForCorrect(FormApp.createFeedback().setText("Barakalla! Xakerlar o'g'irlangan Telegram akkauntlar nomidan barcha kontaktlarga shoshilinch pul so'rab yozishadi. Har qanday moliyaviy so'rov ovozli tekshirilishi shart!").build());
  q14.setFeedbackForIncorrect(FormApp.createFeedback().setText("Xato. O'g'irlangan akkauntdan yozilgan xabarga ishonib pul o'tkazsangiz, firibgarlarga pul bergan bo'lasiz. Avval do'stingizga qo'ng'iroq qiling!").build());
  q14.setRequired(true);

  // Savol 15 (1 ball)
  var q15 = form.addMultipleChoiceItem();
  q15.setTitle("15. Sizga quyidagi havola yuborildi: 'https://payme-uz.security-verify.click/login'. Bu havola rasmiy Payme tizimiga tegishlimi?");
  q15.setPoints(1);
  q15.setChoices([
    q15.createChoice("Yo'q, bu soxta fishing sayt! Asosiy domen 'security-verify.click' bo'lib, 'payme-uz' shunchaki chalg'ituvchi soxta subdomendir", true),
    q15.createChoice("Ha, chunki manzil boshida 'payme-uz' so'zi aniq yozilgan", false),
    q15.createChoice("Ha, chunki havolada yashil qulfcha (https://) bor, demak sayt 100% ishonchli", false),
    q15.createChoice("Agar sahifada rasmiy logotip tursa, demak manzil to'g'ri", false)
  ]);
  q15.setFeedbackForCorrect(FormApp.createFeedback().setText("To'g'ri! Domen qoidasi: Asosiy manzil doimo oxirgi nuqta va kengaytma (.uz) oldidagi so'zdir (payme.uz). security-verify.click esa firibgarlar saytidir!").build());
  q15.setFeedbackForIncorrect(FormApp.createFeedback().setText("Xato. 'https://' faqat aloqa shifrlanganligini bildiradi, saytning halolligini kafolatlamaydi. Firibgarlar soxta domenlardan foydalanadilar.").build());
  q15.setRequired(true);

  // Savol 16 (1 ball)
  var q16 = form.addMultipleChoiceItem();
  q16.setTitle("16. Brauzerda qidirayotganingizda to'satdan qizil ekran ochilib, 'DIQQAT! Telefoningizda 13 ta xavfli virus topildi! Tozalash uchun bu tugmani bosing' deb chiqdi. To'g'ri harakat:");
  q16.setPoints(1);
  q16.setChoices([
    q16.createChoice("Brauzer varaqasini darhol yopish, hech narsa yuklab olmaslik va bosmaslik (bu odamlarni qo'rqituvchi soxta Scareware reklamasi)", true),
    q16.createChoice("Ekranda ko'rsatilgan 'Tozalash' tugmasini tezroq bosib, taklif qilingan ilovani o'rnatish", false),
    q16.createChoice("Telefon raqamingizni kiritib, tozalash kodini kutish", false),
    q16.createChoice("Telefonni o'chirib, suvga solish", false)
  ]);
  q16.setFeedbackForCorrect(FormApp.createFeedback().setText("A'lo! Oddiy veb-saytlar telefoningiz xotirasi ichidagi fayllarni skaner qila olmaydi. Bu sizga zararli dastur o'rnatish uchun uyushtirilgan Scareware tuzog'idir.").build());
  q16.setFeedbackForIncorrect(FormApp.createFeedback().setText("Xato. Saytlar virusni aniqlay olmaydi. Agar 'Tozalash' tugmasini bossangiz, telefoningizga haqiqiy virus yoki obuna to'lovli dastur tushadi.").build());
  q16.setRequired(true);

  // Savol 17 (1 ball)
  var q17 = form.addMultipleChoiceItem();
  q17.setTitle("17. Maktab kompyuterida yoki do'stingizning noutbukida shaxsiy akkauntingizga kirdingiz. Dars tugagach nima qilish shart?");
  q17.setPoints(1);
  q17.setChoices([
    q17.createChoice("Akkauntdan to'liq chiqish (Log out) tugmasini bosish va brauzerda parolni hech qachon saqlamaslik", true),
    q17.createChoice("Faqat brauzer darchasini 'X' tugmasi bilan yopib ketish kifoya", false),
    q17.createChoice("Brauzer 'Parolni eslab qolaymi?' deb so'raganda 'Ha' tugmasini bosish", false),
    q17.createChoice("Kompyuter ekranini o'chirib qo'yish", false)
  ]);
  q17.setFeedbackForCorrect(FormApp.createFeedback().setText("To'g'ri! Agar siz 'Log out' qilmasangiz, kompyuterga keyingi o'tirgan har qanday o'quvchi sizning hisobingizga ruxsatsiz kira oladi.").build());
  q17.setFeedbackForIncorrect(FormApp.createFeedback().setText("Xato. Darchani shunchaki yopish seansni to'xtatmaydi. Parol saqlanib qolsa, boshqalar sizning nomingizdan harakat qilishi mumkin.").build());
  q17.setRequired(true);

  // Savol 18 (1 ball)
  var q18 = form.addMultipleChoiceItem();
  q18.setTitle("18. Smartfon yoki operatsion tizim 'Xavfsizlik yangilanishi mavjud (Update)' deb so'raganda, nega buni o'rnatish muhim?");
  q18.setPoints(1);
  q18.setChoices([
    q18.createChoice("Chunki yangilanishlar tizimdagi zaifliklar (xavfli teshiklar)ni yopadi va xakerlarning yangi viruslaridan himoya qiladi", true),
    q18.createChoice("Faqat telefon ekranidagi fon rasmlari va ikonkalarni almashtirish uchun kerak", false),
    q18.createChoice("Yangilanishlar faqat internet trafigini sarflash uchun chiqariladi, ularni o'rnatish kerak emas", false),
    q18.createChoice("Yangilanish qurilmadagi barcha fotosuratlarni o'chirib yuboradi", false)
  ]);
  q18.setFeedbackForCorrect(FormApp.createFeedback().setText("Barakalla! Xavfsizlik yangilanishlari (Patch) xakerlar kashf etgan zaifliklarni bartaraf qiladi. Yangilanmagan dasturlar xavf ostida qoladi.").build());
  q18.setFeedbackForIncorrect(FormApp.createFeedback().setText("Xato. Yangilanishlar chiroyli dizayn uchun emas, birinchi navbatda xavfsizlik tuynuklarini yopish uchun chiqariladi.").build());
  q18.setRequired(true);

  // Savol 19 (1 ball)
  var q19 = form.addMultipleChoiceItem();
  q19.setTitle("19. Onlayn o'yin chatida notanish odam sizni haqorat qilib, shaxsiy rasmlaringizni tarqatish bilan qo'rqitsa (kiberbulling), to'g'ri chora:");
  q19.setPoints(1);
  q19.setChoices([
    q19.createChoice("Aslo javob qaytarmaslik, skrinshot olib dalil saqlash, odamni bloklash va darhol ota-onangiz yoki o'qituvchingizga aytish", true),
    q19.createChoice("Unga javoban undan ham yomonroq haqoratlar yozish va janjallashish", false),
    q19.createChoice("Qo'rqqaningizdan unga o'z akkaunt parollaringizni yoki pulingizni berish", false),
    q19.createChoice("Hech kimga aytmasdan, o'yinni o'chirib siqilib yurish", false)
  ]);
  q19.setFeedbackForCorrect(FormApp.createFeedback().setText("To'g'ri! Provokatsiyaga berilmang. Xakerlar va trollarning maqsadi — sizni qo'rqitish. Bloklang, dalilni saqlang va kattalarga xabar bering!").build());
  q19.setFeedbackForIncorrect(FormApp.createFeedback().setText("Xato. O'zingiz javob bersangiz vaziyat yanada yomonlashadi, pul berish esa yangi tovlamachilikka olib keladi. Doim kattalarga ayting!").build());
  q19.setRequired(true);

  // Savol 20 (1 ball)
  var q20 = form.addMultipleChoiceItem();
  q20.setTitle("20. Kompyuteringiz qattiq diski buzilsa yoki virus tushsa, barcha dars va loyihalaringizni yo'qotmaslikning yagona kafolatli yo'li nima?");
  q20.setPoints(1);
  q20.setChoices([
    q20.createChoice("Muhim fayllarning zaxira nusxasini (Backup) muntazam ravishda alohida tashqi xotirada yoki xavfsiz bulutda saqlab borish", true),
    q20.createChoice("Fayllarni kompyuterning 'Savat' (Recycle Bin / Корзина) qutisiga solib qo'yish", false),
    q20.createChoice("Fayllar nomini 'Maxfiy va O'chmas' deb o'zgartirib qo'yish", false),
    q20.createChoice("Kompyuterga hech qachon yangi dastur o'rnatmaslik", false)
  ]);
  q20.setFeedbackForCorrect(FormApp.createFeedback().setText("A'lo! '3-2-1 zaxira qoidasi': 3 ta nusxa, 2 xil tashuvchi, 1 ta tashqi/bulut nusxa. Zaxira nusxa bor joyda kiber-hujumlar sizga zarar keltira olmaydi!").build());
  q20.setFeedbackForIncorrect(FormApp.createFeedback().setText("Xato. Savat yoki fayl nomini o'zgartirish himoya qilmaydi. Yagona haqiqiy najot — bu alohida xotiradagi zaxira nusxa (Backup)dir.").build());
  q20.setRequired(true);

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

  // Savol 11 (1 ball)
  var q11 = form.addMultipleChoiceItem();
  q11.setTitle("11. К вашему аккаунту подключена двухфакторная аутентификация (2FA). Если злоумышленник узнает ваш пароль, сможет ли он войти в аккаунт?");
  q11.setPoints(1);
  q11.setChoices([
    q11.createChoice("Нет, не сможет! Потому что секретный одноразовый код (SMS или Authenticator) приходит исключительно на ваш личный телефон", true),
    q11.createChoice("Да, зная пароль, вход выполняется сразу, 2FA отключается", false),
    q11.createChoice("Только днем не сможет, а ночью защита выключается", false),
    q11.createChoice("Хакер видит все SMS-коды без телефона через спутник", false)
  ]);
  q11.setFeedbackForCorrect(FormApp.createFeedback().setText("Правильно! 2FA — это второй надежный замок. Даже при утечке пароля войти без кода невозможно. Никогда никому не передавайте коды!").build());
  q11.setFeedbackForIncorrect(FormApp.createFeedback().setText("Неверно. При включенном 2FA пароля недостаточно — требуется одноразовый секретный код подтверждения с телефона.").build());
  q11.setRequired(true);

  // Savol 12 (1 ball)
  var q12 = form.addMultipleChoiceItem();
  q12.setTitle("12. Во дворе школы или на парте вы нашли новую красивую USB-флешку. Какое действие является правильным с точки зрения кибербезопасности?");
  q12.setPoints(1);
  q12.setChoices([
    q12.createChoice("Ни в коем случае не вставлять в компьютер и передать ее учителю (угроза BadUSB или скрытого вредоноса)", true),
    q12.createChoice("Сразу вставить в ноутбук и проверить, какие интересные игры на ней записаны", false),
    q12.createChoice("Быстро отформатировать ее и скопировать свою музыку", false),
    q12.createChoice("По очереди вставить во все компьютеры одноклассников", false)
  ]);
  q12.setFeedbackForCorrect(FormApp.createFeedback().setText("Правильно! 'Подкинутая флешка' — классический трюк социальной инженерии (BadUSB). Она может мгновенно скомпрометировать систему.").build());
  q12.setFeedbackForIncorrect(FormApp.createFeedback().setText("Неверно. Нельзя вставлять чужие накопители. Это может быть устройство BadUSB, маскирующееся под флешку и заражающее систему.").build());
  q12.setRequired(true);

  // Savol 13 (1 ball)
  var q13 = form.addMultipleChoiceItem();
  q13.setTitle("13. При установке простого фонарика или калькулятора на смартфон приложение запрашивает доступ к камере, микрофону и контактам. Что делать?");
  q13.setPoints(1);
  q13.setChoices([
    q13.createChoice("Отклонить разрешения и удалить приложение (калькулятору не нужен микрофон, это признак шпионского ПО Spyware)", true),
    q13.createChoice("Нажать 'Разрешить все', иначе калькулятор не сможет считать", false),
    q13.createChoice("Разрешить только микрофон, а остальное запретить", false),
    q13.createChoice("Вытащить батарею из смартфона", false)
  ]);
  q13.setFeedbackForCorrect(FormApp.createFeedback().setText("Отлично! Принцип минимальных привилегий: если простая утилита требует доступ к приватным данным, это вредоносный шпион (Spyware).").build());
  q13.setFeedbackForIncorrect(FormApp.createFeedback().setText("Неверно. Калькулятору не нужны личные контакты. Выдача таких прав открывает доступ шпионам к вашей частной жизни.").build());
  q13.setRequired(true);

  // Savol 14 (1 ball)
  var q14 = form.addMultipleChoiceItem();
  q14.setTitle("14. С профиля одноклассника в Telegram приходит сообщение: 'Привет, скинь срочно 50 000 сум на карту, нужно на лекарства, моя карта заблокирована'. Ваши действия:");
  q14.setPoints(1);
  q14.setChoices([
    q14.createChoice("Прежде чем переводить деньги, позвонить однокласснику по обычному телефону и голосом убедиться, что пишет именно он", true),
    q14.createChoice("Срочно отправить деньги, ведь другу нужна помощь", false),
    q14.createChoice("Отправить ему фото своей банковской карты и SMS-код", false),
    q14.createChoice("Переслать это сообщение во все школьные группы", false)
  ]);
  q14.setFeedbackForCorrect(FormApp.createFeedback().setText("Молодец! При взломе аккаунтов мошенники массово рассылают просьбы о займе. Любой денежный запрос проверяется личным голосовым звонком!").build());
  q14.setFeedbackForIncorrect(FormApp.createFeedback().setText("Неверно. Нельзя переводить деньги вслепую. Аккаунт может быть взломан. Сначала обязательно позвоните другу лично.").build());
  q14.setRequired(true);

  // Savol 15 (1 ball)
  var q15 = form.addMultipleChoiceItem();
  q15.setTitle("15. Вам прислали ссылку: 'https://payme-uz.security-verify.click/login'. Принадлежит ли этот адрес официальной платежной системе Payme?");
  q15.setPoints(1);
  q15.setChoices([
    q15.createChoice("Нет, это фишинговый сайт! Основной домен — 'security-verify.click', а 'payme-uz' — лишь обманный поддомен", true),
    q15.createChoice("Да, ведь в начале адреса четко написано имя 'payme-uz'", false),
    q15.createChoice("Да, ведь есть значок замочка (https://), что гарантирует подлинность компании", false),
    q15.createChoice("Если на странице отображается логотип Payme, сайт настоящий", false)
  ]);
  q15.setFeedbackForCorrect(FormApp.createFeedback().setText("Правильно! Правило доменов: истинный адрес находится непосредственно перед доменной зоной. security-verify.click — типичный фишинг.").build());
  q15.setFeedbackForIncorrect(FormApp.createFeedback().setText("Неверно. HTTPS показывает лишь шифрование канала связи, но не честность сайта. Фишеры легко ставят сертификаты на свои домены.").build());
  q15.setRequired(true);

  // Savol 16 (1 ball)
  var q16 = form.addMultipleChoiceItem();
  q16.setTitle("16. В браузере внезапно открывается красная страница: 'ВНИМАНИЕ! На телефоне найдено 13 опасных вирусов! Нажмите для очистки'. Ваши действия:");
  q16.setPoints(1);
  q16.setChoices([
    q16.createChoice("Немедленно закрыть вкладку браузера, ничего не нажимать и не скачивать (это пугающая реклама Scareware)", true),
    q16.createChoice("Быстрее нажать кнопку 'Очистить' и установить предложенную программу", false),
    q16.createChoice("Ввести свой номер телефона и ждать защитный код", false),
    q16.createChoice("Выключить телефон и опустить его в воду", false)
  ]);
  q16.setFeedbackForCorrect(FormApp.createFeedback().setText("Отлично! Обычный сайт не имеет доступа к файловой системе устройства. Такие баннеры — мошеннический Scareware для навязывания вредоносов.").build());
  q16.setFeedbackForIncorrect(FormApp.createFeedback().setText("Неверно. Сайты не сканируют телефон на вирусы. Нажав 'Очистить', вы сами загрузите вредоносную или платную программу.").build());
  q16.setRequired(true);

  // Savol 17 (1 ball)
  var q17 = form.addMultipleChoiceItem();
  q17.setTitle("17. На школьном компьютере или ноутбуке друга вы вошли в свой личный аккаунт. Что обязательно сделать по окончании урока?");
  q17.setPoints(1);
  q17.setChoices([
    q17.createChoice("Нажать 'Выйти' (Log out) из аккаунта и ни в коем случае не сохранять пароль в браузере", true),
    q17.createChoice("Просто закрыть вкладку крестиком 'X', этого вполне достаточно", false),
    q17.createChoice("Нажать 'Да, сохранить пароль' во всплывающем окне браузера", false),
    q17.createChoice("Выключить кнопку монитора", false)
  ]);
  q17.setFeedbackForCorrect(FormApp.createFeedback().setText("Правильно! Закрытия вкладки недостаточно. Без выхода (Log out) любой следующий пользователь получит полный доступ к вашей переписке.").build());
  q17.setFeedbackForIncorrect(FormApp.createFeedback().setText("Неверно. Простое закрытие окна не завершает сессию. Следующий человек откроет браузер и окажется внутри вашего профиля.").build());
  q17.setRequired(true);

  // Savol 18 (1 ball)
  var q18 = form.addMultipleChoiceItem();
  q18.setTitle("18. Когда смартфон или операционная система предлагает установить 'Обновление безопасности (Update)', почему важно не откладывать его?");
  q18.setPoints(1);
  q18.setChoices([
    q18.createChoice("Потому что обновления устраняют уязвимости (дыры в защите) и защищают от новых методов хакерских атак", true),
    q18.createChoice("Это нужно только для изменения значков и обоев на экране", false),
    q18.createChoice("Обновления только тратят трафик и память, ставить их не нужно", false),
    q18.createChoice("Обновление стирает все фотографии на устройстве", false)
  ]);
  q18.setFeedbackForCorrect(FormApp.createFeedback().setText("Молодец! Патчи безопасности закрывают лазейки, через которые действуют вредоносные скрипты. Обновления — основа кибергигиены.").build());
  q18.setFeedbackForIncorrect(FormApp.createFeedback().setText("Неверно. Обновления выпускаются для устранения опасных брешей в защите. Без них устройство становится легкой мишенью.").build());
  q18.setRequired(true);

  // Savol 19 (1 ball)
  var q19 = form.addMultipleChoiceItem();
  q19.setTitle("19. В чате онлайн-игры незнакомец оскорбляет вас и угрожает распространить личные фото (кибербуллинг). Правильное решение:");
  q19.setPoints(1);
  q19.setChoices([
    q19.createChoice("Не отвечать агрессией, сделать скриншоты для доказательств, заблокировать обидчика и немедленно рассказать родителям или учителю", true),
    q19.createChoice("Начать ругаться и оскорблять его в ответ еще сильнее", false),
    q19.createChoice("Испугаться и отдать ему свои пароли или карманные деньги", false),
    q19.createChoice("Никому ничего не говорить и молча переживать в одиночку", false)
  ]);
  q19.setFeedbackForCorrect(FormApp.createFeedback().setText("Правильно! Не вступайте в перепалку. Сохраните улики (скриншоты), заблокируйте буллера и обязательно обратитесь к взрослым.").build());
  q19.setFeedbackForIncorrect(FormApp.createFeedback().setText("Неверно. Ответная агрессия разжигает конфликт, а уступки ведут к вымогательству. Обязательно привлекайте взрослых.").build());
  q19.setRequired(true);

  // Savol 20 (1 ball)
  var q20 = form.addMultipleChoiceItem();
  q20.setTitle("20. Если жесткий диск компьютера выйдет из строя или его заблокирует вирус, какой единственный надежный способ не потерять свои файлы?");
  q20.setPoints(1);
  q20.setChoices([
    q20.createChoice("Регулярно делать резервные копии (Backup) важных файлов на отдельном внешнем диске или в надежном облачном хранилище", true),
    q20.createChoice("Складывать все файлы в корзину на рабочем столе", false),
    q20.createChoice("Переименовать файлы в 'Секретные и неудаляемые'", false),
    q20.createChoice("Никогда не выключать компьютер из розетки", false)
  ]);
  q20.setFeedbackForCorrect(FormApp.createFeedback().setText("Отлично! 'Правило 3-2-1': 3 копии, 2 разных носителя, 1 копия в облаке. Резервная копия гарантирует сохранность данных при любых авариях.").build());
  q20.setFeedbackForIncorrect(FormApp.createFeedback().setText("Неверно. Переименование или помещение в корзину не спасает данные. Единственная защита от потерь — своевременный бэкап.").build());
  q20.setRequired(true);

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

  // Savol 11 (1 ball)
  var q11 = form.addMultipleChoiceItem();
  q11.setTitle("11. Two-Factor Authentication (2FA) is enabled on your account. If a hacker discovers your password, can they directly breach your account?");
  q11.setPoints(1);
  q11.setChoices([
    q11.createChoice("No, they cannot! The secondary one-time verification code (SMS or Authenticator) is delivered exclusively to your personal phone", true),
    q11.createChoice("Yes, knowing the password bypasses everything and disables 2FA automatically", false),
    q11.createChoice("They cannot breach by day, but protection turns off at night", false),
    q11.createChoice("Hackers intercept all SMS codes via satellite without a phone", false)
  ]);
  q11.setFeedbackForCorrect(FormApp.createFeedback().setText("Correct! 2FA provides a critical secondary defense layer. Even with a leaked password, an attacker cannot log in without your one-time code.").build());
  q11.setFeedbackForIncorrect(FormApp.createFeedback().setText("Incorrect. With 2FA enabled, the password alone is insufficient; access requires your secret dynamic mobile code.").build());
  q11.setRequired(true);

  // Savol 12 (1 ball)
  var q12 = form.addMultipleChoiceItem();
  q12.setTitle("12. You find a brand-new, sleek USB flash drive in the schoolyard or on a desk. What is the correct cybersecurity response?");
  q12.setPoints(1);
  q12.setChoices([
    q12.createChoice("Never plug it into any personal or school computer and hand it to a teacher (BadUSB or malware threat)", true),
    q12.createChoice("Immediately plug it in to check what cool games or movies are saved on it", false),
    q12.createChoice("Quickly format it to store personal music files", false),
    q12.createChoice("Plug it into every classmate's computer one by one to test it", false)
  ]);
  q12.setFeedbackForCorrect(FormApp.createFeedback().setText("Correct! The 'dropped USB drive' is a classic hardware attack (BadUSB). Plugging it in can execute malicious keystrokes within seconds.").build());
  q12.setFeedbackForIncorrect(FormApp.createFeedback().setText("Incorrect. Never plug unknown USBs into any machine. They could be BadUSB devices designed to hijack operating systems.").build());
  q12.setRequired(true);

  // Savol 13 (1 ball)
  var q13 = form.addMultipleChoiceItem();
  q13.setTitle("13. When installing a simple flashlight or calculator app, it requests permissions for the Camera, Microphone, and Contacts. What should you do?");
  q13.setPoints(1);
  q13.setChoices([
    q13.createChoice("Deny permissions and uninstall the app immediately (a calculator does not need mic/contacts; it is likely Spyware)", true),
    q13.createChoice("Click 'Allow all', otherwise the calculator cannot compute properly", false),
    q13.createChoice("Allow only microphone access and deny the rest", false),
    q13.createChoice("Remove the battery from the smartphone", false)
  ]);
  q13.setFeedbackForCorrect(FormApp.createFeedback().setText("Excellent! The principle of least privilege: if a simple utility demands sensitive device access, it is disguised Spyware.").build());
  q13.setFeedbackForIncorrect(FormApp.createFeedback().setText("Incorrect. A calculator never needs your microphone or contact book. Granting these permissions exposes your privacy to attackers.").build());
  q13.setRequired(true);

  // Savol 14 (1 ball)
  var q14 = form.addMultipleChoiceItem();
  q14.setTitle("14. A message arrives from your classmate's Telegram profile: 'Hi, please send 50,000 UZS to this card urgently for medicine, mine is blocked.' Your first step:");
  q14.setPoints(1);
  q14.setChoices([
    q14.createChoice("Before sending money, call your classmate via voice phone to verify whether they truly sent the message", true),
    q14.createChoice("Immediately transfer the requested amount because your friend needs urgent help", false),
    q14.createChoice("Send photos of your payment card and one-time SMS verification code", false),
    q14.createChoice("Forward the message to all community chat channels", false)
  ]);
  q14.setFeedbackForCorrect(FormApp.createFeedback().setText("Well done! Compromised accounts are routinely used to broadcast emergency money requests. Always verify financial requests via direct voice call!").build());
  q14.setFeedbackForIncorrect(FormApp.createFeedback().setText("Incorrect. Transferring money blindly rewards account hijackers. Always make a direct phone call first.").build());
  q14.setRequired(true);

  // Savol 15 (1 ball)
  var q15 = form.addMultipleChoiceItem();
  q15.setTitle("15. You receive the following link: 'https://payme-uz.security-verify.click/login'. Does this address belong to the official Payme service?");
  q15.setPoints(1);
  q15.setChoices([
    q15.createChoice("No, this is a phishing scam! The actual domain is 'security-verify.click', while 'payme-uz' is merely a deceptive subdomain", true),
    q15.createChoice("Yes, because the string 'payme-uz' appears clearly at the beginning of the URL", false),
    q15.createChoice("Yes, because the padlock icon (https://) guarantees the company is genuine", false),
    q15.createChoice("If the official company logo is present on the page, the site is verified", false)
  ]);
  q15.setFeedbackForCorrect(FormApp.createFeedback().setText("Correct! Domain inspection rule: the authentic domain is directly adjacent to the TLD (payme.uz). Subdomain prefixes like payme-uz are deceptive.").build());
  q15.setFeedbackForIncorrect(FormApp.createFeedback().setText("Incorrect. HTTPS indicates encrypted transit, not administrative legitimacy. Phishers obtain free SSL certificates routinely.").build());
  q15.setRequired(true);

  // Savol 16 (1 ball)
  var q16 = form.addMultipleChoiceItem();
  q16.setTitle("16. While browsing, a red page pops up alerting: 'WARNING! 13 dangerous viruses detected on your device! Click here to clean'. What is the right response?");
  q16.setPoints(1);
  q16.setChoices([
    q16.createChoice("Close the browser tab immediately, click nothing, and download nothing (this is deceptive Scareware social engineering)", true),
    q16.createChoice("Quickly click 'Clean Now' and install the recommended application", false),
    q16.createChoice("Enter your personal mobile number and await a cleaning code", false),
    q16.createChoice("Turn off the phone and submerge it in water", false)
  ]);
  q16.setFeedbackForCorrect(FormApp.createFeedback().setText("Excellent! Standard web pages have zero access to your device file storage. Such warnings are Scareware ploys designed to trick users into installing malware.").build());
  q16.setFeedbackForIncorrect(FormApp.createFeedback().setText("Incorrect. Web pages cannot scan internal device storage. Clicking 'Clean' installs genuine malware or unauthorized subscription tools.").build());
  q16.setRequired(true);

  // Savol 17 (1 ball)
  var q17 = form.addMultipleChoiceItem();
  q17.setTitle("17. You logged into your personal account on a school desktop or a friend's laptop. What must you do before leaving?");
  q17.setPoints(1);
  q17.setChoices([
    q17.createChoice("Click 'Log out' from the account completely and ensure credentials are never saved in the browser", true),
    q17.createChoice("Simply close the browser window with the 'X' button", false),
    q17.createChoice("Click 'Save password' in the browser popup prompt", false),
    q17.createChoice("Turn off the monitor display power switch", false)
  ]);
  q17.setFeedbackForCorrect(FormApp.createFeedback().setText("Correct! Closing a tab retains active session cookies. Explicitly logging out prevents subsequent users from accessing your identity.").build());
  q17.setFeedbackForIncorrect(FormApp.createFeedback().setText("Incorrect. Closing the browser does not terminate authenticated sessions. You must click Log out to clear session credentials.").build());
  q17.setRequired(true);

  // Savol 18 (1 ball)
  var q18 = form.addMultipleChoiceItem();
  q18.setTitle("18. When your smartphone or operating system prompts you to install a 'Security Update', why is it critical not to delay it?");
  q18.setPoints(1);
  q18.setChoices([
    q18.createChoice("Because updates patch critical system vulnerabilities (flaws) and defend against emerging malware exploits", true),
    q18.createChoice("It only alters desktop wallpapers and application icon styles", false),
    q18.createChoice("Updates merely consume bandwidth and storage and should be skipped entirely", false),
    q18.createChoice("Updates permanently wipe all device photos and personal data", false)
  ]);
  q18.setFeedbackForCorrect(FormApp.createFeedback().setText("Well done! Security patches repair vulnerabilities that hackers exploit. Outdated systems remain exposed to automated network attacks.").build());
  q18.setFeedbackForIncorrect(FormApp.createFeedback().setText("Incorrect. Updates primarily seal known security holes. Postponing them leaves devices vulnerable to compromise.").build());
  q18.setRequired(true);

  // Savol 19 (1 ball)
  var q19 = form.addMultipleChoiceItem();
  q19.setTitle("19. In an online game chat, a stranger insults you and threatens to distribute your photos (cyberbullying). The correct action is:");
  q19.setPoints(1);
  q19.setChoices([
    q19.createChoice("Do not retaliate, take screenshots as evidence, block the user immediately, and report it to parents or teachers", true),
    q19.createChoice("Retaliate with worse insults and engage in an aggressive shouting match", false),
    q19.createChoice("Give in to fear and hand over account credentials or money", false),
    q19.createChoice("Keep it secret, delete the app, and suffer in silence alone", false)
  ]);
  q19.setFeedbackForCorrect(FormApp.createFeedback().setText("Correct! Never engage with trolls or bullies. Capture proof, block them, and seek trusted guidance from parents or educators immediately.").build());
  q19.setFeedbackForIncorrect(FormApp.createFeedback().setText("Incorrect. Engaging escalates hostility, and compliance invites extortion. Always inform adults and preserve evidence.").build());
  q19.setRequired(true);

  // Savol 20 (1 ball)
  var q20 = form.addMultipleChoiceItem();
  q20.setTitle("20. If your computer storage fails or gets infected by malware, what is the single guaranteed safeguard to avoid losing all your schoolwork?");
  q20.setPoints(1);
  q20.setChoices([
    q20.createChoice("Regularly keeping backups of essential files on an external drive or a secure cloud repository", true),
    q20.createChoice("Placing all important documents inside the Desktop Recycle Bin", false),
    q20.createChoice("Renaming files to 'Secret and Permanent'", false),
    q20.createChoice("Leaving the computer running indefinitely without power cycling", false)
  ]);
  q20.setFeedbackForCorrect(FormApp.createFeedback().setText("Excellent! The '3-2-1 backup rule': 3 copies, 2 media types, 1 stored offsite or in cloud. Backups make you impervious to catastrophic data loss.").build());
  q20.setFeedbackForIncorrect(FormApp.createFeedback().setText("Incorrect. Renaming or moving files to trash provides zero security. Isolated backups are the sole protection against data destruction.").build());
  q20.setRequired(true);

  Logger.log("=========================================");
  Logger.log("✅ Google Form muvaffaqiyatli yaratildi!");
  Logger.log("📌 Form Nomi: " + form.getTitle());
  Logger.log("✏️ Tahrirlash havolasi (Edit URL): " + form.getEditUrl());
  Logger.log("🌐 O'quvchilarga tarqatish havolasi (Published URL): " + form.getPublishedUrl());
  Logger.log("=========================================");
}
