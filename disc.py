import discord
from discord.ext import commands

bot = discord.Client()

@bot.event
async def on_ready():
    print('você está logado como {0.user}'.format(bot))

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

# @bot.command( name = "oi")
# async def send_hello(ctx):
#     name = ctx.author.name

#     response = "oi, " + name

#     await ctx.send (response)


bot.run('')
