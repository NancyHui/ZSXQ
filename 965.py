def purify(numbers):
    """
    删除列表中的奇数元素
    :param numbers: 整数列表
    :return: list
    """
    t = []
    for i in range(len(numbers)):
        if numbers[i] % 2 == 0:
            t.append(numbers[i])
    return t


num = [1, 2, 3]
print(purify(num))