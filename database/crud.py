import sqlite3

def insert_to_movie(title, description, photo_url):
    with sqlite3.connect('ansar.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
        INSERT INTO movie(title, description, photo_url)
        VALUES(?, ?, ?)
''', (title, description, photo_url))
        conn.commit()
