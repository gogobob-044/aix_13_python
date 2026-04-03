# import datetime

# now = datetime.datetime.now()
# print(now)
# print(now.year,'년')
# print(f"{now.year}년")
# print(f"{now.month}월")
# print(f"{now.day}일")
# print(f"{now.hour}시")
# print(f"{now.min}분")
# print(f"{now.second}초")
# print(f"{now.weekday}요일") #0월 1화

# #####
# if now.hour < 12:
#     print(f"현재시간 {now.hour}시로 오전입니다")
# else:
#     print(f"현재시간 {now.hour}시로 오후입니다")

#167p
# import datetime
# now = datetime.datetime.now()

# if 3<= now.month <= 5:
#     print(f"이번 달은 {now.month}로 봄입니다!")
# elif 6 <= now.month <=8:
#     print(f"이번 달은 {now.month}로 여름입니다!")
# elif 9 <= now.month <=11:
#     print(f"이번 달은 {now.month}로 가을입니다!")
# else:
#     print(f"이번 달은 {now.month}로 겨울입니다!")

### 월을 입력받아 계절 출력
# month = int(input("월을 입력하세요(1~12): "))

# if month < 3:
#     print(f"이번 달은 {month}로 겨울입니다!")

# elif month <= 5:
#     print(f"이번 달은 {month}로 봄입니다!")
# elif month <=8:
#     print(f"이번 달은 {month}로 여름입니다!")
# elif month <=11:
#     print(f"이번 달은 {month}로 가을입니다!")
# else:
#     print(f"이번 달은 {month}로 겨울입니다!")

##p170
number = input("정수 입력: ")
last_character = number[-1]

if last_character in "02468":
    print("짝수입니다.")
else:
    print("홀수입니다.")

######
