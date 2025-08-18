# Textbook Price Arbitrage Tool

This project scrapes textbook prices from both Drexel's eCampus bookshop and Amazon, stores the results in a local SQLite database, and compares the prices to identify pricing gaps.

## Features
- Scrapes textbook prices from Amazon and eCampus using Selenium and undetected-chromedriver.
- Stores ISBN, price, source, and condition in an SQLite database.
- Compares prices across platforms and calculates price differences and percentage savings.
- Supports batch processing of large ISBN lists.
- Includes a comparison tool with clear CLI output.

## Requirements
- Python 3.9 or later
- Google Chrome and ChromeDriver
- Required Python packages:
  ```bash
  pip install selenium undetected-chromedriver

## Project Structure
textbook/
- db_utils.py
- scraper_amazon.py
- scraper_ecampus.py
- compare_prices.py
- textbook_prices.db
- README.md

## How To Use
1. Scrape Prices

Run both scrapers:

python3 scraper_amazon.py

python3 scraper_ecampus.py

2. Compare Prices

python3 compare_prices.py

Example Output

ISBN: 9780131103627
  Amazon:  $47.22
  eCampus: $65.00
  Difference (eCampus - Amazon): $17.78
  Savings: 27.35%

## Notes
The Amazon scraper handles some common blocks (like "Continue Shopping" popups), but may still fail if CAPTCHA or unusual layouts appear. Set headless=False in the Chrome options if headless mode causes failures. Wait times and simulated typing are to avoid bot detection.

## Purpose

This tool helps students compare textbook prices across vendors and avoid paying unnecessary markups from the Drexel university bookstore.

