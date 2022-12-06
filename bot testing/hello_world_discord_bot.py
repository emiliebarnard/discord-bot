import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print("The bot has logged in!") #outputs to local command line
    server = client.guilds[0]
    first_channel = server.text_channels[0]
    #await first_channel.send("Hello, World!")
    await first_channel.send("Hello, @everyone!")

# call and response example
@client.event
async def on_message(message):
    if message.content == "Hello":
        await message.channel.send("Hi there!")

client.run(TOKEN)
