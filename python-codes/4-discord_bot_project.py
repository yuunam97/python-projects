# Use this to execute the command: py -3 -m pip install -U discord.py

import discord
import requests
import json
from random import choice
# from main_discord_bot import random_message
from dotenv import dotenv_values

config = dotenv_values(".env")

DISCORD_TOKEN = config['DISCORD_BOT_TOKEN']

def random_message():
    bot_responses = [
        'Sue, always know that I am here for you <3',
        'Let\'s go for some running and gym sessions!',
        'Did you take a nice big poo poos?',
        'I missed you for the last 24 hours, 1440 minutes, and 86400 seconds!',
        'I love you more than pizza…and I really, really love pizza.',
        'I heard that a kiss can burn 6.4 calories per minute. You wanna workout?',
        'If you kiss me, I\'m not responsible for what happens next.',
        'I felt a little off today, but you turned me on.',
        'Please be my fav penguin who runs to me whenever I come over!.',
        'I am craving for our snuggles and cuddles!',
        'That film: Poppy Hills was pretty bad ngl',
        'Let\'s go for some cheese cakes and bubble tea!',
        'Custard and malva pudding?',
        'You know you love me Sue... you cannot resist me Mwahaha~!'
        'Let\'s go Siuuuuuuuuu~~!',
        'I love you Sue <3',
    ]

    random_message = choice(bot_responses)

    return random_message


def get_meme():
    response = requests.get('https://meme-api.com/gimme/wholesomememes')
    json_data = json.loads(response.text)
    return json_data['url']

def get_cat_meme():
    response = requests.get('https://meme-api.com/gimme/Catmemes')
    json_data = json.loads(response.text)
    return json_data['url']

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        if message.author == client.user:
            return
        
        if message.content.startswith("Hey Sue".lower() or "Sue".lower()):
            await message.channel.send("I love you Sue! My cute lil potata babs <3")
        elif message.content.startswith("Hey Yuu".lower() or "Yuu".lower()):
            await message.channel.send(random_message())
        elif message.content.startswith("Aweh".lower()):
            await message.channel.send("Aweh my Sue-Brie <3")
        elif message.content.startswith("meme"):
            await message.channel.send(get_meme())
        elif message.content.startswith("gimme cat memes"):
            await message.channel.send(get_cat_meme())

## These are the settings for what our Discord bot can access
# Since we've assigned the default() behavior for our bot, 
# we'll need to explicitly allow it to interact with messages (i.e., message_content=True)
intents = discord.Intents.default()
intents.message_content = True

# the main way to start the client:
client = MyClient(intents = intents)
client.run(DISCORD_TOKEN)
