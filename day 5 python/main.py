# fruits =["apple", "peach", "pear"]
# for fruit in fruits:
#     print(fruit)
#     print()


# # 🚨 Don't change the code below 👇
# student_heights = input("Input a list of student heights ").split()
# for n in range(0, len(student_heights)):
#   student_heights[n] = int(student_heights[n])
# # 🚨 Don't change the code above 👆


# #Write your code below this row 👇
# sum_number  = 0
# for height in student_heights:
#    sum_number += height
# sums = (sum_number)

# number_of_students =0
# for sum in student_heights:
#    number_of_students += 1
# count  = (number_of_students)
# print(round(sums / count))


# 🚨 Don't change the code below 👇
# student_heights = input("Input a list of student heights ").split()
# for n in range(0, len(student_heights)):
#   student_heights[n] = int(student_heights[n])
# #   print(student_heights)
# # 🚨 Don't change the code above 👆


# big_number = 0
# for x in student_heights:
#   if x > big_number:
#     big_number = x
# print(big_number)
# sum = 0
# for number in range(1, 101):
#     # print(number)
#     sum += number
# print(sum)

# total = 0
# for sum in range(2, 101, 2):
#     total += sum
#     # print(sum)
# print(total)

for result in range(1, 101):
    if result % 3 == 0 and result % 5 == 0:
        print("FizzBuzz")
    elif result % 5 == 0:
        print("buzz")
    elif result % 3 == 0:
        print("Fizz")
    else:
        print(result)
