# -*- coding: utf-8 -*-
"""9-sinf · 3-hafta · 13-dars — Git va GitHub: Commit, Branch va Merge Konflikti."""

import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from build import (Lesson, slide, title_slide, box, code, el, i18n,
                   sheet_header, mission, table, sheet_box, rubric, writelines, sign_box)

D = "classes/9-sinf/3-hafta/13-dars-git-va-github"

TITLES = {
    "uz": "13-dars: Git va GitHub — Commit, Branch va Merge Konflikti",
    "ru": "Урок 13: Git и GitHub — Commit, Branch и Merge-конфликт",
    "en": "Lesson 13: Git and GitHub — Commit, Branch and Merge Conflict",
}
SHEET_TITLES = {k: v + (" — Ish Varaqasi" if k == "uz" else
                        " — Рабочий Лист" if k == "ru" else " — Worksheet")
                for k, v in TITLES.items()}

S = []

S.append(title_slide(
    ph=("Kirish", "Введение", "Intro"), time="0–3",
    eyebrow=("Vibecoding · 13-dars · 9-sinf (Junior Vibecoder)",
             "Vibecoding · Урок 13 · 9 класс (Junior Vibecoder)",
             "Vibecoding · Lesson 13 · Grade 9 (Junior Vibecoder)"),
    h1=("Git va GitHub: Kod Tarixini Boshqarish",
        "Git и GitHub: Управление Историей Кода",
        "Git and GitHub: Managing the History of Your Code"),
    lede=("11-darsda siz VS Code o'rnatdingiz, 12-darsda xatolarni topishni o'rgandingiz. "
          "Lekin hali bitta jiddiy muammo qoldi: <b>kod o'zgaradi, va eski versiya "
          "yo'qoladi</b>. Bugun siz professional dasturchilar 20 yildan beri "
          "ishlatadigan vositani o'rganasiz — <b>Git</b>. Bu shunchaki \"saqlash\" emas: "
          "bu parallel ish, orqaga qaytish va jamoaviy dasturlash imkoniyati.",
          "На уроке 11 вы установили VS Code, на уроке 12 научились находить ошибки. "
          "Но осталась одна серьёзная проблема: <b>код меняется, и старая версия "
          "исчезает</b>. Сегодня вы освоите инструмент, которым профессиональные "
          "разработчики пользуются уже 20 лет — <b>Git</b>. Это не просто «сохранение»: "
          "это параллельная работа, откат назад и командная разработка.",
          "In lesson 11 you installed VS Code, in lesson 12 you learned to hunt bugs. "
          "But one serious problem remains: <b>code changes, and the old version "
          "disappears</b>. Today you learn the tool professional developers have used "
          "for 20 years — <b>Git</b>. It is not just \"saving\": it is parallel work, "
          "going back in time and team development."),
    meta=[("<b>Fan:</b> Vibecoding · Muhandislik jarayoni",
           "<b>Предмет:</b> Vibecoding · Инженерный процесс",
           "<b>Subject:</b> Vibecoding · Engineering Process"),
          ("<b>Kohorta:</b> 9-sinf Junior Vibecoder",
           "<b>Когорта:</b> 9 класс Junior Vibecoder",
           "<b>Cohort:</b> Grade 9 Junior Vibecoder"),
          ("<b>Hafta:</b> 3 (1-soat)", "<b>Неделя:</b> 3 (1-й час)", "<b>Week:</b> 3 (Hour 1)")],
))

S.append(slide(
    ph=("Muammo", "Проблема", "Problem"), time="3–6",
    eyebrow=("Tanish holat", "Знакомая ситуация", "A familiar situation"),
    title=("loyiha_final_v2_FINAL_oxirgi(1).html",
           "проект_финал_v2_ФИНАЛ_последний(1).html",
           "project_final_v2_FINAL_last(1).html"),
    body='<div class="cols c2">\n'
         + box("accent", ("Nima uchun bu ishlamaydi", "Почему это не работает",
                          "Why this does not work"),
               items=[
                   ("<b>Qaysi biri oxirgisi?</b> Fayl sanasi yolg'on gapiradi — siz uni "
                    "tasodifan ochib, saqlab yuborgansiz.",
                    "<b>Какой из них последний?</b> Дата файла врёт — вы случайно открыли "
                    "и сохранили его.",
                    "<b>Which one is latest?</b> The file date lies — you opened and "
                    "saved it by accident."),
                   ("<b>Nima o'zgardi?</b> Ikki fayl orasidagi farqni topish uchun "
                    "ularni yonma-yon o'qib chiqish kerak.",
                    "<b>Что изменилось?</b> Чтобы найти разницу между двумя файлами, "
                    "нужно читать их построчно рядом.",
                    "<b>What changed?</b> To find the difference you must read both "
                    "files side by side."),
                   ("<b>Nega o'zgardi?</b> Bu ma'lumot hech qayerda saqlanmagan.",
                    "<b>Почему изменилось?</b> Эта информация нигде не сохранена.",
                    "<b>Why did it change?</b> That information is stored nowhere."),
                   ("<b>Ikki kishi birga ishlasa?</b> Fayllarni qo'lda birlashtirish — "
                    "va kimningdir ishi yo'qoladi.",
                    "<b>А если работают двое?</b> Файлы сливают вручную — и чья-то работа "
                    "теряется.",
                    "<b>And if two people work on it?</b> Files get merged by hand — "
                    "and somebody's work is lost."),
               ])
         + "\n"
         + box("green", ("Git nima beradi", "Что даёт Git", "What Git gives you"),
               items=[
                   ("<b>Bitta fayl</b> — va uning butun tarixi yonida saqlanadi.",
                    "<b>Один файл</b> — и вся его история хранится рядом.",
                    "<b>One file</b> — with its entire history kept beside it."),
                   ("Har bir o'zgarish uchun <b>kim, qachon, nima va nega</b> yozilgan.",
                    "Для каждого изменения записано <b>кто, когда, что и почему</b>.",
                    "Every change records <b>who, when, what and why</b>."),
                   ("Istalgan eski holatga <b>bir buyruq bilan</b> qaytish mumkin.",
                    "К любому старому состоянию можно вернуться <b>одной командой</b>.",
                    "You can return to any old state with <b>one command</b>."),
                   ("Ikki kishi <b>bir vaqtda</b> ishlaydi, Git ishni o'zi birlashtiradi.",
                    "Двое работают <b>одновременно</b>, Git сам объединяет работу.",
                    "Two people work <b>at the same time</b>, and Git merges the work."),
               ])
         + "\n</div>",
))

S.append(slide(
    ph=("Model", "Модель", "Model"), time="6–10",
    eyebrow=("Git aslida nima", "Что такое Git на самом деле", "What Git actually is"),
    title=("Git — bu \"farqlar\" emas, bu <b>suratlar zanjiri</b>",
           "Git — это не «разница», а <b>цепочка снимков</b>",
           "Git is not \"differences\" — it is a <b>chain of snapshots</b>"),
    body='<div class="cols c2">\n'
         + box("purple", ("Keng tarqalgan noto'g'ri tasavvur",
                          "Распространённое заблуждение", "A common misconception"),
               p=("Ko'pchilik Git faqat <b>o'zgargan qatorlarni</b> saqlaydi deb o'ylaydi. "
                  "Aslida har bir commit — loyihaning <b>to'liq surati</b> (snapshot). "
                  "O'zgarmagan fayllar uchun Git yangi nusxa yaratmaydi, balki "
                  "oldingi nusxaga <b>ishora</b> qoldiradi — shuning uchun tarix "
                  "joy egallamaydi.",
                  "Многие думают, что Git хранит только <b>изменённые строки</b>. "
                  "На самом деле каждый коммит — это <b>полный снимок</b> проекта. "
                  "Для неизменённых файлов Git не создаёт копию, а оставляет "
                  "<b>ссылку</b> на предыдущую — поэтому история не занимает много места.",
                  "Many people think Git stores only the <b>changed lines</b>. "
                  "In fact each commit is a <b>full snapshot</b> of the project. "
                  "For unchanged files Git stores a <b>pointer</b> to the previous copy "
                  "instead of duplicating it — which is why history stays small."))
         + "\n"
         + box("green", ("Har commitda nima saqlanadi", "Что хранится в каждом коммите",
                         "What each commit stores"),
               extra_html=code(
                   "commit a3f9c21\n"
                   "├─ muallif:  Aziz <aziz@mail.uz>\n"
                   "├─ sana:     2026-09-21 14:32\n"
                   "├─ xabar:    \"Navbar mobil ekranda tuzatildi\"\n"
                   "├─ ota:      7b2e440   <- oldingi commit\n"
                   "└─ surat:    index.html, style.css, app.js\n\n"
                   "// a3f9c21 — commit ning noyob identifikatori (hash)"))
         + "\n</div>\n"
         + box("accent", ("Ota-bola zanjiri eng muhim g'oya",
                          "Цепочка родитель-потомок — главная идея",
                          "The parent chain is the key idea"),
               p=("Har commit o'zidan <b>oldingisini</b> eslab turadi. Shu zanjir orqali "
                  "Git butun tarixni tiklay oladi. Branch va merge ham aynan shu "
                  "zanjir ustida qurilgan — buni tushunsangiz, qolgan hammasi oson.",
                  "Каждый коммит помнит <b>предыдущий</b>. По этой цепочке Git "
                  "восстанавливает всю историю. Ветки и слияния построены ровно на этой "
                  "цепочке — поймёте её, и остальное станет простым.",
                  "Every commit remembers its <b>predecessor</b>. Git rebuilds the whole "
                  "history from that chain. Branches and merges are built on exactly this "
                  "chain — understand it and the rest becomes easy.")),
))

S.append(slide(
    ph=("Uchta zona", "Три зоны", "Three zones"), time="10–15",
    eyebrow=("add va commit nima qiladi", "Что делают add и commit",
             "What add and commit do"),
    title=("Fayl commitgacha uchta zonadan o'tadi",
           "До коммита файл проходит три зоны",
           "A file passes through three zones before a commit"),
    body='<div class="cols c3">\n' + "\n".join([
        box("", ("1 · Working Directory", "1 · Working Directory", "1 · Working Directory"),
            p=("Sizning papkangiz. Siz shu yerda tahrirlaysiz. Git o'zgarishni "
               "<b>ko'radi</b>, lekin hali eslab qolmaydi.",
               "Ваша папка. Здесь вы редактируете. Git <b>видит</b> изменение, "
               "но пока не запоминает.",
               "Your folder. You edit here. Git <b>sees</b> the change "
               "but does not remember it yet.")),
        box("purple", ("2 · Staging Area", "2 · Staging Area", "2 · Staging Area"),
            p=("<code>git add</code> dan keyingi holat. Bu <b>tayyorlangan</b> "
               "o'zgarishlar ro'yxati — commitga nima kirishini siz tanlaysiz.",
               "Состояние после <code>git add</code>. Это список <b>подготовленных</b> "
               "изменений — вы сами выбираете, что войдёт в коммит.",
               "The state after <code>git add</code>. A list of <b>staged</b> changes — "
               "you choose what goes into the commit.")),
        box("green", ("3 · Repository", "3 · Repository", "3 · Repository"),
            p=("<code>git commit</code> dan keyin. O'zgarish <b>tarixga yozildi</b> "
               "va endi yo'qolmaydi.",
               "После <code>git commit</code>. Изменение <b>записано в историю</b> "
               "и больше не потеряется.",
               "After <code>git commit</code>. The change is <b>written to history</b> "
               "and can no longer be lost.")),
    ]) + "\n</div>\n"
         + box("accent", ("Nega staging kerak? Bu ortiqcha qadamdek tuyuladi",
                          "Зачем нужен staging? Кажется лишним шагом",
                          "Why staging? It looks like an extra step"),
               extra_html=code(
                   "# Siz uchta faylni tahrirladingiz, lekin ular\n"
                   "# ikki xil vazifaga tegishli:\n\n"
                   "git add style.css navbar.html\n"
                   "git commit -m \"Navbar dizayni tuzatildi\"\n\n"
                   "git add api.js\n"
                   "git commit -m \"API xatosi tuzatildi\"\n\n"
                   "# Ikkita toza commit. Staging bo'lmasa\n"
                   "# hammasi bitta chalkash commitga tushardi.")),
))

S.append(slide(
    ph=("Commit xabari", "Сообщение коммита", "Commit message"), time="15–19",
    eyebrow=("Kelajakdagi o'zingizga xat", "Письмо себе в будущее",
             "A letter to your future self"),
    title=("Yaxshi commit xabari <b>nega</b> ga javob beradi",
           "Хорошее сообщение коммита отвечает на <b>почему</b>",
           "A good commit message answers <b>why</b>"),
    body='<div class="cols c2">\n'
         + box("accent", ("❌ Foydasiz xabarlar", "❌ Бесполезные сообщения",
                          "❌ Useless messages"),
               extra_html=code(
                   "\"fix\"\n"
                   "\"update\"\n"
                   "\"ishladi\"\n"
                   "\"asdfgh\"\n"
                   "\"o'zgartirishlar\"\n"
                   "\"final version\"\n\n"
                   "// Uch oydan keyin bu xabarlar\n"
                   "// hech narsa anglatmaydi."))
         + "\n"
         + box("green", ("✅ Foydali xabarlar", "✅ Полезные сообщения", "✅ Useful messages"),
               extra_html=code(
                   "\"Navbar mobil ekranda ustma-ust\n"
                   " tushishi tuzatildi\"\n\n"
                   "\"Valyuta API javobi bo'sh kelganda\n"
                   " xato xabari qo'shildi\"\n\n"
                   "\"Parol maydoniga minimal uzunlik\n"
                   " tekshiruvi qo'shildi\"\n\n"
                   "// Nima va nega — ikkalasi ham bor."))
         + "\n</div>\n"
         + box("purple", ("Sanoat standarti: Conventional Commits",
                          "Индустриальный стандарт: Conventional Commits",
                          "The industry standard: Conventional Commits"),
               extra_html=code(
                   "feat:     yangi imkoniyat qo'shildi\n"
                   "fix:      xato tuzatildi\n"
                   "docs:     hujjat o'zgardi\n"
                   "style:    formatlash, mantiq o'zgarmadi\n"
                   "refactor: kod qayta yozildi, xulq o'zgarmadi\n\n"
                   "fix: valyuta konverterida nol bo'lish xatosi\n"
                   "feat: qorong'i mavzu tugmasi qo'shildi")),
))

S.append(slide(
    ph=("Branch", "Ветки", "Branches"), time="19–24",
    eyebrow=("Parallel ish", "Параллельная работа", "Parallel work"),
    title=("Branch — bu nusxa emas, bu <b>ko'rsatkich</b>",
           "Ветка — это не копия, это <b>указатель</b>",
           "A branch is not a copy — it is a <b>pointer</b>"),
    body='<div class="cols c2">\n'
         + box("purple", ("Nega branch arzon", "Почему ветка «дешёвая»", "Why branches are cheap"),
               p=("Branch — bu papkaning nusxasi emas. Bu shunchaki <b>bitta commitga "
                  "ishora qiluvchi nom</b> — 40 belgidan iborat faylcha. Shuning uchun "
                  "branch yaratish <b>bir zumda</b> bo'ladi va joy egallamaydi. "
                  "Professional loyihalarda kuniga o'nlab branch yaratiladi.",
                  "Ветка — это не копия папки. Это просто <b>имя, указывающее на один "
                  "коммит</b> — файлик из 40 символов. Поэтому создание ветки "
                  "<b>мгновенное</b> и не занимает места. В профессиональных проектах "
                  "создают десятки веток в день.",
                  "A branch is not a copy of the folder. It is just a <b>name pointing at "
                  "one commit</b> — a file holding 40 characters. That is why creating a "
                  "branch is <b>instant</b> and costs no space. Professional projects "
                  "create dozens of branches a day."))
         + "\n"
         + box("green", ("Asosiy buyruqlar", "Основные команды", "The core commands"),
               extra_html=code(
                   "git branch                 # ro'yxat\n"
                   "git switch -c yangi-dizayn # yaratish + o'tish\n"
                   "git switch main            # qaytish\n\n"
                   "# Eski uslub (hali ham ishlaydi):\n"
                   "git checkout -b yangi-dizayn\n"
                   "git checkout main"))
         + "\n</div>\n"
         + box("accent", ("Nega alohida branchda ishlash kerak",
                          "Зачем работать в отдельной ветке",
                          "Why work in a separate branch"),
               items=[
                   ("<code>main</code> har doim <b>ishlaydigan</b> holatda qoladi — "
                    "uni istalgan payt ko'rsatish yoki deploy qilish mumkin.",
                    "<code>main</code> всегда остаётся в <b>рабочем</b> состоянии — "
                    "его можно в любой момент показать или задеплоить.",
                    "<code>main</code> always stays in a <b>working</b> state — you can "
                    "demo or deploy it at any moment."),
                   ("Tajriba muvaffaqiyatsiz chiqsa — branchni <b>o'chirasiz</b>, "
                    "xolos. Hech narsa buzilmaydi.",
                    "Если эксперимент провалился — вы просто <b>удаляете</b> ветку. "
                    "Ничего не сломано.",
                    "If the experiment fails you simply <b>delete</b> the branch. "
                    "Nothing is broken."),
                   ("Ikki kishi ikki branchda <b>bir vaqtda</b> ishlaydi va "
                    "bir-biriga xalaqit bermaydi.",
                    "Двое работают в двух ветках <b>одновременно</b> и не мешают друг другу.",
                    "Two people work in two branches <b>simultaneously</b> without "
                    "getting in each other's way."),
               ]),
))

S.append(slide(
    ph=("Merge", "Слияние", "Merge"), time="24–28",
    eyebrow=("Ikki tarixni birlashtirish", "Объединение двух историй",
             "Joining two histories"),
    title=("Merge — Git ikki zanjirni bitta qilib bog'laydi",
           "Merge — Git связывает две цепочки в одну",
           "Merge — Git ties two chains into one"),
    body='<div class="cols c2">\n'
         + box("green", ("Ikki xil merge", "Два вида слияния", "Two kinds of merge"),
               items=[
                   ("<b>Fast-forward:</b> <code>main</code> o'zgarmagan bo'lsa, Git "
                    "shunchaki ko'rsatkichni oldinga suradi. Yangi commit yaratilmaydi.",
                    "<b>Fast-forward:</b> если <code>main</code> не менялся, Git просто "
                    "сдвигает указатель вперёд. Новый коммит не создаётся.",
                    "<b>Fast-forward:</b> if <code>main</code> has not moved, Git simply "
                    "slides the pointer forward. No new commit is made."),
                   ("<b>Merge commit:</b> ikkala branch ham o'zgargan bo'lsa, Git "
                    "<b>ikkita otasi bor</b> maxsus commit yaratadi.",
                    "<b>Merge commit:</b> если менялись обе ветки, Git создаёт особый "
                    "коммит <b>с двумя родителями</b>.",
                    "<b>Merge commit:</b> if both branches moved, Git creates a special "
                    "commit <b>with two parents</b>."),
               ])
         + "\n"
         + box("purple", ("Buyruqlar ketma-ketligi", "Последовательность команд",
                          "The command sequence"),
               extra_html=code(
                   "# 1. Qabul qiluvchi branchga o'tish\n"
                   "git switch main\n\n"
                   "# 2. Ishni olib kelish\n"
                   "git merge yangi-dizayn\n\n"
                   "# 3. Kerak bo'lmasa branchni o'chirish\n"
                   "git branch -d yangi-dizayn"))
         + "\n</div>\n"
         + box("accent", ("Git qanday hal qiladi", "Как Git принимает решение",
                          "How Git decides"),
               p=("Git ikkala branchning <b>umumiy ajdodini</b> (merge base) topadi va "
                  "undan keyin nima o'zgarganini ikkala tomonda solishtiradi. "
                  "<b>Turli fayllar</b> yoki <b>turli qatorlar</b> o'zgargan bo'lsa — "
                  "Git hammasini avtomatik birlashtiradi va siz hech narsa qilmaysiz. "
                  "Muammo faqat bitta holatda tug'iladi — keyingi slaydda.",
                  "Git находит <b>общего предка</b> двух веток (merge base) и сравнивает, "
                  "что изменилось после него с каждой стороны. Если менялись "
                  "<b>разные файлы</b> или <b>разные строки</b> — Git объединит всё "
                  "автоматически, и вы ничего не делаете. Проблема возникает только "
                  "в одном случае — на следующем слайде.",
                  "Git finds the <b>common ancestor</b> of the two branches (the merge "
                  "base) and compares what changed on each side since then. If "
                  "<b>different files</b> or <b>different lines</b> changed, Git merges "
                  "everything automatically and you do nothing. Trouble arises in only "
                  "one case — on the next slide.")),
))

S.append(slide(
    ph=("Konflikt", "Конфликт", "Conflict"), time="28–33",
    eyebrow=("Eng ko'p qo'rqitadigan narsa", "То, чего боятся больше всего",
             "The thing people fear most"),
    title=("Merge konflikti — bu xato emas, bu <b>savol</b>",
           "Конфликт слияния — это не ошибка, это <b>вопрос</b>",
           "A merge conflict is not an error — it is a <b>question</b>"),
    body='<div class="cols c2">\n'
         + box("purple", ("Konflikt qachon yuzaga keladi",
                          "Когда возникает конфликт", "When a conflict happens"),
               p=("Faqat bitta holatda: <b>ikkala branchda aynan bir xil qator "
                  "boshqacha o'zgartirilgan</b>. Git ikkalasidan qaysi biri to'g'ri "
                  "ekanini bila olmaydi — bu <b>mazmunga oid</b> qaror, va uni faqat "
                  "inson qabul qila oladi. Shuning uchun Git to'xtaydi va sizdan so'raydi.",
                  "Только в одном случае: <b>в обеих ветках изменена одна и та же "
                  "строка по-разному</b>. Git не может знать, какой вариант правильный — "
                  "это <b>смысловое</b> решение, и принять его может только человек. "
                  "Поэтому Git останавливается и спрашивает вас.",
                  "In exactly one case: <b>both branches changed the very same line "
                  "differently</b>. Git cannot know which version is right — that is a "
                  "<b>semantic</b> decision only a human can make. So Git stops and asks."))
         + "\n"
         + box("accent", ("Faylda nima ko'rinadi", "Что вы увидите в файле",
                          "What you see in the file"),
               extra_html=code(
                   "<<<<<<< HEAD\n"
                   "<h1>Mening Portfoliom</h1>\n"
                   "=======\n"
                   "<h1>Aziz Karimov — Dasturchi</h1>\n"
                   ">>>>>>> yangi-dizayn\n\n"
                   "// HEAD          = siz turgan branch (main)\n"
                   "// yangi-dizayn  = olib kelinayotgan branch\n"
                   "// ======= belgisi ikkisini ajratadi"))
         + "\n</div>\n"
         + box("green", ("Yechish tartibi — to'rt qadam",
                         "Порядок решения — четыре шага", "How to resolve — four steps"),
               items=[
                   ("Faylni oching va <b>ikkala variantni o'qing</b>.",
                    "Откройте файл и <b>прочитайте оба варианта</b>.",
                    "Open the file and <b>read both versions</b>."),
                   ("Qaysi biri to'g'ri ekanini hal qiling — yoki <b>ikkalasini "
                    "birlashtirib</b> yangi variant yozing.",
                    "Решите, какой правильный — или напишите новый вариант, "
                    "<b>объединив оба</b>.",
                    "Decide which is right — or write a new version that "
                    "<b>combines both</b>."),
                   ("Uchala belgi qatorini <b>o'chiring</b>: "
                    "<code>&lt;&lt;&lt;</code>, <code>===</code>, <code>&gt;&gt;&gt;</code>.",
                    "<b>Удалите</b> все три строки-маркера: "
                    "<code>&lt;&lt;&lt;</code>, <code>===</code>, <code>&gt;&gt;&gt;</code>.",
                    "<b>Delete</b> all three marker lines: "
                    "<code>&lt;&lt;&lt;</code>, <code>===</code>, <code>&gt;&gt;&gt;</code>."),
                   ("<code>git add</code> va <code>git commit</code> — konflikt yopildi.",
                    "<code>git add</code> и <code>git commit</code> — конфликт закрыт.",
                    "<code>git add</code> and <code>git commit</code> — conflict closed."),
               ]),
))

S.append(slide(
    ph=("GitHub", "GitHub", "GitHub"), time="33–36",
    eyebrow=("Lokaldan bulutga", "С компьютера в облако", "From local to cloud"),
    title=("Git — kompyuteringizda. GitHub — internetda.",
           "Git — на вашем компьютере. GitHub — в интернете.",
           "Git is on your machine. GitHub is on the internet."),
    body='<div class="cols c2">\n'
         + box("green", ("Nima farqi bor", "В чём разница", "What is the difference"),
               items=[
                   ("<b>Git</b> — dastur. U internetsiz, butunlay sizning "
                    "kompyuteringizda ishlaydi.",
                    "<b>Git</b> — программа. Работает без интернета, полностью "
                    "на вашем компьютере.",
                    "<b>Git</b> is a program. It works offline, entirely on your machine."),
                   ("<b>GitHub</b> — sayt. U Git repozitoriyalarini saqlaydi va "
                    "ulashish imkonini beradi.",
                    "<b>GitHub</b> — сайт. Хранит Git-репозитории и позволяет "
                    "ими делиться.",
                    "<b>GitHub</b> is a website. It stores Git repositories and lets "
                    "you share them."),
                   ("GitHub o'rnini GitLab yoki Bitbucket ham bosa oladi — Git bitta.",
                    "Вместо GitHub может быть GitLab или Bitbucket — Git один.",
                    "GitLab or Bitbucket can replace GitHub — Git itself is the same."),
                   ("<b>Sizning GitHub profilingiz — bu portfolio.</b> Ish beruvchilar "
                    "va universitetlar unga qaraydi.",
                    "<b>Ваш профиль на GitHub — это портфолио.</b> Работодатели "
                    "и университеты смотрят на него.",
                    "<b>Your GitHub profile is a portfolio.</b> Employers and "
                    "universities look at it."),
               ])
         + "\n"
         + box("purple", ("To'rtta buyruq", "Четыре команды", "Four commands"),
               extra_html=code(
                   "git clone <url>   # birinchi marta yuklab olish\n"
                   "git push          # o'z commitlaringizni yuborish\n"
                   "git pull          # boshqalarnikini olish\n"
                   "git status        # hozir nima bo'layotganini ko'rish\n\n"
                   "# Oltin qoida:\n"
                   "# ishni boshlashdan oldin HAR DOIM git pull"))
         + "\n</div>",
))

S.append(slide(
    ph=("Amaliyot", "Практика", "Practice"), time="36–47",
    eyebrow=("Laboratoriya · 11 daqiqa", "Лаборатория · 11 минут", "Lab · 11 minutes"),
    title=("Git simulyatori: lab/index.html ni oching",
           "Симулятор Git: откройте lab/index.html",
           "Git simulator: open lab/index.html"),
    body='<div class="cols c4">\n' + "\n".join([
        box("purple", ("1 · Birinchi commit", "1 · Первый коммит", "1 · First commit"),
            p=("Faylni tahrirlang, <code>git add</code> va <code>git commit</code> "
               "bajaring. Grafda yangi tugun paydo bo'lishini kuzating.",
               "Отредактируйте файл, выполните <code>git add</code> и "
               "<code>git commit</code>. Смотрите, как в графе появляется новый узел.",
               "Edit the file, run <code>git add</code> and <code>git commit</code>. "
               "Watch a new node appear in the graph.")),
        box("green", ("2 · Branch", "2 · Ветка", "2 · Branch"),
            p=("<code>git switch -c yangi-dizayn</code> bilan branch yarating va "
               "u yerda 2 ta commit qiling. Graf ikkiga bo'linadi.",
               "Создайте ветку <code>git switch -c yangi-dizayn</code> и сделайте в ней "
               "2 коммита. Граф раздвоится.",
               "Create a branch with <code>git switch -c yangi-dizayn</code> and make "
               "2 commits there. The graph forks.")),
        box("accent", ("3 · Konflikt", "3 · Конфликт", "3 · Conflict"),
            p=("<b>Ikkala branchda ham 1-qatorni o'zgartiring</b>, keyin merge qiling. "
               "Konflikt chiqadi — uni yeching.",
               "<b>Измените строку 1 в обеих ветках</b>, затем выполните merge. "
               "Возникнет конфликт — разрешите его.",
               "<b>Change line 1 in both branches</b>, then merge. "
               "A conflict appears — resolve it.")),
        box("", ("4 · Tarix", "4 · История", "4 · History"),
            p=("<code>git log</code> bilan butun tarixni ko'ring va varaqaga "
               "commitlar sonini hamda oxirgi hash ni yozing.",
               "Посмотрите всю историю через <code>git log</code> и запишите в лист "
               "число коммитов и последний хэш.",
               "View the full history with <code>git log</code> and note the commit "
               "count and the last hash on your worksheet.")),
    ]) + "\n</div>\n"
         + box("green", ("Simulyator haqiqiy Git buyruqlarini qabul qiladi",
                         "Симулятор принимает настоящие команды Git",
                         "The simulator accepts real Git commands"),
               p=("Siz yozgan buyruqlar — <b>haqiqiy Git sintaksisi</b>. Shuning uchun "
                  "bugungi mashq keyinchalik terminalda to'g'ridan-to'g'ri ishlaydi. "
                  "Simulyator xato buyruqqa <b>Git ning haqiqiy xato xabarini</b> beradi.",
                  "Команды, которые вы вводите, — это <b>настоящий синтаксис Git</b>. "
                  "Поэтому сегодняшняя тренировка потом сработает прямо в терминале. "
                  "На неверную команду симулятор выдаёт <b>настоящее сообщение об "
                  "ошибке Git</b>.",
                  "The commands you type are <b>real Git syntax</b>. So today's practice "
                  "will work directly in a terminal later. On a wrong command the "
                  "simulator returns <b>Git's actual error message</b>.")),
))

S.append(slide(
    ph=("AI yordamchi", "AI помощник", "AI helper"), time="47–48",
    eyebrow=("Tayyor promptlar", "Готовые промпты", "Ready-made prompts"),
    title=("AI bilan Git — lekin ehtiyot bo'ling",
           "Git с помощью AI — но осторожно",
           "Git with AI — but carefully"),
    body='<div class="cols c2">\n'
         + box("purple", ("Nusxa oling", "Скопируйте", "Copy these"),
               extra_html=code(
                   "1) Объясни разницу между git merge и\n"
                   "   git rebase простыми словами, с примером\n"
                   "   на графе коммитов.\n\n"
                   "2) Я случайно сделал commit не в ту ветку.\n"
                   "   Как перенести последний коммит в другую\n"
                   "   ветку, ничего не потеряв? Объясни\n"
                   "   каждую команду перед выполнением.\n\n"
                   "3) Напиши сообщение коммита в формате\n"
                   "   Conventional Commits для: \"исправил\n"
                   "   деление на ноль в конвертере валют\"."))
         + "\n"
         + box("accent", ("🛑 Git bilan AI: xavfsizlik qoidasi",
                          "🛑 AI и Git: правило безопасности",
                          "🛑 AI and Git: the safety rule"),
               items=[
                   ("AI ba'zan <code>--force</code>, <code>reset --hard</code> yoki "
                    "<code>clean -fd</code> taklif qiladi. Bu buyruqlar ishni "
                    "<b>qaytarib bo'lmas darajada o'chiradi</b>.",
                    "AI иногда предлагает <code>--force</code>, <code>reset --hard</code> "
                    "или <code>clean -fd</code>. Эти команды удаляют работу "
                    "<b>безвозвратно</b>.",
                    "The AI sometimes suggests <code>--force</code>, "
                    "<code>reset --hard</code> or <code>clean -fd</code>. These delete "
                    "work <b>irreversibly</b>."),
                   ("<b>Qoida:</b> tushunmagan Git buyrug'ini bajarmang. Avval "
                    "\"что делает эта команда и что я потеряю?\" deb so'rang.",
                    "<b>Правило:</b> не выполняйте непонятную команду Git. Сначала "
                    "спросите: «что делает эта команда и что я потеряю?»",
                    "<b>Rule:</b> never run a Git command you do not understand. "
                    "First ask \"what does this do and what will I lose?\""),
                   ("<code>git status</code> — xavfsiz, u hech narsani o'zgartirmaydi. "
                    "Shubhalansangiz — avval shuni yozing.",
                    "<code>git status</code> безопасна, она ничего не меняет. "
                    "Сомневаетесь — начните с неё.",
                    "<code>git status</code> is safe, it changes nothing. "
                    "When in doubt, start there."),
               ])
         + "\n</div>",
))

S.append(slide(
    ph=("Yakun", "Итоги", "Summary"), time="48–50",
    eyebrow=("Uy vazifasi va baholash", "Домашнее задание и оценка", "Homework and grading"),
    title=("Uy vazifasi: Git jurnali va konflikt hisoboti (10 ball)",
           "Домашнее задание: журнал Git и отчёт о конфликте (10 баллов)",
           "Homework: Git log and conflict report (10 points)"),
    body='<div class="cols c2">\n'
         + box("green", ("Nima qilish kerak", "Что нужно сделать", "What to do"),
               items=[
                   ("Varaqadagi 4 bosqich jadvalini to'ldiring.",
                    "Заполните таблицу 4 этапов в рабочем листе.",
                    "Fill the 4-stage table on the worksheet."),
                   ("<b>3 ta yaxshi commit xabari</b> yozing — Conventional Commits "
                    "formatida, o'z loyihangiz uchun.",
                    "Напишите <b>3 хороших сообщения коммита</b> в формате "
                    "Conventional Commits для своего проекта.",
                    "Write <b>3 good commit messages</b> in Conventional Commits "
                    "format for your own project."),
                   ("Konfliktni qanday yechganingizni tushuntiring: qaysi variantni "
                    "tanladingiz va <b>nega</b>.",
                    "Объясните, как вы разрешили конфликт: какой вариант выбрали "
                    "и <b>почему</b>.",
                    "Explain how you resolved the conflict: which version you chose "
                    "and <b>why</b>."),
                   ("Uchta zonani (Working / Staging / Repository) o'z so'zingiz bilan "
                    "tavsiflang.",
                    "Опишите своими словами три зоны (Working / Staging / Repository).",
                    "Describe the three zones (Working / Staging / Repository) "
                    "in your own words."),
               ])
         + "\n"
         + box("accent", ("Baholash mezoni", "Критерии оценки", "Grading rubric"),
               extra_html='<ul class="plain">\n'
               + '  <li><span class="t" %s>4 bosqich jadvali — <b>3 ball</b></span></li>\n'
               % i18n("4 bosqich jadvali — <b>3 ball</b>",
                      "Таблица 4 этапов — <b>3 балла</b>",
                      "Table of 4 stages — <b>3 points</b>")
               + '  <li><span class="t" %s>3 ta commit xabari — <b>3 ball</b></span></li>\n'
               % i18n("3 ta commit xabari — <b>3 ball</b>",
                      "3 сообщения коммита — <b>3 балла</b>",
                      "3 commit messages — <b>3 points</b>")
               + '  <li><span class="t" %s>Konflikt yechimi va sababi — <b>2 ball</b></span></li>\n'
               % i18n("Konflikt yechimi va sababi — <b>2 ball</b>",
                      "Решение конфликта и обоснование — <b>2 балла</b>",
                      "Conflict resolution and reasoning — <b>2 points</b>")
               + '  <li><span class="t" %s>Uchta zona tavsifi — <b>2 ball</b></span></li>\n'
               % i18n("Uchta zona tavsifi — <b>2 ball</b>",
                      "Описание трёх зон — <b>2 балла</b>",
                      "The three zones described — <b>2 points</b>")
               + "</ul>")
         + "\n</div>",
))


NOTES = {
    "uz": [
        ["Titul slayd",
         "Salom! 11-darsda VS Code o'rnatdik, 12-darsda xato ovladik. Bugun professional dasturchilarning eng asosiy vositasini o'rganamiz — Git. Bu sizning GitHub profilingizning va kelajakdagi portfolioyangizning boshlanishi.",
         "lab/index.html ni proyektorda oldindan oching."],
        ["Muammo",
         "Sarlavhani o'qing va sinfdan so'rang: kimda shunday fayllar bor? Deyarli hamma qo'l ko'taradi. Keyin to'rtta savolni ayting: qaysi biri oxirgi, nima o'zgardi, nega o'zgardi, ikki kishi bo'lsa nima bo'ladi.",
         "Sinfdan so'rash: kimda 'final_v2' fayllari bor?"],
        ["Git modeli",
         "Muhim tushuncha: Git farqlarni emas, suratlarni saqlaydi. Ko'pchilik buni teskari tushunadi. Ota-bola zanjirini doskada chizing — branch va merge shu zanjir ustida quriladi.",
         "Doskada commit zanjirini chizish: o <- o <- o"],
        ["Uchta zona",
         "Working, Staging, Repository. Savol beriladi: nega staging kerak? Javobi kod blokida — bitta ishni ikkita toza commitga ajratish uchun. Bu professional odat.",
         "Simulyatorda add va commit ni jonli bajarish."],
        ["Commit xabari",
         "Ikki ustunni solishtiring. Muhim fikr: commit xabari — kelajakdagi o'zingizga xat. Conventional Commits standartini ko'rsating, bu ular ishga kirganda albatta uchraydi.",
         "Doskada 'fix:' va 'feat:' misollarini yozish."],
        ["Branch",
         "Eng muhim fikr: branch nusxa emas, ko'rsatkich. 40 belgili faylcha. Shuning uchun arzon va tez. Ayting: professional loyihalarda kuniga o'nlab branch yaratiladi.",
         "Simulyatorda branch yaratib, graf ikkiga bo'linishini ko'rsatish."],
        ["Merge",
         "Ikki xil merge: fast-forward va merge commit. Keyin eng muhim gapni ayting: turli qatorlar o'zgarsa Git hammasini o'zi qiladi. Muammo faqat bitta holatda — bu keyingi slaydga ko'prik.",
         "Simulyatorda oddiy merge ni ko'rsatish."],
        ["Konflikt",
         "Bolalar konfliktdan qo'rqadi. Asosiy xabar: konflikt xato emas, savol. Git sizdan so'rayapti, chunki mazmunni faqat inson biladi. Belgilarni doskada chizing va to'rt qadamni ayting.",
         "Doskada <<<<<<< ======= >>>>>>> belgilarini chizish."],
        ["GitHub",
         "Git va GitHub farqini aniq ajrating — bu klassik chalkashlik. Keyin muhim gap: GitHub profili — portfolio. Universitet va ish beruvchilar unga qaraydi. Bu 9-sinf uchun kuchli motivatsiya.",
         "GitHub profilini proyektorda ko'rsatish (ixtiyoriy)."],
        ["Amaliyot 11 daqiqa",
         "To'rt bosqich. Eng muhimi uchinchisi — konflikt. Ko'p o'quvchi uni chetlab o'tmoqchi bo'ladi, majburlang: ikkala branchda ham 1-qatorni o'zgartirish kerak.",
         "Sinf bo'ylab yurish. Konflikt bosqichini nazorat qilish."],
        ["AI bilan ishlash",
         "Juda muhim xavfsizlik qoidasi: AI --force va reset --hard taklif qilishi mumkin. Bu ishni qaytarib bo'lmas darajada o'chiradi. Qoida: tushunmagan buyruqni bajarmang.",
         "Doskaga yozib qo'yish: 'Tushunmagan Git buyrug'ini bajarmang'."],
        ["Yakun va baholash",
         "Xulosa: Git — suratlar zanjiri, branch — ko'rsatkich, konflikt — savol. Varaqalarni yig'ing. Keyingi dars — Pull Request va kod ko'rigi.",
         "Varaqalarni yig'ish. Keyingi dars haqida qiziqtirish."],
    ],
    "ru": [
        ["Титульный слайд",
         "Привет! На уроке 11 поставили VS Code, на 12 охотились за багами. Сегодня изучаем главный инструмент профессиональных разработчиков — Git. Это начало вашего профиля на GitHub и будущего портфолио.",
         "Заранее откройте lab/index.html на проекторе."],
        ["Проблема",
         "Прочитайте заголовок и спросите класс: у кого есть такие файлы? Руки поднимут почти все. Затем озвучьте четыре вопроса: какой последний, что изменилось, почему изменилось, что если работают двое.",
         "Спросить класс: у кого есть файлы вида 'финал_v2'?"],
        ["Модель Git",
         "Ключевое понятие: Git хранит не разницу, а снимки. Многие понимают это наоборот. Нарисуйте цепочку родитель-потомок на доске — ветки и слияния строятся на ней.",
         "Нарисовать на доске цепочку коммитов: o <- o <- o"],
        ["Три зоны",
         "Working, Staging, Repository. Задайте вопрос: зачем нужен staging? Ответ в блоке кода — чтобы разделить работу на два чистых коммита. Это профессиональная привычка.",
         "Живьём выполнить add и commit в симуляторе."],
        ["Сообщение коммита",
         "Сравните две колонки. Главная мысль: сообщение коммита — письмо себе в будущее. Покажите стандарт Conventional Commits, они обязательно встретят его на работе.",
         "Написать на доске примеры 'fix:' и 'feat:'."],
        ["Ветки",
         "Самая важная мысль: ветка не копия, а указатель. Файлик из 40 символов. Поэтому дёшево и мгновенно. Скажите: в профессиональных проектах создают десятки веток в день.",
         "Создать ветку в симуляторе и показать раздвоение графа."],
        ["Слияние",
         "Два вида: fast-forward и merge commit. Затем главное: если менялись разные строки, Git сделает всё сам. Проблема только в одном случае — мостик к следующему слайду.",
         "Показать простой merge в симуляторе."],
        ["Конфликт",
         "Дети боятся конфликтов. Главное сообщение: конфликт не ошибка, а вопрос. Git спрашивает вас, потому что смысл знает только человек. Нарисуйте маркеры на доске и назовите четыре шага.",
         "Нарисовать на доске <<<<<<< ======= >>>>>>>"],
        ["GitHub",
         "Чётко разделите Git и GitHub — это классическая путаница. Затем важная мысль: профиль на GitHub — это портфолио. На него смотрят университеты и работодатели. Для 9 класса это сильная мотивация.",
         "Показать профиль GitHub на проекторе (по желанию)."],
        ["Практика 11 минут",
         "Четыре этапа. Самый важный — третий, конфликт. Многие захотят его обойти, настаивайте: нужно изменить строку 1 в обеих ветках.",
         "Ходить по классу. Контролировать этап с конфликтом."],
        ["Работа с AI",
         "Очень важное правило безопасности: AI может предложить --force и reset --hard. Это удаляет работу безвозвратно. Правило: не выполняйте непонятную команду.",
         "Написать на доске: «Не выполняй непонятную команду Git»."],
        ["Итоги и оценивание",
         "Вывод: Git — цепочка снимков, ветка — указатель, конфликт — вопрос. Соберите листы. Следующий урок — Pull Request и код-ревью.",
         "Собрать листы. Заинтриговать следующим уроком."],
    ],
    "en": [
        ["Title slide",
         "Hello! In lesson 11 we installed VS Code, in 12 we hunted bugs. Today we learn the core tool of professional developers — Git. This is the start of your GitHub profile and your future portfolio.",
         "Pre-open lab/index.html on the projector."],
        ["The problem",
         "Read the title and ask the class: who has files like this? Almost every hand goes up. Then state the four questions: which is latest, what changed, why it changed, what happens with two people.",
         "Ask the class: who has 'final_v2' files?"],
        ["The Git model",
         "Key concept: Git stores snapshots, not differences. Many people get this backwards. Draw the parent chain on the board — branches and merges are built on it.",
         "Draw the commit chain on the board: o <- o <- o"],
        ["Three zones",
         "Working, Staging, Repository. Ask: why do we need staging? The answer is in the code block — to split work into two clean commits. A professional habit.",
         "Run add and commit live in the simulator."],
        ["Commit messages",
         "Compare the two columns. Core idea: a commit message is a letter to your future self. Show the Conventional Commits standard — they will meet it at work.",
         "Write 'fix:' and 'feat:' examples on the board."],
        ["Branches",
         "The key point: a branch is a pointer, not a copy. A file holding 40 characters. That is why it is cheap and instant. Say that professional projects create dozens a day.",
         "Create a branch in the simulator and show the graph fork."],
        ["Merging",
         "Two kinds: fast-forward and merge commit. Then the key line: if different lines changed, Git does it all itself. Trouble arises in one case only — the bridge to the next slide.",
         "Show a simple merge in the simulator."],
        ["Conflicts",
         "Students fear conflicts. The core message: a conflict is not an error, it is a question. Git asks you because only a human knows the meaning. Draw the markers and state the four steps.",
         "Draw <<<<<<< ======= >>>>>>> on the board."],
        ["GitHub",
         "Separate Git and GitHub clearly — a classic confusion. Then the key point: a GitHub profile is a portfolio. Universities and employers look at it. Strong motivation for grade 9.",
         "Show a GitHub profile on the projector (optional)."],
        ["Practice, 11 minutes",
         "Four stages. The third one — the conflict — matters most. Many will try to skip it; insist they change line 1 in both branches.",
         "Walk the room. Supervise the conflict stage."],
        ["Working with AI",
         "A critical safety rule: the AI may suggest --force and reset --hard. These delete work irreversibly. Rule: never run a command you do not understand.",
         "Write on the board: 'Never run a Git command you do not understand'."],
        ["Summary and grading",
         "Conclusion: Git is a chain of snapshots, a branch is a pointer, a conflict is a question. Collect the sheets. Next lesson — Pull Requests and code review.",
         "Collect sheets. Tease the next lesson."],
    ],
}

VARAQA = (
    sheet_header(
        ("13-dars: Git va GitHub — Commit, Branch va Merge Konflikti",
         "Урок 13: Git и GitHub — Commit, Branch и Merge-конфликт",
         "Lesson 13: Git and GitHub — Commit, Branch and Merge Conflict"),
        ("Target International School · 9-sinf · 3-hafta (1-soat)",
         "Target International School · 9 класс · 3-я неделя (1-й час)",
         "Target International School · Grade 9 · Week 3 (Hour 1)"))
    + mission(
        ("🎯 Missiya: tarix yarating, bo'ling va birlashtiring",
         "🎯 Миссия: создайте историю, разветвите и слейте",
         "🎯 Mission: build a history, branch it, merge it"),
        ("<b>lab/index.html</b> ni oching. Simulyator <b>haqiqiy Git buyruqlarini</b> "
         "qabul qiladi. Vazifa: commit qiling, branch yarating, ataylab "
         "<b>konflikt keltirib chiqaring</b> va uni yeching. Konfliktdan qochmang — "
         "u darsning asosiy qismi.",
         "Откройте <b>lab/index.html</b>. Симулятор принимает <b>настоящие команды Git</b>. "
         "Задача: сделать коммиты, создать ветку, намеренно <b>вызвать конфликт</b> "
         "и разрешить его. Не избегайте конфликта — это главная часть урока.",
         "Open <b>lab/index.html</b>. The simulator accepts <b>real Git commands</b>. "
         "Your task: commit, branch, deliberately <b>cause a conflict</b> and resolve it. "
         "Do not avoid the conflict — it is the core of this lesson."))
    + table(
        [("Bosqich", "Этап", "Stage"),
         ("Buyruqlar", "Команды", "Commands"),
         ("Natija", "Результат", "Result")],
        [[("1 · Commit", "1 · Коммит", "1 · Commit"),
          ("git add . → git commit -m \"...\"",
           "git add . → git commit -m \"...\"",
           "git add . → git commit -m \"...\""),
          ("Commit hash: ____________",
           "Хэш коммита: ____________",
           "Commit hash: ____________")],
         [("2 · Branch", "2 · Ветка", "2 · Branch"),
          ("git switch -c yangi-dizayn → 2 ta commit",
           "git switch -c yangi-dizayn → 2 коммита",
           "git switch -c yangi-dizayn → 2 commits"),
          ("Branch nomi: ____________ · Commitlar: ____",
           "Имя ветки: ____________ · Коммитов: ____",
           "Branch name: ____________ · Commits: ____")],
         [("3 · Konflikt", "3 · Конфликт", "3 · Conflict"),
          ("Ikkala branchda 1-qator → git merge",
           "Строка 1 в обеих ветках → git merge",
           "Line 1 in both branches → git merge"),
          ("Konflikt chiqdimi? HA / YO'Q · Qaysi fayl: ______",
           "Был конфликт? ДА / НЕТ · Какой файл: ______",
           "Conflict? YES / NO · Which file: ______")],
         [("4 · Tarix", "4 · История", "4 · History"),
          ("git log", "git log", "git log"),
          ("Jami commitlar: ____ · Oxirgi hash: __________",
           "Всего коммитов: ____ · Последний хэш: __________",
           "Total commits: ____ · Last hash: __________")]])
    + '    <div class="rubric-grid">\n'
    + sheet_box(
        ("✏️ Nazariya va konflikt hisoboti",
         "✏️ Теория и отчёт о конфликте",
         "✏️ Theory and conflict report"),
        writelines(3, ("3 ta commit xabari (Conventional Commits: feat: / fix: / docs:):",
                       "3 сообщения коммита (Conventional Commits: feat: / fix: / docs:):",
                       "3 commit messages (Conventional Commits: feat: / fix: / docs:):"))
        + "\n"
        + writelines(2, ("Konfliktni qanday yechdingiz va NEGA shu variantni tanladingiz:",
                         "Как вы разрешили конфликт и ПОЧЕМУ выбрали этот вариант:",
                         "How you resolved the conflict and WHY you chose that version:"))
        + "\n"
        + writelines(2, ("Uchta zona: Working Directory / Staging Area / Repository:",
                         "Три зоны: Working Directory / Staging Area / Repository:",
                         "The three zones: Working Directory / Staging Area / Repository:")))
    + "\n"
    + sheet_box(
        ("📊 Baholash mezoni (10 ball)",
         "📊 Критерии оценки (10 баллов)",
         "📊 Grading rubric (10 points)"),
        rubric([
            (("4 bosqich jadvali", "Таблица 4 этапов", "Table of 4 stages"), "3"),
            (("3 ta commit xabari", "3 сообщения коммита", "3 commit messages"), "3"),
            (("Konflikt yechimi va sababi", "Решение конфликта и обоснование",
              "Conflict resolution and reasoning"), "2"),
            (("Uchta zona tavsifi", "Описание трёх зон", "The three zones described"), "2"),
        ], "10"))
    + "\n    </div>\n  </div>\n"
    + sign_box()
)

if __name__ == "__main__":
    print(Lesson(D, TITLES, SHEET_TITLES, "vc-notes-9-13", S, NOTES, VARAQA).build())
