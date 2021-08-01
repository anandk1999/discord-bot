import discord
from discord.ext import commands

class StatusCog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    # Commands
    @commands.command(aliases=['botstatus', 'stat'])
    @commands.is_owner()
    async def status(self, ctx):
        """Gives bot statistics"""
        # Total members of all servers bot is in
        total_guild_users = 0
        for guild in ctx.bot.guilds:
            total_guild_users += guild.member_count

        embed = discord.Embed(
            title=f"Bot Status",
            description=(f'`{ctx.bot.user.name}` is online.'
            f'\nBot is in `{len(ctx.bot.guilds)}` guilds.'
            f'\nGuilds have `{total_guild_users}` members.'),
            color=ctx.guild.get_member(ctx.bot.user.id).color
        )
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(StatusCog(bot))