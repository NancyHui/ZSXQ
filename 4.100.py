def hotel_cost(nights):
    """
    住宿费用
    :param nights:住几晚
    :return: 住宿费用
    """
    return nights * 488


def train_cost(city):
    """
    高铁费用
    :param city:目的地城市名称
    :return: 单程高铁费用
    """
    if city == "Shanghai":
        return 92.5
    elif city == "Nanjing":
        return 117.5
    elif city == "Suzhou":
        return 111.5
    elif city == "Xian":
        return 653.5


def rent_car_cost(days):
    """
    租车费用
    :param days:租车天数
    :return: 租车费用
    """
    price_per_day = 78
    total_car_cost = price_per_day * days
    if 3 < days < 7:
        return total_car_cost - 20
    elif days > 7:
        return total_car_cost - 67
    else:
        return total_car_cost


def trip_cost(city, days, spending_money):
    """
    总花费
    :param city: 目的地城市
    :param days: 天数
    :return: 总花费
    """
    # 车费应该是往返的
    total_cost = hotel_cost(days - 1) + train_cost(city)*2 + spending_money + rent_car_cost(days)
    return total_cost


print("The total cost is {}".format(trip_cost("Shanghai", 2, 4000)))
print("The total cost is {}".format(trip_cost("Xian", 5, 3000)))