'''
스무고개게임
'''
print('### 스무고개게임 v0.1 ###')

import random
ans = random.randint(1,100)
i = 0
min=1
max=100

while True:
    i += 1
    
    user=int(input(f"{i}번째시도: 1~100사이의 숫자 입력>> "))
    if ans == user :
       print("정답~")
       break
    if ans < user:
        print("낮춰주세요")
        if user - 1 < max: 
            max= user - 1
        
    else :
        print("높여주세요")
        if user + 1 > min:
            min = user + 1
    
    print("후보숫자>>", *range(min, max+1))
    if i == 6:
        print(f"당신은 바보입니까 정답은 {ans}")
        break
