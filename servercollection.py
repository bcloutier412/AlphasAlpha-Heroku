import time
from requestsfunc import retrieve_messages, send_message
from discord import Webhook, RequestsWebhookAdapter, Embed
import discord

class Server():
    # activeToken is the user that is in the server we are scrapping from
    # proxyToken 
    def __init__(self):
        self.serverName = ''
        self.activeToken = ''
        self.proxyToken = ''
        self.channelCollection = []
        self.isLive = False

def serverRun(serverObj):
    recent_messages = []
    for value in serverObj.channelCollection:
        recent_messages.append('')
    try:
        while serverObj.isLive:
            counter = 0
            for value in serverObj.channelCollection:
                json_obj = retrieve_messages(serverObj.activeToken ,value['channel'])
                # print(json_obj)
                try:
                    payload_content_0 = json_obj[0]['id']
                except KeyError:
                    print('KeyError 0')

                if payload_content_0 != recent_messages[counter]:
                        try:
                            if json_obj[0]['embeds'] != []:
                                webhook = Webhook.from_url(value['directedChannel'], adapter=RequestsWebhookAdapter())
                                embed = discord.Embed(title=json_obj[0]['author']['username'], description=json_obj[0]['embeds'][0]['description'])
                                webhook.send(embed=embed)
                                    # send_message(value['directedChannel'], json_obj[0]['content'], aquaHQ.proxyToken)
                            else:
                                webhook = Webhook.from_url(value['directedChannel'], adapter=RequestsWebhookAdapter())
                                embed = discord.Embed(title=json_obj[0]['author']['username'], description=json_obj[0]['content'])
                                url = ''
                                try:
                                    url = json_obj[0]['attachments'][0]['url']
                                except:
                                    pass
                                embed.set_image(url=url)
                                webhook.send(embed=embed)
                                    # send_message(value['directedChannel'], json_obj[0]['content'], aquaHQ.proxyToken)
                            recent_messages[counter] = payload_content_0
                        except KeyError:
                            print('KeyError 0')
                            pass
                counter += 1
                # print(counter)
            print(serverObj.serverName + 'working')
            time.sleep(3)
            counter = 0
    except:
        serverObj.isLive = False


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
        'chatChannel': False
    },
    {
        #mg-alpha
        'channel': '953866553135353856',
        'directedChannel': 'https://discord.com/api/webhooks/965508048875561011/RfdPSaWiVjwd07B6eYmmoHsZBOxOHWLxO0oa6imMSUBz9szvwGO7udjfGxG0ixgr1ILH',
        'chatChannel': False
    }, 
    {
        #chriss-alpha
        'channel': '958179025698844703',
        'directedChannel': 'https://discord.com/api/webhooks/965508108262719488/KeKGkrQkM1_tShhwAN4G7nGMpuJLVmm7D41czPcruxXXCZgu8s1CRX8HCp-xcqWw160D',
        'chatChannel': False

    },
        #friazzin-alpha
    {
        'channel': '955831993667584070',
        'directedChannel': 'https://discord.com/api/webhooks/965508214055637052/8M4xVbMJgM81NG5W04EH3R171QAZx4fgrecBajOhw2YOiffzAoBSkcjyyENRJAiBWJ8h',
        'chatChannel': False
    },
    {
        #miz-alpha
        'channel': '964304266762280960',
        'directedChannel': 'https://discord.com/api/webhooks/965508313871691796/9c0UKbZTcBdmvBct7gQIn2Ok2Nyee_Z77o_V3eOUIFi2js-Z036SX6s5ulbq6kV36T5c',
        'chatChannel': False
    },
        #community alpha 
    {
        'channel' : '958046386711044168',
        'directedChannel': 'https://discord.com/api/webhooks/965508433715527710/mSPx5zp02pHlh6286YUX0zdhqkyeAQa3z7IoPqSj5pRCwgi2vBUXEEI4dSIQ-mIaqbV6',
        'chatChannel': False

    },
        #alpha chat
    {
        'channel': '935772422517448725',
        'directedChannel': 'https://discord.com/api/webhooks/965508551856496690/Bf80kw4LUcE7b5TZ-ENS9X7NeaJlRQGGcj68gSRw8AuZibLc-fXAsW3tAe9kiepQhcA-',
        'chatChannel': True
    },
]


# <--------------------Test----------------------->
test = Server()
test.serverName = 'test'
test.activeToken = "mfa.AqRZyU3IFfWjHsEtDBohbv28PbFsv1lWnOhavoGEddRd1ixdxCvbK2BdqeFfZSVdQgjbJUgWJw0qG8vjrPbo"
test.proxyToken = 'MjAzMjM3NTAxODMyMjY1NzMw.YfBRyQ.23lIcSEjKWumZlSJ129xKBSfE9g'
test.channelCollection = [
    {
        'channel': '951432248798887936',
        'directedChannel': '956824883319414794',
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
        'chatChannel': True
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
        'chatChannel': True
    },
    {
        #llama upcoming
        'channel': '956782102031003698',
        'directedChannel': 'https://discord.com/api/webhooks/965510074321752085/VByYNrhV9k1IuGR2utJT-p27HyOHyBZ9DyfGXRc0wQVyhHnFYzSXbTETBjhb8wVkOOBd',
        'chatChannel': True
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
        'chatChannel': True
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
        'chatChannel': True
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
        'chatChannel': True
    }
]
servercollection = [aquaHQ, test, kaijukingz, llama, degenpass, doodle, rcc]