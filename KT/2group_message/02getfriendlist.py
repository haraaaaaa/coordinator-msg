# 참고 블로그
# https://novice-engineers.tistory.com/14?category=908185

import requests
import json


# 액세스 코드정보 json파일 불러오기   
with open(r"D:\Backup\coordinator-msg\tokens\kakao_code1.json","r") as fp:
    tokens = json.load(fp)

friend_url = "https://kapi.kakao.com/v1/api/talk/friends"

# 액세스 토큰 헤더
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
print("=============================================")
print(friend_id)