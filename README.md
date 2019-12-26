# 텔레그램 번역 챗봇

파이썬, 플라스크, 텔레그램, 파파고를 활용한



[Github에서 보기](https://github.com/hyunro19/telegram_chatbot)

[GithubPage에서 보기](hyunro19.githubpage.io)

[Notion에서 보기](https://www.notion.so/TRANSLATING_CHATBOT-feat-Python-Flask-Telegram-Papago-82cbb7b48acb4c2791c07208e1286dd4)





### 목차

1. 애플리케이션 기능 스펙
2. 사용 방법 (*텔레그램 `my9102_bot` 검색)*
3. 개발환경 및 사용 기술
4. Flask 개발 환경 구축
5. 텔레그램 챗봇 API
6. 파파고 번역 API
7. 소스코드
8. 배포 (Python Anywhere)









---

### 1. 애플리케이션 기능 스펙 (한영 · 영한 번역)

![TRANSLATING_CHATBOT%20feat%20Python%20Flask%20Telegram%20Pap/Screenshot_20191222-161057_Telegram.jpg](https://www.notion.so/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2Fbc557db0-1e6e-491c-8b49-aee0603e77ea%2FScreenshot_20191222-161057_Telegram.jpg?table=block&id=baf93b46-86e4-4455-87ef-37f8a06fec98&width=580&cache=v2)

* 실제 구동 화면

 

- 한영 번역 : `/번역` 뒤에 오는 메세지

`>> `  /번역 오늘 점심은 뭐먹지?`

`>>`  `What are we going to have for lunch?`

- 영한 번역 : `/tran` 뒤에 오는 메세지

`<<`  `/tran Where are we gonna travel this winter?`

`>>`  `이번 겨울에는 어디로 여행을 갈까?`











---

### 2. 사용방법

텔레그램에서 `my9102_bot` 검색

![TRANSLATING_CHATBOT%20feat%20Python%20Flask%20Telegram%20Pap/chatbot_howtouse.png](https://www.notion.so/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F09da39b7-a076-4e27-96fb-179bcffbcfc8%2Fchatbot_howtouse.png?table=block&id=cb619483-ad07-4919-a8d2-a55eab17b940&width=1820&cache=v2)











---

### 3. 개발환경 및 사용 기술

1. Python Language (v3.8)
2. Flask Framework
3. Telegram Chatbot API
4. Naver Papago API
5. PythonAnywhere CloudWebServer
6. VSCode (Win x64)









---

### 4. Flask 개발 환경 구축

1. Flask 설치 및 작동 테스트
2. VENV 가상 환경 설정
* 가상환경 사용 이유 : 프로젝트별로 패키지 사용시 충돌 → 프로젝트별 패키지 별도 관리
3. `.env`  외부 환경변수 파일 설정 *(Telegram, Papago API KEY 보안용)*

        #.env 환경변수 파일
        # Telegram API KEY
        TELEGRAM_BOT_TOKEN='THIS_IS_MY_TOKEN'
        CHAT_ID='*THIS_IS_MY_CHAT_ID'*
        # Papago API KEY
        NAVER_CLIENT_ID='ID_CODE_FROM_DEVELOPERS_PAGE'
        NAVER_CLIENT_SECRET='SECRET_CODE_FROM_DEVELOPERS_PAGE'
    
    
    ​    
    ​    #app.py 내에서 호출
    ​    from decouple import config ##외부 환경변수 호출 라이브러리
    ​    token = config('TELEGRAM_BOT_TOKEN')
    ​    chat_id = config('CHAT_ID')
    ​    naver_client_id = config('NAVER_CLIENT_ID')
    ​    naver_client_secret = config('NAVER_CLIENT_SECRET')

---

### 5. 텔레그램 챗봇 API

1. 개인 API KEY(=token) 생성
    텔레그램 BotFather 계정 →`/start` →`/newbot`→ bot_name, user_name 설정

  ```
  BotFather, [13.12.19 10:28]
   Done! Congratulations on your new bot. You will find it at t.me/my9102_bot. 
   You can now add a description, about section and profile picture for your bot, 
   see /help for a list of commands. By the way, when you've finished creating your cool bot, 
   ping our Bot Support if you want a better username for it. 
   Just make sure the bot is fully operational before you do this.
  
   Use this token to access the HTTP API:
  
   APIKEY_#*&(*&@#%&*SDJK*#*(Y%(**(@#%
  
   Keep your token secure and store it safely, it can be used by anyone to control your bot.
  
   For a description of the Bot API, see this page: https://core.telegram.org/bots/api
  ```

  

2. 봇 정보 확인  [https://api.telegram.org/botAPIKEY/getMe](https://api.telegram.org/botAPIKEY/getMe)

3. 봇에 들어온 요청사항, 수정사항 확인 [https://api.telegram.org/botAPIKEY/getUpdates](https://api.telegram.org/botAPIKEY/getUpdates)

4. Bot → myPhone 메세지 보내기 [https://api.telegram.org/botAPIKEY/sendMessage?chat_id=CHAT_ID,&text=안녕하세요](https://api.telegram.org/botAPPKEY/sendMessage?chat_id=CHAT_ID,&text=%EC%95%88%EB%85%95%ED%95%98%EC%84%B8%EC%9A%94)

![TRANSLATING_CHATBOT%20feat%20Python%20Flask%20Telegram%20Pap.png](https://www.notion.so/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F8ebf9c95-6608-400a-9e58-e3278c1ee5d4%2F.png?table=block&id=d450a519-11e2-4a17-bbd2-07e4f5d0f7f5&width=380&cache=v2)

5. WebhookSet (내 Bot이 받는 메세지를 포워딩 할 서버 설정)

[https://api.telegram.org/botAPIKEY/](https://api.telegram.org/botAPPKEY/)setWebhook?url=https://149c31cd.ngrok.io/APIKEY
 → "Webhook was set" 출력시 설정 완료

6. 봇으로 메세지를 보내기 (send.py)

    ```python
    # send.py (bot으로 메세지 보내기)
    
    import requests
    from decouple import config
    #.env 파일도 .gitignore에 추가해주기
    #key값을 외부로 노출시켰기 때문에 github에 push해도 노출되지 않음
    
    base = 'http://api.telegram.org'
    token = config('TELEGRAM_BOT_TOKEN')
    chat_id = config('CHAT_ID')
    text = '메세지'
    
    url = f'{base}/bot{token}/sendMessage?chat_id={chat_id}&text={text}'
    send_message = requests.get(url)
    
    print(send_message)
    ```









---

 

### 6. 파파고 번역 API

- `.env`  파일에 파파고 API 추가

    ```python
    NAVER_CLIENT_ID='ID_CODE_FROM_DEVELOPERS_PAGE'
    NAVER_CLIENT_SECRET='SECRET_CODE_FROM_DEVELOPERS_PAGE'
    ```









---

 

### 7. 소스코드

- /app.py

```python
from flask import Flask, request
from decouple import config #외부 설정파일 읽어오는 라이브러리
import requests
app = Flask(__name__)

# .env로부터 환경변수를 읽어온다.
base = 'http://api.telegram.org'
token = config('TELEGRAM_BOT_TOKEN')
chat_id = config('CHAT_ID')
naver_client_id = config('NAVER_CLIENT_ID')
naver_client_secret = config('NAVER_CLIENT_SECRET')

# http://hyunro19.pythonanywhere.com/로 접속시 아래 메세지 출력
@app.route('/')
def hello_world():
    return '''HOW TO USE
			텔레그램 'my9102_bot' 검색
			/번역 뒤에 한글을 입력하면 한영 번역
			/tran 뒤에 영어를 입력하면 영한 번역'''

# post로 들어온 요청에 응답하는 함수
@app.route(f'/{token}', methods=['POST'])
def telegram():
    # print(request.get_json())
    from_telegram = request.get_json()
    if from_telegram.get('message') is not None: # None이 아닐 때 만 실행되는 내용
        chat_id = from_telegram.get('message').get('from').get('id')
        text = from_telegram.get('message').get('text')
        
        if text[0:4] == '/번역 ': #input text의 index 0~3이 /번역 이면 한영번역
            headers = {
                'X-Naver-Client-Id': naver_client_id, 
                'X-Naver-Client-Secret': naver_client_secret
                }
            data = {'source':'ko', 'target':'en', 'text':text[4:]}
            papago_res = requests.post('https://openapi.naver.com/v1/papago/n2mt', headers=headers, data=data) 
						# API에 요청을 보내고 리턴 값이 papago_res에 담긴다.
						# == requests.post()함수를 실행해 return값을 papago_res에 담는다.
            text = papago_res.json().get('message').get('result').get('translatedText')
						#리턴된 json에서 translatedText 추출
        
        if text[0:6] == '/tran ': #input text의 index 0~3이 /tran 이면 영한번역
            headers = {
                'X-Naver-Client-Id': naver_client_id, 
                'X-Naver-Client-Secret': naver_client_secret
                }
            data = {'source':'en', 'target':'ko', 'text':text[6:]}
            papago_res = requests.post('https://openapi.naver.com/v1/papago/n2mt', headers=headers, data=data)
            text = papago_res.json().get('message').get('result').get('translatedText')

    return '', 200
```


​    

- /template/write.py

```html
<h1>메세지가 성공적으로 전송되었습니다.</h1>
```



- /template/send.py

```html
<h1>Telegram</h1>

<form action="/send">
    <input type="text" name="message">
    <input type="submit" value="메세지 전송">
</form>
```



​    





---

### 8. 배포 (Python Anywhere)

1. 서버 내 코드 저장 (flask_app.py) 
2. 환경변수 설정

    `pip3 install python-decouple --user`  외부 환경변수 호출 라이브러리 설치
    `.env` 파일 작성

3. 챗봇 WebhookSet 재설정 (BOT이 받는 메세지를 웹서버로 포워딩)

    https://api.telegram.org/botAPIKEY/](https://api.telegram.org/botAPPKEY/)setWebhook?url=https://[hyunro19.pythonanywhere.com](http://hyunro19.pythonanywhere.com/)/APIKEY

    `>>`  `{"ok":true, "result":true, "description":"Webhook was set"}`







