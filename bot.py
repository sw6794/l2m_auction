import discord
from discord.ext import commands
import os
import random

bot = commands.Bot(command_prefix = '$')

@bot.event
async def on_ready():
  print(f'Logged in as {bot.user} (ID: {bot.user.id})')
  print('------')

@bot.command()
async def test(ctx, *args):
    num = len(args)
    if num == 2:
        return await ctx.send('**', args[1], '**\n`所持者(소지자) : ', args[0], '`')
    elif num == 3:
        return await ctx.send(num)
    else:
        return



bot.run(os.environ['token'])
