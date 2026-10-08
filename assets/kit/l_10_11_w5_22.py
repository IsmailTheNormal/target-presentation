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
          "Bugun siz <b>IAM (Identity and Access Management)</b>, <b>RBAC vs ABAC</b> dinamik qoidalarini, "
          "va <b>Zero Trust & IAM Studio</b> orqali Capital One $80M kiber-halokatini bartaraf etishni amalda o'rganasiz.",
          "Классическая безопасность напоминала замок со рвом: защита по периметру, "
          "но внутри сети любой узел считался доверенным. В облачную эпоху этот подход смертелен. "
          "Ему на смену пришёл стандарт <b>NIST SP 800-207 — Zero Trust («Никому не доверяй, всегда проверяй»)</b>. "
          "Сегодня вы разберёте системы <b>IAM</b>, разницу политик <b>RBAC и ABAC</b>, "
          "и на практике в <b>Zero Trust Studio</b> исправите уязвимость из кейса Capital One на $80 млн.",
          "Traditional perimeter security operated like a medieval castle and moat: hardened borders, "
          "yet implicitly trusting all internal traffic once breached. In modern cloud infrastructures, this model failed. "
          "It has been replaced by <b>NIST SP 800-207: Zero Trust (\"Never Trust, Always Verify\")</b>. "
          "Today you will master enterprise <b>IAM governance</b>, compare <b>RBAC vs dynamic ABAC</b>, "
          "and hands-on mitigate the $80M Capital One catastrophe using interactive <b>Zero Trust & IAM Studio</b>."),
    meta=[("<b>Fan:</b> Kiberxavfsizlik · Enterprise Architecture",
           "<b>Предмет:</b> Кибербезопасность · Корпоративная Архитектура",
           "<b>Subject:</b> CyberSecurity · Enterprise Architecture"),
          ("<b>Kohorta:</b> 10-11-sinf Kiber-Muhandis",
           "<b>Когорта:</b> 10-11 класс Инженер Безопасности",
           "<b>Cohort:</b> Grade 10-11 Security Engineer"),
          ("<b>Hafta:</b> 5 (2-soat)", "<b>Неделя:</b> 5 (2-й час)", "<b>Week:</b> 5 (Hour 2)")],
))

# 2. Paradigm Shift: Castle-and-Moat vs Airport Security
S.append(slide(
    ph=("Paradigma", "Парадигма", "Paradigm Shift"), time="3–6",
    eyebrow=("Arxitektura inqilobi", "Архитектурная революция", "Architectural Evolution"),
    title=("Perimetr Mudofaasi O'ldi: Nega Qasr Modeli Barham Topdi?",
           "Периметр Мёртв: Почему Модель «Замка» Уступила Место Аэропорту?",
           "The Death of the Perimeter: Why Castle-and-Moat Failed"),
    body='<div class="cols c2">\n'
         + box("accent", ("1. Eski Model: Qasr va Xandak (Castle-and-Moat)", "1. Старая Модель: Замок со Рвом", "1. Legacy Castle-and-Moat"),
               items=[
                   ("<b>VPN ichidagi so'zsiz ishonch:</b> Bir marta korporativ VPN ga ulangan xodim butun ichki tarmoqqa to'liq ishonchli deb qaralgan.",
                    "<b>Безусловное доверие внутри VPN:</b> Подключившись к корпоративной сети, пользователь получал доступ ко всем ресурсам.",
                    "<b>Implicit trust:</b> Connecting to corporate VPN implicitly granted blanket access to intranet subnets."),
                   ("<b>Lateral Movement (Yonlama siljish):</b> Xaker bitta buxgalter noutbukini buzsa, butun ichki tarmoq bo'ylab erkin harakatlanib bazalarga kirgan.",
                    "<b>Боковое перемещение:</b> Взлом одного ноутбука позволял свободно атаковать сервера баз данных компании.",
                    "<b>Lateral movement:</b> Compromising an endpoint allowed pivoting freely across database clusters."),
               ])
         + box("green", ("2. Yangi Model: Aeroport Standarti (Zero Trust)", "2. Модель Аэропорта: Zero Trust", "2. Zero Trust (Airport Model)"),
               items=[
                   ("<b>Aeroportdagi kabi qat'iy nazorat:</b> Aeroport eshigida bitta chipta ko'rsatib, samolyot kabinasiga kirib keta olmaysiz!",
                    "<b>Контроль как в аэропорту:</b> Предъявив билет на входе, нельзя зайти в кабину пилотов. Каждый гейт проверяется заново.",
                    "<b>Airport security paradigm:</b> A terminal boarding pass does not grant cockpit access. Every checkpoint verifies context."),
                   ("<b>Doimiy tasdiqlash:</b> Ichki Wi-Fi dagi noutbuk ham, internetdagi notanish server ham bir xil potentsial xavf deb tekshiriladi.",
                    "<b>Непрерывная проверка:</b> Компьютер в офисе считается столь же потенциально опасным, как узел в интернете.",
                    "<b>Continuous verification:</b> Nodes on corporate LAN are treated as untrusted as nodes on the public internet."),
                   ("<b>Mikro-segmentatsiya:</b> Har bir baza va xizmat o'zining shaxsiy mTLS shifrlangan darvozasiga ega.",
                    "<b>Микросегментация:</b> Каждый сервис защищён персональным шлюзом с взаимным mTLS шифрованием.",
                    "<b>Micro-segmentation:</b> Microservices enforce zero visibility without authenticated mutual TLS channels."),
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
               p=("Doim barcha mavjud signallarni tekshirish: shaxs (identifikator), joylashuv, qurilma holati (EDR/MDM), xizmat turi, anomaliyalar va xavf darajasi.",
                  "Всегда проверять контекст: личность, геолокацию, здоровье устройства, EDR, прошивку, аномалии поведения.",
                  "Continuously evaluate all contextual signals: user identity, geolocation, endpoint posture, and anomaly scores."))
         + box("purple", ("2. Least Privilege (Minimal Huquq)", "2. Минимум Прав (Least Privilege)", "2. Use Least-Privilege Access"),
               p=("Foydalanuvchiga faqat ayni daqiqadagi topshiriq uchun zarur bo'lgan minimal huquq beriladi. Just-In-Time (JIT) va Just-Enough-Access (JEA).",
                  "Ограничение доступа ровно тем минимумом, который нужен для текущей задачи, и строго на ограниченное время.",
                  "Limit user access with Just-In-Time (JIT) and Just-Enough-Access (JEA) constraints, closing permissions immediately."))
         + box("green", ("3. Assume Breach (Buzilgan deb hisobla)", "3. Допущение Взлома (Assume Breach)", "3. Assume Breach"),
               p=("Tizim allaqachon dushman tomonidan buzilgan deb harakat qilish. Ma'lumotlarni shifrlash, barcha loglarni kuzatish va tarmoqni mikro-zonalarga ajratish.",
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
                   ("<b>Mantiq:</b> Foydalanuvchiga bitta statik rol biriktiriladi (masalan, <code>Admin</code>, <code>Editor</code>, <code>Viewer</code>).",
                    "<b>Логика:</b> Права привязаны к статичной роли пользователя (Admin, Editor, Viewer).",
                    "<b>Mechanism:</b> Permissions map to coarse static roles (Admin, Editor, Viewer)."),
                   ("<b>Kamchiligi: Role Explosion!</b> Katta korxonalarda <i>'Kechasi ishlaydigan Londonlik moliya tahrirchisi'</i> kabi yuzlab sun'iy rollar paydo bo'ladi.",
                    "<b>Минус: Взрыв ролей (Role Explosion).</b> Появление сотен узких ролей под каждого сотрудника.",
                    "<b>Fatal flaw: Role Explosion.</b> Enterprise systems end up with thousands of redundant, overlapping roles."),
                   ("<b>Vaqt va joyni bilmaydi:</b> Admin hisobidan xaker tungi 03:00 da begona IP dan kirsa ham ruxsat beraveradi!",
                    "<b>Слепота к контексту:</b> Хакер под админом ночью из другой страны получит полный доступ.",
                    "<b>Context blindness:</b> An attacker with stolen admin creds at 03:00 AM from an unknown IP gets full clearance."),
               ])
         + box("accent", ("ABAC (Attribute-Based Access Control)", "ABAC (На Основе Атрибутов)", "ABAC (Attribute-Based Policy)"),
               items=[
                   ("<b>Mantiq:</b> Qaror 4 ta atribut kombinatsiyasi asosida dinamik qabul qilinadi:",
                    "<b>Логика:</b> Доступ рассчитывается на лету на основе 4 групп атрибутов:",
                    "<b>Mechanism:</b> Dynamic policy engine evaluates 4 contextual attribute dimensions:"),
                   ("<b>1. Subyekt:</b> Lavozimi, departamenti, tozalik darajasi.",
                    "<b>1. Субъект:</b> Должность, отдел, допуск секретности.",
                    "<b>1. Subject:</b> Department, role, security clearance."),
                   ("<b>2. Resurs:</b> Hujjat maxfiyligi (Top Secret), turi, egasi.",
                    "<b>2. Объект:</b> Гриф секретности документа, владелец.",
                    "<b>2. Resource:</b> Data classification, tenant project tag."),
                   ("<b>3. Amal:</b> Read, Write, Delete, AdminExecute.",
                    "<b>3. Действие:</b> Чтение, редактирование, удаление.",
                    "<b>3. Action:</b> Read, Write, Sign, Delete."),
                   ("<b>4. Muhit:</b> Vaqt (faqat ish soatlari), IP manzil, korporativ noutbuk sog'lomligi.",
                    "<b>4. Контекст:</b> Время суток, доверенная подсеть, статус антивируса/EDR.",
                    "<b>4. Environment:</b> Working hours, corporate subnet, endpoint EDR compliance."),
               ])
         + '\n</div>'
))

# 5. Policy-as-Code: AWS IAM JSON Siyosatining Anatomiyasi
S.append(slide(
    ph=("Kod Sifatida Siyosat", "Политики как Код", "Policy-as-Code"), time="14–18",
    eyebrow=("Zamonaviy IAM amaliyoti", "Практика IAM в облаке", "Cloud IAM Declarations"),
    title=("IAM Siyosatining Anatomiyasi: 4 Ta Asosiy Kalit",
           "Анатомия Политики IAM: 4 Ключевых Элемента",
           "Anatomy of an IAM Policy: 4 Essential Primitives"),
    body='<div class="cols c2">\n'
         + box("", ("Qoidaning Tuzilishi", "Структура Директивы", "Policy Directives"),
               items=[
                   ("<b>1. Effect:</b> <code>Allow</code> (Ruxsat) yoki <code>Deny</code> (Taqiq). <b>Taqiq har doim ruxsatdan ustun!</b>",
                    "<b>1. Effect:</b> `Allow` (Разрешить) или `Deny` (Запретить). <b>`Deny` всегда побеждает!</b>",
                    "<b>1. Effect:</b> Explicit `Deny` unconditionally trumps any `Allow`."),
                   ("<b>2. Action:</b> Aniq amallar ro'yxati (masalan, <code>s3:GetObject</code>, lekin <code>s3:DeleteObject</code> emas).",
                    "<b>2. Action:</b> Точный список разрешённых методов API.",
                    "<b>2. Action:</b> Exact enumerated API operations (e.g. read-only vs delete)."),
                   ("<b>3. Resource:</b> Qaysi aniq server yoki omborga tegishli (ARN).",
                    "<b>3. Resource:</b> Точный идентификатор объекта (ARN).",
                    "<b>3. Resource:</b> Target Amazon Resource Name (ARN) identifier."),
                   ("<b>4. Condition:</b> Qat'iy shartlar (masalan, faqat korporativ IP va MFA yoqilgan bo'lsa).",
                    "<b>4. Condition:</b> Дополнительные условия (только с доверенного IP и при наличии 2FA).",
                    "<b>4. Condition:</b> Dynamic guards (enforce source IP CIDR and mandatory MFA)."),
               ])
         + '<div class="box accent">\n'
         + el("h3", "Haqiqiy Xavfsiz IAM JSON Siyosati", "Боевой JSON Политики IAM", "Production Least-Privilege IAM Policy")
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

# 6. Mutual TLS (mTLS)
S.append(slide(
    ph=("mTLS Mudofaasi", "mTLS Защита", "Mutual TLS"), time="18–22",
    eyebrow=("Mikroservislar xavfsizligi", "Безопасность микросервисов", "Zero Trust Microservices"),
    title=("Mutual TLS (mTLS): Mikroservislar O'rtasidagi Ikki Tomonlama Ishonch",
           "Mutual TLS (mTLS): Взаимная Аутентификация Сервисов",
           "Mutual TLS (mTLS): Two-Way Cryptographic Service Attestation"),
    body='<div class="cols c2">\n'
         + box("green", ("Oddiy TLS vs mTLS Farqi", "Разница TLS и mTLS", "Standard TLS vs Mutual TLS"),
               items=[
                   ("<b>Oddiy TLS (Bir tomonlama):</b> Faqat mijoz serverning sertifikatini tekshiradi (masalan siz Google ni tekshirasiz). Server esa har qanday ulanishga ishonadi.",
                    "<b>Обычный TLS:</b> Только браузер проверяет сертификат сервера. Сервер же принимает любые подключения.",
                    "<b>Standard TLS:</b> Client verifies server identity. Server accepts anonymous incoming connections."),
                   ("<b>Mutual TLS (Ikki tomonlama):</b> Server ham, mijoz ham bir-biriga o'z xususiy <b>X.509 raqamli sertifikatini</b> ko'rsatadi.",
                    "<b>Mutual TLS (mTLS):</b> И клиент, и сервер обязаны предъявить взаимные криптографические сертификаты X.509.",
                    "<b>Mutual TLS (mTLS):</b> Both endpoints mandate mutual cryptographic X.509 certificate presentation."),
                   ("Ichki tarmoqqa begona hacker kirib olsa ham, uning sertifikati yo'qligi sababli <b>bitta ham mikroservis uning so'rovini qabul qilmaydi!</b>",
                    "Даже если злоумышленник внутри офиса, без персонального сертификата сервисы сбросят его запросы.",
                    "Even if an attacker breaches the internal network, missing client certificates result in immediate TCP drops."),
               ])
         + '<div class="box purple">\n'
         + el("h3", "mTLS Muloqot Sxemasi", "Схема mTLS Handshake", "mTLS Handshake Mechanics")
         + el("p", "1. <b>Mijoz:</b> <i>'Server, sertifikatingni ko'rsat!'</i><br><br>"
              "2. <b>Server:</b> Sertifikatini beradi va aytadi: <i>'Sen ham o'z sertifikatingni ko'rsat!'</i><br><br>"
              "3. <b>Mijoz:</b> O'zining kriptografik sertifikatini taqdim etadi.<br><br>"
              "4. Ikkala tomon markaziy Root CA orqali bir-birini tasdiqlagach, kanal shifrlanadi!",
              "1. <b>Клиент:</b> «Сервер, покажи сертификат!»<br><br>"
              "2. <b>Сервер:</b> «Вот мой сертификат. А теперь предъяви свой клиентский сертификат!»<br><br>"
              "3. <b>Клиент:</b> Предъявляет свой подписанный сертификат.<br><br>"
              "4. Обе стороны проверяют подписи через единый внутренний CA, после чего канал шифруется.",
              "1. <b>Client:</b> Requests server certificate validation.<br><br>"
              "2. <b>Server:</b> Serves cert and demands: <i>\"Authenticate yourself!\"</i><br><br>"
              "3. <b>Client:</b> Submits authenticated client certificate.<br><br>"
              "4. Mutually validated against enterprise Root CA before encrypted stream opens.")
         + '</div>\n</div>'
))

# 7. Real-World Case Study: Capital One Breach
S.append(slide(
    ph=("Real Keys", "Кейс из Жизни", "Case Study"), time="22–26",
    eyebrow=("80 million dollarlik IAM xatosi", "Убыток $80 млн из-за IAM", "The $80M IAM Failure"),
    title=("Capital One Kiber-Halokati: Haddan Tashqari Keng IAM Ruxsatlari",
           "Взлом Capital One: Слишком Широкие Права в IAM",
           "The Capital One Breach: Excessive IAM Permissions Disaster"),
    body='<div class="cols c2">\n'
         + box("accent", ("Nima Sodir Bo'lgan?", "Хроника Инцидента", "Incident Anatomy"),
               p=("2019-yilda xaker Paige Thompson bankning AWS bulutidagi WAF (Web Application Firewall) serveridagi SSRF zaifligi orqali ichkariga kirdi. Ammo eng katta falokat ichkarida yotardi: WAF serverining IAM roliga <b>haddan tashqari keng huquqlar (Over-privileged Role: Action: *, Resource: *)</b> berilgan edi. Natijada xaker bankning <b>106 million mijozlari kredit arizalari</b> saqlanadigan 700 dan ortiq S3 omborlarini bir zumda yuklab oldi.",
                  "В 2019 году через уязвимость SSRF хакер проникла на сервер WAF банка Capital One. Сервер имел избыточные права IAM (`Action: *`, `Resource: *`). Злоумышленница скачала 700 корзин S3 с данными 106 миллионов кредитных карт.",
                  "In 2019, an adversary leveraged an SSRF flaw on Capital One's WAF EC2 instance. The instance IAM role was over-privileged (`Action: *`, `Resource: *`). The attacker listed and dumped 700+ S3 buckets containing credit applications for 106 million customers."))
         + box("purple", ("Falokat Sabog'i: Minimal Huquq (Least Privilege)", "Урок: Принцип Наименьших Прав", "Core Lesson: Least Privilege"),
               items=[
                   ("<b>106 000 000 ta mijoz:</b> Ijtimoiy himoya raqamlari (SSN) va bank hisoblari sizib chiqdi.",
                    "<b>106 млн клиентов:</b> Утечка номеров страхования и банковских транзакций.",
                    "<b>106 million records:</b> Social Security numbers, bank accounts, and credit scores exposed."),
                   ("<b>80 000 000 dollar jarima:</b> AQSh regulyatorlari bankni IAM nazoratini yo'qotgani uchun 80 million dollar jarimaga tortdi.",
                    "<b>Штраф $80 млн:</b> Банк оштрафован за отсутствие принципа Least Privilege.",
                    "<b>$80,000,000 regulatory fine:</b> Slapped with massive fines for gross IAM governance failure."),
                   ("<b>Yechim:</b> WAF serveriga faqat tarmoqni filtrlash ruxsati berilishi kerak edi, S3 kredit ma'lumotlarini o'qish huquqi mutlaqo berilmasligi shart edi!",
                    "<b>Вывод:</b> Серверу фаервола были не нужны права на чтение всех баз клиентов!",
                    "<b>Remedy:</b> The WAF role had zero business reading customer S3 storage. Principle of Least Privilege would have isolated the blast radius to zero!"),
               ])
         + '\n</div>'
))

# 8. Interactive Studio Introduction
S.append(slide(
    ph=("Trenajyor", "Тренажёр", "Interactive Studio"), time="26–30",
    eyebrow=("Interaktiv Studio", "Интерактивная Студия", "Interactive Studio"),
    title=("Zero Trust & IAM Studio: Jonli Siyosat Simulyatori",
           "Zero Trust & IAM Studio: Интерактивный Симулятор Политик",
           "Zero Trust & IAM Studio: Live Access Gatekeeper & Sandbox"),
    body='<div class="cols c2">\n'
         + box("accent", ("1. PDP Shlyuzi (Policy Decision Point)", "1. PDP Шлюз Решений", "1. PDP Decision Gate"),
               items=[
                   ("<b>Subyektni tanlang:</b> Alice (Intern), Bob (DevOps) yoki Eve (Xaker).",
                    "<b>Выбор субъекта:</b> Алиса (стажёр), Боб (DevOps) или Ева (хакер).",
                    "<b>Select subject:</b> Alice (intern), Bob (DevOps), or Eve (adversary)."),
                   ("<b>Kontekstual signallar:</b> Qurilma holati (MacBook vs Android), IP joylashuv, Ish vaqti, MFA mavjudligi.",
                    "<b>Контекст:</b> Здоровье устройства, IP-локация, рабочее время, наличие 2FA.",
                    "<b>Contextual signals:</b> Device posture, geolocation subnet, off-hours, MFA presence."),
                   ("<b>PDP natijasi:</b> Har bir so'rov bo'yicha 5 ta tekshiruv va yakuniy <code>200 OK</code> yoki <code>403 Denied</code>.",
                    "<b>Решение:</b> Проход по 5 правилам и мгновенный вердикт 200 OK или 403 Forbidden.",
                    "<b>Instant PDP verdict:</b> 5-point evaluation pipeline yielding 200 OK or 403 Forbidden."),
               ])
         + box("green", ("2. Capital One Kiber-Poligoni (Fix the Breach)", "2. Полигон Capital One", "2. Capital One Breach Sandbox"),
               items=[
                   ("<b>Wildcard xatosini ko'ring:</b> Zaif <code>Action: *</code> va <code>Resource: *</code> siyosati.",
                    "<b>Увидьте уязвимость:</b> Опасная политика с подстановочными знаками `*`.",
                    "<b>Inspect vulnerable policy:</b> Wildcard `Action: *` and `Resource: *` flaws."),
                   ("<b>Tugmachalar bilan tuzating:</b> Action ni `s3:GetObject` ga, resursni public assets ga cheklang va MFA/IP qo'shing.",
                    "<b>Исправьте тумблерами:</b> Ограничьте права, внедрите условия MFA и IP.",
                    "<b>Harden with toggles:</b> Restrict actions, isolate credit data, enforce MFA & IP guards."),
                   ("<b>SSRF hujumini simulyatsiya qiling:</b> Xaker hujumini qaytaring va zararni 0 ga tushiring!",
                    "<b>Запустите симуляцию атаки:</b> Отразите эксплойт хакера с нулевым ущербом!",
                    "<b>Simulate exploit:</b> Thwart adversary SSRF pivoting with zero data exposure!"),
               ])
         + '\n</div>'
))

# 9. Practical Mission (12 min timer)
S.append(slide(
    ph=("Amaliyot", "Практика", "Hands-On Lab"), time="30–42",
    eyebrow=("Mustaqil laboratoriya · 12 daqiqa", "Лабораторная работа · 12 минут", "Practical Lab · 12 Minutes"),
    title=("Amaliy Topshiriq: Zero Trust IAM Siyosatini Loyihalash",
           "Практическое Задание: Проектирование Политики IAM в Студии",
           "Mission: Hardening Zero Trust IAM Policies in Studio"),
    body='<div class="cols c2">\n'
         + box("green", ("Laboratoriya Bosqichlari (Studio da)", "Шаги в Студии", "Mission Checkpoints"),
               items=[
                   ("<b>1-Kvest:</b> PDP shlyuzida Eve ning shaxsiy telefonidan tungi kirishini rad eting (403 Forbidden) — <b>+2 Ball</b>.",
                    "<b>Квест 1:</b> Заблокируйте ночную попытку Евы с не доверенного устройства — <b>+2 Балла</b>.",
                    "<b>Quest 1:</b> Block Eve's off-hours access from untrusted device — <b>+2 Pts</b>."),
                   ("<b>2-Kvest:</b> Bob ning korporativ noutbukdan MFA orqali steyjing loglarini o'qishini tasdiqlang (200 OK) — <b>+2 Ball</b>.",
                    "<b>Квест 2:</b> Одобрите легитимный доступ Боба с MFA к dev-логам — <b>+2 Балла</b>.",
                    "<b>Quest 2:</b> Validate Bob's compliant access with MFA — <b>+2 Pts</b>."),
                   ("<b>3-Kvest:</b> Capital One siyosatidagi <code>*</code> wildcard xatolarini Least Privilege ga o'tkazing — <b>+3 Ball</b>.",
                    "<b>Квест 3:</b> Устраните опасные звёздочки `*` в политике WAF роли — <b>+3 Балла</b>.",
                    "<b>Quest 3:</b> Eliminate wildcard `*` flaws in Capital One sandbox — <b>+3 Pts</b>."),
                   ("<b>4-Kvest:</b> MFA va IP shartlarini yoqib, SSRF xaker hujumini 100% qaytaring — <b>+3 Ball</b>.",
                    "<b>Квест 4:</b> Включите условия MFA и IP, отразив атаку с 0 утечек — <b>+3 Балла</b>.",
                    "<b>Quest 4:</b> Enforce MFA & IP conditions to thwart attack with 0 leaks — <b>+3 Pts</b>."),
               ])
         + box("accent", ("O'lchanadigan Natija", "Критерий Сдачи", "Deliverable Spec"),
               p=("Zero Trust & IAM Studio da 10/10 ball to'plash, ish varaqasiga xavfsiz JSON siyosatini ko'chirish va Capital One keysidagi 3 ta xatolikni yozma izohlash!",
                  "Набрать 10/10 баллов в Zero Trust Studio, зафиксировать валидный JSON в листе и объяснить 3 правила защиты кейса Capital One!",
                  "Achieve 10/10 pts in Zero Trust Studio, author production-ready JSON policy on worksheet, and justify the 3 mitigation gates!"))
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
                   ("Zero Trust Studio da 10/10 ball to'plangan.", "В Zero Trust Studio набрано 10/10 баллов.", "10/10 points achieved in Zero Trust Studio."),
                   ("RBAC vs ABAC va mTLS farqi to'g'ri ko'rsatilgan.", "Разница RBAC/ABAC и mTLS обоснована верно.", "RBAC vs ABAC & mTLS justifications accurate."),
                   ("Varaqa 100% to'ldirilgan.", "Рабочий лист заполнен на 100%.", "Worksheet completed 100%."),
               ])
         + box("", ("Yaxshi (7–8 Ball)", "Хорошо (7–8)", "Proficient (7–8)"),
               items=[
                   ("IAM siyosatida kichik kamchilik bor, lekin xavfsiz.", "В политике IAM мелкие недочёты, но она безопасна.", "IAM policy functional with minor scope oversights."),
                   ("Zero Trust g'oyasi tushunilgan.", "Концепция Zero Trust усвоена.", "Zero Trust paradigm understood."),
                   ("Studio da 7-8 ball to'plangan.", "В Studio набрано 7-8 баллов.", "7-8 points achieved in Studio."),
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
               p=("Zero Trust — bu bitta dastur yoki qurilma emas, balki korporativ arxitektura tamoyilidir. Identifikatsiyani doimiy tekshirish, huquqlarni minimal darajada cheklash (Least Privilege) va har bir so'rovni dushman deb hisoblash (Assume Breach) har qanday kiber-buzilishning oqibatlarini nolga tenglashtiradi.",
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
                   ("<b>Keyingi Dars:</b> 23-dars: API Xavfsizligi va Rate Limiting (Token Bucket, DDoS va HMAC).",
                    "<b>Следующий Урок:</b> Урок 23: Безопасность API и Rate Limiting (Token Bucket, DDoS и HMAC).",
                    "<b>Next Session:</b> Lesson 23: API Security & Rate Limiting (Token Bucket, DDoS & HMAC)."),
               ])
         + '\n</div>'
))

# Teacher Notes
N_UZ = [
    ["Kirish", "Darsni boshlash: Zero Trust va IAM. Nega eski perimetr mudofaasi o'ldi?", "Slaydni oching, bulutli texnologiyalar davrida VPN ning nima uchun yetarli emasligini tushuntiring."],
    ["Paradigma", "Qasr vs Aeroport modeli. Ichki tarmoqqa ishonish halokati va lateral movement xavfi.", "Aeroportda har bir darvoza va uchuvchi kabinasi alohida tekshirilishi kabi analogiyani bering."],
    ["Asosiy Ustunlar", "Zero Trust ning 3 ta asosiy qoidasi: Verify Explicitly, Least Privilege, Assume Breach.", "NIST SP 800-207 standartini tanishtiring."],
    ["Ruxsat Nazorati", "RBAC va ABAC solishtirmasi. Nega katta tizimlarda dinamik atributlar (ABAC) kerak?", "Doskaga 4 ta atribut guruhini (Subyekt, Resurs, Amal, Muhit) yozib ko'rsating."],
    ["Kod Sifatida Siyosat", "IAM JSON siyosati. Effect, Action, Resource, Condition maydonlari.", "Ekranda AWS IAM siyosati strukturasini tahlil qiling."],
    ["mTLS Mudofaasi", "Mutual TLS nima? Mikroservislar bir-birining sertifikatini qanday tekshiradi?", "TLS va mTLS dialogini o'quvchilar bilan birga o'qing."],
    ["Real Keys", "Capital One kiber-halokati. Haddan tashqari keng IAM huquqlari tufayli 80 million dollar jarima.", "SSRF orqali kirib S3 larni o'g'irlash keysini tahlil qiling."],
    ["Trenajyor", "Zero Trust & IAM Studio bilan tanishuv. PDP shlyuzi va Capital One kiber-poligoni.", "Brauzerda Studio ochilishini ko'rsating."],
    ["Amaliyot", "12 daqiqalik laboratoriya. O'quvchilar Studio da 4 ta kvestni bajarib 10 ball oladilar.", "Taymerni yoqing (12 daqiqa), o'quvchilar natijalarini kuzating."],
    ["Tekshirish", "Nazorat tekshiruvi. Yulduzchalar yo'qligini va MFA shartini tekshirish.", "JSON sintaksisini tekshiring."],
    ["Mezon", "10 ballik baholash mezoni tushuntiriladi.", "Talablarni e'lon qiling."],
    ["Xulosa", "Dars yakuni va uy vazifasi. Kelgusi darsda API Xavfsizligi va Rate Limiting ni o'rganamiz.", "Varaqalarni yig'ing."]
]

N_RU = [
    ["Введение", "Старт урока: Архитектура Zero Trust и IAM в корпоративных системах.", "Откройте слайд, объясните смену парадигмы безопасности."],
    ["Парадигма", "Смерть периметра: почему концепция «Замка со рвом» уступила место парадигме аэропорта.", "Объясните опасность бокового перемещения хакера (Lateral Movement)."],
    ["Столпы Zero Trust", "3 принципа NIST SP 800-207: явная проверка, минимум прав, допущение взлома.", "Разберите каждый постулат с точки зрения архитектуры."],
    ["Контроль Доступа", "RBAC против ABAC: переход от статичных ролей к контекстным атрибутам.", "Покажите проблему Role Explosion."],
    ["Политики как Код", "Анатомия политик IAM в формате JSON: Effect, Action, Resource, Condition.", "Покажите боевой JSON с ограничением по IP и MFA."],
    ["mTLS Защита", "Взаимный TLS (mTLS): двусторонняя проверка подлинности микросервисов.", "Сравните классический TLS и mTLS."],
    ["Кейс из Жизни", "Кейс Capital One: $80 млн штрафа за избыточные права IAM у роли WAF.", "Разберите хронологию масштабной утечки данных."],
    ["Тренажёр", "Знакомство с Zero Trust & IAM Studio: шлюз PDP и песочница Capital One.", "Продемонстрируйте студию в браузере."],
    ["Практика", "12 минут практики: прохождение 4 квестов в Studio и получение 10 баллов.", "Запустите таймер, помогайте с директивами."],
    ["Проверка", "Чек-лист проверки: убедитесь в отсутствии `*` и наличии условий MFA.", "Проверьте вывод политик учащихся."],
    ["Критерии", "10-балльная шкала оценивания практической работы.", "Озвучьте критерии оценки."],
    ["Итоги", "Завершение урока и домашнее задание. На следующем занятии — безопасность API и Rate Limiting.", "Соберите рабочие листы."]
]

N_EN = [
    ["Intro", "Lesson opening: Zero Trust Architecture & enterprise IAM governance.", "Frame the systemic shift in security philosophy."],
    ["Paradigm Shift", "The collapse of castle-and-moat perimeter defense and the airport analogy.", "Illustrate lateral movement risks."],
    ["Core Pillars", "The 3 NIST SP 800-207 pillars: Verify explicitly, least privilege, assume breach.", "Explain defense-in-depth principles."],
    ["Access Control", "RBAC vs dynamic ABAC: Resolving the enterprise role explosion trap.", "Contrast static role assignments with dynamic context evaluation."],
    ["Policy-as-Code", "Deconstructing JSON IAM declarations: Effect, Action, Resource, and Conditions.", "Walk through real-world IAM definitions."],
    ["Mutual TLS", "Mutual TLS (mTLS) zero-trust microservice communication.", "Diagram mutual X.509 handshake attestation."],
    ["Case Study", "The Capital One catastrophe: An over-privileged WAF role triggering $80M in penalties.", "Analyze the blast radius of unsegmented permissions."],
    ["Interactive Studio", "Introducing Zero Trust & IAM Studio: PDP Decision Gate & Capital One Sandbox.", "Open the browser playground."],
    ["Hands-On Lab", "12-minute lab: Completing 4 quests in Studio for 10 points.", "Start 12-minute countdown timer and provide feedback."],
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
    h=("Laboratoriya Vazifasi: Zero Trust & IAM Studio Orqali Siyosatni Loyihalash",
       "Миссия Лабораторной: Проектирование Политики Zero Trust в Studio",
       "Lab Mission: Engineering Zero Trust Policies in Studio"),
    p=("Zero Trust & IAM Studio trenajyori yordamida PDP shlyuzini sinovdan o'tkazish, "
       "Capital One $80M kiber-halokatiga sabab bo'lgan wildcard `*` xatolarini bartaraf etish "
       "va xavfsiz JSON siyosatini shakllantirib, 4 ta kvest bo'yicha 10/10 ball to'plash.",
       "Протестировать шлюз решений PDP в Zero Trust Studio, устранить опасные подстановочные знаки `*` "
       "из кейса Capital One на $80 млн и набрать 10/10 баллов по 4 практическим квестам.",
       "Leverage interactive Zero Trust & IAM Studio to test the PDP gate, eliminate dangerous wildcard `*` "
       "flaws from the $80M Capital One catastrophe, and score 10/10 points across 4 practical quests."))
)

V.append(table(
    headers=[
        ("Me'moriy Qatlam", "Уровень Архитектуры", "Architecture Layer"),
        ("Eski Model (Qasr va Xandak)", "Старый Подход (Периметр)", "Legacy Castle-and-Moat"),
        ("Zero Trust Standarti", "Стандарт Zero Trust", "Zero Trust Standard"),
        ("Studio Natijasi", "Результат в Studio", "Studio Finding")
    ],
    rows=[
        [("1. Tarmoq Ishonchi", "1. Доверие Сети", "1. Network Trust"),
         ("VPN ichidagi barcha qurilmalar ishonchli", "Внутренний трафик VPN доверенный", "Implicit trust inside VPN perimeter"),
         ("Har bir so'rov dushman deb tekshiriladi", "Каждый запрос строго проверяется", "Zero implicit trust; continuous checks"),
         ("✅ 403 Forbidden (Eve bloklandi)", "✅ 403 Forbidden (Ева блокирована)", "✅ 403 Forbidden (Eve Blocked)")],
        [("2. Ruxsat Modeli", "2. Модель Доступа", "2. Authorization"),
         ("Statik rollar (`Admin`, `User`)", "Статичные роли (Role Explosion)", "Coarse static roles (RBAC)"),
         ("Dinamik kontekstual ABAC siyosati", "Динамический контекстный ABAC", "Contextual attribute policies (ABAC)"),
         ("✅ 4 ta atribut tahlili", "✅ Оценка 4 атрибутов", "✅ 4 Attributes Evaluated")],
        [("3. Mikroservislar", "3. Микросервисы", "3. Microservices"),
         ("Ochiq HTTP / Bir tomonlama TLS", "Открытый HTTP внутри кластера", "Plaintext HTTP across private cluster"),
         ("Ikki tomonlama shifrlangan mTLS", "Взаимный mTLS с сертификатами", "Mutual TLS (mTLS) with strict certs"),
         ("✅ X.509 sertifikat tekshiruvi", "✅ Проверка X.509", "✅ X.509 Validated")],
        [("4. Imtiyoz Muddati", "4. Срок Привилегий", "4. Privilege Lifetime"),
         ("Doimiy ochiq admin huquqlari", "Постоянные права администратора", "Standing perpetual admin rights"),
         ("Just-In-Time (JIT) vaqtinchalik ruxsat", "Временный доступ по запросу (JIT)", "Just-In-Time (JIT) ephemeral access"),
         ("✅ Zarar radiusi = 0", "✅ Радиус ущерба = 0", "✅ Zero Blast Radius")],
    ]
))

V.append(sheet_box(
    h=("Xavfsizlik Tahlili va Texnik Savollar", "Анализ Безопасности и Вопросы", "Architectural Analysis & Written Queries"),
    body_html=writelines(3, label=("1. Nega korporativ siyosatda 'Action: *' va 'Resource: *' yozish Capital One fojiasiga ($80M jarima) olib keldi? Least Privilege qanday himoya beradi?",
                                   "1. Почему использование 'Action: *' и 'Resource: *' в IAM привело к катастрофе Capital One ($80 млн)? Как Least Privilege защищает систему?",
                                   "1. Why did authoring 'Action: *' and 'Resource: *' trigger the Capital One $80M disaster? How does Least Privilege constrain blast radius?"))
             + "<br>"
             + writelines(3, label=("2. Aeroport xavfsizligi analogiyasi orqali Zero Trust ning 3 ta asosiy qoidasini (Verify Explicitly, Least Privilege, Assume Breach) izohlang:",
                                   "2. На аналогии безопасности аэропорта объясните 3 главных принципа Zero Trust (явная проверка, минимум прав, допущение взлома):",
                                   "2. Using the airport security analogy, explain the 3 core tenets of Zero Trust (Verify Explicitly, Least Privilege, Assume Breach):"))
))

V.append(sheet_box(
    h=("Baholash Mezoni (10 Ball)", "Критерии Оценки (10 Баллов)", "Grading Rubric (10 Points)"),
    body_html=rubric([
        (("Zero Trust tamoyillari va aeroport modeli to'liq tushuntirilgan", "Принципы Zero Trust и модель аэропорта разобраны верно", "Zero Trust tenets & airport analogy mastered"), "3 ball"),
        (("Zero Trust Studio da 4 ta kvest to'liq bajarilgan (10/10 ball)", "В Zero Trust Studio выполнены все 4 квеста (10/10)", "All 4 quests completed in Zero Trust Studio (10/10)"), "3 ball"),
        (("Capital One keysidagi wildcard xatosi va mTLS arxitekturasi aniq asoslangan", "Разобраны кейс Capital One и архитектура mTLS", "Capital One wildcard flaw & mTLS architecture justified"), "2 ball"),
        (("Varaqadagi texnik savollarga to'liq va asosli javob berilgan", "Даны развернутые ответы на технические вопросы", "Written technical queries thoroughly answered"), "2 ball"),
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
