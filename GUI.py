##!/usr/bin/env python3

# It is recomended to bind this script to a keybind (I recommend Host+H).
# If you have any other hotkeys binded to the hotkey you choose, unbind them or set them to a different hotkey.
# Lookup how to set custom keybinds for your linux distro.

from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from linuxosinfo import is_dark_mode, os_color
import subprocess, sys
import json5

# Load and apply config
with open("config.json5", "r", encoding="utf-8") as f:
    config = json5.load(f)

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

is_dark_mode_real = is_dark_mode()


if force_dark_mode:
    is_dark_mode_real = True
elif force_light_mode:
    is_dark_mode_real = False


class DraggableWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Voice Typing Linux GUI")
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint) # Always on top and no title bar
        self.setFixedSize(window_width, window_height)  # non-resizable
        if is_dark_mode_real:
            self.setStyleSheet(f"background-color: {background_color_dark}; border: 2px solid {button_border_color_dark}; border-radius: {button_border_thickness}px;")
        else:
            self.setStyleSheet(f"background-color: {background_color_light}; border: 2px solid {button_border_color_light}; border-radius: {button_border_thickness}px;")
        layout = QVBoxLayout()
        self.button = QPushButton()
        if is_dark_mode_real:
            self.button.setIcon(QIcon("assets/mic_icon_white.png"))
        else:
            self.button.setIcon(QIcon("assets/mic_icon_black.png"))
        self.button.setStyleSheet("QPushButton { padding: 10px; font-size: 16px; }")
        self.button.clicked.connect(self.run_script)
        layout.addWidget(self.button)
        self.setLayout(layout)

        self.old_pos = None

    def run_script(self):
        subprocess.Popen([sys.executable, "yourscript.py"])

    if window_movable:
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