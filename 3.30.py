def result(statement):
    if statement:
        print('The result is True!')
    else:
        print('The result is False!')


# 顺序：not, or, and
# and: 一假则假     or: 一真则真
statement1 = not not True or False and not True
result(statement1)