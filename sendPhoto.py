import os 
import requests

TOKEN = os.environ['TOKEN']

def sendPhoto(chat_id:str,photo:str):
    URL = f'https://api.telegram.org/bot{TOKEN}/sendPhoto'
    param = {
        'chat_id':chat_id
        # 'photo':photo
    }
    files = {
        'photo':photo
    }
    r = requests.post(url=URL,params=param,files=files)
    print(r.json())


chat_id ='5575549228'

photo_url='https://random.dog/2bff25d0-c721-4078-8cc9-f3ce6b464428.jpg'
photo_id = 'AgACAgIAAxkDAAMgY7evYvSyDJQ8DS-1S5Irjcd9cIgAAoa_MRvjDsFJ4H7lvD-PEXwBAAMCAAN4AAMtBA'

img = open('logo.jpg','rb').read()

sendPhoto(chat_id=chat_id,photo=img)