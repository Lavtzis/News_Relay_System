# This file handles all commands that can be issued by users with administrator privileges.
# Allows the termination of the bot through command. (Bot requires manual reactivation afterwards).
# Allows setting other users as administrators or removing them.
import discord
from discord.ext import commands

class administratorPanel(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def adminInfo(self, ctx):
        await ctx.channel.send("This is the administrator panel")

    # Commmands to be added
    #
    # - Shutdown command, to shutdown without need to turn off the server (COMPLETE SHUTDOWN)
    # - Halt command, bot ONLINE but doesn't post news anymore.
    # - Set Administrators, allows adding administrators who can use the administrator commands.
    # - Remove Administrators, removing administrators.
    # - Change rate, change the rate/delay at which articles are posted.

async def setup(bot):
    await bot.add_cog(administratorPanel(bot))