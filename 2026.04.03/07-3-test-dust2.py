from urllib import request
from bs4 import BeautifulSoup
from urllib.parse import quote_plus

def get_dust(city='서울'):

    city = quote_plus(city)
    url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EB%AF%B8%EC%84%B8%EB%A8%BC%EC%A7%80+"+city
    target = request.urlopen(url) #접속정보 등록
    soup = BeautifulSoup(target, "html.parser")

    tag = "div.detail_info.lv3 > dl" #오전
    #>의 의미: 바로 밑 자식만이냐, 없으면 모든 자식들이냐
    #똑같은 클래스 dd.lvl인데 하나만 나오는 이유: select_one은 첫번째거만
    #temp = soup.select("dd.lvl").get_text() #여러개
    temp = soup.select_one(tag).get_text()
    temp = " ".join(temp.split())

    temp = temp.split()
    result = {temp[0] : temp[1]}#'오전':'나쁨' #딕셔너리 만든거

    tag = "div.detail_info.lv2 > dl" #오후
    temp = soup.select_one(tag).get_text()
    temp = " ".join(temp.split())
    
    temp = temp.split()
    result[temp[0]] = temp[1] #추가!!!!!!!!!!
    #'오전':'나쁨'
    # print('result:',result)

    return result

get_dust()