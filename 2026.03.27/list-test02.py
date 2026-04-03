#로또번호 생성 - 난수
mylotto = [] #리스트: 중복값 허용, 순서 제공
import random
r=random.randint(1,45)
if r not in mylotto:
    mylotto.append(r)    
r=random.randint(1,45)
if r not in mylotto:
    mylotto.append(r)
r=random.randint(1,45)
if r not in mylotto:
    mylotto.append(r)
r=random.randint(1,45)
if r not in mylotto:
    mylotto.append(r)
    r=random.randint(1,45)
if r not in mylotto:
    mylotto.append(r)
    r=random.randint(1,45)
if r not in mylotto:
    mylotto.append(r)
    #중복되면 5개로 나옴


# mylotto.append(random.randint(1,45))
# mylotto.append(random.randint(1,45))
# mylotto.append(random.randint(1,45))
# mylotto.append(random.randint(1,45))
# mylotto.append(random.randint(1,45))
# mylotto.append(random.randint(1,45))
# print(mylotto)

