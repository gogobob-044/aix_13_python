from urllib import request
from bs4 import BeautifulSoup


#삼성전자 주가 추출
def get_stock():
    url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EC%82%BC%EC%84%B1%EC%A0%84%EC%9E%90+%EC%A3%BC%EA%B0%80"
    target = request.urlopen(url)
    soup = BeautifulSoup(target, "html.parser")

    tag = "a._target strong" #부모 자식을 보가며 클래스 찾기
    stock = soup.select_one(tag).get_text()

    print(stock)

get_stock()