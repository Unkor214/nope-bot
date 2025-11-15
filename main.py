import disnake
from disnake.ext import commands

from configparser import ConfigParser
from pathlib import Path


config = ConfigParser()
config.read(Path(__file__).resolve().parent / "config.ini")

intents = disnake.Intents.all()

bot = commands.Bot(command_prefix="n!", help_command=None, intents=intents)


@bot.event
async def on_ready():
    print(f"bot - {bot.user.name}, in online")


bot.load_extension("cogs")

bot.run(config["data"]["token"])