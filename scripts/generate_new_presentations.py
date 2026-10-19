#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Target International School — Minimalist Typographic Presentation Generator
Generates full 12-slide modern presentations with:
- Minimalist typographic design (Zero bottom bar, huge text, no visual boxes)
- Top-right floating pill dock: [UZ | RU | EN] [🌓] [📝] [⌨️]
- Floating slide counter and phase badge
- In-slide interactive Quiz & "Yechimni ko'rish (Fix)" toggle
- 100% trilingual in-place localization (data-ru, data-en)
- Complete teacher notes (UZ/RU/EN)
"""

import os
import json
import html

# We will generate presentation for 26-dars, 31-dars, 29-dars, 21-dars
# Let's inspect the exact CSS chassis from 28-dars
with open("classes/9-sinf/8-hafta/28-dars-fullstack-xavfsiz-servis-oraliq-nazorat/prezentatsiya.html", "r", encoding="utf-8") as f:
    template_content = f.read()

# Extract head CSS and scripts from 28-dars
css_start = template_content.find("<style>")
css_end = template_content.find("</style>") + len("</style>")
head_css = template_content[css_start:css_end]

js_start = template_content.find("<script>")
js_end = template_content.rfind("</script>") + len("</script>")
base_js = template_content[js_start:js_end]

print("Chassis CSS and JS extracted successfully!")
