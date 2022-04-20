"""
작업순서 및 미해결점

O-해결됨/X-해결안됨/?-모르겠음

(?)1. 인가코드생성 주소 보안
https://kauth.kakao.com/oauth/authorize?client_id=8fgegre1bd(일부삭제됨)b34fb&redirect_uri=https://www.google.com/&response_type=code&scope=t
형식이라서 카카오계정 로그인 요구시 REST API KEY가 노출되는거 같은데 어쩔수없나? 

(?)2. 인가코드 생성 불러오기
https://www.google.com/?code={authorized_code}
카카오 계정 로그인 후 url에 보이는 인가코드를 자동으로 코드환경으로..? 불러 올 수 없을까

(O)3. 인가코드로 액세스 토큰 생성
2group_message/01mktoken.py 모듈로 진행가능

(?)4. 액세스 토큰 갱신
기본생성 액세스토큰은 6시간뒤 만료, 리프레시토큰(갱신토큰)으로 갱신하면 60일까지 사용가능
액세스토큰의 갱신 자동화방법을 찾아야

(X)5. 액세스코드를 사용하여 메세지를 보낼 타겟목록(친구목록) 생성
2group_message/02getfriendlist.py 모듈로 진행가능
부계정 생성문제로인해 아직 테스트 진행 못함

(X)6. 발신 메세지 템플릿 생성
DB팀에서 가공된 데이터를 어떻게 받아올것이냐? > API긴한데 어... 내가할수있지그거?맞지?
가공된 데이터를 사용해서 어떤 형식의 메세지가 구성될것이냐 > 미학적 욕심을 버리면 단순구현은 가능할듯

(X)7. 메세지 발신 테스트
2group_message/03sendmsgtolist.py 모듈로 진행가능
부계정 생성문제로인해 아직 테스트 진행 못함

---------------- 여기까지가 기본기능구현
(?)8. 메세지 예약 발송 방법
카카오 서비스를 이용하는방법은(카카오앱-카카오채널) 사업자 등록한 비즈니스 회원만 가능
AWS 인스턴스하나 만들고 
crontab -e 
* 7 * * * ec2-user ./finalcode.py
하는방법을 생각중임  
"""

