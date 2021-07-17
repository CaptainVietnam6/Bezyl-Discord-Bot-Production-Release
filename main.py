'''
Copyright (©) 2021 Kiet Pham <kiet.riley2005@gmail.com>
This software/program has a copyright license, more information is in the 'LICENSE' file
IF YOU WANT TO USE/COPY/MODIFY/REPRODUCE/RE-DISTRIBUTE THIS PROGRAM, YOU MUST INCLUDE A COPY OF THE LICENSE

Author Name(s): Kiet Pham
Co-Author Name(s): Junle Yan
Author Contact: kiet.riley2005@gmail.com, yanjunlereal@gmail.com
Discord: CaptainVietnam6#0001, wholefood_doufu#0001
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
import datetime as datetime
import youtube_dl
import shutil
import asyncio
import PyDictionary
from PyDictionary import PyDictionary

#imports from other files
from keep_alive import keep_alive
#from BOT_TOKEN import BOT_TOKEN #no longer needed, BOT_TOKEN now in main.py
from constants import bot_color
from constants import requested_by
from constants import auto_color
from constants import bot_typing


'''REFER TO NOTES OR MANUAL & INFORMATIVE SHEET AND USE THE INDEX TO UNDERSTAND AND SEE WHERE CERTAIN COMMANDS ARE'''

'''START OF IMPORTANT STUFF, DEALS WITH BOT AND INTERNAL COMMANDS'''

#INTENTS
intents = discord.Intents().all()


#BOT PREFIX
bot_prefixes = ["bz ", "BZ ", "Bz ", "bZ ", "bz", "BZ", "Bz", "bZ"]
client = commands.Bot(command_prefix = bot_prefixes, case_insensitive = True, intents = intents)


#REMOVES THE DEFAULT HELP COMMAND
#@client.remove_command("help")


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
    await client.change_presence(status = discord.Status.online, activity = discord.Game("Bot in Development"))
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


# RETURNS THE BOT'S PING IN MILLISECONDS
@client.command()
async def ping(ctx):
    # Latency Calculation
    start_time_b = datetime.datetime.now()
    await client.fetch_user(int(ctx.author.id))
    elapsed_b = datetime.datetime.now() - start_time_b
    restapilatency = str(round(elapsed_b.total_seconds()*1000, 4))
    before_ws = str(round(client.latency * 1000, 4))

    embed = discord.Embed(
        title = "Latency",
        description = "Successfully Received Message",
        color = auto_color(ctx)
    )
    embed.add_field(
        name = f"Websocket Latency:", 
        value = f"`{before_ws}` ms", 
        inline = False
    )
    embed.add_field(
        name = f"REST API Latency:", 
        value = f"`{restapilatency}` ms", 
        inline = False
    )

    requested_by(ctx, embed)#, auto_color(ctx, embed)
    await bot_typing(ctx, 0.15), await ctx.reply(embed = embed, mention_author = False)


#SERVER COLOR HEX CODE REMINDER THINGY
#color not finalised; subject to change
@client.command(aliases = ["botcolor"])
async def _bothexcode(ctx):
    await bot_typing(ctx, 0.15)
    await ctx.reply("The bot's theme color hex code is **#ff0000** (this is the average colour of the gradient in our pfp)", mention_author = False)


#SEND INVITE LINK FOR BOT
@client.command(aliases = ["invite"])
async def _invite(ctx):
    await bot_typing(ctx, 0.15)
    await ctx.reply("https://discord.com/api/oauth2/authorize?client_id=839638438055903242&permissions=0&scope=bot", mention_author = False)


#SEND LINK TO DOCS
@client.command(aliases = ["docs"])
async def _documentation(ctx):
    await bot_typing(ctx, 0.15)
    await ctx.reply("https://docs.google.com/document/d/1dNQBnMU0YK7g8-pjC77wViGKHBHNnE1NKbocAIf5HBA/edit?usp=sharing", mention_author = False)


#KEEP ALIVE COMMAND FOR WEBSERVER
keep_alive() 

#BOT TOKEN TO CONNECT TO DISCORD'S API
#this is the bot's token and will be required for the IDE to connect with discord's API
#get bot token from discord developer portal > applications > (your bot) > bot > copy token
BOT_TOKEN = os.environ["BOT_TOKEN_HIDDEN"]
client.run(BOT_TOKEN) #TOKEN CAN BE FOUND IN HIDDEN ENVIROMENTAL VARIABLES FILE
