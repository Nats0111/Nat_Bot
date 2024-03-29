import discord
from discord.ext import commands
from Core.Classes import Cog_Extension
import random
import json

with open('setting.json', mode='r', encoding='utf8') as jfile:
   jdata = json.load(jfile)


class React(Cog_Extension):

   @commands.command()
   async def web(self, ctx):
      random_pic = random.choice(jdata['url_pic'])
      await ctx.send(random_pic)

   @commands.command()
   async def 圖片(self, ctx):
      random_pic = random.choice(jdata['pictrue'])
      pictrue = discord.File(random_pic)
      await ctx.send(file= pictrue)


def setup(bot):
    bot.add_cog(React(bot))