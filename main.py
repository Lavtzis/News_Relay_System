import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
import datetime as dt
import asyncio

##### Core  

# dotenv
load_dotenv()
token = os.getenv('TOKEN')

# Logging (Debug & Crashes)
from src.handlers.log_handler import logger
logger()

# Discord Intents
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

# Command Settings
ownerId = os.getenv('OWNER_ID')
bot = commands.Bot(command_prefix='!', intents=intents)

# Functions (Events & Commands) -- These will later on be separated into different files later on (In order to declutter the main.py file).
@bot.event
async def on_ready():   
    print(f"system ready: {bot.user.name}")
    
##### Bot Run Token & Logging -- DONT TOUCH
async def main():
    await bot.load_extension("src.commands.infoTab")
    await bot.load_extension("src.commands.administratorCommands")
    await bot.load_extension("src.commands.setupTab")
    await bot.load_extension("src.events.automatedResponses")
    await bot.start(token)

asyncio.run(main())