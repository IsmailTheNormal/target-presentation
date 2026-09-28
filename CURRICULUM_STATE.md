# Vibecoding Curriculum - State & Context

> **AGENT NOTE:** Read this file whenever you lose context on what has been built, the rationale behind the age groups, or the technical bugs that have been fixed.

## 📅 Schedule & Cohort Mapping (Week 1)

The curriculum is split into 4 distinct age groups. The teaching approach drastically changes depending on the grade.

### 🎓 9-11-sinf (High Technical Depth, Systems Thinking)
- **Approach:** No childish games. Deep dive into mechanics, vocabulary, and top-down architecture. Unified for 9th, 10th, and 11th grades.
- **01-dars-ai-nima:** Serious introduction to AI and tools.
- **02-dars-vibecoding-asoslari:** Web Architecture. Teaches UI/UX, Frontend, Backend, and specific vocabulary (Navbar, Hero, Padding, Margin, Grid, Flexbox). Uses **inline SVG diagrams** for visual learning instead of just bullet points.
- **03-dars-it-dunyosi-kod-va-cloud:** The anatomy of web technologies (HTML, CSS, JS) and cloud infrastructure (Domain, IP, Hosting, Server, DB, Cloud). Uses a flowchart to show how they all connect.
- **04-dars-frilans-buyurtma-ui:** Freelance Order Simulation: PRD specifications, CSS Grid centering, Flexbox rows, Contrast and Hierarchy laws.
- **05-dars-frilans-mantiq-js:** JavaScript Logic: Events, Functions, State, and Client Revision handling (Dark Mode toggle without breaking CSS).
- **06-dars-deploy-va-taqdimot:** Going Live: Cloud deployment via Vercel/Netlify, SSL certificates, Mobile responsive testing, QR code verification, and Demo Day pitch.
- **07-dars-api-va-json-asoslari:** API & JSON Fundamentals: Client-Server communication, Restaurant metaphor, JSON structure, GET/POST methods, HTTP status codes, and CORS.
- **08-dars-jonli-valyuta-konverteri:** Fintech Project: Real-time Currency Converter with live central bank/crypto APIs, async/await, loading UX, and error resilience.
- **09-dars-localstorage-va-state:** Persistent Storage: LocalStorage vs Cookies/Session, stringify/parse, state persistence, DevTools inspection, and security restrictions.
- **10-dars-auth-va-himoya:** Security & Secrets: Authentication vs Authorization, password hashing, API key leakage risks, .env configuration, and login modals.
- **11-dars-vscode-va-mahalliy-muhit:** Local Dev Environment: Installing VS Code, essential extensions (Live Server, Prettier), integrated terminal, and workspace setup.
- **12-dars-agentic-ai-va-avtonom-kod:** Agentic AI: Autonomous coding agents (Cline/Cursor/Copilot), tools (read/write/terminal), ReAct reasoning loop, and task delegation.

### 🎮 7-8-sinf (Playful but Competitive)
- **Approach:** Gamified learning, creative engineering, and tournament competitions.
- **01-dars-ai-nima:** "Capybara" version. Fun, joke-filled introduction to AI mechanics.
- **02-dars-ai-duel:** Prompt Dueling: Competitive arena teaching prompt precision and constraints.
- **03-dars-ai-rassom:** Visual Prompting: Diffusion models, 4 pillars formula, camera angles, lighting magic, and negative prompts.
- **04-dars-ai-kvest-oyini:** Game Dev: Interactive choose-your-own-adventure text quest, branching story trees, HP system, and game loop debugging.
- **05-dars-veb-sahifa-birinchi-kod:** Gamer Profile: Building a dark cyberpunk portfolio website with neon glow, image galleries, and interactive play buttons.
- **06-dars-haftalik-turnir:** Grand Tournament: 90-second pitches on the projector, peer voting ballots, QR code mobile testing, and week championship awards.

### 🧸 5-6-sinf (Simple, Playful, Conceptual)
- **Approach:** Highly conceptual, easy to grasp metaphors, cartoon animations, and creative storytelling.
- **01-dars-ai-nima:** "Capybara" version. Friendly, accessible introduction to AI concepts.
- **02-dars-ai-aktyor:** AI Personas: The Actor & Mask metaphor, role-playing, and context reset techniques.
- **03-dars-ai-ertakchi:** Storyteller: Character creation, plot formulas (Intro, Problem, Victory), and playful constraint rules ("No letter A", ending in "Meow").
- **04-dars-ai-multfilm:** Cartoon Comics: 4-panel storyboard template, speech bubbles, character visual consistency, and sound effects (BOOM! ZAP!).
- **05-dars-ai-siri-va-detektiv:** AI Detective: Spotting hallucinations, "2 Truths and 1 Lie", cross-checking sources, and cyber safety rules.
- **06-dars-sehrli-korgazma:** The Magic Showcase: Classroom digital museum, compiling the personal portfolio album, presentation culture, and Junior Vibecoder diplomas.

---

## 🛠️ Technical Fixes & Chassis Rules (DO NOT REPEAT)

When generating or modifying `.html` files for the presentations, these are the critical bugs we solved and must never repeat:

1. **The CSS Grid Text-Crush Bug:**
   - **Bug:** Text inside `<li>` elements gets crushed into a 1-word-wide vertical column.
   - **Cause:** `<li>` has `display: grid` in the teacher's CSS.
   - **Fix:** ALL text inside a list item MUST be wrapped in a `<span class="t">`. 
   - **Example:** `<li><span class="t"><b>Bold text:</b> Normal text</span></li>`.

2. **The Missing `</div>` UI Break:**
   - **Bug:** The language/theme toggles (`<div class="bar">`) move away from the bottom right and break the layout.
   - **Cause:** Regex slide replacement accidentally deleted the closing `</div>` belonging to `<div class="stage">`.
   - **Fix:** Always ensure `</div>` exists immediately before `<div class="bar">`.

3. **The Silent Timer JS Crash (Language Toggle Failure):**
   - **Bug:** The presentation loads with all 3 languages visible and the default 'UZ' button is inactive.
   - **Cause:** The JavaScript looks for `<div id="timer">` buttons to attach event listeners. If the slides don't contain a timer, the JS throws a `TypeError` and crashes *before* it can run `setLang('uz')` at the bottom of the script.
   - **Fix:** The timer initialization in the JS has been wrapped in a safety check (`if(document.getElementById('tstart')) { ... }`). Never overwrite this safe JS with the old unsafe JS.

4. **The Base64 System Prompt Leak:**
   - **Bug:** The agent's internal system prompt (`AGENTS.md`) leaked directly into the presentation slides.
   - **Cause:** A generation script accidentally encoded the agent's instructions into the string replacement phase.
   - **Fix:** Keep script generation strictly decoupled from agent context files.


5. **The Invisible Dark Mode Text Bug:**
   - **Bug:** Text becomes completely invisible (white on white, or white on light pink).
   - **Cause:** Hardcoding a light background color (e.g., `background:#FFE7E3`) on a `<div>`, but forgetting that in Dark Mode, the presentation automatically forces text to be white.
   - **Fix:** If you hardcode a background color, you MUST explicitly hardcode a contrasting text color (e.g., `color: #000;`) on that exact same element.

---

## 🧰 Dars qurish to'plami (`assets/kit/`) — 2026-09-21 da qo'shildi

Shassi endi qo'lda nusxa qilinmaydi. `assets/kit/` ichida:

| Fayl | Vazifasi |
|---|---|
| `prez_head.html` / `prez_tail.html` | Prezentatsiya shassisi (CSS, tema, til, izohlar) — 10-11 `14-dars` dan olingan |
| `varaqa_head.html` / `varaqa_tail.html` | Varaqa shassisi. **`@media print` dagi to'rtala selektor va `@page` qo'shilgan** (ma'lum tuzoq #3 tuzatilgan) |
| `build.py` | `Lesson` klassi + `slide`, `box`, `code`, `table`, `rubric` yordamchilari. In-place `data-ru`/`data-en` ni avtomatik yozadi |
| `check.py` | Validator — HTMLParser bilan (regex emas, chunki atribut ichida `<b>` bo'ladi) |
| `l_*.py` | Har darsning mazmuni (slaydlar + NOTES + varaqa) |

Dars qurish: `python3 assets/kit/l_9_w3_13.py` → `prezentatsiya.html` va `varaqa.html`.
Tekshirish: `python3 assets/kit/check.py classes/9-sinf/3-hafta/*/`

`check.py` quyidagilarni ushlaydi: yopilmagan teglar, `</div><!-- /stage -->` yo'qligi,
`.notes[hidden]` yo'qligi, `NOTES` va slaydlar sonining mos kelmasligi, `data-phase`
uch qismli emasligi, `@media print` da to'rtala selektor yo'qligi, `ul.plain li` ichida
`<span class="t">` yo'qligi, va tarjimasiz qolgan `h1..h4/p/th/td/li` elementlari.

## 🆕 4-hafta darslari (va 7-8/9 uchun 3-hafta) — 2026-09-21

Har birida: `prezentatsiya.html` (12 slayd, uch til) + `varaqa.html` (A4) +
`TEACHER_READING.md` + **interaktiv stend** (internetsiz, kutubxonasiz).

* **5-6 `4-hafta/15`** — Dushman AI: holat mashinasi (patrul/sezdi/ta'qib), ko'rish
  radiusi, Line of Sight, xotira taymeri. Stend: `game/` — slayderlar va sekundomer.
* **5-6 `4-hafta/16`** — Level redaktor: 20×10 panjara, RLE level kodi
  (`8a1c1a1d1a6b`), BFS yo'l tekshiruvi (sakrash 3 katak), o'ynash rejimi. Stend: `editor/`.
* **7-8 `3-hafta/13`** — Canvas va o'yin tsikli, RAF vs setInterval, **Delta Time**,
  AABB. Stend `lab/` FPS ni 60/30/15 ga cheklaydi va tezlikni px/s da **o'lchaydi**
  (dt o'chiq: 300→150→75, dt yoniq: 300→300→300).
* **7-8 `3-hafta/14`** — Ochko, kombo, to'lqinlar, holat mashinasi, JSON, `sort`,
  leaderboard. Stendda `💀 CHEAT` va `🛡 TEKSHIRISH` — mijoz ma'lumotiga
  ishonmaslik darsi.
* **9 `3-hafta/13`** — Git: uch zona, commit, branch, merge, **konflikt**. Stend —
  haqiqiy Git sintaksisini qabul qiluvchi simulyator, real 3-tomonlama birlashtirish.
* **9 `3-hafta/14`** — Pull Request va kod ko'rigi. Stenddagi diffda **4 ta xato**,
  ulardan biri (biznes mantiqi) **AI reviewer uchun ko'rinmas** — darsning asosiy nuqtasi.
  O'qituvchi kaliti `TEACHER_READING.md` 2-bo'limida.
* **10-11 `4-hafta/15`** — RAG: chunking, embedding, **kosinus o'xshashlik**, ANN/HNSW,
  grounding. Stend — ishlaydigan TF-IDF + L2 normalizatsiya + top-K. Bazada javobi
  yo'q savol uchun kosinus **aniq 0.000**.
* **10-11 `4-hafta/16`** — Prompt injection (OWASP LLM01). Stendda 4 himoya qatlami.
  Isbotlangan xulosa: **filtrni chetlab o'tish mumkin, imtiyozlarni ajratishni yo'q.**

Barcha 8 stend Node bilan avtomatik sinovdan o'tkazilgan (124 ta xatti-harakat
tekshiruvi): holat mashinalari, kod round-trip, BFS, delta time, `sort`, 3-tomonlama
merge, kosinus xossalari va himoya qatlamlari.
