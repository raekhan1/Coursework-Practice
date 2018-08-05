import sqlite3

def createUsersTable():
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE users(id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, password TEXT)''')
    conn.commit()
    conn.close()

def add_user(username, password):
    conn = sqlite3.connect('example.db')
    with conn:
        cursor = conn.cursor()
        query = "INSERT INTO users (username, password) VALUES ('" + username + "','" + password + "')"
        cursor.execute(query)



# createUsersTable()
# addUser('Steve', 'Jobs')