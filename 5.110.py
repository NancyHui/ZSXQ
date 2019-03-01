import keyword

print(keyword.kwlist)


# *******************************************************
names = ["Adam", "Alex", "Martine", "Columbus"]

for name in names:
    print(name)
print("*******************************************")


# *****************************************************************************
def count(numbers):
    """
    输出列表数据
    :param numbers: 列表
    :return: 更新后的列表数据
    """
    sub_numbers = []
    for n in numbers:
        if n % 3 == 0 and n % 5 == 0:
            sub_numbers.append("FizzBuzz")
            print("FizzBuzz")
        elif n % 3 == 0:
            print("Fizz")
        elif n % 5 == 0:
            print("Buzz")
        else:
            print(n)


# range(a, b) [a, b)
numbers = range(1, 101)
count(numbers)


# ************************************************************
def count_small(nums):
    """
    列表中小于10的数字个数
    :param nums: 列表
    :return: 列表中小于10的数字个数
    """
    total = 0
    for n in nums:
        if n < 10:
            total += 1
    return total


nums = range(1, 21)
print(count_small(nums))


# *****************************************************
word = "Programming is funny!"
# 输出"!"
for letter in word:
    if letter == "!":
        print(letter)
