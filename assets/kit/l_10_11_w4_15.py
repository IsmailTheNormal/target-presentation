# -*- coding: utf-8 -*-
"""10-11-sinf · 4-hafta · 15-dars — RAG va Embeddinglar: Chunking, Vektor Qidiruv, Kosinus."""

import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from build import (Lesson, slide, title_slide, box, code, el, i18n,
                   sheet_header, mission, table, sheet_box, rubric, writelines, sign_box)

D = "classes/10-11-sinf/4-hafta/15-dars-rag-va-embeddinglar"

TITLES = {
    "uz": "15-dars: RAG va Embeddinglar — Chunking, Vektor Qidiruv va Kosinus O'xshashlik",
    "ru": "Урок 15: RAG и Эмбеддинги — Чанкинг, Векторный Поиск и Косинусная Близость",
    "en": "Lesson 15: RAG and Embeddings — Chunking, Vector Search and Cosine Similarity",
}
SHEET_TITLES = {k: v + (" — Ish Varaqasi" if k == "uz" else
                        " — Рабочий Лист" if k == "ru" else " — Worksheet")
                for k, v in TITLES.items()}

S = []

S.append(title_slide(
    ph=("Kirish", "Введение", "Intro"), time="0–3",
    eyebrow=("Vibecoding · 15-dars · 10–11-sinflar (Senior)",
             "Vibecoding · Урок 15 · 10–11 классы (Senior)",
             "Vibecoding · Lesson 15 · Grades 10–11 (Senior)"),
    h1=("RAG va Embeddinglar: Modelga O'z Bilimingizni Berish",
        "RAG и Эмбеддинги: Как Дать Модели Ваши Собственные Знания",
        "RAG and Embeddings: Giving a Model Your Own Knowledge"),
    lede=("13-darsda biz modelning ichki tuzilishini (kontekst oynasi, sampling, "
          "system prompt) o'rgandik, 14-darsda unga <b>qo'l</b> berdik (Tool Calling). "
          "Lekin bitta jiddiy muammo qoldi: model <b>sizning</b> hujjatlaringizni, "
          "maktabingiz qoidalarini yoki kompaniyangiz bazasini bilmaydi. "
          "Bugun biz eng keng tarqalgan sanoat yechimini quramiz — <b>RAG</b> "
          "(Retrieval-Augmented Generation) va uning yuragi bo'lgan <b>vektor "
          "qidiruvni</b> matematikasi bilan ochamiz.",
          "На уроке 13 мы разобрали внутреннее устройство модели (контекстное окно, "
          "сэмплинг, system prompt), на уроке 14 дали ей <b>руки</b> (Tool Calling). "
          "Но осталась серьёзная проблема: модель не знает <b>ваших</b> документов, "
          "правил вашей школы или базы вашей компании. "
          "Сегодня мы построим самое распространённое индустриальное решение — "
          "<b>RAG</b> (Retrieval-Augmented Generation) — и вскроем его сердце, "
          "<b>векторный поиск</b>, вместе с математикой.",
          "In lesson 13 we opened the model's internals (context window, sampling, "
          "system prompt); in lesson 14 we gave it <b>hands</b> (Tool Calling). "
          "But a serious problem remains: the model does not know <b>your</b> documents, "
          "your school's rules or your company's database. "
          "Today we build the dominant industry solution — <b>RAG</b> "
          "(Retrieval-Augmented Generation) — and open up its heart, "
          "<b>vector search</b>, mathematics included."),
    meta=[("<b>Fan:</b> AI Engineering · Axborot qidiruvi",
           "<b>Предмет:</b> AI Engineering · Информационный поиск",
           "<b>Subject:</b> AI Engineering · Information Retrieval"),
          ("<b>Kohorta:</b> Senior 10–11", "<b>Когорта:</b> Senior 10–11",
           "<b>Cohort:</b> Senior 10–11"),
          ("<b>Hafta:</b> 4 (1-soat)", "<b>Неделя:</b> 4 (1-й час)", "<b>Week:</b> 4 (Hour 1)")],
))

S.append(slide(
    ph=("Muammo", "Проблема", "Problem"), time="3–7",
    eyebrow=("Nega yolg'iz LLM yetarli emas", "Почему одной LLM недостаточно",
             "Why an LLM alone is not enough"),
    title=("Uchta chegara: bilim kesimi, gallyutsinatsiya, kontekst narxi",
           "Три предела: отсечка знаний, галлюцинации, цена контекста",
           "Three limits: knowledge cutoff, hallucination, context cost"),
    body='<div class="cols c3">\n' + "\n".join([
        box("accent", ("1 · Knowledge cutoff", "1 · Knowledge cutoff", "1 · Knowledge cutoff"),
            p=("Model o'qitilgan sanadan keyingi hech narsani bilmaydi. Sizning "
               "kechagi hujjatingiz, bugungi narx ro'yxatingiz — u uchun mavjud emas. "
               "Va u <b>mavjud emasligini ham bilmaydi</b>.",
               "Модель не знает ничего после даты обучения. Ваш вчерашний документ, "
               "сегодняшний прайс — для неё не существуют. И она <b>не знает, что они "
               "не существуют</b>.",
               "The model knows nothing after its training date. Your document from "
               "yesterday, today's price list — they do not exist for it. And it "
               "<b>does not know that they do not exist</b>.")),
        box("purple", ("2 · Gallyutsinatsiya", "2 · Галлюцинации", "2 · Hallucination"),
            p=("LLM — keyingi tokenning ehtimolini hisoblovchi model. Agar fakt yo'q "
               "bo'lsa, u <b>bo'shliq qoldirmaydi</b> — eng ehtimolli matnni "
               "generatsiya qiladi. Natija ishonchli ko'rinadi va noto'g'ri bo'ladi.",
               "LLM — модель вероятности следующего токена. Если факта нет, она "
               "<b>не оставит пустоту</b> — сгенерирует наиболее вероятный текст. "
               "Результат выглядит уверенно и оказывается неверным.",
               "An LLM computes next-token probability. With no fact available it "
               "<b>will not leave a gap</b> — it generates the most probable text. "
               "The result looks confident and is wrong.")),
        box("green", ("3 · Kontekst narxi", "3 · Цена контекста", "3 · Context cost"),
            p=("\"Hamma hujjatni promptga solaylik\" ishlamaydi: kontekst oynasi "
               "cheklangan, har token pul turadi va uzun kontekstda model "
               "<b>o'rtadagi ma'lumotni yo'qotadi</b> (lost in the middle).",
               "«Засунем все документы в промпт» не работает: окно ограничено, каждый "
               "токен стоит денег, а в длинном контексте модель <b>теряет информацию "
               "из середины</b> (lost in the middle).",
               "\"Just paste all the documents\" does not work: the window is limited, "
               "every token costs money, and in a long context the model "
               "<b>loses what is in the middle</b> (lost in the middle).")),
    ]) + "\n</div>\n"
         + box("", ("Muhandislik xulosasi", "Инженерный вывод", "The engineering conclusion"),
               p=("Bizga kerak: <b>so'rov paytida</b>, <b>faqat kerakli</b> parchalarni "
                  "topib, ularni promptga qo'shadigan tizim. Model o'sha parchalarga "
                  "tayanib javob beradi — bu <b>grounding</b> deb ataladi. "
                  "Aynan shu — RAG.",
                  "Нам нужна система, которая <b>во время запроса</b> находит "
                  "<b>только нужные</b> фрагменты и добавляет их в промпт. Модель "
                  "отвечает, опираясь на них — это называется <b>grounding</b>. "
                  "Это и есть RAG.",
                  "We need a system that, <b>at query time</b>, finds <b>only the "
                  "relevant</b> fragments and injects them into the prompt. The model "
                  "answers grounded in those fragments — this is called <b>grounding</b>. "
                  "That is RAG.")),
))

S.append(slide(
    ph=("Tanlov", "Выбор", "The choice"), time="7–11",
    eyebrow=("Fine-tuning yoki RAG", "Fine-tuning или RAG", "Fine-tuning or RAG"),
    title=("Modelni qayta o'qitish emas — unga kutubxona berish",
           "Не переобучать модель, а дать ей библиотеку",
           "Do not retrain the model — give it a library"),
    body='<div class="cols c2">\n'
         + box("purple", ("Fine-tuning (qayta o'qitish)", "Fine-tuning (дообучение)",
                          "Fine-tuning"),
               items=[
                   ("Bilim model <b>vaznlariga</b> yoziladi. Yangilash uchun qaytadan "
                    "o'qitish kerak — soatlar va pul.",
                    "Знание записывается в <b>веса</b> модели. Для обновления нужно "
                    "переобучение — часы и деньги.",
                    "Knowledge is written into the model's <b>weights</b>. Updating "
                    "means retraining — hours and money."),
                   ("Manbani ko'rsatib bo'lmaydi: model <b>nega</b> shunday javob "
                    "berganini isbotlay olmaydi.",
                    "Источник не показать: модель не может доказать, <b>почему</b> "
                    "ответила именно так.",
                    "No citations possible: the model cannot prove <b>why</b> it "
                    "answered that way."),
                   ("Yaxshi ishlaydigan joyi: <b>uslub</b>, format, domen tili. "
                    "Faktlar uchun emas.",
                    "Где работает хорошо: <b>стиль</b>, формат, язык домена. "
                    "Не для фактов.",
                    "Where it shines: <b>style</b>, format, domain language. "
                    "Not for facts."),
               ])
         + "\n"
         + box("green", ("RAG (qidiruv bilan kengaytirish)", "RAG (поиск + генерация)",
                         "RAG (retrieval-augmented)"),
               items=[
                   ("Bilim <b>tashqi bazada</b>. Hujjatni yangiladingiz — tizim "
                    "darhol yangi javob beradi. Qayta o'qitish yo'q.",
                    "Знание — <b>во внешней базе</b>. Обновили документ — система сразу "
                    "отвечает по-новому. Переобучения нет.",
                    "Knowledge lives in an <b>external store</b>. Update a document and "
                    "the system answers differently at once. No retraining."),
                   ("<b>Manba ko'rsatiladi:</b> javob ostida \"3-hujjat, 2-bo'lim\". "
                    "Tekshirish mumkin.",
                    "<b>Источник показывается:</b> под ответом «документ 3, раздел 2». "
                    "Можно проверить.",
                    "<b>Sources are shown:</b> \"document 3, section 2\" under the "
                    "answer. Verifiable."),
                   ("Kirish huquqini boshqarish mumkin: har foydalanuvchi faqat "
                    "o'ziga ruxsat etilgan hujjatlarni ko'radi.",
                    "Можно управлять доступом: каждый пользователь видит только "
                    "разрешённые ему документы.",
                    "Access control is possible: each user sees only the documents "
                    "they are allowed to."),
                   ("Kamchiligi: <b>qidiruv sifati</b> butun tizim sifatini belgilaydi.",
                    "Недостаток: <b>качество поиска</b> определяет качество всей системы.",
                    "The catch: <b>retrieval quality</b> caps the quality of the "
                    "whole system."),
               ])
         + "\n</div>",
))

S.append(slide(
    ph=("Arxitektura", "Архитектура", "Architecture"), time="11–16",
    eyebrow=("Ikki bosqich", "Два этапа", "Two phases"),
    title=("RAG ikki mustaqil bosqichdan iborat — ularni chalkashtirmang",
           "RAG состоит из двух независимых этапов — не путайте их",
           "RAG has two independent phases — do not confuse them"),
    body='<div class="cols c2">\n'
         + box("purple", ("A · Indekslash (oldindan, bir marta)",
                          "A · Индексация (заранее, один раз)",
                          "A · Indexing (offline, once)"),
               extra_html=code(
                   "1. Hujjatlarni yuklash (PDF, HTML, DOCX)\n"
                   "2. Matnga aylantirish va tozalash\n"
                   "3. CHUNKING — parchalarga bo'lish\n"
                   "4. Har parcha -> EMBEDDING (vektor)\n"
                   "5. Vektorlarni bazaga yozish\n\n"
                   "// Bu bosqich sekin va qimmat,\n"
                   "// lekin faqat bir marta bajariladi."))
         + "\n"
         + box("green", ("B · So'rov (har savolda)", "B · Запрос (на каждый вопрос)",
                         "B · Query (every question)"),
               extra_html=code(
                   "1. Foydalanuvchi savoli -> EMBEDDING\n"
                   "2. Bazada eng yaqin K ta vektorni topish\n"
                   "3. Ularning matnini olish\n"
                   "4. Prompt yig'ish:\n"
                   "   system + [topilgan parchalar] + savol\n"
                   "5. LLM javob beradi + manbalar\n\n"
                   "// Bu bosqich tez: 50-200 ms"))
         + "\n</div>\n"
         + box("accent", ("Eng muhim nuqta", "Самое важное", "The key point"),
               p=("LLM bu yerda <b>faqat oxirgi qadamda</b> qatnashadi. RAG ning "
                  "sifati 90% <b>qidiruv bosqichiga</b> bog'liq. Agar noto'g'ri "
                  "parchalar topilsa, dunyodagi eng kuchli model ham to'g'ri javob "
                  "bera olmaydi — u faqat berilgan axlatni chiroyli qilib qaytaradi. "
                  "Shuning uchun RAG — bu <b>qidiruv muhandisligi</b>, generatsiya emas.",
                  "LLM участвует здесь <b>только на последнем шаге</b>. Качество RAG "
                  "на 90% определяется <b>этапом поиска</b>. Если найдены не те "
                  "фрагменты, даже сильнейшая модель не ответит верно — она лишь "
                  "красиво перескажет мусор. Поэтому RAG — это <b>инженерия поиска</b>, "
                  "а не генерации.",
                  "The LLM appears <b>only in the last step</b>. RAG quality is 90% "
                  "determined by the <b>retrieval phase</b>. If the wrong chunks are "
                  "retrieved, even the strongest model cannot answer correctly — it "
                  "will just restate the garbage elegantly. RAG is <b>retrieval "
                  "engineering</b>, not generation.")),
))

S.append(slide(
    ph=("Chunking", "Чанкинг", "Chunking"), time="16–21",
    eyebrow=("Eng ko'p xato qilinadigan qadam", "Этап с наибольшим числом ошибок",
             "The step most often done wrong"),
    title=("Chunk hajmi — RAG dagi eng muhim giperparametr",
           "Размер чанка — главный гиперпараметр RAG",
           "Chunk size is the key hyperparameter in RAG"),
    body='<div class="cols c3">\n' + "\n".join([
        box("accent", ("Juda kichik (< 100 token)", "Слишком мелкий (< 100 токенов)",
                       "Too small (< 100 tokens)"),
            p=("Parcha <b>kontekstni yo'qotadi</b>. \"U 15% ni tashkil qiladi\" — "
               "nima 15%? Olmosh oldingi chunkda qolgan. Qidiruv topadi, lekin "
               "javob ma'nosiz chiqadi.",
               "Фрагмент <b>теряет контекст</b>. «Он составляет 15%» — что составляет? "
               "Местоимение осталось в предыдущем чанке. Поиск найдёт, но ответ "
               "получится бессмысленным.",
               "The chunk <b>loses context</b>. \"It amounts to 15%\" — what does? "
               "The antecedent stayed in the previous chunk. Retrieval succeeds, "
               "the answer is meaningless.")),
        box("purple", ("Juda katta (> 1000 token)", "Слишком крупный (> 1000 токенов)",
                       "Too large (> 1000 tokens)"),
            p=("Bitta vektor <b>bir nechta mavzuni</b> o'z ichiga oladi va ularning "
               "o'rtachasiga aylanadi. Natijada u hech bir so'rovga aniq mos kelmaydi "
               "— <b>semantik suyultirish</b> (dilution).",
               "Один вектор вбирает <b>несколько тем</b> и становится их усреднением. "
               "В итоге он не подходит точно ни к одному запросу — "
               "<b>семантическое размывание</b>.",
               "One vector absorbs <b>several topics</b> and becomes their average. "
               "It then matches no query precisely — <b>semantic dilution</b>.")),
        box("green", ("Amaliy oraliq", "Рабочий диапазон", "The practical range"),
            p=("<b>200–500 token</b> + <b>10–20% overlap</b>. Overlap chegarada "
               "qolib ketgan jumlani qutqaradi. Va eng muhimi: <b>ma'no chegarasi "
               "bo'yicha</b> bo'ling — paragraf, sarlavha, bo'lim.",
               "<b>200–500 токенов</b> + <b>10–20% перекрытие</b>. Overlap спасает "
               "предложение, разрезанное на границе. И главное: режьте "
               "<b>по смысловым границам</b> — абзац, заголовок, раздел.",
               "<b>200–500 tokens</b> + <b>10–20% overlap</b>. Overlap rescues a "
               "sentence cut at the boundary. And above all: split "
               "<b>on semantic boundaries</b> — paragraph, heading, section.")),
    ]) + "\n</div>\n"
         + box("", ("Oltin qoida", "Золотое правило", "The golden rule"),
               p=("<b>Bir chunk — bir tugallangan fikr.</b> Belgi yoki token bo'yicha "
                  "ko'r-ko'rona kesish (naive fixed-size splitting) — RAG tizimlaridagi "
                  "muammolarning eng ko'p uchraydigan sababi. Stendda buni o'z ko'zingiz "
                  "bilan ko'rasiz.",
                  "<b>Один чанк — одна законченная мысль.</b> Слепая нарезка по символам "
                  "или токенам (naive fixed-size splitting) — самая частая причина "
                  "проблем в RAG-системах. На стенде вы увидите это своими глазами.",
                  "<b>One chunk, one complete thought.</b> Blind fixed-size splitting by "
                  "characters or tokens is the single most common cause of failure in "
                  "RAG systems. You will see it on the lab yourself.")),
))

S.append(slide(
    ph=("Embedding", "Эмбеддинг", "Embedding"), time="21–26",
    eyebrow=("Matndan vektorga", "Из текста в вектор", "From text to vector"),
    title=("Embedding — ma'noning ko'p o'lchovli fazodagi koordinatasi",
           "Эмбеддинг — координата смысла в многомерном пространстве",
           "An embedding is a coordinate of meaning in a high-dimensional space"),
    body='<div class="cols c2">\n'
         + box("purple", ("Nima bo'lyapti", "Что происходит", "What is happening"),
               p=("Maxsus neyron model matnni <b>sonlar massiviga</b> aylantiradi — "
                  "odatda 384, 768 yoki 1536 o'lchov. Bu sonlar tasodifiy emas: model "
                  "shunday o'qitilganki, <b>ma'nosi yaqin matnlar fazoda yaqin "
                  "joylashadi</b>. Muhimi: taqqoslanayotgan barcha matnlar "
                  "<b>bitta model</b> bilan vektorlanishi shart.",
                  "Специальная нейросеть превращает текст в <b>массив чисел</b> — обычно "
                  "384, 768 или 1536 измерений. Эти числа не случайны: модель обучена "
                  "так, что <b>близкие по смыслу тексты оказываются рядом в "
                  "пространстве</b>. Важно: все сравниваемые тексты должны быть "
                  "векторизованы <b>одной моделью</b>.",
                  "A dedicated neural model turns text into an <b>array of numbers</b> — "
                  "typically 384, 768 or 1536 dimensions. Those numbers are not random: "
                  "the model is trained so that <b>texts close in meaning land close in "
                  "the space</b>. Critically: every text being compared must be embedded "
                  "by the <b>same model</b>."))
         + "\n"
         + box("green", ("Nega bu kalit so'z qidiruvidan kuchli",
                         "Почему это сильнее поиска по ключевым словам",
                         "Why this beats keyword search"),
               extra_html=code(
                   "Savol:  \"Xodim kasal bo'lsa nima qilsin?\"\n"
                   "Hujjat: \"Mehnatga layoqatsizlik varaqasi\"\n\n"
                   "Umumiy so'z:      0 ta\n"
                   "Kalit so'z qidiruvi: TOPMAYDI\n"
                   "Vektor qidiruv:      TOPADI (0.81)\n\n"
                   "// Chunki ma'no yaqin, garchi\n"
                   "// so'zlar butunlay boshqa bo'lsa ham."))
         + "\n</div>\n"
         + box("accent", ("⚠️ Stend haqida halol ogohlantirish",
                          "⚠️ Честное предупреждение о стенде",
                          "⚠️ An honest note about the lab"),
               p=("Laboratoriya brauzerda, internetsiz ishlaydi — shuning uchun unda "
                  "<b>soddalashtirilgan leksik embedding</b> (TF-IDF uslubidagi vektor) "
                  "ishlatiladi. Chunking, kosinus o'xshashlik, top-K va reranking "
                  "mexanikasi <b>aynan real tizimdagidek</b>, lekin semantik yaqinlik "
                  "real neyron embedding darajasida emas. Buni yodda tuting.",
                  "Лаборатория работает в браузере без интернета, поэтому в ней "
                  "используется <b>упрощённый лексический эмбеддинг</b> (вектор в стиле "
                  "TF-IDF). Механика чанкинга, косинусной близости, top-K и реранкинга "
                  "<b>в точности как в реальной системе</b>, но семантическая близость "
                  "не на уровне настоящего нейросетевого эмбеддинга. Держите это в уме.",
                  "The lab runs in the browser with no internet, so it uses a "
                  "<b>simplified lexical embedding</b> (a TF-IDF style vector). The "
                  "mechanics of chunking, cosine similarity, top-K and reranking are "
                  "<b>exactly as in a real system</b>, but semantic closeness is not at "
                  "the level of a true neural embedding. Keep that in mind.")),
))

S.append(slide(
    ph=("Matematika", "Математика", "The maths"), time="26–31",
    eyebrow=("Kosinus o'xshashlik", "Косинусная близость", "Cosine similarity"),
    title=("Nega burchak o'lchanadi, masofa emas",
           "Почему измеряют угол, а не расстояние",
           "Why we measure the angle, not the distance"),
    body='<div class="cols c2">\n'
         + box("green", ("Formula", "Формула", "The formula"),
               extra_html=code(
                   "cos(A, B) = (A · B) / (|A| × |B|)\n\n"
                   "A · B = a1*b1 + a2*b2 + ... + an*bn   // skalyar ko'paytma\n"
                   "|A|   = sqrt(a1^2 + a2^2 + ... + an^2) // uzunlik (norma)\n\n"
                   "Natija: -1 ... +1\n"
                   "  1.0  — bir xil yo'nalish (ma'no bir xil)\n"
                   "  0.0  — ortogonal (umuman bog'liq emas)\n"
                   " -1.0  — qarama-qarshi yo'nalish"))
         + "\n"
         + box("purple", ("Nega aynan burchak", "Почему именно угол", "Why the angle"),
               items=[
                   ("Vektor <b>uzunligi</b> ko'pincha matn <b>hajmini</b> aks ettiradi, "
                    "ma'nosini emas. Uzun hujjat = uzun vektor.",
                    "<b>Длина</b> вектора часто отражает <b>объём</b> текста, а не смысл. "
                    "Длинный документ = длинный вектор.",
                    "A vector's <b>length</b> often reflects text <b>size</b>, not "
                    "meaning. A long document gives a long vector."),
                   ("Evklid masofasi ishlatilsa, qisqa savol uzun hujjatdan "
                    "\"uzoq\" bo'lib chiqadi — hatto mavzu bir xil bo'lsa ham.",
                    "При евклидовом расстоянии короткий вопрос окажется «далеко» от "
                    "длинного документа — даже если тема одна.",
                    "With Euclidean distance a short question lands \"far\" from a long "
                    "document — even when the topic is identical."),
                   ("Burchak <b>yo'nalishni</b> o'lchaydi, ya'ni <b>sof ma'noni</b>. "
                    "Hajm ta'sir qilmaydi.",
                    "Угол измеряет <b>направление</b>, то есть <b>чистый смысл</b>. "
                    "Объём не влияет.",
                    "The angle measures <b>direction</b> — pure <b>meaning</b>. "
                    "Size does not interfere."),
                   ("Amalda vektorlar <b>normalizatsiya qilinadi</b> (|A| = 1), shunda "
                    "kosinus oddiy skalyar ko'paytmaga aylanadi — juda tez.",
                    "На практике векторы <b>нормализуют</b> (|A| = 1), и косинус "
                    "превращается в обычное скалярное произведение — очень быстро.",
                    "In practice vectors are <b>normalised</b> (|A| = 1), so cosine "
                    "reduces to a plain dot product — very fast."),
               ])
         + "\n</div>",
))

S.append(slide(
    ph=("Vektor baza", "Векторная БД", "Vector DB"), time="31–35",
    eyebrow=("Millionlab vektor ichidan qidirish", "Поиск среди миллионов векторов",
             "Searching millions of vectors"),
    title=("To'liq saralash ishlamaydi — ANN va HNSW kerak",
           "Полный перебор не работает — нужны ANN и HNSW",
           "Brute force does not scale — you need ANN and HNSW"),
    body='<div class="cols c2">\n'
         + box("accent", ("Brute force muammosi", "Проблема полного перебора",
                          "The brute-force problem"),
               extra_html=code(
                   "10 000 000 vektor x 1536 o'lcham\n"
                   "= har so'rovga 15 milliard ko'paytirish\n\n"
                   "Kutish vaqti: ~10 soniya\n"
                   "Kerakli vaqt:  ~50 millisekund\n\n"
                   "// 200 barobar farq — boshqa\n"
                   "// algoritm kerak."))
         + "\n"
         + box("green", ("ANN: aniqlikni tezlikka almashtirish",
                         "ANN: обмен точности на скорость",
                         "ANN: trading accuracy for speed"),
               items=[
                   ("<b>ANN</b> = Approximate Nearest Neighbour. U <b>eng yaqin</b> "
                    "emas, <b>deyarli eng yaqin</b> vektorlarni topadi.",
                    "<b>ANN</b> = Approximate Nearest Neighbour. Находит не "
                    "<b>самые близкие</b>, а <b>почти самые близкие</b> векторы.",
                    "<b>ANN</b> = Approximate Nearest Neighbour. It finds not the "
                    "<b>nearest</b> but the <b>almost-nearest</b> vectors."),
                   ("<b>HNSW</b> — ko'p qavatli graf. Yuqori qavat — \"samolyot\" "
                    "(uzoq sakrashlar), pastki qavat — \"piyoda\" (aniq qidiruv).",
                    "<b>HNSW</b> — многослойный граф. Верхний слой — «самолёт» "
                    "(дальние прыжки), нижний — «пешком» (точный поиск).",
                    "<b>HNSW</b> — a multi-layer graph. The top layer is the "
                    "\"aeroplane\" (long hops), the bottom is \"on foot\" (precise)."),
                   ("Natija: <b>~99% aniqlik</b>, lekin <b>1000 barobar tez</b>. "
                    "Bu tijoriy tizimlar uchun mutlaqo maqbul savdo.",
                    "Результат: <b>~99% точности</b>, но <b>в 1000 раз быстрее</b>. "
                    "Для коммерческих систем это полностью приемлемый обмен.",
                    "Result: <b>~99% accuracy</b> but <b>1000× faster</b>. "
                    "A perfectly acceptable trade for production systems."),
                   ("Sanoat yechimlari: <b>pgvector</b>, Qdrant, Pinecone, Weaviate, "
                    "Milvus, FAISS.",
                    "Индустриальные решения: <b>pgvector</b>, Qdrant, Pinecone, "
                    "Weaviate, Milvus, FAISS.",
                    "Industry options: <b>pgvector</b>, Qdrant, Pinecone, Weaviate, "
                    "Milvus, FAISS."),
               ])
         + "\n</div>",
))

S.append(slide(
    ph=("Kontekst yig'ish", "Сборка контекста", "Context assembly"), time="35–39",
    eyebrow=("Top-K dan keyin nima bo'ladi", "Что происходит после top-K",
             "What happens after top-K"),
    title=("Topilgan parchalarni promptga <b>qanday</b> joylash ham muhim",
           "<b>Как</b> разместить найденные фрагменты в промпте — тоже важно",
           "<b>How</b> you place the retrieved chunks in the prompt matters too"),
    body='<div class="cols c2">\n'
         + box("purple", ("Uchta texnika", "Три техники", "Three techniques"),
               items=[
                   ("<b>Top-K tanlash.</b> Odatda K = 3–8. Ko'p olsangiz shovqin "
                    "kiradi, kam olsangiz javob to'liq bo'lmaydi.",
                    "<b>Выбор top-K.</b> Обычно K = 3–8. Больше — попадёт шум, "
                    "меньше — ответ будет неполным.",
                    "<b>Top-K selection.</b> Usually K = 3–8. More brings noise, "
                    "fewer leaves the answer incomplete."),
                   ("<b>Reranking.</b> Birinchi qidiruv tez va taxminiy. Keyin "
                    "kuchliroq <b>cross-encoder</b> model top-50 ni qayta baholab, "
                    "eng yaxshi 5 tasini qoldiradi.",
                    "<b>Реранкинг.</b> Первый поиск быстрый и грубый. Затем более "
                    "сильная модель <b>cross-encoder</b> переоценивает top-50 "
                    "и оставляет лучшие 5.",
                    "<b>Reranking.</b> The first pass is fast and rough. Then a "
                    "stronger <b>cross-encoder</b> re-scores the top-50 and keeps "
                    "the best 5."),
                   ("<b>MMR</b> (Maximal Marginal Relevance). Bir xil ma'noli 5 ta "
                    "parcha o'rniga — <b>xilma-xil</b> 5 tasi. Takrorni oldini oladi.",
                    "<b>MMR</b> (Maximal Marginal Relevance). Вместо 5 фрагментов об "
                    "одном и том же — 5 <b>разнообразных</b>. Убирает дубли.",
                    "<b>MMR</b> (Maximal Marginal Relevance). Instead of 5 chunks "
                    "saying the same thing — 5 <b>diverse</b> ones. Removes duplicates."),
               ])
         + "\n"
         + box("green", ("Prompt tuzilishi", "Структура промпта", "Prompt structure"),
               extra_html=code(
                   "SYSTEM:\n"
                   "  Faqat quyidagi kontekstga tayanib javob ber.\n"
                   "  Agar kontekstda javob bo'lmasa, \"bilmayman\" deb ayt.\n"
                   "  Har faktdan keyin manba raqamini ko'rsat.\n\n"
                   "KONTEKST:\n"
                   "  [1] {eng mos parcha}\n"
                   "  [2] {ikkinchi parcha}\n"
                   "  [3] {uchinchi parcha}\n\n"
                   "SAVOL: {foydalanuvchi savoli}\n\n"
                   "// Eng muhim qatorlar: \"bilmayman\" va manba."))
         + "\n</div>",
))

S.append(slide(
    ph=("Nosozliklar", "Отказы", "Failure modes"), time="39–43",
    eyebrow=("RAG qachon buziladi", "Когда RAG ломается", "When RAG breaks"),
    title=("To'rtta tipik nosozlik va ularning belgilari",
           "Четыре типичных отказа и их симптомы",
           "Four typical failure modes and their symptoms"),
    body='<div class="cols c4">\n' + "\n".join([
        box("accent", ("Chunk chegarasi", "Граница чанка", "Chunk boundary"),
            p=("Javob ikki chunk orasida qolib ketgan. <b>Belgi:</b> tizim "
               "\"yarim javob\" beradi. <b>Yechim:</b> overlap oshirish, ma'no "
               "bo'yicha bo'lish.",
               "Ответ разрезан между двумя чанками. <b>Симптом:</b> система даёт "
               "«половину ответа». <b>Решение:</b> увеличить overlap, резать по смыслу.",
               "The answer is split across two chunks. <b>Symptom:</b> the system gives "
               "\"half an answer\". <b>Fix:</b> raise overlap, split on meaning.")),
        box("purple", ("Semantik bo'shliq", "Семантический разрыв", "Semantic gap"),
            p=("Savol tilidan hujjat tili juda farq qiladi (jargon, qisqartma). "
               "<b>Yechim:</b> gibrid qidiruv — vektor + BM25 kalit so'z.",
               "Язык вопроса сильно отличается от языка документа (жаргон, "
               "аббревиатуры). <b>Решение:</b> гибридный поиск — вектор + BM25.",
               "The question's vocabulary differs sharply from the document's (jargon, "
               "acronyms). <b>Fix:</b> hybrid search — vector + BM25 keywords.")),
        box("green", ("Eskirgan indeks", "Устаревший индекс", "Stale index"),
            p=("Hujjat yangilandi, vektor yangilanmadi. Tizim <b>ishonch bilan eski</b> "
               "javob beradi. <b>Yechim:</b> hujjat o'zgarishida qayta indekslash.",
               "Документ обновили, вектор — нет. Система <b>уверенно даёт устаревший</b> "
               "ответ. <b>Решение:</b> переиндексация при изменении документа.",
               "The document changed, the vector did not. The system <b>confidently "
               "serves stale</b> answers. <b>Fix:</b> reindex on document change.")),
        box("", ("Kontekstga qarshi", "Против контекста", "Ignoring context"),
            p=("Parcha to'g'ri topilgan, lekin model o'z \"bilimiga\" tayangan. "
               "<b>Yechim:</b> qattiq system prompt + manba talab qilish.",
               "Фрагмент найден верно, но модель опирается на свои «знания». "
               "<b>Решение:</b> жёсткий system prompt + требование цитаты.",
               "The right chunk was found but the model leaned on its own \"knowledge\". "
               "<b>Fix:</b> a strict system prompt + mandatory citations.")),
    ]) + "\n</div>",
))

S.append(slide(
    ph=("Amaliyot", "Практика", "Practice"), time="43–55",
    eyebrow=("Laboratoriya · 12 daqiqa", "Лаборатория · 12 минут", "Lab · 12 minutes"),
    title=("RAG stendi: lab/index.html ni oching",
           "RAG-стенд: откройте lab/index.html",
           "RAG lab: open lab/index.html"),
    body='<div class="cols c4">\n' + "\n".join([
        box("purple", ("1 · Chunking (3 daq)", "1 · Чанкинг (3 мин)", "1 · Chunking (3 min)"),
            p=("Chunk hajmini <b>40</b> ga tushiring va bir savol bering. Keyin "
               "<b>400</b> ga oshiring. Ikkala holatda ham top-1 ballni yozing.",
               "Опустите размер чанка до <b>40</b> и задайте вопрос. Затем поднимите "
               "до <b>400</b>. Запишите балл top-1 в обоих случаях.",
               "Drop chunk size to <b>40</b> and ask a question. Then raise it to "
               "<b>400</b>. Record the top-1 score in both cases.")),
        box("green", ("2 · Kosinus (3 daq)", "2 · Косинус (3 мин)", "2 · Cosine (3 min)"),
            p=("Stend har parcha uchun kosinus ballini ko'rsatadi. <b>Eng yuqori va "
               "eng past</b> ballni yozing va farqni izohlang.",
               "Стенд показывает косинусный балл для каждого фрагмента. Запишите "
               "<b>наибольший и наименьший</b> и объясните разницу.",
               "The lab shows a cosine score per chunk. Record the <b>highest and "
               "lowest</b> and explain the gap.")),
        box("accent", ("3 · Top-K (3 daq)", "3 · Top-K (3 мин)", "3 · Top-K (3 min)"),
            p=("K ni <b>1</b> dan <b>8</b> gacha o'zgartiring. Javob qachon to'liq "
               "bo'ladi va qachon shovqin kira boshlaydi?",
               "Меняйте K от <b>1</b> до <b>8</b>. Когда ответ станет полным и когда "
               "начнёт попадать шум?",
               "Vary K from <b>1</b> to <b>8</b>. When does the answer become complete "
               "and when does noise creep in?")),
        box("", ("4 · Grounding (3 daq)", "4 · Гроундинг (3 мин)", "4 · Grounding (3 min)"),
            p=("Bazada <b>javobi yo'q</b> savol bering. Qattiq system prompt bilan va "
               "usiz sinab ko'ring — farqni yozing.",
               "Задайте вопрос, <b>ответа на который нет</b> в базе. Попробуйте "
               "с жёстким system prompt и без — запишите разницу.",
               "Ask a question the base <b>cannot answer</b>. Try with the strict "
               "system prompt and without — record the difference.")),
    ]) + "\n</div>\n"
         + box("green", ("🎯 Asosiy kuzatuv", "🎯 Главное наблюдение", "🎯 The key observation"),
               p=("4-sinovda siz RAG ning eng muhim xususiyatini ko'rasiz: "
                  "<b>\"bilmayman\" deb javob bera olish — bu tizimning kuchi, "
                  "zaifligi emas.</b> Gallyutsinatsiya qiladigan tizimdan "
                  "\"topilmadi\" deydigan tizim ancha qimmatliroq.",
                  "В 4-м испытании вы увидите главное свойство RAG: <b>способность "
                  "ответить «не знаю» — это сила системы, а не слабость.</b> Система, "
                  "которая говорит «не найдено», гораздо ценнее той, что галлюцинирует.",
                  "In trial 4 you meet RAG's most important property: <b>being able to "
                  "answer \"I do not know\" is a strength, not a weakness.</b> A system "
                  "that says \"not found\" is far more valuable than one that "
                  "hallucinates.")),
))

S.append(slide(
    ph=("Yakun", "Итоги", "Summary"), time="55–58",
    eyebrow=("Uy vazifasi va baholash", "Домашнее задание и оценка", "Homework and grading"),
    title=("Uy vazifasi: RAG o'lchovlari va loyihalash qarori (10 ball)",
           "Домашнее задание: замеры RAG и проектное решение (10 баллов)",
           "Homework: RAG measurements and a design decision (10 points)"),
    body='<div class="cols c2">\n'
         + box("green", ("Nima qilish kerak", "Что нужно сделать", "What to do"),
               items=[
                   ("Varaqadagi 4 sinov jadvalini <b>aniq raqamlar</b> bilan to'ldiring.",
                    "Заполните таблицу 4 испытаний <b>конкретными числами</b>.",
                    "Fill the 4-trial table with <b>concrete numbers</b>."),
                   ("Kosinus o'xshashlik formulasini yozing va <b>nega burchak "
                    "o'lchanishini</b> tushuntiring.",
                    "Запишите формулу косинусной близости и объясните, <b>почему "
                    "измеряется угол</b>.",
                    "Write the cosine similarity formula and explain <b>why the angle "
                    "is measured</b>."),
                   ("<b>Loyihalash topshirig'i:</b> maktabingiz uchun RAG tizimini "
                    "loyihalang — qaysi hujjatlar, chunk hajmi, K, va qanday "
                    "yangilanadi.",
                    "<b>Проектное задание:</b> спроектируйте RAG для вашей школы — какие "
                    "документы, размер чанка, K, и как обновляется индекс.",
                    "<b>Design task:</b> design a RAG system for your school — which "
                    "documents, chunk size, K, and how the index is refreshed."),
                   ("To'rtta nosozlikdan <b>bittasini</b> tanlab, uni qanday "
                    "aniqlash va tuzatishni yozing.",
                    "Выберите <b>один</b> из четырёх отказов и опишите, как его "
                    "обнаружить и исправить.",
                    "Pick <b>one</b> of the four failure modes and describe how to "
                    "detect and fix it."),
               ])
         + "\n"
         + box("accent", ("Baholash mezoni", "Критерии оценки", "Grading rubric"),
               extra_html='<ul class="plain">\n'
               + '  <li><span class="t" %s>4 sinov jadvali raqamlar bilan — <b>3 ball</b></span></li>\n'
               % i18n("4 sinov jadvali raqamlar bilan — <b>3 ball</b>",
                      "Таблица 4 испытаний с числами — <b>3 балла</b>",
                      "4-trial table with numbers — <b>3 points</b>")
               + '  <li><span class="t" %s>Kosinus formulasi va izohi — <b>2 ball</b></span></li>\n'
               % i18n("Kosinus formulasi va izohi — <b>2 ball</b>",
                      "Формула косинуса и объяснение — <b>2 балла</b>",
                      "Cosine formula and explanation — <b>2 points</b>")
               + '  <li><span class="t" %s>Maktab uchun RAG loyihasi — <b>3 ball</b></span></li>\n'
               % i18n("Maktab uchun RAG loyihasi — <b>3 ball</b>",
                      "Проект RAG для школы — <b>3 балла</b>",
                      "RAG design for the school — <b>3 points</b>")
               + '  <li><span class="t" %s>Nosozlik tahlili — <b>2 ball</b></span></li>\n'
               % i18n("Nosozlik tahlili — <b>2 ball</b>",
                      "Анализ отказа — <b>2 балла</b>",
                      "Failure mode analysis — <b>2 points</b>")
               + "</ul>")
         + "\n</div>",
))


NOTES = {
    "uz": [
        ["Titul slayd",
         "Xush kelibsiz. 13-darsda modelning miyasini ochdik, 14-darsda unga qo'l berdik. Bugun uchinchi muammoni yechamiz: model sizning hujjatlaringizni bilmaydi. Yechim — RAG, va bugun biz uning matematikasini ham ochamiz.",
         "lab/index.html ni proyektorda oldindan oching."],
        ["Uchta chegara",
         "Knowledge cutoff, gallyutsinatsiya, kontekst narxi. Eng muhim nuqta — ikkinchisi: model faktni bilmasa, bo'shliq qoldirmaydi, eng ehtimolli matnni yozadi. Bu arxitektura xususiyati, xato emas.",
         "Uch ustunni ketma-ket ochish."],
        ["Fine-tuning yoki RAG",
         "Aniq ajrating: fine-tuning — uslub uchun, RAG — faktlar uchun. Bu sanoatdagi eng ko'p chalkashtiriladigan qaror. Manba ko'rsatish imkoniyatini alohida ta'kidlang.",
         "Ikki ustunni solishtirish."],
        ["Ikki bosqichli arxitektura",
         "Indekslash oflayn, so'rov onlayn. Eng muhim gapni ayting: RAG sifati 90% qidiruvga bog'liq, LLM faqat oxirgi qadamda. Noto'g'ri parcha topilsa, eng kuchli model ham yordam bermaydi.",
         "Doskada ikki bosqichni chizish."],
        ["Chunking",
         "Eng ko'p xato qilinadigan qadam. Uchta holat: juda kichik, juda katta, to'g'ri. 200-500 token va 10-20% overlap raqamlarini doskaga yozing. Oltin qoida: bir chunk — bir tugallangan fikr.",
         "Doskaga '200-500 token, 10-20% overlap' yozish."],
        ["Embedding",
         "Matn -> vektor. Kalit so'z qidiruvi bilan taqqoslash misolini albatta ko'rsating — u juda ishonarli. VA: stend haqidagi halol ogohlantirishni o'qib bering, bu ilmiy halollik masalasi.",
         "Kod blokidagi misolni o'qish. Stend ogohlantirishini aytish."],
        ["Kosinus o'xshashlik",
         "Formulani doskada yozing. Asosiy savol: nega burchak, masofa emas? Javob — uzunlik hajmni aks ettiradi, ma'noni emas. Normalizatsiyadan keyin kosinus = skalyar ko'paytma.",
         "Doskada formulani chiqarish."],
        ["Vektor baza va HNSW",
         "Raqamlarni ayting: 15 milliard ko'paytirish, 10 soniya va 50 ms. 200 barobar farq. HNSW metaforasi — samolyot va piyoda. 99% aniqlik, 1000 barobar tezlik.",
         "Raqamlarni doskaga yozish."],
        ["Kontekst yig'ish",
         "Top-K, reranking, MMR. Prompt tuzilishidagi ikkita eng muhim qatorni ta'kidlang: 'bilmayman deb ayt' va 'manba ko'rsat'. Bu ikkalasi gallyutsinatsiyani keskin kamaytiradi.",
         "Prompt blokini o'qib chiqish."],
        ["To'rtta nosozlik",
         "Har birining BELGISI va YECHIMI bor — bu diagnostika jadvali. Bu slayd uy vazifasining bir qismi uchun asos, shuning uchun aniq o'ting.",
         "To'rt ustunni ketma-ket ko'rsatish."],
        ["Amaliyot 12 daqiqa",
         "To'rt sinov. Eng qimmatlisi — to'rtinchisi: bazada javobi yo'q savol. O'quvchilar 'bilmayman' javobi tizimning kuchi ekanini tushunishi kerak.",
         "Vaqtni nazorat qilish, raqamlar yozilganini tekshirish."],
        ["Yakun va baholash",
         "Xulosa: RAG — qidiruv muhandisligi, generatsiya emas. Uy vazifasida loyihalash topshirig'i bor — bu eng qimmatli qism, 3 ball. Varaqalarni yig'ing.",
         "Varaqalarni yig'ish. Keyingi dars — prompt injection va AI xavfsizligi."],
    ],
    "ru": [
        ["Титульный слайд",
         "Добро пожаловать. На уроке 13 мы вскрыли мозг модели, на 14 дали ей руки. Сегодня решаем третью проблему: модель не знает ваших документов. Решение — RAG, и сегодня мы вскроем и его математику.",
         "Заранее откройте lab/index.html на проекторе."],
        ["Три предела",
         "Knowledge cutoff, галлюцинации, цена контекста. Главное — второе: не зная факта, модель не оставит пустоту, она напишет наиболее вероятный текст. Это свойство архитектуры, а не баг.",
         "Открывать три колонки по очереди."],
        ["Fine-tuning или RAG",
         "Чётко разделите: fine-tuning — для стиля, RAG — для фактов. Это самое частое путаемое решение в индустрии. Отдельно подчеркните возможность показать источник.",
         "Сравнить две колонки."],
        ["Двухэтапная архитектура",
         "Индексация офлайн, запрос онлайн. Скажите главное: качество RAG на 90% определяется поиском, LLM участвует только в последнем шаге. Нашли не тот фрагмент — не спасёт и сильнейшая модель.",
         "Нарисовать два этапа на доске."],
        ["Чанкинг",
         "Этап с наибольшим числом ошибок. Три случая: слишком мелко, слишком крупно, правильно. Напишите на доске 200-500 токенов и 10-20% overlap. Золотое правило: один чанк — одна законченная мысль.",
         "Написать на доске «200-500 токенов, 10-20% overlap»."],
        ["Эмбеддинг",
         "Текст -> вектор. Обязательно покажите пример сравнения с поиском по ключевым словам — он очень убедителен. И: прочитайте честное предупреждение о стенде, это вопрос научной честности.",
         "Прочитать пример из блока кода. Озвучить предупреждение."],
        ["Косинусная близость",
         "Напишите формулу на доске. Главный вопрос: почему угол, а не расстояние? Ответ — длина отражает объём, а не смысл. После нормализации косинус = скалярное произведение.",
         "Вывести формулу на доске."],
        ["Векторная БД и HNSW",
         "Назовите числа: 15 миллиардов умножений, 10 секунд против 50 мс. Разница в 200 раз. Метафора HNSW — самолёт и пешком. 99% точности, в 1000 раз быстрее.",
         "Написать числа на доске."],
        ["Сборка контекста",
         "Top-K, реранкинг, MMR. Подчеркните две важнейшие строки в структуре промпта: «скажи не знаю» и «покажи источник». Вдвоём они резко снижают галлюцинации.",
         "Прочитать блок промпта."],
        ["Четыре отказа",
         "У каждого есть СИМПТОМ и РЕШЕНИЕ — это диагностическая таблица. Слайд лежит в основе части домашнего задания, поэтому пройдите его чётко.",
         "Показать четыре колонки по очереди."],
        ["Практика 12 минут",
         "Четыре испытания. Самое ценное — четвёртое: вопрос, ответа на который нет в базе. Ученики должны понять, что ответ «не знаю» — это сила системы.",
         "Следить за временем, проверять записанные числа."],
        ["Итоги и оценивание",
         "Вывод: RAG — это инженерия поиска, а не генерации. В домашнем задании есть проектная часть — самая ценная, 3 балла. Соберите листы.",
         "Собрать листы. Следующий урок — prompt injection и безопасность AI."],
    ],
    "en": [
        ["Title slide",
         "Welcome. In lesson 13 we opened the model's brain, in 14 we gave it hands. Today we solve the third problem: the model does not know your documents. The answer is RAG, and today we open its maths too.",
         "Pre-open lab/index.html on the projector."],
        ["Three limits",
         "Knowledge cutoff, hallucination, context cost. The second matters most: lacking a fact, the model will not leave a gap — it writes the most probable text. An architectural property, not a bug.",
         "Reveal the three columns in turn."],
        ["Fine-tuning or RAG",
         "Separate them clearly: fine-tuning is for style, RAG is for facts. This is the most commonly confused decision in industry. Stress the ability to cite sources.",
         "Compare the two columns."],
        ["The two-phase architecture",
         "Indexing offline, querying online. State the key line: RAG quality is 90% retrieval, the LLM only appears in the last step. Retrieve the wrong chunk and no model can save you.",
         "Draw the two phases on the board."],
        ["Chunking",
         "The step most often done wrong. Three cases: too small, too large, right. Write 200-500 tokens and 10-20% overlap on the board. Golden rule: one chunk, one complete thought.",
         "Write '200-500 tokens, 10-20% overlap' on the board."],
        ["Embeddings",
         "Text -> vector. Definitely show the keyword-search comparison — it is very convincing. And read out the honest note about the lab; this is a matter of scientific integrity.",
         "Read the code-block example. State the lab caveat."],
        ["Cosine similarity",
         "Write the formula on the board. The key question: why the angle, not the distance? Because length reflects size, not meaning. After normalisation cosine equals the dot product.",
         "Derive the formula on the board."],
        ["Vector DBs and HNSW",
         "Say the numbers: 15 billion multiplications, 10 seconds versus 50 ms. A 200× gap. The HNSW metaphor: aeroplane and on foot. 99% accuracy, 1000× faster.",
         "Write the numbers on the board."],
        ["Context assembly",
         "Top-K, reranking, MMR. Stress the two most important lines in the prompt structure: 'say I do not know' and 'cite the source'. Together they cut hallucination sharply.",
         "Read through the prompt block."],
        ["Four failure modes",
         "Each has a SYMPTOM and a FIX — this is a diagnostic table. The slide underpins part of the homework, so cover it precisely.",
         "Show the four columns in turn."],
        ["Practice, 12 minutes",
         "Four trials. The fourth is the most valuable: a question the base cannot answer. Students must grasp that answering 'I do not know' is a strength.",
         "Watch the clock, check the numbers are written."],
        ["Summary and grading",
         "Conclusion: RAG is retrieval engineering, not generation. The homework has a design task — the most valuable part, 3 points. Collect the sheets.",
         "Collect sheets. Next lesson — prompt injection and AI security."],
    ],
}

VARAQA = (
    sheet_header(
        ("15-dars: RAG va Embeddinglar — Chunking, Vektor Qidiruv, Kosinus",
         "Урок 15: RAG и Эмбеддинги — Чанкинг, Векторный Поиск, Косинус",
         "Lesson 15: RAG and Embeddings — Chunking, Vector Search, Cosine"),
        ("Target International School · 10–11-sinflar (Senior) · 4-hafta (1-soat)",
         "Target International School · 10–11 классы (Senior) · 4-я неделя (1-й час)",
         "Target International School · Grades 10–11 (Senior) · Week 4 (Hour 1)"))
    + mission(
        ("🎯 Laboratoriya missiyasi: qidiruv sifatini o'lchang",
         "🎯 Лабораторная миссия: измерьте качество поиска",
         "🎯 Lab mission: measure retrieval quality"),
        ("<b>lab/index.html</b> ni oching. RAG sifati generatsiyaga emas, "
         "<b>qidiruvga</b> bog'liq — bugun buni raqamlar bilan isbotlaysiz. "
         "Har sinovda kosinus ballini aniq yozing. Yakuniy topshiriq: "
         "maktabingiz uchun RAG tizimini loyihalash.",
         "Откройте <b>lab/index.html</b>. Качество RAG определяется не генерацией, "
         "а <b>поиском</b> — сегодня вы докажете это числами. В каждом испытании "
         "записывайте косинусный балл. Финальное задание: спроектировать RAG "
         "для вашей школы.",
         "Open <b>lab/index.html</b>. RAG quality is set by <b>retrieval</b>, not "
         "generation — today you prove it with numbers. Record the cosine score in "
         "every trial. Final task: design a RAG system for your school."))
    + table(
        [("Sinov", "Испытание", "Trial"),
         ("Sozlama", "Настройка", "Setting"),
         ("O'lchov", "Замер", "Measurement"),
         ("Xulosa", "Вывод", "Conclusion")],
        [[("1 · Chunking", "1 · Чанкинг", "1 · Chunking"),
          ("Chunk = 40 → keyin 400", "Чанк = 40 → затем 400", "Chunk = 40 → then 400"),
          ("top-1 ball: ______ → ______",
           "балл top-1: ______ → ______",
           "top-1 score: ______ → ______"), None],
         [("2 · Kosinus", "2 · Косинус", "2 · Cosine"),
          ("Bitta savol, barcha parchalar",
           "Один вопрос, все фрагменты",
           "One question, all chunks"),
          ("maks: ______ · min: ______",
           "макс: ______ · мин: ______",
           "max: ______ · min: ______"), None],
         [("3 · Top-K", "3 · Top-K", "3 · Top-K"),
          ("K = 1 → 3 → 8", "K = 1 → 3 → 8", "K = 1 → 3 → 8"),
          ("Eng yaxshi K: ______ · Nega: ______",
           "Лучший K: ______ · Почему: ______",
           "Best K: ______ · Why: ______"), None],
         [("4 · Grounding", "4 · Гроундинг", "4 · Grounding"),
          ("Bazada javobi yo'q savol",
           "Вопрос без ответа в базе",
           "A question the base cannot answer"),
          ("Qattiq prompt bilan: ______ · Usiz: ______",
           "С жёстким промптом: ______ · Без: ______",
           "With strict prompt: ______ · Without: ______"), None]])
    + '    <div class="rubric-grid">\n'
    + sheet_box(
        ("✏️ Matematika va loyihalash",
         "✏️ Математика и проектирование",
         "✏️ Maths and design"),
        writelines(2, ("Kosinus o'xshashlik formulasi va NEGA masofa emas, burchak:",
                       "Формула косинусной близости и ПОЧЕМУ угол, а не расстояние:",
                       "The cosine similarity formula and WHY the angle, not distance:"))
        + "\n"
        + writelines(4, ("🏫 Maktab uchun RAG loyihasi (hujjatlar, chunk, K, yangilanish):",
                         "🏫 Проект RAG для школы (документы, чанк, K, обновление):",
                         "🏫 RAG design for the school (documents, chunk, K, refresh):"))
        + "\n"
        + writelines(2, ("⚠️ Bitta nosozlik: belgisi va yechimi:",
                         "⚠️ Один отказ: симптом и решение:",
                         "⚠️ One failure mode: symptom and fix:")))
    + "\n"
    + sheet_box(
        ("📊 Baholash mezoni (10 ball)",
         "📊 Критерии оценки (10 баллов)",
         "📊 Grading rubric (10 points)"),
        rubric([
            (("4 sinov jadvali raqamlar bilan", "Таблица 4 испытаний с числами",
              "4-trial table with numbers"), "3"),
            (("Kosinus formulasi va izohi", "Формула косинуса и объяснение",
              "Cosine formula and explanation"), "2"),
            (("Maktab uchun RAG loyihasi", "Проект RAG для школы",
              "RAG design for the school"), "3"),
            (("Nosozlik tahlili", "Анализ отказа", "Failure mode analysis"), "2"),
        ], "10"))
    + "\n    </div>\n  </div>\n"
    + sign_box()
)

if __name__ == "__main__":
    print(Lesson(D, TITLES, SHEET_TITLES, "vc-notes-10-15", S, NOTES, VARAQA).build())
