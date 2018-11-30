# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Shop.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_InGame4(object):
    def setupUi(self, InGame4):
        InGame4.setObjectName("InGame4")
        InGame4.resize(960, 540)
        self.graphicsView = QtWidgets.QGraphicsView(InGame4)
        self.graphicsView.setGeometry(QtCore.QRect(60, 260, 831, 192))
        self.graphicsView.setObjectName("graphicsView")
        self.lineEdit = QtWidgets.QLineEdit(InGame4)
        self.lineEdit.setGeometry(QtCore.QRect(50, 470, 851, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.progressBar = QtWidgets.QProgressBar(InGame4)
        self.progressBar.setGeometry(QtCore.QRect(80, 220, 791, 23))
        self.progressBar.setProperty("value", 50)
        self.progressBar.setTextVisible(False)
        self.progressBar.setObjectName("progressBar")
        self.graphicsView_2 = QtWidgets.QGraphicsView(InGame4)
        self.graphicsView_2.setGeometry(QtCore.QRect(80, 80, 161, 131))
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.graphicsView_3 = QtWidgets.QGraphicsView(InGame4)
        self.graphicsView_3.setGeometry(QtCore.QRect(710, 80, 161, 131))
        self.graphicsView_3.setObjectName("graphicsView_3")
        self.graphicsView_4 = QtWidgets.QGraphicsView(InGame4)
        self.graphicsView_4.setGeometry(QtCore.QRect(290, 80, 161, 131))
        self.graphicsView_4.setObjectName("graphicsView_4")
        self.graphicsView_5 = QtWidgets.QGraphicsView(InGame4)
        self.graphicsView_5.setGeometry(QtCore.QRect(500, 80, 161, 131))
        self.graphicsView_5.setObjectName("graphicsView_5")
        self.pushButton = QtWidgets.QPushButton(InGame4)
        self.pushButton.setGeometry(QtCore.QRect(10, 10, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(InGame4)
        self.pushButton_2.setGeometry(QtCore.QRect(860, 10, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.lcdNumber = QtWidgets.QLCDNumber(InGame4)
        self.lcdNumber.setGeometry(QtCore.QRect(80, 40, 151, 31))
        self.lcdNumber.setObjectName("lcdNumber")
        self.lcdNumber_2 = QtWidgets.QLCDNumber(InGame4)
        self.lcdNumber_2.setGeometry(QtCore.QRect(290, 40, 161, 31))
        self.lcdNumber_2.setObjectName("lcdNumber_2")

        self.retranslateUi(InGame4)
        QtCore.QMetaObject.connectSlotsByName(InGame4)

    def retranslateUi(self, InGame4):
        _translate = QtCore.QCoreApplication.translate
        InGame4.setWindowTitle(_translate("InGame4", "Dialog"))
        self.pushButton.setText(_translate("InGame4", "상점"))
        self.pushButton_2.setText(_translate("InGame4", "나가기"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    InGame4 = QtWidgets.QDialog()
    ui = Ui_InGame4()
    ui.setupUi(InGame4)
    InGame4.show()
    sys.exit(app.exec_())

