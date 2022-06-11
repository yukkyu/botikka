import random
import discord

from cat_images import url, emoji_list, url_list
from config import token
from discord.ext import commands
from utils import printt

botinok = commands.Bot(command_prefix=";")


@botinok.event
async def on_ready(): printt("Hello World!")


@botinok.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, *, number=711): await ctx.channel.purge(limit=number + 1)


@botinok.command()
async def cat(ctx):
    embed = discord.Embed(color=discord.Color.red())
    embed.set_image(url=url())
    embed.title = "I found cat for you! " + random.choice(emoji_list)
    embed.url = "https://github.com/yukkyu/botikka"
    await ctx.reply(embed=embed)


@botinok.command()
async def dev_urlen(ctx): await ctx.send(str(len(url_list)) + " urls!")


botinok.run(token)
