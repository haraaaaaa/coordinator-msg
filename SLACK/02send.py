# MAIN REFERENCE, 사유: 220405 가장최근 
# https://dev-nam.tistory.com/11?category=1007364
# MINOR REFENCE, 아직 미적용; 뭔가 방식이 다른데? __NAME__하는게 뭐라고하셨더라
# https://losskatsu.github.io/programming/py-slack/#4-%EC%8A%AC%EB%9E%99-%EC%B1%84%EB%84%90%EC%97%90-%EB%B4%87-%EC%B4%88%EB%8C%80%ED%95%98%EA%B8%B0



import requests

token = "xoxp-"
channel = "#test"
text = "Check your stock crawler."

requests.post("https://slack.com/api/chat.postMessage",
    headers={"Authorization": "Bearer "+token},
    data={"channel": channel,"text": text})