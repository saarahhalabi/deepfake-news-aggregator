import sqlite3

def init_db():
    conn = sqlite3.connect("news.db")
    conn.execute("""
        CREATE TABLE IF NOT EXISTS articles (
            id INTEGER PRIMARY KEY,
            url TEXT UNIQUE,
            title TEXT,
            source TEXT,
            published TEXT,
            summary TEXT,
            classification TEXT
        )
    """)
    conn.commit()
    return conn
