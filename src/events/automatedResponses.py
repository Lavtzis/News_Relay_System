import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
#import datetime as dt

load_dotenv()
test_channel = int(os.getenv('TEST_CHANNEL'))

# Core
# All automated responses like the on_ready fire from this file.
class automatedResponses(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"Automated responses ready: {self.bot.user.name}")
        channel = self.bot.get_channel(test_channel)
        await channel.send(f"News Bot is Online.")

        #dt.strftime("%d:%m:%Y:%H:%M")
        #time = dt.datetime
        #await channel.send(f"{time} - News Bot is Online.")
        

async def setup(bot):
    await bot.add_cog(automatedResponses(bot))