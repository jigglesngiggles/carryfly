from playwright.sync_api import sync_playwright

def fetch_amazon_price(url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(user_agent=(
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/91.0.4472.124 Safari/537.36"
        ))
        try:
            page.goto(url, timeout=15000)
            price = page.locator("span.a-offscreen").first.text_content(timeout=5000)
        except Exception as e:
            print("Error fetching price:", e)
            price = "$0.00"
        finally:
            browser.close()
        return price
