# This file is for the !setupTab command.
# It prints an embed panel to the user that shows a guide on how to setup the bot.
# - Select channel/s (Possibility of multiple channels will be added later on.)
# - Select Feed/s
import discord
from discord.ext import commands

class setupCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Command/Function name might be changed later on to something more appropriate.
    @commands.command()
    async def setupGuide(self, ctx):
        em = discord.Embed(title="Setup Guide", description="SETUP BOT TEXT, ADD LATER")
        await ctx.channel.send(embed=em)

async def setup(bot):
    await bot.add_cog(setupCommands(bot))