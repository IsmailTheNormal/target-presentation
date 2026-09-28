# -*- coding: utf-8 -*-
"""5-6-sinf · 4-hafta · 16-dars — O'z Levelingni Qur: Redaktor, Level Kodi va Ulashish."""

import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from build import (Lesson, slide, title_slide, box, code, el, i18n,
                   sheet_header, mission, table, sheet_box, rubric, writelines, sign_box)

D = "classes/5-6-sinf/4-hafta/16-dars-level-redaktor-va-ulashish"

TITLES = {
    "uz": "16-dars: O'z Levelingni Qur — Redaktor, Level Kodi va Ulashish",
    "ru": "Урок 16: Построй Свой Уровень — Редактор, Код Уровня и Обмен",
    "en": "Lesson 16: Build Your Own Level — Editor, Level Code and Sharing",
}
SHEET_TITLES = {k: v + (" — Ish Varaqasi" if k == "uz" else
                        " — Рабочий Лист" if k == "ru" else " — Worksheet")
                for k, v in TITLES.items()}

S = []

S.append(title_slide(
    ph=("Kirish", "Введение", "Intro"), time="0–3",
    eyebrow=("Vibecoding · 16-dars · 5–6-sinflar",
             "Vibecoding · Урок 16 · 5–6 классы",
             "Vibecoding · Lesson 16 · Grades 5–6"),
    h1=("O'z Levelingni Qur: Redaktor, Level Kodi va Ulashish",
        "Построй Свой Уровень: Редактор, Код Уровня и Обмен",
        "Build Your Own Level: Editor, Level Code and Sharing"),
    lede=("Shu paytgacha siz <b>boshqa odam qurgan</b> maydonda o'ynadingiz. "
          "Bugun hammasi teskari bo'ladi: siz dizayner bo'lasiz, o'z maydoningizni "
          "sichqoncha bilan chizasiz, uni <b>level kodi</b>ga aylantirasiz va "
          "sinfdoshingizga berasiz. Dars oxirida sizda o'z leveligizning kodi qoladi — "
          "uni istalgan kompyuterda ochish mumkin.",
          "До сих пор вы играли на площадке, которую <b>построил кто-то другой</b>. "
          "Сегодня всё наоборот: вы становитесь дизайнером, рисуете свою площадку "
          "мышкой, превращаете её в <b>код уровня</b> и отдаёте однокласснику. "
          "В конце урока у вас останется код вашего уровня — его можно открыть "
          "на любом компьютере.",
          "So far you have played on an arena <b>somebody else built</b>. "
          "Today it flips: you become the designer, paint your own arena with the "
          "mouse, turn it into a <b>level code</b> and hand it to a classmate. "
          "By the end you will own your level's code — and it opens on any computer."),
    meta=[("<b>Fan:</b> Vibecoding · O'yin dizayni",
           "<b>Предмет:</b> Vibecoding · Геймдизайн",
           "<b>Subject:</b> Vibecoding · Game Design"),
          ("<b>Kohorta:</b> 5–6-sinf (10–12 yosh)",
           "<b>Когорта:</b> 5–6 класс (10–12 лет)",
           "<b>Cohort:</b> Grades 5–6 (ages 10–12)"),
          ("<b>Hafta:</b> 4 (2-soat)", "<b>Неделя:</b> 4 (2-й час)", "<b>Week:</b> 4 (Hour 2)")],
))

S.append(slide(
    ph=("Rol almashadi", "Смена роли", "Role swap"), time="3–6",
    eyebrow=("O'yinchidan dizaynerga", "Из игрока в дизайнеры", "From player to designer"),
    title=("Bugun siz o'ynamaysiz — siz qurasiz",
           "Сегодня вы не играете — вы строите",
           "Today you do not play — you build"),
    body='<div class="cols c2">\n'
         + box("", ("🎮 O'yinchi nima qiladi", "🎮 Что делает игрок", "🎮 What a player does"),
               items=[
                   ("Maydon qanday bo'lsa, shunday qabul qiladi.",
                    "Принимает площадку такой, какая она есть.",
                    "Takes the arena exactly as it is."),
                   ("Faqat bitta savol beradi: \"qanday o'tsam bo'ladi?\"",
                    "Задаёт один вопрос: «как мне пройти?»",
                    "Asks one question: \"how do I get through?\""),
                   ("Level tugadi — o'yin tugadi.",
                    "Уровень закончился — игра закончилась.",
                    "Level over, game over."),
               ])
         + "\n"
         + box("accent", ("🛠 Dizayner nima qiladi", "🛠 Что делает дизайнер", "🛠 What a designer does"),
               items=[
                   ("Maydonni <b>o'zi yaratadi</b> — har bir tikan uning qarori.",
                    "<b>Создаёт</b> площадку сам — каждый шип это его решение.",
                    "<b>Creates</b> the arena — every spike is their decision."),
                   ("Savol boshqacha: \"o'ynayotgan odam nimani his qiladi?\"",
                    "Вопрос другой: «что почувствует тот, кто играет?»",
                    "The question differs: \"what will the player feel?\""),
                   ("Level tugamaydi — u <b>boshqalarga uzatiladi</b>.",
                    "Уровень не заканчивается — он <b>передаётся другим</b>.",
                    "The level does not end — it is <b>passed to others</b>."),
               ])
         + "\n</div>\n"
         + box("green", ("Mario, Roblox va Minecraft ni kim qurgan?",
                         "Кто построил Mario, Roblox и Minecraft?",
                         "Who built Mario, Roblox and Minecraft?"),
               p=("Roblox dagi o'yinlarning katta qismini — <b>bolalar</b> qurgan. "
                  "Ular ham xuddi bugungidek boshlagan: panjara, bir nechta \"bo'yoq\" "
                  "va birinchi level. Farqi shundaki, ular <b>to'xtamagan</b>.",
                  "Большую часть игр в Roblox построили <b>дети</b>. Они начинали ровно "
                  "так же, как вы сегодня: сетка, несколько «красок» и первый уровень. "
                  "Разница только в том, что они <b>не остановились</b>.",
                  "Most games on Roblox were built by <b>kids</b>. They started exactly "
                  "like you today: a grid, a few \"paints\" and a first level. "
                  "The only difference is they <b>did not stop</b>.")),
))

S.append(slide(
    ph=("Panjara", "Сетка", "The grid"), time="6–10",
    eyebrow=("Level qanday tuzilgan", "Из чего состоит уровень", "What a level is made of"),
    title=("Har qanday level — bu kataklarga bo'lingan panjara",
           "Любой уровень — это сетка из клеток",
           "Every level is a grid of cells"),
    body='<div class="cols c2">\n'
         + box("purple", ("Kompyuter maydonni qanday ko'radi",
                          "Как компьютер видит площадку", "How the computer sees the arena"),
               p=("Kompyuter rasm ko'rmaydi. U uchun maydon — <b>raqamlar jadvali</b>. "
                  "Bizning redaktorimizda maydon <b>20 ustun × 10 qator</b> = 200 katak. "
                  "Har katakda bitta raqam turadi.",
                  "Компьютер не видит картинку. Для него площадка — это <b>таблица чисел</b>. "
                  "В нашем редакторе площадка — <b>20 столбцов × 10 строк</b> = 200 клеток. "
                  "В каждой клетке стоит одно число.",
                  "The computer sees no picture. To it the arena is a <b>table of numbers</b>. "
                  "In our editor it is <b>20 columns × 10 rows</b> = 200 cells. "
                  "Each cell holds one number."))
         + "\n"
         + box("green", ("Bitta qator shunday ko'rinadi",
                         "Одна строка выглядит так", "One row looks like this"),
               extra_html=code(
                   "0 0 0 0 0 0 0 0 0 0\n"
                   "0 0 2 0 0 0 3 0 0 0\n"
                   "1 1 1 1 1 1 1 1 1 1\n\n"
                   "// 0 = bo'shliq   1 = platforma\n"
                   "// 2 = tikan      3 = dushman"))
         + "\n</div>\n"
         + box("accent", ("💡 Shuning uchun level kodini yuborish oson",
                          "💡 Поэтому код уровня легко переслать",
                          "💡 That is why a level code is easy to send"),
               p=("Agar level rasm bo'lganida, uni yuborish uchun katta fayl kerak bo'lardi. "
                  "Lekin level — bu <b>raqamlar</b>, ya'ni oddiy matn. Matnni esa xabar "
                  "orqali, qog'ozda yoki og'zaki ham uzatish mumkin!",
                  "Если бы уровень был картинкой, для пересылки понадобился бы большой файл. "
                  "Но уровень — это <b>числа</b>, то есть обычный текст. А текст можно "
                  "передать сообщением, на бумаге и даже вслух!",
                  "If a level were a picture you would need a big file to send it. "
                  "But a level is <b>numbers</b> — plain text. And text travels by message, "
                  "on paper, even spoken aloud!")),
))

S.append(slide(
    ph=("Asboblar", "Инструменты", "Tools"), time="10–14",
    eyebrow=("Beshta bo'yoq", "Пять красок", "Five paints"),
    title=("Redaktorda beshta \"bo'yoq\" bor — boshqa hech narsa",
           "В редакторе пять «красок» — и больше ничего",
           "The editor has five \"paints\" — nothing more"),
    body='<div class="cols c3">\n' + "\n".join([
        box("", ("⬜ 0 · Bo'shliq", "⬜ 0 · Пустота", "⬜ 0 · Empty"),
            p=("Havo. Qahramon bemalol o'tadi. Levelning ko'p qismi shu bo'lishi kerak — "
               "bo'sh joy ham dizayn!",
               "Воздух. Герой свободно проходит. Большая часть уровня должна быть такой — "
               "пустое место это тоже дизайн!",
               "Air. The hero passes freely. Most of the level should be this — "
               "empty space is design too!")),
        box("purple", ("🟦 1 · Platforma", "🟦 1 · Платформа", "🟦 1 · Platform"),
            p=("Qattiq yer. Ustida turish va sakrash mumkin. Platformalarni "
               "<b>pog'ona qilib</b> joylashtiring — shunda sakrash qiziq bo'ladi.",
               "Твёрдая земля. Можно стоять и прыгать. Ставьте платформы "
               "<b>лесенкой</b> — тогда прыгать интересно.",
               "Solid ground. You can stand and jump on it. Place platforms "
               "<b>like stairs</b> to make jumping interesting.")),
        box("accent", ("🔺 2 · Tikan", "🔺 2 · Шип", "🔺 2 · Spike"),
            p=("Tegsangiz <b>1 jon</b> ketadi. Ko'p qo'ymang! 200 katakda 8–12 ta tikan "
               "yetarli. 50 ta tikan — bu qiyin emas, bu asabiylashtiruvchi.",
               "Коснулись — минус <b>1 жизнь</b>. Не ставьте много! На 200 клеток хватит "
               "8–12 шипов. 50 шипов — это не сложно, это раздражает.",
               "Touch it and lose <b>1 life</b>. Do not overdo it! 8–12 spikes per 200 "
               "cells is plenty. 50 spikes is not hard, it is annoying.")),
        box("accent", ("🤖 3 · Dushman", "🤖 3 · Враг", "🤖 3 · Enemy"),
            p=("O'tgan darsdagi dushman! U shu joydan patrul qiladi, sizni ko'radi va "
               "quvadi. Levelda <b>1–3 ta</b> dushman — eng yaxshi miqdor.",
               "Враг с прошлого урока! Он патрулирует отсюда, видит вас и гонится. "
               "<b>1–3 врага</b> на уровень — самое удачное количество.",
               "The enemy from last lesson! It patrols from here, sees you and chases. "
               "<b>1–3 enemies</b> per level is the sweet spot.")),
        box("green", ("🏁 4 · Finish", "🏁 4 · Финиш", "🏁 4 · Finish"),
            p=("G'alaba portali. <b>Aynan bitta</b> bo'lishi shart — bo'lmasa levelni "
               "yutib bo'lmaydi. Redaktor buni avtomatik tekshiradi.",
               "Портал победы. Должен быть <b>ровно один</b> — иначе уровень нельзя "
               "выиграть. Редактор проверяет это автоматически.",
               "The victory portal. There must be <b>exactly one</b> — otherwise the level "
               "cannot be won. The editor checks this automatically.")),
        box("purple", ("🚩 5 · Start", "🚩 5 · Старт", "🚩 5 · Start"),
            p=("Qahramon shu yerdan boshlaydi. Bu ham <b>bitta</b> bo'ladi. "
               "Startni tikan yoniga qo'ymang — bu eng keng tarqalgan dizayn xatosi!",
               "Герой начинает отсюда. Он тоже <b>один</b>. "
               "Не ставьте старт рядом с шипом — это самая частая ошибка дизайна!",
               "The hero starts here. Also <b>exactly one</b>. "
               "Never put the start next to a spike — the most common design mistake!")),
    ]) + "\n</div>",
))

S.append(slide(
    ph=("Level kodi", "Код уровня", "Level code"), time="14–18",
    eyebrow=("Jadvaldan matnga", "Из таблицы в текст", "From table to text"),
    title=("Level kodi — bu 200 katakning bitta qatorga siqilgani",
           "Код уровня — это 200 клеток, сжатые в одну строку",
           "A level code is 200 cells squeezed into one line"),
    body='<div class="cols c2">\n'
         + box("green", ("Qanday hosil bo'ladi", "Как он получается", "How it is made"),
               items=[
                   ("Redaktor jadvalni <b>yuqoridan pastga</b>, chapdan o'ngga o'qiydi.",
                    "Редактор читает таблицу <b>сверху вниз</b>, слева направо.",
                    "The editor reads the table <b>top to bottom</b>, left to right."),
                   ("Har katakning raqamini ketma-ket yozadi.",
                    "Записывает число каждой клетки подряд.",
                    "It writes each cell's number in order."),
                   ("Bir xil raqamlar ketma-ket kelsa — <b>qisqartiradi</b>: "
                    "<code>0000000</code> o'rniga <code>7a</code>.",
                    "Если одинаковые числа идут подряд — <b>сокращает</b>: "
                    "вместо <code>0000000</code> пишет <code>7a</code>.",
                    "Repeated numbers get <b>shortened</b>: "
                    "<code>7a</code> instead of <code>0000000</code>."),
                   ("Natija — qisqa kod, odatda 40–70 belgi. Uni qo'lda ko'chirish mumkin!",
                    "Результат — короткий код, обычно 40–70 символов. Его можно переписать от руки!",
                    "The result is a short code, usually 40–70 characters. You can copy it by hand!"),
               ])
         + "\n"
         + box("purple", ("Haqiqiy misol", "Настоящий пример", "A real example"),
               extra_html=code(
                   "Jadval (3 qator):\n"
                   "  0 0 0 0 0 0\n"
                   "  0 0 2 0 3 0\n"
                   "  1 1 1 1 1 1\n\n"
                   "Level kodi:\n"
                   "  8a1c1a1d1a6b\n\n"
                   "a=0  b=1  c=2  d=3\n"
                   "8a = sakkizta nol"))
         + "\n</div>\n"
         + box("accent", ("🎓 Bu usulning kattalar tilidagi nomi",
                          "🎓 Как это называется у взрослых",
                          "🎓 The grown-up name for this trick"),
               p=("Jadvalni matnga aylantirish — <b>serializatsiya</b>, "
                  "takrorlanishni qisqartirish esa — <b>siqish</b> (compression). "
                  "Aynan shu ikki usul bilan telefoningiz rasmlarni va videolarni "
                  "internetga yuboradi.",
                  "Превращение таблицы в текст — <b>сериализация</b>, а сокращение "
                  "повторов — <b>сжатие</b> (compression). Именно этими двумя приёмами "
                  "ваш телефон отправляет фотографии и видео в интернет.",
                  "Turning a table into text is <b>serialization</b>; shortening repeats "
                  "is <b>compression</b>. These two tricks are exactly how your phone "
                  "sends photos and videos over the internet.")),
))

S.append(slide(
    ph=("Dizayn qoidalari", "Правила дизайна", "Design rules"), time="18–23",
    eyebrow=("Yaxshi level qanday bo'ladi", "Каким бывает хороший уровень", "What a good level looks like"),
    title=("Uchta qoida — va levelingiz professional ko'rinadi",
           "Три правила — и ваш уровень выглядит профессионально",
           "Three rules and your level looks professional"),
    body='<div class="cols c3">\n' + "\n".join([
        box("green", ("1 · Boshlanish xavfsiz", "1 · Начало безопасно", "1 · A safe start"),
            p=("Start atrofidagi 3 katak <b>bo'sh</b> bo'lsin. O'yinchi birinchi soniyada "
               "o'lsa — u o'yinni yomon deb hisoblaydi, o'zini emas.",
               "3 клетки вокруг старта должны быть <b>пустыми</b>. Если игрок умирает "
               "в первую секунду — он винит игру, а не себя.",
               "Keep the 3 cells around the start <b>empty</b>. If a player dies in the "
               "first second they blame the game, not themselves.")),
        box("purple", ("2 · Qiyinlik asta oshadi", "2 · Сложность растёт плавно",
                       "2 · Difficulty ramps up"),
            p=("Chapda oson, o'ngda qiyin. Birinchi tikan yakka tursin, keyin ikkitasi, "
               "keyin dushman. <b>Eng qiyin joy — finish oldida.</b>",
               "Слева легко, справа сложно. Первый шип пусть стоит один, потом два, "
               "потом враг. <b>Самое сложное — перед финишем.</b>",
               "Easy on the left, hard on the right. Let the first spike stand alone, "
               "then two, then an enemy. <b>The hardest bit sits before the finish.</b>")),
        box("accent", ("3 · Har doim yo'l bor", "3 · Проход есть всегда", "3 · A path always exists"),
            p=("Har to'siqdan <b>o'tish yo'li</b> qolsin. Qahramon 3 katak balandlikka "
               "sakraydi — undan baland devor <b>o'tib bo'lmaydigan</b> devor.",
               "От каждого препятствия должен быть <b>проход</b>. Герой прыгает на 3 клетки "
               "в высоту — стена выше становится <b>непроходимой</b>.",
               "Every obstacle needs a <b>way through</b>. The hero jumps 3 cells high — "
               "a taller wall becomes <b>impassable</b>.")),
    ]) + "\n</div>\n"
         + box("", ("🔎 Redaktor sizga yordam beradi", "🔎 Редактор вам поможет",
                    "🔎 The editor helps you"),
               p=("Yuqoridagi <b>\"Tekshirish\"</b> tugmasini bossangiz, redaktor levelni "
                  "avtomatik tekshiradi: start bormi, finish bormi, o'tish yo'li bormi. "
                  "Muammo topilsa — qizil xabar chiqadi va joyi ko'rsatiladi.",
                  "Нажмите кнопку <b>«Проверить»</b> сверху, и редактор проверит уровень "
                  "автоматически: есть ли старт, есть ли финиш, есть ли проход. "
                  "Если найдётся проблема — появится красное сообщение с указанием места.",
                  "Press the <b>\"Check\"</b> button at the top and the editor validates the "
                  "level automatically: is there a start, a finish, a path through? "
                  "If something is wrong a red message points at the spot.")),
))

S.append(slide(
    ph=("Sinov", "Тестирование", "Playtesting"), time="23–26",
    eyebrow=("O'zingiz o'ynab ko'ring", "Сыграйте сами", "Play it yourself"),
    title=("Qurgan levelingizni o'zingiz o'ynamaguningizcha u tayyor emas",
           "Пока вы не сыграли в свой уровень, он не готов",
           "Your level is not finished until you have played it"),
    body='<div class="cols c2">\n'
         + box("accent", ("Dizaynerning eng katta xatosi", "Главная ошибка дизайнера",
                          "A designer's biggest mistake"),
               p=("Siz levelni <b>bilasiz</b> — qayerda tikan borligini, qayerdan sakrash "
                  "kerakligini yoddan bilasiz. Shuning uchun sizga u oson tuyuladi. "
                  "Lekin sinfdoshingiz buni <b>birinchi marta</b> ko'radi!",
                  "Вы <b>знаете</b> свой уровень — помните наизусть, где шип и откуда прыгать. "
                  "Поэтому вам он кажется лёгким. Но одноклассник видит его "
                  "<b>в первый раз</b>!",
                  "You <b>know</b> your level — you remember where every spike is and where "
                  "to jump. So it feels easy to you. But your classmate sees it "
                  "<b>for the first time</b>!"))
         + "\n"
         + box("green", ("Sinov tartibi", "Порядок тестирования", "Testing order"),
               items=[
                   ("<b>▶ O'ynash</b> tugmasini bosing va levelni boshidan oxirigacha o'ting.",
                    "Нажмите <b>▶ Играть</b> и пройдите уровень от начала до конца.",
                    "Press <b>▶ Play</b> and clear the level from start to finish."),
                   ("O'ta olmadingizmi? Demak level <b>juda qiyin</b> — tuzating.",
                    "Не прошли? Значит уровень <b>слишком сложный</b> — исправьте.",
                    "Could not finish it? Then it is <b>too hard</b> — fix it."),
                   ("Birinchi urinishda o'tdingizmi? Demak <b>juda oson</b> — to'siq qo'shing.",
                    "Прошли с первой попытки? Значит <b>слишком легко</b> — добавьте препятствий.",
                    "Cleared it first try? Then it is <b>too easy</b> — add an obstacle."),
                   ("Maqsad: <b>3–5 urinishda</b> o'tiladigan level. Mana shu ideal.",
                    "Цель: уровень проходится <b>с 3–5 попытки</b>. Вот это идеал.",
                    "Target: the level takes <b>3–5 attempts</b>. That is the sweet spot."),
               ])
         + "\n</div>",
))

S.append(slide(
    ph=("Amaliyot", "Практика", "Practice"), time="26–38",
    eyebrow=("Laboratoriya · 12 daqiqa", "Лаборатория · 12 минут", "Lab · 12 minutes"),
    title=("Qurish vaqti: editor/index.html ni oching",
           "Время строить: откройте editor/index.html",
           "Build time: open editor/index.html"),
    body='<div class="cols c4">\n' + "\n".join([
        box("purple", ("1 · Skelet (3 daq)", "1 · Скелет (3 мин)", "1 · Skeleton (3 min)"),
            p=("🚩 Start ni chapga, 🏁 Finish ni o'ngga qo'ying. Pastki qatorni "
               "🟦 platforma bilan to'ldiring. Hozircha to'siq yo'q.",
               "Поставьте 🚩 Старт слева, 🏁 Финиш справа. Заполните нижнюю строку "
               "🟦 платформой. Препятствий пока нет.",
               "Put 🚩 Start on the left, 🏁 Finish on the right. Fill the bottom row "
               "with 🟦 platform. No obstacles yet.")),
        box("accent", ("2 · Qiyinlik (4 daq)", "2 · Сложность (4 мин)", "2 · Difficulty (4 min)"),
            p=("8–12 ta 🔺 tikan va 1–3 ta 🤖 dushman qo'ying. Chapdan o'ngga "
               "<b>asta qiyinlashtiring</b>.",
               "Добавьте 8–12 🔺 шипов и 1–3 🤖 врагов. Слева направо "
               "<b>постепенно усложняйте</b>.",
               "Add 8–12 🔺 spikes and 1–3 🤖 enemies. Ramp the difficulty "
               "<b>left to right</b>.")),
        box("green", ("3 · Tekshirish (2 daq)", "3 · Проверка (2 мин)", "3 · Check (2 min)"),
            p=("<b>🔎 Tekshirish</b> tugmasini bosing. Qizil xabarlar qolmasin. "
               "Keyin <b>▶ O'ynash</b> — 3–5 urinishda o'tsin.",
               "Нажмите <b>🔎 Проверить</b>. Красных сообщений быть не должно. "
               "Затем <b>▶ Играть</b> — должно проходиться с 3–5 попытки.",
               "Press <b>🔎 Check</b>. No red messages should remain. "
               "Then <b>▶ Play</b> — it should take 3–5 attempts.")),
        box("", ("4 · Almashish (3 daq)", "4 · Обмен (3 мин)", "4 · Swap (3 min)"),
            p=("<b>📋 Kodni ko'chirish</b> → kodni varaqaga yozing va qo'shningizga bering. "
               "Uning kodini <b>📥 Yuklash</b> orqali oching va o'ynang!",
               "<b>📋 Скопировать код</b> → запишите код в лист и отдайте соседу. "
               "Его код откройте через <b>📥 Загрузить</b> и сыграйте!",
               "<b>📋 Copy code</b> → write it on your worksheet and hand it to your "
               "neighbour. Open theirs with <b>📥 Load</b> and play!")),
    ]) + "\n</div>",
))

S.append(slide(
    ph=("Ulashish", "Обмен", "Sharing"), time="38–41",
    eyebrow=("Eng qiziqarli qism", "Самая интересная часть", "The best part"),
    title=("Sinfdoshingizning leveli — bu sizning haqiqiy imtihoningiz",
           "Уровень одноклассника — ваш настоящий экзамен",
           "Your classmate's level is your real exam"),
    body='<div class="cols c2">\n'
         + box("accent", ("Kodni qanday uzatasiz", "Как передать код", "How to hand over the code"),
               items=[
                   ("<b>📋 Kodni ko'chirish</b> tugmasini bosing — kod buferga tushadi.",
                    "Нажмите <b>📋 Скопировать код</b> — код попадёт в буфер обмена.",
                    "Press <b>📋 Copy code</b> — the code goes to the clipboard."),
                   ("Kodni <b>varaqaning katagiga yozing</b> — bu uy vazifasining bir qismi.",
                    "Впишите код <b>в рамку рабочего листа</b> — это часть домашнего задания.",
                    "Write the code <b>in the worksheet box</b> — it is part of the homework."),
                   ("Qo'shningizga bering, uniki sizga. <b>📥 Yuklash</b> ga qo'ying.",
                    "Отдайте соседу, возьмите его. Вставьте в <b>📥 Загрузить</b>.",
                    "Swap with your neighbour. Paste theirs into <b>📥 Load</b>."),
               ])
         + "\n"
         + box("green", ("Qo'shningizga aytiladigan 2 ta fikr",
                         "Два отзыва для соседа", "Two pieces of feedback"),
               items=[
                   ("<b>Bitta yaxshi narsa:</b> \"Bu yerdagi sakrash juda zo'r chiqibdi\".",
                    "<b>Одно хорошее:</b> «Вот этот прыжок получился отличным».",
                    "<b>One good thing:</b> \"That jump right there works great\"."),
                   ("<b>Bitta taklif:</b> \"Bu joyda tikan juda ko'p, ikkitasini olib tashla\".",
                    "<b>Одно предложение:</b> «Здесь слишком много шипов, убери два».",
                    "<b>One suggestion:</b> \"Too many spikes here, remove two\"."),
                   ("Faqat \"yomon\" yoki \"zo'r\" demang — bu yordam bermaydi. "
                    "<b>Aniq joyni</b> ko'rsating.",
                    "Не говорите просто «плохо» или «круто» — это не помогает. "
                    "Указывайте <b>конкретное место</b>.",
                    "Never just say \"bad\" or \"cool\" — that does not help. "
                    "Point at a <b>specific spot</b>."),
               ])
         + "\n</div>",
))

S.append(slide(
    ph=("Kasb", "Профессия", "Career"), time="41–43",
    eyebrow=("Bu nimaga kerak", "Зачем это нужно", "Why this matters"),
    title=("Level dizayneri — bu haqiqiy kasb",
           "Дизайнер уровней — это настоящая профессия",
           "Level designer is a real job"),
    body='<div class="cols c3">\n' + "\n".join([
        box("purple", ("Nima qiladi", "Чем занимается", "What they do"),
            p=("O'yin studiyasida level dizayneri kun bo'yi maydonlarni quradi, sinaydi "
               "va qayta quradi. Bitta level ustida <b>bir necha hafta</b> ishlashi mumkin.",
               "В игровой студии дизайнер уровней целый день строит площадки, тестирует "
               "и перестраивает. Над одним уровнем он может работать <b>несколько недель</b>.",
               "At a game studio a level designer builds, tests and rebuilds arenas all day. "
               "One level can take them <b>several weeks</b>.")),
        box("green", ("Qanday o'rganiladi", "Как этому учатся", "How you learn it"),
            p=("Aynan bugungidek: kichik redaktorda ko'p level qurib, ularni "
               "boshqalarga o'ynatib. <b>Miqdor sifatga aylanadi.</b>",
               "Ровно так, как сегодня: строить много уровней в простом редакторе и "
               "давать другим играть. <b>Количество превращается в качество.</b>",
               "Exactly like today: build many levels in a simple editor and let others "
               "play them. <b>Quantity turns into quality.</b>")),
        box("accent", ("Bugun nima qildingiz", "Что вы сделали сегодня", "What you did today"),
            p=("Siz maydon qurdingiz, uni sinadingiz, kodga aylantirdingiz va "
               "foydalanuvchidan <b>fikr oldingiz</b>. Bu — professional ish tsiklining "
               "aynan o'zi.",
               "Вы построили площадку, протестировали её, превратили в код и получили "
               "<b>отзыв пользователя</b>. Это в точности профессиональный рабочий цикл.",
               "You built an arena, tested it, turned it into code and collected "
               "<b>user feedback</b>. That is precisely the professional workflow.")),
    ]) + "\n</div>",
))

S.append(slide(
    ph=("AI yordamchi", "AI помощник", "AI helper"), time="43–44",
    eyebrow=("Tayyor promptlar", "Готовые промпты", "Ready-made prompts"),
    title=("AI dan levelingizni baholashni so'rang",
           "Попросите AI оценить ваш уровень",
           "Ask the AI to review your level"),
    body='<div class="cols c2">\n'
         + box("purple", ("Nusxa oling va ChatGPT/Claude ga tashlang",
                          "Скопируйте и отправьте в ChatGPT/Claude",
                          "Copy and paste into ChatGPT/Claude"),
               extra_html=code(
                   "1) Я делаю 2D-платформер. Уровень это сетка\n"
                   "   20x10. Герой прыгает на 3 клетки в высоту.\n"
                   "   Сколько шипов и врагов поставить, чтобы\n"
                   "   уровень проходился с 3-5 попытки?\n\n"
                   "2) Объясни простыми словами, что такое\n"
                   "   сериализация, ученику 6 класса.\n\n"
                   "3) Придумай название для моего уровня, где\n"
                   "   есть лазеры, два врага и узкий проход."))
         + "\n"
         + box("accent", ("⚠️ Esda tuting", "⚠️ Помните", "⚠️ Remember"),
               items=[
                   ("AI sizning levelingizni <b>ko'rmaydi</b> — faqat siz tasvirlagan "
                    "narsani biladi.",
                    "AI <b>не видит</b> ваш уровень — он знает только то, что вы описали.",
                    "The AI <b>cannot see</b> your level — it only knows what you described."),
                   ("Qiziqarli yoki zerikarli ekanini <b>faqat o'ynagan odam</b> aytadi.",
                    "Интересно или скучно — скажет <b>только тот, кто сыграл</b>.",
                    "Only <b>someone who played it</b> can tell you if it is fun."),
                   ("Shuning uchun eng qimmatli fikr — <b>qo'shningizniki</b>, AI niki emas.",
                    "Поэтому самый ценный отзыв — <b>от соседа</b>, а не от AI.",
                    "So the most valuable feedback is <b>your neighbour's</b>, not the AI's."),
               ])
         + "\n</div>",
))

S.append(slide(
    ph=("Yakun", "Итоги", "Summary"), time="44–45",
    eyebrow=("Uy vazifasi va baholash", "Домашнее задание и оценка", "Homework and grading"),
    title=("Uy vazifasi: levelingizning kodi va sinov hisoboti (10 ball)",
           "Домашнее задание: код уровня и отчёт о тестировании (10 баллов)",
           "Homework: your level code and test report (10 points)"),
    body='<div class="cols c2">\n'
         + box("green", ("Nima qilish kerak", "Что нужно сделать", "What to do"),
               items=[
                   ("O'z levelingizning <b>kodini</b> varaqaga to'liq ko'chiring.",
                    "Полностью перепишите <b>код</b> своего уровня в рабочий лист.",
                    "Copy your level's <b>code</b> onto the worksheet in full."),
                   ("Levelingizga <b>nom</b> bering va 3 ta to'siqni sanab o'ting.",
                    "Придумайте <b>название</b> уровня и перечислите 3 препятствия.",
                    "Give your level a <b>name</b> and list its 3 obstacles."),
                   ("Qo'shningiz levelni <b>necha urinishda</b> o'tdi — yozing.",
                    "Запишите, <b>с какой попытки</b> сосед прошёл ваш уровень.",
                    "Write down <b>how many attempts</b> your neighbour needed."),
                   ("Qo'shningizga bergan <b>2 ta fikringizni</b> yozing.",
                    "Запишите <b>2 своих отзыва</b> соседу.",
                    "Write the <b>2 pieces of feedback</b> you gave your neighbour."),
               ])
         + "\n"
         + box("accent", ("Baholash mezoni", "Критерии оценки", "Grading rubric"),
               extra_html='<ul class="plain">\n'
               + '  <li><span class="t" %s>Level kodi to\'liq ko\'chirilgan — <b>3 ball</b></span></li>\n'
               % i18n("Level kodi to'liq ko'chirilgan — <b>3 ball</b>",
                      "Код уровня полностью переписан — <b>3 балла</b>",
                      "Level code copied in full — <b>3 points</b>")
               + '  <li><span class="t" %s>Nom va 3 ta to\'siq tavsifi — <b>2 ball</b></span></li>\n'
               % i18n("Nom va 3 ta to'siq tavsifi — <b>2 ball</b>",
                      "Название и описание 3 препятствий — <b>2 балла</b>",
                      "Name and 3 obstacles described — <b>2 points</b>")
               + '  <li><span class="t" %s>Sinov natijasi (urinishlar soni) — <b>2 ball</b></span></li>\n'
               % i18n("Sinov natijasi (urinishlar soni) — <b>2 ball</b>",
                      "Результат теста (число попыток) — <b>2 балла</b>",
                      "Test result (attempt count) — <b>2 points</b>")
               + '  <li><span class="t" %s>Qo\'shningizga 2 ta aniq fikr — <b>2 ball</b></span></li>\n'
               % i18n("Qo'shningizga 2 ta aniq fikr — <b>2 ball</b>",
                      "2 конкретных отзыва соседу — <b>2 балла</b>",
                      "2 specific notes for your neighbour — <b>2 points</b>")
               + '  <li><span class="t" %s>Ozodalik va tartib — <b>1 ball</b></span></li>\n'
               % i18n("Ozodalik va tartib — <b>1 ball</b>",
                      "Аккуратность и порядок — <b>1 балл</b>",
                      "Neatness and order — <b>1 point</b>")
               + "</ul>")
         + "\n</div>",
))


NOTES = {
    "uz": [
        ["Titul slayd",
         "Salom! Birinchi soatda biz dushmanni sozladik. Endi eng qiziq qismi: siz o'ynamaysiz, siz quruvchisiz. Bugun har biringiz o'z maydoningizni yaratadi va uni sinfdoshiga beradi.",
         "editor/index.html ni proyektorda oldindan oching."],
        ["O'yinchidan dizaynerga",
         "Ikki rolni ajrating. O'yinchi 'qanday o'tsam?' deb so'raydi, dizayner 'o'ynayotgan odam nimani his qiladi?' deb so'raydi. Roblox o'yinlarining ko'pini bolalar qurganini ayting — bu juda kuchli motivatsiya.",
         "Bolalardan Roblox'da o'zlari nimadir qurganmi deb so'rash."],
        ["Panjara",
         "Eng muhim tushuncha: kompyuter uchun level — raqamlar jadvali. Proyektorda redaktorni oching va panjarani ko'rsating. 20x10 = 200 katak.",
         "Redaktorda bir nechta katakni bosib, jadval o'zgarishini ko'rsatish."],
        ["Beshta bo'yoq",
         "Har bir bo'yoqni redaktorda bosib ko'rsating. Eng muhim ogohlantirish: tikan ko'p bo'lmasin. 50 ta tikan qiyin emas, asabiylashtiradi — bu farqni bolalar tushunishi kerak.",
         "Har bo'yoq bilan bir nechta katakni bo'yab ko'rsatish."],
        ["Level kodi",
         "Sehrli lahza. Redaktorda 'Kodni ko'chirish' ni bosing va ekranda qisqa kod chiqishini ko'rsating. Keyin bitta katakni o'zgartiring va kod ham o'zgarishini ko'rsating. Bolalar hayratlanadi.",
         "Kodni o'zgartirib ko'rsatish: bitta katak = kod o'zgaradi."],
        ["Dizayn qoidalari",
         "Uchta qoidani aniq ayting. Ayniqsa birinchisi muhim: start yonida tikan bo'lmasin. Bu eng ko'p uchraydigan xato va uni oldindan aytib qo'ysangiz yarim sinf xatodan qutuladi.",
         "Doskada yomon va yaxshi start misolini chizish."],
        ["Sinov (playtesting)",
         "Kalit fikr: siz o'z levelingizni bilasiz, shuning uchun u sizga oson. Maqsad — 3-5 urinishda o'tiladigan level. Bu raqamni doskaga yozib qo'ying.",
         "Doskaga '3-5 urinish' deb yozib qo'yish."],
        ["Amaliyot 12 daqiqa",
         "Eng uzun qism. To'rt bosqichni doskada vaqt bilan yozib qo'ying: skelet 3, qiyinlik 4, tekshirish 2, almashish 3. Vaqtni ovoz chiqarib e'lon qiling.",
         "Har bosqich oxirida vaqtni e'lon qilish. Sinf bo'ylab yurish."],
        ["Ulashish",
         "Eng qiziq lahza. Kod almashishni tartibli qiling — qo'shni bilan, o'rnidan turmasdan. Fikr bildirishda 'yomon' emas, aniq joy ko'rsatilsin.",
         "Kod almashishni nazorat qilish. Varaqaga kod yozilganini tekshirish."],
        ["Kasb",
         "Bolalarga ayting: siz bugun professional ish tsiklini bajardingiz — qurdingiz, sinadingiz, fikr oldingiz. Bu o'yin studiyasidagi kunning aynan o'zi.",
         "Qisqa, 1-2 daqiqa. Motivatsiya uchun."],
        ["AI bilan ishlash",
         "Muhim nuance: AI levelni ko'rmaydi. Shuning uchun uning maslahati umumiy bo'ladi, qo'shningizning fikri esa aniq. Bolalar bu farqni tushunsin.",
         "Bitta ekranda AI javobini ko'rsatib, uning umumiyligini tahlil qilish."],
        ["Yakun va baholash",
         "Varaqalarni yig'ing va kod yozilganini tekshiring — kodsiz varaqa 3 balldan mahrum. Uy vazifasini e'lon qiling.",
         "Varaqalarni yig'ish, kod katagi to'ldirilganini tekshirish."],
    ],
    "ru": [
        ["Титульный слайд",
         "Привет! На первом часе мы настроили врага. Теперь самое интересное: вы не играете, вы строите. Сегодня каждый создаст свою площадку и отдаст её однокласснику.",
         "Заранее откройте editor/index.html на проекторе."],
        ["Из игрока в дизайнеры",
         "Разделите две роли. Игрок спрашивает «как мне пройти?», дизайнер — «что почувствует тот, кто играет?». Скажите, что большую часть игр в Roblox построили дети — это очень сильная мотивация.",
         "Спросить, строил ли кто-то что-то в Roblox."],
        ["Сетка",
         "Главное понятие: для компьютера уровень — это таблица чисел. Откройте редактор на проекторе и покажите сетку. 20x10 = 200 клеток.",
         "Нажать на несколько клеток и показать, как меняется таблица."],
        ["Пять красок",
         "Покажите каждую краску прямо в редакторе. Самое важное предупреждение: шипов не должно быть много. 50 шипов — это не сложно, это раздражает; эту разницу дети должны понять.",
         "Закрасить несколько клеток каждой краской."],
        ["Код уровня",
         "Магический момент. Нажмите «Скопировать код» и покажите на экране короткий код. Затем измените одну клетку и покажите, что код тоже изменился. Дети удивляются.",
         "Показать: одна клетка изменилась — код изменился."],
        ["Правила дизайна",
         "Чётко назовите три правила. Особенно первое: рядом со стартом не должно быть шипов. Это самая частая ошибка, и если предупредить заранее — половина класса её избежит.",
         "Нарисовать на доске плохой и хороший старт."],
        ["Тестирование",
         "Ключевая мысль: вы знаете свой уровень, поэтому он кажется вам лёгким. Цель — уровень проходится с 3-5 попытки. Напишите это число на доске.",
         "Написать на доске «3-5 попыток»."],
        ["Практика 12 минут",
         "Самая длинная часть. Напишите на доске четыре этапа с таймингом: скелет 3, сложность 4, проверка 2, обмен 3. Объявляйте время вслух.",
         "Объявлять время в конце каждого этапа. Ходить по классу."],
        ["Обмен",
         "Самый интересный момент. Организуйте обмен кодами по порядку — с соседом, не вставая. В отзывах не «плохо», а конкретное место.",
         "Контролировать обмен. Проверить, что код записан в лист."],
        ["Профессия",
         "Скажите детям: сегодня вы прошли профессиональный рабочий цикл — построили, протестировали, получили отзыв. Это в точности рабочий день в игровой студии.",
         "Коротко, 1-2 минуты. Для мотивации."],
        ["Работа с AI",
         "Важный нюанс: AI не видит уровень. Поэтому его совет будет общим, а отзыв соседа — конкретным. Дети должны почувствовать эту разницу.",
         "Показать ответ AI на одном экране и разобрать его общность."],
        ["Итоги и оценивание",
         "Соберите листы и проверьте, что код записан — лист без кода теряет 3 балла. Объявите домашнее задание.",
         "Собрать листы, проверить заполнение рамки с кодом."],
    ],
    "en": [
        ["Title slide",
         "Hello! In hour one we tuned the enemy. Now the best part: you are not playing, you are building. Today each of you creates an arena and hands it to a classmate.",
         "Pre-open editor/index.html on the projector."],
        ["From player to designer",
         "Separate the two roles. A player asks 'how do I get through?', a designer asks 'what will the player feel?'. Mention that most Roblox games were built by kids — a very strong motivator.",
         "Ask whether anyone has built something in Roblox."],
        ["The grid",
         "The key concept: to a computer a level is a table of numbers. Open the editor on the projector and show the grid. 20x10 = 200 cells.",
         "Click a few cells and show the table changing."],
        ["Five paints",
         "Demonstrate each paint in the editor. The key warning: do not overdo spikes. 50 spikes is not hard, it is annoying — the class must feel that difference.",
         "Paint a few cells with each tool."],
        ["The level code",
         "The magic moment. Press 'Copy code' and show the short code on screen. Then change one cell and show the code changing too. This surprises them.",
         "Demonstrate: one cell changed, the code changed."],
        ["Design rules",
         "State the three rules clearly. Rule one matters most: no spikes next to the start. It is the most common mistake, and warning them up front saves half the class.",
         "Sketch a bad and a good start on the board."],
        ["Playtesting",
         "Key idea: you know your own level, so it feels easy to you. Target: clearable in 3-5 attempts. Write that number on the board.",
         "Write '3-5 attempts' on the board."],
        ["Practice, 12 minutes",
         "The longest stretch. Put the four stages with timings on the board: skeleton 3, difficulty 4, check 2, swap 3. Call out the time aloud.",
         "Announce the time at each stage boundary. Walk the room."],
        ["Sharing",
         "The best moment. Keep the code swap orderly — with a neighbour, nobody leaving their seat. Feedback must name a spot, not just say 'bad'.",
         "Supervise the swap. Check the code is written on the sheet."],
        ["Career",
         "Tell them: today you ran a professional workflow — build, test, collect feedback. That is exactly a day at a game studio.",
         "Keep it short, 1-2 minutes. Motivation only."],
        ["Working with AI",
         "An important nuance: the AI cannot see the level. So its advice stays generic while the neighbour's feedback is specific. Let them feel that difference.",
         "Show one AI answer on screen and discuss how generic it is."],
        ["Summary and grading",
         "Collect the sheets and check the code is written — a sheet with no code loses 3 points. Announce the homework.",
         "Collect sheets, verify the code box is filled."],
    ],
}

VARAQA = (
    sheet_header(
        ("16-dars: O'z Levelingni Qur — Redaktor va Level Kodi",
         "Урок 16: Построй Свой Уровень — Редактор и Код Уровня",
         "Lesson 16: Build Your Own Level — Editor and Level Code"),
        ("Target International School · 5–6-sinf · 4-hafta (2-soat)",
         "Target International School · 5–6 класс · 4-я неделя (2-й час)",
         "Target International School · Grades 5–6 · Week 4 (Hour 2)"))
    + mission(
        ("🎯 Missiya: level quring, sinang va ulashing",
         "🎯 Миссия: построй уровень, протестируй и обменяйся",
         "🎯 Mission: build a level, test it, share it"),
        ("<b>editor/index.html</b> ni oching. Skelet → qiyinlik → tekshirish → almashish. "
         "Maqsad: level <b>3–5 urinishda</b> o'tilsin. Oxirida level kodini shu varaqaga "
         "ko'chiring — kodsiz uy vazifasi qabul qilinmaydi.",
         "Откройте <b>editor/index.html</b>. Скелет → сложность → проверка → обмен. "
         "Цель: уровень проходится <b>с 3–5 попытки</b>. В конце перепишите код уровня "
         "в этот лист — без кода домашнее задание не принимается.",
         "Open <b>editor/index.html</b>. Skeleton → difficulty → check → swap. "
         "Target: the level clears in <b>3–5 attempts</b>. At the end copy the level code "
         "onto this sheet — homework without the code is not accepted."))
    + table(
        [("Bosqich", "Этап", "Stage"),
         ("Nima qilasiz", "Что делаете", "What you do"),
         ("Natija", "Результат", "Result"),
         ("✔", "✔", "✔")],
        [[("1 · Skelet", "1 · Скелет", "1 · Skeleton"),
          ("🚩 Start, 🏁 Finish va pastki 🟦 platforma qatori",
           "🚩 Старт, 🏁 Финиш и нижний ряд 🟦 платформы",
           "🚩 Start, 🏁 Finish and the bottom 🟦 platform row"),
          ("Panjara o'lchami: 20 × 10",
           "Размер сетки: 20 × 10",
           "Grid size: 20 × 10"), None],
         [("2 · Qiyinlik", "2 · Сложность", "2 · Difficulty"),
          ("🔺 tikan va 🤖 dushman qo'yish, chapdan o'ngga qiyinlashtirish",
           "Расставить 🔺 шипы и 🤖 врагов, усложняя слева направо",
           "Place 🔺 spikes and 🤖 enemies, ramping left to right"),
          ("Tikan: ____ ta · Dushman: ____ ta",
           "Шипов: ____ · Врагов: ____",
           "Spikes: ____ · Enemies: ____"), None],
         [("3 · Tekshirish", "3 · Проверка", "3 · Check"),
          ("🔎 Tekshirish tugmasi — qizil xabar qolmasin",
           "Кнопка 🔎 Проверить — красных сообщений быть не должно",
           "The 🔎 Check button — no red messages left"),
          ("O'zim necha urinishda o'tdim? ____",
           "С какой попытки прошёл сам? ____",
           "Attempts I needed myself: ____"), None],
         [("4 · Almashish", "4 · Обмен", "4 · Swap"),
          ("Kodni qo'shningizga bering, uniki bilan o'ynang",
           "Отдайте код соседу, сыграйте в его уровень",
           "Hand your code over, play your neighbour's"),
          ("Qo'shnim necha urinishda o'tdi? ____",
           "С какой попытки прошёл сосед? ____",
           "Attempts my neighbour needed: ____"), None]])
    + '    <div style="margin-bottom:7px">\n'
    + '      ' + el("h4", "🔑 Mening levelimning kodi (to'liq ko'chiring)",
                    "🔑 Код моего уровня (перепишите полностью)",
                    "🔑 My level code (copy it in full)",
                    extra='style="margin:0 0 3px; font-family:Manrope,sans-serif; font-size:8.2pt"') + "\n"
    + '      <div style="border:1px dashed var(--accent); border-radius:3px; min-height:15mm; padding:4px 6px; font-family:\'JetBrains Mono\',monospace; font-size:8pt; word-break:break-all;"></div>\n'
    + '      ' + el("p", "Levelning nomi: ______________________________",
                    "Название уровня: ______________________________",
                    "Level name: ______________________________",
                    extra='style="font-size:7.6pt; color:var(--ink-2); margin-top:4px"') + "\n"
    + "    </div>\n"
    + '    <div class="rubric-grid">\n'
    + sheet_box(
        ("💬 Qo'shningizga 2 ta aniq fikr",
         "💬 2 конкретных отзыва соседу",
         "💬 2 specific notes for your neighbour"),
        writelines(2, ("👍 Bitta yaxshi narsa (aniq joyni ko'rsating):",
                       "👍 Одно хорошее (укажите конкретное место):",
                       "👍 One good thing (name the exact spot):"))
        + "\n"
        + writelines(2, ("💡 Bitta taklif (nimani o'zgartirish kerak):",
                         "💡 Одно предложение (что изменить):",
                         "💡 One suggestion (what to change):")))
    + "\n"
    + sheet_box(
        ("📊 Baholash mezoni (10 ball)",
         "📊 Критерии оценки (10 баллов)",
         "📊 Grading rubric (10 points)"),
        rubric([
            (("Level kodi to'liq ko'chirilgan", "Код уровня переписан полностью",
              "Level code copied in full"), "3"),
            (("Nom va 3 ta to'siq tavsifi", "Название и 3 препятствия",
              "Name and 3 obstacles"), "2"),
            (("Sinov natijasi (urinishlar)", "Результат теста (попытки)",
              "Test result (attempts)"), "2"),
            (("2 ta aniq fikr", "2 конкретных отзыва", "2 specific notes"), "2"),
            (("Ozodalik va tartib", "Аккуратность и порядок", "Neatness and order"), "1"),
        ], "10"))
    + "\n    </div>\n  </div>\n"
    + sign_box()
)

if __name__ == "__main__":
    print(Lesson(D, TITLES, SHEET_TITLES, "vc-notes-5-16", S, NOTES, VARAQA).build())
