import my_util
#import: 파일의 메모리를 읽으며 실행
#__name__ == "__main__" 아니면 그냥 실행했을 때 안나옴

#불러오기
w = my_util.get_weather("서울")
print('서울온도+', w['temp'])

d = my_util.get_dust("서울")
print(f'서울의 미세먼지는{d}')