from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QWidget


class RegLogWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.setObjectName("Form")
        self.resize(270, 151)
        self.setStyleSheet(
            "background-color: qlineargradient(spread:reflect, x1:0.549682, y1:0.494, x2:0, y2:0, stop:0 rgba(0, 18, 221, 216), stop:1 rgba(179, 0, 241, 216));\n"
            "font: 10pt \"Bahnschrift SemiLight\";\n"
            "")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(parent=self)
        self.frame.setStyleSheet("background-color: rgba(255, 255, 255, 30);\n"
                                 "border: 1px solid rgba(255, 255, 255, 40);\n"
                                 "border-radius: 7px;")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.regButton = QtWidgets.QPushButton(parent=self.frame)
        self.regButton.setMinimumSize(QtCore.QSize(0, 40))
        self.regButton.setStyleSheet("QPushButton {\n"
                                     "font: 11pt \"MS Shell Dlg 2\";\n"
                                     "color: rgb(255, 255, 255);\n"
                                     "background-color: rgba(255, 255, 255, 40);\n"
                                     "border: 1px solid rgba(255, 255, 255, 60);\n"
                                     "border-radius: 7px;\n"
                                     "width: 230px;\n"
                                     "height: 30px;\n"
                                     "}\n"
                                     "QPushButton:hover{\n"
                                     "background-color: rgba(255, 255, 255, 60);\n"
                                     "}\n"
                                     "\n"
                                     "QPushButton:pressed{\n"
                                     "background-color: rgba(255, 255, 255, 80);\n"
                                     "}")
        self.regButton.setObjectName("regButton")
        self.verticalLayout.addWidget(self.regButton)
        self.logButton = QtWidgets.QPushButton(parent=self.frame)
        self.logButton.setMinimumSize(QtCore.QSize(0, 40))
        self.logButton.setStyleSheet("QPushButton {\n"
                                     "font: 11pt \"MS Shell Dlg 2\";\n"
                                     "color: rgb(255, 255, 255);\n"
                                     "background-color: rgba(255, 255, 255, 40);\n"
                                     "border: 1px solid rgba(255, 255, 255, 60);\n"
                                     "border-radius: 7px;\n"
                                     "width: 230px;\n"
                                     "height: 30px;\n"
                                     "}\n"
                                     "QPushButton:hover{\n"
                                     "background-color: rgba(255, 255, 255, 60);\n"
                                     "}\n"
                                     "\n"
                                     "QPushButton:pressed{\n"
                                     "background-color: rgba(255, 255, 255, 80);\n"
                                     "}")
        self.logButton.setObjectName("logButton")
        self.verticalLayout.addWidget(self.logButton)
        self.logButton.raise_()
        self.regButton.raise_()
        self.horizontalLayout.addWidget(self.frame)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "WalletWise: Family Finance Tracker"))
        self.regButton.setText(_translate("Form", "Зарегестрироваться"))
        self.logButton.setText(_translate("Form", "Войти"))
        self.regButton.clicked.connect(self.open_reg)
        self.logButton.clicked.connect(self.open_log)

    def open_reg(self):
        from RegWindow import RegWindow
        self.close()
        self.dlg = RegWindow()
        self.dlg.show()

    def open_log(self):
        from AuthWindow import AuthWindow
        self.close()
        self.dlg = AuthWindow()
        self.dlg.show()
