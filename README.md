# Coffee Capsule Price Desktop Notifier

This application automatically notifies the user of the current prices for Nescafe Dolce Gusto Espresso Intenso at three Greek supermarkets: Market-In, Sklavenitis, and MyMarket. On each run, it performs web scraping and displays a desktop notification on Ubuntu, showing each price on a separate line for easy reading.

## Description

- The program scrapes the corresponding product pages from the supermarkets and presents the prices in a desktop notification.
- It is designed for Greek supermarkets whose websites allow web scraping of price data.
- The notification appears automatically every time the computer starts.

## Installation Instructions

1. **Requirements:**
   - Python 3
   - The `requests` and `beautifulsoup4` Python packages
   - The `notify-send` program (pre-installed on most Ubuntu systems)

2. **Install Python packages:**
   ```bash
   pip install requests beautifulsoup4
   ```

3. **Save the script:**
   - Download or copy the `coffee.py` file to your desired folder.

4. **Make the script executable:**
   ```bash
   chmod +x /path/to/coffee.py
   ```

5. **Set up automatic execution at startup (Ubuntu):**
   - Open the "Startup Applications" menu in Ubuntu.
   - Click "Add".
   - Fill in:
     - **Name:** Coffee Prices Notification
     - **Command:** `/path/to/coffee.py`
     - **Comment:** (optional)
   - Save and restart your computer to verify it works.

## Notes

- If a supermarket changes its website structure, the scraping logic may need updating.
- The notification will only show prices that are available.
- This project is intended for personal use and for websites that allow scraping of product prices.

---

**Enjoy! Feel free to modify or expand the project as you wish.**
