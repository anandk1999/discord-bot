import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.environ.get("TOKEN")
client = commands.Bot(command_prefix= 'd!')

@client.event
async def on_ready():
    print(f'{client.user.name} is ready.')
    await client.change_presence(activity=discord.Streaming(name="duck pictures.", url="https://www.youtube.com/watch?v=dQw4w9WgXcQ"))

@commands.is_owner()
@client.command()
async def load(ctx, extension):
    """Loads a cog"""
    client.load_extension(f'cogs.{extension}')

@commands.is_owner()
@client.command()
async def unload(ctx, extension):
    """Unloads a cog"""
    client.unload_extension(f'cogs.{extension}')

# Subfolders
# for filename in os.listdir('./cogs/fun'):
#     if filename.endswith('.py'):
#         client.load_extension(f'cogs.fun.{filename[:-3]}')

# for filename in os.listdir('./cogs/general'):
#     if filename.endswith('.py'):
#         client.load_extension(f'cogs.general.{filename[:-3]}')

for filename in os.listdir('./cogs/info'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.info.{filename[:-3]}')

for filename in os.listdir('./cogs/moderation'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.moderation.{filename[:-3]}')

for filename in os.listdir('./cogs/music'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.music.{filename[:-3]}')

# for filename in os.listdir('./cogs/owner'):
#     if filename.endswith('.py'):
#         client.load_extension(f'cogs.owner.{filename[:-3]}')

for filename in os.listdir('./cogs/inventory'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.inventory.{filename[:-3]}')

client.run(TOKEN)