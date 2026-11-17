# 9-sinf, 11-hafta, 32-dars: O'qituvchi Qo'llanmasi
## WebRTC MediaStream va Jonli P2P Mesh: Video, Audio va Ekran Ulashish

### Dars Haqida Ma'lumot:
- **Kohorta:** 9-sinf (Junior Vibecoders, Full-Stack & DevOps Track)
- **Format:** 80 daqiqalik Juftlik Dars (Double Block, 2 bosqichli)
- **Asosiy maqsad:** O'quvchilarga WebRTC MediaStream arxitekturasini o'rgatish, `getUserMedia()` va `getDisplayMedia()` orqali apparat resurslarini boshqarish, videoni SRTP shifrlash bilan uzatish, `replaceTrack()` yordamida aloqani uzmasdan ekran ulashish va Canvas matritsali kiber-filtrlarni kodlash.

---

### 80 Daqiqalik Dars Pacing Xaritasi:

#### 1-BOSQICH (40 daqiqa): Nazariya, Xatolar Tahlili va Jonli Test
| Vaqt | Bosqich | Slayd | O'qituvchi Harakati | Kutiladigan Natija |
|---|---|:---:|---|---|
| **00:00–04:00** | Kirish va Maqsad | 1 | Dars mavzusini e'lon qilish, Discord va Google Meet qanday ishlashini aytish. | O'quvchilarda qiziqish uyg'onadi. |
| **04:00–12:00** | O'tgan Dars HW Tahlili | 2 | 31-darsdagi videoni Base64 matn qilib jo'natish xatosi (33% o'sish va qotish) ni tushuntirish. Blitz savol. | Nega naqd media treklari kerakligi o'zlashtiriladi. |
| **12:00–18:00** | Kamera va getUserMedia | 3 | `getUserMedia` va uning sozlamalari (resolution, echo cancellation) ni tahlil qilish. | HTTPS talabi va media obyekti tushuniladi. |
| **18:00–24:00** | addTrack va ontrack | 4 | Treklar hayot tsikli va SDP kelishuvi. | MediaStream treklarining ulanishi o'rganiladi. |
| **24:00–30:00** | SRTP Shifrlash | 5 | RTP vs SRTP AES-128 va DTLS kalitlar almashishi. | Kiberxavfsizlik va maxfiylik kafolati anglanadi. |
| **30:00–35:00** | Ekran Ulashish | 6 | `getDisplayMedia` va `replaceTrack` orqali uzilishsiz almashtirish. | Ekranni translyatsiya qilish o'rganiladi. |
| **35:00–40:00** | Canvas Kiber-Filtrlari | 7 | Matrix yashil, oq-qora va invert filtrlari formulasini ko'rsatish. | 60 FPS kadrlar bilan ishlash tushuniladi. |

#### 2-BOSQICH (40 daqiqa): Amaliy Kiber-Arena va Taqdimot
| Vaqt | Bosqich | Slayd | O'qituvchi Harakati | Kutiladigan Natija |
|---|---|:---:|---|---|
| **40:00–48:00** | Smartboard Sinovi | 8 | Slayd ichidagi simulyatorda kamerani yoqib, Matrix filtrini ko'rsatish. | Vizual tajriba ortadi. |
| **48:00–54:00** | 3-Savolli Quiz | 9 | Butun sinf bilan interaktiv test o'tkazish. | Bilimlar mustahkamlanadi. |
| **54:00–69:00** | 25 Daqiqalik Arena | 10 | Bolalarga `studio/index.html` da P2P video-chatni ko'tarishni topshirish. | Har bir o'quvchi video-chatni ishga tushiradi. |
| **69:00–74:00** | Partadosh Auditi | 11 | O'rin almashib, 4 ta mezon bo'yicha video va ovozni tekshirish. | Sifat nazorati va kiber-audit. |
| **74:00–77:00** | Katta Ekran Showcasi | 12 | 2 ta parta o'rtasida katta ekranda jonli P2P video-qo'ng'iroqni ko'rsatish. | O'quvchilarda g'urur va ishonch. |
| **77:00–79:00** | Uy Vazifasi | 13 | 10 ballik 3 darajali vazifani tushuntirish. | Vazifa tushuniladi. |
| **79:00–80:00** | Xulosa va Keyingi Dars | 14 | Darsni sarhisob qilish va SPA / Client-side routing mavzusiga ko'prik. | 80 daqiqa to'liq yakunlanadi. |

---

### Keng Tarqalgan Savollar va Maslahatlar:
1. **"Nega brauzer kameraga ruxsat bermayapti?"**
   - Javob: Brauzer xavfsizlik nuqtai nazaridan faqat `localhost` yoki `https://` protokoli orqali ishlovchi saytlarga kamera va mikrofondan foydalanishga ruxsat beradi.
2. **"replaceTrack() chaqirilganda nega qayta offer/answer qilish shart emas?"**
   - Javob: Chunki P2P kanal va kodeklar muzokaralari allaqachon o'rnatilgan. `replaceTrack()` faqat jo'natilayotgan apparat oqimining manbasini almashtiradi (kamera o'rniga ekran treki), kanalning o'zi uzilmaydi!
