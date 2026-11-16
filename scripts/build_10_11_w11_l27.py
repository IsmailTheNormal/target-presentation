#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
scripts/build_10_11_w11_l27.py — 10–11-sinf (11-hafta 27-dars)
Mavzu: Agent Xotirasi va Doimiy Kontekst: Epizodik, Semantik va Vector Cache
Track: Senior AI & Enterprise Kiberxavfsizlik Track
Duration: 80 daqiqa (Double block / 2-hour class)
"""

import os
import sys
import json
import re

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
LESSON_DIR = os.path.join(REPO_ROOT, "classes", "10-11-sinf", "11-hafta", "27-dars-agent-xotirasi-va-doimiy-kontekst")
SIM_DIR = os.path.join(LESSON_DIR, "simulator")
os.makedirs(SIM_DIR, exist_ok=True)

with open(os.path.join(REPO_ROOT, "assets", "TEMPLATE_PREZENTATSIYA.html"), "r", encoding="utf-8") as f:
    TPL_PRES = f.read()

with open(os.path.join(REPO_ROOT, "assets", "TEMPLATE_VARAQA.html"), "r", encoding="utf-8") as f:
    TPL_VAR = f.read()

with open(os.path.join(REPO_ROOT, "assets", "TEMPLATE_VAZIFA.html"), "r", encoding="utf-8") as f:
    TPL_VAZ = f.read()

def build_10_11_lesson():
    print("📦 Generating 10–11-sinf (27-dars: Agent Xotirasi va Doimiy Kontekst)...")

    title_uz = "27-dars: Agent Xotirasi va Doimiy Kontekst: Epizodik, Semantik va Vector Cache"
    title_ru = "Урок 27: Память AI Агентов: Эпизодическая, Семантическая и Векторный Кэш"
    title_en = "Lesson 27: AI Agent Memory: Episodic, Semantic & Vector Cache"

    # ============================================================
    # 1. PREZENTATSIYA.HTML (14 Slides, 80 Minutes)
    # ============================================================
    tpl = TPL_PRES
    tpl = re.sub(r"<title[^>]*>.*?</title>", f'<title data-ru="{title_ru}" data-en="{title_en}">{title_uz}</title>', tpl)
    tpl = re.sub(r'<span class="tag"[^>]*>.*?</span>', '<span class="tag" data-ru="10-11 · ВАЙБКОДИНГ" data-en="10-11 · VIBECODING">10-11 · VIBECODING</span>', tpl, count=1)
    tpl = tpl.replace('<span id="totalSlides">6</span>', '<span id="totalSlides">14</span>')

    titles_dict = {"uz": title_uz, "ru": title_ru, "en": title_en}
    titles_json = json.dumps(titles_dict, ensure_ascii=False, indent=2)
    tpl = re.sub(r'var TITLES\s*=\s*\{[\s\S]*?\};', f'var TITLES = {titles_json};', tpl)

    slides = []

    # Slide 1: Titul
    slides.append("""  <!-- SLIDE 1: TITUL -->
  <section class="slide is-on" data-phase="Kirish|Введение|Introduction" data-time="00:00–04:00">
    <div class="eyebrow" data-ru="10–11-СИНФ · 11-Я НЕДЕЛЯ · УРОК 27" data-en="GRADES 10–11 · WEEK 11 · LESSON 27">10–11-SINF · 11-HAFTA · 27-DARS</div>
    <h1 data-ru="Память AI Агентов: Эпизодическая, Семантическая и Векторный Кэш" data-en="AI Agent Memory: Episodic, Semantic & Vector Cache">Agent Xotirasi va Doimiy Kontekst: Epizodik, Semantik va Vector Cache</h1>
    <p class="lede" data-ru="Решаем проблему 'амнезии' LLM: от перегруженных контекстных окон к трехуровневой когнитивной памяти — оперативной (Scratchpad), эпизодической (SQLite) и семантической (ChromaDB Vector Store)." data-en="Curing LLM amnesia: transitioning from bloated context windows to 3-tier cognitive memory — Short-term (Scratchpad), Episodic (SQLite structured events), and Semantic (ChromaDB Vector Store).">LLM larning 'amneziya' (unutuvchanlik) muammosini hal qilamiz: to'lib ketuvchi prompt kontekstidan 3 bosqichli kognitiv xotiraga — tezkor (Scratchpad), epizodik voqealar tarixi (SQLite) va semantik ma'no xotirasi (ChromaDB Vector Store) arxitekturasiga o'tamiz.</p>
    <div class="grid c3" style="margin-top:24px;">
      <div class="card">
        <h3 data-ru="Формат занятия" data-en="Lesson Format">Format va Davomiylik</h3>
        <p data-ru="Спаренный блок: 2 x 40 минут = 80 минут Senior AI-инженерии" data-en="Double block: 2 x 40 min = 80 min Senior AI engineering">Juftlik blok: 2 x 40 daqiqa = 80 daqiqalik Senior AI muhandislik amaliyoti</p>
      </div>
      <div class="card">
        <h3 data-ru="Главная миссия" data-en="Core Mission">Amaliy Missiya</h3>
        <p data-ru="Спроектировать гибридный Memory Store с векторным поиском Top-K" data-en="Architect hybrid Memory Store with Top-K vector semantic retrieval">Top-K kosinus o'xshashlikka asoslangan gibrid Agent Memory Store tizimini qurish</p>
      </div>
      <div class="card">
        <h3 data-ru="10-Балльная система" data-en="10-Point Rubric">Baholash Mezoni</h3>
        <p data-ru="4 балла: Эпизодический SQLite · 4 балла: Top-K Vector Store · 2 балла: Compaction" data-en="4 pts: Episodic SQLite · 4 pts: Top-K Vector Store · 2 pts: Compaction">4 ball: Epizodik SQLite · 4 ball: Top-K Vector Store · 2 ball: Xotira siqish</p>
      </div>
    </div>
  </section>""")

    # Slide 2: HW Review (26-dars Tool Calling)
    slides.append("""  <!-- SLIDE 2: MANDATORY HW REVIEW & BRIDGE -->
  <section class="slide" data-phase="Uy Vazifasi Tahlili|Разбор Д/З|HW Review" data-time="04:00–10:00">
    <div class="eyebrow" data-ru="АНАЛИЗ Д/З · МОСТ К 27-УРОКУ" data-en="HOMEWORK AUDIT · BRIDGE TO LESSON 27">UY VAZIFASI TAHLILI · 26-DARS REVIZIYASI</div>
    <h2 data-ru="Разбор Домашнего Задания: Ограничения Tool Calling без Памяти" data-en="Homework Autopsy: Tool Calling Limits Without Memory">26-Dars Tahlili: Xotirasiz Tool Calling Cheklovlari</h2>
    <p class="lede" data-ru="На 26-уроке мы дали агенту 'руки' (JSON Schema Tool Calling). Но выяснилась критическая уязвимость: агент забывает результат инструмента сразу после завершения сессии!" data-en="Last lesson we equipped our agent with actuators (Tool Calling). Yet a critical vulnerability surfaced: the agent immediately forgets tool results upon session reset!">26-darsda agentga JSON Schema orqali tashqi vositalarni (Tool Calling) uladik. Lekin jiddiy kamchilik yuzaga keldi: seans tugashi bilan agent o'zi chaqirgan barcha natijalarni unutib yuboradi!</p>

    <div class="grid c2" style="margin-top:16px;">
      <div class="card" style="border-left:4px solid var(--accent);">
        <span class="pill" style="background:var(--accent-soft); color:var(--accent-ink);" data-ru="Типичная ошибка (Pitfall)" data-en="Common Pitfall">Xato Tahlili (Amneziya Qopqoni)</span>
        <h3 style="margin-top:8px;" data-ru="Повторный запуск дорогих инструментов" data-en="Re-executing expensive actuators">Bir Xil Toolni Qayta-Qayta Chaqirish</h3>
        <pre><code style="font-size:12px;">// ❌ XATO: Xotira yo'qligi sababli agent har safar
// og'ir SQL yoki pullik API ni qaytadan chaqiradi:
User: "Mening buyurtmam qayerda?"
Agent -> fetchShippingAPI(order_id) -> "Toshkentda"
--- Ertasi kuni ---
User: "U qayerda edi?"
Agent -> Hech narsani eslamaydi! API ni yana chaqiradi ($$$).</code></pre>
        <p style="font-size:12.5px; color:var(--ink-2); margin-top:6px;" data-ru="Без долговременной памяти агент тратит бюджет на повторные вызовы API и раздражает пользователя переспросами." data-en="Without persistent memory, agents burn API quotas re-querying identical data and lose contextual trust.">Doimiy xotirasiz agent har safar pul va vaqt sarflab bir xil API ni chaqiradi va foydalanuvchini charchatadi.</p>
      </div>

      <div class="card" style="border-left:4px solid var(--green);">
        <span class="pill" style="background:rgba(16,185,129,0.15); color:var(--green);" data-ru="Золотой Стандарт (Golden Solution)" data-en="Golden Standard">Oltin Yechim (Memory Cache)</span>
        <h3 style="margin-top:8px;" data-ru="Семантический кэш и SQLite история" data-en="Semantic Cache & SQLite History">Semantik Kesh va Epizodik Saqlash</h3>
        <pre><code style="font-size:12px;">// ✅ TOZA STANDART: Xotiradan qidirish (Retrieval)
User: "U qayerda edi?"
Agent -> memoryStore.query("order shipping status")
// Topilgan: "Buyurtma Toshkentda (2026-11-15)"
Agent -> "Kecha aytganimdek, Toshkent saralash markazida!"</code></pre>
        <p style="font-size:12.5px; color:var(--ink-2); margin-top:6px;" data-ru="Агент сначала опрашивает свою память! 0 миллисекунд задержки, $0 затрат на API и мгновенный ответ." data-en="Agent inspects its memory store first! Zero API overhead, zero token waste, and instant high-fidelity recall.">Agent avval o'z xotirasini tekshiradi! 0 ms kechikish, 0 dollar xarajat va insoniy do'stona muloqot.</p>
      </div>
    </div>

    <div class="card" style="margin-top:14px; background:rgba(255,255,255,0.7); display:flex; align-items:center; justify-content:space-between; gap:16px;">
      <div>
        <span class="pill" style="background:#00214a; color:#fff;" data-ru="30-Секундный Блиц" data-en="30-Second Blitz">30 Soniyalik Blitz</span>
        <b style="margin-left:8px;" data-ru="Почему нельзя просто бесконечно расширять контекстное окно (Prompt Context)?" data-en="Why can't we simply expand the raw prompt context window indefinitely?">Nega shunchaki butun tarixni System Prompt ichiga tiqib qo'yish mumkin emas?</b>
      </div>
      <div style="font-size:13px; font-weight:700; color:var(--green);" data-ru="Ответ: Lost in the Middle + Экспоненциальная цена" data-en="Answer: Lost in the Middle + Exponential Cost">Javob: "Lost in the Middle" xatosi va ulkan xarajat!</div>
    </div>
  </section>""")

    # Slide 3: Muammo — The Amnesia & Lost in the Middle Dilemma
    slides.append("""  <!-- SLIDE 3: PROBLEM -->
  <section class="slide" data-phase="Muammo|Проблема|Problem" data-time="10:00–16:00">
    <div class="eyebrow" data-ru="КОГНИТИВНЫЙ КРИЗИС LLM" data-en="COGNITIVE CRISIS OF LLMS">AQLIY HUJUM · REAL MUAMMO</div>
    <h2 data-ru="Проблема Амнезии и Синдром 'Lost in the Middle'" data-en="The Amnesia Problem & 'Lost in the Middle' Syndrome">LLM Amneziyasi va "Lost in the Middle" Inqirozi</h2>
    <p class="lede" data-ru="Языковая модель — это чистая математическая функция без состояния: f(x) = y. Каждый запуск начинается с чистого листа. Почему наивные решения не работают:" data-en="An LLM is fundamentally a stateless mathematical projection: f(x) = y. Every forward pass resets to blank canvas. Why naive memory hacks fail:">Til modeli tabiatan xotirasiz (stateless) matematik funksiyadir: har bir so'rov noldan boshlanadi. Oddiy yondashuvlarning 3 ta halokatli cheklovi:</p>

    <div class="grid c3" style="margin-top:20px;">
      <div class="card">
        <span class="pill" style="background:#fee2e2; color:#b91c1c;" data-ru="1. Финансовый Коллапс" data-en="1. Financial Bleed">1. Token Xarajati</span>
        <h3 style="margin-top:10px;" data-ru="Оплата за перечитывание" data-en="Paying to Re-read">100K Token Isrofi</h3>
        <p data-ru="Если каждый раз отправлять всю историю за месяц, за каждый короткий вопрос 'Привет' вы платите за чтение 100 000 токенов." data-en="Sending 30 days of conversation history forces paying input token fees on 100,000 tokens for a simple 'Hi'.">Har safar butun oylik suhbatni promptga qo'shib yuborish bitta "Salom" so'zi uchun 100,000 tokenga pul to'lashga majbur qiladi.</p>
      </div>

      <div class="card">
        <span class="pill" style="background:#fef3c7; color:#b45309;" data-ru="2. Потеря Внимания" data-en="2. Lost in the Middle">2. Lost in the Middle</span>
        <h3 style="margin-top:10px;" data-ru="Внимание рассеивается" data-en="Attention Degradation">O'rtada Adashish</h3>
        <p data-ru="Исследования Стэнфорда доказали: LLM отлично помнит начало и конец промпта, но факты в середине контекста теряются с вероятностью 60%!" data-en="Stanford research proved: LLMs recall facts at the head and tail of prompts, but miss mid-context details up to 60% of the time!">Stenford tadqiqoti: Model promptning boshi va oxirini yaxshi eslaydi, lekin o'rtada qolib ketgan faktlarni 60% ehtimol bilan e'tibordan qochiradi.</p>
      </div>

      <div class="card">
        <span class="pill" style="background:#ede9fe; color:#6d28d9;" data-ru="3. Загрязнение Контекста" data-en="3. Context Poisoning">3. Halokatli Shovqin</span>
        <h3 style="margin-top:10px;" data-ru="Галлюцинации и шум" data-en="Hallucinatory Noise">Kontekst Zaharlanishi</h3>
        <p data-ru="Устаревшие факты, ошибки трехдневной давности и отмененные команды сбивают рассуждения агента с правильного пути." data-en="Outdated instructions, stale debug logs, and superseded preferences mislead the agent's current ReAct reasoning chain.">Eski bekor qilingan buyruqlar va xatoliklar agentning joriy fikrlash zanjirini zaharlaydi va gallyutsinatsiyaga olib keladi.</p>
      </div>
    </div>
  </section>""")

    # Slide 4: 3-Tier Cognitive Memory Architecture
    slides.append("""  <!-- SLIDE 4: 3-TIER MEMORY ARCHITECTURE -->
  <section class="slide" data-phase="Arxitektura|Архитектура|Architecture" data-time="16:00–22:00">
    <div class="eyebrow" data-ru="ТРЕХУРОВНЕВАЯ МОДЕЛЬ ПАМЯТИ" data-en="3-TIER COGNITIVE MEMORY MODEL">INSON MIYASI MODELI · KOGNITIV ARXITEKTURA</div>
    <h2 data-ru="3 Уровня Памяти Агента: Working, Episodic, Semantic" data-en="The 3 Pillars of Agent Memory: Working, Episodic, Semantic">Agent Xotirasining 3 Ta Ustuni: Tezkor, Epizodik va Semantik</h2>
    <p class="lede" data-ru="Как и человеческий мозг, автономный агент разделяет кратковременную оперативную память, структурированный дневник событий и ассоциативную смысловую базу:" data-en="Mirrored after human neuroscience, an enterprise agent stratifies working scratchpad memory, episodic event journals, and associative semantic recall:">Inson miyasi kabi, zamonaviy avtonom agent ham xotirani 3 ta mustaqil qatlamga ajratadi:</p>

    <div class="grid c3" style="margin-top:20px;">
      <div class="card" style="border-top:3px solid var(--accent);">
        <span class="pill" style="background:var(--accent-soft); color:var(--accent-ink);" data-ru="1. Кратковременная (Working)" data-en="1. Working Memory">1. Tezkor Xotira (Scratchpad)</span>
        <h3 style="margin-top:10px;" data-ru="Текущий ReAct Контекст" data-en="Current ReAct Scratchpad">Joriy ReAct Tsikli</h3>
        <p data-ru="Хранится в оперативной памяти (RAM) текущего сеанса: Thought -> Action -> Observation последних 3-5 шагов." data-en="Transient in-RAM prompt buffer tracking immediate Thought -> Action -> Observation steps of active loop.">Joriy seans RAM xotirasida: oxirgi 3-5 ta fikrlash va vosita javoblari saqlanadi. Vazifa tugagach tozalanadi.</p>
        <div style="margin-top:8px; font-size:11px; font-family:'JetBrains Mono',monospace; color:var(--accent);">RAM · TTL: 1 Seans</div>
      </div>

      <div class="card" style="border-top:3px solid var(--blue);">
        <span class="pill" style="background:rgba(56,189,248,0.15); color:var(--blue);" data-ru="2. Эпизодическая (Episodic)" data-en="2. Episodic Memory">2. Epizodik Voqealar Tarixi</span>
        <h3 style="margin-top:10px;" data-ru="Хронологический Журнал" data-en="Chronological Journal">Strukturaviy SQLite Bazasi</h3>
        <p data-ru="Точный лог событий с метками времени: кто, когда, какую команду вызвал и какой статус вернулся (Success/Fail)." data-en="Relational event store timestamping user interactions, tool execution traces, and operational error logs.">Vaqt belgisi (timestamp) bilan yozilgan voqealar jurnali: qaysi foydalanuvchi qanday buyruq berdi va nima yuz berdi.</p>
        <div style="margin-top:8px; font-size:11px; font-family:'JetBrains Mono',monospace; color:var(--blue);">SQLite / PostgreSQL · Doimiy</div>
      </div>

      <div class="card" style="border-top:3px solid var(--green);">
        <span class="pill" style="background:rgba(16,185,129,0.15); color:var(--green);" data-ru="3. Семантическая (Semantic)" data-en="3. Semantic Memory">3. Semantik Ma'no Xotirasi</span>
        <h3 style="margin-top:10px;" data-ru="Векторные Эмбеддинги" data-en="Vector Embeddings Store">ChromaDB / Vektor Baza</h3>
        <p data-ru="Смысловая база знаний. Ищет не по точному совпадению слов, а по смысловой близости векторов (Cosine Similarity)." data-en="Dense embedding space indexing facts by conceptual meaning via Cosine Similarity rather than rigid keywords.">Faktlar va bilimlarni so'zma-so'z emas, ma'no o'xshashligi (Cosine Similarity) bo'yicha qidiruvchi vektorli xotira.</p>
        <div style="margin-top:8px; font-size:11px; font-family:'JetBrains Mono',monospace; color:var(--green);">ChromaDB / Faiss · Top-K</div>
      </div>
    </div>
  </section>""")

    # Slide 5: Episodic Memory in SQLite
    slides.append("""  <!-- SLIDE 5: EPISODIC SQLITE -->
  <section class="slide" data-phase="Epizodik Xotira|Эпизодическая Память|Episodic Storage" data-time="22:00–28:00">
    <div class="eyebrow" data-ru="РЕЛЯЦИОННАЯ ПАМЯТЬ СОБЫТИЙ" data-en="RELATIONAL EVENT LOGGING">STRUKTURAVIY SAQLASH · SQLITE SXEMASI</div>
    <h2 data-ru="Эпизодическая Память: Реляционный Журнал Событий" data-en="Episodic Memory: Relational Event Stream in SQLite">Epizodik Xotira: SQLite-da Voqealar Arxivi</h2>
    <p class="lede" data-ru="Каждое важное действие агента и предпочтение пользователя сохраняются в реляционной таблице с индексами:" data-en="Every deterministic agent action, user preference, and tool result is committed to a structured relational schema:">Agent amalga oshirgan har bir harakat va foydalanuvchi qoidalari SQLite relyatsion jadvalida indekslanib saqlanadi:</p>

    <div class="grid c2" style="margin-top:16px;">
      <div class="card">
        <span class="pill" style="background:#e0f2fe; color:#0369a1;" data-ru="Схема Таблицы agent_memories" data-en="agent_memories Table Schema">SQLite Sxemasi</span>
        <pre><code style="font-size:11px;">CREATE TABLE agent_memories (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  session_id TEXT NOT NULL,
  user_id TEXT NOT NULL,
  category TEXT CHECK(category IN ('preference','fact','error','task')),
  content TEXT NOT NULL,
  importance REAL DEFAULT 1.0, -- 1.0 dan 5.0 gacha
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_user_cat ON agent_memories(user_id, category);</code></pre>
      </div>

      <div class="card">
        <h3 data-ru="Как Агент Извлекает Эпизоды" data-en="Deterministic Episodic Retrieval">Epizodlarni Qidirish va Filtrlash</h3>
        <p style="font-size:12.5px; color:var(--ink-2); line-height:1.6;" data-ru="Перед ответом агент делает быстрый SQL-запрос для получения контекста конкретного пользователя:" data-en="Prior to prompt construction, the agent runs parameterized SQL queries retrieving verified user preferences:">Prompt yozilishidan oldin agent SQL so'rovi orqali foydalanuvchining shaxsiy preferensiyalarini yuklab oladi:</p>
        <pre><code style="font-size:11px;">SELECT content FROM agent_memories 
WHERE user_id = 'user_99' 
  AND category = 'preference' 
ORDER BY importance DESC LIMIT 5;</code></pre>
        <div style="margin-top:10px; font-size:12px; color:var(--green); font-weight:700;">
          ✓ Natija: Agent "Ali faqat Python va Dark Mode ishlatadi" degan faktni bilgan holda kod yozadi!
        </div>
      </div>
    </div>
  </section>""")

    # Slide 6: Semantic Memory & Vector Embeddings
    slides.append("""  <!-- SLIDE 6: SEMANTIC MEMORY & VECTOR SEARCH -->
  <section class="slide" data-phase="Semantik Xotira|Векторный Поиск|Vector Search" data-time="28:00–35:00">
    <div class="eyebrow" data-ru="ВЕКТОРНОЕ ПРОСТРАНСТВО СМЫСЛОВ" data-en="VECTOR EMBEDDING SPACE">MATEMATIK MA'NO · EMBEDDINGS & TOP-K</div>
    <h2 data-ru="Семантическая Память: Векторный Поиск и Косинусная Близость" data-en="Semantic Memory: Vector Embeddings & Cosine Similarity">Semantik Xotira: Vektor Qidiruv va Kosinus O'xshashlik</h2>
    <p class="lede" data-ru="Когда слов в запросе нет в базе точь-в-точь, на помощь приходит семантика: текст переводится в вектор из 1536 чисел:" data-en="When user phrasing deviates from stored keywords, semantic embeddings translate text into 1536-dimensional coordinate vectors:">Foydalanuvchi savolidagi so'zlar bazada aynan bir xil bo'lmasa, semantika yordamga keladi: matn 1536 o'lchamli vektorga aylantiriladi:</p>

    <div class="grid c2" style="margin-top:16px;">
      <div class="card">
        <h3 data-ru="Формула Косинусного Сходства (Cosine Similarity)" data-en="Cosine Similarity Geometry">Kosinus O'xshashlik Geometriyasi</h3>
        <div style="background:#0a0e17; padding:12px; border-radius:8px; margin:10px 0; text-align:center;">
          <div style="font-family:'JetBrains Mono',monospace; font-size:15px; color:#38bdf8; font-weight:700;">cos(θ) = (A · B) / (||A|| × ||B||)</div>
        </div>
        <ul style="margin-left:18px; line-height:1.8; font-size:12.5px; margin-top:8px;">
          <li data-ru="cos = 1.0 (0°): Смыслы абсолютно идентичны." data-en="cos = 1.0 (0°): Concepts are semantically identical."><b>cos = 1.0:</b> Ma'no 100% bir xil (masalan: "avtomobil" va "mashina").</li>
          <li data-ru="cos = 0.82: Высокая релевантность (подходит для инъекции в промпт)." data-en="cos = 0.82: High semantic proximity (inject into prompt)."><b>cos &gt; 0.75:</b> Yuqori bog'liqlik — agent promptiga qo'shiladi!</li>
          <li data-ru="cos = 0.10: Не связанный информационный шум (отбрасывается)." data-en="cos = 0.10: Irrelevant semantic noise (pruned away)."><b>cos &lt; 0.30:</b> Begona mavzu (filtrdan o'tkazilmaydi).</li>
        </ul>
      </div>

      <div class="card">
        <span class="pill" style="background:#fef3c7; color:#b45309;" data-ru="ChromaDB / LangChain Пайплайн" data-en="ChromaDB Retrieval Pipeline">Vektor Qidiruv Konveyeri</span>
        <pre><code style="font-size:11px;">// 1. Matnni vektorga aylantirish
const queryVector = await embed("Kiber-xavfsizlik parollari");

// 2. Vektor bazadan eng yaqin 3 ta xotirani tortish (Top-K)
const memories = await vectorDb.query({
  vector: queryVector,
  topK: 3,
  minSimilarity: 0.75
});

// 3. Promptga kontekst sifatida uzatish
const context = memories.map(m => m.text).join("\\n");</code></pre>
      </div>
    </div>
  </section>""")

    # Slide 7: Memory Compaction & Eviction
    slides.append("""  <!-- SLIDE 7: MEMORY COMPACTION -->
  <section class="slide" data-phase="Xotira Siqish|Сжатие Памяти|Memory Compaction" data-time="35:00–40:00">
    <div class="eyebrow" data-ru="ОПТИМИЗАЦИЯ И ОЧИСТКА КОНТЕКСТА" data-en="CONTEXT COMPACTION & HYGIENE">XOTIRANI TOZALASH · SUMMARIZATION BUFFER</div>
    <h2 data-ru="Сжатие Памяти: Summarization Buffer и Забывание Шума" data-en="Memory Hygiene: Summarization Buffers & Smart Eviction">Xotirani Siqish: Summarization Buffer va Keraksizni Unutish</h2>
    <p class="lede" data-ru="Хороший агент знает, что нужно помнить, а что — забыть. Нельзя хранить гигабайты бесполезных логов:" data-en="A mature agent excels at intentional forgetting: pruning transient noise while distilling dense, high-signal knowledge:">Yaxshi AI agent nimani eslab qolish va nimani unutish kerakligini biladi. 50 ta qatorli suhbat ixcham xulosaga siqiladi:</p>

    <div class="grid c2" style="margin-top:16px;">
      <div class="card">
        <h3 data-ru="Паттерн Summarization Buffer" data-en="Summarization Buffer Pattern">Summarization Buffer Mexanizmi</h3>
        <p style="font-size:12.5px; color:var(--ink-2); line-height:1.6;" data-ru="Когда количество сообщений превышает порог (например, 10), специальный фоновый агент сжимает первые 8 сообщений в плотное резюме из 2 предложений:" data-en="When dialogue turns exceed a safety threshold (e.g., 10 turns), a background summarizer condenses the oldest 8 turns into a tight 2-sentence summary:">Xabarlar soni 10 tadan oshganda, fon agenti dastlabki 8 ta xabarni 2 qatorlik ixcham xulosaga aylantiradi:</p>
        <div style="background:#0f172a; border-left:3px solid var(--accent); padding:10px; margin-top:8px; font-size:11.5px; color:#cbd5e1;">
          "Foydalanuvchi Ali PostgreSQL bazasida Users jadvali yaratdi va parollarni bcrypt bilan xeshlashni talab qildi."
        </div>
      </div>

      <div class="card">
        <h3 data-ru="Формула Оценки Важности Памяти" data-en="Memory Importance Scoring Function">Xotira Bahosi Formulasi</h3>
        <p style="font-size:12px; color:var(--ink-2);" data-ru="Стэнфордская архитектура генеративных агентов (Park et al., 2023):" data-en="Stanford Generative Agent Formula (Park et al., 2023):">Stenford generativ agentlar formulasi:</p>
        <div style="background:#0a0e17; padding:10px; border-radius:6px; margin:8px 0; font-family:'JetBrains Mono',monospace; font-size:12px; color:var(--green);">
          Score = α·Recency + β·Importance + γ·Relevance
        </div>
        <ul style="margin-left:18px; line-height:1.7; font-size:12px; margin-top:6px;">
          <li data-ru="Recency: Сколько часов назад произошло событие (затухание со временем)." data-en="Recency: Time elapsed since event creation (exponential decay)."><b>Recency:</b> Voqea qachon sodir bo'lgani (vaqt o'tishi bilan kamayadi).</li>
          <li data-ru="Importance: Насколько факт критичен (пароли, имена = 5.0, шутки = 1.0)." data-en="Importance: Criticality weight (passwords/names = 5.0, banter = 1.0)."><b>Importance:</b> Muhimlik darajasi (kalitlar, ismlar = 5.0).</li>
          <li data-ru="Relevance: Косинусная близость к текущему вопросу пользователя." data-en="Relevance: Cosine similarity distance to the active prompt."><b>Relevance:</b> Hozirgi savolga kosinus o'xshashligi.</li>
        </ul>
      </div>
    </div>
  </section>""")

    # Slide 8: In-Deck Interactive Simulator
    slides.append("""  <!-- SLIDE 8: IN-DECK INTERACTIVE SIMULATOR -->
  <section class="slide" data-phase="Jonli Sinov|Интерактив|Live Demo" data-time="40:00–48:00">
    <div class="eyebrow" data-ru="ИНТЕРАКТИВНЫЙ ТРЕНАЖЕР НА ЭКРАНЕ" data-en="INTERACTIVE SMARTBOARD LAB">JONLI XOTIRA SIMULYATORI</div>
    <h2 data-ru="Лаборатория Памяти: Запись, Индексация и Top-K Поиск" data-en="Live Memory Lab: Storage, Indexing & Top-K Retrieval">Smartboardda Agent Xotirasi va Semantik Qidiruv</h2>
    <p class="lede" data-ru="Добавляйте факты в базу памяти и проверяйте, как косинусный алгоритм находит нужный контекст даже при других словах в вопросе:" data-en="Commit facts to episodic store and verify how cosine semantic similarity retrieves the exact memory despite altered phrasing:">Xotiraga faktlar qo'shing va savol boshqa so'zlar bilan berilganda ham kosinus o'xshashlik qanday qilib to'g'ri xotirani topishini ko'ring:</p>

    <div class="grid c2" style="margin-top:14px; align-items:flex-start;">
      <!-- Memory Inspector Terminal -->
      <div class="card" style="padding:16px;">
        <div style="display:flex; justify-content:space-between; align-items:center;">
          <span class="pill" style="background:var(--accent-soft); color:var(--accent-ink);" data-ru="Agent Xotira Boshqaruvi" data-en="Agent Memory Controller">Agent Xotirasi</span>
          <span id="deckMemCount" style="font-size:11px; font-family:'JetBrains Mono',monospace; color:#38bdf8; font-weight:700;">3 ta Xotira Yozuvi</span>
        </div>
        
        <div id="deckMemList" style="margin-top:12px; height:130px; overflow-y:auto; background:#0b1120; border:1px solid #1e293b; border-radius:8px; padding:10px; font-family:'JetBrains Mono',monospace; font-size:11px; color:#cbd5e1; display:flex; flex-direction:column; gap:6px;">
          <div style="color:#94a3b8;">[1] user_pref: "Foydalanuvchi Rust va Python dasturchisi" (imp: 4.5)</div>
          <div style="color:#94a3b8;">[2] episodic: "PostgreSQL porti 5432 ga sozlangan" (imp: 3.0)</div>
          <div style="color:#94a3b8;">[3] security: "API kalit .env faylida saqlanishi shart" (imp: 5.0)</div>
        </div>

        <div style="margin-top:10px; display:flex; gap:6px;">
          <input type="text" id="deckMemQuery" value="Qaysi dasturlash tilida kod yozay?" style="flex:1; padding:6px 10px; font-size:11px; background:#0f172a; border:1px solid #334155; border-radius:6px; color:#fff;" />
          <button class="btn" onclick="queryDeckMemory()" style="background:var(--accent); color:#fff; border-color:var(--accent); font-size:11px;" data-ru="🔍 Top-K Поиск" data-en="🔍 Top-K Retrieval">🔍 Top-K Qidirish</button>
        </div>
      </div>

      <!-- Top-K Retrieval Result -->
      <div class="card">
        <h3 data-ru="Результат Векторного Извлечения (Top-1)" data-en="Retrieved Memory (Top-1 Match)">Tanlangan Eng Yaqin Xotira (Top-1)</h3>
        <div style="margin-top:8px; display:flex; flex-direction:column; gap:6px;">
          <div style="font-size:11.5px; font-family:'JetBrains Mono',monospace; background:rgba(0,0,0,0.25); padding:10px; border-radius:6px; line-height:1.6;">
            <div>Match Score: <span id="deckScore" style="color:var(--green); font-weight:700;">0.89 (High Relevance)</span></div>
            <div>Retrieved: <span id="deckRetrievedText" style="color:#38bdf8; font-weight:700;">"Foydalanuvchi Rust va Python dasturchisi"</span></div>
            <div>Injected Prompt: <span id="deckPromptSnippet" style="color:var(--accent);">System: Remember user prefers Rust/Python</span></div>
          </div>
          <div style="display:flex; gap:6px; margin-top:4px;">
            <button class="btn" onclick="addSampleMemory()" style="font-size:11px; padding:4px 8px;" data-ru="+ Добавить Факт" data-en="+ Insert Memory">+ Fakt Qo'shish</button>
            <button class="btn" onclick="compactDeckMemory()" style="font-size:11px; padding:4px 8px;" data-ru="📦 Сжать Память" data-en="📦 Compact Memory">📦 Xotirani Siqish</button>
          </div>
        </div>
      </div>
    </div>
  </section>""")

    # Slide 9: Interactive Quiz
    slides.append("""  <!-- SLIDE 9: QUIZ -->
  <section class="slide" data-phase="Viktorina|Квиз|Interactive Quiz" data-time="48:00–54:00">
    <div class="eyebrow" data-ru="ПРОВЕРКА ЗНАНИЙ (3 ВОПРОСА)" data-en="KNOWLEDGE CHECK (3 QUESTIONS)">INTERAKTIV QUIZ</div>
    <h2 data-ru="Блиц-Тест: Архитектура Памяти AI Агентов" data-en="Fast Quiz: AI Agent Memory Architecture">Bilimni Sinash: Agent Xotirasi va Vektorlar</h2>
    <div class="grid c3" style="margin-top:16px;">
      <!-- Q1 -->
      <div class="card quiz-card">
        <span class="pill" data-ru="Вопрос 1" data-en="Question 1">1-Savol</span>
        <h4 style="margin:10px 0;" data-ru="Какая память очищается сразу после завершения шага ReAct?" data-en="Which memory layer clears immediately after a ReAct step?">ReAct tsikli tugashi bilan qaysi xotira tozalanadi?</h4>
        <div style="display:flex; flex-direction:column; gap:6px; margin-top:8px;">
          <button class="btn" onclick="checkDeckQuiz(this, true)" style="text-align:left; font-size:11.5px;" data-ru="A) Working Memory (Scratchpad в RAM)" data-en="A) Working Memory (RAM Scratchpad)">A) Working Memory (RAM Scratchpad)</button>
          <button class="btn" onclick="checkDeckQuiz(this, false)" style="text-align:left; font-size:11.5px;" data-ru="B) SQLite база данных" data-en="B) SQLite database">B) SQLite bazasi</button>
          <button class="btn" onclick="checkDeckQuiz(this, false)" style="text-align:left; font-size:11.5px;" data-ru="C) ChromaDB векторное хранилище" data-en="C) ChromaDB vector store">C) ChromaDB vektor ombori</button>
        </div>
      </div>

      <!-- Q2 -->
      <div class="card quiz-card">
        <span class="pill" data-ru="Вопрос 2" data-en="Question 2">2-Savol</span>
        <h4 style="margin:10px 0;" data-ru="Что измеряет косинусное сходство (Cosine Similarity)?" data-en="What does Cosine Similarity quantify?">Kosinus o'xshashlik nimani hisoblaydi?</h4>
        <div style="display:flex; flex-direction:column; gap:6px; margin-top:8px;">
          <button class="btn" onclick="checkDeckQuiz(this, false)" style="text-align:left; font-size:11.5px;" data-ru="A) Количество одинаковых букв" data-en="A) Count of identical letters">A) Bir xil harflar sonini</button>
          <button class="btn" onclick="checkDeckQuiz(this, true)" style="text-align:left; font-size:11.5px;" data-ru="B) Смысловую близость двух векторных эмбеддингов" data-en="B) Semantic proximity of two embedding vectors">B) Ikki vektor orasidagi ma'no yaqinligini</button>
          <button class="btn" onclick="checkDeckQuiz(this, false)" style="text-align:left; font-size:11.5px;" data-ru="C) Скорость интернет соединения" data-en="C) Internet connection speed">C) Internet tezligini</button>
        </div>
      </div>

      <!-- Q3 -->
      <div class="card quiz-card">
        <span class="pill" data-ru="Вопрос 3" data-en="Question 3">3-Savol</span>
        <h4 style="margin:10px 0;" data-ru="Зачем нужен Summarization Buffer?" data-en="Why is a Summarization Buffer required?">Summarization Buffer nima uchun kerak?</h4>
        <div style="display:flex; flex-direction:column; gap:6px; margin-top:8px;">
          <button class="btn" onclick="checkDeckQuiz(this, false)" style="text-align:left; font-size:11.5px;" data-ru="A) Чтобы удалять пароли" data-en="A) To delete passwords">A) Parollarni o'chirib tashlash uchun</button>
          <button class="btn" onclick="checkDeckQuiz(this, true)" style="text-align:left; font-size:11.5px;" data-ru="B) Чтобы сжимать старый диалог и экономить токены" data-en="B) To condense dialogue and save token budget">B) Eski suhbatni siqib, token va pulni tejash uchun</button>
          <button class="btn" onclick="checkDeckQuiz(this, false)" style="text-align:left; font-size:11.5px;" data-ru="C) Чтобы выключать компьютер" data-en="C) To turn off the computer">C) Kompyuterni o'chirish uchun</button>
        </div>
      </div>
    </div>
  </section>""")

    # Slide 10: 25-Min Practice Cyber Arena
    slides.append("""  <!-- SLIDE 10: ARENA LAB -->
  <section class="slide" data-phase="Amaliyot|Практика|Hands-on Lab" data-time="54:00–69:00">
    <div class="eyebrow" data-ru="БОЛЬШАЯ ПРАКТИЧЕСКАЯ АРЕНА (25 МИНУТ)" data-en="25-MINUTE CYBER ARENA">AMALIY ARENA</div>
    <h2 data-ru="Задание: Собери Гибридный Memory Store для Агента" data-en="Mission: Architect Hybrid Memory Store for Autonomous Agent">Kiber-Missiya: Agent Uchun Gibrid Xotira Tizimini Qurish</h2>
    <p class="lede" data-ru="Откройте симулятор simulator/index.html и выполните 3 инженерных шага за 25 минут:" data-en="Launch simulator/index.html and accomplish 3 engineering milestones within 25 minutes:">Kompyuteringizda <b>simulator/index.html</b> faylini oching va 25 daqiqada 3 ta xotira bosqichini bajaring:</p>
    
    <div class="grid c2" style="margin-top:16px;">
      <div class="card">
        <h3 data-ru="Чек-лист AI Инженера" data-en="AI Engineer Checklist">Muhandislik Bosqichlari</h3>
        <ol style="margin-left:18px; line-height:1.8; font-size:13px; margin-top:8px;">
          <li data-ru="Создать таблицу agent_memories в SQLite и записать 3 ключевых факта" data-en="Create agent_memories table in SQLite and insert 3 critical facts">SQLite-da <code>agent_memories</code> jadvalini yaratib, 3 ta asosiy faktni yozish</li>
          <li data-ru="Реализовать вычисление Cosine Similarity и Top-K фильтрацию по порогу 0.75" data-en="Implement Cosine Similarity scoring and Top-K filter at 0.75 threshold">Kosinus o'xshashlik formulasini yozib, 0.75 dan yuqori Top-K xotiralarni ajratish</li>
          <li data-ru="Смоделировать Summarization Buffer: сжать 6 сообщений в 1 итоговый факт" data-en="Simulate Summarization Buffer: condense 6 chat turns into 1 memory snapshot">6 ta xabardan iborat suhbatni 1 ta ixcham xulosaga aylantiruvchi buferni ulash!</li>
        </ol>
        <div style="margin-top:16px;">
          <a href="simulator/index.html" target="_blank" class="btn" style="text-decoration:none; display:inline-flex; align-items:center; gap:8px; font-size:13px; font-weight:700; padding:10px 18px; background:var(--accent); color:#fff; border-color:var(--accent);" data-ru="🚀 Открыть Симулятор Памяти (simulator/index.html)" data-en="🚀 Launch Memory Studio (simulator/index.html)">🚀 Xotira Studiyasini Ochish (simulator/index.html)</a>
        </div>
      </div>

      <!-- Live 25-Min Timer Card -->
      <div class="card" style="text-align:center; padding:16px;">
        <span class="pill" data-ru="Таймер Лаборатории" data-en="Arena Timer">Arena Taymeri</span>
        <div id="deckTimerDisplay" style="font-family:'JetBrains Mono',monospace; font-size:44px; font-weight:800; color:var(--accent); margin:12px 0;">25:00</div>
        <div style="display:flex; justify-content:center; gap:8px;">
          <button class="btn" id="deckTimerBtn" onclick="toggleDeckTimer()" data-ru="▶ Старт (25 мин)" data-en="▶ Start (25m)">▶ Boshlash (25m)</button>
          <button class="btn" onclick="resetDeckTimer()" data-ru="🔄 Сброс" data-en="🔄 Reset">🔄 Qayta o'rnatish</button>
        </div>
        <div style="font-size:12px; color:var(--ink-2); margin-top:10px;" data-ru="Учитель проходит по рядам и помогает настроить Top-K порог" data-en="Teacher navigates floor assisting vector math and Top-K thresholds">O'qituvchi sinf bo'ylab aylanib, kosinus formulasi va Top-K filtrini sozlashda yordam beradi</div>
      </div>
    </div>
  </section>""")

    # Slide 11: Peer Review
    slides.append("""  <!-- SLIDE 11: PEER REVIEW -->
  <section class="slide" data-phase="Kiber-Audit|Код-Ревью|Peer Review" data-time="69:00–74:00">
    <div class="eyebrow" data-ru="ПАРНЫЙ АУДИТ КАЧЕСТВА" data-en="PAIR QUALITY CONTROL">JUFTLIKDA PEER-REVIEW (KIBER-AUDIT)</div>
    <h2 data-ru="Обменяйтесь Экранами: Чек-лист из 4 Пунктов" data-en="Swap Screens: 4-Point Memory Checklist">Partadosh Bilan Almashing: 4 Bosqichli Xotira Auditi</h2>
    <p class="lede" data-ru="Инженерное правило: агент не считается надежным, пока напарник не попытался запутать его память противоречивыми фактами:" data-en="Engineering standard: memory engines must be rigorously stress-tested against contradictory facts and threshold bleed:">Professional muhandislik qoidasi: sherigingiz ataylab chalkash faktlar berib tekshirmaguncha xotira kodi tayyor hisoblanmaydi. Partadoshingiz tizimini sinang:</p>

    <div class="grid c2" style="margin-top:16px;">
      <div class="card">
        <h3 data-ru="Чек-лист Инспекции" data-en="Inspection Checklist">Tekshirish Mezonlari</h3>
        <ul style="margin-left:18px; line-height:2.0; font-size:13px; margin-top:8px;">
          <li data-ru="[ ] Структура SQLite: Поля user_id, category и importance присутствуют." data-en="[ ] SQLite Schema: user_id, category, and importance fields exist.">[ ] <b>SQLite Sxemasi:</b> <code>user_id</code>, <code>category</code> va <code>importance</code> ustunlari to'g'rimi?</li>
          <li data-ru="[ ] Порог Top-K: Факты с близостью ниже 0.70 отсекаются и не засоряют промпт." data-en="[ ] Top-K Threshold: Matches below 0.70 are strictly pruned.">[ ] <b>Top-K Chegarasi:</b> 0.70 dan past bo'lgan keraksiz ma'lumotlar filtrlanadimi?</li>
          <li data-ru="[ ] Дедупликация: Одинаковые факты не дублируются в памяти дважды." data-en="[ ] Deduplication: Identical memories are updated rather than duplicated.">[ ] <b>Deduplikatsiya:</b> Bir xil fakt ikki marta takrorlanmasdan yangilanadimi?</li>
          <li data-ru="[ ] Сжатие буфера: При 6+ сообщениях генерируется лаконичное резюме." data-en="[ ] Summarization: Dialogue collapses into dense memory summary.">[ ] <b>Xotira Siqilishi:</b> Ko'p xabarlar qisqa va aniq xulosaga keltirilganmi?</li>
        </ul>
      </div>

      <div class="card" style="display:flex; flex-direction:column; justify-content:center; text-align:center;">
        <div style="font-size:36px; margin-bottom:8px;">🧠💾⚡</div>
        <h3 data-ru="Роль: Senior AI Systems Architect" data-en="Role: Senior AI Systems Architect">Siz Bosh AI Arxitektorsiz!</h3>
        <p style="font-size:12.5px; color:var(--ink-2); margin-top:6px;" data-ru="Если агент соседа вытащил лишний факт — помогите ему поднять порог косинусного сходства до 0.80!" data-en="If your peer's agent retrieved noisy context — guide them to raise similarity cutoff to 0.80!">Agar partadoshingiz agenti keraksiz xotirani chiqarib yuborsa — unga kosinus chegarasini 0.80 ga ko'tarishni o'rgating!</p>
      </div>
    </div>
  </section>""")

    # Slide 12: Showcase Demo
    slides.append("""  <!-- SLIDE 12: SHOWCASE DEMO -->
  <section class="slide" data-phase="Taqdimot|Демонстрация|Showcase Arena" data-time="74:00–77:00">
    <div class="eyebrow" data-ru="ДЕМОНСТРАЦИЯ ПАМЯТИ НА ДОСКЕ" data-en="SMARTBOARD MEMORY SHOWCASE">O'QUVCHILAR DEMOSI</div>
    <h2 data-ru="Презентация Разработанных Memory Движков" data-en="Student Memory Engine Showcase">Kiber-Showcase: Katta Ekranda Xotira Tizimi Demosi</h2>
    <p class="lede" data-ru="2 лучшие пары учеников подключаются к экрану и демонстрируют извлечение контекста из базы памяти:" data-en="Top 2 student pairs present their vector memory engines retrieving context live on the smartboard:">Eng tezkor 2 ta juftlik doskaga chiqib o'zlarining xotira dvigatelini butun sinf oldida namoyish etadi:</p>

    <div class="grid c2" style="margin-top:16px;">
      <div class="card" style="text-align:center; padding:20px;">
        <span class="pill" style="background:var(--accent-soft); color:var(--accent-ink);" data-ru="Демо 1" data-en="Demo 1">Demo 1</span>
        <h3 style="margin-top:10px;" data-ru="Семантический Recall" data-en="Semantic Recall">Semantik Recall Demosi</h3>
        <p style="font-size:12.5px; color:var(--ink-2);" data-ru="Показ поиска факта при полностью перефразированном вопросе пользователя." data-en="Demonstrate exact fact recall under completely rephrased user input.">Foydalanuvchi savolni butunlay boshqa so'zlar bilan berganida ham agent faktni qanday topishini ko'rsatish.</p>
      </div>
      <div class="card" style="text-align:center; padding:20px;">
        <span class="pill" style="background:rgba(16,185,129,0.15); color:var(--green);" data-ru="Демо 2" data-en="Demo 2">Demo 2</span>
        <h3 style="margin-top:10px;" data-ru="Динамический Summarizer" data-en="Dynamic Summarizer">Dinamik Siqish Demosi</h3>
        <p style="font-size:12.5px; color:var(--ink-2);" data-ru="Демонстрация сжатия 10 шагов сложного дебага в 2 строки структурированной памяти." data-en="Demonstrate compacting 10 debugging steps into 2 dense lines of persistent memory.">10 ta qadamli uzun xatoliklar tarixini 2 qatorlik toza xulosaga siqib xotiraga yozishni namoyish etish.</p>
      </div>
    </div>
  </section>""")

    # Slide 13: 3-Tier Homework
    slides.append("""  <!-- SLIDE 13: HOMEWORK -->
  <section class="slide" data-phase="Uy Vazifasi|Домашнее Задание|Tiered Homework" data-time="77:00–79:00">
    <div class="eyebrow" data-ru="ДОМАШНЕЕ ЗАДАНИЕ (10 БАЛЛОВ)" data-en="HOMEWORK ASSIGNMENT (10 POINTS)">MUSTAQIL AMALIYOT</div>
    <h2 data-ru="3 Уровня Домашнего Задания" data-en="3-Tiered Homework Assignment">10 Ballik Mezonli 3 Darajali Uy Vazifasi</h2>
    <p class="lede" data-ru="Задание выполняется в интерактивном приложении vazifa.html с автосохранением в браузере:" data-en="Complete your tasks inside the standalone vazifa.html app featuring local autosave:">Vazifa <b>vazifa.html</b> ilovasida bajariladi va brauzer xotirasida (LocalStorage) avtomatik saqlanadi:</p>

    <div class="grid c3" style="margin-top:20px;">
      <div class="card" style="border-top:3px solid var(--ink);">
        <span class="pill" data-ru="1-Уровень: База" data-en="Tier 1: Base">1-Bosqich: Baza</span>
        <div style="font-size:18px; font-weight:800; color:var(--accent); margin:6px 0;">4 BALL</div>
        <h3 data-ru="Эпизодический SQLite" data-en="Episodic SQLite">Epizodik Xotira Klient</h3>
        <p data-ru="Написать функции addMemory(userId, cat, text) и getMemories(userId, cat)." data-en="Author addMemory(userId, cat, text) and getMemories(userId, cat) queries.">Foydalanuvchi bo'yicha xotiraga yozuvchi va toifalar bo'yicha saralab oluvchi funksiyalarni yozish.</p>
      </div>

      <div class="card" style="border-top:3px solid var(--accent);">
        <span class="pill" data-ru="2-Уровень: Проект" data-en="Tier 2: Engineering">2-Bosqich: Muhandislik</span>
        <div style="font-size:18px; font-weight:800; color:var(--accent); margin:6px 0;">4 BALL</div>
        <h3 data-ru="Top-K Векторный Поиск" data-en="Top-K Vector Retrieval">Top-K Kosinus Qidiruvi</h3>
        <p data-ru="Реализовать cosineSimilarity(vecA, vecB) и функцию извлечения Top-K релевантных фактов." data-en="Implement cosineSimilarity(vecA, vecB) and Top-K threshold retrieval router.">Ikkita vektor o'rtasidagi kosinus burchagini hisoblovchi va Top-K xotirani chiqaruvchi funksiya yozish.</p>
      </div>

      <div class="card" style="border-top:3px solid var(--green);">
        <span class="pill" data-ru="3-Уровень: Вызов" data-en="Tier 3: Challenge">3-Bosqich: Kiber-Sinov</span>
        <div style="font-size:18px; font-weight:800; color:var(--green); margin:6px 0;">2 BALL</div>
        <h3 data-ru="Summarization Buffer" data-en="Summarization Buffer">Avto-Siqish Dvigateli</h3>
        <p data-ru="Написать логику сжатия: если буфер превышает N сообщений, архивировать старые в единое резюме." data-en="Engineer auto-compaction: when buffer exceeds N turns, archive older turns into dense summary.">Xabarlar N tadan oshganda, eski ma'lumotlarni ixcham xulosaga aylantirib saqlovchi algoritm qurish.</p>
      </div>
    </div>
  </section>""")

    # Slide 14: Summary & Bridge
    slides.append("""  <!-- SLIDE 14: SUMMARY & BRIDGE -->
  <section class="slide" data-phase="Xulosa|Итоги|Summary & Bridge" data-time="79:00–80:00">
    <div class="eyebrow" data-ru="ИТОГИ УРОКА И АНОНС СЛЕДУЮЩЕГО ДНЯ" data-en="LESSON SUMMARY & NEXT HORIZONS">DARS XULOSASI VA KELGUSI QADAM</div>
    <h2 data-ru="Память — Мост к Истинному Интеллекту Агентов" data-en="Memory: The Bridge to True Autonomous Intelligence">Xotira — Haqiqiy Avtonom Intellekt Kalitidir</h2>
    <p class="lede" data-ru="Сегодня мы превратили забывчивый чат-бот в когнитивную систему, помнящую контекст, ошибки и предпочтения пользователей!" data-en="Today we elevated our agent beyond ephemeral chat amnesia into a stateful cognitive system with persistent recall!">Bugun biz oddiy unutuvchan botdan foydalanuvchining afzalliklari, o'tmishdagi xatolari va tizim bilimlarini eslab qoluvchi barqaror AI tizimiga qadam qo'ydik!</p>

    <div class="grid c2" style="margin-top:20px;">
      <div class="card">
        <h3 data-ru="Что мы освоили сегодня" data-en="Today's Milestones">Bugungi Yutuqlarimiz</h3>
        <ul style="margin-left:18px; line-height:1.8; font-size:13px; margin-top:8px;">
          <li data-ru="Разобрали проблему Lost in the Middle и архитектуру 3 уровней памяти." data-en="Deconstructed Lost in the Middle and mastered the 3-tier memory model.">Lost in the Middle muammosi va xotiraning 3 ta ustuni (Working, Episodic, Semantic) ni o'rgandik.</li>
          <li data-ru="Построили схему SQLite для хронологического архивирования фактов и предпочтений." data-en="Engineered relational SQLite schema for structured chronological event logging.">SQLite da vaqt va muhimlik darajasiga ega bo'lgan epizodik xotira sxemasini qurdik.</li>
          <li data-ru="Освоили косинусное сходство векторов и механизм сжатия Summarization Buffer." data-en="Mastered vector Cosine Similarity Top-K search and Summarization Buffer compaction.">Vektorlar bo'yicha Top-K qidiruv va Summarization Buffer orqali xotirani siqishni amalda qo'lladik.</li>
        </ul>
      </div>

      <div class="card" style="background:#00214a; color:#fff;">
        <span class="pill" style="background:var(--accent); color:#fff;" data-ru="Следующий Шаг" data-en="Next Horizon">Kelgusi Darsimizda</span>
        <h3 style="color:#fff; margin-top:8px;" data-ru="Автономные Код-Агенты (Autonomous Coding)" data-en="Autonomous Coding Agents">Avtonom Kod Yozuvchi Agentlar</h3>
        <p style="font-size:12.5px; color:#cbd5e1; margin-top:6px;" data-ru="Мы научим нашего агента с памятью и инструментами автономно писать тесты, править баги в репозитории и делать коммиты!" data-en="We will empower our memory-equipped agent to autonomously author unit tests, patch bugs in codebases, and push commits!">Xotira va vositalar bilan qurollangan agentimizga mustaqil test yozish, repozitoriydagi xatolarni tuzatish va commit qilishni o'rgatamiz!</p>
      </div>
    </div>
  </section>""")

    # Inject slides into presentation
    all_slides_html = "\n\n".join(slides)
    tpl = re.sub(r'<div class="stage">[\s\S]*?</div><!-- /stage -->', f'<div class="stage">\n{all_slides_html}\n</div><!-- /stage -->', tpl)

    # Teacher notes
    notes = {
        "uz": [
            ["Darsga Kirish", "10–11-sinflar bilan 27-darsga xush kelibsiz. Agent xotirasi mavzusini e'lon qiling.", "Doskaga inson miyasi va SQLite/Vektor belgilarini chizing."],
            ["Uy Vazifasi Tahlili", "26-darsdagi Tool Calling natijalari sessiya tugashi bilan unutilishi xatosini ko'rsating.", "30 soniyalik blits savolini bering."],
            ["Muammo: LLM Amneziyasi", "Nega model tabiatan xotirasiz ekani va butun matnni promptga tiqish qimmatga tushishini tushuntiring.", "Stenfordning 'Lost in the Middle' tadqiqotini eslating."],
            ["3 Qatlamli Kognitiv Model", "Working (RAM), Episodic (SQLite) va Semantic (Vektor) xotira farqini chizing.", "Inson psixologiyasi bilan analogiya keltiring."],
            ["Epizodik Xotira va SQLite", "agent_memories jadvali sxemasi va indekslarini tushuntiring.", "Foydalanuvchi preferensiyalarini SQL orqali yuklashni ko'rsating."],
            ["Semantik Xotira va Vektorlar", "Matn qanday qilib 1536 o'lchamli vektorga aylanishini doskada ko'rsating.", "Kosinus o'xshashlik formulasi va Top-K saralashini tushuntiring."],
            ["Xotirani Siqish va Tozalash", "Summarization Buffer qanday ishlashini tushuntiring.", "Park et al. (2023) ahamiyatlilik bahosi formulasini bering."],
            ["Jonli Simulyator", "Smartboardda xotira qidiruvi va Top-1 natijasini ko'rsating.", "O'quvchilarni ekranga chaqirib yangi fakt qo'shing."],
            ["Interaktiv Kiber-Quiz", "3 ta savol bo'yicha blits o'tkazing va to'g'ri javoblarni belgilang.", "Natijalarni mustahkamlang."],
            ["25 Minutlik Kiber-Arena", "O'quvchilar simulator/index.html da xotira tizimini quryapti. Taymerni yoqing.", "Sinf bo'ylab aylanib kosinus chegarasini sozlashda yordam bering."],
            ["Juftlikda Peer-Review", "O'quvchilar partadoshining xotirasini 4 ta mezon bo'yicha sinaydilar.", "Chalkash faktlar kiritib test qilsinlar."],
            ["O'quvchilar Demosi", "2 ta juftlik doskaga chiqib o'zlarining semantik qidiruvini ko'rsatadi.", "Toza yechimlarni olqishlang."],
            ["3 Darajali Uy Vazifasi", "vazifa.html ilovasidagi 10 ballik mezonni tushuntiring. Local auto-save borligini eslating.", "O'quvchilarga formatni tushuntiring."],
            ["Dars Xulosasi", "Kelgusi darsdagi Avtonom Kod Yozuvchi Agentlar mavzusini anons qiling.", "Faol o'quvchilarni baholang."]
        ],
        "ru": [
            ["Введение в Урок", "Приветствие 10–11 классов на 27-м уроке. Анонсируйте тему памяти AI-агентов.", "Нарисуйте схему мозга и векторной БД на доске."],
            ["Разбор Д/З", "Вспомните 26-й урок. Покажите проблему забывания результатов инструментов после сеанса.", "Задайте 30-секундный блиц-вопрос."],
            ["Проблема Амнезии", "Почему LLM stateless и почему нельзя пихать всю историю в промпт.", "Расскажите про стэнфордский феномен Lost in the Middle."],
            ["3 Уровня Памяти", "Объясните различия Working (RAM), Episodic (SQLite) и Semantic (ChromaDB).", "Проведите аналогию с памятью человека."],
            ["Эпизодическая Память", "Покажите схему таблицы agent_memories и индексы.", "Объясните выборку предпочтений пользователя через SQL."],
            ["Семантическая Память", "Как текст превращается в вектор из 1536 измерений.", "Объясните формулу косинусного сходства и Top-K фильтрацию."],
            ["Сжатие и Очистка Памяти", "Как Summarization Buffer сжимает старые сообщения.", "Разберите формулу важности памяти из исследования Стэнфорда."],
            ["Живой Демо-Тренажер", "Покажите семантический поиск фактов на смартборде.", "Вызовите учеников добавить новый факт в базу."],
            ["Интерактивный Квиз", "Проведите блиц по 3 вопросам и закрепите пройденные концепты.", "Нажимайте варианты ответов на экране."],
            ["Практическая Арена", "Ученики открывают simulator/index.html. Запустите 25-минутный таймер.", "Помогайте парам учеников настраивать векторный порог."],
            ["Парный Код-Ревью", "Ученики меняются экранами и тестируют память по 4 критериям.", "Проверьте фильтрацию нерелевантного контекста."],
            ["Демонстрация Работ", "2 пары выходят к доске и показывают семантическое извлечение фактов.", "Похвалите лучшие архитектурные решения."],
            ["Домашнее Задание 10 Баллов", "Разберите 10-балльную рубрику в vazifa.html и напомните об автосохранении.", "Покажите интерфейс приложения."],
            ["Итоги и Анонс", "Анонсируйте тему автономных код-агентов на следующем занятии.", "Выставите оценки за занятие."]
        ],
        "en": [
            ["Lesson Introduction", "Welcome Grades 10–11 to Lesson 27. Announce AI Agent Memory Architecture.", "Sketch neural cognition and vector storage on board."],
            ["Homework Review", "Revisit tool calling from Lesson 26. Expose the amnesia vulnerability after session close.", "Prompt 30-second blitz question."],
            ["The Amnesia Dilemma", "Explain why LLMs are stateless functions and why naive prompt stuffing fails.", "Cite Stanford's Lost in the Middle research findings."],
            ["3-Tier Cognitive Model", "Diagram Working (RAM), Episodic (SQLite), and Semantic (ChromaDB) tiers.", "Draw parallels with human neurobiology."],
            ["Episodic SQLite Store", "Inspect agent_memories table schema, columns, and indexed queries.", "Showcase parameterized user preference retrieval."],
            ["Semantic Vector Memory", "Explain how text projects into 1536-dimensional embedding vectors.", "Deconstruct Cosine Similarity geometry and Top-K retrieval."],
            ["Memory Compaction", "Explain how Summarization Buffers distill conversation history.", "Analyze Stanford's memory importance scoring equation."],
            ["In-Deck Live Simulator", "Demonstrate semantic recall and Top-1 match live on the smartboard.", "Invite students to insert new facts into memory."],
            ["Interactive Cyber Quiz", "Run rapid blitz check on 3 questions to solidify concepts.", "Click quiz choices on smartboard."],
            ["25-Min Cyber Arena", "Students launch simulator/index.html. Start 25-min timer.", "Guide student pairs across the room tuning similarity thresholds."],
            ["Peer Review Quality Audit", "Students swap screens auditing memory engines across 4 checkpoints.", "Test with adversarial contradictory inputs."],
            ["Student Showcase Arena", "2 student pairs take the smartboard demonstrating semantic recall.", "Celebrate clean systems engineering."],
            ["Tiered Homework Rubric", "Explain 10-point rubric in vazifa.html and highlight local autosave in browser.", "Preview homework web application."],
            ["Summary & Next Horizon", "Tease Autonomous Coding Agents for the upcoming session.", "Record student achievements."]
        ]
    }
    notes_json = json.dumps(notes, ensure_ascii=False, indent=2)
    tpl = re.sub(r'var NOTES\s*=\s*\{[\s\S]*?\};', f'var NOTES = {notes_json};', tpl)

    # In-Deck Simulator & Timer scripts
    demo_js = """
// ============================================================
// IN-DECK INTERACTIVE SIMULATOR (Slide 8: Agent Memory)
// ============================================================
var deckMemories = [
  { id: 1, text: "Foydalanuvchi Rust va Python dasturchisi", cat: "preference", score: 0.89 },
  { id: 2, text: "PostgreSQL porti 5432 ga sozlangan", cat: "episodic", score: 0.42 },
  { id: 3, text: "API kalit .env faylida saqlanishi shart", cat: "security", score: 0.65 }
];

function renderDeckMemoryList() {
  var box = document.getElementById("deckMemList");
  var cEl = document.getElementById("deckMemCount");
  if (cEl) cEl.textContent = deckMemories.length + " ta Xotira Yozuvi";
  if (!box) return;
  box.innerHTML = "";
  deckMemories.forEach(function(m) {
    var div = document.createElement("div");
    div.style.color = "#94a3b8";
    div.textContent = "[" + m.id + "] " + m.cat + ': "' + m.text + '"';
    box.appendChild(div);
  });
}

function queryDeckMemory() {
  var inp = document.getElementById("deckMemQuery");
  var q = inp ? inp.value.trim().toLowerCase() : "";
  if (!q) return;

  var topMatch = deckMemories[0];
  if (q.indexOf("port") >= 0 || q.indexOf("baza") >= 0 || q.indexOf("sql") >= 0) {
    topMatch = deckMemories[1];
    topMatch.score = 0.94;
  } else if (q.indexOf("kalit") >= 0 || q.indexOf("xavfsiz") >= 0 || q.indexOf("env") >= 0) {
    topMatch = deckMemories[2];
    topMatch.score = 0.96;
  } else {
    topMatch = deckMemories[0];
    topMatch.score = 0.89;
  }

  var sEl = document.getElementById("deckScore");
  var tEl = document.getElementById("deckRetrievedText");
  var pEl = document.getElementById("deckPromptSnippet");

  if (sEl) sEl.textContent = topMatch.score + " (Top-1 Relevance)";
  if (tEl) tEl.textContent = '"' + topMatch.text + '"';
  if (pEl) pEl.textContent = "System: Context injected -> " + topMatch.text;
}

function addSampleMemory() {
  var id = deckMemories.length + 1;
  deckMemories.push({
    id: id,
    text: "Foydalanuvchi Toshkent vaqti bilan ishlaydi (UTC+5)",
    cat: "timezone",
    score: 0.78
  });
  renderDeckMemoryList();
}

function compactDeckMemory() {
  deckMemories = [
    { id: 1, text: "Xulosa: Foydalanuvchi Ali (Rust/Python, UTC+5, PostgreSQL 5432, .env himoyasi)", cat: "summary_buffer", score: 0.98 }
  ];
  renderDeckMemoryList();
  var pEl = document.getElementById("deckPromptSnippet");
  if (pEl) pEl.textContent = "System: Compacted Memory Buffer active (Tokens reduced by 75%)";
}

// 25-Min Arena Timer
var deckTimerSec = 25 * 60;
var deckTimerInterval = null;

function toggleDeckTimer() {
  var btn = document.getElementById("deckTimerBtn");
  if (deckTimerInterval) {
    clearInterval(deckTimerInterval);
    deckTimerInterval = null;
    if (btn) btn.textContent = "▶ Davom etish";
  } else {
    deckTimerInterval = setInterval(function() {
      if (deckTimerSec > 0) {
        deckTimerSec--;
        var m = Math.floor(deckTimerSec / 60);
        var s = deckTimerSec % 60;
        var disp = document.getElementById("deckTimerDisplay");
        if (disp) disp.textContent = (m < 10 ? "0" + m : m) + ":" + (s < 10 ? "0" + s : s);
      } else {
        clearInterval(deckTimerInterval);
        deckTimerInterval = null;
        alert("⏰ 25-Minutlik Kiber-Arena vaqti yakunlandi! Kodni peer-review qilishga o'ting.");
      }
    }, 1000);
    if (btn) btn.textContent = "⏸ Pauza";
  }
}

function resetDeckTimer() {
  if (deckTimerInterval) {
    clearInterval(deckTimerInterval);
    deckTimerInterval = null;
  }
  deckTimerSec = 25 * 60;
  var disp = document.getElementById("deckTimerDisplay");
  if (disp) disp.textContent = "25:00";
  var btn = document.getElementById("deckTimerBtn");
  if (btn) btn.textContent = "▶ Boshlash (25m)";
}

function checkDeckQuiz(btn, isCorrect) {
  var parent = btn.parentElement;
  var btns = parent.querySelectorAll("button");
  btns.forEach(function(b) {
    b.disabled = true;
    b.style.opacity = "0.7";
  });
  btn.style.opacity = "1";
  if (isCorrect) {
    btn.style.background = "var(--green)";
    btn.style.color = "#fff";
    btn.style.borderColor = "var(--green)";
  } else {
    btn.style.background = "var(--accent)";
    btn.style.color = "#fff";
    btn.style.borderColor = "var(--accent)";
  }
}
"""
    tpl = tpl.replace("</script>\n</body>", f"{demo_js}\n</script>\n</body>")

    with open(os.path.join(LESSON_DIR, "prezentatsiya.html"), "w", encoding="utf-8") as f:
        f.write(tpl)
    print("  ✓ Created: prezentatsiya.html")

    # ============================================================
    # 2. VARAQA.HTML (Printable A4 Worksheet)
    # ============================================================
    v_tpl = TPL_VAR
    v_tpl = v_tpl.replace("{{LESSON_NUM}}", "27")
    v_tpl = v_tpl.replace("{{TITLE_UZ}}", "Agent Xotirasi va Doimiy Kontekst: Epizodik, Semantik va Vector Cache")
    v_tpl = v_tpl.replace("{{TITLE_RU}}", "Память AI Агентов: Эпизодическая, Семантическая и Векторный Кэш")
    v_tpl = v_tpl.replace("{{TITLE_EN}}", "AI Agent Memory: Episodic, Semantic & Vector Cache")
    v_tpl = v_tpl.replace("{{SUBTITLE_UZ}}", "LLM amneziyasi, Lost in the Middle, 3 qatlamli kognitiv xotira, SQLite relyatsion saqlash va Cosine Similarity Top-K qidiruvi")
    v_tpl = v_tpl.replace("{{SUBTITLE_RU}}", "Амнезия LLM, Lost in the Middle, 3 уровня когнитивной памяти, SQLite и Top-K косинусный поиск")
    v_tpl = v_tpl.replace("{{SUBTITLE_EN}}", "LLM amnesia, Lost in the Middle, 3-tier cognitive memory, SQLite event store, and Cosine Similarity Top-K retrieval")

    v_tpl = v_tpl.replace("{{SEC1_TITLE_UZ}}", "1-Qism: Kognitiv Xotira Qatlamlari Taqqoslash Matritsasi")
    v_tpl = v_tpl.replace("{{SEC1_TITLE_RU}}", "Часть 1: Сравнительная Матрица Уровней Когнитивной Памяти")
    v_tpl = v_tpl.replace("{{SEC1_TITLE_EN}}", "Part 1: Cognitive Memory Tiers Comparison Matrix")
    v_sec1 = """    <p data-ru="Заполните различия между тремя ключевыми уровнями памяти автономного агента:" data-en="Analyze the structural characteristics across the 3 cognitive memory tiers:">Avtonom agentning 3 ta asosiy xotira qatlami o'rtasidagi farqlarni tahlil qiling va jadvalni to'ldiring:</p>
    <div class="box" style="margin-top:6px;">
      <table style="width:100%; border-collapse:collapse; font-size:8.5pt;">
        <thead>
          <tr style="border-bottom:1px solid var(--rule); text-align:left;">
            <th style="padding:4px 6px;" data-ru="Уровень Памяти" data-en="Memory Tier">Xotira Qatlami</th>
            <th style="padding:4px 6px;" data-ru="Носитель / База" data-en="Storage Backend">Saqlash Muhiti</th>
            <th style="padding:4px 6px;" data-ru="Механизм Поиска" data-en="Retrieval Logic">Qidiruv Mexanizmi</th>
            <th style="padding:4px 6px;" data-ru="Время Жизни (TTL)" data-en="Lifetime (TTL)">Yashash Muddati</th>
          </tr>
        </thead>
        <tbody>
          <tr style="border-bottom:1px dashed var(--hair);">
            <td style="padding:4px 6px;" data-ru="Working (Оперативная)" data-en="Working Memory"><b>Working Memory (Scratchpad)</b></td>
            <td style="padding:4px 6px;" data-ru="Оперативная память (RAM / Prompt)" data-en="In-Memory RAM / Prompt">Joriy Prompt / RAM</td>
            <td style="padding:4px 6px;" data-ru="Прямой доступ в контекстном окне" data-en="Direct context window access">To'g'ridan-to'g'ri o'qish</td>
            <td style="padding:4px 6px;" data-ru="1 ReAct сессия" data-en="1 ReAct session">1 ta ReAct tsikli</td>
          </tr>
          <tr style="border-bottom:1px dashed var(--hair);">
            <td style="padding:4px 6px;" data-ru="Episodic (Эпизодическая)" data-en="Episodic Memory"><b>Episodic Memory (Voqealar)</b></td>
            <td style="padding:4px 6px;" data-ru="SQLite / PostgreSQL таблицы" data-en="SQLite / PostgreSQL tables">SQLite relyatsion bazasi</td>
            <td style="padding:4px 6px;" data-ru="SQL запросы (WHERE user_id = ?)" data-en="SQL queries (WHERE user_id = ?)">Aniq SQL so'rovlari</td>
            <td style="padding:4px 6px;" data-ru="Постоянно (Persistent)" data-en="Persistent">Doimiy (yillar davomida)</td>
          </tr>
          <tr>
            <td style="padding:4px 6px;" data-ru="Semantic (Семантическая)" data-en="Semantic Memory"><b>Semantic Memory (Ma'no)</b></td>
            <td style="padding:4px 6px;" data-ru="ChromaDB / Векторное хранилище" data-en="ChromaDB / Vector Store">ChromaDB / Faiss Vector DB</td>
            <td style="padding:4px 6px;" data-ru="Косинусное сходство (Cosine Top-K)" data-en="Cosine Similarity Top-K">Kosinus burchagi (Top-K)</td>
            <td style="padding:4px 6px;" data-ru="Постоянно с индексацией" data-en="Persistent with indexing">Doimiy indekslangan</td>
          </tr>
        </tbody>
      </table>
    </div>"""
    v_tpl = v_tpl.replace("{{SEC1_CONTENT}}", v_sec1)

    v_tpl = v_tpl.replace("{{SEC2_TITLE_UZ}}", "2-Qism: Kod Tahlili — Top-K Kosinus O'xshashlik Qidiruvi")
    v_tpl = v_tpl.replace("{{SEC2_TITLE_RU}}", "Часть 2: Анализ Кода — Top-K Косинусный Поиск Памяти")
    v_tpl = v_tpl.replace("{{SEC2_TITLE_EN}}", "Part 2: Code Analysis — Top-K Cosine Memory Retrieval")
    v_sec2 = """    <div class="code-snippet">// ⚠️ Kodni to'g'rilang: Kosinus o'xshashlik formulasini to'ldiring va past sifatli xotirani filtrlang:
function cosineSimilarity(vecA, vecB) {
  let dotProduct = 0, normA = 0, normB = 0;
  for (let i = 0; i &lt; vecA.length; i++) {
    dotProduct += vecA[i] * vecB[i];
    normA += vecA[i] ** 2;
    normB += vecB[i] ** 2;
  }
  // ❌ XATO: return dotProduct (normallashtirilmagan!)
  // ✅ TO'G'RI:
  return dotProduct / (____________________ * ____________________);
}

function retrieveTopK(queryVec, memoryList, k = 3, minScore = 0.75) {
  return memoryList
    .map(mem =&gt; ({ ...mem, score: cosineSimilarity(queryVec, mem.vector) }))
    .filter(mem =&gt; mem.score &gt;= ____________________)
    .sort((a, b) =&gt; b.score - a.score)
    .slice(0, k);
}</div>
    <p style="margin-top:4px;" data-ru="Запишите правильный знаменатель формулы косинуса и условие фильтра:" data-en="Fill in cosine denominator and minimum relevance threshold:">Bo'sh joylarga kosinus maxrajini (`Math.sqrt(...)`) va filtr chegarasini yozing:</p>
    <div class="write-line"></div>"""
    v_tpl = v_tpl.replace("{{SEC2_CONTENT}}", v_sec2)

    v_tpl = v_tpl.replace("{{SEC3_TITLE_UZ}}", "3-Qism: Amaliy Laboratoriya (ChromaDB Memory Audit)")
    v_tpl = v_tpl.replace("{{SEC3_TITLE_RU}}", "Часть 3: Практическая Лаборатория (Аудит Памяти в ChromaDB)")
    v_tpl = v_tpl.replace("{{SEC3_TITLE_EN}}", "Part 3: Hands-on Lab (ChromaDB Memory Audit Table)")
    v_sec3 = """    <p data-ru="Проверьте работу извлечения фактов в simulator/index.html и заполните таблицу:" data-en="Verify memory retrieval operations in simulator/index.html and complete audit table:"><b>simulator/index.html</b> da xotirani tekshirib, 4 xil savol bo'yicha kosinus natijalarini qayd eting:</p>
    <div class="box" style="margin-top:6px;">
      <table style="width:100%; border-collapse:collapse; font-size:8.5pt;">
        <thead>
          <tr style="border-bottom:1px solid var(--rule); text-align:left;">
            <th style="padding:4px 6px;">#</th>
            <th style="padding:4px 6px;" data-ru="Запрос Пользователя" data-en="User Query">Foydalanuvchi Savoli</th>
            <th style="padding:4px 6px;" data-ru="Найденный Факт" data-en="Retrieved Fact">Topilgan Xotira Fakti</th>
            <th style="padding:4px 6px;" data-ru="Cosine Score" data-en="Cosine Score">Kosinus Bali</th>
            <th style="padding:4px 6px;" data-ru="Статус Инъекции" data-en="Injection Status">Promptga Qo'shildimi</th>
          </tr>
        </thead>
        <tbody>
          <tr style="border-bottom:1px dashed var(--hair);">
            <td style="padding:4px 6px;">1</td>
            <td style="padding:4px 6px;" data-ru="«На каком языке писать код?»" data-en="Which language to code in?">"Qaysi tilda kod yozay?"</td>
            <td style="padding:4px 6px;" data-ru="Разработчик Rust и Python" data-en="Rust & Python developer">Foydalanuvchi Rust/Python dasturchisi</td>
            <td style="padding:4px 6px;"><code>0.89</code></td>
            <td style="padding:4px 6px;" data-ru="[ &nbsp; ] ДА (Injected)" data-en="[ &nbsp; ] YES (Injected)">[ &nbsp; ] HA (Injected)</td>
          </tr>
          <tr style="border-bottom:1px dashed var(--hair);">
            <td style="padding:4px 6px;">2</td>
            <td style="padding:4px 6px;" data-ru="«Какой был порт БД?»" data-en="What was database port?">"Baza porti nechi edi?"</td>
            <td style="padding:4px 6px;" data-ru="Порт PostgreSQL 5432" data-en="PostgreSQL port 5432">PostgreSQL porti 5432</td>
            <td style="padding:4px 6px;"><code>0.94</code></td>
            <td style="padding:4px 6px;" data-ru="[ &nbsp; ] ДА (Injected)" data-en="[ &nbsp; ] YES (Injected)">[ &nbsp; ] HA (Injected)</td>
          </tr>
          <tr style="border-bottom:1px dashed var(--hair);">
            <td style="padding:4px 6px;">3</td>
            <td style="padding:4px 6px;" data-ru="«Какая погода?»" data-en="What is the weather?">"Ob-havo qanday?"</td>
            <td style="padding:4px 6px;" data-ru="Посторонний шум / Нет совпадений" data-en="Irrelevant noise">(Mos xotira topilmadi)</td>
            <td style="padding:4px 6px;"><code>0.21</code></td>
            <td style="padding:4px 6px;" data-ru="[ &nbsp; ] НЕТ (Filtered)" data-en="[ &nbsp; ] NO (Filtered)">[ &nbsp; ] YO'Q (Filtered)</td>
          </tr>
          <tr>
            <td style="padding:4px 6px;">4</td>
            <td style="padding:4px 6px;" data-ru="«Куда сохранить пароль?»" data-en="Where to put password?">"Parolni qayerga qo'yaman?"</td>
            <td style="padding:4px 6px;" data-ru="Сохранять в файле .env" data-en="Store in .env file">API kalit .env faylida saqlansin</td>
            <td style="padding:4px 6px;"><code>0.96</code></td>
            <td style="padding:4px 6px;" data-ru="[ &nbsp; ] ДА (Injected)" data-en="[ &nbsp; ] YES (Injected)">[ &nbsp; ] HA (Injected)</td>
          </tr>
        </tbody>
      </table>
    </div>"""
    v_tpl = v_tpl.replace("{{SEC3_CONTENT}}", v_sec3)

    v_sec4 = """    <div class="box-grid" style="margin-top:6px;">
      <div class="box">
        <h4 data-ru="1-Уровень: База (4 балла)" data-en="Tier 1: Base (4 pts)">1-Daraja: Baza (4 ball)</h4>
        <p data-ru="Создать таблицу agent_memories в SQLite и написать функции add/query." data-en="Author agent_memories table in SQLite with add/query operations.">SQLite da agent_memories jadvalini yaratish va xotirani yozish/olish funksiyalarini yozish.</p>
        <div class="write-line"></div>
      </div>
      <div class="box">
        <h4 data-ru="2-Уровень: Проект (4 балла)" data-en="Tier 2: Engineering (4 pts)">2-Daraja: Amaliyot (4 ball)</h4>
        <p data-ru="Реализовать cosineSimilarity и Top-K семантический фильтр с порогом 0.75." data-en="Implement cosineSimilarity and Top-K retrieval router at 0.75 threshold.">Kosinus o'xshashlik hisoblagichi va Top-K xotira ajratuvchi algoritmni qurish.</p>
        <div class="write-line"></div>
      </div>
    </div>
    <div class="box" style="margin-top:6px;">
      <h4 data-ru="3-Уровень: Кибер-Вызов (2 балла)" data-en="Tier 3: Cyber Challenge (2 pts)">3-Daraja: Kiber-Chaqiruv (2 ball)</h4>
      <p data-ru="Создать Summarization Buffer, сжимающий N сообщений в 1 структурированное резюме." data-en="Engineer Summarization Buffer compacting N conversation turns into dense summary.">Xabarlar soni N tadan oshganda suhbatni 1 ta ixcham xulosaga siquvchi mexanizm yaratish.</p>
      <div class="write-line"></div>
    </div>"""
    v_tpl = v_tpl.replace("{{SEC4_CONTENT}}", v_sec4)

    with open(os.path.join(LESSON_DIR, "varaqa.html"), "w", encoding="utf-8") as f:
        f.write(v_tpl)
    print("  ✓ Created: varaqa.html")

    # ============================================================
    # 3. VAZIFA.HTML (Interactive Homework App)
    # ============================================================
    vz_tpl = TPL_VAZ
    vz_tpl = vz_tpl.replace("{{TITLE_UZ}}", "27-dars: Agent Xotirasi va Doimiy Kontekst: Epizodik, Semantik va Vector Cache")
    vz_tpl = vz_tpl.replace("{{TITLE_RU}}", "Урок 27: Память AI Агентов: Эпизодическая, Семантическая и Векторный Кэш")
    vz_tpl = vz_tpl.replace("{{TITLE_EN}}", "Lesson 27: AI Agent Memory: Episodic, Semantic & Vector Cache")
    vz_tpl = vz_tpl.replace("{{LESSON_SLUG}}", "10-11-w11-l27-agent-memory")
    vz_tpl = vz_tpl.replace("{{COHORT_LABEL_UZ}}", "10–11-SINF · 11-HAFTA")
    vz_tpl = vz_tpl.replace("{{HERO_TAG_UZ}}", "SENIOR AI & KOGNITIV XOTIRA ARXITEKTURASI")
    vz_tpl = vz_tpl.replace("{{HERO_DESC_UZ}}", "LLM amneziyasi, Lost in the Middle, 3 qatlamli kognitiv xotira, SQLite epizodik saqlash va Cosine Similarity Top-K qidiruvi bo'yicha 3 darajali topshiriqlarni bajaring.")
    vz_tpl = vz_tpl.replace("{{HERO_DESC_RU}}", "Выполните 3 уровня задач по преодолению амнезии LLM, феномену Lost in the Middle, SQLite памяти и Top-K семантическому извлечению.")
    vz_tpl = vz_tpl.replace("{{HERO_DESC_EN}}", "Complete 3 challenge tiers overcoming LLM amnesia, conquering Lost in the Middle, designing SQLite episodic stores, and Top-K cosine similarity retrieval.")

    vz_tpl = vz_tpl.replace("{{RUBRIC_T1_UZ}}", "Epizodik SQLite xotira boshqaruvi (4 ball)")
    vz_tpl = vz_tpl.replace("{{RUBRIC_T1_RU}}", "Эпизодическое хранилище памяти в SQLite (4 балла)")
    vz_tpl = vz_tpl.replace("{{RUBRIC_T1_EN}}", "Episodic SQLite memory store implementation (4 pts)")

    vz_tpl = vz_tpl.replace("{{RUBRIC_T2_UZ}}", "Top-K kosinus o'xshashlik qidiruvi (4 ball)")
    vz_tpl = vz_tpl.replace("{{RUBRIC_T2_RU}}", "Top-K семантический поиск по косинусной близости (4 балла)")
    vz_tpl = vz_tpl.replace("{{RUBRIC_T2_EN}}", "Top-K cosine similarity vector retrieval (4 pts)")

    vz_tpl = vz_tpl.replace("{{RUBRIC_T3_UZ}}", "Summarization Buffer va xotirani siqish (2 ball)")
    vz_tpl = vz_tpl.replace("{{RUBRIC_T3_RU}}", "Summarization Buffer и сжатие контекста (2 балла)")
    vz_tpl = vz_tpl.replace("{{RUBRIC_T3_EN}}", "Summarization Buffer context compaction engine (2 pts)")

    tasks_10 = """  <!-- TASK 1 -->
  <article class="task-card">
    <div class="task-head">
      <span class="task-badge" data-ru="1-Уровень: База" data-en="Tier 1: Base">1-Bosqich: Baza</span>
      <span class="task-score">4 BALL</span>
    </div>
    <h3 data-ru="Эпизодический SQLite Хранилище Памяти" data-en="Episodic SQLite Memory Store">Epizodik SQLite Xotira Klientini Yozish</h3>
    <p data-ru="Напишите класс EpisodicMemoryStore со схемой agent_memories, методом add(userId, category, content, importance) и методом queryUserPreferences(userId), возвращающим до 5 фактов:" data-en="Author class EpisodicMemoryStore managing agent_memories table with add(userId, category, content, importance) and queryUserPreferences(userId) returning up to 5 highest importance preferences:"><code>agent_memories</code> jadvaliga fakt qo'shuvchi <code>add()</code> va berilgan foydalanuvchining eng muhim 5 ta preferensiyasini qaytaruvchi <code>queryUserPreferences()</code> metodlariga ega klass yozing:</p>
    <div class="code-box">// Kutilayotgan klass:
class EpisodicMemoryStore {
  // 1. init: CREATE TABLE IF NOT EXISTS agent_memories
  // 2. add(userId, category, content, importance)
  // 3. queryUserPreferences(userId) -> SELECT WHERE category='preference' ORDER BY importance DESC LIMIT 5
}</div>
    <textarea class="answer-area" id="ans_task_1" rows="7" placeholder="JavaScript / SQL kodingizni bu yerga yozing..." data-placeholder-ru="Напишите ваш код здесь..." data-placeholder-en="Write your code here..." oninput="saveAnswers()"></textarea>
    <div style="margin-top:12px;">
      <button class="btn btn-outline teacher-solution-only" onclick="toggleSolution('sol_1')" data-ru="🔒 Эталон Решения (Учитель)" data-en="🔒 Solution (Teacher)">🔒 Etalon Yechim (O'qituvchi)</button>
      <div class="solution-box teacher-solution-only" id="sol_1" hidden>
        <h4 data-ru="✅ Эталонный Episodic Memory Класс" data-en="✅ Reference Episodic Memory Class">✅ Etalon Yechim</h4>
        <pre><code>export class EpisodicMemoryStore {
  constructor(dbClient) {
    this.db = dbClient;
  }
  async add(userId, category, content, importance = 1.0) {
    const query = `
      INSERT INTO agent_memories (user_id, category, content, importance)
      VALUES (?, ?, ?, ?)
    `;
    return await this.db.run(query, [userId, category, content, importance]);
  }
  async queryUserPreferences(userId, limit = 5) {
    const query = `
      SELECT content, importance FROM agent_memories
      WHERE user_id = ? AND category = 'preference'
      ORDER BY importance DESC
      LIMIT ?
    `;
    return await this.db.all(query, [userId, limit]);
  }
}</code></pre>
      </div>
    </div>
  </article>

  <!-- TASK 2 -->
  <article class="task-card">
    <div class="task-head">
      <span class="task-badge" data-ru="2-Уровень: Проект" data-en="Tier 2: Engineering">2-Bosqich: Muhandislik</span>
      <span class="task-score">4 BALL</span>
    </div>
    <h3 data-ru="Top-K Семантический Поиск по Косинусной Близости" data-en="Top-K Cosine Similarity Retrieval Engine">Top-K Kosinus O'xshashlik Qidiruv Dvigateli</h3>
    <p data-ru="Реализуйте функцию cosineSimilarity(vecA, vecB) и функцию retrieveTopK(queryVec, memoryCollection, k, minThreshold), которая фильтрует факты ниже minThreshold (0.75) и сортирует по убыванию:" data-en="Implement cosineSimilarity(vecA, vecB) and retrieveTopK(queryVec, memoryCollection, k, minThreshold) pruning memories below threshold (0.75) and sorting descending:">Ikkita vektor orasidagi kosinus burchagini hisoblovchi va <code>minThreshold</code> (0.75) dan yuqori bo'lgan eng yaqin K ta xotirani saralab qaytaruvchi funksiyalarni yozing:</p>
    <div class="code-box">function cosineSimilarity(a, b) {
  // cos(theta) = (a . b) / (||a|| * ||b||)
}
function retrieveTopK(queryVec, memories, k = 3, threshold = 0.75) {
  // score calculation, threshold filtering, sort desc, limit k
}</div>
    <textarea class="answer-area" id="ans_task_2" rows="8" placeholder="Vektor matematikasi va Top-K kodini bu yerga yozing..." data-placeholder-ru="Напишите код здесь..." data-placeholder-en="Write code here..." oninput="saveAnswers()"></textarea>
    <div style="margin-top:12px;">
      <button class="btn btn-outline teacher-solution-only" onclick="toggleSolution('sol_2')" data-ru="🔒 Эталон Решения (Учитель)" data-en="🔒 Solution (Teacher)">🔒 Etalon Yechim (O'qituvchi)</button>
      <div class="solution-box teacher-solution-only" id="sol_2" hidden>
        <h4 data-ru="✅ Эталонная Векторная Математика" data-en="✅ Reference Vector Retrieval">✅ Etalon Yechim</h4>
        <pre><code>export function cosineSimilarity(vecA, vecB) {
  let dot = 0, normA = 0, normB = 0;
  for (let i = 0; i &lt; vecA.length; i++) {
    dot += vecA[i] * vecB[i];
    normA += vecA[i] ** 2;
    normB += vecB[i] ** 2;
  }
  const denom = Math.sqrt(normA) * Math.sqrt(normB);
  return denom === 0 ? 0 : dot / denom;
}

export function retrieveTopK(queryVec, memories, k = 3, minScore = 0.75) {
  return memories
    .map(mem =&gt; ({ ...mem, score: cosineSimilarity(queryVec, mem.vector) }))
    .filter(mem =&gt; mem.score &gt;= minScore)
    .sort((a, b) =&gt; b.score - a.score)
    .slice(0, k);
}</code></pre>
      </div>
    </div>
  </article>

  <!-- TASK 3 -->
  <article class="task-card">
    <div class="task-head">
      <span class="task-badge" data-ru="3-Уровень: Вызов" data-en="Tier 3: Challenge">3-Bosqich: Kiber-Sinov</span>
      <span class="task-score">2 BALL</span>
    </div>
    <h3 data-ru="Summarization Buffer (Сжатие Истории Диалога)" data-en="Summarization Buffer (Conversation Compactor)">Summarization Buffer va Avto-Siqish Mexanizmi</h3>
    <p data-ru="Создайте класс ConversationBuffer(maxTurns, summarizerLLM). Когда длина истории превышает maxTurns, класс сжимает старые сообщения через summarizerLLM и оставляет краткое резюме + последние 2 реплики:" data-en="Create class ConversationBuffer(maxTurns, summarizerLLM). When dialogue exceeds maxTurns, compact older messages via summarizerLLM, retaining dense executive summary + latest 2 turns:">Xabarlar <code>maxTurns</code> (masalan, 6) dan oshganda, eski xabarlarni LLM orqali ixcham xulosaga aylantirib, faqat xulosa va oxirgi 2 ta xabarni saqlovchi <code>ConversationBuffer</code> klassini yozing:</p>
    <div class="code-box">class ConversationBuffer {
  constructor(maxTurns = 6, summarizerFn) { ... }
  async addTurn(role, content) {
    // If turns > maxTurns -> summarize oldest turns, prepend summary
  }
}</div>
    <textarea class="answer-area" id="ans_task_3" rows="8" placeholder="ConversationBuffer kodini bu yerga yozing..." data-placeholder-ru="Напишите код здесь..." data-placeholder-en="Write code here..." oninput="saveAnswers()"></textarea>
    <div style="margin-top:12px;">
      <button class="btn btn-outline teacher-solution-only" onclick="toggleSolution('sol_3')" data-ru="🔒 Эталон Решения (Учитель)" data-en="🔒 Solution (Teacher)">🔒 Etalon Yechim (O'qituvchi)</button>
      <div class="solution-box teacher-solution-only" id="sol_3" hidden>
        <h4 data-ru="✅ Эталонный Summarization Buffer" data-en="✅ Reference Summarization Buffer">✅ Etalon Yechim</h4>
        <pre><code>export class ConversationBuffer {
  constructor(maxTurns = 6, summarizerFn) {
    this.maxTurns = maxTurns;
    this.summarizer = summarizerFn;
    this.summary = "";
    this.activeTurns = [];
  }
  async addTurn(role, content) {
    this.activeTurns.push({ role, content });
    if (this.activeTurns.length &gt; this.maxTurns) {
      const toCompress = this.activeTurns.slice(0, this.activeTurns.length - 2);
      this.activeTurns = this.activeTurns.slice(this.activeTurns.length - 2);
      
      const newSummary = await this.summarizer(this.summary, toCompress);
      this.summary = newSummary;
    }
  }
  getPromptContext() {
    return {
      summary: this.summary,
      recentMessages: this.activeTurns
    };
  }
}</code></pre>
      </div>
    </div>
  </article>"""
    vz_tpl = vz_tpl.replace("{{TASKS_LIST}}", tasks_10)

    with open(os.path.join(LESSON_DIR, "vazifa.html"), "w", encoding="utf-8") as f:
        f.write(vz_tpl)
    print("  ✓ Created: vazifa.html")

    # ============================================================
    # 4. TEACHER_READING.MD (Guide & Rubric)
    # ============================================================
    tr_md = f"""# 10–11-sinf: 27-dars — Agent Xotirasi va Doimiy Kontekst: Epizodik, Semantik va Vector Cache
**Target International School · Yunusobod Filiali**
**O'qituvchi:** Ismoiljon Usmonov · **Format:** 80 Daqiqa (Double Block / Juftlik dars)

---

## 🎯 Dars Maqsadi va Asosiy Mohiyati
Ushbu 80 daqiqalik darsda 10–11-sinf o'quvchilari LLM larning eng katta muammosi bo'lgan amneziya (xotirasizlik) va "Lost in the Middle" sindromini hal qiladilar.

O'quvchilar inson miyasiga o'xshash 3 qatlamli kognitiv xotira modelini o'rganadilar:
1. **Working Memory (Scratchpad in RAM):** Joriy ReAct qadami va qisqa muddatli kontekst.
2. **Episodic Memory (SQLite Event Log):** Foydalanuvchi afzalliklari va vositalar xatolari tarixi.
3. **Semantic Memory (ChromaDB / Vector Store):** 1536 o'lchamli vektorlar va Kosinus o'xshashlik Top-K saralash.

---

## ⏱️ 80 Daqiqalik Vaqt Taqsimoti (2 Bosqichli Reja)

### 1-Bosqich: Nazariya, Protokol va Jonli Simulyator (40 Daqiqa)
* **00:00 – 04:00 (4 min) | Kirish & Missiya:** Dars mavzusi va 10 ballik mezonni e'lon qilish.
* **04:00 – 10:00 (6 min) | 26-Dars Tahlili (HW Review):** Tool calling cheklovlari va doimiy xotira zaruriyati. 30 soniyalik blits savol.
* **10:00 – 16:00 (6 min) | Real Muammo:** LLM amneziyasi, 100K token isrofi va "Lost in the Middle" U-simon e'tibor pasayishi.
* **16:00 – 22:00 (6 min) | 3 Qatlamli Kognitiv Arxitektura:** Working, Episodic va Semantic qatlamlari.
* **22:00 – 28:00 (6 min) | Epizodik SQLite Xotirasi:** agent_memories jadvali va preferensiyalarni indekslash.
* **28:00 – 35:00 (7 min) | Semantik Vektor Qidiruv:** Kosinus o'xshashlik matematikasi va Top-K filtri.
* **35:00 – 40:00 (5 min) | Xotira Siqish (Compaction):** Summarization Buffer va Park et al. (2023) ahamiyat formulasi.

### 2-Bosqich: Jonli Tajriba, Kiber-Arena va Demos (40 Daqiqa)
* **40:00 – 48:00 (8 min) | Jonli Slayd Simulyatori:** Smartboardda xotiradan faktlarni izlash va Top-1 o'xshashlikni tekshirish.
* **48:00 – 54:00 (6 min) | Interaktiv Kiber-Quiz:** 3 ta savol bo'yicha blits o'tkazish.
* **54:00 – 69:00 (15 min) | Kiber-Arena (Amaliyot):** O'quvchilar `simulator/index.html` da xotira dvigatelini yozadilar.
* **69:00 – 74:00 (5 min) | Juftlikda Peer-Review:** 4 ta mezon bo'yicha xotira izolyatsiyasi va kosinus filtri auditi.
* **74:00 – 77:00 (3 min) | O'quvchilar Demosi:** 2 ta juftlik doskaga chiqib o'zlarining xotira dvigatelini namoyish etadi.
* **77:00 – 80:00 (3 min) | Xulosa & Uy Vazifasi:** 10 ballik `vazifa.html` ilovasini tushuntirish va Avtonom Kod Yozuvchi Agentlar mavzusini anons qilish.

---

## 🏆 10 Ballik Rasmiy Baholash Mezoni
1. **1-Daraja: Baza (4 ball):** SQLite da agent_memories jadvalini yaratish va preferensiyalarni olish.
2. **2-Daraja: Amaliyot (4 ball):** cosineSimilarity formulasini yozish va 0.75 dan yuqori Top-K xotirani ajratish.
3. **3-Daraja: Kiber-Sinov (2 ball):** Summarization Buffer orqali ko'p xabarlarni ixcham xulosaga siqish.
"""
    with open(os.path.join(LESSON_DIR, "TEACHER_READING.md"), "w", encoding="utf-8") as f:
        f.write(tr_md)
    print("  ✓ Created: TEACHER_READING.md")

    # ============================================================
    # 5. SIMULATOR/INDEX.HTML (Target Agent Memory Studio)
    # ============================================================
    sim_html = """<!DOCTYPE html>
<html lang="uz" data-theme="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title data-ru="Target Agent Memory Studio — Эпизодическая и Векторная Память" data-en="Target Agent Memory Studio — Episodic & Vector Store">Target Agent Memory Studio — Epizodik va Vektor Xotira</title>
  <style>
    :root {
      --bg: #090d16;
      --panel: #0f172a;
      --panel-2: #1e293b;
      --ink: #f8fafc;
      --ink-2: #94a3b8;
      --accent: #e11d48;
      --green: #10b981;
      --blue: #38bdf8;
      --amber: #f59e0b;
      --rule: #334155;
    }
    :root[data-theme="light"] {
      --bg: #f8fafc;
      --panel: #ffffff;
      --panel-2: #f1f5f9;
      --ink: #0f172a;
      --ink-2: #64748b;
      --accent: #e11d48;
      --green: #059669;
      --blue: #0284c7;
      --amber: #d97706;
      --rule: #e2e8f0;
    }
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      background: var(--bg);
      color: var(--ink);
      min-height: 100vh;
      display: flex;
      flex-direction: column;
    }
    header {
      background: var(--panel);
      border-bottom: 1px solid var(--rule);
      padding: 12px 24px;
      display: flex;
      align-items: center;
      justify-content: space-between;
    }
    .brand {
      display: flex;
      align-items: center;
      gap: 12px;
      font-weight: 800;
      font-size: 14px;
    }
    .tag {
      background: var(--accent);
      color: #fff;
      font-size: 10px;
      padding: 2px 8px;
      border-radius: 4px;
      letter-spacing: 0.05em;
    }
    .header-actions {
      display: flex;
      align-items: center;
      gap: 8px;
    }
    .btn {
      font-family: inherit;
      font-size: 12px;
      font-weight: 600;
      padding: 6px 12px;
      border-radius: 6px;
      border: 1px solid var(--rule);
      background: var(--panel-2);
      color: var(--ink);
      cursor: pointer;
      transition: all 0.15s;
    }
    .btn:hover { border-color: var(--accent); }
    .lang-btn.active {
      background: var(--accent);
      color: #fff;
      border-color: var(--accent);
    }
    main {
      flex: 1;
      display: grid;
      grid-template-columns: 320px 1fr 340px;
      gap: 1px;
      background: var(--rule);
    }
    @media (max-width: 960px) {
      main { grid-template-columns: 1fr; }
    }
    .sidebar-left, .workbench, .sidebar-right {
      background: var(--bg);
      padding: 16px;
      display: flex;
      flex-direction: column;
      gap: 14px;
    }
    h2 {
      font-size: 12px;
      text-transform: uppercase;
      letter-spacing: 0.06em;
      color: var(--ink-2);
      display: flex;
      justify-content: space-between;
      align-items: center;
    }
    .form-group {
      display: flex;
      flex-direction: column;
      gap: 6px;
    }
    label {
      font-size: 12px;
      font-weight: 600;
      color: var(--ink-2);
    }
    input, select, textarea {
      background: var(--panel);
      border: 1px solid var(--rule);
      border-radius: 6px;
      padding: 8px 12px;
      color: var(--ink);
      font-family: inherit;
      font-size: 12.5px;
    }
    input:focus, select:focus, textarea:focus {
      outline: none;
      border-color: var(--accent);
    }
    .memory-table-wrap {
      flex: 1;
      background: var(--panel);
      border: 1px solid var(--rule);
      border-radius: 8px;
      overflow-y: auto;
      max-height: 480px;
    }
    table {
      width: 100%;
      border-collapse: collapse;
      font-size: 11.5px;
    }
    th, td {
      padding: 8px 10px;
      border-bottom: 1px solid var(--rule);
      text-align: left;
    }
    th {
      background: var(--panel-2);
      color: var(--ink-2);
      font-weight: 700;
      position: sticky;
      top: 0;
    }
    .telemetry {
      background: var(--panel);
      border: 1px solid var(--rule);
      border-radius: 8px;
      padding: 12px;
      display: flex;
      flex-direction: column;
      gap: 6px;
      font-size: 12px;
      font-family: "JetBrains Mono", monospace;
    }
    .terminal-box {
      flex: 1;
      font-family: "JetBrains Mono", monospace;
      font-size: 11px;
      background: #030712;
      border: 1px solid var(--rule);
      border-radius: 8px;
      padding: 12px;
      overflow-y: auto;
      color: #94a3b8;
      display: flex;
      flex-direction: column;
      gap: 6px;
      max-height: 280px;
    }
    .badge {
      font-size: 10px;
      padding: 2px 6px;
      border-radius: 4px;
      font-weight: 700;
      display: inline-block;
    }
    .badge-pref { background: rgba(56,189,248,0.2); color: #38bdf8; }
    .badge-fact { background: rgba(16,185,129,0.2); color: #34d399; }
    .badge-sec { background: rgba(225,29,72,0.2); color: #f43f5e; }
  </style>
</head>
<body>

<header>
  <div class="brand">
    <span class="tag">TARGET VIBECODING</span>
    <span data-ru="Target Agent Memory Studio — Эпизодическая и Векторная Память" data-en="Target Agent Memory Studio — Episodic & Vector Store">Target Agent Memory Studio — Epizodik va Vektor Xotira</span>
  </div>
  <div class="header-actions">
    <button class="btn" onclick="toggleTheme()" aria-label="Theme">🌓</button>
    <div style="display:flex; gap:4px;">
      <button class="btn lang-btn active" data-lang="uz" onclick="setAppLang('uz')">UZ</button>
      <button class="btn lang-btn" data-lang="ru" onclick="setAppLang('ru')">RU</button>
      <button class="btn lang-btn" data-lang="en" onclick="setAppLang('en')">EN</button>
    </div>
  </div>
</header>

<main>
  <!-- Sidebar Left: Insert Memory -->
  <div class="sidebar-left">
    <h2 data-ru="Добавить Память (Insert)" data-en="Add Memory Record">Xotiraga Yozish</h2>

    <div class="form-group">
      <label data-ru="Пользователь (User ID):" data-en="User ID:">Foydalanuvchi ID:</label>
      <input type="text" id="memUser" value="user_ali" />
    </div>

    <div class="form-group">
      <label data-ru="Категория Памяти:" data-en="Category:">Kategoriya:</label>
      <select id="memCat">
        <option value="preference">preference (Afzallik)</option>
        <option value="fact">fact (Haqiqat / Fakt)</option>
        <option value="security">security (Kiberxavfsizlik)</option>
      </select>
    </div>

    <div class="form-group">
      <label data-ru="Важность (1.0 - 5.0):" data-en="Importance (1.0 - 5.0):">Ahamiyat Darajasi:</label>
      <input type="number" id="memImp" min="1" max="5" step="0.5" value="4.5" />
    </div>

    <div class="form-group">
      <label data-ru="Содержимое Факта:" data-en="Memory Content:">Xotira Matni:</label>
      <textarea id="memContent" rows="3" placeholder="Masalan: Foydalanuvchi faqat Rust tilida kod yozadi..." data-placeholder-ru="Например: Пользователь пишет код только на Rust..." data-placeholder-en="E.g.: User writes code only in Rust..."></textarea>
    </div>

    <button class="btn" onclick="insertNewMemory()" style="background:var(--accent); color:#fff; border-color:var(--accent);" data-ru="💾 Записать в SQLite" data-en="💾 Commit to SQLite">💾 SQLite-ga Yozish</button>

    <div style="margin-top:auto; font-size:11px; color:var(--ink-2); line-height:1.5;" data-ru="💡 Эпизодическая память хранится постоянно. Агент проверяет категорию preference перед генерацией кода." data-en="💡 Episodic store persists across sessions. Agent inspects preference category before code generation.">
      💡 Epizodik xotira yillab saqlanadi. Agent kod yozishdan oldin <code>preference</code> toifasini SQL orqali tekshiradi.
    </div>
  </div>

  <!-- Center: Memory Table & Search -->
  <div class="workbench">
    <div style="display:flex; justify-content:space-between; align-items:center;">
      <h2 data-ru="База Эпизодической Памяти (agent_memories)" data-en="Episodic Memory Store (agent_memories)">agent_memories Relyatsion Jadvali</h2>
      <button class="btn" onclick="compactBuffer()" data-ru="📦 Сжать Буфер (Summarize)" data-en="📦 Compact Buffer">📦 Xotirani Siqish (Summarize)</button>
    </div>

    <div class="memory-table-wrap">
      <table>
        <thead>
          <tr>
            <th>ID</th>
            <th data-ru="Пользователь" data-en="User">Foydalanuvchi</th>
            <th data-ru="Категория" data-en="Category">Kategoriya</th>
            <th data-ru="Содержимое" data-en="Content">Fakt Matni</th>
            <th data-ru="Важность" data-en="Importance">Ahamiyat</th>
          </tr>
        </thead>
        <tbody id="memoryTableBody">
          <!-- Filled by JS -->
        </tbody>
      </table>
    </div>

    <div style="display:flex; gap:8px;">
      <input type="text" id="queryInput" placeholder="Savol bering: 'Ali qaysi tilda kod yozadi?'..." style="flex:1;" data-placeholder-ru="Задайте вопрос: 'На каком языке пишет Али?'..." data-placeholder-en="Ask query: 'Which language does Ali code in?'..." onkeydown="if(event.key==='Enter') executeSemanticSearch()" />
      <button class="btn" onclick="executeSemanticSearch()" style="background:var(--blue); color:#000; border-color:var(--blue); font-weight:700;" data-ru="🔍 Top-K Поиск" data-en="🔍 Top-K Search">🔍 Top-K Qidirish</button>
    </div>
  </div>

  <!-- Sidebar Right: Telemetry & Injected Prompt -->
  <div class="sidebar-right">
    <h2>
      <span data-ru="Телеметрия Векторов" data-en="Vector Telemetry">Vektor Telemetriyasi</span>
      <button class="btn" onclick="clearLog()" data-ru="Очистить" data-en="Clear">Tozalash</button>
    </h2>

    <div class="telemetry">
      <div data-ru="Всего Памяти: " data-en="Total Records: ">Total Records: <span id="telTotal" style="color:var(--blue); font-weight:700;">3</span></div>
      <div data-ru="Порог Сходства: " data-en="Similarity Cutoff: ">Similarity Cutoff: <span style="color:var(--green); font-weight:700;">0.75</span></div>
      <div data-ru="Top-1 Релевантность: " data-en="Top-1 Relevance: ">Top-1 Relevance: <span id="telTopScore" style="color:var(--accent); font-weight:700;">0.89</span></div>
      <div data-ru="Экономия Токенов: " data-en="Token Efficiency: ">Token Efficiency: <span style="color:var(--green); font-weight:700;">+84%</span></div>
    </div>

    <h2 style="margin-top:4px;" data-ru="Сформированный Промпт (Injection)" data-en="Injected Prompt Preview">Promptga Qo'shilgan Xotira</h2>
    <div class="terminal-box" id="terminalBox">
      <div style="color:#64748b;">// Vektor qidiruv natijasida chiqarilgan xotira bu yerda ko'rinadi...</div>
    </div>
  </div>
</main>

<script>
var appLang = "uz";
var memories = [
  { id: 1, user: "user_ali", cat: "preference", content: "Foydalanuvchi faqat Rust va Python tilida kod yozadi", imp: 4.5, vec: [0.85, 0.45, 0.12] },
  { id: 2, user: "user_ali", cat: "fact", content: "PostgreSQL porti standart 5432 ga sozlangan", imp: 3.0, vec: [0.15, 0.92, 0.35] },
  { id: 3, user: "user_ali", cat: "security", content: "API kalitlarini faqat .env faylida saqlash shart", imp: 5.0, vec: [0.22, 0.31, 0.94] }
];

function renderTable() {
  var tbody = document.getElementById("memoryTableBody");
  var tTot = document.getElementById("telTotal");
  if (tTot) tTot.textContent = memories.length;
  if (!tbody) return;
  tbody.innerHTML = "";

  memories.forEach(function(m) {
    var tr = document.createElement("tr");
    var badgeClass = m.cat === "preference" ? "badge-pref" : (m.cat === "fact" ? "badge-fact" : "badge-sec");
    tr.innerHTML = `
      <td>${m.id}</td>
      <td><b>${escapeHtml(m.user)}</b></td>
      <td><span class="badge ${badgeClass}">${m.cat}</span></td>
      <td>${escapeHtml(m.content)}</td>
      <td>⭐ ${m.imp}</td>
    `;
    tbody.appendChild(tr);
  });
}

function insertNewMemory() {
  var u = document.getElementById("memUser").value.trim() || "user_ali";
  var c = document.getElementById("memCat").value;
  var i = parseFloat(document.getElementById("memImp").value) || 3.0;
  var t = document.getElementById("memContent").value.trim();
  if (!t) return;

  var id = memories.length + 1;
  memories.push({
    id: id,
    user: u,
    cat: c,
    content: t,
    imp: i,
    vec: [Math.random(), Math.random(), Math.random()]
  });
  renderTable();
  document.getElementById("memContent").value = "";
  logTerminal("💾 SQLite INSERT OK: [id=" + id + "] " + t);
}

function executeSemanticSearch() {
  var inp = document.getElementById("queryInput");
  var q = inp ? inp.value.trim().toLowerCase() : "";
  if (!q) return;

  var matched = memories[0];
  var score = 0.89;

  if (q.indexOf("port") >= 0 || q.indexOf("baza") >= 0 || q.indexOf("sql") >= 0) {
    matched = memories[1];
    score = 0.95;
  } else if (q.indexOf("kalit") >= 0 || q.indexOf("parol") >= 0 || q.indexOf("env") >= 0) {
    matched = memories[2];
    score = 0.97;
  } else if (q.indexOf("ob-havo") >= 0 || q.indexOf("film") >= 0) {
    score = 0.22;
  }

  var sEl = document.getElementById("telTopScore");
  if (sEl) sEl.textContent = score;

  var term = document.getElementById("terminalBox");
  if (!term) return;

  if (score >= 0.75) {
    term.innerHTML = `
      <div style="color:#34d399;">✓ Cosine Match Score: ${score} (Threshold &gt;= 0.75 PASS)</div>
      <div style="color:#38bdf8;">📥 Retrieved Memory: "${escapeHtml(matched.content)}"</div>
      <div style="color:#cbd5e1; margin-top:6px;">--- INJECTED SYSTEM CONTEXT ---</div>
      <div style="color:#f43f5e;">System: The following verified memory is known about user: ${escapeHtml(matched.content)}</div>
    `;
  } else {
    term.innerHTML = `
      <div style="color:#f59e0b;">⚠️ Cosine Match Score: ${score} (Below 0.75 Cutoff)</div>
      <div style="color:#64748b;">🚫 Irrelevant noise filtered. Zero tokens wasted in system prompt!</div>
    `;
  }
}

function compactBuffer() {
  memories = [
    { id: 1, user: "user_ali", cat: "preference", content: "Xulosa: Ali (Rust/Python dasturchisi, PostgreSQL port 5432, .env majburiy)", imp: 5.0, vec: [0.7, 0.7, 0.7] }
  ];
  renderTable();
  logTerminal("📦 Summarization Buffer: 3 ta xotira 1 ta zich xulosaga siqildi (-75% token tejash)");
}

function logTerminal(msg) {
  var term = document.getElementById("terminalBox");
  if (!term) return;
  var d = document.createElement("div");
  d.textContent = "[" + new Date().toLocaleTimeString() + "] " + msg;
  term.prepend(d);
}

function clearLog() {
  var term = document.getElementById("terminalBox");
  if (term) term.innerHTML = '<div style="color:#64748b;">// Log tozalandi</div>';
}

function setAppLang(l) {
  appLang = l;
  document.documentElement.lang = l;
  document.querySelectorAll(".lang-btn").forEach(function(b) {
    b.classList.toggle("active", b.getAttribute("data-lang") === l);
  });
  document.querySelectorAll("[data-" + l + "]").forEach(function(el) {
    if (el.children.length === 0 || el.tagName === "TITLE") {
      el.textContent = el.getAttribute("data-" + l);
    }
  });
  var inp = document.getElementById("queryInput");
  if (inp) {
    var ph = inp.getAttribute("data-placeholder-" + l);
    if (ph) inp.placeholder = ph;
  }
}

function toggleTheme() {
  var cur = document.documentElement.getAttribute("data-theme") || "dark";
  var next = (cur === "dark") ? "light" : "dark";
  document.documentElement.setAttribute("data-theme", next);
}

function escapeHtml(s) {
  return String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
}

window.addEventListener("DOMContentLoaded", function() {
  renderTable();
});
</script>
</body>
</html>
"""
    with open(os.path.join(SIM_DIR, "index.html"), "w", encoding="utf-8") as f:
        f.write(sim_html)
    print("  ✓ Created: simulator/index.html")

    print(f"🎉 10–11-sinf (27-dars) generation finished in {LESSON_DIR}!")

if __name__ == "__main__":
    build_10_11_lesson()
