import turtle
from turtle import Turtle, Screen


timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("green")
for _ in range(4):
    timmy_the_turtle.forward(100)
    timmy_the_turtle.left(360)

# timmy_the_turtle.back(100)
# timmy_the_turtle.right(100)





screen = Screen()
screen.exitonclick()
