# MAIN REFERNCE https://velog.io/@eeeclipse/Build-a-SlackBot-Daily-Indicator
# REFERENCE
# 
# https://dragon1-honey1-wayfarer.tistory.com/entry/Python-%EC%8A%AC%EB%9E%99Slack-%EC%95%8C%EB%A6%BC%EB%B4%87-%EC%84%A4%EC%A0%95%ED%95%98%EC%97%AC-%EB%A7%A4%EC%9D%BC-%EC%A6%9D%EC%8B%9C-%EC%95%8C%EB%A6%BC-%EB%B0%9B%EA%B8%B0-fin


import pymysql
import requests
import json

db = pymysql.Connect(host='localhost', user='dbadmin', password='123123123!', database='testdb')
cursor = db.cursor()

query = "SELECT gender, clothe FROM test1"
cursor.execute(query)
result = cursor.fetchall()

for message in result:
    print(message)

# token = "xoxp-3327808871477-333855608094b246"
# channel = "#test"

# requests.post("https://slack.com/api/chat.postMessage",
#     headers={"Authorization": "Bearer "+token},
#     data={"channel": channel,"text": result})
# 튜플이라서그런가 제일 마지막에 후드티만 출력됨

def post_message(channel, text): 
    SLACK_BOT_TOKEN = "xoxp-3327808871477-3338556080275-"
    headers = {
        'Content-Type': 'application/json', 
        'Authorization': 'Bearer ' + SLACK_BOT_TOKEN
        }
    payload = {
        'channel': channel,
        'text': text
        }
    r = requests.post('https://slack.com/api/chat.postMessage', 
        headers=headers, 
        data=json.dumps(payload)
        )
if __name__ == '__main__':
    post_message("#test", result)




