from urllib import request
from bs4 import BeautifulSoup

url = "https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&ssc=tab.nx.all&query=%EC%9D%BC%EA%B8%B0%EC%98%88%EB%B3%B4+%EC%84%9C%EC%9A%B8&oquery=dlfrldPqh+tjdnf&tqi=jN8KbdqXKZwsskOzQ%2Bl-452885&ackey=5x0herpa"
target = request.urlopen(url) #접속정보 등록
soup = BeautifulSoup(target, "html.parser")

tag = "div.temperature_text"
temp = soup.select_one(tag).get_text()
print('temp:', temp)