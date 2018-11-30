# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'InGame8.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_InGame8(object):
    def setupUi(self, InGame8):
        InGame8.setObjectName("InGame8")
        InGame8.resize(960, 540)
        self.pushButton = QtWidgets.QPushButton(InGame8)
        self.pushButton.setGeometry(QtCore.QRect(10, 10, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(InGame8)
        self.pushButton_2.setGeometry(QtCore.QRect(860, 10, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.graphicsView = QtWidgets.QGraphicsView(InGame8)
        self.graphicsView.setGeometry(QtCore.QRect(60, 260, 821, 192))
        self.graphicsView.setObjectName("graphicsView")
        self.graphicsView_2 = QtWidgets.QGraphicsView(InGame8)
        self.graphicsView_2.setGeometry(QtCore.QRect(80, 80, 81, 131))
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.lcdNumber = QtWidgets.QLCDNumber(InGame8)
        self.lcdNumber.setGeometry(QtCore.QRect(80, 40, 81, 31))
        self.lcdNumber.setObjectName("lcdNumber")
        self.lineEdit = QtWidgets.QLineEdit(InGame8)
        self.lineEdit.setGeometry(QtCore.QRect(50, 470, 841, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.progressBar = QtWidgets.QProgressBar(InGame8)
        self.progressBar.setGeometry(QtCore.QRect(80, 220, 791, 23))
        self.progressBar.setProperty("value", 50)
        self.progressBar.setTextVisible(False)
        self.progressBar.setObjectName("progressBar")
        self.lcdNumber_5 = QtWidgets.QLCDNumber(InGame8)
        self.lcdNumber_5.setGeometry(QtCore.QRect(180, 40, 81, 31))
        self.lcdNumber_5.setObjectName("lcdNumber_5")
        self.graphicsView_6 = QtWidgets.QGraphicsView(InGame8)
        self.graphicsView_6.setGeometry(QtCore.QRect(180, 80, 81, 131))
        self.graphicsView_6.setObjectName("graphicsView_6")
        self.lcdNumber_2 = QtWidgets.QLCDNumber(InGame8)
        self.lcdNumber_2.setGeometry(QtCore.QRect(280, 40, 81, 31))
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.graphicsView_3 = QtWidgets.QGraphicsView(InGame8)
        self.graphicsView_3.setGeometry(QtCore.QRect(280, 80, 81, 131))
        self.graphicsView_3.setObjectName("graphicsView_3")
        self.graphicsView_7 = QtWidgets.QGraphicsView(InGame8)
        self.graphicsView_7.setGeometry(QtCore.QRect(380, 80, 81, 131))
        self.graphicsView_7.setObjectName("graphicsView_7")
        self.lcdNumber_6 = QtWidgets.QLCDNumber(InGame8)
        self.lcdNumber_6.setGeometry(QtCore.QRect(380, 40, 81, 31))
        self.lcdNumber_6.setObjectName("lcdNumber_6")
        self.lcdNumber_3 = QtWidgets.QLCDNumber(InGame8)
        self.lcdNumber_3.setGeometry(QtCore.QRect(480, 40, 81, 31))
        self.lcdNumber_3.setObjectName("lcdNumber_3")
        self.graphicsView_4 = QtWidgets.QGraphicsView(InGame8)
        self.graphicsView_4.setGeometry(QtCore.QRect(480, 80, 81, 131))
        self.graphicsView_4.setObjectName("graphicsView_4")
        self.graphicsView_8 = QtWidgets.QGraphicsView(InGame8)
        self.graphicsView_8.setGeometry(QtCore.QRect(580, 80, 81, 131))
        self.graphicsView_8.setObjectName("graphicsView_8")
        self.lcdNumber_7 = QtWidgets.QLCDNumber(InGame8)
        self.lcdNumber_7.setGeometry(QtCore.QRect(580, 40, 81, 31))
        self.lcdNumber_7.setObjectName("lcdNumber_7")
        self.lcdNumber_4 = QtWidgets.QLCDNumber(InGame8)
        self.lcdNumber_4.setGeometry(QtCore.QRect(680, 40, 81, 31))
        self.lcdNumber_4.setObjectName("lcdNumber_4")
        self.graphicsView_5 = QtWidgets.QGraphicsView(InGame8)
        self.graphicsView_5.setGeometry(QtCore.QRect(680, 80, 81, 131))
        self.graphicsView_5.setObjectName("graphicsView_5")
        self.graphicsView_9 = QtWidgets.QGraphicsView(InGame8)
        self.graphicsView_9.setGeometry(QtCore.QRect(780, 80, 81, 131))
        self.graphicsView_9.setObjectName("graphicsView_9")
        self.lcdNumber_8 = QtWidgets.QLCDNumber(InGame8)
        self.lcdNumber_8.setGeometry(QtCore.QRect(780, 40, 81, 31))
        self.lcdNumber_8.setObjectName("lcdNumber_8")
        self.pushButton_3 = QtWidgets.QPushButton(InGame8)
        self.pushButton_3.setGeometry(QtCore.QRect(740, 10, 93, 28))
        self.pushButton_3.setObjectName("pushButton_3")

        self.retranslateUi(InGame8)
        QtCore.QMetaObject.connectSlotsByName(InGame8)

    def retranslateUi(self, InGame8):
        _translate = QtCore.QCoreApplication.translate
        InGame8.setWindowTitle(_translate("InGame8", "Dialog"))
        self.pushButton.setText(_translate("InGame8", "상점"))
        self.pushButton_2.setText(_translate("InGame8", "나가기"))
        self.pushButton_3.setText(_translate("InGame8", "시작"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    InGame8 = QtWidgets.QDialog()
    ui = Ui_InGame8()
    ui.setupUi(InGame8)
    InGame8.show()
    sys.exit(app.exec_())

