from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)

start_x = 0
start_y = 0
segments = []

for n in range(3):
    new_turtle = Turtle(shape="square")
    new_turtle.penup()
    new_turtle.color("white")
    new_turtle.goto(x=start_x, y=start_y)
    start_x -= 20
    segments.append(new_turtle)

screen.update()
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    for n in range(len(segments)-1, 0, -1):
            position = segments[n-1].pos()
            segments[n].goto(position)
    segments[0].forward(20)








screen.exitonclick()