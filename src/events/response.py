import discord
from discord.ext import commands

# Core
# Test file to test importing external commands to main or other.

class greetingsResponse(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready():
        print(f"Response file is ready!")

    @commands.command
    async def hello2(self, ctx):
        await ctx.send(f"Hello from the response.py file!")

##### 
async def setup(bot):
    await bot.add_cog(greetingsResponse(bot))