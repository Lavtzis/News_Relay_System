import discord
from discord.ext import commands

# Core
# Test file to test importing external commands to main or other.

class greetingsResponse(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def hello2(ctx):
        await ctx.send(f"Hello from the response.py file!")

print(f"Hello2 has been loaded successfully")