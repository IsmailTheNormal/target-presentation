# -*- coding: utf-8 -*-
"""9-sinf · 4-hafta · 19-dars — Vebhooklar va Hodisalarga Asoslangan Avtomatlashtirish: Real-Vaqt Integratsiya."""

import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from build import (Lesson, slide, title_slide, box, code, el, i18n,
                   sheet_header, mission, table, sheet_box, rubric, writelines, sign_box)

D = "classes/9-sinf/4-hafta/19-dars-vebhooklar-va-avtomatlashtirish"

TITLES = {
    "uz": "19-dars: Vebhooklar va Avtomatlashtirish — Real-Vaqt Integratsiya va Kiber-Himoya",
    "ru": "Урок 19: Вебхуки и Автоматизация — Интеграция в Реальном Времени и Киберзащита",
    "en": "Lesson 19: Webhooks & Event Automation — Real-Time Integration & HMAC Security",
}
SHEET_TITLES = {k: v + (" — Ish Varaqasi" if k == "uz" else
                        " — Рабочий Лист" if k == "ru" else " — Worksheet")
                for k, v in TITLES.items()}

S = []

# 1. Title Slide
S.append(title_slide(
    ph=("Kirish", "Введение", "Intro"), time="0–3",
    eyebrow=("Vibecoding · 19-dars · 9-sinf (Event-Driven Track)",
             "Vibecoding · Урок 19 · 9 класс (Event-Driven Track)",
             "Vibecoding · Lesson 19 · Grade 9 (Event-Driven Track)"),
    h1=("Vebhooklar: Hodisalarga Asoslangan Real-Vaqt Integratsiya",
        "Вебхуки: Событийно-Ориентированная Интеграция в Реальном Времени",
        "Webhooks: Event-Driven Real-Time Architecture & HMAC Defense"),
    lede=("Eski usul: serverdan har 5 soniyada <i>\"Yangi xabar bormi?\"</i> deb so'rash (Polling) "
          "tarmoq trafigi va batareyani behuda yondiradi. Zamonaviy dunyo <b>Hodisalarga Asoslangan (Event-Driven)</b> "
          "arxitektura ustiga qurilgan: hodisa yuz berganda server o'zi bizning endpointimizga qo'ng'iroq qiladi — "
          "bu <b>Webhook (Teskari API)</b> deyiladi. Bugun siz xavfsiz <b>HMAC SHA-256 imzo tekshiruvi</b>, "
          "<b>Idempotentlik</b> va <b>GitHub to Telegram jonli avtomatlashtirish</b>ni yaratasiz.",
          "Устаревший подход: опрашивать сервер каждые 5 секунд вопросом <i>«Есть новое сообщение?»</i> (Polling) "
          "впустую сжигает трафик и ресурсы. Современный IT-мир работает на <b>Событийно-Ориентированной (Event-Driven)</b> "
          "архитектуре: при наступлении события сервис сам отправляет HTTP-вызов на наш сервер — "
          "это называется <b>Webhook (Обратный API)</b>. Сегодня вы научитесь криптографической проверке <b>HMAC SHA-256</b>, "
          "<b>Идемпотентности</b> и создадите живую связку <b>GitHub → Telegram бот</b>.",
          "The antiquated pattern of asking the server every 5 seconds <i>\"Any new data?\"</i> (Polling) "
          "wastes bandwidth, compute, and power. Modern distributed systems rely on <b>Event-Driven</b> architecture: "
          "the moment a state change occurs, the provider executes an HTTP callback into our listener — "
          "this is a <b>Webhook (Reverse API)</b>. Today you master <b>HMAC SHA-256 cryptographic verification</b>, "
          "<b>Idempotency</b>, and wire a real-time <b>GitHub-to-Telegram automation bridge</b>."),
    meta=[("<b>Fan:</b> Vibecoding · Event-Driven Arxitektura",
           "<b>Предмет:</b> Vibecoding · Событийная Архитектура",
           "<b>Subject:</b> Vibecoding · Event-Driven Architecture"),
          ("<b>Kohorta:</b> 9-sinf Junior Vibecoder",
           "<b>Когоrta:</b> 9 класс Junior Vibecoder",
           "<b>Cohort:</b> Grade 9 Junior Vibecoder"),
          ("<b>Hafta:</b> 4 (3-soat)", "<b>Неделя:</b> 4 (3-й час)", "<b>Week:</b> 4 (Hour 3)")],
))

# 2. Polling vs Webhooks
S.append(slide(
    ph=("Arxitektura", "Архитектура", "Architecture"), time="3–6",
    eyebrow=("Arxitektura taqqoslovi", "Сравнение архитектур", "Architectural comparison"),
    title=("Polling vs Webhook: Nega Dunyo Webhookga O'tdi?",
           "Polling против Webhook: Почему Индустрия Выбрала Вебхуки?",
           "Polling vs Webhooks: The Paradigm Shift to Event-Driven"),
    body='<div class="cols c2">\n'
         + box("accent", ("Klassik Polling (Muntazam So'rash)",
                          "Классический Polling (Постоянный опрос)",
                          "Classic Polling (Periodic Request)"),
               items=[
                   ("<b>99% bo'sh trafik:</b> Mijoz har 3 soniyada so'raydi: `GET /orders/new`. 99.9% holatda javob: `[]` (bo'sh).",
                    "<b>99% пустых запросов:</b> Клиент опрашивает сервер каждые 3 сек: `GET /orders/new`. В 99.9% ответ пуст.",
                    "<b>99% wasted bandwidth:</b> Client polls `GET /orders/new` every 3s. Over 99% of responses return empty arrays."),
                   ("<b>Kechikish (Latency):</b> Agar xarid so'rov tugaganidan 100ms keyin sodir bo'lsa, xaridor keyingi so'rovgacha (3 sek) kutadi.",
                    "<b>Задержка:</b> Если событие произошло через 100мс после опроса, клиент ждёт следующий цикл (3 сек).",
                    "<b>Inherent latency:</b> Events occurring right after a poll cycle must wait until the next tick."),
                   ("<b>Serverning qulashi:</b> 10 000 ta foydalanuvchi bir vaqtda doimiy so'rov yuborsa, API server qulab tushadi.",
                    "<b>Перегрузка сервера:</b> 10 000 клиентов создают миллионы паразитных запросов в минуту.",
                    "<b>Server DDOS:</b> 10,000 active clients hammer the gateway with millions of unnecessary requests per hour."),
               ])
         + "\n"
         + box("green", ("Webhook Arxitekturasi (Hodisa Chaqiruvi)",
                         "Архитектура Webhook (Вызов по событию)",
                         "Webhook Architecture (Event Callbacks)"),
               items=[
                   ("<b>0% ortiqcha yuklama:</b> Hodisa bo'lmaguncha hech kim so'rov yubormaydi. Tarmoq 100% tinch.",
                    "<b>0% паразитной нагрузки:</b> Пока событий нет, сеть и процессор полностью свободны.",
                    "<b>Zero idle chatter:</b> Zero HTTP requests transpire until a concrete domain event fires."),
                   ("<b>Real-vaqt (Sub-sekund):</b> To'lov o'tishi bilanoq provayder bizning `/webhook` endpointimizga `POST` yuboradi.",
                    "<b>Мгновенно:</b> В момент оплаты платежный шлюз мгновенно шлёт `POST` на наш URL.",
                    "<b>Sub-second delivery:</b> Upstream services push `POST` payloads within milliseconds of event execution."),
                   ("<b>Inversion of Control:</b> Endi biz mijoz emasmiz — biz servermiz, tashqi gigant (GitHub, Stripe) esa bizga xabar yetkazadi.",
                    "<b>Инверсия контроля:</b> Теперь мы не опрашиваем, а выступаем слушателем для GitHub или Stripe.",
                    "<b>Inversion of control:</b> We expose an ingestion listener; enterprise providers act as our clients."),
               ])
         + "\n</div>",
))

# 3. Webhook HTTP Anatomy
S.append(slide(
    ph=("Protokol", "Протокол", "Protocol"), time="6–9",
    eyebrow=("HTTP anatomiya", "Анатомия HTTP", "HTTP anatomy"),
    title=("Webhook HTTP So'rovi: Sarlavha va Payload",
           "Анатомия Webhook-Запроса: Заголовки и Payload",
           "Webhook HTTP Anatomy: Headers & Event Payload"),
    body='<div class="cols c2">\n'
         + code("""POST /webhook/github HTTP/1.1
Host: api.target.uz
User-Agent: GitHub-Hookshot/7b63f21
Content-Type: application/json
X-GitHub-Delivery: 72d3162e-cc78-11ee-818b-0242ac120002
X-GitHub-Event: push
X-Hub-Signature-256: sha256=d57c2a498b...

{
  "ref": "refs/heads/main",
  "repository": { "name": "cyber-core", "owner": { "name": "target" } },
  "pusher": { "name": "jasur_dev", "email": "jasur@target.uz" },
  "commits": [
    { "id": "f8a12c4", "message": "feat: add payment gateway webhook" }
  ]
}""")
         + "\n"
         + box("ink", ("Kritik Sarlavhalar (HTTP Headers)", "Критические Заголовки", "Essential HTTP Headers"),
               items=[
                   ("<b>X-GitHub-Event:</b> Qaysi hodisa yuz berganini bildiradi (`push`, `pull_request`, `issues`, `release`).",
                    "<b>X-GitHub-Event:</b> Тип события (`push`, `pull_request`, `issues`, `release`).",
                    "<b>X-GitHub-Event:</b> Declares event type (`push`, `pull_request`, `issues`, `release`)."),
                   ("<b>X-GitHub-Delivery:</b> Har bir so'rovning unikal UUID raqami (Idempotentlik uchun muhim).",
                    "<b>X-GitHub-Delivery:</b> Уникальный UUID конкретной доставки события (для идемпотентности).",
                    "<b>X-GitHub-Delivery:</b> Unique UUID identifying this single dispatch attempt."),
                   ("<b>X-Hub-Signature-256:</b> Payloadning kriptografik imzosi (Hujumchilardan himoya).",
                    "<b>X-Hub-Signature-256:</b> Криптографическая подпись данных (защита от спуфинга).",
                    "<b>X-Hub-Signature-256:</b> HMAC-SHA256 signature calculated over the raw body payload."),
                   ("<b>200 OK Qoidasi:</b> Listener 5 soniya ichida `200 OK` qaytarmasa, provayder so'rovni bekor qilingan deb qayta yuboradi (Retry).",
                    "<b>Правило 200 OK:</b> Если сервер не ответит за 5 сек, провайдер начнёт повторную отправку.",
                    "<b>Strict 200 OK:</b> Listener must ACK with HTTP 200 within ~5s, or upstream initiates retry storm."),
               ])
         + "\n</div>",
))

# 4. Cybersecurity: HMAC SHA-256 Signature Verification
S.append(slide(
    ph=("Xavfsizlik", "Безопасность", "Security"), time="9–13",
    eyebrow=("Kriptografik himoya", "Криптографическая защита", "Cryptographic verification"),
    title=("HMAC SHA-256: Soxta Webhooklarni Fosh Qilish",
           "HMAC SHA-256: Распознавание Поддельных Вебхуков",
           "HMAC SHA-256: Defending Against Spoofed Webhooks"),
    body='<div class="cols c2">\n'
         + code("""const crypto = require('crypto');

function verifySignature(req, webhookSecret) {
  const signature = req.headers['x-hub-signature-256'];
  if (!signature) return false;

  // 1. Secret kalit va Raw Body asosida hash hisoblash
  const hmac = crypto.createHmac('sha256', webhookSecret);
  const digest = 'sha256=' + hmac.update(req.rawBody).digest('hex');

  // 2. Timing attackdan himoyalangan xavfsiz solishtirish
  const trustedBuffer = Buffer.from(digest, 'ascii');
  const untrustedBuffer = Buffer.from(signature, 'ascii');

  if (trustedBuffer.length !== untrustedBuffer.length) return false;
  return crypto.timingSafeEqual(trustedBuffer, untrustedBuffer);
}""")
         + "\n"
         + box("accent", ("Nega Oddiy Solishtirish (===) Xavfli?",
                          "Почему Обычное Сравнение (===) Опасно?",
                          "Why Primitive Equality (===) Fails"),
               items=[
                   ("<b>Hujumchi ssenariysi:</b> Hujumchi sizning `/webhook` manzilingizga soxta `POST` yuborib, o'z hisobiga 100 000$ tushirishi mumkin!",
                    "<b>Сценарий атаки:</b> Злоумышленник шлёт фейковый `POST` на ваш URL и начисляет себе баланс.",
                    "<b>Spoofing attack:</b> An attacker POSTs fake payment payloads to credit arbitrary balances."),
                   ("<b>Timing Attack (Vaqt tahlili):</b> `===` operatori birinchi noto'g'ri belgidayoq to'xtaydi. Xaker javob vaqtini nanosekundlarda o'lchab sirni topadi.",
                    "<b>Timing Attack:</b> Оператор `===` прерывается на первом несовпавшем символе, выдавая хэш по времени.",
                    "<b>Timing side-channel:</b> Native `===` short-circuits early, allowing attackers to deduce the HMAC byte-by-byte."),
                   ("<b>timingSafeEqual kafolati:</b> Xakerning imzosini solishtirishda doim bir xil vaqt sarflaydi va kiber-hujumni 100% yo'qqa chiqaradi.",
                    "<b>timingSafeEqual:</b> Всегда сравнивает байты за строго постоянное время, исключая утечку.",
                    "<b>Constant-time guarantee:</b> `crypto.timingSafeEqual` executes in constant time across all inputs."),
               ])
         + "\n</div>",
))

# 5. Idempotency & Duplicate Deliveries
S.append(slide(
    ph=("Idempotentlik", "Идемпотентность", "Idempotency"), time="13–16",
    eyebrow=("Takroriy yetkazib berish", "Повторная доставка", "Duplicate delivery protection"),
    title=("Idempotentlik: Bitta To'lovni 3 Marta Yechmaslik",
           "Идемпотентность: Защита от Двойных Списаний",
           "Idempotency: Preventing Double-Billing from Retries"),
    body='<div class="cols c2">\n'
         + box("accent", ("Tarmoqdagi nosozlik va Retry muammosi",
                          "Сетевые сбои и проблема Retry",
                          "Network faults and retry storms"),
               items=[
                   ("<b>At-Least-Once Delivery:</b> Webhook provayderlari ma'lumot yo'qolmasligi uchun uni <b>kamida bir marta</b> yetkazishni kafolatlaydi.",
                    "<b>At-Least-Once:</b> Провайдер гарантирует доставку <b>минимум один раз</b>, но может прислать дубль.",
                    "<b>At-least-once delivery:</b> Providers guarantee minimum delivery, which inherently causes duplicates."),
                   ("<b>Kutilmagan stsenariy:</b> Bizning server to'lovni qabul qildi va balansni to'ldirdi, lekin internet uzilib provayderga 200 OK yetib bormadi.",
                    "<b>Сбой отправки 200 OK:</b> Мы обработали оплату, но ответ 200 OK застрял в сети из-за таймаута.",
                    "<b>Lost ACKs:</b> The server processes payment, but network drops before HTTP 200 reaches the provider."),
                   ("<b>Provayder takrorlaydi:</b> Provayder yana 2 marta xuddi shu so'rovni jo'natadi. Agar himoyalanmasak, mijozdan 3 barobar pul yechiladi!",
                    "<b>Шторм повторов:</b> Провайдер шлёт хук повторно. Без защиты баланс начислится трижды!",
                    "<b>Catastrophic repeats:</b> Upstream retries 2 more times; naive code charges the customer 3x!"),
               ])
         + "\n"
         + box("green", ("Idempotency Kaliti va Baza Tekshiruvi",
                         "Ключ Идемпотентности и База Данных",
                         "Idempotency Keys and State Deduplication"),
               items=[
                   ("<b>Delivery ID ni bazada saqlash:</b> Har bir qabul qilingan `X-GitHub-Delivery` yoki `payment_intent_id` bazaga yoziladi.",
                    "<b>Фиксация Delivery ID:</b> Уникальный ID хука сразу записывается в базу данных с уникальным индексом.",
                    "<b>Record delivery IDs:</b> Insert `X-GitHub-Delivery` into a `processed_events` table with a UNIQUE constraint."),
                   ("<b>Takrorlansa o'tkazib yuborish:</b> Agar shu ID avval ko'rilgan bo'lsa, og'ir biznes-mantiq ishlatilmaydi, darhol `200 OK` qaytariladi.",
                    "<b>Игнорирование дублей:</b> Если ID уже есть в базе, повторная логика пропускается, сразу отдаётся `200 OK`.",
                    "<b>Fast short-circuit:</b> If ID exists, skip state mutations and immediately reply `200 OK`."),
                   ("<b>Oltin qoida:</b> 1 ta so'rov 10 marta kelsa ham, tizim holati faqat 1 marta o'zgarishi shart.",
                    "<b>Золотое правило:</b> Сколько бы раз ни пришёл один и тот же вебхук, состояние меняется ровно один раз.",
                    "<b>Idempotent invariant:</b> Applying the same webhook N times yields identical state to applying it once."),
               ])
         + "\n</div>",
))

# 6. Architecture: Asynchronous Webhook Workers
S.append(slide(
    ph=("Arxitektura", "Архитектура", "Queues"), time="16–19",
    eyebrow=("Masshtablanuvchi arxitektura", "Масштабируемая архитектура", "Scalable queues"),
    title=("Asinxron Navbatlar: Nega 200 OK Darhol Qaytadi?",
           "Асинхронные Очереди: Почему 200 OK Отдают Сразу?",
           "Asynchronous Decoupling: Ingest Fast, Process in Queue"),
    body='<div class="cols c2">\n'
         + code("""// ❌ XATO: Webhook ichida og'ir ish qilish (Timeout xavfi)
app.post('/webhook', async (req, res) => {
  await generatePdfInvoice(req.body); // 8 soniya oladi!
  await sendEmailNotification(req.body); // 3 soniya!
  res.status(200).send('OK'); // Provayder allaqachon timeout qildi!
});

// ✅ TO'G'RI: Darhol qabul qilish va navbatga (Queue) qo'yish
app.post('/webhook', async (req, res) => {
  if (!verifySignature(req)) return res.status(401).end();
  
  // 1. Ishni fon navbatiga (BullMQ / Redis) topshiramiz (1ms)
  await eventQueue.add('process_payment', req.body);
  
  // 2. Provayderga darhol 200 OK qaytaramiz (50ms)
  res.status(200).json({ received: true });
});""")
         + "\n"
         + box("ink", ("Arxitekturaning 3 Ta Afzalligi", "3 Преимущества Архитектуры", "3 Architectural Virtues"),
               items=[
                   ("<b>Hech qachon timeout bermaydi:</b> GitHub yoki Stripe 5 soniya kutadi. Biz esa 50 millisekundda javob beramiz.",
                    "<b>Никаких таймаутов:</b> Сервис отвечает за 50мс, легко укладываясь в 5-секундный лимит провайдера.",
                    "<b>Zero timeouts:</b> Acknowledging in 50ms safely beats the 5-second upstream timeout window."),
                   ("<b>Spike Absorbatsiya (Zarba yutish):</b> Birdaniga 5 000 ta webhook kelsa, server qulab tushmaydi — barchasini navbatga yozib oladi.",
                    "<b>Гашение пиковых нагрузок:</b> Внезапные тысячи вебхуков буферизуются в Redis без падения основного сервиса.",
                    "<b>Load shedding & buffering:</b> Ingest thousands of events during flash traffic spikes without CPU saturation."),
                   ("<b>Dead Letter Queue (DLQ):</b> Xato yuz bergan so'rovlar yo'qolmaydi, alohida karantin navbatiga o'tadi va tuzatilgach qayta ishlanadi.",
                    "<b>Dead Letter Queue:</b> Упавшие задачи не теряются, а оседают в очереди ошибок для ручного ретрая.",
                    "<b>Dead Letter Queues (DLQ):</b> Poison messages migrate to quarantine queues for inspection and safe replays."),
               ])
         + "\n</div>",
))

# 7. Building a Real Node.js Webhook Server
S.append(slide(
    ph=("Qurish", "Разработка", "Implementation"), time="19–22",
    eyebrow=("Amaliy backend kod", "Практический бэкенд код", "Practical implementation"),
    title=("Node.js da Xavfsiz Webhook Listener Qurish",
           "Создание Безопасного Webhook-Сервера на Node.js",
           "Building a Production Webhook Ingestion Listener"),
    body='<div class="cols c2">\n'
         + code("""const express = require('express');
const crypto = require('crypto');
const app = express();

// DIQQAT: Signature tekshirish uchun Raw Body kerak!
app.use(express.json({
  verify: (req, res, buf) => { req.rawBody = buf; }
}));

const SECRET = process.env.GITHUB_WEBHOOK_SECRET;

app.post('/api/github-webhook', (req, res) => {
  const sig = req.headers['x-hub-signature-256'];
  const hmac = crypto.createHmac('sha256', SECRET);
  const digest = 'sha256=' + hmac.update(req.rawBody).digest('hex');

  if (sig !== digest) {
    console.warn('🚨 Kiber-ogohlantirish: Soxta webhook qaytarildi!');
    return res.status(401).send('Invalid signature');
  }

  const event = req.headers['x-github-event'];
  console.log(`✅ Qonuniy hodisa qabul qilindi: ${event}`);
  res.status(200).send({ status: 'success' });
});""")
         + "\n"
         + box("green", ("Amaliyot Qoidalari", "Правила Разработки", "Implementation Rules"),
               items=[
                   ("<b>Raw Body saqlab qolinishi shart:</b> JSON parse qilingan obyekt orqali HMAC hisoblansa hash mutlaqo to'g'ri chiqmaydi!",
                    "<b>Сохраняйте Raw Body:</b> Если считать хэш от распарсенного JSON, сигнатура не сойдётся из-за пробелов.",
                    "<b>Preserve raw bytes:</b> Computing HMAC over parsed JSON objects fails due to key ordering and whitespace discrepancies."),
                   ("<b>Secretni `.env` da saqlang:</b> Webhook secret kalitini hech qachon ochiq kodda Gitga yuklamang.",
                    "<b>Секреты только в .env:</b> Никогда не коммитьте секретный ключ вебхука в публичный репозиторий.",
                    "<b>Guard secrets in `.env`:</b> Never hardcode or commit shared webhook secrets to source control."),
               ])
         + "\n</div>",
))

# 8. Real-World Telegram Bot Bridge
S.append(slide(
    ph=("Integratsiya", "Интеграция", "Integration"), time="22–25",
    eyebrow=("Jonli xabarnoma", "Живые уведомления", "Live notifications"),
    title=("GitHub Webhook → Telegram Kiber-Bot Ko'prigi",
           "Мост GitHub Webhook → Telegram Кибер-Бот",
           "Event Pipeline: GitHub Webhook to Telegram Bot"),
    body='<div class="cols c2">\n'
         + code("""// GitHub Push hodisasini Telegramga yo'naltirish
async function notifyTelegram(payload) {
  const repoName = payload.repository.name;
  const author = payload.pusher.name;
  const commitMsg = payload.commits[0]?.message || 'No msg';
  const branch = payload.ref.replace('refs/heads/', '');

  const text = `🚀 <b>Yangi Commit Gitga Push Qilindi!</b>\\n` +
               `📦 <b>Repo:</b> ${repoName} (<code>${branch}</code>)\\n` +
               `👤 <b>Muallif:</b> ${author}\\n` +
               `💬 <b>Xabar:</b> ${commitMsg}`;

  const botToken = process.env.TELEGRAM_BOT_TOKEN;
  const chatId = process.env.TELEGRAM_CHAT_ID;

  await fetch(`https://api.telegram.org/bot${botToken}/sendMessage`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ chat_id: chatId, text, parse_mode: 'HTML' })
  });
}""")
         + "\n"
         + box("ink", ("To'liq Avtomatlashtirish Zanjiri", "Цепочка Автоматизации", "Complete Automation Flow"),
               items=[
                   ("<b>1. Dasturchi kod yozadi:</b> `git push origin main` buyrug'ini terminalda bajaradi.",
                    "<b>1. Разработчик пушит:</b> Вводит `git push origin main` в терминале рабочей станции.",
                    "<b>1. Developer push:</b> Engineer pushes commits to GitHub via git CLI."),
                   ("<b>2. GitHub Webhook yuboradi:</b> Millisekund ichida bizning xavfsiz URL listenerimizga POST so'rovi yetib keladi.",
                    "<b>2. Вызов Webhook:</b> GitHub за миллисекунды отправляет POST-запрос с сигнатурой на наш сервер.",
                    "<b>2. Webhook triggers:</b> GitHub dispatches an HMAC-signed POST payload to our ingest URL."),
                   ("<b>3. Imzo tekshiriladi:</b> Server hash to'g'riligini tasdiqlaydi va Telegram API ga xabar yo'llaydi.",
                    "<b>3. Проверка и отправка:</b> Сервер валидирует HMAC и мгновенно шлёт алерт в Telegram.",
                    "<b>3. HMAC check & dispatch:</b> Listener verifies authenticity and triggers Telegram Bot message."),
                   ("<b>4. Jamoa xabardor bo'ladi:</b> 1 soniya ichida butun guruh kim qaysi faylni o'zgartirganini ko'radi.",
                    "<b>4. Команда в курсе:</b> Меньше чем за 1 секунду вся команда видит автора и суть изменений.",
                    "<b>4. Instant sync:</b> The entire engineering squad receives formatted telemetry in under 1 second."),
               ])
         + "\n</div>",
))

# 9. Mission Briefing
S.append(slide(
    ph=("Amaliyot", "Практика", "Hands-on"), time="25–28",
    eyebrow=("12 daqiqalik laboratoriya", "12-минутная лаборатория", "12-minute lab"),
    title=("Amaliy Missiya: Webhook Listener va Telegram Integratsiya",
           "Практическая Миссия: Сервер Вебхуков и Telegram-Бот",
           "Hands-on Mission: Webhook Listener & Telegram Bot Integration"),
    body='<div class="cols c2">\n'
         + box("accent", ("Missiya topshiriqlari", "Задачи миссии", "Mission requirements"),
               items=[
                   ("<b>1. Mahalliy Server:</b> Node.js da `/webhook` endpointini ishga tushiring.",
                    "<b>1. Локальный сервер:</b> Запустите Node.js сервер с эндпоинтом `/webhook`.",
                    "<b>1. Ingestion Endpoint:</b> Spin up a Node.js listener exposing `/webhook`."),
                   ("<b>2. Tunnel Yaratish:</b> Cloudflare Tunnel yoki ngrok orqali serveringizni tashqi internetga oching (`https://...`).",
                    "<b>2. Туннель:</b> Откройте локальный порт в интернет через Cloudflare Tunnel или ngrok.",
                    "<b>2. Public Tunnel:</b> Expose local port via Cloudflare Tunnel or ngrok with HTTPS."),
                   ("<b>3. GitHub Webhook Sozlash:</b> Repongizda Webhook oching, Secret kalit kiriting va `push` hodisasini tanlang.",
                    "<b>3. Настройка GitHub:</b> Добавьте Webhook в репозиторий с Secret-ключом на событие `push`.",
                    "<b>3. GitHub Webhook Config:</b> Add webhook to your repository with shared Secret on `push`."),
                   ("<b>4. HMAC Tekshiruvi:</b> Soxta so'rov kelganda 401 Unauthorized qaytishini, haqiqiy push kelganda 200 OK qaytishini tekshiring.",
                    "<b>4. Проверка HMAC:</b> Убедитесь, что фейковый запрос блокируется (401), а настоящий отдаёт 200 OK.",
                    "<b>4. Security Audit:</b> Verify fake requests return 401 Unauthorized, and genuine pushes return 200 OK."),
               ])
         + "\n"
         + box("ink", ("Laboratoriya Vositalari", "Инструменты Лаборатории", "Workstation Toolchain"),
               items=[
                   ("<b>CLI buyruqlari:</b> `node server.js` va `ngrok http 3000` (yoki `cloudflared tunnel`).",
                    "<b>Команды:</b> `node server.js` и `ngrok http 3000` (или `cloudflared tunnel`).",
                    "<b>CLI Commands:</b> `node server.js` and `ngrok http 3000` (or `cloudflared tunnel`)."),
                   ("<b>Qog'oz varaqa:</b> Olingan Webhook Payload ma'lumotlarini qog'oz ish varaqasiga qayd qiling.",
                    "<b>Рабочий лист:</b> Зафиксируйте заголовки и Delivery ID в распечатанном бланке.",
                    "<b>Telemetry worksheet:</b> Log incoming event delivery IDs and HMAC verification outcomes."),
               ])
         + "\n</div>",
))

# 10. Live Timer
S.append(slide(
    ph=("Taymer", "Таймер", "Timer"), time="28–37",
    eyebrow=("Mustaqil amaliy ish", "Самостоятельная работа", "Independent lab"),
    title=("Laboratoriya Ishi: 12 Daqiqa",
           "Лабораторная Работа: 12 Минут",
           "Laboratory Execution: 12 Minutes"),
    body='<div class="timer-card" data-timer="720">\n'
         + '  <div class="timer-display">12:00</div>\n'
         + '  <div class="timer-controls">\n'
         + '    <button class="navbtn" data-action="start" '
         + i18n("Boshlash", "Старт", "Start") + '>Boshlash</button>\n'
         + '    <button class="navbtn" data-action="pause" '
         + i18n("Pauza", "Пауза", "Pause") + '>Pauza</button>\n'
         + '    <button class="navbtn" data-action="reset" '
         + i18n("Qaytarish", "Сброс", "Reset") + '>Qaytarish</button>\n'
         + '  </div>\n'
         + '  <p style="color:var(--ink-2); font-size:13px; margin-top:14px;" '
         + i18n("Serverni ishga tushiring, tunnel orqali webhookni ulang va Git push qilib test qiling.",
                "Запустите сервер, подключите вебхук через туннель и протестируйте через git push.",
                "Spin up server, tunnel webhook endpoint, and verify dispatch via git push.")
         + ">Serverni ishga tushiring, tunnel orqali webhookni ulang va Git push qilib test qiling.</p>\n"
         + '</div>',
))

# 11. Security Post-Mortem: Webhook Failures
S.append(slide(
    ph=("Xavfsizlik", "Анализ", "Post-Mortem"), time="37–41",
    eyebrow=("Haqiqiy hodisalar tahlili", "Анализ реальных инцидентов", "Real-world incident post-mortem"),
    title=("Webhooklar Qachon Tizimni Qulatadi? Post-Mortem",
           "Когда Вебхуки Ломают Продакшен? Post-Mortem",
           "When Webhooks Crash Production: Incident Post-Mortem"),
    body='<div class="cols c2">\n'
         + box("accent", ("3 Ta Katta Xatolik (Sanoat Xatoliklari)",
                          "3 Фатальные Ошибки в Индустрии",
                          "3 Fatal Industry Mistakes"),
               items=[
                   ("<b>1. Imzosiz ochiq endpoint:</b> Dasturchi HMAC tekshirmasdan webhook qabul qilgan. Hujumchi soxta xarid signallari yuborib do'konni talagan.",
                    "<b>1. Открытый эндпоинт:</b> Приём хуков без HMAC. Хакер прислал фейк об оплате и получил товар бесплатно.",
                    "<b>1. Unsigned endpoints:</b> Ingesting webhooks without HMAC verification allows attackers to spoof payments."),
                   ("<b>2. Sinxron bloklanish:</b> Webhook ichida og'ir fayl yaratilib, provayderga 5 soniyada javob berilmagan. Natijada provayder 1 000 ta retry bilan serverni o'ldirgan.",
                    "<b>2. Синхронные операции:</b> Сервер не успел ответить за 5 сек; провайдер завалил его лавиной повторов (Retry Storm).",
                    "<b>2. Synchronous blockage:</b> Slow internal work causes timeout, prompting upstream to trigger a crushing retry storm."),
                   ("<b>3. Idempotentlik yo'qligi:</b> Xaridor hisobidan 1 marta pul yechilishi o'rniga, takroriy webhook tufayli 3 marta yechilgan.",
                    "<b>3. Отсутствие идемпотентности:</b> Из-за повторной доставки вебхука с пользователя списали деньги трижды.",
                    "<b>3. Missing deduplication:</b> Network hiccups duplicate payloads, leading to catastrophic duplicate billing."),
               ])
         + "\n"
         + box("green", ("Muhandisning Xavfsizlik Qonunlari", "Законы Безопасности Инженера", "Engineering Hardening Rules"),
               items=[
                   ("<b>Har doim HMAC:</b> Imzosi to'g'ri kelmagan bironta ham baytni biznes mantiqqa o'tkazmang.",
                    "<b>Всегда HMAC:</b> Ни байта данных без валидной криптографической подписи.",
                    "<b>Mandatory HMAC:</b> Discard any payload failing constant-time cryptographic signature checks."),
                   ("<b>Darhol 200 OK:</b> Og'ir ishlarni navbatga o'tkazib, provayderga millisekundlarda javob bering.",
                    "<b>Мгновенный 200 OK:</b> Буферизуйте задачи в очередь и отдавайте статус 200 без задержек.",
                    "<b>Immediate 200 OK:</b> Push jobs to background workers and respond with 200 OK in sub-100ms."),
                   ("<b>Delivery ID bilan tekshirish:</b> Har bir so'rov ID si bazada tekshirilmaguncha amal bajarilmasin.",
                    "<b>Проверка Delivery ID:</b> Убедитесь, что ID события ещё не обрабатывался ранее.",
                    "<b>Deduplicate IDs:</b> Never mutate database state without verifying Delivery ID idempotency."),
               ])
         + "\n</div>",
))

# 12. Conclusion & Rubric
S.append(slide(
    ph=("Xulosa", "Итоги", "Conclusion"), time="41–45",
    eyebrow=("Dars yakuni va baholash", "Итоги урока и оценка", "Lesson recap & grading"),
    title=("Xulosa va Baholash Mezoni (10 Ball)",
           "Итоги и Критерии Оценки (10 Баллов)",
           "Key Takeaways & 10-Point Rubric"),
    body='<div class="cols c2">\n'
         + box("green", ("Bugungi asosiy xulosalar", "Главные выводы урока", "Core engineering principles"),
               items=[
                   ("<b>Polling o'rniga Webhook:</b> Hodisalarga asoslangan arxitektura resurslarni tejaydi va real-vaqt tezligini beradi.",
                    "<b>Webhook вместо Polling:</b> Событийная модель экономит ресурсы и обеспечивает мгновенную реакцию.",
                    "<b>Webhooks replace Polling:</b> Event-driven architecture minimizes idle overhead and delivers sub-second sync."),
                   ("<b>HMAC SHA-256 — qalqon:</b> Faqat rasmiy provayder yuborganligini kriptografik kafolatlaydi.",
                    "<b>HMAC SHA-256 — броня:</b> Гарантирует, что запрос пришёл именно от доверенного сервиса.",
                    "<b>HMAC SHA-256 integrity:</b> Cryptographically guarantees payloads originate strictly from authorized providers."),
                   ("<b>Idempotentlik — barqarorlik:</b> Takroriy so'rovlar tizim ma'lumotlarini buzmasligi shart.",
                    "<b>Идемпотентность — стабильность:</b> Повторные вебхуки никогда не должны дублировать операции.",
                    "<b>Idempotency assurance:</b> Redundant retry deliveries must never corrupt or duplicate financial/application state."),
                   ("<b>Asinxron navbatlar:</b> Listener tez javob berishi va ishlarni fonga yuklashi zarur.",
                    "<b>Очереди задач:</b> Приёмник вебхуков должен отвечать за миллисекунды, делегируя работу воркерам.",
                    "<b>Queue decoupling:</b> Ingest fast, decouple via Redis/BullMQ, and process intensive jobs asynchronously."),
               ])
         + "\n"
         + box("accent", ("10 Ballik Baholash Mezoni", "Критерии на 10 Баллов", "10-Point Grading Rubric"),
               items=[
                   ("<b>2 ball:</b> Polling vs Webhook va arxitektura tushunchasi.",
                    "<b>2 балла:</b> Понимание различий между Polling и Webhook.",
                    "<b>2 points:</b> Articulation of Polling vs Webhooks and event-driven benefits."),
                   ("<b>3 ball:</b> To'g'ri ishlovchi Node.js Webhook listener va tunnel sozlash.",
                    "<b>3 балла:</b> Работающий сервер вебхуков и настройка туннеля.",
                    "<b>3 points:</b> Functional Node.js webhook listener with public tunnel routing."),
                   ("<b>3 ball:</b> HMAC SHA-256 imzo tekshiruvi (timingSafeEqual bilan).",
                    "<b>3 балла:</b> Реализация проверки HMAC через timingSafeEqual.",
                    "<b>3 points:</b> HMAC SHA-256 verification using timingSafeEqual."),
                   ("<b>2 ball:</b> Idempotentlik tahlili va hodisani Telegramga yo'naltirish.",
                    "<b>2 балла:</b> Анализ идемпотентности и пересылка алерта в Telegram.",
                    "<b>2 points:</b> Idempotency reasoning and Telegram alert relay."),
               ])
         + "\n</div>",
))

# ----------------- SPEAKER NOTES (O'QITUVCHI UCHUN QO'LLANMA) -----------------
NOTES = {
    "uz": [
        ["Kirish", "Darsni zamonaviy ilovalarning bir-biri bilan qanday gaplashishidan boshlang: Instagram, Telegram, GitHub va to'lov tizimlari.", "Polling qilish nima uchun telefon quvvatini tez tugatishini misol qilib ko'rsating."],
        ["Polling vs Webhook", "Doskada ikkita modelni chizing: 1-modelda o'quvchi har 10 soniyada o'qituvchiga qarab 'Baho qo'ydingizmi?' deb so'raydi. 2-modelda o'qituvchi baho qo'yilgach o'zi chaqiradi.", "Resurs va vaqt tejalishini ko'rsating."],
        ["HTTP Anatomiya", "HTTP Headerlardagi X-GitHub-Delivery va X-GitHub-Event sarlavhalariga urg'u bering.", "5 soniyalik javob kutish qoidasini tushuntiring."],
        ["HMAC Kiberxavfsizlik", "Oddiy paroldan ko'ra HMAC nega kuchliroq ekanini ayting: har bir so'rovning o'ziga xos imzosi bo'ladi.", "timingSafeEqual funksiyasi nega === o'rniga ishlatilishini uqtiring."],
        ["Idempotentlik", "Real bank misolini keltiring: bitta xarid uchun 2 marta SMS kelsa nima bo'ladi?", "Delivery ID orqali takroriy so'rovlarni filtrlashni doskada ko'rsating."],
        ["Asinxron Navbat", "Nega webhook ichida PDF yasab o'tirmaymiz? Chunki provayder kutmaydi va timeout beradi.", "Fast ACK (200 OK) va Background Queue modelini tushuntiring."],
        ["Node.js Listener", "Expressda Raw Body ni ushlab qolish kerakligini tushuntiring (express.json verify funksiyasi).", "O'quvchilar ko'p qiladigan xato: JSON stringify qilingan obyekt hashini hisoblash."],
        ["Telegram Integratsiya", "GitHub hodisasini Telegram Botga ulash skriptini ko'rsating.", "Bot tokeni va Chat ID qayerdan olinishini eslating."],
        ["Missiya", "Amaliy ishni boshlang. ngrok yoki cloudflared o'rnatilganligini tekshiring.", "12 daqiqalik taymerni yoqing."],
        ["Taymer", "Taymer vaqtida partalar bo'ylab aylanib, tunnel manzillari to'g'ri olinganini tekshiring.", "GitHub Webhook sozlamalarida 'Content-type: application/json' tanlanganini nazorat qiling."],
        ["Xavfsizlik Tahlili", "Post-mortem slaydida katta kompaniyalarning webhook tufayli yuz bergan nosozliklarini tushuntiring.", "Xavfsizlik qonunlarini qaytadan mustahkamlang."],
        ["Baholash", "O'quvchilarning ish varaqalarini yig'ib oling va 10 ballik mezon bo'yicha baholang.", "Kelgusi 20-darsda butun 4-haftaning kulminatsiyasi — Fullstack Deploy va Jonli Demo Day bo'lishini e'lon qiling!"]
    ],
    "ru": [
        ["Введение", "Начните с того, как сервисы общаются между собой в реальном мире: Telegram, GitHub, Stripe.", "Объясните на пальцах, почему Polling сажает батарею смартфона."],
        ["Polling vs Webhook", "Нарисуйте аналогию: дёргать учителя каждые 10 секунд с вопросом «Вы поставили оценку?» против звонка учителя, когда оценка готова.", "Покажите экономию трафика."],
        ["HTTP Анатомия", "Обратите внимание на заголовки X-GitHub-Delivery и X-GitHub-Event.", "Объясните жесткий лимит ожидания ответа в 5 секунд."],
        ["HMAC Кибербезопасность", "Разберите, почему HMAC надежнее обычного токена: подпись генерируется для каждого конкретного тела запроса.", "Подчеркните необходимость timingSafeEqual вместо ==="],
        ["Идемпотентность", "Приведите пример двойного списания денег в банке из-за сетевого сбоя.", "Покажите механизм дедупликации через уникальный Delivery ID."],
        ["Очереди", "Почему нельзя генерировать PDF внутри обработчика вебхука? Провайдер отвалится по таймауту.", "Объясните модель: быстрый 200 OK + задача в очередь Redis."],
        ["Node.js Listener", "Особое внимание уделите сохранению Raw Body в middleware Express.", "Предупредите типичную ошибку: хэширование уже распарсенного объекта."],
        ["Интеграция", "Покажите пайплайн от git push до сообщения в Telegram-группе.", "Напомните, как безопасно передавать секреты через переменные окружения."],
        ["Миссия", "Объявите условия миссии. Проверьте работоспособность туннелей (ngrok / cloudflared).", "Включите 12-минутный таймер."],
        ["Таймер", "Помогайте студентам с маршрутизацией туннелей и отладкой сигнатур.", "Следите, чтобы в GitHub был выбран формат application/json."],
        ["Анализ Сбоев", "Разберите реальные кейсы сбоев из-за шторма повторов (Retry Storm).", "Закрепите золотые правила продакшен-вебхуков."],
        ["Итоги", "Соберите рабочие листы, выставьте оценки по 10-балльной шкале.", "Анонсируйте финальный 20-й урок: Full-Stack Деплой и Demo Day!"]
    ],
    "en": [
        ["Introduction", "Introduce how distributed microservices communicate asynchronously.", "Explain how Polling exhausts mobile batteries and server bandwidth."],
        ["Polling vs Webhooks", "Diagram polling vs push callbacks. Contrast passive polling with event-driven triggers.", "Highlight bandwidth efficiency."],
        ["HTTP Anatomy", "Examine critical HTTP headers: X-GitHub-Delivery and X-Hub-Signature-256.", "Explain upstream 5-second timeout constraints."],
        ["HMAC Verification", "Deconstruct HMAC digest calculation. Contrast shared secret matching with body-derived hashes.", "Stress constant-time comparison via timingSafeEqual."],
        ["Idempotency", "Illustrate race conditions leading to double-billing during retry cycles.", "Show deduplication workflows using recorded event delivery IDs."],
        ["Queue Workers", "Explain why long-running tasks cannot block the synchronous request loop.", "Demonstrate instant 200 OK response followed by background worker processing."],
        ["Node.js Server", "Detail raw body preservation during JSON parsing in Express.", "Warn against hashing reconstructed JSON strings."],
        ["Telegram Bridge", "Review the end-to-end telemetry pipeline from git push to Telegram alert.", "Reiterate environment variable hygiene for bot credentials."],
        ["Mission Brief", "Announce lab targets. Verify local tunneling utilities (ngrok/cloudflared).", "Engage the 12-minute countdown timer."],
        ["Live Timer", "Walk the lab assisting students with tunnel ports and signature verification.", "Ensure GitHub webhook content type is explicitly configured to application/json."],
        ["Post-Mortem", "Review real-world outages caused by unhandled webhook retry storms and timing attacks.", "Solidify security best practices."],
        ["Grading", "Collect physical worksheets and grade against the 10-point rubric.", "Tease Lesson 20: Full-Stack Cloud Deployment and Live Demo Day!"]
    ]
}

# ----------------- WORKSHEET (VARAQA) -----------------
VARAQA = (
    sheet_header(
        ("19-dars. Vebhooklar va Avtomatlashtirish: Real-Vaqt Integratsiya va Kiber-Himoya",
         "Урок 19. Вебхуки и Автоматизация: Интеграция в Реальном Времени и Киберзащита",
         "Lesson 19. Webhooks & Event Automation: Real-Time Integration & HMAC Security"),
        ("9-sinf · 4-hafta (3-soat) · Event-Driven Track",
         "9 класс · 4-неделя (3-й час) · Event-Driven Track",
         "Grade 9 · Week 4 (Hour 3) · Event-Driven Track")
    )
    + "\n"
    + mission(
        ("Amaliy Missiya: Webhook Server Qurish, HMAC Tekshiruvi va Telegram Bot Integratsiyasi",
         "Практическая Миссия: Сервер Вебхуков, Валидация HMAC и Интеграция с Telegram",
         "Hands-on Mission: Webhook Listener Ingestion, HMAC Verification, and Telegram Bot Alerting"),
        ("1. Express/Node.js da `/webhook` endpointini oching va unga tunnel orqali HTTPS manzil bering.\n"
         "2. GitHub repongizda `push` hodisasi uchun Webhook va Secret kalitni sozlang.\n"
         "3. `crypto.timingSafeEqual` bilan HMAC SHA-256 tekshiruvini amalga oshiring.\n"
         "4. Repoga bitta commit push qilib, jonli hodisani qabul qiling va Telegram botga ma'lumot jo'nating.\n"
         "5. Delivery ID va tekshiruv natijalarini quyidagi laboratoriya jadvaliga yozing.",
         "1. Запустите эндпоинт `/webhook` на Node.js и откройте HTTPS через туннель.\n"
         "2. Настройте Webhook в репозитории GitHub на событие `push` с секретным ключом.\n"
         "3. Реализуйте валидацию HMAC SHA-256 через `crypto.timingSafeEqual`.\n"
         "4. Сделайте push в репозиторий, поймайте событие и отправьте оповещение в Telegram.\n"
         "5. Заполните Delivery ID и параметры проверки в таблицу ниже.",
         "1. Author a Node.js `/webhook` endpoint and route public HTTPS traffic via a tunnel.\n"
         "2. Configure a GitHub Webhook with a secret key targeting `push` events.\n"
         "3. Implement HMAC SHA-256 validation utilizing `crypto.timingSafeEqual`.\n"
         "4. Push a commit to your repo, ingest the live event, and dispatch an alert to Telegram.\n"
         "5. Record delivery telemetry and verification metrics in the table below.")
    )
    + "\n"
    + table(
        [("Bosqich", "Этап", "Stage"),
         ("Sozlama / Buyruq", "Настройка / Команда", "Configuration / Command"),
         ("Kutilgan Natija / Tekshiruv", "Ожидаемый Результат / Проверка", "Expected Telemetry / Check")],
        [
            [("1 · Tunnel", "1 · Туннель", "1 · Tunnel"),
             ("ngrok http 3000 || cloudflared tunnel",
              "ngrok http 3000 || cloudflared tunnel",
              "ngrok http 3000 || cloudflared tunnel"),
             ("Olingan ochiq URL: https://______________________________",
              "Публичный HTTPS URL: https://______________________________",
              "Public HTTPS URL: https://______________________________")],
            [("2 · Webhook", "2 · Вебхук", "2 · Webhook"),
             ("GitHub Repo → Settings → Webhooks",
              "GitHub Repo → Settings → Webhooks",
              "GitHub Repo → Settings → Webhooks"),
             ("Hodisa: [ push / PR ] · Secret kiritildimi? [ HA / YO'Q ]",
              "Событие: [ push / PR ] · Введён ли Secret? [ ДА / НЕТ ]",
              "Event: [ push / PR ] · Secret configured? [ YES / NO ]")],
            [("3 · Delivery", "3 · Доставка", "3 · Delivery"),
             ("git push origin main",
              "git push origin main",
              "git push origin main"),
             ("X-GitHub-Delivery (UUID): _______________________________",
              "X-GitHub-Delivery (UUID): _______________________________",
              "X-GitHub-Delivery (UUID): _______________________________")],
            [("4 · HMAC & Bot", "4 · HMAC и Бот", "4 · HMAC & Bot"),
             ("crypto.timingSafeEqual(trusted, untrusted)",
              "crypto.timingSafeEqual(trusted, untrusted)",
              "crypto.timingSafeEqual(trusted, untrusted)"),
             ("HTTP Status: 200 OK · Telegram xabar keldimi? [ HA / YO'Q ]",
              "HTTP Status: 200 OK · Пришёл ли алерт в Telegram? [ ДА / НЕТ ]",
              "HTTP Status: 200 OK · Telegram notification received? [ YES / NO ]")]
        ]
    )
    + "\n"
    + '    <div class="rubric-grid">\n'
    + sheet_box(
        ("✏️ Muhandislik Hisoboti",
         "✏️ Инженерный Отчёт",
         "✏️ Engineering Report"),
        writelines(2, ("Nega Polling o'rniga Webhook arxitekturasi tanlanadi (Tarmoq va Server jihatidan):",
                       "Почему Webhook эффективнее Polling (с точки зрения сети и нагрузки):",
                       "Why Webhooks outperform Polling (network bandwidth and server load):"))
        + "\n"
        + writelines(2, ("HMAC SHA-256 imzo tekshiruvi soxta webhooklarni qanday fosh qiladi:",
                         "Как криптографическая подпись HMAC защищает от поддельных вебхуков:",
                         "How HMAC SHA-256 signature verification stops spoofed webhooks:"))
        + "\n"
        + writelines(2, ("Idempotentlik qoidasi: takroriy webhook kelganda nima qilish kerak:",
                         "Принцип идемпотентности: как обрабатывать повторные запросы провайдера:",
                         "The idempotency rule: how to safely handle duplicate retry dispatches:"))
    )
    + "\n"
    + sheet_box(
        ("📊 Baholash Mezoni (10 Ball)",
         "📊 Критерии Оценки (10 Баллов)",
         "📊 Grading Rubric (10 Points)"),
        rubric([
            (("Polling vs Webhook arxitektura tushunchasi", "Понимание Polling против Webhook", "Polling vs Webhooks architecture"), "2"),
            (("Ishlovchi Webhook listener va tunnel", "Работающий Webhook listener и туннель", "Working Webhook listener & tunnel"), "3"),
            (("HMAC SHA-256 xavfsiz tekshiruvi", "Проверка подписи HMAC SHA-256", "HMAC SHA-256 verification"), "3"),
            (("Idempotentlik va Telegram bot integratsiyasi", "Идемпотентность и Telegram-интеграция", "Idempotency & Telegram relay"), "2"),
        ], "10")
    )
    + "\n    </div>\n  </div>\n"
    + sign_box()
)

if __name__ == "__main__":
    print(Lesson(D, TITLES, SHEET_TITLES, "vc-notes-9-19", S, NOTES, VARAQA).build())
