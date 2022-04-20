# 참고 블로그
# https://novice-engineers.tistory.com/13?category=908185

# https://kauth.kakao.com/oauth/authorize?client_id=sdfd(일부삭제됨)b6fb&redirect_uri=https://www.google.com/&response_type=code&scope=talk_message

import requests

url = 'https://kauth.kakao.com/oauth/token'
rest_api_key = '8ffwef5(일부삭제됨)ewefwefb4b6fb'
redirect_uri = 'https://www.google.com/'
authorize_code = 'dxKEU6u0jtIWwefjy0Kvwdwcw'

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


