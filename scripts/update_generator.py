#!/usr/bin/env python3
# -*- coding: utf-8 -*-

with open("scripts/generate_interactive_tests.py", "r", encoding="utf-8") as f:
    content = f.read()

# 1. Replace format_title_with_code definition
old_fmt = '''def format_title_with_code(text):
    """Formats question titles containing code into <pre><code> blocks"""
    # Detect code blocks separated by double newlines or starting with code keywords
    parts = text.split("\\n\\n")
    if len(parts) > 1 and any(kw in parts[1] for kw in ["app.", "const ", "let ", "SELECT", "import ", "function", "docker ", "npm "]):
        title_text = html.escape(parts[0])
        code_text = html.escape("\\n\\n".join(parts[1:]))
        return f'<div class="q-title-text">{title_text}</div><pre class="code-box"><code>{code_text}</code></pre>'
    return f'<div class="q-title-text">{html.escape(text)}</div>' '''

# Let's use substring replacement or regex
import re

old_fmt_re = r'def format_title_with_code\(text\):.*?' + re.escape("return f'<div class=\"q-title-text\">{html.escape(text)}</div>'")
new_fmt = '''def split_title_and_code(text):
    """Splits question title into text prompt and code block if present"""
    parts = text.split("\\n\\n")
    if len(parts) > 1 and any(kw in parts[1] for kw in ["app.", "const ", "let ", "SELECT", "import ", "function", "docker ", "npm ", "<form", "router.", "def ", "curl ", "python", "CREATE ", "SELECT "]):
        return parts[0], "\\n\\n".join(parts[1:])
    return text, None'''

content = re.sub(old_fmt_re, new_fmt, content, flags=re.DOTALL)
print("✓ Replaced format_title_with_code")

# 2. Update question title HTML generation
old_loop_prep = '''        # Title in 3 languages
        t_uz = q["title"]["uz"]
        t_ru = q["title"]["ru"]
        t_en = q["title"]["en"]'''

new_loop_prep = '''        # Title in 3 languages & separated code
        t_uz = q["title"]["uz"]
        t_ru = q["title"]["ru"]
        t_en = q["title"]["en"]
        t_uz_text, code_uz = split_title_and_code(t_uz)
        t_ru_text, _ = split_title_and_code(t_ru)
        t_en_text, _ = split_title_and_code(t_en)
        code_html = f'<pre class="code-box"><code>{html.escape(code_uz)}</code></pre>' if code_uz else ""'''

content = content.replace(old_loop_prep, new_loop_prep)

old_q_html = '''          <div class="q-title" data-ru="{html.escape(t_ru)}" data-en="{html.escape(t_en)}">
            {format_title_with_code(t_uz)}
          </div>'''

new_q_html = '''          <div class="q-title">
            <div class="q-title-text" data-ru="{html.escape(t_ru_text)}" data-en="{html.escape(t_en_text)}">{html.escape(t_uz_text)}</div>
            {code_html}
          </div>'''

content = content.replace(old_q_html, new_q_html)

# 3. Update top-bar styles
old_top_bar_css = '''/* Floating Header Bar */
.top-bar {{
  position: sticky;
  top: 14px;
  z-index: 100;
  max-width: 1000px;
  width: calc(100% - 32px);
  margin: 0 auto 24px;
  background: var(--glass-bg);
  backdrop-filter: blur(16px);
  -webkit-backdrop-filter: blur(16px);
  border: 1px solid var(--glass-border);
  border-radius: 999px;
  padding: 8px 18px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  box-shadow: var(--shadow-sm);
}}

.bar-brand {{
  display: flex;
  align-items: center;
  gap: 12px;
  font-family: "Manrope", sans-serif;
  font-weight: 800;
  font-size: 14px;
  color: var(--ink);
  text-decoration: none;
}}

.bar-brand span.dot {{
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: var(--accent);
  display: inline-block;
}}

.bar-controls {{
  display: flex;
  align-items: center;
  gap: 8px;
}}

.lang-btn, .theme-btn, .back-btn {{
  background: var(--panel-2);
  border: 1px solid var(--rule);
  color: var(--ink-2);
  font-family: "JetBrains Mono", monospace;
  font-size: 12px;
  font-weight: 700;
  padding: 5px 12px;
  border-radius: 999px;
  cursor: pointer;
  transition: all 0.15s ease;
  text-decoration: none;
  display: inline-flex;
  align-items: center;
  gap: 4px;
}}

.lang-btn.active, .lang-btn:hover, .theme-btn:hover, .back-btn:hover {{
  background: var(--ink);
  color: var(--bg);
  border-color: var(--ink);
}}'''

new_top_bar_css = '''/* Floating Header Nav */
.top-nav {{
  position: sticky;
  top: 14px;
  z-index: 100;
  max-width: 900px;
  width: calc(100% - 32px);
  margin: 0 auto 24px;
  background: var(--glass-bg);
  backdrop-filter: blur(14px);
  -webkit-backdrop-filter: blur(14px);
  border: 1px solid var(--glass-border);
  padding: 8px 18px;
  border-radius: 999px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  box-shadow: var(--shadow-sm);
}}

.nav-brand {{
  display: flex;
  align-items: center;
  gap: 10px;
  text-decoration: none;
  color: var(--ink);
}}

.nav-brand .logo-box img {{
  height: 22px;
  width: auto;
  display: block;
}}

.nav-brand .name {{
  font-family: "Manrope", sans-serif;
  font-weight: 800;
  font-size: 14px;
  letter-spacing: 0.04em;
}}

.nav-brand .tag {{
  font-family: "JetBrains Mono", monospace;
  font-size: 11px;
  font-weight: 700;
  color: var(--ink-2);
  letter-spacing: 0.08em;
  text-transform: uppercase;
  padding-left: 8px;
  border-left: 1px solid var(--rule);
}}

.nav-tools {{
  display: flex;
  align-items: center;
  gap: 4px;
}}

.dock-btn {{
  background: transparent;
  border: none;
  color: var(--ink-2);
  font-family: "JetBrains Mono", monospace;
  font-size: 12px;
  font-weight: 700;
  padding: 6px 12px;
  border-radius: 999px;
  cursor: pointer;
  transition: all 0.18s ease;
  text-decoration: none;
  display: inline-flex;
  align-items: center;
  justify-content: center;
}}

.dock-btn:hover {{
  color: var(--ink);
  background: var(--rule-light);
}}

.dock-btn.active {{
  color: var(--ink);
  background: var(--panel-2);
  border: 1px solid var(--rule);
  box-shadow: 0 2px 6px rgba(0,0,0,0.12);
}}'''

content = content.replace(old_top_bar_css, new_top_bar_css)

# 4. Update top-bar HTML
old_top_bar_html = '''<!-- Floating Header -->
<div class="top-bar">
  <a href="/index.html" class="bar-brand">
    <span class="dot"></span>
    <span>TARGET · TEST RUNNER</span>
  </a>
  <div class="bar-controls">
    <a href="/index.html" class="back-btn" data-ru="🏠 Портал" data-en="🏠 Portal">🏠 Bosh sahifa</a>
    <button type="button" class="lang-btn active" data-lang="uz" onclick="setLang('uz')">UZ</button>
    <button type="button" class="lang-btn" data-lang="ru" onclick="setLang('ru')">RU</button>
    <button type="button" class="lang-btn" data-lang="en" onclick="setLang('en')">EN</button>
    <button type="button" class="theme-btn" onclick="toggleTheme()" title="Theme">🌓</button>
  </div>
</div>'''

new_top_bar_html = '''<!-- Floating Header Nav -->
<nav class="top-nav">
  <a href="/index.html" class="nav-brand">
    <div class="logo-box"><img src="/assets/target-logo.png" alt="Target Logo"></div>
    <span class="name">TARGET</span>
    <span class="tag">{cohort_id.upper()} · TEST</span>
  </a>
  <div class="nav-tools">
    <button type="button" class="dock-btn lang-btn active" data-lang="uz" onclick="setLang('uz')">UZ</button>
    <button type="button" class="dock-btn lang-btn" data-lang="ru" onclick="setLang('ru')">RU</button>
    <button type="button" class="dock-btn lang-btn" data-lang="en" onclick="setLang('en')">EN</button>
    <button type="button" class="dock-btn" onclick="toggleTheme()" title="Mavzu" data-title-ru="Тема" data-title-en="Theme">🌓</button>
    <a href="/index.html" class="dock-btn back-btn" title="Bosh sahifa" data-title-ru="Главная" data-title-en="Home">🏠</a>
  </div>
</nav>'''

content = content.replace(old_top_bar_html, new_top_bar_html)

# 5. Update setLang and DOMContentLoaded
old_set_lang = '''function setLang(lang) {{
  currentLang = lang;
  document.documentElement.lang = lang;'''

new_set_lang = '''function setLang(lang) {{
  currentLang = lang;
  try {{ localStorage.setItem('target_lang', lang); }} catch(e) {{}}
  document.documentElement.lang = lang;'''

content = content.replace(old_set_lang, new_set_lang)

old_dom_load = '''document.addEventListener('DOMContentLoaded', function() {{
  var savedTheme = 'dark';
  try {{ savedTheme = localStorage.getItem('target_theme') || 'dark'; }} catch(e) {{}}
  document.documentElement.setAttribute('data-theme', savedTheme);
  setLang('uz');
  loadStudentProfile();
}});'''

new_dom_load = '''document.addEventListener('DOMContentLoaded', function() {{
  var savedTheme = 'dark';
  try {{ savedTheme = localStorage.getItem('target_theme') || 'dark'; }} catch(e) {{}}
  document.documentElement.setAttribute('data-theme', savedTheme);
  var savedLang = 'uz';
  try {{ savedLang = localStorage.getItem('target_lang') || 'uz'; }} catch(e) {{}}
  setLang(savedLang);
  loadStudentProfile();
}});'''

content = content.replace(old_dom_load, new_dom_load)

with open("scripts/generate_interactive_tests.py", "w", encoding="utf-8") as f:
    f.write(content)

print("Finished updating generate_interactive_tests.py!")
