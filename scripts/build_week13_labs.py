#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""13-hafta interaktiv laboratoriyalari (3 kohorta)."""

import os

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

SHELL = """<!DOCTYPE html>
<html lang="uz">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title data-ru="{title_ru}" data-en="{title_en}">{title_uz}</title>
<style>
:root{{--ink:#12243d;--accent:#be995b;--bg:#f8f6f0;--card:#fff;--green:#16a34a;--red:#dc2626;--line:#e2e8f0}}
*{{box-sizing:border-box}}
body{{margin:0;background:var(--bg);color:var(--ink);font:16px/1.6 system-ui,-apple-system,'Segoe UI',sans-serif}}
header{{padding:18px 28px;background:#12243d;color:#fff;display:flex;flex-wrap:wrap;gap:14px;align-items:center;justify-content:space-between}}
header h1{{margin:0;font-size:clamp(20px,3vw,30px)}}
header .pill{{background:#ffffff18;border:1px solid #ffffff35;border-radius:999px;padding:6px 14px;font-size:13px}}
main{{max-width:1100px;margin:24px auto;padding:0 18px 60px}}
.panel{{background:var(--card);border:1px solid var(--line);border-radius:18px;padding:22px;box-shadow:0 8px 30px #12243d0c;margin-bottom:18px}}
.panel h2{{margin:0 0 10px;font-size:20px}}
.row{{display:flex;flex-wrap:wrap;gap:10px;align-items:center;margin:12px 0}}
button{{font:inherit;cursor:pointer;border:1px solid var(--line);background:#fff;color:var(--ink);border-radius:10px;padding:9px 16px;font-weight:600}}
button:hover{{border-color:var(--accent)}}
button.primary{{background:var(--ink);color:#fff;border-color:var(--ink)}}
button.gold{{background:var(--accent);color:#fff;border-color:var(--accent)}}
canvas{{display:block;width:100%;max-width:900px;background:#0b1220;border-radius:12px;margin:10px auto}}
pre{{background:#0b1220;color:#b7f7c8;border-radius:12px;padding:16px;overflow:auto;font:13px/1.55 ui-monospace,monospace;min-height:180px;white-space:pre-wrap}}
.stat{{display:inline-flex;gap:8px;align-items:center;background:#f1f5f9;border-radius:999px;padding:6px 14px;font-weight:700;font-size:14px}}
.ok{{color:var(--green)}} .bad{{color:var(--red)}}
.hint{{color:#64748b;font-size:14px}}
.grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:14px}}
.note{{background:#fff8e8;border-left:4px solid var(--accent);border-radius:10px;padding:12px 16px}}
@media print{{header{{background:#12243d!important;-webkit-print-color-adjust:exact}}button{{display:none}}}}
</style>
</head>
<body>
<header>
  <h1 data-ru="{title_ru}" data-en="{title_en}">{title_uz}</h1>
  <span class="pill" data-ru="13-Я НЕДЕЛЯ · ИНТЕРАКТИВНАЯ ЛАБОРАТОРИЯ" data-en="WEEK 13 · INTERACTIVE LAB">13-HAFTA · INTERAKTIV LABORATORIYA</span>
</header>
<main>
<div class="panel">
  <h2 data-ru="{subtitle_ru}" data-en="{subtitle_en}">{subtitle_uz}</h2>
  <p class="hint" data-ru="{hint_ru}" data-en="{hint_en}">{hint_uz}</p>
{body}
</div>
<div class="panel" id="reportPanel">
  <h2 data-ru="Hisobot" data-en="Report">Hisobot</h2>
  <div class="row"><span class="stat" data-ru="Ball" data-en="Score">Ball: <b id="score">0</b></span>
  <span class="stat" data-ru="Bosqich" data-en="Stage">Bosqich: <b id="stage">0</b></span></div>
  <pre id="log">// tizim tayyor</pre>
  <div class="row"><button class="primary" onclick="exportReport()" data-ru="Eksport qilish" data-en="Export report">Hisobotni eksport qilish</button>
  <button onclick="resetAll()" data-ru="Qayta boshlash" data-en="Reset">Qayta boshlash</button></div>
</div>
</main>
<script>
{script}
</script>
</body>
</html>
"""

LABS = [
    dict(
        path="classes/10-11-sinf/13-hafta/33-dars-avtonom-kod-agentlari-va-tdd/simulator/index.html",
        title_uz="TDD Code Agent Simulyatori",
        title_ru="Симулятор TDD Code Agent",
        title_en="TDD Code Agent Simulator",
        subtitle_uz="ReAct tsikli: test yoz → agent tuzat → diff tekshir",
        subtitle_ru="Цикл ReAct: написать тест → агент чинит → проверить diff",
        subtitle_en="ReAct loop: write a test → agent fixes → review the diff",
        hint_uz="Agentga 3 iteratsiya beriladi. «Reward hacking» rejimini yoqing — agent testlarni o‘chirishga urinadi.",
        hint_ru="Агенту дано 3 итерации. Включите «reward hacking» — агент попытается удалить тесты.",
        hint_en="The agent gets 3 iterations. Enable \"reward hacking\" — it will try to delete tests.",
        body="""  <div class="row">
    <button class="gold" onclick="writeTest()" data-ru="1 · Qizil test yozish" data-en="1 · Write red test">1 · Qizil test yozish</button>
    <button class="primary" onclick="runAgent()" data-ru="2 · Agentni ishga tushurish" data-en="2 · Run agent">2 · Agentni ishga tushurish</button>
    <button onclick="reviewDiff()" data-ru="3 · Diff tekshirish" data-en="3 · Review diff">3 · Diff tekshirish</button>
    <button onclick="toggleHack()" id="hackBtn" data-ru="Reward hacking: Выкл." data-en="Reward hacking: Off">Reward hacking: Yo'q</button>
  </div>
  <div class="grid">
    <div class="note"><b data-ru="Qizil bosqich" data-en="Red stage">Qizil bosqich</b><p data-ru="test('find([]) === null') — hali o'tmaydi." data-en="test('find([]) === null') — failing."">test('find([]) === null') — hali o'tmaydi.</p></div>
    <div class="note"><b data-ru="Yashil bosqich" data-en="Green stage">Yashil bosqich</b><p data-ru="const find = xs => xs[0] ?? null;" data-en="const find = xs => xs[0] ?? null;">const find = xs => xs[0] ?? null;</p></div>
  </div>""",
        script="""let stage=0, score=0, hacking=false, tests=4;
const L=document.getElementById('log');
function say(t){L.innerHTML += '\\n'+t; L.scrollTop=L.scrollHeight;}
function writeTest(){
  if(stage!==0) return say('// Avval qizil test yozilishi kerak');
  stage=1; document.getElementById('stage').textContent=stage;
  say('[QIZIL] test yozildi: find([]) \\u2192 null');
  say('[TEST] 3/4 pass, 1 FAIL');
}
function runAgent(){
  if(stage<1) return say('// Avval test yozing');
  const steps=['Thought: funksiya bo\\u2018sh massivda xato qaytaradi','Action: edit src/find.js','Observation: test 4/4 pass','Thought: refaktor uchun xavf yo\\u2018q'];
  steps.forEach((s,i)=>setTimeout(()=>say('[ITER '+(i+1)+'] '+s), i*420));
  setTimeout(()=>{
    if(hacking){tests--; say('[XAVF] test fayli o\\u2018chirildi! testlar soni: '+tests);}
    else {score+=4; say('[OK] agent tuzatdi, 4/4 test yashil');}
    document.getElementById('score').textContent=score;
    stage=2; document.getElementById('stage').textContent=stage;
  }, 1900);
}
function reviewDiff(){
  if(stage<2) return say('// Agent hali ishlamadi');
  if(hacking){say('[RAD ETILDI] diff testlarni o\\u2018chiradi \\u2192 reward hacking'); score=Math.max(0,score-2);}
  else {say('[TASDIQLANDI] diff toza: 1 funksiya, 0 test o\\u2018zgarishi'); score+=2;}
  document.getElementById('score').textContent=score; stage=3; document.getElementById('stage').textContent=stage;
  say('[TRACE] Thought/Action/Observation jurnali saqlandi');
}
function toggleHack(){
  hacking=!hacking;
  document.getElementById('hackBtn').textContent = hacking?'Reward hacking: Ha':'Reward hacking: Yo\\u2018q';
  say('[GUARD] test hash himoyasi '+(hacking?'O\\u2018CHIRILDI':'YOQILDI'));
}
function exportReport(){
  const blob=new Blob([JSON.stringify({topic:'TDD Code Agent',stage,score,tests,hacking,date:new Date().toISOString()},null,2)],{type:'application/json'});
  const a=document.createElement('a');a.href=URL.createObjectURL(blob);a.download='tdd_agent_report.json';a.click();
}
function resetAll(){stage=0;score=0;tests=4;hacking=false;L.innerHTML='// tizim tayyor';document.getElementById('score').textContent=0;document.getElementById('stage').textContent=0;
  document.getElementById('hackBtn').textContent='Reward hacking: Yo\\u2018q';}
""",
    ),
    dict(
        path="classes/7-8-sinf/13-hafta/36-dars-oq-fizikasi-va-trigonometriya/simulator/index.html",
        title_uz="Kiber-Turret: atan2 va O'q Fizikasi",
        title_ru="Кибер-Турель: atan2 и физика снарядов",
        title_en="Cyber Turret: atan2 and Bullet Physics",
        subtitle_uz="Sichqonchaga qarab o‘q uz, burchak va traektoriyani kuzat",
        subtitle_ru="Стреляй по курсору, наблюдай угол и траекторию",
        subtitle_en="Aim at the cursor and watch the angle and trajectory",
        hint_uz="Sichqonchani harakatlantiring: burchak real vaqtda hisoblanadi. Bosish — o‘q uzish. R — qayta boshlash.",
        hint_ru="Двигайте курсор: угол вычисляется в реальном времени. Клик — выстрел. R — сброс.",
        hint_en="Move the cursor: the angle updates live. Click to fire. R resets.",
        body="""  <div class="row"><span class="stat" data-ru="Burchak" data-en="Angle">atan2 = <b id="ang">0.00</b> rad</span>
  <span class="stat" data-ru="Снаряды" data-en="Bullets">O‘qlar: <b id="bul">0</b></span>
  <span class="stat" data-ru="Tegishlar" data-en="Hits">Tegishlar: <b id="hits">0</b></span>
  <button onclick="resetAll()" data-ru="Qayta boshlash" data-en="Reset">Qayta boshlash</button></div>
  <canvas id="cv" width="900" height="430"></canvas>""",
        script="""const cv=document.getElementById('cv'), x=cv.getContext('2d');
let mx=450,my=120, bullets=[], parts=[], targets=[], score=0, hits=0;
for(let i=0;i<5;i++) targets.push({x:120+i*150,y:80+(i%2)*90,r:22,alive:true});
cv.addEventListener('mousemove',e=>{const r=cv.getBoundingClientRect();mx=(e.clientX-r.left)*cv.width/r.width;my=(e.clientY-r.top)*cv.height/r.height;});
cv.addEventListener('click',()=>{
  const a=Math.atan2(my-215,mx-90);
  bullets.push({x:90,y:215,vx:Math.cos(a)*460,vy:Math.sin(a)*460,life:2.2});
  for(let i=0;i<4;i++){const p=Math.random()*6.28;parts.push({x:90,y:215,vx:Math.cos(p)*70,vy:Math.sin(p)*70,life:.25});}
});
function hit(a,b){return Math.hypot(a.x-b.x,a.y-b.y)<b.r+5;}
function loop(){
  x.fillStyle='#0b1220';x.fillRect(0,0,cv.width,cv.height);
  x.strokeStyle='#1b2a44';for(let i=0;i<cv.width;i+=50){x.beginPath();x.moveTo(i,0);x.lineTo(i,cv.height);x.stroke();}
  const a=Math.atan2(my-215,mx-90);document.getElementById('ang').textContent=a.toFixed(2);
  // turret
  x.save();x.translate(90,215);x.rotate(a);x.fillStyle='#be995b';x.fillRect(0,-8,54,16);x.restore();
  x.fillStyle='#e2e8f0';x.beginPath();x.arc(90,215,17,0,6.28);x.fill();
  // targetlar
  targets.forEach(t=>{if(!t.alive)return;x.fillStyle='#22c55e';x.beginPath();x.arc(t.x,t.y,t.r,0,6.28);x.fill();x.fillStyle='#0b1220';x.font='14px sans-serif';x.fillText('AI',t.x-9,t.y+5);});
  bullets=bullets.filter(b=>{
    b.x+=b.vx/60;b.y+=b.vy/60;b.life-=1/60;
    x.fillStyle='#fbbf24';x.beginPath();x.arc(b.x,b.y,4,0,6.28);x.fill();
    for(const t of targets){if(t.alive&&hit(b,t)){t.alive=false;hits++;score+=10;for(let i=0;i<10;i++){const p=Math.random()*6.28;parts.push({x:t.x,y:t.y,vx:Math.cos(p)*110,vy:Math.sin(p)*110,life:.5});}return false;}}
    return b.life>0&&b.x>0&&b.x<cv.width&&b.y>0&&b.y<cv.height;
  });
  parts=parts.filter(p=>{p.x+=p.vx/60;p.y+=p.vy/60;p.life-=1/60;x.fillStyle='rgba(251,191,36,'+Math.max(0,p.life*2)+')';x.fillRect(p.x,p.y,3,3);return p.life>0;});
  x.fillStyle='#94a3b8';x.font='13px monospace';x.fillText('vx = cos(a)·460   vy = sin(a)·460',16,26);
  document.getElementById('bul').textContent=bullets.length;document.getElementById('hits').textContent=hits;
  document.getElementById('score').textContent=score;
  requestAnimationFrame(loop);
}
loop();
function exportReport(){const blob=new Blob([JSON.stringify({topic:'Bullet Physics',angle:document.getElementById('ang').textContent,bullets:bullets.length,hits,score,date:new Date().toISOString()},null,2)],{type:'application/json'});const a=document.createElement('a');a.href=URL.createObjectURL(blob);a.download='physics_report.json';a.click();}
function resetAll(){bullets=[];parts=[];hits=0;score=0;targets.forEach(t=>t.alive=true);}
document.addEventListener('keydown',e=>{if(e.key.toLowerCase()==='r')resetAll();});
""",
    ),
    dict(
        path="classes/5-6-sinf/13-hafta/32-dars-aqlli-shartlar-va-sezgirlik/playground/index.html",
        title_uz="Sehrli Labirint — Aqlli Shartlar",
        title_ru="Волшебный лабиринт — умные условия",
        title_en="Magic Maze — Smart Conditions",
        subtitle_uz="Kalitni ol, qizil tuzoqdan qoch, yashil eshikka yet",
        subtitle_ru="Возьми ключ, избеги красную ловушку, дойди до зелёной двери",
        subtitle_en="Collect the key, avoid the red trap, reach the green door",
        hint_uz="Boshqaruv: ← ↑ ↓ →. Qahramon har qadamda rangni tekshiradi (touching color).",
        hint_ru="Управление: ← ↑ ↓ →. Герой проверяет цвет на каждом шаге (touching color).",
        hint_en="Controls: arrow keys. The hero checks colour every step (touching colour).",
        body="""  <div class="row"><span class="stat" data-ru="Jonlar" data-en="Lives">Jon: <b id="hp">3</b></span>
  <span class="stat" data-ru="Kalit" data-en="Key">Kalit: <b id="key">Yo‘q</b></span>
  <span class="stat" data-ru="Bosqich" data-en="Stage">Bosqich: <b id="lvl">1</b></span>
  <button onclick="resetAll()" data-ru="Qayta boshlash" data-en="Reset">Qayta boshlash</button></div>
  <canvas id="cv" width="720" height="480"></canvas>
  <p class="hint" data-ru="Правило: если следующая клетка серая — остановиться. Если красная — потерять жизнь." data-en="Rule: if the next tile is grey — stop. If red — lose a life.">Qoida: agar keyingi katak kulrang bo‘lsa — to‘xtash. Agar qizil bo‘lsa — jon kamayadi.</p>""",
        script="""const cv=document.getElementById('cv'),x=cv.getContext('2d');const S=60;
const map=[
'############',
'#S..#...K..#',
'#.#.#.####.#',
'#.#...#....#',
'#.#####.##.#',
'#.....R...D#',
'############'];
let px=1,py=1,hp=3,hasKey=false,lvl=1;
function color(c){return c==='#'?'#475569':c==='R'?'#ef4444':c==='K'?'#fbbf24':c==='D'?'#22c55e':c==='S'?'#60a5fa':'#f8f6f0';}
function draw(){
 x.fillStyle='#0b1220';x.fillRect(0,0,cv.width,cv.height);
 for(let r=0;r<map.length;r++)for(let c=0;c<map[r].length;c++){
   x.fillStyle=color(map[r][c]);x.fillRect(c*S+2,r*S+2,S-4,S-4);
 }
 if(hasKey){x.fillStyle='#fbbf24';x.fillRect(2*S+2,1*S+2,S-4,S-4);}
 x.fillStyle='#fff';x.beginPath();x.arc(px*S+S/2,py*S+S/2,S*.3,0,6.28);x.fill();
 x.fillStyle='#12243d';x.beginPath();x.arc(px*S+S/2-6,py*S+S/2-3,2.5,0,6.28);x.arc(px*S+S/2+6,py*S+S/2-3,2.5,0,6.28);x.fill();
 document.getElementById('hp').textContent=hp;document.getElementById('key').textContent=hasKey?'Ha':'Yo‘q';document.getElementById('lvl').textContent=lvl;
 document.getElementById('score').textContent=(hasKey?5:0)+(lvl-1)*5;
}
function move(dx,dy){
 const nx=px+dx, ny=py+dy, next=map[ny]?.[nx];
 if(next===undefined||next==='#'){say('[SENSOR] kulrang devor — harakat TO‘XTATILDI');return;}
 px=nx;py=ny;
 if(next==='R'){hp--;say('[SENSOR] qizil tuzoq! jon: '+hp);px=1;py=1;if(hp<=0){hp=3;hasKey=false;lvl=1;say('[GAME OVER] qaytadan boshlaymiz');}}
 if(next==='K'){hasKey=true;say('[SENSOR] sariq kalit olindi');map[py]=map[py].slice(0,nx)+'.'+map[py].slice(nx+1);px=nx;}
 if(next==='D'){
   if(hasKey){lvl++;say('[SENSOR] yashil eshik ochildi! Bosqich '+lvl);px=1;py=1;}
   else say('[SENSOR] eshik yopiq — KALIT KERAK');
 }
 draw();
}
document.addEventListener('keydown',e=>{
 const k=e.key;
 if(k==='ArrowLeft')move(-1,0);else if(k==='ArrowRight')move(1,0);
 else if(k==='ArrowUp')move(0,-1);else if(k==='ArrowDown')move(0,1);
});
function resetAll(){hp=3;hasKey=false;lvl=1;px=1;py=1;map[1]='#S..#...K..#';draw();say('[RESET] labirint qayta boshlandi');}
function exportReport(){const blob=new Blob([JSON.stringify({topic:'Smart Conditions',lvl,hp,hasKey,score:document.getElementById('score').textContent,date:new Date().toISOString()},null,2)],{type:'application/json'});const a=document.createElement('a');a.href=URL.createObjectURL(blob);a.download='maze_report.json';a.click();}
function say(t){document.getElementById('log').innerHTML+='\\n'+t;}
draw();
""",
    ),
]

for lab in LABS:
    path = os.path.join(ROOT, lab["path"])
    os.makedirs(os.path.dirname(path), exist_ok=True)
    content = SHELL.format(**lab)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print("Created:", lab["path"])
