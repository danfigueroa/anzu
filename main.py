import discord
import os
import requests
import json
import random
from replit import db
from keep_alive import keep_alive
import dice

client = discord.Client()


@client.event
async def on_ready():
    print("Logamos como {0.user}".format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("oi"):
        await message.channel.send("Oi sumido rs...")

    elif message.content.startswith("cachorro"):
        await message.channel.send("au au")

    elif message.content.startswith("rolar"):
        rolagem = message
        # score = dice.roll(rolagem[1])
        await message.channel.send(rolagem.split("rolar ")[1])
        # score = dice.roll("2d6+18")


keep_alive()
client.run(os.getenv("TOKEN"))
