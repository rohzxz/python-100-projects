# # name ={
# #     "bug":"programer"
# # }
# # name["bug"]= "a non programer make anything "
# # print(name["bug"])

# # for thing in name:
# #     print(thing)

# student_scores = {
#   "Harry": 81,
#   "Ron": 78,
#   "Hermione": 99, 
#   "Draco": 74,
#   "Neville": 62,
# }
# # 🚨 Don't change the code above 👆
# # TODO-1: Create an empty dictionary called student_grades.
# student_grades={}
# # TODO-2: Write your code below to add the grades to student_grades.👇
# for student in student_scores:
#     score = student_scores[student]
#     if score > 90:
#         student_grades[student] = "outstanding"
#     elif score >80:
#         student_grades[student]= "exceeds Expectations"
#     elif score >70:
#         student_grades[student]= "acceptable"
#     else:
#         student_grades[student]= "fail"


    
    
    


# # 🚨 Don't change the code below 👇
# print(student_grades)

# nesting dictionary in a dictionary
# travel_log ={
#     "france":{"city_visited":["paris", "lille", "dijon"],"total_visits":12},
#     "germany":["berlin", "hamburg","stuttgart"]
    
# }

# travel_log =[
#   {
# "country":"france",
# "cities_visited":["paris"],
# "total_visits":12
#   },
#   {
#       "country":"germany",
#       "cities_visited":["berlin","humburg","london"],
#       "total_visits":5
#   },
#  ]

country = input() # Add country name
visits = int(input()) # Number of visits
list_of_cities = eval(input()) # create list from formatted string

travel_log = [
  {
    "country": "France",
    "visits": 12,
    "cities": ["Paris", "Lille", "Dijon"]
  },
  {
    "country": "Germany",
    "visits": 5,
    "cities": ["Berlin", "Hamburg", "Stuttgart"]
  },
]
# Do NOT change the code above 👆

# TODO: Write the function that will allow new countries
# to be added to the travel_log. 
def add_new_country(name,times_visited,cities_visited):
    new_country={}
    new_country["country"] = name
    new_country["country"] = times_visited
    new_country["country"] = cities_visited
    # new_country["country"] = name
    travel_log.append(new_country)



# Do not change the code below 👇
add_new_country(country, visits, list_of_cities)
print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
print(f"My favourite city was {travel_log[2]['cities'][0]}.")
