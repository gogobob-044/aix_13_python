#03-2. 도전문제1
a = input("입력: ")
if a == '안녕' or a == '안녕하세요.':
    print("안녕하세요.")
elif a == '지금 몇 시야?' or a == '지금 몇 시예요?':
    print("지금은 15시입니다.")
else :
    print(a)

#03-2. 도전문제2
a = int(input("정수를 입력해주세요: "))
if a % 2 == 0:
    print(f"{a}는 2로 나누어 떨어지는 숫자입니다.")
else:
    print(f"{a}는 2로 나누어 떨어지는 숫자가 아닙니다.")
if a %3 == 0:
    print(f"{a}는 3로 나누어 떨어지는 숫자입니다.")
else:
    print(f"{a}는 3로 나누어 떨어지는 숫자가 아닙니다.") 
if a % 4 == 0:
    print(f"{a}는 4로 나누어 떨어지는 숫자입니다.")
else:
    print(f"{a}는 4로 나누어 떨어지는 숫자가 아닙니다.")
if a % 5 == 0:
    print(f"{a}는 5로 나누어 떨어지는 숫자입니다.")
else:
    print(f"{a}는 5로 나누어 떨어지는 숫자가 아닙니다.")
    
#04-1. 확인문제1
list_a = [0,1,2,3,4,5,6,7]
list_a.extend(list_a)
list_a.append(10)
list_a.insert(3,0)
list_a.remove(3)
list_a.pop(3)
list_a.clear()
print(list_a)

#04-1. 2번
numbers = [273,103,5,32,65,9,72,800,99]
for number in numbers:
    if number >= 100 :
        print("- 100 이상의 수: ", number)

#04-1. 3번
numbers = [273,103,5,32,65,9,72,800,99]
for number in numbers:
    if number % 2 != 0 :
        print(f"{number}은 홀수입니다")
    else :
        print(f"{number}은 짝수입니다")
for number in numbers:
    if number < 10 :
        print(f"{number}는 1의 자릿수입니다.")
    elif number < 100 :
        print(f"{number}는 2의 자릿수입니다.")
    elif number < 1000 :
        print(f"{number}는 3의 자릿수입니다.")

#04-1. 4번
numbers = [1,2,3,4,5,6,7,8,9]
output = [[],[],[]]

for number in numbers:
    output[(number - 1) % 3].append(number)
    # 나머지가 1,2,0인 방
print(output)

#04-1. 5번
numbers = [1,2,3,4,5,6,7,8,9]
for i in range(0,len(numbers) // 2):
    j = i*2 +1
    print(f"i = {i}, j = {j}")
    numbers[j] = numbers[j]**2
print(numbers)
