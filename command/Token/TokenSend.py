import discord, enum

from discord import app_commands
from discord.ext import commands
from discord import ui
from tools.data import *
from tools.check import *

class Type(enum.Enum):
    
    Token = "token"
    TokenBoost1Month = "tokenboost1"
    TokenBoost3Month = "tokenboost3"   
    
async def setup(client):
    await client.add_cog(tokensend(client))

class tokensend(commands.Cog):
    
    def __init__(self, client):
        self.client = client



    @app_commands.command(name= "tokensend", description= "send token to discord user",)
    async def tokensend(self, interaction: discord.Interaction, user : discord.User, type : Type, number : int):

        if Check.owner(str(interaction.user.id)) == True :
            value = ""
            if type.value == "token":

                with open('database/token.json', 'r') as f:
                    file = json.load(f)
                if number <= len(file["token"][type.value]) :
                    for number_enum, token in enumerate(file["token"][type.value]):

                        if number_enum <= number :

                            value += f"\n {token}"

                            with open('database/token.json', 'r') as f:
                                file = json.load(f)
                            
                            file["token"][type.value].remove(token)

                            with open('database/token.json', 'w') as f:
                                json.dump(file, f , indent= 2)
                        else :
                            return
                    await user.send(value)

                    await interaction.response.send_message(f"token succes sended at <@{user.id}>", ephemeral= True)

                else :
                    await interaction.response.send_message(f"no enough tokens ther is {len(file['token'][type.value])} tokens", ephemeral= True)

                
                
                    
        else :
            await interaction.response.send_message("you are not authorized to use this command", ephemeral= True)