import discord
import discord.ext.commands
import asyncio

from sqlite import SQLite

COLOUR = discord.Color.from_rgb(0, 153, 0)

class commands(discord.ext.commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.sql = SQLite()

        self.courses = []

        # self.output.start()

    def generate_response(self, title, description):
        return discord.Embed(title = title, description = description, color = COLOUR)

    @discord.ext.commands.command(name = 'test')
    async def test(self, context):
        embed = discord.Embed(title = 'test command', description = 'top desc', color = COLOUR)
        embed.add_field(name = 'desc', value = ':one: emoji test', inline = False)

        message = await context.channel.send(embed = embed)
        await message.add_reaction('1\N{COMBINING ENCLOSING KEYCAP}')

        def check(reaction, usr):
            return str(reaction.emoji) == '1\N{COMBINING ENCLOSING KEYCAP}' and usr == context.author

        embed.clear_fields()

        try:
            await self.bot.wait_for('reaction_add', timeout = 5.0, check = check)
        except asyncio.TimeoutError:
            embed.add_field(name = 'desc', value = 'bad emoji', inline = False)
        else:
            embed.add_field(name = 'desc', value = 'good emoji', inline = False)
        finally:
            await message.edit(embed = embed)

    @discord.ext.commands.command(name = 'add')
    async def add_course(self, context, *args):
        channel_obj = context.message.channel_mentions

        if len(args) == 1:
            channel_id = context.channel
        elif len(args) == 2 and len(channel_obj) == 1:
            channel_obj = channel_obj[0]
        else:
            channel_obj = None

        if channel_obj == None:
            embed = self.generate_response('', 'Invalid channel `%s`' % args[1])
            await context.channel.send(embed = embed)
        else:
            embed = self.generate_response('', '%s %s' % (args[0], args[1]))
            await context.channel.send(embed = embed)

        await context.message.delete()
    
    @discord.ext.commands.command(name = 'setup')
    async def setup(self, context):
        pass

    # @tasks.loop(seconds = 10)
    # async def output(self):
    # 	await self.bot.get_channel(CHANNEL).send('loop')

def setup(bot):
    bot.add_cog(commands(bot))