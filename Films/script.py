import sqlite3
from ui.ui_main import Ui_MainWindow

global films
class FunctionsFilms(Ui_MainWindow):
    global films

    def __init__(self):
        self.ui = Ui_MainWindow()

    def FILMS(self):
        global films
        conn = sqlite3.connect("bd.db")
        cursor = conn.cursor()

        # Получаем данные с таблица
        cursor.execute("SELECT * FROM Фильмы")
        films = cursor.fetchall()

        # print(films)
        for i in films:
            self.ui.comboBox.addItem(i[1])
