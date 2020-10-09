import sqlite3
import random

# define actions
actions = {
    'AVG': "SELECT AVG(num) from nums",
    'MAX': "SELECT MAX(num) from nums",
    'MIN': "SELECT MIN(num) from nums",
    'SUM': "SELECT SUM(num) from nums",
}

prompt = """
Select the operation that you want to perform:
AVG
MAX
MIN
SUM
exit
"""

while True:
    # ask for action
    user_input = input(prompt)

    # if exit end program
    if user_input in actions.keys():    
        with sqlite3.connect("newnum.db") as connection:
            cursor = connection.cursor()
            cursor.execute(actions[user_input])
            result = cursor.fetchone()
            print(f"{user_input} = {result[0]}")
    elif user_input == 'exit':
        break
    else:
        print('Not a valid action.')
