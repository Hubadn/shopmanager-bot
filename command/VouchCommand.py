import discord, datetime

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
    id_vouch = discord.ui.TextInput(
        style= discord.TextStyle.short,
        label= "seller id",
        required= True,
        placeholder= "seller id of discord account"
    ) 
    message_vouch = discord.ui.TextInput(
        style=discord.TextStyle.long,
        label="vouch content",
        required=True,
        max_length=100,
        placeholder="format : <product> <quantity> <price>"
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

        with open('database/vouch.json','r') as f:
            file = json.load(f)
        
        file[f"vouch : {datetime.datetime.utcnow()}"] = {
            "VouchIdUser" : self.id_vouch.value,
            "VouchType" : self.type_vouch.value,
            "VouchUser" : self.user_vouch.value,
            "VouchValue" : self.message_vouch.value
        }

        with open('database/vouch.json','w') as f:
            json.dump(file, f , indent = 2)

    async def on_error(self, interaction: discord.Interaction, error : Exception) :
        await interaction.response.send_message(f"vouch invalide or latence error", ephemeral=True)
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