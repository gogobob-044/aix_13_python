print( 10 == 100 ) #equal
# print(10 = 100) 오류:10은 변수,변수는 숫자로 시작하면 안됨
print( 10 != 100) # not equal
print( 10 < 100 )
print( 10 > 100 )
print( 10 <= 100 )
print( 10 >= 100 )

#한글은 가나다순으로 작은값
a= "가방"
b= "하마"
print( a == b) #False 
print( a < b) #True
print( a > b) #False

#범위
c=25
print( 10 < c < 30 ) #True
print( 10 < c < 20 ) #False

#조건문(참일 때만 실행)
if c < 30: # c는 30보타 작음  END 
    print("c는 30보타 작음")
print("END")

if c < 20: #END
    print("c는 20보타 큼")
print("END")

#조건문 거짓일 때
if c < 30:  
    print("c는 30보타 작음")
else:
    print("c는 30보타 큼")

print("END")

# a = int(input("학점: "))
# if a >= 90:
#     print("A")
# elif 80 <= a < 90:
#     print("B")
# else:
#     print("c")
    
####
score = 88
grade = "" #비워둠
if score >= 90:
    grade="A"
elif score >= 80:
    grade="B"
elif score >= 70:
    grade="C"
else:
    grade="F"
print(f"{score}의 학점음 {grade}입니다.")

#not
if not c < 30: #반대로 출력  
    print("c는 30보타 작음")
else:
    print("c는 30보타 큼")

print("END")

####
score = 88
if score <= 100 and score >= 90:
    grade = "A"
elif score <= 89 and score >= 80:
    grade = "B"
else:
    grade = "F"
print(f"{score}의 학점음 {grade}")