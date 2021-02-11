# TentaAI
Made by [@TentaRJ](https://twitter.com/tentarj)

So, what is all of this?
This is a little passion project of mine! I wanted to make a great bot I can use!

But why, you may be asking yourself. Why did you go through the hassle of making a bot?
I got tired of bots where you have to pay for simple things like volume control or custom status or a different command prefix... so I did it myself!

![funny](https://external-preview.redd.it/0wJ2ZY6d6EwPxn39HOtt5Y6FSfEfsyvEoLQWY4tsS3M.jpg?auto=webp&s=678a2dbbf0311977b3bc0049e23583c86725b113)

### Getting Started!

First, you will need a way to host this whole thing! You can use your own IDE or you can use [Repl.it](https://repl.it) for development hosting. There are other services to look for however!

Second off, you will need to create a `config.py` file.
  1. Create a new file in the `assetFiles` folder called `config.py`.
  2. Add `value = {` at the start.
  3. Add `"token":` inside.
  4. Add your bot's token behind `"token":`.
  5. Close it off with `}`.
  It should look like this now:
  ```py
value = {
  "token" : "<Your-Token-Here>"
}
  ```
You can grab your bot's token from the [Discord Devloper Portal](https://discord.com/developers). Copy the token and keep it secret! If it ever gets lost, you can always regenerate it!

### What can the bot do?

You are able to set it to detect any word and respond with an array of options, like whenever you say `Mario`, it will trigger!

You can add your own custom commands using the [Discord API](https://discordpy.readthedocs.io/en/latest/api.html)! Just type this out to make a command:
```py
@client.command()
async def commandname(ctx):
  # Put any custom actions here!
```