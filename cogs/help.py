# библиотеки
import discord
from discord.ext import commands
import time
import datetime
from discord.ext.commands import MissingPermissions
from discord.utils import get
from discord import Intents
from discord import member
from config import settings
import json

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command()
    async def help(self, ctx):
        await ctx.send('Список команд')


def setup(bot):
    bot.add_cog(Help(bot))