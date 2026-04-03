from urllib import request
from bs4 import BeautifulSoup
from urllib.parse import quote_plus

city = input("날씨를 알고싶은 도시 이름>> ")
city = quote_plus(city) #부호화
url = 'https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&ssc=tab.nx.all&query=%EB%82%A0%EC%94%A8'+city
target = request.urlopen(url)
soup = BeautifulSoup(target, 'html.parser')

temp=soup.select_one('div.temperature_text').get_text()
print('temp=', temp)

hum=soup.select_one('dl.summary_list').get_text()
a = hum.strip().split(' ')
print('습도=',a[5])
print('end')

