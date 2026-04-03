# file = open("basic.txt", "w")

# file.write("Hello Python PRogramming")
# input('enter 누르세요')
# file.close()
# print('end')

with open("basic.txt", "a") as file:
    file.write("\n")
    file.write("heellooooo")
    file.writelines()
print('end')