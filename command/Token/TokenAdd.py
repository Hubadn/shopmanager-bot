import discord, enum

from discord import app_commands
from discord.ext import commands
from discord import ui
from tools.data import *
from tools.check import *

class Type(enum.Enum):
    
    Token = "token"
    TokenBoost1Month = "tokenboost1"
    TokenBoost3Month = "tokenboost3"   

async def setup(client):
    await client.add_cog(VouchCommandPhone(client))

class VouchCommandPhone(commands.Cog):
    
    def __init__(self, client):
        self.client = client



    @app_commands.command(name= "addtoken", description= "add token to your db",)
    async def addtoken(self, interaction: discord.Interaction, type : Type, file : discord.Attachment):

        if Check.owner(str(interaction.user.id)) == True :