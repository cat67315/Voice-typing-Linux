#!/usr/bin/env python3

# It is recommend to bind this script to a keybind (I recommend Host+H).
# If you have any other hotkeys binded to the hotkey you choose, unbind them or set them to a different hotkey.
# Lookup how to set custom keybinds for your linux distro. 

# Import pre modules
import os
import json5

# Load and apply config
with open("config.json5", "r", encoding="utf-8") as f:
    config = json5.load(f)

# Note: in the future, make the config checks hapen on the exicuting line of code, not here. 
force_dark_mode = config["Force dark mode"]
force_light_mode = config["Force light mode"]
window_width = config["Window width"]
window_height = config["Window height"]
background_color_dark = config["Background color dark mode"]
background_color_light = config["Background color light mode"]
button_border_color_dark = config["Button Border color dark mode"]
button_border_color_light = config["Button Border color light mode"]
button_border_thickness = config["Button Border thickness"]
window_movable = config["Window movable"]

if config["Force X11 backend"]:
    os.environ["QT_QPA_PLATFORM"] = "xcb"
    print("Forcing X11 backend for QT")

# Import rest of modules
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from linuxosinfo import is_dark_mode # This module does not work on some desktops. If it dosint work for you go into config.json5 and turn Force dark mode to true
import subprocess

is_dark_mode_real = is_dark_mode() # I know, realy jank

if force_dark_mode:
    is_dark_mode_real = True
elif force_light_mode:
    is_dark_mode_real = False

session_type = (
    "Wayland" if os.getenv("WAYLAND_DISPLAY") and config["Force X11 backend"] == False else
    "X11"     if os.getenv("DISPLAY") else
    "unknown"
)
print(f"Session type: {session_type}")

class DraggableWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Voice Typing Linux GUI")
        if session_type == "Wayland":
            self.setWindowFlags(Qt.WindowStaysOnTopHint) # Always on top (Dragging is broken with wayland so we have the title bar on wayland)
        else:
            self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint) # Always on top and no tile bar
        self.setFixedSize(window_width, window_height)  # non-resizable
        if is_dark_mode_real:
            self.setStyleSheet(f"background-color: {background_color_dark}; border: 2px solid {button_border_color_dark}; border-radius: {button_border_thickness}px;")
        else:
            self.setStyleSheet(f"background-color: {background_color_light}; border: 2px solid {button_border_color_light}; border-radius: {button_border_thickness}px;")
        layout = QVBoxLayout()
        self.button = QPushButton()
        if is_dark_mode_real:
            self.button.setIcon(QIcon("assets/mic_icon_white.png")) # Note: In the future, use SVG icons so they scale better
        else:
            self.button.setIcon(QIcon("assets/mic_icon_black.png")) # Note: In the future, use SVG icons so they scale better
        self.button.setStyleSheet("QPushButton { padding: 10px; font-size: 16px; }")
        self.button.clicked.connect(self.run_script)
        layout.addWidget(self.button)
        self.setLayout(layout)

        self.old_pos = None

    def run_script(self):
        # Get absolute path to the workspace root
        script_dir = os.path.dirname(os.path.abspath(__file__))

        if config["Use punctuation model"]:
            vosk_model_path = os.path.join(script_dir, "Vosk", "Punctuation models")
        else:
            vosk_model_path = os.path.join(script_dir, "Vosk", "vosk-model-en-us-0.22")
        
        os.environ["vosk_model_dir"] = vosk_model_path
        print(os.path.join(script_dir, "Vosk", "vosk-model-en-us-0.22") + "ruhrggfjnfgfhtrefgtjrfvguyrhfjdvihuytjrfkoiguhty") # Temp line
        subprocess.run(["./nerd-dictation", "begin"], cwd=os.path.join(script_dir, "nerd-dictation"))

    if window_movable and session_type != "Wayland":
        # Mouse events for dragging
        def mousePressEvent(self, event):
            if event.button() == Qt.LeftButton:
                self.old_pos = event.globalPosition().toPoint()

        def mouseMoveEvent(self, event):
            if self.old_pos is not None:
                delta = event.globalPosition().toPoint() - self.old_pos
                self.move(self.x() + delta.x(), self.y() + delta.y())
                self.old_pos = event.globalPosition().toPoint()

        def mouseReleaseEvent(self, event):
            self.old_pos = None


app = QApplication([])
window = DraggableWindow()
window.show()
app.exec()