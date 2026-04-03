# try:
#     list1 = [10,20,30]
#     n = list1[2]
#     print(n)
# except: print("오류가 발생했습니다")
# print("end")

list=['52','273','32','스파이','103']
list2 =[]
for i in list :
    try:
        float(i)
        list2.append(i)
    except:pass

print(f"{list}내부에 있는 숫자는")
print(f'{list2}입니다')