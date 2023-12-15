# Review:
# Create a function called greet().
# Write 3 print statements inside the function.
# Call the greet() function and run your code.


# def greet():
#     print("hello")
#     print("hello")
#     print("hello")


# greet()


# Write your code below this line 👇
def prime_checker(number):
    if number % 2 == 0 or number % 3 == 0:
        print("this is a not prime number")
    else:
        print("this is prime number")

# Write your code above this line 👆


# Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
