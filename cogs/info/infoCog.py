import discord
from discord.ext import commands

class InfoCog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    # Commands
    @commands.command(aliases=['botinfo'])
    async def info(self, ctx):
        embed = discord.Embed(
            title=f"Rutgers Esports Bot <:RutgersEsports:608498339192766505>",
            description=(
                f'Rutgers Esports Bot is the official Discord bot\n'
                'for handling all internal Rutgers Esports operations.\n\n'
                '🔗 Check out Rutgers Esports '
                '[here](https://linktr.ee/RutgersEsports).\n'
                '🤖 To add this bot to your server use '
                '[this link](https://bit.ly/rutgers-esports-bot).\n'
                "⭐ Star our repo on GitHub [here](https://github.com/rutgersesports/discord-bot)."
            ),
            color=0xC94949
        )
        embed.set_thumbnail(url=ctx.bot.user.avatar_url)

        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(InfoCog(bot))