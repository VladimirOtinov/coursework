from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QWidget
from database import DatabaseManager

class AskLogWindow(QWidget):
    def __init__(self):
        super(AskLogWindow, self).__init__()
        self.db_manager = DatabaseManager("budget.db")
        self.setupUi(self)
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(350, 152)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(350, 0))
        Form.setStyleSheet("background-color: qlineargradient(spread:reflect, x1:0.549682, y1:0.494, x2:0, y2:0, stop:0 rgba(0, 18, 221, 216), stop:1 rgba(179, 0, 241, 216));\n"
"font: 10pt \"Bahnschrift SemiLight\";\n"
"")
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(parent=Form)
        self.frame.setMinimumSize(QtCore.QSize(0, 0))
        self.frame.setStyleSheet("background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;\n"
"color: rgb(255, 255, 255);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.askLogin = QtWidgets.QLabel(parent=self.frame)
        self.askLogin.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 24pt \"MS Shell Dlg 2\";\n"
"background-color: none;\n"
"border: none;\n"
"")
        self.askLogin.setObjectName("askLogin")
        self.verticalLayout_2.addWidget(self.askLogin)
        self.loginLine = QtWidgets.QLineEdit(parent=self.frame)
        self.loginLine.setMinimumSize(QtCore.QSize(0, 0))
        self.loginLine.setStyleSheet("font-size: 16pt;\n"
"color:rgb(255, 255, 255);\n"
"padding-left: 10px;")
        self.loginLine.setObjectName("loginLine")
        self.verticalLayout_2.addWidget(self.loginLine)
        self.verticalLayout.addWidget(self.frame)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.backButton = QtWidgets.QPushButton(parent=Form)
        self.backButton.setMinimumSize(QtCore.QSize(1, 0))
        self.backButton.setMaximumSize(QtCore.QSize(200, 16777215))
        self.backButton.setStyleSheet("QPushButton {\n"
"font: 11pt \"MS Shell Dlg 2\";\n"
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
        self.confirmButton = QtWidgets.QPushButton(parent=Form)
        self.confirmButton.setMinimumSize(QtCore.QSize(1, 0))
        self.confirmButton.setMaximumSize(QtCore.QSize(200, 16777215))
        self.confirmButton.setStyleSheet("QPushButton {\n"
"font: 11pt \"MS Shell Dlg 2\";\n"
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
        self.confirmButton.setObjectName("confirmButton")
        self.horizontalLayout.addWidget(self.confirmButton)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Form)
        self.confirmButton.clicked.connect(self.checkLogin)
        self.backButton.clicked.connect(self.open_log)

        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.askLogin.setText(_translate("Form", "Введите ваш логин"))
        self.loginLine.setPlaceholderText(_translate("Form", "Введите ваш семейный логин"))
        self.backButton.setText(_translate("Form", "Назад"))
        self.confirmButton.setText(_translate("Form", "Подтвердить"))

    def checkLogin(self):
        from NewPassword import NewPassword
        from message_box import MessageBox
        login = self.loginLine.text().strip()
        if login:
            family_id = self.db_manager.get_user_id_by_login(login)
            if family_id:
                print(f"family_id: {family_id}")
                self.close()
                self.new_password_window = NewPassword(family_id)
                self.new_password_window.show()

            else:
                error_msg = MessageBox(self)
                error_msg.show_message("Ошибка", "Пользователь с таким логином не найден.", MessageBox.Icon.Error)
        else:
            warn_msg = MessageBox(self)
            warn_msg.show_message("Ошибка", "Введите логин семьи.", MessageBox.Icon.Warning)

    def open_log(self):
        from AuthWindow import AuthWindow
        self.close()
        self.dlg = AuthWindow()
        self.dlg.show()
