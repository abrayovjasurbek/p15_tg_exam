from playwright.async_api import async_playwright

url = 'https://kun.uz/'

async def kunuz():
    async with async_playwright() as playwright:
        browser = await playwright.firefox.launch(headless=True)
        context = await browser.new_context()
        page = await context.new_page()
        await page.goto(url)
        await page.screenshot(path='new.png')
        await browser.close()