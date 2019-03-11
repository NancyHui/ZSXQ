# 去掉首字母
def anti_vowel(text):
    """
    去掉元音字母 a,e,i,o,u
    :param text: 任意字符串
    :return: 去掉元音字母的字符串
    """
    s = []
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    # lower_text = text.lower()
    for i in range(len(text)):
        if text[i] in vowels:
            continue
        else:
            s.append(text[i])
    print(s)
    return "".join(s)


x = "HEY YOU!"
print(anti_vowel(x))
