import os 
import requests

TOKEN = os.environ['TOKEN']

def sendPhoto(chat_id:str,photo:str):
    URL = f'https://api.telegram.org/bot{TOKEN}/sendPhoto'
    param = {
        'chat_id':chat_id,
        'photo':photo
    }
    files = {
        'photo':photo
    }
    # r = requests.post(url=URL,params=param,files=files)
    r = requests.get(url=URL,params=param)
    print(r.json())


chat_id ='996172963'

photo_url='https://random.dog/15038-13875-14202.jpg'
photo_id = 'AgACAgIAAxkBAAMnY7ezjNMhfqkXJVOM8XxpgB8LoSEAAu3BMRvK3LlJTc69b5lsz8EBAAMCAAN5AAMtBA'

img = open('logo.jpg','rb').read()

sendPhoto(chat_id=chat_id,photo=photo_id)