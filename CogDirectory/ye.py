import discord
from discord.ext import commands
import requests
import random

class KanyeQuotesModule(commands.Cog):
  """
  Based
  """
  def __init__(self, client):
    self.client = client
  @commands.command(
    aliases=["kanye","Kanye","Advice","advice","ye", "YE"],
    brief="Replies with a Kanye Quote",
    description="Replies with a Kanye Quote, use `-ye <User Nickname/Mention>` to direct the quote at an individual."
  )
  async def KanyeQuotes(self,ctx,member:discord.Member=None):
    """
    Replies with a Kanye Quote
    """
    quote = requests.get("https://api.kanye.rest/").json()["quote"]
    if member:
      await ctx.send(f"{quote}")
    else:
      await ctx.send(quote)

  @commands.Cog.listener()
  async def on_message(self,message):
    """
    For every message, there is a 0.25% chance of a Kanye quote reply
    """
    if random.randint(0,self.client.CONFIG.get("KanyeFrequency")) == 0 and message.author != self.client.user:
      quote = requests.get("https://api.kanye.rest/").json()["quote"]
      await message.send(quote,mention_author=False)
def setup(client):
  client.add_cog(KanyeQuotesModule(client))




