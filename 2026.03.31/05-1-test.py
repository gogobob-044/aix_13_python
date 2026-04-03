# def print_n(n,*values):
#     for i in range(n):
#         for value in values:
#             print(value)
#         print()

# print_n(3,1,4,3)
# print_n(3,'ㅎㅇ0','안녕','ㅂㅇ','ㅋㅋ')   

# def print_n(*values,n=1):
#     for i in range(n):
#         for value in values:
#             print(value)
#         print()

#     return None #아무것도 없으면 생략가능
# #리턴하면 함수밖으로 가고 되돌아올 수 없음

# print_n(3,1,4,3)
# print_n('ㅎㅇ0','안녕','ㅂㅇ','ㅋㅋ')

# ans =print_n('ㅎㅇ0','안녕','ㅂㅇ','ㅋㅋ')
# print('ans', ans)

# #greetiing(이르)->출력
# def greeting(name):
#     return "안녕하세요"+name+"님"
# ans = greeting("홍길동") #-> 안녕하세요 길동님
# print(ans)

# #입력받은 숫자들의 평균 반환하는 함수
# def calc_avg(*v):
#     return sum(v) / len(v)
# ans= calc_avg(10,20,40,50)
# print(ans)
# ans= calc_avg(10,20,)
# print(ans)

# #sum()대신
# # tot = 0
# # for i in v:
# #     tot += i
# # return tot / len(v)

# #학점계산
# def get_grade(a):
#     if a >= 90: return 'A'
#     if a >= 80: return 'B'
#     if a >= 70: return 'C'
#     return 'F'
    
# ans=get_grade(66)
# print(ans)

#가위바위보
import random
def get_gbb():
    r = random.randint(0,2)
    arr = '가위,바위,보'.split(',')#리스트형태로됨
    return arr[r]

ans = get_gbb()
print(ans)

def fac(n):
    if n==0:
        return 1
    return n * fac(n-1)

ans = fac(5)
print('fac(3)=',ans)
