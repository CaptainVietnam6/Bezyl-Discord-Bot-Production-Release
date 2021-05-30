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
from constants import auto_color
from constants import bot_typing
from constants import requested_by


class Cogs(commands.Cog):
    def __init__(self, client):
        self.client = client

    #COG FUNCTIONALITY TEST COMMAND
    @commands.command(aliases = ["cogs_moderation"])
    async def _cogs_moderation(self, ctx):
        await ctx.send("moderation cog works yay")

    
    #MEMBER ID GET
    @commands.command(aliases = ["id", "getid"])
    async def _get_member_id(self, ctx, *, user: discord.User):
        embed = discord.Embed(
            title = "Requested User ID",
            description = f"{user.id}",
            color = bot_color #first declare color variable when using auto_color
        )
        auto_color(ctx, embed) #function cannot be called inside the embed, change outside
        requested_by(ctx, embed)

        await bot_typing(ctx, 0.15)
        await ctx.send(embed = embed)


    #VOTEKICK COMMAND
    @commands.command(aliases = ["votekick"])
    @commands.cooldown(1, 60, BucketType.guild)
    async def _votekick(self, ctx, user_tag, *, kick_reason = "None Provided"): 
        thumbs_down = "👎"
        thumbs_up = "👍"
        embed = discord.Embed(
            title = "Votekick Member",
            description = f"Votekick for member {user_tag}\nReason: {kick_reason}",
            color = bot_color
        )
        auto_color(ctx, embed) 
        requested_by(ctx, embed)

        await bot_typing(ctx, 0.15)
        embed_message = await ctx.send(embed = embed)
        await embed_message.add_reaction(thumbs_up)
        await embed_message.add_reaction(thumbs_down)
    
    #cooldown error for Votekick command
    @_votekick.error
    async def _votekick_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await bot_typing(ctx, 0.15)
            await ctx.send(f"Command on cooldown wait {error.retry_after:.2f} seconds")

    
    #KICK COMMAND
    @commands.command(aliases = ["kick"])
    #@commands.has_permissions(kick_members = True)
    async def _kick(self, ctx, member: str, *, reason = "None provided"):
        try: 
            member = await discord.ext.commands.MemberConverter().convert(ctx, member)
        except discord.ext.commands.errors.BadArgument:
            try:
                # fetch user with id if member not mention
                member = await self.bot.fetch_user(int(member))
            except:
                return
        
        embed = discord.Embed(
            title = "User Kicked",
            description = f"Kicked User <@{member}>\nReason: {reason}",
            color = bot_color
        )
        auto_color(ctx, embed) 
        requested_by(ctx, embed)

        await bot_typing(ctx, 0.15)
        await member.kick(reason = reason)
        await ctx.send(embed = embed)

    #error for kick commands
    #@_kick.error
    #async def _kick_error(self, ctx, error):
        #await bot_typing(ctx, 0.15)
        #await ctx.send("Error: No kick permissions or invalid parameter")

    #BAN COMMAND
    @commands.command(aliases = ["ban"])
    @commands.has_permissions(ban_members = True)
    async def _ban(self, ctx, member: str, *, reason = "None provided"):
        try: 
            member = await discord.ext.commands.MemberConverter().convert(ctx, member)
        except discord.ext.commands.errors.BadArgument:
            try:
                # fetch user with id if member not mention
                member = await self.bot.fetch_user(int(member))
            except:
                return
        embed = discord.Embed(
            title = "User Banned",
            description = f"Banned User {member}\nReason: {reason}",
            color = bot_color
        )
        auto_color(ctx, embed) 
        requested_by(ctx, embed)

        await bot_typing(ctx, 0.15)
        await member.ban(reason = reason)
        await ctx.send(embed = embed)

    #error for kick commands
    @_ban.error
    async def _ban_error(self, ctx, error):
        await bot_typing(ctx, 0.15)
        await ctx.send("Error: No kick permissions or invalid parameter")


def setup(client):
    client.add_cog(Cogs(client))
