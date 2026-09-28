# -*- coding: utf-8 -*-
"""7-8-sinf · 3-hafta · 13-dars — Canvas va O'yin Tsikli: RAF, Delta Time va Fizika."""

import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from build import (Lesson, slide, title_slide, box, code, el, i18n,
                   sheet_header, mission, table, sheet_box, rubric, writelines, sign_box)

D = "classes/7-8-sinf/3-hafta/13-dars-canvas-va-oyin-tsikli"

TITLES = {
    "uz": "13-dars: Canvas va O'yin Tsikli — RAF, Delta Time va Fizika",
    "ru": "Урок 13: Canvas и Игровой Цикл — RAF, Delta Time и Физика",
    "en": "Lesson 13: Canvas and the Game Loop — RAF, Delta Time and Physics",
}
SHEET_TITLES = {k: v + (" — Ish Varaqasi" if k == "uz" else
                        " — Рабочий Лист" if k == "ru" else " — Worksheet")
                for k, v in TITLES.items()}

S = []

S.append(title_slide(
    ph=("Kirish", "Введение", "Intro"), time="0–3",
    eyebrow=("Vibecoding · 13-dars · 7–8-sinflar",
             "Vibecoding · Урок 13 · 7–8 классы",
             "Vibecoding · Lesson 13 · Grades 7–8"),
    h1=("Canvas va O'yin Tsikli: Tugmadan Haqiqiy Dvigatelgacha",
        "Canvas и Игровой Цикл: От Кнопки к Настоящему Движку",
        "Canvas and the Game Loop: From Buttons to a Real Engine"),
    lede=("Shu paytgacha sizning o'yinlaringiz <b>tugma bosishdan</b> iborat edi: "
          "klik → hisob oshadi. Bu o'yin emas, bu forma. Haqiqiy o'yinda ekran "
          "sekundiga <b>60 marta</b> qaytadan chiziladi, qahramon tezlik va "
          "gravitatsiyaga ega, to'qnashuvlar esa matematik hisoblanadi. "
          "Bugun siz o'sha dvigatelni ichidan ko'rasiz.",
          "До сих пор ваши игры состояли из <b>нажатий кнопок</b>: клик → счёт вырос. "
          "Это не игра, это форма. В настоящей игре экран перерисовывается "
          "<b>60 раз в секунду</b>, у героя есть скорость и гравитация, "
          "а столкновения считаются математически. "
          "Сегодня вы увидите этот движок изнутри.",
          "Until now your games were <b>button presses</b>: click → score goes up. "
          "That is not a game, that is a form. In a real game the screen redraws "
          "<b>60 times a second</b>, the hero has velocity and gravity, and "
          "collisions are computed mathematically. "
          "Today you look inside that engine."),
    meta=[("<b>Fan:</b> Vibecoding · O'yin dvigateli",
           "<b>Предмет:</b> Vibecoding · Игровой движок",
           "<b>Subject:</b> Vibecoding · Game Engine"),
          ("<b>Kohorta:</b> 7–8-sinf", "<b>Когорта:</b> 7–8 класс", "<b>Cohort:</b> Grades 7–8"),
          ("<b>Hafta:</b> 3 (1-soat)", "<b>Неделя:</b> 3 (1-й час)", "<b>Week:</b> 3 (Hour 1)")],
))

S.append(slide(
    ph=("Muammo", "Проблема", "Problem"), time="3–6",
    eyebrow=("DOM ning chegarasi", "Предел DOM", "The limit of the DOM"),
    title=("Nega &lt;div&gt; lardan o'yin qurib bo'lmaydi",
           "Почему из &lt;div&gt; нельзя собрать игру",
           "Why you cannot build a game out of &lt;div&gt;s"),
    body='<div class="cols c2">\n'
         + box("", ("DOM qanday ishlaydi", "Как работает DOM", "How the DOM works"),
               items=[
                   ("Har bir element — brauzer uchun alohida <b>obyekt</b>: rangi, "
                    "o'lchami, joylashuvi, hodisalari.",
                    "Каждый элемент — отдельный <b>объект</b> для браузера: цвет, "
                    "размер, положение, события.",
                    "Every element is a separate <b>object</b> to the browser: colour, "
                    "size, position, events."),
                   ("Bitta elementni siljitsangiz, brauzer <b>butun sahifani</b> qayta "
                    "hisoblashi mumkin (reflow).",
                    "Сдвинете один элемент — браузер может пересчитать <b>всю страницу</b> "
                    "(reflow).",
                    "Move one element and the browser may recompute <b>the whole page</b> "
                    "(reflow)."),
                   ("100 ta <code>div</code> — sekin. 1000 tasi — slayd-shou.",
                    "100 <code>div</code> — медленно. 1000 — слайд-шоу.",
                    "100 <code>div</code>s — slow. 1000 — a slideshow."),
               ])
         + "\n"
         + box("accent", ("Canvas qanday ishlaydi", "Как работает Canvas", "How Canvas works"),
               items=[
                   ("Canvas — bu <b>bitta</b> element. Uning ichida obyektlar yo'q, "
                    "faqat piksellar.",
                    "Canvas — это <b>один</b> элемент. Внутри него нет объектов, "
                    "только пиксели.",
                    "Canvas is <b>one</b> element. Inside it there are no objects, "
                    "only pixels."),
                   ("Siz unga rasm <b>chizasiz</b> — xuddi doskaga bo'r bilan.",
                    "Вы <b>рисуете</b> на нём — как мелом на доске.",
                    "You <b>draw</b> on it — like chalk on a board."),
                   ("10 000 ta obyektni 60 FPS da chizish — normal holat.",
                    "10 000 объектов на 60 FPS — обычное дело.",
                    "10,000 objects at 60 FPS is routine."),
               ])
         + "\n</div>\n"
         + box("purple", ("Doskadagi metafora", "Метафора доски", "The chalkboard metaphor"),
               p=("DOM — bu <b>magnit doska</b>: har bir magnitni alohida surasiz, "
                  "brauzer ularni eslab turadi. Canvas — bu <b>oddiy doska</b>: "
                  "har kadrda o'chirib, hammasini qaytadan chizasiz. "
                  "Aynan shuning uchun tez — brauzer hech narsani eslab turmaydi.",
                  "DOM — это <b>магнитная доска</b>: каждый магнит двигаете отдельно, "
                  "браузер их помнит. Canvas — это <b>обычная доска</b>: "
                  "каждый кадр стираете и рисуете всё заново. "
                  "Именно поэтому быстро — браузеру нечего помнить.",
                  "The DOM is a <b>magnet board</b>: you move each magnet and the browser "
                  "remembers them all. Canvas is a <b>plain chalkboard</b>: every frame you "
                  "wipe it and redraw everything. "
                  "That is exactly why it is fast — the browser remembers nothing.")),
))

S.append(slide(
    ph=("Canvas", "Canvas", "Canvas"), time="6–10",
    eyebrow=("Ikkita qator kod", "Две строки кода", "Two lines of code"),
    title=("Canvas bilan ishlash butunlay ikkita obyektdan iborat",
           "Вся работа с Canvas — это два объекта",
           "All Canvas work comes down to two objects"),
    body='<div class="cols c2">\n'
         + box("green", ("Boshlash", "Начало", "Getting started"),
               extra_html=code(
                   "// 1. HTML da maydon\n"
                   "<canvas id=\"cv\" width=\"800\" height=\"400\"></canvas>\n\n"
                   "// 2. JS da \"qalam\" olish\n"
                   "var cv  = document.getElementById('cv');\n"
                   "var ctx = cv.getContext('2d');\n\n"
                   "// 3. Chizish\n"
                   "ctx.fillStyle = '#FF1100';\n"
                   "ctx.fillRect(100, 50, 40, 40);   // x, y, w, h"))
         + "\n"
         + box("accent", ("Eng ko'p ishlatiladigan 5 ta amal",
                          "5 самых нужных команд", "The 5 commands you need most"),
               items=[
                   ("<code>fillRect(x,y,w,h)</code> — to'ldirilgan to'rtburchak.",
                    "<code>fillRect(x,y,w,h)</code> — закрашенный прямоугольник.",
                    "<code>fillRect(x,y,w,h)</code> — a filled rectangle."),
                   ("<code>clearRect(0,0,W,H)</code> — <b>butun ekranni o'chirish</b>.",
                    "<code>clearRect(0,0,W,H)</code> — <b>стереть весь экран</b>.",
                    "<code>clearRect(0,0,W,H)</code> — <b>wipe the whole screen</b>."),
                   ("<code>fillStyle</code> — keyingi chiziqlar rangi.",
                    "<code>fillStyle</code> — цвет для следующих фигур.",
                    "<code>fillStyle</code> — the colour for what you draw next."),
                   ("<code>fillText(s,x,y)</code> — matn (hisob, FPS).",
                    "<code>fillText(s,x,y)</code> — текст (счёт, FPS).",
                    "<code>fillText(s,x,y)</code> — text (score, FPS)."),
                   ("<code>arc(x,y,r,0,7)</code> — doira (o'q, to'p, zarra).",
                    "<code>arc(x,y,r,0,7)</code> — круг (пуля, мяч, частица).",
                    "<code>arc(x,y,r,0,7)</code> — a circle (bullet, ball, particle)."),
               ])
         + "\n</div>\n"
         + box("", ("⚠️ Koordinata tizimi maktabdagidan boshqacha",
                    "⚠️ Система координат не как в школе",
                    "⚠️ The coordinate system is not the school one"),
               p=("Canvas da <b>(0,0) yuqori chap burchakda</b>, va <b>Y pastga o'sadi</b>. "
                  "Ya'ni <code>y = 300</code> — bu <code>y = 100</code> dan <b>pastroq</b>. "
                  "Shuning uchun sakrash <code>y</code> ni <b>kamaytiradi</b>: "
                  "<code>vy = -13</code>. Bu eng ko'p uchraydigan chalkashlik.",
                  "В Canvas <b>(0,0) в левом верхнем углу</b>, и <b>Y растёт вниз</b>. "
                  "То есть <code>y = 300</code> <b>ниже</b>, чем <code>y = 100</code>. "
                  "Поэтому прыжок <b>уменьшает</b> <code>y</code>: "
                  "<code>vy = -13</code>. Это самая частая путаница.",
                  "In Canvas <b>(0,0) is the top-left corner</b> and <b>Y grows downward</b>. "
                  "So <code>y = 300</code> is <b>lower</b> than <code>y = 100</code>. "
                  "That is why jumping <b>decreases</b> <code>y</code>: "
                  "<code>vy = -13</code>. This is the most common confusion.")),
))

S.append(slide(
    ph=("O'yin tsikli", "Игровой цикл", "Game loop"), time="10–14",
    eyebrow=("Har qanday o'yinning yuragi", "Сердце любой игры", "The heart of every game"),
    title=("O'yin tsikli — sekundiga 60 marta takrorlanadigan 3 qadam",
           "Игровой цикл — 3 шага, повторяемые 60 раз в секунду",
           "The game loop — 3 steps repeated 60 times a second"),
    body='<div class="cols c3">\n' + "\n".join([
        box("", ("1 · CLEAR", "1 · CLEAR", "1 · CLEAR"),
            p=("Ekranni butunlay o'chirish. Agar bu qadamni tashlab ketsangiz, "
               "qahramon o'zidan <b>iz qoldiradi</b> — ba'zan bu qasddan effekt, "
               "lekin odatda xato.",
               "Полностью стереть экран. Пропустите этот шаг — герой начнёт "
               "<b>оставлять след</b>. Иногда это приём, но обычно баг.",
               "Wipe the screen completely. Skip this step and the hero leaves a "
               "<b>trail</b> — sometimes an effect, usually a bug.")),
        box("purple", ("2 · UPDATE", "2 · UPDATE", "2 · UPDATE"),
            p=("Hech narsa chizilmaydi! Faqat <b>raqamlar o'zgaradi</b>: pozitsiya, "
               "tezlik, hisob, dushman holati. Bu — o'yinning <b>miyasi</b>.",
               "Ничего не рисуется! Только <b>меняются числа</b>: позиция, скорость, "
               "счёт, состояние врага. Это — <b>мозг</b> игры.",
               "Nothing is drawn! Only <b>numbers change</b>: position, velocity, "
               "score, enemy state. This is the game's <b>brain</b>.")),
        box("accent", ("3 · DRAW", "3 · DRAW", "3 · DRAW"),
            p=("Hech narsa hisoblanmaydi! Faqat <b>joriy holat chiziladi</b>. "
               "Bu — o'yinning <b>ko'zi</b>. Ikkovini aralashtirmaslik — professional "
               "kodning asosiy qoidasi.",
               "Ничего не считается! Только <b>рисуется текущее состояние</b>. "
               "Это — <b>глаза</b> игры. Не смешивать эти два — главное правило "
               "профессионального кода.",
               "Nothing is computed! Only the <b>current state is drawn</b>. "
               "This is the game's <b>eyes</b>. Keeping the two apart is the core rule "
               "of professional code.")),
    ]) + "\n</div>\n"
         + box("green", ("Kodda", "В коде", "In code"),
               extra_html=code(
                   "function loop(time){\n"
                   "  ctx.clearRect(0, 0, W, H);   // 1 CLEAR\n"
                   "  update();                    // 2 UPDATE — faqat raqamlar\n"
                   "  draw();                      // 3 DRAW  — faqat chizish\n"
                   "  requestAnimationFrame(loop); // o'zini qayta chaqiradi\n"
                   "}\n"
                   "requestAnimationFrame(loop);   // birinchi kadr")),
))

S.append(slide(
    ph=("RAF", "RAF", "RAF"), time="14–18",
    eyebrow=("setInterval nega yomon", "Почему setInterval плох", "Why setInterval is bad"),
    title=("requestAnimationFrame vs setInterval",
           "requestAnimationFrame против setInterval",
           "requestAnimationFrame vs setInterval"),
    body='<div class="cols c2">\n'
         + box("accent", ("❌ setInterval(loop, 16)", "❌ setInterval(loop, 16)", "❌ setInterval(loop, 16)"),
               items=[
                   ("Brauzer ekranni qachon yangilashini <b>bilmaydi</b> — kadrlar "
                    "monitordan ajralib qoladi (tearing, silkinish).",
                    "<b>Не знает</b>, когда браузер обновит экран — кадры "
                    "рассинхронизируются с монитором (разрывы, дёрганье).",
                    "It <b>does not know</b> when the browser repaints — frames drift out "
                    "of sync with the monitor (tearing, stutter)."),
                   ("Vkladka fonga o'tsa ham <b>ishlashda davom etadi</b> va batareyani "
                    "yeydi.",
                    "Продолжает <b>работать в фоновой вкладке</b> и жрёт батарею.",
                    "Keeps <b>running in a background tab</b> and drains the battery."),
                   ("16 ms — bu <b>kafolat emas</b>, bu iltimos. Brauzer kechiktirishi mumkin.",
                    "16 мс — это <b>не гарантия</b>, а просьба. Браузер может задержать.",
                    "16 ms is <b>not a guarantee</b>, it is a request. The browser may delay."),
               ])
         + "\n"
         + box("green", ("✅ requestAnimationFrame(loop)",
                         "✅ requestAnimationFrame(loop)", "✅ requestAnimationFrame(loop)"),
               items=[
                   ("Brauzer <b>o'zi</b> chaqiradi — aynan ekran yangilanishidan oldin. "
                    "Kadrlar monitor bilan sinxron.",
                    "Браузер вызывает <b>сам</b> — прямо перед обновлением экрана. "
                    "Кадры синхронны с монитором.",
                    "The browser calls it <b>itself</b> — right before a repaint. "
                    "Frames stay in sync with the monitor."),
                   ("Fon vkladkasida <b>avtomatik to'xtaydi</b> — batareya tejaladi.",
                    "В фоновой вкладке <b>останавливается сам</b> — батарея экономится.",
                    "It <b>pauses automatically</b> in a background tab — saving battery."),
                   ("144 Gts monitorda <b>144 FPS</b> beradi, 60 Gts da — 60. "
                    "O'zi moslashadi.",
                    "На мониторе 144 Гц даст <b>144 FPS</b>, на 60 Гц — 60. "
                    "Подстраивается сам.",
                    "On a 144 Hz monitor it gives <b>144 FPS</b>, on 60 Hz — 60. "
                    "It adapts by itself."),
               ])
         + "\n</div>\n"
         + box("purple", ("Lekin shu yerda tuzoq bor",
                          "Но здесь есть ловушка", "But here is the trap"),
               p=("Agar RAF turli kompyuterda turli tezlikda ishlasa — demak "
                  "<b>o'yin ham turli tezlikda ketadi!</b> Kuchli kompyuterda qahramon "
                  "uchadi, zaifida sudraladi. Keyingi slayd shu muammoni yechadi.",
                  "Если RAF на разных компьютерах работает с разной частотой — значит "
                  "<b>и игра пойдёт с разной скоростью!</b> На мощном компьютере герой "
                  "летит, на слабом — ползёт. Следующий слайд решает эту проблему.",
                  "If RAF runs at different rates on different machines, then "
                  "<b>the game runs at different speeds too!</b> On a fast machine the hero "
                  "flies, on a slow one it crawls. The next slide fixes this.")),
))

S.append(slide(
    ph=("Delta Time", "Delta Time", "Delta Time"), time="18–24",
    eyebrow=("Darsning eng muhim tushunchasi",
             "Главное понятие урока", "The key concept of the lesson"),
    title=("Delta Time — o'yin har kompyuterda bir xil tezlikda ketishi uchun",
           "Delta Time — чтобы игра шла одинаково на любом компьютере",
           "Delta Time — so the game runs the same on every machine"),
    body='<div class="cols c2">\n'
         + box("accent", ("❌ Delta Time siz", "❌ Без Delta Time", "❌ Without Delta Time"),
               extra_html=code(
                   "hero.x += 5;   // har KADRDA 5 piksel\n\n"
                   "// 60 FPS -> 300 piksel/sek\n"
                   "// 30 FPS -> 150 piksel/sek  (2x sekin!)\n"
                   "// 144 FPS -> 720 piksel/sek (2.4x tez!)\n\n"
                   "// Bir xil kod, uch xil o'yin."))
         + "\n"
         + box("green", ("✅ Delta Time bilan", "✅ С Delta Time", "✅ With Delta Time"),
               extra_html=code(
                   "hero.x += 300 * dt;  // har SONIYADA 300 piksel\n\n"
                   "// dt = o'tgan kadrdan beri o'tgan vaqt\n"
                   "// 60 FPS  -> dt = 0.016 -> 4.8 px/kadr\n"
                   "// 30 FPS  -> dt = 0.033 -> 10 px/kadr\n"
                   "// 144 FPS -> dt = 0.007 -> 2.1 px/kadr\n\n"
                   "// Turli kadr, BIR XIL tezlik."))
         + "\n</div>\n"
         + box("purple", ("dt qanday hisoblanadi", "Как считается dt", "How dt is computed"),
               extra_html=code(
                   "var oldingi = 0;\n"
                   "function loop(vaqt){            // RAF vaqtni o'zi beradi (ms)\n"
                   "  var dt = (vaqt - oldingi) / 1000;   // soniyaga o'tkazish\n"
                   "  oldingi = vaqt;\n"
                   "  if (dt > 0.1) dt = 0.1;       // vkladka qaytganda sakrashni cheklash\n"
                   "  update(dt);\n"
                   "  requestAnimationFrame(loop);\n"
                   "}")),
))

S.append(slide(
    ph=("Fizika", "Физика", "Physics"), time="24–28",
    eyebrow=("Pozitsiya, tezlik, tezlanish", "Позиция, скорость, ускорение",
             "Position, velocity, acceleration"),
    title=("Butun o'yin fizikasi — uchta qator",
           "Вся игровая физика — три строки",
           "All game physics fits in three lines"),
    body='<div class="cols c2">\n'
         + box("green", ("Uchta qator", "Три строки", "Three lines"),
               extra_html=code(
                   "// 1. Tezlanish tezlikni o'zgartiradi\n"
                   "hero.vy += GRAVITY * dt;\n\n"
                   "// 2. Tezlik pozitsiyani o'zgartiradi\n"
                   "hero.y  += hero.vy * dt;\n\n"
                   "// 3. Yer to'xtatadi\n"
                   "if (hero.y > FLOOR) {\n"
                   "  hero.y = FLOOR;\n"
                   "  hero.vy = 0;\n"
                   "  hero.onGround = true;\n"
                   "}"))
         + "\n"
         + box("accent", ("Bu fizika darsidagi formulaning o'zi",
                          "Это та же формула, что на физике",
                          "This is the formula from physics class"),
               items=[
                   ("<b>Tezlanish</b> (gravitatsiya) tezlikni oshiradi — <code>a → v</code>.",
                    "<b>Ускорение</b> (гравитация) увеличивает скорость — <code>a → v</code>.",
                    "<b>Acceleration</b> (gravity) increases velocity — <code>a → v</code>."),
                   ("<b>Tezlik</b> joyni o'zgartiradi — <code>v → s</code>.",
                    "<b>Скорость</b> меняет положение — <code>v → s</code>.",
                    "<b>Velocity</b> changes position — <code>v → s</code>."),
                   ("Sakrash — bu <code>vy = -JUMP</code>, ya'ni <b>bir zumlik</b> "
                    "yuqoriga tezlik. Qolganini gravitatsiya qiladi.",
                    "Прыжок — это <code>vy = -JUMP</code>, то есть <b>мгновенная</b> "
                    "скорость вверх. Остальное делает гравитация.",
                    "A jump is <code>vy = -JUMP</code> — an <b>instant</b> upward velocity. "
                    "Gravity does the rest."),
                   ("Balandlikni oshirish uchun <code>JUMP</code> ni emas, "
                    "<code>GRAVITY</code> ni kamaytirish ham mumkin — <b>oy effekti</b>.",
                    "Чтобы прыгать выше, можно не увеличивать <code>JUMP</code>, "
                    "а уменьшить <code>GRAVITY</code> — <b>лунный эффект</b>.",
                    "To jump higher you can lower <code>GRAVITY</code> instead of raising "
                    "<code>JUMP</code> — the <b>moon effect</b>."),
               ])
         + "\n</div>",
))

S.append(slide(
    ph=("To'qnashuv", "Столкновения", "Collision"), time="28–31",
    eyebrow=("AABB", "AABB", "AABB"),
    title=("To'qnashuv — bu to'rtta taqqoslash, boshqa hech narsa",
           "Столкновение — это четыре сравнения, и ничего больше",
           "A collision is four comparisons, nothing more"),
    body='<div class="cols c2">\n'
         + box("purple", ("AABB nima", "Что такое AABB", "What AABB means"),
               p=("<b>A</b>xis-<b>A</b>ligned <b>B</b>ounding <b>B</b>ox — "
                  "\"o'qlarga parallel chegaraviy to'rtburchak\". Kompyuter qahramonni "
                  "va dushmanni <b>rasm sifatida ko'rmaydi</b> — u ikkita ko'rinmas "
                  "to'rtburchakning koordinatalarini taqqoslaydi.",
                  "<b>A</b>xis-<b>A</b>ligned <b>B</b>ounding <b>B</b>ox — "
                  "«ограничивающий прямоугольник, параллельный осям». Компьютер "
                  "<b>не видит картинку</b> героя и врага — он сравнивает координаты "
                  "двух невидимых прямоугольников.",
                  "<b>A</b>xis-<b>A</b>ligned <b>B</b>ounding <b>B</b>ox. "
                  "The computer <b>does not see the sprites</b> of the hero and the enemy — "
                  "it compares the coordinates of two invisible rectangles."))
         + "\n"
         + box("green", ("To'rtta shart", "Четыре условия", "Four conditions"),
               extra_html=code(
                   "function toqnashdi(a, b){\n"
                   "  return a.x < b.x + b.w &&\n"
                   "         a.x + a.w > b.x &&\n"
                   "         a.y < b.y + b.h &&\n"
                   "         a.y + a.h > b.y;\n"
                   "}\n\n"
                   "// Bittasi ham false bo'lsa — to'qnashuv YO'Q"))
         + "\n</div>\n"
         + box("accent", ("🎮 Stendda ko'ring", "🎮 Посмотрите на стенде", "🎮 See it on the lab"),
               p=("<b>Hitbox</b> tugmasini bosing — ekranda ko'rinmas to'rtburchaklar "
                  "chiziladi. Siz darhol tushunasiz: o'yinda \"tegmaganday tuyuldi, "
                  "lekin jon ketdi\" holati <b>hitbox rasmdan kattaroq</b> bo'lgani uchun "
                  "sodir bo'ladi.",
                  "Нажмите кнопку <b>Hitbox</b> — на экране появятся невидимые "
                  "прямоугольники. Вы сразу поймёте: ситуация «вроде не задел, а жизнь "
                  "сняли» происходит потому, что <b>хитбокс больше картинки</b>.",
                  "Press the <b>Hitbox</b> button and the invisible rectangles appear. "
                  "You will instantly understand why \"I did not even touch it but lost a "
                  "life\" happens: the <b>hitbox is bigger than the sprite</b>.")),
))

S.append(slide(
    ph=("Optimallashtirish", "Оптимизация", "Optimisation"), time="31–33",
    eyebrow=("FPS nega tushadi", "Почему падает FPS", "Why FPS drops"),
    title=("Kadr 16 millisekundga sig'ishi kerak",
           "Кадр должен уложиться в 16 миллисекунд",
           "A frame must fit inside 16 milliseconds"),
    body='<div class="cols c3">\n' + "\n".join([
        box("green", ("60 FPS = 16.6 ms", "60 FPS = 16.6 мс", "60 FPS = 16.6 ms"),
            p=("Sekundni 60 ga bo'lsangiz — 16.6 ms chiqadi. Update va Draw shu vaqtga "
               "<b>ikkovi birga</b> sig'ishi kerak.",
               "Разделите секунду на 60 — получится 16.6 мс. Update и Draw должны "
               "уложиться в это время <b>вдвоём</b>.",
               "Divide a second by 60 and you get 16.6 ms. Update and Draw must fit in "
               "that window <b>together</b>.")),
        box("accent", ("Nima vaqtni yeydi", "Что съедает время", "What eats the time"),
            p=("Har kadrda yangi obyekt yaratish, <code>fillText</code> ni yuzlab marta "
               "chaqirish, kerak bo'lmagan narsalarni chizish (ekrandan tashqarida).",
               "Создание новых объектов каждый кадр, сотни вызовов <code>fillText</code>, "
               "отрисовка ненужного (за пределами экрана).",
               "Allocating new objects every frame, hundreds of <code>fillText</code> calls, "
               "drawing things that are off-screen.")),
        box("purple", ("Qanday o'lchanadi", "Как измерить", "How to measure"),
            p=("Stendda <b>kadr vaqti grafigi</b> bor. Yashil zona — 16 ms ichida. "
               "Qizil chiziqlar — kechikkan kadrlar. Zarralar sonini oshirib, "
               "grafik qizarishini ko'ring.",
               "На стенде есть <b>график времени кадра</b>. Зелёная зона — внутри 16 мс. "
               "Красные полосы — просевшие кадры. Увеличьте число частиц и посмотрите, "
               "как график краснеет.",
               "The lab has a <b>frame-time graph</b>. Green zone — within 16 ms. "
               "Red bars — dropped frames. Raise the particle count and watch the graph "
               "turn red.")),
    ]) + "\n</div>",
))

S.append(slide(
    ph=("Amaliyot", "Практика", "Practice"), time="33–43",
    eyebrow=("Laboratoriya · 10 daqiqa", "Лаборатория · 10 минут", "Lab · 10 minutes"),
    title=("4 ta sinov: lab/index.html ni oching",
           "4 испытания: откройте lab/index.html",
           "4 trials: open lab/index.html"),
    body='<div class="cols c4">\n' + "\n".join([
        box("accent", ("1 · Delta Time isboti", "1 · Доказать Delta Time", "1 · Prove Delta Time"),
            p=("FPS ni <b>15</b> ga tushiring. <b>dt: O'CHIQ</b> da qahramon sekinlashadi. "
               "<b>dt: YONIQ</b> da — tezlik o'zgarmaydi. Ikkala o'lchovni yozing.",
               "Опустите FPS до <b>15</b>. При <b>dt: ВЫКЛ</b> герой замедлится. "
               "При <b>dt: ВКЛ</b> скорость не изменится. Запишите оба замера.",
               "Drop FPS to <b>15</b>. With <b>dt: OFF</b> the hero slows down. "
               "With <b>dt: ON</b> the speed holds. Record both measurements.")),
        box("purple", ("2 · Hitbox", "2 · Хитбокс", "2 · Hitbox"),
            p=("<b>Hitbox</b> ni yoqing. Qahramonni to'pga sekin yaqinlashtiring va "
               "to'qnashuv <b>aynan qachon</b> qayd etilishini kuzating.",
               "Включите <b>Hitbox</b>. Медленно подведите героя к шару и заметьте, "
               "<b>в какой именно момент</b> засчитывается столкновение.",
               "Turn on <b>Hitbox</b>. Ease the hero towards the ball and watch "
               "<b>exactly when</b> the collision registers.")),
        box("green", ("3 · Oy effekti", "3 · Лунный эффект", "3 · Moon effect"),
            p=("<b>Gravitatsiya</b> ni 300 gacha tushiring, <b>Sakrash</b> ni o'zgartirmang. "
               "Sakrash balandligi qanday o'zgardi? Sababini yozing.",
               "Опустите <b>Гравитацию</b> до 300, <b>Прыжок</b> не трогайте. "
               "Как изменилась высота прыжка? Запишите причину.",
               "Lower <b>Gravity</b> to 300, leave <b>Jump</b> alone. "
               "How did the jump height change? Write down why.")),
        box("", ("4 · FPS byudjeti", "4 · Бюджет FPS", "4 · The FPS budget"),
            p=("<b>Zarralar</b> slayderini oshiring. Kadr vaqti <b>16 ms dan oshgan</b> "
               "nuqtadagi zarralar sonini toping va yozing.",
               "Увеличивайте слайдер <b>Частицы</b>. Найдите и запишите число частиц, "
               "при котором кадр <b>превысил 16 мс</b>.",
               "Raise the <b>Particles</b> slider. Find and note the particle count at "
               "which the frame time <b>crosses 16 ms</b>.")),
    ]) + "\n</div>",
))

S.append(slide(
    ph=("AI yordamchi", "AI помощник", "AI helper"), time="43–44",
    eyebrow=("Tayyor promptlar", "Готовые промпты", "Ready-made prompts"),
    title=("AI bilan dvigatelni tushunish",
           "Разобраться в движке с помощью AI",
           "Use AI to understand the engine"),
    body='<div class="cols c2">\n'
         + box("purple", ("Nusxa oling", "Скопируйте", "Copy these"),
               extra_html=code(
                   "1) Объясни разницу между setInterval и\n"
                   "   requestAnimationFrame для игрового цикла.\n"
                   "   Приведи пример, когда setInterval ломает игру.\n\n"
                   "2) У меня hero.x += 5 в игровом цикле. Перепиши\n"
                   "   через delta time так, чтобы скорость была\n"
                   "   300 пикселей в секунду. Объясни каждую строку.\n\n"
                   "3) Напиши функцию AABB-столкновения двух\n"
                   "   прямоугольников на JavaScript и объясни,\n"
                   "   почему нужны именно 4 сравнения."))
         + "\n"
         + box("accent", ("Javobni qanday tekshirasiz",
                          "Как проверить ответ", "How to verify the answer"),
               items=[
                   ("AI bergan <code>dt</code> kodini stenddagi qiymatlar bilan solishtiring "
                    "— raqamlar mos kelishi kerak.",
                    "Сравните код <code>dt</code> от AI со значениями на стенде — "
                    "числа должны совпасть.",
                    "Compare the AI's <code>dt</code> code with the lab's values — "
                    "the numbers must match."),
                   ("AI ba'zan <code>dt</code> ni millisekundda qoldiradi (1000 ga bo'lishni "
                    "unutadi) — bu <b>klassik xato</b>. Tekshiring!",
                    "AI иногда оставляет <code>dt</code> в миллисекундах (забывает делить "
                    "на 1000) — это <b>классическая ошибка</b>. Проверяйте!",
                    "The AI sometimes leaves <code>dt</code> in milliseconds (forgets the "
                    "/1000) — a <b>classic bug</b>. Check it!"),
                   ("\"Ishlaydi\" degani \"to'g'ri\" degani emas. O'lchang.",
                    "«Работает» не значит «правильно». Измеряйте.",
                    "\"It works\" is not \"it is correct\". Measure it."),
               ])
         + "\n</div>",
))

S.append(slide(
    ph=("Yakun", "Итоги", "Summary"), time="44–45",
    eyebrow=("Uy vazifasi va baholash", "Домашнее задание и оценка", "Homework and grading"),
    title=("Uy vazifasi: dvigatel o'lchovlari hisoboti (10 ball)",
           "Домашнее задание: отчёт об измерениях движка (10 баллов)",
           "Homework: engine measurement report (10 points)"),
    body='<div class="cols c2">\n'
         + box("green", ("Nima qilish kerak", "Что нужно сделать", "What to do"),
               items=[
                   ("Varaqadagi 4 sinov jadvalini to'liq to'ldiring.",
                    "Полностью заполните таблицу 4 испытаний в рабочем листе.",
                    "Fill the 4-trial table on the worksheet completely."),
                   ("O'yin tsiklining 3 qadamini <b>o'z so'zingiz bilan</b> yozing.",
                    "Опишите 3 шага игрового цикла <b>своими словами</b>.",
                    "Describe the 3 steps of the game loop <b>in your own words</b>."),
                   ("Delta Time nima uchun kerakligini <b>bitta gap</b> bilan tushuntiring.",
                    "Объясните <b>одним предложением</b>, зачем нужен Delta Time.",
                    "Explain in <b>one sentence</b> why Delta Time is needed."),
                   ("Keyingi dars uchun: o'z arkadangiz uchun <b>g'oya</b> yozing "
                    "(nomi, qahramon, maqsad).",
                    "К следующему уроку: запишите <b>идею</b> своей аркады "
                    "(название, герой, цель).",
                    "For next lesson: write your arcade <b>concept</b> "
                    "(name, hero, goal)."),
               ])
         + "\n"
         + box("accent", ("Baholash mezoni", "Критерии оценки", "Grading rubric"),
               extra_html='<ul class="plain">\n'
               + '  <li><span class="t" %s>4 sinov jadvali (raqamlar bilan) — <b>4 ball</b></span></li>\n'
               % i18n("4 sinov jadvali (raqamlar bilan) — <b>4 ball</b>",
                      "Таблица 4 испытаний (с числами) — <b>4 балла</b>",
                      "Table of 4 trials (with numbers) — <b>4 points</b>")
               + '  <li><span class="t" %s>O\'yin tsiklining 3 qadami — <b>2 ball</b></span></li>\n'
               % i18n("O'yin tsiklining 3 qadami — <b>2 ball</b>",
                      "3 шага игрового цикла — <b>2 балла</b>",
                      "The 3 steps of the game loop — <b>2 points</b>")
               + '  <li><span class="t" %s>Delta Time izohi — <b>2 ball</b></span></li>\n'
               % i18n("Delta Time izohi — <b>2 ball</b>",
                      "Объяснение Delta Time — <b>2 балла</b>",
                      "Delta Time explanation — <b>2 points</b>")
               + '  <li><span class="t" %s>Arkada g\'oyasi — <b>2 ball</b></span></li>\n'
               % i18n("Arkada g'oyasi — <b>2 ball</b>",
                      "Идея аркады — <b>2 балла</b>",
                      "Arcade concept — <b>2 points</b>")
               + "</ul>")
         + "\n</div>",
))


NOTES = {
    "uz": [
        ["Titul slayd",
         "Salom, muhandislar! Shu paytgacha sizning o'yinlaringiz tugma bosishdan iborat edi. Bugun biz DOM ni tashlab, haqiqiy o'yin dvigatelini ochamiz: Canvas, 60 FPS, gravitatsiya va to'qnashuvlar.",
         "lab/index.html ni proyektorda oldindan oching."],
        ["DOM ning chegarasi",
         "Metaforani aniq ayting: DOM — magnit doska, brauzer har bir magnitni eslab turadi. Canvas — oddiy doska, har kadrda o'chirib qaytadan chizasiz. Shuning uchun tez.",
         "Bolalardan so'rash: nega 1000 ta div sekin ishlaydi?"],
        ["Canvas asoslari",
         "Ikkita obyekt: cv va ctx. Eng muhim ogohlantirish — koordinata tizimi. Y pastga o'sadi! Doskada o'q chizib ko'rsating, aks holda sakrash mantig'i chalkashadi.",
         "Doskada koordinata o'qlarini chizish: (0,0) yuqori chapda."],
        ["O'yin tsikli",
         "Uchta qadamni ajrating: CLEAR, UPDATE, DRAW. Eng muhim professional qoida — update ichida chizmaslik, draw ichida hisoblamaslik. Bu kelajakdagi barcha kodlariga taalluqli.",
         "Stendda CLEAR ni o'chirib, iz qolishini ko'rsatish."],
        ["RAF va setInterval",
         "Ikki ustunni solishtiring. Keyin tuzoqni ayting: RAF turli kompyuterda turli tezlikda ishlaydi — demak o'yin ham. Bu keyingi slaydga ko'prik.",
         "Fon vkladkasida setInterval ishlashda davom etishini aytish."],
        ["Delta Time — darsning cho'qqisi",
         "Eng muhim slayd. Ikki kod blokini yonma-yon ko'rsating. Keyin stendda jonli isbotlang: FPS 15, dt o'chiq — qahramon sudraladi; dt yoniq — tezlik o'zgarmaydi. Bolalar buni ko'rishi shart.",
         "Stendda FPS 15 va dt tugmasi bilan jonli demo. 2-3 marta takrorlang."],
        ["Fizika uchta qator",
         "Bu fizika darsidagi formulaning aynan o'zi ekanini ayting — a→v→s. Bolalar 'fizika kerak emas' deb o'ylaydi, mana bu yerda kerak bo'ldi.",
         "Gravitatsiya slayderini surib, oy effektini ko'rsatish."],
        ["AABB to'qnashuv",
         "To'rtta taqqoslash. Keyin stendda Hitbox tugmasini yoqing. Bu 'tegmaganday edi, lekin jon ketdi' savolining javobi — bolalar buni o'yinlarda ko'p uchratgan.",
         "Hitbox yoqib, qahramonni to'pga sekin yaqinlashtirish."],
        ["FPS byudjeti",
         "16.6 ms raqamini doskaga yozing. Keyin stenddagi zarralar slayderini oshirib, grafik qizarishini ko'rsating. Optimallashtirish mavhum emas — u o'lchanadi.",
         "Doskaga '16.6 ms' yozish. Zarralarni oshirib grafikni ko'rsatish."],
        ["Amaliyot 10 daqiqa",
         "To'rt sinov. Eng muhimi birinchisi — delta time isboti. Har bir o'quvchi ikkita raqamni o'z ko'zi bilan ko'rishi va yozishi kerak. Sinf bo'ylab yuring.",
         "Har sinovga ~2.5 daqiqa. Raqamlar yozilganini tekshiring."],
        ["AI bilan ishlash",
         "Muhim nuance: AI ko'pincha dt ni 1000 ga bo'lishni unutadi. Bu klassik xato. Bolalarga AI javobini stend qiymatlari bilan solishtirishni o'rgating.",
         "Bitta ekranda AI javobidagi dt ni tekshirish."],
        ["Yakun va baholash",
         "Xulosa: o'yin dvigateli sehr emas — tsikl, delta time, uchta fizika qatori va to'rtta taqqoslash. Varaqalarni yig'ing, uy vazifasini e'lon qiling.",
         "Varaqalarni yig'ish. Keyingi dars — o'z arkadangiz va leaderboard."],
    ],
    "ru": [
        ["Титульный слайд",
         "Привет, инженеры! До сих пор ваши игры состояли из нажатий кнопок. Сегодня мы бросаем DOM и открываем настоящий игровой движок: Canvas, 60 FPS, гравитация и столкновения.",
         "Заранее откройте lab/index.html на проекторе."],
        ["Предел DOM",
         "Чётко озвучьте метафору: DOM — магнитная доска, браузер помнит каждый магнит. Canvas — обычная доска, каждый кадр стираете и рисуете заново. Поэтому быстро.",
         "Спросить у ребят: почему 1000 див тормозят?"],
        ["Основы Canvas",
         "Два объекта: cv и ctx. Самое важное предупреждение — система координат. Y растёт вниз! Нарисуйте оси на доске, иначе логика прыжка запутает.",
         "Нарисовать на доске оси: (0,0) в левом верхнем углу."],
        ["Игровой цикл",
         "Разделите три шага: CLEAR, UPDATE, DRAW. Главное профессиональное правило — не рисовать внутри update и не считать внутри draw. Это касается всего их будущего кода.",
         "Отключить CLEAR на стенде и показать след."],
        ["RAF против setInterval",
         "Сравните две колонки. Затем озвучьте ловушку: RAF на разных компьютерах работает с разной частотой — значит, и игра тоже. Это мостик к следующему слайду.",
         "Сказать, что setInterval продолжает работать в фоновой вкладке."],
        ["Delta Time — вершина урока",
         "Самый важный слайд. Покажите два блока кода рядом. Затем докажите живьём на стенде: FPS 15, dt выкл — герой ползёт; dt вкл — скорость не меняется. Дети обязаны это увидеть.",
         "Живое демо: FPS 15 и кнопка dt. Повторить 2-3 раза."],
        ["Физика в три строки",
         "Скажите, что это ровно та же формула, что на физике — a→v→s. Дети думают «физика не нужна» — вот здесь она понадобилась.",
         "Подвигать слайдер гравитации и показать лунный эффект."],
        ["Столкновения AABB",
         "Четыре сравнения. Затем включите на стенде кнопку Hitbox. Это ответ на вопрос «вроде не задел, а жизнь сняли» — дети часто с этим сталкивались в играх.",
         "Включить Hitbox и медленно подвести героя к шару."],
        ["Бюджет FPS",
         "Напишите на доске число 16.6 мс. Затем увеличьте слайдер частиц и покажите, как краснеет график. Оптимизация не абстрактна — она измеряется.",
         "Написать на доске «16.6 мс». Увеличить частицы и показать график."],
        ["Практика 10 минут",
         "Четыре испытания. Самое важное — первое, доказательство delta time. Каждый ученик должен своими глазами увидеть два числа и записать их. Ходите по классу.",
         "~2.5 минуты на испытание. Проверяйте, что числа записаны."],
        ["Работа с AI",
         "Важный нюанс: AI часто забывает поделить dt на 1000. Это классическая ошибка. Научите детей сверять ответ AI со значениями на стенде.",
         "Проверить dt из ответа AI на одном экране."],
        ["Итоги и оценивание",
         "Вывод: игровой движок не магия — цикл, delta time, три строки физики и четыре сравнения. Соберите листы, объявите домашнее задание.",
         "Собрать листы. Следующий урок — своя аркада и таблица рекордов."],
    ],
    "en": [
        ["Title slide",
         "Hello engineers! Until now your games were button presses. Today we drop the DOM and open a real game engine: Canvas, 60 FPS, gravity and collisions.",
         "Pre-open lab/index.html on the projector."],
        ["The limit of the DOM",
         "State the metaphor clearly: the DOM is a magnet board, the browser remembers every magnet. Canvas is a plain chalkboard, wiped and redrawn each frame. That is why it is fast.",
         "Ask the class: why do 1000 divs lag?"],
        ["Canvas basics",
         "Two objects: cv and ctx. The critical warning is the coordinate system. Y grows downward! Draw the axes on the board or the jump logic will confuse them.",
         "Sketch the axes on the board: (0,0) top-left."],
        ["The game loop",
         "Separate the three steps: CLEAR, UPDATE, DRAW. The key professional rule — never draw inside update, never compute inside draw. This applies to all their future code.",
         "Disable CLEAR on the lab and show the trail."],
        ["RAF vs setInterval",
         "Compare the two columns. Then state the trap: RAF runs at different rates on different machines — so the game does too. That bridges to the next slide.",
         "Mention setInterval keeps running in a background tab."],
        ["Delta Time — the peak of the lesson",
         "The most important slide. Show the two code blocks side by side. Then prove it live: FPS 15, dt off — the hero crawls; dt on — the speed holds. They must see this.",
         "Live demo: FPS 15 and the dt button. Repeat 2-3 times."],
        ["Physics in three lines",
         "Point out this is the exact formula from physics class — a→v→s. Kids think physics is useless; here it just became useful.",
         "Drag the gravity slider and show the moon effect."],
        ["AABB collision",
         "Four comparisons. Then turn on the Hitbox button. This answers 'I did not even touch it but lost a life' — something they have all met in games.",
         "Enable Hitbox and ease the hero towards the ball."],
        ["The FPS budget",
         "Write 16.6 ms on the board. Then raise the particle slider and show the graph turning red. Optimisation is not abstract — it is measured.",
         "Write '16.6 ms' on the board. Raise particles and show the graph."],
        ["Practice, 10 minutes",
         "Four trials. The first one matters most — the delta time proof. Every student must see the two numbers themselves and write them down. Walk the room.",
         "~2.5 minutes per trial. Check the numbers are written."],
        ["Working with AI",
         "An important nuance: the AI often forgets to divide dt by 1000. A classic bug. Teach them to cross-check the AI's answer against the lab's values.",
         "Check the dt from an AI answer on one screen."],
        ["Summary and grading",
         "Conclusion: a game engine is not magic — a loop, delta time, three lines of physics and four comparisons. Collect the sheets, announce the homework.",
         "Collect sheets. Next lesson — your own arcade and a leaderboard."],
    ],
}

VARAQA = (
    sheet_header(
        ("13-dars: Canvas va O'yin Tsikli — RAF, Delta Time va Fizika",
         "Урок 13: Canvas и Игровой Цикл — RAF, Delta Time и Физика",
         "Lesson 13: Canvas and the Game Loop — RAF, Delta Time and Physics"),
        ("Target International School · 7–8-sinf · 3-hafta (1-soat)",
         "Target International School · 7–8 класс · 3-я неделя (1-й час)",
         "Target International School · Grades 7–8 · Week 3 (Hour 1)"))
    + mission(
        ("🎯 Laboratoriya missiyasi: dvigatelni o'lchang",
         "🎯 Лабораторная миссия: измерьте движок",
         "🎯 Lab mission: measure the engine"),
        ("<b>lab/index.html</b> ni oching. Sizning vazifangiz — dvigatel haqida "
         "gapirish emas, uni <b>o'lchash</b>. Har bir sinovda aniq raqam yozing: "
         "piksel/soniya, millisekund, zarralar soni. Raqamsiz javob qabul qilinmaydi.",
         "Откройте <b>lab/index.html</b>. Ваша задача — не рассуждать о движке, "
         "а <b>измерить</b> его. В каждом испытании запишите конкретное число: "
         "пиксели/секунду, миллисекунды, количество частиц. Ответ без числа не принимается.",
         "Open <b>lab/index.html</b>. Your job is not to talk about the engine but to "
         "<b>measure</b> it. Every trial needs a concrete number: pixels/second, "
         "milliseconds, particle count. An answer without a number is not accepted."))
    + table(
        [("Sinov", "Испытание", "Trial"),
         ("Sozlama", "Настройка", "Setting"),
         ("O'lchov natijasi", "Результат замера", "Measured result"),
         ("Xulosa", "Вывод", "Conclusion")],
        [[("1 · Delta Time", "1 · Delta Time", "1 · Delta Time"),
          ("FPS = 15, dt: O'CHIQ → keyin dt: YONIQ",
           "FPS = 15, dt: ВЫКЛ → затем dt: ВКЛ",
           "FPS = 15, dt: OFF → then dt: ON"),
          ("dt o'chiq: ____ px/s\ndt yoniq: ____ px/s",
           "dt выкл: ____ px/s\ndt вкл: ____ px/s",
           "dt off: ____ px/s\ndt on: ____ px/s"), None],
         [("2 · Hitbox (AABB)", "2 · Хитбокс (AABB)", "2 · Hitbox (AABB)"),
          ("Hitbox yoqilgan, qahramonni to'pga yaqinlashtirish",
           "Хитбокс включён, подвести героя к шару",
           "Hitbox on, ease the hero towards the ball"),
          ("Hitbox rasmdan katta / kichik / teng\n(keraksizini o'chiring)",
           "Хитбокс больше / меньше / равен картинке\n(ненужное зачеркнуть)",
           "Hitbox is bigger / smaller / equal to the sprite\n(cross out what does not apply)"), None],
         [("3 · Oy effekti", "3 · Лунный эффект", "3 · Moon effect"),
          ("Gravitatsiya 1600 → 300, Sakrash o'zgarmaydi",
           "Гравитация 1600 → 300, Прыжок не меняем",
           "Gravity 1600 → 300, Jump unchanged"),
          ("Balandlik: ____ px → ____ px",
           "Высота: ____ px → ____ px",
           "Height: ____ px → ____ px"), None],
         [("4 · FPS byudjeti", "4 · Бюджет FPS", "4 · FPS budget"),
          ("Zarralarni oshirib, kadr vaqtini kuzatish",
           "Увеличивать частицы, следя за временем кадра",
           "Raise particles, watch the frame time"),
          ("16 ms dan oshgan nuqta: ____ ta zarra",
           "Превысило 16 мс при: ____ частиц",
           "Crossed 16 ms at: ____ particles"), None]])
    + '    <div class="rubric-grid">\n'
    + sheet_box(
        ("✏️ Nazariya: o'z so'zingiz bilan",
         "✏️ Теория: своими словами",
         "✏️ Theory: in your own words"),
        writelines(3, ("O'yin tsiklining 3 qadami va har birida nima bo'ladi:",
                       "3 шага игрового цикла и что происходит в каждом:",
                       "The 3 steps of the game loop and what each one does:"))
        + "\n"
        + writelines(2, ("Delta Time nega kerak? (bitta gap)",
                         "Зачем нужен Delta Time? (одно предложение)",
                         "Why is Delta Time needed? (one sentence)")))
    + "\n"
    + sheet_box(
        ("📊 Baholash mezoni (10 ball)",
         "📊 Критерии оценки (10 баллов)",
         "📊 Grading rubric (10 points)"),
        rubric([
            (("4 sinov jadvali raqamlar bilan", "Таблица 4 испытаний с числами",
              "4-trial table with numbers"), "4"),
            (("O'yin tsiklining 3 qadami", "3 шага игрового цикла",
              "The 3 game-loop steps"), "2"),
            (("Delta Time izohi", "Объяснение Delta Time", "Delta Time explanation"), "2"),
            (("Arkada g'oyasi (nom, qahramon, maqsad)",
              "Идея аркады (название, герой, цель)",
              "Arcade concept (name, hero, goal)"), "2"),
        ], "10")
        + "\n"
        + writelines(2, ("🎮 Keyingi dars uchun arkada g'oyam:",
                         "🎮 Моя идея аркады к следующему уроку:",
                         "🎮 My arcade concept for next lesson:")))
    + "\n    </div>\n  </div>\n"
    + sign_box()
)

if __name__ == "__main__":
    print(Lesson(D, TITLES, SHEET_TITLES, "vc-notes-7-13", S, NOTES, VARAQA).build())
