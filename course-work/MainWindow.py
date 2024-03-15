from datetime import datetime

from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMainWindow
from database import DatabaseManager
from message_box import MessageBox
from NewTransaction import NewTransaction


class MainWindow(QMainWindow):
    def __init__(self, familly_id):
        super(MainWindow, self).__init__()
        self.bank_acc_dialog = None
        self.new_tr = None
        self.transs = None
        self.tableWidget = None
        self.accs = None
        self.db_manager = DatabaseManager("budget.db")
        self.familly_id = familly_id
        self.setupUi(self)


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1110, 740)
        MainWindow.setStyleSheet(
            "background-color: qlineargradient(spread:reflect, x1:0.549682, y1:0.494, x2:0, y2:0, stop:0 rgba(0, 18, 221, 216), stop:1 rgba(179, 0, 241, 216));\n"
            "font: 10pt \"Bahnschrift SemiLight\";\n"
            "")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.changeFamilyButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.changeFamilyButton.setStyleSheet("QPushButton {\n"
                                              "font: 11pt \"MS Shell Dlg 2\";\n"
                                              "color: rgb(255, 255, 255);\n"
                                              "background-color: rgba(255, 255, 255, 50);\n"
                                              "border: 1px solid rgba(255, 255, 255, 60);\n"
                                              "border-radius: 7px;\n"
                                              "width: 230px;\n"
                                              "height: 30px;\n"
                                              "}\n"
                                              "QPushButton:hover{\n"
                                              "background-color: rgba(255, 255, 255, 70);\n"
                                              "}\n"
                                              "\n"
                                              "QPushButton:pressed{\n"
                                              "background-color: rgba(255, 255, 255, 80);\n"
                                              "}")
        self.changeFamilyButton.setObjectName("changeFamilyButton")
        self.horizontalLayout_4.addWidget(self.changeFamilyButton)
        self.addBankAccButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.addBankAccButton.setStyleSheet("QPushButton {\n"
                                            "font: 11pt \"MS Shell Dlg 2\";\n"
                                            "color: rgb(255, 255, 255);\n"
                                            "background-color: rgba(255, 255, 255, 50);\n"
                                            "border: 1px solid rgba(255, 255, 255, 60);\n"
                                            "border-radius: 7px;\n"
                                            "width: 230px;\n"
                                            "height: 30px;\n"
                                            "}\n"
                                            "QPushButton:hover{\n"
                                            "background-color: rgba(255, 255, 255, 70);\n"
                                            "}\n"
                                            "\n"
                                            "QPushButton:pressed{\n"
                                            "background-color: rgba(255, 255, 255, 80);\n"
                                            "}")
        self.addBankAccButton.setObjectName("addBankAccButton")
        self.horizontalLayout_4.addWidget(self.addBankAccButton)
        self.delBankAccButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.delBankAccButton.setStyleSheet("QPushButton {\n"
                                            "font: 11pt \"MS Shell Dlg 2\";\n"
                                            "color: rgb(255, 255, 255);\n"
                                            "background-color: rgba(255, 255, 255, 50);\n"
                                            "border: 1px solid rgba(255, 255, 255, 60);\n"
                                            "border-radius: 7px;\n"
                                            "width: 230px;\n"
                                            "height: 30px;\n"
                                            "}\n"
                                            "QPushButton:hover{\n"
                                            "background-color: rgba(255, 255, 255, 70);\n"
                                            "}\n"
                                            "\n"
                                            "QPushButton:pressed{\n"
                                            "background-color: rgba(255, 255, 255, 80);\n"
                                            "}")
        self.delBankAccButton.setObjectName("delBankAccButton")
        self.horizontalLayout_4.addWidget(self.delBankAccButton)
        self.label_22 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_22.setStyleSheet("color: rgb(255, 255, 255);\n"
                                    "font: 75 14pt \"MS Shell Dlg 2\";\n"
                                    "background-color: none;\n"
                                    "border: none;")
        self.label_22.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignRight | QtCore.Qt.AlignmentFlag.AlignTrailing | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_22.setObjectName("label_22")
        self.horizontalLayout_4.addWidget(self.label_22)
        self.changePersonComboBox = QtWidgets.QComboBox(parent=self.centralwidget)
        self.changePersonComboBox.setStyleSheet("\n"
                                                "QComboBox {\n"
                                                "color: rgb(255, 255, 255);\n"
                                                "background-color: qlineargradient(spread:reflect, x1:0.549682, y1:0.494, x2:0, y2:0, stop:0 rgba(0, 18, 221, 150), stop:1 rgba(179, 0, 241, 150));;\n"
                                                "border: 1px solid rgba(255, 255, 255, 50);\n"
                                                "border-radius: 7px;\n"
                                                "    font: 14pt \"MS Shell Dlg 2\";\n"
                                                "}\n"
                                                "")
        self.changePersonComboBox.setObjectName("changePersonComboBox")
        self.changePersonComboBox.addItem("")
        self.horizontalLayout_4.addWidget(self.changePersonComboBox)
        self.infoBankAccButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.infoBankAccButton.setStyleSheet("QPushButton {\n"
                                             "font: 11pt \"MS Shell Dlg 2\";\n"
                                             "color: rgb(255, 255, 255);\n"
                                             "background-color: rgba(255, 255, 255, 50);\n"
                                             "border: 1px solid rgba(255, 255, 255, 60);\n"
                                             "border-radius: 7px;\n"
                                             "width: 230px;\n"
                                             "height: 30px;\n"
                                             "}\n"
                                             "QPushButton:hover{\n"
                                             "background-color: rgba(255, 255, 255, 70);\n"
                                             "}\n"
                                             "\n"
                                             "QPushButton:pressed{\n"
                                             "background-color: rgba(255, 255, 255, 80);\n"
                                             "}")
        self.infoBankAccButton.setObjectName("infoBankAccButton")
        self.horizontalLayout_4.addWidget(self.infoBankAccButton)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.balance_category_frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.balance_category_frame.setStyleSheet("background-color: rgba(255, 255, 255, 30);\n"
                                                  "border: 1px solid rgba(255, 255, 255, 40);\n"
                                                  "border-radius: 7px;\n"
                                                  "color: rgb(255, 255, 255);\n"
                                                  "font: 12pt \"MS Shell Dlg 2\";")
        self.balance_category_frame.setObjectName("balance_category_frame")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.balance_category_frame)
        self.horizontalLayout_9.setContentsMargins(1, -1, -1, -1)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.Balance_frame = QtWidgets.QFrame(parent=self.balance_category_frame)
        self.Balance_frame.setStyleSheet("background-color: rgba(255, 255, 255, 30);\n"
                                         "border: 1px solid rgba(255, 255, 255, 40);\n"
                                         "border-radius: 7px;")
        self.Balance_frame.setObjectName("Balance_frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.Balance_frame)
        self.verticalLayout.setContentsMargins(12, 12, 12, 12)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.currentBalance = QtWidgets.QLabel(parent=self.Balance_frame)
        self.currentBalance.setStyleSheet("color: rgb(255, 255, 255);\n"
                                          "font: 75 30pt \"MS Shell Dlg 2\";\n"
                                          "background-color: none;\n"
                                          "border: none;\n"
                                          "font-weight: bold;\n"
                                          "")
        self.currentBalance.setObjectName("currentBalance")
        self.verticalLayout.addWidget(self.currentBalance)
        self.moneyCurrentBalance = QtWidgets.QLabel(parent=self.Balance_frame)
        self.moneyCurrentBalance.setStyleSheet("color: rgb(255, 255, 255);\n"
                                               "font: 75 24pt \"MS Shell Dlg 2\";\n"
                                               "background-color: none;\n"
                                               "border: none;\n"
                                               "")
        self.moneyCurrentBalance.setObjectName("moneyCurrentBalance")
        self.verticalLayout.addWidget(self.moneyCurrentBalance)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(parent=self.Balance_frame)
        self.label_2.setMaximumSize(QtCore.QSize(30, 16777215))
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "background-color:none;\n"
                                   "border: none;\n"
                                   "font-weight: bold;\n"
                                   "padding-top: 5px;")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/icon/icons/income.svg"))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.earn = QtWidgets.QLabel(parent=self.Balance_frame)
        self.earn.setStyleSheet("color: rgb(255, 255, 255);\n"
                                "font: 75 22pt \"MS Shell Dlg 2\";\n"
                                "background-color: none;\n"
                                "border: none;\n"
                                "padding-top: 5px;\n"
                                "")
        self.earn.setObjectName("earn")
        self.horizontalLayout.addWidget(self.earn)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.earnBalance = QtWidgets.QLabel(parent=self.Balance_frame)
        self.earnBalance.setStyleSheet("color: rgb(255, 255, 255);\n"
                                       "font: 75 18pt \"MS Shell Dlg 2\";\n"
                                       "background-color: none;\n"
                                       "border: none;\n"
                                       "")
        self.earnBalance.setObjectName("earnBalance")
        self.verticalLayout.addWidget(self.earnBalance)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_5 = QtWidgets.QLabel(parent=self.Balance_frame)
        self.label_5.setMaximumSize(QtCore.QSize(30, 16777215))
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "background-color:none;\n"
                                   "border: none;\n"
                                   "font-weight: bold;\n"
                                   "padding-top: 5px;")
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap(":/icon/icons/outcome.svg"))
        self.label_5.setObjectName("questionLabel")
        self.horizontalLayout_2.addWidget(self.label_5)
        self.spend = QtWidgets.QLabel(parent=self.Balance_frame)
        self.spend.setStyleSheet("color: rgb(255, 255, 255);\n"
                                 "font: 75 22pt \"MS Shell Dlg 2\";\n"
                                 "background-color: none;\n"
                                 "border: none;\n"
                                 "padding-top: 5px;\n"
                                 "")
        self.spend.setObjectName("spend")
        self.horizontalLayout_2.addWidget(self.spend)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.spendBalance = QtWidgets.QLabel(parent=self.Balance_frame)
        self.spendBalance.setStyleSheet("color: rgb(255, 255, 255);\n"
                                        "font: 75 18pt \"MS Shell Dlg 2\";\n"
                                        "background-color: none;\n"
                                        "border: none;\n"
                                        "")
        self.spendBalance.setObjectName("spendBalance")
        self.verticalLayout.addWidget(self.spendBalance)
        self.horizontalLayout_9.addWidget(self.Balance_frame)
        self.category_frame = QtWidgets.QFrame(parent=self.balance_category_frame)
        self.category_frame.setStyleSheet("background-color: rgba(255, 255, 255, 15);\n"
                                          "border: 1px solid rgba(255, 255, 255, 30);\n"
                                          "border-radius: 7px;")
        self.category_frame.setObjectName("category_frame")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.category_frame)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.spend_frame = QtWidgets.QFrame(parent=self.category_frame)
        self.spend_frame.setObjectName("spend_frame")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.spend_frame)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_8 = QtWidgets.QLabel(parent=self.spend_frame)
        self.label_8.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "font: 75 18pt \"MS Shell Dlg 2\";\n"
                                   "background-color: none;\n"
                                   "border: none;")
        self.label_8.setObjectName("headLabel")
        self.verticalLayout_5.addWidget(self.label_8)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_10 = QtWidgets.QLabel(parent=self.spend_frame)
        self.label_10.setMaximumSize(QtCore.QSize(30, 16777215))
        self.label_10.setStyleSheet("color: rgb(255, 255, 255);\n"
                                    "background-color:none;\n"
                                    "border: none;")
        self.label_10.setText("")
        self.label_10.setPixmap(QtGui.QPixmap(":/icon/icons/health.svg"))
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_8.addWidget(self.label_10)
        self.label_11 = QtWidgets.QLabel(parent=self.spend_frame)
        self.label_11.setMinimumSize(QtCore.QSize(210, 0))
        self.label_11.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_11.setStyleSheet("color: rgb(255, 255, 255);\n"
                                    "background-color:none;\n"
                                    "border: none;")
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_8.addWidget(self.label_11)
        self.healthMoney = QtWidgets.QLabel(parent=self.spend_frame)
        self.healthMoney.setStyleSheet("color: rgb(255, 255, 255);\n"
                                       "background-color:none;\n"
                                       "border: none;")
        self.healthMoney.setObjectName("healthMoney")
        self.horizontalLayout_8.addWidget(self.healthMoney)
        self.verticalLayout_5.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_13 = QtWidgets.QLabel(parent=self.spend_frame)
        self.label_13.setMaximumSize(QtCore.QSize(30, 16777215))
        self.label_13.setStyleSheet("color: rgb(255, 255, 255);\n"
                                    "background-color:none;\n"
                                    "border: none;")
        self.label_13.setText("")
        self.label_13.setPixmap(QtGui.QPixmap(":/icon/icons/food.svg"))
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_7.addWidget(self.label_13)
        self.label_15 = QtWidgets.QLabel(parent=self.spend_frame)
        self.label_15.setMinimumSize(QtCore.QSize(210, 0))
        self.label_15.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_15.setStyleSheet("color: rgb(255, 255, 255);\n"
                                    "background-color:none;\n"
                                    "border: none;")
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_7.addWidget(self.label_15)
        self.foodMoney = QtWidgets.QLabel(parent=self.spend_frame)
        self.foodMoney.setStyleSheet("color: rgb(255, 255, 255);\n"
                                     "background-color:none;\n"
                                     "border: none;")
        self.foodMoney.setObjectName("foodMoney")
        self.horizontalLayout_7.addWidget(self.foodMoney)
        self.verticalLayout_5.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_16 = QtWidgets.QLabel(parent=self.spend_frame)
        self.label_16.setMaximumSize(QtCore.QSize(30, 16777215))
        self.label_16.setStyleSheet("color: rgb(255, 255, 255);\n"
                                    "background-color:none;\n"
                                    "border: none;")
        self.label_16.setText("")
        self.label_16.setPixmap(QtGui.QPixmap(":/icon/icons/enjoy.svg"))
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_6.addWidget(self.label_16)
        self.label_18 = QtWidgets.QLabel(parent=self.spend_frame)
        self.label_18.setMinimumSize(QtCore.QSize(210, 0))
        self.label_18.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_18.setStyleSheet("color: rgb(255, 255, 255);\n"
                                    "background-color:none;\n"
                                    "border: none;")
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_6.addWidget(self.label_18)
        self.funMoney = QtWidgets.QLabel(parent=self.spend_frame)
        self.funMoney.setStyleSheet("color: rgb(255, 255, 255);\n"
                                    "background-color:none;\n"
                                    "border: none;")
        self.funMoney.setObjectName("funMoney")
        self.horizontalLayout_6.addWidget(self.funMoney)
        self.verticalLayout_5.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_25 = QtWidgets.QLabel(parent=self.spend_frame)
        self.label_25.setMaximumSize(QtCore.QSize(30, 16777215))
        self.label_25.setStyleSheet("color: rgb(255, 255, 255);\n"
                                    "background-color:none;\n"
                                    "border: none;")
        self.label_25.setText("")
        self.label_25.setPixmap(QtGui.QPixmap(":/icon/icons/gift.svg"))
        self.label_25.setObjectName("label_25")
        self.horizontalLayout_3.addWidget(self.label_25)
        self.label_27 = QtWidgets.QLabel(parent=self.spend_frame)
        self.label_27.setMinimumSize(QtCore.QSize(210, 0))
        self.label_27.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_27.setStyleSheet("color: rgb(255, 255, 255);\n"
                                    "background-color:none;\n"
                                    "border: none;")
        self.label_27.setObjectName("label_27")
        self.horizontalLayout_3.addWidget(self.label_27)
        self.giftSpendMoney = QtWidgets.QLabel(parent=self.spend_frame)
        self.giftSpendMoney.setStyleSheet("color: rgb(255, 255, 255);\n"
                                          "background-color:none;\n"
                                          "border: none;")
        self.giftSpendMoney.setObjectName("giftSpendMoney")
        self.horizontalLayout_3.addWidget(self.giftSpendMoney)
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_19 = QtWidgets.QLabel(parent=self.spend_frame)
        self.label_19.setMaximumSize(QtCore.QSize(30, 16777215))
        self.label_19.setStyleSheet("color: rgb(255, 255, 255);\n"
                                    "background-color:none;\n"
                                    "border: none;")
        self.label_19.setText("")
        self.label_19.setPixmap(QtGui.QPixmap(":/icon/icons/other.svg"))
        self.label_19.setObjectName("label_19")
        self.horizontalLayout_5.addWidget(self.label_19)
        self.label_21 = QtWidgets.QLabel(parent=self.spend_frame)
        self.label_21.setMinimumSize(QtCore.QSize(210, 0))
        self.label_21.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_21.setStyleSheet("color: rgb(255, 255, 255);\n"
                                    "background-color:none;\n"
                                    "border: none;")
        self.label_21.setObjectName("label_21")
        self.horizontalLayout_5.addWidget(self.label_21)
        self.otherSpendMoney = QtWidgets.QLabel(parent=self.spend_frame)
        self.otherSpendMoney.setStyleSheet("color: rgb(255, 255, 255);\n"
                                           "background-color:none;\n"
                                           "border: none;")
        self.otherSpendMoney.setObjectName("otherSpendMoney")
        self.horizontalLayout_5.addWidget(self.otherSpendMoney)
        self.verticalLayout_5.addLayout(self.horizontalLayout_5)
        self.verticalLayout_6.addWidget(self.spend_frame)
        self.earn_frame = QtWidgets.QFrame(parent=self.category_frame)
        self.earn_frame.setObjectName("earn_frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.earn_frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_55 = QtWidgets.QLabel(parent=self.earn_frame)
        self.label_55.setStyleSheet("color: rgb(255, 255, 255);\n"
                                    "font: 75 18pt \"MS Shell Dlg 2\";\n"
                                    "background-color: none;\n"
                                    "border: none;")
        self.label_55.setObjectName("label_55")
        self.verticalLayout_2.addWidget(self.label_55)
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.label_59 = QtWidgets.QLabel(parent=self.earn_frame)
        self.label_59.setMaximumSize(QtCore.QSize(30, 16777215))
        self.label_59.setStyleSheet("color: rgb(255, 255, 255);\n"
                                    "background-color:none;\n"
                                    "border: none;")
        self.label_59.setText("")
        self.label_59.setPixmap(QtGui.QPixmap(":/icon/icons/work.svg"))
        self.label_59.setObjectName("label_59")
        self.horizontalLayout_20.addWidget(self.label_59)
        self.label_60 = QtWidgets.QLabel(parent=self.earn_frame)
        self.label_60.setMinimumSize(QtCore.QSize(210, 0))
        self.label_60.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_60.setStyleSheet("color: rgb(255, 255, 255);\n"
                                    "background-color:none;\n"
                                    "border: none;")
        self.label_60.setObjectName("label_60")
        self.horizontalLayout_20.addWidget(self.label_60)
        self.jobMoney = QtWidgets.QLabel(parent=self.earn_frame)
        self.jobMoney.setStyleSheet("color: rgb(255, 255, 255);\n"
                                    "background-color:none;\n"
                                    "border: none;")
        self.jobMoney.setObjectName("jobMoney")
        self.horizontalLayout_20.addWidget(self.jobMoney)
        self.verticalLayout_2.addLayout(self.horizontalLayout_20)
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.label_62 = QtWidgets.QLabel(parent=self.earn_frame)
        self.label_62.setMaximumSize(QtCore.QSize(30, 16777215))
        self.label_62.setStyleSheet("color: rgb(255, 255, 255);\n"
                                    "background-color:none;\n"
                                    "border: none;")
        self.label_62.setText("")
        self.label_62.setPixmap(QtGui.QPixmap(":/icon/icons/bank.svg"))
        self.label_62.setObjectName("label_62")
        self.horizontalLayout_21.addWidget(self.label_62)
        self.label_63 = QtWidgets.QLabel(parent=self.earn_frame)
        self.label_63.setMinimumSize(QtCore.QSize(210, 0))
        self.label_63.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_63.setStyleSheet("color: rgb(255, 255, 255);\n"
                                    "background-color:none;\n"
                                    "border: none;")
        self.label_63.setObjectName("label_63")
        self.horizontalLayout_21.addWidget(self.label_63)
        self.bankMoney = QtWidgets.QLabel(parent=self.earn_frame)
        self.bankMoney.setStyleSheet("color: rgb(255, 255, 255);\n"
                                     "background-color:none;\n"
                                     "border: none;")
        self.bankMoney.setObjectName("bankMoney")
        self.horizontalLayout_21.addWidget(self.bankMoney)
        self.verticalLayout_2.addLayout(self.horizontalLayout_21)
        self.horizontalLayout_23 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_23.setObjectName("horizontalLayout_23")
        self.label_68 = QtWidgets.QLabel(parent=self.earn_frame)
        self.label_68.setMaximumSize(QtCore.QSize(30, 16777215))
        self.label_68.setStyleSheet("color: rgb(255, 255, 255);\n"
                                    "background-color:none;\n"
                                    "border: none;")
        self.label_68.setText("")
        self.label_68.setPixmap(QtGui.QPixmap(":/icon/icons/gift.svg"))
        self.label_68.setObjectName("label_68")
        self.horizontalLayout_23.addWidget(self.label_68)
        self.label_69 = QtWidgets.QLabel(parent=self.earn_frame)
        self.label_69.setMinimumSize(QtCore.QSize(210, 0))
        self.label_69.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_69.setStyleSheet("color: rgb(255, 255, 255);\n"
                                    "background-color:none;\n"
                                    "border: none;")
        self.label_69.setObjectName("label_69")
        self.horizontalLayout_23.addWidget(self.label_69)
        self.giftEarnMoney = QtWidgets.QLabel(parent=self.earn_frame)
        self.giftEarnMoney.setStyleSheet("color: rgb(255, 255, 255);\n"
                                         "background-color:none;\n"
                                         "border: none;")
        self.giftEarnMoney.setObjectName("giftEarnMoney")
        self.horizontalLayout_23.addWidget(self.giftEarnMoney)
        self.verticalLayout_2.addLayout(self.horizontalLayout_23)
        self.horizontalLayout_24 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_24.setObjectName("horizontalLayout_24")
        self.label_56 = QtWidgets.QLabel(parent=self.earn_frame)
        self.label_56.setMaximumSize(QtCore.QSize(30, 16777215))
        self.label_56.setStyleSheet("color: rgb(255, 255, 255);\n"
                                    "background-color:none;\n"
                                    "border: none;")
        self.label_56.setText("")
        self.label_56.setPixmap(QtGui.QPixmap(":/icon/icons/other.svg"))
        self.label_56.setObjectName("label_56")
        self.horizontalLayout_24.addWidget(self.label_56)
        self.label_24 = QtWidgets.QLabel(parent=self.earn_frame)
        self.label_24.setMinimumSize(QtCore.QSize(210, 0))
        self.label_24.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_24.setStyleSheet("color: rgb(255, 255, 255);\n"
                                    "background-color:none;\n"
                                    "border: none;")
        self.label_24.setObjectName("label_24")
        self.horizontalLayout_24.addWidget(self.label_24)
        self.otherEarnMoney = QtWidgets.QLabel(parent=self.earn_frame)
        self.otherEarnMoney.setStyleSheet("color: rgb(255, 255, 255);\n"
                                          "background-color:none;\n"
                                          "border: none;")
        self.otherEarnMoney.setObjectName("otherEarnMoney")
        self.horizontalLayout_24.addWidget(self.otherEarnMoney)
        self.verticalLayout_2.addLayout(self.horizontalLayout_24)
        self.verticalLayout_6.addWidget(self.earn_frame)
        self.horizontalLayout_9.addWidget(self.category_frame)
        self.verticalLayout_3.addWidget(self.balance_category_frame)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.newTransactionButton = QtWidgets.QPushButton(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.newTransactionButton.setFont(font)
        self.newTransactionButton.setStyleSheet("QPushButton {\n"
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
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/icons/add.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.newTransactionButton.setIcon(icon)
        self.newTransactionButton.setIconSize(QtCore.QSize(20, 20))
        self.newTransactionButton.setObjectName("newTransactionButton")
        self.horizontalLayout_10.addWidget(self.newTransactionButton)
        self.newTransactionButton_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.newTransactionButton_2.setFont(font)
        self.newTransactionButton_2.setStyleSheet("QPushButton {\n"
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
        self.newTransactionButton_2.setIcon(icon)
        self.newTransactionButton_2.setIconSize(QtCore.QSize(20, 20))
        self.newTransactionButton_2.setObjectName("newTransactionButton_2")
        self.horizontalLayout_10.addWidget(self.newTransactionButton_2)
        self.label_23 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_23.setStyleSheet("color: rgb(255, 255, 255);\n"
                                    "font: 75 14pt \"MS Shell Dlg 2\";\n"
                                    "background-color: none;\n"
                                    "border: none;")
        self.label_23.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignRight | QtCore.Qt.AlignmentFlag.AlignTrailing | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_23.setObjectName("label_23")
        self.horizontalLayout_10.addWidget(self.label_23)
        self.sortComboBox = QtWidgets.QComboBox(parent=self.centralwidget)
        self.sortComboBox.setStyleSheet("\n"
                                        "QComboBox {\n"
                                        "color: rgb(255, 255, 255);\n"
                                        "background-color: qlineargradient(spread:reflect, x1:0.549682, y1:0.494, x2:0, y2:0, stop:0 rgba(0, 18, 221, 150), stop:1 rgba(179, 0, 241, 150));;\n"
                                        "border: 1px solid rgba(255, 255, 255, 50);\n"
                                        "border-radius: 7px;\n"
                                        "    font: 14pt \"MS Shell Dlg 2\";\n"
                                        "}\n"
                                        "")
        self.sortComboBox.setObjectName("sortComboBox")
        self.sortComboBox.addItem("")
        self.sortComboBox.addItem("")
        self.sortComboBox.addItem("")
        self.sortComboBox.addItem("")
        self.horizontalLayout_10.addWidget(self.sortComboBox)
        self.deleteButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.deleteButton.setStyleSheet("QPushButton {\n"
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
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icon/icons/delete.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.deleteButton.setIcon(icon1)
        self.deleteButton.setIconSize(QtCore.QSize(20, 20))
        self.deleteButton.setObjectName("deleteButton")
        self.horizontalLayout_10.addWidget(self.deleteButton)
        self.verticalLayout_3.addLayout(self.horizontalLayout_10)

        self.excelButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.excelButton.setStyleSheet("QPushButton {\n"
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
        self.excelButton.setIcon(icon1)
        self.excelButton.setIconSize(QtCore.QSize(20, 20))
        self.excelButton.setObjectName("excelButton")
        self.horizontalLayout_10.addWidget(self.excelButton)
        self.verticalLayout_3.addLayout(self.horizontalLayout_10)
        self.tableWidget = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.tableWidget.setStyleSheet("QTableWidget {\n"
                                       "    background-color: rgba(255, 255, 255, 30);\n"
                                       "    border: none;\n"
                                       "    border-bottom-left-radius: 7px;\n"
                                       "    border-bottom-right-radius: 7px;\n"
                                       "}\n"
                                       "\n"
                                       "QTableWidget::corner {\n"
                                       "    background-color: transparent;\n"
                                       "    border: none;\n"
                                       "}\n"
                                       "\n"
                                       "QTableWidget::item {\n"
                                       "    border-style: none;\n"
                                       "    border-bottom: rgba(255, 255, 255, 50);\n"
                                       "}\n"
                                       "\n"
                                       "QTableWidget::item:selected {\n"
                                       "    border: none;\n"
                                       "    color: rgb(255, 255, 255);\n"
                                       "    background-color: rgba(255, 255, 255, 50);\n"
                                       "}\n"
                                       "\n"
                                       "QHeaderView::section {\n"
                                       "    background-color: rgba(0, 0, 0, 30);\n"
                                       "    color: white;\n"
                                       "    font-size: 14px;\n"
                                       "    padding: 8px;\n"
                                       "    selection-background-color: transparent;\n"
                                       "    selection-color: transparent; \n"
                                       "}\n"
                                       "")
        self.tableWidget.setObjectName("tableWidget")

        self.verticalLayout_3.addWidget(self.tableWidget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.accs = self.db_manager.get_bank_data(self.familly_id)

        self.render_familly_members()
        self.infoBankAccButton.clicked.connect(self.info_user_bank_data)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "WalletWise: Family Finance Tracker"))
        self.changeFamilyButton.setText(_translate("MainWindow", "Сменить аккаунт"))
        self.addBankAccButton.setText(_translate("MainWindow", "Добавить счет"))
        self.delBankAccButton.setText(_translate("MainWindow", "Удалить счет"))
        self.label_22.setText(_translate("MainWindow", "Владелец текущего счета:"))
        self.infoBankAccButton.setText(_translate("MainWindow", "Информация о текущем счете"))
        self.currentBalance.setText(_translate("MainWindow", "Текущий баланс"))
        self.moneyCurrentBalance.setText(_translate("MainWindow", "1221 рублей"))
        self.earn.setText(_translate("MainWindow", "Поступления"))
        self.earnBalance.setText(_translate("MainWindow", "12321 рублей"))
        self.spend.setText(_translate("MainWindow", "Расходы"))
        self.spendBalance.setText(_translate("MainWindow", "23 рублей"))
        self.label_8.setText(_translate("MainWindow", "Расходы по категориям"))
        self.label_11.setText(_translate("MainWindow", "Здоровье"))
        self.healthMoney.setText(_translate("MainWindow", "money"))
        self.label_15.setText(_translate("MainWindow", "Еда"))
        self.foodMoney.setText(_translate("MainWindow", "money"))
        self.label_18.setText(_translate("MainWindow", "Развлечения"))
        self.funMoney.setText(_translate("MainWindow", "money"))
        self.label_27.setText(_translate("MainWindow", "Подарки"))
        self.giftSpendMoney.setText(_translate("MainWindow", "money"))
        self.label_21.setText(_translate("MainWindow", "Другое"))
        self.otherSpendMoney.setText(_translate("MainWindow", "money"))
        self.label_55.setText(_translate("MainWindow", "Доходы по категориям"))
        self.label_60.setText(_translate("MainWindow", "Работа"))
        self.jobMoney.setText(_translate("MainWindow", "money"))
        self.label_63.setText(_translate("MainWindow", "Акции, вклады, облигации"))
        self.bankMoney.setText(_translate("MainWindow", "money"))
        self.label_69.setText(_translate("MainWindow", "Подарки"))
        self.giftEarnMoney.setText(_translate("MainWindow", "money1"))
        self.label_24.setText(_translate("MainWindow", "Другое"))
        self.otherEarnMoney.setText(_translate("MainWindow", "money1"))
        self.newTransactionButton.setText(_translate("MainWindow", "Добавить доход"))
        self.newTransactionButton_2.setText(_translate("MainWindow", "Добавить расход"))
        self.label_23.setText(_translate("MainWindow", "Cортировать по:"))
        self.sortComboBox.setItemText(0, _translate("MainWindow", "Сумме"))
        self.sortComboBox.setItemText(1, _translate("MainWindow", "Категории"))
        self.sortComboBox.setItemText(2, _translate("MainWindow", "Дате (снач. старые)"))
        self.sortComboBox.setItemText(3, _translate("MainWindow", "Дате (снач. новые)"))
        self.deleteButton.setText(_translate("MainWindow", "Удалить транзакцию"))
        self.excelButton.setText(_translate("MainWindow", "Вывести в excel"))

        self.addBankAccButton.clicked.connect(self.add_bank)
        self.changePersonComboBox.currentTextChanged.connect(self.render_main_info)

        self.newTransactionButton.clicked.connect(self.add_tr_in)
        self.newTransactionButton_2.clicked.connect(self.add_tr_out)
        self.deleteButton.clicked.connect(self.rm_tr)

        self.tableWidget.setColumnCount(5)
        self.tableWidget.setSelectionBehavior(QtWidgets.QTableWidget.SelectionBehavior.SelectRows)
        self.tableWidget.setSelectionBehavior(QtWidgets.QTableWidget.SelectionBehavior.SelectRows)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)
        self.tableWidget.setHorizontalHeaderLabels(
            ['Цена', 'Дата', 'Подробности', 'Категория', "Тип транзакции"])
        self.tableWidget.verticalHeader().hide()

        self.sortComboBox.currentTextChanged.connect(self.render_trans)

        self.delBankAccButton.clicked.connect(self.rm_bank_acc)
        self.changeFamilyButton.clicked.connect(self.reg_or_log_sh)
        self.excelButton.clicked.connect(self.export_excel_file)





    def render_trans(self):
        self.transs = self.db_manager.select_tr(self.current_acc()[0])

        if self.sortComboBox.currentText() == "Сумме":
            self.transs = sorted(self.transs, key=lambda x: x[1])[::-1]

        if self.sortComboBox.currentText() == "Категории":
            self.transs = sorted(self.transs, key=lambda x: x[4])

        if self.sortComboBox.currentText() == "Дате (снач. старые)":
            self.transs = sorted(self.transs, key=lambda x: datetime.strptime(x[2], '%Y-%m-%d').date())

        if self.sortComboBox.currentText() == "Дате (снач. новые)":
            self.transs = sorted(self.transs, key=lambda x: datetime.strptime(x[2], '%Y-%m-%d').date())[::-1]

        for i in self.transs:
            print(i)
        self.tableWidget.setRowCount(len(self.transs))
        for row in range(len(self.transs)):
            for col in range(self.tableWidget.columnCount()):
                value = self.transs[row][col + 1]
                if col == 4:
                    value = "Доход" if int(self.transs[row][5]) == 1 else "Расход"
                item = QtWidgets.QTableWidgetItem(f'{value}')
                self.tableWidget.setItem(row, col, item)

    def current_acc(self):
        return self.accs[self.changePersonComboBox.currentIndex()]

    def reg_or_log_sh(self):
        from RegOrLog import RegLogWindow
        self.reg_or_log = RegLogWindow()
        self.reg_or_log.show()
        self.close()

    def rm_bank_acc(self):

        user = self.current_acc()
        self.db_manager.remove_bank_acc(user[0])
        self.render_familly_members()
        self.render_main_info()

    def render_familly_members(self):
        self.changePersonComboBox.clear()
        self.accs = self.db_manager.get_bank_data(self.familly_id)
        if self.accs is None:
            from NewBankAcc import BankAccWin
            self.bank_acc_dialog = BankAccWin(self.familly_id, is_registration=False)
            self.bank_acc_dialog.show()
        for i in self.accs:
            self.changePersonComboBox.addItem(i[1])
        if self.changePersonComboBox.count() == 1:
            self.delBankAccButton.hide()
        else:
            self.delBankAccButton.show()


    def rm_tr(self):
        try:
            if self.tableWidget.item(self.tableWidget.currentRow(), 0).text() != 'Цена':
                for i in self.transs:
                    if self.tableWidget.item(self.tableWidget.currentRow(), 0).text() == str(i[1]) and \
                            self.tableWidget.item(self.tableWidget.currentRow(), 1).text() == str(i[2]) and \
                            self.tableWidget.item(self.tableWidget.currentRow(), 2).text() == str(i[3]) and \
                            self.tableWidget.item(self.tableWidget.currentRow(), 3).text() == str(i[4]):
                        self.db_manager.remove_tr(i[1], i[2], i[3], i[4])
                self.render_trans()
                self.render_main_info()
        except:
            msg = MessageBox(self)
            msg.show_message(f"Предупреждение", f"Выберите одину из строк в таблице нажав на любой элемент входящий в нее.", MessageBox.Icon.Warning)

    def render_main_info(self):
        if self.changePersonComboBox.count() == 1:
            self.delBankAccButton.hide()
        else:
            self.delBankAccButton.show()
        user = self.current_acc()
        if user is None:
            user = self.accs[0]
            self.changePersonComboBox.setCurrentIndex(0)

        print(user)

        doh = self.db_manager.select_sum_d(user[0])
        rash = self.db_manager.select_sum_r(user[0])

        self.moneyCurrentBalance.setText(f"{user[3] + doh - rash} рублей")
        self.earnBalance.setText(f"{doh} рублей")
        self.spendBalance.setText(f"{rash} рублей")
        self.render_trans()
        d_cat = self.db_manager.select_sum_d_cat(user[0])
        r_cat = self.db_manager.select_sum_r_cat(user[0])

        labels_d = [self.bankMoney, self.otherEarnMoney, self.giftEarnMoney, self.jobMoney]
        labels_r = [self.otherSpendMoney, self.foodMoney, self.healthMoney, self.giftSpendMoney, self.funMoney]

        for i in range(len(labels_d)):
            labels_d[i].setText(str(d_cat[i][0]))
        for i in range(len(labels_r)):
            labels_r[i].setText(str(r_cat[i][0]))


    def info_user_bank_data(self):
        user = self.current_acc()
        msg = MessageBox(self)
        msg.show_message(f"Информация о счете: {user[1]}", f"Аккаунт: {user[2]}", MessageBox.Icon.Information)

    def add_tr_out(self):
        self.new_tr = NewTransaction(self.current_acc()[0], 0)
        self.new_tr.save_pushButton.clicked.connect(self.render_trans)
        self.new_tr.save_pushButton.clicked.connect(self.render_main_info)
        self.new_tr.show()

    def add_tr_in(self):
        self.new_tr = NewTransaction(self.current_acc()[0], 1)
        self.new_tr.save_pushButton.clicked.connect(self.render_trans)
        self.new_tr.save_pushButton.clicked.connect(self.render_main_info)
        self.new_tr.show()

    def add_bank(self):
        from NewBankAcc import BankAccWin
        self.hide()
        self.addBank = BankAccWin(self.familly_id)
        self.addBank.show()

    def export_excel_file(self):
        from message_box import MessageBox
        from report_generator import ReportGenerator
        """pass
        
        идея такая: 
        лист1: реализовать вывод диаграмм с общей статистикой, всего 4 диаграммы, 2 доходы, 2 расходы
        одна с доходами отображает членов семьи, показывает в процентном соотношении кто сколько зааботал
        вторая с доходами всей семьи по категории, то есть идет группировка по категориям для всех членов семьи,
        где в процентном соотношении показывается по каким категориям семья заработала сколько
        аналогичные диаграммы для расходов
        
        лист2: реализовать вывод в excel диаграмм по расходам и доходам раздельно
        то есть вывести круговую диаграмму "Доходы" в которой будет содержаться закрашенные 
        части означающие процент доходов и расходов по данной категории. Аналогично выводится по расходам
        выводится для каждого члена семьи раздельно
        
        """
        try:
            report_generator = ReportGenerator(self.db_manager)

            # Генерация диаграмм и отчета
            report_generator.generate_family_income_chart()
            report_generator.generate_family_category_chart()
            report_generator.generate_individual_charts()
            report_generator.generate_excel_report()

            from message_box import MessageBox
            success_msg = MessageBox(self)
            success_msg.show_message("Успех", "Экспорт выполнен успешно.", MessageBox.Icon.Information)

        except Exception as e:
            print("Ошибка при экспорте в Excel:", e)
            error_msg = MessageBox(self)
            error_msg.show_message("Ошибка", "Произошла ошибка при экспорте в Excel.", MessageBox.Icon.Critical)