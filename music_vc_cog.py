#imports related to discord or discord packages
import discord
from discord.ext import commands

class Cogs(commands.Cog):
    def __init(self, client):
        self.client = client

    @commands.command()
    async def cogs_test5(self, ctx):
        await ctx.send("cogs works yay")

def setup(client):
    client.add_cog(Cogs(client))