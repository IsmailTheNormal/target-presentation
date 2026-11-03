/**
 * ============================================================
 * TARGET INTERNATIONAL SCHOOL — Kiber-Bunker Backend Server
 * 5-6-Sinf · 8-Hafta · 23-Dars: Horror Game Studio & Asymmetric Co-op
 * Tech: Node.js · Express · WebSockets (ws) · REST API
 * ============================================================
 */

const express = require('express');
const http = require('http');
const path = require('path');
const WebSocket = require('ws');

const app = express();
const server = http.createServer(app);
const wss = new WebSocket.Server({ server });

const PORT = process.env.PORT || 3000;

app.use(express.json());
// Serve the 3D Client from ../client
app.use(express.static(path.join(__dirname, '../client')));

// Serve the CCTV Terminal from ./public
app.use('/cctv', express.static(path.join(__dirname, 'public'), { index: ['cctv.html', 'index.html'] }));
app.get('/cctv.css', (req, res) => res.sendFile(path.join(__dirname, 'public/cctv.css')));
app.get('/cctv.js', (req, res) => res.sendFile(path.join(__dirname, 'public/cctv.js')));

// -----------------------------------------------------------------------------
// GAME STATE MANAGEMENT (Node.js InMemory State)
// -----------------------------------------------------------------------------
const bunkerState = {
  generatorPower: 100, // 0 - 100%
  alarmActive: false,
  alarmSector: null,
  doors: {
    doorA: { name: "Sector A (Cryo Lab)", locked: true, code: "4041" },
    doorB: { name: "Sector B (Reactor Core)", locked: true, code: "7319" },
    doorExit: { name: "Surface Airlock (Exit)", locked: true, requiredCores: 3 }
  },
  coresTotal: 3,
  coresCollected: 0,
  coreLocations: [
    { id: 1, x: -14, z: -14, room: "Sector A: Cryo-Lab", taken: false },
    { id: 2, x: 14, z: -14, room: "Sector B: Reactor Core", taken: false },
    { id: 3, x: 14, z: 14, room: "Sector C: Server Vault", taken: false }
  ],
  anomaly: {
    x: 0,
    z: -10,
    targetX: 0,
    targetZ: -10,
    speed: 0.08,
    state: "PATROL", // PATROL, HUNT, STUNNED
    stunTimer: 0,
    waypoints: [
      { x: 0, z: -10 },
      { x: -12, z: -12 },
      { x: 0, z: 0 },
      { x: 12, z: -12 },
      { x: 12, z: 12 },
      { x: -12, z: 12 }
    ],
    currentWpIndex: 0
  },
  players: {}, // id -> { id, team, x, z, rotation, battery, hp, alive, cores }
  survivors: [
    { team: "Cyber-Guard 5A", time: "03:42", cores: 3, date: "2026-11-03" },
    { team: "Shadow Hunters 6B", time: "04:15", cores: 3, date: "2026-11-03" }
  ],
  logs: [
    { time: "00:00", sender: "SYSTEM", text: "Kiber-Bunker server ishga tushdi. Havfsizlik quvvati: 100%." }
  ]
};

function addLog(sender, text) {
  const now = new Date();
  const timeStr = `${String(now.getMinutes()).padStart(2, '0')}:${String(now.getSeconds()).padStart(2, '0')}`;
  const logItem = { time: timeStr, sender, text };
  bunkerState.logs.unshift(logItem);
  if (bunkerState.logs.length > 30) bunkerState.logs.pop();
  broadcast({ type: "new_log", log: logItem });
}

// -----------------------------------------------------------------------------
// WEBSOCKET BROADCAST & CLIENT HANDLERS
// -----------------------------------------------------------------------------
function broadcast(data) {
  const msg = JSON.stringify(data);
  wss.clients.forEach(client => {
    if (client.readyState === WebSocket.OPEN) {
      client.send(msg);
    }
  });
}

// Anomaly AI Heartbeat Loop (Server Tick: 500ms)
setInterval(() => {
  const anom = bunkerState.anomaly;
  if (anom.state === "STUNNED") {
    anom.stunTimer -= 0.5;
    if (anom.stunTimer <= 0) {
      anom.state = "PATROL";
      addLog("AI ANOMALY", "Anomaliya chalg'itishdan qutuldi. Patrul qayta tiklandi!");
    }
  } else if (anom.state === "PATROL") {
    // Patrol towards current waypoint
    const wp = anom.waypoints[anom.currentWpIndex];
    const dx = wp.x - anom.x;
    const dz = wp.z - anom.z;
    const dist = Math.sqrt(dx * dx + dz * dz);

    if (dist < 1.0) {
      anom.currentWpIndex = (anom.currentWpIndex + 1) % anom.waypoints.length;
    } else {
      anom.x += (dx / dist) * 0.45;
      anom.z += (dz / dist) * 0.45;
    }

    // Check if any alive player is within detection distance (e.g. 7 meters)
    Object.values(bunkerState.players).forEach(p => {
      if (p.alive) {
        const pdx = p.x - anom.x;
        const pdz = p.z - anom.z;
        const pDist = Math.sqrt(pdx * pdx + pdz * pdz);
        if (pDist < 6.5) {
          anom.state = "HUNT";
          anom.targetX = p.x;
          anom.targetZ = p.z;
          addLog("DANGER", `🚨 Anomaliya o'yinchini payqadi! (Masofa: ${pDist.toFixed(1)}m)`);
        }
      }
    });
  } else if (anom.state === "HUNT") {
    // Find closest player
    let closest = null;
    let minDist = 999;
    Object.values(bunkerState.players).forEach(p => {
      if (p.alive) {
        const pdx = p.x - anom.x;
        const pdz = p.z - anom.z;
        const pDist = Math.sqrt(pdx * pdx + pdz * pdz);
        if (pDist < minDist) {
          minDist = pDist;
          closest = p;
        }
      }
    });

    if (closest && minDist < 15.0) {
      const dx = closest.x - anom.x;
      const dz = closest.z - anom.z;
      anom.x += (dx / minDist) * 0.7;
      anom.z += (dz / minDist) * 0.7;

      if (minDist < 1.4) {
        // Attack player!
        closest.alive = false;
        closest.hp = 0;
        addLog("CASUALTY", `⚠️ O'yinchi [${closest.team || closest.id}] Anomaliya tomonidan qo'lga olindi!`);
        broadcast({ type: "player_caught", playerId: closest.id });
        anom.state = "PATROL";
      }
    } else {
      anom.state = "PATROL";
    }
  }

  // Periodic Telemetry Broadcast to all connected clients (3D pilots & CCTV screens)
  broadcast({
    type: "telemetry",
    anomaly: { x: anom.x, z: anom.z, state: anom.state },
    generatorPower: bunkerState.generatorPower,
    alarmActive: bunkerState.alarmActive,
    alarmSector: bunkerState.alarmSector,
    doors: bunkerState.doors,
    coresCollected: bunkerState.coresCollected,
    cores: bunkerState.coreLocations,
    players: bunkerState.players
  });
}, 400);

wss.on('connection', (ws) => {
  let clientId = 'client_' + Math.random().toString(36).substr(2, 6);
  let isPlayer = false;

  ws.send(JSON.stringify({
    type: "init",
    clientId,
    state: bunkerState
  }));

  ws.on('message', (message) => {
    try {
      const data = JSON.parse(message);

      switch (data.type) {
        case 'player_join':
          isPlayer = true;
          clientId = data.id || clientId;
          bunkerState.players[clientId] = {
            id: clientId,
            team: data.team || "Squad Alpha",
            x: data.x || 0,
            z: data.z || 14,
            rotation: 0,
            battery: 100,
            hp: 100,
            alive: true,
            cores: 0
          };
          addLog("PILOT", `Yangi 3D Explorer qo'shildi: [${bunkerState.players[clientId].team}]`);
          break;

        case 'player_move':
          if (bunkerState.players[clientId]) {
            bunkerState.players[clientId].x = data.x;
            bunkerState.players[clientId].z = data.z;
            bunkerState.players[clientId].rotation = data.rotation;
            bunkerState.players[clientId].battery = data.battery;
          }
          break;

        case 'collect_core':
          const core = bunkerState.coreLocations.find(c => c.id === data.coreId);
          if (core && !core.taken) {
            core.taken = true;
            bunkerState.coresCollected++;
            if (bunkerState.players[clientId]) {
              bunkerState.players[clientId].cores++;
            }
            addLog("OBJECTIVE", `⚡ Energiya yadrosi topildi! [${core.room}] (${bunkerState.coresCollected}/3)`);
            if (bunkerState.coresCollected >= 3) {
              bunkerState.doors.doorExit.locked = false;
              addLog("ALERT", `🟢 BARCHA YADROLAR YIG'ILDI! Chiqish havo lyuki (Surface Airlock) OCHILDI!`);
            }
          }
          break;

        case 'cctv_door_override':
          const targetDoor = bunkerState.doors[data.doorId];
          if (targetDoor) {
            targetDoor.locked = !targetDoor.locked;
            const statusStr = targetDoor.locked ? "QULFLANDI 🔴" : "OCHILDI 🟢";
            addLog("CCTV OVERRIDE", `Dispetcher eshikni o'zgartirdi: [${targetDoor.name}] -> ${statusStr}`);
          }
          break;

        case 'cctv_power_boost':
          if (bunkerState.generatorPower >= 15) {
            bunkerState.generatorPower -= 15;
            Object.values(bunkerState.players).forEach(p => {
              p.battery = Math.min(100, p.battery + 35);
            });
            addLog("CCTV COMMAND", `⚡ Dispetcher zaxira quvvat impulsi yubordi! (+35% Chiroq quvvati)`);
            broadcast({ type: "power_boost_received", amount: 35 });
          } else {
            addLog("WARNING", `⚠️ Generator quvvati yetarli emas! (Qoldiq: ${bunkerState.generatorPower}%)`);
          }
          break;

        case 'cctv_trigger_alarm':
          // Distract anomaly to a chosen sector
          bunkerState.alarmActive = true;
          bunkerState.alarmSector = data.sector || "Sector A";
          bunkerState.anomaly.state = "STUNNED";
          bunkerState.anomaly.stunTimer = 6.0; // 6 seconds stun/distraction
          addLog("CCTV SIREN", `🚨 [${bunkerState.alarmSector}] da qizil signalizatsiya yoqildi! Anomaliya 6 soniya chalg'idi!`);
          setTimeout(() => {
            bunkerState.alarmActive = false;
            bunkerState.alarmSector = null;
          }, 6000);
          break;

        case 'cctv_radio_msg':
          addLog("DISPATCH RADIO", `📻 "${data.text}"`);
          broadcast({ type: "radio_transmission", text: data.text, sender: data.sender || "DISPATCH" });
          break;

        case 'player_escaped':
          addLog("VICTORY", `🏆 G'ALABA! [${data.team}] jamoasi barcha 3 ta yadro bilan bunkerdan qochishga muvaffaq bo'ldi!`);
          bunkerState.survivors.unshift({
            team: data.team || "Squad",
            time: data.time || "02:50",
            cores: 3,
            date: new Date().toISOString().split('T')[0]
          });
          broadcast({ type: "team_victory", team: data.team, time: data.time });
          break;
      }
    } catch (e) {
      console.error("WS error:", e);
    }
  });

  ws.on('close', () => {
    if (isPlayer && bunkerState.players[clientId]) {
      addLog("SYSTEM", `O'yinchi [${bunkerState.players[clientId].team}] tarmoqdan uzildi.`);
      delete bunkerState.players[clientId];
    }
  });
});

// -----------------------------------------------------------------------------
// REST API ENDPOINTS
// -----------------------------------------------------------------------------
app.get('/api/status', (req, res) => {
  res.json({
    status: "ONLINE",
    bunker: bunkerState
  });
});

app.get('/api/bunker/layout', (req, res) => {
  res.json({
    sectors: [
      { id: "A", name: "Cryo-Lab", x: -14, z: -14, door: "doorA" },
      { id: "B", name: "Reactor Core", x: 14, z: -14, door: "doorB" },
      { id: "C", name: "Server Vault", x: 14, z: 14, door: null },
      { id: "EXIT", name: "Surface Airlock", x: 0, z: -18, door: "doorExit" }
    ],
    cores: bunkerState.coreLocations
  });
});

app.post('/api/doors/override', (req, res) => {
  const { doorId } = req.body;
  if (bunkerState.doors[doorId]) {
    bunkerState.doors[doorId].locked = !bunkerState.doors[doorId].locked;
    addLog("API OVERRIDE", `REST API: ${doorId} holati o'zgartirildi.`);
    return res.json({ success: true, door: bunkerState.doors[doorId] });
  }
  res.status(400).json({ error: "Invalid door ID" });
});

app.post('/api/generator/boost', (req, res) => {
  bunkerState.generatorPower = Math.min(100, bunkerState.generatorPower + 25);
  addLog("REST API", `Generator quvvati qo'lda to'ldirildi.`);
  res.json({ success: true, generatorPower: bunkerState.generatorPower });
});

app.get('/api/survivors', (req, res) => {
  res.json(bunkerState.survivors);
});

// Start Server
server.listen(PORT, () => {
  console.log(`=======================================================`);
  console.log(`🎮 KIBER-BUNKER HORROR ENGINE SERVER IS RUNNING!`);
  console.log(`📍 3D Client (Laptops):      http://localhost:${PORT}`);
  console.log(`📡 CCTV Terminal (Phones):    http://localhost:${PORT}/cctv`);
  console.log(`⚡ WebSocket Server:          ws://localhost:${PORT}`);
  console.log(`=======================================================`);
});
