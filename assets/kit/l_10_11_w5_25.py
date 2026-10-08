# -*- coding: utf-8 -*-
"""10-11-sinf · 5-hafta · 25-dars — SOC Simulyatsiyasi va Kiber-Insident Boshqaruvi: SIEM, Sigma Qoidalari, MTTR va Post-Mortem."""

import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from build import (Lesson, slide, title_slide, box, code, el, i18n,
                   sheet_header, mission, table, sheet_box, rubric, writelines, sign_box)

D = "classes/10-11-sinf/5-hafta/25-dars-soc-simulyatsiyasi-va-insident-boshqaruvi"

TITLES = {
    "uz": "25-dars: SOC Simulyatsiyasi — SIEM, Sigma Qoidalari, MTTR va Post-Mortem",
    "ru": "Урок 25: Симуляция SOC — SIEM, Правила Sigma, MTTR и Постмортем",
    "en": "Lesson 25: SOC Simulation — SIEM Analytics, Sigma Rules, MTTR & Incident Post-Mortem",
}
SHEET_TITLES = {k: v + (" — Ish Varaqasi" if k == "uz" else
                        " — Рабочий Лист" if k == "ru" else " — Worksheet")
                for k, v in TITLES.items()}

S = []

# 1. Title Slide
S.append(title_slide(
    ph=("Kirish", "Введение", "Intro"), time="0–3",
    eyebrow=("CyberSecurity · 25-dars · 10–11-sinf (Enterprise SOC & Incident Response)",
             "CyberSecurity · Урок 25 · 10–11 класс (Enterprise SOC & Incident Response)",
             "CyberSecurity · Lesson 25 · Grades 10–11 (Enterprise SOC & Incident Response)"),
    h1=("SOC Simulyatsiyasi va Kiber-Insident Boshqaruvi",
        "Симуляция SOC и Управление Киберинцидентами",
        "SOC Simulation & Enterprise Incident Response"),
    lede=("Kiberxavfsizlikda eng qimmatli resurs — bu <b>vaqt</b>. Katta kompaniyalar tizimiga buzg'unchi kirib olgandan so'ng, "
          "uni aniqlash uchun o'rtacha 200 kundan ortiq vaqt ketadi (Dwell Time). "
          "<b>SOC (Security Operations Center)</b> — bu tashkilotning 24/7 kiber-qalqoni bo'lib, millionlab loglar ichidan "
          "haqiqiy xavf signallarini sekundlar ichida ajratib oladi va hujumni bartaraf etadi. "
          "Bugungi darsda siz <b>SIEM / SOAR</b> arxitekturasi, <b>Sigma qoidalari</b> yozish, "
          "<b>NIST SP 800-61</b> bo'yicha insidentlarni bartaraf qilish va kiber-halokatlardan so'ng professional <b>Post-Mortem</b> "
          "tahlilini o'tkazishni amalda o'rganasiz.",
          "В кибербезопасности решающий фактор — <b>время реакции</b>. По мировой статистике, хакер находится в корпоративной сети "
          "в среднем более 200 дней (Dwell Time) до первого обнаружения. "
          "<b>SOC (Security Operations Center)</b> — это круглосуточный центр мониторинга, обрабатывающий миллионы событий в секунду (EPS) "
          "через системы <b>SIEM и SOAR</b>. Сегодня вы научитесь писать правила обнаружения <b>Sigma</b>, управлять инцидентами "
          "по регламенту <b>NIST SP 800-61</b>, снижать метрику <b>MTTR</b> и оформлять инженерный <b>Post-Mortem</b>.",
          "In cybersecurity engineering, the ultimate battleground is <b>dwell time</b>. Global telemetry reveals adversaries "
          "persist within compromised corporate perimeters for an average of over 200 days before initial detection. "
          "A modern <b>SOC (Security Operations Center)</b> operates as a 24/7 detection nexus correlating millions of event logs per second (EPS) "
          "via <b>SIEM & SOAR</b> pipelines. Today you master vendor-agnostic <b>Sigma detection engineering</b>, "
          "<b>NIST SP 800-61</b> incident containment workflows, aggressive <b>MTTD/MTTR</b> optimization, and blameless <b>Post-Mortem</b> root cause analysis."),
    meta=[("<b>Fan:</b> Kiberxavfsizlik · SOC va Insident Boshqaruvi",
           "<b>Предмет:</b> Кибербезопасность · SOC и Реагирование на Инциденты",
           "<b>Subject:</b> CyberSecurity · Enterprise SOC & Incident Response"),
          ("<b>Kohorta:</b> 10-11-sinf Kiber-Muhandis",
           "<b>Когорта:</b> 10-11 класс Инженер Безопасности",
           "<b>Cohort:</b> Grade 10-11 Security Engineer"),
          ("<b>Hafta:</b> 5 (5-soat)", "<b>Неделя:</b> 5 (5-й час)", "<b>Week:</b> 5 (Hour 5)")],
))

# 2. SOC Architecture & Tier Hierarchy
S.append(slide(
    ph=("Arxitektura", "Архитектура", "Architecture"), time="3–7",
    eyebrow=("Tashkiliy tuzilma", "Организационная структура", "Operational Hierarchy"),
    title=("Zamonaviy SOC Qanday Ishlaydi? Tier 1, 2 va 3 Rollari",
           "Как Устроен Современный SOC? Уровни Tier 1, 2 и 3",
           "Inside Modern SOC Operations: Tier 1, 2 & 3 Hierarchies"),
    body=table(
        headers=[("SOC Bosqichi (Tier)", "Уровень (Tier)", "SOC Tier"),
                 ("Asosiy Mas'uliyati", "Ключевая Ответственность", "Primary Responsibilities"),
                 ("Foydalanadigan Asboblari", "Рабочие Инструменты", "Toolchain Stack"),
                 ("Muvaffaqiyat Mezoni (KPI)", "Ключевые Метрики", "Key Performance Indicator")],
        rows=[
            [("<b>Tier 1: Triage Analyst</b><br>(Birlamchi saralash)", "<b>Tier 1: Triage Аналитик</b>", "<b>Tier 1: Alert Triage Analyst</b>"),
             ("SIEM dan kelayotgan signallarni (Alerts) tekshirish, soxta signallarni (False Positives) elash va haqiqiy xavfni keyingi bosqichga uzatish.",
              "Круглосуточный мониторинг тревог SIEM, отсев ложных срабатываний и эскалация критических инцидентов.",
              "24/7 queue triage, triaging SIEM alerts, discarding false positives, escalating confirmed anomalies."),
             ("Wazuh, Splunk, Elastic SIEM, TheHive chipta tizimi.",
              "Wazuh, Splunk, Elastic SIEM, TheHive, Jira Service Desk.",
              "Elastic SIEM, Splunk, Wazuh, TheHive, ticketing consoles."),
             ("<b>MTTA &lt; 5 daqiqa:</b> Har bir signalni tezda ko'rib chiqish.",
              "<b>MTTA &lt; 5 минут:</b> Время первой реакции на тревогу.",
              "<b>MTTA &lt; 5 min:</b> Mean Time to Acknowledge.")],
            [("<b>Tier 2: Incident Responder</b><br>(Insident bartarafchisi)", "<b>Tier 2: Incident Responder</b>", "<b>Tier 2: Incident Responder</b>"),
             ("Buzilgan kompyuterni tarmoqdan uzish (Isolation), zararli fayllarni o'chirish, hujum ildizini yo'qotish va tizimni tiklash.",
              "Глубокий анализ инцидента, изоляция хостов, удаление вредоносного ПО и восстановление сервисов.",
              "Deep incident triage, host network isolation, payload eradication, credential revocation, recovery."),
             ("EDR (CrowdStrike, SentinelOne), Wireshark, Memory dump tahlili.",
              "EDR (SentinelOne, Falcon), Volatility, Wireshark, Bash/PowerShell.",
              "Enterprise EDR, Volatility memory analysis, Wireshark, forensic tools."),
             ("<b>MTTR &lt; 30 daqiqa:</b> Hujumni to'liq to'xtatish va tozalash.",
              "<b>MTTR &lt; 30 минут:</b> Время полной ликвидации угрозы.",
              "<b>MTTR &lt; 30 min:</b> Mean Time to Remediate.")],
            [("<b>Tier 3: Threat Hunter</b><br>(Kiber-Ovchi muhandis)", "<b>Tier 3: Threat Hunter</b>", "<b>Tier 3: Threat Hunter & Forensics</b>"),
             ("Signal bermagan yashirin dushmanlarni proaktiv izlash, yangi Sigma/YARA qoidalarini yozish, kiber-razvedka (CTI).",
              "Проактивный поиск скрытых угроз без алертов, разработка правил Sigma, обратная разработка малвари.",
              "Proactive threat hunting without prior alerts, authoring Sigma/YARA rules, malware reverse-engineering."),
             ("Ghidra, IDA Pro, MISP (Threat Intel), MITRE ATT&CK.",
              "Ghidra, IDA Pro, MISP, Jupyter Notebooks, ATT&CK Navigator.",
              "Ghidra, YARA, MISP threat feeds, ATT&CK matrices, Python."),
             ("<b>Dwell Time 0 kun:</b> Buzg'unchiga imkon bermaslik.",
              "<b>Dwell Time &rarr; 0:</b> Сведение времени присутствия к нулю.",
              "<b>Dwell Time &rarr; 0:</b> Eliminating persistence windows.")]
        ]
    )
))

# 3. SIEM & Log Telemetry Pipeline
S.append(slide(
    ph=("Telemetriya", "Телеметрия", "Telemetry Architecture"), time="7–11",
    eyebrow=("Log yig'ish va tahlil", "Сбор и анализ логов", "Log Pipeline"),
    title=("SIEM Arxitekturasi: Millionlab Loglarni Sekundda Qanday Tahlil Qiladi?",
           "Архитектура SIEM: Корреляция Миллионов Событий в Секунду",
           "SIEM Pipeline: Ingestion, Normalization & Correlation at Scale"),
    body='<div class="cols">\n'
         + box("blue", ("1. Telemetriya Manbalari (Event Ingestion)", "1. Источники Телеметрии", "1. Telemetry Sources"),
               items=[
                   ("<b>Serverlar:</b> Linux <code>auditd</code>, <code>auth.log</code>, Windows Event Log (Sysmon ID 1 - Process, ID 3 - Network).",
                    "<b>Серверы:</b> Журналы Linux auditd, Windows Event Log (Sysmon ID 1, 3).",
                    "<b>Host Telemetry:</b> Linux auditd, syslog, Windows Event Log (Sysmon Process & Network events)."),
                   ("<b>Tarmoq qurilmalari:</b> Firewall (UFW, Palo Alto), VPN gateway, DNS so'rovlar jurnali.",
                    "<b>Сетевые шлюзы:</b> Межсетевые экраны, логи VPN, DNS-запросы и прокси.",
                    "<b>Perimeter Telemetry:</b> Next-Gen Firewalls, VPN logs, DNS resolution records, proxy streams."),
                   ("<b>Ilovalar:</b> Nginx/Apache kirish loglari, ma'lumotlar bazasi audit loglari, CloudTrail.",
                    "<b>Приложения:</b> HTTP-логи веб-серверов, журналы БД, AWS CloudTrail.",
                    "<b>Application Telemetry:</b> Ingress access logs, database query audits, AWS CloudTrail.")
               ])
         + box("purple", ("2. Korrelyatsiya Mantiqi (Correlation Engine)", "2. Движок Корреляции", "2. Correlation Engine"),
               items=[
                   ("Bitta ajratilgan log xavfli ko'rinmasligi mumkin (masalan 1 ta parolni noto'g'ri terish).",
                    "Одиночный лог невинен (например, опечатка в пароле сотрудника).",
                    "An isolated log entry appears benign (e.g. single failed login attempt)."),
                   ("<b>Korrelyatsiya Qoidasi:</b> <i>'Agar 1 daqiqada 50 marta xato login kelsa VA keyin muvaffaqiyatli login bo'lsa VA darhol <code>powershell.exe</code> ochilsa'</i> &rarr; <b>KRITIK OGOHLANTIRISH!</b>",
                    "<b>Правило корреляции:</b> 50 сбоев пароля + 1 успех + немедленный запуск PowerShell = Критическая тревога!",
                    "<b>Correlation logic:</b> 50 failed logins + 1 success + immediate PowerShell execution = High Severity Incident!"),
                   ("Oddiy ma'lumotlar oqimi bir zumda <b>Kiber-Hujum Tarixiga (Timeline)</b> aylanadi!",
                    "Разрозненные строки превращаются в ясный хронологический таймлайн атаки.",
                    "Isolated noise transforms into a coherent chronological attack timeline!")
               ])
         + '</div>'
))

# 4. Detection Engineering: Sigma Rules
S.append(slide(
    ph=("Qoidalar", "Детекция", "Detection Rules"), time="11–15",
    eyebrow=("Sigma standarti", "Индустриальный стандарт Sigma", "Sigma Standard"),
    title=("Sigma Qoidalari: Har Qanday SIEM Uchun Universal Detektor",
           "Правила Sigma: Универсальный Детектор для Любой SIEM",
           "Sigma Rules: The Universal Detection Standard for Enterprise SIEM"),
    body='<div class="cols">\n'
         + box("navy", ("Sigma Nima va Nega U Standart?", "Что Такое Sigma?", "Why Sigma Rules Dominate"),
               items=[
                   ("Dasturchilar uchun Git qanday bo'lsa, xavfsizlik muhandislari uchun <b>Sigma</b> shunday umumiy standartdir.",
                    "Sigma — это как Markdown или YARA для журналов событий: универсальный формат описания сигнатур.",
                    "Sigma serves as the open-source YAML standard for log signatures across security vendors."),
                   ("Sigma qoidasi YAML formatida yoziladi va <code>sigmac</code> konverteri orqali Splunk, Elastic, Wazuh yoki QRadar so'rovlariga avtomatik o'giriladi.",
                    "Одно правило на YAML автоматически компилируется в запросы для Splunk, Elasticsearch или QRadar.",
                    "A single YAML file compiles seamlessly into Splunk SPL, Elastic Lucene, or SQL queries."),
                   ("Kompaniya SIEM tizimini o'zgartirsa ham, yozilgan 1000 ta xavfsizlik qoidasi zoe ketmaydi!",
                    "При смене SIEM компании не нужно переписывать заново тысячи правил обнаружения.",
                    "Vendor independence: detection logic remains preserved even when migrating SIEM engines.")
               ])
         + box("green", ("Sigma Qoidasi Tuzilmasi", "Структура Правила Sigma", "Core Sigma Architecture"),
               items=[
                   ("<b>Title & ID:</b> Qoidaning nomi va unikal UUID kodi.",
                    "<b>Title / ID:</b> Уникальный идентификатор и название правила.",
                    "<b>Title & UUID:</b> Unique identification and descriptive metadata."),
                   ("<b>Logsource:</b> Qaysi log tekshiriladi (Linux, Windows Sysmon, Web).",
                    "<b>Logsource:</b> Источник данных (category: process_creation).",
                    "<b>Logsource:</b> Target log telemetry category and operating system."),
                   ("<b>Detection:</b> Filtrlash shartlari (Selection, Filter, Condition).",
                    "<b>Detection:</b> Селекторы, условия поиска и булева логика.",
                    "<b>Detection:</b> Selection primitives, filter exclusions, and boolean conditions."),
                   ("<b>Tags:</b> MITRE ATT&CK texnika kodi (masalan: <code>attack.t1059</code>).",
                    "<b>Tags:</b> Привязка к техникам матрицы MITRE ATT&CK.",
                    "<b>Tags:</b> Formal tagging to MITRE ATT&CK techniques.")
               ])
         + '</div>'
))

# 5. Code Dissection: Production Sigma Rule in YAML
S.append(slide(
    ph=("Kod Tahlili", "Анализ Кода", "Code Dissection"), time="15–18",
    eyebrow=("Detektor kodi", "Код сигнатуры детекции", "Sigma Implementation"),
    title=("Linux da Shubhali 'whoami' va 'sudo' Harakatini Aniqlash",
           "Реализация Правила Sigma для Детекции Эскалации Прав",
           "Production Sigma Rule: Detecting Web Shell Privilege Escalation"),
    body=code("""title: Suspicious Web Server Shell Spawn & Privilege Escalation
id: 7c4b8e91-34a2-4a11-8f55-091a92bf6c22
status: production
description: Detects execution of privilege reconnaissance commands by www-data
author: Target Cybersecurity Team
references:
    - https://attack.mitre.org/techniques/T1059/004/
tags:
    - attack.execution
    - attack.privilege_escalation
    - attack.t1059.004
logsource:
    category: process_creation
    product: linux
detection:
    selection_parent:
        ParentImage|endswith:
            - '/nginx'
            - '/apache2'
            - '/php-fpm'
    selection_cmd:
        Image|endswith:
            - '/whoami'
            - '/id'
            - '/sudo'
            - '/bash'
    condition: selection_parent and selection_cmd
fields:
    - User
    - Image
    - CommandLine
    - ParentImage
falsepositives:
    - Legitimate automated maintenance scripts (audit required)
level: high""")
))

# 6. Incident Response Lifecycle: NIST SP 800-61
S.append(slide(
    ph=("Jarayon", "Процедура", "Incident Response"), time="18–22",
    eyebrow=("NIST SP 800-61 standarti", "Стандарт NIST SP 800-61", "NIST SP 800-61 Standard"),
    title=("Kiber-Insident Bosqichlari: Hujum Paytida Nima Qilinadi?",
           "Жизненный Цикл Реагирования на Инциденты (NIST)",
           "The 4 Phases of Incident Response (NIST SP 800-61 Lifecycle)"),
    body='<div class="cols">\n'
         + box("blue", ("1. Tayyorgarlik va Aniqlash (Prep & Detect)", "1. Подготовка и Обнаружение", "1. Preparation & Detection"),
               items=[
                   ("<b>Preparation:</b> Xodimlarni o'qitish, zaxira nusxalar (Backups), EDR o'rnatish, aloqa rejasini tuzish.",
                    "<b>Подготовка:</b> Создание бэкапов, настройка EDR, регламенты оповещения руководства.",
                    "<b>Preparation:</b> Offline backups, deployed EDR agents, communication channels."),
                   ("<b>Detection & Analysis:</b> SIEM signali orqali hujum ko'lamini (Scope) va jiddiyligini (Severity) aniqlash.",
                    "<b>Обнаружение и анализ:</b> Определение масштаба вторжения и критичности скомпрометированных хостов.",
                    "<b>Detection & Analysis:</b> Confirming compromise, determining blast radius and attack vector.")
               ])
         + box("red", ("2. Lokallashtirish va Tiklash (Contain & Recover)", "2. Локализация и Восстановление", "2. Containment & Recovery"),
               items=[
                   ("<b>Containment (Lokallashtirish):</b> Zararlangan serverni tarmoqdan uzish (Host Isolation), sessiyalarni bekor qilish.",
                    "<b>Локализация:</b> Немедленная изоляция хоста от сети, сброс скомпрометированных паролей и API-токенов.",
                    "<b>Containment:</b> Immediate network isolation, disabling compromised service accounts."),
                   ("<b>Eradication & Recovery:</b> Xakerning troyan va webshell fayllarini tozalash, xavfsiz zaxiradan tiklash va monitoringni kuchaytirish.",
                    "<b>Ликвидация и возврат:</b> Удаление бэкдоров, патчинг уязвимостей, восстановление из чистых бэкапов.",
                    "<b>Eradication & Recovery:</b> Eradicating persistence artifacts, patching exploits, system restore.")
               ])
         + '</div>'
))

# 7. Incident Metrics: MTTD vs MTTR
S.append(slide(
    ph=("Metrikalar", "Метрики", "SOC Metrics"), time="22–26",
    eyebrow=("Samaradorlik ko'rsatkichlari", "Показатели эффективности", "Performance Benchmarks"),
    title=("SOC Samaradorligi: MTTD, MTTA va MTTR Metriklari",
           "Метрики SOC: MTTD, MTTA и MTTR в Секундах",
           "Quantifying SOC Speed: MTTD, MTTA and MTTR Benchmarks"),
    body=table(
        headers=[("Metrika", "Метрика", "Metric"),
                 ("To'liq Nomi", "Расшифровка", "Definition"),
                 ("Sanoatdagi Yomon Ko'rsatkich", "Опасный Уровень", "Industry Failure Level"),
                 ("World-Class SOC Maqsadi", "Целевой Эталон", "Elite Benchmark Target")],
        rows=[
            [("<b>MTTD</b>", "<b>MTTD</b>", "<b>MTTD</b>"),
             ("Mean Time to Detect (Hujumni aniqlash uchun ketgan o'rtacha vaqt).",
              "Среднее время от проникновения хакера до первого срабатывания алерта.",
              "Mean Time to Detect (elapsed duration from compromise to alert)."),
             ("<b>&gt; 90 kun</b> (Buzg'unchi barcha sirlarni o'g'irlab ulguradi).",
              "<b>&gt; 90 дней</b> (полный перехват инфраструктуры злоумышленником).",
              "<b>&gt; 90 days</b> (adversary has exfiltrated all data)."),
             ("<b>&lt; 15 daqiqa:</b> SIEM va EDR yordamida tezkor aniqlash.",
              "<b>&lt; 15 минут</b> благодаря автоматическим правилам корреляции.",
              "<b>&lt; 15 minutes:</b> Near real-time automated correlation.")],
            [("<b>MTTA</b>", "<b>MTTA</b>", "<b>MTTA</b>"),
             ("Mean Time to Acknowledge (Signalga Tier 1 xodimi javob berish vaqti).",
              "Время от генерации тревоги до взятия её аналитиком в работу.",
              "Mean Time to Acknowledge (queue latency to analyst ownership)."),
             ("<b>&gt; 4 soat</b> (Alert Fatigue — xodimlar signallarga e'tibor bermaydi).",
              "<b>&gt; 4 часов</b> (синдром усталости от бесконечных ложных алертов).",
              "<b>&gt; 4 hours</b> (alert fatigue backlog symptom)."),
             ("<b>&lt; 3 daqiqa:</b> Avtomatlashtirilgan SOAR playbooklari orqali.",
              "<b>&lt; 3 минут</b> благодаря авто-обогащению контекста в SOAR.",
              "<b>&lt; 3 minutes:</b> Enriched by automated SOAR workflows.")],
            [("<b>MTTR</b>", "<b>MTTR</b>", "<b>MTTR</b>"),
             ("Mean Time to Respond / Remediate (Hujumni to'liq bartaraf etish vaqti).",
              "Время от подтверждения атаки до полной изоляции и ликвидации угрозы.",
              "Mean Time to Remediate (elapsed duration to full eradication)."),
             ("<b>&gt; 30 kun</b> (Katta moliyaviy yo'qotish va jarimalar).",
              "<b>&gt; 30 дней</b> (огромные штрафы регуляторов и простой бизнеса).",
              "<b>&gt; 30 days</b> (crippling business disruption and regulatory fines)."),
             ("<b>&lt; 60 daqiqa:</b> Tarmoqni zudlik bilan izolyatsiya qilish.",
              "<b>&lt; 60 минут</b> для полной локализации скомпрометированного сегмента.",
              "<b>&lt; 60 minutes:</b> Automated containment and segmented isolation.")]
        ]
    )
))

# 8. Real World Case Study: CrowdStrike Falcon Outage (July 2024)
S.append(slide(
    ph=("Keyslar", "Кейсы", "Case Studies"), time="26–30",
    eyebrow=("Tarixdagi eng yirik IT halokat", "Крупнейший IT-сбой в истории", "Global Resilience Case"),
    title=("CrowdStrike 2024 Falokati: 8.5 Million Kompyuterning Yiqilishi",
           "Инцидент CrowdStrike 2024: Падение 8.5 Миллионов Компьютеров",
           "The CrowdStrike Falcon Global Outage: 8.5M Hosts Crashed"),
    body='<div class="cols">\n'
         + box("red", ("Hodisa Sababi: Yadro Qatlami (Kernel Ring 0) Xatosi", "Причина: Ошибка на Уровне Ядра (Ring 0)", "Root Cause: Kernel-Level Driver Fault"),
               items=[
                   ("<b>19-iyul, 2024-yil:</b> Dunyodagi eng nufuzli kiberxavfsizlik kompaniyasi CrowdStrike o'zining Falcon EDR agenti uchun Channel File 291 yangilanishini chiqardi.",
                    "19 июля 2024: CrowdStrike выпустила обновление правил для EDR-агента Falcon.",
                    "July 19, 2024: CrowdStrike released configuration update Channel File 291 for its Falcon agent."),
                   ("Yangilanishdagi mantiqiy xato (Null Pointer / Out-of-bounds read) Windows drayverini yiqitdi.",
                    "Логическая ошибка в файле конфигурации привела к обращению по нулевому указателю в драйвере ядра.",
                    "A logic validation flaw caused a memory access violation inside the Ring 0 kernel driver."),
                   ("Dunyo bo'ylab <b>8.5 million Windows kompyuter</b> bir vaqtda Moviy O'lim Ekrani (BSOD) ga tushdi!",
                    "Более 8.5 млн серверов и рабочих станций Windows мгновенно ушли в циклический BSOD.",
                    "Over 8.5 million Windows hosts instantly cascaded into infinite BSOD boot loops.")
               ])
         + box("purple", ("Dunyo Iqtisodiyotiga Zarari va Muhandislik Darsi", "Ущерб и Главные Инженерные Уроки", "Economic Impact & Engineering Lessons"),
               items=[
                   ("<b>Oqibat:</b> Aviakompaniyalar (Delta, United) minglab reyslarni bekor qildi, shifoxonalar operatsiyalarni to'xtatdi, bankomatlar ishlamay qoldi. Zarar <b>$10 milliarddan oshdi</b>.",
                    "Отмена десятков тысяч авиарейсов, паралич больниц и банков. Убытки превысили $10 млрд.",
                    "Grounded thousands of commercial flights, paralyzed healthcare surgeries, damages exceeded $10B."),
                   ("<b>Asosiy sabab:</b> Bosqichma-bosqich yangilash (Canary / Staged Deployment) qoidasi buzilib, yangilanish <b>bir paytda butun dunyoga</b> tarqatilgan!",
                    "<b>Фатальная ошибка:</b> Отсутствие канареечного деплоя (Canary) — файл выкатили на весь мир разом.",
                    "<b>Fatal Flaw:</b> Complete bypass of Canary deployment ring testing — update pushed globally at once!"),
                   ("<b>Xulosa:</b> Xavfsizlik dasturining o'zi eng katta xavfga aylanmasligi uchun qat'iy sinov va bosqichli deploy shart!",
                    "Даже защитное ПО требует строгой верификации и поэтапного развертывания.",
                    "Defensive security tools themselves must adhere to strict staged rollouts and sandboxed validation.")
               ])
         + '</div>'
))

# 9. Engineering Governance: The Blameless Post-Mortem & 5 Whys
S.append(slide(
    ph=("Post-Mortem", "Постмортем", "Post-Mortem"), time="30–33",
    eyebrow=("Madaniyat va boshqaruv", "Инженерная культура", "Root Cause Analysis"),
    title=("Blameless Post-Mortem va 5 Whys (5 Nega?) Metodi",
           "Безобвинительный Постмортем и Метод «5 Почему»",
           "Engineering Governance: Blameless Post-Mortems & The 5 Whys"),
    body='<div class="cols">\n'
         + box("navy", ("Blameless (Aybdor Qidirmaslik) Madaniyati", "Культура Без Поиска Виноватых", "Blameless Engineering Culture"),
               items=[
                   ("Agar tizim buzilsa, xodimni jazolash yoki ishdan bo'shatish kiberxavfsizlikni yaxshilamaydi — odamlar xatolarini yashira boshlaydi.",
                    "Наказание дежурного инженера контрпродуктивно: сотрудники начинают скрывать инциденты.",
                    "Punishing individual engineers fosters a culture of concealment rather than transparency."),
                   ("<b>Google SRE tamoyili:</b> Xatolik inson aybi emas, balki tizimning zaifligi (protsess, testlar va avtomatlashtirish yetishmasligi) tufayli sodir bo'ladi.",
                    "Принцип Google SRE: инцидент — это сбой защитных механизмов системы и процессов тестирования.",
                    "Google SRE doctrine: incidents stem from systemic architecture and testing gaps, not human malice."),
                   ("Maqsad: xatolik takrorlanmasligi uchun tizimga avtomatik tekshiruvlar (Guardrails) qo'shish.",
                    "Цель постмортема — внедрить технические барьеры, делающие повторение ошибки невозможным.",
                    "Objective: implement architectural safeguards preventing the failure mode from ever recurring.")
               ])
         + box("green", ("5 Nega? (5 Whys) Tahlili Misoli", "Метод «5 Почему» на Практике", "The 5 Whys Root Cause Chain"),
               items=[
                   ("1. Nega server buzildi? <i>— Chunki hacker web-shell yukladi.</i>",
                    "1. Почему упал сервер? <i>— Хакер залил веб-шелл.</i>",
                    "1. Why was the server breached? <i>— Attacker uploaded a web shell.</i>"),
                   ("2. Nega yuklay oldi? <i>— Chunki rasm yuklash joyida kengaytma tekshirilmagan.</i>",
                    "2. Почему залил? <i>— Не было валидации расширения файла.</i>",
                    "2. Why could they upload it? <i>— Upload endpoint lacked file extension validation.</i>"),
                   ("3. Nega tekshirilmagan? <i>— Chunki yangi chiqqan kod xavfsizlik testidan o'tmagan.</i>",
                    "3. Почему не проверили? <i>— Код релиза пропустил ревью безопасности.</i>",
                    "3. Why was it unvalidated? <i>— Developer skipped security peer review under deadline.</i>"),
                   ("4. Nega o'tmagan? <i>— Chunki CI/CD da avtomatik SAST skaneri bo'lmagan.</i>",
                    "4. Почему пропустил? <i>— В CI/CD пайплайне отсутствовал статический анализатор.</i>",
                    "4. Why did it skip? <i>— CI/CD pipeline lacked automated SAST security scanning.</i>"),
                   ("5. <b>Ildiz sabab:</b> CI/CD ga majburiy SAST skanerini integratsiya qilish!",
                    "5. <b>Истинная причина:</b> Обязать блокировать деплой без прохождения сканера SAST!",
                    "5. <b>Root Cause:</b> Mandate automated SAST gating in CI/CD before any deployment!")
               ])
         + '</div>'
))

# # 10. Hands-on Lab
S.append(slide(
    ph=("Amaliyot", "Практика", "Hands-on Lab"), time="33–42",
    eyebrow=("Interaktiv Studio", "Интерактивная Студия", "Interactive Studio"),
    title=("Amaliy Ish: SOC Dashboard Studio — SIEM, Sigma va Post-Mortem",
           "Практика: Студия SOC Dashboard — SIEM, Sigma и Постмортем",
           "Hands-on Lab: SOC Dashboard Studio — SIEM, Sigma & Post-Mortem"),
    body='<div class="box blue">\n'
         + el("h3", "Laboratoriya Missiyasi: SOC Dashboard Studio (12 Daqiqa)", "Миссия Лаборатории: Студия SOC Dashboard (12 Минут)", "Lab Mission: SOC Dashboard Studio (12 Minutes)")
         + el("p", "Brauzerda <code>studio/index.html</code> ni oching. Terminal yoki murakkab serverlar shart emas! Jonli 12,000+ EPS telemetriya oqimi, xakerlik signallarini tahlil qilish, EDR xost izolyatsiyasi va Sigma qoidalarini amalda boshqaring.",
              "Откройте <code>studio/index.html</code> в браузере. Установка серверов не требуется! Исследуйте живой поток телеметрии 12,000+ EPS, проводите триаж инцидентов, EDR изоляцию и пишите правила Sigma.",
              "Open <code>studio/index.html</code> in your browser. No server setup required! Command a live 12,000+ EPS telemetry stream, triage high-severity alerts, execute EDR host isolation, and validate Sigma detection rules.")
         + '</div>\n'
         + table(
             headers=[("Kvest", "Квест", "Quest"),
                      ("Amal va Vazifa", "Действие в Студии", "Studio Action"),
                      ("Kutilayotgan Natija (Tekshirish)", "Ожидаемый Результат", "Expected Verification")],
             rows=[
                 [("<b>1-Kvest: SSH Brute-Force Bloklash</b><br>(2 Ball)", "<b>Квест 1: Блокировка Brute-Force</b>", "<b>Quest 1: SSH Brute-Force Block</b>"),
                  ("Alerts ro'yxatida 2-signalni tanlang va <code>IP ni Bloklash (UFW)</code> tugmasini bosing.",
                   "Выберите алерт 2 (SSH Brute-Force) и нажмите <code>Заблокировать IP на Фаерволе</code>.",
                   "Select Alert 2 (SSH Brute-Force) and click <code>Block IP on Firewall (UFW)</code>."),
                  ("Buzg'unchining <code>194.26.29.41</code> IP-si darhol UFW xavfsizlik devorida drop qilinadi.",
                   "IP атакующего <code>194.26.29.41</code> мгновенно сбрасывается правилом фаервола.",
                   "Malicious IP <code>194.26.29.41</code> is dropped immediately by UFW rules.")],
                 [("<b>2-Kvest: Xostni Izolyatsiya Qilish</b><br>(3 Ball)", "<b>Квест 2: Изоляция Хоста (EDR)</b>", "<b>Quest 2: EDR Host Isolation</b>"),
                  ("1-kritik signaldagi Web Shell ni tanlang va <code>Xostni Izolyatsiya Qilish (EDR)</code> ni bosing.",
                   "Выберите критический инцидент Web Shell и примените <code>Изолировать Хост</code>.",
                   "Select critical Web Shell alert and trigger <code>Isolate Host (EDR Quarantine)</code>."),
                  ("<code>web-srv-01</code> xosti korporativ tarmoqdan uziladi, hujumchining lateral movement harakati to'xtatiladi.",
                   "Скомпрометированный сервер изолирован, атака отрезана от корпоративной сети.",
                   "Compromised host isolated from LAN, halting lateral spread across subnet.")],
                 [("<b>3-Kvest: Sigma Qoidasini Sinash</b><br>(3 Ball)", "<b>Квест 3: Тест Правила Sigma</b>", "<b>Quest 3: Validate Sigma Rule</b>"),
                  ("Sigma tabida <code>Qoidani Sinovdan O'tkazish</code> tugmasini bosing.",
                   "В табе Sigma нажмите <code>Проверить и Скомпилировать Правило</code>.",
                   "In Sigma tab, execute <code>Verify & Compile Rule</code>."),
                  ("YAML qoidasi 100% to'g'ri deb tasdiqlanib, Splunk SPL va Elastic KQL ga muvaffaqiyatli o'giriladi.",
                   "Синтаксис YAML успешно подтвержден и транслирован в диалекты Splunk и Elastic.",
                   "YAML syntax validated 100% and translated into Splunk SPL and Elastic KQL queries.")],
                 [("<b>4-Kvest: Blameless Post-Mortem</b><br>(2 Ball)", "<b>Квест 4: Постмортем 5 Почему</b>", "<b>Quest 4: Blameless Post-Mortem</b>"),
                  ("Post-Mortem tabida '5 Nega?' zanjirini o'rganing va rasmiy hisobotni generatsiya qiling.",
                   "В табе Post-Mortem изучите цепочку «5 Почему» и сформируйте официальный отчет.",
                   "In Post-Mortem tab, review 5 Whys chain and generate formal incident post-mortem."),
                  ("MTTD: 4 min va MTTR: 18 min bilan rasmiy hisobot tayyorlanadi, xatolik qayta takrorlanmaydigan qilib yopiladi.",
                   "Фиксируются метрики MTTD 4 мин и MTTR 18 мин с планом устранения уязвимостей.",
                   "Formal post-mortem generated with MTTD 4 min & MTTR 18 min, embedding preventive CI/CD gates.")]
             ]
         )
))

# 11. Security Matrix
S.append(slide(
    ph=("Taqqoslash", "Сравнение", "Comparison"), time="42–44",
    eyebrow=("Muhandislik xulosasi", "Инженерное резюме", "SOC Capability Matrix"),
    title=("SOC Asboblari va Himoya Tizimlarining Taqqoslanishi",
           "Сравнение Инструментов Мониторинга и Реагирования",
           "Enterprise SOC Technology & Incident Toolchain Comparison"),
    body=table(
        headers=[("Tizim Turi", "Тип Системы", "Tool Category"),
                 ("Asosiy Vazifasi", "Ключевая Функция", "Core Functionality"),
                 ("Ma'lumot Manbasi", "Источник Данных", "Primary Telemetry"),
                 ("Avtomatlashtirish Darajasi", "Уровень Автоматизации", "Automation Capability")],
        rows=[
            [("<b>SIEM (Wazuh, Splunk)</b>", "<b>SIEM (Wazuh, Splunk)</b>", "<b>SIEM (Wazuh, Splunk)</b>"),
             ("Loglarni markazlashtirish, saqlash, qidiruv va korrelyatsiya.",
              "Централизованный сбор, индексация и поиск по логам.",
              "Log centralization, correlation rules, historical search."),
             ("Barcha serverlar, firewall va dastur loglari.",
              "Журналы ОС, фаерволов, приложений и облака.",
              "All OS logs, network firewalls, and cloud API events."),
             ("O'rtacha (Faqat signallar yaratadi, amal bajarmaydi).",
              "Пассивный (генерация алертов для человека).",
              "Passive (Alert generation for human triage).")],
            [("<b>EDR (CrowdStrike, Defender)</b>", "<b>EDR (CrowdStrike, Defender)</b>", "<b>EDR (CrowdStrike, Defender)</b>"),
             ("Kompyuter ichidagi jarayonlarni nazorat qilish, xostni izolyatsiya qilish.",
              "Мониторинг процессов на хосте, изоляция зараженной машины.",
              "Deep endpoint telemetry, process behavior, instant isolation."),
             ("Yadro qatlami (Kernel hooks), xotira, fayl tizimi.",
              "Уровень ядра ОС, память процессов, системные вызовы.",
              "Kernel Ring 0 driver, process memory, file I/O."),
             ("Yuqori (Zararli jarayonni bir zumda o'ldiradi).",
              "Высокий (автоматическая блокировка и изоляция хоста).",
              "High (Autonomous process killing and host containment).")],
            [("<b>SOAR (Cortex, Shuffle)</b>", "<b>SOAR (Cortex, Shuffle)</b>", "<b>SOAR (Cortex, Shuffle)</b>"),
             ("Kiber-hujumga javob qaytarish ssenariylarini (Playbooks) avtomatlashtirish.",
              "Автоматизация цепочек реагирования (плейбуков) без участия человека.",
              "Orchestrating response playbooks across disparate security tools."),
             ("SIEM signallari va EDR ogohlantirishlari.",
              "Алерты от SIEM, фиды CTI и EDR события.",
              "SIEM incident alerts, threat feeds, and EDR detections."),
             ("To'liq avtonom (IP ni bloklash, parolni tiklash).",
              "Полная автоматизация (блокировка IP, сброс учетки).",
              "Full autonomous execution (firewall bans, ticket closure).")]
        ]
    )
))

# 12. Summary & Homework
S.append(slide(
    ph=("Xulosa", "Итоги", "Summary"), time="44–45",
    eyebrow=("Mustaqil muhandislik ishi", "Домашнее задание", "Engineering Project"),
    title=("Xulosa va Uy Vazifasi: Rasmiy Insident Post-Mortem Hujjati",
           "Итоги и Задание: Составление Документа Постмортема",
           "Summary & Homework: Enterprise Incident Post-Mortem Document"),
    body='<div class="cols">\n'
         + box("blue", ("Dars Xulosasi", "Главные Выводы", "Key Takeaways"),
               items=[
                   ("Hujum sodir bo'lishi ehtimol emas, bu <b>aniq muqarrar voqea</b>. Asosiy ustunlik — tezkor aniqlash (MTTD) va lokallashtirish (MTTR) da.",
                    "Взлом неизбежен. Главная победа безопасности измеряется минутами обнаружения и локализации.",
                    "Breaches are inevitable. Defense excellence is measured entirely by MTTD reduction and MTTR velocity."),
                   ("<b>Sigma qoidalari</b> korporatsiyalarga bitta SIEM ga qaram bo'lib qolmasdan universal himoya yozish imkonini beradi.",
                    "Правила Sigma обеспечивают независимость от вендора SIEM и переносимость сигнатур обнаружения.",
                    "Sigma rules guarantee vendor-neutral, portable detection logic across heterogeneous enterprise SIEM stacks."),
                   ("Blameless Post-Mortem va 5 Whys xatolarni jazolash emas, balki tizimni mustahkamlashning eng oliy madaniyatidir.",
                    "Постмортем без поиска виновных строит культуру инженерной надежности и прозрачности.",
                    "Blameless Post-Mortems transform operational failures into permanent architectural resilience.")
               ])
         + box("purple", ("Uy Vazifasi: Real Insident Post-Mortem Loyihasi (10 Ball)", "Домашнее Задание: Постмортем Инцидента (10 Баллов)", "Homework: Enterprise Incident Post-Mortem (10 Pts)"),
               items=[
                   ("Kompaniyangizda yuz bergan faraziy <b>Ransomware / Kiber-hujum</b> bo'yicha to'liq texnik Post-Mortem hisobotini tayyorlang.",
                    "Составьте полноценный инженерный постмортем по учебному сценарию проникновения программы-вымогателя.",
                    "Author a comprehensive technical Post-Mortem report for a simulated enterprise Ransomware breach."),
                   ("<b>Hujjat bo'limlari:</b> 1) Xulosa va Metrikalar (MTTD, MTTR). 2) Cyber Kill Chain xronologiyasi. 3) 5 Nega? (5 Whys) ildiz tahlili. 4) Tizimni qayta tiklash choralari (Preventive Action Items).",
                    "<b>Разделы:</b> 1) Метрики MTTD/MTTR. 2) Таймлайн Kill Chain. 3) Анализ «5 Почему». 4) План устранения уязвимостей.",
                    "<b>Sections:</b> 1) Incident summary & MTTD/MTTR. 2) Chronological timeline. 3) 5 Whys root cause analysis. 4) Preventive engineering action items."),
                   ("Hisobotni professional Markdown formatida taqdim eting.",
                    "Оформите отчет в формате технического Markdown документа.",
                    "Submit post-mortem in professional GitHub-flavored Markdown.")
               ])
         + '</div>'
))

# Teacher Notes
N_UZ = [
    ["Kirish", "Dwell Time (hujumchining tarmoqda sezilmay yurish vaqti) o'rtacha 200 kun ekanini va bu vaqtni qisqartirish SOC ning bosh maqsadi ekanini tushuntiring.", "Slaydni oching."],
    ["SOC Darajalari", "Tier 1 (Triage), Tier 2 (IR) va Tier 3 (Threat Hunter) mutaxassislarining real vazifalari va maoshlarini aytib, o'quvchilarda motivatsiya uyg'oting.", "Ierarxiyani ko'rsating."],
    ["SIEM Telemetriyasi", "Oddiy loglar (100 ta xato parol) va korrelyatsiya qoidasi qanday qilib haqiqiy xavfni fosh qilishini tushuntiring.", "Telemetriya oqimini chizing."],
    ["Sigma Qoidalari", "Nega xavfsizlik olamida Sigma formati hamma SIEM larga mos universal tilga aylanganini tushuntiring.", "Sigma afzalliklarini ko'rsating."],
    ["Kod Tahlili", "YAML formatidagi Sigma qoidasini satrma-satr tahlil qiling. Nginx web-shell orqali whoami chaqirilganda qoida qanday ishlashini ko'rsating.", "Qoidani oching."],
    ["NIST Bosqichlari", "Hujum bo'lganda serverni o'chirib qo'yish (xotiradagi dalillarni yo'qotish) o'rniga uni tarmoqdan uzish (Host Isolation) to'g'ri ekanini o'rgating.", "Jarayonni tushuntiring."],
    ["Metrikalar", "MTTD, MTTA va MTTR nimani anglatishini va alert fatigue (charchoq sindromi) xavfini tushuntiring.", "Jadvalni ko'rsating."],
    ["CrowdStrike Keysi", "Tarixdagi eng yirik global IT halokat qanday yuz berganini, bitta drayver xatosi 8.5 million serverni to'xtatganini tushuntiring.", "Keysni tahlil qiling."],
    ["Post-Mortem", "Google SRE ning 'Blameless' madaniyatini o'rgating: xodimni ayblash o'rniga tizimning o'zini tuzatish nega muhimligini 5 Whys misolida oching.", "5 Whys zanjirini ko'rsating."],
    ["Amaliyot", "O'quvchilar bilan birgalikda loglarni o'rganib, xronologiya tuzish va Sigma shartini tekshirish amaliyotini o'tkazing.", "12 daqiqa taymerni yoqing."],
    ["Matritsa", "SIEM, EDR va SOAR tizimlari bir-biri bilan qanday integratsiya bo'lishini xulosa qiling.", "Matritsani ko'rib chiqing."],
    ["Xulosa", "Uy vazifasidagi Post-Mortem talablarini va 10 ballik mezonni e'lon qiling, savollarga javob bering.", "Varaqalarni yig'ing."]
]

N_RU = [
    ["Введение", "Объясните, что метрика Dwell Time составляет более 200 дней, и миссия SOC — сократить её до считанных минут.", "Откройте титульный слайд."],
    ["Уровни SOC", "Опишите карьерный путь и задачи: Tier 1 (первичный триаж), Tier 2 (расследование и реагирование), Tier 3 (проактивный поиск угроз).", "Разберите иерархию SOC."],
    ["Телеметрия SIEM", "Покажите, как движок корреляции связывает отдельные события в единую цепочку атаки Cyber Kill Chain.", "Разберите логи и корреляцию."],
    ["Правила Sigma", "Подчеркните независимость правил Sigma: одно правило компилируется под Splunk, QRadar, Elasticsearch и Wazuh.", "Объясните формат Sigma."],
    ["Анализ кода", "Построчно разберите YAML-файл детекции веб-шелла: родительский процесс web-сервера и запуск команд reconnaissance.", "Разберите код правила."],
    ["Цикл NIST", "Предостерегите от фатальной ошибки новичков — выключения питания ПК (стирание оперативной памяти). Объясните изоляцию хоста.", "Разберите регламент NIST."],
    ["Метрики", "Разберите метрики MTTD, MTTA и MTTR. Объясните феномен усталости от алертов (Alert Fatigue) у операторов.", "Обсудите метрики."],
    ["Кейс CrowdStrike", "Детально разберите крушение 8.5 млн ПК в июле 2024: отсутствие канареечного деплоя и последствия сбоя на уровне Ring 0.", "Разберите сбой CrowdStrike."],
    ["Постмортем", "Объясните инженерную культуру Blameless Post-Mortem и проведите цепочку «5 Почему» до системного дефекта в пайплайне.", "Поясните метод «5 Почему»."],
    ["Практикум", "Курируйте практическое задание: составление правила Sigma, хронологии атаки и расчет метрик инцидента.", "Запустите таймер 12 минут."],
    ["Матрица", "Резюмируйте матрицу технологий: SIEM для анализа логов, EDR для хостов, SOAR для автоматических плейбуков.", "Обобщите матрицу мер."],
    ["Итоги", "Огласите критерии домашнего задания на 10 баллов и ответьте на вопросы.", "Соберите рабочие листы."]
]

N_EN = [
    ["Intro", "Contextualize that modern adversaries enjoy over 200 days of median Dwell Time, establishing SOC velocity as the primary differentiator.", "Open title slide."],
    ["SOC Tiers", "Break down the functional responsibilities and escalation chains of Tier 1 Triage, Tier 2 Incident Response, and Tier 3 Threat Hunters.", "Review SOC hierarchy."],
    ["SIEM Telemetry", "Illustrate how correlation engines connect low-priority telemetry bursts into high-fidelity attack chains.", "Diagram correlation logic."],
    ["Sigma Rules", "Emphasize why open-source Sigma YAML rules are the industry standard for portable, vendor-neutral detection engineering.", "Explain Sigma portability."],
    ["Code Dissection", "Walk through the production Sigma rule line by line, identifying web server parentage executing system triage utilities.", "Analyze YAML detection code."],
    ["NIST Lifecycle", "Caution against pulling power plugs (destroying volatile RAM artifacts) and emphasize network host isolation during containment.", "Explain NIST containment."],
    ["SOC Metrics", "Define MTTD, MTTA, and MTTR benchmarks while highlighting alert fatigue as the primary operational vulnerability.", "Review performance metrics."],
    ["CrowdStrike Incident", "Dissect the July 2024 global outage: kernel-level Ring 0 driver invalid memory reads and the absence of canary deployment rings.", "Analyze CrowdStrike case."],
    ["Post-Mortem", "Inculcate Google SRE Blameless Post-Mortem culture, tracing incident mechanics through 5 Whys to architectural root causes.", "Demonstrate 5 Whys chain."],
    ["Lab", "Guide students through authoring Sigma detection conditions, correlating 4-phase timelines, and calculating MTTR under SLA pressure.", "Start 12-min lab timer."],
    ["Matrix", "Synthesize security integration: SIEM for enterprise correlation, EDR for host execution telemetry, and SOAR for autonomous response.", "Review technology matrix."],
    ["Summary", "Announce the 10-point Ransomware post-mortem homework assignment and address student technical inquiries.", "Collect worksheets."]
]

NOTES = {"uz": N_UZ, "ru": N_RU, "en": N_EN}

# --- Worksheet (Varaqa) ---
V = []
V.append(sheet_header(
    h1=("Kiberxavfsizlik: SOC Simulyatsiyasi va Insident Boshqaruvi",
        "Кибербезопасность: Симуляция SOC и Управление Инцидентами",
        "CyberSecurity: Enterprise SOC & Incident Response"),
    sub=("Amaliy Laboratoriya Varaqasi · 10–11-sinf · 5-hafta · 25-dars",
         "Практический Рабочий Лист · 10–11 класс · Неделя 5 · Урок 25",
         "Hands-On Lab Worksheet · Grades 10–11 · Week 5 · Lesson 25")
))

V.append(mission(
    h=("Laboratoriya Vazifasi: SOC Dashboard Studio Kvestlari",
       "Миссия Лабораторной: Квесты в Студии SOC Dashboard",
       "Lab Mission: SOC Dashboard Studio Incident Defense Quests"),
    p=("Interaktiv <code>SOC Dashboard Studio</code> (studio/index.html) markazida 12,000+ EPS telemetriya oqimini kuzatish, "
       "SSH Brute-Force IP-sini bloklash, zararlangan serverni EDR orqali izolyatsiya qilish, universal Sigma qoidasini sinash hamda Blameless Post-Mortem hisobotini tayyorlash.",
       "В интерактивной среде <code>SOC Dashboard Studio</code> (studio/index.html) исследовать поток телеметрии 12,000+ EPS, "
       "заблокировать IP атаки Brute-Force, изолировать скомпрометированный сервер через EDR, протестировать правило Sigma и сформировать постмортем.",
       "In the interactive <code>SOC Dashboard Studio</code> (studio/index.html), analyze a live 12,000+ EPS telemetry stream, "
       "mitigate SSH Brute-Force attacks, execute EDR network isolation on compromised hosts, validate Sigma detection rules, and publish a formal Blameless Post-Mortem."))
)

V.append(table(
    headers=[
        ("Amaliy Kvest (Studio)", "Практический Квест (Студия)", "Studio Defense Quest"),
        ("Harakat / Hujum Turi", "Действие / Тип Атаки", "Action / Attack Scenario"),
        ("Kutilgan Natija (Status)", "Ожидаемый Результат", "Expected Verification"),
        ("Ball va Holat", "Баллы и Статус", "Score & Status")
    ],
    rows=[
        [("1. SSH Brute-Force Bloklash", "1. Блокировка Brute-Force", "1. SSH Brute-Force Block"),
         ("`2-signal: 194.26.29.41 ni bloklash`", "`Алерт 2: Блокировка IP 194.26.29.41`", "`Alert 2: Block IP 194.26.29.41`"),
         ("UFW xavfsizlik devori so'rovlarni drop qiladi", "Пакеты атакующего сброшены правилом фаервола", "Attacker packets dropped at firewall level"),
         ("2 ball / [  ]", "2 балла / [  ]", "2 pts / [  ]")],
        [("2. Xostni Izolyatsiya Qilish", "2. Изоляция Хоста (EDR)", "2. EDR Host Isolation"),
         ("`1-kritik signal: web-srv-01 ni uzish`", "`Алерт 1: Изоляция web-srv-01`", "`Alert 1: Isolate web-srv-01 host`"),
         ("EDR Quarantine faollashadi, tarmoqqa o'tish to'xtaydi", "Хост изолирован, боковое движение хакера пресечено", "Host quarantined, lateral spread neutralized"),
         ("3 ball / [  ]", "3 балла / [  ]", "3 pts / [  ]")],
        [("3. Sigma Qoidasini Sinash", "3. Проверка Правила Sigma", "3. Validate Sigma Rule"),
         ("`Nginx -> Bash qoidasini kompilyatsiya qilish`", "`Компиляция правила Sigma для Nginx`", "`Compile Nginx -> Bash Sigma rule`"),
         ("Qoida Splunk SPL va Elastic KQL ga muvaffaqiyatli o'giriladi", "Успешная трансляция в Splunk SPL и Elastic KQL", "Rule compiled cleanly into Splunk and Elastic"),
         ("3 ball / [  ]", "3 балла / [  ]", "3 pts / [  ]")],
        [("4. Blameless Post-Mortem", "4. Постмортем «5 Почему»", "4. Blameless Post-Mortem"),
         ("`5 Nega? zanjiri va rasmiy hisobot`", "`Анализ 5 Почему и генерация отчета`", "`5 Whys chain & official report`"),
         ("MTTD: 4 min, MTTR: 18 min va IaC CI/CD chorasi kiritiladi", "Метрики зафиксированы, деплой переведен под контроль", "Metrics recorded, CI/CD security gating mandated"),
         ("2 ball / [  ]", "2 балла / [  ]", "2 pts / [  ]")]
    ]
))

V.append(sheet_box(
    h=("Xavfsizlik Tahlili va Nazariy Savollar", "Анализ Безопасности и Вопросы", "Architectural Analysis & Written Queries"),
    body_html=writelines(3, label=("1. Nega kiber-hujum aniqlanganda server elektr tarmog'idan uzib qo'yilmaydi (o'chirilmaydi), balki faqat tarmoqdan izolyatsiya qilinadi (Host Isolation)?",
                                   "1. Почему при взломе сервер изолируют от сети (Host Isolation), а не выключают питание из розетки?",
                                   "1. Why must a compromised server undergo network host isolation rather than an immediate hard power shutdown during incident containment?"))
             + "<br>"
             + writelines(3, label=("2. Google SRE tamoyilidagi 'Blameless Post-Mortem' (Aybdor qidirmaslik) madaniyati nima va u 5 Whys metodi orqali korporativ xavfsizlikni qanday kuchaytiradi?",
                                   "2. Что представляет собой культура «Blameless Post-Mortem» и как метод «5 Почему» укрепляет безопасность без поиска козла отпущения?",
                                   "2. What is the philosophy of a 'Blameless Post-Mortem' and how does the 5 Whys framework systematically fortify enterprise security architecture?"))
))

V.append(sheet_box(
    h=("Baholash Mezoni (10 Ball)", "Критерии Оценки (10 Баллов)", "Grading Rubric (10 Points)"),
    body_html=rubric([
        (("Sigma qoidasi sintaksisi (Logsource, Selection, Condition) xatosiz tuzilgan", "Синтаксис и логика правила Sigma составлены безупречно", "Sigma rule YAML syntax and detection logic authored correctly"), "3 ball"),
        (("Hujum xronologiyasi (Timeline) va NIST SP 800-61 lokallashtirish choralari to'liq yoritilgan", "Таймлайн инцидента и регламент NIST SP 800-61 описаны верно", "Incident timeline and NIST SP 800-61 containment measures justified"), "3 ball"),
        (("CrowdStrike keysi, MTTD/MTTR metrikalari va 5 Whys tahlili chuqur tushuntirilgan", "Разобраны инцидент CrowdStrike, метрики MTTD/MTTR и метод «5 Почему»", "CrowdStrike case, MTTD/MTTR metrics, and 5 Whys methodology evaluated"), "2 ball"),
        (("Laboratoriya topshiriqlari to'liq bajarilgan va yozma tahliliy savollarga asosli javob berilgan", "Практические задачи выполнены, даны ответы на аналитические вопросы", "Lab experiments validated and written analytical queries thoroughly answered"), "2 ball"),
    ], "10 ball")
))

V.append("</div>\n" + sign_box("Musulmonov Mamarajab"))

VARAQA_BODY = "\n".join(V)

lesson = Lesson(
    outdir=D,
    titles=TITLES,
    sheet_titles=SHEET_TITLES,
    key="vc-notes-10-25",
    slides=S,
    notes=NOTES,
    varaqa_body=VARAQA_BODY
)

if __name__ == "__main__":
    out = lesson.build()
    print("Created:", out)
