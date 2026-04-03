'''
숫자맞추기게임
'''
print('### 숫자 맞추기 게임 v0.1 ###')

import random
ans = random.randint(1,100)
i = 0
while True:
    i += 1
    
    user=int(input(f"{i}번째시도: 1~100사이의 숫자 입력>> "))
    if ans == user :
       print("정답~")
       break
    # if ans < user:
    #     print("낮춰주세요")
    # else :
    #     print("높여주세요")
    print("낮춰주세요" if ans < user else "높여주세요")
    if i == 6:
        print(f"당신은 바보입니다 정답은 {ans}")
        break

