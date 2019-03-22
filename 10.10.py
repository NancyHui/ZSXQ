my_dict = {"name":"Harry", "age": 10, "address": "London"}

print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())

for key in my_dict.keys():
# for key in my_dict:
    print("{} {}".format(key, my_dict[key]))


for key, value in my_dict.items():
    print(key + " " + str(value))
