import discord
from discord.ext import commands
from discord import NotFound
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
        embed=discord.Embed()
        embed.add_field(name="ITEM", value=args[1], inline=True)
        embed.add_field(name="所持者(소지자)", value=args[0], inline=True)
        embed.set_footer(text="参加者は以下に絵文字をクリックしてください。\n참여를 원하시면 이모티콘으로 반응해주세요.")

        msg = await ctx.send(embed = embed)
        await msg.add_reaction("✅")
    else:
        return

@bot.command()
async def end(ctx, msgID: int):
    msg = await ctx.channel.fetch_message(msgID)
    await ctx.send(msg.reactions)



bot.run(os.environ['token'])
