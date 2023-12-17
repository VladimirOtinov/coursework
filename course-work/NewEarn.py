from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QWidget


class NewEarn(QWidget):
    def __init__(self):
        super(NewEarn, self).__init__()
        self.setupUi(self)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        Form.setStyleSheet(
            "background-color: qlineargradient(spread:reflect, x1:0.549682, y1:0.494, x2:0, y2:0, stop:0 rgba(0, 18, 221, 216), stop:1 rgba(179, 0, 241, 216));\n"
            "font: 10pt \"Bahnschrift SemiLight\";\n"
            "\n"
            "")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtWidgets.QFrame(parent=Form)
        self.frame.setStyleSheet("background-color: rgba(255, 255, 255, 30);\n"
                                 "border: 1px solid rgba(255, 255, 255, 40);\n"
                                 "border-radius: 7px;")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.transaction_label = QtWidgets.QLabel(parent=self.frame)
        self.transaction_label.setStyleSheet("color: rgb(255, 255, 255);\n"
                                             "font: 75 20pt \"MS Shell Dlg 2\";\n"
                                             "background-color: none;\n"
                                             "border: none;\n"
                                             "font-weight: bold;\n"
                                             "")
        self.transaction_label.setObjectName("transaction_label")
        self.verticalLayout.addWidget(self.transaction_label)
        self.categoryComboBox = QtWidgets.QComboBox(parent=self.frame)
        self.categoryComboBox.setStyleSheet("QComboBox{\n"
                                            "font-size: 16pt;\n"
                                            "color: white;\n"
                                            "}\n"
                                            "\n"
                                            "QComboBox::item{\n"
                                            "color: black;\n"
                                            "}")
        self.categoryComboBox.setEditable(False)
        self.categoryComboBox.setDuplicatesEnabled(False)
        self.categoryComboBox.setObjectName("categoryComboBox")
        self.categoryComboBox.addItem("")
        self.categoryComboBox.addItem("")
        self.categoryComboBox.addItem("")
        self.categoryComboBox.addItem("")
        self.categoryComboBox.addItem("")
        self.verticalLayout.addWidget(self.categoryComboBox)
        self.dateEdit = QtWidgets.QDateEdit(parent=self.frame)
        self.dateEdit.setStyleSheet("font-size: 16pt;\n"
                                    "color: white;\n"
                                    "padding-left:10px;")
        self.dateEdit.setButtonSymbols(QtWidgets.QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.dateEdit.setDate(QtCore.QDate(2023, 1, 1))
        self.dateEdit.setObjectName("dateEdit")
        self.verticalLayout.addWidget(self.dateEdit)
        self.descriptionLine = QtWidgets.QLineEdit(parent=self.frame)
        self.descriptionLine.setStyleSheet("font-size: 16pt;\n"
                                           "color:rgb(255, 255, 255);\n"
                                           "padding-left: 10px;")
        self.descriptionLine.setObjectName("descriptionLine")
        self.verticalLayout.addWidget(self.descriptionLine)
        self.money_sumLine = QtWidgets.QLineEdit(parent=self.frame)
        self.money_sumLine.setStyleSheet("font-size: 15pt;\n"
                                         "color:rgb(255, 255, 255);\n"
                                         "padding-left: 10px;")
        self.money_sumLine.setObjectName("money_sumLine")
        self.verticalLayout.addWidget(self.money_sumLine)
        self.save_pushButton = QtWidgets.QPushButton(parent=self.frame)
        self.save_pushButton.setStyleSheet("QPushButton {\n"
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
        self.save_pushButton.setObjectName("save_pushButton")
        self.verticalLayout.addWidget(self.save_pushButton)
        self.verticalLayout_2.addWidget(self.frame)

        self.retranslateUi(Form)
        self.categoryComboBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.transaction_label.setText(_translate("Form", "Новая транзакция"))
        self.categoryComboBox.setCurrentText(_translate("Form", "Выберите категорию"))
        self.categoryComboBox.setItemText(0, _translate("Form", "Выберите категорию"))
        self.categoryComboBox.setItemText(1, _translate("Form", "Работа"))
        self.categoryComboBox.setItemText(2, _translate("Form", "Акции, вклады, облигации"))
        self.categoryComboBox.setItemText(3, _translate("Form", "Подарки"))
        self.categoryComboBox.setItemText(4, _translate("Form", "Другое"))
        self.descriptionLine.setPlaceholderText(_translate("Form", "Описание"))
        self.money_sumLine.setPlaceholderText(_translate("Form", "Введите сумму транзакции, до сотых"))
        self.save_pushButton.setText(_translate("Form", "Сохранить Транзанкцию"))
