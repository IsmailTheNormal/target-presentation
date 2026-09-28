# O'qituvchi uchun Qo'llanma — 14-Dars: Tizimli Promptlar, Rollar va Kiberxavfsizlik

## 1. Darsning Pedagogik Maqsadi
O'quvchilarga til modellarining zaifliklarini (Prompt Injection va Jailbreak) tushuntirish, tizimli promptning 4 ta ustunini (Rol, Maqsad, Guardrails va Fallback), XML delimiterlar orqali foydalanuvchi matnini xavfsiz izolyatsiyalashni hamda Red Team vs Blue Team kiber-dueli orqali xavfsizlik madaniyatini shakllantirish.

## 2. Dars Vaqti Taqsimoti (40 daqiqa)
- **0–3 daq:** Kirish. Bank botini aldash misoli.
- **3–13 daq:** Nazariya: Tizimli prompt tuzilishi, Rol berish va Few-Shot namunalari.
- **13–23 daq:** Xavfsizlik: Prompt Injection (Direct vs Indirect), DAN jailbreaki va XML delimiterlar bilan himoyalanish.
- **23–33 daq:** Amaliyot: `lab/index.html` da Kiber-Duel: biri buzuvchi, biri himoyachi bo'lib sinov o'tkazish.
- **33–37 daq:** Tahlil: Chiqishni filtrlash (Output Guardrails) va OWASP Top 10 for LLMs.
- **37–40 daq:** Xulosa va 10 ballik mezon bo'yicha baholash.

## 3. O'quvchilarga beriladigan savollar
1. "Nega oddiy foydalanuvchi kiritgan matn ichiga tizimli buyruq yozsa, model uni buyruq deb tushunib qoladi?"
2. "XML teglari (`<user_input>`) modelga qanday qilib matnni shunchaki ma'lumot deb qabul qilishga yordam beradi?"
3. "Indirect Prompt Injection nima va u nega kiberxavfsizlikda eng xavfli hujum hisoblanadi?"
