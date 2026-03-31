import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

##### Main Branch   

load_dotenv()
token = os.getenv('TOKEN')

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='!n', intents=intents)

##### DONT TOUCH
bot.run(token)