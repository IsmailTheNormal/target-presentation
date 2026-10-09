#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Target International School — DOCX Yillik Ish Rejasi Generator (36 Hafta / 4 Chorak)
Ushbu skript yillik o'quv dasturi (annual_curriculum_data.py) asosida
rasmiy, chiroyli va chop etishga tayyor bo'lgan Microsoft Word (.docx)
hujjatlarini to'liq generatsiya qiladi.
"""

import json
import re
import os
import sys
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.enum.section import WD_ORIENT
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

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

def set_cell_background(cell, color_hex):
    shading = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{color_hex}"/>')
    cell._tc.get_or_add_tcPr().append(shading)

def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = OxmlElement('w:tcMar')
    for m, val in [('top', top), ('bottom', bottom), ('left', left), ('right', right)]:
        node = OxmlElement(f'w:{m}')
        node.set(qn('w:w'), str(val))
        node.set(qn('w:type'), 'dxa')
        tcMar.append(node)
    tcPr.append(tcMar)

def set_table_borders(table, color="CCCCCC", sz="4", val="single"):
    tblPr = table._tbl.tblPr
    borders = parse_xml(
        f'<w:tblBorders {nsdecls("w")}>\n'
        f'  <w:top w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>\n'
        f'  <w:bottom w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>\n'
        f'  <w:insideH w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>\n'
        f'  <w:insideV w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>\n'
        f'  <w:left w:val="none"/>\n'
        f'  <w:right w:val="none"/>\n'
        f'</w:tblBorders>'
    )
    tblPr.append(borders)

def make_callout_box(doc, title, text, bg_color="F1F5F9", border_color="2563EB"):
    tbl = doc.add_table(rows=1, cols=1)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    cell = tbl.cell(0, 0)
    set_cell_background(cell, bg_color)
    set_cell_margins(cell, top=140, bottom=140, left=200, right=200)

    tcPr = cell._tc.get_or_add_tcPr()
    borders = parse_xml(
        f'<w:tcBorders {nsdecls("w")}>\n'
        f'  <w:left w:val="single" w:sz="24" w:space="0" w:color="{border_color}"/>\n'
        f'  <w:top w:val="none"/>\n'
        f'  <w:bottom w:val="none"/>\n'
        f'  <w:right w:val="none"/>\n'
        f'</w:tcBorders>'
    )
    tcPr.append(borders)

    p = cell.paragraphs[0]
    p.paragraph_format.space_before = Pt(2)
    p.paragraph_format.space_after = Pt(2)
    r1 = p.add_run(f"{title}: ")
    r1.bold = True
    r1.font.name = "Arial"
    r1.font.size = Pt(9.5)
    r1.font.color.rgb = RGBColor(0x1E, 0x3A, 0x8A)

    r2 = p.add_run(text)
    r2.font.name = "Arial"
    r2.font.size = Pt(9.5)
    r2.font.color.rgb = RGBColor(0x33, 0x41, 0x55)

    doc.add_paragraph().paragraph_format.space_after = Pt(6)

def build_curriculum_document(cohorts, output_filename, is_master=True, single_cohort=None):
    doc = docx.Document()

    # Landscape A4 for wide table layout
    section = doc.sections[0]
    section.orientation = WD_ORIENT.LANDSCAPE
    section.page_width = Inches(11.69)
    section.page_height = Inches(8.27)
    section.top_margin = Inches(0.5)
    section.bottom_margin = Inches(0.5)
    section.left_margin = Inches(0.5)
    section.right_margin = Inches(0.5)

    # 1. Header / Approval Table
    app_table = doc.add_table(rows=1, cols=2)
    app_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    app_table.autofit = False

    # Left: Kelishildi
    c_left = app_table.cell(0, 0)
    c_left.width = Inches(5.3)
    p_left = c_left.paragraphs[0]
    p_left.paragraph_format.space_after = Pt(2)
    r = p_left.add_run("«KELISHILDI»\n")
    r.bold = True
    r.font.size = Pt(9)
    r = p_left.add_run("Target International School\nIlmiy bo'lim mudiri (Zavuch):\n_________________________\n«___» ____________ 2026-yil")
    r.font.size = Pt(8.5)

    # Right: Tasdiqlayman
    c_right = app_table.cell(0, 1)
    c_right.width = Inches(5.3)
    p_right = c_right.paragraphs[0]
    p_right.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    p_right.paragraph_format.space_after = Pt(2)
    r = p_right.add_run("«TASDIQLAYMAN»\n")
    r.bold = True
    r.font.size = Pt(9)
    r = p_right.add_run("Target International School\nMaktab Direktori / Metodbirlashma Rahbari:\n_________________________\n«___» ____________ 2026-yil")
    r.font.size = Pt(8.5)

    doc.add_paragraph().paragraph_format.space_after = Pt(8)

    # 2. Main Title
    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_title.paragraph_format.space_after = Pt(4)
    run_t1 = p_title.add_run("TARGET INTERNATIONAL SCHOOL — YUNUSOBOD FILIALI\n")
    run_t1.bold = True
    run_t1.font.name = "Arial"
    run_t1.font.size = Pt(11)
    run_t1.font.color.rgb = RGBColor(0x0F, 0x17, 0x2A)

    run_t2 = p_title.add_run("2026–2027 O'QUV YILI UCHUN YILLIK TAQVIM-MAVZU ISH REJASI (SYLLABUS)\n")
    run_t2.bold = True
    run_t2.font.name = "Arial"
    run_t2.font.size = Pt(14)
    run_t2.font.color.rgb = RGBColor(0x1E, 0x3A, 0x8A)

    subtitle_text = "IT, Kiberxavfsizlik va Vibecoding (5–11-sinflar — 36 Hafta / 4 Chorak)" if is_master else f"{single_cohort['title']['uz']} Bo'yicha Maxsus Yillik Ish Rejasi (36 Hafta / 4 Chorak)"
    run_t3 = p_title.add_run(subtitle_text)
    run_t3.bold = True
    run_t3.font.name = "Arial"
    run_t3.font.size = Pt(11)
    run_t3.font.color.rgb = RGBColor(0x25, 0x63, 0xEB)

    # Meta paragraph
    p_meta = doc.add_paragraph()
    p_meta.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_meta.paragraph_format.space_after = Pt(12)
    r_meta = p_meta.add_run("Tuzuvchi o'qituvchi: Musulmonov Mamarajab (va Ismoiljon Usmonov) · Haftalik yuklama: 31 soat · Dars davomiyligi: 40 daqiqa")
    r_meta.italic = True
    r_meta.font.size = Pt(9.5)
    r_meta.font.color.rgb = RGBColor(0x64, 0x74, 0x8B)

    # Callout box
    make_callout_box(
        doc,
        "YILLIK O'QUV REJASI VA METODIK STANDART",
        "Mazkur taqvim-mavzu rejasi to'liq 36 o'quv haftasini (4 ta chorak) qamrab oladi. Har bir dars 40 daqiqalik qat'iy reglament "
        "(Kirish 0-3 daq, Muammo 3-7 daq, Nazariya 7-23 daq, Mustahkamlash/Amaliyot 23-36 daq, Xulosa/Baholash 36-40 daq) va 10 ballik mezon asosida o'tiladi. "
        "Materiallar 20% nazariya va 80% amaliyot formatida tuzilgan.",
        bg_color="EFF6FF", border_color="2563EB"
    )

    # 3. Weekly Timetable (if master)
    if is_master:
        p_sch_head = doc.add_paragraph()
        p_sch_head.paragraph_format.space_before = Pt(8)
        p_sch_head.paragraph_format.space_after = Pt(4)
        r = p_sch_head.add_run("I. Haftalik Dars Jadvali va Kohortalar Taqsimoti (31 Soat / Hafta)")
        r.bold = True
        r.font.name = "Arial"
        r.font.size = Pt(11)
        r.font.color.rgb = RGBColor(0x1E, 0x3A, 0x8A)

        sch_table = doc.add_table(rows=1, cols=5)
        sch_table.alignment = WD_TABLE_ALIGNMENT.CENTER
        set_table_borders(sch_table, color="CBD5E1")

        headers = ["Kohorta (Sinf)", "Fan Yo'nalishi", "Haftalik Soat", "Dars Kunlari va Vaqtlari", "Xona / Format"]
        widths = [Inches(1.8), Inches(2.8), Inches(1.0), Inches(3.2), Inches(1.8)]

        hdr_row = sch_table.rows[0]
        tblHeader = OxmlElement('w:tblHeader')
        hdr_row._tr.get_or_add_trPr().append(tblHeader)

        for i, h in enumerate(headers):
            cell = hdr_row.cells[i]
            cell.width = widths[i]
            set_cell_background(cell, "1E3A8A")
            set_cell_margins(cell, top=100, bottom=100, left=120, right=120)
            p = cell.paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            run = p.add_run(h)
            run.bold = True
            run.font.name = "Arial"
            run.font.size = Pt(8.5)
            run.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)

        sch_data = [
            ("10A 10B 11A 11B", "Senior AI & Enterprise Kiberxavfsizlik", "5 soat", "Seshanba (5-dars) · Chorshanba (5, 6-dars) · Payshanba (5, 6-dars)", "Kompyuter Lab"),
            ("9A 9B", "Junior Vibecoders, Full-Stack & DevOps", "5 soat", "Dushanba (7-dars) · Seshanba (6, 7-dars) · Juma (7, 8-dars)", "Kompyuter Lab"),
            ("7A 7B 8A 8B", "Game Dev, Interaktiv Veb & FUT Creator", "5 soat", "Dushanba (8-dars) · Chorshanba (7, 8-dars) · Payshanba (7, 8-dars)", "Kompyuter Lab"),
            ("5A 5B 6A 6B", "Junior Creators & Kiber-Xavfsizlik", "6 soat", "Seshanba (3, 4-dars) · Chorshanba (3, 4-dars) · Payshanba (3, 4-dars)", "Kompyuter Lab"),
            ("Choice: IT (9–11)", "Tanlov IT: Amaliy Dasturlash & Hackathon", "10 soat", "Dushanba–Juma (9-dars 16:10, 10-dars 16:55)", "IT Hub / Maydon"),
            ("JAMI", "Barcha kohortalar bo'yicha", "31 soat", "Haftasiga 31 akademik soat", "Target Yunusobod"),
        ]

        for r_idx, row_values in enumerate(sch_data):
            row = sch_table.add_row()
            bg = "F8FAFC" if r_idx % 2 == 1 else "FFFFFF"
            if r_idx == len(sch_data) - 1:
                bg = "E2E8F0"
            for c_idx, val in enumerate(row_values):
                cell = row.cells[c_idx]
                cell.width = widths[c_idx]
                set_cell_background(cell, bg)
                set_cell_margins(cell, top=80, bottom=80, left=120, right=120)
                p = cell.paragraphs[0]
                run = p.add_run(val)
                run.font.name = "Arial"
                run.font.size = Pt(8.5)
                if r_idx == len(sch_data) - 1 or c_idx == 0:
                    run.bold = True

        doc.add_paragraph().paragraph_format.space_after = Pt(14)

    # 4. Cohort Tables across all 36 Weeks (grouped by quarters)
    target_cohorts = [single_cohort] if single_cohort else cohorts

    for cohort in target_cohorts:
        cid = cohort['id']
        ctitle = cohort['title']['uz']
        cdesc = cohort['desc']['uz']
        badge = cohort.get('badge', '')
        total_hours = cohort.get('total_annual_hours', 180)

        p_sec = doc.add_paragraph()
        p_sec.paragraph_format.space_before = Pt(16)
        p_sec.paragraph_format.space_after = Pt(2)
        r = p_sec.add_run(f"Kohorta: {ctitle} ({badge}) — Yillik Reja (36 Hafta / {total_hours} Soat)")
        r.bold = True
        r.font.name = "Arial"
        r.font.size = Pt(12)
        r.font.color.rgb = RGBColor(0x1E, 0x3A, 0x8A)

        p_desc = doc.add_paragraph()
        p_desc.paragraph_format.space_after = Pt(8)
        r_d = p_desc.add_run(f"Yo'nalish tavsifi: {cdesc} · Haftalik soat: {cohort['weekly_hours']} soat")
        r_d.italic = True
        r_d.font.size = Pt(9)
        r_d.font.color.rgb = RGBColor(0x47, 0x55, 0x69)

        # Loop through the 4 Quarters
        for q in QUARTERS_INFO:
            q_id = q['id']
            q_name = q['name']['uz']
            q_focus = q['focus']['uz']
            q_weeks = [w for w in cohort['weeks'] if w['quarter'] == q_id]

            if not q_weeks:
                continue

            q_hours = sum(w['hours'] for w in q_weeks)

            # Quarter Header
            p_qh = doc.add_paragraph()
            p_qh.paragraph_format.space_before = Pt(10)
            p_qh.paragraph_format.space_after = Pt(4)
            r_qh = p_qh.add_run(f"📚 {q_name} ({len(q_weeks)} hafta, {q_hours} soat)")
            r_qh.bold = True
            r_qh.font.name = "Arial"
            r_qh.font.size = Pt(10)
            r_qh.font.color.rgb = RGBColor(0x1E, 0x40, 0xAF)

            # Columns: Hafta/№ | Dars Mavzusi | Soat | Shakl | Kompetensiyalar va O'rganish Maqsadi | Kutilayotgan Natija | Dasturiy Vosita | Sana
            cols_w = [Inches(0.7), Inches(2.3), Inches(0.45), Inches(1.1), Inches(2.7), Inches(1.8), Inches(1.1), Inches(0.55)]
            table = doc.add_table(rows=1, cols=8)
            table.alignment = WD_TABLE_ALIGNMENT.CENTER
            set_table_borders(table, color="CBD5E1")

            hdr_row = table.rows[0]
            tblHeader = OxmlElement('w:tblHeader')
            hdr_row._tr.get_or_add_trPr().append(tblHeader)

            th_names = ["Hafta/№", "Dars Mavzusi", "Soat", "Dars Turi", "Kompetensiyalar va O'rganish Maqsadi", "Kutilayotgan Natija", "Dasturiy Vosita", "Sana"]
            for i, th in enumerate(th_names):
                cell = hdr_row.cells[i]
                cell.width = cols_w[i]
                set_cell_background(cell, "0B192C")
                set_cell_margins(cell, top=80, bottom=80, left=80, right=80)
                p = cell.paragraphs[0]
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                run = p.add_run(th)
                run.bold = True
                run.font.name = "Arial"
                run.font.size = Pt(8)
                run.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)

            row_count = 0
            for w in q_weeks:
                w_num = w['week_num']
                w_title = w['title']['uz']
                status = w.get('status', 'planned')

                if status == 'done' and 'lessons' in w:
                    for l in w['lessons']:
                        row_count += 1
                        num = l['num']
                        title = l['title']['uz']
                        lid = l['id']
                        comp = COMPETENCIES.get(lid, {
                            "type": "Amaliy",
                            "skills": l.get('lede', {}).get('uz', '')[:80],
                            "deliverable": "Amaliy ish varaqasi va kod",
                            "tools": "VS Code / Brauzer"
                        })
                        lab_str = l.get('interactive_name', {}).get('uz', comp.get('tools', 'VS Code')) if l.get('interactive_name') else comp.get('tools', 'VS Code')

                        row = table.add_row()
                        bg = "F8FAFC" if row_count % 2 == 1 else "FFFFFF"

                        vals = [
                            f"{w_num}-h/{num}",
                            title,
                            "1",
                            comp['type'],
                            comp['skills'],
                            comp['deliverable'],
                            lab_str,
                            "___/___"
                        ]

                        for c_i, v in enumerate(vals):
                            cell = row.cells[c_i]
                            cell.width = cols_w[c_i]
                            set_cell_background(cell, bg)
                            set_cell_margins(cell, top=60, bottom=60, left=80, right=80)
                            p = cell.paragraphs[0]
                            run = p.add_run(v)
                            run.font.name = "Arial"
                            run.font.size = Pt(7.5)
                            if c_i == 0 or c_i == 2 or c_i == 7:
                                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                                if c_i == 0:
                                    run.bold = True
                            elif c_i == 1:
                                run.bold = True
                else:
                    row_count += 1
                    plan = w.get('plan', {})
                    p_title = plan.get('title', {}).get('uz', w_title)
                    p_type = plan.get('type', {}).get('uz', 'Amaliy Loyiha')
                    p_skills = plan.get('skills', {}).get('uz', 'Amaliy dasturlash ko\'nikmalari')
                    p_deliv = plan.get('deliverable', {}).get('uz', 'Amaliy modul va loyiha topshirig\'i')
                    p_tools = plan.get('tools', 'VS Code, Git')

                    row = table.add_row()
                    bg = "F0F9FF" if row_count % 2 == 1 else "FFFFFF"

                    vals = [
                        f"{w_num}-hafta",
                        p_title,
                        str(w['hours']),
                        p_type,
                        p_skills,
                        p_deliv,
                        p_tools,
                        "___/___"
                    ]

                    for c_i, v in enumerate(vals):
                        cell = row.cells[c_i]
                        cell.width = cols_w[c_i]
                        set_cell_background(cell, bg)
                        set_cell_margins(cell, top=60, bottom=60, left=80, right=80)
                        p = cell.paragraphs[0]
                        run = p.add_run(v)
                        run.font.name = "Arial"
                        run.font.size = Pt(7.5)
                        if c_i == 0 or c_i == 2 or c_i == 7:
                            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                            if c_i == 0:
                                run.bold = True
                        elif c_i == 1:
                            run.bold = True

            doc.add_paragraph().paragraph_format.space_after = Pt(8)

    # 5. Vibecoding 108 Master Plan Table (if master)
    if is_master:
        p_vhead = doc.add_paragraph()
        p_vhead.paragraph_format.space_before = Pt(16)
        p_vhead.paragraph_format.space_after = Pt(4)
        r = p_vhead.add_run("II. Vibecoding Yagona Taqvim-Mavzu Rejasi (36 Hafta / 108 Dars)")
        r.bold = True
        r.font.name = "Arial"
        r.font.size = Pt(12)
        r.font.color.rgb = RGBColor(0x1E, 0x3A, 0x8A)

        p_vsub = doc.add_paragraph()
        p_vsub.paragraph_format.space_after = Pt(8)
        r_vs = p_vsub.add_run("Manba: assets/reja_vibecoding.docx · Haftasiga 3 dars · 4 chorak, 12 blok, 108 dars")
        r_vs.italic = True
        r_vs.font.size = Pt(9)
        r_vs.font.color.rgb = RGBColor(0x47, 0x55, 0x69)

        v_cols_w = [Inches(1.2), Inches(6.0), Inches(2.2), Inches(1.2)]
        v_table = doc.add_table(rows=1, cols=4)
        v_table.alignment = WD_TABLE_ALIGNMENT.CENTER
        set_table_borders(v_table, color="CBD5E1")

        v_hdr = v_table.rows[0]
        v_hdr_el = OxmlElement('w:tblHeader')
        v_hdr._tr.get_or_add_trPr().append(v_hdr_el)

        v_headers = ["Dars / Hafta", "Mavzu va O'rganish Maqsadi", "Chorak va Blok", "Dars Shakli"]
        for i, h in enumerate(v_headers):
            cell = v_hdr.cells[i]
            cell.width = v_cols_w[i]
            set_cell_background(cell, "1E3A8A")
            set_cell_margins(cell, top=80, bottom=80, left=80, right=80)
            p = cell.paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            run = p.add_run(h)
            run.bold = True
            run.font.name = "Arial"
            run.font.size = Pt(8)
            run.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)

        for idx, item in enumerate(VIBECODING_108_MASTER):
            is_theory = "[Nazariy]" in item['title']
            clean_title = item['title'].replace("[Nazariy]", "").replace("[Amaliy]", "").strip()
            shakl = "Nazariy" if is_theory else "Amaliy"

            row = v_table.add_row()
            bg = "F8FAFC" if idx % 2 == 1 else "FFFFFF"

            vals = [
                item['label'],
                clean_title,
                f"{item.get('quarter', '')}\n{item.get('block', '')}",
                shakl
            ]

            for c_i, v in enumerate(vals):
                cell = row.cells[c_i]
                cell.width = v_cols_w[c_i]
                set_cell_background(cell, bg)
                set_cell_margins(cell, top=50, bottom=50, left=80, right=80)
                p = cell.paragraphs[0]
                run = p.add_run(v)
                run.font.name = "Arial"
                run.font.size = Pt(7.5)
                if c_i == 0:
                    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                    run.bold = True
                elif c_i == 3:
                    p.alignment = WD_ALIGN_PARAGRAPH.CENTER

        doc.add_paragraph().paragraph_format.space_after = Pt(14)

    # 6. Pedagogical Rubric & Sign-offs
    p_ped = doc.add_paragraph()
    p_ped.paragraph_format.space_before = Pt(12)
    p_ped.paragraph_format.space_after = Pt(4)
    r = p_ped.add_run("III. Pedagogik Baholash Nizomi va 10 Ballik Mezon")
    r.bold = True
    r.font.name = "Arial"
    r.font.size = Pt(11)
    r.font.color.rgb = RGBColor(0x1E, 0x3A, 0x8A)

    rubric_tbl = doc.add_table(rows=1, cols=3)
    rubric_tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(rubric_tbl, color="CBD5E1")
    r_hdr = rubric_tbl.rows[0]
    r_widths = [Inches(1.8), Inches(1.8), Inches(7.0)]
    for i, h in enumerate(["Daraja (Baho)", "Ball Oralig'i", "Tavsif va O'zlashtirish Ko'rsatkichi"]):
        cell = r_hdr.cells[i]
        cell.width = r_widths[i]
        set_cell_background(cell, "334155")
        set_cell_margins(cell, top=70, bottom=70, left=90, right=90)
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = p.add_run(h)
        run.bold = True
        run.font.size = Pt(8)
        run.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)

    rubric_rows = [
        ("A'lo (Advanced)", "9 – 10 ball", "Nazariy arxitektura to'liq tushunilgan, amaliy laboratoriya/studio topshirig'i 100% mustaqil bajarilgan, ish varaqasi va savollar xatosiz to'ldirilgan."),
        ("Yaxshi (Proficient)", "7 – 8 ball", "Asosiy tushunchalar o'zlashtirilgan, amaliy topshiriqda mayda kamchiliklar bor, ish varaqasi 80% to'ldirilgan."),
        ("Qoniqarli (Basic)", "5 – 6 ball", "Tushunchalarda chalkashlik bor, amaliy vazifa o'qituvchi yordamida qisman bajarilgan, ish varaqasi 50% to'ldirilgan.")
    ]
    for r_data in rubric_rows:
        row = rubric_tbl.add_row()
        for i, val in enumerate(r_data):
            cell = row.cells[i]
            cell.width = r_widths[i]
            set_cell_background(cell, "FFFFFF")
            set_cell_margins(cell, top=60, bottom=60, left=90, right=90)
            p = cell.paragraphs[0]
            run = p.add_run(val)
            run.font.size = Pt(8)
            if i == 0 or i == 1:
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                run.bold = True

    doc.add_paragraph().paragraph_format.space_after = Pt(16)

    # 7. Signature Footer Table
    sign_table = doc.add_table(rows=1, cols=2)
    sign_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    s_left = sign_table.cell(0, 0)
    s_left.width = Inches(5.3)
    p_sl = s_left.paragraphs[0]
    p_sl.add_run("Tuzuvchi o'qituvchi:\n").bold = True
    p_sl.add_run("Target International School IT & Kiberxavfsizlik o'qituvchisi:\n")
    p_sl.add_run("Musulmonov Mamarajab ___________________\n")
    p_sl.add_run("Sana: «___» ____________ 2026-yil")

    s_right = sign_table.cell(0, 1)
    s_right.width = Inches(5.3)
    p_sr = s_right.paragraphs[0]
    p_sr.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    p_sr.add_run("Tasdiqlayman:\n").bold = True
    p_sr.add_run("Target International School Metodbirlashma Rahbari:\n")
    p_sr.add_run("_____________________________________\n")
    p_sr.add_run("Sana: «___» ____________ 2026-yil")

    # Save document
    doc.save(output_filename)
    print(f"Generated DOCX: {output_filename} ({os.path.getsize(output_filename):,} bytes)")

def build_vibecoding_only_docx(output_filename):
    doc = docx.Document()
    section = doc.sections[0]
    section.orientation = WD_ORIENT.LANDSCAPE
    section.page_width = Inches(11.69)
    section.page_height = Inches(8.27)
    section.top_margin = Inches(0.5)
    section.bottom_margin = Inches(0.5)
    section.left_margin = Inches(0.5)
    section.right_margin = Inches(0.5)

    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r1 = p_title.add_run("VIBECODING FANIDAN YAGONA TAQVIM-MAVZU REJASI\n")
    r1.bold = True
    r1.font.size = Pt(14)
    r1.font.color.rgb = RGBColor(0x1E, 0x3A, 0x8A)

    r2 = p_title.add_run("Prompt Engineering, AI Dizayn, Freelance, Agentik Dasturlash va AI Avtomatlashtirish\n")
    r2.bold = True
    r2.font.size = Pt(11)
    r2.font.color.rgb = RGBColor(0x25, 0x63, 0xEB)

    r3 = p_title.add_run("36 Hafta / 108 Dars (Haftasiga 3 dars) · Tuzuvchilar: Musulmonov Mamarajab, Ismoiljon Usmonov")
    r3.italic = True
    r3.font.size = Pt(9.5)

    v_cols_w = [Inches(1.2), Inches(6.0), Inches(2.2), Inches(1.2)]
    v_table = doc.add_table(rows=1, cols=4)
    v_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(v_table, color="CBD5E1")

    v_hdr = v_table.rows[0]
    v_headers = ["Dars / Hafta", "Mavzu va O'rganish Maqsadi", "Chorak va Blok", "Dars Shakli"]
    for i, h in enumerate(v_headers):
        cell = v_hdr.cells[i]
        cell.width = v_cols_w[i]
        set_cell_background(cell, "1E3A8A")
        set_cell_margins(cell, top=80, bottom=80, left=80, right=80)
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = p.add_run(h)
        run.bold = True
        run.font.size = Pt(8.5)
        run.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)

    for idx, item in enumerate(VIBECODING_108_MASTER):
        is_theory = "[Nazariy]" in item['title']
        clean_title = item['title'].replace("[Nazariy]", "").replace("[Amaliy]", "").strip()
        shakl = "Nazariy" if is_theory else "Amaliy"

        row = v_table.add_row()
        bg = "F8FAFC" if idx % 2 == 1 else "FFFFFF"

        vals = [
            item['label'],
            clean_title,
            f"{item.get('quarter', '')}\n{item.get('block', '')}",
            shakl
        ]

        for c_i, v in enumerate(vals):
            cell = row.cells[c_i]
            cell.width = v_cols_w[c_i]
            set_cell_background(cell, bg)
            set_cell_margins(cell, top=50, bottom=50, left=80, right=80)
            p = cell.paragraphs[0]
            run = p.add_run(v)
            run.font.size = Pt(8)
            if c_i == 0:
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                run.bold = True
            elif c_i == 3:
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER

    doc.save(output_filename)
    print(f"Generated DOCX: {output_filename} ({os.path.getsize(output_filename):,} bytes)")

def main():
    print("Generating Master Annual Curriculum DOCX...")
    build_curriculum_document(ANNUAL_COHORTS_DATA, "TARGET_ISH_REJASI_2026_2027.docx", is_master=True)
    build_curriculum_document(ANNUAL_COHORTS_DATA, "assets/TARGET_ISH_REJASI_2026_2027.docx", is_master=True)

    print("Generating Individual Cohort DOCX documents...")
    cohort_map = {
        "10-11-sinf": "assets/ISH_REJASI_10_11_SINF.docx",
        "9-sinf": "assets/ISH_REJASI_9_SINF.docx",
        "7-8-sinf": "assets/ISH_REJASI_7_8_SINF.docx",
        "5-6-sinf": "assets/ISH_REJASI_5_6_SINF.docx"
    }

    for c in ANNUAL_COHORTS_DATA:
        fname = cohort_map.get(c['id'])
        if fname:
            build_curriculum_document(ANNUAL_COHORTS_DATA, fname, is_master=False, single_cohort=c)

    print("Generating Vibecoding 108 Master DOCX...")
    build_vibecoding_only_docx("assets/YILLIK_ISH_REJASI_36_HAFTA_108_DARS.docx")

if __name__ == '__main__':
    main()
