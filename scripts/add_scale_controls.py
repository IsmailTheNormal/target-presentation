#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
scripts/add_scale_controls.py — Inject live Scale Controller into presentations.

Enables:
  - Visual scale adjustment buttons in the bottom-right dock ([-] [100%] [+])
  - Keyboard shortcuts (+ / - to zoom, 0 to reset)
  - Two-finger pinch-to-zoom on Smartboards & tablets
  - localStorage ('target_scale') persistence
  - 100% in-place trilingual (UZ, RU, EN) compliance
"""

import os
import sys
import re
import subprocess

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

SCALE_CSS = """:root {
  --deck-scale: 1;"""

SCALE_DOCK_BTN_CSS = """.dock-btn.scale-label-btn {
  font-size: 11px;
  font-weight: 800;
  letter-spacing: 0.02em;
  padding: 5px 8px;
  min-width: 44px;
}"""

SCALE_DOCK_HTML = """  <span style="width:1px; height:16px; background:var(--rule); margin:0 2px;"></span>
  <button class="dock-btn" onclick="adjustScale(-0.1)" title="Masshtabni kichraytirish (-)" data-title-ru="Уменьшить масштаб (-)" data-title-en="Zoom out (-)" aria-label="Masshtabni kichraytirish">
    <svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" aria-hidden="true"><line x1="5" y1="12" x2="19" y2="12"/></svg>
  </button>
  <button class="dock-btn scale-label-btn" onclick="cycleScale()" title="Masshtabni o'zgartirish yoki tiklash (0)" data-title-ru="Сменить или сбросить масштаб (0)" data-title-en="Cycle or reset scale (0)" aria-label="Masshtab">
    <span id="scaleLabel">100%</span>
  </button>
  <button class="dock-btn" onclick="adjustScale(0.1)" title="Masshtabni kattalashtirish (+)" data-title-ru="Увеличить масштаб (+)" data-title-en="Zoom in (+)" aria-label="Masshtabni kattalashtirish">
    <svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" aria-hidden="true"><line x1="12" y1="5" x2="12" y2="19"/><line x1="5" y1="12" x2="19" y2="12"/></svg>
  </button>"""

HELP_ROW_HTML = """      <div><kbd>+</kbd> / <kbd>-</kbd> / <kbd>0</kbd></div>
      <div data-ru="Масштаб (увеличить / уменьшить / 100%)" data-en="Presentation scale (zoom in / zoom out / reset)">Masshtab (kattalashtirish / kichraytirish / 100%)</div>"""

SCALE_JS = """// ============================================================
// PRESENTATION SCALE CONTROLLER (Direct in-deck zoom & Smartboard pinch)
// ============================================================
var currentScale = 1.0;
var MIN_SCALE = 0.6;
var MAX_SCALE = 1.6;

function setScale(scale) {
  currentScale = Math.min(MAX_SCALE, Math.max(MIN_SCALE, Math.round(scale * 100) / 100));
  document.documentElement.style.setProperty("--deck-scale", currentScale);
  var slidesList = document.querySelectorAll(".slide");
  slidesList.forEach(function(s) {
    s.style.zoom = currentScale;
  });
  var lbl = document.getElementById("scaleLabel");
  if (lbl) {
    lbl.textContent = Math.round(currentScale * 100) + "%";
  }
  try { localStorage.setItem("target_scale", currentScale.toString()); } catch(e) {}
}

function adjustScale(delta) {
  var next = Math.round((currentScale + delta) * 10) / 10;
  setScale(next);
}

function resetScale() {
  setScale(1.0);
}

function cycleScale() {
  var presets = [1.0, 1.15, 1.3, 1.5, 0.85];
  var next = presets[0];
  for (var i = 0; i < presets.length; i++) {
    if (Math.abs(presets[i] - currentScale) < 0.05) {
      next = presets[(i + 1) % presets.length];
      break;
    }
  }
  setScale(next);
}"""

TOUCH_PINCH_JS = """// Touch / Swipe Navigation & Smartboard Pinch-to-Zoom
var touchStartX = 0, touchStartY = 0, touchStartTime = 0;
var initialPinchDist = 0, pinchStartScale = 1.0;

document.addEventListener("touchstart", function(e) {
  if (e.touches && e.touches.length === 2) {
    var dx = e.touches[0].clientX - e.touches[1].clientX;
    var dy = e.touches[0].clientY - e.touches[1].clientY;
    initialPinchDist = Math.hypot(dx, dy);
    pinchStartScale = currentScale;
  } else if (e.touches && e.touches.length === 1) {
    touchStartX = e.touches[0].clientX;
    touchStartY = e.touches[0].clientY;
    touchStartTime = Date.now();
  }
}, { passive: true });

document.addEventListener("touchmove", function(e) {
  if (e.touches && e.touches.length === 2 && initialPinchDist > 0) {
    var dx = e.touches[0].clientX - e.touches[1].clientX;
    var dy = e.touches[0].clientY - e.touches[1].clientY;
    var dist = Math.hypot(dx, dy);
    var ratio = dist / initialPinchDist;
    var targetScale = Math.round(pinchStartScale * ratio * 10) / 10;
    if (Math.abs(targetScale - currentScale) >= 0.05) {
      setScale(targetScale);
    }
  }
}, { passive: true });

document.addEventListener("touchend", function(e) {
  if (e.touches && e.touches.length < 2) {
    initialPinchDist = 0;
  }
  if (e.changedTouches && e.changedTouches.length === 1 && initialPinchDist === 0) {
    var dx = e.changedTouches[0].clientX - touchStartX;
    var dy = e.changedTouches[0].clientY - touchStartY;
    var dt = Date.now() - touchStartTime;
    if (Math.abs(dx) > 40 && Math.abs(dx) > Math.abs(dy) * 1.3 && dt < 800) {
      var target = e.target;
      if (target.closest("input, textarea, select, button, .quiz-box, .code-snippet, .notes-drawer, .notes-modal")) return;
      if (dx < 0) { nextSlide(); } else { prevSlide(); }
    }
  }
}, { passive: true });"""

DOM_INIT_JS = """  var savedScale = 1.0;
  try {
    var rawScale = localStorage.getItem("target_scale");
    if (rawScale) savedScale = parseFloat(rawScale);
  } catch(e) {}
  if (savedScale && !isNaN(savedScale) && savedScale >= MIN_SCALE && savedScale <= MAX_SCALE) {
    setScale(savedScale);
  } else {
    setScale(1.0);
  }"""


def upgrade_file(path):
    print(f"\nProcessing {os.path.relpath(path, REPO_ROOT)}...")
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    orig_content = content

    # 1. CSS: --deck-scale
    if "--deck-scale" not in content:
        content = re.sub(r':root\s*\{', ':root {\n  --deck-scale: 1;', content, count=1)

    # 2. CSS: .dock-btn.scale-label-btn
    if ".scale-label-btn" not in content:
        if ".dock-btn.nav-btn {" in content:
            content = content.replace(".dock-btn.nav-btn {", f"{SCALE_DOCK_BTN_CSS}\n.dock-btn.nav-btn {{", 1)
        elif ".dock-btn:hover" in content:
            content = content.replace(".dock-btn:hover", f"{SCALE_DOCK_BTN_CSS}\n.dock-btn:hover", 1)

    # 3. CSS: .slide zoom
    if "zoom: var(--deck-scale" not in content:
        # Match .slide { ... }
        def repl_slide(m):
            body = m.group(0)
            if "zoom:" not in body:
                return body[:-1] + "  zoom: var(--deck-scale, 1);\n}"
            return body
        content = re.sub(r'\.slide\s*\{[^}]*\}', repl_slide, content, count=1)

    # 4. Dock HTML: insert scale controls
    if "adjustScale" not in content:
        # Target either after the language buttons or before theme button
        if re.search(r'data-lang=["\']en["\'][^>]*>EN</button>', content):
            pattern = r'(data-lang=["\']en["\'][^>]*>EN</button>\s*(?:<span[^>]*class=["\']dock-sep["\'][^>]*></span>|<span[^>]*style=["\'][^"\']*var\(--rule\)[^"\']*>[^<]*</span>)?)'
            replacement = r'\1\n' + SCALE_DOCK_HTML
            content = re.sub(pattern, replacement, content, count=1)
        elif 'onclick="toggleTheme()"' in content:
            content = content.replace('<button class="dock-btn" onclick="toggleTheme()"', SCALE_DOCK_HTML + '\n  <span style="width:1px; height:16px; background:var(--rule); margin:0 2px;"></span>\n  <button class="dock-btn" onclick="toggleTheme()"', 1)

    # 5. Help modal shortcut row
    if "Presentation scale" not in content and "Prezentatsiya masshtabi" not in content and "Masshtab (" not in content:
        if '<div><kbd>Esc</kbd></div>' in content:
            target = re.search(r'(<div><kbd>Esc</kbd></div>\s*<div[^>]*>.*?</div>)', content)
            if target:
                content = content.replace(target.group(1), target.group(1) + "\n" + HELP_ROW_HTML, 1)
        elif '</table>' in content and 'class="notes-modal"' in content:
            content = content.replace('</table>', f'<tr><td><kbd>+</kbd> / <kbd>-</kbd> / <kbd>0</kbd></td><td data-ru="Масштаб (увеличить / уменьшить / 100%)" data-en="Presentation scale (zoom in / zoom out / reset)">Masshtab (kattalashtirish / kichraytirish / 100%)</td></tr>\n    </table>', 1)

    # 6. JS functions: Scale controller
    if "function setScale" not in content:
        # Insert before Keyboard Navigation or updateSlide
        if "// Keyboard Navigation" in content:
            content = content.replace("// Keyboard Navigation", SCALE_JS + "\n\n// Keyboard Navigation", 1)
        elif "document.addEventListener(\"keydown\"" in content:
            content = content.replace("document.addEventListener(\"keydown\"", SCALE_JS + "\n\ndocument.addEventListener(\"keydown\"", 1)

    # 7. Keydown shortcuts
    if "adjustScale(0.1)" not in content:
        if 'else if (e.key === "Escape")' in content:
            content = content.replace('else if (e.key === "Escape")',
                                      'else if (e.key === "+" || e.key === "=") { adjustScale(0.1); }\n  else if (e.key === "-" || e.key === "_") { adjustScale(-0.1); }\n  else if (e.key === "0") { resetScale(); }\n  else if (e.key === "Escape")',
                                      1)
        elif 'if (e.key === "Escape")' in content:
            content = content.replace('if (e.key === "Escape")',
                                      'if (e.key === "+" || e.key === "=") { adjustScale(0.1); }\n  else if (e.key === "-" || e.key === "_") { adjustScale(-0.1); }\n  else if (e.key === "0") { resetScale(); }\n  else if (e.key === "Escape")',
                                      1)

    # 8. Touch / Swipe & Pinch
    if "initialPinchDist" not in content:
        # Replace existing touch handlers if present, or insert before DOMContentLoaded
        touch_block_re = re.search(r'// Touch / Swipe Navigation[\s\S]*?document\.addEventListener\("touchend"[\s\S]*?\}\);\s*', content)
        if touch_block_re:
            content = content.replace(touch_block_re.group(0), TOUCH_PINCH_JS + "\n\n", 1)
        elif "window.addEventListener(\"DOMContentLoaded\"" in content:
            content = content.replace("window.addEventListener(\"DOMContentLoaded\"", TOUCH_PINCH_JS + "\n\nwindow.addEventListener(\"DOMContentLoaded\"", 1)

    # 9. DOMContentLoaded scale restoration
    if "localStorage.getItem(\"target_scale\")" not in content:
        if "updateSlide();" in content and "window.addEventListener(\"DOMContentLoaded\"" in content:
            content = content.replace("updateSlide();", DOM_INIT_JS + "\n  updateSlide();", 1)
        elif "updateSlideView();" in content and "window.addEventListener(\"DOMContentLoaded\"" in content:
            content = content.replace("updateSlideView();", DOM_INIT_JS + "\n  updateSlideView();", 1)

    if content != orig_content:
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        print("  ✓ Updated with scale controls.")
    else:
        print("  - Already has scale controls.")

    # Validate i18n
    verify_script = os.path.join(REPO_ROOT, "scripts", "verify_i18n.py")
    res = subprocess.run(["python3", verify_script, path], capture_output=True, text=True)
    if res.returncode != 0:
        print(f"  ❌ Verification failed:\n{res.stdout}\n{res.stderr}")
    else:
        print("  ✨ 100% i18n verification passed!")


def main():
    target_files = [
        "classes/5-6-sinf/10-hafta/24-dars-scratch-spraytlar-va-sahnalar/prezentatsiya.html",
        "classes/10-11-sinf/10-hafta/25-dars-ai-agentlar-va-react-tsikli/prezentatsiya.html",
        "classes/7-8-sinf/10-hafta/29-dars-tilemaps-va-2d-labirint/prezentatsiya.html",
        "classes/9-sinf/10-hafta/29-dars-es6-modullar-va-asinxron-chuqurlik/prezentatsiya.html"
    ]
    if len(sys.argv) > 1:
        target_files = sys.argv[1:]

    for p in target_files:
        full_p = os.path.join(REPO_ROOT, p) if not os.path.isabs(p) else p
        if os.path.exists(full_p):
            upgrade_file(full_p)
        else:
            print(f"File not found: {p}")

if __name__ == "__main__":
    main()
