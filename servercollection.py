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
                # try:
                payload_content_0 = json_obj[0]['id']
                # except KeyError:
                #     print('KeyError 0')

                if payload_content_0 != recent_messages[counter]:
                    # send_message(value['directedChannel'], json_obj[0]['content'], aquaHQ.proxyToken)
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
                counter += 1
            time.sleep(3)
            counter = 0
    except:
        serverObj.isLive = False


# <--------------aquaHQ----------------->
aquaHQ = Server()
aquaHQ.serverName = 'aquaHQ'
aquaHQ.activeToken = 'MjAzMjM3NTAxODMyMjY1NzMw.YfBRyQ.23lIcSEjKWumZlSJ129xKBSfE9g'
aquaHQ.proxyToken = 'ODg0NjU0MDYyODcwNjAxNzM5.YTbocQ.DWod2UZqL50hkuUcC0Hw0P9mSLo'
aquaHQ.channelCollection = [
    {
        #mg-alpha
        'channel': '953866553135353856',
        'directedChannel': 'https://discord.com/api/webhooks/958625760518737980/TwgPBK9rPiX4cIXjPiB2FqjldE1oRd0lkzUfNfqiPoUwGftf2dsUcqxBMNgwga28q2_1',
        'chatChannel': False
    }, 
        #mrprada-alpha
    {
        'channel': '935774469740429352',
        'directedChannel': 'https://discord.com/api/webhooks/958625635364925470/-e_nzkm1JKEYCIsnAWY9SfhEW4GYZYFg3IcYaZCyu7gCH-U76nHnsEx5fUwsSg7AuB-A',
        'chatChannel': False
    },
        #friazzin-alpha
    {
        'channel': '955831993667584070',
        'directedChannel': 'https://discord.com/api/webhooks/958625987099263016/U9S8wfcvqH3E9jJ4tbBPcmEBfpe86zljmah4mmtHAkUXYXESWTtporm56sUvOnzMMVpN',
        'chatChannel': False
    },
        #alpha chat
    {
        'channel': '935772422517448725',
        'directedChannel': 'https://discord.com/api/webhooks/958015368142671983/YYstRSYcSVV4D5UT10zBA6uSVqVNevdFpzQH3U10awDOChPoiXCoAqQ1VJBqGulrzPpR',
        'chatChannel': True
    }
]





# <--------------Yuck Pass----------------->
yuckPass = Server()
yuckPass.serverName = 'yuckPass'
yuckPass.activeToken = 'MjAzMjM3NTAxODMyMjY1NzMw.YfBRyQ.23lIcSEjKWumZlSJ129xKBSfE9g'
yuckPass.proxyToken = 'OTM2NTI2NjIyMjk3ODQ1Nzcy.YfOe0w._gnjg1tHO3bTrF-nHo8TjPTcfEI'
yuckPass.channelCollection = [
    {
        'channel': '951616970665635910',
        'directedChannel': 'https://discord.com/api/webhooks/958637998445056080/KzyVI5VsmKY9Q1SGvFYsO3nUIzU3NBsU2b8jrAQoYVKPWIJYJAmNWks8DAIQUCK063CG',
        'chatChannel': False
    },
    {
        'channel': '953375551219974165',
        'directedChannel': 'https://discord.com/api/webhooks/958638146633994290/qZCkv8TWnDCptJz4Qa8wnEiap6-2Ccfo6an2vvREUldXXBUBbUEsW_3lq6Q1CjjodxoB',
        'chatChannel': False
    },
    {
        'channel': '928843551855489136',
        'directedChannel': 'https://discord.com/api/webhooks/958638267203469332/aaaB7_D2mH4Nch-lW-f_aycvD5UCkBpV1c3UGed2P1m2r6TPlzgjWrFCEVJ-ar17FVVz',
        'chatChannel': True
    }
]


# <--------------------Test----------------------->
test = Server()
test.serverName = 'test'
test.activeToken = 'MjAzMjM3NTAxODMyMjY1NzMw.YfBRyQ.23lIcSEjKWumZlSJ129xKBSfE9g'
test.proxyToken = 'MjAzMjM3NTAxODMyMjY1NzMw.YfBRyQ.23lIcSEjKWumZlSJ129xKBSfE9g'
test.channelCollection = [
    {
        'channel': '951432248798887936',
        'directedChannel': '956824883319414794',
        'chatChannel': True
    }
]


# <--------------------Alpha Oni----------------------->
oni = Server()
oni.serverName = 'Alpha Oni'
oni.activeToken = 'MjAzMjM3NTAxODMyMjY1NzMw.YfBRyQ.23lIcSEjKWumZlSJ129xKBSfE9g'
oni.proxyToken = 'OTM2NTMxOTAxNzI3MDE0OTgz.YfOjeA.V5COqMTZ-ql2eFM6FjJ9NIVl4Kk'
oni.channelCollection = [
    {
        'channel': '945551117411053578',
        'directedChannel': '957413862209093644',
        'chatChannel': False
    },
    {   
        'channel': '943990390942470144',
        'directedChannel': '957413902679965757',
        'chatChannel': True 
    },
    {   
        'channel': '952888290489540608',
        'directedChannel': '957414111262675025',
        'chatChannel': False
    },
    {   
        'channel': '944012876396511272',
        'directedChannel': '957414637454884864',
        'chatChannel': False
    },
    {   
        'channel': '944152306897805323',
        'directedChannel': '957414953256644698',
        'chatChannel': False
    }
]

servercollection = [aquaHQ, yuckPass, oni, test]