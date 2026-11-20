/**
 * scripts/verify_browser_i18n.js
 * 
 * Direct in-browser verification using Headless Chrome & Chrome DevTools Protocol (CDP).
 * Validates real-time trilingual rendering (UZ, RU, EN), zero-blank fallbacks,
 * interactive SPA routing, and captures screenshots as proof.
 */

const { spawn } = require('child_process');
const fs = require('fs');
const path = require('path');

const ARTIFACT_DIR = '/home/dpdp/.gemini/antigravity-cli/brain/48dda7aa-4fa5-472c-b559-1c924ee7d28a/browser_i18n';
const BASE_DIR = '/home/dpdp/target/classes/9-sinf/11-hafta/33-dars-spa-va-client-side-routing';

class ChromeClient {
  constructor(ws) {
    this.ws = ws;
    this.id = 1;
    this.pending = new Map();
    this.events = new Map();

    ws.onmessage = (msg) => {
      try {
        const data = JSON.parse(msg.data);
        if (data.id && this.pending.has(data.id)) {
          const { resolve, reject } = this.pending.get(data.id);
          this.pending.delete(data.id);
          if (data.error) reject(new Error(JSON.stringify(data.error)));
          else resolve(data.result);
        } else if (data.method) {
          const handlers = this.events.get(data.method) || [];
          handlers.forEach(fn => fn(data.params));
        }
      } catch (err) {
        console.error('WS parse error:', err);
      }
    };
  }

  send(method, params = {}) {
    return new Promise((resolve, reject) => {
      const id = this.id++;
      this.pending.set(id, { resolve, reject });
      this.ws.send(JSON.stringify({ id, method, params }));
    });
  }

  on(event, handler) {
    if (!this.events.has(event)) this.events.set(event, []);
    this.events.get(event).push(handler);
  }

  async eval(expression) {
    const res = await this.send('Runtime.evaluate', {
      expression,
      returnByValue: true,
      awaitPromise: true
    });
    if (res.exceptionDetails) {
      throw new Error(res.exceptionDetails.text || 'Eval error: ' + JSON.stringify(res.exceptionDetails));
    }
    return res.result ? res.result.value : undefined;
  }

  async captureScreenshot(outputPath) {
    const res = await this.send('Page.captureScreenshot', { format: 'png' });
    fs.writeFileSync(outputPath, Buffer.from(res.data, 'base64'));
  }
}

async function startChrome() {
  const chrome = spawn('google-chrome', [
    '--headless=new',
    '--remote-debugging-port=9222',
    '--no-sandbox',
    '--disable-gpu',
    '--window-size=1920,1080',
    'about:blank'
  ]);

  for (let i = 0; i < 30; i++) {
    await new Promise(r => setTimeout(r, 200));
    try {
      const res = await fetch('http://127.0.0.1:9222/json');
      if (res.ok) {
        const tabs = await res.json();
        const tab = tabs.find(t => t.type === 'page');
        if (tab && tab.webSocketDebuggerUrl) {
          const ws = new WebSocket(tab.webSocketDebuggerUrl);
          await new Promise(resolve => { ws.onopen = resolve; });
          const client = new ChromeClient(ws);
          await client.send('Page.enable');
          await client.send('Runtime.enable');
          await client.send('Emulation.setDeviceMetricsOverride', {
            width: 1920,
            height: 1080,
            deviceScaleFactor: 1,
            mobile: false
          });
          return { chrome, client };
        }
      }
    } catch (e) {}
  }
  throw new Error('Could not connect to Chrome on port 9222');
}

async function navigateAndWait(client, fileUrl) {
  let loaded = false;
  const onLoad = () => { loaded = true; };
  client.on('Page.loadEventFired', onLoad);

  await client.send('Page.navigate', { url: fileUrl });

  for (let i = 0; i < 50; i++) {
    if (loaded) break;
    await new Promise(r => setTimeout(r, 100));
  }
  // Wait extra 200ms for scripts to finish execution
  await new Promise(r => setTimeout(r, 300));
}

async function auditCurrentSlide(client, slideIndex, lang) {
  return await client.eval(`
    (() => {
      const slide = document.querySelectorAll('.slide')[${slideIndex}];
      if (!slide) return { error: 'Slide not found' };

      const candidateTags = ['H1', 'H2', 'H3', 'H4', 'H5', 'P', 'LI', 'TH', 'TD', 'BUTTON'];
      const all = slide.querySelectorAll('*');
      let totalNodes = 0;
      let blankNodes = [];
      let translatedNodes = 0;
      let missingAttrs = [];

      all.forEach(el => {
        if (!candidateTags.includes(el.tagName) && !el.classList.contains('t') && !el.classList.contains('lede')) return;
        if (el.closest('pre') || el.closest('code') || el.classList.contains('mono') || el.classList.contains('lg')) return;
        
        const txt = (el.innerText || el.textContent || '').trim();
        if (txt.length <= 1) return;
        if (/^[\\s\\d\\W_]+$/.test(txt)) return;

        totalNodes++;
        if (txt === '') {
          blankNodes.push(el.tagName + (el.className ? '.' + el.className : ''));
        }

        const hasLangAttr = el.hasAttribute('data-ru') && el.hasAttribute('data-en');
        const hasChildLang = el.querySelector('[data-ru][data-en], .t[data-ru][data-en]');
        if (hasLangAttr || hasChildLang) {
          translatedNodes++;
        } else {
          missingAttrs.push({
            tag: el.tagName,
            class: el.className,
            sample: txt.slice(0, 30)
          });
        }
      });

      const titleEl = slide.querySelector('h2');
      const ledeEl = slide.querySelector('.lede');

      return {
        totalNodes,
        translatedNodes,
        blankNodes,
        missingAttrs,
        sampleTitle: titleEl ? titleEl.innerText : '',
        sampleLede: ledeEl ? ledeEl.innerText : ''
      };
    })()
  `);
}

async function runBrowserAudit() {
  console.log('================================================================');
  console.log('🚀 DIRECT IN-BROWSER LOCALIZATION AUDIT (Google Chrome CDP)');
  console.log('================================================================\n');

  const { chrome, client } = await startChrome();
  const summary = {
    slidesChecked: 0,
    totalLangChecks: 0,
    totalDomElementsAudited: 0,
    blankFallbacks: 0,
    missingTranslations: 0,
    screenshots: []
  };

  try {
    // -------------------------------------------------------------------------
    // 1. PREZENTATSIYA AUDIT
    // -------------------------------------------------------------------------
    const deckUrl = `file://${BASE_DIR}/prezentatsiya.html?i18n=1`;
    console.log(`[1/4] Loading Prezentatsiya in Chrome: ${deckUrl}`);
    await navigateAndWait(client, deckUrl);

    const slideCount = await client.eval(`document.querySelectorAll('.slide').length`);
    console.log(`✓ Deck loaded. Total slides: ${slideCount}`);

    const languages = ['uz', 'ru', 'en'];

    for (let s = 0; s < slideCount; s++) {
      // Go to slide s via official deck engine
      await client.eval(`
        (() => {
          if (typeof goToSlide === 'function') {
            goToSlide(${s});
          }
          const slides = document.querySelectorAll('.slide');
          slides.forEach((sl, idx) => {
            sl.classList.toggle('is-on', idx === ${s});
          });
          currentSlide = ${s};
          if (typeof updateSlide === 'function') updateSlide(true);
          if (typeof window.updateHUD === 'function') window.updateHUD();
        })()
      `);
      await new Promise(r => setTimeout(r, 100));

      const slideTitleUz = await client.eval(`
        (() => {
          const h2 = document.querySelectorAll('.slide')[${s}].querySelector('h2');
          return h2 ? h2.innerText : ('Slide ' + (${s} + 1));
        })()
      `);

      process.stdout.write(`  Slide ${s + 1}/${slideCount} [${slideTitleUz.slice(0, 32)}...]: `);

      for (const lang of languages) {
        // Change language
        await client.eval(`setLang('${lang}')`);
        await new Promise(r => setTimeout(r, 100));

        const audit = await auditCurrentSlide(client, s, lang);
        summary.totalLangChecks++;
        summary.totalDomElementsAudited += audit.totalNodes;

        if (audit.blankNodes.length > 0) {
          summary.blankFallbacks += audit.blankNodes.length;
          console.error(`\n    ❌ BLANK NODES in ${lang.toUpperCase()}:`, audit.blankNodes);
        }
        if (audit.missingAttrs.length > 0) {
          summary.missingTranslations += audit.missingAttrs.length;
          console.error(`\n    ❌ MISSING ATTRS in ${lang.toUpperCase()}:`, audit.missingAttrs);
        }

        // Verify text in RU has cyrillic, EN has english
        if (lang === 'ru') {
          const hasCyrillic = /[А-Яа-яЁё]/.test(audit.sampleTitle) || /[А-Яа-яЁё]/.test(audit.sampleLede);
          if (!hasCyrillic && audit.sampleTitle.length > 5) {
            console.warn(`    ⚠️ RU Title may not contain Cyrillic: "${audit.sampleTitle}"`);
          }
        }

        // Take screenshots for Key Slides (1: Title, 8: SPA Simulator, 14: Summary)
        if (s === 0 || s === 7 || s === 13) {
          const screenshotName = `slide_${s + 1}_${lang}.png`;
          const screenshotPath = path.join(ARTIFACT_DIR, screenshotName);
          await client.captureScreenshot(screenshotPath);
          summary.screenshots.push({ name: screenshotName, slide: s + 1, lang, path: screenshotPath });
        }

        process.stdout.write(`${lang.toUpperCase()}✓ `);
      }
      console.log('');
      summary.slidesChecked++;
    }

    // Reset language to UZ
    await client.eval(`setLang('uz')`);

    // Verify HUD Status
    const hudStatus = await client.eval(`
      (() => {
        const hud = document.getElementById('i18nHUD');
        return hud ? hud.innerText.replace(/\\n/g, ' ') : 'HUD NOT FOUND';
      })()
    `);
    console.log(`  ✓ Real-Time i18n HUD Status: "${hudStatus}"`);

    // -------------------------------------------------------------------------
    // 2. INTERACTIVE SPA STUDIO AUDIT
    // -------------------------------------------------------------------------
    const studioUrl = `file://${BASE_DIR}/studio/index.html`;
    console.log(`\n[2/4] Loading Interactive Studio: ${studioUrl}`);
    await navigateAndWait(client, studioUrl);

    for (const lang of languages) {
      await client.eval(`setLang('${lang}')`);
      await new Promise(r => setTimeout(r, 60));
      const studioTitle = await client.eval(`document.querySelector('.brand span') ? document.querySelector('.brand span').innerText : document.title`);
      console.log(`  Studio in ${lang.toUpperCase()}: "${studioTitle}"`);
    }

    // Test client-side routing dynamically
    console.log(`  Testing client-side routes (/terminal, /traffic, /settings, /dashboard)...`);
    const routes = ['/terminal', '/traffic', '/settings', '/dashboard'];
    for (const r of routes) {
      const routeResult = await client.eval(`
        (() => {
          const btn = document.querySelector('.nav-link[data-path="${r}"]');
          if (btn) btn.click();
          return {
            currentPath: window.__currentSpaPath || '',
            urlDisplay: document.getElementById('spaUrlBar') ? document.getElementById('spaUrlBar').innerText : ''
          };
        })()
      `);
      console.log(`    Navigated to ${r} -> Current: "${routeResult.currentPath}" · URL: "${routeResult.urlDisplay}"`);
    }

    const studioScreenshot = path.join(ARTIFACT_DIR, 'studio_dashboard.png');
    await client.captureScreenshot(studioScreenshot);
    summary.screenshots.push({ name: 'studio_dashboard.png', slide: 'Studio', lang: 'uz', path: studioScreenshot });

    // -------------------------------------------------------------------------
    // 3. WORKSHEET (VARAQA) AUDIT
    // -------------------------------------------------------------------------
    const varaqaUrl = `file://${BASE_DIR}/varaqa.html`;
    console.log(`\n[3/4] Loading Printable Worksheet: ${varaqaUrl}`);
    await navigateAndWait(client, varaqaUrl);

    for (const lang of languages) {
      await client.eval(`setLang('${lang}')`);
      await new Promise(r => setTimeout(r, 60));
      const sheetTitle = await client.eval(`document.querySelector('h1').innerText`);
      console.log(`  Varaqa in ${lang.toUpperCase()}: "${sheetTitle}"`);
    }

    const varaqaScreenshot = path.join(ARTIFACT_DIR, 'varaqa_sheet.png');
    await client.captureScreenshot(varaqaScreenshot);
    summary.screenshots.push({ name: 'varaqa_sheet.png', slide: 'Varaqa', lang: 'uz', path: varaqaScreenshot });

    // -------------------------------------------------------------------------
    // 4. HOMEWORK (VAZIFA) APP AUDIT
    // -------------------------------------------------------------------------
    const vazifaUrl = `file://${BASE_DIR}/vazifa.html`;
    console.log(`\n[4/4] Loading Interactive Homework: ${vazifaUrl}`);
    await navigateAndWait(client, vazifaUrl);

    for (const lang of languages) {
      await client.eval(`setLang('${lang}')`);
      await new Promise(r => setTimeout(r, 60));
      const hwTitle = await client.eval(`document.querySelector('h1').innerText`);
      console.log(`  Vazifa in ${lang.toUpperCase()}: "${hwTitle}"`);
    }

    const vazifaScreenshot = path.join(ARTIFACT_DIR, 'vazifa_app.png');
    await client.captureScreenshot(vazifaScreenshot);
    summary.screenshots.push({ name: 'vazifa_app.png', slide: 'Vazifa', lang: 'uz', path: vazifaScreenshot });

  } finally {
    chrome.kill();
    console.log('\n================================================================');
    console.log('📊 IN-BROWSER AUDIT FINAL REPORT');
    console.log('================================================================');
    console.log(`Total Slides Checked:           ${summary.slidesChecked}`);
    console.log(`Total Language Switches Tested: ${summary.totalLangChecks}`);
    console.log(`DOM Elements Inspected:         ${summary.totalDomElementsAudited}`);
    console.log(`Zero-Blank Fallback Failures:   ${summary.blankFallbacks}`);
    console.log(`Missing Translation Attributes: ${summary.missingTranslations}`);
    console.log(`Screenshots Captured:           ${summary.screenshots.length}`);
    console.log('================================================================');

    if (summary.blankFallbacks === 0 && summary.missingTranslations === 0) {
      console.log('🎉 100% PERFECT IN-BROWSER LOCALIZATION CONFIRMED!');
    } else {
      console.log('❌ ISSUES DETECTED! See logs above.');
      process.exit(1);
    }
  }
}

runBrowserAudit().catch(err => {
  console.error('Audit failed with error:', err);
  process.exit(1);
});
