import sqlite3

def init_db():
    conn = sqlite3.connect("ats.db")
    c = conn.cursor()

    c.execute("""
    CREATE TABLE IF NOT EXISTS results (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        score TEXT,
        review TEXT,
        rewrite TEXT
    )
    """)

    conn.commit()
    conn.close()


def save_result(score, review, rewrite):
    conn = sqlite3.connect("ats.db")
    c = conn.cursor()

    c.execute(
        "INSERT INTO results (score, review, rewrite) VALUES (?, ?, ?)",
        (score, review, rewrite)
    )

    conn.commit()
    conn.close()