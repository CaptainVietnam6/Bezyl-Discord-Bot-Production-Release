#COGS WILL BE READ AND EXECUTEDIN MAIN.PY
#This cog is for the moderation category of commands

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
from constants import requested_by


class Cogs(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases = ["cogs_moderation"])
    async def _cogs_moderation(self, ctx):
        await ctx.send("moderation cog works yay")
    
    

def setup(client):
    client.add_cog(Cogs(client))
