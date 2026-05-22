# This file handles the construction/building of the embed structure. Changes here would reflect a change in every embed posted afterwards.
# This function is called automatically when a channel is selected. It is called every time, with all relevant information sent to it. It constructs the embed and then returns it.
# Currenlty expiremental as I do not know if embeds work like this
import discord
from discord.ext import commands


def embedGenerator(titleIn, descIn):

    embedVar = discord.Embed(title=titleIn)
    embedVar.add_field(name="Test", value=descIn)

    # Debugging
    print(titleIn)
    print(descIn)
    
    return embedVar

embedOut = embedGenerator("hi", "desc")

print(embedOut)