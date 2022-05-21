# 참고 블로그
# https://novice-engineers.tistory.com/14?category=908185
# https://developers.kakao.com/docs/latest/ko/kakaologin/rest-api#req-user-info 사용자정보가져오기

import requests
import json


# 액세스 코드정보 json파일 불러오기   
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