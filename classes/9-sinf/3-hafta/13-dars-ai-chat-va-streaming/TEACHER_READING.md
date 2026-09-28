# O'qituvchi uchun Qo'llanma — 13-Dars: AI Chat Interfeysi va Real-Vaqt Streaming

## 1. Darsning Pedagogik Maqsadi
O'quvchilarga ChatGPT kabi AI chat interfeyslarining orqa tomonidagi tarmoq arxitekturasini (Server-Sent Events) tushuntirish. Nega oddiy HTTP kutish o'rniga tokenma-token oqim (Streaming) ishlatilishini, JavaScript da ReadableStream va TextDecoder yordamida oqimni ushlashni, avto-skroll hamda AbortController orqali generatsiyani to'xtatish mexanizmini o'rgatish.

## 2. Dars Vaqti Taqsimoti (40 daqiqa)
- **0–3 daq:** Kirish. HTTP kutish vs Real-vaqt Streaming namoyishi.
- **3–13 daq:** Nazariya: SSE protokoli, Content-Type: text/event-stream, ReadableStream va TextDecoder kodi.
- **13–23 daq:** Interfeys: Avto-skroll kodi, Markdown renderlash, suhbat tarixi (messages massivi) va AbortController.
- **23–33 daq:** Amaliyot: `lab/index.html` da streaming tezligini o'zgartirish, Stop tugmasini sinash va varaqaga yozish.
- **33–37 daq:** Tahlil: Tarmoq uzilishi va professional UI standartlari (Shift+Enter, Copy tugmasi).
- **37–40 daq:** Xulosa va 10 ballik mezon bo'yicha baholash.

## 3. O'quvchilarga beriladigan savollar
1. "Nega YouTube da video ko'rayotganda butun videoni yuklanishini kutmaymiz? Buni AI chat bilan qanday bog'liqligi bor?"
2. "Agar chat tarixi 50 ta xabarga yetsa, modelga har safar hammasini yuborish qanday muammo tug'diradi?"
3. "AbortController tugmasi bosilganda server va brauzer orasida nima yuz beradi?"
