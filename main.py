'''
Copyright (©) 2021 Kiet Pham <kiet.riley2005@gmail.com>
This software/program has a copyright license, more information is in the 'LICENSE' file
IF YOU WANT TO USE/COPY/MODIFY/REPRODUCE/RE-DISTRIBUTE THIS PROGRAM, YOU MUST INCLUDE A COPY OF THE LICENSE

Author Name(s): Kiet Pham
Co-Author Name(s): Junle Yan
Author Contact: kiet.riley2005@gmail.com, yanjunlereal@gmail.com
Discord: CaptainVietnam6#0001, wholefood_doufu#9523
Discord Server: https://discord.gg/3z76p8H5yj
GitHub: https://github.com/CaptainVietnam6
GitHub Repo: https://github.com/CaptainVietnam6/Bezyl-Discord-Bot-Production-Release
Instagram: @itz_kietttttttttt
Program Status: ACTIVE - Production Release
'''

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
from keep_alive import keep_alive
from BOT_TOKEN import BOT_TOKEN
from constants import bot_color
from constants import requested_by


'''REFER TO NOTES OR MANUAL & INFORMATIVE SHEET AND USE THE INDEX TO UNDERSTAND AND SEE WHERE CERTAIN COMMANDS ARE'''

'''START OF IMPORTANT STUFF, DEALS WITH BOT AND INTERNAL COMMANDS'''

#INTENTS
intents = discord.Intents().all()


#BOT PREFIX
bot_prefixes = ["bz ", "BZ ", "Bz ", "bZ ", "bz", "BZ", "Bz", "bZ"]
client = commands.Bot(command_prefix = bot_prefixes, case_insensitive = True, intents = intents)


#REMOVES THE DEFAULT HELP COMMAND
@client.remove_command("help")


#LOAD cog
@client.command()
async def cogs_load(ctx, extension):
    user_id = ctx.author.id
    if user_id == 467451098735837186 or user_id == 597621743070216203:
        client.load_extension(f"cogs.{extension}")
    else:
        await ctx.send("Sorry, only developers of the bot can use this command")


#UNLOAD cog
@client.command()
async def cogs_unload(ctx, extension):
    user_id = ctx.author.id
    if user_id == 467451098735837186 or user_id == 597621743070216203:
        client.unload_extension(f"cogs.{extension}")
    else:
        await ctx.send("Sorry, only developers of the bot can use this command")


#RELOAD COG
@client.command()
async def cogs_reload(ctx, extension):
    user_id = ctx.author.id
    if user_id == 467451098735837186 or user_id == 597621743070216203:
        client.reload_extension(f"cogs.{extension}")
    else:
        await ctx.send("Sorry, only developers of the bot can use this command")


#CONNECTS COGS FILE 
for filename in os.listdir("./"):
    if filename.endswith("cog.py"):
        client.load_extension(f"{filename[:-3]}") #this will remove the last 3 characters off of the name ".py"


#ON READY AND ONLINE ALERT
@client.event
async def on_ready():
    await client.change_presence(status = discord.Status.online, activity = discord.Game("Programmed by CaptainVietnam6#0001 in Python 3.8.2"))
    await asyncio.sleep(float(1.5))
    print("Bezyl is online and ready")

    #notifications for CV6's Playground Server
    channel = client.get_channel(816179144961818634)
    await channel.send("Bezyl is online and ready")
    #notifications for CV6's Bots Server
    channel = client.get_channel(812974446801059860)
    await channel.send("Bezyl is online and ready")

    #joins CV6's Playground Server #beta-testing Voice Channel
    channel = client.get_channel(815933179378270208)
    await channel.connect()


#RETURNS THE BOT'S PING IN MILLISECONDS
@client.command()
async def ping(ctx):
    await ctx.trigger_typing()
    print(f"ping: {round(client.latency * 1000)}ms")
    embed = discord.Embed(
        title = "Latency",
        description = "Successfully Received Message",
        color = bot_color
    )
    embed.add_field(
        name = f"Websocket Latency:", 
        value = f"`{round(client.latency * 1000)}ms`", 
        inline = False
    )
    requested_by(ctx, embed)
    await asyncio.sleep(float(0.15))
    await ctx.send(embed = embed)


#SERVER COLOR HEX CODE REMINDER THINGY
@client.command(aliases = ["botcolor"])
async def _bothexcode(ctx):
    await ctx.trigger_typing()
    await asyncio.sleep(float(0.15))
    await ctx.send("The bot theme hex code is **#ff0000** (this is the average colour of the gradient in our pfp)")


#SEND INVITE LINK FOR BOT
@client.command(aliases = ["invite"])
async def _invite(ctx):
    await ctx.trigger_typing()
    await asyncio.sleep(float(0.15))
    await ctx.send("https://discord.com/api/oauth2/authorize?client_id=839638438055903242&permissions=0&scope=bot")


#SEND LINK TO DOCS
@client.command(aliases = ["docs"])
async def _documentation(ctx):
    await ctx.trigger_typing()
    await asyncio.sleep(float(0.15))
    await ctx.send("https://docs.google.com/document/d/1dNQBnMU0YK7g8-pjC77wViGKHBHNnE1NKbocAIf5HBA/edit?usp=sharing")


#KEEP ALIVE COMMAND FOR WEBSERVER
keep_alive()

#BOT TOKEN TO CONNECT TO DISCORD'S API
client.run(BOT_TOKEN) #TOKEN CAN BE FOUND IN HIDDEN ENVIROMENTAL VARIABLES FILE
 