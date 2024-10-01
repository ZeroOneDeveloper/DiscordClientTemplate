from discord import app_commands, Interaction
from discord.ext import commands

from __main__ import Client


class Core(commands.Cog):
    def __init__(self, bot: Client):
        self.bot = bot

    @app_commands.command(name="ping", description="Check the bot's latency.")
    async def ping(self, interaction: Interaction):
        await interaction.response.send_message(
            f"Pong! 🏓 `{round(self.bot.latency * 1000)}ms`",
            ephemeral=True
        )


async def setup(bot: Client):
    await bot.add_cog(Core(bot))
