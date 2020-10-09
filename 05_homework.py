import sqlite3


with sqlite3.connect("cars.db") as connection:
    cursor = connection.cursor()

    cursor.execute("CREATE TABLE orders (Make TEXT, Model TEXT, order_date TEXT)")

    orders = [
        ('Ford', 'Mustang', '2020-05-23'),
        ('Ford', 'Mustang', '2020-08-21'),
        ('Ford', 'Mustang', '2020-04-02'),
        ('Ford', 'Fiesta', '2020-02-14'),
        ('Ford', 'Fiesta', '2020-06-12'),
        ('Ford', 'Fiesta', '2020-09-08'),
        ('Ford', 'Puma', '2020-10-28'),
        ('Ford', 'Puma', '2020-06-23'),
        ('Ford', 'Puma', '2020-09-21'),
        ('Honda', 'Accord', '2020-06-23'),
        ('Honda', 'Accord', '2020-08-06'),
        ('Honda', 'Accord', '2020-09-11'),
        ('Honda', 'Civic', '2020-02-23'),
        ('Honda', 'Civic', '2020-07-03'),
        ('Honda', 'Civic', '2020-08-20'),
    ]

    cursor.executemany('INSERT INTO orders VALUES(?,?,?)', orders)

    cursor.execute("""SELECT inventory.Make, inventory.Model, inventory.Quantity,
            orders.order_date FROM inventory INNER JOIN orders
            ON inventory.model = orders.model""")

    for r in cursor.fetchall():
        print(r[0], r[1])
        print(r[2])
        print(r[3])
        print() 
