#!/usr/bin/env python3
import os
import re

BASE_DIR = "/home/dpdp/target/classes/5-6-sinf/1-hafta"

# Base footer with placeholder for NOTES
def make_footer(notes_json_str):
    with open(os.path.join(BASE_DIR, "02-dars-ai-aktyor/prezentatsiya.html"), "r", encoding="utf-8") as f:
        html = f.read()
    
    footer_start = html.find('<div class="bar">')
    stage_close_idx = html.rfind('</div>', 0, footer_start)
    footer = html[stage_close_idx:]
    
    # Replace NOTES = { ... };
    notes_pattern = re.compile(r'var\s+NOTES\s*=\s*\{.*?\};', re.DOTALL)
    new_notes = f"var NOTES = {notes_json_str};"
    footer = notes_pattern.sub(new_notes, footer)
    return footer

with open(os.path.join(BASE_DIR, "02-dars-ai-aktyor/prezentatsiya.html"), "r", encoding="utf-8") as f:
    sample_html = f.read()
header_end = sample_html.find('<div class="stage">') + len('<div class="stage">')
BASE_HEADER = sample_html[:header_end]

print("Script template ready.")
