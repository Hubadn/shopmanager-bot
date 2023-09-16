import discord

from discord import app_commands
from discord.ext import commands
from discord import ui
from tools.data import *
from tools.check import *

async def setup(client):
    await client.add_cog(vouchprofilesetup(client))

class vouchprofilesetup(commands.Cog):
    
    def __init__(self, client):
        self.client = client



    @app_commands.command(name= "setup_vouch_profile", description= "create your profile vouch in database",)
    async def vouchprofilesetup(self, interaction: discord.Interaction):
        if Check.owner(str(interaction.user.id)) == True :
            with open('database/vouch.json', 'r') as f:
                file = json.load(f)
            
            file[f"vouch : {interaction.user.id}"] = {
                "content": [],
                "type" : []
            }

            with open('database/vouch.json', 'w') as f:
                json.dump(file, f, indent=2)
                
            await interaction.response.send_message("your profile is successfully created ;)")
        else :
            await interaction.response.send_message("you are not authorized to use this command", ephemeral= True)