import pymysql

# 전역변수 설정
conn=None
cur=None

sql=''

#메인코드

conn=pymysql.connect(host='localhost', user='chungwon', password='1234', db='notingbetter',charset='utf8')#접속정보
cur = conn.cursor() #커서생성

sql="CREATE TABLE IF NOT EXISTS userTable (id char(4),userName char(10), email char(15),brirthYear int)"# 실행할 sql문 
cur.execute(sql)# 커서로 sql 실행

conn.commit()# 저장 
conn.close()#종료 