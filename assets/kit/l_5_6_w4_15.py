# -*- coding: utf-8 -*-
"""5-6-sinf · 4-hafta · 15-dars — Dushman AI: Patrul, Ko'rish Radiusi va Ta'qib."""

import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from build import (Lesson, slide, title_slide, box, ul, code, el, i18n)

D = "classes/5-6-sinf/4-hafta/15-dars-dushman-ai-va-tagib"

TITLES = {
    "uz": "15-dars: Dushman AI — Patrul, Ko'rish Radiusi va Ta'qib",
    "ru": "Урок 15: ИИ Врага — Патруль, Радиус Зрения и Погоня",
    "en": "Lesson 15: Enemy AI — Patrol, Vision Radius and Chase",
}
SHEET_TITLES = {k: v + (" — Ish Varaqasi" if k == "uz" else
                        " — Рабочий Лист" if k == "ru" else " — Worksheet")
                for k, v in TITLES.items()}

S = []

S.append(title_slide(
    ph=("Kirish", "Введение", "Intro"), time="0–3",
    eyebrow=("Vibecoding · 15-dars · 5–6-sinflar",
             "Vibecoding · Урок 15 · 5–6 классы",
             "Vibecoding · Lesson 15 · Grades 5–6"),
    h1=("Dushman AI: Patrul, Ko'rish Radiusi va Ta'qib",
        "ИИ Врага: Патруль, Радиус Зрения и Погоня",
        "Enemy AI: Patrol, Vision Radius and Chase"),
    lede=("O'tgan darsda trassada tikan va lazer bor edi — lekin ular qimirlamaydi, "
          "o'ylamaydi. Bugun biz trassaga <b>tirik dushman</b> qo'yamiz: u patrul qiladi, "
          "qahramonni ko'radi va ortidan quvadi. Dushmanning \"miyasi\" — bu sehr emas, "
          "bu <b>uchta oddiy qoida</b>, va siz ularni bugun o'zingiz sozlaysiz.",
          "На прошлом уроке на трассе были шипы и лазер — но они не двигаются и не думают. "
          "Сегодня мы поставим на трассу <b>живого врага</b>: он патрулирует, замечает героя "
          "и бежит за ним. «Мозг» врага — это не магия, это <b>три простых правила</b>, "
          "и сегодня вы настроите их сами.",
          "Last lesson the track had spikes and a laser — but they never move or think. "
          "Today we add a <b>living enemy</b>: it patrols, spots the hero and chases. "
          "The enemy's \"brain\" is not magic — it is <b>three simple rules</b>, "
          "and today you will tune them yourself."),
    meta=[("<b>Fan:</b> Vibecoding · O'yin yaratish",
           "<b>Предмет:</b> Vibecoding · Геймдев",
           "<b>Subject:</b> Vibecoding · Game Dev"),
          ("<b>Kohorta:</b> 5–6-sinf (10–12 yosh)",
           "<b>Когорта:</b> 5–6 класс (10–12 лет)",
           "<b>Cohort:</b> Grades 5–6 (ages 10–12)"),
          ("<b>Hafta:</b> 4 (1-soat)", "<b>Неделя:</b> 4 (1-й час)", "<b>Week:</b> 4 (Hour 1)")],
))

S.append(slide(
    ph=("Muammo", "Проблема", "Problem"), time="3–6",
    eyebrow=("Nega o'yin zerikarli?", "Почему игра скучная?", "Why is the game boring?"),
    title=("Tikan qimirlamaydi. Dushman — o'ylaydi.",
           "Шип не двигается. Враг — думает.",
           "A spike never moves. An enemy thinks."),
    body='<div class="cols c3">\n' + "\n".join([
        box("", ("🪨 Tikan (o'tgan dars)", "🪨 Шип (прошлый урок)", "🪨 Spike (last lesson)"),
            p=("Bir joyda turadi. Siz yo'lni yodlab olasiz va 3-urinishda muammosiz o'tasiz. "
               "Qiziqish 2 daqiqada tugaydi.",
               "Стоит на одном месте. Вы запоминаете путь и с 3-й попытки проходите без проблем. "
               "Интерес заканчивается за 2 минуты.",
               "It stands still. You memorise the path and clear it on attempt 3. "
               "The fun runs out in 2 minutes.")),
        box("purple", ("🔁 Lazer (o'tgan dars)", "🔁 Лазер (прошлый урок)", "🔁 Laser (last lesson)"),
            p=("Harakatlanadi, lekin <b>doim bir xil</b>. Ritmni poylash kerak. "
               "Bu allaqachon qiziqroq, ammo lazer sizni ko'rmaydi.",
               "Двигается, но <b>всегда одинаково</b>. Нужно поймать ритм. "
               "Уже интереснее, но лазер вас не видит.",
               "It moves, but <b>always the same way</b>. You time the rhythm. "
               "Better — but the laser cannot see you.")),
        box("accent", ("🤖 Dushman AI (bugun)", "🤖 ИИ Врага (сегодня)", "🤖 Enemy AI (today)"),
            p=("<b>Sizga qarab o'zgaradi.</b> Yashirinsangiz — qidiradi. Yugursangiz — quvadi. "
               "Har o'yin boshqacha chiqadi. Mana shuning uchun Mario, Roblox va Among Us "
               "zerikarli emas.",
               "<b>Меняется в ответ на вас.</b> Спрячетесь — ищет. Побежите — догоняет. "
               "Каждая партия другая. Именно поэтому Mario, Roblox и Among Us не надоедают.",
               "<b>It reacts to you.</b> Hide and it searches. Run and it chases. "
               "Every run differs. That is why Mario, Roblox and Among Us stay fun.")),
    ]) + "\n</div>",
))

S.append(slide(
    ph=("Asosiy g'oya", "Главная идея", "Core idea"), time="6–10",
    eyebrow=("Dushmanning miyasi", "Мозг врага", "The enemy's brain"),
    title=("Dushmanda 3 ta kayfiyat bor — boshqa hech narsa yo'q",
           "У врага есть 3 настроения — и больше ничего",
           "The enemy has 3 moods — and nothing else"),
    body='<div class="cols c3">\n' + "\n".join([
        box("green", ("1 · 😴 PATRUL", "1 · 😴 ПАТРУЛЬ", "1 · 😴 PATROL"),
            p=("Dushman qahramonni ko'rmayapti. U o'z yo'lida sokin yuradi: chapga, o'ngga, "
               "chapga... Ustida belgi yo'q.",
               "Враг не видит героя. Он спокойно ходит по своему маршруту: влево, вправо, "
               "влево... Значка над ним нет.",
               "The enemy cannot see the hero. It walks its route calmly: left, right, "
               "left... No icon above it.")),
        box("purple", ("2 · ❓ SEZDI", "2 · ❓ ЗАМЕТИЛ", "2 · ❓ ALERTED"),
            p=("Qahramon ko'rish radiusiga kirdi! Dushman <b>to'xtaydi</b> va 0.5 soniya "
               "o'ylaydi. Ustida sariq <b>?</b> chiqadi. Bu sizga qochish uchun berilgan fursat.",
               "Герой попал в радиус зрения! Враг <b>останавливается</b> и думает 0.5 секунды. "
               "Над ним появляется жёлтый <b>?</b>. Это ваш шанс убежать.",
               "The hero entered the vision radius! The enemy <b>stops</b> and thinks for 0.5s. "
               "A yellow <b>?</b> appears above it. That is your chance to escape.")),
        box("accent", ("3 · ❗ TA'QIB", "3 · ❗ ПОГОНЯ", "3 · ❗ CHASE"),
            p=("Dushman qizil <b>!</b> bilan qahramon tomon yuguradi. Tezligi oshadi. "
               "Tegib ketsa — <b>1 jon</b> ketadi (o'tgan darsdagi HP tizimi).",
               "Враг с красным <b>!</b> бежит к герою. Скорость растёт. "
               "Коснётся — минус <b>1 жизнь</b> (система HP из прошлого урока).",
               "The enemy runs at the hero with a red <b>!</b>. Its speed rises. "
               "On contact you lose <b>1 life</b> (the HP system from last lesson).")),
    ]) + "\n</div>\n" + box("", (
        "💡 Kattalar buni qanday ataydi?", "💡 Как это называют взрослые?",
        "💡 What do grown-ups call this?"),
        p=("Bu uchta kayfiyatning almashuvi — <b>holat mashinasi</b> (state machine). "
           "Xuddi shu narsa svetoforni ham boshqaradi: qizil → sariq → yashil. "
           "Dunyodagi deyarli barcha o'yin dushmanlari shu tamoyilda ishlaydi.",
           "Смена этих трёх настроений — <b>машина состояний</b> (state machine). "
           "Точно так же работает светофор: красный → жёлтый → зелёный. "
           "Почти все игровые враги в мире построены на этом принципе.",
           "Switching between these three moods is a <b>state machine</b>. "
           "A traffic light works the same way: red → amber → green. "
           "Nearly every game enemy in the world is built on this idea.")),
))

S.append(slide(
    ph=("Qoida 1", "Правило 1", "Rule 1"), time="10–13",
    eyebrow=("Patrul qanday ishlaydi", "Как работает патруль", "How patrol works"),
    title=("Patrul — bu ikki ustun orasidagi yurish",
           "Патруль — это ходьба между двумя столбами",
           "Patrol is walking between two posts"),
    body='<div class="cols c2">\n'
         + box("", ("Kompyuterga aytiladigan gap", "Что мы говорим компьютеру", "What we tell the computer"),
               items=[
                   ("Dushmanning <b>chap chegarasi</b> va <b>o'ng chegarasi</b> bor.",
                    "У врага есть <b>левая граница</b> и <b>правая граница</b>.",
                    "The enemy has a <b>left edge</b> and a <b>right edge</b>."),
                   ("Har kadrda u qarab turgan tomonga bir qadam siljiydi.",
                    "Каждый кадр он делает шаг в ту сторону, куда смотрит.",
                    "Each frame it steps in the direction it faces."),
                   ("Chegaraga yetdimi? — <b>tomonni teskarisiga almashtir</b>.",
                    "Дошёл до границы? — <b>меняем сторону на противоположную</b>.",
                    "Reached an edge? — <b>flip the direction</b>."),
                   ("Tamom. Patrul shu — uch qator qoida, sehr yo'q.",
                    "Всё. Патруль — это три строки правил, никакой магии.",
                    "That is all. Patrol is three lines of rules, no magic."),
               ])
         + "\n"
         + box("green", ("Kodda qanday ko'rinadi", "Как это выглядит в коде", "How it looks in code"),
               extra_html=code(
                   "// dushman.yon: 1 = o'ngga, -1 = chapga\n"
                   "dushman.x = dushman.x + dushman.yon * dushman.tezlik;\n\n"
                   "if (dushman.x > dushman.ongChegara) {\n"
                   "  dushman.yon = -1;   // burildi\n"
                   "}\n"
                   "if (dushman.x < dushman.chapChegara) {\n"
                   "  dushman.yon = 1;    // yana burildi\n"
                   "}"))
         + "\n</div>\n"
         + box("purple", ("🎛 Stendda sinab ko'ring", "🎛 Проверьте на стенде", "🎛 Try it on the lab"),
               p=("<b>Patrul kengligi</b> slayderi — chegaralar orasidagi masofa. "
                  "Tor qilsangiz dushman bir joyda tebranadi, keng qilsangiz butun xonani aylanadi.",
                  "Слайдер <b>Ширина патруля</b> — расстояние между границами. "
                  "Сузите — враг топчется на месте, расширьте — обходит всю комнату.",
                  "The <b>Patrol width</b> slider sets the gap between edges. "
                  "Narrow it and the enemy shuffles in place; widen it and it circles the room.")),
))

S.append(slide(
    ph=("Qoida 2", "Правило 2", "Rule 2"), time="13–17",
    eyebrow=("Ko'rish radiusi", "Радиус зрения", "Vision radius"),
    title=("Dushman qanday \"ko'radi\"? Ikkita savol bilan.",
           "Как враг «видит»? Двумя вопросами.",
           "How does the enemy \"see\"? With two questions."),
    body='<div class="cols c2">\n' + "\n".join([
        box("accent", ("Savol 1: yaqinmi?", "Вопрос 1: близко ли?", "Question 1: is it near?"),
            p=("Kompyuter dushman bilan qahramon orasidagi <b>masofani</b> o'lchaydi. "
               "Agar masofa ko'rish radiusidan kichik bo'lsa — birinchi shart bajarildi. "
               "Bu xuddi sizning atrofingizdagi ko'rinmas doira.",
               "Компьютер измеряет <b>расстояние</b> между врагом и героем. "
               "Если оно меньше радиуса зрения — первое условие выполнено. "
               "Это как невидимый круг вокруг врага.",
               "The computer measures the <b>distance</b> between enemy and hero. "
               "If it is smaller than the vision radius, condition one passes. "
               "Think of an invisible circle around the enemy.")),
        box("purple", ("Savol 2: shu tomondami?", "Вопрос 2: в ту ли сторону?", "Question 2: the right way?"),
            p=("Dushmanning <b>orqa ko'zi yo'q!</b> U faqat o'zi qarab turgan tomonni ko'radi. "
               "Agar qahramon orqada bo'lsa — dushman uni sezmaydi. "
               "Mana shuning uchun o'yinlarda dushman orqasidan o'tish mumkin.",
               "У врага <b>нет глаз на затылке!</b> Он видит только ту сторону, куда смотрит. "
               "Если герой сзади — враг его не замечает. "
               "Именно поэтому в играх можно прокрасться врагу за спину.",
               "The enemy has <b>no eyes in the back of its head!</b> It sees only where it faces. "
               "A hero behind it stays unseen. "
               "That is exactly why you can sneak up behind enemies in games.")),
    ]) + "\n</div>\n"
         + box("green", ("Ikkala shart birga bajarilsa — SEZDI",
                         "Оба условия вместе — ЗАМЕТИЛ", "Both conditions together — ALERTED"),
               extra_html=code(
                   "masofa = |qahramon.x - dushman.x|;\n"
                   "oldindami = (qahramon.x - dushman.x) * dushman.yon > 0;\n\n"
                   "if (masofa < korishRadiusi && oldindami) {\n"
                   "  dushman.kayfiyat = 'SEZDI';   // ❓ sariq belgi\n"
                   "}")),
))

S.append(slide(
    ph=("Qoida 2+", "Правило 2+", "Rule 2+"), time="17–20",
    eyebrow=("Devor to'sadi", "Стена мешает", "Walls block sight"),
    title=("Devor orqasida turgan qahramon ko'rinmaydi",
           "Героя за стеной не видно",
           "A hero behind a wall stays invisible"),
    body='<div class="cols c2">\n' + "\n".join([
        box("", ("Nega bu muhim?", "Почему это важно?", "Why does it matter?"),
            p=("Agar dushman devor orqali ham ko'raversa, o'yinchi <b>hech qayerga yashirina "
               "olmaydi</b> — va o'yin adolatsiz bo'lib qoladi. Yashirinish imkoni — "
               "o'yinni qiziqarli qiladigan asosiy narsa.",
               "Если враг видит сквозь стену, игроку <b>негде спрятаться</b> — "
               "и игра становится нечестной. Возможность спрятаться — главное, "
               "что делает игру интересной.",
               "If the enemy sees through walls the player has <b>nowhere to hide</b> — "
               "and the game feels unfair. The option to hide is the main thing "
               "that makes it fun.")),
        box("accent", ("Kompyuter buni qanday tekshiradi?",
                       "Как компьютер это проверяет?", "How does the computer check?"),
            p=("U dushmanning ko'zidan qahramongacha <b>ko'rinmas nur</b> (ray) tortadi. "
               "Agar nur yo'lda biror devorga urilsa — demak ko'rinmaydi. "
               "Bu usul <b>Line of Sight</b> (ko'rish chizig'i) deb ataladi.",
               "Он проводит от глаз врага к герою <b>невидимый луч</b> (ray). "
               "Если луч упирается в стену — значит, не видно. "
               "Этот приём называется <b>Line of Sight</b> (линия обзора).",
               "It draws an <b>invisible ray</b> from the enemy's eye to the hero. "
               "If the ray hits a wall, there is no sight. "
               "The trick is called <b>Line of Sight</b>.")),
    ]) + "\n</div>\n"
         + box("purple", ("🎮 Stendda: \"Devorni yoqish\" tugmasi",
                          "🎮 На стенде: кнопка «Включить стену»",
                          "🎮 On the lab: the \"Wall on\" button"),
               p=("Tugmani bosing va maydon o'rtasida ustun paydo bo'ladi. Ustun orqasiga "
                  "turib ko'ring — dushmanning sariq konusi devorda kesiladi va siz ko'rinmay "
                  "qolasiz. Keyin tugmani o'chiring va farqni his qiling.",
                  "Нажмите кнопку — посреди площадки появится столб. Встаньте за него: "
                  "жёлтый конус врага обрежется о стену, и вас не видно. "
                  "Потом выключите кнопку и почувствуйте разницу.",
                  "Press it and a post appears mid-arena. Stand behind it: the enemy's yellow "
                  "cone is cut off by the wall and you vanish. "
                  "Then switch it off and feel the difference.")),
))

S.append(slide(
    ph=("Qoida 3", "Правило 3", "Rule 3"), time="20–23",
    eyebrow=("Ta'qib", "Погоня", "The chase"),
    title=("Ta'qib — bu bitta savol: \"u chapdami yoki o'ngdami?\"",
           "Погоня — это один вопрос: «он слева или справа?»",
           "Chasing is one question: \"is it left or right?\""),
    body='<div class="cols c2">\n'
         + box("accent", ("Butun ta'qib mantig'i", "Вся логика погони", "The whole chase logic"),
               extra_html=code(
                   "if (qahramon.x > dushman.x) {\n"
                   "  dushman.yon = 1;    // o'ngga yugur\n"
                   "} else {\n"
                   "  dushman.yon = -1;   // chapga yugur\n"
                   "}\n\n"
                   "dushman.x += dushman.yon * dushman.taqibTezligi;"))
         + "\n"
         + box("green", ("Ajablanarli haqiqat", "Удивительный факт", "A surprising fact"),
               p=("Ha, shundoq xolos. Dunyodagi eng mashhur o'yin dushmanlarining ko'pi "
                  "<b>aynan shu to'rt qator</b> bilan quvadi. Murakkab \"sun'iy intellekt\" "
                  "emas — oddiy taqqoslash. Aqlli ko'rinish esa <b>ko'rish radiusi</b> va "
                  "<b>kechikish</b> hisobiga paydo bo'ladi.",
                  "Да, и всё. Большинство самых известных игровых врагов гонятся за вами "
                  "<b>именно этими четырьмя строками</b>. Никакого сложного «искусственного "
                  "интеллекта» — простое сравнение. А умным враг кажется за счёт "
                  "<b>радиуса зрения</b> и <b>задержки</b>.",
                  "Yes, that is it. Most famous game enemies chase you with "
                  "<b>exactly these four lines</b>. No complex \"artificial intelligence\" — "
                  "just a comparison. The smart feel comes from the <b>vision radius</b> "
                  "and the <b>reaction delay</b>."))
         + "\n</div>",
))

S.append(slide(
    ph=("Qoida 4", "Правило 4", "Rule 4"), time="23–26",
    eyebrow=("Xotira va unutish", "Память и забывание", "Memory and forgetting"),
    title=("Dushman qahramonni yo'qotsa nima qiladi?",
           "Что делает враг, потеряв героя из виду?",
           "What happens when the enemy loses the hero?"),
    body='<div class="cols c3">\n' + "\n".join([
        box("", ("❌ Yomon variant", "❌ Плохой вариант", "❌ Bad option"),
            p=("Darhol unutadi va patrulga qaytadi. O'yinchi bir qadam orqaga tisarilib, "
               "dushmanni cheksiz aldayveradi. Zerikarli.",
               "Сразу забывает и возвращается к патрулю. Игрок делает шаг назад "
               "и бесконечно обманывает врага. Скучно.",
               "It forgets at once and returns to patrol. The player steps back "
               "and fools it forever. Boring.")),
        box("accent", ("❌ Yana yomon variant", "❌ Тоже плохой вариант", "❌ Also bad"),
            p=("Hech qachon unutmaydi va o'yin oxirigacha quvadi. O'yinchi hech qachon "
               "dam ololmaydi. Asabiylashtiradi.",
               "Никогда не забывает и гонится до конца игры. Игрок не может передохнуть. "
               "Это раздражает.",
               "It never forgets and chases to the end. The player never gets a break. "
               "Frustrating.")),
        box("green", ("✅ To'g'ri variant", "✅ Правильный вариант", "✅ The right option"),
            p=("<b>3 soniya eslab turadi.</b> Qahramon ko'rinmay qolganda dushman yana "
               "3 soniya o'sha tomonga yuradi, keyin \"hm, yo'qoldi\" deb patrulga qaytadi. "
               "Mana bu <b>tirik</b> tuyuladi.",
               "<b>Помнит 3 секунды.</b> Когда герой исчез, враг ещё 3 секунды идёт в ту "
               "сторону, а потом «хм, пропал» — и возвращается к патрулю. "
               "Вот это ощущается <b>живым</b>.",
               "<b>It remembers for 3 seconds.</b> Once the hero is gone the enemy keeps "
               "going that way for 3 more seconds, then \"hm, lost him\" and patrols again. "
               "This feels <b>alive</b>.")),
    ]) + "\n</div>\n"
         + box("purple", ("🎛 \"Xotira\" slayderi", "🎛 Слайдер «Память»", "🎛 The \"Memory\" slider"),
               p=("0 soniya → aqlsiz dushman. 10 soniya → shafqatsiz dushman. "
                  "Eng qiziqarli qiymatni o'zingiz toping va varaqaga yozib qo'ying.",
                  "0 секунд → глупый враг. 10 секунд → беспощадный враг. "
                  "Найдите самое интересное значение сами и запишите его в рабочий лист.",
                  "0 seconds → a dumb enemy. 10 seconds → a merciless one. "
                  "Find the most fun value yourself and write it on your worksheet.")),
))

S.append(slide(
    ph=("Adolat", "Честность", "Fairness"), time="26–29",
    eyebrow=("O'yin dizayni qoidasi", "Правило геймдизайна", "Game design rule"),
    title=("Yaxshi dushman — kuchli emas, <b>adolatli</b> dushman",
           "Хороший враг — не сильный, а <b>честный</b>",
           "A good enemy is not strong — it is <b>fair</b>"),
    body='<div class="cols c2">\n'
         + box("green", ("3 ta oltin qoida", "3 золотых правила", "3 golden rules"),
               items=[
                   ("<b>Dushman qahramondan sekinroq bo'lsin.</b> Aks holda qochishning "
                    "iloji yo'q va o'yinchi taslim bo'ladi.",
                    "<b>Враг должен быть медленнее героя.</b> Иначе убежать невозможно "
                    "и игрок сдаётся.",
                    "<b>The enemy must be slower than the hero.</b> Otherwise escape is "
                    "impossible and the player quits."),
                   ("<b>Ogohlantirish belgisi shart.</b> ❓ va ❗ — o'yinchiga \"tayyorlan!\" "
                    "degan signal. Belgisiz hujum aldov hisoblanadi.",
                    "<b>Значок предупреждения обязателен.</b> ❓ и ❗ — сигнал игроку "
                    "«приготовься!». Атака без значка воспринимается как обман.",
                    "<b>A warning icon is required.</b> ❓ and ❗ tell the player to get ready. "
                    "An attack with no warning reads as cheating."),
                   ("<b>Reaksiya kechikishi 0.5 soniya.</b> Dushman sizni ko'rgan zahoti "
                    "otilmaydi — bir lahza o'ylaydi. Shu lahza o'yinni halol qiladi.",
                    "<b>Задержка реакции 0.5 секунды.</b> Враг не бросается сразу — "
                    "секунду думает. Эта пауза делает игру честной.",
                    "<b>A 0.5s reaction delay.</b> The enemy does not pounce instantly — "
                    "it thinks for a beat. That beat keeps the game honest."),
               ])
         + "\n"
         + box("accent", ("Sinovda tekshiring", "Проверьте на тесте", "Check it in testing"),
               p=("Stendda <b>Dushman tezligi</b> slayderini qahramon tezligidan yuqoriga "
                  "ko'taring va 30 soniya o'ynab ko'ring. His qilasiz: o'yin darhol "
                  "yoqimsiz bo'lib qoladi. Keyin pastga tushiring — qiziqish qaytadi. "
                  "Mana shu <b>o'yin dizayneri</b> ishi.",
                  "Поднимите на стенде слайдер <b>Скорость врага</b> выше скорости героя "
                  "и поиграйте 30 секунд. Вы почувствуете: играть сразу становится "
                  "неприятно. Потом опустите обратно — интерес вернётся. "
                  "Вот это и есть работа <b>геймдизайнера</b>.",
                  "Push the <b>Enemy speed</b> slider above the hero's speed and play for "
                  "30 seconds. You will feel the game turn unpleasant at once. "
                  "Drop it back and the fun returns. "
                  "That is the <b>game designer's</b> job."))
         + "\n</div>",
))

S.append(slide(
    ph=("Amaliyot", "Практика", "Practice"), time="29–40",
    eyebrow=("Laboratoriya · 11 daqiqa", "Лаборатория · 11 минут", "Lab · 11 minutes"),
    title=("4 ta sinov: game/index.html ni oching",
           "4 испытания: откройте game/index.html",
           "4 trials: open game/index.html"),
    body='<div class="cols c4">\n' + "\n".join([
        box("", ("1-sinov · Orqadan o'tish", "Тест 1 · Пройти сзади", "Trial 1 · Sneak behind"),
            p=("Dushman teskari tomonga qaragan paytni poylang va orqasidan sekin o'ting. "
               "Muvaffaqiyat bo'lsa — varaqaga ✔ qo'ying.",
               "Дождитесь, когда враг отвернётся, и тихо пройдите сзади. "
               "Получилось — ставьте ✔ в рабочем листе.",
               "Wait until the enemy looks away and slip behind it. "
               "Tick ✔ on the worksheet if it works.")),
        box("purple", ("2-sinov · Devor ortida", "Тест 2 · За стеной", "Trial 2 · Behind the wall"),
            p=("\"Devor\" tugmasini yoqing. Ustun ortida turib, dushmanning konusi qanday "
               "kesilishini kuzating. Radiusni o'lchab yozing.",
               "Включите кнопку «Стена». Встаньте за столбом и посмотрите, как обрезается "
               "конус врага. Измерьте и запишите радиус.",
               "Switch the \"Wall\" button on. Stand behind the post and watch the cone get "
               "cut. Measure and note the radius.")),
        box("accent", ("3-sinov · Xotira sinovi", "Тест 3 · Проверка памяти", "Trial 3 · Memory test"),
            p=("Dushmanni ta'qibga qo'zg'ating, keyin yashirining. Necha soniyadan keyin "
               "u patrulga qaytdi? Sekundomer bilan o'lchang.",
               "Спровоцируйте погоню, затем спрячьтесь. Через сколько секунд он вернулся "
               "к патрулю? Замерьте секундомером.",
               "Trigger the chase, then hide. How many seconds until it patrols again? "
               "Time it with a stopwatch.")),
        box("green", ("4-sinov · Adolat sozlamasi", "Тест 4 · Настройка честности", "Trial 4 · Tune fairness"),
            p=("Uchta slayderni shunday sozlangki, o'yin <b>qiyin, lekin halol</b> bo'lsin. "
               "Uchta raqamni varaqaga ko'chiring — bu sizning shaxsiy retseptingiz.",
               "Настройте три слайдера так, чтобы игра была <b>сложной, но честной</b>. "
               "Перепишите три числа в рабочий лист — это ваш личный рецепт.",
               "Tune the three sliders so the game is <b>hard but fair</b>. "
               "Copy the three numbers onto your worksheet — that is your own recipe.")),
    ]) + "\n</div>",
))

S.append(slide(
    ph=("AI yordamchi", "AI помощник", "AI helper"), time="40–43",
    eyebrow=("Tayyor promptlar", "Готовые промпты", "Ready-made prompts"),
    title=("AI dan dushmaningizni yaxshilashni so'rang",
           "Попросите AI улучшить вашего врага",
           "Ask the AI to improve your enemy"),
    body='<div class="cols c2">\n'
         + box("purple", ("Nusxa oling va ChatGPT/Claude ga tashlang",
                          "Скопируйте и отправьте в ChatGPT/Claude",
                          "Copy and paste into ChatGPT/Claude"),
               extra_html=code(
                   "1) У меня 2D-игра на JavaScript. Враг патрулирует\n"
                   "   между двумя точками. Подскажи, какую скорость\n"
                   "   врага поставить, если скорость героя = 4,\n"
                   "   чтобы игра была сложной, но честной?\n\n"
                   "2) Добавь врагу состояние \"ПОДОЗРЕНИЕ\": он\n"
                   "   останавливается на 0.5 сек и показывает знак ?\n"
                   "   перед тем, как начать погоню.\n\n"
                   "3) Объясни простыми словами, что такое\n"
                   "   Line of Sight в играх, для ученика 6 класса."))
         + "\n"
         + box("accent", ("⚠️ Muhim qoida", "⚠️ Важное правило", "⚠️ Important rule"),
               items=[
                   ("AI bergan raqamni <b>ko'r-ko'rona ishonmang</b> — slayderga qo'yib, "
                    "o'zingiz o'ynab tekshiring.",
                    "<b>Не верьте вслепую</b> числу от AI — поставьте его на слайдер "
                    "и проверьте игрой.",
                    "<b>Never trust the AI's number blindly</b> — put it on the slider "
                    "and test it by playing."),
                   ("AI o'yinni siz uchun o'ynab bermaydi. <b>Qiziqarlimi yoki yo'qmi</b> — "
                    "buni faqat inson hal qiladi.",
                    "AI не сыграет за вас. <b>Весело или нет</b> — это решает только человек.",
                    "The AI cannot play for you. <b>Fun or not fun</b> is a human call."),
                   ("Javobni tushunmadingizmi? \"Объясни проще, я в 6 классе\" deb yozing.",
                    "Не поняли ответ? Напишите: «Объясни проще, я в 6 классе».",
                    "Did not understand the answer? Write \"Explain it simpler, I am in grade 6\"."),
               ])
         + "\n</div>",
))

S.append(slide(
    ph=("Yakun", "Итоги", "Summary"), time="43–45",
    eyebrow=("Uy vazifasi va baholash", "Домашнее задание и оценка", "Homework and grading"),
    title=("Uy vazifasi: o'z dushmaningizni loyihalang (10 ball)",
           "Домашнее задание: спроектируйте своего врага (10 баллов)",
           "Homework: design your own enemy (10 points)"),
    body='<div class="cols c2">\n'
         + box("green", ("Nima qilish kerak", "Что нужно сделать", "What to do"),
               items=[
                   ("Varaqadagi jadvalni to'ldiring: 4 sinovning natijalari.",
                    "Заполните таблицу в рабочем листе: результаты 4 испытаний.",
                    "Fill the worksheet table: results of all 4 trials."),
                   ("O'z dushmaningizni <b>chizing</b> va 3 kayfiyatini yozing: "
                    "patrulda nima qiladi, sezganda nima qiladi, quvganda nima qiladi.",
                    "<b>Нарисуйте</b> своего врага и опишите 3 настроения: что делает "
                    "в патруле, что при обнаружении, что в погоне.",
                    "<b>Draw</b> your own enemy and write its 3 moods: what it does on patrol, "
                    "when alerted, and while chasing."),
                   ("Uchta slayder qiymatini yozing va <b>nega shunday</b> tanlaganingizni "
                    "bir gap bilan tushuntiring.",
                    "Запишите три значения слайдеров и одним предложением объясните, "
                    "<b>почему</b> выбрали именно их.",
                    "Write your three slider values and explain in one sentence <b>why</b> "
                    "you chose them."),
               ])
         + "\n"
         + box("accent", ("Baholash mezoni", "Критерии оценки", "Grading rubric"),
               extra_html='<ul class="plain">\n'
               + '  <li><span class="t" %s>4 sinov jadvali to\'ldirilgan — <b>4 ball</b></span></li>\n'
               % i18n("4 sinov jadvali to'ldirilgan — <b>4 ball</b>",
                      "Таблица 4 испытаний заполнена — <b>4 балла</b>",
                      "Table of 4 trials completed — <b>4 points</b>")
               + '  <li><span class="t" %s>Dushman chizmasi va 3 kayfiyati — <b>3 ball</b></span></li>\n'
               % i18n("Dushman chizmasi va 3 kayfiyati — <b>3 ball</b>",
                      "Рисунок врага и 3 настроения — <b>3 балла</b>",
                      "Enemy drawing and its 3 moods — <b>3 points</b>")
               + '  <li><span class="t" %s>Slayder qiymatlari va izoh — <b>2 ball</b></span></li>\n'
               % i18n("Slayder qiymatlari va izoh — <b>2 ball</b>",
                      "Значения слайдеров и объяснение — <b>2 балла</b>",
                      "Slider values and reasoning — <b>2 points</b>")
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
         "Salom, muhandislar! O'tgan darsda biz trassaga tikan, lazer va 3 ta jon qo'shdik. Lekin bir narsa yetishmayapti — trassa hali ham tirik emas. Bugun biz unga o'ylaydigan dushman qo'yamiz.",
         "Titul slaydni ochish. game/index.html ni proyektorda oldindan ochib qo'ying."],
        ["Nega o'yin zerikarli",
         "Bolalardan so'rang: qaysi o'yinni 100 marta o'ynagansiz va zerikmagansiz? Nega? Javob deyarli har doim bitta — chunki har safar boshqacha bo'ladi. Boshqacha qiladigan narsa esa — dushman.",
         "3 ta ustunni birma-bir ko'rsatish. O'quvchilardan misol so'rash."],
        ["Dushmanning 3 kayfiyati",
         "Eng muhim slayd. Dushmanning miyasi — sehr emas, uchta kayfiyat. Proyektorda stendni oching va dushmanning boshidagi belgi qanday o'zgarishini jonli ko'rsating: belgisiz → ❓ → ❗.",
         "Stendda jonli demo. Belgilar almashuvini 2-3 marta takrorlang."],
        ["Patrul qoidasi",
         "Patrul — bu ikki ustun orasidagi yurish. Kodni o'qishga majburlamang, faqat mantiqni ayting: chegaraga yetdi — burildi. Patrul kengligi slayderini surib ko'rsating.",
         "Slayderni tor va keng holatga surib farqni ko'rsatish."],
        ["Ko'rish radiusi",
         "Ikkita savol: yaqinmi va shu tomondami. Ikkinchisi muhimroq — dushmanning orqa ko'zi yo'q. Bitta o'quvchini doskaga chaqirib, orqasiga o'ting va 'meni ko'ryapsizmi?' deb so'rang. Bolalar darhol tushunadi.",
         "Sinfda jonli ko'rgazma: o'quvchining orqasiga o'tish."],
        ["Devor va Line of Sight",
         "Agar dushman devor orqali ko'raversa, yashirinishning ma'nosi qolmaydi. Stendda 'Devor' tugmasini yoqib, konus devorda kesilishini ko'rsating.",
         "Devor tugmasini yoqib-o'chirib ko'rsatish."],
        ["Ta'qib mantig'i",
         "Butun ta'qib — to'rt qator kod. Bolalarga ayting: siz o'ylagan murakkab 'sun'iy intellekt' aslida oddiy taqqoslash. Aqlli tuyulishi esa ko'rish radiusi va kechikish hisobiga.",
         "Kod blokini ko'rsatish, lekin yodlashni talab qilmaslik."],
        ["Xotira va unutish",
         "Uchta variantni solishtiring. Bolalardan so'rang: qaysi biri qiziqarli? Deyarli hamma uchinchisini tanlaydi. Demak, ular o'yin dizayneri kabi fikrlay boshladi.",
         "Xotira slayderini 0, 3 va 10 ga qo'yib sinab ko'rsatish."],
        ["Adolat qoidalari",
         "Eng muhim pedagogik nuqta: kuchli dushman yomon dushman. Stendda dushman tezligini qahramondan oshirib qo'ying va 20 soniya o'ynang — bolalar darhol norozi bo'ladi. Mana shu tuyg'u — dizayn darsi.",
         "Tezlikni oshirib jonli sinash, keyin qaytarish."],
        ["Amaliyot 11 daqiqa",
         "Endi noutbuklar. Har bir o'quvchi game/index.html ni ochadi va 4 sinovni bajaradi. Siz sinf bo'ylab yurib, faqat qotib qolganlarga yordam bering. Javobni aytmang — savol bering.",
         "Vaqtni nazorat qiling: har sinovga ~2.5 daqiqa. Varaqani to'ldirishni eslating."],
        ["AI bilan ishlash",
         "Tayyor promptlarni nusxa olishsin. Eng muhimi — oxirgi qoida: AI bergan raqamni tekshirmasdan ishlatmaslik. Bu darsdan chiqadigan eng katta hayotiy saboq.",
         "Bitta o'quvchining ekranida AI javobini birga tahlil qilish."],
        ["Yakun va baholash",
         "Darsni xulosalang: dushman aqlli emas, u uchta qoidadan iborat. Varaqalarni yig'ing. Uy vazifasini 10 ballik mezon bilan e'lon qiling.",
         "Varaqalarni yig'ish. Keyingi dars — o'z levelingizni qurish — haqida qiziqtirish."],
    ],
    "ru": [
        ["Титульный слайд",
         "Привет, инженеры! На прошлом уроке мы добавили на трассу шипы, лазер и 3 жизни. Но кое-чего не хватает — трасса всё ещё неживая. Сегодня мы поставим на неё думающего врага.",
         "Открыть титульный слайд. Заранее откройте game/index.html на проекторе."],
        ["Почему игра скучная",
         "Спросите ребят: в какую игру вы играли 100 раз и не надоело? Почему? Ответ почти всегда один — потому что каждый раз по-разному. А по-разному делает именно враг.",
         "Показать 3 колонки по очереди. Попросить примеры у учеников."],
        ["Три настроения врага",
         "Самый важный слайд. Мозг врага — не магия, а три настроения. Откройте стенд на проекторе и живьём покажите, как меняется значок над врагом: пусто → ❓ → ❗.",
         "Живое демо на стенде. Повторите смену значков 2-3 раза."],
        ["Правило патруля",
         "Патруль — это ходьба между двумя столбами. Не заставляйте читать код, скажите только логику: дошёл до границы — развернулся. Подвигайте слайдер ширины патруля.",
         "Показать разницу, двигая слайдер в узкое и широкое положение."],
        ["Радиус зрения",
         "Два вопроса: близко ли и в ту ли сторону. Второй важнее — у врага нет глаз на затылке. Вызовите ученика к доске, зайдите ему за спину и спросите: «ты меня видишь?». Дети поймут мгновенно.",
         "Живая демонстрация в классе: зайти ученику за спину."],
        ["Стена и Line of Sight",
         "Если враг видит сквозь стену, прятаться бессмысленно. Включите на стенде кнопку «Стена» и покажите, как конус обрезается о столб.",
         "Включить и выключить кнопку стены."],
        ["Логика погони",
         "Вся погоня — четыре строки кода. Скажите детям: тот сложный «искусственный интеллект», который вы представляли, на деле — простое сравнение. А умным враг кажется из-за радиуса зрения и задержки.",
         "Показать блок кода, но не требовать заучивания."],
        ["Память и забывание",
         "Сравните три варианта. Спросите: какой интереснее? Почти все выберут третий. Значит, они уже начали думать как геймдизайнеры.",
         "Поставить слайдер памяти на 0, 3 и 10 и дать попробовать."],
        ["Правила честности",
         "Главная педагогическая точка: сильный враг — плохой враг. Поднимите на стенде скорость врага выше героя и поиграйте 20 секунд — дети сразу возмутятся. Вот это чувство и есть урок дизайна.",
         "Поднять скорость, дать почувствовать, вернуть обратно."],
        ["Практика 11 минут",
         "Теперь ноутбуки. Каждый открывает game/index.html и проходит 4 испытания. Вы ходите по классу и помогаете только застрявшим. Не давайте ответ — задавайте вопрос.",
         "Следите за временем: ~2.5 минуты на испытание. Напоминайте про рабочий лист."],
        ["Работа с AI",
         "Пусть скопируют готовые промпты. Самое важное — последнее правило: не использовать число от AI без проверки. Это главный жизненный урок сегодняшнего занятия.",
         "Разобрать ответ AI на экране одного из учеников."],
        ["Итоги и оценивание",
         "Подведите итог: враг не умный, он состоит из трёх правил. Соберите рабочие листы. Объявите домашнее задание по 10-балльным критериям.",
         "Собрать листы. Заинтриговать следующим уроком — постройте свой уровень."],
    ],
    "en": [
        ["Title slide",
         "Hello engineers! Last lesson we added spikes, a laser and 3 lives. But something is missing — the track still is not alive. Today we add a thinking enemy.",
         "Open the title slide. Pre-open game/index.html on the projector."],
        ["Why games get boring",
         "Ask the class: which game did you play 100 times without getting bored? Why? The answer is almost always the same — because it plays differently each time. And what makes it different is the enemy.",
         "Walk through the 3 columns. Ask students for examples."],
        ["The enemy's three moods",
         "The key slide. The enemy's brain is not magic — it is three moods. Open the lab on the projector and show the icon above the enemy changing live: none → ❓ → ❗.",
         "Live demo on the lab. Repeat the icon switch 2-3 times."],
        ["The patrol rule",
         "Patrol is walking between two posts. Do not make them read code — just state the logic: hit an edge, flip around. Drag the patrol width slider.",
         "Show the difference with narrow and wide slider positions."],
        ["Vision radius",
         "Two questions: is it near, and is it in front. The second matters more — the enemy has no eyes in the back of its head. Call a student to the board, step behind them and ask 'can you see me?'. They get it instantly.",
         "Live classroom demo: step behind a student."],
        ["Walls and Line of Sight",
         "If the enemy sees through walls, hiding is pointless. Turn on the 'Wall' button and show the cone being cut by the post.",
         "Toggle the wall button on and off."],
        ["Chase logic",
         "The whole chase is four lines of code. Tell them: the complex 'artificial intelligence' you imagined is really a simple comparison. The smart feel comes from vision radius and delay.",
         "Show the code block but do not require memorisation."],
        ["Memory and forgetting",
         "Compare the three options. Ask which is more fun. Almost everyone picks the third. That means they are already thinking like game designers.",
         "Set the memory slider to 0, 3 and 10 and let them feel it."],
        ["Fairness rules",
         "The core teaching moment: a strong enemy is a bad enemy. Raise the enemy speed above the hero's and play for 20 seconds — the class will protest immediately. That feeling is the design lesson.",
         "Raise the speed, let them feel it, then restore it."],
        ["Practice, 11 minutes",
         "Laptops now. Everyone opens game/index.html and runs the 4 trials. Walk the room and help only those who are stuck. Do not give answers — ask questions.",
         "Watch the clock: ~2.5 minutes per trial. Remind them to fill the worksheet."],
        ["Working with AI",
         "Let them copy the ready prompts. The key point is the last rule: never use a number from the AI without testing it. That is the biggest life lesson of today.",
         "Analyse one student's AI answer together on screen."],
        ["Summary and grading",
         "Wrap up: the enemy is not smart, it is three rules. Collect the worksheets. Announce the homework with the 10-point rubric.",
         "Collect sheets. Tease the next lesson — build your own level."],
    ],
}


# ---------------------------------------------------------------- varaqa

from build import sheet_header, mission, table, sheet_box, rubric, writelines, sign_box

VARAQA = (
    sheet_header(
        ("15-dars: Dushman AI — Patrul, Ko'rish va Ta'qib",
         "Урок 15: ИИ Врага — Патруль, Зрение и Погоня",
         "Lesson 15: Enemy AI — Patrol, Vision and Chase"),
        ("Target International School · 5–6-sinf · 4-hafta (1-soat)",
         "Target International School · 5–6 класс · 4-я неделя (1-й час)",
         "Target International School · Grades 5–6 · Week 4 (Hour 1)"))
    + mission(
        ("🎯 Missiya: dushmanning miyasini sozlang",
         "🎯 Миссия: настройте мозг врага",
         "🎯 Mission: tune the enemy's brain"),
        ("<b>game/index.html</b> ni oching. Dushmanda 3 ta kayfiyat bor: "
         "😴 PATRUL → ❓ SEZDI → ❗ TA'QIB. 4 ta sinovni bajaring, natijalarni "
         "jadvalga yozing va oxirida o'z dushmaningizni loyihalang.",
         "Откройте <b>game/index.html</b>. У врага 3 настроения: "
         "😴 ПАТРУЛЬ → ❓ ЗАМЕТИЛ → ❗ ПОГОНЯ. Пройдите 4 испытания, запишите "
         "результаты в таблицу и в конце спроектируйте своего врага.",
         "Open <b>game/index.html</b>. The enemy has 3 moods: "
         "😴 PATROL → ❓ ALERTED → ❗ CHASE. Run the 4 trials, log the results "
         "in the table, then design your own enemy."))
    + table(
        [("Sinov", "Испытание", "Trial"),
         ("Nima qilasiz", "Что делаете", "What you do"),
         ("Natija / o'lchov", "Результат / замер", "Result / measurement"),
         ("✔", "✔", "✔")],
        [[("1 · Orqadan", "1 · Сзади", "1 · Behind"),
          ("Dushman teskari qaragan payt orqasidan o'ting",
           "Пройдите сзади, когда враг отвернулся",
           "Slip behind while the enemy faces away"),
          ("Nechanchi urinishda muvaffaqiyat? ____",
           "С какой попытки получилось? ____",
           "Which attempt worked? ____"), None],
         [("2 · Devor", "2 · Стена", "2 · Wall"),
          ("\"Devor\" tugmasini yoqing, ustun ortida turing",
           "Включите «Стену», встаньте за столбом",
           "Turn on \"Wall\", stand behind the post"),
          ("Konus devorda kesildimi? HA / YO'Q",
           "Конус обрезался о стену? ДА / НЕТ",
           "Was the cone cut by the wall? YES / NO"), None],
         [("3 · Xotira", "3 · Память", "3 · Memory"),
          ("Ta'qibni boshlating, keyin yashiring va sanang",
           "Спровоцируйте погоню, спрячьтесь и считайте",
           "Trigger a chase, hide and count"),
          ("Necha soniyada patrulga qaytdi? ____ sek",
           "Через сколько вернулся к патрулю? ____ сек",
           "Seconds until it patrolled again? ____ s"), None],
         [("4 · Adolat", "4 · Честность", "4 · Fairness"),
          ("Slayderlarni \"qiyin, lekin halol\" holatga sozlang",
           "Настройте слайдеры на «сложно, но честно»",
           "Tune the sliders to \"hard but fair\""),
          ("Tezlik ___ · Radius ___ · Xotira ___",
           "Скорость ___ · Радиус ___ · Память ___",
           "Speed ___ · Radius ___ · Memory ___"), None]])
    + '    <div class="rubric-grid">\n'
    + sheet_box(
        ("✏️ Uy vazifasi: o'z dushmaningiz",
         "✏️ Домашнее задание: свой враг",
         "✏️ Homework: your own enemy"),
        '      ' + el("p", *(
            "Dushmaningizni pastdagi katakka chizing va uchta kayfiyatini yozing.",
            "Нарисуйте врага в рамке ниже и опишите три его настроения.",
            "Draw your enemy in the frame below and describe its three moods."),
            extra='style="font-size:7.6pt; margin:0 0 4px"')
        + '\n      <div style="border:1px dashed var(--rule); height:26mm; border-radius:3px;"></div>\n'
        + writelines(3, ("😴 Patrulda / ❓ Sezganda / ❗ Ta'qibda nima qiladi:",
                         "😴 В патруле / ❓ При обнаружении / ❗ В погоне:",
                         "😴 On patrol / ❓ When alerted / ❗ While chasing:")))
    + "\n"
    + sheet_box(
        ("📊 Baholash mezoni (10 ball)",
         "📊 Критерии оценки (10 баллов)",
         "📊 Grading rubric (10 points)"),
        rubric([
            (("4 sinov jadvali to'ldirilgan", "Таблица 4 испытаний заполнена",
              "Table of 4 trials completed"), "4"),
            (("Dushman chizmasi va 3 kayfiyat", "Рисунок врага и 3 настроения",
              "Enemy drawing and 3 moods"), "3"),
            (("Slayder qiymatlari va izoh", "Значения слайдеров и объяснение",
              "Slider values and reasoning"), "2"),
            (("Ozodalik va tartib", "Аккуратность и порядок", "Neatness and order"), "1"),
        ], "10"))
    + "\n    </div>\n  </div>\n"
    + sign_box()
)

if __name__ == "__main__":
    print(Lesson(D, TITLES, SHEET_TITLES, "vc-notes-5-15", S, NOTES, VARAQA).build())
