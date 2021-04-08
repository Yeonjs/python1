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
datalist=(("tom","010-123"),("lsd","010-567"))
cur.executemany("insert into PhoneBook values (?, ?);", datalist)
#검색
cur.execute("select * from PhoneBook;")
# for row in cur:       #전체 출력
#     print(row)

#1건 검색
print(cur.fetchone())
#N건 검색
print("---fetchMany(2)---")
print(cur.fetchmany())
print("===fetchall()===") 
#위에 1건 검색하고 2건 검색 해서 다 처리된걸로 간주하고 나머지 하나만 출력됨
#데이터가 사라진건 아닌데 버퍼가 날라간겨 
cur.execute("select*from PhoneBook;")   #이코드 쓰면 위에꺼 좆까고 다출력됨
print(cur.fetchall())
print("------"*8)

#결과를 슬라이싱
cur.execute("select*from PhoneBook;") 
result=cur.fetchone()
print(result[0])
print(result[1])

print("==========다중행의 경우==========")
#2차원 행렬 데이터 [행][렬]
result=cur.fetchall()
#이것도 마찬가지 위에 1번 사용되서 길동새끼부터 시작됨
print(result[0][0])
print(result[0][1])

