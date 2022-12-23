import requests
TOKEN = '5355192064:AAEbylzYMrRsWJCqufKA6H2leOWhH3kIcdg'
BASE_URL = f'https://api.telegram.org/bot{TOKEN}/getUpdates'

response = requests.get(url=BASE_URL)
updates=response.json()['result']
 
for update in updates:
    msg = update['message']
    # print(msg['from'])
    print(msg['text'])
