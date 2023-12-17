from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QWidget
from database import DatabaseManager

class NewPassword(QWidget):
    def __init__(self):
        super(NewPassword, self).__init__()
        self.setupUi(self)
        # Создаем элементы интерфейса
        self.db_manager = DatabaseManager("budget.db")
        self.load_security_question()

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(512, 338)
        Form.setStyleSheet(
            "background-color: qlineargradient(spread:reflect, x1:0.549682, y1:0.494, x2:0, y2:0, stop:0 rgba(0, 18, 221, 216), stop:1 rgba(179, 0, 241, 216));\n"
            "font: 10pt \"Bahnschrift SemiLight\";\n"
            "")
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_3 = QtWidgets.QFrame(parent=Form)
        self.frame_3.setStyleSheet("background-color: rgba(255, 255, 255, 30);\n"
                                   "border: 1px solid rgba(255, 255, 255, 40);\n"
                                   "border-radius: 7px;")
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_3 = QtWidgets.QLabel(parent=self.frame_3)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "font: 75 20pt \"MS Shell Dlg 2\";\n"
                                   "background-color: none;\n"
                                   "border: none;\n"
                                   "font-weight: bold;\n"
                                   "")
        self.label_3.setObjectName("label_3")
        self.verticalLayout_4.addWidget(self.label_3)
        self.frame_5 = QtWidgets.QFrame(parent=self.frame_3)
        self.frame_5.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_5 = QtWidgets.QLabel(parent=self.frame_5)
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "font: 75 18pt \"MS Shell Dlg 2\";\n"
                                   "background-color: none;\n"
                                   "border: none;")
        self.label_5.setObjectName("label_5")
        self.verticalLayout_6.addWidget(self.label_5)
        self.lineEdit_4 = QtWidgets.QLineEdit(parent=self.frame_5)
        self.lineEdit_4.setStyleSheet("font-size: 16pt;\n"
                                      "color:rgb(255, 255, 255);\n"
                                      "padding-left: 10px;")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.verticalLayout_6.addWidget(self.lineEdit_4)
        self.verticalLayout_4.addWidget(self.frame_5)
        self.frame_6 = QtWidgets.QFrame(parent=self.frame_3)
        self.frame_6.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_6 = QtWidgets.QLabel(parent=self.frame_6)
        self.label_6.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "font: 75 18pt \"MS Shell Dlg 2\";\n"
                                   "background-color: none;\n"
                                   "border: none;")
        self.label_6.setObjectName("label_6")
        self.verticalLayout_7.addWidget(self.label_6)
        self.lineEdit_5 = QtWidgets.QLineEdit(parent=self.frame_6)
        self.lineEdit_5.setStyleSheet("font-size: 16pt;\n"
                                      "color:rgb(255, 255, 255);\n"
                                      "padding-left: 10px;")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.verticalLayout_7.addWidget(self.lineEdit_5)
        self.lineEdit_6 = QtWidgets.QLineEdit(parent=self.frame_6)
        self.lineEdit_6.setStyleSheet("font-size: 16pt;\n"
                                      "color:rgb(255, 255, 255);\n"
                                      "padding-left: 10px;")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.verticalLayout_7.addWidget(self.lineEdit_6)
        self.verticalLayout_4.addWidget(self.frame_6)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.backButton_2 = QtWidgets.QPushButton(parent=self.frame_3)
        self.backButton_2.setStyleSheet("QPushButton {\n"
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
        self.backButton_2.setObjectName("backButton_2")
        self.horizontalLayout_2.addWidget(self.backButton_2)
        self.saveButton_2 = QtWidgets.QPushButton(parent=self.frame_3)
        self.saveButton_2.setStyleSheet("QPushButton {\n"
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
        self.saveButton_2.setObjectName("saveButton_2")
        self.horizontalLayout_2.addWidget(self.saveButton_2)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.verticalLayout.addWidget(self.frame_3)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_3.setText(_translate("Form", "Восстановление пароля"))
        self.label_5.setText(_translate("Form", "вопрос"))
        self.lineEdit_4.setPlaceholderText(_translate("Form", "Ответ на вопрос"))
        self.label_6.setText(_translate("Form", "Изменение пароля"))
        self.lineEdit_5.setPlaceholderText(_translate("Form", "Введите новый пароль"))
        self.lineEdit_6.setPlaceholderText(_translate("Form", "Повторите новый пароль"))
        self.backButton_2.setText(_translate("Form", "Назад"))
        self.saveButton_2.setText(_translate("Form", "Сохранить"))


        self.backButton.clicked.connect(self.back_win)
        self.saveButton.clicked.connect(self.save_password)

    def back_win(self):
        from AuthWindow import AuthWindow
        self.close()
        self.dlg = AuthWindow()
        self.dlg.exec()

    def load_security_question(self):
        # Получаем кодовый вопрос из базы данных и выводим его в label
        security_question = self.db_manager.get_security_question()
        if security_question:
            self.label.setText(security_question)
        else:
            self.label.setText("Не удалось загрузить вопрос")


    def save_password(self):
        from AuthWindow import AuthWindow
        from message_box import MessageBox

        # Получаем кодовый ответ из базы данных
        correct_answer = self.db_manager.get_security_answer()

        # Проверяем, совпадает ли введенный ответ с сохраненным в базе данных
        entered_answer = self.lineEdit.text()
        if not entered_answer:
            # Отображаем сообщение о том, что поле с ответом на вопрос не заполнено
            error_msg = MessageBox(self)
            error_msg.show_message("Ошибка", "Пожалуйста, введите ответ на кодовый вопрос.", MessageBox.Icon.Critical)
            return

        if entered_answer == correct_answer:
            new_password = self.lineEdit_2.text()
            confirm_password = self.lineEdit_3.text()

            # Проверяем, что все поля нового пароля заполнены
            if not new_password or not confirm_password:
                # Отображаем сообщение о том, что не все поля заполнены
                error_msg = MessageBox(self)
                error_msg.show_message("Ошибка", "Пожалуйста, заполните все поля для изменения пароля.",
                                       MessageBox.Icon.Critical)
                return

            # Проверяем, что новый пароль и его подтверждение совпадают
            if new_password == confirm_password:
                # Сохраняем новый пароль в базе данных
                user_id = 1  # Идентификатор пользователя
                success = self.db_manager.change_password_by_id(user_id, new_password)

                if success:
                    # Отображаем успешное сообщение
                    success_msg = MessageBox(self)
                    success_msg.show_message("Успех", "Пароль успешно изменен.", MessageBox.Icon.Information)
                    self.close()

                    # Открываем окно авторизации
                    self.dlg = AuthWindow()
                    self.dlg.show()
                else:
                    # Отображаем сообщение об ошибке
                    error_msg = MessageBox(self)
                    error_msg.show_message("Ошибка", "Не удалось изменить пароль.", MessageBox.Icon.Critical)
            else:
                # Отображаем сообщение о несовпадении паролей
                error_msg = MessageBox(self)
                error_msg.show_message("Ошибка", "Новый пароль и подтверждение не совпадают.", MessageBox.Icon.Critical)
        else:
            # Отображаем сообщение о неверном ответе на вопрос
            error_msg = MessageBox(self)
            error_msg.show_message("Ошибка", "Неверный ответ на кодовый вопрос.", MessageBox.Icon.Critical)
