dan = 3
print(str(dan)+"*")#귀찮음

#format() 함수: 숫자->문자열
print("{}*{}={}".format(dan,1,dan*1))
print("{}*{:5d}={}".format(dan,1,dan*1))
# {:5d}: 5칸 확보, 맨 우측부터 채워짐
print("{}*{:5d}={}".format(dan,1,dan*1))

print("헬로 python 프로그래밍".upper()) #대문자로

a="""
     헬로 파이썬 프로그래밍     
"""
print(a+"/")
print(a.strip()+"/")

print("안녕123".isalnum())
#공백도 문자임

print("abc abc programing".find("ab")) #0
#->0번째부터 있다는 뜻
print("abc abc programing".find("bc")) #1
print("abc abc programing".find("BC")) #-1
#->못찾음
print("abc abc programing".find("bc",2)) #5
#->2번 인덱스부터 찾음 공백은 인덱스X
a="안녕하세요"
print("안녕" in a)
print("잘가" in a)

#split(",")-> ","기준으로 스플릿(문자로됨)
b = "홍,이,박,강".split(",")
print(b)
b = "100,200,300,200".split(",")
print(b)
#['100', '200', '300', '200']
#''가 붙었다는 건 문자라는 뜻
print(b[0]) #문자
print(int(b[0])) #숫자
print(int(b[0])+int(b[1]))
print(b[0]+b[1]) #'100200'

#합과 평균
totoal = 0
mean = 0
total = int(b[0])+int(b[1])+int(b[2])+int(b[3])
print("total={}".format(total))
print("mean={}".format(total/4))

#더간단한 f-
print(f"total={total}")
print(f"mean={total/4}")

#구구단
dan=3
print(f"{dan}*{1}={dan*1}")
print(f"{dan}*{2}={dan*2}")
print(f"{dan}*{3}={dan*3}")

#생년을 입력받아 나이를 계산하기
a = input("태어난 해 4자리를 입력하세요: ")
print(f"당신은 {2026 - int(a)}살입니다")

