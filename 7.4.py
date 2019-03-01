for i in range(3):
    print(i)

print(list(range(3)))


# 复制列表的两种方法，遍历列表的两种方法：下标、元素
def my_function(x):
    """
    复制列表，利用下标
    :param x:原始列表
    :return:复制的列表
    """
    y = []
    # 遍历时可以修改列表内的元素
    for i in range(0, len(x)):
        y.append(x[i])
    return y


def copy_list(x):
    """
    复制列表 利用元素
    :param x:原始列表
    :return:复制的列表
    """
    y = []
    # 遍历时不可以修改列表内的元素
    for element in x:
        y.append(element)
    return y


# ******************************************************
def total(numbers):
    """
    列表中各元素求和
    :param numbers:列表
    :return: 求和
    """
    result = 0
    for i in range(len(numbers)):
        result += numbers[i]
    return result


# ***************************************************************
def join_string(words):
    """
    将列表中每一个单词都加入到字符串中，单词之间没有空格
    :param words:列表
    :return: 字符串
    """
    result = ""
    for i in range(len(words)):
        result += words[i]
    return result


print(my_function(list(range(3))))
print(copy_list(list(range(3))))

print(total(list(range(0, 11))))
print(sum(list(range(0, 11))))

n = ["Michael", "Lieberman"]
print(join_string(n))