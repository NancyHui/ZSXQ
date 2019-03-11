def count(sequence, item):
    """
    列表中含有指定item的次数
    :param sequence: 列表：由数字、字符串、列表组成
    :param item: 各种数据类型数据：数字（整数、浮点数）、字符串、列表。。。
    :return: 次数
    """
    total = 0
    for i in range(len(sequence)):
        # 判断当前元素是哪种数据类型，是否为列表？
        if item == sequence[i]:
            total += 1
    return total


print(count([1, 2, 1, 1], [1, 2]))