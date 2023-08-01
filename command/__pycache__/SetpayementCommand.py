import discord
from discord.ext import commands
import tools.data
from tools.data import *
def setup(client):
    client.add_cog(setpayement(client))



class setpayement(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def setpayement(self,ctx, select : str, value : str, value_op :str  = None):
