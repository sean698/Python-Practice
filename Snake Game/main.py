from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("My snake game")
# Turn off the animation
screen.tracer(0)

snake = Snake()
food = Food()
score_board = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")


is_game_over = False
while not is_game_over:
    # Tell the program when to redraw
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        score_board.increase_score()
        snake.increase_length()

    # Detect collision with wall
    if snake.head.xcor() > 280 or  snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() <-280:
        is_game_over = True
        score_board.game_over()

    # Detect collision with tail
    # If head collides with any segment in the tail, trigger game over
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            is_game_over = True
            score_board.game_over()
 
screen.exitonclick()