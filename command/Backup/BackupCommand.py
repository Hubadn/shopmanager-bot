import discord, enum

from discord import app_commands
from discord.ext import commands
from discord import ui
from tools.data import *
from tools.check import *

class Type(enum.Enum):

    server = "server"
    emoji = "emoji"

class Action(enum.Enum):

    create = "create"
    delete = "delete"
    load = "load"
    list = "list"

async def setup(client):
    await client.add_cog(backup(client))


class backup(commands.Cog):
    def __init__(self, client):
        self.client = client

    @app_commands.command(name="backup", description="backup command")
    async def backup(self,interaction: discord.Interaction, type : Type , action: Action  , name: str = None ):
        if Check.owner(str(interaction.user.id)) == True  :
            if type.value == "server" and action.value == "create" :
                channels = interaction.guild.channels
                categories = interaction.guild.categories

                with open('database/backup.json', 'r') as file_json:
                    file = json.load(file_json)
                
                file[name] = {}
                file[name]["Server-Name"] = interaction.guild.name
                file[name]["channel_without_category_texte"] = []
                file[name]["channel_without_category_voc"] = []
                file[name]["categories"] = {}
                file[name]["role"] = {
                    "role" : []
                } 

                with open('database/backup.json', 'w') as file_json :
                    json.dump(file, file_json, indent= 2)


                with open('database/backup.json', 'r') as file_json:
                    file = json.load(file_json)

                for category in categories :

                    file[name]["categories"][category.name] = {

                        "voice" : [],
                        "text" : [] 
                    }
                
                with open('database/backup.json', 'w') as file_json :
                    json.dump(file, file_json, indent= 2)

                with open('database/backup.json', 'r') as file_json:
                    file = json.load(file_json)

                for channel in channels :
                    with open('database/backup.json', 'r') as file_json:
                        file = json.load(file_json)
                    try :
                        
                        category_name = channel.category.name
                        file[name]["categories"][category_name][f"{channel.type}"].append(channel.name)


                    except :
                        if f"{channel.type}" == "category" :    
                            break
                        
                        elif f"{channel.type}" == "text":
                            
                            file[name]["channel_without_category_texte"].append(channel.name)

                        elif f"{channel.type}"== "voice" :

                            file[name]["channel_without_category_voc"].append(channel.name)

                    with open('database/backup.json', 'w') as file_json :
                            json.dump(file, file_json, indent= 2)       
        

                with open('database/backup.json', 'r') as file_json:
                    file = json.load(file_json)

                    for role in interaction.guild.roles :
                    
                        file[name]["role"]["role"].append(role.name)

                with open('database/backup.json', 'w') as file_json :
                    json.dump(file, file_json, indent= 2)       


                await interaction.response.send_message("backup server create with succes")
            elif type.value == "server" and action.value == "load": 
                    with open('database/backup.json', 'r') as file_json:
                        file = json.load(file_json)

                    try : 
                        file[name]
                        nofound = False
                    except : 
                        await interaction.response.send_message("backup no found")
                        nofound =  True
                    
                    channels = interaction.guild.channels
                    roles = interaction.guild.roles

                    if nofound is True :
                        return
                    elif nofound is False :
                        for channel in channels :
                            try :
                                await channel.delete()
                            except :
                                pass
                        for role in roles :
                            try :
                                await role.delete()
                            except :
                                pass  
                        for channel_text in file[name]["channel_without_category_texte"] : 

                            await interaction.guild.create_text_channel(channel_text)

                        for channel_voice in file[name]["channel_without_category_voc"]:

                            await interaction.guild.create_voice_channel(channel_voice)

                        for category_name in file[name]["categories"] :

                            category_id = await interaction.guild.create_category(category_name)

                            for channel_category in file[name]["categories"][category_name]["text"] :
                                
                                await interaction.guild.create_text_channel(channel_category, category=category_id)

                            for channel_category in file[name]["categories"][category_name]["voice"] :
                                
                                    await interaction.guild.create_voice_channel(channel_category, category=category_id)        
                        for role in file[name]["role"]["role"] :

                                    await interaction.guild.create_role(name= role)
                        
                        await interaction.user.send("backup load with success !")

            elif type.value == "server" and action.value == "list" :

                server_list = ""

                with open('database/backup.json', 'r') as file_json :
                    file = json.load(file_json)
                    
                for object in file :
                    print(object)
                    server_list = server_list + f"\n{object}"
                    
                embed = discord.Embed(

                        title = "list of backup",

                        description ="```" + server_list + "```"

                    )
                await interaction.response.send_message(embed = embed)
            
            elif type.value == "server" and action.value == "delete" :
                with open('database/backup.json', 'r') as file_json :
                    file = json.load(file_json)
                try :    
                    del file[name]

                    with open('database/backup.json','w') as fichier:
                        json.dump(file, fichier, indent=2)
                    
                    await interaction.response.send_message(f"backup successfuly deleted {name}", ephemeral= True)
                except :
                    await interaction.response.send_message(f"backup : {name} is not found", ephemeral= True)
                    
        else :
            await interaction.response.send_message("you are not authorized to use this command", ephemeral= True)