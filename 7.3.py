def list_function(x):
    """
    列表第二个元素+3后的列表
    :param x: list
    :return: 列表第二个元素+3后的列表
    """
    x[1] += 3
    x.append(9)
    return x


def double_list(y):
    """
    列表元素乘以2
    :param y: 列表
    :return: 新列表
    """
    # 该表列表值的时候，需新建一个空列表，
    z = []
    for i in y:
         z.append(i*2)
    return z


n = [3, 5, 7]
print(list_function(n))
print(double_list(n))

