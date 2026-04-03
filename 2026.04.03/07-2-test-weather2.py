from urllib import request
from bs4 import BeautifulSoup
from urllib.parse import quote_plus

#도시이름 입력
def get_weather(city):
    city= "서울"
    city = quote_plus(city)
    url = "https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&ssc=tab.nx.all&query=%EC%9D%BC%EA%B8%B0%EC%98%88%EB%B3%B4+%EC%84%9C%EC%9A%B8"+city
    target = request.urlopen(url) #접속정보 등록
    soup = BeautifulSoup(target, "html.parser")

    tag = "div.temperature_text"
    temp = soup.select_one(tag).get_text()
    return temp


#모듈로 실행할 땐 실행X
city = "수원"
ans = get_weather("city")
print(f'{city}의 {ans}')


#출력하는 범위를 바꾸려면 div.temperature_text를 수정