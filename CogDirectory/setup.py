import discord
from discord.ext import commands, tasks
import random

class YeHelpCommand(commands.HelpCommand):

  def __init__(self):
    super().__init__()
  
  async def send_bot_help(self,mapping):
    destination = self.get_destination()
    embed = discord.Embed(colour=discord.Colour.red(),title="Help Menu\n‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
    for cog in mapping:
      if len(mapping[cog]) > 0 and cog:
        cog_commands = [f"`{command.name}`\t{command.brief}" for command in cog.get_commands()]
        cog_string = "\n".join(cog_commands)
        embed.add_field(name=cog.qualified_name,value = cog_string,inline=False)
    await destination.send(embed=embed)
    return await super().send_bot_help(mapping)

  async def send_command_help(self,command):
    embed = discord.Embed(colour=discord.Colour.red(),title=f"Help for {command.name}",description=command.description)
    await self.get_destination().send(embed=embed)
    return await super().send_command_help(command)

  async def send_cog_help(self,cog):
    embed = discord.Embed(colour=discord.Colour.red(),title=f"Help for {cog.qualified_name}",description=cog.description)
    await self.get_destination().send(embed=embed)
    return await super().send_cog_help(cog)

class Setup(commands.Cog):
  
  def __init__(self,client):
    self.client = client
    self.STATUSES = [(discord.ActivityType.playing, "The College Dropout"),
            (discord.ActivityType.streaming, "Graduation"),
            (discord.ActivityType.listening, "My Beautiful Dark Twisted Fantasy"),
            (discord.ActivityType.watching, "Ye Sleep")]

  @commands.Cog.listener()
  async def on_ready(self):
    print("Bot is online")
    self.statusChange.start()

  @tasks.loop(seconds=30.0)
  async def statusChange(self):
      randStatus = random.choice(self.STATUSES)
      await self.client.change_presence(
          activity=discord.Activity(type=randStatus[0],
                                    name=randStatus[1],
                                    url="https://open.spotify.com/artist/5K4W6rqBFWDnAN6FQUkS6x?si=Tu32eXk-TkOw_B2aOxzjwA")),
def setup(client):
  client.add_cog(Setup(client))
  client.help_command = YeHelpCommand()