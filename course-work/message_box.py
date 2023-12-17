from PyQt6.QtWidgets import QMessageBox, QPushButton, QLabel


class MessageBox(QMessageBox):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setStyleSheet("QPushButton{font: 75 12pt \"MS Shell Dlg 2\"; color: rgb(255, 255, 255); "
                           "background-color: rgba(255, 255, 255, 50); border: 1px solid rgba(255, 255, 255, 60); "
                           "border-radius:7px; width: 230; height: 30; }"
                           "QPushButton:hover{background-color: rgba(255, 255, 255, 70);}"
                           "QPushButton:pressed{background-color: rgba(255, 255, 255, 90);}"
                           "QLabel{color: rgb(255, 255, 255); font: 75 12pt \"MS Shell Dlg 2\"; background-color: none; "
                           "border: none; font-weight: bold;}")

    def show_message(self, title, text, icon):
        self.setWindowTitle(title)
        self.setText(text)
        self.setIcon(icon)
        self.exec()
