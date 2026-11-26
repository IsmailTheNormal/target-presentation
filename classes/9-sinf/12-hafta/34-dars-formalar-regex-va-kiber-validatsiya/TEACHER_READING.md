# 34-dars: Formalar, Regex va Real-Vaqt Kiber-Validatsiya (O'qituvchi Metodologiyasi)

## Darsning Pasporti
- **Sinf:** 9-sinf (Junior Vibecoders, Full-Stack & DevOps Track)
- **Davomiyligi:** 40 daqiqa (Yakka Dars / Single Block)
- **Asosiy maqsad:** O'quvchilarga SPA ilovalarda klassik sahifani qayta yuklovchi POST formalardan voz kechib, `input` hodisasida 0 ms kechikish bilan ishlovchi real-vaqt kiber-validatsiyasini o'rgatish. Regex muntazam ifodalari sintaksisi, O'zbekiston telefon raqamlari qolipi, parol entropiyasini matematik hisoblash va XSS xurujlarini zararsizlantirish.

---

## 40 Daqiqalik Aniq Vaqt Taqsimoti (Pacing)

| Vaqt | Bosqich | Slayd | O'qituvchi Faoliyati | O'quvchilar Faoliyati |
|---|---|:---:|---|---|
| **00:00–04:00** | Kirish va Motivatsiya | 1 | Nega 2026-yilda yomon formalar mijozlarni yo'qotishi va kiber-xavfsizlik xavfini tushuntirish. | Diqqat bilan tinglaydilar va dars maqsadini belgilaydilar. |
| **04:00–08:00** | 33-dars HW Tahlili | 2 | SPA routerda F5 bosganda 404 xatosi chiqishi (Vercel rewrite yo'qligi) sababini tahlil qilish. | Blitz savolga javob beradilar, server rewrites qoidasini yozadilar. |
| **08:00–14:00** | Klassik Formalar Muammosi | 3 | Sahifa qayta yuklanishi o'rniga e.preventDefault() va input hodisasi ishlash tartibini ko'rsatish. | 0 ms validatsiya afzalligini anglaydilar. |
| **14:00–20:00** | Regex Sintaksisi | 4 | Meta-belgilar (^, $, \d, \w, +, {8,}) va RegExp.test() metodini doskaga yozish. | Sintaksisni daftarlariga qayd etadilar. |
| **20:00–25:00** | Amaliy Qoliplar | 5 | Email, O'zbekiston telefoni (+998) va kuchli parol qoliplarini tahlil qilish. | Qoliplar tuzilishini o'rganadilar. |
| **25:00–29:00** | Parol Entropiyasi | 6 | E = L * log2(R) formulasi va RTX 4090 da brute-force vaqtlari taqqoslashini ko'rsatish. | Parol uzunligi nega muhimligini tushunadilar. |
| **29:00–33:00** | XSS Sanitizatsiya | 7 | innerHTML orqali script va img onerror inyeksiyasi qanday sodir bo'lishini ko'rsatish. | sanitizeHTML funksiyasini yozishni o'rganadilar. |
| **33:00–37:00** | Smartboard Sinovi | 8 | Slayddagi simulyatorda email va parollarni sinash, xakerlik kodini tozalashni ko'rsatish. | Ekranda real-vaqt validatsiyani kuzatadilar. |
| **37:00–39:00** | Viktorina (Quiz) | 9 | 3 ta nazorat savoli bo'yicha tezkor blitz o'tkazish. | Faol javob beradilar va bilimlarini mustahkamlaydilar. |
| **39:00–40:00** | Xulosa va Uy Vazifasi | 10 | 10 ballik uy vazifasini tushuntirish va NPM mavzusiga ko'prik! | Kundaliklariga vazifani yozib oladilar. |

---

## O'qituvchi Uchun Muhim Blitz Savollari
1. **"Nega `change` hodisasi o'rniga `input` hodisasidan foydalanish afzalroq?"**
   - Javob: Chunki `change` faqat foydalanuvchi maydondan fokusni uzgandagina (blur) ishlaydi. `input` esa har bitta harf yozilganda 0 ms da javob qaytaradi.
2. **"Nega parolda belgilar xilma-xilligi (R) emas, ko'proq uzunlik (L) entropiyani tezroq oshiradi?"**
   - Javob: Chunki formula bo'yicha uzunlik $L$ ko'paytuvchi sifatida turadi, $R$ esa logarifm ichida. Uzunlikning 1 taga oshishi ehtimolliklar fazosini bir necha karra ko'paytiradi.

---

## 10 Ballik Baholash Rubrikasi
- **4 Ball (Baza):** Email va +998 telefon raqamlari uchun to'g'ri Regex yozadi va test() metodidan foydalanadi.
- **4 Ball (Amaliy):** `input` hodisasida parol entropiyasini hisoblab, rangli shkalada ko'rsata oladi.
- **2 Ball (Challenge):** XSS xavfli belgilarini (&lt;, &gt;, &amp;, &quot;) maxsus HTML obyektlariga aylantiruvchi tozalash modulini yaratadi!
