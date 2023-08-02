print("welcome to island game. your mission is find the right way")

game = (input("you\'have choose right and left "))
game_lower_case = game.lower()
if game_lower_case == "left":
    wait = input("choose a do you want to wait or swim ")
    wait_lower_case = wait.lower()
    if wait_lower_case == "wait":
        color = input("you have to choose 1 door , red, yellow and white ")
        color_lower_case = color.lower()
        if color_lower_case == "yellow":
            print("you win")
        else:
            print("GAME OVER")
    else: 
        print("GAME OVER")
else:
    print("your in hole GAME OVER")



