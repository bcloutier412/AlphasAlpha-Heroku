import time
from servercollection import aquaHQ
from requestsfunc import retrieve_messages, send_message
from discord import Webhook, RequestsWebhookAdapter, Embed
import discord

def aquaHQrun():
    recent_messages = []
    for value in aquaHQ.channelCollection:
        recent_messages.append('')
    try:
        while aquaHQ.isLive:
            counter = 0
            for value in aquaHQ.channelCollection:
                json_obj = retrieve_messages(aquaHQ.activeToken ,value['channel'])
                try:
                    payload_content_0 = json_obj[0]['id']
                except KeyError:
                    print('KeyError 0')

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
        aquaHQ.isLive = False


if __name__ == '__main__':
    aquaHQrun()