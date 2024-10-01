from discord import Intents, Object
from discord.ext import commands

import os
from dotenv import load_dotenv

load_dotenv(verbose=True)


class Client(commands.AutoShardedBot):
    def __init__(self):
        super().__init__(command_prefix="!", intents=Intents.all())

    async def on_ready(self) -> None:
        print(f"Logged in as {self.user}")

    async def setup_hook(self) -> None:
        for i in os.listdir("./extensions"):
            if i.endswith(".py"):
                await self.load_extension(f"extensions.{i[:-3]}")
                print(f"Loaded {i}")
        await self.tree.sync(guild=Object(id=866250605815136276))


if __name__ == "__main__":
    Client().run(os.getenv("TOKEN"))
