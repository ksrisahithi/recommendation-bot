import random
import discord
from finalspotifyapi import *
import os
from dotenv import load_dotenv
load_dotenv()

def rand_song():
    pair = random.choice(list(playlist.items()))
    ans = "'" + pair[0] + "' by " + pair[1]
    return ans

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    user_message = str(message.content)
    if message.author == client.user:
        return

    if user_message.startswith('$recommend'):
        await message.channel.send("kay wants to recommend " + rand_song() + " , let her know if you liked it")

client.run(os.getenv('TOKEN'))