i = 1
while i in range(1, 11):
    print(i**2)
    i += 1

# choice = input("喜欢课程吗？(y/n)")
# while choice != "y" and choice != "n":
#     choice = input("重新输入(y/nt)")

count = 0
while True:
    print(count, end='')
    count += 1
    if count >= 10:
        break


count1 = 0
while True:
    count1 += 1
    if count1 == 6:
        continue
    print(count1)
    if count1 >= 10:
        break