import pathlib
import disnake
from disnake.ext import commands
from configparser import ConfigParser

config = ConfigParser()
config.read(pathlib.Path(__file__).resolve().parent / 'config.ini')

class OnJoin(commands.Cog):
    def __init__(self, bot):
        super().__init__()

        self.bot = bot

    @commands.Cog.listener()
    async def on_meber_join(self, member: disnake.Member):
        if member.bot:
            await member.add_roles(member.guild.get_role(config['role']['bot-role']))
        else:
            await member.add_roles(member.guild.get_role(config['role']['meber-role']))

        embed = disnake.Embed(
            title=f"{member.display_name}",
            description="",
            color=0xFFFFFF
        )
        embed.set_thumbnail(url=member.avatar)

        await member.guild.get_channel(config['data']['helloGoodbyeChannel']).send(embed=embed)
