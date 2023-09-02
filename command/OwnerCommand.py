import discord, json
from discord.ext import commands
from  tools.check import *

async def setup(client):
    await client.add_cog(owner(client))

class owner(commands.Cog):
    def __init__(self,client):
        self.client = client 

    @commands.command()
    async def owner(self,ctx, fonction= None, user: discord.Member = None):
        await ctx.message.delete()
        if Check.owner(str(ctx.message.author.id)) == True:
            if fonction == "add":
                
                with open('database/buyer-owner.json', 'r') as f :
                        file = json.load(f)

                file["owner"]["list"].append(str(ctx.message.author.id)) 

                with open('database/buyer-owner.json', 'w') as f :
                    json.dump(file, f, indent= 2)

                await ctx.send(f"{user.name} be added to owner list")
            elif fonction == "list" :
                ownerlist = ""
                
                with open('database/buyer-owner.json', 'r') as f:
                     file = json.load(f)
                
                superowner = file["owner"]["superowner"]
                for owner in file["owner"]["list"]:
                     
                     ownerlist += f"\n <@{owner}>"
                
                ownerlist += f"\n <@{owner}>"
                embed = discord.Embed(
                    title= "Owner list",

                    description= ownerlist,

                )

                await ctx.send(embed = embed)
            elif fonction == "remove":
                with open('database/buyer-owner.json', 'r') as f :
                        file = json.load(f)

                file["owner"]["list"].remove(str(user.id)) 

                with open('database/buyer-owner.json', 'w') as f :
                    json.dump(file, f, indent= 2)
                
                await ctx.send(f"{user.name} be remove form owner list")
                
            else :

                embed = discord.Embed(
                title = "Argument invalide",
                description = "Synthax: **``owner <add/remove/list> <@user>``**",
                color = 0xFF0000
                )
                await ctx.send(embed= embed)
                return
        elif not Check.owner(str(ctx.message.author.id)) == True:
            await ctx.send("you are not authorized to use this command")