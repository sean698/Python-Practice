from turtle import Turtle, mode
FONT = ("Arial", 18, "normal")
ALIGN = "center"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("Snake Game/HighScore.txt") as file:
            self.high_score = int(file.read())
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.color("white")
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}, High score: {self.high_score}", align=ALIGN, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_score()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("Snake Game/HighScore.txt", mode="w") as file:
                file.write(f"{self.high_score}")
        self.update_score()
        self.score = 0

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("Game Over", align=ALIGN, font=FONT)
