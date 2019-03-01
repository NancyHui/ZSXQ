choices = ["pizza", "pie", "salad", "chips"]
for index, item in enumerate(choices, 1):
    print(index, item)

list_a = [3, 9, 17, 15, 19]
list_b = [2, 4, 8, 10, 30, 40, 50, 60, 70, 80, 90]
list_c = [1, 2, 3]

for a, b in zip(list_a, list_b):
    if b >= a:
        print(b)
    else:
        print(a)
for a, b, c in zip(list_a, list_b, list_c):
    if c <= a and c <= b:
        print(c)
    else:
        print(a)
