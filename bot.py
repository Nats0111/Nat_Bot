import discord
from discord.ext import commands
import json

with open('setting.json', mode='r', encoding='utf8') as jfile:
   jdata = json.load(jfile)

bot = commands.Bot(command_prefix= '*')

@bot.event
async def on_ready():
   print(">> Bot is online <<")
   await bot.change_presence(activity = discord.Activity(type=discord.ActivityType.listening, name="My Prefix is * !"))

@bot.event
async def on_member_join(member):
   channel = bot.get_channel(int(jdata['WL_channel']))
   await channel.send(f'{member} join!')

@bot.event
async def on_member_remove(member):
   channel = bot.get_channel(int(jdata['WL_channel']))
   await channel.send(f'{member} left!')

@bot.command()
async def ping(ctx):
   await ctx.send(f'{round(bot.latency*1000)} (ms)')
 


bot.run(jdata['TOKEN'])