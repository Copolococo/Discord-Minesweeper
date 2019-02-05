#!/usr/bin/env python3

import discord
import asyncio
import argparse
import minesweeper as ms

client = discord.Client()

@client.event
async def on_ready():
    print("Logged in")
    print(client.user.name)
    print(client.user.id)
    print("------")

@client.event
async def on_message(message):
    if message.content.startswith('.minesweeper'):
        level = ms.generate_level()
        text = ""
        for y in range(len(level)):
            for x in range(len(level[y])):
                text = text + "||`[" + str(level[y][x]) + "]`||"
            text = text + "\n"
        await client.send_message(message.channel, text)

parser = argparse.ArgumentParser(description="Simple discord bot")
parser.add_argument("-t", "--token", help="Discord bot token")
args = vars(parser.parse_args())

token = args["token"]

while token == None or token == "":
    token = input("insert bot token:\n")

client.run(token)