#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
scripts/build_10_11_w11_l28.py — Builder for 10–11th Grade, Week 11, Lesson 28

Mavzu: Multi-Agent Tizimlari: Supervisor va Worker Naqshlari (LangGraph & Message Routing)
Format: Yakka Dars (40 daqiqa), 10 slayd
Kohorta: 10-11-sinf (Senior AI & Enterprise Kiberxavfsizlik Track)
"""

import os
import sys
import json
import re

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DEST_DIR = os.path.join(REPO_ROOT, "classes", "10-11-sinf", "11-hafta", "28-dars-multi-agent-tizimlari-supervisor-va-worker")

os.makedirs(DEST_DIR, exist_ok=True)
os.makedirs(os.path.join(DEST_DIR, "simulator"), exist_ok=True)

# -----------------------------------------------------------------------------
# 1. SLIDES HTML (10 Slides)
# -----------------------------------------------------------------------------
SLIDES_HTML = """
  <!-- SLIDE 1: TITUL -->
  <section class="slide current" data-phase="Kirish|Введение|Intro" data-time="00:00–04:00" data-slide-index="0">
    <div class="eyebrow"><span class="t" data-ru="10–11-КЛАСС · 11-Я НЕДЕЛЯ · УРОК 28" data-en="GRADES 10–11 · WEEK 11 · LESSON 28">10–11-SINF · 11-HAFTA · 28-DARS</span></div>
    <h1 class="display" data-ru="Мультиагентные Системы: Паттерны Supervisor и Worker в LangGraph" data-en="Multi-Agent Systems: Supervisor & Worker Patterns in LangGraph">Multi-Agent Tizimlari: Supervisor va Worker Naqshlari (LangGraph)</h1>
    <p class="lede" data-ru="Отказ от единого монолитного агента в пользу специализированных ролей: маршрутизация сообщений, граф состояний (StateGraph) и защита от взаимных блокировок (Deadlocks)." data-en="Moving beyond monolithic agents to specialized autonomous teams: message routing, StateGraph orchestration, and deadlock prevention.">Yagona monolit agentdan ixtisoslashgan jamoaga o'tish: xabarlarni marshrutlash, StateGraph holat grafigi va cheksiz sikllardan (deadlock) himoyalangan agentlar jamoasi.</p>
    <div class="hero-split">
      <div class="box">
        <div class="tag" data-ru="Формат урока" data-en="Lesson Format">40 daqiqalik Yakka Dars</div>
        <h3 data-ru="Паттерн Супервизора" data-en="Supervisor Pattern">Supervisor Arxitekturasi</h3>
        <p data-ru="Один координатор распределяет подзадачи между исследователем, программистом и тестировщиком." data-en="A central coordinator dispatches subtasks across researcher, coder, and reviewer agents.">Boshqaruvchi agent murakkab topshiriqni tadqiqotchi, dasturchi va tanqidchi agentlarga taqsimlaydi.</p>
      </div>
      <div class="box">
        <div class="tag" data-ru="Ожидаемый результат" data-en="Deliverable">Multi-Agent Router</div>
        <h3 data-ru="Оркестрация LangGraph" data-en="LangGraph StateGraph">Holat Grafigi</h3>
        <p data-ru="Каждый ученик запрограммирует логику маршрутизации StateGraph и условных ребер (conditional edges)." data-en="Each student writes StateGraph routing logic with conditional edges and agent state merging.">Har bir o'quvchi StateGraph grafigi va shartli marshrutlash (conditional edges) mantig'ini kodlaydi.</p>
      </div>
    </div>
  </section>

  <!-- SLIDE 2: MANDATORY HW REVIEW -->
  <section class="slide" data-phase="Uy Vazifasi Tahlili|Разбор ДЗ|Homework Review" data-time="04:00–08:00" data-slide-index="1">
    <div class="eyebrow"><span class="t" data-ru="АНАЛИЗ ДОМАШНЕГО ЗАДАНИЯ 27-УРОКА" data-en="LESSON 27 HOMEWORK REVIEW">27-DARS UY VAZIFASI TAHLILI</span></div>
    <h2 data-ru="Память Агентов: Ошибка Перегрузки Контекста Полным Дампом" data-en="Agent Memory: The Raw DB Dump Context Overflow Trap">Agent Xotirasi: Bazani To'liq Promptga Tiqish Xatosi</h2>
    <div class="grid-2">
      <div class="box danger-border">
        <div class="tag" style="background:rgba(239,68,68,0.15); color:var(--red);" data-ru="Типичная ошибка (Pitfall)" data-en="Common Pitfall">Keng Tarqalgan Xato (Pitfall)</div>
        <h3 data-ru="Заливка всех 500 фактов из SQLite прямо в системный промпт" data-en="Dumping all 500 SQLite facts into system prompt">Barcha 500 Ta Faktni To'g'ridan-to'g'ri Promptga Yuklash</h3>
        <p data-ru="Ученики сделали SELECT * FROM memories и отправили весь массив текста в LLM. Результат: контекстное окно мгновенно исчерпано, модель ловит «Lost in the Middle», а стоимость каждого вызова выросла в 20 раз!" data-en="Students ran SELECT * FROM memories and stuffed raw strings into LLM prompts. Result: immediate context exhaustion, 'Lost in the Middle' amnesia, and a 20x spike in API token bills!">O'quvchilar SELECT * FROM memories deb butun bazani bitta promptga tiqdilar. Natijada kontekst to'lib ketdi, model "Lost in the Middle" xatoligi bilan faktlarni chalkashtirib, xarajat 20 barobarga oshib ketdi!</p>
        <pre><code>// ❌ Xato: Kontekstni behuda to'ldirish
prompt = `Barcha xotiralar: ${db.getAllRows()}`; // 50,000 token!</code></pre>
      </div>
      <div class="box success-border">
        <div class="tag" style="background:rgba(16,185,129,0.15); color:var(--green);" data-ru="Золотой стандарт (Golden Solution)" data-en="Golden Standard">Oltin Standart (Golden Solution)</div>
        <h3 data-ru="Семантический поиск Top-K + Сжатый буфер фактов" data-en="Semantic Top-K + Compact Episodic Facts">Semantik Top-K Qidiruv + Qisqa Epizodik Faktlar</h3>
        <p data-ru="Векторный поиск извлекает только 3 самых релевантных факта (косинусное сходство &gt; 0.8). Контекст остается чистым, время ответа модели падает в 4 раза, а точность генерации возрастает до 98%." data-en="Vector search retrieves strictly top-3 relevant facts (cosine similarity &gt; 0.8). Context remains lean, response latency drops 4x, and reasoning accuracy hits 98%.">Vektor qidiruv faqat eng yaqin 3 ta faktni (kosinus o'xshashligi &gt; 0.8) ajratib oladi. Kontekst toza saqlanadi, model tezligi 4 barobar oshadi va aniqlik 98% ga yetadi.</p>
        <pre><code>// ✅ To'g'ri: Faqat eng dolzarb Top-3 faktni kiritish
const relevantFacts = vectorStore.search(userQuery, { topK: 3 });
prompt = `Mavzuga oid faktlar: ${relevantFacts.join('\\n')}`;</code></pre>
      </div>
    </div>
    <div class="bridge-card" style="margin-top:12px; padding:10px 16px; border-radius:10px; background:rgba(59,130,246,0.08); border-left:4px solid var(--accent); display:flex; justify-content:space-between; align-items:center;">
      <div>
        <strong style="color:var(--accent);" data-ru="Блиц-вопрос (30 сек):" data-en="Blitz Question (30s):">⚡ Blitz-Savol (30s):</strong>
        <span data-ru="Может ли один агент с 50 инструментами одновременно писать идеальный бэкенд, верстать UI и тестировать код?" data-en="Can a single generalist agent with 50 tools write backend, design UI, and run penetration tests flawlessly?">Bitta umumiy agent 50 ta vosita bilan bir vaqtda mukammal backend yozish, UI dizayn qilish va testlashni eplay oladimi?</span>
      </div>
      <span class="badge" style="font-size:11px;" data-ru="Нет, нужен Multi-Agent!" data-en="No, Multi-Agent needed!">Yo'q, chalkashib ketadi!</span>
    </div>
  </section>

  <!-- SLIDE 3: PROBLEM - MONOLITHIC VS MULTI-AGENT -->
  <section class="slide" data-phase="Muammo|Проблема|Problem" data-time="08:00–12:00" data-slide-index="2">
    <div class="eyebrow"><span class="t" data-ru="ОГРАНИЧЕНИЯ ЕДИНОГО АГЕНТА" data-en="MONOLITHIC AGENT BOTTLENECK">MONOLIT AGENT MUAMMOSI</span></div>
    <h2 data-ru="Почему Монолитный Агент Заваливает Сложные Задачи?" data-en="Why Do Monolithic Agents Fail at Complex Missions?">Nega Monolit Yagona Agent Murakkab Loyihalarda Qulaydi?</h2>
    <div class="grid-2">
      <div>
        <p class="lede" style="font-size:15px; margin-bottom:12px;" data-ru="Когда один промпт пытается заставить LLM быть архитектором, кодером и безопасником одновременно, наступает коллапс внимания." data-en="When a single prompt forces an LLM to be architect, programmer, and penetration tester at once, attention collapse occurs.">Bitta agentga bir vaqtning o'zida arxitektor, dasturchi, dizayner va xavfsizlik auditori bo'lish talabi qo'yilsa, diqqat chalkashadi.</p>
        <ul class="clean-list">
          <li data-ru="<strong>Перегрузка системного промпта:</strong> Промпт из 15 страниц правил приводит к тому, что модель игнорирует половину инструкций." data-en="<strong>System Prompt Bloat:</strong> 15-page instruction sets cause models to drop edge-case directives."><strong>System Prompt To'lib Ketishi:</strong> 10 sahifalik qoidalar to'plamida model yo'riqnomalarning yarmini esdan chiqaradi.</li>
          <li data-ru="<strong>Галлюцинации с инструментами:</strong> Имея 30 инструментов, агент путает аргументы и вызывает не те функции." data-en="<strong>Tool Call Hallucinations:</strong> With 30+ tools in schema, agents mix parameter signatures."><strong>Vositalar Chalkashishi:</strong> 30 ta tool berilsa, agent noto'g'ri funksiyalarni noto'g'ri parametr bilan chaqira boshlaydi.</li>
          <li data-ru="<strong>Отсутствие критики:</strong> Один агент не может беспристрастно проверить собственный свеженаписанный код." data-en="<strong>No Self-Critique:</strong> An authoring agent cannot objectively audit its own newly minted code."><strong>Tanqidning Yo'qligi:</strong> O'zi kod yozgan agent o'z xatolarini xolis tekshira olmaydi — mustaqil retsenzent (Reviewer) kerak!</li>
        </ul>
      </div>
      <div class="box" style="background:var(--surface-2); font-size:12px; line-height:1.6;">
        <div style="font-weight:700; color:var(--accent); margin-bottom:6px;" data-ru="Корпоративный Принцип Разделения Ответственности:" data-en="Enterprise Separation of Concerns:">Separation of Concerns (Mas'uliyatni Ajratish):</div>
        <div style="display:flex; flex-direction:column; gap:8px;">
          <div style="background:rgba(239,68,68,0.1); padding:6px 10px; border-radius:6px; border-left:3px solid var(--red);">
            <strong>Monolit Agent:</strong> 1 ta prompt, 30 ta vosita ➔ 62% xatolik ehtimoli, sekin javob.
          </div>
          <div style="background:rgba(16,185,129,0.1); padding:6px 10px; border-radius:6px; border-left:3px solid var(--green);">
            <strong>Multi-Agent Tizimi:</strong> 1 ta Supervisor + 3 ta ixcham Worker ➔ 94% muvaffaqiyatli topshirish, mustaqil testlash!
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- SLIDE 4: SUPERVISOR-WORKER PATTERN -->
  <section class="slide" data-phase="Arxitektura|Архитектура|Architecture" data-time="12:00–16:00" data-slide-index="3">
    <div class="eyebrow"><span class="t" data-ru="ПАТТЕРН SUPERVISOR-WORKER" data-en="SUPERVISOR-WORKER PATTERN">SUPERVISOR VA WORKER TUZILMASI</span></div>
    <h2 data-ru="Архитектура Команды Агентов: Кто за Что Отвечает?" data-en="Multi-Agent Team Architecture: Division of Roles">Multi-Agent Jamoasi Arxitekturasi: Rollar Taqsimoti</h2>
    <div class="grid-4" style="gap:10px;">
      <div class="box" style="border-top:3px solid var(--accent);">
        <div class="tag" style="color:var(--accent);">1. Supervisor</div>
        <h4 style="margin:6px 0;" data-ru="Координатор" data-en="Supervisor">Boshqaruvchi</h4>
        <p style="font-size:12px;" data-ru="Принимает задачу пользователя, разбивает на шаги и решает, кому передать ход: Researcher, Coder или Finish." data-en="Ingests user prompt, breaks into milestones, and decides next step: Researcher, Coder, or Finish.">Foydalanuvchi talabini o'qiydi, reja tuzadi va navbatdagi qadamni kimga berishni hal qiladi.</p>
      </div>
      <div class="box" style="border-top:3px solid var(--purple);">
        <div class="tag" style="color:var(--purple);">2. Researcher</div>
        <h4 style="margin:6px 0;" data-ru="Исследователь" data-en="Researcher">Tadqiqotchi</h4>
        <p style="font-size:12px;" data-ru="Имеет доступ к поиску и базам знаний. Собирает документацию, спецификации API и примеры." data-en="Equipped with web search and vector docs. Gathers API specs, schemas, and references.">Qidiruv va hujjatlar bilan ishlaydi. API spetsifikatsiyalari va kerakli bilimlarni to'playdi.</p>
      </div>
      <div class="box" style="border-top:3px solid var(--green);">
        <div class="tag" style="color:var(--green);">3. Coder Worker</div>
        <h4 style="margin:6px 0;" data-ru="Программист" data-en="Coder Worker">Dasturchi</h4>
        <p style="font-size:12px;" data-ru="Получает чистый контекст и пишет чистый, изолированный код строго по собранным спецификациям." data-en="Receives sanitized context and authors clean, modular code against research specs.">Tadqiqot xulosalarini oladi va faqat toza, xavfsiz kod yozishga e'tibor qaratadi.</p>
      </div>
      <div class="box" style="border-top:3px solid var(--amber);">
        <div class="tag" style="color:var(--amber);">4. Reviewer/Tester</div>
        <h4 style="margin:6px 0;" data-ru="Тестировщик" data-en="Reviewer/Tester">Tanqidchi/Audit</h4>
        <p style="font-size:12px;" data-ru="Проверяет написанный код на баги и OWASP уязвимости. Если находит ошибку — возвращает Coder'у." data-en="Audits authored code for bugs and security flaws. If bugs persist, routes back to Coder.">Kodni sintaktik va xavfsizlik (OWASP) bo'yicha tekshiradi. Xato topsa, Coderga qaytaradi.</p>
      </div>
    </div>
    <div style="margin-top:12px; font-family:var(--font-mono); font-size:11px; background:var(--surface-2); padding:8px 12px; border-radius:6px; color:var(--ink-2); display:flex; justify-content:space-between; align-items:center;">
      <span><strong>Xabarlar Marshruti:</strong> User ➔ Supervisor ➔ Researcher ➔ Supervisor ➔ Coder ➔ Reviewer ➔ Supervisor ➔ Finish!</span>
      <span class="badge" style="background:var(--accent); color:#fff;" data-ru="Цикл LangGraph" data-en="LangGraph Loop">LangGraph Loop</span>
    </div>
  </section>

  <!-- SLIDE 5: LANGGRAPH & STATEGRAPH -->
  <section class="slide" data-phase="Holat Grafigi|Граф Состояний|StateGraph" data-time="16:00–20:00" data-slide-index="4">
    <div class="eyebrow"><span class="t" data-ru="ОРКЕСТРАЦИЯ LANGGRAPH" data-en="LANGGRAPH ORCHESTRATION">STATEGRAPH VA SHARTLI QIRRALAR</span></div>
    <h2 data-ru="LangGraph: Граф Состояний и Условные Переходы (Edges)" data-en="LangGraph: StateGraph & Conditional Routing Edges">LangGraph: StateGraph va Shartli Qirralar (Conditional Edges)</h2>
    <div class="grid-2">
      <div>
        <pre><code class="language-python">from langgraph.graph import StateGraph, END
from typing import TypedDict, Annotated, Sequence

# 1. Umumiy jamoa holati (Shared State)
class TeamState(TypedDict):
    messages: Sequence[str]
    next_step: str
    code_artifact: str
    review_status: str

# 2. Grafigini yaratish
workflow = StateGraph(TeamState)

# 3. Tugunlar (Nodes)
workflow.add_node("supervisor", supervisor_node)
workflow.add_node("researcher", researcher_node)
workflow.add_node("coder", coder_node)
workflow.add_node("reviewer", reviewer_node)

# 4. Shartli marshrutlash (Conditional Edges)
workflow.add_conditional_edges(
    "supervisor",
    lambda state: state["next_step"],
    {"research": "researcher", "code": "coder", "finish": END}
)
workflow.add_edge("coder", "reviewer")
workflow.add_edge("reviewer", "supervisor")</code></pre>
      </div>
      <div>
        <h4 style="margin-bottom:6px; color:var(--accent);" data-ru="Ключевые понятия графа:" data-en="Core Graph Primitives:">Grafigining Asosiy Tushunchalari:</h4>
        <ul class="clean-list" style="font-size:12px;">
          <li data-ru="<strong>Общее состояние (Shared State):</strong> Единый источник правды, доступный всем агентам (сообщения, сгенерированный код, статус)." data-en="<strong>Shared State:</strong> The single source of shared truth across agents (messages, code, status)."><strong>Shared State:</strong> Barcha agentlar bir-birining natijasini o'qiydigan umumiy xotira.</li>
          <li data-ru="<strong>Узлы графа (Nodes):</strong> Изолированные функции, выполняющие логику конкретного специализированного агента." data-en="<strong>Nodes:</strong> Dedicated functions executing isolated agent reasoning cycles."><strong>Nodes (Tugunlar):</strong> Har bir agentning ixtisoslashgan funksiyasi.</li>
          <li data-ru="<strong>Условные переходы (Conditional Edges):</strong> Динамическая маршрутизация в зависимости от решения супервизора." data-en="<strong>Conditional Edges:</strong> Dynamic routers steering execution based on Supervisor decisions."><strong>Shartli Qirralar:</strong> Supervisor qaroriga qarab oqimni buruvchi yo'l ko'rsatkich.</li>
        </ul>
      </div>
    </div>
  </section>

  <!-- SLIDE 6: DEADLOCK PREVENTION & GUARDRAILS -->
  <section class="slide" data-phase="Xavfsizlik|Безопасность|Guardrails" data-time="20:00–24:00" data-slide-index="5">
    <div class="eyebrow"><span class="t" data-ru="БЕЗОПАСНОСТЬ МУЛЬТИАГЕНТОВ" data-en="MULTI-AGENT SAFETY">DEADLOCK VA CHEKSIZ SIKLLAR HIMOYA</span></div>
    <h2 data-ru="Как Предотвратить Бесконечный Спор Агентов? (Deadlocks)" data-en="Preventing Infinite Agent Debates: Loop Guards & Deadlocks">Agentlar Cheksiz Tortishib Qolishining Oldini Olish (Deadlock)</h2>
    <div class="grid-3" style="gap:12px;">
      <div class="box">
        <div class="tag" style="background:rgba(239,68,68,0.15); color:var(--red);">Max Iterations</div>
        <h4 data-ru="Лимит Шагов (Квота)" data-en="Max Iterations Cap">Qat'iy Qadam Cheklovi</h4>
        <p style="font-size:12px;" data-ru="Если Coder и Reviewer спорят более 5 раз, граф ПРИНУДИТЕЛЬНО останавливается, предотвращая утечку $1000 токенов." data-en="If Coder and Reviewer ping-pong for 5 rounds, graph execution is forcefully terminated to cap token burn.">Agar Coder va Reviewer 5 martadan ko'p tortishsa, tizim majburiy to'xtaydi va byudjetni saqlab qoladi.</p>
      </div>
      <div class="box">
        <div class="tag" style="background:rgba(16,185,129,0.15); color:var(--green);">State Reducer</div>
        <h4 data-ru="Контроль Слияния" data-en="Safe State Reducer">Xavfsiz Birlashtirish</h4>
        <p style="font-size:12px;" data-ru="Новые сообщения только ДОПИСЫВАЮТСЯ (append), а не перезаписывают память предыдущего агента." data-en="State messages are strictly appended using reducers, preventing race condition overwrites.">Yangi agentlar bir-birining xabarini o'chirib yubormasligi uchun append operatoridan foydalaniladi.</p>
      </div>
      <div class="box">
        <div class="tag" style="background:rgba(59,130,246,0.15); color:var(--accent);">Human-in-the-Loop</div>
        <h4 data-ru="Одобрение Человеком" data-en="Human-in-the-Loop">Inson Ruxsati (HITL)</h4>
        <p style="font-size:12px;" data-ru="Перед опасным действием (деплой, удаление файлов, запись в БД) агент запрашивает клик человека." data-en="Prior to critical mutations (deploy, disk write, DB delete), the workflow pauses for human approval.">Xavfli buyruqlar (deploy, o'chirish) bajarilishidan oldin tizim inson roziligini so'rab to'xtaydi.</p>
      </div>
    </div>
    <div class="box" style="margin-top:14px; background:rgba(0,0,0,0.2); border:1px solid var(--hair); font-family:var(--font-mono); font-size:11px;">
      <code>if state["iteration_count"] &gt;= 5: state["next_step"] = "escalate_to_human"</code>
    </div>
  </section>

  <!-- SLIDE 7: IN-DECK INTERACTIVE SIMULATOR -->
  <section class="slide" data-phase="Jonli Sinov|Интерактив|Live Demo" data-time="24:00–28:00" data-slide-index="6">
    <div class="eyebrow"><span class="t" data-ru="СИМУЛЯТОР В ПРЕЗЕНТАЦИИ" data-en="IN-DECK SIMULATOR">SMARTBOARDDA JONLI MULTI-AGENT SINOVI</span></div>
    <h2 data-ru="Интерактивный Граф: Пошаговая Оркестрация Агентов" data-en="Interactive Studio: Step-by-Step Multi-Agent Orchestration">Jonli Sinov: Multi-Agent Ish Oqimini Boshqarish</h2>
    <div class="box" style="padding:12px;">
      <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:10px;">
        <div style="display:flex; gap:8px;">
          <button class="btn" onclick="deckStartMultiAgent()" id="btnDeckAgentStart" style="background:var(--accent); color:#fff; padding:6px 14px; font-size:12px;" data-ru="⚡ Запустить Оркестрацию" data-en="⚡ Run Orchestration">⚡ Vazifani Ishga Tushirish</button>
          <button class="btn" onclick="deckResetMultiAgent()" style="padding:6px 10px; font-size:12px;" data-ru="Сброс" data-en="Reset">Qayta O'rnatish</button>
        </div>
        <div style="font-family:var(--font-mono); font-size:12px; color:var(--ink-2);">
          Faol Tugun: <strong style="color:var(--green);" id="deckActiveNode">SUPERVISOR</strong> | Sikl: <strong id="deckIterCount">0 / 5</strong>
        </div>
      </div>
      <div class="grid-2" style="gap:10px;">
        <div style="background:var(--surface-2); border-radius:8px; padding:10px; font-family:var(--font-mono); font-size:11px;">
          <div style="color:var(--accent); font-weight:700; margin-bottom:6px;">[XABARLAR VA STATE JURNALI]</div>
          <div id="deckAgentLog" style="height:120px; overflow-y:auto; line-height:1.5; color:var(--ink-2);">
            • Tizim tayyor. 'Vazifani Ishga Tushirish' tugmasini bosing...
          </div>
        </div>
        <div style="background:var(--surface-2); border-radius:8px; padding:10px; font-family:var(--font-mono); font-size:11px; display:flex; flex-direction:column; justify-content:space-between;">
          <div style="color:var(--purple); font-weight:700;">[STATEGRAPH TUGUNLAR HOLATI]</div>
          <div style="display:flex; flex-direction:column; gap:4px; margin:6px 0;">
            <div id="node_sup" style="padding:4px 8px; border-radius:4px; background:rgba(59,130,246,0.1); border:1px solid var(--accent); color:var(--accent);">👑 Supervisor (Router)</div>
            <div id="node_res" style="padding:4px 8px; border-radius:4px; background:rgba(255,255,255,0.03); color:var(--ink-2);">🔍 Researcher (Doc Search)</div>
            <div id="node_cod" style="padding:4px 8px; border-radius:4px; background:rgba(255,255,255,0.03); color:var(--ink-2);">💻 Coder (Implementation)</div>
            <div id="node_rev" style="padding:4px 8px; border-radius:4px; background:rgba(255,255,255,0.03); color:var(--ink-2);">🛡️ Reviewer (Security & QA)</div>
          </div>
          <div style="font-size:10px; color:var(--ink-2);" id="deckArtifactStatus">Artifakt: Kutilmoqda...</div>
        </div>
      </div>
    </div>
  </section>

  <!-- SLIDE 8: INTERACTIVE QUIZ -->
  <section class="slide" data-phase="Viktorina|Квиз|Quiz" data-time="28:00–32:00" data-slide-index="7">
    <div class="eyebrow"><span class="t" data-ru="ПРОВЕРКА ЗНАНИЙ" data-en="KNOWLEDGE CHECK">3-SAVOLLI INTERAKTIV TEST</span></div>
    <h2 data-ru="Блиц-Тест: Архитектура LangGraph и Мультиагентов" data-en="Fast Quiz: LangGraph & Multi-Agent Architecture">Bilimni Sinash: LangGraph va Multi-Agent Arxitekturasi</h2>
    <div class="quiz-container" style="display:flex; flex-direction:column; gap:12px;">
      <!-- Q1 -->
      <div class="box" style="padding:10px 14px;">
        <div style="font-weight:700; font-size:14px; margin-bottom:6px;" data-ru="1. Какова главная функция агента Supervisor в LangGraph?" data-en="1. What is the primary function of the Supervisor agent in LangGraph?">1. LangGraph arxitekturasida Supervisor agentining asosiy vazifasi nima?</div>
        <div class="quiz-options" style="display:flex; gap:8px; flex-wrap:wrap;">
          <button class="btn quiz-btn" onclick="checkQuiz(this, false, 'Bu ishni Coder agenti bajaradi.')" style="font-size:12px;" data-ru="A) Писать весь исходный код проекта" data-en="A) Writing all source code directly">A) Barcha kodni o'zi mustaqil yozish</button>
          <button class="btn quiz-btn" onclick="checkQuiz(this, true, 'To‘g‘ri! Supervisor boshqaruvchi sifatida qadamlarni ixtisoslashgan workerlarga marshrutlaydi.')" style="font-size:12px;" data-ru="B) Анализировать задачу и направлять ход нужному воркеру" data-en="B) Evaluate task state and route to appropriate worker">B) Topshiriqni tahlil qilib, navbatni kerakli workerga yo'naltirish</button>
          <button class="btn quiz-btn" onclick="checkQuiz(this, false, 'Bu xotira moduli vazifasi.')" style="font-size:12px;" data-ru="C) Хранить только векторные эмбеддинги" data-en="C) Storing only vector embeddings">C) Faqat vektor embeddinglarni saqlash</button>
        </div>
        <div class="quiz-feedback" style="font-size:12px; margin-top:4px; font-weight:600;"></div>
      </div>
      <!-- Q2 -->
      <div class="box" style="padding:10px 14px;">
        <div style="font-weight:700; font-size:14px; margin-bottom:6px;" data-ru="2. Что такое Conditional Edge (условное ребро) в графе состояний?" data-en="2. What is a Conditional Edge in a StateGraph?">2. StateGraph holat grafigida Conditional Edge (shartli qirra) nima?</div>
        <div class="quiz-options" style="display:flex; gap:8px; flex-wrap:wrap;">
          <button class="btn quiz-btn" onclick="checkQuiz(this, true, 'Aynan shunday! Funksiya qaytargan qiymatga qarab grafik keyingi mos agentga o‘tadi.')" style="font-size:12px;" data-ru="A) Переход к следующему узлу в зависимости от логики" data-en="A) Dynamic transition to next node based on state outcome">A) Holat natijasiga qarab keyingi mos tugunga yo'naltiruvchi shart</button>
          <button class="btn quiz-btn" onclick="checkQuiz(this, false, 'CSS chiziqlariga aloqasi yo‘q.')" style="font-size:12px;" data-ru="B) Цветная линия в интерфейсе браузера" data-en="B) Decorative CSS line in user interface">B) Brauzer interfeysidagi chiziq</button>
          <button class="btn quiz-btn" onclick="checkQuiz(this, false, 'Doimiy to‘xtatish faqat END tuguni bilan bo‘ladi.')" style="font-size:12px;" data-ru="C) Команда вечной остановки сервера" data-en="C) Command terminating server execution permanently">C) Serverni doimiy o'chiruvchi buyruq</button>
        </div>
        <div class="quiz-feedback" style="font-size:12px; margin-top:4px; font-weight:600;"></div>
      </div>
      <!-- Q3 -->
      <div class="box" style="padding:10px 14px;">
        <div style="font-weight:700; font-size:14px; margin-bottom:6px;" data-ru="3. Зачем в мультиагентных системах устанавливают лимит Max Iterations (например, 5 или 10)?" data-en="3. Why configure a Max Iterations cap (e.g. 5 or 10) in multi-agent workflows?">3. Nega multi-agent tizimlarida Max Iterations cheklovi qo'yilishi shart?</div>
        <div class="quiz-options" style="display:flex; gap:8px; flex-wrap:wrap;">
          <button class="btn quiz-btn" onclick="checkQuiz(this, false, 'Tezlikka bevosita ta‘siri yo‘q.')" style="font-size:12px;" data-ru="A) Чтобы компьютер работал быстрее" data-en="A) To accelerate CPU clock speed">A) Kompyuter tezroq ishlashi uchun</button>
          <button class="btn quiz-btn" onclick="checkQuiz(this, true, 'To‘g‘ri! Coder va Reviewer cheksiz tortishib byudjetni yoqib yubormasligi uchun.')" style="font-size:12px;" data-ru="B) Предотвратить бесконечный цикл спора и слив токенов" data-en="B) Prevent infinite debate loops and runaway token billing">B) Agentlar cheksiz aylanib, barcha tokenlarni sarflab yubormasligi uchun</button>
          <button class="btn quiz-btn" onclick="checkQuiz(this, false, 'Xatolar soniga cheklov qo‘yilmaydi.')" style="font-size:12px;" data-ru="C) Чтобы ограничить размер файла" data-en="C) To restrict generated file sizes">C) Fayl hajmini cheklash uchun</button>
        </div>
        <div class="quiz-feedback" style="font-size:12px; margin-top:4px; font-weight:600;"></div>
      </div>
    </div>
  </section>

  <!-- SLIDE 9: HANDS-ON ARENA -->
  <section class="slide" data-phase="Amaliyot|Практика|Hands-on Lab" data-time="32:00–37:00" data-slide-index="8">
    <div class="eyebrow"><span class="t" data-ru="ПРАКТИЧЕСКАЯ МИССИЯ" data-en="HANDS-ON LAB MISSION">15 DAQIQALIK KIBER-ARENA</span></div>
    <h2 data-ru="Лаборатория: Собери Supervisor Маршрутизатор" data-en="Lab Mission: Build a Supervisor Workflow Router">Kiber-Missiya: Supervisor Marshrutlash Grafigini Yaratish</h2>
    <div class="grid-2">
      <div>
        <p class="lede" style="font-size:14px; margin-bottom:10px;" data-ru="Откройте симулятор simulator/index.html и реализуйте функцию диспетчеризации Supervisor." data-en="Launch simulator/index.html and implement the Supervisor dispatch logic.">Darsning <a href="simulator/index.html" target="_blank" style="color:var(--accent); font-weight:700;">simulator/index.html</a> laboratoriyasini oching va Supervisor dispetcherini ishga tushiring.</p>
        <ul class="clean-list">
          <li data-ru="<strong>1-Шаг:</strong> Задайте схему <code>TeamState</code> с полями <code>task</code>, <code>next_agent</code>, <code>iterations</code>." data-en="<strong>Step 1:</strong> Define <code>TeamState</code> schema containing <code>task</code>, <code>next_agent</code>, <code>iterations</code>."><strong>1-Qadam:</strong> <code>TeamState</code> holat obyektini tuzing.</li>
          <li data-ru="<strong>2-Шаг:</strong> Напишите логику <code>supervisor_router(state)</code>: если задача требует поиска ➔ 'researcher', если код ➔ 'coder'." data-en="<strong>Step 2:</strong> Implement <code>supervisor_router(state)</code> to steer tasks based on intent."><strong>2-Qadam:</strong> <code>supervisor_router(state)</code> funksiyasini yozing: qidiruv kerak bo'lsa ➔ 'researcher', kod bo'lsa ➔ 'coder'.</li>
          <li data-ru="<strong>3-Шаг:</strong> Добавьте ограничение <code>iterations &gt;= 5</code> для безопасного выхода (FINISH)." data-en="<strong>Step 3:</strong> Enforce <code>iterations &gt;= 5</code> guard for safe termination."><strong>3-Qadam:</strong> Cheksiz aylanishdan himoya qiluvchi <code>iterations &gt;= 5</code> qoidasini qo'ying.</li>
        </ul>
      </div>
      <div class="box" style="border-left:4px solid var(--accent);">
        <h4 style="margin-bottom:8px;" data-ru="10-Балльная Рубрика Оценки:" data-en="10-Point Grading Rubric:">10 Ballik Baholash Mezoni:</h4>
        <div style="font-size:12px; line-height:1.8;">
          <div><strong style="color:var(--green);">4 Ball:</strong> Supervisor router funksiyasi to'g'ri qaror qabul qiladi.</div>
          <div><strong style="color:var(--accent);">4 Ball:</strong> Workerlar natijasi State obyekti orqali to'g'ri uzatiladi va sintezlanadi.</div>
          <div><strong style="color:var(--purple);">2 Ball (Bonus):</strong> Max Iterations va Deadlock Guard to'liq sozlangan.</div>
        </div>
      </div>
    </div>
  </section>

  <!-- SLIDE 10: TIERED HOMEWORK & SUMMARY -->
  <section class="slide" data-phase="Uy Vazifasi|Домашнее Задание|Tiered Homework" data-time="37:00–40:00" data-slide-index="9">
    <div class="eyebrow"><span class="t" data-ru="ИТОГИ И ДОМАШНЕЕ ЗАДАНИЕ" data-en="SUMMARY & HOMEWORK">XULOSA VA 3 DARAJALI VAZIFA</span></div>
    <h2 data-ru="Итоги 28-Урока и Мост к Завтрашнему Двойному Уроку" data-en="Lesson 28 Recap & Bridge to Tomorrow's Double Class">Xulosa va Ertangi Katta Juftlik Darsiga Ko'prik</h2>
    <div class="grid-3" style="gap:10px;">
      <div class="box" style="border-top:3px solid var(--green);">
        <div class="tag" style="color:var(--green);">1-Daraja: Baza (4 ball)</div>
        <h4 data-ru="Базовый Диспетчер" data-en="Basic Dispatcher">Supervisor Router</h4>
        <p style="font-size:12px;" data-ru="Реализуйте функцию маршрутизатора, распределяющую 3 вида задач между researcher и coder." data-en="Implement a router function dispatching 3 task types between researcher and coder.">Topshiriq turiga qarab 3 xil vazifani mos workerlarga yo'naltiruvchi router yozing.</p>
      </div>
      <div class="box" style="border-top:3px solid var(--accent);">
        <div class="tag" style="color:var(--accent);">2-Daraja: Loyiha (4 ball)</div>
        <h4 data-ru="Coder + Reviewer Цикл" data-en="Coder + Reviewer Loop">Coder va Reviewer Zanjiri</h4>
        <p style="font-size:12px;" data-ru="Постройте цикл исправления: Reviewer находит ошибку, Coder исправляет, пока статус не станет APPROVED." data-en="Build remediation loop: Reviewer catches bug, Coder fixes until status is APPROVED.">Reviewer xato topsa, Coder xatoni to'g'rilab qayta topshiruvchi 2-bosqichli zanjir quring.</p>
      </div>
      <div class="box" style="border-top:3px solid var(--purple);">
        <div class="tag" style="color:var(--purple);">3-Daraja: Challenge (2 ball)</div>
        <h4 data-ru="Human Approval Gate" data-en="Human Approval Gate">Inson Ruxsati (HITL)</h4>
        <p style="font-size:12px;" data-ru="Добавьте паузу в графе: перед отправкой финального кода система ждет одобрения пользователя." data-en="Add workflow interruption: pauses before code release awaiting human confirmation.">Kodni chiqarishdan oldin inson roziligini so'rab pauza qiluvchi Human-in-the-Loop darvozasini quring.</p>
      </div>
    </div>
    <div class="bridge-card" style="margin-top:12px; padding:10px 16px; border-radius:10px; background:rgba(147,51,234,0.08); border-left:4px solid var(--purple); display:flex; justify-content:space-between; align-items:center;">
      <div>
        <strong style="color:var(--purple);" data-ru="Завтра (Двойной Урок 80 мин):" data-en="Tomorrow (Double Block 80 min):">🚀 Ertaga (80 Daqiqalik Juftlik Dars):</strong>
        <span data-ru="Автономная Команда Разработки: Multi-Agent Software Agency, создающая готовый сервис с нуля!" data-en="Autonomous Engineering Team: Multi-Agent Software Agency building full-stack apps from scratch!">Avtonom Dasturiy Injiniring: Noldan to'liq ishchi servisni yaratuvchi Multi-Agent Jamoasi!</span>
      </div>
      <a href="vazifa.html" class="btn" style="background:var(--purple); color:#fff; font-size:12px;" data-ru="Открыть ДЗ" data-en="Open HW">Vazifani Ochish ➔</a>
    </div>
  </section>
"""

# In-deck JS for Slide 7 multi-agent simulator
IN_DECK_JS = """
// --- IN-DECK MULTI-AGENT ORCHESTRATION SIMULATOR ---
var deckAgentIter = 0;
var deckAgentRunning = false;
var deckAgentTimer = null;

function deckAgentLog(msg, color) {
  var el = document.getElementById('deckAgentLog');
  if (!el) return;
  var row = document.createElement('div');
  row.style.color = color || 'var(--ink)';
  row.style.margin = '2px 0';
  row.textContent = '• ' + msg;
  el.appendChild(row);
  el.scrollTop = el.scrollHeight;
}

function deckHighlightNode(nodeId) {
  ['node_sup', 'node_res', 'node_cod', 'node_rev'].forEach(function(id) {
    var el = document.getElementById(id);
    if (!el) return;
    if (id === nodeId) {
      el.style.background = 'var(--accent)';
      el.style.color = '#fff';
      el.style.fontWeight = '700';
    } else {
      el.style.background = 'rgba(255,255,255,0.03)';
      el.style.color = 'var(--ink-2)';
      el.style.fontWeight = '400';
    }
  });
}

function deckStartMultiAgent() {
  document.getElementById('btnDeckAgentStart').disabled = true;
  deckAgentIter = 0;
  deckAgentLog('Vazifa kelib tushdi: "Xavfsiz JWT Auth moduli yozilsin"', 'var(--ink)');
  deckRunStep1_Supervisor();
}

function deckRunStep1_Supervisor() {
  deckAgentIter++;
  document.getElementById('deckIterCount').textContent = deckAgentIter + ' / 5';
  document.getElementById('deckActiveNode').textContent = 'SUPERVISOR';
  deckHighlightNode('node_sup');
  deckAgentLog('👑 Supervisor: Vazifa o‘rganilmoqda. 1-qadam: Hujjatlarni tekshirish kerak.', 'var(--accent)');

  setTimeout(function() {
    deckRunStep2_Researcher();
  }, 900);
}

function deckRunStep2_Researcher() {
  document.getElementById('deckActiveNode').textContent = 'RESEARCHER';
  deckHighlightNode('node_res');
  deckAgentLog('🔍 Researcher: RFC 7519 va JWT xavfsiz algoritmlari (RS256) o‘rganildi.', 'var(--purple)');

  setTimeout(function() {
    deckRunStep3_Coder();
  }, 1000);
}

function deckRunStep3_Coder() {
  document.getElementById('deckActiveNode').textContent = 'CODER';
  deckHighlightNode('node_cod');
  deckAgentLog('💻 Coder: signJWT() va verifyJWT() funksiyalari yozildi.', 'var(--green)');
  document.getElementById('deckArtifactStatus').textContent = 'Artifakt: auth.js (Generatsiya qilindi)';

  setTimeout(function() {
    deckRunStep4_Reviewer();
  }, 1000);
}

function deckRunStep4_Reviewer() {
  document.getElementById('deckActiveNode').textContent = 'REVIEWER';
  deckHighlightNode('node_rev');
  deckAgentLog('🛡️ Reviewer: Kod tekshirildi: Zaifliklar topilmadi. Status: APPROVED ✅', 'var(--green)');

  setTimeout(function() {
    document.getElementById('deckActiveNode').textContent = 'FINISH';
    deckHighlightNode('node_sup');
    deckAgentLog('🎉 Supervisor: Multi-Agent zanjiri muvaffaqiyatli yakunlandi! Natija tayyor.', 'var(--accent)');
    document.getElementById('btnDeckAgentStart').disabled = false;
  }, 900);
}

function deckResetMultiAgent() {
  deckAgentIter = 0;
  document.getElementById('deckIterCount').textContent = '0 / 5';
  document.getElementById('deckActiveNode').textContent = 'SUPERVISOR';
  deckHighlightNode('node_sup');
  document.getElementById('deckAgentLog').innerHTML = '• Qayta ishga tushirildi. Tugmani bosing...';
  document.getElementById('deckArtifactStatus').textContent = 'Artifakt: Kutilmoqda...';
  document.getElementById('btnDeckAgentStart').disabled = false;
}

function checkQuiz(btn, isCorrect, feedbackText) {
  var parent = btn.closest('.box');
  var allBtns = parent.querySelectorAll('.quiz-btn');
  allBtns.forEach(function(b) {
    b.disabled = true;
    b.style.opacity = '0.6';
  });
  btn.style.opacity = '1';
  var fb = parent.querySelector('.quiz-feedback');
  if (isCorrect) {
    btn.style.background = 'var(--green)';
    btn.style.color = '#fff';
    fb.style.color = 'var(--green)';
    fb.textContent = '✅ ' + feedbackText;
  } else {
    btn.style.background = 'var(--red)';
    btn.style.color = '#fff';
    fb.style.color = 'var(--red)';
    fb.textContent = '❌ ' + feedbackText;
  }
}
"""

# Notes array for 10 slides
NOTES_DATA = {
    "uz": [
        ["Kirish va Maqsad", "O'quvchilarga bugungi dars mavzusi: Multi-Agent tizimlari va LangGraph arxitekturasi haqida so'zlab bering.", "Doskaga Monolit Agent vs Multi-Agent jamoasi farqini chizing."],
        ["Uy Vazifasi Tahlili", "27-darsdagi xotira xatosini (bazani to'liq promptga tiqish) tushuntiring.", "Oltin yechim: Top-K vektor qidiruvi kontekstni qanday qutqarishini eslatib bering."],
        ["Monolit Agent Muammosi", "Nega bitta agent hamma narsani bir vaqtda qila olmasligini (diqqat chalkashishi) tushuntiring.", "Mas'uliyatni ajratish (Separation of Concerns) korporativ tamoyilini ayting."],
        ["Supervisor-Worker Naqshi", "Supervisor, Researcher, Coder va Reviewer vazifalarini ko'rsating.", "Har bir agent o'z ishini a'lo darajada bajarib, navbatni boshqasiga uzatishini tushuntiring."],
        ["LangGraph va StateGraph", "LangGraph-da State, Nodes va Conditional Edges qanday ishlashini ko'rsating.", "Python TypedDict orqali umumiy holatni boshqarish sintaksisini tahlil qiling."],
        ["Deadlock va Xavfsizlik", "Agentlar cheksiz tortishib qolmasligi uchun Max Iterations va Human-in-the-Loop zarurligini ta'kidlang.", "Token xarajatlarini nazorat qilish usullarini ayting."],
        ["Smartboardda Jonli Sinov", "Slayd ichidagi simulyatorda vazifani ishga tushiring.", "Xabarlar bir agentdan ikkinchisiga qanday o'tishini butun sinfga ko'rsating."],
        ["Bilimni Sinash (Quiz)", "3 ta savol bo'yicha tezkor blitz o'tkazing.", "Har bir javobni tahlil qilib bering."],
        ["Amaliy Missiya", "O'quvchilarga simulator/index.html ni ochishni buyuring.", "Supervisor-Worker router funksiyasini yozishlarini nazorat qiling."],
        ["Xulosa va Ertangi Dars", "3 darajali uy vazifasini tushuntiring.", "Ertaga bo'ladigan 80 daqiqalik juftlik darsida to'liq avtonom dasturchilar jamoasini ishga tushirishimizni ayting!"]
    ],
    "ru": [
        ["Введение и Цель", "Представьте тему: мультиагентные системы и оркестрация в LangGraph.", "Нарисуйте на доске разницу между монолитным агентом и командой воркеров."],
        ["Разбор Домашнего Задания", "Разберите ошибку перегрузки промпта полным дампом БД из 27-го урока.", "Напомните золотой стандарт семантического поиска Top-K."],
        ["Проблема Монолита", "Объясните, почему один агент не может одновременно быть исследователем, программистом и аудитором.", "Объясните корпоративный принцип Separation of Concerns."],
        ["Паттерн Supervisor-Worker", "Покажите роли: Супервизор, Исследователь, Программист и Ревьюер.", "Объясните цикл передачи эстафеты между агентами."],
        ["LangGraph и StateGraph", "Разберите концепции State, Nodes и Conditional Edges.", "Поясните структуру TypedDict для общего состояния."],
        ["Защита от Тупиков (Deadlock)", "Объясните необходимость лимита Max Iterations и Human-in-the-Loop.", "Покажите предотвращение слива токенов."],
        ["Интерактив на Доске", "Запустите пошаговую симуляцию оркестрации в слайде.", "Покажите переключение активных узлов графа."],
        ["Тест (Квиз)", "Проведите опрос по 3 контрольным вопросам.", "Разберите причины ошибок."],
        ["Практическая Лаборатория", "Дайте команду открыть simulator/index.html.", "Курируйте написание логики маршрутизатора за 15 минут."],
        ["Итоги и Анонс", "Объясните 3 уровня домашнего задания.", "Анонсируйте завтрашний двойной урок (80 мин): автономное агентство разработки программного обеспечения!"]
    ],
    "en": [
        ["Intro & Objectives", "Introduce multi-agent systems and LangGraph workflow orchestration.", "Diagram monolithic agents vs specialized worker squads on the board."],
        ["Homework Review", "Review the raw DB dump trap from Lesson 27.", "Reiterate the golden solution: semantic Top-K retrieval."],
        ["The Monolith Bottleneck", "Explain why generalist single agents suffer from attention collapse on large tasks.", "Present the enterprise principle of Separation of Concerns."],
        ["Supervisor-Worker Pattern", "Detail roles: Supervisor router, Researcher, Coder, and QA Reviewer.", "Trace message passing across the team."],
        ["LangGraph & StateGraph", "Break down StateGraph primitives: Shared State, Nodes, and Conditional Edges.", "Review Python TypedDict syntax for state merging."],
        ["Deadlock & Guardrails", "Emphasize Max Iterations caps and Human-in-the-Loop gates.", "Discuss protecting enterprise API token budgets."],
        ["In-Deck Live Demo", "Trigger the in-deck multi-agent workflow visualizer.", "Trace execution transitions across nodes in real-time."],
        ["Knowledge Check (Quiz)", "Facilitate the 3 quick questions with the class.", "Clarify why distractors fail."],
        ["Hands-on Lab Mission", "Instruct students to open simulator/index.html.", "Guide the 15-minute challenge to implement a Supervisor routing engine."],
        ["Summary & Next Class", "Detail the 3-tiered homework assignment.", "Preview tomorrow's 80-minute double block: autonomous multi-agent software engineering agency!"]
    ]
}

def build_presentation():
    with open(os.path.join(REPO_ROOT, "assets", "TEMPLATE_PREZENTATSIYA.html"), "r", encoding="utf-8") as f:
        tpl = f.read()

    title_uz = "28-dars: Multi-Agent Tizimlari: Supervisor va Worker"
    title_ru = "Урок 28: Мультиагентные Системы: Supervisor и Worker"
    title_en = "Lesson 28: Multi-Agent Systems: Supervisor & Worker"

    tpl = re.sub(r"<title[^>]*>.*?</title>",
                 f'<title data-ru="{title_ru}" data-en="{title_en}">{title_uz}</title>',
                 tpl)

    tpl = re.sub(r'<span class="tag"[^>]*>.*?</span>',
                 '<span class="tag" data-ru="10–11 КЛАСС" data-en="GRADE 10–11">10–11-SINF</span>',
                 tpl)

    titles_json = json.dumps({"uz": title_uz, "ru": title_ru, "en": title_en}, ensure_ascii=False, indent=2)
    tpl = re.sub(r'var TITLES\s*=\s*\{[\s\S]*?\};', f'var TITLES = {titles_json};', tpl)

    notes_json = json.dumps(NOTES_DATA, ensure_ascii=False, indent=2)
    tpl = re.sub(r'var NOTES\s*=\s*\{[\s\S]*?\};', f'var NOTES = {notes_json};', tpl)

    stage_regex = r'<div class="stage">[\s\S]*?</div><!-- /stage -->'
    new_stage = f'<div class="stage">\n{SLIDES_HTML}\n  </div><!-- /stage -->'
    tpl = re.sub(stage_regex, new_stage, tpl)

    tpl = tpl.replace("</script>\n</body>", f"\n{IN_DECK_JS}\n</script>\n</body>")

    out_path = os.path.join(DEST_DIR, "prezentatsiya.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(tpl)
    print("  ✓ Created: prezentatsiya.html")

# -----------------------------------------------------------------------------
# 2. WORKSHEET (varaqa.html)
# -----------------------------------------------------------------------------
def build_worksheet():
    with open(os.path.join(REPO_ROOT, "assets", "TEMPLATE_VARAQA.html"), "r", encoding="utf-8") as f:
        tpl = f.read()

    tpl = tpl.replace("{{COHORT_LABEL}}", "10–11-sinf")
    tpl = tpl.replace("{{WEEK_NUM}}", "11")
    tpl = tpl.replace("{{LESSON_NUM}}", "28")
    tpl = tpl.replace("{{TRACK_UZ}}", "Senior AI & Enterprise Kiberxavfsizlik Track")
    tpl = tpl.replace("{{TRACK_RU}}", "Senior AI & Enterprise Кибербезопасность")
    tpl = tpl.replace("{{TRACK_EN}}", "Senior AI & Enterprise Cybersecurity Track")
    tpl = tpl.replace("{{LESSON_TITLE_UZ}}", "Multi-Agent Tizimlari: Supervisor va Worker Naqshlari (LangGraph)")
    tpl = tpl.replace("{{LESSON_TITLE_RU}}", "Мультиагентные Системы: Паттерны Supervisor и Worker в LangGraph")
    tpl = tpl.replace("{{LESSON_TITLE_EN}}", "Multi-Agent Systems: Supervisor & Worker Patterns in LangGraph")

    sec1_html = """
    <p style="font-size:12px; line-height:1.5; margin-bottom:8px;" data-ru="В корпоративной разработке один агент не способен писать код, проводить аудит безопасности и проектировать архитектуру одновременно. Паттерн Supervisor-Worker разделяет ответственность: Супервизор принимает решения и направляет задачи узкоспециализированным воркерам." data-en="In enterprise AI, monolithic agents fail at executing full software lifecycles concurrently. The Supervisor-Worker pattern introduces separation of concerns: a coordinator plans milestones and routes subtasks to specialized workers.">Korporativ AI amaliyotida monolit yagona agent bir vaqtning o'zida kod yozish, xavfsizlik auditi va arxitektura dizaynini eplay olmaydi. Supervisor-Worker naqshi mas'uliyatni ajratadi: Boshqaruvchi vazifani tahlil qiladi va ixtisoslashgan workerlarga yo'naltiradi.</p>
    <div style="background:var(--surface-2); padding:6px 10px; border-radius:6px; font-size:11px; font-family:var(--font-mono); border-left:3px solid var(--accent);">
      <strong>Asosiy Standart:</strong> LangGraph StateGraph + Supervisor Router + Specialized Workers (Researcher, Coder, Reviewer) + Deadlock Guard (Max Iterations).
    </div>
    """

    sec2_html = """
    <pre style="background:var(--surface-2); padding:8px; border-radius:6px; font-size:11px; font-family:var(--font-mono); line-height:1.4; border:1px solid var(--hair);"><code># Supervisor Router Mantig'i
def supervisor_router(state: TeamState) -> str:
    if state["iterations"] >= 5:
        return END  # Deadlock himoyasi
    last_msg = state["messages"][-1]
    if "hujjat" in last_msg or "qidiruv" in last_msg:
        return "researcher"
    elif "kod" in last_msg or "funksiya" in last_msg:
        return "coder"
    elif "test" in last_msg or "tekshir" in last_msg:
        return "reviewer"
    return END</code></pre>
    """

    sec3_html = """
    <div style="overflow-x:auto;">
      <table style="width:100%; border-collapse:collapse; font-size:11px; text-align:left;">
        <thead>
          <tr style="border-bottom:1px solid var(--hair); background:rgba(0,0,0,0.03);">
            <th style="padding:4px 6px;">#</th>
            <th style="padding:4px 6px;" data-ru="Роль Агента" data-en="Agent Role">Agent Roli</th>
            <th style="padding:4px 6px;" data-ru="Зона Ответственности" data-en="Responsibility">Mas'uliyat Sohası</th>
            <th style="padding:4px 6px;" data-ru="Входные / Выходные Данные" data-en="I/O Payload">Kirish / Chiqish Ma'lumoti</th>
            <th style="padding:4px 6px;" data-ru="Статус" data-en="Status">Holat</th>
          </tr>
        </thead>
        <tbody>
          <tr style="border-bottom:1px dashed var(--hair);">
            <td style="padding:4px 6px;">1</td>
            <td style="padding:4px 6px;" data-ru="Supervisor" data-en="Supervisor"><code>Supervisor</code></td>
            <td style="padding:4px 6px;" data-ru="Анализ плана и маршрутизация" data-en="Planning & Routing">Rejalashtirish va marshrutlash</td>
            <td style="padding:4px 6px;" data-ru="Task ➔ next_worker" data-en="Task ➔ next_worker">Task ➔ next_worker</td>
            <td style="padding:4px 6px;" data-ru="[ &nbsp; ] Изучено" data-en="[ &nbsp; ] Done">[ &nbsp; ] O'rganildi</td>
          </tr>
          <tr style="border-bottom:1px dashed var(--hair);">
            <td style="padding:4px 6px;">2</td>
            <td style="padding:4px 6px;" data-ru="Researcher" data-en="Researcher"><code>Researcher</code></td>
            <td style="padding:4px 6px;" data-ru="Поиск спецификаций и документации" data-en="Docs & Spec Gathering">Hujjatlar va spetsifikatsiyalarni izlash</td>
            <td style="padding:4px 6px;" data-ru="Query ➔ research_notes" data-en="Query ➔ research_notes">Query ➔ research_notes</td>
            <td style="padding:4px 6px;" data-ru="[ &nbsp; ] Изучено" data-en="[ &nbsp; ] Done">[ &nbsp; ] O'rganildi</td>
          </tr>
          <tr style="border-bottom:1px dashed var(--hair);">
            <td style="padding:4px 6px;">3</td>
            <td style="padding:4px 6px;" data-ru="Coder" data-en="Coder"><code>Coder</code></td>
            <td style="padding:4px 6px;" data-ru="Написание чистого модульного кода" data-en="Clean Code Authoring">Toza modulli kod yozish</td>
            <td style="padding:4px 6px;" data-ru="Specs ➔ code_artifact" data-en="Specs ➔ code_artifact">Specs ➔ code_artifact</td>
            <td style="padding:4px 6px;" data-ru="[ &nbsp; ] Изучено" data-en="[ &nbsp; ] Done">[ &nbsp; ] O'rganildi</td>
          </tr>
          <tr>
            <td style="padding:4px 6px;">4</td>
            <td style="padding:4px 6px;" data-ru="Reviewer" data-en="Reviewer"><code>Reviewer</code></td>
            <td style="padding:4px 6px;" data-ru="Аудит кода и безопасность OWASP" data-en="Code Audit & OWASP QA">Kod sifati va kiberxavfsizlik auditi</td>
            <td style="padding:4px 6px;" data-ru="Code ➔ APPROVED / REJECT" data-en="Code ➔ APPROVED / REJECT">Code ➔ APPROVED / REJECT</td>
            <td style="padding:4px 6px;" data-ru="[ &nbsp; ] Изучено" data-en="[ &nbsp; ] Done">[ &nbsp; ] O'rganildi</td>
          </tr>
        </tbody>
      </table>
    </div>
    """

    sec4_html = """
    <p style="font-size:12px; margin-bottom:6px;" data-ru="Запустите симулятор мультиагентов. Проведите задачу через весь цикл (Supervisor ➔ Researcher ➔ Coder ➔ Reviewer). Запишите итоговый статус:" data-en="Run the multi-agent simulator. Step through the entire cycle (Supervisor ➔ Researcher ➔ Coder ➔ Reviewer). Record final status:">Multi-agent simulyatorini ishga tushiring. Vazifani to'liq zanjir bo'ylab o'tkazing (Supervisor ➔ Researcher ➔ Coder ➔ Reviewer). Chiqqan natijalarni yozing:</p>
    <div style="border:1px dashed var(--hair); border-radius:6px; height:80px; padding:8px; font-family:var(--font-mono); font-size:11px; color:var(--ink-2);" data-ru="[Итоговый статус ревью, число итераций и сгенерированный артефакт]" data-en="[Final review status, iterations count, and generated artifact]">
      // Yakuniy review xulosasi: ___________________ (APPROVED / REJECT)<br>
      // Sarflangan iteratsiyalar soni: ___________________ ta<br>
      // Yaratilgan artifakt nomi: ___________________
    </div>
    """

    rubric_html = """
    <div style="display:grid; grid-template-columns:1fr 1fr 1fr; gap:8px; font-size:11px;">
      <div style="border-left:3px solid var(--green); padding-left:6px;">
        <strong style="color:var(--green);" data-ru="4 Балла: База" data-en="4 Pts: Base">4 Ball: Baza</strong>
        <p style="margin:2px 0;" data-ru="Схема TeamState и функция Supervisor Router написаны без ошибок." data-en="TeamState schema and Supervisor Router function implemented cleanly.">TeamState sxemasi va Supervisor Router funksiyasi xatoliksiz tuzilgan.</p>
      </div>
      <div style="border-left:3px solid var(--accent); padding-left:6px;">
        <strong style="color:var(--accent);" data-ru="4 Балла: Проект" data-en="4 Pts: Project">4 Ball: Loyiha</strong>
        <p style="margin:2px 0;" data-ru="Условные ребра связывают воркеров, сообщения корректно передаются по графу." data-en="Conditional edges route workers, messages pass across graph smoothly.">Shartli qirralar workerlarni to'g'ri ulaydi, xabarlar oqimi buzilmaydi.</p>
      </div>
      <div style="border-left:3px solid var(--purple); padding-left:6px;">
        <strong style="color:var(--purple);" data-ru="2 Балла: Challenge" data-en="2 Pts: Challenge">2 Ball: Challenge</strong>
        <p style="margin:2px 0;" data-ru="Ограничение Max Iterations и Human-in-the-Loop шлюз одобрения." data-en="Max Iterations cap and Human-in-the-Loop approval gate configured.">Max Iterations cheklovi va Human-in-the-Loop darvozasi sozlangan.</p>
      </div>
    </div>
    """

    tpl = tpl.replace("{{SEC1_CONTENT}}", sec1_html)
    tpl = tpl.replace("{{SEC2_CONTENT}}", sec2_html)
    tpl = tpl.replace("{{SEC3_CONTENT}}", sec3_html)
    tpl = tpl.replace("{{SEC4_CONTENT}}", sec4_html)
    tpl = tpl.replace("{{RUBRIC_CONTENT}}", rubric_html)

    out_path = os.path.join(DEST_DIR, "varaqa.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(tpl)
    print("  ✓ Created: varaqa.html")

# -----------------------------------------------------------------------------
# 3. INTERACTIVE HOMEWORK (vazifa.html)
# -----------------------------------------------------------------------------
def build_homework():
    with open(os.path.join(REPO_ROOT, "assets", "TEMPLATE_VAZIFA.html"), "r", encoding="utf-8") as f:
        tpl = f.read()

    tpl = tpl.replace("{{COHORT_LABEL}}", "10–11-sinf")
    tpl = tpl.replace("{{WEEK_NUM}}", "11")
    tpl = tpl.replace("{{LESSON_NUM}}", "28")
    tpl = tpl.replace("{{TRACK_UZ}}", "Senior AI & Enterprise Kiberxavfsizlik Track")
    tpl = tpl.replace("{{TRACK_RU}}", "Senior AI & Enterprise Кибербезопасность")
    tpl = tpl.replace("{{TRACK_EN}}", "Senior AI & Enterprise Cybersecurity Track")
    tpl = tpl.replace("{{LESSON_TITLE_UZ}}", "Multi-Agent Tizimlari: Supervisor va Worker Naqshlari (LangGraph)")
    tpl = tpl.replace("{{LESSON_TITLE_RU}}", "Мультиагентные Системы: Паттерны Supervisor и Worker в LangGraph")
    tpl = tpl.replace("{{LESSON_TITLE_EN}}", "Multi-Agent Systems: Supervisor & Worker Patterns in LangGraph")
    tpl = tpl.replace("{{TOTAL_TASKS}}", "3")

    tasks_html = """
  <!-- 1-DARAJA: BAZA -->
  <div class="task-card">
    <div class="task-header">
      <span class="task-badge tier-1" data-ru="1-Уровень: База (4 балла)" data-en="Tier 1: Base (4 pts)">1-Daraja: Baza (4 ball)</span>
      <h3 style="margin:4px 0;" data-ru="Схема Состояния TeamState и Маршрутизатор" data-en="TeamState Schema & Router Function">TeamState Holat Sxemasi va Supervisor Router</h3>
    </div>
    <p style="font-size:13px; line-height:1.5; color:var(--ink-2);" data-ru="Опишите схему состояния <code>TeamState</code> (на Python TypedDict или JavaScript объекте) и напишите функцию <code>route_task(state)</code>, которая по ключевым словам в задаче направляет ее к 'researcher', 'coder' или завершает работу ('END')." data-en="Define the <code>TeamState</code> schema and write a <code>route_task(state)</code> function that inspects incoming prompt keywords to route between 'researcher', 'coder', or 'END'."><code>TeamState</code> umumiy holat sxemasini tuzing va vazifadagi kalit so'zlarga qarab uni 'researcher', 'coder' yoki 'END' ga yo'naltiruvchi <code>route_task(state)</code> funksiyasini yozing.</p>
    <textarea class="answer-area" id="ans_task_1" rows="7" placeholder="Kodingizni bu yerga yozing..." data-placeholder-ru="Напишите ваш код здесь..." data-placeholder-en="Write your code here..." oninput="saveAnswers()"></textarea>
    <div class="teacher-sol" id="sol_task_1">
      <strong style="color:var(--green);" data-ru="Эталонное решение:" data-en="Model Solution:">Oltin Yechim:</strong>
      <pre><code>from typing import TypedDict, List

class TeamState(TypedDict):
    task: str
    messages: List[str]
    iterations: int

def route_task(state: TeamState) -> str:
    if state.get("iterations", 0) >= 5:
        return "END"
    task_lower = state["task"].lower()
    if any(k in task_lower for k in ["search", "hujjat", "find", "arxiv"]):
        return "researcher"
    elif any(k in task_lower for k in ["code", "yoz", "dastur", "script"]):
        return "coder"
    return "END"</code></pre>
    </div>
  </div>

  <!-- 2-DARAJA: AMALIYOT -->
  <div class="task-card">
    <div class="task-header">
      <span class="task-badge tier-2" data-ru="2-Уровень: Проект (4 балла)" data-en="Tier 2: Project (4 pts)">2-Daraja: Amaliyot (4 ball)</span>
      <h3 style="margin:4px 0;" data-ru="Цикл Ремедиации: Coder + Reviewer" data-en="Remediation Loop: Coder + Reviewer">Tuzatish Zanjiri: Coder va Reviewer</h3>
    </div>
    <p style="font-size:13px; line-height:1.5; color:var(--ink-2);" data-ru="Напишите функцию узла <code>reviewer_node(state)</code>, которая проверяет код на наличие уязвимости (например, небезопасного <code>eval()</code>). Если уязвимость найдена, она ставит статус <code>status='NEEDS_FIX'</code> и возвращает на доработку Coder'у." data-en="Implement <code>reviewer_node(state)</code> which scans code artifacts for vulnerabilities (e.g. <code>eval()</code> calls). If found, it updates <code>status='NEEDS_FIX'</code> and routes back to Coder.">Kod ichida xavfli <code>eval()</code> yoki SQL inyeksiyani tekshiruvchi <code>reviewer_node(state)</code> funksiyasini yozing: xato bo'lsa <code>status='NEEDS_FIX'</code> qilib Coderga qaytarsin, toza bo'lsa <code>status='APPROVED'</code> bersin.</p>
    <textarea class="answer-area" id="ans_task_2" rows="8" placeholder="Reviewer kodini bu yerga yozing..." data-placeholder-ru="Напишите код ревьюера здесь..." data-placeholder-en="Write reviewer code here..." oninput="saveAnswers()"></textarea>
    <div class="teacher-sol" id="sol_task_2">
      <strong style="color:var(--accent);" data-ru="Эталонное решение:" data-en="Model Solution:">Oltin Yechim:</strong>
      <pre><code>def reviewer_node(state: dict) -> dict:
    code = state.get("code_artifact", "")
    critique = []
    if "eval(" in code or "exec(" in code:
        critique.append("RCE xavfi: eval() ishlatilgan!")
    if len(critique) > 0:
        return {
            "review_status": "NEEDS_FIX",
            "messages": state["messages"] + [f"Reviewer rad etdi: {', '.join(critique)}"],
            "next_step": "coder"
        }
    return {
        "review_status": "APPROVED",
        "messages": state["messages"] + ["Reviewer ma'qulladi: Kod xavfsiz."],
        "next_step": "supervisor"
    }</code></pre>
    </div>
  </div>

  <!-- 3-DARAJA: CHALLENGE -->
  <div class="task-card">
    <div class="task-header">
      <span class="task-badge tier-3" data-ru="3-Уровень: Challenge (2 балла)" data-en="Tier 3: Challenge (2 pts)">3-Daraja: Kiber-Challenge (2 ball)</span>
      <h3 style="margin:4px 0;" data-ru="Шлюз Человеческого Одобрения (Human-in-the-Loop)" data-en="Human-in-the-Loop Approval Gate">Inson Ruxsati (Human-in-the-Loop) Darvozasi</h3>
    </div>
    <p style="font-size:13px; line-height:1.5; color:var(--ink-2);" data-ru="Реализуйте функцию <code>human_approval_gate(state)</code>, которая приостанавливает выполнение графа, если Coder предлагает перезаписать файл базы данных, и требует явного флага <code>state['human_approved'] == True</code> для продолжения." data-en="Write <code>human_approval_gate(state)</code> which interrupts workflow execution if mutations target DB overwrites, strictly requiring <code>state['human_approved'] == True</code> to resume.">Agar Coder ma'lumotlar bazasini o'chirish yoki faylni almashtirish buyrug'ini bersa, grafigini to'xtatib, faqat <code>state['human_approved'] == True</code> bo'lgandagina davom etuvchi <code>human_approval_gate(state)</code> funksiyasini yozing.</p>
    <textarea class="answer-area" id="ans_task_3" rows="8" placeholder="Human-in-the-loop kodini bu yerga yozing..." data-placeholder-ru="Напишите код шлюза одобрения здесь..." data-placeholder-en="Write approval gate code here..." oninput="saveAnswers()"></textarea>
    <div class="teacher-sol" id="sol_task_3">
      <strong style="color:var(--purple);" data-ru="Эталонное решение:" data-en="Model Solution:">Oltin Yechim:</strong>
      <pre><code>def human_approval_gate(state: dict) -> str:
    critical_actions = ["DROP TABLE", "DELETE FROM", "rm -rf", "overwrite"]
    code = state.get("code_artifact", "")
    is_dangerous = any(action in code for action in critical_actions)

    if is_dangerous and not state.get("human_approved", False):
        print("⚠️ XAVFLI BUYRUQ ANIQLANDI! Inson roziligi kutilmoqda...")
        return "PAUSE_FOR_HUMAN"
    return "PROCEED_TO_DEPLOY"</code></pre>
    </div>
  </div>
    """

    tpl = tpl.replace("{{TASKS_CONTENT}}", tasks_html)
    out_path = os.path.join(DEST_DIR, "vazifa.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(tpl)
    print("  ✓ Created: vazifa.html")

# -----------------------------------------------------------------------------
# 4. TEACHER READING GUIDE (TEACHER_READING.md)
# -----------------------------------------------------------------------------
def build_teacher_reading():
    content = """# 10–11-sinf, 11-hafta, 28-dars: O'qituvchi Qo'llanmasi
## Multi-Agent Tizimlari: Supervisor va Worker Naqshlari (LangGraph)

### Dars Haqida Ma'lumot:
- **Kohorta:** 10–11-sinf (Senior AI & Enterprise Kiberxavfsizlik Track)
- **Format:** 40 daqiqalik Yakka Dars (Single Block)
- **Asosiy maqsad:** O'quvchilarga monolit agentlar cheklovlarini tushuntirish, mas'uliyatni ajratish (Separation of Concerns) orqali Supervisor va ixtisoslashgan Workerlar (Researcher, Coder, Reviewer) arxitekturasini o'rgatish, LangGraph StateGraph va conditional edges orqali xavfsiz marshrutlashni kodlash.

---

### 40 Daqiqalik Dars Pacing Xaritasi:

| Vaqt | Bosqich | Slayd | O'qituvchi Harakati | Kutiladigan Natija |
|---|---|:---:|---|---|
| **00:00–04:00** | Kirish va Maqsad | 1 | Dars mavzusini e'lon qilish, monolit vs multi-agent jamoalarini solishtirish. | O'quvchilar multi-agent zarurligini tushunishadi. |
| **04:00–08:00** | O'tgan Dars HW Tahlili | 2 | 27-darsdagi to'liq DB dump xatosini tahlil qilish. Blitz savol. | Nega semantik qidiruv kerakligi mustahkamlanadi. |
| **08:00–12:00** | Monolit Agent Muammosi | 3 | Diqqat chalkashishi (attention collapse) va ortiqcha vositalar oqibatlarini tushuntirish. | Mas'uliyatni ajratish tamoyili o'zlashtiriladi. |
| **12:00–16:00** | Supervisor-Worker Naqshi | 4 | Supervisor, Researcher, Coder, Reviewer rollarini doskada chizib ko'rsatish. | Rolli jamoa tuzilmasi tushuniladi. |
| **16:00–20:00** | LangGraph va StateGraph | 5 | Shared State, Nodes va Conditional Edges sintaksisini tahlil qilish. | Holat grafigi mantig'i o'rganiladi. |
| **20:00–24:00** | Deadlock va Kiberxavfsizlik | 6 | Max Iterations cheklovi va Human-in-the-Loop darvozasini tushuntirish. | Byudjet va xavfsizlik himoyasi anglanadi. |
| **24:00–28:00** | Jonli Smartboard Demo | 7 | Slayd ichidagi simulyatorda vazifani ishga tushirib, agentlar o'rtasida ma'lumot oqimini ko'rsatish. | Vizual idrok mustahkamlanadi. |
| **28:00–32:00** | Bilimni Sinash (Quiz) | 8 | 3 ta savol bo'yicha interaktiv viktorina o'tkazish. | O'quvchilar bilimi mustahkamlanadi. |
| **32:00–37:00** | 15 Daqiqalik Arena | 9 | `simulator/index.html` ilovasida o'quvchilarga o'z routerlarini kodlashni topshirish. | Har bir o'quvchi ishchi router yozadi. |
| **37:00–40:00** | Baholash va Ertangi Dars | 10 | 10 ballik mezonni e'lon qilish, 3 darajali uy vazifasini tushuntirish va ertangi 80 daqiqalik juftlik darsiga ko'prik. | Uy vazifasi tushuniladi. |

---

### Keng Tarqalgan Savollar va Pedagogik Ko'rsatmalar:
1. **"Nega LangGraph ishlatiladi, oddiy Python funksiyalari yetarli emasmi?"**
   - Javob: Oddiy Python funksiyalarida oraliq xatolik yuz bersa, agentning holati (state) yo'qoladi. LangGraph har bir qadamni xotirada saqlaydi, istalgan nuqtadan qayta tiklash (time-travel debugging) va inson ruxsatini (human-in-the-loop) ta'minlaydi.
2. **"Deadlock nima va undan qanday saqlaniladi?"**
   - Javob: Coder xato kod yozadi, Reviewer rad etadi; Coder yana tuzatib yuboradi, Reviewer yana rad etadi. Bu sikl cheksiz aylanib, barcha API pullarni tugatib yuborishi mumkin. Bunga qarshi `iterations >= 5` bo'lganda majburiy to'xtatish (circuit breaker) qo'yiladi.
"""
    out_path = os.path.join(DEST_DIR, "TEACHER_READING.md")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("  ✓ Created: TEACHER_READING.md")

# -----------------------------------------------------------------------------
# 5. STANDALONE SIMULATOR (simulator/index.html)
# -----------------------------------------------------------------------------
def build_simulator():
    sim_html = """<!DOCTYPE html>
<html lang="uz">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title data-ru="LangGraph Multi-Agent Студия — 10–11 Класс" data-en="LangGraph Multi-Agent Studio — Grade 10–11">LangGraph Multi-Agent Studiyasi — 10–11-Sinf</title>
  <link rel="stylesheet" href="../../../../assets/brand.css" />
  <style>
    :root {
      --bg: #090d16;
      --surface: #111827;
      --surface-2: #1f293d;
      --hair: #374151;
      --ink: #f3f4f6;
      --ink-2: #9ca3af;
      --accent: #3b82f6;
      --green: #10b981;
      --red: #ef4444;
      --purple: #8b5cf6;
      --amber: #f59e0b;
      --font-mono: 'JetBrains Mono', 'Fira Code', monospace;
    }
    body {
      margin: 0;
      padding: 20px;
      background: var(--bg);
      color: var(--ink);
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    }
    .header-bar {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 20px;
      padding-bottom: 12px;
      border-bottom: 1px solid var(--hair);
    }
    .btn {
      padding: 8px 16px;
      border-radius: 6px;
      border: 1px solid var(--hair);
      background: var(--surface-2);
      color: var(--ink);
      cursor: pointer;
      font-weight: 600;
      font-size: 13px;
      transition: all 0.15s ease;
    }
    .btn:hover:not(:disabled) { filter: brightness(1.1); }
    .btn:disabled { opacity: 0.5; cursor: not-allowed; }
    .btn-accent { background: var(--accent); color: #fff; border-color: var(--accent); }
    .grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 20px;
    }
    .card {
      background: var(--surface);
      border: 1px solid var(--hair);
      border-radius: 12px;
      padding: 16px;
      display: flex;
      flex-direction: column;
      gap: 12px;
    }
    .log-box {
      background: var(--surface-2);
      border: 1px solid var(--hair);
      border-radius: 8px;
      padding: 10px;
      font-family: var(--font-mono);
      font-size: 11px;
      height: 240px;
      overflow-y: auto;
      line-height: 1.5;
    }
    .node-item {
      padding: 8px 12px;
      border-radius: 6px;
      border: 1px solid var(--hair);
      background: var(--surface-2);
      font-size: 12px;
      font-family: var(--font-mono);
      display: flex;
      justify-content: space-between;
      align-items: center;
      transition: all 0.2s ease;
    }
    .node-item.active {
      border-color: var(--accent);
      background: rgba(59,130,246,0.15);
      color: #fff;
    }
    .lang-btn {
      padding: 4px 10px;
      border-radius: 6px;
      background: transparent;
      border: 1px solid var(--hair);
      color: var(--ink-2);
      font-size: 12px;
      cursor: pointer;
    }
    .lang-btn.active {
      background: var(--accent);
      color: #fff;
      border-color: var(--accent);
    }
  </style>
</head>
<body>

  <div class="header-bar">
    <div>
      <h2 style="margin:0 0 4px 0;" data-ru="LangGraph Multi-Agent Студия" data-en="LangGraph Multi-Agent Studio">LangGraph Multi-Agent Kiber-Studiyasi</h2>
      <span style="font-size:12px; color:var(--ink-2);" data-ru="10–11-Класс · 11-Неделя · 28-Урок · Supervisor, Researcher, Coder и Reviewer" data-en="Grades 10–11 · Week 11 · Lesson 28 · Supervisor, Researcher, Coder & Reviewer">10–11-Sinf · 11-Hafta · 28-Dars · Supervisor, Researcher, Coder va Reviewer arxitekturasi</span>
    </div>
    <div style="display:flex; gap:10px; align-items:center;">
      <div style="display:flex; gap:4px;">
        <button class="lang-btn active" onclick="setLang('uz')">UZ</button>
        <button class="lang-btn" onclick="setLang('ru')">RU</button>
        <button class="lang-btn" onclick="setLang('en')">EN</button>
      </div>
    </div>
  </div>

  <div style="margin-bottom:16px; display:flex; gap:10px; align-items:center;">
    <button class="btn btn-accent" id="btnRunWorkflow" onclick="runWorkflow()" data-ru="⚡ Запустить Оркестрацию Задачи" data-en="⚡ Run Multi-Agent Workflow">⚡ Vazifani Ishga Tushirish</button>
    <button class="btn" onclick="resetStudio()" data-ru="🔄 Сброс" data-en="🔄 Reset">🔄 Qayta O'rnatish</button>
    <span style="font-size:12px; color:var(--ink-2); margin-left:auto; font-family:var(--font-mono);">
      Sikl: <strong id="statIters" style="color:var(--green);">0 / 5</strong> | Holat: <strong id="statStatus" style="color:var(--accent);">IDLE</strong>
    </span>
  </div>

  <div class="grid">
    <!-- GRAPH NODES -->
    <div class="card">
      <h3 style="margin:0;" data-ru="Граф Состояний (StateGraph)" data-en="StateGraph Nodes">StateGraph Tugunlari</h3>
      <div style="display:flex; flex-direction:column; gap:8px;">
        <div class="node-item" id="sim_sup">
          <span>👑 <strong>Supervisor</strong> (Router & Planner)</span>
          <span style="font-size:11px; color:var(--accent);">Decision Node</span>
        </div>
        <div class="node-item" id="sim_res">
          <span>🔍 <strong>Researcher</strong> (Web & Docs API)</span>
          <span style="font-size:11px; color:var(--purple);">Knowledge Worker</span>
        </div>
        <div class="node-item" id="sim_cod">
          <span>💻 <strong>Coder</strong> (Clean Code Synthesis)</span>
          <span style="font-size:11px; color:var(--green);">Implementation Worker</span>
        </div>
        <div class="node-item" id="sim_rev">
          <span>🛡️ <strong>Reviewer</strong> (OWASP & QA Audit)</span>
          <span style="font-size:11px; color:var(--amber);">Security Gate</span>
        </div>
      </div>

      <div style="margin-top:auto; background:var(--surface-2); padding:10px; border-radius:8px; font-size:12px; line-height:1.5; color:var(--ink-2);">
        <strong style="color:var(--ink);" data-ru="Текущий Артефакт:" data-en="Current Artifact:">Yaratilgan Artifakt:</strong><br>
        <code id="simArtifactCode" style="color:var(--green); font-size:11px;">// Hali kod yaratilmadi...</code>
      </div>
    </div>

    <!-- LOGS & TRACE -->
    <div class="card">
      <h3 style="margin:0;" data-ru="Трассировка Сообщений (State Trace)" data-en="State Execution Trace">Xabarlar va Davlat Jurnali (State Trace)</h3>
      <div class="log-box" id="simLogs">
        <div style="color:var(--ink-2);" data-ru="• Нажмите «Запустить Оркестрацию» для старта миссии..." data-en="• Click 'Run Multi-Agent Workflow' to initiate...">• Boshlash tugmasini bosing...</div>
      </div>
      <div style="display:flex; justify-content:space-between; font-size:11px; color:var(--ink-2); font-family:var(--font-mono);">
        <span>Circuit Breaker: Max 5 iters</span>
        <span style="color:var(--green);">HITL: ACTIVE</span>
      </div>
    </div>
  </div>

  <script>
    var currentLang = 'uz';
    var iterations = 0;
    var running = false;

    function setLang(lang) {
      currentLang = lang;
      document.querySelectorAll('.lang-btn').forEach(function(b) {
        b.classList.toggle('active', b.textContent.toLowerCase() === lang);
      });
      document.querySelectorAll('[data-' + lang + ']').forEach(function(el) {
        el.textContent = el.getAttribute('data-' + lang);
      });
    }

    function appendLog(msg, color) {
      var box = document.getElementById('simLogs');
      var row = document.createElement('div');
      row.style.color = color || 'var(--ink)';
      row.style.margin = '2px 0';
      row.textContent = '• ' + msg;
      box.appendChild(row);
      box.scrollTop = box.scrollHeight;
    }

    function setActiveNode(nodeId) {
      ['sim_sup', 'sim_res', 'sim_cod', 'sim_rev'].forEach(function(id) {
        var el = document.getElementById(id);
        if (id === nodeId) el.classList.add('active');
        else el.classList.remove('active');
      });
    }

    function runWorkflow() {
      if (running) return;
      running = true;
      document.getElementById('btnRunWorkflow').disabled = true;
      document.getElementById('statStatus').textContent = 'RUNNING';

      iterations = 1;
      document.getElementById('statIters').textContent = iterations + ' / 5';
      setActiveNode('sim_sup');
      appendLog('Foydalanuvchi talabi: "Redis Cache bilan ishlovchi Rate Limiter yozilsin"', 'var(--ink)');
      appendLog('👑 Supervisor: Talab o‘rganildi. 1-bosqich: Token Bucket algoritmi bo‘yicha spetsifikatsiya kerak.', 'var(--accent)');

      setTimeout(stepResearcher, 900);
    }

    function stepResearcher() {
      setActiveNode('sim_res');
      appendLog('🔍 Researcher: Redis EVAL Lua script va Token Bucket formula hujjatlari yuklandi.', 'var(--purple)');
      setTimeout(stepCoder, 1000);
    }

    function stepCoder() {
      setActiveNode('sim_cod');
      appendLog('💻 Coder: rateLimiter.js moduli yozildi (Redis INCR + EXPIRE).', 'var(--green)');
      document.getElementById('simArtifactCode').textContent = 'export async function checkRateLimit(key, max, windowSec)...';
      setTimeout(stepReviewer, 1000);
    }

    function stepReviewer() {
      setActiveNode('sim_rev');
      appendLog('🛡️ Reviewer: Kod tekshirildi. Race condition xavfi yo‘q, Atomic Lua ishlatilgan. Status: APPROVED ✅', 'var(--green)');
      setTimeout(stepFinish, 900);
    }

    function stepFinish() {
      setActiveNode('sim_sup');
      document.getElementById('statStatus').textContent = 'COMPLETED';
      appendLog('👑 Supervisor: Jamoa vazifani muvaffaqiyatli yakunladi. Natija foydalanuvchiga taqdim etildi!', 'var(--accent)');
      running = false;
      document.getElementById('btnRunWorkflow').disabled = false;
    }

    function resetStudio() {
      running = false;
      iterations = 0;
      document.getElementById('statIters').textContent = '0 / 5';
      document.getElementById('statStatus').textContent = 'IDLE';
      setActiveNode(null);
      document.getElementById('simLogs').innerHTML = '<div style="color:var(--ink-2);">• Qayta ishga tushirildi...</div>';
      document.getElementById('simArtifactCode').textContent = '// Hali kod yaratilmadi...';
      document.getElementById('btnRunWorkflow').disabled = false;
    }
  </script>
</body>
</html>
"""
    out_path = os.path.join(DEST_DIR, "simulator", "index.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(sim_html)
    print("  ✓ Created: simulator/index.html")

def main():
    print("📦 Building 10–11-sinf (Lesson 28: Multi-Agent Tizimlari)...")
    build_presentation()
    build_worksheet()
    build_homework()
    build_teacher_reading()
    build_simulator()
    print("🎉 Done! Generated Grade 10–11 Lesson 28.")

if __name__ == "__main__":
    main()
