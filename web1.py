# web1.py
#from 패키지명 import 모듈명
from bs4 import BeautifulSoup

#페이지를 로딩(HTML문서를 읽어오누.유니코드)
page=open("c:\\work2\\test01.html", "rt" ,encoding="utf-8").read()
#검색이 용이한 객체 생성
soup=BeautifulSoup(page,"html.parser")
#print(soup.prettify())

#<p>를 모두 검색해 리스트형식으로
#print(soup.find_all("p"))

#첫번째<p>를검색
#print(soup.find("p"))

#<p class="outer-text"> 된 경우(약간의 필터링)
#print(soup.find_all("p", class_="outer-text"))

#특정 id속성을 검색
#print(soup.find(id="first"))

#<a>태그or<b> 가져와
#print(soup.find_all("a"))
#print(soup.find_all("b"))

#태그를 제거하고 내부 문자열(컨텐츠만)
#<p>컨텐츠</p>
for tag in soup.find_all("p"):
    #앞뒤에 존나긴 공백문자를 제거하려면 .strip()
    print(tag.text.strip())

