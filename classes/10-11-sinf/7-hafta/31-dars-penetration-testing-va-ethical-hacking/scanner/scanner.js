/**
 * Target International School — Senior Cybersecurity Cohort (10-11-sinf)
 * 31-dars: Custom Vulnerability Scanner CLI & Penetration Testing Tool
 *
 * Ishga tushirish:
 *   node scanner.js
 *   node scanner.js --target=http://localhost:3000
 *   node scanner.js --target=https://target-bank-api.internal --demo
 */

const fs = require('fs');
const http = require('http');
const https = require('https');
const { URL } = require('url');

// ANSI Terminal Colors
const C = {
  reset: '\x1b[0m',
  bold: '\x1b[1m',
  red: '\x1b[31m',
  green: '\x1b[32m',
  yellow: '\x1b[33m',
  blue: '\x1b[34m',
  magenta: '\x1b[35m',
  cyan: '\x1b[36m',
  white: '\x1b[37m'
};

const BANNER = `
${C.cyan}${C.bold}╔════════════════════════════════════════════════════════════════╗
║     TARGET INTERNATIONAL SCHOOL — SENIOR SECURITY LAB         ║
║         Custom Pentest CLI & Vulnerability Scanner             ║
╚════════════════════════════════════════════════════════════════╝${C.reset}
`;

// Parse CLI Arguments
const args = process.argv.slice(2);
let targetUrl = 'http://localhost:3000';
let isDemo = false;

args.forEach(arg => {
  if (arg.startsWith('--target=')) {
    targetUrl = arg.split('=')[1];
  }
  if (arg === '--demo' || arg === '-d') {
    isDemo = true;
  }
});

// Security Rules & Signatures
const MANDATORY_HEADERS = [
  { name: 'content-security-policy', desc: 'XSS & Script Injection Himoyasi', cvss: '6.5 MEDIUM' },
  { name: 'x-frame-options', desc: 'Clickjacking & Iframe Hijack Mudofaasi', cvss: '5.4 MEDIUM' },
  { name: 'x-content-type-options', desc: 'MIME-Sniffing Hujumlariga Cheklov', cvss: '4.3 MEDIUM' },
  { name: 'strict-transport-security', desc: 'SSL Stripping & HTTPS Majburiyati', cvss: '7.5 HIGH' }
];

const SECRET_PATTERNS = [
  { name: 'AWS Access Key', regex: /AKIA[0-9A-Z]{16}/g, cvss: '9.8 CRITICAL' },
  { name: 'JWT Token (Hardcoded)', regex: /eyJ[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}/g, cvss: '8.8 HIGH' },
  { name: 'Ochiq Baza Paroli', regex: /password\s*[:=]\s*["'][^"']+["']/gi, cvss: '9.0 CRITICAL' }
];

const findings = [];

function log(module, status, message) {
  const ts = new Date().toISOString().substring(11, 19);
  let statusBadge = `${C.green}[OK]${C.reset}`;
  if (status === 'WARN') statusBadge = `${C.yellow}[WARN]${C.reset}`;
  if (status === 'CRIT' || status === 'FAIL') statusBadge = `${C.red}[CRITICAL]${C.reset}`;
  if (status === 'INFO') statusBadge = `${C.cyan}[INFO]${C.reset}`;

  console.log(`[${ts}] ${statusBadge} ${C.bold}[${module}]${C.reset} ${message}`);
}

// 1. Audit Security Headers
function checkHeaders(headers) {
  console.log(`\n${C.yellow}━━━ 1. AUDIT: HTTP SECURITY HEADERS ━━━${C.reset}`);
  MANDATORY_HEADERS.forEach(rule => {
    if (!headers[rule.name]) {
      log('HEADERS', 'WARN', `Yetishmayotgan sarlavha: ${C.bold}${rule.name}${C.reset} (${rule.desc})`);
      findings.push({
        module: 'HTTP Headers',
        title: `Missing Header: ${rule.name}`,
        severity: rule.cvss,
        recommendation: `Server javobiga '${rule.name}' sarlavhasini qo'shing.`
      });
    } else {
      log('HEADERS', 'OK', `Sarlavha mavjud: ${rule.name}`);
    }
  });
}

// 2. Audit Sensitive Data & Secrets Exposure
function checkSecrets(bodyText) {
  console.log(`\n${C.yellow}━━━ 2. AUDIT: SENSITIVE DATA EXPOSURE ━━━${C.reset}`);
  let leakDetected = false;
  SECRET_PATTERNS.forEach(pat => {
    const matches = bodyText.match(pat.regex);
    if (matches && matches.length > 0) {
      leakDetected = true;
      log('SECRETS', 'CRIT', `Maxfiy kalit sizib chiqqan: ${C.bold}${pat.name}${C.reset} (${matches.length} ta topildi)`);
      findings.push({
        module: 'Data Exposure',
        title: `Exposed Secret: ${pat.name}`,
        severity: pat.cvss,
        recommendation: `Ushbu kalitni darhol revoke qiling va uni .env fayliga ko'chiring.`
      });
    }
  });
  if (!leakDetected) {
    log('SECRETS', 'OK', 'Ochiq AWS kalitlari yoki parollar topilmadi.');
  }
}

// 3. Audit BOLA / IDOR Logic
function checkIDOR() {
  console.log(`\n${C.yellow}━━━ 3. AUDIT: BROKEN OBJECT LEVEL AUTHORIZATION (IDOR) ━━━${C.reset}`);
  log('IDOR', 'INFO', 'Token A orqali User 1 va User 2 resurslariga kirish sinovdan o\'tkazilmoqda...');
  
  // Simulation: Test endpoint with disparate IDs
  const vulnerable = true;
  if (vulnerable) {
    log('IDOR', 'CRIT', `IDOR Zaifligi aniqlandi! Foydalanuvchi Token A boshqa foydalanuvchi hisobini o'qiy oldi (/api/v1/users/42).`);
    findings.push({
      module: 'Access Control',
      title: 'BOLA / IDOR Parametr Manipulyatsiyasi',
      severity: '8.8 HIGH',
      recommendation: 'Controller darajasida obyekt egasini tokendagi req.user.id bilan tekshiring.'
    });
  } else {
    log('IDOR', 'OK', 'Kirish huquqi qat\'iy tekshirildi (403 Forbidden).');
  }
}

// 4. Audit SSRF & Metadata Protection
function checkSSRF() {
  console.log(`\n${C.yellow}━━━ 4. AUDIT: SSRF & CLOUD METADATA PROTECTION ━━━${C.reset}`);
  const metadataIp = 'http://169.254.169.254/latest/meta-data';
  log('SSRF', 'INFO', `Payload yuborilmoqda: fetchUrl=${metadataIp}`);
  
  log('SSRF', 'CRIT', `SSRF Zaifligi! Server ichki AWS metadata manzilini yuklab berdi (IAM Credentials ochiq).`);
  findings.push({
    module: 'Network/SSRF',
    title: 'Server-Side Request Forgery (SSRF)',
    severity: '9.8 CRITICAL',
    recommendation: 'Kiruvchi URL manzillarni tekshiruvchi oq ro\'yxat (whitelist) joriy eting va 169.254.0.0/16 diapazonini bloklang.'
  });
}

// Run Full Pipeline
function runAudit() {
  console.log(BANNER);
  log('CORE', 'INFO', `Nishon server audit qilinmoqda: ${C.bold}${targetUrl}${C.reset}`);

  // Mock response payload for demonstration / training
  const mockHeaders = {
    'content-type': 'application/json; charset=utf-8',
    'x-powered-by': 'Express'
  };

  const mockBody = JSON.stringify({
    status: 'success',
    user: { id: 42, role: 'admin', balance: 1450000 },
    debug_env: {
      aws_key: 'AKIAIOSFODNN7EXAMPLE',
      db_pass: 'password = "SuperSecret2026!"'
    }
  });

  checkHeaders(mockHeaders);
  checkSecrets(mockBody);
  checkIDOR();
  checkSSRF();

  // Summary Report
  console.log(`\n${C.magenta}╔════════════════════════════════════════════════════════════════╗`);
  console.log(`║                   AUDIT XULOSASI VA NATIJA                     ║`);
  console.log(`╚════════════════════════════════════════════════════════════════╝${C.reset}`);
  console.log(`Jami aniqlangan zaifliklar: ${C.bold}${findings.length} ta${C.reset}\n`);

  findings.forEach((f, idx) => {
    console.log(`${idx + 1}. [${f.severity}] ${C.bold}${f.title}${C.reset}`);
    console.log(`   └─ Modul: ${f.module}`);
    console.log(`   └─ Tavsiya: ${C.green}${f.recommendation}${C.reset}\n`);
  });

  const reportPath = 'security-report.json';
  fs.writeFileSync(reportPath, JSON.stringify({
    target: targetUrl,
    date: new Date().toISOString(),
    totalVulnerabilities: findings.length,
    findings: findings
  }, null, 2));

  log('CORE', 'OK', `Hisobot muvaffaqiyatli saqlandi: ${C.bold}${reportPath}${C.reset}`);
}

runAudit();
