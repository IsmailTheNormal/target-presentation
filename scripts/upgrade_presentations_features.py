#!/usr/bin/env python3
"""
scripts/upgrade_presentations_features.py
Upgrades presentations across all classes with:
1. Asterisked programming and tech terms that open Google Search when tapped/clicked.
2. Standardized 10-point checklist on the last slide (matching 9th grade 27-dars).
3. 100% trilingual in-place compliance.
"""

import re
import sys
import pathlib

TECH_TERMS_CSS = """
/* Tech Terms Search & Asterisk Styling */
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
}
"""

TECH_TERMS_JS = """
// --- Tech Terms Auto-Search & Asterisk Engine ---
var TECH_DICTIONARY = [
  "Cross-Site Scripting", "Cross-Site Request Forgery", "Stored XSS", "Reflected XSS", "DOM-based XSS",
  "SQL Injection", "SQLi", "DOMPurify", "Helmet", "express-validator", "HttpOnly", "SameSite=Strict", "SameSite",
  "XSS", "CSRF", "BOLA", "IDOR", "SSRF", "CVSS", "PTES", "OWASP", "CSP", "HSTS", "X-Frame-Options",
  "X-Content-Type-Options", "JWT", "MVC", "SQLite", "Foreign Key", "INNER JOIN", "REST API", "CRUD",
  "A* Algoritmi", "A* Algorithm", "Dijkstra", "BFS", "Manxetten evristikasi", "Manhattan", "EXIF", "OSINT",
  "Billboard Rule", "2FA", "MFA", "Brute-Force", "SHA-256", "Token Bucket", "HMAC", "Zero Trust", "IAM", "RBAC",
  "Docker", "Terraform", "Vault", "DevSecOps", "CI/CD", "KV Cache", "Self-Attention", "Few-Shot", "Prompt Injection",
  "RAG", "Vector Database", "Embedding", "Sanitization"
];

function applyTechTermLinks() {
  if (typeof document === 'undefined') return;
  var slides = document.querySelectorAll('.slide');
  if (!slides || slides.length === 0) return;

  var terms = TECH_DICTIONARY.slice().sort(function(a, b) { return b.length - a.length; });
  var escapedTerms = terms.map(function(t) {
    return t.replace(/[-/\\\\^$*+?.()|[\\]{}]/g, '\\\\$&');
  });
  var pattern = new RegExp('\\\\b(' + escapedTerms.join('|') + ')\\\\b', 'g');

  slides.forEach(function(slide) {
    var walker = document.createTreeWalker(
      slide,
      NodeFilter.SHOW_TEXT,
      {
        acceptNode: function(node) {
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
        }
      }
    );

    var nodesToReplace = [];
    var currentNode;
    while ((currentNode = walker.nextNode())) {
      nodesToReplace.push(currentNode);
    }

    nodesToReplace.forEach(function(node) {
      var val = node.nodeValue;
      pattern.lastIndex = 0;
      var frag = document.createDocumentFragment();
      var lastIdx = 0;
      var match;
      while ((match = pattern.exec(val)) !== null) {
        if (match.index > lastIdx) {
          frag.appendChild(document.createTextNode(val.substring(lastIdx, match.index)));
        }
        var span = document.createElement('span');
        span.className = 'tech-term';
        span.setAttribute('data-term', match[0]);
        span.setAttribute('role', 'button');
        span.setAttribute('tabindex', '0');

        var lang = (typeof currentLang !== 'undefined' ? currentLang : 'uz');
        var tTitle = (lang === 'ru' ? 'Искать в Google: ' : (lang === 'en' ? 'Search Google: ' : "Google'da qidirish: ")) + match[0];
        span.setAttribute('title', tTitle);

        span.textContent = match[0];
        var star = document.createElement('span');
        star.className = 'term-star';
        star.textContent = '*';
        span.appendChild(star);

        span.addEventListener('click', function(e) {
          e.stopPropagation();
          e.preventDefault();
          var q = this.getAttribute('data-term') || this.textContent.replace(/\\*$/, '').trim();
          var query = q;
          var upper = q.toUpperCase();
          if (['SQL', 'API', 'MVC', 'BFS', 'RAG', 'LLM', '2FA', 'MFA', 'IAM', 'UFW'].indexOf(upper) !== -1) {
            query = q + ' computer science';
          } else if (['XSS', 'CSRF', 'BOLA', 'IDOR', 'SSRF', 'CVSS', 'EXIF', 'HMAC'].indexOf(upper) !== -1) {
            query = q + ' cybersecurity';
          }
          window.open('https://www.google.com/search?q=' + encodeURIComponent(query), '_blank', 'noopener,noreferrer');
        });

        span.addEventListener('keydown', function(e) {
          if (e.key === 'Enter' || e.key === ' ') {
            e.stopPropagation();
            e.preventDefault();
            this.click();
          }
        });

        frag.appendChild(span);
        lastIdx = pattern.lastIndex;
      }
      if (lastIdx < val.length) {
        frag.appendChild(document.createTextNode(val.substring(lastIdx)));
      }
      if (node.parentNode) {
        node.parentNode.replaceChild(frag, node);
      }
    });
  });
}
"""

LAST_SLIDES = {
    "classes/9-sinf/6-hafta/26-dars-mvc-backend-va-relyatsion-baza/prezentatsiya.html": {
        "html": """<section class="slide" data-phase="Yakun|Итог|Wrap-up" data-time="42–45 daq">
  <div class="eyebrow"><span data-ru="ИТОГИ И ДОМАШНЕЕ ЗАДАНИЕ" data-en="WRAP-UP &amp; HOMEWORK">YAKUN VA UY VAZIFASI</span></div>
  <h2><span data-ru="Чек-лист MVC бэкенда и реляционной базы данных" data-en="MVC Backend &amp; Database Architecture Checklist">MVC Backend va Relyatsion Baza Nazorat Ro'yxati</span></h2>
  <p class="lede"><span data-ru="Домашнее задание: Перевести проект интернет-магазина на архитектуру MVC и сдать отчёт по 10-балльному критерию в vazifa.html:" data-en="Homework: Refactor your web store into MVC architecture and complete the 10-point rubric report in vazifa.html:">Uy vazifasi: Do'kon loyihangizni to'liq MVC arxitekturasiga o'tkazing va vazifa.html dagi 10 ballik hisobotni bajaring:</span></p>
  <ul class="big-list" style="margin-top:10px;">
    <li>
      <span class="num">4b</span>
      <div>
        <span class="item-title" data-ru="Архитектура MVC и разделение слоёв (4 балла)" data-en="MVC Architecture &amp; Layer Separation (4 pts)">MVC Arxitekturasi va Qatlamlar Ajratilishi (4 ball)</span>
        <span class="item-desc" data-ru="Контроллеры, маршруты и модели изолированы; логика роутов очищена от прямых SQL-запросов." data-en="Controllers, routes, and models decoupled; routes contain zero direct database access logic.">Controllers, Routes va Models to'liq ajratilgan; marshrutlar ichida to'g'ridan-to'g'ri SQL so'rovlari yo'q.</span>
      </div>
    </li>
    <li>
      <span class="num">3b</span>
      <div>
        <span class="item-title" data-ru="Реляционная схема SQLite и Foreign Keys (3 балла)" data-en="Relational SQLite Schema &amp; Foreign Keys (3 pts)">Relyatsion SQLite Sxemasi va Bog'lanishlar (3 ball)</span>
        <span class="item-desc" data-ru="Таблицы users, products, orders связаны через Foreign Key с каскадным удалением (ON DELETE CASCADE)." data-en="Tables users, products, orders linked via Foreign Keys with ON DELETE CASCADE integrity.">Jadvallar users, products va orders o'zaro Foreign Key bilan bog'langan, ON DELETE CASCADE qo'llangan.</span>
      </div>
    </li>
    <li>
      <span class="num">3b</span>
      <div>
        <span class="item-title" data-ru="Безопасные JOIN запросы и валидация (3 балла)" data-en="Safe JOIN Queries &amp; Input Validation (3 pts)">Xavfsiz JOIN So'rovlari va Validatsiya (3 ball)</span>
        <span class="item-desc" data-ru="Запросы INNER JOIN используют параметризацию (?) против SQL-инъекций, внедрена проверка входных данных." data-en="INNER JOIN queries leverage parameterized placeholders (?) preventing SQLi; strict payload validation added.">INNER JOIN so'rovlarida parametrli (?) o'zgaruvchilar ishlatilgan, xatoliklarda HTTP 400 qaytariladi.</span>
      </div>
    </li>
  </ul>
</section>""",
        "note": {
            "uz": ["Yakun va Uy Vazifasi", "Bugungi darsda monolit spagetti-koddan professional MVC arxitekturasiga o'tdik. O'quvchilarga vazifa.html dagi 4 ta topshiriqni va test.html ni mustaqil bajarishni topshiring.", "10 ballik mezonni tushuntiring, natijalar avtomatik pochtaga yuborilishini eslatib o'ting."],
            "ru": ["Итоги и Домашнее задание", "Сегодня мы перешли от спагетти-кода к профессиональной MVC архитектуре. Поручите ученикам выполнить 4 задачи в vazifa.html и тест test.html.", "Объясните 10-балльный критерий и напомните об автоматической отправке на почту."],
            "en": ["Wrap-up & Homework", "Today we evolved from spaghetti code to professional MVC architecture. Guide students to complete 4 tasks in vazifa.html and the test.html quiz.", "Explain the 10-point rubric and confirm automatic grade submission to teacher email."]
        }
    },
    "classes/10-11-sinf/7-hafta/31-dars-penetration-testing-va-ethical-hacking/prezentatsiya.html": {
        "html": """<section class="slide" data-phase="Yakun|Итог|Wrap-up" data-time="42–45 daq">
  <div class="eyebrow"><span data-ru="ИТОГИ И ДОМАШНЕЕ ЗАДАНИЕ" data-en="WRAP-UP &amp; HOMEWORK">YAKUN VA UY VAZIFASI</span></div>
  <h2><span data-ru="Чек-лист аудита безопасности и этичного хакинга" data-en="Security Audit &amp; Ethical Hacking Checklist">Kiber-Xavfsizlik va Pentest Audit Nazorat Ro'yxati</span></h2>
  <p class="lede"><span data-ru="Домашнее задание: Провести аудит уязвимостей API, устранить BOLA/IDOR и заполнить 10-балльный отчёт в vazifa.html:" data-en="Homework: Conduct a thorough API vulnerability audit, patch BOLA/IDOR flaws, and submit the 10-point report in vazifa.html:">Uy vazifasi: API dagi BOLA/IDOR va sarlavhalar zaifliklarini audit qiling hamda vazifa.html dagi 10 ballik hisobotni to'ldiring:</span></p>
  <ul class="big-list" style="margin-top:10px;">
    <li>
      <span class="num">4b</span>
      <div>
        <span class="item-title" data-ru="Защита от BOLA / IDOR уязвимостей (4 балла)" data-en="BOLA / IDOR Neutralization (4 pts)">BOLA / IDOR Zaifliklarini Bartaraf Etish (4 ball)</span>
        <span class="item-desc" data-ru="В каждом эндпоинте внедрена проверка владельца ресурса (req.user.id === resource.ownerId) с возвратом HTTP 403." data-en="Every endpoint validates ownership (req.user.id === resource.ownerId) returning HTTP 403 Forbidden on tamper.">Har bir marshrutda foydalanuvchi huquqi (req.user.id === resource.ownerId) tekshiriladi, HTTP 403 qaytariladi.</span>
      </div>
    </li>
    <li>
      <span class="num">3b</span>
      <div>
        <span class="item-title" data-ru="Внедрение HTTP Security Headers (3 балла)" data-en="HTTP Security Headers Deployment (3 pts)">HTTP Xavfsizlik Sarlavhalari (Headers) (3 ball)</span>
        <span class="item-desc" data-ru="Настроены 4 критических заголовка: CSP, HSTS, X-Frame-Options и X-Content-Type-Options через Helmet." data-en="Configured 4 critical headers: CSP, HSTS, X-Frame-Options, and X-Content-Type-Options via Helmet middleware.">Helmet orqali 4 ta asosiy sarlavha (CSP, HSTS, X-Frame-Options, X-Content-Type-Options) to'liq sozlangan.</span>
      </div>
    </li>
    <li>
      <span class="num">3b</span>
      <div>
        <span class="item-title" data-ru="Предотвращение SSRF и утечек секретов (3 балла)" data-en="SSRF Defense &amp; Secret Leak Audit (3 pts)">SSRF Himoyasi va Maxfiy Kalitlar Auditi (3 ball)</span>
        <span class="item-desc" data-ru="Заблокированы запросы к метаданным облака (169.254.169.254) и исключена утечка приватных JWT / AWS ключей в коде." data-en="Requests to cloud metadata (169.254.169.254) blocked; source sanitized against hardcoded JWT and AWS credentials.">Cloud metadata (169.254.169.254) so'rovlari bloklangan, ochiq API kalitlari va tokenlar koddan tozalangan.</span>
      </div>
    </li>
  </ul>
</section>""",
        "note": {
            "uz": ["Yakun va Uy Vazifasi", "Etik xakerlik metodologiyasi va zaifliklarni fosh qilishni o'rgandik. vazifa.html dagi 4 ta topshiriqni va test.html sinovini topshirishni talab qiling.", "Oraliq nazorat CTF ga tayyorgarlik uchun ushbu 10 ballik mezon muhim ahamiyatga ega."],
            "ru": ["Итоги и Домашнее задание", "Мы изучили этичный хакинг и поиск уязвимостей. Поручите выполнить 4 задачи в vazifa.html и тест test.html.", "Этот 10-балльный критерий критически важен для подготовки к рубежному CTF."],
            "en": ["Wrap-up & Homework", "We explored ethical hacking methodologies and vulnerability discovery. Direct students to complete vazifa.html and test.html.", "This 10-point rubric is foundational preparation for the upcoming Midterm CTF."]
        }
    },
    "classes/7-8-sinf/7-hafta/29-dars-gps-navigatsiya-va-eng-qisqa-yol/prezentatsiya.html": {
        "html": """<section class="slide" data-phase="Yakun|Итог|Wrap-up" data-time="42–45 daq">
  <div class="eyebrow"><span data-ru="ИТОГИ И ДОМАШНЕЕ ЗАДАНИЕ" data-en="WRAP-UP &amp; HOMEWORK">YAKUN VA UY VAZIFASI</span></div>
  <h2><span data-ru="Чек-лист инженера GPS маршрутизации" data-en="GPS Route Engineer Audit Checklist">GPS Marshrut Muhandisi Nazorat Ro'yxati</span></h2>
  <p class="lede"><span data-ru="Домашнее задание: Построить оптимальный маршрут в Route Studio и заполнить 10-балльный отчёт в vazifa.html:" data-en="Homework: Build an optimal path in Route Studio and submit your 10-point rubric report in vazifa.html:">Uy vazifasi: Route Studio da optimal marshrutni quring va vazifa.html dagi 10 ballik mezon hisobotini topshiring:</span></p>
  <ul class="big-list" style="margin-top:10px;">
    <li>
      <span class="num">4b</span>
      <div>
        <span class="item-title" data-ru="Алгоритм A* и эвристика Манхэттена (4 балла)" data-en="A* Algorithm &amp; Manhattan Heuristic (4 pts)">A* Algoritmi va Manxetten Evristikasi (4 ball)</span>
        <span class="item-desc" data-ru="Реализована формула F = G + H: алгоритм исследует минимальное количество клеток и находит самый короткий путь." data-en="Implemented F = G + H formula: algorithm evaluates minimal tiles and guarantees shortest path to school.">F = G + H formulasi to'g'ri ishlagan: algoritm eng kam kataklarni tekshirib, maktabgacha eng qisqa yo'lni topadi.</span>
      </div>
    </li>
    <li>
      <span class="num">3b</span>
      <div>
        <span class="item-title" data-ru="Учёт весов пробок (Traffic Jam) (3 балла)" data-en="Traffic Jam Cost Accounting (3 pts)">Tirbandlik (Traffic Jam) Narxini Hisoblash (3 ball)</span>
        <span class="item-desc" data-ru="Пробки с весом 4 успешно обойдены по свободному пути, снизив суммарную стоимость поездки." data-en="Traffic jam areas (weight 4) smartly bypassed via clear roads, reducing total route cost.">Og'irligi 4 bo'lgan tirbandliklar oqilona aylanib o'tilgan va yo'lning umumiy narxi minimallashtirilgan.</span>
      </div>
    </li>
    <li>
      <span class="num">3b</span>
      <div>
        <span class="item-title" data-ru="Преодоление лабиринта и экспорт route.json (3 балла)" data-en="Maze Navigation &amp; route.json Export (3 pts)">Labirint Sinovi va route.json Eksporti (3 ball)</span>
        <span class="item-desc" data-ru="Путь построен сквозь узкие городские лабиринты и сохранён в файл route.json без тупиков." data-en="Path successfully traced across dense urban mazes and exported to route.json file with zero dead-ends.">Yo'l murakkab shahar to'siqlari orasidan o'tkazilgan va route.json fayli muvaffaqiyatli yuklab olingan.</span>
      </div>
    </li>
  </ul>
</section>""",
        "note": {
            "uz": ["Yakun va Uy Vazifasi", "GPS va A* qidiruv algoritmi qanday ishlashini o'rgandik. vazifa.html dagi 4 ta topshiriqni va test.html ni topshirishni ayting.", "O'quvchilar route.json faylini eksport qilib topshirishlari mumkin."],
            "ru": ["Итоги и Домашнее задание", "Мы изучили GPS и алгоритм поиска A*. Поручите сдать 4 задачи в vazifa.html и тест test.html.", "Ученики могут экспортировать route.json и прикрепить его к отчету."],
            "en": ["Wrap-up & Homework", "We investigated GPS pathfinding and A* algorithm mechanics. Assign the 4 tasks in vazifa.html and the quiz in test.html.", "Students can export route.json and attach it to their report."]
        }
    },
    "classes/5-6-sinf/7-hafta/21-dars-raqamli-iz-va-maxfiylik/prezentatsiya.html": {
        "html": """<section class="slide" data-phase="Yakun|Итог|Wrap-up" data-time="42–45 daq">
  <div class="eyebrow"><span data-ru="ИТОГИ И ДОМАШНЕЕ ЗАДАНИЕ" data-en="WRAP-UP &amp; HOMEWORK">YAKUN VA UY VAZIFASI</span></div>
  <h2><span data-ru="Чек-лист стража цифровой приватности" data-en="Digital Privacy Guardian Checklist">Raqamli Maxfiylik Qalqoni Nazorat Ro'yxati</span></h2>
  <p class="lede"><span data-ru="Домашнее задание: Проверить свои фотографии и аккаунты по 10-балльному критерию в vazifa.html:" data-en="Homework: Audit your personal photos and accounts based on the 10-point rubric in vazifa.html:">Uy vazifasi: Shaxsiy fotosuratlaringiz va profillaringizni vazifa.html dagi 10 ballik mezon bo'yicha tekshiring:</span></p>
  <ul class="big-list" style="margin-top:10px;">
    <li>
      <span class="num">4b</span>
      <div>
        <span class="item-title" data-ru="Очистка EXIF GPS метаданных из фото (4 балла)" data-en="Strip Hidden EXIF GPS Metadata (4 pts)">Fotosuratlardan EXIF GPS Manzilini O'chirish (4 ball)</span>
        <span class="item-desc" data-ru="Скрытые координаты дома и модель телефона найдены и очищены с помощью инструмента Strip EXIF." data-en="Hidden GPS home coordinates and device models audited and scrubbed using the Strip EXIF utility.">Fotosuratlardagi yashirin uy koordinatalari fosh qilingan va Strip EXIF orqali tozalangan.</span>
      </div>
    </li>
    <li>
      <span class="num">3b</span>
      <div>
        <span class="item-title" data-ru="Соблюдение Правила Большого Экрана (3 балла)" data-en="Billboard Rule Compliance (3 pts)">Katta Ekran Qoidasiga (Billboard Rule) Amal Qilish (3 ball)</span>
        <span class="item-desc" data-ru="Все личные данные проверены: в интернет не выкладываются билеты, геометки, пароли и документы." data-en="Zero sensitive info disclosed: tickets, geolocations, passwords, and IDs strictly excluded from social feeds.">Internetga chiqarishdan oldin samolyot chiptasi, joylashuv, hujjatlar va shaxsiy sirlar tekshirilgan.</span>
      </div>
    </li>
    <li>
      <span class="num">3b</span>
      <div>
        <span class="item-title" data-ru="Построение 100% Щита Приватности (3 балла)" data-en="Building a 100% Privacy Shield (3 pts)">100% Maxfiylik Qalqonini Yaratish (3 ball)</span>
        <span class="item-desc" data-ru="Профиль переведён в приватный режим, незнакомцы удалены, включена двухфакторная защита (2FA)." data-en="Account switched to Private mode, unknown contacts cleared, Two-Factor Authentication (2FA) active.">Akkaunt yopiq (Private) rejimga o'tkazilgan, begona so'rovlar bekor qilingan, 2FA yoqilgan.</span>
      </div>
    </li>
  </ul>
</section>""",
        "note": {
            "uz": ["Yakun va Uy Vazifasi", "Raqamli iz va shaxsiy fotosuratlar xavfsizligini o'rgandik. vazifa.html dagi 4 ta topshiriqni va test.html ni to'ldirishni so'rang.", "Katta Ekran Qoidasi va fotosuratlarni tozalashni uyda ota-onalari bilan ham sinab ko'rishni tavsiya qiling."],
            "ru": ["Итоги и Домашнее задание", "Мы изучили цифровой след и безопасность фотографий. Поручите выполнить 4 задачи в vazifa.html и тест test.html.", "Рекомендуйте протестировать Правило Большого Экрана дома вместе с родителями."],
            "en": ["Wrap-up & Homework", "We investigated digital footprints and photo metadata privacy. Direct students to complete vazifa.html and test.html.", "Encourage students to practice the Billboard Rule at home with family."]
        }
    },
    "classes/9-sinf/8-hafta/28-dars-fullstack-xavfsiz-servis-oraliq-nazorat/prezentatsiya.html": {
        "html": """<section class="slide" data-phase="Yakun|Итог|Wrap-up" data-time="42–45 daq">
  <div class="eyebrow"><span data-ru="РУБРИКА РУБЕЖНОГО КОНТРОЛЯ" data-en="MIDTERM ASSESSMENT RUBRIC">ORALIQ NAZORAT MEZONI</span></div>
  <h2><span data-ru="10-Балльный критерий рубежного экзамена" data-en="10-Point Midterm Capstone Rubric">10 Ballik Oraliq Nazorat Nazorat Ro'yxati</span></h2>
  <p class="lede"><span data-ru="Рубежный контроль: Выполните финальный аудит и зафиксируйте баллы в vazifa.html:" data-en="Midterm Exam: Complete the final full-stack security audit and record points in vazifa.html:">Oraliq nazorat: Full-Stack do'koningizni CTF sinovlaridan o'tkazing va vazifa.html dagi hisobotni topshiring:</span></p>
  <ul class="big-list" style="margin-top:10px;">
    <li>
      <span class="num">4b</span>
      <div>
        <span class="item-title" data-ru="Архитектура MVC и целостность базы данных (4 балла)" data-en="MVC Architecture &amp; Database Integrity (4 pts)">MVC Arxitekturasi va Relyatsion Baza (4 ball)</span>
        <span class="item-desc" data-ru="В Express проекте слои Model, View и Controller изолированы, связь users-products-orders работает без сбоев." data-en="Clean separation of Model, View, and Controller layers; SQLite relational integrity with zero leaks.">Express serverida Model, View va Controller qatlamlari ajratilgan, reliesion bog'lanishlar to'g'ri qurilgan.</span>
      </div>
    </li>
    <li>
      <span class="num">3b</span>
      <div>
        <span class="item-title" data-ru="Комплексная защита от XSS и CSRF (3 балла)" data-en="Full-Spectrum XSS &amp; CSRF Defense (3 pts)">XSS va CSRF Kompleks Himoyasi (3 ball)</span>
        <span class="item-desc" data-ru="DOMPurify и express-validator активны, сессионные куки защищены HttpOnly и SameSite=Strict." data-en="DOMPurify and express-validator active, cookies fortified with HttpOnly and SameSite=Strict.">DOMPurify va express-validator filtrlari sozlangan, kukilar HttpOnly va SameSite=Strict bilan himoyalangan.</span>
      </div>
    </li>
    <li>
      <span class="num">3b</span>
      <div>
        <span class="item-title" data-ru="Успешный захват CTF флагов (3 балла)" data-en="Successful CTF Flag Captures (3 pts)">CTF Bayroqlarini Qo'lga Kiritish (3 ball)</span>
        <span class="item-desc" data-ru="Найдены флаги FLAG_SQLI и FLAG_XSS_DOM, составлен официальный отчёт по устранению уязвимостей." data-en="Security audit successfully discovers and documents both FLAG_SQLI and FLAG_XSS_DOM flags.">Zaifliklarni fosh etuvchi FLAG_SQLI va FLAG_XSS_DOM bayroqlari topilgan va hisobot topshirilgan.</span>
      </div>
    </li>
  </ul>
</section>""",
        "note": {
            "uz": ["Oraliq Nazorat Yakuni", "1-Chorak oraliq nazorati yakunlandi. O'quvchilardan vazifa.html hisobotini va test.html natijalarini to'plash.", "Barcha natijalar o'qituvchi elektron pochtasiga avtomatik yuborilganini tekshiring."],
            "ru": ["Итоги Рубежного Контроля", "Рубежный контроль 1-й четверти завершен. Соберите отчеты vazifa.html и результаты test.html.", "Проверьте поступление оценок на электронную почту учителя."],
            "en": ["Midterm Exam Wrap-up", "Quarter 1 Midterm Exam completed. Collect vazifa.html reports and test.html quiz submissions.", "Verify automated grade submissions in the teacher email inbox."]
        }
    },
    "classes/7-8-sinf/8-hafta/30-dars-sport-simulyatori-oraliq-nazorat/prezentatsiya.html": {
        "html": """<section class="slide" data-phase="Yakun|Итог|Wrap-up" data-time="42–45 daq">
  <div class="eyebrow"><span data-ru="РУБРИКА РУБЕЖНОГО КОНТРОЛЯ" data-en="MIDTERM ASSESSMENT RUBRIC">ORALIQ NAZORAT MEZONI</span></div>
  <h2><span data-ru="10-Балльный критерий рубежного экзамена" data-en="10-Point Midterm Capstone Rubric">10 Ballik Oraliq Nazorat Nazorat Ro'yxati</span></h2>
  <p class="lede"><span data-ru="Рубежный контроль: Завершите финальный проект игры и зафиксируйте баллы в vazifa.html:" data-en="Midterm Exam: Complete the final sports simulation project and submit points in vazifa.html:">Oraliq nazorat: Karta, kimyo va o'yin dvigatelini yakunlang hamda vazifa.html dagi hisobotni topshiring:</span></p>
  <ul class="big-list" style="margin-top:10px;">
    <li>
      <span class="num">4b</span>
      <div>
        <span class="item-title" data-ru="Генерация карточек и расчет OVR (4 балла)" data-en="Card Studio &amp; OVR Calculation (4 pts)">Karta Studiyasi va OVR Formulalari (4 ball)</span>
        <span class="item-desc" data-ru="Расчёт точного OVR по формуле весов, загрузка фото через File API и чистый рендеринг карточки." data-en="Accurate weighted OVR calculation, dynamic photo upload via File API, and clean card UI rendering.">Vaznli koeffitsiyentlar orqali aniq OVR hisobi, File API fotosurat yuklash va yuqori sifatli vizual render.</span>
      </div>
    </li>
    <li>
      <span class="num">3b</span>
      <div>
        <span class="item-title" data-ru="Граф сыгранности и тактика команды (3 балла)" data-en="Chemistry Graph &amp; Tactical Lineup (3 pts)">Kimyo Graflari va Taktik Sinergiya (3 ball)</span>
        <span class="item-desc" data-ru="Связи нации, клуба и лиги (33 очка сыгранности) рассчитаны и визуализированы в составе 11 игроков." data-en="11-player tactical lineup calculates 33-point chemistry graph with nation, club, and league links.">11 talik tarkibda klub, liga va millat aloqalari (33 ballik kimyo) to'g'ri hisoblangan va chizilgan.</span>
      </div>
    </li>
    <li>
      <span class="num">3b</span>
      <div>
        <span class="item-title" data-ru="Игровой движок (FSM) и физика матча (3 балла)" data-en="Match Engine (FSM) &amp; Physics Simulation (3 pts)">Match Engine (FSM) va O'yin Fizikasi (3 ball)</span>
        <span class="item-desc" data-ru="90-минутный цикл событий, расчёт вероятности xG и контроль 5% налога на аукционе (Coin Sink)." data-en="90-minute stochastic event chain, expected goals (xG), and 5% auction tax (Coin Sink) economy.">90 daqiqalik stoxastik hodisalar zanjiri, xG ehtimolligi va auksiondagi 5% soliq (Coin Sink) nazorati.</span>
      </div>
    </li>
  </ul>
</section>""",
        "note": {
            "uz": ["Oraliq Nazorat Yakuni", "Sport simulyatori va o'yin fizikasi moduli yakunlandi. O'quvchilardan vazifa.html va test.html topshiriqlarini qabul qiling.", "O'yin loyihasi va auksion mexanizmini to'liq baholang."],
            "ru": ["Итоги Рубежного Контроля", "Модуль спортивного симулятора завершен. Примите работы vazifa.html и результаты теста test.html.", "Оцените игровой движок и экономику аукциона."],
            "en": ["Midterm Exam Wrap-up", "Sports simulation and physics module completed. Collect assignments from vazifa.html and test.html.", "Grade the game engine and auction market mechanics."]
        }
    },
    "classes/5-6-sinf/8-hafta/22-dars-kiber-qalqon-oraliq-nazorat/prezentatsiya.html": {
        "html": """<section class="slide" data-phase="Yakun|Итог|Wrap-up" data-time="42–45 daq">
  <div class="eyebrow"><span data-ru="РУБРИКА РУБЕЖНОГО КОНТРОЛЯ" data-en="MIDTERM ASSESSMENT RUBRIC">ORALIQ NAZORAT MEZONI</span></div>
  <h2><span data-ru="10-Балльный критерий рубежного экзамена" data-en="10-Point Midterm Capstone Rubric">10 Ballik Oraliq Nazorat Nazorat Ro'yxati</span></h2>
  <p class="lede"><span data-ru="Рубежный контроль: Пройдите финальные испытания и зафиксируйте баллы в vazifa.html:" data-en="Midterm Exam: Complete the final cybersecurity challenges and record points in vazifa.html:">Oraliq nazorat: Kiber-qalqon sinovlaridan o'ting va vazifa.html dagi hisobotni topshiring:</span></p>
  <ul class="big-list" style="margin-top:10px;">
    <li>
      <span class="num">4b</span>
      <div>
        <span class="item-title" data-ru="Стойкие пароли и распознавание фишинга (4 балла)" data-en="Strong Passwords &amp; Phishing Detection (4 pts)">Kuchli Parollar va Fishingni Fosh Qilish (4 ball)</span>
        <span class="item-desc" data-ru="Пароли 14+ знаков, распознавание поддельных доменов в ссылках и включение двухфакторной защиты (2FA)." data-en="14+ character passwords, spotting domain spoofing in URLs, and two-factor authentication.">14+ belgili entropiyali parollar, soxta havolalarni domen bo'yicha aniqlash va 2FA himoyasi.</span>
      </div>
    </li>
    <li>
      <span class="num">3b</span>
      <div>
        <span class="item-title" data-ru="Защита от троянов и «Бесплатных робуксов» (3 балла)" data-en="Defense Against Trojans &amp; Free Robux Traps (3 pts)">Troyanlar va Tekin Mod Qopqonlari Mudofaasi (3 ball)</span>
        <span class="item-desc" data-ru="Разоблачение двойных расширений (.png.exe) и ловушек с читами, отказ от подозрительных загрузок." data-en="Exposing double extensions (.png.exe) and bait schemes, avoiding untrusted downloads.">Ikki qavatli kengaytmalar (.png.exe) va aldovlarni fosh qilish, shubhali fayllarni ochmaslik.</span>
      </div>
    </li>
    <li>
      <span class="num">3b</span>
      <div>
        <span class="item-title" data-ru="Цифровой след и Правило Большого Экрана (3 балла)" data-en="Digital Footprint &amp; Billboard Rule (3 pts)">Raqamli Iz va Katta Ekran Qoidasi (3 ball)</span>
        <span class="item-desc" data-ru="Очистка EXIF GPS координат из фото и построение 100% личного защитного щита приватности." data-en="Scrubbing EXIF GPS coordinates and establishing a comprehensive 100% personal privacy defense.">EXIF GPS koordinatalarini tozalash va shaxsiy maxfiylik qalqonini 100% ga yetkazish.</span>
      </div>
    </li>
  </ul>
</section>""",
        "note": {
            "uz": ["Oraliq Nazorat Yakuni", "Kiber-qalqon 1-chorak yakuniy sinovi. O'quvchilardan vazifa.html topshiriqlarini va test.html javoblarini oling.", "Barcha 10 ballik mezonlarni tekshirib, yakuniy baholarni qo'ying."],
            "ru": ["Итоги Рубежного Контроля", "Финальный рубежный контроль 1-й четверти. Примите отчеты vazifa.html и ответы теста test.html.", "Проверьте все 10-балльные критерии и выставьте итоговые оценки."],
            "en": ["Midterm Exam Wrap-up", "Quarter 1 Cyber Guardian midterm finale. Collect vazifa.html reports and test.html test submissions.", "Assess all 10-point criteria and finalize scores."]
        }
    }
}

TARGET_PRESENTATIONS = [
    "classes/9-sinf/6-hafta/26-dars-mvc-backend-va-relyatsion-baza/prezentatsiya.html",
    "classes/9-sinf/7-hafta/27-dars-veb-xavfsizlik-xss-va-csrf/prezentatsiya.html",
    "classes/9-sinf/8-hafta/28-dars-fullstack-xavfsiz-servis-oraliq-nazorat/prezentatsiya.html",
    "classes/10-11-sinf/7-hafta/31-dars-penetration-testing-va-ethical-hacking/prezentatsiya.html",
    "classes/10-11-sinf/8-hafta/32-dars-korporativ-himoya-va-ctf/prezentatsiya.html",
    "classes/7-8-sinf/7-hafta/29-dars-gps-navigatsiya-va-eng-qisqa-yol/prezentatsiya.html",
    "classes/7-8-sinf/8-hafta/30-dars-sport-simulyatori-oraliq-nazorat/prezentatsiya.html",
    "classes/5-6-sinf/7-hafta/21-dars-raqamli-iz-va-maxfiylik/prezentatsiya.html",
    "classes/5-6-sinf/8-hafta/22-dars-kiber-qalqon-oraliq-nazorat/prezentatsiya.html",
]

def upgrade_presentation(filepath_str):
    p = pathlib.Path(filepath_str)
    if not p.is_file():
        print(f"Skipping missing: {filepath_str}")
        return False

    content = p.read_text(encoding="utf-8")

    # 1. Inject or update CSS for tech-term
    if ".tech-term" not in content:
        # insert before </style>
        content = content.replace("</style>", TECH_TERMS_CSS + "\n</style>", 1)
        print(f"  + Added .tech-term CSS to {filepath_str}")

    # 2. Inject or update JS for applyTechTermLinks
    if "applyTechTermLinks" not in content:
        # Insert TECH_TERMS_JS before closing </script>
        content = content.replace("</script>", TECH_TERMS_JS + "\n</script>", 1)
        print(f"  + Added TECH_TERMS_JS to {filepath_str}")

    # Ensure setLang calls applyTechTermLinks()
    if "applyTechTermLinks();" not in content:
        # inside function setLang(lang) { ... updateSlideView(); }
        content = re.sub(
            r'(updateSlideView\(\);\s*\})',
            r'updateSlideView();\n  applyTechTermLinks();\n}',
            content,
            count=1
        )
        print(f"  + Hooked applyTechTermLinks into setLang in {filepath_str}")

    # Ensure DOMContentLoaded calls applyTechTermLinks()
    if "applyTechTermLinks();" in content and "updateSlideView();\n  applyTechTermLinks();\n});" not in content:
        content = re.sub(
            r'(updateSlideView\(\);\s*\}\);)',
            r'updateSlideView();\n  applyTechTermLinks();\n});',
            content,
            count=1
        )

    # 3. Upgrade Last Slide if defined in LAST_SLIDES
    if filepath_str in LAST_SLIDES:
        ls_info = LAST_SLIDES[filepath_str]
        new_slide_html = ls_info["html"]

        # Replace the last <section class="slide" ...> ... </section>
        # Find all slides
        slides = list(re.finditer(r'<section class=\"slide[^\"]*\".*?</section>', content, re.DOTALL))
        if slides:
            last_slide_match = slides[-1]
            content = content[:last_slide_match.start()] + new_slide_html + content[last_slide_match.end():]
            print(f"  + Replaced last slide with 10-point rubric in {filepath_str}")

        # Update NOTES in JS for the last slide
        # NOTES is formatted as: var NOTES = { uz: [...], ru: [...], en: [...] };
        notes_match = re.search(r'var NOTES\s*=\s*(\{.*?\});', content, re.DOTALL)
        if notes_match:
            try:
                import json
                notes_str = notes_match.group(1)
                # python json parse or regex replace of last element in uz, ru, en
                for lang_code in ["uz", "ru", "en"]:
                    # find the list for this lang
                    l_match = re.search(r'["\']?' + lang_code + r'["\']?\s*:\s*\[(.*?)\]\s*[,}]', notes_str, re.DOTALL)
                    if l_match:
                        # find all triplets inside: [ ... ]
                        triplets = re.findall(r'\[\s*"([^"]*)"\s*,\s*"([^"]*)"\s*,\s*"([^"]*)"\s*\]', l_match.group(1))
                        if triplets:
                            # replace last triplet with ls_info["note"][lang_code]
                            new_trip = ls_info["note"][lang_code]
                            # format replacement string
                            escaped_trip = f'["{new_trip[0]}", "{new_trip[1]}", "{new_trip[2]}"]'
                            # replace the last triplet in the full content
                            pattern_last_trip = re.findall(r'\[\s*"[^"]*"\s*,\s*"[^"]*"\s*,\s*"[^"]*"\s*\]', l_match.group(1))
                            if pattern_last_trip:
                                old_last_trip = pattern_last_trip[-1]
                                l_block = l_match.group(1)
                                new_l_block = l_block[:l_block.rfind(old_last_trip)] + escaped_trip + l_block[l_block.rfind(old_last_trip) + len(old_last_trip):]
                                notes_str = notes_str[:l_match.start(1)] + new_l_block + notes_str[l_match.end(1):]
                # put notes_str back
                content = content[:notes_match.start(1)] + notes_str + content[notes_match.end(1):]
                print(f"  + Updated NOTES for slide 12 in {filepath_str}")
            except Exception as ex:
                print(f"  ! Note update warning: {ex}")

    p.write_text(content, encoding="utf-8")
    print(f"✓ Successfully upgraded {filepath_str}")
    return True

def main():
    print("Starting Presentation Feature Upgrade...")
    for path_str in TARGET_PRESENTATIONS:
        upgrade_presentation(path_str)

if __name__ == "__main__":
    main()
