import discord
from discord.ext import commands
from discord import activity
from discord import client
from discord.enums import Status
from discord.ext.commands.core import after_invoke, dm_only
from discord.player import AudioSource

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print('bot is ready.')

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong!!! {round(client.latency * 1000)}ms')


@client.command()
async def chlaja(ctx):
    await ctx.send('https://c.tenor.com/sWEY8anP4dwAAAAM/chala-ja-chala-ja-b-sd-k.gif')

@client.command()
async def abesale(ctx):
    await ctx.send('https://i.pinimg.com/474x/8b/60/be/8b60bec74f330a7e41a9a2f78e850b6c.jpg')

@client.command()
async def saale(ctx):
    await ctx.send('https://akm-img-a-in.tosshub.com/indiatoday/images/story/202106/cover4_new_1200x768.jpeg?1ddh2wMj.1sWvDuJNNtgqjyvpihWf3BZ&size=1200:675')

@client.command()
async def candoit(ctx):
    await ctx.send('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ-ducQqCWuIF5IrTgh9PWyGVjuKUVla7dV8w&usqp=CAU')

@client.command()
async def heyboy(ctx):
    await ctx.send('https://c.tenor.com/n8DB4bmpduIAAAAM/yeah-bwoi-grin.gif')

@client.command()
async def wow(ctx):
    await ctx.send('https://c.tenor.com/KsiylS6mJtQAAAAM/wow-cat.gif')
    
@client.command()
async def claping(ctx):
    await ctx.send('https://c.tenor.com/ThUxAJl3zHQAAAAM/dragon-ball-z-goku.gif')

@client.command()
async def heythere(ctx):
    await ctx.send('https://c.tenor.com/ysLag0us3mQAAAAM/oh-hey-oh-hey-there.gif')



#test


client.run('ODg4NDU5OTI4MjkxOTA1NTc2.YUTAyQ.sCJ6d18ulD4bn_9n0Byg5m4cUFE')
