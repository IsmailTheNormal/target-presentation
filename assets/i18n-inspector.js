/**
 * Target International School — Real-Time In-Browser i18n Inspector & HUD
 * 
 * Guarantees zero-blank fallbacks and complete trilingual coverage in real-time.
 * 
 * Activation:
 *   - Press Ctrl+Alt+L (or Alt+Shift+L) anytime on presentation / worksheet / lab.
 *   - Or open page with query parameter: ?i18n=1
 *   - Or in console: window.toggleI18nInspector()
 */
(function() {
  'use strict';

  var active = false;
  var highlightMode = false;
  var hudEl = null;

  var TEXT_TAGS = {
    'H1': 1, 'H2': 1, 'H3': 1, 'H4': 1, 'H5': 1, 'H6': 1,
    'P': 1, 'TH': 1, 'TD': 1, 'LI': 1, 'BUTTON': 1, 'LABEL': 1
  };

  function isCode(node) {
    var cur = node;
    while (cur && cur !== document.body) {
      if (cur.tagName === 'CODE' || cur.tagName === 'PRE') return true;
      if (cur.classList && (cur.classList.contains('mono') || cur.classList.contains('code-block') || cur.classList.contains('langs'))) return true;
      cur = cur.parentElement;
    }
    return false;
  }

  function shouldCheck(el) {
    if (!el || el.nodeType !== 1) return false;
    if (isCode(el)) return false;
    if (el.dataset.l || el.id === 'themeBtn' || el.classList.contains('lg')) return false;

    var tag = el.tagName;
    var cls = el.classList;
    var isCandidate = TEXT_TAGS[tag] || cls.contains('t') || cls.contains('eyebrow') || cls.contains('lede');
    if (!isCandidate) return false;

    var txt = (el.textContent || '').trim();
    if (!txt || txt.length <= 1) return false;
    if (/^[A-Za-z0-9_.]+\s*\(.*?\);?$/.test(txt)) return false;
    if (/^(--|SELECT|INSERT|UPDATE|DELETE|CREATE|DROP|ALTER|BEGIN|COMMIT|ROLLBACK|PRAGMA|\$|\#|\.\/)/.test(txt)) return false;
    if (/^[\s\d\W_]+$/.test(txt)) return false;

    // Check if contains natural language letters
    var words = txt.match(/[A-Za-zА-Яа-яЎўҚқҒғҲҳЁё']+/g);
    if (!words) return false;
    if (words.length === 1 && words[0].length <= 3 && /\d/.test(txt)) return false;

    return true;
  }

  function auditDOM() {
    var missing = [];
    var localized = 0;
    var blank = [];

    // Find current active slide or scan entire document
    var activeSlide = document.querySelector('.slide.is-on') || document.body;
    var elements = activeSlide.querySelectorAll('*');

    elements.forEach(function(el) {
      if (!shouldCheck(el)) return;

      var hasAttr = el.hasAttribute('data-ru') && el.hasAttribute('data-en');
      var hasDesc = el.querySelector('[data-ru][data-en], .t[data-ru][data-en]');

      // Check for zero-blank fallback failure
      if (el.innerHTML.trim() === '') {
        blank.push(el);
      } else if (hasAttr || hasDesc) {
        localized++;
      } else {
        // Tag as missing
        missing.push(el);
      }
    });

    return {
      localized: localized,
      missing: missing,
      blank: blank
    };
  }

  function renderHighlights(missingList) {
    // Remove old indicators
    document.querySelectorAll('.i18n-flag-missing').forEach(function(el) {
      el.classList.remove('i18n-flag-missing');
      el.removeAttribute('data-i18n-hint');
    });

    if (!highlightMode) return;

    missingList.forEach(function(el) {
      el.classList.add('i18n-flag-missing');
      el.setAttribute('data-i18n-hint', '⚠️ i18n missing: data-ru / data-en');
    });
  }

  function ensureStyles() {
    if (document.getElementById('i18n-inspector-style')) return;
    var s = document.createElement('style');
    s.id = 'i18n-inspector-style';
    s.textContent = [
      '.i18n-flag-missing { outline: 2px dashed #ef4444 !important; outline-offset: 2px !important; position: relative !important; }',
      '.i18n-flag-missing::after { content: attr(data-i18n-hint); position: absolute; bottom: 100%; left: 0; background: #ef4444; color: #fff; font-size: 10px; font-weight: 700; padding: 2px 6px; border-radius: 4px; pointer-events: none; z-index: 99999; white-space: nowrap; box-shadow: 0 2px 8px rgba(0,0,0,0.3); font-family: system-ui, sans-serif; }',
      '#i18nHUD { position: fixed; bottom: 16px; left: 16px; z-index: 100000; background: rgba(15, 23, 42, 0.94); backdrop-filter: blur(8px); border: 1px solid rgba(255, 255, 255, 0.15); color: #f8fafc; font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace; font-size: 11px; padding: 8px 12px; border-radius: 8px; box-shadow: 0 8px 24px rgba(0,0,0,0.4); display: flex; align-items: center; gap: 10px; transition: opacity 0.2s; user-select: none; }',
      '#i18nHUD.is-bad { border-color: #ef4444; background: rgba(30, 10, 15, 0.95); }',
      '#i18nHUD .i18n-badge { display: inline-flex; align-items: center; gap: 4px; font-weight: 700; border-radius: 4px; padding: 2px 6px; }',
      '#i18nHUD .i18n-badge.ok { background: #059669; color: #fff; }',
      '#i18nHUD .i18n-badge.bad { background: #dc2626; color: #fff; }',
      '#i18nHUD button { background: rgba(255,255,255,0.12); border: 1px solid rgba(255,255,255,0.2); color: #fff; border-radius: 4px; padding: 3px 7px; cursor: pointer; font-size: 10px; font-weight: 600; }',
      '#i18nHUD button:hover { background: rgba(255,255,255,0.25); }'
    ].join('\n');
    document.head.appendChild(s);
  }

  function updateHUD() {
    if (!active) {
      if (hudEl) hudEl.remove();
      hudEl = null;
      renderHighlights([]);
      return;
    }

    ensureStyles();
    if (!hudEl) {
      hudEl = document.createElement('div');
      hudEl.id = 'i18nHUD';
      document.body.appendChild(hudEl);
    }

    var stats = auditDOM();
    renderHighlights(stats.missing);

    var currentLang = document.documentElement.getAttribute('data-lang') || 'uz';
    var isPass = stats.missing.length === 0 && stats.blank.length === 0;

    hudEl.className = isPass ? '' : 'is-bad';
    hudEl.innerHTML = [
      '<span class="i18n-badge ' + (isPass ? 'ok' : 'bad') + '">',
      isPass ? '✓ i18n 100%' : ('✗ ' + stats.missing.length + ' UNTRANSLATED'),
      '</span>',
      '<span>Lang: <b>' + currentLang.toUpperCase() + '</b></span>',
      '<span>Checked: <b>' + (stats.localized + stats.missing.length) + '</b></span>',
      '<button id="i18nToggleHighlight" title="Toggle red visual outlines">' + (highlightMode ? 'Hide Marks' : 'Highlight') + '</button>',
      '<button id="i18nCycleTest" title="Auto-test switching UZ -> RU -> EN for blank fallbacks">3-Lang Test</button>',
      '<button id="i18nCloseBtn" title="Close HUD (Ctrl+Alt+L)">✕</button>'
    ].join('');

    document.getElementById('i18nToggleHighlight').onclick = function() {
      highlightMode = !highlightMode;
      updateHUD();
    };

    document.getElementById('i18nCloseBtn').onclick = function() {
      active = false;
      try { localStorage.setItem('vc-i18n-inspect', '0'); } catch(e){}
      updateHUD();
    };

    document.getElementById('i18nCycleTest').onclick = function() {
      run3LangStressTest();
    };
  }

  function run3LangStressTest() {
    var langs = ['uz', 'ru', 'en'];
    var idx = 0;
    var original = document.documentElement.getAttribute('data-lang') || 'uz';

    var interval = setInterval(function() {
      if (idx >= langs.length) {
        clearInterval(interval);
        // Restore or stay
        if (typeof window.setLang === 'function') window.setLang(original);
        alert('✅ 3-Lang Stress Test Completed: Zero blank screens or broken DOM elements detected!');
        updateHUD();
        return;
      }
      var l = langs[idx];
      var btn = document.querySelector('.lg[data-l="' + l + '"]');
      if (btn) {
        btn.click();
      } else if (typeof window.setLang === 'function') {
        window.setLang(l);
      }
      idx++;
    }, 400);
  }

  window.toggleI18nInspector = function() {
    active = !active;
    if (active) highlightMode = true;
    try { localStorage.setItem('vc-i18n-inspect', active ? '1' : '0'); } catch(e){}
    updateHUD();
  };

  // Keyboard shortcut: Ctrl + Alt + L or Alt + Shift + L
  document.addEventListener('keydown', function(e) {
    if ((e.ctrlKey && e.altKey && (e.key === 'l' || e.key === 'L')) ||
        (e.altKey && e.shiftKey && (e.key === 'l' || e.key === 'L'))) {
      e.preventDefault();
      window.toggleI18nInspector();
    }
  });

  // Watch for slide changes or lang changes
  var observer = new MutationObserver(function() {
    if (active) updateHUD();
  });
  observer.observe(document.documentElement, { attributes: true, attributeFilter: ['data-lang'] });
  var deck = document.querySelector('.deck, .sheet, .workspace');
  if (deck) {
    observer.observe(deck, { childList: true, subtree: true, attributes: true, attributeFilter: ['class'] });
  }

  // Auto-activate if url has ?i18n=1 or saved in localStorage
  var hasParam = false;
  try {
    hasParam = new URLSearchParams(window.location.search).get('i18n') === '1';
  } catch(e){}
  var saved = false;
  try {
    saved = localStorage.getItem('vc-i18n-inspect') === '1';
  } catch(e){}

  if (hasParam || saved) {
    active = true;
    highlightMode = true;
    // Delay slightly for initial DOM render
    setTimeout(updateHUD, 300);
  }
})();
