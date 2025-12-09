# WhatsApp Google Meet Auto-Joiner for Windows

This tool monitors a specific WhatsApp group for Google Meet links or codes. When detected, it opens the meeting in your existing Chrome browser (new tab) and automatically clicks "Ask to join" for instant joining. Ignores duplicates to avoid re-joining.
 
### Features
 * **Smart Link Detection:** Works with full URLs (`https://meet.google.com/abc-defg-hij`), partial links (`meet.google.com/abc-defg-hij`), or just the meeting code (`abc-defg-hij`).
  * **Auto-Normalization:** Automatically repairs missing protocols (adds `https://`) to ensure the browser opens correctly.

* **How it Works**: Configure via extension icon in Meet; free core features, pro for Workspace users.  
This complements the script — use the extension for advanced Meet controls while the bot handles link detection/opening.

* **Supported Formats**: Full URL (`https://meet.google.com/ege-gdsf-zto`), short (`meet.google.com/ege-gdsf-zto`), raw code (`ege-gdsf-zto`), or embedded in text.
* **Platform**: Windows 10/11 (tested on Dec 2025 Chrome v136+).
* **Tech**: Node.js for WhatsApp, Python + Selenium for Chrome automation.
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
   cd wa-meet-joiner
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

5. **Add Chrome Extension (For Auto-join):**<br>
    [Google Meet Enhancement Suite](https://chromewebstore.google.com/detail/google-meet-enhancement-s/ljojmlmdapmnibgflmmminacbjebjpno)
    
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
- **QR Scan Fails**: Restart `node watcher.js`.
- **Deps Error**: Run `npm install` or `pip install` again.
- **Extension Issues**: Check Chrome Web Store for updates.

### Happy auto-joining! 🚀 