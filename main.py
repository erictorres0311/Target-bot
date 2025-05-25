import time
from playwright.sync_api import sync_playwright
import requests
import os

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
TARGET_ITEM_URL = "https://www.target.com/p/-/94300072"  # Update if needed
TARGET_KEYWORDS = [
    "prismatic evolutions",
    "pokemon",
    "elite trainer",
    "booster bundle",
    "destined rivals",
    "scarlet & violet-151",
    "ultra-premium collection"
]

def send_telegram(message):
    if TELEGRAM_TOKEN and TELEGRAM_CHAT_ID:
        requests.post(
            f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage",
            data={"chat_id": TELEGRAM_CHAT_ID, "text": message}
        )

def run_bot():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://www.target.com/")

        page.wait_for_timeout(5000)
        print("Searching for Pokémon products...")

        for keyword in TARGET_KEYWORDS:
            try:
                search_url = f"https://www.target.com/s?searchTerm={keyword.replace(' ', '+')}"
                page.goto(search_url)
                page.wait_for_timeout(3000)

                if "Add to cart" in page.content():
                    send_telegram(f"🔔 In stock: {keyword}\n{search_url}")
                    print(f"Product found with keyword: {keyword}")
                    break
            except Exception as e:
                print(f"Error with keyword '{keyword}':", e)

        context.close()
        browser.close()

if __name__ == "__main__":
    while True:
        try:
            run_bot()
        except Exception as e:
            print("Bot crashed:", e)
        time.sleep(60)
