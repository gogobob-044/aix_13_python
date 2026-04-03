from urllib import request
from bs4 import BeautifulSoup
from urllib.parse import quote_plus

#도시이름 입력
def get_weather(city):
    city= "서울"
    city = quote_plus(city)
    url = "https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&ssc=tab.nx.all&query=%EC%9D%BC%EA%B8%B0%EC%98%88%EB%B3%B4+"+city
    target = request.urlopen(url) #접속정보 등록
    soup = BeautifulSoup(target, "html.parser")

    tag = "div.temperature_text" #온도
    mytemp = soup.select_one(tag).get_text().strip()

    tag = "div.temperature_info" #날씨 정보
    temp = soup.select_one(tag).get_text() #공백이 너무 많아!
    temp = temp.strip() #앞뒤공백삭제
    temp = " ".join(temp.split()) #공백으로 조인
    temp = temp.split()

    return {
        'temp': mytemp,
        'yestd': temp[1]+" "+temp[2],
        'weather':temp[3],
        'hum':temp[7],
        'windd':temp[8],
        'winds':temp[9]
    }

#모듈로 실행할 땐 실행X
city = "수원"
ans = get_weather("city")
print(f'{city}은 {ans}')


#출력하는 범위를 바꾸려면 div.temperature_text를 수정