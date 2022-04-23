from discord.ext import commands

import os
from dotenv import load_dotenv

load_dotenv(verbose=True)


class Client(commands.AutoShardedBot):
    def __init__(self):
        super().__init__(command_prefix="!")

    async def on_ready(self):
        print(f"Logged in as {self.user}")


if __name__ == "__main__":
    Client().run(os.getenv("TOKEN"))
