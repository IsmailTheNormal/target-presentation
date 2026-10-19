#!/usr/bin/env python3
"""
scripts/fix_modals_and_tech_terms.py

Fixes:
1. Modals (#notesModal, #helpModal) permanently displayed on slide load due to class/CSS mismatch.
   - Converts <div class="notes-modal" id="notesModal"> to class="modal-overlay"
   - Updates CSS to guarantee .modal-overlay has display:none by default and display:flex when open/active/is-open
   - Updates JS toggle functions and Escape key handler
2. Tech terms auto-search & asterisks:
   - Excludes headings (h1..h6, .hero-title, .section-title, .eyebrow, .kicker, .num, .col-title, .col-num)
   - Excludes interactive and navigation elements
   - Reduces asterisk size to 0.65em so it never looks gigantic
   - Adds white-space: nowrap to .tech-term so phrases like 'Foreign Key' don't break awkwardly across lines
"""

import os
import re
import glob

PRESENTATIONS = [
    "classes/9-sinf/6-hafta/26-dars-mvc-backend-va-relyatsion-baza/prezentatsiya.html",
    "classes/10-11-sinf/7-hafta/31-dars-penetration-testing-va-ethical-hacking/prezentatsiya.html",
    "classes/7-8-sinf/7-hafta/29-dars-gps-navigatsiya-va-eng-qisqa-yol/prezentatsiya.html",
    "classes/5-6-sinf/7-hafta/21-dars-raqamli-iz-va-maxfiylik/prezentatsiya.html",
    "classes/9-sinf/7-hafta/27-dars-veb-xavfsizlik-xss-va-csrf/prezentatsiya.html",
    "classes/9-sinf/8-hafta/28-dars-fullstack-xavfsiz-servis-oraliq-nazorat/prezentatsiya.html",
    "classes/10-11-sinf/8-hafta/32-dars-korporativ-himoya-va-ctf/prezentatsiya.html",
    "classes/7-8-sinf/8-hafta/30-dars-sport-simulyatori-oraliq-nazorat/prezentatsiya.html",
    "classes/5-6-sinf/8-hafta/22-dars-kiber-qalqon-oraliq-nazorat/prezentatsiya.html"
]

NEW_TECH_TERMS_CSS = """/* Tech Terms Search & Asterisk Styling */
.tech-term {
  color: var(--accent-ink, #c21000);
  cursor: pointer;
  display: inline;
  white-space: nowrap;
  position: relative;
  text-decoration: underline dotted 1.5px rgba(255, 17, 0, 0.6);
  text-underline-offset: 3px;
  border-radius: 3px;
  padding: 0 2px;
  transition: all 0.15s ease;
}
:root[data-theme="dark"] .tech-term {
  color: #FF6B57;
  text-decoration-color: rgba(255, 107, 87, 0.7);
}
.tech-term:hover, .tech-term:focus-visible {
  color: #FFFFFF !important;
  background: var(--accent, #FF1100);
  text-decoration: none;
  outline: none;
  box-shadow: 0 2px 8px rgba(255, 17, 0, 0.35);
}
:root[data-theme="dark"] .tech-term:hover, :root[data-theme="dark"] .tech-term:focus-visible {
  background: #FF2B1A;
  color: #FFFFFF !important;
}
.tech-term .term-star {
  font-size: 0.65em;
  font-weight: 700;
  vertical-align: super;
  margin-left: 1.5px;
  color: var(--accent, #FF1100);
  line-height: 0;
  display: inline-block;
  user-select: none;
  transition: transform 0.15s ease;
}
.tech-term:hover .term-star, .tech-term:focus-visible .term-star {
  color: #FFFFFF !important;
  transform: translateY(-1px) scale(1.1);
}"""

MODAL_OVERLAY_CSS = """.modal-overlay {
  position: fixed;
  inset: 0;
  background: rgba(6, 21, 48, 0.75);
  backdrop-filter: blur(10px);
  -webkit-backdrop-filter: blur(10px);
  z-index: 2000;
  display: none;
  align-items: center;
  justify-content: center;
  padding: 20px;
}

.modal-overlay.open,
.modal-overlay.active,
.modal-overlay.is-open {
  display: flex !important;
}

.notes-modal {
  display: none !important;
}"""

def fix_presentation(filepath):
    if not os.path.exists(filepath):
        print(f"Skipping {filepath} (does not exist)")
        return

    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    orig_content = content

    # 1. Fix modal classes in HTML
    content = re.sub(r'<div class="notes-modal" id="notesModal"', '<div class="modal-overlay" id="notesModal"', content)
    content = re.sub(r'<div class="notes-modal" id="helpModal"', '<div class="modal-overlay" id="helpModal"', content)

    # 2. Fix CSS for .modal-overlay
    if ".modal-overlay {" in content:
        content = re.sub(
            r'\.modal-overlay\s*\{[^}]*\}',
            MODAL_OVERLAY_CSS,
            content
        )
    else:
        # Append before </style>
        content = content.replace("</style>", MODAL_OVERLAY_CSS + "\n</style>")

    # 3. Replace tech-terms CSS
    tech_css_pattern = r'/\*\s*Tech Terms Search & Asterisk Styling\s*\*/.*?\.tech-term:hover \.term-star,\s*\.tech-term:focus-visible \.term-star\s*\{[^}]*\}'
    if re.search(tech_css_pattern, content, re.DOTALL):
        content = re.sub(tech_css_pattern, NEW_TECH_TERMS_CSS, content, flags=re.DOTALL)
    elif ".tech-term {" in content:
        # Replace up to term-star hover
        content = re.sub(r'\.tech-term\s*\{.*?\.tech-term:hover \.term-star[^}]*\}', NEW_TECH_TERMS_CSS, content, flags=re.DOTALL)

    # 4. Fix acceptNode inside applyTechTermLinks
    old_accept_node_pattern = r'acceptNode:\s*function\(node\)\s*\{.*?return NodeFilter\.FILTER_SKIP;\s*\}'
    new_accept_node = """acceptNode: function(node) {
          var parent = node.parentElement;
          if (!parent) return NodeFilter.FILTER_REJECT;
          var tag = parent.tagName.toLowerCase();
          if (tag === 'code' || tag === 'pre' || tag === 'script' || tag === 'style' || tag === 'button' ||
              tag === 'h1' || tag === 'h2' || tag === 'h3' || tag === 'h4' || tag === 'h5' || tag === 'h6' ||
              tag === 'kbd' || tag === 'a' || tag === 'input' || tag === 'select' || tag === 'textarea') {
            return NodeFilter.FILTER_REJECT;
          }
          if (parent.closest('.hero-title') || parent.closest('.section-title') || parent.closest('.eyebrow') ||
              parent.closest('.kicker') || parent.closest('.num') || parent.closest('.col-num') || parent.closest('.col-title') ||
              parent.closest('.quiz-box') || parent.closest('.tech-term') || parent.closest('a') ||
              parent.closest('.dock-pill') || parent.closest('.floating-brand') || parent.closest('.floating-dock') ||
              parent.closest('.modal-box') || parent.closest('.modal-card')) {
            return NodeFilter.FILTER_REJECT;
          }
          if (pattern.test(node.nodeValue)) {
            pattern.lastIndex = 0;
            return NodeFilter.FILTER_ACCEPT;
          }
          return NodeFilter.FILTER_SKIP;
        }"""
    content = re.sub(old_accept_node_pattern, new_accept_node, content, flags=re.DOTALL)

    # 5. Fix toggleNotes and toggleHelp in JavaScript
    old_toggle_notes = r'function toggleNotes\(\)\s*\{[^}]*\}'
    new_toggle_notes = """function toggleNotes() {
  var m = document.getElementById("notesModal");
  if (!m) return;
  var isOpen = m.classList.contains("open") || m.classList.contains("active") || m.classList.contains("is-open");
  if (isOpen) {
    m.classList.remove("open", "active", "is-open");
    var btn = document.getElementById("notesBtn");
    if (btn) btn.classList.remove("is-active", "active");
  } else {
    m.classList.add("open", "active", "is-open");
    var btn = document.getElementById("notesBtn");
    if (btn) btn.classList.add("is-active", "active");
    if (typeof updateSlideView === "function") updateSlideView();
  }
}"""
    content = re.sub(old_toggle_notes, new_toggle_notes, content)

    old_toggle_help = r'function toggleHelp\(\)\s*\{[^}]*\}'
    new_toggle_help = """function toggleHelp() {
  var m = document.getElementById("helpModal");
  if (!m) return;
  var isOpen = m.classList.contains("open") || m.classList.contains("active") || m.classList.contains("is-open");
  if (isOpen) {
    m.classList.remove("open", "active", "is-open");
    var btn = document.getElementById("helpBtn");
    if (btn) btn.classList.remove("is-active", "active");
  } else {
    m.classList.add("open", "active", "is-open");
    var btn = document.getElementById("helpBtn");
    if (btn) btn.classList.add("is-active", "active");
  }
}"""
    content = re.sub(old_toggle_help, new_toggle_help, content)

    # 6. Ensure Escape key closes both modals
    if 'e.key === "Escape"' in content:
        content = re.sub(
            r'else\s+if\s*\((?:e\.key\s*===\s*["\']Escape["\']|e\.keyCode\s*===\s*27)\)\s*\{[^}]*\}',
            '''else if (e.key === "Escape" || e.keyCode === 27) {
    var m1 = document.getElementById("notesModal");
    var m2 = document.getElementById("helpModal");
    if (m1) m1.classList.remove("open", "active", "is-open");
    if (m2) m2.classList.remove("open", "active", "is-open");
    var b1 = document.getElementById("notesBtn");
    var b2 = document.getElementById("helpBtn");
    if (b1) b1.classList.remove("is-active", "active");
    if (b2) b2.classList.remove("is-active", "active");
  }''',
            content
        )

    if content != orig_content:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Fixed: {filepath}")
    else:
        print(f"No changes needed: {filepath}")

if __name__ == "__main__":
    for p in PRESENTATIONS:
        fix_presentation(p)
