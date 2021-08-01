import os
import discord
import DiscordUtils
import asyncio
from google.cloud import firestore
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

class InventoryCog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    # Commands
    # Get a single item from inventory
    @commands.command(aliases=['inv'])
    @commands.is_owner()
    async def inventory(self, ctx, arg1):
        """Get a single item from the inventory database"""

        # Make single input embed
        def single_embed(item, id):
            embed = discord.Embed(title=item["item_name"], description=id)
            if item["item_type"] != "": embed.add_field(name="Item Type", value=item["item_type"], inline=True)
            if item["color"] != "": embed.add_field(name="Color", value=item["color"], inline=True)
            if item["brand"] != "": embed.add_field(name="Brand", value=item["brand"], inline=True)
            if item["model"] != "": embed.add_field(name="Model", value=item["model"], inline=True)
            if item["size"] != "": embed.add_field(name="Size", value=item["size"], inline=True)
            if item["quantity"] != "": embed.add_field(name="Quantity", value=item["quantity"], inline=True)
            if item["box"] != "": embed.add_field(name="Box", value=item["box"], inline=True)
            return embed

        # Connect to Firestore DB inventory collection and get the item arg1 as doc
        if "INVENTORY_PROJECT_ID" in os.environ and "GOOGLE_APPLICATION_CREDENTIALS" in os.environ:
            try:
                db = firestore.AsyncClient(project=os.environ.get("INVENTORY_PROJECT_ID"))
                inventory_ref = db.collection("inventory").document(arg1)
                doc = await inventory_ref.get()

                if doc.exists:
                    await ctx.send(embed=single_embed(doc.to_dict(), doc.id))
                else:
                    await ctx.send("That ID doesn't exist!")
            except:
                await ctx.send("The DB connection is not working.")
        elif "INVENTORY_PROJECT_ID" not in os.environ and "GOOGLE_APPLICATION_CREDENTIALS" in os.environ:
            await ctx.send("Inventory Project ID not found!")
        elif "GOOGLE_APPLICATION_CREDENTIALS" not in os.environ:
            await ctx.send("GAPP Credentials not found!")

    @inventory.error
    async def inventory_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Missing required argument! (e.g. d!inventory __10000__)")
        if isinstance(error, commands.NotOwner):
            await ctx.send("You do not have permissions to run this command.")

def setup(bot):
    bot.add_cog(InventoryCog(bot))