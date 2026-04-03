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

def get_dust(city='서울'):

    city = quote_plus(city)
    url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EB%AF%B8%EC%84%B8%EB%A8%BC%EC%A7%80+"+city
    target = request.urlopen(url) #접속정보 등록
    soup = BeautifulSoup(target, "html.parser")

    tag = "div.detail_info.lv3 > dl" #오전
#똑같은 클래스 dd.lvl인데 하나만 나오는 이유: select_one은 첫번째거만
#temp = soup.select("dd.lvl").get_text() #여러개
    temp = soup.select_one(tag).get_text()
    temp = " ".join(temp.split())

    temp = temp.split()
    result = {temp[0] : temp[1]}#'오전':'나쁨' #딕셔너리 만든거

    tag = "div.detail_info.lv2 > dl" #오후
    temp = soup.select_one(tag).gt_text()
    temp = " ".join(temp.split())
    
    temp = temp.split()
    result[temp[0]] = temp[1] #추가!!!!!!!!!!
    #'오전':'나쁨'
    # print('result:',result)

    return result


if __name__ == "__main__": #임포트할 땐 실행 X
    city = "수원"
    ans = get_weather(city)
    print(f'{city} 날씨는 {ans}')
    ans = get_dust(city)
    print(f'{city} 미세먼지는 {ans}')

# print('__name__', __name__)

#출력하는 범위를 바꾸려면 div.temperature_text를 수정

