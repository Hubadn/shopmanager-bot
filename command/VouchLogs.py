import discord, datetime

from discord import app_commands
from discord.ext import commands
from discord import ui
from tools.data import *
from tools.check import *

async def setup(client):
    await client.add_cog(setvouchlogs(client))

class setvouchlogs(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def setvouchlog(self, ctx, channel : discord.TextChannel):
        if Check.owner(str(ctx.message.author.id)) == True :
            
            with open('database/logs.json', 'r') as f :
                file = json.load(f)
            
            file["vouch"] = channel.id

            with open('database/logs.json', 'w') as f:
                json.dump(file, f, indent=2)
            
            await ctx.send(f"logs succesfuly setup in <#{channel.id}>")
            await channel.send("Vouch Setup in this **channel**")

        else :
            await ctx.send("you are not authorized to use this command")
    
    @app_commands.command(name = "setvouchlog", description="setup vouch log channel")
    async def setvouchlog(self, interaction: discord.Interaction, channel: discord.TextChannel):
        if Check.owner(str(interaction.user.id)) == True :
            with open('database/logs.json', 'r') as f :
                file = json.load(f)
            
            file["vouch"] = channel.id

            with open('database/logs.json', 'w') as f:
                json.dump(file, f, indent=2)
            
            await interaction.response.send_message(f"logs succesfuly setup in <#{channel.id}>", ephemeral= True)
            await channel.send("Vouch Setup in this **channel**")

        else :
            await interaction.response.send_message("you are not authorized to use this command", ephemeral= True)        
    