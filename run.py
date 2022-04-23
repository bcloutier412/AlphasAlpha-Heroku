from http import server
import threading
import discord
from discord.ext import commands
from servercollection import *

autoRun = False
def autorun():
    autoRun = True
    while autoRun == True:
        print('start of the iteration')
        try:    
            for server in servercollection:
                if server.isLive == False and server.initialactivation == True:
                    t = threading.Thread(target=serverRun,args=(server,))
                    t.start()
                    print(server.serverName + " is online")
            print('auto run scanned')
        except:
            pass
        time.sleep(5)

bot = commands.Bot(command_prefix='>')

@bot.command()
async def ping(ctx):
    await ctx.send('pong')


@bot.command()
async def run(ctx, arg=''):
    global autoRun
    if arg == 'aquaHQ' and aquaHQ.isLive == False:
        aquaHQ.isLive = True
        t = threading.Thread(target=serverRun,args=(aquaHQ,))
        t.start()
        await ctx.send('aquaHQ online')
    elif arg == 'test' and test.isLive == False:
        test.isLive = True
        t = threading.Thread(target=serverRun,args=(test,))
        t.start()
        await ctx.send('Test monitor is online')
    elif arg == 'kaijukingz' and kaijukingz.isLive == False:
        kaijukingz.isLive = True
        t = threading.Thread(target=serverRun,args=(kaijukingz,))
        t.start()
        await ctx.send('Kaiju Kingz monitor is online')
    elif arg == 'llama' and llama.isLive == False:
        llama.isLive = True
        t = threading.Thread(target=serverRun,args=(llama,))
        t.start()
        await ctx.send('llama monitor is online')
    elif arg == 'degenpass' and degenpass.isLive == False:
        degenpass.isLive = True
        t = threading.Thread(target=serverRun,args=(degenpass,))
        t.start()
        await ctx.send('degenpass monitor is online')
    elif arg == 'doodle' and doodle.isLive == False:
        doodle.isLive = True
        t = threading.Thread(target=serverRun,args=(doodle,))
        t.start()
        await ctx.send('doodle monitor is online')
    elif arg == 'rcc' and rcc.isLive == False:
        rcc.isLive = True
        t = threading.Thread(target=serverRun,args=(rcc,))
        t.start()
        await ctx.send('rcc monitor is online')
    elif arg == 'autorun' and autoRun == False:
        autoRun = True
        t = threading.Thread(target=autorun)
        t.start()
        await ctx.send('autorun mode monitor is online')
    elif arg =='sendembed':
        sendEmbed()
    else:
        await ctx.send('Invalid Entry')

@bot.command()
async def end(ctx, arg=''):
    if arg == 'aquaHQ':
        aquaHQ.isLive = False
        # aquaHQ.initialactivation = False
        await ctx.send('aquaHQ offline')
    elif arg == 'test':
        test.isLive = False
        await ctx.send('test offline')
    elif arg == 'kaijukingz':
        kaijukingz.isLive = False
        kaijukingz.initialactivation = False
        await ctx.send('Kaiju Kingz offline')
    elif arg == 'llama':
        llama.isLive = False
        llama.initialactivation = False
        await ctx.send('llama offline')
    elif arg == 'degenpass':
        degenpass.isLive = False
        degenpass.initialactivation = False
        await ctx.send('degenpass offline')
    elif arg == 'doodle':
        doodle.isLive = False
        doodle.initialactivation = False
        await ctx.send('doodle offline')
    elif arg == 'rcc':
        rcc.isLive = False
        rcc.initialactivation = False
        await ctx.send('rcc offline')
    else:
        await ctx.send('Invalid Arg')

@bot.command()
async def isonline(ctx, arg=''):
    if arg == 'aquaHQ':
        await ctx.send(aquaHQ.isLive)
    elif arg == 'test':
        await ctx.send(test.isLive)
    elif arg == 'kaijukingz':
        await ctx.send(kaijukingz.isLive)
    elif arg == 'llama':
        await ctx.send(llama.isLive)
    elif arg == 'degenpass':
        await ctx.send(degenpass.isLive)
    elif arg == 'doodle':
        await ctx.send(doodle.isLive)
    elif arg == 'rcc':
        await ctx.send(rcc.isLive)
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
