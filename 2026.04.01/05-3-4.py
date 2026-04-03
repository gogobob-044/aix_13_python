# def power(item):
#     return item*item

# list1=[1,2,3,]
# r1=map(power,list1)
# list2 = '10,20,30'.split(',')
# print(list2)
# list3=[int(i) for i in list2]
# def to_int(c):
#     return int(c)
# r2 = map(to_int, list2)
# print(list(r2))

# #짝수만 추출
# list4 = [i for i in list1 if i%2==0 ]
# #list4=[]
# # for i in list1:
# #     if i52==0:
# #         list4.append(i)

# def only_even(i): #짝수
#     return i %2==0 #True인 애들만 반환 

# list4 = filter(only_even, list1)
# print(list4)
# print(type(list4))
# print(list(list4))

# names ='홍길동,김길동,박길동'.split(',')
# #김씨만 추출

# def only_kim(i):
#     return i[0] == '김'

# kims = filter(only_kim,names)
# print(list(kims))

power = lambda x:x*x
print(power(3))
#단축
map(lambda x:x*x, [1,3,5])

