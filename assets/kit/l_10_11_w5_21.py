# -*- coding: utf-8 -*-
"""10-11-sinf · 5-hafta · 21-dars — Kriptografiya Asoslari: Simmetrik va Asimmetrik Shifrlash (AES-256, RSA & ECC)."""

import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from build import (Lesson, slide, title_slide, box, code, el, i18n,
                   sheet_header, mission, table, sheet_box, rubric, writelines, sign_box)

D = "classes/10-11-sinf/5-hafta/21-dars-kriptografiya-aes-va-rsa"

TITLES = {
    "uz": "21-dars: Kriptografiya Asoslari — AES-256, RSA va ECC Shifrlash",
    "ru": "Урок 21: Основы Криптографии — Шифрование AES-256, RSA и ECC",
    "en": "Lesson 21: Foundations of Cryptography — AES-256, RSA & ECC Protocols",
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
    h1=("Kriptografiya Asoslari: AES, RSA va ECC",
        "Основы Криптографии: AES-256, RSA и ECC",
        "Foundations of Cryptography: AES, RSA & ECC"),
    lede=("Zamonaviy raqamli sivilizatsiya — bank o'tkazmalari, harbiy aloqa, kriptovalyutalar va maxfiy ma'lumotlar — "
          "faqatgina qonunlar bilan emas, balki buzib bo'lmas <b>matematik qonuniyatlar</b> bilan himoyalangan. "
          "Dunyoning barcha superkompyuterlari birlashsa ham, to'g'ri shifrlangan 256-bitli kalitni sindirish uchun "
          "Koinot yoshidan ko'proq vaqt talab etiladi. Bugungi darsda siz <b>Simmetrik (AES-256)</b> va "
          "<b>Asimmetrik (RSA, Elliptik egri chiziqlar ECC)</b> shifrlash mexanizmlarini, "
          "Diffie-Hellman kalit almashinuvini va Kvant kompyuterlari tahdidini o'rganasiz.",
          "Цифровая цивилизация — банковские транзакции, гостайна, мессенджеры и облачные хранилища — "
          "держится на фундаменте <b>математической криптографии</b>. "
          "Даже всем суперкомпьютерам планеты понадобятся миллиарды лет для взлома ключа AES-256. "
          "Сегодня вы разберёте <b>симметричное шифрование (AES)</b>, <b>асимметричные криптосистемы (RSA, ECC)</b>, "
          "протокол обмена ключами Диффи-Хеллмана и угрозу квантовых вычислений.",
          "Modern digital civilization — interbank settlements, classified defense communications, and cloud ecosystems — "
          "is secured not by policy, but by unyielding <b>mathematical hardness assumptions</b>. "
          "Even if every planetary supercomputer executed in parallel, brute-forcing a 256-bit key would outlast the cosmos. "
          "Today you will master <b>Symmetric Ciphers (AES-256-GCM)</b>, <b>Asymmetric Keypairs (RSA-4096 & ECC)</b>, "
          "Diffie-Hellman key exchange mechanics, and post-quantum threat vectors."),
    meta=[("<b>Fan:</b> Kiberxavfsizlik · Amaliy Kriptografiya",
           "<b>Предмет:</b> Кибербезопасность · Прикладная Криптография",
           "<b>Subject:</b> CyberSecurity · Applied Cryptography"),
          ("<b>Kohorta:</b> 10-11-sinf Kiber-Muhandis",
           "<b>Когорта:</b> 10-11 класс Инженер Безопасности",
           "<b>Cohort:</b> Grade 10-11 Security Engineer"),
          ("<b>Hafta:</b> 5 (1-soat)", "<b>Неделя:</b> 5 (1-й час)", "<b>Week:</b> 5 (Hour 1)")],
))

# 2. Hard Math: Hashing vs Encryption vs Encoding
S.append(slide(
    ph=("Nazariya", "Теория", "Theory"), time="3–6",
    eyebrow=("Terminologik aniqlik", "Терминологическая строгость", "Mathematical Rigor"),
    title=("Encoding vs Encryption vs Hashing: Farqni Biling!",
           "Encoding против Encryption против Hashing: Не Путать!",
           "Encoding vs Encryption vs Hashing: The Core Trifecta"),
    body='<div class="cols c3">\n'
         + box("", ("1. Encoding (Kodlash)", "1. Кодирование (Encoding)", "1. Encoding (Representation)"),
               p=("Ma'lumot formatini o'zgartirish (masalan, Base64, ASCII, URL encode). <b>Maxfiylik yo'q!</b> Istalgan kishi kalitsiz ochib o'qiy oladi.",
                  "Преобразование байт для удобной передачи (Base64, URL-encode). <b>Секретности нет!</b> Любой декодирует без ключа.",
                  "Reformatting bytes for transmission (Base64, ASCII). <b>Zero confidentiality!</b> Reversible by anyone without credentials."))
         + box("purple", ("2. Hashing (Xeshlash)", "2. Хэширование (Hashing)", "2. Hashing (One-Way Digest)"),
               p=("Bir tomonlama matematik funksiya (SHA-256, bcrypt). Ortga qaytarib bo'lmaydi! <b>Parollar va yaxlitlikni tekshirish</b> uchun ishlatiladi.",
                  "Односторонняя функция фиксированной длины (SHA-256). Необратима! Применяется для <b>паролей и проверки целостности</b>.",
                  "Irreversible deterministic one-way mathematical function (SHA-256, Argon2). Used for <b>passwords and integrity digests</b>."))
         + box("accent", ("3. Encryption (Shifrlash)", "3. Шифрование (Encryption)", "3. Encryption (Reversible with Key)"),
               p=("Matnni maxfiy kalit bilan shifrga (ciphertext) aylantirish. <b>Faqat to'g'ri kalit egasi</b> uni qaytadan ochib (decrypt) o'qiy oladi.",
                  "Двустороннее криптографическое преобразование. <b>Только владелец секретного ключа</b> может расшифровать исходный текст.",
                  "Two-way cryptographic transformation. <b>Exclusively decrypted</b> by authorized holders of the valid secret key."))
         + '\n</div>'
))

# 3. Symmetric Encryption: AES-256
S.append(slide(
    ph=("AES-256", "AES-256", "Symmetric AES"), time="6–10",
    eyebrow=("Sanoat standarti", "Индустриальный стандарт", "Industry Standard"),
    title=("Simmetrik Shifrlash: AES-256 (Advanced Encryption Standard)",
           "Симметричное Шифрование: Стандарт AES-256",
           "Symmetric Encryption: AES-256-GCM in Production"),
    body='<div class="cols c2">\n'
         + box("accent", ("AES-256 Qanday Ishlaydi?", "Принцип Работы AES-256", "AES-256 Mechanics"),
               items=[
                   ("<b>1 ta umumiy kalit:</b> Shifrlash uchun ham, qayta ochish uchun ham bitta maxfiy kalit (256-bit) ishlatiladi.",
                    "<b>Один секретный ключ:</b> И для зашифровки, и для расшифровки используется одинаковый ключ 256 бит.",
                    "<b>Shared secret key:</b> The identical 256-bit key executes both encryption and decryption."),
                   ("<b>Blokli shifr:</b> Ma'lumotlar 128-bitli (16 bayt) bloklarga bo'linadi va 14 raund matematik almashtirishdan (SubBytes, ShiftRows, MixColumns) o'tadi.",
                    "<b>Блочный шифр:</b> Данные делятся на блоки по 128 бит и проходят 14 раундов крипто-перестановок.",
                    "<b>Block cipher:</b> Data streams segment into 128-bit blocks, processed across 14 rounds of substitution/permutation."),
                   ("<b>GCM Rejimi (Galois/Counter Mode):</b> Shifrlash bilan birga <b>yaxlitlikni tasdiqlovchi Auth Tag</b> beradi.",
                    "<b>Режим GCM:</b> Одновременно обеспечивает конфиденциальность и аутентичность (Auth Tag).",
                    "<b>AEAD Mode (GCM):</b> Simultaneously guarantees confidentiality and cryptographic integrity (Auth Tag)."),
               ])
         + '<div class="box green">\n'
         + el("h3", "Node.js Crypto: AES-256-GCM Shifrlash", "Код Шифрования AES-256", "Node.js AES-256-GCM Implementation")
         + code("""import crypto from 'crypto';

const key = crypto.randomBytes(32); // 256-bitli kalit
const iv = crypto.randomBytes(12);  // 96-bitli Nonce (Initialization Vector)

const cipher = crypto.createCipheriv('aes-256-gcm', key, iv);
let encrypted = cipher.update('Maxfiy Hujjat: Top Secret', 'utf8', 'hex');
encrypted += cipher.final('hex');

const authTag = cipher.getAuthTag(); // Yaxlitlik tegi
// Natija: encrypted + iv + authTag saqlanadi""")
         + '</div>\n</div>'
))

# 4. Asymmetric Encryption: RSA & ECC
S.append(slide(
    ph=("Asimmetrik", "Асимметрия", "Asymmetric Crypto"), time="10–14",
    eyebrow=("Ochiq kalitli kriptografiya", "Криптография с открытым ключом", "Public-Key Cryptography"),
    title=("Asimmetrik Shifrlash: RSA va Elliptik Egri Chiziqlar (ECC)",
           "Асимметричное Шифрование: RSA и Эллиптические Кривые (ECC)",
           "Asymmetric Systems: RSA-4096 vs Elliptic Curve Cryptography (ECC)"),
    body='<div class="cols c2">\n'
         + box("purple", ("RSA-4096 (Katta Tub Sonlar)", "RSA-4096 (Простые Числа)", "RSA-4096 (Prime Factorization)"),
               items=[
                   ("<b>Matematik asosi:</b> Ikki ulkan tub sonni (prime numbers) bir-biriga ko'paytirish oson, lekin hosil bo'lgan 1200 xonali sonni ko'paytuvchilarga ajratish <b>(faktoring)</b> imkonsiz.",
                    "<b>Математика:</b> Перемножить два огромных простых числа легко, но разложить факторизацией 1200-значное число невозможно.",
                    "<b>Mathematical Trapdoor:</b> Multiplying two prime numbers is trivial; factoring their product is computationally infeasible."),
                   ("<b>Kamchiligi:</b> Kalit hajmi juda katta (4096 bit) va protsessorni ko'p yuklaydi.",
                    "<b>Минус:</b> Огромный размер ключа (4096 бит) и высокая нагрузка на процессор.",
                    "<b>Drawback:</b> Massive key length (4096 bits) and heavy computational overhead."),
               ])
         + box("green", ("ECC / Ed25519 (Elliptik Egri Chiziqlar)", "ECC / Ed25519 (Эллиптические Кривые)", "ECC / Ed25519 (Discrete Logarithm)"),
               items=[
                   ("<b>Matematik asosi:</b> <code>y^2 = x^3 + ax + b</code> egri chizig'idagi nuqtalarni ko'paytirish diskret logarifm muammosiga asoslanadi.",
                    "<b>Математика:</b> Задача дискретного логарифма на группе точек эллиптической кривой.",
                    "<b>Mathematical Trapdoor:</b> Elliptic curve discrete logarithm problem (ECDLP)."),
                   ("<b>Katta ustunlik:</b> <b>256-bitli ECC kaliti</b> 3072-bitli RSA kaliti bilan teng kuchga ega, lekin <b>10 baravar tezroq</b> va yengil!",
                    "<b>Преимущество:</b> Ключ ECC 256 бит равен по стойкости RSA 3072 бит, но в 10 раз быстрее!",
                    "<b>Supreme Efficiency:</b> 256-bit ECC key matches 3072-bit RSA security at 10x compute throughput!"),
               ])
         + '\n</div>'
))

# 5. Hybrid Cryptography: The TLS 1.3 Handshake
S.append(slide(
    ph=("Gibrid Shifr", "Гибридный Шифр", "Hybrid Cryptography"), time="14–18",
    eyebrow=("Internet qanday ishlaydi?", "Как устроен TLS?", "The Engine of the Internet"),
    title=("Gibrid Kriptografiya: Nega Internetda Ikkala Shifr Birga Ishlatiladi?",
           "Гибридная Криптография: Почему Они Работают в Паре?",
           "Hybrid Cryptography: Orchestrating Asymmetric & Symmetric Ciphers"),
    body='<div class="cols c2">\n'
         + box("", ("Dilemma: Asimmetrik sekin, Simmetrik kalitini qanday uzatamiz?", "Дилемма Скорости и Доставки", "The Cryptographic Dilemma"),
               items=[
                   ("<b>Simmetrik (AES):</b> O'ta tezkor (gigabitlab trafikni shifrlaydi), lekin kalitni begona ko'rmasdan qanday yetkazamiz?",
                    "<b>AES:</b> Невероятно быстр, но как передать общий ключ через враждебную сеть?",
                    "<b>Symmetric (AES):</b> Hardware-accelerated and lightning fast, but key distribution over open networks is hazardous."),
                   ("<b>Asimmetrik (RSA/ECC):</b> Kalit almashish xavfsiz, lekin butun videoni shifrlashga juda sekin.",
                    "<b>Асимметрия:</b> Безопасный обмен, но шифровать большие файлы процессорно дорого.",
                    "<b>Asymmetric:</b> Flawless key exchange, but far too computationally intensive for bulk payload streaming."),
               ])
         + '<div class="box accent">\n'
         + el("h3", "Gibrid Yechim (TLS 1.3 / HTTPS)", "Гибридное Решение (TLS 1.3)", "The Hybrid Handshake Solution") + "\n"
         + el("p", "1. Brauzer va server <b>Diffie-Hellman / ECC</b> yordamida ochiq tarmoqda bir martalik <b>Session Key (AES-256)</b> kelishib oladi.<br><br>"
              "2. Kalit o'rnatilgach, butun veb-trafik <b>AES-256</b> bilan ultra-tezkor shifrlanadi.<br><br>"
              "3. Har bir yangi ulanish uchun yangi kalit yaratiladi (<b>Forward Secrecy</b>)!",
              "1. Браузер и сервер через протокол Диффи-Хеллмана на кривых (ECDH) генерируют общий сессионный ключ AES.<br><br>"
              "2. Основной трафик шифруется супербыстрым AES-256.<br><br>"
              "3. Для каждой сессии генерируется уникальный ключ (Forward Secrecy).",
              "1. Browser and server negotiate an ephemeral AES-256 session key via Elliptic Curve Diffie-Hellman (ECDH).<br><br>"
              "2. Bulk data stream is encrypted via ultra-fast AES-256-GCM.<br><br>"
              "3. Ephemeral keys ensure Forward Secrecy: compromising one key never decrypts past traffic.") + "\n"
         + '</div>\n</div>'
))

# 6. Post-Quantum Cryptography (PQC)
S.append(slide(
    ph=("Kvant Xavfi", "Квантовая Угроза", "Post-Quantum"), time="18–22",
    eyebrow=("Yaqin kelajak tahdidi", "Угроза квантовых ЭВМ", "Quantum Computing Threat"),
    title=("Kvant Tahdidi: Shor Algoritmi va Post-Kvant Kriptografiyasi",
           "Квантовая Угроза: Алгоритм Шора и Пост-Квантовая Защита",
           "The Quantum Threat: Shor's Algorithm & Post-Quantum Cryptography"),
    body='<div class="cols c2">\n'
         + box("accent", ("Kvant Kompyuter Nimalarni Buzadi?", "Что Сломает Квантовый Компьютер?", "What Quantum Breaks"),
               items=[
                   ("<b>Shor Algoritmi:</b> Kvant kompyuterlar tub sonlarga ajratish va diskret logarifmni bir necha soniyada yechadi.",
                    "<b>Алгоритм Шора:</b> Квантовый компьютер взломает RSA и ECC за секунды полиномиальным алгоритмом.",
                    "<b>Shor's Algorithm:</b> Solves prime factorization and discrete logarithms in polynomial time, breaking RSA and ECC."),
                   ("<b>RSA va ECC o'ladi:</b> Kvant davri kelganda barcha hozirgi ochiq kalitli tizimlar yaroqsiz bo'ladi.",
                    "<b>Конец RSA и ECC:</b> Все асимметричные шифры станут уязвимыми при появлении мощных квантовых процессоров.",
                    "<b>RSA & ECC rendered obsolete:</b> Every classical asymmetric scheme will collapse once fault-tolerant quantum hardware arrives."),
                   ("<b>AES-256 omon qoladi:</b> Grover algoritmi simmetrik kalit kuchini 256 dan 128 ga tushiradi (lekin 128 hali ham buzib bo'lmas darajada kuchli).",
                    "<b>AES-256 устоит:</b> Алгоритм Гровера снижает стойкость вдвое (до 128 бит), что по-прежнему безопасно.",
                    "<b>AES-256 survives:</b> Grover's algorithm reduces effective strength to 128 bits, which remains computationally unbreachable."),
               ])
         + box("green", ("Yangi Standart: NIST PQC (Lattice-Based)", "Новый Стандарт NIST PQC", "NIST Post-Quantum Standards"),
               items=[
                   ("<b>Panjarali Kriptografiya (Lattices):</b> Ko'p o'lchovli panjara fazosidagi matematik masalalar kvant kompyuterlar uchun ham yechib bo'lmas darajada murakkab.",
                    "<b>Решёточная криптография:</b> Математические задачи на многомерных решётках не под силу квантовым алгоритмам.",
                    "<b>Lattice Cryptography:</b> High-dimensional Euclidean lattice geometries defeat quantum speedups."),
                   ("<b>Yangi standartlar (2024):</b> NIST <b>ML-KEM (Kyber)</b> kalit almashish va <b>ML-DSA (Dilithium)</b> raqamli imzo standartlarini qabul qildi.",
                    "<b>Новые стандарты NIST (2024):</b> Алгоритмы ML-KEM (Kyber) и ML-DSA (Dilithium).",
                    "<b>Official NIST Standards (2024):</b> ML-KEM (Kyber) for encryption and ML-DSA (Dilithium) for digital signatures."),
               ])
         + '\n</div>'
))

# 7. Code Dissection: Cryptographic Implementation
S.append(slide(
    ph=("Kod Tahlili", "Анализ Кода", "Code Dissection"), time="22–26",
    eyebrow=("Xavfsiz amaliyot", "Безопасная реализация", "Cryptographic API Dissection"),
    title=("Kriptografiyada 3 Ta Halokatli Xato",
           "3 Фатальные Ошибки в Прикладной Криптографии",
           "The 3 Catastrophic Implementation Sins"),
    body='<div class="cols c3">\n'
         + box("accent", ("1. O'z Shifringni Yozish", "1. Свой Самодельный Шифр", "1. Rolling Custom Crypto"),
               p=("<i>\"Men o'zim yangi algoritm o'ylab topdim!\"</i> — Kriptografiyaning 1-qoidasi: <b>Hech qachon o'zingiz yangi shifr yozmang!</b> Faqat tekshirilgan standart kutubxonalardan foydalaning.",
                  "Никогда не изобретайте свои шифры! Используйте только проверенные библиотеки (`libsodium`, `node:crypto`).",
                  "Never roll your own crypto! Obscurity is not security. Rely strictly on peer-reviewed standards (`libsodium`, `WebCrypto`)."))
         + box("accent", ("2. IV / Nonce Qayta Ishlatish", "2. Повторное Использование IV", "2. Reusing Nonces / IVs"),
               p=("GCM rejimida bir xil kalit bilan bir xil IV (Nonce) ishlatilsa, xaker ikkala shifrlangan matnni XOR qilib, <b>ochiq matnni va kalitni fosh qila oladi!</b>",
                  "В режиме GCM повтор IV для одного ключа позволяет математически раскрыть открытый текст!",
                  "Reusing a nonce under the same AES-GCM key allows attackers to XOR ciphertexts and recover plaintext instantly."))
         + box("accent", ("3. Math.random() Ishlatish", "3. Math.random() в Криптографии", "3. Insecure Randomness"),
               p=("Parol yoki kalit yaratishda <code>Math.random()</code> ishlatish halokatdir. U psevdo-tasodifiy. Faqat <code>crypto.randomBytes()</code> ishlatilishi shart!",
                  "`Math.random()` предсказуем! Для ключей и токенов используйте криптографический генератор `crypto.randomBytes()`.",
                  "`Math.random()` is PRNG deterministic. Cryptographic randomness demands CSPRNG entropy (`crypto.randomBytes`)."))
         + '\n</div>'
))

# 8. Real-World Case Study: Sony PS3 Epic Fail
S.append(slide(
    ph=("Real Keys", "Кейс из Жизни", "Case Study"), time="26–30",
    eyebrow=("Tarixiy kripto-halokat", "Эпический провал Sony", "Historic Crypto Flaw"),
    title=("Sony PlayStation 3 Kripto-Halokati: O'zgarmas 'Tasodifiy' Son",
           "Крипто-Катастрофа Sony PS3: Постоянное 'Случайное' Число",
           "The Sony PlayStation 3 Cryptographic Disaster: Hardcoded Randomness"),
    body='<div class="cols c2">\n'
         + box("accent", ("Sony Dasturchilari Nima Qilgan?", "Что Сделали Инженеры Sony?", "What Sony Did"),
               p=("Sony PS3 da o'yinlar faqat rasmiy imzo bilan ishlashi uchun <b>ECDSA (Elliptic Curve Digital Signature)</b> ishlatilgan. ECDSA matematikasida har bir imzo uchun mutlaqo yangi tasodifiy son <code>k</code> (nonce) tanlanishi shart. Ammo Sony dasturchilari <code>k</code> sonini o'zgarmas qilib (hardcoded constant) yozib qo'ygan!",
                  "В консоли PS3 для подписи игр применялся алгоритм ECDSA. По стандарту параметр `k` должен быть строго случайным для каждой подписи. Инженеры Sony захардкодили постоянное число `k`!",
                  "Sony enforced ECDSA signatures to prevent piracy on the PS3. The ECDSA specification strictly mandates a unique random nonce `k` per signature. Sony developers hardcoded `k` as a static constant across all builds!"))
         + box("purple", ("Halokatli Oqibat", "Катастрофический Финал", "Catastrophic Impact"),
               items=[
                   ("<b>Xususiy kalit fosh bo'ldi:</b> Xakerlar ikkita imzoni solishtirib, oddiy maktab algebra formulasi bilan Sony'ning <b>bosh maxfiy kalitini (Private Key)</b> hisoblab chiqardi!",
                    "<b>Утечка мастер-ключа:</b> Хакеры через школьную алгебру вычислили закрытый мастер-ключ Sony!",
                    "<b>Master private key exfiltrated:</b> Researchers used elementary algebra across two signed games to extract Sony's root private key!"),
                   ("<b>Butun tizim yiqildi:</b> Xakerlar o'z o'yinlarini Sony nomidan imzolash imkoniyatiga ega bo'ldi. Konsolni yangilash bilan ham buni tuzatib bo'lmasdi!",
                    "<b>Фатальный взлом:</b> Консоль была взломана навсегда, исправить это обновлениями было невозможно.",
                    "<b>Irreversible jailbreak:</b> Anyone could sign custom software as authentic Sony binaries; unpatchable without revoking hardware."),
               ])
         + '\n</div>'
))

# 9. Practical Mission (12 min timer)
S.append(slide(
    ph=("Amaliyot", "Практика", "Hands-On Lab"), time="30–42",
    eyebrow=("Mustaqil laboratoriya · 12 daqiqa", "Лабораторная работа · 12 минут", "Crypto Lab · 12 Minutes"),
    title=("Amaliy Topshiriq: AES-256 Shifrlash va RSA Kalit Almashinuvi",
           "Практическое Задание: Шифрование AES-256 и RSA",
           "Mission: Implementing AES-256-GCM & RSA-4096 Key Exchange"),
    body='<div class="cols c2">\n'
         + box("green", ("Laboratoriya Bosqichlari", "Шаги Лабораторной", "Mission Checkpoints"),
               items=[
                   ("<b>1. AES-256-GCM Shifrlash:</b> Node.js skripti orqali xabarni shifrlang, IV va Auth Tag ni ajrating.",
                    "<b>1. Шифрование AES-256:</b> Зашифруйте строку с генерацией IV и Auth Tag.",
                    "<b>1. Encrypt with AES-256:</b> Encrypt payload using authenticated AES-GCM cipher."),
                   ("<b>2. Tamper Testi (Yaxlitlik sinovi):</b> Shifrlangan matnning bitta baytini o'zgartiring va `authTag` xato berishini tekshiring.",
                    "<b>2. Проверка Auth Tag:</b> Измените 1 байт в шифротексте и убедитесь в отказе расшифровки.",
                    "<b>2. Tamper verification:</b> Mutate 1 byte of ciphertext and verify GCM authentication failure."),
                   ("<b>3. RSA Kalit Juftligi:</b> `openssl genpkey -algorithm RSA -pkeyopt rsa_keygen_bits:4096` orqali kalit juftligini hosil qiling.",
                    "<b>3. Генерация RSA-4096:</b> Создайте пару ключей через OpenSSL.",
                    "<b>3. Generate RSA-4096:</b> Mint a 4096-bit RSA keypair via OpenSSL."),
                   ("<b>4. Gibrid Shifrlash:</b> AES kalitini RSA ochiq kaliti bilan shifrlab ko'ring.",
                    "<b>4. Гибридный тест:</b> Зашифруйте ключ AES публичным ключом RSA.",
                    "<b>4. Hybrid encapsulation:</b> Encrypt the symmetric AES key using recipient's RSA public key."),
               ])
         + box("accent", ("O'lchanadigan Natija", "Критерий Сдачи", "Deliverable Spec"),
               p=("Shifrlangan fayl to'g'ri kalit bilan muvaffaqiyatli ochilishi, o'zgartirilgan bayt esa <b>\"Unsupported state or unable to authenticate data\"</b> xatosi bilan yaxlitlikni himoya qilgani isbotlanishi shart!",
                  "Успешная расшифровка исходного сообщения и гарантированный отказ при попытке подделки байтов Auth Tag!",
                  "Flawless decryption of authentic payloads and immediate cryptographic rejection upon single-bit tampering!"))
         + '\n</div>'
))

# 10. Verification Checklist
S.append(slide(
    ph=("Tekshirish", "Чек-лист", "Verification"), time="42–43",
    eyebrow=("Kripto-audit", "Проверка реализации", "Cryptographic Audit"),
    title=("Kriptografik Nazorat Cheklisti: 5 Ta Oltin Qoida",
           "Чек-лист Криптографии: 5 Золотых Правил",
           "Cryptographic Implementation Quality Gates"),
    body='<div class="cols c3">\n'
         + box("", ("1. Tasodifiy IV / Nonce", "1. Уникальный IV", "1. Unique Nonce"),
               p=("Har bir shifrlash amali uchun yangi `crypto.randomBytes(12)` yaratildimi?",
                  "Генерируется ли свежий IV для каждого вызова шифрования?",
                  "Is a fresh 96-bit nonce minted for every single encryption call?"))
         + box("", ("2. Auth Tag Tekshiruvi", "2. Проверка Auth Tag", "2. Auth Tag Verification"),
               p=("GCM rejimida yaxlitlik tegi `cipher.getAuthTag()` bilan saqlandimi?",
                  "Сохранён и проверен ли аутентификационный тег `authTag`?",
                  "Is the GCM authentication tag explicitly retrieved and validated?"))
         + box("", ("3. Kalit O'lchami", "3. Размер Ключа", "3. Key Entropy"),
               p=("AES uchun aniq 256-bit (32 bayt), RSA uchun kamida 4096-bit tanlandimi?",
                  "Использованы ли надежные длины: AES 256 бит, RSA от 4096 бит?",
                  "Are enterprise key lengths strictly enforced (AES-256, RSA-4096)?"))
         + '\n</div>'
))

# 11. Rubric (10-Ball)
S.append(slide(
    ph=("Mezon", "Критерии", "Evaluation"), time="43–44",
    eyebrow=("10 ballik mezon", "10-балльная шкала", "10-Point Rubric"),
    title=("Darsni Baholash Mezonlari (10 Ball)",
           "Критерии Оценки за Урок (10 Баллов)",
           "Lesson Evaluation Rubric (10 Points)"),
    body='<div class="cols c3">\n'
         + box("green", ("A'lo (9–10 Ball)", "Отлично (9–10)", "Exemplary (9–10)"),
               items=[
                   ("AES-256-GCM kodi xatosiz yozilgan va tushuntirilgan.", "Код AES-256-GCM реализован и объяснен.", "AES-256-GCM implementation flawless."),
                   ("Auth Tag orqali yaxlitlik tekshiruvi namoyish etilgan.", "Проверка целостности через Auth Tag показана.", "Auth Tag integrity verification proven."),
                   ("Sony PS3 keysi va PQC tushunchalari asoslangan.", "Кейс Sony PS3 и основы PQC разобраны.", "Sony PS3 incident & PQC concepts analyzed."),
                   ("Varaqa 100% to'ldirilgan.", "Рабочий лист заполнен на 100%.", "Worksheet completed 100%."),
               ])
         + box("", ("Yaxshi (7–8 Ball)", "Хорошо (7–8)", "Proficient (7–8)"),
               items=[
                   ("AES kodi ishlaydi, lekin Auth Tag tahlili qisman.", "Шифрование работает, но анализ Auth Tag неполный.", "AES works, Auth Tag analysis incomplete."),
                   ("Simmetrik va asimmetrik farqi tushunilgan.", "Разница симметрии и асимметрии усвоена.", "Symmetric vs asymmetric differences grasped."),
                   ("Varaqa 80% to'ldirilgan.", "Лист заполнен на 80%.", "Worksheet completed 80%."),
               ])
         + box("accent", ("Qoniqarli (5–6 Ball)", "Удовл. (5–6)", "Developing (5–6)"),
               items=[
                   ("Faqat nazariy tushunchalar yozilgan, kod ishlamagan.", "Только теория, практический код с ошибками.", "Theory answered, code failed to execute."),
                   ("IV va Nonce vazifasi tushunarsiz qolgan.", "Назначение IV не понято.", "Purpose of IV/Nonce misunderstood."),
                   ("Varaqa to'liq emas.", "Лист заполнен частично.", "Worksheet incomplete."),
               ])
         + '\n</div>'
))

# 12. Summary & Homework
S.append(slide(
    ph=("Xulosa", "Итоги", "Summary"), time="44–45",
    eyebrow=("Uyga vazifa", "Домашнее задание", "Homework & Next Steps"),
    title=("Xulosa va Uy Vazifasi: Kriptografik Madaniyat",
           "Итоги и Домашнее Задание: Криптографическая Культура",
           "Summary & Homework: Enterprise Cryptographic Hygiene"),
    body='<div class="cols c2">\n'
         + box("purple", ("Dars Xulosasi", "Итоги Урока", "Core Summary"),
               p=("Kriptografiya — zamonaviy IT muhandisining eng kuchli quroli. Shifrlash faqat maxfiylik emas, balki yaxlitlik (Integrity) va haqiqiylik (Authenticity) kafolatidir. Hech qachon o'z algoritmingizni o'ylab topmang va tasodifiy sonlar entropiyasiga qat'iy e'tibor bering.",
                  "Криптография — главное оружие инженера. Шифрование гарантирует не только тайну, но и целостность данных. Никогда не создавайте самодельные шифры и следите за энтропией ключей.",
                  "Cryptography is the ultimate shield of software engineering. It guarantees not just confidentiality, but immutable integrity and non-repudiation. Never invent custom algorithms and enforce strict entropy."))
         + box("accent", ("Uy Vazifasi (10 Ball)", "Домашнее Задание (10 Баллов)", "Homework Assignment (10 Pts)"),
               items=[
                   ("<b>OpenSSL:</b> Terminalda `openssl rand -hex 32` orqali 256-bitli kalit yarating va bitta faylni AES-256-CBC bilan shifrlab ko'ring.",
                    "<b>OpenSSL:</b> Сгенерируйте ключ 256 бит через OpenSSL и зашифруйте текстовый файл.",
                    "<b>OpenSSL:</b> Generate a 256-bit key via `openssl rand -hex 32` and encrypt a test document."),
                   ("<b>Tahlil:</b> Post-Kvant davrida RSA nima uchun buziladi va NIST qanday yangi algoritmlarni standartlashtirganini 1 sahifa yozing.",
                    "<b>Анализ:</b> Опишите алгоритм Шора и почему алгоритм Kyber (ML-KEM) устойчив к квантовым компьютерам.",
                    "<b>Written Analysis:</b> Write a 1-page paper on Shor's algorithm and NIST's new ML-KEM standard."),
                   ("<b>Varaqa:</b> Ish varaqasidagi barcha masalalarni yakunlab topshiring.",
                    "<b>Лист:</b> Заполните печатный рабочий лист.",
                    "<b>Worksheet:</b> Complete and submit your printable lab worksheet."),
               ])
         + '\n</div>'
))

# Teacher Notes
N_UZ = [
    ["Kirish", "Darsni boshlash: Kriptografiya — zamonaviy kiberxavfsizlikning matematik asosi.", "Slaydni oching, superkompyuterlar ham 256-bitli kalit oldida ojiz ekanini ta'kidlang."],
    ["Nazariya", "Encoding, Encryption va Hashing farqi. Nega Base64 shifrlash emas?", "O'quvchilar ko'p adashtiradigan bu uch tushunchani doskada aniq ajrating."],
    ["AES-256", "Simmetrik shifrlash: AES-256 va GCM rejimi. Auth Tag yaxlitlikni qanday himoya qiladi.", "Node.js dagi crypto kodini tushuntiring."],
    ["Asimmetrik", "RSA va ECC (Elliptik egri chiziqlar). Nega ECC 10 baravar tez va yengil?", "Katta tub sonlarni ko'paytirish va diskret logarifm masalalarini sodda tushuntiring."],
    ["Gibrid Shifr", "Gibrid kriptografiya: TLS 1.3 HTTPS qanday ishlashi. Diffie-Hellman kalit almashinuvi.", "Dilemma va uning yechimini doskaga chizing."],
    ["Kvant Xavfi", "Kvant kompyuterlar xavfi. Shor algoritmi RSA ni qanday o'ldiradi?", "NIST yangi qabul qilgan Kyber va Dilithium algoritmlarini tanishtiring."],
    ["Kod Tahlili", "Kriptografiyada 3 ta xato: o'z shifringni yozish, IV ni takrorlash, Math.random() ishlatish.", "Xavfsizlik qoidalarini ta'kidlang."],
    ["Real Keys", "Sony PlayStation 3 kiber-halokati. O'zgarmas 'k' soni tufayli butun konsolning buzilishi.", "Sony dasturchilarining xatosini hikoya qilib bering."],
    ["Amaliyot", "12 daqiqalik laboratoriya. O'quvchilar AES-256 bilan fayl shifrlab, Auth Tag ni tekshiradilar.", "Taymerni yoqing (12 daqiqa), o'quvchilarga yordam bering."],
    ["Tekshirish", "Nazorat tekshiruvi. Yaxlitlik buzilganda dastur xato berishi kerak.", "Natijalarni tekshiring."],
    ["Mezon", "10 ballik baholash mezoni tushuntiriladi.", "Baholash shartlarini eslating."],
    ["Xulosa", "Dars yakuni va uy vazifasi. Kelgusi darsda Zero Trust arxitekturasi va IAM ni o'rganamiz.", "Varaqalarni yig'ing."]
]

N_RU = [
    ["Введение", "Старт урока: Криптография как математический фундамент кибербезопасности.", "Откройте слайд, подчеркните вычислительную стойкость 256-битных ключей."],
    ["Теория", "Разница Encoding, Encryption и Hashing. Почему Base64 — это не шифрование.", "Чётко разграничьте понятия обратимости и односторонности."],
    ["AES-256", "Симметричное шифрование: блочный шифр AES-256 и режим GCM.", "Объясните назначение вектора инициализации IV и тега аутентичности Auth Tag."],
    ["Асимметрия", "RSA против эллиптических кривых ECC. Преимущество коротких ключей Ed25519.", "Сравните производительность RSA-4096 и ECC-256."],
    ["Гибридный Шифр", "Гибридная криптография в TLS 1.3: синтез асимметрии и симметрии.", "Объясните протокол Диффи-Хеллмана и Forward Secrecy."],
    ["Квантовая Угроза", "Угроза квантовых ЭВМ: алгоритм Шора и разрушение RSA.", "Расскажите о новых постквантовых стандартах NIST (Kyber)."],
    ["Анализ Кода", "3 фатальные ошибки: самодельный шифр, повтор IV и Math.random().", "Предостерегите от типичных ошибок начинающих разработчиков."],
    ["Кейс из Жизни", "Взлом Sony PS3: статичный nonce `k` в ECDSA и утечка мастер-ключа.", "Разберите алгебраическую ошибку инженеров Sony."],
    ["Практика", "12 минут практики: шифрование AES-256-GCM и генерация RSA через OpenSSL.", "Запустите таймер, проверяйте корректность вызова crypto."],
    ["Проверка", "Чек-лист проверки: демонстрация сбоя дешифровки при подмене байтов.", "Проверьте экраны учеников."],
    ["Критерии", "10-балльная шкала оценивания практической работы.", "Озвучьте правила начисления баллов."],
    ["Итоги", "Завершение урока и домашнее задание. На следующем занятии изучим модель Zero Trust и IAM.", "Соберите рабочие листы."]
]

N_EN = [
    ["Intro", "Lesson opening: Applied cryptography as the mathematical bedrock of cyberspace.", "Introduce computational hardness assumptions."],
    ["Theory", "Differentiating Encoding, Encryption, and Hashing with absolute precision.", "Dissect one-way functions vs two-way keyed ciphers."],
    ["Symmetric AES", "Symmetric block ciphers: AES-256-GCM authenticated encryption.", "Explain initialization vector (IV) entropy and GCM authentication tags."],
    ["Asymmetric Crypto", "RSA-4096 vs Elliptic Curve Cryptography (ECC). Why ECC achieves parity at a fraction of the cost.", "Compare prime factorization to elliptic curve discrete logarithms."],
    ["Hybrid Cryptography", "Hybrid encryption in TLS 1.3: ECDH key exchange feeding bulk AES-GCM.", "Diagram session key negotiation on whiteboard."],
    ["Post-Quantum", "The post-quantum landscape: Shor's algorithm breaking RSA/ECC.", "Introduce NIST's standardized lattice schemes (ML-KEM/Kyber)."],
    ["Code Dissection", "The 3 implementation sins: Rolling custom crypto, nonce reuse, and Math.random().", "Review secure CSPRNG standards."],
    ["Case Study", "The Sony PS3 disaster: Hardcoded ECDSA nonce `k` exposing private root keys.", "Demonstrate the fatal algebraic vulnerability."],
    ["Crypto Lab", "12-minute lab: Implementing AES-256-GCM and testing auth tag tampering.", "Start 12-minute countdown timer and provide code assistance."],
    ["Verification", "Cryptographic verification checklist: Confirming tamper detection.", "Review student console exceptions."],
    ["Evaluation", "10-point evaluation rubric breakdown.", "Review grading thresholds."],
    ["Summary", "Wrap-up and homework preview. Next session: Zero Trust architecture and IAM governance.", "Collect worksheets."]
]

NOTES = {"uz": N_UZ, "ru": N_RU, "en": N_EN}

# ---------------------------------------------------------------- Varaqa Body
V = []
V.append(sheet_header(
    h1=("Kiberxavfsizlik: Amaliy Kriptografiya (AES & RSA)",
        "Кибербезопасность: Прикладная Криптография (AES & RSA)",
        "CyberSecurity: Applied Cryptography (AES & RSA)"),
    sub=("Amaliy Laboratoriya Varaqasi · 10–11-sinf · 5-hafta · 21-dars",
         "Практический Рабочий Лист · 10–11 класс · Неделя 5 · Урок 21",
         "Hands-On Lab Worksheet · Grades 10–11 · Week 5 · Lesson 21")
))

V.append(mission(
    h=("Laboratoriya Vazifasi: AES-256 Shifrlash va Yaxlitlik Testi",
       "Миссия Лабораторной: Шифрование AES-256 и Проверка Целостности",
       "Lab Mission: AES-256-GCM Encryption & Cryptographic Integrity Testing"),
    p=("Node.js crypto kutubxonasida AES-256-GCM algoritmi bilan matnni shifrlash, "
       "IV va Auth Tag ni ajratish, hamda shifrlangan baytlarni ataylab o'zgartirib yaxlitlik tekshiruvini sinash.",
       "Реализовать шифрование AES-256-GCM в Node.js, извлечь IV и Auth Tag, "
       "и проверить работу криптографического контроля целостности при модификации байт.",
       "Implement AES-256-GCM encryption in Node.js, isolate nonce IV and Auth Tag, "
       "and verify authenticated cipher tamper detection by mutating ciphertext bytes."))
)

V.append(table(
    headers=[
        ("Kriptografik Bosqich", "Этап Криптографии", "Cryptographic Phase"),
        ("Dastur Kodi / Buyruq", "Код / Команда", "Code / Command"),
        ("Kutilgan Natija", "Ожидаемый Результат", "Expected Outcome"),
        ("Holat", "Статус", "Status")
    ],
    rows=[
        [("1. Kalit Generatsiya", "1. Генерация Ключа", "1. Key Derivation"),
         ("`crypto.randomBytes(32)`", "`crypto.randomBytes(32)`", "`crypto.randomBytes(32)`"),
         ("256-bitli yuqori entropiyali kalit", "256-битный крипто-ключ", "256-bit CSPRNG key generated"),
         ("✅ Tayyor", "✅ Готово", "✅ Ready")],
        [("2. AES-GCM Shifrlash", "2. AES-GCM Шифр", "2. AES-GCM Cipher"),
         ("`createCipheriv('aes-256-gcm', k, iv)`", "`createCipheriv('aes-256-gcm', k, iv)`", "`createCipheriv('aes-256-gcm', k, iv)`"),
         ("Ciphertext + Auth Tag yaratildi", "Получены шифротекст и Auth Tag", "Ciphertext + Auth Tag produced"),
         None],
        [("3. Tamper Test (Buzish)", "3. Тест Подделки", "3. Tamper Verification"),
         ("`enc[0] = enc[0] === 'a' ? 'b' : 'a'`", "Модификация 1 байта шифротекста", "Mutate 1 byte in hex ciphertext"),
         ("`Unsupported state` xatosi (Rad etildi)", "Ошибка: Данные подделаны!", "Authentication error: Tamper detected"),
         None],
        [("4. RSA OpenSSL", "4. Ключи OpenSSL", "4. OpenSSL RSA-4096"),
         ("`openssl genpkey -algorithm RSA`", "`openssl genpkey -algorithm RSA`", "`openssl genpkey -algorithm RSA`"),
         ("4096-bitli asimmetrik kalit juftligi", "Пара ключей RSA 4096 бит", "4096-bit RSA asymmetric keypair"),
         None],
    ]
))

V.append(sheet_box(
    h=("Kriptografik Tahlil va Nazariy Savollar", "Криптографический Анализ и Вопросы", "Cryptographic Analysis & Written Queries"),
    body_html=writelines(3, label=("1. Nega GCM rejimida bir xil kalit bilan bir xil IV (Nonce) ni qayta ishlatish butun shifrlash tizimini fosh qiladi?",
                                   "1. Почему повторное использование IV с тем же ключом в режиме GCM разрушает безопасность шифра?",
                                   "1. Why is reusing an IV/Nonce under the same AES-GCM key fatal to cryptographic confidentiality?"))
             + "<br>"
             + writelines(3, label=("2. Kvant kompyuterlari chiqqanda Shor algoritmi nega RSA va ECC ni yo'q qiladi, lekin AES-256 omon qoladi?",
                                   "2. Почему алгоритм Шора на квантовых ЭВМ ломает RSA и ECC, но AES-256 остаётся безопасным?",
                                   "2. Why does Shor's algorithm dismantle RSA & ECC while AES-256 survives quantum advances?"))
))

V.append(sheet_box(
    h=("Baholash Mezoni (10 Ball)", "Критерии Оценки (10 Баллов)", "Grading Rubric (10 Points)"),
    body_html=rubric([
        (("AES-256-GCM shifrlash va ochish kodi to'g'ri yozilgan", "Шифрование и дешифрование AES-GCM реализованы", "AES-256-GCM encryption & decryption implemented"), "3 ball"),
        (("Auth Tag orqali yaxlitlik buzilishi amalda isbotlangan", "Продемонстрирован отказ при подмене байта Auth Tag", "Tamper detection via Auth Tag proven"), "3 ball"),
        (("Sony PS3 xatosi va PQC asoslari to'g'ri tahlil qilingan", "Разобраны кейс Sony PS3 и концепция PQC", "Sony PS3 incident and PQC concepts analyzed"), "2 ball"),
        (("Nazariy savollarga to'liq va asosli javob berilgan", "Даны развернутые ответы на теоретические вопросы", "Written analytical queries thoroughly answered"), "2 ball"),
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
