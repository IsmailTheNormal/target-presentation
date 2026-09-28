#!/usr/bin/env python3
"""
Target International School — 5-6th Grade Track Upgrader
Generates modern, tech-savvy, age-appropriate Game Dev & AI curriculum for lessons 3-6.
100% In-Place data-ru/data-en, Canonical .hw layout, 10-slide 40-minute pacing, full notes.
"""
import os
import json

BASE_DIR = "/home/dpdp/target/classes/5-6-sinf/1-hafta"

# Read logo and styles from 02-dars-ai-aktyor
with open(os.path.join(BASE_DIR, "02-dars-ai-aktyor/prezentatsiya.html"), "r", encoding="utf-8") as f:
    sample_html = f.read()

# Extract header up to <div class="stage">
header_end = sample_html.find('<div class="stage">') + len('<div class="stage">')
HTML_HEADER_BASE = sample_html[:header_end]

# Extract footer from </div>\n<div class="bar"> to end
footer_start = sample_html.find('<div class="bar">')
# Include the closing </div> of stage
stage_close_idx = sample_html.rfind('</div>', 0, footer_start)
HTML_FOOTER_TEMPLATE = sample_html[stage_close_idx:]

print("Header length:", len(HTML_HEADER_BASE), "Footer length:", len(HTML_FOOTER_TEMPLATE))
