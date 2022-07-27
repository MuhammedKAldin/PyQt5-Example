# Python-Qt-Example

- index -> Triggers and MessageBox
- index2 -> Conditionals, Events and ComboBox
- Ui_home -> Ui_home -> form load management

*Instantiation*
``` if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_otherWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_()) 
