import requests
def Chat_id():
    TOKEN = '5766174948:AAFPOJO7Udzs9sAwjnb67LBjsNmubxIm5rQ'
    BASE_URL = f'https://api.telegram.org/bot{TOKEN}/getUpdates'

    response = requests.get(url=BASE_URL)
    updates=response.json()['result'][-1]
 
    message = updates['message']

    text = message['text']
    id = message['chat']['id']

    return id, text

def sendMessage():
    TOKEN = '5766174948:AAFPOJO7Udzs9sAwjnb67LBjsNmubxIm5rQ'
    BASE_URL = f'https://api.telegram.org/bot{TOKEN}/sendMessage'

    id, text = Chat_id()
    
    param = {
        'chat_id':id,
        'text':text
    }
    data = requests.get(BASE_URL, param)
    return data.json()

print(sendMessage())

