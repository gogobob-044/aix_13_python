# #인사말함수
# def hello():
#     print("안녕하세요")

# hello()

# def hello_3():
#     print("안녕하세요")
#     print("안녕하세요")
#     print("안녕하세요")
# hello_3()

def hello_n(n=1,msg="안녕하세요", ㅜ=1): #n은 매개변수
    for i in range(n):
        print(msg)
        print("안녕하세요")
#hello_n(4)
hello_n(2,"방가방가")

def gugudan(n=2,m=-1):
    if m ==-1:
        for i in range(1,10):
            print(f"{n}*{i} = {n*i}")
    else:
        for j in range(n,m+1):
            for i in range(1,10):
                print(f"{j}*{i} = {j*i}")
gugudan(2,5)




