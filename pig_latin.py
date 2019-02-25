# 屏幕输入
word = input('Please enter a word')

# 检查用户输入是否为英文单词：word不为空，并且使用isalpha()方法检查是否为英文单词
if len(word) > 0 and word.isalpha():
    pyg = 'ay'
    lower_word = word.lower()
    first = lower_word[0]
    new_word = lower_word + first + pyg
    new_word = new_word[1:]
    print("The Pig Latin word is {}".format(new_word.lower()))
else:
    print("Invalid input")

