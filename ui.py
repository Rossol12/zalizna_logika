import random


from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from ui import Ui_MainWindow




class Widget(QMainWindow):
   def __init__(self):
       super().__init__()
       self.ui = Ui_MainWindow()
       self.ui.setupUi(self)
       self.ui.pushButton.clicked.connect(self.example)


   def example(self):
       signs = ''
       if self.ui.checkBox.isChecked():
           signs = 'qwertyuiopsdfghjklzxcvbnm'
       if self.ui.checkBox_2.isChecked():
           signs += '0123456789'
      
       result = ''
       number = random.randint(5, 10)
       for i in range(number):
           result += random.choice(signs)
      
       self.ui.label_2.setText(result)


app = QApplication([])
ex = Widget()
ex.show()
app.exec_()
from PyQt5 import QtCore, QtGui, QtWidgets




class Ui_MainWindow(object):
   def setupUi(self, MainWindow):
       MainWindow.setObjectName("MainWindow")
       MainWindow.resize(246, 232)
       self.centralwidget = QtWidgets.QWidget(MainWindow)
       self.centralwidget.setObjectName("centralwidget")
       self.label = QtWidgets.QLabel(self.centralwidget)
       self.label.setGeometry(QtCore.QRect(30, 20, 195, 24))
       font = QtGui.QFont()
       font.setPointSize(12)
       font.setBold(True)
       font.setWeight(75)
       self.label.setFont(font)
       self.label.setObjectName("label")
       self.label_2 = QtWidgets.QLabel(self.centralwidget)
       self.label_2.setGeometry(QtCore.QRect(30, 60, 112, 16))
       self.label_2.setObjectName("label_2")
       self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
       self.checkBox.setGeometry(QtCore.QRect(30, 90, 178, 20))
       self.checkBox.setObjectName("checkBox")
       self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
       self.checkBox_2.setGeometry(QtCore.QRect(30, 130, 165, 20))
       self.checkBox_2.setObjectName("checkBox_2")
       self.pushButton = QtWidgets.QPushButton(self.centralwidget)
       self.pushButton.setGeometry(QtCore.QRect(70, 180, 93, 28))
       self.pushButton.setStyleSheet("background-color: white;\n"
"border: 1px solid #222222;\n"
"border-radius: 8px")
       self.pushButton.setObjectName("pushButton")
       MainWindow.setCentralWidget(self.centralwidget)


       self.retranslateUi(MainWindow)
       QtCore.QMetaObject.connectSlotsByName(MainWindow)


   def retranslateUi(self, MainWindow):
       _translate = QtCore.QCoreApplication.translate
       MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
       self.label.setText(_translate("MainWindow", "Генератор паролів"))
       self.label_2.setText(_translate("MainWindow", "тут буде результат"))
       self.checkBox.setText(_translate("MainWindow", "Використовувати алфавіт"))
       self.checkBox_2.setText(_translate("MainWindow", "Використовувати числа"))
       self.pushButton.setText(_translate("MainWindow", "Сгенерувати"))




if __name__ == "__main__":
   import sys
   app = QtWidgets.QApplication(sys.argv)
   MainWindow = QtWidgets.QMainWindow()
   ui = Ui_MainWindow()
   ui.setupUi(MainWindow)
   MainWindow.show()
   sys.exit(app.exec_())
