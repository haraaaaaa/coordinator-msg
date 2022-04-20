# 현재 카카오API 앱 생성자 본인계정만 작동하는것 같습니다
# 타인 카카오계정으로 로그인하고 메세지받기는 진행중(220420,김종진)

# 아래 링크에 지라에 업로드된 REST API KEY를 입력하고 크롬 새 시크릿창에 붙여넣어서 카카오계정 로그인 
# https://kauth.kakao.com/oauth/authorize?client_id='REST_API_KEY'&redirect_uri=https://www.google.com/&response_type=code&scope=talk_message
# 로그인 진행후 리다이렉트되는 구글 주소에서 /?code= 뒷부분을 복사하여 17줄 ''사이에 삽입

import requests
import json

#인가코드(authorize_code)생성은 4~6줄 참조해주세요

#인가코드를 사용하여 액세스 토큰 생성 및 터미널 출력
url = 'https://kauth.kakao.com/oauth/token'
rest_api_key = '8ff9157(일부삭제됨)9ee69a3b4b6fb'
redirect_uri = 'https://www.google.com/'
authorize_code = 'ZcemWTJmHlR5eWX(일부삭제됨)Ehwx6gERYQoLXKfSWO3dcV_wq'

data = {
    'grant_type':'authorization_code',
    'client_id':rest_api_key,
    'redirect_uri':redirect_uri,
    'code': authorize_code,
    }

response = requests.post(url, data=data)
tokens = response.json()
print(tokens)

# 생성된 액세스코드,접근범위,갱신코드 json파일 생성, 액세스코드는 6시간(21599초)유효, 갱신코드는 60일(5183999초) 유효
with open("kakao_code.json","w") as fp:
    json.dump(tokens, fp)

# 코드정보 json파일 불러오기    
with open("kakao_code.json","r") as fp:
    tokens = json.load(fp)

url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"

# 사용자 토큰 헤더
headers={
    "Authorization" : "Bearer " + tokens["access_token"]
}

# 메세지 템플릿
template = {
    "object_type" : "list",
    "header_title" : "오늘의 의상 추천",
    "header_link" : {
        "web_url" : "www.google.com",
        "mobile_web_url" : "www.google.com"
    },
    "contents" : [
        {
            "title" : "오늘의 당신에겐 티셔츠가 어울려요!",
            "description" : "상의 추천",
            "image_url" : "https://www.picoop.co.kr/data/goods/17/2020/05/1243_tmp_9253441e841e04a1b9c63e489ae6e54b7526view.JPG",
            "image_width" : 50, "image_height" : 50,
            "link" : {
                "web_url" : "www.google.com",
                "mobile_web_url" : "www.google.com"
            }
        },
        {
            "title" : "오늘의 당신에겐 청바지가 어울려요!",
            "description" : "하의 추천",
            "image_url" : "https://image.musinsa.com/mfile_s01/2022/01/21/3310353cbe48b3d8c3dcebbc3738f58b125136.jpg",
            "image_width" : 50, "image_height" : 50,
            "link" : {
                "web_url" : "www.google.com",
                "mobile_web_url" : "www.google.com"
            }
        }
        
    ]
    
}

# 발송 결과
data = {
    "template_object" : json.dumps(template)
}

response = requests.post(url, data=data, headers=headers)
print(response.status_code)
if response.json().get('result_code') == 0:
    print('메시지를 성공적으로 보냈습니다.')
else:
    print('메시지를 성공적으로 보내지 못했습니다. 오류메시지 : ' + str(response.json()))
    
    
    
# 참고 블로그
# https://novice-engineers.tistory.com/11?category=908185
# https://ai-creator.tistory.com/23
# https://blog.daum.net/geoscience/1624
