import discord
from discord.ext import commands

bot = commands.Bot(command_prefix= '*')

@bot.event
async def on_ready():
   print(">> Bot is online <<")

@bot.event
async def on_member_join(member):
   channel = bot.get_channel(751116126754439239)
   await channel.send(f'{member} join!')

@bot.event
async def on_member_remove(member):
   channel = bot.get_channel(751116126754439239)
   await channel.send(f'{member} left!')

@bot.command()
async def ping(ctx):
   await ctx.send(f'{round(bot.latency*1000)} (ms)')
 


bot.run('NzUxMDgzNTU2NTk5NDk2NzA1.X1D7Eg.eC-SX9sCXL9LB7oxwXEwhAt1eUk')