import apprise
import os

def send_push(title, message):
    apobj = apprise.Apprise()
    apuri = os.environ['APPRISE_URI']
    apobj.add(apuri)
    try:
        apobj.notify(body=message,title=title,)
    except Exception(e):
        print(e)
