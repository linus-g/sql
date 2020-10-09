import sqlite3


with sqlite3.connect("cars.db") as connection:
    cursor = connection.cursor()

    cursor.execute("""CREATE TABLE inventory 
               (Make TEXT, Model TEXT, Quantity INT)
               """)
