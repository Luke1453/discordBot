# Work with Python 3.6
import discord
from discord import Game
from discord.ext import commands
from discord.ext.commands import Bot
import random
import asyncio
import aiohttp
# from time import * #for debugging


BOT_PREFIX = ("!")

TOKEN = "NTM1OTM4MjE5NTM2MTU0NjM0.DyPbUg.meucjFVT65LI9NYyHlKQKasb-qw"

client = Bot(command_prefix=BOT_PREFIX,)
client.remove_command("help")

# Function for exit


def bot_exit():
    client.logout()
    client.close()
    exit(0)

"""
# Logging in
@client.event
async def on_ready():
    await client.change_presence(game=Game(name="!Gay"))
    print("Logged in as " + client.user.name)
    print(client.user.id)
    print('------')
"""

@client.event
async def on_message(message):
    if message.author.id == "205614254148157440":
        await client.add_reaction(message, '🍆')
        await client.add_reaction(message, '💦')
    # To enable commands
    await client.process_commands(message)

"""
#on typing bullying
bully = True
@client.event
async def on_typing(channel, user, when):
    global bully
    await asyncio.sleep(1)
    if  bully == True:
        #time = strftime("%H:%M:%S", gmtime())
        await client.send_message(channel, "%s Learn to type faster cunt." % user.mention)
        bully = False
    else: 
        await asyncio.sleep(180)
        bully= True
"""


@client.command(pass_context=True)
async def Gay(ctx):
    if ctx.message.author.id == "252171414981967873":  # me
        edvardid = '<@205614254148157440>'
        await client.say("%s is gay af." % edvardid)
    else:
        mem = list(client.get_server("245253328445898762").members)
        await client.say("%s is gay af." % random.choice(mem).mention)
        await client.add_reaction(ctx.message, '😡')


@client.command()
async def Square(number):
    squared_value = int(number) * int(number)
    await client.say(str(number) + " squared is " + str(squared_value))


@client.command()
async def Cry():
    msg = ":cry:"
    await client.say(msg)


@client.command()
async def Hello(*arg):
    if arg[0] == "There":
        await client.upload(r'C:\\Users\\Luke\\Desktop\\python\\Discord Bot\\Images\\generel_kenobi.jpg')
    if arg[0] == "Sexy":
        await client.upload(r'C:\\Users\\Luke\\Desktop\\python\\Discord Bot\\Images\\Sex.jpeg')
    if arg[0] == "Scary":
        await client.upload(r'C:\\Users\\Luke\\Desktop\\python\\Discord Bot\\Images\\Scarry.jpeg')
    if arg[0] == "Depression":
        await client.upload(r'C:\\Users\\Luke\\Desktop\\python\\Discord Bot\\Images\\deppressed.gif')


# Help command
@client.command(pass_context=True)
async def help(ctx):

    sender = ctx.message.author

    helpembed = discord.Embed(
        colour=discord.Colour.purple()
    )

    helpembed.set_author(name='Help')

    helpembed.add_field(
        name='!Hello', value='Responds with a meme.', inline=True)
    helpembed.add_field(
        name='Arguments', value='There, Sexy, Depression, Scary', inline=True)

    helpembed.add_field(
        name='!Gay', value='Mentions random member of Sombrero Army and calls him gay.', inline=False)

    helpembed.add_field(name='!Cry', value='Sends crying emoji.', inline=False)

    helpembed.add_field(
        name='!Square', value='Responds with square of argument.', inline=False)

    await client.send_message(sender, embed=helpembed)

# Logging off command
@client.command(pass_context=True)
async def STFU(ctx):
    if ctx.message.author.id == "252171414981967873":
        msg = "Logging off, Dad. :disappointed_relieved:"
        await client.say(msg)
        bot_exit()
    else:
        await client.say("BTFO! You dont have a fucking permit!")


"""async def list_servers():
    await client.wait_until_ready()
    while not client.is_closed:
        print("Current servers:")
        for server in client.servers:
            print(server.name)
        await asyncio.sleep(600)"""

# client.loop.create_task(list_servers())
client.run(TOKEN)
