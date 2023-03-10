from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from game import Game
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
game = Game()
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
    if snake.head.distance(food) < 15:
        food.get_food()
        snake.grow()
        scoreboard.new_score()

    if snake.head.xcor() > 270 or snake.head.xcor() < -270 or snake.head.ycor() > 270 or snake.head.ycor() < -270:
        snake.reset()
        scoreboard.reset_score()
        food.reset_food()
        time.sleep(1)

    if snake.collision():
        snake.reset()
        scoreboard.reset_score()
        food.reset_food()
        time.sleep(1)


screen.exitonclick()
