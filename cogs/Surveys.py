import discord
from discord.ext import commands

from globalfuncs.EmbedBuilder import EmbedBuilder


def surveys() -> list[str]:
    surveys = [
        "https://forms.gle/",
        "https://docs.google.com/forms/",
        "https://www.surveymonkey.com/",
        "https://www.qualtrics.com/",
        "https://forms.office.com/",
    ]
    return surveys


class Surveys(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message) -> None:
        if message.channel.name != "surveys":
            for survey in surveys():
                if survey in message.content:
                    embed = EmbedBuilder(
                        title="Survey Link Detected",
                        description=f"Hey {message.author.mention}, it looks like you tried to post a survey link. If this is correct, please post survey links in the <#580936851360055296> channel instead! Thanks.",
                    ).build()
                    await message.channel.send(embed=embed)
        await self.bot.process_commands(message)


def setup(bot) -> None:
    bot.add_cog(Surveys(bot))