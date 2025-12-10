// watcher.js - Windows-Optimized Version
const { Client, LocalAuth } = require('whatsapp-web.js');
const qrcode = require('qrcode-terminal');
const { execFile } = require('child_process');
const fs = require('fs');
const path = require('path');

const TARGET_GROUP_NAME = "";  // Change to your group name
const PYTHON_JOINER = path.join(__dirname, "join_meet.py");
const LAST_LINK_FILE = path.join(__dirname, "last_link.txt");

const client = new Client({
  authStrategy: new LocalAuth(),
  puppeteer: { headless: true }
});

client.on('qr', qr => {
  qrcode.generate(qr, { small: true });
  console.log("Scan the QR code above with your phone");
});

client.on('ready', () => {
  console.log('WhatsApp bot is READY and watching the group:', TARGET_GROUP_NAME);
});

function readLastLink() {
  try {
    return fs.readFileSync(LAST_LINK_FILE, 'utf8').trim();
  } catch (e) {
    return "";
  }
}

function writeLastLink(link) {
  fs.writeFileSync(LAST_LINK_FILE, link, 'utf8');
}

function extractMeetCode(text) {
  if (!text) return null;

  const lower = text.toLowerCase();

  // 1. meet.google.com/abc-def-ghi (with or without https://)
  let match = lower.match(/meet\.google\.com\/([a-z0-9-]{8,})/);
  if (match) return match[1];

  // 2. g.co/meet/name
  match = lower.match(/g\.co\/meet\/([a-z0-9-]+)/);
  if (match) return match[1];

  // 3. Raw code like abc-def-ghi (most common!)
  const codes = lower.match(/\b([a-z0-9]{3,4}-[a-z0-9]{3,4}-[a-z0-9]{3,4})\b/g);
  if (codes && codes.length > 0) {
    return codes[codes.length - 1];
  }

  return null;
}

client.on('message_create', async (msg) => {
  try {
    const chat = await msg.getChat();

    if (!chat.isGroup || chat.name !== TARGET_GROUP_NAME) return;

    const body = msg.body || "";
    const code = extractMeetCode(body);

    if (!code) return;

    const fullUrl = `https://meet.google.com/${code}`;
    const last = readLastLink();

    if (fullUrl === last) {
      console.log("Duplicate link, ignoring:", code);
      return;
    }

    console.log("NEW MEET LINK →", code);
    writeLastLink(fullUrl);

    // Windows: Use "python" (not "python3")
    execFile("python", [PYTHON_JOINER, code], (error, stdout, stderr) => {
      if (error) {
        console.error("Failed to run join_meet.py:", error.message);
        if (stderr) console.error("Python stderr:", stderr);
        return;
      }
      console.log("Auto-join attempted!");
      if (stdout.trim()) console.log(stdout.trim());
    });

  } catch (err) {
    console.error("Error processing message:", err);
  }
});

client.initialize();