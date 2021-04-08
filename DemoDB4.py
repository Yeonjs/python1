#DemoDB4.py
import sqlite3

#연결객체 리턴
con=sqlite3.connect("c:\\work2\\Demo10.db")
#커서객체 리턴
cur=con.cursor()
cur.execute("select * from Emp;")
for row in cur:
    print(row)