# 数字求和


def digit_sum(n):
    """
    正整数各个位数上的数字之和
    :param n:正整数
    :return: 和
    """
    total = 0
    # 正数
    if n > 0:
        remainder = (n * 10) % 10
        # 整数
        if remainder == 0:
            # if n < 10:
            #     total = n
            # else:
            #     while n > 10:
            #         n_remainder = n % 10
            #         total += n_remainder
            #         n = int(n / 10)
            #     total += n
            # return total
            while n > 10:
                n_remainder = n % 10
                total += n_remainder
                # n = int(n / 10)
                n = n // 10
            total += n

        else:
            print("Please enter integer!")
    else:
        print("Please enter positive number!")
    return total


x = 1234
print(digit_sum(x))


# https://blog.csdn.net/oh5W6HinUg43JvRhhB/article/details/79165250
def digit_sum1(y):
    """
    递归
    :param y:
    :return:
    """
    if y == 0:
        return 0
    return digit_sum1(y // 10) + y % 10


print(digit_sum1(x))


def digit_sum2(y):
    """
    函数式编程
    :param y:
    :return:
    """
    return sum(map(int, str(y)))
# map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回



print(digit_sum2(x))
print(map(int, str(x)))
print(int(str(x)))
print(str(x))
