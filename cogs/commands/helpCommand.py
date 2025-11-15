import disnake
from disnake.ext import commands


class HelpCommand(commands.Cog):
    def __init__(self, bot):
        super().__init__()

        self.bot = bot

    @commands.command(name="help")
    async def help_command(self, ctx: commands.Context):
        embed = disnake.Embed(
            title="~~моральная~~ помощь",
            description=f"текуший префикс: {self.bot.command_prefix}",
            colour=0xFFFFFF,
        )
        embed.add_field(
            name="Команда", value=f"{self.bot.command_prefix}exemple", inline=True
        )
        embed.add_field(
            name="Значение",
            value="*выполняет функцию* ~~выдование пиздюлей~~",
            inline=True,
        )

        await ctx.send(embed=embed)