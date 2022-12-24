import requests
def sendMssage(chat_id,text):
    TOKEN = '5766174948:AAFPOJO7Udzs9sAwjnb67LBjsNmubxIm5rQ'
    BASE_URL = f'https://api.telegram.org/bot{TOKEN}/sendMessage'

    param = {
        'chat_id':chat_id,
        'text':text
    }

    data = requests.get(BASE_URL, param)
    return data.json()

print(sendMssage(996172963,'Salom'))

