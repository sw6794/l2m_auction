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
		embed = discord.Embed(
				title = args[1],
				description= "11",
				color=0x0000ff
				)
        await ctx.send( embed=embed)

    elif num == 3:
        await ctx.send(num)
    else:
        return



bot.run(os.environ['token'])
