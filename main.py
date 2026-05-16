import os
import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv

##### Core   

# dotenv
load_dotenv()
token = os.getenv('TOKEN')

# Logging (Debug & Crashes)
handler = logging.FileHandler(filename='discord_news.log', encoding='utf-8', mode='w')

# Discord Intents
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

# Command Settings
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f"System ready:, {bot.user.name}")

# Test Command -- Remove later on
@bot.command()
async def hello(ctx):
    await ctx.send(f"Hello there {ctx.author.mention}")

@bot.command()
async def terminate(ctx):
    print(f"Bot will be terminating...")
    await bot.close()


##### Bot Run Token -- DONT TOUCH
bot.run(token, log_handler=handler, log_level=logging.DEBUG)