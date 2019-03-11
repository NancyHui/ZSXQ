def product(numbers):
    """
    整数列表各元素的乘积
    :param numbers: 整数列表
    :return: 各元素乘积
    """
    pro = 1
    length = len(numbers)
    if length != 0:
        for i in range(length):
            pro *= numbers[i]
    return pro


num = [4, 6, 5]
# num = []
print(product(num))
