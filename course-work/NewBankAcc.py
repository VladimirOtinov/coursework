from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QDialog
from database import DatabaseManager

class BankAccDialog(QDialog):
    def __init__(self):
        super(BankAccDialog, self).__init__()
        self.db_manager = DatabaseManager("budget.db")  # Создаем объект базы данных
        self.setupUi(self)
    def setupUi(self, bankAccDialog):
        bankAccDialog.setObjectName("bankAccDialog")
        bankAccDialog.resize(267, 247)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(bankAccDialog.sizePolicy().hasHeightForWidth())
        bankAccDialog.setSizePolicy(sizePolicy)
        bankAccDialog.setStyleSheet("background-color: qlineargradient(spread:reflect, x1:0.549682, y1:0.494, x2:0, y2:0, stop:0 rgba(0, 18, 221, 216), stop:1 rgba(179, 0, 241, 216));\n"
"font: 10pt \"Bahnschrift SemiLight\";\n"
"")
        self.verticalLayout = QtWidgets.QVBoxLayout(bankAccDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(parent=bankAccDialog)
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 16pt \"MS Shell Dlg 2\";\n"
"background-color: none;\n"
"border: none;\n"
"font-weight: bold;\n"
"")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.frame = QtWidgets.QFrame(parent=bankAccDialog)
        self.frame.setStyleSheet("background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.bankAccLine = QtWidgets.QLineEdit(parent=self.frame)
        self.bankAccLine.setStyleSheet("font-size: 16pt;\n"
"color:rgb(255, 255, 255);\n"
"padding-left: 10px;")
        self.bankAccLine.setObjectName("bankAccLine")
        self.verticalLayout_2.addWidget(self.bankAccLine)
        self.bankAccLine_2 = QtWidgets.QLineEdit(parent=self.frame)
        self.bankAccLine_2.setStyleSheet("font-size: 16pt;\n"
"color:rgb(255, 255, 255);\n"
"padding-left: 10px;")
        self.bankAccLine_2.setObjectName("bankAccLine_2")
        self.verticalLayout_2.addWidget(self.bankAccLine_2)
        self.label_2 = QtWidgets.QLabel(parent=self.frame)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color:none;\n"
"border: none;\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.moneySpinBox = QtWidgets.QDoubleSpinBox(parent=self.frame)
        self.moneySpinBox.setStyleSheet("font-size: 16pt;\n"
"color: white;\n"
"padding-left:10px;")
        self.moneySpinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.ButtonSymbols.PlusMinus)
        self.moneySpinBox.setSpecialValueText("")
        self.moneySpinBox.setMaximum(9999999999999900.0)
        self.moneySpinBox.setSingleStep(100.0)
        self.moneySpinBox.setProperty("value", 1000.0)
        self.moneySpinBox.setObjectName("moneySpinBox")
        self.verticalLayout_2.addWidget(self.moneySpinBox)
        self.verticalLayout.addWidget(self.frame)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.cancelButton = QtWidgets.QPushButton(parent=bankAccDialog)
        self.cancelButton.setStyleSheet("QPushButton {\n"
"font: 75 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 50);\n"
"border: 1px solid rgba(255, 255, 255, 60);\n"
"border-radius: 7px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(255, 255, 255, 60);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgba(255, 255, 255, 80);\n"
"}")
        self.cancelButton.setObjectName("cancelButton")
        self.horizontalLayout.addWidget(self.cancelButton)
        self.saveButton = QtWidgets.QPushButton(parent=bankAccDialog)
        self.saveButton.setStyleSheet("QPushButton {\n"
"font: 75 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 50);\n"
"border: 1px solid rgba(255, 255, 255, 60);\n"
"border-radius: 7px;\n"
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
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(bankAccDialog)
        QtCore.QMetaObject.connectSlotsByName(bankAccDialog)

    def retranslateUi(self, bankAccDialog):
        _translate = QtCore.QCoreApplication.translate
        bankAccDialog.setWindowTitle(_translate("bankAccDialog", "WalletWise: Family Finance Tracker"))
        self.label.setText(_translate("bankAccDialog", "Заполнение данных \n"
"о счете"))
        self.bankAccLine.setPlaceholderText(_translate("bankAccDialog", "Название счета"))
        self.bankAccLine_2.setPlaceholderText(_translate("bankAccDialog", "Краткое описание"))
        self.label_2.setText(_translate("bankAccDialog", "Введите остаток на счете"))
        self.cancelButton.setText(_translate("bankAccDialog", "Отмена"))
        self.saveButton.setText(_translate("bankAccDialog", "Сохранить"))

    def save_family_member_account(self):
        # Получаем данные из интерфейса
        name = self.bankAccLine.text()
        account_info = self.bankAccLine_2.text()
        money = self.moneySpinBox.value()

        # Получаем ID текущего пользователя (предполагая, что у вас есть метод для этого)
        user_id = self.get_current_user_id()

        # Добавляем счет члена семьи в базу данных
        if self.db_manager.add_family_member_account(name, account_info, money, user_id):
            print("Счет успешно сохранен.")
        else:
            print("Не удалось сохранить счет.")