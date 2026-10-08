# -*- coding: utf-8 -*-
"""10-11-sinf · 5-hafta · 21-dars — Kriptografiya Asoslari: AES-256, RSA va Crypto Studio Playground."""

import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from build import (Lesson, slide, title_slide, box, code, el, i18n,
                   sheet_header, mission, table, sheet_box, rubric, writelines, sign_box)

D = "classes/10-11-sinf/5-hafta/21-dars-kriptografiya-aes-va-rsa"

TITLES = {
    "uz": "21-dars: Kriptografiya Asoslari — AES-256, RSA va Crypto Studio",
    "ru": "Урок 21: Основы Криптографии — AES-256, RSA и Crypto Studio",
    "en": "Lesson 21: Applied Cryptography — AES-256, RSA & Crypto Studio Playground",
}
SHEET_TITLES = {k: v + (" — Ish Varaqasi" if k == "uz" else
                        " — Рабочий Лист" if k == "ru" else " — Worksheet")
                for k, v in TITLES.items()}

S = []

# 1. Title Slide
S.append(title_slide(
    ph=("Kirish", "Введение", "Intro"), time="0–3",
    eyebrow=("CyberSecurity · 21-dars · 10–11-sinf (Applied Cryptography)",
             "CyberSecurity · Урок 21 · 10–11 класс (Applied Cryptography)",
             "CyberSecurity · Lesson 21 · Grades 10–11 (Applied Cryptography)"),
    h1=("Kriptografiya Asoslari: AES-256, RSA va Maxfiy Aloqa",
        "Основы Криптографии: AES-256, RSA и Секретная Связь",
        "Applied Cryptography: AES-256, RSA & Secure Messaging"),
    lede=("Har kuni milliardlab odamlar WhatsApp orqali yozishadi, bank kartalari bilan to'lov qilishadi va parollarni saqlashadi. "
          "Nega xakerlar bu ma'lumotlarni o'g'irlay olishmaydi? Chunki ularni zamonaviy <b>matematik shifrlar</b> qo'riqlaydi! "
          "Bugungi darsda biz <b>Simmetrik (AES-256)</b> va <b>Asimmetrik (RSA-2048)</b> shifrlash sirlarini, "
          "Sony PlayStation 3 ning tarixiy kiber-halokatini hamda interaktiv <b>Crypto Studio</b> laboratoriyasida "
          "bir-birimizga maxfiy shifrlangan xabarlar yuborishni o'rganamiz!",
          "Каждый день миллиарды людей переписываются в WhatsApp, оплачивают покупки картами и входят в аккаунты. "
          "Почему злоумышленники не могут перехватить эти данные в сети? Их защищает <b>математическая криптография</b>! "
          "Сегодня мы разберём секреты <b>симметричного (AES-256)</b> и <b>асимметричного (RSA-2048)</b> шифрования, "
          "катастрофическую ошибку инженеров Sony PlayStation 3 и в интерактивной лаборатории <b>Crypto Studio</b> "
          "научимся обмениваться зашифрованными сообщениями!",
          "Every day, billions of users chat over WhatsApp, execute banking transactions, and store credentials. "
          "Why can't eavesdroppers read this in transit? Because it is safeguarded by <b>applied mathematics and cryptography</b>! "
          "Today, we unpack <b>Symmetric (AES-256)</b> and <b>Asymmetric (RSA-2048)</b> ciphers, investigate the epic "
          "Sony PlayStation 3 cryptographic failure, and deploy our interactive <b>Crypto Studio</b> to exchange "
          "authenticated secret payloads!"),
    meta=[("<b>Fan:</b> Kiberxavfsizlik · Amaliy Kriptografiya",
           "<b>Предмет:</b> Кибербезопасность · Прикладная Криптография",
           "<b>Subject:</b> CyberSecurity · Applied Cryptography"),
          ("<b>Kohorta:</b> 10-11-sinf Kiber-Muhandis",
           "<b>Когорта:</b> 10-11 класс Инженер Безопасности",
           "<b>Cohort:</b> Grade 10-11 Security Engineer"),
          ("<b>Hafta:</b> 5 (1-soat)", "<b>Неделя:</b> 5 (1-й час)", "<b>Week:</b> 5 (Hour 1)")],
))

# 2. Encoding vs Encryption vs Hashing
S.append(slide(
    ph=("Asosiy Tushunchalar", "Базовые Понятия", "Core Concepts"), time="3–6",
    eyebrow=("Farqlarni bilish", "Три кита информации", "The Core Trifecta"),
    title=("Encoding vs Encryption vs Hashing: Eng Katta Xato!",
           "Encoding против Encryption против Hashing: Не Путать!",
           "Encoding vs Encryption vs Hashing: The Core Trifecta"),
    body='<div class="cols c3">\n'
         + box("", ("1. Encoding (Kodlash) 🔄", "1. Кодирование (Encoding) 🔄", "1. Encoding (Representation) 🔄"),
               p=("Faqat ma'lumot shaklini o'zgartirish (masalan: Base64, ASCII). <b>Maxfiylik yo'q!</b> Istalgan odam kalitsiz ochib o'qiydi.",
                  "Преобразование формата для удобной передачи (Base64, URL-encode). <b>Секретности нет!</b> Любой декодирует без пароля.",
                  "Byte formatting for transmission (Base64, ASCII). <b>Zero confidentiality!</b> Reversible by anyone without a key."))
         + box("purple", ("2. Hashing (Xeshlash) 🧬", "2. Хэширование (Hashing) 🧬", "2. Hashing (One-Way Digest) 🧬"),
               p=("Bir tomonlama matematik barmoq izi (SHA-256). Ortga qaytarib bo'lmaydi! <b>Parollar va yaxlitlikni tekshirish</b> uchun xizmat qiladi.",
                  "Односторонний математический отпечаток (SHA-256). Необратим! Применяется для <b>хранения паролей и проверки целостности</b>.",
                  "One-way deterministic fingerprint (SHA-256). Irreversible! Powers <b>password verification and integrity audits</b>."))
         + box("accent", ("3. Encryption (Shifrlash) 🔐", "3. Шифрование (Encryption) 🔐", "3. Encryption (Reversible with Key) 🔐"),
               p=("Matnni maxfiy kalit bilan qulflash. <b>Faqat to'g'ri kalit egasi</b> uni qaytadan ochib (decrypt) o'qiy oladi.",
                  "Двустороннее криптографическое преобразование. <b>Только владелец секретного ключа</b> может расшифровать исходный текст.",
                  "Two-way keyed transformation. <b>Exclusively decrypted</b> by authorized holders of the valid cryptographic key."))
         + '\n</div>'
))

# 3. Symmetric Encryption: AES-256
S.append(slide(
    ph=("Simmetrik Shifr", "Симметричный Шифр", "Symmetric Ciphers"), time="6–10",
    eyebrow=("AES-256 standarti", "Индустриальный стандарт", "Industry Standard"),
    title=("Simmetrik Shifrlash: AES-256 va GCM Yaxlitlik Qalqoni",
           "Симметричное Шифрование: Стандарт AES-256 и Режим GCM",
           "Symmetric Encryption: AES-256 and Authenticated GCM"),
    body='<div class="cols c2">\n'
         + box("accent", ("AES-256 Qanday Ishlaydi? 🛡️", "Принцип Работы AES-256 🛡️", "AES-256 Mechanics 🛡️"),
               items=[
                   ("<b>1 ta umumiy kalit:</b> Shifrlash uchun ham, ochish uchun ham bitta maxfiy 256-bitli kalit ishlatiladi.",
                    "<b>Один секретный ключ:</b> И для зашифровки, и для расшифровки используется один и тот же ключ 256 бит.",
                    "<b>Shared secret key:</b> The identical 256-bit key performs both encryption and decryption."),
                   ("<b>Super-Tezlik:</b> Kompyuter protsessori AES algoritmini apparat darajasida soniyasiga gigabaytlab tezlikda bajaradi.",
                    "<b>Молниеносная скорость:</b> Процессоры поддерживают инструкции AES-NI на аппаратном уровне (гигабайты в секунду).",
                    "<b>Hardware Acceleration:</b> Modern CPUs process AES instructions in silicon at multi-gigabit throughput."),
                   ("<b>GCM Rejimi (Auth Tag):</b> Nafaqat shifrlaydi, balki <b>yaxlitlik tegi</b> yaratadi. Agar xaker bitta baytni o'zgartirsa, tizim ochishdan bosh tortadi!",
                    "<b>Режим GCM (Auth Tag):</b> Не только шифрует, но и создаёт тег аутентичности. Подмена 1 бита сразу вызывает отказ!",
                    "<b>GCM Mode (Auth Tag):</b> Provides authenticated encryption. Modifying even 1 bit causes cryptographic rejection!"),
               ])
         + box("purple", ("Haqiqiy Misol: WhatsApp Chatlari 💬", "Живой Пример: Сквозное Шифрование WhatsApp 💬", "Real-World Context: WhatsApp End-to-End 💬"),
               items=[
                   ("Siz do'stingizga fotosurat yoki video yuborganingizda, u telefoningizda <b>AES-256</b> bilan shifrlanadi.",
                    "Когда вы отправляете фото другу в мессенджере, телефон шифрует медиафайл быстрым <b>AES-256</b>.",
                    "When sending media over WhatsApp or Signal, your device encrypts payloads via high-speed <b>AES-256</b>."),
                   ("WhatsApp serverlari faqat shifrlangan qora qutini ko'radi, uni ochish kaliti esa faqat do'stingizning telefonida bo'ladi!",
                    "Серверы мессенджера видят лишь зашифрованный шум — ключ есть только у получателя!",
                    "Intermediary servers only process opaque ciphertext — decryption keys reside strictly on endpoints!"),
               ])
         + '\n</div>'
))

# 4. Asymmetric Encryption: RSA
S.append(slide(
    ph=("Asimmetrik Shifr", "Асимметричный Шифр", "Asymmetric Ciphers"), time="10–14",
    eyebrow=("Ochiq kalitli shifrlash", "Ключевая пара", "Public-Key Cryptography"),
    title=("Asimmetrik Shifrlash: RSA-2048 va Pochta Qutisi Metaforasi",
           "Асимметричное Шифрование: RSA-2048 и Метафора Почтового Ящика",
           "Asymmetric Systems: RSA-2048 & The Postbox Analogy"),
    body='<div class="cols c2">\n'
         + box("purple", ("Pochta Qutisi Metaforasi 📬", "Метафора Почтового Ящика 📬", "The Postbox Analogy 📬"),
               p=("Ko'chadagi pochta qutisini tasavvur qiling: "
                  "Istalgan kishi kelib, qutining teshigidan ichkariga xat tashlay oladi — bu <b>Ochiq Kalit (Public Key)</b>.<br><br>"
                  "Lekin qutining orqa eshigini ochib, xatlarni olib o'qish uchun maxfiy temir kalit kerak — bu <b>Yopiq Kalit (Private Key)</b>!<br>"
                  "Yopiq kalit faqat pochtachida bo'ladi va uni hech kimga bermaydi.",
                  "Представьте уличный почтовый ящик: "
                  "Любой прохожий может бросить в прорезь письмо — это <b>Открытый Ключ (Public Key)</b>.<br><br>"
                  "Но открыть дверцу ящика и прочитать собранные письма может только почтальон своим секретным ключом — "
                  "это <b>Закрытый Ключ (Private Key)</b>!<br>"
                  "Закрытый ключ хранится в тайне и никогда не передаётся по сети.",
                  "Picture a public streetside postbox: "
                  "Any passerby can drop an envelope through the slot — this is the <b>Public Key</b>.<br><br>"
                  "However, retrieving and reading the letters requires the postmaster's private brass key — the <b>Private Key</b>!<br>"
                  "The private key remains strictly safeguarded and is never transmitted over the network."))
         + box("green", ("Nega Ikkala Kalit Birga Ishlaydi? 🔑", "Зачем Нужны Два Ключа? 🔑", "The Dual-Key Advantage 🔑"),
               items=[
                   ("<b>Ochiq Kalit (Public):</b> Siz uni butun dunyoga, internetga bemalol tarqatishingiz mumkin.",
                    "<b>Открытый Ключ:</b> Можно свободно публиковать в интернете и отправлять кому угодно.",
                    "<b>Public Key:</b> Published openly across the internet without any confidentiality hazard."),
                   ("<b>Yopiq Kalit (Private):</b> Faqat sizning kompyuteringizda qoladi. U hech qachon tarmoqqa chiqmaydi!",
                    "<b>Закрытый Ключ:</b> Хранится только на вашем компьютере и никогда не покидает его.",
                    "<b>Private Key:</b> Stored exclusively on your host workstation; never traverses the wire."),
                   ("<b>Matematik mo''jiza:</b> Ochiq kalit bilan shifrlangan xabarni hatto uni shifrlagan odamning o'zi ham ocha olmaydi! Faqat Yopiq kalit egasi ocha oladi.",
                    "<b>Крипто-магия:</b> Даже тот, кто зашифровал сообщение открытым ключом, не может прочитать его обратно без приватного ключа!",
                    "<b>Mathematical Trapdoor:</b> Even the sender who encrypted the payload cannot decrypt it back without the recipient's private key!"),
               ])
         + '\n</div>'
))

# 5. Hybrid Cryptography (TLS 1.3 / HTTPS)
S.append(slide(
    ph=("Gibrid Kripto", "Гибридный Шифр", "Hybrid Cryptography"), time="14–18",
    eyebrow=("Internet qanday ishlaydi?", "Как устроен HTTPS?", "The Engine of HTTPS"),
    title=("Gibrid Shifrlash: Nega Internetda Ikkalasi Birga Ishlaydi?",
           "Гибридная Криптография: Почему Они Работают в Паре?",
           "Hybrid Cryptography: The Perfect Partnership in HTTPS"),
    body='<div class="cols c2">\n'
         + box("accent", ("Dilemma: Qaysi Biri Yaxshiroq? 🤔", "Дилемма Скорости и Доставки 🤔", "The Speed vs Delivery Dilemma 🤔"),
               items=[
                   ("<b>AES (Simmetrik):</b> Juda tez, lekin bitta muammo — umumiy kalitni internet orqali xavfsiz qanday yetkazamiz?",
                    "<b>AES (Симметрия):</b> Невероятно быстр, но как передать общий секретный ключ через открытый интернет?",
                    "<b>AES (Symmetric):</b> Blazing fast, but how do we securely transmit the shared key across an untrusted network?"),
                   ("<b>RSA (Asimmetrik):</b> Kalit yetkazish xavfsiz, lekin juda og'ir va sekin. Katta video yoki fayllarni shifrlashga kuchi yetmaydi.",
                    "<b>RSA (Асимметрия):</b> Решает проблему передачи ключа, но работает в сотни раз медленнее и грузит процессор.",
                    "<b>RSA (Asymmetric):</b> Solves key distribution seamlessly, but executes orders of magnitude slower on bulk payloads."),
               ])
         + box("green", ("Gibrid Yechim (TLS 1.3 / HTTPS Qulfi) 🔒", "Гибридное Решение (TLS 1.3 / HTTPS) 🔒", "The Hybrid Masterstroke (TLS 1.3) 🔒"),
               p=("Internet muhandislari eng zo'r yechimni topishdi:<br><br>"
                  "1. Saytga kirganingizda, brauzer va server <b>RSA/ECC (Asimmetrik)</b> orqali bir soniyada bir martalik <b>AES kalitini</b> kelishib oladi.<br><br>"
                  "2. Kalit kelishilgach, butun veb-sahifa va videolar tezkor <b>AES-256</b> bilan shifrlanadi!<br><br>"
                  "Natija: <b>100% xavfsizlik + 100% yuqori tezlik!</b>",
                  "Инженеры нашли гениальное решение:<br><br>"
                  "1. Браузер и сервер через <b>RSA/ECC</b> безопасно передают временный <b>сессионный ключ AES</b>.<br><br>"
                  "2. Как только ключ получен, весь дальнейший трафик (видео, сайты) шифруется молниеносным <b>AES-256</b>!<br><br>"
                  "Итог: <b>Максимальная безопасность + Максимальная скорость!</b>",
                  "Engineers engineered the optimal synthesis:<br><br>"
                  "1. During the handshake, endpoints deploy <b>RSA/ECC</b> to securely negotiate an ephemeral <b>AES session key</b>.<br><br>"
                  "2. Once established, bulk traffic streams over hardware-accelerated <b>AES-256</b>!<br><br>"
                  "Result: <b>Unbreakable key distribution + Uncompromised wire speed!</b>"))
         + '\n</div>'
))

# 6. Case Study: Sony PS3 Epic Fail
S.append(slide(
    ph=("Tarixiy Keys", "Реальный Кейс", "Case Study"), time="18–22",
    eyebrow=("Tarixiy kripto-xato", "Эпический провал Sony", "Historic Security Flaw"),
    title=("Sony PlayStation 3 Xatosi: O'zgarmas 'Tasodifiy' Son Halokati",
           "Крипто-Катастрофа Sony PS3: Постоянное «Случайное» Число",
           "The Sony PlayStation 3 Cryptographic Disaster (2010)"),
    body='<div class="cols c2">\n'
         + box("accent", ("Sony Muhandislari Nima Xato Qilishgan? 🎮", "Что Сделали Инженеры Sony? 🎮", "The Developer Blunder 🎮"),
               items=[
                   ("Sony PS3 da o'yinlar faqat rasmiy raqamli imzo bilan ishlashi uchun <b>ECDSA</b> algoritmi o'rnatilgan edi.",
                    "В консоли PS3 для проверки подлинности игр применялся криптографический алгоритм подписи <b>ECDSA</b>.",
                    "Sony deployed <b>ECDSA</b> cryptographic signatures to restrict the PS3 solely to authentic licensed binaries."),
                   ("ECDSA qoidasiga ko'ra, har bir imzo uchun yangi tasodifiy son <code>k</code> (nonce) tanlanishi shart edi.",
                    "По стандарту для каждой подписи требовалось генерировать новое строго случайное число <code>k</code>.",
                    "The cryptographic specification mandated a fresh random nonce <code>k</code> for every single signature."),
                   ("Sony dasturchilari erinib, <code>k</code> sonini doimiy qilib (masalan: <code>const k = 42</code>) yozib qo'yishgan!",
                    "Инженеры Sony поленились и захардкодили постоянное число <code>k</code> в код прошивки!",
                    "Sony engineers lazily hardcoded <code>k</code> as a static constant across production builds!"),
               ])
         + box("purple", ("Xakerlarning G'alabasi: Bosh Kalit Fosh Bo'ldi! 💥", "Финал: Хакеры Вычислили Мастер-Ключ! 💥", "The Catastrophic Fallout 💥"),
               items=[
                   ("2010 yili <b>fail0verflow</b> xakerlar guruhi ikkita imzolangan o'yinni solishtirib, oddiy maktab algebra formulasi orqali Sony'ning <b>bosh maxfiy kalitini (Private Key)</b> hisoblab chiqardi!",
                    "В 2010 году хакеры сопоставили две подписанные игры и через простую алгебру вычислили закрытый <b>мастер-ключ Sony</b>!",
                    "In 2010, the <b>fail0verflow</b> team correlated two signed games and used simple school algebra to isolate Sony's root private key!"),
                   ("Butun dunyodagi PS3 konsollari bir kunda buzildi — xakerlar istalgan dasturni Sony nomidan imzolash imkoniga ega bo'ldi!",
                    "Консоль PS3 была взломана навсегда — злоумышленники получили возможность подписывать любые пиратские игры!",
                    "The PS3 was permanently jailbroken — anyone could mint custom binaries carrying Sony's authentic corporate signature!"),
               ])
         + '\n</div>'
))

# 7. 3 Implementation Sins
S.append(slide(
    ph=("Xatolar Tahlili", "Ошибки Разработки", "Implementation Sins"), time="22–26",
    eyebrow=("Xavfsizlik qoidalari", "3 фатальные ошибки", "Critical Rules"),
    title=("Kriptografiyada Dasturchilarning 3 Ta Halokatli Xatosi",
           "3 Фатальные Ошибки в Прикладной Криптографии",
           "The 3 Deadly Sins of Software Cryptography"),
    body='<div class="cols c3">\n'
         + box("accent", ("1. O'z Shifringni Yozish ❌", "1. Свой Самодельный Шифр ❌", "1. Rolling Custom Crypto ❌"),
               p=("<i>'Men o'zim yangi sirli algoritm o'ylab topdim'</i> — Kriptografiyaning 1-qoidasi: <b>O'z shifringizni o'ylab topmang!</b> Faqat dunyo tan olgan standartlardan foydalaning.",
                  "Никогда не изобретайте свои алгоритмы шифрования! Полагайтесь только на проверенные мировые библиотеки (`WebCrypto`, `OpenSSL`).",
                  "Never roll your own crypto algorithm! Rely exclusively on standardized, peer-reviewed primitives (`WebCrypto`, `OpenSSL`)."))
         + box("accent", ("2. IV / Nonce Takrorlash ❌", "2. Повторное Использование IV ❌", "2. Reusing Nonces / IVs ❌"),
               p=("AES-GCM shifrida bitta kalit bilan bir xil IV (Nonce) qayta ishlatilsa, xaker ikkala xabarni XOR qilib, <b>asl matnni o'qiy oladi!</b>",
                  "В режиме GCM повторное использование одного и того же IV позволяет злоумышленнику раскрыть открытый текст математически!",
                  "Reusing an IV/Nonce under the same AES-GCM key allows an adversary to XOR ciphertexts and recover plaintexts!"))
         + box("accent", ("3. Math.random() Ishlatish ❌", "3. Использование Math.random() ❌", "3. Insecure Randomness ❌"),
               p=("Oddiy <code>Math.random()</code> kalitlar uchun yaramaydi, chunki u oldindan aytish mumkin bo'lgan psevdo-son. Faqat <code>crypto.getRandomValues()</code> ishlatilishi shart!",
                  "Функция `Math.random()` предсказуема! Для ключей и токенов требуется криптографический генератор случайных чисел.",
                  "`Math.random()` is mathematically predictable! Cryptographic security strictly demands CSPRNG entropy generators."))
         + '\n</div>'
))

# 8. Interactive Studio Launch
S.append(slide(
    ph=("Amaliyot", "Интерактивная Лаборатория", "Interactive Studio"), time="26–38",
    eyebrow=("Jonli laboratoriya", "Crypto Studio", "Hands-on Playground"),
    title=("Crypto Studio & Cipher Playground: Amaliy Missiya!",
           "Crypto Studio: Ваша Интерактивная Миссия!",
           "Crypto Studio & Cipher Playground: Live Mission!"),
    body='<div class="cols c2">\n'
         + box("green", ("Bugungi Amaliy Topshiriqlar 🛠️", "Что Мы Будем Делать 🛠️", "Laboratory Mission Checkpoints 🛠️"),
               items=[
                   ("<b>1-Kvest:</b> 3-tabga o'ting, matndagi 1 ta harfni o'zgartirib <b>SHA-256 Ko'chki Samarasini</b> o'z ko'zingiz bilan ko'ring.",
                    "<b>Квест 1:</b> Перейдите на вкладку 3, измените 1 символ и увидьте лавинный эффект SHA-256.",
                    "<b>Quest 1:</b> Open Tab 3, mutate 1 letter, and observe the SHA-256 avalanche effect."),
                   ("<b>2-Kvest:</b> 1-tabda maxfiy xabar yozing va <b>AES-256-GCM</b> bilan shifrlang. Ciphertext va Auth Tag hosil bo'ladi.",
                    "<b>Квест 2:</b> На вкладке 1 зашифруйте текст через AES-256-GCM и получите тег целостности Auth Tag.",
                    "<b>Quest 2:</b> Encrypt plaintext on Tab 1 with AES-256-GCM and isolate the Auth Tag."),
                   ("<b>3-Kvest:</b> <b>'1 Baytni Buzish'</b> tugmasini bosing va qayta ochishga urining — GCM qanday qizil signal berishini sinang!",
                    "<b>Квест 3:</b> Нажмите «Подделать 1 Байт» и вызовите ошибку нарушения целостности Auth Tag!",
                    "<b>Quest 3:</b> Click 'Tamper 1 Byte' and observe the cryptographic integrity breach alarm!"),
                   ("<b>4-Kvest:</b> 2-tabda <b>RSA-2048</b> kalit juftligini yarating, ochiq kalit bilan shifrlab yopiq kalit bilan oching.",
                    "<b>Квест 4:</b> На вкладке 2 сгенерируйте пару RSA-2048, зашифруйте открытым ключом и расшифруйте закрытым.",
                    "<b>Quest 4:</b> Generate an RSA-2048 pair on Tab 2, encrypt with Public and decrypt with Private."),
               ])
         + box("purple", ("Qayerda Ishlaymiz? 💻", "Где Открыть Тренажёр? 💻", "Where to Work? 💻"),
               p=("Brauzeringizda <b>Crypto Studio</b> dasturini oching (yoki <code>studio/index.html</code> fayliga kiring).<br><br>"
                  "Hech qanday terminal yoki murakkab o'rnatish shart emas — butun kriptografiya to'g'ridan-to'g'ri brauzeringizda jonli ishlaydi!",
                  "Откройте на экране тренажёр <b>Crypto Studio</b> (файл <code>studio/index.html</code>).<br><br>"
                  "Никаких консольных команд и сложных настроек — алгоритмы WebCrypto работают прямо в браузере!",
                  "Open <b>Crypto Studio</b> in your browser (browse to <code>studio/index.html</code>).<br><br>"
                  "Zero terminal friction or command line errors — WebCrypto executes native hardware cryptography directly!"))
         + '\n</div>'
))

# 9. Verification Checklist
S.append(slide(
    ph=("Tekshirish", "Чек-лист Проверки", "Verification Gate"), time="38–41",
    eyebrow=("Kripto-audit", "Проверка знаний", "Audit Criteria"),
    title=("Kriptografik Nazorat Cheklisti: 4 Ta Asosiy Savol",
           "Криптографический Чек-лист: 4 Главных Вопроса",
           "Cryptographic Implementation Checklist: 4 Core Checks"),
    body='<div class="cols c2">\n'
         + box("green", ("O'zingizni Tekshiring 🔍", "Контрольные Вопросы 🔍", "Self-Assessment 🔍"),
               items=[
                   ("Nega Base64 kodlash shifrlash hisoblanmaydi?",
                    "Почему кодирование Base64 не обеспечивает конфиденциальность?",
                    "Why does Base64 encoding fail to deliver confidentiality?"),
                   ("AES-256 da 'Auth Tag' qanday qilib xakerlikni fosh qiladi?",
                    "Как Auth Tag в AES-GCM определяет подделку байтов?",
                    "How does the Auth Tag in AES-GCM detect malicious byte tampering?"),
                   ("Nega RSA da Ochiq kalitni hammaga bersa ham xavfsiz?",
                    "Почему открытый ключ RSA можно безопасно передавать кому угодно?",
                    "Why is public distribution of an RSA Public Key mathematically safe?"),
                   ("Sony PS3 muhandislari qaysi sonni o'zgarmas qilib qo'ygani uchun tizim buzildi?",
                    "Из-за какого статического числа взломали консоль Sony PS3?",
                    "Which static parameter caused the catastrophic Sony PS3 root key leak?"),
               ])
         + box("accent", ("Kutilgan Natija (Varaqaga Yozing) 📝", "Ожидаемый Результат 📝", "Expected Deliverables 📝"),
               items=[
                   ("1. SHA-256 dagi 64 belgili xesh natijasi.",
                    "1. Записанный хеш SHA-256 из 64 символов.",
                    "1. Documented 64-character SHA-256 digest."),
                   ("2. AES-256 shifrlangan HEX kodi va Auth Tag.",
                    "2. Зашифрованный HEX шифротекст и Auth Tag.",
                    "2. Documented AES-256 ciphertext HEX and Auth Tag."),
                   ("3. Tamper testi natijasida chiqqan xato matni.",
                    "3. Зафиксированная ошибка нарушения целостности.",
                    "3. Documented AEAD integrity error upon byte tampering."),
                   ("4. RSA ochilgan xabar.",
                    "4. Расшифрованное сообщение RSA.",
                    "4. Successfully recovered RSA message."),
               ])
         + '\n</div>'
))

# 10. Rubric (10-Ball)
S.append(slide(
    ph=("Mezon", "Критерии Оценки", "10-Point Rubric"), time="41–43",
    eyebrow=("10 ballik mezon", "10-балльная шкала", "Grading Criteria"),
    title=("Laboratoriya Baholash Mezoni (10 Ball)",
           "Критерии Оценки за Лабораторную (10 Баллов)",
           "Lesson Evaluation Rubric (10 Points)"),
    body='<div class="cols c3">\n'
         + box("green", ("A'lo (9–10 Ball) 🏆", "Отлично (9–10) 🏆", "Exemplary (9–10) 🏆"),
               items=[
                   ("Crypto Studio'dagi barcha 4 ta kvest bajarilgan.", "Все 4 квеста в Crypto Studio выполнены на 100%.", "All 4 Crypto Studio quests executed."),
                   ("Tamper testi orqali Auth Tag xatosi ko'rsatilgan.", "Показана ошибка целостности при атаке Tamper.", "Auth Tag integrity fault demonstrated."),
                   ("Varaqa to'liq va tushunarli to'ldirilgan.", "Рабочий лист аккуратно заполнен.", "Worksheet fully documented."),
               ])
         + box("", ("Yaxshi (7–8 Ball) 👍", "Хорошо (7–8) 👍", "Proficient (7–8) 👍"),
               items=[
                   ("AES va SHA-256 kvestlari bajarilgan, RSA qisman.", "AES и SHA-256 выполнены, RSA частично.", "AES & SHA-256 quests completed, RSA partial."),
                   ("Simmetrik va asimmetrik farqi tushuntirilgan.", "Разница симметрии и асимметрии усвоена.", "Symmetric vs asymmetric grasp demonstrated."),
                   ("Varaqa 80% to'ldirilgan.", "Рабочий лист заполнен на 80%.", "Worksheet completed to 80%."),
               ])
         + box("accent", ("Qoniqarli (5–6 Ball) ⚠️", "Удовл. (5–6) ⚠️", "Developing (5–6) ⚠️"),
               items=[
                   ("Faqat 1-2 ta kvest bajarilgan.", "Выполнено только 1-2 квеста.", "Only 1-2 quests completed."),
                   ("Auth Tag nima ekani tushunarsiz qolgan.", "Назначение Auth Tag не освоено.", "Auth Tag purpose misunderstood."),
                   ("Varaqa to'liq emas.", "Рабочий лист заполнен частично.", "Worksheet incomplete."),
               ])
         + '\n</div>'
))

# 11. Conclusion & Next Lesson
S.append(slide(
    ph=("Xulosa", "Итоги Урока", "Summary"), time="43–45",
    eyebrow=("Xulosa va ko'prik", "Итоги и мост", "Wrap-up & Bridge"),
    title=("Xulosa: Siz Kripto-Xavfsizlik Muhandisisiz!",
           "Итоги: Вы Освоили Основы Криптографии!",
           "Summary: You Mastered Core Applied Cryptography!"),
    body='<div class="cols c2">\n'
         + box("purple", ("Bugungi Yutuqlarimiz 🌟", "Главные Выводы 🌟", "Core Takeaways 🌟"),
               items=[
                   ("<b>AES-256:</b> Tezkor shifrlash va GCM yaxlitlik nazoratini o'rgandik.",
                    "<b>AES-256:</b> Освоили быстрый шифр и контроль целостности Auth Tag.",
                    "<b>AES-256:</b> Mastered bulk encryption and GCM authenticated integrity."),
                   ("<b>RSA-2048:</b> Ochiq va yopiq kalitlar orqali xavfsiz kalit almashishni tushundik.",
                    "<b>RSA-2048:</b> Поняли безопасный обмен секретами через пару ключей.",
                    "<b>RSA-2048:</b> Mastered secure key encapsulation via public/private pairs."),
                   ("<b>Kripto-Madaniyat:</b> Hech qachon o'z shifringizni o'ylab topmaslik va tasodifiy sonlarni to'g'ri tanlashni bildik.",
                    "<b>Культура безопасности:</b> Закрепили правило не создавать самодельные шифры.",
                    "<b>Hygiene:</b> Cemented the golden rule never to roll custom cryptographic primitives."),
               ])
         + box("accent", ("Keyingi 22-darsga Ko'prik 🚀", "Мост к Уроку 22 🚀", "Bridge to Lesson 22 🚀"),
               p=("Endi biz ma'lumotlarni shifrlashni bilamiz.<br><br>"
                  "Keyingi 22-darsda biz butun dunyo korporatsiyalari o'tayotgan <b>Zero Trust ('Hech kimga ishonma, doim tekshir')</b> "
                  "arxitekturasini va foydalanuvchilar ruxsatini boshqaruvchi <b>IAM (Identity and Access Management)</b> tizimini o'rganamiz!",
                  "Теперь мы умеем надежно защищать данные.<br><br>"
                  "На следующем 22-м уроке мы разберём современную модель безопасности <b>Zero Trust («Никому не доверяй, всегда проверяй»)</b> "
                  "и управление правами доступа <b>IAM (RBAC / ABAC)</b>!",
                  "Now we command the science of encrypting payloads.<br><br>"
                  "In Lesson 22, we advance to enterprise <b>Zero Trust (&quot;Never Trust, Always Verify&quot;)</b> architecture "
                  "and centralized <b>IAM access control (RBAC / ABAC)</b>!"))
         + '\n</div>'
))

# Teacher Notes
NOTES = {
    "uz": [
        ["Kirish", "O'quvchilarga xush kelibsiz deng. WhatsApp, bank ilovalari va parollar ortida turgan kriptografiya haqida aytib, motivatsiya bering.", "Dars mavzusini doskaga yozing va slaydni oching."],
        ["Asosiy Tushunchalar", "Encoding, Encryption va Hashing farqini tushuntiring. Base64 shifrlash emasligini, SHA-256 qaytmas barmoq izi ekanini ta'kidlang.", "O'quvchilardan misollar so'rang."],
        ["Simmetrik AES-256", "AES-256 simmetrik shifrlashini tushuntiring. GCM rejimidagi Auth Tag yaxlitlikni qanday himoya qilishini ayting.", "WhatsApp misolini keltiring."],
        ["Asimmetrik RSA", "Pochta qutisi metaforasi orqali Ochiq va Yopiq kalitlar qanday ishlashini tushuntiring.", "Nega ikkala kalit kerakligini savol-javob qiling."],
        ["Gibrid Kripto", "Dilemmani tushuntiring: AES tez lekin kalitni qanday uzatamiz? RSA xavfsiz lekin sekin. HTTPS ikkalasini qanday birlashtiradi.", "TLS 1.3 arxitekturasini doskaga chizing."],
        ["Sony PS3 Keysi", "Sony PS3 kiber-halokatini qiziqarli hikoya qilib bering. Dasturchilar tasodifiy sonni o'zgarmas qilgani uchun butun konsol buzilganini ayting.", "Kriptografiyada tasodifiylik qanchalik muhimligini ta'kidlang."],
        ["3 Ta Xato", "Dasturchilarning 3 ta xatosini aytib bering: o'z shifringni o'ylab topma, IV ni takrorlama, Math.random() ishlatma.", "O'quvchilarni ogohlantiring."],
        ["Crypto Studio Boshlanishi", "Barcha o'quvchilarni Crypto Studio (studio/index.html) ga yo'naltiring. 4 ta kvestni navbatma-navbat tushuntiring.", "O'quvchilarga 12 daqiqa amaliyot vaqti bering."],
        ["Tekshirish", "O'quvchilar ekranidagi natijalarni tekshiring. Tamper testida qizil xato chiqqanini ko'ring.", "Varaqadagi jadvallar to'ldirilayotganini nazorat qiling."],
        ["Baholash Mezoni", "10 ballik mezonni tushuntiring: 4 ta kvest to'liq bajarilsa 10 ball.", "Taymerni nazorat qiling."],
        ["Xulosa", "Darsni yakunlang. O'quvchilar bugun haqiqiy amaliy kriptografiyani o'zlashtirganlarini ta'kidlang va keyingi Zero Trust darsiga qiziqtiring.", "Varaqalarni yig'ib oling."]
    ],
    "ru": [
        ["Введение", "Поприветствуйте учеников. Объясните, что за шифрованием WhatsApp и банковских карт стоит строгая математика.", "Откройте титульный слайд и озвучьте тему."],
        ["Базовые Понятия", "Разграничьте Encoding, Encryption и Hashing. Докажите, что Base64 — это не защита, а SHA-256 необратим.", "Приведите примеры из жизни."],
        ["Симметричный AES-256", "Объясните работу AES-256 и роль Auth Tag в режиме GCM для предотвращения подделки байтов.", "Приведите в пример чаты WhatsApp."],
        ["Асимметричный RSA", "Объясните пару ключей через метафору почтового ящика: открытый ключ бросает письмо, закрытый достаёт.", "Задайте вопрос ученикам на понимание."],
        ["Гибридный Шифр", "Разберите дилемму: скорость AES против доставки RSA. Покажите, как HTTPS объединяет оба мира.", "Нарисуйте схему рукопожатия TLS 1.3."],
        ["Кейс Sony PS3", "Расскажите историю взлома PS3 из-за захардкоженного числа k. Покажите важность случайности в криптографии.", "Объясните алгебраический просчет Sony."],
        ["3 Ошибки", "Озвучьте 3 главных греха: самодельный шифр, повтор IV и вызов Math.random().", "Предостерегите будущих разработчиков."],
        ["Старт Crypto Studio", "Переведите класс в Crypto Studio (studio/index.html). Разъясните 4 квеста практикума.", "Выделите 12 минут на работу."],
        ["Контроль", "Проверьте экраны учеников: правильность генерации RSA и обнаружение ошибки при Tamper тесте.", "Следите за заполнением листа."],
        ["Критерии", "Напомните 10-балльную шкалу: по 2.5 балла за каждый успешно закрытый квест тренажёра.", "Контролируйте таймер."],
        ["Итоги", "Подведите итоги урока, похвалите класс и сделайте анонс следующего урока по Zero Trust и IAM.", "Соберите рабочие листы."]
    ],
    "en": [
        ["Intro", "Welcome students. Motivate them with the real-world mechanics protecting WhatsApp chats and banking payloads.", "Announce scope and display slide 1."],
        ["Core Concepts", "Dissect Encoding vs Encryption vs Hashing. Reiterate that Base64 lacks confidentiality and SHA-256 is irreversible.", "Engage class with quick examples."],
        ["Symmetric AES-256", "Explain AES-256-GCM and how authentication tags defeat adversary bit-flipping attacks.", "Contextualize using WhatsApp end-to-end."],
        ["Asymmetric RSA", "Deliver the postbox analogy: Public key drops mail, secret Private key opens the door.", "Prompt students on key pairs."],
        ["Hybrid Cryptography", "Address the dilemma: Fast AES vs safe key transport in RSA. Detail how TLS 1.3 combines both.", "Diagram TLS handshake on whiteboard."],
        ["Sony PS3 Flaw", "Narrate the PS3 root key catastrophe caused by a static nonce k constant.", "Emphasize entropy requirements."],
        ["Implementation Sins", "Highlight the 3 deadly sins: Custom ciphers, nonce reuse, and Math.random().", "Review secure coding rules."],
        ["Crypto Studio Launch", "Direct students to Crypto Studio (studio/index.html). Walk through the 4 hands-on quests.", "Allocate 12 minutes for lab execution."],
        ["Verification", "Inspect student screens: Confirm valid RSA key derivation and GCM integrity faults upon tampering.", "Supervise worksheet documentation."],
        ["Grading Rubric", "Review the 10-point rubric: 2.5 points per successfully solved studio quest.", "Track remaining time."],
        ["Wrap-up", "Summarize achievements. Commend students on mastering applied cryptography and bridge to Lesson 22 (Zero Trust).", "Collect completed worksheets."]
    ]
}

# ---------------------------------------------------------------- Worksheet (Varaqa)
V = []
V.append(sheet_header(
    h1=("Kiberxavfsizlik: Amaliy Kriptografiya (AES-256 & RSA)",
        "Кибербезопасность: Прикладная Криптография (AES-256 & RSA)",
        "CyberSecurity: Applied Cryptography (AES-256 & RSA)"),
    sub=("Amaliy Laboratoriya Varaqasi · 10–11-sinf · 5-hafta · 21-dars",
         "Практический Рабочий Лист · 10–11 класс · Неделя 5 · Урок 21",
         "Hands-On Lab Worksheet · Grades 10–11 · Week 5 · Lesson 21")
))

V.append(mission(
    h=("Laboratoriya Missiyasi: Crypto Studio Kvestlari va Yaxlitlik Testi",
       "Миссия Лабораторной: Квесты Crypto Studio и Контроль Целостности",
       "Lab Mission: Crypto Studio Milestones & Cryptographic Integrity Audit"),
    p=("Crypto Studio interaktiv laboratoriyasida SHA-256 ko'chki samarasini isbotlash, "
       "AES-256-GCM bilan matnni shifrlab bitta baytni buzish (Tamper) orqali Auth Tag xatosini chaqirish, "
       "hamda RSA-2048 kalit juftligi bilan maxfiy xat almashish.",
       "В тренажёре Crypto Studio подтвердить лавинный эффект SHA-256, "
       "зашифровать сообщение в AES-256-GCM и вызвать ошибку целостности через Tamper-атаку, "
       "а также сгенерировать пару RSA-2048 для защищённой переписки.",
       "Prove the SHA-256 avalanche effect in Crypto Studio, "
       "encrypt plaintext via authenticated AES-256-GCM and trigger an integrity breach via bit tampering, "
       "and derive an RSA-2048 keypair to execute asymmetric payload exchanges."))
)

V.append(table(
    headers=[
        ("Kvest / Bosqich", "Этап Квеста", "Quest Stage"),
        ("Kiritilgan / Generatsiya Qilingan Ma'lumot", "Данные / Входные Параметры", "Data / Input Parameters"),
        ("Kriptografik Natija (HEX / Xabar)", "Криптографический Результат", "Cryptographic Output"),
        ("Xulosa va Status", "Статус и Вывод", "Status & Conclusion")
    ],
    rows=[
        [("1. SHA-256 Ko'chki Samarasi", "1. Лавинный Эффект SHA-256", "1. SHA-256 Avalanche Proof"),
         ("`TargetSchool2026` vs `TargetSchool2027`", "«TargetSchool2026» vs «TargetSchool2027»", "'TargetSchool2026' vs 'TargetSchool2027'"),
         ("64 belgili xeshlar 50%+ farq qildi", "Хеши полностью отличаются", "Hashes differ by >50% bits"),
         ("✅ Isbotlandi (+2.5b)", "✅ Доказано (+2.5б)", "✅ Proven (+2.5pts)")],
        [("2. AES-256-GCM Shifrlash", "2. Шифрование AES-GCM", "2. AES-256-GCM Encryption"),
         ("Ochiq matn + 256-bitli tasodifiy kalit", "Открытый текст + ключ 256 бит", "Plaintext + 256-bit CSPRNG key"),
         ("Ciphertext HEX + 128-bit Auth Tag", "Шифротекст и Auth Tag", "Ciphertext HEX + 128-bit Auth Tag"),
         ("✅ Tayyor (+2.5b)", "✅ Готово (+2.5б)", "✅ Solved (+2.5pts)")],
        [("3. Tamper (Hujum) Testi", "3. Атака Подделки Байт", "3. Tamper Attack Test"),
         ("1 baytni ataylab o'zgartirish (XOR)", "Изменение 1 байта шифротекста", "Mutating 1 byte of ciphertext"),
         ("`INTEGRITY BREACH: Auth tag mismatch`", "Ошибка целостности GCM", "Integrity failure triggered"),
         ("✅ Fosh qilindi (+2.5b)", "✅ Разоблачено (+2.5б)", "✅ Caught (+2.5pts)")],
        [("4. RSA-2048 Maxfiy Xat", "4. Секретное Сообщение RSA", "4. RSA Secret Message"),
         ("Public Key (Ochiq) + Private Key (Yopiq)", "Пара ключей RSA-2048", "RSA-2048 Keypair"),
         ("Ochiq kalit shifrladi, Yopiq kalit ochdi", "Успешная расшифровка закрытым ключом", "Decrypted via Private Key"),
         ("✅ Yakunlandi (+2.5b)", "✅ Завершено (+2.5б)", "✅ Completed (+2.5pts)")]
    ]
))

V.append(sheet_box(
    h=("Kiber-Ekspert Savollari va Tahliliy Xulosalar", "Вопросы Кибер-Эксперта и Анализ", "Forensic Cryptography Analysis"),
    body_html=writelines(3, label=("1. Nega AES-256 da 'Auth Tag' (yaxlitlik tegi) bo'lmasa, xaker shifrlangan xabarni buzib o'zgartirishi xavfli?",
                                   "1. Почему без тега Auth Tag в AES злоумышленник может незаметно изменить зашифрованные данные?",
                                   "1. Why does an absent Auth Tag allow an adversary to tamper with encrypted payloads undetected?"))
             + "<br>"
             + writelines(2, label=("2. Sony PS3 muhandislari qaysi tasodifiy sonni o'zgarmas qilib qo'yganliklari sababli bosh kalit fosh bo'ldi?",
                                   "2. Какую ошибку с параметром k допустили инженеры Sony PlayStation 3, приведшую к утечке мастер-ключа?",
                                   "2. Which fatal static nonce k flaw caused the complete compromise of Sony PS3 root private keys?"))
))

V.append(sheet_box(
    h=("Baholash Mezoni (10 Ball)", "Критерии Оценки (10 Баллов)", "Grading Rubric (10 Points)"),
    body_html=rubric([
        (("Crypto Studio'dagi 4 ta amaliy kvest natijalari qayd etilgan", "Все 4 квеста Crypto Studio выполнены и зафиксированы", "All 4 Crypto Studio quest proofs recorded"), "4 ball"),
        (("Simmetrik (AES) va Asimmetrik (RSA) ishlash prinsiplari asoslangan", "Принципы симметричного и асимметричного шифрования обоснованы", "Symmetric and asymmetric cryptographic mechanics justified"), "3 ball"),
        (("Auth Tag yaxlitligi va Sony PS3 xatosi tahlili to'g'ri yozilgan", "Разбор роли Auth Tag и ошибки Sony PS3 дан верно", "Auth Tag integrity analysis and Sony PS3 case study articulated"), "3 ball"),
    ], "10 ball")
))

V.append("</div>\n" + sign_box("Musulmonov Mamarajab"))

VARAQA_BODY = "\n".join(V)

lesson = Lesson(
    outdir=D,
    titles=TITLES,
    sheet_titles=SHEET_TITLES,
    key="vc-notes-10-21",
    slides=S,
    notes=NOTES,
    varaqa_body=VARAQA_BODY
)

if __name__ == "__main__":
    out = lesson.build()
    print("Created:", out)
