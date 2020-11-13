import discord
from discord.ext import commands, tasks

CHANNEL = 484113924468244495

class test(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
		self.output.start()

	@commands.command(name = 'here')
	async def here(self, context):
		await context.channel.send('hello')
	
	@tasks.loop(seconds = 10)
	async def output(self):
		await self.bot.get_channel(CHANNEL).send('loop')

def setup(bot):
	bot.add_cog(test(bot))
