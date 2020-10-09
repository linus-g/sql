# executemany() method

import sqlite3

with sqlite3.connect("new.db") as connection:
    cursor = connection.cursor()

    cursor.execute("""SELECT population.city, population.population,
                    regions.region FROM population, regions
                    WHERE population.city = regions.city""")

    for r in cursor.fetchall():
        print(f"City: {r[0]}")
        print(f"Population: {r[1]}")
        print(f"Region: {r[2]}")
        print("")
