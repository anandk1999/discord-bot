import os
import discord
import DiscordUtils
import datetime
from dateutil.parser import parse
import requests
from discord.ext import commands

class CalendarCog(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Commands
    @commands.command()
    async def events(self, ctx):
        """Gets all upcoming events from Google Calendar"""
        # Check if environment variable exists
        if not os.environ.get("GOOGLE_CALENDAR_ENDPOINT"):
            return await ctx.send("No Google Calendar endpoint specified!")

        # Get upcoming events data from calendar
        current_time = datetime.datetime.utcnow()
        formatted_time = current_time.isoformat("T") + "Z"
        calendar = os.environ.get("GOOGLE_CALENDAR_ENDPOINT") + "&timeMin=" + formatted_time
        data = requests.get(calendar).json()

        # Check if there are any events
        if not data["items"]:
            return await ctx.send("There are no upcoming events!")

        # Get all upcoming events as a list
        list_of_events = data["items"]
        embeds = []

        for event in list_of_events:
            # Create data set
            title = event["summary"]
            start_time = event["start"]["dateTime"]
            description = "No description."
            if "description" in event:
                description = event["description"]
            formatted_start_time = datetime.datetime.strftime(parse(start_time), format="%B %d, %Y")

            # Create embed for single event and add to embeds list
            embed = discord.Embed(color=ctx.author.color, title=title, description=description)
            embed.add_field(name="Starts On", value=formatted_start_time, inline=True)
            embeds.append(embed)

        # Create paginator
        paginator = DiscordUtils.Pagination.CustomEmbedPaginator(ctx)
        paginator.add_reaction('⏮️', "first")
        paginator.add_reaction('⏪', "back")
        paginator.add_reaction('⏩', "next")
        paginator.add_reaction('⏭️', "last")
        await paginator.run(embeds)

def setup(client):
    client.add_cog(CalendarCog(client))