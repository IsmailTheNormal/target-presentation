/**
 * Target International School — Google Forms Generator Script
 * Dars: 7–8-Sinf: 28-Dars Katta Takrorlash va Oraliq Nazorat — Kiber-Test
 * 
 * QO'LLANMA:
 * 1. https://script.new sahifasini oching.
 * 2. Ushbu fayl kodini to'liq nusxalab, script.new tahrirchisiga qo'ying.
 * 3. Tepada funksiyani tanlang (masalan, createGoogleForm_28_dars_katta_takrorlash_va_oraliq_nazorat_uz) va "Run" (▶️) tugmasini bosing.
 * 4. Google Drive ichingizda test avtomatik yaratiladi va konsolda havola chiqadi!
 */

/**
 * Target International School — Google Form Generator
 * Dars: 7–8-Sinf: 28-Dars Katta Takrorlash va Oraliq Nazorat — Kiber-Test
 * Til / Language: UZ
 */
function createGoogleForm_28_dars_katta_takrorlash_va_oraliq_nazorat_uz() {
  var form = FormApp.create("7–8-Sinf: 28-Dars Katta Takrorlash va Oraliq Nazorat — Kiber-Test");
  form.setDescription("Target International School // 7–8-Sinf // 8-Hafta // 28-Dars\nMavzu: 1-Chorak Oraliq Nazorat Testi (25 ta savol) · Canvas 2D, O'yin Tsikli, Fizika, FUT va Web API\nO'qituvchi: Ismoiljon Usmonov");
  form.setIsQuiz(true);
  form.setRequireLogin(false);
  form.setCollectEmail(true);
  form.setShowLinkToRespondAgain(false);
  form.setProgressBar(true);
  form.setShuffleQuestions(false);

  // O'quvchi ma'lumotlari
  form.addTextItem().setTitle("O'quvchining F.I.Sh. (Familiya, Ism)").setRequired(true);
  form.addListItem().setTitle("Sinfingizni tanlang:").setChoiceValues(["7-A", "7-B", "8-A", "8-B"]).setRequired(true);

  // Savol 1 (1 ball)
  var q1 = form.addMultipleChoiceItem();
  q1.setTitle("1. 1-darsga ko'ra, Katta Til Modellari (LLM) dasturlashda bizga qanday yordam beradi?");
  q1.setPoints(1);
  q1.setChoices([
    q1.createChoice("Faqat kompyuter o'yinlarini o'ynab o'tiradi.", false),
    q1.createChoice("Faqat oddiy kalkulyator vazifasini bajaradi.", false),
    q1.createChoice("Biz yozgan promptdagi talablarni tushunib, HTML, CSS va JavaScript kodlarini tezkor generatsiya qiladi.", true),
    q1.createChoice("Kompyuterdan barcha fayllarni o'chirib yuboradi.", false),
    q1.createChoice("Ular kompyuter monitorini yangilab beradi.", false)
  ]);
  q1.setFeedbackForCorrect(FormApp.createFeedback().setText("To'g'ri! LLM modellari tabiiy tildagi talablarni qabul qilib, mos dasturlash kodini tez va to'g'ri yozib beradi.").build());
  q1.setFeedbackForIncorrect(FormApp.createFeedback().setText("Xato. To'g'ri javob: C. LLM modellari tabiiy tildagi talablarni qabul qilib, mos dasturlash kodini tez va to'g'ri yozib beradi.").build());
  q1.setRequired(true);

  // Savol 2 (1 ball)
  var q2 = form.addMultipleChoiceItem();
  q2.setTitle("2. 2-darsdagi 'AI Duel' darsida AI ga qanday prompt berilsa eng yaxshi natija olinadi?");
  q2.setPoints(1);
  q2.setChoices([
    q2.createChoice("AI ga hech qanday talab bermasdan o'ziga tashlab qo'yilsa.", false),
    q2.createChoice("Faqat bitta noaniq so'z yozilsa.", false),
    q2.createChoice("Dastur nima qilishi kerakligi, qaysi tilda yozilishi va qanday tugmalar bo'lishi aniq ko'rsatilsa.", true),
    q2.createChoice("Prompt faqat qora rangda yozilsa.", false),
    q2.createChoice("Faqat kulgili stikerlar yuborilsa.", false)
  ]);
  q2.setFeedbackForCorrect(FormApp.createFeedback().setText("To'g'ri! Aniq rollar, texnologiya (HTML/CSS/JS) va qoidalar ko'rsatilgan prompt eng sifatli natijani beradi.").build());
  q2.setFeedbackForIncorrect(FormApp.createFeedback().setText("Xato. To'g'ri javob: C. Aniq rollar, texnologiya (HTML/CSS/JS) va qoidalar ko'rsatilgan prompt eng sifatli natijani beradi.").build());
  q2.setRequired(true);

  // Savol 3 (1 ball)
  var q3 = form.addMultipleChoiceItem();
  q3.setTitle("3. 3-darsda o'rganilgan SVG (Scalable Vector Graphics) formatining asosiy afzalligi nimada?");
  q3.setPoints(1);
  q3.setChoices([
    q3.createChoice("Uni brauzerda ochib bo'lmaydi.", false),
    q3.createChoice("U vektor chiziqlardan iborat bo'lgani uchun, qanchalik kattalashtirilsa ham xiralashmaydi va tiniq turadi.", true),
    q3.createChoice("U faqat qora rangda bo'ladi.", false),
    q3.createChoice("U kompyuterda 10 gigabayt joy oladi.", false),
    q3.createChoice("U faqat musiqa tinglash uchun xizmat qiladi.", false)
  ]);
  q3.setFeedbackForCorrect(FormApp.createFeedback().setText("To'g'ri! SVG pikselli rasm emas, balki matematik vektor chiziqlar bo'lib, istalgan ekranda tiniq ko'rinadi.").build());
  q3.setFeedbackForIncorrect(FormApp.createFeedback().setText("Xato. To'g'ri javob: B. SVG pikselli rasm emas, balki matematik vektor chiziqlar bo'lib, istalgan ekranda tiniq ko'rinadi.").build());
  q3.setRequired(true);

  // Savol 4 (1 ball)
  var q4 = form.addMultipleChoiceItem();
  q4.setTitle("4. 5-darsda veb-sahifaning asosiy mazmunini o'rab turish uchun qaysi semantik HTML tegi ishlatiladi?");
  q4.setPoints(1);
  q4.setChoices([
    q4.createChoice("<span>", false),
    q4.createChoice("<input>", false),
    q4.createChoice("<br>", false),
    q4.createChoice("<main>", true),
    q4.createChoice("<div>", false)
  ]);
  q4.setFeedbackForCorrect(FormApp.createFeedback().setText("To'g'ri! <main> tegi sahifaning bosh (asosiy) mazmuni qayerda joylashganini brauzerga aniq ko'rsatib beradi.").build());
  q4.setFeedbackForIncorrect(FormApp.createFeedback().setText("Xato. To'g'ri javob: D. <main> tegi sahifaning bosh (asosiy) mazmuni qayerda joylashganini brauzerga aniq ko'rsatib beradi.").build());
  q4.setRequired(true);

  // Savol 5 (1 ball)
  var q5 = form.addMultipleChoiceItem();
  q5.setTitle("5. 7-darsda CSS Flexbox da elementlarni gorizontal o'q bo'ylab markazga qo'yish uchun nima yoziladi?");
  q5.setPoints(1);
  q5.setChoices([
    q5.createChoice("float: center;", false),
    q5.createChoice("justify-content: center;", true),
    q5.createChoice("align-items: center;", false),
    q5.createChoice("text-align: middle;", false),
    q5.createChoice("display: hidden;", false)
  ]);
  q5.setFeedbackForCorrect(FormApp.createFeedback().setText("To'g'ri! Flexbox tizimida justify-content: center elementlarni gorizontal asosiy o'q markaziga tekislaydi.").build());
  q5.setFeedbackForIncorrect(FormApp.createFeedback().setText("Xato. To'g'ri javob: B. Flexbox tizimida justify-content: center elementlarni gorizontal asosiy o'q markaziga tekislaydi.").build());
  q5.setRequired(true);

  // Savol 6 (1 ball)
  var q6 = form.addMultipleChoiceItem();
  q6.setTitle("6. 8-darsda tugma bosilganini (klik qilinganini) JavaScript orqali eshitib turish qanday yoziladi?");
  q6.setPoints(1);
  q6.setChoices([
    q6.createChoice("console.clear()", false),
    q6.createChoice("button.startClick()", false),
    q6.createChoice("window.destroy()", false),
    q6.createChoice("button.addEventListener('click', () => { ... });", true),
    q6.createChoice("document.write('click')", false)
  ]);
  q6.setFeedbackForCorrect(FormApp.createFeedback().setText("To'g'ri! addEventListener('click', callback) metodi foydalanuvchi tugmani bosgan paytda funksiyani ishga tushiradi.").build());
  q6.setFeedbackForIncorrect(FormApp.createFeedback().setText("Xato. To'g'ri javob: D. addEventListener('click', callback) metodi foydalanuvchi tugmani bosgan paytda funksiyani ishga tushiradi.").build());
  q6.setRequired(true);

  // Savol 7 (1 ball)
  var q7 = form.addMultipleChoiceItem();
  q7.setTitle("7. 9-darsdagi 'Kiber-Reaksiya' mini-o'yinida o'yinchining qanday qobiliyati o'lchanadi?");
  q7.setPoints(1);
  q7.setChoices([
    q7.createChoice("O'yinchining klaviaturani qanchalik qattiq ura olishi.", false),
    q7.createChoice("Kompyuterning internet tezligi.", false),
    q7.createChoice("Ekran yashil rangga kirgan zahoti tugmani qanchalik tez bosishi, ya'ni reaktsiya vaqti.", true),
    q7.createChoice("Sichqonchaning qanchalik og'irligi.", false),
    q7.createChoice("O'yinchining inglizcha so'zlarni qanchalik tez o'qishi.", false)
  ]);
  q7.setFeedbackForCorrect(FormApp.createFeedback().setText("To'g'ri! Kiber-Reaksiya o'yini ekranda signal berilishi bilan o'yinchining reaksiyasini millisekundlarda o'lchaydi.").build());
  q7.setFeedbackForIncorrect(FormApp.createFeedback().setText("Xato. To'g'ri javob: C. Kiber-Reaksiya o'yini ekranda signal berilishi bilan o'yinchining reaksiyasini millisekundlarda o'lchaydi.").build());
  q7.setRequired(true);

  // Savol 8 (1 ball)
  var q8 = form.addMultipleChoiceItem();
  q8.setTitle("8. 10-darsda brauzerda dastur kodidagi xatolar va console.log natijalari qayerda ko'rinadi?");
  q8.setPoints(1);
  q8.setChoices([
    q8.createChoice("Faqat Word dasturida.", false),
    q8.createChoice("Brauzer DevTools ning 'Console' (Konsol) panelida.", true),
    q8.createChoice("Hech qayerda ko'rinmaydi.", false),
    q8.createChoice("Kompyuterning 'Mening kompyuterim' papkasida.", false),
    q8.createChoice("Telefon ekranida.", false)
  ]);
  q8.setFeedbackForCorrect(FormApp.createFeedback().setText("To'g'ri! Dasturchilar kodni sinash va xatolarni aniqlash uchun brauzerning Console oynasiga qaraydi.").build());
  q8.setFeedbackForIncorrect(FormApp.createFeedback().setText("Xato. To'g'ri javob: B. Dasturchilar kodni sinash va xatolarni aniqlash uchun brauzerning Console oynasiga qaraydi.").build());
  q8.setRequired(true);

  // Savol 9 (1 ball)
  var q9 = form.addMultipleChoiceItem();
  q9.setTitle("9. 11-darsda LocalStorage ga saqlangan o'yin rekordlari qachon o'chib ketadi?");
  q9.setPoints(1);
  q9.setChoices([
    q9.createChoice("Faqat kompyuter zaryadi tugaganda o'chadi.", false),
    q9.createChoice("Klaviatura bosilishi bilan o'chadi.", false),
    q9.createChoice("Har 5 soniyada avtomatik o'chib turadi.", false),
    q9.createChoice("O'chib ketmaydi: sahifa qayta yangilanganda ham, brauzer yopilib qayta ochilganda ham saqlanib turadi.", true),
    q9.createChoice("Brauzer oynasi yopilishi bilan darhol o'chadi.", false)
  ]);
  q9.setFeedbackForCorrect(FormApp.createFeedback().setText("To'g'ri! LocalStorage ma'lumotlarni uzoq muddat saqlaydi, shuning uchun rekord ballar yo'qolmaydi.").build());
  q9.setFeedbackForIncorrect(FormApp.createFeedback().setText("Xato. To'g'ri javob: D. LocalStorage ma'lumotlarni uzoq muddat saqlaydi, shuning uchun rekord ballar yo'qolmaydi.").build());
  q9.setRequired(true);

  // Savol 10 (1 ball)
  var q10 = form.addMultipleChoiceItem();
  q10.setTitle("10. 12-darsda o'yinni do'stlarga havola orqali ulashish uchun Vercel xizmatiga yuklaganda qaysi xavfsiz protokol beriladi?");
  q10.setPoints(1);
  q10.setChoices([
    q10.createChoice("Faqat Bluetooth aloqasi.", false),
    q10.createChoice("Faqat kabel orqali ulanish.", false),
    q10.createChoice("Faqat kompyuter ichidagi localhost.", false),
    q10.createChoice("Yashil qulf belgili xavfsiz HTTPS va bepul SSL sertifikati.", true),
    q10.createChoice("Oddiy shifrlanmagan HTTP.", false)
  ]);
  q10.setFeedbackForCorrect(FormApp.createFeedback().setText("To'g'ri! Vercel o'yinni butun dunyo ochishi uchun avtomatik ravishda xavfsiz HTTPS havolasini taqdim etadi.").build());
  q10.setFeedbackForIncorrect(FormApp.createFeedback().setText("Xato. To'g'ri javob: D. Vercel o'yinni butun dunyo ochishi uchun avtomatik ravishda xavfsiz HTTPS havolasini taqdim etadi.").build());
  q10.setRequired(true);

  // Savol 11 (1 ball)
  var q11 = form.addMultipleChoiceItem();
  q11.setTitle("11. 13-darsda JavaScript orqali 2D o'yin grafikasi chiziladigan maxsus HTML tegi qaysi?");
  q11.setPoints(1);
  q11.setChoices([
    q11.createChoice("<canvas>", true),
    q11.createChoice("<audio>", false),
    q11.createChoice("<button>", false),
    q11.createChoice("<table>", false),
    q11.createChoice("<link>", false)
  ]);
  q11.setFeedbackForCorrect(FormApp.createFeedback().setText("To'g'ri! <canvas> tegi JavaScript yordamida qahramonlar, to'siqlar va 2D o'yinlarni chizish maydonidir.").build());
  q11.setFeedbackForIncorrect(FormApp.createFeedback().setText("Xato. To'g'ri javob: A. <canvas> tegi JavaScript yordamida qahramonlar, to'siqlar va 2D o'yinlarni chizish maydonidir.").build());
  q11.setRequired(true);

  // Savol 12 (1 ball)
  var q12 = form.addMultipleChoiceItem();
  q12.setTitle("12. 13-darsda o'yin soniyasiga 60 kadr (60 FPS) silliq harakatlanishi uchun qaysi funksiya chaqiriladi?");
  q12.setPoints(1);
  q12.setChoices([
    q12.createChoice("requestAnimationFrame(gameLoop);", true),
    q12.createChoice("alert('kadr');", false),
    q12.createChoice("window.close();", false),
    q12.createChoice("setInterval(update, 5000);", false),
    q12.createChoice("document.clear();", false)
  ]);
  q12.setFeedbackForCorrect(FormApp.createFeedback().setText("To'g'ri! requestAnimationFrame ekranning yangilanishiga moslashib, harakatlarni qotmasdan silliq (60 FPS) chizadi.").build());
  q12.setFeedbackForIncorrect(FormApp.createFeedback().setText("Xato. To'g'ri javob: A. requestAnimationFrame ekranning yangilanishiga moslashib, harakatlarni qotmasdan silliq (60 FPS) chizadi.").build());
  q12.setRequired(true);

  // Savol 13 (1 ball)
  var q13 = form.addMultipleChoiceItem();
  q13.setTitle("13. 14-darsda o'yinda yangi paydo bo'lgan dushmanni dushmanlar massiviga qo'shish uchun qaysi metod ishlatiladi?");
  q13.setPoints(1);
  q13.setChoices([
    q13.createChoice("enemies.reverse()", false),
    q13.createChoice("enemies.pop()", false),
    q13.createChoice("enemies.slice()", false),
    q13.createChoice("enemies.push(newEnemy)", true),
    q13.createChoice("enemies.clear()", false)
  ]);
  q13.setFeedbackForCorrect(FormApp.createFeedback().setText("To'g'ri! Massivning .push() metodi yangi elementni (yangi dushmanni) massivning oxiriga qo'shadi.").build());
  q13.setFeedbackForIncorrect(FormApp.createFeedback().setText("Xato. To'g'ri javob: D. Massivning .push() metodi yangi elementni (yangi dushmanni) massivning oxiriga qo'shadi.").build());
  q13.setRequired(true);

  // Savol 14 (1 ball)
  var q14 = form.addMultipleChoiceItem();
  q14.setTitle("14. 15-darsda platformer o'yinida qahramon sakragandan so'ng yerga qaytib tushishini nima ta'minlaydi?");
  q14.setPoints(1);
  q14.setChoices([
    q14.createChoice("Faqat o'yin musiqasi.", false),
    q14.createChoice("Gravitatsiya (tortishish kuchi) simulyatsiyasi.", true),
    q14.createChoice("Klaviatura tugmalari soni.", false),
    q14.createChoice("Kompyuter ekranining yorug'ligi.", false),
    q14.createChoice("O'yinchi sichqonchasining tezligi.", false)
  ]);
  q14.setFeedbackForCorrect(FormApp.createFeedback().setText("To'g'ri! Gravitatsiya kuchi qahramon sakraganda uni pastga tortib, tabiiy tushish harakatini hosil qiladi.").build());
  q14.setFeedbackForIncorrect(FormApp.createFeedback().setText("Xato. To'g'ri javob: B. Gravitatsiya kuchi qahramon sakraganda uni pastga tortib, tabiiy tushish harakatini hosil qiladi.").build());
  q14.setRequired(true);

  // Savol 15 (1 ball)
  var q15 = form.addMultipleChoiceItem();
  q15.setTitle("15. 15-darsda qahramon tangaga yoki dushmanga tekkanini o'yin kodi qanday biladi?");
  q15.setPoints(1);
  q15.setChoices([
    q15.createChoice("To'qnashuv (Collision) tekshiruvi orqali: qahramon va obyekt chegaralari ustma-ust tushganda.", true),
    q15.createChoice("Faqat ikkala obyektning rangi bir xil bo'lganda.", false),
    q15.createChoice("O'yin vaqti tugaganda.", false),
    q15.createChoice("Qahramon to'xtab qolganda.", false),
    q15.createChoice("Faqat sichqoncha bilan bosilganda.", false)
  ]);
  q15.setFeedbackForCorrect(FormApp.createFeedback().setText("To'g'ri! To'qnashuv algoritmi qahramon va tanga koordinatalari kesishganini tekshirib, tegishni aniqlaydi.").build());
  q15.setFeedbackForIncorrect(FormApp.createFeedback().setText("Xato. To'g'ri javob: A. To'qnashuv algoritmi qahramon va tanga koordinatalari kesishganini tekshirib, tegishni aniqlaydi.").build());
  q15.setRequired(true);

  // Savol 16 (1 ball)
  var q16 = form.addMultipleChoiceItem();
  q16.setTitle("16. 17-darsda tashqi audio fayllarsiz toza ovoz effektlarini generatsiya qiluvchi brauzer vositasi nima?");
  q16.setPoints(1);
  q16.setChoices([
    q16.createChoice("Faqat video pleyer.", false),
    q16.createChoice("Faqat mikrofon kabeli.", false),
    q16.createChoice("Web Audio API (AudioContext va OscillatorNode).", true),
    q16.createChoice("Faqat telefon qo'ng'irog'i.", false),
    q16.createChoice("Faqat kompyuter klaviaturasi.", false)
  ]);
  q16.setFeedbackForCorrect(FormApp.createFeedback().setText("To'g'ri! Web Audio API dinamiklar orqali to'g'ridan-to'g'ri tovush to'lqinlarini (sinus, kvadrat) sintez qiladi.").build());
  q16.setFeedbackForIncorrect(FormApp.createFeedback().setText("Xato. To'g'ri javob: C. Web Audio API dinamiklar orqali to'g'ridan-to'g'ri tovush to'lqinlarini (sinus, kvadrat) sintez qiladi.").build());
  q16.setRequired(true);

  // Savol 17 (1 ball)
  var q17 = form.addMultipleChoiceItem();
  q17.setTitle("17. 18-darsda qahramon katta xarita bo'ylab yugurganida kamera nima qiladi?");
  q17.setPoints(1);
  q17.setChoices([
    q17.createChoice("Qahramon orqasidan ergashib siljiydi (Camera Scrolling) va yangi yo'llarni ko'rsatib boradi.", true),
    q17.createChoice("Kompyuter ekranini o'chirib qo'yadi.", false),
    q17.createChoice("Qahramonni ekranning chetida to'xtatib qo'yadi.", false),
    q17.createChoice("O'yinni boshidan boshlaydi.", false),
    q17.createChoice("O'yinni butunlay to'xtatadi.", false)
  ]);
  q17.setFeedbackForCorrect(FormApp.createFeedback().setText("To'g'ri! Kamera skrollingi qahramonni markazda ushlab, orqa fon va dunyoni siljitib ko'rsatadi.").build());
  q17.setFeedbackForIncorrect(FormApp.createFeedback().setText("Xato. To'g'ri javob: A. Kamera skrollingi qahramonni markazda ushlab, orqa fon va dunyoni siljitib ko'rsatadi.").build());
  q17.setRequired(true);

  // Savol 18 (1 ball)
  var q18 = form.addMultipleChoiceItem();
  q18.setTitle("18. 19-darsda smartfon sensor ekraniga barmoq tekkan paytda qaysi hodisa ishga tushadi?");
  q18.setPoints(1);
  q18.setChoices([
    q18.createChoice("onsubmit", false),
    q18.createChoice("onhover", false),
    q18.createChoice("mouseleave", false),
    q18.createChoice("keypress", false),
    q18.createChoice("touchstart", true)
  ]);
  q18.setFeedbackForCorrect(FormApp.createFeedback().setText("To'g'ri! Mobil qurilmalarda ekranga barmoq tekkanda 'touchstart', siljitganda 'touchmove', olganda 'touchend' sodir bo'ladi.").build());
  q18.setFeedbackForIncorrect(FormApp.createFeedback().setText("Xato. To'g'ri javob: E. Mobil qurilmalarda ekranga barmoq tekkanda 'touchstart', siljitganda 'touchmove', olganda 'touchend' sodir bo'ladi.").build());
  q18.setRequired(true);

  // Savol 19 (1 ball)
  var q19 = form.addMultipleChoiceItem();
  q19.setTitle("19. 21-darsdagi 'FUT Card Studio' loyihasida o'yinchining OVR qisqartmasi nimani bildiradi?");
  q19.setPoints(1);
  q19.setChoices([
    q19.createChoice("Futbolchining telefon raqami.", false),
    q19.createChoice("Overall Rating — futbolchi kartasining umumiy mahorat reytingi bali.", true),
    q19.createChoice("O'yin vaqti.", false),
    q19.createChoice("Kartaning narxi.", false),
    q19.createChoice("Futbolchining oyoq kiyimi o'lchami.", false)
  ]);
  q19.setFeedbackForCorrect(FormApp.createFeedback().setText("To'g'ri! OVR (Overall Rating) — futbolchining tezligi, zarbasi va uzatmalari asosida hisoblangan umumiy mahorat bali.").build());
  q19.setFeedbackForIncorrect(FormApp.createFeedback().setText("Xato. To'g'ri javob: B. OVR (Overall Rating) — futbolchining tezligi, zarbasi va uzatmalari asosida hisoblangan umumiy mahorat bali.").build());
  q19.setRequired(true);

  // Savol 20 (1 ball)
  var q20 = form.addMultipleChoiceItem();
  q20.setTitle("20. 22-darsdagi 'FUT Squad Builder' loyihasida bir xil klubdagi futbolchilar birgalikda o'ynasa nima bo'ladi?");
  q20.setPoints(1);
  q20.setChoices([
    q20.createChoice("Ikkala futbolchi ham qizil kartochka oladi.", false),
    q20.createChoice("Futbolchilar jamoadan chiqib ketadi.", false),
    q20.createChoice("Ularning kiyim raqami o'zgaradi.", false),
    q20.createChoice("O'yin to'xtab qoladi.", false),
    q20.createChoice("Ularning orasida klub aloqasi bog'lanib, jamoaning Kimyo (Chemistry) bali maksimal darajada oshadi.", true)
  ]);
  q20.setFeedbackForCorrect(FormApp.createFeedback().setText("To'g'ri! Bir xil klubdagi futbolchilar eng kuchli aloqa hosil qilib, butun jamoaning o'yin sifatini oshiradi.").build());
  q20.setFeedbackForIncorrect(FormApp.createFeedback().setText("Xato. To'g'ri javob: E. Bir xil klubdagi futbolchilar eng kuchli aloqa hosil qilib, butun jamoaning o'yin sifatini oshiradi.").build());
  q20.setRequired(true);

  // Savol 21 (1 ball)
  var q21 = form.addMultipleChoiceItem();
  q21.setTitle("21. 24-darsda FUT Transfer bozorida EA nega har bir sotuvdan 5% soliq (Coin Sink) oladi?");
  q21.setPoints(1);
  q21.setChoices([
    q21.createChoice("O'yinchilarni xafa qilish uchun.", false),
    q21.createChoice("Kompyuterlarni tozalash uchun.", false),
    q21.createChoice("Barcha o'yinchilarni tekin qilish uchun.", false),
    q21.createChoice("O'yinda virtual pullar haddan tashqari ko'payib ketmasligi va narxlar oshib ketmasligi (inflyatsiyani to'xtatish) uchun.", true),
    q21.createChoice("Haqiqiy do'kondan kiyim sotib olish uchun.", false)
  ]);
  q21.setFeedbackForCorrect(FormApp.createFeedback().setText("To'g'ri! 5% transfer solig'i (Coin Sink) iqtisodiyotdagi ortiqcha tangalarni yo'qotib, narxlarni barqaror ushlab turadi.").build());
  q21.setFeedbackForIncorrect(FormApp.createFeedback().setText("Xato. To'g'ri javob: D. 5% transfer solig'i (Coin Sink) iqtisodiyotdagi ortiqcha tangalarni yo'qotib, narxlarni barqaror ushlab turadi.").build());
  q21.setRequired(true);

  // Savol 22 (1 ball)
  var q22 = form.addMultipleChoiceItem();
  q22.setTitle("22. 25-darsdagi 'Target Jarvis' sun'iy intellektida ovozni matnga aylantirish uchun qaysi Web API ishlatildi?");
  q22.setPoints(1);
  q22.setChoices([
    q22.createChoice("window.alert()", false),
    q22.createChoice("navigator.vibrate()", false),
    q22.createChoice("Web Speech API (SpeechRecognition).", true),
    q22.createChoice("localStorage.clear()", false),
    q22.createChoice("document.body.remove()", false)
  ]);
  q22.setFeedbackForCorrect(FormApp.createFeedback().setText("To'g'ri! SpeechRecognition interfeysi mikrofon orqali aytilgan so'zlarni taniydi va ularni matn shaklida dasturga uzatadi.").build());
  q22.setFeedbackForIncorrect(FormApp.createFeedback().setText("Xato. To'g'ri javob: C. SpeechRecognition interfeysi mikrofon orqali aytilgan so'zlarni taniydi va ularni matn shaklida dasturga uzatadi.").build());
  q22.setRequired(true);

  // Savol 23 (1 ball)
  var q23 = form.addMultipleChoiceItem();
  q23.setTitle("23. 26-darsda 'Kiber-Ko'z' veb-kamera orqali xonadagi harakatni qanday payqaydi?");
  q23.setPoints(1);
  q23.setChoices([
    q23.createChoice("Kameraning oldingi va keyingi kadrlari orasidagi piksellarning rang o'zgarishini taqqoslash orqali.", true),
    q23.createChoice("Xonadagi havo haroratini o'lchash orqali.", false),
    q23.createChoice("Faqat sichqoncha qimirlaganda.", false),
    q23.createChoice("Ekranni qora qilib qo'yish orqali.", false),
    q23.createChoice("Faqat odamning ismini chaqirish orqali.", false)
  ]);
  q23.setFeedbackForCorrect(FormApp.createFeedback().setText("To'g'ri! Harakat detektori kadrlar orasidagi piksellar farqini hisoblaydi: agar o'zgargan piksellar ko'p bo'lsa, demak harakat bor.").build());
  q23.setFeedbackForIncorrect(FormApp.createFeedback().setText("Xato. To'g'ri javob: A. Harakat detektori kadrlar orasidagi piksellar farqini hisoblaydi: agar o'zgargan piksellar ko'p bo'lsa, demak harakat bor.").build());
  q23.setRequired(true);

  // Savol 24 (1 ball)
  var q24 = form.addMultipleChoiceItem();
  q24.setTitle("24. 27-darsda Biometrik Face ID tizimi insonni qaysi belgilari orqali taniydi?");
  q24.setPoints(1);
  q24.setChoices([
    q24.createChoice("Insonning kiygan kiyimi rangi orqali.", false),
    q24.createChoice("Foydalanuvchining telefon raqami orqali.", false),
    q24.createChoice("Faqat poyabzal o'lchami orqali.", false),
    q24.createChoice("Faqat insonning bo'yi uzunligi orqali.", false),
    q24.createChoice("Inson yuzining tuzilishi, ko'zlar, burun va qoshlar orasidagi masofalar (Face Landmarks) orqali.", true)
  ]);
  q24.setFeedbackForCorrect(FormApp.createFeedback().setText("To'g'ri! Face ID yuzdagi o'nlab nuqtalarni (Landmarks) skanerlab, har bir insonning o'ziga xos yuz xaritasini tekshiradi.").build());
  q24.setFeedbackForIncorrect(FormApp.createFeedback().setText("Xato. To'g'ri javob: E. Face ID yuzdagi o'nlab nuqtalarni (Landmarks) skanerlab, har bir insonning o'ziga xos yuz xaritasini tekshiradi.").build());
  q24.setRequired(true);

  // Savol 25 (1 ball)
  var q25 = form.addMultipleChoiceItem();
  q25.setTitle("25. 7–8-sinf Vibecoding dasturchisining eng asosiy ko'nikmasi nima?");
  q25.setPoints(1);
  q25.setChoices([
    q25.createChoice("Faqat bitta tugmali o'yinlar yasash.", false),
    q25.createChoice("Kodni tushunmasdan ko'chirib olish.", false),
    q25.createChoice("Hech qachon o'z loyihasini internetga chiqarmaslik.", false),
    q25.createChoice("Kiber-xavfsizlik qoidalarini e'tiborsiz qoldirish.", false),
    q25.createChoice("G'oyani interaktiv veb-sayt yoki 2D o'yinga aylantirish, AI yordamida kod yozish va xatolarni mustaqil to'g'rilash.", true)
  ]);
  q25.setFeedbackForCorrect(FormApp.createFeedback().setText("To'g'ri! 7-8 sinf o'quvchisi interaktiv ilovalar yarata oladi, DevTools bilan xatolarni topadi va zamonaviy veb-texnologiyalardan foydalanadi.").build());
  q25.setFeedbackForIncorrect(FormApp.createFeedback().setText("Xato. To'g'ri javob: E. 7-8 sinf o'quvchisi interaktiv ilovalar yarata oladi, DevTools bilan xatolarni topadi va zamonaviy veb-texnologiyalardan foydalanadi.").build());
  q25.setRequired(true);

  Logger.log("✓ Google Form (UZ) yaratildi: " + form.getEditUrl());
  Logger.log("✓ O'quvchilar uchun havola: " + form.getPublishedUrl());
}

/**
 * Target International School — Google Form Generator
 * Урок: 7–8-Класс: 28-Урок Большое повторение и рубежный контроль — Кибер-Тест
 * Язык / Language: RU
 */
function createGoogleForm_28_dars_katta_takrorlash_va_oraliq_nazorat_ru() {
  var form = FormApp.create("7–8-Класс: 28-Урок Большое повторение и рубежный контроль — Кибер-Тест");
  form.setDescription("Target International School // 7–8-Класс // 8-Неделя // 28-Урок\nТема: Рубежный тест за 1-ю четверть (25 вопросов) · Canvas 2D, Игровой цикл, Физика, FUT и Web API\nПреподаватель: Исмоилжон Усмонов");
  form.setIsQuiz(true);
  form.setRequireLogin(false);
  form.setCollectEmail(true);
  form.setShowLinkToRespondAgain(false);
  form.setProgressBar(true);
  form.setShuffleQuestions(false);

  // Данные ученика
  form.addTextItem().setTitle("Ф.И.О. Ученика").setRequired(true);
  form.addListItem().setTitle("Выберите ваш класс:").setChoiceValues(["7-A", "7-B", "8-A", "8-B"]).setRequired(true);

  // Вопрос 1 (1 балл)
  var q1 = form.addMultipleChoiceItem();
  q1.setTitle("1. Согласно Уроку 1, как Большие Языковые Модели (LLM) помогают нам в веб-разработке?");
  q1.setPoints(1);
  q1.setChoices([
    q1.createChoice("Они просто играют в компьютерные игры вместо нас.", false),
    q1.createChoice("Они работают исключительно как простейший калькулятор.", false),
    q1.createChoice("Они понимают задачи из нашего промпта и быстро генерируют рабочий код на HTML, CSS и JavaScript.", true),
    q1.createChoice("Они удаляют все системные файлы с компьютера.", false),
    q1.createChoice("Они протирают монитор от пыли.", false)
  ]);
  q1.setFeedbackForCorrect(FormApp.createFeedback().setText("Верно! LLM понимают инструкции на человеческом языке и мгновенно создают рабочий код веб-приложений и игр.").build());
  q1.setFeedbackForIncorrect(FormApp.createFeedback().setText("Неверно. Правильный ответ: C. LLM понимают инструкции на человеческом языке и мгновенно создают рабочий код веб-приложений и игр.").build());
  q1.setRequired(true);

  // Вопрос 2 (1 балл)
  var q2 = form.addMultipleChoiceItem();
  q2.setTitle("2. Как правильно составить промпт на Уроке 2 ('AI Duel'), чтобы получить самый качественный и точный код?");
  q2.setPoints(1);
  q2.setChoices([
    q2.createChoice("Не давать никаких инструкций и ждать чуда.", false),
    q2.createChoice("Написать всего одно размытое слово.", false),
    q2.createChoice("Четко описать, что должна делать программа, какие языки использовать (HTML/CSS/JS) и какие кнопки должны быть.", true),
    q2.createChoice("Писать промпт только черными буквами.", false),
    q2.createChoice("Отправлять нейросети только смайлики.", false)
  ]);
  q2.setFeedbackForCorrect(FormApp.createFeedback().setText("Верно! Четкое описание интерфейса, логики и используемого стека гарантирует получение качественного кода с первой попытки.").build());
  q2.setFeedbackForIncorrect(FormApp.createFeedback().setText("Неверно. Правильный ответ: C. Четкое описание интерфейса, логики и используемого стека гарантирует получение качественного кода с первой попытки.").build());
  q2.setRequired(true);

  // Вопрос 3 (1 балл)
  var q3 = form.addMultipleChoiceItem();
  q3.setTitle("3. В чем заключается главное преимущество векторной графики SVG (Урок 3)?");
  q3.setPoints(1);
  q3.setChoices([
    q3.createChoice("Ее невозможно открыть в браузере.", false),
    q3.createChoice("Она состоит из математических линий, поэтому не размывается и остается четкой при любом увеличении экрана.", true),
    q3.createChoice("Она бывает исключительно черного цвета.", false),
    q3.createChoice("Она занимает на диске 10 гигабайт.", false),
    q3.createChoice("Она используется только для прослушивания музыки.", false)
  ]);
  q3.setFeedbackForCorrect(FormApp.createFeedback().setText("Верно! SVG масштабируется без потери качества на любых экранах, так как строится на векторах, а не на пикселях.").build());
  q3.setFeedbackForIncorrect(FormApp.createFeedback().setText("Неверно. Правильный ответ: B. SVG масштабируется без потери качества на любых экранах, так как строится на векторах, а не на пикселях.").build());
  q3.setRequired(true);

  // Вопрос 4 (1 балл)
  var q4 = form.addMultipleChoiceItem();
  q4.setTitle("4. Какой семантический тег HTML используется на Уроке 5 для выделения основного контента страницы?");
  q4.setPoints(1);
  q4.setChoices([
    q4.createChoice("<span>", false),
    q4.createChoice("<input>", false),
    q4.createChoice("<br>", false),
    q4.createChoice("<main>", true),
    q4.createChoice("<div>", false)
  ]);
  q4.setFeedbackForCorrect(FormApp.createFeedback().setText("Верно! Тег <main> четко указывает браузеру и поисковикам, где расположена ключевая смысловая часть страницы.").build());
  q4.setFeedbackForIncorrect(FormApp.createFeedback().setText("Неверно. Правильный ответ: D. Тег <main> четко указывает браузеру и поисковикам, где расположена ключевая смысловая часть страницы.").build());
  q4.setRequired(true);

  // Вопрос 5 (1 балл)
  var q5 = form.addMultipleChoiceItem();
  q5.setTitle("5. Какое свойство CSS Flexbox центрирует элементы вдоль главной горизонтальной оси (Урок 7)?");
  q5.setPoints(1);
  q5.setChoices([
    q5.createChoice("float: center;", false),
    q5.createChoice("justify-content: center;", true),
    q5.createChoice("align-items: center;", false),
    q5.createChoice("text-align: middle;", false),
    q5.createChoice("display: hidden;", false)
  ]);
  q5.setFeedbackForCorrect(FormApp.createFeedback().setText("Верно! Свойство justify-content: center выравнивает дочерние элементы точно по центру вдоль главной оси строки.").build());
  q5.setFeedbackForIncorrect(FormApp.createFeedback().setText("Неверно. Правильный ответ: B. Свойство justify-content: center выравнивает дочерние элементы точно по центру вдоль главной оси строки.").build());
  q5.setRequired(true);

  // Вопрос 6 (1 балл)
  var q6 = form.addMultipleChoiceItem();
  q6.setTitle("6. Как в коде JavaScript слушать нажатие (клик) по кнопке (Урок 8)?");
  q6.setPoints(1);
  q6.setChoices([
    q6.createChoice("console.clear()", false),
    q6.createChoice("button.startClick()", false),
    q6.createChoice("window.destroy()", false),
    q6.createChoice("button.addEventListener('click', () => { ... });", true),
    q6.createChoice("document.write('click')", false)
  ]);
  q6.setFeedbackForCorrect(FormApp.createFeedback().setText("Верно! Метод addEventListener('click', fn) вешает слушатель события, реагируя на каждый щелчок мыши.").build());
  q6.setFeedbackForIncorrect(FormApp.createFeedback().setText("Неверно. Правильный ответ: D. Метод addEventListener('click', fn) вешает слушатель события, реагируя на каждый щелчок мыши.").build());
  q6.setRequired(true);

  // Вопрос 7 (1 балл)
  var q7 = form.addMultipleChoiceItem();
  q7.setTitle("7. Какую способность игрока измеряет мини-игра 'Кибер-Реакция' на Уроке 9?");
  q7.setPoints(1);
  q7.setChoices([
    q7.createChoice("Силу удара пальцем по клавиатуре.", false),
    q7.createChoice("Скорость интернет-соединения в комнате.", false),
    q7.createChoice("Скорость реакции: насколько быстро игрок успевает нажать на кнопку после того, как экран стал зеленым.", true),
    q7.createChoice("Вес компьютерной мышки.", false),
    q7.createChoice("Скорость чтения текста на английском языке.", false)
  ]);
  q7.setFeedbackForCorrect(FormApp.createFeedback().setText("Верно! Игра замеряет время между появлением зеленого сигнала и кликом игрока в миллисекундах.").build());
  q7.setFeedbackForIncorrect(FormApp.createFeedback().setText("Неверно. Правильный ответ: C. Игра замеряет время между появлением зеленого сигнала и кликом игрока в миллисекундах.").build());
  q7.setRequired(true);

  // Вопрос 8 (1 балл)
  var q8 = form.addMultipleChoiceItem();
  q8.setTitle("8. Где в браузере разработчик смотрит ошибки JavaScript и выводы функции console.log (Урок 10)?");
  q8.setPoints(1);
  q8.setChoices([
    q8.createChoice("Только в программе Microsoft Word.", false),
    q8.createChoice("На вкладке 'Console' (Консоль) в панели DevTools браузера.", true),
    q8.createChoice("Они нигде не отображаются.", false),
    q8.createChoice("В папке 'Мой компьютер'.", false),
    q8.createChoice("На экране смартфона.", false)
  ]);
  q8.setFeedbackForCorrect(FormApp.createFeedback().setText("Верно! Консоль браузера (F12 -> Console) — главное рабочее место для поиска багов и проверки работы скриптов.").build());
  q8.setFeedbackForIncorrect(FormApp.createFeedback().setText("Неверно. Правильный ответ: B. Консоль браузера (F12 -> Console) — главное рабочее место для поиска багов и проверки работы скриптов.").build());
  q8.setRequired(true);

  // Вопрос 9 (1 балл)
  var q9 = form.addMultipleChoiceItem();
  q9.setTitle("9. Когда стираются рекорды игры, сохраненные в LocalStorage (Урок 11)?");
  q9.setPoints(1);
  q9.setChoices([
    q9.createChoice("Только когда в ноутбуке садится батарейка.", false),
    q9.createChoice("Они удаляются при первом нажатии пробела.", false),
    q9.createChoice("Они автоматически стираются каждые 5 секунд.", false),
    q9.createChoice("Они не стираются: сохраняются даже при перезагрузке страницы и закрытии браузера.", true),
    q9.createChoice("Они стираются сразу же при закрытии вкладки браузера.", false)
  ]);
  q9.setFeedbackForCorrect(FormApp.createFeedback().setText("Верно! LocalStorage надежно хранит рекорды на диске браузера, позволяя возвращаться к игре в любое время.").build());
  q9.setFeedbackForIncorrect(FormApp.createFeedback().setText("Неверно. Правильный ответ: D. LocalStorage надежно хранит рекорды на диске браузера, позволяя возвращаться к игре в любое время.").build());
  q9.setRequired(true);

  // Вопрос 10 (1 балл)
  var q10 = form.addMultipleChoiceItem();
  q10.setTitle("10. Какой протокол безопасности автоматически выдается при публикации игры на платформе Vercel (Урок 12)?");
  q10.setPoints(1);
  q10.setChoices([
    q10.createChoice("Только беспроводной Bluetooth.", false),
    q10.createChoice("Только проводной кабель.", false),
    q10.createChoice("Только локальный localhost.", false),
    q10.createChoice("Безопасный протокол HTTPS с зеленым значком замка и сертификатом SSL.", true),
    q10.createChoice("Устаревший незашифрованный HTTP.", false)
  ]);
  q10.setFeedbackForCorrect(FormApp.createFeedback().setText("Верно! Vercel автоматически защищает проект бесплатным SSL-сертификатом, делая ссылку общедоступной и безопасной.").build());
  q10.setFeedbackForIncorrect(FormApp.createFeedback().setText("Неверно. Правильный ответ: D. Vercel автоматически защищает проект бесплатным SSL-сертификатом, делая ссылку общедоступной и безопасной.").build());
  q10.setRequired(true);

  // Вопрос 11 (1 балл)
  var q11 = form.addMultipleChoiceItem();
  q11.setTitle("11. Какой HTML-тег предназначен для рисования 2D игр с помощью JavaScript (Урок 13)?");
  q11.setPoints(1);
  q11.setChoices([
    q11.createChoice("<canvas>", true),
    q11.createChoice("<audio>", false),
    q11.createChoice("<button>", false),
    q11.createChoice("<table>", false),
    q11.createChoice("<link>", false)
  ]);
  q11.setFeedbackForCorrect(FormApp.createFeedback().setText("Верно! Тег <canvas> — это интерактивный холст, на котором скрипт рисует графику, персонажей и физику игры.").build());
  q11.setFeedbackForIncorrect(FormApp.createFeedback().setText("Неверно. Правильный ответ: A. Тег <canvas> — это интерактивный холст, на котором скрипт рисует графику, персонажей и физику игры.").build());
  q11.setRequired(true);

  // Вопрос 12 (1 балл)
  var q12 = form.addMultipleChoiceItem();
  q12.setTitle("12. Какая функция обеспечивает плавную анимацию игры со скоростью 60 кадров в секунду (60 FPS) на Уроке 13?");
  q12.setPoints(1);
  q12.setChoices([
    q12.createChoice("requestAnimationFrame(gameLoop);", true),
    q12.createChoice("alert('кадр');", false),
    q12.createChoice("window.close();", false),
    q12.createChoice("setInterval(update, 5000);", false),
    q12.createChoice("document.clear();", false)
  ]);
  q12.setFeedbackForCorrect(FormApp.createFeedback().setText("Верно! requestAnimationFrame синхронизируется с частотой развертки монитора, обеспечивая идеальную плавность.").build());
  q12.setFeedbackForIncorrect(FormApp.createFeedback().setText("Неверно. Правильный ответ: A. requestAnimationFrame синхронизируется с частотой развертки монитора, обеспечивая идеальную плавность.").build());
  q12.setRequired(true);

  // Вопрос 13 (1 балл)
  var q13 = form.addMultipleChoiceItem();
  q13.setTitle("13. Какой метод массива в JavaScript добавляет вновь появившегося врага в список врагов (Урок 14)?");
  q13.setPoints(1);
  q13.setChoices([
    q13.createChoice("enemies.reverse()", false),
    q13.createChoice("enemies.pop()", false),
    q13.createChoice("enemies.slice()", false),
    q13.createChoice("enemies.push(newEnemy)", true),
    q13.createChoice("enemies.clear()", false)
  ]);
  q13.setFeedbackForCorrect(FormApp.createFeedback().setText("Верно! Метод .push() добавляет новый элемент в конец массива объектов.").build());
  q13.setFeedbackForIncorrect(FormApp.createFeedback().setText("Неверно. Правильный ответ: D. Метод .push() добавляет новый элемент в конец массива объектов.").build());
  q13.setRequired(true);

  // Вопрос 14 (1 балл)
  var q14 = form.addMultipleChoiceItem();
  q14.setTitle("14. Что заставляет героя в платформере возвращаться на землю после прыжка (Урок 15)?");
  q14.setPoints(1);
  q14.setChoices([
    q14.createChoice("Музыкальное сопровождение.", false),
    q14.createChoice("Симуляция гравитации (силы тяжести).", true),
    q14.createChoice("Количество клавиш на клавиатуре.", false),
    q14.createChoice("Яркость подсветки экрана.", false),
    q14.createChoice("Скорость перемещения мышки.", false)
  ]);
  q14.setFeedbackForCorrect(FormApp.createFeedback().setText("Верно! Гравитация непрерывно тянет персонажа вниз, делая прыжки естественными и плавными.").build());
  q14.setFeedbackForIncorrect(FormApp.createFeedback().setText("Неверно. Правильный ответ: B. Гравитация непрерывно тянет персонажа вниз, делая прыжки естественными и плавными.").build());
  q14.setRequired(true);

  // Вопрос 15 (1 балл)
  var q15 = form.addMultipleChoiceItem();
  q15.setTitle("15. Как код игры узнает, что герой дотронулся до монетки или врага (Урок 15)?");
  q15.setPoints(1);
  q15.setChoices([
    q15.createChoice("С помощью проверки столкновения (Collision): когда границы героя и объекта пересекаются.", true),
    q15.createChoice("Только если у них совпал цвет заливки.", false),
    q15.createChoice("Только когда истекло игровое время.", false),
    q15.createChoice("Когда герой полностью остановился.", false),
    q15.createChoice("Только при нажатии кнопкой мыши.", false)
  ]);
  q15.setFeedbackForCorrect(FormApp.createFeedback().setText("Верно! Алгоритм коллизий проверяет координаты объектов: при их наложении срабатывает сбор монетки или урон.").build());
  q15.setFeedbackForIncorrect(FormApp.createFeedback().setText("Неверно. Правильный ответ: A. Алгоритм коллизий проверяет координаты объектов: при их наложении срабатывает сбор монетки или урон.").build());
  q15.setRequired(true);

  // Вопрос 16 (1 балл)
  var q16 = form.addMultipleChoiceItem();
  q16.setTitle("16. Какой веб-инструмент синтезирует звуковые эффекты в браузере без скачивания внешних файлов (Урок 17)?");
  q16.setPoints(1);
  q16.setChoices([
    q16.createChoice("Обычный видеоплеер.", false),
    q16.createChoice("Провод от наушников.", false),
    q16.createChoice("Web Audio API (AudioContext и генератор OscillatorNode).", true),
    q16.createChoice("Телефонный звонок.", false),
    q16.createChoice("Клавиатура ноутбука.", false)
  ]);
  q16.setFeedbackForCorrect(FormApp.createFeedback().setText("Верно! Web Audio API позволяет программно генерировать чистые звуковые волны прямо через звуковую карту.").build());
  q16.setFeedbackForIncorrect(FormApp.createFeedback().setText("Неверно. Правильный ответ: C. Web Audio API позволяет программно генерировать чистые звуковые волны прямо через звуковую карту.").build());
  q16.setRequired(true);

  // Вопрос 17 (1 балл)
  var q17 = form.addMultipleChoiceItem();
  q17.setTitle("17. Что делает камера в игре, когда герой бежит вперед по большому уровню (Урок 18)?");
  q17.setPoints(1);
  q17.setChoices([
    q17.createChoice("Плавно следует за героем (Camera Scrolling), открывая новые участки игрового мира.", true),
    q17.createChoice("Выключает монитор компьютера.", false),
    q17.createChoice("Останавливает героя у края экрана навсегда.", false),
    q17.createChoice("Перезапускает игру с начала.", false),
    q17.createChoice("Полностью закрывает игру.", false)
  ]);
  q17.setFeedbackForCorrect(FormApp.createFeedback().setText("Верно! Скроллинг камеры удерживает персонажа в поле зрения, создавая ощущение движения по огромному миру.").build());
  q17.setFeedbackForIncorrect(FormApp.createFeedback().setText("Неверно. Правильный ответ: A. Скроллинг камеры удерживает персонажа в поле зрения, создавая ощущение движения по огромному миру.").build());
  q17.setRequired(true);

  // Вопрос 18 (1 балл)
  var q18 = form.addMultipleChoiceItem();
  q18.setTitle("18. Какое событие JavaScript срабатывает в момент касания пальцем сенсорного экрана телефона (Урок 19)?");
  q18.setPoints(1);
  q18.setChoices([
    q18.createChoice("onsubmit", false),
    q18.createChoice("onhover", false),
    q18.createChoice("mouseleave", false),
    q18.createChoice("keypress", false),
    q18.createChoice("touchstart", true)
  ]);
  q18.setFeedbackForCorrect(FormApp.createFeedback().setText("Верно! На смартфонах касание пальца вызывает событие 'touchstart', движение — 'touchmove', отрыв — 'touchend'.").build());
  q18.setFeedbackForIncorrect(FormApp.createFeedback().setText("Неверно. Правильный ответ: E. На смартфонах касание пальца вызывает событие 'touchstart', движение — 'touchmove', отрыв — 'touchend'.").build());
  q18.setRequired(true);

  // Вопрос 19 (1 балл)
  var q19 = form.addMultipleChoiceItem();
  q19.setTitle("19. Что означает аббревиатура OVR на карточке футболиста в проекте 'FUT Card Studio' (Урок 21)?");
  q19.setPoints(1);
  q19.setChoices([
    q19.createChoice("Номер телефона спортсмена.", false),
    q19.createChoice("Overall Rating — общий итоговый рейтинг мастерства игрока.", true),
    q19.createChoice("Время начала матча.", false),
    q19.createChoice("Стоимость карточки в магазине.", false),
    q19.createChoice("Размер футбольной обуви.", false)
  ]);
  q19.setFeedbackForCorrect(FormApp.createFeedback().setText("Верно! OVR (Overall Rating) — ключевое число на карточке, показывающее общий класс и мастерство футболиста.").build());
  q19.setFeedbackForIncorrect(FormApp.createFeedback().setText("Неверно. Правильный ответ: B. OVR (Overall Rating) — ключевое число на карточке, показывающее общий класс и мастерство футболиста.").build());
  q19.setRequired(true);

  // Вопрос 20 (1 балл)
  var q20 = form.addMultipleChoiceItem();
  q20.setTitle("20. Что произойдет в 'FUT Squad Builder' (Урок 22), если поставить рядом двух игроков из одного клуба?");
  q20.setPoints(1);
  q20.setChoices([
    q20.createChoice("Оба игрока получат красную карточку.", false),
    q20.createChoice("Футболисты уйдут из состава.", false),
    q20.createChoice("У них поменяются номера на форме.", false),
    q20.createChoice("Игра немедленно заблокируется.", false),
    q20.createChoice("Между ними образуется клубная связь, дающая максимальный бонус командной химии (Chemistry).", true)
  ]);
  q20.setFeedbackForCorrect(FormApp.createFeedback().setText("Верно! Игроки одного клуба образуют самую крепкую синергию, принося максимум очков командной химии.").build());
  q20.setFeedbackForIncorrect(FormApp.createFeedback().setText("Неверно. Правильный ответ: E. Игроки одного клуба образуют самую крепкую синергию, принося максимум очков командной химии.").build());
  q20.setRequired(true);

  // Вопрос 21 (1 балл)
  var q21 = form.addMultipleChoiceItem();
  q21.setTitle("21. Почему на трансферном рынке FUT разработчики ввели 5% налог с каждой продажи (Урок 24)?");
  q21.setPoints(1);
  q21.setChoices([
    q21.createChoice("Чтобы расстроить игроков.", false),
    q21.createChoice("Чтобы стереть старые компьютеры.", false),
    q21.createChoice("Чтобы сделать всех футболистов бесплатными.", false),
    q21.createChoice("Чтобы сдерживать инфляцию, выводя лишние монеты из игры и удерживая стабильные цены на игроков.", true),
    q21.createChoice("Чтобы купить реальную одежду в магазине.", false)
  ]);
  q21.setFeedbackForCorrect(FormApp.createFeedback().setText("Верно! Механизм 5% налога (Coin Sink) выводит избыточную виртуальную валюту из оборота, предотвращая гиперинфляцию.").build());
  q21.setFeedbackForIncorrect(FormApp.createFeedback().setText("Неверно. Правильный ответ: D. Механизм 5% налога (Coin Sink) выводит избыточную виртуальную валюту из оборота, предотвращая гиперинфляцию.").build());
  q21.setRequired(true);

  // Вопрос 22 (1 балл)
  var q22 = form.addMultipleChoiceItem();
  q22.setTitle("22. Какой браузерный Web API распознает человеческую речь в текст в проекте 'Target Jarvis' (Урок 25)?");
  q22.setPoints(1);
  q22.setChoices([
    q22.createChoice("window.alert()", false),
    q22.createChoice("navigator.vibrate()", false),
    q22.createChoice("Web Speech API (интерфейс SpeechRecognition).", true),
    q22.createChoice("localStorage.clear()", false),
    q22.createChoice("document.body.remove()", false)
  ]);
  q22.setFeedbackForCorrect(FormApp.createFeedback().setText("Верно! Интерфейс SpeechRecognition слушает микрофон и превращает слова пользователя в строку текста.").build());
  q22.setFeedbackForIncorrect(FormApp.createFeedback().setText("Неверно. Правильный ответ: C. Интерфейс SpeechRecognition слушает микрофон и превращает слова пользователя в строку текста.").build());
  q22.setRequired(true);

  // Вопрос 23 (1 балл)
  var q23 = form.addMultipleChoiceItem();
  q23.setTitle("23. Как веб-камера в проекте 'Кибер-Глаз' обнаруживает движение в комнате (Урок 26)?");
  q23.setPoints(1);
  q23.setChoices([
    q23.createChoice("Сравнивая изменение цвета пикселей между предыдущим и текущим видеокадрами.", true),
    q23.createChoice("Измеряя температуру воздуха термометром.", false),
    q23.createChoice("Только когда двигается компьютерная мышка.", false),
    q23.createChoice("Заливая весь экран черной краской.", false),
    q23.createChoice("Громко выкрикивая имя человека.", false)
  ]);
  q23.setFeedbackForCorrect(FormApp.createFeedback().setText("Верно! Алгоритм сравнивает два соседних кадра: если разница в цветах пикселей превысила порог — зафиксировано движение.").build());
  q23.setFeedbackForIncorrect(FormApp.createFeedback().setText("Неверно. Правильный ответ: A. Алгоритм сравнивает два соседних кадра: если разница в цветах пикселей превысила порог — зафиксировано движение.").build());
  q23.setRequired(true);

  // Вопрос 24 (1 балл)
  var q24 = form.addMultipleChoiceItem();
  q24.setTitle("24. По каким признакам биометрическая система Face ID распознает человека на Уроке 27?");
  q24.setPoints(1);
  q24.setChoices([
    q24.createChoice("По цвету футболки человека.", false),
    q24.createChoice("По номеру мобильного телефона.", false),
    q24.createChoice("Только по размеру обуви.", false),
    q24.createChoice("Только по росту человека.", false),
    q24.createChoice("По уникальному строению лица: расстоянию между глазами, носом и губами (Face Landmarks).", true)
  ]);
  q24.setFeedbackForCorrect(FormApp.createFeedback().setText("Верно! Face ID сопоставляет ключевые ориентиры лица (Landmarks), создавая неповторимый биометрический профиль.").build());
  q24.setFeedbackForIncorrect(FormApp.createFeedback().setText("Неверно. Правильный ответ: E. Face ID сопоставляет ключевые ориентиры лица (Landmarks), создавая неповторимый биометрический профиль.").build());
  q24.setRequired(true);

  // Вопрос 25 (1 балл)
  var q25 = form.addMultipleChoiceItem();
  q25.setTitle("25. В чем заключается главное умение разработчика (Vibecoder) 7–8 классов?");
  q25.setPoints(1);
  q25.setChoices([
    q25.createChoice("Создавать игры, где есть только одна кнопка.", false),
    q25.createChoice("Слепо копировать чужой код без понимания.", false),
    q25.createChoice("Никогда не показывать свои проекты другим.", false),
    q25.createChoice("Игнорировать цифровую безопасность.", false),
    q25.createChoice("Уметь воплотить идею в интерактивную веб-игру, создавать код с помощью ИИ и самостоятельно находить ошибки в DevTools.", true)
  ]);
  q25.setFeedbackForCorrect(FormApp.createFeedback().setText("Верно! Vibecoder умеет проектировать интерфейсы, оживлять их физикой и логикой и грамотно работать с AI-инструментами.").build());
  q25.setFeedbackForIncorrect(FormApp.createFeedback().setText("Неверно. Правильный ответ: E. Vibecoder умеет проектировать интерфейсы, оживлять их физикой и логикой и грамотно работать с AI-инструментами.").build());
  q25.setRequired(true);

  Logger.log("✓ Google Form (RU) создана: " + form.getEditUrl());
  Logger.log("✓ Ссылка для учеников: " + form.getPublishedUrl());
}