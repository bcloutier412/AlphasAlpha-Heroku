import threading
import discord
from discord.ext import commands
from aquaHQ import aquaHQrun
from yuckPass import yuckPassrun
from test import testrun
from oni import onirun
from servercollection import *


# def ping_hosts_and_put_in_db():
#     while True:
#         print('ping a host...')
#         time.sleep(3)

# def main_menu():
#     while True:
#         choice = input('choose an option ')
#         if choice == 'scan':
#             t = threading.Thread(target=ping_hosts_and_put_in_db)
#             t.start()
#         else:
#             print('valid options are "scan"')

# if __name__ == '__main__':
#     main_menu()

# client = discord.Client()

# @client.event
# async def on_ready():
#     print('Bot is now online and ready to roll')


# @client.event
# async def on_message(message):

#     if message.author == client.user:
#         return
    
#     if message.content == 'hello':
#         await message.channel.send('Welcome here')

# client.run('OTU2NjYzNTgzNzE3MDkzMzc3.YjzgZA.rdHO42UDG60_M7AIb8aPTS8dAFU')

bot = commands.Bot(command_prefix='>')

@bot.command()
async def ping(ctx):
    await ctx.send('pong')


@bot.command()
async def run(ctx, arg=''):
    if arg == 'aquaHQ' and aquaHQ.isLive == False:
        aquaHQ.isLive = True
        t = threading.Thread(target=serverRun,args=(aquaHQ,))
        t.start()
        await ctx.send('aquaHQ online')
    elif arg == 'yuckPass' and yuckPass.isLive == False:
        yuckPass.isLive = True
        t = threading.Thread(target=serverRun,args=(yuckPass,))
        t.start()
        await ctx.send('yuckPass online')
    elif arg == 'test' and test.isLive == False:
        test.isLive = True
        t = threading.Thread(target=testrun)
        t.start()
        await ctx.send('Test monitor is online')
    elif arg == 'oni' and oni.isLive == False:
        oni.isLive = True
        t = threading.Thread(target=onirun)
        t.start()
        await ctx.send('Alpha Oni online')
    else:
        await ctx.send('Invalid Entry')

@bot.command()
async def end(ctx, arg=''):
    if arg == 'aquaHQ':
        aquaHQ.isLive = False
        await ctx.send('aquaHQ offline')
    elif arg == 'yuckPass':
        yuckPass.isLive = False
        await ctx.send('yuckPass offline')
    elif arg == 'test':
        test.isLive = False
        await ctx.send('test offline')
    elif arg == 'oni':
        oni.isLive = False
        await ctx.send('Alpha Oni offline')
    else:
        await ctx.send('Invalid Arg')

@bot.command()
async def isonline(ctx, arg=''):
    if arg == 'aquaHQ':
        await ctx.send(aquaHQ.isLive)
    elif arg == 'yuckPass':
        await ctx.send(yuckPass.isLive)
    elif arg == 'test':
        await ctx.send(test.isLive)
    elif arg == 'oni':
        await ctx.send(oni.isLive)
    else:
        await ctx.send('Invalid Arg')

@bot.command()
async def status(ctx):
    for value in servercollection:
        await ctx.send(value.serverName + ': ' + str(value.isLive))

# @bot.event
# async def on_command_error(ctx, error):
#     if isinstance(error, commands.MissingRequiredArgument):
#         await ctx.send('Please pass in all required arguements.')
    
bot.run('OTU2NjYzNTgzNzE3MDkzMzc3.YjzgZA.BnDgVc_fwiX2RhCeRqs-WGhab0g')

