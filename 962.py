# Scrabble积分
def scrabble_score(word):
    """
    指定字符串各字母分数的总和
    :param word: 任意字符串
    :return: 分数
    """
    total = 0
    score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
             "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
             "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
             "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
             "x": 8, "z": 10}
    lower_word = word.lower()
    for i in range(len(lower_word)):
        total += score[lower_word[i]]
    return total


x = "Helix"
print(scrabble_score(x))