def cube(n):
    """
    立方计算
    :param n:任意数
    :return: 立方
    """
    num = n ** 3
    return num


def test_three(n):
    """
    能被3整除的数返回立方，否则返回False
    :param n:任意数
    :return:
    """
    if n%3 == 0:
        num = cube(n)
        return num
    else:
        return False


print("The result is {}".format(test_three(6)))


