import discord
from discord import app_commands
from discord.ext import commands
from tools.data import *
from tools.check import *



async def setup(client):
    await client.add_cog(backup(client))



class backup(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def backup(self,ctx, type : str = None , action: str = None  , name: str = None ):
        if Check.owner(str(ctx.message.author.id)) == True  :
            if type == "server" and action == "create" :
                channels = ctx.guild.channels
                categories = ctx.guild.categories

                with open('database/backup.json', 'r') as file_json:
                    file = json.load(file_json)
                
                file[name] = {}
                file[name]["Server-Name"] = ctx.guild.name
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

                    for role in ctx.guild.roles :
                    
                        file[name]["role"]["role"].append(role.name)

                with open('database/backup.json', 'w') as file_json :
                    json.dump(file, file_json, indent= 2)       


                await ctx.send("backup server create with succes")
            elif type == "server" and action == "load": 
                    with open('database/backup.json', 'r') as file_json:
                        file = json.load(file_json)

                    try : 
                        file[name]
                        nofound = False
                    except : 
                        await ctx.send("backup no found")
                        nofound =  True
                    
                    channels = ctx.guild.channels
                    roles = ctx.guild.roles

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

                            await ctx.guild.create_text_channel(channel_text)

                        for channel_voice in file[name]["channel_without_category_voc"]:

                            await ctx.guild.create_voice_channel(channel_voice)

                        for category_name in file[name]["categories"] :

                            category_id = await ctx.guild.create_category(category_name)

                            for channel_category in file[name]["categories"][category_name]["text"] :
                                
                                await ctx.guild.create_text_channel(channel_category, category=category_id)

                            for channel_category in file[name]["categories"][category_name]["voice"] :
                                
                                    await ctx.guild.create_voice_channel(channel_category, category=category_id)        
                        for role in file[name]["role"]["role"] :

                                    await ctx.guild.create_role(name= role)
                        
                        await ctx.author.send("backup load with success !")

            elif type == "server" and action == "list" :

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
                await ctx.send(embed = embed)
        else :
            await ctx.send("you are not authorized to use this command")