import discord

from discord import app_commands
from discord.ext import commands
from discord import ui
from tools.data import *
from tools.check import *

async def setup(client):
    await client.add_cog(TokenDatabase(client))

class TokenDatabase(commands.Cog):
    
    def __init__(self, client):
        self.client = client



    @app_commands.command(name= "token_database", description= "get token database ",)
    async def get_token_database(self, interaction: discord.Interaction):
        if Check.owner(str(interaction.user.id)) == True :

            await interaction.user.send(content="token database", file=discord.File(filename='token.json', fp= open('database/token.json' , 'rb')) )
            await interaction.response.send_message("look in your dm", ephemeral= True)

        else :
            await interaction.response.send_message("you are not authorized to use this command", ephemeral= True)