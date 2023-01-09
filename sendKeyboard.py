
import os 
import requests

TOKEN = os.environ['TOKEN']

def sendMessage(chat_id:str,text:str):
    URL = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    button = [
    {
        'text':'12'
    },
    {
        'text':'21'
    },
    {
        'text':'Home'
    }
    ]
    keyboard =  [[button[0]],[button[0]]]
    reply_markup = {
        'keyboard':keyboard
    }

    payload = {
        'chat_id':chat_id,
        'text':'Salom',
        'reply_markup':reply_markup
    }
    r = requests.get(url=URL,json=payload)

chat_id ='996172963'

sendMessage(chat_id=chat_id,text='Salom')

