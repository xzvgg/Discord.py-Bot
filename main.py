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

# запуск
def time4logs():
    return f'[{datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")}]'
print(time4logs(), 'Запуск:')
start = time.time()

# включаем интенты и создаем переменную бота
intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix=settings['prefix'], intents=intents, help_command=None)

# коги
cogs_list = [
    'help',
    'test'
]

for cog in cogs_list:
    bot.load_extension(f'cogs.{cog}')

# бот запущен
@bot.event
async def on_ready(arg='playing', *, names=f'{settings["bot"]} | {settings["prefix"]}help') -> None:
    def time4logs():
        return f'[{datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")}]'
    print('\n', time4logs(), f"Статус: онлайн\n\n| Пинг: [{round(bot.latency * 1000)}] ms\n| Префикс: {settings['prefix']}\n\n--------------------\n")
    await bot.change_presence(activity=discord.Game(name=names))
    start = time.time()

# ошибки
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
       em = Embed(title=f"<:utility8:1025054226289786940> | Ошибка",description=f"> Перезарядка `{error.retry_after:.2f}` сек.", color=Color.red())
       await ctx.send(embed=em)
    elif isinstance(error, commands.CommandNotFound ):
        embed = Embed(title=f"<:utility8:1025054226289786940> | Ошибка",description=f"> Такой команды не существует", color=Color.red())
        await ctx.send(embed=embed)


bot.run(settings['token'])