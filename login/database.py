import sqlite3
import bcrypt


def create_users_table():

    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE users(id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, password TEXT)''')
    conn.commit()
    conn.close()


def add_user(username, password):

    conn = sqlite3.connect('example.db')
    with conn:
        cursor = conn.cursor()
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode("utf-8")
        query = "INSERT INTO users (username, password) VALUES ('" + username + "','" + hashed_password + "')"
        cursor.execute(query)


def check_user(username, password):

    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()

    cursor.execute("SELECT password FROM users WHERE username = '" + username + "'")

    hs_password = cursor.fetchone()[0]

    if hs_password is None:
        return False

    if bcrypt.checkpw(password.encode('utf8'), hs_password.encode('utf8')):
        return True
    return False


def fp_check_user(username):

    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()

    cursor.execute("SELECT password FROM users WHERE username = '" + username + "'")

    ck_user = cursor.fetchone()

    if ck_user is None:
        return False
    return True


def change_pass(username, password):
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()

    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode("utf-8")

    query = ("UPDATE users SET password = '"+hashed_password+"' WHERE username ='"+username+"' ")
    cursor.execute(query)
    conn.commit()
    conn.close()

# createUsersTable()
