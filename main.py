import time
from turtle import Screen
from scoreboard import ScoreBoard
from food import Food
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game Written in Python")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()

    # detect collision with wall
    if snake.check_collision_with_wall():
        game_is_on = False
        scoreboard.game_over()

    # detect collision with tale
    if snake.detect_collision_with_tail:
        game_is_on = False
        scoreboard.game_over()

screen.exitonclick()
