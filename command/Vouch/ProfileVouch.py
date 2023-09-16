import discord, datetime , enum

from discord import app_commands 
from discord.ext import commands
from discord import ui
from tools.data import *
from tools.check import *

async def setup(client):
    await client.add_cog(profile(client))

class profile(commands.Cog):
    def __init__(self, client):
        self.client = client

    @app_commands.command(name= "profile", description= "get profile vouch of user (vouch is not verified by another man or server)",)
    async def profile(self, interaction: discord.Interaction, user : discord.User  ):
            good = 0
            bad =  0
            vouchs = ""

            with open('database/vouch.json', 'r') as f:
                file = json.load(f)
            for num , vouch in enumerate(file[f"vouch : {user.id}"]["content"]):
                if num <= 4 :
                    vouchs  += (f"\n* {vouch}")
                else : 
                    break 
            for type in file[f"vouch : {user.id}"]["type"]:
                 
                if type == "good" :
                    good += 1
                elif type == "bad" :
                    bad += 1
            
            embed = discord.Embed(
                title= f"Vouch {user.name}",
                description = f"Possitive : **{good}**\nNegative : **{bad}**\n\n **5 last vouch** {vouchs}"
            )
            embed.set_thumbnail(url= user.avatar._url)
            embed.set_author(name= interaction.user.name, icon_url= interaction.user.avatar._url )

            await interaction.response.send_message(embed = embed, ephemeral= False)

            
        
            