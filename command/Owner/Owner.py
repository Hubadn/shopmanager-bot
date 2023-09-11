import discord, enum

from discord import app_commands
from discord.ext import commands
from discord import ui
from tools.data import *
from tools.check import *

class Fonction(enum.Enum):
     
    add = "add"
    remove = "remove"
    clear =  "clear"
    list = "list"
    


async def setup(client):
    await client.add_cog(owner(client))

class owner(commands.Cog):
    def __init__(self,client):
        self.client = client 

    @app_commands.command(name= "owner",  description= "gestion of owner bot",)
    async def owner(self,interaction: discord.Interaction, fonction : Fonction, user: discord.Member = None):
        if Check.superowner(str(interaction.user.id)) == True:
            if fonction.value == "add" and user != None:
                alreadyin = False
                
                with open('database/buyer-owner.json', 'r') as f :
                        file = json.load(f)

                for owner in file['owner']["list"]:
                    if owner == str(user.id):
                          alreadyin = True

                if file["owner"]["superowner"] == str(user.id) :
                    alreadyin = True

                if alreadyin == False :
                    file["owner"]["list"].append(str(user.id))

                    with open('database/buyer-owner.json', 'w') as f :
                        json.dump(file, f, indent= 2)

                    await interaction.response.send_message(f"{user.name} be added to owner list")
                
                else :
                    await interaction.response.send_message("this is already an owner or this the superowner")
            elif fonction.value == "list" :
                ownerlist = ""
                
                with open('database/buyer-owner.json', 'r') as f:
                     file = json.load(f)
                
                superowner = file["owner"]["superowner"]

                for owner in file["owner"]["list"]:
                     
                    ownerlist += f"\n <@{owner}>"
                
                ownerlist += f"\n <@{superowner}>"

                embed = discord.Embed(
                    title= "Owner list",
                    description= ownerlist,

                )

                await interaction.response.send_message(embed = embed)

            elif fonction.value == "remove"  and user != None:
                with open('database/buyer-owner.json', 'r') as f :
                        file = json.load(f)

                file["owner"]["list"].remove(str(user.id)) 

                with open('database/buyer-owner.json', 'w') as f :
                    json.dump(file, f, indent= 2)
                
                await interaction.response.send_message(f"{user.name} be remove form owner list")

            elif fonction.value == "clear" :

                with open('database/buyer-owner.json', 'r') as f:
                    file = json.load(f)    

                for owner in file["owner"]["list"]:
                    file["owner"]["list"].remove(owner)

                with open('database/buyer-owner.json', 'w') as f :
                    json.dump(file, f, indent= 2)   
       
                await interaction.response.send_message("owner list cleared")

            else :

                embed = discord.Embed(
                title = "Argument invalide",
                description = "Synthax: **``/owner <add/remove/clear/list> <@user>``**",
                color = 0xFF0000
                )

                await interaction.response.send_message(embed= embed, ephemeral= True)

                return
        else : 
            await interaction.response.send_message("you are not authorized to use this command", ephemeral= True)