import discord, enum

from discord import app_commands
from discord.ext import commands
from discord import ui
from tools.data import *
from tools.check import *

channels = ["mods", "message", "roles"]
async def setup(client):
    await client.add_cog(autologs(client))


class autologs(commands.Cog):
    def __init__(self, client):
        self.client = client

    @app_commands.command(name="autologs", description="autologs command")
    async def autologs(self,interaction: discord.Interaction):

        if Check.owner(str(interaction.user.id)) == True :
            
            overwrite = discord.PermissionOverwrite()
            overwrite.view_channel = False

            category = await interaction.guild.create_category(name="logs")

            await category.set_permissions(interaction.guild.default_role ,overwrite= overwrite)

            for channel in channels:
                channel_dis = await interaction.guild.create_text_channel(name= channel, category = category)
                
                with open('database/logs.json', 'r') as f :
                    file = json.load(f)

                file[channel] = channel_dis.id

                with open('database/logs.json', 'w') as f:
                    json.dump(file, f , indent=2)

                await channel_dis.send(f"{channel}logs is setup in this channel")

            await interaction.response.send_message("autologs successfully setup", ephemeral= True)



        else :
            await interaction.response.send_message("you are not authorized to use this command", ephemeral= True)