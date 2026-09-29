# -*- coding: utf-8 -*-
"""10-11-sinf · 5-hafta · 22-dars — Zero Trust va IAM Arxitekturasi: 'Hech Kimga Ishonma, Doim Tekshir' Tamoyili."""

import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from build import (Lesson, slide, title_slide, box, code, el, i18n,
                   sheet_header, mission, table, sheet_box, rubric, writelines, sign_box)

D = "classes/10-11-sinf/5-hafta/22-dars-zero-trust-va-iam-arxitekturasi"

TITLES = {
    "uz": "22-dars: Zero Trust va IAM Arxitekturasi — Korporativ Ruxsat Nazorati",
    "ru": "Урок 22: Архитектура Zero Trust и IAM — Контроль Корпоративного Доступа",
    "en": "Lesson 22: Zero Trust Architecture & Enterprise IAM — Identity Governance",
}
SHEET_TITLES = {k: v + (" — Ish Varaqasi" if k == "uz" else
                        " — Рабочий Лист" if k == "ru" else " — Worksheet")
                for k, v in TITLES.items()}

S = []

# 1. Title Slide
S.append(title_slide(
    ph=("Kirish", "Введение", "Intro"), time="0–3",
    eyebrow=("CyberSecurity · 22-dars · 10–11-sinf (Enterprise Architecture)",
             "CyberSecurity · Урок 22 · 10–11 класс (Enterprise Architecture)",
             "CyberSecurity · Lesson 22 · Grades 10–11 (Enterprise Architecture)"),
    h1=("Zero Trust va IAM Arxitekturasi",
        "Архитектура Zero Trust и Управление Доступом (IAM)",
        "Zero Trust Architecture & Enterprise IAM"),
    lede=("Eski kiberxavfsizlik modeli qasr va xandakka (Castle-and-Moat) o'xshardi: tashqaridan devor bilan o'ralgan, "
          "lekin bir marta ichkariga kirib olgan har kim barcha serverlarga to'liq kirish huquqiga ega bo'lardi. "
          "Bugungi bulutli va masofaviy dunyoda bu model o'ldi. Uning o'rniga <b>NIST SP 800-207</b> standarti — "
          "<b>Zero Trust (\"Hech kimga ishonma, doim tekshir\")</b> arxitekturasi keldi. "
          "Bugun siz <b>IAM (Identity and Access Management)</b>, <b>RBAC vs ABAC</b> granular ruxsatlar mantiqini, "
          "mikro-segmentatsiyani va <b>Minimal Huquq (Least Privilege)</b> tamoyilini o'rganasiz.",
          "Классическая безопасность напоминала замок со рвом: защита по периметру, "
          "но внутри сети любой узел считался доверенным. В облачную эпоху этот подход смертелен. "
          "Ему на смену пришёл стандарт <b>NIST SP 800-207 — Zero Trust («Никому не доверяй, всегда проверяй»)</b>. "
          "Сегодня вы разберёте системы <b>IAM</b>, разницу политик <b>RBAC и ABAC</b>, "
          "микросегментацию сетей и принцип наименьших привилегий (Least Privilege).",
          "Traditional perimeter security operated like a medieval castle and moat: hardened borders, "
          "yet implicitly trusting all internal traffic once breached. In modern distributed cloud infrastructures, this model is bankrupt. "
          "It has been replaced by <b>NIST SP 800-207: Zero Trust (\"Never Trust, Always Verify\")</b>. "
          "Today you will master enterprise <b>IAM governance</b>, compare <b>RBAC vs dynamic ABAC</b>, "
          "implement micro-segmentation, and enforce the <b>Principle of Least Privilege (PoLP)</b>."),
    meta=[("<b>Fan:</b> Kiberxavfsizlik · Enterprise Architecture",
           "<b>Предмет:</b> Кибербезопасность · Корпоративная Архитектура",
           "<b>Subject:</b> CyberSecurity · Enterprise Architecture"),
          ("<b>Kohorta:</b> 10-11-sinf Kiber-Muhandis",
           "<b>Когорта:</b> 10-11 класс Инженер Безопасности",
           "<b>Cohort:</b> Grade 10-11 Security Engineer"),
          ("<b>Hafta:</b> 5 (2-soat)", "<b>Неделя:</b> 5 (2-й час)", "<b>Week:</b> 5 (Hour 2)")],
))

# 2. Paradigm Shift: Castle-and-Moat vs Zero Trust
S.append(slide(
    ph=("Paradigma", "Парадигма", "Paradigm Shift"), time="3–6",
    eyebrow=("Arxitektura inqilobi", "Архитектурная революция", "Architectural Evolution"),
    title=("Perimetr Mudofaasi O'ldi: Nega Qasr Modeli Barham Topdi?",
           "Периметр Мёртв: Почему Рухнула Модель «Замка со Рвом»?",
           "The Death of the Perimeter: Why Castle-and-Moat Failed"),
    body='<div class="cols c2">\n'
         + box("accent", ("1. Eski Model: Castle-and-Moat (Perimetr)", "1. Старая Модель: Периметр", "1. Legacy Castle-and-Moat"),
               items=[
                   ("<b>VPN ichidagi ishonch:</b> Bir marta korporativ VPN ga ulangan xodim butun ichki tarmoqqa to'liq ishonchli deb qaralgan.",
                    "<b>Доверие внутри VPN:</b> Подключившись к корпоративной сети, пользователь получал доступ ко всем ресурсам.",
                    "<b>Implicit trust:</b> Connecting to corporate VPN implicitly granted blanket access to intranet subnets."),
                   ("<b>Lateral Movement (Yonlama siljish):</b> Xaker bitta buxgalter noutbukini buzsa, butun server xonasiga erkin kirib borgan.",
                    "<b>Боковое перемещение:</b> Взлом одного ноутбука позволял свободно атаковать сервера баз данных.",
                    "<b>Unrestricted lateral movement:</b> Compromising an endpoint allowed pivoting freely across database clusters."),
               ])
         + box("green", ("2. Yangi Model: Zero Trust (NIST SP 800-207)", "2. Новая Модель: Zero Trust", "2. Zero Trust (NIST SP 800-207)"),
               items=[
                   ("<b>Ichki va tashqi tarmoq teng:</b> Ofis ichidagi noutbuk ham, internetdagi notanish qurilma ham bir xil dushman deb hisoblanadi.",
                    "<b>Периметра больше нет:</b> Компьютер в офисе считается столь же потенциально опасным, как сервер в интернете.",
                    "<b>Zero implicit trust:</b> Devices on internal corporate LAN are treated as hostile as nodes on the public internet."),
                   ("<b>Har bir so'rov tekshiriladi:</b> Har bir API chaqiruvi, ma'lumotlar bazasi so'rovi qaytadan autentifikatsiya qilinadi.",
                    "<b>Каждый запрос верифицируется:</b> Доступ даётся к конкретному сервису, а не ко всей сети.",
                    "<b>Continuous verification:</b> Every single API transaction is dynamically authenticated and authorized."),
                   ("<b>Mikro-segmentatsiya:</b> Serverlar bir-biri bilan faqat shifrlangan mTLS va qat'iy firewall orqali gaplashadi.",
                    "<b>Микросегментация:</b> Сети разбиты на изолированные зоны с взаимным шифрованием mTLS.",
                    "<b>Micro-segmentation:</b> Microservices communicate strictly via mutual TLS (mTLS) with zero implicit visibility."),
               ])
         + '\n</div>'
))

# 3. The 3 Pillars of Zero Trust
S.append(slide(
    ph=("Asosiy Ustunlar", "Столпы Zero Trust", "Core Pillars"), time="6–10",
    eyebrow=("NIST SP 800-207", "NIST SP 800-207", "NIST SP 800-207"),
    title=("Zero Trust ning 3 Ta Asosiy Qoidasi",
           "3 Фундаментальных Принципа Zero Trust",
           "The 3 Foundational Tenets of Zero Trust"),
    body='<div class="cols c3">\n'
         + box("accent", ("1. Verify Explicitly (Aniq Tasdiqla)", "1. Явная Проверка (Verify Explicitly)", "1. Verify Explicitly"),
               p=("Doim barcha mavjud signallarni tekshirish: shaxs (identifikator), joylashuv, qurilma holati, xizmat turi, anomaliyalar va xavf darajasi.",
                  "Всегда проверять контекст: личность, геолокацию, здоровье устройства, прошивку, аномалии поведения.",
                  "Continuously evaluate all contextual signals: user identity, geolocation, endpoint posture, and anomaly scores."))
         + box("purple", ("2. Least Privilege (Minimal Huquq)", "2. Минимум Прав (Least Privilege)", "2. Use Least-Privilege Access"),
               p=("Foydalanuvchiga faqat ayni daqiqadagi topshiriq uchun zarur bo'lgan minimal huquq beriladi. Just-In-Time (JIT) va Just-Enough-Access (JEA).",
                  "Ограничение доступа ровно тем минимумом, который нужен для текущей задачи, и строго на ограниченное время.",
                  "Limit user access with Just-In-Time (JIT) and Just-Enough-Access (JEA) constraints, closing permissions immediately."))
         + box("green", ("3. Assume Breach (Buzilgan deb hisobla)", "3. Допущение Взлома (Assume Breach)", "3. Assume Breach"),
               p=("Tizim allaqachon xakerlar tomonidan buzilgan deb harakat qilish. Ma'lumotlarni shifrlash, loglarni kuzatish va tarmoqni mikro-zonalarga ajratish.",
                  "Действовать так, будто злоумышленник уже внутри периметра. Тотальное шифрование и непрерывный аудит.",
                  "Operate under the assumption that adversaries already reside inside the network. Encrypt all traffic and log all interactions."))
         + '\n</div>'
))

# 4. Access Control: RBAC vs ABAC
S.append(slide(
    ph=("Ruxsat Nazorati", "Контроль Доступа", "Access Control"), time="10–14",
    eyebrow=("Ruxsat modellari", "Модели авторизации", "Authorization Models"),
    title=("RBAC vs ABAC: Statik Rollardan Dinamik Atributlarga",
           "RBAC против ABAC: От Статических Ролей к Динамике",
           "RBAC vs ABAC: Transitioning from Static Roles to Dynamic Attributes"),
    body='<div class="cols c2">\n'
         + box("", ("RBAC (Role-Based Access Control)", "RBAC (На Основе Ролей)", "RBAC (Role-Based)"),
               items=[
                   ("<b>Mantiq:</b> Foydalanuvchiga bitta rol biriktiriladi (masalan, <code>Admin</code>, <code>Editor</code>, <code>Viewer</code>).",
                    "<b>Логика:</b> Права привязаны к роли пользователя (Admin, Editor, Viewer).",
                    "<b>Mechanism:</b> Permissions map to coarse static roles (Admin, Editor, Viewer)."),
                   ("<b>Kamchiligi: Role Explosion!</b> Katta korxonalarda <i>'Kechasi ishlaydigan Londonlik moliya tahrirchisi'</i> kabi yuzlab sun'iy rollar paydo bo'ladi.",
                    "<b>Минус: Взрыв ролей (Role Explosion).</b> Появление сотен узких ролей под каждого сотрудника.",
                    "<b>Fatal flaw: Role Explosion.</b> Enterprise systems end up with thousands of redundant, overlapping roles."),
               ])
         + box("accent", ("ABAC (Attribute-Based Access Control)", "ABAC (На Основе Атрибутов)", "ABAC (Attribute-Based Policy)"),
               items=[
                   ("<b>Mantiq:</b> Qaror 4 ta atribut kombinatsiyasi asosida qabul qilinadi:",
                    "<b>Логика:</b> Доступ рассчитывается на лету на основе 4 групп атрибутов:",
                    "<b>Mechanism:</b> Dynamic policy engine evaluates 4 contextual attribute dimensions:"),
                   ("<b>1. Foydalanuvchi:</b> Lavozimi, departamenti, tozalik darajasi.",
                    "<b>1. Субъект:</b> Должность, отдел, допуск секретности.",
                    "<b>1. Subject:</b> Department, security clearance, contractor status."),
                   ("<b>2. Resurs:</b> Hujjat maxfiyligi (Top Secret), turi, egasi.",
                    "<b>2. Объект:</b> Гриф секретности документа, владелец.",
                    "<b>2. Resource:</b> Data classification (Confidential), project tag."),
                   ("<b>3. Harakat:</b> Read, Write, Delete, Export.",
                    "<b>3. Действие:</b> Чтение, редактирование, удаление.",
                    "<b>3. Action:</b> Read, Write, Sign, Delete."),
                   ("<b>4. Muhit:</b> Vaqt (faqat 09:00-18:00), IP manzil, korporativ noutbuk sog'lomligi.",
                    "<b>4. Контекст:</b> Время суток, страна, состояние антивируса.",
                    "<b>4. Environment:</b> Time epoch, geolocation whitelist, endpoint EDR health."),
               ])
         + '\n</div>'
))

# 5. Policy-as-Code: Open Policy Agent (OPA) / AWS IAM
S.append(slide(
    ph=("Kod Sifatida Siyosat", "Политики как Код", "Policy-as-Code"), time="14–18",
    eyebrow=("Zamonaviy IAM amaliyoti", "Практика IAM в облаке", "Cloud IAM Declarations"),
    title=("IAM Siyosati: JSON Qoidalari Orqali Serverni Boshqarish",
           "Политики IAM: Управление Доступом через JSON-Правила",
           "Policy-as-Code: Declaring Granular Least-Privilege in JSON"),
    body='<div class="cols c2">\n'
         + box("", ("IAM Siyosatining Anatomiyasi", "Анатомия Политики IAM", "Anatomy of an IAM Policy"),
               items=[
                   ("<b>Effect:</b> <code>Allow</code> (Ruxsat) yoki <code>Deny</code> (Taqiq). Taqiq har doim ruxsatdan ustun!",
                    "<b>Effect:</b> `Allow` (Разрешить) или `Deny` (Запретить). `Deny` всегда побеждает!",
                    "<b>Effect:</b> Explicit `Deny` unconditionally trumps any `Allow`."),
                   ("<b>Action:</b> Ruxsat berilgan aniq amallar (masalan, <code>s3:GetObject</code>, lekin <code>s3:DeleteObject</code> emas).",
                    "<b>Action:</b> Точный список разрешённых методов API.",
                    "<b>Action:</b> Exact enumerated API operations (e.g. read-only vs delete)."),
                   ("<b>Resource:</b> Qaysi aniq server yoki ma'lumotlar omboriga tegishli (ARN).",
                    "<b>Resource:</b> Точный идентификатор объекта (ARN).",
                    "<b>Resource:</b> Target Amazon Resource Name (ARN) identifier."),
                   ("<b>Condition:</b> Qat'iy shartlar (masalan, faqat korporativ IP va MFA yoqilgan bo'lsa).",
                    "<b>Condition:</b> Дополнительные условия (только с корпоративного IP и при наличии 2FA).",
                    "<b>Condition:</b> Granular guardrails (enforce IP CIDR block and MFA presence)."),
               ])
         + '<div class="box accent">\n'
         + el("h3", "Haqiqiy Xavfsiz IAM Siyosati (JSON)", "Боевой JSON Политики IAM", "Production Least-Privilege IAM Policy")
         + code("""{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowProductionDatabaseRead",
      "Effect": "Allow",
      "Action": ["rds:DescribeDBInstances", "rds:Connect"],
      "Resource": "arn:aws:rds:us-east-1:123456:db:production-core",
      "Condition": {
        "Bool": { "aws:MultiFactorAuthPresent": "true" },
        "IpAddress": { "aws:SourceIp": "195.158.3.0/24" }
      }
    }
  ]
}""")
         + '</div>\n</div>'
))

# 6. Service-to-Service: Mutual TLS (mTLS)
S.append(slide(
    ph=("mTLS Mudofaasi", "mTLS Защита", "Mutual TLS"), time="18–22",
    eyebrow=("Mikroservislar xavfsizligi", "Безопасность микросервисов", "Zero Trust Microservices"),
    title=("Mutual TLS (mTLS): Mikroservislar O'rtasidagi Ikki Tomonlama Ishonch",
           "Mutual TLS (mTLS): Взаимная Аутентификация Сервисов",
           "Mutual TLS (mTLS): Two-Way Cryptographic Service Attestation"),
    body='<div class="cols c2">\n'
         + box("green", ("Oddiy TLS vs mTLS Farqi", "Разница TLS и mTLS", "Standard TLS vs Mutual TLS"),
               items=[
                   ("<b>Oddiy TLS (Bir tomonlama):</b> Faqat mijoz serverning sertifikatini tekshiradi (Masalan siz Google saytini tekshirasiz). Server sizning brauzeringizga so'zsiz ishonadi.",
                    "<b>Обычный TLS:</b> Только браузер проверяет сертификат сервера. Сервер же принимает любые подключения.",
                    "<b>Standard TLS:</b> Client verifies server identity. Server accepts anonymous incoming connections."),
                   ("<b>Mutual TLS (Ikki tomonlama):</b> Server ham, mijoz ham bir-biriga o'z xususiy <b>X.509 raqamli sertifikatini</b> ko'rsatadi.",
                    "<b>Mutual TLS (mTLS):</b> И клиент, и сервер обязаны предъявить взаимные криптографические сертификаты X.509.",
                    "<b>Mutual TLS (mTLS):</b> Both endpoints mandate mutual cryptographic X.509 certificate presentation."),
                   ("Ichki tarmoqqa begona hacker kirib olsa ham, uning sertifikati yo'qligi sababli <b>bitta ham mikroservisga so'rov yubora olmaydi!</b>",
                    "Даже если злоумышленник внутри офиса, без персонального сертификата сервисы сбросят его запросы.",
                    "Even if an attacker breaches the internal network, missing client certificates result in immediate TCP drops."),
               ])
         + '<div class="box purple">\n'
         + el("h3", "mTLS Handshake Sxemasi", "Схема mTLS Handshake", "mTLS Handshake Mechanics")
         + el("p", "1. <b>Mijoz:</b> <i>'Server, sertifikatingni ko'rsat!'</i><br><br>"
              "2. <b>Server:</b> Sertifikatini beradi va aytadi: <i>'Sen ham o'z sertifikatingni ko'rsat!'</i><br><br>"
              "3. <b>Mijoz:</b> O'zining maxfiy sertifikatini taqdim etadi.<br><br>"
              "4. Ikkala tomon o'zaro ishonchli Root CA (Markaziy Sertifikatlash Markazi) orqali tekshirilgach, shifrlangan kanal ochiladi!",
              "1. <b>Клиент:</b> «Сервер, покажи сертификат!»<br><br>"
              "2. <b>Сервер:</b> «Вот мой сертификат. А теперь предъяви свой клиентский сертификат!»<br><br>"
              "3. <b>Клиент:</b> Предъявляет свой подписанный сертификат.<br><br>"
              "4. Обе стороны проверяют подписи через единый внутренний CA, после чего канал шифруется.",
              "1. <b>Client:</b> Requests server certificate validation.<br><br>"
              "2. <b>Server:</b> Serves cert and demands: <i>\"CertificateRequest: Authenticate yourself!\"</i><br><br>"
              "3. <b>Client:</b> Submits authenticated client certificate.<br><br>"
              "4. Mutually validated against enterprise Root CA before encrypted stream opens.")
         + '</div>\n</div>'
))

# 7. Code Dissection: ABAC Policy Engine
S.append(slide(
    ph=("Kod Tahlili", "Анализ Кода", "Code Dissection"), time="22–26",
    eyebrow=("Dasturiy realizatsiya", "Программная реализация", "Policy Engine Implementation"),
    title=("Dinamik ABAC Qoidalarini Kodda Tekshirish",
           "Реализация Движка ABAC на Node.js",
           "Implementing Dynamic ABAC Decision Logic in Node.js"),
    body='<div class="cols c2">\n'
         + box("accent", ("Kontekstual Xavfsizlik Qoidasi", "Контекстное Правило", "Contextual Policy Specification"),
               p=("Foydalanuvchi <b>'Moliya Direktori'</b> bo'lsa ham, agar u <b>chet eldan (boshqa davlat IP)</b> yoki <b>tungi soat 03:00 da</b> kirayotgan bo'lsa, pul o'tkazish operatsiyasi darhol bloklanadi va xavfsizlik xizmatiga ogohlantirish yuboriladi.",
                  "Даже финансовый директор блокируется при попытке перевода денег ночью в 03:00 или из подозрительной страны.",
                  "Even a CFO role is blocked if an authorization request originates from an unapproved geolocation or anomalous off-hours window."))
         + '<div class="box green">\n'
         + el("h3", "ABAC Middleware Kodi", "Код Проверки ABAC", "ABAC Decision Middleware")
         + code("""function authorizeABAC(user, resource, action, env) {
  // 1. Rol va Huquqni tekshirish
  if (user.role !== 'CFO' && action === 'wire_transfer') return false;

  // 2. Muhit atributlari (Vaqt va Geolocation)
  const currentHour = new Date().getHours();
  if (currentHour < 8 || currentHour > 19) {
    console.warn(`[ALERT] Off-hours attempt by ${user.id}`);
    return false; // Ish vaqtidan tashqarida taqiqlangan!
  }

  if (env.country !== 'UZ' || !env.isCorporateDevice) {
    console.warn(`[ALERT] Non-compliant device: ${env.deviceId}`);
    return false; // Faqat korporativ noutbuk va O'zbekiston!
  }

  return true; // Barcha atributlar mos keldi!
}""")
         + '</div>\n</div>'
))

# 8. Real-World Case Study: Capital One Breach
S.append(slide(
    ph=("Real Keys", "Кейс из Жизни", "Case Study"), time="26–30",
    eyebrow=("80 million dollarlik IAM xatosi", "Убыток $80 млн из-за IAM", "The $80M IAM Failure"),
    title=("Capital One Kiber-Halokati: Haddan Tashqari Keng IAM Ruxsatlari",
           "Взлом Capital One: Слишком Широкие Права в IAM",
           "The Capital One Breach: Excessive IAM Permissions Disaster"),
    body='<div class="cols c2">\n'
         + box("accent", ("Nima Sodir Bo'lgan?", "Хроника Инцидента", "Incident Anatomy"),
               p=("2019-yilda xaker Paige Thompson bankning AWS bulutidagi WAF (Web Application Firewall) serveridagi SSRF zaifligi orqali ichkariga kirdi. Ammo eng katta falokat ichkarida yotardi: WAF serverining IAM roliga <b>haddan tashqari keng huquqlar (Over-privileged Role)</b> berilgan edi. Natijada xaker bankning barcha mijozlari kredit arizalari saqlanadigan <b>700 dan ortiq S3 omborlarini</b> bir zumda ko'chirib oldi.",
                  "В 2019 году бывший инженер AWS через уязвимость SSRF проникла на сервер WAF банка Capital One. Сервер имел избыточные права IAM. Злоумышленница скачала 700 корзин S3 с данными 106 миллионов кредитных карт.",
                  "In 2019, an adversary leveraged an SSRF flaw on Capital One's WAF EC2 instance. The instance IAM role was egregiously over-privileged. The attacker listed and dumped 700+ S3 buckets containing credit applications for 106 million customers."))
         + box("purple", ("Falokat Sabog'i: Minimal Huquq (Least Privilege)", "Урок: Принцип Наименьших Прав", "Core Lesson: Least Privilege"),
               items=[
                   ("<b>106 000 000 ta mijoz:</b> Ijtimoiy himoya raqamlari (SSN) va bank hisoblari o'g'irlandi.",
                    "<b>106 млн клиентов:</b> Утечка номеров страхования и банковских транзакций.",
                    "<b>106 million records:</b> Social Security numbers, bank accounts, and credit scores exposed."),
                   ("<b>80 000 000 dollar jarima:</b> AQSh regulyatorlari bankni IAM nazoratini yo'qotgani uchun 80 million dollar jarimaga tortdi.",
                    "<b>Штраф $80 млн:</b> Банк оштрафован за отсутствие принципа Least Privilege.",
                    "<b>$80,000,000 regulatory fine:</b> Slapped with massive fines for gross IAM governance failure."),
                   ("<b>Yechim:</b> WAF serveriga faqat tarmoqni filtrlash ruxsati berilishi kerak edi, S3 ma'lumotlar omborini o'qish huquqi mutlaqo taqiqlanishi shart edi!",
                    "<b>Вывод:</b> Серверу фаервола были не нужны права на чтение всех баз клиентов!",
                    "<b>Remedy:</b> The WAF role had zero business reading customer S3 storage. Principle of Least Privilege would have isolated the blast radius to zero!"),
               ])
         + '\n</div>'
))

# 9. Practical Mission (12 min timer)
S.append(slide(
    ph=("Amaliyot", "Практика", "Hands-On Lab"), time="30–42",
    eyebrow=("Mustaqil laboratoriya · 12 daqiqa", "Лабораторная работа · 12 минут", "Practical Lab · 12 Minutes"),
    title=("Amaliy Topshiriq: Zero Trust IAM Siyosatini Loyihalash",
           "Практическое Задание: Проектирование Политики IAM",
           "Mission: Architecting a Zero Trust Least-Privilege IAM Policy"),
    body='<div class="cols c2">\n'
         + box("green", ("Laboratoriya Bosqichlari", "Шаги Лабораторной", "Mission Checkpoints"),
               items=[
                   ("<b>1. Haddan tashqari huquqni aniqlash:</b> Berilgan xavfli siyosatdagi <code>\"Action\": \"*\"</code> va <code>\"Resource\": \"*\"</code> xatolarini toping.",
                    "<b>1. Аудит уязвимой политики:</b> Найдите опасные подстановочные знаки `Action: *`.",
                    "<b>1. Audit wildcard policies:</b> Locate dangerous `Action: *` and `Resource: *` flaws."),
                   ("<b>2. Minimal huquqqa o'tkazish:</b> Siyosatni faqat `db:ReadProductionData` ga cheklab, yozish va o'chirishni taqiqlang.",
                    "<b>2. Ограничение прав:</b> Сузьте действие политики строго до чтения данных.",
                    "<b>2. Restrict to read-only:</b> Enforce explicit least-privilege action boundaries."),
                   ("<b>3. ABAC Shartlari (Condition):</b> Siyosatga <code>MultiFactorAuthPresent: true</code> va korporativ IP cheklovini qo'shing.",
                    "<b>3. Добавление условий:</b> Внедрите обязательное требование MFA и доверенного IP.",
                    "<b>3. Inject dynamic conditions:</b> Mandate MFA attestation and source IP subnet CIDR."),
                   ("<b>4. Policy Test:</b> Yozilgan JSON siyosatini validator orqali sinab, ruxsatsiz urinish rad etilishini tasdiqlang.",
                    "<b>4. Тестирование:</b> Проверьте отказ доступа при несоответствии условий.",
                    "<b>4. Validate policy:</b> Confirm denial upon non-compliant environmental context."),
               ])
         + box("accent", ("O'lchanadigan Natija", "Критерий Сдачи", "Deliverable Spec"),
               p=("Ish varaqasiga 100% xavfsiz Zero Trust IAM JSON siyosatini yozish va Capital One keysidagi xatolikni bartaraf etuvchi 3 ta nazorat qoidasini ko'rsatish!",
                  "Составить валидный JSON политики с ограничениями MFA и IP, закрывающий уязвимость из кейса Capital One!",
                  "Deliver a production-ready Zero Trust JSON IAM policy enforcing MFA and IP restrictions, eliminating the Capital One failure mode!"))
         + '\n</div>'
))

# 10. Verification Checklist
S.append(slide(
    ph=("Tekshirish", "Чек-лист", "Verification"), time="42–43",
    eyebrow=("Arxitektura auditi", "Проверка архитектуры", "Architectural Audit"),
    title=("Zero Trust Nazorat Cheklisti: 5 Ta Talab",
           "Чек-лист Аудита Zero Trust: 5 Требований",
           "Zero Trust Architectural Quality Gates"),
    body='<div class="cols c3">\n'
         + box("", ("1. Wildcard (*) Yo'qmi?", "1. Нет Wildcard (*)?", "1. No Wildcard (*)"),
               p=("`Action` va `Resource` maydonlarida xavfli `*` yulduzcha butunlay yo'q qilinganmi?",
                  "Исключены ли опасные звёздочки `*` из полей действий и ресурсов?",
                  "Are dangerous wildcard asterisks strictly excised from permissions?"))
         + box("", ("2. MFA Majburiymi?", "2. Требование MFA?", "2. Mandatory MFA?"),
               p=("`Condition` blokida ko'p faktorli tasdiq (MFA) mavjudligi talab qilinganmi?",
                  "Проверяется ли обязательное наличие двухфакторки в блоке Condition?",
                  "Does the Condition block strictly mandate active MFA validation?"))
         + box("", ("3. mTLS Mikro-segment", "3. Сегментация mTLS?", "3. mTLS Segmentation?"),
               p=("Mikroservislararo aloqa o'zaro sertifikatlar bilan himoyalanganmi?",
                  "Защищены ли межсервисные вызовы взаимными сертификатами mTLS?",
                  "Are inter-service channels mutually authenticated via X.509 certs?"))
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
                   ("Zero Trust tamoyillari (NIST SP 800-207) to'liq tushuntirilgan.", "Принципы Zero Trust объяснены профессионально.", "Zero Trust core tenets thoroughly mastered."),
                   ("IAM JSON siyosati Least Privilege talabiga mos yozilgan.", "Политика IAM JSON написана по принципу Least Privilege.", "IAM JSON policy enforces exact least-privilege boundaries."),
                   ("RBAC vs ABAC va mTLS farqi to'g'ri ko'rsatilgan.", "Разница RBAC/ABAC и mTLS обоснована верно.", "RBAC vs ABAC & mTLS justifications accurate."),
                   ("Varaqa 100% to'ldirilgan.", "Рабочий лист заполнен на 100%.", "Worksheet completed 100%."),
               ])
         + box("", ("Yaxshi (7–8 Ball)", "Хорошо (7–8)", "Proficient (7–8)"),
               items=[
                   ("IAM siyosatida kichik kamchilik bor, lekin xavfsiz.", "В политике IAM мелкие недочёты, но она безопасна.", "IAM policy functional with minor scope oversights."),
                   ("Zero Trust g'oyasi tushunilgan.", "Концепция Zero Trust усвоена.", "Zero Trust paradigm understood."),
                   ("Varaqa 80% to'ldirilgan.", "Лист заполнен на 80%.", "Worksheet completed 80%."),
               ])
         + box("accent", ("Qoniqarli (5–6 Ball)", "Удовл. (5–6)", "Developing (5–6)"),
               items=[
                   ("Wildcard (*) xatolari to'liq bartaraf etilmagan.", "Остались опасные звёздочки в политике IAM.", "Wildcards remain in IAM permissions."),
                   ("ABAC tushunchasida chalkashlik bor.", "Слабое понимание модели ABAC.", "Confusion regarding ABAC dynamic attributes."),
                   ("Varaqa to'liq emas.", "Лист заполнен частично.", "Worksheet incomplete."),
               ])
         + '\n</div>'
))

# 12. Summary & Homework
S.append(slide(
    ph=("Xulosa", "Итоги", "Summary"), time="44–45",
    eyebrow=("Uyga vazifa", "Домашнее задание", "Homework & Next Steps"),
    title=("Xulosa va Uy Vazifasi: Chegarasiz Korxona Xavfsizligi",
           "Итоги и Домашнее Задание: Безопасность без Периметра",
           "Summary & Homework: Borderless Enterprise Defense"),
    body='<div class="cols c2">\n'
         + box("purple", ("Dars Xulosasi", "Итоги Урока", "Core Summary"),
               p=("Zero Trust — bu bitta dastur yoki qurilma emas, balki korporativ madaniyat va arxitektura tamoyilidir. Identifikatsiyani doimiy tekshirish, huquqlarni minimal darajada cheklash va har bir so'rovni dushman deb hisoblash har qanday kiber-buzilishning oqibatlarini nolga tenglashtiradi.",
                  "Zero Trust — это не утилита, а целостная архитектурная парадигма. Непрерывная проверка личности и принцип наименьших привилегий локализуют радиус любого инцидента до нуля.",
                  "Zero Trust is not a software vendor SKU; it is an architectural discipline. Enforcing continuous identity attestation and ruthless least privilege bounds blast radiuses to absolute zero."))
         + box("accent", ("Uy Vazifasi (10 Ball)", "Домашнее Задание (10 Баллов)", "Homework Assignment (10 Pts)"),
               items=[
                   ("<b>Arxitektura Loyihasi:</b> Tasavvur qiling, siz bank kiberxavfsizlik me'morisiz. Mobil ilova va baza o'rtasida Zero Trust arxitektura sxemasini chizing.",
                    "<b>Архитектурный проект:</b> Разработайте схему Zero Trust для мобильного банка.",
                    "<b>Architecture Diagram:</b> Design a Zero Trust topology for a digital banking system."),
                   ("<b>IAM Siyosati:</b> Junior dasturchiga faqat `staging` serverdagi loglarni o'qish huquqini beruvchi, lekin `production` ga kirishni qat'iy taqiqlovchi JSON siyosatini yozing.",
                    "<b>Политика IAM:</b> Напишите JSON-политику для джуниора: только чтение логов staging с запретом prod.",
                    "<b>IAM Declaration:</b> Write an IAM JSON policy granting read-only staging access while denying production."),
                   ("<b>Varaqa:</b> Ish varaqasidagi barcha masalalarni yakunlab topshiring.",
                    "<b>Лист:</b> Заполните и сдайте печатный рабочий лист.",
                    "<b>Worksheet:</b> Complete and submit your printable lab worksheet."),
               ])
         + '\n</div>'
))

# Teacher Notes
N_UZ = [
    ["Kirish", "Darsni boshlash: Zero Trust va IAM. Nega eski perimetr mudofaasi o'ldi?", "Slaydni oching, bulutli texnologiyalar davrida VPN ning nima uchun yetarli emasligini tushuntiring."],
    ["Paradigma", "Castle-and-Moat vs Zero Trust. Ichki tarmoqqa ishonish halokati va lateral movement xavfi.", "Qasr va xandak metaforasi orqali eski modelning xatolarini ochib bering."],
    ["Asosiy Ustunlar", "Zero Trust ning 3 ta asosiy qoidasi: Verify Explicitly, Least Privilege, Assume Breach.", "NIST SP 800-207 standartini tanishtiring."],
    ["Ruxsat Nazorati", "RBAC va ABAC solishtirmasi. Nega katta tizimlarda dinamik atributlar (ABAC) kerak?", "Doskaga 4 ta atribut guruhini (Subyekt, Resurs, Amal, Muhit) yozib ko'rsating."],
    ["Kod Sifatida Siyosat", "IAM JSON siyosati. Effect, Action, Resource, Condition maydonlari.", "Ekranda AWS IAM siyosati strukturasini tahlil qiling."],
    ["mTLS Mudofaasi", "Mutual TLS nima? Mikroservislar bir-birining sertifikatini qanday tekshiradi?", "TLS va mTLS dialogini o'quvchilar bilan birga o'qing."],
    ["Kod Tahlili", "Node.js da dinamik ABAC qoidalarini tekshiruvchi funksiya.", "Tungi vaqt va chet el IP-si bo'yicha cheklov kodini ko'rsating."],
    ["Real Keys", "Capital One kiber-halokati. Haddan tashqari keng IAM huquqlari tufayli 80 million dollar jarima.", "SSRF orqali kirib S3 larni o'g'irlash keysini tahlil qiling."],
    ["Amaliyot", "12 daqiqalik laboratoriya. O'quvchilar Least Privilege IAM siyosatini loyihalaydilar.", "Taymerni yoqing (12 daqiqa), o'quvchilar bilan ishlang."],
    ["Tekshirish", "Nazorat tekshiruvi. Yulduzchalar yo'qligini va MFA shartini tekshirish.", "JSON sintaksisini tekshiring."],
    ["Mezon", "10 ballik baholash mezoni tushuntiriladi.", "Talablarni e'lon qiling."],
    ["Xulosa", "Dars yakuni va uy vazifasi. Kelgusi darsda API Xavfsizligi va Rate Limiting ni o'rganamiz.", "Varaqalarni yig'ing."]
]

N_RU = [
    ["Введение", "Старт урока: Архитектура Zero Trust и IAM в корпоративных системах.", "Откройте слайд, объясните смену парадигмы безопасности."],
    ["Парадигма", "Смерть периметра: почему концепция «Замка со рвом» провалилась.", "Объясните опасность бокового перемещения хакера (Lateral Movement)."],
    ["Столпы Zero Trust", "3 принципа NIST SP 800-207: явная проверка, минимум прав, допущение взлома.", "Разберите каждый постулат с точки зрения архитектуры."],
    ["Контроль Доступа", "RBAC против ABAC: переход от статичных ролей к контекстным атрибутам.", "Покажите проблему Role Explosion."],
    ["Политики как Код", "Анатомия политик IAM в формате JSON: Effect, Action, Resource, Condition.", "Покажите боевой JSON с ограничением по IP и MFA."],
    ["mTLS Защита", "Взаимный TLS (mTLS): двусторонняя проверка подлинности микросервисов.", "Сравните классический TLS и mTLS."],
    ["Анализ Кода", "Реализация проверок ABAC в коде на Node.js.", "Объясните контекстные фильтры времени и корпоративного устройства."],
    ["Кейс из Жизни", "Кейс Capital One: $80 млн штрафа за избыточные права IAM у роли WAF.", "Разберите хронологию масштабной утечки данных."],
    ["Практика", "12 минут практики: проектирование безопасной политики Least Privilege.", "Запустите таймер, помогайте с директивами JSON."],
    ["Проверка", "Чек-лист проверки: убедитесь в отсутствии `*` и наличии условий MFA.", "Проверьте вывод политик учащихся."],
    ["Критерии", "10-балльная шкала оценивания практической работы.", "Озвучьте критерии оценки."],
    ["Итоги", "Завершение урока и домашнее задание. На следующем занятии — безопасность API и Rate Limiting.", "Соберите рабочие листы."]
]

N_EN = [
    ["Intro", "Lesson opening: Zero Trust Architecture & enterprise IAM governance.", "Frame the systemic shift in security philosophy."],
    ["Paradigm Shift", "The collapse of castle-and-moat perimeter defense and VPN trust assumptions.", "Illustrate lateral movement risks."],
    ["Core Pillars", "The 3 NIST SP 800-207 pillars: Verify explicitly, least privilege, assume breach.", "Explain defense-in-depth principles."],
    ["Access Control", "RBAC vs dynamic ABAC: Resolving the enterprise role explosion trap.", "Contrast static role assignments with dynamic context evaluation."],
    ["Policy-as-Code", "Deconstructing JSON IAM declarations: Effect, Action, Resource, and Conditions.", "Walk through real-world IAM definitions."],
    ["Mutual TLS", "Mutual TLS (mTLS) zero-trust microservice communication.", "Diagram mutual X.509 handshake attestation."],
    ["Code Dissection", "Implementing an ABAC decision engine in Node.js middleware.", "Highlight contextual time/device checks."],
    ["Case Study", "The Capital One catastrophe: An over-privileged WAF role triggering $80M in penalties.", "Analyze the blast radius of unsegmented permissions."],
    ["Hands-On Lab", "12-minute lab: Architecting a least-privilege IAM JSON policy.", "Start 12-minute countdown timer and provide feedback."],
    ["Verification", "Zero Trust quality gate: Verifying removal of wildcards and MFA enforcement.", "Audit student JSON policies."],
    ["Evaluation", "10-point evaluation rubric breakdown.", "Review grading thresholds."],
    ["Summary", "Wrap-up and homework preview. Next session: API Security & Rate Limiting algorithms.", "Collect worksheets."]
]

NOTES = {"uz": N_UZ, "ru": N_RU, "en": N_EN}

# ---------------------------------------------------------------- Varaqa Body
V = []
V.append(sheet_header(
    h1=("Kiberxavfsizlik: Zero Trust va IAM Arxitekturasi",
        "Кибербезопасность: Архитектура Zero Trust и IAM",
        "CyberSecurity: Zero Trust Architecture & IAM"),
    sub=("Amaliy Laboratoriya Varaqasi · 10–11-sinf · 5-hafta · 22-dars",
         "Практический Рабочий Лист · 10–11 класс · Неделя 5 · Урок 22",
         "Hands-On Lab Worksheet · Grades 10–11 · Week 5 · Lesson 22")
))

V.append(mission(
    h=("Laboratoriya Vazifasi: Minimal Huquqli IAM Siyosatini Tuzish",
       "Миссия Лабораторной: Разработка Политики Least Privilege в IAM",
       "Lab Mission: Engineering a Least-Privilege Zero Trust IAM Policy"),
    p=("Haddan tashqari keng huquqli xavfli IAM siyosatini tahlil qilish, undagi xatolarni bartaraf etish, "
       "va faqat zarur amallarga ruxsat beruvchi, MFA va korporativ IP ni talab qiluvchi xavfsiz JSON siyosatini yozish.",
       "Проанализировать небезопасную политику IAM с избыточными правами, устранить уязвимости, "
       "и составить строгий JSON с ограничениями по ролям, MFA и доверенным подсетям IP.",
       "Audit an over-privileged wildcard IAM policy, eliminate exposure vulnerabilities, "
       "and author a resilient Zero Trust JSON policy enforcing strict action scoping, MFA presence, and trusted IP ranges."))
)

V.append(table(
    headers=[
        ("Me'moriy Qatlam", "Уровень Архитектуры", "Architecture Layer"),
        ("Eski Model (Xavfli)", "Старый Подход (Опасно)", "Legacy Castle-and-Moat"),
        ("Zero Trust Standarti", "Стандарт Zero Trust", "Zero Trust Standard"),
        ("Holat", "Статус", "Status")
    ],
    rows=[
        [("1. Tarmoq Ishonchi", "1. Доверие Сети", "1. Network Trust"),
         ("VPN ichidagi barcha qurilmalar ishonchli", "Внутренний трафик доверенный", "Implicit trust inside VPN perimeter"),
         ("Har bir so'rov dushman deb tekshiriladi", "Каждый запрос строго проверяется", "Zero implicit trust; continuous checks"),
         ("✅ O'zlashtirildi", "✅ Освоено", "✅ Mastered")],
        [("2. Ruxsat Modeli", "2. Модель Доступа", "2. Authorization"),
         ("Statik rollar (`Admin`, `User`)", "Статичные роли (Role Explosion)", "Coarse static roles (RBAC)"),
         ("Dinamik kontekstual ABAC siyosati", "Динамический контекстный ABAC", "Contextual attribute policies (ABAC)"),
         None],
        [("3. Mikroservislar", "3. Микросервисы", "3. Microservices"),
         ("Ochiq HTTP / Bir tomonlama TLS", "Открытый HTTP внутри кластера", "Plaintext HTTP across private cluster"),
         ("Ikki tomonlama shifrlangan mTLS", "Взаимный mTLS с сертификатами", "Mutual TLS (mTLS) with strict certs"),
         None],
        [("4. Imtiyoz Muddati", "4. Срок Привилегий", "4. Privilege Lifetime"),
         ("Doimiy ochiq admin huquqlari", "Постоянные права администратора", "Standing perpetual admin rights"),
         ("Just-In-Time (JIT) vaqtinchalik ruxsat", "Временный доступ по запросу (JIT)", "Just-In-Time (JIT) ephemeral access"),
         None],
    ]
))

V.append(sheet_box(
    h=("Xavfsizlik Tahlili va Nazariy Savollar", "Анализ Безопасности и Вопросы", "Architectural Analysis & Written Queries"),
    body_html=writelines(3, label=("1. Nega korporativ tarmoqda 'Action: *' va 'Resource: *' yozish Capital One fojiasiga o'xshash falokatga olib keladi?",
                                   "1. Почему использование 'Action: *' в IAM приводит к катастрофам масштаба Capital One?",
                                   "1. Why is authoring 'Action: *' and 'Resource: *' in IAM policies an enterprise catastrophe risk?"))
             + "<br>"
             + writelines(3, label=("2. mTLS (Mutual TLS) oddiy TLS dan nimasi bilan farq qiladi va ichki tarmoq xavfsizligini qanday kafolatlaydi?",
                                   "2. Чем mTLS отличается от обычного TLS и как он защищает микросервисы от внутреннего перехвата?",
                                   "2. How does Mutual TLS (mTLS) fundamentally differ from standard TLS in securing microservices?"))
))

V.append(sheet_box(
    h=("Baholash Mezoni (10 Ball)", "Критерии Оценки (10 Баллов)", "Grading Rubric (10 Points)"),
    body_html=rubric([
        (("Zero Trust tamoyillari va NIST SP 800-207 to'liq tahlil qilingan", "Принципы Zero Trust и NIST SP 800-207 разобраны верно", "Zero Trust tenets & NIST SP 800-207 analyzed"), "3 ball"),
        (("IAM JSON siyosati Least Privilege va Condition bilan to'g'ri yozilgan", "Политика IAM JSON составлена с ограничениями MFA и IP", "IAM JSON policy correctly authored with MFA & IP guards"), "3 ball"),
        (("Capital One keysi va mTLS arxitekturasi aniq asoslangan", "Разобраны кейс Capital One и архитектура mTLS", "Capital One incident & mTLS architecture justified"), "2 ball"),
        (("Nazariy savollarga to'liq va asosli javob berilgan", "Даны развернутые ответы на теоретические вопросы", "Written analytical queries thoroughly answered"), "2 ball"),
    ], "10 ball")
))

V.append("</div>\n" + sign_box("Musulmonov Mamarajab"))

VARAQA_BODY = "\n".join(V)

lesson = Lesson(
    outdir=D,
    titles=TITLES,
    sheet_titles=SHEET_TITLES,
    key="vc-notes-10-22",
    slides=S,
    notes=NOTES,
    varaqa_body=VARAQA_BODY
)

if __name__ == "__main__":
    out = lesson.build()
    print("Created:", out)
