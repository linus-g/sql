import sqlite3
import random

with sqlite3.connect("newnum.db") as connection:
    cursor = connection.cursor()

    cursor.execute("DROP TABLE if exists nums")
    cursor.execute("CREATE TABLE nums (num INT)")

    nums = [(random.randint(0, 100), ) for _ in range(100)]
    
    cursor.executemany("INSERT INTO nums VALUES(?)", nums)
