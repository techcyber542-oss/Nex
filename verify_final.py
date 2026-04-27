import asyncio
from playwright.async_api import async_playwright
import os

async def verify():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        context = await browser.new_context(viewport={'width': 1280, 'height': 800})
        page = await context.new_page()

        # Load the file
        curr_dir = os.getcwd()
        file_path = f"file://{curr_dir}/index.html"
        await page.goto(file_path)
        await asyncio.sleep(2)

        # Screenshot of the Gate
        await page.screenshot(path="final_gate.png")

        # Bypass Gate
        await page.click("button:has-text('BYPASS')")
        await asyncio.sleep(2)

        # Screenshot of the Hero
        await page.screenshot(path="final_hero.png")

        # Scroll to Games
        await page.evaluate("window.scrollTo(0, 1000)")
        await asyncio.sleep(1)
        await page.screenshot(path="final_games.png")

        # Click an order button (using text to find one)
        # We know Roblox 800 is there
        try:
            await page.click("button:has-text('800 Robux')")
            await asyncio.sleep(1)
            await page.screenshot(path="final_modal.png")
        except Exception as e:
            print(f"Could not click modal: {e}")

        await browser.close()

if __name__ == "__main__":
    asyncio.run(verify())
