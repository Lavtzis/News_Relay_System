# This file is for the !setupTab command.
# It prints an embed panel to the user that shows a guide on how to setup the bot.
# - Select channel/s (Possibility of multiple channels will be added later on.)
# - Select Feed/s
import discord
from discord.ext import commands

class setupCommands(commands.cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command
    async def setupGuide(self, ctx):
        await ctx.channel.send("This will post the setup guide")

async def setup(bot):
    await bot.add_cog(setupCommands)