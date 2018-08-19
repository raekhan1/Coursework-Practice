import sqlite3
import bcrypt

def createUsersTable():
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE users(id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, password TEXT)''')
    conn.commit()
    conn.close()

def add_user (username, password):

    conn = sqlite3.connect('example.db')
    with conn:
        cursor = conn.cursor()
        query = "INSERT INTO users (username, password) VALUES ('" + username + "','" + password + "')"
        cursor.execute(query)

def check_user (username, password):

    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()

    cursor.execute("SELECT password FROM users WHERE username = '" + username + "'")

    hs_password= cursor.fetchone()[0]

    if hs_password is None:
        return False

    if bcrypt.checkpw(password, hs_password.encode('utf8')):
        return True
    return False


#createUsersTable()
