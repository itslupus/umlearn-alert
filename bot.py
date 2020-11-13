#!/usr/bin/python3

import discord
from discord.ext import commands

VERSION = '0.1a'
PREFIX = '.'

# over engineered reading of a single token
token = None
with open('token', 'r') as token_file:
	token = token_file.read()

bot = commands.Bot(command_prefix = PREFIX, activity = discord.Game(name = 'beep boop version ' + VERSION), help_command = None)

@bot.event
async def on_connect():
	print('Connected to Discord')

@bot.event
async def on_ready():
	print('Bot ready, version ' + VERSION)
	bot.load_extension('test')

bot.run(token)
