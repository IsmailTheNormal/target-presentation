# -*- coding: utf-8 -*-
"""9-sinf · 4-hafta · 20-dars — Full-Stack Deploy va Demo Day: Prodaction Muhandislik va Jonli Taqdimot."""

import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from build import (Lesson, slide, title_slide, box, code, el, i18n,
                   sheet_header, mission, table, sheet_box, rubric, writelines, sign_box)

D = "classes/9-sinf/4-hafta/20-dars-fullstack-deploy-va-demo-day"

TITLES = {
    "uz": "20-dars: Full-Stack Deploy va Demo Day — Prodaction Muhandislik va Taqdimot",
    "ru": "Урок 20: Full-Stack Деплой и Demo Day — Продакшен-Инженерия и Презентация",
    "en": "Lesson 20: Full-Stack Cloud Deployment & Demo Day — Production Engineering & Pitch",
}
SHEET_TITLES = {k: v + (" — Ish Varaqasi" if k == "uz" else
                        " — Рабочий Лист" if k == "ru" else " — Worksheet")
                for k, v in TITLES.items()}

S = []

# 1. Title Slide
S.append(title_slide(
    ph=("Kirish", "Введение", "Intro"), time="0–3",
    eyebrow=("Vibecoding · 20-dars · 9-sinf (Kulminatsiya & Demo Day)",
             "Vibecoding · Урок 20 · 9 класс (Кульминация и Demo Day)",
             "Vibecoding · Lesson 20 · Grade 9 (Culmination & Demo Day)"),
    h1=("Full-Stack Deploy va Demo Day: Prodaction Muhandislik",
        "Full-Stack Деплой и Demo Day: Продакшен-Инженерия",
        "Full-Stack Cloud Deployment & Demo Day: Production Engineering"),
    lede=("Biz Docker bilan konteynerladik, PostgreSQL relyatsion arxitekturasini qurdik va "
          "vebhooklar orqali real-vaqt integratsiyasini yaratdik. Bugun butun tizimni yagona "
          "<b>Docker Compose</b> orqali bulutga chiqaramiz, <b>Nginx Reverse Proxy</b> va "
          "<b>SSL (HTTPS)</b> bilan qulflaymiz hamda <b>90 soniyalik Jonli Demo Day</b> o'tkazib, "
          "haqiqiy loyihangizni internet auditoriyasiga taqdim etasiz!",
          "Мы упаковали код в Docker, создали базу данных PostgreSQL и настроили "
          "автоматизацию на вебхуках. Сегодня мы объединяем всю систему через <b>Docker Compose</b>, "
          "защищаем её <b>Nginx Reverse Proxy</b> и <b>SSL-сертификатом</b>, а затем проводим "
          "<b>90-секундный Живой Demo Day</b>, презентуя работающий сервис всему миру!",
          "We containerized applications with Docker, engineered relational PostgreSQL schemas, and wired "
          "event-driven webhooks. Today we orchestrate the entire multi-tier stack with <b>Docker Compose</b>, "
          "shield it behind an <b>Nginx Reverse Proxy with automated SSL</b>, and execute a high-stakes "
          "<b>90-Second Live Demo Day Pitch</b> showcasing production-grade software to the world!"),
    meta=[("<b>Fan:</b> Vibecoding · Prodaction & DevOps",
           "<b>Предмет:</b> Vibecoding · Продакшен и DevOps",
           "<b>Subject:</b> Vibecoding · Production & DevOps"),
          ("<b>Kohorta:</b> 9-sinf Junior Vibecoder",
           "<b>Когорта:</b> 9 класс Junior Vibecoder",
           "<b>Cohort:</b> Grade 9 Junior Vibecoder"),
          ("<b>Hafta:</b> 4 (4-soat · Final)", "<b>Неделя:</b> 4 (4-й час · Финал)", "<b>Week:</b> 4 (Hour 4 · Final)")],
))

# 2. Production Architecture: Multi-Tier Model
S.append(slide(
    ph=("Arxitektura", "Архитектура", "Architecture"), time="3–6",
    eyebrow=("3 qatlamli sanoat arxitekturasi", "3-уровневая архитектура", "3-tier production architecture"),
    title=("Sanoat Standartidagi 3 Qatlamli Bulut Tizimi",
           "3-Уровневая Продакшен-Архитектура в Облаке",
           "3-Tier Production Cloud Architecture"),
    body='<div class="cols c2">\n'
         + box("ink", ("Arxitektura Zanjiri (Tashqaridan Ichkariga)",
                       "Цепочка Запроса (Снаружи Внутрь)",
                       "Request Pipeline Flow"),
               items=[
                   ("<b>1. Kirish darvozasi (Port 443 HTTPS):</b> Internet trafigi to'g'ridan-to'g'ri Nginx ga keladi. SSL sertifikati shifrlashni shu yerda yechadi (SSL Termination).",
                    "<b>1. Шлюз (Порт 443 HTTPS):</b> Трафик из интернета встречает Nginx, снимая шифрование SSL (SSL Termination).",
                    "<b>1. Ingress (Port 443 HTTPS):</b> External traffic terminates at Nginx for SSL decryption and gzip compression."),
                   ("<b>2. Veb-xizmat (Node.js Container):</b> Nginx ichki tarmoq orqali so'rovni Node ilovaga yo'naltiradi (`proxy_pass http://web:3000`).",
                    "<b>2. Веб-сервис (Node.js):</b> Nginx перенаправляет трафик на Node-приложение через внутреннюю сеть (`proxy_pass`).",
                    "<b>2. Application layer (Node.js):</b> Nginx proxies cleartext requests to internal container `http://web:3000`."),
                   ("<b>3. Baza qatlami (PostgreSQL Container):</b> Baza porti (5432) internetga mutlaqo ochilmaydi! Unga faqat web konteyner kira oladi.",
                    "<b>3. База данных (PostgreSQL):</b> Порт 5432 закрыт от интернета! Доступ имеет только контейнер бэкенда.",
                    "<b>3. Isolated database:</b> Port 5432 is strictly unexposed to WAN; accessible only via private Docker bridge."),
               ])
         + "\n"
         + box("accent", ("Nega Node.js To'g'ridan-To'g'ri Ochilmaydi?",
                          "Почему Node.js Не Выставляют Наружу?",
                          "Why Node.js Must Never Face WAN Directly"),
               items=[
                   ("<b>Privileged Ports:</b> 80 va 443 portlarni ochish uchun Node ilovani `root` huquqi bilan ishga tushirish kerak bo'ladi — bu kiber-falokat!",
                    "<b>Root-привилегии:</b> Запуск Node на 80/443 требует root-прав, что фатально при уязвимости в коде.",
                    "<b>Privileged root risks:</b> Binding port 80/443 requires root privileges, exposing the host if Node is compromised."),
                   ("<b>Statik fayllar:</b> Nginx rasmlar, CSS va JS fayllarni Node.js ga qaraganda 10 barobar tezroq va keshlab uzatadi.",
                    "<b>Статика:</b> Nginx отдаёт изображения, CSS и JS в 10 раз быстрее Node.js, экономя процессор.",
                    "<b>Static asset caching:</b> Nginx serves static media and CSS directly from disk cache 10x faster than Node."),
                   ("<b>DDoS va Rate Limiting:</b> Nginx sekundiga 100 ta so'rov yuborgan botlarni Node.js ga yetkazmasdanoq bloklaydi.",
                    "<b>Защита от DDoS:</b> Nginx отсекает спам-ботов и ограничивает частоту запросов на лету.",
                    "<b>Rate limiting & DDoS:</b> Nginx throttles abusive crawlers and bot attacks before they reach application workers."),
               ])
         + "\n</div>",
))

# 3. Docker Compose Orchestration
S.append(slide(
    ph=("Orkestratsiya", "Оркестрация", "Orchestration"), time="6–10",
    eyebrow=("Ko'p servisli tizim", "Мультисервисная система", "Multi-service orchestration"),
    title=("Docker Compose: Butun Tizimni Bitta Buyruqda Ko'tarish",
           "Docker Compose: Подъём Всей Системы Одной Командой",
           "Docker Compose: Multi-Container Orchestration"),
    body='<div class="cols c2">\n'
         + code("""# docker-compose.yml
version: '3.8'

services:
  web:
    build: .
    restart: always
    environment:
      - DATABASE_URL=postgres://user:pass@db:5432/production_db
      - PORT=3000
    depends_on:
      db:
        condition: service_healthy
    networks:
      - internal-net

  db:
    image: postgres:16-alpine
    restart: always
    environment:
      POSTGRES_USER: user
      POSTGRES_PASSWORD: pass
      POSTGRES_DB: production_db
    volumes:
      - pgdata:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U user -d production_db"]
      interval: 5s
      timeout: 5s
      retries: 5
    networks:
      - internal-net

volumes:
  pgdata:

networks:
  internal-net:
    driver: bridge""")
         + "\n"
         + box("green", ("Kritik Muhandislik Nuqtalari", "Критические Инженерные Точки", "Key Architecture Decisions"),
               items=[
                   ("<b>depends_on + condition:</b> Veb-xizmat baza to'liq yuklanib, `healthy` holatga o'tmaguncha start olmaydi (Crash oldi olinadi).",
                    "<b>depends_on + condition:</b> Бэкенд ждёт готовности базы данных перед запуском, исключая падение при старте.",
                    "<b>Health-gated startup:</b> `depends_on` prevents web crashes by waiting until PostgreSQL is fully healthy."),
                   ("<b>Doimiy Xotira (Volumes):</b> Baza konteyneri o'chib qayta yaratilsa ham, `pgdata` jildi barcha jadvallarni saqlab qoladi.",
                    "<b>Постоянные данные:</b> Том `pgdata` сохраняет все таблицы базы даже при полном пересоздании контейнера.",
                    "<b>Persistent volume:</b> Named volume `pgdata` guarantees data survival across container destroys and updates."),
                   ("<b>Yopiq Tarmoq (bridge):</b> `db` portlari `ports` qismida ko'rsatilmagan — tashqi dunyodan xaker unga ulana olmaydi.",
                    "<b>Изолированная сеть:</b> Порты БД не проброшены наружу, прямой доступ из интернета физически невозможен.",
                    "<b>Private internal network:</b> Database ports are omitted from host bindings, barring external WAN penetration."),
               ])
         + "\n</div>",
))

# 4. Nginx Reverse Proxy & Let's Encrypt SSL
S.append(slide(
    ph=("Nginx & SSL", "Nginx и SSL", "Nginx & SSL"), time="10–14",
    eyebrow=("Xavfsiz darvoza", "Безопасный шлюз", "Hardened gateway"),
    title=("Nginx Konfiguratsiyasi va Bepul SSL (Let's Encrypt)",
           "Конфигурация Nginx и Бесплатный SSL (Let's Encrypt)",
           "Nginx Gateway Configuration & Automated SSL"),
    body='<div class="cols c2">\n'
         + code("""# /etc/nginx/sites-available/cyber-app
server {
    listen 80;
    server_name api.target.uz;
    # Barcha HTTP so'rovlarni majburiy HTTPS ga yo'naltirish
    return 301 https://$host$request_uri;
}

server {
    listen 443 ssl http2;
    server_name api.target.uz;

    ssl_certificate /etc/letsencrypt/live/api.target.uz/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/api.target.uz/privkey.pem;

    location / {
        proxy_pass http://localhost:3000;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}""")
         + "\n"
         + box("ink", ("Certbot va Avtomatik Yangilanish", "Certbot и Автопродление", "Certbot Auto-Renewal"),
               items=[
                   ("<b>1 ta buyruq bilan SSL:</b> `sudo certbot --nginx -d api.target.uz` buyrug'i Let's Encrypt dan bepul rasmiy SSL oladi.",
                    "<b>SSL в 1 команду:</b> `certbot --nginx -d domain` автоматически получает сертификат Let's Encrypt.",
                    "<b>1-command SSL:</b> `sudo certbot --nginx -d api.target.uz` provisions trusted SSL certs in seconds."),
                   ("<b>Avtomatik uzaytirish:</b> Certbot har 60 kunda sertifikatni o'zi tekshiradi va yangilaydi (`certbot renew --dry-run`).",
                    "<b>Автопродление:</b> Certbot проверяет и продлевает сертификаты каждые 60 дней в фоновом режиме.",
                    "<b>Automated renewals:</b> Systemd timers test and renew certificates without human intervention."),
                   ("<b>X-Real-IP sarlavhasi:</b> Mijozning haqiqiy IP manzilini Nginx orqali Node.js ga xavfsiz yetkazadi.",
                    "<b>X-Real-IP:</b> Передаёт реальный IP-адрес пользователя в Node.js для логирования и аналитики.",
                    "<b>Client IP attribution:</b> `X-Real-IP` proxies true client IPs through reverse proxy layers."),
               ])
         + "\n</div>",
))

# 5. Zero-Downtime Deploy & Rolling Updates
S.append(slide(
    ph=("Deploy", "Деплой", "Zero-Downtime"), time="14–17",
    eyebrow=("Uzluksiz xizmat", "Бесперебойная работа", "Zero-downtime updates"),
    title=("Zero-Downtime Deploy: Foydalanuvchi Sezmagan Yangilanish",
           "Zero-Downtime Деплой: Обновления Без Остановки Сервиса",
           "Zero-Downtime Deployment & Rolling Upgrades"),
    body='<div class="cols c2">\n'
         + box("accent", ("Eski Usul (Downtime va Zararlar)",
                          "Устаревший подход (Остановка сервиса)",
                          "Legacy Outages (Downtime Flaws)"),
               items=[
                   ("<b>Serverni o'chirish:</b> Yangi kod chiqqanda `kill node` qilinadi. Sayt 2 daqiqaga ochilmay qoladi (`502 Bad Gateway`).",
                    "<b>Остановка процесса:</b> Перезапуск сервиса вырубает сайт на 2 минуты, теряя пользователей.",
                    "<b>Crude process termination:</b> Killing server processes throws 502 Bad Gateway errors for minutes."),
                   ("<b>Chala tranzaksiyalar:</b> Shu 2 daqiqa ichida to'lov qilayotgan mijozlarning puli yo'qoladi yoki muzlab qoladi.",
                    "<b>Обрыв транзакций:</b> Оплаты, происходящие в момент перезапуска, зависают с ошибками.",
                    "<b>Orphaned transactions:</b> In-flight payments abort mid-execution, corrupting user balances."),
               ])
         + "\n"
         + box("green", ("Prodaction Usul (Rolling Update)",
                         "Продакшен-подход (Rolling Update)",
                         "Production Rolling Update"),
               items=[
                   ("<b>1. Orqa fonda yangi build:</b> `docker compose build` yangi imagini fonda sokin tayyorlaydi.",
                    "<b>1. Фоновая сборка:</b> `docker compose build` собирает новый образ в фоне, старый сервис работает.",
                    "<b>1. Background build:</b> `docker compose build` prepares new container layers without touching active traffic."),
                   ("<b>2. Yangi konteynerni ko'tarish:</b> Yangi versiya ishga tushib, sog'lomlik testidan (`healthcheck`) o'tadi.",
                    "<b>2. Проверка здоровья:</b> Новый контейнер поднимается и проходит проверку работоспособности.",
                    "<b>2. Health-gated boot:</b> New instance boots and passes internal `/health` checks."),
                   ("<b>3. Trafigi almashtirish:</b> Yangi konteyner tayyor bo'lgandagina Nginx trafigi unga buriladi, eski konteyner to'xtatiladi.",
                    "<b>3. Переключение трафика:</b> Nginx мгновенно переключает трафик на новый контейнер без задержки.",
                    "<b>3. Instant traffic swap:</b> Upstream traffic switches seamlessly; obsolete instance terminates gracefully."),
                   ("<b>Natija:</b> 0 millisekund uzilish. Foydalanuvchi yangilanish bo'lganini mutlaqo sezmaydi!",
                    "<b>Итог:</b> Ровно 0 миллисекунд простоя. Пользователи даже не заметят деплоя!",
                    "<b>Outcome:</b> Bit-perfect 0ms downtime. End users never witness a service interruption."),
               ])
         + "\n</div>",
))

# 6. Observability: Logs, Health & Metrics
S.append(slide(
    ph=("Monitoring", "Мониторинг", "Observability"), time="17–20",
    eyebrow=("Tizim telemetriyasi", "Телеметрия системы", "System telemetry"),
    title=("Kiber-Kuzatuv: Jonli Loglar va Resurs Nazorati",
           "Кибер-Наблюдение: Логи и Мониторинг Ресурсов",
           "Observability: Live Telemetry, Logs & Health Checks"),
    body='<div class="cols c2">\n'
         + code("""# 1. Barcha servislarning jonli loglarini kuzatish
docker compose logs -f --tail 50

# 2. Resurslar sarfini real vaqtda ko'rish (CPU, RAM, Tarmoq)
docker stats --no-stream

# 3. Server sog'ligini tekshiruvchi HTTP endpoint
curl -I https://api.target.uz/api/health
# HTTP/2 200 OK
# Content-Type: application/json
# {"status":"UP","uptime":1420,"db":"connected"}

# 4. Buzilgan konteynerlarni avtomatik qayta ko'tarish
# docker-compose.yml dagi `restart: unless-stopped` qoidasi""")
         + "\n"
         + box("ink", ("3 Ta Oltin Monitoring Qoidasi", "3 Золотых Правила Мониторинга", "3 Golden Telemetry Rules"),
               items=[
                   ("<b>Hech qachon 'ko'r' ishlamang:</b> Loglarsiz server — chiroqsiz tunda haydalayotgan avtomobil kabidir.",
                    "<b>Не работайте вслепую:</b> Сервер без логов — как автомобиль без фар ночью.",
                    "<b>Never fly blind:</b> A server without unified structured logging is an unmanageable black box."),
                   ("<b>Structured JSON Logs:</b> Loglarni matn emas, JSON ko'rinishida yozing (vaqt, daraja, so'rov_id, foydalanuvchi_id).",
                    "<b>Структурированные логи:</b> Пишите логи в JSON для быстрой фильтрации и поиска аномалий.",
                    "<b>Structured JSON logs:</b> Emit JSON telemetry with timestamps, log levels, request UUIDs, and user IDs."),
                   ("<b>Health Endpoint majburiy:</b> `/api/health` bazaga ulanishni va xotira holatini har 10 soniyada tekshirib turishi shart.",
                    "<b>Обязательный Health Check:</b> Эндпоинт `/api/health` тестирует базу и память каждые 10 секунд.",
                    "<b>Mandatory Health Endpoint:</b> `/api/health` asserts database readiness and memory pressure dynamically."),
               ])
         + "\n</div>",
))

# 7. Demo Day Pitch Standard: The 90-Second Rule
S.append(slide(
    ph=("Taqdimot", "Презентация", "Demo Day"), time="20–23",
    eyebrow=("90 soniyalik qat'iy standart", "Жесткий 90-секундный регламент", "90-second pitch framework"),
    title=("Demo Day Qoidasi: 90 Soniyada Dunyoni Hayratda Qoldirish",
           "Стандарт Demo Day: Покорить Аудиторию за 90 Секунд",
           "The 90-Second Demo Day Pitch Framework"),
    body='<div class="cols c2">\n'
         + box("accent", ("90 Soniyaning Daqiqali Rejasi", "Поминутный Регламент (90 сек)", "Minute-by-Minute Breakdown"),
               items=[
                   ("<b>00–15s · Muammo (The Hook):</b> O'zbekistonda/dunyoda qanday og'riqli muammo bor? Sanoat nima uchun qiynalmoqda?",
                    "<b>00–15 сек · Боль (The Hook):</b> Какую острую проблему решает ваш сервис? В чём боль рынка?",
                    "<b>00–15s · Problem Hook:</b> What acute friction exists in industry today? Frame the core pain point."),
                   ("<b>15–45s · Jonli Namoyish (Live Demo):</b> Saytni oching! Auditoriya telefonida QR kodni skanerlab ko'rsin. Haqiqiy ma'lumot kiriting.",
                    "<b>15–45 сек · Живой Показ:</b> Откройте рабочий сайт! Пусть зал отсканирует QR-код со смартфона.",
                    "<b>15–45s · Live Proof:</b> Open production deployment! Audience scans QR code on smartphones. Show real data."),
                   ("<b>45–70s · Muhandislik Steki (Under the Hood):</b> Docker konteynerlar, PostgreSQL bazasi, Webhook va Nginx SSL qanday ishlayotganini ko'rsating.",
                    "<b>45–70 сек · Стек и Инженерия:</b> Покажите Docker, базу PostgreSQL, вебхуки и защиту Nginx SSL.",
                    "<b>45–70s · Engineering Depth:</b> Highlight Docker Compose, PostgreSQL schema, Webhooks, and Nginx SSL."),
                   ("<b>70–90s · Xulosa va Kelajak (Call to Action):</b> Loyihaning keyingi qadami nima? Tomoshabinlar savoliga 1 ta kuchli yakun.",
                    "<b>70–90 сек · Финал и Призыв:</b> Каковы планы развития? Уверенная точка и переход к Q&A.",
                    "<b>70–90s · Vision & Close:</b> Roadmap milestones, business potential, and a confident segue into Q&A."),
               ])
         + "\n"
         + box("green", ("Demo Dayda Taqiqlanadi va Talab Qilinadi",
                         "Что Запрещено и Что Требуется",
                         "Forbidden Antipatterns & Winning Traits"),
               items=[
                   ("<b>❌ Taqiqlanadi:</b> Slaydlardan matn o'qish, 'Mening kompyuterimda ishlayotgandi' deb bahona qilish.",
                    "<b>❌ Запрещено:</b> Читать текст со слайдов, оправдываться «на ноутбуке работало».",
                    "<b>❌ Banned:</b> Reading text walls from slides, or excusing failures with \"it worked locally\"."),
                   ("<b>❌ Taqiqlanadi:</b> Ishlamaydigan tugmani bosib tushuntirib o'tirish. Faqat jonli, tekshirilgan funksiya ko'rsatiladi.",
                    "<b>❌ Запрещено:</b> Кликать сломанные кнопки. Показывайте только 100% стабильный функционал.",
                    "<b>❌ Banned:</b> Clicking broken links or unverified features. Present battle-tested code paths only."),
                   ("<b>✅ Talab qilinadi:</b> Kiber-ishonch, aniq ovoz, ekranda jonli ishlayotgan internetdagi URL manzil.",
                    "<b>✅ Требуется:</b> Инженерная уверенность, четкий голос, живой общедоступный URL в браузере.",
                    "<b>✅ Required:</b> Engineering poise, crisp delivery, and a reachable public HTTPS deployment."),
               ])
         + "\n</div>",
))

# 8. Production Checklist: Before Going Live
S.append(slide(
    ph=("Checklist", "Чек-лист", "Checklist"), time="23–25",
    eyebrow=("Jonli efir oldidan", "Перед живым показом", "Pre-flight checks"),
    title=("Prodaction Checklist: Jonli Taqdimot Oldidan Tekshiruv",
           "Продакшен Чек-лист: Финальная Проверка Перед Стартом",
           "Production Pre-Flight Checklist Before Going Live"),
    body='<div class="cols c2">\n'
         + box("ink", ("5 Bosqichli Kiber-Tekshiruv", "5 Шагов Проверки", "5-Step Verification Gate"),
               items=[
                   ("<b>1. HTTPS Yashil Qulf:</b> Brauzerda qizil xatolik yo'qligini, SSL sertifikati yashil turganini tekshiring.",
                    "<b>1. Зелёный замок SSL:</b> Убедитесь, что сертификат валиден и нет предупреждений безопасности.",
                    "<b>1. Valid SSL lock:</b> Confirm browser green padlock with zero mixed-content or expiry warnings."),
                   ("<b>2. QR Kod Tayyor:</b> Ekrandagi QR kod to'g'ri ishlab chiqarish manziliga olib borishini telefoningizda sinab ko'ring.",
                    "<b>2. QR-код протестирован:</b> Проверьте смартфоном, что QR ведёт на боевой HTTPS домен.",
                    "<b>2. QR code scanned:</b> Verify mobile camera redirects flawlessly to production HTTPS domain."),
                   ("<b>3. Baza Ma'lumotlari Toza:</b> Sinov paytida kiritilgan 'asdasd' kabi test ma'lumotlarni o'chirib, chiroyli demo holatga keltiring.",
                    "<b>3. Данные очищены:</b> Удалите мусорные тесты («asdasd»), подготовьте реалистичные демо-данные.",
                    "<b>3. Seed data primed:</b> Flush garbage test inputs ('asdasd') and load realistic demonstration records."),
                   ("<b>4. /health Javob Beradi:</b> `curl` orqali xizmat statusi 200 OK qaytarayotganini ko'ring.",
                    "<b>4. Health Check в норме:</b> Запрос к `/health` отдаёт статус 200 OK и статус базы.",
                    "<b>4. Health check green:</b> Verify `/health` responds with HTTP 200 and database connectivity status."),
                   ("<b>5. Zaxira Reja (Backup):</b> Agar internet uzilsa, mahalliy Docker konteyneringiz ham tayyor tursin.",
                    "<b>5. План Б:</b> Имейте локально запущенный Docker-контейнер на случай сбоя интернета в зале.",
                    "<b>5. Fallback plan:</b> Keep an active local Docker instance primed in case room Wi-Fi fails."),
               ])
         + "\n"
         + box("accent", ("Auditoriya Baholashi Mezonlari", "Критерии Оценки Зала", "Audience Evaluation Dimensions"),
               items=[
                   ("<b>Tezlik va Javob Berish:</b> Sayt sahifalari necha millisekundda yuklanmoqda?",
                    "<b>Скорость:</b> Насколько быстро откликаются страницы под нагрузкой аудитории?",
                    "<b>Latency:</b> How swiftly do UI views and API routes resolve under audience traffic?"),
                   ("<b>Dizayn va Qulaylik:</b> Target School dizayn tizimi (Navy, Oq, Qizil) qoidalari saqlanganmi?",
                    "<b>Дизайн:</b> Соблюдены ли фирменные цвета Target School и правила аккуратного UI?",
                    "<b>UI Polish:</b> Does interface adhere to clean typography, mobile responsiveness, and dark mode?"),
                   ("<b>Muhandislik Chuqurligi:</b> Savollarga qanchalik professional javob berildi?",
                    "<b>Глубина:</b> Насколько аргументированно спикер отвечает на технические вопросы?",
                    "<b>Technical depth:</b> How authoritatively does presenter justify architectural trade-offs?"),
               ])
         + "\n</div>",
))

# 9. Mission Briefing
S.append(slide(
    ph=("Amaliyot", "Практика", "Hands-on"), time="25–28",
    eyebrow=("12 daqiqalik laboratoriya", "12-минутная лаборатория", "12-minute lab"),
    title=("Amaliy Missiya: Tizimni Deploy Qilish va QR Kod Tayyorlash",
           "Практическая Миссия: Деплой Системы и Подготовка QR-Кода",
           "Hands-on Mission: Orchestrated Deployment & Demo Preparation"),
    body='<div class="cols c2">\n'
         + box("accent", ("Missiya vazifalari", "Задачи миссии", "Mission requirements"),
               items=[
                   ("<b>1. Compose Ishga Tushirish:</b> `docker compose up -d --build` bilan butun stekni fonda ko'taring.",
                    "<b>1. Запуск Compose:</b> Поднимите весь стек командой `docker compose up -d --build`.",
                    "<b>1. Spin up Stack:</b> Launch multi-container stack via `docker compose up -d --build`."),
                   ("<b>2. Telemetriya Tekshiruvi:</b> `docker compose ps` va `curl http://localhost:3000/api/health` bilan tekshiring.",
                    "<b>2. Проверка статуса:</b> Проверьте статус контейнеров и ответ эндпоинта `/api/health`.",
                    "<b>2. Telemetry Verification:</b> Inspect container states and verify `/api/health` 200 OK response."),
                   ("<b>3. QR Kod Generatsiya:</b> Saytingiz URL manzili uchun QR kod yarating va ekranga chiqaring.",
                    "<b>3. Генерация QR:</b> Сгенерируйте QR-код для вашего продакшен-домена.",
                    "<b>3. QR Code Generation:</b> Generate high-contrast QR code pointing to your live URL."),
                   ("<b>4. 90 Soniyalik Nutq Tayyorlash:</b> Ish varaqasidagi 4 qismdan iborat pitch rejasini to'ldiring.",
                    "<b>4. Подготовка речи:</b> Заполните 4 ключевых тезиса 90-секундного питча в рабочем листе.",
                    "<b>4. Pitch Outline:</b> Draft the 4 structured bullet points of your 90-second pitch on the sheet."),
               ])
         + "\n"
         + box("ink", ("Ish Maydoni Ko'rsatmalari", "Указания к Работе", "Workstation Directives"),
               items=[
                   ("<b>Terminal:</b> Konteynerlar loglarini `docker compose logs -f` bilan ochiq tuting.",
                    "<b>Терминал:</b> Держите открытым окно логов `docker compose logs -f`.",
                    "<b>Terminal:</b> Keep streaming logs open via `docker compose logs -f` for live telemetry."),
                   ("<b>Qog'oz varaqa:</b> Barcha URL, konteyner ID va nutq rejasini ish varaqasiga yozing.",
                    "<b>Рабочий лист:</b> Зафиксируйте URL, ID контейнеров и тезисы в распечатанном бланке.",
                    "<b>Worksheet:</b> Document live deployment URLs, container states, and pitch thesis on paper."),
               ])
         + "\n</div>",
))

# 10. Live Timer
S.append(slide(
    ph=("Taymer", "Таймер", "Timer"), time="28–37",
    eyebrow=("Mustaqil tayyorgarlik", "Самостоятельная подготовка", "Independent lab"),
    title=("Laboratoriya Ishi: 12 Daqiqa",
           "Лабораторная Работа: 12 Минут",
           "Laboratory Execution: 12 Minutes"),
    body='<div class="timer-card" data-timer="720">\n'
         + '  <div class="timer-display">12:00</div>\n'
         + '  <div class="timer-controls">\n'
         + '    <button class="navbtn" data-action="start" '
         + i18n("Boshlash", "Старт", "Start") + '>Boshlash</button>\n'
         + '    <button class="navbtn" data-action="pause" '
         + i18n("Pauza", "Пауза", "Pause") + '>Pauza</button>\n'
         + '    <button class="navbtn" data-action="reset" '
         + i18n("Qaytarish", "Сброс", "Reset") + '>Qaytarish</button>\n'
         + '  </div>\n'
         + '  <p style="color:var(--ink-2); font-size:13px; margin-top:14px;" '
         + i18n("Stekni ko'taring, sog'lomlikni tekshiring, QR kodni tayyorlang va 90 soniyalik nutqingizni sinab ko'ring.",
                "Поднимите стек, проверьте здоровье, подготовьте QR и отрепетируйте 90-секундную речь.",
                "Deploy stack, assert health, prep QR code, and rehearse your 90-second pitch.")
         + ">Stekni ko'taring, sog'lomlikni tekshiring, QR kodni tayyorlang va 90 soniyalik nutqingizni sinab ko'ring.</p>\n"
         + '</div>',
))

# 11. Live Demo Day Stage
S.append(slide(
    ph=("Demo Day", "Demo Day", "Live Pitches"), time="37–42",
    eyebrow=("Jonli himoya bosqichi", "Живая защита проектов", "Live project defense"),
    title=("Sahna Sizniki: 90 Soniyalik Jonli Demo Day",
           "Сцена Ваша: 90-Секундный Живой Demo Day",
           "The Stage is Yours: 90-Second Live Demo Day"),
    body='<div class="cols c2">\n'
         + box("green", ("Taqdimotchi uchun 4 Qadam", "4 Шага Докладчика", "4 Steps for Presenters"),
               items=[
                   ("<b>1. Ekranga loyihani chiqaring:</b> Sayt ochiq tursin, brauzer konsoli toza bo'lsin.",
                    "<b>1. Откройте проект:</b> Браузер на весь экран, консоль разработчика чиста.",
                    "<b>1. Fullscreen live URL:</b> Production app open in browser with clean devtools console."),
                   ("<b>2. QR kodni ko'rsating:</b> Hakamlar va o'rtoqlaringiz telefonida ochib ko'rishsin.",
                    "<b>2. Покажите QR-код:</b> Дайте залу 10 секунд на сканирование и открытие проекта.",
                    "<b>2. Display QR code:</b> Give audience 10 seconds to scan and load your application on mobile."),
                   ("<b>3. Bosh vazifani bajaring:</b> Saytingizdagi eng asosiy imkoniyatni jonli ko'rsating (Xarid, Buyurtma, AI tahlil).",
                    "<b>3. Покажите главное:</b> Продемонстрируйте ключевую фичу (покупка, заказ, аналитика).",
                    "<b>3. Execute core user journey:</b> Demonstrate prime value proposition (checkout, ingest, analysis)."),
                   ("<b>4. 90 soniyada to'xtang:</b> Vaqt tugaganda to'xtash — professional muhandislik intizomi belgisidir.",
                    "<b>4. Стоп ровно в 90 сек:</b> Уважение тайминга — признак зрелого инженера.",
                    "<b>4. Conclude at 90s:</b> Strict time discipline signals professional engineering maturity."),
               ])
         + "\n"
         + box("ink", ("Hakamlar va Auditoriya Savollari", "Вопросы Жюри и Зала", "Evaluation Questions"),
               items=[
                   ("<i>\"Server qulab qolsa ma'lumotlar saqlanib qoladimi?\"</i> — Docker volumes va PostgreSQL javobi.",
                    "<i>«Что будет при падении сервера?»</i> — Ответ: защита данных через тома Docker и транзакции.",
                    "<i>\"What happens on server crashes?\"</i> — Explain persistent volumes and ACID durability."),
                   ("<i>\"Soxta so'rovlardan qanday himoyalangansiz?\"</i> — HMAC SHA-256 va Prepared Statements javobi.",
                    "<i>«Как защищаетесь от взлома?»</i> — Ответ: подписи HMAC и параметризованные запросы SQL.",
                    "<i>\"How is it defended against spoofing?\"</i> — Detail HMAC signatures and parameterized SQL queries."),
                   ("<i>\"Nega aynan shu arxitektura tanlandi?\"</i> — Unumdorlik va kengayuvchanlik asoslari.",
                    "<i>«Почему именно такая архитектура?»</i> — Обоснование скорости и масштабируемости.",
                    "<i>\"Why this specific topology?\"</i> — Justify performance, security, and scalability trade-offs."),
               ])
         + "\n</div>",
))

# 12. Conclusion, Quarter 1 Review & 10-Point Rubric
S.append(slide(
    ph=("Xulosa", "Итоги", "Final Recap"), time="42–45",
    eyebrow=("1-Chorak yakuni va baholash", "Итоги 1-й четверти и оценка", "Quarter 1 wrap-up & grading"),
    title=("1-Chorak G'alabasi va Baholash Mezoni (10 Ball)",
           "Победа 1-й Четверти и Критерии Оценки (10 Баллов)",
           "Quarter 1 Milestone & 10-Point Final Rubric"),
    body='<div class="cols c2">\n'
         + box("green", ("1-Chorakda Siz Nimalarga Erishdingiz?",
                         "Чего Вы Достигли в 1-й Четверти?",
                         "Your Journey Across Quarter 1"),
               items=[
                   ("<b>Frontend va UI/UX:</b> Semantik HTML, Zamonaviy CSS, Flexbox, Grid va Moslashuvchan dizayn.",
                    "<b>Frontend и UI/UX:</b> Семантический HTML, современный CSS, Flexbox, Grid и адаптивность.",
                    "<b>Frontend & UI/UX:</b> Semantic HTML, modern CSS, Flexbox, Grid, and mobile responsiveness."),
                   ("<b>Backend va API:</b> REST API, JSON, Asinxron JavaScript va Doimiy xotira (LocalStorage).",
                    "<b>Backend и API:</b> REST API, JSON, асинхронный JS и локальное хранилище.",
                    "<b>Backend & API:</b> REST APIs, JSON data structures, async JS, and state persistence."),
                   ("<b>Git va Kiber-Hamkorlik:</b> Commit, Branch, Merge Konfliktlari, Pull Request va CI/CD Actions.",
                    "<b>Git и командная работа:</b> Коммиты, ветки, мердж-конфликты, Pull Request и CI/CD.",
                    "<b>Git & Collaboration:</b> Commits, branches, merge conflicts, Pull Requests, and automated CI/CD."),
                   ("<b>DevOps va Ma'lumotlar:</b> Docker konteynerlar, PostgreSQL, SQL xavfsizligi, Webhooklar va Deploy.",
                    "<b>DevOps и Данные:</b> Docker-контейнеры, PostgreSQL, SQL-безопасность, вебхуки и деплой.",
                    "<b>DevOps & Data:</b> Docker containers, PostgreSQL schemas, SQL injection defense, webhooks, and live deploy."),
               ])
         + "\n"
         + box("accent", ("10 Ballik Baholash Mezoni", "Критерии на 10 Баллов", "10-Point Final Rubric"),
               items=[
                   ("<b>2 ball:</b> 3 qatlamli arxitektura va Nginx Reverse Proxy tushunchasi.",
                    "<b>2 балла:</b> Понимание 3-уровневой архитектуры и Nginx Reverse Proxy.",
                    "<b>2 points:</b> Clear explanation of 3-tier architecture and Nginx Reverse Proxy."),
                   ("<b>3 ball:</b> To'g'ri sozlangan `docker-compose.yml` va Healthcheck.",
                    "<b>3 балла:</b> Корректный docker-compose.yml и рабочий Healthcheck.",
                    "<b>3 points:</b> Well-configured `docker-compose.yml` with working healthcheck."),
                   ("<b>3 ball:</b> Jonli ishlayotgan HTTPS xizmati va QR kod integratsiyasi.",
                    "<b>3 балла:</b> Работающий HTTPS сервис и интеграция с QR-кодом.",
                    "<b>3 points:</b> Reachable HTTPS service with functional QR code integration."),
                   ("<b>2 ball:</b> 90 soniyalik intizomli va ishonchli Demo Day nutqi.",
                    "<b>2 балла:</b> Уверенный 90-секундный питч на Demo Day без запинок.",
                    "<b>2 points:</b> Confident, disciplined 90-second Demo Day presentation."),
               ])
         + "\n</div>",
))

# ----------------- SPEAKER NOTES (O'QITUVCHI UCHUN QO'LLANMA) -----------------
NOTES = {
    "uz": [
        ["Kirish", "Darsni butun 4-haftalik mehnatning tantanali yakuni sifatida boshlang.", "O'quvchilarga bugun ular shunchaki talaba emas, balki jonli mahsulotini namoyish qilayotgan yosh muhandis ekanliklarini ayting."],
        ["3 Qatlamli Model", "Nega Node.js to'g'ridan-to'g'ri internetga ochilmasligini doskada chizib tushuntiring.", "Nginx qanday qilib qorovul vazifasini o'tashini ko'rsating."],
        ["Docker Compose", "docker-compose.yml dagi `depends_on` va `volumes` qismlariga urg'u bering.", "Baza konteyneri o'chsa ham ma'lumotlar saqlanib qolishini ta'kidlang."],
        ["Nginx va SSL", "Certbot qanday qilib bepul SSL berishini va Nginx proksi sarlavhalarini (X-Forwarded-For) tushuntiring.", "Yashil qulf nima uchun mijoz ishonchi garovi ekanini ayting."],
        ["Zero-Downtime", "Katta kompaniyalar (Google, Amazon) yangilanish paytida hech qachon saytni o'chirmasligini ayting.", "Rolling updates va Healthcheck tamoyilini tushuntiring."],
        ["Monitoring", "Loglarni o'qish (docker compose logs -f) va /health endpointi ahamiyatini uqtiring.", "Server xotirasi to'lib qolmasligini nazorat qilishni o'rgating."],
        ["Demo Day Standarti", "90 soniyalik qat'iy reja bilan tanishtiring. Hech kim 90 soniyadan oshmasligi kerakligini ayting.", "Muvaffaqiyatli pitch sirlari: baland ovoz, ko'z aloqasi va jonli veb-sayt."],
        ["Checklist", "Jonli efir oldidan 5 ta tekshiruvdan o'tishni buyuring.", "Zaxira reja (offline rejim) har doim tayyor turishi kerakligini eslating."],
        ["Missiya", "12 daqiqalik tayyorgarlik va deploy missiyasini e'lon qiling.", "O'quvchilar QR kodlarini va nutq rejalarini tekshiring."],
        ["Taymer", "Taymer davomida o'quvchilarga Docker Compose va Nginx sozlamalaridagi xatoliklarni bartaraf etishda yordam bering.", "QR kodlar to'g'ri ochilayotganini o'zingiz ham tekshirib ko'ring."],
        ["Demo Day Sahna", "O'quvchilarni navbatma-navbat sahnaga chaqiring. Har biriga 90 soniya vaqt bering.", "Auditoriya bilan birgalikda jonli QR kodlarni skanerlang va qisqa texnik savollar bering."],
        ["Xulosa", "1-chorakni a'lo darajada yakunlagan barcha o'quvchilarni tabriklang!", "Ish varaqalarini yig'ib, yakuniy 10 ballik baholarni qo'ying. 2-chorakda Agentik Dasturlash boshlanishini e'lon qiling!"]
    ],
    "ru": [
        ["Введение", "Откройте урок как торжественный финал первого месяца упорного труда.", "Подчеркните: сегодня ребята выступают как настоящие инженеры, демонстрирующие боевой продукт."],
        ["3-Уровневая Модель", "Нарисуйте на доске цепочку: Интернет → Nginx → Node.js → PostgreSQL.", "Объясните, почему Nginx выступает надежным щитом перед бэкендом."],
        ["Docker Compose", "Разберите параметры `depends_on` и `volumes` в файле docker-compose.yml.", "Покажите, как персистентный том защищает данные от удаления."],
        ["Nginx и SSL", "Объясните получение SSL-сертификата через Certbot и проброс заголовков X-Real-IP.", "Подчеркните важность HTTPS для доверия пользователей."],
        ["Zero-Downtime", "Расскажите, как крупные корпорации обновляют софт без единой секунды простоя.", "Покажите роль Healthcheck в плавном переключении трафика."],
        ["Мониторинг", "Объясните важность чтения потоковых логов (`docker compose logs -f`).", "Покажите работу легковесного эндпоинта проверки здоровья `/health`."],
        ["Стандарт Demo Day", "Ознакомьте класс с жестким 90-секундным регламентом.", "Секрет идеального питча: уверенный голос, зрительный контакт и живой работающий сайт."],
        ["Чек-лист", "Проведите класс по 5 пунктам пре-флайт чек-листа перед выходом на сцену.", "Напомните о важности локального бэкапа на случай сбоя Wi-Fi."],
        ["Миссия", "Дайте старт 12-минутной подготовке к финальной защите.", "Контролируйте готовность QR-кодов и тезисов питча."],
        ["Таймер", "Помогайте исправлять ошибки маршрутизации портов и сборки контейнеров.", "Проверяйте читаемость QR-кодов со смартфона."],
        ["Demo Day Защита", "Приглашайте студентов на сцену по очереди, строго засекая 90 секунд.", "Сканируйте QR-коды из зала и задавайте практические технические вопросы."],
        ["Итоги", "Поздравьте класс с триумфальным завершением 1-й четверти!", "Соберите бланки, выставьте итоговые оценки и анонсируйте 2-ю четверть: Агентное Программирование!"]
    ],
    "en": [
        ["Introduction", "Frame this lesson as the ceremonial milestone capstone of Month 1.", "Instill pride: students are now emerging full-stack engineers deploying real cloud software."],
        ["3-Tier Architecture", "Diagram the ingress topology: WAN → Nginx (443) → Node app → Isolated DB.", "Explain security benefits of terminating cleartext inside private bridges."],
        ["Docker Compose", "Highlight `depends_on: condition: service_healthy` and persistent `volumes`.", "Demonstrate data survival across complete container teardowns."],
        ["Nginx & SSL", "Explain Certbot automated provisioning and proxy headers (`X-Forwarded-Proto`).", "Reinforce that HTTPS is the universal barrier to production entry."],
        ["Zero-Downtime", "Discuss how enterprise tech giants deploy code thousands of times a day without outages.", "Illustrate health-gated rolling updates."],
        ["Observability", "Demonstrate streaming logs (`docker compose logs -f`) and metric profiling (`docker stats`).", "Enforce the `/health` endpoint invariant."],
        ["Demo Day Pitch", "Walk through the 4-phase 90-second pitch framework. Strictly enforce time limits.", "Stress live interaction over passive slide recitation."],
        ["Pre-Flight Checklist", "Guide students through the 5 pre-flight checklist gates before stepping on stage.", "Ensure offline Docker fallbacks are primed."],
        ["Mission Brief", "Launch the 12-minute deployment and pitch preparation countdown.", "Verify that QR codes navigate cleanly to target production URLs."],
        ["Live Timer", "Circulate assisting with Docker Compose network bindings and reverse proxy rules.", "Test audience QR scans directly from student screens."],
        ["Demo Day Pitches", "Call presenters to the stage one by one. Strictly enforce 90-second countdown.", "Scan mobile QR codes from the room and probe with architectural questions."],
        ["Quarter 1 Wrap-up", "Celebrate students' monumental achievement across Quarter 1!", "Collect worksheets, award final grades, and tease Quarter 2: Autonomous Agentic AI!"]
    ]
}

# ----------------- WORKSHEET (VARAQA) -----------------
VARAQA = (
    sheet_header(
        ("20-dars. Full-Stack Deploy va Demo Day: Prodaction Muhandislik va Taqdimot",
         "Урок 20. Full-Stack Деплой и Demo Day: Продакшен-Инженерия и Презентация",
         "Lesson 20. Full-Stack Cloud Deployment & Demo Day: Production Engineering & Pitch"),
        ("9-sinf · 4-hafta (4-soat · Final) · Prodaction & DevOps",
         "9 класс · 4-неделя (4-й час · Финал) · Продакшен и DevOps",
         "Grade 9 · Week 4 (Hour 4 · Final) · Production & DevOps")
    )
    + "\n"
    + mission(
        ("Amaliy Missiya: Full-Stack Loyihani Deploy Qilish, QR Kod Yaratish va Jonli Himoya",
         "Практическая Миссия: Полный Деплой Проекта, Генерация QR-Кода и Живая Защита",
         "Hands-on Mission: Full-Stack Cloud Deployment, QR Code Generation & Live Defense"),
        ("1. `docker-compose.yml` orqali Web va PostgreSQL servislarini fonda ko'taring.\n"
         "2. Nginx Reverse Proxy va SSL holatini tekshirib, `/api/health` javobini oling.\n"
         "3. Loyihangizning jonli HTTPS manzili uchun QR kod yarating va ekranga chiqaring.\n"
         "4. Ish varaqasidagi 90 soniyalik Demo Day nutq rejasini 4 ta aniq band bilan to'ldiring.\n"
         "5. Hakamlar va sinfdoshlar oldida 90 soniyalik jonli taqdimotni muvaffaqiyatli o'tkazing.",
         "1. Запустите сервисы Web и PostgreSQL в фоновом режиме через `docker-compose.yml`.\n"
         "2. Проверьте Nginx Reverse Proxy и SSL, убедитесь в статусе 200 OK на `/api/health`.\n"
         "3. Сгенерируйте QR-код для вашего живого HTTPS домена и выведите его на экран.\n"
         "4. Заполните тезисы 90-секундного питча в 4 разделах рабочего листа ниже.\n"
         "5. Проведите живую 90-секундную презентацию работающего проекта перед аудиторией.",
         "1. Spin up Web and PostgreSQL services in detached mode via `docker-compose.yml`.\n"
         "2. Audit Nginx Reverse Proxy & SSL status, confirming HTTP 200 on `/api/health`.\n"
         "3. Generate a high-contrast QR code for your live HTTPS URL and display it on screen.\n"
         "4. Draft the 4 thesis points of your 90-second Demo Day pitch on the worksheet below.\n"
         "5. Deliver an authoritative 90-second live demonstration to the audience and jury.")
    )
    + "\n"
    + table(
        [("Bosqich", "Этап", "Stage"),
         ("Terminal / Sozlama", "Команда / Настройка", "Command / Configuration"),
         ("Kutilgan Natija / Tekshiruv", "Ожидаемый Результат / Проверка", "Expected Telemetry / Check")],
        [
            [("1 · Compose", "1 · Сборка", "1 · Compose"),
             ("docker compose up -d --build",
              "docker compose up -d --build",
              "docker compose up -d --build"),
             ("Konteynerlar holati: [ web: UP / db: healthy ]",
              "Статус контейнеров: [ web: UP / db: healthy ]",
              "Container status: [ web: UP / db: healthy ]")],
            [("2 · Health", "2 · Здоровье", "2 · Health"),
             ("curl -I https://api.target.uz/api/health",
              "curl -I https://api.target.uz/api/health",
              "curl -I https://api.target.uz/api/health"),
             ("HTTP Status: 200 OK · Baza holati: [ ULANDI / XATO ]",
              "HTTP Status: 200 OK · Статус БД: [ OK / Ошибка ]",
              "HTTP Status: 200 OK · DB connection: [ CONNECTED / ERR ]")],
            [("3 · QR & URL", "3 · QR и Домен", "3 · QR & URL"),
             ("Jonli Production Manzil:",
              "Боевой Production Адрес:",
              "Production URL:"),
             ("https://________________________________________________",
              "https://________________________________________________",
              "https://________________________________________________")],
            [("4 · Pitch", "4 · Питч", "4 · Pitch"),
             ("90 Soniyalik Demo Day Nutqi",
              "90-секундная речь Demo Day",
              "90-Second Demo Day Pitch"),
             ("Vaqt nazorati: _____ soniya · Natija: [ A'LO / YAXSHI ]",
              "Время выступления: _____ сек · Оценка: [ ОТЛИЧНО / ХОРОШО ]",
              "Pitch duration: _____ sec · Outcome: [ EXCELLENT / GOOD ]")]
        ]
    )
    + "\n"
    + '    <div class="rubric-grid">\n'
    + sheet_box(
        ("🎤 90 Soniyalik Demo Day Nutq Rejasi",
         "🎤 Тезисы 90-Секундного Питча",
         "🎤 90-Second Pitch Structure"),
        writelines(1, ("1. Muammo (00–15s — Bozor va foydalanuvchining og'riqli muammosi):",
                       "1. Проблема (00–15 сек — Боль пользователя и рынка):",
                       "1. Problem (00–15s — User and market friction point):"))
        + "\n"
        + writelines(1, ("2. Yechim va Jonli Namoyish (15–45s — Saytda nima ko'rsatiladi):",
                         "2. Решение (15–45 сек — Что показываем вживую на сайте):",
                         "2. Solution & Live Demo (15–45s — What is demonstrated live):"))
        + "\n"
        + writelines(1, ("3. Texnik Stek (45–70s — Docker, Postgres, Webhook, Nginx, SSL):",
                         "3. Стек (45–70 сек — Docker, Postgres, Webhooks, Nginx, SSL):",
                         "3. Architecture (45–70s — Docker, Postgres, Webhooks, Nginx, SSL):"))
        + "\n"
        + writelines(1, ("4. Kelajak va Yakun (70–90s — Keyingi qadam va Call to Action):",
                         "4. Финал (70–90 сек — Следующие шаги и призыв):",
                         "4. Vision (70–90s — Roadmap and call to action):"))
    )
    + "\n"
    + sheet_box(
        ("📊 1-Chorak Yakuniy Baholash Mezoni (10 Ball)",
         "📊 Итоговые Критерии 1-й Четверти (10 Баллов)",
         "📊 Quarter 1 Final Grading Rubric (10 Points)"),
        rubric([
            (("3 qatlamli model va Nginx Reverse Proxy", "3-уровневая модель и Nginx Reverse Proxy", "3-tier architecture & Nginx proxy"), "2"),
            (("To'g'ri sozlangan docker-compose.yml", "Корректный docker-compose.yml", "Production docker-compose setup"), "3"),
            (("Jonli ishlayotgan HTTPS xizmat va QR kod", "Работающий HTTPS сервис и QR-код", "Live HTTPS deployment & QR code"), "3"),
            (("90 soniyalik intizomli Demo Day nutqi", "Уверенная речь на Demo Day (90 сек)", "Disciplined 90-sec Demo Day pitch"), "2"),
        ], "10")
    )
    + "\n    </div>\n  </div>\n"
    + sign_box()
)

if __name__ == "__main__":
    print(Lesson(D, TITLES, SHEET_TITLES, "vc-notes-9-20", S, NOTES, VARAQA).build())
