import sqlite3

def compare_prices():
    conn = sqlite3.connect("textbook_prices.db")
    c = conn.cursor()

    c.execute("""
    SELECT isbn,
           MAX(CASE WHEN source = 'amazon' THEN price END) AS amazon_price,
           MAX(CASE WHEN source = 'ecampus' THEN price END) AS ecampus_price
    FROM textbook_prices
    GROUP BY isbn
    """)

    rows = c.fetchall()

    total_amazon = 0
    total_ecampus = 0
    count = 0

    for isbn, amazon_price, ecampus_price in rows:
        print(f"\n ISBN: {isbn}")
        print(f"   Amazon:  ${amazon_price if amazon_price else 'N/A'}")
        print(f"   eCampus: ${ecampus_price if ecampus_price else 'N/A'}")
        if amazon_price and ecampus_price:
            diff = float(ecampus_price) - float(amazon_price)
            print(f" Difference (eCampus - Amazon): ${diff:.2f}")

            total_amazon += float(amazon_price)
            total_ecampus += float(ecampus_price)
            count += 1

    if count > 0:
        percent_diff = ((total_ecampus - total_amazon) / total_amazon) * 100
        print(f"\n Overall Difference: ${total_ecampus - total_amazon:.2f} across {count} matched books")
        print(f"eCampus is {percent_diff:.2f}% {'more' if percent_diff > 0 else 'less'} expensive than Amazon on average.")

    conn.close()

if __name__ == "__main__":
    compare_prices()
