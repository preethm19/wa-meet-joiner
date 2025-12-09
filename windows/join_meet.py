#!/usr/bin/env python3
"""
join_meet.py - Windows Version: Manual Open Only (December 2025)
Opens URL in existing Chrome (new tab, no new/guest window).
No auto-click — manual join after open.

Requirements: None (uses built-in subprocess).
"""

import sys
import time
import re
import subprocess

def extract_meet_code(text):
    text = str(text).strip().lower()
    m = re.search(r'meet\.google\.com[/:]([a-z0-9-]{8,})', text)
    if m: return m.group(1)
    m = re.search(r'g\.co/meet/([a-z0-9-]+)', text)
    if m: return m.group(1)
    codes = re.findall(r'\b([a-z0-9]{3,4}-[a-z0-9]{3,4}-[a-z0-9]{3,4})\b', text)
    if codes: return codes[-1]
    return None

if len(sys.argv) < 2:
    print("Usage: python join_meet.py <meet link or code>")
    sys.exit(1)

input_text = " ".join(sys.argv[1:])
code = extract_meet_code(input_text)
if not code:
    print("No Google Meet code found.")
    sys.exit(1)

url = f"https://meet.google.com/{code}"
print(f"Opening -> {url}...")

# Open in existing Chrome
subprocess.run(["start", "chrome", url], shell=True)
print("Open complete, enjoy the meeting!")

print("Done! Check Chrome.")