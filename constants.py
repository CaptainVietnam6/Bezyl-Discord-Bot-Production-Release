#this is the file for any universal declarations or defines or whatever that will be imported into other files
#just do "from constants import {function_name}" to get it

#imports related to discord or discord packages
import discord
from discord.ext import commands
from discord.utils import get
from discord.ext.commands import cooldown
from discord.ext.commands import BucketType
from discord import FFmpegPCMAudio

#other important imports for system
import os
from os import system
import random
from random import randint
import time
import datetime
import youtube_dl
import shutil
import asyncio
import PyDictionary
from PyDictionary import PyDictionary

#imports from other files


#DEFINES BOT COLOR TO BE USED IN EMBEDS
#import into other files for use
bot_color = 0xff0000


#REQUESTED BY FOOTER FOR EMBEDS
def requested_by(ctx, embed, verb = "Requested"):
    author_name = ctx.author.name
    embed.set_footer(text = f"{verb} by {author_name}", icon_url = ctx.author.avatar_url)
    embed.timestamp = datetime.datetime.utcnow()


#AUTO COLOR IN EMBED ACCORDING TO HIGHEST ROLE OF THE BOT
def auto_color(ctx):
    roles = (ctx.message.guild.get_member(ctx.me.id)).roles 
    roles.reverse()
    return roles[0].color


#CUSTOM EMBED
def custom_embed(description, color, title = "Something doesn't seem right?"):
    embed = discord.Embed(title = title, description = description, color = color)
    return embed


#BOT TYPING DELAY
async def bot_typing(ctx, wait_time):
    await ctx.trigger_typing()
    await asyncio.sleep(float(wait_time))
