import sqlite3
from sqlite3.dbapi2 import Cursor

conn = sqlite3.connect("new.db")

cursor = conn.cursor()

cursor.execute("""CREATE TABLE population 
               (city TEXT, state TEXT, population INT)
               """)

conn.close()
            