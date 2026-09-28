#!/usr/bin/env python3
import os
import json
from generate_all_5_6 import make_presentation, BASE_DIR

# ==========================================
# LESSON 5: CYBER-DETECTIVE & AI SAFETY
# ==========================================

l5_slides = """
<section class="slide is-on" data-phase="Kirish|Вступление|Opening" data-time="0–3">
  <div class="title-wrap">
    <div class="eyebrow">Vibecoding · <span data-ru="урок 5 · 5-6 классы" data-en="lesson 5 · grades 5-6">5-dars · 5-6 sinflar</span></div>
    <div class="title-meta">
      <span><b lang="uz">Fan:</b><span data-ru=" IT / Vibecoding" data-en=" IT / Vibecoding"> IT / Vibecoding</span><b lang="ru">Предмет:</b><span lang="ru"> IT / Vibecoding</span><b lang="en">Subject:</b><span lang="en"> IT / Vibecoding</span></span>
      <span><b lang="uz">Hafta:</b><span data-ru=" 1" data-en=" 1"> 1</span><b lang="ru">Неделя:</b><span lang="ru"> 1</span><b lang="en">Week:</b><span lang="en"> 1</span></span>
    </div>
    <h1 data-ru="Кибер-Детектив: Deepfake и Безопасность ИИ" data-en="Cyber-Detective: Deepfakes & AI Safety">Kiber-Detektiv: Deepfake va AI Xavfsizligi</h1>
    <p class="lede" data-ru="Как нейросети создают неотличимые от реальности фейки, фото и клонируют голоса? Цифровая гигиена, факт-чекинг и методы разоблачения обмана." data-en="How does AI generate hyper-realistic fake images, audio, and clones? Digital hygiene, forensic fact-checking, and scam defense.">Sun'iy intellekt qanday qilib haqiqatdek tuyuluvchi soxta rasm, video va ovozlarni yaratadi? Kiber-xavfsizlik, fakt-cheking va raqamli firibgarlardan himoyalanish usullari.</p>
  </div>
</section>

<section class="slide" data-phase="Deepfake Nima|Что такое Deepfake|What is Deepfake" data-time="3–7">
  <div class="eyebrow"><span data-ru="Цифровой Обман" data-en="Digital Spoofing">Kiber-Xavf</span></div>
  <h2 data-ru="Что такое Deepfake: Как ИИ Подделывает Реальность" data-en="What is a Deepfake: How AI Fabricates Reality">Deepfake Nima: AI Qanday Qilib Soxta Dunyo Yaratadi?</h2>
  <p data-ru="Deepfake (Deep Learning + Fake) — технология создания фальшивых фото, видео и аудиозаписей:" data-en="Deepfake (Deep Learning + Fake) is the synthetic fabrication of deceptive images, videos, and voices:">Deepfake (Chuqur O'rganish + Qalbaki) — inson aytmagan gaplarni va qilmagan ishlarini soxtalashtirish texnologiyasi:</p>
  <div class="cols c2" style="margin-top:15px;">
    <div class="box">
      <h3 style="color:var(--ink-2);" data-ru="Обычный Фотошоп" data-en="Classic Photo Editing">Oddiy Fotomontaj</h3>
      <p data-ru="Художник часами вырезает детали вручную. При сильном зуме всегда видны кривые пиксели и следы склейки." data-en="Manual cut-and-paste in editors. Inconsistencies and jagged pixel borders are easily detected on zoom.">Qo'lda soatlab kesiladi. Katta qilib qaralganda piksellar va qirqilgan chegaralar darhol ko'rinib qoladi.</p>
    </div>
    <div class="box" style="border-left:4px solid var(--accent);">
      <h3 style="color:var(--accent);" data-ru="Генеративный Deepfake" data-en="Generative AI Deepfake">AI Deepfake</h3>
      <p data-ru="Нейросеть генерирует видео целиком. Она идеально подделывает мимику лица, движение губ и блеск глаз!" data-en="Neural nets generate cohesive video frames, matching facial muscle kinetics, lip-sync, and iris glint!">Neyrotarmoq kadrni noldan yaratadi. U insonning yuz mimikasi, lab qimirlashi va ko'z qarashlarini mukammal soxtalashtiradi!</p>
    </div>
  </div>
</section>

<section class="slide" data-phase="Vizual Ekspertiza|Визуальный Анализ|Visual Forensics" data-time="7–11">
  <div class="eyebrow"><span data-ru="Визуальная Экспертиза" data-en="Visual Forensics">Vizual Detektiv</span></div>
  <h2 data-ru="4 Признака Фейка: Как Распознать ИИ-Картинку" data-en="4 Forensic Tells: Spotting AI-Generated Images">AI Rasmlarini Fosh Qilishning 4 Ta Alomati</h2>
  <p data-ru="Даже лучшие нейросети совершают анатомические и физические ошибки. Ищите эти 4 улики:" data-en="Even bleeding-edge diffusion models make topological errors. Scrutinize these 4 forensic clues:">Har qanday mukammal AI ham fizik va anatomik xatolar qiladi. Kiber-detektiv ularni shu 4 belgidan topadi:</p>
  <div class="grid" style="display:grid; grid-template-columns:1fr 1fr; gap:12px; margin-top:10px;">
    <div class="box">
      <h3 style="color:var(--accent);" data-ru="1. Пальцы и Суставы 🖐️" data-en="1. Hands & Joints 🖐️">1. Qo'l Barmoqlari va Tirnoqlar 🖐️</h3>
      <p data-ru="6-7 пальцев на одной руке, неестественно изогнутые фаланги, размытые или отсутствующие ногти." data-en="6 or 7 fingers on a hand, unnatural joint bends, missing or fused fingernails.">Qo'lda 6-7 ta barmoq, g'alati qiyshaygan bo'g'inlar yoki birlashib ketgan tirnoqlar.</p>
    </div>
    <div class="box" style="color:var(--accent);"><div class="box" style="margin:0; padding:0; border:0;">
      <h3 style="color:var(--accent);" data-ru="2. Зрачки и Блики 👀" data-en="2. Pupils & Reflections 👀">2. Ko'z Qorachig'i va Nur Aksi 👀</h3>
      <p data-ru="У человека блики в обоих глазах одинаковые. У ИИ зрачки бывают квадратными, а блики не совпадают." data-en="Human pupils share identical reflections. AI renders mismatched specular glints or deformed irises.">Haqiqiy odamda ko'z nuri ikkala ko'zda bir xil aks etadi. AI da esa nurlar turlicha yoki qorachiq qiyshiq bo'ladi.</p>
    </div></div>
    <div class="box">
      <h3 style="color:var(--accent);" data-ru="3. Текст на Заднем Плане 🔤" data-en="3. Gibberish Background Text 🔤">3. Orqa Fondagi Matnlar 🔤</h3>
      <p data-ru="Надписи на футболках, вывесках и дорожных знаках превращаются в бессмысленные иероглифы." data-en="T-shirt logos, billboards, and street signs mutate into unreadable alien hieroglyphics.">Kiyimlardagi yozuvlar, do'kon peshtoqlari va belgilardagi so'zlar ma'nosiz belgilarga aylanib qoladi.</p>
    </div>
    <div class="box">
      <h3 style="color:var(--accent);" data-ru="4. Логика Теней и Физика 💡" data-en="4. Shadow Physics & Light 💡">4. Fizika va Soyalar Mantiqi 💡</h3>
      <p data-ru="Источник света слева, а тень падает вперед. Очки или серьги имеют разную форму с двух сторон." data-en="Light comes from the left, but shadow casts forward. Earrings or glasses are asymmetric.">Yorug'lik chap tomondan tushayotgan bo'lsa-da, soya yo'q. Ko'zoynak yoki ziraklar har xil shaklda.</p>
    </div>
  </div>
</section>

<section class="slide" data-phase="Ovoz Klonlash|Клоны Голоса|Voice Cloning" data-time="11–15">
  <div class="eyebrow"><span data-ru="Аудио-Клоны" data-en="Voice Cloning">Ovoz Firibgarligi</span></div>
  <h2 data-ru="Клонирование Голоса: Как Мошенники Имитируют Звонки" data-en="Voice Cloning: Spoofing Phone Calls with AI">Ovoz Klonlash (Voice Spoofing): 3 Soniyada Shaxsni O'g'irlash</h2>
  <p data-ru="Современные голосовые нейросети могут скопировать голос человека всего по 3 секундам аудио:" data-en="Modern audio engines can synthesize a replica voice from a 3-second audio sample:">Bugungi sun'iy intellekt odamning internetdagi 3 soniyalik gapidan uning ovoz tembrini nusxalay oladi:</p>
  <ul class="rules">
    <li><span class="t" data-ru="<b>Как работает обман:</b> Мошенники берут голосовое сообщение из Telegram и звонят родителям голосом ребенка: <i>'Мама, я потерял телефон, скинь деньги сюда!'</i>" data-en="<b>The Scam Mechanism:</b> Fraudsters grab a public Telegram voice clip and call parents mimicking their child: <i>'Mom, emergency, transfer funds here!'</i>"><b>Firibgarlik Sxemasi:</b> Telegram yoki Instagram'dagi ovozdan nusxa olib, ota-onaga qo'ng'iroq qilishadi: <i>'Oyi, favqulodda holat bo'ldi, zudlik bilan pul o'tkazing!'</i></span></li>
    <li><span class="t" data-ru="<b>Как разоблачить робота:</b> Задайте личный вопрос, которого нет в интернете: <i>'Как зовут нашего попугая?'</i> или <i>'Что мы ели вчера на ужин?'</i>" data-en="<b>Forensic Trap:</b> Ask an offline secret only your real family knows: <i>'What is our pet's secret nickname?'</i> or <i>'What did we eat last night?'</i>"><b>Fosh Qilish Yo'li:</b> Internetda yo'q shaxsiy savolni bering: <i>'Uyimizdagi mushukning laqabi nima?'</i> yoki <i>'Kecha kechki ovqatga nima yedik?'</i></span></li>
    <li><span class="t" data-ru="<b>Семейный Пароль (Safe Word):</b> Придумайте секретное кодовое слово в семье, которое знают только близкие!" data-en="<b>Family Safe Word:</b> Establish an offline emergency secret passphrase known exclusively to household members!"><b>Oila Paroli (Safe Word):</b> Oila a'zolaringiz bilan faqat o'zingiz biladigan maxfiy 'parol-so'z' kelishib oling!</span></li>
  </ul>
</section>

<section class="slide" data-phase="Gallyutsinatsiyalar|Галлюцинации ИИ|AI Hallucinations" data-time="15–19">
  <div class="eyebrow"><span data-ru="Ложные Факты" data-en="Hallucination Hunting">AI Xatolari</span></div>
  <h2 data-ru="Галлюцинации ИИ: Почему Нейросеть Уверенно Врёт" data-en="AI Hallucinations: Why AI Lies with Total Confidence">AI Gallyutsinatsiyasi: AI Qanday Qilib Ishonch Bilan Aldaydi?</h2>
  <p data-ru="ИИ не знает концепции правды. Он просто угадывает следующее самое вероятное слово:" data-en="AI does not understand objective reality; it only predicts the next statistically probable word token:">Sun'iy intellekt haqiqat nimaligini tushunmaydi. U shunchaki ketma-ket kelishi ehtimoli yuqori bo'lgan so'zlarni ulaydi:</p>
  <div class="box" style="background:var(--panel); border-left:5px solid var(--accent); padding:16px;">
    <p style="font-family:monospace; font-size:0.9em; line-height:1.5;" data-ru="<b>Ученик:</b> 'Какой смартфон был самым популярным в Самарканде в 1895 году?'<br><b>AI (галлюцинация):</b> 'В 1895 году в Самарканде наибольшей популярностью пользовался кнопочный смартфон Samarkand-Phone 1 с медным корпусом...'" data-en="<b>Student:</b> 'What smartphone model was most popular in Samarkand in 1895?'<br><b>AI (hallucination):</b> 'In 1895, Samarkand citizens predominantly used the copper-framed Samarkand-Phone 1 mobile device...'">
      <b>O'quvchi:</b> "1895-yilda Samarqandda eng mashhur smartfon qaysi bo'lgan?"<br>
      <b>AI (gallyutsinatsiya):</b> "1895-yilda Samarqand aholisi orasida mis korpusli 'Samarkand-Phone 1' smartfoni eng ommabop hisoblangan..."
    </p>
  </div>
  <p style="margin-top:12px; font-size:0.95em;" data-ru="Главное правило кибер-детектива: никогда не используйте факты от ИИ без проверки в Google или энциклопедии!" data-en="Golden cyber-detective rule: Never publish AI factual claims without cross-referencing credible encyclopedias!">Kiber-detektivning oltin qoidasi: AI aytgan har qanday tarixiy yoki ilmiy faktni qidiruv tizimlarida tekshirish shart!</p>
</section>

<section class="slide" data-phase="Fishing Botlar|Игровой Фишинг|Gaming Scams" data-time="19–23">
  <div class="eyebrow"><span data-ru="Игровой Фишинг" data-en="Social Engineering">O'yin Firibgarlari</span></div>
  <h2 data-ru="Фишинг в Roblox и Discord: Опасные AI-Боты" data-en="Roblox & Discord: Phishing & Scam Chatbots">Roblox va Discord: O'yin Hisoblarini O'g'irlovchi AI Botlar</h2>
  <p data-ru="Злоумышленники используют умных чат-ботов, чтобы выманивать аккаунты игроков и пароли:" data-en="Cyber-criminals deploy conversational bots to hijack player accounts and sensitive credentials:">Kiber-jinoyatchilar o'yinchilarning qimmatli hisoblarini o'g'irlash uchun aqlli fishing botlardan foydalanadi:</p>
  <div class="cols c2" style="margin-top:15px;">
    <div class="box">
      <h3 style="color:var(--accent);" data-ru="Ловушка Бота 🪤" data-en="Scam Bot Bait 🪤">Firibgar Bot Tuzog'i 🪤</h3>
      <p data-ru="<i>'Привет! Ты выбран победителем! Получи 10 000 Robux бесплатно. Перейди по ссылке robl0x-free-gift.cc и введи свой логин и пароль!'</i>" data-en="<i>'Hey! You won our raffle! Claim 10,000 free Robux right now. Visit robl0x-free-gift.cc and log in with your credentials!'</i>"><i>"Salom! Sen tanlov g'olibi bo'lding! 10 000 Robux bepul olish uchun zudlik bilan robl0x-free.cc saytiga kirib, login va parolingni yoz!"</i></p>
    </div>
    <div class="box" style="border-left:4px solid var(--green);">
      <h3 style="color:var(--green);" data-ru="Защита Детектива 🛡️" data-en="Detective Shield 🛡️">Kiber-Qalqon 🛡️</h3>
      <p data-ru="Никто не раздает бесплатную валюту за пароль! Официальные ссылки проверяются по домену (roblox.com). Включите 2FA (двухфакторку)!" data-en="Nobody gives free currency in exchange for passwords. Verify exact domain names and mandate 2-Factor Authentication (2FA)!">Hech kim parolingiz evaziga tekinga Robux bermaydi! Sayt domenini tekshiring va darhol 2FA (ikki bosqichli tasdiqlash)ni yoqing!</p>
    </div>
  </div>
</section>

<section class="slide" data-phase="Detektiv Asboblari|Инструменты Детектива|Forensic Tools" data-time="23–27">
  <div class="eyebrow"><span data-ru="Инструменты Детектива" data-en="Forensic Toolkit">Fakt-Cheking Qurollari</span></div>
  <h2 data-ru="Инструменты Детектива: Обратный Поиск и Анализ" data-en="Cyber-Forensic Toolkit: Reverse Image Search & Analysis">Raqamli Izni Tekshirish: Qidiruv va Ekspertiza Vositalari</h2>
  <p data-ru="Профессиональные факт-чекеры используют 3 главных инструмента для проверки подозрительного контента:" data-en="Professional fact-checkers deploy 3 vital forensic tools to verify suspect media:">Haqiqiy kiber-detektivlar shubhali ma'lumotlarni tekshirish uchun 3 ta asosiy qurolni ishlatadi:</p>
  <ul class="rules">
    <li><span class="t" data-ru="<b>1. Google / Yandex Reverse Image Search:</b> Загрузите картинку в поиск, чтобы узнать, где и когда она появилась впервые." data-en="<b>1. Reverse Image Search:</b> Upload the image into search engines to uncover its true origin date and first upload source."><b>1. Qidiruvga Rasm Yuklash (Reverse Search):</b> Rasmni Google/Yandex qidiruviga tashlang — u qachon va qayerda birinchi marta chiqqanini ko'rasiz.</span></li>
    <li><span class="t" data-ru="<b>2. EXIF & Metadata Viewer:</b> Проверка скрытых данных файла: какая камера сделала снимок или какой графический софт его сохранил." data-en="<b>2. EXIF Metadata Inspection:</b> Inspect hidden digital signatures revealing camera hardware or AI generator rendering engines."><b>2. EXIF va Metama'lumotlar:</b> Faylning yashirin ma'lumotlari: rasm qaysi kamera yoki qaysi dasturda saqlanganini ko'rsatadi.</span></li>
    <li><span class="t" data-ru="<b>3. Первоисточник (Original Source):</b> Найдите официальный сайт или проверенное новостное агентство перед тем, как верить новости." data-en="<b>3. Primary Source Verification:</b> Trace the original press release or verified agency before circulating sensational claims."><b>3. Rasmiy Asl Manba:</b> Shov-shuvli xabarga ishonishdan oldin uning rasmiy manbasini va xalqaro yangiliklar tasdig'ini qidiring.</span></li>
  </ul>
</section>

<section class="slide" data-phase="Kiber-Gigiyena|Кибергигиена|Digital Hygiene" data-time="27–31">
  <div class="eyebrow"><span data-ru="Кибергигиена" data-en="Digital Hygiene">Raqamli Xavfsizlik</span></div>
  <h2 data-ru="Золотые Правила Кибербезопасности: 2FA и Пароли" data-en="Golden Rules of Cyber Safety: 2FA & Password Armor">Kiber-Xavfsizlikning Oltin Qoidasi: 2FA va Kuchli Parol</h2>
  <p data-ru="99% взломов игровых и учебных аккаунтов происходят из-за слабых паролей:" data-en="99% of gaming and school account breaches stem from flimsy, reused passwords:">O'yin va maktab akkauntlarining 99% buzilishi oson parollar tufayli sodir bo'ladi:</p>
  <div class="cols c2" style="margin-top:15px;">
    <div class="box">
      <h3 style="color:var(--accent);" data-ru="Легкая Добыча 🔓" data-en="Vulnerable Targets 🔓">Xavfli Parollar 🔓</h3>
      <p data-ru="<code>123456</code>, <code>password</code>, свое имя или дата рождения. Бот-взломщик подбирает такой пароль за 0.01 секунды." data-en="<code>123456</code>, <code>qwerty</code>, or birthdates. Automated brute-force cracking bots solve these in 0.01 seconds."><code>123456</code>, <code>qwerty</code>, o'z ismi yoki tug'ilgan yili. Buzg'unchi botlar bunday parolni 0.01 soniyada topadi.</p>
    </div>
    <div class="box" style="border-left:4px solid var(--green);">
      <h3 style="color:var(--green);" data-ru="Броня Детектива 🔐" data-en="Detective Armor 🔐">Kiber-Zirh 🔐</h3>
      <p data-ru="12+ символов, смесь букв, цифр и знаков (<code>Cyber#Storm_2026!</code>) + <b>2FA</b> (код из СМС/приложения при каждом входе)!" data-en="12+ characters, mixed cases, digits, and symbols (<code>Cyber#Storm_2026!</code>) backed by mandatory <b>2FA</b> auth codes!">Kamida 12 belgi, aralash harf, raqam va belgilar (<code>Kiber#Burgut_2026!</code>) hamda <b>2FA</b> (telefonga keluvchi kod)!</p>
    </div>
  </div>
</section>

<section class="slide" data-phase="Detektiv Sinovi|Практикум|Detective Challenge" data-time="31–36">
  <div class="eyebrow"><span data-ru="Практикум Детектива" data-en="Detective Lab">Interaktiv Sinov</span></div>
  <h2 data-ru="Практикум: Отличите Реальное Фото от Нейросети!" data-en="Forensic Challenge: Spot the Real Photo vs AI Generation!">Detektiv Sinovi: Haqiqiy Surat va AI Generatsiyasini Ajrating!</h2>
  <p data-ru="Объединитесь в пары и проведите экспресс-экспертизу предложенных изображений:" data-en="Team up in detective pairs and conduct a rapid forensic audit of the test images:">Juftlikda ishlang va taqdim etilgan suratlarni kiber-ekspertizadan o'tkazing:</p>
  <div class="cols c2" style="margin-top:15px;">
    <div class="box">
      <h3 style="color:var(--green);" data-ru="Шаг 1: Поиск Улик (2 мин)" data-en="Step 1: Spotting Clues (2 min)">1-Qadam: Dalillar Qidiruvi (2 daq)</h3>
      <p data-ru="Изучите зумом: пальцы, отражения в глазах, надписи на заднем плане и логику теней." data-en="Zoom in closely: inspect fingers, eye iris reflections, background signage, and shadow physics.">Kattalashtirib qarang: barmoqlar, ko'z nuri, orqa fondagi belgilar va soyalar mantiqi.</p>
    </div>
    <div class="box" style="border-left:4px solid var(--accent);">
      <h3 style="color:var(--accent);" data-ru="Шаг 2: Вердикт (3 мин)" data-en="Step 2: The Verdict (3 min)">2-Qadam: Yakuniy Xulosa (3 daq)</h3>
      <p data-ru="Запишите вердикт: РЕАЛЬНОЕ фото или AI-ФЕЙК? Назовите минимум 2 неопровержимых доказательства!" data-en="Issue the verdict: REAL photo or AI FAKE? List at least 2 indisputable forensic proofs!">Xulosa bering: Bu HAQIQIY suratmi yoki AI SOXTALASHTIRIShI? Kamida 2 ta aniq isbotni ayting!</p>
    </div>
  </div>
</section>

<section class="slide" data-phase="Uy vazifasi|Домашка|Homework" data-time="36–40">
  <div class="eyebrow"><span data-ru="Домашнее задание" data-en="Homework">Uyga vazifa</span></div>
  <h2 data-ru="Домашка: Памятка по Защите от Deepfake и Мошенников" data-en="Homework: Craft a Cyber-Safety & Anti-Deepfake Field Guide">Uy vazifasi: Kiber-Xavfsizlik va Deepfakedan Himoya Bukleti</h2>
  <div class="hw">
    <div style="display:grid; gap:16px">
      <p class="lede" data-ru="Создайте памятку кибербезопасности для своей семьи и друзей:" data-en="Engineer a practical cyber-safety field guide for your friends and family:">Oila a'zolaringiz va do'stlaringiz uchun amaliy kiber-xavfsizlik qo'llanmasini tayyorlang:</p>
      <ul class="plain">
        <li><span class="t" data-ru="Найдите в интернете 1 AI-фейк и выпишите 3 визуальных артефакта" data-en="Find 1 viral AI image and pinpoint 3 forensic artifacts proving it is generated">Internetdan 1 ta AI soxta suratini toping va uning soxtaligini isbotlovchi 3 ta vizual xatoni aniqlang.</span></li>
        <li><span class="t" data-ru="Составьте чек-лист из 4 правил защиты аккаунтов в играх (Roblox/Discord)" data-en="Draft a 4-point defense checklist protecting gaming accounts (Roblox/Discord) against phishing">O'yin hisoblarini (Roblox, Discord) firibgarlardan asrash bo'yicha 4 ta oltin qoida tuzing.</span></li>
        <li><span class="t" data-ru="Придумайте с семьей секретное кодовое слово на случай телефонного фейка" data-en="Establish a secret family emergency passphrase to defeat voice spoofing scams">Telefon orqali ovoz klonlashdan himoyalanish uchun oilangiz bilan maxfiy parol so'zini kelishib oling.</span></li>
      </ul>
    </div>
    
    <div class="grade">
      <div class="tag" data-ru="10-балльная шкала" data-en="10 point rubric">10 ballik mezon</div>
      <div class="g"><span><span data-ru="Анализ артефактов фейка" data-en="AI Image Forensic Proof">Soxta surat tahlili</span></span><b>4</b></div>
      <div class="g"><span><span data-ru="Чек-лист безопасности" data-en="Account Safety Checklist">Xavfsizlik qoidalari</span></span><b>4</b></div>
      <div class="g"><span><span data-ru="Сдано вовремя" data-en="On-time Submission">Vaqtida topshirilgani</span></span><b>2</b></div>
      <div class="g"><span><b><span data-ru="Итого" data-en="Total">Jami</span></b></span><b>10</b></div>
    </div>
  </div>
</section>
"""

l5_notes = {
  "uz": [
    "Darsni boshlash: O'quvchilarga internetda ko'rgan har bir narsaga ishonish xavfli ekanligini ayting. Mavzu: Kiber-detektiv va AI xavfsizligi.",
    "Deepfake nima: Neyrotarmoqlar video, yuz va ovozni qanday soxtalashtirishi. Photoshop bilan deepfake o'rtasidagi farq.",
    "Vizual fosh qilish: 4 ta alomat — qo'llar/barmoqlar, ko'z qorachig'i aksi, fondagi g'alati yozuvlar va soyalar fizikasi.",
    "Ovoz klonlash va telefon firibgarlari: 3 soniyalik audio orqali ovoz nusxalash xavfi va oilaviy maxfiy parol (safe word) himoyasi.",
    "AI gallyutsinatsiyasi: AI yolg'on gapirishni bilmaydi, u faqat so'zlarni ulaydi. 1895-yil smartfoni misolida tushuntiring.",
    "O'yinlardagi fishing botlar: Roblox va Discordda 'bepul Robux' va'da qiluvchi tuzoqlar. Hech qachon shaxsiy ma'lumotlarni bermaslik.",
    "Kiber-detektiv asboblari: Reverse image search, EXIF metama'lumotlar va asl manbani tekshirish madaniyati.",
    "Raqamli gigiyena: Kuchli parol formulasi va ikki bosqichli tasdiqlash (2FA) ning hal qiluvchi ahamiyati.",
    "Amaliy sinov: Juftlikda ishlayotgan o'quvchilarga rasmlar beriladi. Ular 3 daqiqada soxta rasmni dalillar bilan fosh qiladi.",
    "Uy vazifasi: Deepfake va firibgarlikdan himoyalanish bo'yicha qo'llanma tayyorlash. 10 ballik baholash mezonini tushuntiring."
  ],
  "ru": [
    "Вводная часть: Объясните ученикам, почему в цифровую эпоху нельзя слепо верить контенту. Тема: Кибер-детектив и безопасность ИИ.",
    "Что такое Deepfake: Как нейросети подделывают мимику, лица и видео. Разница между ручным фотошопом и диффузией.",
    "Визуальный анализ: 4 улики — деформация пальцев, блики в зрачках, абракадабра на фоне и противоречия в тенях.",
    "Клонирование голоса: Как мошенники используют 3-секундные голосовые для обмана родителей, и важность секретного семейного пароля.",
    "Галлюцинации нейросетей: Почему ИИ уверенно сочиняет небылицы вроде 'смартфонов 19 века'. Важность проверки фактов.",
    "Игровой фишинг: Боты в Roblox и Discord, предлагающие бесплатную валюту в обмен на логин. Защита аккаунта.",
    "Инструменты детектива: Обратный поиск по картинке (Reverse Search), чтение метаданных EXIF и поиск первоисточника.",
    "Кибергигиена: Создание надежных паролей (12+ знаков) и обязательное включение двухфакторной аутентификации (2FA).",
    "Практикум: Работа в парах. Экспресс-анализ подозрительных фотографий и формулирование доказательств подделки.",
    "Домашнее задание: Создать семейную памятку по защите от фейков и фишинга. Разъясните критерии 10-балльной оценки."
  ],
  "en": [
    "Introduction: Frame the stakes: in the age of generative AI, seeing is no longer believing. Topic: Cyber-Detective & AI Safety.",
    "Demystifying Deepfakes: How generative diffusion fabricates lifelike video and facial kinetics. Contrast with traditional Photoshop.",
    "Visual Forensic Clues: 4 core artifacts — hand anatomy glitches, pupil reflection mismatches, garbled text, and shadow physics.",
    "Voice Cloning & Audio Scams: Synthesizing voices from brief 3-second audio clips, and deploying offline family passphrases.",
    "Hallucination Hazards: Why probabilistic models fabricate historical myths with absolute confidence. Emphasize verification.",
    "Gaming Phishing Bots: Social engineering vectors in Roblox and Discord promising free currency to steal credentials.",
    "Forensic Investigator Toolkit: Reverse image search, EXIF metadata inspection, and primary source cross-checking.",
    "Digital Hygiene: Robust password entropy (12+ characters, symbols) and mandatory multi-factor authentication (2FA).",
    "Hands-on Detective Lab: Pair audit of challenge images. Formulate indisputable forensic proof identifying generated media.",
    "Homework: Engineer a family cyber-safety and anti-deepfake guide. Review the 10-point evaluation rubric."
  ]
}

# ==========================================
# LESSON 6: GAME PITCH & DIGITAL EXPO
# ==========================================

l6_slides = """
<section class="slide is-on" data-phase="Kirish|Вступление|Opening" data-time="0–3">
  <div class="title-wrap">
    <div class="eyebrow">Vibecoding · <span data-ru="урок 6 · 5-6 классы" data-en="lesson 6 · grades 5-6">6-dars · 5-6 sinflar</span></div>
    <div class="title-meta">
      <span><b lang="uz">Fan:</b><span data-ru=" IT / Vibecoding" data-en=" IT / Vibecoding"> IT / Vibecoding</span><b lang="ru">Предмет:</b><span lang="ru"> IT / Vibecoding</span><b lang="en">Subject:</b><span lang="en"> IT / Vibecoding</span></span>
      <span><b lang="uz">Hafta:</b><span data-ru=" 1" data-en=" 1"> 1</span><b lang="ru">Неделя:</b><span lang="ru"> 1</span><b lang="en">Week:</b><span lang="en"> 1</span></span>
    </div>
    <h1 data-ru="Гейм-Питч и Цифровое Экспо: Demo Day" data-en="Game Pitch & Digital Expo: Demo Day">Game Pitch va Digital Expo: Demo Day</h1>
    <p class="lede" data-ru="Время представить миру свой игровой проект: персонажи, лор и концепт-арты! Искусство питча, живое демо и сбор отзывов игроков." data-en="Time to showcase your game universe: NPCs, lore, and concept art! The art of game pitching, live demos, and playtest feedback.">1 hafta davomida yaratgan o'yin olamingiz, NPC botlaringiz va konsept-artlaringizni taqdim etish vaqti keldi! Pitching san'ati, jonli namoyish va o'yinchilardan fikr (feedback) olish.</p>
  </div>
</section>

<section class="slide" data-phase="Pitch Nima|Что такое Питч|What is a Pitch" data-time="3–7">
  <div class="eyebrow"><span data-ru="Искусство Питча" data-en="The Art of Pitching">Geymdev Taqdimoti</span></div>
  <h2 data-ru="Что такое Питч: Как Зажечь Игроков за 2 Минуты" data-en="What is a Game Pitch: Hooking Players in 2 Minutes">Geym-Pitch Nima: 2 Daqiqada O'yin G'oyasini Himoya Qilish</h2>
  <p data-ru="Питч (Pitch) — это короткая, мощная презентация вашей игры перед издателями или игроками:" data-en="A Pitch is a high-impact, concise presentation showcasing your game vision to publishers and players:">Pitch — bu o'z o'yin g'oyangiz, xarakterlari va innovatsiyasini 2 daqiqada qiziqarli ko'rsatib berish san'atidir:</p>
  <div class="cols c2" style="margin-top:15px;">
    <div class="box">
      <h3 style="color:var(--ink-2);" data-ru="Скучная Презентация ❌" data-en="Boring Presentation ❌">Zerikarli Taqdimot ❌</h3>
      <p data-ru="<i>'Ну, у меня тут игра... там персонаж бегает, потом прыгает... короче, весело, поиграйте.'</i> Нет энергии, нет уникальности." data-en="<i>'Well, here is a game... there is a guy running and jumping... it's fun, check it out.'</i> Zero energy, zero uniqueness."><i>"Mening o'yinimda bir qahramon bor, u yuguradi, keyin sakraydi... qisqasi zo'r, o'ynab ko'ring."</i> Qiziqish yo'q, o'ziga xoslik yo'q.</p>
    </div>
    <div class="box" style="border-left:4px solid var(--green);">
      <h3 style="color:var(--green);" data-ru="Победный Питч 🏆" data-en="Winning Game Pitch 🏆">G'olib Geym-Pitch 🏆</h3>
      <p data-ru="<i>'Представьте: 2150 год! Парящий город без гравитации. Вы — кибер-механик, общаетесь с умными ИИ-ботами и спасаете сектор!'</i>" data-en="<i>'Imagine this: 2150! A zero-gravity sky city. You are a cyber-mechanic interacting with dynamic AI bots to save the power grid!'</i>"><i>"Tasavvur qiling: 2150-yil, osmondagi shahar! Siz reaktorni tuzatuvchi kiber-muhandissiz. Jonli AI botlar bilan savdo qilasiz va dunyoni qutqarasiz!"</i></p>
    </div>
  </div>
</section>

<section class="slide" data-phase="High Concept|Формула Идеи|High Concept" data-time="7–11">
  <div class="eyebrow"><span data-ru="Формула High Concept" data-en="High Concept Formula">High Concept</span></div>
  <h2 data-ru="High Concept: Формула Идеи в Одно Предложение" data-en="High Concept: The One-Sentence Game Formula">High Concept: Har Bir Mashhur O'yinning Qisqa Formulasi</h2>
  <p data-ru="Каждый мировой хит можно описать одной емкой фразой по формуле <b>High Concept</b>:" data-en="Every global blockbuster can be distilled into a single powerful <b>High Concept</b> sentence:">Har qanday jahon darajasidagi o'yinni 1 ta jumlada ifodalash mumkin. Bunga <b>High Concept</b> deyiladi:</p>
  <div class="box" style="background:var(--panel); border-left:5px solid var(--accent); padding:16px;">
    <p style="font-size:1.05em; font-weight:700; color:var(--accent);" data-ru="[Жанр] + [Главная Механика] + [Уникальная Фишка (X-Factor)]" data-en="[Genre] + [Core Mechanic] + [Unique Innovation (X-Factor)]">
      [Janr] + [Bosh Mexanika] + [O'ziga Xos Yangilik (X-Factor)]
    </p>
  </div>
  <ul class="rules" style="margin-top:10px;">
    <li><span class="t" data-ru="<b>Minecraft:</b> Песочница на выживание в бесконечном мире из разрушаемых кубических блоков." data-en="<b>Minecraft:</b> Infinite voxel sandbox survival where players mine and build anything block by block."><b>Minecraft:</b> Cheksiz kubik bloklardan iborat olamda omon qolish va qurilish qumloq-o'yini (sandbox).</span></li>
    <li><span class="t" data-ru="<b>Subnautica:</b> Научно-фантастическое выживание на неизведанной океанической планете с крафтом батискафов." data-en="<b>Subnautica:</b> Sci-fi underwater exploration and survival on an alien ocean planet with submarine crafting."><b>Subnautica:</b> Notanish suv osti sayyorasida batiskaflar yasash va tadqiqot olib borish sarguzashti.</span></li>
    <li><span class="t" data-ru="<b>Наш Проект:</b> Sci-Fi RPG с живыми генеративными AI-персонажами, помнящими каждое действие игрока!" data-en="<b>Our Project:</b> Sci-Fi RPG featuring generative AI NPCs who remember player choices and react dynamically!"><b>Bizning Loyiha:</b> O'yinchi qarorlarini eslab qoluvchi va jonli fikrlovchi AI NPC lari bor kiberpank RPG o'yini!</span></li>
  </ul>
</section>

<section class="slide" data-phase="Pitch Deck|Структура Питча|Pitch Deck" data-time="11–15">
  <div class="eyebrow"><span data-ru="Слайды Питча" data-en="Pitch Deck Slides">Taqdimot Slaydlari</span></div>
  <h2 data-ru="Структура Питч-Дека: 4 Главных Слайда Проекта" data-en="Pitch Deck Architecture: 4 Essential Slides">Professional Game Pitch Deck: 4 Asosiy Bo'lim</h2>
  <p data-ru="Для успешной защиты проекта вам нужны всего 4 информативных слайда:" data-en="To present your game project like a studio founder, structure these 4 core slides:">O'yin loyihangizni professional himoya qilish uchun 4 ta asosiy bo'lim kifoya:</p>
  <div class="grid" style="display:grid; grid-template-columns:1fr 1fr; gap:12px; margin-top:10px;">
    <div class="box">
      <h3 style="color:var(--accent);" data-ru="1. Слайд: Визитка и Концепт 🎮" data-en="1. Slide: Identity & Concept 🎮">1. Tashrif Qog'ozi va High Concept 🎮</h3>
      <p data-ru="Название игры, логотип, слоган и жанр (Roblox RPG, Кибер-песочница)." data-en="Game title, studio logo, high-concept tagline, and core genre (Roblox sandbox, RPG).">O'yin nomi, logotipi, bosh shiori va janri (Roblox RPG, Kiber-sandbox).</p>
    </div>
    <div class="box">
      <h3 style="color:var(--accent);" data-ru="2. Слайд: Лор и Биомы 🗺️" data-en="2. Slide: World Lore & Biomes 🗺️">2. Dunyo Loresi va Biomlar 🗺️</h3>
      <p data-ru="Краткая история мира, 2 соперничающие фракции и главный конфликт вселенной." data-en="World history summary, 2 rival factions, and the central existential conflict.">Olamning qisqacha tarixi, 2 ta dushman fraksiya va dunyodagi asosiy ziddiyat.</p>
    </div>
    <div class="box">
      <h3 style="color:var(--accent);" data-ru="3. Слайд: AI NPC и Геймплей 🤖" data-en="3. Slide: AI NPC & Gameplay 🤖">3. AI NPC va O'yin Mexanikasi 🤖</h3>
      <p data-ru="Имя бота, его System Prompt, роль в квесте и защита от выхода из роли." data-en="Bot identity, System Prompt snippet, role in the quest chain, and safety guardrails.">Bot ismi, uning System Prompti, kvestdagi vazifasi va xarakter chegaralari.</p>
    </div>
    <div class="box">
      <h3 style="color:var(--accent);" data-ru="4. Слайд: Концепт-Арт 🎨" data-en="4. Slide: Concept Art Showcase 🎨">4. Konsept-Art va Vizual Paket 🎨</h3>
      <p data-ru="Сгенерированный Character Sheet главного героя, арт биома и иконки лута." data-en="Generated Character Turnaround sheet, biome environment shot, and item inventory icons.">Bosh qahramonning Character Sheet chizmasi, biom manzarasi va inventar ikonkalari.</p>
    </div>
  </div>
</section>

<section class="slide" data-phase="Live Demo|Живое Демо|Live Demonstration" data-time="15–19">
  <div class="eyebrow"><span data-ru="Живое Демо" data-en="Live Demonstration">Jonli Demo</span></div>
  <h2 data-ru="Live Demo: Как Показать Своего Бота в Реальном Времени" data-en="Live Demo: Showcasing Your AI NPC in Real-Time">Live Demo: O'yin NPC si Bilan Jonli Suhbatni Ko'rsatish</h2>
  <p data-ru="Самая захватывающая часть питча — живой тест бота перед аудиторией:" data-en="The most electrifying moment of any game pitch is the interactive live demo with the audience:">Taqdimotning eng hayajonli qismi — sinfdoshlar ko'z o'ngida bot bilan jonli muloqot o'tkazishdir:</p>
  <ul class="rules">
    <li><span class="t" data-ru="<b>Шаг 1. Запуск:</b> Откройте диалог с ботом, у которого уже активирован ваш System Prompt." data-en="<b>Step 1. Boot:</b> Launch the interface with your pre-configured System Prompt primed."><b>1-Qadam. Boshlash:</b> Oldindan System Prompt kiritilgan bot oynasini ekranga chiqaring.</span></li>
    <li><span class="t" data-ru="<b>Шаг 2. Вызов из зала:</b> Попросите одноклассника задать боту каверзный вопрос по игре." data-en="<b>Step 2. Audience Provocation:</b> Invite an audience member to challenge the NPC with an in-game question."><b>2-Qadam. Sinfdoshlar Savoli:</b> Sinfdoshlaringizdan biriga: "Qahramonimizga savol bering!" deb taklif qiling.</span></li>
    <li><span class="t" data-ru="<b>Шаг 3. Триумф:</b> Покажите, как NPC блестяще отвечает в своем образе, не выходя из роли!" data-en="<b>Step 3. Persona Triumph:</b> Showcase how the NPC delivers in-lore dynamic responses without breaking role! "><b>3-Qadam. Muvaffaqiyat:</b> Bot qanday qilib roldan chiqmasdan, xarakteriga mos javob berganini ko'rsating!</span></li>
  </ul>
</section>

<section class="slide" data-phase="Playtesting|Плейтест и Отзывы|Feedback Loop" data-time="19–23">
  <div class="eyebrow"><span data-ru="Плейтест и Отзывы" data-en="Playtest & Feedback">Playtesting Madaniyati</span></div>
  <h2 data-ru="Плейтестинг: Как Принимать Критику и Улучшать Игру" data-en="Playtesting: Collecting Feedback & Iterating">Playtesting: Haqiqiy O'yinchilar Fikrini Yig'ish</h2>
  <p data-ru="В геймдеве фидбек игроков — это ценнейшее золото. Разработчик слушает критику без обид:" data-en="In game production, player feedback is pure gold. Professional creators embrace criticism constructively:">O'yin sanoatida o'yinchilar fikri — eng qimmatli boylikdir. Professional geym-dizayner xafa bo'lmaydi:</p>
  <div class="cols c2" style="margin-top:15px;">
    <div class="box">
      <h3 style="color:var(--accent);" data-ru="Детская Обида ❌" data-en="Immature Defense ❌">Xafa Bo'lish ❌</h3>
      <p data-ru="<i>'Вы просто ничего не понимаете! Мой мир идеален, а вы играете неправильно!'</i> Игра остается с багами." data-en="<i>'You just don't get my genius! My game is perfect, you are playing it wrong!'</i> Game remains buggy."><i>"Siz mening zo'r o'yinimni tushunmadingiz! Hamma narsa to'g'ri, o'zingiz noto'g'ri o'ynayapsiz!"</i> O'yin xatolari tuzatilmaydi.</p>
    </div>
    <div class="box" style="border-left:4px solid var(--green);">
      <h3 style="color:var(--green);" data-ru="Инженерный Подход ✅" data-en="Engineering Mindset ✅">Professional Yondashuv ✅</h3>
      <p data-ru="<i>'Спасибо за замечание! Где именно квест показался запутанным? Я перепишу System Prompt к релизу!'</i>" data-en="<i>'Awesome catch! Where exactly did the dialogue feel confusing? I will refine the System Prompt before launch!'</i>"><i>"Taklif uchun rahmat! Aynan qaysi joyda dialog tushunarsiz tuyuldi? Keyingi versiyada buni yanada qiziq qilamiz!"</i></p>
    </div>
  </div>
</section>

<section class="slide" data-phase="Roadmap|План Релиза|Project Roadmap" data-time="23–27">
  <div class="eyebrow"><span data-ru="План Релиза" data-en="Release Roadmap">Kelajak Rejasi</span></div>
  <h2 data-ru="Roadmap Проекта: От Концепта к Запуску в Roblox" data-en="Project Roadmap: From Lore Concept to Roblox Launch">Roadmap: G'oyadan Haqiqiy O'yingacha Qadamlar</h2>
  <p data-ru="Как превратить дизайн-документ этой недели в опубликованную игру? 3 шага дорожной карты:" data-en="How does this week's design document evolve into a published game? 3 roadmap milestones:">1 hafta davomida to'plangan materiallarni haqiqiy o'yinga aylantirishning 3 ta bosqichi:</p>
  <ul class="rules">
    <li><span class="t" data-ru="<b>Этап 1: Альфа-Прототип (Сейчас):</b> Лор, архитектура квестов, визуальный пак и протестированный System Prompt." data-en="<b>Phase 1: Alpha Prototype (Current):</b> Lore Bible, questlines, visual concept pack, and battle-tested System Prompt."><b>1-Bosqich: Alfa-Prototip (Hozirgi holat):</b> Dunyo loresi, kvestlar tuzilmasi, vizual paket va sinalgan System Prompt.</span></li>
    <li><span class="t" data-ru="<b>Этап 2: Сборка в Движке (Следующий шаг):</b> Перенос концептов в Roblox Studio или игровой веб-движок, скриптинг." data-en="<b>Phase 2: Engine Assembly (Next step):</b> Importing assets into Roblox Studio / Web game engine, attaching AI API."><b>2-Bosqich: Dvigatelga Ko'chirish:</b> Konseptlarni Roblox Studio yoki Web o'yin motoriga kiritish, botlarni API orqali ulash.</span></li>
    <li><span class="t" data-ru="<b>Этап 3: Релиз и Публикация:</b> Запуск игры для друзей, сбор статистики и первое обновление (Update 1.0)!" data-en="<b>Phase 3: Launch & Community:</b> Publishing to the public, tracking retention analytics, and releasing Update 1.0! "><b>3-Bosqich: Ommaviy Reliz:</b> O'yinni do'stlar va dunyo o'yinchilari uchun e'lon qilish hamda 1.0 yangilanishini chiqarish!</span></li>
  </ul>
</section>

<section class="slide" data-phase="Kelajak Kasbi|Профессии Будущего|Future Careers" data-time="27–31">
  <div class="eyebrow"><span data-ru="Профессии Будущего" data-en="Future Careers">Kelajak Texnologiyalari</span></div>
  <h2 data-ru="Профессии Будущего: Промпт-Инженер и Архитектор Миров" data-en="Future Careers: AI Prompt Engineer & World Architect">Kelajak Kasblari: AI Prompt Muhandisi va Geym-Dizayner</h2>
  <p data-ru="Ученики 5-6 классов сегодня — это создатели индустрии интерактивных развлечений завтра:" data-en="Today's 5-6th graders are tomorrow's architects of the global interactive economy:">Bugungi 5-6-sinf o'quvchilari kelajakda butun boshli virtual olamlarni boshqaruvchi mutaxassislarga aylanadi:</p>
  <div class="cols c2" style="margin-top:15px;">
    <div class="box">
      <h3 style="color:var(--accent);" data-ru="AI Prompt Engineer 💻" data-en="AI Prompt Engineer 💻">AI Prompt Muhandisi 💻</h3>
      <p data-ru="Специалист, создающий логику ботов, системные промпты и правила взаимодействия между игроками и ИИ." data-en="Engineers writing complex agentic prompts, conversational system logic, and neural guardrails.">Botlar miyasi, xavfsizlik cheklovlari va sun'iy intellekt xatti-harakatlarini boshqaruvchi mutaxassis.</p>
    </div>
    <div class="box" style="border-left:4px solid var(--green);">
      <h3 style="color:var(--green);" data-ru="Game World Architect 🌐" data-en="Game World Architect 🌐">O'yin Olamlari Arxitektori 🌐</h3>
      <p data-ru="Гейм-дизайнер, проектирующий биомы, нарратив, экономику и сюжетные развилки многопользовательских миров." data-en="Lead designers conceiving biomes, branching narrative lore, virtual economies, and player journeys.">Virtual biomlar, o'yin iqtisodiyoti, kvestlar va sarguzashtlar zanjirini loyihalashtiruvchi bosh dizayner.</p>
    </div>
  </div>
</section>

<section class="slide" data-phase="Demo Day Expo|Большой Финал|Grand Finale" data-time="31–36">
  <div class="eyebrow"><span data-ru="Большой Финал" data-en="Grand Finale">Sinf Ko'rgazmasi</span></div>
  <h2 data-ru="Demo Day Expo: Презентация Проектов перед Классом!" data-en="Demo Day Expo: Presenting World Projects to the Class!">Demo Day Expo: Har Bir Jamoa O'z Loyihasini Himoya Qiladi!</h2>
  <p data-ru="Начинается главная битва идей! У каждой команды ровно 2 минуты на триумфальное выступление:" data-en="The grand showcase begins! Every indie creator team has 2 minutes on the main stage:">G'oyalar ko'rgazmasi boshlandi! Har bir jamoada sahnada o'zini ko'rsatish uchun roppa-rosa 2 daqiqa bor:</p>
  <div class="cols c2" style="margin-top:15px;">
    <div class="box">
      <h3 style="color:var(--green);" data-ru="Тайминг Питча (2 мин)" data-en="Pitch Timing (2 min)">Taqdimot Rejasi (2 daq)</h3>
      <p data-ru="30 сек: High Concept и название. 30 сек: Лор и показ концепт-арта. 60 сек: Живой диалог с ботом!" data-en="30s: High Concept & title. 30s: World lore & concept art reveal. 60s: Interactive live bot demo!">30 sek: High Concept va nom. 30 sek: Olam loresi va konsept-art namoyishi. 60 sek: Bot bilan jonli muloqot!</p>
    </div>
    <div class="box" style="border-left:4px solid var(--accent);">
      <h3 style="color:var(--accent);" data-ru="Оценка Одноклассников" data-en="Peer Review Rubric">Sinfdoshlar Bahosi</h3>
      <p data-ru="Каждый зритель голосует за самый оригинальный мир, лучший арт и самого неподкупного NPC!" data-en="Peers vote for the most inventive world lore, sharpest concept art, and most resilient in-character NPC!">Tomoshabinlar eng original olam, eng chiroyli konsept-art va roldan chiqmagan eng aqlli NPC ga ovoz beradi!</p>
    </div>
  </div>
</section>

<section class="slide" data-phase="Uy vazifasi|Домашка|Homework" data-time="36–40">
  <div class="eyebrow"><span data-ru="Домашнее задание" data-en="Homework">Uyga vazifa</span></div>
  <h2 data-ru="Домашка: Оформить Game Design Document (GDD) в Портфолио" data-en="Homework: Compile Your Final Game Design Document (GDD)">Uy vazifasi: To'liq O'yin Hujjatini (GDD) Portfolioga Joylash</h2>
  <div class="hw">
    <div style="display:grid; gap:16px">
      <p class="lede" data-ru="Соберите все наработки 1-й недели в единый Game Design Document (GDD):" data-en="Consolidate all week 1 milestones into a complete Game Design Document (GDD):">1-hafta davomida yaratilgan barcha ishlaringizni yagona "Game Design Document" (GDD) ga jamlang:</p>
      <ul class="plain">
        <li><span class="t" data-ru="Объедините: High Concept, Лор мира, System Prompt для NPC и концепт-арты" data-en="Combine: High Concept, World Lore Bible, NPC System Prompt, and Concept Art">Birlashtiring: O'yin nomi, High Concept, Dunyo loresi, NPC System Prompti va Konsept-artlar.</span></li>
        <li><span class="t" data-ru="Запишите 3 главных отзыва одноклассников с сегодняшнего Demo Day" data-en="Record 3 actionable feedback insights received from classmates during Demo Day">Bugungi ko'rgazmada sinfdoshlaringizdan olgan 3 ta eng foydali taklif va fikrlarni yozing.</span></li>
        <li><span class="t" data-ru="Оформите цифровую папку проекта для своего портфолио разработчика" data-en="Package the materials into a digital portfolio showcase folder ready for production">O'z kelajak geymdev portfoliongiz uchun loyihaning raqamli to'plamini tayyorlang.</span></li>
      </ul>
    </div>
    
    <div class="grade">
      <div class="tag" data-ru="10-балльная шкала" data-en="10 point rubric">10 ballik mezon</div>
      <div class="g"><span><span data-ru="Полный GDD документ" data-en="Complete GDD Package">To'liq GDD hujjati</span></span><b>4</b></div>
      <div class="g"><span><span data-ru="Защита на Demo Day" data-en="Demo Day Showcase">Ko'rgazmadagi taqdimot</span></span><b>4</b></div>
      <div class="g"><span><span data-ru="Сдано вовремя" data-en="On-time Submission">Vaqtida topshirilgani</span></span><b>2</b></div>
      <div class="g"><span><b><span data-ru="Итого" data-en="Total">Jami</span></b></span><b>10</b></div>
    </div>
  </div>
</section>
"""

l6_notes = {
  "uz": [
    "Darsni boshlash: O'quvchilarni tabriklang — bugun 1-haftaning eng katta tadbiri: Demo Day ko'rgazmasi! Mavzu: Geym-pitch va taqdimot.",
    "Geym-pitch nima: 2 daqiqada o'yin g'oyasini ishtiyoq bilan ko'rsatish. Zerikarli hikoya bilan g'olibona pitch farqi.",
    "High Concept formulasi: Janr + Bosh mexanika + X-faktor. Minecraft va Subnautica misollarida 1 jumlada o'yinni sotish siri.",
    "Pitch Deck tuzilmasi: 4 ta asosiy slayd — Konsept vizitkasi, Dunyo loresi, AI NPC roli va Konsept-art to'plami.",
    "Live Demo qoidalari: Auditoriya bilan jonli muloqot. Sinfdoshlardan savol so'rash va botning xarakterini jonli ko'rsatish.",
    "Playtesting va fikr-mulohaza (feedback): O'yinchilar tanqidini xafa bo'lmasdan qabul qilish va xatolarni tuzatish madaniyati.",
    "Roadmap: G'oyadan haqiqiy Roblox/Web o'yingacha bo'lgan 3 bosqich — Prototip, Dvigatelga ko'chirish va Reliz.",
    "Kelajak kasblari: 11 yoshda AI Prompt muhandisi va virtual olamlar dizayneri bo'lish imkoniyatlari.",
    "Demo Day Expo: Har bir jamoaga 2 daqiqa beriladi. Sinfdoshlar ovoz beradi va loyihalarni baholaydi.",
    "Uy vazifasi: Hafta davomida yaratilgan barcha ishlarni bitta 'Game Design Document' (GDD) ga jamlab, portfolioga saqlash."
  ],
  "ru": [
    "Вводная часть: Поздравьте учеников с финалом 1-й недели. Сегодня главный праздник: Demo Day! Тема: Гейм-питч и презентация игры.",
    "Что такое питч: Как за 2 минуты заразить своей идеей игроков и инвесторов. Сравните вялое бормотание и энергичный рассказ.",
    "Формула High Concept: Жанр + Главная механика + X-фактор. Разберите примеры культовых игр, описанных в одно предложение.",
    "Структура Pitch Deck: 4 ключевых слайда — Визитка концепта, Лор и биомы, AI NPC и геймплей, Галерея концепт-арта.",
    "Правила Live Demo: Как проводить живой интерактив с залом. Дайте возможность зрителям протестировать бота.",
    "Плейтестинг и фидбек: Культура взрослого разработчика — слушать критику без обид и использовать ее для полировки игры.",
    "Roadmap проекта: 3 шага к релизу — Альфа-прототип лора, сборка в движке (Roblox Studio) и публичный релиз 1.0.",
    "Профессии будущего: Промпт-инженер игровых ботов и архитектор виртуальных миров как востребованные карьеры.",
    "Demo Day Expo: Каждой команде дается ровно 2 минуты на питч и живое демо. Голосование класса за лучшие проекты.",
    "Домашнее задание: Собрать материалы всех уроков недели в итоговый Game Design Document (GDD). Напомните 10-балльный регламент."
  ],
  "en": [
    "Introduction: Celebrate Week 1 finale: Demo Day! Frame the mission: presenting their game universes to the class like studio founders.",
    "What is a Game Pitch: Hooking players in 2 minutes. Contrast low-energy monologues with electrifying high-concept storytelling.",
    "High Concept Formula: Genre + Core Loop + X-Factor. Break down how Minecraft and Subnautica sell their premise in one crisp line.",
    "Pitch Deck Architecture: 4 vital slides — Identity & Premise, Lore & Factions, AI NPC Gameplay, and Concept Art Pack.",
    "Live Demo Mastery: Conducting audience-driven interactive tests. Let peers interrogate the NPC in real time.",
    "Playtesting & Feedback Culture: The pro studio mindset — embracing critique constructively to iterate mechanics before launch.",
    "Roadmap: 3 milestones from alpha document to live Roblox/Web game deployment and version 1.0 updates.",
    "Future Careers: Prompt Engineering and Virtual World Architecture as high-impact real-world career paths.",
    "Demo Day Expo: 2-minute timed team pitch blitz featuring live bot interactions and peer-reviewed voting.",
    "Homework: Consolidate all week 1 outputs into a unified Game Design Document (GDD) for their digital portfolio. Review 10-pt rubric."
  ]
}

# --- WRITE LESSON 5 ---
p5_html = make_presentation("05-dars: Kiber-Detektiv: Deepfake va AI Xavfsizligi", l5_slides, l5_notes)
with open(os.path.join(BASE_DIR, "05-dars-ai-siri-va-detektiv/prezentatsiya.html"), "w", encoding="utf-8") as f:
    f.write(p5_html)
print("Lesson 5 presentation generated successfully.")

# --- WRITE LESSON 6 ---
p6_html = make_presentation("06-dars: Game Pitch va Digital Expo: Demo Day", l6_slides, l6_notes)
with open(os.path.join(BASE_DIR, "06-dars-sehrli-korgazma/prezentatsiya.html"), "w", encoding="utf-8") as f:
    f.write(p6_html)
print("Lesson 6 presentation generated successfully.")

