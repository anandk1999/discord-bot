import discord
from discord.ext import commands

class PingCog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    # Commands
    @commands.command(aliases=['latency'])
    async def ping(self, ctx):
        """Returns the bot bot latency"""
        await ctx.send(f'Pong! {round(self.bot.latency * 1000)}ms')

def setup(bot):
    bot.add_cog(PingCog(bot))