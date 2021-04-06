#DemoFunction2.py
#가변인자로 덧셈처리
def v(*ar):
    result=0
    for item in ar:
        result += item

    return result

#호호호
print(v(2,3))    
print(v(2,3,4))
print("^"*40)

#함수를 정의(단일값,스칼라)

def add10(i):
    return i+10

x=[1,2,3,4,5]
#각 아이템에 맵핑하는 함수
#map(함수명, 순회가능한 형식)
for item in map(add10, x):
    print(item)

print("------람다함수사용--------")
#위에 def add10이 필요가없음 한줄로 끄읏
for item in map(lambda i:i+10, x):
    print(item)
