import discord, datetime

from discord import app_commands
from discord.ext import commands
from discord import ui
from tools.data import *
from tools.check import *

async def setup(client):
    await client.add_cog(teste(client))
class SimpleView(discord.ui.View):
    
    foo : bool = None
    
    async def disable_all_items(self):
        for item in self.children:
            item.disabled = True
        await self.message.edit(view=self)
    
    
    @discord.ui.button(label="Hello", 
                       style=discord.ButtonStyle.success)
    async def hello(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("World")
        self.foo = True
        self.stop()
        
    @discord.ui.button(label="Cancel", 
                       style=discord.ButtonStyle.red)
    async def cancel(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("Cancelling")
        self.foo = False
        self.stop()

class teste(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def teste(self, ctx):
        view = SimpleView(timeout=50)
        # button = discord.ui.Button(label="Click me")
        # view.add_item(button)
        
        message = await ctx.send(view=view)
        view.message = message
        
        await view.wait()
        await view.disable_all_items()
    