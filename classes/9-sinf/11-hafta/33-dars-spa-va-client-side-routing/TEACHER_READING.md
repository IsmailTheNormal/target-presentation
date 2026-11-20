# 9-sinf · 11-hafta · 33-dars: SPA va Client-Side Routing
## O'qituvchi Uchun Dars O'tish Qo'llanmasi (80 daqiqalik Juftlik Dars)

**O'qituvchi:** Ismoiljon Usmonov  
**Fan:** Vibecoding / Full-Stack & DevOps  
**Mavzu:** SPA (Single Page Application) Asoslari va Client-Side Routing  
**Dars turi:** Juftlik blok (Double Block — 80 daqiqa)

---

### 1. Darsning Asosiy Maqsadi va Metodikasi
O'quvchilar oldingi darslarda WebSockets va WebRTC orqali real-vaqt ma'lumotlarini almashishni o'rgandilar. Ammo klassik veb-saytlarda har safar havola bosilganda sahifa qayta yuklanadi va barcha socket/webrtc ulanishlari uzilib qoladi!
Bugungi darsda o'quvchilar:
1. Nega zamonaviy veb (Gmail, YouTube, Discord) **SPA** ga o'tganini;
2. **HTML5 History API** (`pushState`, `replaceState`, `popstate`) ichki ishlash mexanizmini;
3. `e.preventDefault()` orqali havolalarni tutib qolish va 0 ms da komponentlarni yangilashni;
4. F5 bosilganda serverdagi 404 xatosini bartaraf qilish (Vercel rewrites) amaliyotini o'zlashtiradilar.

---

### 2. 80 Daqiqalik Dars Pacing Xaritasi

| Bosqich | Vaqt | Faoliyat Mazmuni |
|:---:|:---:|---|
| **1-Bosqich** | 00:00–04:00 | **Titul va Darsga Kirish:** Nega sahifalar qayta yuklanmasligi kerakligi va SPA inqilobi. |
| **2-Bosqich** | 04:00–12:00 | **Uy Vazifasi Tahlili:** 32-darsdagi video treklarni to'xtatmaslik (camera LED leak) xatosi tahlili va blitz savol. |
| **3-Bosqich** | 12:00–20:00 | **MPA vs SPA Arxitekturasi:** FOUC (oq ekran) muammosi va tarmoq trafigini tejash. |
| **4-Bosqich** | 20:00–28:00 | **HTML5 History API:** pushState, replaceState va popstate hodisalarini jonli konsolda ko'rsatish. |
| **5-Bosqich** | 28:00–36:00 | **Hash vs Path Routing:** Nega zamonaviy veb toza Path (/about) marshrutlashni tanlaydi? |
| **6-Bosqich** | 36:00–44:00 | **Link Interception:** e.preventDefault() bilan a[data-link] havolalarni markaziy tutib qolish. |
| **7-Bosqich** | 44:00–50:00 | **Routes Map va View Rendiring:** Marshrutlar xaritasi va aktiv menyu indikatori. |
| **8-Bosqich** | 50:00–60:00 | **Jonli Test-Drayv:** Taqdimot ichidagi Cyber-OS SPA panelini ishlatib ko'rish. |
| **9-Bosqich** | 60:00–66:00 | **Dinamik Parametrlar va 404:** Regex bilan /user/:id ni ajratish va NotFoundView. |
| **10-Bosqich** | 66:00–70:00 | **F5 Tuzog'i va Server Fallback:** vercel.json rewrites va Nginx try_files siri. |
| **11-Bosqich** | 70:00–74:00 | **Vibecoding Prompt Arxitekturasi:** AI ga 4 bosqichli buyruqlar berish yo'riqnomasi. |
| **12-Bosqich** | 74:00–77:00 | **Juftlikda Kod Auditi:** Partadoshining routerni tekshirish (Back/Fwd va 404). |
| **13-Bosqich** | 77:00–79:00 | **Xulosa va Oltin Qoidalar:** SPA ning 4 ta oltin qoidasini mustahkamlash. |
| **14-Bosqich** | 79:00–80:00 | **3 Darajali Uy Vazifasi:** 10 ballik rubrika va topshiriq reglamenti. |

---

### 3. Keng Tarqalgan Xatolar (Pitfalls) va Oltin Yechimlar
* **Tuzoq 1: Tashqi havolalarning ham to'xtab qolishi:**
  * *Xato:* `document.addEventListener('click', ...)` barcha `<a>` teglarini to'xtatadi.
  * *Yechim:* Faqat ichki havolalarga `data-link` atributini qo'ying: `e.target.closest('a[data-link]')`.
* **Tuzoq 2: Orqaga qaytganda sahifa yangilanmasligi:**
  * *Xato:* `popstate` tinglovchisini qo'shish unutiladi, natijada brauzer tugmasi bosilsa ham eski sahifa qolaveradi.
  * *Yechim:* `window.addEventListener('popstate', router)` albatta yozilishi shart!
