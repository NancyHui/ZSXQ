# 倒序输出字符串


def reverse(text):
    """
    倒序输出字符串
    :param text: 字符串
    :return:
    """
    s = []
    for i in range(len(text)):
        print((len(text) - 1 - i))
        s.append(text[len(text) - 1 - i])
    return "".join(s)


t = "apple"
print(reverse(t))