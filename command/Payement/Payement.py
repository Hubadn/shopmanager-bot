import discord , enum

from discord import app_commands
from discord.ext import commands
from discord import ui
from tools.data import *
from tools.check import *

class Select(enum.Enum):

    paypal = "paypal"
    litecoin = "ltc"
    bitecoin = "btc"
    etherum = "eth"

def get_payement(type : str , value : str):
    
    with open('database/payement.json', 'r') as f:
        file = json.load(f)
    
    return file[type][value]

async def setup(client):
    await client.add_cog(payement(client))


class payement(commands.Cog):
    def __init__(self, client):
        self.client = client

    @app_commands.command(name= "payement" , description="select your payement method",)
    async def payement(self, interaction: discord.Interaction, select : Select):
        def check(id, message):
            if id == message:
                 return True
            else :
                 return False
        if select.value == "paypal":
            embed = discord.Embed(

                title =f"Payement method by : {select}",

                description = f"> paypal link : {get_payement(type= 'paypal', value= 'link' )}\n> paypal email: {get_payement(type= 'paypal', value= 'email' )} ",
                color = 0x0000FF
                )
            embed.set_thumbnail(url="https://media.discordapp.net/attachments/1135971296774193223/1135972383950381137/paypal-logo.gif")
            embed.set_footer(text="for copy put reaction : 📱")

            message_ppl = await interaction.response.send_message(embed=embed)
            # await message_ppl.add_reaction("📱")
            # while True: 
            #             try:
            #                 reaction, user = await self.client.wait_for("reaction_add")
            #                 if str(reaction.emoji) == "📱":
            #                     if check(id = reaction.message.id, message =  message_ppl.id) is True :
            #                         await user.send(f"{importdata.tableau(chemin='database', filename='payement', name_list='paypal', name='link' )}")
            #                         await user.send(f"{importdata.tableau(chemin='database', filename='payement', name_list='paypal', name='email' )}")
            #                     else : 
            #                          pass
                                 
            #             except :
            #                 break                    
            # return
        elif select.value == "ltc":
            embed = discord.Embed(

                title =f"Payement method by : {select}",

                description = f"> ltc adresse : {get_payement(type= 'crypto', value= 'ltc')}",

                color = 0x808080

                )
            
            
            
            embed.set_thumbnail(url ="https://media.discordapp.net/attachments/1135971296774193223/1135972383140872242/ltc-logo.gif")
            embed.set_footer(text="for copy put reaction : 📱")

            message_ltc = await interaction.response.send_message(embed=embed)
            await message_ltc.add_reaction("📱")
            # while True:
            #             try:
            #                 reaction, user = await self.client.wait_for("reaction_add")
            #                 if str(reaction.emoji) == "📱":
            #                     if  check(id = reaction.message.id, message =  message_ltc.id) is True :
            #                         await user.send(f"{importdata.tableau(chemin='database', filename='payement', name_list='crypto', name='ltc' )}")
            #                     else : 
            #                          pass
                                 
            #             except :
            #                 break                    

            # return

        elif select.value == "btc":
            embed = discord.Embed(

                title =f"Payement method by : {select}",

                description = f"> btc adresse : {get_payement(type= 'crypto', value= 'btc')}",

                color = 0xFFFF00
                )
            
            embed.set_thumbnail(url = "https://media.discordapp.net/attachments/1135971296774193223/1135972383522566255/btc-logo.gif")
            
            message_btc = await interaction.response.send_message(embed=embed)
            await message_btc.add_reaction("📱")
            
            # while True:
            #             try:
            #                 reaction, user = await self.client.wait_for("reaction_add")
            #                 if str(reaction.emoji) == "📱":
            #                     if  check(id = reaction.message.id, message =  message_btc.id) is True :
            #                         await user.send(f"{importdata.tableau(chemin='database', filename='payement', name_list='crypto', name='btc' )}")
            #                     else : 
            #                          pass
                                 
            #             except :
            #                 break                    

            # return

        elif select.value == "eth":
            embed = discord.Embed(

                title =f"Payement method by : {select}",

                description = f"> eth adresse : {get_payement(type= 'crypto', value= 'eth')}",

                color = 0x000000

                )
            embed.set_thumbnail(url = "https://media.discordapp.net/attachments/1135971296774193223/1135972755385364481/eth-logo.gif")
        
            message_eth= await interaction.response.send_message(embed=embed)
            await message_eth.add_reaction("📱")

#            while True:
#                        try:
#                            reaction, user = await self.client.wait_for("reaction_add")
#                            if str(reaction.emoji) == "📱":
#                                if  check(id = reaction.message.id, message =  message_eth.id) is True :
#                                    await user.send(f"{importdata.tableau(chemin='database', filename='payement', name_list='crypto', name='eth' )}")
#                                else : 
#                                     pass
#                                
#                        except :
#                            break                    
#
#            return