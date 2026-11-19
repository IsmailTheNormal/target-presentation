#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
scripts/build_10_11_w11_l29.py — Builder for 10–11th Grade, Week 11, Lesson 29

Mavzu: Avtonom Kod Yozuvchi Agentlar: Coder, Critic va TDD Tsikli
Format: Juftlik Dars (80 daqiqa), 14 slayd
Kohorta: 10-11-sinf (Senior AI & Enterprise Architecture Track)
"""

import os
import sys
import json
import re

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DEST_DIR = os.path.join(REPO_ROOT, "classes", "10-11-sinf", "11-hafta", "29-dars-avtonom-kod-agentlari-va-tdd")

os.makedirs(DEST_DIR, exist_ok=True)
os.makedirs(os.path.join(DEST_DIR, "simulator"), exist_ok=True)

# -----------------------------------------------------------------------------
# 1. SLIDES HTML (14 Slides for 80-min Double Block)
# -----------------------------------------------------------------------------
SLIDES_HTML = """
  <!-- SLIDE 1: TITUL -->
  <section class="slide current" data-phase="Kirish|Введение|Intro" data-time="00:00–04:00" data-slide-index="0">
    <div class="eyebrow"><span class="t" data-ru="10–11-КЛАСС · 11-Я НЕДЕЛЯ · УРОК 29" data-en="GRADES 10–11 · WEEK 11 · LESSON 29">10–11-SINF · 11-HAFTA · 29-DARS</span></div>
    <h1 class="display" data-ru="Автономные Код-Агенты: Coder, Critic и Цикл TDD" data-en="Autonomous Coding Agents: Coder, Critic & TDD Reflection Loops">Avtonom Kod Yozuvchi Agentlar: Coder, Critic va TDD Tsikli</h1>
    <p class="lede" data-ru="Переход от слепой генерации кода к самовосстанавливающимся системам: Coder пишет код, Sandbox запускает тесты, Critic анализирует трейсбек и исправляет ошибки до идеального прохождения." data-en="Moving from raw code generation to self-correcting agentic engineering: Coder drafts implementation, Sandbox executes test suites, and Critic analyzes tracebacks to achieve 100% test passes.">Ko'r-ko'rona kod yozishdan o'z-o'zini tuzatuvchi tizimlarga o'tish: Coder kod yozadi, Sandbox testlarni ishga tushiradi, Critic xatolarni tahlil qilib kodni 100% yashil testlarga yetkazadi.</p>
    <div class="hero-split">
      <div class="box">
        <div class="tag" data-ru="Формат урока" data-en="Lesson Format">80 daqiqalik Juftlik Dars</div>
        <h3 data-ru="TDD и Рефлексия" data-en="TDD & Reflection">TDD va Self-Correction</h3>
        <p data-ru="Тест-ориентированная разработка (Test-Driven Development) как главная защита от галлюцинаций LLM." data-en="Test-Driven Development (TDD) as the ultimate safeguard against LLM hallucinations.">LLM gallyutsinatsiyalariga qarshi eng kuchli qurol: avval qat'iy testlar, keyin kod va refleksiya tsikli.</p>
      </div>
      <div class="box">
        <div class="tag" data-ru="Ожидаемый результат" data-en="Deliverable">Coder-Critic Studio</div>
        <h3 data-ru="Автономный Цикл" data-en="Autonomous Engine">Avtonom Dasturchi</h3>
        <p data-ru="Каждый ученик создаст замкнутый цикл Coder ➔ Runner ➔ Critic, способный исправить баги без участия человека." data-en="Each student configures a closed-loop Coder ➔ Runner ➔ Critic system that refines code autonomously.">Har bir o'quvchi xatolarni inson yordamisiz mustaqil tuzatuvchi Coder-Runner-Critic zanjirini kodlaydi.</p>
      </div>
    </div>
  </section>

  <!-- SLIDE 2: MANDATORY HW REVIEW -->
  <section class="slide" data-phase="Uy Vazifasi Tahlili|Разбор ДЗ|Homework Review" data-time="04:00–12:00" data-slide-index="1">
    <div class="eyebrow"><span class="t" data-ru="АНАЛИЗ ДОМАШНЕГО ЗАДАНИЯ 28-УРОКА" data-en="LESSON 28 HOMEWORK REVIEW">28-DARS UY VAZIFASI TAHLILI</span></div>
    <h2 data-ru="Multi-Agent Supervisor: Зацикливание и Ловушка Бесконечных Сообщений" data-en="Multi-Agent Supervisor: Infinite Message Ping-Pong Trap">Multi-Agent Supervisor: Cheksiz Ping-Pong va Deadlock</h2>
    <div class="grid-2">
      <div class="box danger-border">
        <div class="tag" style="background:rgba(239,68,68,0.15); color:var(--red);" data-ru="Типичная ошибка (Pitfall)" data-en="Common Pitfall">Keng Tarqalgan Xato (Pitfall)</div>
        <h4 data-ru="Бесконечный пинг-понг между Worker-ами без лимита шагов" data-en="Unbounded ping-pong between Workers without step limits">Workerlar o'rtasida cheksiz xabar almashinuvi</h4>
        <p style="font-size:12px;" data-ru="Supervisor не получил четкого условия FINISH, и два агента (Researcher и Coder) бесконечно пересылали друг другу уточнения. За 30 секунд сгорело 150,000 токенов!" data-en="Supervisor lacked an explicit FINISH condition, causing Researcher and Coder to ping-pong endlessly. Over 150,000 tokens were burned in 30 seconds!">Supervisor agentda aniq FINISH sharti qo'yilmagani sababli, Researcher va Coder bir-biriga cheksiz savol jo'natib 150,000 tokenni 30 soniyada yoqib yubordi!</p>
        <pre><code class="language-python"># ❌ Xato: Cheksiz siklga tushuvchi router
def route(state):
    return state["next_worker"] # Hech qachon FINISH bo'lmaydi!</code></pre>
      </div>
      <div class="box" style="border:1px solid var(--green);">
        <div class="tag" style="background:rgba(16,185,129,0.15); color:var(--green);" data-ru="Золотой стандарт (Golden Solution)" data-en="Golden Standard">Oltin Standart Yechim</div>
        <h4 data-ru="Recursion Limit + Счётчик итераций (Loop Guard)" data-en="Recursion Limit + Iteration Guard">Rekursiya Cheklovi + Loop Guard Qalqoni</h4>
        <p style="font-size:12px;" data-ru="В LangGraph задается config={'recursion_limit': 10}, а состояние хранит steps_taken. При достижении лимита градиент принудительно перенаправляется на Human-in-the-Loop." data-en="Configure recursion_limit=10 in LangGraph and track steps_taken in state. If limit is hit, gracefully route to Human-in-the-Loop for manual review.">LangGraph ichida recursion_limit=10 o'rnatiladi va har bir qadam sanaladi. Cheklov buzilsa, tizim to'xtatilib, inson nazoratiga yo'naltiriladi.</p>
        <pre><code class="language-python"># ✅ To'g'ri: Loop Guard va majburiy to'xtash
if state.get("step_count", 0) >= 6:
    return "human_approval" # Zudlik bilan to'xtatish!</code></pre>
      </div>
    </div>
    <div class="box" style="margin-top:12px; background:var(--surface-2);">
      <div style="font-size:12px; font-weight:700; color:var(--accent); margin-bottom:4px;" data-ru="⚡ Блиц-Вопрос и Мост к Теме:" data-en="⚡ Blitz Question & Lesson Bridge:">⚡ Blitz Savol va Bugungi Mavzuga Ko'prik:</div>
      <p style="font-size:12px; margin:0;" data-ru="<strong>Вопрос:</strong> Как гарантировать, что сгенерированный агентом код действительно работает, а не просто выглядит правильным? <em>(Ответ: Автоматические тесты в изолированной песочнице)</em>.<br><strong>Мост:</strong> Сегодня мы создадим Coder-агента, который не просто генерирует код, а прогоняет его через тесты и сам исправляет свои ошибки!" data-en="<strong>Question:</strong> How can we guarantee that AI-generated code actually executes correctly rather than merely looking plausible? <em>(Answer: Automated test execution inside an isolated sandbox)</em>.<br><strong>Bridge:</strong> Today we engineer autonomous coding agents that write unit tests, run code in sandboxes, and self-correct syntax and logical bugs!"><strong>Savol:</strong> AI yozgan kod shunchaki chiroyli ko'rinmasdan, real ishlayotganiga qanday kafolat beramiz? <em>(Javob: Xavfsiz sandboxda avtomatik unit testlarni ishga tushirish orqali)</em>.<br><strong>Ko'prik:</strong> Bugun biz kod yozuvchi Coder agentiga testlarni ishga tushiruvchi Sandbox va xatolarni tushuntiruvchi Critic agentini ulab, mustaqil TDD tsiklini quramiz!</p>
    </div>
  </section>

  <!-- SLIDE 3: WHY ONE-SHOT FAILS -->
  <section class="slide" data-phase="Muammo Tahlili|Анализ Проблемы|Problem Analysis" data-time="12:00–18:00" data-slide-index="2">
    <div class="eyebrow"><span class="t" data-ru="ПОЧЕМУ ПАДАЕТ ONE-SHOT КОД" data-en="WHY ONE-SHOT CODING FAILS">BIRINCHI URINISH MUAMMOSI</span></div>
    <h2 data-ru="Парадокс Генерации Кода: Почему LLM Ошибаются?" data-en="The Code Generation Paradox: Why Do Models Hallucinate?">Kod Yozish Paradoksi: Nega LLM Birinchi Urinishda Xato Qiladi?</h2>
    <div class="grid-2">
      <div>
        <p class="lede" style="font-size:14px; margin-bottom:12px;" data-ru="Большинство людей просят ChatGPT: «Напиши мне бэкенд на FastAPI». Модель выдает правдоподобный код, но в продакшене он ломается на первой же строчке." data-en="Most people prompt LLMs with: 'Write me a backend in FastAPI'. The model outputs plausible syntax, yet it crashes instantly in production.">Ko'pchilik AIga: "Menga FastAPI da backend yoz" deb buyruq beradi. Chiqqan kod chiroyli ko'rinadi, lekin productionda birinchi so'rovdayoq qulaydi.</p>
        <ul class="clean-list">
          <li data-ru="<strong>Отсутствие среды выполнения (No Runtime):</strong> LLM предсказывает следующие токены, а не компилирует абстрактное синтаксическое дерево (AST)." data-en="<strong>No Runtime Awareness:</strong> LLMs predict subsequent tokens; they do not evaluate ASTs or execute bytecode."><strong>Muhitning yo'qligi:</strong> LLM kodni kompyuterda run qilmaydi, u faqat ehtimollik bo'yicha keyingi so'zni topadi.</li>
          <li data-ru="<strong>Скрытые краевые случаи (Edge Cases):</strong> Пустые массивы, None-типы, гонки потоков (Race Conditions) не видны без тестов." data-en="<strong>Silent Edge Cases:</strong> Null pointers, empty payloads, and race conditions evade textual inspection without unit suites."><strong>Chekka holatlar (Edge Cases):</strong> Bo'sh massivlar, null qiymatlar va chegaraviy holatlar testlarsiz ko'rinmaydi.</li>
          <li data-ru="<strong>Галлюцинации API (Hallucinated Methods):</strong> Вызов несуществующих библиотечных методов с уверенным тоном." data-en="<strong>API Hallucinations:</strong> Inventing non-existent framework parameters with utmost grammatical confidence."><strong>Soxta API kutubxonalar:</strong> Real hayotda mavjud bo'lmagan metodlarni o'ylab topish.</li>
        </ul>
      </div>
      <div class="box" style="background:var(--surface-2); display:flex; flex-direction:column; justify-content:center; gap:8px;">
        <div style="font-weight:700; color:var(--red); font-size:13px;" data-ru="One-Shot Генерация vs Автономный Агент:" data-en="One-Shot Generation vs Autonomous Agent:">One-Shot Prompt vs Avtonom Agent:</div>
        <div style="font-size:11px; line-height:1.6; font-family:var(--font-mono);">
          <div style="color:var(--red);">❌ One-Shot: Prompt ➔ Kod ➔ 💥 Xatolik (Inson tuzatadi)</div>
          <div style="color:var(--green); margin-top:8px;">✅ Agentic TDD: Prompt ➔ Testlar ➔ Kod ➔ Sandbox ➔ Critic ➔ ✅ 100% Yashil Testlar!</div>
        </div>
      </div>
    </div>
  </section>

  <!-- SLIDE 4: TDD PARADIGM -->
  <section class="slide" data-phase="TDD Paradigmasi|Парадигма TDD|TDD Paradigm" data-time="18:00–24:00" data-slide-index="3">
    <div class="eyebrow"><span class="t" data-ru="ТЕСТ-ОРИЕНТИРОВАННАЯ РАЗРАБОТКА" data-en="TEST-DRIVEN DEVELOPMENT">TDD STANDARTI</span></div>
    <h2 data-ru="Тесты Первее Кода: Цикл RED-GREEN-REFACTOR для AI" data-en="Tests Before Code: The RED-GREEN-REFACTOR Loop for AI">Avval Test, Keyin Kod: RED-GREEN-REFACTOR Tsikli</h2>
    <div class="grid-3" style="gap:12px;">
      <div class="box" style="border-top:4px solid var(--red);">
        <div class="tag" style="background:rgba(239,68,68,0.15); color:var(--red);">1. RED (Qizil)</div>
        <h4 data-ru="Спецификация и Тесты" data-en="Spec & Unit Tests">Qat'iy Testlar Yozish</h4>
        <p style="font-size:12px;" data-ru="Агент-тестировщик сначала пишет 5 строгих модульных тестов на PyTest до написания реализации." data-en="Tester agent writes 5 rigorous PyTest unit tests defining inputs and outputs prior to implementation.">Tester agenti hali kod yozilmasdan oldin uning barcha talablari va chekka holatlari uchun 5 ta test yozadi.</p>
      </div>
      <div class="box" style="border-top:4px solid var(--green);">
        <div class="tag" style="background:rgba(16,185,129,0.15); color:var(--green);">2. GREEN (Yashil)</div>
        <h4 data-ru="Минимальный Рабочий Код" data-en="Minimal Implementation">Kod Generatsiyasi</h4>
        <p style="font-size:12px;" data-ru="Coder пишет код с единственной целью: чтобы все упавшие тесты загорелись зеленым цветом." data-en="Coder writes clean implementation focused strictly on satisfying every failing assertion.">Coder kodi faqat bitta maqsadga qaratiladi: yozilgan testlarning barchasidan muvaffaqiyatli o'tish.</p>
      </div>
      <div class="box" style="border-top:4px solid var(--purple);">
        <div class="tag" style="background:rgba(147,51,234,0.15); color:var(--purple);">3. REFACTOR (Tozalash)</div>
        <h4 data-ru="Оптимизация и Стиль" data-en="Refactor & Lint">Critic Tahlili va Tozalash</h4>
        <p style="font-size:12px;" data-ru="Critic проверяет асимптотическую сложность O(N), безопасность типов и читаемость кода." data-en="Critic reviews algorithmic complexity O(N), type safety, and memory consumption.">Critic agenti kodning murakkabligini O(N), xotira sarfini va xavfsizligini tekshirib tozalaydi.</p>
      </div>
    </div>
  </section>

  <!-- SLIDE 5: CODER AGENT -->
  <section class="slide" data-phase="Coder Arxitekturasi|Архитектура Coder|Coder Architecture" data-time="24:00–30:00" data-slide-index="4">
    <div class="eyebrow"><span class="t" data-ru="АГЕНТ-РАЗРАБОТЧИК" data-en="DEVELOPER AGENT">CODER AGENTI</span></div>
    <h2 data-ru="Системный Промпт и Архитектурные Ограничения Coder" data-en="System Prompt & Strict Architectural Constraints">Coder Agentining Tizimli Prompti va Qoidalari</h2>
    <div class="grid-2">
      <div>
        <p class="lede" style="font-size:14px; margin-bottom:12px;" data-ru="Coder не должен писать лишний текст или рассуждения вперемешку с кодом. Он возвращает строго валидный Python-модуль с Type Hints." data-en="Coder must never output conversational banter mixed into source code. It emits strictly validated, typed Python modules.">Coder agenti chalg'ituvchi gaplar yozmasligi shart. U faqat Type Hints va docstringlarga ega sof Python kodini qaytarishi lozim.</p>
        <ul class="clean-list">
          <li data-ru="<strong>Строгая типизация:</strong> Все функции имеют аннотации типов (typing.List, Dict, Optional)." data-en="<strong>Type Safety:</strong> Strict type annotations across all inputs and return signatures."><strong>Qat'iy turlar (Type Hints):</strong> Har bir parametr va qaytuvchi qiymat tipi ko'rsatiladi.</li>
          <li data-ru="<strong>Чистая функция (Pure Functions):</strong> Без скрытых глобальных мутаций состояния." data-en="<strong>Pure Functions:</strong> Zero unmanaged global side-effects or state mutation."><strong>Toza funksiyalar:</strong> Global o'zgaruvchilarga bog'lanmagan xavfsiz modullar.</li>
          <li data-ru="<strong>Структурированный вывод:</strong> Markdown-блоки кода с именем файла." data-en="<strong>Structured Output:</strong> File-scoped markdown code blocks parseable by AST."><strong>Strukturali format:</strong> Parser o'qiy oladigan toza format.</li>
        </ul>
      </div>
      <div class="box" style="background:var(--surface-2); font-family:var(--font-mono); font-size:11px; line-height:1.6;">
        <div style="color:var(--accent); font-weight:700; margin-bottom:6px;">[Coder System Prompt]</div>
        <pre><code class="language-markdown">Siz professional Python arxitektori va Coder agentsiz.
Vazifangiz: Berilgan texnik talablar va PyTest testlaridan
100% o'tuvchi toza, samarali kod yozish.
Qoidalar:
1. Faqat Python kodini ```python blokida qaytaring.
2. Har bir funksiyaga Type Hints va Docstring bering.
3. Hech qanday tashqi kutubxona ishlatmang (faqat standart lib).</code></pre>
      </div>
    </div>
  </section>

  <!-- SLIDE 6: SANDBOX RUNNER -->
  <section class="slide" data-phase="Sandbox Muhiti|Изолированная Песочница|Isolated Sandbox" data-time="30:00–35:00" data-slide-index="5">
    <div class="eyebrow"><span class="t" data-ru="БЕЗОПАСНОЕ ИСПОЛНЕНИЕ" data-en="SAFE CODE EXECUTION">SANDBOX TEST RUNNER</span></div>
    <h2 data-ru="Запуск Кода в Песочнице: Сбор Вывода и Трейсбеков" data-en="Executing Code in Sandbox: Capturing STDOUT & Tracebacks">Xavfsiz Sandboxda Testlarni Run Qilish va Tahlil</h2>
    <div class="grid-2">
      <div>
        <p class="lede" style="font-size:14px; margin-bottom:12px;" data-ru="Никогда не запускайте AI-код прямо на хост-сервере! Используется изолированный процесс с лимитами по памяти и таймаутом." data-en="Never run AI-generated code directly on host infrastructure! Enforce process sandboxing with tight memory and timeout limits.">AI yozgan kodni hech qachon asosiy serverda ishga tushirmang! U cheklangan vaqt (timeout 3s) va xavfsiz konteynerda bajarilishi shart.</p>
        <ul class="clean-list">
          <li data-ru="<strong>Захват STDOUT и STDERR:</strong> Все print() и сообщения об ошибках собираются в JSON." data-en="<strong>STDOUT & STDERR Capture:</strong> Structured capture of execution logs and stack traces into JSON."><strong>Loglarni yig'ish:</strong> Barcha konsol xabarlari va Tracebacklar JSON formatida saqlanadi.</li>
          <li data-ru="<strong>Код возврата (Exit Code):</strong> 0 — все тесты пройдены, 1 — падение ассертов." data-en="<strong>Exit Codes:</strong> Exit code 0 signals test success; code 1 highlights assertion failures."><strong>Chiqish kodi (Exit Code):</strong> 0 bo'lsa barcha testlar muvaffaqiyatli, 1 bo'lsa xatolik.</li>
          <li data-ru="<strong>Защита от зависаний:</strong> Принудительный SIGKILL через 3.0 секунды." data-en="<strong>Timeout Guard:</strong> Enforced SIGKILL after 3.0s prevents infinite while loops."><strong>Qotib qolishdan himoya:</strong> 3 soniyadan oshgan cheksiz while sikllari avtomatik o'chiriladi.</li>
        </ul>
      </div>
      <div class="box" style="background:var(--surface-2); font-family:var(--font-mono); font-size:11px; line-height:1.6;">
        <div style="color:var(--green); font-weight:700; margin-bottom:6px;">[Sandbox Runner Rejimi]</div>
        <pre><code class="language-python">import subprocess

def run_tests_safe(code_str, test_str):
    full_script = f"{code_str}\\n\\n{test_str}"
    res = subprocess.run(
        ["python3", "-c", full_script],
        capture_output=True, text=True,
        timeout=3.0 # Xavfsiz vaqt cheklovi
    )
    return {
        "success": res.returncode == 0,
        "stdout": res.stdout,
        "stderr": res.stderr
    }</code></pre>
      </div>
    </div>
  </section>

  <!-- SLIDE 7: CRITIC & REFLECTION -->
  <section class="slide" data-phase="Critic Tahlili|Критик и Рефлексия|Critic & Reflection" data-time="35:00–40:00" data-slide-index="6">
    <div class="eyebrow"><span class="t" data-ru="РЕФЛЕКСИЯ И САМОЛЕЧЕНИЕ" data-en="REFLECTION & HEALING">CRITIC VA REFLEKSIYA</span></div>
    <h2 data-ru="Анализ Ошибок: Как Critic Направляет Coder на Исправление" data-en="Traceback Analysis: How Critic Guides Coder to Self-Correction">Critic Qanday Qilib Xatoni Tahlil Qiladi va Tuzatadi?</h2>
    <div class="grid-2">
      <div>
        <p class="lede" style="font-size:14px; margin-bottom:12px;" data-ru="Если тесты упали, мы не просим Coder «переписать все заново». Critic вычленяет точную причину падения (Root Cause) и формирует патч." data-en="When tests fail, we never tell Coder to 'rewrite everything'. Critic pinpoints the precise root cause and instructs a targeted diff patch.">Testlar yiqilganda Coderga butun kodni noldan yozdirish xato! Critic xatolikning tub ildizini (Root Cause) aniqlab, qaysi qatorda nima o'zgarishi kerakligini aytadi.</p>
        <ul class="clean-list">
          <li data-ru="<strong>Сравнение Expected vs Actual:</strong> Почему тест ожидал 42, а функция вернула None?" data-en="<strong>Expected vs Actual Diff:</strong> Why did the test expect 42 while the function returned None?"><strong>Kutilgan vs Haqiqiy:</strong> Nega test 42 kutganida, funksiya None qaytardi?</li>
          <li data-ru="<strong>Локализация бага:</strong> Указание конкретной строки и переменной с ошибкой." data-en="<strong>Bug Localization:</strong> Isolating the exact variable and logic branch at fault."><strong>Xatolik nuqtasi:</strong> Qaysi o'zgaruvchi yoki if shartida xato ketgani ko'rsatiladi.</li>
          <li data-ru="<strong>Сохранение контекста:</strong> Не трогать уже работающие функции!" data-en="<strong>Regression Guard:</strong> Preserving already passing methods without regression."><strong>Boshqa qismlarga tegmaslik:</strong> Ishlab turgan testlarni buzib qo'ymaslik qoidasi.</li>
        </ul>
      </div>
      <div class="box" style="background:var(--surface-2); font-family:var(--font-mono); font-size:11px; line-height:1.6;">
        <div style="color:var(--purple); font-weight:700; margin-bottom:6px;">[Critic Tahlil Xabari]</div>
        <pre><code class="language-markdown">DIAGNOZ: Test 3 muvaffaqiyatsiz bo'ldi.
Xatolik: ZeroDivisionError on line 14.
Sababi: 'total_count' 0 ga teng bo'lgan holat
if tekshiruvi bilan himoyalanmagan.
KO'RSATMA CODERGA:
14-qatorga 'if total_count == 0: return 0.0'
qo'shing. Boshqa funksiyalarga tegmang!</code></pre>
      </div>
    </div>
  </section>

  <!-- SLIDE 8: IN-DECK INTERACTIVE SIMULATOR -->
  <section class="slide" data-phase="Smartboard Simulyatori|Интерактив на Доске|In-Deck Simulator" data-time="40:00–48:00" data-slide-index="7">
    <div class="eyebrow"><span class="t" data-ru="СИМУЛЯТОР НА СМАРТБОРДЕ" data-en="SMARTBOARD SIMULATOR">JONLI KOD AGENTI</span></div>
    <h2 data-ru="Запустите Цикл Coder-Runner-Critic Прямо на Доске!" data-en="Run the Coder-Runner-Critic TDD Loop Right on the Board!">Coder-Runner-Critic TDD Tsiklini Jonli Ishga Tushiring!</h2>
    <div style="display:grid; grid-template-columns: 1fr 340px; gap:14px; align-items:start;">
      <div style="background:#020617; border-radius:8px; border:1px solid var(--accent); padding:12px; font-family:var(--font-mono); font-size:11px; height:260px; overflow-y:auto; display:flex; flex-direction:column; gap:6px;" id="deckTerminal">
        <div style="color:var(--accent); font-weight:700;">[Terminal: Avtonom Kod Agentlari Tizimi]</div>
        <div style="color:#64748b;">Vazifani tanlang va "▶️ Agent Tsiklini Boshlash" tugmasini bosing...</div>
      </div>
      <div class="box" style="display:flex; flex-direction:column; gap:8px;">
        <label style="font-size:11px; font-weight:700;" data-ru="Выбор Задачи:" data-en="Select Task:">Vazifa Tanlovi:</label>
        <select id="selTask" style="background:var(--surface-2); color:var(--ink); border:1px solid var(--hair); border-radius:4px; padding:4px 8px; font-size:11px;">
          <option value="fib">Keshli Fibonacci (Recursion + Cache)</option>
          <option value="rate_limiter">Token Bucket Rate Limiter</option>
          <option value="lru">LRU Kesh Tizimi (O(1) Get/Put)</option>
        </select>
        <button class="btn" id="btnRunAgent" onclick="runDeckAgentCycle()" style="background:var(--green); color:#fff; font-weight:700; font-size:12px;" data-ru="▶️ Запустить Цикл Агента" data-en="▶️ Run Agent Loop">▶️ Agent Tsiklini Boshlash</button>
        <div style="font-size:11px; color:var(--ink-2); line-height:1.4; border-top:1px solid var(--hair); padding-top:6px;">
          <div>Iteratsiya: <strong id="deckIter" style="color:var(--purple);">0 / 3</strong></div>
          <div>Testlar: <strong id="deckTestStatus" style="color:var(--ink);">Kutilmoqda</strong></div>
        </div>
        <button class="btn" onclick="resetDeckAgent()" style="font-size:11px; background:var(--surface-2); border:1px solid var(--hair);" data-ru="🔄 Сброс" data-en="🔄 Reset">🔄 Qayta Boshlash</button>
      </div>
    </div>
  </section>

  <!-- SLIDE 9: INTERACTIVE QUIZ -->
  <section class="slide" data-phase="Viktorina|Квиз|Quiz" data-time="48:00–55:00" data-slide-index="8">
    <div class="eyebrow"><span class="t" data-ru="ПРОВЕРКА ЗНАНИЙ" data-en="KNOWLEDGE CHECK">KIBER-VIKTORINA</span></div>
    <h2 data-ru="3 Вопроса по Автономным Код-Агентам и TDD" data-en="3 Questions on Autonomous Coding & TDD">Avtonom Kodlash Bo'yicha 3 Ta Tezkor Savol</h2>
    <div class="grid-3" style="gap:12px;">
      <div class="box">
        <div class="tag" style="background:var(--accent); color:#fff;">1-Savol</div>
        <p style="font-size:12px; margin-bottom:10px;" data-ru="Почему в парадигме TDD тесты пишутся ДО написания основного кода?" data-en="Why are unit tests authored BEFORE implementation in TDD?">Nega TDD da testlar asosiy koddan OLDIN yoziladi?</p>
        <div style="display:flex; flex-direction:column; gap:6px;">
          <button class="btn quiz-btn" onclick="checkQuiz(this, true, 'To‘g‘ri! Testlar kod bajarishi kerak bo‘lgan qat‘iy chegaralarni oldindan belgilab beradi.')" style="font-size:11px;" data-ru="A) Задают строгие критерии приемки" data-en="A) Defines strict acceptance criteria">A) Qat'iy talab va chegaralarni belgilaydi</button>
          <button class="btn quiz-btn" onclick="checkQuiz(this, false, 'Noto‘g‘ri. Testlar kod hajmini kamaytirmaydi, sifatini kafolatlaydi.')" style="font-size:11px;" data-ru="B) Чтобы уменьшить размер файла" data-en="B) To minimize file size">B) Fayl hajmini kamaytirish uchun</button>
        </div>
      </div>
      <div class="box">
        <div class="tag" style="background:var(--purple); color:#fff;">2-Savol</div>
        <p style="font-size:12px; margin-bottom:10px;" data-ru="Какова главная задача агента Critic при падении тестов?" data-en="What is the primary objective of the Critic agent when tests fail?">Testlar yiqilganda Critic agentining asosiy vazifasi nima?</p>
        <div style="display:flex; flex-direction:column; gap:6px;">
          <button class="btn quiz-btn" onclick="checkQuiz(this, true, 'To‘g‘ri! Critic xatolik ildizini aniqlab, Coderga aniq ko‘rsatma beradi.')" style="font-size:11px;" data-ru="A) Найти причину сбоя и дать точный диф" data-en="A) Isolate root cause and provide targeted diff">A) Xatolik ildizini topib, aniq ko'rsatma berish</button>
          <button class="btn quiz-btn" onclick="checkQuiz(this, false, 'Noto‘g‘ri. Butun kodni o‘chirib noldan yozish xatoliklarni ko‘paytiradi.')" style="font-size:11px;" data-ru="B) Удалить весь код и начать с нуля" data-en="B) Delete all code and restart">B) Butun kodni o'chirib noldan yozish</button>
        </div>
      </div>
      <div class="box">
        <div class="tag" style="background:var(--green); color:#fff;">3-Savol</div>
        <p style="font-size:12px; margin-bottom:10px;" data-ru="Зачем песочнице (Sandbox) жесткий лимит времени (timeout: 3.0s)?" data-en="Why does the Sandbox enforce a strict execution timeout (e.g. 3.0s)?">Nega Sandboxda 3 soniyalik timeout qo'yilishi shart?</p>
        <div style="display:flex; flex-direction:column; gap:6px;">
          <button class="btn quiz-btn" onclick="checkQuiz(this, true, 'To‘g‘ri! Model cheksiz while sikl yozib qo‘ysa, server qotib qolmasligi uchun.')" style="font-size:11px;" data-ru="A) Защита от бесконечных циклов (while True)" data-en="A) Prevents infinite loops (while True)">A) Cheksiz sikllardan (while True) himoya</button>
          <button class="btn quiz-btn" onclick="checkQuiz(this, false, 'Noto‘g‘ri. Timeout internet tezligiga bog‘liq emas.')" style="font-size:11px;" data-ru="B) Чтобы ускорить интернет-соединение" data-en="B) To accelerate network bandwidth">B) Internet tezligini oshirish uchun</button>
        </div>
      </div>
    </div>
    <div id="quizFeedback" style="margin-top:10px; font-weight:700; font-size:12px; min-height:18px;"></div>
  </section>

  <!-- SLIDE 10: 25-MIN ARENA -->
  <section class="slide" data-phase="Amaliy Arena|Практическая Арена|Hands-on Arena" data-time="55:00–70:00" data-slide-index="9">
    <div class="eyebrow"><span class="t" data-ru="ПРАКТИЧЕСКАЯ АРЕНА (25 МИНУТ)" data-en="HANDS-ON ARENA (25 MIN)">AMALIY ARENA (25 DAQIQA)</span></div>
    <h2 data-ru="Создание Автономного Агента Coder-Critic" data-en="Engineering an Autonomous Coder-Critic System">Coder-Critic Avtonom Tizimini Qurish</h2>
    <div class="grid-2">
      <div>
        <div style="display:flex; gap:10px; align-items:center; margin-bottom:12px;">
          <button class="btn" id="arenaTimerBtn" onclick="toggleArenaTimer()" style="background:var(--accent); color:#fff; font-weight:700;" data-ru="⏱️ Запустить Таймер" data-en="⏱️ Start Timer">⏱️ Taymerni Boshlash</button>
          <span id="arenaTimerDisplay" style="font-family:var(--font-mono); font-size:24px; font-weight:700; color:var(--red);">25:00</span>
        </div>
        <p class="lede" style="font-size:13px; margin-bottom:8px;" data-ru="Откройте симулятор или VS Code и настройте граф рефлексии со следующими условиями:" data-en="Open the simulator or VS Code and implement the self-correcting reflection graph:">Simulyatorni oching va quyidagi 3 bosqichli avtonom tsiklni ishga tushiring:</p>
        <ul class="clean-list" style="font-size:12px;">
          <li data-ru="<strong>1-й Шаг (7 мин):</strong> Напишите Coder-промпт, генерирующий функцию с типизацией." data-en="<strong>Step 1 (7 min):</strong> Define Coder prompt producing typed, isolated Python code."><strong>1-Qadam (7 min):</strong> Type Hints bilan kod yozuvchi Coder promptini sozlang.</li>
          <li data-ru="<strong>2-й Шаг (8 мин):</strong> Подключите Sandbox Runner с перехватом STDOUT и Exit Code." data-en="<strong>Step 2 (8 min):</strong> Wire Sandbox Runner capturing stdout and return codes."><strong>2-Qadam (8 min):</strong> STDOUT va Exit Code qaytaruvchi Sandbox muhitini ulang.</li>
          <li data-ru="<strong>3-й Шаг (10 мин):</strong> Настройте рефлексию Critic: если Exit Code != 0, вернуть трейсбек в Coder!" data-en="<strong>Step 3 (10 min):</strong> Configure Critic: if Exit Code != 0, route tracebacks back to Coder!"><strong>3-Qadam (10 min):</strong> Critic refleksiyasini bog'lang: agar xato bo'lsa, Coderga qaytarib tuzating!</li>
        </ul>
      </div>
      <div class="box" style="background:var(--surface-2); display:flex; flex-direction:column; justify-content:space-between;">
        <div>
          <div style="font-weight:700; color:var(--accent); margin-bottom:6px;" data-ru="Критерии Оценки (10 Баллов):" data-en="10 Points Rubric:">10 Ballik Mezon:</div>
          <div style="font-size:11px; line-height:1.6;">
            <div>✅ <strong>4 Ball:</strong> Coder boshlang'ich kodni xatolarsiz generatsiya qiladi.</div>
            <div>✅ <strong>4 Ball:</strong> Sandbox testlarni run qilib, xatolikni Criticga uzatadi.</div>
            <div>✅ <strong>2 Ball:</strong> O'z-o'zini tuzatish tsikli (Self-Correction) 2-urinishda 100% yashil testlarga erishadi!</div>
          </div>
        </div>
        <div style="margin-top:10px; text-align:right;">
          <a href="simulator/index.html" target="_blank" class="btn" style="background:var(--purple); color:#fff; font-size:11px;" data-ru="Открыть Лабораторию" data-en="Launch Lab Studio">Katta Simulyatorni Ochish ➔</a>
        </div>
      </div>
    </div>
  </section>

  <!-- SLIDE 11: PEER REVIEW -->
  <section class="slide" data-phase="Partadosh Auditi|Взаимный Аудит|Peer Review" data-time="70:00–74:00" data-slide-index="10">
    <div class="eyebrow"><span class="t" data-ru="ВЗАИМНЫЙ АУДИТ КОДА" data-en="PEER CODE AUDIT">PARTADOSH AUDITI</span></div>
    <h2 data-ru="Аудит Системы Рефлексии: 4 Контрольные Точки" data-en="Reflection System Audit: 4 Critical Checkpoints">Refleksiya Tizimini Sinash: 4 Nazorat Nuqtasi</h2>
    <div class="grid-2">
      <div>
        <p class="lede" style="font-size:14px; margin-bottom:12px;" data-ru="Поменяйтесь местами и проверьте агентную систему одноклассника на прочность:" data-en="Swap workstations and battle-test your peer's autonomous agent architecture:">O'rin almashib, partadoshingizning avtonom tizimini tekshiring:</p>
        <ul class="clean-list">
          <li data-ru="<strong>1. Защита от бесконечного цикла:</strong> Есть ли счетчик итераций (max_iterations &lt;= 3)?" data-en="<strong>1. Loop Guard:</strong> Is max_iterations strictly bounded (&lt;= 3)?"><strong>1. Sikl cheklovi:</strong> Maksimal urinishlar soni (max_iterations &lt;= 3) bormi?</li>
          <li data-ru="<strong>2. Парсинг Трейсбека:</strong> Передает ли Critic точный номер строки с ошибкой?" data-en="<strong>2. Traceback Parsing:</strong> Does Critic pinpoint exact offending line numbers?"><strong>2. Xatolik tahlili:</strong> Critic xato qatorini aniq ko'rsatib beryaptimi?</li>
          <li data-ru="<strong>3. Таймаут Песочницы:</strong> Убивается ли процесс при while True?" data-en="<strong>3. Sandbox Timeout:</strong> Does SIGKILL terminate infinite while True loops?"><strong>3. Timeout himoyasi:</strong> Cheksiz siklda qotib qolmasdan to'xtayaptimi?</li>
          <li data-ru="<strong>4. Чистый Выход:</strong> Завершается ли агент корректным кодом 0 при успехе?" data-en="<strong>4. Clean Termination:</strong> Does system return Exit Code 0 upon green tests?"><strong>4. Yashil yakun:</strong> Testlar o'tgach, tizim muvaffaqiyatli to'xtayaptimi?</li>
        </ul>
      </div>
      <div class="box" style="border:1px dashed var(--accent); background:rgba(59,130,246,0.05); display:flex; flex-direction:column; justify-content:center; align-items:center; text-align:center;">
        <div style="font-size:40px; margin-bottom:8px;">🤖 🔍 🛡️</div>
        <h4 data-ru="Инженерная Честность" data-en="Engineering Integrity">Muhandislik Halolligi</h4>
        <p style="font-size:12px; color:var(--ink-2); max-width:240px; margin:0;" data-ru="Не подсказывайте ответы руками. Пусть агент исправит собственный баг через Critic!" data-en="Do not manually fix the bug. Force the autonomous Critic loop to resolve it!">Kodni qo'lda to'g'rilab bermang. Agent Critic ko'rsatmasi bilan o'zi tuzatishiga imkon bering!</p>
      </div>
    </div>
  </section>

  <!-- SLIDE 12: SHOWCASE -->
  <section class="slide" data-phase="Katta Ekran|Шоукейс|Showcase" data-time="74:00–77:00" data-slide-index="11">
    <div class="eyebrow"><span class="t" data-ru="ДЕМОНСТРАЦИЯ НА ДОСКЕ" data-en="SMARTBOARD SHOWCASE">KATTA EKRAN SHOWCASI</span></div>
    <h2 data-ru="Шоукейс: Автономный Дебаг Сложной Алгоритмической Задачи" data-en="Showcase: Autonomous Self-Correction of Complex Algorithmic Bugs">Showcase: Murakkab Algoritmik Xatolikni Avtonom Tuzatish</h2>
    <div class="grid-3" style="gap:12px;">
      <div class="box" style="border-top:4px solid var(--accent);">
        <h4 data-ru="1. Попытка 1: Сбой" data-en="1. Attempt 1: Fail">1. Birinchi Urinish (Crash)</h4>
        <p style="font-size:12px; color:var(--ink-2);" data-ru="Coder написал код без учета пустой строки. PyTest выбросил IndexError." data-en="Coder drafts solution neglecting empty strings. PyTest raises IndexError.">Bo'sh string hisobga olinmagani sababli IndexError yuz berdi.</p>
      </div>
      <div class="box" style="border-top:4px solid var(--purple);">
        <h4 data-ru="2. Рефлексия Critic" data-en="2. Critic Diagnosis">2. Critic Diagnostikasi</h4>
        <p style="font-size:12px; color:var(--ink-2);" data-ru="Critic проанализировал трейсбек и выдал точный патч: добавить проверку len(s) == 0." data-en="Critic dissects traceback and instructs adding 'if not s: return None'.">Critic xato sababini aniqlab, <code>if not s: return None</code> qo'shishni buyurdi.</p>
      </div>
      <div class="box" style="border-top:4px solid var(--green);">
        <h4 data-ru="3. Попытка 2: Успех!" data-en="3. Attempt 2: 100% Pass">3. Ikkinchi Urinish: G'alaba!</h4>
        <p style="font-size:12px; color:var(--ink-2);" data-ru="Coder применил патч. Все 5 тестов загорелись зеленым! Без вмешательства человека." data-en="Coder patches targeted line. All 5 test assertions pass without human intervention!">Coder tuzatdi va 5 ta test 100% yashil bo'ldi! Inson aralashuvisiz!</p>
      </div>
    </div>
    <div class="box" style="margin-top:12px; background:rgba(16,185,129,0.08); border:1px solid var(--green); text-align:center;">
      <span style="font-weight:700; color:var(--green); font-size:13px;" data-ru="🎉 Успех! Система самоисправления доказала свою надежность!" data-en="🎉 Success! Autonomous self-correction engine successfully verified!">🎉 Muvaffaqiyat! O'z-o'zini tuzatuvchi tizim inson aralashuvisiz kodni yashil testlarga yetkazdi!</span>
    </div>
  </section>

  <!-- SLIDE 13: TIERED HOMEWORK -->
  <section class="slide" data-phase="Uy Vazifasi|Домашнее Задание|Homework" data-time="77:00–79:00" data-slide-index="12">
    <div class="eyebrow"><span class="t" data-ru="ДОМАШНЕЕ ЗАДАНИЕ (10 БАЛЛОВ)" data-en="HOMEWORK (10 POINTS)">UY VAZIFASI (10 BALL)</span></div>
    <h2 data-ru="3 Уровня: От Базового Coder до Многошаговой Рефлексии" data-en="3 Challenge Tiers: From Base Coder to Multi-Step Self-Correction">3 Darajali Muhandislik Vazifasi: Coder-Critic</h2>
    <div class="grid-3" style="gap:12px;">
      <div class="box" style="border-top:4px solid var(--accent);">
        <div class="tag" style="background:rgba(59,130,246,0.15); color:var(--accent);">1-Daraja (Baza)</div>
        <h4 data-ru="TDD Промпт (4 Балла)" data-en="TDD Prompt (4 Points)">TDD Prompti (4 Ball)</h4>
        <p style="font-size:12px;" data-ru="Напишите спецификацию и 3 строгих PyTest-теста для валидатора email-адресов с проверкой краевых случаев." data-en="Author specification and 3 PyTest assertions for an email validator covering edge cases.">Email tekshirgich funksiyasi uchun 3 ta qat'iy PyTest testini va chekka holatlarni yozing.</p>
      </div>
      <div class="box" style="border-top:4px solid var(--purple);">
        <div class="tag" style="background:rgba(147,51,234,0.15); color:var(--purple);">2-Daraja (Amaliy)</div>
        <h4 data-ru="Sandbox Runner (4 Балла)" data-en="Sandbox Runner (4 Points)">Sandbox Runner (4 Ball)</h4>
        <p style="font-size:12px;" data-ru="Напишите Python-функцию safe_runner(), запускающую сгенерированный код с таймаутом 2.0 секунды и перехватом STDERR." data-en="Implement safe_runner() executing code with 2.0s timeout and structured stderr capture.">2.0 soniyalik timeout va STDERR loglarini tutib oluvchi xavfsiz safe_runner() funksiyasini yozing.</p>
      </div>
      <div class="box" style="border-top:4px solid var(--green);">
        <div class="tag" style="background:rgba(16,185,129,0.15); color:var(--green);">3-Daraja (Challenge)</div>
        <h4 data-ru="Critic Reflector (2 Балла)" data-en="Critic Reflector (2 Points)">Critic Refleksiya (2 Ball)</h4>
        <p style="font-size:12px;" data-ru="Создайте логику Critic: при ошибке извлечь имя упавшего ассерта и сформировать точечную инструкцию без перезаписи всего файла!" data-en="Build Critic prompt: extract failing assertion name and guide surgical diff without rewriting entire file!">Yiqilgan test nomini ajratib, butun faylni o'chirmasdan faqat xato qatorni tuzatuvchi Critic promptini tuzing!</p>
      </div>
    </div>
    <div style="margin-top:12px; text-align:right;">
      <a href="vazifa.html" class="btn" style="background:var(--purple); color:#fff; font-size:12px;" data-ru="Открыть ДЗ" data-en="Open HW">Vazifalar Ilovasini Ochish ➔</a>
    </div>
  </section>

  <!-- SLIDE 14: SUMMARY & BRIDGE -->
  <section class="slide" data-phase="Xulosa|Итоги|Summary & Bridge" data-time="79:00–80:00" data-slide-index="13">
    <div class="eyebrow"><span class="t" data-ru="ИТОГИ УРОКА" data-en="LESSON SUMMARY">XULOSA VA KEYINGI DARS</span></div>
    <h2 data-ru="Эра Самовосстанавливающегося Кода" data-en="The Era of Self-Healing Code">O'z-O'zini Tuzatuvchi Avtonom Kod Davri</h2>
    <div class="grid-2">
      <div>
        <p class="lede" style="font-size:14px; margin-bottom:12px;" data-ru="Сегодня мы увидели, как соединение Coder + Sandbox + Critic превращает ненадежную LLM в надежный инженерный инструмент." data-en="Today we witnessed how combining Coder + Sandbox + Critic transforms volatile LLMs into deterministic engineering tooling.">Bugun biz Coder + Sandbox + Critic uyg'unligi orqali beqaror LLM modelini ishonchli muhandislik vositasiga aylantirishni o'rgandik.</p>
        <ul class="clean-list">
          <li data-ru="<strong>TDD — Фундамент:</strong> Тесты определяют правильность, а не интуиция модели." data-en="<strong>TDD Foundation:</strong> Rigorous assertions define truth, not model intuition."><strong>TDD — Asosiy Qalqon:</strong> To'g'rilikni modelning gapi emas, unit testlar belgilaydi.</li>
          <li data-ru="<strong>Изоляция:</strong> Sandbox защищает сервер от опасных команд и бесконечных циклов." data-en="<strong>Sandbox Isolation:</strong> Guards host environments against unsafe calls and infinite loops."><strong>Izolyatsiya:</strong> Sandbox muhiti serverni xavfli kod va cheksiz sikllardan asraydi.</li>
          <li data-ru="<strong>Рефлексия:</strong> Critic точечно лечит баги, экономя токены и время." data-en="<strong>Reflection:</strong> Critic performs surgical bugfixes, conserving tokens and time."><strong>Refleksiya:</strong> Critic xatoni to'g'ridan-to'g'ri nuqtasidan tuzatadi.</li>
        </ul>
      </div>
      <div class="box" style="border-left:4px solid var(--purple); background:rgba(147,51,234,0.08);">
        <strong style="color:var(--purple); font-size:14px;" data-ru="Следующая Тема:" data-en="Next Topic:">🚀 Keyingi Dars Ko'prigi:</strong>
        <p style="font-size:12px; margin-top:6px; line-height:1.5;" data-ru="<strong>Agentic Web Browsing и Headless Scraping:</strong> Как научить AI самостоятельно выходить в интернет через Playwright, анализировать DOM-дерево и собирать данные!" data-en="<strong>Agentic Web Browsing & Headless Scraping:</strong> Teaching AI agents to browse the live web via Playwright, analyze DOM trees, and extract real-time web data!"><strong>Agentik Veb-Brauzing va Headless Scraping:</strong> Agentni Playwright orqali internetga chiqarish, DOM daraxtini tahlil qilish va ma'lumotlarni mustaqil yig'ish!</p>
      </div>
    </div>
  </section>
"""

# -----------------------------------------------------------------------------
# 2. IN-DECK INTERACTIVE SIMULATOR SCRIPT (Slide 8)
# -----------------------------------------------------------------------------
SIMULATOR_JS = """
// Slide 8: Interactive Coder-Runner-Critic Simulator
var deckAgentRunning = false;
var deckCurrentStep = 0;
var deckCycleTimer = null;

var TASK_DATA = {
  "fib": {
    "title": "Keshli Fibonacci",
    "step1_code": "def fib(n:\\n    if n <= 1: return n\\n    return fib(n-1) + fib(n-2) # XATO: Kesh yo'q, n=35 da qotadi",
    "step1_test": "FAIL: test_fib(35) timed out (> 3.0s)! O(2^N) eksponentsial xatolik.",
    "critic_msg": "DIAGNOZ: Rekursiya keshlanmagan. @functools.lru_cache(None) dekoratorini qo'shing yoki dict ishlating.",
    "step2_code": "from functools import lru_cache\\n\\n@lru_cache(maxsize=None)\\ndef fib(n: int) -> int:\\n    if n <= 1: return n\\n    return fib(n-1) + fib(n-2)",
    "step2_test": "SUCCESS: Barcha 4 ta test o'tdi (fib(10)=55, fib(35)=9227465, vaqt: 0.002s). 100% YASHIL!"
  },
  "rate_limiter": {
    "title": "Token Bucket Rate Limiter",
    "step1_code": "class Limiter:\\n    def __init__(self, cap): self.cap = cap\\n    def allow(self): self.cap -= 1; return self.cap >= 0 # XATO: Vaqt bo'yicha to'lish yo'q",
    "step1_test": "FAIL: test_refill() yiqildi! 2 soniya kutgandan keyin tokenlar to'lmadi.",
    "critic_msg": "DIAGNOZ: self.last_time va self.refill_rate hisobga olinmagan. Vaqt deltasini qo'shing.",
    "step2_code": "import time\\n\\nclass Limiter:\\n    def __init__(self, cap: int, rate: float):\\n        self.cap = cap; self.tokens = cap; self.rate = rate; self.last = time.time()\\n    def allow(self) -> bool:\\n        now = time.time()\\n        self.tokens = min(self.cap, self.tokens + (now - self.last) * self.rate)\\n        self.last = now\\n        if self.tokens >= 1:\\n            self.tokens -= 1; return True\\n        return False",
    "step2_test": "SUCCESS: Barcha 5 ta test o'tdi (Bursts, Refill rate, Zero capacity). 100% YASHIL!"
  },
  "lru": {
    "title": "LRU Kesh Tizimi",
    "step1_code": "class LRU:\\n    def __init__(self, cap): self.c = cap; self.d = {}\\n    def get(self, k): return self.d.get(k, -1)\\n    def put(self, k, v): self.d[k] = v # XATO: Cheklov yo'q",
    "step1_test": "FAIL: test_capacity_eviction() yiqildi! Kesh 2 ta elementdan oshib ketdi.",
    "critic_msg": "DIAGNOZ: Element eskirganini kuzatuvchi OrderedDict yoki Doubly-Linked List yo'q. Eng eski elementni o'chiring.",
    "step2_code": "from collections import OrderedDict\\n\\nclass LRU:\\n    def __init__(self, capacity: int):\\n        self.cap = capacity; self.cache = OrderedDict()\\n    def get(self, key: int) -> int:\\n        if key not in self.cache: return -1\\n        self.cache.move_to_end(key)\\n        return self.cache[key]\\n    def put(self, key: int, value: int) -> None:\\n        if key in self.cache: self.cache.move_to_end(key)\\n        self.cache[key] = value\\n        if len(self.cache) > self.cap: self.cache.popitem(last=False)",
    "step2_test": "SUCCESS: Barcha 6 ta test o'tdi (Eviction, Move to end, O(1) ops). 100% YASHIL!"
  }
};

function runDeckAgentCycle() {
  var term = document.getElementById('deckTerminal');
  var sel = document.getElementById('selTask').value;
  var task = TASK_DATA[sel];
  if (!task) return;

  var btn = document.getElementById('btnRunAgent');
  btn.disabled = true;
  btn.style.opacity = '0.5';

  term.innerHTML = '<div style="color:var(--accent);">▶️ Topshiriq: ' + task.title + ' boshlandi...</div>';
  document.getElementById('deckIter').textContent = '1 / 2';
  document.getElementById('deckTestStatus').textContent = 'Kod yozilmoqda...';
  document.getElementById('deckTestStatus').style.color = 'var(--accent)';

  // Step 1: Coder generates first draft
  setTimeout(function() {
    term.innerHTML += '<div style="color:#cbd5e1; margin-top:4px;">🧑‍💻 [Coder]: Boshlang‘ich kod generatsiya qilindi:</div>';
    term.innerHTML += '<pre style="background:#0f172a; padding:6px; color:#38bdf8; border-radius:4px; margin:2px 0;">' + task.step1_code + '</pre>';

    // Step 2: Sandbox runs tests
    setTimeout(function() {
      term.innerHTML += '<div style="color:var(--yellow); margin-top:4px;">⚡ [Sandbox Runner]: Testlar ishga tushirildi...</div>';
      term.innerHTML += '<div style="color:var(--red); font-weight:700;">' + task.step1_test + '</div>';
      document.getElementById('deckTestStatus').textContent = '❌ Test yiqildi';
      document.getElementById('deckTestStatus').style.color = 'var(--red)';

      // Step 3: Critic reflects
      setTimeout(function() {
        term.innerHTML += '<div style="color:var(--purple); margin-top:4px; font-weight:700;">🔍 [Critic]: ' + task.critic_msg + '</div>';
        document.getElementById('deckIter').textContent = '2 / 2';
        document.getElementById('deckTestStatus').textContent = 'Qayta tuzatilmoqda...';
        document.getElementById('deckTestStatus').style.color = 'var(--purple)';

        // Step 4: Coder self-corrects and passes!
        setTimeout(function() {
          term.innerHTML += '<div style="color:#cbd5e1; margin-top:4px;">🛠️ [Coder]: Critic ko‘rsatmasi bo‘yicha kod yangilandi:</div>';
          term.innerHTML += '<pre style="background:#0f172a; padding:6px; color:#10b981; border-radius:4px; margin:2px 0;">' + task.step2_code + '</pre>';
          term.innerHTML += '<div style="color:var(--green); font-weight:700; margin-top:4px;">' + task.step2_test + '</div>';
          document.getElementById('deckTestStatus').textContent = '✅ 100% YASHIL';
          document.getElementById('deckTestStatus').style.color = 'var(--green)';
          btn.disabled = false;
          btn.style.opacity = '1';
          term.scrollTop = term.scrollHeight;
        }, 1200);

      }, 1000);

    }, 900);

  }, 700);
}

function resetDeckAgent() {
  var term = document.getElementById('deckTerminal');
  term.innerHTML = '<div style="color:var(--accent); font-weight:700;">[Terminal: Avtonom Kod Agentlari Tizimi]</div><div style="color:#64748b;">Vazifani tanlang va "▶️ Agent Tsiklini Boshlash" tugmasini bosing...</div>';
  document.getElementById('deckIter').textContent = '0 / 3';
  document.getElementById('deckTestStatus').textContent = 'Kutilmoqda';
  document.getElementById('deckTestStatus').style.color = 'var(--ink)';
  var btn = document.getElementById('btnRunAgent');
  btn.disabled = false;
  btn.style.opacity = '1';
}

// Slide 10 Arena Countdown Timer
var arenaSeconds = 25 * 60;
var arenaTimerInterval = null;
function toggleArenaTimer() {
  var btn = document.getElementById('arenaTimerBtn');
  var display = document.getElementById('arenaTimerDisplay');
  if (arenaTimerInterval) {
    clearInterval(arenaTimerInterval);
    arenaTimerInterval = null;
    btn.textContent = '▶️ Davom Ettirish';
  } else {
    btn.textContent = '⏸️ To‘xtatish';
    arenaTimerInterval = setInterval(function() {
      if (arenaSeconds > 0) {
        arenaSeconds--;
        var m = Math.floor(arenaSeconds / 60);
        var s = arenaSeconds % 60;
        display.textContent = (m < 10 ? '0' : '') + m + ':' + (s < 10 ? '0' : '') + s;
      } else {
        clearInterval(arenaTimerInterval);
        display.textContent = '00:00 - VAQT TUGADI!';
      }
    }, 1000);
  }
}

// Slide 9 Quiz Feedback
function checkQuiz(btn, isCorrect, feedbackText) {
  var fb = document.getElementById('quizFeedback');
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

# Notes array for 14 slides (Strictly triplets [title, say, do])
NOTES_DATA = {
    "uz": [
        ["Kirish va Maqsad", "O'quvchilarga bugungi mavzu: Avtonom kod agentlari va TDD refleksiya tsikli haqida so'zlang.", "Doskaga Coder -> Runner -> Critic zanjirini chizing."],
        ["Uy Vazifasi Tahlili", "28-darsdagi Supervisor agentida FINISH sharti bo'lmaganda cheksiz sikl va token yonishi xatosini tushuntiring.", "Oltin yechim: recursion_limit va step guard ekanini ko'rsating."],
        ["One-Shot Muammosi", "Nega bitta prompt orqali olingan kod productionda yiqilishini tushuntiring.", "AST va runtime tekshiruvi yo'qligini tahlil qiling."],
        ["TDD Paradigmasi", "RED-GREEN-REFACTOR qoidasini tushuntiring. Nega testlar koddan oldin yozilishi shartligini ayting.", "PyTest misolini doskaga yozing."],
        ["Coder Arxitekturasi", "Coder agentining tizimli prompti va Type Hints cheklovlarini ko'rsating.", "Toza funksiyalar va docstringlar talabini ayting."],
        ["Sandbox Runner", "AI kodini host serverda emas, izolyatsiyalangan subprocess va timeout bilan bajarish xavfsizligini tushuntiring.", "Exit code 0 va 1 farqini ko'rsating."],
        ["Critic va Refleksiya", "Critic qanday qilib Tracebackdan xatolik ildizini topib, butun kodni o'chirmasdan tuzatishini tushuntiring.", "Diff ko'rsatmalarini tahlil qiling."],
        ["Smartboard Simulyatori", "Taqdimot ichidagi simulyatorda Fibonacci yoki Rate Limiter topshirig'ini ishga tushiring.", "Test yiqilishi, Critic tahlili va 100% yashil bo'lish jarayonini ko'rsating."],
        ["Bilimni Sinash (Quiz)", "3 ta nazorat savoli bo'yicha tezkor viktorina o'tkazing.", "Har bir javobni tahlil qiling."],
        ["25 Daqiqalik Arena", "O'quvchilarga simulator/index.html ni ochishni buyuring.", "Har bir partada Coder-Critic tsikli sozlanishini nazorat qiling."],
        ["Partadosh Auditi", "O'rin almashib, 4 ta mezon bo'yicha partadosh tizimini tekshirishsin.", "Cheksiz while sikli berilganda timeout ishlashini sinang."],
        ["Katta Ekran Showcasi", "Sinfdagi eng ilg'or Coder-Critic agentini katta doskada jonli sinovdan o'tkazing.", "Mualliflarni olqishlang."],
        ["3 Darajali Uy Vazifasi", "10 ballik uy vazifasi shartlarini tushuntiring.", "3-darajadagi nuqtali diff tuzatuvchi Critic topshirig'iga e'tibor qarating."],
        ["Xulosa va Keyingi Dars", "Darsni sarhisob qiling va keyingi darsda Playwright orqali veb-brauzing agentlarini o'rganishimizni e'lon qiling.", "O'quvchilar savollariga javob bering va uy vazifasi topshirilish muddatini eslating."]
    ],
    "ru": [
        ["Введение и Цель", "Представьте тему: автономные код-агенты, исполнение тестов в песочнице и цикл рефлексии.", "Нарисуйте на доске архитектуру Coder ➔ Runner ➔ Critic."],
        ["Разбор Домашнего Задания", "Объясните ловушку бесконечного пинг-понга сообщений без условия FINISH из 28-урока.", "Покажите золотой стандарт: recursion_limit и счетчик шагов."],
        ["Проблема One-Shot", "Объясните, почему разовый промпт генерирует внешне красивый, но нерабочий код.", "Разберите отсутствие среды исполнения (runtime) у LLM."],
        ["Парадигма TDD", "Разберите цикл RED-GREEN-REFACTOR для AI. Объясните, почему тесты пишутся первыми.", "Покажите пример модульного теста на доске."],
        ["Архитектура Coder", "Покажите системный промпт Coder с жесткими требованиями Type Hints и чистоты функций.", "Объясните запрет на разговорные фразы в коде."],
        ["Песочница Sandbox", "Объясните запуск непроверенного кода в изолированном subprocess с таймаутом 3.0 секунды.", "Покажите обработку Exit Code и логов stderr."],
        ["Критик и Рефлексия", "Покажите, как Critic анализирует трейсбек и выдает точечный диф без переписывания всего файла.", "Разберите локализацию корневой причины сбоя."],
        ["Интерактив на Доске", "Запустите встроенный в смартборд симулятор автономного агента.", "Продемонстрируйте падение первого теста и самоисправление."],
        ["Тест (Квиз)", "Проведите опрос по 3 контрольным вопросам.", "Разберите ошибки вместе с классом."],
        ["Практическая Арена (25 мин)", "Дайте команду открыть simulator/index.html.", "Курируйте создание графа Coder-Critic каждым учеником."],
        ["Взаимный Аудит", "Организуйте обмен местами за партами по чек-листу из 4 пунктов.", "Проверьте поведение песочницы на бесконечном цикле."],
        ["Шоукейс на Доске", "Выведите лучшую систему самовосстановления кода на интерактивную доску.", "Похвалите авторов."],
        ["Домашнее Задание", "Объясните 3 уровня 10-балльного домашнего задания.", "Обратите внимание на вызов 3-го уровня с точечным дифом."],
        ["Итоги и Анонс", "Подведите итоги урока и анонсируйте следующую тему: веб-агенты на Playwright и парсинг DOM.", "Ответьте на вопросы учеников и напомните дедлайн сдачи практического ДЗ."]
    ],
    "en": [
        ["Intro & Objectives", "Introduce autonomous coding agents, sandbox runners, and TDD reflection loops.", "Diagram the Coder ➔ Runner ➔ Critic pipeline on the whiteboard."],
        ["Homework Review", "Analyze the infinite message ping-pong deadlock when missing explicit FINISH states in Lesson 28.", "Demonstrate the golden solution: recursion_limit and step bounds."],
        ["One-Shot Coding Traps", "Discuss why single-shot code prompts crash in production despite looking plausible.", "Explain LLM token prediction versus runtime AST evaluation."],
        ["TDD Paradigm", "Break down the RED-GREEN-REFACTOR cycle for AI systems. Justify tests before code.", "Illustrate PyTest assertion mechanics on the board."],
        ["Coder Architecture", "Walk through Coder system prompts enforcing Type Hints and zero side-effects.", "Highlight clean code block parsing constraints."],
        ["Sandbox Runner", "Explain executing unvetted code inside isolated subprocesses with 3.0s timeouts.", "Contrast return codes 0 (pass) and 1 (assertion failure)."],
        ["Critic & Reflection", "Showcase how Critic dissects tracebacks to draft surgical patches without regression.", "Explain root cause diagnosis and diff delivery."],
        ["In-Deck Live Demo", "Trigger the in-deck dual-step agent simulator on the Smartboard.", "Observe test failures, traceback analysis, and self-correction."],
        ["Knowledge Check (Quiz)", "Lead the class through the 3 quick questions.", "Discuss each answer with the class."],
        ["Hands-on Arena (25 min)", "Instruct students to open simulator/index.html.", "Supervise student implementation of the Coder-Critic loop."],
        ["Peer Code Audit", "Facilitate seat swapping to audit agent systems using the 4-point rubric.", "Stress test sandbox timeout handling against infinite loops."],
        ["Showcase Arena", "Project the highest-performing autonomous coding agent onto the Smartboard.", "Celebrate student achievements."],
        ["Tiered Homework", "Explain the 3-tiered 10-point homework assignment.", "Highlight Tier 3's surgical patch prompt challenge."],
        ["Summary & Next Class", "Summarize core takeaways and preview Agentic Web Browsing via Playwright and DOM trees.", "Answer student questions and remind them of the homework lab deadline."]
    ]
}

def build_presentation():
    with open(os.path.join(REPO_ROOT, "assets", "TEMPLATE_PREZENTATSIYA.html"), "r", encoding="utf-8") as f:
        tpl = f.read()

    title_uz = "29-dars: Avtonom Kod Yozuvchi Agentlar: Coder, Critic va TDD Tsikli"
    title_ru = "Урок 29: Автономные Код-Агенты: Coder, Critic и Цикл TDD"
    title_en = "Lesson 29: Autonomous Coding Agents: Coder, Critic & TDD Reflection Loops"

    tpl = re.sub(r"<title[^>]*>.*?</title>",
                 f'<title data-ru="{title_ru}" data-en="{title_en}">{title_uz}</title>',
                 tpl)

    tpl = re.sub(r'<span class="tag"[^>]*>.*?</span>',
                 '<span class="tag" data-ru="10–11 КЛАСС" data-en="GRADES 10–11">10–11-SINF</span>',
                 tpl)

    titles_json = json.dumps({"uz": title_uz, "ru": title_ru, "en": title_en}, ensure_ascii=False, indent=2)
    tpl = re.sub(r'var TITLES\s*=\s*\{[\s\S]*?\};', f'var TITLES = {titles_json};', tpl)

    notes_json = json.dumps(NOTES_DATA, ensure_ascii=False, indent=2)
    tpl = re.sub(r'var NOTES\s*=\s*\{[\s\S]*?\};', f'var NOTES = {notes_json};', tpl)

    stage_regex = r'<div class="stage">[\s\S]*?</div><!-- /stage -->'
    new_stage = f'<div class="stage">\n{SLIDES_HTML}\n  </div><!-- /stage -->'
    tpl = re.sub(stage_regex, new_stage, tpl)

    custom_script = f"<script>\n{SIMULATOR_JS}\n</script>\n</body>"
    tpl = tpl.replace("</body>", custom_script)

    out_path = os.path.join(DEST_DIR, "prezentatsiya.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(tpl)
    print("  ✓ Created: prezentatsiya.html")

def build_worksheet():
    with open(os.path.join(REPO_ROOT, "assets", "TEMPLATE_VARAQA.html"), "r", encoding="utf-8") as f:
        tpl = f.read()

    title_uz = "29-dars: Avtonom Kod Yozuvchi Agentlar: Coder, Critic va TDD Tsikli"
    title_ru = "Урок 29: Автономные Код-Агенты: Coder, Critic и Цикл TDD"
    title_en = "Lesson 29: Autonomous Coding Agents: Coder, Critic & TDD Reflection Loops"

    tpl = re.sub(r"<title[^>]*>.*?</title>",
                 f'<title data-ru="{title_ru}" data-en="{title_en}">{title_uz}</title>',
                 tpl)

    tpl = re.sub(r'<h1>.*?</h1>',
                 f'<h1 data-ru="{title_ru}" data-en="{title_en}">{title_uz}</h1>',
                 tpl)

    sec1_html = """
    <p class="lead" style="font-size:12px; margin-bottom:8px;" data-ru="<strong>Миссия Урока:</strong> Спроектировать и запрограммировать замкнутую мультиагентную систему Coder ➔ Runner ➔ Critic, способную автономно писать функции, запускать PyTest в песочнице и исправлять баги до 100% прохождения тестов." data-en="<strong>Lesson Mission:</strong> Architect and program a closed-loop Coder ➔ Runner ➔ Critic multi-agent system that writes typed Python functions, executes PyTest suites in an isolated sandbox, and self-corrects bugs to 100% green tests."><strong>Dars Missiyasi:</strong> Coder ➔ Runner ➔ Critic zanjiridan iborat avtonom multi-agent tizimini qurish: kod generatsiyasi, testlarni xavfsiz sandboxda run qilish va xatolarni inson aralashuvisiz tuzatish.</p>
    <div style="background:var(--surface-2); padding:8px; border-radius:6px; font-size:11px; line-height:1.5;">
      <div style="font-weight:700; color:var(--accent); margin-bottom:4px;" data-ru="3 Фазы TDD Рефлексии:" data-en="3 Phases of TDD Reflection:">TDD Refleksiyasining 3 Bosqichi:</div>
      <div>1. <strong>RED (Qizil):</strong> <span data-ru="Написание строгих PyTest-тестов до кода реализации" data-en="Drafting strict PyTest suites defining edge cases prior to code">Amalga oshirishdan oldin chekka holatlar uchun qat'iy testlar yozish</span>.</div>
      <div>2. <strong>GREEN (Yashil):</strong> <span data-ru="Coder генерирует код с Type Hints под прохождение тестов" data-en="Coder drafts typed implementation satisfying failing assertions">Coder testlardan o'tish uchun toza Type Hints bilan kod yozadi</span>.</div>
      <div>3. <strong>REFACTOR / HEAL:</strong> <span data-ru="Critic анализирует трейсбек и выдает точечный патч без регрессий" data-en="Critic parses tracebacks and guides surgical diffs without regression">Critic xato qatorini aniqlab, boshqa testlarni buzmasdan tuzatadi</span>.</div>
    </div>
    """

    sec2_html = """
    <p style="font-size:11px; margin-bottom:6px;" data-ru="Архитектура безопасного запуска тестов в песочнице:" data-en="Architecture of isolated sandbox test runner:">Xavfsiz sandbox muhitida testlarni ishga tushirish kodi:</p>
    <pre style="background:var(--surface-2); padding:6px; font-size:11px; border-radius:4px; margin:0;"><code class="language-python">import subprocess

def run_tests_safe(code_str: str, test_str: str) -> dict:
    full_script = f"{code_str}\\n\\n{test_str}"
    res = subprocess.run(
        ["python3", "-c", full_script],
        capture_output=True, text=True,
        timeout=3.0 # Timeout guard protiv while True
    )
    return {"ok": res.returncode == 0, "stderr": res.stderr}</code></pre>
    """

    sec3_html = """
    <div style="overflow-x:auto;">
      <table style="width:100%; border-collapse:collapse; font-size:11px; text-align:left;">
        <thead>
          <tr style="border-bottom:1px solid var(--hair); background:rgba(0,0,0,0.03);">
            <th style="padding:4px 6px;">#</th>
            <th style="padding:4px 6px;" data-ru="Агент / Модуль" data-en="Agent / Node">Agent / Modul</th>
            <th style="padding:4px 6px;" data-ru="Входные Данные" data-en="Inputs">Kiruvchi Ma'lumot</th>
            <th style="padding:4px 6px;" data-ru="Выходной Артефакт" data-en="Output Artifact">Chiquvchi Natija</th>
            <th style="padding:4px 6px;" data-ru="Статус" data-en="Status">Holat</th>
          </tr>
        </thead>
        <tbody>
          <tr style="border-bottom:1px dashed var(--hair);">
            <td style="padding:4px 6px;">1</td>
            <td style="padding:4px 6px;" data-ru="Tester Agent" data-en="Tester Agent"><code>Tester Agent</code></td>
            <td style="padding:4px 6px;" data-ru="Техническое Задание (PRD)" data-en="Feature Specs">Texnik topshiriq (PRD)</td>
            <td style="padding:4px 6px;" data-ru="Набор тестов PyTest (RED)" data-en="PyTest assertions (RED)">Qat'iy PyTest to'plami</td>
            <td style="padding:4px 6px;" data-ru="[ &nbsp; ] Настроен" data-en="[ &nbsp; ] Configured">[ &nbsp; ] Sozlandi</td>
          </tr>
          <tr style="border-bottom:1px dashed var(--hair);">
            <td style="padding:4px 6px;">2</td>
            <td style="padding:4px 6px;" data-ru="Coder Agent" data-en="Coder Agent"><code>Coder Agent</code></td>
            <td style="padding:4px 6px;" data-ru="Тесты + Замечания Critic" data-en="Tests + Critic Feedback">Testlar + Critic tahlili</td>
            <td style="padding:4px 6px;" data-ru="Python-модуль с Type Hints" data-en="Typed Python module">Typed Python kodi</td>
            <td style="padding:4px 6px;" data-ru="[ &nbsp; ] Настроен" data-en="[ &nbsp; ] Configured">[ &nbsp; ] Sozlandi</td>
          </tr>
          <tr style="border-bottom:1px dashed var(--hair);">
            <td style="padding:4px 6px;">3</td>
            <td style="padding:4px 6px;" data-ru="Sandbox Runner" data-en="Sandbox Runner"><code>Sandbox Runner</code></td>
            <td style="padding:4px 6px;" data-ru="Код + Тесты" data-en="Code + Test suite">Kod + Testlar</td>
            <td style="padding:4px 6px;" data-ru="Exit Code, stdout, stderr" data-en="Exit code, stdout, stderr">Natija va Traceback</td>
            <td style="padding:4px 6px;" data-ru="[ &nbsp; ] Настроен" data-en="[ &nbsp; ] Configured">[ &nbsp; ] Sozlandi</td>
          </tr>
          <tr>
            <td style="padding:4px 6px;">4</td>
            <td style="padding:4px 6px;" data-ru="Critic Reflector" data-en="Critic Reflector"><code>Critic Reflector</code></td>
            <td style="padding:4px 6px;" data-ru="Трейсбек ошибки" data-en="Error traceback">Yiqilgan test logi</td>
            <td style="padding:4px 6px;" data-ru="Точечный патч-инструкция" data-en="Surgical patch guidance">Nuqtali tuzatish ko'rsatmasi</td>
            <td style="padding:4px 6px;" data-ru="[ &nbsp; ] Настроен" data-en="[ &nbsp; ] Configured">[ &nbsp; ] Sozlandi</td>
          </tr>
        </tbody>
      </table>
    </div>
    """

    sec4_html = """
    <p style="font-size:11px; margin-bottom:6px;" data-ru="Спроектируйте граф состояний LangGraph для цикла Coder-Critic:" data-en="Draft the LangGraph StateGraph topology for the Coder-Critic reflection loop:">Coder-Critic zanjirining holat grafigini to'ldiring:</p>
    <div style="border:1px dashed var(--hair); padding:8px; border-radius:4px; font-family:var(--font-mono); font-size:11px; line-height:1.6;">
      <div>State: {"code": str, "tests": str, "logs": str, "iterations": int}</div>
      <div style="margin-top:4px;">START ➔ [Tester] ➔ [Coder] ➔ [SandboxRunner]</div>
      <div style="margin-top:2px;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;│</div>
      <div>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Shartli Qirra (Conditional Edge)]</div>
      <div>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├── agar ok == True ➔ END (Muvaffaqiyat!)</div>
      <div>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├── agar iterations >= 3 ➔ Human-in-the-Loop</div>
      <div>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└── agar ok == False ➔ [Critic] ➔ [Coder] (Qayta!)</div>
    </div>
    """

    sec5_html = """
    <div style="font-size:11px; line-height:1.6;">
      <div>[ &nbsp; ] <strong>4 Ball (Baza):</strong> Coder toza Type Hints bilan boshlang'ich kodni xatolarsiz generatsiya qildi.</div>
      <div>[ &nbsp; ] <strong>4 Ball (Amaliy):</strong> Sandbox Runner xavfsiz subprocess orqali testlarni run qilib, STDERR tahlilini uzatdi.</div>
      <div>[ &nbsp; ] <strong>2 Ball (Challenge):</strong> Critic yiqilgan test ildizini topib, 2-urinishda inson aralashuvisiz 100% yashil testlarga erishdi!</div>
      <div style="margin-top:6px; border-top:1px solid var(--hair); padding-top:4px; font-weight:700; color:var(--accent);" data-ru="Итоговый балл: _____ / 10 &nbsp; Подпись учителя: ____________" data-en="Total Score: _____ / 10 &nbsp; Teacher Signature: ____________">Jami to'plangan ball: _____ / 10 &nbsp; O'qituvchi imzosi: ____________</div>
    </div>
    """

    replacements = {
        "{{LESSON_NUM}}": "29",
        "{{TITLE_UZ}}": "Avtonom Kod Yozuvchi Agentlar: Coder, Critic va TDD Tsikli",
        "{{TITLE_RU}}": "Автономные Код-Агенты: Coder, Critic и Цикл TDD",
        "{{TITLE_EN}}": "Autonomous Coding Agents: Coder, Critic & TDD Reflection Loops",
        "{{COHORT_LABEL_UZ}}": "10–11-SINF",
        "{{COHORT_LABEL_RU}}": "10–11 КЛАСС",
        "{{COHORT_LABEL_EN}}": "GRADES 10–11",
        "{{META_UZ}}": "11-Hafta · Juftlik Dars (80 daqiqa) · Senior AI & Enterprise Track",
        "{{META_RU}}": "11-я Неделя · Сдвоенный Урок (80 минут) · Направление Senior AI",
        "{{META_EN}}": "Week 11 · Double Block (80 min) · Senior AI & Enterprise Track",
        "{{MISSION_UZ}}": "Coder ➔ Runner ➔ Critic zanjiridan iborat avtonom multi-agent tizimini qurish: qat'iy PyTest testlarini yozish, kod generatsiyasi, testlarni xavfsiz sandboxda run qilish va yiqilgan testlarni inson aralashuvisiz tuzatib 100% yashil natijaga erishish.",
        "{{MISSION_RU}}": "Спроектировать замкнутую мультиагентную систему Coder ➔ Runner ➔ Critic: генерация типизированного кода, изолированный запуск тестов в песочнице и автономное исправление багов до 100% прохождения тестов.",
        "{{MISSION_EN}}": "Architect and program a closed-loop Coder ➔ Runner ➔ Critic multi-agent system: typed code generation, isolated sandbox execution, and autonomous traceback reflection achieving 100% green tests.",
        "{{SEC1_TITLE_UZ}}": "TDD Refleksiyasining 3 Bosqichi (RED ➔ GREEN ➔ REFACTOR)",
        "{{SEC1_TITLE_RU}}": "3 Фазы TDD Рефлексии (RED ➔ GREEN ➔ REFACTOR)",
        "{{SEC1_TITLE_EN}}": "3 Phases of TDD Reflection (RED ➔ GREEN ➔ REFACTOR)",
        "{{SEC1_CONTENT}}": sec1_html,
        "{{SEC2_TITLE_UZ}}": "Izolyatsiyalangan Sandbox Test Runner Arxitekturasi",
        "{{SEC2_TITLE_RU}}": "Архитектура Изолированной Песочницы Test Runner",
        "{{SEC2_TITLE_EN}}": "Isolated Sandbox Test Runner Architecture",
        "{{SEC2_CONTENT}}": sec2_html,
        "{{SEC3_TITLE_UZ}}": "Coder-Critic Agentlar Rol Matritsasi",
        "{{SEC3_TITLE_RU}}": "Матрица Ролей Агентов Coder-Critic",
        "{{SEC3_TITLE_EN}}": "Coder-Critic Agent Role Matrix",
        "{{SEC3_CONTENT}}": sec3_html + sec4_html,
        "{{SEC4_CONTENT}}": sec5_html
    }

    for k, v in replacements.items():
        tpl = tpl.replace(k, v)

    out_path = os.path.join(DEST_DIR, "varaqa.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(tpl)
    print("  ✓ Created: varaqa.html")

def build_homework():
    with open(os.path.join(REPO_ROOT, "assets", "TEMPLATE_VAZIFA.html"), "r", encoding="utf-8") as f:
        tpl = f.read()

    title_uz = "29-dars: Avtonom Kod Yozuvchi Agentlar: Coder, Critic va TDD Tsikli"
    title_ru = "Урок 29: Автономные Код-Агенты: Coder, Critic и Цикл TDD"
    title_en = "Lesson 29: Autonomous Coding Agents: Coder, Critic & TDD Reflection Loops"

    tpl = re.sub(r"<title[^>]*>.*?</title>",
                 f'<title data-ru="{title_ru}" data-en="{title_en}">{title_uz}</title>',
                 tpl)

    tasks_html = """
    <!-- TIER 1 (4 BALL) -->
    <div class="task-card" style="margin-bottom:14px; border:1px solid var(--hair); border-radius:6px; padding:12px; background:var(--surface);">
      <div class="tag" style="background:rgba(59,130,246,0.15); color:var(--accent);">1-Daraja (Baza — 4 Ball)</div>
      <h3 style="margin:4px 0;" data-ru="TDD Спецификация и Модульные Тесты" data-en="TDD Specification & PyTest Assertions">TDD Spetsifikatsiyasi va Qat'iy Testlar</h3>
      <p style="font-size:12px; color:var(--ink-2);" data-ru="Напишите 3 строгих модульных теста на PyTest для функции validate_email(email: str) -> bool, проверяющих валидный email, отсутствие символа '@' и недопустимые домены." data-en="Write 3 strict PyTest assertions for validate_email(email: str) -> bool covering valid formats, missing '@' symbols, and invalid domain extensions."><code>validate_email(email: str) -> bool</code> funksiyasi uchun 3 ta qat'iy PyTest testini yozing (to'g'ri email, '@' belgisi yo'qligi va noto'g'ri domen holatlari).</p>
      <textarea class="answer-area" id="ans_task_1" rows="6" placeholder="PyTest kodingizni bu yerga yozing..." data-placeholder-ru="Напишите тесты PyTest здесь..." data-placeholder-en="Write your PyTest code here..." oninput="saveAnswers()"></textarea>
      <div class="solution-box" id="sol_task_1" style="display:none; margin-top:8px; padding:8px; background:rgba(16,185,129,0.08); border-left:3px solid var(--green); font-size:11px; font-family:var(--font-mono);">
        <strong>Namunaviy Yechim:</strong><br>
        <code>def test_valid_email(): assert validate_email("user@target.uz") == True</code><br>
        <code>def test_missing_at(): assert validate_email("usertarget.uz") == False</code><br>
        <code>def test_empty_string(): assert validate_email("") == False</code>
      </div>
    </div>

    <!-- TIER 2 (4 BALL) -->
    <div class="task-card" style="margin-bottom:14px; border:1px solid var(--hair); border-radius:6px; padding:12px; background:var(--surface);">
      <div class="tag" style="background:rgba(147,51,234,0.15); color:var(--purple);">2-Daraja (Amaliy — 4 Ball)</div>
      <h3 style="margin:4px 0;" data-ru="Безопасная Песочница: safe_runner() с Таймаутом" data-en="Sandbox Runner: safe_runner() with Timeout">Xavfsiz Sandbox: safe_runner() va Timeout</h3>
      <p style="font-size:12px; color:var(--ink-2);" data-ru="Напишите функцию safe_runner(code_str: str, timeout: float = 2.0) -> dict на Python, которая запускает код в отдельном процессе через subprocess.run, перехватывает STDERR и возвращает {'ok': bool, 'error': str}." data-en="Implement safe_runner(code_str: str, timeout: float = 2.0) -> dict in Python executing code in subprocess, capturing STDERR and returning {'ok': bool, 'error': str}.">Python <code>subprocess.run</code> yordamida 2 soniyalik timeout bilan kodni xavfsiz run qiluvchi va STDERR loglarini qaytaruvchi <code>safe_runner()</code> funksiyasini yozing.</p>
      <textarea class="answer-area" id="ans_task_2" rows="7" placeholder="safe_runner funksiyasini bu yerga yozing..." data-placeholder-ru="Напишите функцию safe_runner здесь..." data-placeholder-en="Write safe_runner function here..." oninput="saveAnswers()"></textarea>
      <div class="solution-box" id="sol_task_2" style="display:none; margin-top:8px; padding:8px; background:rgba(16,185,129,0.08); border-left:3px solid var(--green); font-size:11px; font-family:var(--font-mono);">
        <strong>Namunaviy Yechim:</strong><br>
        <code>import subprocess</code><br>
        <code>def safe_runner(code_str: str, timeout: float = 2.0) -> dict:</code><br>
        <code>&nbsp;&nbsp;try:</code><br>
        <code>&nbsp;&nbsp;&nbsp;&nbsp;res = subprocess.run(["python3", "-c", code_str], capture_output=True, text=True, timeout=timeout)</code><br>
        <code>&nbsp;&nbsp;&nbsp;&nbsp;return {"ok": res.returncode == 0, "error": res.stderr}</code><br>
        <code>&nbsp;&nbsp;except subprocess.TimeoutExpired:</code><br>
        <code>&nbsp;&nbsp;&nbsp;&nbsp;return {"ok": False, "error": "TimeoutExpired: kod 2.0 soniyadan ko'p vaqt oldi!"}</code>
      </div>
    </div>

    <!-- TIER 3 (2 BALL) -->
    <div class="task-card" style="margin-bottom:14px; border:1px solid var(--hair); border-radius:6px; padding:12px; background:var(--surface);">
      <div class="tag" style="background:rgba(16,185,129,0.15); color:var(--green);">3-Daraja (Challenge — 2 Ball)</div>
      <h3 style="margin:4px 0;" data-ru="Агент Critic: Точечный Диф Без Перезаписи" data-en="Critic Agent: Surgical Diff Patching">Critic Agenti: Nuqtali Diff va O'z-O'zini Tuzatish</h3>
      <p style="font-size:12px; color:var(--ink-2);" data-ru="Составьте системный промпт для Critic, который получает трейсбек ошибки и требует от Coder исправить ТОЛЬКО конкретную строку с багом, запрещая переписывать рабочие функции." data-en="Design a Critic system prompt that takes failing tracebacks and forces Coder to patch strictly the offending line without rewriting operational logic.">Yiqilgan test logini olib, Coderga butun faylni o'chirmasdan faqat xato ketgan aniq 1 qatorni to'g'rilashni talab qiluvchi Critic tizimli promptini tuzing.</p>
      <textarea class="answer-area" id="ans_task_3" rows="6" placeholder="Critic promptini bu yerga yozing..." data-placeholder-ru="Напишите промпт Critic здесь..." data-placeholder-en="Write Critic prompt here..." oninput="saveAnswers()"></textarea>
      <div class="solution-box" id="sol_task_3" style="display:none; margin-top:8px; padding:8px; background:rgba(16,185,129,0.08); border-left:3px solid var(--green); font-size:11px; font-family:var(--font-mono);">
        <strong>Namunaviy Yechim:</strong><br>
        <code>Siz qat'iy Code Reviewer va Critic agentsiz.</code><br>
        <code>Vazifangiz: Berilgan Tracebackni tahlil qilib, xatolik keltirib chiqargan qatorni aniqlash.</code><br>
        <code>Coderga ko'rsatma: Faqat xatolik yuz bergan funksiyaga minimal 'if' shartini qo'shing. Boshqa ishlayotgan testlarni aslo o'zgartirmang!</code>
      </div>
    </div>
    """

    replacements = {
        "{{TITLE_UZ}}": "29-dars: Avtonom Kod Yozuvchi Agentlar: Coder, Critic va TDD Tsikli",
        "{{TITLE_RU}}": "Урок 29: Автономные Код-Агенты: Coder, Critic и Цикл TDD",
        "{{TITLE_EN}}": "Lesson 29: Autonomous Coding Agents: Coder, Critic & TDD Reflection Loops",
        "{{COHORT_LABEL_UZ}}": "10–11-SINF",
        "{{HERO_TAG_UZ}}": "11-Hafta · Senior AI & Enterprise Track",
        "{{HERO_DESC_UZ}}": "Avtonom dasturchi agentlar (Coder-Runner-Critic) zanjirini qurish, TDD testlarini avtomatlashtirish va xatolarni mustaqil tuzatuvchi tizimlar bo'yicha 3 darajali topshiriqlar.",
        "{{HERO_DESC_RU}}": "Построение замкнутой цепочки код-агентов (Coder-Runner-Critic), автоматизация тестов TDD и самовосстановление кода.",
        "{{HERO_DESC_EN}}": "Architecting autonomous code agents (Coder-Runner-Critic), automating TDD suites, and engineering self-healing code loops across 3 tiers.",
        "{{RUBRIC_T1_UZ}}": "1-Bosqich: Baza (TDD va PyTest testlari)",
        "{{RUBRIC_T1_RU}}": "1-й Уровень: База (Спецификация TDD и тесты PyTest)",
        "{{RUBRIC_T1_EN}}": "Tier 1: Base (TDD specification & PyTest assertions)",
        "{{RUBRIC_T2_UZ}}": "2-Bosqich: Amaliyot (Izolyatsiyalangan Sandbox Runner)",
        "{{RUBRIC_T2_RU}}": "2-й Уровень: Практика (Песочница Subprocess с таймаутом)",
        "{{RUBRIC_T2_EN}}": "Tier 2: Practice (Isolated subprocess sandbox with timeout)",
        "{{RUBRIC_T3_UZ}}": "3-Bosqich: Kiber-Chaqiruv (Critic prompti va nuqtali diff)",
        "{{RUBRIC_T3_RU}}": "3-й Уровень: Вызов (Промпт Критика с точечным diff)",
        "{{RUBRIC_T3_EN}}": "Tier 3: Challenge (Critic prompt with surgical diff)",
        "{{TASKS_HTML}}": tasks_html,
        "{{LESSON_SLUG}}": "10-11-w11-l29-avtonom-kod-agentlari-va-tdd"
    }

    for k, v in replacements.items():
        tpl = tpl.replace(k, v)

    out_path = os.path.join(DEST_DIR, "vazifa.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(tpl)
    print("  ✓ Created: vazifa.html")

def build_teacher_reading():
    doc = """# 29-dars: Avtonom Kod Yozuvchi Agentlar: Coder, Critic va TDD Tsikli (O'qituvchi Metodologiyasi)

## Darsning Pasporti
- **Sinf:** 10–11-sinf (Senior AI & Enterprise Architecture Track)
- **Davomiyligi:** 80 daqiqa (Juftlik Dars / Double Block)
- **Asosiy maqsad:** O'quvchilarga LLM ko'r-ko'rona kod yozishidan Test-Driven Development (TDD) asosidagi avtonom o'z-o'zini tuzatuvchi tizimlarga o'tishni o'rgatish. Coder (kod generatsiyasi), Sandbox Runner (xavfsiz test bajarilishi) va Critic (traceback tahlili va nuqtali diff tuzatish) arxitekturasini kodlash.

---

## 80 Daqiqalik Aniq Vaqt Taqsimoti (Pacing)

### 1-Qism: Nazariya, Xatolar Tahlili va Jonli Test (40 daqiqa)
| Vaqt | Bosqich | Slayd | O'qituvchi Faoliyati | O'quvchilar Faoliyati |
|---|---|:---:|---|---|
| **00:00–04:00** | Kirish va Motivatsiya | 1 | TDD va avtonom kod agentlari nima uchun enterprise standart ekanini tushuntirish. | Diqqat bilan tinglaydilar va dars maqsadini belgilaydilar. |
| **04:00–12:00** | 28-dars HW Tahlili | 2 | Supervisor agentida FINISH sharti bo'lmaganda cheksiz token sarflanishi xatosini tahlil qilish. | Blitz savolga javob beradilar, loop guard qoidasini yozib oladilar. |
| **12:00–18:00** | One-Shot Muammosi | 3 | Nega bitta prompt bilan olingan kod productionda yiqilishini ko'rsatish (AST va runtime yo'qligi). | Real arxitektura kamchiliklarini tushunadilar. |
| **18:00–24:00** | TDD Paradigmasi | 4 | RED ➔ GREEN ➔ REFACTOR zanjirini tushuntirish. Nega testlar koddan oldin yozilishini asoslash. | PyTest sintaksisini eslab qoladilar. |
| **24:00–30:00** | Coder Arxitekturasi | 5 | Coder tizimli prompti, Type Hints va toza funksiyalar talabini tushuntirish. | Coder cheklovlarini ko'rib chiqadilar. |
| **30:00–35:00** | Sandbox Runner | 6 | Xavfsiz subprocess, exit code 0/1 va 3.0s timeout mexanizmini ko'rsatish. | Host xavfsizligi nega muhimligini anglaydilar. |
| **35:00–40:00** | Critic va Refleksiya | 7 | Tracebackdan Root Cause topish va nuqtali diff generatsiyasini o'rgatish. | Qayta noldan yozmaslik tamoyilini o'rganadilar. |

### 2-Qism: Smartboard Sinovi, Katta Arena va Showcase (40 daqiqa)
| Vaqt | Bosqich | Slayd | O'qituvchi Faoliyati | O'quvchilar Faoliyati |
|---|---|:---:|---|---|
| **40:00–48:00** | Smartboard Simulyatori | 8 | Slayddagi Coder-Runner-Critic tsiklini doskada ishga tushirish (Fibonacci / Rate Limiter). | 1-urinishda yiqilish, Critic tahlili va yashil bo'lishni kuzatadilar. |
| **48:00–55:00** | Viktorina (Quiz) | 9 | 3 ta nazorat savoli bo'yicha viktorina o'tkazish. | Faol javob beradilar va o'z bilimlarini tekshiradilar. |
| **55:00–70:00** | 25 Daqiqalik Arena | 10 | 25:00 taymerni yoqish, partalar bo'ylab yurib ko'maklashish. | simulator/index.html da o'z Coder-Critic agentlarini dasturlaydilar. |
| **70:00–74:00** | Partadosh Auditi | 11 | O'rin almashishni e'lon qilish, 4 mezonli sinovni nazorat qilish. | Bir-birining tizimiga cheksiz sikl berib, timeoutni tekshiradilar. |
| **74:00–77:00** | Katta Ekran Showcasi | 12 | Eng zo'r avtonom agentni katta doskaga chiqarib jonli test qilish. | Sinfdoshlari natijasini tahlil qiladilar. |
| **77:00–80:00** | Uy Vazifasi va Yakun | 13–14 | 10 ballik uy vazifasini tushuntirish va Playwright veb-agentlariga ko'prik! | Kundaliklariga vazifani belgilaydilar. |

---

## O'qituvchi Uchun Muhim Blitz Savollari
1. **"Nega test yiqilganda Coderga butun kodni noldan qayta yozdirish xavfli?"**
   - Javob: Chunki model ilgari muvaffaqiyatli o'tgan boshqa testlarni buzib qo'yishi (regression) va yana yangi gallyutsinatsiyalar kiritishi mumkin. Critic faqat xato qatorni nuqtali tuzatishi shart.
2. **"Sandboxda subprocess nima uchun timeout bilan o'ralishi kerak?"**
   - Javob: Agar model xatoni tuzatish paytida `while True` yoki qotuvchi rekursiya kiritib qo'ysa, server abadiy muzlab qolmasligi uchun SIGKILL beriladi.

---

## 10 Ballik Baholash Rubrikasi
- **4 Ball (Baza):** Coder Type Hints bilan toza Python kodini generatsiya qiladi.
- **4 Ball (Amaliy):** Sandbox Runner xavfsiz muhitda testlarni bajaradi va stderr tracebackni ajratadi.
- **2 Ball (Challenge):** Critic xatoni aniqlab, 2-urinishda inson aralashuvisiz kodni 100% yashil testlarga yetkazadi!
"""
    out_path = os.path.join(DEST_DIR, "TEACHER_READING.md")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(doc)
    print("  ✓ Created: TEACHER_READING.md")

def build_simulator():
    html = """<!DOCTYPE html>
<html lang="uz">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title data-ru="Лаборатория Автономных Код-Агентов (TDD Loop)" data-en="Autonomous Coding Agents Lab (TDD Loop)">Avtonom Kod Agentlari Studiyasi (TDD Loop)</title>
  <style>
    :root {
      --bg: #090d16;
      --surface: #131b2e;
      --surface-2: #1e293b;
      --ink: #f8fafc;
      --ink-2: #94a3b8;
      --accent: #38bdf8;
      --green: #10b981;
      --red: #ef4444;
      --yellow: #f59e0b;
      --purple: #a855f7;
      --font: system-ui, -apple-system, sans-serif;
      --font-mono: 'JetBrains Mono', monospace, Consolas, monospace;
    }
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      background: var(--bg);
      color: var(--ink);
      font-family: var(--font);
      height: 100vh;
      display: flex;
      flex-direction: column;
      overflow: hidden;
    }
    header {
      background: var(--surface);
      border-bottom: 1px solid rgba(255,255,255,0.08);
      padding: 10px 20px;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }
    .brand {
      display: flex;
      align-items: center;
      gap: 10px;
      font-weight: 700;
      font-size: 16px;
      color: var(--accent);
    }
    .hud {
      display: flex;
      gap: 14px;
      align-items: center;
      font-weight: 700;
      font-size: 13px;
    }
    .hud-badge {
      background: var(--surface-2);
      padding: 6px 12px;
      border-radius: 6px;
      display: flex;
      align-items: center;
      gap: 6px;
    }
    main {
      flex: 1;
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 14px;
      padding: 14px;
      overflow: hidden;
    }
    .pane {
      background: var(--surface);
      border: 1px solid rgba(255,255,255,0.08);
      border-radius: 10px;
      display: flex;
      flex-direction: column;
      overflow: hidden;
    }
    .pane-header {
      background: var(--surface-2);
      padding: 8px 14px;
      font-weight: 700;
      font-size: 12px;
      color: var(--accent);
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-bottom: 1px solid rgba(255,255,255,0.05);
    }
    .editor-body {
      flex: 1;
      background: #020617;
      padding: 12px;
      font-family: var(--font-mono);
      font-size: 11px;
      line-height: 1.6;
      color: #38bdf8;
      overflow-y: auto;
      white-space: pre-wrap;
    }
    .terminal-body {
      flex: 1;
      background: #000;
      padding: 12px;
      font-family: var(--font-mono);
      font-size: 11px;
      line-height: 1.5;
      color: #e2e8f0;
      overflow-y: auto;
      display: flex;
      flex-direction: column;
      gap: 8px;
    }
    .btn {
      background: var(--accent);
      color: #000;
      border: none;
      border-radius: 6px;
      padding: 8px 14px;
      font-weight: 700;
      cursor: pointer;
      font-size: 12px;
      transition: all 0.2s;
    }
    .btn:hover { opacity: 0.9; transform: scale(1.02); }
    .btn-green { background: var(--green); color: #fff; }
    .btn-gray { background: #334155; color: #fff; }
    .footer-bar {
      background: var(--surface);
      border-top: 1px solid rgba(255,255,255,0.08);
      padding: 10px 20px;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }
  </style>
</head>
<body>

<header>
  <div class="brand">
    <span>🤖 Autonomous Coding Agent: Coder ➔ Runner ➔ Critic</span>
    <span style="font-size:11px; background:rgba(56,189,248,0.15); color:var(--accent); padding:2px 8px; border-radius:12px;">10–11-Sinf</span>
  </div>
  <div class="hud">
    <div class="hud-badge">🔄 Iteratsiya: <strong id="hudIter" style="color:var(--purple); font-size:14px;">0 / 3</strong></div>
    <div class="hud-badge">⚡ Status: <strong id="hudStatus" style="color:var(--yellow); font-size:14px;">Kutilmoqda</strong></div>
    <div class="hud-badge">🛡️ Testlar: <strong id="hudTests" style="color:var(--ink); font-size:14px;">0 / 5</strong></div>
  </div>
</header>

<main>
  <!-- Left Pane: Code & AST View -->
  <div class="pane">
    <div class="pane-header">
      <span data-ru="Сгенерированный Код (Coder Node)" data-en="Generated Source (Coder Node)">📄 Coder Generatsiya Qilgan Kod (Python)</span>
      <span id="codeLangBadge" style="font-size:10px; background:#0f172a; padding:2px 6px; border-radius:4px; color:var(--green);">Typed Python 3.11</span>
    </div>
    <div class="editor-body" id="codeView"># Coder kodi shu yerda real vaqtda paydo bo'ladi...
# "▶️ Agent Tsiklini Boshlash" tugmasini bosing!</div>
  </div>

  <!-- Right Pane: Terminal & Critic Diagnosis -->
  <div class="pane">
    <div class="pane-header">
      <span data-ru="Изолированный Sandbox и Трейсбек Critic" data-en="Isolated Sandbox & Critic Diagnosis">⚡ Sandbox Terminali & Critic Diagnostikasi</span>
      <span id="runnerBadge" style="font-size:10px; background:#0f172a; padding:2px 6px; border-radius:4px; color:var(--accent);">Timeout: 3.0s</span>
    </div>
    <div class="terminal-body" id="termView">
      <div style="color:#64748b;">[Sandbox tayyor] Vazifani tanlang va avtonom TDD tsiklini ishga tushiring.</div>
    </div>
  </div>
</main>

<div class="footer-bar">
  <div style="display:flex; gap:10px; align-items:center;">
    <label style="font-size:12px; font-weight:700;" data-ru="Задача:" data-en="Challenge:">Vazifa:</label>
    <select id="selTask" style="background:var(--surface-2); color:#fff; border:1px solid #334155; border-radius:4px; padding:6px 10px; font-size:12px;">
      <option value="fib" data-ru="Кэшированный Фибоначчи (O(N) против O(2^N))" data-en="Cached Fibonacci (O(N) vs O(2^N))">Keshli Fibonacci (O(N) vaqt)</option>
      <option value="rate_limiter" data-ru="Token Bucket Rate Limiter (Алгоритм ограничения частоты)" data-en="Token Bucket Rate Limiter">Token Bucket Rate Limiter</option>
      <option value="lru" data-ru="LRU-Кэш с O(1) операциями get/put" data-en="LRU Cache with O(1) operations">LRU Kesh Tizimi (O(1) Get/Put)</option>
    </select>
  </div>
  <div style="display:flex; gap:10px;">
    <button class="btn btn-green" id="btnStart" onclick="runAutonomousLoop()" data-ru="▶️ Запустить Агентный Цикл" data-en="▶️ Start Agent Loop">▶️ Agent Tsiklini Boshlash</button>
    <button class="btn btn-gray" onclick="resetStudio()" data-ru="🔄 Сброс" data-en="🔄 Reset">🔄 Qayta Boshlash</button>
  </div>
</div>

<script>
var TASKS = {
  "fib": {
    "title": "Keshli Fibonacci",
    "step1_code": `def fib(n: int) -> int:
    # 1-Urinish: Oddiy rekursiya keshlanmagan
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)
`,
    "step1_fail": `============================= FAILURES =============================
____________________________ test_fib_large ____________________________
    def test_fib_large():
>       assert fib(35) == 9227465
E       Failed: TimeoutExpired (> 3.0s)! Eksponentsial O(2^N) rekursiya aniqlandi.
========================= 1 failed, 2 passed in 3.02s =========================`,
    "critic_fix": `🔍 [Critic Reflector Diagnostikasi]:
Xatolik ildizi: Eksponentsial rekursiya vaqt limiti (3s) dan oshib ketdi.
Ko'rsatma Coderga:
1. 'from functools import lru_cache' import qiling.
2. '@lru_cache(maxsize=None)' dekoratorini 'fib' ustiga qo'ying.
3. Rekursiya mantig'iga tegmang!`,
    "step2_code": `from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n: int) -> int:
    # Keshli Fibonacci funksiyasi O(N) vaqt murakkabligida
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)
`,
    "step2_pass": `============================= TEST SUMMARY =============================
test_fib_base (n=0, n=1) ........................................ PASSED
test_fib_mid (n=10 -> 55) ....................................... PASSED
test_fib_large (n=35 -> 9227465) ................................ PASSED (0.001s)
test_fib_stress (n=100 -> 354224848179261915075) ................ PASSED (0.002s)
========================= 4 passed in 0.04s (100% YASHIL) =========================`
  },
  "rate_limiter": {
    "title": "Token Bucket Rate Limiter",
    "step1_code": `class TokenBucket:
    def __init__(self, capacity: int, refill_rate: float):
        self.capacity = capacity
        self.tokens = capacity
    
    def allow_request(self) -> bool:
        # XATO: Vaqt deltasini tekshirish unutilgan
        if self.tokens >= 1:
            self.tokens -= 1
            return True
        return False
`,
    "step1_fail": `============================= FAILURES =============================
____________________________ test_refill_after_wait ____________________________
    def test_refill_after_wait():
        bucket = TokenBucket(capacity=2, refill_rate=1.0)
        assert bucket.allow_request() == True
        assert bucket.allow_request() == True
        assert bucket.allow_request() == False
        time.sleep(1.1)
>       assert bucket.allow_request() == True
E       AssertionError: Tokenlar 1.1s o'tgach qayta to'lmadi!
========================= 1 failed, 2 passed in 1.15s =========================`,
    "critic_fix": `🔍 [Critic Reflector Diagnostikasi]:
Xatolik ildizi: Tokenlar vaqt bo'yicha refill qilinmayapti.
Ko'rsatma Coderga:
1. 'self.last_refill = time.time()' o'zgaruvchisini saqlang.
2. Har bir so'rovda 'now - self.last_refill' orqali yangi tokenlarni qo'shing.
3. 'self.tokens = min(self.capacity, self.tokens + added)' deb cheklang!`,
    "step2_code": `import time

class TokenBucket:
    # Xavfsiz va aniq Token Bucket Rate Limiter
    def __init__(self, capacity: int, refill_rate: float):
        self.capacity = capacity
        self.tokens = float(capacity)
        self.refill_rate = refill_rate
        self.last_refill = time.time()
    
    def allow_request(self) -> bool:
        now = time.time()
        elapsed = now - self.last_refill
        self.tokens = min(float(self.capacity), self.tokens + elapsed * self.refill_rate)
        self.last_refill = now
        
        if self.tokens >= 1.0:
            self.tokens -= 1.0
            return True
        return False
`,
    "step2_pass": `============================= TEST SUMMARY =============================
test_initial_burst (2 tokens allowed) ........................... PASSED
test_rate_limit_exceeded (3rd blocked) .......................... PASSED
test_refill_after_wait (refilled successfully) ................. PASSED
test_capacity_cap (never exceeds capacity) ...................... PASSED
========================= 4 passed in 1.18s (100% YASHIL) =========================`
  },
  "lru": {
    "title": "LRU Kesh Tizimi",
    "step1_code": `class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.data = {}
        
    def get(self, key: int) -> int:
        return self.data.get(key, -1)
        
    def put(self, key: int, value: int) -> None:
        # XATO: Sig'imdan oshganda eng eski elementni o'chirish yo'q!
        self.data[key] = value
`,
    "step1_fail": `============================= FAILURES =============================
____________________________ test_eviction_policy ____________________________
    def test_eviction_policy():
        lru = LRUCache(2)
        lru.put(1, 1); lru.put(2, 2)
        assert lru.get(1) == 1
        lru.put(3, 3) # Sig'im 2, 2 o'chishi kerak edi
>       assert lru.get(2) == -1
E       AssertionError: 2 o'chirilmadi! Kesh hajmi oshib ketdi.
========================= 1 failed, 2 passed in 0.05s =========================`,
    "critic_fix": `🔍 [Critic Reflector Diagnostikasi]:
Xatolik ildizi: Oddiy dict ishlatilgan va eskirgan elementlar kuzatilmayapti.
Ko'rsatma Coderga:
1. 'from collections import OrderedDict' dan foydalaning.
2. Har bir get() va put() chaqirilganda 'move_to_end(key)' qiling.
3. Agar len > capacity bo'lsa, 'popitem(last=False)' orqali eng eskini o'chiring!`,
    "step2_code": `from collections import OrderedDict

class LRUCache:
    # O(1) vaqt murakkabligiga ega LRU Kesh tizimi
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()
        
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)
`,
    "step2_pass": `============================= TEST SUMMARY =============================
test_basic_get_put .............................................. PASSED
test_eviction_policy (LRU element dropped) ...................... PASSED
test_access_order_update (recently read preserved) .............. PASSED
test_overwrite_existing_key ..................................... PASSED
========================= 4 passed in 0.04s (100% YASHIL) =========================`
  }
};

function runAutonomousLoop() {
  var sel = document.getElementById('selTask').value;
  var t = TASKS[sel];
  if (!t) return;

  var btn = document.getElementById('btnStart');
  btn.disabled = true;
  btn.style.opacity = '0.5';

  var cView = document.getElementById('codeView');
  var term = document.getElementById('termView');

  // Iteration 1: Coder generates initial code
  document.getElementById('hudIter').textContent = '1 / 2';
  document.getElementById('hudStatus').textContent = 'Coder: Kod yozmoqda...';
  document.getElementById('hudStatus').style.color = 'var(--accent)';
  document.getElementById('hudTests').textContent = '0 / 4';
  document.getElementById('hudTests').style.color = 'var(--ink)';

  cView.textContent = t.step1_code;
  term.innerHTML = '<div style="color:var(--accent);">[Iteratsiya 1]: Coder topshiriq bo‘yicha kod generatsiya qildi.</div>';
  term.innerHTML += '<div style="color:var(--yellow); margin-top:4px;">⚡ Sandbox Runner: PyTest testlari ishga tushirilmoqda...</div>';

  setTimeout(function() {
    // Tests fail
    term.innerHTML += '<pre style="color:var(--red); font-size:10px; background:#1e1014; padding:8px; border-radius:4px; margin-top:4px;">' + t.step1_fail + '</pre>';
    document.getElementById('hudStatus').textContent = 'Critic: Tahlil qilmoqda...';
    document.getElementById('hudStatus').style.color = 'var(--red)';
    document.getElementById('hudTests').textContent = '❌ 1 ta xato';
    document.getElementById('hudTests').style.color = 'var(--red)';

    setTimeout(function() {
      // Critic diagnoses
      term.innerHTML += '<div style="color:var(--purple); background:rgba(168,85,247,0.1); border-left:3px solid var(--purple); padding:8px; border-radius:4px; margin-top:6px; font-weight:700;">' + t.critic_fix.replace(/\\n/g, '<br>') + '</div>';
      document.getElementById('hudIter').textContent = '2 / 2';
      document.getElementById('hudStatus').textContent = 'Coder: Qayta tuzatmoqda...';
      document.getElementById('hudStatus').style.color = 'var(--purple)';

      setTimeout(function() {
        // Coder self-corrects and passes
        cView.textContent = t.step2_code;
        term.innerHTML += '<div style="color:var(--green); margin-top:6px;">🛠️ Coder: Critic ko‘rsatmasi bo‘yicha nuqtali patch kiritildi!</div>';
        term.innerHTML += '<pre style="color:var(--green); font-size:10px; background:#0e231b; padding:8px; border-radius:4px; margin-top:4px;">' + t.step2_pass + '</pre>';
        document.getElementById('hudStatus').textContent = '✅ Muvaffaqiyat (Yashil)';
        document.getElementById('hudStatus').style.color = 'var(--green)';
        document.getElementById('hudTests').textContent = '✅ 4 / 4 (100%)';
        document.getElementById('hudTests').style.color = 'var(--green)';
        btn.disabled = false;
        btn.style.opacity = '1';
        term.scrollTop = term.scrollHeight;
      }, 1500);

    }, 1500);

  }, 1200);
}

function resetStudio() {
  document.getElementById('codeView').textContent = '# Coder kodi shu yerda real vaqtda paydo bo‘ladi...\\n# "▶️ Agent Tsiklini Boshlash" tugmasini bosing!';
  document.getElementById('termView').innerHTML = '<div style="color:#64748b;">[Sandbox tayyor] Vazifani tanlang va avtonom TDD tsiklini ishga tushiring.</div>';
  document.getElementById('hudIter').textContent = '0 / 3';
  document.getElementById('hudStatus').textContent = 'Kutilmoqda';
  document.getElementById('hudStatus').style.color = 'var(--yellow)';
  document.getElementById('hudTests').textContent = '0 / 5';
  document.getElementById('hudTests').style.color = 'var(--ink)';
  var btn = document.getElementById('btnStart');
  btn.disabled = false;
  btn.style.opacity = '1';
}
</script>

</body>
</html>
"""
    out_path = os.path.join(DEST_DIR, "simulator", "index.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)
    print("  ✓ Created: simulator/index.html")

def main():
    print("📦 Building 10-11-sinf (Lesson 29: Autonomous Coding Agents & TDD)...")
    build_presentation()
    build_worksheet()
    build_homework()
    build_teacher_reading()
    build_simulator()
    print("🎉 Done! Generated Grade 10–11 Lesson 29.")

if __name__ == "__main__":
    main()
