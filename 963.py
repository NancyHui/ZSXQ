# 屏蔽
# 类似于字符串中的replace()方法
# str.replace(old, new[, max])，replace() 方法把字符串中的 old（旧字符串） 替换成 new(新字符串)，
# 如果指定第三个参数max，则替换不超过 max 次。


def censor(text, word):
    """
    text中含有word的地方换成*，*个数=len(word)
    :param text:字符串
    :param word:字符串
    :return:
    """
    i = 0
    t = ""
    while i < len(text):
        if text[i] == word[0]:
            print(text[i: (i + len(word))])
            print("*" * len(word))
            if text[i: (i + len(word))] == word:
                t += "*" * len(word)
                print(t)
                i = i + len(word)
            else:
                t += text[i]
                i += 1
        else:
            t += text[i]
            i += 1
    return t


x = "this hack is wack hack!"
y = "hack"

print(censor(x, y))