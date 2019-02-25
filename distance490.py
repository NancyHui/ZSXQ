def distance_from_zero(n):
    """
    绝对值计算
    :param n: 任意数
    :return: 传入参数的绝对值或无法计算提示
    """
    if type(n) == int or type(n) == float:
        return abs(n)
    else:
        return "Error: Can not be calculated!"


# print("The result is {}".format(distance_from_zero((1))))
# # 元祖中只有一个元素，并且为int类型时（例如：(1)），type显示的类型是int
# # print(type((1)))