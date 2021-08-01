import discord
from discord.ext import commands

class SayCog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    # Commands
    @commands.command(aliases=['speak'])
    @commands.is_owner()
    async def say(self, ctx, *, content):
        """Lets the bot say given arguments"""
        await ctx.message.delete()
        await ctx.send(content)

def setup(bot):
    bot.add_cog(SayCog(bot))