# -*- coding: utf-8 -*-
"""9-sinf · 5-hafta · 21-dars — Linux Server Xavfsizligi va SSH Himoyasi: Serverni Qulflash va Portlarni Nazorat Qilish."""

import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from build import (Lesson, slide, title_slide, box, code, el, i18n,
                   sheet_header, mission, table, sheet_box, rubric, writelines, sign_box)

D = "classes/9-sinf/5-hafta/21-dars-linux-server-va-ssh-himoyasi"

TITLES = {
    "uz": "21-dars: Linux Server Xavfsizligi va SSH Himoyasi — Serverni Qulflash",
    "ru": "Урок 21: Безопасность Linux-Сервера и Защита SSH — Блокировка Угроз",
    "en": "Lesson 21: Linux Server Hardening & SSH Defense — Locking Down Production",
}
SHEET_TITLES = {k: v + (" — Ish Varaqasi" if k == "uz" else
                        " — Рабочий Лист" if k == "ru" else " — Worksheet")
                for k, v in TITLES.items()}

S = []

# 1. Title Slide
S.append(title_slide(
    ph=("Kirish", "Введение", "Intro"), time="0–3",
    eyebrow=("CyberSecurity · 21-dars · 9-sinf (Server Defense Track)",
             "CyberSecurity · Урок 21 · 9 класс (Server Defense Track)",
             "CyberSecurity · Lesson 21 · Grade 9 (Server Defense Track)"),
    h1=("Linux Server Xavfsizligi va SSH Himoyasi",
        "Безопасность Linux-Сервера и Защита SSH",
        "Linux Server Hardening & SSH Key Defense"),
    lede=("Internetga ulangan har bir Linux server har soniyada minglab avtomatlashgan botlar va parollarni taxmin qiluvchi "
          "<b>Brute-force</b> hujumlariga uchraydi. Standart sozlamalar va ochiq root paroli — buzib kirishga ochiq taklifnomadir. "
          "Bugungi darsda siz serverni sanoat standartida himoyalashni: <b>Ed25519 SSH kalitlari</b> orqali parolsiz kirishni, "
          "standart 22-portni o'zgartirishni, <b>UFW Firewall</b> devorini qurishni va <b>Fail2ban</b> orqali hujumchilarni avtomatik bloklashni o'rganasiz.",
          "Каждый Linux-сервер в интернете ежесекундно атакуют тысячи ботнетов с помощью <b>Brute-force</b> перебора паролей. "
          "Стандартные настройки и открытый root-пароль — прямой билет для взломщиков. "
          "Сегодня вы научитесь профессиональному харденингу серверов: входу без пароля по <b>ключам SSH Ed25519</b>, "
          "смене порта 22, настройке межсетевого экрана <b>UFW Firewall</b> и автобану атак через <b>Fail2ban</b>.",
          "Every Linux server exposed to the public internet suffers relentless automated <b>Brute-force</b> attacks every second. "
          "Default settings and password-enabled root access are an open invitation to breach. "
          "Today you will master enterprise server hardening: passwordless <b>Ed25519 SSH keypairs</b>, "
          "port relocation, <b>UFW Firewall</b> configuration, and automated attacker blacklisting with <b>Fail2ban</b>."),
    meta=[("<b>Fan:</b> Kiberxavfsizlik · Linux Server Defense",
           "<b>Предмет:</b> Кибербезопасность · Защита Серверов Linux",
           "<b>Subject:</b> CyberSecurity · Linux Server Defense"),
          ("<b>Kohorta:</b> 9-sinf Kiber-Muhandis",
           "<b>Когорта:</b> 9 класс Кибер-Инженер",
           "<b>Cohort:</b> Grade 9 Cyber-Engineer"),
          ("<b>Hafta:</b> 5 (1-soat)", "<b>Неделя:</b> 5 (1-й час)", "<b>Week:</b> 5 (Hour 1)")],
))

# 2. Problem: The Scanner Storm
S.append(slide(
    ph=("Xavf Tahlili", "Анализ Угроз", "Threat Vector"), time="3–6",
    eyebrow=("Internetdagi real xavf", "Реальная угроза в интернете", "Real Internet Threat"),
    title=("22-Port Bo'ron: Nega Standart Server 5 Daqiqada Buziladi?",
           "Шторм 22-го Порта: Почему Дефолтный Сервер Ломают за 5 Минут?",
           "Port 22 Storm: Why Default Servers Fall Within 5 Minutes"),
    body='<div class="cols c2">\n'
         + box("accent", ("Brute-Force va Botnet Hujumlari", "Brute-Force и Ботнеты", "Brute-Force & Botnet Storms"),
               items=[
                   ("<b>Global skanerlar:</b> Shodan va botnetlar doimiy ravishda ochiq 22-portlarni qidiradi.",
                    "<b>Глобальные сканеры:</b> Shodan и ботнеты непрерывно сканируют интернет в поисках порта 22.",
                    "<b>Global scanners:</b> Shodan and botnets scan public IPv4 ranges 24/7 for port 22."),
                   ("<b>Lug'at hujumlari:</b> 'root', 'admin', 'ubuntu' kabi foydalanuvchilarga millionlab parollar sinab ko'riladi.",
                    "<b>Словарные атаки:</b> Миллионы попыток подбора паролей к учеткам 'root', 'admin', 'ubuntu'.",
                    "<b>Dictionary attacks:</b> Millions of password permutations pummel default accounts."),
                   ("<b>Resurslar o'g'irlanishi:</b> Server buzilsa, u darhol kiber-qurol yoki kripto-maynerga aylanadi.",
                    "<b>Кража ресурсов:</b> Скомпрометированный сервер становится зомби-нодой или майнером.",
                    "<b>Resource hijacking:</b> Compromised servers are immediately weaponized into DDoS nodes."),
               ])
         + box("purple", ("Statistika va Faktlar", "Статистика и Факты", "Telemetry & Hard Facts"),
               p=("Yangi ochilgan virtual server (VPS) internetga ulangach, birinchi hujum o'rtacha <b>3 daqiqa 40 soniyada</b> boshlanadi. Kuniga 1 ta serverga o'rtacha <b>12 000 dan ortiq</b> ruxsatsiz kirish urinishlari yoziladi.",
                  "Новый виртуальный сервер (VPS) в интернете подвергается первой атаке в среднем через <b>3 минуты 40 секунд</b>. За сутки фиксируется свыше <b>12 000 попыток</b> несанкционированного входа.",
                  "A newly provisioned VPS faces its first intrusion attempt within an average of <b>3 minutes 40 seconds</b>. Over <b>12,000 automated login attempts</b> strike per day per IP."))
         + '\n</div>'
))

# 3. SSH Key Architecture
S.append(slide(
    ph=("Arxitektura", "Архитектура", "Architecture"), time="6–10",
    eyebrow=("Kriptografik kirish", "Криптографический доступ", "Cryptographic Access"),
    title=("SSH Kalitlar Qanday Ishlaydi? Ochiq va Maxfiy Kalit Juftligi",
           "Как Работают SSH-Ключи? Пара Открытого и Закрытого Ключей",
           "How SSH Keys Work: The Asymmetric Public/Private Keypair"),
    body='<div class="cols c3">\n'
         + box("", ("1. Maxfiy Kalit (Private Key)", "1. Закрытый Ключ (Private Key)", "1. Private Key (Secret)"),
               p=("Sizning noutbukingizda qoladi (`~/.ssh/id_ed25519`). <b>Hech qachon</b> serverga yoki internetga yuborilmaydi. Shaxsiy raqamli imzo vazifasini bajaradi.",
                  "Хранится только на вашем компьютере (`~/.ssh/id_ed25519`). <b>Никогда</b> не передается по сети. Служит цифровой подписью.",
                  "Resides exclusively on your laptop (`~/.ssh/id_ed25519`). <b>Never</b> transmitted across networks. Acts as your digital signature."),
               extra_html='<span class="tag purple" %s>Maxfiy · Qattiq himoya</span>' % i18n("Maxfiy · Qattiq himoya", "Секретно · Строгий доступ", "Strictly Confidential"))
         + box("", ("2. Ochiq Kalit (Public Key)", "2. Открытый Ключ (Public Key)", "2. Public Key (Public)"),
               p=("Serverdagi `~/.ssh/authorized_keys` fayliga yoziladi (`.pub`). Uni istalgan odam ko'rishi mumkin. Bu qulf vazifasini bajaradi.",
                  "Записывается на сервер в `~/.ssh/authorized_keys` (`.pub`). Может быть публичным. Выступает в роли криптографического замка.",
                  "Copied to the server inside `~/.ssh/authorized_keys` (`.pub`). Can be shared openly. Acts as the cryptographic lock."),
               extra_html='<span class="tag green" %s>Ochiq · Serverga yuklanadi</span>' % i18n("Ochiq · Serverga yuklanadi", "Открытый · На сервер", "Public · On Server"))
         + box("accent", ("3. Challenge-Response Muloqot", "3. Проверка Challenge-Response", "3. Challenge-Response Handshake"),
               p=("Server tasodifiy son (challenge) yaratib ochiq kalit bilan shifrlaydi. Noutbuk uni maxfiy kalit bilan yechib qaytaradi. <b>Parol tarmoqqa chiqmaydi!</b>",
                  "Сервер шифрует случайное число открытым ключом. Ваш ПК расшифровывает закрытым ключом. <b>Пароль не передается по сети!</b>",
                  "Server encrypts a random nonce with public key. Laptop decrypts it using private key. <b>Zero credentials cross the wire!</b>"),
               extra_html='<span class="tag red" %s>100%% Brute-Forcega chidamli</span>' % i18n("100% Brute-Forcega chidamli", "100% Устойчивость к перебору", "100% Brute-Force Proof"))
         + '\n</div>'
))

# 4. Linux Hardening Steps
S.append(slide(
    ph=("Himoya Rejasi", "План Харденинга", "Hardening Plan"), time="10–14",
    eyebrow=("Standart muhandislik amaliyoti", "Инженерный протокол", "Engineering Protocol"),
    title=("Serverni Qulflashning 4 Ta Oltin Qoidasi (Hardening Checklist)",
           "4 Золотых Правила Харденинга Сервера (Hardening Checklist)",
           "The 4 Golden Rules of Linux Server Hardening"),
    body='<div class="cols c2">\n'
         + box("accent", ("1. Root Parolini va Loginini O'chirish", "1. Отключение Паролей и Root", "1. Disable Root & Password Auth"),
               items=[
                   ("`PermitRootLogin no` — to'g'ridan-to'g'ri root bo'lib kirishni man etish.",
                    "`PermitRootLogin no` — полный запрет прямого входа под суперпользователем.",
                    "`PermitRootLogin no` — completely prohibit direct root logins."),
                   ("`PasswordAuthentication no` — parolli kirishni butunlay to'xtatish (faqat SSH kalit).",
                    "`PasswordAuthentication no` — выключение входа по паролям (только SSH-ключи).",
                    "`PasswordAuthentication no` — disable all password authentications."),
                   ("Har bir dasturchi o'z nomidagi `sudo` foydalanuvchisi bilan kirishi shart.",
                    "Каждый инженер заходит под личным пользователем с правами `sudo`.",
                    "Every operator uses an individual named user with `sudo` privileges."),
               ])
         + box("green", ("2. Port Ko'chirish va Tarmoq Himoyasi", "2. Смена Порта и Фаервол", "2. Port Relocation & Firewall"),
               items=[
                   ("<b>Port 22 -> 2222:</b> Standart portni o'zgartirish botnet skanerlarining 99% ini to'xtatadi.",
                    "<b>Порт 22 -> 2222:</b> Смена порта отсекает 99% автоматических сканеров ботнетов.",
                    "<b>Port 22 -> 2222:</b> Relocating the port eliminates 99% of noisy botnet probes."),
                   ("<b>UFW Firewall:</b> Faqat kerakli portlarni (80, 443, 2222) ochib, qolgan barchasini yopish.",
                    "<b>UFW Firewall:</b> Открытие только рабочих портов (80, 443, 2222), остальное заблокировано.",
                    "<b>UFW Firewall:</b> Whitelist only needed ports (80, 443, 2222), drop all ingress traffic."),
                   ("<b>Fail2ban:</b> 3 marta noto'g'ri uringan IP manzilni 24 soatga iptables darajasida qora ro'yxatga olish.",
                    "<b>Fail2ban:</b> Автоматический бан IP в фаерволе после 3 неудачных попыток входа.",
                    "<b>Fail2ban:</b> Automated dynamic ban for 24 hours after 3 failed handshakes."),
               ])
         + '\n</div>'
))

# 5. sshd_config in action
S.append(slide(
    ph=("Konfiguratsiya", "Конфигурация", "Configuration"), time="14–18",
    eyebrow=("/etc/ssh/sshd_config", "/etc/ssh/sshd_config", "/etc/ssh/sshd_config"),
    title=("Haqiqiy Xavfsiz SSH Konfiguratsiyasi (sshd_config)",
           "Боевая Безопасная Конфигурация SSH (sshd_config)",
           "Production-Hardened SSH Daemon Configuration"),
    body='<div class="cols c2">\n'
         + box("", ("sshd_config Faylidagi Kalit Sozlamalar", "Ключевые Параметры sshd_config", "Core sshd_config Parameters"),
               items=[
                   ("<b>Port 2222:</b> Standart port o'rniga noan'anaviy yuqori port.",
                    "<b>Port 2222:</b> Нестандартный порт вместо порта по умолчанию.",
                    "<b>Port 2222:</b> Non-standard port evasion."),
                   ("<b>PermitRootLogin no:</b> Root hisobi xakerlar uchun asosiy nishon bo'lgani sababli yopiladi.",
                    "<b>PermitRootLogin no:</b> Закрытие прямого доступа к суперюзеру.",
                    "<b>PermitRootLogin no:</b> Disables attacks against the ubiquitous root account."),
                   ("<b>PasswordAuthentication no:</b> Parolli hujumlarni ildizi bilan yo'q qiladi.",
                    "<b>PasswordAuthentication no:</b> Исключает вероятность перебора паролей.",
                    "<b>PasswordAuthentication no:</b> Eliminates all brute-force vulnerabilities."),
                   ("<b>MaxAuthTries 3:</b> 3 ta muvaffaqiyatsiz urinishdan so'ng sessiya uziladi.",
                    "<b>MaxAuthTries 3:</b> Разрыв соединения после 3 ошибок.",
                    "<b>MaxAuthTries 3:</b> Kills TCP stream after 3 failed auth handshakes."),
               ])
         + '<div class="box accent">\n'
         + el("h3", "sshd_config Xavfsizlik Bloki", "Блок Безопасности sshd_config", "Hardened sshd_config Snippet")
         + code("""# /etc/ssh/sshd_config.d/hardened.conf
Port 2222
Protocol 2
PermitRootLogin no
PasswordAuthentication no
PubkeyAuthentication yes
AuthorizedKeysFile .ssh/authorized_keys
MaxAuthTries 3
ClientAliveInterval 300
ClientAliveCountMax 2
X11Forwarding no""")
         + '</div>\n</div>'
))

# 6. UFW Firewall
S.append(slide(
    ph=("Firewall", "Фаервол", "Firewall"), time="18–22",
    eyebrow=("Tarmoq qalqoni", "Сетевой щит", "Network Shield"),
    title=("UFW (Uncomplicated Firewall): Server Chegarasini Himoyalash",
           "UFW: Защита Периметра Сервера",
           "UFW Firewall: Enforcing Strict Ingress Whitelisting"),
    body='<div class="cols c2">\n'
         + box("green", ("UFW Xavfsizlik Buyruqlari", "Команды Управления UFW", "UFW Security Directives"),
               items=[
                   ("<b>Default Deny:</b> Barcha kiruvchi ulanishlarni sukut bo'yicha bloklash.",
                    "<b>Default Deny:</b> Запрет всех входящих соединений по умолчанию.",
                    "<b>Default Deny:</b> Block all inbound requests unless explicitly whitelisted."),
                   ("<b>SSH Portini ochish:</b> Avval yangi portni ochmasdan UFW ni yoqmang!",
                    "<b>Открыть SSH:</b> Никогда не включайте UFW, не открыв свой порт SSH!",
                    "<b>Allow SSH First:</b> Never enable UFW before explicitly punching through your SSH port!"),
                   ("<b>Veb-trafik:</b> 80 (HTTP) va 443 (HTTPS) portlariga ruxsat berish.",
                    "<b>Веб-порты:</b> Разрешение легитимного веб-трафика 80 и 443.",
                    "<b>Web ports:</b> Allow standard 80 (HTTP) and 443 (HTTPS) services."),
               ])
         + '<div class="box purple">\n'
         + el("h3", "Terminalda UFW Ni Ishga Tushirish", "Запуск UFW в Терминале", "Executing UFW in Terminal")
         + code("""# 1. Barcha kiruvchilarni yopish
sudo ufw default deny incoming
sudo ufw default allow outgoing

# 2. Xavfsiz SSH va Veb portlarni ochish
sudo ufw allow 2222/tcp comment 'Hardened SSH'
sudo ufw allow 80/tcp   comment 'Web HTTP'
sudo ufw allow 443/tcp  comment 'Web HTTPS SSL'

# 3. Faollashtirish va holatni tekshirish
sudo ufw enable
sudo ufw status verbose""")
         + '</div>\n</div>'
))

# 7. Fail2ban Defense
S.append(slide(
    ph=("Avtomat Himoya", "Автозащита", "Active Defense"), time="22–26",
    eyebrow=("Aqlli mudofaa", "Интеллектуальная защита", "Intelligent IPS"),
    title=("Fail2ban: Hujumchilarni Jonli Efirda Izolyatsiya Qilish",
           "Fail2ban: Автоматическая Блокировка Атакующих в Реальном Времени",
           "Fail2ban: Real-Time Intrusion Prevention & Dynamic Blacklisting"),
    body='<div class="cols c2">\n'
         + box("", ("Qanday Ishlaydi?", "Принцип Работы", "How It Operates"),
               items=[
                   ("<b>Loglarni skanerlaydi:</b> `/var/log/auth.log` faylidagi har bir kirish urinishini kuzatadi.",
                    "<b>Мониторит логи:</b> Непрерывно анализирует системный журнал `/var/log/auth.log`.",
                    "<b>Continuous log analysis:</b> Streams and parses auth events from `/var/log/auth.log`."),
                   ("<b>Qoidabuzarlikni hisoblaydi:</b> Masalan, 10 daqiqa ichida 3 ta xato urinish.",
                    "<b>Считает нарушения:</b> Фиксирует 3 неудачные попытки за 10 минут (maxretry).",
                    "<b>Violation scoring:</b> Tracks threshold violations (e.g. 3 failures within findtime)."),
                   ("<b>Iptables qoidasi yozadi:</b> Hujumchi IP-si to'g'ridan-to'g'ri Linux yadrosida bloklanadi.",
                    "<b>Добавляет бан в iptables:</b> IP блокируется мгновенно на уровне сетевого стека ядра.",
                    "<b>Kernel drop:</b> Injects drop rules directly into kernel iptables/nftables chains."),
               ])
         + '<div class="box accent">\n'
         + el("h3", "Fail2ban Jail Sozlamasi (jail.local)", "Конфиг Дрожания Fail2ban", "Fail2ban Jail Configuration")
         + code("""# /etc/fail2ban/jail.d/sshd.local
[sshd]
enabled  = true
port     = 2222
filter   = sshd
logpath  = /var/log/auth.log
maxretry = 3
findtime = 600
bantime  = 86400  # 24 soatga to'liq bloklash!

# Bloklangan IP larni ko'rish:
# sudo fail2ban-client status sshd""")
         + '</div>\n</div>'
))

# 8. Live Incident / Case Study
S.append(slide(
    ph=("Real Keys", "Кейс из Жизни", "Case Study"), time="26–30",
    eyebrow=("Haqiqiy insident tahlili", "Анализ инцидента", "Security Post-Mortem"),
    title=("Kompaniyaning 50 000$ Lik Xatosi: Ochiq Root Paroli",
           "Ошибка на $50 000: Оставленный Пароль от Root",
           "The $50,000 Mistake: Default Root Password Left Exposed"),
    body='<div class="cols c2">\n'
         + box("accent", ("Voqea Tafsiloti", "Хронология Инцидента", "Incident Timeline"),
               p=("Stajyor dasturchi test maqsadida AWS EC2 server ochadi va tezda kirish uchun <code>root:admin2024!</code> parolini o'rnatadi. 2 soat o'tgach, serverga Xitoy va Sharqiy Yevropa botnetlari kirib oladi.",
                  "Стажёр для тестов создал сервер AWS EC2 со слабым паролем <code>root:admin2024!</code>. Спустя всего 2 часа ботнеты подобрали пароль и захватили инстанс.",
                  "An intern created a staging AWS EC2 instance with default password <code>root:admin2024!</code> for quick testing. Within 2 hours, automated scanners cracked the server."))
         + box("purple", ("Natijalar va Xarajatlar", "Последствия и Убытки", "Consequences & Blast Radius"),
               items=[
                   ("<b>Kripto-mayning:</b> Serverda Monero mayneri ishga tushirilib, AWS hisobi <b>50 000$</b> ga yetadi.",
                    "<b>Майнинг:</b> На сервере запустили майнинг Monero, счёт за серверы взлетел до $50 000.",
                    "<b>Crypto-jacking:</b> Monero miners pinned CPUs at 100%, racking up a $50,000 AWS bill."),
                   ("<b>Ma'lumotlar sizishi:</b> Serverdagi barcha mijozlar bazasi o'g'irlanadi va Darknetga sotuvga qo'yiladi.",
                    "<b>Утечка базы:</b> База данных клиентов была украдена и выставлена в даркнет.",
                    "<b>Data exfiltration:</b> Staging production database clone was dumped and sold on breach forums."),
                   ("<b>Oddiy yechim:</b> Agar SSH kalit o'rnatilib, parol o'chirilganda, bu hujum 0% muvaffaqiyatga ega bo'lardi!",
                    "<b>Вывод:</b> Всего один SSH-ключ с отключённым паролем свёл бы риск к нулю!",
                    "<b>Takeaway:</b> Disabling password auth and enforcing Ed25519 keys would have made this 100% impossible!"),
               ])
         + '\n</div>'
))

# 9. Practical Mission (12 min timer)
S.append(slide(
    ph=("Amaliyot", "Практика", "Hands-On Lab"), time="30–42",
    eyebrow=("Mustaqil laboratoriya · 12 daqiqa", "Лабораторная работа · 12 минут", "Practical Lab · 12 Minutes"),
    title=("Amaliy Topshiriq: Kiber-Serverni Qulflash Protokoli",
           "Практическое Задание: Протокол Защиты Сервера",
           "Mission: Execute Complete Server Hardening Protocol"),
    body='<div class="cols c2">\n'
         + box("green", ("Laboratoriya Bosqichlari", "Шаги Лабораторной", "Mission Checkpoints"),
               items=[
                   ("<b>1. SSH Kalit generatsiya:</b> `ssh-keygen -t ed25519 -C 'ismingiz@target.uz'`",
                    "<b>1. Генерация ключа:</b> `ssh-keygen -t ed25519 -C 'ваше_имя@target.uz'`",
                    "<b>1. Keypair generation:</b> Generate modern Ed25519 curve keypair."),
                   ("<b>2. Kalitni serverga yuklash:</b> `ssh-copy-id -i ~/.ssh/id_ed25519.pub user@server`",
                    "<b>2. Копирование ключа:</b> `ssh-copy-id -i ~/.ssh/id_ed25519.pub user@server`",
                    "<b>2. Authorize public key:</b> Copy public key to authorized_keys on VPS."),
                   ("<b>3. sshd_config ni tahrirlash:</b> Port 2222, Root va Parol o'chiriladi.",
                    "<b>3. Настройка sshd:</b> Порт 2222, отключение Root и паролей.",
                    "<b>3. Lock sshd:</b> Enforce port 2222, disable root & passwords."),
                   ("<b>4. UFW va Fail2ban:</b> Port 2222, 80, 443 ruxsat berilib, faollashtiriladi.",
                    "<b>4. Фаервол и бан:</b> Открытие 2222, 80, 443 и запуск защиты.",
                    "<b>4. Firewalls up:</b> Whitelist active ports and verify Fail2ban jail status."),
               ])
         + box("accent", ("O'lchanadigan Natija (Definition of Done)", "Критерий Сдачи", "Deliverable Spec"),
               p=("Terminalda parolsiz `ssh -p 2222 user@server` orqali ulanish muvaffaqiyatli o'tishi va parolli urinish <b>\"Permission denied (publickey)\"</b> xatosi bilan darhol rad etilishi shart!",
                  "Успешное подключение без пароля `ssh -p 2222 user@server` и мгновенный отказ на ввод пароля с ошибкой <b>«Permission denied (publickey)»</b>!",
                  "Verified passwordless login via `ssh -p 2222 user@server` while legacy password attempts instantly fail with <b>\"Permission denied (publickey)\"</b>!"))
         + '\n</div>'
))

# 10. Verification Checklist
S.append(slide(
    ph=("Tekshirish", "Чек-лист", "Verification"), time="42–43",
    eyebrow=("Kiber-inspeksiya", "Аудит безопасности", "Security Audit"),
    title=("Xavfsizlik Auditi: 5 Ta Nazorat Nuqtasi",
           "Аудит Безопасности: 5 Контрольных Точек",
           "Post-Hardening Verification Checklist"),
    body='<div class="cols c3">\n'
         + box("", ("1. Kalit Turi", "1. Алгоритм Ключа", "1. Key Algorithm"),
               p=("Ed25519 ishlatildimi? RSA-1024 kabi eskirgan zaif kalitlar taqiqlanadi.",
                  "Использован ли Ed25519? Устаревший RSA-1024 строго запрещён.",
                  "Is Ed25519 active? Outdated RSA-1024 is strictly non-compliant."))
         + box("", ("2. Parol O'chiqmi?", "2. Пароли Отключены?", "2. Password Auth Off?"),
               p=("`PasswordAuthentication no` tekshirildimi? Parol bilan kirish urinishi xato berishi shart.",
                  "Проверено `PasswordAuthentication no`? Попытка входа по паролю блокируется.",
                  "Verified `PasswordAuthentication no`? Password prompts must never appear."))
         + box("", ("3. UFW Holati", "3. Статус UFW", "3. UFW Active?"),
               p=("`sudo ufw status` holati 'active' va faqat 2222, 80, 443 ochiqmi?",
                  "Статус `sudo ufw status` — 'active' и открыты только порты 2222, 80, 443?",
                  "`sudo ufw status` shows 'active' with only 2222, 80, 443 allowed?"))
         + '\n</div>'
))

# 11. Rubric (10-Ball)
S.append(slide(
    ph=("Mezon", "Критерии", "Evaluation"), time="43–44",
    eyebrow=("10 ballik tizim", "10-балльная шкала", "10-Point Rubric"),
    title=("Darsni Baholash Mezonlari (10 Ball)",
           "Критерии Оценки за Урок (10 Баллов)",
           "Lesson Evaluation Rubric (10 Points)"),
    body='<div class="cols c3">\n'
         + box("green", ("A'lo (9–10 Ball)", "Отлично (9–10)", "Exemplary (9–10)"),
               items=[
                   ("Ed25519 kalit generatsiya qilingan.", "Сгенерирован ключ Ed25519.", "Ed25519 keypair created."),
                   ("Port 2222 ga o'zgartirilgan va root o'chirilgan.", "Порт 2222, root отключён.", "Port 2222 active, root disabled."),
                   ("UFW va Fail2ban faol ishlamoqda.", "UFW и Fail2ban полностью настроены.", "UFW & Fail2ban fully operational."),
                   ("Varaqa 100% to'ldirilgan.", "Лист заполнен на 100%.", "Worksheet completed 100%."),
               ])
         + box("", ("Yaxshi (7–8 Ball)", "Хорошо (7–8)", "Proficient (7–8)"),
               items=[
                   ("SSH kalit o'rnatilgan, parollar o'chirilgan.", "Ключ настроен, пароли выключены.", "SSH key active, passwords disabled."),
                   ("UFW yoqilgan, lekin port 22 da qolgan.", "UFW включен, но порт остался 22.", "UFW enabled, but default port 22 kept."),
                   ("Varaqa 80% to'ldirilgan.", "Лист заполнен на 80%.", "Worksheet completed 80%."),
               ])
         + box("accent", ("Qoniqarli (5–6 Ball)", "Удовл. (5–6)", "Developing (5–6)"),
               items=[
                   ("Faqat kalit yaratilgan, server sozlanmagan.", "Только создан ключ, конфиг не изменён.", "Only key generated, sshd unconfigured."),
                   ("UFW yoqilmagan yoki xatoliklar bor.", "Фаервол не запущен или ошибки в портах.", "Firewall offline or misconfigured."),
                   ("Varaqa to'liq emas.", "Лист заполнен частично.", "Worksheet incomplete."),
               ])
         + '\n</div>'
))

# 12. Summary & Homework
S.append(slide(
    ph=("Xulosa", "Итоги", "Summary"), time="44–45",
    eyebrow=("Uyga vazifa", "Домашнее задание", "Homework & Next Steps"),
    title=("Xulosa va Uy Vazifasi: O'z Serveringizni Himoyalang",
           "Итоги и Домашнее Задание: Защитите Свой Сервер",
           "Summary & Homework: Harden Your Production Environment"),
    body='<div class="cols c2">\n'
         + box("purple", ("Dars Xulosasi", "Итоги Урока", "Core Summary"),
               p=("Linux xavfsizligi tasodif emas — bu qat'iy qoidalar zanjiri. SSH kaliti + Port o'zgartirish + UFW Firewall + Fail2ban kombinatsiyasi serveringizni internetdagi ommaviy avtomatlashgan hujumlarning 99.9% idan ishonchli himoya qiladi.",
                  "Безопасность Linux — это не случайность, а система. Связка SSH-ключей, смены порта, UFW и Fail2ban отсекает 99.9% всех массовых атак в интернете.",
                  "Linux security is a deterministic discipline. The combination of Ed25519 keys, non-standard ports, UFW whitelisting, and Fail2ban filters eliminates 99.9% of all automated internet botnet intrusions."))
         + box("accent", ("Uy Vazifasi (10 Ball)", "Домашнее Задание (10 Баллов)", "Homework Assignment (10 Pts)"),
               items=[
                   ("<b>Amaliy:</b> O'z kompyuteringizda yoki virtual mashinada Ed25519 SSH kalit juftligini yarating.",
                    "<b>Практика:</b> Сгенерируйте пару ключей Ed25519 на своём ПК или виртуальной машине.",
                    "<b>Hands-on:</b> Generate a secure Ed25519 keypair on your local workstation."),
                   ("<b>Tahlil:</b> `auth.log` faylidan muvaffaqiyatsiz kirish urinishlarini `grep 'Failed password'` bilan tahlil qiling.",
                    "<b>Анализ:</b> Проанализируйте `auth.log` на наличие сбоев с помощью команды `grep 'Failed password'`.",
                    "<b>Analysis:</b> Inspect authentication logs using `grep 'Failed password'` to count attacks."),
                   ("<b>Varaqa:</b> Ish varaqasidagi barcha kiber-xavfsizlik savollarini to'ldirib topshiring.",
                    "<b>Лист:</b> Заполните рабочий лист и сдайте на проверку.",
                    "<b>Submission:</b> Complete and submit your printable lab worksheet."),
               ])
         + '\n</div>'
))

# Teacher Notes
N_UZ = [
    ["Kirish", "Darsni boshlash: Bugun biz haqiqiy kiberxavfsizlikka qadam qo'yamiz. Internetdagi serverlar qanday hujumga uchrashini ko'rsatamiz.", "Slaydni oching, o'quvchilarga internetda har qanday server daqiqalar ichida nishonga aylanishini tushuntiring."],
    ["Xavf Tahlili", "Brute-force nima? Botnetlar 24/7 rejimda qanday qilib ochiq portlarni qidiradi va parollarni taxmin qiladi.", "Shodan.io yoki jonli kiber-hujumlar xaritasini ekranda ko'rsating."],
    ["Arxitektura", "SSH kalitlarining asimmetrik tabiati: Ochiq kalit va maxfiy kalit. Nega maxfiy kalit hech qachon tarmoqqa chiqmasligi kerak?", "Qulf va kalit metaforasi orqali tushuntiring, lekin texnik terminlarni qoldiring."],
    ["Himoya Rejasi", "Hardening checklist: 4 ta asosiy qadam. Root hisobini nishondan chiqarish va parolli kirishni butunlay to'xtatish.", "Doskaga 4 ta qadamni yozib qo'ying."],
    ["Konfiguratsiya", "sshd_config fayli — server yuragi. Har bir parametr qanday ma'no beradi va xatolar serverdan uzib qo'yishi mumkin.", "Ekranda /etc/ssh/sshd_config faylini nano yoki vim da ochib ko'rsating."],
    ["Firewall", "UFW bilan ishlash. Eng katta tuzoq: SSH portini ochmasdan firewallni yoqib qo'yish! Shunda server bloklanib qoladi.", "Qat'iy ogohlantiring: Avval allow 2222, keyin enable!"],
    ["Avtomat Himoya", "Fail2ban dinamik mudofaasi. Qoidabuzarlarni qanday topadi va iptables orqali yo'lini to'sadi.", "fail2ban-client status sshd buyrug'i natijasini ko'rsating."],
    ["Real Keys", "50 000 dollarlik xato. Ochiq qolgan root paroli tufayli AWS hisobi qanday osmonga sakragani.", "Stajyorning real keysini hikoya qilib bering."],
    ["Amaliyot", "12 daqiqalik laboratoriya. Har bir o'quvchi o'z kompyuterida kalit hosil qilib, serverga bog'lanishi kerak.", "Taymerni yoqing (12 daqiqa), qatorlar orasida yurib xatoliklarga yordam bering."],
    ["Tekshirish", "Nazorat tekshiruvi: 5 ta nuqta. Permission denied xabari chiqqani — bu xato emas, bu g'alaba!", "O'quvchilardan natijalarni tekshirishni so'rang."],
    ["Mezon", "10 ballik baholash mezoni. 4 ta asosiy talab.", "Baholash shartlarini tushuntiring."],
    ["Xulosa", "Dars yakuni va uy vazifasi. Kelgusi darsda biz tarmoq paketlarini tahlil qilishni — Wiresharkni o'rganamiz.", "Varaqalarni yig'ing yoki imzolab bering."]
]

N_RU = [
    ["Введение", "Старт урока: Сегодня мы начинаем блок реальной кибербезопасности. Покажем, как серверы атакуются ботами в интернете.", "Откройте слайд, объясните студентам неизбежность атак на любой публичный IP."],
    ["Анализ Угроз", "Что такое Brute-force? Как ботнеты непрерывно ищут открытые порты 22 и перебирают пароли.", "Покажите карту кибератак или интерфейс Shodan."],
    ["Архитектура", "Асимметричная криптография SSH: публичный и приватный ключ. Почему приватный ключ никогда не передается.", "Объясните через концепцию криптографического замка и личной подписи."],
    ["План Харденинга", "4 шага харденинга: отключение root, блокировка паролей, смена порта, фаервол.", "Выпишите ключевые директивы на доску."],
    ["Конфигурация", "Разбор боевого файла sshd_config. Важность каждого параметра.", "Покажите редактирование конфигурации в реальном терминале."],
    ["Фаервол", "UFW — межсетевой экран. Главная ловушка: не закрыть себе доступ, включив фаервол до разрешения порта SSH.", "Предупредите класс: сначала allow 2222, только потом enable!"],
    ["Автозащита", "Fail2ban — активная защита. Как он ловит злоумышленников в логах и банит в iptables.", "Продемонстрируйте статус fail2ban-client status sshd."],
    ["Кейс из Жизни", "Кейс на $50 000: майнинг на взломанном сервере стажёра.", "Расскажите реальную историю ошибки облачной безопасности."],
    ["Практика", "12-минутный практикум. Генерация ключей Ed25519 и настройка защищенного соединения.", "Запустите таймер на 12 минут, помогайте студентам с ошибками прав доступа."],
    ["Чек-лист", "Проверка защиты: ошибка Permission denied на пароль означает успех!", "Проверьте чек-листы на экранах учащихся."],
    ["Критерии", "10-балльная шкала оценивания практической работы.", "Озвучьте правила начисления баллов."],
    ["Итоги", "Завершение урока и домашнее задание. На следующем уроке перейдем к анализу сетевого трафика в Wireshark.", "Соберите рабочие листы."]
]

N_EN = [
    ["Intro", "Lesson opening: Today we enter the production cybersecurity domain. We dissect how Linux servers are probed and exploited.", "Open title slide and contextualize the hostility of the public internet."],
    ["Threat Vector", "Brute-force mechanics: How botnets continuously scan port 22 and execute dictionary attacks.", "Display live cyber threat map telemetry or Shodan query."],
    ["Architecture", "Asymmetric SSH architecture: Public lock vs private key signature. Why private keys never leave local storage.", "Explain challenge-response cryptography handshake."],
    ["Hardening Plan", "The 4-step hardening plan: Disable root, disable passwords, change port, activate firewall.", "Write the 4 hardening rules on whiteboard."],
    ["Configuration", "Dissecting production sshd_config file parameters and timeout policies.", "Walk through config file in live terminal demo."],
    ["Firewall", "Configuring UFW packet filtering. The critical pitfall: Never enable UFW before punching the custom SSH port.", "Emphasize safety order: allow port first, then enable!"],
    ["Active Defense", "Fail2ban intrusion prevention: How automated log parsers dynamically feed bans into Linux kernel iptables.", "Demonstrate fail2ban-client status queries."],
    ["Case Study", "The $50,000 AWS incident: An intern's default root password leading to cryptojacking.", "Analyze breach timeline and business impact."],
    ["Hands-On Lab", "12-minute hardening drill: Generating Ed25519 keys and locking authentication down.", "Start 12-minute countdown timer and provide 1-on-1 terminal troubleshooting."],
    ["Verification", "Audit checklist: Confirming that password challenges are completely blocked by the daemon.", "Ensure students verify the publickey permission rejection."],
    ["Evaluation", "10-point evaluation rubric breakdown.", "Explain grading benchmarks."],
    ["Summary", "Wrap-up and homework preview. Next session: Deep packet inspection and Wireshark network security.", "Collect and sign lab worksheets."]
]

NOTES = {"uz": N_UZ, "ru": N_RU, "en": N_EN}

# ---------------------------------------------------------------- Varaqa Body
V = []
V.append(sheet_header(
    h1=("Kiberxavfsizlik: Linux Server va SSH Himoyasi",
        "Кибербезопасность: Защита Сервера Linux и SSH",
        "CyberSecurity: Linux Server & SSH Hardening"),
    sub=("Amaliy Laboratoriya Varaqasi · 9-sinf · 5-hafta · 21-dars",
         "Практический Рабочий Лист · 9 класс · Неделя 5 · Урок 21",
         "Hands-On Lab Worksheet · Grade 9 · Week 5 · Lesson 21")
))

V.append(mission(
    h=("Laboratoriya Vazifasi: Serverni Qulflash (Hardening)",
       "Миссия Лабораторной: Полный Харденинг Сервера",
       "Lab Mission: Full Server Hardening Execution"),
    p=("Ed25519 kriptografik SSH kalit juftligini yaratish, parolli kirishni butunlay to'xtatish, "
       "portni 2222 ga ko'chirish, UFW firewall va Fail2ban faollashtirish orqali serverni 100% himoyalash.",
       "Создать пару ключей Ed25519, полностью отключить аутентификацию по паролям, "
       "сменить порт на 2222, настроить межсетевой экран UFW и защиту Fail2ban.",
       "Generate an Ed25519 keypair, eliminate password authentication entirely, relocate SSH port to 2222, "
       "and configure UFW firewall and Fail2ban IPS."))
)

V.append(table(
    headers=[
        ("Xavfsizlik Bosqichi", "Этап Безопасности", "Security Phase"),
        ("Terminal Buyrug'i", "Команда Терминала", "Terminal Command"),
        ("Natija / Tekshiruv", "Результат / Проверка", "Expected Verification"),
        ("Holat", "Статус", "Status")
    ],
    rows=[
        [("1. SSH Kalit", "1. SSH-Ключ", "1. SSH Keypair"),
         ("ssh-keygen -t ed25519 -C 'user@target'", "ssh-keygen -t ed25519 -C 'user@target'", "ssh-keygen -t ed25519 -C 'user@target'"),
         ("id_ed25519 va id_ed25519.pub yaratildi", "Созданы id_ed25519 и id_ed25519.pub", "Keys generated in ~/.ssh/"),
         ("✅ Tayyor", "✅ Готово", "✅ Ready")],
        [("2. Kalit Yuklash", "2. Копирование", "2. Deploy Key"),
         ("ssh-copy-id -i ~/.ssh/id_ed25519.pub user@vps", "ssh-copy-id -i ~/.ssh/id_ed25519.pub user@vps", "ssh-copy-id -i ~/.ssh/id_ed25519.pub user@vps"),
         ("authorized_keys ga qo'shildi", "Добавлен в authorized_keys", "Added to authorized_keys"),
         None],
        [("3. Parolni O'chirish", "3. Запрет Паролей", "3. Disable Passwords"),
         ("PasswordAuthentication no", "PasswordAuthentication no", "PasswordAuthentication no"),
         ("Parolli kirish urinishi darhol rad etiladi", "Отказ при попытке ввода пароля", "Permission denied (publickey)"),
         None],
        [("4. UFW Faollashtirish", "4. Запуск UFW", "4. Enable UFW"),
         ("sudo ufw allow 2222/tcp && sudo ufw enable", "sudo ufw allow 2222/tcp && sudo ufw enable", "sudo ufw allow 2222/tcp && sudo ufw enable"),
         ("Status: active (2222, 80, 443 ochiq)", "Status: active (открыты 2222, 80, 443)", "Status: active (2222, 80, 443)"),
         None],
    ]
))

V.append(sheet_box(
    h=("Xavfsizlik Tahlili va Nazariy Savollar", "Анализ Безопасности и Вопросы", "Security Analysis & Written Queries"),
    body_html=writelines(3, label=("1. Nega RSA-1024 o'rniga zamonaviy Ed25519 algoritmi tavsiya etiladi?",
                                   "1. Почему современный Ed25519 предпочтительнее устаревшего RSA-1024?",
                                   "1. Why is Ed25519 mathematically superior to legacy RSA-1024?"))
             + "<br>"
             + writelines(3, label=("2. Fail2ban qanday qilib Brute-force hujumlarini aniqlaydi va bloklaydi?",
                                   "2. Как именно Fail2ban обнаруживает и изолирует Brute-force атаки?",
                                   "2. How does Fail2ban detect and dynamically quarantine brute-force intruders?"))
))

V.append(sheet_box(
    h=("Baholash Mezoni (10 Ball)", "Критерии Оценки (10 Баллов)", "Grading Rubric (10 Points)"),
    body_html=rubric([
        (("Ed25519 kalit yaratilib, serverga joylangan", "Ключ Ed25519 создан и установлен", "Ed25519 key generated & authorized"), "3 ball"),
        (("sshd_config da parol va root o'chirilgan (Port 2222)", "В sshd_config отключены пароли и root (порт 2222)", "Passwords & root disabled, port 2222"), "3 ball"),
        (("UFW firewall va Fail2ban to'g'ri sozlangan", "UFW фаервол и Fail2ban активны", "UFW & Fail2ban configured and active"), "2 ball"),
        (("Savollarga to'liq va asosli javob berilgan", "Даны развернутые ответы на вопросы листа", "Written analytical queries answered"), "2 ball"),
    ], "10 ball")
))

V.append("</div>\n" + sign_box("Musulmonov Mamarajab"))

VARAQA_BODY = "\n".join(V)

lesson = Lesson(
    outdir=D,
    titles=TITLES,
    sheet_titles=SHEET_TITLES,
    key="vc-notes-9-21",
    slides=S,
    notes=NOTES,
    varaqa_body=VARAQA_BODY
)

if __name__ == "__main__":
    out = lesson.build()
    print("Created:", out)
