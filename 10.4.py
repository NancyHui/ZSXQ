languages = ["HTML", "JavaScript", "Python", "Ruby"]
print(list(filter(lambda x: x == "Python", languages)))


squares = [i**2 for i in range(1, 11)]
print(squares)

print(list(filter(lambda x: 30 < x < 70, squares)))

my_list = range(1, 11)
print(list(my_list[::2]))
print([i for i in my_list[::2]])

