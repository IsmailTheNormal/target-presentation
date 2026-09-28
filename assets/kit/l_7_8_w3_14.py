# -*- coding: utf-8 -*-
"""7-8-sinf · 3-hafta · 14-dars — Dushmanlar, Ochko va Leaderboard: JSON, sort, halollik."""

import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from build import (Lesson, slide, title_slide, box, code, el, i18n,
                   sheet_header, mission, table, sheet_box, rubric, writelines, sign_box)

D = "classes/7-8-sinf/3-hafta/14-dars-dushmanlar-ochko-va-leaderboard"

TITLES = {
    "uz": "14-dars: Dushmanlar, Ochko va Leaderboard — JSON, Sort va Halollik",
    "ru": "Урок 14: Враги, Очки и Таблица Рекордов — JSON, Сортировка и Честность",
    "en": "Lesson 14: Enemies, Score and Leaderboard — JSON, Sorting and Fair Play",
}
SHEET_TITLES = {k: v + (" — Ish Varaqasi" if k == "uz" else
                        " — Рабочий Лист" if k == "ru" else " — Worksheet")
                for k, v in TITLES.items()}

S = []

S.append(title_slide(
    ph=("Kirish", "Введение", "Intro"), time="0–3",
    eyebrow=("Vibecoding · 14-dars · 7–8-sinflar",
             "Vibecoding · Урок 14 · 7–8 классы",
             "Vibecoding · Lesson 14 · Grades 7–8"),
    h1=("Dushmanlar, Ochko va Leaderboard: Dvigateldan O'yingacha",
        "Враги, Очки и Таблица Рекордов: От Движка к Игре",
        "Enemies, Score and Leaderboard: From Engine to Game"),
    lede=("O'tgan darsda siz <b>dvigatel</b> qurdingiz: tsikl, delta time, fizika, "
          "to'qnashuv. Lekin dvigatel — bu hali o'yin emas. O'yin bo'lishi uchun "
          "<b>maqsad</b>, <b>xavf</b> va <b>natija</b> kerak. Bugun biz ochko tizimini, "
          "dushman to'lqinlarini va sinf <b>reyting jadvalini</b> quramiz — "
          "hamda nega ochkoga ishonib bo'lmasligini bilib olamiz.",
          "На прошлом уроке вы построили <b>движок</b>: цикл, delta time, физика, "
          "столкновения. Но движок — это ещё не игра. Чтобы получилась игра, нужны "
          "<b>цель</b>, <b>риск</b> и <b>результат</b>. Сегодня мы соберём систему очков, "
          "волны врагов и классную <b>таблицу рекордов</b> — "
          "и узнаем, почему очкам нельзя верить.",
          "Last lesson you built an <b>engine</b>: loop, delta time, physics, collisions. "
          "But an engine is not yet a game. A game needs a <b>goal</b>, a <b>risk</b> and "
          "a <b>result</b>. Today we build the scoring system, enemy waves and a class "
          "<b>leaderboard</b> — and learn why a score can never be trusted."),
    meta=[("<b>Fan:</b> Vibecoding · O'yin va ma'lumot",
           "<b>Предмет:</b> Vibecoding · Игра и данные",
           "<b>Subject:</b> Vibecoding · Game and Data"),
          ("<b>Kohorta:</b> 7–8-sinf", "<b>Когорта:</b> 7–8 класс", "<b>Cohort:</b> Grades 7–8"),
          ("<b>Hafta:</b> 3 (2-soat)", "<b>Неделя:</b> 3 (2-й час)", "<b>Week:</b> 3 (Hour 2)")],
))

S.append(slide(
    ph=("O'yin dizayni", "Геймдизайн", "Game design"), time="3–7",
    eyebrow=("Dvigatel ≠ o'yin", "Движок ≠ игра", "Engine ≠ game"),
    title=("Harakatlanadigan kvadrat — bu hali o'yin emas",
           "Движущийся квадрат — это ещё не игра",
           "A moving square is not yet a game"),
    body='<div class="cols c3">\n' + "\n".join([
        box("purple", ("1 · MAQSAD", "1 · ЦЕЛЬ", "1 · A GOAL"),
            p=("O'yinchi <b>nima uchun</b> harakat qiladi? Ochko yig'ish, omon qolish, "
               "rekord o'rnatish. Maqsadsiz o'yin — bu ekran saqlagich.",
               "<b>Ради чего</b> игрок двигается? Набрать очки, выжить, поставить рекорд. "
               "Игра без цели — это заставка.",
               "<b>Why</b> does the player move? To score, to survive, to beat a record. "
               "A game with no goal is a screensaver.")),
        box("accent", ("2 · XAVF", "2 · РИСК", "2 · A RISK"),
            p=("Yutqazish <b>mumkin</b> bo'lishi shart. Yutqazib bo'lmaydigan o'yinda "
               "g'alabaning qiymati yo'q. Xavf — bu ochkoning narxi.",
               "Проигрыш должен быть <b>возможен</b>. Там, где нельзя проиграть, "
               "победа ничего не стоит. Риск — это цена очков.",
               "Losing must be <b>possible</b>. Where you cannot lose, winning is worth "
               "nothing. Risk is the price of points.")),
        box("green", ("3 · NATIJA", "3 · РЕЗУЛЬТАТ", "3 · A RESULT"),
            p=("O'yin tugagach <b>raqam</b> qolishi kerak — va uni boshqalar bilan "
               "solishtirish mumkin bo'lsin. Mana shuning uchun leaderboard bor.",
               "После игры должно остаться <b>число</b> — и его можно сравнить с другими. "
               "Именно для этого существует таблица рекордов.",
               "When the game ends a <b>number</b> must remain — and it must be comparable "
               "with others. That is exactly what a leaderboard is for.")),
    ]) + "\n</div>\n"
         + box("", ("Bugungi darsning tuzilishi", "Структура сегодняшнего урока",
                    "How today is structured"),
               p=("Uchala element bugun quriladi: <b>ochko</b> (maqsad), "
                  "<b>dushman to'lqinlari</b> (xavf) va <b>reyting jadvali</b> (natija). "
                  "Dars oxirida sinfda bitta umumiy jadval bo'ladi va siz undagi "
                  "o'rningizni ko'rasiz.",
                  "Сегодня строим все три: <b>очки</b> (цель), <b>волны врагов</b> (риск) "
                  "и <b>таблицу рекордов</b> (результат). В конце урока в классе будет "
                  "одна общая таблица, и вы увидите своё место в ней.",
                  "All three get built today: <b>score</b> (goal), <b>enemy waves</b> (risk) "
                  "and a <b>leaderboard</b> (result). By the end the class has one shared "
                  "table and you will see your place in it.")),
))

S.append(slide(
    ph=("Ochko", "Очки", "Score"), time="7–11",
    eyebrow=("Teskari aloqa halqasi", "Петля обратной связи", "The feedback loop"),
    title=("Ochko — bu mukofot emas, bu <b>xabar</b>",
           "Очки — это не награда, это <b>сообщение</b>",
           "Score is not a reward, it is a <b>message</b>"),
    body='<div class="cols c2">\n'
         + box("green", ("Ochko o'yinchiga nima deydi",
                         "Что очки говорят игроку", "What the score tells the player"),
               items=[
                   ("<b>\"To'g'ri qilding\"</b> — ochko o'sganda o'yinchi qaysi harakat "
                    "foydali ekanini tushunadi.",
                    "<b>«Ты сделал правильно»</b> — когда счёт растёт, игрок понимает, "
                    "какое действие полезно.",
                    "<b>\"That was right\"</b> — when the score rises the player learns "
                    "which action pays off."),
                   ("<b>\"Xavf arziydi\"</b> — qiyinroq dushman ko'proq ochko bersa, "
                    "o'yinchi xavfni tanlaydi. Bu qiziqarli qaror.",
                    "<b>«Риск того стоит»</b> — если сложный враг даёт больше очков, "
                    "игрок выбирает риск. Это интересное решение.",
                    "<b>\"The risk pays\"</b> — if a harder enemy gives more points the "
                    "player chooses risk. That is an interesting decision."),
                   ("<b>\"Yaxshiroq bo'lyapsan\"</b> — o'z rekordini urish — "
                    "eng kuchli motivatsiya.",
                    "<b>«Ты становишься лучше»</b> — побить свой рекорд — "
                    "самая сильная мотивация.",
                    "<b>\"You are improving\"</b> — beating your own record is the "
                    "strongest motivator."),
               ])
         + "\n"
         + box("accent", ("Kombo: oddiy, lekin kuchli",
                          "Комбо: просто, но мощно", "Combo: simple but powerful"),
               extra_html=code(
                   "// Ketma-ket urish kombo beradi\n"
                   "kombo = kombo + 1;\n"
                   "ochko = ochko + 10 * kombo;\n\n"
                   "// Xato qilsa — kombo nolga tushadi\n"
                   "if (jarohat) kombo = 0;\n\n"
                   "// 5 ta ketma-ket: 10+20+30+40+50 = 150\n"
                   "// 5 ta uzilib:    10+10+10+10+10 = 50"))
         + "\n</div>\n"
         + box("purple", ("Nega kombo o'yinni o'zgartiradi",
                          "Почему комбо меняет игру", "Why combo changes the game"),
               p=("Kombosiz o'yinchi <b>ehtiyotkor</b> o'ynaydi. Kombo bilan u "
                  "<b>tavakkal qiladi</b> — chunki uzilish og'riqli. Bitta qator kod "
                  "o'yinchining butun xulq-atvorini o'zgartiradi. Mana bu — dizayn.",
                  "Без комбо игрок играет <b>осторожно</b>. С комбо он <b>рискует</b> — "
                  "потому что обрыв болезненный. Одна строка кода меняет всё поведение "
                  "игрока. Вот это и есть дизайн.",
                  "Without combo a player plays it <b>safe</b>. With combo they <b>take "
                  "risks</b> — because breaking it hurts. One line of code changes the "
                  "player's entire behaviour. That is design.")),
))

S.append(slide(
    ph=("To'lqinlar", "Волны", "Waves"), time="11–15",
    eyebrow=("Qiyinlik egri chizig'i", "Кривая сложности", "The difficulty curve"),
    title=("Dushmanlar to'lqin bo'lib keladi va asta kuchayadi",
           "Враги приходят волнами и постепенно усиливаются",
           "Enemies come in waves and ramp up"),
    body='<div class="cols c2">\n'
         + box("purple", ("Spawn — dushman qayerdan paydo bo'ladi",
                          "Spawn — откуда берутся враги", "Spawn — where enemies come from"),
               extra_html=code(
                   "// Har N soniyada yangi dushman\n"
                   "spawnTaymer -= dt;\n"
                   "if (spawnTaymer <= 0){\n"
                   "  dushmanlar.push(yangiDushman());\n"
                   "  spawnTaymer = spawnOraligi;\n"
                   "}\n\n"
                   "// To'lqin o'sgani sayin oraliq qisqaradi\n"
                   "spawnOraligi = 2.0 - tolqin * 0.15;\n"
                   "if (spawnOraligi < 0.4) spawnOraligi = 0.4;"))
         + "\n"
         + box("accent", ("Qiyinlikni oshirishning 3 yo'li",
                          "3 способа повысить сложность", "3 ways to raise difficulty"),
               items=[
                   ("<b>Ko'proq</b> dushman — eng oddiy, lekin tez zeriktiradi.",
                    "<b>Больше</b> врагов — самое простое, но быстро надоедает.",
                    "<b>More</b> enemies — simplest, but gets boring fast."),
                   ("<b>Tezroq</b> dushman — yaxshiroq, reaksiyani sinaydi.",
                    "<b>Быстрее</b> враги — лучше, проверяет реакцию.",
                    "<b>Faster</b> enemies — better, it tests reaction."),
                   ("<b>Boshqacha</b> dushman — eng yaxshi: yangi xulq, yangi strategiya "
                    "kerak bo'ladi.",
                    "<b>Другие</b> враги — лучше всего: новое поведение требует новой "
                    "стратегии.",
                    "<b>Different</b> enemies — best of all: new behaviour demands a new "
                    "strategy."),
                   ("Eng yomon usul: dushmanga <b>ko'p jon</b> berish. Bu qiyin emas, "
                    "bu uzoq va zerikarli.",
                    "Худший способ: дать врагу <b>много здоровья</b>. Это не сложно, "
                    "это долго и скучно.",
                    "The worst approach: giving enemies <b>more health</b>. That is not "
                    "hard, it is just long and dull."),
               ])
         + "\n</div>\n"
         + box("green", ("🎮 Stendda", "🎮 На стенде", "🎮 On the lab"),
               p=("Stendda har <b>15 soniyada</b> yangi to'lqin boshlanadi: dushman "
                  "tezligi oshadi va oraliq qisqaradi. Yuqorida joriy to'lqin raqami "
                  "ko'rsatiladi. Necha to'lqingacha yetganingizni varaqaga yozing.",
                  "На стенде каждые <b>15 секунд</b> начинается новая волна: скорость "
                  "врагов растёт, интервал сокращается. Сверху показан номер текущей "
                  "волны. Запишите в лист, до какой волны вы дошли.",
                  "On the lab a new wave starts every <b>15 seconds</b>: enemies speed up "
                  "and the interval shrinks. The current wave number shows at the top. "
                  "Write down how far you got.")),
))

S.append(slide(
    ph=("Holatlar", "Состояния", "States"), time="15–18",
    eyebrow=("O'yin holat mashinasi", "Машина состояний игры", "The game state machine"),
    title=("O'yinda uchta ekran bor — va ular chalkashmasligi kerak",
           "В игре три экрана — и они не должны путаться",
           "A game has three screens — and they must not mix"),
    body='<div class="cols c3">\n' + "\n".join([
        box("", ("MENU", "MENU", "MENU"),
            p=("Ism kiritiladi, boshlash tugmasi. O'yin tsikli ishlaydi, lekin "
               "<code>update</code> qahramonni qimirlatmaydi.",
               "Ввод имени, кнопка старта. Игровой цикл работает, но "
               "<code>update</code> не двигает героя.",
               "Name entry, start button. The loop runs, but <code>update</code> "
               "does not move the hero.")),
        box("green", ("PLAYING", "PLAYING", "PLAYING"),
            p=("Asosiy holat: fizika, dushmanlar, ochko, to'lqinlar. Klaviatura "
               "qahramonni boshqaradi.",
               "Основное состояние: физика, враги, очки, волны. Клавиатура "
               "управляет героем.",
               "The main state: physics, enemies, score, waves. The keyboard "
               "drives the hero.")),
        box("accent", ("GAME OVER", "GAME OVER", "GAME OVER"),
            p=("Yakuniy ochko ko'rsatiladi, rekord saqlanadi, leaderboard yangilanadi. "
               "<code>Space</code> — qaytadan.",
               "Показывается финальный счёт, рекорд сохраняется, таблица обновляется. "
               "<code>Space</code> — заново.",
               "The final score shows, the record saves, the leaderboard refreshes. "
               "<code>Space</code> — restart.")),
    ]) + "\n</div>\n"
         + box("purple", ("Nega bu muhim", "Почему это важно", "Why it matters"),
               extra_html=code(
                   "function update(dt){\n"
                   "  if (holat === 'MENU')      return;          // hech narsa qilmaydi\n"
                   "  if (holat === 'GAMEOVER')  return;\n"
                   "  // faqat shu yerdan pastda o'yin mantig'i\n"
                   "  qahramonniYangila(dt);\n"
                   "  dushmanlarniYangila(dt);\n"
                   "}\n\n"
                   "// Holatni tekshirmasangiz: GAME OVER ekranida\n"
                   "// dushmanlar harakatda qoladi va ochko o'sishda davom etadi.")),
))

S.append(slide(
    ph=("JSON", "JSON", "JSON"), time="18–23",
    eyebrow=("Ma'lumotni saqlash tili", "Язык хранения данных", "The language of stored data"),
    title=("JSON — obyektni matnga, matnni obyektga",
           "JSON — объект в текст, текст в объект",
           "JSON — object to text, text to object"),
    body='<div class="cols c2">\n'
         + box("green", ("Ikkita funksiya — hammasi shu",
                         "Две функции — и это всё", "Two functions — that is all"),
               extra_html=code(
                   "var natija = { ism:'Aziz', ochko:1240, tolqin:7 };\n\n"
                   "// Obyekt -> matn (saqlash uchun)\n"
                   "var matn = JSON.stringify(natija);\n"
                   "// '{\"ism\":\"Aziz\",\"ochko\":1240,\"tolqin\":7}'\n\n"
                   "// Matn -> obyekt (o'qish uchun)\n"
                   "var qayta = JSON.parse(matn);\n"
                   "qayta.ochko + 10;   // 1250 — bu yana son!"))
         + "\n"
         + box("accent", ("Nega matnga aylantirish kerak",
                          "Зачем превращать в текст", "Why turn it into text"),
               items=[
                   ("<code>localStorage</code> faqat <b>matn</b> saqlaydi — obyektni "
                    "to'g'ridan-to'g'ri qo'ysangiz <code>[object Object]</code> chiqadi.",
                    "<code>localStorage</code> хранит только <b>текст</b> — положите объект "
                    "напрямую и получите <code>[object Object]</code>.",
                    "<code>localStorage</code> stores only <b>text</b> — put an object in "
                    "directly and you get <code>[object Object]</code>."),
                   ("Tarmoq bo'ylab ham faqat matn uzatiladi. Server JSON qabul qiladi.",
                    "По сети тоже передаётся только текст. Сервер принимает JSON.",
                    "Networks also carry only text. Servers accept JSON."),
                   ("JSON — <b>barcha tillar</b> tushunadigan format: Python, Java, "
                    "PHP, Swift.",
                    "JSON понимают <b>все языки</b>: Python, Java, PHP, Swift.",
                    "JSON is understood by <b>every language</b>: Python, Java, PHP, Swift."),
               ])
         + "\n</div>\n"
         + box("purple", ("⚠️ Eng ko'p uchraydigan xato",
                          "⚠️ Самая частая ошибка", "⚠️ The most common mistake"),
               extra_html=code(
                   "// ❌ parse ni unutish\n"
                   "var reyting = localStorage.getItem('top');\n"
                   "reyting.push(yangi);   // XATO: bu matn, massiv emas!\n\n"
                   "// ✅ To'g'ri\n"
                   "var reyting = JSON.parse(localStorage.getItem('top') || '[]');\n"
                   "reyting.push(yangi);\n"
                   "localStorage.setItem('top', JSON.stringify(reyting));")),
))

S.append(slide(
    ph=("Leaderboard", "Таблица рекордов", "Leaderboard"), time="23–27",
    eyebrow=("Massiv, sort, top-10", "Массив, сортировка, топ-10", "Array, sort, top-10"),
    title=("Reyting jadvali — uchta amaldan iborat",
           "Таблица рекордов — это три операции",
           "A leaderboard is three operations"),
    body='<div class="cols c2">\n'
         + box("green", ("Uchta amal", "Три операции", "Three operations"),
               extra_html=code(
                   "// 1. Qo'shish\n"
                   "reyting.push({ ism:ism, ochko:ochko, sana:Date.now() });\n\n"
                   "// 2. Saralash — kattadan kichikka\n"
                   "reyting.sort(function(a, b){\n"
                   "  return b.ochko - a.ochko;\n"
                   "});\n\n"
                   "// 3. Faqat top-10 ni qoldirish\n"
                   "reyting = reyting.slice(0, 10);"))
         + "\n"
         + box("accent", ("sort() ni tushunish", "Разобраться с sort()", "Understanding sort()"),
               items=[
                   ("<code>sort</code> ga <b>taqqoslash funksiyasi</b> beriladi: "
                    "u ikkita elementni oladi va son qaytaradi.",
                    "В <code>sort</code> передаётся <b>функция сравнения</b>: "
                    "она берёт два элемента и возвращает число.",
                    "<code>sort</code> takes a <b>comparator</b>: it receives two items "
                    "and returns a number."),
                   ("<code>b.ochko - a.ochko</code> → <b>kamayish</b> (katta birinchi). "
                    "<code>a.ochko - b.ochko</code> → o'sish.",
                    "<code>b.ochko - a.ochko</code> → <b>по убыванию</b> (большие первые). "
                    "<code>a.ochko - b.ochko</code> → по возрастанию.",
                    "<code>b.ochko - a.ochko</code> → <b>descending</b> (highest first). "
                    "<code>a.ochko - b.ochko</code> → ascending."),
                   ("⚠️ Funksiyasiz <code>sort()</code> sonlarni <b>matn sifatida</b> "
                    "saralaydi: <code>[100, 9, 80]</code> → <code>[100, 80, 9]</code>. "
                    "Klassik tuzoq!",
                    "⚠️ Без функции <code>sort()</code> сортирует числа <b>как текст</b>: "
                    "<code>[100, 9, 80]</code> → <code>[100, 80, 9]</code>. "
                    "Классическая ловушка!",
                    "⚠️ Without a comparator <code>sort()</code> sorts numbers <b>as "
                    "text</b>: <code>[100, 9, 80]</code> → <code>[100, 80, 9]</code>. "
                    "A classic trap!"),
               ])
         + "\n</div>",
))

S.append(slide(
    ph=("Halollik", "Честность", "Fair play"), time="27–33",
    eyebrow=("Darsning eng muhim g'oyasi",
             "Главная идея урока", "The key idea of the lesson"),
    title=("Mijoz tomonidan kelgan ochkoga <b>hech qachon</b> ishonmang",
           "<b>Никогда</b> не верьте очкам, пришедшим от клиента",
           "<b>Never</b> trust a score that comes from the client"),
    body='<div class="cols c2">\n'
         + box("accent", ("Buzish qanchalik oson", "Насколько легко сжульничать",
                          "How easy cheating is"),
               extra_html=code(
                   "// Brauzerda F12 -> Console va bitta qator:\n"
                   "localStorage.setItem('top',\n"
                   "  JSON.stringify([{ism:'Men', ochko:999999}]));\n\n"
                   "// Yoki to'g'ridan-to'g'ri o'zgaruvchiga:\n"
                   "ochko = 999999;\n\n"
                   "// Tamom. Rekord \"o'rnatildi\"."))
         + "\n"
         + box("green", ("Nega bunday", "Почему так", "Why this happens"),
               items=[
                   ("Brauzerdagi <b>butun kod o'yinchi kompyuterida</b> ishlaydi — "
                    "demak u kodni ham, xotirani ham o'zgartira oladi.",
                    "<b>Весь код в браузере</b> работает на компьютере игрока — значит, "
                    "он может изменить и код, и память.",
                    "<b>All browser code</b> runs on the player's machine — so they can "
                    "change both the code and the memory."),
                   ("<code>localStorage</code> — bu <b>himoya emas</b>, bu shunchaki "
                    "qulaylik. U parol bilan yopilmagan.",
                    "<code>localStorage</code> — это <b>не защита</b>, а просто удобство. "
                    "Он не закрыт паролем.",
                    "<code>localStorage</code> is <b>not security</b>, it is convenience. "
                    "It has no password."),
                   ("Shuning uchun jiddiy o'yinlarda ochko <b>serverda</b> hisoblanadi.",
                    "Поэтому в серьёзных играх очки считаются <b>на сервере</b>.",
                    "That is why serious games compute the score <b>on the server</b>."),
               ])
         + "\n</div>\n"
         + box("purple", ("Real o'yinlar buni qanday hal qiladi",
                          "Как это решают настоящие игры",
                          "How real games solve this"),
               items=[
                   ("<b>Server hisoblaydi.</b> Mijoz faqat harakatlarni yuboradi, ochkoni "
                    "server o'zi chiqaradi. Eng ishonchli, lekin qimmat.",
                    "<b>Сервер считает.</b> Клиент шлёт только действия, очки выводит сам "
                    "сервер. Самое надёжное, но дорогое.",
                    "<b>The server computes.</b> The client sends only actions; the server "
                    "derives the score. Most reliable, but expensive."),
                   ("<b>Takrorlash yozuvi (replay).</b> O'yin barcha tugma bosishlarini "
                    "saqlaydi, server o'yinni qayta o'ynab tekshiradi.",
                    "<b>Реплей.</b> Игра сохраняет все нажатия, сервер переигрывает партию "
                    "и проверяет.",
                    "<b>Replay.</b> The game records every input and the server replays "
                    "the run to verify it."),
                   ("<b>Mantiqiy tekshiruv.</b> \"30 soniyada 999999 ochko olish mumkin "
                    "emas\" — shubhali natija rad etiladi.",
                    "<b>Проверка здравым смыслом.</b> «За 30 секунд нельзя набрать 999999» "
                    "— подозрительный результат отклоняется.",
                    "<b>Sanity checks.</b> \"999,999 points in 30 seconds is impossible\" — "
                    "the suspicious result is rejected."),
               ]),
))

S.append(slide(
    ph=("Amaliyot", "Практика", "Practice"), time="33–45",
    eyebrow=("Turnir · 12 daqiqa", "Турнир · 12 минут", "Tournament · 12 minutes"),
    title=("Sinf turniri: lab/index.html ni oching",
           "Классный турнир: откройте lab/index.html",
           "Class tournament: open lab/index.html"),
    body='<div class="cols c4">\n' + "\n".join([
        box("purple", ("1 · Ism (1 daq)", "1 · Имя (1 мин)", "1 · Name (1 min)"),
            p=("Ismingizni kiriting va 2 ta mashq o'yin o'ynang. Boshqaruvni his qiling: "
               "harakat, sakrash, dushmanni bosish.",
               "Введите имя и сыграйте 2 тренировочные партии. Почувствуйте управление: "
               "движение, прыжок, прыжок на врага.",
               "Enter your name and play 2 practice runs. Get a feel for the controls: "
               "move, jump, stomp.")),
        box("accent", ("2 · Rekord (5 daq)", "2 · Рекорд (5 мин)", "2 · Record (5 min)"),
            p=("Eng yaxshi natijangizni qo'ying. <b>Kombo</b>ni uzmaslikka harakat qiling — "
               "aynan u eng ko'p ochko beradi.",
               "Поставьте лучший результат. Старайтесь не рвать <b>комбо</b> — "
               "именно оно даёт больше всего очков.",
               "Set your best score. Try not to break the <b>combo</b> — "
               "that is where most points come from.")),
        box("green", ("3 · Tahlil (3 daq)", "3 · Анализ (3 мин)", "3 · Analysis (3 min)"),
            p=("Jadvaldagi <b>o'rningizni</b> yozing. Birinchi o'rindagi natijadan qancha "
               "orqadasiz? Qaysi to'lqinda yutqazdingiz?",
               "Запишите своё <b>место</b> в таблице. На сколько отстали от первого? "
               "На какой волне проиграли?",
               "Write your <b>rank</b>. How far behind first place? "
               "Which wave killed you?")),
        box("", ("4 · Cheat (3 daq)", "4 · Чит (3 мин)", "4 · Cheat (3 min)"),
            p=("<b>💀 CHEAT</b> tugmasini bosing — jadvalga soxta rekord tushadi. "
               "Keyin <b>🛡 Tekshirish</b> ni bosing va nima bo'lishini ko'ring.",
               "Нажмите <b>💀 ЧИТ</b> — в таблицу попадёт фальшивый рекорд. "
               "Затем нажмите <b>🛡 Проверка</b> и посмотрите, что будет.",
               "Press <b>💀 CHEAT</b> — a fake record lands in the table. "
               "Then press <b>🛡 Validate</b> and see what happens.")),
    ]) + "\n</div>\n"
         + box("accent", ("🏆 Sinf chempioni", "🏆 Чемпион класса", "🏆 Class champion"),
               p=("Dars oxirida o'qituvchi proyektorda jadvalni ochadi. Birinchi uch o'rin "
                  "e'lon qilinadi. <b>Lekin:</b> avval <b>🛡 Tekshirish</b> ishga tushadi va "
                  "mumkin bo'lmagan natijalar o'chiriladi.",
                  "В конце урока учитель откроет таблицу на проекторе. Объявляются первые "
                  "три места. <b>Но:</b> сначала запускается <b>🛡 Проверка</b> и "
                  "невозможные результаты удаляются.",
                  "At the end the teacher opens the table on the projector. The top three "
                  "are announced. <b>But:</b> first <b>🛡 Validate</b> runs and impossible "
                  "results are removed.")),
))

S.append(slide(
    ph=("AI yordamchi", "AI помощник", "AI helper"), time="45–46",
    eyebrow=("Tayyor promptlar", "Готовые промпты", "Ready-made prompts"),
    title=("AI bilan ma'lumot va xavfsizlik",
           "Данные и безопасность с помощью AI",
           "Data and security with AI"),
    body='<div class="cols c2">\n'
         + box("purple", ("Nusxa oling", "Скопируйте", "Copy these"),
               extra_html=code(
                   "1) Объясни, почему нельзя доверять счёту,\n"
                   "   который прислал браузер игрока.\n"
                   "   Приведи 3 способа защиты в реальных играх.\n\n"
                   "2) Напиши функцию на JavaScript, которая\n"
                   "   сортирует массив {ism, ochko} по убыванию\n"
                   "   очков и оставляет топ-10.\n\n"
                   "3) Почему [100, 9, 80].sort() даёт\n"
                   "   [100, 80, 9]? Объясни и покажи, как\n"
                   "   исправить."))
         + "\n"
         + box("accent", ("Javobni tekshirish", "Проверка ответа", "Checking the answer"),
               items=[
                   ("3-promptning javobi darsdagi tuzoq bilan mos kelishi kerak — "
                    "<code>sort()</code> sonlarni matn sifatida saralaydi.",
                    "Ответ на 3-й промпт должен совпасть с ловушкой из урока — "
                    "<code>sort()</code> сортирует числа как текст.",
                    "The answer to prompt 3 must match the trap from the lesson — "
                    "<code>sort()</code> sorts numbers as text."),
                   ("AI bergan kodni stendda sinab ko'ring: jadval to'g'ri "
                    "saralanyaptimi?",
                    "Проверьте код от AI на стенде: правильно ли сортируется таблица?",
                    "Test the AI's code on the lab: does the table sort correctly?"),
                   ("AI \"localStorage xavfsiz\" desa — bu <b>xato javob</b>. "
                    "Bugun buning aksini o'z ko'zingiz bilan ko'rdingiz.",
                    "Если AI скажет «localStorage безопасен» — это <b>неверный ответ</b>. "
                    "Сегодня вы своими глазами видели обратное.",
                    "If the AI says \"localStorage is secure\" that is a <b>wrong answer</b>. "
                    "Today you saw the opposite with your own eyes."),
               ])
         + "\n</div>",
))

S.append(slide(
    ph=("Yakun", "Итоги", "Summary"), time="46–47",
    eyebrow=("Nimani o'rgandik", "Что мы изучили", "What we learned"),
    title=("Dvigateldan to'liq o'yingacha — ikki darsda",
           "От движка до полной игры — за два урока",
           "From engine to full game — in two lessons"),
    body='<div class="cols c2">\n'
         + box("green", ("13-dars bergan narsa", "Что дал урок 13", "What lesson 13 gave"),
               items=[
                   ("Canvas va o'yin tsikli: CLEAR → UPDATE → DRAW.",
                    "Canvas и игровой цикл: CLEAR → UPDATE → DRAW.",
                    "Canvas and the game loop: CLEAR → UPDATE → DRAW."),
                   ("Delta Time — har kompyuterda bir xil tezlik.",
                    "Delta Time — одинаковая скорость на любом компьютере.",
                    "Delta Time — the same speed on every machine."),
                   ("Fizika uchta qator va AABB to'qnashuv.",
                    "Физика в три строки и AABB-столкновения.",
                    "Physics in three lines and AABB collisions."),
               ])
         + "\n"
         + box("accent", ("14-dars bergan narsa", "Что дал урок 14", "What lesson 14 gave"),
               items=[
                   ("Ochko, kombo va dushman to'lqinlari — o'yin dizayni.",
                    "Очки, комбо и волны врагов — геймдизайн.",
                    "Score, combo and enemy waves — game design."),
                   ("Holat mashinasi: MENU → PLAYING → GAME OVER.",
                    "Машина состояний: MENU → PLAYING → GAME OVER.",
                    "State machine: MENU → PLAYING → GAME OVER."),
                   ("JSON, <code>sort</code> va leaderboard.",
                    "JSON, <code>sort</code> и таблица рекордов.",
                    "JSON, <code>sort</code> and the leaderboard."),
                   ("<b>Va eng muhimi:</b> mijoz ma'lumotiga ishonib bo'lmaydi.",
                    "<b>И самое важное:</b> данным клиента нельзя доверять.",
                    "<b>And most importantly:</b> client data cannot be trusted."),
               ])
         + "\n</div>",
))

S.append(slide(
    ph=("Uy vazifasi", "Домашнее задание", "Homework"), time="47–48",
    eyebrow=("Baholash mezoni", "Критерии оценки", "Grading rubric"),
    title=("Uy vazifasi: turnir hisoboti va himoya rejasi (10 ball)",
           "Домашнее задание: отчёт о турнире и план защиты (10 баллов)",
           "Homework: tournament report and defence plan (10 points)"),
    body='<div class="cols c2">\n'
         + box("green", ("Nima qilish kerak", "Что нужно сделать", "What to do"),
               items=[
                   ("Turnir natijalarini varaqaga yozing: ochko, to'lqin, o'rin.",
                    "Запишите результаты турнира в лист: очки, волна, место.",
                    "Log your tournament results: score, wave, rank."),
                   ("<code>JSON.stringify</code> va <code>JSON.parse</code> nima "
                    "qilishini <b>misol bilan</b> yozing.",
                    "Напишите <b>с примером</b>, что делают <code>JSON.stringify</code> "
                    "и <code>JSON.parse</code>.",
                    "Explain <b>with an example</b> what <code>JSON.stringify</code> and "
                    "<code>JSON.parse</code> do."),
                   ("Cheat sinovini tavsiflang: nima qildingiz va tekshiruv nima qildi.",
                    "Опишите чит-тест: что вы сделали и что сделала проверка.",
                    "Describe the cheat test: what you did and what the validator did."),
                   ("<b>Himoya rejasi:</b> o'yiningizni aldashdan himoya qilishning "
                    "2 ta usulini taklif qiling.",
                    "<b>План защиты:</b> предложите 2 способа защитить вашу игру от "
                    "читеров.",
                    "<b>Defence plan:</b> propose 2 ways to protect your game from "
                    "cheating."),
               ])
         + "\n"
         + box("accent", ("Baholash mezoni", "Критерии оценки", "Grading rubric"),
               extra_html='<ul class="plain">\n'
               + '  <li><span class="t" %s>Turnir natijalari jadvali — <b>3 ball</b></span></li>\n'
               % i18n("Turnir natijalari jadvali — <b>3 ball</b>",
                      "Таблица результатов турнира — <b>3 балла</b>",
                      "Tournament results table — <b>3 points</b>")
               + '  <li><span class="t" %s>JSON izohi misol bilan — <b>3 ball</b></span></li>\n'
               % i18n("JSON izohi misol bilan — <b>3 ball</b>",
                      "Объяснение JSON с примером — <b>3 балла</b>",
                      "JSON explained with an example — <b>3 points</b>")
               + '  <li><span class="t" %s>Cheat sinovi tavsifi — <b>2 ball</b></span></li>\n'
               % i18n("Cheat sinovi tavsifi — <b>2 ball</b>",
                      "Описание чит-теста — <b>2 балла</b>",
                      "Cheat test description — <b>2 points</b>")
               + '  <li><span class="t" %s>Himoyaning 2 ta usuli — <b>2 ball</b></span></li>\n'
               % i18n("Himoyaning 2 ta usuli — <b>2 ball</b>",
                      "2 способа защиты — <b>2 балла</b>",
                      "2 defence methods — <b>2 points</b>")
               + "</ul>")
         + "\n</div>",
))


NOTES = {
    "uz": [
        ["Titul slayd",
         "Salom! O'tgan darsda siz dvigatel qurdingiz — tsikl, delta time, fizika. Lekin dvigatel hali o'yin emas. Bugun unga maqsad, xavf va natija qo'shamiz. Dars oxirida sinfda umumiy reyting jadvali bo'ladi.",
         "lab/index.html ni proyektorda oldindan oching."],
        ["Dvigatel emas, o'yin",
         "Uchta ustunni ayting: maqsad, xavf, natija. Bolalardan so'rang: nega yutqazib bo'lmaydigan o'yin zerikarli? Javob — g'alabaning qiymati yo'qoladi.",
         "Uchta ustunni birma-bir ko'rsatish."],
        ["Ochko va kombo",
         "Asosiy fikr: ochko mukofot emas, xabar. Kombo esa o'yinchining xulq-atvorini o'zgartiradi — ehtiyotkorlikdan tavakkalga. Bitta qator kod, katta ta'sir.",
         "Stendda kombo ko'rsatkichini jonli ko'rsatish."],
        ["To'lqinlar va qiyinlik",
         "Qiyinlikni oshirishning uch yo'lini ayting va eng yomonini alohida ta'kidlang: dushmanga ko'p jon berish. Bu qiyin emas, uzoq va zerikarli. Bolalar buni o'yinlarda ko'p uchratgan.",
         "Stendda to'lqin raqamini ko'rsatish."],
        ["Holat mashinasi",
         "MENU, PLAYING, GAME OVER. Kod blokidagi erta return ni ko'rsating. Holatni tekshirmasangiz — GAME OVER ekranida dushmanlar yuraverdi. Bu real xato.",
         "Stendda uchala ekranni ketma-ket ko'rsatish."],
        ["JSON",
         "stringify va parse. Eng muhim ogohlantirish — parse ni unutish. localStorage matn qaytaradi, unga push qilib bo'lmaydi. Bu eng ko'p uchraydigan xato.",
         "F12 Console da localStorage ni ochib ko'rsatish."],
        ["Leaderboard: sort",
         "Uchta amal: push, sort, slice. Klassik tuzoqni albatta ko'rsating: [100,9,80].sort() natijasi [100,80,9]. Doskada yozing — bolalar hayratlanadi.",
         "Doskada [100,9,80].sort() misolini yozish."],
        ["Halollik — darsning cho'qqisi",
         "Eng muhim slayd. Proyektorda F12 ni oching va localStorage ni bitta qator bilan o'zgartirib ko'rsating. Bolalar buni ko'rishi shart. Keyin ayting: shuning uchun jiddiy o'yinlarda server hisoblaydi.",
         "F12 Console da jonli cheat demo. Keyin himoya usullarini aytish."],
        ["Turnir 12 daqiqa",
         "To'rt bosqich. Vaqtni qattiq nazorat qiling. Oxirgi bosqich — cheat sinovi — eng qiziqarlisi, uni tashlab ketmang. Sinf bo'ylab yuring.",
         "Har bosqich oxirida vaqtni e'lon qilish."],
        ["AI bilan ishlash",
         "Muhim tekshiruv: agar AI 'localStorage xavfsiz' desa — bu xato. Bolalar bugun buning aksini o'z ko'zi bilan ko'rdi, shuning uchun ular AI ni tuzata oladi. Bu kuchli lahza.",
         "Bitta ekranda AI javobini birga tahlil qilish."],
        ["Ikki darsning xulosasi",
         "13 va 14-darsni birlashtiring: dvigateldan to'liq o'yingacha. Bolalar nimalarni o'rganganini ro'yxat qilib ko'rsating — bu ularga o'sishni his qildiradi.",
         "Ikki ustunni ko'rsatish."],
        ["Yakun va baholash",
         "Proyektorda jadvalni oching, Tekshirish tugmasini bosing va soxta natijalar o'chishini ko'rsating. Keyin chempionlarni e'lon qiling. Varaqalarni yig'ing.",
         "Tekshirishni jonli ishga tushirib, top-3 ni e'lon qilish."],
    ],
    "ru": [
        ["Титульный слайд",
         "Привет! На прошлом уроке вы построили движок — цикл, delta time, физику. Но движок — ещё не игра. Сегодня добавим цель, риск и результат. В конце урока в классе будет общая таблица рекордов.",
         "Заранее откройте lab/index.html на проекторе."],
        ["Не движок, а игра",
         "Назовите три колонки: цель, риск, результат. Спросите: почему игра, в которой нельзя проиграть, скучная? Ответ — победа обесценивается.",
         "Показать три колонки по очереди."],
        ["Очки и комбо",
         "Главная мысль: очки — не награда, а сообщение. А комбо меняет поведение игрока — с осторожного на рискованное. Одна строка кода, большой эффект.",
         "Показать счётчик комбо живьём на стенде."],
        ["Волны и сложность",
         "Назовите три способа усложнения и отдельно подчеркните худший: дать врагу много здоровья. Это не сложно, это долго и скучно. Дети часто это встречали в играх.",
         "Показать номер волны на стенде."],
        ["Машина состояний",
         "MENU, PLAYING, GAME OVER. Покажите ранний return в блоке кода. Не проверите состояние — на экране GAME OVER враги продолжат ходить. Это реальный баг.",
         "Показать все три экрана по очереди на стенде."],
        ["JSON",
         "stringify и parse. Самое важное предупреждение — забыть parse. localStorage возвращает текст, к нему нельзя применить push. Это самая частая ошибка.",
         "Открыть localStorage в F12 Console и показать."],
        ["Таблица рекордов: sort",
         "Три операции: push, sort, slice. Обязательно покажите классическую ловушку: [100,9,80].sort() даёт [100,80,9]. Напишите на доске — дети удивятся.",
         "Написать на доске пример [100,9,80].sort()."],
        ["Честность — вершина урока",
         "Самый важный слайд. Откройте F12 на проекторе и одной строкой измените localStorage. Дети обязаны это увидеть. Затем скажите: вот почему в серьёзных играх считает сервер.",
         "Живое чит-демо в F12 Console. Затем назвать способы защиты."],
        ["Турнир 12 минут",
         "Четыре этапа. Жёстко следите за временем. Последний этап — чит-тест — самый интересный, не пропускайте его. Ходите по классу.",
         "Объявлять время в конце каждого этапа."],
        ["Работа с AI",
         "Важная проверка: если AI скажет «localStorage безопасен» — это ошибка. Дети сегодня своими глазами видели обратное, поэтому они могут поправить AI. Это сильный момент.",
         "Разобрать ответ AI вместе на одном экране."],
        ["Итог двух уроков",
         "Соедините уроки 13 и 14: от движка до полной игры. Перечислите, чему научились — это даёт им почувствовать рост.",
         "Показать две колонки."],
        ["Итоги и оценивание",
         "Откройте таблицу на проекторе, нажмите Проверку и покажите, как удаляются фальшивые результаты. Затем объявите чемпионов. Соберите листы.",
         "Запустить проверку живьём и объявить топ-3."],
    ],
    "en": [
        ["Title slide",
         "Hello! Last lesson you built an engine — loop, delta time, physics. But an engine is not a game. Today we add goal, risk and result. By the end the class will have a shared leaderboard.",
         "Pre-open lab/index.html on the projector."],
        ["Not an engine, a game",
         "Name the three columns: goal, risk, result. Ask: why is a game you cannot lose boring? Because winning becomes worthless.",
         "Walk through the three columns."],
        ["Score and combo",
         "Core idea: score is not a reward, it is a message. And combo changes player behaviour — from cautious to risk-taking. One line of code, huge effect.",
         "Show the combo counter live on the lab."],
        ["Waves and difficulty",
         "Name the three ways to raise difficulty and call out the worst one separately: giving enemies more health. That is not hard, just long and dull. They have met this in games.",
         "Show the wave number on the lab."],
        ["State machine",
         "MENU, PLAYING, GAME OVER. Show the early return in the code block. Skip the state check and enemies keep moving on the GAME OVER screen. A real bug.",
         "Show all three screens in turn on the lab."],
        ["JSON",
         "stringify and parse. The key warning is forgetting parse. localStorage returns text; you cannot push to it. The most common mistake.",
         "Open localStorage in the F12 console and show it."],
        ["Leaderboard: sort",
         "Three operations: push, sort, slice. Definitely show the classic trap: [100,9,80].sort() gives [100,80,9]. Write it on the board — it surprises them.",
         "Write the [100,9,80].sort() example on the board."],
        ["Fair play — the peak of the lesson",
         "The key slide. Open F12 on the projector and change localStorage with one line. They must see this. Then say: that is why serious games compute on the server.",
         "Live cheat demo in the F12 console. Then name the defences."],
        ["Tournament, 12 minutes",
         "Four stages. Keep time strictly. The last stage — the cheat test — is the most interesting, do not skip it. Walk the room.",
         "Announce the time at each stage boundary."],
        ["Working with AI",
         "An important check: if the AI says 'localStorage is secure' that is wrong. They saw the opposite today, so they can correct the AI. A powerful moment.",
         "Analyse an AI answer together on one screen."],
        ["Two lessons summarised",
         "Join lessons 13 and 14: from engine to complete game. List what they learned — it lets them feel the progress.",
         "Show the two columns."],
        ["Summary and grading",
         "Open the table on the projector, press Validate and show the fake results being removed. Then announce the champions. Collect the sheets.",
         "Run the validation live and announce the top 3."],
    ],
}

VARAQA = (
    sheet_header(
        ("14-dars: Dushmanlar, Ochko va Leaderboard",
         "Урок 14: Враги, Очки и Таблица Рекордов",
         "Lesson 14: Enemies, Score and Leaderboard"),
        ("Target International School · 7–8-sinf · 3-hafta (2-soat)",
         "Target International School · 7–8 класс · 3-я неделя (2-й час)",
         "Target International School · Grades 7–8 · Week 3 (Hour 2)"))
    + mission(
        ("🎯 Turnir missiyasi: rekord qo'ying va uni sindiring",
         "🎯 Миссия турнира: поставь рекорд и сломай его",
         "🎯 Tournament mission: set a record, then break it"),
        ("<b>lab/index.html</b> ni oching, ismingizni kiriting va eng yaxshi natijangizni "
         "qo'ying. Keyin eng qiziq qism: <b>💀 CHEAT</b> tugmasi bilan jadvalni aldang va "
         "<b>🛡 Tekshirish</b> uni qanday fosh qilishini ko'ring.",
         "Откройте <b>lab/index.html</b>, введите имя и поставьте лучший результат. "
         "Затем самое интересное: обманите таблицу кнопкой <b>💀 ЧИТ</b> и посмотрите, "
         "как <b>🛡 Проверка</b> его разоблачит.",
         "Open <b>lab/index.html</b>, enter your name and set your best score. "
         "Then the fun part: cheat the table with <b>💀 CHEAT</b> and watch "
         "<b>🛡 Validate</b> expose it."))
    + table(
        [("Bosqich", "Этап", "Stage"),
         ("Nima qilasiz", "Что делаете", "What you do"),
         ("Natija", "Результат", "Result")],
        [[("1 · Mashq", "1 · Тренировка", "1 · Practice"),
          ("2 ta mashq o'yin", "2 тренировочные партии", "2 practice runs"),
          ("Eng yaxshi mashq ochkosi: ______",
           "Лучший тренировочный счёт: ______",
           "Best practice score: ______")],
         [("2 · Rekord", "2 · Рекорд", "2 · Record"),
          ("Eng yaxshi natijangiz", "Ваш лучший результат", "Your best run"),
          ("Ochko: ______ · To'lqin: ______ · Maks kombo: ______",
           "Очки: ______ · Волна: ______ · Макс комбо: ______",
           "Score: ______ · Wave: ______ · Max combo: ______")],
         [("3 · Reyting", "3 · Рейтинг", "3 · Ranking"),
          ("Jadvaldagi o'rningiz", "Ваше место в таблице", "Your place in the table"),
          ("O'rin: ____ / ____ · 1-o'rindan farq: ______ ochko",
           "Место: ____ / ____ · Отрыв от 1-го: ______ очков",
           "Rank: ____ / ____ · Behind 1st by: ______ points")],
         [("4 · Cheat", "4 · Чит", "4 · Cheat"),
          ("💀 CHEAT → keyin 🛡 Tekshirish",
           "💀 ЧИТ → затем 🛡 Проверка",
           "💀 CHEAT → then 🛡 Validate"),
          ("Tekshiruv nechta natijani o'chirdi? ______",
           "Сколько результатов удалила проверка? ______",
           "How many records did the validator remove? ______")]])
    + '    <div class="rubric-grid">\n'
    + sheet_box(
        ("✏️ Nazariya va himoya rejasi",
         "✏️ Теория и план защиты",
         "✏️ Theory and defence plan"),
        writelines(2, ("JSON.stringify va JSON.parse nima qiladi? (misol bilan)",
                       "Что делают JSON.stringify и JSON.parse? (с примером)",
                       "What do JSON.stringify and JSON.parse do? (with an example)"))
        + "\n"
        + writelines(3, ("🛡 O'yinni aldashdan himoya qilishning 2 ta usuli:",
                         "🛡 2 способа защитить игру от читеров:",
                         "🛡 2 ways to protect the game from cheating:")))
    + "\n"
    + sheet_box(
        ("📊 Baholash mezoni (10 ball)",
         "📊 Критерии оценки (10 баллов)",
         "📊 Grading rubric (10 points)"),
        rubric([
            (("Turnir natijalari jadvali", "Таблица результатов турнира",
              "Tournament results table"), "3"),
            (("JSON izohi misol bilan", "Объяснение JSON с примером",
              "JSON explained with an example"), "3"),
            (("Cheat sinovi tavsifi", "Описание чит-теста", "Cheat test description"), "2"),
            (("Himoyaning 2 ta usuli", "2 способа защиты", "2 defence methods"), "2"),
        ], "10"))
    + "\n    </div>\n  </div>\n"
    + sign_box()
)

if __name__ == "__main__":
    print(Lesson(D, TITLES, SHEET_TITLES, "vc-notes-7-14", S, NOTES, VARAQA).build())
