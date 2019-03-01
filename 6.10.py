def list_fruit(prices, stock):
    """
    包含水果名称、单价、库存
    :param prices:水果价格 dict
    :param stock: 水果库存 dict
    :return:
    """
    # 两个字典的key是相同的，所以只需要遍历一个字典即可
    for key in prices:
    # for key in prices and stock:
        print(key)
        print("售价 {}".format(prices[key]))
        print("现有数量 {}".format(stock[key]))


def total_money(prices, stock):
    """
    库存水果的总价
    :param prices: 水果价格
    :param stock: 水果库存
    :return: 库存水果总价
    """
    total = 0
    for key in prices and stock:
        total += prices[key] * stock[key]
    return total


def compute_bill(prices, stock, food):
    """
    订单总价
    :param prices: 水果价格 dict
    :param stock: 水果库存 dict
    :param food: 订单 list
    :return:订单总价
    """
    total = 0
    for f in food:
        if f in prices and stock:
            if stock[f] > 0:
                total += prices[f]
                stock[f] -= 1
    return total


def compute_bill_1(prices, stock, food):
    """
    订单总价
    :param prices: 水果价格 dict
    :param stock: 水果库存 dict
    :param food: 订单 dict
    :return:订单总价
    """
    total = 0
    for f in food:
        if f in prices:

            if stock[f] - food[f] > 0:
                total += prices[f] * food[f]
                stock[f] -= food[f]
            else:
                total += prices[f] * stock[f]
                stock[f] = 0
    return total


prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3,
}
stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15,
}
list_fruit(prices, stock)
print(total_money(prices, stock))
food = ["banana", "orange", "apple"]
food_dict = {
    "banana": 8,
    "apple": 3,
    "orange": 2,
}

# print(compute_bill(prices, stock, food))
print(4 + 1.5)

print(compute_bill_1(prices, stock, food_dict))