/**
 * ============================================================
 * TARGET INTERNATIONAL SCHOOL — Kiber-Bunker 3D Horror Client
 * 5-6-Sinf · 8-Hafta · 23-Dars: Horror Game Studio Engine
 * Tech: Three.js · Web Audio API · PointerLock · WebSockets
 * ============================================================
 */

let scene, camera, renderer;
let spotLight, spotLightTarget;
let ambientLight;
let walls = [];
let doors3D = {};
let coreMeshes = [];
let anomalyMesh = null;
let anomalyLight = null;

// Game State
let gameState = {
  active: false,
  battery: 100,
  flashlightOn: true,
  stamina: 100,
  isSprinting: false,
  coresCollected: 0,
  alive: true,
  escaped: false,
  teamName: "Squad Alpha",
  startTime: null,
  doorAOpen: false,
  doorBOpen: false,
  exitOpen: false
};

// Controls & Movement
const keys = { w: false, a: false, s: false, d: false, shift: false };
const velocity = new THREE.Vector3();
const direction = new THREE.Vector3();
let euler = new THREE.Euler(0, 0, 0, 'YXZ');
const PI_2 = Math.PI / 2;
let isPointerLocked = false;

// Audio System (Web Audio API)
let audioCtx = null;
let heartbeatTimer = null;
let currentBpm = 72;

// WebSocket
let ws = null;
let clientId = 'p_' + Math.random().toString(36).substr(2, 6);

// -----------------------------------------------------------------------------
// TEXTURE GENERATORS (Procedural Canvas Textures for PBR/Metallic Realism)
// -----------------------------------------------------------------------------
function createMetalWallTexture() {
  const canvas = document.createElement('canvas');
  canvas.width = 512;
  canvas.height = 512;
  const ctx = canvas.getContext('2d');

  // Base metallic dark grey
  ctx.fillStyle = '#222831';
  ctx.fillRect(0, 0, 512, 512);

  // Rivets and panels
  ctx.strokeStyle = '#181E26';
  ctx.lineWidth = 4;
  ctx.strokeRect(4, 4, 504, 504);
  ctx.strokeRect(16, 16, 480, 480);

  // Noise / scratches / grime
  for (let i = 0; i < 800; i++) {
    const x = Math.random() * 512;
    const y = Math.random() * 512;
    const len = Math.random() * 30 + 5;
    ctx.strokeStyle = Math.random() > 0.5 ? 'rgba(0,0,0,0.3)' : 'rgba(255,255,255,0.06)';
    ctx.lineWidth = Math.random() * 2;
    ctx.beginPath();
    ctx.moveTo(x, y);
    ctx.lineTo(x + len, y + (Math.random() - 0.5) * 6);
    ctx.stroke();
  }

  // Rust stains
  for (let i = 0; i < 15; i++) {
    const rx = Math.random() * 512;
    const ry = Math.random() * 512;
    const rad = Math.random() * 40 + 10;
    const grad = ctx.createRadialGradient(rx, ry, 2, rx, ry, rad);
    grad.addColorStop(0, 'rgba(120, 45, 15, 0.45)');
    grad.addColorStop(1, 'rgba(120, 45, 15, 0.0)');
    ctx.fillStyle = grad;
    ctx.beginPath();
    ctx.arc(rx, ry, rad, 0, Math.PI * 2);
    ctx.fill();
  }

  return new THREE.CanvasTexture(canvas);
}

function createFloorTexture() {
  const canvas = document.createElement('canvas');
  canvas.width = 512;
  canvas.height = 512;
  const ctx = canvas.getContext('2d');

  ctx.fillStyle = '#141820';
  ctx.fillRect(0, 0, 512, 512);

  // Diamond plate steel grid
  ctx.strokeStyle = '#283142';
  ctx.lineWidth = 2;
  for (let x = 0; x < 512; x += 32) {
    for (let y = 0; y < 512; y += 32) {
      ctx.beginPath();
      ctx.moveTo(x + 4, y + 8);
      ctx.lineTo(x + 12, y + 16);
      ctx.stroke();
      ctx.beginPath();
      ctx.moveTo(x + 20, y + 24);
      ctx.lineTo(x + 28, y + 16);
      ctx.stroke();
    }
  }

  const texture = new THREE.CanvasTexture(canvas);
  texture.wrapS = THREE.RepeatWrapping;
  texture.wrapT = THREE.RepeatWrapping;
  texture.repeat.set(8, 8);
  return texture;
}

function createHazardTexture() {
  const canvas = document.createElement('canvas');
  canvas.width = 256;
  canvas.height = 256;
  const ctx = canvas.getContext('2d');

  ctx.fillStyle = '#0F131A';
  ctx.fillRect(0, 0, 256, 256);

  ctx.fillStyle = '#FFD60A';
  for (let i = -256; i < 512; i += 40) {
    ctx.beginPath();
    ctx.moveTo(i, 0);
    ctx.lineTo(i + 20, 0);
    ctx.lineTo(i + 20 + 256, 256);
    ctx.lineTo(i + 256, 256);
    ctx.fill();
  }
  return new THREE.CanvasTexture(canvas);
}

// -----------------------------------------------------------------------------
// AUDIO SYNTHESIZERS (Web Audio API)
// -----------------------------------------------------------------------------
function initAudio() {
  if (!audioCtx) {
    audioCtx = new (window.AudioContext || window.webkitAudioContext)();
  }
  if (audioCtx.state === 'suspended') {
    audioCtx.resume();
  }
}

function playHeartbeatSound() {
  if (!audioCtx) return;
  const now = audioCtx.currentTime;

  // Thump 1
  const osc1 = audioCtx.createOscillator();
  const gain1 = audioCtx.createGain();
  osc1.type = 'sine';
  osc1.frequency.setValueAtTime(65, now);
  osc1.frequency.exponentialRampToValueAtTime(35, now + 0.12);

  gain1.gain.setValueAtTime(0.4, now);
  gain1.gain.exponentialRampToValueAtTime(0.01, now + 0.12);

  osc1.connect(gain1);
  gain1.connect(audioCtx.destination);
  osc1.start(now);
  osc1.stop(now + 0.13);

  // Thump 2 (slightly softer, 0.15s later)
  const osc2 = audioCtx.createOscillator();
  const gain2 = audioCtx.createGain();
  osc2.type = 'sine';
  osc2.frequency.setValueAtTime(55, now + 0.15);
  osc2.frequency.exponentialRampToValueAtTime(30, now + 0.28);

  gain2.gain.setValueAtTime(0.3, now + 0.15);
  gain2.gain.exponentialRampToValueAtTime(0.01, now + 0.28);

  osc2.connect(gain2);
  gain2.connect(audioCtx.destination);
  osc2.start(now + 0.15);
  osc2.stop(now + 0.29);
}

function playFootstepSound(isSprint) {
  if (!audioCtx) return;
  const now = audioCtx.currentTime;
  const osc = audioCtx.createOscillator();
  const gain = audioCtx.createGain();

  osc.type = 'triangle';
  osc.frequency.setValueAtTime(isSprint ? 90 : 75, now);
  osc.frequency.exponentialRampToValueAtTime(30, now + 0.08);

  gain.gain.setValueAtTime(isSprint ? 0.25 : 0.15, now);
  gain.gain.exponentialRampToValueAtTime(0.01, now + 0.08);

  osc.connect(gain);
  gain.connect(audioCtx.destination);
  osc.start(now);
  osc.stop(now + 0.09);
}

function playRadioChirp() {
  if (!audioCtx) return;
  const now = audioCtx.currentTime;
  const osc = audioCtx.createOscillator();
  const gain = audioCtx.createGain();

  osc.type = 'sine';
  osc.frequency.setValueAtTime(880, now);
  osc.frequency.setValueAtTime(1200, now + 0.06);

  gain.gain.setValueAtTime(0.2, now);
  gain.gain.exponentialRampToValueAtTime(0.01, now + 0.15);

  osc.connect(gain);
  gain.connect(audioCtx.destination);
  osc.start(now);
  osc.stop(now + 0.16);
}

function playPickupChime() {
  if (!audioCtx) return;
  const now = audioCtx.currentTime;
  [523.25, 659.25, 783.99, 1046.50].forEach((freq, i) => {
    const osc = audioCtx.createOscillator();
    const gain = audioCtx.createGain();
    osc.type = 'sine';
    osc.frequency.setValueAtTime(freq, now + i * 0.06);
    gain.gain.setValueAtTime(0.25, now + i * 0.06);
    gain.gain.exponentialRampToValueAtTime(0.01, now + i * 0.06 + 0.3);
    osc.connect(gain);
    gain.connect(audioCtx.destination);
    osc.start(now + i * 0.06);
    osc.stop(now + i * 0.06 + 0.31);
  });
}

function playJumpscareSound() {
  if (!audioCtx) return;
  const now = audioCtx.currentTime;
  const osc = audioCtx.createOscillator();
  const gain = audioCtx.createGain();

  osc.type = 'sawtooth';
  osc.frequency.setValueAtTime(180, now);
  osc.frequency.linearRampToValueAtTime(700, now + 0.2);
  osc.frequency.exponentialRampToValueAtTime(90, now + 1.2);

  gain.gain.setValueAtTime(0.8, now);
  gain.gain.exponentialRampToValueAtTime(0.01, now + 1.2);

  osc.connect(gain);
  gain.connect(audioCtx.destination);
  osc.start(now);
  osc.stop(now + 1.25);
}

function playDoorSlideSound() {
  if (!audioCtx) return;
  const now = audioCtx.currentTime;
  const osc = audioCtx.createOscillator();
  const gain = audioCtx.createGain();

  osc.type = 'triangle';
  osc.frequency.setValueAtTime(120, now);
  osc.frequency.linearRampToValueAtTime(45, now + 0.6);

  gain.gain.setValueAtTime(0.3, now);
  gain.gain.exponentialRampToValueAtTime(0.01, now + 0.6);

  osc.connect(gain);
  gain.connect(audioCtx.destination);
  osc.start(now);
  osc.stop(now + 0.65);
}

// -----------------------------------------------------------------------------
// THREE.JS SCENE INITIALIZATION
// -----------------------------------------------------------------------------
function initScene() {
  const container = document.getElementById('gameContainer');

  scene = new THREE.Scene();
  scene.background = new THREE.Color(0x020408);
  scene.fog = new THREE.FogExp2(0x020408, 0.08);

  camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 100);
  camera.position.set(0, 1.6, 14); // Start in Spawn area

  renderer = new THREE.WebGLRenderer({ antialias: true, powerPreference: "high-performance" });
  renderer.setSize(window.innerWidth, window.innerHeight);
  renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
  renderer.shadowMap.enabled = true;
  renderer.shadowMap.type = THREE.PCFSoftShadowMap;
  container.appendChild(renderer.domElement);

  // Very dim ambient light so absolute darkness is realistic
  ambientLight = new THREE.AmbientLight(0x0a121e, 0.35);
  scene.add(ambientLight);

  // Player Flashlight (SpotLight attached to camera)
  spotLightTarget = new THREE.Object3D();
  scene.add(spotLightTarget);

  spotLight = new THREE.SpotLight(0xfff1dc, 3.8, 26, Math.PI / 4.2, 0.45, 1.4);
  spotLight.position.set(0, 0, 0);
  spotLight.castShadow = true;
  spotLight.shadow.mapSize.width = 1024;
  spotLight.shadow.mapSize.height = 1024;
  spotLight.target = spotLightTarget;
  camera.add(spotLight);
  scene.add(camera);

  buildBunkerEnvironment();
  buildAnomalyEntity();
  initPointerLock();

  window.addEventListener('resize', onWindowResize);
}

// -----------------------------------------------------------------------------
// ENVIRONMENT & BUNKER GEOMETRY
// -----------------------------------------------------------------------------
function buildBunkerEnvironment() {
  const wallMat = new THREE.MeshStandardMaterial({
    map: createMetalWallTexture(),
    roughness: 0.8,
    metalness: 0.35
  });

  const floorMat = new THREE.MeshStandardMaterial({
    map: createFloorTexture(),
    roughness: 0.6,
    metalness: 0.5
  });

  const ceilingMat = new THREE.MeshStandardMaterial({
    color: 0x121824,
    roughness: 0.95
  });

  const hazardMat = new THREE.MeshStandardMaterial({
    map: createHazardTexture(),
    roughness: 0.5
  });

  // Floor (44x44 meters)
  const floorGeo = new THREE.PlaneGeometry(44, 44);
  const floor = new THREE.Mesh(floorGeo, floorMat);
  floor.rotation.x = -Math.PI / 2;
  floor.receiveShadow = true;
  scene.add(floor);

  // Ceiling
  const ceiling = new THREE.Mesh(floorGeo, ceilingMat);
  ceiling.rotation.x = Math.PI / 2;
  ceiling.position.y = 3.6;
  scene.add(ceiling);

  // Helper to create a wall with collision box
  function addWall(x, z, w, d, h = 3.6, mat = wallMat) {
    const geo = new THREE.BoxGeometry(w, h, d);
    const mesh = new THREE.Mesh(geo, mat);
    mesh.position.set(x, h / 2, z);
    mesh.castShadow = true;
    mesh.receiveShadow = true;
    scene.add(mesh);

    // Save bounding box for player collision
    mesh.geometry.computeBoundingBox();
    walls.push({
      mesh,
      box: new THREE.Box3().setFromObject(mesh)
    });
    return mesh;
  }

  // Outer Perimeter Walls
  addWall(0, -22, 44, 1);
  addWall(0, 22, 44, 1);
  addWall(-22, 0, 1, 44);
  addWall(22, 0, 1, 44);

  // Internal Room Partitions
  // Sector A (Cryo Lab: -18, -18 to -8, -8)
  addWall(-13, -8, 10, 1);
  addWall(-8, -16, 1, 6); // Wall above Door A
  addWall(-8, -10, 1, 4); // Wall below Door A

  // Sector B (Reactor Core: 8, -18 to 18, -8)
  addWall(13, -8, 10, 1);
  addWall(8, -16, 1, 6);
  addWall(8, -10, 1, 4);

  // Sector C (Server Vault: 8, 8 to 18, 18)
  addWall(13, 8, 10, 1);
  addWall(8, 13, 1, 10);

  // Spawn Area (-18, 8 to -8, 18)
  addWall(-13, 8, 10, 1);
  addWall(-8, 13, 1, 10);

  // Surface Airlock Exit Gate (0, -21)
  const exitFrame = addWall(0, -20.5, 6, 1, 3.6, hazardMat);
  const exitDoorGeo = new THREE.BoxGeometry(3.6, 3.4, 0.4);
  const exitDoorMesh = new THREE.Mesh(exitDoorGeo, hazardMat);
  exitDoorMesh.position.set(0, 1.7, -20.5);
  scene.add(exitDoorMesh);
  doors3D.doorExit = exitDoorMesh;

  // Door A (Cryo Lab Entrance: -8, -13)
  const doorAGeo = new THREE.BoxGeometry(0.4, 3.4, 2.4);
  const doorAMesh = new THREE.Mesh(doorAGeo, hazardMat);
  doorAMesh.position.set(-8, 1.7, -13);
  doorAMesh.castShadow = true;
  scene.add(doorAMesh);
  doors3D.doorA = doorAMesh;

  // Door B (Reactor Entrance: 8, -13)
  const doorBGeo = new THREE.BoxGeometry(0.4, 3.4, 2.4);
  const doorBMesh = new THREE.Mesh(doorBGeo, hazardMat);
  doorBMesh.position.set(8, 1.7, -13);
  doorBMesh.castShadow = true;
  scene.add(doorBMesh);
  doors3D.doorB = doorBMesh;

  // Fluorescent Ceiling Lights (Flickering Lamps)
  addCeilingLight(0, 0, 0x00f0ff, 1.5);
  addCeilingLight(-14, -14, 0x3388ff, 2.2); // Cryo Lab Light
  addCeilingLight(14, -14, 0x34c759, 2.2);  // Reactor Light
  addCeilingLight(14, 14, 0xff9500, 2.0);   // Server Vault Light
  addCeilingLight(-14, 14, 0xffffff, 1.8);  // Spawn Light

  // 3D Collectible Energy Cores
  createEnergyCore(1, -14, -14, "Sector A: Cryo-Lab");
  createEnergyCore(2, 14, -14, "Sector B: Reactor Core");
  createEnergyCore(3, 14, 14, "Sector C: Server Vault");
}

function addCeilingLight(x, z, colorHex, intensity) {
  const light = new THREE.PointLight(colorHex, intensity, 12, 1.8);
  light.position.set(x, 3.3, z);
  scene.add(light);

  // Visual fixture mesh
  const fixtureGeo = new THREE.BoxGeometry(1.6, 0.1, 0.4);
  const fixtureMat = new THREE.MeshBasicMaterial({ color: colorHex });
  const fixture = new THREE.Mesh(fixtureGeo, fixtureMat);
  fixture.position.set(x, 3.5, z);
  scene.add(fixture);

  // Random lamp flicker loop
  setInterval(() => {
    if (Math.random() > 0.85) {
      light.intensity = 0.1;
      setTimeout(() => { light.intensity = intensity; }, Math.random() * 120 + 30);
    }
  }, 1000);
}

function createEnergyCore(id, x, z, room) {
  const group = new THREE.Group();
  group.position.set(x, 1.2, z);

  const coreGeo = new THREE.OctahedronGeometry(0.45);
  const coreMat = new THREE.MeshStandardMaterial({
    color: 0xffd60a,
    emissive: 0xffaa00,
    emissiveIntensity: 0.8,
    roughness: 0.2,
    metalness: 0.8
  });
  const coreMesh = new THREE.Mesh(coreGeo, coreMat);
  group.add(coreMesh);

  // Outer energy ring
  const ringGeo = new THREE.TorusGeometry(0.7, 0.04, 8, 24);
  const ringMat = new THREE.MeshBasicMaterial({ color: 0x00f0ff });
  const ring = new THREE.Mesh(ringGeo, ringMat);
  ring.rotation.x = Math.PI / 2;
  group.add(ring);

  const pLight = new THREE.PointLight(0xffd60a, 1.8, 6);
  group.add(pLight);

  scene.add(group);
  coreMeshes.push({ id, group, coreMesh, ring, pLight, room, collected: false });
}

// -----------------------------------------------------------------------------
// ANOMALY 3D ENTITY (The Monster)
// -----------------------------------------------------------------------------
function buildAnomalyEntity() {
  anomalyMesh = new THREE.Group();
  anomalyMesh.position.set(0, 0, -10);

  // Tall shadowy body
  const bodyGeo = new THREE.CylinderGeometry(0.3, 0.4, 2.4, 8);
  const bodyMat = new THREE.MeshStandardMaterial({
    color: 0x080808,
    roughness: 0.9,
    metalness: 0.1
  });
  const body = new THREE.Mesh(bodyGeo, bodyMat);
  body.position.y = 1.2;
  anomalyMesh.add(body);

  // Head
  const headGeo = new THREE.SphereGeometry(0.35, 12, 12);
  const head = new THREE.Mesh(headGeo, bodyMat);
  head.position.y = 2.4;
  anomalyMesh.add(head);

  // Glowing Red Eyes
  const eyeMat = new THREE.MeshBasicMaterial({ color: 0xff0000 });
  const eyeGeo = new THREE.SphereGeometry(0.06, 8, 8);

  const eyeL = new THREE.Mesh(eyeGeo, eyeMat);
  eyeL.position.set(-0.12, 2.45, 0.3);
  anomalyMesh.add(eyeL);

  const eyeR = new THREE.Mesh(eyeGeo, eyeMat);
  eyeR.position.set(0.12, 2.45, 0.3);
  anomalyMesh.add(eyeR);

  // Red glow light
  anomalyLight = new THREE.PointLight(0xff1100, 2.5, 8);
  anomalyLight.position.set(0, 2.2, 0.4);
  anomalyMesh.add(anomalyLight);

  scene.add(anomalyMesh);
}

// -----------------------------------------------------------------------------
// CONTROLS & POINTER LOCK
// -----------------------------------------------------------------------------
function initPointerLock() {
  document.addEventListener('keydown', (e) => {
    switch (e.code) {
      case 'KeyW': keys.w = true; break;
      case 'KeyA': keys.a = true; break;
      case 'KeyS': keys.s = true; break;
      case 'KeyD': keys.d = true; break;
      case 'ShiftLeft': case 'ShiftRight': keys.shift = true; break;
      case 'KeyF':
        gameState.flashlightOn = !gameState.flashlightOn;
        spotLight.visible = gameState.flashlightOn && gameState.battery > 0;
        break;
      case 'KeyE':
        handleInteraction();
        break;
    }
  });

  document.addEventListener('keyup', (e) => {
    switch (e.code) {
      case 'KeyW': keys.w = false; break;
      case 'KeyA': keys.a = false; break;
      case 'KeyS': keys.s = false; break;
      case 'KeyD': keys.d = false; break;
      case 'ShiftLeft': case 'ShiftRight': keys.shift = false; break;
    }
  });

  document.addEventListener('mousemove', (e) => {
    if (!isPointerLocked) return;
    const movementX = e.movementX || 0;
    const movementY = e.movementY || 0;

    euler.y -= movementX * 0.0022;
    euler.x -= movementY * 0.0022;
    euler.x = Math.max(-PI_2 + 0.05, Math.min(PI_2 - 0.05, euler.x));

    camera.quaternion.setFromEuler(euler);
  });

  document.addEventListener('pointerlockchange', () => {
    isPointerLocked = (document.pointerLockElement === document.body);
  });
}

function handleInteraction() {
  // Check if near any Energy Core
  coreMeshes.forEach(c => {
    if (!c.collected) {
      const dist = camera.position.distanceTo(c.group.position);
      if (dist < 2.6) {
        c.collected = true;
        scene.remove(c.group);
        gameState.coresCollected++;
        playPickupChime();
        document.getElementById('coreCount').textContent = `${gameState.coresCollected} / 3`;

        showRadioNotification(`⚡ ENERGIYA YADROSI TOPILDI! (${gameState.coresCollected}/3)`);

        if (ws && ws.readyState === WebSocket.OPEN) {
          ws.send(JSON.stringify({ type: 'collect_core', coreId: c.id }));
        }

        if (gameState.coresCollected >= 3) {
          gameState.exitOpen = true;
          doors3D.doorExit.position.y = 5.0; // Open exit blast door
          showRadioNotification(`🚨 BARCHA YADROLAR YIG'ILDI! CHIQISH AIRLOCK OCHILDI! QOCHING!`);
        }
      }
    }
  });
}

// -----------------------------------------------------------------------------
// WEBSOCKET INTEGRATION
// -----------------------------------------------------------------------------
function connectWebSocket() {
  const host = window.location.host || 'localhost:3000';
  const protocol = window.location.protocol === 'https:' ? 'wss:' : 'ws:';

  try {
    ws = new WebSocket(`${protocol}//${host}`);

    ws.onopen = () => {
      ws.send(JSON.stringify({
        type: 'player_join',
        id: clientId,
        team: gameState.teamName,
        x: camera.position.x,
        z: camera.position.z
      }));
    };

    ws.onmessage = (event) => {
      try {
        const msg = JSON.parse(event.data);

        if (msg.type === 'telemetry') {
          // Sync Anomaly position
          if (anomalyMesh && msg.anomaly) {
            anomalyMesh.position.x = msg.anomaly.x;
            anomalyMesh.position.z = msg.anomaly.z;
          }

          // Sync Doors
          if (msg.doors) {
            if (doors3D.doorA) {
              const shouldBeOpen = !msg.doors.doorA.locked;
              if (shouldBeOpen !== gameState.doorAOpen) {
                gameState.doorAOpen = shouldBeOpen;
                doors3D.doorA.position.y = shouldBeOpen ? 5.0 : 1.7;
                playDoorSlideSound();
              }
            }
            if (doors3D.doorB) {
              const shouldBeOpen = !msg.doors.doorB.locked;
              if (shouldBeOpen !== gameState.doorBOpen) {
                gameState.doorBOpen = shouldBeOpen;
                doors3D.doorB.position.y = shouldBeOpen ? 5.0 : 1.7;
                playDoorSlideSound();
              }
            }
          }
        } else if (msg.type === 'radio_transmission') {
          playRadioChirp();
          showRadioNotification(`📻 ${msg.sender}: ${msg.text}`);
        } else if (msg.type === 'power_boost_received') {
          gameState.battery = Math.min(100, gameState.battery + msg.amount);
          playPickupChime();
          showRadioNotification(`⚡ DISPETCHER: +${msg.amount}% CHIROQ QUVVATI YUBORILDI!`);
        } else if (msg.type === 'player_caught' && msg.playerId === clientId) {
          triggerGameOver();
        }
      } catch (e) {
        console.error("WS msg error", e);
      }
    };
  } catch (e) {
    console.log("WebSocket running offline fallback.");
  }
}

function showRadioNotification(text) {
  const alertEl = document.getElementById('hudRadioAlert');
  const msgEl = document.getElementById('radioMsgText');
  msgEl.textContent = text;
  alertEl.style.boxShadow = '0 0 24px rgba(0, 240, 255, 0.8)';
  setTimeout(() => {
    alertEl.style.boxShadow = '0 0 16px rgba(0, 240, 255, 0.3)';
  }, 2000);
}

// -----------------------------------------------------------------------------
// GAME LOOP & MOVEMENT PHYSICS
// -----------------------------------------------------------------------------
let prevTime = performance.now();

function animate() {
  requestAnimationFrame(animate);

  const time = performance.now();
  const delta = (time - prevTime) / 1000;
  prevTime = time;

  if (gameState.active && gameState.alive && !gameState.escaped) {
    updatePlayerMovement(delta);
    updateFlashlightAndBattery(delta);
    updateHeartbeatAndAnomaly(delta);
    updateHUDTimer();
    checkInteractions();
    checkVictory();

    // Rotate collectible cores
    coreMeshes.forEach(c => {
      if (!c.collected) {
        c.coreMesh.rotation.y += 0.02;
        c.ring.rotation.z += 0.03;
        c.group.position.y = 1.2 + Math.sin(time * 0.003) * 0.15;
      }
    });

    // Send periodic position to server
    if (ws && ws.readyState === WebSocket.OPEN && Math.random() > 0.7) {
      ws.send(JSON.stringify({
        type: 'player_move',
        x: camera.position.x,
        z: camera.position.z,
        rotation: euler.y,
        battery: Math.round(gameState.battery)
      }));
    }
  }

  renderer.render(scene, camera);
}

function updatePlayerMovement(delta) {
  // Stamina & Sprint
  gameState.isSprinting = keys.shift && (keys.w || keys.a || keys.s || keys.d) && gameState.stamina > 5;
  if (gameState.isSprinting) {
    gameState.stamina = Math.max(0, gameState.stamina - delta * 25);
  } else {
    gameState.stamina = Math.min(100, gameState.stamina + delta * 15);
  }
  document.getElementById('staminaBar').style.width = `${gameState.stamina}%`;

  const moveSpeed = gameState.isSprinting ? 6.2 : 3.4;

  velocity.x -= velocity.x * 10.0 * delta;
  velocity.z -= velocity.z * 10.0 * delta;

  direction.z = Number(keys.w) - Number(keys.s);
  direction.x = Number(keys.d) - Number(keys.a);
  direction.normalize();

  if (keys.w || keys.s) velocity.z -= direction.z * moveSpeed * 10.0 * delta;
  if (keys.a || keys.d) velocity.x -= direction.x * moveSpeed * 10.0 * delta;

  // Calculate intended movement vector
  const moveVector = new THREE.Vector3();
  moveVector.copy(velocity).multiplyScalar(delta);
  moveVector.applyEuler(new THREE.Euler(0, euler.y, 0));

  // Collision detection with bunker walls
  const nextPos = camera.position.clone().add(moveVector);
  let collideX = false;
  let collideZ = false;

  const playerRadius = 0.45;
  const playerBox = new THREE.Box3(
    new THREE.Vector3(nextPos.x - playerRadius, 0.2, camera.position.z - playerRadius),
    new THREE.Vector3(nextPos.x + playerRadius, 3.0, camera.position.z + playerRadius)
  );

  walls.forEach(w => {
    if (w.box.intersectsBox(playerBox)) collideX = true;
  });

  playerBox.min.x = camera.position.x - playerRadius;
  playerBox.max.x = camera.position.x + playerRadius;
  playerBox.min.z = nextPos.z - playerRadius;
  playerBox.max.z = nextPos.z + playerRadius;

  walls.forEach(w => {
    if (w.box.intersectsBox(playerBox)) collideZ = true;
  });

  // Check Door A collision if locked
  if (!gameState.doorAOpen && doors3D.doorA) {
    const doorBox = new THREE.Box3().setFromObject(doors3D.doorA);
    if (doorBox.intersectsBox(playerBox)) collideZ = true;
  }
  // Check Door B collision if locked
  if (!gameState.doorBOpen && doors3D.doorB) {
    const doorBox = new THREE.Box3().setFromObject(doors3D.doorB);
    if (doorBox.intersectsBox(playerBox)) collideZ = true;
  }
  // Check Exit Airlock collision if locked
  if (!gameState.exitOpen && doors3D.doorExit) {
    const doorBox = new THREE.Box3().setFromObject(doors3D.doorExit);
    if (doorBox.intersectsBox(playerBox)) collideZ = true;
  }

  if (!collideX) camera.position.x += moveVector.x;
  if (!collideZ) camera.position.z += moveVector.z;

  // Footstep audio triggers
  if ((keys.w || keys.a || keys.s || keys.d) && Math.random() > (gameState.isSprinting ? 0.8 : 0.92)) {
    playFootstepSound(gameState.isSprinting);
  }

  // Update spotlight target in front of camera
  const forward = new THREE.Vector3(0, 0, -1).applyQuaternion(camera.quaternion);
  spotLightTarget.position.copy(camera.position).add(forward.multiplyScalar(10));
}

function updateFlashlightAndBattery(delta) {
  if (gameState.flashlightOn) {
    gameState.battery = Math.max(0, gameState.battery - delta * 0.8);
    const batVal = Math.round(gameState.battery);
    document.getElementById('batteryText').textContent = `${batVal}%`;
    const bar = document.getElementById('batteryBar');
    bar.style.width = `${batVal}%`;

    if (batVal < 20) {
      bar.style.background = '#FF3B30';
      // Erratic flicker when low battery
      spotLight.intensity = Math.random() > 0.25 ? 3.8 : 0.4;
    } else if (batVal < 50) {
      bar.style.background = '#FF9500';
      spotLight.intensity = 3.8;
    } else {
      bar.style.background = '#34C759';
      spotLight.intensity = 3.8;
    }

    if (gameState.battery <= 0) {
      spotLight.visible = false;
    }
  } else {
    spotLight.visible = false;
  }
}

function updateHeartbeatAndAnomaly(delta) {
  if (!anomalyMesh) return;

  const dist = camera.position.distanceTo(anomalyMesh.position);

  // Proximity Heartbeat Calculation:
  // 20m -> 60 BPM
  // 10m -> 110 BPM
  // 3m  -> 175 BPM
  let targetBpm = 68;
  if (dist < 22) {
    const t = 1 - Math.max(0, Math.min(1, dist / 22));
    targetBpm = 68 + Math.round(t * 110);
  }

  currentBpm = targetBpm;
  document.getElementById('bpmVal').textContent = currentBpm;

  // Heartbeat interval
  if (!heartbeatTimer) {
    heartbeatTimer = setInterval(() => {
      if (gameState.active && gameState.alive) {
        playHeartbeatSound();
      }
    }, (60 / currentBpm) * 1000);
  }

  // Jumpscare Death Check
  if (dist < 1.6) {
    triggerGameOver();
  }
}

function updateHUDTimer() {
  if (!gameState.startTime) return;
  const elapsed = Math.floor((Date.now() - gameState.startTime) / 1000);
  const m = String(Math.floor(elapsed / 60)).padStart(2, '0');
  const s = String(elapsed % 60).padStart(2, '0');
  document.getElementById('missionTimer').textContent = `00:${m}:${s}`;
}

function checkInteractions() {
  const promptEl = document.getElementById('interactPrompt');
  let nearInteractable = false;

  coreMeshes.forEach(c => {
    if (!c.collected && camera.position.distanceTo(c.group.position) < 2.5) {
      nearInteractable = true;
      document.getElementById('promptText').textContent = "ENERGIYA YADROSINI OLISH [E]";
    }
  });

  if (nearInteractable) {
    promptEl.style.display = 'flex';
  } else {
    promptEl.style.display = 'none';
  }
}

function checkVictory() {
  // Exit point is at Z < -19
  if (gameState.exitOpen && camera.position.z < -19.5 && !gameState.escaped) {
    gameState.escaped = true;
    const finalTimeStr = document.getElementById('missionTimer').textContent.replace('00:', '');
    document.getElementById('finalTime').textContent = finalTimeStr;
    document.getElementById('victoryScreen').style.display = 'flex';
    document.exitPointerLock();

    if (ws && ws.readyState === WebSocket.OPEN) {
      ws.send(JSON.stringify({
        type: 'player_escaped',
        team: gameState.teamName,
        time: finalTimeStr
      }));
    }
  }
}

function triggerGameOver() {
  gameState.alive = false;
  playJumpscareSound();
  document.getElementById('jumpscareScreen').style.display = 'flex';
  document.exitPointerLock();
}

function onWindowResize() {
  camera.aspect = window.innerWidth / window.innerHeight;
  camera.updateProjectionMatrix();
  renderer.setSize(window.innerWidth, window.innerHeight);
}

// -----------------------------------------------------------------------------
// START BUTTON EVENT
// -----------------------------------------------------------------------------
document.getElementById('launchBtn').addEventListener('click', () => {
  const teamInput = document.getElementById('teamNameInput');
  if (teamInput && teamInput.value.trim()) {
    gameState.teamName = teamInput.value.trim();
  }

  initAudio();
  document.getElementById('startModal').style.display = 'none';
  document.body.requestPointerLock();

  gameState.active = true;
  gameState.startTime = Date.now();

  connectWebSocket();
});

// Boot Three.js
initScene();
animate();
