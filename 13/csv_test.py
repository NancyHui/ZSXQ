# https://blog.csdn.net/u011541946/article/details/71302254
# https://blog.csdn.net/melody113026/article/details/80757668
# https://www.cnblogs.com/meitian/p/4626455.html

# https://www.cnblogs.com/cloud-ken/p/8432999.html
import csv

with open("data.csv", "r", encoding="utf-8") as csvfile:
    read_csv = csv.reader(csvfile)
    for row in read_csv:
        print(row)
        print(type(row))
        print("price = {}".format(row[1]))
