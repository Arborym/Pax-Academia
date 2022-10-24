import os

import discord
from dotenv import load_dotenv

from webcache import quilling

load_dotenv()
TOKEN: str = os.getenv("DISCORD_TOKEN")

bot = discord.Bot()


@bot.event
async def on_ready() -> None:
    print(f"We have logged in as {bot.user}")


@bot.slash_command(guild_ids=[883845473893482517])
async def correct_grammar(ctx, text: str) -> None:
    await ctx.respond("Correcting grammar...")
    corrected_text: str = await quilling(text)
    await ctx.respond(corrected_text)


bot.run(TOKEN)