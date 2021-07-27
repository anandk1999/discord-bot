import discord
from discord.ext import commands

class PingCog(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Commands
    @commands.command(aliases=['latency'])
    async def ping(self, ctx):
        """Returns the bot client latency"""
        await ctx.send(f'Pong! {round(self.client.latency * 1000)}ms')

def setup(client):
    client.add_cog(PingCog(client))