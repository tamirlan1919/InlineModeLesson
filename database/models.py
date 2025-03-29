import sqlite3


def make_table_movie():
    with sqlite3.connect('ansar.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS movie(
            id INTEGER PRIMARY KEY,
            title VARCHAR(150),
            description TEXT,
            photo_url TEXT             
        )
''')
        conn.commit()