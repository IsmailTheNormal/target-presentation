#!/usr/bin/env python3
import os
import json

BASE_DIR = "/home/dpdp/target/classes/5-6-sinf/1-hafta"

# Load base header and footer from 02-dars
with open(os.path.join(BASE_DIR, "02-dars-ai-aktyor/prezentatsiya.html"), "r", encoding="utf-8") as f:
    sample_html = f.read()

header_end = sample_html.find('<div class="stage">') + len('<div class="stage">')
BASE_HEADER = sample_html[:header_end]

footer_start = sample_html.find('<div class="bar">')
stage_close_idx = sample_html.rfind('</div>', 0, footer_start)
BASE_FOOTER_TEMPLATE = sample_html[stage_close_idx:]

def make_presentation(title, slides_html, notes_dict):
    # Title replacement
    t_start = BASE_HEADER.find('<title>')
    t_end = BASE_HEADER.find('</title>') + len('</title>')
    header = BASE_HEADER[:t_start] + f"<title>{title}</title>" + BASE_HEADER[t_end:]
    
    # Notes replacement via fast slice
    notes_json = json.dumps(notes_dict, ensure_ascii=False, indent=2)
    n_start = BASE_FOOTER_TEMPLATE.find('var NOTES = {')
    n_end = BASE_FOOTER_TEMPLATE.find('};', n_start) + 2
    footer = BASE_FOOTER_TEMPLATE[:n_start] + f"var NOTES = {notes_json};" + BASE_FOOTER_TEMPLATE[n_end:]
    
    # Ensure slide count display shows 10 slides
    footer = footer.replace('1 / 14', '1 / 10').replace('1 / 11', '1 / 10')
    return f"{header}\n{slides_html}\n{footer}"

def make_worksheet(num, t_uz, t_ru, t_en, d_uz, d_ru, d_en, boxes_html):
    return f"""<!DOCTYPE html>
<html lang="uz">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{t_uz} - Varaqa</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Manrope:wght@500;700;800&family=Source+Sans+3:wght@400;600;700&family=JetBrains+Mono:wght@400;700&display=swap">
<style>
:root{{
  --bg:#C9D6E8; --sheet:#FFFFFF; --panel:#EDF2F9; --panel-2:#DEE7F3;
  --grid:rgba(0,33,74,.05);
  --ink:#00214A; --ink-2:#46587A; --ink-3:#8496B0;
  --rule:#C4D2E4; --hair:#DCE5F0;
  --accent:#FF1100; --accent-ink:#C21000; --accent-soft:#FFE7E3;
  --green:#0B6B4F;
}}
@media (prefers-color-scheme: dark){{
  :root{{
    --bg:#03101F; --sheet:#0A1D3D; --panel:#102550; --panel-2:#183260;
    --grid:rgba(232,238,247,.05);
    --ink:#E9EFF8; --ink-2:#A2B4CE; --ink-3:#70859F;
    --rule:#22406B; --hair:#1A3358;
    --accent:#FF3B26; --accent-ink:#FF7563; --accent-soft:#3B140F;
    --green:#7FD3B2;
  }}
}}
body{{background:var(--bg); margin:0; padding:20px; display:flex; justify-content:center;
  font-family:"Source Sans 3",sans-serif; color:var(--ink); font-size:10pt}}
.sheet{{background:var(--sheet); width:100%; max-width:210mm; min-height:297mm;
  padding:18mm; box-shadow:0 10px 30px rgba(0,0,0,.1); position:relative; box-sizing:border-box}}
header{{border-bottom:2px solid var(--ink); padding-bottom:12px; margin-bottom:20px;
  display:flex; justify-content:space-between; align-items:flex-end}}
h1{{margin:0; font-family:"Manrope",sans-serif; font-weight:800; font-size:18pt;
  letter-spacing:-.02em; color:var(--ink)}}
.meta{{display:grid; gap:4px; text-align:right}}
.meta span{{font-family:"JetBrains Mono",monospace; font-size:7.5pt;
  text-transform:uppercase; letter-spacing:.05em; color:var(--ink-2)}}
.meta i.s{{display:inline-block; width:40px; border-bottom:1px solid var(--ink-2);
  margin-left:4px; vertical-align:bottom}}
.grid{{display:grid; grid-template-columns:1fr 1fr; gap:16px}}
.box{{border:1px solid var(--rule); padding:12px; border-radius:6px; background:var(--panel)}}
h3{{margin:0 0 8px 0; font-family:"Manrope",sans-serif; color:var(--accent); font-size:11pt;}}
ul, ol{{margin:0; padding-left:18px}}
li{{margin-bottom:6px}}
@media print {{
  body{{background:none; padding:0}}
  .sheet{{box-shadow:none; width:210mm; min-height:297mm; padding:12mm}}
}}
</style>
</head>
<body>
<div class="sheet">
  <header>
    <div>
      <div style="font-family:'JetBrains Mono',monospace; font-size:8pt; color:var(--accent); margin-bottom:4px">
        VIBECODING // 1-HAFTA // {num}-DARS
      </div>
      <h1><span lang="uz">{t_uz}</span><span lang="ru" style="display:none">{t_ru}</span><span lang="en" style="display:none">{t_en}</span></h1>
    </div>
    <div class="meta">
      <span><span lang="uz">O'quvchi</span><span lang="ru" style="display:none">Ученик</span><span lang="en" style="display:none">Student</span> <i class="s" style="width:120px"></i></span>
      <span><span lang="uz">Sinf</span><span lang="ru" style="display:none">Класс</span><span lang="en" style="display:none">Grade</span> <i class="s"></i></span>
      <span><span lang="uz">Sana</span><span lang="ru" style="display:none">Дата</span><span lang="en" style="display:none">Date</span> <i class="s" style="width:70px"></i></span>
    </div>
  </header>

  <p style="margin-bottom:15px; font-size:10.5pt; line-height:1.5;">
    <span lang="uz">{d_uz}</span>
    <span lang="ru" style="display:none">{d_ru}</span>
    <span lang="en" style="display:none">{d_en}</span>
  </p>

  {boxes_html}

</div>
<script>
  var lang = localStorage.getItem('vc-lang') || 'uz';
  document.documentElement.lang = lang;
  document.querySelectorAll('[lang]').forEach(function(el) {{
    if (el.tagName !== 'HTML') {{
      el.style.display = (el.getAttribute('lang') === lang) ? '' : 'none';
    }}
  }});
</script>
</body>
</html>
"""

print("Generator functions compiled cleanly.")
