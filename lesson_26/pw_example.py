import time
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)

    page = browser.new_page()
    page.goto("https://wa.dev.uklon.net/login")
    page.get_by_label("")
    time.sleep(3)