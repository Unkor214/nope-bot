import disnake
import pathlib
from disnake.ext import commands
from main import config
from configparser import ConfigParser

config = ConfigParser()
config.read(pathlib.Path(__file__).resolve().parent / 'config.ini')

class OnRemove(commands.Cog) :
    def __init__(self, bot):
        super().__init__()

        self.bot = bot

    @commands.Cog.listener()
    async def on_member_remove(self, member: disnake.Member) :
        await member.guild.get_channel(config['data']['helloGoodbyeChannel']).send(
            embed=disnake.Embed(
                title=f'Прощяй {member.display_name}! :sob:'
            ))