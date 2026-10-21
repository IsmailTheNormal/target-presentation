/**
 * Target International School // 10–11-Sinf // 24-Dars
 * Mavzu: Shaxsiy AI Telegram Bot — Webhooklar, VS Code Port Forwarding va LLM Integratsiyasi
 * 
 * Ushbu server Telegram Webhook so'rovlarini qabul qiladi va
 * Groq / DeepSeek LLM orqali intellektual javob qaytaradi.
 */

require('dotenv').config();
const express = require('express');

const app = express();
app.use(express.json());

const PORT = process.env.PORT || 3000;
const TELEGRAM_TOKEN = process.env.TELEGRAM_BOT_TOKEN;
const GROQ_API_KEY = process.env.GROQ_API_KEY;
const SYSTEM_PROMPT = process.env.BOT_SYSTEM_PROMPT || 
  "Sen Target International School ning aqlli va do'stona AI assistentsan. Javoblaringni aniq, ixcham va o'zbek tilida ber.";

// 1. Server Holatini Tekshirish (Healthcheck)
app.get('/', (req, res) => {
  res.send(`
    <div style="font-family:sans-serif; text-align:center; padding:50px; background:#07152D; color:#F0F4FA; min-height:100vh;">
      <h1 style="color:#FF3B26;">Target AI Telegram Bot Serveri Ishlamoqda!</h1>
      <p style="font-size:18px; color:#A5B6D0;">VS Code Dev Tunnels muvaffaqiyatli ulandi.</p>
      <div style="display:inline-block; padding:12px 24px; background:#0E2246; border:1px solid #1B355A; border-radius:8px;">
        Webhook marshruti: <code>/webhook</code> (POST)
      </div>
    </div>
  `);
});

// 2. Telegram Webhook Qabul Qilish Marshruti
app.post('/webhook', async (req, res) => {
  // Telegram ga 200 OK qaytaramiz (aks holda Telegram qayta-qayta yuboraveradi)
  res.sendStatus(200);

  try {
    const update = req.body;
    console.log('📩 [Telegram Update]:', JSON.stringify(update, null, 2));

    // Xabar borligini tekshiramiz
    if (!update || !update.message || !update.message.text) {
      return;
    }

    const chatId = update.message.chat.id;
    const userText = update.message.text;
    const firstName = update.message.from.first_name || "O'quvchi";

    console.log(`👤 [${firstName}] (ID: ${chatId}): "${userText}"`);

    // Maxsus buyruqlarni tekshirish
    if (userText === '/start') {
      await sendTelegramMessage(chatId, 
        `Assalomu alaykum, ${firstName}! 👋\n\nMen Target International School da yaratilgan Shaxsiy AI Botman. Menga xohlagan savolingizni yozing, men sun'iy intellekt orqali javob beraman!`
      );
      return;
    }

    if (userText === '/help') {
      await sendTelegramMessage(chatId, 
        `💡 <b>Yordam Menyusi:</b>\n\n• Menga to'g'ridan-to'g'ri savol yozing\n• Men VS Code Port Forwarding orqali lokal kompyuterdan ishlayapman\n• Texnologiyalar: Node.js, Express, Webhook, Groq/DeepSeek LLM`
      );
      return;
    }

    // "Typing..." (Yozmoqda...) harakatini ko'rsatish
    await sendChatAction(chatId, 'typing');

    // AI dan javob olish
    const aiReply = await getAIResponse(userText, firstName);

    // Javobni Telegramga yuborish
    await sendTelegramMessage(chatId, aiReply);

  } catch (error) {
    console.error('❌ [Xatolik Webhookda]:', error.message);
  }
});

// 3. AI (Groq / OpenRouter / Fallback) bilan bog'lanish
async function getAIResponse(prompt, userName) {
  if (!GROQ_API_KEY || GROQ_API_KEY.includes('your_groq_api_key')) {
    // Agar API kalit kiritilmagan bo'lsa, aqlli ta'lim simulyatsiyasi
    return `🤖 [Target AI Simulyator]: Salom ${userName}! Sizning savolingiz: "${prompt}".\n\n(Haqiqiy Groq/DeepSeek API kalitini .env faylga qo'ysangiz, jonli LLM javob qaytaradi!)`;
  }

  try {
    const response = await fetch('https://api.groq.com/openai/v1/chat/completions', {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${GROQ_API_KEY}`,
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        model: 'llama-3.3-70b-versatile',
        messages: [
          { role: 'system', content: SYSTEM_PROMPT },
          { role: 'user', content: prompt }
        ],
        temperature: 0.7,
        max_tokens: 500
      })
    });

    const data = await response.json();
    if (data.choices && data.choices[0] && data.choices[0].message) {
      return data.choices[0].message.content;
    } else {
      return "Kechirasiz, sun'iy intellekt javob berishda to'xtaldi. Qaytadan urinib ko'ring.";
    }
  } catch (err) {
    console.error('❌ AI API xatosi:', err.message);
    return `AI bilan bog'lanishda xatolik yuz berdi: ${err.message}`;
  }
}

// 4. Telegram SendMessage funksiyasi
async function sendTelegramMessage(chatId, text) {
  if (!TELEGRAM_TOKEN) {
    console.error('❌ TELEGRAM_BOT_TOKEN topilmadi!');
    return;
  }

  const url = `https://api.telegram.org/bot${TELEGRAM_TOKEN}/sendMessage`;
  const response = await fetch(url, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      chat_id: chatId,
      text: text,
      parse_mode: 'HTML'
    })
  });

  const resData = await response.json();
  if (!resData.ok) {
    console.error('❌ Telegram xatosi:', resData.description);
  }
}

// 5. Telegram "Typing" aksiyasi
async function sendChatAction(chatId, action = 'typing') {
  if (!TELEGRAM_TOKEN) return;
  const url = `https://api.telegram.org/bot${TELEGRAM_TOKEN}/sendChatAction`;
  await fetch(url, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ chat_id: chatId, action: action })
  }).catch(() => {});
}

// 6. Serverni ishga tushirish
app.listen(PORT, () => {
  console.log(`
======================================================
🚀 Target AI Telegram Bot Serveri Ishga Tushdi!
📡 Lokal port: http://localhost:${PORT}
🔗 Webhook marshruti: http://localhost:${PORT}/webhook
======================================================
👉 QADAMLAR:
1. VS Code da "Ports" panelini oching (Ctrl + ~).
2. "Forward a Port" tugmasini bosing va ${PORT} deb yozing.
3. Port Visibility ni "Public" ga o'tkazing.
4. Microsoft devtunnels HTTPS manzilini oling.
5. Brauzerda quyidagi manzilni oching:
   https://api.telegram.org/bot<TOKEN>/setWebhook?url=<DEV_TUNNEL_URL>/webhook
======================================================
`);
});
