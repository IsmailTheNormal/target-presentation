# 9-sinf, 11-hafta, 31-dars: O'qituvchi Qo'llanmasi
## WebRTC va Peer-to-Peer (P2P) Aloqa: STUN, SDP Handshake va RTCDataChannel

### Dars Haqida Ma'lumot:
- **Kohorta:** 9-sinf (Junior Vibecoders, Full-Stack & DevOps Track)
- **Format:** 40 daqiqalik Yakka Dars (Single Block)
- **Asosiy maqsad:** O'quvchilarga markaziy serversiz to'g'ridan-to'g'ri brauzerlararo P2P aloqani o'rgatish, NAT to'siqlarini tushuntirish, STUN serveri vazifasini ko'rsatish va RTCDataChannel orqali xavfsiz shifrlangan ma'lumot uzatish.

---

### 40 Daqiqalik Dars Pacing Xaritasi:

| Vaqt | Bosqich | Slayd | O'qituvchi Harakati | Kutiladigan Natija |
|---|---|:---:|---|---|
| **00:00–04:00** | Kirish va Maqsad | 1 | Dars mavzusini e'lon qilish, HTTP vs WebSocket vs WebRTC arxitekturasini qisqa solishtirish. | O'quvchilar darsning markaziy maqsadi — to'g'ridan-to'g'ri P2P aloqa ekanini tushunishadi. |
| **04:00–08:00** | O'tgan Dars HW Tahlili | 2 | 30-darsdagi keng tarqalgan xato: markaziy WebSocket serverga katta fayllarni yuklash oqibatlarini tahlil qilish. Blitz savol. | O'quvchilar nega markaziy server tiqilib qolishini va WebRTC nega kerakligini anglaydilar. |
| **08:00–12:00** | NAT To'sig'i va STUN | 3 | Nega 192.168.x.x manzilga internetdan to'g'ridan-to'g'ri bog'lanib bo'lmasligini doskada chizib tushuntirish. | STUN serveri mijozning tashqi IP va portini bildiruvchi ko'zgu ekanligi o'zlashtiriladi. |
| **08:00–16:00** | SDP va ICE Handshake | 4 | SDP offer/answer va ICE candidate qadamlarini ketma-ket ko'rsatish. | 4 bosqichli bog'lanish protokoli tushuniladi. |
| **16:00–20:00** | Kod Mexanizmi | 5 | `RTCPeerConnection` va `createDataChannel` kodini tahlil qilish. | JavaScript WebRTC API sintaksisi o'rganiladi. |
| **20:00–24:00** | Xavfsizlik (DTLS/SCTP) | 6 | WebRTC protokollar steki: UDP ustidagi DTLS shifrlash va SCTP oqimini tushuntirish. | WebRTC ochiq uzatilishi mumkin emasligi (majburiy shifr) bilib olinadi. |
| **24:00–28:00** | Jonli Smartboard Demo | 7 | Slayd ichidagi interaktiv P2P simulyatorda Alice va Bob o'rtasida kanal ochib, paket yuborish. | Vizual real-vaqt P2P ishlashi va &lt;1ms kechikish ko'riladi. |
| **28:00–32:00** | Bilimni Sinash (Quiz) | 8 | 3 ta savolli testni butun sinf bilan yechish va darhol izohlash. | O'quvchilar tushunchalari mustahkamlanadi. |
| **32:00–37:00** | 15 Daqiqalik Arena | 9 | `studio/index.html` laboratoriyasida o'quvchilarga P2P terminalni mustaqil ishga tushirishni buyurish. | Har bir o'quvchi ishlaydigan P2P kanal ko'taradi. |
| **37:00–40:00** | Baholash va Ertangi Dars | 10 | 10 ballik mezonni e'lon qilish, 3 darajali uy vazifasini tushuntirish va ertangi 80 daqiqalik juftlik darsi (WebRTC video oqimlari) ga ko'prik. | Uy vazifasi tushuniladi va ertangi katta darsga qiziqish uyg'onadi. |

---

### Keng Tarqalgan Savollar va Pedagogik Ko'rsatmalar:
1. **"Nega STUN serveri bo'lmasa ulanib bo'lmaydi?"**
   - Javob: Chunki kompyuteringiz o'zining router ortidagi ichki IP manzilini (masalan, `192.168.1.15`) biladi, lekin internet provayder unga qaysi tashqi ommaviy IP va port berganini bilmaydi. STUN serveriga birinchi so'rov yuborilganda, STUN router ochgan tashqi portni ko'radi va javobda: "Sening tashqi porting 49811" deb xabar qiladi.
2. **"SDP nima degani?"**
   - Javob: SDP (Session Description Protocol) — oddiy matnli fayl. Unda: "Menda qaysi audio/video kodeklar bor, qaysi shifr kalitlar ishlatiladi va DataChannel parametrlari nima?" degan ma'lumotlar saqlanadi.
3. **"Agar bitta Wi-Fi tarmog'ida bo'lsak STUN kerakmi?"**
   - Javob: Bitta Wi-Fi tarmog'ida `host` nomzodlari (lokal IP) orqali ulanish mumkin, ammo brauzer baribir STUN-ga so'rov tashlab ko'radi.
