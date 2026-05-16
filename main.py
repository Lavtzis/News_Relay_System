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
bot = commands.Bot(command_prefix='!n', intents=intents)

##### Bot Run Token -- DONT TOUCH
bot.run(token, log_handler=handler, log_level=logging.DEBUG)

print("system reaches this places")