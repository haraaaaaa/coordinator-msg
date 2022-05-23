"""
작업순서 및 미해결점

O-해결됨/X-해결안됨/?-모르겠음

# (?)1. 인가코드생성 주소 보안
# https://kauth.kakao.com/oauth/authorize?client_id=8fgegre1bd(일부삭제됨)b34fb&redirect_uri=https://www.google.com/&response_type=code&scope=t
# 형식이라서 카카오계정 로그인 요구시 REST API KEY가 노출되는거 같은데 어쩔수없나? 

(?)2. 인가코드 생성 불러오기
https://www.google.com/?code={authorized_code}
카카오 계정 로그인 후 url에 보이는 인가코드를 자동으로 코드환경으로..? 불러 올 수 없을까

1+2 > 로그인페이지를 Spring이나 Node.js react로 별도구현하면 해결,
그전까지는 수동으로 생성된 인가코드 입력

셀레니움ㅍ selenium


(O)3. 인가코드로 액세스 토큰 생성
01mktoken.py 모듈로 진행가능

(O)4. 액세스 토큰 갱신
기본생성 액세스토큰은 6시간뒤 만료, 리프레시토큰(갱신토큰)으로 갱신하면 60일까지 사용가능
02refresh.py 모듈로 진행가능

(O)5. 액세스코드를 사용하여 사용자 정보 받아오기
03getgenderdata.py로 진행가능

(X)6. 발신 메세지 템플릿 생성
DB팀에서 가공된 데이터를 어떻게 받아올것이냐? > API긴한데 어... 내가할수있지그거?맞지?
가공된 데이터를 사용해서 어떤 형식의 메세지가 구성될것이냐 > 미학적 욕심을 버리면 단순구현은 가능할듯

(O)7. 액세스코드를 사용하여 메세지를 보낼 타겟목록(친구목록) 생성
04sendmsgtolist.py로 진행가능

(O)8. 메세지 발신 테스트
04sendmsgtolist.py로 진행가능

---------------- 여기까지가 기본기능구현
(?)9. 메세지 예약 발송 방법
카카오 서비스를 이용하는방법은(카카오앱-카카오채널) 사업자 등록한 비즈니스 회원만 가능
AWS 인스턴스하나 만들고 
crontab -e 
* 7 * * * ec2-user ./finalcode.py
하는방법을 생각중임  
"""
# 카카오 문제점 

# 1. 제한된 5명밖에 사용못함

# 2. 더 받아올 데이터가 필요하다면(이름,성별제외)

# 슬랙이든 트위터등 다른 메신저를 사용해야될거같아요.
# 구분자-이름or이메일 / 성별 / (...더위추위취향,위치정보,)

# 어제입은거안입을거야
# https://kauth.kakao.com/oauth/authorize?client_id=8ff9157a006628fe0bd9ee69a3b4b6fb&redirect_uri=https://www.google.com/&response_type=code&scope=talk_message,friends,gender

import requests
import json

# url = 'https://kauth.kakao.com/oauth/token'
# rest_api_key = '8ff9157a006628fe0bd9ee69a3b4b6fb'
# redirect_uri = 'https://www.google.com/'
# authorize_code = 'snEMXS9zs3zjSunzH24t7ev9B8Q12gWIgEkqwbo0X5m8WvZAtpnTYzwTyOstvHSSdBXJoAo9cpcAAAGAYEXoUQ'

# data = {
#     'grant_type':'authorization_code',
#     'client_id':rest_api_key,
#     'redirect_uri':redirect_uri,
#     'code': authorize_code,
#     }

# response = requests.post(url, data=data)
# tokens = response.json()
# print(tokens)

# with open(r"D:\Backup\coordinator-msg\tokens\kakao_code1.json","w") as fp:
#     json.dump(tokens, fp)

with open(r"D:\Backup\coordinator-msg\tokens\kakao_code1.json","r") as fp:
    tokens = json.load(fp)

gender_url = "https://kapi.kakao.com/v2/user/me"

# 액세스 토큰 헤더
headers={"Authorization" : "Bearer " + tokens["access_token"]}

# 발송대상 목록 불러오기
result = json.loads(requests.get(gender_url, headers=headers).text)

# 발송대상 uuid list 생성
print(type(result))
print("=============================================")
print(result)
print("=============================================")
gender_list = result.get("kakao_account")
print(gender_list)
print(type(gender_list))
print("=============================================")
print(gender_list.get("gender"))
gender_id = gender_list.get("gender")
print("=============================================")
print(gender_id)

with open(r"D:\Backup\coordinator-msg\tokens\gender1.json","w") as fp:
    json.dump(gender_id, fp)


friend_url = "https://kapi.kakao.com/v1/api/talk/friends"

headers={"Authorization" : "Bearer " + tokens["access_token"]}

# 발송대상 목록 불러오기
result = json.loads(requests.get(friend_url, headers=headers).text)

# 발송대상 uuid list 생성
print(type(result))
print("=============================================")
print(result)
print("=============================================")
friends_list = result.get("elements")
print(friends_list)
# print(type(friends_list))
print("=============================================")
print(friends_list[0].get("uuid"))
friend_id = friends_list[0].get("uuid")
print(friend_id)


#메세지 발송영역
send_url= "https://kapi.kakao.com/v1/api/talk/friends/message/default/send"


data={
    'receiver_uuids': '["{}"]'.format(friend_id),
    "template_object": json.dumps({
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
    })
}

data = {
    "template_object" : json.dumps(data)
}

response = requests.post(send_url, data=data, headers=headers)
print(response.status_code)
if response.json().get('result_code') == 0:
    print('메시지를 성공적으로 보냈습니다.')
else:
    print('메시지를 성공적으로 보내지 못했습니다. 오류메시지 : ' + str(response.json()))