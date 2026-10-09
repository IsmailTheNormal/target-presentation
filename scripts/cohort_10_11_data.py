#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Cohort 10-11-sinf planned weeks (Weeks 6–36) for Target International School.
5 hours/week. Total: 31 weeks * 5 = 155 hours (plus 23 hours in weeks 1-5 = 178 ~ 180 hours).
"""

WEEKS_10_11_PLANNED = {
    6: {
        "title": {"uz": "Cloud Security va DevSecOps", "ru": "Cloud Security и DevSecOps", "en": "Cloud Security and DevSecOps"},
        "type": {"uz": "Kiberxavfsizlik Lab", "ru": "Кибербезопасность Лаб", "en": "CyberSecurity Lab"},
        "skills": {"uz": "AWS/GCP IAM rollari, Terraform xavfsizlik tekshiruvlari, Ochiq S3 chelaklar zaifligi, HashiCorp Vault va Secret Management", "ru": "Роли AWS/GCP IAM, аудит Terraform, открытые S3 бакеты, HashiCorp Vault и управление секретами", "en": "AWS/GCP IAM roles, Terraform security audit, open S3 bucket vulnerabilities, HashiCorp Vault, and secret management"},
        "deliverable": {"uz": "Xavfsiz Terraform infratuzilma skripti va Vault yordamida dinamik token boshqaruvi", "ru": "Безопасный скрипт Terraform и динамическое управление токенами через Vault", "en": "Hardened Terraform infrastructure script and dynamic secret leasing via Vault"},
        "tools": "AWS CLI, Terraform, Trivy, HashiCorp Vault"
    },
    7: {
        "title": {"uz": "Penetration Testing va Ethical Hacking Lab", "ru": "Penetration Testing и Лаборатория Этичного Хакинга", "en": "Penetration Testing and Ethical Hacking Lab"},
        "type": {"uz": "Kiber-Hujum Lab", "ru": "Атака и Пентест Лаб", "en": "Offensive Security Lab"},
        "skills": {"uz": "Burp Suite orqali trafikni tutish, SSRF va IDOR hujumlari, Metasploit ekspluatatsiyasi, Privilege Escalation tamoyillari", "ru": "Перехват трафика через Burp Suite, атаки SSRF и IDOR, эксплойты Metasploit, эскалация привилегий", "en": "Traffic interception with Burp Suite, SSRF and IDOR attacks, Metasploit framework, and privilege escalation vectors"},
        "deliverable": {"uz": "Zaif veb-ilovada 3 ta kritik bo'shliqni fosh etuvchi professional Pentest hisoboti", "ru": "Профессиональный отчет о пентесте с выявлением 3 критических уязвимостей", "en": "Professional penetration testing report documenting 3 high-severity vulnerabilities"},
        "tools": "Burp Suite, OWASP ZAP, Kali Linux Tools, Metasploit"
    },
    8: {
        "title": {"uz": "1-Chorak Oraliq Nazorat: Korporativ Tarmoq Himoyasi va CTF", "ru": "Промежуточный Контроль 1-й Четверти: Защита Сети и CTF", "en": "Quarter 1 Midterm Exam: Enterprise Defense and CTF Challenge"},
        "type": {"uz": "Oraliq Imtihon", "ru": "Промежуточный Экзамен", "en": "Midterm Examination"},
        "skills": {"uz": "Hujum va himoya stsenariylari, Blue Team monitori, Red Team xakerlik amallari, NIST 800-61 bo'yicha hisobot berish", "ru": "Сценарии атаки и защиты, мониторинг Blue Team, действия Red Team, отчетность по NIST 800-61", "en": "Attack/Defense scenarios, Blue Team telemetry, Red Team vectors, and incident response under NIST 800-61"},
        "deliverable": {"uz": "Oraliq nazorat CTF bayroqchalari (Flags) va to'liq texnik tahlil protokoli (10 ballik mezon)", "ru": "Флаги соревнований CTF и полный протокол технического аудита (10-балльная шкала)", "en": "CTF competition challenge flags and formal technical incident debrief (10-point rubric)"},
        "tools": "CTFd Platform, SIEM Console, Wireshark, UFW"
    },
    9: {
        "title": {"uz": "1-Chorak Demo Day: Enterprise Kiber-Mudofaa Arxitekturasi", "ru": "Demo Day 1-й Четверти: Архитектура Корпоративной Киберзащиты", "en": "Quarter 1 Demo Day: Enterprise Cyber Defense Architecture Showcase"},
        "type": {"uz": "Demo Day / Taqdimot", "ru": "Demo Day / Презентация", "en": "Demo Day / Presentation"},
        "skills": {"uz": "Xavfsizlik tizimi taqdimoti, Texnik himoya, Jonli ekspluatatsiyani qaytarish namoyishi, Jamoatchilik oldida nutq", "ru": "Презентация системы безопасности, техническая защита, отражение живой атаки, публичное выступление", "en": "Security architecture pitch, defensive live demo, live exploit mitigation, and public speaking"},
        "deliverable": {"uz": "Maktab yoki virtual kompaniya uchun ishlab chiqilgan to'liq Kiber-Xavfsizlik Konsepsiyasi va sertifikat", "ru": "Концепция кибербезопасности для школы или компании и сертификат 1-й четверти", "en": "Complete Cyber Defense Concept Document for enterprise and Quarter 1 Mastery Certificate"},
        "tools": "Keynote / Slides, Live Infrastructure Demo, GitHub Repo"
    },
    10: {
        "title": {"uz": "AI Agentlar Paradigmasi va ReAct Tsikli", "ru": "Парадигма AI Агентов и Цикл ReAct", "en": "AI Agent Paradigm and ReAct Loop"},
        "type": {"uz": "Agentik AI", "ru": "Агентный AI", "en": "Agentic AI"},
        "skills": {"uz": "Chatbot vs Mustaqil Agent, Fikrlash-Harakat-Kuzatish (Thought-Action-Observation) zanjiri, LangChain va LangGraph asoslari", "ru": "Чат-бот vs Автономный Агент, цепочка Thought-Action-Observation, основы LangChain и LangGraph", "en": "Chatbot vs Autonomous Agent, Thought-Action-Observation loop, LangChain and LangGraph foundations"},
        "deliverable": {"uz": "Mustaqil fikrlab muammoni ketma-ket yechuvchi birinchi avtonom ReAct agent prototipi", "ru": "Первый автономный прототип ReAct-агента, пошагово решающий задачу", "en": "First autonomous ReAct agent prototype executing multi-step reasoning"},
        "tools": "Python, LangChain, OpenAI/Claude API, ReAct Framework"
    },
    11: {
        "title": {"uz": "Agent Vositalari (Tools) va Sandboxing", "ru": "Инструменты Агента (Tools) и Sandboxing", "en": "Agent Tools and Sandboxed Execution"},
        "type": {"uz": "Interaktiv Lab", "ru": "Интерактивная Лаб", "en": "Interactive Lab"},
        "skills": {"uz": "Funksiyalarni agentga ulash, Python Interpreter vositasi, Xavfsiz Docker sandboxing, Havfli buyruqlarni bloklash", "ru": "Подключение инструментов к агенту, Python Interpreter, безопасная песочница Docker, изоляция опасных команд", "en": "Equipping agents with custom tools, Python Interpreter tool, Docker sandboxing, and execution safety boundaries"},
        "deliverable": {"uz": "Matematik va analitik hisob-kitoblarni kod yozib xavfsiz izolyatsiyada bajaruvchi agent", "ru": "Агент, выполняющий расчеты путем написания и запуска кода в изолированной песочнице", "en": "Autonomous agent generating and executing code safely within an isolated sandbox"},
        "tools": "Docker Sandbox, Python exec, Tool Decorators"
    },
    12: {
        "title": {"uz": "Agent Xotirasi: Epizodik, Semantik va Vector Cache", "ru": "Память Агентов: Эпизодическая, Семантическая и Векторный Кэш", "en": "Agent Memory: Episodic, Semantic, and Vector Cache"},
        "type": {"uz": "Interaktiv Lab", "ru": "Интерактивная Лаб", "en": "Interactive Lab"},
        "skills": {"uz": "Qisqa muddatli kontekst oynasi, Doimiy xotira (Long-term memory), SQLite va Vector DB integratsiyasi, Foydalanuvchi preferensiyalari", "ru": "Контекстное окно, долговременная память, интеграция SQLite и Vector DB, сохранение предпочтений пользователя", "en": "Working context window, long-term persistence, SQLite and Vector DB caching, and user preference state machines"},
        "deliverable": {"uz": "O'tmishdagi suhbatlar va xatolarni eslab qoluvchi doimiy xotirali AI muhandis yordamchisi", "ru": "AI-ассистент с долговременной памятью, помнящий предыдущие сессии и ошибки", "en": "AI assistant with persistent episodic memory retaining historical context across restarts"},
        "tools": "ChromaDB, SQLite Memory Store, LangChain Memory"
    },
    13: {
        "title": {"uz": "Avtonom Kod Yozuvchi Agentlar (Autonomous Coding)", "ru": "Автономные Кодовые Агенты (Autonomous Coding)", "en": "Autonomous Coding Agents"},
        "type": {"uz": "Muhandislik Lab", "ru": "Инженерная Лаб", "en": "Engineering Lab"},
        "skills": {"uz": "Cursor Rules, Claude Code CLI, GitHub Copilot Workspace, Testlarga asoslangan rivojlantirish (TDD) agenti", "ru": "Cursor Rules, Claude Code CLI, GitHub Copilot Workspace, разработка через тестирование (TDD) агентом", "en": "Cursor Rules, Claude Code CLI, GitHub Copilot Workspace, autonomous TDD refactoring workflows"},
        "deliverable": {"uz": "Texnik topshiriq bo'yicha mustaqil test yozib, kodni muvaffaqiyatli topshiruvchi kod agenti", "ru": "Агент, самостоятельно пишущий тесты и реализацию по техническому заданию", "en": "Code generation agent writing unit tests and auto-fixing syntax errors until tests pass"},
        "tools": "Cursor IDE, Claude Code CLI, PyTest / Jest"
    },
    14: {
        "title": {"uz": "Multi-Agent Tizimlari: Supervisor va Worker Naqshlari", "ru": "Мультиагентные Системы: Паттерны Supervisor и Worker", "en": "Multi-Agent Systems: Supervisor and Worker Patterns"},
        "type": {"uz": "Murakkab Tizimlar", "ru": "Сложные Системы", "en": "Complex Systems"},
        "skills": {"uz": "Vazifalarni taqsimlovchi boshqaruvchi (Supervisor), Tadqiqotchi agent, Dasturchi agent, Tanqidchi (Critic/Reflector) agent", "ru": "Агент-супервизор, исследователь, программист, критик/рецензент, оркестрация мультиагентных систем", "en": "Supervisor orchestration, specialized worker agents (Researcher, Coder, Critic/Reflector), agent consensus"},
        "deliverable": {"uz": "Bir-biri bilan maslahatlashib murakkab ilova kodini yaratuvchi 3 talik agentlar jamoasi", "ru": "Команда из 3 агентов, создающая комплексное приложение через взаимные консультации", "en": "Autonomous multi-agent squad (Architect, Developer, QA) collaborating on a software feature"},
        "tools": "LangGraph, AutoGen / CrewAI, Python Multi-threading"
    },
    15: {
        "title": {"uz": "Agentik Veb-Brauzing va Headless Scraping", "ru": "Агентный Веб-Браузинг и Headless Scraping", "en": "Agentic Web Browsing and Headless Scraping"},
        "type": {"uz": "Interaktiv Lab", "ru": "Интерактивная Лаб", "en": "Interactive Lab"},
        "skills": {"uz": "Playwright AI, Stagehand, Browser-Use kutubxonasi, DOM daraxtini semantik tahlil qilish, Dinamik saytlardan ma'lumot olish", "ru": "Playwright AI, Stagehand, библиотека Browser-Use, семантический парсинг DOM, сбор данных со сложных сайтов", "en": "Playwright AI, Stagehand, Browser-Use library, semantic DOM compression, autonomous web interaction"},
        "deliverable": {"uz": "Brauzerni mustaqil ochib, narxlarni solishtirib jadval yaratuvchi veb-agent", "ru": "Веб-агент, самостоятельно открывающий браузер, собирающий данные и формирующий отчет", "en": "Autonomous browsing agent navigating websites, solving pagination, and exporting structured JSON"},
        "tools": "Playwright, Browser-Use, Chromium Headless, Stagehand"
    },
    16: {
        "title": {"uz": "Human-in-the-Loop va Agentik Xavfsizlik Guardrails", "ru": "Human-in-the-Loop и Защитные Барьеры (Guardrails) Агентов", "en": "Human-in-the-Loop and Agent Safety Guardrails"},
        "type": {"uz": "Kiberxavfsizlik", "ru": "Кибербезопасность", "en": "CyberSecurity"},
        "skills": {"uz": "Ishonchlilik ko'rsatkichi (Confidence Score), Muhim harakatlar oldidan inson roziligi, Rollback", "ru": "Уровень уверенности (Confidence Score), подтверждение человеком критических действий, откат транзакций", "en": "Confidence scoring thresholds, human approval gates for critical actions (delete, payment), audit trails"},
        "deliverable": {"uz": "Inson nazorati ostida xavfsiz ishlovchi va har bir qarorini audit logiga yozuvchi agent tizimi", "ru": "Безопасная система агентов с обязательным подтверждением человеком и логом аудита", "en": "Fault-tolerant agent workflow with approval gates, rate controls, and tamper-proof audit trails"},
        "tools": "NeMo Guardrails, Human Approval API, SQLite Audit Logger"
    },
    17: {
        "title": {"uz": "2-Chorak Oraliq Nazorat: Avtonom Multi-Agent Tizimi Auditi", "ru": "Промежуточный Контроль 2-й Четверти: Аудит Мультиагентной Системы", "en": "Quarter 2 Midterm Exam: Multi-Agent System Audit"},
        "type": {"uz": "Oraliq Imtihon", "ru": "Промежуточный Экзамен", "en": "Midterm Examination"},
        "skills": {"uz": "Multi-agent zanjirlarini sozlash, Token iste'molini optimallashtirish, Cheksiz sikllardan himoya, Xatolarni tiklash", "ru": "Настройка мультиагентных цепочек, оптимизация токенов, защита от бесконечных циклов, отказоустойчивость", "en": "Multi-agent graph orchestration, token budgeting, circular dependency detection, and error recovery"},
        "deliverable": {"uz": "Berilgan murakkab biznes keysni to'liq mustaqil yechuvchi barqaror agent tizimi kodi (10 ballik mezon)", "ru": "Работающий код устойчивой агентной системы, решающей бизнес-кейс (10-балльная шкала)", "en": "Production-grade multi-agent workflow solving an unconstrained business scenario (10-point rubric)"},
        "tools": "LangGraph CLI, Profiler, Token Counter"
    },
    18: {
        "title": {"uz": "2-Chorak Demo Day: Qishki Agentik AI Hackathoni", "ru": "Demo Day 2-й Четверти: Зимний Хакатон Агентного AI", "en": "Quarter 2 Demo Day: Winter Autonomous Agents Hackathon"},
        "type": {"uz": "Demo Day / Hackathon", "ru": "Demo Day / Хакатон", "en": "Demo Day / Hackathon"},
        "skills": {"uz": "Loyiha himoyasi, Real vaqtda agentlar ishini jonli namoyish qilish, Savol-javob, Jamoaviy taqdimot", "ru": "Защита проекта, живая демонстрация работы агентов в реальном времени, ответы на вопросы, командный питч", "en": "Live demonstration of autonomous agents, resilience under edge cases, technical defense, and showcase"},
        "deliverable": {"uz": "Sinfdoshlar va hakamlar oldida himoya qilingan to'liq ishchi Avtonom AI Agent mahsuloti", "ru": "Готовый рабочий продукт на базе AI агентов, защищенный перед жюри и сертификат", "en": "Fully functional autonomous AI agent product presented live, plus Quarter 2 Diploma"},
        "tools": "Live Demo Rig, Pitch Deck, Open Source Repository"
    },
    19: {
        "title": {"uz": "Avtomatlashtirish Asoslari va n8n Dvigateli", "ru": "Основы Автоматизации и Движок n8n", "en": "Automation Fundamentals and n8n Workflow Engine"},
        "type": {"uz": "Avtomatlashtirish", "ru": "Автоматизация", "en": "Automation"},
        "skills": {"uz": "Raqamli ish oqimlari (Workflows), Trigger va Action tushunchasi, Webhooklar, Docker orqali n8n serverini ishga tushirish", "ru": "Цифровые рабочие процессы, триггеры и действия, вебхуки, запуск сервера n8n через Docker", "en": "Workflow orchestration, Triggers and Actions, Webhook lifecycles, hosting local n8n via Docker"},
        "deliverable": {"uz": "Mahalliy serverda ishga tushirilgan n8n va birinchi avtomatik Webhook-to-Telegram oqimi", "ru": "Локальный сервер n8n и первый рабочий поток Webhook-to-Telegram", "en": "Self-hosted n8n instance and deployed Webhook-to-Telegram real-time notification workflow"},
        "tools": "Docker, n8n Self-Hosted, Telegram Bot API, Postman"
    },
    20: {
        "title": {"uz": "n8n Nodlari, JSON Ma'lumotlar Oqimi va Filtrlash", "ru": "Узлы n8n, Поток Данных JSON и Фильтрация", "en": "n8n Node Architecture, JSON Data Streams, and Filtering"},
        "type": {"uz": "Amaliy Lab", "ru": "Практическая Лаб", "en": "Hands-on Lab"},
        "skills": {"uz": "Node arxitekturasi, JSON ma'lumotlar massivlarini qayta ishlash, Shartli tarmoqlanish (IF/Switch), Ma'lumotlarni o'zgartirish (Set Node)", "ru": "Архитектура узлов, обработка массивов JSON, условное ветвление (IF/Switch), трансформация данных (Set)", "en": "Node pipelines, JSON array manipulation, branching logic (IF/Switch nodes), data mutation via Code nodes"},
        "deliverable": {"uz": "Kiruvchi ma'lumotlarni saralab, tozalab tegishli manzillarga yo'naltiruvchi mukammal n8n ssenariysi", "ru": "Сценарий n8n для фильтрации, валидации и маршрутизации входящих данных", "en": "Multi-branch n8n scenario parsing, normalizing, and routing unstructured payload batches"},
        "tools": "n8n Expression Editor, JSON Schema, JavaScript Code Nodes"
    },
    21: {
        "title": {"uz": "n8n + AI Nodlari va Neyro-Tahlil Konveyerlari", "ru": "n8n + Узлы ИИ и Конвейеры Нейроанализа", "en": "n8n + AI Nodes and Neural Analytics Pipelines"},
        "type": {"uz": "Interaktiv Lab", "ru": "Интерактивная Лаб", "en": "Interactive Lab"},
        "skills": {"uz": "n8n ichida OpenAI/Anthropic/Ollama ulanmalari, Prompt zanjirlari, Kiruvchi arizalarni avtomatik baholash va xulosa yozish", "ru": "Подключение OpenAI/Anthropic/Ollama в n8n, цепочки промптов, автоанализ входящих заявок и резюмирование", "en": "Connecting OpenAI/Anthropic/Ollama in n8n, AI Agent Nodes, dynamic document synthesis and auto-replies"},
        "deliverable": {"uz": "Mijoz xatlarini AI yordamida o'qib, sentiment tahlil qilib javob tayyorlovchi aqlli n8n boti", "ru": "Умный n8n бот, читающий письма, анализирующий тональность и генерирующий ответы", "en": "Intelligent n8n pipeline analyzing incoming customer tickets with sentiment tags and drafting responses"},
        "tools": "n8n AI Agent Nodes, OpenAI API, Anthropic API"
    },
    22: {
        "title": {"uz": "Make.com vs n8n: Korporativ Ma'lumotlar Quvurlari", "ru": "Make.com vs n8n: Корпоративные Конвейеры Данных", "en": "Make.com vs n8n: Enterprise Data Pipelines"},
        "type": {"uz": "Tizimli Muhandislik", "ru": "Системная Инженерия", "en": "Systems Engineering"},
        "skills": {"uz": "Cloud iPaaS (Make) va Open-Source (n8n) taqqoslash, Google Sheets, Notion API, CRM tizimlari, Xatolarni avtomatik ushlash (Error Handlers)", "ru": "Сравнение Make и n8n, интеграция Google Sheets, Notion API, CRM, перехват ошибок (Error Handlers)", "en": "Cloud iPaaS (Make) vs Open-source (n8n), Google Workspace, Notion databases, CRM APIs, error handling triggers"},
        "deliverable": {"uz": "Google Sheets, Notion va Telegramni birlashtiruvchi sinxron korporativ ish stoli oqimi", "ru": "Синхронизированный корпоративный поток, объединяющий Google Sheets, Notion и Telegram", "en": "Synchronized multi-platform sync pipeline bridging Google Sheets, Notion DB, and operational Telegram alerts"},
        "tools": "Make.com, n8n, Google Cloud Console, Notion API"
    },
    23: {
        "title": {"uz": "Model Context Protocol (MCP) Standarti va Arxitekturasi", "ru": "Стандарт и Архитектура Model Context Protocol (MCP)", "en": "Model Context Protocol (MCP) Architecture and Standards"},
        "type": {"uz": "Ilg'or Standart", "ru": "Продвинутый Стандарт", "en": "Advanced Standard"},
        "skills": {"uz": "Anthropic MCP spetsifikatsiyasi, Host, Client va Server rollari, JSON-RPC protokoli, Resurslar, Vositalar va Promptlar ta'rifi", "ru": "Спецификация Anthropic MCP, роли Host, Client и Server, протокол JSON-RPC, ресурсы, инструменты и промпты", "en": "Anthropic MCP specification, Host/Client/Server roles, JSON-RPC transport, resources, tools, and prompt definitions"},
        "deliverable": {"uz": "Claude Desktop yoki Cursor muhitiga MCP protokoli orqali birinchi standart serverni ulash", "ru": "Подключение первого стандартного MCP сервера к Claude Desktop или Cursor", "en": "Working MCP connection between Claude Desktop/Cursor and local system services via JSON-RPC"},
        "tools": "Claude Desktop, MCP Inspector, JSON-RPC, Python MCP SDK"
    },
    24: {
        "title": {"uz": "Shaxsiy MCP Server Dasturlash (Custom MCP Server)", "ru": "Разработка Кастомного MCP Сервера", "en": "Building Custom MCP Servers"},
        "type": {"uz": "Chuqur Dasturlash", "ru": "Глубокая Разработка", "en": "Deep Engineering"},
        "skills": {"uz": "TypeScript/Python da shaxsiy MCP server yozish, Korporativ SQLite/PostgreSQL bazasini AI ga MCP vositasi sifatida ulash", "ru": "Создание кастомного MCP сервера на TypeScript/Python, подключение SQLite/PostgreSQL к ИИ через MCP", "en": "Writing a custom MCP server in Python/TypeScript, exposing local SQLite/PostgreSQL queries safely to LLMs"},
        "deliverable": {"uz": "Foydalanuvchi ma'lumotlar bazasini AI ga xavfsiz o'qib beruvchi maxsus ishlab chiqilgan shaxsiy MCP server", "ru": "Кастомный MCP сервер, безопасно предоставляющий данные из базы для AI ассистента", "en": "Custom open-source MCP server enabling local database inspection and dynamic report generation"},
        "tools": "FastMCP Python, TypeScript, SQLite, GitHub"
    },
    25: {
        "title": {"uz": "AI RPA va Hujjatlarni Intellektual Qayta Ishlash", "ru": "AI RPA и Интеллектуальная Обработка Документов", "en": "AI RPA and Intelligent Document Processing"},
        "type": {"uz": "Biznes Yechim", "ru": "Бизнес Решение", "en": "Enterprise Solution"},
        "skills": {"uz": "RPA (Robotic Process Automation), Hujjatlar (PDF, schet-fakturalar, cheklar) dan ma'lumot ajratish (OCR), Strukturaviy JSON eksporti", "ru": "RPA (роботизация процессов), извлечение данных из PDF, счетов и чеков (OCR), экспорт в структурированный JSON", "en": "Robotic Process Automation (RPA), PDF/invoice OCR extraction, structured data schema enforcement"},
        "deliverable": {"uz": "Kompaniyaga kelgan PDF schet-fakturalarni 1 soniyada o'qib, hisob-kitob bazasiga kirituvchi avtonom robot", "ru": "Автономный робот, мгновенно считывающий PDF-счета и вносящий данные в базу", "en": "Autonomous document processing pipeline parsing raw PDF invoices into verified accounting entries"},
        "tools": "Tesseract / Document AI, Python PDFPlumber, n8n Pipeline"
    },
    26: {
        "title": {"uz": "3-Chorak Oraliq Nazorat: To'liq Korporativ Avtomatlashtirish Sinovi", "ru": "Промежуточный Контроль 3-й Четверти: Корпоративная Автоматизация", "en": "Quarter 3 Midterm Exam: End-to-End Enterprise Automation Pipeline"},
        "type": {"uz": "Oraliq Imtihon", "ru": "Промежуточный Экзамен", "en": "Midterm Examination"},
        "skills": {"uz": "n8n + MCP + Tashqi servislar integratsiyasining barqarorligi, Xatolarga chidamlilik, Tezlik va xavfsizlik auditi", "ru": "Отказоустойчивость связки n8n + MCP + внешние сервисы, аудит скорости и безопасности", "en": "Integration stability of n8n + custom MCP servers, error recovery, throughput metrics, and audit"},
        "deliverable": {"uz": "Imtihon topshirig'i bo'yicha to'liq avtomatlashtirilgan ko'p bosqichli korporativ konveyer (10 ballik mezon)", "ru": "Полностью автоматизированный многоэтапный корпоративный конвейер (10-балльная шкала)", "en": "Production-ready enterprise workflow integrating webhook ingestion, MCP query, and alert dispatch"},
        "tools": "n8n Server, Custom MCP, Docker Monitor"
    },
    27: {
        "title": {"uz": "3-Chorak Demo Day: Target Maktabi Biznes Avtomatlashtirish Ko'rgazmasi", "ru": "Demo Day 3-й Четверти: Выставка Бизнес-Автоматизации Школы Target", "en": "Quarter 3 Demo Day: Target School Business Automation Expo"},
        "type": {"uz": "Demo Day / Ko'rgazma", "ru": "Demo Day / Выставка", "en": "Demo Day / Expo"},
        "skills": {"uz": "Biznes keys taqdimoti, Samaradorlik (ROI) hisobi, Jonli avtomatlashtirish jarayonini ko'rsatish, Savollarga javob", "ru": "Презентация бизнес-кейса, расчет окупаемости (ROI), демонстрация живого процесса, ответы на вопросы", "en": "Business automation pitch, efficiency/ROI metric calculations, live pipeline demo, and feedback review"},
        "deliverable": {"uz": "Maktab ma'muriyati yoki real kompaniyaga topshirilgan ishchi avtomatlashtirish tizimi va diplom", "ru": "Работающая система автоматизации, переданная школе или компании, и диплом 3-й четверти", "en": "Operational enterprise automation pipeline delivered to school stakeholders, plus Quarter 3 Diploma"},
        "tools": "Live Production Pipeline, Project Docs, Video Walkthrough"
    },
    28: {
        "title": {"uz": "Startap G'oyasi, PRD va Tizim Arxitekturasi (System Design)", "ru": "Идея Стартапа, PRD и Системный Дизайн", "en": "Startup Ideation, PRD, and System Design Architecture"},
        "type": {"uz": "Startap Dizayn", "ru": "Дизайн Стартапа", "en": "Startup Design"},
        "skills": {"uz": "Muammoni aniqlash, PRD (Product Requirements Document), C4 arxitektura diagrammalari, Texnologik stekni tanlash", "ru": "Анализ проблемы, документ PRD, диаграммы архитектуры C4, выбор технологического стека", "en": "Problem discovery, PRD document authoring, C4 architecture mapping, and tech stack specification"},
        "deliverable": {"uz": "Tasdiqlangan PRD hujjati va bo'lajak SaaS loyihasining to'liq arxitektura chizmasi", "ru": "Утвержденный документ PRD и полная схема системной архитектуры SaaS проекта", "en": "Approved Product Requirements Document (PRD) and C4 System Architecture Specification"},
        "tools": "Notion PRD Template, Mermaid.js, Excalidraw, Git"
    },
    29: {
        "title": {"uz": "Ma'lumotlar Bazasi va Backend Core: Supabase va RLS", "ru": "База Данных и Ядро Бэкенда: Supabase и RLS", "en": "Database and Backend Core: Supabase, PostgreSQL, and RLS"},
        "type": {"uz": "Backend Muhandislik", "ru": "Бэкенд Инженерия", "en": "Backend Engineering"},
        "skills": {"uz": "PostgreSQL reliesion sxemasi, Row Level Security (RLS) qoidalari, Supabase Auth (JWT), Edge Functions va Triggers", "ru": "Схема PostgreSQL, правила Row Level Security (RLS), Supabase Auth (JWT), Edge Functions и триггеры", "en": "PostgreSQL relational modeling, Row-Level Security (RLS) policies, Supabase Auth, and Edge Functions"},
        "deliverable": {"uz": "Xavfsiz sozlangan ishlab turuvchi korporativ ma'lumotlar bazasi va CRUD API nuqtalari", "ru": "Безопасная корпоративная база данных с политиками RLS и эндпоинты CRUD API", "en": "Production PostgreSQL schema with enforced RLS policies and authenticated REST/GraphQL endpoints"},
        "tools": "Supabase, PostgreSQL, SQL Editor, TablePlus"
    },
    30: {
        "title": {"uz": "AI Agent va RAG Yadrosi Integratsiyasi", "ru": "Интеграция Ядра AI Агентов и RAG", "en": "AI Agent and RAG Core Integration"},
        "type": {"uz": "AI Muhandislik", "ru": "AI Инженерия", "en": "AI Engineering"},
        "skills": {"uz": "Loyiha backendiga RAG va multi-agent funksiyalarini ulash, Streaming javoblar (SSE), Token kesh va tejamkorlik", "ru": "Подключение RAG и агентов к бэкенду, стриминг ответов (SSE), кэширование токенов и оптимизация", "en": "Integrating RAG and autonomous agents with backend APIs, response streaming (SSE), and token caching"},
        "deliverable": {"uz": "Sayt ichida real vaqtda aqlli yechimlar beruvchi va bazaga yozuvchi AI moduli", "ru": "Интегрированный модуль AI, анализирующий запросы и работающий с базой в реальном времени", "en": "End-to-end AI module processing complex queries with streaming UI and DB transaction logging"},
        "tools": "OpenAI/Claude API, Vector Search, SSE Streaming"
    },
    31: {
        "title": {"uz": "Zamonaviy Frontend va Dizayn Tizimi (Linear/Supabase Aesthetic)", "ru": "Современный Фронтенд и Дизайн-Система (Linear/Supabase)", "en": "Modern Frontend and High-Fidelity UI/UX (Linear Aesthetic)"},
        "type": {"uz": "Frontend Mahorat", "ru": "Фронтенд Мастерство", "en": "Frontend Polish"},
        "skills": {"uz": "Zamonaviy SaaS estetikasi, Tailwind CSS, Dark/Light rejim, Moslashuvchan qismlar, Yuklanish skeletlari (Skeletons)", "ru": "Эстетика SaaS (Linear/Supabase), Tailwind CSS, темная/светлая тема, адаптивные компоненты, скелетоны загрузки", "en": "High-fidelity SaaS design system, Tailwind CSS tokens, responsive UI, micro-animations, loading skeletons"},
        "deliverable": {"uz": "Har qanday qurilmada mukammal ochiluvchi professional foydalanuvchi interfeysi (UI)", "ru": "Профессиональный интерфейс пользователя (UI), идеально работающий на всех устройствах", "en": "Polished responsive SaaS web interface matching Linear/Supabase aesthetic standards"},
        "tools": "Next.js / Vanilla SPA, Tailwind CSS, Lucide Icons"
    },
    32: {
        "title": {"uz": "Prodaction Infratuzilma, Docker va CI/CD Konveyeri", "ru": "Продакшн Инфраструктура, Docker и CI/CD", "en": "Production Infrastructure, Docker, and CI/CD Pipeline"},
        "type": {"uz": "DevOps Deploy", "ru": "DevOps Деплой", "en": "DevOps Deployment"},
        "skills": {"uz": "Docker ko'p bosqichli build (multi-stage), GitHub Actions orqali avtomatik Vercel/VPS deploy, SSL va Custom domen", "ru": "Многоэтапная сборка Docker, автодеплой через GitHub Actions на Vercel/VPS, SSL и кастомный домен", "en": "Multi-stage Docker build, automated GitHub Actions deployment to production, custom domain and SSL"},
        "deliverable": {"uz": "Global internetda o'z domenida xavfsiz HTTPS bilan ishlayotgan jonli mahsulot", "ru": "Работающий в интернете живой продукт на собственном домене с сертификатом SSL", "en": "Live production deployment on custom domain with automated CI/CD and HTTPS certificate"},
        "tools": "GitHub Actions, Vercel / Railway, Docker, Cloudflare DNS"
    },
    33: {
        "title": {"uz": "Kiber-Xavfsizlik Auditi, OWASP va Yuklama Sinovi (Stress-Test)", "ru": "Аудит Кибербезопасности, OWASP и Нагрузочное Тестирование", "en": "Security Audit, OWASP Verification, and Load Testing"},
        "type": {"uz": "Xavfsizlik & Yuklama", "ru": "Безопасность и Нагрузка", "en": "Security and Load Testing"},
        "skills": {"uz": "OWASP Top 10 tekshiruvi, Rate limiter samaradorligi, k6 yoki Locust orqali 1000 RPS stress testi, Zaifliklarni tuzatish", "ru": "Проверка OWASP Top 10, эффективность Rate limiter, стресс-тест на 1000 RPS через k6/Locust, устранение багов", "en": "OWASP Top 10 compliance audit, rate limiting validation, 1000 RPS load testing via k6, and patch deployment"},
        "deliverable": {"uz": "Yuklama va xavfsizlik sinovlaridan muvaffaqiyatli o'tgan rasmiy Xavfsizlik Sertifikati hisoboti", "ru": "Официальный отчет об аудите безопасности и нагрузочных испытаниях продукта", "en": "Comprehensive load test and security audit report certifying production readiness"},
        "tools": "k6, OWASP ZAP, Postman Newman, Sentry"
    },
    34: {
        "title": {"uz": "Foydalanuvchi Sinovi (Beta Testing) va Bug Fixing", "ru": "Бета-Тестирование Пользователями и Устранение Багов", "en": "Beta User Testing and Defect Remediation"},
        "type": {"uz": "Sifat Kafolati (QA)", "ru": "Контроль Качества (QA)", "en": "Quality Assurance"},
        "skills": {"uz": "Haqiqiy foydalanuvchilar bilan beta test, Telemetriya tahlili (PostHog), Xatolarni bartaraf etish", "ru": "Бета-тест с реальными пользователями, анализ телеметрии (PostHog), исправление пользовательских ошибок", "en": "Beta user cohorts, UX feedback loops, telemetry monitoring, and prioritized bug triage"},
        "deliverable": {"uz": "10+ foydalanuvchi fikri asosida to'liq yaxshilangan va xatolardan tozalangan v1.0 relizi", "ru": "Улучшенная версия v1.0, оптимизированная на основе отзывов 10+ пользователей", "en": "Polished v1.0 release addressing all beta tester feedback and telemetry edge cases"},
        "tools": "PostHog, Bug Tracker, GitHub Milestones"
    },
    35: {
        "title": {"uz": "Startap Hujjatlari, Pitch Deck va Demo Video", "ru": "Документация Стартапа, Питч-Дек и Демо-Видео", "en": "Startup Documentation, Pitch Deck, and Demo Video"},
        "type": {"uz": "Portfel & Pitch", "ru": "Портфолио и Питч", "en": "Portfolio and Pitch Deck"},
        "skills": {"uz": "Investorlar va mijozlar uchun 3 daqiqalik video lavha, Pitch Deck slaydlar, GitHub README arxitekturasi va API qo'llanmasi", "ru": "3-минутное демо-видео, слайды Pitch Deck, документация README на GitHub и руководство по API", "en": "3-minute product walkthrough video, 10-slide investor pitch deck, comprehensive GitHub documentation"},
        "deliverable": {"uz": "Professional GitHub repozitoriysi, demo video va taqdimot slaydlar to'plami", "ru": "Профессиональный репозиторий на GitHub, демо-видео и комплект слайдов презентации", "en": "Professional GitHub open-source showcase repository, recorded demo video, and pitch deck"},
        "tools": "Loom / OBS, Canva / Keynote, Markdown, Git"
    },
    36: {
        "title": {"uz": "Target Grand Demo Day: Yillik Capstone Himoyasi va Bitiruv", "ru": "Target Grand Demo Day: Защита Годового Capstone Проекта и Выпуск", "en": "Target Grand Demo Day: Annual Capstone Defense and Graduation"},
        "type": {"uz": "Grand Demo Day", "ru": "Grand Demo Day", "en": "Grand Demo Day"},
        "skills": {"uz": "Maktab ma'muriyati, ota-onalar va IT ekspertlari oldida startap himoyasi, Savol-javob, Mahsulotni topshirish", "ru": "Защита стартапа перед жюри школы, родителями и IT экспертами, сессия вопросов и ответов", "en": "Formal defense before School Board and industry evaluators, live capability proof, diploma awarding"},
        "deliverable": {"uz": "Muvaffaqiyatli himoya qilingan to'liq yillik Capstone SaaS startapi va Target IT Oltin Sertifikati", "ru": "Успешно защищенный годовой Capstone SaaS стартап и золотой сертификат Target IT", "en": "Successfully defended annual production Capstone SaaS platform and Target IT Honors Diploma"},
        "tools": "Stage Presentation, Live Production App, Honors Certificate"
    }
}
