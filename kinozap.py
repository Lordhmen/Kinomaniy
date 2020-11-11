import sqlite3
import random

conn = sqlite3.connect("bd.db")
cursor = conn.cursor()
# Получаем данные с таблица Фильмы
cursor.execute("SELECT * FROM Киножурнал")
gurnal = cursor.fetchall()

for i in range(1, 64):
    vvv = 1
    datad = random.randint(1, 31)
    datam = random.randint(1, 13)
    if datad < 10:
        datad = '0' + str(datad)
    if datam < 10:
        datam = '0' + str(datam)
    cursor.execute(
        "INSERT INTO 'Киножурнал' VALUES (" + str(i) + ", '" + str(i) + "', '" + str(
            str(datad) + '.' + str(datam) + '.' + '2020') + "', '" + str(0) + "')")
conn.commit()

cursor.execute("SELECT * FROM 'Места в зале'")
mexto = cursor.fetchall()
cursor.execute("SELECT * FROM Фильмы")
films = cursor.fetchall()
cursor.execute("SELECT * FROM Киножурнал")
gurnal = cursor.fetchall()

dan_gurnal = []
for i in gurnal:
    dan_gurnal.append(i[2])

dan_films = []
for i in films:
    dan_films.append(i[0])

print(dan_films)
print(dan_gurnal)
print(len(dan_films), len(dan_gurnal))

pb = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 17, 16, 15, 14, 13, 20, 28, 26, 19, 32, 29, 30, 21, 22, 23, 31, 24, 25,
      27, 18, 35, 43, 41, 34, 47, 44, 45, 36, 37, 38, 46, 39, 40, 42, 33, 50, 58, 56, 49, 62, 59, 60, 51, 52,
      53, 61, 54, 55, 57, 48, 65, 73, 71, 64, 77, 74, 75, 66, 67, 68, 76, 69, 70, 72, 63, 80, 88, 86, 79, 92,
      89, 90, 81, 82, 83, 91, 84, 85, 87, 78]

r = 1
m = 1
h = 0
h_films = 0
h_gurnal = 0
h_cikl = 1
o = 1
for i in range(1, 5734):
    if h_cikl != 91:
        print(h_films, h_cikl)
        if r <= 6:
            cursor.execute(
                "INSERT INTO 'Места в зале' VALUES (" + str(o) + ", '" + str(dan_films[h_films]) + "', '" + str(
                    r) + "', '" + str(
                    m) + "', '" + str(0) + "', '" + str(pb[h]) + "', '" + str(dan_gurnal[h_gurnal]) + "')")
            o += 1
        m += 1
        if m == 16:
            r += 1
            m = 1
        h += 1
        h_cikl += 1
    else:
        conn.commit()
        r = 1
        m = 1
        h = 0
        h_cikl = 1
        h_films += 1
        h_gurnal += 1

conn.commit()
