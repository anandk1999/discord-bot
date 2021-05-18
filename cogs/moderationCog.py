import discord
from discord.ext import commands

class ModerationCog(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Commands
    @commands.command()
    @commands.has_permissions(kick_members = True)
    async def kick(self, ctx, member : discord.Member, *, reason="No reason provided."):
        await ctx.send(member.mention + " has been kicked.")
        await member.send("You have been kicked from the server because: " + reason)
        await member.kick(reason=reason)

def setup(client):
    client.add_cog(ModerationCog(client))