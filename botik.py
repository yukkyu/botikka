import random
import discord

from cat_images import emoji_list, id_list, better_random_list
from config import token
from discord.ext import commands
from utils import printt, list_element_exists

botinok = commands.Bot(command_prefix=";")


@botinok.event
async def on_ready(): printt("Hello World!")


@botinok.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, *, number=711): await ctx.channel.purge(limit=number + 1)


@botinok.command()
async def cat(ctx):
    embed = discord.Embed(color=discord.Color.red())

    for identifier in id_list:
        random_id = random.choice(id_list)
        if not list_element_exists(better_random_list, random_id):
            embed.set_image(url="https://cdn.discordapp.com/attachments/984213928689172541/" + random_id + ".jpg")
            better_random_list.append(random_id)
            embed.title = "I found cat for you! " + random.choice(emoji_list)
            embed.url = "https://github.com/yukkyu/botikka"
            await ctx.reply(embed=embed)
            break
        elif len(better_random_list) == len(id_list):
            better_random_list.clear()


@botinok.command()
async def dev_catlen(ctx): await ctx.send(str(len(id_list)) + " cats!")


botinok.run(token)
