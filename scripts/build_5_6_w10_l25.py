#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
scripts/build_5_6_w10_l25.py — Target Jarvis (5-6-sinf 10-hafta 25-dars)
Compiles:
  1. prezentatsiya.html (14 slides, master chassis, touch controls, in-deck scale, live Jarvis demo)
  2. varaqa.html (2-page printable A4 worksheet with 10-point rubric)
  3. vazifa.html (Interactive homework app with LocalStorage)
  4. TEACHER_READING.md (80-minute double block pedagogical briefing)
  5. studio/index.html (Interactive Target Jarvis Voice Studio for 5-6 graders)
"""

import os
import sys
import json
import re
import subprocess

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
LESSON_DIR = os.path.join(REPO_ROOT, "classes", "5-6-sinf", "10-hafta", "25-dars-target-jarvis-ai-ovozli-yordamchi")
STUDIO_DIR = os.path.join(LESSON_DIR, "studio")
os.makedirs(STUDIO_DIR, exist_ok=True)

# ---------------------------------------------------------------------------
# 1. PREZENTATSIYA.HTML
# ---------------------------------------------------------------------------
def build_prezentatsiya():
    template_path = os.path.join(REPO_ROOT, "assets", "TEMPLATE_PREZENTATSIYA.html")
    with open(template_path, "r", encoding="utf-8") as f:
        tpl = f.read()

    # 1. Replace Title & Brand tag
    title_uz = "25-dars: Target Jarvis — AI Ovozli Yordamchi"
    title_ru = "Урок 25: Target Jarvis — Голосовой AI-Помощник"
    title_en = "Lesson 25: Target Jarvis — AI Voice Assistant"

    tpl = re.sub(r"<title[^>]*>.*?</title>",
                 f'<title data-ru="{title_ru}" data-en="{title_en}">{title_uz}</title>',
                 tpl)

    # Brand tag
    tpl = re.sub(r'<span class="tag"[^>]*>.*?</span>',
                 '<span class="tag" data-ru="5-6 · ВАЙБКОДИНГ" data-en="5-6 · VIBECODING">5-6 · VIBECODING</span>',
                 tpl, count=1)

    # TITLES dict
    titles_dict = {"uz": title_uz, "ru": title_ru, "en": title_en}
    titles_json = json.dumps(titles_dict, ensure_ascii=False, indent=2)
    tpl = re.sub(r'var TITLES\s*=\s*\{[\s\S]*?\};', f'var TITLES = {titles_json};', tpl)

    # Total slides counter default
    tpl = tpl.replace('<span id="totalSlides">6</span>', '<span id="totalSlides">14</span>')

    # SLIDES MARKUP (14 SLIDES)
    slides = []

    # Slide 1: Titul
    slides.append("""  <!-- SLIDE 1: TITUL -->
  <section class="slide is-on" data-phase="Kirish|Введение|Introduction" data-time="00:00–04:00">
    <div class="eyebrow" data-ru="5–6-СИНФ · 10-Я НЕДЕЛЯ · УРОК 25" data-en="GRADES 5–6 · WEEK 10 · LESSON 25">5–6-SINF · 10-HAFTA · 25-DARS</div>
    <h1 data-ru="Target Jarvis: Голосовой AI-Помощник" data-en="Target Jarvis: AI Voice Assistant">Target Jarvis: AI Ovozli Yordamchi</h1>
    <p class="lede" data-ru="Создаем персонального голосового помощника: микрофон распознает речь (STT), мозг понимает команду (NLP), а синтезатор озвучивает ответ (TTS)!" data-en="Building a personal voice assistant: microphone transcribes speech (STT), brain matches intent (NLP), and synthesizer speaks back (TTS)!">Shaxsiy ovozli yordamchimizni quramiz: mikrofon nutqni taniydi (STT), miya niyatni tushunadi (NLP), dinamik esa insondek ovoz chiqarib javob qaytaradi (TTS)!</p>
    <div class="grid c3" style="margin-top:24px;">
      <div class="card">
        <h3 data-ru="Формат урока" data-en="Lesson Format">Format va Davomiylik</h3>
        <p data-ru="Спаренный блок: 2 x 40 минут = 80 минут интенсивной лаборатории" data-en="Double block: 2 x 40 min = 80 min intensive hands-on lab">Juftlik blok: 2 x 40 daqiqa = 80 daqiqalik qizg'in kiber-amaliyot</p>
      </div>
      <div class="card">
        <h3 data-ru="Главная миссия" data-en="Core Mission">Amaliy Missiya</h3>
        <p data-ru="Оживить персонажа Scratch и управлять страницей силой своего голоса" data-en="Animate Scratch characters and control web pages purely by voice commands">Scratch qahramonlarini jonlantirish va veb-sahifani ovoz bilan boshqarish</p>
      </div>
      <div class="card">
        <h3 data-ru="10-Балльная система" data-en="10-Point Rubric">Baholash Mezoni</h3>
        <p data-ru="4 балла: Базовые команды · 4 балла: Свои намерения · 2 балла: Эффекты" data-en="4 pts: Base commands · 4 pts: Custom intents · 2 pts: Sound effects">4 ball: Baza · 4 ball: Shaxsiy buyruqlar · 2 ball: Ovoz effektlari</p>
      </div>
    </div>
  </section>""")

    # Slide 2: Mandatory HW Review
    slides.append("""  <!-- SLIDE 2: MANDATORY HW REVIEW & BRIDGE -->
  <section class="slide" data-phase="Uy Vazifasi Tahlili|Разбор Д/З|HW Review" data-time="04:00–10:00">
    <div class="eyebrow" data-ru="АНАЛИЗ Д/З · РАЗБОР ОШИБОК 24-УРОКА" data-en="HOMEWORK AUDIT · LESSON 24 PITFALLS">UY VAZIFASI TAHLILI · 24-DARS XATOLAR REVIZIYASI</div>
    <h2 data-ru="Разбор Домашнего Задания: Координаты X и Y в Scratch" data-en="Homework Autopsy: X and Y Coordinates in Scratch">O'tgan Dars Vazifasi Tahlili: Scratchda X va Y Koordinatalar</h2>
    <div class="grid c2" style="margin-top:16px;">
      <div class="card" style="border-left:4px solid var(--accent);">
        <span class="pill" style="color:var(--accent-ink);" data-ru="Типичная ошибка" data-en="Common Pitfall">Xato Tahlili (Pitfall)</span>
        <h3 data-ru="Спрайт улетает за пределы сцены или путаются оси" data-en="Sprite flies off-screen or axis inversion">Sprayt ekrandan chiqib ketishi yoki X va Y chalkashishi</h3>
        <p data-ru="Ученики меняли X вместо Y при прыжке вверх, или персонаж застревал у края сцены, потому что не был включен блок проверки границ." data-en="Students altered X instead of Y when jumping up, or sprites got stuck at edges due to missing boundary guards.">Tepaga sakrashda Y o'rniga X o'zgartirilgan, yoki devorga tekkanda qaytish bloki (`if on edge, bounce`) qo'yilmagani uchun sprayt sahnadan chiqib yo'qolgan.</p>
        <pre class="code-snippet" style="margin-top:8px;"><code>// ❌ Xato:
change X by (50) // Tepaga sakramaydi, o'ngga suriladi!</code></pre>
      </div>
      <div class="card" style="border-left:4px solid var(--green);">
        <span class="pill" style="color:var(--green);" data-ru="Золотой стандарт" data-en="Golden Standard">Oltin Yechim (Best Practice)</span>
        <h3 data-ru="Точные оси и проверка краев экрана" data-en="Explicit axes & boundary bounce guards">Aniq koordinatalar va devordan qaytish</h3>
        <p data-ru="X — это горизонталь (влево/вправо), Y — вертикаль (вверх/вниз). Блок 'оттолкнуться от края' удерживает персонажа внутри холста." data-en="X is horizontal (left/right), Y is vertical (up/down). The 'bounce on edge' block keeps characters inside the visible stage.">X gorizontal (chap/o'ng), Y vertikal (tepa/past). Devordan qaytish va aylanishni `left-right` qilish qahramonni har doim to'g'ri ushlaydi.</p>
        <pre class="code-snippet" style="margin-top:8px;"><code>// ✅ To'g'ri:
change Y by (50) // Tepaga sakrash!
if on edge, bounce // Sahnada qolish!</code></pre>
      </div>
    </div>
    <div class="grid c2" style="margin-top:16px;">
      <div class="card">
        <span class="pill" data-ru="Блиц-контроль (30 сек)" data-en="30s Blitz Check">30s Blits-Nazorat</span>
        <p data-ru="Где находится точка (X: 0, Y: 0) на сцене Scratch? Ответ: Ровно по центру холста!" data-en="Where is the point (X: 0, Y: 0) on the Scratch stage? Answer: Exactly at the center of the canvas!">Scratch sahnasining qoq markazidagi koordinata qanday? Javob: <b>(X: 0, Y: 0)</b>!</p>
      </div>
      <div class="card">
        <span class="pill" data-ru="Мост к новому уроку" data-en="Bridge to Topic">Bugungi Darsga Ko'prik</span>
        <p data-ru="Вчера мы управляли спрайтом клавишами. А что, если персонаж будет слышать ваш голос и отвечать? Сегодня мы создаем Jarvis!" data-en="Yesterday we pressed keyboard arrows. What if our sprite could listen to our voice and answer? Today we build Jarvis!">Kecha qahramonni klaviatura bilan yurgizdik. Agar u inson kabi ovozingizni eshitsa va gapirsa-chi? Bugun shaxsiy ovozli AI yaratamiz!</p>
      </div>
    </div>
  </section>""")

    # Slide 3: VUI
    slides.append("""  <!-- SLIDE 3: VUI CONCEPT -->
  <section class="slide" data-phase="Tushuncha|Концепция|Concept" data-time="10:00–16:00">
    <div class="eyebrow" data-ru="ИНТЕРФЕЙС БУДУЩЕГО · VUI" data-en="INTERFACE OF THE FUTURE · VUI">KELAJAK INTERFEYSI · VUI</div>
    <h2 data-ru="От Клавиатуры к Голосу: Эволюция Интерфейсов" data-en="From Keyboard to Voice: Evolution of Interfaces">Klaviaturadan Ovozga: Interfeyslar Evolyutsiyasi</h2>
    <p class="lede" data-ru="Раньше компьютерам писали сложные команды. Затем кликали мышкой. Сегодня — мы просто говорим с искусственным интеллектом." data-en="We once typed arcane commands into terminals. Then we clicked icons. Today, we simply speak to AI with natural voice.">Avval kompyuterlarga murakkab matnli buyruqlar yozilgan. Keyin sichqoncha bilan tugmalar bosilgan. Bugun esa sun'iy intellekt bilan shunchaki gaplashamiz.</p>
    <div class="grid c3" style="margin-top:20px;">
      <div class="card">
        <span class="pill">1980-yillar: CLI</span>
        <h3 data-ru="Командная строка" data-en="Command Line">Matnli Konsol</h3>
        <p data-ru="Черный экран, мигающий курсор и необходимость наизусть помнить сотни сложных команд." data-en="Black screen, blinking cursor, and memorizing hundreds of cryptic terminal commands.">Faqat qora ekran va matn. Har bir buyruqni qo'lda yodlab yozish talab etilgan.</p>
      </div>
      <div class="card">
        <span class="pill">1990–2020: GUI</span>
        <h3 data-ru="Графический экран" data-en="Graphical Screen">Grafik Interfeys</h3>
        <p data-ru="Окна, красивые иконки, кнопки и курсор мыши. Сделало компьютеры доступными каждому ребенку." data-en="Windows, visual icons, buttons, and mouse pointers that made computers intuitive for everyone.">Oynalar, yorliqlar, sichqoncha va sensorli ekranlar. Kompyuterni ommalashtirdi.</p>
      </div>
      <div class="card" style="border:2px solid var(--accent);">
        <span class="pill" style="color:var(--accent-ink);">Bugun: VUI</span>
        <h3 data-ru="Голосовой интерфейс" data-en="Voice Interface">Ovozli Muloqot (VUI)</h3>
        <p data-ru="Siri, Алиса, Alexa и наш Target Jarvis: руки свободны, мы говорим естественным человеческим языком." data-en="Siri, Alexa, Alice, and Target Jarvis: hands-free natural spoken conversation with machines.">Siri, Alexa, Alisa va Target Jarvis: qo'llar bo'sh, kompyuter bilan jonli suhbat!</p>
      </div>
    </div>
  </section>""")

    # Slide 4: 3 Engines Architecture
    slides.append("""  <!-- SLIDE 4: ARCHITECTURE 3 ENGINES -->
  <section class="slide" data-phase="Arxitektura|Архитектура|Architecture" data-time="16:00–22:00">
    <div class="eyebrow" data-ru="3 ДВИГАТЕЛЯ ГОЛОСОВОГО AI" data-en="3 ENGINES OF VOICE AI">OVOZLI AI 3 TA DVIGATELI</div>
    <h2 data-ru="Как Устроен Jarvis: Уши, Мозг и Голос" data-en="How Jarvis Works: Ears, Brain, and Voice">Jarvis Qanday Ishlaydi: Quloq, Miya va Til</h2>
    <p class="lede" data-ru="Голосовой ассистент состоит из трех неразрывных звеньев конвейера: STT ➔ NLP ➔ TTS." data-en="A voice assistant relies on three pipeline pillars: STT ➔ NLP ➔ TTS.">Har qanday aqlli ovozli yordamchi 3 ta asosiy bo'g'indan iborat: STT ➔ NLP ➔ TTS.</p>
    <div style="margin:20px 0; overflow-x:auto;">
      <svg viewBox="0 0 740 210" style="width:100%; max-width:740px; height:auto; display:block; margin:0 auto;">
        <defs>
          <marker id="arrow" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
            <path d="M 0 1 L 8 5 L 0 9 z" fill="var(--accent)" />
          </marker>
        </defs>
        <!-- Engine 1: STT -->
        <rect x="20" y="30" width="200" height="150" rx="12" fill="var(--panel)" stroke="var(--rule)" stroke-width="2" />
        <circle cx="120" cy="75" r="26" fill="rgba(0,240,255,0.12)" stroke="var(--accent)" stroke-width="2" />
        <text x="120" y="82" font-size="22" text-anchor="middle">🎤</text>
        <text x="120" y="125" fill="var(--accent)" font-family="'Manrope', sans-serif" font-weight="800" font-size="14" text-anchor="middle">1. QULOQ (STT)</text>
        <text x="120" y="145" fill="var(--ink-2)" font-family="'Source Sans 3', sans-serif" font-size="11" text-anchor="middle" data-ru="Speech-to-Text" data-en="Speech-to-Text">Nutq ➔ Matn</text>
        <text x="120" y="162" fill="var(--ink-3)" font-family="'JetBrains Mono', monospace" font-size="9.5" text-anchor="middle">webkitSpeechRecognition</text>

        <!-- Arrow 1 -->
        <path d="M 225 105 L 265 105" stroke="var(--accent)" stroke-width="2.5" marker-end="url(#arrow)" />

        <!-- Engine 2: NLP -->
        <rect x="270" y="30" width="200" height="150" rx="12" fill="var(--panel)" stroke="var(--accent)" stroke-width="2" />
        <circle cx="370" cy="75" r="26" fill="rgba(255,17,0,0.12)" stroke="var(--accent)" stroke-width="2" />
        <text x="370" y="82" font-size="22" text-anchor="middle">🧠</text>
        <text x="370" y="125" fill="var(--accent)" font-family="'Manrope', sans-serif" font-weight="800" font-size="14" text-anchor="middle">2. MIYA (NLP)</text>
        <text x="370" y="145" fill="var(--ink-2)" font-family="'Source Sans 3', sans-serif" font-size="11" text-anchor="middle" data-ru="Intent Matching" data-en="Intent Matching">Niyatni Anglash</text>
        <text x="370" y="162" fill="var(--ink-3)" font-family="'JetBrains Mono', monospace" font-size="9.5" text-anchor="middle">text.includes("salom")</text>

        <!-- Arrow 2 -->
        <path d="M 475 105 L 515 105" stroke="var(--accent)" stroke-width="2.5" marker-end="url(#arrow)" />

        <!-- Engine 3: TTS -->
        <rect x="520" y="30" width="200" height="150" rx="12" fill="var(--panel)" stroke="var(--rule)" stroke-width="2" />
        <circle cx="620" cy="75" r="26" fill="rgba(16,185,129,0.12)" stroke="var(--green)" stroke-width="2" />
        <text x="620" y="82" font-size="22" text-anchor="middle">🔊</text>
        <text x="620" y="125" fill="var(--green)" font-family="'Manrope', sans-serif" font-weight="800" font-size="14" text-anchor="middle">3. TIL (TTS)</text>
        <text x="620" y="145" fill="var(--ink-2)" font-family="'Source Sans 3', sans-serif" font-size="11" text-anchor="middle" data-ru="Text-to-Speech" data-en="Text-to-Speech">Matn ➔ Inson Nutqi</text>
        <text x="620" y="162" fill="var(--ink-3)" font-family="'JetBrains Mono', monospace" font-size="9.5" text-anchor="middle">speechSynthesis.speak()</text>
      </svg>
    </div>
  </section>""")

    # Slide 5: Interactive Slide — Live Jarvis Simulator inside presentation
    slides.append("""  <!-- SLIDE 5: INTERACTIVE LIVE JARVIS DEMO -->
  <section class="slide" data-phase="Jonli Sinov|Живой Тест|Live Demo" data-time="22:00–30:00">
    <div class="eyebrow" data-ru="СЕНСОРНЫЙ СИМУЛЯТОР JARVIS НА СМАРТБОРДЕ" data-en="INTERACTIVE JARVIS TOUCH SIMULATOR">INTERAKTIV JARVIS SIMULYATORI</div>
    <h2 data-ru="Попробуйте Прямо Сейчас: Нажимайте Команды или Говорите!" data-en="Try it Right Now: Tap Commands or Speak!">Jonli Sinov: Tugmalarni Bosing yoki Mikrofonda Gapiring!</h2>
    <p class="lede" data-ru="Нажимайте на быстрые карточки команд ниже, чтобы увидеть и услышать работу Jarvis прямо в презентации." data-en="Tap the preset command pills below to watch and hear Jarvis in action right on the slide.">Quyidagi buyruqlarni bosing yoki mikrofonni yoqing: Jarvis ovoz chiqaradi va Scratch mushugi sakraydi!</p>
    
    <div class="grid c2" style="margin-top:14px; align-items:center;">
      <!-- Left: Interactive Visualizer & Scratch Cat -->
      <div class="card" style="text-align:center; padding:18px; position:relative; overflow:hidden;">
        <div id="jarvisPulseRing" style="width:110px; height:110px; border-radius:50%; margin:0 auto 12px; display:flex; align-items:center; justify-content:center; background:radial-gradient(circle, rgba(0,240,255,0.25) 0%, rgba(0,240,255,0.02) 70%); border:2px solid var(--accent); transition:all 0.3s ease;">
          <div id="jarvisCatAvatar" style="font-size:42px; transition:transform 0.3s ease;">🐱</div>
        </div>
        <div id="jarvisLiveStatus" style="font-family:'JetBrains Mono', monospace; font-size:12px; font-weight:700; color:var(--accent);" data-ru="Статус: Готов к командам" data-en="Status: Ready for commands">Holat: Buyruq kutmoqda...</div>
        <div id="jarvisLiveResponse" style="font-size:13px; font-weight:600; color:var(--ink); margin-top:6px; min-height:36px;" data-ru="«Нажмите любую кнопку справа!»" data-en="«Tap any button on the right!»">«O'ng tarafdagi biror tugmani bosing!»</div>
        <div style="margin-top:10px;">
          <button type="button" class="dock-btn" onclick="toggleSlideMic()" id="slideMicBtn" style="background:var(--accent); color:#00214A; font-weight:800; padding:6px 16px;" data-ru="🎤 Включить Микрофон" data-en="🎤 Toggle Mic">🎤 Mikrofonni Yoqish</button>
        </div>
      </div>

      <!-- Right: Touch Presets -->
      <div style="display:flex; flex-direction:column; gap:8px;">
        <button type="button" class="dock-btn" onclick="triggerJarvisPreset('salom')" style="text-align:left; padding:8px 14px; font-size:12px; border:1px solid var(--rule);" data-ru="👋 «Привет, Джарвис!»" data-en="👋 «Hello Jarvis!»">👋 «Salom, Jarvis!»</button>
        <button type="button" class="dock-btn" onclick="triggerJarvisPreset('soat')" style="text-align:left; padding:8px 14px; font-size:12px; border:1px solid var(--rule);" data-ru="⏰ «Сколько сейчас времени?»" data-en="⏰ «What time is it?»">⏰ «Soat necha bo'ldi?»</button>
        <button type="button" class="dock-btn" onclick="triggerJarvisPreset('mushuk')" style="text-align:left; padding:8px 14px; font-size:12px; border:1px solid rgba(0,240,255,0.4); color:var(--accent-ink); font-weight:700;" data-ru="🐱 «Кот, подпрыгни вверх!»" data-en="🐱 «Cat, jump up!»">🐱 «Mushuk, sakra!»</button>
        <button type="button" class="dock-btn" onclick="triggerJarvisPreset('mavzu')" style="text-align:left; padding:8px 14px; font-size:12px; border:1px solid var(--rule);" data-ru="🌓 «Переключи темную/светлую тему»" data-en="🌓 «Toggle dark/light theme»">🌓 «Mavzuni almashtir»</button>
        <button type="button" class="dock-btn" onclick="triggerJarvisPreset('musiqa')" style="text-align:left; padding:8px 14px; font-size:12px; border:1px solid var(--rule);" data-ru="🎵 «Сыграй кибер-мелодию»" data-en="🎵 «Play cyber melody»">🎵 «Kiber-musiqa chal»</button>
        <button type="button" class="dock-btn" onclick="triggerJarvisPreset('latifa')" style="text-align:left; padding:8px 14px; font-size:12px; border:1px solid var(--rule);" data-ru="😂 «Расскажи шутку про программистов»" data-en="😂 «Tell a coder joke»">😂 «IT haqida latifa ayt»</button>
      </div>
    </div>
  </section>""")

    # Slide 6: Engine 1 (STT Deep Dive)
    slides.append("""  <!-- SLIDE 6: ENGINE 1 (STT) -->
  <section class="slide" data-phase="Texnologiya|Технология|Technology" data-time="30:00–36:00">
    <div class="eyebrow" data-ru="1-Й ДВИГАТЕЛЬ · SPEECH-TO-TEXT" data-en="ENGINE 1 · SPEECH-TO-TEXT">1-DVIGATEL · NUTQNI TANISH (STT)</div>
    <h2 data-ru="Уши Компьютера: Web Speech API" data-en="The Computer's Ears: Web Speech API">Kompyuter Quloqlari: Web Speech API</h2>
    <p class="lede" data-ru="В браузер Chrome уже встроен модуль распознавания речи: он слушает микрофон и возвращает текст." data-en="Modern browsers include a native speech recognition engine: it listens to the mic and outputs text.">Chrome va zamonaviy brauzerlarda maxsus nutq qabul qiluvchi dvigatel bor: u mikrofondan kelgan tovushni matnga aylantiradi.</p>
    <div class="grid c2" style="margin-top:16px;">
      <div class="card">
        <h3 data-ru="Как запустить распознавание" data-en="How to activate recognition">Nutq Qabul Qilishni Yoqish</h3>
        <p data-ru="Создаем объект распознавания и указываем язык (узбекский, русский или английский):" data-en="Create the recognition object and configure language:">Dasturda yangi recognition obyektini ochamiz va tilni tanlaymiz:</p>
        <pre class="code-snippet"><code>const rec = new webkitSpeechRecognition();
rec.lang = 'uz-UZ'; // O'zbek tili
rec.continuous = false; // Bitta gap
rec.start(); // Eshitishni boshlash</code></pre>
      </div>
      <div class="card">
        <h3 data-ru="Событие результата onresult" data-en="The onresult event handler">Natijani Tutish (onresult)</h3>
        <p data-ru="Когда ученик произносит фразу, срабатывает событие onresult и передает текст:" data-en="As soon as you speak, the onresult event delivers the recognized transcript:">Siz gapirib bo'lishingiz bilan `onresult` voqeasi ishga tushadi va matnni beradi:</p>
        <pre class="code-snippet"><code>rec.onresult = function(event) {
  let gap = event.results[0][0].transcript;
  console.log("Eshitildi:", gap);
};</code></pre>
      </div>
    </div>
  </section>""")

    # Slide 7: Engine 2 (NLP & Intent Matching)
    slides.append("""  <!-- SLIDE 7: ENGINE 2 (INTENT MATCHING) -->
  <section class="slide" data-phase="Mantiq|Логика|Logic" data-time="36:00–42:00">
    <div class="eyebrow" data-ru="2-Й ДВИГАТЕЛЬ · INTENT MATCHING" data-en="ENGINE 2 · INTENT MATCHING">2-DVIGATEL · NIYATNI ANGLASH (NLP)</div>
    <h2 data-ru="Мозг Ассистента: Распознаем Намерения (Intents)" data-en="The Assistant's Brain: Intent Matching Logic">Yordamchi Miyasi: Niyatni Aniqlash (Intent Matching)</h2>
    <p class="lede" data-ru="Люди говорят по-разному: «Привет», «Салом», «Доброе утро». Задача Jarvis — понять скрытый смысл." data-en="People speak in various ways: 'Hi', 'Hello', 'Good morning'. Jarvis must recognize the underlying intent.">O'quvchilar bir xil gapirmaydi: "Salom", "Salom Jarvis", "Assalomu alaykum". AI kalit so'zlarni qidiradi.</p>
    <div class="grid c2" style="margin-top:16px;">
      <div class="card">
        <h3 data-ru="Секрет .toLowerCase() и .includes()" data-en="Power of .toLowerCase() and .includes()">Kichik Harflar va Kalit So'zlar</h3>
        <p data-ru="Сначала приводим текст к нижнему регистру, чтобы заглавные буквы не мешали сравнению:" data-en="First normalize text to lowercase so case differences don't break logic:">Barcha harflarni kichik qilib olamiz, keyin `includes()` bilan tekshiramiz:</p>
        <pre class="code-snippet"><code>let text = gap.toLowerCase();

if (text.includes("salom")) {
  javob = "Assalomu alaykum do'stim!";
} else if (text.includes("soat")) {
  javob = "Hozir soat " + new Date().toLocaleTimeString();
}</code></pre>
      </div>
      <div class="card">
        <h3 data-ru="Что если команда неизвестна?" data-en="Fallback for Unknown Queries">Noma'lum Buyruq (Fallback)</h3>
        <p data-ru="Если ни одно условие не подошло, ассистент вежливо сообщает, что учится:" data-en="If no rule matches, Jarvis politely explains it hasn't learned that command yet:">Agar shartlar mos kelmasa, dastur xato bermasdan xushmuomala javob qaytaradi:</p>
        <pre class="code-snippet"><code>else {
  javob = "Kechirasiz, bu buyruqni bilmayman. Menga yangi narsa o'rgating!";
}</code></pre>
      </div>
    </div>
  </section>""")

    # Slide 8: Engine 3 (TTS Speech Synthesis)
    slides.append("""  <!-- SLIDE 8: ENGINE 3 (TTS) -->
  <section class="slide" data-phase="Sintez|Синтез|Synthesis" data-time="42:00–48:00">
    <div class="eyebrow" data-ru="3-Й ДВИГАТЕЛЬ · TEXT-TO-SPEECH" data-en="ENGINE 3 · TEXT-TO-SPEECH">3-DVIGATEL · OVOZ CHIQARISH (TTS)</div>
    <h2 data-ru="Голос Ассистента: Движок Речи speechSynthesis" data-en="Voice of the Assistant: speechSynthesis Engine">Yordamchining Tili: speechSynthesis Dvigateli</h2>
    <p class="lede" data-ru="Любой текст из JavaScript можно превратить в живую человеческую речь через встроенный синтезатор." data-en="Any text string can be vocalized as human speech via the browser's native synthesis engine.">Brauzer ichidagi ovoz sintezatori orqali istalgan matnni insoniy ovoz bilan eshittirish mumkin.</p>
    <div class="grid c2" style="margin-top:16px;">
      <div class="card">
        <h3 data-ru="Базовая команда речи" data-en="Basic Speech Utterance">Ovoz Chiqarish Sintaksisi</h3>
        <p data-ru="Создаем объект SpeechSynthesisUtterance и отправляем его в динамик:" data-en="Instantiate a SpeechSynthesisUtterance and pass it to speak():">Gapirilishi kerak bo'lgan jumlani yozamiz va dinamikdan yangratamiz:</p>
        <pre class="code-snippet"><code>function gapir(matn) {
  let utter = new SpeechSynthesisUtterance(matn);
  utter.rate = 1.0;  // Gapirish tezligi
  utter.pitch = 1.1; // Ovoz balandligi
  window.speechSynthesis.speak(utter);
}</code></pre>
      </div>
      <div class="card">
        <h3 data-ru="Настройка тональности и робота" data-en="Tuning Pitch & Speed">Robot va Multfilm Ovozini Sozlash</h3>
        <p data-ru="Меняя pitch (от 0.5 до 2.0), можно сделать голос великана, робота или мультяшного кота:" data-en="Varying pitch (0.5 to 2.0) transforms voice into robot, giant, or cartoon character:">`pitch` qiymatini 1.8 qilsangiz quvnoq multfilm qahramoni, 0.6 qilsangiz bahaybat kiber-robot ovozi chiqadi!</p>
        <ul style="margin-top:8px; line-height:1.7; padding-left:18px;">
          <li data-ru="pitch: 0.6 — Тяжелый Кибер-Робот" data-en="pitch: 0.6 — Heavy Cyber-Robot"><code>pitch: 0.6</code> — Og'ir Kiber-Robot</li>
          <li data-ru="pitch: 1.0 — Обычный Голос" data-en="pitch: 1.0 — Standard Voice"><code>pitch: 1.0</code> — Normal Inson Ovozi</li>
          <li data-ru="pitch: 1.8 — Мультяшный Кот Scratch" data-en="pitch: 1.8 — Cartoon Scratch Cat"><code>pitch: 1.8</code> — Scratch Mushukchasi</li>
        </ul>
      </div>
    </div>
  </section>""")

    # Slide 9: Scratch Cat Integration
    slides.append("""  <!-- SLIDE 9: SCRATCH + VOICE INTEGRATION -->
  <section class="slide" data-phase="Integratsiya|Интеграция|Integration" data-time="48:00–54:00">
    <div class="eyebrow" data-ru="СВЯЗКА SCRATCH И ГОЛОСА" data-en="CONNECTING SCRATCH & VOICE">SCRATCH VA OVOZ BOG'LANISHI</div>
    <h2 data-ru="Управляем Персонажем: Голос Двигает Спрайт!" data-en="Controlling Sprites: Your Voice Moves the Character!">Ovozli Buyruq: Spraytni Harakatga Keltirish!</h2>
    <p class="lede" data-ru="Когда Jarvis распознает «Прыгай!», JavaScript находит HTML/SVG спрайт кота и меняет его координаты." data-en="When Jarvis hears 'Jump!', JavaScript selects the cat element and animates its coordinates.">Siz "Mushuk sakrasin!" deganingizda, JavaScript Scratch mushugini topadi va uni sakratadi!</p>
    <div class="grid c2" style="margin-top:16px;">
      <div class="card">
        <h3 data-ru="Логика прыжка спрайта" data-en="Sprite Jump Trigger">Sakrash Funksiyasi</h3>
        <pre class="code-snippet"><code>function mushukSakrasin() {
  const cat = document.getElementById("cat");
  // Tepaga 80 piksel sakrash:
  cat.style.transform = "translateY(-80px)";
  
  // 500 ms dan so'ng yerga tushish:
  setTimeout(() => {
    cat.style.transform = "translateY(0px)";
  }, 500);
}</code></pre>
      </div>
      <div class="card">
        <h3 data-ru="Связка с намерением (Intent)" data-en="Wiring with Intent">Niyat bilan Bog'lash</h3>
        <pre class="code-snippet"><code>if (text.includes("mushuk") || text.includes("sakra")) {
  mushukSakrasin();
  gapir("Bajarildi! Mushuk sakradi!");
}</code></pre>
        <p style="margin-top:8px; font-size:12px; color:var(--ink-2);" data-ru="Один голосовой триггер запускает одновременно анимацию и звуковой ответ!" data-en="A single voice trigger simultaneously triggers physics animation and spoken response!">Bitta ovozli buyruq bir vaqtning o'zida ham animatsiyani, ham Jarvis ovozini ishga tushiradi!</p>
      </div>
    </div>
  </section>""")

    # Slide 10: Interactive Quiz
    slides.append("""  <!-- SLIDE 10: CYBER QUIZ -->
  <section class="slide" data-phase="Interaktiv Test|Тест|Interactive Quiz" data-time="54:00–60:00">
    <div class="eyebrow" data-ru="КИБЕР-ТЕСТ · ПРОВЕРКА ПОНИМАНИЯ" data-en="CYBER QUIZ · KNOWLEDGE CHECK">KIBER-TEST · BILIMNI TEKSHIRISH</div>
    <h2 data-ru="Кибер-Тест: Что Делает Jarvis в Момент Распознавания?" data-en="Cyber Quiz: What Does Jarvis Do Upon Hearing Speech?">Kiber-Sinov: Jarvis Ovozni Eshitgach Qaysi Amalni Bajaradi?</h2>
    <p class="lede" data-ru="Ученик сказал в микрофон: «Jarvis, включи музыку!». Какой компонент системы решает, какую песню включить?" data-en="A student spoke: 'Jarvis, play music!'. Which engine decides what action to execute?">O'quvchi mikrofon orqali "Jarvis, musiqa chal!" dedi. Qaysi bosqich aynan musiqani yoqish kerakligini belgilaydi?</p>
    <div class="quiz-box">
      <div class="quiz-options">
        <div class="quiz-opt" onclick="checkQuiz(this, false)">
          <span>A)</span> <span data-ru="Только динамик компьютера (TTS)" data-en="The computer speaker alone (TTS)">Faqat kompyuter dinamigi (TTS)</span>
        </div>
        <div class="quiz-opt" onclick="checkQuiz(this, true)">
          <span>B)</span> <span data-ru="Модуль понимания намерений (NLP / text.includes('musiqa'))" data-en="Intent matching engine (NLP / text.includes('music'))">Niyatni anglash bloki (NLP / text.includes("musiqa"))</span>
        </div>
        <div class="quiz-opt" onclick="checkQuiz(this, false)">
          <span>C)</span> <span data-ru="Провод от розетки питания" data-en="The power cable">Rozetka toki simi</span>
        </div>
      </div>
      <button class="fix-btn" onclick="toggleTestFix()">
        <span class="btn-txt" data-ru="🔍 Посмотреть Разбор / Решение" data-en="🔍 View Breakdown / Solution">🔍 Yechim Tahlilini Ko'rish</span>
      </button>
      <div class="test-fix-box" id="testFixBox" style="display:none; margin-top:12px; padding:12px; background:rgba(16,185,129,0.08); border-left:3px solid var(--green); border-radius:4px;">
        <b style="color:var(--green);" data-ru="Правильный ответ: B!" data-en="Correct Answer: B!">To'g'ri javob: B!</b>
        <p style="margin-top:4px; font-size:12px;" data-ru="Микрофон лишь переводит звук в буквы. Именно логика Intent Matching (if / includes) понимает смысл команды и вызывает функцию музыки!" data-en="The microphone only converts sound waves into letters. Intent Matching logic inspects keywords and executes the music function!">Mikrofon tovushni matnga aylantiradi xolos. Niyatni anglash (Intent Matching) sharti esa aynan 'musiqa' so'zini tutib olib, tegishli funksiyani chaqiradi!</p>
      </div>
    </div>
  </section>""")

    # Slide 11: Hands-on Arena (25 min)
    slides.append("""  <!-- SLIDE 11: HANDS-ON ARENA -->
  <section class="slide" data-phase="Amaliyot|Практика|Hands-on Lab" data-time="60:00–72:00">
    <div class="eyebrow" data-ru="ПРАКТИЧЕСКАЯ АРЕНА · 25 МИНУТ" data-en="HANDS-ON ARENA · 25 MINUTES">AMALIY ARENA · 25 DAQIQA</div>
    <h2 data-ru="Большая Лаборатория: Запустите Студию Jarvis!" data-en="Hands-on Lab: Launch Your Jarvis Studio!">Katta Amaliy Laboratoriya: Shaxsiy Jarvis Studiyangizni Yoqing!</h2>
    <p class="lede" data-ru="Откройте папку studio/index.html в браузере, разрешите микрофон и выполните 4 миссии." data-en="Open studio/index.html in Chrome, allow microphone access, and accomplish the 4 missions.">Har bir o'quvchi kompyuterida <b>studio/index.html</b> ni ochadi, mikrofonga ruxsat beradi va 4 ta kiber-missiyani bajaradi:</p>
    <div class="grid c2" style="margin-top:16px;">
      <div class="card">
        <h3 data-ru="Чек-лист миссии" data-en="Mission Checklist">Amaliy Missiyalar Ro'yxati</h3>
        <ol style="margin-left:18px; line-height:1.8; font-size:13px;">
          <li data-ru="Разрешить доступ к микрофону в Chrome" data-en="Grant Chrome microphone permission">Brauzerda mikrofonga ruxsat berish (Allow)</li>
          <li data-ru="Произнести «Привет, Jarvis!» и получить голосовой ответ" data-en="Say 'Hello Jarvis!' and hear spoken reply">"Salom, Jarvis!" deb gapirib ovozli javob olish</li>
          <li data-ru="Сказать «Mushuk sakra» и увидеть анимацию прыжка" data-en="Say 'Cat jump' and verify jump physics">"Mushuk sakra!" buyrug'ida animatsiyani ko'rish</li>
          <li data-ru="Создать СВОЮ новую команду в блоке Custom Intents!" data-en="Create your own custom command in Custom Intents!">O'zingizning yangi shaxsiy buyrug'ingizni kiritish!</li>
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
    <div class="eyebrow" data-ru="ОХОТА ЗА БАГАМИ · РЕАЛЬНЫЕ ЛОВУШКИ" data-en="BUG HUNTER · REAL-WORLD PITFALLS">KIBER-DETEKTIV · REAL TUZOQLAR</div>
    <h2 data-ru="Главные Ошибки: Почему Микрофон Зависает?" data-en="Core Pitfalls: Why Does the Microphone Freeze?">Eng Ko'p Uchraydigan Xatolar va Ularni Yechish</h2>
    <div class="grid c2" style="margin-top:16px;">
      <div class="card" style="border-left:4px solid var(--accent);">
        <span class="pill" style="color:var(--accent-ink);">Xato 1: Ketma-ket Bosish</span>
        <h3 data-ru="InvalidStateError: already started" data-en="InvalidStateError: already started">recognition has already started</h3>
        <p data-ru="Если нажать кнопку микрофона 5 раз подряд, браузер выдаст ошибку и зависнет." data-en="Spamming the start button triggers a browser crash due to unmanaged state.">Tugma qayta-qayta bosilganda mikrofon 2 marta start ololmaydi va xato beradi.</p>
        <pre class="code-snippet"><code>// ✅ Yechim: Bayroq (Flag) qo'yish:
if (!isListening) {
  rec.start();
  isListening = true;
}</code></pre>
      </div>
      <div class="card" style="border-left:4px solid var(--accent);">
        <span class="pill" style="color:var(--accent-ink);">Xato 2: Shovqinli Sinf</span>
        <h3 data-ru="Шум и ложные срабатывания" data-en="Classroom Noise & False Positives">Sinfdagi Shovqin va Xato Eshitish</h3>
        <p data-ru="Когда 15 человек говорят одновременно, микрофон может уловить чужой голос." data-en="When 15 students speak simultaneously, mics catch ambient classroom chatter.">Hamma bir vaqtda baqirsa, mikrofon so'zlarni chalkashtirib yuborishi mumkin.</p>
        <div style="margin-top:8px; font-size:12px; color:var(--ink-2);" data-ru="💡 Решение: В студии Target Jarvis предусмотрены сенсорные кнопки-дублеры (Smartboard Touch Presets) для бесшумного тестирования!" data-en="💡 Solution: Target Jarvis includes direct Touch Preset buttons for silent, bulletproof testing!">💡 Yechim: Studiyamizda sensorli tayyor tugmalar bor — shovqin bo'lsa ham 100% ishlaydi!</div>
      </div>
    </div>
  </section>""")

    # Slide 13: 3-Tiered Homework
    slides.append("""  <!-- SLIDE 13: HOMEWORK -->
  <section class="slide" data-phase="Uy vazifasi|Домашнее задание|Homework" data-time="76:00–78:00">
    <div class="eyebrow" data-ru="10-БАЛЛЬНАЯ СИСТЕМА · 3 УРОВНЯ СЛОЖНОСТИ" data-en="10-POINT RUBRIC · 3 TIERS">10 BALLIK MEZON · 3 BOSQICHLI UY VAZIFASI</div>
    <h2 data-ru="Домашнее Задание: Прокачайте Своего Jarvis!" data-en="Homework Mission: Supercharge Your Jarvis!">Mustaqil Vazifa: Shaxsiy Jarvisingizni Kengaytiring!</h2>
    <div class="grid c3" style="margin-top:20px;">
      <div class="card" style="border-top:4px solid var(--ink-3);">
        <span class="pill">1-Bosqich (4 Ball)</span>
        <h3 data-ru="База: 3 Команды" data-en="Base: 3 Commands">Baza: 3 ta Buyruq</h3>
        <p data-ru="Запустить студию Jarvis, успешно протестировать команды «Салом», «Соат» и «Мавзу» и записать ответы в тетрадь." data-en="Launch Jarvis studio, test 'Hello', 'Time', and 'Theme' commands, and log results in worksheet.">Jarvis studiyasini ochib, "Salom", "Soat" va "Mavzu" buyruqlarini sinab, daftarga yozish.</p>
      </div>
      <div class="card" style="border-top:4px solid var(--accent);">
        <span class="pill" style="color:var(--accent-ink);">2-Bosqich (4 Ball)</span>
        <h3 data-ru="Проект: 2 Свои Команды" data-en="Project: 2 Custom Commands">Amaliyot: 2 ta Yangi Buyruq</h3>
        <p data-ru="Добавить в студию 2 новые команды (например: вопрос о погоде, любимой игре или любимом школьном предмете)." data-en="Add 2 custom commands into Jarvis (e.g., weather query, favorite game, or school subject).">Studiyaga 2 ta yangi buyruq qo'shish (masalan: sevimli o'yin yoki dars jadvali haqida).</p>
      </div>
      <div class="card" style="border-top:4px solid var(--green);">
        <span class="pill" style="color:var(--green);">3-Bosqich (2 Ball)</span>
        <h3 data-ru="Кибер-Вызов: Робот-Тон" data-en="Cyber Challenge: Robot Tone">Kiber-Chaqiruv: Robot Ovozi</h3>
        <p data-ru="Изменить параметр pitch до 0.6 или 1.8 и заставить Jarvis говорить голосом трансформера или мультгероя!" data-en="Adjust pitch to 0.6 or 1.8 to make Jarvis sound like a futuristic transformer or cartoon hero!">Ovoz balandligini (`pitch`) o'zgartirib, Jarvisga haqiqiy robot yoki personaj ovozini berish!</p>
      </div>
    </div>
    <div class="card" style="margin-top:16px; background:rgba(0,240,255,0.06); border:1px solid rgba(0,240,255,0.2);">
      <p data-ru="Выполнить задание можно интерактивно в файле vazifa.html с автосохранением в браузере или на печатном бланке varaqa.html." data-en="You can complete the homework interactively in vazifa.html (with LocalStorage auto-save) or via printed varaqa.html.">Topshiriqni <b>vazifa.html</b> ilovasida (avtomatik saqlanadi) yoki <b>varaqa.html</b> qog'ozida topshirishingiz mumkin.</p>
    </div>
  </section>""")

    # Slide 14: Summary & Cheat Sheet
    slides.append("""  <!-- SLIDE 14: SUMMARY & CHEAT SHEET -->
  <section class="slide" data-phase="Xulosa|Итоги|Summary" data-time="78:00–80:00">
    <div class="eyebrow" data-ru="ИТОГИ УРОКА · ПАМЯТКА" data-en="KEY TAKEAWAYS · CHEAT SHEET">DARS YAKUNI · SPRAVOCHNIK</div>
    <h2 data-ru="Чему Мы Научились: Золотые Правила Voice AI" data-en="What We Mastered: Golden Rules of Voice AI">Bugun O'rganganlarimiz: Voice AI Oltin Qoidalari</h2>
    <div class="grid c3" style="margin-top:20px;">
      <div class="card">
        <h3 data-ru="🎤 STT (Слух)" data-en="🎤 STT (Hearing)">🎤 STT (Quloq)</h3>
        <p data-ru="webkitSpeechRecognition преобразует человеческий голос в текст. Событие onresult возвращает результат." data-en="webkitSpeechRecognition converts spoken words into digital text via onresult.">`webkitSpeechRecognition` inson ovozini matnga aylantiradi. Natijani `onresult` ushlaydi.</p>
      </div>
      <div class="card">
        <h3 data-ru="🧠 NLP (Мышление)" data-en="🧠 NLP (Thinking)">🧠 NLP (Miya)</h3>
        <p data-ru="text.toLowerCase() и .includes('ключ') находят смысл в сказанном и выбирают действие." data-en="text.toLowerCase() and .includes('key') analyze transcript meaning and route commands.">`toLowerCase()` va `.includes()` niyatni aniqlab, qaysi amalni bajarishni hal qiladi.</p>
      </div>
      <div class="card">
        <h3 data-ru="🔊 TTS (Речь)" data-en="🔊 TTS (Speaking)">🔊 TTS (Til)</h3>
        <p data-ru="window.speechSynthesis озвучивает ответ живым голосом. pitch и rate настраивают характер." data-en="window.speechSynthesis articulates responses aloud with tunable pitch and rate.">`speechSynthesis` javobni ovoz chiqarib aytadi. `pitch` va `rate` xarakterni belgilaydi.</p>
      </div>
    </div>
  </section>""")

    all_slides_html = "\n\n".join(slides)

    # Replace stage
    tpl = re.sub(r'<div class="stage">[\s\S]*?</div><!-- /stage -->',
                 f'<div class="stage">\n{all_slides_html}\n</div><!-- /stage -->',
                 tpl)

    # Generate NOTES (14 items)
    notes_obj = {
        "uz": [
            ["Darsga Kirish", "O'quvchilarga bugun o'z shaxsiy Jarvis ovozli yordamchisini yaratishimizni e'lon qiling.", "Proyektorga 1-slaydni oching."],
            ["Uy Vazifasi Tahlili", "O'tgan darsdagi Scratch X va Y koordinatalari xatosini ko'rsating.", "Markaz (0, 0) koordinatasini so'rang."],
            ["VUI Tushunchasi", "CLI dan VUI gacha evolyutsiyani tushuntiring.", "Siri va Alisadan kim qanday foydalanishini so'rang."],
            ["3 Dvigatel Sxemasi", "STT (quloq), NLP (miya), TTS (til) zanjirini doskaga chizing.", "Sxemani daftarga chizdiring."],
            ["Jonli Jarvis Simulyatori", "Smartboardda tugmalarni bosing va ovozli javoblarni eshittiring.", "Mushuk sakrashini ko'rsating."],
            ["STT: Nutqni Eshitish", "webkitSpeechRecognition sintaksisini tushuntiring.", "onresult hodisasini ko'rsating."],
            ["NLP: Niyatni Anglash", "includes() kalit so'zlarni qanday ushlashini ko'rsating.", "Daftarga shart yozdiring."],
            ["TTS: Ovoz Chiqarish", "SpeechSynthesisUtterance parametrlarini ko'rsating.", "pitch sozlashini sinab ko'ring."],
            ["Scratch Bog'lanishi", "Ovozli buyruq sprayt koordinatasini o'zgartirishini tushuntiring.", "translateY animatsiyasini ko'rsating."],
            ["Kiber-Quiz", "O'quvchilardan to'g'ri variantni so'rang.", "Doskada variantni bosing va yechimni oching."],
            ["Amaliy Laboratoriya", "O'quvchilarga studio/index.html ni ochishni buyuring.", "25 daqiqalik taymerni yoqing."],
            ["Xatolar Reviziyasi", "Mikrofonni qayta-qayta bosganda nima bo'lishini tushuntiring.", "isListening bayrog'ini ko'rsating."],
            ["Uy Vazifasi Rubrikasi", "10 ballik mezonni (4-4-2) tushuntiring.", "vazifa.html ilovasini ko'rsating."],
            ["Dars Yakuni", "Bugungi 3 ta dvigatelni qaytarib, o'quvchilarni baholang.", "Daftarlarni yopishni ayting."]
        ],
        "ru": [
            ["Введение в урок", "Объявите классу, что сегодня мы создаем собственного голосового помощника Джарвиса.", "Откройте 1-й слайд на проекторе."],
            ["Разбор Д/З", "Покажите ошибку по осям X и Y из прошлого урока Scratch.", "Спросите координаты центра (0, 0)."],
            ["Концепция VUI", "Объясните путь от терминала к голосовому диалогу.", "Спросите, кто пользуется Алисой или Siri."],
            ["3 Двигателя Voice AI", "Нарисуйте цепочку STT (уши) ➔ NLP (мозг) ➔ TTS (голос).", "Попросите перерисовать схему в тетрадь."],
            ["Живой симулятор Джарвиса", "Нажимайте карточки на смартборде и демонстрируйте голос.", "Покажите прыжок кота."],
            ["STT: Распознавание речи", "Покажите код webkitSpeechRecognition.", "Объясните событие onresult."],
            ["NLP: Распознавание намерения", "Покажите работу includes() и toLowerCase().", "Запишите условие на доске."],
            ["TTS: Синтез речи", "Объясните параметры SpeechSynthesisUtterance.", "Покажите настройку pitch."],
            ["Связка со Scratch", "Покажите, как голосовая команда меняет translateY кота.", "Продемонстрируйте анимацию."],
            ["Кибер-Тест", "Спросите класс о правильном варианте ответа.", "Откройте разбор решения на смартборде."],
            ["Практическая арена", "Дайте команду открыть studio/index.html.", "Запустите 25-минутный таймер."],
            ["Анализ ловушек", "Предупредите об ошибке repeated start.", "Покажите защиту через флаг isListening."],
            ["Домашнее задание", "Огласите 10-балльную рубрику (4-4-2).", "Напомните про интерактивный vazifa.html."],
            ["Итоги урока", "Повторите 3 кита Voice AI и выставьте оценки.", "Завершите спаренный урок."]
        ],
        "en": [
            ["Lesson Intro", "Announce to students that we are building our own personal Jarvis AI assistant.", "Present Slide 1 on screen."],
            ["Homework Review", "Analyze the X/Y coordinate pitfall from Lesson 24.", "Quiz students on center origin (0, 0)."],
            ["VUI Concept", "Explain the evolution from CLI terminals to natural voice interfaces.", "Ask about Siri and Alexa usage."],
            ["3 Engine Architecture", "Draw the STT (ears) ➔ NLP (brain) ➔ TTS (voice) pipeline.", "Instruct students to copy diagram."],
            ["Live Jarvis Simulator", "Interact with preset touch cards on smartboard and listen to audio.", "Trigger cat jump physics."],
            ["STT: Speech Recognition", "Explain webkitSpeechRecognition API.", "Show the onresult event handler."],
            ["NLP: Intent Matching", "Demonstrate includes() and toLowerCase() logic.", "Write conditional matching on board."],
            ["TTS: Speech Synthesis", "Break down SpeechSynthesisUtterance attributes.", "Demonstrate robotic pitch adjustments."],
            ["Scratch Integration", "Explain how voice commands mutate translateY CSS coordinates.", "Show synchronized audio-visual jump."],
            ["Cyber Quiz", "Poll the class for the correct answer.", "Reveal and discuss the architectural fix."],
            ["Hands-on Arena", "Direct students to open studio/index.html.", "Activate 25-minute practice countdown."],
            ["Pitfall Autopsy", "Discuss repeated start crashes.", "Demonstrate isListening guard flag."],
            ["Homework Rubric", "Clarify the 10-point rubric breakdown (4-4-2).", "Point out interactive vazifa.html."],
            ["Summary & Wrap-up", "Recap STT, NLP, and TTS and record grades.", "Conclude the double block session."]
        ]
    }
    notes_json = json.dumps(notes_obj, ensure_ascii=False, indent=2)
    tpl = re.sub(r'var NOTES\s*=\s*\{[\s\S]*?\};', f'var NOTES = {notes_json};', tpl)

    # ADD INTERACTIVE JAVASCRIPT HANDLERS FOR SLIDE 5 & ARENA TIMER
    slide_js = """
// ============================================================
// SLIDE 5: LIVE JARVIS SIMULATOR LOGIC
// ============================================================
var slideRecognition = null;
var slideIsListening = false;
var arenaTimerInterval = null;

function triggerJarvisPreset(cmd) {
  var ring = document.getElementById("jarvisPulseRing");
  var cat = document.getElementById("jarvisCatAvatar");
  var status = document.getElementById("jarvisLiveStatus");
  var resp = document.getElementById("jarvisLiveResponse");

  if (ring) {
    ring.style.boxShadow = "0 0 40px var(--accent)";
    ring.style.borderColor = "var(--accent)";
  }

  var msg = "";
  if (cmd === "salom") {
    msg = currentLang === "ru" ? "Привет! Рад тебя слышать. Чем могу помочь?" : (currentLang === "en" ? "Hello! Great to hear you. How can I assist you today?" : "Salom, do'stim! Seni eshitganimdan xursandman!");
    if (cat) cat.textContent = "😸";
  } else if (cmd === "soat") {
    var now = new Date().toLocaleTimeString();
    msg = currentLang === "ru" ? "Сейчас ровно " + now : (currentLang === "en" ? "The current time is " + now : "Hozir soat roppa-rosa " + now);
    if (cat) cat.textContent = "⏰";
  } else if (cmd === "mushuk") {
    msg = currentLang === "ru" ? "Мяу! Прыгаю на 80 пикселей вверх!" : (currentLang === "en" ? "Meow! Jumping 80 pixels up!" : "Miyov! 80 piksel tepaga sakradim!");
    if (cat) {
      cat.textContent = "🚀";
      cat.style.transform = "translateY(-40px)";
      setTimeout(function() {
        cat.style.transform = "translateY(0)";
        cat.textContent = "🐱";
      }, 600);
    }
  } else if (cmd === "mavzu") {
    toggleTheme();
    msg = currentLang === "ru" ? "Тема оформления переключена!" : (currentLang === "en" ? "Display theme toggled!" : "Mavzu muvaffaqiyatli almashtirildi!");
    if (cat) cat.textContent = "🌓";
  } else if (cmd === "musiqa") {
    msg = currentLang === "ru" ? "Играю кибер-бит! Туц-туц-туц!" : (currentLang === "en" ? "Playing cyber beat! Beep boop beep!" : "Kiber-musiqa yangramoqda! Bip-bup-bip!");
    if (cat) cat.textContent = "🎵";
    playSynthChime();
  } else if (cmd === "latifa") {
    msg = currentLang === "ru" ? "Почему программисты любят темную тему? Потому что свет притягивает багов!" : (currentLang === "en" ? "Why do coders love dark mode? Because light attracts bugs!" : "Nega dasturchilar qorong'i mavzuni yaxshi ko'radi? Chunki yorug'likka hasharotlar (buglar) uchib keladi!");
    if (cat) cat.textContent = "😹";
  }

  if (status) status.textContent = currentLang === "ru" ? "Джарвис говорит..." : (currentLang === "en" ? "Jarvis speaking..." : "Jarvis gapirmoqda...");
  if (resp) resp.textContent = "«" + msg + "»";

  speakJarvisText(msg);

  setTimeout(function() {
    if (ring) {
      ring.style.boxShadow = "none";
      ring.style.borderColor = "var(--rule)";
    }
    if (status) status.textContent = currentLang === "ru" ? "Готов к командам" : (currentLang === "en" ? "Ready for commands" : "Buyruq kutmoqda...");
  }, 3500);
}

function speakJarvisText(text) {
  if (!('speechSynthesis' in window)) return;
  window.speechSynthesis.cancel();
  var utter = new SpeechSynthesisUtterance(text);
  utter.rate = 1.05;
  utter.pitch = 1.2;
  utter.lang = currentLang === "ru" ? "ru-RU" : (currentLang === "en" ? "en-US" : "uz-UZ");
  window.speechSynthesis.speak(utter);
}

function playSynthChime() {
  try {
    var ctx = new (window.AudioContext || window.webkitAudioContext)();
    var osc = ctx.createOscillator();
    var gain = ctx.createGain();
    osc.type = "sine";
    osc.frequency.setValueAtTime(523.25, ctx.currentTime); // C5
    osc.frequency.exponentialRampToValueAtTime(659.25, ctx.currentTime + 0.15); // E5
    osc.frequency.exponentialRampToValueAtTime(783.99, ctx.currentTime + 0.3); // G5
    gain.gain.setValueAtTime(0.2, ctx.currentTime);
    gain.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + 0.6);
    osc.connect(gain);
    gain.connect(ctx.destination);
    osc.start();
    osc.stop(ctx.currentTime + 0.6);
  } catch(e) {}
}

function toggleSlideMic() {
  var btn = document.getElementById("slideMicBtn");
  var status = document.getElementById("jarvisLiveStatus");
  var resp = document.getElementById("jarvisLiveResponse");

  if (!('webkitSpeechRecognition' in window) && !('SpeechRecognition' in window)) {
    alert("Brauzeringizda Web Speech API qo'llab-quvvatlanmaydi. Iltimos Google Chrome ishlating.");
    return;
  }

  if (slideIsListening) {
    if (slideRecognition) slideRecognition.stop();
    slideIsListening = false;
    if (btn) btn.textContent = currentLang === "ru" ? "🎤 Включить Микрофон" : (currentLang === "en" ? "🎤 Toggle Mic" : "🎤 Mikrofonni Yoqish");
    if (status) status.textContent = currentLang === "ru" ? "Микрофон выключен" : (currentLang === "en" ? "Mic stopped" : "Mikrofon o'chirildi");
    return;
  }

  var SpeechRec = window.SpeechRecognition || window.webkitSpeechRecognition;
  slideRecognition = new SpeechRec();
  slideRecognition.lang = currentLang === "ru" ? "ru-RU" : (currentLang === "en" ? "en-US" : "uz-UZ");
  slideRecognition.continuous = false;

  slideRecognition.onstart = function() {
    slideIsListening = true;
    if (btn) btn.textContent = currentLang === "ru" ? "⏹️ Остановить Запись" : (currentLang === "en" ? "⏹️ Stop Listening" : "⏹️ Tinglashni To'xtatish");
    if (status) status.textContent = currentLang === "ru" ? "Слушаю вас... Говорите!" : (currentLang === "en" ? "Listening... Speak now!" : "Sizni eshitmoqdaman... Gapiring!");
    var ring = document.getElementById("jarvisPulseRing");
    if (ring) ring.style.boxShadow = "0 0 30px var(--accent)";
  };

  slideRecognition.onresult = function(e) {
    var transcript = e.results[0][0].transcript;
    if (resp) resp.textContent = "«" + transcript + "»";
    processSlideVoice(transcript.toLowerCase());
  };

  slideRecognition.onerror = function() {
    slideIsListening = false;
    if (btn) btn.textContent = "🎤 Mikrofonni Yoqish";
    if (status) status.textContent = "Xatolik yuz berdi";
  };

  slideRecognition.onend = function() {
    slideIsListening = false;
    if (btn) btn.textContent = "🎤 Mikrofonni Yoqish";
    var ring = document.getElementById("jarvisPulseRing");
    if (ring) ring.style.boxShadow = "none";
  };

  slideRecognition.start();
}

function processSlideVoice(text) {
  if (text.includes("salom") || text.includes("привет") || text.includes("hello")) {
    triggerJarvisPreset("salom");
  } else if (text.includes("soat") || text.includes("время") || text.includes("time")) {
    triggerJarvisPreset("soat");
  } else if (text.includes("mushuk") || text.includes("кот") || text.includes("cat") || text.includes("sakra") || text.includes("прыг")) {
    triggerJarvisPreset("mushuk");
  } else if (text.includes("mavzu") || text.includes("тем") || text.includes("theme")) {
    triggerJarvisPreset("mavzu");
  } else if (text.includes("musiqa") || text.includes("музык") || text.includes("music")) {
    triggerJarvisPreset("musiqa");
  } else if (text.includes("latifa") || text.includes("шутк") || text.includes("joke")) {
    triggerJarvisPreset("latifa");
  } else {
    var unknownMsg = currentLang === "ru" ? "Я услышал: «" + text + "», но еще не знаю этой команды." : (currentLang === "en" ? "I heard: '" + text + "', but I don't know that command yet." : "Eshitdim: '" + text + "', ammo bu buyruqni hali bilmayman.");
    speakJarvisText(unknownMsg);
    var resp = document.getElementById("jarvisLiveResponse");
    if (resp) resp.textContent = "«" + unknownMsg + "»";
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
      playSynthChime();
    }
  }, 1000);
}

function resetArenaTimer() {
  clearInterval(arenaTimerInterval);
  var display = document.getElementById("arenaTimer");
  if (display) display.textContent = "25:00";
}
"""

    # Insert slide_js right before closing </script>
    tpl = tpl.replace("</script>", slide_js + "\n</script>")

    out_file = os.path.join(LESSON_DIR, "prezentatsiya.html")
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(tpl)
    print(f"  ✓ Written: {os.path.relpath(out_file, REPO_ROOT)} ({len(tpl)} bytes)")

# ---------------------------------------------------------------------------
# 2. VARAQA.HTML
# ---------------------------------------------------------------------------
def build_varaqa():
    template_path = os.path.join(REPO_ROOT, "assets", "TEMPLATE_VARAQA.html")
    with open(template_path, "r", encoding="utf-8") as f:
        tpl = f.read()

    tpl = tpl.replace("{{LESSON_NUM}}", "25")
    tpl = tpl.replace("{{TITLE_UZ}}", "Target Jarvis — AI Ovozli Yordamchi")
    tpl = tpl.replace("{{TITLE_RU}}", "Target Jarvis — Голосовой AI-Помощник")
    tpl = tpl.replace("{{TITLE_EN}}", "Target Jarvis — AI Voice Assistant")
    tpl = tpl.replace("{{COHORT_LABEL_UZ}}", "5–6-sinf")
    tpl = tpl.replace("{{COHORT_LABEL_RU}}", "5–6 класс")
    tpl = tpl.replace("{{COHORT_LABEL_EN}}", "Grades 5–6")

    meta_uz = "2-Chorak · 10-hafta · 25-dars · Junior Creators & Kiber-Gigiyena Track"
    meta_ru = "2-я четверть · 10-я неделя · 25-й урок · Junior Creators & Кибер-Гигиена"
    meta_en = "Quarter 2 · Week 10 · Lesson 25 · Junior Creators & Cyber Hygiene Track"
    tpl = tpl.replace("{{META_UZ}}", meta_uz)
    tpl = tpl.replace("{{META_RU}}", meta_ru)
    tpl = tpl.replace("{{META_EN}}", meta_en)

    mission_uz = "Shaxsiy Target Jarvis ovozli yordamchisini yaratish, mikrofondan ovozli buyruqlarni qabul qilish (STT), niyatni aniqlash (NLP) va dinamikdan ovoz chiqarib javob qaytarish (TTS)."
    mission_ru = "Создание персонального голосового помощника Target Jarvis, распознавание речи с микрофона (STT), анализ намерений (NLP) и синтез голосового ответа (TTS)."
    mission_en = "Building a personal Target Jarvis voice assistant, transcribing microphone speech (STT), matching user intent (NLP), and vocalizing spoken replies (TTS)."
    tpl = tpl.replace("{{MISSION_UZ}}", mission_uz)
    tpl = tpl.replace("{{MISSION_RU}}", mission_ru)
    tpl = tpl.replace("{{MISSION_EN}}", mission_en)

    # SEC 1: 3 Engines
    tpl = tpl.replace("{{SEC1_TITLE_UZ}}", "1-Qism: Ovozli Yordamchining 3 ta Dvigateli (STT ➔ NLP ➔ TTS)")
    tpl = tpl.replace("{{SEC1_TITLE_RU}}", "Часть 1: 3 Двигателя Голосового Помощника (STT ➔ NLP ➔ TTS)")
    tpl = tpl.replace("{{SEC1_TITLE_EN}}", "Part 1: 3 Engines of Voice AI (STT ➔ NLP ➔ TTS)")
    sec1 = """    <div class="box-grid">
      <div class="box">
        <h4 data-ru="1. Quloq (Speech-to-Text / STT)" data-en="1. Ear (Speech-to-Text / STT)">1. Quloq (Speech-to-Text / STT)</h4>
        <p data-ru="Какую функцию выполняет микрофон и модуль STT? Запишите название JS API:" data-en="What does the microphone and STT engine do? Write the JS API name:">Mikrofon va STT dvigateli qanday vazifani bajaradi? JavaScriptdagi API nomini yozing:</p>
        <div class="write-line"></div>
        <div class="write-line"></div>
      </div>
      <div class="box">
        <h4 data-ru="2. Miya (Intent Matching / NLP)" data-en="2. Brain (Intent Matching / NLP)">2. Miya (Intent Matching / NLP)</h4>
        <p data-ru="Как программа понимает смысл фразы ученика? Какой метод проверяет ключевые слова?" data-en="How does the program extract intent? Which method checks keywords?">Dastur o'quvchining gapini qanday tushunadi? Qaysi usul kalit so'zlarni qidiradi?</p>
        <div class="write-line"></div>
        <div class="write-line"></div>
      </div>
    </div>
    <div class="box" style="margin-top:6px;">
      <h4 data-ru="3. Til (Text-to-Speech / TTS)" data-en="3. Voice (Text-to-Speech / TTS)">3. Til (Text-to-Speech / TTS)</h4>
      <p data-ru="Какой модуль отвечает за озвучивание ответа из динамика? Запишите команду вызова:" data-en="Which module vocalizes the response through the speaker? Write the invocation command:">Dinamikdan insoniy ovoz bilan javob qaytarish uchun qaysi obyekt ishlatiladi? Chaqirish buyrug'ini yozing:</p>
      <div class="write-line"></div>
    </div>"""
    tpl = tpl.replace("{{SEC1_CONTENT}}", sec1)

    # SEC 2: Code Analysis
    tpl = tpl.replace("{{SEC2_TITLE_UZ}}", "2-Qism: Kod Tahlili va Niyatni Aniqlash (Intent Matching)")
    tpl = tpl.replace("{{SEC2_TITLE_RU}}", "Часть 2: Анализ Кода и Определение Намерений (Intent Matching)")
    tpl = tpl.replace("{{SEC2_TITLE_EN}}", "Part 2: Code Analysis & Intent Matching")
    sec2 = """    <div class="code-snippet">// ⚠️ Kodni to'ldiring: agar gapda "soat" so'zi bo'lsa, vaqtni aytsin!
let text = transcript.toLowerCase();

if (text.includes("salom")) {
  gapir("Salom, do'stim!");
} else if (text.___________________("soat")) {
  gapir("Hozir soat " + new Date().toLocaleTimeString());
} else {
  gapir("Kechirasiz, bu buyruqni bilmayman.");
}</div>
    <p style="margin-top:4px;" data-ru="Пропущенный метод в условии проверки времени:" data-en="Fill in the missing method in the condition:">Bo'sh qoldirilgan joyga to'g'ri metod nomini yozing:</p>
    <div class="write-line"></div>"""
    tpl = tpl.replace("{{SEC2_CONTENT}}", sec2)

    # SEC 3: Practical Lab
    tpl = tpl.replace("{{SEC3_TITLE_UZ}}", "3-Qism: Katta Amaliy Laboratoriya (5 ta Sinov Jadvali)")
    tpl = tpl.replace("{{SEC3_TITLE_RU}}", "Часть 3: Большая Практическая Лаборатория (Таблица 5 Тестов)")
    tpl = tpl.replace("{{SEC3_TITLE_EN}}", "Part 3: Hands-on Lab (5 Tests Audit Table)")
    sec3 = """    <p data-ru="Запустите studio/index.html и проверьте 5 голосовых команд. Запишите ответ Jarvis:" data-en="Launch studio/index.html and test 5 voice queries. Record Jarvis's reply:"><b>studio/index.html</b> ilovasini oching, 5 ta buyruqni sinab, Jarvis qaytargan javobni yozing:</p>
    <div class="box" style="margin-top:6px;">
      <table style="width:100%; border-collapse:collapse; font-size:8.5pt;">
        <thead>
          <tr style="border-bottom:1px solid var(--rule); text-align:left;">
            <th style="padding:4px 6px;">#</th>
            <th style="padding:4px 6px;" data-ru="Произнесенная команда" data-en="Spoken Command">Aytilgan Ovozli Buyruq</th>
            <th style="padding:4px 6px;" data-ru="Действие Jarvis (Ответ/Анимация)" data-en="Jarvis Action (Reply/Anim)">Jarvis Qaytargan Javob yoki Harakat</th>
            <th style="padding:4px 6px;" data-ru="Статус" data-en="Status">Holat</th>
          </tr>
        </thead>
        <tbody>
          <tr style="border-bottom:1px dashed var(--hair);">
            <td style="padding:4px 6px;">1</td>
            <td style="padding:4px 6px;" data-ru="«Привет, Джарвис»" data-en="«Hello Jarvis»">«Salom Jarvis»</td>
            <td style="padding:4px 6px;"><div class="write-line" style="margin:2px 0;"></div></td>
            <td style="padding:4px 6px;" data-ru="[ &nbsp; ] Готово" data-en="[ &nbsp; ] Done">[ &nbsp; ] OK</td>
          </tr>
          <tr style="border-bottom:1px dashed var(--hair);">
            <td style="padding:4px 6px;">2</td>
            <td style="padding:4px 6px;" data-ru="«Сколько времени?»" data-en="«What time is it?»">«Soat necha?»</td>
            <td style="padding:4px 6px;"><div class="write-line" style="margin:2px 0;"></div></td>
            <td style="padding:4px 6px;" data-ru="[ &nbsp; ] Готово" data-en="[ &nbsp; ] Done">[ &nbsp; ] OK</td>
          </tr>
          <tr style="border-bottom:1px dashed var(--hair);">
            <td style="padding:4px 6px;">3</td>
            <td style="padding:4px 6px;" data-ru="«Кот, прыгай»" data-en="«Cat, jump»">«Mushuk sakrasin»</td>
            <td style="padding:4px 6px;"><div class="write-line" style="margin:2px 0;"></div></td>
            <td style="padding:4px 6px;" data-ru="[ &nbsp; ] Готово" data-en="[ &nbsp; ] Done">[ &nbsp; ] OK</td>
          </tr>
          <tr style="border-bottom:1px dashed var(--hair);">
            <td style="padding:4px 6px;">4</td>
            <td style="padding:4px 6px;" data-ru="«Смени тему»" data-en="«Toggle theme»">«Mavzuni almashtir»</td>
            <td style="padding:4px 6px;"><div class="write-line" style="margin:2px 0;"></div></td>
            <td style="padding:4px 6px;" data-ru="[ &nbsp; ] Готово" data-en="[ &nbsp; ] Done">[ &nbsp; ] OK</td>
          </tr>
          <tr>
            <td style="padding:4px 6px;">5</td>
            <td style="padding:4px 6px;"><i data-ru="(Ваша новая команда)" data-en="(Your custom command)">(Sizning yangi shaxsiy buyrug'ingiz)</i></td>
            <td style="padding:4px 6px;"><div class="write-line" style="margin:2px 0;"></div></td>
            <td style="padding:4px 6px;" data-ru="[ &nbsp; ] Готово" data-en="[ &nbsp; ] Done">[ &nbsp; ] OK</td>
          </tr>
        </tbody>
      </table>
    </div>"""
    tpl = tpl.replace("{{SEC3_CONTENT}}", sec3)

    # SEC 4: Homework 10-point Rubric
    sec4 = """    <div class="box-grid" style="margin-top:6px;">
      <div class="box">
        <h4 data-ru="1-Уровень: База (4 балла)" data-en="Tier 1: Base (4 pts)">1-Daraja: Baza (4 ball)</h4>
        <p data-ru="Запустить студию, проверить 3 базовые команды («Салом», «Соат», «Мавзу») и убедиться в голосовом ответе." data-en="Launch studio, verify 3 core commands ('Hello', 'Time', 'Theme') and confirm vocal feedback.">Studiyani ishga tushirish, 3 ta asosiy buyruqni ("Salom", "Soat", "Mavzu") xatolarsiz sinash va natijani qayd etish.</p>
        <div class="write-line"></div>
      </div>
      <div class="box">
        <h4 data-ru="2-Уровень: Проект (4 балла)" data-en="Tier 2: Project (4 pts)">2-Daraja: Amaliyot (4 ball)</h4>
        <p data-ru="Придумать и добавить 2 свои уникальные голосовые команды в блок Custom Intents." data-en="Invent and register 2 unique voice triggers into the Custom Intents studio module.">Studiyadagi Custom Intents bo'limiga 2 ta yangi shaxsiy buyruq o'ylab topib kiritish va sinash.</p>
        <div class="write-line"></div>
      </div>
    </div>
    <div class="box" style="margin-top:6px;">
      <h4 data-ru="3-Уровень: Кибер-Вызов (2 балла)" data-en="Tier 3: Cyber Challenge (2 pts)">3-Daraja: Kiber-Chaqiruv (2 ball)</h4>
      <p data-ru="Настроить тональность голоса (pitch: 0.6 для робота или 1.8 для мультяшного кота) и записать результат." data-en="Configure speech synthesis pitch (0.6 for transformer or 1.8 for cartoon cat) and document output.">Jarvis ovozi balandligini (`pitch`) sozlab, unga robot yoki multfilm ovozini berish va natijani yozish.</p>
      <div class="write-line"></div>
    </div>"""
    tpl = tpl.replace("{{SEC4_CONTENT}}", sec4)

    out_file = os.path.join(LESSON_DIR, "varaqa.html")
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(tpl)
    print(f"  ✓ Written: {os.path.relpath(out_file, REPO_ROOT)} ({len(tpl)} bytes)")

# ---------------------------------------------------------------------------
# 3. VAZIFA.HTML
# ---------------------------------------------------------------------------
def build_vazifa():
    template_path = os.path.join(REPO_ROOT, "assets", "TEMPLATE_VAZIFA.html")
    with open(template_path, "r", encoding="utf-8") as f:
        tpl = f.read()

    tpl = tpl.replace("{{LESSON_NUM}}", "25")
    tpl = tpl.replace("{{TITLE_UZ}}", "Target Jarvis: AI Ovozli Yordamchi")
    tpl = tpl.replace("{{TITLE_RU}}", "Target Jarvis: Голосовой AI-Помощник")
    tpl = tpl.replace("{{TITLE_EN}}", "Target Jarvis: AI Voice Assistant")
    tpl = tpl.replace("{{COHORT_LABEL_UZ}}", "5–6-sinf")
    tpl = tpl.replace("{{COHORT_LABEL_RU}}", "5–6 класс")
    tpl = tpl.replace("{{COHORT_LABEL_EN}}", "Grades 5–6")

    meta_uz = "2-Chorak · 10-hafta · 25-dars · Mustaqil Kiber-Laboratoriya"
    meta_ru = "2-я четверть · 10-я неделя · 25-й урок · Самостоятельная кибер-лаборатория"
    meta_en = "Quarter 2 · Week 10 · Lesson 25 · Independent Cyber Lab"
    tpl = tpl.replace("{{META_UZ}}", meta_uz)
    tpl = tpl.replace("{{META_RU}}", meta_ru)
    tpl = tpl.replace("{{META_EN}}", meta_en)

    desc_uz = "Ushbu interaktiv ilovada 3 ta topshiriqni bajaring. Javoblaringiz brauzer xotirasida (LocalStorage) avtomatik saqlanib boradi."
    desc_ru = "Выполните 3 задания в этом интерактивном приложении. Ответы автоматически сохраняются в LocalStorage."
    desc_en = "Complete the 3 tasks in this interactive app. Your progress auto-saves to LocalStorage."
    tpl = tpl.replace("{{DESC_UZ}}", desc_uz)
    tpl = tpl.replace("{{DESC_RU}}", desc_ru)
    tpl = tpl.replace("{{DESC_EN}}", desc_en)

    # Task 1
    t1_title_uz = "1-Topshiriq: Ovozli Yordamchining 3 ta Dvigatelini Tushuntiring (Baza — 4 ball)"
    t1_title_ru = "Задание 1: Объясните 3 Двигателя Голосового Помощника (База — 4 балла)"
    t1_title_en = "Task 1: Explain the 3 Engines of Voice AI (Base — 4 pts)"
    tpl = tpl.replace("{{T1_TITLE_UZ}}", t1_title_uz)
    tpl = tpl.replace("{{T1_TITLE_RU}}", t1_title_ru)
    tpl = tpl.replace("{{T1_TITLE_EN}}", t1_title_en)

    t1_desc_uz = "Har bir dvigatelning (STT, NLP, TTS) asosiy vazifasini qisqa jumlada yozib bering:"
    t1_desc_ru = "Опишите главную задачу каждого компонента (STT, NLP, TTS) простыми словами:"
    t1_desc_en = "Describe the primary role of each engine (STT, NLP, TTS) in concise words:"
    tpl = tpl.replace("{{T1_DESC_UZ}}", t1_desc_uz)
    tpl = tpl.replace("{{T1_DESC_RU}}", t1_desc_ru)
    tpl = tpl.replace("{{T1_DESC_EN}}", t1_desc_en)

    # Task 2
    t2_title_uz = "2-Topshiriq: 2 ta Yangi Shaxsiy Buyruq Yarating (Amaliyot — 4 ball)"
    t2_title_ru = "Задание 2: Создайте 2 Новые Голосовые Команды (Проект — 4 балла)"
    t2_title_en = "Task 2: Register 2 Custom Voice Intents (Project — 4 pts)"
    tpl = tpl.replace("{{T2_TITLE_UZ}}", t2_title_uz)
    tpl = tpl.replace("{{T2_TITLE_RU}}", t2_title_ru)
    tpl = tpl.replace("{{T2_TITLE_EN}}", t2_title_en)

    t2_desc_uz = "Masalan: 'maktab' so'zi aytilganda 'Target International School — eng yaxshi maktab!', 'ob-havo' aytilganda quyoshli deb javob bersin:"
    t2_desc_ru = "Например: при слове «школа» ответ «Target International School — лучшая школа!», при слове «погода» — рассказ о погоде:"
    t2_desc_en = "For example: saying 'school' triggers 'Target International School is amazing!', saying 'weather' gives a forecast:"
    tpl = tpl.replace("{{T2_DESC_UZ}}", t2_desc_uz)
    tpl = tpl.replace("{{T2_DESC_RU}}", t2_desc_ru)
    tpl = tpl.replace("{{T2_DESC_EN}}", t2_desc_en)

    # Task 3
    t3_title_uz = "3-Topshiriq: Kiber-Chaqiruv — Robot Ovozini Sozlash (2 ball)"
    t3_title_ru = "Задание 3: Кибер-Вызов — Настройка Голоса Робота (2 балла)"
    t3_title_en = "Task 3: Cyber Challenge — Robot Tone Tuning (2 pts)"
    tpl = tpl.replace("{{T3_TITLE_UZ}}", t3_title_uz)
    tpl = tpl.replace("{{T3_TITLE_RU}}", t3_title_ru)
    tpl = tpl.replace("{{T3_TITLE_EN}}", t3_title_en)

    t3_desc_uz = "SpeechSynthesisUtterance obyektida ovoz balandligini (pitch) va tezligini (rate) qanday kod orqali o'zgartirasiz? Kod namunasini yozing:"
    t3_desc_ru = "Как изменить pitch (высоту тона) и rate (скорость) в SpeechSynthesisUtterance? Напишите код:"
    t3_desc_en = "How do you configure pitch and rate on a SpeechSynthesisUtterance instance? Provide code snippet:"
    tpl = tpl.replace("{{T3_DESC_UZ}}", t3_desc_uz)
    tpl = tpl.replace("{{T3_DESC_RU}}", t3_desc_ru)
    tpl = tpl.replace("{{T3_DESC_EN}}", t3_desc_en)

    out_file = os.path.join(LESSON_DIR, "vazifa.html")
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(tpl)
    print(f"  ✓ Written: {os.path.relpath(out_file, REPO_ROOT)} ({len(tpl)} bytes)")

# ---------------------------------------------------------------------------
# 4. TEACHER_READING.MD
# ---------------------------------------------------------------------------
def build_teacher_reading():
    content = """# 25-Dars: O'qituvchi Uchun Metodik Qo'llanma (Teacher Briefing)

**Kohorta:** 5–6-Sinf · Junior Creators & Kiber-Gigiyena Track  
**Mavzu:** Target Jarvis — AI Ovozli Yordamchi (Voice AI, Web Speech API va Scratch Boshqaruvi)  
**Ajratilgan vaqt:** 80 daqiqa (Juftlik blok / Double Block)  
**Amaliy natija:** Brauzerda ovozli buyruqlarni mikrofondan taniydigan (STT), niyatni anglovchi (NLP), o'zi insondek ovoz chiqarib javob qaytaruvchi (TTS) va Scratch mushugini ovoz bilan sakratuvchi shaxsiy AI yordamchi.

---

## 1. 5 Daqiqalik Darsoldi Konspekti (O'qituvchiga Eslatma)

Ushbu dars 5–6-sinf o'quvchilarida kompyuter bilan muloqot qilishning eng zamonaviy bosqichi — **Voice User Interface (VUI)** dunyosini ochib beradi.
Ko'pchilik bolalar Siri, Alisa yoki Alexani o'ta murakkab va faqat gigant korporatsiyalar qila oladigan "sehr" deb o'ylashadi.
Bugun ular o'z ko'zlari bilan ko'rishadi: **JavaScript va Web Speech API yordamida o'zlarining shaxsiy Target Jarvisini yaratish mumkin!**

### Darsning 3 ta asosiy ustuni:
1. **Speech-to-Text (`webkitSpeechRecognition`):** Mikrofondan kelgan tovush to'lqinlarini ushlab, `onresult` hodisasi orqali matn (`transcript`) ko'rinishida chiqarish.
2. **Intent Matching (Niyatni aniqlash):** `.toLowerCase()` va `.includes()` orqali gapirilgan gap ma'nosini tahlil qilib, qaysi buyruqni bajarishni belgilash.
3. **Text-to-Speech (`speechSynthesis`):** `SpeechSynthesisUtterance` orqali javob matnini insoniy nutqqa aylantirib, dinamikdan balandlik (`pitch`) va tezlik (`rate`) bilan eshittirish.

---

## 2. 80 Daqiqalik Dars Vaqt Xaritasi (Double Block Roadmap)

### 1-Bosqich: Nazariya, Tushuncha va Jonli Demo (40 daqiqa)
| Vaqt | Bosqich | O'qituvchi amali | O'quvchi harakati |
|---|---|---|---|
| **00–04 daq** | Titul & Motivatsiya | Proyektorda 1-slaydni ochish, Jarvis nimaligini tushuntirish | Ekranga qarab hayratlanish, maqsadni tushunish |
| **04–10 daq** | O'tgan Dars Tahlili (HW Review) | 24-darsdagi Scratch X va Y koordinatalari xatosini ko'rsatish | X gorizontal, Y vertikal ekanligini qaytarish |
| **10–16 daq** | VUI Evolyutsiyasi | CLI (1980) ➔ GUI (1990) ➔ VUI (Bugun) bosqichlarini tushuntirish | Daftarga 3 ta bosqichni yozish |
| **16–22 daq** | 3 Dvigatel Arxitekturasi | Quloq (STT) ➔ Miya (NLP) ➔ Til (TTS) zanjirini doskaga chizish | Sxemani daftarga tushirish |
| **22–30 daq** | Jonli Jarvis Simulyatori | 5-slaydda Smartboardda tugmalarni bosib, mushukni sakratish va gapirtirish | Smartboardga chiqib buyruqlarni bosish |
| **30–40 daq** | Dvigatellar Sintaksisi & Quiz | 6–8 slaydlar: `rec.start()`, `includes()`, `speechSynthesis` va 10-slayddagi kiber-test | Kiber-quiz javobini belgilash |

### 2-Bosqich: Katta Amaliy Laboratoriya (40 daqiqa)
| Vaqt | Bosqich | O'qituvchi amali | O'quvchi harakati |
|---|---|---|---|
| **40–65 daq (25 min)** | Katta Amaliy Arena | Har bir o'quvchi noutbukida `studio/index.html` ni ochish, 25 daqiqalik taymerni yoqish | 5 ta buyruqni sinash, yangi shaxsiy buyruq qo'shish |
| **65–72 daq (7 min)** | Juftlikda Sinov (Peer Review) | Partadoshlar bilan joy almashib, bir-birining Jarvisini mikrofonda sinash | Bir-birining yangi buyruqlarini sinovdan o'tkazish |
| **72–76 daq (4 min)** | Xatolar Tahlili (Bug Hunter) | `recognition already started` xatosi va mikrofon ruxsatini tushuntirish | Daftarga `isListening` himoyasini qayd etish |
| **76–80 daq (4 min)** | Baholash va Uy Vazifasi | 10 ballik mezon bo'yicha baholash, `vazifa.html` topshirig'ini tushuntirish | Ish varaqalarini topshirish |

---

## 3. O'quvchilar Eng Ko'p Yo'l Qo'yadigan 3 Ta Xato va Ularning Yechimi

### 1-Xato: Brauzerda mikrofon bloklanib qolishi (Permission Denied)
* **Muammo:** O'quvchi sahifa birinchi marta ochilganda tasodifan "Bloklash" (Block) tugmasini bosib yuboradi.
* **Yechim:** URL satrining chap tomonidagi qulf belgisini bosing, "Mikrofon" ruxsatini "Ruxsat berilgan" (Allow) qilib, `F5` bilan yangilang.

### 2-Xato: `recognition has already started` xatosi
* **Muammo:** O'quvchi mikrofon tugmasini ketma-ket bir necha marta tez-tez bosganda dastur qotib qoladi.
* **Yechim:** Tugma bosilganda doimo `isListening` bayrog'i tekshirilishi kerak: agar faol bo'lsa, `recognition.stop()`, aks holda `recognition.start()` chaqiriladi.

### 3-Xato: Shovqinli sinfda so'zlarning xato tanilishi
* **Muammo:** Sinfda 15 ta o'quvchi baravar gapirganda mikrofon atrofdagi tovushlarni ilib olishi mumkin.
* **Yechim:** Studiyada tayyor sensorli tugmalar (Touch Presets) va klaviatura maydoni mavjud — o'quvchilar shovqin bo'lganda ham barcha funksiyalarni 100% aniqlik bilan sinay oladilar.

---

## 4. Baholash Mezoni (10 Ballik Standart)

- **1–4 Ball (Baza):** Studiya ochildi, mikrofon ishga tushdi va aytilgan so'zlar ekranda matn ko'rinishida hosil bo'ldi.
- **5–7 Ball (Standart):** Jarvis ovoz chiqarib javob qaytardi, salomlashish, soat, mushuk sakrashi va mavzu almashtirish buyruqlari muvaffaqiyatli sinovdan o'tdi.
- **8–10 Ball (Junior Creator):** O'quvchi o'zining yangi 2 ta shaxsiy buyrug'ini (Custom Intents) kiritdi, Jarvis ovozi balandligini (`pitch`) robotga moslab sozlay oldi va varaqadagi barcha 5 ta sinovni to'ldirib topshirdi.
"""
    out_file = os.path.join(LESSON_DIR, "TEACHER_READING.md")
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"  ✓ Written: {os.path.relpath(out_file, REPO_ROOT)} ({len(content)} bytes)")

# ---------------------------------------------------------------------------
# 5. STUDIO/INDEX.HTML (Dedicated Interactive Voice Studio for 5-6 Sinf)
# ---------------------------------------------------------------------------
def build_studio():
    # Copy and adapt 7-8 sinf studio with 5-6 grade Scratch Cat visuals & touch presets
    source_studio = os.path.join(REPO_ROOT, "classes", "7-8-sinf", "5-hafta", "25-dars-ai-ovozli-yordamchi-web-speech", "studio", "index.html")
    with open(source_studio, "r", encoding="utf-8") as f:
        studio_html = f.read()

    # Update title and cohort badges
    studio_html = studio_html.replace("7–8-Sinf · AI & Game Development Track", "5–6-Sinf · Junior Creators & Kiber-Gigiyena Track")
    studio_html = studio_html.replace("7-8 · ВАЙБКОДИНГ", "5-6 · ВАЙБКОДИНГ")
    studio_html = studio_html.replace("7-8 · VIBECODING", "5-6 · VIBECODING")

    # Add Scratch Cat jumping action to the studio script if missing
    cat_script = """
  // Scratch Cat Voice Action for 5-6 graders
  if (text.includes("mushuk") || text.includes("кот") || text.includes("cat") || text.includes("sakra") || text.includes("прыг")) {
    var catEl = document.getElementById("scratchCatStudioAvatar");
    if (catEl) {
      catEl.style.transform = "translateY(-60px) scale(1.15)";
      setTimeout(function() {
        catEl.style.transform = "translateY(0) scale(1.0)";
      }, 500);
    }
    var catReply = currentLang === "ru" ? "Мяу! Прыжок выполнен успешно!" : (currentLang === "en" ? "Meow! Jump executed flawlessly!" : "Miyov! Mushuk 60 piksel balandlikka sakradi!");
    speak(catReply);
    addLog(text, catReply);
    return;
  }
"""
    if "mushuk" not in studio_html:
        studio_html = studio_html.replace('function processIntent(rawText) {', 'function processIntent(rawText) {\n' + cat_script)

    out_file = os.path.join(STUDIO_DIR, "index.html")
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(studio_html)
    print(f"  ✓ Written: {os.path.relpath(out_file, REPO_ROOT)} ({len(studio_html)} bytes)")

def main():
    print("🚀 Building 25-dars for 5-6-sinf (Target Jarvis: AI Ovozli Yordamchi)...")
    build_prezentatsiya()
    build_varaqa()
    build_vazifa()
    build_teacher_reading()
    build_studio()
    print("✨ Compilation complete! Validating with verify_i18n.py...")
    res = subprocess.run([sys.executable, os.path.join(REPO_ROOT, "scripts", "verify_i18n.py"), LESSON_DIR], capture_output=True, text=True)
    print(res.stdout)
    if res.returncode != 0:
        print("STDERR:", res.stderr)
        sys.exit(res.returncode)
    else:
        print("🎉 100% SUCCESS: All files created and verified without errors!")

if __name__ == "__main__":
    main()
