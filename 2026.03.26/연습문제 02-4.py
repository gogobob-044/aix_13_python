#1번 - 3
#인자개수보다 {}가 많으면 빈공간에 생겨서 에러남
#참조할 인덱스가 부족하기 때문..

#2번
#순서대로 d b a c

#3번
a = int(input("1: "))
b = int(input("2: "))
print()
print("{}+{}={}".format(a,b,a+b))

#4번
# A 지점: hello
# B 지점: HELLO
#string.upper()는 값을 바꾸는 게 아니라
# 새로운 문자열을 만들어서 반환하는건데 저장을 하지 않았기 떄문에
#string은 바뀌지 않음

#도전문제 1번
pi = 3.141592
r = int(input("구의 반지름을 입력해주세요: "))
a = 4/3*pi*r**3
b = 4*pi*r**2
print(f"= 구의 부피는 {a}입니다.")
print(f"= 구의 겉넓이는 {b}입니다.")

#도전문제2번
a = float(input("밑변의 길이를 입력해주세요: "))
b = float(input("높이의 길이를 입력해주세요: "))
c = (a**2 + b**2)**(1/2)
print(f"= 빗변의 길이는 {c}입니다.")



#입력받을 때 실수로 입력받지 않은 경우
#3번
a = input("1: ")
b = input("2: ")
print()
print("{}+{}={}".format(a,b,int(a)+int(b)))
#도전 2번
a = input("밑변의 길이를 입력해주세요: ")
b = input("높이의 길이를 입력해주세요: ")

c = (float(a)**2 + float(b)**2)**(1/2)
print(f"= 빗변의 길이는{c}입니다.")

