# Task 1
class Triangle(object):
    # 类变量
    number_of_sides = 3

    # 实例变量
    def __init__(self, angle1, angle2, angle3):
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3

    def check_angles(self):
        angles = self.angle1 + self.angle2 + self.angle3
        if angles == 180:
            return True
        else:
            return False


tri = Triangle(30, 60, 80)
print(tri.number_of_sides)
print(tri.check_angles())


class Equilateral(Triangle):
    angle = 60

    def __init__(self):
        self.angle1 = self.angle
        self.angle2 = self.angle
        self.angle3 = self.angle


etri = Equilateral()
print(etri.check_angles())