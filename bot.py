import discord
from discord.ext import commands
import os

client = commands.Bot(command_prefix = '/')

@client.command(name='auction')
async def auction(ctx, *arg):
    await ctx.send('{} arguments: {}'.format(len(args), ', '.join(args)))


@client.event
async def on_ready():
  await client.change_presence(status=discord.Status.online)
  await client.change_presence(activity=discord.Game(name="@help"))
  print("봇 이름:",client.user.name,"봇 아이디:",client.user.id,"봇 버전:",discord.__version__)

client.run(os.environ['token'])
