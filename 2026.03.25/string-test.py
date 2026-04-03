#s1=s2
s1 = "abc"
s2 = 'abc'
#3겹은 줄바꿈 가능
s3 = """abc""" 
s4 = '''abc'''
s5 = '''
a
b
c
'''
print(s5)

#문자열 안에 '나1'를 넣으려면 안과 밖을 다르게
s6 = '"안녕"이라고함'
print(s6)

s7 = "Tom\’s Bear"
print(s7)
print(s6+s7)
print(s6+" "+s7)

s8= '홍길동'
print(s8+" "+s8+" "+s8)

print("홍길동 "*3)

print("홍길동"[0])
print("홍길동"[1])
print("홍길동"[2])

print(s8[0])

print("홍길동"[-1]) #끝에서 첫번째