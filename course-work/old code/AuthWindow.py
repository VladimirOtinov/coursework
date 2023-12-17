from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QDialog, QApplication, QMessageBox
from database import DatabaseManager


class AuthDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.db_manager = DatabaseManager("budget.db")

        # Устанавливаем размеры и стили диалогового окна
        self.setObjectName("authDialog")
        self.resize(326, 215)
        self.setStyleSheet("background-color: qlineargradient(spread:reflect, x1:0.549682, y1:0.494, x2:0, y2:0, stop:0 rgba(0, 18, 221, 216), stop:1 rgba(179, 0, 241, 216));\n"
                           "font: 10pt \"Bahnschrift SemiLight\";\n"
                           "")

        # Создаем вертикальный layout
        self.verticalLayout = QtWidgets.QVBoxLayout(self)

        # Создаем фрейм для заголовка
        self.frame = QtWidgets.QFrame(self)
        self.frame.setStyleSheet("background-color:none;\n"
                                "border: none;\n"
                                "border-radius: 7px;")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)

        # Вложенный вертикальный layout в фрейме
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)

        # Создаем метку для заголовка
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
                                "font: 75 22pt \"MS Shell Dlg 2\";\n"
                                "background-color: none;\n"
                                "border: none;\n"
                                "padding-bottom: 10px;")
        self.verticalLayout_2.addWidget(self.label)

        # Добавляем фрейм в основной layout
        self.verticalLayout.addWidget(self.frame)

        # Создаем фрейм для ввода логина и пароля
        self.frame_2 = QtWidgets.QFrame(self)
        self.frame_2.setStyleSheet("background-color: rgba(255, 255, 255, 30);\n"
                                  "border: 1px solid rgba(255, 255, 255, 40);\n"
                                  "border-radius: 7px;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)

        # Вложенный вертикальный layout во втором фрейме
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_2)

        # Создаем поле для ввода логина
        self.logLine = QtWidgets.QLineEdit(self.frame_2)
        self.logLine.setStyleSheet("font-size: 16pt;\n"
                                   "color:rgb(255, 255, 255);\n"
                                   "padding-left: 10px;")
        self.verticalLayout_3.addWidget(self.logLine)

        # Создаем поле для ввода пароля
        self.passLine = QtWidgets.QLineEdit(self.frame_2)
        self.passLine.setStyleSheet("font-size: 16pt;\n"
                                    "color:rgb(255, 255, 255);\n"
                                    "padding-left: 10px;")
        self.verticalLayout_3.addWidget(self.passLine)

        # Добавляем второй фрейм в основной layout
        self.verticalLayout.addWidget(self.frame_2)

        # Создаем горизонтальный layout для кнопок
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        # Создаем кнопку для восстановления пароля
        self.forgotButton = QtWidgets.QPushButton(self)
        self.forgotButton.setMaximumSize(QtCore.QSize(150, 16777215))
        self.forgotButton.setStyleSheet("QPushButton {\n"
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
        self.forgotButton.setObjectName("forgotButton")

        # Создаем кнопку для авторизации
        self.nextButton = QtWidgets.QPushButton(self)
        self.nextButton.setMaximumSize(QtCore.QSize(150, 16777215))
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

        # Добавляем кнопки в горизонтальный layout
        self.horizontalLayout_2.addWidget(self.forgotButton)
        self.horizontalLayout_2.addWidget(self.nextButton)

        # Добавляем горизонтальный layout в основной layout
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        # Вызываем метод для перевода строк на нужный язык
        self.retranslateUi()

    def retranslateUi(self):
        # Получаем объект для перевода строк
        _translate = QtCore.QCoreApplication.translate

        # Устанавливаем текст заголовка окна
        self.setWindowTitle(_translate("authDialog", "WalletWise: Family Finance Tracker"))

        # Устанавливаем текст метки для заголовка
        self.label.setText(_translate("authDialog", "Авторизация"))

        # Устанавливаем текст подсказок для полей ввода
        self.logLine.setPlaceholderText(_translate("authDialog", "Введите логин"))
        self.passLine.setPlaceholderText(_translate("authDialog", "Введите пароль"))

        # Устанавливаем текст кнопки для восстановления пароля
        self.forgotButton.setText(_translate("authDialog", "Забыли пароль?"))

        # Устанавливаем текст кнопки для авторизации
        self.nextButton.setText(_translate("authDialog", "Далее"))

        self.nextButton.clicked.connect(self.open_main)
        self.forgotButton.clicked.connect(self.open_fpw)

    def open_main(self):
        from message_box import MessageBox
        from MainWindow import MyMainWindow
        login_input = self.logLine.text()
        password_input = self.passLine.text()

        # Проверка учетных данных в базе данных
        if self.db_manager.check_credentials(login_input, password_input):
            # Открываем главное окно
            self.main_win = MyMainWindow()
            self.main_win.show()

            # Закрываем соединение с базой данных после открытия главного окна


            # Закрываем окно авторизации
            self.close()
        else:
            # Отображение сообщения об ошибке
            error_msg = MessageBox(self)
            error_msg.show_message("Ошибка", "Неправильный логин или пароль", MessageBox.Icon.Critical)



    def open_fpw(self):
        from ChangePassword import ForgotPassDialog
        self.close()
        self.dlg = ForgotPassDialog()
        self.dlg.open()