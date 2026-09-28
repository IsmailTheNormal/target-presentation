import os
from generate_all_worksheets import build_worksheet, BASE_DIR

# =========================================================================
# LESSON 4 WORKSHEET
# =========================================================================
l4_t1 = {"uz": "Game Concept Art va Vizual Dizayn", "ru": "Гейм-Концепт Арт и Визуальный Дизайн", "en": "Game Concept Art & Visual Design"}
l4_s1 = {
  "uz": "Grafik neyrotarmoqlar orqali o'yin qahramonlari, biomlar va qurollarning konsept-artlarini yarating.",
  "ru": "Создавайте концепт-арт персонажей, биомов и оружия через графические нейросети.",
  "en": "Generate game concept art for characters, biomes, and weapons via AI image engines."
}
l4_k1 = {
  "uz": "Concept Art — bu shunchaki rasm emas, balki 3D modelerlar uchun aniq ishlab chiqarish chizmasidir.",
  "ru": "Концепт-арт — это не просто картинка, а производственный чертеж для 3D-моделлеров и движка.",
  "en": "Concept art is not mere illustration; it is an actionable technical blueprint for 3D modelers."
}
l4_p1 = """
  <section class="sec">
    <div class="h"><span class="no">01</span><h2><span lang="uz">Concept Art Nima?</span><span lang="ru">Что такое Концепт-Арт?</span><span lang="en">What is Concept Art?</span></h2></div>
    <div class="compare">
      <div class="bad">
        <span class="lbl"><span lang="uz">Tasodifiy Chiroyli Rasm</span><span lang="ru">Случайная Картинка</span><span lang="en">Random Artwork</span></span>
        <p class="pr"><span lang="uz">Chiroyli ko'rinadi, lekin burchaklari noaniq va proporsiyalari xato. 3D model yasab bo'lmaydi.</span><span lang="ru">Красиво, но ракурс непонятен, детали размыты. Нельзя сделать 3D-модель для игры.</span><span lang="en">Looks cool, but angles are vague and geometry warped. Useless for 3D production.</span></p>
      </div>
      <div class="good">
        <span class="lbl"><span lang="uz">Ishlab Chiqarish Konsepti</span><span lang="ru">Производственный Концепт</span><span lang="en">Production Concept Art</span></span>
        <p class="pr"><span lang="uz">Materiallar (metall, lazer), ranglar palitrasi va barcha burchaklar aniq ko'rsatilgan!</span><span lang="ru">Материалы, точные пропорции и ракурсы со всех сторон для 3D-художника.</span><span lang="en">Clear surface materials, orthographic angles, and precise color palettes.</span></p>
      </div>
    </div>
  </section>

  <section class="sec">
    <div class="h"><span class="no">02</span><h2><span lang="uz">O'yin Art Uslublari (Art Styles)</span><span lang="ru">Стили Игровой Графики</span><span lang="en">Visual Art Directions</span></h2></div>
    <div class="trio">
      <div>
        <b><span lang="uz">Voxel & Low-Poly 🧊</span><span lang="ru">Voxel & Low-Poly 🧊</span><span lang="en">Voxel & Low-Poly 🧊</span></b>
        <span class="d"><span lang="uz">Roblox va Minecraft uslubi: sodda geometriya va toza ranglar.</span><span lang="ru">Стиль Roblox и Minecraft: чистые формы и яркие цвета.</span><span lang="en">Roblox and Minecraft aesthetic: clean meshes.</span></span>
      </div>
      <div>
        <b><span lang="uz">Pixel Art 👾</span><span lang="ru">Pixel Art 👾</span><span lang="en">Pixel Art 👾</span></b>
        <span class="d"><span lang="uz">8-bit / 16-bit retro uslub: 2D arkadalar va indie o'yinlar.</span><span lang="ru">8/16-бит ретро для 2D-платформеров и инди-хитов.</span><span lang="en">Retro 8/16-bit styling for responsive 2D platformers.</span></span>
      </div>
      <div>
        <b><span lang="uz">Cyberpunk 🏙️</span><span lang="ru">Cyberpunk 🏙️</span><span lang="en">Cyberpunk 🏙️</span></b>
        <span class="d"><span lang="uz">Neon nurlar, qorong'u metall va kelajak shahar estetikasi.</span><span lang="ru">Неоновые огни, темный металл и ночной мегаполис.</span><span lang="en">Neon rimlights, dark metal, and sci-fi skylines.</span></span>
      </div>
    </div>
  </section>

  <section class="sec">
    <div class="h"><span class="no">03</span><h2><span lang="uz">AI Rasm Prompti Formulasi (5 Element)</span><span lang="ru">Формула Промпта (5 Частей)</span><span lang="en">5-Element Visual Formula</span></h2></div>
    <div class="formula">
      <div class="p"><b>1. Obyekt</b><span class="d">Kiber-tulki mexanik</span></div>
      <div class="plus">+</div>
      <div class="p"><b>2. Uslub</b><span class="d">Low-poly 3D render</span></div>
      <div class="plus">+</div>
      <div class="p"><b>3. Yorug'lik</b><span class="d">Neon ko'k nur</span></div>
      <div class="plus">+</div>
      <div class="p"><b>4. Burchak</b><span class="d">Front model view</span></div>
      <div class="plus">+</div>
      <div class="p"><b>5. Dvigatel</b><span class="d">Unreal Engine 5</span></div>
    </div>
  </section>

  <section class="sec">
    <div class="h"><span class="no">04</span><h2><span lang="uz">AI Glitchlari va Negative Prompt</span><span lang="ru">Артефакты и Negative Prompt</span><span lang="en">Artifacts & Negative Prompts</span></h2></div>
    <ul class="rules">
      <li><span class="t"><span lang="uz"><b>Xatolar sababi:</b> AI piksellar statistikasini hisoblaydi, shuning uchun ba'zan 6 ta barmoq yoki qo'shaloq qurol chizib qo'yadi.</span><span lang="ru"><b>Причина багов:</b> ИИ генерирует по статистике, поэтому путает пальцы и генерирует лишние мечи.</span><span lang="en"><b>Bug Origin:</b> Diffusion computes statistical pixel probabilities, glitching hand geometry.</span></span></li>
      <li><span class="t"><span lang="uz"><b>Negative Prompt Yechimi:</b> Prompt oxiriga taqiqlarni qo'shing: <code>--no deformed hands, extra fingers, blurry</code></span><span lang="ru"><b>Решение:</b> Добавляйте негативный промпт: <code>--no deformed hands, extra fingers, blurry</code></span><span lang="en"><b>Constraint Fix:</b> Append negative parameters: <code>--no deformed hands, extra fingers, blurry</code></span></span></li>
    </ul>
  </section>
"""

l4_t2 = {"uz": "Character Sheet va Asset Dizayn", "ru": "Лист Персонажа и Игровые Ассеты", "en": "Character Sheet & Asset Design"}
l4_s2 = {
  "uz": "5 qismli formula yordamida personaj va inventar assetlarini loyihalash amaliyoti.",
  "ru": "Практика проектирования персонажа и игровых ассетов по формуле 5 параметров.",
  "en": "Hands-on engineering of character turnaround and inventory game assets."
}
l4_p2 = """
  <section class="sec">
    <div class="h"><span class="no">05</span><h2><span lang="uz">5 Qismli Prompt Konstruktori</span><span lang="ru">Конструктор Промпта Персонажа</span><span lang="en">5-Part Prompt Builder</span></h2></div>
    <div class="scroll-x">
      <table>
        <thead>
          <tr>
            <th>1. Obyekt (Subject)</th>
            <th>2. Uslub (Art Style)</th>
            <th>3. Yoritish (Lighting)</th>
            <th>4. Burchak (Camera)</th>
            <th>5. Sifat / Engine</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><span lang="uz">Kiber-skaut ninja</span><span lang="ru">Киборг-ниндзя</span><span lang="en">Cyborg ninja scout</span></td>
            <td>Low-poly Roblox</td>
            <td>Neon rimlight</td>
            <td>Front / Orthographic</td>
            <td>Unreal Engine 5, 8k</td>
          </tr>
        </tbody>
      </table>
    </div>
  </section>

  <section class="sec">
    <div class="h"><span class="no">06</span><h2><span lang="uz">Character Turnaround Sheet Chizmasi</span><span lang="ru">Модельный Лист (Ракурсы)</span><span lang="en">Multi-Angle Model Sheet</span></h2></div>
    <div class="key">
      <span class="k"><span lang="uz">Bitta Varaqda 3 Ta Burchak</span><span lang="ru">3 Ракурса на Одном Листе</span><span lang="en">3 Angles on Single Sheet</span></span>
      <p style="font-family:'JetBrains Mono',monospace; font-size:9pt;">
        "Character model sheet turnaround, futuristic scout, front view, side view, back view, orthographic projection, plain white background"
      </p>
    </div>
    <div class="lines" style="gap:5mm; padding-top:2mm">
      <i></i><i></i>
    </div>
  </section>

  <section class="sec">
    <div class="h"><span class="no">07</span><h2><span lang="uz">Inventar Ikonkalari (Sprite Sheet)</span><span lang="ru">Иконки Инвентаря (Спрайты)</span><span lang="en">Inventory Icons (Sprite Sheet)</span></h2></div>
    <div class="formula">
      <div class="p"><b>1. Qurol ⚔️</b><span class="d">Plazma qilichi</span></div>
      <div class="p"><b>2. Qalqon 🛡️</b><span class="d">Kvant qalqoni</span></div>
      <div class="p"><b>3. Eliksir 🧪</b><span class="d">Energiya batareyasi</span></div>
      <div class="p"><b>4. Artefakt 🔮</b><span class="d">Qadimiy kiber-chip</span></div>
    </div>
  </section>

  <section class="sec">
    <div class="h"><span class="no">08</span><h2><span lang="uz">Rassomlar Mehnati va Etika</span><span lang="ru">Этика и Авторское Право</span><span lang="en">Art Ethics & Copyright</span></h2></div>
    <p><span lang="uz">AI dan o'yin prototiplari, ilhom va g'oyalar uchun foydalaning. Hech qachon tirik rassomlarning nomini o'g'irlamang va loyihada AI ishlatilganini halol ko'rsating.</span><span lang="ru">Используйте ИИ для прототипов и мудбордов. Уважайте труд живых художников и честно указывайте использование нейросетей.</span><span lang="en">Leverage AI for prototyping and ideation. Respect living artists and credit generative tools transparently.</span></p>
  </section>
"""
l4_hw = """
<p><span lang="uz">O'z o'yin loyihangiz (Roblox, RPG) uchun vizual konsept-paket yarating:</span><span lang="ru">Создайте визуальный концепт-пак для своего игрового проекта:</span><span lang="en">Build a visual concept pack for your game project:</span></p>
<ul class="plain">
  <li><span lang="uz"><b>1. Bosh Qahramon:</b> 5 qismli formula yordamida qahramonning to'liq konseptini yarating.</span><span lang="ru"><b>1. Главный герой:</b> Сгенерируйте концепт по 5-элементной формуле.</span><span lang="en"><b>1. Main Hero:</b> Generate concept art via the 5-element formula.</span></li>
  <li><span lang="uz"><b>2. Biom yoki Buyumlar:</b> 1 ta biom manzarasi yoki 2 ta inventar buyumi suratini oling.</span><span lang="ru"><b>2. Биом или предметы:</b> Арт 1 биома или 2 игровых предметов инвентаря.</span><span lang="en"><b>2. Biome or Gear:</b> 1 biome landscape or 2 distinct inventory items.</span></li>
  <li><span lang="uz"><b>3. Sifat Nazorati:</b> Negative promptlar yordamida artefaktlarni tozalang va rasmlarni saqlang.</span><span lang="ru"><b>3. Чистка артефактов:</b> Очистите баги через negative prompt и сохраните арты.</span><span lang="en"><b>3. Quality Polish:</b> Prune glitches via negative prompts and save outputs.</span></li>
</ul>
"""
l4_crit = """
<div class="row"><span><span lang="uz">5 qismli formula bilan personaj</span><span lang="ru">Персонаж по формуле</span><span lang="en">5-Element Character Art</span></span><b>4</b></div>
<div class="row"><span><span lang="uz">Biom yoki buyumlar konsepti</span><span lang="ru">Концепт биома / лута</span><span lang="en">Biome / Gear Concept</span></span><b>4</b></div>
<div class="row"><span><span lang="uz">Vaqtida topshirilgani</span><span lang="ru">Сдано вовремя</span><span lang="en">On-time Submission</span></span><b>2</b></div>
<div class="row"><span><b><span lang="uz">Jami</span><span lang="ru">Итого</span><span lang="en">Total</span></b></span><b>10</b></div>
"""

out4 = build_worksheet(4, l4_t1, l4_s1, l4_k1, l4_p1, l4_t2, l4_s2, l4_p2, l4_hw, l4_crit, {"uz": "Kiber-Detektiv: Deepfake va AI Xavfsizligi", "ru": "Кибер-Детектив и Безопасность", "en": "Cyber-Detective & AI Safety"})
with open(os.path.join(BASE_DIR, "04-dars-ai-multfilm/varaqa.html"), "w", encoding="utf-8") as f:
    f.write(out4)
print("Saved 04-dars-ai-multfilm/varaqa.html")

# =========================================================================
# LESSON 5 WORKSHEET
# =========================================================================
l5_t1 = {"uz": "Kiber-Detektiv: Deepfake va AI Xavfsizligi", "ru": "Кибер-Детектив: Deepfake и Безопасность ИИ", "en": "Cyber-Detective: Deepfakes & AI Safety"}
l5_s1 = {
  "uz": "Generativ soxta tasvirlar, ovoz klonlash va kiber-fishing botlariga qarshi himoya ko'nikmalari.",
  "ru": "Навыки защиты от дипфейков, клонирования голоса и игровых фишинг-ботов.",
  "en": "Defensive skills against synthetic deepfakes, voice clones, and social engineering bots."
}
l5_k1 = {
  "uz": "Kiber-detektiv sun'iy intellektga ko'r-ko'rona ishonmaydi — u piksellar, ovozlar va dalillarni doim tekshiradi.",
  "ru": "Кибер-детектив не верит ИИ на слово — он проверяет пиксели, звук и факты на прочность.",
  "en": "A cyber-detective never trusts AI blindly — they rigorously fact-check pixels, audio frequencies, and sources."
}
l5_p1 = """
  <section class="sec">
    <div class="h"><span class="no">01</span><h2><span lang="uz">Deepfake Nima?</span><span lang="ru">Что такое Deepfake?</span><span lang="en">What is a Deepfake?</span></h2></div>
    <div class="compare">
      <div class="bad">
        <span class="lbl"><span lang="uz">Oddiy Fotomontaj</span><span lang="ru">Обычный Фотошоп</span><span lang="en">Classic Photo Edit</span></span>
        <p class="pr"><span lang="uz">Qo'lda kesiladi, kattalashtirganda piksellar va qirqilgan chegaralar oson bilinadi.</span><span lang="ru">Ручная склейка. При увеличении всегда видны неровные пиксели и стыки.</span><span lang="en">Manual cut-and-paste. Pixel seams are easily spotted on zoom.</span></p>
      </div>
      <div class="good">
        <span class="lbl"><span lang="uz">AI Deepfake</span><span lang="ru">Генеративный Deepfake</span><span lang="en">Generative Deepfake</span></span>
        <p class="pr"><span lang="uz">Neyrotarmoq yuz mimikasi, lab harakati va ko'z qarashlarini soniyada soxtalashtiradi!</span><span lang="ru">Нейросеть генерирует мимику, движение губ и свет за секунды!</span><span lang="en">Neural nets synthesize facial kinematics, lighting, and lip-sync in seconds!</span></p>
      </div>
    </div>
  </section>

  <section class="sec">
    <div class="h"><span class="no">02</span><h2><span lang="uz">AI Rasmlarini Fosh Qilishning 4 Ta Alomati</span><span lang="ru">4 Улики Против ИИ-Картинки</span><span lang="en">4 Forensic Visual Tells</span></h2></div>
    <div class="trio">
      <div>
        <b><span lang="uz">1. Qo'llar & Barmoqlar</span><span lang="ru">1. Пальцы и Руки</span><span lang="en">1. Hands & Fingers</span></b>
        <span class="d"><span lang="uz">6-7 ta barmoq, g'alati bo'g'inlar, yo'qolgan tirnoqlar.</span><span lang="ru">Лишние пальцы, деформированные суставы.</span><span lang="en">6-7 fingers, deformed joint bends.</span></span>
      </div>
      <div>
        <b><span lang="uz">2. Ko'z Qorachig'i Nuri</span><span lang="ru">2. Блики в Зрачках</span><span lang="en">2. Pupil Reflections</span></b>
        <span class="d"><span lang="uz">Haqiqiy odamda nur ikkala ko'zda bir xil aks etadi.</span><span lang="ru">У человека блики в обоих глазах строго одинаковые.</span><span lang="en">Human eyes share identical specular reflections.</span></span>
      </div>
      <div>
        <b><span lang="uz">3. Fondagi Yozuvlar</span><span lang="ru">3. Текст на Фоне</span><span lang="en">3. Background Text</span></b>
        <span class="d"><span lang="uz">Belgilar va ko'chadagi so'zlar ma'nosiz iyeroglifga aylanadi.</span><span lang="ru">Надписи превращаются в бессмыслицу.</span><span lang="en">Signage mutates into alien hieroglyphics.</span></span>
      </div>
    </div>
  </section>

  <section class="sec">
    <div class="h"><span class="no">03</span><h2><span lang="uz">Ovoz Klonlash va Telefon Firibgarlari</span><span lang="ru">Клоны Голоса и Звонки</span><span lang="en">Voice Spoofing Scams</span></h2></div>
    <div class="formula">
      <div class="p"><b>3 Sekund Audio</b><span class="d">Telegram ovozli xabaridan nusxa</span></div>
      <div class="plus">→</div>
      <div class="p"><b>AI Ovoz Kloni</b><span class="d">Xohlagan gapni uning ovozida aytadi</span></div>
      <div class="plus">→</div>
      <div class="p"><b>Oila Paroli (Safe Word)</b><span class="d">Faqat oila biladigan sirli so'z qalqoni</span></div>
    </div>
  </section>

  <section class="sec">
    <div class="h"><span class="no">04</span><h2><span lang="uz">AI Gallyutsinatsiyasi Nega Xavfli?</span><span lang="ru">Почему Опасны Галлюцинации?</span><span lang="en">Why Hallucinations Are Risky</span></h2></div>
    <ul class="rules">
      <li><span class="t"><span lang="uz"><b>AI haqiqatni bilmaydi:</b> U faqat so'zlarni ehtimollik bo'yicha ulaydi. Shuning uchun uydirmani ham ishonch bilan aytadi.</span><span lang="ru"><b>ИИ не знает фактов:</b> Он соединяет вероятные слова. Поэтому ложь произносится уверенно.</span><span lang="en"><b>AI lacks factual truth:</b> It strings probable words, speaking myths with confidence.</span></span></li>
      <li><span class="t"><span lang="uz"><b>Fakt-cheking majburiy:</b> AI bergan har bir muhim tarixiy, ilmiy yoki tibbiy faktni qidiruv tizimida tekshiring!</span><span lang="ru"><b>Проверка обязательна:</b> Любой важный факт проверяйте в надежных источниках и Google!</span><span lang="en"><b>Mandatory Verification:</b> Cross-reference any historical claim via search engines!</span></span></li>
    </ul>
  </section>
"""

l5_t2 = {"uz": "Kiber-Ekspertiza va Fishingdan Himoya", "ru": "Экспертиза и Защита от Фишинга", "en": "Forensic Audit & Phishing Defense"}
l5_s2 = {
  "uz": "Shubhali o'yin xabarlari, soxta fotosuratlar va akkaunt xavfsizligini tekshirish.",
  "ru": "Проверка подозрительных игровых ссылок, фейковых фото и защита аккаунта.",
  "en": "Auditing suspicious gaming links, fake photos, and locking down accounts."
}
l5_p2 = """
  <section class="sec">
    <div class="h"><span class="no">05</span><h2><span lang="uz">Roblox va Discord Fishing Botlarini Fosh Qilish</span><span lang="ru">Анализ Фишинг-Ботов в Играх</span><span lang="en">Deconstructing Phishing Bots</span></h2></div>
    <div class="compare">
      <div class="bad">
        <span class="lbl"><span lang="uz">Bot Tuzog'i: "Tekinga 10,000 Robux yutdingiz! Havolaga kiring!"</span><span lang="ru">Ловушка: "10 000 Robux бесплатно! Введи пароль тут!"</span><span lang="en">Trap: "Claim 10,000 free Robux! Log in here!"</span></span>
        <div class="lines" style="gap:4mm; padding-top:2mm"><i></i><i></i></div>
      </div>
      <div class="good">
        <span class="lbl"><span lang="uz">Kiber-Detektiv Javobi: (Nega bu xavfli va nima qilish kerak?)</span><span lang="ru">Ответ Детектива: (Почему это фейк?)</span><span lang="en">Detective Action: (Why fake and how to respond?)</span></span>
        <div class="lines" style="gap:4mm; padding-top:2mm"><i></i><i></i></div>
      </div>
    </div>
  </section>

  <section class="sec">
    <div class="h"><span class="no">06</span><h2><span lang="uz">Fakt-Cheking Algoritmi (3 Qadam)</span><span lang="ru">Алгоритм Факт-Чекинга (3 Шага)</span><span lang="en">Fact-Checking Protocol (3 Steps)</span></h2></div>
    <div class="scroll-x">
      <table>
        <thead>
          <tr>
            <th style="width:33%">1. Reverse Image Search</th>
            <th style="width:33%">2. EXIF Metama'lumotlar</th>
            <th style="width:34%">3. Asl Rasmiy Manba</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><span lang="uz">Rasmni qidiruvga tashlab, qachon paydo bo'lganini topish.</span><span lang="ru">Поиск первоисточника картинки по дате публикации.</span><span lang="en">Reverse lookup to trace first upload date.</span></td>
            <td><span lang="uz">Fayl kameradanmi yoki generatordan chiqqanini ko'rish.</span><span lang="ru">Проверка камеры или графического редактора.</span><span lang="en">Inspect camera tags or AI rendering meta.</span></td>
            <td><span lang="uz">Xalqaro rasmiy xabar saytlarida tasdiq borligini tekshirish.</span><span lang="ru">Поиск подтверждения на официальных сайтах.</span><span lang="en">Confirming via primary news sources.</span></td>
          </tr>
        </tbody>
      </table>
    </div>
  </section>

  <section class="sec">
    <div class="h"><span class="no">07</span><h2><span lang="uz">Kuchli Parol Formulasi</span><span lang="ru">Формула Надежного Пароля</span><span lang="en">Strong Password Formula</span></h2></div>
    <div class="key">
      <span class="k"><span lang="uz">Kiber-Zirh Qoidasi</span><span lang="ru">Броня Безопасности</span><span lang="en">Security Armor</span></span>
      <p style="font-family:'JetBrains Mono',monospace; font-size:9.5pt;">
        <span lang="uz">12+ belgi: Katta harf + Kichik harf + Raqam + Maxsus belgi (!@#$) + <b>2FA</b> (Ikki bosqichli kod)!</span>
        <span lang="ru">12+ символов: Заглавная + Строчная + Цифры + Спецзнаки (!@#$) + <b>2FA</b> (СМС-код)!</span>
        <span lang="en">12+ characters: Upper + Lower + Digits + Symbols (!@#$) + Mandatory <b>2FA</b>!</span>
      </p>
    </div>
    <div class="lines" style="gap:4mm; padding-top:2mm"><i></i></div>
  </section>

  <section class="sec">
    <div class="h"><span class="no">08</span><h2><span lang="uz">Raqamli Gigiyena Qoidalari</span><span lang="ru">Правила Цифровой Гигиены</span><span lang="en">Digital Hygiene Rules</span></h2></div>
    <p><span lang="uz">Begona odamlardan kelgan fayl va havolalarni ochmang. O'yin do'konlarida login parolingizni hech qachon boshqalar bilan bo'lishmang!</span><span lang="ru">Не открывайте подозрительные файлы и ссылки. Никогда не делитесь паролями от игр и почты!</span><span lang="en">Never open unknown links or attachments. Never share gaming account credentials with anyone!</span></p>
  </section>
"""
l5_hw = """
<p><span lang="uz">Oila a'zolaringiz va do'stlaringiz uchun amaliy kiber-xavfsizlik qo'llanmasini tayyorlang:</span><span lang="ru">Создайте памятку кибербезопасности для своей семьи и друзей:</span><span lang="en">Engineer a practical cyber-safety field guide for family and friends:</span></p>
<ul class="plain">
  <li><span lang="uz"><b>1. AI Soxta Surat Tahlili:</b> Internetdan 1 ta AI soxta suratini toping va 3 ta vizual xatosini ko'rsating.</span><span lang="ru"><b>1. Анализ фейка:</b> Найдите 1 ИИ-картинку и выпишите 3 улики.</span><span lang="en"><b>1. AI Fake Audit:</b> Find 1 AI image and document 3 forensic glitches.</span></li>
  <li><span lang="uz"><b>2. O'yin Xavfsizligi Qoidalari:</b> O'yin hisoblarini (Roblox, Discord) asrash bo'yicha 4 ta oltin qoida tuzing.</span><span lang="ru"><b>2. Защита аккаунтов:</b> 4 правила защиты профилей в играх.</span><span lang="en"><b>2. Gaming Defense:</b> 4 golden rules protecting game accounts.</span></li>
  <li><span lang="uz"><b>3. Oila Paroli (Safe Word):</b> Telefon firibgarlariga qarshi oilaviy maxfiy so'zni kelishib oling.</span><span lang="ru"><b>3. Семейный пароль:</b> Придумайте секретное кодовое слово.</span><span lang="en"><b>3. Family Passphrase:</b> Establish a family emergency secret word.</span></li>
</ul>
"""
l5_crit = """
<div class="row"><span><span lang="uz">Soxta surat tahlili</span><span lang="ru">Анализ артефактов фейка</span><span lang="en">AI Image Forensic Proof</span></span><b>4</b></div>
<div class="row"><span><span lang="uz">Xavfsizlik qoidalari</span><span lang="ru">Чек-лист безопасности</span><span lang="en">Account Safety Checklist</span></span><b>4</b></div>
<div class="row"><span><span lang="uz">Vaqtida topshirilgani</span><span lang="ru">Сдано вовремя</span><span lang="en">On-time Submission</span></span><b>2</b></div>
<div class="row"><span><b><span lang="uz">Jami</span><span lang="ru">Итого</span><span lang="en">Total</span></b></span><b>10</b></div>
"""

out5 = build_worksheet(5, l5_t1, l5_s1, l5_k1, l5_p1, l5_t2, l5_s2, l5_p2, l5_hw, l5_crit, {"uz": "Game Pitch va Digital Expo: Demo Day", "ru": "Гейм-Питч и Demo Day", "en": "Game Pitch & Demo Day"})
with open(os.path.join(BASE_DIR, "05-dars-ai-siri-va-detektiv/varaqa.html"), "w", encoding="utf-8") as f:
    f.write(out5)
print("Saved 05-dars-ai-siri-va-detektiv/varaqa.html")

# =========================================================================
# LESSON 6 WORKSHEET
# =========================================================================
l6_t1 = {"uz": "Game Pitch va Digital Expo: Demo Day", "ru": "Гейм-Питч и Цифровое Экспо: Demo Day", "en": "Game Pitch & Digital Expo: Demo Day"}
l6_s1 = {
  "uz": "1 hafta davomida yaratilgan o'yin olami, NPC personajlari va konsept-artlarni taqdim etish va himoya qilish.",
  "ru": "Презентация и защита игрового проекта, персонажей и концепт-артов перед аудиторией.",
  "en": "Showcasing and defending your week 1 game world, NPCs, and concept art showcase."
}
l6_k1 = {
  "uz": "Geym-pitch san'ati — o'z virtual olami, NPC botlari va yangiligini 2 daqiqada ishonarli ko'rsatib berishdir.",
  "ru": "Искусство питча — это умение за 2 минуты доказать инвесторам и игрокам уникальность своего мира.",
  "en": "The art of game pitching is proving your world, characters, and core game loop in a 2-minute compelling showcase."
}
l6_p1 = """
  <section class="sec">
    <div class="h"><span class="no">01</span><h2><span lang="uz">Geym-Pitch Nima?</span><span lang="ru">Что такое Гейм-Питч?</span><span lang="en">What is a Game Pitch?</span></h2></div>
    <div class="compare">
      <div class="bad">
        <span class="lbl"><span lang="uz">Zerikarli Taqdimot</span><span lang="ru">Скучный Рассказ</span><span lang="en">Boring Monologue</span></span>
        <p class="pr"><span lang="uz">Mavhum gaplar: "O'yinimda bir odam yuradi, qiziq narsalar bor". Aniq g'oya va energiya yo'q.</span><span lang="ru">Вялые слова: "Ну там человечек ходит, вроде прикольно". Нет энергии и идеи.</span><span lang="en">Vague rambling: "A guy runs around, it's cool". Zero hook or energy.</span></p>
      </div>
      <div class="good">
        <span class="lbl"><span lang="uz">G'olib Geym-Pitch</span><span lang="ru">Победный Питч</span><span lang="en">Winning Game Pitch</span></span>
        <p class="pr"><span lang="uz">"2150-yil, suzuvchi shahar! Siz kiber-muhandissiz. AI botlar bilan savdo qilib, reaktorni qutqarasiz!"</span><span lang="ru">"2150 год, парящий город! Вы — инженер, торгуете с ИИ-ботами и спасаете реактор!"</span><span lang="en">"Year 2150! Floating sky city. You are an engineer bargaining with AI NPCs to save grid!"</span></p>
      </div>
    </div>
  </section>

  <section class="sec">
    <div class="h"><span class="no">02</span><h2><span lang="uz">High Concept Formulasi</span><span lang="ru">Формула High Concept</span><span lang="en">High Concept Formula</span></h2></div>
    <div class="formula">
      <div class="p"><b>1. Janr</b><span class="d">Roblox Sandbox RPG</span></div>
      <div class="plus">+</div>
      <div class="p"><b>2. Bosh Mexanika</b><span class="d">Omon qolish va savdo</span></div>
      <div class="plus">+</div>
      <div class="p"><b>3. X-Faktor (Yangilik)</b><span class="d">Generativ AI NPC lar!</span></div>
    </div>
  </section>

  <section class="sec">
    <div class="h"><span class="no">03</span><h2><span lang="uz">Pitch Deckning 4 Asosiy Sahifasi</span><span lang="ru">4 Слайда Питч-Дека</span><span lang="en">4 Pitch Deck Slides</span></h2></div>
    <div class="trio">
      <div>
        <b><span lang="uz">1. Vizitka & Konsept</span><span lang="ru">1. Визитка и Идея</span><span lang="en">1. Hook & Title</span></b>
        <span class="d"><span lang="uz">O'yin nomi, logotipi va bosh shiori.</span><span lang="ru">Название, логотип и слоган проекта.</span><span lang="en">Title, logo, and core tagline.</span></span>
      </div>
      <div>
        <b><span lang="uz">2. Dunyo Loresi & Biom</span><span lang="ru">2. Лор и Биомы</span><span lang="en">2. Lore & Biomes</span></b>
        <span class="d"><span lang="uz">Xarita, 2 ta fraksiya va katta konflikt.</span><span lang="ru">Карта, 2 фракции и главный конфликт.</span><span lang="en">Map, 2 factions, and main conflict.</span></span>
      </div>
      <div>
        <b><span lang="uz">3. AI NPC & Art</span><span lang="ru">3. AI NPC и Арт</span><span lang="en">3. NPC & Concept Art</span></b>
        <span class="d"><span lang="uz">Jonli bot dialogi va Character Sheet.</span><span lang="ru">Живой бот и модельный лист героя.</span><span lang="en">Live bot dialogue and character sheet.</span></span>
      </div>
    </div>
  </section>

  <section class="sec">
    <div class="h"><span class="no">04</span><h2><span lang="uz">Jonli Namoyish (Live Demo) Qoidalari</span><span lang="ru">Правила Live Demo</span><span lang="en">Live Demo Protocols</span></h2></div>
    <ul class="rules">
      <li><span class="t"><span lang="uz"><b>Zaldan savol oling:</b> Sinfdoshlarga bot bilan muloqot qilish imkonini bering.</span><span lang="ru"><b>Вопрос из зала:</b> Дайте одноклассникам возможность протестировать бота.</span><span lang="en"><b>Audience Test:</b> Let classmates challenge the NPC with an in-game question.</span></span></li>
      <li><span class="t"><span lang="uz"><b>Xarakterni isbotlang:</b> Bot hech qanday hiyla bilan roldan chiqmaganini namoyish eting.</span><span lang="ru"><b>Держите образ:</b> Докажите, что бот выдержал характер без срывов.</span><span lang="en"><b>Guardrail Proof:</b> Demonstrate the NPC holds persona against jailbreaks.</span></span></li>
    </ul>
  </section>
"""

l6_t2 = {"uz": "Playtesting, Feedback va Game Design Document", "ru": "Плейтест, Фидбек и GDD", "en": "Playtesting, Feedback & GDD"}
l6_s2 = {
  "uz": "Demo Day taqdimoti, sinfdoshlar fikrini qayd qilish va loyihani to'liq jamlash.",
  "ru": "Презентация на Demo Day, сбор отзывов плейтестеров и сборка итогового GDD.",
  "en": "Demo Day presentation, capturing playtest feedback, and compiling the master GDD."
}
l6_p2 = """
  <section class="sec">
    <div class="h"><span class="no">05</span><h2><span lang="uz">30 Soniyalik Elevator Pitch Matnini Yozing</span><span lang="ru">Напишите Текст 30-секундного Питча</span><span lang="en">Draft 30-Second Elevator Pitch</span></h2></div>
    <div class="key">
      <span class="k"><span lang="uz">Taqdimot Matni</span><span lang="ru">Речь Питча</span><span lang="en">Pitch Speech</span></span>
      <p><span lang="uz">"Mening o'yinim nomi — [____]. Bu [____] janridagi o'yin. Unda o'yinchi [____] qiladi va o'ziga xosligi [____] hisoblanadi!"</span><span lang="ru">"Моя игра называется [____]. Это игра в жанре [____]. В ней игрок [____], а главная фишка — [____]!"</span><span lang="en">"My game is called [____]. It is a [____] game where players [____] and the unique hook is [____]!"</span></p>
    </div>
    <div class="lines">
      <i></i><i></i><i></i>
    </div>
  </section>

  <section class="sec">
    <div class="h"><span class="no">06</span><h2><span lang="uz">Live Demo: Botga 2 Ta Sinov Savoli</span><span lang="ru">Live Demo: 2 Вопроса Боту</span><span lang="en">Live Demo: 2 Test Queries</span></h2></div>
    <div class="scroll-x">
      <table>
        <thead>
          <tr>
            <th style="width:50%"><span lang="uz">Auditoriya Savoli</span><span lang="ru">Вопрос Аудитории</span><span lang="en">Audience Question</span></th>
            <th style="width:50%"><span lang="uz">Botning Roldagi Javobi</span><span lang="ru">Ответ Бота в Образе</span><span lang="en">In-Character Bot Reply</span></th>
          </tr>
        </thead>
        <tbody>
          <tr><td></td><td></td></tr>
          <tr><td></td><td></td></tr>
        </tbody>
      </table>
    </div>
  </section>

  <section class="sec">
    <div class="h"><span class="no">07</span><h2><span lang="uz">Sinfdoshlar Fikr-Mulohazalari (Feedback Grid)</span><span lang="ru">Отзывы Одноклассников</span><span lang="en">Playtester Feedback Grid</span></h2></div>
    <div class="scroll-x">
      <table>
        <thead>
          <tr>
            <th style="width:25%"><span lang="uz">Sinfdosh Ismi</span><span lang="ru">Имя Одноклассника</span><span lang="en">Peer Name</span></th>
            <th style="width:40%"><span lang="uz">Eng Yoqqan Qismi</span><span lang="ru">Что Понравилось</span><span lang="en">What Worked Best</span></th>
            <th style="width:35%"><span lang="uz">Yaxshilash Uchun Maslahat</span><span lang="ru">Совет по Улучшению</span><span lang="en">Improvement Idea</span></th>
          </tr>
        </thead>
        <tbody>
          <tr><td></td><td></td><td></td></tr>
          <tr><td></td><td></td><td></td></tr>
        </tbody>
      </table>
    </div>
  </section>

  <section class="sec">
    <div class="h"><span class="no">08</span><h2><span lang="uz">Reliz Rejasi: Roadmap</span><span lang="ru">Дорожная Карта: Roadmap</span><span lang="en">Roadmap to Launch</span></h2></div>
    <p><span lang="uz">1-Bosqich (GDD hujjati tayyor) → 2-Bosqich (Roblox Studio / Web dvigatelga ko'chirish) → 3-Bosqich (Do'stlar uchun ommaviy reliz)!</span><span lang="ru">Этап 1 (GDD документ готов) → Этап 2 (Сборка в Roblox Studio) → Этап 3 (Публичный релиз для друзей)!</span><span lang="en">Phase 1 (GDD ready) → Phase 2 (Roblox Studio / Web build) → Phase 3 (Public launch for friends)!</span></p>
  </section>
"""
l6_hw = """
<p><span lang="uz">1-hafta davomida yaratilgan barcha ishlaringizni yagona "Game Design Document" (GDD) ga jamlang:</span><span lang="ru">Соберите все наработки недели в единый Game Design Document (GDD):</span><span lang="en">Consolidate all week 1 outputs into a complete Game Design Document (GDD):</span></p>
<ul class="plain">
  <li><span lang="uz"><b>1. To'liq GDD To'plami:</b> High Concept, Dunyo loresi, NPC System Prompti va Konsept-artlar.</span><span lang="ru"><b>1. Полный пакет GDD:</b> High Concept, лор, System Prompt и концепт-арты.</span><span lang="en"><b>1. Complete GDD:</b> High Concept, lore, NPC System Prompt, and art pack.</span></li>
  <li><span lang="uz"><b>2. Sinfdoshlar Fikri:</b> Demo Day davomida olingan 3 ta eng foydali taklifni yozing.</span><span lang="ru"><b>2. Фидбек:</b> Запишите 3 главных отзыва с Demo Day.</span><span lang="en"><b>2. Feedback:</b> Record 3 key actionable takeaways from Demo Day.</span></li>
  <li><span lang="uz"><b>3. Portfolio:</b> O'z kelajak geymdev portfoliongiz uchun raqamli papkani saqlang.</span><span lang="ru"><b>3. Портфолио:</b> Оформите цифровую папку проекта разработчика.</span><span lang="en"><b>3. Portfolio:</b> Archive the project into your digital creator portfolio.</span></li>
</ul>
"""
l6_crit = """
<div class="row"><span><span lang="uz">To'liq GDD hujjati</span><span lang="ru">Полный пакет GDD</span><span lang="en">Complete GDD Package</span></span><b>4</b></div>
<div class="row"><span><span lang="uz">Ko'rgazmadagi taqdimot</span><span lang="ru">Защита на Demo Day</span><span lang="en">Demo Day Presentation</span></span><b>4</b></div>
<div class="row"><span><span lang="uz">Vaqtida topshirilgani</span><span lang="ru">Сдано вовремя</span><span lang="en">On-time Submission</span></span><b>2</b></div>
<div class="row"><span><b><span lang="uz">Jami</span><span lang="ru">Итого</span><span lang="en">Total</span></b></span><b>10</b></div>
"""

out4 = build_worksheet(4, l4_t1, l4_s1, l4_k1, l4_p1, l4_t2, l4_s2, l4_p2, l4_hw, l4_crit, {"uz": "Kiber-Detektiv: Deepfake va AI Xavfsizligi", "ru": "Кибер-Детектив и Безопасность", "en": "Cyber-Detective & AI Safety"})
with open(os.path.join(BASE_DIR, "04-dars-ai-multfilm/varaqa.html"), "w", encoding="utf-8") as f:
    f.write(out4)
print("Saved 04-dars-ai-multfilm/varaqa.html")

out5 = build_worksheet(5, l5_t1, l5_s1, l5_k1, l5_p1, l5_t2, l5_s2, l5_p2, l5_hw, l5_crit, {"uz": "Game Pitch va Digital Expo: Demo Day", "ru": "Гейм-Питч и Demo Day", "en": "Game Pitch & Demo Day"})
with open(os.path.join(BASE_DIR, "05-dars-ai-siri-va-detektiv/varaqa.html"), "w", encoding="utf-8") as f:
    f.write(out5)
print("Saved 05-dars-ai-siri-va-detektiv/varaqa.html")

out6 = build_worksheet(6, l6_t1, l6_s1, l6_k1, l6_p1, l6_t2, l6_s2, l6_p2, l6_hw, l6_crit, {"uz": "2-Hafta: Agentic AI va VS Code bilan Dasturlash", "ru": "2-я Неделя: Agentic AI и VS Code", "en": "Week 2: Agentic AI & Coding in VS Code"})
with open(os.path.join(BASE_DIR, "06-dars-sehrli-korgazma/varaqa.html"), "w", encoding="utf-8") as f:
    f.write(out6)
print("Saved 06-dars-sehrli-korgazma/varaqa.html")
