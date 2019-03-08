# 质数问题


def is_prime(x):
    """
    判断是否为质数
    质数：大于1的自然数，只能被1和本身整除的数字
    :param x: 数字
    :return:
    -100, 0, 1 False
    2 True
    """
    # 遍历：除1和本身之外的其他数字
    if x > 1:
        for i in range(2, (x-1)):
            # 被整除了
            if x % i == 0:
                return False
        # 遍历所有数据之后，没有整除
        return True
    else:
        return False


from random import randint
n = randint(1, 100)
print(n)
print(is_prime(n))
