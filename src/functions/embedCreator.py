# This file handles the construction/building of the embed structure. Changes here would reflect a change in every embed posted afterwards.
# This function is called automatically when a channel is selected. It is called every time, with all relevant information sent to it. It constructs the embed and then returns it.
# Currenlty expiremental as I do not know if embeds work like this
import discord
from discord.ext import commands


def create_Embed(titleIn, descIn, linkIn):

    embeds = []

    em = discord.Embed(title=titleIn)
    em.add_field(name="Test", value=descIn)

    embeds.append(em)

    # Debugging
    print("This files content is the following: ")
    print("1. " + titleIn)
    print("2. " + descIn)
    print ("3. " + linkIn)
    
    return embeds

# Testing direct output inside the file rather than Discord.
embedOut = create_Embed("News Flash!", "Firefighters save kitten from a tree!", "urlHere")
print(embedOut)
