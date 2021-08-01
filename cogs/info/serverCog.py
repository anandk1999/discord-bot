import discord
from discord.ext import commands

class ServerCog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    # Commands
    @commands.command(aliases=['server', 'sinfo'])
    async def serverinfo(self, ctx):
        """Get information about the current server"""
        guild = ctx.guild

        roles = str(len(guild.roles))
        emojis = str(len(guild.emojis))
        vchannels = str(len(guild.voice_channels))
        tchannels = str(len(guild.text_channels))

        embed = discord.Embed(title='Server info', description=guild.name, color=ctx.guild.get_member(ctx.bot.user.id).color)
        embed.set_thumbnail(url=guild.icon_url)
        embed.add_field(name='ID', value=guild.id, inline=True)
        embed.add_field(name='Owner', value=guild.owner, inline=True)
        embed.add_field(name='Members', value=guild.member_count, inline=True)
        embed.add_field(name='Text channels', value=tchannels, inline=True)
        embed.add_field(name='Voice channels', value=vchannels, inline=True)
        embed.add_field(name='Created on', value=guild.created_at.strftime('%B %d, %Y'), inline=True)
        embed.add_field(name='Region', value=guild.region, inline=True)
        embed.add_field(name='Roles', value=roles, inline=True)
        embed.add_field(name='Verification', value=guild.verification_level, inline=True)

        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(ServerCog(bot))