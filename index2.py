# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\Github\PyQuiz\PyQuiz-API\test2.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(490, 90, 211, 121))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(80, 90, 211, 121))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setObjectName("comboBox_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(170, 360, 371, 141))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
                
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        # Event Handlers
        self.pushButton.clicked.connect(self.pressed)
        
        self.comboBox.addItem("Easy")
        self.comboBox.addItem("Medium")
        self.comboBox.addItem("Hard")
        
        self.comboBox_2.addItem("Easy")
        self.comboBox_2.addItem("Medium")
        self.comboBox_2.addItem("Hard") 
    
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.comboBox.setItemText(0, _translate("MainWindow", "0"))
        self.comboBox.setItemText(1, _translate("MainWindow", "1"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "0"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "1"))
        self.pushButton.setText(_translate("MainWindow", "Submit"))
        
    # Additions
    def pressed(self):
        if(self.comboBox.currentText() == self.comboBox_2.currentText()):
            self.pushButton.setText(self.comboBox.currentText())
    
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
