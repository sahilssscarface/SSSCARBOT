import discord
import os
from discord.ext import commands
from keep_alive import keep_alive

client = commands.Bot(command_prefix="!")
client.remove_command("help")

@client.group(invoke_without_command=True)
async def help(ctx):
  em = discord.Embed(title = "Help",description = "Use !help <command> for extended information",color  = ctx.author.color)
  em.add_field(name = "Sensitivity Converters", value="csgotovalo\nvalotocsgo")
  await ctx.send(embed = em)

@help.command()
async def csgotovalo(ctx):
 em = discord.Embed(title = "!csgotovalo", description = "Converts the CSGO sensitivity to the equivalent Valorant sensitivity, provided the mouse dpi remains constant ",color  = ctx.author.color)
 em.add_field(name  = "**Syntax**", value = "!csgotovalo <your csgo sensitivity>")
 await ctx.send(embed = em)

@help.command()
async def valotocsgo(ctx):
 em = discord.Embed(title = "!valotocsgo", description = "Converts the VALORANT sensitivity to the equivalent CSGO sensitivity, provided the mouse dpi remains constant ",color  = ctx.author.color)
 em.add_field(name  = "**Syntax**", value = "!valotocsgo <your valorant sensitivity>")
 await ctx.send(embed = em) 

@client.event
async def on_ready():
	print('We have logged in as {0.user}'.format(client))


@client.command()
async def csgotovalo(ctx, x: float):
  result = round((x/3.18),3)
  eb = discord.Embed(title = "Converted Sensitivity:",description = "{}".format(result),color  = ctx.author.color)
  await ctx.send(ctx.message.author.mention,embed = eb)
  
  
  
@client.command()
async def valotocsgo(ctx, x: float):
  result = round((x*3.18),2)
  eb = discord.Embed(title = "Converted Sensitivity:",description = "{}".format(result),color  = ctx.author.color)
  await ctx.send(ctx.message.author.mention,embed = eb)








keep_alive()
client.run(os.getenv('TOKEN'))
