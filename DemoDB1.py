#DemoDB1.py
#SQLite를 사용하는 데모(로컬 데이터베이스)
import sqlite3

#첨에는 DBFile(또는 메모리)를 생성
con=sqlite3.connect(":memory:")
#SQL구문을 실행하는것은 대부분 커서객체
cur=con.cursor()
#저장소(테이블) 만들기 = 테이블 스키마(뼈대)
cur.execute("create table PhoneBook (Name text, PhoneNum text);")
#1건입력
cur.execute("insert into PhoneBook values ('weed', '010-011');")
#입력 파라메터 처리
#텍스트박스(GUI,WebPage)에서 입력을 받아서 처리
name="gildong"
phoneNumber="010-222"
cur.execute("insert into PhoneBook values (?, ?);",(name,phoneNumber))
#다중의 레코드(행, row)를 입력받는 경우 = 2차원 행렬데이터
datalist=(("tom","010-123"),("weed","010-567"))
cur.execute("insert into PhoneBook values (?, ?);", datalist))
#검색
cur.execute("select * from PhoneBook;")
for row in cur:
    print(row)