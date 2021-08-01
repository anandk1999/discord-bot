import discord
from discord.ext import commands

class PruneCog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    # Commands
    @commands.command(aliases=['clear', 'prune'])
    @commands.has_permissions(manage_messages=True)
    async def purge(self, ctx, amount=10):
        """Removes a number of messages (10 by default)"""
        await ctx.channel.purge(limit=amount+1)
        await ctx.send(f'`{amount}` messages deleted.', delete_after=3)

def setup(bot):
    bot.add_cog(PruneCog(bot))