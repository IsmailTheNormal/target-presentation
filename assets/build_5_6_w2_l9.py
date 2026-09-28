#!/usr/bin/env python3
import os, sys
sys.path.insert(0, '/home/dpdp/target/assets')
from curriculum_generator import build_presentation, build_worksheet

BASE = '/home/dpdp/target/classes/5-6-sinf/2-hafta'
l9_dir = os.path.join(BASE, '09-dars-ovoz-va-effektlar-sfx')
os.makedirs(l9_dir, exist_ok=True)

l9_slides = """
<section class="slide is-on" data-phase="Kirish|Вступление|Opening" data-time="0–3">
  <div class="title-wrap">
    <div class="eyebrow">Vibecoding · <span data-ru="урок 9 · 5-6 классы" data-en="lesson 9 · grades 5-6">9-dars · 5-6 sinflar</span></div>
    <div class="title-meta">
      <span><b lang="uz">Fan:</b><span data-ru=" IT / Vibecoding" data-en=" IT / Vibecoding"> IT / Vibecoding</span><b lang="ru">Предмет:</b><span lang="ru"> IT / Vibecoding</span><b lang="en">Subject:</b><span lang="en"> IT / Vibecoding</span></span>
      <span><b lang="uz">Hafta:</b><span data-ru=" 2" data-en=" 2"> 2</span><b lang="ru">Неделя:</b><span lang="ru"> 2</span><b lang="en">Week:</b><span lang="en"> 2</span></span>
    </div>
    <h1 data-ru="Магия Игрового Звука: AI SFX, Музыка и Атмосфера" data-en="Game Audio Magic: AI SFX, Music & Dynamic Ambience">O'yin Ovozlar Sehri: AI SFX, Musiqa va Dinamik Atmosfera</h1>
    <p class="lede" data-ru="Звук — это 50% эмоций в игре! Почему без щелчков и взрывов игра кажется мертвой? Создаем звуковые эффекты (SFX) и саундтрек с помощью ИИ." data-en="Audio accounts for 50% of immersion! Why do silent games feel lifeless? Synthesizing sound effects (SFX) and dynamic game soundtracks with AI.">Ovoz — o'yindagi hissiyotlarning 50 foizidir! Nega ovozsiz o'yin jonsiz tuyuladi? AI yordamida harakat tovushlari (SFX) va o'yin musiqasini yaratamiz.</p>
  </div>
</section>

<section class="slide" data-phase="Tushuncha|Сила звука|Audio Immersion" data-time="3–7">
  <div class="eyebrow"><span data-ru="Психология звука" data-en="Audio Psychology">Ovoz Psixologiyasi</span></div>
  <h2 data-ru="Сила Звука: Почему Глаза Верят Ушам" data-en="The Power of Audio: Why Eyes Believe Ears">Ovozning Kuchi: Ko'zlar Quloqlarga Nega Ishonadi?</h2>
  <p data-ru="Даже самая красивая 3D-графика выглядит картонной, если шаги и удары не звучат сочно:" data-en="Even photorealistic 3D environments feel lifeless if footsteps and hits lack punch:">Eng chiroyli 3D grafika ham, agar qadamlar va zarbalar ovozsiz bo'lsa, jonsiz va soxta ko'rinadi:</p>
  <div class="cols c2" style="margin-top:15px;">
    <div class="box">
      <h3 style="color:var(--ink-2);" data-ru="Игра без звука (Тишина) 🔇" data-en="Silent Game 🔇">Ovozsiz O'yin (Sukut) 🔇</h3>
      <p data-ru="Игрок нажимает на кнопку удара мечом, но ничего не слышит. Удар кажется слабым, кнопки кажутся неработающими. Погружение рушится." data-en="Swinging a plasma blade produces zero acoustic feedback. Hits feel weightless, controls feel unresponsive.">Qilich bilan zarba berganda hech qanday tovush eshitilmaydi. Zarba kuchsizdek tuyuladi, o'yin qiziqarsiz bo'lib qoladi.</p>
    </div>
    <div class="box" style="border-left:4px solid var(--accent);">
      <h3 style="color:var(--accent);" data-ru="Сочный Саунд-Дизайн (SFX) 🔊" data-en="Punchy Sound Design 🔊">Shirali SFX va Musiqa 🔊</h3>
      <p data-ru="Гул лазера, звон монет с басом и тревожная музыка! Мозг выбрасывает дофамин от каждого точного клика." data-en="Humming lasers, bass-boosted coin chimes, and adaptive combat music trigger immediate dopamine rewards.">Lazerning g'uvillashi, tanga olgandagi jiringlash va hayajonli musiqa! Har bir harakat o'yinchiga zavq va g'alaba hissini beradi.</p>
    </div>
  </div>
</section>

<section class="slide" data-phase="Qatlamlar|3 Слоя Звука|3 Audio Layers" data-time="7–11">
  <div class="eyebrow"><span data-ru="Аудио-архитектура" data-en="Audio Hierarchy">Audio Arxitekturasi</span></div>
  <h2 data-ru="3 Главных Слоя Звука в Любой Игре" data-en="The 3 Core Audio Layers of Interactive Games">O'yindagi Tovushning 3 Ta Asosiy Qatlami</h2>
  <p data-ru="Профессиональный саундтрек игры состоит из трех параллельных дорожек:" data-en="A professional game audio mix balances three independent acoustic layers:">Professional o'yin tovushi 3 ta alohida yo'nalishdan yig'iladi:</p>
  <div class="cols c3" style="display:grid; grid-template-columns:1fr 1fr 1fr; gap:12px; margin-top:12px;">
    <div class="box" style="border-top:4px solid var(--accent);">
      <h3 style="color:var(--accent);" data-ru="1. SFX (Эффекты) 💥" data-en="1. SFX (Effects) 💥">1. SFX (Harakat Ovozlar) 💥</h3>
      <p data-ru="Короткие звуки действий: прыжок, выстрел лазера, сбор монет, открытие сундука (длина 0.2–2 сек)." data-en="Micro-actions: jump, laser shot, coin pickup, chest opening (0.2–2 sec length).">Qisqa harakat tovushlari: sakrash, lazer otilishi, tanga olish, sandiq ochilishi (0.2–2 soniya).</p>
    </div>
    <div class="box" style="border-top:4px solid var(--green);">
      <h3 style="color:var(--green);" data-ru="2. BGM (Фоновая музыка) 🎵" data-en="2. BGM (Music) 🎵">2. BGM (Fon Musiqasi) 🎵</h3>
      <p data-ru="Бесконечный луп (Loop): спокойная мелодия исследования или адреналиновый рок для битвы с боссом." data-en="Seamless audio loop: atmospheric exploration synth or adrenaline boss rock.">Uzluksiz fon musiqasi (Loop): xaritani kezishdagi sokin kuy yoki boss bilan jangdagi shiddatli musiqa.</p>
    </div>
    <div class="box" style="border-top:4px solid #00E5FF;">
      <h3 style="color:#00838F;" data-ru="3. Эмбиент (Окружение) 🍃" data-en="3. Ambience 🍃">3. Atrof-muhit (Ambient) 🍃</h3>
      <p data-ru="Шум ветра в горах, гул турбин на космической базе, капли воды в темной пещере." data-en="Wind howling over dunes, distant humming engine reactors, cave water droplets.">Tog'lardagi shamol shovqini, kosmik stansiya turbinalari g'uvillashi, g'ordagi suv tomchilari.</p>
    </div>
  </div>
</section>

<section class="slide" data-phase="Mexanizm|Генерация звука с ИИ|AI Audio Engines" data-time="11–15">
  <div class="eyebrow"><span data-ru="Генерация аудио" data-en="Generative Audio">AI Audio Qanday Ishlaydi?</span></div>
  <h2 data-ru="Как ИИ Синтезирует Звуки из Текстового Описания" data-en="How AI Synthesizes Audio from Text Prompts">AI Qanday Qilib Matn Asosida Tovush Yaratadi?</h2>
  <p data-ru="Сервисы вроде ElevenLabs SFX и Suno создают звуки по частотным спектрограммам:" data-en="Audio engines like ElevenLabs Sound Effects and Suno generate audio from acoustic spectrograms:">Zamonaviy AI audio generatorlar (ElevenLabs SFX, Suno) chastotalar to'lqinini matndan sintez qiladi:</p>
  <ul class="rules">
    <li><span class="t" data-ru="<b>1. Текстовое описание физики:</b> Указываем действие, материал и акустику (например: тяжелый железный люк с эхом)." data-en="<b>1. Acoustic Physics Description:</b> Define action, material resonance, and reverb space."><b>1. Tovush fizikasini tasvirlash:</b> Harakat, material va aks-sado (masalan: aks-sado beruvchi og'ir temir lyuk yopilishi).</span></li>
    <li><span class="t" data-ru="<b>2. Диффузия звуковой волны:</b> ИИ генерирует звуковой шум и очищает его до чистого звукового сэмпла." data-en="<b>2. Waveform Diffusion:</b> AI generates acoustic noise and refines it into a pristine audio sample."><b>2. Tovush to'lqini diffuziyasi:</b> AI shovqindan boshlab uni toza musiqiy yoki mexanik signalga aylantiradi.</span></li>
    <li><span class="t" data-ru="<b>3. Бесшовный луп (Looping):</b> Для фоновой музыки важно, чтобы конец трека плавно перетекал в начало." data-en="<b>3. Seamless Looping:</b> For background music, ensure the tail smoothly crossfades back into the head."><b>3. Choksiz takrorlanish (Loop):</b> Fon musiqasi tugaganda hech qanday pauzasiz yana boshidan ulanib ketishi shart.</span></li>
  </ul>
</section>

<section class="slide" data-phase="Ko'rsatma|Формула SFX|SFX Prompt Formula" data-time="15–19">
  <div class="eyebrow"><span data-ru="Промпт-инжиниринг звука" data-en="Audio Prompting">SFX Prompt Formulasi</span></div>
  <h2 data-ru="Формула SFX-Промпта из 4 Компонентов" data-en="The 4-Part SFX Audio Prompt Formula">Professional O'yin SFX Promptining 4 Qismi</h2>
  <div class="box" style="background:var(--panel); border-left:5px solid var(--green); padding:16px;">
    <p style="font-family:monospace; font-size:0.95em; line-height:1.6;" data-ru="<b>[ДЕЙСТВИЕ]</b> Сбор энергетического кристалла<br>+ <b>[МАТЕРИАЛ / ТЕМБР]</b> Высокий хрустальный перезвон, синтезаторный аккорд<br>+ <b>[ДИНАМИКА]</b> Резкая быстрая атака, затухание 0.8 секунд<br>+ <b>[СТИЛЬ]</b> 8-bit arcade retro chiptune / modern sci-fi game UI" data-en="<b>[ACTION]</b> Energy crystal harvest pickup<br>+ <b>[TIMBRE]</b> High-pitched glass chime, sparkling synthesizer chord<br>+ <b>[DYNAMICS]</b> Crisp fast attack, 0.8s tail decay, zero background noise<br>+ <b>[STYLE]</b> Modern sci-fi UI notification or retro chiptune arcade">
      <b>1. HARAKAT:</b> Energiya kristalini terib olish (pickup)<br>
      + <b>2. TEMBR VA MATERIAL:</b> Mayin billur jaranglashi, kiber-sintezator akkordi<br>
      + <b>3. DINAMIKA:</b> Tezkor boshlanish (fast attack), 0.8 soniyali aks-sado (reverb decay)<br>
      + <b>4. O'YIN USLUBI:</b> Modern sci-fi game UI sound effect, toza audio
    </p>
  </div>
  <p style="margin-top:12px; font-size:0.9em; color:var(--ink-2);" data-ru="Ключевое слово 'UI sound effect' или 'game SFX' отсекает лишний шум и разговоры людей!" data-en="Keywords like 'UI sound effect' and 'isolated game SFX' prevent unwanted vocal noise!">"UI sound effect" va "isolated game SFX" so'zlari keraksiz fon shovqinlari va odam ovozlari aralashishining oldini oladi!</p>
</section>

<section class="slide" data-phase="Sinov|Ошибки звука|Audio Pitfalls" data-time="19–23">
  <div class="eyebrow"><span data-ru="Звуковые ошибки" data-en="Audio Pitfalls">Ovoz Xatolari</span></div>
  <h2 data-ru="3 Звуковые Ошибки, Раздражающие Игроков" data-en="3 Audio Mistakes That Annoy Gamers">O'yinchilarning Jahlini Chiqaruvchi 3 Ovoz Xatosi</h2>
  <p data-ru="Плохой звук может испортить даже идеальную игру. Избегайте этих 3 ловушек:" data-en="Bad audio ruins immersion instantly. Guard against these three fatal traps:">Yomon ovoz tufayli o'yinchi tovushni butunlay o'chirib qo'yadi. Quyidagi 3 xatoga yo'l qo'ymang:</p>
  <div class="cols c3" style="display:grid; grid-template-columns:1fr 1fr 1fr; gap:12px; margin-top:12px;">
    <div class="box" style="border-top:4px solid var(--accent);">
      <h3 style="color:var(--accent);" data-ru="1. Слишком громко (Clipping) 📢" data-en="1. Ear-Rape Clipping 📢">1. Quloqni Yirtuvchi Shovqin 📢</h3>
      <p data-ru="Если выстрел пистолета бьет по ушам громче музыки в 5 раз, игрок выключит звук навсегда." data-en="Blasting lasers 5x louder than music destroys hearing and prompts instant mute.">Agar o'q ovozi musiqadan 5 baravar baland bo'lib quloqni og'ritsa, o'yinchi ovozni o'chiradi.</p>
    </div>
    <div class="box" style="border-top:4px solid var(--accent);">
      <h3 style="color:var(--accent);" data-ru="2. Задержка (Latency) ⏱️" data-en="2. Audio Latency Lag ⏱️">2. Tovush Kechikishi (Latency) ⏱️</h3>
      <p data-ru="Игрок нажал пробел, прыгнул, приземлился — и только потом слышит 'Бум'. Звук обязан звучать синхронно!" data-en="Hearing the jump 'thud' 1 second after landing feels broken and laggy.">O'yinchi sakrab yerga tushgandan 1 soniya o'tib tovush chiqsa, o'yin qotayotgandek tuyuladi.</p>
    </div>
    <div class="box" style="border-top:4px solid var(--green);">
      <h3 style="color:var(--green);" data-ru="3. Нудный повтор (Fatigue) 🔄" data-en="3. Repetitive Fatigue 🔄">3. Zerikarli Takrorlanish 🔄</h3>
      <p data-ru="Один и тот же звук шагов каждые 0.3 секунды сводит с ума. В играх делают 3-4 вариации шага." data-en="Hearing the exact same footstep pitch 200 times induces auditory fatigue. Vary pitch!">Har qadamda bir xil tovush takrorlansa quloq charchaydi. Harakatlar uchun 2-3 xil ohang kerak.</p>
    </div>
  </div>
</section>

<section class="slide" data-phase="Vazifa|Миссия урока|Audio Mission" data-time="23–27">
  <div class="eyebrow"><span data-ru="Практическая миссия" data-en="Audio Lab Mission">Amaliy Vazifa</span></div>
  <h2 data-ru="Миссия: Собрать Аудио-Пак для Своего Проекта" data-en="Mission: Construct the Core Game Audio Pack">Bugungi Vazifa: O'yin Loyihangiz Uchun Audio To'plam Yig'ing</h2>
  <p data-ru="Используя рабочий лист и генератор ИИ, создайте и зафиксируйте звуковой пак из 4 элементов:" data-en="Using your worksheet blueprint and AI audio tools, synthesize 4 flagship sound assets:">Varaqadagi jadval va AI generator yordamida o'z loyihangiz uchun 4 ta tovushni yarating:</p>
  <ul class="rules">
    <li><span class="t" data-ru="<b>1. Звук прыжка / рывка:</b> Быстрый свист ветра или импульс джетпака (0.5 сек)." data-en="<b>1. Jump / Dash SFX:</b> Quick wind whoosh or jetpack burst (0.5 sec)."><b>1. Sakrash / Tezlanish SFX:</b> Shamol shiddati yoki jetpak tutuni (0.5 soniya).</span></li>
    <li><span class="t" data-ru="<b>2. Звук сбора награды:</b> Приятный перезвон монеты или кристалла (0.8 сек)." data-en="<b>2. Loot Pickup SFX:</b> Satisfying crystal or coin pickup chime (0.8 sec)."><b>2. Mukofot SFX:</b> Tanga yoki kristall terib olgandagi yoqimli jaranglash (0.8 soniya).</span></li>
    <li><span class="t" data-ru="<b>3. Звук ловушки / урона:</b> Предупреждающий сигнал или треск электричества (1 сек)." data-en="<b>3. Trap / Damage SFX:</b> Warning buzz or electric discharge zap (1.0 sec)."><b>3. Ziyon / Tuzoq SFX:</b> Elektr toki urishi yoki ogohlantiruvchi signal (1.0 soniya).</span></li>
    <li><span class="t" data-ru="<b>4. Фоновый трек (BGM):</b> 15-секундный луп саундтрека биома (Suno AI)." data-en="<b>4. Ambient Soundtrack (BGM):</b> 15-second looping biome soundtrack (Suno AI)."><b>4. Asosiy fon musiqasi (BGM):</b> O'yin biomingizga mos 15 soniyalik fon kuyi (Suno AI).</span></li>
  </ul>
</section>

<section class="slide" data-phase="Amaliyot|Аудио-Спринт|Audio Sprint" data-time="27–31">
  <div class="eyebrow"><span data-ru="Инженерный спринт" data-en="Audio Sprint">Jonli Amaliyot · Taymer</span></div>
  <h2 data-ru="Аудио-Спринт: 11 Минут на Создание Звукового Пака" data-en="Audio Sprint: 11 Minutes to Forge Game Sound">Audio Ustaxona: 11 Daqiqalik Ovoz Generatsiyasi</h2>
  <div class="timer" id="timer">
    <div class="digits" id="digits">11:00</div>
    <div class="ctrls">
      <button id="tstart">Start / Stop</button>
      <button class="ghost" id="treset">Reset</button>
    </div>
  </div>
  <p style="margin-top:15px; font-size:0.95em;" data-ru="Откройте генератор звуков. Сгенерируйте эффекты, прослушайте в наушниках и запишите промпты в тетрадь!" data-en="Open the audio engine. Generate your assets, audition in headphones, and log prompts on your sheet!">Ovoz generatorini oching. Tovushlarni sinab ko'ring, quloqchinlarda tinglang va promptlarni varaqaga yozing!</p>
</section>

<section class="slide" data-phase="Tahlil|Прослушивание|Audio Audition" data-time="31–36">
  <div class="eyebrow"><span data-ru="Аудио-контроль" data-en="Audio Audition">Tahlil va Tinglash</span></div>
  <h2 data-ru="Краш-Тест Звука: Слепое Прослушивание в Парах" data-en="Audio Crash Test: Blind Audition in Pairs">Ko'r-ko'rona Tinglash Testi (Blind Test)</h2>
  <p data-ru="Дайте соседу послушать ваш SFX, не показывая экран. Пусть он угадает действие:" data-en="Play your SFX to your partner without showing your screen. Can they identify the action?">Sherigingizga ekranni ko'rsatmasdan tovushni qo'yib bering. U qanday harakat sodir bo'lganini topa oladimi?</p>
  <div class="cols c3" style="display:grid; grid-template-columns:1fr 1fr 1fr; gap:12px; margin-top:15px;">
    <div class="box">
      <h3 style="color:var(--accent);" data-ru="1. Узнаваемость" data-en="1. Clarity">1. Aniqlik</h3>
      <p data-ru="Сразу ли понятно, что подобрана монетка, а не упал кирпич?" data-en="Is it immediately obvious that a coin was collected rather than a brick dropped?">Tanga olingani darhol tushunarlimi yoki g'isht qulagandek eshitiladimi?</p>
    </div>
    <div class="box">
      <h3 style="color:var(--accent);" data-ru="2. Длительность" data-en="2. Duration">2. Davomiylik</h3>
      <p data-ru="Звук не тянется слишком долго? (Для прыжка идеально 0.3–0.5 с)" data-en="Does the sound cut off cleanly without lagging into the next action?">Tovush cho'zilib ketmadimi? (Sakrash uchun 0.3–0.5 soniya ideal).</p>
    </div>
    <div class="box" style="border-left:4px solid var(--green);">
      <h3 style="color:var(--green);" data-ru="3. Баланс громкости" data-en="3. Master Volume">3. Balandlik Me'yori</h3>
      <p data-ru="Не бьет ли по барабанным перепонкам резким скрежетом?" data-en="Does the acoustic frequency sit smoothly without harsh clipping spikes?">Quloqqa yoqimli eshitiladimi, o'tkir shovqinlar yo'qmi?</p>
    </div>
  </div>
</section>

<section class="slide" data-phase="Uy vazifasi|Домашнее задание|Homework" data-time="36–40">
  <div class="eyebrow"><span data-ru="Домашний проект" data-en="Take-Home Project">Uyga Vazifa</span></div>
  <h2 data-ru="Домашнее Задание: Аудио-Пак из 3 SFX + 1 Музыка + 10 Баллов" data-en="Homework: 3 SFX + 1 Biome Track + 10-Point Rubric">Uyga Vazifa: 3 Ta SFX va 1 Ta Fon Musiqasi To'plami</h2>
  <div class="hw" style="display:grid; grid-template-columns:1.4fr 1fr; gap:20px; margin-top:15px;">
    <div class="box" style="border-left:5px solid var(--accent);">
      <h3 style="color:var(--accent);" data-ru="Что нужно сделать:" data-en="Assignment Details:">Bajarilishi shart bo'lgan vazifalar:</h3>
      <ol style="margin-top:8px; padding-left:18px; line-height:1.6;">
        <li data-ru="Сгенерировать 3 чистых звуковых эффекта (прыжок, монета, урон) и скачать в формате .mp3 или .wav." data-en="Generate 3 clean SFX assets (jump, loot, damage) and download as .mp3 or .wav.">3 ta toza SFX tovushini (sakrash, tanga, ziyon) AI da yarating va .mp3/.wav formatda saqlang.</li>
        <li data-ru="Сгенерировать 1 атмосферный трек саундтрека биома (15–30 секунд) через Suno AI." data-en="Generate 1 atmospheric 15-30s biome soundtrack loop using Suno AI.">Suno AI orqali biomingizga mos 1 ta fon musiqasini (15–30 soniya) yarating.</li>
        <li data-ru="Заполнить звуковую матрицу в рабочей тетради (действие -> название файла -> тайминг)." data-en="Complete the audio trigger matrix in your workbook (Action -> Filename -> Duration).">Varaqadagi tovushlar jadvalini (Harakat -> Fayl nomi -> Davomiyligi) to'liq to'ldiring.</li>
      </ol>
    </div>
    <div class="box" style="background:var(--panel);">
      <h3 style="color:var(--green);" data-ru="Критерии Оценки (10 баллов):" data-en="Grading Rubric (10 Points):">Baholash Mezoni (10 ball):</h3>
      <ul style="margin-top:8px; padding-left:16px; line-height:1.6; font-size:0.9em;">
        <li data-ru="<b>3 балла:</b> Сгенерированы 3 коротких игровых SFX без шумов." data-en="<b>3 pts:</b> 3 short isolated gameplay SFX generated."><b>3 ball:</b> Shovqinsiz, toza 3 ta o'yin SFX tovushi yaratilgan.</li>
        <li data-ru="<b>4 балла:</b> Создан саундтрек биома, подходящий по настроению." data-en="<b>4 pts:</b> Cohesive biome background soundtrack created."><b>4 ball:</b> Biom kayfiyatiga mos fon musiqasi tayyorlangan.</li>
        <li data-ru="<b>3 балла:</b> Звуковая матрица заполнена в рабочей тетради." data-en="<b>3 pts:</b> Audio trigger matrix fully logged in workbook."><b>3 ball:</b> Varaqadagi tovushlar jadvali to'liq to'ldirilgan.</li>
      </ul>
    </div>
  </div>
</section>
"""

l9_notes = {
  'uz': [
    "Kirish: Ovozning o'yindagi qudratini ko'rsatish uchun avval biror o'yin videosini ovozsiz, so'ng ovozli qo'yib bering.",
    "Ovoz psixologiyasi: 'Ko'zlar quloqlarga ishonadi' qoidasini tushuntiring. SFX harakatga salmoq va quvvat beradi.",
    "3 qatlam: SFX (qisqa harakatlar), BGM (fon musiqasi) va Atrof-muhit (Ambient shamol/suv) farqlarini ajrating.",
    "AI bilan audio yaratish: ElevenLabs va Suno AI vositalari qanday ishlashini, matndan chastota generatsiyasini tushuntiring.",
    "SFX formulasi: Harakat + Tembr/Material + Dinamika + Uslub formulasi doskada tahlil qilinsin.",
    "Ovoz xatolari: Quloqni og'rituvchi baland shovqin, kechikish va bir xil zerikarli takrorlanishdan saqlanish.",
    "Amaliy vazifa: 4 ta tovushdan iborat audio to'plam tayyorlash (sakrash, tanga, ziyon, musiqa).",
    "Jonli sprint: 11 daqiqalik taymer. O'quvchilar quloqchinlarda tovushlarni generatsiya qilishadi.",
    "Tinglash testi: Sherigiga ekranni ko'rsatmasdan ovozni qo'yib berish va qaysi harakat ekanini topish mashqi.",
    "Uy vazifasi: Audio fayllarni saqlash va jadvalni to'ldirish. 10 ballik mezonni eslating."
  ],
  'ru': [
    "Вступление: Покажите фрагмент игры сначала без звука, затем со звуком, чтобы доказать силу погружения.",
    "Психология звука: Глаза верят ушам. Без сочного звука удара графика кажется картонной.",
    "3 слоя звука: Разберите SFX (эффекты), BGM (фоновая музыка) и Эмбиент (окружение).",
    "ИИ в аудио: Как ElevenLabs SFX и Suno создают сэмплы из текстовых описаний.",
    "Формула промпта: Действие + Тембр + Динамика + Игровой стиль.",
    "Звуковые ошибки: Перегрузка по громкости, задержка звука и слуховая усталость.",
    "Постановка задачи: Собрать аудио-пак из 4 элементов для своего проекта.",
    "Практический спринт: Таймер на 11 минут. Генерация звуков в наушниках.",
    "Слепое прослушивание: Сосед угадывает действие по звуку с закрытыми глазами.",
    "Домашнее задание: Сохранить сэмплы и заполнить звуковую матрицу (10 баллов)."
  ],
  'en': [
    "Opening: Demonstrate gameplay with sound muted versus full audio to illustrate acoustic immersion.",
    "Audio Psychology: Eyes believe ears. Kinetic impact requires crisp audio feedback.",
    "3 Audio Layers: Demystify SFX (micro-actions), BGM (musical loops), and Ambient environmental drone.",
    "Generative Audio: How ElevenLabs SFX and Suno synthesize waveforms from descriptive text prompts.",
    "SFX Formula: Action + Timbre/Material + Attack Dynamics + Game Style.",
    "Audio Pitfalls: Volume clipping, latency lag, and repetitive ear fatigue.",
    "Mission Brief: Construct an audio kit of 4 assets (Jump, Loot, Hazard, Biome theme).",
    "Live Lab Sprint: 11-minute timer. Students audition and tweak AI sound prompts with headphones.",
    "Blind Audition: Peer test guessing the in-game action solely through audio cues.",
    "Homework: Save audio files and log the trigger matrix. Review the 10-point rubric."
  ]
}

p9_html = build_presentation("09-dars: O'yin Ovozlar Sehri: AI SFX va Musiqa", l9_slides, l9_notes)
with open(os.path.join(l9_dir, "prezentatsiya.html"), "w", encoding="utf-8") as f:
    f.write(p9_html)

l9_t1 = {"uz": "O'yin Ovozlar Sehri: AI SFX va Musiqa", "ru": "Магия Игрового Звука: AI SFX и Музыка", "en": "Game Audio Magic: AI SFX & Music"}
l9_s1 = {"uz": "O'yinga hayot bag'ishlovchi ovoz effektlari (SFX), fon musiqasi (BGM) va atmosferani AI da yarating.", "ru": "Создавайте звуковые эффекты (SFX), музыку (BGM) и атмосферу с помощью ИИ.", "en": "Synthesize immersive sound effects (SFX), background music, and ambience using AI."}
l9_k1 = {"uz": "Ovoz — o'yindagi hissiyotlarning 50 foizidir. Shirali SFX har bir klikni maroqli qiladi.", "ru": "Звук — это 50% погружения в игру. Сочный SFX делает каждое действие незабываемым.", "en": "Audio is 50% of immersion. Punchy SFX makes every player interaction rewarding."}

l9_p1 = """
  <section class="sec">
    <div class="h"><span class="no">01</span><h2><span lang="uz">Ovozning O'yindagi O'rni</span><span lang="ru">Роль Звука в Игре</span><span lang="en">Audio Impact in Gaming</span></h2></div>
    <div class="compare">
      <div class="bad">
        <span class="lbl"><span lang="uz">Ovozsiz O'yin (Mute)</span><span lang="ru">Без Звука</span><span lang="en">Muted Gameplay</span></span>
        <p class="pr"><span lang="uz">Tugmalar bosilishi sezilmaydi, zarbalar kuchsiz tuyuladi. Qahramon yiqilganda ham hech narsa eshitilmaydi.</span><span lang="ru">Нет отдачи от кнопок, удары кажутся слабыми. Игра кажется мертвой и скучной.</span><span lang="en">Zero tactile feedback. Attacks feel weightless and mechanics feel broken.</span></p>
      </div>
      <div class="good">
        <span class="lbl"><span lang="uz">Jonli SFX va Dinamika</span><span lang="ru">Сочный Саунд-Дизайн</span><span lang="en">Dynamic Audio Design</span></span>
        <p class="pr"><span lang="uz">Har bir sakrash, tanga va zarba jaranglaydi! O'yinchi harakatidan quvonadi va o'yinga sho'ng'iydi.</span><span lang="ru">Звон монет, басовый гул лазеров и четкие шаги дают мгновенный заряд дофамина!</span><span lang="en">Resonant crystal pickups and punchy laser hums deliver instantaneous dopamine hits.</span></p>
      </div>
    </div>
  </section>

  <section class="sec">
    <div class="h"><span class="no">02</span><h2><span lang="uz">O'yin Tovushining 3 Qatlami</span><span lang="ru">3 Слоя Аудио</span><span lang="en">3 Audio Layers</span></h2></div>
    <div class="trio">
      <div>
        <b><span lang="uz">1. SFX (Effektlar) 💥</span><span lang="ru">1. SFX (Эффекты) 💥</span><span lang="en">1. SFX Effects 💥</span></b>
        <span class="d"><span lang="uz">Sakrash, o'q otish, sandiq ochish (0.2–2 soniya).</span><span lang="ru">Прыжки, выстрелы, сбор лута (0.2–2 сек).</span><span lang="en">Jumps, laser bursts, chest unlocks (0.2–2s).</span></span>
      </div>
      <div>
        <b><span lang="uz">2. BGM (Musiqa) 🎵</span><span lang="ru">2. BGM (Музыка) 🎵</span><span lang="en">2. BGM Soundtrack 🎵</span></b>
        <span class="d"><span lang="uz">Uzluksiz fon musiqasi (Loop): xotirjam yoki shiddatli.</span><span lang="ru">Фоновый музыкальный луп биома или битвы.</span><span lang="en">Atmospheric exploration or battle synth loop.</span></span>
      </div>
      <div>
        <b><span lang="uz">3. Ambient (Muhit) 🍃</span><span lang="ru">3. Эмбиент 🍃</span><span lang="en">3. Ambience 🍃</span></b>
        <span class="d"><span lang="uz">Shamol, suv tomchilari, kosmik dvigatel ovozi.</span><span lang="ru">Ветер, капли в пещере, гул реактора.</span><span lang="en">Wind gusts, cavern drips, reactor drone.</span></span>
      </div>
    </div>
  </section>

  <section class="sec">
    <div class="h"><span class="no">03</span><h2><span lang="uz">SFX Prompt Formulasi (4 Qism)</span><span lang="ru">Формула SFX-Промпта</span><span lang="en">SFX Prompt Formula</span></h2></div>
    <div class="formula">
      <div class="p"><b>1. Harakat</b><span class="d">Tanga olish</span></div>
      <div class="plus">+</div>
      <div class="p"><b>2. Tembr</b><span class="d">Billur jarang</span></div>
      <div class="plus">+</div>
      <div class="p"><b>3. Dinamika</b><span class="d">Fast attack 0.8s</span></div>
      <div class="plus">+</div>
      <div class="p"><b>4. Uslub</b><span class="d">Sci-fi game UI</span></div>
    </div>
  </section>

  <section class="sec">
    <div class="h"><span class="no">04</span><h2><span lang="uz">Ovoz Nazorati Qoidalari</span><span lang="ru">Правила Аудио</span><span lang="en">Audio Quality Rules</span></h2></div>
    <div class="checklist">
      <div><b>Balandlik Balansi:</b> <span lang="uz">SFX hech qachon musiqani bosib, quloqni og'ritmasligi kerak (master hajmi -3dB).</span><span lang="ru">SFX не должен оглушать игрока (баланс громкости).</span><span lang="en">SFX must never clip or overpower background music.</span></div>
      <div><b>Nol Kechikish:</b> <span lang="uz">Tovush harakat bilan bir vaqtda chiqishi shart (audio fayl boshidagi bo'shliq kesiladi).</span><span lang="ru">Звук синхронен действию без пауз в начале.</span><span lang="en">Trim leading silence so audio triggers with zero input delay.</span></div>
    </div>
  </section>
"""

l9_t2 = {"uz": "O'yin Audio Trigger Matritsasi", "ru": "Матрица Аудио-Триггеров", "en": "Game Audio Trigger Matrix"}
l9_s2 = {"uz": "O'yiningizdagi harakatlar va ularga ulangan tovush fayllarini ro'yxatga oling.", "ru": "Зафиксируйте действия игры и привязанные к ним аудиофайлы.", "en": "Log gameplay action triggers and their corresponding sound assets."}

l9_p2 = """
  <section class="sec">
    <div class="h"><span class="no">05</span><h2><span lang="uz">Audio Fayllar Matritsasi</span><span lang="ru">Таблица Звуков</span><span lang="en">Sound Trigger Matrix</span></h2></div>
    <table class="gridtable" style="width:100%; border-collapse:collapse; font-size:8.5pt; text-align:left;">
      <tr style="background:var(--panel-2);">
        <th style="padding:5px; border:1px solid var(--rule);">O'yin Harakati</th>
        <th style="padding:5px; border:1px solid var(--rule);">Fayl Nomi</th>
        <th style="padding:5px; border:1px solid var(--rule);">Vaqti</th>
        <th style="padding:5px; border:1px solid var(--rule);">AI Generator Prompti</th>
      </tr>
      <tr>
        <td style="padding:5px; border:1px solid var(--rule);">1. Sakrash (Jump)</td>
        <td style="padding:5px; border:1px solid var(--rule);">jump_whoosh.wav</td>
        <td style="padding:5px; border:1px solid var(--rule);">0.4 s</td>
        <td style="padding:5px; border:1px solid var(--rule);">Fast kinetic wind jump whoosh, game SFX</td>
      </tr>
      <tr>
        <td style="padding:5px; border:1px solid var(--rule);">2. Tanga Olish (Loot)</td>
        <td style="padding:5px; border:1px solid var(--rule);">coin_pickup.wav</td>
        <td style="padding:5px; border:1px solid var(--rule);">0.8 s</td>
        <td style="padding:5px; border:1px solid var(--rule);">__________________________________________</td>
      </tr>
      <tr>
        <td style="padding:5px; border:1px solid var(--rule);">3. Ziyon / Tuzoq (Hit)</td>
        <td style="padding:5px; border:1px solid var(--rule);">hazard_shock.wav</td>
        <td style="padding:5px; border:1px solid var(--rule);">1.0 s</td>
        <td style="padding:5px; border:1px solid var(--rule);">__________________________________________</td>
      </tr>
      <tr>
        <td style="padding:5px; border:1px solid var(--rule);">4. Fon Musiqasi (BGM)</td>
        <td style="padding:5px; border:1px solid var(--rule);">biome_theme.mp3</td>
        <td style="padding:5px; border:1px solid var(--rule);">20.0 s</td>
        <td style="padding:5px; border:1px solid var(--rule);">Cyberpunk ambient synthwave loop, sci-fi</td>
      </tr>
    </table>
  </section>

  <section class="sec">
    <div class="h"><span class="no">06</span><h2><span lang="uz">Fon Musiqasi Parametrlari (Suno AI)</span><span lang="ru">Параметры Музыки</span><span lang="en">Music Settings</span></h2></div>
    <div style="border:1px solid var(--rule); background:var(--panel); padding:8px; font-size:8.5pt;">
      <b>Janr / Uslub:</b> [ ] Synthwave [ ] 8-Bit Chiptune [ ] Epic Orchestral [ ] Cyber Rock<br>
      <b>Kayfiyat (Mood):</b> [ ] Sirli va Xotirjam [ ] Qizg'in Jang [ ] G'alaba va Tantanavor<br>
      <b>Tezlik (BPM):</b> [ ] Sekin (80 BPM) [ ] O'rtacha (120 BPM) [ ] Tez (145 BPM)
    </div>
  </section>

  <section class="sec">
    <div class="h"><span class="no">07</span><h2><span lang="uz">Blind Test: Sherik Baholashi</span><span lang="ru">Слепой Тест</span><span lang="en">Blind Audition Test</span></h2></div>
    <div style="display:flex; flex-direction:column; gap:4px; font-size:8.5pt;">
      <label><input type="checkbox"> Sherigim ekranni ko'rmasdan barcha 3 ta SFX tovushini to'g'ri topdi.</label>
      <label><input type="checkbox"> Fon musiqasi o'yin biomi va atmosferasiga 100% mos keladi.</label>
      <label><input type="checkbox"> Tovush boshlanishida noqulay kechikish (silence) yo'q.</label>
    </div>
  </section>
"""

l9_hw = """
  <p><b>1. SFX Fayllari:</b> AI vositasida 3 ta qisqa SFX tovushini (sakrash, tanga, ziyon) yarating va saqlang.</p>
  <p><b>2. Fon Musiqasi:</b> Suno AI orqali biomingizga mos 1 ta 15–30 soniyalik fon kuyini generatsiya qiling.</p>
  <p><b>3. Matritsani To'ldirish:</b> Varaqadagi barcha qatorlarga promptlar va fayl nomlarini yozing.</p>
"""

l9_crit = """
  <div class="r"><span>3 ta toza SFX yaratilgan va saqlangan</span><b>3</b></div>
  <div class="r"><span>Biomga mos sifatli fon musiqasi tayyorlangan</span><b>4</b></div>
  <div class="r"><span>Audio matritsa to'liq to'ldirilgan</span><b>3</b></div>
"""

l9_nxt = {'uz': "Aqlli NPC va Kvest Qahramonlari", 'ru': "Умные NPC и Квестовые Персонажи", 'en': "Smart NPCs & Quest Characters"}

ws9_html = build_worksheet('5-6-sinf', 2, 9, l9_t1, l9_s1, l9_k1, l9_p1, l9_t2, l9_s2, l9_p2, l9_hw, l9_crit, l9_nxt)
with open(os.path.join(l9_dir, 'varaqa.html'), 'w', encoding='utf-8') as f:
    f.write(ws9_html)

print("5-6 Week 2 Lesson 9 generated successfully!")
