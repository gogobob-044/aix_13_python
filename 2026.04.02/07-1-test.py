# import math
# print(math.pi)

# from math import pi
# print(pi)

# import math as m
# print(m.pi)

# import random
# print(random.choice([1,2,3,4,5]))

# a = [1,2,3,4,5]
# random.shuffle(a)
# print(a)
# print(random.sample([1,2,3,4,5], k=2))

# import sys
# print(sys.getwindowsversion())

# import os
# print(os.name)

# dir = os.listdir()
# for d in dir:
#     print (d)

# import time
# print('지금부터 3초 정지합니다')
# time.sleep(3)
# print('END')

from urllib import request
target = request.urlopen ("https://www.naver.com/")
output = target.read()
print(output)