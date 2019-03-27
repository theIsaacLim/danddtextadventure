# Work with Python 3.6
import discord

client = discord.Client()
TOKEN = 'NTU3NzY0OTQ4OTQ4OTQyODc4.D3YQtA.NhIFAjbb8MT5XNqFd_iqarh9LHI'

@client.event
async def on_ready():
    print("The bot is ready!")
    await client.change_presence(game=discord.Game(name="Making a bot"))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content == "Howdy":
        await client.send_message(message.channel, "Howdy, partner! Want to do some rootin\' and shootin\'?")
    elif message.content == "Fire":
        await client.send_message(message.channel, "Pow! Faster than ye shadow, ya pull out ya trusty revolver and shoot an innocent bucket that was nearby.")

client.run(TOKEN)
