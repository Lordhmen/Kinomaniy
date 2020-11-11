import sqlite3

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
        conn = sqlite3.connect("bd.db")
        cursor = conn.cursor()

        # Получаем данные с таблица Фильмы
        cursor.execute("SELECT * FROM Фильмы")
        films = cursor.fetchall()

        cursor.execute(
            "INSERT INTO 'Фильмы'(Kod_films, Название_фильма, Страна, Жанр, Длительность, Бюджет, Описание, Рейтинг, Дата_выхода, Состояние) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (str(len(films) + 1), str(self.ui.tableWidget.item(0, 0).text()),
             str(self.ui.tableWidget.item(0, 1).text()),
             str(self.ui.tableWidget.item(0, 2).text()), str(self.ui.tableWidget.item(0, 3).text()),
             str(self.ui.tableWidget.item(0, 4).text()), str(self.ui.tableWidget.item(0, 5).text()),
             str(self.ui.tableWidget.item(0, 6).text()), str(self.ui.tableWidget.item(0, 7).text()),
             str(self.ui.tableWidget.item(0, 8).text())))
        conn.commit()

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
        conn = sqlite3.connect("bd.db")
        cursor = conn.cursor()

        # Получаем данные с таблица Фильмы
        cursor.execute("SELECT * FROM Фильмы")
        films = cursor.fetchall()

        kod_film = -1

        for i in films:
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

        cursor.execute("SELECT * FROM Киножурнал")
        gurnal = cursor.fetchall()

        StatusM = True
        for i in gurnal:
            if str(kod_film) == str(i[1]) and str(self.ui.tableWidget_2.item(0, 1).text()) == str(i[2]):
                StatusM = False

        if StatusM:
            if kod_film != -1:
                cursor.execute(
                    "INSERT INTO 'Киножурнал' VALUES (" + str(int(gurnal[-1][0]) + 1) + ", '" + str(
                        kod_film) + "', '" + str(self.ui.tableWidget_2.item(0, 1).text()) + "', '" + str(0) + "')")
                conn.commit()

            cursor.execute("SELECT * FROM 'Места в зале'")
            mexto = cursor.fetchall()

            pb = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 17, 16, 15, 14, 13, 20, 28, 26, 19, 32, 29, 30, 21, 22, 23, 31, 24, 25,
                  27, 18, 35, 43, 41, 34, 47, 44, 45, 36, 37, 38, 46, 39, 40, 42, 33, 50, 58, 56, 49, 62, 59, 60, 51, 52,
                  53, 61, 54, 55, 57, 48, 65, 73, 71, 64, 77, 74, 75, 66, 67, 68, 76, 69, 70, 72, 63, 80, 88, 86, 79, 92,
                  89, 90, 81, 82, 83, 91, 84, 85, 87, 78]

            i_mesto = []
            for i in range(int(mexto[-1][0]) + 1, int(mexto[-1][0]) + 1 + 90 + 1):
                i_mesto.append(i)
            r = 1
            m = 1
            h = 0
            yyy = -1
            for i in range(92):
                if r <= 6:
                    yyy += 1
                    cursor.execute(
                        "INSERT INTO 'Места в зале' VALUES (" + str(i_mesto[yyy]) + ", '" + str(kod_film) + "', '" + str(
                            r) + "', '" + str(
                            m) + "', '" + str(0) + "', '" + str(pb[h]) + "', '" + str(
                            self.ui.tableWidget_2.item(0, 1).text()) + "')")
                    m += 1
                if m == 16:
                    r += 1
                    m = 1
                h += 1

            # Сохраняем изменения
            conn.commit()
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
