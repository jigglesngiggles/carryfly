import re
from price_fetcher import fetch_amazon_price

HTML_FILE = "../index.html"
PRODUCT_URL = "https://www.amazon.com/AMUFER-Upgraded-Exclusive-Improvement-Mosquito/dp/B0CT4KKSB5?source=ps-sl-shoppingads-lpcontext&ref_=fplfs&psc=1&smid=A3ASA9QYNZUULE&gQT=1"
MARKUP = 15.00

price_text = fetch_amazon_price(PRODUCT_URL)
try:
    base_price = float(price_text.replace("$", "").replace(",", ""))
except ValueError:
    print("Failed to parse price from fetched text:", price_text)
    exit(1)

final_price = round(base_price + MARKUP, 2)

with open(HTML_FILE, "r", encoding="utf-8") as f:
    html = f.read()

new_html = re.sub(
    r'(<span id="product-price">)\$\d+\.\d{2}(</span>)',
    rf'\1${final_price}\2',
    html
)

with open(HTML_FILE, "w", encoding="utf-8") as f:
    f.write(new_html)

print(f"Updated price to ${final_price} in {HTML_FILE}")
