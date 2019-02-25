def grade_conventer(grade):
    if grade >= 90:
        print("优秀")
    elif 80 <= grade <= 89:
        print("良好")
    elif 70 <= grade <= 79:
        print("尚可")
    elif 60 <= grade <= 69:
        print("及格")
    else:
        print("不及格")


grade = 70
grade_conventer(grade)