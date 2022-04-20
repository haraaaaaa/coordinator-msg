import json
import requests

with open(r"D:\python_workspace\kakao\kakao_code.json","r") as fp:
    tokens = json.load(fp)

url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"

# 사용자 토큰
headers={
    "Authorization" : "Bearer " + tokens["access_token"]
}

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

data = {
    "template_object" : json.dumps(template)
}

response = requests.post(url, data=data, headers=headers)
print(response.status_code)
if response.json().get('result_code') == 0:
    print('메시지를 성공적으로 보냈습니다.')
else:
    print('메시지를 성공적으로 보내지 못했습니다. 오류메시지 : ' + str(response.json()))