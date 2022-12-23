import requests
TOKEN = '5766174948:AAFPOJO7Udzs9sAwjnb67LBjsNmubxIm5rQ'
BASE_URL = f'https://api.telegram.org/bot{TOKEN}/getMe'

response = requests.get(url=BASE_URL)
user = response.json()['result']

print(user['first_name'])

