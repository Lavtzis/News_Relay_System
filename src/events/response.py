# File at the moment has no use except testing when neccessary
import discord
from discord.ext import commands

# Test file to test importing external commands to main or other.

class responses(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready():
        print(f"Response file is ready!")

##### 
async def setup(bot):
    await bot.add_cog(responses(bot))