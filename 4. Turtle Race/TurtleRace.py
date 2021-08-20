from turtle import Turtle, Screen
from random import randint

screen = Screen()
screen.setup(width=500, height=400)
user_choice = screen.textinput("Make your bet", "Which turtle will win the race? Enter a color: ")
color = ["red", "blue", "green", "black", "purple", "brown"]
initial_y = [-100, -60, -20, 20, 60, 100]
all_turtles = []


def game_initial():
    for turtle_index in range(6):
        turtle = Turtle("turtle")
        turtle.penup()
        turtle.color(color[turtle_index])
        turtle.goto(-230, initial_y[turtle_index])
        all_turtles.append(turtle)

def get_rand_distance():
    return randint(0, 10)

def check_gameover(turtle):
    if turtle.xcor() >= 220:
        return True

def check_user_bet(user_bet, turtle_color):
    if user_bet == turtle_color:
        print(f"You win! The winner is the {turtle_color} turtle.")
    else:
        print(f"You lose. The winner is the {turtle_color} turtle.")


def play():
    game_initial()
    is_game_over = False
    while not is_game_over:
        for turtle in all_turtles:
            if check_gameover(turtle):
                is_game_over = True
                check_user_bet(user_choice, turtle.pencolor())
                break
            turtle.forward(get_rand_distance())
            

play()
screen.exitonclick()