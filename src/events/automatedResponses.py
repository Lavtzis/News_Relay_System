import discord
from discord.ext import commands
#import datetime as dt

# Core
# All automated responses like the on_ready fire from this file.
class automatedResponses(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"Automated responses ready: {self.bot.user.name}")
        channel = self.bot.get_channel(1488399642969374800)
        #dt.strftime("%d:%m:%Y:%H:%M")
        #time = dt.now()
        await channel.send(f"{time} - News Bot is Online.")

async def setup(bot):
    await bot.add_cog(automatedResponses(bot))