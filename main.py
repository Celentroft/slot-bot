# Github: https://github.com/Celentroft
# Don't be a skid, ty

import os
import json
import discord
from discord.ext import commands

config = json.load(open('config.json', 'r'))
bot = commands.Bot(command_prefix='!', intents=discord.Intents.all(), help_command=None)

commands_files = [f"commands.{filename[:-3]}" for filename in os.listdir("./commands/") if filename.endswith('.py')]
events_files = [f"events.{filename[:-3]}" for filename in os.listdir("./events/") if filename.endswith('.py')]

for file in commands_files:
    try:
        bot.load_extension(file)
    except Exception as e:
        print(f"failed to load {file}", e)

for file in events_files:
    try:
        bot.load_extension(file)
    except Exception as e:
        print(f"failed to load {file}", e)

@bot.event
async def on_ready():
    print(f"Logged as {bot.user.name}")
    print("Github: https://github.com/Scarlxrd211")
    print("Telegram: https://t.me/scarlxrd_1337")

bot.run(config["token"])