# 30-Dars: O'qituvchi Uchun Metodik Qo'llanma va Imtihon Kaliti (Teacher Guide & Fixes)
**Target International School // 7–8-Sinf // 8-Hafta (1-Chorak Oraliq Nazorat: 40 daqiqa)**
**Mavzu:** Sport Simulyatori va O'yin Fizikasi (OVR, Kimyo Graflari, Match Engine va Bozor Solig'i)
**Kohorta:** `7A 7B 8A 8B` (Sports Simulation, Game Physics & Virtual Economies)

---

## 1. Asosiy Pedagogik Maqsad
7–8-sinf o'quvchilari uchun 1-chorak oraliq imtihoni. O'quvchilar EA Sports FC / FUT uslubidagi o'yin dvigatelining 4 ta asosiy ustunini sinovdan o'tkazadilar: vaznli OVR formulasi, 11 tugunli kimyo graflari (33 ballik sinergiya), 2D AABB to'qnashuv fizikasi va transfer bozoridagi 5% EA solig'i (Coin Sink).

---

## 2. Test Savollari va O'qituvchi Yechimlar Kaliti (Test & Fixes Key)

### Test 1: CAM Pozitsiyasi OVR Hisobi
* **Parametrlar:** PAS=88 (0.30), DRI=86 (0.25), SHO=78 (0.20), PAC=82 (0.15), DEF=54 (0.05), PHY=70 (0.05).
* **Hisob:**
  * 88 * 0.30 = 26.4
  * 86 * 0.25 = 21.5
  * 78 * 0.20 = 15.6
  * 82 * 0.15 = 12.3
  * 54 * 0.05 = 2.7
  * 70 * 0.05 = 3.5
  * Jami yig'indi: 26.4 + 21.5 + 15.6 + 12.3 + 2.7 + 3.5 = **82.0 OVR**.

### Test 2: AABB To'qnashuv Mantiqi
* **Shart:** To'p (x=140, y=90, r=5), Darvoza qutisi: x(120..150), y(70..100).
* **Etalon Yechim (Teacher Fix):**
  ```javascript
  function isGoal(ball, goal) {
    return (ball.x + ball.r > goal.xmin) && // 145 > 120 (rost)
           (ball.x - ball.r < goal.xmax) && // 135 < 150 (rost)
           (ball.y + ball.r > goal.ymin) && // 95 > 70 (rost)
           (ball.y - ball.r < goal.ymax);   // 85 < 100 (rost)
    // Natija: TO'LIQ GOOOL!
  }
  ```

---

## 3. Uy Vazifasi (`vazifa.html`) Baholash Mezoni (10 Ball)
* **OVR Matematikasi (4 ball):** Vaznli formula va hisob-kitoblar xatosiz bajarilgan.
* **Kimyo Graflari (3 ball):** N*(N-1)/2 formulasi va jamoaviy sinergiya to'g'ri topilgan.
* **AABB Fizikasi (2 ball):** To'qnashuv chegaralari mantiqiy asoslangan.
* **Bozor Solig'i va Tahlil (1 ball):** 5% EA soliq ayirmasi va inflyatsiya tushunchasi aniq bayon etilgan.
