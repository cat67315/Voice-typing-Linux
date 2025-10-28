##!/usr/bin/env python3

from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
import subprocess, sys

class DraggableWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My GUI")
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setFixedSize(100, 50)  # non-resizable
        self.setStyleSheet("background-color: #2e2e2e; border: 2px solid #555; border-radius: 10px;")

        layout = QVBoxLayout()
        self.button = QPushButton()
        self.button.setIcon(QIcon("assets/mic_icon.png"))
        self.button.setStyleSheet("QPushButton { padding: 10px; font-size: 16px; }")
        self.button.clicked.connect(self.run_script)
        layout.addWidget(self.button)
        self.setLayout(layout)

        self.old_pos = None

    def run_script(self):
        subprocess.Popen([sys.executable, "yourscript.py"])

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
