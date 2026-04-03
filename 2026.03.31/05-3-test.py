# t1 = (1,3,5)
# print(t1)
# print(t1[1]) #3
# print(type(t1))
# # t1[1] = 4 #오류 변경 불가능
# t2 =[3]
# print(type(t2))
# t2=(3)
# print(type(t2))
# t2=(3,)
# print(type(t2))

def calc_total_avg(*v):
    total=0
    avg=0
    total = sum(v)
    avg = total/len(v)
    return total, avg #(),[] 써도됨
t, a = calc_total_avg(10,30,50)
print('total',t)
print('avg',a)

a,b=10,20
print(a,b)
a,b=b,a
print(a,b)

print(calc_total_avg)
#<function calc_total_avg at 0x000001CC58C3FD70> 메모리주소
#함수 이름에 해당하는 변수 만들어짐

def print_func(fn):
    fn();fn();fn()
def hello():
    print("hello")
print_func(hello)
#hello의 주소를 print_func(fn)의 fn으로 보냄