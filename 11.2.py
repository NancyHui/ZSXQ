class Animal:
    # 类属性
    is_alive = True
    health = "good"

    # 实例属性
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def description(self):
        print("The name is {}".format(self.name))
        print("The age is {}".format(self.age))


zebra = Animal("Jeffrey", 2)
zebra.description()


# class Square(object):
#     def __init__(self):
#         self.sides = 4
#
#
# my_square = Square()
# print(my_square.sides)


# 购物车
class ShoppingCart(object):
    def __init__(self, customer_name):
        self.customer_name = customer_name
        self.items_in_cart = {}

    def add_item(self, product, price):
        if product not in self.items_in_cart:
            self.items_in_cart[product] = price
            print("{} is added into shopping cart".format(product))
        else:
            print("{} is already in the shoppingcart!".format(product))

    def remove_item(self, product):
        if product in self.items_in_cart:
            del self.items_in_cart[product]
            print("{} is removed from the shoppingcart!".format(product))
        else:
            print("{} is not in the shoppingcart!".format(product))


my_cart = ShoppingCart("Harry")
my_cart.add_item("iPhone", 9000)
my_cart.remove_item("ipad")
