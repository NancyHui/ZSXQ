# Task 1
class Customer(object):
    def __init__(self, customer_id):
        self.customer_id = customer_id

    def display_cart(self):
        print("The products in the cart are milk, apple.")


class ReturnedCustomer(Customer):
    def display_order_history(self):
        print("The history orders are No.234 and No.456")


monty_python = ReturnedCustomer("12345")
monty_python.display_cart()
monty_python.display_order_history()


# Task 2
class Shape(object):
    def __init__(self, number_of_sides):
        self.number_of_sides = number_of_sides

class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3


tri = Triangle(3, 4, 5)
print(tri)


# Task 3
class Employee(object):
    def __init__(self, name):
        self.name = name

    #   other这里代表的是Employee对象或者Boss对象
    def greet(self, other):
        print("Hello %s" % other.name)

    def calculate_wage(self, hours):
        self.hour = hours
        return 20.00 * hours


class Boss(Employee):
    def greet(self, other):
        print("Please go back to work, %s" % other.name)


class PartTimeEmployee(Employee):
    def calculate_wage(self, hours):
        self.hours = hours
        return 12.00 * hours
        # print("The wage is {}".format(wage))

    def full_time_wage(self, hours):
        self.hours = hours
        return super(PartTimeEmployee, self).calculate_wage(hours)


emp = Employee("Lily")
boss = Boss("Bush")
emp.greet(emp)
emp.greet(boss)
pemp = PartTimeEmployee("Lucy")
print(pemp.calculate_wage(2))
print(pemp.full_time_wage(10))