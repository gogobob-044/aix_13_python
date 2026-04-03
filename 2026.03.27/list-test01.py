#댄스동아리회원관리
names = ['홍','김','박'] 
print(names[0])
print(names[1:2]) #김
print(names[1:]) #김 박
#->새로운 리스트가 반환됨
n = names[1:] #복사본 생성

names[1] = '이'
print(names) #원본 수정
#리스트 이중접근
print(names[1:][1]) #[이 박][1] -> 박
print(n[0]) # 김

arr = [[1,2,3], [4,5,6]]
print(arr[0]) #[1,2,3]
print(arr[0][1])

a=[10,20,30]
b=[40,50,60]
print(a+b)
print(a*3)
print(f"홍길동의길이={len("홍길동")}")
print(len(a+b))