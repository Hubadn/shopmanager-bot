import discord

from discord import app_commands
from discord.ext import commands
from discord import ui
from tools.data import *
from tools.check import *

async def setup(client):
    await client.add_cog(VouchCommand(client))
class FeedbackModal(discord.ui.Modal, title="Send Vouch"):
    type_vouch = discord.ui.TextInput(
        style=discord.TextStyle.short,
        label="type vouch",
        required=True,
        placeholder="good or bad"
    )
    user_vouch = discord.ui.TextInput(
        style= discord.TextStyle.short,
        label= "seller name",
        required= True,
        placeholder= "exemple : legenduser"

    ) 
    message_vouch = discord.ui.TextInput(
        style=discord.TextStyle.long,
        label="vouch content",
        required=True,
        max_length=500,
        placeholder="format : <product> <price> <quantity>"
    )

    async def on_submit(self, interaction: discord.Interaction):
        """This is my summary

        Args:
            interaction (discord.Interaction): Default discordpy Interaction
        """
        with open('database/logs.json', 'r') as f:
            file = json.load(f)

        channel = interaction.guild.get_channel(int(file["vouch"])) 
        
        
        embed = discord.Embed(title=f"Vouch for {self.user_vouch.value}",
                              description=f"\n> type : **{self.type_vouch.value}**"+ "\n> vouch  : " +self.message_vouch.value)
        
        if self.type_vouch.value == "good" :
            embed.color = discord.Color.green()
        if self.type_vouch.value == "bad" :
            embed.color = discord.Color.red()
        
        embed.set_author(name=self.user.name, url= f"https://discord.com/users/{self.user.id}")

        await channel.send(embed = embed)

        await interaction.response.send_message(f"Thank you, {self.user.name}", ephemeral=True)

    async def on_error(self, interaction: discord.Interaction, error : Exception):
        
        print("error")
class VouchCommand(commands.Cog):
    
    def __init__(self, client):
        self.client = client
    @commands.command()
    async def sync(self, ctx) -> None:
        await ctx.client.tree.sync(guild=ctx.guild)


    @app_commands.command(name= "vouch", description= "vouch command",)
    async def vouch(self, interaction: discord.Interaction ):
        feedback_modal = FeedbackModal()
        feedback_modal.user = interaction.user
        await interaction.response.send_modal(feedback_modal)