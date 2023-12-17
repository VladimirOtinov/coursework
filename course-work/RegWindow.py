from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QDialog, QMessageBox
from database import DatabaseManager

class RegDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.db_manager = DatabaseManager("budget.db")


        # Устанавливаем размеры и стили диалогового окна
        self.setObjectName("regDialog")
        self.resize(554, 452)
        self.setSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        self.setStyleSheet(
            "background-color: qlineargradient(spread:reflect, x1:0.549682, y1:0.494, x2:0, y2:0, stop:0 rgba(0, 18, 221, 216), stop:1 rgba(179, 0, 241, 216));\n"
            "font: 10pt \"Bahnschrift SemiLight\";\n"
            "")

        # Создаем вертикальный layout
        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.verticalLayout.setObjectName("verticalLayout")

        # Создаем метку для заголовка
        self.label_8 = QtWidgets.QLabel(self)
        self.label_8.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "font: 75 24pt \"MS Shell Dlg 2\";\n"
                                   "background-color: none;\n"
                                   "border: none;\n"
                                   "font-weight: bold;")
        self.label_8.setObjectName("label_8")
        self.verticalLayout.addWidget(self.label_8)

        # Создаем фрейм для данных авторизации
        self.passwordFrame = QtWidgets.QFrame(self)
        self.passwordFrame.setStyleSheet("background-color: rgba(255, 255, 255, 30);\n"
                                         "border: 1px solid rgba(255, 255, 255, 40);\n"
                                         "border-radius: 7px;")
        self.passwordFrame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.passwordFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)

        # Вложенный вертикальный layout в фрейме
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.passwordFrame)
        self.verticalLayout_3.setObjectName("verticalLayout_3")

        # Создаем метку для данных авторизации
        self.label = QtWidgets.QLabel(self.passwordFrame)
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
                                 "font: 75 20pt \"MS Shell Dlg 2\";\n"
                                 "background-color: none;\n"
                                 "border: none;")
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)

        # Создаем поля для ввода данных авторизации
        self.lineEdit_5 = QtWidgets.QLineEdit(self.passwordFrame)
        self.lineEdit_5.setStyleSheet("font-size: 16pt;\n"
                                      "color:rgb(255, 255, 255);\n"
                                      "padding-left: 10px;")
        self.verticalLayout_3.addWidget(self.lineEdit_5)

        self.lineEdit_4 = QtWidgets.QLineEdit(self.passwordFrame)
        self.lineEdit_4.setStyleSheet("font-size: 16pt;\n"
                                      "color:rgb(255, 255, 255);\n"
                                      "padding-left: 10px;")
        self.verticalLayout_3.addWidget(self.lineEdit_4)

        self.lineEdit_3 = QtWidgets.QLineEdit(self.passwordFrame)
        self.lineEdit_3.setStyleSheet("font-size: 16pt;\n"
                                      "color:rgb(255, 255, 255);\n"
                                      "padding-left: 10px;")
        self.verticalLayout_3.addWidget(self.lineEdit_3)

        # Добавляем фрейм в основной layout
        self.verticalLayout.addWidget(self.passwordFrame)

        # Создаем фрейм для восстановления пароля
        self.remembPassFrame = QtWidgets.QFrame(self)
        self.remembPassFrame.setStyleSheet("background-color: rgba(255, 255, 255, 30);\n"
                                           "border: 1px solid rgba(255, 255, 255, 40);\n"
                                           "border-radius: 7px;")
        self.remembPassFrame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.remembPassFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)

        # Вложенный вертикальный layout во втором фрейме
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.remembPassFrame)
        self.verticalLayout_7.setObjectName("verticalLayout_7")

        # Создаем метку для восстановления пароля
        self.label_5 = QtWidgets.QLabel(self.remembPassFrame)
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "font: 75 20pt \"MS Shell Dlg 2\";\n"
                                   "background-color: none;\n"
                                   "border: none;")
        self.label_5.setObjectName("label_5")
        self.verticalLayout_7.addWidget(self.label_5)

        # Создаем фрейм внутри фрейма для ввода вопроса и ответа
        self.frame_2 = QtWidgets.QFrame(self.remembPassFrame)
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)

        # Вложенный вертикальный layout во втором фрейме
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_8.setObjectName("verticalLayout_8")

        # Создаем метку для ввода вопроса и ответа
        self.label_6 = QtWidgets.QLabel(self.frame_2)
        self.label_6.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "font: 75 12pt \"MS Shell Dlg 2\";\n"
                                   "background-color: none;\n"
                                   "border: none;")
        self.label_6.setObjectName("label_6")
        self.verticalLayout_8.addWidget(self.label_6)

        # Создаем поля для ввода вопроса и ответа
        self.lineEdit = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit.setStyleSheet("font-size: 16pt;\n"
                                    "color:rgb(255, 255, 255);\n"
                                    "padding-left: 10px;")
        self.verticalLayout_8.addWidget(self.lineEdit)

        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_2.setStyleSheet("font-size: 16pt;\n"
                                      "color:rgb(255, 255, 255);\n"
                                      "padding-left: 10px;")
        self.verticalLayout_8.addWidget(self.lineEdit_2)

        # Добавляем фрейм в основной layout
        self.verticalLayout_7.addWidget(self.frame_2)
        self.verticalLayout.addWidget(self.remembPassFrame)

        # Создаем кнопку "Сохранить"
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setStyleSheet("QPushButton {\n"
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
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)

        # Переводим текст на форму
        self.retranslateUi()

        # Соединяем слоты и сигналы
        QtCore.QMetaObject.connectSlotsByName(self)
        self.setTabOrder(self.lineEdit, self.pushButton)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("regDialog", "WalletWise: Family Finance Tracker"))
        self.label_8.setText(_translate("regDialog", "Создание аккаунта семьи"))
        self.label.setText(_translate("regDialog", "Данные для авторизации"))
        self.lineEdit_5.setPlaceholderText(_translate("regDialog", "Введите фамилию семьи"))
        self.lineEdit_4.setPlaceholderText(_translate("regDialog", "Придумайте и введите пароль"))
        self.lineEdit_3.setPlaceholderText(_translate("regDialog", "Введите пароль повторно"))
        self.label_5.setText(_translate("regDialog", "Восстановление пароля"))
        self.label_6.setText(_translate("regDialog", "Придумайте вопрос и ответ на него \n"
                                                     "(будет использоваться для напоминания пароля)"))
        self.lineEdit.setPlaceholderText(_translate("regDialog", "Вопрос"))
        self.lineEdit_2.setPlaceholderText(_translate("regDialog", "Ответ на ваш вопрос"))
        self.pushButton.setText(_translate("regDialog", "Сохранить"))

        self.pushButton.clicked.connect(self.reg_log)

    def reg_log(self):
        from AuthWindow import AuthDialog

        # Проверяем, что все поля заполнены
        if any(field.text().strip() == "" for field in [self.lineEdit_5, self.lineEdit_4, self.lineEdit_3, self.lineEdit, self.lineEdit_2]):
            msg = QMessageBox(self)
            msg.setStyleSheet("QPushButton{\n"
                              "font: 75 12pt \"MS Shell Dlg 2\";\n"
                              "color: rgb(255, 255, 255);"
                              "background-color: rgba(255, 255, 255, 50);\n"
                              "border: 1px solid rgba(255, 255, 255, 60);\n"
                              "border-radius:7px;\n"
                              "width: 230;\n"
                              "height: 30;\n"
                              "}\n"
                              "QPushButton:hover{\n"
                              "background-color: rgba(255, 255, 255, 70);\n"
                              "}\n"
                              "QPushButton:pressed{\n"
                              "background-color: rgba(255, 255, 255, 90);\n"
                              "}"
                              "QLabel{"
                              "color: rgb(255, 255, 255);\n"
                              "font: 75 12pt \"MS Shell Dlg 2\";\n"
                              "background-color: none;\n"
                              "border: none;\n"
                              "font-weight: bold;};\n")
            msg.setText("Пожалуйста, заполните все поля.")
            msg.setWindowTitle("Ошибка")
            msg.exec()
            return

        # Проверяем, что пароли совпадают
        if self.lineEdit_4.text() != self.lineEdit_3.text():
            msg = QMessageBox(self)
            msg.setStyleSheet("QPushButton{\n"
                              "font: 75 12pt \"MS Shell Dlg 2\";\n"
                              "color: rgb(255, 255, 255);"
                              "background-color: rgba(255, 255, 255, 50);\n"
                              "border: 1px solid rgba(255, 255, 255, 60);\n"
                              "border-radius:7px;\n"
                              "width: 230;\n"
                              "height: 30;\n"
                              "}\n"
                              "QPushButton:hover{\n"
                              "background-color: rgba(255, 255, 255, 70);\n"
                              "}\n"
                              "QPushButton:pressed{\n"
                              "background-color: rgba(255, 255, 255, 90);\n"
                              "}"
                              "QLabel{"
                              "color: rgb(255, 255, 255);\n"
                              "font: 75 12pt \"MS Shell Dlg 2\";\n"
                              "background-color: none;\n"
                              "border: none;\n"
                              "font-weight: bold;};\n")
            msg.setText("Пароли не совпадают.")
            msg.setWindowTitle("Ошибка")
            msg.exec()
            return

        # Сохраняем данные пользователя в базе данных
        login = self.lineEdit_5.text()
        password = self.lineEdit_4.text()
        code_question = self.lineEdit.text()
        code_answer = self.lineEdit_2.text()

        if self.db_manager.add_user(login, password, code_question, code_answer):
            msg = QMessageBox(self)
            msg.setStyleSheet("QPushButton{\n"
                              "font: 75 12pt \"MS Shell Dlg 2\";\n"
                              "color: rgb(255, 255, 255);"
                              "background-color: rgba(255, 255, 255, 50);\n"
                              "border: 1px solid rgba(255, 255, 255, 60);\n"
                              "border-radius:7px;\n"
                              "width: 230;\n"
                              "height: 30;\n"
                              "}\n"
                              "QPushButton:hover{\n"
                              "background-color: rgba(255, 255, 255, 70);\n"
                              "}\n"
                              "QPushButton:pressed{\n"
                              "background-color: rgba(255, 255, 255, 90);\n"
                              "}"
                              "QLabel{"
                              "color: rgb(255, 255, 255);\n"
                              "font: 75 12pt \"MS Shell Dlg 2\";\n"
                              "background-color: none;\n"
                              "border: none;\n"
                              "font-weight: bold;};\n")
            msg.setText("Семья успешно зарегистрирована.")
            msg.setWindowTitle("Успех")
            msg.exec()
            self.close()
            # Открываем окно авторизации
            self.dlg = AuthDialog()
            self.dlg.show()
        else:
            msg = QMessageBox(self)
            msg.setStyleSheet("QPushButton{\n"
                              "font: 75 12pt \"MS Shell Dlg 2\";\n"
                              "color: rgb(255, 255, 255);"
                              "background-color: rgba(255, 255, 255, 50);\n"
                              "border: 1px solid rgba(255, 255, 255, 60);\n"
                              "border-radius:7px;\n"
                              "width: 230;\n"
                              "height: 30;\n"
                              "}\n"
                              "QPushButton:hover{\n"
                              "background-color: rgba(255, 255, 255, 70);\n"
                              "}\n"
                              "QPushButton:pressed{\n"
                              "background-color: rgba(255, 255, 255, 90);\n"
                              "}"
                              "QLabel{"
                              "color: rgb(255, 255, 255);\n"
                              "font: 75 12pt \"MS Shell Dlg 2\";\n"
                              "background-color: none;\n"
                              "border: none;\n"
                              "font-weight: bold;};\n")
            msg.setText("Не удалось зарегистрировать семью.")
            msg.setWindowTitle("Ошибка")
            msg.exec()

    def closeEvent(self, event):
        # Закрываем соединение с базой данных при закрытии окна
        self.db_manager.close_connection()
        event.accept()