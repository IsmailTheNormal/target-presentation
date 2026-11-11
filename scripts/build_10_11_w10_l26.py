#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
scripts/build_10_11_w10_l26.py — 10–11-sinf (10-hafta 26-dars)
Mavzu: Agentik Tool Calling, Funksiyalar va Xavfsiz Sandboxing
Track: Senior AI & Enterprise Kiberxavfsizlik Track
Duration: 80 daqiqa (Double block / 2-hour class)
"""

import os
import sys
import json
import re
import subprocess

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
LESSON_DIR = os.path.join(REPO_ROOT, "classes", "10-11-sinf", "10-hafta", "26-dars-agentik-tool-calling-va-funksiyalar")
SIM_DIR = os.path.join(LESSON_DIR, "simulator")
os.makedirs(SIM_DIR, exist_ok=True)

with open(os.path.join(REPO_ROOT, "assets", "TEMPLATE_PREZENTATSIYA.html"), "r", encoding="utf-8") as f:
    TPL_PRES = f.read()

with open(os.path.join(REPO_ROOT, "assets", "TEMPLATE_VARAQA.html"), "r", encoding="utf-8") as f:
    TPL_VAR = f.read()

with open(os.path.join(REPO_ROOT, "assets", "TEMPLATE_VAZIFA.html"), "r", encoding="utf-8") as f:
    TPL_VAZ = f.read()

def build_10_11_lesson():
    print("📦 Generating 10–11-sinf (26-dars: Agentik Tool Calling va Funksiyalar)...")

    title_uz = "26-dars: Agentik Tool Calling, Funksiyalar va Xavfsiz Sandboxing"
    title_ru = "Урок 26: Агентный Tool Calling, Функции и Безопасный Sandboxing"
    title_en = "Lesson 26: Agentic Tool Calling, Function Actuators & Safe Sandboxing"

    # 1. PREZENTATSIYA
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
    <div class="eyebrow" data-ru="10–11-СИНФ · 10-Я НЕДЕЛЯ · УРОК 26" data-en="GRADES 10–11 · WEEK 10 · LESSON 26">10–11-SINF · 10-HAFTA · 26-DARS</div>
    <h1 data-ru="Агентный Tool Calling, Функции и Sandboxing" data-en="Agentic Tool Calling, Function Actuators & Safe Sandboxing">Agentik Tool Calling, Funksiyalar va Xavfsiz Sandboxing</h1>
    <p class="lede" data-ru="Даем языковой модели 'руки': протокол вызова инструментов (JSON Schema), выполнение в изолированном песочнике (Sandboxing) и защита от RCE-инъекций." data-en="Equipping LLMs with actuators: declarative JSON Schema tool specs, sandboxed runtime execution, and hardening against Remote Code Execution (RCE).">Til modeliga 'qo'l' beramiz: tashqi asboblar protokoli (JSON Schema), ajratilgan muhitda xavfsiz kod bajarish (Sandboxing) va RCE hujumlaridan himoyalanish.</p>
    <div class="grid c3" style="margin-top:24px;">
      <div class="card">
        <h3 data-ru="Формат урока" data-en="Lesson Format">Format va Davomiylik</h3>
        <p data-ru="Спаренный блок: 2 x 40 минут = 80 минут Senior AI-инженерии" data-en="Double block: 2 x 40 min = 80 min Senior AI engineering">Juftlik blok: 2 x 40 daqiqa = 80 daqiqalik Senior AI muhandislik amaliyoti</p>
      </div>
      <div class="card">
        <h3 data-ru="Главная миссия" data-en="Core Mission">Amaliy Missiya</h3>
        <p data-ru="Спроектировать схему вызова калькулятора, API и изолировать их в песочнице" data-en="Design declarative tool schemas for calculator/APIs and sandbox execution">Kalkulyator, SQL va API vositalari uchun JSON Schema yozish va xavfsiz bajarish</p>
      </div>
      <div class="card">
        <h3 data-ru="10-Балльная система" data-en="10-Point Rubric">Baholash Mezoni</h3>
        <p data-ru="4 балла: Схема · 4 балла: Валидация типов · 2 балла: Защита от RCE" data-en="4 pts: Schema · 4 pts: Type validation · 2 pts: RCE isolation">4 ball: Sxema · 4 ball: Validatsiya · 2 ball: RCE izolyatsiyasi</p>
      </div>
    </div>
  </section>""")

    # Slide 2: HW Review (25-dars ReAct)
    slides.append("""  <!-- SLIDE 2: MANDATORY HW REVIEW & BRIDGE -->
  <section class="slide" data-phase="Uy Vazifasi Tahlili|Разбор Д/З|HW Review" data-time="04:00–10:00">
    <div class="eyebrow" data-ru="АНАЛИЗ Д/З · РАЗБОР ОШИБОК 25-УРОКА" data-en="HOMEWORK AUDIT · LESSON 25 PITFALLS">UY VAZIFASI TAHLILI · 25-DARS XATOLAR REVIZIYASI</div>
    <h2 data-ru="Разбор Домашнего Задания: Бесконечные Циклы в ReAct" data-en="Homework Autopsy: Infinite Loops in ReAct Cycles">O'tgan Dars Vazifasi Tahlili: ReAct Tsiklida Cheksiz Aylanish</h2>
    <div class="grid c2" style="margin-top:16px;">
      <div class="card" style="border-left:4px solid var(--accent);">
        <span class="pill" style="color:var(--accent-ink);" data-ru="Типичная ошибка" data-en="Common Pitfall">Xato Tahlili (Pitfall)</span>
        <h3 data-ru="Отсутствие лимита шагов и зацикливание агента" data-en="Missing step bounds and agent spin-locks">Maksimal qadamlar (max_iterations) chegarasi yo'qligi</h3>
        <p data-ru="Агент получал неожиданный ответ инструмента и уходил в бесконечный цикл Thought ➔ Action, сжигая миллионы токенов и зависая намертво." data-en="When an actuator returned an anomaly, agents entered runaway Thought ➔ Action loops, burning millions of tokens and exhausting API quotas.">Vosita xato qaytarganda agent nima qilishni bilmay, cheksiz aylanib qolgan va millionlab tokenlarni behuda sarflagan.</p>
        <pre class="code-snippet" style="margin-top:8px;"><code>// ❌ Xato:
while (!done) { // Cheksiz tsikl xavfi!
  step = agent.think();
}</code></pre>
      </div>
      <div class="card" style="border-left:4px solid var(--green);">
        <span class="pill" style="color:var(--green);" data-ru="Золотой стандарт" data-en="Golden Standard">Oltin Yechim (Best Practice)</span>
        <h3 data-ru="Детерминированный Loop Guard и Human-in-the-Loop" data-en="Deterministic Loop Guards & Human Approval">Loop Guard va inson nazorati (HITL)</h3>
        <p data-ru="Строгий счетчик итераций (max_iterations: 5) и аварийный выход при повторении одинаковых действий защищают продакшн от сбоев." data-en="Hardcoded step quotas (max_iterations: 5) coupled with cycle-detection guards guarantee safe production fallback.">Qat'iy `max_iterations = 5` chegarasi, bir xil harakat takrorlanganda to'xtash va inson roziligini so'rash mexanizmi.</p>
        <pre class="code-snippet" style="margin-top:8px;"><code>// ✅ To'g'ri:
if (iterations++ >= MAX_STEPS) {
  return fallbackHumanApproval();
}</code></pre>
      </div>
    </div>
    <div class="grid c2" style="margin-top:16px;">
      <div class="card">
        <span class="pill" data-ru="Блиц-контроль (30 сек)" data-en="30s Blitz Check">30s Blits-Nazorat</span>
        <p data-ru="Каковы 3 обязательные фазы архитектуры ReAct? Ответ: Thought (Мысль) ➔ Action (Действие) ➔ Observation (Наблюдение)!" data-en="What are the 3 mandatory phases of ReAct? Answer: Thought ➔ Action ➔ Observation!">ReAct tsiklining 3 ta majburiy bosqichi nima? Javob: <b>Thought (Fikr)</b> ➔ <b>Action (Harakat)</b> ➔ <b>Observation (Kuzatuv)</b>!</p>
      </div>
      <div class="card">
        <span class="pill" data-ru="Мост к новому уроку" data-en="Bridge to Topic">Bugungi Darsga Ko'prik</span>
        <p data-ru="На прошлом уроке мы изучили логику мысли агента. Но как именно Action превращается в реальное действие? Сегодня мы подключаем Function Calling!" data-en="Last lesson we mastered agent cognition. But how does an Action translate into reality? Today we build production Tool Calling actuators!">O'tgan darsda agentning fikrlash tsiklini qurdik. Ammo 'Action' qanday qilib real dunyodagi amallarni bajaradi? Bugun Tool Calling mexanizmini ulaymiz!</p>
      </div>
    </div>
  </section>""")

    # Slide 3: Parametric Knowledge vs Ground Truth
    slides.append("""  <!-- SLIDE 3: WHY TOOL CALLING -->
  <section class="slide" data-phase="Muammo|Проблема|Problem" data-time="10:00–16:00">
    <div class="eyebrow" data-ru="ПАРАМЕТРИЧЕСКАЯ ПАМЯТЬ VS ФАКТЫ" data-en="PARAMETRIC MEMORY VS GROUND TRUTH">PARAMETRIK XOTIRA VA REAL DUNYO</div>
    <h2 data-ru="Почему LLM Нужны Инструменты: Границы Модели" data-en="Why LLMs Need Tools: Fundamental Model Limitations">Nega LLM Modeliga Tashqi Asboblar (Tools) Kerak?</h2>
    <p class="lede" data-ru="Языковая модель знает только то, на чем обучалась в прошлом. Она не умеет точно считать длинные числа и не видит текущие данные." data-en="LLMs only reflect static pre-training weights. They hallucinate high-precision math, cannot query live databases, and cannot execute system tasks.">Til modellari faqat o'tmishdagi matnlarni biladi. Ular aniq arifmetikada yanglishadi, joriy valyuta kursini bilmaydi va fayllarni mustaqil ocholmaydi.</p>
    <div class="grid c3" style="margin-top:20px;">
      <div class="card">
        <span class="pill" style="color:var(--accent-ink);" data-ru="Слабость 1: Арифметика" data-en="Flaw 1: Arithmetic">Zaiflik 1: Arifmetika</span>
        <h3 data-ru="Галлюцинации в расчетах" data-en="Arithmetic Hallucinations">Katta Hisoblarda Xatolar</h3>
        <p data-ru="LLM угадывает следующее слово, а не вычисляет. '18492 * 9281' выдаст неверную цифру." data-en="LLMs predict token probabilities rather than performing ALU computations. Complex multiplications hallucinate.">Model hisoblamaydi, ehtimollik bo'yicha keyingi so'zni topadi. Katta raqamlarni noto'g'ri ko'paytiradi.</p>
      </div>
      <div class="card">
        <span class="pill" style="color:var(--accent-ink);" data-ru="Слабость 2: Данные" data-en="Flaw 2: Live Data">Zaiflik 2: Jonli Ma'lumot</span>
        <h3 data-ru="Застывшее время (Cutoff)" data-en="Knowledge Cutoff Horizon">Eskirgan Ma'lumotlar</h3>
        <p data-ru="Модель не знает погоду за окном прямо сейчас и не имеет доступа к вашей базе данных." data-en="Models cannot inspect today's live stock prices or read private corporate SQLite schemas without tools.">Hozirgi ob-havo, Toshkent birjasi yoki korxonangiz bazasidagi qoldiqlarni model o'zidan o'zi bilmaydi.</p>
      </div>
      <div class="card" style="border:2px solid var(--green);">
        <span class="pill" style="color:var(--green);" data-ru="Решение: Инструменты" data-en="Solution: Tools">Yechim: Asboblar (Tools)</span>
        <h3 data-ru="Актаторы и функции" data-en="Function Actuators">Tool Calling Qalqoni</h3>
        <p data-ru="Модель генерирует строгий JSON-вызов, сервер запускает функцию и возвращает точный факт!" data-en="The LLM emits a declarative JSON call; your deterministic runtime executes it and feeds facts back!">Model JSON buyruq yozadi, server kalkulyator yoki API ni ishlatib, aniq natijani qaytaradi!</p>
      </div>
    </div>
  </section>""")

    # Slide 4: Tool Calling Pipeline
    slides.append("""  <!-- SLIDE 4: TOOL CALLING PIPELINE -->
  <section class="slide" data-phase="Arxitektura|Архитектура|Architecture" data-time="16:00–22:00">
    <div class="eyebrow" data-ru="ПРОТОКОЛ ВЫЗОВА ИНСТРУМЕНТОВ" data-en="TOOL CALLING PIPELINE PROTOCOL">TOOL CALLING PROTOKOLI VA BOSQICHLAR</div>
    <h2 data-ru="Как Работает Tool Calling: 4 Шага Конвейера" data-en="The 4-Step Tool Calling Invocation Pipeline">Tool Calling Qanday Ishlaydi: 4 Bosqichli Konveyer</h2>
    <p class="lede" data-ru="Модель сама НЕ выполняет код. Она выступает диспетчером, выбирая инструмент и формируя валидный JSON." data-en="The LLM does NOT execute code directly. It acts as an orchestrator, selecting the tool and drafting valid JSON payload arguments.">Model o'zidan o'zi kodni ishga tushirmaydi! U faqat qaysi vosita kerakligini va unga qanday JSON argument berishni hal qiladi.</p>
    <div style="margin:20px 0; overflow-x:auto;">
      <svg viewBox="0 0 740 180" style="width:100%; max-width:740px; height:auto; display:block; margin:0 auto;">
        <defs>
          <marker id="arrow10" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
            <path d="M 0 1 L 8 5 L 0 9 z" fill="var(--accent)" />
          </marker>
        </defs>
        <rect x="10" y="20" width="160" height="140" rx="8" fill="var(--panel)" stroke="var(--rule)" stroke-width="1.5" />
        <text x="90" y="50" fill="var(--accent)" font-family="'Manrope', sans-serif" font-weight="800" font-size="12" text-anchor="middle" data-ru="1. ПРОМПТ + ИНСТРУМЕНТЫ" data-en="1. PROMPT + TOOLS">1. PROMPT + TOOLS</text>
        <text x="90" y="80" fill="var(--ink-2)" font-size="11" text-anchor="middle" data-ru="Запрос пользователя" data-en="User query">Foydalanuvchi savoli</text>
        <text x="90" y="100" fill="var(--ink-3)" font-size="9.5" text-anchor="middle" data-ru="+ JSON Schema схема" data-en="+ JSON Schema specs">+ JSON Schema ta'rifi</text>

        <path d="M 175 90 L 205 90" stroke="var(--accent)" stroke-width="2.5" marker-end="url(#arrow10)" />

        <rect x="210" y="20" width="160" height="140" rx="8" fill="var(--panel)" stroke="var(--accent)" stroke-width="2" />
        <text x="290" y="50" fill="var(--accent)" font-family="'Manrope', sans-serif" font-weight="800" font-size="12" text-anchor="middle" data-ru="2. ВЫЗОВ (JSON)" data-en="2. TOOL CALL JSON">2. TOOL CALL JSON</text>
        <text x="290" y="80" fill="var(--ink-2)" font-size="11" text-anchor="middle" data-ru="Решение LLM:" data-en="LLM decision:">LLM qarori:</text>
        <text x="290" y="100" fill="var(--ink-3)" font-family="'JetBrains Mono', monospace" font-size="9.5" text-anchor="middle" data-ru='name: "calculator"' data-en='name: "calculator"'>name: "calculator"</text>
        <text x="290" y="115" fill="var(--ink-3)" font-family="'JetBrains Mono', monospace" font-size="9.5" text-anchor="middle" data-ru='args: {"expr":"12*8"}' data-en='args: {"expr":"12*8"}'>args: {"expr":"12*8"}</text>

        <path d="M 375 90 L 405 90" stroke="var(--accent)" stroke-width="2.5" marker-end="url(#arrow10)" />

        <rect x="410" y="20" width="150" height="140" rx="8" fill="var(--panel)" stroke="var(--rule)" stroke-width="1.5" />
        <text x="485" y="50" fill="var(--green)" font-family="'Manrope', sans-serif" font-weight="800" font-size="12" text-anchor="middle" data-ru="3. ПЕСОЧНИЦА (EXEC)" data-en="3. SANDBOX EXEC">3. SANDBOX EXEC</text>
        <text x="485" y="80" fill="var(--ink-2)" font-size="11" text-anchor="middle" data-ru="Сервер исполняет" data-en="Server executes">Server funksiyani</text>
        <text x="485" y="100" fill="var(--ink-2)" font-size="11" text-anchor="middle" data-ru="в изоляции" data-en="in isolated sandbox">izolyatsiyada bajaradi</text>
        <text x="485" y="125" fill="var(--green)" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="700" text-anchor="middle" data-ru="Результат: 96" data-en="Result: 96">Natija: 96</text>

        <path d="M 565 90 L 595 90" stroke="var(--accent)" stroke-width="2.5" marker-end="url(#arrow10)" />

        <rect x="600" y="20" width="130" height="140" rx="8" fill="var(--panel)" stroke="var(--rule)" stroke-width="1.5" />
        <text x="665" y="50" fill="var(--accent)" font-family="'Manrope', sans-serif" font-weight="800" font-size="12" text-anchor="middle" data-ru="4. ОТВЕТ" data-en="4. RESPONSE">4. JAVOB</text>
        <text x="665" y="80" fill="var(--ink-2)" font-size="11" text-anchor="middle" data-ru="Observation (Факт)" data-en="Observation (Fact)">Observation</text>
        <text x="665" y="100" fill="var(--ink-2)" font-size="11" text-anchor="middle" data-ru="возврат в модель" data-en="returns to model">modelga qaytadi</text>
        <text x="665" y="125" fill="var(--accent)" font-size="10.5" font-weight="700" text-anchor="middle" data-ru="Итоговый синтез" data-en="Final synthesis">Yakuniy tahlil</text>
      </svg>
    </div>
  </section>""")

    # Slide 5: Interactive Slide — Live Tool Calling Simulator
    slides.append("""  <!-- SLIDE 5: INTERACTIVE TOOL CALLING SIMULATOR -->
  <section class="slide" data-phase="Jonli Sinov|Живой Тест|Live Demo" data-time="22:00–30:00">
    <div class="eyebrow" data-ru="ИНТЕРАКТИВНЫЙ СИМУЛЯТОР FUNCTION CALLING" data-en="INTERACTIVE TOOL CALLING ACTUATOR">INTERAKTIV TOOL CALLING LABORATORIYASI</div>
    <h2 data-ru="Симулятор Вызова Инструментов: Нажимайте Кнопки на Смартборде!" data-en="Live Tool Invocation: Tap Actuators on Smartboard!">Jonli Sinov: Asboblarni Chaqiring va Natijani Kuzating!</h2>
    <p class="lede" data-ru="Выберите задачу, чтобы увидеть, как модель генерирует структурированный JSON, а песочница возвращает факт." data-en="Select an operational query to trace declarative JSON generation, validation, and sandbox execution.">Smartboardda so'rovni tanlang: model qanday JSON argument yaratishi va sandbox qanday fakt qaytarishini ko'ring:</p>

    <div class="grid c2" style="margin-top:14px; align-items:flex-start;">
      <!-- Left: JSON Schema & Output -->
      <div class="card" style="padding:14px;">
        <span class="pill" id="simToolName" data-ru="Инструмент: calculate" data-en="Tool: calculate">Asbob: kalkulyator</span>
        <pre class="code-snippet" id="simJsonPayload" style="margin-top:8px; font-size:11px; max-height:160px; overflow-y:auto;"><code>{
  "name": "calculate",
  "arguments": {
    "expression": "48 * 125 + 720"
  }
}</code></pre>
        <div style="margin-top:8px; padding:8px; background:rgba(16,185,129,0.08); border-left:3px solid var(--green); border-radius:4px;">
          <div style="font-size:11px; font-weight:800; color:var(--green);" data-ru="Результат песочницы (Observation):" data-en="Sandbox Observation:">Sandbox Natijasi (Observation):</div>
          <div id="simObservationText" style="font-family:'JetBrains Mono', monospace; font-size:12px; margin-top:2px;">6720</div>
        </div>
      </div>

      <!-- Right: Presets -->
      <div style="display:flex; flex-direction:column; gap:8px;">
        <button type="button" class="dock-btn" onclick="runSimTool('calc')" style="text-align:left; padding:8px 12px; font-size:12px; border:1px solid var(--rule);" data-ru="🧮 1. «Вычислить: 48 * 125 + 720»" data-en="🧮 1. 'Calculate: 48 * 125 + 720'">🧮 1. «Hisobla: 48 * 125 + 720»</button>
        <button type="button" class="dock-btn" onclick="runSimTool('weather')" style="text-align:left; padding:8px 12px; font-size:12px; border:1px solid var(--rule);" data-ru="🌤️ 2. «Какая погода в Ташкенте?»" data-en="🌤️ 2. 'Weather in Tashkent?'">🌤️ 2. «Toshkentda ob-havo qanday?»</button>
        <button type="button" class="dock-btn" onclick="runSimTool('sql')" style="text-align:left; padding:8px 12px; font-size:12px; border:1px solid var(--rule);" data-ru="🗄️ 3. «Найти остаток товара SKU-902»" data-en="🗄️ 3. 'Query inventory for SKU-902'">🗄️ 3. «SKU-902 tovar qoldig'ini top»</button>
        <button type="button" class="dock-btn" onclick="runSimTool('bash')" style="text-align:left; padding:8px 12px; font-size:12px; border:1px solid rgba(255,17,0,0.3); color:var(--accent);" data-ru="⚠️ 4. «Опасный вызов: rm -rf /»" data-en="⚠️ 4. 'Dangerous Exec: rm -rf /'">⚠️ 4. «Xavfli Buyruq: rm -rf /»</button>
      </div>
    </div>
  </section>""")

    # Slide 6: JSON Schema Standard
    slides.append("""  <!-- SLIDE 6: JSON SCHEMA SPEC -->
  <section class="slide" data-phase="Standart|Стандарт|Standard" data-time="30:00–36:00">
    <div class="eyebrow" data-ru="ДЕКЛАРАЦИЯ ИНСТРУМЕНТОВ · JSON SCHEMA" data-en="TOOL DECLARATIONS · JSON SCHEMA">ASBOBLAR TAVSIFI · JSON SCHEMA STANDARTI</div>
    <h2 data-ru="Как Описать Инструмент для Модели: JSON Schema" data-en="Describing Actuators to LLMs: Declarative JSON Schema">Model Asbobni Qayerdan Biladi: JSON Schema</h2>
    <p class="lede" data-ru="Каждый инструмент описывается строгой схемой: имя, текстовое описание (критично для роутинга!), параметры и обязательные поля." data-en="Actuators require rigorous declarative specs: exact name, semantic description, strongly typed parameter trees, and required properties.">Model vositani to'g'ri tanlashi uchun unga aniq JSON Schema beriladi: nomi, maqsadi (description o'ta muhim!), parametrlari va turlari.</p>
    <div class="grid c2" style="margin-top:16px;">
      <div class="card">
        <h3 data-ru="Каноническая схема OpenAI / Anthropic" data-en="Standard Tool Definition">Kanonik Tool Sxemasi</h3>
        <pre class="code-snippet"><code>{
  "name": "get_stock_price",
  "description": "Berilgan aksiya belgisi (ticker) bo'yicha jonli narxni oladi",
  "parameters": {
    "type": "object",
    "properties": {
      "ticker": { "type": "string", "description": "AAPL, TSLA, MSFT" }
    },
    "required": ["ticker"]
  }
}</code></pre>
      </div>
      <div class="card">
        <h3 data-ru="Ключевые требования к описанию" data-en="Crucial Spec Guidelines">Sxema Bo'yicha Oltin Qoidalar</h3>
        <ul style="margin-top:8px; line-height:1.7; padding-left:18px;">
          <li data-ru="Description — это промпт для выбора инструмента!" data-en="Description directs the LLM's routing heuristics!"><b>Description</b> — model aynan qachon bu asbobni ishlatishini tushuntiradi.</li>
          <li data-ru="required — гарантирует, что аргумент не будет пропущен." data-en="required prevents missing parameter runtime bugs."><b>required</b> — argument tashlab ketilmasligini kafolatlaydi.</li>
          <li data-ru="Строгие типы: string, number, boolean, array." data-en="Strong typing: string, number, boolean, array."><b>type</b> — noto'g'ri formatdagi ma'lumotlarni bloklaydi.</li>
        </ul>
      </div>
    </div>
  </section>""")

    # Slide 7: Argument Validation
    slides.append("""  <!-- SLIDE 7: ARGUMENT VALIDATION -->
  <section class="slide" data-phase="Validatsiya|Валидация|Validation" data-time="36:00–42:00">
    <div class="eyebrow" data-ru="ЗАЩИТА ВХОДНЫХ ДАННЫХ · PYDANTIC И ZOD" data-en="TYPE SAFETY & VALIDATION GUARDS">MA'LUMOTLAR HAVFSIZLIGI · ARGUMENTLAR VALIDATSIYASI</div>
    <h2 data-ru="Валидация Аргументов: Доверяй, Но Проверяй!" data-en="Validating Arguments: Never Trust Raw LLM Payloads!">Argumentlarni Tekshirish: Hech Qachon Xom JSONga Ishonmang!</h2>
    <p class="lede" data-ru="Языковая модель может передать строку вместо числа или null. Без строгой схемы Pydantic сервер упадет с ошибкой 500." data-en="LLMs frequently emit stringified numbers or invalid nulls. Without explicit schema validators, backends crash with uncaught 500s.">Model ba'zan raqam o'rniga so'z yozishi yoki kutilmagan null berishi mumkin. Server qulab tushmasligi uchun Zod yoki Pydantic bilan tekshiramiz.</p>
    <div class="grid c2" style="margin-top:16px;">
      <div class="card">
        <h3 data-ru="Слой валидации на сервере" data-en="Backend Validation Layer">Validatsiya Qatlami</h3>
        <pre class="code-snippet"><code>function executeTool(name, rawArgs) {
  // 1. JSON parse xavfsizligi
  const args = JSON.parse(rawArgs);

  // 2. Majburiy parametrlar tekshiruvi
  if (!args.ticker || typeof args.ticker !== 'string') {
    throw new Error("Invalid parameter: ticker is required string!");
  }
  
  return fetchTickerPrice(args.ticker.toUpperCase());
}</code></pre>
      </div>
      <div class="card">
        <h3 data-ru="Что делать при ошибке валидации?" data-en="Error Feedback Loop">Xato Chiqsa Nima Qilish Kerak?</h3>
        <p data-ru="Не роняйте сервер! Верните ошибку в модель в блоке Observation. LLM прочитает замечание и САМА исправит аргументы со второй попытки!" data-en="Never crash the host! Return the schema error back into the LLM's Observation window. It will auto-correct its payload!">Serverni o'chirib qo'ymang! Xatolik matnini Observation orqali modelga qaytaring. Model xatosini tushunib, 2-urinishda to'g'rilab yuboradi!</p>
      </div>
    </div>
  </section>""")

    # Slide 8: Sandboxing & RCE Isolation
    slides.append("""  <!-- SLIDE 8: SANDBOXING -->
  <section class="slide" data-phase="Kiberxavfsizlik|Безопасность|Security" data-time="42:00–48:00">
    <div class="eyebrow" data-ru="ИЗОЛЯЦИЯ ПЕСОЧНИЦЫ · ЗАЩИТА ОТ RCE" data-en="SANDBOX ISOLATION · RCE DEFENSE">KIBER-HIMOYA · XAVFSIZ SANDBOXING</div>
    <h2 data-ru="Песочницы: Как Защитить Сервер от 'Злых' Команд" data-en="Sandboxing: Shielding Systems from Malicious Commands">Sandboxing: Serverni Xavfli Buyruqlardan Qanday Himoyalaymiz?</h2>
    <p class="lede" data-ru="Если вы дадите агенту инструмент 'выполнить bash', злоумышленник через Prompt Injection заставит его удалить сервер!" data-en="Exposing arbitrary shell or code execution tools risks disastrous Remote Code Execution (RCE) via prompt injection.">Agar agentga 'bash buyrug'ini bajarish' asbobi berilsa, tajovuzkor Prompt Injection orqali butun bazani o'chirib yuborishi mumkin!</p>
    <div class="grid c3" style="margin-top:20px;">
      <div class="card">
        <span class="pill" style="color:var(--accent-ink);" data-ru="Правило 1" data-en="Rule 1">Qoida 1</span>
        <h3 data-ru="White-list команд" data-en="Tool Whitelisting">Ruxsatlar Oq Ro'yxati</h3>
        <p data-ru="Никакого eval()! Доступны только явно разрешенные функции: add, search, query." data-en="Strictly prohibit eval()! Only expose explicit deterministic functions.">Hech qachon `eval()` ishlatilmaydi! Faqat aniq tasdiqlangan funksiyalar ulanadi.</p>
      </div>
      <div class="card" style="border:2px solid var(--green);">
        <span class="pill" style="color:var(--green);" data-ru="Правило 2" data-en="Rule 2">Qoida 2</span>
        <h3 data-ru="Docker / gVisor" data-en="Container Sandboxes">Docker Izolyatsiyasi</h3>
        <p data-ru="Код выполняется в изолированном микро-контейнере без доступа к хост-системе и сети." data-en="Run untrusted scripts in ephemeral isolated containers stripped of root and network access.">Kod asosiy serverda emas, alohida xotira va huquqlari cheklangan Docker ichida aylanadi.</p>
      </div>
      <div class="card">
        <span class="pill" data-ru="Правило 3" data-en="Rule 3">Qoida 3</span>
        <h3 data-ru="Таймауты и память" data-en="Quotas & Timeouts">Resurs Cheklovlari</h3>
        <p data-ru="Лимит: 2 секунды на команду и максимум 128 MB RAM. Защита от fork-бомб." data-en="Cap execution: 2-second timeout and 128MB RAM limit prevent runaway fork bombs.">Har bir asbobga 2 sekunddan ko'p vaqt va 128 MB dan ortiq xotira berilmaydi.</p>
      </div>
    </div>
  </section>""")

    # Slide 9: Multi-Tool Chaining
    slides.append("""  <!-- SLIDE 9: MULTI-TOOL CHAINING -->
  <section class="slide" data-phase="Zanjir|Цепочки|Chaining" data-time="48:00–54:00">
    <div class="eyebrow" data-ru="ЦЕПОЧКИ ИНСТРУМЕНТОВ · MULTI-TOOL" data-en="MULTI-TOOL CHAINING">KO'P ASBOBLI ZANJIR · MULTI-TOOL CHAINING</div>
    <h2 data-ru="Цепочка Инструментов: Когда Одного Мало" data-en="Tool Chaining: Orchestrating Sequential Actuators">Asboblar Zanjiri: Bir Nechta Vositalarni Ketma-ket Chaqirish</h2>
    <p class="lede" data-ru="Реальные задачи требуют комбинации: сначала 'поиск в базе', затем 'расчет скидки', затем 'отправка в Telegram'." data-en="Production workflows chain tools sequentially: database query ➔ calculation ➔ Telegram alert dispatch.">Haqiqiy biznes vazifalarida asboblar birin-ketin chaqiriladi: Bazadan ma'lumot olish ➔ Chegirmani hisoblash ➔ Telegramga xabar yuborish.</p>
    <div class="grid c2" style="margin-top:16px;">
      <div class="card">
        <h3 data-ru="Пример цепочки из 3 шагов" data-en="3-Step Sequential Pipeline">3 Qadamli Ketma-ketlik</h3>
        <ol style="margin-left:18px; line-height:1.8; font-size:13px;">
          <li data-ru="Tool 1: get_user(id=42) ➔ Баланс: 500$" data-en="Tool 1: get_user(id=42) ➔ Balance: $500">1-Asbob: `get_user(id=42)` ➔ Foydalanuvchi balansi olinadi</li>
          <li data-ru="Tool 2: calculate(500 - 120) ➔ Остаток: 380$" data-en="Tool 2: calculate(500 - 120) ➔ Remainder: $380">2-Asbob: `calculate(500 - 120)` ➔ Yangi balans hisoblanadi</li>
          <li data-ru="Tool 3: send_sms(phone, msg) ➔ Успешно!" data-en="Tool 3: send_sms(phone, msg) ➔ Success!">3-Asbob: `send_sms(phone, msg)` ➔ Mijozga SMS tasdiq ketadi</li>
        </ol>
      </div>
      <div class="card">
        <h3 data-ru="Управление контекстом Observation" data-en="Observation Context Management">Xotira Va Kontekst Oynasi</h3>
        <p data-ru="Каждое наблюдение увеличивает контекст. Важно возвращать только компактные факты, а не гигантские дампы HTML на 100 страниц!" data-en="Every observation bloats context. Return compact structured facts rather than dumping 100-page raw HTML payloads!">Har bir javob model xotirasini to'ldiradi. Shuning uchun butun sahifani emas, faqat kerakli 2 qator faktni qaytarish kerak!</p>
      </div>
    </div>
  </section>""")

    # Slide 10: Cyber Quiz
    slides.append("""  <!-- SLIDE 10: CYBER QUIZ -->
  <section class="slide" data-phase="Interaktiv Test|Тест|Interactive Quiz" data-time="54:00–60:00">
    <div class="eyebrow" data-ru="КИБЕР-ТЕСТ · ПРОВЕРКА ПОНИМАНИЯ" data-en="CYBER QUIZ · KNOWLEDGE CHECK">KIBER-TEST · BILIMNI TEKSHIRISH</div>
    <h2 data-ru="Кибер-Тест: Какая Ошибка в Описании Инструмента?" data-en="Cyber Quiz: Spot the Fatal Flaw in the Tool Specification">Kiber-Sinov: JSON Schemadagi Kritik Xatoni Toping!</h2>
    <p class="lede" data-ru="Разработчик описал инструмент get_weather. Но модель постоянно падает с ошибкой missing arguments. Где дефект схемы?" data-en="An engineer specified get_weather, but the model intermittently fails with missing arguments. Where is the flaw?">Dasturchi `get_weather` asbobini yozdi, lekin model ba'zan shahar nomini bermasdan xato chiqaryapti. Sxemada nima tushib qolgan?</p>
    <div class="quiz-box">
      <div class="quiz-options">
        <div class="quiz-opt" onclick="checkQuiz(this, false)">
          <span>A)</span> <span data-ru="Имя инструмента написано строчными буквами" data-en="Tool name is lowercase">Asbob nomi kichik harflar bilan yozilgan</span>
        </div>
        <div class="quiz-opt" onclick="checkQuiz(this, true)">
          <span>B)</span> <span data-ru="Забыли объявить массив required: ['city']" data-en="Omitted the mandatory required: ['city'] array">Majburiy maydonlar massivi `required: ['city']` yozilmagan</span>
        </div>
        <div class="quiz-opt" onclick="checkQuiz(this, false)">
          <span>C)</span> <span data-ru="Нужно было писать на C++, а не на JSON" data-en="Must use C++ instead of JSON">JSON o'rniga C++ ishlatish kerak edi</span>
        </div>
      </div>
      <button class="fix-btn" onclick="toggleTestFix()">
        <span class="btn-txt" data-ru="🔍 Посмотреть Разбор / Решение" data-en="🔍 View Breakdown / Solution">🔍 Yechim Tahlilini Ko'rish</span>
      </button>
      <div class="test-fix-box" id="testFixBox" style="display:none; margin-top:12px; padding:12px; background:rgba(16,185,129,0.08); border-left:3px solid var(--green); border-radius:4px;">
        <b style="color:var(--green);" data-ru="Правильный ответ: B!" data-en="Correct Answer: B!">To'g'ri javob: B!</b>
        <p style="margin-top:4px; font-size:12px;" data-ru="Без поля required модель считает аргумент опциональным и в 30% случаев не передает его, что приводит к краху сервера при попытке прочитать undefined." data-en="Without the required array, models treat parameters as optional and omit them unpredictably, causing uncaught undefined errors!">Agar `required` ko'rsatilmasa, model parametrni ixtiyoriy deb o'ylaydi va uni yubormaydi. Natijada server `undefined` xatosini oladi!</p>
      </div>
    </div>
  </section>""")

    # Slide 11: Hands-on Arena (25 min)
    slides.append("""  <!-- SLIDE 11: HANDS-ON ARENA -->
  <section class="slide" data-phase="Amaliyot|Практика|Hands-on Lab" data-time="60:00–72:00">
    <div class="eyebrow" data-ru="ПРАКТИЧЕСКАЯ АРЕНА · 25 МИНУТ" data-en="HANDS-ON ARENA · 25 MINUTES">AMALIY ARENA · 25 DAQIQA</div>
    <h2 data-ru="Большая Лаборатория: Создайте Свой Набор Инструментов!" data-en="Hands-on Lab: Engineer Production Tool Actuators!">Katta Amaliy Laboratoriya: Shaxsiy Asboblar To'plamini Yarating!</h2>
    <p class="lede" data-ru="Откройте симулятор simulator/index.html и разработайте 3 инструмента: Калькулятор, Поиск в БД и Защищенный Runner." data-en="Launch simulator/index.html and implement 3 enterprise tools: Safe Math, SQL Lookup, and Isolated Runner.">Kompyuteringizda <b>simulator/index.html</b> ilovasini oching va 3 ta asbob uchun to'liq JSON Schema va bajaruvchi funksiyalarni quring:</p>
    <div class="grid c2" style="margin-top:16px;">
      <div class="card">
        <h3 data-ru="Чек-лист инженера" data-en="Engineer Checklist">Amaliyot Bosqichlari</h3>
        <ol style="margin-left:18px; line-height:1.8; font-size:13px;">
          <li data-ru="Написать схему инструмента calculate с валидацией математического выражения" data-en="Author JSON Schema for calculate with expression checks">`calculate` vositasi uchun JSON Schema yozish va xavfsiz hisoblash</li>
          <li data-ru="Создать инструмент query_database с обязательным параметром id" data-en="Implement query_database with required id parameter">`query_database` vositasida `id` parametrini tekshirish</li>
          <li data-ru="Реализовать блок Sandbox: отловить команду rm -rf и заблокировать!" data-en="Build Sandbox guard: intercept and reject dangerous rm -rf commands!">Xavfli buyruqlarni (masalan `rm -rf`) tutib olib bloklovchi qalqon qo'yish!</li>
          <li data-ru="Проверить возврат Observation и получить финальный ответ от агента" data-en="Verify Observation loop and validate final synthesized agent output">Observation orqali modelga natija qaytarib, yakuniy javobni olish</li>
        </ol>
      </div>
      <div class="card" style="text-align:center;">
        <span class="pill" data-ru="Таймер арены" data-en="Arena Timer">Kiber-Taymer</span>
        <div style="font-family:'JetBrains Mono', monospace; font-size:48px; font-weight:800; color:var(--accent); margin:12px 0;" id="arenaTimer">25:00</div>
        <div style="display:flex; justify-content:center; gap:8px;">
          <button type="button" class="dock-btn" onclick="startArenaTimer(25*60)" style="background:var(--accent); color:#00214A; font-weight:800;" data-ru="▶️ Старт" data-en="▶️ Start">▶️ Boshlash</button>
          <button type="button" class="dock-btn" onclick="resetArenaTimer()" style="border:1px solid var(--rule);" data-ru="🔄 Сброс" data-en="🔄 Reset">🔄 Qayta o'rnatish</button>
        </div>
      </div>
    </div>
  </section>""")

    # Slide 12: Bug Hunter
    slides.append("""  <!-- SLIDE 12: BUG HUNTER -->
  <section class="slide" data-phase="Tahlil|Анализ|Bug Hunter" data-time="72:00–76:00">
    <div class="eyebrow" data-ru="ОХОТА ЗА БАГАМИ · ТИПИЧНЫЕ ЛОВУШКИ" data-en="BUG HUNTER · REAL-WORLD PITFALLS">KIBER-DETEKTIV · REAL TUZOQLAR</div>
    <h2 data-ru="2 Главные Ловушки: Галлюцинации Аргументов и Injection" data-en="2 Critical Pitfalls: Argument Hallucinations & Injections">Eng Xavfli 2 ta Tuzoq: Soxta Parametrlar va RCE Injection</h2>
    <div class="grid c2" style="margin-top:16px;">
      <div class="card" style="border-left:4px solid var(--accent);">
        <span class="pill" style="color:var(--accent-ink);" data-ru="Ловушка 1: Выдуманные аргументы" data-en="Pitfall 1: Hallucinated Args">Tuzoq 1: Hallucinated Args</span>
        <h3 data-ru="Выдуманные параметры" data-en="Hallucinated Arguments">Model O'ylab Topgan Parametrlar</h3>
        <p data-ru="Модель передает аргументы, которых не было в схеме (например format: 'pdf')." data-en="Models invent spurious arguments not declared in the JSON Schema.">Model sxemada yo'q bo'lgan parametrlarni to'qib chiqarishi mumkin.</p>
        <div style="margin-top:6px; font-size:12px; color:var(--green); font-weight:700;" data-ru="✅ Защита: Строгая валидация Pydantic/Zod с флагом extra='forbid'!" data-en="✅ Fix: Enforce strict schema stripping with extra='forbid'!">✅ Qalqon: Zod yoki Pydantic orqali ortiqcha kalitlarni rad etish (`extra: forbid`)!</div>
      </div>
      <div class="card" style="border-left:4px solid var(--accent);">
        <span class="pill" style="color:var(--accent-ink);" data-ru="Ловушка 2: Инъекция команд" data-en="Pitfall 2: Command Injection">Tuzoq 2: Command Injection</span>
        <h3 data-ru="Инъекции через bash" data-en="Command Injection Actuators">Shell Argumentlarida Xakerlik</h3>
        <p data-ru="Если в калькулятор передать '1; rm -rf /', наивный eval() уничтожит систему." data-en="Passing '1; rm -rf /' into naive eval() erases host file structures.">Oddiy kalkulyatorga '1; rm -rf' berilsa, ehtiyotsiz `eval()` serverni o'chiradi.</p>
        <div style="margin-top:6px; font-size:12px; color:var(--green); font-weight:700;" data-ru="✅ Защита: AST-парсеры математики (mathjs) вместо eval()!" data-en="✅ Fix: Use AST math parsers rather than arbitrary code exec!">✅ Qalqon: `eval()` o'rniga faqat xavfsiz AST matematik kutubxona (`mathjs`) ishlatish!</div>
      </div>
    </div>
  </section>""")

    # Slide 13: 3-Tiered Homework
    slides.append("""  <!-- SLIDE 13: HOMEWORK -->
  <section class="slide" data-phase="Uy vazifasi|Домашнее задание|Homework" data-time="76:00–78:00">
    <div class="eyebrow" data-ru="10-БАЛЛЬНАЯ СИСТЕМА · 3 УРОВНЯ СЛОЖНОСТИ" data-en="10-POINT RUBRIC · 3 TIERS">10 BALLIK MEZON · 3 BOSQICHLI UY VAZIFASI</div>
    <h2 data-ru="Домашнее Задание: Защищенный Агентный Сервис" data-en="Homework Mission: Hardened Agentic Tool Service">Mustaqil Vazifa: Xavfsiz Agentik Asboblar Servisi</h2>
    <div class="grid c3" style="margin-top:20px;">
      <div class="card" style="border-top:4px solid var(--ink-3);">
        <span class="pill" data-ru="1-Уровень · 4 балла" data-en="Tier 1 · 4 pts">1-Bosqich (4 Ball)</span>
        <h3 data-ru="База: 2 JSON Схемы" data-en="Base: 2 JSON Schemas">Baza: 2 ta JSON Sxema</h3>
        <p data-ru="Описать 2 инструмента (kalkulyator va ob-havo) по стандарту JSON Schema со всеми типами и required." data-en="Specify 2 production tools (calculator & weather) in JSON Schema with strict types & required tags.">Kalkulyator va ob-havo uchun to'liq JSON Schema spetsifikatsiyasini xatosiz yozish.</p>
      </div>
      <div class="card" style="border-top:4px solid var(--accent);">
        <span class="pill" style="color:var(--accent-ink);" data-ru="2-Уровень · 4 балла" data-en="Tier 2 · 4 pts">2-Bosqich (4 Ball)</span>
        <h3 data-ru="Проект: Диспетчер вызова" data-en="Project: Execution Dispatcher">Amaliyot: Asboblar Ijrochisi</h3>
        <p data-ru="Написать функцию dispatchTool(name, args) с try/catch и возвратом ошибки в Observation." data-en="Build dispatchTool(name, args) with robust try/catch and structured Observation error routing.">`dispatchTool(name, args)` funksiyasini yozish, xatolarni ushlab Observation ga qaytarish.</p>
      </div>
      <div class="card" style="border-top:4px solid var(--green);">
        <span class="pill" style="color:var(--green);" data-ru="3-Уровень · 2 балла" data-en="Tier 3 · 2 pts">3-Bosqich (2 Ball)</span>
        <h3 data-ru="Кибер-Вызов: Песочница" data-en="Cyber Challenge: Sandboxing">Kiber-Chaqiruv: Sandboxing</h3>
        <p data-ru="Реализовать блок проверки безопасности: отклонять любые команды, содержащие exec, eval, sudo, rm." data-en="Implement regex security guard rejecting payloads containing exec, eval, sudo, rm.">Xavfsizlik filtri qurish: `eval`, `exec`, `sudo`, `rm` kabi buyruqlarni qat'iy bloklash.</p>
      </div>
    </div>
    <div class="card" style="margin-top:16px; background:rgba(0,240,255,0.06); border:1px solid rgba(0,240,255,0.2);">
      <p data-ru="Выполнить задание можно интерактивно в файле vazifa.html с автосохранением в браузере или на печатном бланке varaqa.html." data-en="You can complete the homework interactively in vazifa.html (with LocalStorage auto-save) or via printed varaqa.html.">Topshiriqni <b>vazifa.html</b> ilovasida (avtomatik saqlanadi) yoki <b>varaqa.html</b> qog'ozida topshirishingiz mumkin.</p>
    </div>
  </section>""")

    # Slide 14: Summary & Cheat Sheet
    slides.append("""  <!-- SLIDE 14: SUMMARY & CHEAT SHEET -->
  <section class="slide" data-phase="Xulosa|Итоги|Summary" data-time="78:00–80:00">
    <div class="eyebrow" data-ru="ИТОГИ УРОКА · ПАМЯТКА АРХИТЕКТОРА" data-en="KEY TAKEAWAYS · ARCHITECT CHEAT SHEET">DARS YAKUNI · ARXITEKTOR SPRAVOCHNIGI</div>
    <h2 data-ru="Чему Мы Научились: Золотой Стандарт Tool Calling" data-en="What We Mastered: Enterprise Tool Calling Rules">Bugun O'rganganlarimiz: Tool Calling Oltin Qoidalari</h2>
    <div class="grid c3" style="margin-top:20px;">
      <div class="card">
        <h3 data-ru="📋 JSON Schema" data-en="📋 JSON Schema">📋 JSON Schema</h3>
        <p data-ru="name, description и required — фундамент. Описание должно четко объяснять модели задачу." data-en="name, description, and required are foundational. Clear descriptions guide routing.">`name`, `description` va `required` poydevordir. Ta'rif modelga yo'l ko'rsatadi.</p>
      </div>
      <div class="card">
        <h3 data-ru="🛡️ Sandboxing" data-en="🛡️ Sandboxing">🛡️ Sandboxing</h3>
        <p data-ru="Никогда не доверяйте коду модели. Выполняйте вызовы в изолированных контейнерах с таймаутом." data-en="Never trust generated code. Run actuators in sandboxed containers with strict timeouts.">Model bergan kodni hech qachon asosiy tizimda yurgizmang. Vaqt va xotirani cheklang.</p>
      </div>
      <div class="card">
        <h3 data-ru="🔄 Observation Loop" data-en="🔄 Observation Loop">🔄 Observation Tsikli</h3>
        <p data-ru="Ошибки инструментов возвращаются модели для самокоррекции, а не валят бэкенд." data-en="Tool errors flow back into Observation for self-correction rather than crashing hosts.">Xatoliklar serverni o'ldirmaydi, modelga yangi imkoniyat sifatida qaytariladi.</p>
      </div>
    </div>
  </section>""")

    all_slides_html = "\n\n".join(slides)
    tpl = re.sub(r'<div class="stage">[\s\S]*?</div><!-- /stage -->', f'<div class="stage">\n{all_slides_html}\n</div><!-- /stage -->', tpl)

    # 14 NOTES Triplets
    notes_obj = {
        "uz": [
            ["Darsga Kirish", "Til modeliga qo'l berish va Tool calling ahamiyatini tushuntiring.", "1-slaydni ekranga oching."],
            ["Uy Vazifasi Tahlili", "O'tgan darsdagi ReAct tsikli va max_iterations cheklovini tekshiring.", "ReAct ning 3 bosqichini so'rang."],
            ["Parametrik Xotira Cheklovi", "Nega LLM yolg'iz o'zi aniq hisob-kitob qila olmasligini ko'rsating.", "Hallucination misollarini ayting."],
            ["Tool Calling Konveyeri", "4 bosqichli konveyerni doskaga chizing (Prompt ➔ JSON ➔ Sandbox ➔ Observation).", "Daftarga qayd qildiring."],
            ["Interaktiv Simulyator", "Smartboardda kalkulyator, ob-havo va xavfli bash buyruqlarini sinab ko'rsating.", "O'quvchilarni doskaga chaqiring."],
            ["JSON Schema Standarti", "name, description va required maydonlarining vazifasini tushuntiring.", "Description prompt ekanligini ayting."],
            ["Argumentlar Validatsiyasi", "Zod va Pydantic nima uchun kerakligini ko'rsating.", "Xatoni Observation ga qaytarishni tushuntiring."],
            ["Xavfsiz Sandboxing", "RCE xavfi va Docker izolyatsiyasi zaruratini ta'kidlang.", "eval() ishlatish taqiqlanishini ayting."],
            ["Asboblar Zanjiri", "Bir nechta vositani ketma-ket ulash tartibini ko'rsating.", "Kontekst oynasini tejashni ayting."],
            ["Kiber-Quiz", "O'quvchilardan to'g'ri javobni so'rang.", "Doskada yechimni ochib tushuntiring."],
            ["Amaliy Laboratoriya", "O'quvchilarga simulator ilovasini ochishni ayting.", "25 daqiqalik taymerni yoqing."],
            ["Xatolar Tahlili", "Model to'qib chiqargan parametrlar va injection xatolarini fosh qiling.", "Himoya kodini ko'rsating."],
            ["Uy Vazifasi", "10 ballik rubrikani (4-4-2) tushuntiring.", "vazifa.html ilovasini ko'rsating."],
            ["Dars Yakuni", "Tool Callingning 3 oltin qoidasini takrorlab, o'quvchilarni baholang.", "Darsni yakunlang."]
        ],
        "ru": [
            ["Введение в урок", "Объясните важность предоставления инструментов языковой модели.", "Откройте 1-й слайд на проекторе."],
            ["Разбор Д/З", "Покажите ошибку с бесконечным циклом в ReAct из урока 25.", "Повторите 3 фазы ReAct."],
            ["Ограничения LLM", "Объясните, почему модель ошибается в арифметике без инструментов.", "Разберите галлюцинации."],
            ["Конвейер вызовов", "Нарисуйте 4 шага вызова инструментов на доске.", "Попросите переписать схему."],
            ["Интерактивный симулятор", "Протестируйте вызовы на смартборде: калькулятор, погода, bash.", "Покажите ответ песочницы."],
            ["JSON Schema", "Разберите поля name, description и required.", "Подчеркните роль описания."],
            ["Валидация типов", "Объясните защитный слой Zod/Pydantic.", "Покажите цикл обратной связи при ошибке."],
            ["Sandboxing и RCE", "Предупредите об угрозе выполнения произвольного кода.", "Покажите изоляцию в Docker."],
            ["Цепочки инструментов", "Разберите сценарий вызова нескольких функций подряд.", "Объясните контроль токенов."],
            ["Кибер-Тест", "Спросите класс о фатальной ошибке в схеме.", "Откройте правильный ответ B."],
            ["Практическая арена", "Дайте старт 25-минутной разработке в simulator.", "Включите таймер на экране."],
            ["Анализ ловушек", "Разберите выдуманные аргументы и инъекции команд.", "Покажите AST-парсеры."],
            ["Домашнее задание", "Огласите 10-балльную систему (4-4-2).", "Напомните про интерактивный vazifa.html."],
            ["Итоги урока", "Повторите 3 золотых правила Tool Calling.", "Выставите оценки за спаренный блок."]
        ],
        "en": [
            ["Lesson Intro", "Explain why language models require external tool actuators.", "Display Slide 1."],
            ["Homework Review", "Review the runaway loop and max_iterations pitfall from Lesson 25.", "Quiz students on ReAct."],
            ["LLM Limitations", "Demonstrate why pre-trained weights fail at deterministic arithmetic.", "Highlight hallucinations."],
            ["Tool Calling Pipeline", "Diagram the 4-step invocation pipeline on board.", "Instruct students to sketch flow."],
            ["Interactive Simulator", "Interact with calculator, weather, and dangerous bash calls on smartboard.", "Show observation return."],
            ["JSON Schema Standard", "Break down name, description, parameters, and required constraints.", "Emphasize routing prompts."],
            ["Type Validation", "Demonstrate validation guards using Zod and Pydantic.", "Explain error recovery loops."],
            ["Sandboxing & RCE", "Warn against Remote Code Execution and advocate container isolation.", "Ban arbitrary eval()."],
            ["Multi-Tool Chaining", "Trace sequential multi-actuator chaining architectures.", "Discuss context frugality."],
            ["Cyber Quiz", "Poll the class regarding missing required properties.", "Reveal answer B on screen."],
            ["Hands-on Arena", "Direct students to open simulator/index.html.", "Activate 25-min countdown timer."],
            ["Pitfall Autopsy", "Analyze hallucinated arguments and command injections.", "Show AST math parsers."],
            ["Homework Rubric", "Clarify the 10-point rubric breakdown (4-4-2).", "Point out vazifa.html auto-save."],
            ["Summary & Wrap-up", "Recap JSON Schema, Sandboxing, and Observation loops.", "Record grades."]
        ]
    }
    notes_json = json.dumps(notes_obj, ensure_ascii=False, indent=2)
    tpl = re.sub(r'var NOTES\s*=\s*\{[\s\S]*?\};', f'var NOTES = {notes_json};', tpl)

    # Interactive Slide JS for Tool Calling Simulator
    slide_js = """
// ============================================================
// SLIDE 5: TOOL CALLING SIMULATOR LOGIC
// ============================================================
var arenaTimerInterval = null;

function runSimTool(type) {
  var nameEl = document.getElementById("simToolName");
  var payloadEl = document.getElementById("simJsonPayload");
  var obsEl = document.getElementById("simObservationText");
  if (!nameEl || !payloadEl || !obsEl) return;

  if (type === "calc") {
    nameEl.textContent = currentLang === "ru" ? "Инструмент: calculate" : (currentLang === "en" ? "Tool: calculate" : "Asbob: calculate");
    payloadEl.innerHTML = "<code>{\\n  \\\"name\\\": \\\"calculate\\\",\\n  \\\"arguments\\\": {\\n    \\\"expression\\\": \\\"48 * 125 + 720\\\"\\n  }\\n}</code>";
    obsEl.textContent = "6720";
    obsEl.style.color = "var(--green)";
  } else if (type === "weather") {
    nameEl.textContent = currentLang === "ru" ? "Инструмент: get_weather" : (currentLang === "en" ? "Tool: get_weather" : "Asbob: get_weather");
    payloadEl.innerHTML = "<code>{\\n  \\\"name\\\": \\\"get_weather\\\",\\n  \\\"arguments\\\": {\\n    \\\"city\\\": \\\"Tashkent\\\",\\n    \\\"units\\\": \\\"celsius\\\"\\n  }\\n}</code>";
    obsEl.textContent = currentLang === "ru" ? "{\\\"temp\\\": 18, \\\"condition\\\": \\\"Солнечно\\\", \\\"humidity\\\": 42}" : (currentLang === "en" ? "{\\\"temp\\\": 18, \\\"condition\\\": \\\"Sunny\\\", \\\"humidity\\\": 42}" : "{\\\"temp\\\": 18, \\\"condition\\\": \\\"Quyoshli\\\", \\\"namlik\\\": 42}");
    obsEl.style.color = "var(--green)";
  } else if (type === "sql") {
    nameEl.textContent = currentLang === "ru" ? "Инструмент: query_database" : (currentLang === "en" ? "Tool: query_database" : "Asbob: query_database");
    payloadEl.innerHTML = "<code>{\\n  \\\"name\\\": \\\"query_database\\\",\\n  \\\"arguments\\\": {\\n    \\\"sku\\\": \\\"SKU-902\\\"\\n  }\\n}</code>";
    obsEl.textContent = "{\\\"item\\\": \\\"Target Cyber-Backpack\\\", \\\"stock\\\": 14, \\\"warehouse\\\": \\\"Tashkent-Central\\\"}";
    obsEl.style.color = "var(--green)";
  } else if (type === "bash") {
    nameEl.textContent = currentLang === "ru" ? "Инструмент: execute_bash (ЗАБЛОКИРОВАН)" : (currentLang === "en" ? "Tool: execute_bash (BLOCKED)" : "Asbob: execute_bash (BLOKLANDI)");
    payloadEl.innerHTML = "<code>{\\n  \\\"name\\\": \\\"execute_bash\\\",\\n  \\\"arguments\\\": {\\n    \\\"command\\\": \\\"rm -rf /\\\"\\n  }\\n}</code>";
    obsEl.textContent = currentLang === "ru" ? "⛔ SECURITY ERROR: Destructive system command rejected by Sandbox Guardrail!" : (currentLang === "en" ? "⛔ SECURITY ERROR: Destructive system command rejected by Sandbox Guardrail!" : "⛔ XAVFSIZLIK XATOSI: Zararli tizim buyrug'i Sandbox Qalqoni tomonidan bloklandi!");
    obsEl.style.color = "var(--red)";
  }
}

function toggleTestFix() {
  var b = document.getElementById("testFixBox");
  if (b) b.style.display = (b.style.display === "none") ? "block" : "none";
}

function startArenaTimer(dur) {
  var display = document.getElementById("arenaTimer");
  if (!display) return;
  clearInterval(arenaTimerInterval);
  var remaining = dur;
  arenaTimerInterval = setInterval(function() {
    remaining--;
    var m = Math.floor(remaining / 60);
    var s = remaining % 60;
    display.textContent = (m < 10 ? "0" : "") + m + ":" + (s < 10 ? "0" : "") + s;
    if (remaining <= 0) {
      clearInterval(arenaTimerInterval);
      display.textContent = "00:00";
    }
  }, 1000);
}

function resetArenaTimer() {
  clearInterval(arenaTimerInterval);
  var display = document.getElementById("arenaTimer");
  if (display) display.textContent = "25:00";
}
"""
    tpl = tpl.replace("</script>", slide_js + "\n</script>")

    with open(os.path.join(LESSON_DIR, "prezentatsiya.html"), "w", encoding="utf-8") as f:
        f.write(tpl)
    print(f"  ✓ Created: prezentatsiya.html")

    # 2. VARAQA.HTML
    v_tpl = TPL_VAR
    v_tpl = v_tpl.replace("{{LESSON_NUM}}", "26")
    v_tpl = v_tpl.replace("{{TITLE_UZ}}", "Agentik Tool Calling, Funksiyalar va Xavfsiz Sandboxing")
    v_tpl = v_tpl.replace("{{TITLE_RU}}", "Агентный Tool Calling, Функции и Безопасный Sandboxing")
    v_tpl = v_tpl.replace("{{TITLE_EN}}", "Agentic Tool Calling, Function Actuators & Safe Sandboxing")
    v_tpl = v_tpl.replace("{{COHORT_LABEL_UZ}}", "10–11-sinf")
    v_tpl = v_tpl.replace("{{COHORT_LABEL_RU}}", "10–11 класс")
    v_tpl = v_tpl.replace("{{COHORT_LABEL_EN}}", "Grades 10–11")

    v_tpl = v_tpl.replace("{{META_UZ}}", "2-Chorak · 10-hafta · 26-dars · Senior AI & Enterprise Kiberxavfsizlik Track")
    v_tpl = v_tpl.replace("{{META_RU}}", "2-я четверть · 10-я неделя · 26-й урок · Senior AI & Enterprise Кибербезопасность")
    v_tpl = v_tpl.replace("{{META_EN}}", "Quarter 2 · Week 10 · Lesson 26 · Senior AI & Enterprise Cybersecurity Track")

    v_tpl = v_tpl.replace("{{MISSION_UZ}}", "LLM agentiga tashqi asboblarni (Tools) JSON Schema orqali ulash, argumentlarni validatsiya qilish va xavfli buyruqlarni Sandboxing orqali izolyatsiya qilish.")
    v_tpl = v_tpl.replace("{{MISSION_RU}}", "Подключение внешних инструментов к LLM через JSON Schema, валидация аргументов и безопасная изоляция выполнения в Sandboxing.")
    v_tpl = v_tpl.replace("{{MISSION_EN}}", "Connecting external actuators to LLMs via JSON Schema, validating payloads, and enforcing sandboxed execution to defend against RCE.")

    v_tpl = v_tpl.replace("{{SEC1_TITLE_UZ}}", "1-Qism: JSON Schema Spetsifikatsiyasi va Majburiy Maydonlar")
    v_tpl = v_tpl.replace("{{SEC1_TITLE_RU}}", "Часть 1: Спецификация JSON Schema и Обязательные Поля")
    v_tpl = v_tpl.replace("{{SEC1_TITLE_EN}}", "Part 1: JSON Schema Specification & Mandatory Fields")
    v_sec1 = """    <div class="box-grid">
      <div class="box">
        <h4 data-ru="1. Роль поля description" data-en="1. Role of description">1. Description Maydonining Vazifasi</h4>
        <p data-ru="Почему текстовое описание инструмента является промптом для роутера модели?" data-en="Why is the tool description critical for LLM routing heuristics?">Asbobning 'description' matni nega model uchun qaror qabul qiluvchi prompt hisoblanadi?</p>
        <div class="write-line"></div>
        <div class="write-line"></div>
      </div>
      <div class="box">
        <h4 data-ru="2. Массив required" data-en="2. required Array">2. 'required' Massivi</h4>
        <p data-ru="Какая ошибка возникает в рантайме, если параметр не указан в массиве required?" data-en="What runtime exception emerges if a parameter is missing from required?">Agar parametr 'required' ro'yxatiga kiritilmasa, qanday xatolik ro'y berishi mumkin?</p>
        <div class="write-line"></div>
        <div class="write-line"></div>
      </div>
    </div>"""
    v_tpl = v_tpl.replace("{{SEC1_CONTENT}}", v_sec1)

    v_tpl = v_tpl.replace("{{SEC2_TITLE_UZ}}", "2-Qism: Kod Tahlili — Valyuta Konverteri Schemasi")
    v_tpl = v_tpl.replace("{{SEC2_TITLE_RU}}", "Часть 2: Анализ Кода — Схема Конвертера Валют")
    v_tpl = v_tpl.replace("{{SEC2_TITLE_EN}}", "Part 2: Code Analysis — Currency Converter Schema")
    v_sec2 = """    <div class="code-snippet">// ⚠️ JSON Schemani to'ldiring: summa (number) va valyuta (string) majburiy bo'lsin:
{
  "name": "convert_currency",
  "description": "Valyutani joriy kurs bo'yicha so'mga aylantiradi",
  "parameters": {
    "type": "object",
    "properties": {
      "amount": { "type": "________________" },
      "from_currency": { "type": "string" }
    },
    "required": [________________________________________]
  }
}</div>
    <p style="margin-top:4px;" data-ru="Запишите недостающие типы и обязательный массив:" data-en="Fill in the missing types and required array:">Bo'sh qoldirilgan joylarga to'g'ri tur va massiv elementlarini yozing:</p>
    <div class="write-line"></div>"""
    v_tpl = v_tpl.replace("{{SEC2_CONTENT}}", v_sec2)

    v_tpl = v_tpl.replace("{{SEC3_TITLE_UZ}}", "3-Qism: Amaliy Laboratoriya (4 ta Tool Sinovi)")
    v_tpl = v_tpl.replace("{{SEC3_TITLE_RU}}", "Часть 3: Практическая Лаборатория (Таблица 4 Тестов)")
    v_tpl = v_tpl.replace("{{SEC3_TITLE_EN}}", "Part 3: Hands-on Lab (4 Tests Audit Table)")
    v_sec3 = """    <p data-ru="Проверьте работу инструментов в simulator/index.html и заполните протокол:" data-en="Verify tool execution in simulator/index.html and log the protocol:"><b>simulator/index.html</b> ilovasida 4 ta asbobni sinab, natijalarni qayd eting:</p>
    <div class="box" style="margin-top:6px;">
      <table style="width:100%; border-collapse:collapse; font-size:8.5pt;">
        <thead>
          <tr style="border-bottom:1px solid var(--rule); text-align:left;">
            <th style="padding:4px 6px;">#</th>
            <th style="padding:4px 6px;" data-ru="Имя инструмента" data-en="Tool Name">Asbob Nomi</th>
            <th style="padding:4px 6px;" data-ru="Переданный JSON" data-en="Dispatched JSON">Model Bergan Argumentlar</th>
            <th style="padding:4px 6px;" data-ru="Observation (Факт)" data-en="Observation (Fact)">Sandbox Qaytargan Natija</th>
            <th style="padding:4px 6px;" data-ru="Статус" data-en="Status">Holat</th>
          </tr>
        </thead>
        <tbody>
          <tr style="border-bottom:1px dashed var(--hair);">
            <td style="padding:4px 6px;">1</td>
            <td style="padding:4px 6px;" data-ru="calculate" data-en="calculate"><code>calculate</code></td>
            <td style="padding:4px 6px;" data-ru='{"expr": "48*125+720"}' data-en='{"expr": "48*125+720"}'><code>{"expr": "48*125+720"}</code></td>
            <td style="padding:4px 6px;">6720</td>
            <td style="padding:4px 6px;" data-ru="[ &nbsp; ] Готово" data-en="[ &nbsp; ] Done">[ &nbsp; ] OK</td>
          </tr>
          <tr style="border-bottom:1px dashed var(--hair);">
            <td style="padding:4px 6px;">2</td>
            <td style="padding:4px 6px;" data-ru="get_weather" data-en="get_weather"><code>get_weather</code></td>
            <td style="padding:4px 6px;" data-ru='{"city": "Tashkent"}' data-en='{"city": "Tashkent"}'><code>{"city": "Tashkent"}</code></td>
            <td style="padding:4px 6px;"><div class="write-line" style="margin:2px 0;"></div></td>
            <td style="padding:4px 6px;" data-ru="[ &nbsp; ] Готово" data-en="[ &nbsp; ] Done">[ &nbsp; ] OK</td>
          </tr>
          <tr style="border-bottom:1px dashed var(--hair);">
            <td style="padding:4px 6px;">3</td>
            <td style="padding:4px 6px;" data-ru="query_db" data-en="query_db"><code>query_db</code></td>
            <td style="padding:4px 6px;" data-ru='{"sku": "SKU-902"}' data-en='{"sku": "SKU-902"}'><code>{"sku": "SKU-902"}</code></td>
            <td style="padding:4px 6px;"><div class="write-line" style="margin:2px 0;"></div></td>
            <td style="padding:4px 6px;" data-ru="[ &nbsp; ] Готово" data-en="[ &nbsp; ] Done">[ &nbsp; ] OK</td>
          </tr>
          <tr>
            <td style="padding:4px 6px;">4</td>
            <td style="padding:4px 6px;" data-ru="execute_bash" data-en="execute_bash"><code>execute_bash</code></td>
            <td style="padding:4px 6px;" data-ru='{"cmd": "rm -rf /"}' data-en='{"cmd": "rm -rf /"}'><code>{"cmd": "rm -rf /"}</code></td>
            <td style="padding:4px 6px;" data-ru="SECURITY BLOCKED" data-en="SECURITY BLOCKED">BLOKLANDI (Xavfli buyruq)</td>
            <td style="padding:4px 6px;" data-ru="[ &nbsp; ] Готово" data-en="[ &nbsp; ] Done">[ &nbsp; ] OK</td>
          </tr>
        </tbody>
      </table>
    </div>"""
    v_tpl = v_tpl.replace("{{SEC3_CONTENT}}", v_sec3)

    v_sec4 = """    <div class="box-grid" style="margin-top:6px;">
      <div class="box">
        <h4 data-ru="1-Уровень: База (4 балла)" data-en="Tier 1: Base (4 pts)">1-Daraja: Baza (4 ball)</h4>
        <p data-ru="Описать 2 валидных JSON Schema инструмента со всеми типами и required полями." data-en="Author 2 valid JSON Schema tool specifications with types and required arrays.">Barcha turlari va required massiviga ega bo'lgan 2 ta to'g'ri JSON Schema yozish.</p>
        <div class="write-line"></div>
      </div>
      <div class="box">
        <h4 data-ru="2-Уровень: Проект (4 балла)" data-en="Tier 2: Project (4 pts)">2-Daraja: Amaliyot (4 ball)</h4>
        <p data-ru="Реализовать диспетчер dispatchTool с безопасным try/catch и обработкой ошибок." data-en="Implement dispatchTool runner with defensive try/catch error routing.">Xatolarni ushlab Observation ga qaytaruvchi xavfsiz `dispatchTool` funksiyasini dasturlash.</p>
        <div class="write-line"></div>
      </div>
    </div>
    <div class="box" style="margin-top:6px;">
      <h4 data-ru="3-Уровень: Кибер-Вызов (2 балла)" data-en="Tier 3: Cyber Challenge (2 pts)">3-Daraja: Kiber-Chaqiruv (2 ball)</h4>
      <p data-ru="Реализовать фильтр песочницы, блокирующий вызовы системных деструктивных команд." data-en="Implement a regex sandbox guardrail intercepting destructive shell commands.">Tizimni buzuvchi buyruqlarni (`rm`, `eval`, `sudo`) aniqlab bloklovchi xavfsizlik filtri qo'yish.</p>
      <div class="write-line"></div>
    </div>"""
    v_tpl = v_tpl.replace("{{SEC4_CONTENT}}", v_sec4)

    with open(os.path.join(LESSON_DIR, "varaqa.html"), "w", encoding="utf-8") as f:
        f.write(v_tpl)
    print(f"  ✓ Created: varaqa.html")

    # 3. VAZIFA.HTML
    vz_tpl = TPL_VAZ
    vz_tpl = vz_tpl.replace("{{LESSON_NUM}}", "26")
    vz_tpl = vz_tpl.replace("{{TITLE_UZ}}", "Agentik Tool Calling, Funksiyalar va Xavfsiz Sandboxing")
    vz_tpl = vz_tpl.replace("{{TITLE_RU}}", "Агентный Tool Calling, Функции и Безопасный Sandboxing")
    vz_tpl = vz_tpl.replace("{{TITLE_EN}}", "Agentic Tool Calling, Function Actuators & Safe Sandboxing")
    vz_tpl = vz_tpl.replace("{{COHORT_LABEL_UZ}}", "10–11-sinf")
    vz_tpl = vz_tpl.replace("{{COHORT_LABEL_RU}}", "10–11 класс")
    vz_tpl = vz_tpl.replace("{{COHORT_LABEL_EN}}", "Grades 10–11")

    vz_tpl = vz_tpl.replace("{{META_UZ}}", "2-Chorak · 10-hafta · 26-dars · Mustaqil Kiber-Laboratoriya")
    vz_tpl = vz_tpl.replace("{{META_RU}}", "2-я четверть · 10-я неделя · 26-й урок · Самостоятельная кибер-лаборатория")
    vz_tpl = vz_tpl.replace("{{META_EN}}", "Quarter 2 · Week 10 · Lesson 26 · Independent Cyber Lab")

    vz_tpl = vz_tpl.replace("{{DESC_UZ}}", "Tool Calling, JSON Schema va Sandboxing xavfsizligi bo'yicha 3 ta topshiriqni bajaring. Javoblaringiz avtomatik saqlanadi.")
    vz_tpl = vz_tpl.replace("{{DESC_RU}}", "Выполните 3 задания по спецификации JSON Schema, вызовам инструментов и изоляции в песочнице. Прогресс сохраняется автоматически.")
    vz_tpl = vz_tpl.replace("{{DESC_EN}}", "Complete 3 engineering tasks on JSON Schema specs, tool dispatching, and sandbox isolation. Progress auto-saves.")

    vz_tpl = vz_tpl.replace("{{T1_TITLE_UZ}}", "1-Topshiriq: JSON Schema Spetsifikatsiyasi (Baza — 4 ball)")
    vz_tpl = vz_tpl.replace("{{T1_TITLE_RU}}", "Задание 1: Спецификация JSON Schema (База — 4 балла)")
    vz_tpl = vz_tpl.replace("{{T1_TITLE_EN}}", "Task 1: JSON Schema Authoring (Base — 4 pts)")
    vz_tpl = vz_tpl.replace("{{T1_DESC_UZ}}", "Foydalanuvchi elektron pochtasini jo'natuvchi 'send_email' vositasi uchun JSON Schema yozing (to, subject, body majburiy bo'lsin):")
    vz_tpl = vz_tpl.replace("{{T1_DESC_RU}}", "Напишите спецификацию JSON Schema для инструмента 'send_email' с обязательными полями to, subject, body:")
    vz_tpl = vz_tpl.replace("{{T1_DESC_EN}}", "Write JSON Schema specification for a 'send_email' actuator requiring to, subject, and body:")

    vz_tpl = vz_tpl.replace("{{T2_TITLE_UZ}}", "2-Topshiriq: Xatolarni Observation ga Qaytarish (Amaliyot — 4 ball)")
    vz_tpl = vz_tpl.replace("{{T2_TITLE_RU}}", "Задание 2: Возврат Ошибок в Observation (Проект — 4 балла)")
    vz_tpl = vz_tpl.replace("{{T2_TITLE_EN}}", "Task 2: Observation Error Feedback (Project — 4 pts)")
    vz_tpl = vz_tpl.replace("{{T2_DESC_UZ}}", "Nega asbob xato berganida server qulab tushmasligi, balki xato matnini modelga qaytarishi kerak? Ushbu mexanizmni tushuntiring:")
    vz_tpl = vz_tpl.replace("{{T2_DESC_RU}}", "Почему при ошибке выполнения инструмента сервер не должен падать, а возвращать ошибку в Observation модели?")
    vz_tpl = vz_tpl.replace("{{T2_DESC_EN}}", "Why should runtime actuator failures return structured error messages into Observation rather than aborting the process?")

    vz_tpl = vz_tpl.replace("{{T3_TITLE_UZ}}", "3-Topshiriq: Kiber-Chaqiruv — RCE dan Qalqon (2 ball)")
    vz_tpl = vz_tpl.replace("{{T3_TITLE_RU}}", "Задание 3: Кибер-Вызов — Защита от RCE (2 балла)")
    vz_tpl = vz_tpl.replace("{{T3_TITLE_EN}}", "Task 3: Cyber Challenge — Hardened Sandboxing (2 pts)")
    vz_tpl = vz_tpl.replace("{{T3_DESC_UZ}}", "Tashqi kod bajaruvchi agentga tajovuzkor 'eval(malicious_code)' yuborsa, qanday arxitektura uni to'xtatib qoladi? Sandboxing qoidalarini yozing:")
    vz_tpl = vz_tpl.replace("{{T3_DESC_RU}}", "Как защитить систему, если агент пытается выполнить вредоносный код через eval()? Опишите архитектуру изоляции:")
    vz_tpl = vz_tpl.replace("{{T3_DESC_EN}}", "How do you safeguard backends when prompt injection forces arbitrary eval() executions? Outline sandboxing rules:")

    with open(os.path.join(LESSON_DIR, "vazifa.html"), "w", encoding="utf-8") as f:
        f.write(vz_tpl)
    print(f"  ✓ Created: vazifa.html")

    # 4. TEACHER_READING.MD
    tr_content = """# 26-Dars: O'qituvchi Uchun Metodik Qo'llanma (Teacher Briefing)

**Kohorta:** 10–11-Sinf · Senior AI & Enterprise Kiberxavfsizlik Track  
**Mavzu:** Agentik Tool Calling, Funksiyalar va Xavfsiz Sandboxing  
**Ajratilgan vaqt:** 80 daqiqa (Juftlik blok / Double Block)  
**Amaliy natija:** LLM ga tashqi asboblarni (Tools) JSON Schema orqali ulash, deterministik argumentlar validatsiyasi, xavfli buyruqlarni bloklash va sandbox muhitida xavfsiz bajarish.

---

## 1. 5 Daqiqalik Darsoldi Konspekti (O'qituvchiga Eslatma)
Katta til modellari (LLM) o'zicha mustaqil hisob-kitob qila olmaydi yoki real vaqt ma'lumotlarini bilmaydi.
Ular **Tool Calling (Function Calling)** protokoli orqali tashqi dunyo bilan aloqa qiladi:
1. **JSON Schema:** Modelga funksiya qanday nomlanishi, nima vazifa bajarishi va qanday parametrlar qabul qilishi deklarativ ta'riflanadi.
2. **Argumentlar Validatsiyasi:** LLM bergan argumentlar xom holda ishlatilmaydi, Zod / Pydantic bilan qat'iy tekshiriladi.
3. **Sandboxing & RCE Mudofaasi:** Agentga hech qachon xom `eval()` yoki erkin bash berilmaydi. Buyruqlar izolyatsiyalangan konteynerda bajariladi.
4. **Observation Feedback:** Vosita xato qaytarsa, jarayon to'xtatilmaydi — xato matni modelga yuboriladi va u o'zini o'zi tuzatadi.

---

## 2. 80 Daqiqalik Vaqt Xaritasi (Double Block Roadmap)
| Vaqt | Bosqich | O'qituvchi amali | O'quvchi harakati |
|---|---|---|---|
| **00–04 daq** | Titul & Motivatsiya | Proyektorda 1-slaydni ochish, modelga 'qo'l' berish tushunchasini e'lon qilish | Muhandislik maqsadini tushunish |
| **04–10 daq** | O'tgan Dars Tahlili (HW Review) | 25-darsdagi ReAct tsikli va cheksiz aylanish (loop guard) xatolarini tahlil qilish | ReAct bosqichlarini qaytarish |
| **10–16 daq** | Parametrik Xotira Cheklovi | Nega LLM arifmetikada va yangi faktlarda yanglishishini ko'rsatish | Hallucination sababini yozish |
| **16–22 daq** | Tool Calling Konveyeri | 4 bosqichli oqimni (Prompt ➔ JSON ➔ Sandbox ➔ Observation) tushuntirish | Daftarga konveyerni chizish |
| **22–30 daq** | Jonli Simulyator (Slayd 5) | Smartboardda kalkulyator, ob-havo va xavfli bash buyruqlarini sinab ko'rsatish | Smartboardga chiqib asbob chaqirish |
| **30–40 daq** | JSON Schema & Sandboxing | 6–9 slaydlar: `name`, `description`, `required`, RCE xavfsizligi va 10-slayddagi kiber-test | Kiber-quiz javobini belgilash |
| **40–65 daq (25 min)** | Katta Amaliy Arena | Har bir o'quvchi kompyuterida `simulator/index.html` ni ochish, 25 daqiqalik taymerni yoqish | 3 ta asbob uchun sxema yozish |
| **65–72 daq (7 min)** | Juftlikda Peer Review | Partadoshlar bir-birining asboblar sxemasini xatolik va RCE zaifliklariga tekshiradi | Kodni audit qilish |
| **72–76 daq (4 min)** | Xatolar Tahlili (Bug Hunter) | Model o'ylab topgan soxta parametrlar va command injection himoyasini tushuntirish | Extra-forbid qoidasini yozish |
| **76–80 daq (4 min)** | Baholash va Vazifa | 10 ballik mezon asosida baholash, `vazifa.html` topshirig'ini tushuntirish | Ish varaqalarini topshirish |

---

## 3. Baholash Mezoni (10 Ballik Standart)
- **1–4 Ball (Baza):** 2 ta to'g'ri JSON Schema yozildi (`name`, `description`, `parameters`, `required`).
- **5–7 Ball (Standart):** Argumentlar validatsiyasi va xatolarni Observation ga xavfsiz qaytarish dasturlandi.
- **8–10 Ball (Senior AI Engineer):** Sandboxing filtri to'liq ishlaydi, xavfli buyruqlar bloklandi va ish varaqasi 100% to'ldirildi.
"""
    with open(os.path.join(LESSON_DIR, "TEACHER_READING.md"), "w", encoding="utf-8") as f:
        f.write(tr_content)
    print(f"  ✓ Created: TEACHER_READING.md")

    # 5. SIMULATOR/INDEX.HTML
    sim_html = """<!DOCTYPE html>
<html lang="uz" data-theme="dark">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title data-ru="Target Tool Calling Studio (10–11 класс)" data-en="Target Tool Calling Studio (Grades 10–11)">Target Tool Calling Studiyasi (10–11-sinf)</title>
<link rel="icon" type="image/svg+xml" href="/assets/favicon.svg">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Manrope:wght@600;700;800&family=Source+Sans+3:wght@400;600;700&family=JetBrains+Mono:wght@400;700&display=swap">
<style>
:root {
  --bg: #050E1F; --panel: #0B1A38; --panel-2: #122852;
  --ink: #F0F4FA; --ink-2: #A5B6D0; --ink-3: #6C819F;
  --rule: #1B355A; --accent: #00F0FF; --green: #10B981; --red: #FF3B26;
}
:root[data-theme="light"] {
  --bg: #F0F4FA; --panel: #FFFFFF; --panel-2: #E8EEF8;
  --ink: #00214A; --ink-2: #384A68; --ink-3: #7586A2;
  --rule: #DCE4EF; --accent: #0284C7; --green: #059669; --red: #FF1100;
}
* { box-sizing: border-box; margin: 0; padding: 0; }
body {
  font-family: 'Source Sans 3', sans-serif;
  background: var(--bg);
  color: var(--ink);
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}
header {
  padding: 16px 24px;
  background: var(--panel);
  border-bottom: 1px solid var(--rule);
  display: flex;
  justify-content: space-between;
  align-items: center;
}
.brand { display: flex; align-items: center; gap: 10px; font-weight: 800; }
.badge { background: var(--accent); color: #00214A; padding: 3px 8px; border-radius: 4px; font-size: 11px; font-weight: 800; }
main {
  flex: 1;
  max-width: 1000px;
  width: 100%;
  margin: 24px auto;
  padding: 0 16px;
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 20px;
}
.card {
  background: var(--panel);
  border: 1px solid var(--rule);
  border-radius: 12px;
  padding: 20px;
  display: flex;
  flex-direction: column;
  gap: 12px;
}
h2 { font-size: 16px; font-weight: 800; color: var(--accent); }
pre {
  background: var(--panel-2);
  border: 1px solid var(--rule);
  border-radius: 8px;
  padding: 12px;
  font-family: 'JetBrains Mono', monospace;
  font-size: 11.5px;
  color: var(--ink);
  overflow-x: auto;
  min-height: 140px;
}
button.btn {
  background: var(--panel-2);
  color: var(--ink);
  border: 1px solid var(--rule);
  padding: 10px 14px;
  border-radius: 8px;
  font-weight: 700;
  font-size: 13px;
  cursor: pointer;
  text-align: left;
  transition: all 0.2s ease;
}
button.btn:hover { border-color: var(--accent); color: var(--accent); }
button.btn-danger:hover { border-color: var(--red); color: var(--red); }
.status-box {
  padding: 12px;
  border-radius: 8px;
  background: var(--panel-2);
  border-left: 4px solid var(--green);
  font-family: 'JetBrains Mono', monospace;
  font-size: 12px;
  min-height: 50px;
}
</style>
</head>
<body>
<header>
  <div class="brand">
    <span>TARGET AGENTIC TOOL STUDIO</span>
    <span class="badge" data-ru="10–11 КЛАСС" data-en="GRADES 10–11">10–11-SINF</span>
  </div>
  <button class="btn" onclick="toggleTheme()" data-ru="🌓 Тема" data-en="🌓 Theme">🌓 Mavzu</button>
</header>
<main>
  <div class="card">
    <h2 data-ru="Инструменты Агента (Tool Catalog)" data-en="Agent Tool Catalog">Asboblar Katalogi (Tool Catalog)</h2>
    <p style="font-size:12px; color:var(--ink-2);" data-ru="Нажмите на любой инструмент, чтобы отправить вызов в модель и песочницу:" data-en="Click any tool to dispatch declarative payload to sandbox:">Asbobni tanlang: model qanday JSON argument yaratishini kuzating:</p>
    <div style="display:flex; flex-direction:column; gap:8px;">
      <button class="btn" onclick="execTool('calc')" data-ru="🧮 1. Вычислить выражение (calculate)" data-en="🧮 1. Evaluate math (calculate)">🧮 1. Matematik Hisoblash (calculate)</button>
      <button class="btn" onclick="execTool('weather')" data-ru="🌤️ 2. Запрос погоды (get_weather)" data-en="🌤️ 2. Live Weather Query (get_weather)">🌤️ 2. Jonli Ob-havo API (get_weather)</button>
      <button class="btn" onclick="execTool('db')" data-ru="🗄️ 3. Поиск в SQLite базе (query_inventory)" data-en="🗄️ 3. Query SQLite Database (query_inventory)">🗄️ 3. SQLite Bazadan Qidiruv (query_inventory)</button>
      <button class="btn btn-danger" onclick="execTool('danger')" data-ru="⚠️ 4. Опасный шелл-вызов (rm -rf /)" data-en="⚠️ 4. Dangerous Shell Exec (rm -rf /)">⚠️ 4. Xavfli Buyruq: rm -rf /</button>
    </div>
  </div>

  <div class="card">
    <h2 data-ru="Вызов JSON и Результат Песочницы" data-en="JSON Payload & Sandbox Output">JSON Payload va Sandbox Natijasi</h2>
    <div style="font-size:11px; font-weight:700; color:var(--ink-3);" data-ru="Сгенерированный LLM JSON-вызов:" data-en="LLM Generated Payload:">Model Bergan JSON Argumentlar:</div>
    <pre id="jsonViewer"><code>// Kutilmoqda...</code></pre>
    <div style="font-size:11px; font-weight:700; color:var(--ink-3);" data-ru="Результат песочницы (Observation):" data-en="Sandbox Observation:">Sandbox Qaytargan Javob (Observation):</div>
    <div class="status-box" id="obsViewer">Kutilmoqda...</div>
  </div>
</main>
<script>
function execTool(type) {
  var jv = document.getElementById("jsonViewer");
  var ov = document.getElementById("obsViewer");
  
  if (type === "calc") {
    jv.innerHTML = "<code>{\\n  \\\"name\\\": \\\"calculate\\\",\\n  \\\"arguments\\\": {\\n    \\\"expr\\\": \\\"(450 * 12) + (1800 / 4)\\\"\\n  }\\n}</code>";
    ov.textContent = "5850";
    ov.style.borderColor = "var(--green)";
    ov.style.color = "var(--green)";
  } else if (type === "weather") {
    jv.innerHTML = "<code>{\\n  \\\"name\\\": \\\"get_weather\\\",\\n  \\\"arguments\\\": {\\n    \\\"city\\\": \\\"Tashkent\\\",\\n    \\\"format\\\": \\\"celsius\\\"\\n  }\\n}</code>";
    ov.textContent = "{\\\"city\\\": \\\"Tashkent\\\", \\\"temp\\\": 19, \\\"wind\\\": \\\"4 m/s\\\", \\\"air_quality\\\": \\\"Good\\\"}";
    ov.style.borderColor = "var(--green)";
    ov.style.color = "var(--green)";
  } else if (type === "db") {
    jv.innerHTML = "<code>{\\n  \\\"name\\\": \\\"query_inventory\\\",\\n  \\\"arguments\\\": {\\n    \\\"product_id\\\": 1042\\n  }\\n}</code>";
    ov.textContent = "{\\\"id\\\": 1042, \\\"title\\\": \\\"Target Cyber-Notebook Pro\\\", \\\"stock\\\": 28, \\\"status\\\": \\\"In Stock\\\"}";
    ov.style.borderColor = "var(--green)";
    ov.style.color = "var(--green)";
  } else if (type === "danger") {
    jv.innerHTML = "<code>{\\n  \\\"name\\\": \\\"execute_shell\\\",\\n  \\\"arguments\\\": {\\n    \\\"command\\\": \\\"rm -rf / --no-preserve-root\\\"\\n  }\\n}</code>";
    ov.textContent = "⛔ SANDBOX SECURITY BREACH INTERCEPTED: Dangerous shell execution is strictly blocked by Guardrails!";
    ov.style.borderColor = "var(--red)";
    ov.style.color = "var(--red)";
  }
}

function toggleTheme() {
  var cur = document.documentElement.getAttribute("data-theme") || "dark";
  document.documentElement.setAttribute("data-theme", cur === "dark" ? "light" : "dark");
}
</script>
</body>
</html>"""
    with open(os.path.join(SIM_DIR, "index.html"), "w", encoding="utf-8") as f:
        f.write(sim_html)
    print(f"  ✓ Created: simulator/index.html")

build_10_11_lesson()
print("🎉 10–11-sinf generation finished!")
