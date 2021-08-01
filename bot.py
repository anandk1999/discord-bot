# Import all required packages and variables
import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents().all()

TOKEN = os.environ.get("TOKEN")
bot = commands.Bot(command_prefix='.', intents=intents)

# Bot initialized
@bot.event
async def on_ready():
    print(f'{bot.user.name} is ready.')
    await bot.change_presence(activity=discord.Streaming(name="Use .help to learn more!", url="https://linktr.ee/RutgersEsports"))

class CustomHelpCommand(commands.MinimalHelpCommand):
    async def send_pages(self):
        destination = self.get_destination()
        for page in self.paginator.pages:
            embed = discord.Embed(description=page, color=0xC94949)
            await destination.send(embed=embed)

bot.help_command = CustomHelpCommand()

# Cogs
for group in os.listdir('./cogs'):
    for cog in os.listdir(f'./cogs/{group}'):
        if cog.endswith('.py'):
            bot.load_extension(f'cogs.{group}.{cog[:-3]}')

bot.run(TOKEN)