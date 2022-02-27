import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!')
bot.remove_command('help')

@bot.command()
async def help(ctx):
    embed = discord.Embed(
        title='Bot commands',
        description='Welcome to the help menu. Here are all the commands for this bot',
        color=discord.Colour.dark_magenta()
    )

    embed.set_thumbnail(url='https://blob.sololearn.com/avatars/f4c57516-be37-48bb-abfe-3b0658a2a804.jpg')
    embed.add_field(
        name='!help',
        value='List all the commands',
        inline='False'
    )
    embed.add_field(
        name='!punch',
        value='This command punches another member',
        inline='False'
    )


    await ctx.send(embed=embed)

@bot.command()
async def info(ctx):
    """
    This command shows information about the server and the person that is looking for help

    !info
    """

    await ctx.send(ctx.guild)
    await ctx.send(ctx.author)
    await ctx.send(ctx.message.id)

@bot.command()
async def punch(ctx, arg):
    """
    This command punches another member
    """

    await ctx.send(f'Punched {arg}')



