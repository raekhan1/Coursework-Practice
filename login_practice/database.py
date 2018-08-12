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

def check_user(username, password):
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users WHERE username = '" + username + "'AND password ='" + password + "'")
    result = cursor.fetchall()
    if len(result) > 0:
        return True
    else:
        return False
    conn.commit()
    conn.close()

#createUsersTable()
