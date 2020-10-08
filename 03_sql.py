# executemany() method

import sqlite3

with sqlite3.connect("new.db") as connection:
    cursor = connection.cursor()

    cities = [
        ('Boston', 'MA', 600_000),
        ('Chicago', 'IL', 2_700_000),
        ('Houston', 'TX', 2_100_000),
        ('Phoenix', 'AZ', 1_500_000),
        ]

    cursor.executemany('INSERT INTO population VALUES(?, ?, ?)', cities)
