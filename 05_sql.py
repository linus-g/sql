# INSERT Command with Error Handler
import sqlite3


connection = sqlite3.connect("new.db")
cursor = connection.cursor()

try:
   # insert data
    cursor.execute("INSERT INTO populations VALUES('New York City', \
        'NY', 8400000)") 
    cursor.execute("INSERT INTO populations VALUES('San Francisco', \
        'CA', 800000)")

    connection.commit()
except sqlite3.OperationalError as error:
    print("Oops! Something went wrong. Try again...")
    print(error)
    
connection.close()
