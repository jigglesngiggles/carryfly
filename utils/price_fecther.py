from playwright.sync_api import sync_playwright

def fetch_amazon_price(url):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(url)
        price = page.locator("span.a-offscreen").first.text_content()
        browser.close()
        return price