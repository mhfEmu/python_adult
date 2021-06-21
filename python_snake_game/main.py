from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Snake Game")
screen.bgcolor("black")
screen.tracer(0)

# TODO:1: Create a Snake Body
# has been created on SNAKE CLASS
# all_turtles = []
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# TODO:3: Control the snake
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    # TODO:2: Move the Snake
    snake.move()

    # TODO:4: Detect collision with food
    if snake.head.distance(food) < 15:
        # TODO:5: Create a Scoreboard
        food.refresh()
        snake.extend()
        scoreboard.increment_score()

# TODO:6: Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

# TODO:7: Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()
