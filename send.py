import requests
from decouple import config
# .env 파일도 .gitignore에 추가해주기
# key값을 외부로 노출시켰기 때문에 github에 push해도 노출되지 않음

base = 'http://api.telegram.org'
token = config('TELEGRAM_BOT_TOKEN')
chat_id = config('CHAT_ID')
text = '안녕'

url = f'{base}/bot{token}/sendMessage?chat_id={chat_id}&text={text}'
send_message = requests.get(url)

print(send_message)