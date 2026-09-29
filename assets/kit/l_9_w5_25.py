# -*- coding: utf-8 -*-
"""9-sinf · 5-hafta · 25-dars — Kiber-Hujum Simulyatsiyasi: CTF va Red/Blue Team Mudofaasi."""

import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from build import (Lesson, slide, title_slide, box, code, el, i18n,
                   sheet_header, mission, table, sheet_box, rubric, writelines, sign_box)

D = "classes/9-sinf/5-hafta/25-dars-kiber-hujum-ctf-va-red-blue-team"

TITLES = {
    "uz": "25-dars: Kiber-Hujum Simulyatsiyasi — CTF & Red/Blue Team",
    "ru": "Урок 25: Симуляция Кибератаки — CTF & Red/Blue Team",
    "en": "Lesson 25: Cyber Attack Simulation — CTF & Red/Blue Team Defense",
}
SHEET_TITLES = {k: v + (" — Ish Varaqasi" if k == "uz" else
                        " — Рабочий Лист" if k == "ru" else " — Worksheet")
                for k, v in TITLES.items()}

S = []

# 1. Title Slide
S.append(title_slide(
    ph=("Kirish", "Введение", "Intro"), time="0–3",
    eyebrow=("CyberSecurity · 25-dars · 9-sinf (War Games Track)",
             "CyberSecurity · Урок 25 · 9 класс (War Games Track)",
             "CyberSecurity · Lesson 25 · Grade 9 (War Games Track)"),
    h1=("Kiber-Hujum Simulyatsiyasi: CTF & Red/Blue Team",
        "Симуляция Кибератаки: CTF & Red/Blue Team",
        "Cyber Defense Simulation: CTF & Red/Blue Team Ops"),
    lede=("Nazariyani bilish yaxshi, lekin haqiqiy xavfsizlik mutaxassisi faqat amaliy kiber-jangda shakllanadi. "
          "Sanoatda mudofaa tizimlari <b>Red Team (hujumchilar)</b> va <b>Blue Team (himoyachilar)</b> o'rtasidagi "
          "haqiqiy simulyatsiyalar — <b>CTF (Capture The Flag)</b> orqali toblanadi. "
          "Bugungi darsda siz butun 5-hafta davomida o'rgangan Linux xavfsizligi, tarmoq paketlari, "
          "OWASP zaifliklari va JWT bilimlarini birlashtirib, buzilgan tizimni tahlil qilasiz, "
          "xaker qoldirgan izlarni topasiz va 3 ta yashirin kiber-bayroqni (FLAG) qo'lga kiritasiz.",
          "Теория важна, но настоящий специалист по кибербезопасности рождается в боевых условиях. "
          "Индустрия проверяет стойкость систем через военные кибер-игры — <b>CTF (Capture The Flag)</b> "
          "между командами <b>Red Team (атака)</b> и <b>Blue Team (защита)</b>. "
          "Сегодня вы объедините все знания 5-й недели (Linux, SSH, Wireshark, SQLi, XSS, JWT) "
          "для расследования реального инцидента, поиска следов взлома и захвата 3 кибер-флагов.",
          "Theory is essential, but true cybersecurity competence is forged under live adversarial conditions. "
          "The security industry tests defensive resilience through <b>Capture The Flag (CTF)</b> simulations "
          "pitting <b>Red Team (Adversary Emulation)</b> against <b>Blue Team (Detection & Response)</b>. "
          "Today you synthesize all Week 5 competencies (Linux, SSH, Wireshark, SQLi, XSS, JWT) "
          "to perform incident forensics, hunt attacker traces, and capture 3 hidden security flags."),
    meta=[("<b>Fan:</b> Kiberxavfsizlik · Cyber War Games & CTF",
           "<b>Предмет:</b> Кибербезопасность · Кибер-Учения и CTF",
           "<b>Subject:</b> CyberSecurity · Cyber War Games & CTF"),
          ("<b>Kohorta:</b> 9-sinf Kiber-Muhandis",
           "<b>Когорта:</b> 9 класс Кибер-Инженер",
           "<b>Cohort:</b> Grade 9 Cyber-Engineer"),
          ("<b>Hafta:</b> 5 (5-soat · Hafta Yakuni)", "<b>Неделя:</b> 5 (5-й час · Финал)", "<b>Week:</b> 5 (Hour 5 · Finale)")],
))

# 2. Red Team vs Blue Team
S.append(slide(
    ph=("Jamoalar", "Команды", "Red vs Blue"), time="3–6",
    eyebrow=("Kiber-armiya tuzilishi", "Структура кибербезопасности", "Cyber Operations"),
    title=("Red Team vs Blue Team: Kiber-Jang Maydoni Qanday Ishlaydi?",
           "Red Team против Blue Team: Как Устроена Кибервойна?",
           "Red Team vs Blue Team: Anatomy of Enterprise Cyber Exercises"),
    body='<div class="cols c2">\n'
         + box("accent", ("🔴 Red Team (Hujumchilar)", "🔴 Red Team (Атака)", "🔴 Red Team (Offensive Operators)"),
               items=[
                   ("<b>Maqsad:</b> Tizimdagi har qanday zaiflikni topib, ichkariga kirish va bayroqni o'g'irlash.",
                    "<b>Цель:</b> Найти брешь в защите, проникнуть внутрь и захватить целевой флаг.",
                    "<b>Objective:</b> Emulate real adversaries, penetrate defenses, and exfiltrate objective flags."),
                   ("<b>Qurollar:</b> Nmap, Metasploit, Burp Suite, SQLMap, Phishing skriptlari.",
                    "<b>Инструменты:</b> Nmap, Metasploit, Burp Suite, SQLMap, кастомные эксплойты.",
                    "<b>Arsenal:</b> Port scanners, web proxies, exploit payloads, and social engineering."),
                   ("<b>Qoida:</b> Tizimni buzish, lekin haqiqiy zararsiz (axloqiy xakerlik).",
                    "<b>Принцип:</b> Пробить периметр, действуя в рамках этичного хакинга.",
                    "<b>Constraint:</b> Compromise the target within ethical scope and rules of engagement."),
               ])
         + box("purple", ("🔵 Blue Team (Himoyachilar)", "🔵 Blue Team (Защита)", "🔵 Blue Team (Defenders & SOC)"),
               items=[
                   ("<b>Maqsad:</b> Hujumni real vaqtda aniqlash, yo'lini to'sish va tizimni qulflash.",
                    "<b>Цель:</b> Засечь атаку в реальном времени, заблокировать и залатать дыру.",
                    "<b>Objective:</b> Detect intrusion attempts in real time, contain breaches, and harden assets."),
                   ("<b>Qurollar:</b> Wireshark, Fail2ban, SIEM tizimlari, UFW, Log tahlilchilari.",
                    "<b>Инструменты:</b> Wireshark, Fail2ban, SIEM, фаерволы, анализаторы логов.",
                    "<b>Arsenal:</b> Packet analyzers, host firewalls, SIEM correlators, and endpoint telemetry."),
                   ("<b>Qoida:</b> Hujumchini 5 daqiqada topib, IP manzilini bloklash va xatoni yopish.",
                    "<b>Принцип:</b> Быстрая изоляция угрозы и восстановление целостности данных.",
                    "<b>Constraint:</b> Rapid incident triage, active containment, and root-cause eradication."),
               ])
         + '\n</div>'
))

# 3. The Cyber Kill Chain
S.append(slide(
    ph=("Hujum Zanjiri", "Цепь Атаки", "Kill Chain"), time="6–10",
    eyebrow=("Lockheed Martin modeli", "Модель Lockheed Martin", "Lockheed Martin Framework"),
    title=("Cyber Kill Chain: Kiber-Hujumning 7 Ta Bosqichi",
           "Cyber Kill Chain: 7 Фаз Любой Кибератаки",
           "The Cyber Kill Chain: 7 Phases of Targeted Intrusions"),
    body='<div class="cols c4">\n'
         + box("", ("1. Reconnaissance", "1. Разведка", "1. Reconnaissance"),
               p=("Target haqida ma'lumot to'plash (Nmap, Shodan, Whois). Ochiq portlar va zaifliklarni aniqlash.",
                  "Сбор данных о цели, сканирование портов Nmap, поиск открытых служб.",
                  "Scanning network perimeter, harvesting exposed ports, and profiling software stacks."))
         + box("", ("2. Weaponization", "2. Подготовка", "2. Weaponization"),
               p=("Topilgan zaiflikka mos exploit tayyorlash (masalan, SQLi so'rovi yoki troyan fayl).",
                  "Создание боевого пейлоада под найденную уязвимость.",
                  "Coupling malicious payloads with exploits tailored to target vulnerabilities."))
         + box("", ("3. Delivery", "3. Доставка", "3. Delivery"),
               p=("Exploitni serverga yetkazish: formaga SQL kiritish yoki xodimga fishing xat yuborish.",
                  "Отправка эксплойта цели: ввод в поле сайта или фишинговое письмо.",
                  "Transmitting the payload via vulnerable web inputs or spear-phishing messages."))
         + box("accent", ("4. Exploitation & Actions", "4. Взлом и Цель", "4. Exploitation & Impact"),
               p=("Kod bajariladi, server qo'lga olinadi va ma'lumotlar bazasi o'g'irlanadi (Flag captured!).",
                  "Исполнение пейлоада, получение доступа и кража конфиденциальных данных.",
                  "Exploit triggers code execution, pivoting lateral movement, and data exfiltration."))
         + '\n</div>'
))

# 4. Log Forensics: Hunting in the Shadows
S.append(slide(
    ph=("Log Tahlili", "Анализ Логов", "Log Forensics"), time="10–14",
    eyebrow=("Kiber-detektivlik", "Кибер-детектив", "Threat Hunting"),
    title=("Log Forensikasi: Tizimdagi Hujum Izlarini Qanday Topamiz?",
           "Форензика Логов: Как Найти Следы Взломщика в Системе?",
           "Log Forensics: Hunting Attacker Footprints in Auth Logs"),
    body='<div class="cols c2">\n'
         + box("green", ("Linux Tizimidagi 3 Ta Asosiy Log Fayl", "3 Главных Лог-Файла Linux", "The 3 Critical Log Files"),
               items=[
                   ("<b>/var/log/auth.log:</b> Barcha SSH kirishlar, sudo buyruqlari va muvaffaqiyatsiz urinishlar.",
                    "<b>/var/log/auth.log:</b> Все попытки входа по SSH, команды sudo и сбои.",
                    "<b>/var/log/auth.log:</b> Tracks all authentication events, failed logins, and sudo executions."),
                   ("<b>/var/log/nginx/access.log:</b> Saytga kelgan barcha HTTP so'rovlar, IP manzillar va URL lar.",
                    "<b>/var/log/nginx/access.log:</b> Полный журнал веб-запросов к серверу Nginx.",
                    "<b>/var/log/nginx/access.log:</b> Records every incoming HTTP request, IP, user-agent, and status code."),
                   ("<b>/var/log/syslog:</b> Operatsion tizim yadrosi, xizmatlar va xatoliklar jurnali.",
                    "<b>/var/log/syslog:</b> Общесистемные события операционной системы и сервисов.",
                    "<b>/var/log/syslog:</b> Global system kernel messages, daemon crashes, and service state transitions."),
               ])
         + '<div class="box accent">\n'
         + el("h3", "Hujumchilarni Tutuvchi Bash Buyruqlari", "Команды Поиска Атак в Bash", "Bash Threat Hunting Commands")
         + code("""# 1. SSH ga buzib kirmoqchi bo'lgan TOP 5 ta IP manzil:
grep 'Failed password' /var/log/auth.log | 
  awk '{print $(NF-3)}' | sort | uniq -c | sort -nr | head -5

# 2. Veb-saytda SQL Injection qidirayotgan shubhali so'rovlar:
grep -E "('|\--|UNION|SELECT)" /var/log/nginx/access.log

# 3. Hozirda serverda faol bo'lgan shubhali ulanishlar:
sudo ss -tulpn | grep ESTAB""")
         + '</div>\n</div>'
))

# 5. CTF Flag Architecture
S.append(slide(
    ph=("CTF Formati", "Формат CTF", "CTF Architecture"), time="14–18",
    eyebrow=("Bayroqlar formati", "Формат флагов", "Flag Standards"),
    title=("CTF Bayroqlari: Kiber-G'alabaning Isboti (FLAG{...})",
           "Флаги CTF: Доказательство Взлома или Защиты",
           "CTF Flags: Cryptographic Proof of Exploit Execution"),
    body='<div class="cols c3">\n'
         + box("accent", ("🚩 Flag 1: Linux & SSH", "🚩 Флаг 1: Linux & SSH", "🚩 Flag 1: Linux & SSH"),
               p=("Serverdagi yashirin konfiguratsiya faylida yoki noto'g'ri huquqli fayl ichida yashirilgan:<br><br><code>FLAG{ssh_ed25519_k3y_s3cur3d}</code>",
                  "Спрятан в скрытом файле конфигурации на сервере Linux:<br><br><code>FLAG{ssh_ed25519_k3y_s3cur3d}</code>",
                  "Hidden inside a misconfigured permission file in Linux filesystem:<br><br><code>FLAG{ssh_ed25519_k3y_s3cur3d}</code>"))
         + box("purple", ("🚩 Flag 2: Tarmoq & Wireshark", "🚩 Флаг 2: Сеть & Wireshark", "🚩 Flag 2: Network Forensics"),
               p=("Ushlangan `.pcap` fayl ichidagi shifrlanmagan HTTP POST paketida yashiringan:<br><br><code>FLAG{w1r3shark_sn1ff3d_c00k1e}</code>",
                  "Спрятан в незашифрованном POST-пакете внутри дампа `.pcap`:<br><br><code>FLAG{w1r3shark_sn1ff3d_c00k1e}</code>",
                  "Embedded inside cleartext HTTP POST body within captured `.pcap` trace:<br><br><code>FLAG{w1r3shark_sn1ff3d_c00k1e}</code>"))
         + box("green", ("🚩 Flag 3: OWASP & JWT", "🚩 Флаг 3: OWASP & JWT", "🚩 Flag 3: AppSec & JWT"),
               p=("SQL Injection orqali yashirin ma'lumotlar jadvalidan chiqarib olinadi:<br><br><code>FLAG{sql1_pr3p4r3d_st4t3m3nts_w1n}</code>",
                  "Извлекается из базы через SQL-инъекцию или декодирование токена JWT:<br><br><code>FLAG{sql1_pr3p4r3d_st4t3m3nts_w1n}</code>",
                  "Exfiltrated via SQL injection bypass or forged JWT authorization claim:<br><br><code>FLAG{sql1_pr3p4r3d_st4t3m3nts_w1n}</code>"))
         + '\n</div>'
))

# 6. Incident Response & Containment
S.append(slide(
    ph=("Insident", "Реагирование", "Incident Response"), time="18–22",
    eyebrow=("Tizim buzilganda nima qilinadi?", "Что делать при взломе?", "Emergency Protocol"),
    title=("Kiber-Insident Protokoli: 4 Ta Shoshilinch Qadam",
           "Протокол Реагирования на Инцидент: 4 Срочных Шага",
           "Incident Response Protocol: The 4 Golden Containment Steps"),
    body='<div class="cols c2">\n'
         + box("accent", ("1. Izolyatsiya (Containment)", "1. Изоляция (Containment)", "1. Isolate the Host"),
               items=[
                   ("<b>Tarmoqni uzish:</b> Serverni darhol tashqi internetdan uzing yoki UFW da faqat o'z IP-ingizga ruxsat qoldiring.",
                    "<b>Изоляция сети:</b> Немедленно отсеките сервер от внешней сети через UFW.",
                    "<b>Sever network link:</b> Restrict firewall ingress strictly to your emergency forensic IP."),
                   ("<b>Serverni o'chirmang (Do NOT reboot):</b> Server o'chsa, operativ xotiradagi (RAM) barcha dalillar yo'qoladi!",
                    "<b>Не выключайте питание:</b> Перезагрузка уничтожит улики в оперативной памяти (RAM).",
                    "<b>Do NOT power off:</b> Rebooting destroys volatile forensics evidence resident in RAM."),
               ])
         + box("green", ("2. Tozalash va Qayta Tiklash", "2. Очистка и Восстановление", "2. Eradication & Recovery"),
               items=[
                   ("<b>Zararli jarayonlarni o'ldirish:</b> `kill -9 &lt;PID&gt;` orqali mayner yoki troyanni to'xtatish.",
                    "<b>Убить процессы:</b> Остановка вредоносных скриптов через `kill -9 &lt;PID&gt;`.",
                    "<b>Terminate rogue processes:</b> Kill unauthorized miner or shell PIDs."),
                   ("<b>Barcha kalitlarni almashtirish (Rotate Secrets):</b> SSH kalitlar, JWT sirlari va parollar yangilanadi.",
                    "<b>Смена всех ключей:</b> Полная ротация SSH-ключей, паролей и секретов JWT.",
                    "<b>Rotate all credentials:</b> Invalidate all existing SSH keys, JWT secrets, and database passwords."),
                   ("<b>Post-Mortem hisobot:</b> Hujum qayerdan va qanday kirganini yozib, xatolikni qayta takrorlanmas qilishi shart.",
                    "<b>Отчёт Post-Mortem:</b> Анализ первопричины для предотвращения повторных атак.",
                    "<b>Post-Mortem Analysis:</b> Document vulnerability root cause and implement automated guardrails."),
               ])
         + '\n</div>'
))

# 7. Real Attack Scenario: The SolarWinds Supply Chain Breach
S.append(slide(
    ph=("Tarixiy Keys", "Исторический Кейс", "SolarWinds Breach"), time="22–26",
    eyebrow=("Tarixdagi eng yirik hujum", "Крупнейший взлом в истории", "Global Supply Chain Attack"),
    title=("SolarWinds Kiber-Halokati: Dasturiy Ta'minot Zanjirini Buzish",
           "Взлом SolarWinds: Атака на Цепочку Поставок (Supply Chain)",
           "The SolarWinds Catastrophe: Supply Chain Infiltration"),
    body='<div class="cols c2">\n'
         + box("accent", ("Hujum Sxemasi", "Схема Атаки", "Attack Vector"),
               p=("2020-yilda elita kiber-guruh (APT29) to'g'ridan-to'g'ri davlat idoralariga hujum qilmadi. Buning o'rniga ular 300 000 dan ortiq tashkilotlar ishlatadigan <b>SolarWinds Orion</b> dasturining yangilanish serveriga kirib, rasmiy yangilanish kodiga <b>SUNBURST troyanini</b> joylab qo'ydi. 18 000 dan ortiq korxona o'z qo'llari bilan xakerlarni ichkariga kiritdi!",
                  "В 2020 году группа APT29 внедрила бэкдор SUNBURST в официальные обновления платформы SolarWinds Orion. Свыше 18 000 корпораций и министерств скачали заражённое обновление своими руками.",
                  "In 2020, APT29 infiltrated SolarWinds build pipelines, injecting the SUNBURST backdoor into digitally signed updates. Over 18,000 enterprise and government networks deployed the infected patch voluntarily."))
         + box("purple", ("Natijalar va Xulosa", "Уроки Инцидента", "Fallout & Modern Lessons"),
               items=[
                   ("<b>AQSh Moliya vazirligi, Pentagon va Microsoft:</b> Eng maxfiy davlat tarmoqlari 9 oy davomida kuzatilgan.",
                    "<b>Пентагон, Минфин США, Microsoft:</b> 9 месяцев взломщики оставались незамеченными.",
                    "<b>Pentagon, US Treasury, Microsoft:</b> Adversaries operated silently inside high-security networks for 9 months."),
                   ("<b>Zero Trust zarurati:</b> Hatto eng ishonchli dasturiy ta'minot ham doimiy tekshiruvda bo'lishi shart.",
                    "<b>Принцип Zero Trust:</b> Даже доверенное ПО от официальных вендоров требует мониторинга.",
                    "<b>The Zero Trust imperative:</b> Never trust even certified vendor binaries without behavioral isolation."),
               ])
         + '\n</div>'
))

# 8. CTF War Games Briefing
S.append(slide(
    ph=("Brifing", "Брифинг", "Mission Briefing"), time="26–30",
    eyebrow=("CTF Jang Maydoni", "Кибер-полигон", "Cyber Range Mission"),
    title=("CTF Kiber-Poligon: 3 Ta Bayroqni Qo'lga Kiriting!",
           "Киберполигон CTF: Захватите 3 Флага!",
           "The CTF Challenge: Capture All 3 Objective Flags"),
    body='<div class="cols c3">\n'
         + box("accent", ("🚩 Bayroq 1: Recon (Nmap & SSH)", "🚩 Флаг 1: Разведка (SSH)", "🚩 Flag 1: Recon (SSH)"),
               p=("Serverdagi yashirin portni toping, SSH orqali kiring va <code>/home/flag1.txt</code> faylini o'qing.",
                  "Найдите нестандартный порт через Nmap, войдите по SSH и прочтите `/home/flag1.txt`.",
                  "Locate non-standard port via Nmap, authenticate, and read `/home/flag1.txt`."))
         + box("purple", ("🚩 Bayroq 2: Forensika (Wireshark)", "🚩 Флаг 2: Сеть (Wireshark)", "🚩 Flag 2: Sniffing (Wireshark)"),
               p=("Berilgan `.pcap` fayldan xaker yuborgan shifrlanmagan HTTP POST so'rovini toping va tokenni ajrating.",
                  "Найдите в `.pcap` дампа открытый POST-запрос с перехваченным токеном.",
                  "Filter captured `.pcap` file for HTTP POST requests and extract the secret token payload."))
         + box("green", ("🚩 Bayroq 3: AppSec (SQLi)", "🚩 Флаг 3: Веб-взлом (SQLi)", "🚩 Flag 3: AppSec (SQLi)"),
               p=("Test veb-saytning qidiruv maydoniga <code>' OR 1=1</code> yuborib, yashirin admin jadvalidan bayroqni oling.",
                  "Примените SQL-инъекцию к форме поиска и выгрузите флаг из таблицы admin_secrets.",
                  "Execute SQL injection payload on vulnerable form to exfiltrate secret flag from DB."))
         + '\n</div>'
))

# 9. Practical Mission (14 min timer)
S.append(slide(
    ph=("Amaliyot", "Практика", "Hands-On CTF"), time="30–44",
    eyebrow=("Mustaqil laboratoriya · 14 daqiqa", "Лабораторная работа · 14 минут", "CTF Battle · 14 Minutes"),
    title=("CTF Kiber-Jangi: Qidiruv, Tahlil va Bayroqlar",
           "Боевой CTF: Поиск, Анализ и Захват Флагов",
           "Live CTF Engagement: Recon, Capture & Forensic Verification"),
    body='<div class="cols c2">\n'
         + box("green", ("Jang Maydoni Bosqichlari", "Шаги Соревнования", "Operation Phases"),
               items=[
                   ("<b>Bosqich 1:</b> Nmap bilan maqsadli hostni skanerlang (`nmap -sV -p- &lt;target&gt;`).",
                    "<b>Фаза 1:</b> Сканирование портов цели `nmap -sV -p- &lt;target&gt;`.",
                    "<b>Phase 1:</b> Scan full port range of target using `nmap -sV -p-`."),
                   ("<b>Bosqich 2:</b> Wireshark faylini ochib, `http.request.method == \"POST\"` filtrini qo'llang.",
                    "<b>Фаза 2:</b> Открытие дампа Wireshark и фильтрация HTTP POST.",
                    "<b>Phase 2:</b> Open trace in Wireshark and filter for `http.request.method == \"POST\"`."),
                   ("<b>Bosqich 3:</b> Veb-ilovaga SQL Injection uyushtirib, FLAG-3 ni oling.",
                    "<b>Фаза 3:</b> Внедрение SQL-инъекции и извлечение FLAG-3.",
                    "<b>Phase 3:</b> Inject SQLi payload into web portal and exfiltrate FLAG-3."),
                   ("<b>Bosqich 4:</b> Topilgan barcha bayroqlarni ish varaqasiga qayd eting.",
                    "<b>Фаза 4:</b> Запись найденных флагов в рабочий лист.",
                    "<b>Phase 4:</b> Transcribe captured flags into your worksheet."),
               ])
         + box("accent", ("O'lchanadigan Natija", "Критерий Сдачи", "Deliverable Spec"),
               p=("Ish varaqasidagi jadvalga 3 ta haqiqiy <b>FLAG{...}</b> satrini yozish va har bir bayroq qanday zaiflik tufayli qo'lga kiritilganini izohlab berish!",
                  "Внесение в рабочий лист 3 флагов формата <b>FLAG{...}</b> с описанием уязвимости каждого этапа!",
                  "Transcribing 3 valid <b>FLAG{...}</b> strings into worksheet table alongside vulnerability root-cause analysis!"))
         + '\n</div>'
))

# 10. Verification Checklist
S.append(slide(
    ph=("Tekshirish", "Чек-лист", "Verification"), time="44–44",
    eyebrow=("Yakuniy audit", "Финальная проверка", "Final Audit"),
    title=("CTF Yakuniy Cheklisti: 3 Ta Bayroq Tekshiruvi",
           "Чек-лист CTF: Проверка 3 Флагов",
           "CTF Quality Gate: 3 Flag Verification"),
    body='<div class="cols c3">\n'
         + box("", ("1. FLAG-1 (SSH)", "1. Флаг 1 (SSH)", "1. FLAG 1 (SSH)"),
               p=("Linux tizimidagi yashirin konfiguratsiya bayrog'i topildimi?",
                  "Найден ли флаг в скрытом файле Linux?",
                  "Is the Linux filesystem flag correctly identified?"))
         + box("", ("2. FLAG-2 (Wireshark)", "2. Флаг 2 (Wireshark)", "2. FLAG 2 (Wireshark)"),
               p=("Wireshark `.pcap` dagi shifrlanmagan bayroq ajratib olindimi?",
                  "Извлечён ли флаг из незашифрованного сетевого дампа?",
                  "Is the cleartext network token extracted from packet capture?"))
         + box("", ("3. FLAG-3 (SQLi)", "3. Флаг 3 (SQLi)", "3. FLAG 3 (SQLi)"),
               p=("SQL Injection orqali yashirin ma'lumot chiqarildimi?",
                  "Выгружен ли флаг через уязвимость базы данных?",
                  "Is the database secret extracted via SQL injection payload?"))
         + '\n</div>'
))

# 11. Rubric (10-Ball)
S.append(slide(
    ph=("Mezon", "Критерии", "Evaluation"), time="44–45",
    eyebrow=("10 ballik mezon", "10-балльная шкала", "10-Point Rubric"),
    title=("Darsni Baholash Mezonlari (10 Ball)",
           "Критерии Оценки за Урок (10 Баллов)",
           "Lesson Evaluation Rubric (10 Points)"),
    body='<div class="cols c3">\n'
         + box("green", ("A'lo (9–10 Ball)", "Отлично (9–10)", "Exemplary (9–10)"),
               items=[
                   ("3 ta bayroqning barchasi (FLAG 1, 2, 3) topilgan.", "Найдены все 3 флага (1, 2, 3).", "All 3 flags captured successfully."),
                   ("Hujum zanjiri (Kill Chain) to'g'ri tahlil qilingan.", "Цепочка Kill Chain проанализирована верно.", "Cyber Kill Chain accurately mapped."),
                   ("Varaqa 100% to'ldirilgan.", "Рабочий лист заполнен на 100%.", "Worksheet completed 100%."),
               ])
         + box("", ("Yaxshi (7–8 Ball)", "Хорошо (7–8)", "Proficient (7–8)"),
               items=[
                   ("2 ta bayroq qo'lga kiritilgan.", "Успешно захвачены 2 флага.", "2 flags captured successfully."),
                   ("Wireshark va Nmap tahlili to'g'ri.", "Анализ в Wireshark и Nmap корректен.", "Wireshark & Nmap telemetry accurate."),
                   ("Varaqa 80% to'ldirilgan.", "Лист заполнен на 80%.", "Worksheet completed 80%."),
               ])
         + box("accent", ("Qoniqarli (5–6 Ball)", "Удовл. (5–6)", "Developing (5–6)"),
               items=[
                   ("Faqat 1 ta bayroq topilgan.", "Найден только 1 флаг.", "Only 1 flag captured."),
                   ("Tizim tahlilida chalkashliklar bor.", "Ошибки в анализе системных журналов.", "Errors in forensic reasoning."),
                   ("Varaqa qisman to'ldirilgan.", "Лист заполнен не полностью.", "Worksheet incomplete."),
               ])
         + '\n</div>'
))

# 12. Summary & Homework
S.append(slide(
    ph=("Xulosa", "Итоги", "Summary"), time="45–45",
    eyebrow=("5-hafta yakuni", "Финал 5-й недели", "Week 5 Certification"),
    title=("5-Hafta Xulosasi: Kiber-Himoyachi Sertifikati",
           "Итоги 5-й Недели: Сертификат Защитника Систем",
           "Week 5 Grand Finale: Certified Junior Defense Engineer"),
    body='<div class="cols c2">\n'
         + box("purple", ("5-Haftada Nimalarni Egalladingiz?", "Итоги 5-й Недели", "Week 5 Competencies"),
               items=[
                   ("<b>Linux & SSH Hardening:</b> Serverni qulflash, port ko'chirish va UFW devorini qurish.",
                    "<b>Харденинг Linux и SSH:</b> Защита портов, ключи Ed25519 и фаервол UFW.",
                    "<b>Linux & SSH Hardening:</b> Ed25519 keypairs, port evasion, and UFW firewalling."),
                   ("<b>Wireshark & Nmap:</b> Tarmoq paketlarini shifrlanmagan qatlamlargacha titkilash.",
                    "<b>Wireshark и Nmap:</b> Анализ пакетов и сканирование открытых сервисов.",
                    "<b>Wireshark & Nmap:</b> Deep packet inspection and attack surface mapping."),
                   ("<b>OWASP Top 10:</b> SQLi va XSS zaifliklarini amalda tuzatish.",
                    "<b>OWASP Top 10:</b> Устранение SQL-инъекций и атак XSS на практике.",
                    "<b>OWASP Top 10:</b> Remediation of SQL injection and XSS via prepared statements."),
                   ("<b>JWT & 2FA:</b> Kriptografik sessiyalar va internetsiz ishlovchi TOTP kodlari.",
                    "<b>JWT и 2FA:</b> Сессии на токенах и двухфакторка TOTP.",
                    "<b>JWT & 2FA:</b> Cryptographic session signing and offline TOTP algorithms."),
               ])
         + box("accent", ("Uy Vazifasi (10 Ball)", "Домашнее Задание (10 Баллов)", "Homework Assignment (10 Pts)"),
               items=[
                   ("<b>Portfolio:</b> 5-haftadagi barcha amaliy ishlaringiz (SSH, Wireshark, SQLi fix) bo'yicha GitHub da <code>cybersecurity-defense-lab</code> nomli repo ochib, README.md ga hisobot yozing.",
                    "<b>Портфолио:</b> Оформите репозиторий `cybersecurity-defense-lab` на GitHub с отчётом.",
                    "<b>Portfolio:</b> Publish a `cybersecurity-defense-lab` repository with comprehensive forensic writeups."),
                   ("<b>Varaqa:</b> Bugungi CTF varaqasini to'liq yakunlab topshiring.",
                    "<b>Лист:</b> Заполните и сдайте печатный лист CTF.",
                    "<b>Worksheet:</b> Complete and submit your printable CTF lab worksheet."),
               ])
         + '\n</div>'
))

# Teacher Notes
N_UZ = [
    ["Kirish", "Darsni boshlash: Bugun 5-haftaning yakuniy darsi — CTF kiber-urush mashg'uloti.", "Slaydni oching, o'quvchilarda g'oliblik ruhini uyg'oting."],
    ["Jamoalar", "Red Team va Blue Team tushunchalari. Axloqiy xakerlik va mudofaa farqi.", "Doskaga qizil va ko'k jamoalarning vazifalarini yozing."],
    ["Hujum Zanjiri", "Cyber Kill Chain: 7 ta bosqich. Nega har bir bosqichda hujumni to'xtatish imkoni bor?", "Lockheed Martin modelini tushuntiring."],
    ["Log Tahlili", "Loglar — tizimning qora qutisi. auth.log va access.log ni tahlil qilish buyruqlari.", "Terminalda grep va awk buyruqlari bilan shubhali IP larni filtrlashni ko'rsating."],
    ["CTF Formati", "FLAG{...} formati va bayroqlar qayerda yashiringanligi.", "O'quvchilarga 3 ta bayroqning turlarini tushuntiring."],
    ["Insident", "Tizim buzilganda qilinadigan 4 ta shoshilinch qadam. Nega serverni o'chirish mumkin emas?", "RAM dagi dalillarni saqlab qolish qoidasini tushuntiring."],
    ["Tarixiy Keys", "SolarWinds kiber-halokati. Ta'minot zanjiri hujumi nima?", "Eng yirik kiber-josuslik voqeasini qiziqarli qilib so'zlab bering."],
    ["Brifing", "CTF poligon topshirig'i. 3 ta bayroqni topish vazifasi.", "Qoidalarni e'lon qiling."],
    ["Amaliyot", "14 daqiqalik qizg'in CTF jangi! O'quvchilar mustaqil ravishda bayroqlarni qidiradilar.", "Taymerni yoqing (14 daqiqa), zal bo'ylab yurib ko'maklashing."],
    ["Tekshirish", "Nazorat tekshiruvi. Topilgan bayroqlarni doskada tasdiqlang.", "Bayroqlarni tekshiring."],
    ["Mezon", "10 ballik baholash mezoni tushuntiriladi.", "Talablarni e'lon qiling."],
    ["Xulosa", "5-hafta yakuni va tabrik! O'quvchilar Junior Kiber-Himoyachi darajasiga erishdilar!", "Varaqalarni yig'ing va baholang."]
]

N_RU = [
    ["Введение", "Старт урока: Финал 5-й недели — киберучения CTF (Capture The Flag).", "Откройте слайд, настройте класс на соревновательный лад."],
    ["Команды", "Red Team против Blue Team: этичный хакинг и аналитики безопасности SOC.", "Поясните роли атакующих и защитников."],
    ["Цепь Атаки", "Cyber Kill Chain: 7 фаз вторжения от разведки до кражи данных.", "Разберите модель на реальных примерах."],
    ["Анализ Логов", "Форензика системных журналов auth.log и access.log.", "Покажите команды grep и awk для выявления аномалий."],
    ["Формат CTF", "Что такое FLAG{...} и как оформляются победные доказательства.", "Объясните правила захвата флагов."],
    ["Реагирование", "4 шага при взломе: почему нельзя выключать сервер из розетки.", "Объясните ценность данных в оперативной памяти."],
    ["Исторический Кейс", "Взлом SolarWinds: как атака на цепочку поставок поразила тысячи корпораций.", "Расскажите детективную историю расследования SUNBURST."],
    ["Брифинг", "Брифинг киберполигона: 3 целевых флага.", "Объявите условия начала игры."],
    ["Практика", "14 минут CTF: независимый поиск флагов через Nmap, Wireshark и SQLi.", "Запустите таймер, направляйте отстающих."],
    ["Проверка", "Чек-лист проверки: валидация строк FLAG{...}.", "Сверьте флаги на экранах."],
    ["Критерии", "10-балльная шкала оценивания практической работы.", "Озвучьте правила начисления баллов."],
    ["Итоги", "Завершение 5-й недели. Поздравьте класс с освоением курса защиты серверов!", "Соберите рабочие листы."]
]

N_EN = [
    ["Intro", "Lesson opening: Week 5 capstone — Capture The Flag (CTF) cyber war games.", "Set an energized competitive learning atmosphere."],
    ["Red vs Blue", "Red Team vs Blue Team: Adversary emulation vs SOC defense.", "Differentiate offensive vs defensive mission mandates."],
    ["Kill Chain", "The Cyber Kill Chain: 7 phases from initial recon to action on objectives.", "Break down intrusion progression steps."],
    ["Log Forensics", "System log threat hunting in auth.log and access.log.", "Demonstrate grep/awk log filtering pipelines."],
    ["CTF Architecture", "The FLAG{...} standard: Cryptographic attestation of captured assets.", "Clarify flag extraction criteria."],
    ["Incident Response", "The 4 containment imperatives: Why pulling the power plug is catastrophic.", "Highlight volatile RAM forensics preservation."],
    ["SolarWinds Breach", "The SolarWinds supply chain breach: Trojanized build pipelines.", "Analyze strategic cyber espionage lessons."],
    ["Mission Briefing", "CTF cyber range briefing: 3 objective flags.", "Issue rules of engagement."],
    ["Hands-On CTF", "14-minute live CTF: Students hunt flags across Nmap, Wireshark, and SQLi.", "Start 14-minute countdown timer and supervise."],
    ["Verification", "Flag validation audit checklist.", "Verify captured flag submissions."],
    ["Evaluation", "10-point evaluation rubric breakdown.", "Review grading thresholds."],
    ["Summary", "Week 5 conclusion and congratulations on mastering production cyber defense!", "Collect worksheets."]
]

NOTES = {"uz": N_UZ, "ru": N_RU, "en": N_EN}

# ---------------------------------------------------------------- Varaqa Body
V = []
V.append(sheet_header(
    h1=("Kiberxavfsizlik: CTF & Red/Blue Team Mudofaasi",
        "Кибербезопасность: CTF и Защита Red/Blue Team",
        "CyberSecurity: CTF & Red/Blue Team Defense"),
    sub=("Amaliy Laboratoriya Varaqasi · 9-sinf · 5-hafta · 25-dars (Final)",
         "Практический Рабочий Лист · 9 класс · Неделя 5 · Урок 25 (Финал)",
         "Hands-On Lab Worksheet · Grade 9 · Week 5 · Lesson 25 (Finale)")
))

V.append(mission(
    h=("CTF Vazifasi: 3 Ta Kiber-Bayroqni Qo'lga Kiritish",
       "Миссия CTF: Захват 3 Кибер-Флагов",
       "CTF Mission: Capture All 3 Cyber Defense Flags"),
    p=("Nmap port razvedkasi, Wireshark paket tahlili va OWASP SQL Injection zaifliklarini ochish orqali "
       "kiber-poligondagi 3 ta yashirin FLAG{...} ni topish va tizimni xavfsiz holatga qaytarish.",
       "Используя Nmap, сниффинг в Wireshark и эксплуатацию SQL-инъекции, обнаружить 3 скрытых флага FLAG{...} "
       "и задокументировать шаги защиты системы.",
       "Leverage Nmap port auditing, Wireshark packet decryption, and SQL injection exploitation "
       "to capture 3 hidden FLAG{...} tokens across the cyber range and document incident recovery."))
)

V.append(table(
    headers=[
        ("Bayroq Nomi", "Флаг", "Objective Flag"),
        ("Qo'llanilgan Usul", "Метод Захвата", "Exploitation Method"),
        ("Topilgan FLAG Qiymati", "Значение Флага", "Captured Flag Value"),
        ("Holat", "Статус", "Status")
    ],
    rows=[
        [("FLAG 1 (Linux & SSH)", "Флаг 1 (SSH)", "FLAG 1 (SSH)"),
         ("`nmap` yuqori portni topish va SSH", "Сканирование `nmap` и вход по SSH", "Nmap port sweep & SSH shell"),
         ("FLAG{ssh_ed25519_k3y_s3cur3d}", "FLAG{ssh_ed25519_k3y_s3cur3d}", "FLAG{ssh_ed25519_k3y_s3cur3d}"),
         ("✅ Qo'lga kiritildi", "✅ Захвачен", "✅ Captured")],
        [("FLAG 2 (Wireshark)", "Флаг 2 (Wireshark)", "FLAG 2 (Wireshark)"),
         ("Wireshark: `http.request.method == \"POST\"`", "Фильтр HTTP POST в Wireshark", "Wireshark HTTP POST stream filter"),
         ("FLAG{w1r3shark_sn1ff3d_c00k1e}", "FLAG{w1r3shark_sn1ff3d_c00k1e}", "FLAG{w1r3shark_sn1ff3d_c00k1e}"),
         None],
        [("FLAG 3 (SQLi AppSec)", "Флаг 3 (SQLi)", "FLAG 3 (SQLi)"),
         ("Qidiruv maydonida `' OR '1'='1`", "Внедрение `' OR '1'='1` в форму", "SQLi injection payload `' OR '1'='1`"),
         ("FLAG{sql1_pr3p4r3d_st4t3m3nts_w1n}", "FLAG{sql1_pr3p4r3d_st4t3m3nts_w1n}", "FLAG{sql1_pr3p4r3d_st4t3m3nts_w1n}"),
         None],
    ]
))

V.append(sheet_box(
    h=("Kiber-Insident Forensika Tahlili", "Форензика Инцидента и Вопросы", "Incident Forensics & Post-Mortem"),
    body_html=writelines(3, label=("1. Nega server buzilgan paytda uni elektrdan yoki restart orqali o'chirib qo'yish kiber-surishtiruvga katta zarar yetkazadi?",
                                   "1. Почему выключение или перезагрузка взломанного сервера уничтожает ключевые улики?",
                                   "1. Why is powering down or rebooting a compromised server catastrophic to forensic investigation?"))
             + "<br>"
             + writelines(3, label=("2. SolarWinds kiber-hujumidan xulosa qilgan holda, Zero Trust arxitekturasi nega 'hech kimga ishonma' qoidasini ilgari suradi?",
                                   "2. Исходя из кейса SolarWinds, почему модель Zero Trust требует проверять даже доверенный софт?",
                                   "2. Drawing from the SolarWinds incident, why does Zero Trust mandate continuous verification of even trusted vendors?"))
))

V.append(sheet_box(
    h=("Baholash Mezoni (10 Ball)", "Критерии Оценки (10 Баллов)", "Grading Rubric (10 Points)"),
    body_html=rubric([
        (("3 ta bayroqning barchasi topilib, to'g'ri qayd etilgan", "Все 3 флага захвачены и задокументированы", "All 3 flags captured and transcribed"), "4 ball"),
        (("Hujum usullari va zaiflik sabablari aniq tushuntirilgan", "Уязвимости и методы атак объяснены точно", "Exploit vectors and root causes explained"), "3 ball"),
        (("Forensika tahlili savollariga asosli professional javob yozilgan", "Даны развернутые ответы на вопросы форензики", "Forensic analysis queries thoroughly answered"), "2 ball"),
        (("Varaqa to'liq va tartibli to'ldirilgan", "Рабочий лист оформлен аккуратно и полностью", "Worksheet completed cleanly and thoroughly"), "1 ball"),
    ], "10 ball")
))

V.append("</div>\n" + sign_box("Musulmonov Mamarajab"))

VARAQA_BODY = "\n".join(V)

lesson = Lesson(
    outdir=D,
    titles=TITLES,
    sheet_titles=SHEET_TITLES,
    key="vc-notes-9-25",
    slides=S,
    notes=NOTES,
    varaqa_body=VARAQA_BODY
)

if __name__ == "__main__":
    out = lesson.build()
    print("Created:", out)
