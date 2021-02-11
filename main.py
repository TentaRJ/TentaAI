import os
import discord
import asyncio
import json
import random
import time
import datetime
from PIL import Image
from discord.ext import commands
from func_timeout import func_timeout, FunctionTimedOut
from assetFiles.keep_alive import keep_alive
from assetFiles.bowser import bowser

client = commands.Bot(command_prefix="?")

tentaID = "270293124444717056"
client.bot_id = "798286010944585759"
delayInput = 5 

async def is_owner(ctx):
  return ctx.author.id == int(tentaID)

@client.event   # When the bot is ready
async def on_ready():
  timeRaw=datetime.datetime.now()
  time=(timeRaw.strftime("%X"))
  date=(timeRaw.strftime("%x"))
  await client.change_presence(status=discord.Status.online, activity=discord.Game(name=f"Connected at {time} {date} GMT"))
  print('Bot Connected!')
  print("Discord.py Version ", discord.__version__)
  with os.scandir('.//') as entries:
    print("In rootDirectory:")
    for entry in entries:
        print(entry.name)
  with os.scandir('.//assetFiles') as entries:
    print("\nIn assetFiles:")
    for entry in entries:
      print(entry.name)
  with os.scandir('.//gamble') as entries:
    print("\nIn gamble:")
    for entry in entries:
      print(entry.name)
  print("\n")

@client.event
async def on_message(ctx):
  if ctx.author.id == client.bot_id:
    return
  if ctx.author.bot == True:
    return
  if "mario" in ctx.content.lower():
    inputBowser=random.choice(bowser)
    embed=discord.Embed(title="Mario?!", url="", description="How dare you disturb my family vacation!", color=discord.Color.red())
    embed.set_author(name="Bowser", url="", icon_url=inputBowser)
    embed.set_thumbnail(url=inputBowser)
    await ctx.channel.send(embed=embed)
  elif "swear" in ctx.content.lower():
    # message = await ctx.fetch_message(id)
    # print(message)
    try:
      await ctx.channel.purge(limit=1)
      await ctx.channel.send(f"**Woah there {ctx.author.mention}! You can't say that! Saying too many offensive words will get you muted!**")
    except:
      await ctx.channel.send(f"**Woah there {ctx.author.mention}! You can't say that! Saying too many offensive words will get you muted!**")
  else:
    await client.process_commands(ctx)

@client.command()
@commands.check(is_owner)
async def test(ctx):
  output=await ctx.channel.send("message content here")

  def checkDelete(reaction, user):
    return user == ctx.author and str(reaction.emoji) == '🗑'

  await output.add_reaction(emoji='🗑')
  try:
    await client.wait_for('reaction_add', timeout=300.0,  check=checkDelete)
  except asyncio.TimeoutError:
    return
  else:
    await output.delete()

@client.command()
async def file(ctx):
  value=ctx.content.split()
  file=open(".//gamble//ID.py", 'r')
  ID=file.read()
  file.close()
  try:
    if value[1] in ID:
      file=open(f".//gamble//{value[1]}.py", "r")
      data=file.read()
      file.close()
      await ctx.channel.send(f"```File:\n{data}```")
      return
    else:
      await ctx.channel.send(f"```\nFile not found! Are you sure the user used {client.command_prefix}gamble set?\n```")
  except:
    with os.scandir('.//gamble') as entries:
      for entry in entries:
        files= entry.name
    await ctx.channel.send(f"```The propper way to format your query is ?check [file name]\nThe files available to check are:\n{files}\n```")
    return

@client.command()
async def die(ctx):
  await ctx.channel.send("*Cough cough!* Im dying! Nooo!")
  await client.close()

@client.command()
async def clear(ctx, clearValue=''):
  try:
    try:
      delete = await ctx.channel.purge(limit=int(clearValue))
      message = await ctx.channel.send(f"Purge complete! Deleted {clearValue} messages!")
      time.sleep(delayInput)
    except:
      delete=await ctx.channel.purge(limit=9999999999999999999)
      message=await ctx.channel.send(f"Purge complete! Deleted all messages!")
      time.sleep(delayInput)
    await message.delete()
  except:
    await ctx.channel.send("nah")

@client.command()
@commands.check(is_owner)
async def invite(ctx):
  from assetFiles.invite import invite
  if str(ctx.author.id) == str(tentaID):
    await ctx.channel.send(f"{invite}")
  else:
    await ctx.channel.send("Aww, you wanna invite me! Unfortunatly, I can't be shared...")

@client.command()
async def change(ctx):
  print("Status!")
  content=ctx.content.split()
  inputStatus=content[1]
  inputActivity=content[2]
  inputName=content[3]
  print(inputStatus, inputActivity, inputName)
  if inputStatus.lower() == "online":
    val1=discord.Status.online
  elif inputStatus.lower() == "idle":
    val1=discord.Status.idle
  elif inputStatus.lower() == "dnd":
    val1=discord.Status.do_not_disturb
  elif inputStatus.lower() == "offline":
    val1=discord.Status.invisible
  else:
    print("1")
    return
  if inputActivity.lower() == "playing" or inputActivity.lower() == "game":
    val2=discord.Game(name=inputName)
  elif inputActivity.lower() == "streaming":
    val2=discord.Streaming(name=inputName, url="")
  elif inputActivity.lower() == "listening":
    val2=discord.Activity(type=discord.ActivityType.listening, name=inputName, large_image_URL=inputBowser)
  elif inputActivity.lower() == "watching":
    val2=discord.Activity(type=discord.ActivityType.watching, name=inputName, large_image_URL=inputBowser)
  else:
    print("2")  
    return
  await pres(val1, val2)

@client.command()
async def ping(ctx):
  print("ping!")
  await ctx.channel.send(f"Pong! This ping took {round (client.latency * 1000)}ms to get back.")

@client.command()
async def info(ctx):
	await ctx.channel.send(f"> Hey there! I am ModBot, a helpfull tool created in Python by my owner, @{tentaRJ.mention}")

@client.command()
async def hello(ctx):
	await ctx.channel.send(f"Hello {ctx.author.mention}!")

@client.command()
async def plug(ctx):
	await ctx.channel.send(f"https://www.twitter.com/TentaRJ")

@client.command()
async def who(ctx):
  who=805879990943481876
  print(who)

@client.command()
async def judge(ctx):
  file=open(f'.//assetFiles/judge.py', 'r')
  judge=file.read()
  file.close()
  judgeValue=random.randint(1,9)
  while judge == judgeValue:
    judgeValue=random.randint(1,9)
    if judge != judgeValue:
      break
  embed=discord.Embed(title="Mr. Game and Watch's Judge 'o Fun!", url="https://twitter.com/Maister_SSB", description=f"You got hit by {judgeValue}!", color=discord.Color.blue())
  embed.set_author(name="The Funny Man Himself!", url="https://twitter.com/Maister_SSB", icon_url="https://pbs.twimg.com/profile_images/1334922327713308675/sG56XOZW_400x400.jpg")
  embed.set_thumbnail(url="")
  embed.set_footer(text="Funny Judge")
  file=open(".//assetFiles/judge.py", "w")
  file.write(f'{judgeValue}')
  file.close
  time.sleep(.75)
  await ctx.channel.send(embed=embed)

@client.command()
async def gamble(ctx, gValue=''):
  gUser=str(ctx.author.id)
  try:
    if "set" in gValue.lower():
      rV=0
      file=open(f".//gamble//ID.py", "r")
      ID = file.read()
      file.close()
      if gUser in ID:
        message=await ctx.channel.send(f'Woah {ctx.author.mention}! You are about to **reset** your casino file!\nIf you want to continue, react to this message with 🗑 in 10 seconds to erase everything!')
        await message.add_reaction(emoji='🗑')

        def checkReset(reaction, user):
          return user == ctx.author and str(reaction.emoji) == '🗑'

        try:
          await client.wait_for('reaction_add', timeout=10.0, check=checkReset)
          rV=1
        except asyncio.TimeoutError:
          await message.delete()
          time.sleep(0.01)
          await ctx.channel.send(f'{ctx.author.mention} Action canceled')
          return
      elif gUser not in ID:
        file2=open(f".//gamble/ID.py", "a")
        file2.write(f'"{gUser}", ')
        file2.close()
        file=open(f".//gamble/{gUser}", "x")
        rV=0
      else:
        return
      if rV==1:
        await message.delete()
        output=await ctx.channel.send("Ok then. Resetting...")
        file=open(f'.//gamble//{gUser}.py', 'w')
        file.write(f'id="{ctx.author.id}"\nname="{ctx.author.name}"\n0')
        file.close()
        time.sleep(2)
      elif rV==0:
        output=await ctx.channel.send("Setting up...")
        time.sleep(2)
        file=open(f'.//gamble//{gUser}.py', 'w')
        file.write(f'id="{ctx.author.id}"\nname="{ctx.author.name}"\n0')
        file.close()
        print(gUser)
      await output.edit(content=f"All done! File created for {ctx.author.mention}!")

      def checkDelete(reaction, user):
        return user == ctx.author and str(reaction.emoji) == '🗑'

      await output.add_reaction(emoji='🗑')
      try:
        await client.wait_for('reaction_add', timeout=300.0,  check=checkDelete)
      except asyncio.TimeoutError:
        return
      else:
        await output.delete()
    elif "add" in gValue.lower():
      await ctx.channel.send("This should work...")
      try:
        change=-100
        await gambleAdd(ctx,gUser,change)
        return
      except:
        await ctx.channel.send(f'`Error! There is no file! Use "{client.command_prefix}gamble set" to make a file!`')
    else:
      await ctx.channel.send(f"Hey there {ctx.author.mention}!\n```We have some cool commands to use for gambling!\nThe current actions are:\n[set]\n\nStructure your command like this:\n{client.command_prefix}gamble [action]\n\nExample:\n{client.command_prefix}gamble reset```")
      return
  except:
    print("2")
    await ctx.channel.send(f"Hey there {ctx.author.mention}!\n```We have some cool commands to use for gambling!\nThe current actions are:\n[set]\n\nStructure your command like this:\n{client.command_prefix}gamble [action]\n\nExample:\n{client.command_prefix}gamble reset```")

@client.event
async def gambleAdd(ctx,gUser,change):
  file=open(f".//gamble/{gUser}.py", "r")
  rawInfo=file.read().split("\n")
  file.close()
  print(rawInfo[2])
  sumValue = int(rawInfo[2])+change
  file=open(f".//gamble/{gUser}.py", "w")
  file.write(f'{rawInfo[0]}\n{rawInfo[1]}\n{sumValue}')
  file.close()
  await ctx.channel.send(sumValue)

extensions = [
	'cogs.cog_example'  # Same name as it would be if you were importing it
]

if __name__ == '__main__':  # Ensures this is the file being ran
	for extension in extensions:
		client.load_extension(extension)  # Loades every extension.

keep_alive()

try:
  from config import value
  client.run(value['token'])
except:
  print(f"\n\nUh oh! Something happened!\n\nMake sure your config.py is formatted properly and the token is correct!\n\n")