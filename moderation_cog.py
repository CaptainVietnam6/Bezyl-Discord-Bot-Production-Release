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
from constants import auto_color, bot_typing, requested_by, custom_embed


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
            color = auto_color(ctx)
        )
        requested_by(ctx, embed)

        await bot_typing(ctx, 0.15)
        await ctx.send(embed = embed)


    #VOTEKICK COMMAND
    @commands.command(aliases = ["votemod"])
    @commands.cooldown(1, 60, BucketType.guild)
    async def _votemod(self, ctx, member: str, *, reason = "None provided"): 
        try:
            member = await discord.ext.commands.MemberConverter().convert(ctx, member) #create user object using mention or id
            thumbs_down, thumbs_up = "👎", "👍"
            embed = custom_embed(f"Vote to take actions against {member.mention}", auto_color(ctx), "Poll Started")
            embed.add_field(name = "**Reason**", value = reason)
            requested_by(ctx, embed, "Initialized")
            embed.set_thumbnail(url = member.avatar_url)
            await bot_typing(ctx, 0.15)
            embed_message = await ctx.reply(embed = embed, mention_author = False)
            await embed_message.add_reaction(thumbs_up)
            await embed_message.add_reaction(thumbs_down)

        except: # error response for invalid mention or id
            embed = custom_embed(f"User: `{member}` could not be found!", auto_color(ctx))
            requested_by(ctx, embed)
            await bot_typing(ctx, 0.15)
            await ctx.reply(embed = embed, mention_author = False)

    #cooldown error for votekick command
    @_votemod.error
    async def _votemod_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            embed = custom_embed(f"This command is on cooldown. Try again in {error.retry_after:.2f} seconds", auto_color(ctx))
            requested_by(ctx, embed)
            await bot_typing(ctx, 0.15)
            await ctx.reply(embed = embed, mention_author = False)
        
        elif isinstance(error, commands.MissingRequiredArgument): # error response for if the bot doesnt have perm
            embed = custom_embed("One or more of the paramaters needed for this command is missing.", auto_color(ctx))
            requested_by(ctx, embed)
            await bot_typing(ctx, 0.15)
            await ctx.reply(embed = embed, mention_author = False)
        
        else:
            raise

    
    #KICK COMMAND
    @commands.command(aliases = ["kick"])
    @commands.has_permissions(kick_members = True)
    @commands.bot_has_permissions(kick_members = True)
    async def _kick(self, ctx, member: str, *, reason = "Moderator did not specify a reason."):
        try: 
            member = await discord.ext.commands.MemberConverter().convert(ctx, member) # creates user object using id or mention
            if str(ctx.author.id) != str(member.id): # check if user object is the author of command
                if ctx.author.top_role > member.top_role: # check if author have a higher rank than the user object
                    if ctx.me.top_role > member.top_role: # check if bot have a higher rank than the user object
                        embed = custom_embed(f"Kicked User: {member.mention}", auto_color(ctx), "Successfully Kicked")
                        dm_embed = custom_embed(f"You have been kicked out of {ctx.guild.name} by {ctx.author.mention} \n for the following reason: \n ```{reason}```", auto_color(ctx), "Kicked")
                        embed.add_field(name = "**Reason**", value = f"{reason}")
                        requested_by(ctx, embed)
                        await bot_typing(ctx, 0.15)
                        await member.kick(reason = reason)
                        await ctx.reply(embed = embed, mention_author = False)
                        await member.send(embed = dm_embed)
                    else: 
                        embed = custom_embed("I can only kick members below my rank.", auto_color(ctx))
                        requested_by(ctx, embed)
                        await bot_typing(ctx, 0.15)
                        await ctx.reply(embed = embed, mention_author = False)
                else:
                    embed = custom_embed("You can only kick members below your rank.", auto_color(ctx))
                    requested_by(ctx, embed)
                    await bot_typing(ctx, 0.15)
                    await ctx.reply(embed = embed, mention_author = False)
            else: 
                embed = custom_embed("You can't kick yourself!", auto_color(ctx))
                requested_by(ctx, embed)
                await bot_typing(ctx, 0.15)
                await ctx.reply(embed = embed, mention_author = False)

        except discord.ext.commands.errors.BadArgument:
            # error response for invalid member parameter and id
            embed = custom_embed(f"User: `{member}` could not be found!", auto_color(ctx))
            requested_by(ctx, embed)
            await bot_typing(ctx, 0.15)
            await ctx.reply(embed = embed, mention_author = False)
            

    #error for kick command
    @_kick.error
    async def _kick_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions): # error response for if the author doesnt have perm
            embed = custom_embed("You do not have permission to use `kick`.", auto_color(ctx))
            requested_by(ctx, embed)
            await bot_typing(ctx, 0.15)
            await ctx.reply(embed = embed, mention_author = False)
        elif isinstance(error, commands.BotMissingPermissions): # error response for if the bot doesnt have perm
            embed = custom_embed("I am missing the permissions needed to perform this action.", auto_color(ctx))
            requested_by(ctx, embed)
            await bot_typing(ctx, 0.15)
            await ctx.reply(embed = embed, mention_author = False)
        elif isinstance(error, commands.MissingRequiredArgument): # error response for if the bot doesnt have perm
            embed = custom_embed("One or more of the paramaters needed for this command is missing.", auto_color(ctx))
            requested_by(ctx, embed)
            await bot_typing(ctx, 0.15)
            await ctx.reply(embed = embed, mention_author = False)
        elif isinstance(error, commands.CommandInvokeError): # error response for if the bot doesnt have perm
            pass
        else:
            raise


    #BAN COMMAND
    @commands.command(aliases = ["ban"])
    @commands.has_permissions(ban_members = True)
    @commands.bot_has_permissions(ban_members = True)
    async def _ban(self, ctx, member: str, *, reason = "Moderator did not specify a reason."):
        try: 
            member = await discord.ext.commands.MemberConverter().convert(ctx, member) # creates user object using mention or id
            if str(ctx.author.id) != str(member.id): # check if user object is the author
                if ctx.author.top_role > member.top_role: # check if author have higher rank than the user object
                    if ctx.me.top_role > member.top_role: # check if bot have higher rank than the user object
                        embed = custom_embed(f"Banned User: {member.mention}", auto_color(ctx), "Successfully Banned")
                        dm_embed = custom_embed(f"You have been banned from {ctx.guild.name} by {ctx.author.mention} \n for the following reason: \n ```{reason}```", auto_color(ctx), "Banned")
                        embed.add_field(name = "**Reason**", value = f"{reason}")
                        requested_by(ctx, embed)
                        await bot_typing(ctx, 0.15)
                        await member.ban(reason = reason)
                        await ctx.reply(embed = embed, mention_author = False)
                        await member.send(embed = dm_embed)
                    else: 
                        embed = custom_embed(f"I can only ban members below my rank.", auto_color(ctx))
                        requested_by(ctx, embed)
                        await bot_typing(ctx, 0.15)
                        await ctx.reply(embed = embed, mention_author = False)
                else:
                    embed = custom_embed(f"You can only ban members below your rank.", auto_color(ctx))
                    requested_by(ctx, embed)
                    await bot_typing(ctx, 0.15)
                    await ctx.reply(embed = embed, mention_author = False)
            else: 
                embed = custom_embed(f"You can't ban yourself!", auto_color(ctx))
                requested_by(ctx, embed)
                await bot_typing(ctx, 0.15)
                await ctx.reply(embed = embed, mention_author = False)

        except:
            try:
                user = await self.client.fetch_user(member) # handles user outside of the server
                await ctx.guild.ban(user)
                embed = custom_embed(f"User: {user.mention} is now prohibited from entering the server!", auto_color(ctx), "Successfully Banned")
                embed.add_field(name = "**Reason**", value = f"{reason}"), requested_by(ctx, embed)
                await bot_typing(ctx, 0.15),
                await ctx.reply(embed = embed, mention_author = False)

            except: # error response for invalid user id or mention
                embed = custom_embed(f"User: `{member}` could not be found!", auto_color(ctx))
                requested_by(ctx, embed)
                await bot_typing(ctx, 0.15)
                await ctx.reply(embed = embed, mention_author = False)
                raise

    #error for ban command
    @_ban.error
    async def _ban_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions): # error response for if the author doesnt have perms
            embed = custom_embed("You do not have permission to use `ban`.", auto_color(ctx))
            requested_by(ctx, embed), 
            await bot_typing(ctx, 0.15)
            await ctx.reply(embed = embed, mention_author = False)
        elif isinstance(error, commands.BotMissingPermissions): # error response for if the bot doesnt have perms
            embed = custom_embed("I am missing the permissions needed to perform this action.", auto_color(ctx))
            requested_by(ctx, embed), 
            await bot_typing(ctx, 0.15)
            await ctx.reply(embed = embed, mention_author = False)
        elif isinstance(error, commands.MissingRequiredArgument): # error response for if the bot doesnt have perms
            embed = custom_embed("One or more of the paramaters needed for this command is missing.", auto_color(ctx))
            requested_by(ctx, embed)
            await bot_typing(ctx, 0.15)
            await ctx.reply(embed = embed, mention_author = False)
        else:
            raise


    #UNBAN COMMAND
    @commands.command(aliases = ["unban"])
    @commands.has_permissions(ban_members = True)
    @commands.bot_has_permissions(ban_members = True)
    async def _unban(self, ctx, *, member: int):
        try:
            user = await self.client.fetch_user(member) #fetch user object from id
            try:
                await ctx.guild.fetch_ban(user) # this single line checks if the user is banned, returns an error if isnt banned
                embed = custom_embed(f"{user.mention} got unbanned!", auto_color(ctx), "Successfully Unbanned")
                requested_by(ctx, embed)
                await ctx.guild.unban(user)
                await bot_typing(ctx, 0.15)
                await ctx.reply(embed = embed, mention_author = False)

            except discord.NotFound: # error response for user that hasn't been banned
                embed = custom_embed(f"User: {user.mention} haven't been banned before.", auto_color(ctx))
                requested_by(ctx, embed), 
                await bot_typing(ctx, 0.15)
                await ctx.reply(embed = embed, mention_author = False)

        except: # error response for invalid user id
            embed = custom_embed(f"User: `{member}` could not be found!", auto_color(ctx))
            requested_by(ctx, embed)
            await bot_typing(ctx, 0.15)
            await ctx.reply(embed = embed, mention_author = False)
            raise
              
    #error for unban command
    @_unban.error
    async def _unban_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions): # error response for if the author doesnt have perm
            embed = custom_embed("You do not have permission to use `unban`.", auto_color(ctx))
            requested_by(ctx, embed), 
            await bot_typing(ctx, 0.15)
            await ctx.reply(embed = embed, mention_author = False)

        elif isinstance(error, commands.BotMissingPermissions): # error response for if the bot doesnt have perm
            embed = custom_embed("I am missing the permissions needed to perform this action.", auto_color(ctx))
            requested_by(ctx, embed), 
            await bot_typing(ctx, 0.15)
            await ctx.reply(embed = embed, mention_author = False)

        elif isinstance(error, commands.MissingRequiredArgument): # error response for if the bot doesnt have perm
            embed = custom_embed("One or more of the paramaters needed for this command is missing.", auto_color(ctx))
            requested_by(ctx, embed)
            await bot_typing(ctx, 0.15)
            await ctx.reply(embed = embed, mention_author = False)
        else:
            raise


    #WARN COMMAND
    @commands.command(aliases = ['warn'])
    @commands.check_any(commands.has_permissions(kick_members = True, ban_members = True))
    async def _warn(self, ctx, member: str, *, reason = "None provided"):
        try:
            member = await discord.ext.commands.MemberConverter().convert(ctx, member) #fetch user object from id
            embed = custom_embed(f"Warned User: {member.mention}", auto_color(ctx), "Warning Sent")
            dm_embed = custom_embed(f"You have received a warning \nfrom {ctx.guild.name} sent by {ctx.author.mention} \n for the following: \n ```{reason}```", auto_color(ctx), "Warning")
            embed.add_field(name = "**Reason**", value = f"{reason}")
            requested_by(ctx, embed)
            await bot_typing(ctx, 0.15)
            await ctx.reply(embed = embed, mention_author = False)
            await member.send(embed = dm_embed)

        except: # error response for invalid user id
            embed = custom_embed(f"User: `{member}` could not be found!", auto_color(ctx))
            requested_by(ctx, embed)
            await bot_typing(ctx, 0.15)
            await ctx.reply(embed = embed, mention_author = False)
            raise


def setup(client):
    client.add_cog(Cogs(client))
