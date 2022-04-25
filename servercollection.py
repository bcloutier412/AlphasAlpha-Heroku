import json
import time
from tkinter import E
from requestsfunc import retrieve_messages, send_message
from discord import Webhook, RequestsWebhookAdapter, Embed
import discord
import threading
import time
import logging
logging.basicConfig(filename='myapp.log', level=logging.DEBUG, 
                    format='%(asctime)s %(levelname)s %(name)s %(message)s')
logger=logging.getLogger(__name__)

delayedMessageCollection = []
delayedMessageBot = False
class Server():
    # activeToken is the user that is in the server we are scrapping from
    # proxyToken 
    def __init__(self):
        self.serverName = ''
        self.activeToken = ''
        self.proxyToken = ''
        self.channelCollection = []
        self.isLive = False
        self.initialactivation = False

def serverRun(serverObj):
    global  delayedMessageCollection
    try:
        while serverObj.isLive:
            recent_messages = []
            for value in serverObj.channelCollection:
                recent_messages.append('')
            # try:
            while serverObj.isLive:
                counter = 0
                for value in serverObj.channelCollection:
                    try:
                        json_obj = retrieve_messages(serverObj.activeToken ,value['channel'])
                    except Exception as err:
                        logger.error(serverObj.serverName)
                        logger.error(err)
                    # print(json_obj)
                    payload_content_0 = json_obj[0]['id']
                        # logger.error(err)
                    if payload_content_0 != recent_messages[counter]:
                        embedsList = []
                        if  json_obj[0]['content'] != '':
                            embed = discord.Embed(title=json_obj[0]['author']['username'],description=json_obj[0]['content'])
                            embedsList.append(embed)
                        try:
                            if json_obj[0]['embeds'] != []:
                                for count, embed in enumerate(json_obj[0]['embeds']):
                                    embed = discord.Embed(title=json_obj[0]['author']['username'], description=json_obj[0]['embeds'][count]['description'])
                                    embedsList.append(embed)
                        except Exception as err:
                            logger.error(serverObj.serverName)
                            logger.error(err)
                        if json_obj[0]['attachments'] != []:
                            embed = discord.Embed(title=json_obj[0]['author']['username'])
                            for count, embed in enumerate(json_obj[0]['attachments']):
                                embed = discord.Embed(title=json_obj[0]['author']['username'])
                                url = json_obj[0]['attachments'][0]['url']
                                embed.set_image(url=url)
                                embedsList.append(embed)
                        if embedsList != []:
                            webhook = Webhook.from_url(value['directedChannel'], adapter=RequestsWebhookAdapter())
                            webhook.send(embeds=embedsList)
                            timestamp = time.time()
                            listitem = [embedsList, value['directedChannel'], value['delayedWebhook'],timestamp]
                            delayedMessageCollection.append(listitem)
                        recent_messages[counter] = payload_content_0
                    counter += 1
                
                # print(serverObj.serverName + 'working')
                time.sleep(3)
                counter = 0
            # except:
            #     # serverObj.isLive = False
            #     pass
    except Exception as err:
        logger.error(serverObj.serverName)
        logger.error(err)
def sendEmbed():
    send_message(956827879591784518, '<----------------------->', "mfa.AqRZyU3IFfWjHsEtDBohbv28PbFsv1lWnOhavoGEddRd1ixdxCvbK2BdqeFfZSVdQgjbJUgWJw0qG8vjrPbo")
    # https://discord.com/api/webhooks/967010755931164692/0H94eZa6keDdxk4XN5IOPf-5k5rCaJvJVo1ln-p5xfN8w9QYylqeG0QOujf6aGuS7GU8
    webhook = Webhook.from_url("https://discord.com/api/webhooks/967010755931164692/0H94eZa6keDdxk4XN5IOPf-5k5rCaJvJVo1ln-p5xfN8w9QYylqeG0QOujf6aGuS7GU8", adapter=RequestsWebhookAdapter())
    embed = discord.Embed(title='Dino', description='first embed')
    embed2 = discord.Embed(title='yert', description='second embed')
    embeds = [embed, embed2]
    webhook.send(embeds=embeds)

def parseSendMessageCollection():
    global delayedMessageBot
    global delayedMessageCollection
    while True:
        # try:
        for count, message in enumerate(delayedMessageCollection):
            if  time.time() - delayedMessageCollection[count][3]> 600:
                webhook = Webhook.from_url(delayedMessageCollection[count][2], adapter=RequestsWebhookAdapter())
                webhook.send(embeds=delayedMessageCollection[count][0])
                delayedMessageCollection.remove(message)
        time.sleep(1)
        # except KeyError:
        #     pass
# <--------------aquaHQ----------------->
aquaHQ = Server()
aquaHQ.serverName = 'aquaHQ'
aquaHQ.activeToken = "mfa.AqRZyU3IFfWjHsEtDBohbv28PbFsv1lWnOhavoGEddRd1ixdxCvbK2BdqeFfZSVdQgjbJUgWJw0qG8vjrPbo"
aquaHQ.proxyToken = 'ODg0NjU0MDYyODcwNjAxNzM5.YTbocQ.DWod2UZqL50hkuUcC0Hw0P9mSLo'
aquaHQ.channelCollection = [
    {
        #prada alpha
        'channel': '935774469740429352',
        'directedChannel': 'https://discord.com/api/webhooks/965507961164292096/coAaxF9gt03najAmqprVx5I51U2SqJpB7TpR_71EcFL1FWp5Ukq_hF7D2DGLE-S4WWJD',
        'chatChannel': False,
        'delayedWebhook': 'https://discord.com/api/webhooks/967364563047694356/fcsW79fpzq2m_5y5Y9j6WJlal-Mu9qycyJYVJZ_x405LriL2lY2OETFERZMJdftNvV9y'
    },
    {
        #mg-alpha
        'channel': '953866553135353856',
        'directedChannel': 'https://discord.com/api/webhooks/965508048875561011/RfdPSaWiVjwd07B6eYmmoHsZBOxOHWLxO0oa6imMSUBz9szvwGO7udjfGxG0ixgr1ILH',
        'chatChannel': False,
        'delayedWebhook': 'https://discord.com/api/webhooks/967390301545177139/AqbYeb7urfBEl7asW2u7toct2QkT5FrbAVtNAMTIMCeuvz1v75kVRcWbId6Zy42R0iqn'
    }, 
    {
        #chriss-alpha
        'channel': '958179025698844703',
        'directedChannel': 'https://discord.com/api/webhooks/965508108262719488/KeKGkrQkM1_tShhwAN4G7nGMpuJLVmm7D41czPcruxXXCZgu8s1CRX8HCp-xcqWw160D',
        'chatChannel': False,
        'delayedWebhook': 'https://discord.com/api/webhooks/967391291107323994/zDFIunT7sXAy68FIANIxZLjiUklm4Ted5fkvyNiAP1TjR5ISzFj3ztT3iWc6ZyQGPCnW'

    },
        #friazzin-alpha
    {
        'channel': '955831993667584070',
        'directedChannel': 'https://discord.com/api/webhooks/965508214055637052/8M4xVbMJgM81NG5W04EH3R171QAZx4fgrecBajOhw2YOiffzAoBSkcjyyENRJAiBWJ8h',
        'chatChannel': False,
        'delayedWebhook': 'https://discord.com/api/webhooks/967391566580809729/DoW6N48ZU1SHlQKZdVIb3W_4oKBl4JOnuwb8KLOnk3J853vJeAdcmFBoe1N0dz1jnygD'
    },
    {
        #miz-alpha
        'channel': '964304266762280960',
        'directedChannel': 'https://discord.com/api/webhooks/965508313871691796/9c0UKbZTcBdmvBct7gQIn2Ok2Nyee_Z77o_V3eOUIFi2js-Z036SX6s5ulbq6kV36T5c',
        'chatChannel': False,
        'delayedWebhook': 'https://discord.com/api/webhooks/967391816204820530/3C5RLt6CHkrTLfCJeVkdc48doeuGP8xXVknMHl9pGSSwWW9RKsWdjEIxPeI1XWYJy5Zl'
    },
        #community alpha 
    {
        'channel' : '958046386711044168',
        'directedChannel': 'https://discord.com/api/webhooks/965508433715527710/mSPx5zp02pHlh6286YUX0zdhqkyeAQa3z7IoPqSj5pRCwgi2vBUXEEI4dSIQ-mIaqbV6',
        'chatChannel': False,
        'delayedWebhook': 'https://discord.com/api/webhooks/967392076872450071/56tOY63mjI78jxIqqKCcFKkTXwk-IsDx4drevU5XqoI-v452QpBOvH6iLQH3Ev6Z02aP'
    },
        #alpha chat
    {
        'channel': '935772422517448725',
        'directedChannel': 'https://discord.com/api/webhooks/965508551856496690/Bf80kw4LUcE7b5TZ-ENS9X7NeaJlRQGGcj68gSRw8AuZibLc-fXAsW3tAe9kiepQhcA-',
        'chatChannel': True,
        'delayedWebhook': 'https://discord.com/api/webhooks/967364563047694356/fcsW79fpzq2m_5y5Y9j6WJlal-Mu9qycyJYVJZ_x405LriL2lY2OETFERZMJdftNvV9y'
    },
]


# <--------------------Test----------------------->
test = Server()
test.serverName = 'test'
test.activeToken = "mfa.AqRZyU3IFfWjHsEtDBohbv28PbFsv1lWnOhavoGEddRd1ixdxCvbK2BdqeFfZSVdQgjbJUgWJw0qG8vjrPbo"
test.proxyToken = 'MjAzMjM3NTAxODMyMjY1NzMw.YfBRyQ.23lIcSEjKWumZlSJ129xKBSfE9g'
test.channelCollection = [
    {
        'channel': '956824883319414794',
        'directedChannel': 'https://discord.com/api/webhooks/967025388838608926/rBQ8HZgZI7kAEytqmE48taa0xgemP2fQwp7YAZtzDYylry7UscAOCMxmfLdkTcxklrPH',
        'chatChannel': True
    }
]

kaijukingz = Server()
kaijukingz.serverName = 'Kaiju Kingz'
kaijukingz.activeToken = "mfa.AqRZyU3IFfWjHsEtDBohbv28PbFsv1lWnOhavoGEddRd1ixdxCvbK2BdqeFfZSVdQgjbJUgWJw0qG8vjrPbo"
kaijukingz.proxyToken = 'MjAzMjM3NTAxODMyMjY1NzMw.YfBRyQ.23lIcSEjKWumZlSJ129xKBSfE9g'
kaijukingz.channelCollection = [
    {
        'channel': '904260227812192267',
        'directedChannel': 'https://discord.com/api/webhooks/965505617374634025/slXFX_R-vlZkdTEB2YxG-cS-joV52bjpiqVZ-s8x75ZSO4-4M-HS-YJX50p3CIGvPYkl',
        'chatChannel': True,
        'delayedWebhook': 'https://discord.com/api/webhooks/967369510954885161/bk6UUKvzwrlzQ-V85p1w2rfDyDDUvymWNE59G-RbAXAhQnvWrPSVW8pqHi5twZCpPa5t'
    }
]

llama = Server()
llama.serverName = 'llamaverse'
llama.activeToken = "mfa.AqRZyU3IFfWjHsEtDBohbv28PbFsv1lWnOhavoGEddRd1ixdxCvbK2BdqeFfZSVdQgjbJUgWJw0qG8vjrPbo"
llama.proxyToken = 'MjAzMjM3NTAxODMyMjY1NzMw.YfBRyQ.23lIcSEjKWumZlSJ129xKBSfE9g'
llama.channelCollection = [
    {
        #llama calls
        'channel': '956781876733952021',
        'directedChannel': 'https://discord.com/api/webhooks/965509893933117450/qehcCwFcU3TWgCeILX-8QwUijXWDdEf3ijsFerO-D7_t8w6u9-Xu8mrXb52OrSvhdkmh',
        'chatChannel': True,
        'delayedWebhook': 'https://discord.com/api/webhooks/967393264032419890/CensluCdxpEhla24uUh4l1H2FzHh4YmeWzqYqAZiwNc48yhCWOhQuJst9H2_dYf50cAc'
    },
    {
        #llama upcoming
        'channel': '956782102031003698',
        'directedChannel': 'https://discord.com/api/webhooks/965510074321752085/VByYNrhV9k1IuGR2utJT-p27HyOHyBZ9DyfGXRc0wQVyhHnFYzSXbTETBjhb8wVkOOBd',
        'chatChannel': True,
        'delayedWebhook': 'https://discord.com/api/webhooks/967393645890256896/BARxGh1FGuISnCNi9iPvf-Z3jbOx-oS1P9jbivXUZ5xIAczJ3RbQAlATXcytDRYSebo5'
    }
]

degenpass = Server()
degenpass.serverName = 'degenpass'
degenpass.activeToken = "mfa.AqRZyU3IFfWjHsEtDBohbv28PbFsv1lWnOhavoGEddRd1ixdxCvbK2BdqeFfZSVdQgjbJUgWJw0qG8vjrPbo"
degenpass.proxyToken = 'MjAzMjM3NTAxODMyMjY1NzMw.YfBRyQ.23lIcSEjKWumZlSJ129xKBSfE9g'
degenpass.channelCollection = [
    {
        'channel': '958549427574939658',
        'directedChannel': 'https://discord.com/api/webhooks/965511342486335539/973DofSOxdeKC2_R0K26PLcvyZWtfpKYOCsmX-k80XTKE32awxM8HLYdto9L-keXmE3o',
        'chatChannel': True,
        'delayedWebhook': 'https://discord.com/api/webhooks/967393951327866891/0SmFq6vEC8qe-mMkQXUENBqvESADJuROJwNakYJ-ziXXT1XJ3gJ61i5vMSNJASQFhjGD'
    }
]
doodle = Server()
doodle.serverName = 'doodle'
doodle.activeToken = 'MTUwNTA2NzkwOTY1MDg0MTYw.Yl0Rvw.0THUAtreVOa3fmE4suweXLp4ajE'
doodle.proxyToken = 'MjAzMjM3NTAxODMyMjY1NzMw.YfBRyQ.23lIcSEjKWumZlSJ129xKBSfE9g'
doodle.channelCollection = [
    {
        'channel': '958882835442335765',
        'directedChannel': 'https://discord.com/api/webhooks/965514751536922634/emTOjdkM94lErJkG2kd66B1Tamcczg0jSFm3xSAMyH39LTmBlsrF2Wl-SlqUpLLudD0T',
        'chatChannel': True,
        'delayedWebhook': 'https://discord.com/api/webhooks/967394244174155856/XwTIiZqqRFEUZXgRISKImmzHkW7i81RSjFsQM4RP8qCOzYHa6ls-CPrmWFdO3t8bPr51'
    }
]
rcc = Server()
rcc.serverName = 'rcc'
rcc.activeToken = 'mfa.BGgsz4fbXzWfltPyH8_qWlAL3lcx3YeAEOKjSQmp30hagHWSyp40CdrbtU_UadnI26tl8nAVhTHXIl9Jpf52'
rcc.proxyToken = 'MjAzMjM3NTAxODMyMjY1NzMw.YfBRyQ.23lIcSEjKWumZlSJ129xKBSfE9g'
rcc.channelCollection = [
    {
        'channel': '961256795962232922',
        'directedChannel': 'https://discord.com/api/webhooks/965517223546462219/L1umlE9vXCwzE10ipLqtuUQq3khTSQwHbeNwIiuT_waGst40pWCwVEFRvtUmZ3f3mG1A',
        'chatChannel': True,
        'delayedWebhook': 'https://discord.com/api/webhooks/967394444057911307/Cy9i_XngwnzhxqxqmeZdjj4vFQuuLgoNaasehl5PjJrUD7xebaQTh0KGh8pH5tTjF7MO'
    }
]
servercollection = [aquaHQ, test, kaijukingz, llama, degenpass, doodle, rcc]