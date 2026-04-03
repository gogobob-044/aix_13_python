from urllib import request
from bs4 import BeautifulSoup
from urllib.parse import quote_plus

def get_exchange(m):
    m = quote_plus(m)
    url = "https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&ssc=tab.nx.all&query=%ED%99%98%EC%9C%A8"+m
    target = request.urlopen(url)
    soup = BeautifulSoup(target, "html.parser")

    tag = "div.price_info strong" #부모 자식을 보가며 클래스 찾기
    exchange = soup.select_one(tag).get_text()
    
    return (f'{exchange}원')

ans=get_exchange("달러")
print(ans)