import os
import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import datetime as dt

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

# Functions (Events & Commands) -- These will later on be separated into different files later on (In order to declutter the main.py file).
@bot.event
async def on_ready():
    print(f"system ready: {bot.user.name}")

    
##### Bot Run Token & Logging -- DONT TOUCH
bot.run(token, log_handler=handler, log_level=logging.DEBUG)