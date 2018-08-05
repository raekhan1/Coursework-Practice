import sqlite3


def create_table():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    try:
        cursor.execute('''CREATE TABLE users
        (username TEXT NOT NULL,
        password TEXT NOT NULL);''')
    except:
        pass

def add_user(data):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    for record in data:
        cursor.execute("INSERT INTO users VALUES(?,?)", record)

    conn.commit()
    conn.close()



def check(user, password):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM users WHERE username = '"+user+"'AND WHERE password='"+password+"'")
        r = True
    except:
        r = False
    conn.commit()
    conn.close()

    return r

