# 참고 블로그
# https://kangprog.tistory.com/99?category=793131


# def refreshToken(refresh_token) -> str:
#     REST_API_KEY = "8ff9157a006628fe0bd9ee69a3b4b6fb"
#     REDIRECT_URI = "https://kauth.kakao.com/oauth/token"

#     data = {
#         "grant_type": "refresh_token", # 얘는 단순 String임. "refresh_token"
#         "client_id":f"{REST_API_KEY}",
#         "refresh_token": refresh_token # 여기가 위에서 얻은 refresh_token 값
#     }    
 
#     resp = requests.post(REDIRECT_URI , data=data)
#     new_token = resp.json()

#     return new_token['access_token']

import requests
import json

with open(r"D:\Backup\coordinator-msg\tokens\kakao_code1.json","r") as fp:
    tokens = json.load(fp)

url = 'https://kauth.kakao.com/oauth/token'
rest_api_key = '8ff9157a006628fe0bd9ee69a3b4b6fb'
redirect_uri = 'https://www.google.com/'
refresh_token = tokens["refresh_token"]

data = {
    'grant_type':'refresh_token',
    'client_id':rest_api_key,
    'redirect_uri':redirect_uri,
    'refresh_token': refresh_token,
    }

response = requests.post(url, data=data)
tokens = response.json()
print(tokens)

# json 저장
import json
#1.
with open(r"D:\Backup\coordinator-msg\tokens\kakao_code1.json","w") as fp:
    json.dump(tokens, fp)
