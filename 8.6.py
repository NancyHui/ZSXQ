hobbies = []
for i in range(3):
    hobby = input("Please input your hobby")
    hobbies.append(hobby)
print(hobbies)

phrase = "A bird in the hand..."
for i in range(len(phrase)):
    if phrase[i].lower() == "a":
        print("X", end="")
    else:
        print(phrase[i], end="")
