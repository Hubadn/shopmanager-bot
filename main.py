import discord 
from discord.ext import commands, tasks
import os, datetime, time , asyncio, json, colorama
from colorama import *
import tools.data
from tools.data import *


init()

intents = discord.Intents.all()
client = commands.Bot(command_prefix=";",help_command= None,intents=intents)

class load : 
    def command():
        for filename in os.listdir('./command'):
            if filename.endswith('.py'):
                client.load_extension(f'command.{filename[:-3]}')
                print("[" + Fore.GREEN +" + "+ Fore.WHITE + f"] : {filename[:-3]} loaded")
            else :
                print("[" + Fore.RED +" - "+ Fore.WHITE + f"] : {filename[:-3]} is not a .py file")
class unload :
    def command():
        commandnb = 0
        for filename in os.listdir('./command'):
            commandnb = commandnb+ 1
            if filename.endswith('.py'):
                client.unload_extension(f'command.{filename[:-3]}')
@client.command()
async def reload(ctx):
    await ctx.send("Les command on été reload")
    unload.command()
    load.command()


load.command()
client.run(importdata.simple("database", "config")["token"])
