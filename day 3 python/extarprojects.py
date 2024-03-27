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

number = int(input('witch number do want check? '))
if number % 2 == 0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")
