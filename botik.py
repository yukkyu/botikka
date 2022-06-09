import random
import discord

from cat_images import url, emoji_list, url_list
from config import token
from discord.ext import commands
from utils import printt

botinok = commands.Bot(
    command_prefix=";"
)


@botinok.event
async def on_ready():
    printt("Hello World!")


@botinok.command(
    pass_context=True
)
async def botika(ctx):
    await ctx.send("botik!")


@botinok.command()
async def cat(ctx):
    embed = discord.Embed(
        title="I found cat for you! " + random.choice(emoji_list),
        color=discord.Color.red()
    )
    embed.url = "https://github.com/mjaucher/botik"
    embed.set_image(url=url())
    await ctx.reply(embed=embed)


@botinok.command()
async def dev_urlen(ctx):
    await ctx.send(str(len(url_list)) + " cats!")


botinok.run(token)
