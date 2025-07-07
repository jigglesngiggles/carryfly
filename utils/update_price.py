import re
from price_fetcher import fetch_amazon_price

HTML_FILE = "../index.html"
PRODUCT_URL = "https://www.amazon.com/dp/B0BZD92D6X"
MARKUP = 15.00

price_text = fetch_amazon_price(PRODUCT_URL)
base_price = float(price_text.replace("$", "").replace(",", ""))
final_price = round(base_price + MARKUP, 2)

with open(HTML_FILE, "r", encoding="utf-8") as f:
    html = f.read()

new_html = re.sub(r"\$\d+\.\d{2}", f"${final_price}", html, count=1)

with open(HTML_FILE, "w", encoding="utf-8") as f:
    f.write(new_html)

print(f"Updated price to ${final_price} in {HTML_FILE}")
