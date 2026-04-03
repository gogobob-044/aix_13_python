from urllib import request
from bs4 import BeautifulSoup


def get_news():
    url = "https://news.naver.com/section/105"
    target = request.urlopen(url)
    soup = BeautifulSoup(target, "html.parser")

    tag = "li.rl_item .rl_txt" #부모 자식을 보가며 클래스 찾기
    news = soup.select(tag)
    for t in news:
        title = t.get_text()
        print(title)

get_news()