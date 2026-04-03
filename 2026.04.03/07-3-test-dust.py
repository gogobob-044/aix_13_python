from urllib import request
from bs4 import BeautifulSoup


url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EB%AF%B8%EC%84%B8%EB%A8%BC%EC%A7%80+%EC%84%9C%EC%9A%B8&ackey=t7fciwnr"
target = request.urlopen(url) #접속정보 등록
soup = BeautifulSoup(target, "html.parser")

tag = "div.detail_info.lv3 > dl" #오전
#똑같은 클래스 dd.lvl인데 하나만 나오는 이유: select_one은 첫번째거만
#temp = soup.select("dd.lvl").get_text() #여러개
temp = soup.select_one(tag).get_text()
temp = " ".join(temp.split())

print(temp)

tag = "div.detail_info.lv2 > dl" #오후
temp = soup.select_one(tag).get_text()
temp = " ".join(temp.split())
print(temp)