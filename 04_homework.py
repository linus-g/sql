import sqlite3


with sqlite3.connect("cars.db") as connection:
    cursor = connection.cursor()

    for row in cursor.execute("SELECT * from inventory WHERE Make='Ford'"):
        print(row)

