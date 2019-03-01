def value(key, scores, name):
    """
    为字典中的空列表赋值
    :param key: 需要赋值的键值
    :param scores: 分数 list
    :param name: 字典名称
    :return:赋值的列表值
    """
    if key in name:
        for score in scores:
            name[key].append(score)
    return name[key]


def iteral_name(students):
    """
    遍历每个学生（列表遍历）及其属性（字典遍历）
    :param students: 学生列表，每个学生为dict
    :return:
    """
    for student in students:
        for key in student:
            print(key + ": " + str(student[key]))


def average(numbers):
    """
    列表中所有元素的平均值
    :param numbers: list
    :return: 列表元素的平均值
    """
    # 列表元素求和，使用sum(list)
    total = sum(numbers)
    length = len(numbers)
    if length > 0:
        average = total/length
    return average


def get_average(student):
    """
    过权重计算后的平均分
    :param student: 学生成绩单 dict，传入的值可以是lilei,hanmeimei,jim
    :return: 该学生经过权重计算后的平均分
    """
    homework = average(student["homework"])
    quizzes = average(student["quizzes"])
    tests = average(student["tests"])
    total = homework * 0.1 + quizzes * 0.3 + tests * 0.6
    return total


def get_letter_score(score):
    """
    根据分数输出对应的等级
    :param score: 加权分数
    :return: 等级
    """
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


def get_class_average(class_list):
    """
    班级平均分：每个学生加权平均分后的班级平均分
    :param class_list: list，由dict组成的list
    :return: 班级平均分
    """
    result = []
    for student in class_list:
        result.append(get_average(student))
    average_class = average(result)
    return  average_class

lilei = {
    "name": "Lilei",
    "homework": [],
    "quizzes": [],
    "tests": [],
}
hanmeimei = {
    "name": "Hanmeimei",
    "homework": [],
    "quizzes": [],
    "tests": [],
}
jim = {
    "name": "Jim",
    "homework": [],
    "quizzes": [],
    "tests": [],
}

value("homework", name=lilei, scores=[90, 97, 75, 92])
value("quizzes", name=lilei, scores=[88, 40, 94])
value("tests", name=lilei, scores=[75, 90])
print(lilei)

value("homework", name=hanmeimei, scores=[100, 92, 98, 100])
value("quizzes", name=hanmeimei, scores=[82, 83, 91])
value("tests", name=hanmeimei, scores=[89, 97])
print(hanmeimei)

value("homework", name=jim, scores=[0, 87, 75, 22])
value("quizzes", name=jim, scores=[0, 75, 78])
value("tests", name=jim, scores=[100, 100])
print(jim)

students = [lilei, hanmeimei, jim]

for student in students:
    print("{}加权平均分：{}".format(student["name"], get_average(student)))
    print("{}成绩等级评定：{}".format(student["name"], get_letter_score(get_average(student))))

print("班级平均分：{}".format(get_class_average(students)))
print((80.55+79.9+91.1499999999999)/3)