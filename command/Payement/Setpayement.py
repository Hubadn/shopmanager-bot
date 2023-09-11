import discord, enum

from discord import app_commands
from discord.ext import commands
from discord import ui
from tools.data import *
from tools.check import *


async def setup(client):
    await client.add_cog(setpayement(client))

class Select(enum.Enum):

    paypal = "paypal"
    crypto = "crypto"

            

class setpayement(commands.Cog):
    def __init__(self, client):
        self.client = client

    @app_commands.command(name= "setpayement", description ="set your payement methode")
    async def setpayement(self,interaction: discord.Interaction, select :  Select, value : str, paypal_link :str  = None):
        if Check.owner(str(interaction.user.id)) == True :
            if select.value == "paypal":
                postdata.tableau(chemin= 'database/', filename= 'payement', name_list= 'paypal', name= 'link', value= value)
                postdata.tableau(chemin= 'database/', filename= 'payement', name_list= 'paypal', name= 'email', value= paypal_link)
                
                embed = discord.Embed(
                    
                    title = f"Payement setup : {select.value}",
                    
                    description = f"> Payement link : {value}\n> Payement email : {paypal_link}",

                    color = discord.Color.blue()
                )
                embed.set_footer(text= CREDIT)
                embed.set_thumbnail(url="https://media.discordapp.net/attachments/1135971296774193223/1135972383950381137/paypal-logo.gif")
                
                await interaction.response.send_message(embed=embed, ephemeral=True)

            elif select.value == "eth" or "btc" or "ltc"  :
                postdata.tableau(chemin= 'database/', filename= 'payement',name_list='crypto', name= select.value, value= value)

                embed = discord.Embed(
                    title = f"Payement setup : {select}",
                                
                    description = f"> {select.value} addy  : {value}",    

                )
                if select.value == "eth" :
                    embed.color = 0x000000
                    embed.set_thumbnail(url = "https://media.discordapp.net/attachments/1135971296774193223/1135972755385364481/eth-logo.gif")

                elif select.value == "btc" :
                    embed.color = 0xFFFF00
                    embed.set_thumbnail(url = "https://media.discordapp.net/attachments/1135971296774193223/1135972383522566255/btc-logo.gif")

                elif select.value == "ltc" :
                    embed.color = discord.Color.blue()
                    embed.set_thumbnail(url ="https://media.discordapp.net/attachments/1135971296774193223/1135972383140872242/ltc-logo.gif")
                
                embed.set_footer(text= CREDIT)

                await interaction.response.send_message(embed=embed, ephemeral=True)
        else : 
            await interaction.response.send_message("you are not authorized to use this command", ephemeral= True)


