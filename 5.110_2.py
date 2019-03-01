def count(numbers):
    """
    输出列表
    :param numbers: 列表
    :return: 更新后的列表
    """
    sub_numbers = []
    for n in numbers:
        if n % 3 == 0 and n % 5 == 0:
            sub_numbers.append("FizzBuzz")
            # print("FizzBuzz")
        elif n % 3 == 0:
            sub_numbers.append("Fizz")
            # print("Fizz")
        elif n % 5 == 0:
            sub_numbers.append("Buzz")
            # print("Buzz")
        else:
            sub_numbers.append(n)
            # print(n)
    return sub_numbers

# # range(a, b) [a, b)
# numbers = range(1, 101)
# print(count(numbers))


def fizz_count(kindles):
    """
    列表中"Fizz"的个数
    :param kindles: 列表
    :return: 个数
    """
    ins = 0
    for kindle in kindles:
        if kindle == "Fizz":
            ins += 1
    return ins


kindles = count(range(1, 101))
print(fizz_count(kindles))
print(kindles)
