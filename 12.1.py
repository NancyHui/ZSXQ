my_list = [i**2 for i in range(1, 11)]
print(my_list)

my_file = open("output.txt", "w+")

for e in my_list:
    my_file.write(str(e) + "\n")

my_file.close()

with open("output1.txt", "a") as f:
    for e in my_list:
        f.write(str(e) + "\n")