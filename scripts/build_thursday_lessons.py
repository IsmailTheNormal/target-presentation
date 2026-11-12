#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
scripts/build_thursday_lessons.py — Complete Compiler for Thursday's 3 Double-Block Lessons

Thursday Schedule:
  1. 5–6-sinf (10:30–11:55, 80 min): 26-dars Scratch Jonli Animatsiyalar va Kostyumlar
  2. 10–11-sinf (12:00–14:10, 80 min): 26-dars Agentik Tool Calling, Funksiyalar va Sandboxing
  3. 7–8-sinf (14:15–15:40, 80 min): 30-dars Kamera, Viewport va Fog of War (Urush Tumani)
"""

import os
import sys
import json
import re
import subprocess
REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if REPO_ROOT not in sys.path:
    sys.path.insert(0, REPO_ROOT)
from scripts.scratch_builder import generate_lesson_26_projects

# Load Master Templates
with open(os.path.join(REPO_ROOT, "assets", "TEMPLATE_PREZENTATSIYA.html"), "r", encoding="utf-8") as f:
    TPL_PRES = f.read()

with open(os.path.join(REPO_ROOT, "assets", "TEMPLATE_VARAQA.html"), "r", encoding="utf-8") as f:
    TPL_VAR = f.read()

with open(os.path.join(REPO_ROOT, "assets", "TEMPLATE_VAZIFA.html"), "r", encoding="utf-8") as f:
    TPL_VAZ = f.read()


def load_clean_scratch_svgs(prefix=""):
    with open(os.path.join(REPO_ROOT, "assets", "scratch-cat-costume1.svg"), "r", encoding="utf-8") as f:
        c1 = f.read().strip()
    with open(os.path.join(REPO_ROOT, "assets", "scratch-cat-costume2.svg"), "r", encoding="utf-8") as f:
        c2 = f.read().strip()

    def clean(s, svg_id, w, h, disp):
        s = re.sub(r'<\?xml[^>]*\?>', '', s)
        s = re.sub(r'<!--.*?-->', '', s, flags=re.DOTALL)
        s = re.sub(r'<title>.*?</title>', '', s)
        s = re.sub(r'<desc>.*?</desc>', '', s)
        s = s.strip()
        s = re.sub(r'<svg\b[^>]*>', f'<svg id="{svg_id}" viewBox="0 0 {w} {h}" style="width:90px; height:96px; display:{disp}; user-select:none;">', s, count=1)
        return s

    p = prefix + "_" if prefix else ""
    svg1 = clean(c1, f"{p}scratchCatPose1", 96, 101, "block")
    svg2 = clean(c2, f"{p}scratchCatPose2", 93, 106, "none")
    return svg1, svg2

def ensure_dir(path):
    os.makedirs(path, exist_ok=True)
    return path

# ===========================================================================
# 1. COHORT 5–6-SINF (26-DARS: SCRATCH JONLI ANIMATSIYALAR VA KOSTYUMLAR)
# ===========================================================================
def build_5_6_lesson():
    lesson_dir = ensure_dir(os.path.join(REPO_ROOT, "classes", "5-6-sinf", "10-hafta", "26-dars-scratch-jonli-animatsiyalar-va-kostyumlar"))
    app_dir = ensure_dir(os.path.join(lesson_dir, "playground"))
    proj_dir = ensure_dir(os.path.join(lesson_dir, "projects"))

    print("\n📦 Generating 5–6-sinf (26-dars: Scratch Jonli Animatsiyalar)...")
    generate_lesson_26_projects(proj_dir)

    # --- 1.1 PREZENTATSIYA ---
    title_uz = "26-dars: Scratchda Jonli Animatsiyalar va Kostyumlar"
    title_ru = "Урок 26: Живая Анимация и Костюмы в Scratch"
    title_en = "Lesson 26: Live Sprite Animations & Costumes in Scratch"

    tpl = TPL_PRES
    tpl = re.sub(r"<title[^>]*>.*?</title>", f'<title data-ru="{title_ru}" data-en="{title_en}">{title_uz}</title>', tpl)
    tpl = re.sub(r'<span class="tag"[^>]*>.*?</span>', '<span class="tag" data-ru="5-6 · ВАЙБКОДИНГ" data-en="5-6 · VIBECODING">5-6 · VIBECODING</span>', tpl, count=1)
    tpl = tpl.replace('<span id="totalSlides">6</span>', '<span id="totalSlides">14</span>')

    titles_dict = {"uz": title_uz, "ru": title_ru, "en": title_en}
    titles_json = json.dumps(titles_dict, ensure_ascii=False, indent=2)
    tpl = re.sub(r'var TITLES\s*=\s*\{[\s\S]*?\};', f'var TITLES = {titles_json};', tpl)

    slides = []

    # Slide 1: Titul
    slides.append("""  <!-- SLIDE 1: TITUL -->
  <section class="slide is-on" data-phase="Kirish|Введение|Introduction" data-time="00:00–04:00">
    <div class="eyebrow" data-ru="5–6-СИНФ · 10-Я НЕДЕЛЯ · УРОК 26" data-en="GRADES 5–6 · WEEK 10 · LESSON 26">5–6-SINF · 10-HAFTA · 26-DARS</div>
    <h1 data-ru="Живая Анимация в Scratch: Костюмы и Циклы Ходьбы" data-en="Live Animations in Scratch: Costumes & Walk Cycles">Scratchda Jonli Animatsiyalar: Kostyumlar va Qadamlar</h1>
    <p class="lede" data-ru="Оживляем персонажей: кадровая анимация (Flipbook), циклы шагов (Next costume), плавная ходьба и речевые облака!" data-en="Bringing characters to life: frame-by-frame animation (Flipbook), walk cycles (Next costume), smooth locomotion, and speech bubbles!">Personajlarni haqiqiy multfilm qahramonidek jonlantiramiz: ko'p kadrli kostyumlar, silliq qadam tashlash, burilish qoidalari va gapiruvchi pufakchalar!</p>
    <div class="grid c3" style="margin-top:24px;">
      <div class="card">
        <h3 data-ru="Формат урока" data-en="Lesson Format">Format va Davomiylik</h3>
        <p data-ru="Спаренный блок: 2 x 40 минут = 80 минут интенсивной лаборатории" data-en="Double block: 2 x 40 min = 80 min intensive hands-on lab">Juftlik blok: 2 x 40 daqiqa = 80 daqiqalik qizg'in kiber-amaliyot</p>
      </div>
      <div class="card">
        <h3 data-ru="Главная миссия" data-en="Core Mission">Amaliy Missiya</h3>
        <p data-ru="Создать полноценного шагающего и говорящего героя в Scratch" data-en="Build a fully animated walking, speaking hero in Scratch">Scratchda qadam tashlab yuradigan va gapiradigan to'liq personaj yaratish</p>
      </div>
      <div class="card">
        <h3 data-ru="10-Балльная система" data-en="10-Point Rubric">Baholash Mezoni</h3>
        <p data-ru="4 балла: Кадры · 4 балла: Диалоги · 2 балла: Плавность движения" data-en="4 pts: Frames · 4 pts: Dialogues · 2 pts: Motion fluidity">4 ball: Kadrlar · 4 ball: Dialoglar · 2 ball: Silliq harakat</p>
      </div>
    </div>
  </section>""")

    # Slide 2: HW Review (25-dars Jarvis Voice AI)
    slides.append("""  <!-- SLIDE 2: MANDATORY HW REVIEW & BRIDGE -->
  <section class="slide" data-phase="Uy Vazifasi Tahlili|Разбор Д/З|HW Review" data-time="04:00–10:00">
    <div class="eyebrow" data-ru="АНАЛИЗ Д/З · РАЗБОР ОШИБОК 25-УРОКА" data-en="HOMEWORK AUDIT · LESSON 25 PITFALLS">UY VAZIFASI TAHLILI · 25-DARS XATOLAR REVIZIYASI</div>
    <h2 data-ru="Разбор Домашнего Задания: Target Jarvis и Голосовой AI" data-en="Homework Autopsy: Target Jarvis & Voice AI">O'tgan Dars Vazifasi Tahlili: Target Jarvis va Ovozli AI</h2>
    <div class="grid c2" style="margin-top:16px;">
      <div class="card" style="border-left:4px solid var(--accent);">
        <span class="pill" style="color:var(--accent-ink);" data-ru="Типичная ошибка" data-en="Common Pitfall">Xato Tahlili (Pitfall)</span>
        <h3 data-ru="Повторный запуск микрофона и путаница в словах" data-en="Repeated mic start & string casing issues">Mikrofonni ketma-ket bosish va harflar registri xatosi</h3>
        <p data-ru="Ученики нажимали кнопку старта несколько раз без флага isListening или забывали перевести текст в toLowerCase(), из-за чего условия не срабатывали." data-en="Students spam-clicked the start button without an isListening flag or omitted .toLowerCase(), causing intent conditions to miss.">Mikrofon tugmasi ketma-ket bosilganda `recognition already started` xatosi chiqqan, yoki `.toLowerCase()` ishlatilmagani uchun bosh harflar shartlarga mos kelmagan.</p>
        <pre class="code-snippet" style="margin-top:8px;"><code>// ❌ Xato:
rec.start(); // Tekshiruvsiz yana bosilsa xato beradi!
if (gap === "Salom") // "salom" kichik harf bilan kelsa ishlamaydi!</code></pre>
      </div>
      <div class="card" style="border-left:4px solid var(--green);">
        <span class="pill" style="color:var(--green);" data-ru="Золотой стандарт" data-en="Golden Standard">Oltin Yechim (Best Practice)</span>
        <h3 data-ru="Флаг состояния и безопасный поиск includes()" data-en="State guard flag & robust includes() logic">Holat bayrog'i va toza tekshiruv</h3>
        <p data-ru="Проверка флага isListening защищает браузер от сбоя, а toLowerCase().includes('salom') гарантирует 100% распознавание в любой фразе." data-en="Guarding with isListening prevents crashes, while toLowerCase().includes('salom') reliably finds keywords inside any sentence.">`isListening` bayrog'i mikrofonni takroriy xatodan asraydi, `toLowerCase().includes('salom')` esa harflar qanday yozilishidan qat'i nazar buyruqni topadi.</p>
        <pre class="code-snippet" style="margin-top:8px;"><code>// ✅ To'g'ri:
if (!isListening) { rec.start(); isListening = true; }
if (gap.toLowerCase().includes("salom")) { gapir("Salom!"); }</code></pre>
      </div>
    </div>
    <div class="grid c2" style="margin-top:16px;">
      <div class="card">
        <span class="pill" data-ru="Блиц-контроль (30 сек)" data-en="30s Blitz Check">30s Blits-Nazorat</span>
        <p data-ru="Назовите 3 двигателя любого голосового AI? Ответ: STT (слух), NLP (мозг), TTS (голос)!" data-en="Name the 3 engines of any voice assistant? Answer: STT (hearing), NLP (brain), TTS (voice)!">Ovozli yordamchining 3 ta asosiy dvigateli nima? Javob: <b>STT (quloq)</b>, <b>NLP (miya)</b> va <b>TTS (til)</b>!</p>
      </div>
      <div class="card">
        <span class="pill" data-ru="Мост к новому уроку" data-en="Bridge to Topic">Bugungi Darsga Ko'prik</span>
        <p data-ru="Вчера наш персонаж заговорил. Но он стоит на месте как статуя! Сегодня мы заставим его двигать ногами, менять костюмы и выражать эмоции!" data-en="Yesterday our character spoke. But it stands still like a statue! Today we give it multi-frame legs to walk and express emotions!">Kecha qahramonimiz gapirishni o'rgandi. Ammo u sahnada qotib turgan haykaldek harakatsiz! Bugun unga jonli qadam tashlash va yugurishni o'rgatamiz!</p>
      </div>
    </div>
  </section>""")

    # Slide 3: Animation Concept (Flipbook)
    slides.append("""  <!-- SLIDE 3: FLIPBOOK CONCEPT -->
  <section class="slide" data-phase="Tushuncha|Концепция|Concept" data-time="10:00–16:00">
    <div class="eyebrow" data-ru="КАК РОЖДАЕТСЯ АНИМАЦИЯ · ЭФФЕКТ FLIPBOOK" data-en="HOW ANIMATION WORKS · FLIPBOOK EFFECT">ANIMATSIYA SEHRI · FLIPBOOK EFFEKTI</div>
    <h2 data-ru="Секрет Диснея: Быстрая Смена Неподвижных Кадров" data-en="Disney's Secret: Rapid Playback of Static Frames">Disneyning Katta Siri: Statik Rasmlar Ketma-ketligi</h2>
    <p class="lede" data-ru="Компьютер не умеет 'двигать' картинку сам по себе. Он показывает много похожих рисунков с огромной скоростью!" data-en="Computers do not truly 'move' pictures. They rapidly display sequential still frames to create the illusion of life!">Kompyuter rasmni o'z-o'zidan harakatlantira olmaydi. U bir-biriga o'xshash bir nechta rasmni juda tez almashtirib, harakat illyuziyasini yaratadi!</p>
    <div class="grid c3" style="margin-top:20px;">
      <div class="card">
        <span class="pill" data-ru="Кадр 1" data-en="Frame 1">Kadr 1</span>
        <h3 data-ru="Правая нога впереди" data-en="Right Foot Forward">O'ng Oyoq Oldinda</h3>
        <p data-ru="Персонаж делает шаг правой ногой, левая рука отведена назад." data-en="Sprite steps with right leg forward, left arm swings backward.">Mushuk o'ng oyog'ini oldinga tashlaydi, chap qo'li esa orqada bo'ladi.</p>
      </div>
      <div class="card">
        <span class="pill" data-ru="Кадр 2" data-en="Frame 2">Kadr 2</span>
        <h3 data-ru="Обе ноги на земле" data-en="Neutral Stance">O'tish Holati</h3>
        <p data-ru="Промежуточный кадр: персонаж переносит центр тяжести вперед." data-en="Passing frame: center of gravity transitions smoothly forward.">Qadamlar almashinadigan o'rta holat, qahramon oldinga siljiydi.</p>
      </div>
      <div class="card">
        <span class="pill" data-ru="Кадр 3" data-en="Frame 3">Kadr 3</span>
        <h3 data-ru="Левая нога впереди" data-en="Left Foot Forward">Chap Oyoq Oldinda</h3>
        <p data-ru="Левая нога выбрасывается вперед. Цикл замыкается в бесконечность!" data-en="Left foot strides forward. The loop repeats seamlessly forever!">Chap oyoq oldinga chiqadi. Sikl qayta boshlanib, uzluksiz yugurish hosil bo'ladi!</p>
      </div>
    </div>
  </section>""")

    # Slide 4: Costumes Architecture
    slides.append("""  <!-- SLIDE 4: COSTUMES IN SCRATCH -->
  <section class="slide" data-phase="Arxitektura|Архитектура|Architecture" data-time="16:00–22:00">
    <div class="eyebrow" data-ru="АНАТОМИЯ СПРАЙТА · КОСТЮМЫ (COSTUMES)" data-en="SPRITE ANATOMY · COSTUMES">SPRAYT ANATOMIYASI · KOSTYUMlar</div>
    <h2 data-ru="Вкладка 'Костюмы': Где Живут Фазы Движения" data-en="The Costumes Tab: Where Animation Frames Live">'Kostyumlar' Bo'limi: Harakat Fazalari Qayerda Saqlanadi?</h2>
    <p class="lede" data-ru="Каждый спрайт в Scratch может содержать десятки костюмов: покой, ходьба, прыжок, падение и атака." data-en="Every Scratch sprite can hold dozens of costumes: idle, walk, jump, fall, and attack stances.">Scratchdagi har bir qahramon o'nlab kostyumlarga ega bo'lishi mumkin: tinch turish, qadam tashlash, sakrash va bayramona raqs.</p>
    <div class="grid c2" style="margin-top:20px;">
      <div class="card">
        <h3 data-ru="Имена костюмов имеют значение!" data-en="Costume Names Matter!">Kostyum Nomlari Qoidasi</h3>
        <p data-ru="По умолчанию Scratch называет их costume1, costume2. Но для чистого кода лучше давать смысловые имена:" data-en="Scratch defaults to costume1 and costume2. For clear code, assign explicit semantic names:">Dasturda adashib ketmaslik uchun kostyumlarga to'g'ri nom berish odatiga o'rganamiz:</p>
        <ul style="margin-top:8px; line-height:1.7; padding-left:18px;">
          <li data-ru="walk-1, walk-2 — фазы ходьбы" data-en="walk-1, walk-2 — walking phases"><code>walk-1</code>, <code>walk-2</code> — qadam tashlash</li>
          <li data-ru="jump — поза прыжка" data-en="jump — jump pose"><code>jump</code> — tepaga sakrash holati</li>
          <li data-ru="idle — персонаж стоит и дышит" data-en="idle — resting and breathing"><code>idle</code> — joyida tinch turish</li>
        </ul>
      </div>
      <div class="card">
        <h3 data-ru="Центр привязки (Anchor Point)" data-en="Anchor Point Centering">Markazlashtirish (Anchor Point)</h3>
        <p data-ru="Самая частая ошибка: смещенный центр костюма! Персонаж начинает дергаться и прыгать на месте." data-en="Top beginner error: uncentered costumes! Characters wildly jitter and drift on every frame.">Agar kostyum markazi to'g'ri qo'yilmasa, kadr almashganda personaj qaltirab, joyidan siljib ketadi. Har doim markazga tekislang!</p>
        <div style="margin-top:8px; font-size:12px; color:var(--accent-ink); font-weight:700;" data-ru="🎯 Правило: Ноги или туловище должны быть ровно на крестике редактора!" data-en="🎯 Rule: Center feet or torso directly on the editor crosshair!">🎯 Oltin qoida: Personaj tanasi muharrirdagi nishon (kesishma) markazida tursin!</div>
      </div>
    </div>
  </section>""")
    cat_svg1, cat_svg2 = load_clean_scratch_svgs()

    # Slide 5: Interactive Slide — Scratch Cat Walk Cycle Simulator
    slides.append(f"""  <!-- SLIDE 5: SCRATCH CAT WALK CYCLE SIMULATOR -->
  <section class="slide" data-phase="Jonli Sinov|Живой Тест|Live Demo" data-time="22:00–30:00">
    <div class="eyebrow" data-ru="ГЛАВНАЯ АНИМАЦИЯ · ЦИКЛ ХОДЬБЫ" data-en="CORE ANIMATION · WALK CYCLE LOOP">ASOSIY ANIMATSIYA · QADAM TASHLASH SIKLI</div>
    <h2 data-ru="Живой Тест: Кот Scratch Шагает по Сцене!" data-en="Live Test: Scratch Cat Takes Real Strides on Stage!">Jonli Sinov: Scratch Mushugi Sahnada Qadam Tashlaydi!</h2>
    <p class="lede" data-ru="Каждый шаг состоит из смены 2 костюмов и смещения на 10 пикселей. Переключайте кадры вручную или включите авто-ходьбу!" data-en="Each walk step combines cycling 2 costumes and shifting 10 pixels forward. Toggle frames manually or activate auto-walk!">Har bir qadam 2 ta kostyum almashishi va 10 piksel siljishdan iborat. Kadrlarni qo'lda almashtiring yoki avto-yurishni yoqing:</p>

    <!-- Stage Simulation Canvas -->
    <div class="scratch-stage-box" id="scratchStageArea" style="position:relative; width:100%; max-width:740px; height:185px; margin:8px auto 12px; background:radial-gradient(ellipse at 50% 30%, rgba(255,255,255,0.06), rgba(0,0,0,0.3)), var(--panel-2); border:2px solid var(--rule); border-radius:12px; overflow:hidden;">
      <!-- Stage Status HUD -->
      <div style="position:absolute; top:8px; left:12px; right:12px; display:flex; justify-content:space-between; align-items:center; font-family:'JetBrains Mono', monospace; font-size:11px; color:var(--ink-2); z-index:2; pointer-events:none;">
        <div><span class="t" data-ru="Костюм: " data-en="Costume: ">Kostyum: </span><b id="costumeBadge" style="color:var(--accent);">costume1 (cat-a · Turish)</b></div>
        <div><span>X: </span><b id="posXBadge" style="color:var(--ink);">40</b> &nbsp;|&nbsp; <span>Y: </span><b style="color:var(--ink);">-40</b></div>
        <div><span class="t" data-ru="Направление: " data-en="Direction: ">Yo'nalish: </span><b id="dirBadge" style="color:var(--green);">90° (O'ngga)</b></div>
      </div>

      <!-- Stage Floor Line -->
      <div style="position:absolute; left:0; right:0; bottom:16px; height:2px; background:linear-gradient(90deg, transparent, var(--accent), transparent); opacity:0.8;"></div>
      <div style="position:absolute; right:12px; bottom:4px; font-family:'JetBrains Mono', monospace; font-size:9px; color:var(--ink-3);" data-ru="Поверхность сцены (Y = -40)" data-en="Stage floor (Y = -40)">Sahna zamini (Y = -40)</div>

      <!-- Scratch Cat Sprite Container -->
      <div id="scratchCatMover" style="position:absolute; bottom:16px; left:40px; width:90px; height:96px; transition:left 0.12s linear; transform-origin:50% 100%;">
        {cat_svg1}
        {cat_svg2}
      </div>
    </div>

    <!-- Controls focused squarely on the Scratch Walk Cycle -->
    <div style="max-width:740px; margin:0 auto; display:grid; grid-template-columns:1fr 1.3fr; gap:12px; align-items:stretch;">
      <!-- Manual Costume Stepping -->
      <div class="card" style="padding:10px 14px; display:flex; flex-direction:column; justify-content:space-between;">
        <div>
          <div style="font-size:10.5px; font-weight:800; color:var(--ink-3); text-transform:uppercase; letter-spacing:0.05em; margin-bottom:6px;" data-ru="Ручное переключение (Кадры)" data-en="Manual Toggle (Frames)">Qo'lda Ko'rish (Kadrlar)</div>
          <div style="display:flex; gap:8px;">
            <button type="button" class="dock-btn" onclick="setCostume('costume1')" style="flex:1; padding:7px 10px; font-size:11.5px; border:1px solid var(--rule);" data-ru="🐾 1-Костюм (cat-a)" data-en="🐾 Costume 1 (cat-a)">🐾 1-Kostyum (cat-a)</button>
            <button type="button" class="dock-btn" onclick="setCostume('costume2')" style="flex:1; padding:7px 10px; font-size:11.5px; border:1px solid var(--rule);" data-ru="👣 2-Костюм (cat-b)" data-en="👣 Costume 2 (cat-b)">👣 2-Kostyum (cat-b)</button>
          </div>
        </div>
        <div style="margin-top:6px; font-size:10.5px; color:var(--ink-2); line-height:1.35;" data-ru="1-й костюм (нога на месте) и 2-й костюм (нога делает шаг вперед)." data-en="Costume 1 (foot ready) and Costume 2 (foot stepping forward).">1-kostyum (oyoq tayyor) va 2-kostyum (oldinga qadam).</div>
      </div>

      <!-- Auto Walk Cycle Loop -->
      <div class="card" style="padding:10px 14px; display:flex; flex-direction:column; justify-content:space-between;">
        <div>
          <div style="font-size:10.5px; font-weight:800; color:var(--ink-3); text-transform:uppercase; letter-spacing:0.05em; margin-bottom:6px;" data-ru="Автоматический цикл (Ходьба)" data-en="Automated Loop (Walk Cycle)">Avtomatik Sikl (Harakat)</div>
          <div style="display:flex; gap:8px;">
            <button type="button" class="dock-btn" onclick="toggleAutoWalk()" id="autoWalkBtn" style="flex:2; padding:7px 12px; font-size:12px; font-weight:800; background:var(--accent); color:#00214A;" data-ru="▶️ Авто-Ходьба (Цикл)" data-en="▶️ Auto-Walk Loop">▶️ Avto-Qadam Tashlash</button>
            <button type="button" class="dock-btn" onclick="changeWalkSpeed()" id="speedBtn" style="flex:1; padding:7px 8px; font-size:11px; border:1px solid var(--rule);" data-ru="⚡ 0.15 сек" data-en="⚡ 0.15s">⚡ 0.15s</button>
            <button type="button" class="dock-btn" onclick="resetWalk()" style="padding:7px 10px; font-size:11px; border:1px solid var(--rule);" title="Reset" data-title-ru="Сбросить в начало" data-title-en="Reset to start">🔄</button>
          </div>
        </div>
        <div style="margin-top:6px; font-size:10.5px; color:var(--ink-2); line-height:1.35;" data-ru="next costume + 10 шагов + задержка. Дойдя до края, кот разворачивается!" data-en="next costume + 10 steps + delay. Reaching stage edges, cat flips around!">next costume + 10 qadam + kutish. Chekkaga yetganda mushuk o'giriladi!</div>
      </div>
    </div>
  </section>""")

    # Slide 6: Next Costume & Wait Loop
    slides.append("""  <!-- SLIDE 6: NEXT COSTUME LOGIC -->
  <section class="slide" data-phase="Sikllar|Циклы|Loops" data-time="30:00–36:00">
    <div class="eyebrow" data-ru="ГЛАВНЫЙ АЛГОРИТМ · БЛОКИ ХОДЬБЫ" data-en="CORE ALGORITHM · WALK LOOP">ASOSIY ALGORITM · QADAM TASHLASH SIKLI</div>
    <h2 data-ru="Связка: 'Следующий Костюм' + 'Ждать 0.1 Сек'" data-en="The Golden Pair: 'Next Costume' + 'Wait 0.1 Sec'">Oltin Juftlik: 'Keyingi Kostyum' + '0.1 Sekund Kutish'</h2>
    <p class="lede" data-ru="Если не поставить блок задержки, компьютер сменит 1000 костюмов за секунду — получится бешеное мелькание!" data-en="Without a wait delay, computers cycle 1000 frames per second into an unrecognizable blurry buzz!">Agar kadrlar orasiga kutish qo'yilmasa, kompyuter 1 soniyada 1000 marta kadr almashtirib yuboradi va qahramon qotib qoladi!</p>
    <div class="grid c2" style="margin-top:20px;">
      <div class="card">
        <h3 data-ru="Правильный блок-код ходьбы" data-en="Proper Walking Block Script">To'g'ri Harakat Bloki</h3>
        <pre class="code-snippet"><code>when green flag clicked
forever
  move (10) steps
  next costume
  wait (0.1) seconds // ⏱️ Ko'z ilg'aydigan tezlik!
end</code></pre>
      </div>
      <div class="card">
        <h3 data-ru="Почему именно 0.1–0.15 секунды?" data-en="Why 0.1–0.15 Seconds Delay?">Nega Aynan 0.1–0.15 Sekund?</h3>
        <p data-ru="Человеческий глаз воспринимает плавную иллюзию движения при частоте от 10 до 24 кадров в секунду." data-en="Human vision interprets motion fluidly when frames cycle at roughly 10 to 24 frames per second.">Inson ko'zi sekundiga 10–24 ta kadr almashganda uni yaxlit va ravon harakat deb qabul qiladi:</p>
        <ul style="margin-top:8px; line-height:1.7; padding-left:18px;">
          <li data-ru="wait 0.01 — слишком быстро (мелькание)" data-en="wait 0.01 — too fast (blurry flash)"><code>wait (0.01)</code> — haddan tashqari tez (titrash)</li>
          <li data-ru="wait 0.12 — идеальный бег кота" data-en="wait 0.12 — perfect fluid sprint"><code>wait (0.12)</code> — tabiiy va chiroyli yugurish</li>
          <li data-ru="wait 1.0 — персонаж как робот" data-en="wait 1.0 — robotic slide"><code>wait (1.0)</code> — o'ta sekin, toshdek qotish</li>
        </ul>
      </div>
    </div>
  </section>""")

    # Slide 7: Rotation Style (Left-Right)
    slides.append("""  <!-- SLIDE 7: ROTATION STYLE -->
  <section class="slide" data-phase="Yo'nalish|Вращение|Rotation" data-time="36:00–42:00">
    <div class="eyebrow" data-ru="УПРАВЛЕНИЕ НАПРАВЛЕНИЕМ · СТИЛЬ ВРАЩЕНИЯ" data-en="DIRECTION CONTROL · ROTATION STYLE">BURILISH USLUBLARI · YUZNI O'GIRISH</div>
    <h2 data-ru="Как Не Дать Коту Ходить Вверх Ногами?" data-en="Keeping Sprites Upright: Left-Right Rotation">Sprayt Nega Bosh Quyi Bo'lib Qoladi?</h2>
    <p class="lede" data-ru="Когда спрайт поворачивает в направлении -90 (влево), по умолчанию он переворачивается животом кверху." data-en="When sprites point toward -90 degrees (left), Scratch defaults to flipping them upside down.">Qahramon chap tomonga (-90 daraja) yurganda boshi pastga qarab, chalqancha ag'darilib qolmasligi uchun stilni o'rnatamiz:</p>
    <div class="grid c3" style="margin-top:20px;">
      <div class="card">
        <span class="pill" data-ru="Кругом (360°)" data-en="All Around (360°)">All Around (360°)</span>
        <h3 data-ru="Кругом (360°)" data-en="All Around (360°)">To'liq Aylanish</h3>
        <p data-ru="Подходит для ракет, метеоритов и мячей. Для человека не подходит!" data-en="Great for space rockets and bouncing balls, terrible for humanoids!">Koptok yoki raketalar uchun yaxshi, lekin inson oyog'i bilan pastga tushadi!</p>
      </div>
      <div class="card" style="border:2px solid var(--green);">
        <span class="pill" style="color:var(--green);" data-ru="Влево-Вправо (Золотое Правило)" data-en="Left-Right (Golden Rule)">Left-Right (Oltin Qoida)</span>
        <h3 data-ru="Влево-Вправо" data-en="Left-Right Only">Faqat Chapga-O'ngga</h3>
        <p data-ru="Спрайт просто зеркально отражается по горизонтали и не переворачивается!" data-en="Sprite mirrors cleanly along the X axis and never turns upside down!">Qahramon chapga yurganda faqat ko'zgudek o'giriladi, qulab tushmaydi!</p>
      </div>
      <div class="card">
        <span class="pill" data-ru="Не вращать" data-en="Don't Rotate">Don't Rotate</span>
        <h3 data-ru="Не вращать" data-en="Don't Rotate">Hech Burilmaslik</h3>
        <p data-ru="Персонаж всегда смотрит строго в одну сторону, даже двигаясь назад." data-en="Always faces a single direction, regardless of motion vector.">Har qanday tomonga yursa ham faqat o'ngga qarab orqasi bilan yuradi.</p>
      </div>
    </div>
  </section>""")

    # Slide 8: Speech Bubbles (Say & Think)
    slides.append("""  <!-- SLIDE 8: SPEECH BUBBLES -->
  <section class="slide" data-phase="Muloqot|Диалоги|Speech" data-time="42:00–48:00">
    <div class="eyebrow" data-ru="ДИАЛОГИ И МЫСЛИ · РЕЧЕВЫЕ ОБЛАКА" data-en="DIALOGUES & THOUGHTS · SPEECH BUBBLES">DIOLOGLAR VA FIKRLAR · GAPIRUVCHI PUFAKCHALAR</div>
    <h2 data-ru="Спрайты Умеют Говорить: Блоки 'Say' и 'Think'" data-en="Characters Speak: The 'Say' and 'Think' Blocks">Qahramonlar Gapiradi: 'Say' va 'Think' Bloklari</h2>
    <p class="lede" data-ru="В Scratch можно передавать речь персонажа комиксными облаками: словами или тайными мыслями." data-en="Scratch renders expressive comic bubbles: spoken words or subtle thought whispers.">Scratchda qahramonning suhbati komikslardagidek chiroyli pufakchalarda ko'rinadi:</p>
    <div class="grid c2" style="margin-top:20px;">
      <div class="card">
        <h3 data-ru="Разница между 'Say' и 'Think'" data-en="'Say' vs 'Think' Difference">'Aytish' va 'O'ylash' Farqi</h3>
        <ul style="margin-top:8px; line-height:1.7; padding-left:18px;">
          <li data-ru="say [Salom!] for (2) secs — речевое облако с хвостиком" data-en="say [Hello!] for (2) secs — sharp speech bubble with pointer"><code>say [Salom!] for (2) secs</code> — o'tkir uchli gapirish pufakchasi</li>
          <li data-ru="think [Qiziq...] for (2) secs — облако мыслей с кружками" data-en="think [Hmm...] for (2) secs — floating circular thought bubble"><code>think [Qiziq...] for (2) secs</code> — mayda doirachali o'ylash pufakchasi</li>
        </ul>
      </div>
      <div class="card">
        <h3 data-ru="С таймером или навсегда?" data-en="Timed vs Indefinite Speech">Vaqtli va Doimiy Pufakcha</h3>
        <p data-ru="Блок без секунд 'say [Привет]' оставляет облако висеть вечно, пока не будет сказано пустое значение 'say []'!" data-en="Calling untimed 'say [Hello]' leaves the bubble visible forever until cleared with 'say []'!">Agar soniyasiz `say [Salom]` ishlatilsa, pufakcha to'xtovsiz sahnada qolib ketadi. Uni yopish uchun bo'sh `say []` yuboriladi.</p>
      </div>
    </div>
  </section>""")

    # Slide 9: Audio Synchronization
    slides.append("""  <!-- SLIDE 9: SOUND SYNCHRONIZATION -->
  <section class="slide" data-phase="Tovush|Звук|Audio" data-time="48:00–54:00">
    <div class="eyebrow" data-ru="ЗВУКОВЫЕ ЭФФЕКТЫ · ШАГИ И ЭМОЦИИ" data-en="SOUND EFFECTS · FOOTSTEPS & SFX">OVOZ VA QADAMLARNI SINXRONLASHTIRISH</div>
    <h2 data-ru="Озвучка Движения: Звук Каждого Шага" data-en="Foley Sound: Ticking Every Step">Harakat Ovozini Berish: Har Bir Qadam Tovushi</h2>
    <p class="lede" data-ru="Анимация без звука кажется плоской. Добавим щелчки шагов или мяуканье при каждом прыжке!" data-en="Silent animations feel lifeless. Pair every costume switch with footsteps or cheerful sound effects!">Tovushsiz animatsiya jonsiz ko'rinadi. Har bir qadamga chertilish yoki qahramon kulgisi ovozini qo'shamiz!</p>
    <div class="grid c2" style="margin-top:20px;">
      <div class="card">
        <h3 data-ru="Правильный блок звука" data-en="Proper Sound Script">To'g'ri Ovoz Chaqirish</h3>
        <pre class="code-snippet"><code>when [space] key pressed
start sound [Meow] // O'yinni to'xtatmaydi
repeat (5)
  move (10) steps
  next costume
  wait (0.1) secs
end</code></pre>
      </div>
      <div class="card">
        <h3 data-ru="start sound vs play until done" data-en="start sound vs play until done">'start sound' vs 'play until done'</h3>
        <p data-ru="Блок 'play sound until done' ЗАМОРАЖИВАЕТ весь скрипт, пока песня не закончится! Для шагов используйте только 'start sound'." data-en="'play sound until done' freezes the entire script until finished! Always use non-blocking 'start sound' for rapid footsteps.">`play sound until done` butun dasturni ovoz tugaguncha qotirib qo'yadi! Qadamlar uchun faqat to'xtatmaydigan `start sound` ishlatiladi.</p>
      </div>
    </div>
  </section>""")

    # Slide 10: Cyber Quiz
    slides.append("""  <!-- SLIDE 10: CYBER QUIZ -->
  <section class="slide" data-phase="Interaktiv Test|Тест|Interactive Quiz" data-time="54:00–60:00">
    <div class="eyebrow" data-ru="КИБЕР-ТЕСТ · ПРОВЕРКА ПОНИМАНИЯ" data-en="CYBER QUIZ · KNOWLEDGE CHECK">KIBER-TEST · BILIMNI TEKSHIRISH</div>
    <h2 data-ru="Кибер-Тест: Почему Кот Бешено Мелькает на Экране?" data-en="Cyber Quiz: Why Does the Character Flashingly Glitch?">Kiber-Sinov: Nega Mushuk Ekranda Titrab Qotib Qoladi?</h2>
    <p class="lede" data-ru="Один ученик собрал цикл: 'повторять всегда ➔ идти 10 шагов ➔ следующий костюм'. Но кот превратился в размытое пятно! Чего не хватает?" data-en="A student built a loop: 'forever ➔ move 10 ➔ next costume'. But the cat became a blurry buzz! What is missing?">O'quvchi 'doim takrorlash ➔ 10 qadam yurish ➔ keyingi kostyum' qildi. Lekin mushuk titrab, ko'rinmay qoldi. Skriptda qaysi blok tushib qolgan?</p>
    <div class="quiz-box">
      <div class="quiz-options">
        <div class="quiz-opt" onclick="checkQuiz(this, false)">
          <span>A)</span> <span data-ru="Не хватает блока 'повернуть на 15 градусов'" data-en="Missing 'turn 15 degrees'">15 darajaga burilish bloki yetishmayapti</span>
        </div>
        <div class="quiz-opt" onclick="checkQuiz(this, true)">
          <span>B)</span> <span data-ru="Не хватает блока задержки 'ждать (0.1) секунд'" data-en="Missing 'wait (0.1) seconds' pacing block">Kadrlar oralig'idagi 'kutish (0.1) sekund' bloki qo'yilmagan</span>
        </div>
        <div class="quiz-opt" onclick="checkQuiz(this, false)">
          <span>C)</span> <span data-ru="Нужно удалить Scratch и переустановить компьютер" data-en="Must delete Scratch and reinstall OS">Kompyuterni o'chirib yoqish kerak</span>
        </div>
      </div>
      <button class="fix-btn" onclick="toggleTestFix()">
        <span class="btn-txt" data-ru="🔍 Посмотреть Разбор / Решение" data-en="🔍 View Breakdown / Solution">🔍 Yechim Tahlilini Ko'rish</span>
      </button>
      <div class="test-fix-box" id="testFixBox" style="display:none; margin-top:12px; padding:12px; background:rgba(16,185,129,0.08); border-left:3px solid var(--green); border-radius:4px;">
        <b style="color:var(--green);" data-ru="Правильный ответ: B!" data-en="Correct Answer: B!">To'g'ri javob: B!</b>
        <p style="margin-top:4px; font-size:12px;" data-ru="Компьютер выполняет циклы со скоростью тысяч операций в секунду. Без блока 'wait 0.1 secs' костюмы сменяются мгновенно, и глаз видит лишь хаос!" data-en="Modern processors loop thousands of times per second. Without 'wait (0.1) secs', costumes swap instantaneously into visual noise!">Kompyuter sikllarni sekundiga minglab marta aylantiradi. Agar `wait (0.1) seconds` qo'yilmasa, kadrlar bir zumda almashib, ko'zga faqat titrash bo'lib ko'rinadi!</p>
      </div>
    </div>
  </section>""")

    # Slide 11: Hands-on Arena (25 min)
    slides.append("""  <!-- SLIDE 11: HANDS-ON ARENA -->
  <section class="slide" data-phase="Amaliyot|Практика|Hands-on Lab" data-time="60:00–72:00">
    <div class="eyebrow" data-ru="ПРАКТИЧЕСКАЯ АРЕНА · 25 МИНУТ" data-en="HANDS-ON ARENA · 25 MINUTES">AMALIY ARENA · 25 DAQIQA</div>
    <h2 data-ru="Большая Лаборатория: Оживите Своего Персонажа!" data-en="Hands-on Lab: Bring Your Animated Hero to Life!">Katta Amaliy Laboratoriya: O'z Qahramoningizni Jonlantiring!</h2>
    <p class="lede" data-ru="Запустите студию анимации playground/index.html или откройте Scratch 3.0 и выполните 4 задания." data-en="Open playground/index.html or Scratch 3.0 on your computer and complete the 4 animation quests.">Kompyuteringizda <b>playground/index.html</b> ilovasini oching yoki Scratch 3.0 da 4 ta topshiriqni bajaring:</p>
    <div class="grid c2" style="margin-top:16px;">
      <div class="card">
        <h3 data-ru="Чек-лист аниматора" data-en="Animator Checklist">Amaliy Bosqichlar Ro'yxati</h3>
        <ol style="margin-left:18px; line-height:1.8; font-size:13px;">
          <li data-ru="Выбрать спрайт с минимум 2 костюмами ходьбы (Cat, Pico или Nano)" data-en="Pick a sprite with at least 2 walking costumes (Cat, Pico, Nano)">Kamida 2 ta qadam kostyumi bor spraytni tanlash (Cat, Pico, Nano)</li>
          <li data-ru="Собрать цикл плавной ходьбы с блоком wait (0.12) сек" data-en="Assemble smooth walk loop with wait (0.12) secs">`wait (0.12)` bilan silliq qadam tashlash siklini qurish</li>
          <li data-ru="Настроить стиль вращения 'влево-вправо', чтобы не переворачиваться" data-en="Configure 'left-right' rotation style to avoid flipping">Chapga yurganda yiqilmaslik uchun 'left-right' stilini qo'yish</li>
          <li data-ru="Добавить облако диалога 'Say' при нажатии на пробел!" data-en="Trigger 'Say' speech bubble on Space key press!">Probel bosilganda chiroyli gapiruvchi pufakcha chiqarish!</li>
        </ol>
      </div>
      <div class="card" style="text-align:center;">
        <span class="pill" data-ru="Таймер арены" data-en="Arena Timer">Kiber-Taymer</span>
        <div style="font-family:'JetBrains Mono', monospace; font-size:48px; font-weight:800; color:var(--accent); margin:12px 0;" id="arenaTimer">25:00</div>
        <div style="display:flex; justify-content:center; gap:8px;">
          <button type="button" class="dock-btn" onclick="startArenaTimer(25*60)" style="background:var(--accent); color:#00214A; font-weight:800;" data-ru="▶️ Старт" data-en="▶️ Start">▶️ Boshlash</button>
          <button type="button" class="dock-btn" onclick="resetArenaTimer()" style="border:1px solid var(--rule);" data-ru="🔄 Сброс" data-en="🔄 Reset">🔄 Qayta o'rnatish</button>
        </div>
        <div style="display:flex; justify-content:center; gap:8px; margin-top:14px;">
          <a href="projects/starter_jonli_animatsiya.sb3" download class="dock-btn" style="text-decoration:none; display:inline-flex; align-items:center; gap:4px; font-size:11px; padding:6px 10px; border:1px solid var(--rule); color:var(--ink);" data-ru="📥 Скачать Starter (.sb3)" data-en="📥 Download Starter (.sb3)">📥 Starter Loyiha (.sb3)</a>
          <a href="projects/yechim_jonli_animatsiya.sb3" download class="dock-btn teacher-solution-only" style="text-decoration:none; display:inline-flex; align-items:center; gap:4px; font-size:11px; padding:6px 10px; border:1px solid var(--accent); color:var(--accent);" data-ru="⭐ Скачать Решение (.sb3)" data-en="⭐ Download Solution (.sb3)">⭐ Oltin Yechim (.sb3)</a>
        </div>
      </div>
    </div>
  </section>""")

    # Slide 12: Bug Hunter
    slides.append("""  <!-- SLIDE 12: BUG HUNTER -->
  <section class="slide" data-phase="Tahlil|Анализ|Bug Hunter" data-time="72:00–76:00">
    <div class="eyebrow" data-ru="ОХОТА ЗА БАГАМИ · АНИМАЦИОННЫЕ ЛОВУШКИ" data-en="BUG HUNTER · ANIMATION TRAPS">KIBER-DETEKTIV · ANIMATSIYA TUZOQLARI</div>
    <h2 data-ru="2 Главные Ошибки: Смещение Центра и Вечные Облака" data-en="2 Core Bugs: Offset Anchors & Sticky Bubbles">Eng Ko'p Uchraydigan 2 ta Xato va Yechim</h2>
    <div class="grid c2" style="margin-top:16px;">
      <div class="card" style="border-left:4px solid var(--accent);">
        <span class="pill" style="color:var(--accent-ink);" data-ru="Ошибка 1: Прыжки в сторону" data-en="Bug 1: Sideways Jumping">Xato 1: Sakrab Ketish</span>
        <h3 data-ru="Смещенный центр костюма" data-en="Misaligned costume center">Kostyum Markazi Qochib Ketishi</h3>
        <p data-ru="Если в редакторе костюм 2 нарисован правее центра, персонаж при ходьбе будет нервно дергаться в сторону." data-en="If costume 2 is offset off-center in the paint editor, the sprite visibly jumps sideways every step.">Agar 2-kostyum markazdan chetga chizilgan bo'lsa, qadam tashlaganda qahramon bir sakrab o'ngga-chapga qaltiraydi.</p>
        <div style="margin-top:6px; font-size:12px; color:var(--green); font-weight:700;" data-ru="✅ Yechim: Выделить спрайт и совместить синий крестик с кружком холста!" data-en="✅ Fix: Select sprite in Paint Editor and snap center crosshair!">✅ Yechim: Muharrirda spraytni belgilab, markazdagi nishonga to'g'irlang!</div>
      </div>
      <div class="card" style="border-left:4px solid var(--accent);">
        <span class="pill" style="color:var(--accent-ink);" data-ru="Ошибка 2: Зависшее облачко" data-en="Bug 2: Sticky Speech Bubble">Xato 2: O'chmaydigan Gap</span>
        <h3 data-ru="Зависшее речевое облако" data-en="Sticky speech bubble that never hides">O'chmay Qolgan Pufakcha</h3>
        <p data-ru="Команда 'say [Привет]' без указания секунд оставляет текст на экране навсегда." data-en="Invoking untimed 'say [Hello]' leaves dialogue on stage indefinitely.">Soniya ko'rsatilmagan `say` pufakchani butun o'yin davomida o'chirmasdan qoldiradi.</p>
        <div style="margin-top:6px; font-size:12px; color:var(--green); font-weight:700;" data-ru="✅ Yechim: Использовать 'say for (2) secs' или очищать через 'say []'!" data-en="✅ Fix: Use 'say for (2) secs' or clear with empty 'say []'!">✅ Yechim: `say for (2) secs` ishlating yoki vaqt o'tgach bo'sh `say []` yuboring!</div>
      </div>
    </div>
  </section>""")

    # Slide 13: 3-Tiered Homework
    slides.append("""  <!-- SLIDE 13: HOMEWORK -->
  <section class="slide" data-phase="Uy vazifasi|Домашнее задание|Homework" data-time="76:00–78:00">
    <div class="eyebrow" data-ru="10-БАЛЛЬНАЯ СИСТЕМА · 3 УРОВНЯ СЛОЖНОСТИ" data-en="10-POINT RUBRIC · 3 TIERS">10 BALLIK MEZON · 3 BOSQICHLI UY VAZIFASI</div>
    <h2 data-ru="Домашнее Задание: Создайте Мультфильм-Сценку!" data-en="Homework Mission: Build an Animated Dialogue Scene!">Mustaqil Vazifa: 2 Qahramonli Multfilm Yarating!</h2>
    <div class="grid c3" style="margin-top:20px;">
      <div class="card" style="border-top:4px solid var(--ink-3);">
        <span class="pill" data-ru="1-Уровень · 4 балла" data-en="Tier 1 · 4 pts">1-Bosqich (4 Ball)</span>
        <h3 data-ru="База: Плавная ходьба" data-en="Base: Smooth Walk">Baza: Silliq Qadam</h3>
        <p data-ru="Создать персонажа с 2 костюмами, который ходит от одного края сцены до другого без переворачивания." data-en="Create a 2-costume sprite that walks cleanly between screen edges without flipping.">2 ta kostyumli qahramon yaratish, u chapdan o'ngga ag'darilmasdan qadam tashlasin.</p>
      </div>
      <div class="card" style="border-top:4px solid var(--accent);">
        <span class="pill" style="color:var(--accent-ink);" data-ru="2-Уровень · 4 балла" data-en="Tier 2 · 4 pts">2-Bosqich (4 Ball)</span>
        <h3 data-ru="Проект: Диалог 2 героев" data-en="Project: 2-Hero Dialogue">Amaliyot: 2 Qahramon Diologi</h3>
        <p data-ru="Добавить второго героя. При встрече они здороваются облаками 'Say' и издают звуки!" data-en="Add a second hero. Upon meeting, both exchange 'Say' speech bubbles with audio FX!">2-qahramonni qo'shish. Ular uchrashganda bir-biriga pufakcha orqali salom bersin!</p>
      </div>
      <div class="card" style="border-top:4px solid var(--green);">
        <span class="pill" style="color:var(--green);" data-ru="3-Уровень · 2 балла" data-en="Tier 3 · 2 pts">3-Bosqich (2 Ball)</span>
        <h3 data-ru="Кибер-Вызов: Бег с шифтом" data-en="Cyber Challenge: Shift Sprint">Kiber-Chaqiruv: Tezkor Yugurish</h3>
        <p data-ru="Настроить ускорение: при зажатом пробеле персонаж меняет костюмы в 2 раза быстрее и бежит!" data-en="Add sprint mechanics: holding Space halves the wait delay into a rapid sprint!">Probel bosib turilganda qadamlar tezligi 2 barobar oshib, yugurish rejimiga o'tsin!</p>
      </div>
    </div>
    <div class="card" style="margin-top:16px; background:rgba(0,240,255,0.06); border:1px solid rgba(0,240,255,0.2);">
      <p data-ru="Выполнить задание можно интерактивно в файле vazifa.html с автосохранением в браузере или на печатном бланке varaqa.html." data-en="You can complete the homework interactively in vazifa.html (with LocalStorage auto-save) or via printed varaqa.html.">Topshiriqni <b>vazifa.html</b> ilovasida (avtomatik saqlanadi) yoki <b>varaqa.html</b> qog'ozida topshirishingiz mumkin.</p>
    </div>
  </section>""")

    # Slide 14: Summary & Cheat Sheet
    slides.append("""  <!-- SLIDE 14: SUMMARY & CHEAT SHEET -->
  <section class="slide" data-phase="Xulosa|Итоги|Summary" data-time="78:00–80:00">
    <div class="eyebrow" data-ru="ИТОГИ УРОКА · ПАМЯТКА АНИМАТОРА" data-en="KEY TAKEAWAYS · ANIMATOR CHEAT SHEET">DARS YAKUNI · ANIMATOR SPRAVOCHNIGI</div>
    <h2 data-ru="Чему Мы Научились: Золотые Правила Анимации" data-en="What We Mastered: Golden Rules of Sprite Animation">Bugun O'rganganlarimiz: Jonli Animatsiya Qoidalari</h2>
    <div class="grid c3" style="margin-top:20px;">
      <div class="card">
        <h3 data-ru="👗 Костюмы (Costumes)" data-en="👗 Costumes">👗 Kostyumlar</h3>
        <p data-ru="next costume переключает кадры. Имена walk-1, walk-2 делают проект понятным." data-en="next costume cycles frames. Semantic names keep scripts organized.">`next costume` kadrlarni almashtiradi. To'g'ri nomlar loyihani tushunarli qiladi.</p>
      </div>
      <div class="card">
        <h3 data-ru="⏱️ Задержка (Pacing)" data-en="⏱️ Delay Pacing">⏱️ Kutish (Pacing)</h3>
        <p data-ru="wait (0.1–0.15) secs создает естественную скорость шагов для человеческого глаза." data-en="wait (0.1–0.15) secs creates the optimal natural gait for human perception.">`wait (0.1–0.15)` sekund inson ko'zi uchun eng tabiiy va ravon qadam tezligidir.</p>
      </div>
      <div class="card">
        <h3 data-ru="💬 Облака (Say/Think)" data-en="💬 Speech Bubbles">💬 Pufakchalar</h3>
        <p data-ru="say for (2) secs автоматически исчезает вовремя, не засоряя сцену диалогом." data-en="say for (2) secs self-cleans gracefully, preventing clutter on stage.">`say for (2) secs` vaqt o'tgach o'z-o'zidan yopilib, sahnani toza saqlaydi.</p>
      </div>
    </div>
  </section>""")

    all_slides_html = "\n\n".join(slides)
    tpl = re.sub(r'<div class="stage">[\s\S]*?</div><!-- /stage -->', f'<div class="stage">\n{all_slides_html}\n</div><!-- /stage -->', tpl)

    # 14 NOTES Triplets
    notes_obj = {
        "uz": [
            ["Darsga Kirish", "Animatsiya nimaligini va qahramonni qanday jonlantirishimizni e'lon qiling.", "1-slaydni ekranga chiqaring."],
            ["Uy Vazifasi Tahlili", "O'tgan darsdagi Jarvis ovozli boshqaruvi va isListening xatosini ko'rsating.", "3 ta dvigatelni sinfdan so'rang."],
            ["Flipbook Tushunchasi", "Disney multfilmlari qanday chizilishini tushuntiring.", "Kadrlar ketma-ketligini doskada ko'rsating."],
            ["Kostyumlar Tuzilmasi", "Scratchdagi Costumes bo'limi va markazlashtirish qoidasini tushuntiring.", "Noto'g'ri markaz oqibatini ayting."],
            ["Interaktiv Slayd", "Smartboardda kadrlarni qo'lda bosing va avto-qadamni yoqing.", "Pufakcha chiqarishni ko'rsating."],
            ["Qadam Tashlash Sikli", "next costume va wait 0.1 juftligini doskaga yozing.", "Nega kutish shartligini tushuntiring."],
            ["Burilish Uslubi", "left-right uslubini ko'rsating.", "Mushuk chalqancha yotib qolmasligini ta'kidlang."],
            ["Diolog Pufakchalari", "say va think bloklarining farqini tushuntiring.", "Vaqtli va doimiy pufakchalarni taqqoslang."],
            ["Ovoz Sinxronlash", "Qadam tovushlarini start sound bilan ulashni ko'rsating.", "play until done xatosini ayting."],
            ["Kiber-Quiz", "O'quvchilardan to'g'ri variantni so'rang.", "Doskada variantni bosib yechimni oching."],
            ["Amaliy Laboratoriya", "O'quvchilarga playground ilovasini ochishni ayting.", "25 daqiqalik taymerni yoqing."],
            ["Xatolar Tahlili", "Markaz siljishi va o'chmaydigan pufakcha yechimini ko'rsating.", "Daftarga qayd qildiring."],
            ["Uy Vazifasi", "10 ballik mezonni (4-4-2) tushuntiring.", "vazifa.html ilovasini eslating."],
            ["Dars Yakuni", "Animatsiyaning 3 oltin qoidasini takrorlang.", "Faol o'quvchilarni baholang."]
        ],
        "ru": [
            ["Введение в урок", "Объявите классу, что сегодня мы учим спрайты по-настоящему ходить и бегать.", "Откройте 1-й слайд на проекторе."],
            ["Разбор Д/З", "Покажите ошибку с повторным запуском микрофона из урока 25.", "Повторите 3 двигателя Voice AI."],
            ["Эффект Flipbook", "Объясните покадровую магию мультипликации Disney.", "Покажите быструю смену рисунков."],
            ["Анатомия костюмов", "Разберите вкладку Костюмы и важность центрирования спрайта.", "Предупредите о смещении центра."],
            ["Интерактивный тренажер", "Нажимайте кадры на смартборде и включите цикл ходьбы.", "Покажите речевое облако."],
            ["Алгоритм ходьбы", "Запишите связку next costume + wait 0.1 на доске.", "Объясните частоту кадров."],
            ["Стиль вращения", "Покажите настройку left-right.", "Объясните, почему кот ходит вверх ногами."],
            ["Речевые облака", "Сравните блоки say и think.", "Покажите очистку облака через пустой текст."],
            ["Синхронизация звука", "Покажите запуск щелчков шагов через start sound.", "Предупредите о блокировке play until done."],
            ["Кибер-Тест", "Спросите класс о причине бешеного мелькания спрайта.", "Откройте правильный ответ B."],
            ["Практическая арена", "Дайте старт 25-минутной лаборатории в playground.", "Включите таймер на экране."],
            ["Анализ ловушек", "Разберите прыгающий спрайт и зависший текст.", "Покажите выравнивание привязки."],
            ["Домашнее задание", "Огласите 10-балльную систему (4-4-2).", "Напомните про интерактивный vazifa.html."],
            ["Итоги урока", "Повторите 3 золотых правила аниматора.", "Выставите оценки за спаренный урок."]
        ],
        "en": [
            ["Lesson Intro", "Announce to students that we are giving our sprites animated walking legs.", "Display Slide 1."],
            ["Homework Review", "Review the mic restart and lowercase pitfalls from Lesson 25.", "Quiz students on the 3 AI engines."],
            ["Flipbook Concept", "Explain sequential frame playback inspired by classic Disney animation.", "Illustrate walk cycles."],
            ["Costume Anatomy", "Examine the Costumes tab and anchor point alignment rules.", "Highlight centering crosshairs."],
            ["Interactive Simulator", "Interact with the slide simulator and trigger walking animations.", "Show speech bubbles."],
            ["Walking Loop", "Diagram next costume coupled with wait (0.1) secs on board.", "Explain visual FPS perception."],
            ["Rotation Style", "Demonstrate the left-right rotation guard.", "Prevent inverted upside-down walking."],
            ["Speech Bubbles", "Distinguish between 'say' and 'think' comic bubbles.", "Show how timed blocks self-clear."],
            ["Audio Sync", "Wire footstep sound effects using non-blocking 'start sound'.", "Warn against 'play until done'."],
            ["Cyber Quiz", "Poll the class regarding rapid frame jitter.", "Reveal solution B on screen."],
            ["Hands-on Arena", "Direct students to open playground/index.html.", "Activate 25-min countdown timer."],
            ["Pitfall Autopsy", "Analyze anchor misalignment and sticky bubbles.", "Demonstrate center-snapping."],
            ["Homework Rubric", "Clarify the 10-point rubric breakdown (4-4-2).", "Point out vazifa.html auto-save."],
            ["Summary & Wrap-up", "Recap Costumes, Delay Pacing, and Dialogue bubbles.", "Record grades."]
        ]
    }
    notes_json = json.dumps(notes_obj, ensure_ascii=False, indent=2)
    tpl = re.sub(r'var NOTES\s*=\s*\{[\s\S]*?\};', f'var NOTES = {notes_json};', tpl)

    # Interactive Slide JS for Costume Simulator
    slide_js = """
// ============================================================
// SLIDE 5: SCRATCH CAT WALK CYCLE SIMULATOR LOGIC
// ============================================================
var currentCostume = "costume1";
var isAutoWalking = false;
var autoWalkInterval = null;
var walkDelay = 150; // ms
var posX = 40;
var dir = 1;
var arenaTimerInterval = null;

function updateCatBadges() {
  var bCostume = document.getElementById("costumeBadge");
  var bDir = document.getElementById("dirBadge");
  var bPos = document.getElementById("posXBadge");
  var btn = document.getElementById("autoWalkBtn");
  var spd = document.getElementById("speedBtn");

  if (bCostume) {
    if (currentCostume === "costume1") {
      bCostume.textContent = currentLang === "ru" ? "costume1 (cat-a · Покой)" : (currentLang === "en" ? "costume1 (cat-a · Stance)" : "costume1 (cat-a · Turish)");
    } else {
      bCostume.textContent = currentLang === "ru" ? "costume2 (cat-b · Шаг)" : (currentLang === "en" ? "costume2 (cat-b · Stride)" : "costume2 (cat-b · Qadam)");
    }
  }
  if (bDir) {
    if (dir === 1) {
      bDir.textContent = currentLang === "ru" ? "90° (Вправо)" : (currentLang === "en" ? "90° (Right)" : "90° (O'ngga)");
    } else {
      bDir.textContent = currentLang === "ru" ? "-90° (Влево)" : (currentLang === "en" ? "-90° (Left)" : "-90° (Chapga)");
    }
  }
  if (bPos) bPos.textContent = Math.round(posX);
  if (btn) {
    if (isAutoWalking) {
      btn.textContent = currentLang === "ru" ? "⏹️ Остановить" : (currentLang === "en" ? "⏹️ Stop Loop" : "⏹️ To'xtatish");
      btn.style.background = "#FF5555";
      btn.style.color = "#FFFFFF";
    } else {
      btn.textContent = currentLang === "ru" ? "▶️ Авто-Ходьба (Цикл)" : (currentLang === "en" ? "▶️ Auto-Walk Loop" : "▶️ Avto-Qadam Tashlash");
      btn.style.background = "var(--accent)";
      btn.style.color = "#00214A";
    }
  }
  if (spd) {
    var sec = (walkDelay / 1000).toFixed(2) + "s";
    spd.textContent = "⚡ " + sec;
  }
}

function setCostume(name) {
  if (isAutoWalking) toggleAutoWalk();
  currentCostume = name;
  var p1 = document.getElementById("scratchCatPose1");
  var p2 = document.getElementById("scratchCatPose2");
  var mover = document.getElementById("scratchCatMover");
  if (!p1 || !p2 || !mover) return;

  if (name === "costume1") {
    p1.style.display = "block";
    p2.style.display = "none";
  } else {
    p1.style.display = "none";
    p2.style.display = "block";
    posX += dir * 10;
    mover.style.left = posX + "px";
  }
  playStepChime();
  updateCatBadges();
}

function toggleAutoWalk() {
  var p1 = document.getElementById("scratchCatPose1");
  var p2 = document.getElementById("scratchCatPose2");
  var mover = document.getElementById("scratchCatMover");
  var stage = document.getElementById("scratchStageArea");

  if (isAutoWalking) {
    clearInterval(autoWalkInterval);
    isAutoWalking = false;
    updateCatBadges();
  } else {
    isAutoWalking = true;
    updateCatBadges();
    autoWalkInterval = setInterval(function() {
      if (!mover || !p1 || !p2) return;
      currentCostume = (currentCostume === "costume1") ? "costume2" : "costume1";
      p1.style.display = (currentCostume === "costume1") ? "block" : "none";
      p2.style.display = (currentCostume === "costume2") ? "block" : "none";

      var stageW = stage ? stage.clientWidth : 700;
      posX += dir * 12;

      if (posX > stageW - 110) {
        dir = -1;
        mover.style.transform = "scaleX(-1)";
      } else if (posX < 30) {
        dir = 1;
        mover.style.transform = "scaleX(1)";
      }

      mover.style.left = posX + "px";
      playStepChime();
      updateCatBadges();
    }, walkDelay);
  }
}

function changeWalkSpeed() {
  if (walkDelay === 150) walkDelay = 300;
  else if (walkDelay === 300) walkDelay = 80;
  else walkDelay = 150;

  if (isAutoWalking) {
    clearInterval(autoWalkInterval);
    autoWalkInterval = setInterval(function() {
      var p1 = document.getElementById("scratchCatPose1");
      var p2 = document.getElementById("scratchCatPose2");
      var mover = document.getElementById("scratchCatMover");
      var stage = document.getElementById("scratchStageArea");
      if (!mover || !p1 || !p2) return;
      currentCostume = (currentCostume === "costume1") ? "costume2" : "costume1";
      p1.style.display = (currentCostume === "costume1") ? "block" : "none";
      p2.style.display = (currentCostume === "costume2") ? "block" : "none";

      var stageW = stage ? stage.clientWidth : 700;
      posX += dir * 12;
      if (posX > stageW - 110) { dir = -1; mover.style.transform = "scaleX(-1)"; }
      else if (posX < 30) { dir = 1; mover.style.transform = "scaleX(1)"; }
      mover.style.left = posX + "px";
      playStepChime();
      updateCatBadges();
    }, walkDelay);
  }
  updateCatBadges();
}

function resetWalk() {
  if (isAutoWalking) toggleAutoWalk();
  posX = 40;
  dir = 1;
  currentCostume = "costume1";
  var mover = document.getElementById("scratchCatMover");
  var p1 = document.getElementById("scratchCatPose1");
  var p2 = document.getElementById("scratchCatPose2");
  if (mover) {
    mover.style.transform = "scaleX(1)";
    mover.style.left = "40px";
  }
  if (p1 && p2) {
    p1.style.display = "block";
    p2.style.display = "none";
  }
  updateCatBadges();
}

function playStepChime() {
  try {
    var ctx = new (window.AudioContext || window.webkitAudioContext)();
    var osc = ctx.createOscillator();
    var gain = ctx.createGain();
    osc.type = "sine";
    osc.frequency.setValueAtTime(currentCostume === "costume1" ? 440 : 550, ctx.currentTime);
    gain.gain.setValueAtTime(0.04, ctx.currentTime);
    gain.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + 0.06);
    osc.connect(gain);
    gain.connect(ctx.destination);
    osc.start();
    osc.stop(ctx.currentTime + 0.06);
  } catch(e) {}
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

// Hook setLang to update dynamic HUD labels
var _origSetLang = window.setLang;
window.setLang = function(lang) {
  if (typeof _origSetLang === 'function') _origSetLang(lang);
  updateCatBadges();
};
"""
    tpl = tpl.replace("</script>", slide_js + "\n</script>")

    with open(os.path.join(lesson_dir, "prezentatsiya.html"), "w", encoding="utf-8") as f:
        f.write(tpl)
    print(f"  ✓ Created: prezentatsiya.html")

    # --- 1.2 VARAQA.HTML ---
    v_tpl = TPL_VAR
    v_tpl = v_tpl.replace("{{LESSON_NUM}}", "26")
    v_tpl = v_tpl.replace("{{TITLE_UZ}}", "Scratchda Jonli Animatsiyalar va Kostyumlar")
    v_tpl = v_tpl.replace("{{TITLE_RU}}", "Живая Анимация и Костюмы в Scratch")
    v_tpl = v_tpl.replace("{{TITLE_EN}}", "Live Sprite Animations & Costumes in Scratch")
    v_tpl = v_tpl.replace("{{COHORT_LABEL_UZ}}", "5–6-sinf")
    v_tpl = v_tpl.replace("{{COHORT_LABEL_RU}}", "5–6 класс")
    v_tpl = v_tpl.replace("{{COHORT_LABEL_EN}}", "Grades 5–6")

    v_tpl = v_tpl.replace("{{META_UZ}}", "2-Chorak · 10-hafta · 26-dars · Junior Creators & Kiber-Gigiyena Track")
    v_tpl = v_tpl.replace("{{META_RU}}", "2-я четверть · 10-я неделя · 26-й урок · Junior Creators & Кибер-Гигиена")
    v_tpl = v_tpl.replace("{{META_EN}}", "Quarter 2 · Week 10 · Lesson 26 · Junior Creators & Cyber Hygiene Track")

    v_tpl = v_tpl.replace("{{MISSION_UZ}}", "Scratchda spraytga ko'p kadrli kostyumlarni ulash, qadam tashlash siklini (Next costume) vaqt bilan boshqarish hamda pufakcha orqali gapirtirish.")
    v_tpl = v_tpl.replace("{{MISSION_RU}}", "Создание пошаговой анимации спрайта через костюмы в Scratch, настройка цикла ходьбы и речевых облаков.")
    v_tpl = v_tpl.replace("{{MISSION_EN}}", "Building multi-frame costume walking animations in Scratch, controlling pacing delay, and triggering speech bubbles.")

    v_tpl = v_tpl.replace("{{SEC1_TITLE_UZ}}", "1-Qism: Kadrlar Ketma-ketligi va Kutish Vaqti (Pacing)")
    v_tpl = v_tpl.replace("{{SEC1_TITLE_RU}}", "Часть 1: Последовательность Кадров и Задержка (Pacing)")
    v_tpl = v_tpl.replace("{{SEC1_TITLE_EN}}", "Part 1: Frame Sequences and Delay Pacing")
    v_sec1 = """    <div class="box-grid">
      <div class="box">
        <h4 data-ru="1. Смена костюмов" data-en="1. Costume Cycling">1. Kostyumlarni Almashtirish</h4>
        <p data-ru="Какой блок переключает спрайт на следующую позу? Запишите название:" data-en="Which block toggles the sprite to its next frame pose?">Spraytni navbatdagi kadrga o'tkazuvchi asosiy blok nomini yozing:</p>
        <div class="write-line"></div>
        <div class="write-line"></div>
      </div>
      <div class="box">
        <h4 data-ru="2. Задержка времени" data-en="2. Pacing Delay">2. Kadrlar Oralig'idagi Vaqt</h4>
        <p data-ru="Что произойдет, если убрать блок 'wait 0.1 secs'? Опишите поведение кота:" data-en="What happens if 'wait 0.1 secs' is omitted? Describe cat behavior:">'wait 0.1 secs' qo'yilmasa nima sodir bo'ladi? Mushuk harakatini tasvirlang:</p>
        <div class="write-line"></div>
        <div class="write-line"></div>
      </div>
    </div>"""
    v_tpl = v_tpl.replace("{{SEC1_CONTENT}}", v_sec1)

    v_tpl = v_tpl.replace("{{SEC2_TITLE_UZ}}", "2-Qism: Kod Tahlili va To'g'ri Sikl Qurish")
    v_tpl = v_tpl.replace("{{SEC2_TITLE_RU}}", "Часть 2: Анализ Кода и Построение Цикла")
    v_tpl = v_tpl.replace("{{SEC2_TITLE_EN}}", "Part 2: Code Analysis & Loop Architecture")
    v_sec2 = """    <div class="code-snippet">// ⚠️ Kodni to'ldiring: silliq qadam tashlash va chetdan qaytish:
when green flag clicked
set rotation style [left-right]
forever
  move (10) steps
  next ____________________ // Kadrni almashtirish bloki
  wait (________) seconds   // Tavsiya etilgan qadam tezligi
  if on edge, bounce
end</div>
    <p style="margin-top:4px;" data-ru="Запишите недостающие значения в коде выше:" data-en="Fill in the missing values from the snippet above:">Yuqoridagi kodda bo'sh qoldirilgan joylarga to'g'ri qiymatlarni yozing:</p>
    <div class="write-line"></div>"""
    v_tpl = v_tpl.replace("{{SEC2_CONTENT}}", v_sec2)

    v_tpl = v_tpl.replace("{{SEC3_TITLE_UZ}}", "3-Qism: Amaliy Laboratoriya (4 ta Sinov Sinovi)")
    v_tpl = v_tpl.replace("{{SEC3_TITLE_RU}}", "Часть 3: Практическая Лаборатория (Таблица 4 Тестов)")
    v_tpl = v_tpl.replace("{{SEC3_TITLE_EN}}", "Part 3: Hands-on Lab (4 Tests Audit Table)")
    v_sec3 = """    <p data-ru="Протестируйте проект в Scratch или playground/index.html и заполните таблицу:" data-en="Verify animation tests in Scratch or playground/index.html and complete the table:">Scratch dasturida yoki <b>playground/index.html</b> ilovasida 4 ta mezonni tekshiring:</p>
    <div class="box" style="margin-top:6px;">
      <table style="width:100%; border-collapse:collapse; font-size:8.5pt;">
        <thead>
          <tr style="border-bottom:1px solid var(--rule); text-align:left;">
            <th style="padding:4px 6px;">#</th>
            <th style="padding:4px 6px;" data-ru="Анимационный элемент" data-en="Animation Feature">Animatsiya Elementi</th>
            <th style="padding:4px 6px;" data-ru="Ожидаемое поведение" data-en="Expected Behavior">Kutilgan Natija</th>
            <th style="padding:4px 6px;" data-ru="Статус" data-en="Status">Holat</th>
          </tr>
        </thead>
        <tbody>
          <tr style="border-bottom:1px dashed var(--hair);">
            <td style="padding:4px 6px;">1</td>
            <td style="padding:4px 6px;" data-ru="Смена ног (walk-1 / walk-2)" data-en="Leg toggle (walk-1 / walk-2)">Oyoqlar almashishi (walk-1 va walk-2)</td>
            <td style="padding:4px 6px;" data-ru="Плавная походка без дергания" data-en="Smooth walk without jitter">Ravon qadam, titrash yo'q</td>
            <td style="padding:4px 6px;" data-ru="[ &nbsp; ] Готово" data-en="[ &nbsp; ] Done">[ &nbsp; ] OK</td>
          </tr>
          <tr style="border-bottom:1px dashed var(--hair);">
            <td style="padding:4px 6px;">2</td>
            <td style="padding:4px 6px;" data-ru="Разворот у стены" data-en="Wall Bounce">Devordan qaytish</td>
            <td style="padding:4px 6px;" data-ru="Не переворачивается вверх ногами" data-en="Does not flip upside down">Boshi pastga qulab tushmaydi</td>
            <td style="padding:4px 6px;" data-ru="[ &nbsp; ] Готово" data-en="[ &nbsp; ] Done">[ &nbsp; ] OK</td>
          </tr>
          <tr style="border-bottom:1px dashed var(--hair);">
            <td style="padding:4px 6px;">3</td>
            <td style="padding:4px 6px;" data-ru="Речевое облако (Say)" data-en="Speech Bubble (Say)">Gapiruvchi pufakcha (Say)</td>
            <td style="padding:4px 6px;" data-ru="Исчезает ровно через 2 секунды" data-en="Fades after exactly 2 seconds">Roppa-rosa 2 soniyada o'chadi</td>
            <td style="padding:4px 6px;" data-ru="[ &nbsp; ] Готово" data-en="[ &nbsp; ] Done">[ &nbsp; ] OK</td>
          </tr>
          <tr>
            <td style="padding:4px 6px;">4</td>
            <td style="padding:4px 6px;" data-ru="Звук шага (Start sound)" data-en="Step Audio (Start sound)">Qadam tovushi (Start sound)</td>
            <td style="padding:4px 6px;" data-ru="Звучит синхронно с шагом" data-en="Plays in sync with footstep">Qadam tashlanganda yangraydi</td>
            <td style="padding:4px 6px;" data-ru="[ &nbsp; ] Готово" data-en="[ &nbsp; ] Done">[ &nbsp; ] OK</td>
          </tr>
        </tbody>
      </table>
    </div>"""
    v_tpl = v_tpl.replace("{{SEC3_CONTENT}}", v_sec3)

    v_sec4 = """    <div class="box-grid" style="margin-top:6px;">
      <div class="box">
        <h4 data-ru="1-Уровень: База (4 балла)" data-en="Tier 1: Base (4 pts)">1-Daraja: Baza (4 ball)</h4>
        <p data-ru="Создать персонажа с 2 костюмами, который ходит от края до края без переворотов." data-en="Create a 2-costume sprite walking between stage borders without flipping.">2 ta kostyumli personaj yaratish, u devordan qaytganda teskari aylanmasin.</p>
        <div class="write-line"></div>
      </div>
      <div class="box">
        <h4 data-ru="2-Уровень: Проект (4 балла)" data-en="Tier 2: Project (4 pts)">2-Daraja: Amaliyot (4 ball)</h4>
        <p data-ru="Добавить второго персонажа и организовать диалог через облака Say." data-en="Introduce a second sprite and choreograph a dialogue via Say bubbles.">2-qahramonni qo'shib, ular uchrashganda pufakchalar orqali salomlashish dialogini qilish.</p>
        <div class="write-line"></div>
      </div>
    </div>
    <div class="box" style="margin-top:6px;">
      <h4 data-ru="3-Уровень: Кибер-Вызов (2 балла)" data-en="Tier 3: Cyber Challenge (2 pts)">3-Daraja: Kiber-Chaqiruv (2 ball)</h4>
      <p data-ru="Сделать бег на Shift/Пробел: уменьшить задержку wait в 2 раза при зажатой клавише." data-en="Add sprint mode: halve the wait delay when holding the Space bar.">Probel bosib turilganda qadamlar tezligini 2 marta oshirib, yugurish rejimini hosil qilish.</p>
      <div class="write-line"></div>
    </div>"""
    v_tpl = v_tpl.replace("{{SEC4_CONTENT}}", v_sec4)

    with open(os.path.join(lesson_dir, "varaqa.html"), "w", encoding="utf-8") as f:
        f.write(v_tpl)
    print(f"  ✓ Created: varaqa.html")

    # --- 1.3 VAZIFA.HTML ---
    vz_tpl = TPL_VAZ
    vz_tpl = vz_tpl.replace("{{LESSON_NUM}}", "26")
    vz_tpl = vz_tpl.replace("{{TITLE_UZ}}", "Scratchda Jonli Animatsiyalar va Kostyumlar")
    vz_tpl = vz_tpl.replace("{{TITLE_RU}}", "Живая Анимация и Костюмы в Scratch")
    vz_tpl = vz_tpl.replace("{{TITLE_EN}}", "Live Sprite Animations & Costumes in Scratch")
    vz_tpl = vz_tpl.replace("{{COHORT_LABEL_UZ}}", "5–6-sinf")
    vz_tpl = vz_tpl.replace("{{COHORT_LABEL_RU}}", "5–6 класс")
    vz_tpl = vz_tpl.replace("{{COHORT_LABEL_EN}}", "Grades 5–6")

    vz_tpl = vz_tpl.replace("{{META_UZ}}", "2-Chorak · 10-hafta · 26-dars · Mustaqil Kiber-Laboratoriya")
    vz_tpl = vz_tpl.replace("{{META_RU}}", "2-я четверть · 10-я неделя · 26-й урок · Самостоятельная кибер-лаборатория")
    vz_tpl = vz_tpl.replace("{{META_EN}}", "Quarter 2 · Week 10 · Lesson 26 · Independent Cyber Lab")

    vz_tpl = vz_tpl.replace("{{DESC_UZ}}", "Animatsiyalar, kadrlar tezligi va gapiruvchi pufakchalar bo'yicha 3 ta topshiriqni bajaring. Javoblaringiz avtomatik saqlanadi.")
    vz_tpl = vz_tpl.replace("{{DESC_RU}}", "Выполните 3 задания по анимации костюмов, темпу шагов и диалогам. Прогресс сохраняется автоматически.")
    vz_tpl = vz_tpl.replace("{{DESC_EN}}", "Complete 3 tasks on costume cycling, pacing, and dialogue bubbles. Progress auto-saves.")

    vz_tpl = vz_tpl.replace("{{T1_TITLE_UZ}}", "1-Topshiriq: Kadrlar va Kutish Qoidasi (Baza — 4 ball)")
    vz_tpl = vz_tpl.replace("{{T1_TITLE_RU}}", "Задание 1: Кадры и Правило Задержки (База — 4 балла)")
    vz_tpl = vz_tpl.replace("{{T1_TITLE_EN}}", "Task 1: Costumes & Delay Rule (Base — 4 pts)")
    vz_tpl = vz_tpl.replace("{{T1_DESC_UZ}}", "Nega 'next costume' blokidan so'ng 'wait (0.1) secs' qo'yish shart? Agar kutish qo'yilmasa nima sodir bo'lishini tushuntiring:")
    vz_tpl = vz_tpl.replace("{{T1_DESC_RU}}", "Почему после блока 'next costume' обязательно ставить 'wait (0.1) secs'? Что происходит без задержки?")
    vz_tpl = vz_tpl.replace("{{T1_DESC_EN}}", "Why must 'wait (0.1) secs' follow 'next costume'? Explain what happens when delay is omitted:")

    vz_tpl = vz_tpl.replace("{{T2_TITLE_UZ}}", "2-Topshiriq: 2 Qahramon Diologi Ssenariysi (Amaliyot — 4 ball)")
    vz_tpl = vz_tpl.replace("{{T2_TITLE_RU}}", "Задание 2: Сценарий Диалога 2 Героев (Проект — 4 балла)")
    vz_tpl = vz_tpl.replace("{{T2_TITLE_EN}}", "Task 2: 2-Hero Dialogue Script (Project — 4 pts)")
    vz_tpl = vz_tpl.replace("{{T2_DESC_UZ}}", "Ikkita sprayt (masalan Mushuk va It) uchrashganda 'say for (2) secs' orqali nima deb salomlashadi? Ularning gaplarini yozing:")
    vz_tpl = vz_tpl.replace("{{T2_DESC_RU}}", "Напишите реплики двух спрайтов (например, Кота и Собаки) при встрече через блоки 'say for (2) secs':")
    vz_tpl = vz_tpl.replace("{{T2_DESC_EN}}", "Write dialogue lines for two sprites meeting using 'say for (2) secs' blocks:")

    vz_tpl = vz_tpl.replace("{{T3_TITLE_UZ}}", "3-Topshiriq: Kiber-Chaqiruv — Burilish va Tezlik (2 ball)")
    vz_tpl = vz_tpl.replace("{{T3_TITLE_RU}}", "Задание 3: Кибер-Вызов — Поворот и Спринт (2 балла)")
    vz_tpl = vz_tpl.replace("{{T3_TITLE_EN}}", "Task 3: Cyber Challenge — Rotation & Sprint (2 pts)")
    vz_tpl = vz_tpl.replace("{{T3_DESC_UZ}}", "Qahramon chapga yurganda teskari aylanmasligi uchun qaysi blok tanlanadi? Tez yugurish uchun wait qanday o'zgartiriladi?")
    vz_tpl = vz_tpl.replace("{{T3_DESC_RU}}", "Какой блок предотвращает переворот кота при движении влево? Как изменить wait для быстрого бега?")
    vz_tpl = vz_tpl.replace("{{T3_DESC_EN}}", "Which block stops the sprite from flipping upside down when moving left? How should wait be adjusted for sprinting?")

    vz_banner = """  <!-- SCRATCH PROJECT DOWNLOAD BANNER -->
  <div style="background:var(--panel); border:1px solid var(--rule); border-radius:12px; padding:16px 20px; margin-bottom:20px; display:flex; flex-wrap:wrap; justify-content:space-between; align-items:center; gap:12px;">
    <div>
      <div style="font-weight:800; font-size:14px; color:var(--ink);" data-ru="Файлы Проекта Scratch 3.0" data-en="Scratch 3.0 Project Files">Scratch 3.0 Loyiha Fayllari</div>
      <div style="font-size:12px; color:var(--ink-2); margin-top:2px;" data-ru="Скачайте файл и откройте в Scratch (Файл ➔ Загрузить с компьютера)" data-en="Download file and open in Scratch (File ➔ Load from computer)">Faylni yuklab olib, Scratch dasturida oching (Fayl ➔ Kompyuterdan yuklash)</div>
    </div>
    <div style="display:flex; gap:10px;">
      <a href="projects/starter_jonli_animatsiya.sb3" download class="btn" style="text-decoration:none; display:inline-flex; align-items:center; gap:6px; font-size:12px; font-weight:700; padding:8px 14px; border:1px solid var(--rule); color:var(--ink);" data-ru="📥 Скачать Starter (.sb3)" data-en="📥 Download Starter (.sb3)">📥 Starter Loyiha (.sb3)</a>
      <a href="projects/yechim_jonli_animatsiya.sb3" download class="btn btn-primary teacher-solution-only" style="text-decoration:none; display:inline-flex; align-items:center; gap:6px; font-size:12px; font-weight:800; padding:8px 14px; background:var(--accent); color:#00214A; border:none;" data-ru="⭐ Скачать Решение (.sb3)" data-en="⭐ Download Solution (.sb3)">⭐ Oltin Yechim (.sb3)</a>
    </div>
  </div>\n  <div id="tasks">"""
    vz_tpl = vz_tpl.replace('<div id="tasks">', vz_banner)

    with open(os.path.join(lesson_dir, "vazifa.html"), "w", encoding="utf-8") as f:
        f.write(vz_tpl)
    print(f"  ✓ Created: vazifa.html")

    # --- 1.4 TEACHER_READING.MD ---
    tr_content = """# 26-Dars: O'qituvchi Uchun Metodik Qo'llanma (Teacher Briefing)

**Kohorta:** 5–6-Sinf · Junior Creators & Kiber-Gigiyena Track  
**Mavzu:** Scratchda Jonli Animatsiyalar: Kostyumlar, Qadam Tashlash va Gapiruvchi Pufakchalar  
**Ajratilgan vaqt:** 80 daqiqa (Juftlik blok / Double Block)  
**Amaliy natija:** Scratch 3.0 da kadrlar ketma-ketligi orqali haqiqiy harakat illyuziyasini qurish, personajni ravon yurgizish, teskari aylanmaslik qalqoni va diolog pufakchalarini yaratish.

---

## 1. 5 Daqiqalik Darsoldi Konspekti (O'qituvchiga Eslatma)
Bolalar ko'pincha multfilmlar o'z-o'zidan harakatlanadi deb o'ylashadi.
Bugun ular multfilm ortidagi **Disney tamoyili — Flipbook (kadrlar almashishi)** sirini o'rganadilar:
1. **`next costume`:** Harakat fazalari (`walk1` ➔ `walk2`) ketma-ket almashadi.
2. **`wait (0.1–0.15) seconds`:** Inson ko'zi uchun tabiiy va qulay harakat tezligi.
3. **`set rotation style [left-right]`:** Chapga yurganda bosh pastga qulab tushmaslik kafolati.
4. **`say [Matn] for (2) secs`:** Vaqt o'tgach o'z-o'zidan yopiluvchi nutq pufakchalari.

---

## 2. 80 Daqiqalik Vaqt Xaritasi (Double Block Roadmap)
| Vaqt | Bosqich | O'qituvchi amali | O'quvchi harakati |
|---|---|---|---|
| **00–04 daq** | Titul & Motivatsiya | Proyektorda 1-slaydni ochish, bugun personajga jon kiritishimizni e'lon qilish | Multfilm tamoyilini tushunish |
| **04–10 daq** | O'tgan Dars Tahlili (HW Review) | 25-darsdagi Jarvis ovozli boshqaruvi va mikrofon holatini tekshirish | STT, NLP, TTS zanjirini takrorlash |
| **10–16 daq** | Flipbook Tamoyili | Statik rasmlarning tez almashishi orqali harakat illyuziyasini tushuntirish | Daftarga 3 ta kadr chizish |
| **16–22 daq** | Kostyumlar Tuzilishi | Costumes bo'limi, nomlash qoidasi va markaz nishoni | Markazlashtirish qoidasini yozish |
| **22–30 daq** | Jonli Simulyator (Slayd 5) | Smartboardda kadrlarni qo'lda bosing, avto-yurishni yoqing va pufakcha chiqaring | Doskaga chiqib tajriba qilish |
| **30–40 daq** | Algoritm, Burilish & Quiz | 6–9 slaydlar: `wait 0.1`, `rotation style`, `say` va 10-slayddagi kiber-test | Kiber-quiz javobini belgilash |
| **40–65 daq (25 min)** | Katta Amaliy Arena | Har bir o'quvchi kompyuterida `playground/index.html` yoki Scratch 3.0 ni ochish | 4 ta amaliy missiyani bajarish |
| **65–72 daq (7 min)** | Juftlikda Peer Review | Partadoshlar bir-birining qahramoni qadamlarini va pufakchasini sinaydi | O'rtoqlar loyihasini baholash |
| **72–76 daq (4 min)** | Xatolar Tahlili (Bug Hunter) | Noto'g'ri markaz va o'chmaydigan pufakcha xatolarini fosh qilish | To'g'rilash usulini yozish |
| **76–80 daq (4 min)** | Baholash va Vazifa | 10 ballik mezon asosida baholash, `vazifa.html` ni berish | Ish varaqalarini topshirish |

---

## 3. Baholash Mezoni (10 Ballik Standart)
- **1–4 Ball (Baza):** Qahramon 2 ta kostyum orqali ravon qadam tashlab yurdi, teskari ag'darilmadi.
- **5–7 Ball (Standart):** Qadamlar tezligi to'g'ri (`wait 0.12`), 2-qahramon qo'shilib salomlashish pufakchasi chiqdi.
- **8–10 Ball (Junior Animator):** Shift/Probel bosilganda tezkor yugurish rejimi ishlaydi, qadam tovushlari ulandi va ish varaqasi 100% to'ldirildi.
"""
    with open(os.path.join(lesson_dir, "TEACHER_READING.md"), "w", encoding="utf-8") as f:
        f.write(tr_content)
    print(f"  ✓ Created: TEACHER_READING.md")

    # --- 1.5 PLAYGROUND/INDEX.HTML ---
    play_svg1, play_svg2 = load_clean_scratch_svgs(prefix="pg")
    playground_html = f"""<!DOCTYPE html>
<html lang="uz" data-theme="dark">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title data-ru="Scratch Анимационная Студия (5–6 класс)" data-en="Scratch Animation Studio (Grades 5–6)">Scratch Animatsiya Studiyasi (5–6-sinf)</title>
<link rel="icon" type="image/svg+xml" href="/assets/favicon.svg">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Manrope:wght@600;700;800&family=Source+Sans+3:wght@400;600;700&family=JetBrains+Mono:wght@400;700&display=swap">
<style>
:root {{
  --bg: #050E1F; --panel: #0B1A38; --panel-2: #122852;
  --ink: #F0F4FA; --ink-2: #A5B6D0; --ink-3: #6C819F;
  --rule: #1B355A; --accent: #00F0FF; --green: #10B981;
}}
:root[data-theme="light"] {{
  --bg: #F0F4FA; --panel: #FFFFFF; --panel-2: #E8EEF8;
  --ink: #00214A; --ink-2: #384A68; --ink-3: #7586A2;
  --rule: #DCE4EF; --accent: #0284C7; --green: #059669;
}}
* {{ box-sizing: border-box; margin: 0; padding: 0; }}
body {{
  font-family: 'Source Sans 3', sans-serif;
  background: var(--bg);
  color: var(--ink);
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}}
header {{
  padding: 14px 24px;
  background: var(--panel);
  border-bottom: 1px solid var(--rule);
  display: flex;
  justify-content: space-between;
  align-items: center;
}}
.brand {{ display: flex; align-items: center; gap: 10px; font-weight: 800; }}
.badge {{ background: var(--accent); color: #00214A; padding: 3px 8px; border-radius: 4px; font-size: 11px; font-weight: 800; }}
main {{
  flex: 1;
  max-width: 900px;
  width: 100%;
  margin: 20px auto;
  padding: 0 16px;
  display: flex;
  flex-direction: column;
  gap: 16px;
}}
.stage-card {{
  background: var(--panel);
  border: 1px solid var(--rule);
  border-radius: 14px;
  padding: 20px;
  display: flex;
  flex-direction: column;
  position: relative;
}}
#stageArea {{
  width: 100%;
  height: 260px;
  background: radial-gradient(ellipse at 50% 30%, rgba(255,255,255,0.06), rgba(0,0,0,0.3)), var(--panel-2);
  border: 2px solid var(--rule);
  border-radius: 10px;
  position: relative;
  overflow: hidden;
}}
#stageHud {{
  position: absolute;
  top: 10px;
  left: 14px;
  right: 14px;
  display: flex;
  justify-content: space-between;
  font-family: 'JetBrains Mono', monospace;
  font-size: 11.5px;
  color: var(--ink-2);
  z-index: 2;
  pointer-events: none;
}}
#floorLine {{
  position: absolute;
  left: 0;
  right: 0;
  bottom: 24px;
  height: 2px;
  background: linear-gradient(90deg, transparent, var(--accent), transparent);
}}
#catSpriteMover {{
  position: absolute;
  left: 50px;
  bottom: 24px;
  width: 96px;
  height: 101px;
  transition: transform 0.1s ease, left 0.1s linear;
  user-select: none;
  transform-origin: 50% 100%;
}}
#bubble {{
  position: absolute;
  bottom: 125px;
  left: 60px;
  background: #FFFFFF;
  color: #001026;
  padding: 8px 14px;
  border-radius: 12px;
  font-weight: 800;
  font-size: 13px;
  display: none;
  box-shadow: 0 4px 16px rgba(0,0,0,0.3);
  z-index: 3;
}}
#bubble::after {{
  content: "";
  position: absolute;
  bottom: -6px;
  left: 18px;
  border-width: 6px 6px 0;
  border-style: solid;
  border-color: #FFFFFF transparent;
}}
.controls-grid {{
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(160px, 1fr));
  gap: 10px;
  width: 100%;
  margin-top: 16px;
}}
button.btn {{
  background: var(--panel-2);
  color: var(--ink);
  border: 1px solid var(--rule);
  padding: 10px 14px;
  border-radius: 8px;
  font-weight: 700;
  font-size: 12.5px;
  cursor: pointer;
  transition: all 0.2s ease;
}}
button.btn:hover {{ border-color: var(--accent); color: var(--accent); }}
button.btn-primary {{ background: var(--accent); color: #00214A; border: none; font-weight: 800; }}
button.btn-primary:hover {{ opacity: 0.9; }}
.lang-btn {{
  padding: 4px 8px;
  background: var(--panel-2);
  border: 1px solid var(--rule);
  border-radius: 6px;
  color: var(--ink-2);
  font-size: 11px;
  font-weight: 800;
  cursor: pointer;
}}
.lang-btn.is-active {{
  background: var(--accent);
  color: #00214A;
  border-color: var(--accent);
}}
</style>
</head>
<body>
<header>
  <div class="brand">
    <span>TARGET ANIMATION STUDIO</span>
    <span class="badge" data-ru="5–6 КЛАСС" data-en="GRADE 5–6">5–6-SINF</span>
  </div>
  <div style="display:flex; gap:6px; align-items:center;">
    <button class="lang-btn is-active" data-lang="uz" onclick="setLang('uz')">UZ</button>
    <button class="lang-btn" data-lang="ru" onclick="setLang('ru')">RU</button>
    <button class="lang-btn" data-lang="en" onclick="setLang('en')">EN</button>
    <button class="btn" style="padding:6px 10px; font-size:11px; margin-left:8px;" onclick="toggleTheme()" data-ru="🌓 Тема" data-en="🌓 Theme">🌓 Mavzu</button>
  </div>
</header>
<main>
  <div class="stage-card">
    <div id="stageArea">
      <div id="stageHud">
        <div><span class="t" data-ru="Костюм: " data-en="Costume: ">Kostyum: </span><b id="pgCostume" style="color:var(--accent);">costume1 (cat-a)</b></div>
        <div><span>X: </span><b id="pgX">50</b> &nbsp;|&nbsp; <span>Y: </span><b>-40</b></div>
        <div><span class="t" data-ru="Направление: " data-en="Direction: ">Yo'nalish: </span><b id="pgDir" style="color:var(--green);">90°</b></div>
      </div>
      <div id="floorLine"></div>
      <div id="bubble" data-ru="Привет! Я иду вперед!" data-en="Hello! I'm walking forward!">Salom! Men oldinga yurmoqdaman!</div>
      <div id="catSpriteMover">
        {play_svg1}
        {play_svg2}
      </div>
    </div>
    <div class="controls-grid">
      <button class="btn btn-primary" onclick="toggleWalk()" id="walkBtn" data-ru="▶️ Запустить Ходьбу" data-en="▶️ Start Walk Loop">▶️ Qadam Tashlashni Boshlash</button>
      <button class="btn" onclick="setCostumeManual('costume1')" data-ru="🐾 1-Костюм (cat-a)" data-en="🐾 Costume 1 (cat-a)">🐾 1-Kostyum (cat-a)</button>
      <button class="btn" onclick="setCostumeManual('costume2')" data-ru="👣 2-Костюм (cat-b)" data-en="👣 Costume 2 (cat-b)">👣 2-Kostyum (cat-b)</button>
      <button class="btn" onclick="sayHello()" data-ru="💬 Сказать «Привет!»" data-en="💬 Say 'Hello!'">💬 Gapiruvchi Pufakcha</button>
      <button class="btn" onclick="toggleSpeed()" id="speedBtn" data-ru="⚡ Скорость: 0.12с" data-en="⚡ Speed: 0.12s">⚡ Tezlik: 0.12s</button>
      <button class="btn" onclick="resetCat()" data-ru="🔄 В Начало" data-en="🔄 Reset Pos">🔄 Boshiga Qaytish</button>
    </div>
  </div>
</main>
<script>
var p1 = document.getElementById("pg_scratchCatPose1");
var p2 = document.getElementById("pg_scratchCatPose2");
var mover = document.getElementById("catSpriteMover");
var bubble = document.getElementById("bubble");
var isWalking = false;
var walkInterval = null;
var posX = 50;
var dir = 1;
var currentCostume = "costume1";
var delayMs = 120;
var currentLang = "uz";

function updatePgHud() {{
  var bCost = document.getElementById("pgCostume");
  var bX = document.getElementById("pgX");
  var bDir = document.getElementById("pgDir");
  var btn = document.getElementById("walkBtn");
  if (bCost) bCost.textContent = currentCostume === "costume1" ? "costume1 (cat-a)" : "costume2 (cat-b)";
  if (bX) bX.textContent = Math.round(posX);
  if (bDir) bDir.textContent = dir === 1 ? "90°" : "-90°";
  if (btn) {{
    if (isWalking) {{
      btn.textContent = currentLang === "ru" ? "⏹️ Остановить" : (currentLang === "en" ? "⏹️ Stop Loop" : "⏹️ To'xtatish");
      btn.style.background = "#FF5555";
      btn.style.color = "#FFFFFF";
    }} else {{
      btn.textContent = currentLang === "ru" ? "▶️ Запустить Ходьбу" : (currentLang === "en" ? "▶️ Start Walk Loop" : "▶️ Qadam Tashlashni Boshlash");
      btn.style.background = "var(--accent)";
      btn.style.color = "#00214A";
    }}
  }}
}}

function setCostumeManual(name) {{
  if (isWalking) toggleWalk();
  currentCostume = name;
  if (p1 && p2) {{
    p1.style.display = currentCostume === "costume1" ? "block" : "none";
    p2.style.display = currentCostume === "costume2" ? "block" : "none";
  }}
  updatePgHud();
}}

function toggleWalk() {{
  if (isWalking) {{
    clearInterval(walkInterval);
    isWalking = false;
    updatePgHud();
  }} else {{
    isWalking = true;
    updatePgHud();
    walkInterval = setInterval(function() {{
      currentCostume = (currentCostume === "costume1") ? "costume2" : "costume1";
      if (p1 && p2) {{
        p1.style.display = currentCostume === "costume1" ? "block" : "none";
        p2.style.display = currentCostume === "costume2" ? "block" : "none";
      }}
      posX += dir * 10;
      
      var stageW = document.getElementById("stageArea").clientWidth;
      if (posX > stageW - 110) {{
        dir = -1;
        mover.style.transform = "scaleX(-1)";
      }} else if (posX < 30) {{
        dir = 1;
        mover.style.transform = "scaleX(1)";
      }}
      mover.style.left = posX + "px";
      bubble.style.left = (posX + 10) + "px";
      updatePgHud();
    }}, delayMs);
  }}
}}

function sayHello() {{
  bubble.style.display = "block";
  setTimeout(function() {{ bubble.style.display = "none"; }}, 2500);
}}

function toggleSpeed() {{
  if (delayMs === 120) delayMs = 60;
  else if (delayMs === 60) delayMs = 240;
  else delayMs = 120;
  var btn = document.getElementById("speedBtn");
  var sec = (delayMs/1000).toFixed(2) + "s";
  btn.textContent = currentLang === "ru" ? "⚡ Скорость: " + sec : (currentLang === "en" ? "⚡ Speed: " + sec : "⚡ Tezlik: " + sec);
  if (isWalking) {{
    clearInterval(walkInterval);
    walkInterval = setInterval(function() {{
      currentCostume = (currentCostume === "costume1") ? "costume2" : "costume1";
      if (p1 && p2) {{
        p1.style.display = currentCostume === "costume1" ? "block" : "none";
        p2.style.display = currentCostume === "costume2" ? "block" : "none";
      }}
      posX += dir * 10;
      var stageW = document.getElementById("stageArea").clientWidth;
      if (posX > stageW - 110) {{ dir = -1; mover.style.transform = "scaleX(-1)"; }}
      else if (posX < 30) {{ dir = 1; mover.style.transform = "scaleX(1)"; }}
      mover.style.left = posX + "px";
      bubble.style.left = (posX + 10) + "px";
      updatePgHud();
    }}, delayMs);
  }}
}}

function resetCat() {{
  if (isWalking) toggleWalk();
  posX = 50;
  dir = 1;
  currentCostume = "costume1";
  mover.style.left = posX + "px";
  mover.style.transform = "scaleX(1)";
  if (p1 && p2) {{
    p1.style.display = "block";
    p2.style.display = "none";
  }}
  bubble.style.left = "60px";
  bubble.style.display = "none";
  updatePgHud();
}}

function setLang(lang) {{
  currentLang = lang;
  document.documentElement.setAttribute("lang", lang);
  document.querySelectorAll(".lang-btn").forEach(function(b) {{
    b.classList.toggle("is-active", b.getAttribute("data-lang") === lang);
  }});
  var attr = "data-" + lang;
  document.querySelectorAll("[data-ru], [data-en]").forEach(function(el) {{
    if (!el.hasAttribute("data-uz-orig")) el.setAttribute("data-uz-orig", el.innerHTML);
    el.innerHTML = (lang === "uz") ? el.getAttribute("data-uz-orig") : (el.getAttribute(attr) || el.getAttribute("data-uz-orig"));
  }});
  updatePgHud();
}}

function toggleTheme() {{
  var cur = document.documentElement.getAttribute("data-theme") || "dark";
  document.documentElement.setAttribute("data-theme", cur === "dark" ? "light" : "dark");
}}
</script>
</body>
</html>"""
    with open(os.path.join(app_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(playground_html)
    print(f"  ✓ Created: playground/index.html")

build_5_6_lesson()
print("🎉 5–6-sinf generation finished!")
