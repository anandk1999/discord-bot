import discord
from discord.ext import commands

class PingCog(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Events
    @commands.Cog.listener()
    async def on_ready(self):
        print('Bot is online.')

    # Commands
    @commands.command(aliases=['latency'])
    async def ping(self, ctx):
        await ctx.send(f'Pong! {client.latency}ms')

def setup(client):
    client.add_cog(PingCog(client))