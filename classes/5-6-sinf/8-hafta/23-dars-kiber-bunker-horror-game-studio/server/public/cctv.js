/**
 * TARGET INTERNATIONAL SCHOOL — Kiber-Bunker CCTV Dispatch Script
 * Real-time 2D Radar Canvas · WebSocket Sync · Multi-language i18n
 */

let currentLang = 'uz';
let ws = null;
let bunkerState = {
  generatorPower: 100,
  alarmActive: false,
  alarmSector: null,
  doors: {
    doorA: { name: "Sector A (Cryo Lab)", locked: true },
    doorB: { name: "Sector B (Reactor Core)", locked: true },
    doorExit: { name: "Surface Airlock", locked: true }
  },
  coresTotal: 3,
  coresCollected: 0,
  coreLocations: [
    { id: 1, x: -14, z: -14, room: "Sector A: Cryo-Lab", taken: false },
    { id: 2, x: 14, z: -14, room: "Sector B: Reactor Core", taken: false },
    { id: 3, x: 14, z: 14, room: "Sector C: Server Vault", taken: false }
  ],
  anomaly: { x: 0, z: -10, state: "PATROL" },
  players: {},
  logs: []
};

// Radar Canvas
const canvas = document.getElementById('radarCanvas');
const ctx = canvas.getContext('2d');
let sweepAngle = 0;

// Coordinate mapping: Bunker is roughly -20 to +20 in X and Z
function toCanvasX(worldX) {
  return ((worldX + 22) / 44) * canvas.width;
}
function toCanvasY(worldZ) {
  return ((worldZ + 22) / 44) * canvas.height;
}

// Language Switcher
document.querySelectorAll('.pill-btn[data-lang]').forEach(btn => {
  btn.addEventListener('click', () => {
    document.querySelectorAll('.pill-btn[data-lang]').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
    currentLang = btn.dataset.lang;
    applyLanguage(currentLang);
  });
});

function applyLanguage(lang) {
  document.querySelectorAll('[data-ru], [data-en]').forEach(el => {
    if (!el.dataset.uz) el.dataset.uz = el.textContent;
    if (lang === 'uz') el.textContent = el.dataset.uz;
    else if (lang === 'ru' && el.dataset.ru) el.textContent = el.dataset.ru;
    else if (lang === 'en' && el.dataset.en) el.textContent = el.dataset.en;
  });
}

// Initialize WebSocket Connection
function initWebSocket() {
  const host = window.location.host || 'localhost:3000';
  const protocol = window.location.protocol === 'https:' ? 'wss:' : 'ws:';
  
  try {
    ws = new WebSocket(`${protocol}//${host}`);

    ws.onopen = () => {
      document.getElementById('connStatus').innerHTML = `
        <span class="status-indicator online"></span>
        <span>${currentLang === 'uz' ? 'SERVER ULANGAN' : currentLang === 'ru' ? 'СЕРВЕР ПОДКЛЮЧЕН' : 'SERVER CONNECTED'}</span>
      `;
      ws.send(JSON.stringify({ type: 'cctv_join' }));
    };

    ws.onmessage = (event) => {
      try {
        const msg = JSON.parse(event.data);
        if (msg.type === 'init') {
          bunkerState = msg.state;
          updateUI();
          renderLogs();
        } else if (msg.type === 'telemetry') {
          bunkerState.anomaly = msg.anomaly;
          bunkerState.generatorPower = msg.generatorPower;
          bunkerState.alarmActive = msg.alarmActive;
          bunkerState.alarmSector = msg.alarmSector;
          bunkerState.doors = msg.doors;
          bunkerState.coresCollected = msg.coresCollected;
          bunkerState.coreLocations = msg.cores;
          bunkerState.players = msg.players;
          updateUI();
        } else if (msg.type === 'new_log') {
          bunkerState.logs.unshift(msg.log);
          renderLogs();
        }
      } catch (err) {
        console.error("WS Parse Error", err);
      }
    };

    ws.onclose = () => {
      document.getElementById('connStatus').innerHTML = `
        <span class="status-indicator" style="background:#FF3B30; box-shadow:0 0 8px #FF3B30"></span>
        <span>${currentLang === 'uz' ? 'ALOQA UZILDI (RETRY...)' : currentLang === 'ru' ? 'НЕТ СВЯЗИ' : 'DISCONNECTED'}</span>
      `;
      setTimeout(initWebSocket, 2000);
    };

    ws.onerror = () => {
      ws.close();
    };
  } catch (e) {
    console.log("Offline mode active.");
  }
}

// UI Updaters
function updateUI() {
  // Generator Power
  const genVal = Math.max(0, Math.round(bunkerState.generatorPower));
  document.getElementById('genPowerText').textContent = `${genVal}%`;
  const bar = document.getElementById('genPowerBar');
  bar.style.width = `${genVal}%`;
  if (genVal < 25) {
    bar.style.background = '#FF3B30';
  } else if (genVal < 50) {
    bar.style.background = '#FF9500';
  } else {
    bar.style.background = 'linear-gradient(90deg, #34C759, #30D158)';
  }

  // Anomaly Status
  const badge = document.getElementById('anomalyStatusText');
  const anomState = bunkerState.anomaly ? bunkerState.anomaly.state : 'PATROL';
  badge.className = `stat-val threat-badge ${anomState.toLowerCase()}`;
  if (anomState === 'PATROL') {
    badge.textContent = currentLang === 'uz' ? 'PATRUL QILMOQDA' : currentLang === 'ru' ? 'ПАТРУЛИРУЕТ' : 'PATROLLING';
  } else if (anomState === 'HUNT') {
    badge.textContent = currentLang === 'uz' ? '🚨 QIDIRUV VA TA\'QIB!' : currentLang === 'ru' ? '🚨 ОХОТА НА ИГРОКА!' : '🚨 HUNTING!';
  } else {
    badge.textContent = currentLang === 'uz' ? '⚡ CHALG\'IGAN (OG\'LUSHEN)' : currentLang === 'ru' ? '⚡ ОГЛУШЕН' : '⚡ DISTRACTED';
  }

  // Cores Visual
  const collected = bunkerState.coresCollected || 0;
  for (let i = 1; i <= 3; i++) {
    const slot = document.getElementById(`coreSlot${i}`);
    if (i <= collected) {
      slot.classList.add('active');
    } else {
      slot.classList.remove('active');
    }
  }

  // Doors
  const doorA = bunkerState.doors.doorA;
  const doorB = bunkerState.doors.doorB;
  const stateA = document.getElementById('doorAState');
  const stateB = document.getElementById('doorBState');

  if (doorA.locked) {
    stateA.className = 'btn-state locked';
    stateA.textContent = currentLang === 'uz' ? 'QULFLANGAN 🔒' : currentLang === 'ru' ? 'ЗАПЕРТО 🔒' : 'LOCKED 🔒';
  } else {
    stateA.className = 'btn-state unlocked';
    stateA.textContent = currentLang === 'uz' ? 'OCHIQ 🟢' : currentLang === 'ru' ? 'ОТКРЫТО 🟢' : 'UNLOCKED 🟢';
  }

  if (doorB.locked) {
    stateB.className = 'btn-state locked';
    stateB.textContent = currentLang === 'uz' ? 'QULFLANGAN 🔒' : currentLang === 'ru' ? 'ЗАПЕРТО 🔒' : 'LOCKED 🔒';
  } else {
    stateB.className = 'btn-state unlocked';
    stateB.textContent = currentLang === 'uz' ? 'OCHIQ 🟢' : currentLang === 'ru' ? 'ОТКРЫТО 🟢' : 'UNLOCKED 🟢';
  }
}

function renderLogs() {
  const container = document.getElementById('logStream');
  container.innerHTML = '';
  document.getElementById('logCount').textContent = `${bunkerState.logs.length} ta yozuv`;

  bunkerState.logs.forEach(item => {
    const div = document.createElement('div');
    let category = 'SYSTEM';
    if (item.sender.includes('DANGER') || item.sender.includes('CASUALTY') || item.sender.includes('AI')) category = 'DANGER';
    if (item.sender.includes('OBJECTIVE') || item.sender.includes('VICTORY')) category = 'OBJECTIVE';
    if (item.sender.includes('CCTV') || item.sender.includes('DISPATCH')) category = 'CCTV';

    div.className = `log-entry ${category}`;
    div.innerHTML = `<span class="log-time">[${item.time}]</span><span class="log-sender">${item.sender}:</span> ${item.text}`;
    container.appendChild(div);
  });
}

// Tactical Actions
function toggleDoor(doorId) {
  if (ws && ws.readyState === WebSocket.OPEN) {
    ws.send(JSON.stringify({ type: 'cctv_door_override', doorId }));
  } else {
    // Offline simulated toggle
    bunkerState.doors[doorId].locked = !bunkerState.doors[doorId].locked;
    updateUI();
  }
}

function sendPowerSurge() {
  if (ws && ws.readyState === WebSocket.OPEN) {
    ws.send(JSON.stringify({ type: 'cctv_power_boost' }));
  } else {
    bunkerState.generatorPower = Math.max(0, bunkerState.generatorPower - 15);
    updateUI();
  }
}

function triggerDistractionSiren() {
  if (ws && ws.readyState === WebSocket.OPEN) {
    ws.send(JSON.stringify({ type: 'cctv_trigger_alarm', sector: 'Sector A' }));
  } else {
    bunkerState.anomaly.state = 'STUNNED';
    updateUI();
  }
}

function sendQuickRadio(text) {
  if (ws && ws.readyState === WebSocket.OPEN) {
    ws.send(JSON.stringify({ type: 'cctv_radio_msg', text, sender: 'CCTV DISPATCH' }));
  }
}

function sendCustomRadio() {
  const input = document.getElementById('radioInput');
  const text = input.value.trim();
  if (!text) return;
  if (ws && ws.readyState === WebSocket.OPEN) {
    ws.send(JSON.stringify({ type: 'cctv_radio_msg', text, sender: 'CCTV DISPATCH' }));
  }
  input.value = '';
}

// -----------------------------------------------------------------------------
// RADAR CANVAS RENDERING LOOP
// -----------------------------------------------------------------------------
function drawRadar() {
  ctx.clearRect(0, 0, canvas.width, canvas.height);

  // Background grid
  ctx.strokeStyle = '#0E1F36';
  ctx.lineWidth = 1;
  const step = canvas.width / 8;
  for (let i = 0; i < canvas.width; i += step) {
    ctx.beginPath(); ctx.moveTo(i, 0); ctx.lineTo(i, canvas.height); ctx.stroke();
    ctx.beginPath(); ctx.moveTo(0, i); ctx.lineTo(canvas.width, i); ctx.stroke();
  }

  // Draw Bunker Sectors / Rooms
  ctx.fillStyle = 'rgba(16, 32, 58, 0.45)';
  ctx.strokeStyle = '#1D3B66';
  ctx.lineWidth = 2;

  // Sector A (Cryo Lab: -18, -18 to -8, -8)
  const aX = toCanvasX(-18), aY = toCanvasY(-18), aW = toCanvasX(-8) - aX, aH = toCanvasY(-8) - aY;
  ctx.fillRect(aX, aY, aW, aH); ctx.strokeRect(aX, aY, aW, aH);

  // Sector B (Reactor Core: 8, -18 to 18, -8)
  const bX = toCanvasX(8), bY = toCanvasY(-18), bW = toCanvasX(18) - bX, bH = toCanvasY(-8) - bY;
  ctx.fillRect(bX, bY, bW, bH); ctx.strokeRect(bX, bY, bW, bH);

  // Sector C (Server Vault: 8, 8 to 18, 18)
  const cX = toCanvasX(8), cY = toCanvasY(8), cW = toCanvasX(18) - cX, cH = toCanvasY(18) - cY;
  ctx.fillRect(cX, cY, cW, cH); ctx.strokeRect(cX, cY, cW, cH);

  // Start Airlock (-18, 8 to -8, 18)
  const sX = toCanvasX(-18), sY = toCanvasY(8), sW = toCanvasX(-8) - sX, sH = toCanvasY(18) - sY;
  ctx.fillRect(sX, sY, sW, sH); ctx.strokeRect(sX, sY, sW, sH);

  // Surface Exit Airlock (-4, -20 to 4, -16)
  const eX = toCanvasX(-5), eY = toCanvasY(-20), eW = toCanvasX(5) - eX, eH = toCanvasY(-16) - eY;
  ctx.fillStyle = bunkerState.doors.doorExit.locked ? 'rgba(255, 59, 48, 0.15)' : 'rgba(52, 199, 89, 0.25)';
  ctx.strokeStyle = bunkerState.doors.doorExit.locked ? '#FF3B30' : '#34C759';
  ctx.fillRect(eX, eY, eW, eH); ctx.strokeRect(eX, eY, eW, eH);

  // Corridors Connecting Sectors
  ctx.fillStyle = 'rgba(10, 20, 36, 0.7)';
  // Horizontal Main corridor
  ctx.fillRect(toCanvasX(-18), toCanvasY(-2), toCanvasX(18) - toCanvasX(-18), toCanvasY(2) - toCanvasY(-2));
  // Vertical Main corridor
  ctx.fillRect(toCanvasX(-2), toCanvasY(-18), toCanvasX(2) - toCanvasX(-2), toCanvasY(18) - toCanvasY(-18));

  // Room Labels
  ctx.font = '10px "JetBrains Mono"';
  ctx.fillStyle = '#6E88AC';
  ctx.fillText("SECTOR A (CRYO)", aX + 8, aY + 16);
  ctx.fillText("SECTOR B (REACTOR)", bX + 8, bY + 16);
  ctx.fillText("SECTOR C (VAULT)", cX + 8, cY + 16);
  ctx.fillText("SPAWN BAY", sX + 8, sY + 16);
  ctx.fillStyle = bunkerState.doors.doorExit.locked ? '#FF3B30' : '#34C759';
  ctx.fillText("EXIT AIRLOCK", eX + 6, eY + 14);

  // Draw Blast Doors
  drawDoorMarker(-8, -13, bunkerState.doors.doorA.locked, "DOOR A");
  drawDoorMarker(8, -13, bunkerState.doors.doorB.locked, "DOOR B");

  // Draw Energy Cores
  bunkerState.coreLocations.forEach(core => {
    if (!core.taken) {
      const cx = toCanvasX(core.x);
      const cy = toCanvasY(core.z);
      ctx.beginPath();
      ctx.arc(cx, cy, 6, 0, Math.PI * 2);
      ctx.fillStyle = '#FFD60A';
      ctx.shadowColor = '#FFD60A';
      ctx.shadowBlur = 10;
      ctx.fill();
      ctx.shadowBlur = 0;
      ctx.fillStyle = '#000';
      ctx.font = 'bold 8px "JetBrains Mono"';
      ctx.fillText("⚡", cx - 4, cy + 3);
    }
  });

  // Draw Anomaly
  if (bunkerState.anomaly) {
    const ax = toCanvasX(bunkerState.anomaly.x);
    const ay = toCanvasY(bunkerState.anomaly.z);

    // Threat detection circle
    ctx.beginPath();
    ctx.arc(ax, ay, 24, 0, Math.PI * 2);
    ctx.strokeStyle = 'rgba(255, 59, 48, 0.35)';
    ctx.lineWidth = 1.5;
    ctx.stroke();

    // Red Skull / Anomaly Blip
    ctx.beginPath();
    ctx.arc(ax, ay, 8, 0, Math.PI * 2);
    ctx.fillStyle = '#FF3B30';
    ctx.shadowColor = '#FF3B30';
    ctx.shadowBlur = 14;
    ctx.fill();
    ctx.shadowBlur = 0;

    ctx.fillStyle = '#FFF';
    ctx.font = 'bold 9px "JetBrains Mono"';
    ctx.fillText("☠", ax - 4.5, ay + 3.5);
  }

  // Draw 3D Players
  Object.values(bunkerState.players).forEach(p => {
    if (p.alive) {
      const px = toCanvasX(p.x);
      const py = toCanvasY(p.z);

      // Vision / Flashlight cone direction
      const rot = p.rotation || 0;
      ctx.beginPath();
      ctx.moveTo(px, py);
      ctx.arc(px, py, 26, -rot - 0.5, -rot + 0.5);
      ctx.closePath();
      ctx.fillStyle = 'rgba(0, 240, 255, 0.2)';
      ctx.fill();

      // Cyan Player Dot
      ctx.beginPath();
      ctx.arc(px, py, 7, 0, Math.PI * 2);
      ctx.fillStyle = '#00F0FF';
      ctx.shadowColor = '#00F0FF';
      ctx.shadowBlur = 12;
      ctx.fill();
      ctx.shadowBlur = 0;

      ctx.fillStyle = '#000';
      ctx.font = 'bold 8px "JetBrains Mono"';
      ctx.fillText("P", px - 3, py + 3);
    }
  });

  // Rotating Radar Sweep Line
  sweepAngle += 0.025;
  const centerX = canvas.width / 2;
  const centerY = canvas.height / 2;
  const sweepRadius = canvas.width * 0.7;
  const endX = centerX + Math.cos(sweepAngle) * sweepRadius;
  const endY = centerY + Math.sin(sweepAngle) * sweepRadius;

  const gradient = ctx.createRadialGradient(centerX, centerY, 10, centerX, centerY, sweepRadius);
  gradient.addColorStop(0, 'rgba(0, 240, 255, 0.15)');
  gradient.addColorStop(1, 'rgba(0, 240, 255, 0.0)');

  ctx.beginPath();
  ctx.moveTo(centerX, centerY);
  ctx.arc(centerX, centerY, sweepRadius, sweepAngle - 0.35, sweepAngle);
  ctx.closePath();
  ctx.fillStyle = gradient;
  ctx.fill();

  ctx.beginPath();
  ctx.moveTo(centerX, centerY);
  ctx.lineTo(endX, endY);
  ctx.strokeStyle = 'rgba(0, 240, 255, 0.4)';
  ctx.lineWidth = 1.5;
  ctx.stroke();

  requestAnimationFrame(drawRadar);
}

function drawDoorMarker(x, z, isLocked, label) {
  const dx = toCanvasX(x);
  const dy = toCanvasY(z);
  ctx.fillStyle = isLocked ? '#FF3B30' : '#34C759';
  ctx.fillRect(dx - 12, dy - 3, 24, 6);
  ctx.fillStyle = '#FFF';
  ctx.font = '8px "JetBrains Mono"';
  ctx.fillText(label, dx - 14, dy - 6);
}

// Start
initWebSocket();
requestAnimationFrame(drawRadar);
