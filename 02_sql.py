import sqlite3
# INSERT Command

with sqlite3.connect("new.db") as connection:
    cursor = connection.cursor()
    # insert data
    cursor.execute("INSERT INTO population VALUES('New York City', \
        'NY', 8400000)") 
    cursor.execute("INSERT INTO population VALUES('San Francisco', \
        'CA', 800000)")
