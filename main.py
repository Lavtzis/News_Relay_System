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
bot = commands.Bot(command_prefix='!', intents=intents)

# Functions (Events & Commands) -- These will later on be separated into different files later on (In order to declutter the main.py file).
@bot.event
async def on_ready():   
    print(f"system ready: {bot.user.name}")

# Deprecated - Used only for testing - Will be removed once Cog implementation is compplete
@bot.command()
async def oldBotInfo(ctx):
    embedVar = discord.Embed(title="News Relay System (Bot)", description="This is a Discord system/bot that relays news articles from an external database or feed into a specified Discord channel.")
    embedVar.add_field(name="!botInfo", value="Posts a panel with information about available commands and information relevant to this Bot.", inline=False)
    embedVar.add_field(name="!selectChannel", value="Select a channel by saying the channel ID you wish the bot to post the news articles in.", inline=False)
    await ctx.channel.send(embed=embedVar)
    # Use embeds similarly later on for the news articles. TEST WEBHOOKS
    
##### Bot Run Token & Logging -- DONT TOUCH
async def main():
    await bot.load_extension("src.commands.infoTab")
    await bot.load_extension("src.commands.administratorCommands")
    await bot.load_extension("src.events.automatedResponses")
    await bot.start(token)

asyncio.run(main())