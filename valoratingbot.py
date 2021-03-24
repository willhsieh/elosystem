from games import *

# bot.py
import os
import praw # Python Reddit API Wrapper

from dotenv import load_dotenv

# 1
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# 2
bot = commands.Bot(command_prefix='!')

# Initialize bot
@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

# @bot.command(name='ranks', help='Get the leaderboard')
# async def daily(num_posts):
#     print(printLeaderboard())

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == '!ranks':
        response = printLeaderboard()
        await message.channel.send(response)

bot.run(TOKEN)
