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
            good_text : str = ""
            bad_text : str = ""

            with open('database/vouch.json', 'r') as f:
                file = json.load(f)
            for vouch in file :
                if  file[vouch]["VouchType"]  == "good" and file[vouch]["VouchIdUser"] == user.id :
                    good += 1
                    good_text += f"{file[vouch]['VouchValue']},"
                elif file[vouch]["VouchType"] == "bad" and file[vouch]["VouchIdUser"] == user.id:
                    bad +=1
                    bad_text += f",{file[vouch]['VouchValue']}"
            
            if bad_text  == "" :
                bad_text = "No vouch"
            if good_text == "" :
                good_text = "No vouch"

            embed = discord.Embed(
                title= f"Vouch {user.name}",
                description = f"Possitive : **{good}**\n\n> {good_text}\n\nBad : **{bad}**\n\n> {bad_text}"
            )
            embed.set_thumbnail(url= user.avatar._url)
            embed.set_author(name= interaction.user.name, icon_url= interaction.user.avatar._url )

            await interaction.response.send_message(embed = embed, ephemeral= False)


            
        
            