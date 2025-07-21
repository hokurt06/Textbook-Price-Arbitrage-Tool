import sqlite3
from datetime import datetime

def save_price_to_db(isbn, source, condition, price):
    conn = sqlite3.connect("textbook_prices.db")
    c = conn.cursor()
    c.execute("""
        INSERT INTO textbook_prices (isbn, source, condition, price, timestamp)
        VALUES (?, ?, ?, ?, ?)
    """, (isbn, source, condition, price, datetime.now()))
    conn.commit()
    conn.close()
