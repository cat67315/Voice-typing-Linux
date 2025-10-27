##!/usr/bin/env python3

import keyboard
import subprocess
import threading

keybind = "ctrl+alt+h"

def on_hotkey():
    print("Hotkey presed")
    subprocess.run(["python3", "main.py", "&"])

keyboard.add_hotkey(keybind, on_hotkey)

threading.Event().wait()