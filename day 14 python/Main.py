import random
from art import logo, vs
from game_data import data


def format_data(account):
    random_name = account["name"]
    random_descr = account["description"]
    random_country = account["country"]
    return f"{random_name}, a{random_descr}, from {random_country}"


def check_answer(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


print("day 14 for python")
print("welcome to game call right or wrong")
print(logo)
score = 0
game_should_continue = True

while game_should_continue:
    random1 = random.choice(data)
    random2 = random.choice(data)
    if random1 == random2:
        random2 = random.choice(data)

    print(f"compare A:{format_data(random1)}")
    print(vs)
    print(f"Against B:{format_data(random2)}")

    guess = input("who has more followers?Type 'A'or 'B': ").lower()

    a_follower_count = random1["follower_count"]
    b_follower_count = random2["follower_count"]
    # a_follower_count = account_a["follower_count"]
    # b_follower_count = account_b["follower_count"]
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    if is_correct:
        score += 1
        print(f"You are right! Current score:{score}.")
    else:
        game_should_continue = False
        print(f"sorry, that,s wrong.final score{score}")
