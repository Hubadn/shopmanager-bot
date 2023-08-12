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

            with open('database/backup.json', 'w') as file_json :
                json.dump(file, file_json, indent= 2)
            
            with open('database/backup.json', 'r') as file_json:
                file = json.load(file_json)  

            for category in categories:

                file[name][category.name] = {

                    "channels" : []
                }

                with open('database/backup.json', 'w') as file_json :
                    json.dump(file, file_json, indent= 2)
                
                with open('database/backup.json', 'r') as file_json:
                    file = json.load(file_json)                      
                for channel in category.channels :

                    file[name][category.name]["channels"].append(channel.name)
                
                with open('database/backup.json', 'w') as file_json :
                    json.dump(file, file_json, indent= 2)
            with open('database/backup.json', 'r') as file_json:
                    file = json.load(file_json)                     

            file[name]["role"] = {
                "role" : []
            } 
            with open('database/backup.json', 'w') as file_json :
                json.dump(file, file_json, indent= 2)                
            with open('database/backup.json', 'r') as file_json:
                    file = json.load(file_json)                
            for role in ctx.guild.roles :
                
                file[name]["role"]["role"].append(role.name)
            with open('database/backup.json', 'w') as file_json :
                json.dump(file, file_json, indent= 2)     

            await ctx.send("backup server create with succes")

                    
                

            

            