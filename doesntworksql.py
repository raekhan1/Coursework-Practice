import sqlite3
conn = sqlite3.connect('database.db')

print('Database connection created.')

cursor = conn.execute()

cursor.execute('''CREATE TABLE request_songs 
(id INTEGER PRIMARY KEY ASC, 
song_id INT, 
requester TEXT, 
created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
updated_at DATETIME DEFAULT CURRENT_TIMESTAMP);''')

cursor.execute('''CREATE TABLE songs 
(id INTEGER PRIMARY KEY ASC, 
song_name TEXT, 
artist TEXT, 
origin TEXT,
created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
updated_at DATETIME DEFAULT CURRENT_TIMESTAMP);''')

print('Table created.')

cursor.execute('''INSERT INTO songs
(song_name, 
artist)

VALUES ("Colors",
"Jason Derulo");''')

conn.commit()

cursor.execute('''INSERT INTO songs
(song_name,artist)
VALUES ("BAAM","Momoland");''')

cursor.execute('''INSERT INTO request_songs
(song_id, requester)
VALUES ("2","Rae");''')

conn.commit()
conn.close()
