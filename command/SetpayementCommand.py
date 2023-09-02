import discord
from discord.ext import commands
import tools.data
from tools.data import *

async def setup(client):
    await client.add_cog(setpayement(client))



class setpayement(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def setpayement(self,ctx, select : str, value : str, value_op :str  = None):
        if select == "paypal":
            postdata.tableau(chemin= 'database/', filename= 'payement', name_list= 'paypal', name= 'link', value= value)
            postdata.tableau(chemin= 'database/', filename= 'payement', name_list= 'paypal', name= 'email', value= value_op)
            
            embed = discord.Embed(
                
                title = f"Payement setup : {select}",
                
                description = f"> Payement link : {value}\n> Payement email : {value_op}",

                color = discord.Color.blue()
            )
            embed.set_footer(text= CREDIT)
            embed.set_thumbnail(url="https://media.discordapp.net/attachments/1135971296774193223/1135972383950381137/paypal-logo.gif")
            
            await ctx.send(embed=embed)

        elif select == "eth" or "btc" or "ltc"  :
            postdata.tableau(chemin= 'database/', filename= 'payement',name_list='crypto', name= select, value= value)

            embed = discord.Embed(
                title = f"Payement setup : {select}",
                            
                description = f"> {select} addy  : {value}",    

            )
            if select == "eth" :
                embed.color = 0x000000
                embed.set_thumbnail(url = "https://media.discordapp.net/attachments/1135971296774193223/1135972755385364481/eth-logo.gif")
            elif select == "btc" :
                embed.color = 0xFFFF00
                embed.set_thumbnail(url = "https://media.discordapp.net/attachments/1135971296774193223/1135972383522566255/btc-logo.gif")
            elif select == "ltc" :
                embed.color = discord.Color.blue()
                embed.set_thumbnail(url ="https://media.discordapp.net/attachments/1135971296774193223/1135972383140872242/ltc-logo.gif")
            
            embed.set_footer(text= CREDIT)

            await ctx.send(embed=embed)


