# Command that when ran posts an embed with a list of all available commands, including a description of their functionality, preferably short if possible.
import discord
from discord.ext import commands

class infoTab(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None
    
    @commands.command()
    async def info(self, ctx):
        await ctx.send(f"This message was posted successfully!")

async def setup(bot):
    await bot.add_cog(infoTab(bot))

