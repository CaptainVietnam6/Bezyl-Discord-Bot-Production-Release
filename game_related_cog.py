#COGS WILL BE READ AND EXECUTEDIN MAIN.PY
#This cog is for the game related category of commands

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
from constants import bot_typing
from constants import requested_by


class Cogs(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases = ["cogs_game"])
    async def _cogs_game(self, ctx):
        await ctx.send("game related cogs works yay")


def setup(client):
    client.add_cog(Cogs(client))
