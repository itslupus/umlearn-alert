#!/usr/bin/python3

import discord
import discord.ext.commands

from sqlite import SQLite

PREFIX = '.'

TOKEN = None
with open('token', 'r') as f:
	TOKEN = f.read()

activity = discord.Game(name = 'version alpha')
bot = discord.ext.commands.Bot(command_prefix = PREFIX, activity = activity, help_command = None)

@bot.event
async def on_connect():
	print('Connected to Discord')

@bot.event
async def on_ready():
	bot.load_extension('commands')
	SQLite()

	print('Bot ready')

@bot.command()
async def reload(context, module):
	bot.reload_extension(module)

	await context.channel.send('reloaded ' + module)
	await context.message.delete()

bot.run(TOKEN)