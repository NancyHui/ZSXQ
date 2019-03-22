# 列表推导式 [表达式 for 变量 in 列表 if 条件]
my_list = range(51)
print(list(my_list))
print([x for x in range(50)])


# 生成都是偶数的列表
print([x for x in range(51) if x%2==0])

even_squares = [x**2 for x in range(1, 12) if x % 2 == 0]
print(even_squares)

cubes_by_four = [y**3 for y in range(1,11) if y % 2 == 0]
print(cubes_by_four)
