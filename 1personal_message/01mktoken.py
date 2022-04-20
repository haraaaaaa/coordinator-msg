# https://kauth.kakao.com/oauth/authorize?client_id=8ff9157a006628fe0bd9ee69a3b4b6fb&redirect_uri=https://www.google.com/&response_type=code&scope=talk_message

import requests

url = 'https://kauth.kakao.com/oauth/token'
rest_api_key = '8ff9157a006628fe0bd9ee69a3b4b6fb'
redirect_uri = 'https://www.google.com/'
authorize_code = 'hrmTq95yYZXYw6zZYYipOtC8-h3bMxC2jnbhnTDMhwo9dJgAAAGARNdxRA'

data = {
    'grant_type':'authorization_code',
    'client_id':rest_api_key,
    'redirect_uri':redirect_uri,
    'code': authorize_code,
    }

response = requests.post(url, data=data)
tokens = response.json()
print(tokens)

# json 저장
import json
#1.
with open(r"D:\python_workspace\kakao\kakao_code.json","w") as fp:
    json.dump(tokens, fp)
