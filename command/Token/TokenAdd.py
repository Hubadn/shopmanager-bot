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
    await client.add_cog(addtoken(client))

class addtoken(commands.Cog):
    
    def __init__(self, client):
        self.client = client



    @app_commands.command(name= "addtoken", description= "add token to your db",)
    async def addtoken(self, interaction: discord.Interaction, type : Type, file : discord.Attachment):

        if Check.owner(str(interaction.user.id)) == True :

            if type.value == "token":
                tokens = await file.read()
                tokens = tokens.splitlines()
                with open('database/token.json', 'r') as f:
                    file = json.load(f)
                
                for token in tokens :
                    file["token"][type.value].append(str(token.decode('utf-8')))
                
                with open('database/token.json', 'w') as f:
                    json.dump(file, f, indent=2)
                
                await interaction.response.send_message(f"all tokens as been added in your database", ephemeral= True)
        
        else :
            await interaction.response.send_message("you are not authorized to use this command", ephemeral= True)            