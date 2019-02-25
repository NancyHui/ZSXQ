def coupon(origin_price):
    """
    满80减20
    :param origin_price:原价
    :return: 实际价格
    """
    new_price = origin_price - (origin_price/80)*20
    print("优惠价格为：{}".format(new_price) )
    return new_price


def discount(origin_price):
    """
    85%
    :param origin_price: 原价
    :return: 实际价格
    """
    new_price = origin_price * 0.85
    print("打折价格为：{}".format(new_price))
    return new_price


coupon(315)
discount(315)


# **********************************************************************
def square(number):
    """
    计算平方
    :param number: 值
    :return: 平方值
    """
    num = number**2
    # print("平方值为：{}".format(num))
    return num


print("平方值为：{}".format(square(10)))


# *****************************************
def power(base, exponent):
    """
    计算base的exponet次方
    :param base: 基数
    :param exponent: 平方数
    :return: 结果
    """
    num = base ** exponent
    return num


print("乘方结果为：{}".format(power(35, 3)))


# ******************************************
def add_one(n):
    num = n + 1
    return num


def add_two(n):
    # 方法调用方法
    num = add_one(n) + 1
    return num


print("The result is {}".format(add_two(1)))