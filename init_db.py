import sqlite3

conn = sqlite3.connect("textbook_prices.db")
c = conn.cursor()

c.execute("DROP TABLE IF EXISTS textbook_prices")

c.execute("""
CREATE TABLE textbook_prices (
    isbn TEXT,
    source TEXT,
    condition TEXT,
    price REAL,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (isbn, source, condition)
)
""")

conn.commit()
conn.close()

print("Table recreated.")
