import discord
from discord.ext import commands
import os

bot = commands.Bot(command_prefix = '$')
@bot.event
async def on_ready():
  await bot.change_presence(status=discord.Status.online)
  await bot.change_presence(activity=discord.Game(name="@help"))
  print("봇 이름:",bot.user.name,"봇 아이디:",bot.user.id,"봇 버전:",discord.__version__)

@bot.command()
async def test(ctx, *args):
    num = len(args)
    if num == 2:
        await ctx.send(num)
    elif num == 3:
        await ctx.send(num)
    else:
        return



bot.run(os.environ['token'])
