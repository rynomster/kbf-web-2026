import os
from playwright.sync_api import sync_playwright

def run_cuj(page):
    # Load the local index.html via server
    page.goto("http://localhost:8000/index.html")
    page.wait_for_timeout(2000)

    # 1. Hero Check
    hero_h1 = page.locator('.hero h1')
    print(f"Hero H1: {hero_h1.text_content()}")

    # 2. Welcome Section Check
    welcome_h2 = page.locator('#welcome h2')
    print(f"Welcome H2: {welcome_h2.text_content()}")

    # 3. Committee Preview Check
    committee_preview = page.locator('#committee-preview')
    print(f"Committee Preview section visible: {committee_preview.is_visible()}")
    committee_cards = page.locator('#committee-preview .committee-card')
    print(f"Committee Cards found: {committee_cards.count()}")

    # 4. Directory Preview Check
    directory_preview = page.locator('#directory')
    print(f"Directory Preview section visible: {directory_preview.is_visible()}")

    # 5. Events Preview Check
    events_preview = page.locator('#events')
    print(f"Events Preview section visible: {events_preview.is_visible()}")

    # 6. Gallery Preview Check
    gallery_preview = page.locator('#gallery-preview')
    print(f"Gallery Preview section visible: {gallery_preview.is_visible()}")
    gallery_items = page.locator('#gallery-preview .gallery-item')
    print(f"Gallery items found: {gallery_items.count()}")

    # 7. News (Newsletter) Check
    news_section = page.locator('#news')
    print(f"News section visible: {news_section.is_visible()}")

    # 8. Contact Check
    contact_section = page.locator('#contact')
    print(f"Contact section visible: {contact_section.is_visible()}")

    # Take screenshot
    page.screenshot(path="/home/jules/verification/screenshots/layout_verification.png", full_page=True)
    page.wait_for_timeout(1000)

if __name__ == "__main__":
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            record_video_dir="/home/jules/verification/videos"
        )
        page = context.new_page()
        try:
            run_cuj(page)
        finally:
            context.close()
            browser.close()
