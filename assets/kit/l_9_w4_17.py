# -*- coding: utf-8 -*-
"""9-sinf · 4-hafta · 17-dars — Docker va Konteynerlar: Har Qanday Tizimda Bir Xil Ishlash Kafolati."""

import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from build import (Lesson, slide, title_slide, box, code, el, i18n,
                   sheet_header, mission, table, sheet_box, rubric, writelines, sign_box)

D = "classes/9-sinf/4-hafta/17-dars-docker-va-konteynerlar"

TITLES = {
    "uz": "17-dars: Docker va Konteynerlar — Tizimlararo Moslik Kafolati",
    "ru": "Урок 17: Docker и Контейнеры — Гарантия Совместимости Систем",
    "en": "Lesson 17: Docker and Containers — Cross-System Determinism",
}
SHEET_TITLES = {k: v + (" — Ish Varaqasi" if k == "uz" else
                        " — Рабочий Лист" if k == "ru" else " — Worksheet")
                for k, v in TITLES.items()}

S = []

# 1. Title Slide
S.append(title_slide(
    ph=("Kirish", "Введение", "Intro"), time="0–3",
    eyebrow=("Vibecoding · 17-dars · 9-sinf (DevOps Track)",
             "Vibecoding · Урок 17 · 9 класс (DevOps Track)",
             "Vibecoding · Lesson 17 · Grade 9 (DevOps Track)"),
    h1=("Docker va Konteynerlar: Har Qanday Tizimda Bir Xil Ishlash",
        "Docker и Контейнеры: Одинаковая Работа на Любой Системе",
        "Docker & Containers: Guaranteed Determinism Across Any System"),
    lede=("Dasturchilarning eng mashhur bahonasi: <b>\"Mening kompyuterimda ishlayotgandi-ku!\"</b> "
          "Serverda esa Node versiyasi boshqa, Linux kutubxonasi yetishmaydi, muhit buzilgan. "
          "Bugun siz dasturiy ta'minotni butun muhiti (kutubxonalar, sozlamalar, fayllar) bilan "
          "bitta ixcham qutiga o'rab, har qanday serverda bir soniyada ishga tushirishni — <b>Docker</b>ni o'rganasiz.",
          "Самая частая отговорка разработчиков: <b>«Но на моём компьютере всё работало!»</b> "
          "А на сервере другая версия Node, не хватает библиотек Linux, окружение сломано. "
          "Сегодня вы научитесь упаковывать приложение со всем его окружением в единую "
          "изолированную коробку и запускать её где угодно за секунду — с помощью <b>Docker</b>.",
          "The most notorious excuse in software: <b>\"It worked on my machine!\"</b> "
          "Yet on the server, Node versions mismatch, system binaries are missing, environments break. "
          "Today you learn to package your application with its entire runtime into a deterministic "
          "isolated box that boots in seconds anywhere — powered by <b>Docker</b>."),
    meta=[("<b>Fan:</b> Vibecoding · DevOps & Server Arxitekturasi",
           "<b>Предмет:</b> Vibecoding · DevOps и Архитектура Серверов",
           "<b>Subject:</b> Vibecoding · DevOps & Server Architecture"),
          ("<b>Kohorta:</b> 9-sinf Junior Vibecoder",
           "<b>Когорта:</b> 9 класс Junior Vibecoder",
           "<b>Cohort:</b> Grade 9 Junior Vibecoder"),
          ("<b>Hafta:</b> 4 (1-soat)", "<b>Неделя:</b> 4 (1-й час)", "<b>Week:</b> 4 (Hour 1)")],
))

# 2. Problem: Works on My Machine
S.append(slide(
    ph=("Muammo", "Проблема", "Problem"), time="3–6",
    eyebrow=("Real sanoat muammosi", "Реальная проблема индустрии", "Real industry problem"),
    title=("\"Mening Kompyuterimda Ishlayotgandi\" Sindromi",
           "Синдром «На Моём Компьютере Работало»",
           "The \"Works on My Machine\" Syndrome"),
    body='<div class="cols c2">\n'
         + box("accent", ("Klassik muammolar zanjiri", "Цепочка классических проблем",
                          "Chain of classical flaws"),
               items=[
                   ("<b>Versiyalar to'qnashuvi:</b> Sizda Node v20, serverda esa eski Node v16 o'rnatilgan.",
                    "<b>Конфликт версий:</b> У вас Node v20, а на продакшене старый Node v16.",
                    "<b>Version drift:</b> You develop on Node v20, production runs Node v16."),
                   ("<b>OS farqlari:</b> MacOS da ishlaydigan yo'llar (/Users/...) Linux da xato beradi.",
                    "<b>Разница ОС:</b> Пути файлов MacOS (/Users/...) ломаются на Linux сервере.",
                    "<b>OS discrepancies:</b> File paths on MacOS fail on Linux servers."),
                   ("<b>Yetishmayotgan drayverlar:</b> Python yoki C++ bog'lanmalari serverda yo'q.",
                    "<b>Отсутствующие зависимости:</b> Системные бинарники C++ не установлены на сервере.",
                    "<b>Missing native binaries:</b> Python or C++ shared libraries absent on host."),
                   ("<b>Qo'lda sozlash azobi:</b> Yangi dasturchi kelganda muhitni sozlash 2 kun oladi.",
                    "<b>Мучительный онбординг:</b> Настройка рабочего места новичка занимает 2 дня.",
                    "<b>Onboarding agony:</b> Configuring local environments takes new hires 2 full days."),
               ])
         + "\n"
         + box("green", ("Docker yechimi: Konteyner", "Решение Docker: Контейнер", "Docker solution: Container"),
               items=[
                   ("<b>Yagona standart paket:</b> Kod + Runtime + Kutubxonalar birga muzlatiladi.",
                    "<b>Единый пакет:</b> Код + Среда выполнения + Библиотеки упакованы вместе.",
                    "<b>Unified artifact:</b> Code + Runtime + Dependencies sealed in one bundle."),
                   ("<b>Izolyatsiya:</b> Tizimda nima o'rnatilganidan qat'i nazar, konteyner ichi toza.",
                    "<b>Изоляция:</b> Что бы ни стояло на хосте, внутри контейнера стерильная среда.",
                    "<b>Strict isolation:</b> Clean runtime independent of host machine state."),
                   ("<b>Bir soniyada start:</b> `docker run` buyrug'i tizimni millisekundlarda ko'taradi.",
                    "<b>Старт за секунду:</b> Команда `docker run` запускает приложение за миллисекунды.",
                    "<b>Sub-second boot:</b> `docker run` boots production instances in milliseconds."),
                   ("<b>Ishonch:</b> Kompyuteringizda qanday ishlagan bo'lsa, AWS va DigitalOcean'da ham 100% xuddi shunday ishlaydi.",
                    "<b>Надёжность:</b> Работает на AWS и DigitalOcean точно так же, как на вашем ноутбуке.",
                    "<b>Determinism:</b> Runs bit-for-bit identically on your laptop and cloud servers."),
               ])
         + "\n</div>",
))

# 3. VM vs Container Architecture
S.append(slide(
    ph=("Arxitektura", "Архитектура", "Architecture"), time="6–10",
    eyebrow=("Ichki mexanizm", "Внутренний механизм", "Internal mechanics"),
    title=("Virtual Mashina (VM) va Konteyner Farqi",
           "Разница Между Виртуальной Машиной и Контейнером",
           "Virtual Machines vs Containers"),
    body='<div class="cols c2">\n'
         + box("purple", ("Virtual Mashina (Og'ir & Sekin)", "Виртуальная Машина (Тяжёлая)", "Virtual Machine (Heavyweight)"),
               items=[
                   ("<b>Hypervisor qatlami:</b> Har bir VM alohida to'liq Guest OS (Ubuntu/Windows) yuklaydi.",
                    "<b>Слой Hypervisor:</b> Каждая ВМ запускает собственную полноценную ОС.",
                    "<b>Hypervisor overhead:</b> Each VM boots an entire independent Guest OS kernel."),
                   ("<b>Hajmi:</b> Bitta VM bir necha gigabayt (3–10 GB) diskni egallaydi.",
                    "<b>Размер:</b> Каждая ВМ весит гигабайты (3–10 GB) дискового пространства.",
                    "<b>Storage bloat:</b> Weighs several gigabytes (3–10 GB disk footprint)."),
                   ("<b>Vaqt:</b> Ishga tushishi 1–3 daqiqa vaqt oladi (BIOS, bootloader).",
                    "<b>Запуск:</b> Загрузка операционной системы занимает 1–3 минуты.",
                    "<b>Boot latency:</b> Takes 1–3 minutes to initialize kernel and daemons."),
               ])
         + "\n"
         + box("green", ("Docker Konteyner (Yengil & Yashin)", "Docker Контейнер (Лёгкий и Быстрый)", "Docker Container (Light & Fast)"),
               items=[
                   ("<b>Umumiy Linux Yadrosi:</b> Host OS yadrosini (Kernel) ulashadi (Namespaces & Cgroups).",
                    "<b>Общее ядро Linux:</b> Контейнеры делят общее ядро хоста (Namespaces и Cgroups).",
                    "<b>Shared OS Kernel:</b> Shares host Linux kernel via namespaces and cgroups."),
                   ("<b>Hajmi:</b> Faqat kerakli fayllar — 50–150 MB (Alpine bilan atigi 15 MB!).",
                    "<b>Размер:</b> Только файлы приложения — 50–150 MB (на Alpine всего 15 MB!).",
                    "<b>Compact size:</b> Only runtime binaries — 50–150 MB (Alpine down to 15 MB)."),
                   ("<b>Tezlik:</b> Oddiy operatsion tizim jarayoni (process) kabi 0.2 soniyada start oladi.",
                    "<b>Скорость:</b> Запускается как обычный процесс за доли секунды.",
                    "<b>Instant start:</b> Launches as an isolated system process in sub-second time."),
               ])
         + "\n</div>",
))

# 4. The Docker Trinity: Dockerfile, Image, Container
S.append(slide(
    ph=("Konsepsiya", "Концепция", "Core concept"), time="10–14",
    eyebrow=("Asosiy terminologiya", "Ключевые термины", "Core terminology"),
    title=("Docker Uchligi: Dockerfile → Image → Container",
           "Троица Docker: Dockerfile → Image → Container",
           "The Docker Trinity: Dockerfile → Image → Container"),
    body='<div class="cols c3">\n'
         + box("purple", ("1. Dockerfile (Retsept)", "1. Dockerfile (Рецепт)", "1. Dockerfile (Recipe)"),
               p=("Matnli ko'rsatmalar to'plami. Tizim qanday yig'ilishi kerakligini qadamma-qadam ta'riflaydi.",
                  "Текстовый файл инструкций. Пошагово описывает, как собрать изолированную среду.",
                  "Textual instructions defining how the operating environment is built step by step."))
         + "\n"
         + box("accent", ("2. Image (Qolip / Surat)", "2. Image (Образ / Слепок)", "2. Image (Immutable Snapshot)"),
               p=("Muzlatilgan, o'zgarmas (immutable) fayllar to'plami. Dastur kodi va barcha kutubxonalar arxivi.",
                  "Замороженный неизменяемый снимок файловой системы. Код программы и все зависимости.",
                  "Immutable read-only snapshot containing the app code, binaries, and system libraries."))
         + "\n"
         + box("green", ("3. Container (Tirik Jarayon)", "3. Container (Живой Процесс)", "3. Container (Live Process)"),
               p=("Imagedan tug'ilgan faol, ishlayotgan virtual muhit. Uni to'xtatish, o'chirish va ko'paytirish mumkin.",
                  "Запущенный экземпляр образа. Живой изолированный процесс, который можно масштабировать.",
                  "Running instance instantiated from an Image. Isolated sandbox that can be scaled."))
         + "\n</div>"
         + '<div class="callout" style="margin-top:16px;">\n'
         + el("p", "<b>Metafora:</b> Dockerfile — bu tort retsepti. Image — bu pishirib muzlatilgan tayyor tort. Container — bu mehmonlarga tortilgan tirik porsiya!",
                   "<b>Метафора:</b> Dockerfile — рецепт торта. Image — готовый замороженный торт. Container — отрезанный кусок на столе гостя!",
                   "<b>Metaphor:</b> Dockerfile is the recipe. Image is the baked frozen cake. Container is the live serving on the table!")
         + "\n</div>",
))

# 5. Dockerfile Anatomy
S.append(slide(
    ph=("Sintaksis", "Синтаксис", "Syntax"), time="14–18",
    eyebrow=("Direktivalar", "Директивы", "Directives"),
    title=("Dockerfile Anatomiyasi: Node.js Veb-Xizmati",
           "Анатомия Dockerfile: Веб-Сервис Node.js",
           "Dockerfile Anatomy: Node.js Web Service"),
    body='<div class="cols c2">\n'
         + code("""# 1. Baza qatlami (Rasmiy yengil Node)
FROM node:20-alpine

# 2. Konteyner ichidagi ishchi papka
WORKDIR /app

# 3. Avval faqat bog'liqliklar faylini olamiz (Kesh uchun!)
COPY package*.json ./
RUN npm install --omit=dev

# 4. Asosiy dastur kodini nusxalaymiz
COPY . .

# 5. Konteyner qaysi portda tinglashini bildiramiz
EXPOSE 3000

# 6. Konteyner yoqilganda nima ishga tushsin?
CMD ["node", "server.js"]""")
         + "\n"
         + box("accent", ("6 Ta Asosiy Buyruq", "6 Главных Команд", "6 Essential Directives"),
               items=[
                   ("<b>FROM:</b> Baza sifatida rasmiy xavfsiz image (masalan: `node:20-alpine`, `python:3.11-slim`).",
                    "<b>FROM:</b> Базовый официальный образ (`node:20-alpine`, `python:3.11-slim`).",
                    "<b>FROM:</b> Official base image (`node:20-alpine`, `python:3.11-slim`)."),
                   ("<b>WORKDIR:</b> Konteyner ichida barcha buyruqlar bajariladigan asosiy yo'l.",
                    "<b>WORKDIR:</b> Рабочая директория внутри контейнера для всех последующих команд.",
                    "<b>WORKDIR:</b> Dedicated working directory inside container filesystem."),
                   ("<b>COPY:</b> Kompyuteringizdagi fayllarni konteyner ichiga o'tkazish.",
                    "<b>COPY:</b> Копирование файлов с хоста внутрь контейнера.",
                    "<b>COPY:</b> Copies files from host filesystem into container."),
                   ("<b>RUN:</b> Image qurilayotgan paytda buyruqlarni bajarish (`npm install`, `apt-get`).",
                    "<b>RUN:</b> Выполнение команд на этапе сборки (`npm install`, сборка assets).",
                    "<b>RUN:</b> Executes build-time commands (`npm install`, compilers)."),
                   ("<b>EXPOSE:</b> Tarmoq portini hujjatlashtirish (masalan: 3000 yoki 8080).",
                    "<b>EXPOSE:</b> Декларация сетевого порта сервиса.",
                    "<b>EXPOSE:</b> Informs Docker which network port is listened on."),
                   ("<b>CMD:</b> Konteyner start olganda ishga tushadigan birlamchi buyruq.",
                    "<b>CMD:</b> Финальная команда при запуске контейнера.",
                    "<b>CMD:</b> Runtime command executed when container spins up."),
               ])
         + "\n</div>",
))

# 6. Layer Caching
S.append(slide(
    ph=("Optimizatsiya", "Оптимизация", "Optimization"), time="18–22",
    eyebrow=("Tezlik siri", "Секрет скорости", "Build performance"),
    title=("Qatlamlar Keshi (Layer Caching): 10x Tezkor Build",
           "Кэширование Слоёв: Сборка в 10 Раз Быстрее",
           "Layer Caching: 10x Faster Builds"),
    body='<div class="cols c2">\n'
         + box("accent", ("❌ Xato Tartib (Har safar qayta yuklaydi)", "❌ Плохой порядок (Качает заново)", "❌ Bad Order (Redownloads every time)"),
               items=[
                   ("`COPY . .` avval yozilsa, koddagi bitta nuqta o'zgarsa ham butun kesh buziladi.",
                    "Если скопировать весь код в начале, любая точка в коде сбросит весь кэш.",
                    "Copying all code first busts the entire build cache on any single character change."),
                   ("Natijada `RUN npm install` har buildda 5 daqiqa internetdan kutubxona tortadi!",
                    "В итоге `RUN npm install` заново выкачивает сотни мегабайт каждый раз.",
                    "Forces `RUN npm install` to redownload 300MB of dependencies on every save."),
               ])
         + "\n"
         + box("green", ("✅ To'g'ri Tartib (Professional Usul)", "✅ Грамотный порядок (Кэш работает)", "✅ Optimal Order (Cache hit)"),
               items=[
                   ("1. Avval faqat `package.json` nusxalanadi va `npm install` qilinadi.",
                    "1. Сначала копируется только `package.json` и запускается `npm install`.",
                    "1. Copy `package.json` first and execute `npm install`."),
                   ("2. Yangi kutubxona qo'shilmaguncha bu qatlam <b>0.0 soniyada</b> keshdan olinadi!",
                    "2. Пока зависимости не менялись, этот слой берётся из кэша за <b>0 секунд</b>.",
                    "2. Until package.json changes, this layer resolves from cache in <b>0.0s</b>."),
                   ("3. Shundan keyin `COPY . .` qilinadi — kod o'zgarsa faqat oxirgi qatlam yangilanadi.",
                    "3. Лишь затем копируется исходный код — сборка занимает меньше 1 секунды!",
                    "3. Only then copy application source code — builds finish in under 1 second!"),
               ])
         + "\n</div>",
))

# 7. CLI Commands
S.append(slide(
    ph=("Terminal", "Терминал", "Terminal"), time="22–26",
    eyebrow=("DevOps asboblari", "Инструменты DevOps", "DevOps toolkit"),
    title=("Asosiy Docker Buyruqlari: Terminalda Boshqarish",
           "Главные Команды Docker: Управление в Терминале",
           "Essential Docker CLI Commands"),
    body='<div class="cols c2">\n'
         + box("purple", ("Yig\'ish va Ishga Tushirish", "Сборка и Запуск", "Build & Run"),
               items=[
                   ("`docker build -t target-app .` — joriy papkadan `target-app` nomli image yasash.",
                    "`docker build -t target-app .` — собрать образ `target-app` из текущей папки.",
                    "`docker build -t target-app .` — build image named `target-app` from current dir."),
                   ("`docker run -d -p 8080:3000 --name web target-app` — orqa fonda (-d) port bilan yoqish.",
                    "`docker run -d -p 8080:3000 --name web target-app` — запустить в фоне с пробросом порта.",
                    "`docker run -d -p 8080:3000 --name web target-app` — run in background detached with port map."),
               ])
         + "\n"
         + box("accent", ("Monitoring va Tozalash", "Мониторинг и Очистка", "Inspect & Cleanup"),
               items=[
                   ("`docker ps` — hozir ishlab turgan faol konteynerlarni ko'rish.",
                    "`docker ps` — список активных работающих контейнеров.",
                    "`docker ps` — list currently active running containers."),
                   ("`docker logs -f web` — konteyner konsoliga tushayotgan jonli loglarni kuzatish.",
                    "`docker logs -f web` — просмотр живого потока логов сервиса.",
                    "`docker logs -f web` — stream live stdout/stderr console logs."),
                   ("`docker stop web && docker rm web` — konteynerni to'xtatish va xotiradan tozalash.",
                    "`docker stop web && docker rm web` — остановить и удалить контейнер.",
                    "`docker stop web && docker rm web` — gracefully stop and purge container instance."),
               ])
         + "\n</div>",
))

# 8. Port Mapping Demystified
S.append(slide(
    ph=("Tarmoq", "Сеть", "Networking"), time="26–29",
    eyebrow=("Portlar arxitekturasi", "Архитектура портов", "Port mapping mechanics"),
    title=("Port Mapping: -p 8080:3000 Qanday Ishlaydi?",
           "Port Mapping: Как Работает Флаг -p 8080:3000?",
           "Port Mapping: Demystifying -p 8080:3000"),
    body='<div class="cols c2">\n'
         + box("accent", ("Host Port (Sizning Kompyuteringiz)", "Host Port (Ваш Компьютер)", "Host Port (Your Machine)"),
               items=[
                   ("`-p [HOST_PORT]:[CONTAINER_PORT]` — birinchi raqam kompyuteringiz porti.",
                    "`-p [HOST_PORT]:[CONTAINER_PORT]` — первое число — порт вашего компьютера.",
                    "`-p [HOST_PORT]:[CONTAINER_PORT]` — first parameter represents host machine port."),
                   ("Brauzerda `http://localhost:8080` deb ochasiz.",
                    "В браузере вы открываете `http://localhost:8080`.",
                    "In your browser you visit `http://localhost:8080`."),
                   ("Bitta kompyuterda turli portlarda (8081, 8082, 8083) o'nlab konteynerlarni parallel yoqish mumkin!",
                    "На одном сервере можно запустить 10 одинаковых контейнеров на разных портах!",
                    "You can run dozens of parallel container replicas across ports 8081, 8082, 8083!"),
               ])
         + "\n"
         + box("green", ("Container Port (Konteyner Ichi)", "Container Port (Внутри Контейнера)", "Container Port (Internal)"),
               items=[
                   ("Konteyner ichidagi Node.js `app.listen(3000)` portida kutib turadi.",
                    "Внутри контейнера Node.js слушает порт `app.listen(3000)`.",
                    "Node.js server binds internally to `app.listen(3000)`."),
                   ("Docker drayveri 8080 ga kelgan barcha internet trafikni avtomatik 3000 ga yo'naltiradi.",
                    "Docker автоматически перенаправляет внешний трафик с 8080 внутрь на 3000.",
                    "Docker virtual network bridge forwards all traffic on 8080 to container 3000."),
               ])
         + "\n</div>",
))

# 9. Security & .dockerignore
S.append(slide(
    ph=("Xavfsizlik", "Безопасность", "Security"), time="29–33",
    eyebrow=("Kiberxavfsizlik qoidasi", "Правило кибербезопасности", "Production security rule"),
    title=(".dockerignore va Konteyner Xavfsizligi",
           ".dockerignore и Безопасность Контейнеров",
           ".dockerignore & Container Hardening"),
    body='<div class="cols c2">\n'
         + code("""# .dockerignore fayli
node_modules
npm-debug.log
.git
.gitignore
.env
Dockerfile
README.md
tests""")
         + "\n"
         + box("accent", ("Kritik 3 Xavfsizlik Qoidasi", "3 Критических Правила Безопасности", "3 Critical Hardening Rules"),
               items=[
                   ("<b>Hech qachon `.env` ni image ichiga solmang:</b> Maxfiy API kalitlar va parollar ochiq qoladi!",
                    "<b>Никогда не копируйте `.env`:</b> Секреты и пароли базы утекли бы внутрь образа!",
                    "<b>Never bake `.env` into image:</b> Secrets and passwords would leak inside image layers!"),
                   ("<b>Lokal `node_modules` ni chetlab o'ting:</b> Mac/Windows da yig'ilgan kutubxonalar Linux da qulaydi.",
                    "<b>Игнорируйте локальные `node_modules`:</b> Бинарники Mac сломают сборку на Linux.",
                    "<b>Ignore local `node_modules`:</b> Host architecture binaries break inside Linux containers."),
                   ("<b>Root huquqi bilan ishlatmang:</b> `USER node` direktivasini qo'shib, xakerlik xavfini pasaytiring.",
                    "<b>Не запускайте под root:</b> Директива `USER node` защищает сервер от взлома.",
                    "<b>Enforce non-root execution:</b> Use `USER node` to prevent container breakout exploits."),
               ])
         + "\n</div>",
))

# 10. Practical Lab
S.append(slide(
    ph=("Amaliyot", "Практика", "Hands-on Lab"), time="33–41",
    eyebrow=("12 daqiqalik missiya", "12-минутная миссия", "12-minute mission"),
    title=("Amaliy Vazifa: O'z Loyihangizni Dockerize Qiling",
           "Практика: Упакуйте Свой Проект в Docker",
           "Hands-on Lab: Dockerize Your Web Application"),
    body='<div class="cols c2">\n'
         + box("green", ("Vazifa Bosqichlari", "Шаги Задания", "Mission Checklist"),
               items=[
                   ("1. Loyihangiz papkasida `.dockerignore` faylini yarating va `node_modules`, `.env` ni kiriting.",
                    "1. Создайте `.dockerignore` и добавьте `node_modules`, `.env`.",
                    "1. Create `.dockerignore` and exclude `node_modules` and `.env`."),
                   ("2. Ko'p qatlamli toza `Dockerfile` yozing (Node:20-alpine bazasida).",
                    "2. Напишите чистый `Dockerfile` на базе Node:20-alpine.",
                    "2. Author clean production `Dockerfile` based on Node:20-alpine."),
                   ("3. Terminalda `docker build -t my-cyber-app .` buyrug'i bilan imagini quring.",
                    "3. Соберите образ командой `docker build -t my-cyber-app .`.",
                    "3. Compile image via `docker build -t my-cyber-app .`."),
                   ("4. Konteynerni `docker run -d -p 5000:3000 my-cyber-app` qilib ishga tushiring.",
                    "4. Запустите контейнер командой `docker run -d -p 5000:3000 my-cyber-app`.",
                    "4. Boot container detached via `docker run -d -p 5000:3000 my-cyber-app`."),
                   ("5. Brauzerda `localhost:5000` ga kirib, saytingiz ishlab turganini isbotlang!",
                    "5. Откройте `localhost:5000` в браузере и подтвердите работоспособность сервиса!",
                    "5. Open `localhost:5000` in browser and confirm live operational status!"),
               ])
         + "\n"
         + box("purple", ("Taymer va Natija", "Таймер и Результат", "Timer & Deliverable"),
               p=("Vaqt: 12 daqiqa. Ishchi varaqangizga `docker ps` buyrug'ining chiqish natijasini va Container ID raqamini yozing.",
                  "Время: 12 минут. Запишите в рабочий лист вывод команды `docker ps` и Container ID.",
                  "Time: 12 minutes. Record `docker ps` output and Container ID in your worksheet."),
               extra_html='<div class="timer" id="timer" style="margin-top:12px; font-size:28px; font-family:\'JetBrains Mono\',monospace; font-weight:700; color:var(--accent);">12:00</div>')
         + "\n</div>",
))

# 11. Multi-Stage Builds (Senior Level)
S.append(slide(
    ph=("Ilg'or", "Продвинутый", "Advanced"), time="41–43",
    eyebrow=("Senior muhandislik siri", "Секрет Senior инженера", "Senior engineering secret"),
    title=("Multi-Stage Build: 1 GB dan 25 MB gacha Qisqartirish",
           "Multi-Stage Build: Сокращение с 1 GB до 25 MB",
           "Multi-Stage Builds: Slimming 1GB Down to 25MB"),
    body='<div class="cols c2">\n'
         + code("""# 1-bosqich: Yig'uvchi (Builder)
FROM node:20 AS builder
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build # TypeScript / React yig'ish

# 2-bosqich: Toza Production (Runner)
FROM node:20-alpine AS runner
WORKDIR /app
COPY --from=builder /app/dist ./dist
COPY --from=builder /app/package*.json ./
RUN npm install --omit=dev
USER node
CMD ["node", "dist/main.js"]""")
         + "\n"
         + box("accent", ("Nega Bu Muhim?", "Почему Это Критично?", "Why This Matters"),
               items=[
                   ("<b>Nol ortiqcha axlat:</b> TypeScript kompilyatori va test kutubxonalari production imagega tushmaydi.",
                    "<b>Ноль мусора:</b> Компиляторы TypeScript и dev-зависимости не попадают в прод.",
                    "<b>Zero runtime cruft:</b> Heavy TypeScript compilers and devtools stay out of production."),
                   ("<b>Xavfsizlik:</b> Konteyner qancha kichik bo'lsa, xakerlar buzishi mumkin bo'lgan zaifliklar (CVE) shuncha kam bo'ladi.",
                    "<b>Безопасность:</b> Чем меньше образ, тем меньше потенциальных уязвимостей (CVE).",
                    "<b>Minimal attack surface:</b> Smaller attack surface drastically slashes CVE count."),
                   ("<b>Tezkor deploy:</b> 25 MB li image serverga 2 soniyada yuklanadi, 1 GB esa 3 daqiqa kutdiradi.",
                    "<b>Скорость:</b> Образ 25 MB скачивается за секунды, а 1 GB грузится минуты.",
                    "<b>Lightning rollouts:</b> 25MB pulls in 2 seconds instead of waiting minutes for 1GB."),
               ])
         + "\n</div>",
))

# 12. Summary & Rubric
S.append(slide(
    ph=("Xulosa", "Итоги", "Summary"), time="43–45",
    eyebrow=("Baholash mezonlari", "Критерии оценки", "Grading rubric"),
    title=("Xulosa va 10 Ballik Baholash Mezoni",
           "Итоги и 10-Балльная Шкала Оценивания",
           "Summary & 10-Point Evaluation Rubric"),
    body='<div class="cols c2">\n'
         + box("purple", ("Bugun O'rgangalarimiz", "Что Мы Узнали Сегодня", "Key Takeaways"),
               items=[
                   ("Konteyner — host Linux yadrosini ulashuvchi yengil, izolyatsiyalangan jarayondir.",
                    "Контейнер — изолированный легковесный процесс, разделяющий ядро хоста.",
                    "Containers are lightweight isolated processes sharing the host OS kernel."),
                   ("Dockerfile — retsept, Image — qolip, Container — tirik ishlayotgan nusxa.",
                    "Dockerfile — рецепт, Image — снимок, Container — живой экземпляр.",
                    "Dockerfile is the recipe, Image is the blueprint, Container is the live instance."),
                   ("Qatlamlar keshi va `.dockerignore` build vaqtini 90% ga qisqartiradi.",
                    "Кэш слоёв и `.dockerignore` экономят до 90% времени сборки.",
                    "Layer caching and `.dockerignore` reduce build durations by 90%."),
                   ("Port mapping (`-p 8080:3000`) xost va konteyner tarmoqlarini bog'laydi.",
                    "Проброс портов связывает внешнюю сеть хоста с приложением внутри.",
                    "Port mapping bridges external host traffic to internal container sockets."),
               ])
         + "\n"
         + box("accent", ("10 Ballik Mezon", "10-Балльная Шкала", "10-Point Rubric"),
               items=[
                   ("<b>2 ball:</b> VM va Konteyner farqini tushuntirish va .dockerignore tuzish.",
                    "<b>2 балла:</b> Объяснение разницы VM/Контейнер и создание .dockerignore.",
                    "<b>2 pts:</b> Explaining VM vs Container differences and authoring .dockerignore."),
                   ("<b>3 ball:</b> To'g'ri qatlamli, xatosiz `Dockerfile` yozish.",
                    "<b>3 балла:</b> Грамотный, кэшируемый `Dockerfile` без лишних слоёв.",
                    "<b>3 pts:</b> Writing correct, layer-cached `Dockerfile` with proper syntax."),
                   ("<b>3 ball:</b> `docker build` va `docker run` orqali portni muvaffaqiyatli bog'lash.",
                    "<b>3 балла:</b> Успешная сборка и запуск контейнера с пробросом порта.",
                    "<b>3 pts:</b> Successful build and execution with verified port mapping."),
                   ("<b>2 ball:</b> Multi-stage build mohiyatini va xavfsizlik qoidalarini asoslash.",
                    "<b>2 балла:</b> Понимание multi-stage сборки и запуска от non-root пользователя.",
                    "<b>2 pts:</b> Articulating multi-stage build rationale and non-root execution."),
               ])
         + "\n</div>",
))

# ----------------- TEACHER NOTES -----------------
NOTES = {
    "uz": [
        ["Kirish va Maqsad", "Senior sinfga 'works on my machine' muammosi nima uchun qimmatga tushishini tushuntiring.", "1-slaydni oching. Dasturchilar va DevOps muhandislari farqini ayting."],
        ["Muammo tahlili", "O'quvchilardan so'rang: Boshqa birovning kodini ishga tushirishda qanday xatolar chiqqan?", "Muhit farqlari haqida fikr almashing."],
        ["VM vs Konteyner", "Hypervisor va Shared Kernel farqini doskaga chizing. Nega Docker engil ekanini ko'rsating.", "Namespaces va Cgroups terminlarini aytib o'ting."],
        ["Docker Uchligi", "Retsept, qolip va tirik nusxa metaforasini bering.", "Dockerfile, Image va Container so'zlarini xotirada mustahkamlang."],
        ["Dockerfile Anatomiyasi", "Har bir direktivani (FROM, WORKDIR, COPY, RUN, EXPOSE, CMD) ko'rsating.", "Nega CMD massiv shaklida yozilishini ayting."],
        ["Qatlamlar keshi", "Kesh mexanizmini tushuntiring. Nega package.json avval nusxalanishini ko'rsating.", "Vaqt tejashni soniyalarda hisoblab bering."],
        ["CLI Buyruqlari", "docker build, run, ps, logs buyruqlarini terminalda ko'rsating.", "Flaglar ma'nosini (-d, -p, --name) tushuntiring."],
        ["Port Mapping", "Host port va Container port farqini chizib bering.", "Nega 8080:3000 ekanini, ikkala taraf boshqa bo'lishi mumkinligini ayting."],
        [".dockerignore", "Maxfiy fayllar (.env) konteyner ichiga kirib ketmasligi kerakligini ogohlantiring.", "Kiberxavfsizlik qoidalarini ta'kidlang."],
        ["Amaliy topshiriq", "12 daqiqalik taymerni yoqing. O'quvchilar stollarini aylanib chiqing.", "Port to'qnashuvi (port already in use) xatolarini tuzatishga yordam bering."],
        ["Multi-Stage Build", "Professional production standarti. 1GB dan 25MB ga qanday tushishini ko'rsating.", "Builder va Runner bosqichlarini ajrating."],
        ["Xulosa va Baholash", "O'quvchilar javoblarini tekshirib, 10 ballik mezon bo'yicha baholang.", "Ishchi varaqalarni yig'ib oling."]
    ],
    "ru": [
        ["Введение и Цель", "Объясните старшеклассникам цену проблемы «на моём компьютере работало».", "Откройте 1-й слайд. Сравните разработчиков и DevOps-инженеров."],
        ["Анализ проблемы", "Спросите учеников: с какими ошибками они сталкивались при запуске чужого кода?", "Обсудите несовместимость версий и путей."],
        ["ВМ vs Контейнер", "Нарисуйте разницу между Hypervisor и общим ядром Linux на доске.", "Объясните термины Namespaces и Cgroups."],
        ["Троица Docker", "Используйте метафору рецепта, замороженного торта и порции.", "Закрепите понятия Dockerfile, Image и Container."],
        ["Анатомия Dockerfile", "Разберите каждую инструкцию (FROM, WORKDIR, COPY, RUN, EXPOSE, CMD).", "Объясните формат JSON-массива в CMD."],
        ["Кэширование слоёв", "Покажите, почему package.json должен копироваться ДО остального кода.", "Продемонстрируйте экономию времени."],
        ["Команды CLI", "Покажите в терминале команды docker build, run, ps, logs.", "Разберите флаги -d, -p, --name."],
        ["Проброс портов", "Наглядно покажите хост-порт и порт внутри контейнера.", "Объясните, почему порты могут различаться (8080:3000)."],
        [".dockerignore", "Предупредите об опасности попадания .env файлов внутрь образов.", "Напомните правила кибергигиены."],
        ["Практикум", "Запустите 12-минутный таймер. Пройдитесь по классу.", "Помогите с ошибками занятых портов."],
        ["Multi-Stage сборка", "Покажите стандарт продакшена: сокращение размера с 1 GB до 25 MB.", "Объясните разделение на Builder и Runner."],
        ["Итоги и Оценка", "Проверьте вывод docker ps и оцените работы по 10-балльной шкале.", "Соберите заполненные листы."]
    ],
    "en": [
        ["Intro & Objectives", "Highlight the catastrophic cost of the 'works on my machine' fallacy in enterprise tech.", "Open slide 1. Frame the shift to reproducible DevOps systems."],
        ["Problem Anatomy", "Ask students about friction when cloning unfamiliar repositories.", "Analyze runtime discrepancies and native library mismatches."],
        ["VM vs Container", "Illustrate Hypervisors with Guest OS versus shared Linux kernel namespaces and cgroups.", "Explain the kernel virtualization mechanism."],
        ["The Docker Trinity", "Deploy the recipe, frozen cake, and live slice metaphor.", "Reinforce Dockerfile, Image, and Container mental models."],
        ["Dockerfile Directives", "Dissect FROM, WORKDIR, COPY, RUN, EXPOSE, and CMD line by line.", "Clarify exec form JSON syntax for CMD."],
        ["Layer Caching", "Demonstrate why dependency manifests must be isolated prior to full code copies.", "Calculate bandwidth and compilation time savings."],
        ["Docker CLI", "Execute docker build, run, ps, and logs in the interactive console.", "Clarify detached mode (-d) and named instances (--name)."],
        ["Port Forwarding", "Map host socket binding to internal container listening sockets.", "Demonstrate running multi-container replicas on arbitrary ports."],
        [".dockerignore", "Warn against credential leakage by baking .env files into immutable layers.", "Emphasize supply chain security principles."],
        ["Hands-on Mission", "Engage the 12-minute countdown timer. Assist students at workstations.", "Debug port collision and daemon socket errors."],
        ["Multi-Stage Builds", "Present production enterprise patterns: pruning bloat from 1GB to 25MB.", "Differentiate build environment tools from lean runner images."],
        ["Rubric Evaluation", "Audit student container telemetry and grade against the 10-point rubric.", "Collect physical worksheets."]
    ]
}

# ----------------- WORKSHEET (VARAQA) -----------------
VARAQA = (
    sheet_header(
        ("17-dars. Docker va Konteynerlar: Tizimlararo Moslik Kafolati",
         "Урок 17. Docker и Контейнеры: Гарантия Совместимости Систем",
         "Lesson 17. Docker & Containers: Cross-System Determinism"),
        ("9-sinf · 4-hafta (1-soat) · DevOps & Server Arxitekturasi",
         "9 класс · 4-неделя (1-й час) · DevOps и Архитектура Серверов",
         "Grade 9 · Week 4 (Hour 1) · DevOps & Server Architecture")
    )
    + "\n"
    + mission(
        ("Amaliy Missiya: Veb-Xizmat Uchun Dockerfile Yozish va Port Bog'lash",
         "Практическая Миссия: Написание Dockerfile и Проброс Портов",
         "Hands-on Mission: Writing a Dockerfile and Establishing Port Forwarding"),
        ("1. `.dockerignore` faylini yarating va keraksiz fayllarni chetlab o'ting.\n"
         "2. Node:20-alpine asosida keshni hisobga olgan toza `Dockerfile` yozing.\n"
         "3. `docker build -t cyber-service .` buyrug'i bilan imagini quring.\n"
         "4. Konteynerni `-p 8080:3000` port mapping bilan fonda ishga tushiring.\n"
         "5. `docker ps` buyrug'i natijasini jadvalga to'ldiring.",
         "1. Создайте `.dockerignore` и исключите ненужные файлы.\n"
         "2. Напишите `Dockerfile` на базе Node:20-alpine с учётом кэширования.\n"
         "3. Соберите образ командой `docker build -t cyber-service .`.\n"
         "4. Запустите контейнер с флагом `-p 8080:3000` в фоновом режиме.\n"
         "5. Заполните вывод команды `docker ps` в таблицу ниже.",
         "1. Author a `.dockerignore` file excluding non-runtime artifacts.\n"
         "2. Write a layer-cached `Dockerfile` utilizing Node:20-alpine.\n"
         "3. Build the image via `docker build -t cyber-service .`.\n"
         "4. Spin up the container detached with `-p 8080:3000` port mapping.\n"
         "5. Record the `docker ps` telemetry output in the verification table.")
    )
    + "\n"
    + table(
        [("Bosqich", "Этап", "Stage"),
         ("Terminal Buyrug'i", "Команда Терминала", "Terminal Command"),
         ("Kutilgan Natija / Tekshiruv", "Ожидаемый Результат / Проверка", "Expected Telemetry / Check")],
        [
            [("1 · Ignore", "1 · Игнор", "1 · Ignore"),
             ("touch .dockerignore", "touch .dockerignore", "touch .dockerignore"),
             ("Qaysi fayllar kiritildi: _________________________________",
              "Исключённые файлы: _________________________________",
              "Excluded artifacts: _________________________________")],
            [("2 · Build", "2 · Сборка", "2 · Build"),
             ("docker build -t cyber-service .", "docker build -t cyber-service .", "docker build -t cyber-service ."),
             ("Image ID: _________________ · Hajmi (MB): ____________",
              "Image ID: _________________ · Размер (MB): ____________",
              "Image ID: _________________ · Size (MB): ____________")],
            [("3 · Run", "3 · Запуск", "3 · Run"),
             ("docker run -d -p 8080:3000 --name app cyber-service",
              "docker run -d -p 8080:3000 --name app cyber-service",
              "docker run -d -p 8080:3000 --name app cyber-service"),
             ("Container ID (birinchi 12 belgi): ______________________",
              "Container ID (первые 12 символов): ______________________",
              "Container ID (first 12 chars): ______________________")],
            [("4 · Verify", "4 · Проверка", "4 · Verify"),
             ("curl http://localhost:8080 || browser",
              "curl http://localhost:8080 || browser",
              "curl http://localhost:8080 || browser"),
             ("HTTP Status: 200 OK · Sayt ochildimi? [ HA / YO'Q ]",
              "HTTP Status: 200 OK · Сервис открылся? [ ДА / НЕТ ]",
              "HTTP Status: 200 OK · Service reachable? [ YES / NO ]")]
        ]
    )
    + "\n"
    + '    <div class="rubric-grid">\n'
    + sheet_box(
        ("✏️ Muhandislik Hisoboti",
         "✏️ Инженерный Отчёт",
         "✏️ Engineering Report"),
        writelines(2, ("Nega VM o'rniga Konteyner tanlanadi (Asosiy 2 ta farq):",
                       "Почему Контейнеры предпочтительнее ВМ (2 главных отличия):",
                       "Why Containers beat VMs for web workloads (2 key reasons):"))
        + "\n"
        + writelines(2, ("Port mapping `-p 8080:3000` da 8080 nima va 3000 nima:",
                         "Что означает 8080 и что означает 3000 во флаге `-p 8080:3000`:",
                         "Explain host vs container ports in `-p 8080:3000`:"))
        + "\n"
        + writelines(2, ("Nega `.env` faylini Docker image ichiga nusxalash xavfli:",
                         "Почему копирование `.env` внутрь Docker-образа опасно:",
                         "Why baking `.env` into Docker images is a critical vulnerability:"))
    )
    + "\n"
    + sheet_box(
        ("📊 Baholash Mezoni (10 Ball)",
         "📊 Критерии Оценки (10 Баллов)",
         "📊 Grading Rubric (10 Points)"),
        rubric([
            (("VM vs Konteyner va .dockerignore", "ВМ против Контейнера и .dockerignore", "VM vs Container & .dockerignore"), "2"),
            (("To'g'ri qatlamli Dockerfile", "Корректный Dockerfile с кэшем", "Optimized layer-cached Dockerfile"), "3"),
            (("docker build va run (port mapping)", "docker build и запуск с портами", "docker build & run with port map"), "3"),
            (("Multi-stage build va xavfsizlik tahlili", "Анализ Multi-stage и безопасности", "Multi-stage & security reasoning"), "2"),
        ], "10")
    )
    + "\n    </div>\n  </div>\n"
    + sign_box()
)

if __name__ == "__main__":
    print(Lesson(D, TITLES, SHEET_TITLES, "vc-notes-9-17", S, NOTES, VARAQA).build())
