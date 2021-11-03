import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='./.')
bot.remove_command('help')


@bot.command()
async def help(ctx):
    embed = discord.Embed(
        title='tec-bot Commands',
        description='Welcome to the help section. The following are list of command',
        color=discord.Colour.green()
    )

    embed.set_thumbnail(url='https://i.pinimg.com/originals/e6/86/09/e68609dd0a5ccbd2f772908e9432e509.png')
    embed.add_field(
        name='>help',
        value='Show all the list of commands',
        inline=False
    )
    embed.add_field(
        name='>punch',
        value='Punch any user',
        inline=False
    )
    embed.add_field(
        name='>kick',
        value='kick many users',
        inline=False
    )
    embed.add_field(
        name='>badword',
        value='Say gago to user',
        inline=False
    )
    await ctx.send(embed=embed)


@bot.command()
async def badword(ctx, arg):
    """
    >punch command
    """
    await ctx.send(f'Gagooooo ka {arg} from {ctx.author}')


@bot.command()
async def punch(ctx, arg):
    """
    >punch command
    """
    await ctx.send(f'Punched {arg}')


@bot.command()
async def double_punch(ctx, arg1, arg2):
    """
    >dobule_punch command
    """
    await ctx.send(f'Double punched {arg1} and {arg2}')


@bot.command()
async def kick(ctx, *args):
    """
    >kick command
    """

    everyone = ', '.join(args)
    await ctx.send(f'kick in butt {everyone}')


@bot.command()
async def command(ctx):
    """
    >kick command
    """

    await ctx.send(f'>punch + "username" - punch the user')
    await ctx.send(f'>info - get the current user information')
    await ctx.send(f'>kick + "one or more username". - kick the user')
    await ctx.send(f'>double_punch + "username". - double punch the user')


@bot.command()
async def info(ctx):
    """
    ctx - context (information about how the command was executed

    >info
    """

    await ctx.send(ctx.guild)
    await ctx.send(ctx.author)
    await ctx.send(ctx.message.id)


bot.run('OTA0OTMwNDQxNTM3MTUwOTk2.YYCsJg.26ZlC-zEevtHAC_hSGwGF3twtGs')