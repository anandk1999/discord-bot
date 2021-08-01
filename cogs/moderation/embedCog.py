import discord
from discord.ext import commands

class EmbedCog(commands.Cog):

	def __init__(self, bot):
		self.bot = bot

	# Commands
	@commands.command()
	async def embed(self, ctx, *, data):
		"""Produces a customizable embed"""
		# Split arguments into a list
		data = data.split("%%")

		# Set default channel to current channel where command is used
		channel = ctx.channel

		# Remove [''] surrounding possible channel argument input (slice value to just channel ID)
		possible_channel = data[0].rstrip()[2:-1]

		# Set channel if channel argument is given
		try:
			channel = await commands.TextChannelConverter().convert(ctx, possible_channel)
			data.pop(0)
		except Exception as e:
			pass

		# Check if user has permission to send in given channel
		if not ctx.guild.get_member(ctx.author.id).permissions_in(channel).send_messages:
			return await ctx.send(f"You don't have permission to send messages to {channel.mention}!")


		# Add possible empty list values to deter IndexError for embed
		data += [""] * (3-len(data))

		# Create and send embed
		embed = discord.Embed(
			title=f"{data[0]}",
			description=f"{data[1]}",
			color=ctx.guild.get_member(ctx.bot.user.id).color
			)
		embed.set_footer(
			text=f"{data[2]}"
			)
		await channel.send(embed=embed)

	@embed.error
	async def embed_error(self, ctx, error):
		await ctx.send(
			"Type the command in the following format:```.embed #channel_name %% title %% description %% footer```"
			)
		embed = discord.Embed(
			title="Title",
			description="Description",
			color=ctx.guild.get_member(ctx.bot.user.id).color
			)
		embed.set_footer(
			text="Footer"
			)
		await ctx.send(embed=embed)

def setup(bot):
	bot.add_cog(EmbedCog(bot))