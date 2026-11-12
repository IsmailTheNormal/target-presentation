# 30-Dars: O'qituvchi Uchun Metodik Qo'llanma va Yechimlar Kaliti
**Target International School // 9-Sinf // 10-Hafta (2-Chorak 2-Darsi: 80 daqiqa / Juftlik Blok)**
**Mavzu:** Komponentlar Falsafasi va UI Arxitekturasi: Reusable Components, Props & State
**Kohorta:** `9-sinf` (Junior Vibecoders, Full-Stack & DevOps Track)

---

## 1. Asosiy Pedagogik Maqsad
Bugungi 80 daqiqalik juftlik darsda 9-sinf o'quvchilari korporativ darajadagi **Komponentlar Falsafasi**ni amalda o'rganadilar:
1. **Lego Modeli:** Shablon (Template), Xususiyatlar (Props), Holat (State) va Hodisalar (Events) izolyatsiyasi.
2. **Bir Tomonlama Oqim (Props Down, Events Up):** Ota komponent bolaga props uzatadi, bola esa faqat CustomEvent chaqirib signal beradi.
3. **Immutability Qoidasi:** State-ni to'g'ridan-to'g'ri o'zgartirmasdan, spread (`{ ...this.state }`) orqali xavfsiz klonlash.
4. **Mustaqil Cyber UI Kutubxonasi:** `studio/index.html` laboratoriyasida Badge, MetricCard va Terminal komponentlarini mustaqil qurish.

---

## 2. 80 Daqiqalik Dars Reglamenti

### 1-Bosqich (00:00 – 40:00): Nazariya, Uy Vazifasi Tahlili va Jonli Test
* **00:00 – 04:00 (4 min):** Titul, Dars maqsadi va 80 daqiqalik kiber-missiya anonsi (Slayd 1).
* **04:00 – 12:00 (8 min):** Majburiy Uy Vazifasi Tahlili: 29-darsdagi Heap link mutatsiyasi xatosi va Spread klonlash oltin yechimi (Slayd 2).
* **12:00 – 18:00 (6 min):** Muammo: Spaghetti monolit va 50 ta faylni copy-paste qilish dahshati (Slayd 3).
* **18:00 – 24:00 (6 min):** Komponent anatomiyasi: Template, Props, State va Events (Slayd 4).
* **24:00 – 30:00 (6 min):** Arxitektura: Props Down, Events Up oqim diagrammasi (Slayd 5).
* **30:00 – 35:00 (5 min):** Kod mexanizmi: Factory function vs Native Web Components (Slayd 6).
* **35:00 – 40:00 (5 min):** State reaktivligi va Targeted Re-render mexanikasi (Slayd 7).

### 2-Bosqich (40:00 – 80:00): Jonli Simulyator, Kiber-Arena va Peer-Review
* **40:00 – 48:00 (8 min):** Jonli Simulyator: Smartboardda MetricCard Props va State o'zgarishlarini sinash (Slayd 8).
* **48:00 – 54:00 (6 min):** Interaktiv Quiz: 3 ta savol bo'yicha blits nazorat (Slayd 9).
* **54:00 – 69:00 (15 min):** Katta Kiber-Arena: `studio/index.html` da CyberBadge va MetricCard komponentlarini yozish (Slayd 10).
* **69:00 – 74:00 (5 min):** Juftlikda Peer-Review: 4 ta mezon bo'yicha partadosh kodini tekshirish (Slayd 11).
* **74:00 – 77:00 (3 min):** O'quvchilar Demosi: 2 ta juftlik o'z komponentini doskada ko'rsatadi (Slayd 12).
* **77:00 – 80:00 (3 min):** 10 ballik uy vazifasi tushuntiriladi va 11-haftaga (SPA & Routing) ko'prik tashlanadi (Slayd 13-14).

---

## 3. Topshiriqlar va Viktorina Yechimlari

### Viktorina (Slayd 9):
1. **Props va State farqi:** **B) Props tashqaridan keladi (read-only), State — ichki xotira.**
2. **Bolaning otaga aloqasi:** **B) CustomEvent dispatch qiladi (Events Up).**
3. **Nega direct mutation taqiqlangan:** **B) Re-render chaqirilmaydi va UI eskirib qoladi.**

### Amaliy Laboratoriya Yechimi:
```javascript
// studio/index.html etalon kodi:
export function createMetricCard(props) {
  const card = document.createElement("div");
  card.className = "cyber-card";
  card.innerHTML = `
    <div class="card-title">${props.title}</div>
    <div class="card-val">${props.value}</div>
  `;
  card.onclick = () => {
    card.dispatchEvent(new CustomEvent("metric-click", {
      bubbles: true,
      detail: { title: props.title }
    }));
  };
  return card;
}
```

---

## 4. 10 Ballik Baholash Rubrikasi

* **1-Daraja: Baza (4 ball):** Kiruvchi props asosida toza DOM element yasovchi `<cyber-badge>` komponenti.
* **2-Daraja: Muhandislik (4 ball):** O'zining State xotirasiga ega va CustomEvent chiqaruvchi hisoblagich.
* **3-Daraja: Kiber-Chaqiriq (2 ball):** `observedAttributes` bilan W3C rasmiy Web Component yaratish.
