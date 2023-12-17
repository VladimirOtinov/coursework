from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QDialog
from database import DatabaseManager  # Импортируйте ваш класс DatabaseManager


class ForgotPassDialog(QDialog):
    def __init__(self):
        super().__init__()

        # Создаем элементы интерфейса
        self.db_manager = DatabaseManager("budget.db")
        self.setupUi(self)

    def setupUi(self, forgotPassDialog):
        forgotPassDialog.setObjectName("forgotPassDialog")
        forgotPassDialog.resize(510, 361)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(forgotPassDialog.sizePolicy().hasHeightForWidth())
        forgotPassDialog.setSizePolicy(sizePolicy)
        forgotPassDialog.setStyleSheet("background-color: qlineargradient(spread:reflect, x1:0.549682, y1:0.494, x2:0, y2:0, stop:0 rgba(0, 18, 221, 216), stop:1 rgba(179, 0, 241, 216));\n"
"font: 10pt \"Bahnschrift SemiLight\";\n"
"")
        self.verticalLayout = QtWidgets.QVBoxLayout(forgotPassDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(parent=forgotPassDialog)
        self.frame.setStyleSheet("background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(parent=self.frame)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 20pt \"MS Shell Dlg 2\";\n"
"background-color: none;\n"
"border: none;\n"
"font-weight: bold;\n"
"")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.frame_2 = QtWidgets.QFrame(parent=self.frame)
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(parent=self.frame_2)
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 18pt \"MS Shell Dlg 2\";\n"
"background-color: none;\n"
"border: none;")
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(parent=self.frame_2)
        self.lineEdit.setStyleSheet("font-size: 16pt;\n"
"color:rgb(255, 255, 255);\n"
"padding-left: 10px;")
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_3.addWidget(self.lineEdit)
        self.verticalLayout_2.addWidget(self.frame_2)
        self.frame_4 = QtWidgets.QFrame(parent=self.frame)
        self.frame_4.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_4 = QtWidgets.QLabel(parent=self.frame_4)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 18pt \"MS Shell Dlg 2\";\n"
"background-color: none;\n"
"border: none;")
        self.label_4.setObjectName("label_4")
        self.verticalLayout_5.addWidget(self.label_4)
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.frame_4)
        self.lineEdit_2.setStyleSheet("font-size: 16pt;\n"
"color:rgb(255, 255, 255);\n"
"padding-left: 10px;")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout_5.addWidget(self.lineEdit_2)
        self.lineEdit_3 = QtWidgets.QLineEdit(parent=self.frame_4)
        self.lineEdit_3.setStyleSheet("font-size: 16pt;\n"
"color:rgb(255, 255, 255);\n"
"padding-left: 10px;")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.verticalLayout_5.addWidget(self.lineEdit_3)
        self.verticalLayout_2.addWidget(self.frame_4)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.backButton = QtWidgets.QPushButton(parent=self.frame)
        self.backButton.setStyleSheet("QPushButton {\n"
"font: 75 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 50);\n"
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
        self.backButton.setObjectName("backButton")
        self.horizontalLayout.addWidget(self.backButton)
        self.saveButton = QtWidgets.QPushButton(parent=self.frame)
        self.saveButton.setStyleSheet("QPushButton {\n"
"font: 75 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 50);\n"
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
        self.saveButton.setObjectName("saveButton")
        self.horizontalLayout.addWidget(self.saveButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout.addWidget(self.frame)

        self.retranslateUi(forgotPassDialog)
        QtCore.QMetaObject.connectSlotsByName(forgotPassDialog)

    def retranslateUi(self, forgotPassDialog):
        _translate = QtCore.QCoreApplication.translate
        forgotPassDialog.setWindowTitle(_translate("forgotPassDialog", "WalletWise: Family Finance Tracker"))
        self.label_2.setText(_translate("forgotPassDialog", "Восстановление пароля"))
        self.label.setText(_translate("forgotPassDialog", "вопрос"))
        self.lineEdit.setPlaceholderText(_translate("forgotPassDialog", "Ответ на вопрос"))
        self.label_4.setText(_translate("forgotPassDialog", "Изменение пароля"))
        self.lineEdit_2.setPlaceholderText(_translate("forgotPassDialog", "Введите новый пароль"))
        self.lineEdit_3.setPlaceholderText(_translate("forgotPassDialog", "Повторите новый пароль"))
        self.backButton.setText(_translate("forgotPassDialog", "Назад"))
        self.saveButton.setText(_translate("forgotPassDialog", "Сохранить"))
        self.backButton.clicked.connect(self.back_win)
        self.saveButton.clicked.connect(self.save_password)

    def back_win(self):
        from AuthWindow import AuthDialog
        self.close()
        self.dlg = AuthDialog()
        self.dlg.exec()

    def save_password(self):
        from AuthWindow import AuthDialog
        self.close()
        self.dlg = AuthDialog()
        self.dlg.exec()