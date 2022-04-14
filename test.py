from json import JSONEncoder
import json
import time
from servercollection import test
from requestsfunc import retrieve_messages, send_message
from discord import Webhook, RequestsWebhookAdapter
import discord

recent_messages = []
for value in test.channelCollection:
    recent_messages.append('')
def testrun():
    try:
        while test.isLive:
            counter = 0
            for value in test.channelCollection:
                json_obj = retrieve_messages(test.activeToken ,value['channel'])
                try:
                    payload_content_0 = json_obj[0]['id']
                except KeyError:
                    print('KeyError 0')

                if payload_content_0 != recent_messages[counter]:
                    print(json_obj)
                    if value['chatChannel']:
                        webhook = Webhook.from_url('https://discord.com/api/webhooks/958015368142671983/YYstRSYcSVV4D5UT10zBA6uSVqVNevdFpzQH3U10awDOChPoiXCoAqQ1VJBqGulrzPpR', adapter=RequestsWebhookAdapter())
                    # embed = discord.Embed(title="Hello World", description=":wave:") # Initializing an Embed
                    # embed.add_field(name="Field name", value="Field value") # Adding a new field
                        embed = discord.Embed(title=json_obj[0]['author']['username'], description=json_obj[0]['content'])
                        url = ''
                        try:
                            url = json_obj[0]['attachments'][0]['url']
                        except:
                            pass
                        embed.set_image(url=url)
                        # webhook.send(username=json_obj[0]['author']['username'], content=json_obj[0]['content'])
                        webhook.send(embed=embed)
                        # print(json_obj)
                    else:
                        send_message(value['directedChannel'], json_obj[0]['content'], test.proxyToken)
                    recent_messages[counter] = payload_content_0
                counter += 1
            time.sleep(3)
            counter = 0
    except:
        test.isLive = False
if __name__ == '__main__':
    testrun()