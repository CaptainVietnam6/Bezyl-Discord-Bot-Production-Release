#this is the file for any universal declarations or defines or whatever that will be imported into other files
#just do "from constants import {function_name}" to get iter

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
def requested_by(ctx, embed):
    author_name = ctx.author.display_name
    embed.set_footer(text = f"Requested by {author_name}")


#AUTO COLOR IN EMBED ACCORDING TO HIGHEST ROLE OF THE BOT
def auto_color(ctx, embed):
    roles = (ctx.message.guild.get_member(839638438055903242)).roles 
    roles.reverse()
    embed.color = roles[0].color


#BOT TYPING DELAY
async def bot_typing(ctx, time):
    await ctx.trigger_typing()
    await asyncio.sleep(float(time))
