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
    #outputs to local command line
    print("The bot has logged in!")

@client.event
async def on_message(message):
    # server Hello, World! message
    if message.content == "hello":
        await message.channel.send("Hello, World!")

client.run(TOKEN)
