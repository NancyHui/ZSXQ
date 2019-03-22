list_a = [i**2 for i in range(1, 11)]
print(list_a)
print(list_a[2: 9: 4])

my_list = list(range(1, 11))
print(my_list[:: 2])
print(my_list[:: -1])

to_one_hundred = list(range(101))
print(to_one_hundred[::-10])


to_21 = list(range(1, 22))
print(to_21)
odds1 = [x for x in to_21 if x % 2 == 1]
odds2 = to_21[::2]
print(odds1)
print(odds2)

l = len(to_21)//3
print(l)
middle_list = to_21[l:l*2]
print(middle_list)

middle_list2 = [to_21[i] for i in range(l, l*2)]
print(middle_list2)




