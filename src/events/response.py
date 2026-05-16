import discord
from discord.ext import commands

# Core
bot = commands.Bot(command_prefix='!')

# Test file to test communication with a select channel on Discord.
@bot.command()
async def hello2(res):
    await res.send(f"Hello from the response.py file!")

print(f"Hello2 has been loaded successfully")