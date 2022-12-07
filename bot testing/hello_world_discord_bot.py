import os
import discord
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True #
bot = commands.Bot(command_prefix='$', intents=intents) # $ can be changed

@bot.command()
async def hello(ctx):
    await ctx.send("Hello, World!")
@bot.command()
async def bye(ctx):
    await ctx.send("Goodbye!")
@bot.command()
async def name(ctx, arg): # you can also add arguments
    await ctx.send("Hello, " + arg + "!")

bot.run(TOKEN) # we call run on bot instead of client

# intents = discord.Intents.default()
# intents.message_content = True
# client = discord.Client(intents=intents)
#
# @client.event
# async def on_ready():
#     print("The bot has logged in!") #outputs to local command line
#     server = client.guilds[0]
#     first_channel = server.text_channels[0]
#     #await first_channel.send("Hello, World!")
#     await first_channel.send("Hello, @everyone!")
#
# # call and response example
# @client.event
# async def on_message(message):
#     if message.content == "Hello":
#         await message.channel.send("Hi there!")
#
# client.run(TOKEN)
