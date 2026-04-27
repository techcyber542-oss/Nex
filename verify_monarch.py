from playwright.sync_api import sync_playwright
import os

def verify_monarch_os():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        # Use a larger viewport for better screenshots
        page = browser.new_page(viewport={'width': 1920, 'height': 1080})

        # Load the local index.html
        path = os.path.abspath("index.html")
        page.goto(f"file://{path}")

        # 1. Gate Screenshot
        page.screenshot(path="monarch_gate.png")

        # 2. Bypass gate to see main UI
        page.click("text=GUEST")
        page.wait_for_timeout(2000) # Wait for animations

        # 3. Hero and Header
        page.screenshot(path="monarch_hero.png")

        # 4. Games Section
        page.locator("#games").scroll_into_view_if_needed()
        page.wait_for_timeout(1000)
        page.screenshot(path="monarch_games.png")

        # 5. Apps Section
        page.locator("#apps").scroll_into_view_if_needed()
        page.wait_for_timeout(1000)
        page.screenshot(path="monarch_apps.png")

        # 6. Chat Hub
        page.locator("#chat").scroll_into_view_if_needed()
        page.wait_for_timeout(1000)
        page.screenshot(path="monarch_chat.png")

        # 7. Open Order Modal
        page.locator("#games-grid >> text=Roblox").scroll_into_view_if_needed()
        page.click("text=800 Robux")
        page.wait_for_timeout(1000)
        page.screenshot(path="monarch_modal.png")

        browser.close()

if __name__ == "__main__":
    verify_monarch_os()
