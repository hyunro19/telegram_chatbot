from flask import Flask, render_template, request
from decouple import config
import requests
app = Flask(__name__)

base = 'http://api.telegram.org'
token = config('TELEGRAM_BOT_TOKEN')
chat_id = config('CHAT_ID')
naver_client_id = config('NAVER_CLIENT_ID')
naver_client_secret = config('NAVER_CLIENT_SECRET')

@app.route('/')
def hello_world():
    return 'Hello, World!'

# 127.0.0.1:5000/write 에서 127.0.0.1:5000/send?message=메세지 호출
@app.route('/write')
def write():
    return render_template('write.html')

@app.route('/send')
def send():
    text = request.args.get('message')
    requests.get(f'{base}/bot{token}/sendMessage?chat_id={chat_id}&text={text}')
    return render_template('send.html')


#경로값을 이렇게 해주면 post로 들어오는 요청을 받는 건가?
#telegram에 https://api.telegram.org/bot953897380:AAHpVa1TXM_VPXdvuHCU7q9slmHWgECIrro/
#윗줄에 연결해서 setWebhook?url=https://149c31cd.ngrok.io/953897380:AAHpVa1TXM_VPXdvuHCU7q9slmHWgECIrro
#위 경로로 webhook을 걸어줌, telegram으로 요청이 왔을때, 외부 서버로 걔를 다시 보내줌.
@app.route(f'/{token}', methods=['POST'])
def telegram():
    # print(request.get_json())
    from_telegram = request.get_json()
    if from_telegram.get('message') is not None: # None이 아닐 때 만 실행되는 내용
        chat_id = from_telegram.get('message').get('from').get('id')
        text = from_telegram.get('message').get('text')
        
        if text[0:4] == '/번역 ': #input text의 index 0~3이 /번역 이면
            headers = {
                'X-Naver-Client-Id': naver_client_id, 
                'X-Naver-Client-Secret': naver_client_secret
                }
            data = {'source':'ko', 'target':'en', 'text':text[4:]}
            papago_res = requests.post('https://openapi.naver.com/v1/papago/n2mt', headers=headers, data=data) #API에 보내고 리턴 값이 papago_res에 담김
            text = papago_res.json().get('message').get('result').get('translatedText') #리턴된 json dictionary에서 translatedText 추출
        
        if text[0:6] == '/tran ': #input text의 index 0~3이 /번역 이면
            headers = {
                'X-Naver-Client-Id': naver_client_id, 
                'X-Naver-Client-Secret': naver_client_secret
                }
            data = {'source':'en', 'target':'ko', 'text':text[6:]}
            papago_res = requests.post('https://openapi.naver.com/v1/papago/n2mt', headers=headers, data=data) #API에 보내고 리턴 값이 papago_res에 담김
            #requests.post()함수를 실행해 return값을 papago_res에 담는다.
            text = papago_res.json().get('message').get('result').get('translatedText')
            #리턴된 json dictionary에서 translatedText 추출

        if text[0:4] == '/로또 ':             
            num = text[4:]
            res = requests.get(f'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={num}')
            lotto = res.json()

            winner = []
            for i in range(1, 7):
                winner.append(lotto[f'drwtNo{i}'])
                bonus_num = lotto['bnusNo']
                text = f'{num}회차 로또 당첨번호는 {winner}입니다. 보너스 번호는 {bonus_num}입니다.'
        url = f'{base}/bot{token}/sendMessage?chat_id={chat_id}&text={text}'
        requests.get(url)


    return '', 200

# when error and updated, automatic reloading
if __name__ == "__main__":
    app.run(debug=True)