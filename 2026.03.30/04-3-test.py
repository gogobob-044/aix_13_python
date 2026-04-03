# print(range(3))
# print(list(range(3))) #list 함수로 둘러싸면 실제 값이 리스트로 나옴
# print(list(range(1,46)))
# print(list(range(1,46,5))) #5씩 증가
# print(list(range(5,1,-1))) #거꾸로 #정수만 됨

# ### 3단 구구단 출력
# for i in range(1,10):
#     print(f"3*{i}={3*i}")
# #    
# dan =3
# for i in range(1,10):
#     print(f"{dan}*{i}={dan*i}")


# #중첩반복문 ex)구구단
# for i in range(2,10):
#     for j in range(1,10) :
#         print(f"{i}*{j}={i*j}")

#while

# i = 0
# while i<3: #i가 3보다 작은 동안 실행
#     print(f'i={i}')
#     i += 1 #이거 생략하면 무한반복 ctrl+c로 종료
# print(f'while end i={i}')
# print("end")

# i =0
# while i < 10:
#     print(f'i={i}')
#     i += 1
#     if i == 2:
#         break

####
# ns=[5,15,6,20,7,25]
# for n in ns:
#     if n<10 :
#         continue
#     print(n)


#####함수
a=[5,1,3]
# print(min(a))
# print(max(a))
# print(sum(a))
# print('avg=',sum(a)/len(a))
# a.sort()
# print('sorted',a)
# r=reversed(a) #iterator 반환
# for v in r: #r->반복자(iterator)
#     print(v)

###리스트 내포(많이 씀)
# array= [i*i for i in range(0,20,2)]
# print(array)

# a=[1,3,5]
# b=[i*10 for i in a]
# print(b)

#짝수만 추출
# [i for i in range(10) if i%2==0]
# print(a)

# a=list("12345")
# print(a)
# print("-".join("12345"))

# # a = ['1','2','3']
# a = [1,2,3] #오류
# a=[str(n) for n in a] #내포
# print("-".join(a)) #1은 숫자, -는 문자이기떄문에

#짞수홀수변환
# a = range(1,6)
# #[ 참일때값 if 조건식 else 거짓일때닶 for 변수 in 자료구조]
# b = [ '짝' if n %2 ==0 else '홀'
#              for n in a ]
# print(b)

