def remove_deplicates(s):
    """
    删除列表中的重复元素
    :param s: 列表
    :return: 列表
    """
    t = []
    for i in range(len(s)):
        if s[i] in t:
            continue
        else:
            t.append(s[i])
    return t


x = [1, 1, 2, 2]
print(remove_deplicates(x))