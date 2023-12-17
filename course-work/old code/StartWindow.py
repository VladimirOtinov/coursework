from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMainWindow, QApplication

from database import DatabaseManager


class StartWindow(QMainWindow):
    def __init__(self):
        super(StartWindow, self).__init__()

        # Создайте объект DatabaseManager в конструкторе
        self.db_manager = DatabaseManager("budget.db")

        self.setupUi(self)

    def closeEvent(self, event):
        # Закрываем соединение с базой данных при закрытии окна
        self.db_manager.close_connection()
        event.accept()
    def setupUi(self, startWindow):
        startWindow.resize(453, 225)

        self.centralwidget = QtWidgets.QWidget(parent=startWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.nameLabel = QtWidgets.QLabel(parent=self.frame)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.nameLabel.setFont(font)
        self.nameLabel.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 18pt \"MS Shell Dlg 2\";\n"
"background-color: none;\n"
"border: none;\n"
"font-weight: bold;\n"
"")
        self.nameLabel.setObjectName("nameLabel")
        self.verticalLayout_2.addWidget(self.nameLabel)
        self.frame_2 = QtWidgets.QFrame(parent=self.frame)
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.descripLabel = QtWidgets.QLabel(parent=self.frame_2)
        self.descripLabel.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color:none;\n"
"border: none;\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.descripLabel.setObjectName("descripLabel")
        self.verticalLayout_3.addWidget(self.descripLabel)
        self.verticalLayout_2.addWidget(self.frame_2)
        self.startButton = QtWidgets.QPushButton(parent=self.frame)

        self.startButton.setObjectName("startButton")
        self.verticalLayout_2.addWidget(self.startButton)
        self.verticalLayout.addWidget(self.frame)
        startWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(startWindow)
        QtCore.QMetaObject.connectSlotsByName(startWindow)

    def retranslateUi(self, startWindow):
        _translate = QtCore.QCoreApplication.translate
        startWindow.setWindowTitle(_translate("startWindow", "WalletWise: Family Finance Tracker"))
        self.nameLabel.setText(_translate("startWindow", "Добро пожаловать в WalletWise"))
        self.descripLabel.setText(_translate("startWindow", "WalletWise: Family Finance Tracker — это приложение \n"
"для простого учета доходов и расходов всех членов \n"
"семьи"))
        self.startButton.setText(_translate("startWindow", "Начать"))

        # Прописать проверку наличия данных про пользователя.
        if self.db_manager.check_user_exists():
            self.startButton.clicked.connect(self.open_log)
        else:
            self.startButton.clicked.connect(self.open_reg)


    def open_reg(self):
        from RegWindow import RegDialog
        self.close()
        self.dlg = RegDialog()
        self.dlg.show()

    def open_log(self):
        from AuthWindow import AuthDialog
        self.close()
        self.dlg = AuthDialog()
        self.dlg.show()

    def open_reg_or_log(self):
        from RegOrLogWindow import RegLogWindow
        self.close()
        self.dlg = RegLogWindow()
        self.dlg.show()
