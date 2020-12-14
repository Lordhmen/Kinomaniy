import sqlite3

from flask import Flask, request

app = Flask(__name__)


@app.route("/films", methods=['POST'])
def FILMS():
    conn = sqlite3.connect("bd.db")
    cursor = conn.cursor()

    # Получаем данные с таблица Фильмы
    cursor.execute("SELECT * FROM Фильмы")
    films = cursor.fetchall()

    cursor.execute("SELECT * FROM Киножурнал")
    kinogurnal = cursor.fetchall()

    return {'films': films, 'kinogurnal': kinogurnal}


@app.route("/del_prokat", methods=['POST'])
def del_prokat():
    conn = sqlite3.connect("bd.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Фильмы")
    filmss = cursor.fetchall()
    if filmss[request.json['comboBox']][9] == 1:
        cursor.execute(
            "UPDATE 'Фильмы' SET 'Состояние' = " + str(0) + " WHERE Kod_films = " + str(
                request.json['comboBox'] + 1))
        conn.commit()
        print("Фильм убран из проката")
        return {'ok': True}
    else:
        return {'ok': False}
    # print(request.json['select_comm'])
    # return {'comm': 'qwerttt'}


@app.route("/add_prokat", methods=['POST'])
def add_prokat():
    conn = sqlite3.connect("bd.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Фильмы")
    filmss = cursor.fetchall()
    if filmss[request.json['comboBox']][9] == 0:
        cursor.execute(
            "UPDATE 'Фильмы' SET 'Состояние' = " + str(1) + " WHERE Kod_films = " + str(
                request.json['comboBox'] + 1))
        conn.commit()
        print("Фильм добавлен в проката")
        return {'ok': True}
    else:
        return {'ok': False}


@app.route("/films_mesta_obr", methods=['POST'])
def films_mesta_obr():
    conn = sqlite3.connect("bd.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM 'Места в зале'")
    mesto = cursor.fetchall()
    return {'mesto': mesto}


@app.route("/gurnal_start", methods=['POST'])
def gurnal_start():
    conn = sqlite3.connect("bd.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Киножурнал")
    gurnal = cursor.fetchall()

    cursor.execute("SELECT * FROM Фильмы")
    films = cursor.fetchall()
    return {'films': films, 'gurnal': gurnal}


@app.route("/inf", methods=['POST'])
def inf():
    conn = sqlite3.connect("bd.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Фильмы")
    films = cursor.fetchall()

    return {'films': films}


@app.route("/inf_film", methods=['POST'])
def inf_film():
    conn = sqlite3.connect("bd.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Фильмы")
    films = cursor.fetchall()

    return {'films': films}


@app.route("/films_mesta_obr_one", methods=['POST'])
def films_mesta_obr_one():
    conn = sqlite3.connect("bd.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Киножурнал")
    kinogurnal = cursor.fetchall()

    return {'kinogurnal': kinogurnal}


@app.route("/obraboka_mest_mesto", methods=['POST'])
def obraboka_mest_mesto():
    conn = sqlite3.connect("bd.db")
    cursor = conn.cursor()
    # Получаем данные с таблица Фильмы
    cursor.execute("SELECT * FROM 'Места в зале'")
    mesto = cursor.fetchall()

    return {'mesto': mesto}


@app.route("/obraboka_mest_inf_mesto_1", methods=['POST'])
def obraboka_mest_inf_mesto_1():
    conn = sqlite3.connect("bd.db")
    cursor = conn.cursor()
    # Получаем данные с таблица Фильмы
    cursor.execute("SELECT * FROM 'Места в зале'")
    mesto = cursor.fetchall()
    cursor.execute(
        "UPDATE 'Места в зале' SET 'Состояние' = " + str(1) + " WHERE Kod_zala = " + str(request.json['i'][0]))
    conn.commit()
    print("Изменено состояние места в зале")

    return {'mesto': mesto}


@app.route("/obraboka_mest_inf_mesto_0", methods=['POST'])
def obraboka_mest_inf_mesto_0():
    conn = sqlite3.connect("bd.db")
    cursor = conn.cursor()
    # Получаем данные с таблица Фильмы
    cursor.execute("SELECT * FROM 'Места в зале'")
    mesto = cursor.fetchall()
    cursor.execute(
        "UPDATE 'Места в зале' SET 'Состояние' = " + str(0) + " WHERE Kod_zala = " + str(request.json['i'][0]))
    conn.commit()
    print("Изменено состояние места в зале")

    return {'mesto': mesto}


@app.route("/obraboka_mest_inf_mesto_2", methods=['POST'])
def obraboka_mest_inf_mesto_2():
    conn = sqlite3.connect("bd.db")
    cursor = conn.cursor()
    # Получаем данные с таблица Фильмы
    cursor.execute("SELECT * FROM 'Места в зале'")
    mesto = cursor.fetchall()
    cursor.execute(
        "UPDATE 'Места в зале' SET 'Состояние' = " + str(0) + " WHERE Kod_zala = " + str(request.json['i'][0]))
    conn.commit()
    print("Изменено состояние места в зале")

    return {'mesto': mesto}


@app.route("/obraboka_mest_inf_mesto_3", methods=['POST'])
def obraboka_mest_inf_mesto_3():
    conn = sqlite3.connect("bd.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Киножурнал")
    kinogurnal = cursor.fetchall()
    zapis = 0
    for i in kinogurnal:
        if i[1] == request.json['comboBox_2'] + 1 and i[2] == request.json['comboBox_4']:
            zapis = i[0]
    cursor.execute(
        "UPDATE 'Киножурнал' SET 'Посещаемость' = " + str(request.json['procent']) + " WHERE Zapis = " + str(zapis))
    conn.commit()
    print("Перерасчет посещаемости")

    return {'kinogurnal': kinogurnal}


@app.route("/seve_gurnal", methods=['POST'])
def seve_gurnal():
    conn = sqlite3.connect("bd.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Киножурнал")
    gurnal = cursor.fetchall()
    h = 0
    for i in gurnal:
        cursor.execute("UPDATE 'Киножурнал' SET 'Дата_трансляции' = " + "'" + str(
            request.json['data_t'][h]) + "'" + " WHERE Zapis = " + str(i[0]))
        h += 1
    conn.commit()
    print("Сохранение изменений")

    return {'gurnal': gurnal}


@app.route("/del_gurnal_zapis", methods=['POST'])
def del_gurnal_zapis():
    conn = sqlite3.connect("bd.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Киножурнал")
    gurnal = cursor.fetchall()

    len_gurnal = len(gurnal)
    if len_gurnal < int(request.json['lineEdit']) or int(request.json['lineEdit']) <= 0:
        msg = True

    else:
        msg = False
        dataTra = ''
        for i in gurnal:
            if i[0] == int(request.json['lineEdit']):
                dataTra = i[2]
                break

        if int(request.json['lineEdit']) == len_gurnal:
            cursor.execute("DELETE FROM Киножурнал WHERE Zapis = ?", (str(request.json['lineEdit']),))
            cursor.execute("DELETE FROM 'Места в зале' WHERE Дата_трансляции = ?", (str(dataTra),))
            conn.commit()
        else:
            cursor.execute("DELETE FROM Киножурнал WHERE Zapis = ?", (str(int(request.json['lineEdit'])),))
            cursor.execute("DELETE FROM 'Места в зале' WHERE Дата_трансляции = ?", (str(dataTra),))
            for i in range(int(request.json['lineEdit']), len_gurnal + 1):
                cursor.execute("UPDATE Киножурнал SET 'Zapis' = " + str(i) + " WHERE Zapis = " + str(i + 1))
            conn.commit()
        print("Удаление записи")
    return {'msg': msg}

@app.route("/add_films_zapis", methods=['POST'])
def add_films_zapis():
    conn = sqlite3.connect("bd.db")
    cursor = conn.cursor()
    # Получаем данные с таблица Фильмы
    cursor.execute("SELECT * FROM Фильмы")
    films = cursor.fetchall()

    cursor.execute(
        "INSERT INTO 'Фильмы'(Kod_films, Название_фильма, Страна, Жанр, Длительность, Бюджет, Описание, Рейтинг, Дата_выхода, Состояние) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
        (str(len(films) + 1), str(request.json['data_t'][0]),
         str(request.json['data_t'][1]),
         str(request.json['data_t'][2]), str(request.json['data_t'][3]),
         str(request.json['data_t'][4]), str(request.json['data_t'][5]),
         str(request.json['data_t'][6]), str(request.json['data_t'][7]),
         str(request.json['data_t'][8])))
    conn.commit()
    print("Добавление записи")

    return {'mesto': films}

@app.route("/add_gurnal_zapis_1", methods=['POST'])
def add_gurnal_zapis_1():
    conn = sqlite3.connect("bd.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Киножурнал")
    gurnal = cursor.fetchall()
    print("Изменено состояние места в зале")

    return {'gurnal': gurnal}

@app.route("/add_gurnal_zapis", methods=['POST'])
def add_gurnal_zapis():
    conn = sqlite3.connect("bd.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Фильмы")
    films = cursor.fetchall()

    return {'films': films}

@app.route("/add_gurnal_zapis_2", methods=['POST'])
def add_gurnal_zapis_2():
    conn = sqlite3.connect("bd.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Киножурнал")
    gurnal = cursor.fetchall()
    cursor.execute(
        "INSERT INTO 'Киножурнал' VALUES (" + str(int(gurnal[-1][0]) + 1) + ", '" + str(
            request.json['kod_film']) + "', '" + str(request.json['tableWidget_2']) + "', '" + str(0) + "')")
    conn.commit()

    return {'gurnal': gurnal}

@app.route("/add_gurnal_zapis_3", methods=['POST'])
def add_gurnal_zapis_3():
    conn = sqlite3.connect("bd.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM 'Места в зале'")
    mexto = cursor.fetchall()

    return {'mexto': mexto}

@app.route("/add_gurnal_zapis_4", methods=['POST'])
def add_gurnal_zapis_4():
    conn = sqlite3.connect("bd.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM 'Места в зале'")
    mexto = cursor.fetchall()
    pb = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 17, 16, 15, 14, 13, 20, 28, 26, 19, 32, 29, 30, 21, 22, 23, 31, 24, 25,
          27, 18, 35, 43, 41, 34, 47, 44, 45, 36, 37, 38, 46, 39, 40, 42, 33, 50, 58, 56, 49, 62, 59, 60, 51, 52,
          53, 61, 54, 55, 57, 48, 65, 73, 71, 64, 77, 74, 75, 66, 67, 68, 76, 69, 70, 72, 63, 80, 88, 86, 79, 92,
          89, 90, 81, 82, 83, 91, 84, 85, 87, 78]
    cursor.execute(
        "INSERT INTO 'Места в зале' VALUES (" + str(request.json['i_mesto'][request.json['yyy']]) + ", '" + str(request.json['kod_film']) + "', '" + str(
            request.json['r']) + "', '" + str(
            request.json['m']) + "', '" + str(0) + "', '" + str(pb[request.json['h']]) + "', '" + str(
            request.json['tableWidget_2']) + "')")
    conn.commit()

    return {'mexto': mexto}

@app.route("/add_gurnal_zapis_5", methods=['POST'])
def add_gurnal_zapis_5():
    conn = sqlite3.connect("bd.db")
    conn.commit()

    return {'mexto': 'mexto'}


if __name__ == '__main__':
    app.run()
