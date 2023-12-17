from pathlib import Path
from PyQt6.QtWidgets import QApplication
from StartWindow import StartWindow

if __name__ == "__main__":
    app = QApplication([])

    app.setStyleSheet(Path('style.css').read_text())

    start_win = StartWindow()
    start_win.show()

    app.exec()