from discord.ext import commands
from discord.ext.commands.context import Context

from __main__ import Client


class Core(commands.Cog):
    def __init__(self, bot: Client):
        self.bot = bot

    @commands.command(name="핑", aliases=["ping"])
    async def ping(self, ctx: Context):
        await ctx.reply("Pong! 🏓")


def setup(bot: Client):
    bot.add_cog(Core(bot))
