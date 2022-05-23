# 참고 블로그
# https://novice-engineers.tistory.com/13?category=908185

import requests
import json

# 액세스 코드정보 json파일 불러오기   
with open(r"D:\Backup\coordinator-msg\tokens\kakao_code1.json","r") as fp:
    tokens = json.load(fp)

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


# #메세지 발송영역
# send_url= "https://kapi.kakao.com/v1/api/talk/friends/message/default/send"

# data={
#     'receiver_uuids': '["{}"]'.format(friend_id),
#     "template_object": json.dumps({
#         "object_type" : "list",
#         "header_title" : "오늘의 의상 추천",
#         "header_link" : {
#             "web_url" : "www.google.com",
#             "mobile_web_url" : "www.google.com"
#         },
#         "contents" : [
#             {
#                 "title" : "오늘의 당신에겐 아무튼가 어울려요!",
#                 "description" : "상의 추천",
#                 "image_url" : "https://www.picoop.co.kr/data/goods/17/2020/05/1243_tmp_9253441e841e04a1b9c63e489ae6e54b7526view.JPG",
#                 "image_width" : 50, "image_height" : 50,
#                 "link" : {
#                     "web_url" : "www.google.com",
#                     "mobile_web_url" : "www.google.com"
#                 }
#             },
#             {
#                 "title" : "오늘의 당신에겐 청바지가 어울려요!",
#                 "desㅈㅇㅈㅇription" : "하의 추천",
#                 "image_url" : "https://image.musinsa.com/mfile_s01/2022/01/21/3310353cbe48b3d8c3dcebbc3738f58b125136.jpg",
#                 "image_width" : 50, "image_height" : 50,
#                 "link" : {
#                     "web_url" : "www.google.com",
#                     "mobile_web_url" : "www.google.com"
#                 }
#             }
            
#         ]
#     })
# }

# response = requests.post(send_url, headers=headers, data=data)
# response.status_code
