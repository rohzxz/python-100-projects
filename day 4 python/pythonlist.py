import random
# ramdom_integer = random.randint(1, 5)

# ramdom_float = random.random()

# print(ramdom_float * ramdom_integer + 1)

# t = random.randint(0, 1)
# if t == 1:
#     print("tails")
# else:
#     print("Heads")

# names_string = input("Give me everybody,s names, seperated by a comma. ")
# names = names_string.split(", ")
# count = len(names)
# random_name = random.randint(0, count - 1)
# print(f"{names[random_name]} is going to buy the meal today!")


# a = ["rohit", "mohit"]
# b = ["ram", "sita", "golu"]

# ab = [a, b]
# print(ab[1][1])
# 🚨 Don't change the code below 👇
# row1 = ["⬜️", "️⬜️", "️⬜️"]
# row2 = ["⬜️", "⬜️", "️⬜️"]
# row3 = ["⬜️️", "⬜️️", "⬜️️"]
# map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
# position = input("Where do you want to put the treasure? ")
# # 🚨 Don't change the code above 👆

# # Write your code below this row 👇

# horizon = int(position[0])
# vertical = int(position[1])

# selected_row =(map[vertical - 1])
# selected_row[horizon - 1] = "X"


# # Write your code above this row 👆

# # 🚨 Don't change the code below 👇
# print(f"{row1}\n{row2}\n{row3}")

import random

game = ['heads', 'tails']

randomchoice = random.choice(game)

print(randomchoice)
