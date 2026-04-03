import asyncio
from playwright.async_api import Page
from utils import log_action, human_delay
from config import config

async def login(page: Page, username: str, password: str):
    await page.goto("https://www.instagram.com/accounts/login/", wait_until="networkidle")
    human_delay(3, 6)
    await page.fill('input[name="username"]', username)
    await page.fill('input[name="password"]', password)
    await page.click('button[type="submit"]')
    human_delay(8, 15)
    
    # Basic challenge detection
    if await page.get_by_text("We need to confirm it's you").is_visible(timeout=5000):
        print("🚨 Instagram challenge detected — manual intervention required.")
    log_action("LOGIN", "Successful", username)

async def like_post(page: Page, post_url: str, count: int, account: str):
    for i in range(count):
        if not config.dry_run:
            await page.goto(post_url, wait_until="networkidle")
            human_delay()
            like_btn = page.get_by_role("button", name="Like")
            if await like_btn.is_visible():
                await like_btn.click()
                log_action("LIKE", f"Post {post_url} ({i+1}/{count})", account)
        else:
            log_action("LIKE (DRY-RUN)", f"Would like {post_url}", account)
        human_delay()

async def comment_on_post(page: Page, post_url: str, text: str, count: int, account: str):
    for i in range(count):
        if not config.dry_run:
            await page.goto(post_url, wait_until="networkidle")
            human_delay()
            await page.get_by_role("textbox", name="Add a comment…").click()
            await page.fill('textarea', text)
            await page.keyboard.press("Enter")
            log_action("COMMENT", f"'{text}' on {post_url} ({i+1}/{count})", account)
        else:
            log_action("COMMENT (DRY-RUN)", f"Would comment '{text}'", account)
        human_delay()

async def follow_user(page: Page, target_username: str, count: int, account: str):
    for i in range(count):
        if not config.dry_run:
            await page.goto(f"https://www.instagram.com/{target_username}/", wait_until="networkidle")
            human_delay()
            follow_btn = page.get_by_text("Follow", exact=True)
            if await follow_btn.is_visible():
                await follow_btn.click()
                log_action("FOLLOW", f"{target_username} ({i+1}/{count})", account)
        else:
            log_action("FOLLOW (DRY-RUN)", f"Would follow {target_username}", account)
        human_delay()
