import io
import os

import discord
from discord import option
from discord.ext import commands
from playwright.async_api import async_playwright


class AI(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.slash_command(
        name="detectai", description="Runs text through an AI detector."
    )
    @option(
        "text",
        str,
        description="The text to run through the AI.",
        required=True,
    )
    async def ai(self, ctx: commands.Context, text: str) -> None:
        """
        It opens a headless browser, goes to the website, fills in the text, clicks the button, waits for
        the result, takes a screenshot of the result, closes the browser, and sends the screenshot to the
        channel

        :param ctx: commands.Context - The context of the command
        :type ctx: commands.Context
        :param text: str
        :type text: str
        """
        await ctx.defer(ephemeral=True)
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)
            context = await browser.new_context()
            page = await context.new_page()
            await page.goto("http://gltr.io/dist/index.html")
            await page.fill("textarea", text)
            await page.click("button")
            await page.wait_for_selector("text=top k count")
            screenshot = await page.locator("#all_result").screenshot()
            file_ = io.BytesIO(screenshot)
            await browser.close()
            await ctx.respond(file=discord.File(file_, filename="result.png"))


def setup(bot: commands.Bot) -> None:
    bot.add_cog(AI(bot))
