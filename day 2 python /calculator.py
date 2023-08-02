print("welcome to the tip calculator")
bill = float(input("what was the total bill? "))
per = float(input("what percentage tip would you like to give? 10, 12 or 15 ?  "))
split = int(input("How many people to split the bill? "))
tip_total = float(bill / 100 * per)
result = float((tip_total + bill)/7)
print(round(result, 2))




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