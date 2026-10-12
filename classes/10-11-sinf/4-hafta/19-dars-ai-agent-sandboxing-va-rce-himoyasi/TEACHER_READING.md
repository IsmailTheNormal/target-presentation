# 19-Dars: O'qituvchi Uchun Tayyorgarlik Qo'llanmasi (Teacher Prep Guide)
**Target International School // 10–11-Sinflar (Senior Engineering) // 4-Hafta (3-Soat)**
**Mavzu:** AI Agent Sandboxing va RCE Himoyasi — Xavfsiz Kod Bajarish

> **METODIK ESLATMA:** 14-darsda o'quvchilar modelga Tool Calling (funksiyalar chaqirish),
> 18-darsda esa Prompt Injection hujumlarini o'rgangan edi. Bugun bu ikki omil
> eng xavfli nuqtada to'qnashadi: **agar AI agent o'zi yozgan kodni xost tizimida
> mustaqil bajarsa nima bo'ladi?** Bu 10–11-sinf Senior muhandislik kohortasi uchun
> tizimli Linux xavfsizligi, konteynerlar va mikroyadrolar (gVisor, Firecracker) darsi.

---

## 1. Darsda Qaysi Vositalar Ishlatiladi?

1. **Sandboxing Laboratoriya Stendi (Google Chrome):**
   * Fayl: `classes/10-11-sinf/4-hafta/19-dars-ai-agent-sandboxing-va-rce-himoyasi/lab/index.html`
   * Internet yoki Docker o'rnatish talab qilinmaydi (brauzer ichida to'liq xavfsiz simulyatsiya).
   * Stendda: 5 ta hujum ssenariysi (parol o'g'irlash, reverse shell C2, diskni tozalash, fork-bomba, xavfsiz analitika), 6 ta himoya to'sig'i (Non-Root UID 10001, Read-Only rootfs, Drop Linux Caps, Network None, cgroups v2, gVisor runsc), real vaqtli terminal telemetriyasi va Audit Sertifikati eksporti.
2. **Prezentatsiya:** `prezentatsiya.html` — 12 slayd, `N` — spiker izohlari.
3. **Ishchi Varaqa:** `varaqa.html` — 2 betlik A4 chop etiladigan kiber-laboratoriya jurnali.

---

## 2. Dars Vaqti Rejasi (45 Daqiqa)

* **0–3 daqiqa:** Titul slayd va motivatsiya: nima uchun zamonaviy AI agentlar (Cursor, Claude Code, OpenInterpreter) kod bajaradi va nega bu RCE xavfini tug'diradi?
* **3–11 daqiqa:** OWASP LLM02 (Insecure Output Handling) tahlili va konteyner xatosi ("Docker bu virtual mashina emas, yadro bitta!").
* **11–27 daqiqa:** Himoyaning 3 ta asosiy echeloni:
  - Non-Root + Read-Only rootfs (`--read-only`, ephemeral tmpfs).
  - Linux Capabilities va Seccomp (`--cap-drop=ALL`, `--no-new-privileges`).
  - Tarmoqni uzish (`--network none`) va gVisor / Firecracker mikroyadrolari.
* **27–39 daqiqa:** Amaliy laboratoriya (`lab/index.html`): 4 ta kvestni navbatma-navbat bajarish va varaqaga yozish (12 daqiqa).
* **39–43 daqiqa:** Baholash mezonlari (10 ballik tizim) va varaqalarni tekshirish.
* **43–45 daqiqa:** Xulosa: ertangi 20-dars — Senior Capstone Demo Day e'loni.

---

## 3. Noutbuksiz O'quvchilar Uchun Alternativa (No-Laptop Path)

Noutbuki yo'q o'quvchilar varaqadagi **2-bo'lim (Zararlanish Radiusi tahlili)** va **3-bo'lim (Taqqoslash matritsasi)** ustida juftlikda ishlaydi:
- Doskaga proyektor orqali `lab/index.html` chiqariladi.
- Noutbuksiz o'quvchi xavfsizlik auditori rolini oladi: u "qaysi flagni yoqish kerak?" deb boshqaradi, sherigi esa stendda sinab ko'radi.
- Har ikkala o'quvchi varaqadagi yadro xatolarini (Errno 13, Errno 30, Errno 101, Errno 11) to'liq yozadi.

---

## 4. O'quvchilarning Keng Tarqalgan Xatolari (Misconceptions)

1. *"Docker bu virtual mashina, ichidagi virus tashqariga chiqolmaydi."*
   - **Tushuntirish:** Yo'q! Docker Linux Namespaces va cgroups orqali faqat jarayonlarni ajratadi, yadro esa bitta. Yadroda zaiflik bo'lsa (masalan, `dirty COW`), xaker konteynerdan xostga chiqadi.
2. *"Agar fayllarga huquq bermasak ham, skript baribir parollarni o'qiydi."*
   - **Tushuntirish:** Linux DAC (Discretionary Access Control) qoidalari UID 10001 foydalanuvchisiga `/etc/shadow` ni o'qishga 100% ruxsat bermaydi (`Permission denied`).
3. *"Skript faqat hisob-kitob qilsa, tarmoqni uzish shart emas."*
   - **Tushuntirish:** Xaker bilvosita prompt injection orqali kod ichiga `curl` yoki `socket` qo'shib, butun bazani tashqi C2 serveriga uzatib yuborishi mumkin. Shuning uchun `--network none` majburiydir.
