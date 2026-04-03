import asyncio
import typer
from rich.console import Console
from browser import create_stealth_context
from actions import login, like_post, comment_on_post, follow_user
from config import config

console = Console()
app = typer.Typer(help="Instagram Automation Research Tool — White-hat only")

@app.command()
async def login_command(username: str = typer.Option(None), password: str = typer.Option(None, prompt=True, hide_input=True)):
    console.print("[bold red]⚠️  WARNING: This tool violates Instagram ToS — Research use only![/bold red]")
    context = await create_stealth_context(config.proxy, config.headless)
    page = await context.new_page()
    await login(page, username or config.accounts[0].username, password)
    await context.close()

@app.command()
async def like(post_url: str, count: int = 10):
    console.print("[bold red]⚠️  WARNING: This tool violates Instagram ToS — Research use only![/bold red]")
    context = await create_stealth_context(config.proxy, config.headless)
    page = await context.new_page()
    for acc in config.accounts:
        await login(page, acc.username, acc.password or "")
        await like_post(page, post_url, count, acc.username)
    await context.close()

@app.command()
async def comment(post_url: str, text: str, count: int = 5):
    console.print("[bold red]⚠️  WARNING: This tool violates Instagram ToS — Research use only![/bold red]")
    context = await create_stealth_context(config.proxy, config.headless)
    page = await context.new_page()
    for acc in config.accounts:
        await login(page, acc.username, acc.password or "")
        await comment_on_post(page, post_url, text, count, acc.username)
    await context.close()

@app.command()
async def follow(username: str, count: int = 10):
    console.print("[bold red]⚠️  WARNING: This tool violates Instagram ToS — Research use only![/bold red]")
    context = await create_stealth_context(config.proxy, config.headless)
    page = await context.new_page()
    for acc in config.accounts:
        await login(page, acc.username, acc.password or "")
        await follow_user(page, username, count, acc.username)
    await context.close()

if __name__ == "__main__":
    asyncio.run(app())
