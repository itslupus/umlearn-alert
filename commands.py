import discord
import discord.ext.commands

from sqlite import SQLite

CHANNEL = 484113924468244495

class commands(discord.ext.commands.Cog):
	def __init__(self, bot):
		self.bot = bot
		self.sql = SQLite()
		# self.output.start()

	@discord.ext.commands.command(name = 'here')
	async def here(self, context):
		await context.channel.send('hello')

	@discord.ext.commands.command(name = 'add')
	async def add_course(self, context, *args):
		if len(args) > 0 and len(args) < 3:
			channel_id = args[1] if len(args) == 2 else context.channel.id
			
			if not self.bot.get_channel(channel_id) == None:
				await context.channel.send('%s %s' % (args[0], channel_id))
			else:
				await context.channel.send('invalid channel %s' % (channel_id))

		else:
			await context.channel.send('invalid parameters for add')

		await context.message.delete()
	
	# @tasks.loop(seconds = 10)
	# async def output(self):
	# 	await self.bot.get_channel(CHANNEL).send('loop')

def setup(bot):
	bot.add_cog(commands(bot))