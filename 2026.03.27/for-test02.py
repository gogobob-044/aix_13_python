#로또번호추출방법2
nums = list(range(1,46)) #1~45
print('nums',nums)
mylotto =[]
for a in [1,2,3,4,5,6]:
    #num에서 임의의 위치를 지정,저장,삭제
    import random
    r = random.randint(0,len(nums)-1) #지우고 저장
    mylotto.append(r)
    nums.pop(r) #저장한 번호 삭제,중복선택불가
mylotto.sort()
print('\n',mylotto)