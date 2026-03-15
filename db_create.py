import sqlite3

conn = sqlite3.connect("database.db")

conn.execute("""
CREATE TABLE tasks (
id INTEGER PRIMARY KEY AUTOINCREMENT,
task TEXT NOT NULL,
done INTEGER NOT NULL
)
""")

conn.close()