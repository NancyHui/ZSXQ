skill = "Python Syntax"

case_study = 13
points_per_case = 5

point_total = 100

# 记得使用 +=
point_total += case_study * points_per_case

print("I got " + str(point_total) + " points!")
print("I got %d points!" % (point_total))
print("I got {} points!".format(point_total))


#
initial_time = "6:32"
use_time = 6*1 + 3*0.5 + 6*3

times = initial_time.split(":")
hour = int(times[0])
minute = int(times[1])

minutes = minute + use_time
print(minutes)

if minutes > 60:
    hour += 1
    minute = minutes - 60
    print(str(hour) + ":" + str(minute))
else:
    minute = minutes
    print(str(hour) + ":" + str(minutes))


# 函数形式
# initial_time = "6:32"
# use_time = 6*1 + 3*0.5 + 6*3
#
#
# def current_time(initial_time, use_time):
#     times = initial_time.split(":")
#     hour = int(times[0])
#     minute = int(times[1])
#
#     minutes = minute + use_time
#     print(minutes)
#
#     if minutes > 60:
#         hour += 1
#         minute = minutes - 60
#         print(str(hour) + ":" + str(minute))
#     else:
#         minute = minutes
#         print(str(hour) + ":" + str(minutes))
#
#
# current_time(initial_time, use_time)

# print("%+10x" % 8)
# print("%04d"  % 5)
# print("%6.3f"  % 2.3)