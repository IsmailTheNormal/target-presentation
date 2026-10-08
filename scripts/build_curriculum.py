#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Target International School — Ish Rejasi Generator
Ushbu skript repo ichidagi real darslar (classes/ va index.html COURSE_DATA)
asosida rasmiy REJA.md va interaktiv, chop etiladigan reja.html ni yaratadi.
"""

import json
import re
import os
import sys

def load_course_data():
    with open('index.html', 'r', encoding='utf-8') as f:
        text = f.read()
    m = re.search(r'window\.COURSE_DATA\s*=\s*(\[.*?\]);\s*</script>', text, re.DOTALL)
    if not m:
        raise ValueError("COURSE_DATA not found in index.html")
    return json.loads(m.group(1))

# Qo'shimcha pedagogik ma'lumotlar va kompetensiyalar xaritasi
COMPETENCIES = {
    # 10-11-sinf
    "01-dars-ai-nima": {
        "type": "Nazariy-Amaliy",
        "skills": "AI modellari turlari, LLM generatsiyasi, Prompt sintaksisi",
        "deliverable": "AI vositalari taqqoslash jadvali va birinchi tizimli so'rov",
        "tools": "ChatGPT, Claude, Perplexity"
    },
    "02-dars-vibecoding-asoslari": {
        "type": "Amaliy",
        "skills": "UI/UX asoslari, Frontend va Backend arxitekturasi, Semantik teglari",
        "deliverable": "Mahsulot sahifasi uchun vizual bloklar maketi",
        "tools": "HTML5, CSS3, Chrome DevTools"
    },
    "03-dars-it-dunyosi-kod-va-cloud": {
        "type": "Nazariy-Amaliy",
        "skills": "Internet qanday ishlaydi, DNS, HTTP, Client-Server modeli, Cloud hosting",
        "deliverable": "Internet ma'lumotlar marshruti sxemasi",
        "tools": "Terminal, ping, traceroute, Cloudflare"
    },
    "04-dars-frilans-buyurtma-ui": {
        "type": "Amaliy Loyiha",
        "skills": "Texnik topshiriq (PRD) tahlili, CSS Grid va Flexbox, Moslashuvchan dizayn",
        "deliverable": "Mijoz talabi bo'yicha tayyorlangan Landing Page UI",
        "tools": "VS Code, CSS Flexbox/Grid"
    },
    "05-dars-frilans-mantiq-js": {
        "type": "Amaliy Loyiha",
        "skills": "JavaScript DOM manipulyatsiyasi, Hodisalar (Events), Dark/Light rejim",
        "deliverable": "Interaktiv savatcha va mavzu almashtirgichga ega veb-ilova",
        "tools": "Vanilla JavaScript, DOM API"
    },
    "06-dars-deploy-va-taqdimot": {
        "type": "Deploy / Demo Day",
        "skills": "Git versiya nazorati, Vercel/Netlify deploy, SSL sertifikati, QR kod generatsiyasi",
        "deliverable": "Global internetda ishlayotgan jonli HTTPS sayt va mobil QR kod",
        "tools": "Vercel, Git, QR Code Generator"
    },
    "07-dars-api-va-json-asoslari": {
        "type": "Nazariy-Amaliy",
        "skills": "REST arxitekturasi, JSON ma'lumotlar formati, HTTP metodlar (GET/POST), CORS",
        "deliverable": "Jonli API dan ma'lumot tortuvchi asinxron fetch() skripti",
        "tools": "Fetch API, Postman / Thunder Client"
    },
    "08-dars-jonli-valyuta-konverteri": {
        "type": "Amaliy Loyiha",
        "skills": "Markaziy Bank API integratsiyasi, Dinamik valyuta hisoblash, Xatolarni ushlash",
        "deliverable": "Real vaqt kurslarini hisoblovchi to'liq valyuta kalkulyatori",
        "tools": "CBU REST API, JavaScript Async/Await"
    },
    "09-dars-localstorage-va-state": {
        "type": "Amaliy",
        "skills": "Brauzer xotirasi (LocalStorage), JSON serializatsiya, Ilova holati (State)",
        "deliverable": "Refresh qilinganda o'chmaydigan operatsiyalar tarixi va sozlamalar",
        "tools": "Window.localStorage, JSON.stringify/parse"
    },
    "10-dars-auth-va-himoya": {
        "type": "Kiberxavfsizlik",
        "skills": "Autentifikatsiya, Parollarni xeshlash, Xavfsiz tokonlar, .env maxfiy kalitlar",
        "deliverable": "Xavfsiz login tizimi va GitHub ga kalit sizib ketishidan himoyalangan .gitignore",
        "tools": ".env, bcrypt tushunchasi, Git secret scan"
    },
    "11-dars-vscode-va-mahalliy-muhit": {
        "type": "Muhandislik",
        "skills": "Mahalliy dasturlash muhiti (IDE), Kengaytmalar, Emmet, Live Server, Git integratsiyasi",
        "deliverable": "Sozlangan professional VS Code muhiti va mahalliy server",
        "tools": "VS Code, ESLint, Live Server, Bash"
    },
    "12-dars-agentic-ai-va-avtonom-kod": {
        "type": "Agentik AI",
        "skills": "Agentik dasturlash paradigmasi, ReAct tsikli, Mustaqil kod tuzatish, AI CLI vositalari",
        "deliverable": "AI agent tomonidan yaratilgan va xatolardan tozalangan to'liq modul",
        "tools": "Agent CLI, Cursor / Claude Code / Copilot"
    },
    "13-dars-llm-arxitekturasi-va-prompt-muhandisligi": {
        "type": "Chuqur Muhandislik",
        "skills": "Transformer arxitekturasi, Kontekst oynasi, BPE tokenizatsiya, Sampling (Temp, Top-P)",
        "deliverable": "Optimal parametrlar bilan sozlangan korporativ LLM prompti (Lab)",
        "tools": "LLM Studio / Parameter Playground"
    },
    "14-dars-tool-calling-va-funksiyalar": {
        "type": "Interaktiv Lab",
        "skills": "Function Calling mexanizmi, JSON Schema spetsifikatsiyasi, ReAct tsikli, REST bog'lanish",
        "deliverable": "Tashqi API ni mustaqil chaqiruvchi va ma'lumot oluvchi neyro-agent (Lab)",
        "tools": "JSON Schema, Tool Calling Simulator"
    },
    "15-dars-rag-va-vektor-qidiruv": {
        "type": "Interaktiv Lab",
        "skills": "RAG (Retrieval-Augmented Generation) asoslari, Chunking, Semantik indekslash",
        "deliverable": "Kompaniya ichki hujjatlari bo'yicha adashmasdan javob beruvchi RAG bot (Lab)",
        "tools": "Vector Search Sandbox, Document Chunker"
    },
    "16-dars-avtonom-agentlar-va-xotira": {
        "type": "Interaktiv Lab",
        "skills": "Multi-agent tizimlar, Qisqa va uzoq muddatli xotira, Plan-and-Solve arxitekturasi",
        "deliverable": "Bir nechta ixtisoslashgan agentlardan iborat avtonom muhandislik jamoasi (Lab)",
        "tools": "Multi-Agent Orchestrator"
    },
    "15-dars-rag-va-embeddinglar": {
        "type": "Matematik AI Lab",
        "skills": "Vektor embeddinglar, Yuqori o'lchovli fazo, Kosinus o'xshashlik formulasi, Dot product",
        "deliverable": "Kosinus burchagi orqali semantik yaqinlikni aniqlovchi qidiruv tizimi (Lab)",
        "tools": "Cosine Similarity Calculator, Vector Visualizer"
    },
    "16-dars-prompt-injection-va-ai-xavfsizligi": {
        "type": "Red Team Lab",
        "skills": "OWASP LLM01, Direct va Indirect Prompt Injection, Jailbreak turlari, Dual-LLM filtr",
        "deliverable": "Xakerlik xurujlariga bardosh beruvchi ko'p qatlamli Guardrail himoya tizimi (Lab)",
        "tools": "Red Teaming Playground, NeMo Guardrails simulyatori"
    },
    "21-dars-kriptografiya-aes-va-rsa": {
        "type": "Interaktiv Studio",
        "skills": "Simmetrik AES-256-GCM, Asimmetrik RSA-2048, SHA-256 xesh, Bit Tamper hujumi",
        "deliverable": "Crypto Studio da shifrlangan xabarlar, kalitlar juftligi va tamper tekshiruvi (Studio)",
        "tools": "WebCrypto API (Native SubtleCrypto), Crypto Studio"
    },
    "22-dars-zero-trust-va-iam-arxitekturasi": {
        "type": "Enterprise Architecture",
        "skills": "NIST SP 800-207, Verify Explicitly, Least Privilege, Assume Breach, RBAC vs ABAC, mTLS",
        "deliverable": "Least-Privilege tamoyiliga mos korporativ IAM JSON siyosati va Capital One tahlili",
        "tools": "AWS IAM Policy Engine, Policy Validator"
    },
    "23-dars-api-xavfsizligi-va-rate-limiting": {
        "type": "Kiberxavfsizlik",
        "skills": "OWASP API Top 10, Token Bucket va Leaky Bucket algoritmlari, DDoS mudofaasi, HMAC imzo",
        "deliverable": "API cheklovchi va soxtalashtirilgan so'rovlarni aniqlovchi HMAC middleware",
        "tools": "Rate Limiter Simulator, HMAC-SHA256 Signer"
    },
    "24-dars-ai-model-xavfsizligi-va-adversarial-attacks": {
        "type": "AI Xavfsizlik",
        "skills": "MITRE ATLAS, Adversarial Perturbation, FGSM gradient hujumi, Data Poisoning, Red Teaming",
        "deliverable": "Ko'rinmas shovqinli kiber-hujumlar va zaharli o'quv ma'lumotlarini aniqlash protokoli",
        "tools": "FGSM Perturbation Visualizer, Model Robustness Auditor"
    },
    "25-dars-soc-simulyatsiyasi-va-insident-boshqaruvi": {
        "type": "Kiber-Insident",
        "skills": "SOC (Security Operations Center) 24/7, SIEM/SOAR, Sigma qoidalari, NIST SP 800-61, MTTR",
        "deliverable": "Sigma aniqlash qoidasi va xakerlik hujumidan keyingi rasmiy Post-Mortem hisoboti",
        "tools": "SIEM Log Analyzer, Sigma Rule Editor"
    },

    # 9-sinf o'ziga xos darslari
    "12-dars-ai-bug-hunter": {
        "type": "Kiber-Detektivlik",
        "skills": "AI Bug Hunter metodologiyasi, Xatolarni aniqlash, DevTools Konsol, Sintaksis va Mantiq",
        "deliverable": "Buzilgan 'Kiber-Baza' loyihasining 5 ta xatosini to'liq bartaraf etish (Arena)",
        "tools": "AI Bug Hunter Arena, VS Code Debugger"
    },
    "13-dars-ai-chat-va-streaming": {
        "type": "Interaktiv Lab",
        "skills": "Real-vaqt ma'lumot oqimi (Streaming), Server-Sent Events (SSE), ReadableStream, UI animatsiya",
        "deliverable": "Harflar oqim bilan keluvchi professional ChatGPT kloni (Lab)",
        "tools": "Fetch ReadableStream, EventSource, Markdown Parser"
    },
    "13-dars-git-va-github": {
        "type": "DevOps / VCS",
        "skills": "Git versiya nazorati, git init/add/commit, Branching strategiyasi, Merge mojarolarini yechish",
        "deliverable": "GitHub da repozitoriy, bir nechta branchlar va muvaffaqiyatli merge tarixi (Lab)",
        "tools": "Git CLI, GitHub Web, VS Code Source Control"
    },
    "14-dars-pull-request-va-kod-korigi": {
        "type": "Jamoaviy Hamkorlik",
        "skills": "Pull Request (PR) yuborish, Diff ko'rigi, Inline izohlar, Reviewer etikasi, LGTM",
        "deliverable": "Juftlikda ko'rib chiqilgan, izohlar yozilgan va qabul qilingan PR (Lab)",
        "tools": "GitHub Pull Requests, Markdown Review"
    },
    "14-dars-tizimli-promptlar-va-himoya": {
        "type": "AI Xavfsizlik",
        "skills": "System Prompt arxitekturasi, Rol chegaralari, Delimiterlar, Prompt Injection himoyasi",
        "deliverable": "Hech qanday hiyla bilan sirlarini oshkor qilmaydigan mustahkam himoyalangan bot (Lab)",
        "tools": "System Prompt Sandbox"
    },
    "15-dars-ci-cd-va-avtomatlashtirish": {
        "type": "DevOps Lab",
        "skills": "CI/CD konveyeri, GitHub Actions YAML sintaksisi, Avtomatik testlar, Linting, Webhooklar",
        "deliverable": "Har bir commitda testlarni avtomatik ishga tushiruvchi `.github/workflows/ci.yml` (Lab)",
        "tools": "GitHub Actions, YAML, Node Test Runner"
    },
    "16-dars-semver-release-va-open-source": {
        "type": "Dasturiy Ta'minot",
        "skills": "SemVer (Semantic Versioning), Git Tag, GitHub Releases, Changelog yuritish, Open Source",
        "deliverable": "SemVer standarti bo'yicha versiyalangan va release qilingan rasmiy paket (Lab)",
        "tools": "Git Tag, GitHub Releases, KeepAChangelog"
    },
    "17-dars-docker-va-konteynerlar": {
        "type": "DevOps",
        "skills": "Konteynerlashtirish asoslari, Virtual mashina vs Docker, Dockerfile sintaksisi, Port mapping",
        "deliverable": "Veb-ilovaning Dockerfile fayli va konteynerda ishga tushirish amaliyoti",
        "tools": "Docker CLI, Docker Desktop, Alpine Linux"
    },
    "18-dars-malumotlar-bazasi-va-sql": {
        "type": "Interaktiv Lab",
        "skills": "Relyatsion ma'lumotlar bazasi (RDBMS), SQL tili (SELECT, INSERT, UPDATE, JOIN), Indekslar",
        "deliverable": "E-tijorat tizimi uchun to'liq reliesion SQLite bazasi va SQL so'rovlar to'plami (Lab)",
        "tools": "SQLite3, SQL Lab & Simulyator"
    },
    "19-dars-backend-express-va-rest-api": {
        "type": "Interaktiv Studio",
        "skills": "Node.js, Express.js arxitekturasi, REST API marshrutlash (CRUD), Middleware, JSON javoblar",
        "deliverable": "SQLite bazasiga ulangan va Postman da sinovdan o'tgan Express REST API (Studio)",
        "tools": "Express API Studio & Postman Simulyatori"
    },
    "20-dars-fullstack-deploy-va-demo-day": {
        "type": "Production Deploy",
        "skills": "Full-Stack integratsiyasi, Environment o'zgaruvchilari, Cloud ma'lumotlar bazasi, Jonli server",
        "deliverable": "Frontend + Backend + DB to'liq bulutda ishlayotgan tijoriy loyiha",
        "tools": "Render / Railway / Vercel, Supabase / Neon"
    },
    "21-dars-linux-server-va-ssh-himoyasi": {
        "type": "Tizim Boshqaruvi",
        "skills": "Linux boshqaruvi, SSH kalitlari (ed25519), UFW fayrvoll, Parolsiz kirish, Fail2ban",
        "deliverable": "Brute-force hujumlaridan himoyalangan va qulflangan xavfsiz Linux serveri",
        "tools": "Ubuntu Server, OpenSSH, UFW, Fail2ban"
    },
    "22-dars-tarmoq-xavfsizligi-va-paket-tahlili": {
        "type": "Tarmoq Auditi",
        "skills": "TCP/IP modeli, 3 tomonlama handshake, Wireshark bilan paket tahlili, Nmap port skanerlash",
        "deliverable": "Tarmoq trafigi tahlili va shubhali portlarni aniqlash bo'yicha audit xulosasi",
        "tools": "Wireshark, Nmap, TCPdump"
    },
    "23-dars-veb-zaifliklari-va-owasp-top-10": {
        "type": "AppSec Lab",
        "skills": "SQL Injection (SQLi), Cross-Site Scripting (XSS), CSRF, Sanitizatsiya, Parametrlangan so'rovlar",
        "deliverable": "OWASP Top 10 zaifliklariga qarshi tuzatilgan va himoyalangan veb-ilova",
        "tools": "OWASP Juice Shop / DVWA misollari, DOMPurify"
    },
    "24-dars-autentifikatsiya-jwt-va-2fa": {
        "type": "Xavfsizlik",
        "skills": "JWT (JSON Web Token) tuzilishi, Imzo tekshiruvi, Refresh token strategiyasi, 2FA (TOTP)",
        "deliverable": "JWT asosida ishlovchi va Google Authenticator bilan bog'langan 2FA tizimi",
        "tools": "JWT.io, Speakeasy / Otplib, Authenticator"
    },
    "25-dars-kiber-hujum-ctf-va-red-blue-team": {
        "type": "CTF Musobaqasi",
        "skills": "Capture The Flag (CTF), Red Team (Hujumkor) va Blue Team (Mudofaa) taktikalari",
        "deliverable": "CTF musobaqasida topilgan bayroqlar (flags) va hodisa xavfsizlik tahlili",
        "tools": "CTFd platformasi, Kiber-poligon"
    },

    # 7-8-sinf o'ziga xos darslari
    "01-dars-ai-nima": {
        "type": "Kirish",
        "skills": "AI vositalari, Generativ modellar bilan ishlash, Prompt tuzilishi",
        "deliverable": "Prompt konspekti va AI bilan ishlash xulosasi",
        "tools": "AI Chatbotlar"
    },
    "02-dars-ai-duel": {
        "type": "Interaktiv Bahs",
        "skills": "Prompt jangi (Prompt Duel), Aniqlik, Rollar va cheklovlar berish",
        "deliverable": "G'olib promptlar to'plami va taqqoslash jadvali",
        "tools": "Prompt Arena"
    },
    "03-dars-ai-rassom": {
        "type": "Vizual Ijod",
        "skills": "Vizual prompt tuzish, Uslublar, Kompozitsiya, Rasm generatsiyasi",
        "deliverable": "3 xil san'at uslubida yaratilgan o'yin qahramonlari rasmlari",
        "tools": "Midjourney / Bing Image Creator"
    },
    "04-dars-ai-kvest-oyini": {
        "type": "Geymdev Asoslari",
        "skills": "Matnli sarguzasht, Tarmoqlanuvchi syujet, AI vositasida stsenariy",
        "deliverable": "Tarmoqlanuvchi stsenariyli interaktiv kvest o'yini",
        "tools": "AI Prompting, Matnli muharrir"
    },
    "05-dars-veb-sahifa-birinchi-kod": {
        "type": "Amaliy",
        "skills": "HTML teglari, CSS rang va shriftlar, Veb-sahifa skeleti",
        "deliverable": "O'quvchining shaxsiy birinchi vizitka sahifasi",
        "tools": "HTML5, CSS3, Brauzer"
    },
    "06-dars-haftalik-turnir": {
        "type": "Taqdimot / Demo",
        "skills": "Loyiha taqdimoti, Peer review, Dasturchi etikasi",
        "deliverable": "Haftalik loyihalar ko'rgazmasi va o'zaro baholash",
        "tools": "Veb taqdimot"
    },
    "07-dars-veb-ustaxonasi-grid-va-flexbox": {
        "type": "Amaliy Ustaxona",
        "skills": "CSS Flexbox asoslari, CSS Grid ustunlari, Joylashuv (Layout)",
        "deliverable": "O'yin kartochkalari joylashgan moslashuvchan veb galereya",
        "tools": "CSS Flexbox / Grid"
    },
    "08-dars-javascript-hodisalar-va-klik": {
        "type": "Interaktiv Lab",
        "skills": "JavaScript DOM, querySelector, addEventListener, 'click' hodisasi",
        "deliverable": "Kliklanganda rang o'zgaruvchi va hisoblagich ishlovchi interaktiv panel (Lab)",
        "tools": "JavaScript DOM API"
    },
    "09-dars-mini-oyun-kiber-reaksiya": {
        "type": "Jonli O'yin",
        "skills": "Vaqt hisoblagich (Timer), Performance.now(), Millisekundlar, Reaksiya testi",
        "deliverable": "Insonning reaksiya tezligini o'lchovchi to'liq ishlaydigan mini-o'yin (O'yin)",
        "tools": "JavaScript Timers & Date API"
    },
    "10-dars-ai-debugging-va-mantiq": {
        "type": "Interaktiv Lab",
        "skills": "Xatolarni aniqlash, DevTools konsoli, Breakpoints, AI yordamida tuzatish",
        "deliverable": "Buzilgan kod mantig'ini to'g'rilash va testlardan o'tkazish (Lab)",
        "tools": "Chrome DevTools, AI Debugger"
    },
    "11-dars-localstorage-va-yuqori-ball": {
        "type": "Interaktiv Lab",
        "skills": "LocalStorage xotirasi, High Score saqlash, JSON.stringify/parse",
        "deliverable": "Brauzer yopilganda ham eng yuqori rekordni saqlab qoluvchi o'yin moduli (Lab)",
        "tools": "LocalStorage API"
    },
    "12-dars-oyun-turniri-va-deploy": {
        "type": "Jonli O'yin / Deploy",
        "skills": "Vercel deploy, Global URL, Sinflararo turnir jadvali, Jonli sinov",
        "deliverable": "Internetga yuklangan va sinfdoshlar bilan o'ynaladigan jonli o'yin (O'yin)",
        "tools": "Vercel, Git"
    },
    "13-dars-canvas-va-oyin-tsikli": {
        "type": "Interaktiv Lab",
        "skills": "HTML5 Canvas 2D kontekst, requestAnimationFrame (RAF), Game Loop, Delta Time",
        "deliverable": "60 FPS chastotada silliq harakatlanuvchi kvadrat va harakat dvigateli (Lab)",
        "tools": "Canvas 2D API"
    },
    "14-dars-dushmanlar-ochko-va-leaderboard": {
        "type": "Interaktiv Lab",
        "skills": "O'yin massivlari, Dushmanlar generatsiyasi, Ochko hisoblash, Saralash",
        "deliverable": "Ekrandan tushayotgan nishonlar va eng yaxshi 5 natija jadvali (Lab)",
        "tools": "JavaScript Arrays & Objects"
    },
    "15-dars-oyin-fizikasi-gravitatsiya-va-sakrash": {
        "type": "Interaktiv Lab",
        "skills": "Gravitatsiya (g), Vertikal tezlik (vy), Parabolik sakrash, AABB to'qnashuv algoritmi",
        "deliverable": "Platformalarga sakrovchi va to'qnashuvlarni aniq hisoblovchi fizik personaj (Lab)",
        "tools": "Kinematika & AABB Collision"
    },
    "16-dars-boss-jangi-va-power-ups": {
        "type": "Jonli O'yin Finali",
        "skills": "Boss jangi mexanikasi, Fazalar (Phases), Power-uplar (qalqon, tezlik), Win/Lose",
        "deliverable": "To'liq tugallangan 2D Canvas Arkada o'yini (Jonli O'yin)",
        "tools": "Canvas 2D Game Engine"
    },
    "17-dars-audio-api-va-partikllar": {
        "type": "Interaktiv Lab",
        "skills": "Web Audio API, Ovoz chastotasi (Oscillator), Zarba ovozlari, Partikl portlashi (VFX)",
        "deliverable": "Tugmachalar bosilganda ovoz chiqaruvchi va partikllar sochuvchi vizual tizim (Lab)",
        "tools": "Web Audio API, Particle System"
    },
    "18-dars-kamera-skrollingi-va-dunyo": {
        "type": "Interaktiv Lab",
        "skills": "Kamera siljishi (Camera Offset), Cheksiz dunyo, Procedural generatsiya",
        "deliverable": "Qahramon orqasidan ergashuvchi kamera va keng dunyo xaritasi (Lab)",
        "tools": "Canvas Transform & Camera Math"
    },
    "19-dars-mobil-touch-va-joystik": {
        "type": "Interaktiv Lab",
        "skills": "Sensorli ekran (Touch Events), touchstart/touchmove, Virtual analog joystik",
        "deliverable": "Smartfonda barmog'i bilan erkin boshqariladigan sensorli joystik (Lab)",
        "tools": "Touch Events API"
    },
    "20-dars-final-game-jam-va-deploy": {
        "type": "Game Jam Final",
        "skills": "Geym-dizayn yakunlash, Balanslash, Deploy, Vebda e'lon qilish, QR kod",
        "deliverable": "Smartfon va kompyuterda ishlaydigan mukammal arkada o'yini (O'yin)",
        "tools": "Game Jam, Vercel"
    },
    "21-dars-fut-card-studio": {
        "type": "Interaktiv Studio",
        "skills": "FileReader API, OVR hisoblash vaznli formulasi, CSS 3D Tilt effekti, Rasm yuklash",
        "deliverable": "O'z surati va statistikasi bilan yaratilgan rasmiy EA Sports FC uslubidagi karta (Studio)",
        "tools": "FUT Card Studio, File API"
    },
    "22-dars-fut-squad-builder": {
        "type": "Interaktiv Studio",
        "skills": "Graf tuzilmasi, Dinamik SVG kimyo zanjirlari, 33 ballik kimyo va OVR formulasi",
        "deliverable": "Yashil maydonda 11 talik to'liq taktik tarkib va kimyo hisoblagichi (Builder)",
        "tools": "FUT Squad Builder Studio, SVG"
    },
    "23-dars-fut-match-engine": {
        "type": "Interaktiv Simulyator",
        "skills": "FSM (Finite State Machine), Duel stoxastik ehtimolligi, Jonli xG hisobi, 2D radar",
        "deliverable": "90 daqiqalik o'yinni sharhlar va animatsiyalar bilan simulyatsiya qiluvchi dvigatel (Simulator)",
        "tools": "FUT Match Engine Simulator"
    },
    "24-dars-fut-transfer-market": {
        "type": "Interaktiv Bozor",
        "skills": "Talab va taklif qonuni, Auksion tizimi (Bid vs Buy Now), Anti-sniping, EA 5% Soliq",
        "deliverable": "1,000,000 tangalik byudjet bilan o'yinchilarni xarid qiluvchi virtual bozor (Market)",
        "tools": "Transfer Market Studio"
    },

    # 5-6-sinf o'ziga xos darslari
    "01-dars-ai-nima": {
        "type": "Sehrli Olam",
        "skills": "Sun'iy intellekt tushunchasi, Botlar bilan suhbat, Sehrli savollar",
        "deliverable": "AI nima ekanligi haqida rasm va qisqa xulosa",
        "tools": "Sehrli AI Chatbot"
    },
    "02-dars-ai-aktyor": {
        "type": "Ijodiy O'yin",
        "skills": "NPC (Not Playable Character) tushunchasi, Personaj fe'l-atvori, Rolga kirish",
        "deliverable": "O'yin uchun yaratilgan qahramon va uning dialoglari",
        "tools": "AI Personaj Generator"
    },
    "03-dars-ai-ertakchi": {
        "type": "Stsenariy",
        "skills": "O'yin olami (Game Lore), Sehrli qasrlar, Kiber-shahar tarixi",
        "deliverable": "O'yin boshlanishi haqida yozilgan qiziqarli hikoya",
        "tools": "AI Storyteller"
    },
    "04-dars-ai-multfilm": {
        "type": "Concept Art",
        "skills": "Rasm prompti, O'yin uslublari (Piksel, 3D, Anime), Ranglar",
        "deliverable": "O'yin uchun tayyorlangan 3 ta qahramon va to'siq surati",
        "tools": "AI Image Generator"
    },
    "05-dars-ai-siri-va-detektiv": {
        "type": "Kiber-Xavfsizlik",
        "skills": "Deepfake nima, Soxta rasmlar, AI yolg'onlarini fosh qilish",
        "deliverable": "Haqiqiy va sun'iy suratlarni ajratuvchi detektiv yozuvlari",
        "tools": "AI Fakt-Cheking"
    },
    "06-dars-sehrli-korgazma": {
        "type": "Digital Expo",
        "skills": "Loyiha namoyishi, Do'stlariga so'zlab berish, O'z fikrini himoya qilish",
        "deliverable": "Sinf ko'rgazmasida namoyish etilgan o'yin g'oyasi posteri",
        "tools": "Raqamli ko'rgazma"
    },
    "07-dars-3d-modellar-va-obyektlar": {
        "type": "O'yin Obyektlari",
        "skills": "3D modellar nima, O'yin ichidagi buyumlar (Qilich, Qalqon, Dori)",
        "deliverable": "O'yin inventari uchun tanlangan va tasvirlangan 4 ta artefakt",
        "tools": "AI 3D vizualizator"
    },
    "08-dars-oyun-dunyosi-va-level-design": {
        "type": "Level Design",
        "skills": "Xarita tuzilishi, O'rmon, Cho'l, Kiber-baza biomlari, Bosqichlar",
        "deliverable": "O'yin 1-bosqich xaritasining vizual chizmasi",
        "tools": "Xarita loyihalash"
    },
    "09-dars-ovoz-va-effektlar-sfx": {
        "type": "Ovoz Sehri",
        "skills": "SFX tovushlar (Sakrash, Tangalar, Lazer), Fon musiqasi, Atmosfera",
        "deliverable": "O'yin harakatlariga moslashtirilgan ovozlar to'plami",
        "tools": "AI Audio FX Generator"
    },
    "10-dars-aqlli-npc-va-dialoglar": {
        "type": "Aqlli NPC",
        "skills": "Tarmoqlanuvchi savol-javob, Maslahatchi sehrgar, Kvest topshiriqlari",
        "deliverable": "O'yinchiga topshiriq beruvchi aqlli kiber-ustoz dialogi",
        "tools": "Dialog Daraxti"
    },
    "11-dars-oyun-interfeysi-ui-hud": {
        "type": "O'yin UI",
        "skills": "HUD interfeysi, Qalbchalar (HP bar), Hisoblagich, Tangalar soni",
        "deliverable": "Ekranning yuqori burchagida joylashgan to'liq o'yin paneli",
        "tools": "UI Mockup"
    },
    "12-dars-game-jam-mini-loyiha": {
        "type": "Game Jam",
        "skills": "Barcha qismlarni jamlash, Prototip taqdimoti, Do'stlar o'yini",
        "deliverable": "Taqdim etilgan mini-o'yin prototipi va sertifikat",
        "tools": "Game Jam Showcase"
    },
    "13-dars-oyin-mexanikasi-va-boshqaruv": {
        "type": "Jonli O'yin",
        "skills": "Klaviatura strelkalari, Qahramon yugurishi, O'yin tsikli",
        "deliverable": "Tugmachalar bosilganda yuguruvchi va to'xtovchi Kiber-Qahramon (O'yin)",
        "tools": "Kiber-Yuguruvchi Engine"
    },
    "14-dars-tosiqlar-va-xavflar": {
        "type": "Jonli O'yin",
        "skills": "Tikanlar, Lazer nurlari, To'qnashuvda jon ketishi (HP - 1)",
        "deliverable": "Xavfli to'siqlar qo'shilgan va joni tugasa Game Over bo'ladigan o'yin (O'yin)",
        "tools": "Kiber-Yuguruvchi Engine"
    },
    "15-dars-tangalar-ballar-va-vaqt": {
        "type": "Jonli O'yin",
        "skills": "Oltin kristallar, Yig'ish effekti, Ochkolar hisobi, Sekundomer",
        "deliverable": "Kristall yig'ganda ovoz chiqadigan va ochko qo'shiladigan o'yin (O'yin)",
        "tools": "Kiber-Yuguruvchi 3.0"
    },
    "16-dars-boss-jangi-va-galaba": {
        "type": "Jonli O'yin Finali",
        "skills": "Katta Robot Boss, Qalqon yoqish, Boss o'qlari, G'alaba qozonish",
        "deliverable": "Bossni yengib oltin kubokni qo'lga kirituvchi to'liq o'yin (O'yin)",
        "tools": "Kiber-Yuguruvchi 4.0"
    },
    "15-dars-dushman-ai-va-tagib": {
        "type": "Jonli O'yin",
        "skills": "Dushman botlari, Patrul qilish (chap-o'ng), Ko'rish radiusi, Ta'qib qilish",
        "deliverable": "Qahramon yaqinlashganda quvadigan aqlli dushman kiber-iti (O'yin)",
        "tools": "Kiber-Yuguruvchi AI"
    },
    "16-dars-level-redaktor-va-ulashish": {
        "type": "Interaktiv Redaktor",
        "skills": "Level Editor, Sichqoncha bilan platforma qo'yish, Level kodi (JSON), Ulashish",
        "deliverable": "O'zi yasagan bosqich kodini sinfdoshiga berib o'ynatish (Redaktor)",
        "tools": "Level Redaktor Studiyasi"
    },
    "17-dars-parollar-jangi-va-brute-force": {
        "type": "Kiber-Xavfsizlik",
        "skills": "Parollar kuchi, Xakerlar qanday buzadi, Lug'at va Brute-Force hujumi, Parol qonunlari",
        "deliverable": "100 yil davomida ham buzib bo'lmaydigan mustahkam kiber-parol formulasi",
        "tools": "Password Strength Checker"
    },
    "18-dars-fishing-va-soxta-havolalar": {
        "type": "Kiber-Xavfsizlik",
        "skills": "Fishing (Phishing), Soxta havolalar, 'Tekin Robux/Telegram Premium' qopqonlari, 2FA",
        "deliverable": "Soxta havolalarni 3 ta belgi orqali fosh qiluvchi Kiber-Qalqon eslatmasi",
        "tools": "URL Detektori"
    },
    "19-dars-zararli-dasturlar-va-troyanlar": {
        "type": "Malware Scanner Studio",
        "skills": "Troyan oti tushunchasi, Zararli dasturlar (Trojan, Stealer, Ransomware), VirusTotal, Sandbox",
        "deliverable": "Malware Scanner da 6 ta shubhali faylni skanerlash va xavf xulosasi (Scanner)",
        "tools": "Malware Scanner Studio"
    }
}

def generate_markdown(course_data):
    md = []
    md.append("# Target International School — Taqvim-Mavzu Ish Rejasi (Syllabus)")
    md.append("**Fan:** IT, Kiberxavfsizlik va Vibecoding (5–11-sinflar)")
    md.append("**O'qituvchi:** Musulmonov Mamarajab (va Ismoiljon Usmonov)")
    md.append("**Muassasa:** Target International School, Yunusobod filiali")
    md.append("**O'quv yili:** 2026–2027 o'quv yili · **Umumiy yuklama:** 31 soat / hafta")
    md.append("**Manba va metodik asos:** O'zbekiston Respublikasi MMTB ilg'or pedagogik standartlari + Xalqaro K-12 STEAM / PBL (Project-Based Learning) integratsiyasi.")
    md.append("")
    md.append("---")
    md.append("")
    md.append("## Haftalik Dars Jadvali va Kohortalar Taqsimoti")
    md.append("")
    md.append("| Kohorta | Yo'nalish | Slot/hafta | Dars Kunlari va Vaqtlari | Auditoriya / Format |")
    md.append("|---|---|:---:|---|---|")
    md.append("| **10A 10B 11A 11B** | Senior AI & Enterprise Kiberxavfsizlik | 5 | Seshanba (5-dars) · Chorshanba (5, 6-dars) · Payshanba (5, 6-dars) | Kompyuter laboratoriyasi |")
    md.append("| **9A 9B** | Junior Vibecoders, Full-Stack & DevOps | 5 | Dushanba (7-dars) · Seshanba (6, 7-dars) · Juma (7, 8-dars) | Kompyuter laboratoriyasi |")
    md.append("| **7A 7B 8A 8B** | Game Dev, Interaktiv Veb & FUT Creator | 5 | Dushanba (8-dars) · Chorshanba (7, 8-dars) · Payshanba (7, 8-dars) | Kompyuter laboratoriyasi |")
    md.append("| **5A 5B 6A 6B** | Junior Creators & Kiber-Xavfsizlik | 6 | Seshanba (3, 4-dars) · Chorshanba (3, 4-dars) · Payshanba (3, 4-dars) | Kompyuter laboratoriyasi |")
    md.append("| **Choice: IT (9–11)** | Kengaytirilgan Tanlov IT / Hackathon | 10 | Dushanba–Juma (9-dars 16:10, 10-dars 16:55) | IT Hub & Loyiha maydoni |")
    md.append("| **JAMI** | **31 soat / hafta** | **31** | **Har bir dars 40 daqiqa (Material 45 daqiqalik bufer bilan)** | — |")
    md.append("")
    md.append("---")
    md.append("")

    for cohort in course_data:
        cid = cohort['id']
        ctitle = cohort['title']['uz']
        cdesc = cohort['desc']['uz']
        badge = cohort.get('badge', '')
        icon = cohort.get('icon', '📌')

        md.append(f"## {icon} {ctitle} ({badge})")
        md.append(f"*{cdesc}*")
        md.append("")

        total_lessons = sum(len(w['lessons']) for w in cohort['weeks'])
        md.append(f"**Jami ishlab chiqilgan amaliy darslar soni:** {total_lessons} ta dars (1–5 haftalar to'liq tayyor)")
        md.append("")

        for week in cohort['weeks']:
            wid = week['id']
            wtitle = week['title']['uz']
            lessons = week['lessons']

            md.append(f"### {wtitle} ({len(lessons)} dars)")
            md.append("")
            md.append("| № | Dars Mavzusi | Soat | Dars Turi | Asosiy Kompetensiyalar va O'rganish Maqsadi | Qo'lga Ushlanadigan Natija (Deliverable) | Interaktiv Vosita / Lab |")
            md.append("|:---:|---|:---:|---|---|---|---|")

            for l in lessons:
                num = l['num']
                title = l['title']['uz']
                lid = l['id']
                comp = COMPETENCIES.get(lid, {
                    "type": "Amaliy",
                    "skills": l.get('lede', {}).get('uz', '')[:80],
                    "deliverable": "Amaliy ish varaqasi va kod",
                    "tools": "VS Code / Brauzer"
                })

                lab_name = l.get('interactive_name', {}).get('uz', '—') if l.get('interactive_name') else '—'
                if l.get('interactive_url'):
                    lab_cell = f"[{lab_name}]({l['interactive_url']})"
                else:
                    lab_cell = lab_name

                prez_link = f"[Prezentatsiya]({l['p_url']})" if l.get('p_url') else "—"
                var_link = f"[Varaqa]({l['v_url']})" if l.get('v_url') else "—"

                md.append(f"| **{num}** | **{title}**<br><sub>{prez_link} · {var_link}</sub> | 1 | `{comp['type']}` | {comp['skills']} | {comp['deliverable']} | {lab_cell} |")

            md.append("")

        # Istiqbolli keyingi haftalar (6–9 hafta)
        md.append(f"### 🚀 Kelgusi Haftalar va 1-Chorak Yakuni ({cid})")
        md.append("")
        md.append("| Hafta | Mavzular Yo'nalishi | Soat | Shakl va Kutilayotgan Natija |")
        md.append("|:---:|---|:---:|---|")
        if cid == "10-11-sinf":
            md.append("| **6-hafta** | Cloud Infratuzilma Xavfsizligi va Kubernetes Zero Trust Hardening | 5 | K8s tarmoq siyosatlari va klaster mudofaasi |")
            md.append("| **7-hafta** | Kiber-Tahdidlarni Razvedka Qilish (OSINT & Threat Intelligence) | 5 | Shubhali domenlar va IP larni real-vaqt tergov qilish |")
            md.append("| **8-hafta** | Oraliq Nazorat va Enterprise Kiberxavfsizlik Auditi | 5 | Amaliy sinov imtihoni (Midterm Assessment) |")
            md.append("| **9-hafta** | 1-Chorak Yakuniy Demo Day: Xavfsiz AI Tizimi Taqdimoti | 5 | Hakamlar hay'atiga himoyalangan arxitekturani namoyish etish |")
        elif cid == "9-sinf":
            md.append("| **6-hafta** | Mikroxizmatlar Xavfsizligi va API Shlyuzlari (Gateway) | 5 | Rate-limit va JWT tekshiruvchi yagona shlyuz arxitekturasi |")
            md.append("| **7-hafta** | Avtomatlashtirilgan Kiber-Zondlar va Zaifliklarni Skanning Qilish | 5 | Loyihani CI/CD konveyerida avtomatik tekshiruvchi bot |")
            md.append("| **8-hafta** | Oraliq Nazorat: Full-Stack Kiber-Ilova Himoyasi | 5 | Amaliy sinov imtihoni (Midterm Assessment) |")
            md.append("| **9-hafta** | 1-Chorak Demo Day: Tijoriy Full-Stack Loyiha Taqdimoti | 5 | Global internetdagi tayyor mahsulot taqdimoti |")
        elif cid == "7-8-sinf":
            md.append("| **6-hafta** | Kiber-Turnir Platformasi: Ko'p O'yinchili Veb-Soketlar (Multiplayer) | 5 | WebSocket orqali 2 nafar o'quvchi jonli o'ynashi |")
            md.append("| **7-hafta** | O'yin Xavfsizligi: Chitlar va Soxta Rekordlarga Qarshi Himoya | 5 | Brauzer konsolida ochko ko'paytirishni to'suvchi algoritm |")
            md.append("| **8-hafta** | Oraliq Nazorat: Kiber-Arkada Final Sinovi | 5 | Amaliy o'yin sinovi va portfolioga qo'shish |")
            md.append("| **9-hafta** | 1-Chorak Demo Day: Mustaqil Kiber-O'yin Taqdimoti | 5 | Maktab doirasidagi Jonli Game Jam chempionati |")
        elif cid == "5-6-sinf":
            md.append("| **6-hafta** | Kiber-Xavfsizlik Ertaklari: Kiber-Firibgarlar Qopqoni | 6 | Yangi xakerlik hiylalarini fosh etuvchi detektiv kvest |")
            md.append("| **7-hafta** | O'z Xavfsiz O'yiningni Yarat: O'quvchi Ijodiy Laboratoriyasi | 6 | Qahramon, to'siqlar va parollar bilan to'liq sarguzasht |")
            md.append("| **8-hafta** | Oraliq Nazorat: Kiber-Qalqon Viktorinasi | 6 | O'rganilgan barcha xavfsizlik qoidalari bo'yicha test |")
            md.append("| **9-hafta** | 1-Chorak Demo Day: Sehrli Kiber-Ko'rgazma | 6 | Ota-onalar va tengdoshlarga eng yaxshi o'yinlar namoyishi |")
        md.append("")
        md.append("---")
        md.append("")

    # Pedagogik Baholash va Metodika
    md.append("## Pedagogik Standart va Baholash Nizomi")
    md.append("")
    md.append("### 1. Darsning 5 Bosqichli 40 Daqiqalik Reglamenti")
    md.append("1. **Tashkiliy qism & Kirish (0–3 daqiqa):** Salomlashish, davomat, maqsadni e'lon qilish.")
    md.append("2. **Aqliy hujum & Muammo qo'yish (3–7 daqiqa):** Real hayotiy keys (buyurtmachi muammosi, xakerlik xuruji).")
    md.append("3. **Yangi mavzu bayoni (7–23 daqiqa):** Inline arxitektura sxemalari, taqqoslashlar, mexanizm tahlili.")
    md.append("4. **Mustahkamlash & Amaliy ish (23–36 daqiqa):** 11–13 daqiqalik qat'iy taymer ostida mustaqil laboratoriya/kod.")
    md.append("5. **Xulosa, Baholash & Uy vazifasi (36–40 daqiqa):** 10 ballik mezon asosida formativ baholash va topshiriq.")
    md.append("")
    md.append("### 2. 10 Ballik Baholash Mezoni")
    md.append("- **A'lo (9–10 ball):** Nazariy mexanizm to'liq tushunilgan, amaliy laboratoriya/studio vazifasi 100% bajarilgan, ish varaqasi to'liq to'ldirilgan.")
    md.append("- **Yaxshi (7–8 ball):** Asosiy tushunchalar o'zlashtirilgan, amaliy topshiriqda mayda kamchiliklar bor, ish varaqasi 80% to'ldirilgan.")
    md.append("- **Qoniqarli (5–6 ball):** Tushunchalarda chalkashlik bor, amaliy vazifa o'qituvchi yordamida qisman bajarilgan.")
    md.append("")
    md.append("---")
    md.append("**Tasdiqlayman:**")
    md.append("")
    md.append("Target International School IT & Kiberxavfsizlik o'qituvchisi: **Musulmonov Mamarajab** _________")
    md.append("")
    md.append("Maktab Metodbirlashma Rahbari: ________________________ Sana: «___» _________ 2026-yil")

    return "\n".join(md)

def generate_html(course_data):
    # Trilingual and interactive HTML
    return f"""<!DOCTYPE html>
<html lang="uz" data-theme="dark">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Target International School — Taqvim-Mavzu Ish Rejasi (Syllabus)</title>
  <link rel="icon" href="assets/target-logo.png" type="image/png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;600&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="assets/brand.css">
  <style>
    :root {{
      --bg: #090d16;
      --card-bg: #111827;
      --card-border: #1f2937;
      --text: #f3f4f6;
      --muted: #9ca3af;
      --accent: #2563eb;
      --accent-hover: #1d4ed8;
      --gold: #f59e0b;
      --green: #10b981;
      --purple: #8b5cf6;
      --red: #ef4444;
      --font-sans: 'Plus Jakarta Sans', system-ui, -apple-system, sans-serif;
      --font-mono: 'JetBrains Mono', monospace;
    }}

    [data-theme="light"] {{
      --bg: #f8fafc;
      --card-bg: #ffffff;
      --card-border: #e2e8f0;
      --text: #0f172a;
      --muted: #64748b;
      --accent: #2563eb;
      --accent-hover: #1d4ed8;
    }}

    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      font-family: var(--font-sans);
      background-color: var(--bg);
      color: var(--text);
      line-height: 1.5;
      padding-bottom: 60px;
    }}

    .container {{
      max-width: 1400px;
      margin: 0 auto;
      padding: 0 24px;
    }}

    /* Header */
    header.reja-header {{
      background: rgba(17, 24, 39, 0.85);
      backdrop-filter: blur(12px);
      border-bottom: 1px solid var(--card-border);
      position: sticky;
      top: 0;
      z-index: 100;
      padding: 16px 0;
    }}
    [data-theme="light"] header.reja-header {{
      background: rgba(255, 255, 255, 0.9);
    }}

    .header-inner {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 16px;
      flex-wrap: wrap;
    }}

    .brand-wrap {{
      display: flex;
      align-items: center;
      gap: 14px;
    }}
    .brand-logo {{
      width: 44px;
      height: 44px;
      border-radius: 10px;
      object-fit: contain;
      background: #ffffff;
      padding: 4px;
      box-shadow: 0 4px 12px rgba(0,0,0,0.15);
    }}
    .brand-title h1 {{
      font-size: 1.15rem;
      font-weight: 800;
      letter-spacing: -0.02em;
      color: var(--text);
    }}
    .brand-title p {{
      font-size: 0.8rem;
      color: var(--muted);
      font-weight: 500;
    }}

    .header-actions {{
      display: flex;
      align-items: center;
      gap: 10px;
    }}

    .btn {{
      display: inline-flex;
      align-items: center;
      gap: 8px;
      padding: 8px 14px;
      border-radius: 8px;
      font-size: 0.85rem;
      font-weight: 600;
      text-decoration: none;
      border: 1px solid var(--card-border);
      background: var(--card-bg);
      color: var(--text);
      cursor: pointer;
      transition: all 0.2s ease;
    }}
    .btn:hover {{
      border-color: var(--accent);
      color: var(--accent);
      transform: translateY(-1px);
    }}
    .btn-primary {{
      background: var(--accent);
      color: #ffffff;
      border-color: var(--accent);
    }}
    .btn-primary:hover {{
      background: var(--accent-hover);
      color: #ffffff;
    }}

    /* Hero Banner */
    .hero {{
      padding: 36px 0 24px 0;
    }}
    .hero-badge {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 4px 10px;
      border-radius: 999px;
      background: rgba(37, 99, 235, 0.12);
      border: 1px solid rgba(37, 99, 235, 0.3);
      color: var(--accent);
      font-size: 0.8rem;
      font-weight: 700;
      margin-bottom: 12px;
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }}
    .hero h2 {{
      font-size: 2.2rem;
      font-weight: 800;
      line-height: 1.2;
      letter-spacing: -0.03em;
      margin-bottom: 12px;
    }}
    .hero p {{
      font-size: 1.05rem;
      color: var(--muted);
      max-width: 900px;
      line-height: 1.6;
    }}

    /* Stat Cards */
    .stats-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
      gap: 16px;
      margin: 24px 0;
    }}
    .stat-card {{
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: 12px;
      padding: 18px 20px;
      display: flex;
      align-items: center;
      gap: 16px;
    }}
    .stat-icon {{
      font-size: 2rem;
      background: rgba(37, 99, 235, 0.1);
      width: 52px;
      height: 52px;
      display: flex;
      align-items: center;
      justify-content: center;
      border-radius: 12px;
    }}
    .stat-val {{
      font-size: 1.5rem;
      font-weight: 800;
      color: var(--text);
    }}
    .stat-lbl {{
      font-size: 0.8rem;
      color: var(--muted);
      font-weight: 500;
    }}

    /* Filter Controls */
    .controls-bar {{
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: 12px;
      padding: 12px 16px;
      margin-bottom: 24px;
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      justify-content: space-between;
      gap: 12px;
    }}
    .cohort-pills {{
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
    }}
    .pill-btn {{
      padding: 8px 14px;
      border-radius: 8px;
      font-size: 0.85rem;
      font-weight: 600;
      border: 1px solid var(--card-border);
      background: transparent;
      color: var(--muted);
      cursor: pointer;
      transition: all 0.2s;
    }}
    .pill-btn:hover {{
      color: var(--text);
      border-color: var(--muted);
    }}
    .pill-btn.active {{
      background: var(--accent);
      color: #ffffff;
      border-color: var(--accent);
    }}

    .search-box {{
      position: relative;
      min-width: 260px;
    }}
    .search-input {{
      width: 100%;
      padding: 8px 12px 8px 36px;
      border-radius: 8px;
      border: 1px solid var(--card-border);
      background: var(--bg);
      color: var(--text);
      font-size: 0.85rem;
      outline: none;
    }}
    .search-input:focus {{
      border-color: var(--accent);
    }}
    .search-icon {{
      position: absolute;
      left: 10px;
      top: 50%;
      transform: translateY(-50%);
      color: var(--muted);
      pointer-events: none;
    }}

    /* Cohort Section */
    .cohort-section {{
      margin-bottom: 48px;
    }}
    .cohort-header {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 14px 18px;
      background: rgba(37, 99, 235, 0.08);
      border: 1px solid rgba(37, 99, 235, 0.2);
      border-radius: 12px 12px 0 0;
      margin-top: 24px;
    }}
    .cohort-header-title {{
      display: flex;
      align-items: center;
      gap: 12px;
    }}
    .cohort-header-title h3 {{
      font-size: 1.25rem;
      font-weight: 800;
    }}
    .cohort-header-desc {{
      font-size: 0.85rem;
      color: var(--muted);
      margin-top: 2px;
    }}

    /* Table Styling */
    .table-wrap {{
      overflow-x: auto;
      border: 1px solid var(--card-border);
      border-top: none;
      border-radius: 0 0 12px 12px;
      background: var(--card-bg);
      margin-bottom: 24px;
    }}
    table.reja-table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 0.88rem;
      text-align: left;
    }}
    table.reja-table th {{
      background: rgba(0,0,0,0.15);
      color: var(--text);
      padding: 12px 16px;
      font-weight: 700;
      font-size: 0.8rem;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      border-bottom: 1px solid var(--card-border);
    }}
    [data-theme="light"] table.reja-table th {{
      background: #f1f5f9;
    }}
    table.reja-table td {{
      padding: 14px 16px;
      border-bottom: 1px solid var(--card-border);
      vertical-align: middle;
    }}
    table.reja-table tr:last-child td {{
      border-bottom: none;
    }}
    table.reja-table tr:hover td {{
      background: rgba(255, 255, 255, 0.02);
    }}
    [data-theme="light"] table.reja-table tr:hover td {{
      background: #f8fafc;
    }}

    .cell-num {{
      font-family: var(--font-mono);
      font-weight: 700;
      color: var(--accent);
      white-space: nowrap;
    }}
    .cell-title strong {{
      display: block;
      color: var(--text);
      font-size: 0.92rem;
      margin-bottom: 4px;
    }}
    .cell-links {{
      display: flex;
      gap: 8px;
      font-size: 0.78rem;
    }}
    .cell-links a {{
      color: var(--muted);
      text-decoration: none;
      display: inline-flex;
      align-items: center;
      gap: 3px;
    }}
    .cell-links a:hover {{
      color: var(--accent);
      text-decoration: underline;
    }}

    .badge-type {{
      display: inline-block;
      padding: 3px 8px;
      border-radius: 6px;
      font-size: 0.75rem;
      font-weight: 600;
      background: rgba(139, 92, 246, 0.12);
      color: var(--purple);
      border: 1px solid rgba(139, 92, 246, 0.25);
    }}
    .badge-lab {{
      display: inline-flex;
      align-items: center;
      gap: 4px;
      padding: 4px 10px;
      border-radius: 6px;
      font-size: 0.8rem;
      font-weight: 700;
      background: rgba(16, 185, 129, 0.12);
      color: var(--green);
      border: 1px solid rgba(16, 185, 129, 0.25);
      text-decoration: none;
      transition: all 0.2s;
    }}
    .badge-lab:hover {{
      background: var(--green);
      color: #ffffff;
    }}

    .deliverable-tag {{
      display: inline-block;
      font-size: 0.82rem;
      color: var(--text);
      font-weight: 500;
      background: rgba(245, 158, 11, 0.08);
      border-left: 3px solid var(--gold);
      padding: 4px 8px;
      border-radius: 0 4px 4px 0;
    }}

    /* Official Sign-off */
    .signoff-box {{
      margin-top: 48px;
      padding: 24px;
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: 12px;
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 24px;
    }}
    .sign-row {{
      font-size: 0.9rem;
      line-height: 1.8;
    }}
    .sign-line {{
      display: inline-block;
      width: 180px;
      border-bottom: 1px solid var(--muted);
      margin: 0 8px;
    }}

    /* Print Stylesheet */
    @media print {{
      header.reja-header, .controls-bar, .header-actions, .theme-toggle, .btn {{
        display: none !important;
      }}
      body {{
        background: #ffffff !important;
        color: #000000 !important;
        font-size: 8.5pt !important;
      }}
      .container {{
        max-width: 100% !important;
        padding: 0 !important;
      }}
      .table-wrap {{
        border: 1px solid #000000 !important;
        page-break-inside: auto;
      }}
      table.reja-table th, table.reja-table td {{
        border: 1px solid #cccccc !important;
        padding: 6px 8px !important;
        color: #000000 !important;
      }}
      .hero h2 {{
        font-size: 16pt !important;
        color: #000000 !important;
      }}
      .cohort-section {{
        page-break-before: always;
      }}
      .cohort-section:first-of-type {{
        page-break-before: avoid;
      }}
      .signoff-box {{
        border: 1px solid #000000 !important;
        page-break-inside: avoid;
      }}
    }}
  </style>
</head>
<body>

  <!-- Sticky Header -->
  <header class="reja-header">
    <div class="container header-inner">
      <div class="brand-wrap">
        <img src="assets/target-logo.png" alt="Target Logo" class="brand-logo">
        <div class="brand-title">
          <h1 data-ru="Target International School · Учебный План" data-en="Target International School · Syllabus">Target International School · Taqvim Ish Rejasi</h1>
          <p data-ru="IT и Кибербезопасность · 2026–2027 учебный год" data-en="IT & Cybersecurity · Academic Year 2026–2027">IT va Kiberxavfsizlik · 2026–2027 o'quv yili</p>
        </div>
      </div>
      <div class="header-actions">
        <a href="index.html" class="btn">
          <span>🏠</span>
          <span data-ru="Портал уроков" data-en="Course Portal">Bosh Sahifa</span>
        </a>
        <a href="TARGET_ISH_REJASI_2026_2027.docx" download class="btn" style="border-color: var(--accent); color: var(--accent); background: rgba(37,99,235,0.1);">
          <span>📥</span>
          <span data-ru="Скачать DOCX" data-en="Download DOCX">DOCX Yuklab Olish</span>
        </a>
        <button onclick="window.print()" class="btn btn-primary">
          <span>🖨️</span>
          <span data-ru="Печать / PDF" data-en="Print / PDF">Chop etish / PDF</span>
        </button>
        <button id="langBtn" class="btn">
          <span>🌐</span>
          <span id="langLabel">UZ</span>
        </button>
        <button id="themeBtn" class="btn">
          <span id="themeIcon">☀️</span>
        </button>
      </div>
    </div>
  </header>

  <!-- Hero Section -->
  <main class="container">
    <section class="hero">
      <div class="hero-badge" data-ru="Официальная Учебная Программа" data-en="Official Curriculum Specification">Rasmiy Taqvim-Mavzu Rejasi</div>
      <h2 data-ru="Календарно-Тематический План по IT и Кибербезопасности" data-en="Syllabus & Course Curriculum: IT & Cybersecurity">IT, Kiberxavfsizlik va Vibecoding Bo'yicha Taqvim-Mavzu Ish Rejasi</h2>
      <p data-ru="Единая сквозная программа обучения для 5–11 классов. Ориентирована на современные стандарты индустрии: веб-разработка, AI-агенты, этичный хакинг, облачный деплой и практические интерактивные лаборатории." data-en="Unified curriculum for grades 5–11. Engineered to modern industry standards: full-stack web, AI agents, ethical hacking, cloud deployment, and hands-on interactive labs.">
        Target International School (Yunusobod filiali) 5–11-sinf o'quvchilari uchun yagona ta'lim dasturi. Nazariy bilimlar 20%, chuqur amaliy laboratoriyalar, interaktiv trenajyorlar va kiber-loyihalar 80% formatida tashkil etilgan.
      </p>

      <!-- Stat Cards -->
      <div class="stats-grid">
        <div class="stat-card">
          <div class="stat-icon">🎓</div>
          <div>
            <div class="stat-val">4 ta</div>
            <div class="stat-lbl" data-ru="Специализированные когорты" data-en="Specialized Cohorts">Ixtisoslashgan Kohorta</div>
          </div>
        </div>
        <div class="stat-card">
          <div class="stat-icon">⚡</div>
          <div>
            <div class="stat-val">31 soat</div>
            <div class="stat-lbl" data-ru="Часов в неделю" data-en="Hours Per Week">Haftalik O'quv Yuklamasi</div>
          </div>
        </div>
        <div class="stat-card">
          <div class="stat-icon">🛠️</div>
          <div>
            <div class="stat-val">95+ ta</div>
            <div class="stat-lbl" data-ru="Готовых уроков и лаб" data-en="Ready Lessons & Labs">Tayyor Amaliy Darslar</div>
          </div>
        </div>
        <div class="stat-card">
          <div class="stat-icon">🛡️</div>
          <div>
            <div class="stat-val">100%</div>
            <div class="stat-lbl" data-ru="Практика и симуляторы" data-en="Interactive Studios">Interaktiv Trenajyorlar</div>
          </div>
        </div>
      </div>

      <!-- DOCX Download Center Banner -->
      <div style="background: var(--card-bg); border: 1px solid var(--card-border); border-radius: 12px; padding: 16px 20px; margin-top: 20px; display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 14px;">
        <div>
          <div style="font-weight: 800; font-size: 0.95rem; color: var(--text); display: flex; align-items: center; gap: 8px;">
            <span>📄</span>
            <span data-ru="Официальные документы Word (.docx) для администрации:" data-en="Official Word documents (.docx) for administration:">Maktab ma'muriyati uchun rasmiy Word (.docx) hujjatlari:</span>
          </div>
          <div style="font-size: 0.8rem; color: var(--muted); margin-top: 3px;" data-ru="Готовые утверждённые календарно-тематические планы для печати и сдачи" data-en="Ready certified calendar-thematic plans for print and submission">
            Chop etish va tasdiqqa topshirish uchun tayyor taqvim-mavzu rejalari
          </div>
        </div>
        <div style="display: flex; flex-wrap: wrap; gap: 8px;">
          <a href="TARGET_ISH_REJASI_2026_2027.docx" download class="btn btn-primary" style="font-size: 0.82rem; padding: 6px 12px;">
            <span>📥</span> <span>Barcha Sinflar (.docx)</span>
          </a>
          <a href="assets/ISH_REJASI_10_11_SINF.docx" download class="btn" style="font-size: 0.82rem; padding: 6px 12px;">
            <span>🎓</span> <span>10–11-sinf (.docx)</span>
          </a>
          <a href="assets/ISH_REJASI_9_SINF.docx" download class="btn" style="font-size: 0.82rem; padding: 6px 12px;">
            <span>⚡</span> <span>9-sinf (.docx)</span>
          </a>
          <a href="assets/ISH_REJASI_7_8_SINF.docx" download class="btn" style="font-size: 0.82rem; padding: 6px 12px;">
            <span>🎮</span> <span>7–8-sinf (.docx)</span>
          </a>
          <a href="assets/ISH_REJASI_5_6_SINF.docx" download class="btn" style="font-size: 0.82rem; padding: 6px 12px;">
            <span>🛡️</span> <span>5–6-sinf (.docx)</span>
          </a>
        </div>
      </div>
    </section>

    <!-- Controls Bar -->
    <div class="controls-bar">
      <div class="cohort-pills" id="cohortPills">
        <button class="pill-btn active" data-filter="all" data-ru="Все Классы" data-en="All Grades">Barcha Sinflar</button>
        <button class="pill-btn" data-filter="10-11-sinf">🎓 10–11-sinf (Senior AI)</button>
        <button class="pill-btn" data-filter="9-sinf">⚡ 9-sinf (Full-Stack & DevOps)</button>
        <button class="pill-btn" data-filter="7-8-sinf">🎮 7–8-sinf (Game Dev & FUT)</button>
        <button class="pill-btn" data-filter="5-6-sinf">🛡️ 5–6-sinf (Junior Creators)</button>
      </div>
      <div class="search-box">
        <span class="search-icon">🔍</span>
        <input type="text" id="searchInput" class="search-input" placeholder="Mavzu yoki vositani qidirish..." data-ru="Поиск темы или инструмента..." data-en="Search topic or tool...">
      </div>
    </div>

    <!-- Cohort Tables Section -->
    <div id="cohortsContainer">
""" + build_html_cohorts(course_data) + """
    </div>

    <!-- Official Sign-off Box -->
    <section class="signoff-box">
      <div class="sign-row">
        <strong>O'qituvchi / Tuzuvchi:</strong><br>
        <span>Musulmonov Mamarajab</span> · IT & Kiberxavfsizlik o'qituvchisi<br>
        <span>Imzo: <span class="sign-line"></span> Sana: «___» ________ 2026-y.</span>
      </div>
      <div class="sign-row">
        <strong>Tasdiqlayman:</strong><br>
        <span>Target International School Metodbirlashma Rahbari</span><br>
        <span>Imzo: <span class="sign-line"></span> Sana: «___» ________ 2026-y.</span>
      </div>
    </section>
  </main>

  <script>
    // Theme toggle
    const themeBtn = document.getElementById('themeBtn');
    const themeIcon = document.getElementById('themeIcon');
    let currentTheme = localStorage.getItem('theme') || 'dark';
    document.documentElement.setAttribute('data-theme', currentTheme);
    themeIcon.textContent = currentTheme === 'dark' ? '☀️' : '🌙';

    themeBtn.addEventListener('click', () => {
      currentTheme = currentTheme === 'dark' ? 'light' : 'dark';
      document.documentElement.setAttribute('data-theme', currentTheme);
      localStorage.setItem('theme', currentTheme);
      themeIcon.textContent = currentTheme === 'dark' ? '☀️' : '🌙';
    });

    // Language switcher (UZ -> RU -> EN)
    const langBtn = document.getElementById('langBtn');
    const langLabel = document.getElementById('langLabel');
    const langs = ['uz', 'ru', 'en'];
    let langIndex = 0;

    // Cache original UZ texts
    document.querySelectorAll('[data-ru]').forEach(el => {
      el.setAttribute('data-uz', el.textContent.trim());
    });

    langBtn.addEventListener('click', () => {
      langIndex = (langIndex + 1) % langs.length;
      const lang = langs[langIndex];
      langLabel.textContent = lang.toUpperCase();

      document.querySelectorAll('[data-' + lang + ']').forEach(el => {
        el.textContent = el.getAttribute('data-' + lang);
      });

      // Placeholders
      document.querySelectorAll('[placeholder]').forEach(input => {
        if (input.getAttribute('data-' + lang)) {
          input.placeholder = input.getAttribute('data-' + lang);
        }
      });
    });

    // Cohort pill filtering
    const pills = document.querySelectorAll('.pill-btn');
    const sections = document.querySelectorAll('.cohort-section');
    pills.forEach(pill => {
      pill.addEventListener('click', () => {
        pills.forEach(p => p.classList.remove('active'));
        pill.classList.add('active');
        const filter = pill.getAttribute('data-filter');
        sections.forEach(sec => {
          if (filter === 'all' || sec.id === 'sec-' + filter) {
            sec.style.display = '';
          } else {
            sec.style.display = 'none';
          }
        });
      });
    });

    // Search filter
    const searchInput = document.getElementById('searchInput');
    searchInput.addEventListener('input', (e) => {
      const q = e.target.value.toLowerCase().trim();
      document.querySelectorAll('.reja-table tbody tr').forEach(row => {
        const text = row.textContent.toLowerCase();
        if (!q || text.includes(q)) {
          row.style.display = '';
        } else {
          row.style.display = 'none';
        }
      });
    });
  </script>
</body>
</html>
"""

def build_html_cohorts(course_data):
    html = []
    for cohort in course_data:
        cid = cohort['id']
        ctitle = cohort['title']['uz']
        cdesc = cohort['desc']['uz']
        badge = cohort.get('badge', '')
        icon = cohort.get('icon', '📌')

        html.append(f"""
      <div class="cohort-section" id="sec-{cid}">
        <div class="cohort-header">
          <div class="cohort-header-title">
            <span style="font-size: 1.8rem;">{icon}</span>
            <div>
              <h3>{ctitle} <span class="badge-type" style="margin-left:8px;">{badge}</span></h3>
              <div class="cohort-header-desc">{cdesc}</div>
            </div>
          </div>
        </div>
        <div class="table-wrap">
          <table class="reja-table">
            <thead>
              <tr>
                <th style="width: 50px;">№</th>
                <th style="width: 280px;" data-ru="Тема Урока" data-en="Lesson Topic">Dars Mavzusi</th>
                <th style="width: 60px;" data-ru="Часы" data-en="Hours">Soat</th>
                <th style="width: 140px;" data-ru="Тип" data-en="Format">Dars Turi</th>
                <th data-ru="Компетенции и Цели" data-en="Skills & Competencies">Kompetensiyalar va Maqsad</th>
                <th style="width: 240px;" data-ru="Результат (Deliverable)" data-en="Tangible Deliverable">Kutilayotgan Natija</th>
                <th style="width: 160px;" data-ru="Инструмент / Лаба" data-en="Interactive Tool">Trenajyor / Lab</th>
              </tr>
            </thead>
            <tbody>
""")
        for week in cohort['weeks']:
            wtitle = week['title']['uz']
            html.append(f"""
              <tr style="background: rgba(37, 99, 235, 0.04);">
                <td colspan="7" style="font-weight: 800; color: var(--accent); padding: 10px 16px; border-bottom: 2px solid var(--card-border);">
                  📅 {wtitle}
                </td>
              </tr>
""")
            for l in week['lessons']:
                num = l['num']
                title = l['title']['uz']
                lid = l['id']
                comp = COMPETENCIES.get(lid, {
                    "type": "Amaliy",
                    "skills": l.get('lede', {}).get('uz', '')[:80],
                    "deliverable": "Amaliy ish varaqasi va kod",
                    "tools": "VS Code / Brauzer"
                })

                lab_btn = ""
                if l.get('interactive_url'):
                    lab_name = l.get('interactive_name', {}).get('uz', 'Interaktiv Lab')
                    lab_btn = f"""<a href="{l['interactive_url']}" target="_blank" class="badge-lab"><span>⚡</span> {lab_name}</a>"""
                elif comp.get('tools'):
                    lab_btn = f"""<span style="font-size:0.8rem; color:var(--muted);">{comp['tools']}</span>"""

                p_link = f"""<a href="{l['p_url']}" target="_blank"><span>📊</span> Slayd</a>""" if l.get('p_url') else ""
                v_link = f"""<a href="{l['v_url']}" target="_blank"><span>📝</span> Varaqa</a>""" if l.get('v_url') else ""

                html.append(f"""
              <tr>
                <td class="cell-num">{num}</td>
                <td class="cell-title">
                  <strong>{title}</strong>
                  <div class="cell-links">
                    {p_link}
                    {v_link}
                  </div>
                </td>
                <td style="font-family: var(--font-mono); font-weight:600;">1</td>
                <td><span class="badge-type">{comp['type']}</span></td>
                <td style="color: var(--muted); font-size: 0.84rem;">{comp['skills']}</td>
                <td><div class="deliverable-tag">{comp['deliverable']}</div></td>
                <td>{lab_btn}</td>
              </tr>
""")
        html.append("""
            </tbody>
          </table>
        </div>
      </div>
""")
    return "".join(html)

def main():
    print("Loading COURSE_DATA from index.html...")
    course_data = load_course_data()
    print(f"Loaded {len(course_data)} cohorts.")

    print("Generating REJA.md...")
    md_content = generate_markdown(course_data)
    with open("REJA.md", "w", encoding="utf-8") as f:
        f.write(md_content)
    print("REJA.md generated successfully!")

    print("Generating reja.html...")
    html_content = generate_html(course_data)
    with open("reja.html", "w", encoding="utf-8") as f:
        f.write(html_content)
    print("reja.html generated successfully!")

if __name__ == "__main__":
    main()
