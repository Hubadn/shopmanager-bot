import discord, tools.data 
from discord.ext import commands
from tools.data import *
def setup(client):
    client.add_cog(backup(client))



class backup(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def backup(self,ctx, type : str = None , action: str = None  , name: str = None ):
        if type == "server" and action == "create" :
            channels = ctx.guild.channels
            categories = ctx.guild.categories

            with open('database/backup.json', 'r') as file_json:
                file = json.load(file_json)
            
            file[name] = {}
            file[name]["channel_without_category_texte"] = []
            file[name]["channel_without_category_voc"] = []
            file[name]["role"] = {
                "role" : []
            } 

            with open('database/backup.json', 'w') as file_json :
                json.dump(file, file_json, indent= 2)


            with open('database/backup.json', 'r') as file_json:
                file = json.load(file_json)

            for category in categories :

                file[name][category.name] = {

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
                    file[name][category_name][f"{channel.type}"].append(channel.name)


                except :
                    if f"{channel.type}" == "category" :
                        
                        pass
                    
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
        if type == "server" and action == "list" :

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



                    
                

            

            