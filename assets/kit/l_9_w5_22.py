# -*- coding: utf-8 -*-
"""9-sinf · 5-hafta · 22-dars — Tarmoq Xavfsizligi va Paket Tahlili: Wireshark, Nmap va Shifrlanmagan Trafik Xatarlari."""

import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from build import (Lesson, slide, title_slide, box, code, el, i18n,
                   sheet_header, mission, table, sheet_box, rubric, writelines, sign_box)

D = "classes/9-sinf/5-hafta/22-dars-tarmoq-xavfsizligi-va-paket-tahlili"

TITLES = {
    "uz": "22-dars: Tarmoq Xavfsizligi va Paket Tahlili — Wireshark & Nmap",
    "ru": "Урок 22: Сетевая Безопасность и Анализ Пакетов — Wireshark & Nmap",
    "en": "Lesson 22: Network Security & Packet Analysis — Wireshark & Nmap",
}
SHEET_TITLES = {k: v + (" — Ish Varaqasi" if k == "uz" else
                        " — Рабочий Лист" if k == "ru" else " — Worksheet")
                for k, v in TITLES.items()}

S = []

# 1. Title Slide
S.append(title_slide(
    ph=("Kirish", "Введение", "Intro"), time="0–3",
    eyebrow=("CyberSecurity · 22-dars · 9-sinf (Network Defense Track)",
             "CyberSecurity · Урок 22 · 9 класс (Network Defense Track)",
             "CyberSecurity · Lesson 22 · Grade 9 (Network Defense Track)"),
    h1=("Tarmoq Xavfsizligi va Paket Tahlili",
        "Сетевая Безопасность и Анализ Пакетов",
        "Network Security & Packet Inspection"),
    lede=("Har safar saytga kirganingizda yoki ilovani ochganingizda, ma'lumotlar kabel va havo to'lqinlari orqali "
          "<b>minglab mayda paketlarga</b> bo'linib oqadi. Agar trafik shifrlanmagan bo'lsa (HTTP), bitta Wi-Fi tarmog'idagi "
          "istalgan kishi sizning parollaringiz, xabarlaringiz va cookie-fayllaringizni ochiq ko'ra oladi. "
          "Bugungi darsda siz tarmoq paketlarining ichki anatomiyasini, <b>Wireshark</b> orqali jonli trafikni tahlil qilishni, "
          "<b>Nmap</b> bilan ochiq portlarni skanerlashni va <b>TLS/HTTPS</b> shifrlash qalqonini o'rganasiz.",
          "Каждый раз при открытии сайта данные дробятся на <b>тысячи мелких сетевых пакетов</b>. "
          "Если трафик не зашифрован (HTTP), любой находящийся в том же Wi-Fi злоумышленник может прочесть ваши пароли и переписку. "
          "Сегодня вы изучите анатомию пакетов TCP/IP, глубокий анализ в <b>Wireshark</b>, "
          "сканирование сетевых портов с помощью <b>Nmap</b> и защиту протокола <b>TLS/HTTPS</b>.",
          "Every network transaction fractures into <b>thousands of discrete network packets</b> traversing routers. "
          "If unencrypted (HTTP), anyone eavesdropping on the local network can reconstruct plaintext credentials and cookies. "
          "Today you will master packet anatomy, live capture with <b>Wireshark</b>, "
          "reconnaissance port auditing with <b>Nmap</b>, and enterprise <b>TLS/HTTPS</b> encryption enforcement."),
    meta=[("<b>Fan:</b> Kiberxavfsizlik · Network Protocol Security",
           "<b>Предмет:</b> Кибербезопасность · Безопасность Протоколов",
           "<b>Subject:</b> CyberSecurity · Network Protocol Security"),
          ("<b>Kohorta:</b> 9-sinf Kiber-Muhandis",
           "<b>Когоorta:</b> 9 класс Кибер-Инженер",
           "<b>Cohort:</b> Grade 9 Cyber-Engineer"),
          ("<b>Hafta:</b> 5 (2-soat)", "<b>Неделя:</b> 5 (2-й час)", "<b>Week:</b> 5 (Hour 2)")],
))

# 2. Problem: The Open Airwaves
S.append(slide(
    ph=("Xavf Tahlili", "Анализ Угроз", "Threat Vector"), time="3–6",
    eyebrow=("Ochiq Wi-Fi xavfi", "Опасность открытого Wi-Fi", "Public Wi-Fi Vulnerability"),
    title=("Kafedagi Ochiq Wi-Fi: Shifrlanmagan Trafik Nega O'g'irlanadi?",
           "Открытый Wi-Fi в Кафе: Почему Незашифрованный Трафик Перехватывают?",
           "The Coffee Shop Trap: Why Plaintext Traffic Gets Sniffed in Seconds"),
    body='<div class="cols c2">\n'
         + box("accent", ("Man-in-the-Middle (MitM) Hujumi", "Атака Человек Посередине (MitM)", "Man-in-the-Middle (MitM) Attack"),
               items=[
                   ("<b>Paketlarni tutib olish (Sniffing):</b> Tarmoq kartasi 'promiscuous mode' rejimida havodagi barcha paketlarni yozib oladi.",
                    "<b>Сниффинг пакетов:</b> Сетевая карта в режиме промискуитета слушает чужой эфир.",
                    "<b>Packet Sniffing:</b> Wireless cards in promiscuous mode capture every packet traveling across the airwaves."),
                   ("<b>ARP Spoofing:</b> Xaker o'zini yo'riqnoma (router) sifatida ko'rsatib, barcha trafikni o'zi orqali o'tkazadi.",
                    "<b>ARP-спуфинг:</b> Злоумышленник притворяется шлюзом и пропускает трафик жертвы через себя.",
                    "<b>ARP Cache Poisoning:</b> Adversary impersonates the default gateway, funneling all victim traffic through their rig."),
                   ("<b>Ochiq matn (Plaintext):</b> HTTP orqali yuborilgan har bir POST so'rovi (login, parol) ochiqcha ko'rinadi.",
                    "<b>Открытый текст:</b> Любой POST-запрос по HTTP (логин, пароль) виден как на ладони.",
                    "<b>Plaintext Exposure:</b> HTTP POST payloads transmit passwords in raw ASCII text."),
               ])
         + box("purple", ("Real Tajriba: Wi-Fi Sniffing", "Эксперимент: Перехват Wi-Fi", "Demonstration: Packet Sniffing"),
               p=("Agar siz himoyalanmagan saytda parol tersangiz, Wireshark ishlatayotgan xaker ekranda soniyaning yuzdan bir ulushida quyidagilarni ko'radi:<br><br>"
                  "<code>POST /login HTTP/1.1<br>Host: bank-test.uz<br>username=azamat&password=MeningMaxfiyParolim2026!</code><br><br>"
                  "Hech qanday murakkab xakerlik kerak emas — parol shundoq ko'rinib turibdi!",
                  "При отправке пароля на HTTP-сайт перехватчик в Wireshark мгновенно видит открытый пейлоад:<br><br>"
                  "<code>POST /login HTTP/1.1<br>Host: bank-test.uz<br>username=azamat&password=МойСекретныйПароль2026!</code><br><br>"
                  "Никакого взлома не нужно — пароль открыт для всех в этой сети!",
                  "Submitting credentials over HTTP lets an eavesdropper read your payload in plaintext within milliseconds:<br><br>"
                  "<code>POST /login HTTP/1.1<br>Host: bank-test.uz<br>username=azamat&password=MySecretPassword2026!</code><br><br>"
                  "Zero decryption required — raw credentials broadcast openly across the airwaves."))
         + '\n</div>'
))

# 3. TCP/IP Architecture & Three-Way Handshake
S.append(slide(
    ph=("Arxitektura", "Архитектура", "Architecture"), time="6–10",
    eyebrow=("Protokol mexanikasi", "Механика протоколов", "Protocol Mechanics"),
    title=("TCP Three-Way Handshake: Ulanish Qanday O'rnatiladi?",
           "Трёхстороннее Рукопожатие TCP (Three-Way Handshake)",
           "The TCP Three-Way Handshake: Establishing State Synchrony"),
    body='<div class="cols c3">\n'
         + box("", ("1. SYN (Synchronize)", "1. Пакет SYN", "1. SYN Flag"),
               p=("Mijoz serverga: <i>\"Salom! Men ulanmoqchiman. Mening boshlang'ich ketma-ketlik raqamim (ISN): 1000\"</i>.",
                  "Клиент серверу: <i>«Привет! Хочу подключиться. Мой начальный номер (ISN): 1000»</i>.",
                  "Client to Server: <i>\"Hello! I want to establish a session. My initial sequence number (ISN) is 1000.\"</i>"),
               extra_html='<span class="tag purple" %s>SYN = 1 · Ulanish so\'rovi</span>' % i18n("SYN = 1 · Ulanish so'rovi", "SYN = 1 · Запрос соединения", "SYN = 1 · Connect Request"))
         + box("", ("2. SYN-ACK", "2. Пакет SYN-ACK", "2. SYN-ACK Response"),
               p=("Server mijozga: <i>\"Salom! Qabul qildim (ACK 1001). Mening ham ketma-ketlik raqamim bor (ISN 5000)\"</i>.",
                  "Сервер клиенту: <i>«Привет! Получил (ACK 1001). Мой номер последовательности: 5000»</i>.",
                  "Server to Client: <i>\"Acknowledged (ACK 1001). Here is my sequence number (ISN 5000).\"</i>"),
               extra_html='<span class="tag green" %s>SYN = 1, ACK = 1 · Tasdiq</span>' % i18n("SYN = 1, ACK = 1 · Tasdiq", "SYN = 1, ACK = 1 · Подтверждение", "SYN=1, ACK=1 · Acknowledged"))
         + box("accent", ("3. ACK (Acknowledge)", "3. Пакет ACK", "3. Final ACK"),
               p=("Mijoz serverga: <i>\"Ajoyib! Qabul qildim (ACK 5001). Ulanish o'rnatildi! Endi ma'lumot yuboramiz\"</i>.",
                  "Клиент серверу: <i>«Отлично! Принял (ACK 5001). Канал установлен, передаём данные!»</i>.",
                  "Client to Server: <i>\"Got it (ACK 5001). Session established! Data stream commences.\"</i>"),
               extra_html='<span class="tag red" %s>Kanal ochiq · ESTABLISHED</span>' % i18n("Kanal ochiq · ESTABLISHED", "Канал открыт · ESTABLISHED", "Stream Open · ESTABLISHED"))
         + '\n</div>'
))

# 4. Deep Dive: Wireshark Anatomy
S.append(slide(
    ph=("Wireshark", "Wireshark", "Wireshark"), time="10–14",
    eyebrow=("Paket mikroskopi", "Микроскоп сетевых пакетов", "Packet Microscope"),
    title=("Wireshark Anatomiyasi: Paket Ichida Nimalar Yotadi?",
           "Анатомия Wireshark: Что Лежит Внутри Пакета?",
           "Wireshark Dissection: Packet Layer Encapsulation"),
    body='<div class="cols c2">\n'
         + box("green", ("Paketning 4 Ta Qatlami (Encapsulation)", "4 Уровня Пакета (Encapsulation)", "4 Encapsulation Layers"),
               items=[
                   ("<b>Ethernet II (Frame):</b> Manba va qabul qiluvchi MAC manzillari (masalan, <code>00:1A:2B:3C:4D:5E</code>).",
                    "<b>Ethernet II:</b> Физические MAC-адреса источника и назначения.",
                    "<b>Ethernet II Frame:</b> Source & Destination hardware MAC addresses."),
                   ("<b>Internet Protocol (IPv4/IPv6):</b> Qayerdan qayerga (IP manzil, masalan, <code>192.168.1.50 -> 93.184.216.34</code>).",
                    "<b>IPv4 / IPv6:</b> Сетевые IP-адреса отправителя и получателя.",
                    "<b>IP Layer:</b> Network Layer source and destination IP endpoints."),
                   ("<b>Transmission Control Protocol (TCP):</b> Portlar (Port 54321 -> Port 443), Flaglar (SYN, ACK, FIN, RST).",
                    "<b>TCP:</b> Порты сервисов (например 443) и управляющие флаги.",
                    "<b>Transport Layer (TCP/UDP):</b> Source/Dest ports, Sequence numbers, TCP flags."),
                   ("<b>Application Data (Payload):</b> Haqiqiy yuklama (HTTP so'rov, JSON, TLS shifrlangan ma'lumot).",
                    "<b>Payload:</b> Прикладные данные приложения (HTTP, TLS-шифрованный поток).",
                    "<b>Application Layer:</b> Raw payload (HTTP verbs, JSON structures, TLS ciphertext)."),
               ])
         + '<div class="box accent">\n'
         + el("h3", "Wireshark Display Filtrlarining Oltin To'plami", "Золотые Фильтры Wireshark", "Wireshark Display Filters")
         + code("""# 1. Faqat HTTP POST so'rovlarini ko'rish (Login/parol tutilishi)
http.request.method == "POST"

# 2. DNS so'rovlarini filtrlash (Foydalanuvchi qaysi saytlarga kirgan)
dns && dns.flags.response == 0

# 3. Muayyan IP va Port bo'yicha trafik
ip.addr == 192.168.1.100 && tcp.port == 443

# 4. Buzilgan TCP ulanishlar (RST flag)
tcp.flags.reset == 1""")
         + '</div>\n</div>'
))

# 5. Nmap Network Reconnaissance
S.append(slide(
    ph=("Nmap", "Nmap", "Nmap"), time="14–18",
    eyebrow=("Razvedka va Audit", "Сетевая разведка и аудит", "Reconnaissance & Audit"),
    title=("Nmap: Ochiq Portlarni Qidirish va Xizmatlar Auditi",
           "Nmap: Сканирование Портов и Аудит Сервисов",
           "Nmap: Port Enumeration & Attack Surface Mapping"),
    body='<div class="cols c2">\n'
         + box("", ("Portlarning 3 Xil Holati", "3 Состояния Сетевого Порта", "The 3 Port States"),
               items=[
                   ("<b>Open (Ochiq):</b> Serverda dastur (masalan Nginx) portni eshitmoqda. Ulanish mumkin.",
                    "<b>Open:</b> Сервис активно слушает порт (например, Nginx). Соединение разрешено.",
                    "<b>Open:</b> A service (e.g. Nginx) actively listens on the socket."),
                   ("<b>Closed (Yopiq):</b> Server javob qaytaradi (RST paketi), lekin hech qanday xizmat ishlamayapti.",
                    "<b>Closed:</b> Хост отвечает пакетом RST, порт доступен, но служба не запущена.",
                    "<b>Closed:</b> Host replies with TCP RST; port reachable but no application attached."),
                   ("<b>Filtered (Filtrlangan):</b> Firewall (UFW) paketni yo'lda tashlab yuboradi (DROP). Server javob bermaydi.",
                    "<b>Filtered:</b> Фаервол молча сбрасывает пакеты (DROP). Сервер невидим.",
                    "<b>Filtered:</b> A firewall silently drops probes. Server presence is masked."),
               ])
         + '<div class="box purple">\n'
         + el("h3", "Eng Mashhur Nmap Buyruqlari", "Популярные Команды Nmap", "Essential Nmap Audit Commands")
         + code("""# 1. Tezkor SYN skanerlash (Yarim ochiq skan, yashirin)
sudo nmap -sS -p 1-1000 192.168.1.100

# 2. Ishlayotgan xizmatlar va versiyalarini aniqlash (-sV)
nmap -sV -p 80,443,2222 192.168.1.100

# 3. Operatsion tizimni aniqlash (-O)
sudo nmap -O 192.168.1.100

# 4. Zaifliklarni avtomatik qidiruvchi scriptlar (--script vuln)
nmap --script vuln -p 80,443 target.uz""")
         + '</div>\n</div>'
))

# 6. Defense: TLS/HTTPS Shield
S.append(slide(
    ph=("Himoya", "Защита", "Defense"), time="18–22",
    eyebrow=("Kriptografik himoya", "Криптографическая защита", "Cryptographic Defense"),
    title=("TLS/HTTPS Qalqoni: Sniffingni Qanday Yo'q Qilamiz?",
           "Щит TLS/HTTPS: Как Сделать Сниффинг Бесполезным?",
           "The TLS/HTTPS Shield: Neutralizing Packet Sniffers"),
    body='<div class="cols c2">\n'
         + box("green", ("HTTP vs HTTPS Farqi Wiresharkda", "Разница HTTP и HTTPS в Wireshark", "HTTP vs HTTPS in Wireshark"),
               items=[
                   ("<b>HTTP:</b> Barcha ma'lumotlar ochiq matnda. Paketni tutib olgan har kim to'liq kontentni ko'radi.",
                    "<b>HTTP:</b> Все заголовки, куки и пароли видны снифферу открытым текстом.",
                    "<b>HTTP:</b> Headers, cookies, passwords broadcast in cleartext across every hop."),
                   ("<b>HTTPS (TLS 1.3):</b> Butun dastur qatlami AES-GCM yoki ChaCha20 bilan shifrlanadi.",
                    "<b>HTTPS (TLS 1.3):</b> Весь прикладной слой зашифрован шифром AES-GCM.",
                    "<b>HTTPS (TLS 1.3):</b> Entire application payload is encrypted via AES-GCM."),
                   ("<b>Wireshark ko'rinishi:</b> Xaker faqat tushunarsiz tasodifiy baytlar (Application Data: 3a f1 c8...) ko'radi.",
                    "<b>В сниффере:</b> Злоумышленник видит лишь случайный шум (Application Data).",
                    "<b>Sniffer view:</b> Adversary observes only pseudorandom bytes (TLS Application Data)."),
               ])
         + '<div class="box accent">\n'
         + el("h3", "Serverda HTTPS & HSTS Majburiy Qilish", "Принудительный HTTPS и HSTS", "Enforcing HTTPS & HSTS on Nginx")
         + code("""# Nginx Konfiguratsiyasi: HTTP ni darhol HTTPS ga yo'naltirish
server {
    listen 80;
    server_name target.uz;
    return 301 https://$host$request_uri;
}

# HSTS Qat'iy Sarlavhasi (Downgrade hujumlarni to'xtatadi)
add_header Strict-Transport-Security 
  "max-age=63072000; includeSubDomains; preload" always;""")
         + '</div>\n</div>'
))

# 7. Wireshark in Action: Inspecting Real Attack
S.append(slide(
    ph=("Inspeksiya", "Инспекция", "Deep Inspection"), time="22–26",
    eyebrow=("Jonli tahlil", "Живой анализ", "Live Forensics"),
    title=("Tarmoq Forensikasi: SYN Flood DoS Hujumini Aniqlash",
           "Сетевая Криминалистика: Распознавание SYN-Flood DoS",
           "Network Forensics: Diagnosing a SYN Flood DoS Attack"),
    body='<div class="cols c2">\n'
         + box("accent", ("SYN Flood DoS Mexanikasi", "Механика SYN-Flood DoS", "SYN Flood Mechanism"),
               items=[
                   ("Hujumchi soxta (spoofed) IP manzillardan millionlab <b>SYN paketlari</b> yuboradi.",
                    "Атакующий шлёт миллионы запросов SYN с поддельных IP-адресов.",
                    "Adversary floods server with millions of spoofed SYN packets."),
                   ("Server SYN-ACK javobini qaytaradi va mijoztan ACK kutib <b>yarim ochiq holatda</b> xotirada joy saqlaydi.",
                    "Сервер отвечает SYN-ACK и зависает в ожидании ACK, забивая очередь соединений.",
                    "Server replies with SYN-ACK and allocates memory in TCP connection backlog table."),
                   ("ACK hech qachon kelmaydi! Server xotirasi (backlog queue) to'lib, qonuniy foydalanuvchilarni rad etadi.",
                    "Ответный ACK никогда не приходит! Очередь TCP переполняется, сервер падает.",
                    "ACK never arrives. Server kernel backlog exhausts, refusing legitimate clients."),
               ])
         + '<div class="box green">\n'
         + el("h3", "Tahlil va Himoya (SYN Cookies)", "Анализ и Защита (SYN Cookies)", "Diagnostics & Kernel Mitigation")
         + code("""# 1. Serverda SYN_RECV holatidagi ulanishlarni hisoblash:
netstat -n -p tcp | grep SYN_RECV | wc -l

# 2. Linux yadrosida SYN Cookies ni yoqish (Xotirani to'ldirmaydi):
sudo sysctl -w net.ipv4.tcp_syncookies=1

# 3. SYN Flood ga qarshi UFW Rate Limit:
sudo ufw limit 2222/tcp
sudo ufw limit 443/tcp""")
         + '</div>\n</div>'
))

# 8. Real-World Case Study
S.append(slide(
    ph=("Real Keys", "Кейс из Жизни", "Case Study"), time="26–30",
    eyebrow=("Tarixiy kiber-hujum", "Исторический инцидент", "Historic Incident"),
    title=("Mehmonxona Wi-Fi Hujumi: Darkhotel Kiber-Guruhining Sirlari",
           "Взлом Wi-Fi в Отелях: Атака Группировки Darkhotel",
           "The Darkhotel Hotel Wi-Fi APT Eavesdropping Campaign"),
    body='<div class="cols c2">\n'
         + box("accent", ("Darkhotel Qanday Hujum Qilgan?", "Как Действовали Darkhotel?", "Darkhotel Attack Vector"),
               p=("Xalqaro kiber-guruh elita mehmonxonalarining Wi-Fi tarmoqlariga kirib olgan. Mehmonxonada yashovchi yirik kompaniya rahbarlari Wi-Fi ga ulanganda, ularning trafigi ushlab olingan va soxta <b>Adobe Flash / Windows Update</b> yangilanishi orqali noutbuklariga troyan kiritilgan.",
                  "Хакерская группа Darkhotel компрометировала Wi-Fi сети люксовых отелей. При подключении топ-менеджеров их трафик подменялся, навязывая поддельные обновления Adobe Flash с бэкдором.",
                  "The Darkhotel APT infiltrated luxury hotel Wi-Fi portals. When C-level executives connected, their traffic was intercepted and poisoned with weaponized fake software updates containing spyware."))
         + box("purple", ("Asosiy Saboqlar", "Главные Уроки", "Critical Lessons"),
               items=[
                   ("<b>Ochiq Wi-Fi ga hech qachon ishonmang:</b> Jamoat joylaridagi har qanday tarmoq potensial buzilgan deb qaralishi shart.",
                    "<b>Никогда не доверяйте публичному Wi-Fi:</b> Любая открытая сеть изначально враждебна.",
                    "<b>Never trust public Wi-Fi:</b> Any public hotspot must be treated as hostile ground."),
                   ("<b>Doimiy VPN / WireGuard:</b> Jamoat tarmog'ida barcha trafikni shifrlangan VPN tunnel orqali o'tkazish shart.",
                    "<b>Всегда используйте VPN:</b> Весь трафик в поездках должен идти через защищенный туннель.",
                    "<b>Always enforce VPN tunnels:</b> Encapsulate all raw traffic inside encrypted tunnels."),
                   ("<b>DNS over HTTPS (DoH):</b> DNS so'rovlarini ham provayder yoki kafe egasi o'qiy olmasligi uchun shifrlash.",
                    "<b>Шифруйте DNS (DoH):</b> Не позволяйте владельцам сети видеть историю ваших переходов.",
                    "<b>Enforce Encrypted DNS (DoH):</b> Prevent network operators from spying on host lookups."),
               ])
         + '\n</div>'
))

# 9. Practical Mission (12 min timer)
S.append(slide(
    ph=("Amaliyot", "Практика", "Hands-On Lab"), time="30–42",
    eyebrow=("Mustaqil laboratoriya · 12 daqiqa", "Лабораторная работа · 12 минут", "Practical Lab · 12 Minutes"),
    title=("Amaliy Topshiriq: Tarmoq Paketlarini Tahlil Qilish va Nmap Skandi",
           "Практическое Задание: Анализ Пакетов и Сканирование Nmap",
           "Mission: Live Packet Capture & Network Attack Surface Audit"),
    body='<div class="cols c2">\n'
         + box("green", ("Laboratoriya Bosqichlari", "Шаги Лабораторной", "Mission Checkpoints"),
               items=[
                   ("<b>1. Wireshark da paket ushlash:</b> Mahalliy tarmoq interfeysida paket tutishni boshlang.",
                    "<b>1. Захват в Wireshark:</b> Запустите захват пакетов на локальном интерфейсе.",
                    "<b>1. Start capture:</b> Launch Wireshark capture on active network adapter."),
                   ("<b>2. HTTP vs HTTPS farqini ko'rish:</b> Shifrlanmagan test sahifaga POST so'rov yuborib, parolni ochiq ko'ring.",
                    "<b>2. Сравнение HTTP и HTTPS:</b> Отправьте тестовый POST по HTTP и найдите открытый пароль.",
                    "<b>2. Plaintext inspection:</b> Submit a test HTTP form and locate plaintext password."),
                   ("<b>3. Nmap skaneri:</b> O'z lokal serveringizni yoki test IP-ni `nmap -sV -p 1-1000` bilan skanerlang.",
                    "<b>3. Сканирование Nmap:</b> Просканируйте локальный хост командой `nmap -sV -p 1-1000`.",
                    "<b>3. Nmap service audit:</b> Execute `nmap -sV -p 1-1000` against test target."),
                   ("<b>4. Ochiq portlar ro'yxati:</b> Topilgan barcha ochiq portlar va xizmatlarni jadvalga qayd eting.",
                    "<b>4. Таблица портов:</b> Занесите все найденные открытые порты в рабочий лист.",
                    "<b>4. Port matrix:</b> Document all exposed services and port states in worksheet."),
               ])
         + box("accent", ("O'lchanadigan Natija", "Критерий Сдачи", "Deliverable Spec"),
               p=("Wiresharkda ushlangan HTTP POST paketi ichidagi parolni topib, ekranda ko'rsatish va Nmap skanerlash hisobotidagi 3 ta ochiq xizmatni to'liq tahlil qilish!",
                  "Найти перехваченный пароль в пакете HTTP POST в Wireshark и предоставить отчёт Nmap по 3 открытым службам!",
                  "Demonstrate the extracted plaintext credential from Wireshark HTTP stream and provide Nmap telemetry for 3 open ports!"))
         + '\n</div>'
))

# 10. Verification Checklist
S.append(slide(
    ph=("Tekshirish", "Чек-лист", "Verification"), time="42–43",
    eyebrow=("Inspeksiya", "Проверка", "Audit"),
    title=("Laboratoriya Nazorat Cheklisti: 5 Ta Tekshiruv",
           "Чек-лист Проверки: 5 Пунктов Аудита",
           "Lab Verification Checklist: 5 Quality Gates"),
    body='<div class="cols c3">\n'
         + box("", ("1. Wireshark Filtr", "1. Фильтр Wireshark", "1. Filter Usage"),
               p=("`http.request.method == \"POST\"` filtri to'g'ri ishlatildimi?",
                  "Корректно ли применён фильтр `http.request.method == \"POST\"`?",
                  "Did you accurately apply `http.request.method == \"POST\"`?"))
         + box("", ("2. Nmap -sV Natijasi", "2. Результат Nmap", "2. Nmap Output"),
               p=("Port raqami, xizmat nomi va versiyasi aniqlandimi?",
                  "Определены ли номера портов, службы и точные версии программ?",
                  "Were port numbers, service names, and versions identified?"))
         + box("", ("3. TCP Handshake", "3. Рукопожатие TCP", "3. TCP Handshake"),
               p=("SYN, SYN-ACK va ACK paketlari ketma-ketligi topildimi?",
                  "Найдена ли цепочка пакетов SYN -> SYN-ACK -> ACK?",
                  "Did you trace the consecutive SYN -> SYN-ACK -> ACK stream?"))
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
                   ("Wiresharkda paketlar tahlil qilingan va parol topilgan.", "В Wireshark найден перехваченный пароль.", "Wireshark payload captured and decrypted."),
                   ("Nmap orqali ochiq portlar va versiyalar aniqlangan.", "Nmap определил все порты и версии служб.", "Nmap mapped all open ports and versions."),
                   ("TCP Handshake qadamlari to'g'ri tushuntirilgan.", "Шаги TCP Handshake объяснены верно.", "TCP Handshake steps correctly analyzed."),
                   ("Varaqa 100% to'ldirilgan.", "Рабочий лист заполнен на 100%.", "Worksheet completed 100%."),
               ])
         + box("", ("Yaxshi (7–8 Ball)", "Хорошо (7–8)", "Proficient (7–8)"),
               items=[
                   ("Wiresharkda paketlar ko'rilgan, lekin filtrda xatolik bor.", "Пакеты захвачены, но ошибка в фильтрах.", "Packets captured but display filters flawed."),
                   ("Nmap skaneri faqat oddiy rejimda ishlatilgan.", "Nmap запущен только в базовом режиме.", "Nmap executed only with default scan flags."),
                   ("Varaqa 80% to'ldirilgan.", "Рабочий лист заполнен на 80%.", "Worksheet completed 80%."),
               ])
         + box("accent", ("Qoniqarli (5–6 Ball)", "Удовл. (5–6)", "Developing (5–6)"),
               items=[
                   ("Wireshark ishga tushirilgan, lekin tahlil qilinmagan.", "Wireshark запущен, но анализа нет.", "Wireshark started without analysis."),
                   ("Nmap natijasi tushunarsiz qolgan.", "Результат Nmap не интерпретирован.", "Nmap output misunderstood."),
                   ("Varaqa qisman to'ldirilgan.", "Лист заполнен не полностью.", "Worksheet incomplete."),
               ])
         + '\n</div>'
))

# 12. Summary & Homework
S.append(slide(
    ph=("Xulosa", "Итоги", "Summary"), time="44–45",
    eyebrow=("Uyga vazifa", "Домашнее задание", "Homework & Next Steps"),
    title=("Xulosa va Uy Vazifasi: Tarmoqni Qulflash",
           "Итоги и Домашнее Задание: Защита Трафика",
           "Summary & Homework: Securing Network Perimeters"),
    body='<div class="cols c2">\n'
         + box("purple", ("Dars Xulosasi", "Итоги Урока", "Core Summary"),
               p=("Tarmoqdagi har bir bayt o'z manziliga ochiq ketmasligi shart. Wireshark tarmoqning nima gaplashayotganini ko'rsatuvchi ko'z bo'lsa, TLS/HTTPS begona ko'zlardan himoyalovchi eng kuchli qalqondir.",
                  "Ни один байт не должен уходить в сеть в открытом виде. Wireshark — это глаза инженера, а TLS/HTTPS — надежнейший щит от чужих ушей.",
                  "Never allow raw bytes to travel in the clear. Wireshark represents the engineer's diagnostic eyes, while TLS/HTTPS represents the impenetrable cryptographic shield."))
         + box("accent", ("Uy Vazifasi (10 Ball)", "Домашнее Задание (10 Баллов)", "Homework Assignment (10 Pts)"),
               items=[
                   ("<b>Tahlil:</b> O'z uyingizdagi Wi-Fi routerga ulangan qurilmalarni `nmap -sn 192.168.1.0/24` bilan skanerlang.",
                    "<b>Анализ:</b> Просканируйте устройства в домашней сети командой `nmap -sn 192.168.1.0/24`.",
                    "<b>Audit:</b> Scan active hosts on your home Wi-Fi using `nmap -sn 192.168.1.0/24`."),
                   ("<b>Wireshark:</b> HTTPS va HTTP saytlarga kirganda paketlar mazmunidagi farqni solishtirib yozing.",
                    "<b>Wireshark:</b> Сравните и опишите разницу структуры пакетов при входе на HTTP и HTTPS сайты.",
                    "<b>Wireshark:</b> Compare and contrast packet payloads between HTTP and HTTPS connections."),
                   ("<b>Varaqa:</b> Ish varaqasidagi barcha savollarni to'liq yakunlang.",
                    "<b>Лист:</b> Заполните и сдайте печатный рабочий лист.",
                    "<b>Worksheet:</b> Complete and submit your printable lab worksheet."),
               ])
         + '\n</div>'
))

# Teacher Notes
N_UZ = [
    ["Kirish", "Darsni boshlash: Tarmoq qanday ishlashini va har bir paket qanday sayohat qilishini tushuntiramiz.", "Slaydni oching, internet simlar va to'lqinlar orqali ochiq axborot almashishini ko'rsating."],
    ["Xavf Tahlili", "Ochiq Wi-Fi da sniffing qanday ishlashi. Nega kafeda bank ilovasiga kirish xavfli bo'lishi mumkin?", "MitM hujumi sxemasini doskaga chizing."],
    ["Arxitektura", "TCP Three-Way Handshake: SYN -> SYN-ACK -> ACK formulasi. Har bir qadamning maqsadi.", "O'quvchilar bilan birgalikda 'salom-javob-tasdiq' dialogini ko'rsatib bering."],
    ["Wireshark", "Wireshark anatomiyasi: Ethernet, IP, TCP va Payload qatlamlari. Display filtrlar bilan ishlash.", "Ekranda Wireshark dasturini ochib, jonli efirda paketlar oqimini ko'rsating."],
    ["Nmap", "Nmap bilan ochiq portlarni qidirish. Open, Closed, Filtered farqi.", "Terminalda nmap buyrug'ini ishga tushirib ko'rsating."],
    ["Himoya", "TLS 1.3 qalqoni. Wiresharkda shifrlangan paket qanday ko'rinishi (Application Data).", "HTTP va HTTPS paketlarini yonma-yon solishtiring."],
    ["Inspeksiya", "SYN Flood DoS hujumi tahlili. Yarim ochiq ulanishlar qanday qilib server xotirasini yeb qo'yishi.", "netstat buyrug'i bilan ko'rsating."],
    ["Real Keys", "Darkhotel kiber-guruhi tarixi. Elita mehmonxonalari Wi-Fi tarmog'ini buzib kirish.", "Real kiber-razvedka keysini qiziqarli qilib so'zlab bering."],
    ["Amaliyot", "12 daqiqalik laboratoriya. O'quvchilar Wiresharkda paket tahlil qiladi va Nmap skanini o'tkazadi.", "Taymerni yoqing (12 daqiqa), o'quvchilarga yordam bering."],
    ["Tekshirish", "Nazorat tekshiruvi. Topilgan ochiq portlar va parollarni tekshirish.", "O'quvchilar javoblarini tekshiring."],
    ["Mezon", "10 ballik baholash mezoni tushuntiriladi.", "Talablarni eslatib o'ting."],
    ["Xulosa", "Dars yakuni va uy vazifasi. Keyingi darsda Veb zaifliklari — OWASP Top 10 ni o'rganamiz.", "Varaqalarni yig'ing."]
]

N_RU = [
    ["Введение", "Старт урока: Как данные путешествуют по кабелям и радиоволнам в виде сетевых пакетов.", "Откройте слайд, введите тему сетевой безопасности."],
    ["Анализ Угроз", "Опасность сниффинга в публичных Wi-Fi сетях. Механика перехвата трафика MitM.", "Поясните уязвимость передачи данных без шифрования."],
    ["Архитектура", "Трёхстороннее рукопожатие TCP: SYN, SYN-ACK, ACK. Как согласуются параметры сессии.", "Разыграйте с учениками сценку рукопожатия TCP."],
    ["Wireshark", "Анатомия Wireshark: фрейм, IP, TCP, данные приложения. Применение дисплейных фильтров.", "Продемонстрируйте реальный захват трафика в Wireshark."],
    ["Nmap", "Nmap — исследование сети и портов. Состояния Open, Closed, Filtered.", "Покажите сканирование локального хоста в терминале."],
    ["Защита", "Щит TLS 1.3. Как шифрование превращает открытый текст в нечитаемый шум.", "Сравните незашифрованный HTTP и зашифрованный HTTPS."],
    ["Инспекция", "Анализ сетевой атаки SYN Flood DoS. Переполнение очереди полуоткрытых соединений.", "Покажите системную команду netstat."],
    ["Кейс из Жизни", "Кейс группировки Darkhotel: взлом Wi-Fi в люксовых отелях и целевой шпионаж.", "Расскажите хронологию реальной целевой атаки APT."],
    ["Практика", "12 минут практики: перехват пакетов в Wireshark и аудит сети через Nmap.", "Запустите таймер, контролируйте корректность фильтров."],
    ["Проверка", "Чек-лист проверки: подтверждение обнаружения открытого текста и портов.", "Проверьте вывод терминалов учащихся."],
    ["Критерии", "10-балльная шкала оценивания практической работы.", "Озвучьте критерии оценки."],
    ["Итоги", "Завершение урока и домашнее задание. На следующем занятии разберём веб-уязвимости OWASP Top 10.", "Соберите рабочие листы."]
]

N_EN = [
    ["Intro", "Lesson opening: Demystifying packet transmission across optical fibers and radio frequencies.", "Introduce packet dissection concepts."],
    ["Threat Vector", "Public Wi-Fi risks: Packet sniffing and Man-in-the-Middle (MitM) eavesdropping.", "Diagram MitM attack vectors on whiteboard."],
    ["Architecture", "The TCP Three-Way Handshake protocol state machine: SYN, SYN-ACK, ACK sequence.", "Walk through sequence numbering and state tracking."],
    ["Wireshark", "Wireshark layer encapsulation: Ethernet frame, IP packet, TCP segment, Application payload.", "Live demo of Wireshark stream inspection and display filters."],
    ["Nmap", "Nmap reconnaissance: Distinguishing Open, Closed, and Filtered port statuses.", "Demonstrate targeted port scanning in terminal."],
    ["Defense", "TLS 1.3 encryption: Converting application layer plaintext into uncrackable ciphertext.", "Display comparison of raw HTTP vs TLS application data."],
    ["Deep Inspection", "Forensics of a SYN Flood DoS: Exhausting TCP connection tables with half-open sockets.", "Show kernel socket statistics."],
    ["Case Study", "The Darkhotel APT campaign: Exploiting high-end hotel Wi-Fi to deliver targeted spyware.", "Discuss corporate travel security best practices."],
    ["Hands-On Lab", "12-minute lab: Sniffing live packets in Wireshark and running Nmap reconnaissance.", "Start 12-minute countdown timer and guide students."],
    ["Audit", "Audit verification checklist: Validating extracted plaintext strings and port telemetry.", "Review student captures on screen."],
    ["Evaluation", "10-point evaluation rubric breakdown.", "Review grading thresholds."],
    ["Summary", "Wrap-up and homework preview. Next session: Web application security & OWASP Top 10.", "Collect worksheets."]
]

NOTES = {"uz": N_UZ, "ru": N_RU, "en": N_EN}

# ---------------------------------------------------------------- Varaqa Body
V = []
V.append(sheet_header(
    h1=("Kiberxavfsizlik: Tarmoq Xavfsizligi va Wireshark",
        "Кибербезопасность: Сетевая Безопасность и Wireshark",
        "CyberSecurity: Network Security & Packet Analysis"),
    sub=("Amaliy Laboratoriya Varaqasi · 9-sinf · 5-hafta · 22-dars",
         "Практический Рабочий Лист · 9 класс · Неделя 5 · Урок 22",
         "Hands-On Lab Worksheet · Grade 9 · Week 5 · Lesson 22")
))

V.append(mission(
    h=("Laboratoriya Vazifasi: Paket Tahlili va Nmap Auditi",
       "Миссия Лабораторной: Анализ Пакетов и Аудит Nmap",
       "Lab Mission: Packet Sniffing & Port Reconnaissance"),
    p=("Wireshark orqali jonli tarmoq paketlarini tutib olish, shifrlanmagan HTTP POST so'rovidan parolni ajratib olish, "
       "va Nmap yordamida serverdagi ochiq portlar va xizmatlarni aniqlash.",
       "Захватить сетевые пакеты в Wireshark, извлечь открытый пароль из незашифрованного HTTP POST, "
       "и с помощью Nmap выявить открытые порты и версии служб на сервере.",
       "Capture live packets via Wireshark, extract plaintext credentials from an unencrypted HTTP POST stream, "
       "and map exposed ports and service versions using Nmap."))
)

V.append(table(
    headers=[
        ("Protokol / Bosqich", "Протокол / Этап", "Protocol / Phase"),
        ("Tekshirish Usuli", "Метод Проверки", "Verification Method"),
        ("Aniqlangan Ma'lumot", "Найденные Данные", "Extracted Telemetry"),
        ("Holat", "Статус", "Status")
    ],
    rows=[
        [("1. TCP Handshake", "1. TCP Handshake", "1. TCP Handshake"),
         ("Wireshark filtri: `tcp.flags.syn == 1`", "Фильтр: `tcp.flags.syn == 1`", "Filter: `tcp.flags.syn == 1`"),
         ("SYN -> SYN-ACK -> ACK ketma-ketligi", "Последовательность SYN -> SYN-ACK -> ACK", "SYN -> SYN-ACK -> ACK sequence"),
         ("✅ Aniqlandi", "✅ Найдено", "✅ Verified")],
        [("2. HTTP Sniffing", "2. Сниффинг HTTP", "2. HTTP Sniffing"),
         ("`http.request.method == \"POST\"`", "`http.request.method == \"POST\"`", "`http.request.method == \"POST\"`"),
         ("Ochiq matndagi login va parol", "Открытый логин и пароль в теле пакета", "Plaintext username and password"),
         None],
        [("3. Nmap Skanerlash", "3. Сканирование Nmap", "3. Nmap Port Audit"),
         ("`nmap -sV -p 80,443,2222 &lt;target&gt;`", "`nmap -sV -p 80,443,2222 &lt;target&gt;`", "`nmap -sV -p 80,443,2222 &lt;target&gt;`"),
         ("Ochiq portlar va dastur versiyalari", "Список открытых портов и версий служб", "Open ports and service banners"),
         None],
        [("4. HTTPS Himoyasi", "4. Проверка HTTPS", "4. HTTPS Verification"),
         ("Wireshark: `tls.handshake`", "Wireshark: `tls.handshake`", "Wireshark: `tls.handshake`"),
         ("Trafik to'liq shifrlangan (Application Data)", "Трафик зашифрован (Application Data)", "TLS encrypted Application Data"),
         None],
    ]
))

V.append(sheet_box(
    h=("Tarmoq Tahlili va Nazariy Savollar", "Сетевой Анализ и Вопросы", "Network Forensics & Written Analysis"),
    body_html=writelines(3, label=("1. Nega ochiq Wi-Fi tarmog'ida HTTP orqali parollarni kiritish o'ta xavfli?",
                                   "1. Почему ввод паролей по HTTP в открытых Wi-Fi сетях крайне опасен?",
                                   "1. Why is submitting credentials over HTTP on public Wi-Fi exceptionally hazardous?"))
             + "<br>"
             + writelines(3, label=("2. Nmap skanida 'Filtered' va 'Closed' port holatlari o'rtasida qanday farq bor?",
                                   "2. В чём разница между состояниями портов 'Filtered' и 'Closed' в отчёте Nmap?",
                                   "2. Explain the fundamental difference between 'Filtered' and 'Closed' port states in Nmap?"))
))

V.append(sheet_box(
    h=("Baholash Mezoni (10 Ball)", "Критерии Оценки (10 Баллов)", "Grading Rubric (10 Points)"),
    body_html=rubric([
        (("Wiresharkda paketlar to'g'ri filtrlanib, HTTP parol ajratilgan", "В Wireshark применён фильтр и найден пароль", "Wireshark filter applied and password captured"), "3 ball"),
        (("TCP Three-Way Handshake ketma-ketligi aniqlangan", "Идентифицированы этапы TCP Handshake", "TCP Handshake stages identified"), "3 ball"),
        (("Nmap orqali ochiq portlar va xizmatlar topilgan", "С помощью Nmap определены службы на портах", "Nmap port and service audit executed"), "2 ball"),
        (("Nazariy savollarga to'liq va asosli javob yozilgan", "Даны развернутые ответы на теоретические вопросы", "Written analytical queries answered thoroughly"), "2 ball"),
    ], "10 ball")
))

V.append("</div>\n" + sign_box("Musulmonov Mamarajab"))

VARAQA_BODY = "\n".join(V)

lesson = Lesson(
    outdir=D,
    titles=TITLES,
    sheet_titles=SHEET_TITLES,
    key="vc-notes-9-22",
    slides=S,
    notes=NOTES,
    varaqa_body=VARAQA_BODY
)

if __name__ == "__main__":
    out = lesson.build()
    print("Created:", out)
