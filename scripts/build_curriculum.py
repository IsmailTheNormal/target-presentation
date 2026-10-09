#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Target International School — Yillik Taqvim-Mavzu Ish Rejasi Generator (36 Hafta / 4 Chorak)
Ushbu skript repo ichidagi barcha darslar va yillik o'quv dasturi asosida
rasmiy REJA.md va interaktiv, chop etiladigan reja.html ni to'liq generatsiya qiladi.
"""

import json
import re
import os
import sys

# Import annual data
sys.path.append(os.path.dirname(__file__))
from annual_curriculum_data import QUARTERS_INFO, ANNUAL_COHORTS_DATA, VIBECODING_108_MASTER

# Rich competencies dictionary for weeks 1-5 completed lessons
COMPETENCIES = {
    # 10-11-sinf
    "01-dars-ai-nima": {
        "type": "Nazariy-Amaliy",
        "skills": "AI modellari turlari, LLM generatsiyasi, Prompt sintaksisi va prompt injiniringi",
        "deliverable": "AI vositalari taqqoslash tahlili va birinchi tizimli so'rov konspekti",
        "tools": "ChatGPT, Claude, Perplexity"
    },
    "02-dars-vibecoding-asoslari": {
        "type": "Amaliy",
        "skills": "UI/UX asoslari, Frontend va Backend arxitekturasi, Semantik HTML5 teglari",
        "deliverable": "Mahsulot sahifasi uchun vizual bloklar maketi va DOM daraxti",
        "tools": "HTML5, CSS3, Chrome DevTools"
    },
    "03-dars-it-dunyosi-kod-va-cloud": {
        "type": "Nazariy-Amaliy",
        "skills": "Internet qanday ishlaydi, DNS, HTTP, Client-Server modeli, Cloud hosting va serverlar",
        "deliverable": "Internet ma'lumotlar marshruti sxemasi va tarmoq auditi",
        "tools": "Terminal, ping, traceroute, Cloudflare"
    },
    "04-dars-frilans-buyurtma-ui": {
        "type": "Amaliy Loyiha",
        "skills": "Texnik topshiriq (PRD) tahlili, CSS Grid va Flexbox, Moslashuvchan dizayn",
        "deliverable": "Mijoz talabi bo'yicha tayyorlangan Landing Page UI maketi",
        "tools": "VS Code, CSS Flexbox/Grid"
    },
    "05-dars-frilans-mantiq-js": {
        "type": "Amaliy Loyiha",
        "skills": "JavaScript DOM manipulyatsiyasi, Hodisalar (Events), Dark/Light rejim almashtirish",
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
        "skills": "Autentifikatsiya, Parollarni xeshlash, Xavfsiz tokenlar, .env maxfiy kalitlar",
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

    # 9-sinf
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
        "type": "Database Asos",
        "skills": "Relyatsion ma'lumotlar bazasi, SQL so'rovlari (SELECT, INSERT, UPDATE, DELETE), Baza sxemasi",
        "deliverable": "Mahsulotlar va foydalanuvchilar jadvaliga ega SQLite ma'lumotlar bazasi",
        "tools": "SQLite, DBeaver / DB Browser, SQL"
    },
    "19-dars-backend-express-va-rest-api": {
        "type": "Backend Muhandislik",
        "skills": "Node.js, Express framework, REST API marshrutlash (Routing), JSON so'rov/javob, Middleware",
        "deliverable": "Ma'lumotlar bazasiga ulangan to'liq CRUD Express backend serveri",
        "tools": "Node.js, Express, Postman"
    },
    "20-dars-fullstack-deploy-va-demo-day": {
        "type": "Full-Stack Deploy",
        "skills": "Frontend va Backendni integratsiya qilish, CORS sozlash, Bulutli deploy, Domen va SSL",
        "deliverable": "Internetda real ishlayotgan to'liq Full-Stack loyiha va mobil QR kod",
        "tools": "Render / Railway, Vercel, Supabase"
    },
    "21-dars-linux-server-hardening-va-ssh": {
        "type": "Server Xavfsizligi",
        "skills": "Linux operatsion tizimi, SSH kalitlar bilan kirish, Parolli kirishni o'chirish, UFW fayrvoll, Fail2ban",
        "deliverable": "Brute-force hujumlaridan to'liq himoyalangan xavfsiz Linux serveri",
        "tools": "Ubuntu Linux, OpenSSH, UFW, Fail2ban"
    },
    "22-dars-tarmoq-xavfsizligi-va-wireshark": {
        "type": "Tarmoq Tahlili",
        "skills": "OSI modeli, TCP/IP stek, Paketlar tuzilishi, Wireshark tahlili, Nmap port skanerlash",
        "deliverable": "Tarmoq trafigi tahlili protokoli va ochiq zaif portlar hisoboti",
        "tools": "Wireshark, Nmap, Packet Analyzer"
    },
    "23-dars-veb-zaifliklari-va-owasp-top-10": {
        "type": "Kiber-Himoya",
        "skills": "OWASP Top 10, SQL Injection (SQLi), Cross-Site Scripting (XSS), Kiruvchi ma'lumotlarni tozalash",
        "deliverable": "SQLi va XSS hujumlariga qarshi mustahkamlangan xavfsiz forma kodi",
        "tools": "OWASP ZAP, DVWA / WebGoat, Burp Suite"
    },
    "24-dars-autentifikatsiya-xavfsizligi-va-jwt": {
        "type": "Autentifikatsiya",
        "skills": "Autentifikatsiya vs Avtorizatsiya, JWT (JSON Web Tokens), Parollarni xeshlash (bcrypt), 2FA/TOTP",
        "deliverable": "Xavfsiz tokenli avtorizatsiya va ikki bosqichli tasdiqlash moduli",
        "tools": "JWT.io, bcrypt, Speakeasy TOTP"
    },
    "25-dars-kiber-hujum-simulyatsiyasi-va-ctf": {
        "type": "CTF Musobaqa",
        "skills": "Red Team vs Blue Team konsepsiyasi, Zaifliklarni topish, Bayroqni qo'lga kiritish (CTF)",
        "deliverable": "CTF platformasida topilgan 5 ta bayroq va mudofaa hisoboti",
        "tools": "CTFd, Kali Linux, Web Scanner"
    },

    # 7-8-sinf
    "07-dars-flexbox-va-grid-maketi": {
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

    # 5-6-sinf
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
        "tools": "Level Designer"
    },
    "09-dars-ovoz-va-effektlar-sfx": {
        "type": "Ovoz Sehri",
        "skills": "SFX tovushlar (Sakrash, Tangalar, Lazer), Fon musiqasi, Atmosfera",
        "deliverable": "O'yin harakatlariga moslashtirilgan ovozlar to'plami",
        "tools": "AI Audio FX"
    },
    "10-dars-aqlli-npc-va-dialoglar": {
        "type": "Aqlli NPC",
        "skills": "Tarmoqlanuvchi savol-javob, Maslahatchi sehrgar, Kvest topshiriqlari",
        "deliverable": "O'yinchiga topshiriq beruvchi aqlli kiber-ustoz dialogi",
        "tools": "Dialog Builder"
    },
    "11-dars-oyun-interfeysi-ui-hud": {
        "type": "O'yin UI",
        "skills": "HUD interfeysi, Qalbchalar (HP bar), Hisoblagich, Tangalar soni",
        "deliverable": "Ekranning yuqori burchagida joylashgan to'liq o'yin paneli",
        "tools": "HUD Creator"
    },
    "12-dars-game-jam-mini-loyiha": {
        "type": "Game Jam",
        "skills": "Barcha qismlarni jamlash, Prototip taqdimoti, Do'stlar o'yini",
        "deliverable": "Taqdim etilgan mini-o'yin prototipi va sertifikat",
        "tools": "Game Jam Arena"
    },
    "13-dars-oyin-mexanikasi-va-boshqaruv": {
        "type": "Jonli O'yin",
        "skills": "Klaviatura strelkalari, Qahramon yugurishi, O'yin tsikli",
        "deliverable": "Tugmachalar bosilganda yuguruvchi va to'xtovchi Kiber-Qahramon (O'yin)",
        "tools": "Kiber-Yuguruvchi 1.0"
    },
    "14-dars-tosiqlar-va-xavflar": {
        "type": "Jonli O'yin",
        "skills": "Tikanlar, Lazer nurlari, To'qnashuvda jon ketishi (HP - 1)",
        "deliverable": "Xavfli to'siqlar qo'shilgan va joni tugasa Game Over bo'ladigan o'yin (O'yin)",
        "tools": "Kiber-Yuguruvchi 2.0"
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

def generate_markdown():
    md = []
    md.append("# Target International School — Yillik Taqvim-Mavzu Ish Rejasi (Syllabus)")
    md.append("**Fan:** IT, Kiberxavfsizlik va Vibecoding (5–11-sinflar)")
    md.append("**O'qituvchi:** Musulmonov Mamarajab (va Ismoiljon Usmonov)")
    md.append("**Muassasa:** Target International School, Yunusobod filiali")
    md.append("**O'quv yili:** 2026–2027 o'quv yili · **Davomiyligi:** 36 Hafta / 4 Chorak")
    md.append("**Haftalik yuklama:** 31 soat / hafta · **Yillik umumiy yuklama:** ~1,116 akademik soat")
    md.append("**Rasmiy Manbalar:** O'zbekiston Respublikasi MMTB ilg'or davlat standartlari, Target International School Nizomi va `assets/reja_vibecoding.docx` (108 darslik Yagona Vibecoding Dasturi).")
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

    # Loop cohorts
    for cohort in ANNUAL_COHORTS_DATA:
        cid = cohort['id']
        ctitle = cohort['title']['uz']
        cdesc = cohort['desc']['uz']
        badge = cohort.get('badge', '')
        icon = cohort.get('icon', '📌')
        total_h = cohort.get('total_annual_hours', 180)

        md.append(f"## {icon} {ctitle} ({badge})")
        md.append(f"*{cdesc}*")
        md.append(f"**Yillik yuklama:** 36 hafta · {cohort['weekly_hours']} soat/hafta · Jami: {total_h} soat")
        md.append("")

        # Group by Quarters
        for q in QUARTERS_INFO:
            q_id = q['id']
            q_name = q['name']['uz']
            q_weeks = [w for w in cohort['weeks'] if w['quarter'] == q_id]
            q_hours = sum(w['hours'] for w in q_weeks)

            md.append(f"### 📚 {q_name} ({len(q_weeks)} hafta, {q_hours} soat)")
            md.append(f"*{q['focus']['uz']}*")
            md.append("")
            md.append("| Hafta / № | Mavzu va Dars Yo'nalishi | Soat | Dars Turi | Asosiy Kompetensiyalar va O'rganish Maqsadi | Qo'lga Ushlanadigan Natija (Deliverable) | Dasturiy Vosita / Lab |")
            md.append("|:---:|---|:---:|---|---|---|---|")

            for w in q_weeks:
                w_num = w['week_num']
                w_title = w['title']['uz']
                status = w.get('status', 'planned')

                if status == 'done' and 'lessons' in w:
                    for l in w['lessons']:
                        num = l['num']
                        title = l['title']['uz']
                        lid = l['id']
                        comp = COMPETENCIES.get(lid, {
                            "type": "Amaliy",
                            "skills": l.get('lede', {}).get('uz', '')[:80],
                            "deliverable": "Amaliy ish varaqasi va kod",
                            "tools": "VS Code / Brauzer"
                        })

                        lab_name = l.get('interactive_name', {}).get('uz', comp.get('tools', '—')) if l.get('interactive_name') else comp.get('tools', '—')
                        if l.get('interactive_url'):
                            lab_cell = f"[{lab_name}]({l['interactive_url']})"
                        else:
                            lab_cell = lab_name

                        prez_link = f"[Prezentatsiya]({l['p_url']})" if l.get('p_url') else "—"
                        var_link = f"[Varaqa]({l['v_url']})" if l.get('v_url') else "—"

                        md.append(f"| **{w_num}-h / {num}** | **{title}**<br><sub>{prez_link} · {var_link}</sub> | 1 | `{comp['type']}` | {comp['skills']} | {comp['deliverable']} | {lab_cell} |")
                else:
                    plan = w.get('plan', {})
                    p_title = plan.get('title', {}).get('uz', w_title)
                    p_type = plan.get('type', {}).get('uz', 'Amaliy Loyiha')
                    p_skills = plan.get('skills', {}).get('uz', 'Amaliy muhandislik ko\'nikmalari')
                    p_deliv = plan.get('deliverable', {}).get('uz', 'Loyiha moduli va texnik hisobot')
                    p_tools = plan.get('tools', 'VS Code, Git')

                    md.append(f"| **{w_num}-hafta** | **{p_title}** | {w['hours']} | `{p_type}` | {p_skills} | {p_deliv} | {p_tools} |")

            md.append("")
        md.append("---")
        md.append("")

    # Dedicated Section for Vibecoding 108 Master Plan
    md.append("## ⚡ VIBECODING YAGONA TAQVIM-MAVZU REJASI (36 Hafta / 108 Dars)")
    md.append("*Manba: `assets/reja_vibecoding.docx` · Prompt Engineering, AI Dizayn, Freelance, Agentik Dasturlash va AI Avtomatlashtirish*")
    md.append("**Haftasiga:** 3 dars · **Jami:** 108 dars")
    md.append("")

    cur_q = ""
    cur_b = ""
    for l in VIBECODING_108_MASTER:
        if l['quarter'] and l['quarter'] != cur_q:
            cur_q = l['quarter']
            md.append(f"### 🎯 {cur_q}")
            md.append("")
            md.append("| Dars / Hafta | Dars Nomi va O'rganish Maqsadi | Dars Shakli |")
            md.append("|:---:|---|:---:|")

        if l['block'] and l['block'] != cur_b:
            cur_b = l['block']
            md.append(f"| **BLOK** | **{cur_b}** | — |")

        l_type = "Nazariy" if "[Nazariy]" in l['title'] else "Amaliy"
        clean_title = l['title'].replace("[Nazariy]", "").replace("[Amaliy]", "").strip()
        md.append(f"| **{l['label']}** | {clean_title} | `{l_type}` |")

    md.append("")
    md.append("---")
    md.append("")

    # Pedagogical Standards
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

def generate_html():
    cohorts_json = json.dumps(ANNUAL_COHORTS_DATA, ensure_ascii=False)
    quarters_json = json.dumps(QUARTERS_INFO, ensure_ascii=False)
    vibecoding_json = json.dumps(VIBECODING_108_MASTER, ensure_ascii=False)

    return f"""<!DOCTYPE html>
<html lang="uz" data-theme="dark">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Target International School — Yillik Taqvim-Mavzu Ish Rejasi (36 Hafta / 4 Chorak)</title>
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

    .hero {{
      padding: 36px 0 20px 0;
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
      max-width: 950px;
      line-height: 1.6;
    }}

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

    .controls-bar {{
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: 12px;
      padding: 16px;
      margin-bottom: 24px;
      display: flex;
      flex-direction: column;
      gap: 14px;
    }}
    .filter-row {{
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      justify-content: space-between;
      gap: 12px;
    }}
    .pill-group {{
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
    }}
    .pill-btn {{
      padding: 7px 13px;
      border-radius: 8px;
      font-size: 0.82rem;
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
      flex: 1;
      max-width: 400px;
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

    .quarter-section {{
      margin-bottom: 32px;
    }}
    .quarter-badge-header {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 12px 18px;
      background: rgba(37, 99, 235, 0.12);
      border: 1px solid rgba(37, 99, 235, 0.25);
      border-radius: 10px;
      margin-bottom: 16px;
    }}
    .quarter-badge-header h4 {{
      font-size: 1.1rem;
      font-weight: 800;
      color: var(--accent);
    }}
    .quarter-badge-header span {{
      font-size: 0.82rem;
      color: var(--muted);
    }}

    .table-wrap {{
      overflow-x: auto;
      border: 1px solid var(--card-border);
      border-radius: 12px;
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
      background: rgba(0,0,0,0.2);
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

    .badge-status-done {{
      display: inline-block;
      padding: 2px 7px;
      border-radius: 6px;
      font-size: 0.72rem;
      font-weight: 700;
      background: rgba(16, 185, 129, 0.15);
      color: var(--green);
      border: 1px solid rgba(16, 185, 129, 0.3);
    }}
    .badge-status-planned {{
      display: inline-block;
      padding: 2px 7px;
      border-radius: 6px;
      font-size: 0.72rem;
      font-weight: 700;
      background: rgba(59, 130, 246, 0.12);
      color: #60a5fa;
      border: 1px solid rgba(59, 130, 246, 0.3);
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

    @media print {{
      header.reja-header, .controls-bar, .header-actions {{ display: none !important; }}
      body {{ background: #ffffff !important; color: #000000 !important; }}
      .table-wrap {{ border: 1px solid #cccccc !important; }}
      table.reja-table th {{ background: #eeeeee !important; color: #000000 !important; }}
      table.reja-table td {{ border-bottom: 1px solid #eeeeee !important; color: #000000 !important; }}
    }}
  </style>
</head>
<body>

  <header class="reja-header">
    <div class="container header-inner">
      <div class="brand-wrap">
        <img src="assets/target-logo.png" alt="Target Logo" class="brand-logo">
        <div class="brand-title">
          <h1 data-ru="Target International School — Годовой Учебный План" data-en="Target International School — Annual Master Syllabus">Target International School — Yillik Ish Rejasi</h1>
          <p data-ru="36 Недель / 4 Четверти · IT & Кибербезопасность · 2026–2027" data-en="36 Weeks / 4 Quarters · IT & CyberSecurity · 2026–2027">36 Hafta / 4 Chorak · IT & Kiberxavfsizlik · 2026–2027</p>
        </div>
      </div>
      <div class="header-actions">
        <a href="TARGET_ISH_REJASI_2026_2027.docx" class="btn btn-primary" download>
          <span>📥</span>
          <span data-ru="Скачать Word (.docx)" data-en="Download Word (.docx)">Word (.docx) yuklab olish</span>
        </a>
        <button class="btn" id="themeBtn" title="Mavzuni o'zgartirish">🌓</button>
        <button class="btn" id="langBtn" title="Tilni tanlash">🌐 UZ</button>
      </div>
    </div>
  </header>

  <main class="container">
    <section class="hero">
      <div class="hero-badge" data-ru="ОФИЦИАЛЬНЫЙ ГОДОВОЙ ПЛАН (SYLLABUS)" data-en="OFFICIAL ANNUAL SYLLABUS">RASMIY YILLIK ISH REJASI (SYLLABUS)</div>
      <h2 data-ru="Календарно-Тематический План на 36 Недель (4 Четверти)" data-en="Comprehensive 36-Week / 4-Quarter Annual Curriculum">2026–2027 O'quv Yili Uchun Taqvim-Mavzu Ish Rejasi</h2>
      <p data-ru="Полный учебный план по IT, Кибербезопасности и Вайбкодингу для 5–11 классов. 4 четверти, 108 уроков мастер-программы, интерактивные студии и регламент оценивания." data-en="Comprehensive master curriculum for IT, CyberSecurity, and Vibecoding covering grades 5–11. 4 quarters, 108 lessons master plan, interactive studios, and evaluation criteria.">
        Target International School Yunusobod filiali IT, Kiberxavfsizlik va Vibecoding fani bo'yicha yillik mukammal o'quv dasturi. Barcha 4 ta chorak, 5–11-sinf kohortalari, 108 darslik Vibecoding dasturi va amaliy laboratoriyalar xaritasi.
      </p>
    </section>

    <!-- Stats -->
    <div class="stats-grid">
      <div class="stat-card">
        <div class="stat-icon">📅</div>
        <div>
          <div class="stat-val">36</div>
          <div class="stat-lbl" data-ru="Учебных недель (4 четверти)" data-en="Academic weeks (4 quarters)">O'quv haftasi (4 chorak)</div>
        </div>
      </div>
      <div class="stat-card">
        <div class="stat-icon">🎓</div>
        <div>
          <div class="stat-val">31</div>
          <div class="stat-lbl" data-ru="Часов в неделю" data-en="Weekly hours load">Haftalik soat yuklamasi</div>
        </div>
      </div>
      <div class="stat-card">
        <div class="stat-icon">⚡</div>
        <div>
          <div class="stat-val">108</div>
          <div class="stat-lbl" data-ru="Уроков Vibecoding" data-en="Master Vibecoding lessons">Vibecoding Master darslari</div>
        </div>
      </div>
      <div class="stat-card">
        <div class="stat-icon">🛡️</div>
        <div>
          <div class="stat-val">95+</div>
          <div class="stat-lbl" data-ru="Готовых интерактивных уроков" data-en="Ready interactive lessons">Tayyor interaktiv darslar</div>
        </div>
      </div>
    </div>

    <!-- Controls -->
    <div class="controls-bar">
      <!-- Cohort selection -->
      <div class="filter-row">
        <div class="pill-group" id="cohortPills">
          <button class="pill-btn active" data-cohort="all" data-ru="Все когорты" data-en="All Cohorts">Barcha Kohortalar</button>
          <button class="pill-btn" data-cohort="10-11-sinf">10–11-sinf (Senior)</button>
          <button class="pill-btn" data-cohort="9-sinf">9-sinf (Full-Stack)</button>
          <button class="pill-btn" data-cohort="7-8-sinf">7–8-sinf (Game Dev)</button>
          <button class="pill-btn" data-cohort="5-6-sinf">5–6-sinf (Junior)</button>
          <button class="pill-btn" data-cohort="vibecoding-108">⚡ Vibecoding 108</button>
        </div>
        <div class="search-box">
          <span class="search-icon">🔍</span>
          <input type="text" class="search-input" id="searchInput" placeholder="Dars, mavzu, lab yoki ko'nikma qidirish..." data-ru-ph="Поиск урока, темы или навыка..." data-en-ph="Search lesson, topic or skill...">
        </div>
      </div>
      <!-- Quarter selection -->
      <div class="filter-row">
        <div class="pill-group" id="quarterPills">
          <button class="pill-btn active" data-quarter="all" data-ru="Все 4 четверти (1–36 н.)" data-en="All 4 Quarters (1–36 w.)">Barcha 4 Chorak (1–36 hafta)</button>
          <button class="pill-btn" data-quarter="1" data-ru="1-я Четверть (1–9 н.)" data-en="Quarter 1 (Weeks 1–9)">1-Chorak (1–9-hafta)</button>
          <button class="pill-btn" data-quarter="2" data-ru="2-я Четверть (10–18 н.)" data-en="Quarter 2 (Weeks 10–18)">2-Chorak (10–18-hafta)</button>
          <button class="pill-btn" data-quarter="3" data-ru="3-я Четверть (19–27 н.)" data-en="Quarter 3 (Weeks 19–27)">3-Chorak (19–27-hafta)</button>
          <button class="pill-btn" data-quarter="4" data-ru="4-я Четверть (28–36 н.)" data-en="Quarter 4 (Weeks 28–36)">4-Chorak (28–36-hafta)</button>
        </div>
      </div>
    </div>

    <!-- Curriculum Tables Container -->
    <div id="curriculumContainer"></div>

    <!-- Sign-off Block -->
    <div class="signoff-box">
      <div class="sign-row">
        <strong data-ru="Составитель:" data-en="Prepared by:">Tuzuvchi:</strong><br>
        Target International School IT & Kiberxavfsizlik o'qituvchisi:<br>
        <strong>Musulmonov Mamarajab</strong> <span class="sign-line"></span>
      </div>
      <div class="sign-row">
        <strong data-ru="Утверждаю:" data-en="Approved by:">Tasdiqlayman:</strong><br>
        Target International School Maktab Ma'muriyati / Metodbirlashma Rahbari:<br>
        <span class="sign-line"></span> Sana: «___» _________ 2026-yil
      </div>
    </div>
  </main>

  <script>
    const COHORTS_DATA = {cohorts_json};
    const QUARTERS_DATA = {quarters_json};
    const VIBECODING_108 = {vibecoding_json};

    let activeCohort = 'all';
    let activeQuarter = 'all';
    let searchQuery = '';
    let currentLang = 'uz';

    function render() {{
      const container = document.getElementById('curriculumContainer');
      container.innerHTML = '';

      if (activeCohort === 'vibecoding-108') {{
        renderVibecoding108(container);
        return;
      }}

      COHORTS_DATA.forEach(cohort => {{
        if (activeCohort !== 'all' && cohort.id !== activeCohort) return;

        const cohortSec = document.createElement('div');
        cohortSec.className = 'cohort-section';

        const cTitle = cohort.title[currentLang] || cohort.title.uz;
        const cDesc = cohort.desc[currentLang] || cohort.desc.uz;

        let cohortHtml = `
          <div class="cohort-header" style="border-radius:12px; margin-bottom:16px;">
            <div class="cohort-header-title">
              <span style="font-size:1.8rem">${{cohort.icon}}</span>
              <div>
                <h3>${{cTitle}} (${{cohort.badge}})</h3>
                <div class="cohort-header-desc">${{cDesc}} · ${{cohort.weekly_hours}} soat/hafta</div>
              </div>
            </div>
            <div style="font-weight:700; color:var(--accent);">Jami: ${{cohort.total_annual_hours}} soat</div>
          </div>
        `;

        QUARTERS_DATA.forEach(q => {{
          if (activeQuarter !== 'all' && q.id.toString() !== activeQuarter.toString()) return;

          const qWeeks = cohort.weeks.filter(w => w.quarter === q.id);
          if (qWeeks.length === 0) return;

          const qName = q.name[currentLang] || q.name.uz;
          const qFocus = q.focus[currentLang] || q.focus.uz;

          let rowsHtml = '';
          qWeeks.forEach(w => {{
            const wNum = w.week_num;
            const wTitle = w.title[currentLang] || w.title.uz;
            const status = w.status;

            if (status === 'done' && w.lessons) {{
              w.lessons.forEach(l => {{
                const lTitle = (l.title && l.title[currentLang]) ? l.title[currentLang] : (l.title ? (l.title.uz || l.title) : '');
                const lType = (l.type && l.type[currentLang]) ? l.type[currentLang] : (l.type ? (l.type.uz || l.type) : 'Amaliy');
                const lSkills = (l.skills && l.skills[currentLang]) ? l.skills[currentLang] : (l.skills ? (l.skills.uz || l.skills) : (l.lede ? (l.lede[currentLang] || l.lede.uz) : ''));
                const lDeliv = (l.deliverable && l.deliverable[currentLang]) ? l.deliverable[currentLang] : (l.deliverable ? (l.deliverable.uz || l.deliverable) : '');
                const lTools = l.tools || 'VS Code';

                // Search filtering
                if (searchQuery) {{
                  const hay = (wTitle + ' ' + lTitle + ' ' + lSkills + ' ' + lTools + ' ' + lDeliv).toLowerCase();
                  if (!hay.includes(searchQuery)) return;
                }}

                let links = '';
                if (l.pres) links += `<a href="${{l.pres}}"><span>📺</span> Taqdimot</a>`;
                if (l.sheet) links += `<a href="${{l.sheet}}"><span>📄</span> Varaqa</a>`;

                let labLink = `<span class="badge-type">${{lTools}}</span>`;
                if (l.interactive_path) {{
                  const labName = (l.interactive_name && l.interactive_name[currentLang]) ? l.interactive_name[currentLang] : (l.interactive_name ? l.interactive_name.uz : 'Lab');
                  labLink = `<a href="${{l.interactive_path}}" class="badge-lab"><span>🧪</span> ${{labName}}</a>`;
                }}

                rowsHtml += `
                  <tr>
                    <td class="cell-num">${{wNum}}-h / ${{l.num}}</td>
                    <td class="cell-title">
                      <strong>${{lTitle}}</strong>
                      <div class="cell-links">${{links}}</div>
                    </td>
                    <td style="text-align:center;"><span class="badge-status-done">✅ Tayyor</span></td>
                    <td><span class="badge-type">${{lType}}</span></td>
                    <td style="font-size:0.83rem; color:var(--muted);">${{lSkills}}</td>
                    <td><span class="deliverable-tag">${{lDeliv || 'Amaliy topshiriq'}}</span></td>
                    <td>${{labLink}}</td>
                  </tr>
                `;
              }});
            }} else {{
              const plan = w.plan || {{}};
              const pTitle = (plan.title && plan.title[currentLang]) ? plan.title[currentLang] : (plan.title ? plan.title.uz : wTitle);
              const pType = (plan.type && plan.type[currentLang]) ? plan.type[currentLang] : (plan.type ? plan.type.uz : 'Amaliy Loyiha');
              const pSkills = (plan.skills && plan.skills[currentLang]) ? plan.skills[currentLang] : (plan.skills ? plan.skills.uz : '');
              const pDeliv = (plan.deliverable && plan.deliverable[currentLang]) ? plan.deliverable[currentLang] : (plan.deliverable ? plan.deliverable.uz : '');
              const pTools = plan.tools || 'VS Code, Git';

              if (searchQuery) {{
                const hay = (wTitle + ' ' + pTitle + ' ' + pSkills + ' ' + pTools + ' ' + pDeliv).toLowerCase();
                if (!hay.includes(searchQuery)) return;
              }}

              rowsHtml += `
                <tr>
                  <td class="cell-num">${{wNum}}-hafta</td>
                  <td class="cell-title">
                    <strong>${{pTitle}}</strong>
                    <div style="font-size:0.75rem; color:var(--muted);">${{w.hours}} soatlik o'quv bloki</div>
                  </td>
                  <td style="text-align:center;"><span class="badge-status-planned">🚀 Reja</span></td>
                  <td><span class="badge-type">${{pType}}</span></td>
                  <td style="font-size:0.83rem; color:var(--muted);">${{pSkills}}</td>
                  <td><span class="deliverable-tag">${{pDeliv}}</span></td>
                  <td><span class="badge-type">${{pTools}}</span></td>
                </tr>
              `;
            }}
          }});

          if (rowsHtml) {{
            cohortHtml += `
              <div class="quarter-section">
                <div class="quarter-badge-header">
                  <h4>📚 ${{qName}}</h4>
                  <span>${{qFocus}}</span>
                </div>
                <div class="table-wrap">
                  <table class="reja-table">
                    <thead>
                      <tr>
                        <th style="width:70px;">№</th>
                        <th style="width:240px;">Dars Mavzusi</th>
                        <th style="width:90px; text-align:center;">Holat</th>
                        <th style="width:130px;">Turi</th>
                        <th>Kompetensiyalar</th>
                        <th style="width:230px;">Natija (Deliverable)</th>
                        <th style="width:160px;">Vosita / Lab</th>
                      </tr>
                    </thead>
                    <tbody>
                      ${{rowsHtml}}
                    </tbody>
                  </table>
                </div>
              </div>
            `;
          }}
        }});

        cohortSec.innerHTML = cohortHtml;
        container.appendChild(cohortSec);
      }});
    }}

    function renderVibecoding108(container) {{
      let html = `
        <div class="cohort-section">
          <div class="cohort-header" style="border-radius:12px; margin-bottom:16px;">
            <div class="cohort-header-title">
              <span style="font-size:1.8rem">⚡</span>
              <div>
                <h3>Vibecoding Fanidan Yagona Taqvim-Mavzu Rejasi</h3>
                <div class="cohort-header-desc">Manba: assets/reja_vibecoding.docx · 36 Hafta / 108 Dars (Haftasiga 3 dars)</div>
              </div>
            </div>
            <div style="font-weight:700; color:var(--accent);">Jami: 108 dars</div>
          </div>
          <div class="table-wrap">
            <table class="reja-table">
              <thead>
                <tr>
                  <th style="width:90px;">Dars / Hafta</th>
                  <th>Mavzu va O'rganish Maqsadi</th>
                  <th style="width:130px;">Chorak</th>
                  <th style="width:100px;">Shakl</th>
                </tr>
              </thead>
              <tbody>
      `;

      VIBECODING_108.forEach(item => {{
        const isTheory = item.title.includes('[Nazariy]');
        const cleanTitle = item.title.replace('[Nazariy]', '').replace('[Amaliy]', '').trim();
        const typeBadge = isTheory ? '<span class="badge-type" style="color:#60a5fa; background:rgba(59,130,246,0.1);">Nazariy</span>' : '<span class="badge-type">Amaliy</span>';

        if (searchQuery) {{
          const hay = (item.label + ' ' + item.title + ' ' + item.quarter + ' ' + item.block).toLowerCase();
          if (!hay.includes(searchQuery)) return;
        }}

        html += `
          <tr>
            <td class="cell-num">${{item.label}}</td>
            <td class="cell-title">
              <strong>${{cleanTitle}}</strong>
              <div style="font-size:0.75rem; color:var(--muted);">${{item.block || ''}}</div>
            </td>
            <td style="font-size:0.8rem; color:var(--muted);">${{item.quarter || ''}}</td>
            <td>${{typeBadge}}</td>
          </tr>
        `;
      }});

      html += `
              </tbody>
            </table>
          </div>
        </div>
      `;
      container.innerHTML = html;
    }}

    // Filter Listeners
    document.getElementById('cohortPills').addEventListener('click', e => {{
      if (e.target.dataset.cohort) {{
        document.querySelectorAll('#cohortPills .pill-btn').forEach(b => b.classList.remove('active'));
        e.target.classList.add('active');
        activeCohort = e.target.dataset.cohort;
        render();
      }}
    }});

    document.getElementById('quarterPills').addEventListener('click', e => {{
      if (e.target.dataset.quarter) {{
        document.querySelectorAll('#quarterPills .pill-btn').forEach(b => b.classList.remove('active'));
        e.target.classList.add('active');
        activeQuarter = e.target.dataset.quarter;
        render();
      }}
    }});

    document.getElementById('searchInput').addEventListener('input', e => {{
      searchQuery = e.target.value.toLowerCase().trim();
      render();
    }});

    // Theme Toggle
    document.getElementById('themeBtn').addEventListener('click', () => {{
      const html = document.documentElement;
      const cur = html.getAttribute('data-theme');
      html.setAttribute('data-theme', cur === 'dark' ? 'light' : 'dark');
    }});

    // Language Toggle
    const langBtn = document.getElementById('langBtn');
    langBtn.addEventListener('click', () => {{
      if (currentLang === 'uz') currentLang = 'ru';
      else if (currentLang === 'ru') currentLang = 'en';
      else currentLang = 'uz';

      langBtn.textContent = '🌐 ' + currentLang.toUpperCase();
      document.querySelectorAll('[data-ru]').forEach(el => {{
        if (currentLang === 'ru' && el.dataset.ru) el.textContent = el.dataset.ru;
        else if (currentLang === 'en' && el.dataset.en) el.textContent = el.dataset.en;
        else if (currentLang === 'uz') {{
          // Reset to default uz
          if (el.dataset.defaultText) el.textContent = el.dataset.defaultText;
        }}
      }});
      render();
    }});

    // Store default uz text
    document.querySelectorAll('[data-ru]').forEach(el => {{
      el.dataset.defaultText = el.textContent;
    }});

    render();
  </script>
</body>
</html>
"""

def main():
    print("Generating comprehensive REJA.md...")
    md_content = generate_markdown()
    with open('REJA.md', 'w', encoding='utf-8') as f:
        f.write(md_content)
    print(f"REJA.md generated ({len(md_content)} chars).")

    print("Generating interactive reja.html...")
    html_content = generate_html()
    with open('reja.html', 'w', encoding='utf-8') as f:
        f.write(html_content)
    print(f"reja.html generated ({len(html_content)} chars).")

if __name__ == '__main__':
    main()
