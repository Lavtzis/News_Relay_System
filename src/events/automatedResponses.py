import discord
from discord.ext import commands

# Core
# All automated responses like the on_ready fire from this file.
class automatedResponses(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"System ready: {self.bot.user.name}")

##### 
async def setup(bot):
    await bot.add_cog(automatedResponses(bot))