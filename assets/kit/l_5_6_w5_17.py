# -*- coding: utf-8 -*-
"""5-6-sinf · 5-hafta · 17-dars — Parollar Jangi va Brute-Force: Nega '123456' Bir Sekundda Yiqiladi?"""

import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from build import (Lesson, slide, title_slide, box, code, media_box, el, i18n,
                   sheet_header, mission, table, sheet_box, rubric, writelines, sign_box)

D = "classes/5-6-sinf/5-hafta/17-dars-parollar-jangi-va-brute-force"

TITLES = {
    "uz": "17-dars: Parollar Jangi — Nega '123456' Bir Sekundda Yiqiladi?",
    "ru": "Урок 17: Битва Паролей — Почему «123456» Падает за Секунду?",
    "en": "Lesson 17: Password Wars — Why '123456' Dies in One Second",
}
SHEET_TITLES = {k: v + (" — Ish Varaqasi" if k == "uz" else
                        " — Рабочий Лист" if k == "ru" else " — Worksheet")
                for k, v in TITLES.items()}

S = []

# 1. Title Slide
S.append(title_slide(
    ph=("Kirish", "Введение", "Intro"), time="0–3",
    eyebrow=("CyberSecurity · 17-dars · 5–6-sinf (Kiber-Qalqon)",
             "CyberSecurity · Урок 17 · 5–6 класс (Кибер-Щит)",
             "CyberSecurity · Lesson 17 · Grades 5–6 (Cyber-Shield)"),
    h1=("Parollar Jangi: Xakerlar Qanday Buzadi?",
        "Битва Паролей: Как Взламывают Хакеры?",
        "Password Wars: How Hackers Crack Your Accounts"),
    lede=("Sizning Telegram, Roblox, Brawl Stars yoki Google akkauntingizni qaroqchilardan nima asrab turadi? "
          "Faqat bitta kalit — <b>sizning parolingiz</b>. Ammo millionlab odamlar hali ham <i>'123456'</i> yoki o'z ismini qo'yishadi. "
          "Bugun biz xakerlar parollarni qanday sekundlarda taxmin qilishini (Brute-Force), "
          "nega kompyuterlar uchun 6 ta raqam kulgili o'yinchoq ekanini va Koinot yashaguncha buzilmaydigan <b>Super-Passphrase</b> "
          "yaratish sirini o'rganamiz!",
          "Что защищает ваш Telegram, Roblox, Brawl Stars или Google аккаунт от угона? "
          "Всего один рубеж — <b>ваш пароль</b>. Но миллионы людей по-прежнему ставят <i>«123456»</i> или год рождения. "
          "Сегодня мы разберём, как хакерские роботы подбирают пароли за доли секунды (Brute-Force), "
          "почему 6 цифр взламываются мгновенно и как создать <b>несокрушимый пароль-фразу</b>, "
          "который не взломают даже через миллион лет!",
          "What stands between an attacker and your Telegram, Roblox, Brawl Stars, or Google account? "
          "Just one defense layer — <b>your password</b>. Yet millions still rely on <i>'123456'</i> or their birthday. "
          "Today we investigate how automated bots crack passwords in milliseconds (Brute-Force), "
          "why 6 digits offer zero protection, and how to craft an unbreakable <b>Super-Passphrase</b> "
          "that would outlast the stars!"),
    meta=[("<b>Fan:</b> Kiberxavfsizlik · Raqamli Gigiyena",
           "<b>Предмет:</b> Кибербезопасность · Цифровая Гигиена",
           "<b>Subject:</b> CyberSecurity · Digital Hygiene"),
          ("<b>Kohorta:</b> 5–6-sinf (10–12 yosh)",
           "<b>Когорта:</b> 5–6 класс (10–12 лет)",
           "<b>Cohort:</b> Grades 5–6 (Ages 10–12)"),
          ("<b>Hafta:</b> 5 (1-soat)", "<b>Неделя:</b> 5 (1-й час)", "<b>Week:</b> 5 (Hour 1)")],
))

# 2. Problem: Speed shaking his head Meme
S.append(slide(
    ph=("Muammo", "Проблема", "The Flaw"), time="3–7",
    eyebrow=("Qanday parollar xavfli?", "Опасные иллюзии", "Dangerous Habits"),
    title=("'Mening Parolimni Hech Kim Bilmaydi' Deb O'ylaysizmi?",
           "Думаете, Ваш Пароль «target2026» Никто Не Угадает?",
           "Think Your Password 'target2026' is Safe? Think Again!"),
    body='<div class="cols">\n'
         + box("red", ("Xato Tushuncha: Xakerlar Qo'lda Termaydi! ❌", "Миф: Хакеры Не Сидят и Не Вводят Буквы Руками ❌", "Myth: Hackers Don't Type Guesses Manually ❌"),
               items=[
                   ("Ko'pchilik o'ylaydi: <i>'Hacker mening do'stim emas-ku, mushugimning ismini qayerdan bilsin?'</i>",
                    "Многие думают: «Хакер же меня не знает, откуда ему знать кличку моей кошки?»",
                    "Common myth: <i>'The hacker doesn't know me, how could they guess my dog's name?'</i>"),
                   ("<b>Haqiqat:</b> Hackerlar parolni qo'lda termaydi! Ular maxsus <b>Brute-force (Qo'pol kuch)</b> dasturlarini ishga tushirishadi.",
                    "<b>Реальность:</b> Пароли подбирают скрипты и видеокарты, перебирающие миллиарды комбинаций в секунду!",
                    "<b>Reality:</b> High-speed bot arrays and GPU rigs test billions of cryptographic guesses per second!"),
                   ("Oddiy kompyuter soniyasiga <b>10,000,000,000 (10 milliard)</b> ta parolni tekshirib chiqa oladi!",
                    "Современный кластер проверяет до 10 миллиардов комбинаций каждую секунду!",
                    "Modern botnets compute up to 10 billion candidate hashes every single second!")
               ])
         + media_box("speed-speed-shaking-his-head.mp4")
         + '</div>'
))

# 3. Math: Combination Explosion
S.append(slide(
    ph=("Kombinatorika", "Комбинаторика", "Combinatorics"), time="7–11",
    eyebrow=("Oddiy matematika", "Математика перебора", "Combinatorial Math"),
    title=("Nega Raqamlar Oson, Belgilar Esa Buzib Bo'lmas Qal'a?",
           "Магия Длины: Почему 6 Цифр — Это 0.001 Секунды?",
           "The Math of Entropy: Why Digits Fall in Milliseconds"),
    body=table(
        headers=[("Parol Turi", "Тип Пароля", "Password Type"),
                 ("Misol", "Пример", "Sample"),
                 ("Jami Variantlar Soni", "Число Комбинаций", "Total Combinations"),
                 ("Buzish Vaqti (Brute-Force)", "Время Взлома", "Crack Time (RTX 4090)")],
        rows=[
            [("<b>Faqat 6 ta raqam</b>", "<b>Только 6 цифр</b>", "<b>6 Numeric Digits</b>"),
             ("<code>123456</code>, <code>201408</code>", "<code>123456</code>, <code>201408</code>", "<code>123456</code>, <code>201408</code>"),
             ("10 &times; 10 &times; 10 &times; 10 &times; 10 &times; 10 = <b>1,000,000</b>",
              "10 в 6-й степени = 1 миллион вариантов",
              "10^6 = 1 Million possibilities"),
             ("⚡ <b>0.001 sekund!</b> (Ko'z yumib ochguncha)",
              "⚡ <b>0.001 секунды!</b> (Мгновенно)",
              "⚡ <b>0.001 seconds!</b> (Instantaneous)")],
            [("<b>8 ta kichik harf</b>", "<b>8 строчных букв</b>", "<b>8 Lowercase Letters</b>"),
             ("<code>parollar</code>, <code>shaxzod</code>", "<code>parollar</code>, <code>shaxzod</code>", "<code>parollar</code>, <code>shaxzod</code>"),
             ("26 &times; 26... = <b>208,000,000,000</b> (208 milliard)",
              "26 в 8-й степени = 208 миллиардов",
              "26^8 = 208 Billion possibilities"),
             ("⏱️ <b>2–3 sekund!</b>",
              "⏱️ <b>2–3 секунды!</b>",
              "⏱️ <b>2–3 seconds!</b>")],
            [("<b>12 ta aralash belgi (Passphrase)</b>", "<b>12 символов (Слова + Знаки)</b>", "<b>12 Mixed Characters</b>"),
             ("<code>Olma!Mars#99</code>", "<code>Olma!Mars#99</code>", "<code>Olma!Mars#99</code>"),
             ("94 &times; 94... = <b>475,000,000,000,000,000,000,000</b>",
              "94 в 12-й степени (секстиллионы вариантов)",
              "94^12 = 4.75 Sextillion possibilities"),
             ("🛡️ <b>34,000 YIL!</b> (Buzib bo'lmaydi)",
              "🛡️ <b>34 000 ЛЕТ!</b> (Невозможно взломать)",
              "🛡️ <b>34,000 YEARS!</b> (Unbreakable)")]
        ]
    )
))

# 4. Dictionary Attacks & Leaked Passwords
S.append(slide(
    ph=("Lug'at Hujumi", "Словарные Атаки", "Dictionary Attacks"), time="11–15",
    eyebrow=("Dunyoning eng yomon parollari", "Худшие пароли мира", "Worst Passwords Ever"),
    title=("Lug'at Hujumi: Dunyodagi Eng Yomon 5 Ta Parol",
           "Словарная Атака: ТОП-5 Худших Паролей Планеты",
           "Dictionary Attack: The Top 5 Worst Passwords on Earth"),
    body='<div class="cols">\n'
         + box("navy", ("Dunyodagi Eng Ko'p Ishlatiladigan Xato Parollar", "Самые Популярные и Уязвимые Пароли", "Most Leaked Weak Passwords"),
               items=[
                   ("1. <code>123456</code> (Dunyoda 40 million marta sizib chiqqan)",
                    "1. <code>123456</code> — абсолютный чемпион утечек (более 40 млн аккаунтов).",
                    "1. <code>123456</code> — leaked in over 40M database dumps."),
                   ("2. <code>admin</code> yoki <code>password</code> (Standart tizim parollari).",
                    "2. <code>admin</code> или <code>password</code> — заводские настройки.",
                    "2. <code>admin</code> or <code>password</code> — default credentials."),
                   ("3. <code>qwerty</code> yoki <code>111111</code> (Klaviatura chiziqlari).",
                    "3. <code>qwerty</code> или <code>111111</code> — соседние клавиши.",
                    "3. <code>qwerty</code> or <code>111111</code> — linear keyboard rows."),
                   ("4. Ism + tug'ilgan yil: <code>ali2012</code>, <code>madina2014</code>.",
                    "4. Имя + год рождения: легко находятся через соцсети за 1 минуту.",
                    "4. Name + birth year: easily OSINT harvested from social media in 60s.")
               ])
         + box("purple", ("Xakerlar Qanday Tekshiradi?", "Как Работает Словарный Перебор?", "How Dictionary Search Operates"),
               items=[
                   ("Xakerlar internetdan oldin buzilgan <b>milliardlab parollar lug'atini</b> yuklab oladi.",
                    "У хакеров есть базы из миллиардов реальных утекших паролей (RockYou).",
                    "Hackers maintain corpus wordlists (RockYou, SecLists) with billions of real passwords."),
                   ("Ular nishonga olingan akkauntga birinchi navbatda shu lug'atdagi eng mashhur 10,000 ta so'zni jo'natadi.",
                    "Скрипт проверяет топ-10 000 слов за долю секунды до начала полного перебора.",
                    "Bot scripts spray top 10,000 dictionary words before attempting brute calculations."),
                   ("Agar parolingiz shu ro'yxatda bo'lsa — akkauntingiz <b>bir zumda yo'qotiladi!</b>",
                    "Если ваш пароль есть в словаре, никакой сложный алгоритм вас не спасёт!",
                    "If your password appears on wordlists, your account is compromised instantly!")
               ])
         + '</div>'
))

# 5. The Passphrase Secret: 3 Unrelated Words
S.append(slide(
    ph=("Yechim", "Решение", "The Solution"), time="15–18",
    eyebrow=("Kiber-Gigachad siri", "Секрет надежности", "The Passphrase Secret"),
    title=("Buzib Bo'lmas Parol Yaratish: 3 Ta So'z Qoidasi",
           "Правило Трёх Слов: Как Создать Пароль, Который Не Забудешь?",
           "The 3-Word Passphrase: Easy to Remember, Impossible to Crack"),
    body='<div class="cols">\n'
         + box("green", ("Buzib Bo'lmas 'Passphrase' Retsepti 🛡️", "Рецепт Несокрушимой Пароль-Фразы 🛡️", "Unbreakable Passphrase Formula 🛡️"),
               items=[
                   ("Eski qoida: <i>'Bitta so'z olib, o'rtasiga raqam qo'y'</i> (Masalan <code>Target123</code>) — BU ESKIRGAN VA XAVFLI!",
                    "Старый совет «Возьми слово и добавь 123» безнадежно устарел и легко взламывается.",
                    "Old advice: <i>'Pick a word and append 123'</i> is completely obsolete and trivial to crack."),
                   ("<b>Yangi Oltin Standart:</b> O'zaro bog'liq bo'lmagan <b>3 ta qiziq so'z</b> tanlang!",
                    "<b>Новый стандарт:</b> Выберите <b>три случайных ярких слова</b>, не связанных по смыслу!",
                    "<b>Modern Gold Standard:</b> Chain <b>3 completely unrelated visual nouns</b>!"),
                   ("Masalan: <code>Muzqaymoq</code> + <code>Kosmos</code> + <code>Traktor</code>.",
                    "Например: <code>Мороженое</code> + <code>Космос</code> + <code>Трактор</code>.",
                    "For example: <code>IceCream</code> + <code>Cosmos</code> + <code>Tractor</code>."),
                   ("Oralariga belgi va raqam qo'shing: <code>Muzqaymoq!Kosmos#77</code>. Bu parolni eslab qolish oson, ammo <b>superkompyuterlar uchun 100,000 yilga yetadigan boshog'riq!</b>",
                    "Добавьте разделители и цифры: <code>Morozhenoe!Kosmos#77</code>. Вы запомните за секунду, а компьютер не подберет за 100 000 лет!",
                    "Add symbols and numbers: <code>IceCream!Cosmos#77</code>. Effortless for you to recall, impossible for supercomputers to brute-force!")
               ])
         + box("blue", ("Qanday Qilib Yodda Qoladi? (Vizual Assotsiatsiya)", "Как Запомнить Без Труда? (Ассоциации)", "Visual Memory Mechanics"),
               items=[
                   ("<b>1. Hayolingizda rasm chizing:</b> <i>'Kosmosda uchayotgan Muzqaymoq ushlagan Traktor'</i>.",
                    "<b>1. Визуальный образ:</b> «Трактор летит в космосе и ест мороженое». Мозг мгновенно помнит эту нелепую картину!",
                    "<b>1. Mental Picture:</b> <i>'A tractor floating in deep space eating ice cream'</i>. The brain memorizes absurd imagery effortlessly!"),
                   ("<b>2. Maxsus belgilar qo'ying:</b> So'zlar orasiga bo'sh joy o'rniga <code>!</code>, <code>#</code> yoki <code>$</code> qo'ying.",
                    "<b>2. Разделители:</b> Вместо пробелов поставьте символы <code>!</code>, <code>#</code> или <code>$</code>.",
                    "<b>2. Delimiters:</b> Connect nouns with punctuation like <code>!</code>, <code>#</code>, or <code>$</code>."),
                   ("<b>3. Yoqtirgan raqamingiz:</b> Oxiriga o'zingizning sevimli raqamingizni (masalan <code>77</code>) qo'shing.",
                    "<b>3. Любимое число:</b> В конец добавьте число, которое вы никогда не забудете.",
                    "<b>3. Numeric Salt:</b> Conclude with a favorite two-digit integer (e.g. <code>77</code>)."),
                   ("<b>Natija:</b> <code>Muzqaymoq!Kosmos#77</code> &mdash; yozish oson, buzish esa imkonsiz!",
                    "<b>Итог:</b> <code>Morozhenoe!Kosmos#77</code> — вводится за 2 секунды, а хакеры бессильны.",
                    "<b>Result:</b> <code>IceCream!Cosmos#77</code> — fast to type, cryptographically impenetrable.")
               ])
         + '</div>'
))

# 6. Ronaldo Meme: The Reused Password Catastrophe
S.append(slide(
    ph=("Xavfli Xato", "Фатальная Ошибка", "Password Reuse"), time="18–22",
    eyebrow=("Bir xil parol xatosi", "Один пароль на всё", "The Password Reuse Trap"),
    title=("Bitta Parolni Hamma Saytga Qo'yish — O'z Qopqoningiz!",
           "Один Пароль на Все Сайты — Прямой Путь к Взлому!",
           "Using the Same Password Everywhere is an Open Trap!"),
    body='<div class="cols">\n'
         + box("red", ("Zanjirli Halokat Qanday Yuz Beradi?", "Как Происходит Каскадный Взлом?", "How Credential Stuffing Works"),
               items=[
                   ("Siz bir xil parolni Brawl Stars, Roblox, maktab sayti va Telegramga qo'ygansiz.",
                    "Вы используете один и тот же пароль для Telegram, Roblox и неизвестного игрового форума.",
                    "You reuse the identical password across Telegram, Roblox, Discord, and school portals."),
                   ("Buzg'unchi zaif, arzimas bir o'yin saytini buzadi va u yerdagi parolingizni bilib oladi.",
                    "Злоумышленники взламывают маленький ненадежный форум и забирают оттуда базу логинов.",
                    "Adversaries breach a poorly defended third-party forum and dump its database."),
                   ("Keyin o'sha parol bilan sizning <b>Telegram, Instagram va Gmail</b> akkauntlaringizga kirib ko'radi!",
                    "Затем этот же пароль боты пробуют применить к вашему Telegram, почте и соцсетям!",
                    "Automated bots instantly credential-stuff that password into Telegram, Gmail, and Steam!"),
                   ("<b>Natija:</b> Bitta kichik sayt tufayli butun raqamli hayotingiz qo'ldan ketadi!",
                    "<b>Итог:</b> Из-за утечки на одном сайте вы теряете доступ ко всем аккаунтам сразу!",
                    "<b>Result:</b> A leak on a single throwaway forum compromises your entire identity!")
               ])
         + media_box("rolando-ronaldo.mp4")
         + '</div>'
))

# 7. Code Dissection: Password Strength Checker in Python / JS
S.append(slide(
    ph=("Kod Tahlili", "Анализ Кода", "Code Dissection"), time="22–26",
    eyebrow=("Dasturchi nigohi", "Как думает валидатор", "Under the Hood"),
    title=("Saytlar Parol Kuchini Qanday Hisoblaydi?",
           "Как Сайты Проверяют Сложность Вашего Пароля?",
           "How Web Apps Calculate Password Entropy in JavaScript"),
    body=code("""// Saytlardagi yashil/qizil parol indikatori mantig'i:
function checkPasswordStrength(password) {
  let score = 0;
  
  if (password.length >= 8) score += 20;
  if (password.length >= 12) score += 30; // Uzunlik eng muhimi!
  
  if (/[a-z]/.test(password)) score += 10; // Kichik harf
  if (/[A-Z]/.test(password)) score += 10; // Katta harf
  if (/[0-9]/.test(password)) score += 15; // Raqamlar
  if (/[!@#$%^&*]/.test(password)) score += 15; // Maxsus belgilar

  if (score < 40) return "🔴 O'TA ZAIF! (1 soniyada buziladi)";
  if (score < 70) return "🟡 O'RTACHA (Bir necha kunda buzilishi mumkin)";
  return "🟢 BUZIB BO'LMAS KIBER-QAL'A! (30,000+ yil)";
}""")
))

# 8. Real World Case Studies: The 2012 LinkedIn Leak & RockYou
S.append(slide(
    ph=("Keyslar", "Кейсы", "Real Breaches"), time="26–30",
    eyebrow=("Tarixdagi darslar", "Уроки реальных взломов", "Historic Breaches"),
    title=("Tarixdagi Eng Mashhur O'g'irlangan Parollar Voqeasi",
           "Утечка LinkedIn и База RockYou: 32 Миллиона Паролей",
           "The Historic RockYou & LinkedIn Database Breaches"),
    body='<div class="cols">\n'
         + box("navy", ("RockYou Voqeasi (32 Million Parol)", "Утечка RockYou (32 Миллиона Паролей)", "The RockYou Breach (32M Passwords)"),
               items=[
                   ("2009-yilda RockYou o'yin kompaniyasi buzildi. Ular parollarni shifrlamasdan oddiy matn ko'rinishida saqlagan edi!",
                    "В 2009 году взломали сервис RockYou, где пароли хранились в открытом виде без шифрования!",
                    "In 2009, social gaming company RockYou leaked 32 million unencrypted plaintext passwords!"),
                   ("Ushbu ro'yxat <code>rockyou.txt</code> nomi bilan internetga chiqib ketdi.",
                    "База утекших паролей превратилась в главный инструмент хакеров по всему миру.",
                    "The leaked wordlist became the legendary <code>rockyou.txt</code> dictionary used worldwide."),
                   ("Hatto bugun ham xakerlar birinchi bo'lib o'quvchilar va odamlarning parolini shu ro'yxatdan qidiradi!",
                    "Даже сегодня боты первым делом проверяют именно эти 32 миллиона слов!",
                    "Even today, credential stuffers use this dictionary as their initial attack wave!")
               ])
         + box("purple", ("2FA (Ikki Bosqichli Himoya) — Qutqaruv Halqasi", "Двухфакторная Аутентификация (2FA)", "2FA — The Ultimate Safety Net"),
               items=[
                   ("Tasavvur qiling: xaker parolingizni bilib oldi!",
                    "Представьте: хакер каким-то чудом угадал или украл ваш пароль.",
                    "Imagine an attacker successfully guesses or leaks your password."),
                   ("Ammo sizda <b>2FA (Ikki bosqichli tasdiqlash)</b> yoqilgan bo'lsa, tizim hackerga aytadi: <i>'Telefonga kelgan 6 xonali SMS kodni kirit!'</i>",
                    "Но если у вас включена 2FA, сервис потребует подтверждения через телефон или Telegram!",
                    "If you enabled 2FA, the server halts them: <i>'Enter the 6-digit confirmation code!'</i>"),
                   ("Telefon sizning cho'ntagingizda bo'lgani sababli, hacker parolni bilsa ham <b>hech narsa qila olmaydi!</b>",
                    "Телефон у вас в руках, поэтому злоумышленник остаётся ни с чем!",
                    "Because your physical device holds the token, the hacker remains completely locked out!")
               ])
         + '</div>'
))

# 9. Password Manager: Memory vs Technology
S.append(slide(
    ph=("Asboblar", "Инструменты", "Tools"), time="30–33",
    eyebrow=("Parollar daftarchasi", "Менеджеры паролей", "Password Managers"),
    title=("Hamma Parollarni Qanday Eslab Qolish Mumkin? (Bitwarden & KeePass)",
           "Как Не Забыть 50 Разных Паролей? Менеджеры Паролей",
           "How to Manage 50 Complex Passwords Without Forgetting"),
    body='<div class="cols">\n'
         + box("blue", ("Inson Xotirasining Cheklovi", "Ограничения Человеческой Памяти", "Human Memory Limits"),
               items=[
                   ("Bitta odam 50 ta turli xil murakkab parolni yodda saqlay olmaydi.",
                    "Человеческий мозг не способен помнить 50 длинных бессмысленных комбинаций.",
                    "The human mind cannot reliably memorize 50 unique 16-character passphrases."),
                   ("Shuning uchun odamlar parolini qog'ozga, stikerga yozib monitorda qoldiradi yoki oddiy parol qo'yadi.",
                    "Из-за этого люди пишут пароли на стикерах под клавиатурой или упрощают их до минимума.",
                    "This leads to sticky notes under keyboards or reverting to simplistic repeated passwords."),
                   ("Bu xavfsizlikning eng katta zaif nuqtasidir.",
                    "Это главная причина взломов через человеческий фактор.",
                    "Human memory fatigue is the primary attack vector for social engineering.")
               ])
         + box("green", ("Parollar Menejeri — Raqamli Seyf 🗄️", "Менеджер Паролей — Цифровой Сейф 🗄️", "Password Vault — Your Digital Safe 🗄️"),
               items=[
                   ("<b>Bitwarden / KeePass / Apple Keychain:</b> Siz faqat BITTA bosh parolni (Master Password) eslab qolasiz.",
                    "Вы помните только ОДИН супер-пароль, а программа надежно хранит все остальные в шифрованном виде.",
                    "You memorize only ONE strong Master Password; the vault cryptographically protects the rest."),
                   ("Menejer har bir yangi sayt uchun avtomatik ravishda 20 belgili <code>k8#P!m9$Zq...</code> parollar yaratadi va o'zi kiritadi.",
                    "Менеджер сам генерирует сложнейшие пароли и вставляет их в один клик при входе.",
                    "The vault auto-generates 20-character strings and auto-fills them during legitimate logins."),
                   ("Parolni o'g'irlash yoki adashtirish imkonsiz bo'ladi!",
                    "Подсмотреть или украсть такой пароль через плечо становится невозможно!",
                    "Shoulder surfing or guessing your credentials becomes mathematically impossible!")
               ])
         + '</div>'
))

# 10. Hands-on Lab: Password Strength Arena
S.append(slide(
    ph=("Amaliyot", "Практика", "Hands-on Lab"), time="33–38",
    eyebrow=("Laboratoriya sinovi", "Лабораторная работа", "Hands-on Workshop"),
    title=("Amaliy Ish: Parollar Kuchini Sinash va Super-Passphrase Qurish",
           "Практика: Тестирование Паролей и Создание Супер-Фразы",
           "Hands-on Lab: Password Strength Arena & Passphrase Creation"),
    body='<div class="box blue">\n'
         + el("h3", "Laboratoriya Topshiriqlari (10 Daqiqa)", "Задания Практикума (10 Минут)", "Lab Challenges (10 Minutes)")
         + el("p", "Bugun har bir o'quvchi xavfsiz sinov maydonchasida turli parollarning 'umrini' hisoblaydi va o'zining buzib bo'lmas shaxsiy formulasini yaratadi. (Eslatma: Haqiqiy shaxsiy parollaringizni hech kimga ko'rsatmang!)",
              "Сегодня каждый ученик проверит время жизни разных паролей в симуляторе и составит личную супер-пароль-фразу. (Внимание: никогда не вводите свои реальные пароли в чужие компьютеры!)",
              "Today each student audits password lifespans in a sandboxed simulator and architects an unbreakable personal passphrase. (Rule: Never disclose real personal passwords!)")
         + '</div>\n'
         + table(
             headers=[("Sinov", "Испытание", "Challenge"),
                      ("Kiritilgan Sinov Paroli", "Тестируемый Пароль", "Tested Password"),
                      ("Taxminiy Buzish Vaqti", "Время Взлома", "Estimated Crack Time"),
                      ("Kiber-Baho (🔴/🟡/🟢)", "Вердикт Безопасности", "Verdict")],
             rows=[
                 [("<b>1-Sinov: Raqamlar</b>", "<b>Тест 1: Цифры</b>", "<b>Trial 1: Digits</b>"),
                  ("<code>123456</code> yoki <code>201309</code>", "<code>123456</code> или <code>201309</code>", "<code>123456</code> or birthdate"),
                  ("............................................", "............................................", "............................................"),
                  ("🔴 Juda zaif", "🔴 Очень слабо", "🔴 Very Weak")],
                 [("<b>2-Sinov: Oddiy So'z</b>", "<b>Тест 2: Слово</b>", "<b>Trial 2: Single Word</b>"),
                  ("<code>futbolchi</code> yoki <code>brawlstars</code>", "<code>futbolchi</code> или <code>brawlstars</code>", "<code>football</code> or game title"),
                  ("............................................", "............................................", "............................................"),
                  ("🟡 Xavfli", "🟡 Опасно", "🟡 Vulnerable")],
                 [("<b>3-Sinov: Kiber-Passphrase</b>", "<b>Тест 3: Супер-Фраза</b>", "<b>Trial 3: Passphrase</b>"),
                  ("<code>3 ta so'z + belgi + son</code>", "<code>3 слова + спецсимволы + цифры</code>", "<code>3 words + symbol + number</code>"),
                  ("............................................", "............................................", "............................................"),
                  ("🟢 Buzib bo'lmas!", "🟢 Несокрушимо!", "🟢 Unbreakable!")]
             ]
         )
))

# 11. Security Matrix: Password Rules
S.append(slide(
    ph=("Qoidalar", "Правила", "Golden Rules"), time="38–40",
    eyebrow=("Kiber-Gigiyena qoidalari", "Золотые правила", "Golden Principles"),
    title=("Parol Xavfsizligining 4 Ta Oltin Qoidasi",
           "4 Золотых Правила Парольной Безопасности",
           "The 4 Golden Rules of Password Resilience"),
    body='<div class="cols">\n'
         + box("green", ("1. Uzunlik Qoidasi (12+ Belgi)", "1. Правило Длины (12+ Символов)", "1. Minimum Length (12+ Chars)"),
               items=[
                   ("Har bir qo'shilgan belgi kombinatsiyalar sonini 94 barobar ko'paytiradi!",
                    "Каждый дополнительный символ увеличивает число вариантов почти в 100 раз!",
                    "Every additional character multiplies search complexity by 94!"),
                   ("8 belgili parol bir necha daqiqada, 14 belgili parol esa ming yillarda buziladi.",
                    "8 символов взламываются за минуты, а 14 символов — за тысячи лет.",
                    "An 8-character string falls in minutes, while 14 characters demands millennia.")
               ])
         + box("blue", ("2. Alohidalik Qoidasi (No Reuse)", "2. Уникальность Паролей", "2. No Password Reuse"),
               items=[
                   ("Telegram uchun alohida, Roblox uchun alohida, pochta uchun alohida parol!",
                    "Один пароль — для одного сервиса. Утечка на одном сайте не должна ставить под угрозу другие!",
                    "Unique credentials for Telegram, unique for Roblox, unique for primary email!"),
                   ("Bitta sayt buzilsa ham, qolgan hamma hisoblaringiz 100% xavfsiz qoladi.",
                    "Если утечет база одного сайта, все остальные ваши профили будут в полной безопасности.",
                    "Breaching one forum isolates blast radius, leaving your core identity completely safe.")
               ])
         + box("purple", ("3. Ikki Bosqichli Himoya (2FA)", "3. Включите 2FA Везде", "3. Enforce 2FA Everywhere"),
               items=[
                   ("Telegram sozlamalariga kiring: <b>Maxfiylik &rarr; Ikki bosqichli tekshiruv</b>ni yoqing!",
                    "Зайдите в Telegram прямо сегодня: Конфиденциальность &rarr; Облачный пароль (2FA)!",
                    "Open Telegram settings today: Privacy & Security &rarr; Two-Step Verification!"),
                   ("Bu eng mustahkam kiber-qalqondir.",
                    "Это самая надёжная защита от перехвата аккаунта.",
                    "This serves as the single strongest personal anti-hijacking shield.")
               ])
         + '</div>'
))

# 12. Summary & Homework: The Family Audit
S.append(slide(
    ph=("Xulosa", "Итоги", "Summary"), time="40–43",
    eyebrow=("Uy vazifasi", "Домашнее задание", "Homework Project"),
    title=("Xulosa va Uy Vazifasi: Oilaviy Kiber-Audit (10 Ball)",
           "Итоги и Задание: Семейный Кибер-Аудит (10 Баллов)",
           "Summary & Homework: Family Account Password Audit (10 Pts)"),
    body='<div class="cols">\n'
         + box("blue", ("Bugun Nimalarni O'rgandik?", "Главные Выводы Урока", "Key Takeaways"),
               items=[
                   ("Xakerlar parollarni qo'lda emas, soniyasiga milliardlab taxmin qiluvchi robotlar bilan buzishadi.",
                    "Пароли взламывают не люди, а программы методом миллиардного перебора в секунду.",
                    "Passwords are cracked by automated bot farms evaluating billions of hashes per second."),
                   ("Raqamli qisqa parollar (<code>123456</code>) 0.001 sekundda yo'q qilinadi.",
                    "Короткие цифровые пароли не защищают от взлома даже на доли секунды.",
                    "Short numeric strings provide zero cryptographic friction."),
                   ("Eng kuchli himoya — bu <b>3 ta so'zdan iborat Passphrase va 2FA</b> hisoblanadi.",
                    "Самая надёжная защита — это пароль-фраза из 3 слов в связке с двухфакторной аутентификацией (2FA).",
                    "The ultimate defense is a memorable 3-word Passphrase paired with 2-Factor Authentication.")
               ])
         + box("purple", ("Uy Vazifasi: Oila A'zolaringiz Akkauntini Tekshiring (10 Ball)", "Домашнее Задание: Семейный Аудит (10 Баллов)", "Homework: Family Cyber-Audit Challenge (10 Pts)"),
               items=[
                   ("1. Ota-onangiz yoki akangiz/opangiz bilan birgalikda bitta muhim akkauntni (masalan Telegram) tekshiring.",
                    "1. Вместе с родителями или старшими проверьте защиту одного важного аккаунта (например, Telegram).",
                    "1. Audit one family member's core account (e.g. Telegram or Gmail) alongside them."),
                   ("2. Unda <b>Ikki bosqichli tekshiruv (2FA / Bulutli parol)</b> yoqilganmi yoki yo'qmi ko'ring. Agar yoqilmagan bo'lsa, yoqishga yordamlashing!",
                    "2. Проверьте, включена ли двухфакторная аутентификация (Облачный пароль в Telegram). Если нет — включите!",
                    "2. Verify whether Two-Step Verification is active; assist in configuring it if missing!"),
                   ("3. Ish varaqasidagi audit hisobotini to'ldirib, o'qituvchiga taqdim eting.",
                    "3. Заполните чек-лист аудита в рабочем листе и сдайте на проверку.",
                    "3. Document your audit findings on your worksheet ledger.")
               ])
         + '</div>'
))

# Teacher Notes
N_UZ = [
    ["Kirish", "O'quvchilardan kimning paroli '123456' yoki o'z ismi ekanini so'rang. Kulgili, ammo hayotiy misol bilan darsni boshlang.", "Slaydni oching."],
    ["Muammo", "Speed boshini chayqayotgan memeni ko'rsating. Xakerlar qo'lda emas, soniyasiga 10 milliard ta'minotchi botlar bilan ishlashini ayting.", "Memeni ko'rsating."],
    ["Kombinatorika", "Doskada 10^6 va 94^12 raqamlarini solishtiring. Nega bitta belgi vaqtni 100 barobar oshirishini bolalarga oddiy tushuntiring.", "Jadvalni tahlil qiling."],
    ["Lug'at hujumi", "RockYou faylida 32 million mashhur parol borligini va xakerlar birinchi bo'lib o'shani sinab ko'rishini aytib bering.", "Xato parollarni sanang."],
    ["Passphrase", "3 ta so'z (Muzqaymoq!Mars#77) formulasini bolalarga o'rgating, vizual assotsiatsiyalar tuzing.", "Formulani ko'rsating."],
    ["Ronaldo", "Ronaldo shubha bilan qarayotgan memesi: Bitta parolni hamma joyga qo'yishning fojiasini (Brawl Stars orqali Telegram buzilishi) tushuntiring.", "Memeni ko'rsating."],
    ["Kod", "JavaScript kodidagi o'lchov balini (score) ko'rsating. Uzunlik nega katta harfdan ham muhimroq ekanini ta'kidlang.", "Kodni oching."],
    ["Keyslar", "2FA nima ekanini va nega telefon kodi xakerni to'xtatib qoluvchi qutqaruvchi ekanini hayotiy tushuntiring.", "2FA ni tushuntiring."],
    ["Menejer", "Parollar daftarchasi (Bitwarden) inson xotirasini qanday yengillashtirishini tushuntiring.", "Asboblarni ko'rsating."],
    ["Amaliyot", "O'quvchilar laboratoriya jadvalini to'ldirishsin. Har bir o'quvchi o'zining 3 so'zli super-parolini yaratib ko'rsin.", "Taymerni yoqing (10 daqiqa)."],
    ["Qoidalar", "4 ta oltin qoidani xor bo'lib qaytaring: 12+ belgi, qaytarmaslik, 2FA, sir saqlash.", "Qoidalarni xulosa qiling."],
    ["Xulosa", "Uy vazifasini tushuntiring: uyga borib ota-onaning Telegramida 2FA borligini tekshirish kiber-qahramonlik ekanini ayting.", "Varaqalarni tarqating."]
]

N_RU = [
    ["Введение", "Спросите ребят, у кого пароль «123456» или имя любимого питомца. Начните урок с юмора и интриги.", "Откройте титульный слайд."],
    ["Проблема", "Покажите мем со Спидом, который качает головой. Объясните, что хакеры не печатают руками, а запускают видеокарты-роботы.", "Покажите видео-мем."],
    ["Комбинаторика", "Напишите на доске разницу между 1 миллионом и септиллионами вариантов. Покажите, почему длина решает всё.", "Разберите таблицу."],
    ["Словарная атака", "Расскажите историю базы RockYou на 32 миллиона паролей и почему «ali2012» взломают за 1 секунду.", "Обсудите популярные ошибки."],
    ["Пароль-фраза", "Формула из 3 слов (Мороженое!Космос#77): объясните ассоциативное запоминание без труда.", "Покажите формулу."],
    ["Роналду", "Мем с подозрительным Роналду: покажите опасность использования одного пароля и для игр, и для личной почты.", "Покажите мем."],
    ["Код", "Разберите логику простого JS-валидатора: длина дает больше очков, чем спецсимволы.", "Поясните скрипт."],
    ["Кейсы", "Объясните двухфакторную аутентификацию (2FA) как надежный замок, требующий физический телефон в руках.", "Поясните 2FA."],
    ["Менеджер", "Расскажите о менеджерах паролей, которые избавляют от необходимости держать 50 паролей в голове.", "Разберите менеджеры."],
    ["Практикум", "Курируйте заполнение рабочего листа: тест цифрового пароля, словарного и создание личной супер-фразы.", "Запустите таймер 10 минут."],
    ["Правила", "Закрепите 4 золотых правила: длина 12+, уникальность для каждого сайта, обязательная 2FA.", "Обобщите правила."],
    ["Итоги", "Объясните домашнее задание: провести аудит безопасности Telegram у родителей и включить облачный пароль.", "Соберите рабочие листы."]
]

N_EN = [
    ["Intro", "Ask students how many rely on '123456' or pet names. Hook attention with relatable humor and digital vulnerability.", "Open title slide."],
    ["Problem", "Play the Speed head-shaking meme. Explain that adversaries deploy GPU clusters cracking 10B guesses per second.", "Play video meme."],
    ["Combinatorics", "Contrast 10^6 permutations with 94^12 on whiteboard. Illustrate why string length mathematically dwarfs complexity.", "Review math table."],
    ["Dictionary Attacks", "Narrate the 32M RockYou wordlist history and show why dictionary words crumble immediately.", "Discuss top bad passwords."],
    ["Passphrase", "Teach the 3-word visual passphrase strategy (IceCream!Cosmos#77). Guide mnemonic association.", "Show formula."],
    ["Ronaldo", "Ronaldo suspicious stare meme: unpack the cascade catastrophe of reusing one password across games and Telegram.", "Play video meme."],
    ["Code", "Examine the simple JavaScript entropy scoring rules: length awarded highest points.", "Walk through JS logic."],
    ["Breaches", "Demystify 2FA: even if adversaries harvest a password, the missing physical phone halts the breach.", "Explain 2FA mechanics."],
    ["Managers", "Demonstrate password vaults like Bitwarden that relieve memory fatigue through encrypted auto-fill.", "Review password vaults."],
    ["Lab", "Guide students through worksheet testing: comparing crack times and forging their own 3-word passphrase.", "Start 10-minute lab timer."],
    ["Rules", "Chant the 4 golden rules: 12+ characters, zero reuse, active 2FA, never disclose.", "Summarize principles."],
    ["Summary", "Assign family audit homework: inspecting parents' Telegram settings for active Two-Step Cloud Passwords.", "Collect worksheets."]
]

NOTES = {"uz": N_UZ, "ru": N_RU, "en": N_EN}

# --- Worksheet (Varaqa) ---
V = []
V.append(sheet_header(
    h1=("Kiberxavfsizlik: Parollar Jangi va Kiber-Qalqon",
        "Кибербезопасность: Битва Паролей и Кибер-Щит",
        "CyberSecurity: Password Wars & Cyber-Shield"),
    sub=("Amaliy Laboratoriya Varaqasi · 5–6-sinf · 5-hafta · 17-dars",
         "Практический Рабочий Лист · 5–6 класс · Неделя 5 · Урок 17",
         "Hands-On Lab Worksheet · Grades 5–6 · Week 5 · Lesson 17")
))

V.append(mission(
    h=("Laboratoriya Vazifasi: Parol Entropiyasi va Passphrase Qurish",
       "Миссия Лабораторной: Расчет Сложности и Создание Пароль-Фразы",
       "Lab Mission: Password Entropy Audit & Passphrase Architecture"),
    p=("Zaif parollarning kompyuterlar oldida qanchalik ojizligini tahlil qilish, "
       "va o'zaro bog'liq bo'lmagan 3 ta so'zdan iborat buzib bo'lmas Kiber-Passphrase yaratish.",
       "Проанализировать уязвимость коротких паролей перед компьютерным перебором "
       "и составить личную несокрушимую пароль-фразу из трёх независимых слов со спецсимволами.",
       "Audit the fragility of short dictionary passwords against brute-force automation "
       "and engineer an unbreakable 3-word Passphrase shielded with delimiters and numeric salts."))
)

V.append(table(
    headers=[
        ("Sinov Turi", "Тип Пароля", "Password Test"),
        ("Namuna Parol", "Тестовый Пример", "Sample Input"),
        ("Buzish Vaqti (Taxminiy)", "Расчетное Время Взлома", "Estimated Crack Time"),
        ("Xavfsizlik Xulosasi", "Вердикт", "Security Verdict")
    ],
    rows=[
        [("1. Faqat 6 raqam", "1. Только 6 цифр", "1. 6 Digits Only"),
         ("`123456` yoki `201405`", "`123456` или год рождения", "`123456` or birthdate"),
         ("0.001 sekund (Mavjud emas)", "0.001 секунды (Мгновенно)", "0.001s (Instant crack)"),
         ("🔴 Mutlaqo yaroqsiz", "🔴 Полностью уязвим", "🔴 Catastrophic")],
        [("2. Bitta oddiy so'z", "2. Одно слово", "2. Single Word"),
         ("`maktab2026`", "`shkola2026`", "`targetschool`"),
         ("2–3 sekund (Lug'at hujumi)", "2–3 секунды по словарю", "2–3s (Dictionary attack)"),
         ("🟡 Xavfli va zaif", "🟡 Опасно и ненадежно", "🟡 Highly vulnerable")],
        [("3. 3-So'zli Passphrase", "3. Супер-Пароль-Фраза", "3. 3-Word Passphrase"),
         ("`3 ta so'z + belgi + son`", "`3 слова + символы + цифры`", "`3 words + symbol + num`"),
         ("30,000+ YIL (Buzib bo'lmaydi)", "Более 30 000 ЛЕТ", "30,000+ YEARS (Safe)"),
         ("🟢 Mukammal Kiber-Qal'a", "🟢 Несокрушимая защита", "🟢 Ironclad Shield")]
    ]
))

V.append(sheet_box(
    h=("Mening Maxfiy Passphrase Formulani Yaratish", "Конструктор Моей Пароль-Фразы", "My Personal Passphrase Blueprint"),
    body_html=writelines(3, label=("1. O'zingiz yoqtirgan, lekin bir-biriga mutlaqo bog'liq bo'lmagan 3 ta qiziq so'zni yozing (Masalan: Kitob, Samolyot, Banan):",
                                   "1. Напишите три ярких случайных слова, не связанных друг с другом по смыслу:",
                                   "1. Write down 3 vivid, completely unrelated nouns (e.g. Book, Airplane, Banana):"))
             + "<br>"
             + writelines(2, label=("2. Ularning orasiga qanday belgilar (!, #, $) va oxiriga qanday son qo'shasiz? Namuna ko'rinishida yozing:",
                                   "2. Какие разделители (!, #, $) и цифры вы добавите между ними? Запишите формулу:",
                                   "2. What delimiters (!, #, $) and numbers will you interleave? Write your blueprint pattern:"))
))

V.append(sheet_box(
    h=("Baholash Mezoni (10 Ball)", "Критерии Оценки (10 Баллов)", "Grading Rubric (10 Points)"),
    body_html=rubric([
        (("Brute-force va lug'at hujumi mexanizmi to'g'ri tushuntirilgan", "Механика Brute-force и словарных атак понята верно", "Brute-force and dictionary attack mechanics comprehended"), "3 ball"),
        (("3-so'zli Passphrase formulasi to'liq va xatosiz tuzilgan", "Формула пароль-фразы из 3 слов составлена корректно", "3-word passphrase blueprint constructed flawlessly"), "3 ball"),
        (("Laboratoriya jadvalidagi parollar va vaqtlar to'g'ri taqqoslangan", "Таблица сравнительного анализа паролей заполнена", "Lab password crack times accurately evaluated"), "2 ball"),
        (("Oilaviy kiber-audit vazifasi va 2FA ahamiyati asoslab berilgan", "Понята важность 2FA и выполнен семейный аудит", "2FA importance justified and family audit documented"), "2 ball"),
    ], "10 ball")
))

V.append("</div>\n" + sign_box("Musulmonov Mamarajab"))

VARAQA_BODY = "\n".join(V)

lesson = Lesson(
    outdir=D,
    titles=TITLES,
    sheet_titles=SHEET_TITLES,
    key="vc-notes-5-17",
    slides=S,
    notes=NOTES,
    varaqa_body=VARAQA_BODY
)

if __name__ == "__main__":
    out = lesson.build()
    print("Created:", out)
