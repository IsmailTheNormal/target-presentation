# O'qituvchi uchun qo'llanma: 17-dars — Audio Sintezi, Web Audio API va Partikllar (Zarrachalar Tizimi)

**Kohorta:** 7–8-sinf  
**Hafta / Dars:** 4-hafta / 17-dars  
**Mavzu:** Web Audio API (AudioContext, Osillyatorlar, To'lqin shakllari), Real-Vaqt Ovoz Sintezi va 2D Canvas Partikllar (Zarrachalar) Tizimi  
**Davomiyligi:** 45 daqiqa  

---

## 1. Darsning Pedagogik Maqsadi va Muhandislik Falsafasi

7–8-sinf o'quvchilari 3-haftada Canvas, o'yin tsikli (RAF), dushmanlar to'qnashuvi va sakrash fizikasini o'rgandilar. O'yin mexanik jihatdan ishlayapti, ammo unga **"Game Feel" (O'yin Ta'siri / Juice)** yetishmayapti. O'yinda tovush va vizual effektlar bo'lmasa, u zerikarli va jonsiz tuyuladi.

Ushbu darsda o'quvchilar ikkita yirik sanoat mexanizmini o'rganadilar:
1. **Web Audio API orqali dasturiy ovoz sintezi:**
   - Shunchaki og'ir `.mp3` yoki `.wav` fayllarni yuklash o'rniga, professional o'yinlarda tovushlar matematik to'lqinlar orqali bevosita brauzerning audio-dvijogida generatsiya qilinadi (0 bayt yuklanish, 0 ms kechikish!).
   - `AudioContext` — audio graflar markazi.
   - `OscillatorNode` — to'lqin manbai. To'lqin turlari:
     - `sine` — silliq sinusoidal to'lqin (tanga yoki kristall olish tovushi).
     - `square` — to'rtburchak to'lqin (8-bit retro arkada, lazer otish tovushi).
     - `sawtooth` — o'tkir arra tishli to'lqin (ogohlantirish, dushman zarbasi, qizil lazer).
     - `triangle` — yumshoq uchburchak to'lqin.
   - `GainNode` — tovush balandligi va silliq so'nishi (envelope decay).
   - Chastota modulyatsiyasi (`frequency.exponentialRampToValueAtTime`): Lazer tovushining 880 Hz dan 120 Hz ga tez pasayishi.
2. **Partikllar (Zarrachalar) Tizimi — Visual FX:**
   - Har safar dushman yo'q qilinganda, portlash ro'y berganda yoki kristall olinganda 20–30 ta rangli zarrachalar har tomonga sochiladi.
   - Har bir partiklning xususiyatlari: koordinata `(x, y)`, burchak `angle`, tezlik `vx, vy`, o'lcham `size`, rang `color`, hayot davomiyligi `life` (1.0 dan 0.0 gacha) va so'nish tezligi `decay`.
   - Har bir freymda `x += vx`, `y += vy`, `vy += gravity`, `life -= decay`.
   - Agar `life <= 0` bo'lsa, zarrachalar massividan `splice` orqali tozalash (xotira to'lib ketishining oldini olish).

---

## 2. 45 Daqiqalik Dars Taqsimoti

| Vaqt | Bosqich | O'qituvchi va O'quvchi Faoliyati |
|---|---|---|
| **00:00 – 03:00** | Kirish va Ko'rgazma | O'qituvchi o'yinni ovozsiz va effektsiz o'ynatadi, keyin esa Web Audio va partikllar qo'shilgan variantini ko'rsatadi. "Qaysi biri jonliroq va qiziqroq tuyuldi?" |
| **03:00 – 12:00** | Nazariya: Web Audio API | `AudioContext`, to'lqin turlari (`square`, `sawtooth`, `sine`), Gain tuguni va eksponentsial chastota o'zgarishi tushuntiriladi. |
| **12:00 – 18:00** | Nazariya: Partikllar Fizikasi | Portlash matematikasi: tasodifiy burchaklar ($0 \dots 2\pi$), radial tarqalish va `alpha` shaffoflik so'nishi. |
| **18:00 – 24:00** | Xotira Gigiyenasi | Agar 1 daqiqa ichida 10,000 ta partikl yaratilsa va massiv tozalanmasa, o'yin qotib qoladi (FPS tushishi). `splice` zarurati. |
| **24:00 – 38:00** | Amaliy Laboratoriya (SFX & Particle Studio) | `lab/index.html` interaktiv studiyasida: o'quvchilar o'zlarining shaxsiy SFX (Lazer, Portlash, Sakrash) tovushlarini sintez qiladilar va 5 xil rangdagi zarracha emmitterni sozlaydilar! |
| **38:00 – 43:00** | Varaqa va Mustahkamlash | To'lqin shakllari va partikl obyekti parametrlarini varaqada tahlil qilish. |
| **43:00 – 45:00** | Xulosa va Baholash | 10 ballik rubrika bo'yicha baholash va keyingi 18-dars (Kamera Skrollingi) bilan bog'lash. |

---

## 3. O'quvchilar Ko'p Yo'l Qo'yadigan Xatolar (Tuzoqlar)

1. **Brauzerning Audio Autoplay Taqiqlari:**
   - Brauzerlar foydalanuvchi ekranga birinchi marta bosmaguncha (User Gesture: `click` yoki `keydown`) `AudioContext` ni `suspended` holatida saqlaydi. Agar `new AudioContext()` sahifa yuklanishi bilanoq tovush chiqarishga urinsa, konsolda ogohlantirish chiqadi. Shuning uchun audio har doim tugma bosilganda yoki o'yin boshlanganda faollashtiriladi (`audioCtx.resume()`).
2. **Partikllar massivini tozalashda indeks siljishi:**
   - Massivni boshidan `for (let i = 0; i < particles.length; i++)` qilib `splice(i, 1)` qilsangiz, bitta element tashlab ketiladi. Eng xavfsiz yo'l: orqadan yurish `for (let i = particles.length - 1; i >= 0; i--)` yoki `.filter(p => p.life > 0)`.
3. **Chastota qiymatining 0 ga tenglashishi:**
   - `exponentialRampToValueAtTime` metodi matematik sabablarga ko'ra 0 qiymatini qabul qilmaydi (0 ning eksponentasi aniqlanmagan). Minimal qiymat har doim musbat bo'lishi kerak (masalan: `0.001` yoki `10` Hz).
