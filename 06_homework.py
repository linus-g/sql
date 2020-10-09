import sqlite3


with sqlite3.connect("cars.db") as connection:
    cursor = connection.cursor()

    # create a dictionary of sql queries
    sql = {
            'Mustang count'    : "SELECT count(Make) FROM orders WHERE Model = 'Mustang'",
            'Fiesta count'    : "SELECT count(Make) FROM orders WHERE Model = 'Fiesta'",
            'Puma count'    : "SELECT count(Make) FROM orders WHERE Model = 'Puma'",
            'Accord count'    : "SELECT count(Make) FROM orders WHERE Model = 'Accord'",
            'Civic count'    : "SELECT count(Make) FROM orders WHERE Model = 'Civic'",
        }

    # run each sql query item in the dictionary
    for keys, values in sql.items():

        # run sql
        cursor.execute(values)

        # fetchone() retrieves one record from the query
        result = cursor.fetchone()

        # output the result to screen
        print(keys + ":", result[0])