# 9-sinf: 30-dars — Real-Vaqt Texnologiyalari: WebSockets va LAN Kiber-Chat Engine
**Target International School · Yunusobod Filiali**
**O'qituvchi:** Ismoiljon Usmonov · **Format:** 80 Daqiqa (Double Block / Juftlik dars)

---

## 🎯 Dars Maqsadi va Asosiy Mohiyati
Ushbu 80 daqiqalik juftlik darsda 9-sinf o'quvchilari eskirgan, serverni zo'riqtiruvchi HTTP Polling modeli bilan xayrlashadilar va butun dunyo bo'ylab barcha jonli chatlar (Telegram, Discord) hamda multiplayer o'yinlar ishlatadigan **WebSockets (Full-Duplex TCP soket)** texnologiyasiga o'tadilar.

Sinfdagi kompyuterlar o'rtasida real-vaqt rejimida xabarlar almashinuvi yo'lga qo'yiladi va Chrome DevTools orqali freymlar (Opcodes `0x1 Text`, `0x8 Close`, `0x9 Ping`) bevosita tutib ko'riladi.

---

## ⏱️ 80 Daqiqalik Vaqt Taqsimoti (2 Bosqichli Reja)

### 1-Bosqich: Nazariya, Protokol va Jonli Simulyator (40 Daqiqa)
* **00:00 – 04:00 (4 min) | Kirish & Missiya:** Dars mavzusi va 10 ballik baholash mezonini e'lon qilish.
* **04:00 – 12:00 (8 min) | 29-Dars Tahlili (HW Review):** Asinxron JS va `setInterval(fetch, 1000)` polling xatosi tahlili. 30 soniyalik blits savol (`101 Switching Protocols`).
* **12:00 – 18:00 (6 min) | Real Muammo:** Nega HTTP real-vaqtda qulaydi? 1 soniyalik lag, 1 KB sarlavha isrofi va C10K server falokati.
* **18:00 – 24:00 (6 min) | WebSockets Konsepti:** 101 Handshake mexanizmi va doimiy ochiq full-duplex TCP tunnel.
* **24:00 – 30:00 (6 min) | Paketlar Anatomiyasi & DevTools:** Chrome DevTools -> Network -> WS filtri va Opcodes (`0x1 Text`, `0x8 Close`, `0x9 Ping`).
* **30:00 – 35:00 (5 min) | Server Arxitekturasi:** Node.js `ws` serveri va `wss.clients.forEach` broadcast tsikli.
* **35:00 – 40:00 (5 min) | Klient Hayot Tsikli:** `new WebSocket()`, `onopen`, `onmessage`, `onclose` va auto-reconnect.

### 2-Bosqich: Jonli Tajriba, Kiber-Arena va Demos (40 Daqiqa)
* **40:00 – 48:00 (8 min) | Jonli Slayd Simulyatori:** Smartboardda Alice va Bob terminallari orqali paket uzatish va ping-pong kechikishini sinash.
* **48:00 – 54:00 (6 min) | Interaktiv Kiber-Quiz:** 3 ta savol bo'yicha blits o'tkazish.
* **54:00 – 69:00 (15 min) | Kiber-Arena (Amaliyot):** O'quvchilar `studio/index.html` da LAN chatini ochib, partadoshi bilan xabar almashadilar.
* **69:00 – 74:00 (5 min) | Juftlikda Peer-Review:** 4 ta mezon bo'yicha xonalar izolyatsiyasi va freymlar tekshiruvi.
* **74:00 – 77:00 (3 min) | O'quvchilar Demosi:** 2 ta juftlik doskaga chiqib o'zaro freymlar oqimini namoyish qiladi.
* **77:00 – 80:00 (3 min) | Xulosa & Uy Vazifasi:** 10 ballik `vazifa.html` ilovasini tushuntirish va 11-hafta WebRTC mavzusini anons qilish.

---

## 🏆 10 Ballik Rasmiy Baholash Mezoni
1. **1-Daraja: Baza (4 ball):** `new WebSocket()` ochish, `onopen` statusini ushlash va JSON xabar qabul qilish.
2. **2-Daraja: Amaliyot (4 ball):** Serverda `broadcastToRoom()` orqali faqat bitta xonadagi o'quvchilarga xabar tarqatish.
3. **3-Daraja: Kiber-Sinov (2 ball):** Aloqa uzilganda auto-reconnect mexanizmi va real-vaqt ping o'lchash.
