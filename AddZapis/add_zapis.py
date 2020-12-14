import sqlite3
import sys

import requests

from ui.ui_add_zapis import *
from ui.ui_main import *


class ADDZAPIS(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_mMainWindow()
        self.ui.setupUi(self)
        self.showNormal()
        # self.setWindowFlags(Qt.FramelessWindowHint)
        self.setWindowTitle('Добовление записей')
        self.ui.pushButton.clicked.connect(self.add_films_zapis)
        self.ui.pushButton_2.clicked.connect(self.add_gurnal_zapis)

    def add_films_zapis(self):
        data_t = []
        for i in range(int(self.ui.tableWidget.columnCount())):
            data_t.append(str(self.ui.tableWidget.item(0, i).text()))
        com = requests.post(
            'http://127.0.0.1:5000/add_films_zapis',
            json={'data_t': data_t}
        )

        self.ui.tableWidget.setItem(0, 0, QTableWidgetItem(""))
        self.ui.tableWidget.setItem(0, 1, QTableWidgetItem(""))
        self.ui.tableWidget.setItem(0, 2, QTableWidgetItem(""))
        self.ui.tableWidget.setItem(0, 3, QTableWidgetItem(""))
        self.ui.tableWidget.setItem(0, 4, QTableWidgetItem(""))
        self.ui.tableWidget.setItem(0, 5, QTableWidgetItem(""))
        self.ui.tableWidget.setItem(0, 6, QTableWidgetItem(""))
        self.ui.tableWidget.setItem(0, 7, QTableWidgetItem(""))
        self.ui.tableWidget.setItem(0, 8, QTableWidgetItem(""))

    def add_gurnal_zapis(self):
        com = requests.post(
            'http://127.0.0.1:5000/add_gurnal_zapis',
            json={'data_t': 'data_t'}
        )
        kod_film = -1

        for i in com.json()['films']:
            if str(self.ui.tableWidget_2.item(0, 0).text()) != i[1]:
                pass
            else:
                kod_film = i[0]
                break
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Ошибка")
            msg.setText("Фильма с таким название нет в базе")
            okButton = msg.addButton('Хорошо', QMessageBox.AcceptRole)
            msg.exec()

        comm = requests.post(
            'http://127.0.0.1:5000/add_gurnal_zapis_1',
            json={'data_t': 'data_t'}
        )

        StatusM = True
        for i in comm.json()['gurnal']:
            if str(kod_film) == str(i[1]) and str(self.ui.tableWidget_2.item(0, 1).text()) == str(i[2]):
                StatusM = False

        if StatusM:
            if kod_film != -1:
                commmm = requests.post(
                    'http://127.0.0.1:5000/add_gurnal_zapis_2',
                    json={'kod_film': kod_film, 'tableWidget_2': self.ui.tableWidget_2.item(0, 1).text()}
                )

            commmm = requests.post(
                'http://127.0.0.1:5000/add_gurnal_zapis_3',
                json={'data_t': 'data_t'}
            )
            i_mesto = []
            for i in range(int(commmm.json()['mexto'][-1][0]) + 1, int(commmm.json()['mexto'][-1][0]) + 1 + 90 + 1):
                i_mesto.append(i)
            r = 1
            m = 1
            h = 0
            yyy = -1
            for i in range(92):
                if r <= 6:
                    yyy += 1
                    commmmm = requests.post(
                        'http://127.0.0.1:5000/add_gurnal_zapis_4',
                        json={'i_mesto': i_mesto, 'yyy': yyy, 'kod_film': kod_film, 'r': r, 'm': m, 'h': h,
                              'tableWidget_2': self.ui.tableWidget_2.item(0, 1).text()}
                    )
                    m += 1
                if m == 16:
                    r += 1
                    m = 1
                h += 1

            # Сохраняем изменения
            commmmmm = requests.post(
                'http://127.0.0.1:5000/add_gurnal_zapis_5',
                json={'data_t': 'data_t'}
            )
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Ошибка")
            msg.setText("Запись с такими данными уже есть в БД!")
            okButton = msg.addButton('Хорошо', QMessageBox.AcceptRole)
            msg.exec()
        self.ui.tableWidget_2.setItem(0, 0, QTableWidgetItem(""))
        self.ui.tableWidget_2.setItem(0, 1, QTableWidgetItem(""))
        self.ui.tableWidget_2.setItem(0, 2, QTableWidgetItem(""))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ADDZAPIS()
    window.show()
    sys.exit(app.exec_())
