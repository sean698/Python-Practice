import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "States Game/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("States Game/50_states.csv")
all_states = data["state"].to_list()
guessed_states = []

# Get user's guess
def popup_prompt():
    user_guess = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name?").title()
    return user_guess

# Get the coordinates of the guess
def get_coor(guess):
    guess_row = data[data["state"] == guess]
    x = int(guess_row["x"])
    y = int(guess_row["y"])
    return (x, y)

# Write correct guesses onto the map
def write_answer(answer, coor):
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    t.goto(coor)
    t.write(answer, align="center", font=("Arial", 8, "normal"))

while len(guessed_states) < 50:
    guess = popup_prompt()
    if (guess in all_states) and (guess not in guessed_states):
        guess_coor = get_coor(guess)
        write_answer(guess, guess_coor)
        guessed_states.append(guess)
    if guess == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        df = pandas.DataFrame(missing_states)
        df.to_csv("States Game/missing_states.csv")
        break
