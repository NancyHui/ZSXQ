a = [1, 2, 3]
b = [4, 5, 6]


def join_lists(x, y):
    """
    两个列表结合为一个新的列表：两种方法
    :param x:列表1
    :param y: 列表2
    :return: 结合的新列表
    """
    # #方法一：
    # z = []
    # for i in range(len(x)):
    #     z.append(x[i])
    # for i in range(len(y)):
    #     z.append(y[i])
    # 方法二：
    z = x + y
    return z


print(join_lists(a, b))
# **********************************************
list_of_lists = [[1, 2, 3], [4, 5, 6]]
# 遍历列表中所有子列表
for lis in list_of_lists:
    for l in lis:
        print(l)


def flatten(lists):
    """
    遍历和连接由子列表组成的列表，组成新的列表
    :param lists: 由子列表组成的列表
    :return: 由字列表元素组成的新列表
    """
    results = []
    for numbers in lists:
        for n in numbers:
            results.append(n)
    return results


n = [[i for i in range(1, 4)], [j for j in range(4, 10)]]
print(n)
print(flatten(n   ))