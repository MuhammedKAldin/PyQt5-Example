# Python-Qt-Example

- index -> Triggers and MessageBox
- index2 -> Conditionals, Events and ComboBox
- Ui_home -> Ui_home -> form load management

*Instantiation Through UI -> Py
``` 
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_otherWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_()) 
```

*Instantiation Through UI Directly
``` 
from ast import If
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.uic import loadUi
import sys

class Main(QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        loadUi('Login.ui', self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = Main()
    ui.show()
    app.exec_() 
```
