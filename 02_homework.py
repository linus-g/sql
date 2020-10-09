import sqlite3


with sqlite3.connect("cars.db") as connection:
    cursor = connection.cursor()

    entries = [
        ('Ford', 'Mustang', 5),
        ('Ford', 'Fiesta', 10),
        ('Ford', 'Puma', 3),
        ('Honda', 'Accord', 12),
        ('Honda', 'Civiv', 8),
    ]

    cursor.executemany('INSERT INTO inventory VALUES(?,?,?)', entries)
