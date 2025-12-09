#!/usr/bin/env python3
"""
join_meet.py - THE ONE THAT ACTUALLY WORKS
Auto-opens + clicks "Ask to join" using Google's real class name (Dec 2025)
Works with: yeu-nrdt-sve | meet.google.com/abc-def-ghi | full URL
"""

import sys
import sys
import subprocess
import time
import re

def extract_meet_code(text):
    text = str(text).strip()
    # Case 1: Full URL
    m = re.search(r'meet\.google\.com[/:]([a-z0-9-]{8,})', text, re.I)
    if m: return m.group(1)
    # Case 2: g.co/meet
    m = re.search(r'g\.co/meet/([a-z0-9-]+)', text, re.I)
    if m: return m.group(1)
    # Case 3: Raw code anywhere (most common in WhatsApp)
    codes = re.findall(r'\b([a-z0-9]{3,4}-[a-z0-9]{3,4}-[a-z0-9]{3,4})\b', text)
    if codes: return codes[-1]
    return None

# ============= MAIN =============
if len(sys.argv) < 2:
    print("Usage: python3 join_meet.py <meet link or code>")
    sys.exit(1)

input_text = " ".join(sys.argv[1:])
code = extract_meet_code(input_text)

if not code:
    print("No Google Meet code found in input.")
    sys.exit(1)

url = f"https://meet.google.com/{code}"
print(f"Opening → {url}")

# Open in Chrome
subprocess.run(["open", "-a", "Google Chrome", url], check=False)
time.sleep(4)  # Wait for page + consent screen

# ============ YOUR ORIGINAL PROVEN CLICKER (UPDATED FOR 2025) ============
applescript = '''
tell application "Google Chrome"
    activate
    delay 0.5
    tell active tab of window 1
        execute javascript "
            (function() {
                try {
                    // Current class as of December 2025 - this is the green 'Ask to join' button text
                    const CLASS_NAME = 'UywwFc-RLmnJb';
                    
                    let span = document.querySelector('span.' + CLASS_NAME);
                    if (!span) {
                        // Fallback: search all spans for partial class match
                        const all = document.querySelectorAll('span');
                        for (let s of all) {
                            if (s.className && s.className.toString().includes(CLASS_NAME)) {
                                span = s;
                                break;
                            }
                        }
                    }
                    if (!span) return 'SPAN_NOT_FOUND';

                    // Find closest clickable parent
                    let button = span.closest('div[role=button], button, [jscontroller]');
                    if (!button) button = span.parentElement;

                    // Get center coordinates
                    const rect = button.getBoundingClientRect();
                    const cx = Math.floor(rect.left + rect.width / 2);
                    const cy = Math.floor(rect.top + rect.height / 2);

                    // Ultra-realistic click sequence
                    const fire = (type) => {
                        const ev = new MouseEvent(type, {
                            view: window, bubbles: true, cancelable: true,
                            clientX: cx, clientY: cy, buttons: 1
                        });
                        button.dispatchEvent(ev);
                    };

                    ['pointerdown', 'mousedown', 'pointerup', 'mouseup', 'click'].forEach(fire);
                    button.click();

                    // Also try direct click on span
                    span.click();

                    return 'CLICKED_SUCCESSFULLY';
                } catch (e) {
                    return 'ERROR: ' + e.toString();
                }
            })();
        "
    end tell
end tell
'''

# Execute the click
result = subprocess.run(["osascript", "-e", applescript], capture_output=True, text=True)
output = result.stdout.strip()

print("Click result →", output)

if "CLICKED_SUCCESSFULLY" in output:
    print("Successfully clicked 'Ask to join'!")
elif "SPAN_NOT_FOUND" in output:
    print("Warning: Button class changed. Google updated UI. Open Meet, inspect the green button, find new class containing 'RLmnJb' or similar, and tell me.")
else:
    print("Click attempted. Check if you joined. If not, Google changed the class again.")