# 29-Dars: O'qituvchi Uchun Metodik Qo'llanma (Teacher Prep Guide)
**Target International School // 7–8-Sinflar (12–14 yosh) // 7-Hafta (1-Soat: 40 daqiqa)**
**Mavzu:** Taktika va O'yinchi AI: Taktik Sxemalar va Pozitsiya Algoritmi (FUT Tactical Studio)
**Kohorta:** `7A 7B 8A 8B` (Game Development & Canvas 2D/3D Track)

> **ASOSIY PEDAGOGIK MAQSAD:**
> 7–8-sinf o'quvchilari EA Sports FC va professional futbol tahlilchilarining (Opta, StatsBomb) asosiy muhandislik poydevori — **2D Taktik Maydon Matematikasi** bilan tanishadilar. Ular nima uchun o'yinchilar koordinatalari mutlaq piksellarda emas, balki $0..100\%$ nisbiy foizlarda saqlanishini tushunadilar. O'yinchilar teleport bo'lmasligi uchun kadrlararo silliq **LERP (Linear Interpolation)** harakat formulasini kodlaydilar, 4-3-3, 3-5-2 va 5-3-2 sxemalarining geometrik afzalliklarini tahlil qiladilar, hujum (High Press) va himoya (Low-Block) fazalarida jamoa zichligini solishtiradilar hamda individual AI ko'rsatmalari (Inverted Winger, Sweeper Keeper, Box-to-Box) berib, tayyor `tactics.json` konfiguratsiyasini eksport qiladilar.

---

## 1. Darsda Ishlatiladigan Fayllar va Vositalar

1. **Interaktiv Studiya (Target FUT Tactical & Pitch AI Studio):**
   * Manzil: `classes/7-8-sinf/7-hafta/29-dars-taktika-va-oyinchi-ai/studio/index.html`
   * To'liq oflayn ishlaydi, hech qanday internet kerak emas.
   * Studiya modullari:
     - **Interaktiv 2D Taktik Maydon:** Canvas 2D va SVG koordinatalarida 11 talik o'yinchilarning jonli maydoni.
     - **Sxemalar Selektori:** 4-3-3 Attack, 4-4-2 Flat, 4-2-3-1 Modern, 3-5-2 Balance, 5-3-2 Ultra-Def. Har bir tanlovda o'yinchilar real vaqtda LERP orqali o'z yangi pozitsiyalariga silliq yugurib o'tadi.
     - **Taktik Fazalar (Phase Toggle):** Attacking Phase (jamoa oldinga suriladi, qanotlar ochiladi) vs Defending Phase (Low-Block zich himoya, maydon maydoni 40% ga qisqaradi).
     - **O'yinchi AI Ko'rsatmalari (Player Directives Inspector):** Har bir o'yinchini bosib, uning AI xulq-atvorini o'zgartirish (masalan, LW ga `Inverted Winger` berilsa, u to'g'ri qanotda emas, diagonali bo'ylab jarima maydoniga yorib kiradi).
     - **Taktik Telemetriya:** Jamoa kengligi (Team Width %), Jamoa chuqurligi (Team Depth %), O'rtacha pas masofasi (Avg Pass Distance), Jamoa maydoni maydoni ($m^2$).
     - **4 ta Taktik Kvest (10 ballik mezon):** Avtomatik ball hisoblagich va nom yoziladigan rasmiy Taktik Muhandis Sertifikati.
2. **Prezentatsiya (12 Slayd):**
   * Manzil: `prezentatsiya.html` — Maydon normalizatsiyasi, LERP formulasi, 4-3-3 vs 3-5-2, High-Press vs Low-Block, Inverted Winger, Evklid masofasi, 10 ballik mezon.
3. **Chop Etiladigan Ishchi Varaqa (2 Betlik A4):**
   * Manzil: `varaqa.html` — Normalizatsiya formulalari, sxemalar qiyosiy jadvali, LERP tahlili, individual ko'rsatmalar va 10 ballik o'qituvchi bahosi.

---

## 2. 40 Daqiqalik Dars Reglamenti

| Bosqich | Vaqt | Harakat | O'qituvchi Eslatmasi |
|---|---|---|---|
| **1. Kirish & Muammo** | 0–5 daq | Slayd 1–3 | Nega o'yinchilar koordinatasi piksellarda berilsa turli ekranlarda buziladi? $0..100\%$ normalizatsiya sababi. |
| **2. Taktik Geometriya & LERP** | 5–15 daq | Slayd 4–7 | 4-3-3 (keng qanotlar) va 3-5-2 (markazda 5 talik blok) farqi. LERP formulasi: $current += (target - current) \times 0.08$. |
| **3. AI Direktivalar** | 15–20 daq | Slayd 8–9 | Nega Vinisius yoki Saloh "Inverted Winger" o'ynaydi? Evklid masofasi bilan pas koridorlarini topish. |
| **4. Studiyada Amaliyot** | 20–35 daq | Studiya & Varaqa | O'quvchilar `studio/index.html` da 4 ta kvestni bajaradi: 1) Sxemani o'zgartirish (2b), 2) Fazalarni solishtirish (3b), 3) Inverted Winger berish (3b), 4) `tactics.json` eksport (2b). |
| **5. Xulosa & Baholash** | 35–40 daq | Slayd 10–12 | 10 ballik natijalarni tekshirish, varaqalarga imzo qo'yish, diplomlarni ko'rish. |

---

## 3. Top-3 Texnik Savol-Javob (Q&A)

* **Savol 1:** "Agar LERP alpha koeffitsienti 1.0 qilinsa nima bo'ladi?"
  * **Javob:** O'yinchilar kadrlararo silliq yugurmaydi, balki bir zumda yangi koordinataga teleport bo'ladi (sakrab o'tadi), bu esa sun'iy va yoqimsiz ko'rinadi.
* **Savol 2:** "Low-Block nima va nima uchun Guardiola jamoalari unga qarshi qiynaladi?"
  * **Javob:** Low-Block da jamoa o'z darvozasi oldida 25-30 metrli o'ta zich chiziq quradi (5-3-2 yoki 4-4-2). Bo'sh zonalar deyarli qolmaydi, faqat uzoqdan zarba yoki qanot krosslari orqali yorib o'tish mumkin.
* **Savol 3:** "Nega Inverted Winger zamonaviy futbolda klassik qanot o'yinchisidan ustun qo'yiladi?"
  * **Javob:** Klassik qanot o'yinchisi (Stay Wide) faqat jarima maydoniga oshirib beradi. Inverted Winger esa to'p bilan markazga yorib kirib, to'g'ridan-to'g'ri darvozaga xavfli zarba bera oladi (ikkinchi hujumchiga aylanadi).
