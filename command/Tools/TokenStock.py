import discord

from discord import app_commands
from discord.ext import commands
from discord import ui
from tools.data import *
from tools.check import *

def get_number_of_token():
    token_nb : int = 0
    
    with open('database/token.json') as f:
        file = json.load(f)
    
    for token in file["token"]:

        token_nb += 1

    return token_nb

def get_number_of_token_boost():
    token_1  : int = 0
    token_3 : int = 0
    with open('database/token.json') as f:
        file = json.load(f)
    
    for token in file["tokenboost"]["1"]:
        token_1 +=1
    
    for token in file["tokenboost"]["3"]:
        token_3 +=1

    return token_1, token_3
async def setup(client):
    await client.add_cog(tokenjoineur(client))

class tokenjoineur(commands.Cog):
    def __init__(self, client):
        self.client = client



    @app_commands.command(name= "tokenstock", description= "get stock of your tokenstock",)
    async def tokenstock(self, interaction: discord.Interaction):
        token = get_number_of_token()
        token_boost_1, token_boost_3 = get_number_of_token_boost()

        if Check.owner(str(interaction.user.id)) == True:
            embed = discord.Embed(
                title="Token Stock",

                description=f"> **Token** : {token}\n> **token boost 1 month** : {token_boost_1}\n > **token boost 3 month** : {token_boost_3}"
            )
            await interaction.response.send_message(embed= embed)
        else : 
            await interaction.response.send("you are not authorized to use this command", ephemeral= True)