# MASTER PROMPT: Course Material Showcase Portal & Generator Architect

> **Prompt Nomi:** `Course Showcase Portal Generator Master Prompt`  
> **Maqsad:** Har qanday darslik, kurs yoki maktab o'quv materiallari omboridan (taqdimotlar, ishchi varaqalar, laboratoriyalar, yo'riqnomalar) zamonaviy, tezkor, mustaqil (zero-dependency) va 3 bosqichli navigatsiyaga ega **Showcase Veb-Portali (`index.html`)** va **Avtomatlashtirilgan Skaner Skripti (`build_portal.py`)** ni yaratish.

---

## 📋 Master Prompt Matni (AI Agentlar uchun to'liq nusxalanadigan ko'rsatma)

Ushbu matnni to'g'ridan-to'g'ri AI modelga (Claude, ChatGPT, Gemini, Antigravity, Cursor) yuboring:

```markdown
# MISSION: Build a Production-Grade Course Material Showcase Portal & Scanner

You are an expert Frontend Architect, EdTech Product Designer, and Static Site Specialist.
Your mission is to inspect the course repository/folder structure and generate a high-performance, zero-dependency, ultra-sleek **Course Material Showcase Portal (`index.html`)** along with an automated Python crawler/builder script (`build_portal.py`).

The portal serves as the single entry point for students, educators, and administrators to browse, search, and launch all learning assets (interactive slide decks, printable worksheets, browser-based labs/studios, and teacher guides).

---

## 1. DESIGN PHILOSOPHY & AESTHETIC STANDARDS

1. **Enterprise SaaS / Developer Hub Aesthetic:**
   - Draw inspiration from Linear, Supabase, Vercel, and Stripe.
   - Avoid generic, cluttered, or dated LMS appearances (e.g. default Moodle or basic Bootstrap).
   - Use generous whitespace, crisp border rules (`1px solid var(--rule)`), smooth micro-interactions, subtle shadows, and modern pill tabs.

2. **Zero-Dependency Architecture:**
   - Pure Vanilla HTML5, CSS3, and ES6+ JavaScript.
   - NO Node.js/npm dependencies, NO Webpack/Vite build steps required at runtime.
   - Must execute completely offline or over `file:///` local protocol, as well as when deployed to GitHub Pages, Cloudflare Pages, or Vercel.

3. **Typography & Design Tokens:**
   - Headings: `"Manrope", sans-serif` (800 weight, tight tracking `-0.02em`).
   - Body: `"Source Sans 3", system-ui, sans-serif` (clean, accessible line-height 1.5).
   - Monospace & Numbers: `"JetBrains Mono", monospace` (badges, slugs, tags).
   - Colors (via CSS Custom Properties):
     - Dark Mode (default or toggleable): Background `#061530`, Panel `#0E2249`, Panel-2 `#16305A`, Text `#E9EFF8`, Muted `#A2B4CE`.
     - Light Mode: Background `#F4F7FC`, Panel `#FFFFFF`, Panel-2 `#E8EEF8`, Text `#00214A`, Muted `#46587A`.
     - Brand Accent: Primary `#FF1100` / `#FF3B26`, Lab Accent Emerald `#10B981` / `#059669`.

4. **Multi-Language (In-Place i18n):**
   - Trilingual standard (e.g., UZ primary with `data-ru` and `data-en` attributes, or customizable per project).
   - Zero-blank fallback: If a translation is missing, gracefully display the primary text.
   - Instant language switching across all static UI and dynamic cards without reloading the page.
   - Persist user's language choice in `localStorage`.

5. **Theme Toggle (Dark / Light):**
   - Seamless dark/light theme switcher with `localStorage` persistence and `prefers-color-scheme` support.

---

## 2. USER EXPERIENCE & INTERACTIVE WORKFLOW

Implement a **3-Step Progressive Disclosure Flow**:

### Step 1: Cohort / Grade / Track Selection
- Render distinct cards for each cohort (e.g., "Grades 10–11 Senior AI", "Grade 9 DevOps", "Grades 7–8 Game Dev", "Grades 5–6 Junior Creators").
- Each card must display:
  - Custom Emoji / Icon
  - Track Badge (e.g., `Senior Track`, `DevOps Track`)
  - Cohort Title & localized description
  - Total lesson counter badge
  - Interactive hover state and active indicator bar.

### Step 2: Week / Unit Navigation Tabs
- Upon selecting a cohort, show horizontal scrollable pill tabs for all available weeks/units.
- Each pill displays the week label and total lesson count.
- Clicking a week filters the lesson cards instantly with smooth transitions.

### Step 3: Responsive Lesson Grid Cards
- Display lesson cards in a responsive CSS Grid (`repeat(auto-fill, minmax(360px, 1fr))`).
- Each lesson card must contain:
  1. **Header:** Lesson number badge (`#01`, `#02`, ...), Week indicator tag, and Last Modified date badge (if available).
  2. **Content:** Bold lesson title and clamped 2–3 line elevator pitch/lede description.
  3. **Action Buttons:**
     - **Prezentatsiya / Slides (`prezentatsiya.html`):** Primary navy/accent button.
     - **Ishchi varaqa / Worksheet (`varaqa.html`):** Secondary clean outline button.
     - **Interaktiv Studio / Lab (`lab/index.html` or `studio/index.html`):** Eye-catching emerald gradient button (rendered ONLY if the interactive tool exists).
     - **Copy Deep Link:** Icon button to copy the direct URL with toast notification feedback.

### Global Real-Time Search:
- Prominent header search box with instant debounced filtering.
- Queries match across lesson titles, descriptions, lesson numbers, cohort names, and topics.
- When searching, dynamically switch to a dedicated "Search Results" view displaying total hits, highlighted terms, and a "Clear Search" button.

### Deep Linking & Breadcrumbs:
- Synchronize active view with URL Hash (e.g., `#10-11-sinf/4-hafta` or `#search=docker`).
- Sticky Breadcrumb / Path banner showing `🏠 Home / Cohort / Week` with a one-click "Copy URL" button and animated toast feedback.

---

## 3. DATA SCHEMA & CRAWLER SPECIFICATION

The portal is driven by a clean, embedded or fetched JSON dataset:

```json
[
  {
    "id": "10-11-sinf",
    "title": { "uz": "10–11-sinf", "ru": "10–11 классы", "en": "Grades 10–11" },
    "desc": { "uz": "Tavsif", "ru": "Описание", "en": "Description" },
    "badge": "Senior Track",
    "icon": "🎓",
    "weeks": [
      {
        "id": "1-hafta",
        "title": { "uz": "1-hafta", "ru": "1-неделя", "en": "Week 1" },
        "lessons": [
          {
            "id": "01-dars-mavzu",
            "num": "01",
            "title": { "uz": "Mavzu", "ru": "Тема", "en": "Topic" },
            "lede": { "uz": "Qisqa izoh", "ru": "Краткое описание", "en": "Short pitch" },
            "has_p": true,
            "p_url": "classes/10-11-sinf/1-hafta/01-dars-mavzu/prezentatsiya.html",
            "has_v": true,
            "v_url": "classes/10-11-sinf/1-hafta/01-dars-mavzu/varaqa.html",
            "interactive_url": "classes/10-11-sinf/1-hafta/01-dars-mavzu/lab/index.html",
            "interactive_name": { "uz": "Interaktiv Lab", "ru": "Интерактивная Лаба", "en": "Interactive Lab" },
            "modified": "12.10.2026"
          }
        ]
      }
    ]
  }
]
```

### Python Crawler Requirements (`build_portal.py`):
1. Traverse the repository filesystem starting from the `classes/` (or curriculum) root directory.
2. For each lesson directory:
   - Check existence of `prezentatsiya.html` and `varaqa.html`.
   - Scan subdirectories for interactive apps: `["studio", "lab", "arena", "builder", "simulator", "market", "scanner", "game", "editor"]`.
   - Parse HTML headers (`<h1>`) to extract trilingual titles (`data-ru`, `data-en`, or fallback to text).
   - Parse `<p class="lede">` or meta tags to extract trilingual summaries.
   - Extract lesson numbers from directory prefixes (`01-`, `02-`).
3. Inject the compiled JSON dataset into `window.COURSE_DATA = [...]` inside `index.html`.
4. Embed brand assets (such as base64 logos from `assets/logo-light.txt` and `assets/logo-dark.txt` or standard SVG icons).

---

## 4. DELIVERABLES EXPECTED

When you run this task, produce:
1. `build_portal.py`: Robust, self-contained Python 3 script with clear CLI feedback.
2. `index.html`: Fully self-contained, responsive, dark/light themeable, trilingual showcase website.
3. Verification: Run `python3 build_portal.py` to ensure it generates valid HTML and all links are functional.
```

---

## 🛠️ Qanday Sozlash va Foydalanish Mumkin (O'qituvchi va Dasturchi Uchun)

### 1. Fayllar Tuzilmasi Mosligi
Agar loyihangiz boshqa papka tuzilmasiga ega bo'lsa (masalan `courses/module-1/lesson-1/` yoki `curriculum/grade-9/`), promptdagi quyidagi o'zgaruvchilarni moslashtiring:
- `CLASSES_DIR`: Kurs papkasining nomi (`classes`, `courses`, `curriculum`).
- Taqdimot nomi: `prezentatsiya.html` yoki `slides.html`.
- Ishchi varaqa nomi: `varaqa.html` yoki `worksheet.html`.
- Interaktiv ilovalar: `lab/`, `studio/`, `demo/`, `notebook/`.

### 2. Promptni Ishlatish Usuli
1. Yuqoridagi Master Prompt kod blokini to'liq nusxalang.
2. O'zingiz ishlayotgan loyihada AI yordamchisiga yuboring:
   > *"Ushbu Master Prompt asosida loyihamizdagi barcha mavjud dars materiallarini skanerlab, `index.html` portalini va `build_portal.py` generatorini tayyorlab ber."*
3. AI avtomatik tarzda:
   - Papkalarni aylanib chiqadi;
   - Sarlavhalar va qisqa mazmunni tahlil qiladi;
   - Barcha tugmalar va havolalarni tekshiradi;
   - Qidiruv, tillar va mavzular bilan to'liq ishlaydigan `index.html` ni yaratadi.
