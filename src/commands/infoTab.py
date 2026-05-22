# Command that when ran posts an embed with a list of all available commands, including a description of their functionality, preferably short if possible.
import discord
from discord.ext import commands

class infoCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None
    
    @commands.command()
    async def info(self, ctx):
        em = discord.Embed(title="News Relay System (Bot)", description="This is a Discord system/bot that relays news articles from an external database or feed into a specified Discord channel.")
        #em.color(0x1ABC9C)
        em.add_field(name="!botInfo", value="Posts a panel with information about available commands and information relevant to this Bot.", inline=False)
        em.add_field(name="!selectChannel", value="Select a channel by saying the channel ID you wish the bot to post the news articles in.", inline=False)
        em.add_field(name="!adminInfo", value="A command for administrators that allows them to check what commands they can use.")
        await ctx.channel.send(embed=em)

async def setup(bot):
    await bot.add_cog(infoCommands(bot))

