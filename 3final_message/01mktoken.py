# 참고 블로그
# https://novice-engineers.tistory.com/13?category=908185

# https://kauth.kakao.com/oauth/authorize?client_id=8ff9157a006628fe0bd9ee69a3b4b6fb&redirect_uri=https://www.google.com/&response_type=code&scope=talk_message,friends

import requests

url = 'https://kauth.kakao.com/oauth/token'
rest_api_key = '8ff9153b4b6fb'
redirect_uri = 'https://www.google.com/'
authorize_code = 'dxKwdwcw'

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
with open(r"D:\Backup\coordinator-msg\2group_message\kakao_code1.json","w") as fp:
    json.dump(tokens, fp)

