import random
from fake_useragent import UserAgent
from playwright.async_api import async_playwright
from utils import log_action

ua = UserAgent(browsers=["chrome"], os=["windows", "macos", "linux"])

async def create_stealth_context(proxy: str | None = None, headless: bool = False):
    async with async_playwright() as p:
        browser = await p.chromium.launch(
            headless=headless,
            args=["--disable-blink-features=AutomationControlled", "--no-sandbox"]
        )
        
        context = await browser.new_context(
            user_agent=ua.random,
            viewport={"width": random.randint(1280, 1920), "height": random.randint(720, 1080)},
            locale=random.choice(["en-US", "en-GB", "fr-FR", "de-DE"]),
            timezone_id=random.choice(["America/New_York", "Europe/London", "Asia/Tokyo"]),
            proxy={"server": proxy} if proxy else None,
        )
        
        await context.add_init_script("""
            Object.defineProperty(navigator, 'webdriver', {get: () => undefined});
        """)
        
        await context.storage_state(path="session.json")
        print("✅ Stealth browser context created with randomized fingerprint")
        return context
