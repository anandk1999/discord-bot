import os
import discord
from discord.ext import commands

TOKEN = os.environ.get("TOKEN")
client = commands.Bot(command_prefix= 'd!')

@client.event
async def on_ready():
    print(f'{client.user.name} is ready.')
    await client.change_presence(activity=discord.Streaming(name="duck pictures.", url="https://www.youtube.com/watch?v=dQw4w9WgXcQ"))

@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    
@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run(TOKEN)