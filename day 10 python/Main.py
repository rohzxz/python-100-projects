# print("hello")  
# def format_name(f_name, l_name):
#  """Take a first and last name and format
#  it"""
 
#  if f_name == "" or l_name =="":
#   return("you did,t provide valid input")
#  lol1 = f_name.title()
#  lol2 = l_name.title()
#  return f"{lol1} {lol2}"

# print(format_name(input("what is your first name? "),input("what is your last name ")))


# def is_leap(year):
#   if year % 4 == 0:
#     if year % 100 == 0:
#       if year % 400 == 0:
#         return True
#       else:
#         return False
#     else:
#       return True
#   else:
#     return False
  
# # TODO: Add more code here 👇
# def days_in_month(year,month):
#   month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
#   if month == 2 and is_leap(year):
#     return 29
#   else:
#     return month_days[month - 1]

  
# #🚨 Do NOT change any of the code below 
# year = int(input()) # Enter a year
# month = int(input()) # Enter a month
# days = days_in_month(year, month)
# print(days)

def add(n1,n2):
  return n1+n2
def subtract(n1,n2):
  return n1-n2
def multiply(n1,n2):
  return n1*n2
def divide(n1,n2):
  return n1/n2

operations = {
  "+":add,
  "-":subtract,
  "*":multiply,
  "/":divide
}



def cal():
  num1 = float(input("what's the first number: "))
  for opr in operations:
    print(opr)
  should_continue =True

  while should_continue:
    operation_symbol =input("pick an operation: ")
    num2 = float(input("what's the next number: "))
    calculaion =operations[operation_symbol]
    answer = calculaion(num1,num2)
    # round_result = round(answer)

    print(f"{num1} {operation_symbol}{num2} {round_result}")

    if input("Type 'y' to continue calculating with {answer}, or type 'n' to new cal.: ") =="y":
     num1= answer
    else:
     should_continue = False
     cal()
cal()


