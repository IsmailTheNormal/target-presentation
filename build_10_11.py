#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Builder script for 10-11-sinf:
- 15-dars: RAG (Retrieval-Augmented Generation) va Vektor Qidiruv
- 16-dars: Avtonom Agentlar va Kengaytirilgan Xotira
"""

import os

# Helper to read base template parts from lesson 14
with open("classes/10-11-sinf/3-hafta/14-dars-tool-calling-va-funksiyalar/prezentatsiya.html", "r", encoding="utf-8") as f:
    p14_content = f.read()

# Extract header (up to <div class="stage">)
header_idx = p14_content.find('<div class="stage">')
HEADER = p14_content[:header_idx + len('<div class="stage">')]

# Extract footer starting from <div class="bar">
footer_idx = p14_content.find('<div class="bar">')
FOOTER_TEMPLATE = p14_content[footer_idx:]

with open("classes/10-11-sinf/3-hafta/14-dars-tool-calling-va-funksiyalar/varaqa.html", "r", encoding="utf-8") as f:
    v14_content = f.read()

v_sheet_idx = v14_content.find('<div class="sheet">')
V_HEADER = v14_content[:v_sheet_idx]

print("Base templates extracted successfully.")
