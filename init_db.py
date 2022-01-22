import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()
cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",('заголовок1', 'Пост1'))
cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",('загловок2', 'пост2'))
connection.commit()
connection.close()