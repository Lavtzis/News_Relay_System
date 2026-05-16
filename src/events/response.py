import discord
from discord.ext import commands

# Core
# Test file to test communication with a select channel on Discord.

class greetingsResponse(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def hello2(res):
        await res.send(f"Hello from the response.py file!")

print(f"Hello2 has been loaded successfully")