import os
from dotenv import load_dotenv
import random
import discord
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix= "/",intents=intents)

@client.event
async def on_ready():
    print("Ready for use!")
    print("="*20)

@client.command()
async def command_res(ctx):
    await ctx.send("Hello there ~ ")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    res = ["Hey!", "What's going on?","Hello there.","Yo-"]
    await message.channel.send(random.choice(res))
client.run(TOKEN)


