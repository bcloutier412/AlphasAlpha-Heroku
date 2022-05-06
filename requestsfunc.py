import requests
import json
def retrieve_messages(activeToken, channelid):
    headers = {
        'authorization': activeToken
    }
    r = requests.get(f'https://discord.com/api/v9/channels/{channelid}/messages', headers=headers)
    json_obj = json.loads(r.text)
    print(r.status_code)
    return json_obj

def send_message(channelid, message, proxyToken):
    url = f'https://discord.com/api/v9/channels/{channelid}/messages'
    data = {"content": message}
    header = {"authorization": proxyToken}

    r = requests.post(url, data=data, headers=header)
    print(r.status_code)