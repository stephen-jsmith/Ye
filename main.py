"""
This bot may be used by anyone I give permission to, I guess.
"""
import discord
from discord.ext import commands
import os
from keep_alive import keep_alive

class Ye(commands.Bot):
  def __init__(self):
    intents = discord.Intents.default()
    intents.members = True
    intents.typing = True
    self.CONFIG = {
        "DebugMode":False,
        "Prefix": "-",
        "CogDirectory":os.path.join(os.path.dirname(__file__),"CogDirectory"),
        "UnloadableCogs":["setup"],
        "AdministratorIDs":[247248129282408448, 539166170239205396], # Fire, Stephen
        "Color":discord.Colour.red(),
        "KanyeFrequency":50
    }
    super().__init__(command_prefix=self.CONFIG.get("Prefix"),intents=intents)
  def checkAdmin(self,ctx):
    return ctx.message.author.id in self.CONFIG.get("AdministratorIDs")

client = Ye()

@client.command()
@commands.check(client.checkAdmin)
async def load(ctx, extension):
  """
    Function that loads cogs into the bot.
  """
  client.load_extension(f"cogs.{extension}")

@client.command()
@commands.check(client.checkAdmin)
async def unload(ctx, extension):
  """
    Function that unloads cogs from the bot.
  """
  if extension not in client.CONFIG.get("UnloadableCogs"):
    client.unload_extension(f"cogs.{extension}")

for filename in os.listdir(client.CONFIG.get("CogDirectory")):
  if filename.endswith(".py"):
    client.load_extension(f'CogDirectory.{filename[:-3]}')

keep_alive()
client.run(os.getenv('TOKEN'))
