# MAIN REFERNCE https://luran.me/300
# MINOR REFERENCES 
# http://pythonstudy.xyz/python/article/202-MySQL-%EC%BF%BC%EB%A6%AC
# https://118k.tistory.com/989
# http://bigdata.dongguk.ac.kr/lectures/DB/_book/python%EC%97%90%EC%84%9C-mysql%EB%8D%B0%EC%9D%B4%ED%84%B0%EC%9D%98-%EC%A0%91%EA%B7%BC.html

# DATABASE testdb, TABLE test1, test1( gender, clothe)
# USER dbadmin PW 1231231231!


import pymysql

db = pymysql.Connect(host='localhost', user='dbadmin', password='123123123!', database='testdb')
cursor = db.cursor()

query = "SELECT gender, clothe FROM test1"
cursor.execute(query)
result = cursor.fetchall()

for message in result:
    print(message)

