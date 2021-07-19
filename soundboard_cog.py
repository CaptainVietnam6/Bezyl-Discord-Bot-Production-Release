#COGS WILL BE READ AND EXECUTEDIN MAIN.PY
#This cog is for the soundboard category of commands

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
from constants import bot_color
from constants import auto_color
from constants import requested_by
from constants import bot_typing


class Cogs(commands.Cog):
    def __init__(self, client):
        self.client = client

    #COG FUNCTIONALITY TEST COMMAND
    @commands.command(aliases = ["cogs_soundboard"])
    async def _cogs_soundboard(self, ctx):
        await ctx.send("soundboard cog works yay")

    @commands.group(invoke_without_command = True, aliases = ["sb", "soundboard"])
    async def _soundboard(self, ctx):
        author_name = ctx.display.author_name
        embed = discord.embed(
            title = "**Soundboard commands list**",
            description = "**These are commands that relate to voice channel soundboard features of CV6's PlaygroundBot**\n\nJoin VC: **cv6 join**\nLeave VC: **cv6 leave**\nAirhorn: **cv6 sb airhorn**\nAli-a intro: **cv6 sb alia**\nBegone thot: **cv6 sb begonethot**\nDamn son where'd you find this: **cv6 sb damnson**\nDankstorm: **cv6 sb dankstorm**\nDeez nuts: **cv6 sb deeznuts**\nDeja Vu: **cv6 sb dejavu**\nLook at this dude: **cv6 sb dis_dude**\nAnother fag left the chat: **cv6 sb fleft**\nFart: **cv6 sb fart**\nHah gaaayyy: **cv6 sb hahgay**\nIt's called hentai and it's art: **cv6 sb henart**\nIlluminati song: **cv6 sb illuminati**\nBitch Lasagna: **cv6 sb lasagna**\nLoser: **cv6 sb loser**\nNoob: **cv6 sb noob**\nOof sound: **cv6 sb oof**\nPickle Rick: **cv6 sb picklerick**\nNice: **cv6 sb nice**\nWhy don't we just relax and turn on the radio: **cv6 sb radio**\nRick roll: **cv6 sb rickroll**\nThis is sparta: **cv6 sb sparta**\nTitanic flute fail: **cv6 sb titanic**\nGTA V Wasted: **cv6 sb wasted**\nWide Putin: **cv6 wideputin**\nWubba lubba dub dub: **cv6 sb wubba**\n",
        color = bot_color
        )
        embed.set_footer(text = f"Requested by {author_name}")
        await bot_typing(ctx, 0.15)
        await ctx.send(embed = embed)

def setup(client):
    client.add_cog(Cogs(client))
