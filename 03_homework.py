import sqlite3


with sqlite3.connect("cars.db") as connection:
    cursor = connection.cursor()

    cursor.execute("UPDATE inventory SET Quantity = 23 WHERE Model='Accord'")
    cursor.execute("UPDATE inventory SET Quantity = 0 WHERE Model='Fiesta'")

    for row in cursor.execute("SELECT * from inventory"):
        print(row)

