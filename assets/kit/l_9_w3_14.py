# -*- coding: utf-8 -*-
"""9-sinf · 3-hafta · 14-dars — Pull Request va Kod Ko'rigi: Diff, Izoh va Qaror."""

import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from build import (Lesson, slide, title_slide, box, code, el, i18n,
                   sheet_header, mission, table, sheet_box, rubric, writelines, sign_box)

D = "classes/9-sinf/3-hafta/14-dars-pull-request-va-kod-korigi"

TITLES = {
    "uz": "14-dars: Pull Request va Kod Ko'rigi — Diff, Izoh va Qaror",
    "ru": "Урок 14: Pull Request и Код-ревью — Diff, Комментарий и Решение",
    "en": "Lesson 14: Pull Requests and Code Review — Diff, Comments and Decisions",
}
SHEET_TITLES = {k: v + (" — Ish Varaqasi" if k == "uz" else
                        " — Рабочий Лист" if k == "ru" else " — Worksheet")
                for k, v in TITLES.items()}

S = []

S.append(title_slide(
    ph=("Kirish", "Введение", "Intro"), time="0–3",
    eyebrow=("Vibecoding · 14-dars · 9-sinf (Junior Vibecoder)",
             "Vibecoding · Урок 14 · 9 класс (Junior Vibecoder)",
             "Vibecoding · Lesson 14 · Grade 9 (Junior Vibecoder)"),
    h1=("Pull Request va Kod Ko'rigi: Kod Qanday Qabul Qilinadi",
        "Pull Request и Код-ревью: Как Код Попадает в Проект",
        "Pull Requests and Code Review: How Code Gets Accepted"),
    lede=("Birinchi soatda siz branch yaratdingiz va konfliktni yechdingiz. Lekin real "
          "jamoada <b>hech kim o'z kodini to'g'ridan-to'g'ri <code>main</code> ga "
          "qo'shmaydi</b>. Avval <b>Pull Request</b> ochiladi, keyin boshqa muhandis uni "
          "o'qib chiqadi va izoh yozadi. Bugun siz ikkala tomonni ham sinab ko'rasiz: "
          "PR yozuvchi va <b>reviewer</b>.",
          "На первом часе вы создали ветку и разрешили конфликт. Но в реальной команде "
          "<b>никто не вливает свой код прямо в <code>main</code></b>. Сначала "
          "открывается <b>Pull Request</b>, затем другой инженер читает его и пишет "
          "комментарии. Сегодня вы побываете с обеих сторон: автором PR и "
          "<b>ревьюером</b>.",
          "In hour one you created a branch and resolved a conflict. But in a real team "
          "<b>nobody pushes their code straight into <code>main</code></b>. First a "
          "<b>Pull Request</b> is opened, then another engineer reads it and leaves "
          "comments. Today you play both sides: the PR author and the <b>reviewer</b>."),
    meta=[("<b>Fan:</b> Vibecoding · Muhandislik jarayoni",
           "<b>Предмет:</b> Vibecoding · Инженерный процесс",
           "<b>Subject:</b> Vibecoding · Engineering Process"),
          ("<b>Kohorta:</b> 9-sinf Junior Vibecoder",
           "<b>Когорта:</b> 9 класс Junior Vibecoder",
           "<b>Cohort:</b> Grade 9 Junior Vibecoder"),
          ("<b>Hafta:</b> 3 (2-soat)", "<b>Неделя:</b> 3 (2-й час)", "<b>Week:</b> 3 (Hour 2)")],
))

S.append(slide(
    ph=("Nega kerak", "Зачем это нужно", "Why it matters"), time="3–7",
    eyebrow=("Xatoning narxi", "Цена ошибки", "The cost of a bug"),
    title=("Xato qancha kech topilsa, shuncha qimmat turadi",
           "Чем позже найдена ошибка, тем дороже она стоит",
           "The later a bug is found, the more it costs"),
    body='<div class="cols c4">\n' + "\n".join([
        box("green", ("Yozayotganda", "При написании", "While writing"),
            p=("Dasturchi o'zi sezadi va darhol tuzatadi. Narxi — <b>1 daqiqa</b>.",
               "Разработчик сам замечает и сразу исправляет. Цена — <b>1 минута</b>.",
               "The developer notices and fixes it at once. Cost — <b>1 minute</b>.")),
        box("purple", ("Kod ko'rigida", "На код-ревью", "At code review"),
            p=("Reviewer topadi. Tuzatish — <b>10 daqiqa</b>. Foydalanuvchi buni "
               "umuman ko'rmaydi.",
               "Находит ревьюер. Исправление — <b>10 минут</b>. Пользователь этого "
               "вообще не видит.",
               "The reviewer catches it. Fix — <b>10 minutes</b>. The user never "
               "sees it at all.")),
        box("amber" if False else "", ("Testlashda", "На тестировании", "In testing"),
            p=("Tester topadi, vazifa qaytariladi, kontekst yo'qolgan. "
               "Narxi — <b>1 kun</b>.",
               "Находит тестировщик, задача возвращается, контекст потерян. "
               "Цена — <b>1 день</b>.",
               "A tester finds it, the task bounces back, context is lost. "
               "Cost — <b>1 day</b>.")),
        box("accent", ("Ishlab turgan saytda", "На живом сайте", "In production"),
            p=("Foydalanuvchi topadi. Shoshilinch tuzatish, obro' zarari, ba'zan "
               "pul yo'qotish. Narxi — <b>hafta</b>.",
               "Находит пользователь. Срочное исправление, репутационный ущерб, иногда "
               "потеря денег. Цена — <b>неделя</b>.",
               "A user finds it. Hotfix, reputation damage, sometimes lost money. "
               "Cost — <b>a week</b>.")),
    ]) + "\n</div>\n"
         + box("purple", ("Kod ko'rigi faqat xato uchun emas",
                          "Код-ревью не только про ошибки",
                          "Code review is not only about bugs"),
               items=[
                   ("<b>Bilim tarqaladi.</b> Reviewer loyihaning yangi qismini "
                    "o'rganadi — kasallik yoki ishdan bo'shash loyihani to'xtatmaydi.",
                    "<b>Знания распространяются.</b> Ревьюер узнаёт новую часть проекта — "
                    "болезнь или увольнение не остановят работу.",
                    "<b>Knowledge spreads.</b> The reviewer learns a new part of the "
                    "project — illness or resignation will not stall the work."),
                   ("<b>Yagona standart.</b> Kod bir kishi yozgandek ko'rinadi, "
                    "garchi uni o'n kishi yozgan bo'lsa ham.",
                    "<b>Единый стандарт.</b> Код выглядит так, будто его написал один "
                    "человек, хотя писали десятеро.",
                    "<b>One standard.</b> The code reads as if one person wrote it, "
                    "even when ten people did."),
                   ("<b>Mas'uliyat bo'linadi.</b> Merge dan keyin kod jamoaniki, "
                    "bitta odamniki emas.",
                    "<b>Ответственность делится.</b> После merge код принадлежит команде, "
                    "а не одному человеку.",
                    "<b>Responsibility is shared.</b> After the merge the code belongs to "
                    "the team, not to one person."),
               ]),
))

S.append(slide(
    ph=("Jarayon", "Процесс", "The process"), time="7–11",
    eyebrow=("Pull Request nima", "Что такое Pull Request", "What a Pull Request is"),
    title=("PR — bu so'rov: \"mening branchimni <code>main</code> ga qo'shasizmi?\"",
           "PR — это просьба: «примете мою ветку в <code>main</code>?»",
           "A PR is a request: \"will you take my branch into <code>main</code>?\""),
    body='<div class="cols c2">\n'
         + box("green", ("To'liq yo'l", "Полный путь", "The full path"),
               extra_html=code(
                   "1. git switch -c fix/valyuta-nol\n"
                   "2. ... kod yoziladi, commitlar qilinadi ...\n"
                   "3. git push\n"
                   "4. GitHub da \"Open Pull Request\"\n"
                   "5. Reviewer diff ni o'qiydi va izoh yozadi\n"
                   "6. Muallif tuzatadi, yangi commit qo'shadi\n"
                   "7. Reviewer \"Approve\" beradi\n"
                   "8. Merge -> kod main ga tushdi\n"
                   "9. Branch o'chiriladi"))
         + "\n"
         + box("purple", ("PR nimalardan iborat", "Из чего состоит PR", "What a PR contains"),
               items=[
                   ("<b>Sarlavha</b> — bitta qatorda nima qilinganini aytadi.",
                    "<b>Заголовок</b> — одной строкой говорит, что сделано.",
                    "<b>Title</b> — says what was done in one line."),
                   ("<b>Tavsif</b> — <i>nega</i> kerak bo'lgani, qanday sinalgani.",
                    "<b>Описание</b> — <i>почему</i> это нужно и как проверено.",
                    "<b>Description</b> — <i>why</i> it was needed and how it was tested."),
                   ("<b>Diff</b> — barcha o'zgarishlar qator-baqator.",
                    "<b>Diff</b> — все изменения построчно.",
                    "<b>Diff</b> — every change, line by line."),
                   ("<b>Izohlar</b> — aniq qatorga bog'langan muhokama.",
                    "<b>Комментарии</b> — обсуждение, привязанное к конкретной строке.",
                    "<b>Comments</b> — discussion anchored to a specific line."),
                   ("<b>Tekshiruvlar (CI)</b> — testlar avtomatik ishga tushadi.",
                    "<b>Проверки (CI)</b> — тесты запускаются автоматически.",
                    "<b>Checks (CI)</b> — tests run automatically."),
               ])
         + "\n</div>",
))

S.append(slide(
    ph=("Diff", "Diff", "Diff"), time="11–16",
    eyebrow=("Reviewerning asosiy ko'nikmasi", "Главный навык ревьюера",
             "A reviewer's core skill"),
    title=("Diff o'qishni bilish — kod ko'rigining yarmi",
           "Умение читать diff — это половина код-ревью",
           "Reading a diff is half of code review"),
    body='<div class="cols c2">\n'
         + box("green", ("Unified diff formati", "Формат unified diff", "Unified diff format"),
               extra_html=code(
                   "@@ -14,7 +14,9 @@ function hisobla(a, b){\n"
                   "   var natija = 0;\n"
                   "-  natija = a / b;\n"
                   "+  if (b === 0) {\n"
                   "+    return 'Nolga bo\\'lib bo\\'lmaydi';\n"
                   "+  }\n"
                   "+  natija = a / b;\n"
                   "   return natija;\n"
                   " }"))
         + "\n"
         + box("purple", ("Har belgi nimani anglatadi", "Что означает каждый знак",
                          "What each marker means"),
               items=[
                   ("<code>-</code> qizil — <b>o'chirilgan</b> qator (eski versiya).",
                    "<code>-</code> красный — <b>удалённая</b> строка (старая версия).",
                    "<code>-</code> red — a <b>removed</b> line (the old version)."),
                   ("<code>+</code> yashil — <b>qo'shilgan</b> qator (yangi versiya).",
                    "<code>+</code> зелёный — <b>добавленная</b> строка (новая версия).",
                    "<code>+</code> green — an <b>added</b> line (the new version)."),
                   ("Belgisiz kulrang — <b>kontekst</b>, o'zgarmagan. U faqat "
                    "mo'ljal uchun ko'rsatiladi.",
                    "Серые без знака — <b>контекст</b>, не менялись. Показаны только "
                    "для ориентира.",
                    "Grey with no marker — <b>context</b>, unchanged. Shown only "
                    "for orientation."),
                   ("<code>@@ -14,7 +14,9 @@</code> — qaysi qatordan boshlab "
                    "nechta qator: eski faylda 14-dan 7 ta, yangisida 14-dan 9 ta.",
                    "<code>@@ -14,7 +14,9 @@</code> — с какой строки и сколько строк: "
                    "в старом файле с 14-й 7 строк, в новом с 14-й 9 строк.",
                    "<code>@@ -14,7 +14,9 @@</code> — from which line and how many: "
                    "7 lines from 14 in the old file, 9 from 14 in the new one."),
               ])
         + "\n</div>\n"
         + box("accent", ("⚠️ Diff ni o'qishdagi asosiy tuzoq",
                          "⚠️ Главная ловушка при чтении diff",
                          "⚠️ The main trap when reading a diff"),
               p=("Diff sizga <b>faqat o'zgargan joyni</b> ko'rsatadi. Lekin xato "
                  "ko'pincha <b>o'zgarish bilan qolgan kod o'rtasidagi bog'liqlikda</b> "
                  "bo'ladi. Shuning uchun tajribali reviewer diffni o'qib bo'lgach, "
                  "butun faylni ham ochib ko'radi.",
                  "Diff показывает <b>только изменённое место</b>. Но ошибка часто "
                  "прячется <b>во взаимодействии изменения с остальным кодом</b>. "
                  "Поэтому опытный ревьюер после diff открывает и весь файл целиком.",
                  "A diff shows you <b>only the changed spot</b>. But bugs often hide "
                  "<b>in how the change interacts with the rest of the code</b>. "
                  "That is why an experienced reviewer also opens the whole file.")),
))

S.append(slide(
    ph=("Yaxshi PR", "Хороший PR", "A good PR"), time="16–20",
    eyebrow=("Muallif tomonidan", "Со стороны автора", "From the author's side"),
    title=("Kichik PR tez qabul qilinadi. Katta PR haftalab yotadi.",
           "Маленький PR примут быстро. Большой пролежит неделями.",
           "A small PR gets merged fast. A big one sits for weeks."),
    body='<div class="cols c2">\n'
         + box("accent", ("❌ Yomon PR", "❌ Плохой PR", "❌ A bad PR"),
               items=[
                   ("<b>800 qator</b> o'zgarish. Reviewer charchaydi va "
                    "\"LGTM\" deb o'qimasdan tasdiqlaydi.",
                    "<b>800 строк</b> изменений. Ревьюер устаёт и ставит «LGTM», "
                    "не читая.",
                    "<b>800 lines</b> changed. The reviewer gets tired and stamps "
                    "\"LGTM\" without reading."),
                   ("<b>Bir nechta vazifa aralash:</b> yangi funksiya + refaktoring "
                    "+ dizayn + xato tuzatish.",
                    "<b>Несколько задач вперемешку:</b> новая функция + рефакторинг "
                    "+ дизайн + багфикс.",
                    "<b>Several tasks mixed:</b> a feature + refactoring + design "
                    "+ a bug fix."),
                   ("Tavsif: <b>\"tuzatishlar\"</b>. Reviewer nimani tekshirishini "
                    "bilmaydi.",
                    "Описание: <b>«исправления»</b>. Ревьюер не знает, что проверять.",
                    "Description: <b>\"fixes\"</b>. The reviewer does not know what "
                    "to check."),
               ])
         + "\n"
         + box("green", ("✅ Yaxshi PR", "✅ Хороший PR", "✅ A good PR"),
               items=[
                   ("<b>50–200 qator.</b> 20 daqiqada diqqat bilan o'qib chiqish mumkin.",
                    "<b>50–200 строк.</b> Можно внимательно прочитать за 20 минут.",
                    "<b>50–200 lines.</b> Can be read carefully in 20 minutes."),
                   ("<b>Bitta maqsad.</b> Sarlavhada \"va\" so'zi bo'lsa — PR ni "
                    "ikkiga bo'lish kerak.",
                    "<b>Одна цель.</b> Если в заголовке есть «и» — PR надо разделить "
                    "надвое.",
                    "<b>One purpose.</b> If the title contains \"and\", split the PR."),
                   ("Tavsifda: <b>nima, nega, qanday sinaldi</b>. UI o'zgarsa — "
                    "skrinshot.",
                    "В описании: <b>что, почему, как проверено</b>. Если менялся UI — "
                    "скриншот.",
                    "The description says <b>what, why, how it was tested</b>. "
                    "UI change — attach a screenshot."),
                   ("Muallif <b>o'zi birinchi bo'lib</b> diffni o'qib chiqadi.",
                    "Автор <b>сам первым</b> читает свой diff.",
                    "The author reads their own diff <b>first</b>."),
               ])
         + "\n</div>",
))

S.append(slide(
    ph=("Nimaga qaraladi", "На что смотреть", "What to look for"), time="20–25",
    eyebrow=("Reviewerning 4 darajasi", "4 уровня ревьюера", "The reviewer's 4 levels"),
    title=("Kodni to'rt daraja bo'yicha o'qing — shu tartibda",
           "Читайте код по четырём уровням — именно в этом порядке",
           "Read code on four levels — in this exact order"),
    body='<div class="cols c4">\n' + "\n".join([
        box("accent", ("1 · To'g'rimi?", "1 · Правильно?", "1 · Is it correct?"),
            p=("Kod <b>aytilgan ishni</b> qiladimi? Chegaraviy holatlar: nol, bo'sh "
               "massiv, manfiy son, yo'q internet. <b>Eng muhim daraja.</b>",
               "Делает ли код <b>то, что заявлено</b>? Граничные случаи: ноль, пустой "
               "массив, отрицательное число, нет интернета. <b>Самый важный уровень.</b>",
               "Does the code do <b>what it claims</b>? Edge cases: zero, empty array, "
               "negative numbers, no network. <b>The most important level.</b>")),
        box("purple", ("2 · Xavfsizmi?", "2 · Безопасно?", "2 · Is it safe?"),
            p=("Parol yoki API kalit kodda qolganmi? Foydalanuvchi kiritgan ma'lumot "
               "tekshirilganmi? (10-darsdagi mavzu.)",
               "Не остался ли пароль или API-ключ в коде? Проверены ли данные от "
               "пользователя? (Тема урока 10.)",
               "Is a password or API key left in the code? Is user input validated? "
               "(The topic of lesson 10.)")),
        box("green", ("3 · O'qilodimi?", "3 · Читаемо?", "3 · Is it readable?"),
            p=("O'zgaruvchi nomlari aniqmi? Funksiya juda uzun emasmi? "
               "Olti oydan keyin tushunarli bo'ladimi?",
               "Понятны ли имена переменных? Не слишком ли длинная функция? "
               "Будет ли понятно через полгода?",
               "Are the variable names clear? Is the function too long? "
               "Will it make sense in six months?")),
        box("", ("4 · Kerakmi?", "4 · Нужно ли?", "4 · Is it needed?"),
            p=("Bu kod umuman kerakmi? Balki tayyor yechim bor? Bu eng qiyin va eng "
               "qimmatli savol.",
               "Нужен ли этот код вообще? Может, есть готовое решение? Самый трудный "
               "и самый ценный вопрос.",
               "Is this code needed at all? Maybe a solution already exists? "
               "The hardest and most valuable question.")),
    ]) + "\n</div>\n"
         + box("purple", ("Tartib muhim", "Порядок важен", "The order matters"),
               p=("Agar siz bo'sh joy va nuqta-vergul haqida izoh yozishdan boshlasangiz, "
                  "<b>mantiqiy xatoni o'tkazib yuborasiz</b> — diqqat tugaydi. "
                  "Shuning uchun avval \"to'g'rimi?\", eng oxirida \"chiroylimi?\". "
                  "Formatlashni odam emas, <b>dastur</b> (Prettier) tekshirsin.",
                  "Если начать с комментариев про пробелы и точки с запятой, вы "
                  "<b>пропустите логическую ошибку</b> — внимание закончится. "
                  "Поэтому сначала «правильно?», и только в конце «красиво?». "
                  "Форматирование пусть проверяет <b>программа</b> (Prettier), а не человек.",
                  "If you start with comments about spaces and semicolons you will "
                  "<b>miss the logic bug</b> — your attention runs out. "
                  "So ask \"is it correct?\" first and \"is it pretty?\" last. "
                  "Let a <b>tool</b> (Prettier) check formatting, not a human.")),
))

S.append(slide(
    ph=("Izoh yozish", "Как писать комментарии", "Writing comments"), time="25–31",
    eyebrow=("Eng nozik ko'nikma", "Самый тонкий навык", "The most delicate skill"),
    title=("Izoh <b>kodga</b> yoziladi, odamga emas",
           "Комментарий пишется <b>к коду</b>, а не к человеку",
           "A comment is about the <b>code</b>, never the person"),
    body='<div class="cols c2">\n'
         + box("accent", ("❌ Shunday yozilmaydi", "❌ Так писать нельзя", "❌ Do not write this"),
               extra_html=code(
                   "\"Bu noto'g'ri.\"\n"
                   "\"Nega bunday qilding?\"\n"
                   "\"Sen JS ni bilmaysan shekilli.\"\n"
                   "\"Qayta yoz.\"\n"
                   "\"Yomon kod.\"\n\n"
                   "// Bularda: sabab yo'q, yechim yo'q,\n"
                   "// baho odamga berilgan."))
         + "\n"
         + box("green", ("✅ Shunday yoziladi", "✅ Так нужно", "✅ Write it like this"),
               extra_html=code(
                   "\"Agar b = 0 bo'lsa, bu yer Infinity\n"
                   " qaytaradi. Bo'lishdan oldin tekshiruv\n"
                   " qo'shsak bo'ladimi?\"\n\n"
                   "\"Bu funksiya 80 qator. Uni ikkiga\n"
                   " bo'lsak o'qish osonlashadi —\n"
                   " masalan, tekshiruvni ajratib.\"\n\n"
                   "// Bularda: muammo + sabab + taklif."))
         + "\n</div>\n"
         + box("purple", ("Izohni belgilash: uchta daraja",
                          "Маркировка комментария: три уровня",
                          "Labelling a comment: three levels"),
               items=[
                   ("<b>nit:</b> (nitpick) — mayda, ixtiyoriy. \"nit: bu yerda bo'sh "
                    "qator ortiqcha\". Muallif e'tiborsiz qoldirsa ham bo'ladi.",
                    "<b>nit:</b> (nitpick) — мелочь, необязательно. «nit: тут лишняя "
                    "пустая строка». Автор может проигнорировать.",
                    "<b>nit:</b> (nitpick) — minor, optional. \"nit: extra blank line "
                    "here\". The author may ignore it."),
                   ("<b>savol:</b> — siz tushunmadingiz, ayblamayapsiz. "
                    "\"savol: bu yerda nega 3 soniya?\"",
                    "<b>вопрос:</b> — вы не поняли, а не обвиняете. "
                    "«вопрос: почему здесь 3 секунды?»",
                    "<b>question:</b> — you did not understand; you are not accusing. "
                    "\"question: why 3 seconds here?\""),
                   ("<b>blocking:</b> — bu tuzatilmaguncha merge bo'lmaydi. "
                    "Faqat haqiqiy muammo uchun ishlatiladi.",
                    "<b>blocking:</b> — без исправления merge не будет. "
                    "Используется только для настоящей проблемы.",
                    "<b>blocking:</b> — no merge until this is fixed. "
                    "Use it only for a real problem."),
               ]),
))

S.append(slide(
    ph=("Qaror", "Решение", "The verdict"), time="31–34",
    eyebrow=("Uchta tugma", "Три кнопки", "Three buttons"),
    title=("Ko'rik oxirida reviewer uchta qarordan birini tanlaydi",
           "В конце ревью ревьюер выбирает одно из трёх решений",
           "At the end the reviewer picks one of three verdicts"),
    body='<div class="cols c3">\n' + "\n".join([
        box("green", ("✅ Approve", "✅ Approve", "✅ Approve"),
            p=("Kod tayyor, merge qilsa bo'ladi. <code>nit:</code> izohlar qolishi "
               "mumkin — ular merge ga to'sqinlik qilmaydi.",
               "Код готов, можно мержить. Комментарии <code>nit:</code> могут остаться — "
               "они не мешают merge.",
               "The code is ready to merge. <code>nit:</code> comments may remain — "
               "they do not block the merge.")),
        box("purple", ("💬 Comment", "💬 Comment", "💬 Comment"),
            p=("Savollarim bor, lekin qaror qabul qilmayapman. Odatda boshqa "
               "reviewer ham qarashi kerak bo'lganda ishlatiladi.",
               "Есть вопросы, но решение не принимаю. Обычно когда нужен взгляд "
               "ещё одного ревьюера.",
               "I have questions but am not deciding. Usually when another reviewer "
               "should also look.")),
        box("accent", ("🔁 Request changes", "🔁 Request changes", "🔁 Request changes"),
            p=("Merge dan oldin tuzatish shart. Kamida bitta <code>blocking:</code> "
               "izoh bo'lishi kerak — aks holda bu adolatsiz.",
               "До merge нужно исправить. Должен быть хотя бы один комментарий "
               "<code>blocking:</code> — иначе это несправедливо.",
               "Must be fixed before merge. At least one <code>blocking:</code> comment "
               "is required — otherwise it is unfair.")),
    ]) + "\n</div>\n"
         + box("", ("🛑 Oltin qoida", "🛑 Золотое правило", "🛑 The golden rule"),
               p=("<b>\"Request changes\" bosganingizda, nimani tuzatish kerakligi "
                  "aniq yozilgan bo'lishi shart.</b> Sababsiz rad etish — jamoadagi "
                  "ishonchni buzadigan eng tez yo'l. Va aksincha: o'qimasdan "
                  "\"Approve\" bosish — reviewer sifatida qilish mumkin bo'lgan "
                  "eng yomon ish.",
                  "<b>Нажимая «Request changes», вы обязаны чётко написать, что именно "
                  "исправить.</b> Отказ без причины — самый быстрый способ разрушить "
                  "доверие в команде. И наоборот: нажать «Approve», не читая, — "
                  "худшее, что может сделать ревьюер.",
                  "<b>When you press \"Request changes\" you must state exactly what to "
                  "fix.</b> Rejecting without a reason is the fastest way to destroy "
                  "trust in a team. And the reverse: pressing \"Approve\" without "
                  "reading is the worst thing a reviewer can do.")),
))

S.append(slide(
    ph=("AI reviewer", "AI-ревьюер", "AI reviewer"), time="34–38",
    eyebrow=("AI nimani topadi va nimani topmaydi",
             "Что AI находит и что не находит",
             "What AI catches and what it misses"),
    title=("AI reviewer — birinchi filtr, oxirgi so'z emas",
           "AI-ревьюер — первый фильтр, но не последнее слово",
           "An AI reviewer is a first filter, not the final word"),
    body='<div class="cols c2">\n'
         + box("green", ("✅ AI yaxshi topadi", "✅ AI находит хорошо", "✅ AI catches well"),
               items=[
                   ("Nolga bo'lish, <code>null</code> tekshiruvining yo'qligi, "
                    "massiv chegarasidan chiqish.",
                    "Деление на ноль, отсутствие проверки на <code>null</code>, "
                    "выход за границы массива.",
                    "Division by zero, missing <code>null</code> checks, "
                    "array out-of-bounds."),
                   ("Kodda qolib ketgan parol va API kalitlari.",
                    "Забытые в коде пароли и API-ключи.",
                    "Passwords and API keys left in the code."),
                   ("Takrorlanuvchi kod, ishlatilmaydigan o'zgaruvchilar.",
                    "Дублирующийся код, неиспользуемые переменные.",
                    "Duplicated code, unused variables."),
                   ("Nomlash va formatlash — soniyalarda, charchamasdan.",
                    "Именование и форматирование — за секунды, не уставая.",
                    "Naming and formatting — in seconds, without fatigue."),
               ])
         + "\n"
         + box("accent", ("❌ AI ko'rmaydi", "❌ AI не видит", "❌ AI cannot see"),
               items=[
                   ("<b>Biznes mantiqi.</b> Kod ishlaydi, lekin <b>noto'g'ri narsani</b> "
                    "hisoblaydi — AI buni bilmaydi, chunki talabni ko'rmagan.",
                    "<b>Бизнес-логику.</b> Код работает, но считает <b>не то</b> — "
                    "AI этого не знает, он не видел требований.",
                    "<b>Business logic.</b> The code runs but computes <b>the wrong "
                    "thing</b> — AI cannot know, it never saw the requirements."),
                   ("<b>Loyihaning kontekstini.</b> \"Bizda bu allaqachon "
                    "<code>utils.js</code> da bor\" — buni faqat jamoa biladi.",
                    "<b>Контекст проекта.</b> «У нас это уже есть в <code>utils.js</code>» "
                    "— знает только команда.",
                    "<b>Project context.</b> \"We already have this in "
                    "<code>utils.js</code>\" — only the team knows that."),
                   ("<b>Kelajakni.</b> \"Bu yechim 10 000 foydalanuvchida buziladi\" — "
                    "bu tajriba, matn tahlili emas.",
                    "<b>Будущее.</b> «Это решение сломается на 10 000 пользователей» — "
                    "это опыт, а не анализ текста.",
                    "<b>The future.</b> \"This breaks at 10,000 users\" — that is "
                    "experience, not text analysis."),
                   ("AI ba'zan <b>ishonch bilan noto'g'ri</b> gapiradi. Uning izohini "
                    "ham tekshirish kerak.",
                    "AI иногда <b>уверенно ошибается</b>. Его комментарий тоже нужно "
                    "проверять.",
                    "AI is sometimes <b>confidently wrong</b>. Its comments need "
                    "checking too."),
               ])
         + "\n</div>",
))

S.append(slide(
    ph=("Amaliyot", "Практика", "Practice"), time="38–50",
    eyebrow=("Laboratoriya · 12 daqiqa", "Лаборатория · 12 минут", "Lab · 12 minutes"),
    title=("Siz — reviewer: lab/index.html ni oching",
           "Вы — ревьюер: откройте lab/index.html",
           "You are the reviewer: open lab/index.html"),
    body='<div class="cols c4">\n' + "\n".join([
        box("purple", ("1 · O'qish (3 daq)", "1 · Чтение (3 мин)", "1 · Read (3 min)"),
            p=("PR tavsifi va diffni o'qing. Hali hech narsa yozmang — avval "
               "butun o'zgarishni tushunib oling.",
               "Прочитайте описание PR и diff. Пока ничего не пишите — сначала "
               "поймите изменение целиком.",
               "Read the PR description and the diff. Write nothing yet — "
               "first understand the whole change.")),
        box("accent", ("2 · Xato topish (5 daq)", "2 · Найти баги (5 мин)", "2 · Find bugs (5 min)"),
            p=("Diffda <b>4 ta haqiqiy xato</b> yashiringan. Qatorni bosib izoh "
               "qoldiring va <code>blocking</code> / <code>savol</code> / "
               "<code>nit</code> deb belgilang.",
               "В diff спрятаны <b>4 настоящие ошибки</b>. Кликните по строке, оставьте "
               "комментарий и пометьте его <code>blocking</code> / <code>вопрос</code> / "
               "<code>nit</code>.",
               "<b>4 real bugs</b> are hidden in the diff. Click a line, leave a comment "
               "and label it <code>blocking</code> / <code>question</code> / "
               "<code>nit</code>.")),
        box("green", ("3 · Qaror (2 daq)", "3 · Решение (2 мин)", "3 · Verdict (2 min)"),
            p=("Uchta tugmadan birini bosing. Stend qaroringiz izohlaringizga "
               "<b>mos kelishini</b> tekshiradi.",
               "Нажмите одну из трёх кнопок. Стенд проверит, <b>соответствует</b> ли "
               "решение вашим комментариям.",
               "Press one of the three buttons. The lab checks whether your verdict "
               "<b>matches</b> your comments.")),
        box("", ("4 · AI bilan (2 daq)", "4 · Сравнить с AI (2 мин)", "4 · Compare (2 min)"),
            p=("<b>🤖 AI ko'rigi</b> ni bosing va natijalarni solishtiring: AI nimani "
               "topdi, siz nimani topdingiz, <b>kim nimani o'tkazib yubordi</b>.",
               "Нажмите <b>🤖 Ревью AI</b> и сравните: что нашёл AI, что нашли вы, "
               "<b>кто что пропустил</b>.",
               "Press <b>🤖 AI review</b> and compare: what AI found, what you found, "
               "<b>who missed what</b>.")),
    ]) + "\n</div>\n"
         + box("accent", ("🎯 Asosiy topshiriq", "🎯 Главное задание", "🎯 The key task"),
               p=("Diffdagi <b>to'rtta xatodan bittasini AI umuman topa olmaydi</b> — "
                  "chunki u biznes mantiqiga tegishli. Uni toping va varaqaga yozing. "
                  "Aynan shu — sizning insonni AI dan ustun qiladigan qobiliyatingiz.",
                  "<b>Одну из четырёх ошибок AI не найдёт вообще</b> — она относится "
                  "к бизнес-логике. Найдите её и запишите в лист. Именно это — та "
                  "способность, которая делает человека сильнее AI.",
                  "<b>One of the four bugs is invisible to the AI</b> — it belongs to "
                  "business logic. Find it and write it on your worksheet. That is "
                  "precisely the ability that makes a human stronger than an AI.")),
))

S.append(slide(
    ph=("Jarayon", "Процесс", "Pipeline"), time="50–52",
    eyebrow=("PR dan keyin nima bo'ladi", "Что происходит после PR", "What happens after a PR"),
    title=("Merge — bu oxiri emas, bu konveyerning boshlanishi",
           "Merge — это не конец, а начало конвейера",
           "The merge is not the end — it starts the pipeline"),
    body='<div class="cols c2">\n'
         + box("green", ("Avtomatik tekshiruvlar (CI)", "Автоматические проверки (CI)",
                         "Automated checks (CI)"),
               items=[
                   ("PR ochilishi bilan server kodni <b>o'zi yuklab oladi</b> va "
                    "testlarni ishga tushiradi.",
                    "Как только PR открыт, сервер <b>сам скачивает</b> код и запускает "
                    "тесты.",
                    "As soon as the PR opens, a server <b>pulls the code itself</b> "
                    "and runs the tests."),
                   ("Test qulasa — PR da <b>qizil belgi</b> chiqadi va merge tugmasi "
                    "bloklanadi.",
                    "Тест упал — в PR появляется <b>красная отметка</b>, кнопка merge "
                    "блокируется.",
                    "A failing test puts a <b>red mark</b> on the PR and blocks the "
                    "merge button."),
                   ("Shuning uchun \"mende ishlayapti\" degan gap <b>dalil emas</b>.",
                    "Поэтому фраза «у меня работает» — <b>не доказательство</b>.",
                    "That is why \"it works on my machine\" is <b>not evidence</b>."),
               ])
         + "\n"
         + box("purple", ("Merge dan keyin", "После merge", "After the merge"),
               items=[
                   ("Kod <code>main</code> ga tushadi va odatda <b>avtomatik deploy</b> "
                    "bo'ladi (6-darsdagi Vercel).",
                    "Код попадает в <code>main</code> и обычно <b>деплоится "
                    "автоматически</b> (Vercel из урока 6).",
                    "The code lands in <code>main</code> and usually <b>deploys "
                    "automatically</b> (Vercel from lesson 6)."),
                   ("Branch o'chiriladi — u endi kerak emas, tarix commitlarda qoldi.",
                    "Ветка удаляется — она больше не нужна, история осталась в коммитах.",
                    "The branch is deleted — it is no longer needed, the history lives "
                    "in the commits."),
                   ("Muammo chiqsa — <code>git revert</code> bilan <b>bitta commit</b> "
                    "orqaga qaytariladi.",
                    "Если возникла проблема — <code>git revert</code> откатывает "
                    "<b>один коммит</b>.",
                    "If something breaks, <code>git revert</code> rolls back "
                    "<b>one commit</b>."),
               ])
         + "\n</div>",
))

S.append(slide(
    ph=("Yakun", "Итоги", "Summary"), time="52–53",
    eyebrow=("Uy vazifasi va baholash", "Домашнее задание и оценка", "Homework and grading"),
    title=("Uy vazifasi: ko'rik hisoboti va PR tavsifi (10 ball)",
           "Домашнее задание: отчёт о ревью и описание PR (10 баллов)",
           "Homework: review report and PR description (10 points)"),
    body='<div class="cols c2">\n'
         + box("green", ("Nima qilish kerak", "Что нужно сделать", "What to do"),
               items=[
                   ("Varaqadagi <b>4 ta xato jadvalini</b> to'ldiring: qator, muammo, "
                    "belgi (blocking / savol / nit).",
                    "Заполните <b>таблицу 4 ошибок</b>: строка, проблема, метка "
                    "(blocking / вопрос / nit).",
                    "Fill the <b>4-bug table</b>: line, problem, label "
                    "(blocking / question / nit)."),
                   ("<b>AI topa olmagan xatoni</b> alohida yozing va nega AI uni "
                    "ko'ra olmasligini tushuntiring.",
                    "Отдельно запишите <b>ошибку, которую не нашёл AI</b>, и объясните, "
                    "почему он её не видит.",
                    "Separately note the <b>bug the AI missed</b> and explain why "
                    "it cannot see it."),
                   ("Bitta izohni <b>to'liq shaklda</b> yozing: muammo + sabab + taklif.",
                    "Напишите один комментарий <b>в полной форме</b>: "
                    "проблема + причина + предложение.",
                    "Write one comment <b>in full form</b>: "
                    "problem + reason + suggestion."),
                   ("O'z loyihangiz uchun <b>PR tavsifi</b> yozing: sarlavha, nima, "
                    "nega, qanday sinaldi.",
                    "Напишите <b>описание PR</b> для своего проекта: заголовок, что, "
                    "почему, как проверено.",
                    "Write a <b>PR description</b> for your own project: title, what, "
                    "why, how it was tested."),
               ])
         + "\n"
         + box("accent", ("Baholash mezoni", "Критерии оценки", "Grading rubric"),
               extra_html='<ul class="plain">\n'
               + '  <li><span class="t" %s>4 ta xato jadvali — <b>4 ball</b></span></li>\n'
               % i18n("4 ta xato jadvali — <b>4 ball</b>",
                      "Таблица 4 ошибок — <b>4 балла</b>",
                      "Table of 4 bugs — <b>4 points</b>")
               + '  <li><span class="t" %s>AI topa olmagan xato va sababi — <b>2 ball</b></span></li>\n'
               % i18n("AI topa olmagan xato va sababi — <b>2 ball</b>",
                      "Ошибка, не найденная AI, и причина — <b>2 балла</b>",
                      "The bug AI missed and why — <b>2 points</b>")
               + '  <li><span class="t" %s>To\'liq izoh (muammo+sabab+taklif) — <b>2 ball</b></span></li>\n'
               % i18n("To'liq izoh (muammo+sabab+taklif) — <b>2 ball</b>",
                      "Полный комментарий (проблема+причина+предложение) — <b>2 балла</b>",
                      "A full comment (problem+reason+suggestion) — <b>2 points</b>")
               + '  <li><span class="t" %s>PR tavsifi — <b>2 ball</b></span></li>\n'
               % i18n("PR tavsifi — <b>2 ball</b>",
                      "Описание PR — <b>2 балла</b>",
                      "PR description — <b>2 points</b>")
               + "</ul>")
         + "\n</div>",
))


NOTES = {
    "uz": [
        ["Titul slayd",
         "Birinchi soatda branch yaratdik va konfliktni yechdik. Endi eng muhim savol: kod main ga qanday tushadi? Javob — hech kim to'g'ridan-to'g'ri qo'shmaydi. Avval Pull Request va kod ko'rigi.",
         "lab/index.html ni proyektorda oldindan oching."],
        ["Xatoning narxi",
         "To'rtta ustunni ketma-ket ko'rsating: 1 daqiqa, 10 daqiqa, 1 kun, 1 hafta. Bu jadval kod ko'rigi nega kerakligini boshqa hech qanday tushuntirishdan yaxshiroq aytadi.",
         "To'rt ustunni birma-bir ochish. Narxlarni ovoz chiqarib aytish."],
        ["PR jarayoni",
         "To'qqiz qadamni ko'rsating. Ta'kidlang: 5 va 6-qadam (ko'rik va tuzatish) bir necha marta takrorlanishi mumkin — bu normal, bu muvaffaqiyatsizlik emas.",
         "Kod blokidagi 9 qadamni ko'rsatish."],
        ["Diff o'qish",
         "Minus qizil, plyus yashil, kulrang kontekst. @@ qatorini ham tushuntiring — o'quvchilar undan qo'rqadi. Oxirida tuzoqni ayting: diff faqat o'zgarishni ko'rsatadi, xato esa bog'liqlikda bo'lishi mumkin.",
         "Doskada + va - belgilarini yozib ko'rsatish."],
        ["Yaxshi PR",
         "Asosiy raqam: 50-200 qator. Va oltin qoida: sarlavhada 'va' so'zi bo'lsa — PR ni ikkiga bo'lish kerak. Bu juda amaliy maslahat.",
         "Doskaga '50-200 qator' yozib qo'yish."],
        ["To'rt daraja",
         "Tartib muhim: to'g'rimi -> xavfsizmi -> o'qiladimi -> kerakmi. Ayting: agar bo'sh joydan boshlasangiz, mantiqiy xatoni o'tkazib yuborasiz. Formatlashni Prettier qilsin.",
         "To'rt darajani tartib bilan ko'rsatish."],
        ["Izoh yozish",
         "Eng nozik qism. Ikki ustunni solishtiring. Asosiy gap: izoh kodga yoziladi, odamga emas. Keyin nit/savol/blocking belgilarini tushuntiring — bu stendda ishlatiladi.",
         "Doskada nit: / savol: / blocking: yozib qo'yish."],
        ["Uchta qaror",
         "Approve, Comment, Request changes. Oltin qoidani ikki tomonlama ayting: sababsiz rad etish ham, o'qimasdan tasdiqlash ham yomon. Ikkalasi ham ishonchni buzadi.",
         "Uch tugmani ko'rsatish."],
        ["AI reviewer",
         "Ikki ustun: AI nimani topadi va nimani ko'rmaydi. Eng muhim gap: AI biznes mantiqini bilmaydi, chunki u talabni ko'rmagan. Bu amaliyotga tayyorgarlik — stendda aynan shunday xato bor.",
         "Ikki ustunni solishtirish. Amaliyotga qiziqtirish."],
        ["Amaliyot 12 daqiqa",
         "To'rt bosqich. Muhim: birinchi 3 daqiqada hech narsa yozmasin — avval o'qisin. Bu professional odat. Keyin 4 ta xatoni topish. AI topa olmaydigan xato — asosiy topshiriq.",
         "Vaqtni nazorat qilish. Sinf bo'ylab yurish."],
        ["CI va deploy",
         "PR ochilishi bilan testlar avtomatik ishlaydi. Asosiy gap: 'mende ishlayapti' dalil emas. Bu 6-darsdagi Vercel deploy bilan bog'lanadi.",
         "Qisqa, 2 daqiqa."],
        ["Yakun va baholash",
         "Xulosa: kod ko'rigi xato uchun emas, bilim va standart uchun ham. Varaqalarni yig'ing va AI topa olmagan xato yozilganini tekshiring — bu asosiy topshiriq edi.",
         "Varaqalarni yig'ish, 2-savolga e'tibor berish."],
    ],
    "ru": [
        ["Титульный слайд",
         "На первом часе мы создали ветку и разрешили конфликт. Теперь главный вопрос: как код попадает в main? Ответ — никто не вливает напрямую. Сначала Pull Request и код-ревью.",
         "Заранее откройте lab/index.html на проекторе."],
        ["Цена ошибки",
         "Покажите четыре колонки по порядку: 1 минута, 10 минут, 1 день, 1 неделя. Эта таблица объясняет необходимость код-ревью лучше любых слов.",
         "Открывать колонки по одной. Проговаривать цену вслух."],
        ["Процесс PR",
         "Покажите девять шагов. Подчеркните: шаги 5 и 6 (ревью и правки) могут повториться несколько раз — это нормально, это не провал.",
         "Показать 9 шагов из блока кода."],
        ["Чтение diff",
         "Минус красный, плюс зелёный, серое — контекст. Объясните и строку @@ — учеников она пугает. В конце назовите ловушку: diff показывает только изменение, а ошибка может быть во взаимодействии.",
         "Написать на доске знаки + и -."],
        ["Хороший PR",
         "Главное число: 50-200 строк. И золотое правило: если в заголовке есть «и» — PR надо разделить. Очень практичный совет.",
         "Написать на доске «50-200 строк»."],
        ["Четыре уровня",
         "Порядок важен: правильно -> безопасно -> читаемо -> нужно ли. Скажите: если начать с пробелов, пропустите логическую ошибку. Форматирование пусть делает Prettier.",
         "Показать четыре уровня по порядку."],
        ["Как писать комментарии",
         "Самая тонкая часть. Сравните две колонки. Главное: комментарий пишется к коду, а не к человеку. Затем объясните метки nit/вопрос/blocking — они используются на стенде.",
         "Написать на доске nit: / вопрос: / blocking:"],
        ["Три решения",
         "Approve, Comment, Request changes. Золотое правило с обеих сторон: и отказ без причины, и одобрение без чтения — плохо. И то и другое разрушает доверие.",
         "Показать три кнопки."],
        ["AI-ревьюер",
         "Две колонки: что AI находит и чего не видит. Главное: AI не знает бизнес-логику, он не видел требований. Это подготовка к практике — на стенде есть ровно такая ошибка.",
         "Сравнить две колонки. Заинтриговать практикой."],
        ["Практика 12 минут",
         "Четыре этапа. Важно: первые 3 минуты ничего не писать — сначала прочитать. Это профессиональная привычка. Затем найти 4 ошибки. Ошибка, невидимая для AI, — главное задание.",
         "Следить за временем. Ходить по классу."],
        ["CI и деплой",
         "Как только PR открыт, тесты запускаются автоматически. Главная мысль: «у меня работает» — не доказательство. Связать с деплоем на Vercel из урока 6.",
         "Коротко, 2 минуты."],
        ["Итоги и оценивание",
         "Вывод: код-ревью нужно не только для ошибок, но и для знаний и стандарта. Соберите листы и проверьте, записана ли ошибка, не найденная AI — это было главное задание.",
         "Собрать листы, обратить внимание на второй вопрос."],
    ],
    "en": [
        ["Title slide",
         "In hour one we created a branch and resolved a conflict. Now the key question: how does code get into main? Nobody pushes directly. First a Pull Request and a code review.",
         "Pre-open lab/index.html on the projector."],
        ["The cost of a bug",
         "Show the four columns in order: 1 minute, 10 minutes, 1 day, 1 week. This table justifies code review better than any speech.",
         "Reveal the columns one by one. Say the costs aloud."],
        ["The PR process",
         "Show the nine steps. Stress that steps 5 and 6 (review and fixes) may repeat several times — that is normal, not a failure.",
         "Walk through the 9 steps in the code block."],
        ["Reading a diff",
         "Minus red, plus green, grey is context. Explain the @@ line too — it intimidates students. End with the trap: a diff shows only the change, but bugs hide in the interaction.",
         "Write the + and - markers on the board."],
        ["A good PR",
         "The key number: 50-200 lines. And the golden rule: if the title contains 'and', split the PR. Very practical advice.",
         "Write '50-200 lines' on the board."],
        ["The four levels",
         "Order matters: correct -> safe -> readable -> needed. Say: start with whitespace and you will miss the logic bug. Let Prettier handle formatting.",
         "Show the four levels in order."],
        ["Writing comments",
         "The most delicate part. Compare the two columns. Core point: a comment is about the code, not the person. Then explain the nit/question/blocking labels — they are used on the lab.",
         "Write nit: / question: / blocking: on the board."],
        ["The three verdicts",
         "Approve, Comment, Request changes. State the golden rule both ways: rejecting without a reason and approving without reading are both bad. Both destroy trust.",
         "Show the three buttons."],
        ["AI reviewer",
         "Two columns: what AI finds and what it cannot see. Key point: AI does not know the business logic, it never saw the requirements. This sets up the practice — the lab has exactly such a bug.",
         "Compare the two columns. Tease the practice."],
        ["Practice, 12 minutes",
         "Four stages. Important: write nothing for the first 3 minutes — read first. A professional habit. Then find the 4 bugs. The AI-invisible bug is the key task.",
         "Watch the clock. Walk the room."],
        ["CI and deploy",
         "Tests run automatically as soon as the PR opens. Key idea: 'it works on my machine' is not evidence. Link back to the Vercel deploy from lesson 6.",
         "Keep it short, 2 minutes."],
        ["Summary and grading",
         "Conclusion: code review is not only about bugs but about knowledge and standards. Collect the sheets and check the AI-missed bug is recorded — that was the key task.",
         "Collect sheets, focus on question two."],
    ],
}

VARAQA = (
    sheet_header(
        ("14-dars: Pull Request va Kod Ko'rigi",
         "Урок 14: Pull Request и Код-ревью",
         "Lesson 14: Pull Requests and Code Review"),
        ("Target International School · 9-sinf · 3-hafta (2-soat)",
         "Target International School · 9 класс · 3-я неделя (2-й час)",
         "Target International School · Grade 9 · Week 3 (Hour 2)"))
    + mission(
        ("🎯 Missiya: siz reviewersiz",
         "🎯 Миссия: вы — ревьюер",
         "🎯 Mission: you are the reviewer"),
        ("<b>lab/index.html</b> ni oching. Diffda <b>4 ta haqiqiy xato</b> bor. "
         "Avval 3 daqiqa <b>faqat o'qing</b>, keyin izoh yozing. Eng muhim topshiriq: "
         "AI reviewer <b>topa olmaydigan</b> xatoni aniqlash — u biznes mantiqiga tegishli.",
         "Откройте <b>lab/index.html</b>. В diff спрятаны <b>4 настоящие ошибки</b>. "
         "Сначала 3 минуты <b>только читайте</b>, потом пишите комментарии. Главное "
         "задание: найти ошибку, которую <b>не видит</b> AI-ревьюер — она в бизнес-логике.",
         "Open <b>lab/index.html</b>. The diff hides <b>4 real bugs</b>. "
         "Spend the first 3 minutes <b>reading only</b>, then comment. The key task: "
         "find the bug the AI reviewer <b>cannot see</b> — it lives in the business logic."))
    + table(
        [("#", "#", "#"),
         ("Qator", "Строка", "Line"),
         ("Muammo nima", "В чём проблема", "What is wrong"),
         ("Belgi", "Метка", "Label")],
        [[("1", "1", "1"), None, None, None],
         [("2", "2", "2"), None, None, None],
         [("3", "3", "3"), None, None, None],
         [("4", "4", "4"), None, None, None]])
    + '    <div style="margin-bottom:7px">\n'
    + '      ' + el("p", "Belgi: <b>blocking</b> (merge to'xtaydi) · <b>savol</b> (tushunmadim) · <b>nit</b> (mayda, ixtiyoriy)",
                    "Метка: <b>blocking</b> (merge остановлен) · <b>вопрос</b> (не понял) · <b>nit</b> (мелочь, необязательно)",
                    "Label: <b>blocking</b> (blocks the merge) · <b>question</b> (did not understand) · <b>nit</b> (minor, optional)",
                    extra='style="font-size:7.4pt; color:var(--ink-3); margin:0"') + "\n"
    + "    </div>\n"
    + '    <div class="rubric-grid">\n'
    + sheet_box(
        ("✏️ AI topa olmagan xato va to'liq izoh",
         "✏️ Ошибка, не найденная AI, и полный комментарий",
         "✏️ The bug AI missed, and a full comment"),
        writelines(2, ("🤖 AI topa olmagan xato — va NEGA u buni ko'ra olmaydi:",
                       "🤖 Ошибка, которую не нашёл AI — и ПОЧЕМУ он её не видит:",
                       "🤖 The bug AI missed — and WHY it cannot see it:"))
        + "\n"
        + writelines(3, ("💬 Bitta to'liq izoh (muammo + sabab + taklif):",
                         "💬 Один полный комментарий (проблема + причина + предложение):",
                         "💬 One full comment (problem + reason + suggestion):"))
        + "\n"
        + writelines(2, ("📝 O'z loyihangiz uchun PR tavsifi (sarlavha, nima, nega, sinov):",
                         "📝 Описание PR для своего проекта (заголовок, что, почему, проверка):",
                         "📝 A PR description for your project (title, what, why, testing):")))
    + "\n"
    + sheet_box(
        ("📊 Baholash mezoni (10 ball)",
         "📊 Критерии оценки (10 баллов)",
         "📊 Grading rubric (10 points)"),
        rubric([
            (("4 ta xato jadvali (belgilar bilan)", "Таблица 4 ошибок (с метками)",
              "Table of 4 bugs (with labels)"), "4"),
            (("AI topa olmagan xato va sababi", "Ошибка без AI и причина",
              "The AI-missed bug and why"), "2"),
            (("To'liq izoh", "Полный комментарий", "A full comment"), "2"),
            (("PR tavsifi", "Описание PR", "PR description"), "2"),
        ], "10"))
    + "\n    </div>\n  </div>\n"
    + sign_box()
)

if __name__ == "__main__":
    print(Lesson(D, TITLES, SHEET_TITLES, "vc-notes-9-14", S, NOTES, VARAQA).build())
