# -*- coding: utf-8 -*-
"""5-6-sinf · 5-hafta · 19-dars — Zararli Dasturlar va Troyanlar: 'Troyalik Ot' va Tekin Modlar Qopqoni."""

import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from build import (Lesson, slide, title_slide, box, code, media_box, el, i18n,
                   sheet_header, mission, table, sheet_box, rubric, writelines, sign_box)

D = "classes/5-6-sinf/5-hafta/19-dars-zararli-dasturlar-va-troyanlar"

TITLES = {
    "uz": "19-dars: Zararli Dasturlar va Troyanlar — 'Troyalik Ot' va Tekin Modlar Qopqoni",
    "ru": "Урок 19: Вредоносные Программы и Трояны — «Троянский Конь» и Ловушка Бесплатных Модов",
    "en": "Lesson 19: Malware & Trojans — The Trojan Horse & Fake Mod Trap",
}
SHEET_TITLES = {k: v + (" — Ish Varaqasi" if k == "uz" else
                        " — Рабочий Лист" if k == "ru" else " — Worksheet")
                for k, v in TITLES.items()}

S = []

# 1. Title Slide
S.append(title_slide(
    ph=("Kirish", "Введение", "Intro"), time="0–3",
    eyebrow=("CyberSecurity · 19-dars · 5–6-sinf (Kiber-Qalqon)",
             "CyberSecurity · Урок 19 · 5–6 класс (Кибер-Щит)",
             "CyberSecurity · Lesson 19 · Grades 5–6 (Cyber-Shield)"),
    h1=("Zararli Dasturlar va Troyanlar: 'Troyalik Ot' Qopqoni",
        "Вредоносные Программы и Трояны: Ловушка «Троянского Коня»",
        "Malware & Trojans: Exposing the Trojan Horse Trap"),
    lede=("Har kuni millionlab o'yinchilar internetdan <i>'Minecraft tekin shader'</i>, <i>'Roblox script'</i>, <i>'Brawl Stars mod'</i> yuklab olishadi. "
          "Ammo nega ularning yarmidan ko'pi o'g'irlangan Telegram akkauntlar yoki buzilgan kompyuter bilan tugaydi? "
          "Chunki kiber-jinoyatchilar eng ayyorona usuldan foydalanishadi — <b>Troyalik Ot (Trojan Horse)</b>! "
          "Bugun biz zararli dasturlar (Malware) turlarini, soxta kengaytmalar (.exe, .scr) tuzog'ini va "
          "kompyuterni himoya qiluvchi <b>VirusTotal hamda Sandbox</b> detektiv laboratoriyasini o'rganamiz!",
          "Каждый день миллионы геймеров скачивают <i>«бесплатные шейдеры Minecraft»</i>, <i>«читы для Roblox»</i> или <i>«моды Brawl Stars»</i>. "
          "Но почему половина таких загрузок заканчивается взломом Telegram, кражей паролей или вымогательством? "
          "Потому что киберпреступники применяют древнейшую военную хитрость — <b>Троянского Коня (Trojan Horse)</b>! "
          "Сегодня мы разберём семейства вредоносных программ (Malware), раскроем коварство двойных расширений (.exe, .scr) "
          "и научимся проверять файлы в цифровой лаборатории <b>VirusTotal и Sandbox</b>!",
          "Every day, millions of gamers download <i>'free Minecraft shaders'</i>, <i>'Roblox executors'</i>, or <i>'Brawl Stars gem mods'</i>. "
          "Yet why do so many downloads trigger account hijackings, password theft, or locked files? "
          "Because threat actors deploy history's most cunning trick — the <b>Trojan Horse</b>! "
          "Today, we dissect Malware families, expose double-extension traps (.exe, .scr), and master "
          "forensic threat inspection using <b>VirusTotal & dynamic Sandbox</b> environments!"),
    meta=[("<b>Fan:</b> Kiberxavfsizlik · Zararli Dasturlar Tahlili",
           "<b>Предмет:</b> Кибербезопасность · Анализ Вредоносного ПО",
           "<b>Subject:</b> CyberSecurity · Malware Analysis"),
          ("<b>Kohorta:</b> 5–6-sinf (10–12 yosh)",
           "<b>Когорта:</b> 5–6 класс (10–12 лет)",
           "<b>Cohort:</b> Grades 5–6 (Ages 10–12)"),
          ("<b>Hafta:</b> 5 (3-soat)", "<b>Неделя:</b> 5 (3-й час)", "<b>Week:</b> 5 (Hour 3)")],
))

# 2. Problem: Fake Free Cheats & Mods
S.append(slide(
    ph=("Muammo", "Проблема", "The Trap"), time="3–6",
    eyebrow=("Xavfli yuklamalar", "Опасные иллюзии", "Dangerous Downloads"),
    title=("'Tekin Cheat va Modlar': Xakerlar Bizni Qanday Tuzoqqa Tushiradi?",
           "«Бесплатные Читы и Моды»: Как Хакеры Заманивают в Ловушку?",
           "Free Cheats & Mods: How Attackers Bait Players"),
    body='<div class="cols">\n'
         + box("red", ("Soxta Va'dalar: 'Tekin Robux va Skinlar' ❌", "Ложные Обещания: «Бесплатные Скины и Читы» ❌", "Deceptive Bait: 'Free Robux & Aimbots' ❌"),
               items=[
                   ("YouTube yoki TikTokda jozibador video: <i>'Bu yangi cheatni yuklab olsangiz, har qanday o'yinda yutasiz!'</i>",
                    "Ролик на YouTube/TikTok: <i>«Скачай этот секретный чит и получи 10,000 гемов бесплатно!»</i>",
                    "Enticing YouTube/TikTok clips: <i>'Download this secret utility for infinite gems and instant wins!'</i>"),
                   ("Havola ostidagi fayl: <code>Cheat_Installer.zip</code> yoki <code>BrawlMod.apk</code>.",
                    "Ссылка в описании ведёт на архив: <code>Cheat_Installer.zip</code> или файл <code>BrawlMod.apk</code>.",
                    "Download link serves an archive: <code>Cheat_Installer.zip</code> or payload <code>BrawlMod.apk</code>."),
                   ("<b>Xaker qoidasi:</b> Hech bir begona odam sizga tekinga qimmat dastur bermaydi. Ichida yashirin 'sovg'a' bor!",
                    "<b>Закон сети:</b> Никто не раздаёт платные вещи даром. Внутри файла спрятан опасный «сюрприз»!",
                    "<b>Golden Rule:</b> Strangers never give away commercial assets for free. A payload always lurks inside!"),
               ])
         + "\n"
         + box("", ("Real Kiber-Xavf: Ko'rinmas Bosqin ⚠️", "Реальная Угроза: Невидимое Вторжение ⚠️", "Real Threat: Covert Infiltration ⚠️"),
               items=[
                   ("Faylni ishga tushirganingizda, o'yin ochilmasligi mumkin, lekin orqa fonda <b>virus tizimga o'rnashib oladi</b>.",
                    "При клике игра может даже не запуститься, но в тихом фоновом режиме вирус уже проникает в систему.",
                    "Upon execution, the game may fail to launch, but background scripts silently take full root."),
                   ("U brauzeringizdagi <b>barcha saqlangan parollarni</b> bir necha soniyada o'g'irlab, xakerga yuboradi.",
                    "Скрипт мгновенно выкачивает все сохранённые пароли браузера и отправляет их на командный сервер.",
                    "The payload harvests saved browser passwords within milliseconds and exfiltrates them to C2 servers."),
               ],
               extra_html=media_box("speed-speed-shaking-his-head.mp4", max_height="180px"))
         + "\n</div>"
))

# 3. History & Metaphor: The Trojan Horse
S.append(slide(
    ph=("Tarix va Metafora", "История и Метафора", "The Legend"), time="6–10",
    eyebrow=("Qadimgi afsona", "Военная хитрость", "Historical Roots"),
    title=("Troyalik Ot Nima va Nega Viruslar Shunday Ataladi?",
           "Что Такое «Троянский Конь» и Почему Вирус Назван в Его Честь?",
           "What is a Trojan Horse and Why Are Malware Named After It?"),
    body='<div class="cols">\n'
         + box("purple", ("Qadimgi Afsona: Yog'och Ot Qopqoni 🐴", "Легенда Древней Греции: Деревянный Конь 🐴", "Ancient Legend: The Wooden Steed 🐴"),
               p=("Qadimgi yunonlar Troya shahrining baland devorlarini yorib o'ta olishmagan. "
                  "Shunda ular ayyorlik ishlatishgan: ulkan yog'och ot yasab, ichiga saralangan askarlarni yashirishgan. "
                  "Troyaliklar otni 'g'alaba sovg'asi' deb o'ylab, o'z qo'llari bilan shahar ichiga olib kirishgan. "
                  "Kechasi esa askarlar ot ichidan chiqib, shahar darvozalarini ochib berishgan!",
                  "Греки не могли штурмом взять неприступные стены Трои. "
                  "Тогда они построили огромного деревянного коня и спрятали внутри отряд воинов. "
                  "Жители Трои решили, что это дар богов, и сами затащили коня внутрь крепости. "
                  "Ночью воины выбрались наружу и открыли ворота осаждающей армии!",
                  "Greek forces failed to breach Troy's impenetrable fortress walls for a decade. "
                  "They crafted a massive hollow wooden horse, hiding elite soldiers within. "
                  "Believing it was a sacred tribute, Trojans pulled the horse inside their citadel. "
                  "At midnight, the hidden soldiers emerged and opened the gates to their army!"))
         + "\n"
         + box("accent", ("Kiber-Dunyo: Dasturiy Troyanlar 💻", "Компьютерный Троян: Та Же Хитрость 💻", "Digital World: Software Trojans 💻"),
               p=("Kiber-troyan ham xuddi shunday ishlaydi! "
                  "U tashqaridan <b>juda foydali va qiziqarli dastur</b> (o'yin, fotomontaj, tekin mod) qiyofasiga kiradi. "
                  "Foydalanuvchi unga ishonib, <b>o'z qo'li bilan 'Run' (Ishga tushirish)</b> tugmasini bosadi. "
                  "Ichidagi zararli kod esa kompyuter devorlarini aylanib o'tib, xakerga tizim eshigini ochib beradi!",
                  "Компьютерный троян действует точь-в-точь по этой схеме! "
                  "Снаружи это якобы <b>полезная и крутая программа</b> (мод, чит, редактор скинов). "
                  "Пользователь сам, добровольно нажимает «Запустить». "
                  "А скрытый вредоносный код открывает злоумышленникам полный доступ к вашему компьютеру!",
                  "A computer Trojan behaves identically! "
                  "It masquerades as a <b>useful, desirable app</b> (game patch, skin editor, optimizer). "
                  "The user voluntarily executes it with administrative privileges. "
                  "The hidden payload executes silently from within, handing system keys over to the attacker!"))
         + "\n</div>"
))

# 4. Malware Families: Trojan, Stealer, Ransomware, Keylogger
S.append(slide(
    ph=("Zararli Oila", "Семейства Вирусов", "Malware Types"), time="10–14",
    eyebrow=("Kiber-yirtqichlar", "Классификация угроз", "Threat Taxonomy"),
    title=("Zararli Dasturlar (Malware) Oylasi: 4 Ta Asosiy Yirtqich",
           "Семейство Вредоносного ПО: 4 Главных Кибер-Хищника",
           "The Malware Family: 4 Primary Threat Classes"),
    body='<div class="cols">\n'
         + box("red", ("1. Troyan & InfoStealer (Ayg'oqchi) 🕵️", "1. Троян и Инфостилер (Шпион) 🕵️", "1. Trojan & InfoStealer 🕵️"),
               items=[
                   ("<b>Maqsadi:</b> Brauzerda saqlangan loginlar, Roblox kuki va Telegram sessiyalarini o'g'irlash.",
                    "<b>Цель:</b> Кража сохранённых паролей браузера, токенов Discord, Telegram и Roblox.",
                    "<b>Objective:</b> Stealing browser vaults, Telegram sessions, and Roblox cookies."),
                   ("<b>Misol:</b> RedLine, Lumma stealer — barcha parollarni 1 soniyada ZIP qilib jo'natadi.",
                    "<b>Пример:</b> RedLine, Lumma — упаковывают все ваши аккаунты в ZIP-архив за 1 секунду.",
                    "<b>Example:</b> RedLine, Lumma stealers exfiltrating your entire identity in a split second."),
               ])
         + "\n"
         + box("accent", ("2. Ransomware (Tovlamachi Virus) 🔒", "2. Программы-Вымогатели (Ransomware) 🔒", "2. Ransomware (Extortion) 🔒"),
               items=[
                   ("<b>Maqsadi:</b> Barcha rasmlar, hujjatlar va o'yin fayllarini kuchli shifr bilan qulflash.",
                    "<b>Цель:</b> Шифрование всех личных фото, документов и файлов до нечитаемого состояния.",
                    "<b>Objective:</b> Encrypting personal photos, family archives, and game saves."),
                   ("<b>Talabi:</b> Ekranda qizil xabar chiqadi: <i>'Fayllarni ochish uchun pul to'lang!'</i>",
                    "<b>Шантаж:</b> На экране появляется баннер: <i>«Заплатите выкуп, иначе файлы уничтожатся!»</i>",
                    "<b>Extortion:</b> Red banner demanding cryptocurrency to unlock corrupted files."),
               ])
         + "\n</div>\n"
         + '<div class="cols" style="margin-top:10px;">\n'
         + box("purple", ("3. Keylogger (Klaviaturani Poylovchi) ⌨️", "3. Кейлоггер (Перехватчик Клавиш) ⌨️", "3. Keystroke Logger (Spy) ⌨️"),
               items=[
                   ("<b>Maqsadi:</b> Siz klaviaturada tergan har bir harf, parol va xabarni yashirincha yozib olish.",
                    "<b>Цель:</b> Скрытная запись каждого нажатия клавиш на клавиатуре (логины, пароли, чаты).",
                    "<b>Objective:</b> Intercepting every pressed key to harvest confidential chats and credentials."),
               ])
         + "\n"
         + box("", ("4. Botnet & Zombi Dastur 🧟", "4. Ботнет и Зомби-Сети 🧟", "4. Botnet & Zombie Agent 🧟"),
               items=[
                   ("<b>Maqsadi:</b> Kompyuteringizni masofadan boshqariladigan 'zombi'ga aylantirib, kiber-hujumlar uyushtirish.",
                    "<b>Цель:</b> Превращение устройства в «зомби» для скрытых DDoS-атак на чужие серверы.",
                    "<b>Objective:</b> Enslaving the host machine into an automated army executing DDoS campaigns."),
               ])
         + "\n</div>"
))

# 5. Core Trick: Double Extensions
S.append(slide(
    ph=("Asosiy Hiyla", "Коварная Уловка", "The Decoy"), time="14–18",
    eyebrow=("Niqoblangan fayllar", "Двойные расширения", "Double Extensions"),
    title=("Ikki Qavatli Kengaytma: Xakerlar .exe Faylni Qanday Yashiradi?",
           "Двойное Расширение: Как Хакеры Маскируют .exe под Картинку?",
           "The Double Extension Trick: Camouflaging .exe as Media"),
    body='<div class="cols">\n'
         + box("red", ("Windowsning Standart Kamchiligi ⚙️", "Опасная Настройка Windows ⚙️", "Windows Default Flaw ⚙️"),
               p=("Odatiy holatda Windows operatsion tizimi fayllarning kengaytmasini <b>yashirib ko'rsatadi</b> "
                  "('Hide extensions for known file types'). "
                  "Masalan, <code>rasm.jpg</code> fayli shunchaki <code>rasm</code> bo'lib ko'rinadi.",
                  "По умолчанию Windows <b>скрывает расширения</b> известных типов файлов. "
                  "Например, файл <code>foto.png</code> отображается пользователю просто как <code>foto</code>.",
                  "By default, Windows hides known file extensions ('Hide extensions for known file types'). "
                  "Thus, <code>photo.png</code> appears simply as <code>photo</code>."))
         + "\n"
         + box("accent", ("Xakerning Aldov Hiylasi: .png.exe 🎭", "Хитрость Хакера: .png.exe 🎭", "The Hacker's Cloak: .png.exe 🎭"),
               p=("Xaker zararli dasturga shunday nom beradi: <code>Minecraft_Skin.png.exe</code>.<br>"
                  "Windows oxirgi <code>.exe</code> ni yashiradi, va ekranda faqat <code>Minecraft_Skin.png</code> qoladi!<br>"
                  "Foydalanuvchi buni rasm deb o'ylab 2 marta bosadi, aslida esa <b>zararli dastur (.exe)</b> ishga tushadi!",
                  "Хакер называет вредоносный файл: <code>Minecraft_Skin.png.exe</code>.<br>"
                  "Windows прячет конечный <code>.exe</code>, и на экране остаётся лишь <code>Minecraft_Skin.png</code>!<br>"
                  "Вы думаете, что открываете картинку, а система запускает опасную программу!",
                  "Adversaries name their payload: <code>Minecraft_Skin.png.exe</code>.<br>"
                  "Windows strips the final <code>.exe</code>, leaving only <code>Minecraft_Skin.png</code> visible!<br>"
                  "Victims assume it's harmless media, yet Windows executes raw executable bytecode!"))
         + "\n</div>\n"
         + box("green", ("Himoya Chora: Kengaytmalarni Har Doim Ko'rinadigan Qiling! 🛡️", "Защита: Всегда Включайте Отображение Расширений! 🛡️", "Defense: Always Force File Extension Visibility! 🛡️"),
               p=("Windows Explorer (Provodnik) sozlamalaridan <b>'File name extensions' (Fayl nom kengaytmalari)</b> bandiga "
                  "galochka qo'ying! Shunda hech bir xaker o'zining <code>.exe</code>, <code>.bat</code> yoki <code>.scr</code> kengaytmasini sizdan yashira olmaydi!",
                  "В проводнике Windows включите галочку <b>«Расширения имён файлов» (File name extensions)</b>! "
                  "Тогда ни один злоумышленник не спрячет опасный исполняемый файл <code>.exe</code> или <code>.scr</code>!",
                  "In Windows File Explorer, enable <b>'File name extensions'</b>! "
                  "No attacker will ever deceive you with masked <code>.exe</code>, <code>.bat</code>, or <code>.scr</code> binaries!"))
))

# 6. The Big Lie: False Positive
S.append(slide(
    ph=("Katta Yolg'on", "Большая Ложь", "The False Positive"), time="18–22",
    eyebrow=("Psixologik aldov", "Манипуляция хакеров", "Social Engineering"),
    title=("'Antivirusni O'chir, Bu Soxta Signal' — Kiber-Tuzoq!",
           "«Отключи Антивирус, Это Ложная Тревога» — Главный Обман!",
           "'Disable Antivirus, It Is a False Positive' — The Big Trap!"),
    body='<div class="cols">\n'
         + box("red", ("Xakerlarning Standart Ko'rsatmasi ⛔", "Инструкция от Злоумышленников ⛔", "The Hacker's Standard Playbook ⛔"),
               items=[
                   ("Har bir cheat/mod video qo'llanmasida aytiladi: <i>'Faylni ochishdan oldin Windows Defenderni vaqtinchalik o'chirib turing, u noto'g'ri xato bermoqda (False Positive)!'</i>",
                    "В каждом видео с читами говорят: <i>«Перед запуском отключите Windows Defender, антивирус просто ругается на кряк (False Positive)!»</i>",
                    "Every illicit mod tutorial commands: <i>'Disable Windows Defender before extracting, it is just a harmless False Positive!'</i>"),
                   ("Nega ular buni so'raydi? <b>Chunki antivirus ularning virusini darhol ushlab oladi va yo'q qiladi!</b>",
                    "Зачем они это просят? <b>Потому что антивирус моментально заблокирует их вирус!</b>",
                    "Why do they demand this? <b>Because Windows Defender detects and incinerates their malware on sight!</b>"),
               ])
         + "\n"
         + box("green", ("Kiber-Qalqon Qoidasi: Antivirusni Hech Qachon O'chirmang! 🛡️", "Железное Правило: Никогда Не Отключайте Защиту! 🛡️", "The Iron Rule: Never Disable Real-Time Shields! 🛡️"),
               items=[
                   ("Agar antivirus faylni bloklasa — <b>99.9% ehtimol bilan bu haqiqiy xavfli troyan</b>!",
                    "Если антивирус бьёт тревогу — в 99.9% случаев файл действительно заражён опасным трояном!",
                    "If your security shield raises an alert, it is a critical trojan in 99.9% of instances!"),
                   ("Antivirusni o'chirish — bu o'z uyingizning temir eshigini ochib, qaroqchilarga <i>'Marhamat, kiring'</i> deb aytish bilan tengdir.",
                    "Отключить антивирус — всё равно что открыть входную дверь квартиры настежь и пригласить грабителей.",
                    "Turning off antivirus is equivalent to unlocking your home's front door and inviting burglars in."),
               ])
         + "\n</div>"
))

# 7. Static Analysis: VirusTotal & Hashes
S.append(slide(
    ph=("Statik Tahlil", "Статический Анализ", "Static Triage"), time="22–26",
    eyebrow=("Raqamli barmoq izi", "Цифровой отпечаток", "Cryptographic Hashes"),
    title=("VirusTotal va SHA-256: Faylning Raqamli Barmoq Izi",
           "VirusTotal и Хеши SHA-256: Цифровые Отпечатки Файлов",
           "VirusTotal & SHA-256: Digital File Fingerprinting"),
    body='<div class="cols">\n'
         + box("accent", ("Fayl Xeshi (SHA-256) Nima? 🧬", "Что Такое Хеш Файла (SHA-256)? 🧬", "What is a File Hash (SHA-256)? 🧬"),
               p=("Har bir fayl o'zining takrorlanmas matematik 'barmoq izi'ga (xesh kodiga) ega. "
                  "Fayl ichidagi bitta nuqta o'zgarsa ham, uning SHA-256 xeshi butunlay boshqa bo'lib qoladi.<br>"
                  "<code>SHA-256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855</code>",
                  "Каждый файл имеет уникальный математический «отпечаток пальца» — хеш SHA-256. "
                  "Измените в файле хоть один байт — и хеш полностью изменится до неузнаваемости.<br>"
                  "<code>SHA-256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855</code>",
                  "Every file possesses a unique cryptographic fingerprint known as a SHA-256 hash. "
                  "Altering a single bit alters the computed hash completely.<br>"
                  "<code>SHA-256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855</code>"))
         + "\n"
         + box("purple", ("VirusTotal Platformasi Qanday Ishlaydi? 🌐", "Как Работает Платформа VirusTotal? 🌐", "How Does VirusTotal Operate? 🌐"),
               p=("VirusTotal — bu butun dunyo kiber-ekspertlari ishlatadigan xizmat. "
                  "Siz faylni yuklaganingizda, u bir vaqtning o'zida <b>70 dan ortiq eng kuchli antivirus dvigatellari</b> "
                  "(Kaspersky, Microsoft Defender, ESET, Avast, Bitdefender) orqali tekshiriladi!<br>"
                  "Natija ko'rsatiladi: <b>0/70 (Toza)</b> yoki <b>58/70 (Xavfli Troyan!)</b>.",
                  "VirusTotal — международный сервис кибербезопасности. "
                  "При загрузке файла он проверяется базой из более чем <b>70 ведущих антивирусных движков</b> "
                  "(Kaspersky, Microsoft, ESET, Avast, Sophos) одновременно!<br>"
                  "Вердикт виден сразу: <b>0/70 (Чисто)</b> или <b>58/70 (Опасный троян!)</b>.",
                  "VirusTotal is a global threat intelligence aggregator. "
                  "Uploading a sample executes concurrent scans across <b>70+ premier antivirus engines</b> "
                  "(Kaspersky, Microsoft Defender, ESET, Avast, Bitdefender)!<br>"
                  "The verdict is decisive: <b>0/70 (Clean)</b> or <b>58/70 (Malicious Trojan!)</b>."))
         + "\n</div>"
))

# 8. Dynamic Analysis: The Sandbox
S.append(slide(
    ph=("Dinamik Tahlil", "Песочница", "Dynamic Sandbox"), time="26–30",
    eyebrow=("Virtual laboratoriya", "Безопасный полигон", "Isolated Detonation"),
    title=("Qumloq (Sandbox): Zararli Dasturni Qanday Fosh Qilamiz?",
           "Песочница (Sandbox): Как Изучают Поведение Вирусов?",
           "The Sandbox: Dynamic Behavioral Inspection"),
    body='<div class="cols">\n'
         + box("purple", ("Qumloq (Sandbox) Nima? 🧪", "Что Такое Песочница (Sandbox)? 🧪", "What is an Analysis Sandbox? 🧪"),
               p=("Qumloq — bu haqiqiy operatsion tizimdan to'liq ajratilgan <b>virtual shisha quti</b>. "
                  "Kiber-mutaxassislar shubhali dasturni sandbox ichida xavfsiz ishga tushirib, "
                  "uning nima ish qilmoqchi ekanligini mikroskop ostida kuzatishadi.",
                  "Песочница — это изолированная <b>виртуальная среда</b>, отделённая от вашей реальной системы. "
                  "Аналитики запускают подозрительный файл внутри песочницы и смотрят, как он себя ведёт, "
                  "не рискуя заразить рабочий компьютер.",
                  "A Sandbox is an isolated <b>virtual detonation chamber</b> partitioned from production systems. "
                  "Security analysts safely execute suspicious binaries within to examine their live behaviors "
                  "without endangering host infrastructure."))
         + "\n"
         + box("red", ("Sandbox Nimalarni Nazorat Qiladi? 🔍", "За Чем Следит Песочница? 🔍", "What Behaviors Does It Monitor? 🔍"),
               items=[
                   ("<b>Fayl Tizimi:</b> Dastur yashirincha <code>%AppData%</code> yoki <code>System32</code> ga fayl yozdimi?",
                    "<b>Файловая система:</b> Пытается ли программа спрятать файлы в <code>%AppData%</code> или <code>System32</code>?",
                    "<b>File System:</b> Does the process drop hidden payloads into <code>%AppData%</code> or <code>System32</code>?"),
                   ("<b>Reestr:</b> Kompyuter yoqilganda avtomatik ishga tushish uchun o'zini avto-startga qo'shdimi?",
                    "<b>Реестр:</b> Прописывается ли программа в автозагрузку Windows для постоянного шпионажа?",
                    "<b>Registry:</b> Does it modify Run keys to establish persistent autorun survival?"),
                   ("<b>Tarmoq (Network):</b> Noma'lum xorijiy IP-manzilga parollarni jo'natishga urindimi?",
                    "<b>Сеть:</b> Пытается ли программа связаться с подозрительным сервером за границей (C2)?",
                    "<b>Network Activity:</b> Does it attempt telemetry beaconing or exfiltration to foreign C2 hosts?"),
               ])
         + "\n</div>"
))

# 9. Practical Lab Intro: Malware Scanner Studio
S.append(slide(
    ph=("Amaliy Mashq", "Практикум", "Interactive Lab"), time="30–35",
    eyebrow=("Kiber-detektiv laboratoriyasi", "Тренажёр детектива", "Forensic Studio"),
    title=("Malware Scanner Studio: Bugungi Missiyangiz!",
           "Тренажёр Детектива: Ваша Лабораторная Миссия!",
           "Malware Scanner Studio: Your Forensic Mission!"),
    body='<div class="cols">\n'
         + box("green", ("Sizning Vazifangiz: 6 Ta Shubhali Faylni Tekshirish 🎯", "Ваша Задача: Экспертиза 6 Подозрительных Файлов 🎯", "Your Objective: Inspect 6 Unknown File Payloads 🎯"),
               items=[
                   ("Kompyuteringizda <b>Malware Scanner Studio</b> dasturini oching (yoki <code>scanner/index.html</code> ga kiring).",
                    "Откройте на экране тренажёр <b>Malware Scanner Studio</b> (файл <code>scanner/index.html</code>).",
                    "Launch the <b>Malware Scanner Studio</b> on your workstation (or browse to <code>scanner/index.html</code>)."),
                   ("Navbatdagi har bir faylning haqiqiy kengaytmasini, SHA-256 xeshini va sandbox harakatlarini tahlil qiling.",
                    "Изучите реальное расширение каждого файла, его хеш SHA-256 и поведенческие логи песочницы.",
                    "Analyze the actual extension, SHA-256 hash, and sandbox behavior logs for each payload."),
                   ("To'g'ri qaror qabul qiling: <b>✅ Ruxsat berish (Clean)</b> yoki <b>🛑 Karantinga olish (Quarantine)</b>!",
                    "Вынесите вердикт эксперта: <b>✅ Безопасно (Clean)</b> или <b>🛑 В карантин (Quarantine)</b>!",
                    "Render your verdict: <b>✅ Mark Clean</b> or <b>🛑 Quarantine & Purge</b>!"),
               ])
         + "\n"
         + box("accent", ("Tergov Qilinadigan Fayllar Ro'yxati 📂", "Список Файлов для Расследования 📂", "Evidence Queue for Investigation 📂"),
               items=[
                   ("<code>BrawlStars_UnlimitedGems.apk</code> (Android troyan stealer)",
                    "<code>BrawlStars_UnlimitedGems.apk</code> (Троян-стилер под видом мода)",
                    "<code>BrawlStars_UnlimitedGems.apk</code> (Android credential stealer)"),
                   ("<code>Minecraft_Optifine_Shader.zip.exe</code> (Ikki qavatli kengaytma)",
                    "<code>Minecraft_Optifine_Shader.zip.exe</code> (Опасное двойное расширение)",
                    "<code>Minecraft_Optifine_Shader.zip.exe</code> (Double extension Trojan)"),
                   ("<code>Target_English_Homework.pdf</code> (Haqiqiy maktab hujjati)",
                    "<code>Target_English_Homework.pdf</code> (Легальный школьный PDF)",
                    "<code>Target_English_Homework.pdf</code> (Legitimate school document)"),
                   ("<code>Roblox_Delta_Executor_v3.bat</code> (Xavfli skript fayl)",
                    "<code>Roblox_Delta_Executor_v3.bat</code> (Вредоносный скрипт)",
                    "<code>Roblox_Delta_Executor_v3.bat</code> (Malicious registry batch script)"),
               ])
         + "\n</div>"
))

# 10. The 5 Golden Rules of Safe Software
S.append(slide(
    ph=("Qoidalar", "Золотые Правила", "Safety Rules"), time="35–38",
    eyebrow=("Kiber-gigiyena", "Кодекс кибер-щита", "Hygiene Standard"),
    title=("Kiber-Himoyachining 5 Oltin Qoidasi",
           "5 Золотых Правил Кибер-Защитника от Вирусов",
           "The 5 Golden Rules of Software Safety"),
    body='<div class="cols">\n'
         + box("green", ("Xavfsiz Dasturlar Kodeksi 🛡️", "Кодекс Безопасного Софта 🛡️", "The Safe Software Protocol 🛡️"),
               items=[
                   ("<b>1. Rasmiy Manbalar:</b> O'yin va dasturlarni faqat rasmiy do'konlardan yuklang (Steam, Google Play, App Store).",
                    "<b>1. Официальные источники:</b> Загружайте игры только из официальных сторов (Steam, Google Play, App Store).",
                    "<b>1. Official Repositories:</b> Install software solely from verified app stores (Steam, Google Play, App Store)."),
                   ("<b>2. Kengaytmalarni Tekshir:</b> Windows sozlamalarida fayl kengaytmalarini har doim ko'rinadigan qilib qo'y.",
                    "<b>2. Проверяй расширения:</b> Включи видимость расширений в Windows, чтобы видеть скрытые <code>.exe</code>.",
                    "<b>2. Audit Extensions:</b> Keep file extension visibility enabled in Windows to unmask hidden executables."),
                   ("<b>3. Defender — Qalqon:</b> Hech qachon, hech qanday video iltimosi bilan antivirusni o'chirma!",
                    "<b>3. Защитник включён:</b> Никогда не отключай Windows Defender по просьбе блогеров или роликов!",
                    "<b>3. Shield Stays Active:</b> Never disable real-time protection at the behest of third-party videos!"),
                   ("<b>4. VirusTotal Nazorati:</b> Shubhali har qanday fayl xeshini ochishdan oldin VirusTotal'da tekshir.",
                    "<b>4. Проверка на VirusTotal:</b> Любой незнакомый архив или файл сначала проверь через VirusTotal.",
                    "<b>4. VirusTotal Pre-Check:</b> Submit suspicious downloads to VirusTotal before executing them locally."),
                   ("<b>5. Tekin Pishloq Yo'q:</b> Internetda 'tekin cheat va robux' beruvchi fayllarning barchasi tuzoqdir!",
                    "<b>5. Бесплатный сыр — ловушка:</b> «Бесплатные читы и игровая валюта» создаются только ради кражи ваших данных!",
                    "<b>5. No Free Lunch:</b> Unofficial 'cheat engines' and 'free currency generators' exist only to compromise your accounts!"),
               ])
         + "\n</div>"
))

# 11. Worksheet Rubric & Criteria
S.append(slide(
    ph=("Baholash", "Критерии Оценки", "Grading Rubric"), time="38–41",
    eyebrow=("10 ballik mezon", "Критерии успеха", "Scoring Rubric"),
    title=("Laboratoriya Baholash Mezoni (10 Ball)",
           "Критерии Оценки за Урок (10 Баллов)",
           "Lab Mission Grading Rubric (10 Points)"),
    body='<div class="cols">\n'
         + box("accent", ("Amaliy Topshiriq Mezonlari 📝", "Баллы за Лабораторную Работу 📝", "Worksheet Performance Criteria 📝"),
               items=[
                   ("<b>4 Ball — Laboratoriya Tergovi:</b> Varaqadagi 4 ta keys bo'yicha haqiqiy kengaytma va xavf darajasini to'g'ri topish.",
                    "<b>4 Балла — Экспертиза 4 кейсов:</b> Определение реальных расширений и опасности в таблице рабочего листа.",
                    "<b>4 Points — Forensic Triage:</b> Correctly identifying authentic extensions and threat vectors across 4 cases."),
                   ("<b>3 Ball — Troyan Mexanizmi va Double Extension:</b> .png.exe hiylasi va 'Antivirusni o'chir' yolg'onini tushuntirish.",
                    "<b>3 Балла — Механика троянов:</b> Объяснение уловки с двойным расширением и мифа об отключении антивируса.",
                    "<b>3 Points — Threat Mechanics:</b> Explaining double extensions (.png.exe) and debunking the false-positive myth."),
                   ("<b>3 Ball — VirusTotal va Sandbox Tahlili:</b> Statik xesh (SHA-256) va dinamik qumloq vazifalarini to'g'ri yozish.",
                    "<b>3 Балла — VirusTotal и Sandbox:</b> Грамотное описание роли хешей SHA-256 и песочницы для анализа ПО.",
                    "<b>3 Points — Detection Science:</b> Articulating SHA-256 fingerprinting and sandbox behavior tracking."),
               ])
         + "\n</div>"
))

# 12. Conclusion & Summary
S.append(slide(
    ph=("Xulosa", "Итоги Недели", "Wrap-up"), time="41–45",
    eyebrow=("5-hafta yakuni", "Триумф Кибер-Щита", "Cohort Mastery"),
    title=("5-Hafta Xulosasi: Kiber-Qalqon To'liq Ishga Tushdi! 🏆",
           "Итоги 5-й Недели: Кибер-Щит Полностью Активирован! 🏆",
           "Week 5 Summary: Full Cyber-Shield Activated! 🏆"),
    body='<div class="cols">\n'
         + box("green", ("Uch Qadamli Kiber-Mudofaa 🌟", "Трёхступенчатая Кибер-Оборона 🌟", "Three-Tiered Cyber Defense 🌟"),
               items=[
                   ("<b>17-dars (Parollar Jangi):</b> Buzilmas Passphrase va Brute-Force himoyasi o'rganildi.",
                    "<b>Урок 17 (Битва Паролей):</b> Освоены стойкие пароли-фразы и защита от перебора Brute-Force.",
                    "<b>Lesson 17 (Passwords):</b> Mastered unbreakable Passphrases & Brute-Force defense."),
                   ("<b>18-dars (Fishing Detektori):</b> Soxta havolalar, Telegram tuzoqlari va aldovlar fosh qilindi.",
                    "<b>Урок 18 (Детектор Фишинга):</b> Раскрыты фальшивые ссылки, уловки Telegram и социальная инженерия.",
                    "<b>Lesson 18 (Phishing):</b> Exposed fraudulent URLs, lookalikes, and social engineering."),
                   ("<b>19-dars (Troyanlar va Viruslar):</b> Zararli yuklamalar, .png.exe hiylasi va Sandbox tahlili o'zlashtirildi!",
                    "<b>Урок 19 (Трояны и Вирусы):</b> Изучены опасные файлы, трюк .png.exe и песочницы для проверки софта!",
                    "<b>Lesson 19 (Malware & Trojans):</b> Mastered covert downloads, double extensions, and sandbox triage!"),
               ])
         + "\n</div>\n"
         + box("purple", ("Tabriklaymiz! Siz Endi — Sertifikatlangan Kiber-Himoyachisiz! 🎖️", "Поздравляем! Вы — Сертифицированный Кибер-Защитник! 🎖️", "Congratulations! You Are Certified Cyber-Defenders! 🎖️"),
               p=("5–6-sinf o'quvchilari o'z akkauntlari, oilaviy kompyuterlari va shaxsiy ma'lumotlarini har qanday xakerlik hujumidan "
                  "professional darajada asrashni to'liq o'rganib oldilar!",
                  "Ученики 5–6 классов теперь умеют защищать свои игровые аккаунты, соцсети и домашние компьютеры "
                  "от любых хакерских уловок и вредоносных программ на профессиональном уровне!",
                  "Grades 5–6 students now possess comprehensive defensive skills to safeguard gaming accounts, family workstations, "
                  "and personal identity against sophisticated cyber adversaries!"))
))

NOTES = {
    "uz": [
        ["Kirish", "O'quvchilarga xush kelibsiz deng. O'tgan 17-darsda parollarni, 18-darsda fishing havolalarini o'rganganimizni eslating. Bugun eng xavfli kiber-hujum — troyan viruslari haqida gaplashamiz.", "1-slaydni oching va dars mavzusini doskaga yozing."],
        ["Tekin Modlar Tuzog'i", "O'quvchilardan so'rang: 'Oralaringizda hech o'yinga mod yoki cheat yuklab olganlar bormi?'. YouTube'dagi soxta videolarning asl maqsadini ochib bering.", "Speed videosini ko'rsating va tekin narsa yo'qligini ayting."],
        ["Troyalik Ot Afsonasi", "Qadimgi Troya urushini qisqa va qiziqarli hikoya qilib bering. Nega xakerlar o'z viruslarini aynan 'Troyan' deb atashini tushuntiring.", "Ot metaforasi va foydali dastur niqobi o'rtasidagi o'xshashlikni chizib ko'rsating."],
        ["Malware Oylasi", "Zararli dasturlarning 4 ta asosiy turini tushuntiring: Troyan, InfoStealer (parol o'g'irlaydi), Ransomware (fayllarni qulflaydi) va Keylogger.", "Har bir turning zararini real misollarda (Roblox akkaunt, Discord) tushuntiring."],
        ["Ikki Qavatli Kengaytma", "Windows odatda .exe ni yashirishini va rasm_nomi.png.exe qanday qilib foydalanuvchini aldashini doskada ko'rsatib bering.", "Provodnikda kengaytmalarni ko'rsatish sozlamasini tushuntiring."],
        ["Antivirusni O'chir Yolg'oni", "Nega blogerlar 'Antivirusni o'chir' deyishini fosh qiling. Agar antivirus signal bersa, bu haqiqiy virus ekanligini uqtiring.", "Antivirusni o'chirish hech qachon mumkin emasligini ta'kidlang."],
        ["VirusTotal va Xesh", "SHA-256 xesh kodini insonning barmoq iziga o'xshating. VirusTotal 70 ta antivirus bilan bir vaqtda tekshirishini ayting.", "VirusTotal ekrani qanday ko'rinishini doskada tasvirlang."],
        ["Sandbox Qumlog'i", "Sandbox nima ekanini virtual laboratoriya sifatida tushuntiring: u xavfsiz shisha idish ichida dastur xatti-harakatini tekshiradi.", "Dastur qaysi fayllarni o'zgartirishi va qayerga parollarni jo'natishini kuzatishni ayting."],
        ["Amaliy Mashq Boshlanishi", "O'quvchilarni Malware Scanner Studio'ga yo'naltiring. 6 ta keysni navbatma-navbat tekshirish tartibini tushuntiring.", "Varaqadagi 4 ta keys jadvalini to'ldirishni boshlashlarini ayting."],
        ["5 Oltin Qoida", "Xavfsiz dastur o'rnatishning 5 ta oltin qoidasini birgalikda o'qing va daftarga yozdiring.", "O'quvchilardan eng muhim qoidani takrorlashni so'rang."],
        ["Baholash Mezoni", "Varaqa qanday baholanishini tushuntiring: 4 ball tergov jadvali, 3 ball troyan mexanizmi, 3 ball xesh va sandbox.", "O'quvchilar mustaqil ishlashiga 12 daqiqa bering va sinf bo'ylab yordam bering."],
        ["Xulosa va Yakun", "5-hafta davomida erishilgan natijalarni sarhisob qiling: Parol + Anti-Fishing + Anti-Troyan = Kiber-Qalqon! O'quvchilarni tabriklang.", "Varaqalarni yig'ib oling va yuqori ball to'plaganlarni e'lon qiling."]
    ],
    "ru": [
        ["Введение", "Поприветствуйте учеников. Напомните, что на 17-м уроке мы защищали пароли, на 18-м разоблачали фишинг, а сегодня изучим самую опасную угрозу — троянские вирусы.", "Откройте титульный слайд и озвучьте тему урока."],
        ["Ловушка Модов", "Спросите ребят: «Кто хоть раз искал читы или моды на Brawl Stars или Roblox?». Объясните скрытую цель таких видеороликов.", "Покажите видеомем со Спидом и объясните коварство бесплатных приманок."],
        ["Легенда о Троянском Коне", "Ярко расскажите легенду об осаде Трои и деревянном коне. Проведите прямую параллель с компьютерными троянами.", "Объясните, почему пользователь сам добровольно запускает троян."],
        ["Семейство Malware", "Разберите 4 типа угроз: троян, инфостилер (крадёт пароли браузера), вымогатель Ransomware и кейлоггер.", "Приведите примеры украденных аккаунтов Roblox и Telegram."],
        ["Двойное Расширение", "Покажите, как скрытие расширений в Windows позволяет маскировать .exe под .png или .pdf.", "Объясните, как включить отображение расширений в проводнике Windows."],
        ["Миф об Отключении Защиты", "Разоблачите уловку авторов читов «отключите антивирус». Докажите, что срабатывание защиты — это реальный сигнал опасности.", "Подчеркните: отключать защиту категорически запрещено."],
        ["VirusTotal и Хеши", "Объясните хеш SHA-256 как цифровой отпечаток пальца файла. Расскажите про 70 антивирусных движков на VirusTotal.", "Покажите, как читать вердикт 0/70 и 58/70."],
        ["Песочница Sandbox", "Расскажите про изолированную среду Sandbox: она позволяет запускать файл без риска для основного компьютера.", "Покажите анализ поведенческих логов: автозагрузка, реестр, сеть."],
        ["Старт Лабораторной", "Направьте учеников к тренажёру Malware Scanner Studio. Объясните алгоритм исследования 6 кейсов.", "Контролируйте заполнение таблицы в рабочем листе."],
        ["5 Золотых Правил", "Зачитайте и закрепите 5 правил цифровой гигиены при установке программ.", "Спросите нескольких учеников, какое правило они считают главным."],
        ["Критерии Оценки", "Разъясните 10-балльную шкалу: 4 балла за экспертизу, 3 за двойное расширение, 3 за хеши и песочницу.", "Выделите 12 минут на самостоятельную работу и помогайте ученикам."],
        ["Итоги Недели", "Подведите итоги 5-й недели: пароли + фишинг + трояны = полный Кибер-Щит! Поздравьте ребят с успешным завершением модуля.", "Соберите рабочие листы и похвалите активных учеников."]
    ],
    "en": [
        ["Introduction", "Welcome students. Recap that lesson 17 fortified passwords and lesson 18 dismantled phishing. Today we confront stealth malware: Trojans.", "Display slide 1 and announce the lesson scope."],
        ["The Fake Cheat Bait", "Engage the room: 'Who has ever searched for Minecraft shaders or Roblox scripts?'. Expose malicious payload distribution tactics.", "Play the Speed reaction clip and emphasize that zero software is truly free."],
        ["The Trojan Horse Legend", "Recount the historical siege of Troy and the wooden horse ploy. Establish a direct analogy with digital Trojan binaries.", "Highlight that victims voluntarily execute Trojan payloads."],
        ["Malware Families", "Deconstruct 4 threat classes: Trojans, InfoStealers, Ransomware lockers, and Keystroke Loggers.", "Illustrate consequences using hijacked Roblox cookies and Discord sessions."],
        ["Double Extension Deception", "Demonstrate how Windows hiding file extensions enables .png.exe deception attacks.", "Instruct students on enabling 'File name extensions' in File Explorer."],
        ["Debunking False Positives", "Dismantle the 'disable Windows Defender' social engineering script. Explain that alerts signify legitimate threats.", "Reiterate the rule: never drop defensive shields."],
        ["VirusTotal & Hashes", "Define SHA-256 hashes as cryptographic file fingerprints. Introduce VirusTotal aggregating 70+ scanner engines.", "Demonstrate interpreting 0/70 vs 58/70 verdicts."],
        ["The Analysis Sandbox", "Explain Sandboxes as virtual glass detonation chambers allowing safe live execution monitoring.", "Walk through behavioral logging: registry edits, persistence, and network exfiltration."],
        ["Lab Mission Launch", "Direct students to the interactive Malware Scanner Studio. Outline the forensic triage protocol across all samples.", "Supervise forensic worksheet documentation."],
        ["5 Golden Rules", "Review the 5 fundamental rules of safe software acquisition.", "Prompt students to articulate the most vital hygiene rule."],
        ["Grading Rubric", "Clarify the 10-point rubric: 4 pts for forensic cases, 3 pts for Trojan mechanics, 3 pts for hashes & sandboxing.", "Allocate 12 minutes for focused worksheet execution."],
        ["Weekly Wrap-up", "Synthesize Week 5 achievements: Passwords + Phishing Defense + Anti-Trojan Shields = Full Cyber-Shield! Commend the cohort.", "Collect worksheets and evaluate detective scores."]
    ]
}

# ---------------------------------------------------------------- Worksheet (Varaqa)
V = []

V.append(sheet_header(
    h1=("Kiberxavfsizlik: Zararli Dasturlar va Troyanlar",
        "Кибербезопасность: Вредоносное ПО и Трояны",
        "CyberSecurity: Malware, Trojans & Software Safety"),
    sub=("5-hafta · 19-dars · Amaliy Laboratoriya Varaqasi",
         "Неделя 5 · Урок 19 · Практический Рабочий Лист",
         "Week 5 · Lesson 19 · Forensic Lab Worksheet")
))

V.append(mission(
    h=("Laboratoriya Vazifasi: Shubhali Fayllar Ekspertizasi va Kiber-Qalqon",
       "Миссия Лабораторной: Экспертиза Подозрительных Файлов и Кибер-Щит",
       "Lab Mission: Forensic Payload Triage & Cyber-Shield Verification"),
    p=("Zararli dasturlar (Malware) turlarini ajratish, soxta ikki qavatli kengaytmalarni (.exe, .scr) fosh qilish "
       "hamda xavfsiz dasturlar bilan viruslarni ajratish bo'yicha tahliliy xulosa berish.",
       "Классифицировать вредоносные программы (Malware), разоблачить коварные двойные расширения (.exe, .scr) "
       "и провести техническую экспертизу подозрительных файлов в симуляторе.",
       "Classify malware species, expose deceptive double-extension camouflages (.exe, .scr), "
       "and execute forensic payload triage across unknown inbound application files."))
)

V.append(table(
    headers=[
        ("Keys #", "Кейс", "Case"),
        ("Fayl Nomi va Ko'rinishi", "Имя и Маскировка Файла", "File Name & Masquerade"),
        ("Haqiqiy Turi / Kengaytma", "Реальное Расширение", "True File Extension"),
        ("Xavf Turi va Hukm (Toza / Virus)", "Угроза и Вердикт", "Threat Type & Verdict")
    ],
    rows=[
        [("Keys 1", "Кейс 1", "Case 1"),
         ("`BrawlStars_UnlimitedGems.apk`", "«BrawlStars_UnlimitedGems.apk»", "'BrawlStars_UnlimitedGems.apk'"),
         ("Android Ilova (.apk)", "Android пакет (.apk)", "Android Application (.apk)"),
         ("❌ Xavfli Troyan InfoStealer", "❌ Опасный троян-стилер", "❌ Critical InfoStealer Trojan")],
        [("Keys 2", "Кейс 2", "Case 2"),
         ("`Minecraft_Shader.zip.exe`", "«Minecraft_Shader.zip.exe»", "'Minecraft_Shader.zip.exe'"),
         ("Ijrochi Fayl (.exe)", "Исполняемый (.exe)", "Executable Binary (.exe)"),
         ("❌ Ikki Kengaytmali Tuzoq", "❌ Двойное расширение (.exe)", "❌ Masked Double-Extension")],
        [("Keys 3", "Кейс 3", "Case 3"),
         ("`Target_Homework.pdf`", "«Target_Homework.pdf»", "'Target_Homework.pdf'"),
         ("Hujjat (.pdf)", "Документ (.pdf)", "Document File (.pdf)"),
         ("✅ Toza Maktab Hujjati", "✅ Безопасный документ", "✅ Clean School Document")],
        [("Keys 4", "Кейс 4", "Case 4"),
         ("`Roblox_AutoClicker.bat`", "«Roblox_AutoClicker.bat»", "'Roblox_AutoClicker.bat'"),
         ("Batch Skript (.bat)", "Скрипт Windows (.bat)", "Windows Batch Script (.bat)"),
         ("❌ Reestrni Buzuvchi Zahar", "❌ Опасный скрипт реестра", "❌ Destructive Registry Script")]
    ]
))

V.append(sheet_box(
    h=("Kiber-Tahlilchi Ekspert Xulosasi", "Экспертное Заключение Кибер-Аналитика", "Cyber-Analyst Technical Findings"),
    body_html=writelines(3, label=("1. Xakerlar nega '.png.exe' yoki '.pdf.scr' usulidan foydalanadi va Windowsda buni qanday fosh qilish mumkin?",
                                   "1. Зачем хакеры используют приём «.png.exe» и как настроить Windows, чтобы видеть обман?",
                                   "1. Why do attackers deploy '.png.exe' decoys, and what Windows configuration neutralizes this trick?"))
             + "<br>"
             + writelines(2, label=("2. Nega cheat yuklaganda blogerlar 'Antivirusni o'chir' deb talab qiladi va nega bunga hech qachon ishonmaslik kerak?",
                                   "2. Почему создатели читов просят отключить антивирус и почему это категорически нельзя делать?",
                                   "2. Why do illicit mod tutorials demand disabling antivirus, and why is obedience disastrous?"))
))

V.append(sheet_box(
    h=("Baholash Mezoni (10 Ball)", "Критерии Оценки (10 Баллов)", "Grading Rubric (10 Points)"),
    body_html=rubric([
        (("4 ta keysdagi soxta fayllar, kengaytmalar va xavf turlari aniqlangan", "Все 4 кейса исследованы, расширения и угрозы зафиксированы", "All 4 cases investigated and file extensions logged"), "4 ball"),
        (("Double extension (.png.exe) va antivirusni o'chirish xavfi asoslangan", "Развенчан миф об отключении защиты и раскрыт трюк .png.exe", "Double-extension risks and antivirus persistence justified"), "3 ball"),
        (("SHA-256 xesh va Sandbox (Qumloq) tahlilining ahamiyati to'g'ri yozilgan", "Обоснована роль хешей SHA-256 и песочницы для анализа ПО", "SHA-256 fingerprinting and sandbox detonation properly explained"), "3 ball"),
    ], "10 ball")
))

V.append("</div>\n" + sign_box("Musulmonov Mamarajab"))

VARAQA_BODY = "\n".join(V)

lesson = Lesson(
    outdir=D,
    titles=TITLES,
    sheet_titles=SHEET_TITLES,
    key="vc-notes-5-19",
    slides=S,
    notes=NOTES,
    varaqa_body=VARAQA_BODY
)

if __name__ == "__main__":
    out = lesson.build()
    print("Created:", out)
