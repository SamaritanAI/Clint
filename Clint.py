import discord
from discord.ext import commands

client = discord.Client()

bot = commands.Bot(command_prefix='!')


@client.event
async def on_ready():
    print("Clint is here!")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == "hello":
        await message.channel.send("Welcome to my server!")

    # Reacting to messages
    if message.content == "cool":
        await message.add_reaction('\U0001F604')

# Check which user reacted with which emoji
@client.event
async def on_reaction_add(reaction, user):
    await reaction.message.channel.send(f'{user} reacted with {reaction.emoji}')

@client.event
async def on_message_edit(before, after):
    await before.channel.send(
        f'{before.author} edited a message.\n'
        f'Before: {before.content}\n'
        f'After: {after.content}'
    )

# Bot commands



