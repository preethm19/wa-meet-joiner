# WhatsApp-Google Meet Auto-Joiner for macOS

A Python automation script designed to streamline the process of joining Google Meet sessions on macOS. It parses various link formats, opens Google Chrome, and attempts to automatically click the "Ask to join" or "Join now" button.

### Features

  * **Smart Link Detection:** Works with full URLs (`https://meet.google.com/abc-defg-hij`), partial links (`meet.google.com/abc-defg-hij`), or just the meeting code (`abc-defg-hij`).
  * **Auto-Normalization:** Automatically repairs missing protocols (adds `https://`) to ensure the browser opens correctly.
  * **Click Automation:** Uses AppleScript and JavaScript to simulate realistic user clicks on the "Join" button.
  * **Status Detection:** Verifies if the join attempt was successful.
  * **Compatibility**: Chrome-only.

## Requirements
- **Node.js** (v18+ LTS): [Download](https://nodejs.org).
- **Python 3.8+**: [Download](https://python.org) (check "Add to PATH" during install).
- **Google Chrome** (latest): [Download](https://google.com/chrome).
- **Python Deps**: Selenium, webdriver-manager (install via pip).
- **Extension**: [Google Meet Enhancement Suite](https://chromewebstore.google.com/detail/google-meet-enhancement-s/ljojmlmdapmnibgflmmminacbjebjpno) for auto-join features.

## Installation
1. **Clone the repository**:
   ```
   git clone https://github.com/preethm19/wa-meet-joiner.git
   cd wa-meet-joiner/macOS
   ```

2. **Install requirements**:
    ```
    pip install -r requirements.txt
    ```

3. **Install Node.js Deps**:
   ```
   npm init -y
   npm install whatsapp-web.js qrcode-terminal
   ```

4. **Install Python Deps**:
   ```
   pip install selenium webdriver-manager
   ```

5. **Allow Apple Events:**<br>
    ```
    Chrome Profile  →  View  →  Developer  →  Allow JavaScript from Apple Events
    ```
    
5. **Run Watcher**:
   ```
   node watcher.js
   ```

## Customization
- **Group Name**: Edit `TARGET_GROUP_NAME = " ";` in watcher.js.


## Usage
1. **Run the Watcher**:
   ```node watcher.js```
   - First time: QR code prints — scan with phone WhatsApp (Settings > Linked Devices > Link Device).
   - Ready: "WhatsApp bot is READY and watching the group: TARGET_GROUP_NAME".

2. **Test**:
   - Send a Meet code/link (e.g., `ege-gdsf-zto`) to "TARGET_GROUP_NAME" group.
   - Script detects → Opens new tab in Chrome → Extension Auto-clicks "Ask to join" → Joined!

3. **Test Python Alone**:<br>
   ```python join_meet.py ege-gdsf-zto```

4. **Stop**: Ctrl+C in terminal.

## Troubleshooting

**If the script opens the page but fails to click "Join":**
1.  Inspect the Google Meet page source.
2.  Check if the class name for the join button has changed (currently targeting `UywwFc-RLmnJb`).

### Happy auto-joining! 🚀 