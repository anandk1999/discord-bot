import discord
from discord.ext import commands

class ModerationCog(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Commands
    @commands.command()
    @commands.has_permissions(kick_members = True)
    async def kick(self, ctx, member : discord.Member, *, reason="No reason provided."):
        try:
            await member.kick(reason=reason)
            await ctx.send(member.mention + " has been kicked.")
        except:
            await ctx.send(f"Unable to kick {member.mention}.\nIs {member.mention} at the same role level or higher than {self.client.user.name}?")


    @commands.command()
    @commands.has_permissions(ban_members = True)
    async def ban(self, ctx, member : discord.Member, *, reason="No reason provided."):
        try:
            await member.ban(reason=reason)
            await ctx.send(member.mention + " has been banned.")
        except:
            await ctx.send(f"Unable to ban {member.mention}.\nIs {member.mention} at the same role level or higher than {self.client.user.name}?")

def setup(client):
    client.add_cog(ModerationCog(client))