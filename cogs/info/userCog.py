import discord
from discord.ext import commands

class UserCog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    # Commands
    @commands.command(aliases=['whois'])
    async def userinfo(self, ctx, member: discord.Member = None):
        """Get information about a given user"""
        # Gather data
        member = ctx.author if not member else member
        roles = [role for role in member.roles]
        default_role = discord.utils.get(member.guild.roles, name='@everyone')
        role_mentions = [f'{role.mention}' for role in sorted(member.roles, key=lambda x: x.position, reverse=True) if role != default_role]
        all_perms = [x for x in dir(ctx.channel.permissions_for(member))]
        permissions = []
        for perm in all_perms:
            perm_name = perm
            if getattr(ctx.channel.permissions_for(member), perm_name) is True:
                permissions.append(perm_name.title().replace("_", " ").replace("Tts", "TTS"))

        # Create embed
        embed = discord.Embed(description = member.mention, color = member.color, timestamp = ctx.message.created_at)

        embed.set_author(name = member, icon_url = member.avatar_url)
        embed.set_thumbnail(url = member.avatar_url)
        embed.set_footer(text = member.id)

        embed.add_field(name = 'Joined', value = member.joined_at.strftime('%a, %d %B %Y, %I:%M %p UTC'), inline=True)
        embed.add_field(name = 'Registered', value = member.created_at.strftime('%a, %d %B %Y, %I:%M %p UTC'), inline=True)

        embed.add_field(name=f'Roles [{len(roles)}]', value=", ".join(role_mentions)+f', {default_role}', inline=False)
        embed.add_field(name=f'Permissions [{len(permissions)}]', value=", ".join(permissions), inline=False)
        

        embed.add_field(name='Nickname', value=member.nick if hasattr(member, 'nick') else 'None', inline=True)

        await ctx.send(embed = embed)

def setup(bot):
    bot.add_cog(UserCog(bot))