from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QWidget
from database import DatabaseManager


class RegWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.bank_acc_dialog = None
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
        self.headLabel = QtWidgets.QLabel(self)
        self.headLabel.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "font: 75 24pt \"MS Shell Dlg 2\";\n"
                                   "background-color: none;\n"
                                   "border: none;\n"
                                   "font-weight: bold;")
        self.headLabel.setObjectName("headLabel")
        self.verticalLayout.addWidget(self.headLabel)

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
        self.famLogLine = QtWidgets.QLineEdit(self.passwordFrame)
        self.famLogLine.setStyleSheet("font-size: 16pt;\n"
                                      "color:rgb(255, 255, 255);\n"
                                      "padding-left: 10px;")
        self.verticalLayout_3.addWidget(self.famLogLine)

        self.passwordLine = QtWidgets.QLineEdit(self.passwordFrame)
        self.passwordLine.setStyleSheet("font-size: 16pt;\n"
                                      "color:rgb(255, 255, 255);\n"
                                      "padding-left: 10px;")
        self.verticalLayout_3.addWidget(self.passwordLine)

        self.confPasswordLine = QtWidgets.QLineEdit(self.passwordFrame)
        self.confPasswordLine.setStyleSheet("font-size: 16pt;\n"
                                      "color:rgb(255, 255, 255);\n"
                                      "padding-left: 10px;")
        self.verticalLayout_3.addWidget(self.confPasswordLine)

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
        self.recPassLabel = QtWidgets.QLabel(self.remembPassFrame)
        self.recPassLabel.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "font: 75 20pt \"MS Shell Dlg 2\";\n"
                                   "background-color: none;\n"
                                   "border: none;")
        self.recPassLabel.setObjectName("questionLabel")
        self.verticalLayout_7.addWidget(self.recPassLabel)

        # Создаем фрейм внутри фрейма для ввода вопроса и ответа
        self.frame_2 = QtWidgets.QFrame(self.remembPassFrame)
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)

        # Вложенный вертикальный layout во втором фрейме
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_8.setObjectName("verticalLayout_8")

        # Создаем метку для ввода вопроса и ответа
        self.recPassMoreLabel = QtWidgets.QLabel(self.frame_2)
        self.recPassMoreLabel.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "font: 75 12pt \"MS Shell Dlg 2\";\n"
                                   "background-color: none;\n"
                                   "border: none;")
        self.recPassMoreLabel.setObjectName("recPassMoreLabel")
        self.verticalLayout_8.addWidget(self.recPassMoreLabel)

        # Создаем поля для ввода вопроса и ответа
        self.codeQuestionLine = QtWidgets.QLineEdit(self.frame_2)
        self.codeQuestionLine.setStyleSheet("font-size: 16pt;\n"
                                    "color:rgb(255, 255, 255);\n"
                                    "padding-left: 10px;")
        self.verticalLayout_8.addWidget(self.codeQuestionLine)

        self.codeAnswerLine = QtWidgets.QLineEdit(self.frame_2)
        self.codeAnswerLine.setStyleSheet("font-size: 16pt;\n"
                                      "color:rgb(255, 255, 255);\n"
                                      "padding-left: 10px;")
        self.verticalLayout_8.addWidget(self.codeAnswerLine)

        # Добавляем фрейм в основной layout
        self.verticalLayout_7.addWidget(self.frame_2)
        self.verticalLayout.addWidget(self.remembPassFrame)

        # Создаем кнопку "Сохранить"
        self.saveButton = QtWidgets.QPushButton(self)
        self.saveButton.setStyleSheet("QPushButton {\n"
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
        self.saveButton.setObjectName("saveButton")
        self.verticalLayout.addWidget(self.saveButton)

        # Переводим текст на форму
        self.retranslateUi()

        # Соединяем слоты и сигналы
        QtCore.QMetaObject.connectSlotsByName(self)
        self.setTabOrder(self.codeQuestionLine, self.saveButton)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("regDialog", "WalletWise: Family Finance Tracker"))
        self.headLabel.setText(_translate("regDialog", "Создание аккаунта семьи"))
        self.label.setText(_translate("regDialog", "Данные для авторизации"))
        self.famLogLine.setPlaceholderText(_translate("regDialog", "Введите фамилию семьи (логин)"))
        self.passwordLine.setPlaceholderText(_translate("regDialog", "Придумайте и введите пароль"))
        self.confPasswordLine.setPlaceholderText(_translate("regDialog", "Введите пароль повторно"))
        self.recPassLabel.setText(_translate("regDialog", "Восстановление пароля"))
        self.recPassMoreLabel.setText(_translate("regDialog", "Придумайте вопрос и ответ на него \n"
                                                     "(будет использоваться для напоминания пароля)"))
        self.codeQuestionLine.setPlaceholderText(_translate("regDialog", "Вопрос"))
        self.codeAnswerLine.setPlaceholderText(_translate("regDialog", "Ответ на ваш вопрос"))
        self.saveButton.setText(_translate("regDialog", "Сохранить"))

        #обработка клика по кнопке "Сохранить"
        self.saveButton.clicked.connect(self.reg_log)

    def reg_log(self):
        from NewBankAcc import BankAccWin
        from message_box import MessageBox

        # Проверяем, что все поля заполнены
        if any(field.text().strip() == "" for field in
               [self.famLogLine, self.passwordLine, self.confPasswordLine, self.codeQuestionLine, self.codeAnswerLine]):
            error_msg = MessageBox(self)
            error_msg.show_message("Ошибка", "Пожалуйста, заполните все поля.", MessageBox.Icon.Critical)
            return

        # Проверяем, что пароли совпадают
        if self.passwordLine.text() != self.confPasswordLine.text():
            error_msg = MessageBox(self)
            error_msg.show_message("Ошибка", "Пароли не совпадают.", MessageBox.Icon.Critical)
            return

        # Сохраняем данные пользователя в базе данных
        login = self.famLogLine.text()
        password = self.passwordLine.text()
        code_question = self.codeQuestionLine.text()
        code_answer = self.codeAnswerLine.text()

        familly = self.db_manager.add_user(login, password, code_question, code_answer)
        print(familly)

        if familly:
            success_msg = MessageBox(self)
            success_msg.show_message("Успех", "Семья успешно зарегистрирована.", MessageBox.Icon.Information)
            self.close()

            # Открываем окно добавления банковского счета после успешной регистрации
            self.bank_acc_dialog = BankAccWin(familly[0], is_registration=True)
            self.bank_acc_dialog.show()
        else:
            error_msg = MessageBox(self)
            error_msg.show_message("Ошибка", "Не удалось зарегистрировать семью.", MessageBox.Icon.Critical)



