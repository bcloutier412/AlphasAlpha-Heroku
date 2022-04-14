import time
from servercollection import yuckPass
from requestsfunc import retrieve_messages, send_message

recent_messages = []
for value in yuckPass.channelCollection:
    recent_messages.append('')
def yuckPassrun():
    try:
        while yuckPass.isLive:
            counter = 0
            for value in yuckPass.channelCollection:
                json_obj = retrieve_messages(yuckPass.activeToken ,value['channel'])
                try:
                    payload_content_0 = json_obj[0]['id']
                except KeyError:
                    print('KeyError 0')

                if payload_content_0 != recent_messages[counter]:
                    send_message(value['directedChannel'], json_obj[0]['content'], yuckPass.proxyToken)
                    recent_messages[counter] = payload_content_0
                counter += 1
            time.sleep(3)
            counter = 0
    except:
        yuckPass.isLive = False
if __name__ == '__main__':
    yuckPassrun()