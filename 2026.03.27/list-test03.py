names = []
scores = []

names.append('홍')
names.append('김')
scores.append(80)
scores.append(90)
print(names)
print(scores)
del names[1] #김 삭제
# names.pop(1)
# names.remove('김')
print(names)
scores.clear()
print(scores)

##########3
arr=[30,50,70,60,]
arr.sort() #오름차순
print(arr)
arr.sort(reverse=True) #내림차순
print(arr)