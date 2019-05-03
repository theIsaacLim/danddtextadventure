import discord
from discord.ext import commands
import random

description = ''' Rootin' tootin' shootin' game, where ye shoot up the bad guys, and maybe shoot up the good guys too!
'''
## Input commands using the prefix '-'
bot = commands.Bot(command_prefix='tfw ', description=description)
TOKEN = 'NTU3NzY0OTQ4OTQ4OTQyODc4.D3YQtA.NhIFAjbb8MT5XNqFd_iqarh9LHI'

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def shoot(enemy : str):
    "Takes the enemy that you want to shoot"
    await bot.say("There's no shootin\' to be done here! Ya bullet hits an innocent cat that was sleepin\' next to ye.")

'''
@bot.command()
async def add(left : int, right : int):
    """Adds two numbers together."""
    await bot.say(left + right)

@bot.command()
async def roll(dice : str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await bot.say('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await bot.say(result)

@bot.command(description='For when you wanna settle the score some other way')
async def choose(*choices : str):
    """Chooses between multiple choices."""
    await bot.say(random.choice(choices))

@bot.command()
async def repeat(times : int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await bot.say(content)

@bot.command()
async def joined(member : discord.Member):
    """Says when a member joined."""
    await bot.say('{0.name} joined in {0.joined_at}'.format(member))

@bot.group(pass_context=True)
async def cool(ctx):
    """Says if a user is cool.
    In reality this just checks if a subcommand is being invoked.
    """
    if ctx.invoked_subcommand is None:
        await bot.say('No, {0.subcommand_passed} is not cool'.format(ctx))

@cool.command(name='bot')
async def _bot():
    """Is the bot cool?"""
    await bot.say('Yes, the bot is cool.')

'''

bot.run('NTU3NzY0OTQ4OTQ4OTQyODc4.D3YQtA.NhIFAjbb8MT5XNqFd_iqarh9LHI')
