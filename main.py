import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print('Logamos como {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('Oi'):
        await message.channel.send('Oi sumido rs...')

client.run(os.getenv())  

