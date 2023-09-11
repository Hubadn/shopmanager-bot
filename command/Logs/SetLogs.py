import discord, enum

from discord import app_commands
from discord.ext import commands
from discord import ui
from tools.data import *
from tools.check import *

class Type(enum.Enum):

    Roles = "roles"
    Mods = "mods"
    Messages= "message"


async def setup(client):
    await client.add_cog(setlogs(client))


class setlogs(commands.Cog):
    def __init__(self, client):
        self.client = client

    @app_commands.command(name="setlogs", description="setlogs command")
    async def setlogs(self,interaction: discord.Interaction, type: Type , channel: discord.TextChannel):

        if Check.owner(str(interaction.user.id)) == True :

                with open('database/logs.json', 'r') as f:
                    file = json.load(f)

                file[type.value] = channel.id   

                with open('database/logs.json', 'w') as f:
                    json.dump(file, f, indent=2)
                
                await channel.send("logs successfully setup in this server")
                await interaction.response.send_message(f"logs {type.value} is successfully setup", ephemeral= True)
        
        else :
            await interaction.response.send_message("you are not authorized to use this command", ephemeral= True)
