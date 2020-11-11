import sqlite3

from ui.user import *
from ui.ui_main import *
import sys

global root
root = False


class USER(QMainWindow):
    global root

    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_mmMainWindow()
        self.ui.setupUi(self)
        self.showNormal()
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.ui.pushButton.clicked.connect(self.Authorization)
        self.ui.lineEdit.setEchoMode(QLineEdit.Password)

    def Authorization(self):
        # root = False
        global root
        client_p = "123"
        admin_p = "1234"
        if self.ui.comboBox.currentIndex() == 1:
            if str(self.ui.lineEdit.text()) == admin_p:
                root = True
                self.close()
            else:
                self.ui.statusBar.setStyleSheet(
                    "QStatusBar{padding-left:22px;color:#fff;font-weight:bold;}")
                self.ui.statusBar.showMessage('Пароль невереный!')
        else:
            if str(self.ui.lineEdit.text()) == client_p:
                root = False
                self.close()
            else:
                self.ui.statusBar.setStyleSheet(
                    "QStatusBar{padding-left:22px;color:#fff;font-weight:bold;}")
                self.ui.statusBar.showMessage('Пароль невереный!')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = USER()
    window.show()
    sys.exit(app.exec_())
