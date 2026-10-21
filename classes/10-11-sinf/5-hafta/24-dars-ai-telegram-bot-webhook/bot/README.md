# Target International School // 10–11-Sinf
## 24-Dars: Shaxsiy AI Telegram Bot (VS Code Port Forwarding + Webhook)

Ushbu loyiha yordamida o'z noutbukingizdan turib global internetda ishlaydigan va sun'iy intellekt (LLM) bilan bog'langan shaxsiy Telegram botingizni ishga tushirasiz.

---

### 1-Qadam: Telegram Bot Ochish (60 soniya)
1. Telegram'da rasmiy **`@BotFather`** botini qidiring va kiring.
2. `/newbot` buyrug'ini yuboring.
3. Botingizga nom bering (masalan: `Target AI Tutor`).
4. Botingizga noyob `@username` tanlang (oxiri albatta `bot` bilan tugashi shart, masalan: `my_target_ai_bot`).
5. `@BotFather` sizga **HTTP API Token** beradi (masalan: `7482910384:AAH...`). Ushbu tokenni saqlab oling!

---

### 2-Qadam: Loyihani O'rnatish
1. Ushbu papkani VS Code da oching.
2. Terminalda paketlarni o'rnating:
   ```bash
   npm install
   ```
3. `.env.example` faylidan nusxa olib `.env` nomli fayl yarating:
   ```bash
   cp .env.example .env
   ```
4. `.env` ichiga o'zingizning `TELEGRAM_BOT_TOKEN`ingizni qo'ying.

---

### 3-Qadam: Serverni Ishga Tushirish
Terminalda quyidagi buyruqni bering:
```bash
npm start
```
Server `http://localhost:3000` portida ishga tushadi.

---

### 4-Qadam: VS Code Port Forwarding (Microsoft Dev Tunnels)
1. VS Code ning pastki terminal qismida **"Ports"** yorlig'ini (tab) bosing.
2. **"Forward a Port"** tugmasini bosing va `3000` deb yozing.
3. Yangi hosil bo'lgan port qatori ustiga sichqonchaning o'ng tugmasini bosing:
   * **Port Visibility &rarr; Public** qilib o'zgartiring (Bu juda muhim! Aks holda Telegram xatolik beradi).
4. **Forwarded Address** ustunidagi `https://...devtunnels.ms` manzilini nusxalab oling.

---

### 5-Qadam: Telegramga Webhookni Ulash
Brauzeringizda quyidagi havolani oching (o'zingizning tokenni va devtunnel havolasini qo'ying):

```
https://api.telegram.org/bot<SIZNING_TOKEN>/setWebhook?url=https://<SIZNING_DEV_TUNNEL_URL>/webhook
```

Ekranda:
```json
{"ok": true, "result": true, "description": "Webhook was set"}
```
yozuvi chiqsa — tabriklaymiz, botingiz jonli internetga ulandi!

---

### 6-Qadam: Telefonda Sinov!
Telefonda o'zingiz yaratgan botga kiring va:
1. `/start` buyrug'ini yuboring.
2. Xohlagan savolingizni yozing.
3. VS Code terminalingizga qarang — u yerda Telegram yuborgan jonli paketlar va AI javobi ko'rinadi!
