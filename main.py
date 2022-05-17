import turtle
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=1000, height=1000)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
border = turtle.Turtle()
border.hideturtle()
border.penup()
border.goto(-310, 310)
border.pd()
border.color("white")
for i in range(4):
    border.forward(620)
    border.rt(90)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")

game_is_on = True

while game_is_on:
    screen.update()
    speed = 0.1
    time.sleep(speed)

    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()
        speed *= 0.9
    scoreboard.update_scoreboard()
    if snake.head.xcor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() < -300 or snake.head.ycor() > 300:
        scoreboard.reset_score()
        speed = 0.1
        snake.reset_snake()

    for segment in snake.segments[2::]:
        if snake.head.distance(segment) < 3:
            scoreboard.reset_score()
            speed = 0.1
            snake.reset_snake()

screen.exitonclick()
