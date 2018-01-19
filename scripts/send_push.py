import prowlpy
import os

def send_push(title, message):
    apikey = os.environ['PROWL_API']
    p = prowlpy.Prowl(apikey)
    try:
        p.add('apcupsd',title,message, 1, None, None)
    except Exception,msg:
        print msg
