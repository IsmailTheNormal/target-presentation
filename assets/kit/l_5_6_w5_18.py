# -*- coding: utf-8 -*-
"""5-6-sinf · 5-hafta · 18-dars — Fishing Detektori: Soxta Havolalar, 'Bepul Robux' va Telegram Qopqonlari."""

import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from build import (Lesson, slide, title_slide, box, code, media_box, el, i18n,
                   sheet_header, mission, table, sheet_box, rubric, writelines, sign_box)

D = "classes/5-6-sinf/5-hafta/18-dars-fishing-va-soxta-havolalar"

TITLES = {
    "uz": "18-dars: Fishing Detektori — 'Bepul Robux' va Telegram Qopqonlari",
    "ru": "Урок 18: Детектор Фишинга — «Бесплатный Робукс» и Ловушки в Telegram",
    "en": "Lesson 18: Phishing Detective — 'Free Robux' & Telegram Traps",
}
SHEET_TITLES = {k: v + (" — Ish Varaqasi" if k == "uz" else
                        " — Рабочий Лист" if k == "ru" else " — Worksheet")
                for k, v in TITLES.items()}

S = []

# 1. Title Slide
S.append(title_slide(
    ph=("Kirish", "Введение", "Intro"), time="0–3",
    eyebrow=("CyberSecurity · 18-dars · 5–6-sinf (Kiber-Detektiv)",
             "CyberSecurity · Урок 18 · 5–6 класс (Кибер-Детектив)",
             "CyberSecurity · Lesson 18 · Grades 5–6 (Cyber-Detective)"),
    h1=("Fishing Detektori: Soxta Havolalar va Qopqonlar",
        "Детектор Фишинга: Ловушки, Ссылки и Обман в Сети",
        "Phishing Detective: Exposing Fake Links & Account Traps"),
    lede=("Nega dunyodagi eng zo'r xakerlar ham kompyuterlarni emas, balki <b>insonlarni aldashga</b> urinishadi? "
          "Chunki kompyuterning shifrini buzish uchun minglab yillar kerak, lekin odamga <i>'Sizga bepul 5000 Robux chiqdi!'</i> "
          "yoki <i>'Telegramingiz o'chirilmoqda, bu yerga bosing!'</i> deb xabar yuborilsa, ko'pchilik o'z qo'li bilan parolini berib qo'yadi! "
          "Ushbu kiber-aldov <b>Fishing (Baliq ovi)</b> deb ataladi. Bugungi darsda biz kiber-detektivlarga aylanib, "
          "soxta havolalarni (URL), aldovchi harflarni va Telegram tuzoqlarini 1 soniyada fosh qilishni o'rganamiz!",
          "Почему даже самые опытные хакеры мира атакуют не сложные серверы, а <b>человеческие эмоции</b>? "
          "Потому что взломать суперкомпьютер сложно, а отправить сообщение: <i>«Вам начислено 5000 гемов в Brawl Stars!»</i> "
          "или <i>«Ваш Telegram удаляется, подтвердите код!»</i> — просто. И многие сами отдают пароли! "
          "Этот метод называется <b>Фишингом (Рыбалкой на жертву)</b>. Сегодня мы станем кибер-детективами "
          "и научимся распознавать фальшивые сайты, буквы-двойники и ссылки-ловушки с первого взгляда!",
          "Why do elite cyber adversaries target <b>human psychology</b> rather than unbreakable encryption? "
          "Because brute-forcing a cipher demands millennia, but sending a message saying <i>'Free 5000 Robux credited!'</i> "
          "or <i>'Your Telegram account is scheduled for deletion!'</i> tricks users into voluntarily handing over keys! "
          "This deception is known as <b>Phishing</b>. Today we transform into certified Cyber-Detectives "
          "to expose fraudulent URLs, lookalike homoglyphs, and Telegram account traps in seconds!"),
    meta=[("<b>Fan:</b> Kiberxavfsizlik · Anti-Fishing Tahlili",
           "<b>Предмет:</b> Кибербезопасность · Защита от Фишинга",
           "<b>Subject:</b> CyberSecurity · Phishing Defense"),
          ("<b>Kohorta:</b> 5–6-sinf (10–12 yosh)",
           "<b>Когорта:</b> 5–6 класс (10–12 лет)",
           "<b>Cohort:</b> Grades 5–6 (Ages 10–12)"),
          ("<b>Hafta:</b> 5 (2-soat)", "<b>Неделя:</b> 5 (2-й час)", "<b>Week:</b> 5 (Hour 2)")],
))

# 2. What is Phishing: Ronaldo Meme
S.append(slide(
    ph=("Hujum Taktikasi", "Тактика Обмана", "The Hook"), time="3–7",
    eyebrow=("Qanday aldashadi?", "Анатомия крючка", "Social Engineering"),
    title=("Fishing Nima va Nega Xakerlar Uni Yaxshi Ko'radi?",
           "Что Такое Фишинг и Почему Он Работает?",
           "What is Phishing & Why is it the #1 Cyber Trap?"),
    body='<div class="cols">\n'
         + box("red", ("Fishing (Baliq Ovi) Qanday Ishlaydi? 🎣", "Механика Фишинга: Заброс Крючка 🎣", "Phishing Mechanics: The Lure 🎣"),
               items=[
                   ("<b>1. O'lja (Bait):</b> Sizga juda yoqadigan narsa taklif qilinadi: 'Bepul Telegram Premium', 'Brawl Stars skin', 'Olimpiada sovg'asi'.",
                    "<b>1. Наживка:</b> Яркое заманчивое предложение: бесплатный премиум, гемы для игр или выигрыш в лотерее.",
                    "<b>1. The Lure:</b> Irresistible promises: free game currency, Telegram Premium, or tournament prizes."),
                   ("<b>2. Soxta Sahifa:</b> Havolani bossangiz, aynan Telegram yoki Robloxga 100% o'xshash, ammo qalbaki sayt ochiladi.",
                    "<b>2. Копия сайта:</b> Ссылка ведет на идеальную визуальную копию входа в Roblox, Google или Telegram.",
                    "<b>2. The Cloned Portal:</b> A deceptive clone replicating Roblox, Google, or Telegram design down to the pixel."),
                   ("<b>3. Qopqon:</b> Siz login va SMS parolingizni yozganingiz zahoti, u to'g'ridan-to'g'ri hackerning telegram botiga jo'natiladi!",
                    "<b>3. Кража:</b> Как только вы ввели номер и код из SMS — они мгновенно падают в руки хакера!",
                    "<b>3. The Theft:</b> Submitting your phone and SMS token transmits them directly into an adversary's bot!")
               ])
         + media_box("rolando-ronaldo.mp4")
         + '</div>'
))

# 3. Lookalike URLs & Domain Sleuthing
S.append(slide(
    ph=("Detektiv Tahlili", "Анализ Адреса", "URL Sleuthing"), time="7–11",
    eyebrow=("Ko'z ilg'amas farqlar", "Буквы-шпионы", "Lookalike Domains"),
    title=("Haqiqiy Sayt vs Qalbaki Nusxa: Havolani O'qish San'ati",
           "Оригинал или Подделка? Как Читать Адресную Строку",
           "Real Site vs Clone: The Art of Inspecting Domains"),
    body=table(
        headers=[("Xizmat Nomi", "Сервис", "Target Service"),
                 ("Haqiqiy Manzil (Xavfsiz ✅)", "Настоящий Адрес ✅", "Legitimate URL ✅"),
                 ("Qalbaki Fishing Manzil (Xavfli ❌)", "Поддельный Фишинг-Адрес ❌", "Deceptive Phishing URL ❌"),
                 ("Hackerning Hiylasi", "В чем подвох?", "Adversary Trick")],
        rows=[
            [("<b>Telegram</b>", "<b>Telegram</b>", "<b>Telegram</b>"),
             ("<code>https://telegram.org</code>", "<code>https://telegram.org</code>", "<code>https://telegram.org</code>"),
             ("<code>te1egram-login.xyz</code>", "<code>te1egram-login.xyz</code>", "<code>te1egram-login.xyz</code>"),
             ("'l' harfi o'rniga '1' (bir) raqami qo'yilgan!",
              "Буква «l» заменена на цифру «1»!",
              "Letter 'l' swapped with digit '1'!")],
            [("<b>Roblox</b>", "<b>Roblox</b>", "<b>Roblox</b>"),
             ("<code>https://www.roblox.com</code>", "<code>https://www.roblox.com</code>", "<code>https://www.roblox.com</code>"),
             ("<code>robl0x-free-gift.ru</code>", "<code>robl0x-free-gift.ru</code>", "<code>robl0x-free-gift.ru</code>"),
             ("'o' harfi o'rniga '0' (nol) yozilgan!",
              "Буква «o» заменена на ноль «0»!",
              "Letter 'o' replaced with zero '0'!")],
            [("<b>Instagram</b>", "<b>Instagram</b>", "<b>Instagram</b>"),
             ("<code>https://instagram.com</code>", "<code>https://instagram.com</code>", "<code>https://instagram.com</code>"),
             ("<code>instagrarn.com/verify</code>", "<code>instagrarn.com/verify</code>", "<code>instagrarn.com/verify</code>"),
             ("'m' harfi o'rniga 'r' va 'n' (rn) birlashtirilgan!",
              "Буквы «r» и «n» вместе выглядят точь-в-точь как «m»!",
              "Letters 'r' and 'n' joined mimic an 'm'!")],
            [("<b>Target School</b>", "<b>Target School</b>", "<b>Target School</b>"),
             ("<code>targetschool.uz</code>", "<code>targetschool.uz</code>", "<code>targetschool.uz</code>"),
             ("<code>target-school-quiz.site</code>", "<code>target-school-quiz.site</code>", "<code>target-school-quiz.site</code>"),
             ("Soxta domenga maktab nomini qo'shib olgan!",
              "Фальшивый сторонний домен с именем школы!",
              "Untrusted external TLD mimicking school brand!")]
        ]
    )
))

# 4. Psychological Triggers: Urgency & Panic
S.append(slide(
    ph=("Psixologiya", "Психология", "Psychology"), time="11–15",
    eyebrow=("Boshni aylantirish", "Психологическое давление", "Panic Induction"),
    title=("Nega Odamlar Aldanadi? Shoshiltirish Qopqoni!",
           "Почему Люди Верят? Ловушка Срочности и Паники!",
           "Why Do People Fall For It? The Urgency & Panic Trap"),
    body='<div class="cols">\n'
         + box("navy", ("Xakerlar Ishlatadigan 3 Ta Psixologik Nayrang", "3 Главных Трюка Социальной Инженерии", "Top 3 Psychological Exploits"),
               items=[
                   ("1. <b>Qo'rquv va Shoshiltirish:</b> <i>'Akkauntingiz 15 daqiqada bloklanadi! Qutqarish uchun havola ustiga bosing!'</i>",
                    "1. <b>Страх и цейтнот:</b> «Ваш аккаунт удалится через 10 минут! Срочно перейдите по ссылке!»",
                    "1. <b>Fear & Urgency:</b> <i>'Your profile will be terminated in 15 minutes! Click immediately to appeal!'</i>"),
                   ("2. <b>Ochko'zlik (Kutilmagan sovg'a):</b> <i>'Tabriklaymiz! Siz 1,000,000 so'mlik vaucher yoki 10,000 Robux yutib oldingiz!'</i>",
                    "2. <b>Жадность:</b> «Поздравляем! Вы выиграли новенький iPhone или 10 000 кристаллов в игре!»",
                    "2. <b>Greed:</b> <i>'Congratulations! You won a brand-new iPhone or 10,000 game gems!'</i>"),
                   ("3. <b>Do'st nomidan murojaat:</b> Buzilgan do'stingiz nomidan: <i>'Menga ovoz ber, 5000 so'm yutasan'</i> deb yozishadi.",
                    "3. <b>Просьба от друга:</b> «Привет, проголосуй за меня в конкурсе рисунков, очень нужно!»",
                    "3. <b>Compromised Friend:</b> <i>'Hey, please vote for me in this contest, it only takes one click!'</i>")
               ])
         + box("purple", ("Kiber-Detektiv Qoidasi: To'xta, Nafas Ol, Tekshir! 🛑", "Правило Кибер-Детектива: Стоп, Вдох, Проверка! 🛑", "The Detective Protocol: Stop, Breathe, Verify! 🛑"),
               items=[
                   ("Xakerning asosiy maqsadi — sizni <b>o'ylashga ulgurmasdan</b> tugmani bosishga majbur qilishdir.",
                    "Главная цель преступника — отключить ваш критический разум эмоцией страха или радости.",
                    "The adversary's entire tactic is disabling your critical thinking through panic or excitement."),
                   ("Agar sizni kimdir <i>'Tezroq!'</i> deb shoshiltirayotgan bo'lsa — bu <b>99% ehtimol bilan FISHING TUZOG'I!</b>",
                    "Если вас торопят таймером обратного отсчета — это почти со 100% вероятностью развод!",
                    "Whenever an unsolicited message imposes an urgent countdown timer — it is 99% a PHISHING TRAP!"),
                   ("To'xtang. Do'stingizga boshqa kanal orqali qo'ng'iroq qiling va so'rang: <i>'Sen chindan ham xabar yubordingmi?'</i>",
                    "Остановитесь. Позвоните другу по телефону и спросите, отправлял ли он ссылку на самом деле.",
                    "Halt. Voice-call your friend directly and ask: <i>'Did you actually send me that link?'</i>")
               ])
         + '</div>'
))

# 5. Bye I'm Out Meme: Screen Share & SMS Codes
S.append(slide(
    ph=("Oltin Qoida", "Золотое Правило", "SMS Codes"), time="15–18",
    eyebrow=("Hech kimga aytilmaydi!", "Никому и никогда", "Zero Disclosure"),
    title=("SMS Kodni So'rashyaptimi? 'Xayr, Men Ketdim!'",
           "Просят Назвать Код из SMS? «Пока, Я Ухожу!»",
           "Asking for Your SMS Login Code? 'Bye, I'm Out!'"),
    body='<div class="cols">\n'
         + box("red", ("Raqamli Dunyodagi Eng Qat'iy Qoida 🛑", "Главный Закон Цифровой Безопасности 🛑", "The Prime Directive of Authentication 🛑"),
               items=[
                   ("Telefonga keladigan 5 yoki 6 xonali kod — bu sizning <b>uydagi kalitingiz kabidir</b>.",
                    "Код из 5 цифр, приходящий в SMS или в Telegram — это ключ от двери в вашу цифровую квартиру.",
                    "A 5-digit verification code sent via SMS or Telegram is the physical key to your digital home."),
                   ("Hatto o'zini <i>'Telegram Ma'muriyati'</i> yoki <i>'Roblox Xavfsizlik Xizmati'</i> deb tanishtirsa ham — <b>hech qachon kodni bermang!</b>",
                    "Ни один реальный банк, администратор Telegram или поддержка игры НИКОГДА не спрашивают этот код!",
                    "No legitimate bank, Telegram admin, or game support will EVER ask for your login code!"),
                   ("Discord yoki Zoomda ekranni ulashganda (Screen Share) SMS xabarlaringiz ko'rinib qolmasligiga ehtiyot bo'ling!",
                    "Никогда не показывайте экран в Discord или Zoom, когда вам приходят секретные уведомления!",
                    "Never screen-share in Discord or Zoom while receiving authentication prompts on your desktop!")
               ])
         + media_box("bye-im-out.mp4")
         + '</div>'
))

# 6. The Padlock Myth: HTTPS Does Not Equal Safe!
S.append(slide(
    ph=("Xavfsizlik Afsonasi", "Миф о Замочке", "The Padlock Myth"), time="18–22",
    eyebrow=("Brauzer qulfi nimani bildiradi?", "Замочек в браузере", "The Browser Padlock"),
    title=("Brauzerdagi 'Qulfcha' (HTTPS) Sizni Firibgardan Asramaydi!",
           "Замочек в Браузере (HTTPS) Не Означает, Что Сайт Честный!",
           "The Browser Padlock (HTTPS) Does NOT Mean The Site is Safe!"),
    body='<div class="cols">\n'
         + box("blue", ("Qulfcha (HTTPS) Aslida Nimani Bildiradi?", "Что На Самом Деле Значит HTTPS?", "What HTTPS Actually Guarantees"),
               items=[
                   ("Ko'p bolalar o'ylaydi: <i>'Saytda yashil qulfcha bormi, demak u 100% xavfsiz va ishonchli!'</i> — BU KATTA XATO!",
                    "Многие ошибочно считают: «Раз в адресной строке горит замочек — сайт проверен и безопасен». Это ложь!",
                    "Common misunderstanding: <i>'If there is a padlock in the URL bar, the website is 100% trusted!'</i> — FALSE!"),
                   ("Qulfcha faqat bitta narsani bildiradi: siz bilan ushbu server o'rtasidagi ma'lumot <b>shifrlangan</b>.",
                    "Замочек означает лишь одно: трафик между вашим экраном и этим сервером зашифрован.",
                    "The padlock guarantees only one fact: network traffic between your browser and that server is encrypted."),
                   ("Ammo agar serverning egasi <b>hackerning o'zi bo'lsa</b>, siz o'z parolingizni hackerga shifrlangan chiroyli quvur orqali topshirgan bo'lasiz!",
                    "Но если сервер принадлежит мошеннику, вы просто отдадите свой пароль хакеру по зашифрованному каналу!",
                    "If the server belongs to an adversary, you simply hand your password to them over an encrypted tunnel!")
               ])
         + box("purple", ("Hackerlar Qanday Qilib Qulfcha Qo'yadi?", "Откуда у Хакеров Сертификаты?", "How Attackers Acquire SSL Certificates"),
               items=[
                   ("Bugungi kunda har qanday odam (hatto firibgar ham) bepul SSL sertifikat (masalan Let's Encrypt) olishi mumkin.",
                    "Сегодня бесплатный SSL-сертификат можно выпустить за 30 секунд на абсолютно любой поддельный сайт.",
                    "Today anyone (including adversaries) can register free SSL certificates on malicious domains in 30 seconds."),
                   ("Bugungi kunda fishing saytlarning <b>80% dan ortig'i qulfchaga ega!</b>",
                    "Более 80% фишинговых сайтов прямо сейчас имеют красивый замочек в строке браузера!",
                    "Over 80% of active phishing domains present a valid SSL padlock in the address bar!"),
                   ("<b>Xulosa:</b> Qulfchaga emas, <b>sayt nomining harflariga</b> qarang!",
                    "<b>Правило:</b> Смотрите не на замочек, а внимательно читайте каждую букву в доменном имени!",
                    "<b>Rule:</b> Do not rely on the padlock icon; inspect every single character of the domain name!")
               ])
         + '</div>'
))

# 7. Code Dissection: Python Fake URL Detector
S.append(slide(
    ph=("Kod Tahlili", "Анализ Кода", "Code Dissection"), time="22–26",
    eyebrow=("Dasturchi kabi o'ylash", "Код антифишинга", "Automated Detection"),
    title=("Python Skripti Soxta Havolalarni Qanday Fosh Qiladi?",
           "Как Простой Скрипт на Python Выявляет Ловушки?",
           "How a Simple Python Script Unmasks Malicious URLs"),
    body=code("""import urllib.parse

OFFICIAL_DOMAINS = ["telegram.org", "roblox.com", "targetschool.uz"]

def inspect_url(link: str) -> str:
    # 1. URL manzilidan asosiy domenni ajratib olamiz
    parsed = urllib.parse.urlparse(link)
    hostname = parsed.hostname or link
    
    # 2. Xavfli kalit so'zlar bor-yo'qligini tekshiramiz
    traps = ["free-robux", "bonus", "gift", "verify-account", "telegram-premium"]
    for trap in traps:
        if trap in link.lower() and hostname not in OFFICIAL_DOMAINS:
            return f"🚨 XAVF! Soxta tuzoq aniqlandi: '{trap}'"
            
    # 3. Rasmiy saytlar ro'yxatiga solishtiramiz
    if any(hostname.endswith(domain) for domain in OFFICIAL_DOMAINS):
        return "✅ XAVFSIZ: Rasmiy tasdiqlangan domen."
        
    return "⚠️ DIQQAT! Noma'lum notanish sayt, parolni kiritmang!"

# Test:
print(inspect_url("https://robl0x-free-robux.site/login"))
# Natija: 🚨 XAVF! Soxta tuzoq aniqlandi: 'free-robux'""")
))

# 8. The Weeknd Meme: Spotting the 'rn' Trap
S.append(slide(
    ph=("Kiber-G'alaba", "Кибер-Победа", "Victory"), time="26–30",
    eyebrow=("Hacker ustidan kulish", "Победа над хакером", "Spotting The Trap"),
    title=("Hacker Xatoni Kutayotganda, Siz Tuzoqni Fosh Qildingiz!",
           "Хакер Ждёт Вашего Пароля, а Вы Раскусили Подделку!",
           "Adversary Waiting For Your Password vs You Spotting The 'rn'"),
    body='<div class="cols">\n'
         + box("green", ("Kiber-Detektiv G'alabasi! 🏆", "Триумф Кибер-Детектива! 🏆", "The Cyber-Detective Triumph! 🏆"),
               items=[
                   ("Hacker soatlab harakat qilib, chiroyli soxta vebsayt yasadi va sizga jo'natdi.",
                    "Злоумышленник часами копировал верстку сайта, чтобы заманить вас в ловушку.",
                    "An adversary spent hours cloning site markup to set an elaborate credentials trap."),
                   ("U sizni <i>'Tezda kiring, sovg'a oling!'</i> deb aldadi.",
                    "Он надеялся, что жадность или спешка заставят вас ввести пароль не глядя.",
                    "They anticipated that urgency and greed would bypass your caution."),
                   ("Ammo siz URL manziliga qarab: <b>'instagrarn.com? Bu yerda m o'rniga r va n yozilgan-ku!'</b> dedingiz va havolani darhol blokladingiz!",
                    "Но вы спокойно посмотрели на адресную строку, заметили подвох в буквах и нажали «Пожаловаться на спам»!",
                    "Yet you calmly scrutinized the address bar, caught the homoglyph spoofing, and clicked 'Report Phishing'!"),
                   ("Hacker sarflagan vaqt va pulining hammasi bir soniyada ko'kka sovurildi!",
                    "Все усилия и затраты мошенника рассыпались в пыль за одну секунду благодаря вашей бдительности!",
                    "The attacker's entire campaign collapsed instantly in front of your digital vigilance!")
               ])
         + media_box("the-weeknd-weekend.mp4")
         + '</div>'
))

# 9. Telegram Safety: Blue Badges & Verification
S.append(slide(
    ph=("Telegram Xavfsizligi", "Защита Telegram", "Telegram Safety"), time="30–33",
    eyebrow=("O'g'irlanishdan himoya", "Безопасность мессенджера", "Messenger Defense"),
    title=("Telegram Akkauntingizni Qanday Qilib 100% Himoya Qilasiz?",
           "Как Защитить Свой Telegram от Угона на 100%?",
           "How to Shield Your Telegram Account Against Hijacking"),
    body='<div class="cols">\n'
         + box("blue", ("Telegram Rasmiy Xabarlarini Qanday Taniymiz?", "Как Распознать Официальный Telegram?", "Identifying Authentic Telegram Notices"),
               items=[
                   ("Telegram xizmati sizga hech qachon guruhlardan yoki begona botlardan xabar yozmaydi.",
                    "Служба Telegram никогда не пишет из обычных пользовательских аккаунтов или левых ботов.",
                    "Telegram Support never contacts you from standard user handles or unverified bots."),
                   ("Haqiqiy Telegram xabarlarida doimo <b>Moviy Tasdiqlash Belgisi (Verified Badge ✔️)</b> bo'ladi va ularga javob yozib bo'lmaydi.",
                    "Официальные уведомления приходят только в сервисный чат с синей галочкой верификации.",
                    "System messages arrive strictly through service dialogs carrying a verified blue checkmark badge."),
                   ("Telegram hech qachon <i>'Parolingizni botga yuboring'</i> deb so'ramaydi!",
                    "Telegram НИКОГДА не просит переслать код подтверждения другому боту или человеку!",
                    "Telegram NEVER directs users to paste verification codes into third-party bots!")
               ])
         + box("green", ("Zudlik Bilan Yoqilishi Shart Bo'lgan 2 Ta Sozlama", "2 Главные Настройки Прямо Сейчас", "2 Mandatory Settings to Enable Today"),
               items=[
                   ("1. <b>Bulutli Parol (Two-Step Verification):</b> Sozlamalar &rarr; Maxfiylik &rarr; Ikki bosqichli tekshiruv. Parolingizni o'rnating!",
                    "1. <b>Облачный пароль:</b> Настройки &rarr; Конфиденциальность &rarr; Двухэтапная аутентификация.",
                    "1. <b>Two-Step Verification:</b> Settings &rarr; Privacy & Security &rarr; Two-Step Verification. Set a strong passphrase!"),
                   ("2. <b>Faol Seanslar (Active Sessions):</b> Sozlamalar &rarr; Qurilmalar. Begona telefon yoki kompyuter ko'rinsa, darhol <b>'Barcha boshqa seanslarni tugatish'</b> tugmasini bosing!",
                    "2. <b>Устройства:</b> Настройки &rarr; Устройства. Если видите незнакомый телефон — жмите «Завершить все другие сеансы»!",
                    "2. <b>Active Devices:</b> Settings &rarr; Devices. If an unknown device appears, hit 'Terminate All Other Sessions'!")
               ])
         + '</div>'
))

# 10. Hands-on Lab: 4 Forensic Casefiles
S.append(slide(
    ph=("Amaliyot", "Практика", "Hands-on Lab"), time="33–38",
    eyebrow=("Laboratoriya tergovi", "Лабораторное расследование", "Detective Workshop"),
    title=("Amaliy Ish: Kiber-Ekspertiza — 4 Ta Gumonlanuvchi Xabar",
           "Практика: Экспертиза — 4 Подозрительных Сообщения",
           "Hands-on Lab: Forensic Analysis — 4 Suspicious Casefiles"),
    body='<div class="box blue">\n'
         + el("h3", "Laboratoriya Vazifasi (10 Daqiqa)", "Задание Лабораторной (10 Минут)", "Detective Challenge (10 Minutes)")
         + el("p", "Quyidagi 4 ta xabarni tekshiring. Ularning qaysi biri haqiqiy va qaysi biri fishing tuzog'i ekanligini aniqlang, xato joylarini daftaringizga qayd eting!",
              "Изучите 4 реальных сценария сообщений. Определите, где фальшивка, а где легитимное уведомление, и выпишите улики в рабочий лист!",
              "Evaluate 4 simulated incoming notifications. Identify frauds versus authentic notices and log the forensic evidence on your worksheet!")
         + '</div>\n'
         + table(
             headers=[("Keys #", "Кейс", "Case"),
                      ("Kelgan Xabar Matni va Havolasi", "Текст и Ссылка", "Notification Payload"),
                      ("Kiber-Hukm (Soxta / Qonuniy)", "Вердикт (Обман / Норма)", "Verdict"),
                      ("Fosh Etuvchi Dalil (Nega?)", "Главная Улика", "Forensic Evidence")],
             rows=[
                 [("<b>Keys A</b>", "<b>Кейс A</b>", "<b>Case A</b>"),
                  ("<i>'Tabriklaymiz! 5000 Robux yutib oldingiz: https://robl0x-gift.ru'</i>", "«Вам начислено 5000 Robux: robl0x-gift.ru»", "'Free 5000 Robux: https://robl0x-gift.ru'"),
                  ("❌ SOXTA FISHING", "❌ ФИШИНГ", "❌ PHISHING TRAP"),
                  ("robl0x (nol bilan yozilgan) + tekin narsa yo'q", "Ноль вместо «o» и подозрительный домен", "Zero instead of 'o' + free bait")],
                 [("<b>Keys B</b>", "<b>Кейс B</b>", "<b>Case B</b>"),
                  ("<i>'Telegram akkauntingiz o'chirilmoqda. Kodni bu botga yuboring: @VerifyBot'</i>", "«Аккаунт удаляется, перешлите код боту»", "'Account deletion imminent. Send code to bot'"),
                  ("❌ XAVFLI TUZOQ", "❌ ЛОВУШКА", "❌ MALICIOUS TRAP"),
                  ("Telegram hech qachon bot orqali kod so'ramaydi", "Telegram никогда не просит коды через ботов", "Telegram never demands codes via bot")],
                 [("<b>Keys C</b>", "<b>Кейс C</b>", "<b>Case C</b>"),
                  ("<i>'Target School dars jadvali yangilandi: https://targetschool.uz'</i>", "«Расписание Target School: targetschool.uz»", "'Target School schedule update: targetschool.uz'"),
                  ("✅ QONUNIY VA XAVFSIZ", "✅ БЕЗОПАСНО", "✅ LEGITIMATE"),
                  ("Rasmiy maktab domeni, hech qanday parol so'ramaydi", "Официальный сайт школы, нет запросов пароля", "Authentic school domain, zero credential request")],
                 [("<b>Keys D</b>", "<b>Кейс D</b>", "<b>Case D</b>"),
                  ("<i>'Do'stingiz: Menga rasm tanlovida ovoz ber: https://t.me-contest.site'</i>", "«Друг: Проголосуй за меня: t.me-contest.site»", "'Friend: Vote for me in contest: t.me-contest.site'"),
                  ("❌ SOXTA SAYT", "❌ ПОДДЕЛКА", "❌ PHISHING CLONE"),
                  ("Domen telegram emas, balki t.me-contest.site!", "Домен мошеннический, взломан аккаунт друга", "Third-party spoofed contest domain")]
             ]
         )
))

# 11. The Junior Detective 5 Shields
S.append(slide(
    ph=("Qoidalar", "Кодекс", "The Code"), time="38–40",
    eyebrow=("Kiber-Detektiv kodeksi", "Кодекс безопасности", "The Detective Code"),
    title=("Kiber-Detektivning 5 Ta Buzilmas Qoidasi",
           "5 Заповедей Юного Кибер-Детектива",
           "The 5 Unbreakable Laws of the Junior Cyber-Detective"),
    body='<div class="cols">\n'
         + box("green", ("Har Kuni Amal Qilinadigan Qoidalar 🛡️", "Ежедневные Правила Цифровой Жизни 🛡️", "Daily Cyber-Hygiene Principles 🛡️"),
               items=[
                   ("1. <b>Harflarni tekshiring:</b> Havolani bosishdan oldin har bir harfiga diqqat bilan qarang (<code>o</code> vs <code>0</code>, <code>l</code> vs <code>1</code>).",
                    "1. <b>Проверяйте буквы:</b> Всегда внимательно читайте адрес сайта до клика (l или 1, o или 0).",
                    "1. <b>Audit characters:</b> Scrutinize every letter in URLs prior to clicking (o vs 0, l vs 1)."),
                   ("2. <b>Tekin pishloq faqat qopqonda bo'ladi:</b> Hech kim internetda tekinga Robux, iPhone yoki pul tarqatmaydi!",
                    "2. <b>Бесплатный сыр только в мышеловке:</b> Никто в сети не дарит просто так премиумы и кристаллы!",
                    "2. <b>No free lunch:</b> Nobody gives away free Robux, Steam skins, or iPhones on the open internet!"),
                   ("3. <b>SMS kodni hech kimga bermang:</b> Kod — sizning uy kalitingiz.",
                    "3. <b>Код из SMS — тайна:</b> Никому, никогда, ни под каким предлогом не сообщайте цифры из сообщений!",
                    "3. <b>Guarded SMS tokens:</b> Verification codes are strictly non-disclosable credentials."),
                   ("4. <b>2FA ni yoqing:</b> Telegram va o'yinlaringizda ikki bosqichli himoyani o'rnating.",
                    "4. <b>Включите двухфакторку:</b> Двухэтапная аутентификация в Telegram спасает в 99.9% случаев.",
                    "4. <b>Enforce 2FA:</b> Cloud Passwords block account hijacking even if credentials leak."),
                   ("5. <b>Shubha qilsangiz — kattalardan so'rang:</b> O'qituvchingiz yoki ota-onangizga ko'rsatishdan uyalmang!",
                    "5. <b>Сомневаешься — спроси:</b> Покажите подозрительную ссылку учителю или родителям.",
                    "5. <b>When in doubt — consult:</b> Never hesitate to verify suspicious links with teachers or parents!")
               ])
         + '</div>'
))

# 12. Summary & Homework: Anti-Phishing Poster
S.append(slide(
    ph=("Xulosa", "Итоги", "Summary"), time="40–43",
    eyebrow=("Uy vazifasi", "Домашнее задание", "Homework Challenge"),
    title=("Xulosa va Uy Vazifasi: Anti-Fishing Eslatmasi (10 Ball)",
           "Итоги и Задание: Памятка «Осторожно, Фишинг!» (10 Баллов)",
           "Summary & Homework: Junior Anti-Phishing Advisory (10 Pts)"),
    body='<div class="cols">\n'
         + box("blue", ("Bugungi Muhim Saboqlar", "Главные Уроки Дня", "Key Takeaways"),
               items=[
                   ("Fishing — bu kompyuterni emas, inson his-tuyg'ularini (qo'rquv, qiziqish, shoshqaloqlik) aldashdir.",
                    "Фишинг взламывает не устройства, а эмоции человека: любопытство, жадность и страх.",
                    "Phishing exploits human cognitive vulnerabilities rather than computational algorithms."),
                   ("Qulfcha (HTTPS) saytning xavfsizligini kafolatlamaydi — u faqat shifrlashni bildiradi.",
                    "Замочек HTTPS не гарантирует честность сайта: у большинства фишинговых сайтов он есть!",
                    "The HTTPS padlock only certifies channel encryption, not domain trustworthiness."),
                   ("Bitta hushyor nigoh har qanday xakerning oylik mehnatini bir zumda yo'qqa chiqaradi!",
                    "Одна секунда проверки адресной строки спасает ваш аккаунт от полного уничтожения.",
                    "One second of disciplined domain inspection neutralizes entire adversary campaigns!")
               ])
         + box("purple", ("Uy Vazifasi: Do'stlar Uchun Kiber-Ogohlantirish (10 Ball)", "Домашнее Задание: Памятка для Друзей (10 Баллов)", "Homework: Peer Phishing Advisory (10 Pts)"),
               items=[
                   ("1. O'z sinfdoshlaringiz yoki do'stlaringiz uchun daftaringizga <b>'Fishing Qopqoniga Tushmaslik Uchun 3 Maslahat'</b> mini-eslatmasini chizing va yozing.",
                    "1. Нарисуйте и составьте в тетради яркую памятку «3 совета, как не потерять Telegram и игры из-за фишинга».",
                    "1. Draft and illustrate a mini-advisory: '3 Golden Rules to Never Lose Your Telegram or Game Accounts'."),
                   ("2. Unda kamida 1 ta soxta havola misolini (masalan <code>robl0x</code>) ko'rsating va nima uchun xavfli ekanini tushuntiring.",
                    "2. Приведите в ней один пример фальшивого адреса и объясните, как распознать ловушку.",
                    "2. Include at least 1 homoglyph spoof example and explain how to spot the trap."),
                   ("3. Ish varaqasidagi 4 ta keys tahlilini to'liq yakunlab, o'qituvchiga topshiring.",
                    "3. Заполните протокол расследования 4 кейсов в рабочем листе и сдайте учителю.",
                    "3. Complete the 4 forensic case studies on your worksheet and submit for evaluation.")
               ])
         + '</div>'
))

# Teacher Notes
N_UZ = [
    ["Kirish", "O'quvchilarga kimga hech 'Telegram Premium yutib oldingiz' degan xabar kelganini so'rang. Mavzuga qiziqish uyg'oting.", "Slaydni oching."],
    ["Ronaldo", "Ronaldo shubha bilan qarayotgan memeni ko'rsating: begona botlar bepul narsa taklif qilganda aynan shunday qarash kerakligini ayting.", "Memeni ko'rsating."],
    ["URL tahlili", "Doskaga 'roblox.com' va 'robl0x-gift.ru' ni yozing. Bolalarga farqni topdiring, ko'zlarini o'rgating.", "Jadvalni ko'rsating."],
    ["Psixologiya", "Xakerlar nega shoshiltirishini (15 daqiqada bloklanadi!) tushuntiring: odam shoshganda o'ylamaydi.", "Nayranglarni tushuntiring."],
    ["Bye I'm out", "Bye I'm out memesi: agar kimdir SMS kodni so'rasa, hatto do'stingiz bo'lsa ham darhol suhbatni to'xtatish kerakligini ayting.", "Memeni ko'rsating."],
    ["Qulfcha", "Qulfcha afsonasini yo'qoting: qulfcha faqat shifrlash, hackerlar ham o'z saytiga osonlikcha qulfcha qo'ya olishini tushuntiring.", "Qulfchani tushuntiring."],
    ["Kod", "Python kodida qanday qilib 'free-robux' va rasmiy domenlar tekshirilishini bolalarga oddiy tushuntirib bering.", "Kodni oching."],
    ["The Weeknd", "The Weeknd kulayotgan g'alaba memesi: hacker aldashga urinib, o'zi sharmanda bo'lgan vaziyatni ko'rsating.", "Memeni ko'rsating."],
    ["Telegram", "Telegramdagi Moviy belgi (Verified) va Bulutli parol (2FA) sozlamalarini ekranda amalda ko'rsating.", "Sozlamalarni ko'rsating."],
    ["Amaliyot", "O'quvchilar 4 ta keysni tahlil qilishsin, qaysi biri haqiqiy va qaysi biri tuzoq ekanini belgilashsin.", "10 daqiqa taymerni yoqing."],
    ["Qoidalar", "Kiber-detektivning 5 ta qoidasini bolalar bilan birgalikda baland ovozda o'qing.", "Qoidalarni xulosa qiling."],
    ["Xulosa", "Uy vazifasini va 10 ballik mezonni e'lon qiling, bolalarni kiber-hushyorlikka chaqiring.", "Varaqalarni yig'ing."]
]

N_RU = [
    ["Введение", "Спросите у ребят, кому в Telegram хоть раз писали о выигрыше или просили проголосовать. Вовлеките аудиторию.", "Откройте титульный слайд."],
    ["Роналду", "Покажите мем с подозрительным Роналду: объясните, что именно такое лицо должно быть при получении странных ссылок.", "Покажите видео-мем."],
    ["Анализ URL", "Напишите на доске пары ссылок с подменой букв (l/1, o/0). Научите ребят внимательно читать домен второго уровня.", "Разберите таблицу."],
    ["Психология", "Разберите трюк со срочностью (таймер обратного отсчета): паника выключает логику и внимание.", "Объясните манипуляции."],
    ["Пока, я ухожу", "Мем «Bye I'm out»: жесткое правило — любой запрос SMS-кода означает немедленный разрыв диалога.", "Покажите видео-мем."],
    ["Миф о замочке", "Развейте опасный миф об HTTPS: замочек не проверяет честность, у мошенников тоже есть SSL-сертификаты.", "Поясните замочек."],
    ["Код", "Покажите простую логику Python: поиск стоп-слов вроде free-robux и сверка с белым списком доменов.", "Разберите скрипт."],
    ["The Weeknd", "Мем с триумфом The Weeknd: радость внимательного пользователя, раскусившего уловку «instagrarn».", "Покажите мем."],
    ["Telegram", "Наглядно покажите синюю галочку верификации в Telegram и объясните, как завершить чужие сеансы в устройствах.", "Разберите настройки."],
    ["Практикум", "Курируйте детективное расследование 4 кейсов в рабочем листе: выявление улик и вынесение вердикта.", "Запустите таймер 10 минут."],
    ["Кодекс", "Хором прочитайте 5 правил кибер-детектива: внимание к буквам, секретность кодов и двухфакторка.", "Обобщите кодекс."],
    ["Итоги", "Огласите домашнее задание на 10 баллов (памятка для друзей) и ответьте на вопросы учащихся.", "Соберите рабочие листы."]
]

N_EN = [
    ["Intro", "Survey the class on who has received suspicious Telegram giveaway messages. Hook interest with active social dilemmas.", "Open title slide."],
    ["Ronaldo", "Play the suspicious Ronaldo meme: model the exact skeptical mindset required when receiving unsolicited links.", "Play video meme."],
    ["URL Sleuthing", "Diagram lookalike domains on whiteboard (swapping l with 1, o with 0). Train student eyes to inspect hostnames.", "Review domain table."],
    ["Psychology", "Unpack urgency countdown timers: how artificial panic suppresses critical cognitive evaluation.", "Explain psychological hooks."],
    ["Bye I'm out", "Play 'Bye I'm out' meme: reinforce zero tolerance whenever any third party requests incoming SMS verification codes.", "Play video meme."],
    ["Padlock Myth", "Debunk the HTTPS padlock fallacy: certificates only encrypt transport; adversaries deploy SSL on 80%+ of phishing sites.", "Demystify padlock."],
    ["Code", "Walk through basic Python domain parsing logic checking allowlists against keyword traps.", "Walk through Python logic."],
    ["The Weeknd", "Play The Weeknd victory meme: celebrate the satisfaction of spotting homoglyphs ('rn' disguised as 'm').", "Play video meme."],
    ["Telegram", "Demonstrate genuine Telegram verified checkmarks and guide students to terminate rogue active sessions in settings.", "Review Telegram defense."],
    ["Lab", "Guide students through analyzing the 4 forensic casefiles on their worksheets, identifying evidence and verdicts.", "Start 10-minute lab timer."],
    ["The Code", "Recite the 5 laws of the Junior Cyber-Detective in unison: letter inspection, zero code disclosure, active 2FA.", "Review detective code."],
    ["Summary", "Assign the 10-point peer advisory poster homework and address student inquiries.", "Collect worksheets."]
]

NOTES = {"uz": N_UZ, "ru": N_RU, "en": N_EN}

# --- Worksheet (Varaqa) ---
V = []
V.append(sheet_header(
    h1=("Kiberxavfsizlik: Fishing Detektori va Soxta Havolalar",
        "Кибербезопасность: Детектор Фишинга и Ссылки-Ловушки",
        "CyberSecurity: Phishing Detective & Link Traps"),
    sub=("Amaliy Laboratoriya Varaqasi · 5–6-sinf · 5-hafta · 18-dars",
         "Практический Рабочий Лист · 5–6 класс · Неделя 5 · Урок 18",
         "Hands-On Lab Worksheet · Grades 5–6 · Week 5 · Lesson 18")
))

V.append(mission(
    h=("Laboratoriya Tergovi: 4 Ta Shubhali Xabarni Fosh Qilish",
       "Миссия Лабораторной: Экспертиза 4 Подозрительных Сообщений",
       "Lab Mission: Forensic Inspection of 4 Suspicious Inbound Payloads"),
    p=("Fishing tuzoqlarining psixologik va texnik usullarini o'rganish, "
       "soxta domen nomlaridagi xatolarni topish va xavfsiz qonuniy xabarlarni firibgarlikdan ajratish.",
       "Изучить методы социальной инженерии и технические уловки фишинга, "
       "найти подделки в адресных строках и научиться отличать безопасные уведомления от опасных ловушек.",
       "Investigate social engineering psychological triggers and technical URL spoofs, "
       "identify homoglyphs within suspicious hostnames, and cleanly segregate authentic notifications from attacks."))
)

V.append(table(
    headers=[
        ("Keys #", "Кейс", "Case"),
        ("Xabar / Havola", "Текст и Адрес", "Payload / Link"),
        ("Kiber-Hukm (Soxta / Xavfsiz)", "Вердикт", "Verdict"),
        ("Asosiy Dalil (Nega?)", "Улика / Обоснование", "Forensic Rationale")
    ],
    rows=[
        [("Keys 1", "Кейс 1", "Case 1"),
         ("`'Tekin 5000 Robux: robl0x-gift.ru'`", "«5000 Robux: robl0x-gift.ru»", "'Free Robux: robl0x-gift.ru'"),
         ("❌ Fishing Tuzog'i", "❌ Фишинг", "❌ Phishing Trap"),
         ("Nol '0' bilan yozilgan, tekin narsa yo'q", "Ноль вместо «o», наживка", "Zero homoglyph + fake bait")],
        [("Keys 2", "Кейс 2", "Case 2"),
         ("`'Telegram o'chirilmoqda, kodni bering'`", "«Аккаунт удаляется, дайте код»", "'Account deleting, send code'"),
         ("❌ Xavfli O'g'rilik", "❌ Опасный обман", "❌ Malicious Theft"),
         ("Telegram hech qachon kod so'ramaydi", "Telegram не просит коды", "Telegram never demands codes")],
        [("Keys 3", "Кейс 3", "Case 3"),
         ("`'Dars jadvali: targetschool.uz'`", "«Расписание: targetschool.uz»", "'Schedule: targetschool.uz'"),
         ("✅ Xavfsiz Qonuniy", "✅ Безопасно", "✅ Legitimate"),
         ("Rasmiy maktab sayti, parol so'ramaydi", "Официальный сайт школы", "Official domain, zero password ask")],
        [("Keys 4", "Кейс 4", "Case 4"),
         ("`'Do'stingiz: t.me-contest.site'`", "«Друг: t.me-contest.site»", "'Friend: t.me-contest.site'"),
         ("❌ Soxta Qopqon", "❌ Ловушка", "❌ Fraudulent Clone"),
         ("Domen Telegram emas, sayt begona", "Домен не t.me, взлом друга", "Not authentic t.me domain")]
    ]
))

V.append(sheet_box(
    h=("Kiber-Detektiv Ekspert Xulosasi", "Экспертное Заключение Детектива", "Forensic Investigation Findings"),
    body_html=writelines(3, label=("1. Nega brauzerdagi 'Qulfcha' (HTTPS) saytning firibgar emasligini 100% kafolatlay olmaydi?",
                                   "1. Почему наличие «замочка» HTTPS в браузере не гарантирует честность сайта?",
                                   "1. Why does an active browser HTTPS padlock fail to guarantee website legitimacy?"))
             + "<br>"
             + writelines(2, label=("2. Agar do'stingiz nomidan shubhali havola kelsa, uni bosishdan oldin nima qilishingiz kerak?",
                                   "2. Что нужно сделать перед тем, как кликать по ссылке, пришедшей якобы от друга?",
                                   "2. What mandatory action must you take before clicking a suspicious link sent under a friend's name?"))
))

V.append(sheet_box(
    h=("Baholash Mezoni (10 Ball)", "Критерии Оценки (10 Баллов)", "Grading Rubric (10 Points)"),
    body_html=rubric([
        (("Fishing va ijtimoiy muhandislik mexanizmlari to'g'ri tushuntirilgan", "Механика фишинга и манипуляций объяснена верно", "Phishing and social engineering tactics accurately explained"), "3 ball"),
        (("4 ta keysdagi soxta havolalar va dalillar to'liq aniqlangan", "Все 4 кейса расследованы, улики зафиксированы", "All 4 cases investigated and forensic clues properly logged"), "3 ball"),
        (("HTTPS qulfchasi va SMS kodlarni himoyalash qoidalari asoslangan", "Развенчан миф о замочке HTTPS и обоснована тайна SMS-кодов", "HTTPS padlock myth clarified and SMS code secrecy justified"), "2 ball"),
        (("Do'stlar uchun anti-fishing mini-eslatmasi mazmunli tayyorlangan", "Подготовлена памятка безопасности для друзей", "Peer anti-phishing advisory prepared with actionable insights"), "2 ball"),
    ], "10 ball")
))

V.append("</div>\n" + sign_box("Musulmonov Mamarajab"))

VARAQA_BODY = "\n".join(V)

lesson = Lesson(
    outdir=D,
    titles=TITLES,
    sheet_titles=SHEET_TITLES,
    key="vc-notes-5-18",
    slides=S,
    notes=NOTES,
    varaqa_body=VARAQA_BODY
)

if __name__ == "__main__":
    out = lesson.build()
    print("Created:", out)
