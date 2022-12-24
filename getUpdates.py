import requests
TOKEN = '5766174948:AAFPOJO7Udzs9sAwjnb67LBjsNmubxIm5rQ'
BASE_URL = f'https://api.telegram.org/bot{TOKEN}/getUpdates'

response = requests.get(url=BASE_URL)
updates=response.json()['result']
 
for update in updates:
    msg = update['message']['text']
    # print(msg['from'])
    print(msg)
