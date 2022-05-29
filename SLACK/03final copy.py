# MAIN REFERNCE https://velog.io/@eeeclipse/Build-a-SlackBot-Daily-Indicator
# REFERENCE
# 
# https://dragon1-honey1-wayfarer.tistory.com/entry/Python-%EC%8A%AC%EB%9E%99Slack-%EC%95%8C%EB%A6%BC%EB%B4%87-%EC%84%A4%EC%A0%95%ED%95%98%EC%97%AC-%EB%A7%A4%EC%9D%BC-%EC%A6%9D%EC%8B%9C-%EC%95%8C%EB%A6%BC-%EB%B0%9B%EA%B8%B0-fin


import requests
import json
def post_message(channel, text): 
    SLACK_BOT_TOKEN = "xoxp-3259f5456ba194b246"
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
    post_message("#test", "Hello World!")