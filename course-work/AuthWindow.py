from PyQt6 import QtCore, QtGui, QtWidgets
from database import DatabaseManager
from PyQt6.QtWidgets import QWidget

class AuthWindow(QWidget):
    def __init__(self):
        super(AuthWindow, self).__init__()
        self.setupUi(self)
        self.db_manager = DatabaseManager('budget.db')

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(274, 247)
        Form.setStyleSheet(
            "background-color: qlineargradient(spread:reflect, x1:0.549682, y1:0.494, x2:0, y2:0, stop:0 rgba(0, 18, 221, 216), stop:1 rgba(179, 0, 241, 216));\n"
            "font: 10pt \"Bahnschrift SemiLight\";\n"
            "")
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(parent=Form)
        self.frame.setStyleSheet("background-color:none;\n"
                                 "border: none;\n"
                                 "border-radius: 7px;")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(parent=self.frame)
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
                                 "font: 75 22pt \"MS Shell Dlg 2\";\n"
                                 "background-color: none;\n"
                                 "border: none;\n"
                                 "padding-bottom: 10px;")
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.verticalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(parent=Form)
        self.frame_2.setStyleSheet("background-color: rgba(255, 255, 255, 30);\n"
                                   "border: 1px solid rgba(255, 255, 255, 40);\n"
                                   "border-radius: 7px;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.logLine = QtWidgets.QLineEdit(parent=self.frame_2)
        self.logLine.setStyleSheet("font-size: 16pt;\n"
                                   "color:rgb(255, 255, 255);\n"
                                   "padding-left: 10px;")
        self.logLine.setObjectName("logLine")
        self.verticalLayout_3.addWidget(self.logLine)
        self.passLine = QtWidgets.QLineEdit(parent=self.frame_2)
        self.passLine.setStyleSheet("font-size: 16pt;\n"
                                    "color:rgb(255, 255, 255);\n"
                                    "padding-left: 10px;")
        self.passLine.setObjectName("passLine")
        self.verticalLayout_3.addWidget(self.passLine)
        self.forgotButton = QtWidgets.QPushButton(parent=self.frame_2)
        self.forgotButton.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.forgotButton.setStyleSheet("QPushButton {\n"
                                        "background-color: rgba(255, 255, 255, 0);\n"
                                        "font: 10pt \"MS Shell Dlg 2\";\n"
                                        "text-decoration: underline;\n"
                                        "color: rgb(106, 255, 171);\n"
                                        "border: none;\n"
                                        "border-radius: 7px;\n"
                                        "width: 230px;\n"
                                        "height: 30px;\n"
                                        "}\n"
                                        "QPushButton:hover{\n"
                                        "color: rgb(98, 235, 158);\n"
                                        "background-color: rgba(255, 255, 255, 20);\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:pressed{\n"
                                        "color: rgba(98, 235, 158, 100);\n"
                                        "}")
        self.forgotButton.setObjectName("forgotButton")
        self.verticalLayout_3.addWidget(self.forgotButton)
        self.verticalLayout.addWidget(self.frame_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.backButton = QtWidgets.QPushButton(parent=Form)
        self.backButton.setMaximumSize(QtCore.QSize(120, 120))
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
        self.nextButton = QtWidgets.QPushButton(parent=Form)
        self.nextButton.setMaximumSize(QtCore.QSize(120, 16777215))
        self.nextButton.setStyleSheet("QPushButton {\n"
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
        self.nextButton.setObjectName("nextButton")
        self.horizontalLayout.addWidget(self.nextButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Авторизация"))
        self.logLine.setPlaceholderText(_translate("Form", "Введите имя (логин)"))
        self.passLine.setPlaceholderText(_translate("Form", "Введите пароль"))
        self.forgotButton.setText(_translate("Form", "Забыли пароль?"))
        self.backButton.setText(_translate("Form", "Назад"))
        self.nextButton.setText(_translate("Form", "Далее"))

        self.nextButton.clicked.connect(self.open_main)
        self.forgotButton.clicked.connect(self.open_fpw)
        self.backButton.clicked.connect(self.reg_or_log_sh)

    def open_main(self):
        if not self.validate_fields():
            return

        from message_box import MessageBox
        from MainWindow import MainWindow
        login_input = self.logLine.text()
        password_input = self.passLine.text()

        auth = self.db_manager.check_credentials(login_input, password_input)

        # Проверка учетных данных в базе данных
        if auth:
            # Открываем главное окно
            if not self.db_manager.check_familly(auth[0]):
                from NewBankAcc import BankAccWin
                self.bank_acc_dialog = BankAccWin(auth[0], is_registration=False)
                self.bank_acc_dialog.show()
            else:
                self.main_win = MainWindow(auth[0])
                self.main_win.show()

            self.close()
        else:
            error_msg = MessageBox(self)
            error_msg.show_message("Ошибка", "Неправильный логин или пароль", MessageBox.Icon.Critical)

    def validate_fields(self):
        from message_box import MessageBox
        login_input = self.logLine.text()
        password_input = self.passLine.text()

        if not login_input or not password_input:
            warn_msg = MessageBox(self)
            warn_msg.show_message("Осторожно", "Пожалуйста, заполните все поля.", MessageBox.Icon.Warning)
            return False
        return True

    def open_fpw(self):
        from AskLogWindow import AskLogWindow
        self.close()
        self.ask_log = AskLogWindow()
        self.ask_log.show()

    def reg_or_log_sh(self):
        from RegOrLog import RegLogWindow
        self.reg_or_log = RegLogWindow()
        self.reg_or_log.show()
        self.close()