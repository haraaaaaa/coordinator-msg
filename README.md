# coordinator-msg
Recommend what clothes to wear today ( msg-server )


Directory Explanation  
디렉토리 설명  
---

- KT
카카오톡으로 메세지 발신/수신에 관한 코드
1. 1personal_message
    - '나에게 메세지 보내기'에 해당하는 코드 정리

2. 2group_message
    - '등록된 그룹에게 메세지 보내기'에 해당하는 코드 정리
    - kakao developers의 내 어플리케이션에 등록된 최대 5인에게까지만 발송 가능

3. 3final_message
    - '프로세스 서버에서 가공된 데이터를 수신해 메세지 보내기'에 해당하는 코드 정리

- SLACK
슬랙으로 메세지 발신/수신에 관한 코드
- 01. receiving 
    - DB에서 생성된 Query 수신
- 02. sending
    - 해당 Slack 채널로 메세지 발신
