'''
금광찾기게임
가로세로10x10 공간에 있는 금 찾기
'''
print('###금광찾기 게임 v0.1 ###')
import random
com_x = random.randint(1,10)
com_y = random.randint(1,10)

while True:
    ans= input("금의 좌표를 입력하세요(10x10이내 x,y)>> ")
    user_x, user_y = ans.split(',') #배열로 나옴
    user_x, user_y = int(user_x), int(user_y)
    diff_x = abs(com_x - user_x) #x 좌표간격
    diff_y = abs(com_y - user_y) #y 좌표간격
    diff_z = (diff_x**2 + diff_y**2)**(0.5) #지도상 거리
    diff_z = round(diff_z) #반올림
    if diff_z ==0:
        break
    print(f"금괴의 직선거리: {diff_z}")
print("정답입니다")