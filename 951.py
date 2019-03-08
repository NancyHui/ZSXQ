# 偶数问题
# 偶数包含正偶数、负偶数和0


def is_even(x):
    """
    偶数问题
    :param x: 数字
    :return:
    """
    remainder = x % 2
    print(remainder)
    if remainder == 0:
        return True
    else:
        return False


num = -8
print(is_even(num))
