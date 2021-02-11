#This is a file that allows me to throw templates into here to save up on line space.
#python -m pip

# Setting `Playing ` status
await bot.change_presence(activity=discord.Game(name="a game"))

# Setting `Streaming ` status
await bot.change_presence(activity=discord.Streaming(name="My Stream", url=my_twitch_url))

# Setting `Listening ` status
await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="a song"))

# Setting `Watching ` status
await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="a movie"))

@client.event
async def [command]()
if "word" in ctx.content.lower:
  print("Word detected")
  await ctx.channel.send("Response")
elif "other word" in ctx.content:
  print("Other word detected"
  await ctx.channel.send("Response")
else :
  return

@client.event
async def embed5():
    emb=ctx.content.split()
    inputTitle=emb[1]
    inputEmbedTitle=emb[2]
    inputDescription=emb[3]
    inputColor=emb[4]
    inputAuthorName=emb[5]
    inputAuthorURL=emb[6]
    inputAuthorIconURL=emb[7]
    inputThumbnail=emb[8]
    inputFooterText=emb[9]
    inputFieldName1=emb[10]
    inputFieldValue1=emb[11]
    inputFieldInline1=emb[12]
    inputFieldName2=emb[13]
    inputFieldValue2=emb[14]
    inputFieldInline2=emb[15]
    inputFieldName3=emb[16]
    inputFieldValue3=emb[17]
    inputFieldInline3=emb[18]
    inputFieldName4=emb[19]
    inputFieldValue4=emb[20]
    inputFieldInline4=emb[21]
    inputFieldName5=emb[22]
    inputFieldValue5=emb[23]
    inputFieldInline5=emb[24]
    embed=discord.Embed(title=inputTitle, url=inputEmbedTitle, description=inputDescription, color=inputColor)
    embed.set_author(name=inputAuthorName, url=inputAuthorURL, icon_url=inputAuthorIconURL)
    embed.set_thumbnail(url=inputThumbnail)
    embed.set_footer(text=inputFooterText)
    embed.add_field(name=inputFieldName1, value=inputFieldValue1, inline=inputFieldInline1)
    embed.add_field(name=inputFieldName2, value=inputFieldValue2, inline=inputFieldInline2)
    embed.add_field(name=inputFieldName3, value=inputFieldValue3, inline=inputFieldInline3)
    embed.add_field(name=inputFieldName4, value=inputFieldValue4, inline=inputFieldInline4)
    embed.add_field(name=inputFieldName5, value=inputFieldValue5, inline=inputFieldInline5)
    await ctx.channel.send(embed=embed)
    return

output=ctx.channel.send("message content here")

def checkDelete(reaction, user):
  return user == ctx.author and str(reaction.emoji) == '🗑'

await output.add_reaction(emoji='🗑')
try:
  await client.wait_for('reaction_add', timeout=300.0,  check=checkDelete)
except asyncio.TimeoutError:
  return
else:
  await output.delete()