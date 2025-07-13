#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup
import subprocess

PRODUCT_URLS = {
    "Market-In": "https://www.market-in.gr/el-gr/trofima-proino-kafedes-rofhmata-se-kapsoules/nescafe-dolce-gusto-kapsoules-kafe-espresso-intenso-16-kapsoules-112gr",
    "Sklavenitis": "https://www.sklavenitis.gr/eidi-proinoy-rofimata/kafedes-rofimata-afepsimata/kafedes-espresso/nescafe-dolce-gusto-espresso-intenso-16tem/",
    "MyMarket": "https://www.mymarket.gr/nescafe-dolce-gusto-espresso-intenso-16-kapsoules-112gr"
}

def get_market_in_price(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    price_span = soup.find("span", id="finalPrice")
    if price_span:
        price_text = price_span.text.strip()
        return price_text
    return None

def get_sklavenitis_price(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    price_div = soup.find("div", class_="price")
    if price_div:
        price_text = price_div.text.strip()
        return price_text
    return None

def get_mymarket_price(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    price_span = soup.find("span", class_="product-full--final-price font-bold")
    if price_span:
        price_text = price_span.text.strip()
        return price_text
    return None

SCRAPERS = {
    "Market-In": get_market_in_price,
    "Sklavenitis": get_sklavenitis_price,
    "MyMarket": get_mymarket_price
}

def notify_send(title, message):
    subprocess.run(['notify-send', '-t','20000', title, message])

if __name__ == "__main__":
    results = []
    for market, url in PRODUCT_URLS.items():
        try:
            price = SCRAPERS[market](url)
            if price:
                results.append(f"{market}: {price}")
        except Exception as e:
            pass

    if results:
        message = "\n".join(results)
        notify_send("Τιμές καφέ (Nescafe DG Espresso Intenso)", message)
    else:
        notify_send("Τιμές καφέ", "Δεν βρέθηκαν τιμές από τα διαθέσιμα supermarkets.")