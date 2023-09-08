import discord, datetime

from discord import app_commands
from discord.ext import commands
from discord import ui
from tools.data import *
from tools.check import *

async def setup(client):
    await client.add_cog(VouchCommandPhone(client))

class VouchCommandPhone(commands.Cog):
    
    def __init__(self, client):
        self.client = client



    @app_commands.command(name= "vouch", description= "vouch command",)
    async def vouch(self, interaction: discord.Interaction, user: discord.User, type : str  = None, product : str = None,  quantity : str = None , price : str = None):
            with open('database/vouch.json','r') as f:
                file = json.load(f)
            
            file[f"vouch : {datetime.datetime.utcnow()}"] = {
                "VouchIdUser" : user.id,
                "VouchType" : type,
                "VouchUser" : user.name,
                "VouchValue" : product + quantity + price
            }

            with open('database/vouch.json','w') as f:
                json.dump(file, f , indent = 2)
            
            with open('database/logs.json', 'r') as f:
                file = json.load(f)

            channel = interaction.guild.get_channel(int(file["vouch"]))
            embed = discord.Embed(title=f"Vouch for {user.name}",
                                description=f"\n> type : **{type}**"+ f"\n> vouch  : {product}   {quantity} + {price}")
            
            if type == "good" :
                embed.color = discord.Color.green()
            if type == "bad" :
                embed.color = discord.Color.red()
            
            embed.set_author(name=user.name, url= f"https://discord.com/users/{user.id}")
            await channel.send(embed = embed)
            await interaction.response.send_message(f"Thank you, {user.name}", ephemeral=True)          