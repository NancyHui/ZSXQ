def median(x):
    """
    无序序列，中间数
    奇数个元素：中间数
    偶数个元素：中间两个数字的平均数
    :param x:
    :return:
    """
    y = sorted(x)
    length = len(x)
    divisor = length // 2
    remainder = length % 2
    # 偶数
    if remainder == 0:
        mediant = (y[divisor] + y[divisor - 1]) / 2
    # 奇数
    else:
        mediant = y[divisor]
    return mediant


# k = [7, 12, 3, 1, 6]
k = [7, 3, 1, 4]
print(median(k))

