from discord import Intents
from discord.ext import commands

import os
from dotenv import load_dotenv

load_dotenv(verbose=True)


class Client(commands.AutoShardedBot):
    def __init__(self):
        super().__init__(command_prefix="!", intents=Intents.all())
        for i in os.listdir("./extensions"):
            if i.endswith(".py"):
                self.load_extension(f"extensions.{i[:-3]}")
                print(f"Loaded {i}")

    async def on_ready(self):
        print(f"Logged in as {self.user}")


if __name__ == "__main__":
    Client().run(os.getenv("TOKEN"))
