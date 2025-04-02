import sqlite3

def insert_to_movie(title, description, photo_url):
    with sqlite3.connect('ansar.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
        INSERT INTO movie(title, description, photo_url)
        VALUES(?, ?, ?)
''', (title, description, photo_url))
        conn.commit()

def get_movie_by_title(title):
    with sqlite3.connect('ansar.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
        SELECT title, description, photo_url FROM movie WHERE title LIKE ?
''',(f'%{title}%',))
        data = cursor.fetchall()
        return data








        