# Data types

# number = input()
# first = int(number[0])
# second = int(number[1])
# print(first + second)

# BMI = int(input("enter your height in kg "))
# BMI2 = float(input("enter your weight in m "))
# print(BMI / (BMI2 ** 2))


# print(round(8//3))
# age = input("What is your current age? ")
# ages_as_int = int(age)
# years = 90 - ages_as_int
# days = years * 365
# weeks = years * 52
# month = years * 12

# print(f"your {years} and {days} left and {weeks} {month}")


# print("welcome to the tip calculator")
# bill = float(input("what was the total bill? "))
# per = float(input("what percentage tip would you like to give? 10, 12 or 15 ?  "))
# split = int(input("How many people to split the bill? "))
# tip_total = float(bill / 100 * per)
# result = float((tip_total + bill)/7)
# print(round(result, 2))


# print("welcome to the rollercoaster ride")
# height = int(input("what is your height in fet? "))
# if height > 5:
#     print("you can ride the rollercoaster")
# else:
#     print("your dont have enough height")


# print("program even or odd")
# number = float(input("enter a number "))
# # result = ("{:.2f}".format(number))
# if number % 2 == 0:
#     print("this a even number")
# else:
#     print("this a odd number")

# number = input()
# first = int(number[0])
# second = int(number[1])
# print(first + second)

# BMI = int(input("enter your height in kg "))
# BMI2 = float(input("enter your weight in m "))
# result = round(BMI / (BMI2 ** 2))
# if result < 18.5:
#     print(f"your are underweight {result} ")
# elif result < 25:
#     print(f"your have normal weight {result}")
# elif result < 30:
#     print(f"you have overweight {result}")
# elif result < 35:
#     print(f"you are obese {result}")
# else:
#     print(f"your clinically obese {result}")

# year = int(input("Which year do you want to check? "))
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("this is leap years")
#         else:
#             print("this not a leap year")
#     else:
#         print("this a leap year")
# else:
#     print("not a leap year")

# print("Welcome python pizza deliveries ")
# size = input("what size pizza do you want? s, m or l ")
# add_pepperoni = input("Do you want pepperoni? ")
# extra_cheese = input("Do want extra cheese ")
# bill = 0
# if size == "s":
#     bill += 15
# elif size == "m":
#     bill += 20
# else:
#     bill += 25

# if add_pepperoni == "y":
#     if size == "s":
#         bill += 2
#     else:
#         bill += 3
# if extra_cheese == "y":
#     bill += 1

# print(f"your final bill is ${bill}")


# a = 4
# b = 4
# if a == 0 and b == 4:
#     print("this and operators")
# else:
#     print("nothing")


# print("welcome to the love Calculator")
# name1 = input("what is your name? \n")
# name2 = input("what is their name? \n")
# add_name = name1 + name2
# lower_case = add_name.lower()

# t = lower_case.count("t")
# r = lower_case.count("r")
# u = lower_case.count("u")
# e = lower_case.count("e")

# true = t + r + u + e

# l = lower_case.count("l")
# o = lower_case.count("o")
# v = lower_case.count("v")
# e = lower_case.count("e")

# love = l + o + v + e
# love_score = int(str(true) + str(love))

# if love_score < 10 or love_score > 90:
#     print(f"your score is {love_score}, you go together like coke and lime")
# elif love_score >= 40 and love_score <= 50:
#     print(f"your score is {love_score}, you are alright together")
# else:
#     print(f"your score is {love_score}")

# print("welcome to island game. your mission is find the right way")

# game = (input("you\'have choose right and left "))
# game_lower_case = game.lower()
# if game_lower_case == "left":
#     wait = input("choose a do you want to wait or swim ")
#     wait_lower_case = wait.lower()
#     if wait_lower_case == "wait":
#         color = input("you have to choose 1 door , red, yellow and white ")
#         color_lower_case = color.lower()
#         if color_lower_case == "yellow":
#             print("you win")
#         else:
#             print("GAME OVER")
#     else:
#         print("GAME OVER")
# else:
#     print("your in hole GAME OVER")
# import random
# string = input("names for pay bills for todays\n")
# names = string.split(", ")
# print(names)
# # cout = len(names)
# rodom = random.choices(names)
# print(rodom)
# names = ["rohit", "mohit", "abhi"]
# for name in names:
#     print(name)
# 🚨 Don't change the code below 👇
# student_heights = input("Input a list of student heights ").split()
# for n in range(0, len(student_heights)):
#     student_heights[n] = int(student_heights[n])
# print(student_heights)
# 🚨 Don't change the code above 👆
# sum = 0
# conter = 0
# for total in student_heights:
#     sum += total
#     conter += 1
# print(round(sum/conter))
# number = 0
# for high in student_heights:

#     if high > number:
#         number = high
# print(number)


# print(int(sum/len(student_heights)))


# Write your code below this row 👇
# 180, 124, 165, 173, 189, 169, 146
# sum = 0
# for number in range(1, 101):
#     sum += number
# print(sum)
# 🚨 Don't change the code below 👇
# student_heights = input("Input a list of student heights ").split()
# for n in range(0, len(student_heights)):
#   student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


# Write your code below this row 👇
# accum = 0
# for number in range(1, 101):
#     if number % 3 == 0 and number % 5 == 0:
#         print("FizzBuzz")
#     elif number % 3 == 0:
#         print("fizz")
#     elif number % 5 == 0:
#         print("Bizz")
#     else:
#         print(number)


# Password Generator Project
# import random
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
#            'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# print("Welcome to the PyPassword Generator!")
# nr_letters = int(input("How many letters would you like in your password?\n"))
# nr_symbols = int(input(f"How many symbols would you like?\n"))
# nr_numbers = int(input(f"How many numbers would you like?\n"))

# # Eazy Level - Order not randomised:
# # e.g. 4 letter, 2 symbol, 2 number = JduE&!91
# # Hard Level - Order of characters randomised:
# # e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

# password_list = []

# for char in range(1, nr_letters + 1):
#     password_list.append(random.choice(letters))
# for char in range(1, nr_symbols + 1):
#     password_list.append(random.choice(symbols))
# for char in range(1, nr_numbers + 1):
#     password_list.append(random.choice(numbers))
# random.shuffle(password_list)

# # password = ""
# # for char in password_list:
# #     password += char

# ans = "".join(password_list)
# print(ans)
# def my_fun():
#     print("hello")


# print("hello")
# Step 1
# import random
# word_list = ["aardvark", "baboon", "camel"]


# # TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

# chosen_word = random.choice(word_list)
# print(chosen_word)

# display = []
# word_length = len(chosen_word)
# for letter in chosen_word:
#     display += "_"
# print(display)
# # TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
# end_of_game = False
# while not end_of_game:
#     make_guess = input("guess a letter: ").lower()
# # TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
#     for position in range(word_length):
#         let = chosen_word[position]
#         if let == make_guess:
#             display[position] = let
#     print(display)

# if "_" not in display:
#     end_of_game = True
#     print("You Win ")

# def greet():
#     print("hello")
#     print("how do you do?")
#     print("hello")

# greet()


# def greed_with(name, location):
#     print(f"what is name{name}")
#     print(f"where is the your {location}")


# greed_with(" jadam", "  sikar")

# Write your code below this line 👇

import math


def paint_calc(height, width, cover):
    area = height * width
    number_of_cans = math.ceil(area / cover)
    print(f"you'll need {number_of_cans}")

    # Write your code above this line 👆
    # Define a function called paint_calc() so that the code below works.

    # 🚨 Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5


paint_calc(height=test_h, width=test_w, cover=coverage)
