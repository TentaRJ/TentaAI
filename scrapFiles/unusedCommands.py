# @client.command()
# async def refresh(ctx):
#   message = await ctx.channel.send('Refreshing! Please wait a moment!')
#   fileTimeRaw=datetime.datetime.now(); fileTime=(f'{(fileTimeRaw.strftime("%x"))}, {(fileTimeRaw.strftime("%X"))}')
#   file = open("memberList.py", "w"); file.write(f'Filed at {fileTime} for server {ctx.guild}')
#   file2 = open("idList.py", "w"); file2.write(f'idInput = (\n')
#   memValue=0
#   for member in ctx.guild.members:
#     memValue += 1
#     file.write(f'\n{memValue}: {member} ID: {member.id}\n')
#     file2.write(f'"{member.id}"\n')
#   file2.write(")")
#   file.close(); file2.close()
#   time.sleep(1)
#   # await deleteMSG(ctx)
#   time.sleep(.5)
#   await message.edit(content=f"Refreshed the internal memory list! I logged {memValue} members!")

# @client.command()
# async def log(ctx):
#   logType = ctx.content.split()
#   logRaw=datetime.datetime.now()
#   logTime=(logRaw.strftime("%x"))+(logRaw.strftime("%X"))
#   try:
#     if "a" in logType[1].lower() or "w" in logType[1].lower() or "write" in logType[1].lower():
#       logV="1"
#       file = open("txt/discordLog.py", "a")
#       file.write(f'{ctx}\n\nLog written at {logTime}\n\n')
#       file.close()
#       await ctx.channel.send("Log written!")
#     elif "r" in logType[1].lower() or "read" in logType[1].lower():
#       logV="1"
#       file = open("txt/discordLog.py", "r")
#       data = file.read()
#       file.close()
#       emojiV = "🗑"
#       messageV = await ctx.channel.send(f'```py\n{data}\n```')
#       await messageV.add_reaction(emoji=emojiV)
#       # try:
#       #   print("1")
#       #   messageV.wait_for('reaction_add', reaction.emoji == emojiV, message.author.id != client.bot_id)
#       #   await ctx.channel.send("It worked")
#       # except:
#       #   print("2")
#       return
#     elif "c" in logType[1].lower() or "clear" in logType[1].lower():
#       logV="1"
#       file = open("txt/discordLog.py", "w")
#       file.write(f'Cleared at {logTime}\n')
#       file.close()
#       await ctx.channel.send("Log cleared!")
#   except: 
#     if logV=="0":
#       await ctx.channel.send("R(read), W(write), and C(clear) are available!")
#     else:
#       return