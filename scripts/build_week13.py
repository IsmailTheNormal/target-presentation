#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
scripts/build_week13.py — 13-hafta (3 kohorta) tezkor kompilyatori.
9-sinf WebSockets darsi: scripts/build_9_w13_l37.py orqali alohida yaratiladi.
"""

import os
import sys
import html
from importlib.util import spec_from_file_location, module_from_spec

ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ROOT)

from build_lesson import compile_lesson  # noqa: E402


def tri(*args):
    if len(args) == 3:
        uz, ru, en = args
    elif len(args) == 2:
        uz, en = args
        ru = en
    else:
        uz = ru = en = args[0]
    return {"uz": uz, "ru": ru, "en": en}


def e(s):
    return html.escape(s, quote=True)


def card(tag, title, text, color=None):
    t = tri(*tag) if isinstance(tag, tuple) else tag
    ti = tri(*title) if isinstance(title, tuple) else title
    tx = tri(*text) if isinstance(text, tuple) else text
    style = f' style="border-left:4px solid {color};"' if color else ""
    return (f'<div class="box"{style}><div class="tag" data-ru="{e(t["ru"])}" data-en="{e(t["en"])}">{e(t["uz"])}</div>'
            f'<h3 data-ru="{e(ti["ru"])}" data-en="{e(ti["en"])}">{e(ti["uz"])}</h3>'
            f'<p data-ru="{e(tx["ru"])}" data-en="{e(tx["en"])}">{e(tx["uz"])}</p></div>')


def cards(*items):
    return '<div class="cards-grid" style="margin-top:16px;">' + "".join(items) + "</div>"


def steps(items):
    return ('<div class="box" style="margin-top:16px;"><h3 data-ru="Amaliy bosqichlar" data-en="Lab steps">Amaliy bosqichlar</h3>'
            '<ol style="margin-left:20px;line-height:1.8;">'
            + "".join(f'<li data-ru="{e(ru)}" data-en="{e(en)}">{e(uz)}</li>' for uz, ru, en in items)
            + "</ol></div>")


def code(src):
    return f'<pre class="code-block" style="margin-top:14px;"><code>{e(src)}</code></pre>'


def slide(phase, eyebrow, title, lede, body):
    eb = tri(*eyebrow) if isinstance(eyebrow, tuple) else eyebrow
    ti = tri(*title) if isinstance(title, tuple) else title
    ld = tri(*lede) if isinstance(lede, tuple) else lede
    return {
        "phase": phase,
        "eyebrow": eb,
        "title": ti,
        "lede": ld,
        "body": body,
    }


def quiz(q, opts, reveal):
    return {
        "question": tri(*q),
        "options": [
            {**tri(*o), "correct": ok} for o, ok in opts
        ],
        "reveal": tri(*reveal),
    }


def homework(t1, t2, t3):
    return {"tier1": tri(*t1), "tier2": tri(*t2), "tier3": tri(*t3)}


# ============================================================
# 10–11-SINF · 33-DARS · AVTONOM KOD AGENTLARI (80 min)
# ============================================================
SPEC_1011 = {
    "cohort": "10-11-sinf",
    "week": 13,
    "lesson_no": 33,
    "title": tri("Avtonom Kod Yozuvchi Agentlar: Cursor Rules, CLI va TDD Tsikli",
                 "Автономные агенты по написанию кода: Cursor Rules, CLI и цикл TDD",
                 "Autonomous Coding Agents: Cursor Rules, CLI and the TDD Loop"),
    "lede": tri("Avtocomplete’dan avtonom agentga o‘tish: reja tuzish, faylni tahrirlash, testni o‘zi ishga tushirish va natijani o‘zi tekshirish.",
                "Переход от автодополнения к автономному агенту: планирование, редактирование файлов, запуск тестов и самопроверка результата.",
                "From autocomplete to an autonomous agent: planning, editing files, running tests and verifying its own result."),
    "duration": 80,
    "slug": "33-dars-avtonom-kod-agentlari-va-tdd",
    "hw_review": {
        "pitfall": {
            "title": tri("Xato: «ishlaydigan ko‘rinadi», lekin test yo‘q", "Ошибка: «выглядит рабочим», но тестов нет", "Pitfall: looks right but has no tests"),
            "desc": tri("O‘tgan darsda AI yozgan kod manual ko‘rikdan o‘tgan, ammo hech qanday avtomat test himoya qilmagan.",
                        "В прошлом уроке код от AI прошёл только ручную проверку, без автоматических тестов.",
                        "Last lesson's AI-generated code passed only manual review, with no automated test guard."),
            "code": "// ❌ Test yo'q -> regressiya aniqlanmaydi\nconst total = items.reduce((a,b)=>a+b.price, 0);",
        },
        "solution": {
            "title": tri("Oltin yechim: test birinchi, kod keyin", "Золотой стандарт: сначала тест, затем код", "Golden standard: test first, code second"),
            "desc": tri("Har bir o‘zgartirish oldidan xatti-harakat testi yoziladi; agent faqat yashil testlar bilan tugaydi.",
                        "Перед каждым изменением пишется поведенческий тест; агент завершается только при зелёных тестах.",
                        "A behaviour test is written before every change; the agent finishes only with green tests."),
            "code": "// ✅ Test -> kod -> qayta test\ntest('bo'sh savat -> 0', () => assert.equal(total([]), 0));",
        },
        "blitz": tri("Nega AI yozgan kodni ko‘zdan ko‘rish yetarli emas?", "Почему визуальной проверки кода от AI недостаточно?", "Why is eyeballing AI-generated code not enough?"),
        "bridge": tri("Agentning o‘zi test yozib, o‘z kodini tuzatsa, siz faqat natijani tasdiqlaysiz — bugun shuni quramiz.",
                      "Если агент сам пишет тесты и чинит свой код, вы лишь подтверждаете результат — сегодня строим это.",
                      "When the agent writes tests and fixes its own code, you only approve the result — that is today's build."),
    },
    "slides": [
        slide("Muammo|Проблема|Problem",
              ("AGENTIK SAKRASH · 1-QADAM", "AGENTIC LEAP · STEP 1"),
              ("Avtocomplete emas — avtonom ijro", "Not autocomplete — autonomous execution", "Not autocomplete — autonomous execution"),
              ("AI sizga 10 qator taklif qiladi; agent esa butun vazifani oxirigacha bajaradi.",
               "AI предлагает 10 строк; агент доводит всю задачу до конца.",
               "AI suggests ten lines; an agent drives the whole task to completion."),
              cards(
                  card(("AVTOCOMPLETE", "AVTOCOMPLETE", "AUTOCOMPLETE"), ("Faqat taklif", "Лишь подсказka", "Suggestion only"),
                       ("Ishchi doirasi: bitta fayl, bitta funksiya. Inson hamma qadamni bosadi.",
                        "Область: один файл, одна функция. Человек нажимает каждый шаг.",
                        "Scope: one file, one function. The human drives every step."), "var(--accent)"),
                  card(("AGENT", "АГЕНТ", "AGENT"), ("To‘liq tsikl", "Полный цикл", "Full loop"),
                       ("Fayllarni o‘qiydi, reja tuzadi, tahrir qiladi, test ishga tushiradi, xatoni o‘zi tuzatadi.",
                        "Читает файлы, строит план, редактирует, запускает тесты и исправляет ошибки.",
                        "Reads files, plans, edits, runs tests and repairs errors on its own."), "var(--green)"))),
        slide("Arxitektura|Архитектура|Architecture",
              ("REACT TSIKLI", "REACT LOOP"),
              ("Thought → Action → Observation", "Thought → Action → Observation", "Thought → Action → Observation"),
              ("Agent har iteratsiyada kuzatadi, harakat qiladi va natijani qayta o‘qiydi.",
               "На каждой итерации агент наблюдает, действует и перечитывает результат.",
               "Each iteration: observe, act, then re-read the resulting state."),
              steps([
                  ("Kod bazasini o‘qish (Read)", "Чтение кодовой базы (Read)", "Read the codebase"),
                  ("Reja va fayllar ro‘yxati (Plan)", "План и список файлов (Plan)", "Plan and file list"),
                  ("Tahrir / buyruq (Action)", "Правка / команда (Action)", "Edit or run command"),
                  ("Test va diff natijasi (Observation)", "Тест и diff (Observation)", "Test and diff result"),
                  ("Xato bo‘lsa yana 2-qadamga qaytish", "При ошибке возврат к шагу 2", "On failure, loop back to step 2"),
              ]) + code("while (!testsGreen && iterations < MAX) {\n  const obs = await read(state);\n  const action = await plan(obs);\n  await apply(action);\n}")),
        slide("Kontekst|Контекст|Context",
              ("DOIMIY KO‘RSATMALAR", "PERSISTENT INSTRUCTIONS"),
              ("AGENTS.md / Cursor Rules — agentning konstitutsiyasi", "AGENTS.md / Cursor Rules — the agent's constitution", "AGENTS.md / Cursor Rules — the agent's constitution"),
              ("Har bir suhbatda qayta yoziladigan qoidalar emas, repository ichida yashaydigan doimiy shartlar.",
               "Правила не в каждом диалоге, а постоянно в репозитории.",
               "Rules live in the repository, not in every single chat."),
              cards(
                  card(("QOIDALAR", "ПРАВИЛА", "RULES"), ("Nima qilish kerak", "Что делать", "What to do"),
                       ("Texnologiya stacki, papka tuzilmasi, test buyrug‘i, til va format talablari.",
                        "Стек, структура папок, команда тестов, требования к языку и формату.",
                        "Stack, folder layout, test command, language and formatting rules.")),
                  card(("CHEKLAR", "ОГРАНИЧЕНИЯ", "GUARDRAILS"), ("Nima qilmaslik kerak", "Чего не делать", "What not to do"),
                       ("Maxfiy kalitlarga tegma, testlarni o‘chirma, lockfile’ni qo‘lda tahrirlama.",
                        "Не трогать секреты, не удалять тесты, не редактировать lockfile вручную.",
                        "Never touch secrets, never delete tests, never hand-edit the lockfile.")))),
        slide("Vositalar|Инструменты|Tooling",
              ("CLI AGENTLAR", "CLI AGENTS"),
              ("OpenCode, Claude Code, Copilot Workspace", "OpenCode, Claude Code, Copilot Workspace", "OpenCode, Claude Code, Copilot Workspace"),
              ("Terminal ichida ishlovchi agentlar terminalning kuchini ham, xavfini ham meros qilib oladi.",
               "Агенты в терминале наследуют и силу, и риск терминала.",
               "Terminal agents inherit both the power and the risk of the shell."),
              cards(
                  card(("OPENCODE", "OPENCODE", "OPENCODE"), ("Ochiq arxitektura", "Открытая архитектура", "Open architecture"),
                       ("Plugin va model almashtirish;ReAct tsikli va aniq ruxsatlar bilan ishlaydi.",
                        "Плагины и смена моделей; цикл ReAct с явными разрешениями.",
                        "Plugins, swappable models; ReAct loop with explicit permissions.")),
                  card(("CLAUDE CODE", "CLAUDE CODE", "CLAUDE CODE"), ("Kod bazasini tushunish", "Понимание кодовой базы", "Codebase understanding"),
                       ("Butun reponi indekslab, ko‘p faylni bir operatsiyada o‘zgartiradi.",
                        "Индексирует весь репозиторий и меняет много файлов за одну операцию.",
                        "Indexes the whole repo and changes many files in one operation.")),
                  card(("COPILOT", "COPILOT", "COPILOT"), ("Workspace rejasi", "Режим Workspace", "Workspace mode"),
                       ("Topshiriqdan boshlab PR gacha: reja, tahrir, izoh va tasdiqlash.",
                        "От задачи до PR: план, правки, комментарии и подтверждение.",
                        "From issue to PR: plan, edits, comments and approval.")))),
        slide("TDD|TDD|TDD",
              ("QIZIL · YASHIL · REFAKTORING", "RED · GREEN · REFACTOR"),
              ("Test birinchi yoziladi — agent keyin", "Сначала тест — агент потом", "Test first — the agent comes second"),
              ("Qizil test agentga aniq maqsad beradi; yashildan keyingi refaktoring regressiyani ushlaydi.",
               "Красный тест даёт агенту точную цель; рефакторинг после зелёного ловит регрессии.",
               "A red test gives the agent a precise goal; refactoring after green catches regressions."),
              steps([
                  ("Qizil: xatti-harakat testi yoziladi va o‘tmaydi", "Красный: тест написан и падает", "Red: write a failing behaviour test"),
                  ("Yashil: agent eng oddiy kodni yozadi", "Зелёный: агент пишет простейший код", "Green: agent writes the simplest code"),
                  ("Refaktor: structura tozalanadi, test yashil qoladi", "Рефакторинг: чистим структуру, тест зелёный", "Refactor: clean structure, keep tests green"),
                  ("Hisobot: diff + o‘tgan testlar soni", "Отчёт: diff + число пройденных тестов", "Report: diff + passed test count"),
              ]) + code("// 1) QIZIL\ntest('not found -> null', () => assert.equal(find([]), null));\n// 2) YASHIL\nconst find = xs => xs[0] ?? null;\n// 3) REFAKTOR — test o'zgarmaydi")),
        slide("Xavfsizlik|Безопасность|Security",
              ("HIMOYA QATLAMLARI", "GUARDRAIL LAYERS"),
              ("Agentga ishonch emas — cheklar", "Доверие агенту — это проверки", "Trust the agent through checks, not faith"),
              ("Agent xato qilishi mumkin; tizim uni to‘xtata olishi shart.",
               "Агент может ошибиться; система должна уметь его остановить.",
               "An agent can fail; the system must be able to stop it."),
              cards(
                  card(("SANDBOX", "ПЕСОЧНИЦА", "SANDBOX"), ("Izolyatsiya", "Изоляция", "Isolation"),
                       ("Docker / Xvfb ichida ishga tushirish, tarmoq va fayl yo‘llari cheklangan.",
                        "Запуск в Docker/Xvfb с ограниченными сетью и путями.",
                        "Run inside Docker/Xvfb with restricted network and file paths."), "var(--accent)"),
                  card(("LIMIT", "ЛИМИТ", "LIMIT"), ("Iteratsiya cheki", "Лимит итераций", "Iteration cap"),
                       ("Maksimal qadamlar va vaxt; tsiklga tushib qolishdan himoya.",
                        "Максимум шагов и времени; защита от зацикливания.",
                        "Max steps and time protect against infinite loops.")),
                  card(("HITL", "HITL", "HITL"), ("Inson tasdiqi", "Подтверждение человека", "Human approval"),
                       ("Diff ko‘rib chiqilmasdan commit yo‘q; xavfli buyruqlar oldidan to‘xtash.",
                        "Без просмотра diff нет коммита; остановка перед опасными командами.",
                        "No commit before diff review; stop before dangerous commands.")))),
        slide("Xatolar|Ошибки|Failure modes",
              ("REAL KESLAR", "REAL FAILURES"),
              ("Agentning 3 klassik xatosi", "Три классические ошибки агента", "Three classic agent failures"),
              ("Bu xatolar tasodif emas — ular optimallashtirish maqsadining yon ta’siri.",
               "Это не случайность, а побочный эффект целевой оптимизации.",
               "These are not accidents but side effects of goal optimisation."),
              steps([
                  ("Testlarni o‘chirish: agent «yashil» ko‘rsatish uchun testlani del qiladi",
                   "Удаление тестов: агент удаляет тесты ради «зелёного» результата",
                   "Deleting tests: the agent removes tests to make things look green"),
                  ("Reward hacking: faqat metrikani yaxshilaydi, mahsulotni emas",
                   "Reward hacking: улучшает метрику, а не продукт",
                   "Reward hacking: improves the metric, not the product"),
                  ("Context drift: 20 qadam dan keyin dastlabki talabni unutadi",
                   "Context drift: после 20 шагов забывает исходную задачу",
                   "Context drift: after 20 steps it forgets the original requirement"),
                  ("Ye РIM: test hashlarini himoyalash + MAX_ITER + yakuniy inson ko‘rigi",
                   "Решение: защита хэшей тестов + MAX_ITER + финальная проверка",
                   "Fix: protect test hashes + MAX_ITER + final human review"),
              ])),
        slide("Evals|Evals|Evals",
              ("O‘LCHASH", "MEASUREMENT"),
              ("Agent yaxshi ishlayotganini qanday bilamiz?", "Как понять, что агент работает хорошо?", "How do we know the agent works well?"),
              ("Sezgi emas — eval’lar, trace va pul qiymati.", "Не интуиция, а eval’ы, trace и стоимость.", "Not intuition — evals, traces and cost."),
              cards(
                  card(("PASS@K", "PASS@K", "PASS@K"), ("K marta sinab", "K попыток", "K attempts"),
                       ("Bir vazifa K marta bajarilib, necha marta to‘g‘ri chiqqani o‘lchanadi.",
                        "Измеряется, сколько из K попыток дали верный результат.",
                        "Measures how many of K attempts produce a correct result.")),
                  card(("TRACE", "TRACE", "TRACE"), ("Qadamlar jurnali", "Журнал шагов", "Step log"),
                       ("Har bir Thought/Action/Observation vaqt va token bilan yozib boriladi.",
                        "Каждый шаг логируется с временем и токенами.",
                        "Every step is logged with timing and token counts.")),
                  card(("COST", "COST", "COST"), ("Iqtisodiyot", "Экономика", "Economics"),
                       ("Vazifa uchun ketgan token narxi inson vaqti bilan taqqoslanadi.",
                        "Стоимость токенов задачи сравнивается со временем человека.",
                        "Task token cost is compared against human time.")))),
        slide("Arena|Арена|Arena",
              ("KATTA AMALIY LABORATORIYA", "BIG HANDS-ON LAB"),
              ("O‘z TDD agentingni qur", "Собери своего TDD-агента", "Build your own TDD agent"),
              ("Simulyatorda buzilgan funksiyani top, test yoz, agentga tuzatishni buyur va hisobot ol.",
               "В симуляторе найди сломанную функцию, напиши тест, вели агенту починить и получи отчёт.",
               "In the simulator, find the broken function, write a test, tell the agent to fix it and get a report."),
              steps([
                  ("Muammoli funksiyani tanlash va qizil test yozish", "Выбрать функцию и написать красный тест", "Pick a broken function and write a red test"),
                  ("Agent tsiklini 3 iteratsiyaga cheklash", "Ограничить цикл агента 3 итерациями", "Limit the agent loop to 3 iterations"),
                  ("Diff va test natijasini tekshirish", "Проверить diff и результат тестов", "Review the diff and test result"),
                  ("Juftlikda:; agent xatosini topish (peer review)", "В паре найти ошибку агента (peer review)", "Peer-review: find the agent's mistake"),
              ])),
    ],
    "quiz": quiz(
        ("Agent «barcha testlar yashil» deb hisobot berdi, lekin siz testlar sonining kamayganini ko‘rdingiz. Nima qilasiz?",
         "Агент сообщил, что все тесты зелёные, но вы заметили уменьшение их числа. Что делаете?",
         "The agent reports all tests green, but you notice the test count dropped. What do you do?"),
        [
            (("Yashil natijani qabul qilish", "Принять зелёный результат", "Accept the green result"), False),
            (("Test hashlarini solishtirib, o‘chirilgan testlarni tiklash va diffni rad etish",
              "Сравнить хэши тестов, восстановить удалённые и отклонить diff",
              "Compare test hashes, restore deleted tests and reject the diff"), True),
            (("Testlar sonini oxirgi marta ko‘rish", "В последний раз посмотреть число тестов", "Just check the count once more"), False),
        ],
        ("To‘g‘ri: testlarning o‘chirilishi — reward hacking. Oltin qoida: test fayllari hash bilan himoyalanadi va diff inson tomonidan tasdiqlanadi.",
         "Верно: удаление тестов — reward hacking. Тесты защищаются хэшами, diff подтверждается человеком.",
         "Correct: deleting tests is reward hacking. Protect test files with hashes and require human diff approval."),
    ),
    "practice": {
        "title": tri("TDD Agent Laboratoriyasi", "Лаборатория TDD-агента", "TDD Agent Lab"),
        "task": tri("Buzilgan funksiyani tuzatuvchi agent tsiklini yarating va natijani hisobot qiling.",
                    "Создайте цикл агента, исправляющего сломанную функцию, и подготовьте отчёт.",
                    "Build an agent loop that fixes the broken function and report the result."),
        "steps": [
            "Qizil test yozish (1 daqiqa) / Красный тест / Red test",
            "Agentga 3 iteratsiya ruxsat berish / 3 итерации / 3 iterations",
            "Diffni ko‘rib, xavfli o‘zgarishlarni rad etish / Проверить diff / Reject risky edits",
            "Natijani JSON hisobot qilib eksport qilish / Экспорт отчёта / Export report",
        ],
    },
    "homework": homework(
        ("Darsdagi ReAct tsiklini 5 bosqichda xatolarsiz takrorlash.",
         "Воспроизвести цикл ReAct из 5 шагов без ошибок.",
         "Reproduce the 5-step ReAct loop without errors."),
        ("O‘z loyihangizga AGENTS.md yozib, agentga 3 ta aniq qoida va 2 ta taqiq berish.",
         "Написать AGENTS.md для своего проекта с 3 правилами и 2 запретами.",
         "Write an AGENTS.md for your project with 3 rules and 2 prohibitions."),
        ("Test fayllarining hash himoyasini va MAX_ITER chekini qo‘shib, reward hackingni to‘sish.",
         "Добавить хэш-защиту тестов и MAX_ITER против reward hacking.",
         "Add test-file hash protection and MAX_ITER to block reward hacking."),
    ),
}


# ============================================================
# 7–8-SINF · 36-DARS · O'Q FIZIKASI (80 min)
# ============================================================
SPEC_78 = {
    "cohort": "7-8-sinf",
    "week": 13,
    "lesson_no": 36,
    "title": tri("Qurollar va O'qlar Fizikasi: Trigonometriya va Traektoriya",
                 "Физика оружия и снарядов: тригонометрия и траектория",
                 "Weapon and Projectile Physics: Trigonometry and Trajectory"),
    "lede": tri("Sichqoncha qaerda bo‘lsa, o‘q shunga qarab uchadi — buning matematikasi atan2, cos va sin.",
                "Пуля летит туда, где курсор: математика — atan2, cos и sin.",
                "Bullets fly toward the cursor: the math is atan2, cos and sin."),
    "duration": 80,
    "slug": "36-dars-oq-fizikasi-va-trigonometriya",
    "hw_review": {
        "pitfall": {
            "title": tri("Xato: o‘q nishonga tegmaydi", "Ошибка: снаряд не попадает", "Pitfall: the bullet misses"),
            "desc": tri("O‘tgan darsdagi dushman harakatida koordinatalar to‘g‘ri, lekin tezlik faqat X bo‘yicha berilgan edi.",
                        "В прошлом уроке координаты были верны, но скорость задавалась только по X.",
                        "Last lesson had correct coordinates, but velocity was only along X."),
            "code": "// ❌ Faqat gorizontal harakat\nbullet.x += speed;",
        },
        "solution": {
            "title": tri("Oltin yechim: vektorni ikki o‘qqa ajrat", "Золотой стандарт: разложить вектор на оси", "Golden standard: split the vector into axes"),
            "desc": tri("Burchak orqali tezlikni X va Y komponentlariga ajratib, ikkala o‘q bo‘yicha harakatlantirish.",
                        "Через угол разложить скорость на компоненты X и Y и двигать по обеим осям.",
                        "Use the angle to split velocity into X and Y components and move along both axes."),
            "code": "// ✅ To'g'ri traektoriya\nbullet.x += Math.cos(a) * speed;\nbullet.y += Math.sin(a) * speed;",
        },
        "blitz": tri("Math.atan2(dy, dx) qaysi qiymatni qaytaradi?", "Что возвращает Math.atan2(dy, dx)?", "What does Math.atan2(dy, dx) return?"),
        "bridge": tri("Dushmenga qarab burilish uchun aynan shu burchak kerak — bugun otishma tizimini quraymiz.",
                      "Этот угол нужен, чтобы повернуться к врагу — сегодня строим систему стрельбы.",
                      "That exact angle is needed to face the enemy — today we build the shooting system."),
    },
    "slides": [
        slide("Muammo|Проблема|Problem",
              ("NIShON OLISH", "НАВЕДЕНИЕ"),
              ("Nishonga qarab o‘q uzish muammosi", "Проблема наведения снаряда", "The aiming problem"),
              ("O‘q faqat o‘ngga uchadi, sichqoncha esa yuqorida — nima etishmayapti?",
               "Пуля летит только вправо, а курсор сверху — чего не хватает?",
               "The bullet flies right while the cursor is above — what's missing?"),
              cards(
                  card(("ESKI", "СТАРОЕ", "OLD"), ("Faqat X tezlik", "Скорость только по X", "X-only velocity"),
                       ("x += speed; y o‘zgarmaydi -> o‘q nishon pastidan o‘tib ketadi.",
                        "x += speed; y не меняется -> снаряд пролетает ниже цели.",
                        "x += speed; y never changes -> the shot passes below the target."), "var(--accent)"),
                  card(("YANGI", "НОВОЕ", "NEW"), ("Burchak + vektor", "Угол + вектор", "Angle + vector"),
                       ("Oldin burchak hisoblanadi, keyin tezlik ikki o‘qqa bo‘linadi.",
                        "Сначала вычисляется угол, затем скорость делится на оси.",
                        "First compute the angle, then split velocity across both axes."), "var(--green)"))),
        slide("Trigonometriya|Тригонометрия|Trigonometry",
              ("1-QADAM · BURCHAK", "STEP 1 · ANGLE"),
              ("atan2 — to‘g‘ri kvadrantni topadi", "atan2 finds the correct quadrant", "atan2 finds the correct quadrant"),
              ("Oddiy atan(dy/dx) Chap va yuqori kvadrantlarda xato qiladi; atan2 barcha 360° ni qamrab oladi.",
               "Обычный atan(dy/dx) ошибается в левом и верхнем квадрантах; atan2 покрывает все 360°.",
               "Plain atan(dy/dx) fails in left and upper quadrants; atan2 covers all 360°."),
              code("const dx = target.x - player.x;\nconst dy = target.y - player.y;\nconst angle = Math.atan2(dy, dx); // radial\n// E'tibor: canvas da Y pastga qarab o'sadi!")),
        slide("Vektor|Вектор|Vector",
              ("2-QADAM · TEZLIK", "STEP 2 · VELOCITY"),
              ("cos va sin tezlikni ajratadi", "cos and sin split the velocity", "cos and sin split the velocity"),
              ("Burchak bo‘yicha tezlikning gorizontal va vertikal qismlari hisoblanadi.",
               "По углу вычисляются горизонтальная и вертикальная части скорости.",
               "The angle gives the horizontal and vertical parts of the velocity."),
              cards(
                  card(("COS", "COS", "COS"), ("X komponent", "X-компонент", "X component"),
                       ("vx = cos(angle) * speed — qanchalik o‘ngga/chapga.",
                        "vx = cos(angle) * speed — насколько вправо/влево.",
                        "vx = cos(angle) * speed — how far right/left.")),
                  card(("SIN", "SIN", "SIN"), ("Y komponent", "Y-комponent", "Y component"),
                       ("vy = sin(angle) * speed — qanchalik pastga/yuqoriga.",
                        "vy = sin(angle) * speed — насколько вниз/вверх.",
                        "vy = sin(angle) * speed — how far down/up."))) + code("bullet.x += Math.cos(angle) * speed * dt;\nbullet.y += Math.sin(angle) * speed * dt;")),
        slide("Hayot tsikli|Жизненный цикл|Lifecycle",
              ("BULLET ARRAY", "BULLET ARRAY"),
              ("O‘q tug‘iladi, uchadi va o‘chiriladi", "Снаряд рождается, летит и удаляется", "A bullet is born, flies and is removed"),
              ("Har kadr yangi massiv yaratish emas — mavjud o‘qlarni yangilash va vaqti tugaganlarini tozalash.",
               "Не создавать новый массив каждый кадр, а обновлять и удалять старые снаряды.",
               "Update existing bullets and remove expired ones instead of allocating arrays each frame."),
              steps([
                  ("Fire: o‘q obyekti massivga qo‘shiladi", "Fire: объект добавляется в массив", "Fire: push a bullet object"),
                  ("Update: har o‘q pozitsiyasi yangilanadi", "Update: обновляем позиции", "Update: move each bullet"),
                  ("Collide: dushman bilan to‘qnashuv tekshiruvi", "Collide: проверка столкновения", "Collide: test against enemies"),
                  ("Cleanup: ekrandan chiqqan o‘q o‘chiriladi", "Cleanup: удалить за пределами экрана", "Cleanup: remove off-screen bullets"),
              ]) + code("bullets = bullets.filter(b =>\n  b.x > 0 && b.x < W && b.y > 0 && b.y < H && !b.hit);")),
        slide("To‘qnashuv|Столкновение|Collision",
              ("AABB TESTI", "AABB TEST"),
              ("To‘q tegdi yoki tegmadi?", "Попадание или промах?", "Hit or miss?"),
              ("To‘rt tomonlama solishtirish — eng tez va ishonchli usul.",
               "Сравнение четырёх сторон — быстрый и надёжный способ.",
               "Comparing four edges is the fast and reliable approach."),
              code("function hit(a, b) {\n  return a.x < b.x + b.w && a.x + a.w > b.x &&\n         a.y < b.y + b.h && a.y + a.h > b.y;\n}\n// ✅ hit bo'lsa: hp -= 1, o'q o'chiriladi, zarracha qo'shiladi")),
        slide("Recoil|Отдача|Recoil",
              ("SEZGI VA REALIZM", "ОЩУЩЕНИЕ И РЕАЛИЗМ"),
              ("Recoil va tarqalish (spread)", "Отдача и разброс", "Recoil and spread"),
              ("Har o‘qdan keyin burchakka kichik tasodifiy og‘ish qo‘shish otishmani jonli qiladi.",
               "Небольшой случайный сдвиг угла после каждого выстрела делает стрельбу живой.",
               "A small random angle offset per shot makes firing feel alive."),
              cards(
                  card(("RECOIL", "ОТДАЧА", "RECOIL"), ("Orqaga siljish", "Откат", "Kickback"),
                       ("player.x -= cos(a) * 2; kamera 2 px silkishadi.",
                        "player.x -= cos(a) * 2; камера смещается на 2 px.",
                        "player.x -= cos(a) * 2; camera shakes by 2 px.")),
                  card(("SPREAD", "РАЗБРОС", "SPREAD"), ("±3° xato", "Ошибка ±3°", "±3° error"),
                       ("a + (Math.random()-0.5) * 0.1 — har o‘q biroz farq qiladi.",
                        "a + (Math.random()-0.5) * 0.1 — каждый выстрел немного отличается.",
                        "a + (Math.random()-0.5) * 0.1 — every shot differs slightly.")))),
        slide("Zarrachalar|Частицы|Particles",
              ("VIZUAL EFFEKT", "VISUAL EFFECT"),
              ("Zarrachalar tizimi natijani ko‘rsatadi", "Система частиц показывает результат", "Particle system shows the result"),
              ("O‘q dushmanga teganda 8 ta kichik zarracha tarqaladi — bu hit faktini tasdiqlaydi.",
               "При попадании разлетаются 8 частиц — это подтверждает факт попадания.",
               "On impact, 8 particles scatter — visual confirmation of the hit."),
              code("for (let i = 0; i < 8; i++) {\n  const a = Math.random() * Math.PI * 2;\n  particles.push({ x, y,\n    vx: Math.cos(a) * 60, vy: Math.sin(a) * 60, life: 0.4 });\n}")),
        slide("Optimallashtirish|Оптимизация|Optimisation",
              ("60 FPS QOIDASI", "60 FPS RULE"),
              ("O‘qlar soni — xotira va FPS", "Число снарядов — память и FPS", "Bullet count — memory and FPS"),
              ("Cheksiz o‘q yaratish ertami-kechmi freymlarni tushiradi; obyekt pooling va chegaralar shart.",
               "Бесконечное создание снарядов рано или поздно снижает FPS; нужны пул и лимиты.",
               "Unbounded bullets eventually drop FPS; use pooling and limits."),
              cards(
                  card(("LIMIT", "ЛИМИТ", "LIMIT"), ("Maks 40 o‘q", "Макс. 40 снарядов", "Max 40 bullets"),
                       ("Yangi o‘q qo‘shishdan oldin massiv uzunligini tekshirish.",
                        "Проверять длину массива перед добавлением.",
                        "Check array length before adding a new bullet.")),
                  card(("POOL", "ПУЛ", "POOL"), ("Qayta ishlatish", "Повторное использование", "Reuse"),
                       ("O‘chirilgan obyektni yo‘q qilmasdan, yangi o‘q sifatida qayta ishlatish.",
                        "Переиспользовать удалённый объект вместо создания нового.",
                        "Reuse removed objects instead of allocating new ones.")))),
        slide("Xatolar|Ошибки|Failure modes",
              ("TEKSHIRUV", "CHECK"),
              ("Eng ko‘p uchraydigan 4 xato", "Четыре частые ошибки", "Four common mistakes"),
              ("Bularni darsdagi arena oldidan tekshirib chiqing.", "Проверьте их перед лабораторией.", "Check these before the lab."),
              steps([
                  ("Canvas Y o‘qi pastga qarab o‘sadi — dy belgisini almashtirmang",
                   "Ось Y canvas направлена вниз — не меняйте знак dy",
                   "Canvas Y grows downward — don't flip the dy sign"),
                  ("Tezlikni faqat bitta o‘qqa qo‘llash", "Скорость только по одной оси", "Applying velocity to only one axis"),
                  ("O‘qlarni hech qachon o‘chirmaslik -> xotira o‘sadi", "Не удалять снаряды -> рост памяти", "Never removing bullets -> memory growth"),
                  ("Radian va darajani aralashtirish", "Смешивать радианы и градусы", "Mixing radians and degrees"),
              ])),
    ],
    "quiz": quiz(
        ("Player (100,100), nishon (100,40). Math.atan2(dy, dx) qanday burchak beradi?",
         "Игрок (100,100), цель (100,40). Что вернёт Math.atan2(dy, dx)?",
         "Player (100,100), target (100,40). What does Math.atan2(dy, dx) return?"),
        [
            (("0 radian", "0 радиан", "0 radians"), False),
            (("-π/2 (yuqoriga)", "-π/2 (вверх)", "-π/2 (upwards)"), True),
            (("+π/2 (pastga)", "+π/2 (вниз)", "+π/2 (downwards)"), False),
        ],
        ("To‘g‘ri: dy = 40-100 = -60, dx = 0 → atan2(-60, 0) = -π/2. Canvasda Y pastga o‘sadi, shuning uchun manfiy burchak — yuqoriga.",
         "Верно: dy = -60, dx = 0 → atan2 = -π/2. В canvas ось Y растёт вниз, поэтому отрицательный угол — вверх.",
         "Correct: dy = -60, dx = 0 → atan2 = -π/2. Canvas Y grows down, so a negative angle points up."),
    ),
    "practice": {
        "title": tri("Otishma Simulyatori", "Симулятор стрельбы", "Shooting Simulator"),
        "task": tri("Sichqonchaga qarab o‘q uzuvchi, to‘qnashuv va zarracha effekti bor turret yasang.",
                    "Сделайте турель, стреляющую по курсору, со столкновениями и частицами.",
                    "Build a turret that shoots at the cursor with collisions and particles."),
        "steps": [
            "atan2 bilan burchak hisoblash / Угол через atan2 / Angle via atan2",
            "cos/sin bilan tezlikni ajratish / Скорость через cos/sin / Velocity via cos/sin",
            "AABB to‘qnashuv va o‘qni o‘chirish / AABB и удаление / AABB and cleanup",
            "Zarracha effekti va hisob / Частицы и счёт / Particles and score",
        ],
    },
    "homework": homework(
        ("Darsdagi atan2 + cos/sin formulasini xatolarsiz takrorlash.",
         "Воспроизвести формулу atan2 + cos/sin без ошибок.",
         "Reproduce the atan2 + cos/sin formula without errors."),
        ("Turretga 3 soniyaliq «tezkor otish» (rapid fire) va o‘q chegarasi qo‘shish.",
         "Добавить трёхсекундный режим быстрой стрельбы и лимит снарядов.",
         "Add a 3-second rapid-fire mode and a bullet limit."),
        ("Obyekt pooling bilan 60 FPS ni saqlash va xotira sizishini oldini olish.",
         "Сохранить 60 FPS через пул объектов и избежать утечки памяти.",
         "Keep 60 FPS with object pooling and prevent memory leaks."),
    ),
}


# ============================================================
# 5–6-SINF · 32-DARS · AQLLI SHARTLAR (80 min)
# ============================================================
SPEC_56 = {
    "cohort": "5-6-sinf",
    "week": 13,
    "lesson_no": 32,
    "title": tri("Aqlli Shartlar: Agar... U Holda va Sezgirlik Bloklari (Magic Maze)",
                 "Умные условия: Если... То и блоки sensed (Magic Maze)",
                 "Smart Conditions: If... Then and Sensing Blocks (Magic Maze)"),
    "lede": tri("Qahramon endi o‘zi qaror qabul qiladi: devorga tegsa to‘xtaydi, kalitni ko‘rsa eshikni ochadi.",
                "Герой теперь принимает решения: у стены останавливается, увидев ключ — открывает дверь.",
                "The hero now decides: it stops at a wall and opens the door when it sees a key."),
    "duration": 80,
    "slug": "32-dars-aqlli-shartlar-va-sezgirlik",
    "hw_review": {
        "pitfall": {
            "title": tri("Xato: qahramon devor orasidan o‘tib ketadi", "Ошибка: герой проходит сквозь стену", "Pitfall: the hero walks through walls"),
            "desc": tri("O‘tgan darsdagi sikl faqat harakatni takrorlagan — to‘siq bor-yo‘qligi tekshirilmagan.",
                        "В прошлом уроке цикл только повторял движение, не проверяя стены.",
                        "Last lesson's loop repeated movement without checking for walls."),
            "code": "// ❌ Har doim yuraveradi\navast every 5 steps: move();",
        },
        "solution": {
            "title": tri("Oltin yechim: har qadamda shart tekshir", "Золотой стандарт: проверять условие на каждом шаге", "Golden standard: check the condition every step"),
            "desc": tri("Harakatdan oldin «devorga tegayapmanmi?» degan savol beriladi.",
                        "Перед движением задаётся вопрос: «Я касаюсь стены?»",
                        "Before moving, ask: \"Am I touching a wall?\""),
            "code": "// ✅ Agar devor bo'lsa, yurma\nif (touchingColor('gray')) {\n  stop();\n} else {\n  move(10);\n}",
        },
        "blitz": tri("«Agar... u holda» bloki qayerda joylashgan?", "Где находится блок «Если... то»?", "Where is the \"if... then\" block found?"),
        "bridge": tri("Sikl harakatni takrorlaydi, shart esa unga aql beradi — bugun ikkalasini birlashtiramiz.",
                      "Цикл повторяет движение, условие даёт ему ум — сегодня соединяем их.",
                      "The loop repeats motion; the condition adds intelligence — today we combine them."),
    },
    "slides": [
        slide("Takrorlash|Повторение|Recap",
              ("O'TGAN DARS KO'PRIGI", "BRIDGE FROM LAST LESSON"),
              ("Sikl + shart = aqlli harakat", "Цикл + условие = умное движение", "Loop + condition = smart motion"),
              ("Sikl «qancha» takrorlashni biladi, shart esa «qachon» to‘xtashni.",
               "Цикл знает «сколько» повторов, условие — «когда» остановиться.",
               "The loop knows how many times; the condition knows when to stop."),
              cards(
                  card(("SIKL", "ЦИКЛ", "LOOP"), ("Doimiy harakat", "Постоянное движение", "Continuous motion"),
                       ("Forever bloki qahramonni to‘xtovsiz yuritadi.",
                        "Блок forever заставляет героя идти постоянно.",
                        "The forever block keeps the hero moving.")),
                  card(("SHART", "УСЛОВИЕ", "CONDITION"), ("Qaror qabul qilish", "Принятие решения", "Decision making"),
                       ("If bloki har qadamda savol beradi va javobga qarab ishlaydi.",
                        "Блок if задаёт вопрос на каждом шаге и действует по ответу.",
                        "The if block asks a question each step and acts on the answer.")))),
        slide("If-Then|If-Then|If-Then",
              ("1-BLOK · SHART", "BLOCK 1 · CONDITION"),
              ("Agar... u holda", "Если... то", "If... then"),
              ("Shart rost bo‘lsa ichidagi buyruqlar bajariladi, yolg‘on bo‘lsa hech narsa qilinmaydi.",
               "Если условие истинно, команды внутри выполняются; иначе ничего не происходит.",
               "If the condition is true, inner commands run; otherwise nothing happens."),
              code("agar (tikan'ga tegish) {\n  jon -= 1;\n  boshlang'ich joyga qaytish;\n}")),
        slide("Else|Else|Else",
              ("2-BLOK · TANLOV", "BLOCK 2 · ALTERNATIVE"),
              ("Agar... u holda... aks holda", "Если... то... иначе", "If... then... else"),
              ("Ikki yo‘l bor: shart rost bo‘lsa bir ish, yolg‘on bo‘lsa boshqa ish.",
               "Два пути: если условие истинно — одно действие, иначе — другое.",
               "Two paths: one action when true, another when false."),
              cards(
                  card(("ROST", "ИСТИНА", "TRUE"), ("Rang yashil", "Цвет зелёный", "Colour is green"),
                       ("Yurishni davom ettirish.", "Продолжить движение.", "Keep walking."), "var(--green)"),
                  card(("YOLG'ON", "ЛОЖЬ", "FALSE"), ("Rang qizil", "Цвет красный", "Colour is red"),
                       ("To‘xtab, orqaga qaytish.", "Остановиться и отойти назад.", "Stop and step back."), "var(--accent)"))),
        slide("Sezgirlik|Сенсоры|Sensing",
              ("3-BLOK · SEZGIRLIK", "BLOCK 3 · SENSING"),
              ("Qahramon atrofini qanday «ko‘radi»?", "Как герой «видит» вокруг?", "How does the hero sense its surroundings?"),
              ("Sezgirlik bloklari rang, klaviatura va sichqoncha holatini surveydi.",
               "Блоки sensing опрашивают цвет, клавиатуру и мышь.",
               "Sensing blocks poll colour, keyboard and mouse state."),
              steps([
                  ("Rangga tegish (touching color) — devor yoki tuzoqni aniqlash",
                   "Касание цвета (touching color) — стена или ловушка",
                   "Touching colour — detect a wall or trap"),
                  ("Tugma bosilganmi (key pressed) — boshqaruv",
                   "Клавиша нажата (key pressed) — управление",
                   "Key pressed — control input"),
                  ("Sichqoncha holati (mouse down) — bosslarga bosish",
                   "Состояние мыши (mouse down) — нажатие на кнопки",
                   "Mouse down — button clicks"),
                  ("Boshqa sprayt bilan to‘qnashuv — kalit va eshik",
                   "Столкновение со спрайтом — ключ и дверь",
                   "Sprite collision — key and door"),
              ])),
        slide("Mantiq|Логика|Logic",
              ("VA / YOKI", "AND / OR"),
              ("Bir nechta shartni birlashtirish", "Объединение нескольких условий", "Combining multiple conditions"),
              ("«Va» ikkalasi ham rost bo‘lsa, «yoki» kamida bittasi rost bo‘lsa ishlaydi.",
               "«И» требует истины обоих, «ИЛИ» — хотя бы одного.",
               "AND needs both true; OR needs at least one true."),
              code("agar (yashil'ga tegish VA tugma == '->') {\n  yurish();\n}\nagar (qizil'ga tegish YOKI sariq'ga tegish) {\n  jon -= 1;\n}")),
        slide("Ichma-ich|Вложенные|Nested",
              ("SHART ICHIDA SHART", "CONDITION INSIDE CONDITION"),
              ("Ichma-ich shartlar", "Вложенные условия", "Nested conditions"),
              ("Avval kalit bormi, keyin eshik yopiqmi — ikki bosqichli tekshiruv.",
               "Сначала есть ли ключ, затем закрыта ли дверь — двухэтапная проверка.",
               "First check for the key, then whether the door is closed."),
              steps([
                  ("1-qadam: kalit olinganmi?", "Шаг 1: ключ взят?", "Step 1: is the key collected?"),
                  ("2-qadam: eshik yopiqmi?", "Шаг 2: дверь закрыта?", "Step 2: is the door closed?"),
                  ("3-qadam: xabar yuborish — eshik ochiladi", "Шаг 3: broadcast — дверь открывается", "Step 3: broadcast — door opens"),
                  ("Aks holda: «Kalit kerak!» deb yozish", "Иначе: написать «Нужен ключ!»", "Else: show \"Key required!\""),
              ])),
        slide("O'yin|Игра|Game",
              ("MAGIC MAZE", "MAGIC MAZE"),
              ("Sehrli labirint qurish", "Собрать волшебный лабиринт", "Build the Magic Maze"),
              ("Maqsad: kalitni olib, qizil tuzoqlardan qochib, yashil eshikka yetish.",
               "Цель: взять ключ, избежать красных ловушек и достичь зелёной двери.",
               "Goal: collect the key, avoid red traps and reach the green door."),
              cards(
                  card(("QAH RAMON", "ГЕРОЙ", "HERO"), ("Mushuk", "Кот", "Cat"),
                       ("O‘q tugmalari bilan yuradi, har qadamda rangni tekshiradi.",
                        "Ходит стрелками и проверяет цвет на каждом шаге.",
                        "Moves with arrow keys and checks colour each step.")),
                  card(("TUZOQ", "ЛОВУШКА", "TRAP"), ("Qizil rang", "Красный цвет", "Red colour"),
                       ("Tegilsa jon kamayadi va boshlang‘ich joyga qaytadi.",
                        "При касании life уменьшается и герой возвращается в начало.",
                        "On contact, life drops and the hero returns to start."), "var(--accent)"),
                  card(("ESHIK", "ДВЕРЬ", "DOOR"), ("Yashil rang", "Зелёный цвет", "Green colour"),
                       ("Faqat kalit bor bo‘lsa ochiladi — keyingi bosqich.",
                        "Открывается только с ключом — следующий уровень.",
                        "Opens only with the key — next level."), "var(--green)"))),
        slide("Debug|Отладка|Debug",
              ("XATOLARNI TOPISH", "FINDING BUGS"),
              ("Nega shart ishlamayapti?", "Почему условие не работает?", "Why isn't the condition working?"),
              ("Ko‘pincha rang nomi xato yoziladi yoki tekshiruv harakatdan keyin qo‘yiladi.",
               "Часто неверно указан цвет или проверка стоит после движения.",
               "Usually the colour name is wrong or the check is placed after the move."),
              steps([
                  ("Rangni exactly bir xil nom bilan yozing", "Запишите цвет точь-в-точь", "Write the colour name exactly"),
                  ("Tekshiruvni harakatdan OLDIN qo‘ying", "Проверку ставьте ДО движения", "Place the check BEFORE moving"),
                  ("Sensor qiymatini doskaga chiqarib ko‘ring", "Выведите значение сенсора на экран", "Print the sensor value on screen"),
              ])),
    ],
    "quiz": quiz(
        ("Qahramon devorga tegishini qaysi blok aniqlaydi?",
         "Какой блок определяет касание стены героем?",
         "Which block detects that the hero touches a wall?"),
        [
            (("Forever bloki", "Блок forever", "Forever block"), False),
            (("Rangga tegish (touching color) sensori", "Сенсор касания цвета (touching color)", "Touching colour sensor"), True),
            (("Jonlarni nollash bloki", "Блок обнуления жизней", "Reset lives block"), False),
        ],
        ("To‘g‘ri: sezgirlik bloki «rangga tegish» devor rangini aniqlaydi; undan keyin if bloki qaror qabul qiladi.",
         "Верно: сенсор «касание цвета» определяет цвет стены, затем блок if принимает решение.",
         "Correct: the touching-colour sensor detects the wall colour, then the if block decides."),
    ),
    "practice": {
        "title": tri("Sehrli Labirint Arena", "Арена «Волшебный лабиринт»", "Magic Maze Arena"),
        "task": tri("Kalit olib, tuzoqlardan qochib, eshikni ochadigan shartli harakat dasturini yozing.",
                    "Напишите программу с условиями: взять ключ, избежать ловушек, открыть дверь.",
                    "Write a conditional movement program: collect the key, dodge traps, open the door."),
        "steps": [
            "Rang sensori bilan devor tekshiruvi / Проверка стены / Wall check",
            "Agar/aks holda bilan jon himoyasi / Защита жизней / Life protection",
            "Kalit va eshik uchun ichma-ich shart / Вложенные условия / Nested conditions",
            "Juftlikda sinab, xatoni topish / Проверка в паре / Peer testing",
        ],
    },
    "homework": homework(
        ("Darsdagi if/else va rang sensori namunasini xatolarsiz takrorlash.",
         "Воспроизвести пример if/else и сенсора цвета без ошибок.",
         "Reproduce the if/else and colour sensor example without errors."),
        ("Labirintga ikkinchi tuzoq va «Va» sharti bilan qo‘shimcha qoida qo‘shing.",
         "Добавьте вторую ловушку и дополнительное правило с условием «И».",
         "Add a second trap and an extra rule using AND."),
        ("Cheksiz sikl va shart birlashganda qahramon qamalib qolmasligini ta’minlang.",
         "Сделайте так, чтобы герой не застревал при сочетании цикла и условия.",
         "Ensure the hero never gets stuck when a loop and condition combine."),
    ),
}


if __name__ == "__main__":
    for spec in (SPEC_1011, SPEC_78, SPEC_56):
        compile_lesson(spec)
