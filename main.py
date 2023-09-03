import discord 
import asyncio
from discord.ext import commands, tasks
import os, datetime, time , asyncio, json, colorama
from colorama import *
import tools.data
from tools.data import *


init()

intents = discord.Intents.all()
intents.members = True
client = commands.Bot(command_prefix=";",help_command= None,intents=intents)

class load : 
    async def command():
        for filename in os.listdir('./command'):
            if filename.endswith('.py'):
                await client.load_extension(f'command.{filename[:-3]}')
                print("[" + Fore.GREEN +" + "+ Fore.WHITE + f"] : {filename[:-3]} loaded")
            else :
                print("[" + Fore.RED +" - "+ Fore.WHITE + f"] : {filename[:-3]} is not a .py file")
class unload :
    async def command():
        commandnb = 0
        for filename in os.listdir('./command'):
            commandnb = commandnb+ 1
            if filename.endswith('.py'):
               await  client.unload_extension(f'command.{filename[:-3]}')
@client.command()
async def reload(ctx):
    await ctx.send("Les command on été reload")
    await unload.command()
    await load.command()

@client.event
async def on_ready():
    await client.tree.sync()

    
async def main():
    await load.command()
    await client.start(importdata.simple("database", "config")["token"])


asyncio.run(main())