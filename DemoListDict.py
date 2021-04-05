#DemoListDict.py
c=["red","black","white"]
c.append("blue")
print(c)
print(len(c))
print(type(c))
c.insert(1,"pink")
print(c)
c.remove("black")
print(c)
print("="*50)
#딕셔너리(키중심으로 검색,입력,수정,삭제)
f={"똥":5,"오줌":10,"설사":3}
print(f)
#Search
print(f["똥"])
#input
f["코딱지"]=20
print(f)
#modify
f["똥"]=7
#delete
del f["오줌"]
print(f)