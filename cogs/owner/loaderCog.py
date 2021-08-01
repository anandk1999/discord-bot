import discord
from discord.ext import commands

class LoaderCog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    # Commands
    @commands.is_owner()
    @commands.command()
    async def load(self, ctx, extension):
        """Loads a cog"""
        self.bot.load_extension(f'cogs.{extension}')

    @commands.is_owner()
    @commands.command()
    async def unload(self, ctx, extension):
        """Unloads a cog"""
        self.bot.unload_extension(f'cogs.{extension}')

def setup(bot):
    bot.add_cog(LoaderCog(bot))