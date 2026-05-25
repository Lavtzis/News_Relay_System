# Configuration file holds data for variables like the embed's color on default posts (info, adminInfo etc.) and other minor variables, that can be changed by users through commands that will be implemented in the future.
import discord
from discord.ext import commands

# RSS / Feeds
FEED_URLS = []
POST_INTERVAL = 10 # REMINDER, number represents minutes, similarly to RSS' interval settings.

# Channels - Where the feeds will be posted at
CHANNEL = ''
#CHANNELS = [] # Currently unused, will be used later on so the bot can be post different feeds at different

# Misc
EMBED_COLOR = '' # Unused 