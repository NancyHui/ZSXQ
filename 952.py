# 整数问题
# 数字包含两种：整数、浮点数

def is_int(x):
    """
    判断是否为整数
    :param x: 数字
    :return:
    """
    # 7.1*10%10 = 1.0，余数
    remainder = (abs(x) * 10) % 10
    print(remainder)
    if remainder == 0:
        return True
    else:
        return False


num = -1
print(is_int(num))